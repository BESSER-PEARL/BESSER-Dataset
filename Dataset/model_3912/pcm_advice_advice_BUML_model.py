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
			EnumerationLiteral(name="in_"),
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
pcm_av_av_EObject = Class(name="pcm_av_av_EObject")
pcm_av_av_GlobalScopeGlobalScope = Class(name="pcm_av_av_GlobalScopeGlobalScope")
pcm_av_av_PerJoinPointScopePerJoinPointScope = Class(name="pcm_av_av_PerJoinPointScopePerJoinPointScope")
pcm_av_av_Advice = Class(name="pcm_av_av_Advice")
pcm_av_av_GlobalScope = Class(name="pcm_av_av_GlobalScope")
pcm_av_av_PerJoinPointScope = Class(name="pcm_av_av_PerJoinPointScope")
pcm_av_av_core_av_av_PCMRandomVariable = Class(name="pcm_av_av_core_av_av_PCMRandomVariable")
RandomVariable = Class(name="RandomVariable")
ClosedWorkload = Class(name="ClosedWorkload")
PassiveResource = Class(name="PassiveResource")
VariableCharacterisation = Class(name="VariableCharacterisation")
seff_performance_av_av_InfrastructureCall = Class(name="seff_performance_av_av_InfrastructureCall")
seff_performance_av_av_ResourceCall = Class(name="seff_performance_av_av_ResourceCall")
seff_performance_av_av_ParametricResourceDemand = Class(name="seff_performance_av_av_ParametricResourceDemand")
pcm_av_av_DummyClass = Class(name="pcm_av_av_DummyClass")
pcm_av_av_AdviceAdvice = Class(name="pcm_av_av_AdviceAdvice")
composition_av_av_EventChannelSinkConnector = Class(name="composition_av_av_EventChannelSinkConnector")
composition_av_av_AssemblyEventConnector = Class(name="composition_av_av_AssemblyEventConnector")
Loop = Class(name="Loop")
OpenWorkload = Class(name="OpenWorkload")
Delay = Class(name="Delay")
CommunicationLinkResourceSpecification = Class(name="CommunicationLinkResourceSpecification")
ProcessingResourceSpecification = Class(name="ProcessingResourceSpecification")
pcm_av_av_entity_av_av_ResourceProvidedRole = Class(name="pcm_av_av_entity_av_av_ResourceProvidedRole")
Role = Class(name="Role")
entity_av_av_ResourceInterfaceProvidingEntity = Class(name="entity_av_av_ResourceInterfaceProvidingEntity")
ResourceInterface = Class(name="ResourceInterface")
pcm_av_av_entity_av_av_InterfaceProvidingRequiringEntity = Class(name="pcm_av_av_entity_av_av_InterfaceProvidingRequiringEntity")
entity_av_av_InterfaceProvidingEntity = Class(name="entity_av_av_InterfaceProvidingEntity")
entity_av_av_InterfaceRequiringEntity = Class(name="entity_av_av_InterfaceRequiringEntity")
pcm_av_av_entity_av_av_InterfaceProvidingEntity = Class(name="pcm_av_av_entity_av_av_InterfaceProvidingEntity")
Entity = Class(name="Entity")
ProvidedRole = Class(name="ProvidedRole")
pcm_av_av_entity_av_av_InterfaceRequiringEntity = Class(name="pcm_av_av_entity_av_av_InterfaceRequiringEntity")
entity_av_av_Entity = Class(name="entity_av_av_Entity")
entity_av_av_ResourceInterfaceRequiringEntity = Class(name="entity_av_av_ResourceInterfaceRequiringEntity")
RequiredRole = Class(name="RequiredRole")
pcm_av_av_entity_av_av_ResourceInterfaceRequiringEntity = Class(name="pcm_av_av_entity_av_av_ResourceInterfaceRequiringEntity")
entity_av_av_ResourceRequiredRole = Class(name="entity_av_av_ResourceRequiredRole")
LoopAction = Class(name="LoopAction")
GuardedBranchTransition = Class(name="GuardedBranchTransition")
qos_performance_av_av_SpecifiedExecutionTime = Class(name="qos_performance_av_av_SpecifiedExecutionTime")
pcm_av_av_entity_av_av_ResourceInterfaceProvidingEntity = Class(name="pcm_av_av_entity_av_av_ResourceInterfaceProvidingEntity")
entity_av_av_ResourceProvidedRole = Class(name="entity_av_av_ResourceProvidedRole")
pcm_av_av_entity_av_av_ComposedProvidingRequiringEntity = Class(name="pcm_av_av_entity_av_av_ComposedProvidingRequiringEntity")
composition_av_av_ComposedStructure = Class(name="composition_av_av_ComposedStructure")
entity_av_av_InterfaceProvidingRequiringEntity = Class(name="entity_av_av_InterfaceProvidingRequiringEntity")
pcm_av_av_entity_av_av_NamedElement = Class(name="pcm_av_av_entity_av_av_NamedElement")
pcm_av_av_entity_av_av_ResourceInterfaceProvidingRequiringEntity = Class(name="pcm_av_av_entity_av_av_ResourceInterfaceProvidingRequiringEntity")
pcm_av_av_entity_av_av_Entity = Class(name="pcm_av_av_entity_av_av_Entity")
Identifier = Class(name="Identifier")
entity_av_av_NamedElement = Class(name="entity_av_av_NamedElement")
pcm_av_av_composition_av_av_DelegationConnector = Class(name="pcm_av_av_composition_av_av_DelegationConnector")
Connector = Class(name="Connector")
pcm_av_av_composition_av_av_Connector = Class(name="pcm_av_av_composition_av_av_Connector")
pcm_av_av_composition_av_av_ComposedStructure = Class(name="pcm_av_av_composition_av_av_ComposedStructure")
pcm_av_av_entity_av_av_ResourceRequiredRole = Class(name="pcm_av_av_entity_av_av_ResourceRequiredRole")
composition_av_av_AssemblyContext = Class(name="composition_av_av_AssemblyContext")
composition_av_av_ResourceRequiredDelegationConnector = Class(name="composition_av_av_ResourceRequiredDelegationConnector")
composition_av_av_EventChannel = Class(name="composition_av_av_EventChannel")
composition_av_av_Connector = Class(name="composition_av_av_Connector")
pcm_av_av_composition_av_av_ResourceRequiredDelegationConnector = Class(name="pcm_av_av_composition_av_av_ResourceRequiredDelegationConnector")
pcm_av_av_composition_av_av_EventChannel = Class(name="pcm_av_av_composition_av_av_EventChannel")
EventGroup = Class(name="EventGroup")
composition_av_av_EventChannelSourceConnector = Class(name="composition_av_av_EventChannelSourceConnector")
pcm_av_av_composition_av_av_EventChannelSourceConnector = Class(name="pcm_av_av_composition_av_av_EventChannelSourceConnector")
SourceRole = Class(name="SourceRole")
pcm_av_av_composition_av_av_EventChannelSinkConnector = Class(name="pcm_av_av_composition_av_av_EventChannelSinkConnector")
SinkRole = Class(name="SinkRole")
OperationProvidedRole = Class(name="OperationProvidedRole")
pcm_av_av_composition_av_av_RequiredDelegationConnector = Class(name="pcm_av_av_composition_av_av_RequiredDelegationConnector")
OperationRequiredRole = Class(name="OperationRequiredRole")
PCMRandomVariable = Class(name="PCMRandomVariable")
pcm_av_av_composition_av_av_ProvidedDelegationConnector = Class(name="pcm_av_av_composition_av_av_ProvidedDelegationConnector")
DelegationConnector = Class(name="DelegationConnector")
pcm_av_av_composition_av_av_AssemblyConnector = Class(name="pcm_av_av_composition_av_av_AssemblyConnector")
pcm_av_av_composition_av_av_AssemblyEventConnector = Class(name="pcm_av_av_composition_av_av_AssemblyEventConnector")
pcm_av_av_composition_av_av_SinkDelegationConnector = Class(name="pcm_av_av_composition_av_av_SinkDelegationConnector")
pcm_av_av_composition_av_av_AssemblyInfrastructureConnector = Class(name="pcm_av_av_composition_av_av_AssemblyInfrastructureConnector")
InfrastructureProvidedRole = Class(name="InfrastructureProvidedRole")
InfrastructureRequiredRole = Class(name="InfrastructureRequiredRole")
pcm_av_av_composition_av_av_ProvidedInfrastructureDelegationConnector = Class(name="pcm_av_av_composition_av_av_ProvidedInfrastructureDelegationConnector")
pcm_av_av_composition_av_av_RequiredInfrastructureDelegationConnector = Class(name="pcm_av_av_composition_av_av_RequiredInfrastructureDelegationConnector")
pcm_av_av_composition_av_av_RequiredResourceDelegationConnector = Class(name="pcm_av_av_composition_av_av_RequiredResourceDelegationConnector")
pcm_av_av_composition_av_av_SourceDelegationConnector = Class(name="pcm_av_av_composition_av_av_SourceDelegationConnector")
pcm_av_av_composition_av_av_AssemblyContext = Class(name="pcm_av_av_composition_av_av_AssemblyContext")
RepositoryComponent = Class(name="RepositoryComponent")
VariableUsage = Class(name="VariableUsage")
pcm_av_av_usagemodel_av_av_Workload = Class(name="pcm_av_av_usagemodel_av_av_Workload")
UsageScenario = Class(name="UsageScenario")
pcm_av_av_usagemodel_av_av_UsageScenario = Class(name="pcm_av_av_usagemodel_av_av_UsageScenario")
UsageModel = Class(name="UsageModel")
ScenarioBehaviour = Class(name="ScenarioBehaviour")
Workload = Class(name="Workload")
pcm_av_av_usagemodel_av_av_UserData = Class(name="pcm_av_av_usagemodel_av_av_UserData")
pcm_av_av_usagemodel_av_av_UsageModel = Class(name="pcm_av_av_usagemodel_av_av_UsageModel")
UserData = Class(name="UserData")
pcm_av_av_usagemodel_av_av_EntryLevelSystemCall = Class(name="pcm_av_av_usagemodel_av_av_EntryLevelSystemCall")
AbstractUserAction = Class(name="AbstractUserAction")
OperationSignature = Class(name="OperationSignature")
pcm_av_av_usagemodel_av_av_AbstractUserAction = Class(name="pcm_av_av_usagemodel_av_av_AbstractUserAction")
pcm_av_av_usagemodel_av_av_ScenarioBehaviour = Class(name="pcm_av_av_usagemodel_av_av_ScenarioBehaviour")
BranchTransition = Class(name="BranchTransition")
pcm_av_av_usagemodel_av_av_BranchTransition = Class(name="pcm_av_av_usagemodel_av_av_BranchTransition")
Branch = Class(name="Branch")
pcm_av_av_usagemodel_av_av_Branch = Class(name="pcm_av_av_usagemodel_av_av_Branch")
pcm_av_av_usagemodel_av_av_Loop = Class(name="pcm_av_av_usagemodel_av_av_Loop")
pcm_av_av_usagemodel_av_av_Stop = Class(name="pcm_av_av_usagemodel_av_av_Stop")
pcm_av_av_usagemodel_av_av_Start = Class(name="pcm_av_av_usagemodel_av_av_Start")
pcm_av_av_usagemodel_av_av_OpenWorkload = Class(name="pcm_av_av_usagemodel_av_av_OpenWorkload")
pcm_av_av_usagemodel_av_av_Delay = Class(name="pcm_av_av_usagemodel_av_av_Delay")
pcm_av_av_usagemodel_av_av_ClosedWorkload = Class(name="pcm_av_av_usagemodel_av_av_ClosedWorkload")
pcm_av_av_repository_av_av_PassiveResource = Class(name="pcm_av_av_repository_av_av_PassiveResource")
BasicComponent = Class(name="BasicComponent")
ResourceTimeoutFailureType = Class(name="ResourceTimeoutFailureType")
pcm_av_av_repository_av_av_BasicComponent = Class(name="pcm_av_av_repository_av_av_BasicComponent")
ImplementationComponentType = Class(name="ImplementationComponentType")
ServiceEffectSpecification = Class(name="ServiceEffectSpecification")
pcm_av_av_repository_av_av_ImplementationComponentType = Class(name="pcm_av_av_repository_av_av_ImplementationComponentType")
CompleteComponentType = Class(name="CompleteComponentType")
pcm_av_av_repository_av_av_RepositoryComponent = Class(name="pcm_av_av_repository_av_av_RepositoryComponent")
InterfaceProvidingRequiringEntity = Class(name="InterfaceProvidingRequiringEntity")
Repository = Class(name="Repository")
pcm_av_av_repository_av_av_ProvidedRole = Class(name="pcm_av_av_repository_av_av_ProvidedRole")
pcm_av_av_repository_av_av_Parameter = Class(name="pcm_av_av_repository_av_av_Parameter")
DataType = Class(name="DataType")
InfrastructureSignature = Class(name="InfrastructureSignature")
EventType = Class(name="EventType")
ResourceSignature = Class(name="ResourceSignature")
pcm_av_av_repository_av_av_DataType = Class(name="pcm_av_av_repository_av_av_DataType")
pcm_av_av_repository_av_av_Repository = Class(name="pcm_av_av_repository_av_av_Repository")
Interface = Class(name="Interface")
FailureType = Class(name="FailureType")
pcm_av_av_repository_av_av_Interface = Class(name="pcm_av_av_repository_av_av_Interface")
Protocol = Class(name="Protocol")
RequiredCharacterisation = Class(name="RequiredCharacterisation")
pcm_av_av_repository_av_av_RequiredCharacterisation = Class(name="pcm_av_av_repository_av_av_RequiredCharacterisation")
Parameter_ = Class(name="Parameter")
pcm_av_av_repository_av_av_EventGroup = Class(name="pcm_av_av_repository_av_av_EventGroup")
pcm_av_av_repository_av_av_EventType = Class(name="pcm_av_av_repository_av_av_EventType")
Signature = Class(name="Signature")
pcm_av_av_repository_av_av_Signature = Class(name="pcm_av_av_repository_av_av_Signature")
ExceptionType = Class(name="ExceptionType")
pcm_av_av_repository_av_av_ExceptionType = Class(name="pcm_av_av_repository_av_av_ExceptionType")
pcm_av_av_repository_av_av_InfrastructureSignature = Class(name="pcm_av_av_repository_av_av_InfrastructureSignature")
InfrastructureInterface = Class(name="InfrastructureInterface")
pcm_av_av_repository_av_av_InfrastructureInterface = Class(name="pcm_av_av_repository_av_av_InfrastructureInterface")
pcm_av_av_repository_av_av_InfrastructureRequiredRole = Class(name="pcm_av_av_repository_av_av_InfrastructureRequiredRole")
pcm_av_av_repository_av_av_RequiredRole = Class(name="pcm_av_av_repository_av_av_RequiredRole")
pcm_av_av_repository_av_av_OperationSignature = Class(name="pcm_av_av_repository_av_av_OperationSignature")
pcm_av_av_repository_av_av_OperationInterface = Class(name="pcm_av_av_repository_av_av_OperationInterface")
pcm_av_av_repository_av_av_OperationRequiredRole = Class(name="pcm_av_av_repository_av_av_OperationRequiredRole")
pcm_av_av_repository_av_av_SourceRole = Class(name="pcm_av_av_repository_av_av_SourceRole")
pcm_av_av_repository_av_av_SinkRole = Class(name="pcm_av_av_repository_av_av_SinkRole")
pcm_av_av_repository_av_av_OperationProvidedRole = Class(name="pcm_av_av_repository_av_av_OperationProvidedRole")
pcm_av_av_repository_av_av_InfrastructureProvidedRole = Class(name="pcm_av_av_repository_av_av_InfrastructureProvidedRole")
OperationInterface = Class(name="OperationInterface")
pcm_av_av_repository_av_av_CompleteComponentType = Class(name="pcm_av_av_repository_av_av_CompleteComponentType")
ProvidesComponentType = Class(name="ProvidesComponentType")
pcm_av_av_repository_av_av_ProvidesComponentType = Class(name="pcm_av_av_repository_av_av_ProvidesComponentType")
pcm_av_av_repository_av_av_CompositeComponent = Class(name="pcm_av_av_repository_av_av_CompositeComponent")
entity_av_av_ComposedProvidingRequiringEntity = Class(name="entity_av_av_ComposedProvidingRequiringEntity")
repository_av_av_ImplementationComponentType = Class(name="repository_av_av_ImplementationComponentType")
pcm_av_av_repository_av_av_CollectionDataType = Class(name="pcm_av_av_repository_av_av_CollectionDataType")
repository_av_av_DataType = Class(name="repository_av_av_DataType")
pcm_av_av_repository_av_av_CompositeDataType = Class(name="pcm_av_av_repository_av_av_CompositeDataType")
CompositeDataType = Class(name="CompositeDataType")
InnerDeclaration = Class(name="InnerDeclaration")
pcm_av_av_repository_av_av_InnerDeclaration = Class(name="pcm_av_av_repository_av_av_InnerDeclaration")
NamedElement = Class(name="NamedElement")
pcm_av_av_repository_av_av_Role = Class(name="pcm_av_av_repository_av_av_Role")
pcm_av_av_resourcetype_av_av_ResourceSignature = Class(name="pcm_av_av_resourcetype_av_av_ResourceSignature")
pcm_av_av_resourcetype_av_av_ProcessingResourceType = Class(name="pcm_av_av_resourcetype_av_av_ProcessingResourceType")
ResourceType = Class(name="ResourceType")
pcm_av_av_repository_av_av_PrimitiveDataType = Class(name="pcm_av_av_repository_av_av_PrimitiveDataType")
pcm_av_av_resourcetype_av_av_ResourceType = Class(name="pcm_av_av_resourcetype_av_av_ResourceType")
UnitCarryingElement = Class(name="UnitCarryingElement")
ResourceRepository = Class(name="ResourceRepository")
pcm_av_av_resourcetype_av_av_ResourceRepository = Class(name="pcm_av_av_resourcetype_av_av_ResourceRepository")
SchedulingPolicy = Class(name="SchedulingPolicy")
pcm_av_av_resourcetype_av_av_SchedulingPolicy = Class(name="pcm_av_av_resourcetype_av_av_SchedulingPolicy")
pcm_av_av_resourcetype_av_av_CommunicationLinkResourceType = Class(name="pcm_av_av_resourcetype_av_av_CommunicationLinkResourceType")
NetworkInducedFailureType = Class(name="NetworkInducedFailureType")
pcm_av_av_resourcetype_av_av_ResourceInterface = Class(name="pcm_av_av_resourcetype_av_av_ResourceInterface")
pcm_av_av_protocol_av_av_Protocol = Class(name="pcm_av_av_protocol_av_av_Protocol")
pcm_av_av_parameter_av_av_VariableUsage = Class(name="pcm_av_av_parameter_av_av_VariableUsage")
HardwareInducedFailureType = Class(name="HardwareInducedFailureType")
SynchronisationPoint = Class(name="SynchronisationPoint")
CallReturnAction = Class(name="CallReturnAction")
SetVariableAction = Class(name="SetVariableAction")
SpecifiedOutputParameterAbstraction = Class(name="SpecifiedOutputParameterAbstraction")
EntryLevelSystemCall = Class(name="EntryLevelSystemCall")
parameter_av_av_pcm_av_av_AbstractNamedReference = Class(name="parameter_av_av_pcm_av_av_AbstractNamedReference")
pcm_av_av_parameter_av_av_VariableCharacterisation = Class(name="pcm_av_av_parameter_av_av_VariableCharacterisation")
pcm_av_av_parameter_av_av_CharacterisedVariable = Class(name="pcm_av_av_parameter_av_av_CharacterisedVariable")
Variable = Class(name="Variable")
pcm_av_av_reliability_av_av_FailureOccurrenceDescription = Class(name="pcm_av_av_reliability_av_av_FailureOccurrenceDescription")
CallAction = Class(name="CallAction")
pcm_av_av_reliability_av_av_HardwareInducedFailureType = Class(name="pcm_av_av_reliability_av_av_HardwareInducedFailureType")
ProcessingResourceType = Class(name="ProcessingResourceType")
pcm_av_av_reliability_av_av_SoftwareInducedFailureType = Class(name="pcm_av_av_reliability_av_av_SoftwareInducedFailureType")
InternalFailureOccurrenceDescription = Class(name="InternalFailureOccurrenceDescription")
pcm_av_av_reliability_av_av_InternalFailureOccurrenceDescription = Class(name="pcm_av_av_reliability_av_av_InternalFailureOccurrenceDescription")
FailureOccurrenceDescription = Class(name="FailureOccurrenceDescription")
InternalAction = Class(name="InternalAction")
SoftwareInducedFailureType = Class(name="SoftwareInducedFailureType")
pcm_av_av_reliability_av_av_NetworkInducedFailureType = Class(name="pcm_av_av_reliability_av_av_NetworkInducedFailureType")
CommunicationLinkResourceType = Class(name="CommunicationLinkResourceType")
pcm_av_av_reliability_av_av_ExternalFailureOccurrenceDescription = Class(name="pcm_av_av_reliability_av_av_ExternalFailureOccurrenceDescription")
qos_reliability_av_av_SpecifiedReliabilityAnnotation = Class(name="qos_reliability_av_av_SpecifiedReliabilityAnnotation")
pcm_av_av_reliability_av_av_ResourceTimeoutFailureType = Class(name="pcm_av_av_reliability_av_av_ResourceTimeoutFailureType")
pcm_av_av_reliability_av_av_FailureType = Class(name="pcm_av_av_reliability_av_av_FailureType")
pcm_av_av_seff_av_av_StopAction = Class(name="pcm_av_av_seff_av_av_StopAction")
AbstractInternalControlFlowAction = Class(name="AbstractInternalControlFlowAction")
pcm_av_av_seff_av_av_AbstractInternalControlFlowAction = Class(name="pcm_av_av_seff_av_av_AbstractInternalControlFlowAction")
AbstractAction = Class(name="AbstractAction")
pcm_av_av_seff_av_av_AbstractAction = Class(name="pcm_av_av_seff_av_av_AbstractAction")
ResourceDemandingBehaviour = Class(name="ResourceDemandingBehaviour")
pcm_av_av_seff_av_av_ResourceDemandingBehaviour = Class(name="pcm_av_av_seff_av_av_ResourceDemandingBehaviour")
AbstractLoopAction = Class(name="AbstractLoopAction")
AbstractBranchTransition = Class(name="AbstractBranchTransition")
pcm_av_av_seff_av_av_AbstractLoopAction = Class(name="pcm_av_av_seff_av_av_AbstractLoopAction")
pcm_av_av_seff_av_av_AbstractBranchTransition = Class(name="pcm_av_av_seff_av_av_AbstractBranchTransition")
BranchAction = Class(name="BranchAction")
pcm_av_av_seff_av_av_BranchAction = Class(name="pcm_av_av_seff_av_av_BranchAction")
pcm_av_av_seff_av_av_CallAction = Class(name="pcm_av_av_seff_av_av_CallAction")
pcm_av_av_seff_av_av_StartAction = Class(name="pcm_av_av_seff_av_av_StartAction")
pcm_av_av_seff_av_av_ServiceEffectSpecification = Class(name="pcm_av_av_seff_av_av_ServiceEffectSpecification")
pcm_av_av_seff_av_av_ResourceDemandingSEFF = Class(name="pcm_av_av_seff_av_av_ResourceDemandingSEFF")
seff_av_av_ServiceEffectSpecification = Class(name="seff_av_av_ServiceEffectSpecification")
seff_av_av_ResourceDemandingBehaviour = Class(name="seff_av_av_ResourceDemandingBehaviour")
ResourceDemandingInternalBehaviour = Class(name="ResourceDemandingInternalBehaviour")
pcm_av_av_seff_av_av_ResourceDemandingInternalBehaviour = Class(name="pcm_av_av_seff_av_av_ResourceDemandingInternalBehaviour")
ResourceDemandingSEFF = Class(name="ResourceDemandingSEFF")
pcm_av_av_seff_av_av_ReleaseAction = Class(name="pcm_av_av_seff_av_av_ReleaseAction")
pcm_av_av_seff_av_av_ForkAction = Class(name="pcm_av_av_seff_av_av_ForkAction")
ForkedBehaviour = Class(name="ForkedBehaviour")
pcm_av_av_seff_av_av_ForkedBehaviour = Class(name="pcm_av_av_seff_av_av_ForkedBehaviour")
ForkAction = Class(name="ForkAction")
pcm_av_av_seff_av_av_SynchronisationPoint = Class(name="pcm_av_av_seff_av_av_SynchronisationPoint")
pcm_av_av_seff_av_av_ExternalCallAction = Class(name="pcm_av_av_seff_av_av_ExternalCallAction")
seff_av_av_AbstractAction = Class(name="seff_av_av_AbstractAction")
seff_av_av_CallReturnAction = Class(name="seff_av_av_CallReturnAction")
seff_reliability_av_av_FailureHandlingEntity = Class(name="seff_reliability_av_av_FailureHandlingEntity")
pcm_av_av_seff_av_av_LoopAction = Class(name="pcm_av_av_seff_av_av_LoopAction")
pcm_av_av_seff_av_av_CallReturnAction = Class(name="pcm_av_av_seff_av_av_CallReturnAction")
pcm_av_av_seff_av_av_ProbabilisticBranchTransition = Class(name="pcm_av_av_seff_av_av_ProbabilisticBranchTransition")
pcm_av_av_seff_av_av_AcquireAction = Class(name="pcm_av_av_seff_av_av_AcquireAction")
pcm_av_av_seff_av_av_CollectionIteratorAction = Class(name="pcm_av_av_seff_av_av_CollectionIteratorAction")
pcm_av_av_seff_av_av_GuardedBranchTransition = Class(name="pcm_av_av_seff_av_av_GuardedBranchTransition")
pcm_av_av_seff_av_av_SetVariableAction = Class(name="pcm_av_av_seff_av_av_SetVariableAction")
pcm_av_av_seff_av_av_InternalCallAction = Class(name="pcm_av_av_seff_av_av_InternalCallAction")
seff_av_av_CallAction = Class(name="seff_av_av_CallAction")
seff_av_av_AbstractInternalControlFlowAction = Class(name="seff_av_av_AbstractInternalControlFlowAction")
pcm_av_av_seff_av_av_EmitEventAction = Class(name="pcm_av_av_seff_av_av_EmitEventAction")
pcm_av_av_seff_av_av_InternalAction = Class(name="pcm_av_av_seff_av_av_InternalAction")
pcm_av_av_seff_performance_av_av_InfrastructureCall = Class(name="pcm_av_av_seff_performance_av_av_InfrastructureCall")
pcm_av_av_seff_performance_av_av_ResourceCall = Class(name="pcm_av_av_seff_performance_av_av_ResourceCall")
pcm_av_av_seff_performance_av_av_ParametricResourceDemand = Class(name="pcm_av_av_seff_performance_av_av_ParametricResourceDemand")
pcm_av_av_seff_reliability_av_av_RecoveryActionBehaviour = Class(name="pcm_av_av_seff_reliability_av_av_RecoveryActionBehaviour")
seff_reliability_av_av_RecoveryActionBehaviour = Class(name="seff_reliability_av_av_RecoveryActionBehaviour")
seff_reliability_av_av_RecoveryAction = Class(name="seff_reliability_av_av_RecoveryAction")
pcm_av_av_seff_reliability_av_av_RecoveryAction = Class(name="pcm_av_av_seff_reliability_av_av_RecoveryAction")
pcm_av_av_seff_reliability_av_av_FailureHandlingEntity = Class(name="pcm_av_av_seff_reliability_av_av_FailureHandlingEntity")
pcm_av_av_qosannotations_av_av_SpecifiedQoSAnnotation = Class(name="pcm_av_av_qosannotations_av_av_SpecifiedQoSAnnotation")
QoSAnnotations = Class(name="QoSAnnotations")
pcm_av_av_qosannotations_av_av_QoSAnnotations = Class(name="pcm_av_av_qosannotations_av_av_QoSAnnotations")
System = Class(name="System")
SpecifiedQoSAnnotation = Class(name="SpecifiedQoSAnnotation")
pcm_av_av_qosannotations_av_av_SpecifiedOutputParameterAbstraction = Class(name="pcm_av_av_qosannotations_av_av_SpecifiedOutputParameterAbstraction")
pcm_av_av_qos_performance_av_av_SystemSpecifiedExecutionTime = Class(name="pcm_av_av_qos_performance_av_av_SystemSpecifiedExecutionTime")
SpecifiedExecutionTime = Class(name="SpecifiedExecutionTime")
pcm_av_av_qos_performance_av_av_SpecifiedExecutionTime = Class(name="pcm_av_av_qos_performance_av_av_SpecifiedExecutionTime")
pcm_av_av_qos_performance_av_av_ComponentSpecifiedExecutionTime = Class(name="pcm_av_av_qos_performance_av_av_ComponentSpecifiedExecutionTime")
pcm_av_av_qos_reliability_av_av_SpecifiedReliabilityAnnotation = Class(name="pcm_av_av_qos_reliability_av_av_SpecifiedReliabilityAnnotation")
ExternalFailureOccurrenceDescription = Class(name="ExternalFailureOccurrenceDescription")
pcm_av_av_system_av_av_System = Class(name="pcm_av_av_system_av_av_System")
pcm_av_av_resourceenvironment_av_av_ResourceEnvironment = Class(name="pcm_av_av_resourceenvironment_av_av_ResourceEnvironment")
LinkingResource = Class(name="LinkingResource")
ResourceContainer = Class(name="ResourceContainer")
pcm_av_av_resourceenvironment_av_av_LinkingResource = Class(name="pcm_av_av_resourceenvironment_av_av_LinkingResource")
ResourceEnvironment = Class(name="ResourceEnvironment")
pcm_av_av_resourceenvironment_av_av_ResourceContainer = Class(name="pcm_av_av_resourceenvironment_av_av_ResourceContainer")
pcm_av_av_resourceenvironment_av_av_ProcessingResourceSpecification = Class(name="pcm_av_av_resourceenvironment_av_av_ProcessingResourceSpecification")
pcm_av_av_resourceenvironment_av_av_CommunicationLinkResourceSpecification = Class(name="pcm_av_av_resourceenvironment_av_av_CommunicationLinkResourceSpecification")
pcm_av_av_allocation_av_av_AllocationContext = Class(name="pcm_av_av_allocation_av_av_AllocationContext")
Allocation = Class(name="Allocation")
pcm_av_av_allocation_av_av_Allocation = Class(name="pcm_av_av_allocation_av_av_Allocation")
AllocationContext = Class(name="AllocationContext")
pcm_av_av_subsystem_av_av_SubSystem = Class(name="pcm_av_av_subsystem_av_av_SubSystem")
repository_av_av_RepositoryComponent = Class(name="repository_av_av_RepositoryComponent")
pcm_av_av_completions_av_av_Completion = Class(name="pcm_av_av_completions_av_av_Completion")
pcm_av_av_completions_av_av_CompletionRepository = Class(name="pcm_av_av_completions_av_av_CompletionRepository")
Completion = Class(name="Completion")
pcm_av_av_completions_av_av_DelegatingExternalCallAction = Class(name="pcm_av_av_completions_av_av_DelegatingExternalCallAction")
ExternalCallAction = Class(name="ExternalCallAction")
pcm_av_av_completions_av_av_NetworkDemandParametricResourceDemand = Class(name="pcm_av_av_completions_av_av_NetworkDemandParametricResourceDemand")
ParametricResourceDemand = Class(name="ParametricResourceDemand")

# pcm_av_av_EObject class attributes and methods

# pcm_av_av_GlobalScopeGlobalScope class attributes and methods

# pcm_av_av_PerJoinPointScopePerJoinPointScope class attributes and methods

# pcm_av_av_Advice class attributes and methods

# pcm_av_av_GlobalScope class attributes and methods

# pcm_av_av_PerJoinPointScope class attributes and methods

# pcm_av_av_core_av_av_PCMRandomVariable class attributes and methods
pcm_av_av_core_av_av_PCMRandomVariable_m_SpecificationMustNotBeNULL: Method = Method(name="SpecificationMustNotBeNULL", parameters={Parameter(name='pcm_av_av_context', type=StringType), Parameter(name='pcm_av_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_av_core_av_av_PCMRandomVariable.methods={pcm_av_av_core_av_av_PCMRandomVariable_m_SpecificationMustNotBeNULL}

# RandomVariable class attributes and methods

# ClosedWorkload class attributes and methods

# PassiveResource class attributes and methods

# VariableCharacterisation class attributes and methods

# seff_performance_av_av_InfrastructureCall class attributes and methods

# seff_performance_av_av_ResourceCall class attributes and methods

# seff_performance_av_av_ParametricResourceDemand class attributes and methods

# pcm_av_av_DummyClass class attributes and methods

# pcm_av_av_AdviceAdvice class attributes and methods

# composition_av_av_EventChannelSinkConnector class attributes and methods

# composition_av_av_AssemblyEventConnector class attributes and methods

# Loop class attributes and methods

# OpenWorkload class attributes and methods

# Delay class attributes and methods

# CommunicationLinkResourceSpecification class attributes and methods

# ProcessingResourceSpecification class attributes and methods

# pcm_av_av_entity_av_av_ResourceProvidedRole class attributes and methods

# Role class attributes and methods

# entity_av_av_ResourceInterfaceProvidingEntity class attributes and methods

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

# LoopAction class attributes and methods

# GuardedBranchTransition class attributes and methods

# qos_performance_av_av_SpecifiedExecutionTime class attributes and methods

# pcm_av_av_entity_av_av_ResourceInterfaceProvidingEntity class attributes and methods

# entity_av_av_ResourceProvidedRole class attributes and methods

# pcm_av_av_entity_av_av_ComposedProvidingRequiringEntity class attributes and methods
pcm_av_av_entity_av_av_ComposedProvidingRequiringEntity_m_ProvidedRolesMustBeBound: Method = Method(name="ProvidedRolesMustBeBound", parameters={Parameter(name='pcm_av_av_context', type=StringType), Parameter(name='pcm_av_av_diagnostics', type=StringType)}, type=BooleanType)
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

# pcm_av_av_composition_av_av_DelegationConnector class attributes and methods

# Connector class attributes and methods

# pcm_av_av_composition_av_av_Connector class attributes and methods

# pcm_av_av_composition_av_av_ComposedStructure class attributes and methods
pcm_av_av_composition_av_av_ComposedStructure_m_MultipleConnectorsConstraint: Method = Method(name="MultipleConnectorsConstraint", parameters={Parameter(name='pcm_av_av_diagnostics', type=StringType), Parameter(name='pcm_av_av_context', type=StringType)}, type=BooleanType)
pcm_av_av_composition_av_av_ComposedStructure_m_MultipleConnectorsConstraintForAssemblyConnectors: Method = Method(name="MultipleConnectorsConstraintForAssemblyConnectors", parameters={Parameter(name='pcm_av_av_context', type=StringType), Parameter(name='pcm_av_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_av_composition_av_av_ComposedStructure.methods={pcm_av_av_composition_av_av_ComposedStructure_m_MultipleConnectorsConstraintForAssemblyConnectors, pcm_av_av_composition_av_av_ComposedStructure_m_MultipleConnectorsConstraint}

# pcm_av_av_entity_av_av_ResourceRequiredRole class attributes and methods

# composition_av_av_AssemblyContext class attributes and methods

# composition_av_av_ResourceRequiredDelegationConnector class attributes and methods

# composition_av_av_EventChannel class attributes and methods

# composition_av_av_Connector class attributes and methods

# pcm_av_av_composition_av_av_ResourceRequiredDelegationConnector class attributes and methods

# pcm_av_av_composition_av_av_EventChannel class attributes and methods

# EventGroup class attributes and methods

# composition_av_av_EventChannelSourceConnector class attributes and methods

# pcm_av_av_composition_av_av_EventChannelSourceConnector class attributes and methods

# SourceRole class attributes and methods

# pcm_av_av_composition_av_av_EventChannelSinkConnector class attributes and methods

# SinkRole class attributes and methods

# OperationProvidedRole class attributes and methods

# pcm_av_av_composition_av_av_RequiredDelegationConnector class attributes and methods
pcm_av_av_composition_av_av_RequiredDelegationConnector_m_RequiredDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure: Method = Method(name="RequiredDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure", parameters={Parameter(name='pcm_av_av_context', type=StringType), Parameter(name='pcm_av_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_av_composition_av_av_RequiredDelegationConnector_m_ComponentOfAssemblyContextAndInnerRoleRequiringComponentNeedToBeTheSame: Method = Method(name="ComponentOfAssemblyContextAndInnerRoleRequiringComponentNeedToBeTheSame", parameters={Parameter(name='pcm_av_av_context', type=StringType), Parameter(name='pcm_av_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_av_composition_av_av_RequiredDelegationConnector_m_RequiringEntityOfOuterRequiredRoleMustBeTheSameAsTheParentOfTheRequiredDelegationConnector: Method = Method(name="RequiringEntityOfOuterRequiredRoleMustBeTheSameAsTheParentOfTheRequiredDelegationConnector", parameters={Parameter(name='pcm_av_av_context', type=StringType), Parameter(name='pcm_av_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_av_composition_av_av_RequiredDelegationConnector.methods={pcm_av_av_composition_av_av_RequiredDelegationConnector_m_RequiredDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure, pcm_av_av_composition_av_av_RequiredDelegationConnector_m_RequiringEntityOfOuterRequiredRoleMustBeTheSameAsTheParentOfTheRequiredDelegationConnector, pcm_av_av_composition_av_av_RequiredDelegationConnector_m_ComponentOfAssemblyContextAndInnerRoleRequiringComponentNeedToBeTheSame}

# OperationRequiredRole class attributes and methods

# PCMRandomVariable class attributes and methods

# pcm_av_av_composition_av_av_ProvidedDelegationConnector class attributes and methods
pcm_av_av_composition_av_av_ProvidedDelegationConnector_m_ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure: Method = Method(name="ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure", parameters={Parameter(name='pcm_av_av_context', type=StringType), Parameter(name='pcm_av_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_av_composition_av_av_ProvidedDelegationConnector_m_ComponentOfAssemblyContextAndInnerRoleProvidingComponentNeedToBeTheSame: Method = Method(name="ComponentOfAssemblyContextAndInnerRoleProvidingComponentNeedToBeTheSame", parameters={Parameter(name='pcm_av_av_diagnostics', type=StringType), Parameter(name='pcm_av_av_context', type=StringType)}, type=BooleanType)
pcm_av_av_composition_av_av_ProvidedDelegationConnector.methods={pcm_av_av_composition_av_av_ProvidedDelegationConnector_m_ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure, pcm_av_av_composition_av_av_ProvidedDelegationConnector_m_ComponentOfAssemblyContextAndInnerRoleProvidingComponentNeedToBeTheSame}

# DelegationConnector class attributes and methods

# pcm_av_av_composition_av_av_AssemblyConnector class attributes and methods
pcm_av_av_composition_av_av_AssemblyConnector_m_AssemblyConnectorsReferencedProvidedRolesAndChildContextMustMatch: Method = Method(name="AssemblyConnectorsReferencedProvidedRolesAndChildContextMustMatch", parameters={Parameter(name='pcm_av_av_diagnostics', type=StringType), Parameter(name='pcm_av_av_context', type=StringType)}, type=BooleanType)
pcm_av_av_composition_av_av_AssemblyConnector_m_AssemblyConnectorsReferencedRequiredRoleAndChildContextMustMatch: Method = Method(name="AssemblyConnectorsReferencedRequiredRoleAndChildContextMustMatch", parameters={Parameter(name='pcm_av_av_diagnostics', type=StringType), Parameter(name='pcm_av_av_context', type=StringType)}, type=BooleanType)
pcm_av_av_composition_av_av_AssemblyConnector_m_AssemblyConnectorsReferencedInterfacesMustMatch: Method = Method(name="AssemblyConnectorsReferencedInterfacesMustMatch", parameters={Parameter(name='pcm_av_av_diagnostics', type=StringType), Parameter(name='pcm_av_av_context', type=StringType)}, type=BooleanType)
pcm_av_av_composition_av_av_AssemblyConnector.methods={pcm_av_av_composition_av_av_AssemblyConnector_m_AssemblyConnectorsReferencedInterfacesMustMatch, pcm_av_av_composition_av_av_AssemblyConnector_m_AssemblyConnectorsReferencedProvidedRolesAndChildContextMustMatch, pcm_av_av_composition_av_av_AssemblyConnector_m_AssemblyConnectorsReferencedRequiredRoleAndChildContextMustMatch}

# pcm_av_av_composition_av_av_AssemblyEventConnector class attributes and methods

# pcm_av_av_composition_av_av_SinkDelegationConnector class attributes and methods

# pcm_av_av_composition_av_av_AssemblyInfrastructureConnector class attributes and methods

# InfrastructureProvidedRole class attributes and methods

# InfrastructureRequiredRole class attributes and methods

# pcm_av_av_composition_av_av_ProvidedInfrastructureDelegationConnector class attributes and methods

# pcm_av_av_composition_av_av_RequiredInfrastructureDelegationConnector class attributes and methods

# pcm_av_av_composition_av_av_RequiredResourceDelegationConnector class attributes and methods

# pcm_av_av_composition_av_av_SourceDelegationConnector class attributes and methods

# pcm_av_av_composition_av_av_AssemblyContext class attributes and methods

# RepositoryComponent class attributes and methods

# VariableUsage class attributes and methods

# pcm_av_av_usagemodel_av_av_Workload class attributes and methods

# UsageScenario class attributes and methods

# pcm_av_av_usagemodel_av_av_UsageScenario class attributes and methods

# UsageModel class attributes and methods

# ScenarioBehaviour class attributes and methods

# Workload class attributes and methods

# pcm_av_av_usagemodel_av_av_UserData class attributes and methods

# pcm_av_av_usagemodel_av_av_UsageModel class attributes and methods

# UserData class attributes and methods

# pcm_av_av_usagemodel_av_av_EntryLevelSystemCall class attributes and methods
pcm_av_av_usagemodel_av_av_EntryLevelSystemCall_priority: Property = Property(name="priority", type=IntegerType)
pcm_av_av_usagemodel_av_av_EntryLevelSystemCall_m_EntryLevelSystemCallMustReferenceProvidedRoleOfASystem: Method = Method(name="EntryLevelSystemCallMustReferenceProvidedRoleOfASystem", parameters={Parameter(name='pcm_av_av_diagnostics', type=StringType), Parameter(name='pcm_av_av_context', type=StringType)}, type=BooleanType)
pcm_av_av_usagemodel_av_av_EntryLevelSystemCall_m_EntryLevelSystemCallSignatureMustMatchItsProvidedRole: Method = Method(name="EntryLevelSystemCallSignatureMustMatchItsProvidedRole", parameters={Parameter(name='pcm_av_av_context', type=StringType), Parameter(name='pcm_av_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_av_usagemodel_av_av_EntryLevelSystemCall.attributes={pcm_av_av_usagemodel_av_av_EntryLevelSystemCall_priority}
pcm_av_av_usagemodel_av_av_EntryLevelSystemCall.methods={pcm_av_av_usagemodel_av_av_EntryLevelSystemCall_m_EntryLevelSystemCallSignatureMustMatchItsProvidedRole, pcm_av_av_usagemodel_av_av_EntryLevelSystemCall_m_EntryLevelSystemCallMustReferenceProvidedRoleOfASystem}

# AbstractUserAction class attributes and methods

# OperationSignature class attributes and methods

# pcm_av_av_usagemodel_av_av_AbstractUserAction class attributes and methods

# pcm_av_av_usagemodel_av_av_ScenarioBehaviour class attributes and methods
pcm_av_av_usagemodel_av_av_ScenarioBehaviour_m_Exactlyonestart: Method = Method(name="Exactlyonestart", parameters={Parameter(name='pcm_av_av_diagnostics', type=StringType), Parameter(name='pcm_av_av_context', type=StringType)}, type=BooleanType)
pcm_av_av_usagemodel_av_av_ScenarioBehaviour_m_Exactlyonestop: Method = Method(name="Exactlyonestop", parameters={Parameter(name='pcm_av_av_diagnostics', type=StringType), Parameter(name='pcm_av_av_context', type=StringType)}, type=BooleanType)
pcm_av_av_usagemodel_av_av_ScenarioBehaviour_m_EachuseractionexceptStartandStopmusthaveapredecessorandsuccessor: Method = Method(name="EachuseractionexceptStartandStopmusthaveapredecessorandsuccessor", parameters={Parameter(name='pcm_av_av_context', type=StringType), Parameter(name='pcm_av_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_av_usagemodel_av_av_ScenarioBehaviour.methods={pcm_av_av_usagemodel_av_av_ScenarioBehaviour_m_Exactlyonestop, pcm_av_av_usagemodel_av_av_ScenarioBehaviour_m_Exactlyonestart, pcm_av_av_usagemodel_av_av_ScenarioBehaviour_m_EachuseractionexceptStartandStopmusthaveapredecessorandsuccessor}

# BranchTransition class attributes and methods

# pcm_av_av_usagemodel_av_av_BranchTransition class attributes and methods
pcm_av_av_usagemodel_av_av_BranchTransition_branchProbability: Property = Property(name="branchProbability", type=FloatType)
pcm_av_av_usagemodel_av_av_BranchTransition.attributes={pcm_av_av_usagemodel_av_av_BranchTransition_branchProbability}

# Branch class attributes and methods

# pcm_av_av_usagemodel_av_av_Branch class attributes and methods
pcm_av_av_usagemodel_av_av_Branch_m_AllBranchProbabilitiesMustSumUpTo1: Method = Method(name="AllBranchProbabilitiesMustSumUpTo1", parameters={Parameter(name='pcm_av_av_diagnostics', type=StringType), Parameter(name='pcm_av_av_context', type=StringType)}, type=BooleanType)
pcm_av_av_usagemodel_av_av_Branch.methods={pcm_av_av_usagemodel_av_av_Branch_m_AllBranchProbabilitiesMustSumUpTo1}

# pcm_av_av_usagemodel_av_av_Loop class attributes and methods

# pcm_av_av_usagemodel_av_av_Stop class attributes and methods
pcm_av_av_usagemodel_av_av_Stop_m_StopHasNoSuccessor: Method = Method(name="StopHasNoSuccessor", parameters={Parameter(name='pcm_av_av_diagnostics', type=StringType), Parameter(name='pcm_av_av_context', type=StringType)}, type=BooleanType)
pcm_av_av_usagemodel_av_av_Stop.methods={pcm_av_av_usagemodel_av_av_Stop_m_StopHasNoSuccessor}

# pcm_av_av_usagemodel_av_av_Start class attributes and methods
pcm_av_av_usagemodel_av_av_Start_m_StartHasNoPredecessor: Method = Method(name="StartHasNoPredecessor", parameters={Parameter(name='pcm_av_av_diagnostics', type=StringType), Parameter(name='pcm_av_av_context', type=StringType)}, type=BooleanType)
pcm_av_av_usagemodel_av_av_Start.methods={pcm_av_av_usagemodel_av_av_Start_m_StartHasNoPredecessor}

# pcm_av_av_usagemodel_av_av_OpenWorkload class attributes and methods
pcm_av_av_usagemodel_av_av_OpenWorkload_m_InterArrivalTimeInOpenWorkloadNeedsToBeSpecified: Method = Method(name="InterArrivalTimeInOpenWorkloadNeedsToBeSpecified", parameters={Parameter(name='pcm_av_av_context', type=StringType), Parameter(name='pcm_av_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_av_usagemodel_av_av_OpenWorkload.methods={pcm_av_av_usagemodel_av_av_OpenWorkload_m_InterArrivalTimeInOpenWorkloadNeedsToBeSpecified}

# pcm_av_av_usagemodel_av_av_Delay class attributes and methods

# pcm_av_av_usagemodel_av_av_ClosedWorkload class attributes and methods
pcm_av_av_usagemodel_av_av_ClosedWorkload_population: Property = Property(name="population", type=IntegerType)
pcm_av_av_usagemodel_av_av_ClosedWorkload_m_PopulationInClosedWorkloadNeedsToBeSpecified: Method = Method(name="PopulationInClosedWorkloadNeedsToBeSpecified", parameters={Parameter(name='pcm_av_av_diagnostics', type=StringType), Parameter(name='pcm_av_av_context', type=StringType)}, type=BooleanType)
pcm_av_av_usagemodel_av_av_ClosedWorkload_m_ThinkTimeInClosedWorkloadNeedsToBeSpecified: Method = Method(name="ThinkTimeInClosedWorkloadNeedsToBeSpecified", parameters={Parameter(name='pcm_av_av_context', type=StringType), Parameter(name='pcm_av_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_av_usagemodel_av_av_ClosedWorkload.attributes={pcm_av_av_usagemodel_av_av_ClosedWorkload_population}
pcm_av_av_usagemodel_av_av_ClosedWorkload.methods={pcm_av_av_usagemodel_av_av_ClosedWorkload_m_ThinkTimeInClosedWorkloadNeedsToBeSpecified, pcm_av_av_usagemodel_av_av_ClosedWorkload_m_PopulationInClosedWorkloadNeedsToBeSpecified}

# pcm_av_av_repository_av_av_PassiveResource class attributes and methods

# BasicComponent class attributes and methods

# ResourceTimeoutFailureType class attributes and methods

# pcm_av_av_repository_av_av_BasicComponent class attributes and methods
pcm_av_av_repository_av_av_BasicComponent_m_NoSeffTypeUsedTwice: Method = Method(name="NoSeffTypeUsedTwice", parameters={Parameter(name='pcm_av_av_diagnostics', type=StringType), Parameter(name='pcm_av_av_context', type=StringType)}, type=BooleanType)
pcm_av_av_repository_av_av_BasicComponent_m_ProvideSameInterfacesAsImplementationType: Method = Method(name="ProvideSameInterfacesAsImplementationType", parameters={Parameter(name='pcm_av_av_context', type=StringType), Parameter(name='pcm_av_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_av_repository_av_av_BasicComponent_m_RequireSameInterfacesAsImplementationType: Method = Method(name="RequireSameInterfacesAsImplementationType", parameters={Parameter(name='pcm_av_av_context', type=StringType), Parameter(name='pcm_av_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_av_repository_av_av_BasicComponent.methods={pcm_av_av_repository_av_av_BasicComponent_m_RequireSameInterfacesAsImplementationType, pcm_av_av_repository_av_av_BasicComponent_m_NoSeffTypeUsedTwice, pcm_av_av_repository_av_av_BasicComponent_m_ProvideSameInterfacesAsImplementationType}

# ImplementationComponentType class attributes and methods

# ServiceEffectSpecification class attributes and methods

# pcm_av_av_repository_av_av_ImplementationComponentType class attributes and methods
pcm_av_av_repository_av_av_ImplementationComponentType_componentType: Property = Property(name="componentType", type=StringType)
pcm_av_av_repository_av_av_ImplementationComponentType_m_RequiredInterfacesHaveToConformToCompleteType: Method = Method(name="RequiredInterfacesHaveToConformToCompleteType", parameters={Parameter(name='pcm_av_av_diagnostics', type=StringType), Parameter(name='pcm_av_av_context', type=StringType)}, type=BooleanType)
pcm_av_av_repository_av_av_ImplementationComponentType_m_providedInterfacesHaveToConformToCompleteType: Method = Method(name="providedInterfacesHaveToConformToCompleteType", parameters={Parameter(name='pcm_av_av_diagnostics', type=StringType), Parameter(name='pcm_av_av_context', type=StringType)}, type=BooleanType)
pcm_av_av_repository_av_av_ImplementationComponentType_m_ProvidedInterfaceHaveToConformToComponentType: Method = Method(name="ProvidedInterfaceHaveToConformToComponentType", parameters={Parameter(name='pcm_av_av_diagnostics', type=StringType), Parameter(name='pcm_av_av_context', type=StringType)}, type=BooleanType)
pcm_av_av_repository_av_av_ImplementationComponentType.attributes={pcm_av_av_repository_av_av_ImplementationComponentType_componentType}
pcm_av_av_repository_av_av_ImplementationComponentType.methods={pcm_av_av_repository_av_av_ImplementationComponentType_m_RequiredInterfacesHaveToConformToCompleteType, pcm_av_av_repository_av_av_ImplementationComponentType_m_providedInterfacesHaveToConformToCompleteType, pcm_av_av_repository_av_av_ImplementationComponentType_m_ProvidedInterfaceHaveToConformToComponentType}

# CompleteComponentType class attributes and methods

# pcm_av_av_repository_av_av_RepositoryComponent class attributes and methods

# InterfaceProvidingRequiringEntity class attributes and methods

# Repository class attributes and methods

# pcm_av_av_repository_av_av_ProvidedRole class attributes and methods

# pcm_av_av_repository_av_av_Parameter class attributes and methods
pcm_av_av_repository_av_av_Parameter_parameterName: Property = Property(name="parameterName", type=StringType)
pcm_av_av_repository_av_av_Parameter_modifier__Parameter: Property = Property(name="modifier__Parameter", type=StringType)
pcm_av_av_repository_av_av_Parameter.attributes={pcm_av_av_repository_av_av_Parameter_parameterName, pcm_av_av_repository_av_av_Parameter_modifier__Parameter}

# DataType class attributes and methods

# InfrastructureSignature class attributes and methods

# EventType class attributes and methods

# ResourceSignature class attributes and methods

# pcm_av_av_repository_av_av_DataType class attributes and methods

# pcm_av_av_repository_av_av_Repository class attributes and methods
pcm_av_av_repository_av_av_Repository_repositoryDescription: Property = Property(name="repositoryDescription", type=StringType)
pcm_av_av_repository_av_av_Repository.attributes={pcm_av_av_repository_av_av_Repository_repositoryDescription}

# Interface class attributes and methods

# FailureType class attributes and methods

# pcm_av_av_repository_av_av_Interface class attributes and methods
pcm_av_av_repository_av_av_Interface_m_NoProtocolTypeIDUsedTwice: Method = Method(name="NoProtocolTypeIDUsedTwice", parameters={Parameter(name='pcm_av_av_diagnostics', type=StringType), Parameter(name='pcm_av_av_context', type=StringType)}, type=BooleanType)
pcm_av_av_repository_av_av_Interface.methods={pcm_av_av_repository_av_av_Interface_m_NoProtocolTypeIDUsedTwice}

# Protocol class attributes and methods

# RequiredCharacterisation class attributes and methods

# pcm_av_av_repository_av_av_RequiredCharacterisation class attributes and methods
pcm_av_av_repository_av_av_RequiredCharacterisation_type: Property = Property(name="type", type=StringType)
pcm_av_av_repository_av_av_RequiredCharacterisation.attributes={pcm_av_av_repository_av_av_RequiredCharacterisation_type}

# Parameter class attributes and methods

# pcm_av_av_repository_av_av_EventGroup class attributes and methods

# pcm_av_av_repository_av_av_EventType class attributes and methods

# Signature class attributes and methods

# pcm_av_av_repository_av_av_Signature class attributes and methods

# ExceptionType class attributes and methods

# pcm_av_av_repository_av_av_ExceptionType class attributes and methods
pcm_av_av_repository_av_av_ExceptionType_exceptionName: Property = Property(name="exceptionName", type=StringType)
pcm_av_av_repository_av_av_ExceptionType_exceptionMessage: Property = Property(name="exceptionMessage", type=StringType)
pcm_av_av_repository_av_av_ExceptionType.attributes={pcm_av_av_repository_av_av_ExceptionType_exceptionName, pcm_av_av_repository_av_av_ExceptionType_exceptionMessage}

# pcm_av_av_repository_av_av_InfrastructureSignature class attributes and methods

# InfrastructureInterface class attributes and methods

# pcm_av_av_repository_av_av_InfrastructureInterface class attributes and methods

# pcm_av_av_repository_av_av_InfrastructureRequiredRole class attributes and methods

# pcm_av_av_repository_av_av_RequiredRole class attributes and methods

# pcm_av_av_repository_av_av_OperationSignature class attributes and methods
pcm_av_av_repository_av_av_OperationSignature_m_ParameterNamesHaveToBeUniqueForASignature: Method = Method(name="ParameterNamesHaveToBeUniqueForASignature", parameters={Parameter(name='pcm_av_av_context', type=StringType), Parameter(name='pcm_av_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_av_repository_av_av_OperationSignature.methods={pcm_av_av_repository_av_av_OperationSignature_m_ParameterNamesHaveToBeUniqueForASignature}

# pcm_av_av_repository_av_av_OperationInterface class attributes and methods
pcm_av_av_repository_av_av_OperationInterface_m_SignaturesHaveToBeUniqueForAnInterface: Method = Method(name="SignaturesHaveToBeUniqueForAnInterface", parameters={Parameter(name='pcm_av_av_context', type=StringType), Parameter(name='pcm_av_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_av_repository_av_av_OperationInterface.methods={pcm_av_av_repository_av_av_OperationInterface_m_SignaturesHaveToBeUniqueForAnInterface}

# pcm_av_av_repository_av_av_OperationRequiredRole class attributes and methods

# pcm_av_av_repository_av_av_SourceRole class attributes and methods

# pcm_av_av_repository_av_av_SinkRole class attributes and methods

# pcm_av_av_repository_av_av_OperationProvidedRole class attributes and methods

# pcm_av_av_repository_av_av_InfrastructureProvidedRole class attributes and methods

# OperationInterface class attributes and methods

# pcm_av_av_repository_av_av_CompleteComponentType class attributes and methods
pcm_av_av_repository_av_av_CompleteComponentType_m_AtLeastOneInterfaceHasToBeProvidedOrRequiredByAUsefullCompleteComponentType: Method = Method(name="AtLeastOneInterfaceHasToBeProvidedOrRequiredByAUsefullCompleteComponentType", parameters={Parameter(name='pcm_av_av_context', type=StringType), Parameter(name='pcm_av_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_av_repository_av_av_CompleteComponentType_m_providedInterfacesHaveToConformToProvidedType2: Method = Method(name="providedInterfacesHaveToConformToProvidedType2", parameters={Parameter(name='pcm_av_av_context', type=StringType), Parameter(name='pcm_av_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_av_repository_av_av_CompleteComponentType.methods={pcm_av_av_repository_av_av_CompleteComponentType_m_providedInterfacesHaveToConformToProvidedType2, pcm_av_av_repository_av_av_CompleteComponentType_m_AtLeastOneInterfaceHasToBeProvidedOrRequiredByAUsefullCompleteComponentType}

# ProvidesComponentType class attributes and methods

# pcm_av_av_repository_av_av_ProvidesComponentType class attributes and methods
pcm_av_av_repository_av_av_ProvidesComponentType_m_AtLeastOneInterfaceHasToBeProvidedByAUsefullProvidesComponentType: Method = Method(name="AtLeastOneInterfaceHasToBeProvidedByAUsefullProvidesComponentType", parameters={Parameter(name='pcm_av_av_context', type=StringType), Parameter(name='pcm_av_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_av_repository_av_av_ProvidesComponentType.methods={pcm_av_av_repository_av_av_ProvidesComponentType_m_AtLeastOneInterfaceHasToBeProvidedByAUsefullProvidesComponentType}

# pcm_av_av_repository_av_av_CompositeComponent class attributes and methods
pcm_av_av_repository_av_av_CompositeComponent_m_ProvideSameInterfaces: Method = Method(name="ProvideSameInterfaces", parameters={Parameter(name='pcm_av_av_context', type=StringType), Parameter(name='pcm_av_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_av_repository_av_av_CompositeComponent_m_RequireSameInterfaces: Method = Method(name="RequireSameInterfaces", parameters={Parameter(name='pcm_av_av_context', type=StringType), Parameter(name='pcm_av_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_av_repository_av_av_CompositeComponent.methods={pcm_av_av_repository_av_av_CompositeComponent_m_RequireSameInterfaces, pcm_av_av_repository_av_av_CompositeComponent_m_ProvideSameInterfaces}

# entity_av_av_ComposedProvidingRequiringEntity class attributes and methods

# repository_av_av_ImplementationComponentType class attributes and methods

# pcm_av_av_repository_av_av_CollectionDataType class attributes and methods

# repository_av_av_DataType class attributes and methods

# pcm_av_av_repository_av_av_CompositeDataType class attributes and methods

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

# pcm_av_av_repository_av_av_PrimitiveDataType class attributes and methods
pcm_av_av_repository_av_av_PrimitiveDataType_type: Property = Property(name="type", type=StringType)
pcm_av_av_repository_av_av_PrimitiveDataType.attributes={pcm_av_av_repository_av_av_PrimitiveDataType_type}

# pcm_av_av_resourcetype_av_av_ResourceType class attributes and methods

# UnitCarryingElement class attributes and methods

# ResourceRepository class attributes and methods

# pcm_av_av_resourcetype_av_av_ResourceRepository class attributes and methods

# SchedulingPolicy class attributes and methods

# pcm_av_av_resourcetype_av_av_SchedulingPolicy class attributes and methods

# pcm_av_av_resourcetype_av_av_CommunicationLinkResourceType class attributes and methods

# NetworkInducedFailureType class attributes and methods

# pcm_av_av_resourcetype_av_av_ResourceInterface class attributes and methods

# pcm_av_av_protocol_av_av_Protocol class attributes and methods
pcm_av_av_protocol_av_av_Protocol_protocolTypeID: Property = Property(name="protocolTypeID", type=StringType)
pcm_av_av_protocol_av_av_Protocol.attributes={pcm_av_av_protocol_av_av_Protocol_protocolTypeID}

# pcm_av_av_parameter_av_av_VariableUsage class attributes and methods

# HardwareInducedFailureType class attributes and methods

# SynchronisationPoint class attributes and methods

# CallReturnAction class attributes and methods

# SetVariableAction class attributes and methods

# SpecifiedOutputParameterAbstraction class attributes and methods

# EntryLevelSystemCall class attributes and methods

# parameter_av_av_pcm_av_av_AbstractNamedReference class attributes and methods

# pcm_av_av_parameter_av_av_VariableCharacterisation class attributes and methods
pcm_av_av_parameter_av_av_VariableCharacterisation_type: Property = Property(name="type", type=StringType)
pcm_av_av_parameter_av_av_VariableCharacterisation.attributes={pcm_av_av_parameter_av_av_VariableCharacterisation_type}

# pcm_av_av_parameter_av_av_CharacterisedVariable class attributes and methods
pcm_av_av_parameter_av_av_CharacterisedVariable_characterisationType: Property = Property(name="characterisationType", type=StringType)
pcm_av_av_parameter_av_av_CharacterisedVariable.attributes={pcm_av_av_parameter_av_av_CharacterisedVariable_characterisationType}

# Variable class attributes and methods

# pcm_av_av_reliability_av_av_FailureOccurrenceDescription class attributes and methods
pcm_av_av_reliability_av_av_FailureOccurrenceDescription_failureProbability: Property = Property(name="failureProbability", type=FloatType)
pcm_av_av_reliability_av_av_FailureOccurrenceDescription_m_EnsureValidFailureProbabilityRange: Method = Method(name="EnsureValidFailureProbabilityRange", parameters={Parameter(name='pcm_av_av_context', type=StringType), Parameter(name='pcm_av_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_av_reliability_av_av_FailureOccurrenceDescription.attributes={pcm_av_av_reliability_av_av_FailureOccurrenceDescription_failureProbability}
pcm_av_av_reliability_av_av_FailureOccurrenceDescription.methods={pcm_av_av_reliability_av_av_FailureOccurrenceDescription_m_EnsureValidFailureProbabilityRange}

# CallAction class attributes and methods

# pcm_av_av_reliability_av_av_HardwareInducedFailureType class attributes and methods
pcm_av_av_reliability_av_av_HardwareInducedFailureType_m_HardwareInducedFailureTypeHasProcessingResourceType: Method = Method(name="HardwareInducedFailureTypeHasProcessingResourceType", parameters={Parameter(name='pcm_av_av_diagnostics', type=StringType), Parameter(name='pcm_av_av_context', type=StringType)}, type=BooleanType)
pcm_av_av_reliability_av_av_HardwareInducedFailureType.methods={pcm_av_av_reliability_av_av_HardwareInducedFailureType_m_HardwareInducedFailureTypeHasProcessingResourceType}

# ProcessingResourceType class attributes and methods

# pcm_av_av_reliability_av_av_SoftwareInducedFailureType class attributes and methods

# InternalFailureOccurrenceDescription class attributes and methods

# pcm_av_av_reliability_av_av_InternalFailureOccurrenceDescription class attributes and methods
pcm_av_av_reliability_av_av_InternalFailureOccurrenceDescription_m_NoResourceTimeoutFailureAllowedForInternalFailureOccurrenceDescription: Method = Method(name="NoResourceTimeoutFailureAllowedForInternalFailureOccurrenceDescription", parameters={Parameter(name='pcm_av_av_context', type=StringType), Parameter(name='pcm_av_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_av_reliability_av_av_InternalFailureOccurrenceDescription.methods={pcm_av_av_reliability_av_av_InternalFailureOccurrenceDescription_m_NoResourceTimeoutFailureAllowedForInternalFailureOccurrenceDescription}

# FailureOccurrenceDescription class attributes and methods

# InternalAction class attributes and methods

# SoftwareInducedFailureType class attributes and methods

# pcm_av_av_reliability_av_av_NetworkInducedFailureType class attributes and methods
pcm_av_av_reliability_av_av_NetworkInducedFailureType_m_NetworkInducedFailureTypeHasCommunicationLinkResourceType: Method = Method(name="NetworkInducedFailureTypeHasCommunicationLinkResourceType", parameters={Parameter(name='pcm_av_av_context', type=StringType), Parameter(name='pcm_av_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_av_reliability_av_av_NetworkInducedFailureType.methods={pcm_av_av_reliability_av_av_NetworkInducedFailureType_m_NetworkInducedFailureTypeHasCommunicationLinkResourceType}

# CommunicationLinkResourceType class attributes and methods

# pcm_av_av_reliability_av_av_ExternalFailureOccurrenceDescription class attributes and methods
pcm_av_av_reliability_av_av_ExternalFailureOccurrenceDescription_m_NoResourceTimeoutFailureAllowedForExternalFailureOccurrenceDescription: Method = Method(name="NoResourceTimeoutFailureAllowedForExternalFailureOccurrenceDescription", parameters={Parameter(name='pcm_av_av_context', type=StringType), Parameter(name='pcm_av_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_av_reliability_av_av_ExternalFailureOccurrenceDescription.methods={pcm_av_av_reliability_av_av_ExternalFailureOccurrenceDescription_m_NoResourceTimeoutFailureAllowedForExternalFailureOccurrenceDescription}

# qos_reliability_av_av_SpecifiedReliabilityAnnotation class attributes and methods

# pcm_av_av_reliability_av_av_ResourceTimeoutFailureType class attributes and methods

# pcm_av_av_reliability_av_av_FailureType class attributes and methods

# pcm_av_av_seff_av_av_StopAction class attributes and methods
pcm_av_av_seff_av_av_StopAction_m_StopActionSuccessorMustNotBeDefined: Method = Method(name="StopActionSuccessorMustNotBeDefined", parameters={Parameter(name='pcm_av_av_context', type=StringType), Parameter(name='pcm_av_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_av_seff_av_av_StopAction.methods={pcm_av_av_seff_av_av_StopAction_m_StopActionSuccessorMustNotBeDefined}

# AbstractInternalControlFlowAction class attributes and methods

# pcm_av_av_seff_av_av_AbstractInternalControlFlowAction class attributes and methods

# AbstractAction class attributes and methods

# pcm_av_av_seff_av_av_AbstractAction class attributes and methods

# ResourceDemandingBehaviour class attributes and methods

# pcm_av_av_seff_av_av_ResourceDemandingBehaviour class attributes and methods
pcm_av_av_seff_av_av_ResourceDemandingBehaviour_m_ExactlyOneStopAction: Method = Method(name="ExactlyOneStopAction", parameters={Parameter(name='pcm_av_av_context', type=StringType), Parameter(name='pcm_av_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_av_seff_av_av_ResourceDemandingBehaviour_m_ExactlyOneStartAction: Method = Method(name="ExactlyOneStartAction", parameters={Parameter(name='pcm_av_av_diagnostics', type=StringType), Parameter(name='pcm_av_av_context', type=StringType)}, type=BooleanType)
pcm_av_av_seff_av_av_ResourceDemandingBehaviour_m_EachActionExceptStartActionandStopActionMustHhaveAPredecessorAndSuccessor: Method = Method(name="EachActionExceptStartActionandStopActionMustHhaveAPredecessorAndSuccessor", parameters={Parameter(name='pcm_av_av_context', type=StringType), Parameter(name='pcm_av_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_av_seff_av_av_ResourceDemandingBehaviour.methods={pcm_av_av_seff_av_av_ResourceDemandingBehaviour_m_EachActionExceptStartActionandStopActionMustHhaveAPredecessorAndSuccessor, pcm_av_av_seff_av_av_ResourceDemandingBehaviour_m_ExactlyOneStartAction, pcm_av_av_seff_av_av_ResourceDemandingBehaviour_m_ExactlyOneStopAction}

# AbstractLoopAction class attributes and methods

# AbstractBranchTransition class attributes and methods

# pcm_av_av_seff_av_av_AbstractLoopAction class attributes and methods

# pcm_av_av_seff_av_av_AbstractBranchTransition class attributes and methods

# BranchAction class attributes and methods

# pcm_av_av_seff_av_av_BranchAction class attributes and methods
pcm_av_av_seff_av_av_BranchAction_m_EitherGuardedBranchesOrProbabilisiticBranchTransitions: Method = Method(name="EitherGuardedBranchesOrProbabilisiticBranchTransitions", parameters={Parameter(name='pcm_av_av_context', type=StringType), Parameter(name='pcm_av_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_av_seff_av_av_BranchAction_m_AllProbabilisticBranchProbabilitiesMustSumUpTo1: Method = Method(name="AllProbabilisticBranchProbabilitiesMustSumUpTo1", parameters={Parameter(name='pcm_av_av_context', type=StringType), Parameter(name='pcm_av_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_av_seff_av_av_BranchAction.methods={pcm_av_av_seff_av_av_BranchAction_m_EitherGuardedBranchesOrProbabilisiticBranchTransitions, pcm_av_av_seff_av_av_BranchAction_m_AllProbabilisticBranchProbabilitiesMustSumUpTo1}

# pcm_av_av_seff_av_av_CallAction class attributes and methods

# pcm_av_av_seff_av_av_StartAction class attributes and methods
pcm_av_av_seff_av_av_StartAction_m_StartActionPredecessorMustNotBeDefined: Method = Method(name="StartActionPredecessorMustNotBeDefined", parameters={Parameter(name='pcm_av_av_diagnostics', type=StringType), Parameter(name='pcm_av_av_context', type=StringType)}, type=BooleanType)
pcm_av_av_seff_av_av_StartAction.methods={pcm_av_av_seff_av_av_StartAction_m_StartActionPredecessorMustNotBeDefined}

# pcm_av_av_seff_av_av_ServiceEffectSpecification class attributes and methods
pcm_av_av_seff_av_av_ServiceEffectSpecification_seffTypeID: Property = Property(name="seffTypeID", type=StringType)
pcm_av_av_seff_av_av_ServiceEffectSpecification_m_ReferencedSignatureMustBelongToInterfaceReferencedByProvidedRole: Method = Method(name="ReferencedSignatureMustBelongToInterfaceReferencedByProvidedRole", parameters={Parameter(name='pcm_av_av_diagnostics', type=StringType), Parameter(name='pcm_av_av_context', type=StringType)}, type=BooleanType)
pcm_av_av_seff_av_av_ServiceEffectSpecification.attributes={pcm_av_av_seff_av_av_ServiceEffectSpecification_seffTypeID}
pcm_av_av_seff_av_av_ServiceEffectSpecification.methods={pcm_av_av_seff_av_av_ServiceEffectSpecification_m_ReferencedSignatureMustBelongToInterfaceReferencedByProvidedRole}

# pcm_av_av_seff_av_av_ResourceDemandingSEFF class attributes and methods

# seff_av_av_ServiceEffectSpecification class attributes and methods

# seff_av_av_ResourceDemandingBehaviour class attributes and methods

# ResourceDemandingInternalBehaviour class attributes and methods

# pcm_av_av_seff_av_av_ResourceDemandingInternalBehaviour class attributes and methods

# ResourceDemandingSEFF class attributes and methods

# pcm_av_av_seff_av_av_ReleaseAction class attributes and methods

# pcm_av_av_seff_av_av_ForkAction class attributes and methods

# ForkedBehaviour class attributes and methods

# pcm_av_av_seff_av_av_ForkedBehaviour class attributes and methods

# ForkAction class attributes and methods

# pcm_av_av_seff_av_av_SynchronisationPoint class attributes and methods

# pcm_av_av_seff_av_av_ExternalCallAction class attributes and methods
pcm_av_av_seff_av_av_ExternalCallAction_retryCount: Property = Property(name="retryCount", type=IntegerType)
pcm_av_av_seff_av_av_ExternalCallAction_m_SignatureBelongsToRole: Method = Method(name="SignatureBelongsToRole", parameters={Parameter(name='pcm_av_av_diagnostics', type=StringType), Parameter(name='pcm_av_av_context', type=StringType)}, type=BooleanType)
pcm_av_av_seff_av_av_ExternalCallAction_m_OperationRequiredRoleMustBeReferencedByContainer: Method = Method(name="OperationRequiredRoleMustBeReferencedByContainer", parameters={Parameter(name='pcm_av_av_context', type=StringType), Parameter(name='pcm_av_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_av_seff_av_av_ExternalCallAction.attributes={pcm_av_av_seff_av_av_ExternalCallAction_retryCount}
pcm_av_av_seff_av_av_ExternalCallAction.methods={pcm_av_av_seff_av_av_ExternalCallAction_m_SignatureBelongsToRole, pcm_av_av_seff_av_av_ExternalCallAction_m_OperationRequiredRoleMustBeReferencedByContainer}

# seff_av_av_AbstractAction class attributes and methods

# seff_av_av_CallReturnAction class attributes and methods

# seff_reliability_av_av_FailureHandlingEntity class attributes and methods

# pcm_av_av_seff_av_av_LoopAction class attributes and methods

# pcm_av_av_seff_av_av_CallReturnAction class attributes and methods

# pcm_av_av_seff_av_av_ProbabilisticBranchTransition class attributes and methods
pcm_av_av_seff_av_av_ProbabilisticBranchTransition_branchProbability: Property = Property(name="branchProbability", type=FloatType)
pcm_av_av_seff_av_av_ProbabilisticBranchTransition.attributes={pcm_av_av_seff_av_av_ProbabilisticBranchTransition_branchProbability}

# pcm_av_av_seff_av_av_AcquireAction class attributes and methods
pcm_av_av_seff_av_av_AcquireAction_timeout: Property = Property(name="timeout", type=BooleanType)
pcm_av_av_seff_av_av_AcquireAction_timeoutValue: Property = Property(name="timeoutValue", type=FloatType)
pcm_av_av_seff_av_av_AcquireAction_m_TimeoutValueOfAcquireActionMustNotBeNegative: Method = Method(name="TimeoutValueOfAcquireActionMustNotBeNegative", parameters={Parameter(name='pcm_av_av_diagnostics', type=StringType), Parameter(name='pcm_av_av_context', type=StringType)}, type=BooleanType)
pcm_av_av_seff_av_av_AcquireAction.attributes={pcm_av_av_seff_av_av_AcquireAction_timeout, pcm_av_av_seff_av_av_AcquireAction_timeoutValue}
pcm_av_av_seff_av_av_AcquireAction.methods={pcm_av_av_seff_av_av_AcquireAction_m_TimeoutValueOfAcquireActionMustNotBeNegative}

# pcm_av_av_seff_av_av_CollectionIteratorAction class attributes and methods

# pcm_av_av_seff_av_av_GuardedBranchTransition class attributes and methods

# pcm_av_av_seff_av_av_SetVariableAction class attributes and methods

# pcm_av_av_seff_av_av_InternalCallAction class attributes and methods

# seff_av_av_CallAction class attributes and methods

# seff_av_av_AbstractInternalControlFlowAction class attributes and methods

# pcm_av_av_seff_av_av_EmitEventAction class attributes and methods

# pcm_av_av_seff_av_av_InternalAction class attributes and methods
pcm_av_av_seff_av_av_InternalAction_m_MultipleInternalOccurrenceDescriptionsPerFailureTypeNotAllowed: Method = Method(name="MultipleInternalOccurrenceDescriptionsPerFailureTypeNotAllowed", parameters={Parameter(name='pcm_av_av_context', type=StringType), Parameter(name='pcm_av_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_av_seff_av_av_InternalAction_m_SumOfInternalActionFailureProbabilitiesMustNotExceed1: Method = Method(name="SumOfInternalActionFailureProbabilitiesMustNotExceed1", parameters={Parameter(name='pcm_av_av_diagnostics', type=StringType), Parameter(name='pcm_av_av_context', type=StringType)}, type=BooleanType)
pcm_av_av_seff_av_av_InternalAction.methods={pcm_av_av_seff_av_av_InternalAction_m_MultipleInternalOccurrenceDescriptionsPerFailureTypeNotAllowed, pcm_av_av_seff_av_av_InternalAction_m_SumOfInternalActionFailureProbabilitiesMustNotExceed1}

# pcm_av_av_seff_performance_av_av_InfrastructureCall class attributes and methods
pcm_av_av_seff_performance_av_av_InfrastructureCall_m_SignatureMustBelongToUsedRequiredRole: Method = Method(name="SignatureMustBelongToUsedRequiredRole", parameters={Parameter(name='pcm_av_av_context', type=StringType), Parameter(name='pcm_av_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_av_seff_performance_av_av_InfrastructureCall_m_ReferencedRequiredRoleMustBeRequiredByComponent: Method = Method(name="ReferencedRequiredRoleMustBeRequiredByComponent", parameters={Parameter(name='pcm_av_av_diagnostics', type=StringType), Parameter(name='pcm_av_av_context', type=StringType)}, type=BooleanType)
pcm_av_av_seff_performance_av_av_InfrastructureCall_m_SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction: Method = Method(name="SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction", parameters={Parameter(name='pcm_av_av_context', type=StringType), Parameter(name='pcm_av_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_av_seff_performance_av_av_InfrastructureCall.methods={pcm_av_av_seff_performance_av_av_InfrastructureCall_m_SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction, pcm_av_av_seff_performance_av_av_InfrastructureCall_m_ReferencedRequiredRoleMustBeRequiredByComponent, pcm_av_av_seff_performance_av_av_InfrastructureCall_m_SignatureMustBelongToUsedRequiredRole}

# pcm_av_av_seff_performance_av_av_ResourceCall class attributes and methods
pcm_av_av_seff_performance_av_av_ResourceCall_m_ResourceSignatureBelongsToResourceRequiredRole: Method = Method(name="ResourceSignatureBelongsToResourceRequiredRole", parameters={Parameter(name='pcm_av_av_context', type=StringType), Parameter(name='pcm_av_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_av_seff_performance_av_av_ResourceCall_m_ResourceRequiredRoleMustBeReferencedByComponent: Method = Method(name="ResourceRequiredRoleMustBeReferencedByComponent", parameters={Parameter(name='pcm_av_av_diagnostics', type=StringType), Parameter(name='pcm_av_av_context', type=StringType)}, type=BooleanType)
pcm_av_av_seff_performance_av_av_ResourceCall_m_SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction: Method = Method(name="SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction", parameters={Parameter(name='pcm_av_av_context', type=StringType), Parameter(name='pcm_av_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_av_seff_performance_av_av_ResourceCall.methods={pcm_av_av_seff_performance_av_av_ResourceCall_m_SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction, pcm_av_av_seff_performance_av_av_ResourceCall_m_ResourceRequiredRoleMustBeReferencedByComponent, pcm_av_av_seff_performance_av_av_ResourceCall_m_ResourceSignatureBelongsToResourceRequiredRole}

# pcm_av_av_seff_performance_av_av_ParametricResourceDemand class attributes and methods
pcm_av_av_seff_performance_av_av_ParametricResourceDemand_m_DemandedProcessingResourceMustBeUniqueWithinAbstractInternalControlFlowAction: Method = Method(name="DemandedProcessingResourceMustBeUniqueWithinAbstractInternalControlFlowAction", parameters={Parameter(name='pcm_av_av_context', type=StringType), Parameter(name='pcm_av_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_av_seff_performance_av_av_ParametricResourceDemand.methods={pcm_av_av_seff_performance_av_av_ParametricResourceDemand_m_DemandedProcessingResourceMustBeUniqueWithinAbstractInternalControlFlowAction}

# pcm_av_av_seff_reliability_av_av_RecoveryActionBehaviour class attributes and methods
pcm_av_av_seff_reliability_av_av_RecoveryActionBehaviour_m_RecoveryActionBehaviourHasOnlyOnePredecessor: Method = Method(name="RecoveryActionBehaviourHasOnlyOnePredecessor", parameters={Parameter(name='pcm_av_av_context', type=StringType), Parameter(name='pcm_av_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_av_seff_reliability_av_av_RecoveryActionBehaviour_m_RecoveryActionBehaviourIsNotSuccessorOfItself: Method = Method(name="RecoveryActionBehaviourIsNotSuccessorOfItself", parameters={Parameter(name='pcm_av_av_context', type=StringType), Parameter(name='pcm_av_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_av_seff_reliability_av_av_RecoveryActionBehaviour_m_SuccessorsOfRecoveryActionBehaviourHandleDisjointFailureTypes: Method = Method(name="SuccessorsOfRecoveryActionBehaviourHandleDisjointFailureTypes", parameters={Parameter(name='pcm_av_av_diagnostics', type=StringType), Parameter(name='pcm_av_av_context', type=StringType)}, type=BooleanType)
pcm_av_av_seff_reliability_av_av_RecoveryActionBehaviour.methods={pcm_av_av_seff_reliability_av_av_RecoveryActionBehaviour_m_SuccessorsOfRecoveryActionBehaviourHandleDisjointFailureTypes, pcm_av_av_seff_reliability_av_av_RecoveryActionBehaviour_m_RecoveryActionBehaviourHasOnlyOnePredecessor, pcm_av_av_seff_reliability_av_av_RecoveryActionBehaviour_m_RecoveryActionBehaviourIsNotSuccessorOfItself}

# seff_reliability_av_av_RecoveryActionBehaviour class attributes and methods

# seff_reliability_av_av_RecoveryAction class attributes and methods

# pcm_av_av_seff_reliability_av_av_RecoveryAction class attributes and methods
pcm_av_av_seff_reliability_av_av_RecoveryAction_m_PrimaryBehaviourOfRecoveryActionMustBeSet: Method = Method(name="PrimaryBehaviourOfRecoveryActionMustBeSet", parameters={Parameter(name='pcm_av_av_context', type=StringType), Parameter(name='pcm_av_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_av_seff_reliability_av_av_RecoveryAction.methods={pcm_av_av_seff_reliability_av_av_RecoveryAction_m_PrimaryBehaviourOfRecoveryActionMustBeSet}

# pcm_av_av_seff_reliability_av_av_FailureHandlingEntity class attributes and methods

# pcm_av_av_qosannotations_av_av_SpecifiedQoSAnnotation class attributes and methods

# QoSAnnotations class attributes and methods

# pcm_av_av_qosannotations_av_av_QoSAnnotations class attributes and methods
pcm_av_av_qosannotations_av_av_QoSAnnotations_m_MultipleReliabilityAnnotationsPerExternalCallNotAllowed: Method = Method(name="MultipleReliabilityAnnotationsPerExternalCallNotAllowed", parameters={Parameter(name='pcm_av_av_diagnostics', type=StringType), Parameter(name='pcm_av_av_context', type=StringType)}, type=BooleanType)
pcm_av_av_qosannotations_av_av_QoSAnnotations.methods={pcm_av_av_qosannotations_av_av_QoSAnnotations_m_MultipleReliabilityAnnotationsPerExternalCallNotAllowed}

# System class attributes and methods

# SpecifiedQoSAnnotation class attributes and methods

# pcm_av_av_qosannotations_av_av_SpecifiedOutputParameterAbstraction class attributes and methods

# pcm_av_av_qos_performance_av_av_SystemSpecifiedExecutionTime class attributes and methods
pcm_av_av_qos_performance_av_av_SystemSpecifiedExecutionTime_m_SystemSpecifiedExecutionTimeMustReferenceRequiredRoleOfASystem: Method = Method(name="SystemSpecifiedExecutionTimeMustReferenceRequiredRoleOfASystem", parameters={Parameter(name='pcm_av_av_diagnostics', type=StringType), Parameter(name='pcm_av_av_context', type=StringType)}, type=BooleanType)
pcm_av_av_qos_performance_av_av_SystemSpecifiedExecutionTime.methods={pcm_av_av_qos_performance_av_av_SystemSpecifiedExecutionTime_m_SystemSpecifiedExecutionTimeMustReferenceRequiredRoleOfASystem}

# SpecifiedExecutionTime class attributes and methods

# pcm_av_av_qos_performance_av_av_SpecifiedExecutionTime class attributes and methods

# pcm_av_av_qos_performance_av_av_ComponentSpecifiedExecutionTime class attributes and methods

# pcm_av_av_qos_reliability_av_av_SpecifiedReliabilityAnnotation class attributes and methods
pcm_av_av_qos_reliability_av_av_SpecifiedReliabilityAnnotation_m_SpecifiedReliabilityAnnotationMustReferenceRequiredRoleOfASystem: Method = Method(name="SpecifiedReliabilityAnnotationMustReferenceRequiredRoleOfASystem", parameters={Parameter(name='pcm_av_av_context', type=StringType), Parameter(name='pcm_av_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_av_qos_reliability_av_av_SpecifiedReliabilityAnnotation_m_SumOfReliabilityAnnotationFailureProbabilitiesMustNotExceed1: Method = Method(name="SumOfReliabilityAnnotationFailureProbabilitiesMustNotExceed1", parameters={Parameter(name='pcm_av_av_diagnostics', type=StringType), Parameter(name='pcm_av_av_context', type=StringType)}, type=BooleanType)
pcm_av_av_qos_reliability_av_av_SpecifiedReliabilityAnnotation_m_MultipleExternalOccurrenceDescriptionsPerFailureTypeNotAllowed: Method = Method(name="MultipleExternalOccurrenceDescriptionsPerFailureTypeNotAllowed", parameters={Parameter(name='pcm_av_av_diagnostics', type=StringType), Parameter(name='pcm_av_av_context', type=StringType)}, type=BooleanType)
pcm_av_av_qos_reliability_av_av_SpecifiedReliabilityAnnotation.methods={pcm_av_av_qos_reliability_av_av_SpecifiedReliabilityAnnotation_m_SpecifiedReliabilityAnnotationMustReferenceRequiredRoleOfASystem, pcm_av_av_qos_reliability_av_av_SpecifiedReliabilityAnnotation_m_SumOfReliabilityAnnotationFailureProbabilitiesMustNotExceed1, pcm_av_av_qos_reliability_av_av_SpecifiedReliabilityAnnotation_m_MultipleExternalOccurrenceDescriptionsPerFailureTypeNotAllowed}

# ExternalFailureOccurrenceDescription class attributes and methods

# pcm_av_av_system_av_av_System class attributes and methods
pcm_av_av_system_av_av_System_m_SystemMustHaveAtLeastOneProvidedRole: Method = Method(name="SystemMustHaveAtLeastOneProvidedRole", parameters={Parameter(name='pcm_av_av_context', type=StringType), Parameter(name='pcm_av_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_av_system_av_av_System.methods={pcm_av_av_system_av_av_System_m_SystemMustHaveAtLeastOneProvidedRole}

# pcm_av_av_resourceenvironment_av_av_ResourceEnvironment class attributes and methods

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
pcm_av_av_resourceenvironment_av_av_ProcessingResourceSpecification.attributes={pcm_av_av_resourceenvironment_av_av_ProcessingResourceSpecification_MTTR, pcm_av_av_resourceenvironment_av_av_ProcessingResourceSpecification_MTTF, pcm_av_av_resourceenvironment_av_av_ProcessingResourceSpecification_requiredByContainer, pcm_av_av_resourceenvironment_av_av_ProcessingResourceSpecification_numberOfReplicas}

# pcm_av_av_resourceenvironment_av_av_CommunicationLinkResourceSpecification class attributes and methods
pcm_av_av_resourceenvironment_av_av_CommunicationLinkResourceSpecification_failureProbability: Property = Property(name="failureProbability", type=FloatType)
pcm_av_av_resourceenvironment_av_av_CommunicationLinkResourceSpecification.attributes={pcm_av_av_resourceenvironment_av_av_CommunicationLinkResourceSpecification_failureProbability}

# pcm_av_av_allocation_av_av_AllocationContext class attributes and methods
pcm_av_av_allocation_av_av_AllocationContext_m_OneAssemblyContextOrOneEventChannelShouldBeReferred: Method = Method(name="OneAssemblyContextOrOneEventChannelShouldBeReferred", parameters={Parameter(name='pcm_av_av_context', type=StringType), Parameter(name='pcm_av_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_av_allocation_av_av_AllocationContext.methods={pcm_av_av_allocation_av_av_AllocationContext_m_OneAssemblyContextOrOneEventChannelShouldBeReferred}

# Allocation class attributes and methods

# pcm_av_av_allocation_av_av_Allocation class attributes and methods
pcm_av_av_allocation_av_av_Allocation_m_EachAssemblyContextWithinSystemHasToBeAllocatedExactlyOnce: Method = Method(name="EachAssemblyContextWithinSystemHasToBeAllocatedExactlyOnce", parameters={Parameter(name='pcm_av_av_diagnostics', type=StringType), Parameter(name='pcm_av_av_context', type=StringType)}, type=BooleanType)
pcm_av_av_allocation_av_av_Allocation_m_CommunicatingServersHaveToBeConnectedByLinkingResource: Method = Method(name="CommunicatingServersHaveToBeConnectedByLinkingResource", parameters={Parameter(name='pcm_av_av_diagnostics', type=StringType), Parameter(name='pcm_av_av_context', type=StringType)}, type=BooleanType)
pcm_av_av_allocation_av_av_Allocation.methods={pcm_av_av_allocation_av_av_Allocation_m_EachAssemblyContextWithinSystemHasToBeAllocatedExactlyOnce, pcm_av_av_allocation_av_av_Allocation_m_CommunicatingServersHaveToBeConnectedByLinkingResource}

# AllocationContext class attributes and methods

# pcm_av_av_subsystem_av_av_SubSystem class attributes and methods

# repository_av_av_RepositoryComponent class attributes and methods

# pcm_av_av_completions_av_av_Completion class attributes and methods

# pcm_av_av_completions_av_av_CompletionRepository class attributes and methods

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
closedWorkload_PCMRandomVariable11: BinaryAssociation = BinaryAssociation(
    name="closedWorkload_PCMRandomVariable11",
    ends={
        Property(name="ClosedWorkload", type=pcm_av_av_core_av_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="thinkTime_ClosedWorkload", type=ClosedWorkload, multiplicity=Multiplicity(0, 1))
    }
)
passiveResource_capacity_PCMRandomVariable12: BinaryAssociation = BinaryAssociation(
    name="passiveResource_capacity_PCMRandomVariable12",
    ends={
        Property(name="PassiveResource", type=pcm_av_av_core_av_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="capacity_PassiveResource", type=PassiveResource, multiplicity=Multiplicity(0, 1))
    }
)
variableCharacterisation_Specification13: BinaryAssociation = BinaryAssociation(
    name="variableCharacterisation_Specification13",
    ends={
        Property(name="VariableCharacterisation", type=pcm_av_av_core_av_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="specification_VariableCharacterisation", type=VariableCharacterisation, multiplicity=Multiplicity(0, 1))
    }
)
infrastructureCall__PCMRandomVariable14: BinaryAssociation = BinaryAssociation(
    name="infrastructureCall__PCMRandomVariable14",
    ends={
        Property(name="InfrastructureCall", type=pcm_av_av_core_av_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="numberOfCalls__InfrastructureCall", type=seff_performance_av_av_InfrastructureCall, multiplicity=Multiplicity(0, 1))
    }
)
resourceCall__PCMRandomVariable15: BinaryAssociation = BinaryAssociation(
    name="resourceCall__PCMRandomVariable15",
    ends={
        Property(name="ResourceCall", type=pcm_av_av_core_av_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="numberOfCalls__ResourceCall", type=seff_performance_av_av_ResourceCall, multiplicity=Multiplicity(0, 1))
    }
)
parametricResourceDemand_PCMRandomVariable16: BinaryAssociation = BinaryAssociation(
    name="parametricResourceDemand_PCMRandomVariable16",
    ends={
        Property(name="ParametricResourceDemand", type=pcm_av_av_core_av_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="specification_ParametericResourceDemand", type=seff_performance_av_av_ParametricResourceDemand, multiplicity=Multiplicity(0, 1))
    }
)
eventChannelSinkConnector__FilterCondition20: BinaryAssociation = BinaryAssociation(
    name="eventChannelSinkConnector__FilterCondition20",
    ends={
        Property(name="EventChannelSinkConnector", type=pcm_av_av_core_av_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="filterCondition__EventChannelSinkConnector", type=composition_av_av_EventChannelSinkConnector, multiplicity=Multiplicity(0, 1))
    }
)
assemblyEventConnector__FilterCondition21: BinaryAssociation = BinaryAssociation(
    name="assemblyEventConnector__FilterCondition21",
    ends={
        Property(name="AssemblyEventConnector", type=pcm_av_av_core_av_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="filterCondition__AssemblyEventConnector", type=composition_av_av_AssemblyEventConnector, multiplicity=Multiplicity(0, 1))
    }
)
loop_LoopIteration22: BinaryAssociation = BinaryAssociation(
    name="loop_LoopIteration22",
    ends={
        Property(name="Loop", type=pcm_av_av_core_av_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="loopIteration_Loop", type=Loop, multiplicity=Multiplicity(0, 1))
    }
)
openWorkload_PCMRandomVariable23: BinaryAssociation = BinaryAssociation(
    name="openWorkload_PCMRandomVariable23",
    ends={
        Property(name="OpenWorkload", type=pcm_av_av_core_av_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="interArrivalTime_OpenWorkload", type=OpenWorkload, multiplicity=Multiplicity(0, 1))
    }
)
delay_TimeSpecification24: BinaryAssociation = BinaryAssociation(
    name="delay_TimeSpecification24",
    ends={
        Property(name="Delay", type=pcm_av_av_core_av_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="timeSpecification_Delay", type=Delay, multiplicity=Multiplicity(0, 1))
    }
)
communicationLinkResourceSpecifcation_throughput_PCMRandomVariable25: BinaryAssociation = BinaryAssociation(
    name="communicationLinkResourceSpecifcation_throughput_PCMRandomVariable25",
    ends={
        Property(name="CommunicationLinkResourceSpecification", type=pcm_av_av_core_av_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="throughput_CommunicationLinkResourceSpecification", type=CommunicationLinkResourceSpecification, multiplicity=Multiplicity(0, 1))
    }
)
processingResourceSpecification_processingRate_PCMRandomVariable26: BinaryAssociation = BinaryAssociation(
    name="processingResourceSpecification_processingRate_PCMRandomVariable26",
    ends={
        Property(name="ProcessingResourceSpecification", type=pcm_av_av_core_av_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="processingRate_ProcessingResourceSpecification", type=ProcessingResourceSpecification, multiplicity=Multiplicity(0, 1))
    }
)
communicationLinkResourceSpecification_latency_PCMRandomVariable27: BinaryAssociation = BinaryAssociation(
    name="communicationLinkResourceSpecification_latency_PCMRandomVariable27",
    ends={
        Property(name="CommunicationLinkResourceSpecification28", type=pcm_av_av_core_av_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="latency_CommunicationLinkResourceSpecification", type=CommunicationLinkResourceSpecification, multiplicity=Multiplicity(0, 1))
    }
)
resourceInterfaceProvidingEntity__ResourceProvidedRole29: BinaryAssociation = BinaryAssociation(
    name="resourceInterfaceProvidingEntity__ResourceProvidedRole29",
    ends={
        Property(name="ResourceInterfaceProvidingEntity", type=pcm_av_av_entity_av_av_ResourceProvidedRole, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceProvidedRoles__ResourceInterfaceProvidingEntity", type=entity_av_av_ResourceInterfaceProvidingEntity, multiplicity=Multiplicity(0, 1))
    }
)
providedResourceInterface__ResourceProvidedRole30: BinaryAssociation = BinaryAssociation(
    name="providedResourceInterface__ResourceProvidedRole30",
    ends={
        Property(name="ResourceInterface", type=pcm_av_av_entity_av_av_ResourceProvidedRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_entity_av_av_ResourceProvidedRole", type=ResourceInterface, multiplicity=Multiplicity(0, 1))
    }
)
providedRoles_InterfaceProvidingEntity31: BinaryAssociation = BinaryAssociation(
    name="providedRoles_InterfaceProvidingEntity31",
    ends={
        Property(name="ProvidedRole", type=pcm_av_av_entity_av_av_InterfaceProvidingEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="providingEntity_ProvidedRole", type=ProvidedRole, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredRoles_InterfaceRequiringEntity32: BinaryAssociation = BinaryAssociation(
    name="requiredRoles_InterfaceRequiringEntity32",
    ends={
        Property(name="RequiredRole", type=pcm_av_av_entity_av_av_InterfaceRequiringEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="requiringEntity_RequiredRole", type=RequiredRole, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceRequiredRoles__ResourceInterfaceRequiringEntity33: BinaryAssociation = BinaryAssociation(
    name="resourceRequiredRoles__ResourceInterfaceRequiringEntity33",
    ends={
        Property(name="ResourceRequiredRole", type=pcm_av_av_entity_av_av_ResourceInterfaceRequiringEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceInterfaceRequiringEntity__ResourceRequiredRole", type=entity_av_av_ResourceRequiredRole, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
loopAction_PCMRandomVariable17: BinaryAssociation = BinaryAssociation(
    name="loopAction_PCMRandomVariable17",
    ends={
        Property(name="LoopAction", type=pcm_av_av_core_av_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="iterationCount_LoopAction", type=LoopAction, multiplicity=Multiplicity(0, 1))
    }
)
guardedBranchTransition_PCMRandomVariable18: BinaryAssociation = BinaryAssociation(
    name="guardedBranchTransition_PCMRandomVariable18",
    ends={
        Property(name="GuardedBranchTransition", type=pcm_av_av_core_av_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="branchCondition_GuardedBranchTransition", type=GuardedBranchTransition, multiplicity=Multiplicity(0, 1))
    }
)
specifiedExecutionTime_PCMRandomVariable19: BinaryAssociation = BinaryAssociation(
    name="specifiedExecutionTime_PCMRandomVariable19",
    ends={
        Property(name="SpecifiedExecutionTime", type=pcm_av_av_core_av_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="specification_SpecifiedExecutionTime", type=qos_performance_av_av_SpecifiedExecutionTime, multiplicity=Multiplicity(0, 1))
    }
)
resourceProvidedRoles__ResourceInterfaceProvidingEntity37: BinaryAssociation = BinaryAssociation(
    name="resourceProvidedRoles__ResourceInterfaceProvidingEntity37",
    ends={
        Property(name="ResourceProvidedRole", type=pcm_av_av_entity_av_av_ResourceInterfaceProvidingEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceInterfaceProvidingEntity__ResourceProvidedRole", type=entity_av_av_ResourceProvidedRole, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentStructure__Connector38: BinaryAssociation = BinaryAssociation(
    name="parentStructure__Connector38",
    ends={
        Property(name="ComposedStructure", type=pcm_av_av_composition_av_av_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="connectors__ComposedStructure", type=composition_av_av_ComposedStructure, multiplicity=Multiplicity(0, 1))
    }
)
requiredResourceInterface__ResourceRequiredRole34: BinaryAssociation = BinaryAssociation(
    name="requiredResourceInterface__ResourceRequiredRole34",
    ends={
        Property(name="ResourceInterface35", type=pcm_av_av_entity_av_av_ResourceRequiredRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_entity_av_av_ResourceRequiredRole", type=ResourceInterface, multiplicity=Multiplicity(0, 1))
    }
)
resourceInterfaceRequiringEntity__ResourceRequiredRole36: BinaryAssociation = BinaryAssociation(
    name="resourceInterfaceRequiringEntity__ResourceRequiredRole36",
    ends={
        Property(name="ResourceInterfaceRequiringEntity", type=pcm_av_av_entity_av_av_ResourceRequiredRole, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceRequiredRoles__ResourceInterfaceRequiringEntity", type=entity_av_av_ResourceInterfaceRequiringEntity, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContexts__ComposedStructure39: BinaryAssociation = BinaryAssociation(
    name="assemblyContexts__ComposedStructure39",
    ends={
        Property(name="AssemblyContext", type=pcm_av_av_composition_av_av_ComposedStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="parentStructure__AssemblyContext", type=composition_av_av_AssemblyContext, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceRequiredDelegationConnectors_ComposedStructure40: BinaryAssociation = BinaryAssociation(
    name="resourceRequiredDelegationConnectors_ComposedStructure40",
    ends={
        Property(name="ResourceRequiredDelegationConnector", type=pcm_av_av_composition_av_av_ComposedStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="parentStructure_ResourceRequiredDelegationConnector", type=composition_av_av_ResourceRequiredDelegationConnector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eventChannel__ComposedStructure41: BinaryAssociation = BinaryAssociation(
    name="eventChannel__ComposedStructure41",
    ends={
        Property(name="EventChannel", type=pcm_av_av_composition_av_av_ComposedStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="parentStructure__EventChannel", type=composition_av_av_EventChannel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connectors__ComposedStructure42: BinaryAssociation = BinaryAssociation(
    name="connectors__ComposedStructure42",
    ends={
        Property(name="Connector", type=pcm_av_av_composition_av_av_ComposedStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="parentStructure__Connector", type=composition_av_av_Connector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
innerResourceRequiredRole_ResourceRequiredDelegationConnector43: BinaryAssociation = BinaryAssociation(
    name="innerResourceRequiredRole_ResourceRequiredDelegationConnector43",
    ends={
        Property(name="entity_av_av_ResourceRequiredRole", type=pcm_av_av_composition_av_av_ResourceRequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_composition_av_av_ResourceRequiredDelegationConnector", type=entity_av_av_ResourceRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
outerResourceRequiredRole_ResourceRequiredDelegationConnector44: BinaryAssociation = BinaryAssociation(
    name="outerResourceRequiredRole_ResourceRequiredDelegationConnector44",
    ends={
        Property(name="entity_av_av_ResourceRequiredRole46", type=pcm_av_av_composition_av_av_ResourceRequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_composition_av_av_ResourceRequiredDelegationConnector45", type=entity_av_av_ResourceRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
parentStructure_ResourceRequiredDelegationConnector47: BinaryAssociation = BinaryAssociation(
    name="parentStructure_ResourceRequiredDelegationConnector47",
    ends={
        Property(name="ComposedStructure48", type=pcm_av_av_composition_av_av_ResourceRequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceRequiredDelegationConnectors_ComposedStructure", type=composition_av_av_ComposedStructure, multiplicity=Multiplicity(0, 1))
    }
)
eventGroup__EventChannel49: BinaryAssociation = BinaryAssociation(
    name="eventGroup__EventChannel49",
    ends={
        Property(name="EventGroup", type=pcm_av_av_composition_av_av_EventChannel, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_composition_av_av_EventChannel", type=EventGroup, multiplicity=Multiplicity(0, 1))
    }
)
eventChannelSourceConnector__EventChannel50: BinaryAssociation = BinaryAssociation(
    name="eventChannelSourceConnector__EventChannel50",
    ends={
        Property(name="EventChannelSourceConnector", type=pcm_av_av_composition_av_av_EventChannel, multiplicity=Multiplicity(1, 1)),
        Property(name="eventChannel__EventChannelSourceConnector", type=composition_av_av_EventChannelSourceConnector, multiplicity=Multiplicity(0, 9999))
    }
)
eventChannelSinkConnector__EventChannel51: BinaryAssociation = BinaryAssociation(
    name="eventChannelSinkConnector__EventChannel51",
    ends={
        Property(name="EventChannelSinkConnector52", type=pcm_av_av_composition_av_av_EventChannel, multiplicity=Multiplicity(1, 1)),
        Property(name="eventChannel__EventChannelSinkConnector", type=composition_av_av_EventChannelSinkConnector, multiplicity=Multiplicity(0, 9999))
    }
)
parentStructure__EventChannel53: BinaryAssociation = BinaryAssociation(
    name="parentStructure__EventChannel53",
    ends={
        Property(name="ComposedStructure54", type=pcm_av_av_composition_av_av_EventChannel, multiplicity=Multiplicity(1, 1)),
        Property(name="eventChannel__ComposedStructure", type=composition_av_av_ComposedStructure, multiplicity=Multiplicity(0, 1))
    }
)
sourceRole__EventChannelSourceRole55: BinaryAssociation = BinaryAssociation(
    name="sourceRole__EventChannelSourceRole55",
    ends={
        Property(name="SourceRole", type=pcm_av_av_composition_av_av_EventChannelSourceConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_composition_av_av_EventChannelSourceConnector", type=SourceRole, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext__EventChannelSourceConnector56: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__EventChannelSourceConnector56",
    ends={
        Property(name="composition_av_av_AssemblyContext", type=pcm_av_av_composition_av_av_EventChannelSourceConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_composition_av_av_EventChannelSourceConnector57", type=composition_av_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
eventChannel__EventChannelSourceConnector58: BinaryAssociation = BinaryAssociation(
    name="eventChannel__EventChannelSourceConnector58",
    ends={
        Property(name="EventChannel59", type=pcm_av_av_composition_av_av_EventChannelSourceConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="eventChannelSourceConnector__EventChannel", type=composition_av_av_EventChannel, multiplicity=Multiplicity(0, 1))
    }
)
sinkRole__EventChannelSinkConnector60: BinaryAssociation = BinaryAssociation(
    name="sinkRole__EventChannelSinkConnector60",
    ends={
        Property(name="SinkRole", type=pcm_av_av_composition_av_av_EventChannelSinkConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_composition_av_av_EventChannelSinkConnector", type=SinkRole, multiplicity=Multiplicity(0, 1))
    }
)
innerProvidedRole_ProvidedDelegationConnector67: BinaryAssociation = BinaryAssociation(
    name="innerProvidedRole_ProvidedDelegationConnector67",
    ends={
        Property(name="OperationProvidedRole", type=pcm_av_av_composition_av_av_ProvidedDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_composition_av_av_ProvidedDelegationConnector", type=OperationProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
outerProvidedRole_ProvidedDelegationConnector68: BinaryAssociation = BinaryAssociation(
    name="outerProvidedRole_ProvidedDelegationConnector68",
    ends={
        Property(name="OperationProvidedRole70", type=pcm_av_av_composition_av_av_ProvidedDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_composition_av_av_ProvidedDelegationConnector69", type=OperationProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext_ProvidedDelegationConnector71: BinaryAssociation = BinaryAssociation(
    name="assemblyContext_ProvidedDelegationConnector71",
    ends={
        Property(name="composition_av_av_AssemblyContext73", type=pcm_av_av_composition_av_av_ProvidedDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_composition_av_av_ProvidedDelegationConnector72", type=composition_av_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
innerRequiredRole_RequiredDelegationConnector74: BinaryAssociation = BinaryAssociation(
    name="innerRequiredRole_RequiredDelegationConnector74",
    ends={
        Property(name="OperationRequiredRole", type=pcm_av_av_composition_av_av_RequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_composition_av_av_RequiredDelegationConnector", type=OperationRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
filterCondition__EventChannelSinkConnector61: BinaryAssociation = BinaryAssociation(
    name="filterCondition__EventChannelSinkConnector61",
    ends={
        Property(name="PCMRandomVariable", type=pcm_av_av_composition_av_av_EventChannelSinkConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="eventChannelSinkConnector__FilterCondition", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assemblyContext__EventChannelSinkConnector62: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__EventChannelSinkConnector62",
    ends={
        Property(name="composition_av_av_AssemblyContext64", type=pcm_av_av_composition_av_av_EventChannelSinkConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_composition_av_av_EventChannelSinkConnector63", type=composition_av_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
eventChannel__EventChannelSinkConnector65: BinaryAssociation = BinaryAssociation(
    name="eventChannel__EventChannelSinkConnector65",
    ends={
        Property(name="EventChannel66", type=pcm_av_av_composition_av_av_EventChannelSinkConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="eventChannelSinkConnector__EventChannel", type=composition_av_av_EventChannel, multiplicity=Multiplicity(0, 1))
    }
)
outerRequiredRole_RequiredDelegationConnector75: BinaryAssociation = BinaryAssociation(
    name="outerRequiredRole_RequiredDelegationConnector75",
    ends={
        Property(name="OperationRequiredRole77", type=pcm_av_av_composition_av_av_RequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_composition_av_av_RequiredDelegationConnector76", type=OperationRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext_RequiredDelegationConnector78: BinaryAssociation = BinaryAssociation(
    name="assemblyContext_RequiredDelegationConnector78",
    ends={
        Property(name="composition_av_av_AssemblyContext80", type=pcm_av_av_composition_av_av_RequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_composition_av_av_RequiredDelegationConnector79", type=composition_av_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
requiringAssemblyContext_AssemblyConnector81: BinaryAssociation = BinaryAssociation(
    name="requiringAssemblyContext_AssemblyConnector81",
    ends={
        Property(name="composition_av_av_AssemblyContext82", type=pcm_av_av_composition_av_av_AssemblyConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_composition_av_av_AssemblyConnector", type=composition_av_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
providingAssemblyContext_AssemblyConnector83: BinaryAssociation = BinaryAssociation(
    name="providingAssemblyContext_AssemblyConnector83",
    ends={
        Property(name="composition_av_av_AssemblyContext85", type=pcm_av_av_composition_av_av_AssemblyConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_composition_av_av_AssemblyConnector84", type=composition_av_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
providedRole_AssemblyConnector86: BinaryAssociation = BinaryAssociation(
    name="providedRole_AssemblyConnector86",
    ends={
        Property(name="OperationProvidedRole88", type=pcm_av_av_composition_av_av_AssemblyConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_composition_av_av_AssemblyConnector87", type=OperationProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
requiredRole_AssemblyConnector89: BinaryAssociation = BinaryAssociation(
    name="requiredRole_AssemblyConnector89",
    ends={
        Property(name="OperationRequiredRole91", type=pcm_av_av_composition_av_av_AssemblyConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_composition_av_av_AssemblyConnector90", type=OperationRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
sinkRole__AssemblyEventConnector92: BinaryAssociation = BinaryAssociation(
    name="sinkRole__AssemblyEventConnector92",
    ends={
        Property(name="SinkRole93", type=pcm_av_av_composition_av_av_AssemblyEventConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_composition_av_av_AssemblyEventConnector", type=SinkRole, multiplicity=Multiplicity(0, 1))
    }
)
sourceRole__AssemblyEventConnector94: BinaryAssociation = BinaryAssociation(
    name="sourceRole__AssemblyEventConnector94",
    ends={
        Property(name="SourceRole96", type=pcm_av_av_composition_av_av_AssemblyEventConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_composition_av_av_AssemblyEventConnector95", type=SourceRole, multiplicity=Multiplicity(0, 1))
    }
)
sinkAssemblyContext__AssemblyEventConnector97: BinaryAssociation = BinaryAssociation(
    name="sinkAssemblyContext__AssemblyEventConnector97",
    ends={
        Property(name="composition_av_av_AssemblyContext99", type=pcm_av_av_composition_av_av_AssemblyEventConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_composition_av_av_AssemblyEventConnector98", type=composition_av_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
sourceAssemblyContext__AssemblyEventConnector100: BinaryAssociation = BinaryAssociation(
    name="sourceAssemblyContext__AssemblyEventConnector100",
    ends={
        Property(name="composition_av_av_AssemblyContext102", type=pcm_av_av_composition_av_av_AssemblyEventConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_composition_av_av_AssemblyEventConnector101", type=composition_av_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
filterCondition__AssemblyEventConnector103: BinaryAssociation = BinaryAssociation(
    name="filterCondition__AssemblyEventConnector103",
    ends={
        Property(name="PCMRandomVariable104", type=pcm_av_av_composition_av_av_AssemblyEventConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="assemblyEventConnector__FilterCondition", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
innerSourceRole__SourceRole105: BinaryAssociation = BinaryAssociation(
    name="innerSourceRole__SourceRole105",
    ends={
        Property(name="SourceRole106", type=pcm_av_av_composition_av_av_SourceDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_composition_av_av_SourceDelegationConnector", type=SourceRole, multiplicity=Multiplicity(0, 1))
    }
)
outerSourceRole__SourceRole107: BinaryAssociation = BinaryAssociation(
    name="outerSourceRole__SourceRole107",
    ends={
        Property(name="SourceRole109", type=pcm_av_av_composition_av_av_SourceDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_composition_av_av_SourceDelegationConnector108", type=SourceRole, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext__SourceDelegationConnector110: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__SourceDelegationConnector110",
    ends={
        Property(name="composition_av_av_AssemblyContext112", type=pcm_av_av_composition_av_av_SourceDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_composition_av_av_SourceDelegationConnector111", type=composition_av_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext__SinkDelegationConnector113: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__SinkDelegationConnector113",
    ends={
        Property(name="composition_av_av_AssemblyContext114", type=pcm_av_av_composition_av_av_SinkDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_composition_av_av_SinkDelegationConnector", type=composition_av_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
innerSinkRole__SinkRole115: BinaryAssociation = BinaryAssociation(
    name="innerSinkRole__SinkRole115",
    ends={
        Property(name="SinkRole117", type=pcm_av_av_composition_av_av_SinkDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_composition_av_av_SinkDelegationConnector116", type=SinkRole, multiplicity=Multiplicity(0, 1))
    }
)
outerSinkRole__SinkRole118: BinaryAssociation = BinaryAssociation(
    name="outerSinkRole__SinkRole118",
    ends={
        Property(name="SinkRole120", type=pcm_av_av_composition_av_av_SinkDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_composition_av_av_SinkDelegationConnector119", type=SinkRole, multiplicity=Multiplicity(0, 1))
    }
)
providedRole__AssemblyInfrastructureConnector121: BinaryAssociation = BinaryAssociation(
    name="providedRole__AssemblyInfrastructureConnector121",
    ends={
        Property(name="InfrastructureProvidedRole", type=pcm_av_av_composition_av_av_AssemblyInfrastructureConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_composition_av_av_AssemblyInfrastructureConnector", type=InfrastructureProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
requiredRole__AssemblyInfrastructureConnector122: BinaryAssociation = BinaryAssociation(
    name="requiredRole__AssemblyInfrastructureConnector122",
    ends={
        Property(name="InfrastructureRequiredRole", type=pcm_av_av_composition_av_av_AssemblyInfrastructureConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_composition_av_av_AssemblyInfrastructureConnector123", type=InfrastructureRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
providingAssemblyContext__AssemblyInfrastructureConnector124: BinaryAssociation = BinaryAssociation(
    name="providingAssemblyContext__AssemblyInfrastructureConnector124",
    ends={
        Property(name="composition_av_av_AssemblyContext126", type=pcm_av_av_composition_av_av_AssemblyInfrastructureConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_composition_av_av_AssemblyInfrastructureConnector125", type=composition_av_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
requiringAssemblyContext__AssemblyInfrastructureConnector127: BinaryAssociation = BinaryAssociation(
    name="requiringAssemblyContext__AssemblyInfrastructureConnector127",
    ends={
        Property(name="composition_av_av_AssemblyContext129", type=pcm_av_av_composition_av_av_AssemblyInfrastructureConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_composition_av_av_AssemblyInfrastructureConnector128", type=composition_av_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
innerProvidedRole__ProvidedInfrastructureDelegationConnector130: BinaryAssociation = BinaryAssociation(
    name="innerProvidedRole__ProvidedInfrastructureDelegationConnector130",
    ends={
        Property(name="InfrastructureProvidedRole131", type=pcm_av_av_composition_av_av_ProvidedInfrastructureDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_composition_av_av_ProvidedInfrastructureDelegationConnector", type=InfrastructureProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
outerProvidedRole__ProvidedInfrastructureDelegationConnector132: BinaryAssociation = BinaryAssociation(
    name="outerProvidedRole__ProvidedInfrastructureDelegationConnector132",
    ends={
        Property(name="InfrastructureProvidedRole134", type=pcm_av_av_composition_av_av_ProvidedInfrastructureDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_composition_av_av_ProvidedInfrastructureDelegationConnector133", type=InfrastructureProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext__ProvidedInfrastructureDelegationConnector135: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__ProvidedInfrastructureDelegationConnector135",
    ends={
        Property(name="composition_av_av_AssemblyContext137", type=pcm_av_av_composition_av_av_ProvidedInfrastructureDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_composition_av_av_ProvidedInfrastructureDelegationConnector136", type=composition_av_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
innerRequiredRole__RequiredInfrastructureDelegationConnector138: BinaryAssociation = BinaryAssociation(
    name="innerRequiredRole__RequiredInfrastructureDelegationConnector138",
    ends={
        Property(name="InfrastructureRequiredRole139", type=pcm_av_av_composition_av_av_RequiredInfrastructureDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_composition_av_av_RequiredInfrastructureDelegationConnector", type=InfrastructureRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
outerRequiredRole__RequiredInfrastructureDelegationConnector140: BinaryAssociation = BinaryAssociation(
    name="outerRequiredRole__RequiredInfrastructureDelegationConnector140",
    ends={
        Property(name="InfrastructureRequiredRole142", type=pcm_av_av_composition_av_av_RequiredInfrastructureDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_composition_av_av_RequiredInfrastructureDelegationConnector141", type=InfrastructureRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext__RequiredInfrastructureDelegationConnector143: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__RequiredInfrastructureDelegationConnector143",
    ends={
        Property(name="composition_av_av_AssemblyContext145", type=pcm_av_av_composition_av_av_RequiredInfrastructureDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_composition_av_av_RequiredInfrastructureDelegationConnector144", type=composition_av_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext__RequiredResourceDelegationConnector146: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__RequiredResourceDelegationConnector146",
    ends={
        Property(name="composition_av_av_AssemblyContext147", type=pcm_av_av_composition_av_av_RequiredResourceDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_composition_av_av_RequiredResourceDelegationConnector", type=composition_av_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
outerRequiredRole__RequiredResourceDelegationConnector151: BinaryAssociation = BinaryAssociation(
    name="outerRequiredRole__RequiredResourceDelegationConnector151",
    ends={
        Property(name="entity_av_av_ResourceRequiredRole153", type=pcm_av_av_composition_av_av_RequiredResourceDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_composition_av_av_RequiredResourceDelegationConnector152", type=entity_av_av_ResourceRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
parentStructure__AssemblyContext154: BinaryAssociation = BinaryAssociation(
    name="parentStructure__AssemblyContext154",
    ends={
        Property(name="ComposedStructure155", type=pcm_av_av_composition_av_av_AssemblyContext, multiplicity=Multiplicity(1, 1)),
        Property(name="assemblyContexts__ComposedStructure", type=composition_av_av_ComposedStructure, multiplicity=Multiplicity(0, 1))
    }
)
encapsulatedComponent__AssemblyContext156: BinaryAssociation = BinaryAssociation(
    name="encapsulatedComponent__AssemblyContext156",
    ends={
        Property(name="RepositoryComponent", type=pcm_av_av_composition_av_av_AssemblyContext, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_composition_av_av_AssemblyContext", type=RepositoryComponent, multiplicity=Multiplicity(0, 1))
    }
)
configParameterUsages__AssemblyContext157: BinaryAssociation = BinaryAssociation(
    name="configParameterUsages__AssemblyContext157",
    ends={
        Property(name="VariableUsage", type=pcm_av_av_composition_av_av_AssemblyContext, multiplicity=Multiplicity(1, 1)),
        Property(name="assemblyContext__VariableUsage", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
usageScenario_Workload158: BinaryAssociation = BinaryAssociation(
    name="usageScenario_Workload158",
    ends={
        Property(name="UsageScenario", type=pcm_av_av_usagemodel_av_av_Workload, multiplicity=Multiplicity(1, 1)),
        Property(name="workload_UsageScenario", type=UsageScenario, multiplicity=Multiplicity(0, 1))
    }
)
usageModel_UsageScenario159: BinaryAssociation = BinaryAssociation(
    name="usageModel_UsageScenario159",
    ends={
        Property(name="UsageModel", type=pcm_av_av_usagemodel_av_av_UsageScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="usageScenario_UsageModel", type=UsageModel, multiplicity=Multiplicity(0, 1))
    }
)
scenarioBehaviour_UsageScenario160: BinaryAssociation = BinaryAssociation(
    name="scenarioBehaviour_UsageScenario160",
    ends={
        Property(name="ScenarioBehaviour", type=pcm_av_av_usagemodel_av_av_UsageScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="usageScenario_SenarioBehaviour", type=ScenarioBehaviour, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
workload_UsageScenario161: BinaryAssociation = BinaryAssociation(
    name="workload_UsageScenario161",
    ends={
        Property(name="Workload", type=pcm_av_av_usagemodel_av_av_UsageScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="usageScenario_Workload", type=Workload, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assemblyContext_userData162: BinaryAssociation = BinaryAssociation(
    name="assemblyContext_userData162",
    ends={
        Property(name="composition_av_av_AssemblyContext163", type=pcm_av_av_usagemodel_av_av_UserData, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_usagemodel_av_av_UserData", type=composition_av_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
usageModel_UserData164: BinaryAssociation = BinaryAssociation(
    name="usageModel_UserData164",
    ends={
        Property(name="UsageModel165", type=pcm_av_av_usagemodel_av_av_UserData, multiplicity=Multiplicity(1, 1)),
        Property(name="userData_UsageModel", type=UsageModel, multiplicity=Multiplicity(0, 1))
    }
)
userDataParameterUsages_UserData166: BinaryAssociation = BinaryAssociation(
    name="userDataParameterUsages_UserData166",
    ends={
        Property(name="VariableUsage167", type=pcm_av_av_usagemodel_av_av_UserData, multiplicity=Multiplicity(1, 1)),
        Property(name="userData_VariableUsage", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
usageScenario_UsageModel168: BinaryAssociation = BinaryAssociation(
    name="usageScenario_UsageModel168",
    ends={
        Property(name="UsageScenario169", type=pcm_av_av_usagemodel_av_av_UsageModel, multiplicity=Multiplicity(1, 1)),
        Property(name="usageModel_UsageScenario", type=UsageScenario, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
userData_UsageModel170: BinaryAssociation = BinaryAssociation(
    name="userData_UsageModel170",
    ends={
        Property(name="UserData", type=pcm_av_av_usagemodel_av_av_UsageModel, multiplicity=Multiplicity(1, 1)),
        Property(name="usageModel_UserData", type=UserData, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
innerRequiredRole__RequiredResourceDelegationConnector148: BinaryAssociation = BinaryAssociation(
    name="innerRequiredRole__RequiredResourceDelegationConnector148",
    ends={
        Property(name="entity_av_av_ResourceRequiredRole150", type=pcm_av_av_composition_av_av_RequiredResourceDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_composition_av_av_RequiredResourceDelegationConnector149", type=entity_av_av_ResourceRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
providedRole_EntryLevelSystemCall171: BinaryAssociation = BinaryAssociation(
    name="providedRole_EntryLevelSystemCall171",
    ends={
        Property(name="OperationProvidedRole172", type=pcm_av_av_usagemodel_av_av_EntryLevelSystemCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_usagemodel_av_av_EntryLevelSystemCall", type=OperationProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
operationSignature__EntryLevelSystemCall173: BinaryAssociation = BinaryAssociation(
    name="operationSignature__EntryLevelSystemCall173",
    ends={
        Property(name="OperationSignature", type=pcm_av_av_usagemodel_av_av_EntryLevelSystemCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_usagemodel_av_av_EntryLevelSystemCall174", type=OperationSignature, multiplicity=Multiplicity(0, 1))
    }
)
outputParameterUsages_EntryLevelSystemCall175: BinaryAssociation = BinaryAssociation(
    name="outputParameterUsages_EntryLevelSystemCall175",
    ends={
        Property(name="VariableUsage176", type=pcm_av_av_usagemodel_av_av_EntryLevelSystemCall, multiplicity=Multiplicity(1, 1)),
        Property(name="entryLevelSystemCall_OutputParameterUsage", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputParameterUsages_EntryLevelSystemCall177: BinaryAssociation = BinaryAssociation(
    name="inputParameterUsages_EntryLevelSystemCall177",
    ends={
        Property(name="VariableUsage178", type=pcm_av_av_usagemodel_av_av_EntryLevelSystemCall, multiplicity=Multiplicity(1, 1)),
        Property(name="entryLevelSystemCall_InputParameterUsage", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
successor179: BinaryAssociation = BinaryAssociation(
    name="successor179",
    ends={
        Property(name="AbstractUserAction", type=pcm_av_av_usagemodel_av_av_AbstractUserAction, multiplicity=Multiplicity(1, 1)),
        Property(name="predecessor", type=AbstractUserAction, multiplicity=Multiplicity(0, 1))
    }
)
predecessor180: BinaryAssociation = BinaryAssociation(
    name="predecessor180",
    ends={
        Property(name="AbstractUserAction181", type=pcm_av_av_usagemodel_av_av_AbstractUserAction, multiplicity=Multiplicity(1, 1)),
        Property(name="successor", type=AbstractUserAction, multiplicity=Multiplicity(0, 1))
    }
)
scenarioBehaviour_AbstractUserAction182: BinaryAssociation = BinaryAssociation(
    name="scenarioBehaviour_AbstractUserAction182",
    ends={
        Property(name="ScenarioBehaviour183", type=pcm_av_av_usagemodel_av_av_AbstractUserAction, multiplicity=Multiplicity(1, 1)),
        Property(name="actions_ScenarioBehaviour", type=ScenarioBehaviour, multiplicity=Multiplicity(0, 1))
    }
)
usageScenario_SenarioBehaviour184: BinaryAssociation = BinaryAssociation(
    name="usageScenario_SenarioBehaviour184",
    ends={
        Property(name="UsageScenario185", type=pcm_av_av_usagemodel_av_av_ScenarioBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="scenarioBehaviour_UsageScenario", type=UsageScenario, multiplicity=Multiplicity(0, 1))
    }
)
branchTransition_ScenarioBehaviour186: BinaryAssociation = BinaryAssociation(
    name="branchTransition_ScenarioBehaviour186",
    ends={
        Property(name="BranchTransition", type=pcm_av_av_usagemodel_av_av_ScenarioBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="branchedBehaviour_BranchTransition", type=BranchTransition, multiplicity=Multiplicity(0, 1))
    }
)
actions_ScenarioBehaviour189: BinaryAssociation = BinaryAssociation(
    name="actions_ScenarioBehaviour189",
    ends={
        Property(name="AbstractUserAction190", type=pcm_av_av_usagemodel_av_av_ScenarioBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="scenarioBehaviour_AbstractUserAction", type=AbstractUserAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
branch_BranchTransition191: BinaryAssociation = BinaryAssociation(
    name="branch_BranchTransition191",
    ends={
        Property(name="Branch", type=pcm_av_av_usagemodel_av_av_BranchTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="branchTransitions_Branch", type=Branch, multiplicity=Multiplicity(0, 1))
    }
)
branchedBehaviour_BranchTransition192: BinaryAssociation = BinaryAssociation(
    name="branchedBehaviour_BranchTransition192",
    ends={
        Property(name="ScenarioBehaviour193", type=pcm_av_av_usagemodel_av_av_BranchTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="branchTransition_ScenarioBehaviour", type=ScenarioBehaviour, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
branchTransitions_Branch194: BinaryAssociation = BinaryAssociation(
    name="branchTransitions_Branch194",
    ends={
        Property(name="BranchTransition195", type=pcm_av_av_usagemodel_av_av_Branch, multiplicity=Multiplicity(1, 1)),
        Property(name="branch_BranchTransition", type=BranchTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
loopIteration_Loop196: BinaryAssociation = BinaryAssociation(
    name="loopIteration_Loop196",
    ends={
        Property(name="PCMRandomVariable197", type=pcm_av_av_usagemodel_av_av_Loop, multiplicity=Multiplicity(1, 1)),
        Property(name="loop_LoopIteration", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bodyBehaviour_Loop198: BinaryAssociation = BinaryAssociation(
    name="bodyBehaviour_Loop198",
    ends={
        Property(name="ScenarioBehaviour199", type=pcm_av_av_usagemodel_av_av_Loop, multiplicity=Multiplicity(1, 1)),
        Property(name="loop_ScenarioBehaviour", type=ScenarioBehaviour, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
loop_ScenarioBehaviour187: BinaryAssociation = BinaryAssociation(
    name="loop_ScenarioBehaviour187",
    ends={
        Property(name="Loop188", type=pcm_av_av_usagemodel_av_av_ScenarioBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="bodyBehaviour_Loop", type=Loop, multiplicity=Multiplicity(0, 1))
    }
)
interArrivalTime_OpenWorkload200: BinaryAssociation = BinaryAssociation(
    name="interArrivalTime_OpenWorkload200",
    ends={
        Property(name="PCMRandomVariable201", type=pcm_av_av_usagemodel_av_av_OpenWorkload, multiplicity=Multiplicity(1, 1)),
        Property(name="openWorkload_PCMRandomVariable", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
timeSpecification_Delay202: BinaryAssociation = BinaryAssociation(
    name="timeSpecification_Delay202",
    ends={
        Property(name="PCMRandomVariable203", type=pcm_av_av_usagemodel_av_av_Delay, multiplicity=Multiplicity(1, 1)),
        Property(name="delay_TimeSpecification", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thinkTime_ClosedWorkload204: BinaryAssociation = BinaryAssociation(
    name="thinkTime_ClosedWorkload204",
    ends={
        Property(name="PCMRandomVariable205", type=pcm_av_av_usagemodel_av_av_ClosedWorkload, multiplicity=Multiplicity(1, 1)),
        Property(name="closedWorkload_PCMRandomVariable", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
capacity_PassiveResource206: BinaryAssociation = BinaryAssociation(
    name="capacity_PassiveResource206",
    ends={
        Property(name="PCMRandomVariable207", type=pcm_av_av_repository_av_av_PassiveResource, multiplicity=Multiplicity(1, 1)),
        Property(name="passiveResource_capacity_PCMRandomVariable", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
basicComponent_PassiveResource208: BinaryAssociation = BinaryAssociation(
    name="basicComponent_PassiveResource208",
    ends={
        Property(name="BasicComponent", type=pcm_av_av_repository_av_av_PassiveResource, multiplicity=Multiplicity(1, 1)),
        Property(name="passiveResource_BasicComponent", type=BasicComponent, multiplicity=Multiplicity(0, 1))
    }
)
resourceTimeoutFailureType__PassiveResource209: BinaryAssociation = BinaryAssociation(
    name="resourceTimeoutFailureType__PassiveResource209",
    ends={
        Property(name="ResourceTimeoutFailureType", type=pcm_av_av_repository_av_av_PassiveResource, multiplicity=Multiplicity(1, 1)),
        Property(name="passiveResource__ResourceTimeoutFailureType", type=ResourceTimeoutFailureType, multiplicity=Multiplicity(0, 1))
    }
)
serviceEffectSpecifications__BasicComponent210: BinaryAssociation = BinaryAssociation(
    name="serviceEffectSpecifications__BasicComponent210",
    ends={
        Property(name="ServiceEffectSpecification", type=pcm_av_av_repository_av_av_BasicComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="basicComponent_ServiceEffectSpecification", type=ServiceEffectSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
passiveResource_BasicComponent211: BinaryAssociation = BinaryAssociation(
    name="passiveResource_BasicComponent211",
    ends={
        Property(name="PassiveResource212", type=pcm_av_av_repository_av_av_BasicComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="basicComponent_PassiveResource", type=PassiveResource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentCompleteComponentTypes213: BinaryAssociation = BinaryAssociation(
    name="parentCompleteComponentTypes213",
    ends={
        Property(name="CompleteComponentType", type=pcm_av_av_repository_av_av_ImplementationComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_repository_av_av_ImplementationComponentType", type=CompleteComponentType, multiplicity=Multiplicity(0, 9999))
    }
)
componentParameterUsage_ImplementationComponentType214: BinaryAssociation = BinaryAssociation(
    name="componentParameterUsage_ImplementationComponentType214",
    ends={
        Property(name="VariableUsage216", type=pcm_av_av_repository_av_av_ImplementationComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_repository_av_av_ImplementationComponentType215", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
repository__RepositoryComponent217: BinaryAssociation = BinaryAssociation(
    name="repository__RepositoryComponent217",
    ends={
        Property(name="Repository", type=pcm_av_av_repository_av_av_RepositoryComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="components__Repository", type=Repository, multiplicity=Multiplicity(0, 1))
    }
)
providingEntity_ProvidedRole218: BinaryAssociation = BinaryAssociation(
    name="providingEntity_ProvidedRole218",
    ends={
        Property(name="InterfaceProvidingEntity", type=pcm_av_av_repository_av_av_ProvidedRole, multiplicity=Multiplicity(1, 1)),
        Property(name="providedRoles_InterfaceProvidingEntity", type=entity_av_av_InterfaceProvidingEntity, multiplicity=Multiplicity(0, 1))
    }
)
dataType__Parameter219: BinaryAssociation = BinaryAssociation(
    name="dataType__Parameter219",
    ends={
        Property(name="DataType", type=pcm_av_av_repository_av_av_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_repository_av_av_Parameter", type=DataType, multiplicity=Multiplicity(0, 1))
    }
)
infrastructureSignature__Parameter220: BinaryAssociation = BinaryAssociation(
    name="infrastructureSignature__Parameter220",
    ends={
        Property(name="InfrastructureSignature", type=pcm_av_av_repository_av_av_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameters__InfrastructureSignature", type=InfrastructureSignature, multiplicity=Multiplicity(0, 1))
    }
)
operationSignature__Parameter221: BinaryAssociation = BinaryAssociation(
    name="operationSignature__Parameter221",
    ends={
        Property(name="OperationSignature222", type=pcm_av_av_repository_av_av_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameters__OperationSignature", type=OperationSignature, multiplicity=Multiplicity(0, 1))
    }
)
eventType__Parameter223: BinaryAssociation = BinaryAssociation(
    name="eventType__Parameter223",
    ends={
        Property(name="EventType", type=pcm_av_av_repository_av_av_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameter__EventType", type=EventType, multiplicity=Multiplicity(0, 1))
    }
)
resourceSignature__Parameter224: BinaryAssociation = BinaryAssociation(
    name="resourceSignature__Parameter224",
    ends={
        Property(name="ResourceSignature", type=pcm_av_av_repository_av_av_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameter__ResourceSignature", type=ResourceSignature, multiplicity=Multiplicity(0, 1))
    }
)
repository__DataType225: BinaryAssociation = BinaryAssociation(
    name="repository__DataType225",
    ends={
        Property(name="Repository226", type=pcm_av_av_repository_av_av_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="dataTypes__Repository", type=Repository, multiplicity=Multiplicity(0, 1))
    }
)
components__Repository227: BinaryAssociation = BinaryAssociation(
    name="components__Repository227",
    ends={
        Property(name="RepositoryComponent228", type=pcm_av_av_repository_av_av_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="repository__RepositoryComponent", type=RepositoryComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
interfaces__Repository229: BinaryAssociation = BinaryAssociation(
    name="interfaces__Repository229",
    ends={
        Property(name="Interface", type=pcm_av_av_repository_av_av_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="repository__Interface", type=Interface, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
failureTypes__Repository230: BinaryAssociation = BinaryAssociation(
    name="failureTypes__Repository230",
    ends={
        Property(name="FailureType", type=pcm_av_av_repository_av_av_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="repository__FailureType", type=FailureType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataTypes__Repository231: BinaryAssociation = BinaryAssociation(
    name="dataTypes__Repository231",
    ends={
        Property(name="DataType232", type=pcm_av_av_repository_av_av_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="repository__DataType", type=DataType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentInterfaces__Interface233: BinaryAssociation = BinaryAssociation(
    name="parentInterfaces__Interface233",
    ends={
        Property(name="Interface234", type=pcm_av_av_repository_av_av_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_repository_av_av_Interface", type=Interface, multiplicity=Multiplicity(0, 9999))
    }
)
protocols__Interface235: BinaryAssociation = BinaryAssociation(
    name="protocols__Interface235",
    ends={
        Property(name="Protocol", type=pcm_av_av_repository_av_av_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_repository_av_av_Interface236", type=Protocol, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredCharacterisations237: BinaryAssociation = BinaryAssociation(
    name="requiredCharacterisations237",
    ends={
        Property(name="RequiredCharacterisation", type=pcm_av_av_repository_av_av_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="interface_RequiredCharacterisation", type=RequiredCharacterisation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
repository__Interface238: BinaryAssociation = BinaryAssociation(
    name="repository__Interface238",
    ends={
        Property(name="Repository239", type=pcm_av_av_repository_av_av_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="interfaces__Repository", type=Repository, multiplicity=Multiplicity(0, 1))
    }
)
parameter240: BinaryAssociation = BinaryAssociation(
    name="parameter240",
    ends={
        Property(name="Parameter", type=pcm_av_av_repository_av_av_RequiredCharacterisation, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_repository_av_av_RequiredCharacterisation", type=Parameter_, multiplicity=Multiplicity(0, 1))
    }
)
interface_RequiredCharacterisation241: BinaryAssociation = BinaryAssociation(
    name="interface_RequiredCharacterisation241",
    ends={
        Property(name="Interface242", type=pcm_av_av_repository_av_av_RequiredCharacterisation, multiplicity=Multiplicity(1, 1)),
        Property(name="requiredCharacterisations", type=Interface, multiplicity=Multiplicity(0, 1))
    }
)
eventTypes__EventGroup243: BinaryAssociation = BinaryAssociation(
    name="eventTypes__EventGroup243",
    ends={
        Property(name="EventType244", type=pcm_av_av_repository_av_av_EventGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="eventGroup__EventType", type=EventType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eventGroup__EventType247: BinaryAssociation = BinaryAssociation(
    name="eventGroup__EventType247",
    ends={
        Property(name="EventGroup248", type=pcm_av_av_repository_av_av_EventType, multiplicity=Multiplicity(1, 1)),
        Property(name="eventTypes__EventGroup", type=EventGroup, multiplicity=Multiplicity(0, 1))
    }
)
exceptions__Signature249: BinaryAssociation = BinaryAssociation(
    name="exceptions__Signature249",
    ends={
        Property(name="ExceptionType", type=pcm_av_av_repository_av_av_Signature, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_repository_av_av_Signature", type=ExceptionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
failureType250: BinaryAssociation = BinaryAssociation(
    name="failureType250",
    ends={
        Property(name="FailureType252", type=pcm_av_av_repository_av_av_Signature, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_repository_av_av_Signature251", type=FailureType, multiplicity=Multiplicity(0, 9999))
    }
)
parameters__InfrastructureSignature253: BinaryAssociation = BinaryAssociation(
    name="parameters__InfrastructureSignature253",
    ends={
        Property(name="Parameter254", type=pcm_av_av_repository_av_av_InfrastructureSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="infrastructureSignature__Parameter", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
infrastructureInterface__InfrastructureSignature255: BinaryAssociation = BinaryAssociation(
    name="infrastructureInterface__InfrastructureSignature255",
    ends={
        Property(name="InfrastructureInterface", type=pcm_av_av_repository_av_av_InfrastructureSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="infrastructureSignatures__InfrastructureInterface", type=InfrastructureInterface, multiplicity=Multiplicity(0, 1))
    }
)
infrastructureSignatures__InfrastructureInterface256: BinaryAssociation = BinaryAssociation(
    name="infrastructureSignatures__InfrastructureInterface256",
    ends={
        Property(name="InfrastructureSignature257", type=pcm_av_av_repository_av_av_InfrastructureInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="infrastructureInterface__InfrastructureSignature", type=InfrastructureSignature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredInterface__InfrastructureRequiredRole258: BinaryAssociation = BinaryAssociation(
    name="requiredInterface__InfrastructureRequiredRole258",
    ends={
        Property(name="InfrastructureInterface259", type=pcm_av_av_repository_av_av_InfrastructureRequiredRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_repository_av_av_InfrastructureRequiredRole", type=InfrastructureInterface, multiplicity=Multiplicity(0, 1))
    }
)
requiringEntity_RequiredRole260: BinaryAssociation = BinaryAssociation(
    name="requiringEntity_RequiredRole260",
    ends={
        Property(name="InterfaceRequiringEntity", type=pcm_av_av_repository_av_av_RequiredRole, multiplicity=Multiplicity(1, 1)),
        Property(name="requiredRoles_InterfaceRequiringEntity", type=entity_av_av_InterfaceRequiringEntity, multiplicity=Multiplicity(0, 1))
    }
)
parameter__EventType245: BinaryAssociation = BinaryAssociation(
    name="parameter__EventType245",
    ends={
        Property(name="Parameter246", type=pcm_av_av_repository_av_av_EventType, multiplicity=Multiplicity(1, 1)),
        Property(name="eventType__Parameter", type=Parameter_, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters__OperationSignature262: BinaryAssociation = BinaryAssociation(
    name="parameters__OperationSignature262",
    ends={
        Property(name="Parameter263", type=pcm_av_av_repository_av_av_OperationSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="operationSignature__Parameter", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnType__OperationSignature264: BinaryAssociation = BinaryAssociation(
    name="returnType__OperationSignature264",
    ends={
        Property(name="DataType265", type=pcm_av_av_repository_av_av_OperationSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_repository_av_av_OperationSignature", type=DataType, multiplicity=Multiplicity(0, 1))
    }
)
signatures__OperationInterface266: BinaryAssociation = BinaryAssociation(
    name="signatures__OperationInterface266",
    ends={
        Property(name="OperationSignature267", type=pcm_av_av_repository_av_av_OperationInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="interface__OperationSignature", type=OperationSignature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredInterface__OperationRequiredRole268: BinaryAssociation = BinaryAssociation(
    name="requiredInterface__OperationRequiredRole268",
    ends={
        Property(name="OperationInterface269", type=pcm_av_av_repository_av_av_OperationRequiredRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_repository_av_av_OperationRequiredRole", type=OperationInterface, multiplicity=Multiplicity(0, 1))
    }
)
eventGroup__SourceRole270: BinaryAssociation = BinaryAssociation(
    name="eventGroup__SourceRole270",
    ends={
        Property(name="EventGroup271", type=pcm_av_av_repository_av_av_SourceRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_repository_av_av_SourceRole", type=EventGroup, multiplicity=Multiplicity(0, 1))
    }
)
eventGroup__SinkRole272: BinaryAssociation = BinaryAssociation(
    name="eventGroup__SinkRole272",
    ends={
        Property(name="EventGroup273", type=pcm_av_av_repository_av_av_SinkRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_repository_av_av_SinkRole", type=EventGroup, multiplicity=Multiplicity(0, 1))
    }
)
providedInterface__OperationProvidedRole274: BinaryAssociation = BinaryAssociation(
    name="providedInterface__OperationProvidedRole274",
    ends={
        Property(name="OperationInterface275", type=pcm_av_av_repository_av_av_OperationProvidedRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_repository_av_av_OperationProvidedRole", type=OperationInterface, multiplicity=Multiplicity(0, 1))
    }
)
providedInterface__InfrastructureProvidedRole276: BinaryAssociation = BinaryAssociation(
    name="providedInterface__InfrastructureProvidedRole276",
    ends={
        Property(name="InfrastructureInterface277", type=pcm_av_av_repository_av_av_InfrastructureProvidedRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_repository_av_av_InfrastructureProvidedRole", type=InfrastructureInterface, multiplicity=Multiplicity(0, 1))
    }
)
interface__OperationSignature261: BinaryAssociation = BinaryAssociation(
    name="interface__OperationSignature261",
    ends={
        Property(name="OperationInterface", type=pcm_av_av_repository_av_av_OperationSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="signatures__OperationInterface", type=OperationInterface, multiplicity=Multiplicity(0, 1))
    }
)
parentProvidesComponentTypes278: BinaryAssociation = BinaryAssociation(
    name="parentProvidesComponentTypes278",
    ends={
        Property(name="ProvidesComponentType", type=pcm_av_av_repository_av_av_CompleteComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_repository_av_av_CompleteComponentType", type=ProvidesComponentType, multiplicity=Multiplicity(0, 9999))
    }
)
innerType_CollectionDataType279: BinaryAssociation = BinaryAssociation(
    name="innerType_CollectionDataType279",
    ends={
        Property(name="DataType280", type=pcm_av_av_repository_av_av_CollectionDataType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_repository_av_av_CollectionDataType", type=DataType, multiplicity=Multiplicity(0, 1))
    }
)
parentType_CompositeDataType281: BinaryAssociation = BinaryAssociation(
    name="parentType_CompositeDataType281",
    ends={
        Property(name="CompositeDataType", type=pcm_av_av_repository_av_av_CompositeDataType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_repository_av_av_CompositeDataType", type=CompositeDataType, multiplicity=Multiplicity(0, 9999))
    }
)
innerDeclaration_CompositeDataType282: BinaryAssociation = BinaryAssociation(
    name="innerDeclaration_CompositeDataType282",
    ends={
        Property(name="InnerDeclaration", type=pcm_av_av_repository_av_av_CompositeDataType, multiplicity=Multiplicity(1, 1)),
        Property(name="compositeDataType_InnerDeclaration", type=InnerDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
datatype_InnerDeclaration283: BinaryAssociation = BinaryAssociation(
    name="datatype_InnerDeclaration283",
    ends={
        Property(name="DataType284", type=pcm_av_av_repository_av_av_InnerDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_repository_av_av_InnerDeclaration", type=DataType, multiplicity=Multiplicity(0, 1))
    }
)
compositeDataType_InnerDeclaration285: BinaryAssociation = BinaryAssociation(
    name="compositeDataType_InnerDeclaration285",
    ends={
        Property(name="CompositeDataType286", type=pcm_av_av_repository_av_av_InnerDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="innerDeclaration_CompositeDataType", type=CompositeDataType, multiplicity=Multiplicity(0, 1))
    }
)
parameter__ResourceSignature287: BinaryAssociation = BinaryAssociation(
    name="parameter__ResourceSignature287",
    ends={
        Property(name="Parameter288", type=pcm_av_av_resourcetype_av_av_ResourceSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceSignature__Parameter", type=Parameter_, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resourceInterface__ResourceSignature289: BinaryAssociation = BinaryAssociation(
    name="resourceInterface__ResourceSignature289",
    ends={
        Property(name="ResourceInterface290", type=pcm_av_av_resourcetype_av_av_ResourceSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceSignatures__ResourceInterface", type=ResourceInterface, multiplicity=Multiplicity(0, 1))
    }
)
resourceRepository_ResourceType292: BinaryAssociation = BinaryAssociation(
    name="resourceRepository_ResourceType292",
    ends={
        Property(name="ResourceRepository", type=pcm_av_av_resourcetype_av_av_ResourceType, multiplicity=Multiplicity(1, 1)),
        Property(name="availableResourceTypes_ResourceRepository", type=ResourceRepository, multiplicity=Multiplicity(0, 1))
    }
)
resourceInterfaces__ResourceRepository293: BinaryAssociation = BinaryAssociation(
    name="resourceInterfaces__ResourceRepository293",
    ends={
        Property(name="ResourceInterface294", type=pcm_av_av_resourcetype_av_av_ResourceRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceRepository__ResourceInterface", type=ResourceInterface, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
schedulingPolicies__ResourceRepository295: BinaryAssociation = BinaryAssociation(
    name="schedulingPolicies__ResourceRepository295",
    ends={
        Property(name="SchedulingPolicy", type=pcm_av_av_resourcetype_av_av_ResourceRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceRepository__SchedulingPolicy", type=SchedulingPolicy, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
availableResourceTypes_ResourceRepository296: BinaryAssociation = BinaryAssociation(
    name="availableResourceTypes_ResourceRepository296",
    ends={
        Property(name="ResourceType", type=pcm_av_av_resourcetype_av_av_ResourceRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceRepository_ResourceType", type=ResourceType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceRepository__SchedulingPolicy297: BinaryAssociation = BinaryAssociation(
    name="resourceRepository__SchedulingPolicy297",
    ends={
        Property(name="ResourceRepository298", type=pcm_av_av_resourcetype_av_av_SchedulingPolicy, multiplicity=Multiplicity(1, 1)),
        Property(name="schedulingPolicies__ResourceRepository", type=ResourceRepository, multiplicity=Multiplicity(0, 1))
    }
)
networkInducedFailureType__CommunicationLinkResourceType299: BinaryAssociation = BinaryAssociation(
    name="networkInducedFailureType__CommunicationLinkResourceType299",
    ends={
        Property(name="NetworkInducedFailureType", type=pcm_av_av_resourcetype_av_av_CommunicationLinkResourceType, multiplicity=Multiplicity(1, 1)),
        Property(name="communicationLinkResourceType__NetworkInducedFailureType", type=NetworkInducedFailureType, multiplicity=Multiplicity(0, 1))
    }
)
resourceRepository__ResourceInterface300: BinaryAssociation = BinaryAssociation(
    name="resourceRepository__ResourceInterface300",
    ends={
        Property(name="ResourceRepository301", type=pcm_av_av_resourcetype_av_av_ResourceInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceInterfaces__ResourceRepository", type=ResourceRepository, multiplicity=Multiplicity(0, 1))
    }
)
resourceSignatures__ResourceInterface302: BinaryAssociation = BinaryAssociation(
    name="resourceSignatures__ResourceInterface302",
    ends={
        Property(name="ResourceSignature303", type=pcm_av_av_resourcetype_av_av_ResourceInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceInterface__ResourceSignature", type=ResourceSignature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variableCharacterisation_VariableUsage304: BinaryAssociation = BinaryAssociation(
    name="variableCharacterisation_VariableUsage304",
    ends={
        Property(name="VariableCharacterisation305", type=pcm_av_av_parameter_av_av_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="variableUsage_VariableCharacterisation", type=VariableCharacterisation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
userData_VariableUsage306: BinaryAssociation = BinaryAssociation(
    name="userData_VariableUsage306",
    ends={
        Property(name="UserData307", type=pcm_av_av_parameter_av_av_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="userDataParameterUsages_UserData", type=UserData, multiplicity=Multiplicity(0, 1))
    }
)
hardwareInducedFailureType__ProcessingResourceType291: BinaryAssociation = BinaryAssociation(
    name="hardwareInducedFailureType__ProcessingResourceType291",
    ends={
        Property(name="HardwareInducedFailureType", type=pcm_av_av_resourcetype_av_av_ProcessingResourceType, multiplicity=Multiplicity(1, 1)),
        Property(name="processingResourceType__HardwareInducedFailureType", type=HardwareInducedFailureType, multiplicity=Multiplicity(0, 1))
    }
)
synchronisationPoint_VariableUsage309: BinaryAssociation = BinaryAssociation(
    name="synchronisationPoint_VariableUsage309",
    ends={
        Property(name="SynchronisationPoint", type=pcm_av_av_parameter_av_av_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="outputParameterUsage_SynchronisationPoint", type=SynchronisationPoint, multiplicity=Multiplicity(0, 1))
    }
)
callReturnAction__VariableUsage310: BinaryAssociation = BinaryAssociation(
    name="callReturnAction__VariableUsage310",
    ends={
        Property(name="CallReturnAction", type=pcm_av_av_parameter_av_av_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="returnVariableUsage__CallReturnAction", type=CallReturnAction, multiplicity=Multiplicity(0, 1))
    }
)
setVariableAction_VariableUsage311: BinaryAssociation = BinaryAssociation(
    name="setVariableAction_VariableUsage311",
    ends={
        Property(name="SetVariableAction", type=pcm_av_av_parameter_av_av_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="localVariableUsages_SetVariableAction", type=SetVariableAction, multiplicity=Multiplicity(0, 1))
    }
)
specifiedOutputParameterAbstraction_expectedExternalOutputs_VariableUsage312: BinaryAssociation = BinaryAssociation(
    name="specifiedOutputParameterAbstraction_expectedExternalOutputs_VariableUsage312",
    ends={
        Property(name="SpecifiedOutputParameterAbstraction", type=pcm_av_av_parameter_av_av_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="expectedExternalOutputs_SpecifiedOutputParameterAbstraction", type=SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext__VariableUsage313: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__VariableUsage313",
    ends={
        Property(name="AssemblyContext314", type=pcm_av_av_parameter_av_av_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="configParameterUsages__AssemblyContext", type=composition_av_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
entryLevelSystemCall_InputParameterUsage315: BinaryAssociation = BinaryAssociation(
    name="entryLevelSystemCall_InputParameterUsage315",
    ends={
        Property(name="EntryLevelSystemCall", type=pcm_av_av_parameter_av_av_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="inputParameterUsages_EntryLevelSystemCall", type=EntryLevelSystemCall, multiplicity=Multiplicity(0, 1))
    }
)
entryLevelSystemCall_OutputParameterUsage316: BinaryAssociation = BinaryAssociation(
    name="entryLevelSystemCall_OutputParameterUsage316",
    ends={
        Property(name="EntryLevelSystemCall317", type=pcm_av_av_parameter_av_av_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="outputParameterUsages_EntryLevelSystemCall", type=EntryLevelSystemCall, multiplicity=Multiplicity(0, 1))
    }
)
namedReference__VariableUsage318: BinaryAssociation = BinaryAssociation(
    name="namedReference__VariableUsage318",
    ends={
        Property(name="parameter_av_av_pcm_av_av_AbstractNamedReference", type=pcm_av_av_parameter_av_av_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_parameter_av_av_VariableUsage", type=parameter_av_av_pcm_av_av_AbstractNamedReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
specification_VariableCharacterisation319: BinaryAssociation = BinaryAssociation(
    name="specification_VariableCharacterisation319",
    ends={
        Property(name="PCMRandomVariable320", type=pcm_av_av_parameter_av_av_VariableCharacterisation, multiplicity=Multiplicity(1, 1)),
        Property(name="variableCharacterisation_Specification", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variableUsage_VariableCharacterisation321: BinaryAssociation = BinaryAssociation(
    name="variableUsage_VariableCharacterisation321",
    ends={
        Property(name="VariableUsage322", type=pcm_av_av_parameter_av_av_VariableCharacterisation, multiplicity=Multiplicity(1, 1)),
        Property(name="variableCharacterisation_VariableUsage", type=VariableUsage, multiplicity=Multiplicity(0, 1))
    }
)
callAction__VariableUsage308: BinaryAssociation = BinaryAssociation(
    name="callAction__VariableUsage308",
    ends={
        Property(name="CallAction", type=pcm_av_av_parameter_av_av_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="inputVariableUsages__CallAction", type=CallAction, multiplicity=Multiplicity(0, 1))
    }
)
processingResourceType__HardwareInducedFailureType323: BinaryAssociation = BinaryAssociation(
    name="processingResourceType__HardwareInducedFailureType323",
    ends={
        Property(name="ProcessingResourceType", type=pcm_av_av_reliability_av_av_HardwareInducedFailureType, multiplicity=Multiplicity(1, 1)),
        Property(name="hardwareInducedFailureType__ProcessingResourceType", type=ProcessingResourceType, multiplicity=Multiplicity(0, 1))
    }
)
internalFailureOccurrenceDescriptions__SoftwareInducedFailureType324: BinaryAssociation = BinaryAssociation(
    name="internalFailureOccurrenceDescriptions__SoftwareInducedFailureType324",
    ends={
        Property(name="InternalFailureOccurrenceDescription", type=pcm_av_av_reliability_av_av_SoftwareInducedFailureType, multiplicity=Multiplicity(1, 1)),
        Property(name="softwareInducedFailureType__InternalFailureOccurrenceDescription", type=InternalFailureOccurrenceDescription, multiplicity=Multiplicity(0, 9999))
    }
)
internalAction__InternalFailureOccurrenceDescription325: BinaryAssociation = BinaryAssociation(
    name="internalAction__InternalFailureOccurrenceDescription325",
    ends={
        Property(name="InternalAction", type=pcm_av_av_reliability_av_av_InternalFailureOccurrenceDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="internalFailureOccurrenceDescriptions__InternalAction", type=InternalAction, multiplicity=Multiplicity(0, 1))
    }
)
softwareInducedFailureType__InternalFailureOccurrenceDescription326: BinaryAssociation = BinaryAssociation(
    name="softwareInducedFailureType__InternalFailureOccurrenceDescription326",
    ends={
        Property(name="SoftwareInducedFailureType", type=pcm_av_av_reliability_av_av_InternalFailureOccurrenceDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="internalFailureOccurrenceDescriptions__SoftwareInducedFailureType", type=SoftwareInducedFailureType, multiplicity=Multiplicity(0, 1))
    }
)
communicationLinkResourceType__NetworkInducedFailureType327: BinaryAssociation = BinaryAssociation(
    name="communicationLinkResourceType__NetworkInducedFailureType327",
    ends={
        Property(name="CommunicationLinkResourceType", type=pcm_av_av_reliability_av_av_NetworkInducedFailureType, multiplicity=Multiplicity(1, 1)),
        Property(name="networkInducedFailureType__CommunicationLinkResourceType", type=CommunicationLinkResourceType, multiplicity=Multiplicity(0, 1))
    }
)
specifiedReliabilityAnnotation__ExternalFailureOccurrenceDescription328: BinaryAssociation = BinaryAssociation(
    name="specifiedReliabilityAnnotation__ExternalFailureOccurrenceDescription328",
    ends={
        Property(name="SpecifiedReliabilityAnnotation", type=pcm_av_av_reliability_av_av_ExternalFailureOccurrenceDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="externalFailureOccurrenceDescriptions__SpecifiedReliabilityAnnotation", type=qos_reliability_av_av_SpecifiedReliabilityAnnotation, multiplicity=Multiplicity(0, 1))
    }
)
failureType__ExternalFailureOccurrenceDescription329: BinaryAssociation = BinaryAssociation(
    name="failureType__ExternalFailureOccurrenceDescription329",
    ends={
        Property(name="FailureType330", type=pcm_av_av_reliability_av_av_ExternalFailureOccurrenceDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_reliability_av_av_ExternalFailureOccurrenceDescription", type=FailureType, multiplicity=Multiplicity(0, 1))
    }
)
passiveResource__ResourceTimeoutFailureType331: BinaryAssociation = BinaryAssociation(
    name="passiveResource__ResourceTimeoutFailureType331",
    ends={
        Property(name="PassiveResource332", type=pcm_av_av_reliability_av_av_ResourceTimeoutFailureType, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceTimeoutFailureType__PassiveResource", type=PassiveResource, multiplicity=Multiplicity(0, 1))
    }
)
repository__FailureType333: BinaryAssociation = BinaryAssociation(
    name="repository__FailureType333",
    ends={
        Property(name="Repository334", type=pcm_av_av_reliability_av_av_FailureType, multiplicity=Multiplicity(1, 1)),
        Property(name="failureTypes__Repository", type=Repository, multiplicity=Multiplicity(0, 1))
    }
)
resourceDemand_Action335: BinaryAssociation = BinaryAssociation(
    name="resourceDemand_Action335",
    ends={
        Property(name="ParametricResourceDemand336", type=pcm_av_av_seff_av_av_AbstractInternalControlFlowAction, multiplicity=Multiplicity(1, 1)),
        Property(name="action_ParametricResourceDemand", type=seff_performance_av_av_ParametricResourceDemand, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
infrastructureCall__Action337: BinaryAssociation = BinaryAssociation(
    name="infrastructureCall__Action337",
    ends={
        Property(name="InfrastructureCall338", type=pcm_av_av_seff_av_av_AbstractInternalControlFlowAction, multiplicity=Multiplicity(1, 1)),
        Property(name="action__InfrastructureCall", type=seff_performance_av_av_InfrastructureCall, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceCall__Action339: BinaryAssociation = BinaryAssociation(
    name="resourceCall__Action339",
    ends={
        Property(name="ResourceCall340", type=pcm_av_av_seff_av_av_AbstractInternalControlFlowAction, multiplicity=Multiplicity(1, 1)),
        Property(name="action__ResourceCall", type=seff_performance_av_av_ResourceCall, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
predecessor_AbstractAction341: BinaryAssociation = BinaryAssociation(
    name="predecessor_AbstractAction341",
    ends={
        Property(name="AbstractAction", type=pcm_av_av_seff_av_av_AbstractAction, multiplicity=Multiplicity(1, 1)),
        Property(name="successor_AbstractAction", type=AbstractAction, multiplicity=Multiplicity(0, 1))
    }
)
successor_AbstractAction342: BinaryAssociation = BinaryAssociation(
    name="successor_AbstractAction342",
    ends={
        Property(name="AbstractAction343", type=pcm_av_av_seff_av_av_AbstractAction, multiplicity=Multiplicity(1, 1)),
        Property(name="predecessor_AbstractAction", type=AbstractAction, multiplicity=Multiplicity(0, 1))
    }
)
resourceDemandingBehaviour_AbstractAction344: BinaryAssociation = BinaryAssociation(
    name="resourceDemandingBehaviour_AbstractAction344",
    ends={
        Property(name="ResourceDemandingBehaviour", type=pcm_av_av_seff_av_av_AbstractAction, multiplicity=Multiplicity(1, 1)),
        Property(name="steps_Behaviour", type=ResourceDemandingBehaviour, multiplicity=Multiplicity(0, 1))
    }
)
abstractLoopAction_ResourceDemandingBehaviour345: BinaryAssociation = BinaryAssociation(
    name="abstractLoopAction_ResourceDemandingBehaviour345",
    ends={
        Property(name="AbstractLoopAction", type=pcm_av_av_seff_av_av_ResourceDemandingBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="bodyBehaviour_Loop346", type=AbstractLoopAction, multiplicity=Multiplicity(0, 1))
    }
)
abstractBranchTransition_ResourceDemandingBehaviour347: BinaryAssociation = BinaryAssociation(
    name="abstractBranchTransition_ResourceDemandingBehaviour347",
    ends={
        Property(name="AbstractBranchTransition", type=pcm_av_av_seff_av_av_ResourceDemandingBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="branchBehaviour_BranchTransition", type=AbstractBranchTransition, multiplicity=Multiplicity(0, 1))
    }
)
steps_Behaviour348: BinaryAssociation = BinaryAssociation(
    name="steps_Behaviour348",
    ends={
        Property(name="AbstractAction349", type=pcm_av_av_seff_av_av_ResourceDemandingBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceDemandingBehaviour_AbstractAction", type=AbstractAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bodyBehaviour_Loop350: BinaryAssociation = BinaryAssociation(
    name="bodyBehaviour_Loop350",
    ends={
        Property(name="ResourceDemandingBehaviour351", type=pcm_av_av_seff_av_av_AbstractLoopAction, multiplicity=Multiplicity(1, 1)),
        Property(name="abstractLoopAction_ResourceDemandingBehaviour", type=ResourceDemandingBehaviour, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
branchAction_AbstractBranchTransition352: BinaryAssociation = BinaryAssociation(
    name="branchAction_AbstractBranchTransition352",
    ends={
        Property(name="BranchAction", type=pcm_av_av_seff_av_av_AbstractBranchTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="branches_Branch", type=BranchAction, multiplicity=Multiplicity(0, 1))
    }
)
branchBehaviour_BranchTransition353: BinaryAssociation = BinaryAssociation(
    name="branchBehaviour_BranchTransition353",
    ends={
        Property(name="ResourceDemandingBehaviour354", type=pcm_av_av_seff_av_av_AbstractBranchTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="abstractBranchTransition_ResourceDemandingBehaviour", type=ResourceDemandingBehaviour, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
branches_Branch355: BinaryAssociation = BinaryAssociation(
    name="branches_Branch355",
    ends={
        Property(name="AbstractBranchTransition356", type=pcm_av_av_seff_av_av_BranchAction, multiplicity=Multiplicity(1, 1)),
        Property(name="branchAction_AbstractBranchTransition", type=AbstractBranchTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputVariableUsages__CallAction357: BinaryAssociation = BinaryAssociation(
    name="inputVariableUsages__CallAction357",
    ends={
        Property(name="VariableUsage358", type=pcm_av_av_seff_av_av_CallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="callAction__VariableUsage", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
describedService__SEFF359: BinaryAssociation = BinaryAssociation(
    name="describedService__SEFF359",
    ends={
        Property(name="Signature", type=pcm_av_av_seff_av_av_ServiceEffectSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_seff_av_av_ServiceEffectSpecification", type=Signature, multiplicity=Multiplicity(0, 1))
    }
)
basicComponent_ServiceEffectSpecification360: BinaryAssociation = BinaryAssociation(
    name="basicComponent_ServiceEffectSpecification360",
    ends={
        Property(name="BasicComponent361", type=pcm_av_av_seff_av_av_ServiceEffectSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="serviceEffectSpecifications__BasicComponent", type=BasicComponent, multiplicity=Multiplicity(0, 1))
    }
)
resourceDemandingInternalBehaviours362: BinaryAssociation = BinaryAssociation(
    name="resourceDemandingInternalBehaviours362",
    ends={
        Property(name="ResourceDemandingInternalBehaviour", type=pcm_av_av_seff_av_av_ResourceDemandingSEFF, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceDemandingSEFF_ResourceDemandingInternalBehaviour", type=ResourceDemandingInternalBehaviour, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceDemandingSEFF_ResourceDemandingInternalBehaviour363: BinaryAssociation = BinaryAssociation(
    name="resourceDemandingSEFF_ResourceDemandingInternalBehaviour363",
    ends={
        Property(name="ResourceDemandingSEFF", type=pcm_av_av_seff_av_av_ResourceDemandingInternalBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceDemandingInternalBehaviours", type=ResourceDemandingSEFF, multiplicity=Multiplicity(0, 1))
    }
)
passiveResource_ReleaseAction364: BinaryAssociation = BinaryAssociation(
    name="passiveResource_ReleaseAction364",
    ends={
        Property(name="PassiveResource365", type=pcm_av_av_seff_av_av_ReleaseAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_seff_av_av_ReleaseAction", type=PassiveResource, multiplicity=Multiplicity(0, 1))
    }
)
iterationCount_LoopAction366: BinaryAssociation = BinaryAssociation(
    name="iterationCount_LoopAction366",
    ends={
        Property(name="PCMRandomVariable367", type=pcm_av_av_seff_av_av_LoopAction, multiplicity=Multiplicity(1, 1)),
        Property(name="loopAction_PCMRandomVariable", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
asynchronousForkedBehaviours_ForkAction368: BinaryAssociation = BinaryAssociation(
    name="asynchronousForkedBehaviours_ForkAction368",
    ends={
        Property(name="ForkedBehaviour", type=pcm_av_av_seff_av_av_ForkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="forkAction_ForkedBehaivour", type=ForkedBehaviour, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
synchronisingBehaviours_ForkAction369: BinaryAssociation = BinaryAssociation(
    name="synchronisingBehaviours_ForkAction369",
    ends={
        Property(name="SynchronisationPoint370", type=pcm_av_av_seff_av_av_ForkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="forkAction_SynchronisationPoint", type=SynchronisationPoint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
synchronisationPoint_ForkedBehaviour371: BinaryAssociation = BinaryAssociation(
    name="synchronisationPoint_ForkedBehaviour371",
    ends={
        Property(name="SynchronisationPoint372", type=pcm_av_av_seff_av_av_ForkedBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="synchronousForkedBehaviours_SynchronisationPoint", type=SynchronisationPoint, multiplicity=Multiplicity(0, 1))
    }
)
forkAction_ForkedBehaivour373: BinaryAssociation = BinaryAssociation(
    name="forkAction_ForkedBehaivour373",
    ends={
        Property(name="ForkAction", type=pcm_av_av_seff_av_av_ForkedBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="asynchronousForkedBehaviours_ForkAction", type=ForkAction, multiplicity=Multiplicity(0, 1))
    }
)
outputParameterUsage_SynchronisationPoint374: BinaryAssociation = BinaryAssociation(
    name="outputParameterUsage_SynchronisationPoint374",
    ends={
        Property(name="VariableUsage375", type=pcm_av_av_seff_av_av_SynchronisationPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="synchronisationPoint_VariableUsage", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
forkAction_SynchronisationPoint376: BinaryAssociation = BinaryAssociation(
    name="forkAction_SynchronisationPoint376",
    ends={
        Property(name="ForkAction377", type=pcm_av_av_seff_av_av_SynchronisationPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="synchronisingBehaviours_ForkAction", type=ForkAction, multiplicity=Multiplicity(0, 1))
    }
)
synchronousForkedBehaviours_SynchronisationPoint378: BinaryAssociation = BinaryAssociation(
    name="synchronousForkedBehaviours_SynchronisationPoint378",
    ends={
        Property(name="ForkedBehaviour379", type=pcm_av_av_seff_av_av_SynchronisationPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="synchronisationPoint_ForkedBehaviour", type=ForkedBehaviour, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
calledService_ExternalService380: BinaryAssociation = BinaryAssociation(
    name="calledService_ExternalService380",
    ends={
        Property(name="OperationSignature381", type=pcm_av_av_seff_av_av_ExternalCallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_seff_av_av_ExternalCallAction", type=OperationSignature, multiplicity=Multiplicity(0, 1))
    }
)
role_ExternalService382: BinaryAssociation = BinaryAssociation(
    name="role_ExternalService382",
    ends={
        Property(name="OperationRequiredRole384", type=pcm_av_av_seff_av_av_ExternalCallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_seff_av_av_ExternalCallAction383", type=OperationRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
returnVariableUsage__CallReturnAction385: BinaryAssociation = BinaryAssociation(
    name="returnVariableUsage__CallReturnAction385",
    ends={
        Property(name="VariableUsage386", type=pcm_av_av_seff_av_av_CallReturnAction, multiplicity=Multiplicity(1, 1)),
        Property(name="callReturnAction__VariableUsage", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
passiveresource_AcquireAction387: BinaryAssociation = BinaryAssociation(
    name="passiveresource_AcquireAction387",
    ends={
        Property(name="PassiveResource388", type=pcm_av_av_seff_av_av_AcquireAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_seff_av_av_AcquireAction", type=PassiveResource, multiplicity=Multiplicity(0, 1))
    }
)
parameter_CollectionIteratorAction389: BinaryAssociation = BinaryAssociation(
    name="parameter_CollectionIteratorAction389",
    ends={
        Property(name="Parameter390", type=pcm_av_av_seff_av_av_CollectionIteratorAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_seff_av_av_CollectionIteratorAction", type=Parameter_, multiplicity=Multiplicity(0, 1))
    }
)
branchCondition_GuardedBranchTransition391: BinaryAssociation = BinaryAssociation(
    name="branchCondition_GuardedBranchTransition391",
    ends={
        Property(name="PCMRandomVariable392", type=pcm_av_av_seff_av_av_GuardedBranchTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="guardedBranchTransition_PCMRandomVariable", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
localVariableUsages_SetVariableAction393: BinaryAssociation = BinaryAssociation(
    name="localVariableUsages_SetVariableAction393",
    ends={
        Property(name="VariableUsage394", type=pcm_av_av_seff_av_av_SetVariableAction, multiplicity=Multiplicity(1, 1)),
        Property(name="setVariableAction_VariableUsage", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
calledResourceDemandingInternalBehaviour395: BinaryAssociation = BinaryAssociation(
    name="calledResourceDemandingInternalBehaviour395",
    ends={
        Property(name="ResourceDemandingInternalBehaviour396", type=pcm_av_av_seff_av_av_InternalCallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_seff_av_av_InternalCallAction", type=ResourceDemandingInternalBehaviour, multiplicity=Multiplicity(0, 1))
    }
)
eventType__EmitEventAction397: BinaryAssociation = BinaryAssociation(
    name="eventType__EmitEventAction397",
    ends={
        Property(name="EventType398", type=pcm_av_av_seff_av_av_EmitEventAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_seff_av_av_EmitEventAction", type=EventType, multiplicity=Multiplicity(0, 1))
    }
)
sourceRole__EmitEventAction399: BinaryAssociation = BinaryAssociation(
    name="sourceRole__EmitEventAction399",
    ends={
        Property(name="SourceRole401", type=pcm_av_av_seff_av_av_EmitEventAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_seff_av_av_EmitEventAction400", type=SourceRole, multiplicity=Multiplicity(0, 1))
    }
)
internalFailureOccurrenceDescriptions__InternalAction402: BinaryAssociation = BinaryAssociation(
    name="internalFailureOccurrenceDescriptions__InternalAction402",
    ends={
        Property(name="InternalFailureOccurrenceDescription403", type=pcm_av_av_seff_av_av_InternalAction, multiplicity=Multiplicity(1, 1)),
        Property(name="internalAction__InternalFailureOccurrenceDescription", type=InternalFailureOccurrenceDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
signature__InfrastructureCall404: BinaryAssociation = BinaryAssociation(
    name="signature__InfrastructureCall404",
    ends={
        Property(name="InfrastructureSignature405", type=pcm_av_av_seff_performance_av_av_InfrastructureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_seff_performance_av_av_InfrastructureCall", type=InfrastructureSignature, multiplicity=Multiplicity(0, 1))
    }
)
numberOfCalls__InfrastructureCall406: BinaryAssociation = BinaryAssociation(
    name="numberOfCalls__InfrastructureCall406",
    ends={
        Property(name="PCMRandomVariable407", type=pcm_av_av_seff_performance_av_av_InfrastructureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="infrastructureCall__PCMRandomVariable", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
action__InfrastructureCall408: BinaryAssociation = BinaryAssociation(
    name="action__InfrastructureCall408",
    ends={
        Property(name="AbstractInternalControlFlowAction", type=pcm_av_av_seff_performance_av_av_InfrastructureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="infrastructureCall__Action", type=AbstractInternalControlFlowAction, multiplicity=Multiplicity(0, 1))
    }
)
requiredRole__InfrastructureCall409: BinaryAssociation = BinaryAssociation(
    name="requiredRole__InfrastructureCall409",
    ends={
        Property(name="InfrastructureRequiredRole411", type=pcm_av_av_seff_performance_av_av_InfrastructureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_seff_performance_av_av_InfrastructureCall410", type=InfrastructureRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
resourceRequiredRole__ResourceCall414: BinaryAssociation = BinaryAssociation(
    name="resourceRequiredRole__ResourceCall414",
    ends={
        Property(name="entity_av_av_ResourceRequiredRole415", type=pcm_av_av_seff_performance_av_av_ResourceCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_seff_performance_av_av_ResourceCall", type=entity_av_av_ResourceRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
signature__ResourceCall416: BinaryAssociation = BinaryAssociation(
    name="signature__ResourceCall416",
    ends={
        Property(name="ResourceSignature418", type=pcm_av_av_seff_performance_av_av_ResourceCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_seff_performance_av_av_ResourceCall417", type=ResourceSignature, multiplicity=Multiplicity(0, 1))
    }
)
numberOfCalls__ResourceCall419: BinaryAssociation = BinaryAssociation(
    name="numberOfCalls__ResourceCall419",
    ends={
        Property(name="PCMRandomVariable420", type=pcm_av_av_seff_performance_av_av_ResourceCall, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceCall__PCMRandomVariable", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
specification_ParametericResourceDemand421: BinaryAssociation = BinaryAssociation(
    name="specification_ParametericResourceDemand421",
    ends={
        Property(name="PCMRandomVariable422", type=pcm_av_av_seff_performance_av_av_ParametricResourceDemand, multiplicity=Multiplicity(1, 1)),
        Property(name="parametricResourceDemand_PCMRandomVariable", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
requiredResource_ParametricResourceDemand423: BinaryAssociation = BinaryAssociation(
    name="requiredResource_ParametricResourceDemand423",
    ends={
        Property(name="ProcessingResourceType424", type=pcm_av_av_seff_performance_av_av_ParametricResourceDemand, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_seff_performance_av_av_ParametricResourceDemand", type=ProcessingResourceType, multiplicity=Multiplicity(0, 1))
    }
)
action_ParametricResourceDemand425: BinaryAssociation = BinaryAssociation(
    name="action_ParametricResourceDemand425",
    ends={
        Property(name="AbstractInternalControlFlowAction426", type=pcm_av_av_seff_performance_av_av_ParametricResourceDemand, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceDemand_Action", type=AbstractInternalControlFlowAction, multiplicity=Multiplicity(0, 1))
    }
)
action__ResourceCall412: BinaryAssociation = BinaryAssociation(
    name="action__ResourceCall412",
    ends={
        Property(name="AbstractInternalControlFlowAction413", type=pcm_av_av_seff_performance_av_av_ResourceCall, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceCall__Action", type=AbstractInternalControlFlowAction, multiplicity=Multiplicity(0, 1))
    }
)
failureHandlingAlternatives__RecoveryActionBehaviour427: BinaryAssociation = BinaryAssociation(
    name="failureHandlingAlternatives__RecoveryActionBehaviour427",
    ends={
        Property(name="seff_reliability_av_av_RecoveryActionBehaviour", type=pcm_av_av_seff_reliability_av_av_RecoveryActionBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_seff_reliability_av_av_RecoveryActionBehaviour", type=seff_reliability_av_av_RecoveryActionBehaviour, multiplicity=Multiplicity(0, 9999))
    }
)
recoveryAction__RecoveryActionBehaviour428: BinaryAssociation = BinaryAssociation(
    name="recoveryAction__RecoveryActionBehaviour428",
    ends={
        Property(name="RecoveryAction", type=pcm_av_av_seff_reliability_av_av_RecoveryActionBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="recoveryActionBehaviours__RecoveryAction", type=seff_reliability_av_av_RecoveryAction, multiplicity=Multiplicity(0, 1))
    }
)
primaryBehaviour__RecoveryAction429: BinaryAssociation = BinaryAssociation(
    name="primaryBehaviour__RecoveryAction429",
    ends={
        Property(name="seff_reliability_av_av_RecoveryActionBehaviour430", type=pcm_av_av_seff_reliability_av_av_RecoveryAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_seff_reliability_av_av_RecoveryAction", type=seff_reliability_av_av_RecoveryActionBehaviour, multiplicity=Multiplicity(0, 1))
    }
)
recoveryActionBehaviours__RecoveryAction431: BinaryAssociation = BinaryAssociation(
    name="recoveryActionBehaviours__RecoveryAction431",
    ends={
        Property(name="RecoveryActionBehaviour", type=pcm_av_av_seff_reliability_av_av_RecoveryAction, multiplicity=Multiplicity(1, 1)),
        Property(name="recoveryAction__RecoveryActionBehaviour", type=seff_reliability_av_av_RecoveryActionBehaviour, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
failureTypes_FailureHandlingEntity432: BinaryAssociation = BinaryAssociation(
    name="failureTypes_FailureHandlingEntity432",
    ends={
        Property(name="FailureType433", type=pcm_av_av_seff_reliability_av_av_FailureHandlingEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_seff_reliability_av_av_FailureHandlingEntity", type=FailureType, multiplicity=Multiplicity(0, 9999))
    }
)
signature_SpecifiedQoSAnnation434: BinaryAssociation = BinaryAssociation(
    name="signature_SpecifiedQoSAnnation434",
    ends={
        Property(name="Signature435", type=pcm_av_av_qosannotations_av_av_SpecifiedQoSAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_qosannotations_av_av_SpecifiedQoSAnnotation", type=Signature, multiplicity=Multiplicity(0, 1))
    }
)
role_SpecifiedQoSAnnotation436: BinaryAssociation = BinaryAssociation(
    name="role_SpecifiedQoSAnnotation436",
    ends={
        Property(name="Role", type=pcm_av_av_qosannotations_av_av_SpecifiedQoSAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_qosannotations_av_av_SpecifiedQoSAnnotation437", type=Role, multiplicity=Multiplicity(0, 1))
    }
)
qosAnnotations_SpecifiedQoSAnnotation438: BinaryAssociation = BinaryAssociation(
    name="qosAnnotations_SpecifiedQoSAnnotation438",
    ends={
        Property(name="QoSAnnotations", type=pcm_av_av_qosannotations_av_av_SpecifiedQoSAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="specifiedQoSAnnotations_QoSAnnotations", type=QoSAnnotations, multiplicity=Multiplicity(0, 1))
    }
)
specifiedOutputParameterAbstractions_QoSAnnotations439: BinaryAssociation = BinaryAssociation(
    name="specifiedOutputParameterAbstractions_QoSAnnotations439",
    ends={
        Property(name="SpecifiedOutputParameterAbstraction440", type=pcm_av_av_qosannotations_av_av_QoSAnnotations, multiplicity=Multiplicity(1, 1)),
        Property(name="qosAnnotations_SpecifiedOutputParameterAbstraction", type=SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
system_QoSAnnotations441: BinaryAssociation = BinaryAssociation(
    name="system_QoSAnnotations441",
    ends={
        Property(name="System", type=pcm_av_av_qosannotations_av_av_QoSAnnotations, multiplicity=Multiplicity(1, 1)),
        Property(name="qosAnnotations_System", type=System, multiplicity=Multiplicity(0, 1))
    }
)
specifiedQoSAnnotations_QoSAnnotations442: BinaryAssociation = BinaryAssociation(
    name="specifiedQoSAnnotations_QoSAnnotations442",
    ends={
        Property(name="SpecifiedQoSAnnotation", type=pcm_av_av_qosannotations_av_av_QoSAnnotations, multiplicity=Multiplicity(1, 1)),
        Property(name="qosAnnotations_SpecifiedQoSAnnotation", type=SpecifiedQoSAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
signature_SpecifiedOutputParameterAbstraction443: BinaryAssociation = BinaryAssociation(
    name="signature_SpecifiedOutputParameterAbstraction443",
    ends={
        Property(name="Signature444", type=pcm_av_av_qosannotations_av_av_SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_qosannotations_av_av_SpecifiedOutputParameterAbstraction", type=Signature, multiplicity=Multiplicity(0, 1))
    }
)
role_SpecifiedOutputParameterAbstraction445: BinaryAssociation = BinaryAssociation(
    name="role_SpecifiedOutputParameterAbstraction445",
    ends={
        Property(name="Role447", type=pcm_av_av_qosannotations_av_av_SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_qosannotations_av_av_SpecifiedOutputParameterAbstraction446", type=Role, multiplicity=Multiplicity(0, 1))
    }
)
expectedExternalOutputs_SpecifiedOutputParameterAbstraction448: BinaryAssociation = BinaryAssociation(
    name="expectedExternalOutputs_SpecifiedOutputParameterAbstraction448",
    ends={
        Property(name="VariableUsage449", type=pcm_av_av_qosannotations_av_av_SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(1, 1)),
        Property(name="specifiedOutputParameterAbstraction_expectedExternalOutputs_VariableUsage", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
qosAnnotations_SpecifiedOutputParameterAbstraction450: BinaryAssociation = BinaryAssociation(
    name="qosAnnotations_SpecifiedOutputParameterAbstraction450",
    ends={
        Property(name="QoSAnnotations451", type=pcm_av_av_qosannotations_av_av_SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(1, 1)),
        Property(name="specifiedOutputParameterAbstractions_QoSAnnotations", type=QoSAnnotations, multiplicity=Multiplicity(0, 1))
    }
)
specification_SpecifiedExecutionTime452: BinaryAssociation = BinaryAssociation(
    name="specification_SpecifiedExecutionTime452",
    ends={
        Property(name="PCMRandomVariable453", type=pcm_av_av_qos_performance_av_av_SpecifiedExecutionTime, multiplicity=Multiplicity(1, 1)),
        Property(name="specifiedExecutionTime_PCMRandomVariable", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assemblyContext_ComponentSpecifiedExecutionTime454: BinaryAssociation = BinaryAssociation(
    name="assemblyContext_ComponentSpecifiedExecutionTime454",
    ends={
        Property(name="pcm_av_av_qos_performance_av_av_ComponentSpecifiedExecutionTime", type=composition_av_av_AssemblyContext, multiplicity=Multiplicity(0, 1)),
        Property(name="composition_av_av_AssemblyContext455", type=pcm_av_av_qos_performance_av_av_ComponentSpecifiedExecutionTime, multiplicity=Multiplicity(1, 1))
    }
)
externalFailureOccurrenceDescriptions__SpecifiedReliabilityAnnotation456: BinaryAssociation = BinaryAssociation(
    name="externalFailureOccurrenceDescriptions__SpecifiedReliabilityAnnotation456",
    ends={
        Property(name="ExternalFailureOccurrenceDescription", type=pcm_av_av_qos_reliability_av_av_SpecifiedReliabilityAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="specifiedReliabilityAnnotation__ExternalFailureOccurrenceDescription", type=ExternalFailureOccurrenceDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
linkingResources__ResourceEnvironment459: BinaryAssociation = BinaryAssociation(
    name="linkingResources__ResourceEnvironment459",
    ends={
        Property(name="LinkingResource", type=pcm_av_av_resourceenvironment_av_av_ResourceEnvironment, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceEnvironment_LinkingResource", type=LinkingResource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceContainer_ResourceEnvironment460: BinaryAssociation = BinaryAssociation(
    name="resourceContainer_ResourceEnvironment460",
    ends={
        Property(name="ResourceContainer", type=pcm_av_av_resourceenvironment_av_av_ResourceEnvironment, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceEnvironment_ResourceContainer", type=ResourceContainer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connectedResourceContainers_LinkingResource461: BinaryAssociation = BinaryAssociation(
    name="connectedResourceContainers_LinkingResource461",
    ends={
        Property(name="ResourceContainer462", type=pcm_av_av_resourceenvironment_av_av_LinkingResource, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_resourceenvironment_av_av_LinkingResource", type=ResourceContainer, multiplicity=Multiplicity(0, 9999))
    }
)
communicationLinkResourceSpecifications_LinkingResource463: BinaryAssociation = BinaryAssociation(
    name="communicationLinkResourceSpecifications_LinkingResource463",
    ends={
        Property(name="CommunicationLinkResourceSpecification464", type=pcm_av_av_resourceenvironment_av_av_LinkingResource, multiplicity=Multiplicity(1, 1)),
        Property(name="linkingResource_CommunicationLinkResourceSpecification", type=CommunicationLinkResourceSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resourceEnvironment_LinkingResource465: BinaryAssociation = BinaryAssociation(
    name="resourceEnvironment_LinkingResource465",
    ends={
        Property(name="ResourceEnvironment", type=pcm_av_av_resourceenvironment_av_av_LinkingResource, multiplicity=Multiplicity(1, 1)),
        Property(name="linkingResources__ResourceEnvironment", type=ResourceEnvironment, multiplicity=Multiplicity(0, 1))
    }
)
activeResourceSpecifications_ResourceContainer466: BinaryAssociation = BinaryAssociation(
    name="activeResourceSpecifications_ResourceContainer466",
    ends={
        Property(name="ProcessingResourceSpecification467", type=pcm_av_av_resourceenvironment_av_av_ResourceContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceContainer_ProcessingResourceSpecification", type=ProcessingResourceSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceEnvironment_ResourceContainer468: BinaryAssociation = BinaryAssociation(
    name="resourceEnvironment_ResourceContainer468",
    ends={
        Property(name="ResourceEnvironment469", type=pcm_av_av_resourceenvironment_av_av_ResourceContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceContainer_ResourceEnvironment", type=ResourceEnvironment, multiplicity=Multiplicity(0, 1))
    }
)
nestedResourceContainers__ResourceContainer470: BinaryAssociation = BinaryAssociation(
    name="nestedResourceContainers__ResourceContainer470",
    ends={
        Property(name="ResourceContainer471", type=pcm_av_av_resourceenvironment_av_av_ResourceContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="parentResourceContainer__ResourceContainer", type=ResourceContainer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentResourceContainer__ResourceContainer472: BinaryAssociation = BinaryAssociation(
    name="parentResourceContainer__ResourceContainer472",
    ends={
        Property(name="ResourceContainer473", type=pcm_av_av_resourceenvironment_av_av_ResourceContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="nestedResourceContainers__ResourceContainer", type=ResourceContainer, multiplicity=Multiplicity(0, 1))
    }
)
schedulingPolicy474: BinaryAssociation = BinaryAssociation(
    name="schedulingPolicy474",
    ends={
        Property(name="SchedulingPolicy475", type=pcm_av_av_resourceenvironment_av_av_ProcessingResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_resourceenvironment_av_av_ProcessingResourceSpecification", type=SchedulingPolicy, multiplicity=Multiplicity(0, 1))
    }
)
qosAnnotations_System457: BinaryAssociation = BinaryAssociation(
    name="qosAnnotations_System457",
    ends={
        Property(name="QoSAnnotations458", type=pcm_av_av_system_av_av_System, multiplicity=Multiplicity(1, 1)),
        Property(name="system_QoSAnnotations", type=QoSAnnotations, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
processingRate_ProcessingResourceSpecification479: BinaryAssociation = BinaryAssociation(
    name="processingRate_ProcessingResourceSpecification479",
    ends={
        Property(name="PCMRandomVariable480", type=pcm_av_av_resourceenvironment_av_av_ProcessingResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="processingResourceSpecification_processingRate_PCMRandomVariable", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resourceContainer_ProcessingResourceSpecification481: BinaryAssociation = BinaryAssociation(
    name="resourceContainer_ProcessingResourceSpecification481",
    ends={
        Property(name="ResourceContainer482", type=pcm_av_av_resourceenvironment_av_av_ProcessingResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="activeResourceSpecifications_ResourceContainer", type=ResourceContainer, multiplicity=Multiplicity(0, 1))
    }
)
linkingResource_CommunicationLinkResourceSpecification483: BinaryAssociation = BinaryAssociation(
    name="linkingResource_CommunicationLinkResourceSpecification483",
    ends={
        Property(name="LinkingResource484", type=pcm_av_av_resourceenvironment_av_av_CommunicationLinkResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="communicationLinkResourceSpecifications_LinkingResource", type=LinkingResource, multiplicity=Multiplicity(0, 1))
    }
)
communicationLinkResourceType_CommunicationLinkResourceSpecification485: BinaryAssociation = BinaryAssociation(
    name="communicationLinkResourceType_CommunicationLinkResourceSpecification485",
    ends={
        Property(name="CommunicationLinkResourceType486", type=pcm_av_av_resourceenvironment_av_av_CommunicationLinkResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_resourceenvironment_av_av_CommunicationLinkResourceSpecification", type=CommunicationLinkResourceType, multiplicity=Multiplicity(0, 1))
    }
)
latency_CommunicationLinkResourceSpecification487: BinaryAssociation = BinaryAssociation(
    name="latency_CommunicationLinkResourceSpecification487",
    ends={
        Property(name="PCMRandomVariable488", type=pcm_av_av_resourceenvironment_av_av_CommunicationLinkResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="communicationLinkResourceSpecification_latency_PCMRandomVariable", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
throughput_CommunicationLinkResourceSpecification489: BinaryAssociation = BinaryAssociation(
    name="throughput_CommunicationLinkResourceSpecification489",
    ends={
        Property(name="PCMRandomVariable490", type=pcm_av_av_resourceenvironment_av_av_CommunicationLinkResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="communicationLinkResourceSpecifcation_throughput_PCMRandomVariable", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resourceContainer_AllocationContext491: BinaryAssociation = BinaryAssociation(
    name="resourceContainer_AllocationContext491",
    ends={
        Property(name="ResourceContainer492", type=pcm_av_av_allocation_av_av_AllocationContext, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_allocation_av_av_AllocationContext", type=ResourceContainer, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext_AllocationContext493: BinaryAssociation = BinaryAssociation(
    name="assemblyContext_AllocationContext493",
    ends={
        Property(name="composition_av_av_AssemblyContext495", type=pcm_av_av_allocation_av_av_AllocationContext, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_allocation_av_av_AllocationContext494", type=composition_av_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
allocation_AllocationContext496: BinaryAssociation = BinaryAssociation(
    name="allocation_AllocationContext496",
    ends={
        Property(name="Allocation", type=pcm_av_av_allocation_av_av_AllocationContext, multiplicity=Multiplicity(1, 1)),
        Property(name="allocationContexts_Allocation", type=Allocation, multiplicity=Multiplicity(0, 1))
    }
)
activeResourceType_ActiveResourceSpecification476: BinaryAssociation = BinaryAssociation(
    name="activeResourceType_ActiveResourceSpecification476",
    ends={
        Property(name="ProcessingResourceType478", type=pcm_av_av_resourceenvironment_av_av_ProcessingResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_resourceenvironment_av_av_ProcessingResourceSpecification477", type=ProcessingResourceType, multiplicity=Multiplicity(0, 1))
    }
)
targetResourceEnvironment_Allocation499: BinaryAssociation = BinaryAssociation(
    name="targetResourceEnvironment_Allocation499",
    ends={
        Property(name="ResourceEnvironment500", type=pcm_av_av_allocation_av_av_Allocation, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_allocation_av_av_Allocation", type=ResourceEnvironment, multiplicity=Multiplicity(0, 1))
    }
)
system_Allocation501: BinaryAssociation = BinaryAssociation(
    name="system_Allocation501",
    ends={
        Property(name="System503", type=pcm_av_av_allocation_av_av_Allocation, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_allocation_av_av_Allocation502", type=System, multiplicity=Multiplicity(0, 1))
    }
)
allocationContexts_Allocation504: BinaryAssociation = BinaryAssociation(
    name="allocationContexts_Allocation504",
    ends={
        Property(name="AllocationContext", type=pcm_av_av_allocation_av_av_Allocation, multiplicity=Multiplicity(1, 1)),
        Property(name="allocation_AllocationContext", type=AllocationContext, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
completions_CompletionRepository505: BinaryAssociation = BinaryAssociation(
    name="completions_CompletionRepository505",
    ends={
        Property(name="Completion", type=pcm_av_av_completions_av_av_CompletionRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_completions_av_av_CompletionRepository", type=Completion, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredCommunicationLinkResource_ParametricResourceDemand506: BinaryAssociation = BinaryAssociation(
    name="requiredCommunicationLinkResource_ParametricResourceDemand506",
    ends={
        Property(name="CommunicationLinkResourceType507", type=pcm_av_av_completions_av_av_NetworkDemandParametricResourceDemand, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_completions_av_av_NetworkDemandParametricResourceDemand", type=CommunicationLinkResourceType, multiplicity=Multiplicity(0, 1))
    }
)
eventChannel__AllocationContext497: BinaryAssociation = BinaryAssociation(
    name="eventChannel__AllocationContext497",
    ends={
        Property(name="composition_av_av_EventChannel", type=pcm_av_av_allocation_av_av_AllocationContext, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_av_allocation_av_av_AllocationContext498", type=composition_av_av_EventChannel, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_pcm_av_av_core_av_av_PCMRandomVariable_RandomVariable = Generalization(general=RandomVariable, specific=pcm_av_av_core_av_av_PCMRandomVariable)
gen_pcm_av_av_entity_av_av_ResourceProvidedRole_Role = Generalization(general=Role, specific=pcm_av_av_entity_av_av_ResourceProvidedRole)
gen_pcm_av_av_entity_av_av_InterfaceProvidingRequiringEntity_entity_av_av_InterfaceProvidingEntity = Generalization(general=entity_av_av_InterfaceProvidingEntity, specific=pcm_av_av_entity_av_av_InterfaceProvidingRequiringEntity)
gen_pcm_av_av_entity_av_av_InterfaceProvidingRequiringEntity_entity_av_av_InterfaceRequiringEntity = Generalization(general=entity_av_av_InterfaceRequiringEntity, specific=pcm_av_av_entity_av_av_InterfaceProvidingRequiringEntity)
gen_pcm_av_av_entity_av_av_InterfaceProvidingEntity_Entity = Generalization(general=Entity, specific=pcm_av_av_entity_av_av_InterfaceProvidingEntity)
gen_pcm_av_av_entity_av_av_InterfaceRequiringEntity_entity_av_av_Entity = Generalization(general=entity_av_av_Entity, specific=pcm_av_av_entity_av_av_InterfaceRequiringEntity)
gen_pcm_av_av_entity_av_av_InterfaceRequiringEntity_entity_av_av_ResourceInterfaceRequiringEntity = Generalization(general=entity_av_av_ResourceInterfaceRequiringEntity, specific=pcm_av_av_entity_av_av_InterfaceRequiringEntity)
gen_pcm_av_av_entity_av_av_ResourceInterfaceRequiringEntity_Entity = Generalization(general=Entity, specific=pcm_av_av_entity_av_av_ResourceInterfaceRequiringEntity)
gen_pcm_av_av_entity_av_av_ResourceInterfaceProvidingEntity_Entity = Generalization(general=Entity, specific=pcm_av_av_entity_av_av_ResourceInterfaceProvidingEntity)
gen_pcm_av_av_entity_av_av_ComposedProvidingRequiringEntity_composition_av_av_ComposedStructure = Generalization(general=composition_av_av_ComposedStructure, specific=pcm_av_av_entity_av_av_ComposedProvidingRequiringEntity)
gen_pcm_av_av_entity_av_av_ComposedProvidingRequiringEntity_entity_av_av_InterfaceProvidingRequiringEntity = Generalization(general=entity_av_av_InterfaceProvidingRequiringEntity, specific=pcm_av_av_entity_av_av_ComposedProvidingRequiringEntity)
gen_pcm_av_av_entity_av_av_ResourceInterfaceProvidingRequiringEntity_entity_av_av_ResourceInterfaceRequiringEntity = Generalization(general=entity_av_av_ResourceInterfaceRequiringEntity, specific=pcm_av_av_entity_av_av_ResourceInterfaceProvidingRequiringEntity)
gen_pcm_av_av_entity_av_av_ResourceInterfaceProvidingRequiringEntity_entity_av_av_ResourceInterfaceProvidingEntity = Generalization(general=entity_av_av_ResourceInterfaceProvidingEntity, specific=pcm_av_av_entity_av_av_ResourceInterfaceProvidingRequiringEntity)
gen_pcm_av_av_entity_av_av_Entity_Identifier = Generalization(general=Identifier, specific=pcm_av_av_entity_av_av_Entity)
gen_pcm_av_av_entity_av_av_Entity_entity_av_av_NamedElement = Generalization(general=entity_av_av_NamedElement, specific=pcm_av_av_entity_av_av_Entity)
gen_pcm_av_av_composition_av_av_DelegationConnector_Connector = Generalization(general=Connector, specific=pcm_av_av_composition_av_av_DelegationConnector)
gen_pcm_av_av_composition_av_av_Connector_Entity = Generalization(general=Entity, specific=pcm_av_av_composition_av_av_Connector)
gen_pcm_av_av_composition_av_av_ComposedStructure_Entity = Generalization(general=Entity, specific=pcm_av_av_composition_av_av_ComposedStructure)
gen_pcm_av_av_entity_av_av_ResourceRequiredRole_Role = Generalization(general=Role, specific=pcm_av_av_entity_av_av_ResourceRequiredRole)
gen_pcm_av_av_composition_av_av_EventChannel_Entity = Generalization(general=Entity, specific=pcm_av_av_composition_av_av_EventChannel)
gen_pcm_av_av_composition_av_av_EventChannelSourceConnector_Connector = Generalization(general=Connector, specific=pcm_av_av_composition_av_av_EventChannelSourceConnector)
gen_pcm_av_av_composition_av_av_EventChannelSinkConnector_Connector = Generalization(general=Connector, specific=pcm_av_av_composition_av_av_EventChannelSinkConnector)
gen_pcm_av_av_composition_av_av_RequiredDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_av_av_composition_av_av_RequiredDelegationConnector)
gen_pcm_av_av_composition_av_av_ProvidedDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_av_av_composition_av_av_ProvidedDelegationConnector)
gen_pcm_av_av_composition_av_av_AssemblyConnector_Connector = Generalization(general=Connector, specific=pcm_av_av_composition_av_av_AssemblyConnector)
gen_pcm_av_av_composition_av_av_AssemblyEventConnector_Connector = Generalization(general=Connector, specific=pcm_av_av_composition_av_av_AssemblyEventConnector)
gen_pcm_av_av_composition_av_av_SinkDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_av_av_composition_av_av_SinkDelegationConnector)
gen_pcm_av_av_composition_av_av_AssemblyInfrastructureConnector_Connector = Generalization(general=Connector, specific=pcm_av_av_composition_av_av_AssemblyInfrastructureConnector)
gen_pcm_av_av_composition_av_av_ProvidedInfrastructureDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_av_av_composition_av_av_ProvidedInfrastructureDelegationConnector)
gen_pcm_av_av_composition_av_av_RequiredInfrastructureDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_av_av_composition_av_av_RequiredInfrastructureDelegationConnector)
gen_pcm_av_av_composition_av_av_RequiredResourceDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_av_av_composition_av_av_RequiredResourceDelegationConnector)
gen_pcm_av_av_composition_av_av_SourceDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_av_av_composition_av_av_SourceDelegationConnector)
gen_pcm_av_av_composition_av_av_AssemblyContext_Entity = Generalization(general=Entity, specific=pcm_av_av_composition_av_av_AssemblyContext)
gen_pcm_av_av_usagemodel_av_av_UsageScenario_Entity = Generalization(general=Entity, specific=pcm_av_av_usagemodel_av_av_UsageScenario)
gen_pcm_av_av_usagemodel_av_av_EntryLevelSystemCall_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_av_av_usagemodel_av_av_EntryLevelSystemCall)
gen_pcm_av_av_usagemodel_av_av_AbstractUserAction_Entity = Generalization(general=Entity, specific=pcm_av_av_usagemodel_av_av_AbstractUserAction)
gen_pcm_av_av_usagemodel_av_av_ScenarioBehaviour_Entity = Generalization(general=Entity, specific=pcm_av_av_usagemodel_av_av_ScenarioBehaviour)
gen_pcm_av_av_usagemodel_av_av_Branch_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_av_av_usagemodel_av_av_Branch)
gen_pcm_av_av_usagemodel_av_av_Loop_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_av_av_usagemodel_av_av_Loop)
gen_pcm_av_av_usagemodel_av_av_Stop_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_av_av_usagemodel_av_av_Stop)
gen_pcm_av_av_usagemodel_av_av_Start_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_av_av_usagemodel_av_av_Start)
gen_pcm_av_av_usagemodel_av_av_OpenWorkload_Workload = Generalization(general=Workload, specific=pcm_av_av_usagemodel_av_av_OpenWorkload)
gen_pcm_av_av_usagemodel_av_av_Delay_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_av_av_usagemodel_av_av_Delay)
gen_pcm_av_av_usagemodel_av_av_ClosedWorkload_Workload = Generalization(general=Workload, specific=pcm_av_av_usagemodel_av_av_ClosedWorkload)
gen_pcm_av_av_repository_av_av_PassiveResource_Entity = Generalization(general=Entity, specific=pcm_av_av_repository_av_av_PassiveResource)
gen_pcm_av_av_repository_av_av_BasicComponent_ImplementationComponentType = Generalization(general=ImplementationComponentType, specific=pcm_av_av_repository_av_av_BasicComponent)
gen_pcm_av_av_repository_av_av_ImplementationComponentType_RepositoryComponent = Generalization(general=RepositoryComponent, specific=pcm_av_av_repository_av_av_ImplementationComponentType)
gen_pcm_av_av_repository_av_av_RepositoryComponent_InterfaceProvidingRequiringEntity = Generalization(general=InterfaceProvidingRequiringEntity, specific=pcm_av_av_repository_av_av_RepositoryComponent)
gen_pcm_av_av_repository_av_av_ProvidedRole_Role = Generalization(general=Role, specific=pcm_av_av_repository_av_av_ProvidedRole)
gen_pcm_av_av_repository_av_av_Repository_Entity = Generalization(general=Entity, specific=pcm_av_av_repository_av_av_Repository)
gen_pcm_av_av_repository_av_av_Interface_Entity = Generalization(general=Entity, specific=pcm_av_av_repository_av_av_Interface)
gen_pcm_av_av_repository_av_av_EventGroup_Interface = Generalization(general=Interface, specific=pcm_av_av_repository_av_av_EventGroup)
gen_pcm_av_av_repository_av_av_EventType_Signature = Generalization(general=Signature, specific=pcm_av_av_repository_av_av_EventType)
gen_pcm_av_av_repository_av_av_Signature_Entity = Generalization(general=Entity, specific=pcm_av_av_repository_av_av_Signature)
gen_pcm_av_av_repository_av_av_InfrastructureSignature_Signature = Generalization(general=Signature, specific=pcm_av_av_repository_av_av_InfrastructureSignature)
gen_pcm_av_av_repository_av_av_InfrastructureInterface_Interface = Generalization(general=Interface, specific=pcm_av_av_repository_av_av_InfrastructureInterface)
gen_pcm_av_av_repository_av_av_InfrastructureRequiredRole_RequiredRole = Generalization(general=RequiredRole, specific=pcm_av_av_repository_av_av_InfrastructureRequiredRole)
gen_pcm_av_av_repository_av_av_RequiredRole_Role = Generalization(general=Role, specific=pcm_av_av_repository_av_av_RequiredRole)
gen_pcm_av_av_repository_av_av_OperationSignature_Signature = Generalization(general=Signature, specific=pcm_av_av_repository_av_av_OperationSignature)
gen_pcm_av_av_repository_av_av_OperationInterface_Interface = Generalization(general=Interface, specific=pcm_av_av_repository_av_av_OperationInterface)
gen_pcm_av_av_repository_av_av_OperationRequiredRole_RequiredRole = Generalization(general=RequiredRole, specific=pcm_av_av_repository_av_av_OperationRequiredRole)
gen_pcm_av_av_repository_av_av_SourceRole_RequiredRole = Generalization(general=RequiredRole, specific=pcm_av_av_repository_av_av_SourceRole)
gen_pcm_av_av_repository_av_av_SinkRole_ProvidedRole = Generalization(general=ProvidedRole, specific=pcm_av_av_repository_av_av_SinkRole)
gen_pcm_av_av_repository_av_av_OperationProvidedRole_ProvidedRole = Generalization(general=ProvidedRole, specific=pcm_av_av_repository_av_av_OperationProvidedRole)
gen_pcm_av_av_repository_av_av_InfrastructureProvidedRole_ProvidedRole = Generalization(general=ProvidedRole, specific=pcm_av_av_repository_av_av_InfrastructureProvidedRole)
gen_pcm_av_av_repository_av_av_CompleteComponentType_RepositoryComponent = Generalization(general=RepositoryComponent, specific=pcm_av_av_repository_av_av_CompleteComponentType)
gen_pcm_av_av_repository_av_av_ProvidesComponentType_RepositoryComponent = Generalization(general=RepositoryComponent, specific=pcm_av_av_repository_av_av_ProvidesComponentType)
gen_pcm_av_av_repository_av_av_CompositeComponent_entity_av_av_ComposedProvidingRequiringEntity = Generalization(general=entity_av_av_ComposedProvidingRequiringEntity, specific=pcm_av_av_repository_av_av_CompositeComponent)
gen_pcm_av_av_repository_av_av_CompositeComponent_repository_av_av_ImplementationComponentType = Generalization(general=repository_av_av_ImplementationComponentType, specific=pcm_av_av_repository_av_av_CompositeComponent)
gen_pcm_av_av_repository_av_av_PrimitiveDataType_DataType = Generalization(general=DataType, specific=pcm_av_av_repository_av_av_PrimitiveDataType)
gen_pcm_av_av_repository_av_av_CollectionDataType_entity_av_av_Entity = Generalization(general=entity_av_av_Entity, specific=pcm_av_av_repository_av_av_CollectionDataType)
gen_pcm_av_av_repository_av_av_CollectionDataType_repository_av_av_DataType = Generalization(general=repository_av_av_DataType, specific=pcm_av_av_repository_av_av_CollectionDataType)
gen_pcm_av_av_repository_av_av_CompositeDataType_entity_av_av_Entity = Generalization(general=entity_av_av_Entity, specific=pcm_av_av_repository_av_av_CompositeDataType)
gen_pcm_av_av_repository_av_av_CompositeDataType_repository_av_av_DataType = Generalization(general=repository_av_av_DataType, specific=pcm_av_av_repository_av_av_CompositeDataType)
gen_pcm_av_av_repository_av_av_InnerDeclaration_NamedElement = Generalization(general=NamedElement, specific=pcm_av_av_repository_av_av_InnerDeclaration)
gen_pcm_av_av_repository_av_av_Role_Entity = Generalization(general=Entity, specific=pcm_av_av_repository_av_av_Role)
gen_pcm_av_av_resourcetype_av_av_ResourceSignature_Entity = Generalization(general=Entity, specific=pcm_av_av_resourcetype_av_av_ResourceSignature)
gen_pcm_av_av_resourcetype_av_av_ProcessingResourceType_ResourceType = Generalization(general=ResourceType, specific=pcm_av_av_resourcetype_av_av_ProcessingResourceType)
gen_pcm_av_av_resourcetype_av_av_ResourceType_entity_av_av_Entity = Generalization(general=entity_av_av_Entity, specific=pcm_av_av_resourcetype_av_av_ResourceType)
gen_pcm_av_av_resourcetype_av_av_ResourceType_UnitCarryingElement = Generalization(general=UnitCarryingElement, specific=pcm_av_av_resourcetype_av_av_ResourceType)
gen_pcm_av_av_resourcetype_av_av_ResourceType_entity_av_av_ResourceInterfaceProvidingEntity = Generalization(general=entity_av_av_ResourceInterfaceProvidingEntity, specific=pcm_av_av_resourcetype_av_av_ResourceType)
gen_pcm_av_av_resourcetype_av_av_SchedulingPolicy_Entity = Generalization(general=Entity, specific=pcm_av_av_resourcetype_av_av_SchedulingPolicy)
gen_pcm_av_av_resourcetype_av_av_CommunicationLinkResourceType_ResourceType = Generalization(general=ResourceType, specific=pcm_av_av_resourcetype_av_av_CommunicationLinkResourceType)
gen_pcm_av_av_resourcetype_av_av_ResourceInterface_Entity = Generalization(general=Entity, specific=pcm_av_av_resourcetype_av_av_ResourceInterface)
gen_pcm_av_av_parameter_av_av_CharacterisedVariable_Variable = Generalization(general=Variable, specific=pcm_av_av_parameter_av_av_CharacterisedVariable)
gen_pcm_av_av_reliability_av_av_HardwareInducedFailureType_FailureType = Generalization(general=FailureType, specific=pcm_av_av_reliability_av_av_HardwareInducedFailureType)
gen_pcm_av_av_reliability_av_av_SoftwareInducedFailureType_FailureType = Generalization(general=FailureType, specific=pcm_av_av_reliability_av_av_SoftwareInducedFailureType)
gen_pcm_av_av_reliability_av_av_InternalFailureOccurrenceDescription_FailureOccurrenceDescription = Generalization(general=FailureOccurrenceDescription, specific=pcm_av_av_reliability_av_av_InternalFailureOccurrenceDescription)
gen_pcm_av_av_reliability_av_av_NetworkInducedFailureType_FailureType = Generalization(general=FailureType, specific=pcm_av_av_reliability_av_av_NetworkInducedFailureType)
gen_pcm_av_av_reliability_av_av_ExternalFailureOccurrenceDescription_FailureOccurrenceDescription = Generalization(general=FailureOccurrenceDescription, specific=pcm_av_av_reliability_av_av_ExternalFailureOccurrenceDescription)
gen_pcm_av_av_reliability_av_av_ResourceTimeoutFailureType_SoftwareInducedFailureType = Generalization(general=SoftwareInducedFailureType, specific=pcm_av_av_reliability_av_av_ResourceTimeoutFailureType)
gen_pcm_av_av_reliability_av_av_FailureType_Entity = Generalization(general=Entity, specific=pcm_av_av_reliability_av_av_FailureType)
gen_pcm_av_av_seff_av_av_StopAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_av_av_seff_av_av_StopAction)
gen_pcm_av_av_seff_av_av_AbstractInternalControlFlowAction_AbstractAction = Generalization(general=AbstractAction, specific=pcm_av_av_seff_av_av_AbstractInternalControlFlowAction)
gen_pcm_av_av_seff_av_av_AbstractAction_Entity = Generalization(general=Entity, specific=pcm_av_av_seff_av_av_AbstractAction)
gen_pcm_av_av_seff_av_av_ResourceDemandingBehaviour_Identifier = Generalization(general=Identifier, specific=pcm_av_av_seff_av_av_ResourceDemandingBehaviour)
gen_pcm_av_av_seff_av_av_AbstractLoopAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_av_av_seff_av_av_AbstractLoopAction)
gen_pcm_av_av_seff_av_av_AbstractBranchTransition_Entity = Generalization(general=Entity, specific=pcm_av_av_seff_av_av_AbstractBranchTransition)
gen_pcm_av_av_seff_av_av_BranchAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_av_av_seff_av_av_BranchAction)
gen_pcm_av_av_seff_av_av_StartAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_av_av_seff_av_av_StartAction)
gen_pcm_av_av_seff_av_av_ResourceDemandingSEFF_Identifier = Generalization(general=Identifier, specific=pcm_av_av_seff_av_av_ResourceDemandingSEFF)
gen_pcm_av_av_seff_av_av_ResourceDemandingSEFF_seff_av_av_ServiceEffectSpecification = Generalization(general=seff_av_av_ServiceEffectSpecification, specific=pcm_av_av_seff_av_av_ResourceDemandingSEFF)
gen_pcm_av_av_seff_av_av_ResourceDemandingSEFF_seff_av_av_ResourceDemandingBehaviour = Generalization(general=seff_av_av_ResourceDemandingBehaviour, specific=pcm_av_av_seff_av_av_ResourceDemandingSEFF)
gen_pcm_av_av_seff_av_av_ResourceDemandingInternalBehaviour_ResourceDemandingBehaviour = Generalization(general=ResourceDemandingBehaviour, specific=pcm_av_av_seff_av_av_ResourceDemandingInternalBehaviour)
gen_pcm_av_av_seff_av_av_ReleaseAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_av_av_seff_av_av_ReleaseAction)
gen_pcm_av_av_seff_av_av_ForkAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_av_av_seff_av_av_ForkAction)
gen_pcm_av_av_seff_av_av_ForkedBehaviour_ResourceDemandingBehaviour = Generalization(general=ResourceDemandingBehaviour, specific=pcm_av_av_seff_av_av_ForkedBehaviour)
gen_pcm_av_av_seff_av_av_ExternalCallAction_seff_av_av_AbstractAction = Generalization(general=seff_av_av_AbstractAction, specific=pcm_av_av_seff_av_av_ExternalCallAction)
gen_pcm_av_av_seff_av_av_ExternalCallAction_seff_av_av_CallReturnAction = Generalization(general=seff_av_av_CallReturnAction, specific=pcm_av_av_seff_av_av_ExternalCallAction)
gen_pcm_av_av_seff_av_av_ExternalCallAction_seff_reliability_av_av_FailureHandlingEntity = Generalization(general=seff_reliability_av_av_FailureHandlingEntity, specific=pcm_av_av_seff_av_av_ExternalCallAction)
gen_pcm_av_av_seff_av_av_LoopAction_AbstractLoopAction = Generalization(general=AbstractLoopAction, specific=pcm_av_av_seff_av_av_LoopAction)
gen_pcm_av_av_seff_av_av_CallReturnAction_CallAction = Generalization(general=CallAction, specific=pcm_av_av_seff_av_av_CallReturnAction)
gen_pcm_av_av_seff_av_av_ProbabilisticBranchTransition_AbstractBranchTransition = Generalization(general=AbstractBranchTransition, specific=pcm_av_av_seff_av_av_ProbabilisticBranchTransition)
gen_pcm_av_av_seff_av_av_AcquireAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_av_av_seff_av_av_AcquireAction)
gen_pcm_av_av_seff_av_av_CollectionIteratorAction_AbstractLoopAction = Generalization(general=AbstractLoopAction, specific=pcm_av_av_seff_av_av_CollectionIteratorAction)
gen_pcm_av_av_seff_av_av_GuardedBranchTransition_AbstractBranchTransition = Generalization(general=AbstractBranchTransition, specific=pcm_av_av_seff_av_av_GuardedBranchTransition)
gen_pcm_av_av_seff_av_av_SetVariableAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_av_av_seff_av_av_SetVariableAction)
gen_pcm_av_av_seff_av_av_InternalCallAction_seff_av_av_CallAction = Generalization(general=seff_av_av_CallAction, specific=pcm_av_av_seff_av_av_InternalCallAction)
gen_pcm_av_av_seff_av_av_InternalCallAction_seff_av_av_AbstractInternalControlFlowAction = Generalization(general=seff_av_av_AbstractInternalControlFlowAction, specific=pcm_av_av_seff_av_av_InternalCallAction)
gen_pcm_av_av_seff_av_av_EmitEventAction_seff_av_av_AbstractAction = Generalization(general=seff_av_av_AbstractAction, specific=pcm_av_av_seff_av_av_EmitEventAction)
gen_pcm_av_av_seff_av_av_EmitEventAction_seff_av_av_CallAction = Generalization(general=seff_av_av_CallAction, specific=pcm_av_av_seff_av_av_EmitEventAction)
gen_pcm_av_av_seff_av_av_InternalAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_av_av_seff_av_av_InternalAction)
gen_pcm_av_av_seff_performance_av_av_InfrastructureCall_CallAction = Generalization(general=CallAction, specific=pcm_av_av_seff_performance_av_av_InfrastructureCall)
gen_pcm_av_av_seff_performance_av_av_ResourceCall_CallAction = Generalization(general=CallAction, specific=pcm_av_av_seff_performance_av_av_ResourceCall)
gen_pcm_av_av_seff_reliability_av_av_RecoveryActionBehaviour_seff_reliability_av_av_FailureHandlingEntity = Generalization(general=seff_reliability_av_av_FailureHandlingEntity, specific=pcm_av_av_seff_reliability_av_av_RecoveryActionBehaviour)
gen_pcm_av_av_seff_reliability_av_av_RecoveryActionBehaviour_seff_av_av_ResourceDemandingBehaviour = Generalization(general=seff_av_av_ResourceDemandingBehaviour, specific=pcm_av_av_seff_reliability_av_av_RecoveryActionBehaviour)
gen_pcm_av_av_seff_reliability_av_av_RecoveryAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_av_av_seff_reliability_av_av_RecoveryAction)
gen_pcm_av_av_seff_reliability_av_av_FailureHandlingEntity_Entity = Generalization(general=Entity, specific=pcm_av_av_seff_reliability_av_av_FailureHandlingEntity)
gen_pcm_av_av_qosannotations_av_av_QoSAnnotations_Entity = Generalization(general=Entity, specific=pcm_av_av_qosannotations_av_av_QoSAnnotations)
gen_pcm_av_av_qos_performance_av_av_SystemSpecifiedExecutionTime_SpecifiedExecutionTime = Generalization(general=SpecifiedExecutionTime, specific=pcm_av_av_qos_performance_av_av_SystemSpecifiedExecutionTime)
gen_pcm_av_av_qos_performance_av_av_SpecifiedExecutionTime_SpecifiedQoSAnnotation = Generalization(general=SpecifiedQoSAnnotation, specific=pcm_av_av_qos_performance_av_av_SpecifiedExecutionTime)
gen_pcm_av_av_qos_performance_av_av_ComponentSpecifiedExecutionTime_SpecifiedExecutionTime = Generalization(general=SpecifiedExecutionTime, specific=pcm_av_av_qos_performance_av_av_ComponentSpecifiedExecutionTime)
gen_pcm_av_av_qos_reliability_av_av_SpecifiedReliabilityAnnotation_SpecifiedQoSAnnotation = Generalization(general=SpecifiedQoSAnnotation, specific=pcm_av_av_qos_reliability_av_av_SpecifiedReliabilityAnnotation)
gen_pcm_av_av_system_av_av_System_entity_av_av_Entity = Generalization(general=entity_av_av_Entity, specific=pcm_av_av_system_av_av_System)
gen_pcm_av_av_system_av_av_System_entity_av_av_ComposedProvidingRequiringEntity = Generalization(general=entity_av_av_ComposedProvidingRequiringEntity, specific=pcm_av_av_system_av_av_System)
gen_pcm_av_av_resourceenvironment_av_av_ResourceEnvironment_NamedElement = Generalization(general=NamedElement, specific=pcm_av_av_resourceenvironment_av_av_ResourceEnvironment)
gen_pcm_av_av_resourceenvironment_av_av_LinkingResource_Entity = Generalization(general=Entity, specific=pcm_av_av_resourceenvironment_av_av_LinkingResource)
gen_pcm_av_av_resourceenvironment_av_av_ResourceContainer_Entity = Generalization(general=Entity, specific=pcm_av_av_resourceenvironment_av_av_ResourceContainer)
gen_pcm_av_av_resourceenvironment_av_av_ProcessingResourceSpecification_Identifier = Generalization(general=Identifier, specific=pcm_av_av_resourceenvironment_av_av_ProcessingResourceSpecification)
gen_pcm_av_av_resourceenvironment_av_av_CommunicationLinkResourceSpecification_Identifier = Generalization(general=Identifier, specific=pcm_av_av_resourceenvironment_av_av_CommunicationLinkResourceSpecification)
gen_pcm_av_av_allocation_av_av_AllocationContext_Entity = Generalization(general=Entity, specific=pcm_av_av_allocation_av_av_AllocationContext)
gen_pcm_av_av_allocation_av_av_Allocation_Entity = Generalization(general=Entity, specific=pcm_av_av_allocation_av_av_Allocation)
gen_pcm_av_av_subsystem_av_av_SubSystem_entity_av_av_ComposedProvidingRequiringEntity = Generalization(general=entity_av_av_ComposedProvidingRequiringEntity, specific=pcm_av_av_subsystem_av_av_SubSystem)
gen_pcm_av_av_subsystem_av_av_SubSystem_repository_av_av_RepositoryComponent = Generalization(general=repository_av_av_RepositoryComponent, specific=pcm_av_av_subsystem_av_av_SubSystem)
gen_pcm_av_av_completions_av_av_Completion_entity_av_av_ComposedProvidingRequiringEntity = Generalization(general=entity_av_av_ComposedProvidingRequiringEntity, specific=pcm_av_av_completions_av_av_Completion)
gen_pcm_av_av_completions_av_av_Completion_repository_av_av_ImplementationComponentType = Generalization(general=repository_av_av_ImplementationComponentType, specific=pcm_av_av_completions_av_av_Completion)
gen_pcm_av_av_completions_av_av_DelegatingExternalCallAction_ExternalCallAction = Generalization(general=ExternalCallAction, specific=pcm_av_av_completions_av_av_DelegatingExternalCallAction)
gen_pcm_av_av_completions_av_av_NetworkDemandParametricResourceDemand_ParametricResourceDemand = Generalization(general=ParametricResourceDemand, specific=pcm_av_av_completions_av_av_NetworkDemandParametricResourceDemand)

# Domain Model
domain_model = DomainModel(
    name="pcm_av_av",
    types={pcm_av_av_EObject, pcm_av_av_GlobalScopeGlobalScope, pcm_av_av_PerJoinPointScopePerJoinPointScope, pcm_av_av_Advice, pcm_av_av_GlobalScope, pcm_av_av_PerJoinPointScope, pcm_av_av_core_av_av_PCMRandomVariable, RandomVariable, ClosedWorkload, PassiveResource, VariableCharacterisation, seff_performance_av_av_InfrastructureCall, seff_performance_av_av_ResourceCall, seff_performance_av_av_ParametricResourceDemand, pcm_av_av_DummyClass, pcm_av_av_AdviceAdvice, composition_av_av_EventChannelSinkConnector, composition_av_av_AssemblyEventConnector, Loop, OpenWorkload, Delay, CommunicationLinkResourceSpecification, ProcessingResourceSpecification, pcm_av_av_entity_av_av_ResourceProvidedRole, Role, entity_av_av_ResourceInterfaceProvidingEntity, ResourceInterface, pcm_av_av_entity_av_av_InterfaceProvidingRequiringEntity, entity_av_av_InterfaceProvidingEntity, entity_av_av_InterfaceRequiringEntity, pcm_av_av_entity_av_av_InterfaceProvidingEntity, Entity, ProvidedRole, pcm_av_av_entity_av_av_InterfaceRequiringEntity, entity_av_av_Entity, entity_av_av_ResourceInterfaceRequiringEntity, RequiredRole, pcm_av_av_entity_av_av_ResourceInterfaceRequiringEntity, entity_av_av_ResourceRequiredRole, LoopAction, GuardedBranchTransition, qos_performance_av_av_SpecifiedExecutionTime, pcm_av_av_entity_av_av_ResourceInterfaceProvidingEntity, entity_av_av_ResourceProvidedRole, pcm_av_av_entity_av_av_ComposedProvidingRequiringEntity, composition_av_av_ComposedStructure, entity_av_av_InterfaceProvidingRequiringEntity, pcm_av_av_entity_av_av_NamedElement, pcm_av_av_entity_av_av_ResourceInterfaceProvidingRequiringEntity, pcm_av_av_entity_av_av_Entity, Identifier, entity_av_av_NamedElement, pcm_av_av_composition_av_av_DelegationConnector, Connector, pcm_av_av_composition_av_av_Connector, pcm_av_av_composition_av_av_ComposedStructure, pcm_av_av_entity_av_av_ResourceRequiredRole, composition_av_av_AssemblyContext, composition_av_av_ResourceRequiredDelegationConnector, composition_av_av_EventChannel, composition_av_av_Connector, pcm_av_av_composition_av_av_ResourceRequiredDelegationConnector, pcm_av_av_composition_av_av_EventChannel, EventGroup, composition_av_av_EventChannelSourceConnector, pcm_av_av_composition_av_av_EventChannelSourceConnector, SourceRole, pcm_av_av_composition_av_av_EventChannelSinkConnector, SinkRole, OperationProvidedRole, pcm_av_av_composition_av_av_RequiredDelegationConnector, OperationRequiredRole, PCMRandomVariable, pcm_av_av_composition_av_av_ProvidedDelegationConnector, DelegationConnector, pcm_av_av_composition_av_av_AssemblyConnector, pcm_av_av_composition_av_av_AssemblyEventConnector, pcm_av_av_composition_av_av_SinkDelegationConnector, pcm_av_av_composition_av_av_AssemblyInfrastructureConnector, InfrastructureProvidedRole, InfrastructureRequiredRole, pcm_av_av_composition_av_av_ProvidedInfrastructureDelegationConnector, pcm_av_av_composition_av_av_RequiredInfrastructureDelegationConnector, pcm_av_av_composition_av_av_RequiredResourceDelegationConnector, pcm_av_av_composition_av_av_SourceDelegationConnector, pcm_av_av_composition_av_av_AssemblyContext, RepositoryComponent, VariableUsage, pcm_av_av_usagemodel_av_av_Workload, UsageScenario, pcm_av_av_usagemodel_av_av_UsageScenario, UsageModel, ScenarioBehaviour, Workload, pcm_av_av_usagemodel_av_av_UserData, pcm_av_av_usagemodel_av_av_UsageModel, UserData, pcm_av_av_usagemodel_av_av_EntryLevelSystemCall, AbstractUserAction, OperationSignature, pcm_av_av_usagemodel_av_av_AbstractUserAction, pcm_av_av_usagemodel_av_av_ScenarioBehaviour, BranchTransition, pcm_av_av_usagemodel_av_av_BranchTransition, Branch, pcm_av_av_usagemodel_av_av_Branch, pcm_av_av_usagemodel_av_av_Loop, pcm_av_av_usagemodel_av_av_Stop, pcm_av_av_usagemodel_av_av_Start, pcm_av_av_usagemodel_av_av_OpenWorkload, pcm_av_av_usagemodel_av_av_Delay, pcm_av_av_usagemodel_av_av_ClosedWorkload, pcm_av_av_repository_av_av_PassiveResource, BasicComponent, ResourceTimeoutFailureType, pcm_av_av_repository_av_av_BasicComponent, ImplementationComponentType, ServiceEffectSpecification, pcm_av_av_repository_av_av_ImplementationComponentType, CompleteComponentType, pcm_av_av_repository_av_av_RepositoryComponent, InterfaceProvidingRequiringEntity, Repository, pcm_av_av_repository_av_av_ProvidedRole, pcm_av_av_repository_av_av_Parameter, DataType, InfrastructureSignature, EventType, ResourceSignature, pcm_av_av_repository_av_av_DataType, pcm_av_av_repository_av_av_Repository, Interface, FailureType, pcm_av_av_repository_av_av_Interface, Protocol, RequiredCharacterisation, pcm_av_av_repository_av_av_RequiredCharacterisation, Parameter_, pcm_av_av_repository_av_av_EventGroup, pcm_av_av_repository_av_av_EventType, Signature, pcm_av_av_repository_av_av_Signature, ExceptionType, pcm_av_av_repository_av_av_ExceptionType, pcm_av_av_repository_av_av_InfrastructureSignature, InfrastructureInterface, pcm_av_av_repository_av_av_InfrastructureInterface, pcm_av_av_repository_av_av_InfrastructureRequiredRole, pcm_av_av_repository_av_av_RequiredRole, pcm_av_av_repository_av_av_OperationSignature, pcm_av_av_repository_av_av_OperationInterface, pcm_av_av_repository_av_av_OperationRequiredRole, pcm_av_av_repository_av_av_SourceRole, pcm_av_av_repository_av_av_SinkRole, pcm_av_av_repository_av_av_OperationProvidedRole, pcm_av_av_repository_av_av_InfrastructureProvidedRole, OperationInterface, pcm_av_av_repository_av_av_CompleteComponentType, ProvidesComponentType, pcm_av_av_repository_av_av_ProvidesComponentType, pcm_av_av_repository_av_av_CompositeComponent, entity_av_av_ComposedProvidingRequiringEntity, repository_av_av_ImplementationComponentType, pcm_av_av_repository_av_av_CollectionDataType, repository_av_av_DataType, pcm_av_av_repository_av_av_CompositeDataType, CompositeDataType, InnerDeclaration, pcm_av_av_repository_av_av_InnerDeclaration, NamedElement, pcm_av_av_repository_av_av_Role, pcm_av_av_resourcetype_av_av_ResourceSignature, pcm_av_av_resourcetype_av_av_ProcessingResourceType, ResourceType, pcm_av_av_repository_av_av_PrimitiveDataType, pcm_av_av_resourcetype_av_av_ResourceType, UnitCarryingElement, ResourceRepository, pcm_av_av_resourcetype_av_av_ResourceRepository, SchedulingPolicy, pcm_av_av_resourcetype_av_av_SchedulingPolicy, pcm_av_av_resourcetype_av_av_CommunicationLinkResourceType, NetworkInducedFailureType, pcm_av_av_resourcetype_av_av_ResourceInterface, pcm_av_av_protocol_av_av_Protocol, pcm_av_av_parameter_av_av_VariableUsage, HardwareInducedFailureType, SynchronisationPoint, CallReturnAction, SetVariableAction, SpecifiedOutputParameterAbstraction, EntryLevelSystemCall, parameter_av_av_pcm_av_av_AbstractNamedReference, pcm_av_av_parameter_av_av_VariableCharacterisation, pcm_av_av_parameter_av_av_CharacterisedVariable, Variable, pcm_av_av_reliability_av_av_FailureOccurrenceDescription, CallAction, pcm_av_av_reliability_av_av_HardwareInducedFailureType, ProcessingResourceType, pcm_av_av_reliability_av_av_SoftwareInducedFailureType, InternalFailureOccurrenceDescription, pcm_av_av_reliability_av_av_InternalFailureOccurrenceDescription, FailureOccurrenceDescription, InternalAction, SoftwareInducedFailureType, pcm_av_av_reliability_av_av_NetworkInducedFailureType, CommunicationLinkResourceType, pcm_av_av_reliability_av_av_ExternalFailureOccurrenceDescription, qos_reliability_av_av_SpecifiedReliabilityAnnotation, pcm_av_av_reliability_av_av_ResourceTimeoutFailureType, pcm_av_av_reliability_av_av_FailureType, pcm_av_av_seff_av_av_StopAction, AbstractInternalControlFlowAction, pcm_av_av_seff_av_av_AbstractInternalControlFlowAction, AbstractAction, pcm_av_av_seff_av_av_AbstractAction, ResourceDemandingBehaviour, pcm_av_av_seff_av_av_ResourceDemandingBehaviour, AbstractLoopAction, AbstractBranchTransition, pcm_av_av_seff_av_av_AbstractLoopAction, pcm_av_av_seff_av_av_AbstractBranchTransition, BranchAction, pcm_av_av_seff_av_av_BranchAction, pcm_av_av_seff_av_av_CallAction, pcm_av_av_seff_av_av_StartAction, pcm_av_av_seff_av_av_ServiceEffectSpecification, pcm_av_av_seff_av_av_ResourceDemandingSEFF, seff_av_av_ServiceEffectSpecification, seff_av_av_ResourceDemandingBehaviour, ResourceDemandingInternalBehaviour, pcm_av_av_seff_av_av_ResourceDemandingInternalBehaviour, ResourceDemandingSEFF, pcm_av_av_seff_av_av_ReleaseAction, pcm_av_av_seff_av_av_ForkAction, ForkedBehaviour, pcm_av_av_seff_av_av_ForkedBehaviour, ForkAction, pcm_av_av_seff_av_av_SynchronisationPoint, pcm_av_av_seff_av_av_ExternalCallAction, seff_av_av_AbstractAction, seff_av_av_CallReturnAction, seff_reliability_av_av_FailureHandlingEntity, pcm_av_av_seff_av_av_LoopAction, pcm_av_av_seff_av_av_CallReturnAction, pcm_av_av_seff_av_av_ProbabilisticBranchTransition, pcm_av_av_seff_av_av_AcquireAction, pcm_av_av_seff_av_av_CollectionIteratorAction, pcm_av_av_seff_av_av_GuardedBranchTransition, pcm_av_av_seff_av_av_SetVariableAction, pcm_av_av_seff_av_av_InternalCallAction, seff_av_av_CallAction, seff_av_av_AbstractInternalControlFlowAction, pcm_av_av_seff_av_av_EmitEventAction, pcm_av_av_seff_av_av_InternalAction, pcm_av_av_seff_performance_av_av_InfrastructureCall, pcm_av_av_seff_performance_av_av_ResourceCall, pcm_av_av_seff_performance_av_av_ParametricResourceDemand, pcm_av_av_seff_reliability_av_av_RecoveryActionBehaviour, seff_reliability_av_av_RecoveryActionBehaviour, seff_reliability_av_av_RecoveryAction, pcm_av_av_seff_reliability_av_av_RecoveryAction, pcm_av_av_seff_reliability_av_av_FailureHandlingEntity, pcm_av_av_qosannotations_av_av_SpecifiedQoSAnnotation, QoSAnnotations, pcm_av_av_qosannotations_av_av_QoSAnnotations, System, SpecifiedQoSAnnotation, pcm_av_av_qosannotations_av_av_SpecifiedOutputParameterAbstraction, pcm_av_av_qos_performance_av_av_SystemSpecifiedExecutionTime, SpecifiedExecutionTime, pcm_av_av_qos_performance_av_av_SpecifiedExecutionTime, pcm_av_av_qos_performance_av_av_ComponentSpecifiedExecutionTime, pcm_av_av_qos_reliability_av_av_SpecifiedReliabilityAnnotation, ExternalFailureOccurrenceDescription, pcm_av_av_system_av_av_System, pcm_av_av_resourceenvironment_av_av_ResourceEnvironment, LinkingResource, ResourceContainer, pcm_av_av_resourceenvironment_av_av_LinkingResource, ResourceEnvironment, pcm_av_av_resourceenvironment_av_av_ResourceContainer, pcm_av_av_resourceenvironment_av_av_ProcessingResourceSpecification, pcm_av_av_resourceenvironment_av_av_CommunicationLinkResourceSpecification, pcm_av_av_allocation_av_av_AllocationContext, Allocation, pcm_av_av_allocation_av_av_Allocation, AllocationContext, pcm_av_av_subsystem_av_av_SubSystem, repository_av_av_RepositoryComponent, pcm_av_av_completions_av_av_Completion, pcm_av_av_completions_av_av_CompletionRepository, Completion, pcm_av_av_completions_av_av_DelegatingExternalCallAction, ExternalCallAction, pcm_av_av_completions_av_av_NetworkDemandParametricResourceDemand, ParametricResourceDemand, ParameterModifier, ComponentType, PrimitiveTypeEnum, VariableCharacterisationType},
    associations={children0, scopedObject1, scopedObject3, children5, scopedObject7, scopedObject9, closedWorkload_PCMRandomVariable11, passiveResource_capacity_PCMRandomVariable12, variableCharacterisation_Specification13, infrastructureCall__PCMRandomVariable14, resourceCall__PCMRandomVariable15, parametricResourceDemand_PCMRandomVariable16, eventChannelSinkConnector__FilterCondition20, assemblyEventConnector__FilterCondition21, loop_LoopIteration22, openWorkload_PCMRandomVariable23, delay_TimeSpecification24, communicationLinkResourceSpecifcation_throughput_PCMRandomVariable25, processingResourceSpecification_processingRate_PCMRandomVariable26, communicationLinkResourceSpecification_latency_PCMRandomVariable27, resourceInterfaceProvidingEntity__ResourceProvidedRole29, providedResourceInterface__ResourceProvidedRole30, providedRoles_InterfaceProvidingEntity31, requiredRoles_InterfaceRequiringEntity32, resourceRequiredRoles__ResourceInterfaceRequiringEntity33, loopAction_PCMRandomVariable17, guardedBranchTransition_PCMRandomVariable18, specifiedExecutionTime_PCMRandomVariable19, resourceProvidedRoles__ResourceInterfaceProvidingEntity37, parentStructure__Connector38, requiredResourceInterface__ResourceRequiredRole34, resourceInterfaceRequiringEntity__ResourceRequiredRole36, assemblyContexts__ComposedStructure39, resourceRequiredDelegationConnectors_ComposedStructure40, eventChannel__ComposedStructure41, connectors__ComposedStructure42, innerResourceRequiredRole_ResourceRequiredDelegationConnector43, outerResourceRequiredRole_ResourceRequiredDelegationConnector44, parentStructure_ResourceRequiredDelegationConnector47, eventGroup__EventChannel49, eventChannelSourceConnector__EventChannel50, eventChannelSinkConnector__EventChannel51, parentStructure__EventChannel53, sourceRole__EventChannelSourceRole55, assemblyContext__EventChannelSourceConnector56, eventChannel__EventChannelSourceConnector58, sinkRole__EventChannelSinkConnector60, innerProvidedRole_ProvidedDelegationConnector67, outerProvidedRole_ProvidedDelegationConnector68, assemblyContext_ProvidedDelegationConnector71, innerRequiredRole_RequiredDelegationConnector74, filterCondition__EventChannelSinkConnector61, assemblyContext__EventChannelSinkConnector62, eventChannel__EventChannelSinkConnector65, outerRequiredRole_RequiredDelegationConnector75, assemblyContext_RequiredDelegationConnector78, requiringAssemblyContext_AssemblyConnector81, providingAssemblyContext_AssemblyConnector83, providedRole_AssemblyConnector86, requiredRole_AssemblyConnector89, sinkRole__AssemblyEventConnector92, sourceRole__AssemblyEventConnector94, sinkAssemblyContext__AssemblyEventConnector97, sourceAssemblyContext__AssemblyEventConnector100, filterCondition__AssemblyEventConnector103, innerSourceRole__SourceRole105, outerSourceRole__SourceRole107, assemblyContext__SourceDelegationConnector110, assemblyContext__SinkDelegationConnector113, innerSinkRole__SinkRole115, outerSinkRole__SinkRole118, providedRole__AssemblyInfrastructureConnector121, requiredRole__AssemblyInfrastructureConnector122, providingAssemblyContext__AssemblyInfrastructureConnector124, requiringAssemblyContext__AssemblyInfrastructureConnector127, innerProvidedRole__ProvidedInfrastructureDelegationConnector130, outerProvidedRole__ProvidedInfrastructureDelegationConnector132, assemblyContext__ProvidedInfrastructureDelegationConnector135, innerRequiredRole__RequiredInfrastructureDelegationConnector138, outerRequiredRole__RequiredInfrastructureDelegationConnector140, assemblyContext__RequiredInfrastructureDelegationConnector143, assemblyContext__RequiredResourceDelegationConnector146, outerRequiredRole__RequiredResourceDelegationConnector151, parentStructure__AssemblyContext154, encapsulatedComponent__AssemblyContext156, configParameterUsages__AssemblyContext157, usageScenario_Workload158, usageModel_UsageScenario159, scenarioBehaviour_UsageScenario160, workload_UsageScenario161, assemblyContext_userData162, usageModel_UserData164, userDataParameterUsages_UserData166, usageScenario_UsageModel168, userData_UsageModel170, innerRequiredRole__RequiredResourceDelegationConnector148, providedRole_EntryLevelSystemCall171, operationSignature__EntryLevelSystemCall173, outputParameterUsages_EntryLevelSystemCall175, inputParameterUsages_EntryLevelSystemCall177, successor179, predecessor180, scenarioBehaviour_AbstractUserAction182, usageScenario_SenarioBehaviour184, branchTransition_ScenarioBehaviour186, actions_ScenarioBehaviour189, branch_BranchTransition191, branchedBehaviour_BranchTransition192, branchTransitions_Branch194, loopIteration_Loop196, bodyBehaviour_Loop198, loop_ScenarioBehaviour187, interArrivalTime_OpenWorkload200, timeSpecification_Delay202, thinkTime_ClosedWorkload204, capacity_PassiveResource206, basicComponent_PassiveResource208, resourceTimeoutFailureType__PassiveResource209, serviceEffectSpecifications__BasicComponent210, passiveResource_BasicComponent211, parentCompleteComponentTypes213, componentParameterUsage_ImplementationComponentType214, repository__RepositoryComponent217, providingEntity_ProvidedRole218, dataType__Parameter219, infrastructureSignature__Parameter220, operationSignature__Parameter221, eventType__Parameter223, resourceSignature__Parameter224, repository__DataType225, components__Repository227, interfaces__Repository229, failureTypes__Repository230, dataTypes__Repository231, parentInterfaces__Interface233, protocols__Interface235, requiredCharacterisations237, repository__Interface238, parameter240, interface_RequiredCharacterisation241, eventTypes__EventGroup243, eventGroup__EventType247, exceptions__Signature249, failureType250, parameters__InfrastructureSignature253, infrastructureInterface__InfrastructureSignature255, infrastructureSignatures__InfrastructureInterface256, requiredInterface__InfrastructureRequiredRole258, requiringEntity_RequiredRole260, parameter__EventType245, parameters__OperationSignature262, returnType__OperationSignature264, signatures__OperationInterface266, requiredInterface__OperationRequiredRole268, eventGroup__SourceRole270, eventGroup__SinkRole272, providedInterface__OperationProvidedRole274, providedInterface__InfrastructureProvidedRole276, interface__OperationSignature261, parentProvidesComponentTypes278, innerType_CollectionDataType279, parentType_CompositeDataType281, innerDeclaration_CompositeDataType282, datatype_InnerDeclaration283, compositeDataType_InnerDeclaration285, parameter__ResourceSignature287, resourceInterface__ResourceSignature289, resourceRepository_ResourceType292, resourceInterfaces__ResourceRepository293, schedulingPolicies__ResourceRepository295, availableResourceTypes_ResourceRepository296, resourceRepository__SchedulingPolicy297, networkInducedFailureType__CommunicationLinkResourceType299, resourceRepository__ResourceInterface300, resourceSignatures__ResourceInterface302, variableCharacterisation_VariableUsage304, userData_VariableUsage306, hardwareInducedFailureType__ProcessingResourceType291, synchronisationPoint_VariableUsage309, callReturnAction__VariableUsage310, setVariableAction_VariableUsage311, specifiedOutputParameterAbstraction_expectedExternalOutputs_VariableUsage312, assemblyContext__VariableUsage313, entryLevelSystemCall_InputParameterUsage315, entryLevelSystemCall_OutputParameterUsage316, namedReference__VariableUsage318, specification_VariableCharacterisation319, variableUsage_VariableCharacterisation321, callAction__VariableUsage308, processingResourceType__HardwareInducedFailureType323, internalFailureOccurrenceDescriptions__SoftwareInducedFailureType324, internalAction__InternalFailureOccurrenceDescription325, softwareInducedFailureType__InternalFailureOccurrenceDescription326, communicationLinkResourceType__NetworkInducedFailureType327, specifiedReliabilityAnnotation__ExternalFailureOccurrenceDescription328, failureType__ExternalFailureOccurrenceDescription329, passiveResource__ResourceTimeoutFailureType331, repository__FailureType333, resourceDemand_Action335, infrastructureCall__Action337, resourceCall__Action339, predecessor_AbstractAction341, successor_AbstractAction342, resourceDemandingBehaviour_AbstractAction344, abstractLoopAction_ResourceDemandingBehaviour345, abstractBranchTransition_ResourceDemandingBehaviour347, steps_Behaviour348, bodyBehaviour_Loop350, branchAction_AbstractBranchTransition352, branchBehaviour_BranchTransition353, branches_Branch355, inputVariableUsages__CallAction357, describedService__SEFF359, basicComponent_ServiceEffectSpecification360, resourceDemandingInternalBehaviours362, resourceDemandingSEFF_ResourceDemandingInternalBehaviour363, passiveResource_ReleaseAction364, iterationCount_LoopAction366, asynchronousForkedBehaviours_ForkAction368, synchronisingBehaviours_ForkAction369, synchronisationPoint_ForkedBehaviour371, forkAction_ForkedBehaivour373, outputParameterUsage_SynchronisationPoint374, forkAction_SynchronisationPoint376, synchronousForkedBehaviours_SynchronisationPoint378, calledService_ExternalService380, role_ExternalService382, returnVariableUsage__CallReturnAction385, passiveresource_AcquireAction387, parameter_CollectionIteratorAction389, branchCondition_GuardedBranchTransition391, localVariableUsages_SetVariableAction393, calledResourceDemandingInternalBehaviour395, eventType__EmitEventAction397, sourceRole__EmitEventAction399, internalFailureOccurrenceDescriptions__InternalAction402, signature__InfrastructureCall404, numberOfCalls__InfrastructureCall406, action__InfrastructureCall408, requiredRole__InfrastructureCall409, resourceRequiredRole__ResourceCall414, signature__ResourceCall416, numberOfCalls__ResourceCall419, specification_ParametericResourceDemand421, requiredResource_ParametricResourceDemand423, action_ParametricResourceDemand425, action__ResourceCall412, failureHandlingAlternatives__RecoveryActionBehaviour427, recoveryAction__RecoveryActionBehaviour428, primaryBehaviour__RecoveryAction429, recoveryActionBehaviours__RecoveryAction431, failureTypes_FailureHandlingEntity432, signature_SpecifiedQoSAnnation434, role_SpecifiedQoSAnnotation436, qosAnnotations_SpecifiedQoSAnnotation438, specifiedOutputParameterAbstractions_QoSAnnotations439, system_QoSAnnotations441, specifiedQoSAnnotations_QoSAnnotations442, signature_SpecifiedOutputParameterAbstraction443, role_SpecifiedOutputParameterAbstraction445, expectedExternalOutputs_SpecifiedOutputParameterAbstraction448, qosAnnotations_SpecifiedOutputParameterAbstraction450, specification_SpecifiedExecutionTime452, assemblyContext_ComponentSpecifiedExecutionTime454, externalFailureOccurrenceDescriptions__SpecifiedReliabilityAnnotation456, linkingResources__ResourceEnvironment459, resourceContainer_ResourceEnvironment460, connectedResourceContainers_LinkingResource461, communicationLinkResourceSpecifications_LinkingResource463, resourceEnvironment_LinkingResource465, activeResourceSpecifications_ResourceContainer466, resourceEnvironment_ResourceContainer468, nestedResourceContainers__ResourceContainer470, parentResourceContainer__ResourceContainer472, schedulingPolicy474, qosAnnotations_System457, processingRate_ProcessingResourceSpecification479, resourceContainer_ProcessingResourceSpecification481, linkingResource_CommunicationLinkResourceSpecification483, communicationLinkResourceType_CommunicationLinkResourceSpecification485, latency_CommunicationLinkResourceSpecification487, throughput_CommunicationLinkResourceSpecification489, resourceContainer_AllocationContext491, assemblyContext_AllocationContext493, allocation_AllocationContext496, activeResourceType_ActiveResourceSpecification476, targetResourceEnvironment_Allocation499, system_Allocation501, allocationContexts_Allocation504, completions_CompletionRepository505, requiredCommunicationLinkResource_ParametricResourceDemand506, eventChannel__AllocationContext497},
    generalizations={gen_pcm_av_av_core_av_av_PCMRandomVariable_RandomVariable, gen_pcm_av_av_entity_av_av_ResourceProvidedRole_Role, gen_pcm_av_av_entity_av_av_InterfaceProvidingRequiringEntity_entity_av_av_InterfaceProvidingEntity, gen_pcm_av_av_entity_av_av_InterfaceProvidingRequiringEntity_entity_av_av_InterfaceRequiringEntity, gen_pcm_av_av_entity_av_av_InterfaceProvidingEntity_Entity, gen_pcm_av_av_entity_av_av_InterfaceRequiringEntity_entity_av_av_Entity, gen_pcm_av_av_entity_av_av_InterfaceRequiringEntity_entity_av_av_ResourceInterfaceRequiringEntity, gen_pcm_av_av_entity_av_av_ResourceInterfaceRequiringEntity_Entity, gen_pcm_av_av_entity_av_av_ResourceInterfaceProvidingEntity_Entity, gen_pcm_av_av_entity_av_av_ComposedProvidingRequiringEntity_composition_av_av_ComposedStructure, gen_pcm_av_av_entity_av_av_ComposedProvidingRequiringEntity_entity_av_av_InterfaceProvidingRequiringEntity, gen_pcm_av_av_entity_av_av_ResourceInterfaceProvidingRequiringEntity_entity_av_av_ResourceInterfaceRequiringEntity, gen_pcm_av_av_entity_av_av_ResourceInterfaceProvidingRequiringEntity_entity_av_av_ResourceInterfaceProvidingEntity, gen_pcm_av_av_entity_av_av_Entity_Identifier, gen_pcm_av_av_entity_av_av_Entity_entity_av_av_NamedElement, gen_pcm_av_av_composition_av_av_DelegationConnector_Connector, gen_pcm_av_av_composition_av_av_Connector_Entity, gen_pcm_av_av_composition_av_av_ComposedStructure_Entity, gen_pcm_av_av_entity_av_av_ResourceRequiredRole_Role, gen_pcm_av_av_composition_av_av_EventChannel_Entity, gen_pcm_av_av_composition_av_av_EventChannelSourceConnector_Connector, gen_pcm_av_av_composition_av_av_EventChannelSinkConnector_Connector, gen_pcm_av_av_composition_av_av_RequiredDelegationConnector_DelegationConnector, gen_pcm_av_av_composition_av_av_ProvidedDelegationConnector_DelegationConnector, gen_pcm_av_av_composition_av_av_AssemblyConnector_Connector, gen_pcm_av_av_composition_av_av_AssemblyEventConnector_Connector, gen_pcm_av_av_composition_av_av_SinkDelegationConnector_DelegationConnector, gen_pcm_av_av_composition_av_av_AssemblyInfrastructureConnector_Connector, gen_pcm_av_av_composition_av_av_ProvidedInfrastructureDelegationConnector_DelegationConnector, gen_pcm_av_av_composition_av_av_RequiredInfrastructureDelegationConnector_DelegationConnector, gen_pcm_av_av_composition_av_av_RequiredResourceDelegationConnector_DelegationConnector, gen_pcm_av_av_composition_av_av_SourceDelegationConnector_DelegationConnector, gen_pcm_av_av_composition_av_av_AssemblyContext_Entity, gen_pcm_av_av_usagemodel_av_av_UsageScenario_Entity, gen_pcm_av_av_usagemodel_av_av_EntryLevelSystemCall_AbstractUserAction, gen_pcm_av_av_usagemodel_av_av_AbstractUserAction_Entity, gen_pcm_av_av_usagemodel_av_av_ScenarioBehaviour_Entity, gen_pcm_av_av_usagemodel_av_av_Branch_AbstractUserAction, gen_pcm_av_av_usagemodel_av_av_Loop_AbstractUserAction, gen_pcm_av_av_usagemodel_av_av_Stop_AbstractUserAction, gen_pcm_av_av_usagemodel_av_av_Start_AbstractUserAction, gen_pcm_av_av_usagemodel_av_av_OpenWorkload_Workload, gen_pcm_av_av_usagemodel_av_av_Delay_AbstractUserAction, gen_pcm_av_av_usagemodel_av_av_ClosedWorkload_Workload, gen_pcm_av_av_repository_av_av_PassiveResource_Entity, gen_pcm_av_av_repository_av_av_BasicComponent_ImplementationComponentType, gen_pcm_av_av_repository_av_av_ImplementationComponentType_RepositoryComponent, gen_pcm_av_av_repository_av_av_RepositoryComponent_InterfaceProvidingRequiringEntity, gen_pcm_av_av_repository_av_av_ProvidedRole_Role, gen_pcm_av_av_repository_av_av_Repository_Entity, gen_pcm_av_av_repository_av_av_Interface_Entity, gen_pcm_av_av_repository_av_av_EventGroup_Interface, gen_pcm_av_av_repository_av_av_EventType_Signature, gen_pcm_av_av_repository_av_av_Signature_Entity, gen_pcm_av_av_repository_av_av_InfrastructureSignature_Signature, gen_pcm_av_av_repository_av_av_InfrastructureInterface_Interface, gen_pcm_av_av_repository_av_av_InfrastructureRequiredRole_RequiredRole, gen_pcm_av_av_repository_av_av_RequiredRole_Role, gen_pcm_av_av_repository_av_av_OperationSignature_Signature, gen_pcm_av_av_repository_av_av_OperationInterface_Interface, gen_pcm_av_av_repository_av_av_OperationRequiredRole_RequiredRole, gen_pcm_av_av_repository_av_av_SourceRole_RequiredRole, gen_pcm_av_av_repository_av_av_SinkRole_ProvidedRole, gen_pcm_av_av_repository_av_av_OperationProvidedRole_ProvidedRole, gen_pcm_av_av_repository_av_av_InfrastructureProvidedRole_ProvidedRole, gen_pcm_av_av_repository_av_av_CompleteComponentType_RepositoryComponent, gen_pcm_av_av_repository_av_av_ProvidesComponentType_RepositoryComponent, gen_pcm_av_av_repository_av_av_CompositeComponent_entity_av_av_ComposedProvidingRequiringEntity, gen_pcm_av_av_repository_av_av_CompositeComponent_repository_av_av_ImplementationComponentType, gen_pcm_av_av_repository_av_av_PrimitiveDataType_DataType, gen_pcm_av_av_repository_av_av_CollectionDataType_entity_av_av_Entity, gen_pcm_av_av_repository_av_av_CollectionDataType_repository_av_av_DataType, gen_pcm_av_av_repository_av_av_CompositeDataType_entity_av_av_Entity, gen_pcm_av_av_repository_av_av_CompositeDataType_repository_av_av_DataType, gen_pcm_av_av_repository_av_av_InnerDeclaration_NamedElement, gen_pcm_av_av_repository_av_av_Role_Entity, gen_pcm_av_av_resourcetype_av_av_ResourceSignature_Entity, gen_pcm_av_av_resourcetype_av_av_ProcessingResourceType_ResourceType, gen_pcm_av_av_resourcetype_av_av_ResourceType_entity_av_av_Entity, gen_pcm_av_av_resourcetype_av_av_ResourceType_UnitCarryingElement, gen_pcm_av_av_resourcetype_av_av_ResourceType_entity_av_av_ResourceInterfaceProvidingEntity, gen_pcm_av_av_resourcetype_av_av_SchedulingPolicy_Entity, gen_pcm_av_av_resourcetype_av_av_CommunicationLinkResourceType_ResourceType, gen_pcm_av_av_resourcetype_av_av_ResourceInterface_Entity, gen_pcm_av_av_parameter_av_av_CharacterisedVariable_Variable, gen_pcm_av_av_reliability_av_av_HardwareInducedFailureType_FailureType, gen_pcm_av_av_reliability_av_av_SoftwareInducedFailureType_FailureType, gen_pcm_av_av_reliability_av_av_InternalFailureOccurrenceDescription_FailureOccurrenceDescription, gen_pcm_av_av_reliability_av_av_NetworkInducedFailureType_FailureType, gen_pcm_av_av_reliability_av_av_ExternalFailureOccurrenceDescription_FailureOccurrenceDescription, gen_pcm_av_av_reliability_av_av_ResourceTimeoutFailureType_SoftwareInducedFailureType, gen_pcm_av_av_reliability_av_av_FailureType_Entity, gen_pcm_av_av_seff_av_av_StopAction_AbstractInternalControlFlowAction, gen_pcm_av_av_seff_av_av_AbstractInternalControlFlowAction_AbstractAction, gen_pcm_av_av_seff_av_av_AbstractAction_Entity, gen_pcm_av_av_seff_av_av_ResourceDemandingBehaviour_Identifier, gen_pcm_av_av_seff_av_av_AbstractLoopAction_AbstractInternalControlFlowAction, gen_pcm_av_av_seff_av_av_AbstractBranchTransition_Entity, gen_pcm_av_av_seff_av_av_BranchAction_AbstractInternalControlFlowAction, gen_pcm_av_av_seff_av_av_StartAction_AbstractInternalControlFlowAction, gen_pcm_av_av_seff_av_av_ResourceDemandingSEFF_Identifier, gen_pcm_av_av_seff_av_av_ResourceDemandingSEFF_seff_av_av_ServiceEffectSpecification, gen_pcm_av_av_seff_av_av_ResourceDemandingSEFF_seff_av_av_ResourceDemandingBehaviour, gen_pcm_av_av_seff_av_av_ResourceDemandingInternalBehaviour_ResourceDemandingBehaviour, gen_pcm_av_av_seff_av_av_ReleaseAction_AbstractInternalControlFlowAction, gen_pcm_av_av_seff_av_av_ForkAction_AbstractInternalControlFlowAction, gen_pcm_av_av_seff_av_av_ForkedBehaviour_ResourceDemandingBehaviour, gen_pcm_av_av_seff_av_av_ExternalCallAction_seff_av_av_AbstractAction, gen_pcm_av_av_seff_av_av_ExternalCallAction_seff_av_av_CallReturnAction, gen_pcm_av_av_seff_av_av_ExternalCallAction_seff_reliability_av_av_FailureHandlingEntity, gen_pcm_av_av_seff_av_av_LoopAction_AbstractLoopAction, gen_pcm_av_av_seff_av_av_CallReturnAction_CallAction, gen_pcm_av_av_seff_av_av_ProbabilisticBranchTransition_AbstractBranchTransition, gen_pcm_av_av_seff_av_av_AcquireAction_AbstractInternalControlFlowAction, gen_pcm_av_av_seff_av_av_CollectionIteratorAction_AbstractLoopAction, gen_pcm_av_av_seff_av_av_GuardedBranchTransition_AbstractBranchTransition, gen_pcm_av_av_seff_av_av_SetVariableAction_AbstractInternalControlFlowAction, gen_pcm_av_av_seff_av_av_InternalCallAction_seff_av_av_CallAction, gen_pcm_av_av_seff_av_av_InternalCallAction_seff_av_av_AbstractInternalControlFlowAction, gen_pcm_av_av_seff_av_av_EmitEventAction_seff_av_av_AbstractAction, gen_pcm_av_av_seff_av_av_EmitEventAction_seff_av_av_CallAction, gen_pcm_av_av_seff_av_av_InternalAction_AbstractInternalControlFlowAction, gen_pcm_av_av_seff_performance_av_av_InfrastructureCall_CallAction, gen_pcm_av_av_seff_performance_av_av_ResourceCall_CallAction, gen_pcm_av_av_seff_reliability_av_av_RecoveryActionBehaviour_seff_reliability_av_av_FailureHandlingEntity, gen_pcm_av_av_seff_reliability_av_av_RecoveryActionBehaviour_seff_av_av_ResourceDemandingBehaviour, gen_pcm_av_av_seff_reliability_av_av_RecoveryAction_AbstractInternalControlFlowAction, gen_pcm_av_av_seff_reliability_av_av_FailureHandlingEntity_Entity, gen_pcm_av_av_qosannotations_av_av_QoSAnnotations_Entity, gen_pcm_av_av_qos_performance_av_av_SystemSpecifiedExecutionTime_SpecifiedExecutionTime, gen_pcm_av_av_qos_performance_av_av_SpecifiedExecutionTime_SpecifiedQoSAnnotation, gen_pcm_av_av_qos_performance_av_av_ComponentSpecifiedExecutionTime_SpecifiedExecutionTime, gen_pcm_av_av_qos_reliability_av_av_SpecifiedReliabilityAnnotation_SpecifiedQoSAnnotation, gen_pcm_av_av_system_av_av_System_entity_av_av_Entity, gen_pcm_av_av_system_av_av_System_entity_av_av_ComposedProvidingRequiringEntity, gen_pcm_av_av_resourceenvironment_av_av_ResourceEnvironment_NamedElement, gen_pcm_av_av_resourceenvironment_av_av_LinkingResource_Entity, gen_pcm_av_av_resourceenvironment_av_av_ResourceContainer_Entity, gen_pcm_av_av_resourceenvironment_av_av_ProcessingResourceSpecification_Identifier, gen_pcm_av_av_resourceenvironment_av_av_CommunicationLinkResourceSpecification_Identifier, gen_pcm_av_av_allocation_av_av_AllocationContext_Entity, gen_pcm_av_av_allocation_av_av_Allocation_Entity, gen_pcm_av_av_subsystem_av_av_SubSystem_entity_av_av_ComposedProvidingRequiringEntity, gen_pcm_av_av_subsystem_av_av_SubSystem_repository_av_av_RepositoryComponent, gen_pcm_av_av_completions_av_av_Completion_entity_av_av_ComposedProvidingRequiringEntity, gen_pcm_av_av_completions_av_av_Completion_repository_av_av_ImplementationComponentType, gen_pcm_av_av_completions_av_av_DelegatingExternalCallAction_ExternalCallAction, gen_pcm_av_av_completions_av_av_NetworkDemandParametricResourceDemand_ParametricResourceDemand},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)