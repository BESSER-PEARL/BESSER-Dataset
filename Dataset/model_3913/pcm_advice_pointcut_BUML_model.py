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
            EnumerationLiteral(name="in_"),
			EnumerationLiteral(name="out"),
			EnumerationLiteral(name="none"),
			EnumerationLiteral(name="inout")
    }
)

ComponentType: Enumeration = Enumeration(
    name="ComponentType",
    literals={
            EnumerationLiteral(name="INFRASTRUCTURE_COMPONENT"),
			EnumerationLiteral(name="BUSINESS_COMPONENT")
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
            EnumerationLiteral(name="NUMBER_OF_ELEMENTS"),
			EnumerationLiteral(name="VALUE"),
			EnumerationLiteral(name="BYTESIZE"),
			EnumerationLiteral(name="TYPE"),
			EnumerationLiteral(name="STRUCTURE")
    }
)

# Classes
pcm_av_pc_Pointcut = Class(name="pcm_av_pc_Pointcut")
pcm_av_pc_core_av_pc_PCMRandomVariable = Class(name="pcm_av_pc_core_av_pc_PCMRandomVariable")
RandomVariable = Class(name="RandomVariable")
pcm_av_pc_DummyClass = Class(name="pcm_av_pc_DummyClass")
pcm_av_pc_Advice = Class(name="pcm_av_pc_Advice")
pcm_av_pc_EObject = Class(name="pcm_av_pc_EObject")
pcm_av_pc_GlobalScope = Class(name="pcm_av_pc_GlobalScope")
pcm_av_pc_PerJoinPointScope = Class(name="pcm_av_pc_PerJoinPointScope")
CommunicationLinkResourceSpecification = Class(name="CommunicationLinkResourceSpecification")
ProcessingResourceSpecification = Class(name="ProcessingResourceSpecification")
pcm_av_pc_entity_av_pc_ResourceProvidedRole = Class(name="pcm_av_pc_entity_av_pc_ResourceProvidedRole")
Role = Class(name="Role")
entity_av_pc_ResourceInterfaceProvidingEntity = Class(name="entity_av_pc_ResourceInterfaceProvidingEntity")
ClosedWorkload = Class(name="ClosedWorkload")
PassiveResource = Class(name="PassiveResource")
VariableCharacterisation = Class(name="VariableCharacterisation")
seff_performance_av_pc_InfrastructureCall = Class(name="seff_performance_av_pc_InfrastructureCall")
seff_performance_av_pc_ResourceCall = Class(name="seff_performance_av_pc_ResourceCall")
seff_performance_av_pc_ParametricResourceDemand = Class(name="seff_performance_av_pc_ParametricResourceDemand")
LoopAction = Class(name="LoopAction")
GuardedBranchTransition = Class(name="GuardedBranchTransition")
qos_performance_av_pc_SpecifiedExecutionTime = Class(name="qos_performance_av_pc_SpecifiedExecutionTime")
composition_av_pc_EventChannelSinkConnector = Class(name="composition_av_pc_EventChannelSinkConnector")
composition_av_pc_AssemblyEventConnector = Class(name="composition_av_pc_AssemblyEventConnector")
Loop = Class(name="Loop")
OpenWorkload = Class(name="OpenWorkload")
Delay = Class(name="Delay")
pcm_av_pc_entity_av_pc_NamedElement = Class(name="pcm_av_pc_entity_av_pc_NamedElement")
pcm_av_pc_entity_av_pc_ResourceInterfaceProvidingRequiringEntity = Class(name="pcm_av_pc_entity_av_pc_ResourceInterfaceProvidingRequiringEntity")
pcm_av_pc_entity_av_pc_Entity = Class(name="pcm_av_pc_entity_av_pc_Entity")
Identifier = Class(name="Identifier")
entity_av_pc_NamedElement = Class(name="entity_av_pc_NamedElement")
pcm_av_pc_composition_av_pc_DelegationConnector = Class(name="pcm_av_pc_composition_av_pc_DelegationConnector")
Connector = Class(name="Connector")
ResourceInterface = Class(name="ResourceInterface")
pcm_av_pc_entity_av_pc_InterfaceProvidingRequiringEntity = Class(name="pcm_av_pc_entity_av_pc_InterfaceProvidingRequiringEntity")
entity_av_pc_InterfaceProvidingEntity = Class(name="entity_av_pc_InterfaceProvidingEntity")
entity_av_pc_InterfaceRequiringEntity = Class(name="entity_av_pc_InterfaceRequiringEntity")
pcm_av_pc_entity_av_pc_InterfaceProvidingEntity = Class(name="pcm_av_pc_entity_av_pc_InterfaceProvidingEntity")
Entity = Class(name="Entity")
ProvidedRole = Class(name="ProvidedRole")
pcm_av_pc_entity_av_pc_InterfaceRequiringEntity = Class(name="pcm_av_pc_entity_av_pc_InterfaceRequiringEntity")
entity_av_pc_Entity = Class(name="entity_av_pc_Entity")
entity_av_pc_ResourceInterfaceRequiringEntity = Class(name="entity_av_pc_ResourceInterfaceRequiringEntity")
RequiredRole = Class(name="RequiredRole")
pcm_av_pc_entity_av_pc_ResourceInterfaceRequiringEntity = Class(name="pcm_av_pc_entity_av_pc_ResourceInterfaceRequiringEntity")
entity_av_pc_ResourceRequiredRole = Class(name="entity_av_pc_ResourceRequiredRole")
pcm_av_pc_entity_av_pc_ResourceRequiredRole = Class(name="pcm_av_pc_entity_av_pc_ResourceRequiredRole")
pcm_av_pc_entity_av_pc_ResourceInterfaceProvidingEntity = Class(name="pcm_av_pc_entity_av_pc_ResourceInterfaceProvidingEntity")
entity_av_pc_ResourceProvidedRole = Class(name="entity_av_pc_ResourceProvidedRole")
pcm_av_pc_entity_av_pc_ComposedProvidingRequiringEntity = Class(name="pcm_av_pc_entity_av_pc_ComposedProvidingRequiringEntity")
composition_av_pc_ComposedStructure = Class(name="composition_av_pc_ComposedStructure")
entity_av_pc_InterfaceProvidingRequiringEntity = Class(name="entity_av_pc_InterfaceProvidingRequiringEntity")
pcm_av_pc_composition_av_pc_EventChannel = Class(name="pcm_av_pc_composition_av_pc_EventChannel")
EventGroup = Class(name="EventGroup")
composition_av_pc_EventChannelSourceConnector = Class(name="composition_av_pc_EventChannelSourceConnector")
pcm_av_pc_composition_av_pc_EventChannelSourceConnector = Class(name="pcm_av_pc_composition_av_pc_EventChannelSourceConnector")
pcm_av_pc_composition_av_pc_Connector = Class(name="pcm_av_pc_composition_av_pc_Connector")
pcm_av_pc_composition_av_pc_ComposedStructure = Class(name="pcm_av_pc_composition_av_pc_ComposedStructure")
composition_av_pc_AssemblyContext = Class(name="composition_av_pc_AssemblyContext")
composition_av_pc_ResourceRequiredDelegationConnector = Class(name="composition_av_pc_ResourceRequiredDelegationConnector")
composition_av_pc_EventChannel = Class(name="composition_av_pc_EventChannel")
composition_av_pc_Connector = Class(name="composition_av_pc_Connector")
pcm_av_pc_composition_av_pc_ResourceRequiredDelegationConnector = Class(name="pcm_av_pc_composition_av_pc_ResourceRequiredDelegationConnector")
SourceRole = Class(name="SourceRole")
pcm_av_pc_composition_av_pc_EventChannelSinkConnector = Class(name="pcm_av_pc_composition_av_pc_EventChannelSinkConnector")
SinkRole = Class(name="SinkRole")
PCMRandomVariable = Class(name="PCMRandomVariable")
pcm_av_pc_composition_av_pc_ProvidedDelegationConnector = Class(name="pcm_av_pc_composition_av_pc_ProvidedDelegationConnector")
DelegationConnector = Class(name="DelegationConnector")
OperationProvidedRole = Class(name="OperationProvidedRole")
pcm_av_pc_composition_av_pc_RequiredDelegationConnector = Class(name="pcm_av_pc_composition_av_pc_RequiredDelegationConnector")
pcm_av_pc_composition_av_pc_AssemblyEventConnector = Class(name="pcm_av_pc_composition_av_pc_AssemblyEventConnector")
OperationRequiredRole = Class(name="OperationRequiredRole")
pcm_av_pc_composition_av_pc_AssemblyConnector = Class(name="pcm_av_pc_composition_av_pc_AssemblyConnector")
pcm_av_pc_composition_av_pc_RequiredInfrastructureDelegationConnector = Class(name="pcm_av_pc_composition_av_pc_RequiredInfrastructureDelegationConnector")
pcm_av_pc_composition_av_pc_RequiredResourceDelegationConnector = Class(name="pcm_av_pc_composition_av_pc_RequiredResourceDelegationConnector")
pcm_av_pc_composition_av_pc_SourceDelegationConnector = Class(name="pcm_av_pc_composition_av_pc_SourceDelegationConnector")
pcm_av_pc_composition_av_pc_SinkDelegationConnector = Class(name="pcm_av_pc_composition_av_pc_SinkDelegationConnector")
pcm_av_pc_composition_av_pc_AssemblyInfrastructureConnector = Class(name="pcm_av_pc_composition_av_pc_AssemblyInfrastructureConnector")
InfrastructureProvidedRole = Class(name="InfrastructureProvidedRole")
InfrastructureRequiredRole = Class(name="InfrastructureRequiredRole")
pcm_av_pc_composition_av_pc_ProvidedInfrastructureDelegationConnector = Class(name="pcm_av_pc_composition_av_pc_ProvidedInfrastructureDelegationConnector")
pcm_av_pc_usagemodel_av_pc_UsageModel = Class(name="pcm_av_pc_usagemodel_av_pc_UsageModel")
UserData = Class(name="UserData")
pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall = Class(name="pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall")
AbstractUserAction = Class(name="AbstractUserAction")
pcm_av_pc_composition_av_pc_AssemblyContext = Class(name="pcm_av_pc_composition_av_pc_AssemblyContext")
RepositoryComponent = Class(name="RepositoryComponent")
VariableUsage = Class(name="VariableUsage")
pcm_av_pc_usagemodel_av_pc_Workload = Class(name="pcm_av_pc_usagemodel_av_pc_Workload")
UsageScenario = Class(name="UsageScenario")
pcm_av_pc_usagemodel_av_pc_UsageScenario = Class(name="pcm_av_pc_usagemodel_av_pc_UsageScenario")
UsageModel = Class(name="UsageModel")
ScenarioBehaviour = Class(name="ScenarioBehaviour")
Workload = Class(name="Workload")
pcm_av_pc_usagemodel_av_pc_UserData = Class(name="pcm_av_pc_usagemodel_av_pc_UserData")
OperationSignature = Class(name="OperationSignature")
pcm_av_pc_usagemodel_av_pc_AbstractUserAction = Class(name="pcm_av_pc_usagemodel_av_pc_AbstractUserAction")
pcm_av_pc_usagemodel_av_pc_ScenarioBehaviour = Class(name="pcm_av_pc_usagemodel_av_pc_ScenarioBehaviour")
pcm_av_pc_usagemodel_av_pc_Start = Class(name="pcm_av_pc_usagemodel_av_pc_Start")
BranchTransition = Class(name="BranchTransition")
pcm_av_pc_usagemodel_av_pc_BranchTransition = Class(name="pcm_av_pc_usagemodel_av_pc_BranchTransition")
Branch = Class(name="Branch")
pcm_av_pc_usagemodel_av_pc_Branch = Class(name="pcm_av_pc_usagemodel_av_pc_Branch")
pcm_av_pc_usagemodel_av_pc_Loop = Class(name="pcm_av_pc_usagemodel_av_pc_Loop")
pcm_av_pc_usagemodel_av_pc_Stop = Class(name="pcm_av_pc_usagemodel_av_pc_Stop")
BasicComponent = Class(name="BasicComponent")
ResourceTimeoutFailureType = Class(name="ResourceTimeoutFailureType")
pcm_av_pc_repository_av_pc_BasicComponent = Class(name="pcm_av_pc_repository_av_pc_BasicComponent")
ImplementationComponentType = Class(name="ImplementationComponentType")
pcm_av_pc_usagemodel_av_pc_OpenWorkload = Class(name="pcm_av_pc_usagemodel_av_pc_OpenWorkload")
pcm_av_pc_usagemodel_av_pc_Delay = Class(name="pcm_av_pc_usagemodel_av_pc_Delay")
pcm_av_pc_usagemodel_av_pc_ClosedWorkload = Class(name="pcm_av_pc_usagemodel_av_pc_ClosedWorkload")
pcm_av_pc_repository_av_pc_PassiveResource = Class(name="pcm_av_pc_repository_av_pc_PassiveResource")
ServiceEffectSpecification = Class(name="ServiceEffectSpecification")
pcm_av_pc_repository_av_pc_RepositoryComponent = Class(name="pcm_av_pc_repository_av_pc_RepositoryComponent")
InterfaceProvidingRequiringEntity = Class(name="InterfaceProvidingRequiringEntity")
Repository = Class(name="Repository")
pcm_av_pc_repository_av_pc_ProvidedRole = Class(name="pcm_av_pc_repository_av_pc_ProvidedRole")
pcm_av_pc_repository_av_pc_ImplementationComponentType = Class(name="pcm_av_pc_repository_av_pc_ImplementationComponentType")
CompleteComponentType = Class(name="CompleteComponentType")
FailureType = Class(name="FailureType")
pcm_av_pc_repository_av_pc_Interface = Class(name="pcm_av_pc_repository_av_pc_Interface")
pcm_av_pc_repository_av_pc_Parameter = Class(name="pcm_av_pc_repository_av_pc_Parameter")
DataType = Class(name="DataType")
InfrastructureSignature = Class(name="InfrastructureSignature")
EventType = Class(name="EventType")
ResourceSignature = Class(name="ResourceSignature")
pcm_av_pc_repository_av_pc_DataType = Class(name="pcm_av_pc_repository_av_pc_DataType")
pcm_av_pc_repository_av_pc_Repository = Class(name="pcm_av_pc_repository_av_pc_Repository")
Interface = Class(name="Interface")
pcm_av_pc_repository_av_pc_ExceptionType = Class(name="pcm_av_pc_repository_av_pc_ExceptionType")
Protocol = Class(name="Protocol")
RequiredCharacterisation = Class(name="RequiredCharacterisation")
pcm_av_pc_repository_av_pc_RequiredCharacterisation = Class(name="pcm_av_pc_repository_av_pc_RequiredCharacterisation")
Parameter_ = Class(name="Parameter")
pcm_av_pc_repository_av_pc_EventGroup = Class(name="pcm_av_pc_repository_av_pc_EventGroup")
pcm_av_pc_repository_av_pc_EventType = Class(name="pcm_av_pc_repository_av_pc_EventType")
Signature = Class(name="Signature")
pcm_av_pc_repository_av_pc_Signature = Class(name="pcm_av_pc_repository_av_pc_Signature")
ExceptionType = Class(name="ExceptionType")
pcm_av_pc_repository_av_pc_OperationInterface = Class(name="pcm_av_pc_repository_av_pc_OperationInterface")
pcm_av_pc_repository_av_pc_InfrastructureSignature = Class(name="pcm_av_pc_repository_av_pc_InfrastructureSignature")
InfrastructureInterface = Class(name="InfrastructureInterface")
pcm_av_pc_repository_av_pc_InfrastructureInterface = Class(name="pcm_av_pc_repository_av_pc_InfrastructureInterface")
pcm_av_pc_repository_av_pc_InfrastructureRequiredRole = Class(name="pcm_av_pc_repository_av_pc_InfrastructureRequiredRole")
pcm_av_pc_repository_av_pc_RequiredRole = Class(name="pcm_av_pc_repository_av_pc_RequiredRole")
pcm_av_pc_repository_av_pc_OperationSignature = Class(name="pcm_av_pc_repository_av_pc_OperationSignature")
OperationInterface = Class(name="OperationInterface")
pcm_av_pc_repository_av_pc_OperationRequiredRole = Class(name="pcm_av_pc_repository_av_pc_OperationRequiredRole")
pcm_av_pc_repository_av_pc_SourceRole = Class(name="pcm_av_pc_repository_av_pc_SourceRole")
pcm_av_pc_repository_av_pc_SinkRole = Class(name="pcm_av_pc_repository_av_pc_SinkRole")
pcm_av_pc_repository_av_pc_OperationProvidedRole = Class(name="pcm_av_pc_repository_av_pc_OperationProvidedRole")
pcm_av_pc_repository_av_pc_InfrastructureProvidedRole = Class(name="pcm_av_pc_repository_av_pc_InfrastructureProvidedRole")
pcm_av_pc_repository_av_pc_CompositeComponent = Class(name="pcm_av_pc_repository_av_pc_CompositeComponent")
entity_av_pc_ComposedProvidingRequiringEntity = Class(name="entity_av_pc_ComposedProvidingRequiringEntity")
repository_av_pc_ImplementationComponentType = Class(name="repository_av_pc_ImplementationComponentType")
pcm_av_pc_repository_av_pc_CompleteComponentType = Class(name="pcm_av_pc_repository_av_pc_CompleteComponentType")
ProvidesComponentType = Class(name="ProvidesComponentType")
pcm_av_pc_repository_av_pc_ProvidesComponentType = Class(name="pcm_av_pc_repository_av_pc_ProvidesComponentType")
pcm_av_pc_repository_av_pc_Role = Class(name="pcm_av_pc_repository_av_pc_Role")
pcm_av_pc_resourcetype_av_pc_ResourceSignature = Class(name="pcm_av_pc_resourcetype_av_pc_ResourceSignature")
pcm_av_pc_repository_av_pc_PrimitiveDataType = Class(name="pcm_av_pc_repository_av_pc_PrimitiveDataType")
pcm_av_pc_repository_av_pc_CollectionDataType = Class(name="pcm_av_pc_repository_av_pc_CollectionDataType")
repository_av_pc_DataType = Class(name="repository_av_pc_DataType")
pcm_av_pc_repository_av_pc_CompositeDataType = Class(name="pcm_av_pc_repository_av_pc_CompositeDataType")
CompositeDataType = Class(name="CompositeDataType")
InnerDeclaration = Class(name="InnerDeclaration")
pcm_av_pc_repository_av_pc_InnerDeclaration = Class(name="pcm_av_pc_repository_av_pc_InnerDeclaration")
NamedElement = Class(name="NamedElement")
pcm_av_pc_protocol_av_pc_Protocol = Class(name="pcm_av_pc_protocol_av_pc_Protocol")
pcm_av_pc_resourcetype_av_pc_ProcessingResourceType = Class(name="pcm_av_pc_resourcetype_av_pc_ProcessingResourceType")
ResourceType = Class(name="ResourceType")
HardwareInducedFailureType = Class(name="HardwareInducedFailureType")
pcm_av_pc_resourcetype_av_pc_ResourceType = Class(name="pcm_av_pc_resourcetype_av_pc_ResourceType")
UnitCarryingElement = Class(name="UnitCarryingElement")
ResourceRepository = Class(name="ResourceRepository")
pcm_av_pc_resourcetype_av_pc_ResourceRepository = Class(name="pcm_av_pc_resourcetype_av_pc_ResourceRepository")
SchedulingPolicy = Class(name="SchedulingPolicy")
pcm_av_pc_resourcetype_av_pc_SchedulingPolicy = Class(name="pcm_av_pc_resourcetype_av_pc_SchedulingPolicy")
pcm_av_pc_resourcetype_av_pc_CommunicationLinkResourceType = Class(name="pcm_av_pc_resourcetype_av_pc_CommunicationLinkResourceType")
NetworkInducedFailureType = Class(name="NetworkInducedFailureType")
pcm_av_pc_resourcetype_av_pc_ResourceInterface = Class(name="pcm_av_pc_resourcetype_av_pc_ResourceInterface")
pcm_av_pc_parameter_av_pc_VariableUsage = Class(name="pcm_av_pc_parameter_av_pc_VariableUsage")
CallAction = Class(name="CallAction")
SynchronisationPoint = Class(name="SynchronisationPoint")
CallReturnAction = Class(name="CallReturnAction")
SetVariableAction = Class(name="SetVariableAction")
SpecifiedOutputParameterAbstraction = Class(name="SpecifiedOutputParameterAbstraction")
EntryLevelSystemCall = Class(name="EntryLevelSystemCall")
parameter_av_pc_pcm_av_pc_AbstractNamedReference = Class(name="parameter_av_pc_pcm_av_pc_AbstractNamedReference")
pcm_av_pc_parameter_av_pc_VariableCharacterisation = Class(name="pcm_av_pc_parameter_av_pc_VariableCharacterisation")
pcm_av_pc_parameter_av_pc_CharacterisedVariable = Class(name="pcm_av_pc_parameter_av_pc_CharacterisedVariable")
Variable = Class(name="Variable")
CommunicationLinkResourceType = Class(name="CommunicationLinkResourceType")
pcm_av_pc_reliability_av_pc_ExternalFailureOccurrenceDescription = Class(name="pcm_av_pc_reliability_av_pc_ExternalFailureOccurrenceDescription")
pcm_av_pc_reliability_av_pc_FailureOccurrenceDescription = Class(name="pcm_av_pc_reliability_av_pc_FailureOccurrenceDescription")
pcm_av_pc_reliability_av_pc_HardwareInducedFailureType = Class(name="pcm_av_pc_reliability_av_pc_HardwareInducedFailureType")
ProcessingResourceType = Class(name="ProcessingResourceType")
pcm_av_pc_reliability_av_pc_SoftwareInducedFailureType = Class(name="pcm_av_pc_reliability_av_pc_SoftwareInducedFailureType")
InternalFailureOccurrenceDescription = Class(name="InternalFailureOccurrenceDescription")
pcm_av_pc_reliability_av_pc_InternalFailureOccurrenceDescription = Class(name="pcm_av_pc_reliability_av_pc_InternalFailureOccurrenceDescription")
FailureOccurrenceDescription = Class(name="FailureOccurrenceDescription")
InternalAction = Class(name="InternalAction")
SoftwareInducedFailureType = Class(name="SoftwareInducedFailureType")
pcm_av_pc_reliability_av_pc_NetworkInducedFailureType = Class(name="pcm_av_pc_reliability_av_pc_NetworkInducedFailureType")
pcm_av_pc_seff_av_pc_AbstractInternalControlFlowAction = Class(name="pcm_av_pc_seff_av_pc_AbstractInternalControlFlowAction")
AbstractAction = Class(name="AbstractAction")
pcm_av_pc_seff_av_pc_AbstractAction = Class(name="pcm_av_pc_seff_av_pc_AbstractAction")
qos_reliability_av_pc_SpecifiedReliabilityAnnotation = Class(name="qos_reliability_av_pc_SpecifiedReliabilityAnnotation")
pcm_av_pc_reliability_av_pc_ResourceTimeoutFailureType = Class(name="pcm_av_pc_reliability_av_pc_ResourceTimeoutFailureType")
pcm_av_pc_reliability_av_pc_FailureType = Class(name="pcm_av_pc_reliability_av_pc_FailureType")
pcm_av_pc_seff_av_pc_StopAction = Class(name="pcm_av_pc_seff_av_pc_StopAction")
AbstractInternalControlFlowAction = Class(name="AbstractInternalControlFlowAction")
pcm_av_pc_seff_av_pc_AbstractBranchTransition = Class(name="pcm_av_pc_seff_av_pc_AbstractBranchTransition")
BranchAction = Class(name="BranchAction")
pcm_av_pc_seff_av_pc_BranchAction = Class(name="pcm_av_pc_seff_av_pc_BranchAction")
ResourceDemandingBehaviour = Class(name="ResourceDemandingBehaviour")
pcm_av_pc_seff_av_pc_ResourceDemandingBehaviour = Class(name="pcm_av_pc_seff_av_pc_ResourceDemandingBehaviour")
AbstractLoopAction = Class(name="AbstractLoopAction")
AbstractBranchTransition = Class(name="AbstractBranchTransition")
pcm_av_pc_seff_av_pc_AbstractLoopAction = Class(name="pcm_av_pc_seff_av_pc_AbstractLoopAction")
pcm_av_pc_seff_av_pc_ResourceDemandingSEFF = Class(name="pcm_av_pc_seff_av_pc_ResourceDemandingSEFF")
seff_av_pc_ServiceEffectSpecification = Class(name="seff_av_pc_ServiceEffectSpecification")
seff_av_pc_ResourceDemandingBehaviour = Class(name="seff_av_pc_ResourceDemandingBehaviour")
pcm_av_pc_seff_av_pc_CallAction = Class(name="pcm_av_pc_seff_av_pc_CallAction")
pcm_av_pc_seff_av_pc_StartAction = Class(name="pcm_av_pc_seff_av_pc_StartAction")
pcm_av_pc_seff_av_pc_ServiceEffectSpecification = Class(name="pcm_av_pc_seff_av_pc_ServiceEffectSpecification")
pcm_av_pc_seff_av_pc_ExternalCallAction = Class(name="pcm_av_pc_seff_av_pc_ExternalCallAction")
seff_av_pc_AbstractAction = Class(name="seff_av_pc_AbstractAction")
seff_av_pc_CallReturnAction = Class(name="seff_av_pc_CallReturnAction")
seff_reliability_av_pc_FailureHandlingEntity = Class(name="seff_reliability_av_pc_FailureHandlingEntity")
ResourceDemandingInternalBehaviour = Class(name="ResourceDemandingInternalBehaviour")
pcm_av_pc_seff_av_pc_ResourceDemandingInternalBehaviour = Class(name="pcm_av_pc_seff_av_pc_ResourceDemandingInternalBehaviour")
ResourceDemandingSEFF = Class(name="ResourceDemandingSEFF")
pcm_av_pc_seff_av_pc_ReleaseAction = Class(name="pcm_av_pc_seff_av_pc_ReleaseAction")
pcm_av_pc_seff_av_pc_LoopAction = Class(name="pcm_av_pc_seff_av_pc_LoopAction")
pcm_av_pc_seff_av_pc_ForkAction = Class(name="pcm_av_pc_seff_av_pc_ForkAction")
ForkedBehaviour = Class(name="ForkedBehaviour")
pcm_av_pc_seff_av_pc_ForkedBehaviour = Class(name="pcm_av_pc_seff_av_pc_ForkedBehaviour")
ForkAction = Class(name="ForkAction")
pcm_av_pc_seff_av_pc_SynchronisationPoint = Class(name="pcm_av_pc_seff_av_pc_SynchronisationPoint")
pcm_av_pc_seff_av_pc_CollectionIteratorAction = Class(name="pcm_av_pc_seff_av_pc_CollectionIteratorAction")
pcm_av_pc_seff_av_pc_GuardedBranchTransition = Class(name="pcm_av_pc_seff_av_pc_GuardedBranchTransition")
pcm_av_pc_seff_av_pc_SetVariableAction = Class(name="pcm_av_pc_seff_av_pc_SetVariableAction")
pcm_av_pc_seff_av_pc_CallReturnAction = Class(name="pcm_av_pc_seff_av_pc_CallReturnAction")
pcm_av_pc_seff_av_pc_ProbabilisticBranchTransition = Class(name="pcm_av_pc_seff_av_pc_ProbabilisticBranchTransition")
pcm_av_pc_seff_av_pc_AcquireAction = Class(name="pcm_av_pc_seff_av_pc_AcquireAction")
pcm_av_pc_seff_performance_av_pc_InfrastructureCall = Class(name="pcm_av_pc_seff_performance_av_pc_InfrastructureCall")
pcm_av_pc_seff_av_pc_InternalCallAction = Class(name="pcm_av_pc_seff_av_pc_InternalCallAction")
seff_av_pc_CallAction = Class(name="seff_av_pc_CallAction")
seff_av_pc_AbstractInternalControlFlowAction = Class(name="seff_av_pc_AbstractInternalControlFlowAction")
pcm_av_pc_seff_av_pc_EmitEventAction = Class(name="pcm_av_pc_seff_av_pc_EmitEventAction")
pcm_av_pc_seff_av_pc_InternalAction = Class(name="pcm_av_pc_seff_av_pc_InternalAction")
pcm_av_pc_seff_performance_av_pc_ResourceCall = Class(name="pcm_av_pc_seff_performance_av_pc_ResourceCall")
pcm_av_pc_seff_performance_av_pc_ParametricResourceDemand = Class(name="pcm_av_pc_seff_performance_av_pc_ParametricResourceDemand")
pcm_av_pc_seff_reliability_av_pc_RecoveryAction = Class(name="pcm_av_pc_seff_reliability_av_pc_RecoveryAction")
pcm_av_pc_seff_reliability_av_pc_FailureHandlingEntity = Class(name="pcm_av_pc_seff_reliability_av_pc_FailureHandlingEntity")
pcm_av_pc_seff_reliability_av_pc_RecoveryActionBehaviour = Class(name="pcm_av_pc_seff_reliability_av_pc_RecoveryActionBehaviour")
seff_reliability_av_pc_RecoveryActionBehaviour = Class(name="seff_reliability_av_pc_RecoveryActionBehaviour")
seff_reliability_av_pc_RecoveryAction = Class(name="seff_reliability_av_pc_RecoveryAction")
pcm_av_pc_qos_performance_av_pc_SystemSpecifiedExecutionTime = Class(name="pcm_av_pc_qos_performance_av_pc_SystemSpecifiedExecutionTime")
SpecifiedExecutionTime = Class(name="SpecifiedExecutionTime")
pcm_av_pc_qosannotations_av_pc_SpecifiedQoSAnnotation = Class(name="pcm_av_pc_qosannotations_av_pc_SpecifiedQoSAnnotation")
QoSAnnotations = Class(name="QoSAnnotations")
pcm_av_pc_qosannotations_av_pc_QoSAnnotations = Class(name="pcm_av_pc_qosannotations_av_pc_QoSAnnotations")
System = Class(name="System")
SpecifiedQoSAnnotation = Class(name="SpecifiedQoSAnnotation")
pcm_av_pc_qosannotations_av_pc_SpecifiedOutputParameterAbstraction = Class(name="pcm_av_pc_qosannotations_av_pc_SpecifiedOutputParameterAbstraction")
pcm_av_pc_qos_reliability_av_pc_SpecifiedReliabilityAnnotation = Class(name="pcm_av_pc_qos_reliability_av_pc_SpecifiedReliabilityAnnotation")
pcm_av_pc_qos_performance_av_pc_SpecifiedExecutionTime = Class(name="pcm_av_pc_qos_performance_av_pc_SpecifiedExecutionTime")
pcm_av_pc_qos_performance_av_pc_ComponentSpecifiedExecutionTime = Class(name="pcm_av_pc_qos_performance_av_pc_ComponentSpecifiedExecutionTime")
pcm_av_pc_resourceenvironment_av_pc_ResourceEnvironment = Class(name="pcm_av_pc_resourceenvironment_av_pc_ResourceEnvironment")
LinkingResource = Class(name="LinkingResource")
ResourceContainer = Class(name="ResourceContainer")
pcm_av_pc_resourceenvironment_av_pc_LinkingResource = Class(name="pcm_av_pc_resourceenvironment_av_pc_LinkingResource")
ExternalFailureOccurrenceDescription = Class(name="ExternalFailureOccurrenceDescription")
pcm_av_pc_system_av_pc_System = Class(name="pcm_av_pc_system_av_pc_System")
pcm_av_pc_resourceenvironment_av_pc_CommunicationLinkResourceSpecification = Class(name="pcm_av_pc_resourceenvironment_av_pc_CommunicationLinkResourceSpecification")
ResourceEnvironment = Class(name="ResourceEnvironment")
pcm_av_pc_resourceenvironment_av_pc_ResourceContainer = Class(name="pcm_av_pc_resourceenvironment_av_pc_ResourceContainer")
pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification = Class(name="pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification")
Allocation = Class(name="Allocation")
pcm_av_pc_allocation_av_pc_Allocation = Class(name="pcm_av_pc_allocation_av_pc_Allocation")
pcm_av_pc_allocation_av_pc_AllocationContext = Class(name="pcm_av_pc_allocation_av_pc_AllocationContext")
pcm_av_pc_completions_av_pc_Completion = Class(name="pcm_av_pc_completions_av_pc_Completion")
pcm_av_pc_completions_av_pc_CompletionRepository = Class(name="pcm_av_pc_completions_av_pc_CompletionRepository")
Completion = Class(name="Completion")
pcm_av_pc_completions_av_pc_DelegatingExternalCallAction = Class(name="pcm_av_pc_completions_av_pc_DelegatingExternalCallAction")
ExternalCallAction = Class(name="ExternalCallAction")
pcm_av_pc_completions_av_pc_NetworkDemandParametricResourceDemand = Class(name="pcm_av_pc_completions_av_pc_NetworkDemandParametricResourceDemand")
ParametricResourceDemand = Class(name="ParametricResourceDemand")
AllocationContext = Class(name="AllocationContext")
pcm_av_pc_subsystem_av_pc_SubSystem = Class(name="pcm_av_pc_subsystem_av_pc_SubSystem")
repository_av_pc_RepositoryComponent = Class(name="repository_av_pc_RepositoryComponent")

# pcm_av_pc_Pointcut class attributes and methods

# pcm_av_pc_core_av_pc_PCMRandomVariable class attributes and methods
pcm_av_pc_core_av_pc_PCMRandomVariable_m_SpecificationMustNotBeNULL: Method = Method(name="SpecificationMustNotBeNULL", parameters={Parameter(name='pcm_av_pc_diagnostics', type=StringType), Parameter(name='pcm_av_pc_context', type=StringType)}, type=BooleanType)
pcm_av_pc_core_av_pc_PCMRandomVariable.methods={pcm_av_pc_core_av_pc_PCMRandomVariable_m_SpecificationMustNotBeNULL}

# RandomVariable class attributes and methods

# pcm_av_pc_DummyClass class attributes and methods

# pcm_av_pc_Advice class attributes and methods

# pcm_av_pc_EObject class attributes and methods

# pcm_av_pc_GlobalScope class attributes and methods

# pcm_av_pc_PerJoinPointScope class attributes and methods

# CommunicationLinkResourceSpecification class attributes and methods

# ProcessingResourceSpecification class attributes and methods

# pcm_av_pc_entity_av_pc_ResourceProvidedRole class attributes and methods

# Role class attributes and methods

# entity_av_pc_ResourceInterfaceProvidingEntity class attributes and methods

# ClosedWorkload class attributes and methods

# PassiveResource class attributes and methods

# VariableCharacterisation class attributes and methods

# seff_performance_av_pc_InfrastructureCall class attributes and methods

# seff_performance_av_pc_ResourceCall class attributes and methods

# seff_performance_av_pc_ParametricResourceDemand class attributes and methods

# LoopAction class attributes and methods

# GuardedBranchTransition class attributes and methods

# qos_performance_av_pc_SpecifiedExecutionTime class attributes and methods

# composition_av_pc_EventChannelSinkConnector class attributes and methods

# composition_av_pc_AssemblyEventConnector class attributes and methods

# Loop class attributes and methods

# OpenWorkload class attributes and methods

# Delay class attributes and methods

# pcm_av_pc_entity_av_pc_NamedElement class attributes and methods
pcm_av_pc_entity_av_pc_NamedElement_entityName: Property = Property(name="entityName", type=StringType)
pcm_av_pc_entity_av_pc_NamedElement.attributes={pcm_av_pc_entity_av_pc_NamedElement_entityName}

# pcm_av_pc_entity_av_pc_ResourceInterfaceProvidingRequiringEntity class attributes and methods

# pcm_av_pc_entity_av_pc_Entity class attributes and methods

# Identifier class attributes and methods

# entity_av_pc_NamedElement class attributes and methods

# pcm_av_pc_composition_av_pc_DelegationConnector class attributes and methods

# Connector class attributes and methods

# ResourceInterface class attributes and methods

# pcm_av_pc_entity_av_pc_InterfaceProvidingRequiringEntity class attributes and methods

# entity_av_pc_InterfaceProvidingEntity class attributes and methods

# entity_av_pc_InterfaceRequiringEntity class attributes and methods

# pcm_av_pc_entity_av_pc_InterfaceProvidingEntity class attributes and methods

# Entity class attributes and methods

# ProvidedRole class attributes and methods

# pcm_av_pc_entity_av_pc_InterfaceRequiringEntity class attributes and methods

# entity_av_pc_Entity class attributes and methods

# entity_av_pc_ResourceInterfaceRequiringEntity class attributes and methods

# RequiredRole class attributes and methods

# pcm_av_pc_entity_av_pc_ResourceInterfaceRequiringEntity class attributes and methods

# entity_av_pc_ResourceRequiredRole class attributes and methods

# pcm_av_pc_entity_av_pc_ResourceRequiredRole class attributes and methods

# pcm_av_pc_entity_av_pc_ResourceInterfaceProvidingEntity class attributes and methods

# entity_av_pc_ResourceProvidedRole class attributes and methods

# pcm_av_pc_entity_av_pc_ComposedProvidingRequiringEntity class attributes and methods
pcm_av_pc_entity_av_pc_ComposedProvidingRequiringEntity_m_ProvidedRolesMustBeBound: Method = Method(name="ProvidedRolesMustBeBound", parameters={Parameter(name='pcm_av_pc_context', type=StringType), Parameter(name='pcm_av_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_pc_entity_av_pc_ComposedProvidingRequiringEntity.methods={pcm_av_pc_entity_av_pc_ComposedProvidingRequiringEntity_m_ProvidedRolesMustBeBound}

# composition_av_pc_ComposedStructure class attributes and methods

# entity_av_pc_InterfaceProvidingRequiringEntity class attributes and methods

# pcm_av_pc_composition_av_pc_EventChannel class attributes and methods

# EventGroup class attributes and methods

# composition_av_pc_EventChannelSourceConnector class attributes and methods

# pcm_av_pc_composition_av_pc_EventChannelSourceConnector class attributes and methods

# pcm_av_pc_composition_av_pc_Connector class attributes and methods

# pcm_av_pc_composition_av_pc_ComposedStructure class attributes and methods
pcm_av_pc_composition_av_pc_ComposedStructure_m_MultipleConnectorsConstraint: Method = Method(name="MultipleConnectorsConstraint", parameters={Parameter(name='pcm_av_pc_diagnostics', type=StringType), Parameter(name='pcm_av_pc_context', type=StringType)}, type=BooleanType)
pcm_av_pc_composition_av_pc_ComposedStructure_m_MultipleConnectorsConstraintForAssemblyConnectors: Method = Method(name="MultipleConnectorsConstraintForAssemblyConnectors", parameters={Parameter(name='pcm_av_pc_context', type=StringType), Parameter(name='pcm_av_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_pc_composition_av_pc_ComposedStructure.methods={pcm_av_pc_composition_av_pc_ComposedStructure_m_MultipleConnectorsConstraintForAssemblyConnectors, pcm_av_pc_composition_av_pc_ComposedStructure_m_MultipleConnectorsConstraint}

# composition_av_pc_AssemblyContext class attributes and methods

# composition_av_pc_ResourceRequiredDelegationConnector class attributes and methods

# composition_av_pc_EventChannel class attributes and methods

# composition_av_pc_Connector class attributes and methods

# pcm_av_pc_composition_av_pc_ResourceRequiredDelegationConnector class attributes and methods

# SourceRole class attributes and methods

# pcm_av_pc_composition_av_pc_EventChannelSinkConnector class attributes and methods

# SinkRole class attributes and methods

# PCMRandomVariable class attributes and methods

# pcm_av_pc_composition_av_pc_ProvidedDelegationConnector class attributes and methods
pcm_av_pc_composition_av_pc_ProvidedDelegationConnector_m_ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure: Method = Method(name="ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure", parameters={Parameter(name='pcm_av_pc_context', type=StringType), Parameter(name='pcm_av_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_pc_composition_av_pc_ProvidedDelegationConnector_m_ComponentOfAssemblyContextAndInnerRoleProvidingComponentNeedToBeTheSame: Method = Method(name="ComponentOfAssemblyContextAndInnerRoleProvidingComponentNeedToBeTheSame", parameters={Parameter(name='pcm_av_pc_diagnostics', type=StringType), Parameter(name='pcm_av_pc_context', type=StringType)}, type=BooleanType)
pcm_av_pc_composition_av_pc_ProvidedDelegationConnector.methods={pcm_av_pc_composition_av_pc_ProvidedDelegationConnector_m_ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure, pcm_av_pc_composition_av_pc_ProvidedDelegationConnector_m_ComponentOfAssemblyContextAndInnerRoleProvidingComponentNeedToBeTheSame}

# DelegationConnector class attributes and methods

# OperationProvidedRole class attributes and methods

# pcm_av_pc_composition_av_pc_RequiredDelegationConnector class attributes and methods
pcm_av_pc_composition_av_pc_RequiredDelegationConnector_m_ComponentOfAssemblyContextAndInnerRoleRequiringComponentNeedToBeTheSame: Method = Method(name="ComponentOfAssemblyContextAndInnerRoleRequiringComponentNeedToBeTheSame", parameters={Parameter(name='pcm_av_pc_context', type=StringType), Parameter(name='pcm_av_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_pc_composition_av_pc_RequiredDelegationConnector_m_RequiringEntityOfOuterRequiredRoleMustBeTheSameAsTheParentOfTheRequiredDelegationConnector: Method = Method(name="RequiringEntityOfOuterRequiredRoleMustBeTheSameAsTheParentOfTheRequiredDelegationConnector", parameters={Parameter(name='pcm_av_pc_diagnostics', type=StringType), Parameter(name='pcm_av_pc_context', type=StringType)}, type=BooleanType)
pcm_av_pc_composition_av_pc_RequiredDelegationConnector_m_RequiredDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure: Method = Method(name="RequiredDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure", parameters={Parameter(name='pcm_av_pc_diagnostics', type=StringType), Parameter(name='pcm_av_pc_context', type=StringType)}, type=BooleanType)
pcm_av_pc_composition_av_pc_RequiredDelegationConnector.methods={pcm_av_pc_composition_av_pc_RequiredDelegationConnector_m_ComponentOfAssemblyContextAndInnerRoleRequiringComponentNeedToBeTheSame, pcm_av_pc_composition_av_pc_RequiredDelegationConnector_m_RequiringEntityOfOuterRequiredRoleMustBeTheSameAsTheParentOfTheRequiredDelegationConnector, pcm_av_pc_composition_av_pc_RequiredDelegationConnector_m_RequiredDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure}

# pcm_av_pc_composition_av_pc_AssemblyEventConnector class attributes and methods

# OperationRequiredRole class attributes and methods

# pcm_av_pc_composition_av_pc_AssemblyConnector class attributes and methods
pcm_av_pc_composition_av_pc_AssemblyConnector_m_AssemblyConnectorsReferencedProvidedRolesAndChildContextMustMatch: Method = Method(name="AssemblyConnectorsReferencedProvidedRolesAndChildContextMustMatch", parameters={Parameter(name='pcm_av_pc_context', type=StringType), Parameter(name='pcm_av_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_pc_composition_av_pc_AssemblyConnector_m_AssemblyConnectorsReferencedRequiredRoleAndChildContextMustMatch: Method = Method(name="AssemblyConnectorsReferencedRequiredRoleAndChildContextMustMatch", parameters={Parameter(name='pcm_av_pc_context', type=StringType), Parameter(name='pcm_av_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_pc_composition_av_pc_AssemblyConnector_m_AssemblyConnectorsReferencedInterfacesMustMatch: Method = Method(name="AssemblyConnectorsReferencedInterfacesMustMatch", parameters={Parameter(name='pcm_av_pc_diagnostics', type=StringType), Parameter(name='pcm_av_pc_context', type=StringType)}, type=BooleanType)
pcm_av_pc_composition_av_pc_AssemblyConnector.methods={pcm_av_pc_composition_av_pc_AssemblyConnector_m_AssemblyConnectorsReferencedProvidedRolesAndChildContextMustMatch, pcm_av_pc_composition_av_pc_AssemblyConnector_m_AssemblyConnectorsReferencedInterfacesMustMatch, pcm_av_pc_composition_av_pc_AssemblyConnector_m_AssemblyConnectorsReferencedRequiredRoleAndChildContextMustMatch}

# pcm_av_pc_composition_av_pc_RequiredInfrastructureDelegationConnector class attributes and methods

# pcm_av_pc_composition_av_pc_RequiredResourceDelegationConnector class attributes and methods

# pcm_av_pc_composition_av_pc_SourceDelegationConnector class attributes and methods

# pcm_av_pc_composition_av_pc_SinkDelegationConnector class attributes and methods

# pcm_av_pc_composition_av_pc_AssemblyInfrastructureConnector class attributes and methods

# InfrastructureProvidedRole class attributes and methods

# InfrastructureRequiredRole class attributes and methods

# pcm_av_pc_composition_av_pc_ProvidedInfrastructureDelegationConnector class attributes and methods

# pcm_av_pc_usagemodel_av_pc_UsageModel class attributes and methods

# UserData class attributes and methods

# pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall class attributes and methods
pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall_priority: Property = Property(name="priority", type=IntegerType)
pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall_m_EntryLevelSystemCallMustReferenceProvidedRoleOfASystem: Method = Method(name="EntryLevelSystemCallMustReferenceProvidedRoleOfASystem", parameters={Parameter(name='pcm_av_pc_context', type=StringType), Parameter(name='pcm_av_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall_m_EntryLevelSystemCallSignatureMustMatchItsProvidedRole: Method = Method(name="EntryLevelSystemCallSignatureMustMatchItsProvidedRole", parameters={Parameter(name='pcm_av_pc_context', type=StringType), Parameter(name='pcm_av_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall.attributes={pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall_priority}
pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall.methods={pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall_m_EntryLevelSystemCallSignatureMustMatchItsProvidedRole, pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall_m_EntryLevelSystemCallMustReferenceProvidedRoleOfASystem}

# AbstractUserAction class attributes and methods

# pcm_av_pc_composition_av_pc_AssemblyContext class attributes and methods

# RepositoryComponent class attributes and methods

# VariableUsage class attributes and methods

# pcm_av_pc_usagemodel_av_pc_Workload class attributes and methods

# UsageScenario class attributes and methods

# pcm_av_pc_usagemodel_av_pc_UsageScenario class attributes and methods

# UsageModel class attributes and methods

# ScenarioBehaviour class attributes and methods

# Workload class attributes and methods

# pcm_av_pc_usagemodel_av_pc_UserData class attributes and methods

# OperationSignature class attributes and methods

# pcm_av_pc_usagemodel_av_pc_AbstractUserAction class attributes and methods

# pcm_av_pc_usagemodel_av_pc_ScenarioBehaviour class attributes and methods
pcm_av_pc_usagemodel_av_pc_ScenarioBehaviour_m_EachuseractionexceptStartandStopmusthaveapredecessorandsuccessor: Method = Method(name="EachuseractionexceptStartandStopmusthaveapredecessorandsuccessor", parameters={Parameter(name='pcm_av_pc_diagnostics', type=StringType), Parameter(name='pcm_av_pc_context', type=StringType)}, type=BooleanType)
pcm_av_pc_usagemodel_av_pc_ScenarioBehaviour_m_Exactlyonestart: Method = Method(name="Exactlyonestart", parameters={Parameter(name='pcm_av_pc_diagnostics', type=StringType), Parameter(name='pcm_av_pc_context', type=StringType)}, type=BooleanType)
pcm_av_pc_usagemodel_av_pc_ScenarioBehaviour_m_Exactlyonestop: Method = Method(name="Exactlyonestop", parameters={Parameter(name='pcm_av_pc_context', type=StringType), Parameter(name='pcm_av_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_pc_usagemodel_av_pc_ScenarioBehaviour.methods={pcm_av_pc_usagemodel_av_pc_ScenarioBehaviour_m_Exactlyonestart, pcm_av_pc_usagemodel_av_pc_ScenarioBehaviour_m_EachuseractionexceptStartandStopmusthaveapredecessorandsuccessor, pcm_av_pc_usagemodel_av_pc_ScenarioBehaviour_m_Exactlyonestop}

# pcm_av_pc_usagemodel_av_pc_Start class attributes and methods
pcm_av_pc_usagemodel_av_pc_Start_m_StartHasNoPredecessor: Method = Method(name="StartHasNoPredecessor", parameters={Parameter(name='pcm_av_pc_context', type=StringType), Parameter(name='pcm_av_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_pc_usagemodel_av_pc_Start.methods={pcm_av_pc_usagemodel_av_pc_Start_m_StartHasNoPredecessor}

# BranchTransition class attributes and methods

# pcm_av_pc_usagemodel_av_pc_BranchTransition class attributes and methods
pcm_av_pc_usagemodel_av_pc_BranchTransition_branchProbability: Property = Property(name="branchProbability", type=FloatType)
pcm_av_pc_usagemodel_av_pc_BranchTransition.attributes={pcm_av_pc_usagemodel_av_pc_BranchTransition_branchProbability}

# Branch class attributes and methods

# pcm_av_pc_usagemodel_av_pc_Branch class attributes and methods
pcm_av_pc_usagemodel_av_pc_Branch_m_AllBranchProbabilitiesMustSumUpTo1: Method = Method(name="AllBranchProbabilitiesMustSumUpTo1", parameters={Parameter(name='pcm_av_pc_diagnostics', type=StringType), Parameter(name='pcm_av_pc_context', type=StringType)}, type=BooleanType)
pcm_av_pc_usagemodel_av_pc_Branch.methods={pcm_av_pc_usagemodel_av_pc_Branch_m_AllBranchProbabilitiesMustSumUpTo1}

# pcm_av_pc_usagemodel_av_pc_Loop class attributes and methods

# pcm_av_pc_usagemodel_av_pc_Stop class attributes and methods
pcm_av_pc_usagemodel_av_pc_Stop_m_StopHasNoSuccessor: Method = Method(name="StopHasNoSuccessor", parameters={Parameter(name='pcm_av_pc_context', type=StringType), Parameter(name='pcm_av_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_pc_usagemodel_av_pc_Stop.methods={pcm_av_pc_usagemodel_av_pc_Stop_m_StopHasNoSuccessor}

# BasicComponent class attributes and methods

# ResourceTimeoutFailureType class attributes and methods

# pcm_av_pc_repository_av_pc_BasicComponent class attributes and methods
pcm_av_pc_repository_av_pc_BasicComponent_m_NoSeffTypeUsedTwice: Method = Method(name="NoSeffTypeUsedTwice", parameters={Parameter(name='pcm_av_pc_diagnostics', type=StringType), Parameter(name='pcm_av_pc_context', type=StringType)}, type=BooleanType)
pcm_av_pc_repository_av_pc_BasicComponent_m_ProvideSameInterfacesAsImplementationType: Method = Method(name="ProvideSameInterfacesAsImplementationType", parameters={Parameter(name='pcm_av_pc_diagnostics', type=StringType), Parameter(name='pcm_av_pc_context', type=StringType)}, type=BooleanType)
pcm_av_pc_repository_av_pc_BasicComponent_m_RequireSameInterfacesAsImplementationType: Method = Method(name="RequireSameInterfacesAsImplementationType", parameters={Parameter(name='pcm_av_pc_diagnostics', type=StringType), Parameter(name='pcm_av_pc_context', type=StringType)}, type=BooleanType)
pcm_av_pc_repository_av_pc_BasicComponent.methods={pcm_av_pc_repository_av_pc_BasicComponent_m_ProvideSameInterfacesAsImplementationType, pcm_av_pc_repository_av_pc_BasicComponent_m_NoSeffTypeUsedTwice, pcm_av_pc_repository_av_pc_BasicComponent_m_RequireSameInterfacesAsImplementationType}

# ImplementationComponentType class attributes and methods

# pcm_av_pc_usagemodel_av_pc_OpenWorkload class attributes and methods
pcm_av_pc_usagemodel_av_pc_OpenWorkload_m_InterArrivalTimeInOpenWorkloadNeedsToBeSpecified: Method = Method(name="InterArrivalTimeInOpenWorkloadNeedsToBeSpecified", parameters={Parameter(name='pcm_av_pc_diagnostics', type=StringType), Parameter(name='pcm_av_pc_context', type=StringType)}, type=BooleanType)
pcm_av_pc_usagemodel_av_pc_OpenWorkload.methods={pcm_av_pc_usagemodel_av_pc_OpenWorkload_m_InterArrivalTimeInOpenWorkloadNeedsToBeSpecified}

# pcm_av_pc_usagemodel_av_pc_Delay class attributes and methods

# pcm_av_pc_usagemodel_av_pc_ClosedWorkload class attributes and methods
pcm_av_pc_usagemodel_av_pc_ClosedWorkload_population: Property = Property(name="population", type=IntegerType)
pcm_av_pc_usagemodel_av_pc_ClosedWorkload_m_PopulationInClosedWorkloadNeedsToBeSpecified: Method = Method(name="PopulationInClosedWorkloadNeedsToBeSpecified", parameters={Parameter(name='pcm_av_pc_diagnostics', type=StringType), Parameter(name='pcm_av_pc_context', type=StringType)}, type=BooleanType)
pcm_av_pc_usagemodel_av_pc_ClosedWorkload_m_ThinkTimeInClosedWorkloadNeedsToBeSpecified: Method = Method(name="ThinkTimeInClosedWorkloadNeedsToBeSpecified", parameters={Parameter(name='pcm_av_pc_context', type=StringType), Parameter(name='pcm_av_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_pc_usagemodel_av_pc_ClosedWorkload.attributes={pcm_av_pc_usagemodel_av_pc_ClosedWorkload_population}
pcm_av_pc_usagemodel_av_pc_ClosedWorkload.methods={pcm_av_pc_usagemodel_av_pc_ClosedWorkload_m_ThinkTimeInClosedWorkloadNeedsToBeSpecified, pcm_av_pc_usagemodel_av_pc_ClosedWorkload_m_PopulationInClosedWorkloadNeedsToBeSpecified}

# pcm_av_pc_repository_av_pc_PassiveResource class attributes and methods

# ServiceEffectSpecification class attributes and methods

# pcm_av_pc_repository_av_pc_RepositoryComponent class attributes and methods

# InterfaceProvidingRequiringEntity class attributes and methods

# Repository class attributes and methods

# pcm_av_pc_repository_av_pc_ProvidedRole class attributes and methods

# pcm_av_pc_repository_av_pc_ImplementationComponentType class attributes and methods
pcm_av_pc_repository_av_pc_ImplementationComponentType_componentType: Property = Property(name="componentType", type=StringType)
pcm_av_pc_repository_av_pc_ImplementationComponentType_m_RequiredInterfacesHaveToConformToCompleteType: Method = Method(name="RequiredInterfacesHaveToConformToCompleteType", parameters={Parameter(name='pcm_av_pc_context', type=StringType), Parameter(name='pcm_av_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_pc_repository_av_pc_ImplementationComponentType_m_providedInterfacesHaveToConformToCompleteType: Method = Method(name="providedInterfacesHaveToConformToCompleteType", parameters={Parameter(name='pcm_av_pc_diagnostics', type=StringType), Parameter(name='pcm_av_pc_context', type=StringType)}, type=BooleanType)
pcm_av_pc_repository_av_pc_ImplementationComponentType_m_ProvidedInterfaceHaveToConformToComponentType: Method = Method(name="ProvidedInterfaceHaveToConformToComponentType", parameters={Parameter(name='pcm_av_pc_context', type=StringType), Parameter(name='pcm_av_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_pc_repository_av_pc_ImplementationComponentType.attributes={pcm_av_pc_repository_av_pc_ImplementationComponentType_componentType}
pcm_av_pc_repository_av_pc_ImplementationComponentType.methods={pcm_av_pc_repository_av_pc_ImplementationComponentType_m_ProvidedInterfaceHaveToConformToComponentType, pcm_av_pc_repository_av_pc_ImplementationComponentType_m_providedInterfacesHaveToConformToCompleteType, pcm_av_pc_repository_av_pc_ImplementationComponentType_m_RequiredInterfacesHaveToConformToCompleteType}

# CompleteComponentType class attributes and methods

# FailureType class attributes and methods

# pcm_av_pc_repository_av_pc_Interface class attributes and methods
pcm_av_pc_repository_av_pc_Interface_m_NoProtocolTypeIDUsedTwice: Method = Method(name="NoProtocolTypeIDUsedTwice", parameters={Parameter(name='pcm_av_pc_diagnostics', type=StringType), Parameter(name='pcm_av_pc_context', type=StringType)}, type=BooleanType)
pcm_av_pc_repository_av_pc_Interface.methods={pcm_av_pc_repository_av_pc_Interface_m_NoProtocolTypeIDUsedTwice}

# pcm_av_pc_repository_av_pc_Parameter class attributes and methods
pcm_av_pc_repository_av_pc_Parameter_parameterName: Property = Property(name="parameterName", type=StringType)
pcm_av_pc_repository_av_pc_Parameter_modifier__Parameter: Property = Property(name="modifier__Parameter", type=StringType)
pcm_av_pc_repository_av_pc_Parameter.attributes={pcm_av_pc_repository_av_pc_Parameter_parameterName, pcm_av_pc_repository_av_pc_Parameter_modifier__Parameter}

# DataType class attributes and methods

# InfrastructureSignature class attributes and methods

# EventType class attributes and methods

# ResourceSignature class attributes and methods

# pcm_av_pc_repository_av_pc_DataType class attributes and methods

# pcm_av_pc_repository_av_pc_Repository class attributes and methods
pcm_av_pc_repository_av_pc_Repository_repositoryDescription: Property = Property(name="repositoryDescription", type=StringType)
pcm_av_pc_repository_av_pc_Repository.attributes={pcm_av_pc_repository_av_pc_Repository_repositoryDescription}

# Interface class attributes and methods

# pcm_av_pc_repository_av_pc_ExceptionType class attributes and methods
pcm_av_pc_repository_av_pc_ExceptionType_exceptionName: Property = Property(name="exceptionName", type=StringType)
pcm_av_pc_repository_av_pc_ExceptionType_exceptionMessage: Property = Property(name="exceptionMessage", type=StringType)
pcm_av_pc_repository_av_pc_ExceptionType.attributes={pcm_av_pc_repository_av_pc_ExceptionType_exceptionName, pcm_av_pc_repository_av_pc_ExceptionType_exceptionMessage}

# Protocol class attributes and methods

# RequiredCharacterisation class attributes and methods

# pcm_av_pc_repository_av_pc_RequiredCharacterisation class attributes and methods
pcm_av_pc_repository_av_pc_RequiredCharacterisation_type: Property = Property(name="type", type=StringType)
pcm_av_pc_repository_av_pc_RequiredCharacterisation.attributes={pcm_av_pc_repository_av_pc_RequiredCharacterisation_type}

# Parameter class attributes and methods

# pcm_av_pc_repository_av_pc_EventGroup class attributes and methods

# pcm_av_pc_repository_av_pc_EventType class attributes and methods

# Signature class attributes and methods

# pcm_av_pc_repository_av_pc_Signature class attributes and methods

# ExceptionType class attributes and methods

# pcm_av_pc_repository_av_pc_OperationInterface class attributes and methods
pcm_av_pc_repository_av_pc_OperationInterface_m_SignaturesHaveToBeUniqueForAnInterface: Method = Method(name="SignaturesHaveToBeUniqueForAnInterface", parameters={Parameter(name='pcm_av_pc_diagnostics', type=StringType), Parameter(name='pcm_av_pc_context', type=StringType)}, type=BooleanType)
pcm_av_pc_repository_av_pc_OperationInterface.methods={pcm_av_pc_repository_av_pc_OperationInterface_m_SignaturesHaveToBeUniqueForAnInterface}

# pcm_av_pc_repository_av_pc_InfrastructureSignature class attributes and methods

# InfrastructureInterface class attributes and methods

# pcm_av_pc_repository_av_pc_InfrastructureInterface class attributes and methods

# pcm_av_pc_repository_av_pc_InfrastructureRequiredRole class attributes and methods

# pcm_av_pc_repository_av_pc_RequiredRole class attributes and methods

# pcm_av_pc_repository_av_pc_OperationSignature class attributes and methods
pcm_av_pc_repository_av_pc_OperationSignature_m_ParameterNamesHaveToBeUniqueForASignature: Method = Method(name="ParameterNamesHaveToBeUniqueForASignature", parameters={Parameter(name='pcm_av_pc_context', type=StringType), Parameter(name='pcm_av_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_pc_repository_av_pc_OperationSignature.methods={pcm_av_pc_repository_av_pc_OperationSignature_m_ParameterNamesHaveToBeUniqueForASignature}

# OperationInterface class attributes and methods

# pcm_av_pc_repository_av_pc_OperationRequiredRole class attributes and methods

# pcm_av_pc_repository_av_pc_SourceRole class attributes and methods

# pcm_av_pc_repository_av_pc_SinkRole class attributes and methods

# pcm_av_pc_repository_av_pc_OperationProvidedRole class attributes and methods

# pcm_av_pc_repository_av_pc_InfrastructureProvidedRole class attributes and methods

# pcm_av_pc_repository_av_pc_CompositeComponent class attributes and methods
pcm_av_pc_repository_av_pc_CompositeComponent_m_ProvideSameInterfaces: Method = Method(name="ProvideSameInterfaces", parameters={Parameter(name='pcm_av_pc_context', type=StringType), Parameter(name='pcm_av_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_pc_repository_av_pc_CompositeComponent_m_RequireSameInterfaces: Method = Method(name="RequireSameInterfaces", parameters={Parameter(name='pcm_av_pc_diagnostics', type=StringType), Parameter(name='pcm_av_pc_context', type=StringType)}, type=BooleanType)
pcm_av_pc_repository_av_pc_CompositeComponent.methods={pcm_av_pc_repository_av_pc_CompositeComponent_m_RequireSameInterfaces, pcm_av_pc_repository_av_pc_CompositeComponent_m_ProvideSameInterfaces}

# entity_av_pc_ComposedProvidingRequiringEntity class attributes and methods

# repository_av_pc_ImplementationComponentType class attributes and methods

# pcm_av_pc_repository_av_pc_CompleteComponentType class attributes and methods
pcm_av_pc_repository_av_pc_CompleteComponentType_m_AtLeastOneInterfaceHasToBeProvidedOrRequiredByAUsefullCompleteComponentType: Method = Method(name="AtLeastOneInterfaceHasToBeProvidedOrRequiredByAUsefullCompleteComponentType", parameters={Parameter(name='pcm_av_pc_diagnostics', type=StringType), Parameter(name='pcm_av_pc_context', type=StringType)}, type=BooleanType)
pcm_av_pc_repository_av_pc_CompleteComponentType_m_providedInterfacesHaveToConformToProvidedType2: Method = Method(name="providedInterfacesHaveToConformToProvidedType2", parameters={Parameter(name='pcm_av_pc_context', type=StringType), Parameter(name='pcm_av_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_pc_repository_av_pc_CompleteComponentType.methods={pcm_av_pc_repository_av_pc_CompleteComponentType_m_providedInterfacesHaveToConformToProvidedType2, pcm_av_pc_repository_av_pc_CompleteComponentType_m_AtLeastOneInterfaceHasToBeProvidedOrRequiredByAUsefullCompleteComponentType}

# ProvidesComponentType class attributes and methods

# pcm_av_pc_repository_av_pc_ProvidesComponentType class attributes and methods
pcm_av_pc_repository_av_pc_ProvidesComponentType_m_AtLeastOneInterfaceHasToBeProvidedByAUsefullProvidesComponentType: Method = Method(name="AtLeastOneInterfaceHasToBeProvidedByAUsefullProvidesComponentType", parameters={Parameter(name='pcm_av_pc_diagnostics', type=StringType), Parameter(name='pcm_av_pc_context', type=StringType)}, type=BooleanType)
pcm_av_pc_repository_av_pc_ProvidesComponentType.methods={pcm_av_pc_repository_av_pc_ProvidesComponentType_m_AtLeastOneInterfaceHasToBeProvidedByAUsefullProvidesComponentType}

# pcm_av_pc_repository_av_pc_Role class attributes and methods

# pcm_av_pc_resourcetype_av_pc_ResourceSignature class attributes and methods
pcm_av_pc_resourcetype_av_pc_ResourceSignature_resourceServiceId: Property = Property(name="resourceServiceId", type=IntegerType)
pcm_av_pc_resourcetype_av_pc_ResourceSignature.attributes={pcm_av_pc_resourcetype_av_pc_ResourceSignature_resourceServiceId}

# pcm_av_pc_repository_av_pc_PrimitiveDataType class attributes and methods
pcm_av_pc_repository_av_pc_PrimitiveDataType_type: Property = Property(name="type", type=StringType)
pcm_av_pc_repository_av_pc_PrimitiveDataType.attributes={pcm_av_pc_repository_av_pc_PrimitiveDataType_type}

# pcm_av_pc_repository_av_pc_CollectionDataType class attributes and methods

# repository_av_pc_DataType class attributes and methods

# pcm_av_pc_repository_av_pc_CompositeDataType class attributes and methods

# CompositeDataType class attributes and methods

# InnerDeclaration class attributes and methods

# pcm_av_pc_repository_av_pc_InnerDeclaration class attributes and methods

# NamedElement class attributes and methods

# pcm_av_pc_protocol_av_pc_Protocol class attributes and methods
pcm_av_pc_protocol_av_pc_Protocol_protocolTypeID: Property = Property(name="protocolTypeID", type=StringType)
pcm_av_pc_protocol_av_pc_Protocol.attributes={pcm_av_pc_protocol_av_pc_Protocol_protocolTypeID}

# pcm_av_pc_resourcetype_av_pc_ProcessingResourceType class attributes and methods

# ResourceType class attributes and methods

# HardwareInducedFailureType class attributes and methods

# pcm_av_pc_resourcetype_av_pc_ResourceType class attributes and methods

# UnitCarryingElement class attributes and methods

# ResourceRepository class attributes and methods

# pcm_av_pc_resourcetype_av_pc_ResourceRepository class attributes and methods

# SchedulingPolicy class attributes and methods

# pcm_av_pc_resourcetype_av_pc_SchedulingPolicy class attributes and methods

# pcm_av_pc_resourcetype_av_pc_CommunicationLinkResourceType class attributes and methods

# NetworkInducedFailureType class attributes and methods

# pcm_av_pc_resourcetype_av_pc_ResourceInterface class attributes and methods

# pcm_av_pc_parameter_av_pc_VariableUsage class attributes and methods

# CallAction class attributes and methods

# SynchronisationPoint class attributes and methods

# CallReturnAction class attributes and methods

# SetVariableAction class attributes and methods

# SpecifiedOutputParameterAbstraction class attributes and methods

# EntryLevelSystemCall class attributes and methods

# parameter_av_pc_pcm_av_pc_AbstractNamedReference class attributes and methods

# pcm_av_pc_parameter_av_pc_VariableCharacterisation class attributes and methods
pcm_av_pc_parameter_av_pc_VariableCharacterisation_type: Property = Property(name="type", type=StringType)
pcm_av_pc_parameter_av_pc_VariableCharacterisation.attributes={pcm_av_pc_parameter_av_pc_VariableCharacterisation_type}

# pcm_av_pc_parameter_av_pc_CharacterisedVariable class attributes and methods
pcm_av_pc_parameter_av_pc_CharacterisedVariable_characterisationType: Property = Property(name="characterisationType", type=StringType)
pcm_av_pc_parameter_av_pc_CharacterisedVariable.attributes={pcm_av_pc_parameter_av_pc_CharacterisedVariable_characterisationType}

# Variable class attributes and methods

# CommunicationLinkResourceType class attributes and methods

# pcm_av_pc_reliability_av_pc_ExternalFailureOccurrenceDescription class attributes and methods
pcm_av_pc_reliability_av_pc_ExternalFailureOccurrenceDescription_m_NoResourceTimeoutFailureAllowedForExternalFailureOccurrenceDescription: Method = Method(name="NoResourceTimeoutFailureAllowedForExternalFailureOccurrenceDescription", parameters={Parameter(name='pcm_av_pc_diagnostics', type=StringType), Parameter(name='pcm_av_pc_context', type=StringType)}, type=BooleanType)
pcm_av_pc_reliability_av_pc_ExternalFailureOccurrenceDescription.methods={pcm_av_pc_reliability_av_pc_ExternalFailureOccurrenceDescription_m_NoResourceTimeoutFailureAllowedForExternalFailureOccurrenceDescription}

# pcm_av_pc_reliability_av_pc_FailureOccurrenceDescription class attributes and methods
pcm_av_pc_reliability_av_pc_FailureOccurrenceDescription_failureProbability: Property = Property(name="failureProbability", type=FloatType)
pcm_av_pc_reliability_av_pc_FailureOccurrenceDescription_m_EnsureValidFailureProbabilityRange: Method = Method(name="EnsureValidFailureProbabilityRange", parameters={Parameter(name='pcm_av_pc_context', type=StringType), Parameter(name='pcm_av_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_pc_reliability_av_pc_FailureOccurrenceDescription.attributes={pcm_av_pc_reliability_av_pc_FailureOccurrenceDescription_failureProbability}
pcm_av_pc_reliability_av_pc_FailureOccurrenceDescription.methods={pcm_av_pc_reliability_av_pc_FailureOccurrenceDescription_m_EnsureValidFailureProbabilityRange}

# pcm_av_pc_reliability_av_pc_HardwareInducedFailureType class attributes and methods
pcm_av_pc_reliability_av_pc_HardwareInducedFailureType_m_HardwareInducedFailureTypeHasProcessingResourceType: Method = Method(name="HardwareInducedFailureTypeHasProcessingResourceType", parameters={Parameter(name='pcm_av_pc_context', type=StringType), Parameter(name='pcm_av_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_pc_reliability_av_pc_HardwareInducedFailureType.methods={pcm_av_pc_reliability_av_pc_HardwareInducedFailureType_m_HardwareInducedFailureTypeHasProcessingResourceType}

# ProcessingResourceType class attributes and methods

# pcm_av_pc_reliability_av_pc_SoftwareInducedFailureType class attributes and methods

# InternalFailureOccurrenceDescription class attributes and methods

# pcm_av_pc_reliability_av_pc_InternalFailureOccurrenceDescription class attributes and methods
pcm_av_pc_reliability_av_pc_InternalFailureOccurrenceDescription_m_NoResourceTimeoutFailureAllowedForInternalFailureOccurrenceDescription: Method = Method(name="NoResourceTimeoutFailureAllowedForInternalFailureOccurrenceDescription", parameters={Parameter(name='pcm_av_pc_context', type=StringType), Parameter(name='pcm_av_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_pc_reliability_av_pc_InternalFailureOccurrenceDescription.methods={pcm_av_pc_reliability_av_pc_InternalFailureOccurrenceDescription_m_NoResourceTimeoutFailureAllowedForInternalFailureOccurrenceDescription}

# FailureOccurrenceDescription class attributes and methods

# InternalAction class attributes and methods

# SoftwareInducedFailureType class attributes and methods

# pcm_av_pc_reliability_av_pc_NetworkInducedFailureType class attributes and methods
pcm_av_pc_reliability_av_pc_NetworkInducedFailureType_m_NetworkInducedFailureTypeHasCommunicationLinkResourceType: Method = Method(name="NetworkInducedFailureTypeHasCommunicationLinkResourceType", parameters={Parameter(name='pcm_av_pc_diagnostics', type=StringType), Parameter(name='pcm_av_pc_context', type=StringType)}, type=BooleanType)
pcm_av_pc_reliability_av_pc_NetworkInducedFailureType.methods={pcm_av_pc_reliability_av_pc_NetworkInducedFailureType_m_NetworkInducedFailureTypeHasCommunicationLinkResourceType}

# pcm_av_pc_seff_av_pc_AbstractInternalControlFlowAction class attributes and methods

# AbstractAction class attributes and methods

# pcm_av_pc_seff_av_pc_AbstractAction class attributes and methods

# qos_reliability_av_pc_SpecifiedReliabilityAnnotation class attributes and methods

# pcm_av_pc_reliability_av_pc_ResourceTimeoutFailureType class attributes and methods

# pcm_av_pc_reliability_av_pc_FailureType class attributes and methods

# pcm_av_pc_seff_av_pc_StopAction class attributes and methods
pcm_av_pc_seff_av_pc_StopAction_m_StopActionSuccessorMustNotBeDefined: Method = Method(name="StopActionSuccessorMustNotBeDefined", parameters={Parameter(name='pcm_av_pc_context', type=StringType), Parameter(name='pcm_av_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_pc_seff_av_pc_StopAction.methods={pcm_av_pc_seff_av_pc_StopAction_m_StopActionSuccessorMustNotBeDefined}

# AbstractInternalControlFlowAction class attributes and methods

# pcm_av_pc_seff_av_pc_AbstractBranchTransition class attributes and methods

# BranchAction class attributes and methods

# pcm_av_pc_seff_av_pc_BranchAction class attributes and methods
pcm_av_pc_seff_av_pc_BranchAction_m_EitherGuardedBranchesOrProbabilisiticBranchTransitions: Method = Method(name="EitherGuardedBranchesOrProbabilisiticBranchTransitions", parameters={Parameter(name='pcm_av_pc_diagnostics', type=StringType), Parameter(name='pcm_av_pc_context', type=StringType)}, type=BooleanType)
pcm_av_pc_seff_av_pc_BranchAction_m_AllProbabilisticBranchProbabilitiesMustSumUpTo1: Method = Method(name="AllProbabilisticBranchProbabilitiesMustSumUpTo1", parameters={Parameter(name='pcm_av_pc_diagnostics', type=StringType), Parameter(name='pcm_av_pc_context', type=StringType)}, type=BooleanType)
pcm_av_pc_seff_av_pc_BranchAction.methods={pcm_av_pc_seff_av_pc_BranchAction_m_AllProbabilisticBranchProbabilitiesMustSumUpTo1, pcm_av_pc_seff_av_pc_BranchAction_m_EitherGuardedBranchesOrProbabilisiticBranchTransitions}

# ResourceDemandingBehaviour class attributes and methods

# pcm_av_pc_seff_av_pc_ResourceDemandingBehaviour class attributes and methods
pcm_av_pc_seff_av_pc_ResourceDemandingBehaviour_m_ExactlyOneStopAction: Method = Method(name="ExactlyOneStopAction", parameters={Parameter(name='pcm_av_pc_context', type=StringType), Parameter(name='pcm_av_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_pc_seff_av_pc_ResourceDemandingBehaviour_m_ExactlyOneStartAction: Method = Method(name="ExactlyOneStartAction", parameters={Parameter(name='pcm_av_pc_context', type=StringType), Parameter(name='pcm_av_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_pc_seff_av_pc_ResourceDemandingBehaviour_m_EachActionExceptStartActionandStopActionMustHhaveAPredecessorAndSuccessor: Method = Method(name="EachActionExceptStartActionandStopActionMustHhaveAPredecessorAndSuccessor", parameters={Parameter(name='pcm_av_pc_context', type=StringType), Parameter(name='pcm_av_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_pc_seff_av_pc_ResourceDemandingBehaviour.methods={pcm_av_pc_seff_av_pc_ResourceDemandingBehaviour_m_ExactlyOneStartAction, pcm_av_pc_seff_av_pc_ResourceDemandingBehaviour_m_ExactlyOneStopAction, pcm_av_pc_seff_av_pc_ResourceDemandingBehaviour_m_EachActionExceptStartActionandStopActionMustHhaveAPredecessorAndSuccessor}

# AbstractLoopAction class attributes and methods

# AbstractBranchTransition class attributes and methods

# pcm_av_pc_seff_av_pc_AbstractLoopAction class attributes and methods

# pcm_av_pc_seff_av_pc_ResourceDemandingSEFF class attributes and methods

# seff_av_pc_ServiceEffectSpecification class attributes and methods

# seff_av_pc_ResourceDemandingBehaviour class attributes and methods

# pcm_av_pc_seff_av_pc_CallAction class attributes and methods

# pcm_av_pc_seff_av_pc_StartAction class attributes and methods
pcm_av_pc_seff_av_pc_StartAction_m_StartActionPredecessorMustNotBeDefined: Method = Method(name="StartActionPredecessorMustNotBeDefined", parameters={Parameter(name='pcm_av_pc_diagnostics', type=StringType), Parameter(name='pcm_av_pc_context', type=StringType)}, type=BooleanType)
pcm_av_pc_seff_av_pc_StartAction.methods={pcm_av_pc_seff_av_pc_StartAction_m_StartActionPredecessorMustNotBeDefined}

# pcm_av_pc_seff_av_pc_ServiceEffectSpecification class attributes and methods
pcm_av_pc_seff_av_pc_ServiceEffectSpecification_seffTypeID: Property = Property(name="seffTypeID", type=StringType)
pcm_av_pc_seff_av_pc_ServiceEffectSpecification_m_ReferencedSignatureMustBelongToInterfaceReferencedByProvidedRole: Method = Method(name="ReferencedSignatureMustBelongToInterfaceReferencedByProvidedRole", parameters={Parameter(name='pcm_av_pc_diagnostics', type=StringType), Parameter(name='pcm_av_pc_context', type=StringType)}, type=BooleanType)
pcm_av_pc_seff_av_pc_ServiceEffectSpecification.attributes={pcm_av_pc_seff_av_pc_ServiceEffectSpecification_seffTypeID}
pcm_av_pc_seff_av_pc_ServiceEffectSpecification.methods={pcm_av_pc_seff_av_pc_ServiceEffectSpecification_m_ReferencedSignatureMustBelongToInterfaceReferencedByProvidedRole}

# pcm_av_pc_seff_av_pc_ExternalCallAction class attributes and methods
pcm_av_pc_seff_av_pc_ExternalCallAction_retryCount: Property = Property(name="retryCount", type=IntegerType)
pcm_av_pc_seff_av_pc_ExternalCallAction_m_SignatureBelongsToRole: Method = Method(name="SignatureBelongsToRole", parameters={Parameter(name='pcm_av_pc_context', type=StringType), Parameter(name='pcm_av_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_pc_seff_av_pc_ExternalCallAction_m_OperationRequiredRoleMustBeReferencedByContainer: Method = Method(name="OperationRequiredRoleMustBeReferencedByContainer", parameters={Parameter(name='pcm_av_pc_context', type=StringType), Parameter(name='pcm_av_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_pc_seff_av_pc_ExternalCallAction.attributes={pcm_av_pc_seff_av_pc_ExternalCallAction_retryCount}
pcm_av_pc_seff_av_pc_ExternalCallAction.methods={pcm_av_pc_seff_av_pc_ExternalCallAction_m_SignatureBelongsToRole, pcm_av_pc_seff_av_pc_ExternalCallAction_m_OperationRequiredRoleMustBeReferencedByContainer}

# seff_av_pc_AbstractAction class attributes and methods

# seff_av_pc_CallReturnAction class attributes and methods

# seff_reliability_av_pc_FailureHandlingEntity class attributes and methods

# ResourceDemandingInternalBehaviour class attributes and methods

# pcm_av_pc_seff_av_pc_ResourceDemandingInternalBehaviour class attributes and methods

# ResourceDemandingSEFF class attributes and methods

# pcm_av_pc_seff_av_pc_ReleaseAction class attributes and methods

# pcm_av_pc_seff_av_pc_LoopAction class attributes and methods

# pcm_av_pc_seff_av_pc_ForkAction class attributes and methods

# ForkedBehaviour class attributes and methods

# pcm_av_pc_seff_av_pc_ForkedBehaviour class attributes and methods

# ForkAction class attributes and methods

# pcm_av_pc_seff_av_pc_SynchronisationPoint class attributes and methods

# pcm_av_pc_seff_av_pc_CollectionIteratorAction class attributes and methods

# pcm_av_pc_seff_av_pc_GuardedBranchTransition class attributes and methods

# pcm_av_pc_seff_av_pc_SetVariableAction class attributes and methods

# pcm_av_pc_seff_av_pc_CallReturnAction class attributes and methods

# pcm_av_pc_seff_av_pc_ProbabilisticBranchTransition class attributes and methods
pcm_av_pc_seff_av_pc_ProbabilisticBranchTransition_branchProbability: Property = Property(name="branchProbability", type=FloatType)
pcm_av_pc_seff_av_pc_ProbabilisticBranchTransition.attributes={pcm_av_pc_seff_av_pc_ProbabilisticBranchTransition_branchProbability}

# pcm_av_pc_seff_av_pc_AcquireAction class attributes and methods
pcm_av_pc_seff_av_pc_AcquireAction_timeout: Property = Property(name="timeout", type=BooleanType)
pcm_av_pc_seff_av_pc_AcquireAction_timeoutValue: Property = Property(name="timeoutValue", type=FloatType)
pcm_av_pc_seff_av_pc_AcquireAction_m_TimeoutValueOfAcquireActionMustNotBeNegative: Method = Method(name="TimeoutValueOfAcquireActionMustNotBeNegative", parameters={Parameter(name='pcm_av_pc_context', type=StringType), Parameter(name='pcm_av_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_pc_seff_av_pc_AcquireAction.attributes={pcm_av_pc_seff_av_pc_AcquireAction_timeoutValue, pcm_av_pc_seff_av_pc_AcquireAction_timeout}
pcm_av_pc_seff_av_pc_AcquireAction.methods={pcm_av_pc_seff_av_pc_AcquireAction_m_TimeoutValueOfAcquireActionMustNotBeNegative}

# pcm_av_pc_seff_performance_av_pc_InfrastructureCall class attributes and methods
pcm_av_pc_seff_performance_av_pc_InfrastructureCall_m_SignatureMustBelongToUsedRequiredRole: Method = Method(name="SignatureMustBelongToUsedRequiredRole", parameters={Parameter(name='pcm_av_pc_diagnostics', type=StringType), Parameter(name='pcm_av_pc_context', type=StringType)}, type=BooleanType)
pcm_av_pc_seff_performance_av_pc_InfrastructureCall_m_ReferencedRequiredRoleMustBeRequiredByComponent: Method = Method(name="ReferencedRequiredRoleMustBeRequiredByComponent", parameters={Parameter(name='pcm_av_pc_context', type=StringType), Parameter(name='pcm_av_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_pc_seff_performance_av_pc_InfrastructureCall_m_SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction: Method = Method(name="SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction", parameters={Parameter(name='pcm_av_pc_diagnostics', type=StringType), Parameter(name='pcm_av_pc_context', type=StringType)}, type=BooleanType)
pcm_av_pc_seff_performance_av_pc_InfrastructureCall.methods={pcm_av_pc_seff_performance_av_pc_InfrastructureCall_m_SignatureMustBelongToUsedRequiredRole, pcm_av_pc_seff_performance_av_pc_InfrastructureCall_m_ReferencedRequiredRoleMustBeRequiredByComponent, pcm_av_pc_seff_performance_av_pc_InfrastructureCall_m_SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction}

# pcm_av_pc_seff_av_pc_InternalCallAction class attributes and methods

# seff_av_pc_CallAction class attributes and methods

# seff_av_pc_AbstractInternalControlFlowAction class attributes and methods

# pcm_av_pc_seff_av_pc_EmitEventAction class attributes and methods

# pcm_av_pc_seff_av_pc_InternalAction class attributes and methods
pcm_av_pc_seff_av_pc_InternalAction_m_MultipleInternalOccurrenceDescriptionsPerFailureTypeNotAllowed: Method = Method(name="MultipleInternalOccurrenceDescriptionsPerFailureTypeNotAllowed", parameters={Parameter(name='pcm_av_pc_context', type=StringType), Parameter(name='pcm_av_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_pc_seff_av_pc_InternalAction_m_SumOfInternalActionFailureProbabilitiesMustNotExceed1: Method = Method(name="SumOfInternalActionFailureProbabilitiesMustNotExceed1", parameters={Parameter(name='pcm_av_pc_context', type=StringType), Parameter(name='pcm_av_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_pc_seff_av_pc_InternalAction.methods={pcm_av_pc_seff_av_pc_InternalAction_m_MultipleInternalOccurrenceDescriptionsPerFailureTypeNotAllowed, pcm_av_pc_seff_av_pc_InternalAction_m_SumOfInternalActionFailureProbabilitiesMustNotExceed1}

# pcm_av_pc_seff_performance_av_pc_ResourceCall class attributes and methods
pcm_av_pc_seff_performance_av_pc_ResourceCall_m_ResourceSignatureBelongsToResourceRequiredRole: Method = Method(name="ResourceSignatureBelongsToResourceRequiredRole", parameters={Parameter(name='pcm_av_pc_diagnostics', type=StringType), Parameter(name='pcm_av_pc_context', type=StringType)}, type=BooleanType)
pcm_av_pc_seff_performance_av_pc_ResourceCall_m_ResourceRequiredRoleMustBeReferencedByComponent: Method = Method(name="ResourceRequiredRoleMustBeReferencedByComponent", parameters={Parameter(name='pcm_av_pc_diagnostics', type=StringType), Parameter(name='pcm_av_pc_context', type=StringType)}, type=BooleanType)
pcm_av_pc_seff_performance_av_pc_ResourceCall_m_SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction: Method = Method(name="SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction", parameters={Parameter(name='pcm_av_pc_diagnostics', type=StringType), Parameter(name='pcm_av_pc_context', type=StringType)}, type=BooleanType)
pcm_av_pc_seff_performance_av_pc_ResourceCall.methods={pcm_av_pc_seff_performance_av_pc_ResourceCall_m_ResourceSignatureBelongsToResourceRequiredRole, pcm_av_pc_seff_performance_av_pc_ResourceCall_m_ResourceRequiredRoleMustBeReferencedByComponent, pcm_av_pc_seff_performance_av_pc_ResourceCall_m_SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction}

# pcm_av_pc_seff_performance_av_pc_ParametricResourceDemand class attributes and methods
pcm_av_pc_seff_performance_av_pc_ParametricResourceDemand_m_DemandedProcessingResourceMustBeUniqueWithinAbstractInternalControlFlowAction: Method = Method(name="DemandedProcessingResourceMustBeUniqueWithinAbstractInternalControlFlowAction", parameters={Parameter(name='pcm_av_pc_context', type=StringType), Parameter(name='pcm_av_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_pc_seff_performance_av_pc_ParametricResourceDemand.methods={pcm_av_pc_seff_performance_av_pc_ParametricResourceDemand_m_DemandedProcessingResourceMustBeUniqueWithinAbstractInternalControlFlowAction}

# pcm_av_pc_seff_reliability_av_pc_RecoveryAction class attributes and methods
pcm_av_pc_seff_reliability_av_pc_RecoveryAction_m_PrimaryBehaviourOfRecoveryActionMustBeSet: Method = Method(name="PrimaryBehaviourOfRecoveryActionMustBeSet", parameters={Parameter(name='pcm_av_pc_diagnostics', type=StringType), Parameter(name='pcm_av_pc_context', type=StringType)}, type=BooleanType)
pcm_av_pc_seff_reliability_av_pc_RecoveryAction.methods={pcm_av_pc_seff_reliability_av_pc_RecoveryAction_m_PrimaryBehaviourOfRecoveryActionMustBeSet}

# pcm_av_pc_seff_reliability_av_pc_FailureHandlingEntity class attributes and methods

# pcm_av_pc_seff_reliability_av_pc_RecoveryActionBehaviour class attributes and methods
pcm_av_pc_seff_reliability_av_pc_RecoveryActionBehaviour_m_RecoveryActionBehaviourHasOnlyOnePredecessor: Method = Method(name="RecoveryActionBehaviourHasOnlyOnePredecessor", parameters={Parameter(name='pcm_av_pc_context', type=StringType), Parameter(name='pcm_av_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_pc_seff_reliability_av_pc_RecoveryActionBehaviour_m_RecoveryActionBehaviourIsNotSuccessorOfItself: Method = Method(name="RecoveryActionBehaviourIsNotSuccessorOfItself", parameters={Parameter(name='pcm_av_pc_context', type=StringType), Parameter(name='pcm_av_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_pc_seff_reliability_av_pc_RecoveryActionBehaviour_m_SuccessorsOfRecoveryActionBehaviourHandleDisjointFailureTypes: Method = Method(name="SuccessorsOfRecoveryActionBehaviourHandleDisjointFailureTypes", parameters={Parameter(name='pcm_av_pc_context', type=StringType), Parameter(name='pcm_av_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_pc_seff_reliability_av_pc_RecoveryActionBehaviour.methods={pcm_av_pc_seff_reliability_av_pc_RecoveryActionBehaviour_m_RecoveryActionBehaviourIsNotSuccessorOfItself, pcm_av_pc_seff_reliability_av_pc_RecoveryActionBehaviour_m_RecoveryActionBehaviourHasOnlyOnePredecessor, pcm_av_pc_seff_reliability_av_pc_RecoveryActionBehaviour_m_SuccessorsOfRecoveryActionBehaviourHandleDisjointFailureTypes}

# seff_reliability_av_pc_RecoveryActionBehaviour class attributes and methods

# seff_reliability_av_pc_RecoveryAction class attributes and methods

# pcm_av_pc_qos_performance_av_pc_SystemSpecifiedExecutionTime class attributes and methods
pcm_av_pc_qos_performance_av_pc_SystemSpecifiedExecutionTime_m_SystemSpecifiedExecutionTimeMustReferenceRequiredRoleOfASystem: Method = Method(name="SystemSpecifiedExecutionTimeMustReferenceRequiredRoleOfASystem", parameters={Parameter(name='pcm_av_pc_diagnostics', type=StringType), Parameter(name='pcm_av_pc_context', type=StringType)}, type=BooleanType)
pcm_av_pc_qos_performance_av_pc_SystemSpecifiedExecutionTime.methods={pcm_av_pc_qos_performance_av_pc_SystemSpecifiedExecutionTime_m_SystemSpecifiedExecutionTimeMustReferenceRequiredRoleOfASystem}

# SpecifiedExecutionTime class attributes and methods

# pcm_av_pc_qosannotations_av_pc_SpecifiedQoSAnnotation class attributes and methods

# QoSAnnotations class attributes and methods

# pcm_av_pc_qosannotations_av_pc_QoSAnnotations class attributes and methods
pcm_av_pc_qosannotations_av_pc_QoSAnnotations_m_MultipleReliabilityAnnotationsPerExternalCallNotAllowed: Method = Method(name="MultipleReliabilityAnnotationsPerExternalCallNotAllowed", parameters={Parameter(name='pcm_av_pc_diagnostics', type=StringType), Parameter(name='pcm_av_pc_context', type=StringType)}, type=BooleanType)
pcm_av_pc_qosannotations_av_pc_QoSAnnotations.methods={pcm_av_pc_qosannotations_av_pc_QoSAnnotations_m_MultipleReliabilityAnnotationsPerExternalCallNotAllowed}

# System class attributes and methods

# SpecifiedQoSAnnotation class attributes and methods

# pcm_av_pc_qosannotations_av_pc_SpecifiedOutputParameterAbstraction class attributes and methods

# pcm_av_pc_qos_reliability_av_pc_SpecifiedReliabilityAnnotation class attributes and methods
pcm_av_pc_qos_reliability_av_pc_SpecifiedReliabilityAnnotation_m_SpecifiedReliabilityAnnotationMustReferenceRequiredRoleOfASystem: Method = Method(name="SpecifiedReliabilityAnnotationMustReferenceRequiredRoleOfASystem", parameters={Parameter(name='pcm_av_pc_context', type=StringType), Parameter(name='pcm_av_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_pc_qos_reliability_av_pc_SpecifiedReliabilityAnnotation_m_SumOfReliabilityAnnotationFailureProbabilitiesMustNotExceed1: Method = Method(name="SumOfReliabilityAnnotationFailureProbabilitiesMustNotExceed1", parameters={Parameter(name='pcm_av_pc_diagnostics', type=StringType), Parameter(name='pcm_av_pc_context', type=StringType)}, type=BooleanType)
pcm_av_pc_qos_reliability_av_pc_SpecifiedReliabilityAnnotation_m_MultipleExternalOccurrenceDescriptionsPerFailureTypeNotAllowed: Method = Method(name="MultipleExternalOccurrenceDescriptionsPerFailureTypeNotAllowed", parameters={Parameter(name='pcm_av_pc_context', type=StringType), Parameter(name='pcm_av_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_pc_qos_reliability_av_pc_SpecifiedReliabilityAnnotation.methods={pcm_av_pc_qos_reliability_av_pc_SpecifiedReliabilityAnnotation_m_SpecifiedReliabilityAnnotationMustReferenceRequiredRoleOfASystem, pcm_av_pc_qos_reliability_av_pc_SpecifiedReliabilityAnnotation_m_SumOfReliabilityAnnotationFailureProbabilitiesMustNotExceed1, pcm_av_pc_qos_reliability_av_pc_SpecifiedReliabilityAnnotation_m_MultipleExternalOccurrenceDescriptionsPerFailureTypeNotAllowed}

# pcm_av_pc_qos_performance_av_pc_SpecifiedExecutionTime class attributes and methods

# pcm_av_pc_qos_performance_av_pc_ComponentSpecifiedExecutionTime class attributes and methods

# pcm_av_pc_resourceenvironment_av_pc_ResourceEnvironment class attributes and methods

# LinkingResource class attributes and methods

# ResourceContainer class attributes and methods

# pcm_av_pc_resourceenvironment_av_pc_LinkingResource class attributes and methods

# ExternalFailureOccurrenceDescription class attributes and methods

# pcm_av_pc_system_av_pc_System class attributes and methods
pcm_av_pc_system_av_pc_System_m_SystemMustHaveAtLeastOneProvidedRole: Method = Method(name="SystemMustHaveAtLeastOneProvidedRole", parameters={Parameter(name='pcm_av_pc_context', type=StringType), Parameter(name='pcm_av_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_pc_system_av_pc_System.methods={pcm_av_pc_system_av_pc_System_m_SystemMustHaveAtLeastOneProvidedRole}

# pcm_av_pc_resourceenvironment_av_pc_CommunicationLinkResourceSpecification class attributes and methods
pcm_av_pc_resourceenvironment_av_pc_CommunicationLinkResourceSpecification_failureProbability: Property = Property(name="failureProbability", type=FloatType)
pcm_av_pc_resourceenvironment_av_pc_CommunicationLinkResourceSpecification.attributes={pcm_av_pc_resourceenvironment_av_pc_CommunicationLinkResourceSpecification_failureProbability}

# ResourceEnvironment class attributes and methods

# pcm_av_pc_resourceenvironment_av_pc_ResourceContainer class attributes and methods

# pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification class attributes and methods
pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification_numberOfReplicas: Property = Property(name="numberOfReplicas", type=IntegerType)
pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification_MTTR: Property = Property(name="MTTR", type=FloatType)
pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification_MTTF: Property = Property(name="MTTF", type=FloatType)
pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification_requiredByContainer: Property = Property(name="requiredByContainer", type=BooleanType)
pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification.attributes={pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification_MTTF, pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification_numberOfReplicas, pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification_MTTR, pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification_requiredByContainer}

# Allocation class attributes and methods

# pcm_av_pc_allocation_av_pc_Allocation class attributes and methods
pcm_av_pc_allocation_av_pc_Allocation_m_EachAssemblyContextWithinSystemHasToBeAllocatedExactlyOnce: Method = Method(name="EachAssemblyContextWithinSystemHasToBeAllocatedExactlyOnce", parameters={Parameter(name='pcm_av_pc_diagnostics', type=StringType), Parameter(name='pcm_av_pc_context', type=StringType)}, type=BooleanType)
pcm_av_pc_allocation_av_pc_Allocation_m_CommunicatingServersHaveToBeConnectedByLinkingResource: Method = Method(name="CommunicatingServersHaveToBeConnectedByLinkingResource", parameters={Parameter(name='pcm_av_pc_context', type=StringType), Parameter(name='pcm_av_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_pc_allocation_av_pc_Allocation.methods={pcm_av_pc_allocation_av_pc_Allocation_m_CommunicatingServersHaveToBeConnectedByLinkingResource, pcm_av_pc_allocation_av_pc_Allocation_m_EachAssemblyContextWithinSystemHasToBeAllocatedExactlyOnce}

# pcm_av_pc_allocation_av_pc_AllocationContext class attributes and methods
pcm_av_pc_allocation_av_pc_AllocationContext_m_OneAssemblyContextOrOneEventChannelShouldBeReferred: Method = Method(name="OneAssemblyContextOrOneEventChannelShouldBeReferred", parameters={Parameter(name='pcm_av_pc_diagnostics', type=StringType), Parameter(name='pcm_av_pc_context', type=StringType)}, type=BooleanType)
pcm_av_pc_allocation_av_pc_AllocationContext.methods={pcm_av_pc_allocation_av_pc_AllocationContext_m_OneAssemblyContextOrOneEventChannelShouldBeReferred}

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
communicationLinkResourceSpecifcation_throughput_PCMRandomVariable21: BinaryAssociation = BinaryAssociation(
    name="communicationLinkResourceSpecifcation_throughput_PCMRandomVariable21",
    ends={
        Property(name="CommunicationLinkResourceSpecification", type=pcm_av_pc_core_av_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="throughput_CommunicationLinkResourceSpecification", type=CommunicationLinkResourceSpecification, multiplicity=Multiplicity(0, 1))
    }
)
processingResourceSpecification_processingRate_PCMRandomVariable22: BinaryAssociation = BinaryAssociation(
    name="processingResourceSpecification_processingRate_PCMRandomVariable22",
    ends={
        Property(name="ProcessingResourceSpecification", type=pcm_av_pc_core_av_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="processingRate_ProcessingResourceSpecification", type=ProcessingResourceSpecification, multiplicity=Multiplicity(0, 1))
    }
)
communicationLinkResourceSpecification_latency_PCMRandomVariable23: BinaryAssociation = BinaryAssociation(
    name="communicationLinkResourceSpecification_latency_PCMRandomVariable23",
    ends={
        Property(name="CommunicationLinkResourceSpecification24", type=pcm_av_pc_core_av_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="latency_CommunicationLinkResourceSpecification", type=CommunicationLinkResourceSpecification, multiplicity=Multiplicity(0, 1))
    }
)
closedWorkload_PCMRandomVariable7: BinaryAssociation = BinaryAssociation(
    name="closedWorkload_PCMRandomVariable7",
    ends={
        Property(name="ClosedWorkload", type=pcm_av_pc_core_av_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="thinkTime_ClosedWorkload", type=ClosedWorkload, multiplicity=Multiplicity(0, 1))
    }
)
passiveResource_capacity_PCMRandomVariable8: BinaryAssociation = BinaryAssociation(
    name="passiveResource_capacity_PCMRandomVariable8",
    ends={
        Property(name="PassiveResource", type=pcm_av_pc_core_av_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="capacity_PassiveResource", type=PassiveResource, multiplicity=Multiplicity(0, 1))
    }
)
variableCharacterisation_Specification9: BinaryAssociation = BinaryAssociation(
    name="variableCharacterisation_Specification9",
    ends={
        Property(name="VariableCharacterisation", type=pcm_av_pc_core_av_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="specification_VariableCharacterisation", type=VariableCharacterisation, multiplicity=Multiplicity(0, 1))
    }
)
infrastructureCall__PCMRandomVariable10: BinaryAssociation = BinaryAssociation(
    name="infrastructureCall__PCMRandomVariable10",
    ends={
        Property(name="InfrastructureCall", type=pcm_av_pc_core_av_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="numberOfCalls__InfrastructureCall", type=seff_performance_av_pc_InfrastructureCall, multiplicity=Multiplicity(0, 1))
    }
)
resourceCall__PCMRandomVariable11: BinaryAssociation = BinaryAssociation(
    name="resourceCall__PCMRandomVariable11",
    ends={
        Property(name="ResourceCall", type=pcm_av_pc_core_av_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="numberOfCalls__ResourceCall", type=seff_performance_av_pc_ResourceCall, multiplicity=Multiplicity(0, 1))
    }
)
parametricResourceDemand_PCMRandomVariable12: BinaryAssociation = BinaryAssociation(
    name="parametricResourceDemand_PCMRandomVariable12",
    ends={
        Property(name="ParametricResourceDemand", type=pcm_av_pc_core_av_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="specification_ParametericResourceDemand", type=seff_performance_av_pc_ParametricResourceDemand, multiplicity=Multiplicity(0, 1))
    }
)
loopAction_PCMRandomVariable13: BinaryAssociation = BinaryAssociation(
    name="loopAction_PCMRandomVariable13",
    ends={
        Property(name="LoopAction", type=pcm_av_pc_core_av_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="iterationCount_LoopAction", type=LoopAction, multiplicity=Multiplicity(0, 1))
    }
)
guardedBranchTransition_PCMRandomVariable14: BinaryAssociation = BinaryAssociation(
    name="guardedBranchTransition_PCMRandomVariable14",
    ends={
        Property(name="GuardedBranchTransition", type=pcm_av_pc_core_av_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="branchCondition_GuardedBranchTransition", type=GuardedBranchTransition, multiplicity=Multiplicity(0, 1))
    }
)
specifiedExecutionTime_PCMRandomVariable15: BinaryAssociation = BinaryAssociation(
    name="specifiedExecutionTime_PCMRandomVariable15",
    ends={
        Property(name="SpecifiedExecutionTime", type=pcm_av_pc_core_av_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="specification_SpecifiedExecutionTime", type=qos_performance_av_pc_SpecifiedExecutionTime, multiplicity=Multiplicity(0, 1))
    }
)
eventChannelSinkConnector__FilterCondition16: BinaryAssociation = BinaryAssociation(
    name="eventChannelSinkConnector__FilterCondition16",
    ends={
        Property(name="EventChannelSinkConnector", type=pcm_av_pc_core_av_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="filterCondition__EventChannelSinkConnector", type=composition_av_pc_EventChannelSinkConnector, multiplicity=Multiplicity(0, 1))
    }
)
assemblyEventConnector__FilterCondition17: BinaryAssociation = BinaryAssociation(
    name="assemblyEventConnector__FilterCondition17",
    ends={
        Property(name="AssemblyEventConnector", type=pcm_av_pc_core_av_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="filterCondition__AssemblyEventConnector", type=composition_av_pc_AssemblyEventConnector, multiplicity=Multiplicity(0, 1))
    }
)
loop_LoopIteration18: BinaryAssociation = BinaryAssociation(
    name="loop_LoopIteration18",
    ends={
        Property(name="Loop", type=pcm_av_pc_core_av_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="loopIteration_Loop", type=Loop, multiplicity=Multiplicity(0, 1))
    }
)
openWorkload_PCMRandomVariable19: BinaryAssociation = BinaryAssociation(
    name="openWorkload_PCMRandomVariable19",
    ends={
        Property(name="OpenWorkload", type=pcm_av_pc_core_av_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="interArrivalTime_OpenWorkload", type=OpenWorkload, multiplicity=Multiplicity(0, 1))
    }
)
delay_TimeSpecification20: BinaryAssociation = BinaryAssociation(
    name="delay_TimeSpecification20",
    ends={
        Property(name="Delay", type=pcm_av_pc_core_av_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="timeSpecification_Delay", type=Delay, multiplicity=Multiplicity(0, 1))
    }
)
resourceInterfaceProvidingEntity__ResourceProvidedRole25: BinaryAssociation = BinaryAssociation(
    name="resourceInterfaceProvidingEntity__ResourceProvidedRole25",
    ends={
        Property(name="ResourceInterfaceProvidingEntity", type=pcm_av_pc_entity_av_pc_ResourceProvidedRole, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceProvidedRoles__ResourceInterfaceProvidingEntity", type=entity_av_pc_ResourceInterfaceProvidingEntity, multiplicity=Multiplicity(0, 1))
    }
)
providedResourceInterface__ResourceProvidedRole26: BinaryAssociation = BinaryAssociation(
    name="providedResourceInterface__ResourceProvidedRole26",
    ends={
        Property(name="ResourceInterface", type=pcm_av_pc_entity_av_pc_ResourceProvidedRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_entity_av_pc_ResourceProvidedRole", type=ResourceInterface, multiplicity=Multiplicity(0, 1))
    }
)
providedRoles_InterfaceProvidingEntity27: BinaryAssociation = BinaryAssociation(
    name="providedRoles_InterfaceProvidingEntity27",
    ends={
        Property(name="ProvidedRole", type=pcm_av_pc_entity_av_pc_InterfaceProvidingEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="providingEntity_ProvidedRole", type=ProvidedRole, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredRoles_InterfaceRequiringEntity28: BinaryAssociation = BinaryAssociation(
    name="requiredRoles_InterfaceRequiringEntity28",
    ends={
        Property(name="RequiredRole", type=pcm_av_pc_entity_av_pc_InterfaceRequiringEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="requiringEntity_RequiredRole", type=RequiredRole, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceRequiredRoles__ResourceInterfaceRequiringEntity29: BinaryAssociation = BinaryAssociation(
    name="resourceRequiredRoles__ResourceInterfaceRequiringEntity29",
    ends={
        Property(name="ResourceRequiredRole", type=pcm_av_pc_entity_av_pc_ResourceInterfaceRequiringEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceInterfaceRequiringEntity__ResourceRequiredRole", type=entity_av_pc_ResourceRequiredRole, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredResourceInterface__ResourceRequiredRole30: BinaryAssociation = BinaryAssociation(
    name="requiredResourceInterface__ResourceRequiredRole30",
    ends={
        Property(name="ResourceInterface31", type=pcm_av_pc_entity_av_pc_ResourceRequiredRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_entity_av_pc_ResourceRequiredRole", type=ResourceInterface, multiplicity=Multiplicity(0, 1))
    }
)
resourceInterfaceRequiringEntity__ResourceRequiredRole32: BinaryAssociation = BinaryAssociation(
    name="resourceInterfaceRequiringEntity__ResourceRequiredRole32",
    ends={
        Property(name="ResourceInterfaceRequiringEntity", type=pcm_av_pc_entity_av_pc_ResourceRequiredRole, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceRequiredRoles__ResourceInterfaceRequiringEntity", type=entity_av_pc_ResourceInterfaceRequiringEntity, multiplicity=Multiplicity(0, 1))
    }
)
resourceProvidedRoles__ResourceInterfaceProvidingEntity33: BinaryAssociation = BinaryAssociation(
    name="resourceProvidedRoles__ResourceInterfaceProvidingEntity33",
    ends={
        Property(name="ResourceProvidedRole", type=pcm_av_pc_entity_av_pc_ResourceInterfaceProvidingEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceInterfaceProvidingEntity__ResourceProvidedRole", type=entity_av_pc_ResourceProvidedRole, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eventGroup__EventChannel45: BinaryAssociation = BinaryAssociation(
    name="eventGroup__EventChannel45",
    ends={
        Property(name="EventGroup", type=pcm_av_pc_composition_av_pc_EventChannel, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_composition_av_pc_EventChannel", type=EventGroup, multiplicity=Multiplicity(0, 1))
    }
)
eventChannelSourceConnector__EventChannel46: BinaryAssociation = BinaryAssociation(
    name="eventChannelSourceConnector__EventChannel46",
    ends={
        Property(name="EventChannelSourceConnector", type=pcm_av_pc_composition_av_pc_EventChannel, multiplicity=Multiplicity(1, 1)),
        Property(name="eventChannel__EventChannelSourceConnector", type=composition_av_pc_EventChannelSourceConnector, multiplicity=Multiplicity(0, 9999))
    }
)
eventChannelSinkConnector__EventChannel47: BinaryAssociation = BinaryAssociation(
    name="eventChannelSinkConnector__EventChannel47",
    ends={
        Property(name="EventChannelSinkConnector48", type=pcm_av_pc_composition_av_pc_EventChannel, multiplicity=Multiplicity(1, 1)),
        Property(name="eventChannel__EventChannelSinkConnector", type=composition_av_pc_EventChannelSinkConnector, multiplicity=Multiplicity(0, 9999))
    }
)
parentStructure__EventChannel49: BinaryAssociation = BinaryAssociation(
    name="parentStructure__EventChannel49",
    ends={
        Property(name="ComposedStructure50", type=pcm_av_pc_composition_av_pc_EventChannel, multiplicity=Multiplicity(1, 1)),
        Property(name="eventChannel__ComposedStructure", type=composition_av_pc_ComposedStructure, multiplicity=Multiplicity(0, 1))
    }
)
parentStructure__Connector34: BinaryAssociation = BinaryAssociation(
    name="parentStructure__Connector34",
    ends={
        Property(name="ComposedStructure", type=pcm_av_pc_composition_av_pc_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="connectors__ComposedStructure", type=composition_av_pc_ComposedStructure, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContexts__ComposedStructure35: BinaryAssociation = BinaryAssociation(
    name="assemblyContexts__ComposedStructure35",
    ends={
        Property(name="AssemblyContext", type=pcm_av_pc_composition_av_pc_ComposedStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="parentStructure__AssemblyContext", type=composition_av_pc_AssemblyContext, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceRequiredDelegationConnectors_ComposedStructure36: BinaryAssociation = BinaryAssociation(
    name="resourceRequiredDelegationConnectors_ComposedStructure36",
    ends={
        Property(name="ResourceRequiredDelegationConnector", type=pcm_av_pc_composition_av_pc_ComposedStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="parentStructure_ResourceRequiredDelegationConnector", type=composition_av_pc_ResourceRequiredDelegationConnector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eventChannel__ComposedStructure37: BinaryAssociation = BinaryAssociation(
    name="eventChannel__ComposedStructure37",
    ends={
        Property(name="EventChannel", type=pcm_av_pc_composition_av_pc_ComposedStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="parentStructure__EventChannel", type=composition_av_pc_EventChannel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connectors__ComposedStructure38: BinaryAssociation = BinaryAssociation(
    name="connectors__ComposedStructure38",
    ends={
        Property(name="Connector", type=pcm_av_pc_composition_av_pc_ComposedStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="parentStructure__Connector", type=composition_av_pc_Connector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
innerResourceRequiredRole_ResourceRequiredDelegationConnector39: BinaryAssociation = BinaryAssociation(
    name="innerResourceRequiredRole_ResourceRequiredDelegationConnector39",
    ends={
        Property(name="entity_av_pc_ResourceRequiredRole", type=pcm_av_pc_composition_av_pc_ResourceRequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_composition_av_pc_ResourceRequiredDelegationConnector", type=entity_av_pc_ResourceRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
outerResourceRequiredRole_ResourceRequiredDelegationConnector40: BinaryAssociation = BinaryAssociation(
    name="outerResourceRequiredRole_ResourceRequiredDelegationConnector40",
    ends={
        Property(name="entity_av_pc_ResourceRequiredRole42", type=pcm_av_pc_composition_av_pc_ResourceRequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_composition_av_pc_ResourceRequiredDelegationConnector41", type=entity_av_pc_ResourceRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
parentStructure_ResourceRequiredDelegationConnector43: BinaryAssociation = BinaryAssociation(
    name="parentStructure_ResourceRequiredDelegationConnector43",
    ends={
        Property(name="ComposedStructure44", type=pcm_av_pc_composition_av_pc_ResourceRequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceRequiredDelegationConnectors_ComposedStructure", type=composition_av_pc_ComposedStructure, multiplicity=Multiplicity(0, 1))
    }
)
sourceRole__EventChannelSourceRole51: BinaryAssociation = BinaryAssociation(
    name="sourceRole__EventChannelSourceRole51",
    ends={
        Property(name="SourceRole", type=pcm_av_pc_composition_av_pc_EventChannelSourceConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_composition_av_pc_EventChannelSourceConnector", type=SourceRole, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext__EventChannelSourceConnector52: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__EventChannelSourceConnector52",
    ends={
        Property(name="composition_av_pc_AssemblyContext", type=pcm_av_pc_composition_av_pc_EventChannelSourceConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_composition_av_pc_EventChannelSourceConnector53", type=composition_av_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
eventChannel__EventChannelSourceConnector54: BinaryAssociation = BinaryAssociation(
    name="eventChannel__EventChannelSourceConnector54",
    ends={
        Property(name="EventChannel55", type=pcm_av_pc_composition_av_pc_EventChannelSourceConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="eventChannelSourceConnector__EventChannel", type=composition_av_pc_EventChannel, multiplicity=Multiplicity(0, 1))
    }
)
sinkRole__EventChannelSinkConnector56: BinaryAssociation = BinaryAssociation(
    name="sinkRole__EventChannelSinkConnector56",
    ends={
        Property(name="SinkRole", type=pcm_av_pc_composition_av_pc_EventChannelSinkConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_composition_av_pc_EventChannelSinkConnector", type=SinkRole, multiplicity=Multiplicity(0, 1))
    }
)
filterCondition__EventChannelSinkConnector57: BinaryAssociation = BinaryAssociation(
    name="filterCondition__EventChannelSinkConnector57",
    ends={
        Property(name="PCMRandomVariable", type=pcm_av_pc_composition_av_pc_EventChannelSinkConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="eventChannelSinkConnector__FilterCondition", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assemblyContext__EventChannelSinkConnector58: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__EventChannelSinkConnector58",
    ends={
        Property(name="composition_av_pc_AssemblyContext60", type=pcm_av_pc_composition_av_pc_EventChannelSinkConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_composition_av_pc_EventChannelSinkConnector59", type=composition_av_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
eventChannel__EventChannelSinkConnector61: BinaryAssociation = BinaryAssociation(
    name="eventChannel__EventChannelSinkConnector61",
    ends={
        Property(name="EventChannel62", type=pcm_av_pc_composition_av_pc_EventChannelSinkConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="eventChannelSinkConnector__EventChannel", type=composition_av_pc_EventChannel, multiplicity=Multiplicity(0, 1))
    }
)
innerProvidedRole_ProvidedDelegationConnector63: BinaryAssociation = BinaryAssociation(
    name="innerProvidedRole_ProvidedDelegationConnector63",
    ends={
        Property(name="OperationProvidedRole", type=pcm_av_pc_composition_av_pc_ProvidedDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_composition_av_pc_ProvidedDelegationConnector", type=OperationProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
outerProvidedRole_ProvidedDelegationConnector64: BinaryAssociation = BinaryAssociation(
    name="outerProvidedRole_ProvidedDelegationConnector64",
    ends={
        Property(name="OperationProvidedRole66", type=pcm_av_pc_composition_av_pc_ProvidedDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_composition_av_pc_ProvidedDelegationConnector65", type=OperationProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext_ProvidedDelegationConnector67: BinaryAssociation = BinaryAssociation(
    name="assemblyContext_ProvidedDelegationConnector67",
    ends={
        Property(name="composition_av_pc_AssemblyContext69", type=pcm_av_pc_composition_av_pc_ProvidedDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_composition_av_pc_ProvidedDelegationConnector68", type=composition_av_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
requiringAssemblyContext_AssemblyConnector77: BinaryAssociation = BinaryAssociation(
    name="requiringAssemblyContext_AssemblyConnector77",
    ends={
        Property(name="composition_av_pc_AssemblyContext78", type=pcm_av_pc_composition_av_pc_AssemblyConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_composition_av_pc_AssemblyConnector", type=composition_av_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
providingAssemblyContext_AssemblyConnector79: BinaryAssociation = BinaryAssociation(
    name="providingAssemblyContext_AssemblyConnector79",
    ends={
        Property(name="composition_av_pc_AssemblyContext81", type=pcm_av_pc_composition_av_pc_AssemblyConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_composition_av_pc_AssemblyConnector80", type=composition_av_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
providedRole_AssemblyConnector82: BinaryAssociation = BinaryAssociation(
    name="providedRole_AssemblyConnector82",
    ends={
        Property(name="OperationProvidedRole84", type=pcm_av_pc_composition_av_pc_AssemblyConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_composition_av_pc_AssemblyConnector83", type=OperationProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
requiredRole_AssemblyConnector85: BinaryAssociation = BinaryAssociation(
    name="requiredRole_AssemblyConnector85",
    ends={
        Property(name="OperationRequiredRole87", type=pcm_av_pc_composition_av_pc_AssemblyConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_composition_av_pc_AssemblyConnector86", type=OperationRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
sinkRole__AssemblyEventConnector88: BinaryAssociation = BinaryAssociation(
    name="sinkRole__AssemblyEventConnector88",
    ends={
        Property(name="SinkRole89", type=pcm_av_pc_composition_av_pc_AssemblyEventConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_composition_av_pc_AssemblyEventConnector", type=SinkRole, multiplicity=Multiplicity(0, 1))
    }
)
innerRequiredRole_RequiredDelegationConnector70: BinaryAssociation = BinaryAssociation(
    name="innerRequiredRole_RequiredDelegationConnector70",
    ends={
        Property(name="OperationRequiredRole", type=pcm_av_pc_composition_av_pc_RequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_composition_av_pc_RequiredDelegationConnector", type=OperationRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
outerRequiredRole_RequiredDelegationConnector71: BinaryAssociation = BinaryAssociation(
    name="outerRequiredRole_RequiredDelegationConnector71",
    ends={
        Property(name="OperationRequiredRole73", type=pcm_av_pc_composition_av_pc_RequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_composition_av_pc_RequiredDelegationConnector72", type=OperationRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext_RequiredDelegationConnector74: BinaryAssociation = BinaryAssociation(
    name="assemblyContext_RequiredDelegationConnector74",
    ends={
        Property(name="composition_av_pc_AssemblyContext76", type=pcm_av_pc_composition_av_pc_RequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_composition_av_pc_RequiredDelegationConnector75", type=composition_av_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
innerRequiredRole__RequiredInfrastructureDelegationConnector134: BinaryAssociation = BinaryAssociation(
    name="innerRequiredRole__RequiredInfrastructureDelegationConnector134",
    ends={
        Property(name="InfrastructureRequiredRole135", type=pcm_av_pc_composition_av_pc_RequiredInfrastructureDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_composition_av_pc_RequiredInfrastructureDelegationConnector", type=InfrastructureRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
outerRequiredRole__RequiredInfrastructureDelegationConnector136: BinaryAssociation = BinaryAssociation(
    name="outerRequiredRole__RequiredInfrastructureDelegationConnector136",
    ends={
        Property(name="InfrastructureRequiredRole138", type=pcm_av_pc_composition_av_pc_RequiredInfrastructureDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_composition_av_pc_RequiredInfrastructureDelegationConnector137", type=InfrastructureRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext__RequiredInfrastructureDelegationConnector139: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__RequiredInfrastructureDelegationConnector139",
    ends={
        Property(name="composition_av_pc_AssemblyContext141", type=pcm_av_pc_composition_av_pc_RequiredInfrastructureDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_composition_av_pc_RequiredInfrastructureDelegationConnector140", type=composition_av_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext__RequiredResourceDelegationConnector142: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__RequiredResourceDelegationConnector142",
    ends={
        Property(name="composition_av_pc_AssemblyContext143", type=pcm_av_pc_composition_av_pc_RequiredResourceDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_composition_av_pc_RequiredResourceDelegationConnector", type=composition_av_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
sourceRole__AssemblyEventConnector90: BinaryAssociation = BinaryAssociation(
    name="sourceRole__AssemblyEventConnector90",
    ends={
        Property(name="SourceRole92", type=pcm_av_pc_composition_av_pc_AssemblyEventConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_composition_av_pc_AssemblyEventConnector91", type=SourceRole, multiplicity=Multiplicity(0, 1))
    }
)
sinkAssemblyContext__AssemblyEventConnector93: BinaryAssociation = BinaryAssociation(
    name="sinkAssemblyContext__AssemblyEventConnector93",
    ends={
        Property(name="composition_av_pc_AssemblyContext95", type=pcm_av_pc_composition_av_pc_AssemblyEventConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_composition_av_pc_AssemblyEventConnector94", type=composition_av_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
sourceAssemblyContext__AssemblyEventConnector96: BinaryAssociation = BinaryAssociation(
    name="sourceAssemblyContext__AssemblyEventConnector96",
    ends={
        Property(name="composition_av_pc_AssemblyContext98", type=pcm_av_pc_composition_av_pc_AssemblyEventConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_composition_av_pc_AssemblyEventConnector97", type=composition_av_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
filterCondition__AssemblyEventConnector99: BinaryAssociation = BinaryAssociation(
    name="filterCondition__AssemblyEventConnector99",
    ends={
        Property(name="PCMRandomVariable100", type=pcm_av_pc_composition_av_pc_AssemblyEventConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="assemblyEventConnector__FilterCondition", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
innerSourceRole__SourceRole101: BinaryAssociation = BinaryAssociation(
    name="innerSourceRole__SourceRole101",
    ends={
        Property(name="SourceRole102", type=pcm_av_pc_composition_av_pc_SourceDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_composition_av_pc_SourceDelegationConnector", type=SourceRole, multiplicity=Multiplicity(0, 1))
    }
)
outerSourceRole__SourceRole103: BinaryAssociation = BinaryAssociation(
    name="outerSourceRole__SourceRole103",
    ends={
        Property(name="SourceRole105", type=pcm_av_pc_composition_av_pc_SourceDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_composition_av_pc_SourceDelegationConnector104", type=SourceRole, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext__SourceDelegationConnector106: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__SourceDelegationConnector106",
    ends={
        Property(name="composition_av_pc_AssemblyContext108", type=pcm_av_pc_composition_av_pc_SourceDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_composition_av_pc_SourceDelegationConnector107", type=composition_av_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext__SinkDelegationConnector109: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__SinkDelegationConnector109",
    ends={
        Property(name="composition_av_pc_AssemblyContext110", type=pcm_av_pc_composition_av_pc_SinkDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_composition_av_pc_SinkDelegationConnector", type=composition_av_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
innerSinkRole__SinkRole111: BinaryAssociation = BinaryAssociation(
    name="innerSinkRole__SinkRole111",
    ends={
        Property(name="SinkRole113", type=pcm_av_pc_composition_av_pc_SinkDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_composition_av_pc_SinkDelegationConnector112", type=SinkRole, multiplicity=Multiplicity(0, 1))
    }
)
outerSinkRole__SinkRole114: BinaryAssociation = BinaryAssociation(
    name="outerSinkRole__SinkRole114",
    ends={
        Property(name="SinkRole116", type=pcm_av_pc_composition_av_pc_SinkDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_composition_av_pc_SinkDelegationConnector115", type=SinkRole, multiplicity=Multiplicity(0, 1))
    }
)
providedRole__AssemblyInfrastructureConnector117: BinaryAssociation = BinaryAssociation(
    name="providedRole__AssemblyInfrastructureConnector117",
    ends={
        Property(name="InfrastructureProvidedRole", type=pcm_av_pc_composition_av_pc_AssemblyInfrastructureConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_composition_av_pc_AssemblyInfrastructureConnector", type=InfrastructureProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
requiredRole__AssemblyInfrastructureConnector118: BinaryAssociation = BinaryAssociation(
    name="requiredRole__AssemblyInfrastructureConnector118",
    ends={
        Property(name="InfrastructureRequiredRole", type=pcm_av_pc_composition_av_pc_AssemblyInfrastructureConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_composition_av_pc_AssemblyInfrastructureConnector119", type=InfrastructureRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
providingAssemblyContext__AssemblyInfrastructureConnector120: BinaryAssociation = BinaryAssociation(
    name="providingAssemblyContext__AssemblyInfrastructureConnector120",
    ends={
        Property(name="composition_av_pc_AssemblyContext122", type=pcm_av_pc_composition_av_pc_AssemblyInfrastructureConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_composition_av_pc_AssemblyInfrastructureConnector121", type=composition_av_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
requiringAssemblyContext__AssemblyInfrastructureConnector123: BinaryAssociation = BinaryAssociation(
    name="requiringAssemblyContext__AssemblyInfrastructureConnector123",
    ends={
        Property(name="composition_av_pc_AssemblyContext125", type=pcm_av_pc_composition_av_pc_AssemblyInfrastructureConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_composition_av_pc_AssemblyInfrastructureConnector124", type=composition_av_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
innerProvidedRole__ProvidedInfrastructureDelegationConnector126: BinaryAssociation = BinaryAssociation(
    name="innerProvidedRole__ProvidedInfrastructureDelegationConnector126",
    ends={
        Property(name="InfrastructureProvidedRole127", type=pcm_av_pc_composition_av_pc_ProvidedInfrastructureDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_composition_av_pc_ProvidedInfrastructureDelegationConnector", type=InfrastructureProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
outerProvidedRole__ProvidedInfrastructureDelegationConnector128: BinaryAssociation = BinaryAssociation(
    name="outerProvidedRole__ProvidedInfrastructureDelegationConnector128",
    ends={
        Property(name="InfrastructureProvidedRole130", type=pcm_av_pc_composition_av_pc_ProvidedInfrastructureDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_composition_av_pc_ProvidedInfrastructureDelegationConnector129", type=InfrastructureProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext__ProvidedInfrastructureDelegationConnector131: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__ProvidedInfrastructureDelegationConnector131",
    ends={
        Property(name="composition_av_pc_AssemblyContext133", type=pcm_av_pc_composition_av_pc_ProvidedInfrastructureDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_composition_av_pc_ProvidedInfrastructureDelegationConnector132", type=composition_av_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
usageScenario_UsageModel164: BinaryAssociation = BinaryAssociation(
    name="usageScenario_UsageModel164",
    ends={
        Property(name="UsageScenario165", type=pcm_av_pc_usagemodel_av_pc_UsageModel, multiplicity=Multiplicity(1, 1)),
        Property(name="usageModel_UsageScenario", type=UsageScenario, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
userData_UsageModel166: BinaryAssociation = BinaryAssociation(
    name="userData_UsageModel166",
    ends={
        Property(name="UserData", type=pcm_av_pc_usagemodel_av_pc_UsageModel, multiplicity=Multiplicity(1, 1)),
        Property(name="usageModel_UserData", type=UserData, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
innerRequiredRole__RequiredResourceDelegationConnector144: BinaryAssociation = BinaryAssociation(
    name="innerRequiredRole__RequiredResourceDelegationConnector144",
    ends={
        Property(name="entity_av_pc_ResourceRequiredRole146", type=pcm_av_pc_composition_av_pc_RequiredResourceDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_composition_av_pc_RequiredResourceDelegationConnector145", type=entity_av_pc_ResourceRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
outerRequiredRole__RequiredResourceDelegationConnector147: BinaryAssociation = BinaryAssociation(
    name="outerRequiredRole__RequiredResourceDelegationConnector147",
    ends={
        Property(name="entity_av_pc_ResourceRequiredRole149", type=pcm_av_pc_composition_av_pc_RequiredResourceDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_composition_av_pc_RequiredResourceDelegationConnector148", type=entity_av_pc_ResourceRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
parentStructure__AssemblyContext150: BinaryAssociation = BinaryAssociation(
    name="parentStructure__AssemblyContext150",
    ends={
        Property(name="ComposedStructure151", type=pcm_av_pc_composition_av_pc_AssemblyContext, multiplicity=Multiplicity(1, 1)),
        Property(name="assemblyContexts__ComposedStructure", type=composition_av_pc_ComposedStructure, multiplicity=Multiplicity(0, 1))
    }
)
encapsulatedComponent__AssemblyContext152: BinaryAssociation = BinaryAssociation(
    name="encapsulatedComponent__AssemblyContext152",
    ends={
        Property(name="RepositoryComponent", type=pcm_av_pc_composition_av_pc_AssemblyContext, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_composition_av_pc_AssemblyContext", type=RepositoryComponent, multiplicity=Multiplicity(0, 1))
    }
)
configParameterUsages__AssemblyContext153: BinaryAssociation = BinaryAssociation(
    name="configParameterUsages__AssemblyContext153",
    ends={
        Property(name="VariableUsage", type=pcm_av_pc_composition_av_pc_AssemblyContext, multiplicity=Multiplicity(1, 1)),
        Property(name="assemblyContext__VariableUsage", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
usageScenario_Workload154: BinaryAssociation = BinaryAssociation(
    name="usageScenario_Workload154",
    ends={
        Property(name="UsageScenario", type=pcm_av_pc_usagemodel_av_pc_Workload, multiplicity=Multiplicity(1, 1)),
        Property(name="workload_UsageScenario", type=UsageScenario, multiplicity=Multiplicity(0, 1))
    }
)
usageModel_UsageScenario155: BinaryAssociation = BinaryAssociation(
    name="usageModel_UsageScenario155",
    ends={
        Property(name="UsageModel", type=pcm_av_pc_usagemodel_av_pc_UsageScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="usageScenario_UsageModel", type=UsageModel, multiplicity=Multiplicity(0, 1))
    }
)
scenarioBehaviour_UsageScenario156: BinaryAssociation = BinaryAssociation(
    name="scenarioBehaviour_UsageScenario156",
    ends={
        Property(name="ScenarioBehaviour", type=pcm_av_pc_usagemodel_av_pc_UsageScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="usageScenario_SenarioBehaviour", type=ScenarioBehaviour, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
workload_UsageScenario157: BinaryAssociation = BinaryAssociation(
    name="workload_UsageScenario157",
    ends={
        Property(name="Workload", type=pcm_av_pc_usagemodel_av_pc_UsageScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="usageScenario_Workload", type=Workload, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assemblyContext_userData158: BinaryAssociation = BinaryAssociation(
    name="assemblyContext_userData158",
    ends={
        Property(name="composition_av_pc_AssemblyContext159", type=pcm_av_pc_usagemodel_av_pc_UserData, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_usagemodel_av_pc_UserData", type=composition_av_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
usageModel_UserData160: BinaryAssociation = BinaryAssociation(
    name="usageModel_UserData160",
    ends={
        Property(name="UsageModel161", type=pcm_av_pc_usagemodel_av_pc_UserData, multiplicity=Multiplicity(1, 1)),
        Property(name="userData_UsageModel", type=UsageModel, multiplicity=Multiplicity(0, 1))
    }
)
userDataParameterUsages_UserData162: BinaryAssociation = BinaryAssociation(
    name="userDataParameterUsages_UserData162",
    ends={
        Property(name="VariableUsage163", type=pcm_av_pc_usagemodel_av_pc_UserData, multiplicity=Multiplicity(1, 1)),
        Property(name="userData_VariableUsage", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
providedRole_EntryLevelSystemCall167: BinaryAssociation = BinaryAssociation(
    name="providedRole_EntryLevelSystemCall167",
    ends={
        Property(name="OperationProvidedRole168", type=pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall", type=OperationProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
operationSignature__EntryLevelSystemCall169: BinaryAssociation = BinaryAssociation(
    name="operationSignature__EntryLevelSystemCall169",
    ends={
        Property(name="OperationSignature", type=pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall170", type=OperationSignature, multiplicity=Multiplicity(0, 1))
    }
)
outputParameterUsages_EntryLevelSystemCall171: BinaryAssociation = BinaryAssociation(
    name="outputParameterUsages_EntryLevelSystemCall171",
    ends={
        Property(name="VariableUsage172", type=pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall, multiplicity=Multiplicity(1, 1)),
        Property(name="entryLevelSystemCall_OutputParameterUsage", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputParameterUsages_EntryLevelSystemCall173: BinaryAssociation = BinaryAssociation(
    name="inputParameterUsages_EntryLevelSystemCall173",
    ends={
        Property(name="VariableUsage174", type=pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall, multiplicity=Multiplicity(1, 1)),
        Property(name="entryLevelSystemCall_InputParameterUsage", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
successor175: BinaryAssociation = BinaryAssociation(
    name="successor175",
    ends={
        Property(name="AbstractUserAction", type=pcm_av_pc_usagemodel_av_pc_AbstractUserAction, multiplicity=Multiplicity(1, 1)),
        Property(name="predecessor", type=AbstractUserAction, multiplicity=Multiplicity(0, 1))
    }
)
predecessor176: BinaryAssociation = BinaryAssociation(
    name="predecessor176",
    ends={
        Property(name="AbstractUserAction177", type=pcm_av_pc_usagemodel_av_pc_AbstractUserAction, multiplicity=Multiplicity(1, 1)),
        Property(name="successor", type=AbstractUserAction, multiplicity=Multiplicity(0, 1))
    }
)
scenarioBehaviour_AbstractUserAction178: BinaryAssociation = BinaryAssociation(
    name="scenarioBehaviour_AbstractUserAction178",
    ends={
        Property(name="ScenarioBehaviour179", type=pcm_av_pc_usagemodel_av_pc_AbstractUserAction, multiplicity=Multiplicity(1, 1)),
        Property(name="actions_ScenarioBehaviour", type=ScenarioBehaviour, multiplicity=Multiplicity(0, 1))
    }
)
usageScenario_SenarioBehaviour180: BinaryAssociation = BinaryAssociation(
    name="usageScenario_SenarioBehaviour180",
    ends={
        Property(name="UsageScenario181", type=pcm_av_pc_usagemodel_av_pc_ScenarioBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="scenarioBehaviour_UsageScenario", type=UsageScenario, multiplicity=Multiplicity(0, 1))
    }
)
branchTransition_ScenarioBehaviour182: BinaryAssociation = BinaryAssociation(
    name="branchTransition_ScenarioBehaviour182",
    ends={
        Property(name="BranchTransition", type=pcm_av_pc_usagemodel_av_pc_ScenarioBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="branchedBehaviour_BranchTransition", type=BranchTransition, multiplicity=Multiplicity(0, 1))
    }
)
loop_ScenarioBehaviour183: BinaryAssociation = BinaryAssociation(
    name="loop_ScenarioBehaviour183",
    ends={
        Property(name="Loop184", type=pcm_av_pc_usagemodel_av_pc_ScenarioBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="bodyBehaviour_Loop", type=Loop, multiplicity=Multiplicity(0, 1))
    }
)
actions_ScenarioBehaviour185: BinaryAssociation = BinaryAssociation(
    name="actions_ScenarioBehaviour185",
    ends={
        Property(name="AbstractUserAction186", type=pcm_av_pc_usagemodel_av_pc_ScenarioBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="scenarioBehaviour_AbstractUserAction", type=AbstractUserAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
branch_BranchTransition187: BinaryAssociation = BinaryAssociation(
    name="branch_BranchTransition187",
    ends={
        Property(name="Branch", type=pcm_av_pc_usagemodel_av_pc_BranchTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="branchTransitions_Branch", type=Branch, multiplicity=Multiplicity(0, 1))
    }
)
branchedBehaviour_BranchTransition188: BinaryAssociation = BinaryAssociation(
    name="branchedBehaviour_BranchTransition188",
    ends={
        Property(name="ScenarioBehaviour189", type=pcm_av_pc_usagemodel_av_pc_BranchTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="branchTransition_ScenarioBehaviour", type=ScenarioBehaviour, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
branchTransitions_Branch190: BinaryAssociation = BinaryAssociation(
    name="branchTransitions_Branch190",
    ends={
        Property(name="BranchTransition191", type=pcm_av_pc_usagemodel_av_pc_Branch, multiplicity=Multiplicity(1, 1)),
        Property(name="branch_BranchTransition", type=BranchTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
loopIteration_Loop192: BinaryAssociation = BinaryAssociation(
    name="loopIteration_Loop192",
    ends={
        Property(name="PCMRandomVariable193", type=pcm_av_pc_usagemodel_av_pc_Loop, multiplicity=Multiplicity(1, 1)),
        Property(name="loop_LoopIteration", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bodyBehaviour_Loop194: BinaryAssociation = BinaryAssociation(
    name="bodyBehaviour_Loop194",
    ends={
        Property(name="ScenarioBehaviour195", type=pcm_av_pc_usagemodel_av_pc_Loop, multiplicity=Multiplicity(1, 1)),
        Property(name="loop_ScenarioBehaviour", type=ScenarioBehaviour, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
capacity_PassiveResource202: BinaryAssociation = BinaryAssociation(
    name="capacity_PassiveResource202",
    ends={
        Property(name="PCMRandomVariable203", type=pcm_av_pc_repository_av_pc_PassiveResource, multiplicity=Multiplicity(1, 1)),
        Property(name="passiveResource_capacity_PCMRandomVariable", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
basicComponent_PassiveResource204: BinaryAssociation = BinaryAssociation(
    name="basicComponent_PassiveResource204",
    ends={
        Property(name="BasicComponent", type=pcm_av_pc_repository_av_pc_PassiveResource, multiplicity=Multiplicity(1, 1)),
        Property(name="passiveResource_BasicComponent", type=BasicComponent, multiplicity=Multiplicity(0, 1))
    }
)
resourceTimeoutFailureType__PassiveResource205: BinaryAssociation = BinaryAssociation(
    name="resourceTimeoutFailureType__PassiveResource205",
    ends={
        Property(name="ResourceTimeoutFailureType", type=pcm_av_pc_repository_av_pc_PassiveResource, multiplicity=Multiplicity(1, 1)),
        Property(name="passiveResource__ResourceTimeoutFailureType", type=ResourceTimeoutFailureType, multiplicity=Multiplicity(0, 1))
    }
)
interArrivalTime_OpenWorkload196: BinaryAssociation = BinaryAssociation(
    name="interArrivalTime_OpenWorkload196",
    ends={
        Property(name="PCMRandomVariable197", type=pcm_av_pc_usagemodel_av_pc_OpenWorkload, multiplicity=Multiplicity(1, 1)),
        Property(name="openWorkload_PCMRandomVariable", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
timeSpecification_Delay198: BinaryAssociation = BinaryAssociation(
    name="timeSpecification_Delay198",
    ends={
        Property(name="PCMRandomVariable199", type=pcm_av_pc_usagemodel_av_pc_Delay, multiplicity=Multiplicity(1, 1)),
        Property(name="delay_TimeSpecification", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thinkTime_ClosedWorkload200: BinaryAssociation = BinaryAssociation(
    name="thinkTime_ClosedWorkload200",
    ends={
        Property(name="PCMRandomVariable201", type=pcm_av_pc_usagemodel_av_pc_ClosedWorkload, multiplicity=Multiplicity(1, 1)),
        Property(name="closedWorkload_PCMRandomVariable", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
repository__RepositoryComponent213: BinaryAssociation = BinaryAssociation(
    name="repository__RepositoryComponent213",
    ends={
        Property(name="Repository", type=pcm_av_pc_repository_av_pc_RepositoryComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="components__Repository", type=Repository, multiplicity=Multiplicity(0, 1))
    }
)
providingEntity_ProvidedRole214: BinaryAssociation = BinaryAssociation(
    name="providingEntity_ProvidedRole214",
    ends={
        Property(name="InterfaceProvidingEntity", type=pcm_av_pc_repository_av_pc_ProvidedRole, multiplicity=Multiplicity(1, 1)),
        Property(name="providedRoles_InterfaceProvidingEntity", type=entity_av_pc_InterfaceProvidingEntity, multiplicity=Multiplicity(0, 1))
    }
)
serviceEffectSpecifications__BasicComponent206: BinaryAssociation = BinaryAssociation(
    name="serviceEffectSpecifications__BasicComponent206",
    ends={
        Property(name="ServiceEffectSpecification", type=pcm_av_pc_repository_av_pc_BasicComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="basicComponent_ServiceEffectSpecification", type=ServiceEffectSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
passiveResource_BasicComponent207: BinaryAssociation = BinaryAssociation(
    name="passiveResource_BasicComponent207",
    ends={
        Property(name="PassiveResource208", type=pcm_av_pc_repository_av_pc_BasicComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="basicComponent_PassiveResource", type=PassiveResource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentCompleteComponentTypes209: BinaryAssociation = BinaryAssociation(
    name="parentCompleteComponentTypes209",
    ends={
        Property(name="CompleteComponentType", type=pcm_av_pc_repository_av_pc_ImplementationComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_repository_av_pc_ImplementationComponentType", type=CompleteComponentType, multiplicity=Multiplicity(0, 9999))
    }
)
componentParameterUsage_ImplementationComponentType210: BinaryAssociation = BinaryAssociation(
    name="componentParameterUsage_ImplementationComponentType210",
    ends={
        Property(name="VariableUsage212", type=pcm_av_pc_repository_av_pc_ImplementationComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_repository_av_pc_ImplementationComponentType211", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
failureTypes__Repository226: BinaryAssociation = BinaryAssociation(
    name="failureTypes__Repository226",
    ends={
        Property(name="FailureType", type=pcm_av_pc_repository_av_pc_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="repository__FailureType", type=FailureType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataTypes__Repository227: BinaryAssociation = BinaryAssociation(
    name="dataTypes__Repository227",
    ends={
        Property(name="DataType228", type=pcm_av_pc_repository_av_pc_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="repository__DataType", type=DataType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataType__Parameter215: BinaryAssociation = BinaryAssociation(
    name="dataType__Parameter215",
    ends={
        Property(name="DataType", type=pcm_av_pc_repository_av_pc_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_repository_av_pc_Parameter", type=DataType, multiplicity=Multiplicity(0, 1))
    }
)
infrastructureSignature__Parameter216: BinaryAssociation = BinaryAssociation(
    name="infrastructureSignature__Parameter216",
    ends={
        Property(name="InfrastructureSignature", type=pcm_av_pc_repository_av_pc_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameters__InfrastructureSignature", type=InfrastructureSignature, multiplicity=Multiplicity(0, 1))
    }
)
operationSignature__Parameter217: BinaryAssociation = BinaryAssociation(
    name="operationSignature__Parameter217",
    ends={
        Property(name="OperationSignature218", type=pcm_av_pc_repository_av_pc_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameters__OperationSignature", type=OperationSignature, multiplicity=Multiplicity(0, 1))
    }
)
eventType__Parameter219: BinaryAssociation = BinaryAssociation(
    name="eventType__Parameter219",
    ends={
        Property(name="EventType", type=pcm_av_pc_repository_av_pc_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameter__EventType", type=EventType, multiplicity=Multiplicity(0, 1))
    }
)
resourceSignature__Parameter220: BinaryAssociation = BinaryAssociation(
    name="resourceSignature__Parameter220",
    ends={
        Property(name="ResourceSignature", type=pcm_av_pc_repository_av_pc_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameter__ResourceSignature", type=ResourceSignature, multiplicity=Multiplicity(0, 1))
    }
)
repository__DataType221: BinaryAssociation = BinaryAssociation(
    name="repository__DataType221",
    ends={
        Property(name="Repository222", type=pcm_av_pc_repository_av_pc_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="dataTypes__Repository", type=Repository, multiplicity=Multiplicity(0, 1))
    }
)
components__Repository223: BinaryAssociation = BinaryAssociation(
    name="components__Repository223",
    ends={
        Property(name="RepositoryComponent224", type=pcm_av_pc_repository_av_pc_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="repository__RepositoryComponent", type=RepositoryComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
interfaces__Repository225: BinaryAssociation = BinaryAssociation(
    name="interfaces__Repository225",
    ends={
        Property(name="Interface", type=pcm_av_pc_repository_av_pc_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="repository__Interface", type=Interface, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exceptions__Signature245: BinaryAssociation = BinaryAssociation(
    name="exceptions__Signature245",
    ends={
        Property(name="pcm_av_pc_repository_av_pc_Signature", type=ExceptionType, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="ExceptionType", type=pcm_av_pc_repository_av_pc_Signature, multiplicity=Multiplicity(1, 1))
    }
)
failureType246: BinaryAssociation = BinaryAssociation(
    name="failureType246",
    ends={
        Property(name="FailureType248", type=pcm_av_pc_repository_av_pc_Signature, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_repository_av_pc_Signature247", type=FailureType, multiplicity=Multiplicity(0, 9999))
    }
)
parentInterfaces__Interface229: BinaryAssociation = BinaryAssociation(
    name="parentInterfaces__Interface229",
    ends={
        Property(name="Interface230", type=pcm_av_pc_repository_av_pc_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_repository_av_pc_Interface", type=Interface, multiplicity=Multiplicity(0, 9999))
    }
)
protocols__Interface231: BinaryAssociation = BinaryAssociation(
    name="protocols__Interface231",
    ends={
        Property(name="Protocol", type=pcm_av_pc_repository_av_pc_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_repository_av_pc_Interface232", type=Protocol, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredCharacterisations233: BinaryAssociation = BinaryAssociation(
    name="requiredCharacterisations233",
    ends={
        Property(name="RequiredCharacterisation", type=pcm_av_pc_repository_av_pc_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="interface_RequiredCharacterisation", type=RequiredCharacterisation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
repository__Interface234: BinaryAssociation = BinaryAssociation(
    name="repository__Interface234",
    ends={
        Property(name="Repository235", type=pcm_av_pc_repository_av_pc_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="interfaces__Repository", type=Repository, multiplicity=Multiplicity(0, 1))
    }
)
parameter236: BinaryAssociation = BinaryAssociation(
    name="parameter236",
    ends={
        Property(name="Parameter", type=pcm_av_pc_repository_av_pc_RequiredCharacterisation, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_repository_av_pc_RequiredCharacterisation", type=Parameter_, multiplicity=Multiplicity(0, 1))
    }
)
interface_RequiredCharacterisation237: BinaryAssociation = BinaryAssociation(
    name="interface_RequiredCharacterisation237",
    ends={
        Property(name="Interface238", type=pcm_av_pc_repository_av_pc_RequiredCharacterisation, multiplicity=Multiplicity(1, 1)),
        Property(name="requiredCharacterisations", type=Interface, multiplicity=Multiplicity(0, 1))
    }
)
eventTypes__EventGroup239: BinaryAssociation = BinaryAssociation(
    name="eventTypes__EventGroup239",
    ends={
        Property(name="EventType240", type=pcm_av_pc_repository_av_pc_EventGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="eventGroup__EventType", type=EventType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameter__EventType241: BinaryAssociation = BinaryAssociation(
    name="parameter__EventType241",
    ends={
        Property(name="Parameter242", type=pcm_av_pc_repository_av_pc_EventType, multiplicity=Multiplicity(1, 1)),
        Property(name="eventType__Parameter", type=Parameter_, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eventGroup__EventType243: BinaryAssociation = BinaryAssociation(
    name="eventGroup__EventType243",
    ends={
        Property(name="EventGroup244", type=pcm_av_pc_repository_av_pc_EventType, multiplicity=Multiplicity(1, 1)),
        Property(name="eventTypes__EventGroup", type=EventGroup, multiplicity=Multiplicity(0, 1))
    }
)
returnType__OperationSignature260: BinaryAssociation = BinaryAssociation(
    name="returnType__OperationSignature260",
    ends={
        Property(name="DataType261", type=pcm_av_pc_repository_av_pc_OperationSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_repository_av_pc_OperationSignature", type=DataType, multiplicity=Multiplicity(0, 1))
    }
)
parameters__InfrastructureSignature249: BinaryAssociation = BinaryAssociation(
    name="parameters__InfrastructureSignature249",
    ends={
        Property(name="Parameter250", type=pcm_av_pc_repository_av_pc_InfrastructureSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="infrastructureSignature__Parameter", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
infrastructureInterface__InfrastructureSignature251: BinaryAssociation = BinaryAssociation(
    name="infrastructureInterface__InfrastructureSignature251",
    ends={
        Property(name="InfrastructureInterface", type=pcm_av_pc_repository_av_pc_InfrastructureSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="infrastructureSignatures__InfrastructureInterface", type=InfrastructureInterface, multiplicity=Multiplicity(0, 1))
    }
)
infrastructureSignatures__InfrastructureInterface252: BinaryAssociation = BinaryAssociation(
    name="infrastructureSignatures__InfrastructureInterface252",
    ends={
        Property(name="InfrastructureSignature253", type=pcm_av_pc_repository_av_pc_InfrastructureInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="infrastructureInterface__InfrastructureSignature", type=InfrastructureSignature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredInterface__InfrastructureRequiredRole254: BinaryAssociation = BinaryAssociation(
    name="requiredInterface__InfrastructureRequiredRole254",
    ends={
        Property(name="InfrastructureInterface255", type=pcm_av_pc_repository_av_pc_InfrastructureRequiredRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_repository_av_pc_InfrastructureRequiredRole", type=InfrastructureInterface, multiplicity=Multiplicity(0, 1))
    }
)
requiringEntity_RequiredRole256: BinaryAssociation = BinaryAssociation(
    name="requiringEntity_RequiredRole256",
    ends={
        Property(name="InterfaceRequiringEntity", type=pcm_av_pc_repository_av_pc_RequiredRole, multiplicity=Multiplicity(1, 1)),
        Property(name="requiredRoles_InterfaceRequiringEntity", type=entity_av_pc_InterfaceRequiringEntity, multiplicity=Multiplicity(0, 1))
    }
)
interface__OperationSignature257: BinaryAssociation = BinaryAssociation(
    name="interface__OperationSignature257",
    ends={
        Property(name="OperationInterface", type=pcm_av_pc_repository_av_pc_OperationSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="signatures__OperationInterface", type=OperationInterface, multiplicity=Multiplicity(0, 1))
    }
)
parameters__OperationSignature258: BinaryAssociation = BinaryAssociation(
    name="parameters__OperationSignature258",
    ends={
        Property(name="Parameter259", type=pcm_av_pc_repository_av_pc_OperationSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="operationSignature__Parameter", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
signatures__OperationInterface262: BinaryAssociation = BinaryAssociation(
    name="signatures__OperationInterface262",
    ends={
        Property(name="OperationSignature263", type=pcm_av_pc_repository_av_pc_OperationInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="interface__OperationSignature", type=OperationSignature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredInterface__OperationRequiredRole264: BinaryAssociation = BinaryAssociation(
    name="requiredInterface__OperationRequiredRole264",
    ends={
        Property(name="OperationInterface265", type=pcm_av_pc_repository_av_pc_OperationRequiredRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_repository_av_pc_OperationRequiredRole", type=OperationInterface, multiplicity=Multiplicity(0, 1))
    }
)
eventGroup__SourceRole266: BinaryAssociation = BinaryAssociation(
    name="eventGroup__SourceRole266",
    ends={
        Property(name="EventGroup267", type=pcm_av_pc_repository_av_pc_SourceRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_repository_av_pc_SourceRole", type=EventGroup, multiplicity=Multiplicity(0, 1))
    }
)
eventGroup__SinkRole268: BinaryAssociation = BinaryAssociation(
    name="eventGroup__SinkRole268",
    ends={
        Property(name="EventGroup269", type=pcm_av_pc_repository_av_pc_SinkRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_repository_av_pc_SinkRole", type=EventGroup, multiplicity=Multiplicity(0, 1))
    }
)
providedInterface__OperationProvidedRole270: BinaryAssociation = BinaryAssociation(
    name="providedInterface__OperationProvidedRole270",
    ends={
        Property(name="OperationInterface271", type=pcm_av_pc_repository_av_pc_OperationProvidedRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_repository_av_pc_OperationProvidedRole", type=OperationInterface, multiplicity=Multiplicity(0, 1))
    }
)
providedInterface__InfrastructureProvidedRole272: BinaryAssociation = BinaryAssociation(
    name="providedInterface__InfrastructureProvidedRole272",
    ends={
        Property(name="InfrastructureInterface273", type=pcm_av_pc_repository_av_pc_InfrastructureProvidedRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_repository_av_pc_InfrastructureProvidedRole", type=InfrastructureInterface, multiplicity=Multiplicity(0, 1))
    }
)
parentProvidesComponentTypes274: BinaryAssociation = BinaryAssociation(
    name="parentProvidesComponentTypes274",
    ends={
        Property(name="ProvidesComponentType", type=pcm_av_pc_repository_av_pc_CompleteComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_repository_av_pc_CompleteComponentType", type=ProvidesComponentType, multiplicity=Multiplicity(0, 9999))
    }
)
compositeDataType_InnerDeclaration281: BinaryAssociation = BinaryAssociation(
    name="compositeDataType_InnerDeclaration281",
    ends={
        Property(name="CompositeDataType282", type=pcm_av_pc_repository_av_pc_InnerDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="innerDeclaration_CompositeDataType", type=CompositeDataType, multiplicity=Multiplicity(0, 1))
    }
)
innerType_CollectionDataType275: BinaryAssociation = BinaryAssociation(
    name="innerType_CollectionDataType275",
    ends={
        Property(name="DataType276", type=pcm_av_pc_repository_av_pc_CollectionDataType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_repository_av_pc_CollectionDataType", type=DataType, multiplicity=Multiplicity(0, 1))
    }
)
parentType_CompositeDataType277: BinaryAssociation = BinaryAssociation(
    name="parentType_CompositeDataType277",
    ends={
        Property(name="CompositeDataType", type=pcm_av_pc_repository_av_pc_CompositeDataType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_repository_av_pc_CompositeDataType", type=CompositeDataType, multiplicity=Multiplicity(0, 9999))
    }
)
innerDeclaration_CompositeDataType278: BinaryAssociation = BinaryAssociation(
    name="innerDeclaration_CompositeDataType278",
    ends={
        Property(name="InnerDeclaration", type=pcm_av_pc_repository_av_pc_CompositeDataType, multiplicity=Multiplicity(1, 1)),
        Property(name="compositeDataType_InnerDeclaration", type=InnerDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
datatype_InnerDeclaration279: BinaryAssociation = BinaryAssociation(
    name="datatype_InnerDeclaration279",
    ends={
        Property(name="DataType280", type=pcm_av_pc_repository_av_pc_InnerDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_repository_av_pc_InnerDeclaration", type=DataType, multiplicity=Multiplicity(0, 1))
    }
)
parameter__ResourceSignature283: BinaryAssociation = BinaryAssociation(
    name="parameter__ResourceSignature283",
    ends={
        Property(name="Parameter284", type=pcm_av_pc_resourcetype_av_pc_ResourceSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceSignature__Parameter", type=Parameter_, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resourceInterface__ResourceSignature285: BinaryAssociation = BinaryAssociation(
    name="resourceInterface__ResourceSignature285",
    ends={
        Property(name="ResourceInterface286", type=pcm_av_pc_resourcetype_av_pc_ResourceSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceSignatures__ResourceInterface", type=ResourceInterface, multiplicity=Multiplicity(0, 1))
    }
)
hardwareInducedFailureType__ProcessingResourceType287: BinaryAssociation = BinaryAssociation(
    name="hardwareInducedFailureType__ProcessingResourceType287",
    ends={
        Property(name="HardwareInducedFailureType", type=pcm_av_pc_resourcetype_av_pc_ProcessingResourceType, multiplicity=Multiplicity(1, 1)),
        Property(name="processingResourceType__HardwareInducedFailureType", type=HardwareInducedFailureType, multiplicity=Multiplicity(0, 1))
    }
)
resourceRepository_ResourceType288: BinaryAssociation = BinaryAssociation(
    name="resourceRepository_ResourceType288",
    ends={
        Property(name="ResourceRepository", type=pcm_av_pc_resourcetype_av_pc_ResourceType, multiplicity=Multiplicity(1, 1)),
        Property(name="availableResourceTypes_ResourceRepository", type=ResourceRepository, multiplicity=Multiplicity(0, 1))
    }
)
resourceInterfaces__ResourceRepository289: BinaryAssociation = BinaryAssociation(
    name="resourceInterfaces__ResourceRepository289",
    ends={
        Property(name="ResourceInterface290", type=pcm_av_pc_resourcetype_av_pc_ResourceRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceRepository__ResourceInterface", type=ResourceInterface, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
schedulingPolicies__ResourceRepository291: BinaryAssociation = BinaryAssociation(
    name="schedulingPolicies__ResourceRepository291",
    ends={
        Property(name="SchedulingPolicy", type=pcm_av_pc_resourcetype_av_pc_ResourceRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceRepository__SchedulingPolicy", type=SchedulingPolicy, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
availableResourceTypes_ResourceRepository292: BinaryAssociation = BinaryAssociation(
    name="availableResourceTypes_ResourceRepository292",
    ends={
        Property(name="ResourceType", type=pcm_av_pc_resourcetype_av_pc_ResourceRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceRepository_ResourceType", type=ResourceType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceRepository__SchedulingPolicy293: BinaryAssociation = BinaryAssociation(
    name="resourceRepository__SchedulingPolicy293",
    ends={
        Property(name="ResourceRepository294", type=pcm_av_pc_resourcetype_av_pc_SchedulingPolicy, multiplicity=Multiplicity(1, 1)),
        Property(name="schedulingPolicies__ResourceRepository", type=ResourceRepository, multiplicity=Multiplicity(0, 1))
    }
)
networkInducedFailureType__CommunicationLinkResourceType295: BinaryAssociation = BinaryAssociation(
    name="networkInducedFailureType__CommunicationLinkResourceType295",
    ends={
        Property(name="NetworkInducedFailureType", type=pcm_av_pc_resourcetype_av_pc_CommunicationLinkResourceType, multiplicity=Multiplicity(1, 1)),
        Property(name="communicationLinkResourceType__NetworkInducedFailureType", type=NetworkInducedFailureType, multiplicity=Multiplicity(0, 1))
    }
)
resourceRepository__ResourceInterface296: BinaryAssociation = BinaryAssociation(
    name="resourceRepository__ResourceInterface296",
    ends={
        Property(name="ResourceRepository297", type=pcm_av_pc_resourcetype_av_pc_ResourceInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceInterfaces__ResourceRepository", type=ResourceRepository, multiplicity=Multiplicity(0, 1))
    }
)
resourceSignatures__ResourceInterface298: BinaryAssociation = BinaryAssociation(
    name="resourceSignatures__ResourceInterface298",
    ends={
        Property(name="ResourceSignature299", type=pcm_av_pc_resourcetype_av_pc_ResourceInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceInterface__ResourceSignature", type=ResourceSignature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variableCharacterisation_VariableUsage300: BinaryAssociation = BinaryAssociation(
    name="variableCharacterisation_VariableUsage300",
    ends={
        Property(name="VariableCharacterisation301", type=pcm_av_pc_parameter_av_pc_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="variableUsage_VariableCharacterisation", type=VariableCharacterisation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
userData_VariableUsage302: BinaryAssociation = BinaryAssociation(
    name="userData_VariableUsage302",
    ends={
        Property(name="UserData303", type=pcm_av_pc_parameter_av_pc_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="userDataParameterUsages_UserData", type=UserData, multiplicity=Multiplicity(0, 1))
    }
)
callAction__VariableUsage304: BinaryAssociation = BinaryAssociation(
    name="callAction__VariableUsage304",
    ends={
        Property(name="CallAction", type=pcm_av_pc_parameter_av_pc_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="inputVariableUsages__CallAction", type=CallAction, multiplicity=Multiplicity(0, 1))
    }
)
synchronisationPoint_VariableUsage305: BinaryAssociation = BinaryAssociation(
    name="synchronisationPoint_VariableUsage305",
    ends={
        Property(name="SynchronisationPoint", type=pcm_av_pc_parameter_av_pc_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="outputParameterUsage_SynchronisationPoint", type=SynchronisationPoint, multiplicity=Multiplicity(0, 1))
    }
)
callReturnAction__VariableUsage306: BinaryAssociation = BinaryAssociation(
    name="callReturnAction__VariableUsage306",
    ends={
        Property(name="CallReturnAction", type=pcm_av_pc_parameter_av_pc_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="returnVariableUsage__CallReturnAction", type=CallReturnAction, multiplicity=Multiplicity(0, 1))
    }
)
setVariableAction_VariableUsage307: BinaryAssociation = BinaryAssociation(
    name="setVariableAction_VariableUsage307",
    ends={
        Property(name="SetVariableAction", type=pcm_av_pc_parameter_av_pc_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="localVariableUsages_SetVariableAction", type=SetVariableAction, multiplicity=Multiplicity(0, 1))
    }
)
specifiedOutputParameterAbstraction_expectedExternalOutputs_VariableUsage308: BinaryAssociation = BinaryAssociation(
    name="specifiedOutputParameterAbstraction_expectedExternalOutputs_VariableUsage308",
    ends={
        Property(name="SpecifiedOutputParameterAbstraction", type=pcm_av_pc_parameter_av_pc_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="expectedExternalOutputs_SpecifiedOutputParameterAbstraction", type=SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext__VariableUsage309: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__VariableUsage309",
    ends={
        Property(name="AssemblyContext310", type=pcm_av_pc_parameter_av_pc_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="configParameterUsages__AssemblyContext", type=composition_av_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
entryLevelSystemCall_InputParameterUsage311: BinaryAssociation = BinaryAssociation(
    name="entryLevelSystemCall_InputParameterUsage311",
    ends={
        Property(name="EntryLevelSystemCall", type=pcm_av_pc_parameter_av_pc_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="inputParameterUsages_EntryLevelSystemCall", type=EntryLevelSystemCall, multiplicity=Multiplicity(0, 1))
    }
)
entryLevelSystemCall_OutputParameterUsage312: BinaryAssociation = BinaryAssociation(
    name="entryLevelSystemCall_OutputParameterUsage312",
    ends={
        Property(name="EntryLevelSystemCall313", type=pcm_av_pc_parameter_av_pc_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="outputParameterUsages_EntryLevelSystemCall", type=EntryLevelSystemCall, multiplicity=Multiplicity(0, 1))
    }
)
namedReference__VariableUsage314: BinaryAssociation = BinaryAssociation(
    name="namedReference__VariableUsage314",
    ends={
        Property(name="parameter_av_pc_pcm_av_pc_AbstractNamedReference", type=pcm_av_pc_parameter_av_pc_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_parameter_av_pc_VariableUsage", type=parameter_av_pc_pcm_av_pc_AbstractNamedReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
specification_VariableCharacterisation315: BinaryAssociation = BinaryAssociation(
    name="specification_VariableCharacterisation315",
    ends={
        Property(name="PCMRandomVariable316", type=pcm_av_pc_parameter_av_pc_VariableCharacterisation, multiplicity=Multiplicity(1, 1)),
        Property(name="variableCharacterisation_Specification", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variableUsage_VariableCharacterisation317: BinaryAssociation = BinaryAssociation(
    name="variableUsage_VariableCharacterisation317",
    ends={
        Property(name="VariableUsage318", type=pcm_av_pc_parameter_av_pc_VariableCharacterisation, multiplicity=Multiplicity(1, 1)),
        Property(name="variableCharacterisation_VariableUsage", type=VariableUsage, multiplicity=Multiplicity(0, 1))
    }
)
communicationLinkResourceType__NetworkInducedFailureType323: BinaryAssociation = BinaryAssociation(
    name="communicationLinkResourceType__NetworkInducedFailureType323",
    ends={
        Property(name="CommunicationLinkResourceType", type=pcm_av_pc_reliability_av_pc_NetworkInducedFailureType, multiplicity=Multiplicity(1, 1)),
        Property(name="networkInducedFailureType__CommunicationLinkResourceType", type=CommunicationLinkResourceType, multiplicity=Multiplicity(0, 1))
    }
)
processingResourceType__HardwareInducedFailureType319: BinaryAssociation = BinaryAssociation(
    name="processingResourceType__HardwareInducedFailureType319",
    ends={
        Property(name="ProcessingResourceType", type=pcm_av_pc_reliability_av_pc_HardwareInducedFailureType, multiplicity=Multiplicity(1, 1)),
        Property(name="hardwareInducedFailureType__ProcessingResourceType", type=ProcessingResourceType, multiplicity=Multiplicity(0, 1))
    }
)
internalFailureOccurrenceDescriptions__SoftwareInducedFailureType320: BinaryAssociation = BinaryAssociation(
    name="internalFailureOccurrenceDescriptions__SoftwareInducedFailureType320",
    ends={
        Property(name="InternalFailureOccurrenceDescription", type=pcm_av_pc_reliability_av_pc_SoftwareInducedFailureType, multiplicity=Multiplicity(1, 1)),
        Property(name="softwareInducedFailureType__InternalFailureOccurrenceDescription", type=InternalFailureOccurrenceDescription, multiplicity=Multiplicity(0, 9999))
    }
)
internalAction__InternalFailureOccurrenceDescription321: BinaryAssociation = BinaryAssociation(
    name="internalAction__InternalFailureOccurrenceDescription321",
    ends={
        Property(name="InternalAction", type=pcm_av_pc_reliability_av_pc_InternalFailureOccurrenceDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="internalFailureOccurrenceDescriptions__InternalAction", type=InternalAction, multiplicity=Multiplicity(0, 1))
    }
)
softwareInducedFailureType__InternalFailureOccurrenceDescription322: BinaryAssociation = BinaryAssociation(
    name="softwareInducedFailureType__InternalFailureOccurrenceDescription322",
    ends={
        Property(name="SoftwareInducedFailureType", type=pcm_av_pc_reliability_av_pc_InternalFailureOccurrenceDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="internalFailureOccurrenceDescriptions__SoftwareInducedFailureType", type=SoftwareInducedFailureType, multiplicity=Multiplicity(0, 1))
    }
)
resourceDemand_Action331: BinaryAssociation = BinaryAssociation(
    name="resourceDemand_Action331",
    ends={
        Property(name="ParametricResourceDemand332", type=pcm_av_pc_seff_av_pc_AbstractInternalControlFlowAction, multiplicity=Multiplicity(1, 1)),
        Property(name="action_ParametricResourceDemand", type=seff_performance_av_pc_ParametricResourceDemand, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
infrastructureCall__Action333: BinaryAssociation = BinaryAssociation(
    name="infrastructureCall__Action333",
    ends={
        Property(name="InfrastructureCall334", type=pcm_av_pc_seff_av_pc_AbstractInternalControlFlowAction, multiplicity=Multiplicity(1, 1)),
        Property(name="action__InfrastructureCall", type=seff_performance_av_pc_InfrastructureCall, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceCall__Action335: BinaryAssociation = BinaryAssociation(
    name="resourceCall__Action335",
    ends={
        Property(name="ResourceCall336", type=pcm_av_pc_seff_av_pc_AbstractInternalControlFlowAction, multiplicity=Multiplicity(1, 1)),
        Property(name="action__ResourceCall", type=seff_performance_av_pc_ResourceCall, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specifiedReliabilityAnnotation__ExternalFailureOccurrenceDescription324: BinaryAssociation = BinaryAssociation(
    name="specifiedReliabilityAnnotation__ExternalFailureOccurrenceDescription324",
    ends={
        Property(name="SpecifiedReliabilityAnnotation", type=pcm_av_pc_reliability_av_pc_ExternalFailureOccurrenceDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="externalFailureOccurrenceDescriptions__SpecifiedReliabilityAnnotation", type=qos_reliability_av_pc_SpecifiedReliabilityAnnotation, multiplicity=Multiplicity(0, 1))
    }
)
failureType__ExternalFailureOccurrenceDescription325: BinaryAssociation = BinaryAssociation(
    name="failureType__ExternalFailureOccurrenceDescription325",
    ends={
        Property(name="FailureType326", type=pcm_av_pc_reliability_av_pc_ExternalFailureOccurrenceDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_reliability_av_pc_ExternalFailureOccurrenceDescription", type=FailureType, multiplicity=Multiplicity(0, 1))
    }
)
passiveResource__ResourceTimeoutFailureType327: BinaryAssociation = BinaryAssociation(
    name="passiveResource__ResourceTimeoutFailureType327",
    ends={
        Property(name="PassiveResource328", type=pcm_av_pc_reliability_av_pc_ResourceTimeoutFailureType, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceTimeoutFailureType__PassiveResource", type=PassiveResource, multiplicity=Multiplicity(0, 1))
    }
)
repository__FailureType329: BinaryAssociation = BinaryAssociation(
    name="repository__FailureType329",
    ends={
        Property(name="Repository330", type=pcm_av_pc_reliability_av_pc_FailureType, multiplicity=Multiplicity(1, 1)),
        Property(name="failureTypes__Repository", type=Repository, multiplicity=Multiplicity(0, 1))
    }
)
bodyBehaviour_Loop346: BinaryAssociation = BinaryAssociation(
    name="bodyBehaviour_Loop346",
    ends={
        Property(name="ResourceDemandingBehaviour347", type=pcm_av_pc_seff_av_pc_AbstractLoopAction, multiplicity=Multiplicity(1, 1)),
        Property(name="abstractLoopAction_ResourceDemandingBehaviour", type=ResourceDemandingBehaviour, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
branchAction_AbstractBranchTransition348: BinaryAssociation = BinaryAssociation(
    name="branchAction_AbstractBranchTransition348",
    ends={
        Property(name="BranchAction", type=pcm_av_pc_seff_av_pc_AbstractBranchTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="branches_Branch", type=BranchAction, multiplicity=Multiplicity(0, 1))
    }
)
branchBehaviour_BranchTransition349: BinaryAssociation = BinaryAssociation(
    name="branchBehaviour_BranchTransition349",
    ends={
        Property(name="ResourceDemandingBehaviour350", type=pcm_av_pc_seff_av_pc_AbstractBranchTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="abstractBranchTransition_ResourceDemandingBehaviour", type=ResourceDemandingBehaviour, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
predecessor_AbstractAction337: BinaryAssociation = BinaryAssociation(
    name="predecessor_AbstractAction337",
    ends={
        Property(name="AbstractAction", type=pcm_av_pc_seff_av_pc_AbstractAction, multiplicity=Multiplicity(1, 1)),
        Property(name="successor_AbstractAction", type=AbstractAction, multiplicity=Multiplicity(0, 1))
    }
)
successor_AbstractAction338: BinaryAssociation = BinaryAssociation(
    name="successor_AbstractAction338",
    ends={
        Property(name="AbstractAction339", type=pcm_av_pc_seff_av_pc_AbstractAction, multiplicity=Multiplicity(1, 1)),
        Property(name="predecessor_AbstractAction", type=AbstractAction, multiplicity=Multiplicity(0, 1))
    }
)
resourceDemandingBehaviour_AbstractAction340: BinaryAssociation = BinaryAssociation(
    name="resourceDemandingBehaviour_AbstractAction340",
    ends={
        Property(name="ResourceDemandingBehaviour", type=pcm_av_pc_seff_av_pc_AbstractAction, multiplicity=Multiplicity(1, 1)),
        Property(name="steps_Behaviour", type=ResourceDemandingBehaviour, multiplicity=Multiplicity(0, 1))
    }
)
abstractLoopAction_ResourceDemandingBehaviour341: BinaryAssociation = BinaryAssociation(
    name="abstractLoopAction_ResourceDemandingBehaviour341",
    ends={
        Property(name="AbstractLoopAction", type=pcm_av_pc_seff_av_pc_ResourceDemandingBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="bodyBehaviour_Loop342", type=AbstractLoopAction, multiplicity=Multiplicity(0, 1))
    }
)
abstractBranchTransition_ResourceDemandingBehaviour343: BinaryAssociation = BinaryAssociation(
    name="abstractBranchTransition_ResourceDemandingBehaviour343",
    ends={
        Property(name="AbstractBranchTransition", type=pcm_av_pc_seff_av_pc_ResourceDemandingBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="branchBehaviour_BranchTransition", type=AbstractBranchTransition, multiplicity=Multiplicity(0, 1))
    }
)
steps_Behaviour344: BinaryAssociation = BinaryAssociation(
    name="steps_Behaviour344",
    ends={
        Property(name="AbstractAction345", type=pcm_av_pc_seff_av_pc_ResourceDemandingBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceDemandingBehaviour_AbstractAction", type=AbstractAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
describedService__SEFF355: BinaryAssociation = BinaryAssociation(
    name="describedService__SEFF355",
    ends={
        Property(name="Signature", type=pcm_av_pc_seff_av_pc_ServiceEffectSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_seff_av_pc_ServiceEffectSpecification", type=Signature, multiplicity=Multiplicity(0, 1))
    }
)
basicComponent_ServiceEffectSpecification356: BinaryAssociation = BinaryAssociation(
    name="basicComponent_ServiceEffectSpecification356",
    ends={
        Property(name="BasicComponent357", type=pcm_av_pc_seff_av_pc_ServiceEffectSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="serviceEffectSpecifications__BasicComponent", type=BasicComponent, multiplicity=Multiplicity(0, 1))
    }
)
branches_Branch351: BinaryAssociation = BinaryAssociation(
    name="branches_Branch351",
    ends={
        Property(name="AbstractBranchTransition352", type=pcm_av_pc_seff_av_pc_BranchAction, multiplicity=Multiplicity(1, 1)),
        Property(name="branchAction_AbstractBranchTransition", type=AbstractBranchTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputVariableUsages__CallAction353: BinaryAssociation = BinaryAssociation(
    name="inputVariableUsages__CallAction353",
    ends={
        Property(name="VariableUsage354", type=pcm_av_pc_seff_av_pc_CallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="callAction__VariableUsage", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
synchronousForkedBehaviours_SynchronisationPoint374: BinaryAssociation = BinaryAssociation(
    name="synchronousForkedBehaviours_SynchronisationPoint374",
    ends={
        Property(name="ForkedBehaviour375", type=pcm_av_pc_seff_av_pc_SynchronisationPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="synchronisationPoint_ForkedBehaviour", type=ForkedBehaviour, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceDemandingInternalBehaviours358: BinaryAssociation = BinaryAssociation(
    name="resourceDemandingInternalBehaviours358",
    ends={
        Property(name="ResourceDemandingInternalBehaviour", type=pcm_av_pc_seff_av_pc_ResourceDemandingSEFF, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceDemandingSEFF_ResourceDemandingInternalBehaviour", type=ResourceDemandingInternalBehaviour, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceDemandingSEFF_ResourceDemandingInternalBehaviour359: BinaryAssociation = BinaryAssociation(
    name="resourceDemandingSEFF_ResourceDemandingInternalBehaviour359",
    ends={
        Property(name="ResourceDemandingSEFF", type=pcm_av_pc_seff_av_pc_ResourceDemandingInternalBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceDemandingInternalBehaviours", type=ResourceDemandingSEFF, multiplicity=Multiplicity(0, 1))
    }
)
passiveResource_ReleaseAction360: BinaryAssociation = BinaryAssociation(
    name="passiveResource_ReleaseAction360",
    ends={
        Property(name="PassiveResource361", type=pcm_av_pc_seff_av_pc_ReleaseAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_seff_av_pc_ReleaseAction", type=PassiveResource, multiplicity=Multiplicity(0, 1))
    }
)
iterationCount_LoopAction362: BinaryAssociation = BinaryAssociation(
    name="iterationCount_LoopAction362",
    ends={
        Property(name="PCMRandomVariable363", type=pcm_av_pc_seff_av_pc_LoopAction, multiplicity=Multiplicity(1, 1)),
        Property(name="loopAction_PCMRandomVariable", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
asynchronousForkedBehaviours_ForkAction364: BinaryAssociation = BinaryAssociation(
    name="asynchronousForkedBehaviours_ForkAction364",
    ends={
        Property(name="ForkedBehaviour", type=pcm_av_pc_seff_av_pc_ForkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="forkAction_ForkedBehaivour", type=ForkedBehaviour, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
synchronisingBehaviours_ForkAction365: BinaryAssociation = BinaryAssociation(
    name="synchronisingBehaviours_ForkAction365",
    ends={
        Property(name="SynchronisationPoint366", type=pcm_av_pc_seff_av_pc_ForkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="forkAction_SynchronisationPoint", type=SynchronisationPoint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
synchronisationPoint_ForkedBehaviour367: BinaryAssociation = BinaryAssociation(
    name="synchronisationPoint_ForkedBehaviour367",
    ends={
        Property(name="SynchronisationPoint368", type=pcm_av_pc_seff_av_pc_ForkedBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="synchronousForkedBehaviours_SynchronisationPoint", type=SynchronisationPoint, multiplicity=Multiplicity(0, 1))
    }
)
forkAction_ForkedBehaivour369: BinaryAssociation = BinaryAssociation(
    name="forkAction_ForkedBehaivour369",
    ends={
        Property(name="ForkAction", type=pcm_av_pc_seff_av_pc_ForkedBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="asynchronousForkedBehaviours_ForkAction", type=ForkAction, multiplicity=Multiplicity(0, 1))
    }
)
outputParameterUsage_SynchronisationPoint370: BinaryAssociation = BinaryAssociation(
    name="outputParameterUsage_SynchronisationPoint370",
    ends={
        Property(name="VariableUsage371", type=pcm_av_pc_seff_av_pc_SynchronisationPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="synchronisationPoint_VariableUsage", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
forkAction_SynchronisationPoint372: BinaryAssociation = BinaryAssociation(
    name="forkAction_SynchronisationPoint372",
    ends={
        Property(name="ForkAction373", type=pcm_av_pc_seff_av_pc_SynchronisationPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="synchronisingBehaviours_ForkAction", type=ForkAction, multiplicity=Multiplicity(0, 1))
    }
)
parameter_CollectionIteratorAction385: BinaryAssociation = BinaryAssociation(
    name="parameter_CollectionIteratorAction385",
    ends={
        Property(name="Parameter386", type=pcm_av_pc_seff_av_pc_CollectionIteratorAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_seff_av_pc_CollectionIteratorAction", type=Parameter_, multiplicity=Multiplicity(0, 1))
    }
)
branchCondition_GuardedBranchTransition387: BinaryAssociation = BinaryAssociation(
    name="branchCondition_GuardedBranchTransition387",
    ends={
        Property(name="PCMRandomVariable388", type=pcm_av_pc_seff_av_pc_GuardedBranchTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="guardedBranchTransition_PCMRandomVariable", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
calledService_ExternalService376: BinaryAssociation = BinaryAssociation(
    name="calledService_ExternalService376",
    ends={
        Property(name="OperationSignature377", type=pcm_av_pc_seff_av_pc_ExternalCallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_seff_av_pc_ExternalCallAction", type=OperationSignature, multiplicity=Multiplicity(0, 1))
    }
)
role_ExternalService378: BinaryAssociation = BinaryAssociation(
    name="role_ExternalService378",
    ends={
        Property(name="OperationRequiredRole380", type=pcm_av_pc_seff_av_pc_ExternalCallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_seff_av_pc_ExternalCallAction379", type=OperationRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
returnVariableUsage__CallReturnAction381: BinaryAssociation = BinaryAssociation(
    name="returnVariableUsage__CallReturnAction381",
    ends={
        Property(name="VariableUsage382", type=pcm_av_pc_seff_av_pc_CallReturnAction, multiplicity=Multiplicity(1, 1)),
        Property(name="callReturnAction__VariableUsage", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
passiveresource_AcquireAction383: BinaryAssociation = BinaryAssociation(
    name="passiveresource_AcquireAction383",
    ends={
        Property(name="PassiveResource384", type=pcm_av_pc_seff_av_pc_AcquireAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_seff_av_pc_AcquireAction", type=PassiveResource, multiplicity=Multiplicity(0, 1))
    }
)
internalFailureOccurrenceDescriptions__InternalAction398: BinaryAssociation = BinaryAssociation(
    name="internalFailureOccurrenceDescriptions__InternalAction398",
    ends={
        Property(name="InternalFailureOccurrenceDescription399", type=pcm_av_pc_seff_av_pc_InternalAction, multiplicity=Multiplicity(1, 1)),
        Property(name="internalAction__InternalFailureOccurrenceDescription", type=InternalFailureOccurrenceDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
localVariableUsages_SetVariableAction389: BinaryAssociation = BinaryAssociation(
    name="localVariableUsages_SetVariableAction389",
    ends={
        Property(name="VariableUsage390", type=pcm_av_pc_seff_av_pc_SetVariableAction, multiplicity=Multiplicity(1, 1)),
        Property(name="setVariableAction_VariableUsage", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
calledResourceDemandingInternalBehaviour391: BinaryAssociation = BinaryAssociation(
    name="calledResourceDemandingInternalBehaviour391",
    ends={
        Property(name="ResourceDemandingInternalBehaviour392", type=pcm_av_pc_seff_av_pc_InternalCallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_seff_av_pc_InternalCallAction", type=ResourceDemandingInternalBehaviour, multiplicity=Multiplicity(0, 1))
    }
)
eventType__EmitEventAction393: BinaryAssociation = BinaryAssociation(
    name="eventType__EmitEventAction393",
    ends={
        Property(name="EventType394", type=pcm_av_pc_seff_av_pc_EmitEventAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_seff_av_pc_EmitEventAction", type=EventType, multiplicity=Multiplicity(0, 1))
    }
)
sourceRole__EmitEventAction395: BinaryAssociation = BinaryAssociation(
    name="sourceRole__EmitEventAction395",
    ends={
        Property(name="SourceRole397", type=pcm_av_pc_seff_av_pc_EmitEventAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_seff_av_pc_EmitEventAction396", type=SourceRole, multiplicity=Multiplicity(0, 1))
    }
)
requiredRole__InfrastructureCall405: BinaryAssociation = BinaryAssociation(
    name="requiredRole__InfrastructureCall405",
    ends={
        Property(name="InfrastructureRequiredRole407", type=pcm_av_pc_seff_performance_av_pc_InfrastructureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_seff_performance_av_pc_InfrastructureCall406", type=InfrastructureRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
signature__InfrastructureCall400: BinaryAssociation = BinaryAssociation(
    name="signature__InfrastructureCall400",
    ends={
        Property(name="InfrastructureSignature401", type=pcm_av_pc_seff_performance_av_pc_InfrastructureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_seff_performance_av_pc_InfrastructureCall", type=InfrastructureSignature, multiplicity=Multiplicity(0, 1))
    }
)
numberOfCalls__InfrastructureCall402: BinaryAssociation = BinaryAssociation(
    name="numberOfCalls__InfrastructureCall402",
    ends={
        Property(name="PCMRandomVariable403", type=pcm_av_pc_seff_performance_av_pc_InfrastructureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="infrastructureCall__PCMRandomVariable", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
action__InfrastructureCall404: BinaryAssociation = BinaryAssociation(
    name="action__InfrastructureCall404",
    ends={
        Property(name="AbstractInternalControlFlowAction", type=pcm_av_pc_seff_performance_av_pc_InfrastructureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="infrastructureCall__Action", type=AbstractInternalControlFlowAction, multiplicity=Multiplicity(0, 1))
    }
)
numberOfCalls__ResourceCall415: BinaryAssociation = BinaryAssociation(
    name="numberOfCalls__ResourceCall415",
    ends={
        Property(name="PCMRandomVariable416", type=pcm_av_pc_seff_performance_av_pc_ResourceCall, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceCall__PCMRandomVariable", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
specification_ParametericResourceDemand417: BinaryAssociation = BinaryAssociation(
    name="specification_ParametericResourceDemand417",
    ends={
        Property(name="PCMRandomVariable418", type=pcm_av_pc_seff_performance_av_pc_ParametricResourceDemand, multiplicity=Multiplicity(1, 1)),
        Property(name="parametricResourceDemand_PCMRandomVariable", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
requiredResource_ParametricResourceDemand419: BinaryAssociation = BinaryAssociation(
    name="requiredResource_ParametricResourceDemand419",
    ends={
        Property(name="ProcessingResourceType420", type=pcm_av_pc_seff_performance_av_pc_ParametricResourceDemand, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_seff_performance_av_pc_ParametricResourceDemand", type=ProcessingResourceType, multiplicity=Multiplicity(0, 1))
    }
)
action__ResourceCall408: BinaryAssociation = BinaryAssociation(
    name="action__ResourceCall408",
    ends={
        Property(name="AbstractInternalControlFlowAction409", type=pcm_av_pc_seff_performance_av_pc_ResourceCall, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceCall__Action", type=AbstractInternalControlFlowAction, multiplicity=Multiplicity(0, 1))
    }
)
resourceRequiredRole__ResourceCall410: BinaryAssociation = BinaryAssociation(
    name="resourceRequiredRole__ResourceCall410",
    ends={
        Property(name="entity_av_pc_ResourceRequiredRole411", type=pcm_av_pc_seff_performance_av_pc_ResourceCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_seff_performance_av_pc_ResourceCall", type=entity_av_pc_ResourceRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
signature__ResourceCall412: BinaryAssociation = BinaryAssociation(
    name="signature__ResourceCall412",
    ends={
        Property(name="ResourceSignature414", type=pcm_av_pc_seff_performance_av_pc_ResourceCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_seff_performance_av_pc_ResourceCall413", type=ResourceSignature, multiplicity=Multiplicity(0, 1))
    }
)
primaryBehaviour__RecoveryAction425: BinaryAssociation = BinaryAssociation(
    name="primaryBehaviour__RecoveryAction425",
    ends={
        Property(name="seff_reliability_av_pc_RecoveryActionBehaviour426", type=pcm_av_pc_seff_reliability_av_pc_RecoveryAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_seff_reliability_av_pc_RecoveryAction", type=seff_reliability_av_pc_RecoveryActionBehaviour, multiplicity=Multiplicity(0, 1))
    }
)
recoveryActionBehaviours__RecoveryAction427: BinaryAssociation = BinaryAssociation(
    name="recoveryActionBehaviours__RecoveryAction427",
    ends={
        Property(name="RecoveryActionBehaviour", type=pcm_av_pc_seff_reliability_av_pc_RecoveryAction, multiplicity=Multiplicity(1, 1)),
        Property(name="recoveryAction__RecoveryActionBehaviour", type=seff_reliability_av_pc_RecoveryActionBehaviour, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
action_ParametricResourceDemand421: BinaryAssociation = BinaryAssociation(
    name="action_ParametricResourceDemand421",
    ends={
        Property(name="AbstractInternalControlFlowAction422", type=pcm_av_pc_seff_performance_av_pc_ParametricResourceDemand, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceDemand_Action", type=AbstractInternalControlFlowAction, multiplicity=Multiplicity(0, 1))
    }
)
failureHandlingAlternatives__RecoveryActionBehaviour423: BinaryAssociation = BinaryAssociation(
    name="failureHandlingAlternatives__RecoveryActionBehaviour423",
    ends={
        Property(name="seff_reliability_av_pc_RecoveryActionBehaviour", type=pcm_av_pc_seff_reliability_av_pc_RecoveryActionBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_seff_reliability_av_pc_RecoveryActionBehaviour", type=seff_reliability_av_pc_RecoveryActionBehaviour, multiplicity=Multiplicity(0, 9999))
    }
)
recoveryAction__RecoveryActionBehaviour424: BinaryAssociation = BinaryAssociation(
    name="recoveryAction__RecoveryActionBehaviour424",
    ends={
        Property(name="RecoveryAction", type=pcm_av_pc_seff_reliability_av_pc_RecoveryActionBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="recoveryActionBehaviours__RecoveryAction", type=seff_reliability_av_pc_RecoveryAction, multiplicity=Multiplicity(0, 1))
    }
)
signature_SpecifiedOutputParameterAbstraction439: BinaryAssociation = BinaryAssociation(
    name="signature_SpecifiedOutputParameterAbstraction439",
    ends={
        Property(name="Signature440", type=pcm_av_pc_qosannotations_av_pc_SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_qosannotations_av_pc_SpecifiedOutputParameterAbstraction", type=Signature, multiplicity=Multiplicity(0, 1))
    }
)
role_SpecifiedOutputParameterAbstraction441: BinaryAssociation = BinaryAssociation(
    name="role_SpecifiedOutputParameterAbstraction441",
    ends={
        Property(name="Role443", type=pcm_av_pc_qosannotations_av_pc_SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_qosannotations_av_pc_SpecifiedOutputParameterAbstraction442", type=Role, multiplicity=Multiplicity(0, 1))
    }
)
expectedExternalOutputs_SpecifiedOutputParameterAbstraction444: BinaryAssociation = BinaryAssociation(
    name="expectedExternalOutputs_SpecifiedOutputParameterAbstraction444",
    ends={
        Property(name="VariableUsage445", type=pcm_av_pc_qosannotations_av_pc_SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(1, 1)),
        Property(name="specifiedOutputParameterAbstraction_expectedExternalOutputs_VariableUsage", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
qosAnnotations_SpecifiedOutputParameterAbstraction446: BinaryAssociation = BinaryAssociation(
    name="qosAnnotations_SpecifiedOutputParameterAbstraction446",
    ends={
        Property(name="QoSAnnotations447", type=pcm_av_pc_qosannotations_av_pc_SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(1, 1)),
        Property(name="specifiedOutputParameterAbstractions_QoSAnnotations", type=QoSAnnotations, multiplicity=Multiplicity(0, 1))
    }
)
failureTypes_FailureHandlingEntity428: BinaryAssociation = BinaryAssociation(
    name="failureTypes_FailureHandlingEntity428",
    ends={
        Property(name="FailureType429", type=pcm_av_pc_seff_reliability_av_pc_FailureHandlingEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_seff_reliability_av_pc_FailureHandlingEntity", type=FailureType, multiplicity=Multiplicity(0, 9999))
    }
)
signature_SpecifiedQoSAnnation430: BinaryAssociation = BinaryAssociation(
    name="signature_SpecifiedQoSAnnation430",
    ends={
        Property(name="Signature431", type=pcm_av_pc_qosannotations_av_pc_SpecifiedQoSAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_qosannotations_av_pc_SpecifiedQoSAnnotation", type=Signature, multiplicity=Multiplicity(0, 1))
    }
)
role_SpecifiedQoSAnnotation432: BinaryAssociation = BinaryAssociation(
    name="role_SpecifiedQoSAnnotation432",
    ends={
        Property(name="Role", type=pcm_av_pc_qosannotations_av_pc_SpecifiedQoSAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_qosannotations_av_pc_SpecifiedQoSAnnotation433", type=Role, multiplicity=Multiplicity(0, 1))
    }
)
qosAnnotations_SpecifiedQoSAnnotation434: BinaryAssociation = BinaryAssociation(
    name="qosAnnotations_SpecifiedQoSAnnotation434",
    ends={
        Property(name="QoSAnnotations", type=pcm_av_pc_qosannotations_av_pc_SpecifiedQoSAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="specifiedQoSAnnotations_QoSAnnotations", type=QoSAnnotations, multiplicity=Multiplicity(0, 1))
    }
)
specifiedOutputParameterAbstractions_QoSAnnotations435: BinaryAssociation = BinaryAssociation(
    name="specifiedOutputParameterAbstractions_QoSAnnotations435",
    ends={
        Property(name="SpecifiedOutputParameterAbstraction436", type=pcm_av_pc_qosannotations_av_pc_QoSAnnotations, multiplicity=Multiplicity(1, 1)),
        Property(name="qosAnnotations_SpecifiedOutputParameterAbstraction", type=SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
system_QoSAnnotations437: BinaryAssociation = BinaryAssociation(
    name="system_QoSAnnotations437",
    ends={
        Property(name="System", type=pcm_av_pc_qosannotations_av_pc_QoSAnnotations, multiplicity=Multiplicity(1, 1)),
        Property(name="qosAnnotations_System", type=System, multiplicity=Multiplicity(0, 1))
    }
)
specifiedQoSAnnotations_QoSAnnotations438: BinaryAssociation = BinaryAssociation(
    name="specifiedQoSAnnotations_QoSAnnotations438",
    ends={
        Property(name="SpecifiedQoSAnnotation", type=pcm_av_pc_qosannotations_av_pc_QoSAnnotations, multiplicity=Multiplicity(1, 1)),
        Property(name="qosAnnotations_SpecifiedQoSAnnotation", type=SpecifiedQoSAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specification_SpecifiedExecutionTime448: BinaryAssociation = BinaryAssociation(
    name="specification_SpecifiedExecutionTime448",
    ends={
        Property(name="PCMRandomVariable449", type=pcm_av_pc_qos_performance_av_pc_SpecifiedExecutionTime, multiplicity=Multiplicity(1, 1)),
        Property(name="specifiedExecutionTime_PCMRandomVariable", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assemblyContext_ComponentSpecifiedExecutionTime450: BinaryAssociation = BinaryAssociation(
    name="assemblyContext_ComponentSpecifiedExecutionTime450",
    ends={
        Property(name="composition_av_pc_AssemblyContext451", type=pcm_av_pc_qos_performance_av_pc_ComponentSpecifiedExecutionTime, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_qos_performance_av_pc_ComponentSpecifiedExecutionTime", type=composition_av_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
qosAnnotations_System453: BinaryAssociation = BinaryAssociation(
    name="qosAnnotations_System453",
    ends={
        Property(name="QoSAnnotations454", type=pcm_av_pc_system_av_pc_System, multiplicity=Multiplicity(1, 1)),
        Property(name="system_QoSAnnotations", type=QoSAnnotations, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
linkingResources__ResourceEnvironment455: BinaryAssociation = BinaryAssociation(
    name="linkingResources__ResourceEnvironment455",
    ends={
        Property(name="LinkingResource", type=pcm_av_pc_resourceenvironment_av_pc_ResourceEnvironment, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceEnvironment_LinkingResource", type=LinkingResource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceContainer_ResourceEnvironment456: BinaryAssociation = BinaryAssociation(
    name="resourceContainer_ResourceEnvironment456",
    ends={
        Property(name="ResourceContainer", type=pcm_av_pc_resourceenvironment_av_pc_ResourceEnvironment, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceEnvironment_ResourceContainer", type=ResourceContainer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
externalFailureOccurrenceDescriptions__SpecifiedReliabilityAnnotation452: BinaryAssociation = BinaryAssociation(
    name="externalFailureOccurrenceDescriptions__SpecifiedReliabilityAnnotation452",
    ends={
        Property(name="ExternalFailureOccurrenceDescription", type=pcm_av_pc_qos_reliability_av_pc_SpecifiedReliabilityAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="specifiedReliabilityAnnotation__ExternalFailureOccurrenceDescription", type=ExternalFailureOccurrenceDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
activeResourceType_ActiveResourceSpecification472: BinaryAssociation = BinaryAssociation(
    name="activeResourceType_ActiveResourceSpecification472",
    ends={
        Property(name="ProcessingResourceType474", type=pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification473", type=ProcessingResourceType, multiplicity=Multiplicity(0, 1))
    }
)
processingRate_ProcessingResourceSpecification475: BinaryAssociation = BinaryAssociation(
    name="processingRate_ProcessingResourceSpecification475",
    ends={
        Property(name="PCMRandomVariable476", type=pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="processingResourceSpecification_processingRate_PCMRandomVariable", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resourceContainer_ProcessingResourceSpecification477: BinaryAssociation = BinaryAssociation(
    name="resourceContainer_ProcessingResourceSpecification477",
    ends={
        Property(name="ResourceContainer478", type=pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="activeResourceSpecifications_ResourceContainer", type=ResourceContainer, multiplicity=Multiplicity(0, 1))
    }
)
linkingResource_CommunicationLinkResourceSpecification479: BinaryAssociation = BinaryAssociation(
    name="linkingResource_CommunicationLinkResourceSpecification479",
    ends={
        Property(name="LinkingResource480", type=pcm_av_pc_resourceenvironment_av_pc_CommunicationLinkResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="communicationLinkResourceSpecifications_LinkingResource", type=LinkingResource, multiplicity=Multiplicity(0, 1))
    }
)
connectedResourceContainers_LinkingResource457: BinaryAssociation = BinaryAssociation(
    name="connectedResourceContainers_LinkingResource457",
    ends={
        Property(name="ResourceContainer458", type=pcm_av_pc_resourceenvironment_av_pc_LinkingResource, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_resourceenvironment_av_pc_LinkingResource", type=ResourceContainer, multiplicity=Multiplicity(0, 9999))
    }
)
communicationLinkResourceSpecifications_LinkingResource459: BinaryAssociation = BinaryAssociation(
    name="communicationLinkResourceSpecifications_LinkingResource459",
    ends={
        Property(name="CommunicationLinkResourceSpecification460", type=pcm_av_pc_resourceenvironment_av_pc_LinkingResource, multiplicity=Multiplicity(1, 1)),
        Property(name="linkingResource_CommunicationLinkResourceSpecification", type=CommunicationLinkResourceSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resourceEnvironment_LinkingResource461: BinaryAssociation = BinaryAssociation(
    name="resourceEnvironment_LinkingResource461",
    ends={
        Property(name="ResourceEnvironment", type=pcm_av_pc_resourceenvironment_av_pc_LinkingResource, multiplicity=Multiplicity(1, 1)),
        Property(name="linkingResources__ResourceEnvironment", type=ResourceEnvironment, multiplicity=Multiplicity(0, 1))
    }
)
activeResourceSpecifications_ResourceContainer462: BinaryAssociation = BinaryAssociation(
    name="activeResourceSpecifications_ResourceContainer462",
    ends={
        Property(name="ProcessingResourceSpecification463", type=pcm_av_pc_resourceenvironment_av_pc_ResourceContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceContainer_ProcessingResourceSpecification", type=ProcessingResourceSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceEnvironment_ResourceContainer464: BinaryAssociation = BinaryAssociation(
    name="resourceEnvironment_ResourceContainer464",
    ends={
        Property(name="ResourceEnvironment465", type=pcm_av_pc_resourceenvironment_av_pc_ResourceContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceContainer_ResourceEnvironment", type=ResourceEnvironment, multiplicity=Multiplicity(0, 1))
    }
)
nestedResourceContainers__ResourceContainer466: BinaryAssociation = BinaryAssociation(
    name="nestedResourceContainers__ResourceContainer466",
    ends={
        Property(name="ResourceContainer467", type=pcm_av_pc_resourceenvironment_av_pc_ResourceContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="parentResourceContainer__ResourceContainer", type=ResourceContainer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentResourceContainer__ResourceContainer468: BinaryAssociation = BinaryAssociation(
    name="parentResourceContainer__ResourceContainer468",
    ends={
        Property(name="ResourceContainer469", type=pcm_av_pc_resourceenvironment_av_pc_ResourceContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="nestedResourceContainers__ResourceContainer", type=ResourceContainer, multiplicity=Multiplicity(0, 1))
    }
)
schedulingPolicy470: BinaryAssociation = BinaryAssociation(
    name="schedulingPolicy470",
    ends={
        Property(name="SchedulingPolicy471", type=pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification", type=SchedulingPolicy, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext_AllocationContext489: BinaryAssociation = BinaryAssociation(
    name="assemblyContext_AllocationContext489",
    ends={
        Property(name="composition_av_pc_AssemblyContext491", type=pcm_av_pc_allocation_av_pc_AllocationContext, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_allocation_av_pc_AllocationContext490", type=composition_av_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
allocation_AllocationContext492: BinaryAssociation = BinaryAssociation(
    name="allocation_AllocationContext492",
    ends={
        Property(name="Allocation", type=pcm_av_pc_allocation_av_pc_AllocationContext, multiplicity=Multiplicity(1, 1)),
        Property(name="allocationContexts_Allocation", type=Allocation, multiplicity=Multiplicity(0, 1))
    }
)
eventChannel__AllocationContext493: BinaryAssociation = BinaryAssociation(
    name="eventChannel__AllocationContext493",
    ends={
        Property(name="composition_av_pc_EventChannel", type=pcm_av_pc_allocation_av_pc_AllocationContext, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_allocation_av_pc_AllocationContext494", type=composition_av_pc_EventChannel, multiplicity=Multiplicity(0, 1))
    }
)
communicationLinkResourceType_CommunicationLinkResourceSpecification481: BinaryAssociation = BinaryAssociation(
    name="communicationLinkResourceType_CommunicationLinkResourceSpecification481",
    ends={
        Property(name="CommunicationLinkResourceType482", type=pcm_av_pc_resourceenvironment_av_pc_CommunicationLinkResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_resourceenvironment_av_pc_CommunicationLinkResourceSpecification", type=CommunicationLinkResourceType, multiplicity=Multiplicity(0, 1))
    }
)
latency_CommunicationLinkResourceSpecification483: BinaryAssociation = BinaryAssociation(
    name="latency_CommunicationLinkResourceSpecification483",
    ends={
        Property(name="PCMRandomVariable484", type=pcm_av_pc_resourceenvironment_av_pc_CommunicationLinkResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="communicationLinkResourceSpecification_latency_PCMRandomVariable", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
throughput_CommunicationLinkResourceSpecification485: BinaryAssociation = BinaryAssociation(
    name="throughput_CommunicationLinkResourceSpecification485",
    ends={
        Property(name="PCMRandomVariable486", type=pcm_av_pc_resourceenvironment_av_pc_CommunicationLinkResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="communicationLinkResourceSpecifcation_throughput_PCMRandomVariable", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resourceContainer_AllocationContext487: BinaryAssociation = BinaryAssociation(
    name="resourceContainer_AllocationContext487",
    ends={
        Property(name="ResourceContainer488", type=pcm_av_pc_allocation_av_pc_AllocationContext, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_allocation_av_pc_AllocationContext", type=ResourceContainer, multiplicity=Multiplicity(0, 1))
    }
)
completions_CompletionRepository501: BinaryAssociation = BinaryAssociation(
    name="completions_CompletionRepository501",
    ends={
        Property(name="Completion", type=pcm_av_pc_completions_av_pc_CompletionRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_completions_av_pc_CompletionRepository", type=Completion, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredCommunicationLinkResource_ParametricResourceDemand502: BinaryAssociation = BinaryAssociation(
    name="requiredCommunicationLinkResource_ParametricResourceDemand502",
    ends={
        Property(name="CommunicationLinkResourceType503", type=pcm_av_pc_completions_av_pc_NetworkDemandParametricResourceDemand, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_completions_av_pc_NetworkDemandParametricResourceDemand", type=CommunicationLinkResourceType, multiplicity=Multiplicity(0, 1))
    }
)
targetResourceEnvironment_Allocation495: BinaryAssociation = BinaryAssociation(
    name="targetResourceEnvironment_Allocation495",
    ends={
        Property(name="ResourceEnvironment496", type=pcm_av_pc_allocation_av_pc_Allocation, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_allocation_av_pc_Allocation", type=ResourceEnvironment, multiplicity=Multiplicity(0, 1))
    }
)
system_Allocation497: BinaryAssociation = BinaryAssociation(
    name="system_Allocation497",
    ends={
        Property(name="System499", type=pcm_av_pc_allocation_av_pc_Allocation, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_pc_allocation_av_pc_Allocation498", type=System, multiplicity=Multiplicity(0, 1))
    }
)
allocationContexts_Allocation500: BinaryAssociation = BinaryAssociation(
    name="allocationContexts_Allocation500",
    ends={
        Property(name="AllocationContext", type=pcm_av_pc_allocation_av_pc_Allocation, multiplicity=Multiplicity(1, 1)),
        Property(name="allocation_AllocationContext", type=AllocationContext, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_pcm_av_pc_core_av_pc_PCMRandomVariable_RandomVariable = Generalization(general=RandomVariable, specific=pcm_av_pc_core_av_pc_PCMRandomVariable)
gen_pcm_av_pc_entity_av_pc_ResourceProvidedRole_Role = Generalization(general=Role, specific=pcm_av_pc_entity_av_pc_ResourceProvidedRole)
gen_pcm_av_pc_entity_av_pc_ResourceInterfaceProvidingRequiringEntity_entity_av_pc_ResourceInterfaceRequiringEntity = Generalization(general=entity_av_pc_ResourceInterfaceRequiringEntity, specific=pcm_av_pc_entity_av_pc_ResourceInterfaceProvidingRequiringEntity)
gen_pcm_av_pc_entity_av_pc_ResourceInterfaceProvidingRequiringEntity_entity_av_pc_ResourceInterfaceProvidingEntity = Generalization(general=entity_av_pc_ResourceInterfaceProvidingEntity, specific=pcm_av_pc_entity_av_pc_ResourceInterfaceProvidingRequiringEntity)
gen_pcm_av_pc_entity_av_pc_Entity_Identifier = Generalization(general=Identifier, specific=pcm_av_pc_entity_av_pc_Entity)
gen_pcm_av_pc_entity_av_pc_Entity_entity_av_pc_NamedElement = Generalization(general=entity_av_pc_NamedElement, specific=pcm_av_pc_entity_av_pc_Entity)
gen_pcm_av_pc_composition_av_pc_DelegationConnector_Connector = Generalization(general=Connector, specific=pcm_av_pc_composition_av_pc_DelegationConnector)
gen_pcm_av_pc_entity_av_pc_InterfaceProvidingRequiringEntity_entity_av_pc_InterfaceProvidingEntity = Generalization(general=entity_av_pc_InterfaceProvidingEntity, specific=pcm_av_pc_entity_av_pc_InterfaceProvidingRequiringEntity)
gen_pcm_av_pc_entity_av_pc_InterfaceProvidingRequiringEntity_entity_av_pc_InterfaceRequiringEntity = Generalization(general=entity_av_pc_InterfaceRequiringEntity, specific=pcm_av_pc_entity_av_pc_InterfaceProvidingRequiringEntity)
gen_pcm_av_pc_entity_av_pc_InterfaceProvidingEntity_Entity = Generalization(general=Entity, specific=pcm_av_pc_entity_av_pc_InterfaceProvidingEntity)
gen_pcm_av_pc_entity_av_pc_InterfaceRequiringEntity_entity_av_pc_Entity = Generalization(general=entity_av_pc_Entity, specific=pcm_av_pc_entity_av_pc_InterfaceRequiringEntity)
gen_pcm_av_pc_entity_av_pc_InterfaceRequiringEntity_entity_av_pc_ResourceInterfaceRequiringEntity = Generalization(general=entity_av_pc_ResourceInterfaceRequiringEntity, specific=pcm_av_pc_entity_av_pc_InterfaceRequiringEntity)
gen_pcm_av_pc_entity_av_pc_ResourceInterfaceRequiringEntity_Entity = Generalization(general=Entity, specific=pcm_av_pc_entity_av_pc_ResourceInterfaceRequiringEntity)
gen_pcm_av_pc_entity_av_pc_ResourceRequiredRole_Role = Generalization(general=Role, specific=pcm_av_pc_entity_av_pc_ResourceRequiredRole)
gen_pcm_av_pc_entity_av_pc_ResourceInterfaceProvidingEntity_Entity = Generalization(general=Entity, specific=pcm_av_pc_entity_av_pc_ResourceInterfaceProvidingEntity)
gen_pcm_av_pc_entity_av_pc_ComposedProvidingRequiringEntity_composition_av_pc_ComposedStructure = Generalization(general=composition_av_pc_ComposedStructure, specific=pcm_av_pc_entity_av_pc_ComposedProvidingRequiringEntity)
gen_pcm_av_pc_entity_av_pc_ComposedProvidingRequiringEntity_entity_av_pc_InterfaceProvidingRequiringEntity = Generalization(general=entity_av_pc_InterfaceProvidingRequiringEntity, specific=pcm_av_pc_entity_av_pc_ComposedProvidingRequiringEntity)
gen_pcm_av_pc_composition_av_pc_EventChannel_Entity = Generalization(general=Entity, specific=pcm_av_pc_composition_av_pc_EventChannel)
gen_pcm_av_pc_composition_av_pc_EventChannelSourceConnector_Connector = Generalization(general=Connector, specific=pcm_av_pc_composition_av_pc_EventChannelSourceConnector)
gen_pcm_av_pc_composition_av_pc_Connector_Entity = Generalization(general=Entity, specific=pcm_av_pc_composition_av_pc_Connector)
gen_pcm_av_pc_composition_av_pc_ComposedStructure_Entity = Generalization(general=Entity, specific=pcm_av_pc_composition_av_pc_ComposedStructure)
gen_pcm_av_pc_composition_av_pc_EventChannelSinkConnector_Connector = Generalization(general=Connector, specific=pcm_av_pc_composition_av_pc_EventChannelSinkConnector)
gen_pcm_av_pc_composition_av_pc_ProvidedDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_av_pc_composition_av_pc_ProvidedDelegationConnector)
gen_pcm_av_pc_composition_av_pc_RequiredDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_av_pc_composition_av_pc_RequiredDelegationConnector)
gen_pcm_av_pc_composition_av_pc_AssemblyEventConnector_Connector = Generalization(general=Connector, specific=pcm_av_pc_composition_av_pc_AssemblyEventConnector)
gen_pcm_av_pc_composition_av_pc_AssemblyConnector_Connector = Generalization(general=Connector, specific=pcm_av_pc_composition_av_pc_AssemblyConnector)
gen_pcm_av_pc_composition_av_pc_RequiredInfrastructureDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_av_pc_composition_av_pc_RequiredInfrastructureDelegationConnector)
gen_pcm_av_pc_composition_av_pc_RequiredResourceDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_av_pc_composition_av_pc_RequiredResourceDelegationConnector)
gen_pcm_av_pc_composition_av_pc_SourceDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_av_pc_composition_av_pc_SourceDelegationConnector)
gen_pcm_av_pc_composition_av_pc_SinkDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_av_pc_composition_av_pc_SinkDelegationConnector)
gen_pcm_av_pc_composition_av_pc_AssemblyInfrastructureConnector_Connector = Generalization(general=Connector, specific=pcm_av_pc_composition_av_pc_AssemblyInfrastructureConnector)
gen_pcm_av_pc_composition_av_pc_ProvidedInfrastructureDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_av_pc_composition_av_pc_ProvidedInfrastructureDelegationConnector)
gen_pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall)
gen_pcm_av_pc_composition_av_pc_AssemblyContext_Entity = Generalization(general=Entity, specific=pcm_av_pc_composition_av_pc_AssemblyContext)
gen_pcm_av_pc_usagemodel_av_pc_UsageScenario_Entity = Generalization(general=Entity, specific=pcm_av_pc_usagemodel_av_pc_UsageScenario)
gen_pcm_av_pc_usagemodel_av_pc_AbstractUserAction_Entity = Generalization(general=Entity, specific=pcm_av_pc_usagemodel_av_pc_AbstractUserAction)
gen_pcm_av_pc_usagemodel_av_pc_ScenarioBehaviour_Entity = Generalization(general=Entity, specific=pcm_av_pc_usagemodel_av_pc_ScenarioBehaviour)
gen_pcm_av_pc_usagemodel_av_pc_Start_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_av_pc_usagemodel_av_pc_Start)
gen_pcm_av_pc_usagemodel_av_pc_Branch_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_av_pc_usagemodel_av_pc_Branch)
gen_pcm_av_pc_usagemodel_av_pc_Loop_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_av_pc_usagemodel_av_pc_Loop)
gen_pcm_av_pc_usagemodel_av_pc_Stop_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_av_pc_usagemodel_av_pc_Stop)
gen_pcm_av_pc_repository_av_pc_BasicComponent_ImplementationComponentType = Generalization(general=ImplementationComponentType, specific=pcm_av_pc_repository_av_pc_BasicComponent)
gen_pcm_av_pc_usagemodel_av_pc_OpenWorkload_Workload = Generalization(general=Workload, specific=pcm_av_pc_usagemodel_av_pc_OpenWorkload)
gen_pcm_av_pc_usagemodel_av_pc_Delay_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_av_pc_usagemodel_av_pc_Delay)
gen_pcm_av_pc_usagemodel_av_pc_ClosedWorkload_Workload = Generalization(general=Workload, specific=pcm_av_pc_usagemodel_av_pc_ClosedWorkload)
gen_pcm_av_pc_repository_av_pc_PassiveResource_Entity = Generalization(general=Entity, specific=pcm_av_pc_repository_av_pc_PassiveResource)
gen_pcm_av_pc_repository_av_pc_RepositoryComponent_InterfaceProvidingRequiringEntity = Generalization(general=InterfaceProvidingRequiringEntity, specific=pcm_av_pc_repository_av_pc_RepositoryComponent)
gen_pcm_av_pc_repository_av_pc_ProvidedRole_Role = Generalization(general=Role, specific=pcm_av_pc_repository_av_pc_ProvidedRole)
gen_pcm_av_pc_repository_av_pc_ImplementationComponentType_RepositoryComponent = Generalization(general=RepositoryComponent, specific=pcm_av_pc_repository_av_pc_ImplementationComponentType)
gen_pcm_av_pc_repository_av_pc_Interface_Entity = Generalization(general=Entity, specific=pcm_av_pc_repository_av_pc_Interface)
gen_pcm_av_pc_repository_av_pc_Repository_Entity = Generalization(general=Entity, specific=pcm_av_pc_repository_av_pc_Repository)
gen_pcm_av_pc_repository_av_pc_EventGroup_Interface = Generalization(general=Interface, specific=pcm_av_pc_repository_av_pc_EventGroup)
gen_pcm_av_pc_repository_av_pc_EventType_Signature = Generalization(general=Signature, specific=pcm_av_pc_repository_av_pc_EventType)
gen_pcm_av_pc_repository_av_pc_Signature_Entity = Generalization(general=Entity, specific=pcm_av_pc_repository_av_pc_Signature)
gen_pcm_av_pc_repository_av_pc_OperationInterface_Interface = Generalization(general=Interface, specific=pcm_av_pc_repository_av_pc_OperationInterface)
gen_pcm_av_pc_repository_av_pc_InfrastructureSignature_Signature = Generalization(general=Signature, specific=pcm_av_pc_repository_av_pc_InfrastructureSignature)
gen_pcm_av_pc_repository_av_pc_InfrastructureInterface_Interface = Generalization(general=Interface, specific=pcm_av_pc_repository_av_pc_InfrastructureInterface)
gen_pcm_av_pc_repository_av_pc_InfrastructureRequiredRole_RequiredRole = Generalization(general=RequiredRole, specific=pcm_av_pc_repository_av_pc_InfrastructureRequiredRole)
gen_pcm_av_pc_repository_av_pc_RequiredRole_Role = Generalization(general=Role, specific=pcm_av_pc_repository_av_pc_RequiredRole)
gen_pcm_av_pc_repository_av_pc_OperationSignature_Signature = Generalization(general=Signature, specific=pcm_av_pc_repository_av_pc_OperationSignature)
gen_pcm_av_pc_repository_av_pc_OperationRequiredRole_RequiredRole = Generalization(general=RequiredRole, specific=pcm_av_pc_repository_av_pc_OperationRequiredRole)
gen_pcm_av_pc_repository_av_pc_SourceRole_RequiredRole = Generalization(general=RequiredRole, specific=pcm_av_pc_repository_av_pc_SourceRole)
gen_pcm_av_pc_repository_av_pc_SinkRole_ProvidedRole = Generalization(general=ProvidedRole, specific=pcm_av_pc_repository_av_pc_SinkRole)
gen_pcm_av_pc_repository_av_pc_OperationProvidedRole_ProvidedRole = Generalization(general=ProvidedRole, specific=pcm_av_pc_repository_av_pc_OperationProvidedRole)
gen_pcm_av_pc_repository_av_pc_InfrastructureProvidedRole_ProvidedRole = Generalization(general=ProvidedRole, specific=pcm_av_pc_repository_av_pc_InfrastructureProvidedRole)
gen_pcm_av_pc_repository_av_pc_CompositeComponent_entity_av_pc_ComposedProvidingRequiringEntity = Generalization(general=entity_av_pc_ComposedProvidingRequiringEntity, specific=pcm_av_pc_repository_av_pc_CompositeComponent)
gen_pcm_av_pc_repository_av_pc_CompositeComponent_repository_av_pc_ImplementationComponentType = Generalization(general=repository_av_pc_ImplementationComponentType, specific=pcm_av_pc_repository_av_pc_CompositeComponent)
gen_pcm_av_pc_repository_av_pc_CompleteComponentType_RepositoryComponent = Generalization(general=RepositoryComponent, specific=pcm_av_pc_repository_av_pc_CompleteComponentType)
gen_pcm_av_pc_repository_av_pc_ProvidesComponentType_RepositoryComponent = Generalization(general=RepositoryComponent, specific=pcm_av_pc_repository_av_pc_ProvidesComponentType)
gen_pcm_av_pc_repository_av_pc_Role_Entity = Generalization(general=Entity, specific=pcm_av_pc_repository_av_pc_Role)
gen_pcm_av_pc_resourcetype_av_pc_ResourceSignature_Entity = Generalization(general=Entity, specific=pcm_av_pc_resourcetype_av_pc_ResourceSignature)
gen_pcm_av_pc_repository_av_pc_PrimitiveDataType_DataType = Generalization(general=DataType, specific=pcm_av_pc_repository_av_pc_PrimitiveDataType)
gen_pcm_av_pc_repository_av_pc_CollectionDataType_entity_av_pc_Entity = Generalization(general=entity_av_pc_Entity, specific=pcm_av_pc_repository_av_pc_CollectionDataType)
gen_pcm_av_pc_repository_av_pc_CollectionDataType_repository_av_pc_DataType = Generalization(general=repository_av_pc_DataType, specific=pcm_av_pc_repository_av_pc_CollectionDataType)
gen_pcm_av_pc_repository_av_pc_CompositeDataType_entity_av_pc_Entity = Generalization(general=entity_av_pc_Entity, specific=pcm_av_pc_repository_av_pc_CompositeDataType)
gen_pcm_av_pc_repository_av_pc_CompositeDataType_repository_av_pc_DataType = Generalization(general=repository_av_pc_DataType, specific=pcm_av_pc_repository_av_pc_CompositeDataType)
gen_pcm_av_pc_repository_av_pc_InnerDeclaration_NamedElement = Generalization(general=NamedElement, specific=pcm_av_pc_repository_av_pc_InnerDeclaration)
gen_pcm_av_pc_resourcetype_av_pc_ProcessingResourceType_ResourceType = Generalization(general=ResourceType, specific=pcm_av_pc_resourcetype_av_pc_ProcessingResourceType)
gen_pcm_av_pc_resourcetype_av_pc_ResourceType_entity_av_pc_Entity = Generalization(general=entity_av_pc_Entity, specific=pcm_av_pc_resourcetype_av_pc_ResourceType)
gen_pcm_av_pc_resourcetype_av_pc_ResourceType_UnitCarryingElement = Generalization(general=UnitCarryingElement, specific=pcm_av_pc_resourcetype_av_pc_ResourceType)
gen_pcm_av_pc_resourcetype_av_pc_ResourceType_entity_av_pc_ResourceInterfaceProvidingEntity = Generalization(general=entity_av_pc_ResourceInterfaceProvidingEntity, specific=pcm_av_pc_resourcetype_av_pc_ResourceType)
gen_pcm_av_pc_resourcetype_av_pc_SchedulingPolicy_Entity = Generalization(general=Entity, specific=pcm_av_pc_resourcetype_av_pc_SchedulingPolicy)
gen_pcm_av_pc_resourcetype_av_pc_CommunicationLinkResourceType_ResourceType = Generalization(general=ResourceType, specific=pcm_av_pc_resourcetype_av_pc_CommunicationLinkResourceType)
gen_pcm_av_pc_resourcetype_av_pc_ResourceInterface_Entity = Generalization(general=Entity, specific=pcm_av_pc_resourcetype_av_pc_ResourceInterface)
gen_pcm_av_pc_parameter_av_pc_CharacterisedVariable_Variable = Generalization(general=Variable, specific=pcm_av_pc_parameter_av_pc_CharacterisedVariable)
gen_pcm_av_pc_reliability_av_pc_ExternalFailureOccurrenceDescription_FailureOccurrenceDescription = Generalization(general=FailureOccurrenceDescription, specific=pcm_av_pc_reliability_av_pc_ExternalFailureOccurrenceDescription)
gen_pcm_av_pc_reliability_av_pc_HardwareInducedFailureType_FailureType = Generalization(general=FailureType, specific=pcm_av_pc_reliability_av_pc_HardwareInducedFailureType)
gen_pcm_av_pc_reliability_av_pc_SoftwareInducedFailureType_FailureType = Generalization(general=FailureType, specific=pcm_av_pc_reliability_av_pc_SoftwareInducedFailureType)
gen_pcm_av_pc_reliability_av_pc_InternalFailureOccurrenceDescription_FailureOccurrenceDescription = Generalization(general=FailureOccurrenceDescription, specific=pcm_av_pc_reliability_av_pc_InternalFailureOccurrenceDescription)
gen_pcm_av_pc_reliability_av_pc_NetworkInducedFailureType_FailureType = Generalization(general=FailureType, specific=pcm_av_pc_reliability_av_pc_NetworkInducedFailureType)
gen_pcm_av_pc_seff_av_pc_AbstractInternalControlFlowAction_AbstractAction = Generalization(general=AbstractAction, specific=pcm_av_pc_seff_av_pc_AbstractInternalControlFlowAction)
gen_pcm_av_pc_seff_av_pc_AbstractAction_Entity = Generalization(general=Entity, specific=pcm_av_pc_seff_av_pc_AbstractAction)
gen_pcm_av_pc_reliability_av_pc_ResourceTimeoutFailureType_SoftwareInducedFailureType = Generalization(general=SoftwareInducedFailureType, specific=pcm_av_pc_reliability_av_pc_ResourceTimeoutFailureType)
gen_pcm_av_pc_reliability_av_pc_FailureType_Entity = Generalization(general=Entity, specific=pcm_av_pc_reliability_av_pc_FailureType)
gen_pcm_av_pc_seff_av_pc_StopAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_av_pc_seff_av_pc_StopAction)
gen_pcm_av_pc_seff_av_pc_AbstractBranchTransition_Entity = Generalization(general=Entity, specific=pcm_av_pc_seff_av_pc_AbstractBranchTransition)
gen_pcm_av_pc_seff_av_pc_BranchAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_av_pc_seff_av_pc_BranchAction)
gen_pcm_av_pc_seff_av_pc_ResourceDemandingBehaviour_Identifier = Generalization(general=Identifier, specific=pcm_av_pc_seff_av_pc_ResourceDemandingBehaviour)
gen_pcm_av_pc_seff_av_pc_AbstractLoopAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_av_pc_seff_av_pc_AbstractLoopAction)
gen_pcm_av_pc_seff_av_pc_ResourceDemandingSEFF_Identifier = Generalization(general=Identifier, specific=pcm_av_pc_seff_av_pc_ResourceDemandingSEFF)
gen_pcm_av_pc_seff_av_pc_ResourceDemandingSEFF_seff_av_pc_ServiceEffectSpecification = Generalization(general=seff_av_pc_ServiceEffectSpecification, specific=pcm_av_pc_seff_av_pc_ResourceDemandingSEFF)
gen_pcm_av_pc_seff_av_pc_ResourceDemandingSEFF_seff_av_pc_ResourceDemandingBehaviour = Generalization(general=seff_av_pc_ResourceDemandingBehaviour, specific=pcm_av_pc_seff_av_pc_ResourceDemandingSEFF)
gen_pcm_av_pc_seff_av_pc_StartAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_av_pc_seff_av_pc_StartAction)
gen_pcm_av_pc_seff_av_pc_ExternalCallAction_seff_av_pc_AbstractAction = Generalization(general=seff_av_pc_AbstractAction, specific=pcm_av_pc_seff_av_pc_ExternalCallAction)
gen_pcm_av_pc_seff_av_pc_ExternalCallAction_seff_av_pc_CallReturnAction = Generalization(general=seff_av_pc_CallReturnAction, specific=pcm_av_pc_seff_av_pc_ExternalCallAction)
gen_pcm_av_pc_seff_av_pc_ExternalCallAction_seff_reliability_av_pc_FailureHandlingEntity = Generalization(general=seff_reliability_av_pc_FailureHandlingEntity, specific=pcm_av_pc_seff_av_pc_ExternalCallAction)
gen_pcm_av_pc_seff_av_pc_ResourceDemandingInternalBehaviour_ResourceDemandingBehaviour = Generalization(general=ResourceDemandingBehaviour, specific=pcm_av_pc_seff_av_pc_ResourceDemandingInternalBehaviour)
gen_pcm_av_pc_seff_av_pc_ReleaseAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_av_pc_seff_av_pc_ReleaseAction)
gen_pcm_av_pc_seff_av_pc_LoopAction_AbstractLoopAction = Generalization(general=AbstractLoopAction, specific=pcm_av_pc_seff_av_pc_LoopAction)
gen_pcm_av_pc_seff_av_pc_ForkAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_av_pc_seff_av_pc_ForkAction)
gen_pcm_av_pc_seff_av_pc_ForkedBehaviour_ResourceDemandingBehaviour = Generalization(general=ResourceDemandingBehaviour, specific=pcm_av_pc_seff_av_pc_ForkedBehaviour)
gen_pcm_av_pc_seff_av_pc_CollectionIteratorAction_AbstractLoopAction = Generalization(general=AbstractLoopAction, specific=pcm_av_pc_seff_av_pc_CollectionIteratorAction)
gen_pcm_av_pc_seff_av_pc_GuardedBranchTransition_AbstractBranchTransition = Generalization(general=AbstractBranchTransition, specific=pcm_av_pc_seff_av_pc_GuardedBranchTransition)
gen_pcm_av_pc_seff_av_pc_SetVariableAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_av_pc_seff_av_pc_SetVariableAction)
gen_pcm_av_pc_seff_av_pc_CallReturnAction_CallAction = Generalization(general=CallAction, specific=pcm_av_pc_seff_av_pc_CallReturnAction)
gen_pcm_av_pc_seff_av_pc_ProbabilisticBranchTransition_AbstractBranchTransition = Generalization(general=AbstractBranchTransition, specific=pcm_av_pc_seff_av_pc_ProbabilisticBranchTransition)
gen_pcm_av_pc_seff_av_pc_AcquireAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_av_pc_seff_av_pc_AcquireAction)
gen_pcm_av_pc_seff_performance_av_pc_InfrastructureCall_CallAction = Generalization(general=CallAction, specific=pcm_av_pc_seff_performance_av_pc_InfrastructureCall)
gen_pcm_av_pc_seff_av_pc_InternalCallAction_seff_av_pc_CallAction = Generalization(general=seff_av_pc_CallAction, specific=pcm_av_pc_seff_av_pc_InternalCallAction)
gen_pcm_av_pc_seff_av_pc_InternalCallAction_seff_av_pc_AbstractInternalControlFlowAction = Generalization(general=seff_av_pc_AbstractInternalControlFlowAction, specific=pcm_av_pc_seff_av_pc_InternalCallAction)
gen_pcm_av_pc_seff_av_pc_EmitEventAction_seff_av_pc_AbstractAction = Generalization(general=seff_av_pc_AbstractAction, specific=pcm_av_pc_seff_av_pc_EmitEventAction)
gen_pcm_av_pc_seff_av_pc_EmitEventAction_seff_av_pc_CallAction = Generalization(general=seff_av_pc_CallAction, specific=pcm_av_pc_seff_av_pc_EmitEventAction)
gen_pcm_av_pc_seff_av_pc_InternalAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_av_pc_seff_av_pc_InternalAction)
gen_pcm_av_pc_seff_performance_av_pc_ResourceCall_CallAction = Generalization(general=CallAction, specific=pcm_av_pc_seff_performance_av_pc_ResourceCall)
gen_pcm_av_pc_seff_reliability_av_pc_RecoveryAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_av_pc_seff_reliability_av_pc_RecoveryAction)
gen_pcm_av_pc_seff_reliability_av_pc_FailureHandlingEntity_Entity = Generalization(general=Entity, specific=pcm_av_pc_seff_reliability_av_pc_FailureHandlingEntity)
gen_pcm_av_pc_seff_reliability_av_pc_RecoveryActionBehaviour_seff_reliability_av_pc_FailureHandlingEntity = Generalization(general=seff_reliability_av_pc_FailureHandlingEntity, specific=pcm_av_pc_seff_reliability_av_pc_RecoveryActionBehaviour)
gen_pcm_av_pc_seff_reliability_av_pc_RecoveryActionBehaviour_seff_av_pc_ResourceDemandingBehaviour = Generalization(general=seff_av_pc_ResourceDemandingBehaviour, specific=pcm_av_pc_seff_reliability_av_pc_RecoveryActionBehaviour)
gen_pcm_av_pc_qos_performance_av_pc_SystemSpecifiedExecutionTime_SpecifiedExecutionTime = Generalization(general=SpecifiedExecutionTime, specific=pcm_av_pc_qos_performance_av_pc_SystemSpecifiedExecutionTime)
gen_pcm_av_pc_qosannotations_av_pc_QoSAnnotations_Entity = Generalization(general=Entity, specific=pcm_av_pc_qosannotations_av_pc_QoSAnnotations)
gen_pcm_av_pc_qos_reliability_av_pc_SpecifiedReliabilityAnnotation_SpecifiedQoSAnnotation = Generalization(general=SpecifiedQoSAnnotation, specific=pcm_av_pc_qos_reliability_av_pc_SpecifiedReliabilityAnnotation)
gen_pcm_av_pc_qos_performance_av_pc_SpecifiedExecutionTime_SpecifiedQoSAnnotation = Generalization(general=SpecifiedQoSAnnotation, specific=pcm_av_pc_qos_performance_av_pc_SpecifiedExecutionTime)
gen_pcm_av_pc_qos_performance_av_pc_ComponentSpecifiedExecutionTime_SpecifiedExecutionTime = Generalization(general=SpecifiedExecutionTime, specific=pcm_av_pc_qos_performance_av_pc_ComponentSpecifiedExecutionTime)
gen_pcm_av_pc_resourceenvironment_av_pc_ResourceEnvironment_NamedElement = Generalization(general=NamedElement, specific=pcm_av_pc_resourceenvironment_av_pc_ResourceEnvironment)
gen_pcm_av_pc_resourceenvironment_av_pc_LinkingResource_Entity = Generalization(general=Entity, specific=pcm_av_pc_resourceenvironment_av_pc_LinkingResource)
gen_pcm_av_pc_system_av_pc_System_entity_av_pc_Entity = Generalization(general=entity_av_pc_Entity, specific=pcm_av_pc_system_av_pc_System)
gen_pcm_av_pc_system_av_pc_System_entity_av_pc_ComposedProvidingRequiringEntity = Generalization(general=entity_av_pc_ComposedProvidingRequiringEntity, specific=pcm_av_pc_system_av_pc_System)
gen_pcm_av_pc_resourceenvironment_av_pc_CommunicationLinkResourceSpecification_Identifier = Generalization(general=Identifier, specific=pcm_av_pc_resourceenvironment_av_pc_CommunicationLinkResourceSpecification)
gen_pcm_av_pc_resourceenvironment_av_pc_ResourceContainer_Entity = Generalization(general=Entity, specific=pcm_av_pc_resourceenvironment_av_pc_ResourceContainer)
gen_pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification_Identifier = Generalization(general=Identifier, specific=pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification)
gen_pcm_av_pc_allocation_av_pc_Allocation_Entity = Generalization(general=Entity, specific=pcm_av_pc_allocation_av_pc_Allocation)
gen_pcm_av_pc_allocation_av_pc_AllocationContext_Entity = Generalization(general=Entity, specific=pcm_av_pc_allocation_av_pc_AllocationContext)
gen_pcm_av_pc_completions_av_pc_Completion_entity_av_pc_ComposedProvidingRequiringEntity = Generalization(general=entity_av_pc_ComposedProvidingRequiringEntity, specific=pcm_av_pc_completions_av_pc_Completion)
gen_pcm_av_pc_completions_av_pc_Completion_repository_av_pc_ImplementationComponentType = Generalization(general=repository_av_pc_ImplementationComponentType, specific=pcm_av_pc_completions_av_pc_Completion)
gen_pcm_av_pc_completions_av_pc_DelegatingExternalCallAction_ExternalCallAction = Generalization(general=ExternalCallAction, specific=pcm_av_pc_completions_av_pc_DelegatingExternalCallAction)
gen_pcm_av_pc_completions_av_pc_NetworkDemandParametricResourceDemand_ParametricResourceDemand = Generalization(general=ParametricResourceDemand, specific=pcm_av_pc_completions_av_pc_NetworkDemandParametricResourceDemand)
gen_pcm_av_pc_subsystem_av_pc_SubSystem_entity_av_pc_ComposedProvidingRequiringEntity = Generalization(general=entity_av_pc_ComposedProvidingRequiringEntity, specific=pcm_av_pc_subsystem_av_pc_SubSystem)
gen_pcm_av_pc_subsystem_av_pc_SubSystem_repository_av_pc_RepositoryComponent = Generalization(general=repository_av_pc_RepositoryComponent, specific=pcm_av_pc_subsystem_av_pc_SubSystem)

# Domain Model
domain_model = DomainModel(
    name="pcm_av_pc",
    types={pcm_av_pc_Pointcut, pcm_av_pc_core_av_pc_PCMRandomVariable, RandomVariable, pcm_av_pc_DummyClass, pcm_av_pc_Advice, pcm_av_pc_EObject, pcm_av_pc_GlobalScope, pcm_av_pc_PerJoinPointScope, CommunicationLinkResourceSpecification, ProcessingResourceSpecification, pcm_av_pc_entity_av_pc_ResourceProvidedRole, Role, entity_av_pc_ResourceInterfaceProvidingEntity, ClosedWorkload, PassiveResource, VariableCharacterisation, seff_performance_av_pc_InfrastructureCall, seff_performance_av_pc_ResourceCall, seff_performance_av_pc_ParametricResourceDemand, LoopAction, GuardedBranchTransition, qos_performance_av_pc_SpecifiedExecutionTime, composition_av_pc_EventChannelSinkConnector, composition_av_pc_AssemblyEventConnector, Loop, OpenWorkload, Delay, pcm_av_pc_entity_av_pc_NamedElement, pcm_av_pc_entity_av_pc_ResourceInterfaceProvidingRequiringEntity, pcm_av_pc_entity_av_pc_Entity, Identifier, entity_av_pc_NamedElement, pcm_av_pc_composition_av_pc_DelegationConnector, Connector, ResourceInterface, pcm_av_pc_entity_av_pc_InterfaceProvidingRequiringEntity, entity_av_pc_InterfaceProvidingEntity, entity_av_pc_InterfaceRequiringEntity, pcm_av_pc_entity_av_pc_InterfaceProvidingEntity, Entity, ProvidedRole, pcm_av_pc_entity_av_pc_InterfaceRequiringEntity, entity_av_pc_Entity, entity_av_pc_ResourceInterfaceRequiringEntity, RequiredRole, pcm_av_pc_entity_av_pc_ResourceInterfaceRequiringEntity, entity_av_pc_ResourceRequiredRole, pcm_av_pc_entity_av_pc_ResourceRequiredRole, pcm_av_pc_entity_av_pc_ResourceInterfaceProvidingEntity, entity_av_pc_ResourceProvidedRole, pcm_av_pc_entity_av_pc_ComposedProvidingRequiringEntity, composition_av_pc_ComposedStructure, entity_av_pc_InterfaceProvidingRequiringEntity, pcm_av_pc_composition_av_pc_EventChannel, EventGroup, composition_av_pc_EventChannelSourceConnector, pcm_av_pc_composition_av_pc_EventChannelSourceConnector, pcm_av_pc_composition_av_pc_Connector, pcm_av_pc_composition_av_pc_ComposedStructure, composition_av_pc_AssemblyContext, composition_av_pc_ResourceRequiredDelegationConnector, composition_av_pc_EventChannel, composition_av_pc_Connector, pcm_av_pc_composition_av_pc_ResourceRequiredDelegationConnector, SourceRole, pcm_av_pc_composition_av_pc_EventChannelSinkConnector, SinkRole, PCMRandomVariable, pcm_av_pc_composition_av_pc_ProvidedDelegationConnector, DelegationConnector, OperationProvidedRole, pcm_av_pc_composition_av_pc_RequiredDelegationConnector, pcm_av_pc_composition_av_pc_AssemblyEventConnector, OperationRequiredRole, pcm_av_pc_composition_av_pc_AssemblyConnector, pcm_av_pc_composition_av_pc_RequiredInfrastructureDelegationConnector, pcm_av_pc_composition_av_pc_RequiredResourceDelegationConnector, pcm_av_pc_composition_av_pc_SourceDelegationConnector, pcm_av_pc_composition_av_pc_SinkDelegationConnector, pcm_av_pc_composition_av_pc_AssemblyInfrastructureConnector, InfrastructureProvidedRole, InfrastructureRequiredRole, pcm_av_pc_composition_av_pc_ProvidedInfrastructureDelegationConnector, pcm_av_pc_usagemodel_av_pc_UsageModel, UserData, pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall, AbstractUserAction, pcm_av_pc_composition_av_pc_AssemblyContext, RepositoryComponent, VariableUsage, pcm_av_pc_usagemodel_av_pc_Workload, UsageScenario, pcm_av_pc_usagemodel_av_pc_UsageScenario, UsageModel, ScenarioBehaviour, Workload, pcm_av_pc_usagemodel_av_pc_UserData, OperationSignature, pcm_av_pc_usagemodel_av_pc_AbstractUserAction, pcm_av_pc_usagemodel_av_pc_ScenarioBehaviour, pcm_av_pc_usagemodel_av_pc_Start, BranchTransition, pcm_av_pc_usagemodel_av_pc_BranchTransition, Branch, pcm_av_pc_usagemodel_av_pc_Branch, pcm_av_pc_usagemodel_av_pc_Loop, pcm_av_pc_usagemodel_av_pc_Stop, BasicComponent, ResourceTimeoutFailureType, pcm_av_pc_repository_av_pc_BasicComponent, ImplementationComponentType, pcm_av_pc_usagemodel_av_pc_OpenWorkload, pcm_av_pc_usagemodel_av_pc_Delay, pcm_av_pc_usagemodel_av_pc_ClosedWorkload, pcm_av_pc_repository_av_pc_PassiveResource, ServiceEffectSpecification, pcm_av_pc_repository_av_pc_RepositoryComponent, InterfaceProvidingRequiringEntity, Repository, pcm_av_pc_repository_av_pc_ProvidedRole, pcm_av_pc_repository_av_pc_ImplementationComponentType, CompleteComponentType, FailureType, pcm_av_pc_repository_av_pc_Interface, pcm_av_pc_repository_av_pc_Parameter, DataType, InfrastructureSignature, EventType, ResourceSignature, pcm_av_pc_repository_av_pc_DataType, pcm_av_pc_repository_av_pc_Repository, Interface, pcm_av_pc_repository_av_pc_ExceptionType, Protocol, RequiredCharacterisation, pcm_av_pc_repository_av_pc_RequiredCharacterisation, Parameter_, pcm_av_pc_repository_av_pc_EventGroup, pcm_av_pc_repository_av_pc_EventType, Signature, pcm_av_pc_repository_av_pc_Signature, ExceptionType, pcm_av_pc_repository_av_pc_OperationInterface, pcm_av_pc_repository_av_pc_InfrastructureSignature, InfrastructureInterface, pcm_av_pc_repository_av_pc_InfrastructureInterface, pcm_av_pc_repository_av_pc_InfrastructureRequiredRole, pcm_av_pc_repository_av_pc_RequiredRole, pcm_av_pc_repository_av_pc_OperationSignature, OperationInterface, pcm_av_pc_repository_av_pc_OperationRequiredRole, pcm_av_pc_repository_av_pc_SourceRole, pcm_av_pc_repository_av_pc_SinkRole, pcm_av_pc_repository_av_pc_OperationProvidedRole, pcm_av_pc_repository_av_pc_InfrastructureProvidedRole, pcm_av_pc_repository_av_pc_CompositeComponent, entity_av_pc_ComposedProvidingRequiringEntity, repository_av_pc_ImplementationComponentType, pcm_av_pc_repository_av_pc_CompleteComponentType, ProvidesComponentType, pcm_av_pc_repository_av_pc_ProvidesComponentType, pcm_av_pc_repository_av_pc_Role, pcm_av_pc_resourcetype_av_pc_ResourceSignature, pcm_av_pc_repository_av_pc_PrimitiveDataType, pcm_av_pc_repository_av_pc_CollectionDataType, repository_av_pc_DataType, pcm_av_pc_repository_av_pc_CompositeDataType, CompositeDataType, InnerDeclaration, pcm_av_pc_repository_av_pc_InnerDeclaration, NamedElement, pcm_av_pc_protocol_av_pc_Protocol, pcm_av_pc_resourcetype_av_pc_ProcessingResourceType, ResourceType, HardwareInducedFailureType, pcm_av_pc_resourcetype_av_pc_ResourceType, UnitCarryingElement, ResourceRepository, pcm_av_pc_resourcetype_av_pc_ResourceRepository, SchedulingPolicy, pcm_av_pc_resourcetype_av_pc_SchedulingPolicy, pcm_av_pc_resourcetype_av_pc_CommunicationLinkResourceType, NetworkInducedFailureType, pcm_av_pc_resourcetype_av_pc_ResourceInterface, pcm_av_pc_parameter_av_pc_VariableUsage, CallAction, SynchronisationPoint, CallReturnAction, SetVariableAction, SpecifiedOutputParameterAbstraction, EntryLevelSystemCall, parameter_av_pc_pcm_av_pc_AbstractNamedReference, pcm_av_pc_parameter_av_pc_VariableCharacterisation, pcm_av_pc_parameter_av_pc_CharacterisedVariable, Variable, CommunicationLinkResourceType, pcm_av_pc_reliability_av_pc_ExternalFailureOccurrenceDescription, pcm_av_pc_reliability_av_pc_FailureOccurrenceDescription, pcm_av_pc_reliability_av_pc_HardwareInducedFailureType, ProcessingResourceType, pcm_av_pc_reliability_av_pc_SoftwareInducedFailureType, InternalFailureOccurrenceDescription, pcm_av_pc_reliability_av_pc_InternalFailureOccurrenceDescription, FailureOccurrenceDescription, InternalAction, SoftwareInducedFailureType, pcm_av_pc_reliability_av_pc_NetworkInducedFailureType, pcm_av_pc_seff_av_pc_AbstractInternalControlFlowAction, AbstractAction, pcm_av_pc_seff_av_pc_AbstractAction, qos_reliability_av_pc_SpecifiedReliabilityAnnotation, pcm_av_pc_reliability_av_pc_ResourceTimeoutFailureType, pcm_av_pc_reliability_av_pc_FailureType, pcm_av_pc_seff_av_pc_StopAction, AbstractInternalControlFlowAction, pcm_av_pc_seff_av_pc_AbstractBranchTransition, BranchAction, pcm_av_pc_seff_av_pc_BranchAction, ResourceDemandingBehaviour, pcm_av_pc_seff_av_pc_ResourceDemandingBehaviour, AbstractLoopAction, AbstractBranchTransition, pcm_av_pc_seff_av_pc_AbstractLoopAction, pcm_av_pc_seff_av_pc_ResourceDemandingSEFF, seff_av_pc_ServiceEffectSpecification, seff_av_pc_ResourceDemandingBehaviour, pcm_av_pc_seff_av_pc_CallAction, pcm_av_pc_seff_av_pc_StartAction, pcm_av_pc_seff_av_pc_ServiceEffectSpecification, pcm_av_pc_seff_av_pc_ExternalCallAction, seff_av_pc_AbstractAction, seff_av_pc_CallReturnAction, seff_reliability_av_pc_FailureHandlingEntity, ResourceDemandingInternalBehaviour, pcm_av_pc_seff_av_pc_ResourceDemandingInternalBehaviour, ResourceDemandingSEFF, pcm_av_pc_seff_av_pc_ReleaseAction, pcm_av_pc_seff_av_pc_LoopAction, pcm_av_pc_seff_av_pc_ForkAction, ForkedBehaviour, pcm_av_pc_seff_av_pc_ForkedBehaviour, ForkAction, pcm_av_pc_seff_av_pc_SynchronisationPoint, pcm_av_pc_seff_av_pc_CollectionIteratorAction, pcm_av_pc_seff_av_pc_GuardedBranchTransition, pcm_av_pc_seff_av_pc_SetVariableAction, pcm_av_pc_seff_av_pc_CallReturnAction, pcm_av_pc_seff_av_pc_ProbabilisticBranchTransition, pcm_av_pc_seff_av_pc_AcquireAction, pcm_av_pc_seff_performance_av_pc_InfrastructureCall, pcm_av_pc_seff_av_pc_InternalCallAction, seff_av_pc_CallAction, seff_av_pc_AbstractInternalControlFlowAction, pcm_av_pc_seff_av_pc_EmitEventAction, pcm_av_pc_seff_av_pc_InternalAction, pcm_av_pc_seff_performance_av_pc_ResourceCall, pcm_av_pc_seff_performance_av_pc_ParametricResourceDemand, pcm_av_pc_seff_reliability_av_pc_RecoveryAction, pcm_av_pc_seff_reliability_av_pc_FailureHandlingEntity, pcm_av_pc_seff_reliability_av_pc_RecoveryActionBehaviour, seff_reliability_av_pc_RecoveryActionBehaviour, seff_reliability_av_pc_RecoveryAction, pcm_av_pc_qos_performance_av_pc_SystemSpecifiedExecutionTime, SpecifiedExecutionTime, pcm_av_pc_qosannotations_av_pc_SpecifiedQoSAnnotation, QoSAnnotations, pcm_av_pc_qosannotations_av_pc_QoSAnnotations, System, SpecifiedQoSAnnotation, pcm_av_pc_qosannotations_av_pc_SpecifiedOutputParameterAbstraction, pcm_av_pc_qos_reliability_av_pc_SpecifiedReliabilityAnnotation, pcm_av_pc_qos_performance_av_pc_SpecifiedExecutionTime, pcm_av_pc_qos_performance_av_pc_ComponentSpecifiedExecutionTime, pcm_av_pc_resourceenvironment_av_pc_ResourceEnvironment, LinkingResource, ResourceContainer, pcm_av_pc_resourceenvironment_av_pc_LinkingResource, ExternalFailureOccurrenceDescription, pcm_av_pc_system_av_pc_System, pcm_av_pc_resourceenvironment_av_pc_CommunicationLinkResourceSpecification, ResourceEnvironment, pcm_av_pc_resourceenvironment_av_pc_ResourceContainer, pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification, Allocation, pcm_av_pc_allocation_av_pc_Allocation, pcm_av_pc_allocation_av_pc_AllocationContext, pcm_av_pc_completions_av_pc_Completion, pcm_av_pc_completions_av_pc_CompletionRepository, Completion, pcm_av_pc_completions_av_pc_DelegatingExternalCallAction, ExternalCallAction, pcm_av_pc_completions_av_pc_NetworkDemandParametricResourceDemand, ParametricResourceDemand, AllocationContext, pcm_av_pc_subsystem_av_pc_SubSystem, repository_av_pc_RepositoryComponent, ParameterModifier, ComponentType, PrimitiveTypeEnum, VariableCharacterisationType},
    associations={scopedObject3, children5, children0, scopedObject1, communicationLinkResourceSpecifcation_throughput_PCMRandomVariable21, processingResourceSpecification_processingRate_PCMRandomVariable22, communicationLinkResourceSpecification_latency_PCMRandomVariable23, closedWorkload_PCMRandomVariable7, passiveResource_capacity_PCMRandomVariable8, variableCharacterisation_Specification9, infrastructureCall__PCMRandomVariable10, resourceCall__PCMRandomVariable11, parametricResourceDemand_PCMRandomVariable12, loopAction_PCMRandomVariable13, guardedBranchTransition_PCMRandomVariable14, specifiedExecutionTime_PCMRandomVariable15, eventChannelSinkConnector__FilterCondition16, assemblyEventConnector__FilterCondition17, loop_LoopIteration18, openWorkload_PCMRandomVariable19, delay_TimeSpecification20, resourceInterfaceProvidingEntity__ResourceProvidedRole25, providedResourceInterface__ResourceProvidedRole26, providedRoles_InterfaceProvidingEntity27, requiredRoles_InterfaceRequiringEntity28, resourceRequiredRoles__ResourceInterfaceRequiringEntity29, requiredResourceInterface__ResourceRequiredRole30, resourceInterfaceRequiringEntity__ResourceRequiredRole32, resourceProvidedRoles__ResourceInterfaceProvidingEntity33, eventGroup__EventChannel45, eventChannelSourceConnector__EventChannel46, eventChannelSinkConnector__EventChannel47, parentStructure__EventChannel49, parentStructure__Connector34, assemblyContexts__ComposedStructure35, resourceRequiredDelegationConnectors_ComposedStructure36, eventChannel__ComposedStructure37, connectors__ComposedStructure38, innerResourceRequiredRole_ResourceRequiredDelegationConnector39, outerResourceRequiredRole_ResourceRequiredDelegationConnector40, parentStructure_ResourceRequiredDelegationConnector43, sourceRole__EventChannelSourceRole51, assemblyContext__EventChannelSourceConnector52, eventChannel__EventChannelSourceConnector54, sinkRole__EventChannelSinkConnector56, filterCondition__EventChannelSinkConnector57, assemblyContext__EventChannelSinkConnector58, eventChannel__EventChannelSinkConnector61, innerProvidedRole_ProvidedDelegationConnector63, outerProvidedRole_ProvidedDelegationConnector64, assemblyContext_ProvidedDelegationConnector67, requiringAssemblyContext_AssemblyConnector77, providingAssemblyContext_AssemblyConnector79, providedRole_AssemblyConnector82, requiredRole_AssemblyConnector85, sinkRole__AssemblyEventConnector88, innerRequiredRole_RequiredDelegationConnector70, outerRequiredRole_RequiredDelegationConnector71, assemblyContext_RequiredDelegationConnector74, innerRequiredRole__RequiredInfrastructureDelegationConnector134, outerRequiredRole__RequiredInfrastructureDelegationConnector136, assemblyContext__RequiredInfrastructureDelegationConnector139, assemblyContext__RequiredResourceDelegationConnector142, sourceRole__AssemblyEventConnector90, sinkAssemblyContext__AssemblyEventConnector93, sourceAssemblyContext__AssemblyEventConnector96, filterCondition__AssemblyEventConnector99, innerSourceRole__SourceRole101, outerSourceRole__SourceRole103, assemblyContext__SourceDelegationConnector106, assemblyContext__SinkDelegationConnector109, innerSinkRole__SinkRole111, outerSinkRole__SinkRole114, providedRole__AssemblyInfrastructureConnector117, requiredRole__AssemblyInfrastructureConnector118, providingAssemblyContext__AssemblyInfrastructureConnector120, requiringAssemblyContext__AssemblyInfrastructureConnector123, innerProvidedRole__ProvidedInfrastructureDelegationConnector126, outerProvidedRole__ProvidedInfrastructureDelegationConnector128, assemblyContext__ProvidedInfrastructureDelegationConnector131, usageScenario_UsageModel164, userData_UsageModel166, innerRequiredRole__RequiredResourceDelegationConnector144, outerRequiredRole__RequiredResourceDelegationConnector147, parentStructure__AssemblyContext150, encapsulatedComponent__AssemblyContext152, configParameterUsages__AssemblyContext153, usageScenario_Workload154, usageModel_UsageScenario155, scenarioBehaviour_UsageScenario156, workload_UsageScenario157, assemblyContext_userData158, usageModel_UserData160, userDataParameterUsages_UserData162, providedRole_EntryLevelSystemCall167, operationSignature__EntryLevelSystemCall169, outputParameterUsages_EntryLevelSystemCall171, inputParameterUsages_EntryLevelSystemCall173, successor175, predecessor176, scenarioBehaviour_AbstractUserAction178, usageScenario_SenarioBehaviour180, branchTransition_ScenarioBehaviour182, loop_ScenarioBehaviour183, actions_ScenarioBehaviour185, branch_BranchTransition187, branchedBehaviour_BranchTransition188, branchTransitions_Branch190, loopIteration_Loop192, bodyBehaviour_Loop194, capacity_PassiveResource202, basicComponent_PassiveResource204, resourceTimeoutFailureType__PassiveResource205, interArrivalTime_OpenWorkload196, timeSpecification_Delay198, thinkTime_ClosedWorkload200, repository__RepositoryComponent213, providingEntity_ProvidedRole214, serviceEffectSpecifications__BasicComponent206, passiveResource_BasicComponent207, parentCompleteComponentTypes209, componentParameterUsage_ImplementationComponentType210, failureTypes__Repository226, dataTypes__Repository227, dataType__Parameter215, infrastructureSignature__Parameter216, operationSignature__Parameter217, eventType__Parameter219, resourceSignature__Parameter220, repository__DataType221, components__Repository223, interfaces__Repository225, exceptions__Signature245, failureType246, parentInterfaces__Interface229, protocols__Interface231, requiredCharacterisations233, repository__Interface234, parameter236, interface_RequiredCharacterisation237, eventTypes__EventGroup239, parameter__EventType241, eventGroup__EventType243, returnType__OperationSignature260, parameters__InfrastructureSignature249, infrastructureInterface__InfrastructureSignature251, infrastructureSignatures__InfrastructureInterface252, requiredInterface__InfrastructureRequiredRole254, requiringEntity_RequiredRole256, interface__OperationSignature257, parameters__OperationSignature258, signatures__OperationInterface262, requiredInterface__OperationRequiredRole264, eventGroup__SourceRole266, eventGroup__SinkRole268, providedInterface__OperationProvidedRole270, providedInterface__InfrastructureProvidedRole272, parentProvidesComponentTypes274, compositeDataType_InnerDeclaration281, innerType_CollectionDataType275, parentType_CompositeDataType277, innerDeclaration_CompositeDataType278, datatype_InnerDeclaration279, parameter__ResourceSignature283, resourceInterface__ResourceSignature285, hardwareInducedFailureType__ProcessingResourceType287, resourceRepository_ResourceType288, resourceInterfaces__ResourceRepository289, schedulingPolicies__ResourceRepository291, availableResourceTypes_ResourceRepository292, resourceRepository__SchedulingPolicy293, networkInducedFailureType__CommunicationLinkResourceType295, resourceRepository__ResourceInterface296, resourceSignatures__ResourceInterface298, variableCharacterisation_VariableUsage300, userData_VariableUsage302, callAction__VariableUsage304, synchronisationPoint_VariableUsage305, callReturnAction__VariableUsage306, setVariableAction_VariableUsage307, specifiedOutputParameterAbstraction_expectedExternalOutputs_VariableUsage308, assemblyContext__VariableUsage309, entryLevelSystemCall_InputParameterUsage311, entryLevelSystemCall_OutputParameterUsage312, namedReference__VariableUsage314, specification_VariableCharacterisation315, variableUsage_VariableCharacterisation317, communicationLinkResourceType__NetworkInducedFailureType323, processingResourceType__HardwareInducedFailureType319, internalFailureOccurrenceDescriptions__SoftwareInducedFailureType320, internalAction__InternalFailureOccurrenceDescription321, softwareInducedFailureType__InternalFailureOccurrenceDescription322, resourceDemand_Action331, infrastructureCall__Action333, resourceCall__Action335, specifiedReliabilityAnnotation__ExternalFailureOccurrenceDescription324, failureType__ExternalFailureOccurrenceDescription325, passiveResource__ResourceTimeoutFailureType327, repository__FailureType329, bodyBehaviour_Loop346, branchAction_AbstractBranchTransition348, branchBehaviour_BranchTransition349, predecessor_AbstractAction337, successor_AbstractAction338, resourceDemandingBehaviour_AbstractAction340, abstractLoopAction_ResourceDemandingBehaviour341, abstractBranchTransition_ResourceDemandingBehaviour343, steps_Behaviour344, describedService__SEFF355, basicComponent_ServiceEffectSpecification356, branches_Branch351, inputVariableUsages__CallAction353, synchronousForkedBehaviours_SynchronisationPoint374, resourceDemandingInternalBehaviours358, resourceDemandingSEFF_ResourceDemandingInternalBehaviour359, passiveResource_ReleaseAction360, iterationCount_LoopAction362, asynchronousForkedBehaviours_ForkAction364, synchronisingBehaviours_ForkAction365, synchronisationPoint_ForkedBehaviour367, forkAction_ForkedBehaivour369, outputParameterUsage_SynchronisationPoint370, forkAction_SynchronisationPoint372, parameter_CollectionIteratorAction385, branchCondition_GuardedBranchTransition387, calledService_ExternalService376, role_ExternalService378, returnVariableUsage__CallReturnAction381, passiveresource_AcquireAction383, internalFailureOccurrenceDescriptions__InternalAction398, localVariableUsages_SetVariableAction389, calledResourceDemandingInternalBehaviour391, eventType__EmitEventAction393, sourceRole__EmitEventAction395, requiredRole__InfrastructureCall405, signature__InfrastructureCall400, numberOfCalls__InfrastructureCall402, action__InfrastructureCall404, numberOfCalls__ResourceCall415, specification_ParametericResourceDemand417, requiredResource_ParametricResourceDemand419, action__ResourceCall408, resourceRequiredRole__ResourceCall410, signature__ResourceCall412, primaryBehaviour__RecoveryAction425, recoveryActionBehaviours__RecoveryAction427, action_ParametricResourceDemand421, failureHandlingAlternatives__RecoveryActionBehaviour423, recoveryAction__RecoveryActionBehaviour424, signature_SpecifiedOutputParameterAbstraction439, role_SpecifiedOutputParameterAbstraction441, expectedExternalOutputs_SpecifiedOutputParameterAbstraction444, qosAnnotations_SpecifiedOutputParameterAbstraction446, failureTypes_FailureHandlingEntity428, signature_SpecifiedQoSAnnation430, role_SpecifiedQoSAnnotation432, qosAnnotations_SpecifiedQoSAnnotation434, specifiedOutputParameterAbstractions_QoSAnnotations435, system_QoSAnnotations437, specifiedQoSAnnotations_QoSAnnotations438, specification_SpecifiedExecutionTime448, assemblyContext_ComponentSpecifiedExecutionTime450, qosAnnotations_System453, linkingResources__ResourceEnvironment455, resourceContainer_ResourceEnvironment456, externalFailureOccurrenceDescriptions__SpecifiedReliabilityAnnotation452, activeResourceType_ActiveResourceSpecification472, processingRate_ProcessingResourceSpecification475, resourceContainer_ProcessingResourceSpecification477, linkingResource_CommunicationLinkResourceSpecification479, connectedResourceContainers_LinkingResource457, communicationLinkResourceSpecifications_LinkingResource459, resourceEnvironment_LinkingResource461, activeResourceSpecifications_ResourceContainer462, resourceEnvironment_ResourceContainer464, nestedResourceContainers__ResourceContainer466, parentResourceContainer__ResourceContainer468, schedulingPolicy470, assemblyContext_AllocationContext489, allocation_AllocationContext492, eventChannel__AllocationContext493, communicationLinkResourceType_CommunicationLinkResourceSpecification481, latency_CommunicationLinkResourceSpecification483, throughput_CommunicationLinkResourceSpecification485, resourceContainer_AllocationContext487, completions_CompletionRepository501, requiredCommunicationLinkResource_ParametricResourceDemand502, targetResourceEnvironment_Allocation495, system_Allocation497, allocationContexts_Allocation500},
    generalizations={gen_pcm_av_pc_core_av_pc_PCMRandomVariable_RandomVariable, gen_pcm_av_pc_entity_av_pc_ResourceProvidedRole_Role, gen_pcm_av_pc_entity_av_pc_ResourceInterfaceProvidingRequiringEntity_entity_av_pc_ResourceInterfaceRequiringEntity, gen_pcm_av_pc_entity_av_pc_ResourceInterfaceProvidingRequiringEntity_entity_av_pc_ResourceInterfaceProvidingEntity, gen_pcm_av_pc_entity_av_pc_Entity_Identifier, gen_pcm_av_pc_entity_av_pc_Entity_entity_av_pc_NamedElement, gen_pcm_av_pc_composition_av_pc_DelegationConnector_Connector, gen_pcm_av_pc_entity_av_pc_InterfaceProvidingRequiringEntity_entity_av_pc_InterfaceProvidingEntity, gen_pcm_av_pc_entity_av_pc_InterfaceProvidingRequiringEntity_entity_av_pc_InterfaceRequiringEntity, gen_pcm_av_pc_entity_av_pc_InterfaceProvidingEntity_Entity, gen_pcm_av_pc_entity_av_pc_InterfaceRequiringEntity_entity_av_pc_Entity, gen_pcm_av_pc_entity_av_pc_InterfaceRequiringEntity_entity_av_pc_ResourceInterfaceRequiringEntity, gen_pcm_av_pc_entity_av_pc_ResourceInterfaceRequiringEntity_Entity, gen_pcm_av_pc_entity_av_pc_ResourceRequiredRole_Role, gen_pcm_av_pc_entity_av_pc_ResourceInterfaceProvidingEntity_Entity, gen_pcm_av_pc_entity_av_pc_ComposedProvidingRequiringEntity_composition_av_pc_ComposedStructure, gen_pcm_av_pc_entity_av_pc_ComposedProvidingRequiringEntity_entity_av_pc_InterfaceProvidingRequiringEntity, gen_pcm_av_pc_composition_av_pc_EventChannel_Entity, gen_pcm_av_pc_composition_av_pc_EventChannelSourceConnector_Connector, gen_pcm_av_pc_composition_av_pc_Connector_Entity, gen_pcm_av_pc_composition_av_pc_ComposedStructure_Entity, gen_pcm_av_pc_composition_av_pc_EventChannelSinkConnector_Connector, gen_pcm_av_pc_composition_av_pc_ProvidedDelegationConnector_DelegationConnector, gen_pcm_av_pc_composition_av_pc_RequiredDelegationConnector_DelegationConnector, gen_pcm_av_pc_composition_av_pc_AssemblyEventConnector_Connector, gen_pcm_av_pc_composition_av_pc_AssemblyConnector_Connector, gen_pcm_av_pc_composition_av_pc_RequiredInfrastructureDelegationConnector_DelegationConnector, gen_pcm_av_pc_composition_av_pc_RequiredResourceDelegationConnector_DelegationConnector, gen_pcm_av_pc_composition_av_pc_SourceDelegationConnector_DelegationConnector, gen_pcm_av_pc_composition_av_pc_SinkDelegationConnector_DelegationConnector, gen_pcm_av_pc_composition_av_pc_AssemblyInfrastructureConnector_Connector, gen_pcm_av_pc_composition_av_pc_ProvidedInfrastructureDelegationConnector_DelegationConnector, gen_pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall_AbstractUserAction, gen_pcm_av_pc_composition_av_pc_AssemblyContext_Entity, gen_pcm_av_pc_usagemodel_av_pc_UsageScenario_Entity, gen_pcm_av_pc_usagemodel_av_pc_AbstractUserAction_Entity, gen_pcm_av_pc_usagemodel_av_pc_ScenarioBehaviour_Entity, gen_pcm_av_pc_usagemodel_av_pc_Start_AbstractUserAction, gen_pcm_av_pc_usagemodel_av_pc_Branch_AbstractUserAction, gen_pcm_av_pc_usagemodel_av_pc_Loop_AbstractUserAction, gen_pcm_av_pc_usagemodel_av_pc_Stop_AbstractUserAction, gen_pcm_av_pc_repository_av_pc_BasicComponent_ImplementationComponentType, gen_pcm_av_pc_usagemodel_av_pc_OpenWorkload_Workload, gen_pcm_av_pc_usagemodel_av_pc_Delay_AbstractUserAction, gen_pcm_av_pc_usagemodel_av_pc_ClosedWorkload_Workload, gen_pcm_av_pc_repository_av_pc_PassiveResource_Entity, gen_pcm_av_pc_repository_av_pc_RepositoryComponent_InterfaceProvidingRequiringEntity, gen_pcm_av_pc_repository_av_pc_ProvidedRole_Role, gen_pcm_av_pc_repository_av_pc_ImplementationComponentType_RepositoryComponent, gen_pcm_av_pc_repository_av_pc_Interface_Entity, gen_pcm_av_pc_repository_av_pc_Repository_Entity, gen_pcm_av_pc_repository_av_pc_EventGroup_Interface, gen_pcm_av_pc_repository_av_pc_EventType_Signature, gen_pcm_av_pc_repository_av_pc_Signature_Entity, gen_pcm_av_pc_repository_av_pc_OperationInterface_Interface, gen_pcm_av_pc_repository_av_pc_InfrastructureSignature_Signature, gen_pcm_av_pc_repository_av_pc_InfrastructureInterface_Interface, gen_pcm_av_pc_repository_av_pc_InfrastructureRequiredRole_RequiredRole, gen_pcm_av_pc_repository_av_pc_RequiredRole_Role, gen_pcm_av_pc_repository_av_pc_OperationSignature_Signature, gen_pcm_av_pc_repository_av_pc_OperationRequiredRole_RequiredRole, gen_pcm_av_pc_repository_av_pc_SourceRole_RequiredRole, gen_pcm_av_pc_repository_av_pc_SinkRole_ProvidedRole, gen_pcm_av_pc_repository_av_pc_OperationProvidedRole_ProvidedRole, gen_pcm_av_pc_repository_av_pc_InfrastructureProvidedRole_ProvidedRole, gen_pcm_av_pc_repository_av_pc_CompositeComponent_entity_av_pc_ComposedProvidingRequiringEntity, gen_pcm_av_pc_repository_av_pc_CompositeComponent_repository_av_pc_ImplementationComponentType, gen_pcm_av_pc_repository_av_pc_CompleteComponentType_RepositoryComponent, gen_pcm_av_pc_repository_av_pc_ProvidesComponentType_RepositoryComponent, gen_pcm_av_pc_repository_av_pc_Role_Entity, gen_pcm_av_pc_resourcetype_av_pc_ResourceSignature_Entity, gen_pcm_av_pc_repository_av_pc_PrimitiveDataType_DataType, gen_pcm_av_pc_repository_av_pc_CollectionDataType_entity_av_pc_Entity, gen_pcm_av_pc_repository_av_pc_CollectionDataType_repository_av_pc_DataType, gen_pcm_av_pc_repository_av_pc_CompositeDataType_entity_av_pc_Entity, gen_pcm_av_pc_repository_av_pc_CompositeDataType_repository_av_pc_DataType, gen_pcm_av_pc_repository_av_pc_InnerDeclaration_NamedElement, gen_pcm_av_pc_resourcetype_av_pc_ProcessingResourceType_ResourceType, gen_pcm_av_pc_resourcetype_av_pc_ResourceType_entity_av_pc_Entity, gen_pcm_av_pc_resourcetype_av_pc_ResourceType_UnitCarryingElement, gen_pcm_av_pc_resourcetype_av_pc_ResourceType_entity_av_pc_ResourceInterfaceProvidingEntity, gen_pcm_av_pc_resourcetype_av_pc_SchedulingPolicy_Entity, gen_pcm_av_pc_resourcetype_av_pc_CommunicationLinkResourceType_ResourceType, gen_pcm_av_pc_resourcetype_av_pc_ResourceInterface_Entity, gen_pcm_av_pc_parameter_av_pc_CharacterisedVariable_Variable, gen_pcm_av_pc_reliability_av_pc_ExternalFailureOccurrenceDescription_FailureOccurrenceDescription, gen_pcm_av_pc_reliability_av_pc_HardwareInducedFailureType_FailureType, gen_pcm_av_pc_reliability_av_pc_SoftwareInducedFailureType_FailureType, gen_pcm_av_pc_reliability_av_pc_InternalFailureOccurrenceDescription_FailureOccurrenceDescription, gen_pcm_av_pc_reliability_av_pc_NetworkInducedFailureType_FailureType, gen_pcm_av_pc_seff_av_pc_AbstractInternalControlFlowAction_AbstractAction, gen_pcm_av_pc_seff_av_pc_AbstractAction_Entity, gen_pcm_av_pc_reliability_av_pc_ResourceTimeoutFailureType_SoftwareInducedFailureType, gen_pcm_av_pc_reliability_av_pc_FailureType_Entity, gen_pcm_av_pc_seff_av_pc_StopAction_AbstractInternalControlFlowAction, gen_pcm_av_pc_seff_av_pc_AbstractBranchTransition_Entity, gen_pcm_av_pc_seff_av_pc_BranchAction_AbstractInternalControlFlowAction, gen_pcm_av_pc_seff_av_pc_ResourceDemandingBehaviour_Identifier, gen_pcm_av_pc_seff_av_pc_AbstractLoopAction_AbstractInternalControlFlowAction, gen_pcm_av_pc_seff_av_pc_ResourceDemandingSEFF_Identifier, gen_pcm_av_pc_seff_av_pc_ResourceDemandingSEFF_seff_av_pc_ServiceEffectSpecification, gen_pcm_av_pc_seff_av_pc_ResourceDemandingSEFF_seff_av_pc_ResourceDemandingBehaviour, gen_pcm_av_pc_seff_av_pc_StartAction_AbstractInternalControlFlowAction, gen_pcm_av_pc_seff_av_pc_ExternalCallAction_seff_av_pc_AbstractAction, gen_pcm_av_pc_seff_av_pc_ExternalCallAction_seff_av_pc_CallReturnAction, gen_pcm_av_pc_seff_av_pc_ExternalCallAction_seff_reliability_av_pc_FailureHandlingEntity, gen_pcm_av_pc_seff_av_pc_ResourceDemandingInternalBehaviour_ResourceDemandingBehaviour, gen_pcm_av_pc_seff_av_pc_ReleaseAction_AbstractInternalControlFlowAction, gen_pcm_av_pc_seff_av_pc_LoopAction_AbstractLoopAction, gen_pcm_av_pc_seff_av_pc_ForkAction_AbstractInternalControlFlowAction, gen_pcm_av_pc_seff_av_pc_ForkedBehaviour_ResourceDemandingBehaviour, gen_pcm_av_pc_seff_av_pc_CollectionIteratorAction_AbstractLoopAction, gen_pcm_av_pc_seff_av_pc_GuardedBranchTransition_AbstractBranchTransition, gen_pcm_av_pc_seff_av_pc_SetVariableAction_AbstractInternalControlFlowAction, gen_pcm_av_pc_seff_av_pc_CallReturnAction_CallAction, gen_pcm_av_pc_seff_av_pc_ProbabilisticBranchTransition_AbstractBranchTransition, gen_pcm_av_pc_seff_av_pc_AcquireAction_AbstractInternalControlFlowAction, gen_pcm_av_pc_seff_performance_av_pc_InfrastructureCall_CallAction, gen_pcm_av_pc_seff_av_pc_InternalCallAction_seff_av_pc_CallAction, gen_pcm_av_pc_seff_av_pc_InternalCallAction_seff_av_pc_AbstractInternalControlFlowAction, gen_pcm_av_pc_seff_av_pc_EmitEventAction_seff_av_pc_AbstractAction, gen_pcm_av_pc_seff_av_pc_EmitEventAction_seff_av_pc_CallAction, gen_pcm_av_pc_seff_av_pc_InternalAction_AbstractInternalControlFlowAction, gen_pcm_av_pc_seff_performance_av_pc_ResourceCall_CallAction, gen_pcm_av_pc_seff_reliability_av_pc_RecoveryAction_AbstractInternalControlFlowAction, gen_pcm_av_pc_seff_reliability_av_pc_FailureHandlingEntity_Entity, gen_pcm_av_pc_seff_reliability_av_pc_RecoveryActionBehaviour_seff_reliability_av_pc_FailureHandlingEntity, gen_pcm_av_pc_seff_reliability_av_pc_RecoveryActionBehaviour_seff_av_pc_ResourceDemandingBehaviour, gen_pcm_av_pc_qos_performance_av_pc_SystemSpecifiedExecutionTime_SpecifiedExecutionTime, gen_pcm_av_pc_qosannotations_av_pc_QoSAnnotations_Entity, gen_pcm_av_pc_qos_reliability_av_pc_SpecifiedReliabilityAnnotation_SpecifiedQoSAnnotation, gen_pcm_av_pc_qos_performance_av_pc_SpecifiedExecutionTime_SpecifiedQoSAnnotation, gen_pcm_av_pc_qos_performance_av_pc_ComponentSpecifiedExecutionTime_SpecifiedExecutionTime, gen_pcm_av_pc_resourceenvironment_av_pc_ResourceEnvironment_NamedElement, gen_pcm_av_pc_resourceenvironment_av_pc_LinkingResource_Entity, gen_pcm_av_pc_system_av_pc_System_entity_av_pc_Entity, gen_pcm_av_pc_system_av_pc_System_entity_av_pc_ComposedProvidingRequiringEntity, gen_pcm_av_pc_resourceenvironment_av_pc_CommunicationLinkResourceSpecification_Identifier, gen_pcm_av_pc_resourceenvironment_av_pc_ResourceContainer_Entity, gen_pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification_Identifier, gen_pcm_av_pc_allocation_av_pc_Allocation_Entity, gen_pcm_av_pc_allocation_av_pc_AllocationContext_Entity, gen_pcm_av_pc_completions_av_pc_Completion_entity_av_pc_ComposedProvidingRequiringEntity, gen_pcm_av_pc_completions_av_pc_Completion_repository_av_pc_ImplementationComponentType, gen_pcm_av_pc_completions_av_pc_DelegatingExternalCallAction_ExternalCallAction, gen_pcm_av_pc_completions_av_pc_NetworkDemandParametricResourceDemand_ParametricResourceDemand, gen_pcm_av_pc_subsystem_av_pc_SubSystem_entity_av_pc_ComposedProvidingRequiringEntity, gen_pcm_av_pc_subsystem_av_pc_SubSystem_repository_av_pc_RepositoryComponent},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)