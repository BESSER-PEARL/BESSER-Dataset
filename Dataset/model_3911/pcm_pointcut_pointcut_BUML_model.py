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
            EnumerationLiteral(name="NUMBER_OF_ELEMENTS"),
			EnumerationLiteral(name="VALUE"),
			EnumerationLiteral(name="BYTESIZE"),
			EnumerationLiteral(name="TYPE"),
			EnumerationLiteral(name="STRUCTURE")
    }
)

# Classes
seff_performance_pc_pc_ResourceCall = Class(name="seff_performance_pc_pc_ResourceCall")
seff_performance_pc_pc_ParametricResourceDemand = Class(name="seff_performance_pc_pc_ParametricResourceDemand")
LoopAction = Class(name="LoopAction")
GuardedBranchTransition = Class(name="GuardedBranchTransition")
pcm_pc_pc_DummyClass = Class(name="pcm_pc_pc_DummyClass")
pcm_pc_pc_PointcutPointcut = Class(name="pcm_pc_pc_PointcutPointcut")
pcm_pc_pc_EObject = Class(name="pcm_pc_pc_EObject")
pcm_pc_pc_Pointcut = Class(name="pcm_pc_pc_Pointcut")
pcm_pc_pc_core_pc_pc_PCMRandomVariable = Class(name="pcm_pc_pc_core_pc_pc_PCMRandomVariable")
RandomVariable = Class(name="RandomVariable")
ClosedWorkload = Class(name="ClosedWorkload")
PassiveResource = Class(name="PassiveResource")
VariableCharacterisation = Class(name="VariableCharacterisation")
seff_performance_pc_pc_InfrastructureCall = Class(name="seff_performance_pc_pc_InfrastructureCall")
entity_pc_pc_ResourceInterfaceProvidingEntity = Class(name="entity_pc_pc_ResourceInterfaceProvidingEntity")
ResourceInterface = Class(name="ResourceInterface")
pcm_pc_pc_entity_pc_pc_InterfaceProvidingRequiringEntity = Class(name="pcm_pc_pc_entity_pc_pc_InterfaceProvidingRequiringEntity")
entity_pc_pc_InterfaceProvidingEntity = Class(name="entity_pc_pc_InterfaceProvidingEntity")
entity_pc_pc_InterfaceRequiringEntity = Class(name="entity_pc_pc_InterfaceRequiringEntity")
pcm_pc_pc_entity_pc_pc_InterfaceProvidingEntity = Class(name="pcm_pc_pc_entity_pc_pc_InterfaceProvidingEntity")
Entity = Class(name="Entity")
ProvidedRole = Class(name="ProvidedRole")
qos_performance_pc_pc_SpecifiedExecutionTime = Class(name="qos_performance_pc_pc_SpecifiedExecutionTime")
composition_pc_pc_EventChannelSinkConnector = Class(name="composition_pc_pc_EventChannelSinkConnector")
composition_pc_pc_AssemblyEventConnector = Class(name="composition_pc_pc_AssemblyEventConnector")
Loop = Class(name="Loop")
OpenWorkload = Class(name="OpenWorkload")
Delay = Class(name="Delay")
CommunicationLinkResourceSpecification = Class(name="CommunicationLinkResourceSpecification")
ProcessingResourceSpecification = Class(name="ProcessingResourceSpecification")
pcm_pc_pc_entity_pc_pc_ResourceProvidedRole = Class(name="pcm_pc_pc_entity_pc_pc_ResourceProvidedRole")
Role = Class(name="Role")
pcm_pc_pc_entity_pc_pc_ResourceInterfaceProvidingRequiringEntity = Class(name="pcm_pc_pc_entity_pc_pc_ResourceInterfaceProvidingRequiringEntity")
pcm_pc_pc_entity_pc_pc_Entity = Class(name="pcm_pc_pc_entity_pc_pc_Entity")
Identifier = Class(name="Identifier")
entity_pc_pc_NamedElement = Class(name="entity_pc_pc_NamedElement")
pcm_pc_pc_composition_pc_pc_DelegationConnector = Class(name="pcm_pc_pc_composition_pc_pc_DelegationConnector")
Connector = Class(name="Connector")
pcm_pc_pc_composition_pc_pc_Connector = Class(name="pcm_pc_pc_composition_pc_pc_Connector")
pcm_pc_pc_entity_pc_pc_InterfaceRequiringEntity = Class(name="pcm_pc_pc_entity_pc_pc_InterfaceRequiringEntity")
entity_pc_pc_Entity = Class(name="entity_pc_pc_Entity")
entity_pc_pc_ResourceInterfaceRequiringEntity = Class(name="entity_pc_pc_ResourceInterfaceRequiringEntity")
RequiredRole = Class(name="RequiredRole")
pcm_pc_pc_entity_pc_pc_ResourceInterfaceRequiringEntity = Class(name="pcm_pc_pc_entity_pc_pc_ResourceInterfaceRequiringEntity")
entity_pc_pc_ResourceRequiredRole = Class(name="entity_pc_pc_ResourceRequiredRole")
pcm_pc_pc_entity_pc_pc_ResourceRequiredRole = Class(name="pcm_pc_pc_entity_pc_pc_ResourceRequiredRole")
pcm_pc_pc_entity_pc_pc_ResourceInterfaceProvidingEntity = Class(name="pcm_pc_pc_entity_pc_pc_ResourceInterfaceProvidingEntity")
entity_pc_pc_ResourceProvidedRole = Class(name="entity_pc_pc_ResourceProvidedRole")
pcm_pc_pc_entity_pc_pc_ComposedProvidingRequiringEntity = Class(name="pcm_pc_pc_entity_pc_pc_ComposedProvidingRequiringEntity")
composition_pc_pc_ComposedStructure = Class(name="composition_pc_pc_ComposedStructure")
entity_pc_pc_InterfaceProvidingRequiringEntity = Class(name="entity_pc_pc_InterfaceProvidingRequiringEntity")
pcm_pc_pc_entity_pc_pc_NamedElement = Class(name="pcm_pc_pc_entity_pc_pc_NamedElement")
composition_pc_pc_ResourceRequiredDelegationConnector = Class(name="composition_pc_pc_ResourceRequiredDelegationConnector")
composition_pc_pc_EventChannel = Class(name="composition_pc_pc_EventChannel")
composition_pc_pc_Connector = Class(name="composition_pc_pc_Connector")
pcm_pc_pc_composition_pc_pc_ResourceRequiredDelegationConnector = Class(name="pcm_pc_pc_composition_pc_pc_ResourceRequiredDelegationConnector")
pcm_pc_pc_composition_pc_pc_ComposedStructure = Class(name="pcm_pc_pc_composition_pc_pc_ComposedStructure")
composition_pc_pc_AssemblyContext = Class(name="composition_pc_pc_AssemblyContext")
pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector = Class(name="pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector")
DelegationConnector = Class(name="DelegationConnector")
pcm_pc_pc_composition_pc_pc_EventChannel = Class(name="pcm_pc_pc_composition_pc_pc_EventChannel")
EventGroup = Class(name="EventGroup")
composition_pc_pc_EventChannelSourceConnector = Class(name="composition_pc_pc_EventChannelSourceConnector")
pcm_pc_pc_composition_pc_pc_EventChannelSourceConnector = Class(name="pcm_pc_pc_composition_pc_pc_EventChannelSourceConnector")
SourceRole = Class(name="SourceRole")
pcm_pc_pc_composition_pc_pc_EventChannelSinkConnector = Class(name="pcm_pc_pc_composition_pc_pc_EventChannelSinkConnector")
SinkRole = Class(name="SinkRole")
PCMRandomVariable = Class(name="PCMRandomVariable")
OperationRequiredRole = Class(name="OperationRequiredRole")
pcm_pc_pc_composition_pc_pc_AssemblyConnector = Class(name="pcm_pc_pc_composition_pc_pc_AssemblyConnector")
OperationProvidedRole = Class(name="OperationProvidedRole")
pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector = Class(name="pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector")
pcm_pc_pc_composition_pc_pc_SourceDelegationConnector = Class(name="pcm_pc_pc_composition_pc_pc_SourceDelegationConnector")
pcm_pc_pc_composition_pc_pc_SinkDelegationConnector = Class(name="pcm_pc_pc_composition_pc_pc_SinkDelegationConnector")
pcm_pc_pc_composition_pc_pc_AssemblyInfrastructureConnector = Class(name="pcm_pc_pc_composition_pc_pc_AssemblyInfrastructureConnector")
InfrastructureProvidedRole = Class(name="InfrastructureProvidedRole")
InfrastructureRequiredRole = Class(name="InfrastructureRequiredRole")
pcm_pc_pc_composition_pc_pc_AssemblyEventConnector = Class(name="pcm_pc_pc_composition_pc_pc_AssemblyEventConnector")
pcm_pc_pc_composition_pc_pc_RequiredResourceDelegationConnector = Class(name="pcm_pc_pc_composition_pc_pc_RequiredResourceDelegationConnector")
pcm_pc_pc_composition_pc_pc_AssemblyContext = Class(name="pcm_pc_pc_composition_pc_pc_AssemblyContext")
RepositoryComponent = Class(name="RepositoryComponent")
VariableUsage = Class(name="VariableUsage")
pcm_pc_pc_usagemodel_pc_pc_Workload = Class(name="pcm_pc_pc_usagemodel_pc_pc_Workload")
UsageScenario = Class(name="UsageScenario")
pcm_pc_pc_usagemodel_pc_pc_UsageScenario = Class(name="pcm_pc_pc_usagemodel_pc_pc_UsageScenario")
UsageModel = Class(name="UsageModel")
pcm_pc_pc_composition_pc_pc_ProvidedInfrastructureDelegationConnector = Class(name="pcm_pc_pc_composition_pc_pc_ProvidedInfrastructureDelegationConnector")
pcm_pc_pc_composition_pc_pc_RequiredInfrastructureDelegationConnector = Class(name="pcm_pc_pc_composition_pc_pc_RequiredInfrastructureDelegationConnector")
pcm_pc_pc_usagemodel_pc_pc_UsageModel = Class(name="pcm_pc_pc_usagemodel_pc_pc_UsageModel")
UserData = Class(name="UserData")
pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall = Class(name="pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall")
AbstractUserAction = Class(name="AbstractUserAction")
OperationSignature = Class(name="OperationSignature")
pcm_pc_pc_usagemodel_pc_pc_AbstractUserAction = Class(name="pcm_pc_pc_usagemodel_pc_pc_AbstractUserAction")
ScenarioBehaviour = Class(name="ScenarioBehaviour")
Workload = Class(name="Workload")
pcm_pc_pc_usagemodel_pc_pc_UserData = Class(name="pcm_pc_pc_usagemodel_pc_pc_UserData")
BranchTransition = Class(name="BranchTransition")
pcm_pc_pc_usagemodel_pc_pc_BranchTransition = Class(name="pcm_pc_pc_usagemodel_pc_pc_BranchTransition")
pcm_pc_pc_usagemodel_pc_pc_ScenarioBehaviour = Class(name="pcm_pc_pc_usagemodel_pc_pc_ScenarioBehaviour")
pcm_pc_pc_usagemodel_pc_pc_Loop = Class(name="pcm_pc_pc_usagemodel_pc_pc_Loop")
pcm_pc_pc_usagemodel_pc_pc_Stop = Class(name="pcm_pc_pc_usagemodel_pc_pc_Stop")
pcm_pc_pc_usagemodel_pc_pc_Start = Class(name="pcm_pc_pc_usagemodel_pc_pc_Start")
pcm_pc_pc_usagemodel_pc_pc_OpenWorkload = Class(name="pcm_pc_pc_usagemodel_pc_pc_OpenWorkload")
Branch = Class(name="Branch")
pcm_pc_pc_usagemodel_pc_pc_Branch = Class(name="pcm_pc_pc_usagemodel_pc_pc_Branch")
pcm_pc_pc_usagemodel_pc_pc_ClosedWorkload = Class(name="pcm_pc_pc_usagemodel_pc_pc_ClosedWorkload")
pcm_pc_pc_repository_pc_pc_PassiveResource = Class(name="pcm_pc_pc_repository_pc_pc_PassiveResource")
BasicComponent = Class(name="BasicComponent")
ResourceTimeoutFailureType = Class(name="ResourceTimeoutFailureType")
pcm_pc_pc_usagemodel_pc_pc_Delay = Class(name="pcm_pc_pc_usagemodel_pc_pc_Delay")
ServiceEffectSpecification = Class(name="ServiceEffectSpecification")
pcm_pc_pc_repository_pc_pc_ImplementationComponentType = Class(name="pcm_pc_pc_repository_pc_pc_ImplementationComponentType")
pcm_pc_pc_repository_pc_pc_BasicComponent = Class(name="pcm_pc_pc_repository_pc_pc_BasicComponent")
ImplementationComponentType = Class(name="ImplementationComponentType")
CompleteComponentType = Class(name="CompleteComponentType")
pcm_pc_pc_repository_pc_pc_RepositoryComponent = Class(name="pcm_pc_pc_repository_pc_pc_RepositoryComponent")
InterfaceProvidingRequiringEntity = Class(name="InterfaceProvidingRequiringEntity")
Repository = Class(name="Repository")
pcm_pc_pc_repository_pc_pc_ProvidedRole = Class(name="pcm_pc_pc_repository_pc_pc_ProvidedRole")
pcm_pc_pc_repository_pc_pc_Parameter = Class(name="pcm_pc_pc_repository_pc_pc_Parameter")
DataType = Class(name="DataType")
InfrastructureSignature = Class(name="InfrastructureSignature")
EventType = Class(name="EventType")
pcm_pc_pc_repository_pc_pc_Repository = Class(name="pcm_pc_pc_repository_pc_pc_Repository")
Interface = Class(name="Interface")
FailureType = Class(name="FailureType")
pcm_pc_pc_repository_pc_pc_Interface = Class(name="pcm_pc_pc_repository_pc_pc_Interface")
Protocol = Class(name="Protocol")
ResourceSignature = Class(name="ResourceSignature")
pcm_pc_pc_repository_pc_pc_DataType = Class(name="pcm_pc_pc_repository_pc_pc_DataType")
pcm_pc_pc_repository_pc_pc_RequiredCharacterisation = Class(name="pcm_pc_pc_repository_pc_pc_RequiredCharacterisation")
Parameter_ = Class(name="Parameter")
pcm_pc_pc_repository_pc_pc_EventGroup = Class(name="pcm_pc_pc_repository_pc_pc_EventGroup")
pcm_pc_pc_repository_pc_pc_EventType = Class(name="pcm_pc_pc_repository_pc_pc_EventType")
Signature = Class(name="Signature")
pcm_pc_pc_repository_pc_pc_Signature = Class(name="pcm_pc_pc_repository_pc_pc_Signature")
ExceptionType = Class(name="ExceptionType")
pcm_pc_pc_repository_pc_pc_ExceptionType = Class(name="pcm_pc_pc_repository_pc_pc_ExceptionType")
pcm_pc_pc_repository_pc_pc_InfrastructureSignature = Class(name="pcm_pc_pc_repository_pc_pc_InfrastructureSignature")
InfrastructureInterface = Class(name="InfrastructureInterface")
pcm_pc_pc_repository_pc_pc_InfrastructureInterface = Class(name="pcm_pc_pc_repository_pc_pc_InfrastructureInterface")
RequiredCharacterisation = Class(name="RequiredCharacterisation")
pcm_pc_pc_repository_pc_pc_OperationSignature = Class(name="pcm_pc_pc_repository_pc_pc_OperationSignature")
OperationInterface = Class(name="OperationInterface")
pcm_pc_pc_repository_pc_pc_OperationInterface = Class(name="pcm_pc_pc_repository_pc_pc_OperationInterface")
pcm_pc_pc_repository_pc_pc_OperationRequiredRole = Class(name="pcm_pc_pc_repository_pc_pc_OperationRequiredRole")
pcm_pc_pc_repository_pc_pc_SourceRole = Class(name="pcm_pc_pc_repository_pc_pc_SourceRole")
pcm_pc_pc_repository_pc_pc_InfrastructureRequiredRole = Class(name="pcm_pc_pc_repository_pc_pc_InfrastructureRequiredRole")
pcm_pc_pc_repository_pc_pc_RequiredRole = Class(name="pcm_pc_pc_repository_pc_pc_RequiredRole")
pcm_pc_pc_repository_pc_pc_OperationProvidedRole = Class(name="pcm_pc_pc_repository_pc_pc_OperationProvidedRole")
pcm_pc_pc_repository_pc_pc_InfrastructureProvidedRole = Class(name="pcm_pc_pc_repository_pc_pc_InfrastructureProvidedRole")
pcm_pc_pc_repository_pc_pc_CompleteComponentType = Class(name="pcm_pc_pc_repository_pc_pc_CompleteComponentType")
ProvidesComponentType = Class(name="ProvidesComponentType")
pcm_pc_pc_repository_pc_pc_ProvidesComponentType = Class(name="pcm_pc_pc_repository_pc_pc_ProvidesComponentType")
pcm_pc_pc_repository_pc_pc_SinkRole = Class(name="pcm_pc_pc_repository_pc_pc_SinkRole")
pcm_pc_pc_repository_pc_pc_PrimitiveDataType = Class(name="pcm_pc_pc_repository_pc_pc_PrimitiveDataType")
pcm_pc_pc_repository_pc_pc_CollectionDataType = Class(name="pcm_pc_pc_repository_pc_pc_CollectionDataType")
repository_pc_pc_DataType = Class(name="repository_pc_pc_DataType")
pcm_pc_pc_repository_pc_pc_CompositeDataType = Class(name="pcm_pc_pc_repository_pc_pc_CompositeDataType")
pcm_pc_pc_repository_pc_pc_CompositeComponent = Class(name="pcm_pc_pc_repository_pc_pc_CompositeComponent")
entity_pc_pc_ComposedProvidingRequiringEntity = Class(name="entity_pc_pc_ComposedProvidingRequiringEntity")
repository_pc_pc_ImplementationComponentType = Class(name="repository_pc_pc_ImplementationComponentType")
InnerDeclaration = Class(name="InnerDeclaration")
pcm_pc_pc_repository_pc_pc_InnerDeclaration = Class(name="pcm_pc_pc_repository_pc_pc_InnerDeclaration")
NamedElement = Class(name="NamedElement")
pcm_pc_pc_repository_pc_pc_Role = Class(name="pcm_pc_pc_repository_pc_pc_Role")
pcm_pc_pc_resourcetype_pc_pc_ResourceSignature = Class(name="pcm_pc_pc_resourcetype_pc_pc_ResourceSignature")
pcm_pc_pc_resourcetype_pc_pc_ProcessingResourceType = Class(name="pcm_pc_pc_resourcetype_pc_pc_ProcessingResourceType")
ResourceType = Class(name="ResourceType")
HardwareInducedFailureType = Class(name="HardwareInducedFailureType")
pcm_pc_pc_resourcetype_pc_pc_ResourceType = Class(name="pcm_pc_pc_resourcetype_pc_pc_ResourceType")
UnitCarryingElement = Class(name="UnitCarryingElement")
CompositeDataType = Class(name="CompositeDataType")
pcm_pc_pc_resourcetype_pc_pc_ResourceRepository = Class(name="pcm_pc_pc_resourcetype_pc_pc_ResourceRepository")
SchedulingPolicy = Class(name="SchedulingPolicy")
pcm_pc_pc_resourcetype_pc_pc_SchedulingPolicy = Class(name="pcm_pc_pc_resourcetype_pc_pc_SchedulingPolicy")
pcm_pc_pc_resourcetype_pc_pc_CommunicationLinkResourceType = Class(name="pcm_pc_pc_resourcetype_pc_pc_CommunicationLinkResourceType")
NetworkInducedFailureType = Class(name="NetworkInducedFailureType")
pcm_pc_pc_resourcetype_pc_pc_ResourceInterface = Class(name="pcm_pc_pc_resourcetype_pc_pc_ResourceInterface")
pcm_pc_pc_protocol_pc_pc_Protocol = Class(name="pcm_pc_pc_protocol_pc_pc_Protocol")
ResourceRepository = Class(name="ResourceRepository")
CallAction = Class(name="CallAction")
SynchronisationPoint = Class(name="SynchronisationPoint")
CallReturnAction = Class(name="CallReturnAction")
SetVariableAction = Class(name="SetVariableAction")
SpecifiedOutputParameterAbstraction = Class(name="SpecifiedOutputParameterAbstraction")
EntryLevelSystemCall = Class(name="EntryLevelSystemCall")
parameter_pc_pc_pcm_pc_pc_AbstractNamedReference = Class(name="parameter_pc_pc_pcm_pc_pc_AbstractNamedReference")
pcm_pc_pc_parameter_pc_pc_VariableCharacterisation = Class(name="pcm_pc_pc_parameter_pc_pc_VariableCharacterisation")
pcm_pc_pc_parameter_pc_pc_VariableUsage = Class(name="pcm_pc_pc_parameter_pc_pc_VariableUsage")
pcm_pc_pc_reliability_pc_pc_FailureOccurrenceDescription = Class(name="pcm_pc_pc_reliability_pc_pc_FailureOccurrenceDescription")
pcm_pc_pc_reliability_pc_pc_HardwareInducedFailureType = Class(name="pcm_pc_pc_reliability_pc_pc_HardwareInducedFailureType")
pcm_pc_pc_parameter_pc_pc_CharacterisedVariable = Class(name="pcm_pc_pc_parameter_pc_pc_CharacterisedVariable")
Variable = Class(name="Variable")
InternalFailureOccurrenceDescription = Class(name="InternalFailureOccurrenceDescription")
pcm_pc_pc_reliability_pc_pc_InternalFailureOccurrenceDescription = Class(name="pcm_pc_pc_reliability_pc_pc_InternalFailureOccurrenceDescription")
FailureOccurrenceDescription = Class(name="FailureOccurrenceDescription")
InternalAction = Class(name="InternalAction")
SoftwareInducedFailureType = Class(name="SoftwareInducedFailureType")
pcm_pc_pc_reliability_pc_pc_NetworkInducedFailureType = Class(name="pcm_pc_pc_reliability_pc_pc_NetworkInducedFailureType")
CommunicationLinkResourceType = Class(name="CommunicationLinkResourceType")
pcm_pc_pc_reliability_pc_pc_ExternalFailureOccurrenceDescription = Class(name="pcm_pc_pc_reliability_pc_pc_ExternalFailureOccurrenceDescription")
ProcessingResourceType = Class(name="ProcessingResourceType")
pcm_pc_pc_reliability_pc_pc_SoftwareInducedFailureType = Class(name="pcm_pc_pc_reliability_pc_pc_SoftwareInducedFailureType")
pcm_pc_pc_reliability_pc_pc_ResourceTimeoutFailureType = Class(name="pcm_pc_pc_reliability_pc_pc_ResourceTimeoutFailureType")
pcm_pc_pc_reliability_pc_pc_FailureType = Class(name="pcm_pc_pc_reliability_pc_pc_FailureType")
pcm_pc_pc_seff_pc_pc_StopAction = Class(name="pcm_pc_pc_seff_pc_pc_StopAction")
AbstractInternalControlFlowAction = Class(name="AbstractInternalControlFlowAction")
pcm_pc_pc_seff_pc_pc_AbstractInternalControlFlowAction = Class(name="pcm_pc_pc_seff_pc_pc_AbstractInternalControlFlowAction")
AbstractAction = Class(name="AbstractAction")
pcm_pc_pc_seff_pc_pc_AbstractAction = Class(name="pcm_pc_pc_seff_pc_pc_AbstractAction")
qos_reliability_pc_pc_SpecifiedReliabilityAnnotation = Class(name="qos_reliability_pc_pc_SpecifiedReliabilityAnnotation")
AbstractLoopAction = Class(name="AbstractLoopAction")
AbstractBranchTransition = Class(name="AbstractBranchTransition")
pcm_pc_pc_seff_pc_pc_AbstractLoopAction = Class(name="pcm_pc_pc_seff_pc_pc_AbstractLoopAction")
pcm_pc_pc_seff_pc_pc_AbstractBranchTransition = Class(name="pcm_pc_pc_seff_pc_pc_AbstractBranchTransition")
BranchAction = Class(name="BranchAction")
ResourceDemandingBehaviour = Class(name="ResourceDemandingBehaviour")
pcm_pc_pc_seff_pc_pc_ResourceDemandingBehaviour = Class(name="pcm_pc_pc_seff_pc_pc_ResourceDemandingBehaviour")
pcm_pc_pc_seff_pc_pc_CallAction = Class(name="pcm_pc_pc_seff_pc_pc_CallAction")
pcm_pc_pc_seff_pc_pc_StartAction = Class(name="pcm_pc_pc_seff_pc_pc_StartAction")
pcm_pc_pc_seff_pc_pc_ServiceEffectSpecification = Class(name="pcm_pc_pc_seff_pc_pc_ServiceEffectSpecification")
pcm_pc_pc_seff_pc_pc_BranchAction = Class(name="pcm_pc_pc_seff_pc_pc_BranchAction")
pcm_pc_pc_seff_pc_pc_ResourceDemandingInternalBehaviour = Class(name="pcm_pc_pc_seff_pc_pc_ResourceDemandingInternalBehaviour")
ResourceDemandingSEFF = Class(name="ResourceDemandingSEFF")
pcm_pc_pc_seff_pc_pc_ReleaseAction = Class(name="pcm_pc_pc_seff_pc_pc_ReleaseAction")
pcm_pc_pc_seff_pc_pc_LoopAction = Class(name="pcm_pc_pc_seff_pc_pc_LoopAction")
pcm_pc_pc_seff_pc_pc_ForkAction = Class(name="pcm_pc_pc_seff_pc_pc_ForkAction")
ForkedBehaviour = Class(name="ForkedBehaviour")
pcm_pc_pc_seff_pc_pc_ForkedBehaviour = Class(name="pcm_pc_pc_seff_pc_pc_ForkedBehaviour")
ForkAction = Class(name="ForkAction")
pcm_pc_pc_seff_pc_pc_SynchronisationPoint = Class(name="pcm_pc_pc_seff_pc_pc_SynchronisationPoint")
pcm_pc_pc_seff_pc_pc_ResourceDemandingSEFF = Class(name="pcm_pc_pc_seff_pc_pc_ResourceDemandingSEFF")
seff_pc_pc_ServiceEffectSpecification = Class(name="seff_pc_pc_ServiceEffectSpecification")
seff_pc_pc_ResourceDemandingBehaviour = Class(name="seff_pc_pc_ResourceDemandingBehaviour")
ResourceDemandingInternalBehaviour = Class(name="ResourceDemandingInternalBehaviour")
seff_reliability_pc_pc_FailureHandlingEntity = Class(name="seff_reliability_pc_pc_FailureHandlingEntity")
pcm_pc_pc_seff_pc_pc_CallReturnAction = Class(name="pcm_pc_pc_seff_pc_pc_CallReturnAction")
pcm_pc_pc_seff_pc_pc_ExternalCallAction = Class(name="pcm_pc_pc_seff_pc_pc_ExternalCallAction")
seff_pc_pc_AbstractAction = Class(name="seff_pc_pc_AbstractAction")
seff_pc_pc_CallReturnAction = Class(name="seff_pc_pc_CallReturnAction")
pcm_pc_pc_seff_pc_pc_CollectionIteratorAction = Class(name="pcm_pc_pc_seff_pc_pc_CollectionIteratorAction")
pcm_pc_pc_seff_pc_pc_GuardedBranchTransition = Class(name="pcm_pc_pc_seff_pc_pc_GuardedBranchTransition")
pcm_pc_pc_seff_pc_pc_SetVariableAction = Class(name="pcm_pc_pc_seff_pc_pc_SetVariableAction")
pcm_pc_pc_seff_pc_pc_InternalCallAction = Class(name="pcm_pc_pc_seff_pc_pc_InternalCallAction")
seff_pc_pc_CallAction = Class(name="seff_pc_pc_CallAction")
seff_pc_pc_AbstractInternalControlFlowAction = Class(name="seff_pc_pc_AbstractInternalControlFlowAction")
pcm_pc_pc_seff_pc_pc_EmitEventAction = Class(name="pcm_pc_pc_seff_pc_pc_EmitEventAction")
pcm_pc_pc_seff_pc_pc_InternalAction = Class(name="pcm_pc_pc_seff_pc_pc_InternalAction")
pcm_pc_pc_seff_pc_pc_ProbabilisticBranchTransition = Class(name="pcm_pc_pc_seff_pc_pc_ProbabilisticBranchTransition")
pcm_pc_pc_seff_pc_pc_AcquireAction = Class(name="pcm_pc_pc_seff_pc_pc_AcquireAction")
pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall = Class(name="pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall")
pcm_pc_pc_seff_performance_pc_pc_ParametricResourceDemand = Class(name="pcm_pc_pc_seff_performance_pc_pc_ParametricResourceDemand")
pcm_pc_pc_seff_reliability_pc_pc_RecoveryActionBehaviour = Class(name="pcm_pc_pc_seff_reliability_pc_pc_RecoveryActionBehaviour")
pcm_pc_pc_seff_performance_pc_pc_ResourceCall = Class(name="pcm_pc_pc_seff_performance_pc_pc_ResourceCall")
seff_reliability_pc_pc_RecoveryActionBehaviour = Class(name="seff_reliability_pc_pc_RecoveryActionBehaviour")
seff_reliability_pc_pc_RecoveryAction = Class(name="seff_reliability_pc_pc_RecoveryAction")
pcm_pc_pc_seff_reliability_pc_pc_RecoveryAction = Class(name="pcm_pc_pc_seff_reliability_pc_pc_RecoveryAction")
pcm_pc_pc_seff_reliability_pc_pc_FailureHandlingEntity = Class(name="pcm_pc_pc_seff_reliability_pc_pc_FailureHandlingEntity")
pcm_pc_pc_qosannotations_pc_pc_SpecifiedQoSAnnotation = Class(name="pcm_pc_pc_qosannotations_pc_pc_SpecifiedQoSAnnotation")
System = Class(name="System")
SpecifiedQoSAnnotation = Class(name="SpecifiedQoSAnnotation")
pcm_pc_pc_qosannotations_pc_pc_SpecifiedOutputParameterAbstraction = Class(name="pcm_pc_pc_qosannotations_pc_pc_SpecifiedOutputParameterAbstraction")
pcm_pc_pc_qos_performance_pc_pc_SystemSpecifiedExecutionTime = Class(name="pcm_pc_pc_qos_performance_pc_pc_SystemSpecifiedExecutionTime")
SpecifiedExecutionTime = Class(name="SpecifiedExecutionTime")
pcm_pc_pc_qos_performance_pc_pc_SpecifiedExecutionTime = Class(name="pcm_pc_pc_qos_performance_pc_pc_SpecifiedExecutionTime")
QoSAnnotations = Class(name="QoSAnnotations")
pcm_pc_pc_qosannotations_pc_pc_QoSAnnotations = Class(name="pcm_pc_pc_qosannotations_pc_pc_QoSAnnotations")
ExternalFailureOccurrenceDescription = Class(name="ExternalFailureOccurrenceDescription")
pcm_pc_pc_system_pc_pc_System = Class(name="pcm_pc_pc_system_pc_pc_System")
pcm_pc_pc_qos_performance_pc_pc_ComponentSpecifiedExecutionTime = Class(name="pcm_pc_pc_qos_performance_pc_pc_ComponentSpecifiedExecutionTime")
pcm_pc_pc_qos_reliability_pc_pc_SpecifiedReliabilityAnnotation = Class(name="pcm_pc_pc_qos_reliability_pc_pc_SpecifiedReliabilityAnnotation")
ResourceEnvironment = Class(name="ResourceEnvironment")
pcm_pc_pc_resourceenvironment_pc_pc_ResourceContainer = Class(name="pcm_pc_pc_resourceenvironment_pc_pc_ResourceContainer")
pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification = Class(name="pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification")
pcm_pc_pc_resourceenvironment_pc_pc_ResourceEnvironment = Class(name="pcm_pc_pc_resourceenvironment_pc_pc_ResourceEnvironment")
LinkingResource = Class(name="LinkingResource")
ResourceContainer = Class(name="ResourceContainer")
pcm_pc_pc_resourceenvironment_pc_pc_LinkingResource = Class(name="pcm_pc_pc_resourceenvironment_pc_pc_LinkingResource")
pcm_pc_pc_allocation_pc_pc_AllocationContext = Class(name="pcm_pc_pc_allocation_pc_pc_AllocationContext")
pcm_pc_pc_resourceenvironment_pc_pc_CommunicationLinkResourceSpecification = Class(name="pcm_pc_pc_resourceenvironment_pc_pc_CommunicationLinkResourceSpecification")
pcm_pc_pc_allocation_pc_pc_Allocation = Class(name="pcm_pc_pc_allocation_pc_pc_Allocation")
AllocationContext = Class(name="AllocationContext")
pcm_pc_pc_subsystem_pc_pc_SubSystem = Class(name="pcm_pc_pc_subsystem_pc_pc_SubSystem")
repository_pc_pc_RepositoryComponent = Class(name="repository_pc_pc_RepositoryComponent")
pcm_pc_pc_completions_pc_pc_Completion = Class(name="pcm_pc_pc_completions_pc_pc_Completion")
pcm_pc_pc_completions_pc_pc_CompletionRepository = Class(name="pcm_pc_pc_completions_pc_pc_CompletionRepository")
Completion = Class(name="Completion")
Allocation = Class(name="Allocation")
pcm_pc_pc_completions_pc_pc_DelegatingExternalCallAction = Class(name="pcm_pc_pc_completions_pc_pc_DelegatingExternalCallAction")
ExternalCallAction = Class(name="ExternalCallAction")
pcm_pc_pc_completions_pc_pc_NetworkDemandParametricResourceDemand = Class(name="pcm_pc_pc_completions_pc_pc_NetworkDemandParametricResourceDemand")
ParametricResourceDemand = Class(name="ParametricResourceDemand")

# seff_performance_pc_pc_ResourceCall class attributes and methods

# seff_performance_pc_pc_ParametricResourceDemand class attributes and methods

# LoopAction class attributes and methods

# GuardedBranchTransition class attributes and methods

# pcm_pc_pc_DummyClass class attributes and methods

# pcm_pc_pc_PointcutPointcut class attributes and methods

# pcm_pc_pc_EObject class attributes and methods

# pcm_pc_pc_Pointcut class attributes and methods

# pcm_pc_pc_core_pc_pc_PCMRandomVariable class attributes and methods
pcm_pc_pc_core_pc_pc_PCMRandomVariable_m_SpecificationMustNotBeNULL: Method = Method(name="SpecificationMustNotBeNULL", parameters={Parameter(name='pcm_pc_pc_diagnostics', type=StringType), Parameter(name='pcm_pc_pc_context', type=StringType)}, type=BooleanType)
pcm_pc_pc_core_pc_pc_PCMRandomVariable.methods={pcm_pc_pc_core_pc_pc_PCMRandomVariable_m_SpecificationMustNotBeNULL}

# RandomVariable class attributes and methods

# ClosedWorkload class attributes and methods

# PassiveResource class attributes and methods

# VariableCharacterisation class attributes and methods

# seff_performance_pc_pc_InfrastructureCall class attributes and methods

# entity_pc_pc_ResourceInterfaceProvidingEntity class attributes and methods

# ResourceInterface class attributes and methods

# pcm_pc_pc_entity_pc_pc_InterfaceProvidingRequiringEntity class attributes and methods

# entity_pc_pc_InterfaceProvidingEntity class attributes and methods

# entity_pc_pc_InterfaceRequiringEntity class attributes and methods

# pcm_pc_pc_entity_pc_pc_InterfaceProvidingEntity class attributes and methods

# Entity class attributes and methods

# ProvidedRole class attributes and methods

# qos_performance_pc_pc_SpecifiedExecutionTime class attributes and methods

# composition_pc_pc_EventChannelSinkConnector class attributes and methods

# composition_pc_pc_AssemblyEventConnector class attributes and methods

# Loop class attributes and methods

# OpenWorkload class attributes and methods

# Delay class attributes and methods

# CommunicationLinkResourceSpecification class attributes and methods

# ProcessingResourceSpecification class attributes and methods

# pcm_pc_pc_entity_pc_pc_ResourceProvidedRole class attributes and methods

# Role class attributes and methods

# pcm_pc_pc_entity_pc_pc_ResourceInterfaceProvidingRequiringEntity class attributes and methods

# pcm_pc_pc_entity_pc_pc_Entity class attributes and methods

# Identifier class attributes and methods

# entity_pc_pc_NamedElement class attributes and methods

# pcm_pc_pc_composition_pc_pc_DelegationConnector class attributes and methods

# Connector class attributes and methods

# pcm_pc_pc_composition_pc_pc_Connector class attributes and methods

# pcm_pc_pc_entity_pc_pc_InterfaceRequiringEntity class attributes and methods

# entity_pc_pc_Entity class attributes and methods

# entity_pc_pc_ResourceInterfaceRequiringEntity class attributes and methods

# RequiredRole class attributes and methods

# pcm_pc_pc_entity_pc_pc_ResourceInterfaceRequiringEntity class attributes and methods

# entity_pc_pc_ResourceRequiredRole class attributes and methods

# pcm_pc_pc_entity_pc_pc_ResourceRequiredRole class attributes and methods

# pcm_pc_pc_entity_pc_pc_ResourceInterfaceProvidingEntity class attributes and methods

# entity_pc_pc_ResourceProvidedRole class attributes and methods

# pcm_pc_pc_entity_pc_pc_ComposedProvidingRequiringEntity class attributes and methods
pcm_pc_pc_entity_pc_pc_ComposedProvidingRequiringEntity_m_ProvidedRolesMustBeBound: Method = Method(name="ProvidedRolesMustBeBound", parameters={Parameter(name='pcm_pc_pc_diagnostics', type=StringType), Parameter(name='pcm_pc_pc_context', type=StringType)}, type=BooleanType)
pcm_pc_pc_entity_pc_pc_ComposedProvidingRequiringEntity.methods={pcm_pc_pc_entity_pc_pc_ComposedProvidingRequiringEntity_m_ProvidedRolesMustBeBound}

# composition_pc_pc_ComposedStructure class attributes and methods

# entity_pc_pc_InterfaceProvidingRequiringEntity class attributes and methods

# pcm_pc_pc_entity_pc_pc_NamedElement class attributes and methods
pcm_pc_pc_entity_pc_pc_NamedElement_entityName: Property = Property(name="entityName", type=StringType)
pcm_pc_pc_entity_pc_pc_NamedElement.attributes={pcm_pc_pc_entity_pc_pc_NamedElement_entityName}

# composition_pc_pc_ResourceRequiredDelegationConnector class attributes and methods

# composition_pc_pc_EventChannel class attributes and methods

# composition_pc_pc_Connector class attributes and methods

# pcm_pc_pc_composition_pc_pc_ResourceRequiredDelegationConnector class attributes and methods

# pcm_pc_pc_composition_pc_pc_ComposedStructure class attributes and methods
pcm_pc_pc_composition_pc_pc_ComposedStructure_m_MultipleConnectorsConstraint: Method = Method(name="MultipleConnectorsConstraint", parameters={Parameter(name='pcm_pc_pc_context', type=StringType), Parameter(name='pcm_pc_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_pc_composition_pc_pc_ComposedStructure_m_MultipleConnectorsConstraintForAssemblyConnectors: Method = Method(name="MultipleConnectorsConstraintForAssemblyConnectors", parameters={Parameter(name='pcm_pc_pc_context', type=StringType), Parameter(name='pcm_pc_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_pc_composition_pc_pc_ComposedStructure.methods={pcm_pc_pc_composition_pc_pc_ComposedStructure_m_MultipleConnectorsConstraintForAssemblyConnectors, pcm_pc_pc_composition_pc_pc_ComposedStructure_m_MultipleConnectorsConstraint}

# composition_pc_pc_AssemblyContext class attributes and methods

# pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector class attributes and methods
pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector_m_ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure: Method = Method(name="ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure", parameters={Parameter(name='pcm_pc_pc_context', type=StringType), Parameter(name='pcm_pc_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector_m_ComponentOfAssemblyContextAndInnerRoleProvidingComponentNeedToBeTheSame: Method = Method(name="ComponentOfAssemblyContextAndInnerRoleProvidingComponentNeedToBeTheSame", parameters={Parameter(name='pcm_pc_pc_diagnostics', type=StringType), Parameter(name='pcm_pc_pc_context', type=StringType)}, type=BooleanType)
pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector.methods={pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector_m_ComponentOfAssemblyContextAndInnerRoleProvidingComponentNeedToBeTheSame, pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector_m_ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure}

# DelegationConnector class attributes and methods

# pcm_pc_pc_composition_pc_pc_EventChannel class attributes and methods

# EventGroup class attributes and methods

# composition_pc_pc_EventChannelSourceConnector class attributes and methods

# pcm_pc_pc_composition_pc_pc_EventChannelSourceConnector class attributes and methods

# SourceRole class attributes and methods

# pcm_pc_pc_composition_pc_pc_EventChannelSinkConnector class attributes and methods

# SinkRole class attributes and methods

# PCMRandomVariable class attributes and methods

# OperationRequiredRole class attributes and methods

# pcm_pc_pc_composition_pc_pc_AssemblyConnector class attributes and methods
pcm_pc_pc_composition_pc_pc_AssemblyConnector_m_AssemblyConnectorsReferencedProvidedRolesAndChildContextMustMatch: Method = Method(name="AssemblyConnectorsReferencedProvidedRolesAndChildContextMustMatch", parameters={Parameter(name='pcm_pc_pc_context', type=StringType), Parameter(name='pcm_pc_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_pc_composition_pc_pc_AssemblyConnector_m_AssemblyConnectorsReferencedRequiredRoleAndChildContextMustMatch: Method = Method(name="AssemblyConnectorsReferencedRequiredRoleAndChildContextMustMatch", parameters={Parameter(name='pcm_pc_pc_context', type=StringType), Parameter(name='pcm_pc_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_pc_composition_pc_pc_AssemblyConnector_m_AssemblyConnectorsReferencedInterfacesMustMatch: Method = Method(name="AssemblyConnectorsReferencedInterfacesMustMatch", parameters={Parameter(name='pcm_pc_pc_diagnostics', type=StringType), Parameter(name='pcm_pc_pc_context', type=StringType)}, type=BooleanType)
pcm_pc_pc_composition_pc_pc_AssemblyConnector.methods={pcm_pc_pc_composition_pc_pc_AssemblyConnector_m_AssemblyConnectorsReferencedRequiredRoleAndChildContextMustMatch, pcm_pc_pc_composition_pc_pc_AssemblyConnector_m_AssemblyConnectorsReferencedProvidedRolesAndChildContextMustMatch, pcm_pc_pc_composition_pc_pc_AssemblyConnector_m_AssemblyConnectorsReferencedInterfacesMustMatch}

# OperationProvidedRole class attributes and methods

# pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector class attributes and methods
pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector_m_RequiredDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure: Method = Method(name="RequiredDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure", parameters={Parameter(name='pcm_pc_pc_context', type=StringType), Parameter(name='pcm_pc_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector_m_ComponentOfAssemblyContextAndInnerRoleRequiringComponentNeedToBeTheSame: Method = Method(name="ComponentOfAssemblyContextAndInnerRoleRequiringComponentNeedToBeTheSame", parameters={Parameter(name='pcm_pc_pc_context', type=StringType), Parameter(name='pcm_pc_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector_m_RequiringEntityOfOuterRequiredRoleMustBeTheSameAsTheParentOfTheRequiredDelegationConnector: Method = Method(name="RequiringEntityOfOuterRequiredRoleMustBeTheSameAsTheParentOfTheRequiredDelegationConnector", parameters={Parameter(name='pcm_pc_pc_diagnostics', type=StringType), Parameter(name='pcm_pc_pc_context', type=StringType)}, type=BooleanType)
pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector.methods={pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector_m_RequiredDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure, pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector_m_ComponentOfAssemblyContextAndInnerRoleRequiringComponentNeedToBeTheSame, pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector_m_RequiringEntityOfOuterRequiredRoleMustBeTheSameAsTheParentOfTheRequiredDelegationConnector}

# pcm_pc_pc_composition_pc_pc_SourceDelegationConnector class attributes and methods

# pcm_pc_pc_composition_pc_pc_SinkDelegationConnector class attributes and methods

# pcm_pc_pc_composition_pc_pc_AssemblyInfrastructureConnector class attributes and methods

# InfrastructureProvidedRole class attributes and methods

# InfrastructureRequiredRole class attributes and methods

# pcm_pc_pc_composition_pc_pc_AssemblyEventConnector class attributes and methods

# pcm_pc_pc_composition_pc_pc_RequiredResourceDelegationConnector class attributes and methods

# pcm_pc_pc_composition_pc_pc_AssemblyContext class attributes and methods

# RepositoryComponent class attributes and methods

# VariableUsage class attributes and methods

# pcm_pc_pc_usagemodel_pc_pc_Workload class attributes and methods

# UsageScenario class attributes and methods

# pcm_pc_pc_usagemodel_pc_pc_UsageScenario class attributes and methods

# UsageModel class attributes and methods

# pcm_pc_pc_composition_pc_pc_ProvidedInfrastructureDelegationConnector class attributes and methods

# pcm_pc_pc_composition_pc_pc_RequiredInfrastructureDelegationConnector class attributes and methods

# pcm_pc_pc_usagemodel_pc_pc_UsageModel class attributes and methods

# UserData class attributes and methods

# pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall class attributes and methods
pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall_priority: Property = Property(name="priority", type=IntegerType)
pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall_m_EntryLevelSystemCallMustReferenceProvidedRoleOfASystem: Method = Method(name="EntryLevelSystemCallMustReferenceProvidedRoleOfASystem", parameters={Parameter(name='pcm_pc_pc_context', type=StringType), Parameter(name='pcm_pc_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall_m_EntryLevelSystemCallSignatureMustMatchItsProvidedRole: Method = Method(name="EntryLevelSystemCallSignatureMustMatchItsProvidedRole", parameters={Parameter(name='pcm_pc_pc_diagnostics', type=StringType), Parameter(name='pcm_pc_pc_context', type=StringType)}, type=BooleanType)
pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall.attributes={pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall_priority}
pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall.methods={pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall_m_EntryLevelSystemCallMustReferenceProvidedRoleOfASystem, pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall_m_EntryLevelSystemCallSignatureMustMatchItsProvidedRole}

# AbstractUserAction class attributes and methods

# OperationSignature class attributes and methods

# pcm_pc_pc_usagemodel_pc_pc_AbstractUserAction class attributes and methods

# ScenarioBehaviour class attributes and methods

# Workload class attributes and methods

# pcm_pc_pc_usagemodel_pc_pc_UserData class attributes and methods

# BranchTransition class attributes and methods

# pcm_pc_pc_usagemodel_pc_pc_BranchTransition class attributes and methods
pcm_pc_pc_usagemodel_pc_pc_BranchTransition_branchProbability: Property = Property(name="branchProbability", type=FloatType)
pcm_pc_pc_usagemodel_pc_pc_BranchTransition.attributes={pcm_pc_pc_usagemodel_pc_pc_BranchTransition_branchProbability}

# pcm_pc_pc_usagemodel_pc_pc_ScenarioBehaviour class attributes and methods
pcm_pc_pc_usagemodel_pc_pc_ScenarioBehaviour_m_Exactlyonestart: Method = Method(name="Exactlyonestart", parameters={Parameter(name='pcm_pc_pc_context', type=StringType), Parameter(name='pcm_pc_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_pc_usagemodel_pc_pc_ScenarioBehaviour_m_Exactlyonestop: Method = Method(name="Exactlyonestop", parameters={Parameter(name='pcm_pc_pc_diagnostics', type=StringType), Parameter(name='pcm_pc_pc_context', type=StringType)}, type=BooleanType)
pcm_pc_pc_usagemodel_pc_pc_ScenarioBehaviour_m_EachuseractionexceptStartandStopmusthaveapredecessorandsuccessor: Method = Method(name="EachuseractionexceptStartandStopmusthaveapredecessorandsuccessor", parameters={Parameter(name='pcm_pc_pc_context', type=StringType), Parameter(name='pcm_pc_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_pc_usagemodel_pc_pc_ScenarioBehaviour.methods={pcm_pc_pc_usagemodel_pc_pc_ScenarioBehaviour_m_Exactlyonestop, pcm_pc_pc_usagemodel_pc_pc_ScenarioBehaviour_m_Exactlyonestart, pcm_pc_pc_usagemodel_pc_pc_ScenarioBehaviour_m_EachuseractionexceptStartandStopmusthaveapredecessorandsuccessor}

# pcm_pc_pc_usagemodel_pc_pc_Loop class attributes and methods

# pcm_pc_pc_usagemodel_pc_pc_Stop class attributes and methods
pcm_pc_pc_usagemodel_pc_pc_Stop_m_StopHasNoSuccessor: Method = Method(name="StopHasNoSuccessor", parameters={Parameter(name='pcm_pc_pc_diagnostics', type=StringType), Parameter(name='pcm_pc_pc_context', type=StringType)}, type=BooleanType)
pcm_pc_pc_usagemodel_pc_pc_Stop.methods={pcm_pc_pc_usagemodel_pc_pc_Stop_m_StopHasNoSuccessor}

# pcm_pc_pc_usagemodel_pc_pc_Start class attributes and methods
pcm_pc_pc_usagemodel_pc_pc_Start_m_StartHasNoPredecessor: Method = Method(name="StartHasNoPredecessor", parameters={Parameter(name='pcm_pc_pc_context', type=StringType), Parameter(name='pcm_pc_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_pc_usagemodel_pc_pc_Start.methods={pcm_pc_pc_usagemodel_pc_pc_Start_m_StartHasNoPredecessor}

# pcm_pc_pc_usagemodel_pc_pc_OpenWorkload class attributes and methods
pcm_pc_pc_usagemodel_pc_pc_OpenWorkload_m_InterArrivalTimeInOpenWorkloadNeedsToBeSpecified: Method = Method(name="InterArrivalTimeInOpenWorkloadNeedsToBeSpecified", parameters={Parameter(name='pcm_pc_pc_context', type=StringType), Parameter(name='pcm_pc_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_pc_usagemodel_pc_pc_OpenWorkload.methods={pcm_pc_pc_usagemodel_pc_pc_OpenWorkload_m_InterArrivalTimeInOpenWorkloadNeedsToBeSpecified}

# Branch class attributes and methods

# pcm_pc_pc_usagemodel_pc_pc_Branch class attributes and methods
pcm_pc_pc_usagemodel_pc_pc_Branch_m_AllBranchProbabilitiesMustSumUpTo1: Method = Method(name="AllBranchProbabilitiesMustSumUpTo1", parameters={Parameter(name='pcm_pc_pc_diagnostics', type=StringType), Parameter(name='pcm_pc_pc_context', type=StringType)}, type=BooleanType)
pcm_pc_pc_usagemodel_pc_pc_Branch.methods={pcm_pc_pc_usagemodel_pc_pc_Branch_m_AllBranchProbabilitiesMustSumUpTo1}

# pcm_pc_pc_usagemodel_pc_pc_ClosedWorkload class attributes and methods
pcm_pc_pc_usagemodel_pc_pc_ClosedWorkload_population: Property = Property(name="population", type=IntegerType)
pcm_pc_pc_usagemodel_pc_pc_ClosedWorkload_m_PopulationInClosedWorkloadNeedsToBeSpecified: Method = Method(name="PopulationInClosedWorkloadNeedsToBeSpecified", parameters={Parameter(name='pcm_pc_pc_context', type=StringType), Parameter(name='pcm_pc_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_pc_usagemodel_pc_pc_ClosedWorkload_m_ThinkTimeInClosedWorkloadNeedsToBeSpecified: Method = Method(name="ThinkTimeInClosedWorkloadNeedsToBeSpecified", parameters={Parameter(name='pcm_pc_pc_context', type=StringType), Parameter(name='pcm_pc_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_pc_usagemodel_pc_pc_ClosedWorkload.attributes={pcm_pc_pc_usagemodel_pc_pc_ClosedWorkload_population}
pcm_pc_pc_usagemodel_pc_pc_ClosedWorkload.methods={pcm_pc_pc_usagemodel_pc_pc_ClosedWorkload_m_PopulationInClosedWorkloadNeedsToBeSpecified, pcm_pc_pc_usagemodel_pc_pc_ClosedWorkload_m_ThinkTimeInClosedWorkloadNeedsToBeSpecified}

# pcm_pc_pc_repository_pc_pc_PassiveResource class attributes and methods

# BasicComponent class attributes and methods

# ResourceTimeoutFailureType class attributes and methods

# pcm_pc_pc_usagemodel_pc_pc_Delay class attributes and methods

# ServiceEffectSpecification class attributes and methods

# pcm_pc_pc_repository_pc_pc_ImplementationComponentType class attributes and methods
pcm_pc_pc_repository_pc_pc_ImplementationComponentType_componentType: Property = Property(name="componentType", type=StringType)
pcm_pc_pc_repository_pc_pc_ImplementationComponentType_m_RequiredInterfacesHaveToConformToCompleteType: Method = Method(name="RequiredInterfacesHaveToConformToCompleteType", parameters={Parameter(name='pcm_pc_pc_diagnostics', type=StringType), Parameter(name='pcm_pc_pc_context', type=StringType)}, type=BooleanType)
pcm_pc_pc_repository_pc_pc_ImplementationComponentType_m_ProvidedInterfaceHaveToConformToComponentType: Method = Method(name="ProvidedInterfaceHaveToConformToComponentType", parameters={Parameter(name='pcm_pc_pc_diagnostics', type=StringType), Parameter(name='pcm_pc_pc_context', type=StringType)}, type=BooleanType)
pcm_pc_pc_repository_pc_pc_ImplementationComponentType_m_providedInterfacesHaveToConformToCompleteType: Method = Method(name="providedInterfacesHaveToConformToCompleteType", parameters={Parameter(name='pcm_pc_pc_context', type=StringType), Parameter(name='pcm_pc_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_pc_repository_pc_pc_ImplementationComponentType.attributes={pcm_pc_pc_repository_pc_pc_ImplementationComponentType_componentType}
pcm_pc_pc_repository_pc_pc_ImplementationComponentType.methods={pcm_pc_pc_repository_pc_pc_ImplementationComponentType_m_providedInterfacesHaveToConformToCompleteType, pcm_pc_pc_repository_pc_pc_ImplementationComponentType_m_RequiredInterfacesHaveToConformToCompleteType, pcm_pc_pc_repository_pc_pc_ImplementationComponentType_m_ProvidedInterfaceHaveToConformToComponentType}

# pcm_pc_pc_repository_pc_pc_BasicComponent class attributes and methods
pcm_pc_pc_repository_pc_pc_BasicComponent_m_ProvideSameInterfacesAsImplementationType: Method = Method(name="ProvideSameInterfacesAsImplementationType", parameters={Parameter(name='pcm_pc_pc_context', type=StringType), Parameter(name='pcm_pc_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_pc_repository_pc_pc_BasicComponent_m_RequireSameInterfacesAsImplementationType: Method = Method(name="RequireSameInterfacesAsImplementationType", parameters={Parameter(name='pcm_pc_pc_diagnostics', type=StringType), Parameter(name='pcm_pc_pc_context', type=StringType)}, type=BooleanType)
pcm_pc_pc_repository_pc_pc_BasicComponent_m_NoSeffTypeUsedTwice: Method = Method(name="NoSeffTypeUsedTwice", parameters={Parameter(name='pcm_pc_pc_context', type=StringType), Parameter(name='pcm_pc_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_pc_repository_pc_pc_BasicComponent.methods={pcm_pc_pc_repository_pc_pc_BasicComponent_m_ProvideSameInterfacesAsImplementationType, pcm_pc_pc_repository_pc_pc_BasicComponent_m_NoSeffTypeUsedTwice, pcm_pc_pc_repository_pc_pc_BasicComponent_m_RequireSameInterfacesAsImplementationType}

# ImplementationComponentType class attributes and methods

# CompleteComponentType class attributes and methods

# pcm_pc_pc_repository_pc_pc_RepositoryComponent class attributes and methods

# InterfaceProvidingRequiringEntity class attributes and methods

# Repository class attributes and methods

# pcm_pc_pc_repository_pc_pc_ProvidedRole class attributes and methods

# pcm_pc_pc_repository_pc_pc_Parameter class attributes and methods
pcm_pc_pc_repository_pc_pc_Parameter_parameterName: Property = Property(name="parameterName", type=StringType)
pcm_pc_pc_repository_pc_pc_Parameter_modifier__Parameter: Property = Property(name="modifier__Parameter", type=StringType)
pcm_pc_pc_repository_pc_pc_Parameter.attributes={pcm_pc_pc_repository_pc_pc_Parameter_parameterName, pcm_pc_pc_repository_pc_pc_Parameter_modifier__Parameter}

# DataType class attributes and methods

# InfrastructureSignature class attributes and methods

# EventType class attributes and methods

# pcm_pc_pc_repository_pc_pc_Repository class attributes and methods
pcm_pc_pc_repository_pc_pc_Repository_repositoryDescription: Property = Property(name="repositoryDescription", type=StringType)
pcm_pc_pc_repository_pc_pc_Repository.attributes={pcm_pc_pc_repository_pc_pc_Repository_repositoryDescription}

# Interface class attributes and methods

# FailureType class attributes and methods

# pcm_pc_pc_repository_pc_pc_Interface class attributes and methods
pcm_pc_pc_repository_pc_pc_Interface_m_NoProtocolTypeIDUsedTwice: Method = Method(name="NoProtocolTypeIDUsedTwice", parameters={Parameter(name='pcm_pc_pc_diagnostics', type=StringType), Parameter(name='pcm_pc_pc_context', type=StringType)}, type=BooleanType)
pcm_pc_pc_repository_pc_pc_Interface.methods={pcm_pc_pc_repository_pc_pc_Interface_m_NoProtocolTypeIDUsedTwice}

# Protocol class attributes and methods

# ResourceSignature class attributes and methods

# pcm_pc_pc_repository_pc_pc_DataType class attributes and methods

# pcm_pc_pc_repository_pc_pc_RequiredCharacterisation class attributes and methods
pcm_pc_pc_repository_pc_pc_RequiredCharacterisation_type: Property = Property(name="type", type=StringType)
pcm_pc_pc_repository_pc_pc_RequiredCharacterisation.attributes={pcm_pc_pc_repository_pc_pc_RequiredCharacterisation_type}

# Parameter class attributes and methods

# pcm_pc_pc_repository_pc_pc_EventGroup class attributes and methods

# pcm_pc_pc_repository_pc_pc_EventType class attributes and methods

# Signature class attributes and methods

# pcm_pc_pc_repository_pc_pc_Signature class attributes and methods

# ExceptionType class attributes and methods

# pcm_pc_pc_repository_pc_pc_ExceptionType class attributes and methods
pcm_pc_pc_repository_pc_pc_ExceptionType_exceptionName: Property = Property(name="exceptionName", type=StringType)
pcm_pc_pc_repository_pc_pc_ExceptionType_exceptionMessage: Property = Property(name="exceptionMessage", type=StringType)
pcm_pc_pc_repository_pc_pc_ExceptionType.attributes={pcm_pc_pc_repository_pc_pc_ExceptionType_exceptionMessage, pcm_pc_pc_repository_pc_pc_ExceptionType_exceptionName}

# pcm_pc_pc_repository_pc_pc_InfrastructureSignature class attributes and methods

# InfrastructureInterface class attributes and methods

# pcm_pc_pc_repository_pc_pc_InfrastructureInterface class attributes and methods

# RequiredCharacterisation class attributes and methods

# pcm_pc_pc_repository_pc_pc_OperationSignature class attributes and methods
pcm_pc_pc_repository_pc_pc_OperationSignature_m_ParameterNamesHaveToBeUniqueForASignature: Method = Method(name="ParameterNamesHaveToBeUniqueForASignature", parameters={Parameter(name='pcm_pc_pc_diagnostics', type=StringType), Parameter(name='pcm_pc_pc_context', type=StringType)}, type=BooleanType)
pcm_pc_pc_repository_pc_pc_OperationSignature.methods={pcm_pc_pc_repository_pc_pc_OperationSignature_m_ParameterNamesHaveToBeUniqueForASignature}

# OperationInterface class attributes and methods

# pcm_pc_pc_repository_pc_pc_OperationInterface class attributes and methods
pcm_pc_pc_repository_pc_pc_OperationInterface_m_SignaturesHaveToBeUniqueForAnInterface: Method = Method(name="SignaturesHaveToBeUniqueForAnInterface", parameters={Parameter(name='pcm_pc_pc_diagnostics', type=StringType), Parameter(name='pcm_pc_pc_context', type=StringType)}, type=BooleanType)
pcm_pc_pc_repository_pc_pc_OperationInterface.methods={pcm_pc_pc_repository_pc_pc_OperationInterface_m_SignaturesHaveToBeUniqueForAnInterface}

# pcm_pc_pc_repository_pc_pc_OperationRequiredRole class attributes and methods

# pcm_pc_pc_repository_pc_pc_SourceRole class attributes and methods

# pcm_pc_pc_repository_pc_pc_InfrastructureRequiredRole class attributes and methods

# pcm_pc_pc_repository_pc_pc_RequiredRole class attributes and methods

# pcm_pc_pc_repository_pc_pc_OperationProvidedRole class attributes and methods

# pcm_pc_pc_repository_pc_pc_InfrastructureProvidedRole class attributes and methods

# pcm_pc_pc_repository_pc_pc_CompleteComponentType class attributes and methods
pcm_pc_pc_repository_pc_pc_CompleteComponentType_m_AtLeastOneInterfaceHasToBeProvidedOrRequiredByAUsefullCompleteComponentType: Method = Method(name="AtLeastOneInterfaceHasToBeProvidedOrRequiredByAUsefullCompleteComponentType", parameters={Parameter(name='pcm_pc_pc_diagnostics', type=StringType), Parameter(name='pcm_pc_pc_context', type=StringType)}, type=BooleanType)
pcm_pc_pc_repository_pc_pc_CompleteComponentType_m_providedInterfacesHaveToConformToProvidedType2: Method = Method(name="providedInterfacesHaveToConformToProvidedType2", parameters={Parameter(name='pcm_pc_pc_diagnostics', type=StringType), Parameter(name='pcm_pc_pc_context', type=StringType)}, type=BooleanType)
pcm_pc_pc_repository_pc_pc_CompleteComponentType.methods={pcm_pc_pc_repository_pc_pc_CompleteComponentType_m_providedInterfacesHaveToConformToProvidedType2, pcm_pc_pc_repository_pc_pc_CompleteComponentType_m_AtLeastOneInterfaceHasToBeProvidedOrRequiredByAUsefullCompleteComponentType}

# ProvidesComponentType class attributes and methods

# pcm_pc_pc_repository_pc_pc_ProvidesComponentType class attributes and methods
pcm_pc_pc_repository_pc_pc_ProvidesComponentType_m_AtLeastOneInterfaceHasToBeProvidedByAUsefullProvidesComponentType: Method = Method(name="AtLeastOneInterfaceHasToBeProvidedByAUsefullProvidesComponentType", parameters={Parameter(name='pcm_pc_pc_context', type=StringType), Parameter(name='pcm_pc_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_pc_repository_pc_pc_ProvidesComponentType.methods={pcm_pc_pc_repository_pc_pc_ProvidesComponentType_m_AtLeastOneInterfaceHasToBeProvidedByAUsefullProvidesComponentType}

# pcm_pc_pc_repository_pc_pc_SinkRole class attributes and methods

# pcm_pc_pc_repository_pc_pc_PrimitiveDataType class attributes and methods
pcm_pc_pc_repository_pc_pc_PrimitiveDataType_type: Property = Property(name="type", type=StringType)
pcm_pc_pc_repository_pc_pc_PrimitiveDataType.attributes={pcm_pc_pc_repository_pc_pc_PrimitiveDataType_type}

# pcm_pc_pc_repository_pc_pc_CollectionDataType class attributes and methods

# repository_pc_pc_DataType class attributes and methods

# pcm_pc_pc_repository_pc_pc_CompositeDataType class attributes and methods

# pcm_pc_pc_repository_pc_pc_CompositeComponent class attributes and methods
pcm_pc_pc_repository_pc_pc_CompositeComponent_m_ProvideSameInterfaces: Method = Method(name="ProvideSameInterfaces", parameters={Parameter(name='pcm_pc_pc_context', type=StringType), Parameter(name='pcm_pc_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_pc_repository_pc_pc_CompositeComponent_m_RequireSameInterfaces: Method = Method(name="RequireSameInterfaces", parameters={Parameter(name='pcm_pc_pc_diagnostics', type=StringType), Parameter(name='pcm_pc_pc_context', type=StringType)}, type=BooleanType)
pcm_pc_pc_repository_pc_pc_CompositeComponent.methods={pcm_pc_pc_repository_pc_pc_CompositeComponent_m_ProvideSameInterfaces, pcm_pc_pc_repository_pc_pc_CompositeComponent_m_RequireSameInterfaces}

# entity_pc_pc_ComposedProvidingRequiringEntity class attributes and methods

# repository_pc_pc_ImplementationComponentType class attributes and methods

# InnerDeclaration class attributes and methods

# pcm_pc_pc_repository_pc_pc_InnerDeclaration class attributes and methods

# NamedElement class attributes and methods

# pcm_pc_pc_repository_pc_pc_Role class attributes and methods

# pcm_pc_pc_resourcetype_pc_pc_ResourceSignature class attributes and methods
pcm_pc_pc_resourcetype_pc_pc_ResourceSignature_resourceServiceId: Property = Property(name="resourceServiceId", type=IntegerType)
pcm_pc_pc_resourcetype_pc_pc_ResourceSignature.attributes={pcm_pc_pc_resourcetype_pc_pc_ResourceSignature_resourceServiceId}

# pcm_pc_pc_resourcetype_pc_pc_ProcessingResourceType class attributes and methods

# ResourceType class attributes and methods

# HardwareInducedFailureType class attributes and methods

# pcm_pc_pc_resourcetype_pc_pc_ResourceType class attributes and methods

# UnitCarryingElement class attributes and methods

# CompositeDataType class attributes and methods

# pcm_pc_pc_resourcetype_pc_pc_ResourceRepository class attributes and methods

# SchedulingPolicy class attributes and methods

# pcm_pc_pc_resourcetype_pc_pc_SchedulingPolicy class attributes and methods

# pcm_pc_pc_resourcetype_pc_pc_CommunicationLinkResourceType class attributes and methods

# NetworkInducedFailureType class attributes and methods

# pcm_pc_pc_resourcetype_pc_pc_ResourceInterface class attributes and methods

# pcm_pc_pc_protocol_pc_pc_Protocol class attributes and methods
pcm_pc_pc_protocol_pc_pc_Protocol_protocolTypeID: Property = Property(name="protocolTypeID", type=StringType)
pcm_pc_pc_protocol_pc_pc_Protocol.attributes={pcm_pc_pc_protocol_pc_pc_Protocol_protocolTypeID}

# ResourceRepository class attributes and methods

# CallAction class attributes and methods

# SynchronisationPoint class attributes and methods

# CallReturnAction class attributes and methods

# SetVariableAction class attributes and methods

# SpecifiedOutputParameterAbstraction class attributes and methods

# EntryLevelSystemCall class attributes and methods

# parameter_pc_pc_pcm_pc_pc_AbstractNamedReference class attributes and methods

# pcm_pc_pc_parameter_pc_pc_VariableCharacterisation class attributes and methods
pcm_pc_pc_parameter_pc_pc_VariableCharacterisation_type: Property = Property(name="type", type=StringType)
pcm_pc_pc_parameter_pc_pc_VariableCharacterisation.attributes={pcm_pc_pc_parameter_pc_pc_VariableCharacterisation_type}

# pcm_pc_pc_parameter_pc_pc_VariableUsage class attributes and methods

# pcm_pc_pc_reliability_pc_pc_FailureOccurrenceDescription class attributes and methods
pcm_pc_pc_reliability_pc_pc_FailureOccurrenceDescription_failureProbability: Property = Property(name="failureProbability", type=FloatType)
pcm_pc_pc_reliability_pc_pc_FailureOccurrenceDescription_m_EnsureValidFailureProbabilityRange: Method = Method(name="EnsureValidFailureProbabilityRange", parameters={Parameter(name='pcm_pc_pc_diagnostics', type=StringType), Parameter(name='pcm_pc_pc_context', type=StringType)}, type=BooleanType)
pcm_pc_pc_reliability_pc_pc_FailureOccurrenceDescription.attributes={pcm_pc_pc_reliability_pc_pc_FailureOccurrenceDescription_failureProbability}
pcm_pc_pc_reliability_pc_pc_FailureOccurrenceDescription.methods={pcm_pc_pc_reliability_pc_pc_FailureOccurrenceDescription_m_EnsureValidFailureProbabilityRange}

# pcm_pc_pc_reliability_pc_pc_HardwareInducedFailureType class attributes and methods
pcm_pc_pc_reliability_pc_pc_HardwareInducedFailureType_m_HardwareInducedFailureTypeHasProcessingResourceType: Method = Method(name="HardwareInducedFailureTypeHasProcessingResourceType", parameters={Parameter(name='pcm_pc_pc_diagnostics', type=StringType), Parameter(name='pcm_pc_pc_context', type=StringType)}, type=BooleanType)
pcm_pc_pc_reliability_pc_pc_HardwareInducedFailureType.methods={pcm_pc_pc_reliability_pc_pc_HardwareInducedFailureType_m_HardwareInducedFailureTypeHasProcessingResourceType}

# pcm_pc_pc_parameter_pc_pc_CharacterisedVariable class attributes and methods
pcm_pc_pc_parameter_pc_pc_CharacterisedVariable_characterisationType: Property = Property(name="characterisationType", type=StringType)
pcm_pc_pc_parameter_pc_pc_CharacterisedVariable.attributes={pcm_pc_pc_parameter_pc_pc_CharacterisedVariable_characterisationType}

# Variable class attributes and methods

# InternalFailureOccurrenceDescription class attributes and methods

# pcm_pc_pc_reliability_pc_pc_InternalFailureOccurrenceDescription class attributes and methods
pcm_pc_pc_reliability_pc_pc_InternalFailureOccurrenceDescription_m_NoResourceTimeoutFailureAllowedForInternalFailureOccurrenceDescription: Method = Method(name="NoResourceTimeoutFailureAllowedForInternalFailureOccurrenceDescription", parameters={Parameter(name='pcm_pc_pc_diagnostics', type=StringType), Parameter(name='pcm_pc_pc_context', type=StringType)}, type=BooleanType)
pcm_pc_pc_reliability_pc_pc_InternalFailureOccurrenceDescription.methods={pcm_pc_pc_reliability_pc_pc_InternalFailureOccurrenceDescription_m_NoResourceTimeoutFailureAllowedForInternalFailureOccurrenceDescription}

# FailureOccurrenceDescription class attributes and methods

# InternalAction class attributes and methods

# SoftwareInducedFailureType class attributes and methods

# pcm_pc_pc_reliability_pc_pc_NetworkInducedFailureType class attributes and methods
pcm_pc_pc_reliability_pc_pc_NetworkInducedFailureType_m_NetworkInducedFailureTypeHasCommunicationLinkResourceType: Method = Method(name="NetworkInducedFailureTypeHasCommunicationLinkResourceType", parameters={Parameter(name='pcm_pc_pc_context', type=StringType), Parameter(name='pcm_pc_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_pc_reliability_pc_pc_NetworkInducedFailureType.methods={pcm_pc_pc_reliability_pc_pc_NetworkInducedFailureType_m_NetworkInducedFailureTypeHasCommunicationLinkResourceType}

# CommunicationLinkResourceType class attributes and methods

# pcm_pc_pc_reliability_pc_pc_ExternalFailureOccurrenceDescription class attributes and methods
pcm_pc_pc_reliability_pc_pc_ExternalFailureOccurrenceDescription_m_NoResourceTimeoutFailureAllowedForExternalFailureOccurrenceDescription: Method = Method(name="NoResourceTimeoutFailureAllowedForExternalFailureOccurrenceDescription", parameters={Parameter(name='pcm_pc_pc_context', type=StringType), Parameter(name='pcm_pc_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_pc_reliability_pc_pc_ExternalFailureOccurrenceDescription.methods={pcm_pc_pc_reliability_pc_pc_ExternalFailureOccurrenceDescription_m_NoResourceTimeoutFailureAllowedForExternalFailureOccurrenceDescription}

# ProcessingResourceType class attributes and methods

# pcm_pc_pc_reliability_pc_pc_SoftwareInducedFailureType class attributes and methods

# pcm_pc_pc_reliability_pc_pc_ResourceTimeoutFailureType class attributes and methods

# pcm_pc_pc_reliability_pc_pc_FailureType class attributes and methods

# pcm_pc_pc_seff_pc_pc_StopAction class attributes and methods
pcm_pc_pc_seff_pc_pc_StopAction_m_StopActionSuccessorMustNotBeDefined: Method = Method(name="StopActionSuccessorMustNotBeDefined", parameters={Parameter(name='pcm_pc_pc_diagnostics', type=StringType), Parameter(name='pcm_pc_pc_context', type=StringType)}, type=BooleanType)
pcm_pc_pc_seff_pc_pc_StopAction.methods={pcm_pc_pc_seff_pc_pc_StopAction_m_StopActionSuccessorMustNotBeDefined}

# AbstractInternalControlFlowAction class attributes and methods

# pcm_pc_pc_seff_pc_pc_AbstractInternalControlFlowAction class attributes and methods

# AbstractAction class attributes and methods

# pcm_pc_pc_seff_pc_pc_AbstractAction class attributes and methods

# qos_reliability_pc_pc_SpecifiedReliabilityAnnotation class attributes and methods

# AbstractLoopAction class attributes and methods

# AbstractBranchTransition class attributes and methods

# pcm_pc_pc_seff_pc_pc_AbstractLoopAction class attributes and methods

# pcm_pc_pc_seff_pc_pc_AbstractBranchTransition class attributes and methods

# BranchAction class attributes and methods

# ResourceDemandingBehaviour class attributes and methods

# pcm_pc_pc_seff_pc_pc_ResourceDemandingBehaviour class attributes and methods
pcm_pc_pc_seff_pc_pc_ResourceDemandingBehaviour_m_ExactlyOneStartAction: Method = Method(name="ExactlyOneStartAction", parameters={Parameter(name='pcm_pc_pc_diagnostics', type=StringType), Parameter(name='pcm_pc_pc_context', type=StringType)}, type=BooleanType)
pcm_pc_pc_seff_pc_pc_ResourceDemandingBehaviour_m_EachActionExceptStartActionandStopActionMustHhaveAPredecessorAndSuccessor: Method = Method(name="EachActionExceptStartActionandStopActionMustHhaveAPredecessorAndSuccessor", parameters={Parameter(name='pcm_pc_pc_diagnostics', type=StringType), Parameter(name='pcm_pc_pc_context', type=StringType)}, type=BooleanType)
pcm_pc_pc_seff_pc_pc_ResourceDemandingBehaviour_m_ExactlyOneStopAction: Method = Method(name="ExactlyOneStopAction", parameters={Parameter(name='pcm_pc_pc_diagnostics', type=StringType), Parameter(name='pcm_pc_pc_context', type=StringType)}, type=BooleanType)
pcm_pc_pc_seff_pc_pc_ResourceDemandingBehaviour.methods={pcm_pc_pc_seff_pc_pc_ResourceDemandingBehaviour_m_EachActionExceptStartActionandStopActionMustHhaveAPredecessorAndSuccessor, pcm_pc_pc_seff_pc_pc_ResourceDemandingBehaviour_m_ExactlyOneStopAction, pcm_pc_pc_seff_pc_pc_ResourceDemandingBehaviour_m_ExactlyOneStartAction}

# pcm_pc_pc_seff_pc_pc_CallAction class attributes and methods

# pcm_pc_pc_seff_pc_pc_StartAction class attributes and methods
pcm_pc_pc_seff_pc_pc_StartAction_m_StartActionPredecessorMustNotBeDefined: Method = Method(name="StartActionPredecessorMustNotBeDefined", parameters={Parameter(name='pcm_pc_pc_context', type=StringType), Parameter(name='pcm_pc_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_pc_seff_pc_pc_StartAction.methods={pcm_pc_pc_seff_pc_pc_StartAction_m_StartActionPredecessorMustNotBeDefined}

# pcm_pc_pc_seff_pc_pc_ServiceEffectSpecification class attributes and methods
pcm_pc_pc_seff_pc_pc_ServiceEffectSpecification_seffTypeID: Property = Property(name="seffTypeID", type=StringType)
pcm_pc_pc_seff_pc_pc_ServiceEffectSpecification_m_ReferencedSignatureMustBelongToInterfaceReferencedByProvidedRole: Method = Method(name="ReferencedSignatureMustBelongToInterfaceReferencedByProvidedRole", parameters={Parameter(name='pcm_pc_pc_diagnostics', type=StringType), Parameter(name='pcm_pc_pc_context', type=StringType)}, type=BooleanType)
pcm_pc_pc_seff_pc_pc_ServiceEffectSpecification.attributes={pcm_pc_pc_seff_pc_pc_ServiceEffectSpecification_seffTypeID}
pcm_pc_pc_seff_pc_pc_ServiceEffectSpecification.methods={pcm_pc_pc_seff_pc_pc_ServiceEffectSpecification_m_ReferencedSignatureMustBelongToInterfaceReferencedByProvidedRole}

# pcm_pc_pc_seff_pc_pc_BranchAction class attributes and methods
pcm_pc_pc_seff_pc_pc_BranchAction_m_AllProbabilisticBranchProbabilitiesMustSumUpTo1: Method = Method(name="AllProbabilisticBranchProbabilitiesMustSumUpTo1", parameters={Parameter(name='pcm_pc_pc_context', type=StringType), Parameter(name='pcm_pc_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_pc_seff_pc_pc_BranchAction_m_EitherGuardedBranchesOrProbabilisiticBranchTransitions: Method = Method(name="EitherGuardedBranchesOrProbabilisiticBranchTransitions", parameters={Parameter(name='pcm_pc_pc_context', type=StringType), Parameter(name='pcm_pc_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_pc_seff_pc_pc_BranchAction.methods={pcm_pc_pc_seff_pc_pc_BranchAction_m_AllProbabilisticBranchProbabilitiesMustSumUpTo1, pcm_pc_pc_seff_pc_pc_BranchAction_m_EitherGuardedBranchesOrProbabilisiticBranchTransitions}

# pcm_pc_pc_seff_pc_pc_ResourceDemandingInternalBehaviour class attributes and methods

# ResourceDemandingSEFF class attributes and methods

# pcm_pc_pc_seff_pc_pc_ReleaseAction class attributes and methods

# pcm_pc_pc_seff_pc_pc_LoopAction class attributes and methods

# pcm_pc_pc_seff_pc_pc_ForkAction class attributes and methods

# ForkedBehaviour class attributes and methods

# pcm_pc_pc_seff_pc_pc_ForkedBehaviour class attributes and methods

# ForkAction class attributes and methods

# pcm_pc_pc_seff_pc_pc_SynchronisationPoint class attributes and methods

# pcm_pc_pc_seff_pc_pc_ResourceDemandingSEFF class attributes and methods

# seff_pc_pc_ServiceEffectSpecification class attributes and methods

# seff_pc_pc_ResourceDemandingBehaviour class attributes and methods

# ResourceDemandingInternalBehaviour class attributes and methods

# seff_reliability_pc_pc_FailureHandlingEntity class attributes and methods

# pcm_pc_pc_seff_pc_pc_CallReturnAction class attributes and methods

# pcm_pc_pc_seff_pc_pc_ExternalCallAction class attributes and methods
pcm_pc_pc_seff_pc_pc_ExternalCallAction_retryCount: Property = Property(name="retryCount", type=IntegerType)
pcm_pc_pc_seff_pc_pc_ExternalCallAction_m_SignatureBelongsToRole: Method = Method(name="SignatureBelongsToRole", parameters={Parameter(name='pcm_pc_pc_context', type=StringType), Parameter(name='pcm_pc_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_pc_seff_pc_pc_ExternalCallAction_m_OperationRequiredRoleMustBeReferencedByContainer: Method = Method(name="OperationRequiredRoleMustBeReferencedByContainer", parameters={Parameter(name='pcm_pc_pc_diagnostics', type=StringType), Parameter(name='pcm_pc_pc_context', type=StringType)}, type=BooleanType)
pcm_pc_pc_seff_pc_pc_ExternalCallAction.attributes={pcm_pc_pc_seff_pc_pc_ExternalCallAction_retryCount}
pcm_pc_pc_seff_pc_pc_ExternalCallAction.methods={pcm_pc_pc_seff_pc_pc_ExternalCallAction_m_OperationRequiredRoleMustBeReferencedByContainer, pcm_pc_pc_seff_pc_pc_ExternalCallAction_m_SignatureBelongsToRole}

# seff_pc_pc_AbstractAction class attributes and methods

# seff_pc_pc_CallReturnAction class attributes and methods

# pcm_pc_pc_seff_pc_pc_CollectionIteratorAction class attributes and methods

# pcm_pc_pc_seff_pc_pc_GuardedBranchTransition class attributes and methods

# pcm_pc_pc_seff_pc_pc_SetVariableAction class attributes and methods

# pcm_pc_pc_seff_pc_pc_InternalCallAction class attributes and methods

# seff_pc_pc_CallAction class attributes and methods

# seff_pc_pc_AbstractInternalControlFlowAction class attributes and methods

# pcm_pc_pc_seff_pc_pc_EmitEventAction class attributes and methods

# pcm_pc_pc_seff_pc_pc_InternalAction class attributes and methods
pcm_pc_pc_seff_pc_pc_InternalAction_m_MultipleInternalOccurrenceDescriptionsPerFailureTypeNotAllowed: Method = Method(name="MultipleInternalOccurrenceDescriptionsPerFailureTypeNotAllowed", parameters={Parameter(name='pcm_pc_pc_context', type=StringType), Parameter(name='pcm_pc_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_pc_seff_pc_pc_InternalAction_m_SumOfInternalActionFailureProbabilitiesMustNotExceed1: Method = Method(name="SumOfInternalActionFailureProbabilitiesMustNotExceed1", parameters={Parameter(name='pcm_pc_pc_context', type=StringType), Parameter(name='pcm_pc_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_pc_seff_pc_pc_InternalAction.methods={pcm_pc_pc_seff_pc_pc_InternalAction_m_MultipleInternalOccurrenceDescriptionsPerFailureTypeNotAllowed, pcm_pc_pc_seff_pc_pc_InternalAction_m_SumOfInternalActionFailureProbabilitiesMustNotExceed1}

# pcm_pc_pc_seff_pc_pc_ProbabilisticBranchTransition class attributes and methods
pcm_pc_pc_seff_pc_pc_ProbabilisticBranchTransition_branchProbability: Property = Property(name="branchProbability", type=FloatType)
pcm_pc_pc_seff_pc_pc_ProbabilisticBranchTransition.attributes={pcm_pc_pc_seff_pc_pc_ProbabilisticBranchTransition_branchProbability}

# pcm_pc_pc_seff_pc_pc_AcquireAction class attributes and methods
pcm_pc_pc_seff_pc_pc_AcquireAction_timeout: Property = Property(name="timeout", type=BooleanType)
pcm_pc_pc_seff_pc_pc_AcquireAction_timeoutValue: Property = Property(name="timeoutValue", type=FloatType)
pcm_pc_pc_seff_pc_pc_AcquireAction_m_TimeoutValueOfAcquireActionMustNotBeNegative: Method = Method(name="TimeoutValueOfAcquireActionMustNotBeNegative", parameters={Parameter(name='pcm_pc_pc_diagnostics', type=StringType), Parameter(name='pcm_pc_pc_context', type=StringType)}, type=BooleanType)
pcm_pc_pc_seff_pc_pc_AcquireAction.attributes={pcm_pc_pc_seff_pc_pc_AcquireAction_timeout, pcm_pc_pc_seff_pc_pc_AcquireAction_timeoutValue}
pcm_pc_pc_seff_pc_pc_AcquireAction.methods={pcm_pc_pc_seff_pc_pc_AcquireAction_m_TimeoutValueOfAcquireActionMustNotBeNegative}

# pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall class attributes and methods
pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall_m_SignatureMustBelongToUsedRequiredRole: Method = Method(name="SignatureMustBelongToUsedRequiredRole", parameters={Parameter(name='pcm_pc_pc_diagnostics', type=StringType), Parameter(name='pcm_pc_pc_context', type=StringType)}, type=BooleanType)
pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall_m_ReferencedRequiredRoleMustBeRequiredByComponent: Method = Method(name="ReferencedRequiredRoleMustBeRequiredByComponent", parameters={Parameter(name='pcm_pc_pc_context', type=StringType), Parameter(name='pcm_pc_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall_m_SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction: Method = Method(name="SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction", parameters={Parameter(name='pcm_pc_pc_context', type=StringType), Parameter(name='pcm_pc_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall.methods={pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall_m_SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction, pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall_m_SignatureMustBelongToUsedRequiredRole, pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall_m_ReferencedRequiredRoleMustBeRequiredByComponent}

# pcm_pc_pc_seff_performance_pc_pc_ParametricResourceDemand class attributes and methods
pcm_pc_pc_seff_performance_pc_pc_ParametricResourceDemand_m_DemandedProcessingResourceMustBeUniqueWithinAbstractInternalControlFlowAction: Method = Method(name="DemandedProcessingResourceMustBeUniqueWithinAbstractInternalControlFlowAction", parameters={Parameter(name='pcm_pc_pc_diagnostics', type=StringType), Parameter(name='pcm_pc_pc_context', type=StringType)}, type=BooleanType)
pcm_pc_pc_seff_performance_pc_pc_ParametricResourceDemand.methods={pcm_pc_pc_seff_performance_pc_pc_ParametricResourceDemand_m_DemandedProcessingResourceMustBeUniqueWithinAbstractInternalControlFlowAction}

# pcm_pc_pc_seff_reliability_pc_pc_RecoveryActionBehaviour class attributes and methods
pcm_pc_pc_seff_reliability_pc_pc_RecoveryActionBehaviour_m_SuccessorsOfRecoveryActionBehaviourHandleDisjointFailureTypes: Method = Method(name="SuccessorsOfRecoveryActionBehaviourHandleDisjointFailureTypes", parameters={Parameter(name='pcm_pc_pc_context', type=StringType), Parameter(name='pcm_pc_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_pc_seff_reliability_pc_pc_RecoveryActionBehaviour_m_RecoveryActionBehaviourHasOnlyOnePredecessor: Method = Method(name="RecoveryActionBehaviourHasOnlyOnePredecessor", parameters={Parameter(name='pcm_pc_pc_diagnostics', type=StringType), Parameter(name='pcm_pc_pc_context', type=StringType)}, type=BooleanType)
pcm_pc_pc_seff_reliability_pc_pc_RecoveryActionBehaviour_m_RecoveryActionBehaviourIsNotSuccessorOfItself: Method = Method(name="RecoveryActionBehaviourIsNotSuccessorOfItself", parameters={Parameter(name='pcm_pc_pc_context', type=StringType), Parameter(name='pcm_pc_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_pc_seff_reliability_pc_pc_RecoveryActionBehaviour.methods={pcm_pc_pc_seff_reliability_pc_pc_RecoveryActionBehaviour_m_SuccessorsOfRecoveryActionBehaviourHandleDisjointFailureTypes, pcm_pc_pc_seff_reliability_pc_pc_RecoveryActionBehaviour_m_RecoveryActionBehaviourHasOnlyOnePredecessor, pcm_pc_pc_seff_reliability_pc_pc_RecoveryActionBehaviour_m_RecoveryActionBehaviourIsNotSuccessorOfItself}

# pcm_pc_pc_seff_performance_pc_pc_ResourceCall class attributes and methods
pcm_pc_pc_seff_performance_pc_pc_ResourceCall_m_SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction: Method = Method(name="SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction", parameters={Parameter(name='pcm_pc_pc_diagnostics', type=StringType), Parameter(name='pcm_pc_pc_context', type=StringType)}, type=BooleanType)
pcm_pc_pc_seff_performance_pc_pc_ResourceCall_m_ResourceSignatureBelongsToResourceRequiredRole: Method = Method(name="ResourceSignatureBelongsToResourceRequiredRole", parameters={Parameter(name='pcm_pc_pc_context', type=StringType), Parameter(name='pcm_pc_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_pc_seff_performance_pc_pc_ResourceCall_m_ResourceRequiredRoleMustBeReferencedByComponent: Method = Method(name="ResourceRequiredRoleMustBeReferencedByComponent", parameters={Parameter(name='pcm_pc_pc_diagnostics', type=StringType), Parameter(name='pcm_pc_pc_context', type=StringType)}, type=BooleanType)
pcm_pc_pc_seff_performance_pc_pc_ResourceCall.methods={pcm_pc_pc_seff_performance_pc_pc_ResourceCall_m_ResourceRequiredRoleMustBeReferencedByComponent, pcm_pc_pc_seff_performance_pc_pc_ResourceCall_m_ResourceSignatureBelongsToResourceRequiredRole, pcm_pc_pc_seff_performance_pc_pc_ResourceCall_m_SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction}

# seff_reliability_pc_pc_RecoveryActionBehaviour class attributes and methods

# seff_reliability_pc_pc_RecoveryAction class attributes and methods

# pcm_pc_pc_seff_reliability_pc_pc_RecoveryAction class attributes and methods
pcm_pc_pc_seff_reliability_pc_pc_RecoveryAction_m_PrimaryBehaviourOfRecoveryActionMustBeSet: Method = Method(name="PrimaryBehaviourOfRecoveryActionMustBeSet", parameters={Parameter(name='pcm_pc_pc_diagnostics', type=StringType), Parameter(name='pcm_pc_pc_context', type=StringType)}, type=BooleanType)
pcm_pc_pc_seff_reliability_pc_pc_RecoveryAction.methods={pcm_pc_pc_seff_reliability_pc_pc_RecoveryAction_m_PrimaryBehaviourOfRecoveryActionMustBeSet}

# pcm_pc_pc_seff_reliability_pc_pc_FailureHandlingEntity class attributes and methods

# pcm_pc_pc_qosannotations_pc_pc_SpecifiedQoSAnnotation class attributes and methods

# System class attributes and methods

# SpecifiedQoSAnnotation class attributes and methods

# pcm_pc_pc_qosannotations_pc_pc_SpecifiedOutputParameterAbstraction class attributes and methods

# pcm_pc_pc_qos_performance_pc_pc_SystemSpecifiedExecutionTime class attributes and methods
pcm_pc_pc_qos_performance_pc_pc_SystemSpecifiedExecutionTime_m_SystemSpecifiedExecutionTimeMustReferenceRequiredRoleOfASystem: Method = Method(name="SystemSpecifiedExecutionTimeMustReferenceRequiredRoleOfASystem", parameters={Parameter(name='pcm_pc_pc_context', type=StringType), Parameter(name='pcm_pc_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_pc_qos_performance_pc_pc_SystemSpecifiedExecutionTime.methods={pcm_pc_pc_qos_performance_pc_pc_SystemSpecifiedExecutionTime_m_SystemSpecifiedExecutionTimeMustReferenceRequiredRoleOfASystem}

# SpecifiedExecutionTime class attributes and methods

# pcm_pc_pc_qos_performance_pc_pc_SpecifiedExecutionTime class attributes and methods

# QoSAnnotations class attributes and methods

# pcm_pc_pc_qosannotations_pc_pc_QoSAnnotations class attributes and methods
pcm_pc_pc_qosannotations_pc_pc_QoSAnnotations_m_MultipleReliabilityAnnotationsPerExternalCallNotAllowed: Method = Method(name="MultipleReliabilityAnnotationsPerExternalCallNotAllowed", parameters={Parameter(name='pcm_pc_pc_context', type=StringType), Parameter(name='pcm_pc_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_pc_qosannotations_pc_pc_QoSAnnotations.methods={pcm_pc_pc_qosannotations_pc_pc_QoSAnnotations_m_MultipleReliabilityAnnotationsPerExternalCallNotAllowed}

# ExternalFailureOccurrenceDescription class attributes and methods

# pcm_pc_pc_system_pc_pc_System class attributes and methods
pcm_pc_pc_system_pc_pc_System_m_SystemMustHaveAtLeastOneProvidedRole: Method = Method(name="SystemMustHaveAtLeastOneProvidedRole", parameters={Parameter(name='pcm_pc_pc_diagnostics', type=StringType), Parameter(name='pcm_pc_pc_context', type=StringType)}, type=BooleanType)
pcm_pc_pc_system_pc_pc_System.methods={pcm_pc_pc_system_pc_pc_System_m_SystemMustHaveAtLeastOneProvidedRole}

# pcm_pc_pc_qos_performance_pc_pc_ComponentSpecifiedExecutionTime class attributes and methods

# pcm_pc_pc_qos_reliability_pc_pc_SpecifiedReliabilityAnnotation class attributes and methods
pcm_pc_pc_qos_reliability_pc_pc_SpecifiedReliabilityAnnotation_m_SumOfReliabilityAnnotationFailureProbabilitiesMustNotExceed1: Method = Method(name="SumOfReliabilityAnnotationFailureProbabilitiesMustNotExceed1", parameters={Parameter(name='pcm_pc_pc_diagnostics', type=StringType), Parameter(name='pcm_pc_pc_context', type=StringType)}, type=BooleanType)
pcm_pc_pc_qos_reliability_pc_pc_SpecifiedReliabilityAnnotation_m_MultipleExternalOccurrenceDescriptionsPerFailureTypeNotAllowed: Method = Method(name="MultipleExternalOccurrenceDescriptionsPerFailureTypeNotAllowed", parameters={Parameter(name='pcm_pc_pc_diagnostics', type=StringType), Parameter(name='pcm_pc_pc_context', type=StringType)}, type=BooleanType)
pcm_pc_pc_qos_reliability_pc_pc_SpecifiedReliabilityAnnotation_m_SpecifiedReliabilityAnnotationMustReferenceRequiredRoleOfASystem: Method = Method(name="SpecifiedReliabilityAnnotationMustReferenceRequiredRoleOfASystem", parameters={Parameter(name='pcm_pc_pc_diagnostics', type=StringType), Parameter(name='pcm_pc_pc_context', type=StringType)}, type=BooleanType)
pcm_pc_pc_qos_reliability_pc_pc_SpecifiedReliabilityAnnotation.methods={pcm_pc_pc_qos_reliability_pc_pc_SpecifiedReliabilityAnnotation_m_SpecifiedReliabilityAnnotationMustReferenceRequiredRoleOfASystem, pcm_pc_pc_qos_reliability_pc_pc_SpecifiedReliabilityAnnotation_m_MultipleExternalOccurrenceDescriptionsPerFailureTypeNotAllowed, pcm_pc_pc_qos_reliability_pc_pc_SpecifiedReliabilityAnnotation_m_SumOfReliabilityAnnotationFailureProbabilitiesMustNotExceed1}

# ResourceEnvironment class attributes and methods

# pcm_pc_pc_resourceenvironment_pc_pc_ResourceContainer class attributes and methods

# pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification class attributes and methods
pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification_MTTR: Property = Property(name="MTTR", type=FloatType)
pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification_MTTF: Property = Property(name="MTTF", type=FloatType)
pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification_requiredByContainer: Property = Property(name="requiredByContainer", type=BooleanType)
pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification_numberOfReplicas: Property = Property(name="numberOfReplicas", type=IntegerType)
pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification.attributes={pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification_requiredByContainer, pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification_MTTF, pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification_numberOfReplicas, pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification_MTTR}

# pcm_pc_pc_resourceenvironment_pc_pc_ResourceEnvironment class attributes and methods

# LinkingResource class attributes and methods

# ResourceContainer class attributes and methods

# pcm_pc_pc_resourceenvironment_pc_pc_LinkingResource class attributes and methods

# pcm_pc_pc_allocation_pc_pc_AllocationContext class attributes and methods
pcm_pc_pc_allocation_pc_pc_AllocationContext_m_OneAssemblyContextOrOneEventChannelShouldBeReferred: Method = Method(name="OneAssemblyContextOrOneEventChannelShouldBeReferred", parameters={Parameter(name='pcm_pc_pc_context', type=StringType), Parameter(name='pcm_pc_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_pc_allocation_pc_pc_AllocationContext.methods={pcm_pc_pc_allocation_pc_pc_AllocationContext_m_OneAssemblyContextOrOneEventChannelShouldBeReferred}

# pcm_pc_pc_resourceenvironment_pc_pc_CommunicationLinkResourceSpecification class attributes and methods
pcm_pc_pc_resourceenvironment_pc_pc_CommunicationLinkResourceSpecification_failureProbability: Property = Property(name="failureProbability", type=FloatType)
pcm_pc_pc_resourceenvironment_pc_pc_CommunicationLinkResourceSpecification.attributes={pcm_pc_pc_resourceenvironment_pc_pc_CommunicationLinkResourceSpecification_failureProbability}

# pcm_pc_pc_allocation_pc_pc_Allocation class attributes and methods
pcm_pc_pc_allocation_pc_pc_Allocation_m_EachAssemblyContextWithinSystemHasToBeAllocatedExactlyOnce: Method = Method(name="EachAssemblyContextWithinSystemHasToBeAllocatedExactlyOnce", parameters={Parameter(name='pcm_pc_pc_diagnostics', type=StringType), Parameter(name='pcm_pc_pc_context', type=StringType)}, type=BooleanType)
pcm_pc_pc_allocation_pc_pc_Allocation_m_CommunicatingServersHaveToBeConnectedByLinkingResource: Method = Method(name="CommunicatingServersHaveToBeConnectedByLinkingResource", parameters={Parameter(name='pcm_pc_pc_context', type=StringType), Parameter(name='pcm_pc_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_pc_allocation_pc_pc_Allocation.methods={pcm_pc_pc_allocation_pc_pc_Allocation_m_CommunicatingServersHaveToBeConnectedByLinkingResource, pcm_pc_pc_allocation_pc_pc_Allocation_m_EachAssemblyContextWithinSystemHasToBeAllocatedExactlyOnce}

# AllocationContext class attributes and methods

# pcm_pc_pc_subsystem_pc_pc_SubSystem class attributes and methods

# repository_pc_pc_RepositoryComponent class attributes and methods

# pcm_pc_pc_completions_pc_pc_Completion class attributes and methods

# pcm_pc_pc_completions_pc_pc_CompletionRepository class attributes and methods

# Completion class attributes and methods

# Allocation class attributes and methods

# pcm_pc_pc_completions_pc_pc_DelegatingExternalCallAction class attributes and methods

# ExternalCallAction class attributes and methods

# pcm_pc_pc_completions_pc_pc_NetworkDemandParametricResourceDemand class attributes and methods

# ParametricResourceDemand class attributes and methods

# Relationships
infrastructureCall__PCMRandomVariable6: BinaryAssociation = BinaryAssociation(
    name="infrastructureCall__PCMRandomVariable6",
    ends={
        Property(name="InfrastructureCall", type=pcm_pc_pc_core_pc_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="numberOfCalls__InfrastructureCall", type=seff_performance_pc_pc_InfrastructureCall, multiplicity=Multiplicity(0, 1))
    }
)
resourceCall__PCMRandomVariable7: BinaryAssociation = BinaryAssociation(
    name="resourceCall__PCMRandomVariable7",
    ends={
        Property(name="ResourceCall", type=pcm_pc_pc_core_pc_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="numberOfCalls__ResourceCall", type=seff_performance_pc_pc_ResourceCall, multiplicity=Multiplicity(0, 1))
    }
)
parametricResourceDemand_PCMRandomVariable8: BinaryAssociation = BinaryAssociation(
    name="parametricResourceDemand_PCMRandomVariable8",
    ends={
        Property(name="ParametricResourceDemand", type=pcm_pc_pc_core_pc_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="specification_ParametericResourceDemand", type=seff_performance_pc_pc_ParametricResourceDemand, multiplicity=Multiplicity(0, 1))
    }
)
loopAction_PCMRandomVariable9: BinaryAssociation = BinaryAssociation(
    name="loopAction_PCMRandomVariable9",
    ends={
        Property(name="LoopAction", type=pcm_pc_pc_core_pc_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="iterationCount_LoopAction", type=LoopAction, multiplicity=Multiplicity(0, 1))
    }
)
children0: BinaryAssociation = BinaryAssociation(
    name="children0",
    ends={
        Property(name="pcm_pc_pc_EObject", type=pcm_pc_pc_PointcutPointcut, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_PointcutPointcut", type=pcm_pc_pc_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
        Property(name="ClosedWorkload", type=pcm_pc_pc_core_pc_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="thinkTime_ClosedWorkload", type=ClosedWorkload, multiplicity=Multiplicity(0, 1))
    }
)
passiveResource_capacity_PCMRandomVariable4: BinaryAssociation = BinaryAssociation(
    name="passiveResource_capacity_PCMRandomVariable4",
    ends={
        Property(name="PassiveResource", type=pcm_pc_pc_core_pc_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="capacity_PassiveResource", type=PassiveResource, multiplicity=Multiplicity(0, 1))
    }
)
variableCharacterisation_Specification5: BinaryAssociation = BinaryAssociation(
    name="variableCharacterisation_Specification5",
    ends={
        Property(name="VariableCharacterisation", type=pcm_pc_pc_core_pc_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="specification_VariableCharacterisation", type=VariableCharacterisation, multiplicity=Multiplicity(0, 1))
    }
)
resourceInterfaceProvidingEntity__ResourceProvidedRole21: BinaryAssociation = BinaryAssociation(
    name="resourceInterfaceProvidingEntity__ResourceProvidedRole21",
    ends={
        Property(name="ResourceInterfaceProvidingEntity", type=pcm_pc_pc_entity_pc_pc_ResourceProvidedRole, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceProvidedRoles__ResourceInterfaceProvidingEntity", type=entity_pc_pc_ResourceInterfaceProvidingEntity, multiplicity=Multiplicity(0, 1))
    }
)
providedResourceInterface__ResourceProvidedRole22: BinaryAssociation = BinaryAssociation(
    name="providedResourceInterface__ResourceProvidedRole22",
    ends={
        Property(name="ResourceInterface", type=pcm_pc_pc_entity_pc_pc_ResourceProvidedRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_entity_pc_pc_ResourceProvidedRole", type=ResourceInterface, multiplicity=Multiplicity(0, 1))
    }
)
providedRoles_InterfaceProvidingEntity23: BinaryAssociation = BinaryAssociation(
    name="providedRoles_InterfaceProvidingEntity23",
    ends={
        Property(name="ProvidedRole", type=pcm_pc_pc_entity_pc_pc_InterfaceProvidingEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="providingEntity_ProvidedRole", type=ProvidedRole, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
guardedBranchTransition_PCMRandomVariable10: BinaryAssociation = BinaryAssociation(
    name="guardedBranchTransition_PCMRandomVariable10",
    ends={
        Property(name="GuardedBranchTransition", type=pcm_pc_pc_core_pc_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="branchCondition_GuardedBranchTransition", type=GuardedBranchTransition, multiplicity=Multiplicity(0, 1))
    }
)
specifiedExecutionTime_PCMRandomVariable11: BinaryAssociation = BinaryAssociation(
    name="specifiedExecutionTime_PCMRandomVariable11",
    ends={
        Property(name="SpecifiedExecutionTime", type=pcm_pc_pc_core_pc_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="specification_SpecifiedExecutionTime", type=qos_performance_pc_pc_SpecifiedExecutionTime, multiplicity=Multiplicity(0, 1))
    }
)
eventChannelSinkConnector__FilterCondition12: BinaryAssociation = BinaryAssociation(
    name="eventChannelSinkConnector__FilterCondition12",
    ends={
        Property(name="EventChannelSinkConnector", type=pcm_pc_pc_core_pc_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="filterCondition__EventChannelSinkConnector", type=composition_pc_pc_EventChannelSinkConnector, multiplicity=Multiplicity(0, 1))
    }
)
assemblyEventConnector__FilterCondition13: BinaryAssociation = BinaryAssociation(
    name="assemblyEventConnector__FilterCondition13",
    ends={
        Property(name="AssemblyEventConnector", type=pcm_pc_pc_core_pc_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="filterCondition__AssemblyEventConnector", type=composition_pc_pc_AssemblyEventConnector, multiplicity=Multiplicity(0, 1))
    }
)
loop_LoopIteration14: BinaryAssociation = BinaryAssociation(
    name="loop_LoopIteration14",
    ends={
        Property(name="Loop", type=pcm_pc_pc_core_pc_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="loopIteration_Loop", type=Loop, multiplicity=Multiplicity(0, 1))
    }
)
openWorkload_PCMRandomVariable15: BinaryAssociation = BinaryAssociation(
    name="openWorkload_PCMRandomVariable15",
    ends={
        Property(name="OpenWorkload", type=pcm_pc_pc_core_pc_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="interArrivalTime_OpenWorkload", type=OpenWorkload, multiplicity=Multiplicity(0, 1))
    }
)
delay_TimeSpecification16: BinaryAssociation = BinaryAssociation(
    name="delay_TimeSpecification16",
    ends={
        Property(name="Delay", type=pcm_pc_pc_core_pc_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="timeSpecification_Delay", type=Delay, multiplicity=Multiplicity(0, 1))
    }
)
communicationLinkResourceSpecifcation_throughput_PCMRandomVariable17: BinaryAssociation = BinaryAssociation(
    name="communicationLinkResourceSpecifcation_throughput_PCMRandomVariable17",
    ends={
        Property(name="CommunicationLinkResourceSpecification", type=pcm_pc_pc_core_pc_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="throughput_CommunicationLinkResourceSpecification", type=CommunicationLinkResourceSpecification, multiplicity=Multiplicity(0, 1))
    }
)
processingResourceSpecification_processingRate_PCMRandomVariable18: BinaryAssociation = BinaryAssociation(
    name="processingResourceSpecification_processingRate_PCMRandomVariable18",
    ends={
        Property(name="ProcessingResourceSpecification", type=pcm_pc_pc_core_pc_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="processingRate_ProcessingResourceSpecification", type=ProcessingResourceSpecification, multiplicity=Multiplicity(0, 1))
    }
)
communicationLinkResourceSpecification_latency_PCMRandomVariable19: BinaryAssociation = BinaryAssociation(
    name="communicationLinkResourceSpecification_latency_PCMRandomVariable19",
    ends={
        Property(name="CommunicationLinkResourceSpecification20", type=pcm_pc_pc_core_pc_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="latency_CommunicationLinkResourceSpecification", type=CommunicationLinkResourceSpecification, multiplicity=Multiplicity(0, 1))
    }
)
requiredRoles_InterfaceRequiringEntity24: BinaryAssociation = BinaryAssociation(
    name="requiredRoles_InterfaceRequiringEntity24",
    ends={
        Property(name="RequiredRole", type=pcm_pc_pc_entity_pc_pc_InterfaceRequiringEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="requiringEntity_RequiredRole", type=RequiredRole, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceRequiredRoles__ResourceInterfaceRequiringEntity25: BinaryAssociation = BinaryAssociation(
    name="resourceRequiredRoles__ResourceInterfaceRequiringEntity25",
    ends={
        Property(name="ResourceRequiredRole", type=pcm_pc_pc_entity_pc_pc_ResourceInterfaceRequiringEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceInterfaceRequiringEntity__ResourceRequiredRole", type=entity_pc_pc_ResourceRequiredRole, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredResourceInterface__ResourceRequiredRole26: BinaryAssociation = BinaryAssociation(
    name="requiredResourceInterface__ResourceRequiredRole26",
    ends={
        Property(name="ResourceInterface27", type=pcm_pc_pc_entity_pc_pc_ResourceRequiredRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_entity_pc_pc_ResourceRequiredRole", type=ResourceInterface, multiplicity=Multiplicity(0, 1))
    }
)
resourceInterfaceRequiringEntity__ResourceRequiredRole28: BinaryAssociation = BinaryAssociation(
    name="resourceInterfaceRequiringEntity__ResourceRequiredRole28",
    ends={
        Property(name="ResourceInterfaceRequiringEntity", type=pcm_pc_pc_entity_pc_pc_ResourceRequiredRole, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceRequiredRoles__ResourceInterfaceRequiringEntity", type=entity_pc_pc_ResourceInterfaceRequiringEntity, multiplicity=Multiplicity(0, 1))
    }
)
resourceProvidedRoles__ResourceInterfaceProvidingEntity29: BinaryAssociation = BinaryAssociation(
    name="resourceProvidedRoles__ResourceInterfaceProvidingEntity29",
    ends={
        Property(name="ResourceProvidedRole", type=pcm_pc_pc_entity_pc_pc_ResourceInterfaceProvidingEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceInterfaceProvidingEntity__ResourceProvidedRole", type=entity_pc_pc_ResourceProvidedRole, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceRequiredDelegationConnectors_ComposedStructure32: BinaryAssociation = BinaryAssociation(
    name="resourceRequiredDelegationConnectors_ComposedStructure32",
    ends={
        Property(name="ResourceRequiredDelegationConnector", type=pcm_pc_pc_composition_pc_pc_ComposedStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="parentStructure_ResourceRequiredDelegationConnector", type=composition_pc_pc_ResourceRequiredDelegationConnector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eventChannel__ComposedStructure33: BinaryAssociation = BinaryAssociation(
    name="eventChannel__ComposedStructure33",
    ends={
        Property(name="EventChannel", type=pcm_pc_pc_composition_pc_pc_ComposedStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="parentStructure__EventChannel", type=composition_pc_pc_EventChannel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connectors__ComposedStructure34: BinaryAssociation = BinaryAssociation(
    name="connectors__ComposedStructure34",
    ends={
        Property(name="Connector", type=pcm_pc_pc_composition_pc_pc_ComposedStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="parentStructure__Connector", type=composition_pc_pc_Connector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
innerResourceRequiredRole_ResourceRequiredDelegationConnector35: BinaryAssociation = BinaryAssociation(
    name="innerResourceRequiredRole_ResourceRequiredDelegationConnector35",
    ends={
        Property(name="entity_pc_pc_ResourceRequiredRole", type=pcm_pc_pc_composition_pc_pc_ResourceRequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_composition_pc_pc_ResourceRequiredDelegationConnector", type=entity_pc_pc_ResourceRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
parentStructure__Connector30: BinaryAssociation = BinaryAssociation(
    name="parentStructure__Connector30",
    ends={
        Property(name="ComposedStructure", type=pcm_pc_pc_composition_pc_pc_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="connectors__ComposedStructure", type=composition_pc_pc_ComposedStructure, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContexts__ComposedStructure31: BinaryAssociation = BinaryAssociation(
    name="assemblyContexts__ComposedStructure31",
    ends={
        Property(name="AssemblyContext", type=pcm_pc_pc_composition_pc_pc_ComposedStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="parentStructure__AssemblyContext", type=composition_pc_pc_AssemblyContext, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eventChannel__EventChannelSinkConnector57: BinaryAssociation = BinaryAssociation(
    name="eventChannel__EventChannelSinkConnector57",
    ends={
        Property(name="EventChannel58", type=pcm_pc_pc_composition_pc_pc_EventChannelSinkConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="eventChannelSinkConnector__EventChannel", type=composition_pc_pc_EventChannel, multiplicity=Multiplicity(0, 1))
    }
)
outerResourceRequiredRole_ResourceRequiredDelegationConnector36: BinaryAssociation = BinaryAssociation(
    name="outerResourceRequiredRole_ResourceRequiredDelegationConnector36",
    ends={
        Property(name="entity_pc_pc_ResourceRequiredRole38", type=pcm_pc_pc_composition_pc_pc_ResourceRequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_composition_pc_pc_ResourceRequiredDelegationConnector37", type=entity_pc_pc_ResourceRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
parentStructure_ResourceRequiredDelegationConnector39: BinaryAssociation = BinaryAssociation(
    name="parentStructure_ResourceRequiredDelegationConnector39",
    ends={
        Property(name="ComposedStructure40", type=pcm_pc_pc_composition_pc_pc_ResourceRequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceRequiredDelegationConnectors_ComposedStructure", type=composition_pc_pc_ComposedStructure, multiplicity=Multiplicity(0, 1))
    }
)
eventGroup__EventChannel41: BinaryAssociation = BinaryAssociation(
    name="eventGroup__EventChannel41",
    ends={
        Property(name="EventGroup", type=pcm_pc_pc_composition_pc_pc_EventChannel, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_composition_pc_pc_EventChannel", type=EventGroup, multiplicity=Multiplicity(0, 1))
    }
)
eventChannelSourceConnector__EventChannel42: BinaryAssociation = BinaryAssociation(
    name="eventChannelSourceConnector__EventChannel42",
    ends={
        Property(name="EventChannelSourceConnector", type=pcm_pc_pc_composition_pc_pc_EventChannel, multiplicity=Multiplicity(1, 1)),
        Property(name="eventChannel__EventChannelSourceConnector", type=composition_pc_pc_EventChannelSourceConnector, multiplicity=Multiplicity(0, 9999))
    }
)
eventChannelSinkConnector__EventChannel43: BinaryAssociation = BinaryAssociation(
    name="eventChannelSinkConnector__EventChannel43",
    ends={
        Property(name="EventChannelSinkConnector44", type=pcm_pc_pc_composition_pc_pc_EventChannel, multiplicity=Multiplicity(1, 1)),
        Property(name="eventChannel__EventChannelSinkConnector", type=composition_pc_pc_EventChannelSinkConnector, multiplicity=Multiplicity(0, 9999))
    }
)
parentStructure__EventChannel45: BinaryAssociation = BinaryAssociation(
    name="parentStructure__EventChannel45",
    ends={
        Property(name="ComposedStructure46", type=pcm_pc_pc_composition_pc_pc_EventChannel, multiplicity=Multiplicity(1, 1)),
        Property(name="eventChannel__ComposedStructure", type=composition_pc_pc_ComposedStructure, multiplicity=Multiplicity(0, 1))
    }
)
sourceRole__EventChannelSourceRole47: BinaryAssociation = BinaryAssociation(
    name="sourceRole__EventChannelSourceRole47",
    ends={
        Property(name="SourceRole", type=pcm_pc_pc_composition_pc_pc_EventChannelSourceConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_composition_pc_pc_EventChannelSourceConnector", type=SourceRole, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext__EventChannelSourceConnector48: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__EventChannelSourceConnector48",
    ends={
        Property(name="composition_pc_pc_AssemblyContext", type=pcm_pc_pc_composition_pc_pc_EventChannelSourceConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_composition_pc_pc_EventChannelSourceConnector49", type=composition_pc_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
eventChannel__EventChannelSourceConnector50: BinaryAssociation = BinaryAssociation(
    name="eventChannel__EventChannelSourceConnector50",
    ends={
        Property(name="EventChannel51", type=pcm_pc_pc_composition_pc_pc_EventChannelSourceConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="eventChannelSourceConnector__EventChannel", type=composition_pc_pc_EventChannel, multiplicity=Multiplicity(0, 1))
    }
)
sinkRole__EventChannelSinkConnector52: BinaryAssociation = BinaryAssociation(
    name="sinkRole__EventChannelSinkConnector52",
    ends={
        Property(name="SinkRole", type=pcm_pc_pc_composition_pc_pc_EventChannelSinkConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_composition_pc_pc_EventChannelSinkConnector", type=SinkRole, multiplicity=Multiplicity(0, 1))
    }
)
filterCondition__EventChannelSinkConnector53: BinaryAssociation = BinaryAssociation(
    name="filterCondition__EventChannelSinkConnector53",
    ends={
        Property(name="PCMRandomVariable", type=pcm_pc_pc_composition_pc_pc_EventChannelSinkConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="eventChannelSinkConnector__FilterCondition", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assemblyContext__EventChannelSinkConnector54: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__EventChannelSinkConnector54",
    ends={
        Property(name="composition_pc_pc_AssemblyContext56", type=pcm_pc_pc_composition_pc_pc_EventChannelSinkConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_composition_pc_pc_EventChannelSinkConnector55", type=composition_pc_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
innerRequiredRole_RequiredDelegationConnector66: BinaryAssociation = BinaryAssociation(
    name="innerRequiredRole_RequiredDelegationConnector66",
    ends={
        Property(name="OperationRequiredRole", type=pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector", type=OperationRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
outerRequiredRole_RequiredDelegationConnector67: BinaryAssociation = BinaryAssociation(
    name="outerRequiredRole_RequiredDelegationConnector67",
    ends={
        Property(name="OperationRequiredRole69", type=pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector68", type=OperationRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext_RequiredDelegationConnector70: BinaryAssociation = BinaryAssociation(
    name="assemblyContext_RequiredDelegationConnector70",
    ends={
        Property(name="composition_pc_pc_AssemblyContext72", type=pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector71", type=composition_pc_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
innerProvidedRole_ProvidedDelegationConnector59: BinaryAssociation = BinaryAssociation(
    name="innerProvidedRole_ProvidedDelegationConnector59",
    ends={
        Property(name="OperationProvidedRole", type=pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector", type=OperationProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
outerProvidedRole_ProvidedDelegationConnector60: BinaryAssociation = BinaryAssociation(
    name="outerProvidedRole_ProvidedDelegationConnector60",
    ends={
        Property(name="OperationProvidedRole62", type=pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector61", type=OperationProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext_ProvidedDelegationConnector63: BinaryAssociation = BinaryAssociation(
    name="assemblyContext_ProvidedDelegationConnector63",
    ends={
        Property(name="composition_pc_pc_AssemblyContext65", type=pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector64", type=composition_pc_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
requiringAssemblyContext_AssemblyConnector73: BinaryAssociation = BinaryAssociation(
    name="requiringAssemblyContext_AssemblyConnector73",
    ends={
        Property(name="composition_pc_pc_AssemblyContext74", type=pcm_pc_pc_composition_pc_pc_AssemblyConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_composition_pc_pc_AssemblyConnector", type=composition_pc_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
sourceRole__AssemblyEventConnector86: BinaryAssociation = BinaryAssociation(
    name="sourceRole__AssemblyEventConnector86",
    ends={
        Property(name="SourceRole88", type=pcm_pc_pc_composition_pc_pc_AssemblyEventConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_composition_pc_pc_AssemblyEventConnector87", type=SourceRole, multiplicity=Multiplicity(0, 1))
    }
)
sinkAssemblyContext__AssemblyEventConnector89: BinaryAssociation = BinaryAssociation(
    name="sinkAssemblyContext__AssemblyEventConnector89",
    ends={
        Property(name="composition_pc_pc_AssemblyContext91", type=pcm_pc_pc_composition_pc_pc_AssemblyEventConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_composition_pc_pc_AssemblyEventConnector90", type=composition_pc_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
sourceAssemblyContext__AssemblyEventConnector92: BinaryAssociation = BinaryAssociation(
    name="sourceAssemblyContext__AssemblyEventConnector92",
    ends={
        Property(name="composition_pc_pc_AssemblyContext94", type=pcm_pc_pc_composition_pc_pc_AssemblyEventConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_composition_pc_pc_AssemblyEventConnector93", type=composition_pc_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
filterCondition__AssemblyEventConnector95: BinaryAssociation = BinaryAssociation(
    name="filterCondition__AssemblyEventConnector95",
    ends={
        Property(name="PCMRandomVariable96", type=pcm_pc_pc_composition_pc_pc_AssemblyEventConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="assemblyEventConnector__FilterCondition", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
innerSourceRole__SourceRole97: BinaryAssociation = BinaryAssociation(
    name="innerSourceRole__SourceRole97",
    ends={
        Property(name="SourceRole98", type=pcm_pc_pc_composition_pc_pc_SourceDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_composition_pc_pc_SourceDelegationConnector", type=SourceRole, multiplicity=Multiplicity(0, 1))
    }
)
outerSourceRole__SourceRole99: BinaryAssociation = BinaryAssociation(
    name="outerSourceRole__SourceRole99",
    ends={
        Property(name="SourceRole101", type=pcm_pc_pc_composition_pc_pc_SourceDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_composition_pc_pc_SourceDelegationConnector100", type=SourceRole, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext__SourceDelegationConnector102: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__SourceDelegationConnector102",
    ends={
        Property(name="composition_pc_pc_AssemblyContext104", type=pcm_pc_pc_composition_pc_pc_SourceDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_composition_pc_pc_SourceDelegationConnector103", type=composition_pc_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext__SinkDelegationConnector105: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__SinkDelegationConnector105",
    ends={
        Property(name="composition_pc_pc_AssemblyContext106", type=pcm_pc_pc_composition_pc_pc_SinkDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_composition_pc_pc_SinkDelegationConnector", type=composition_pc_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
innerSinkRole__SinkRole107: BinaryAssociation = BinaryAssociation(
    name="innerSinkRole__SinkRole107",
    ends={
        Property(name="SinkRole109", type=pcm_pc_pc_composition_pc_pc_SinkDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_composition_pc_pc_SinkDelegationConnector108", type=SinkRole, multiplicity=Multiplicity(0, 1))
    }
)
outerSinkRole__SinkRole110: BinaryAssociation = BinaryAssociation(
    name="outerSinkRole__SinkRole110",
    ends={
        Property(name="SinkRole112", type=pcm_pc_pc_composition_pc_pc_SinkDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_composition_pc_pc_SinkDelegationConnector111", type=SinkRole, multiplicity=Multiplicity(0, 1))
    }
)
providedRole__AssemblyInfrastructureConnector113: BinaryAssociation = BinaryAssociation(
    name="providedRole__AssemblyInfrastructureConnector113",
    ends={
        Property(name="InfrastructureProvidedRole", type=pcm_pc_pc_composition_pc_pc_AssemblyInfrastructureConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_composition_pc_pc_AssemblyInfrastructureConnector", type=InfrastructureProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
requiredRole__AssemblyInfrastructureConnector114: BinaryAssociation = BinaryAssociation(
    name="requiredRole__AssemblyInfrastructureConnector114",
    ends={
        Property(name="InfrastructureRequiredRole", type=pcm_pc_pc_composition_pc_pc_AssemblyInfrastructureConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_composition_pc_pc_AssemblyInfrastructureConnector115", type=InfrastructureRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
providingAssemblyContext__AssemblyInfrastructureConnector116: BinaryAssociation = BinaryAssociation(
    name="providingAssemblyContext__AssemblyInfrastructureConnector116",
    ends={
        Property(name="composition_pc_pc_AssemblyContext118", type=pcm_pc_pc_composition_pc_pc_AssemblyInfrastructureConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_composition_pc_pc_AssemblyInfrastructureConnector117", type=composition_pc_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
requiringAssemblyContext__AssemblyInfrastructureConnector119: BinaryAssociation = BinaryAssociation(
    name="requiringAssemblyContext__AssemblyInfrastructureConnector119",
    ends={
        Property(name="composition_pc_pc_AssemblyContext121", type=pcm_pc_pc_composition_pc_pc_AssemblyInfrastructureConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_composition_pc_pc_AssemblyInfrastructureConnector120", type=composition_pc_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
providingAssemblyContext_AssemblyConnector75: BinaryAssociation = BinaryAssociation(
    name="providingAssemblyContext_AssemblyConnector75",
    ends={
        Property(name="composition_pc_pc_AssemblyContext77", type=pcm_pc_pc_composition_pc_pc_AssemblyConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_composition_pc_pc_AssemblyConnector76", type=composition_pc_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
providedRole_AssemblyConnector78: BinaryAssociation = BinaryAssociation(
    name="providedRole_AssemblyConnector78",
    ends={
        Property(name="OperationProvidedRole80", type=pcm_pc_pc_composition_pc_pc_AssemblyConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_composition_pc_pc_AssemblyConnector79", type=OperationProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
requiredRole_AssemblyConnector81: BinaryAssociation = BinaryAssociation(
    name="requiredRole_AssemblyConnector81",
    ends={
        Property(name="OperationRequiredRole83", type=pcm_pc_pc_composition_pc_pc_AssemblyConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_composition_pc_pc_AssemblyConnector82", type=OperationRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
sinkRole__AssemblyEventConnector84: BinaryAssociation = BinaryAssociation(
    name="sinkRole__AssemblyEventConnector84",
    ends={
        Property(name="SinkRole85", type=pcm_pc_pc_composition_pc_pc_AssemblyEventConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_composition_pc_pc_AssemblyEventConnector", type=SinkRole, multiplicity=Multiplicity(0, 1))
    }
)
innerRequiredRole__RequiredInfrastructureDelegationConnector130: BinaryAssociation = BinaryAssociation(
    name="innerRequiredRole__RequiredInfrastructureDelegationConnector130",
    ends={
        Property(name="InfrastructureRequiredRole131", type=pcm_pc_pc_composition_pc_pc_RequiredInfrastructureDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_composition_pc_pc_RequiredInfrastructureDelegationConnector", type=InfrastructureRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
outerRequiredRole__RequiredInfrastructureDelegationConnector132: BinaryAssociation = BinaryAssociation(
    name="outerRequiredRole__RequiredInfrastructureDelegationConnector132",
    ends={
        Property(name="InfrastructureRequiredRole134", type=pcm_pc_pc_composition_pc_pc_RequiredInfrastructureDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_composition_pc_pc_RequiredInfrastructureDelegationConnector133", type=InfrastructureRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext__RequiredInfrastructureDelegationConnector135: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__RequiredInfrastructureDelegationConnector135",
    ends={
        Property(name="composition_pc_pc_AssemblyContext137", type=pcm_pc_pc_composition_pc_pc_RequiredInfrastructureDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_composition_pc_pc_RequiredInfrastructureDelegationConnector136", type=composition_pc_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext__RequiredResourceDelegationConnector138: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__RequiredResourceDelegationConnector138",
    ends={
        Property(name="composition_pc_pc_AssemblyContext139", type=pcm_pc_pc_composition_pc_pc_RequiredResourceDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_composition_pc_pc_RequiredResourceDelegationConnector", type=composition_pc_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
innerRequiredRole__RequiredResourceDelegationConnector140: BinaryAssociation = BinaryAssociation(
    name="innerRequiredRole__RequiredResourceDelegationConnector140",
    ends={
        Property(name="entity_pc_pc_ResourceRequiredRole142", type=pcm_pc_pc_composition_pc_pc_RequiredResourceDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_composition_pc_pc_RequiredResourceDelegationConnector141", type=entity_pc_pc_ResourceRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
outerRequiredRole__RequiredResourceDelegationConnector143: BinaryAssociation = BinaryAssociation(
    name="outerRequiredRole__RequiredResourceDelegationConnector143",
    ends={
        Property(name="entity_pc_pc_ResourceRequiredRole145", type=pcm_pc_pc_composition_pc_pc_RequiredResourceDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_composition_pc_pc_RequiredResourceDelegationConnector144", type=entity_pc_pc_ResourceRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
parentStructure__AssemblyContext146: BinaryAssociation = BinaryAssociation(
    name="parentStructure__AssemblyContext146",
    ends={
        Property(name="ComposedStructure147", type=pcm_pc_pc_composition_pc_pc_AssemblyContext, multiplicity=Multiplicity(1, 1)),
        Property(name="assemblyContexts__ComposedStructure", type=composition_pc_pc_ComposedStructure, multiplicity=Multiplicity(0, 1))
    }
)
encapsulatedComponent__AssemblyContext148: BinaryAssociation = BinaryAssociation(
    name="encapsulatedComponent__AssemblyContext148",
    ends={
        Property(name="RepositoryComponent", type=pcm_pc_pc_composition_pc_pc_AssemblyContext, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_composition_pc_pc_AssemblyContext", type=RepositoryComponent, multiplicity=Multiplicity(0, 1))
    }
)
configParameterUsages__AssemblyContext149: BinaryAssociation = BinaryAssociation(
    name="configParameterUsages__AssemblyContext149",
    ends={
        Property(name="VariableUsage", type=pcm_pc_pc_composition_pc_pc_AssemblyContext, multiplicity=Multiplicity(1, 1)),
        Property(name="assemblyContext__VariableUsage", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
usageScenario_Workload150: BinaryAssociation = BinaryAssociation(
    name="usageScenario_Workload150",
    ends={
        Property(name="UsageScenario", type=pcm_pc_pc_usagemodel_pc_pc_Workload, multiplicity=Multiplicity(1, 1)),
        Property(name="workload_UsageScenario", type=UsageScenario, multiplicity=Multiplicity(0, 1))
    }
)
usageModel_UsageScenario151: BinaryAssociation = BinaryAssociation(
    name="usageModel_UsageScenario151",
    ends={
        Property(name="UsageModel", type=pcm_pc_pc_usagemodel_pc_pc_UsageScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="usageScenario_UsageModel", type=UsageModel, multiplicity=Multiplicity(0, 1))
    }
)
innerProvidedRole__ProvidedInfrastructureDelegationConnector122: BinaryAssociation = BinaryAssociation(
    name="innerProvidedRole__ProvidedInfrastructureDelegationConnector122",
    ends={
        Property(name="InfrastructureProvidedRole123", type=pcm_pc_pc_composition_pc_pc_ProvidedInfrastructureDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_composition_pc_pc_ProvidedInfrastructureDelegationConnector", type=InfrastructureProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
outerProvidedRole__ProvidedInfrastructureDelegationConnector124: BinaryAssociation = BinaryAssociation(
    name="outerProvidedRole__ProvidedInfrastructureDelegationConnector124",
    ends={
        Property(name="InfrastructureProvidedRole126", type=pcm_pc_pc_composition_pc_pc_ProvidedInfrastructureDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_composition_pc_pc_ProvidedInfrastructureDelegationConnector125", type=InfrastructureProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext__ProvidedInfrastructureDelegationConnector127: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__ProvidedInfrastructureDelegationConnector127",
    ends={
        Property(name="composition_pc_pc_AssemblyContext129", type=pcm_pc_pc_composition_pc_pc_ProvidedInfrastructureDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_composition_pc_pc_ProvidedInfrastructureDelegationConnector128", type=composition_pc_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
usageScenario_UsageModel160: BinaryAssociation = BinaryAssociation(
    name="usageScenario_UsageModel160",
    ends={
        Property(name="UsageScenario161", type=pcm_pc_pc_usagemodel_pc_pc_UsageModel, multiplicity=Multiplicity(1, 1)),
        Property(name="usageModel_UsageScenario", type=UsageScenario, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
userData_UsageModel162: BinaryAssociation = BinaryAssociation(
    name="userData_UsageModel162",
    ends={
        Property(name="UserData", type=pcm_pc_pc_usagemodel_pc_pc_UsageModel, multiplicity=Multiplicity(1, 1)),
        Property(name="usageModel_UserData", type=UserData, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
providedRole_EntryLevelSystemCall163: BinaryAssociation = BinaryAssociation(
    name="providedRole_EntryLevelSystemCall163",
    ends={
        Property(name="OperationProvidedRole164", type=pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall", type=OperationProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
operationSignature__EntryLevelSystemCall165: BinaryAssociation = BinaryAssociation(
    name="operationSignature__EntryLevelSystemCall165",
    ends={
        Property(name="OperationSignature", type=pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall166", type=OperationSignature, multiplicity=Multiplicity(0, 1))
    }
)
outputParameterUsages_EntryLevelSystemCall167: BinaryAssociation = BinaryAssociation(
    name="outputParameterUsages_EntryLevelSystemCall167",
    ends={
        Property(name="VariableUsage168", type=pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall, multiplicity=Multiplicity(1, 1)),
        Property(name="entryLevelSystemCall_OutputParameterUsage", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputParameterUsages_EntryLevelSystemCall169: BinaryAssociation = BinaryAssociation(
    name="inputParameterUsages_EntryLevelSystemCall169",
    ends={
        Property(name="VariableUsage170", type=pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall, multiplicity=Multiplicity(1, 1)),
        Property(name="entryLevelSystemCall_InputParameterUsage", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
scenarioBehaviour_UsageScenario152: BinaryAssociation = BinaryAssociation(
    name="scenarioBehaviour_UsageScenario152",
    ends={
        Property(name="ScenarioBehaviour", type=pcm_pc_pc_usagemodel_pc_pc_UsageScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="usageScenario_SenarioBehaviour", type=ScenarioBehaviour, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
workload_UsageScenario153: BinaryAssociation = BinaryAssociation(
    name="workload_UsageScenario153",
    ends={
        Property(name="Workload", type=pcm_pc_pc_usagemodel_pc_pc_UsageScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="usageScenario_Workload", type=Workload, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assemblyContext_userData154: BinaryAssociation = BinaryAssociation(
    name="assemblyContext_userData154",
    ends={
        Property(name="composition_pc_pc_AssemblyContext155", type=pcm_pc_pc_usagemodel_pc_pc_UserData, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_usagemodel_pc_pc_UserData", type=composition_pc_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
usageModel_UserData156: BinaryAssociation = BinaryAssociation(
    name="usageModel_UserData156",
    ends={
        Property(name="UsageModel157", type=pcm_pc_pc_usagemodel_pc_pc_UserData, multiplicity=Multiplicity(1, 1)),
        Property(name="userData_UsageModel", type=UsageModel, multiplicity=Multiplicity(0, 1))
    }
)
userDataParameterUsages_UserData158: BinaryAssociation = BinaryAssociation(
    name="userDataParameterUsages_UserData158",
    ends={
        Property(name="VariableUsage159", type=pcm_pc_pc_usagemodel_pc_pc_UserData, multiplicity=Multiplicity(1, 1)),
        Property(name="userData_VariableUsage", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
usageScenario_SenarioBehaviour176: BinaryAssociation = BinaryAssociation(
    name="usageScenario_SenarioBehaviour176",
    ends={
        Property(name="UsageScenario177", type=pcm_pc_pc_usagemodel_pc_pc_ScenarioBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="scenarioBehaviour_UsageScenario", type=UsageScenario, multiplicity=Multiplicity(0, 1))
    }
)
branchTransition_ScenarioBehaviour178: BinaryAssociation = BinaryAssociation(
    name="branchTransition_ScenarioBehaviour178",
    ends={
        Property(name="BranchTransition", type=pcm_pc_pc_usagemodel_pc_pc_ScenarioBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="branchedBehaviour_BranchTransition", type=BranchTransition, multiplicity=Multiplicity(0, 1))
    }
)
loop_ScenarioBehaviour179: BinaryAssociation = BinaryAssociation(
    name="loop_ScenarioBehaviour179",
    ends={
        Property(name="Loop180", type=pcm_pc_pc_usagemodel_pc_pc_ScenarioBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="bodyBehaviour_Loop", type=Loop, multiplicity=Multiplicity(0, 1))
    }
)
actions_ScenarioBehaviour181: BinaryAssociation = BinaryAssociation(
    name="actions_ScenarioBehaviour181",
    ends={
        Property(name="AbstractUserAction182", type=pcm_pc_pc_usagemodel_pc_pc_ScenarioBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="scenarioBehaviour_AbstractUserAction", type=AbstractUserAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
successor171: BinaryAssociation = BinaryAssociation(
    name="successor171",
    ends={
        Property(name="AbstractUserAction", type=pcm_pc_pc_usagemodel_pc_pc_AbstractUserAction, multiplicity=Multiplicity(1, 1)),
        Property(name="predecessor", type=AbstractUserAction, multiplicity=Multiplicity(0, 1))
    }
)
predecessor172: BinaryAssociation = BinaryAssociation(
    name="predecessor172",
    ends={
        Property(name="AbstractUserAction173", type=pcm_pc_pc_usagemodel_pc_pc_AbstractUserAction, multiplicity=Multiplicity(1, 1)),
        Property(name="successor", type=AbstractUserAction, multiplicity=Multiplicity(0, 1))
    }
)
scenarioBehaviour_AbstractUserAction174: BinaryAssociation = BinaryAssociation(
    name="scenarioBehaviour_AbstractUserAction174",
    ends={
        Property(name="ScenarioBehaviour175", type=pcm_pc_pc_usagemodel_pc_pc_AbstractUserAction, multiplicity=Multiplicity(1, 1)),
        Property(name="actions_ScenarioBehaviour", type=ScenarioBehaviour, multiplicity=Multiplicity(0, 1))
    }
)
branchTransitions_Branch186: BinaryAssociation = BinaryAssociation(
    name="branchTransitions_Branch186",
    ends={
        Property(name="BranchTransition187", type=pcm_pc_pc_usagemodel_pc_pc_Branch, multiplicity=Multiplicity(1, 1)),
        Property(name="branch_BranchTransition", type=BranchTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
loopIteration_Loop188: BinaryAssociation = BinaryAssociation(
    name="loopIteration_Loop188",
    ends={
        Property(name="PCMRandomVariable189", type=pcm_pc_pc_usagemodel_pc_pc_Loop, multiplicity=Multiplicity(1, 1)),
        Property(name="loop_LoopIteration", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bodyBehaviour_Loop190: BinaryAssociation = BinaryAssociation(
    name="bodyBehaviour_Loop190",
    ends={
        Property(name="ScenarioBehaviour191", type=pcm_pc_pc_usagemodel_pc_pc_Loop, multiplicity=Multiplicity(1, 1)),
        Property(name="loop_ScenarioBehaviour", type=ScenarioBehaviour, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
branch_BranchTransition183: BinaryAssociation = BinaryAssociation(
    name="branch_BranchTransition183",
    ends={
        Property(name="Branch", type=pcm_pc_pc_usagemodel_pc_pc_BranchTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="branchTransitions_Branch", type=Branch, multiplicity=Multiplicity(0, 1))
    }
)
branchedBehaviour_BranchTransition184: BinaryAssociation = BinaryAssociation(
    name="branchedBehaviour_BranchTransition184",
    ends={
        Property(name="ScenarioBehaviour185", type=pcm_pc_pc_usagemodel_pc_pc_BranchTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="branchTransition_ScenarioBehaviour", type=ScenarioBehaviour, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
timeSpecification_Delay194: BinaryAssociation = BinaryAssociation(
    name="timeSpecification_Delay194",
    ends={
        Property(name="PCMRandomVariable195", type=pcm_pc_pc_usagemodel_pc_pc_Delay, multiplicity=Multiplicity(1, 1)),
        Property(name="delay_TimeSpecification", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thinkTime_ClosedWorkload196: BinaryAssociation = BinaryAssociation(
    name="thinkTime_ClosedWorkload196",
    ends={
        Property(name="PCMRandomVariable197", type=pcm_pc_pc_usagemodel_pc_pc_ClosedWorkload, multiplicity=Multiplicity(1, 1)),
        Property(name="closedWorkload_PCMRandomVariable", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
capacity_PassiveResource198: BinaryAssociation = BinaryAssociation(
    name="capacity_PassiveResource198",
    ends={
        Property(name="PCMRandomVariable199", type=pcm_pc_pc_repository_pc_pc_PassiveResource, multiplicity=Multiplicity(1, 1)),
        Property(name="passiveResource_capacity_PCMRandomVariable", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
basicComponent_PassiveResource200: BinaryAssociation = BinaryAssociation(
    name="basicComponent_PassiveResource200",
    ends={
        Property(name="BasicComponent", type=pcm_pc_pc_repository_pc_pc_PassiveResource, multiplicity=Multiplicity(1, 1)),
        Property(name="passiveResource_BasicComponent", type=BasicComponent, multiplicity=Multiplicity(0, 1))
    }
)
interArrivalTime_OpenWorkload192: BinaryAssociation = BinaryAssociation(
    name="interArrivalTime_OpenWorkload192",
    ends={
        Property(name="PCMRandomVariable193", type=pcm_pc_pc_usagemodel_pc_pc_OpenWorkload, multiplicity=Multiplicity(1, 1)),
        Property(name="openWorkload_PCMRandomVariable", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
serviceEffectSpecifications__BasicComponent202: BinaryAssociation = BinaryAssociation(
    name="serviceEffectSpecifications__BasicComponent202",
    ends={
        Property(name="ServiceEffectSpecification", type=pcm_pc_pc_repository_pc_pc_BasicComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="basicComponent_ServiceEffectSpecification", type=ServiceEffectSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
passiveResource_BasicComponent203: BinaryAssociation = BinaryAssociation(
    name="passiveResource_BasicComponent203",
    ends={
        Property(name="PassiveResource204", type=pcm_pc_pc_repository_pc_pc_BasicComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="basicComponent_PassiveResource", type=PassiveResource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceTimeoutFailureType__PassiveResource201: BinaryAssociation = BinaryAssociation(
    name="resourceTimeoutFailureType__PassiveResource201",
    ends={
        Property(name="ResourceTimeoutFailureType", type=pcm_pc_pc_repository_pc_pc_PassiveResource, multiplicity=Multiplicity(1, 1)),
        Property(name="passiveResource__ResourceTimeoutFailureType", type=ResourceTimeoutFailureType, multiplicity=Multiplicity(0, 1))
    }
)
parentCompleteComponentTypes205: BinaryAssociation = BinaryAssociation(
    name="parentCompleteComponentTypes205",
    ends={
        Property(name="CompleteComponentType", type=pcm_pc_pc_repository_pc_pc_ImplementationComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_repository_pc_pc_ImplementationComponentType", type=CompleteComponentType, multiplicity=Multiplicity(0, 9999))
    }
)
componentParameterUsage_ImplementationComponentType206: BinaryAssociation = BinaryAssociation(
    name="componentParameterUsage_ImplementationComponentType206",
    ends={
        Property(name="VariableUsage208", type=pcm_pc_pc_repository_pc_pc_ImplementationComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_repository_pc_pc_ImplementationComponentType207", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
repository__RepositoryComponent209: BinaryAssociation = BinaryAssociation(
    name="repository__RepositoryComponent209",
    ends={
        Property(name="Repository", type=pcm_pc_pc_repository_pc_pc_RepositoryComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="components__Repository", type=Repository, multiplicity=Multiplicity(0, 1))
    }
)
providingEntity_ProvidedRole210: BinaryAssociation = BinaryAssociation(
    name="providingEntity_ProvidedRole210",
    ends={
        Property(name="InterfaceProvidingEntity", type=pcm_pc_pc_repository_pc_pc_ProvidedRole, multiplicity=Multiplicity(1, 1)),
        Property(name="providedRoles_InterfaceProvidingEntity", type=entity_pc_pc_InterfaceProvidingEntity, multiplicity=Multiplicity(0, 1))
    }
)
dataType__Parameter211: BinaryAssociation = BinaryAssociation(
    name="dataType__Parameter211",
    ends={
        Property(name="DataType", type=pcm_pc_pc_repository_pc_pc_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_repository_pc_pc_Parameter", type=DataType, multiplicity=Multiplicity(0, 1))
    }
)
infrastructureSignature__Parameter212: BinaryAssociation = BinaryAssociation(
    name="infrastructureSignature__Parameter212",
    ends={
        Property(name="InfrastructureSignature", type=pcm_pc_pc_repository_pc_pc_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameters__InfrastructureSignature", type=InfrastructureSignature, multiplicity=Multiplicity(0, 1))
    }
)
operationSignature__Parameter213: BinaryAssociation = BinaryAssociation(
    name="operationSignature__Parameter213",
    ends={
        Property(name="OperationSignature214", type=pcm_pc_pc_repository_pc_pc_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameters__OperationSignature", type=OperationSignature, multiplicity=Multiplicity(0, 1))
    }
)
eventType__Parameter215: BinaryAssociation = BinaryAssociation(
    name="eventType__Parameter215",
    ends={
        Property(name="EventType", type=pcm_pc_pc_repository_pc_pc_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameter__EventType", type=EventType, multiplicity=Multiplicity(0, 1))
    }
)
components__Repository219: BinaryAssociation = BinaryAssociation(
    name="components__Repository219",
    ends={
        Property(name="RepositoryComponent220", type=pcm_pc_pc_repository_pc_pc_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="repository__RepositoryComponent", type=RepositoryComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
interfaces__Repository221: BinaryAssociation = BinaryAssociation(
    name="interfaces__Repository221",
    ends={
        Property(name="Interface", type=pcm_pc_pc_repository_pc_pc_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="repository__Interface", type=Interface, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
failureTypes__Repository222: BinaryAssociation = BinaryAssociation(
    name="failureTypes__Repository222",
    ends={
        Property(name="FailureType", type=pcm_pc_pc_repository_pc_pc_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="repository__FailureType", type=FailureType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataTypes__Repository223: BinaryAssociation = BinaryAssociation(
    name="dataTypes__Repository223",
    ends={
        Property(name="DataType224", type=pcm_pc_pc_repository_pc_pc_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="repository__DataType", type=DataType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentInterfaces__Interface225: BinaryAssociation = BinaryAssociation(
    name="parentInterfaces__Interface225",
    ends={
        Property(name="Interface226", type=pcm_pc_pc_repository_pc_pc_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_repository_pc_pc_Interface", type=Interface, multiplicity=Multiplicity(0, 9999))
    }
)
protocols__Interface227: BinaryAssociation = BinaryAssociation(
    name="protocols__Interface227",
    ends={
        Property(name="Protocol", type=pcm_pc_pc_repository_pc_pc_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_repository_pc_pc_Interface228", type=Protocol, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceSignature__Parameter216: BinaryAssociation = BinaryAssociation(
    name="resourceSignature__Parameter216",
    ends={
        Property(name="ResourceSignature", type=pcm_pc_pc_repository_pc_pc_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameter__ResourceSignature", type=ResourceSignature, multiplicity=Multiplicity(0, 1))
    }
)
repository__DataType217: BinaryAssociation = BinaryAssociation(
    name="repository__DataType217",
    ends={
        Property(name="Repository218", type=pcm_pc_pc_repository_pc_pc_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="dataTypes__Repository", type=Repository, multiplicity=Multiplicity(0, 1))
    }
)
parameter232: BinaryAssociation = BinaryAssociation(
    name="parameter232",
    ends={
        Property(name="Parameter", type=pcm_pc_pc_repository_pc_pc_RequiredCharacterisation, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_repository_pc_pc_RequiredCharacterisation", type=Parameter_, multiplicity=Multiplicity(0, 1))
    }
)
interface_RequiredCharacterisation233: BinaryAssociation = BinaryAssociation(
    name="interface_RequiredCharacterisation233",
    ends={
        Property(name="Interface234", type=pcm_pc_pc_repository_pc_pc_RequiredCharacterisation, multiplicity=Multiplicity(1, 1)),
        Property(name="requiredCharacterisations", type=Interface, multiplicity=Multiplicity(0, 1))
    }
)
eventTypes__EventGroup235: BinaryAssociation = BinaryAssociation(
    name="eventTypes__EventGroup235",
    ends={
        Property(name="EventType236", type=pcm_pc_pc_repository_pc_pc_EventGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="eventGroup__EventType", type=EventType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameter__EventType237: BinaryAssociation = BinaryAssociation(
    name="parameter__EventType237",
    ends={
        Property(name="Parameter238", type=pcm_pc_pc_repository_pc_pc_EventType, multiplicity=Multiplicity(1, 1)),
        Property(name="eventType__Parameter", type=Parameter_, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eventGroup__EventType239: BinaryAssociation = BinaryAssociation(
    name="eventGroup__EventType239",
    ends={
        Property(name="EventGroup240", type=pcm_pc_pc_repository_pc_pc_EventType, multiplicity=Multiplicity(1, 1)),
        Property(name="eventTypes__EventGroup", type=EventGroup, multiplicity=Multiplicity(0, 1))
    }
)
exceptions__Signature241: BinaryAssociation = BinaryAssociation(
    name="exceptions__Signature241",
    ends={
        Property(name="ExceptionType", type=pcm_pc_pc_repository_pc_pc_Signature, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_repository_pc_pc_Signature", type=ExceptionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
failureType242: BinaryAssociation = BinaryAssociation(
    name="failureType242",
    ends={
        Property(name="FailureType244", type=pcm_pc_pc_repository_pc_pc_Signature, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_repository_pc_pc_Signature243", type=FailureType, multiplicity=Multiplicity(0, 9999))
    }
)
parameters__InfrastructureSignature245: BinaryAssociation = BinaryAssociation(
    name="parameters__InfrastructureSignature245",
    ends={
        Property(name="Parameter246", type=pcm_pc_pc_repository_pc_pc_InfrastructureSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="infrastructureSignature__Parameter", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
infrastructureInterface__InfrastructureSignature247: BinaryAssociation = BinaryAssociation(
    name="infrastructureInterface__InfrastructureSignature247",
    ends={
        Property(name="InfrastructureInterface", type=pcm_pc_pc_repository_pc_pc_InfrastructureSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="infrastructureSignatures__InfrastructureInterface", type=InfrastructureInterface, multiplicity=Multiplicity(0, 1))
    }
)
requiredCharacterisations229: BinaryAssociation = BinaryAssociation(
    name="requiredCharacterisations229",
    ends={
        Property(name="RequiredCharacterisation", type=pcm_pc_pc_repository_pc_pc_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="interface_RequiredCharacterisation", type=RequiredCharacterisation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
repository__Interface230: BinaryAssociation = BinaryAssociation(
    name="repository__Interface230",
    ends={
        Property(name="Repository231", type=pcm_pc_pc_repository_pc_pc_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="interfaces__Repository", type=Repository, multiplicity=Multiplicity(0, 1))
    }
)
requiringEntity_RequiredRole252: BinaryAssociation = BinaryAssociation(
    name="requiringEntity_RequiredRole252",
    ends={
        Property(name="InterfaceRequiringEntity", type=pcm_pc_pc_repository_pc_pc_RequiredRole, multiplicity=Multiplicity(1, 1)),
        Property(name="requiredRoles_InterfaceRequiringEntity", type=entity_pc_pc_InterfaceRequiringEntity, multiplicity=Multiplicity(0, 1))
    }
)
interface__OperationSignature253: BinaryAssociation = BinaryAssociation(
    name="interface__OperationSignature253",
    ends={
        Property(name="OperationInterface", type=pcm_pc_pc_repository_pc_pc_OperationSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="signatures__OperationInterface", type=OperationInterface, multiplicity=Multiplicity(0, 1))
    }
)
parameters__OperationSignature254: BinaryAssociation = BinaryAssociation(
    name="parameters__OperationSignature254",
    ends={
        Property(name="Parameter255", type=pcm_pc_pc_repository_pc_pc_OperationSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="operationSignature__Parameter", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnType__OperationSignature256: BinaryAssociation = BinaryAssociation(
    name="returnType__OperationSignature256",
    ends={
        Property(name="DataType257", type=pcm_pc_pc_repository_pc_pc_OperationSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_repository_pc_pc_OperationSignature", type=DataType, multiplicity=Multiplicity(0, 1))
    }
)
signatures__OperationInterface258: BinaryAssociation = BinaryAssociation(
    name="signatures__OperationInterface258",
    ends={
        Property(name="OperationSignature259", type=pcm_pc_pc_repository_pc_pc_OperationInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="interface__OperationSignature", type=OperationSignature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredInterface__OperationRequiredRole260: BinaryAssociation = BinaryAssociation(
    name="requiredInterface__OperationRequiredRole260",
    ends={
        Property(name="OperationInterface261", type=pcm_pc_pc_repository_pc_pc_OperationRequiredRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_repository_pc_pc_OperationRequiredRole", type=OperationInterface, multiplicity=Multiplicity(0, 1))
    }
)
infrastructureSignatures__InfrastructureInterface248: BinaryAssociation = BinaryAssociation(
    name="infrastructureSignatures__InfrastructureInterface248",
    ends={
        Property(name="InfrastructureSignature249", type=pcm_pc_pc_repository_pc_pc_InfrastructureInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="infrastructureInterface__InfrastructureSignature", type=InfrastructureSignature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredInterface__InfrastructureRequiredRole250: BinaryAssociation = BinaryAssociation(
    name="requiredInterface__InfrastructureRequiredRole250",
    ends={
        Property(name="InfrastructureInterface251", type=pcm_pc_pc_repository_pc_pc_InfrastructureRequiredRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_repository_pc_pc_InfrastructureRequiredRole", type=InfrastructureInterface, multiplicity=Multiplicity(0, 1))
    }
)
providedInterface__OperationProvidedRole266: BinaryAssociation = BinaryAssociation(
    name="providedInterface__OperationProvidedRole266",
    ends={
        Property(name="OperationInterface267", type=pcm_pc_pc_repository_pc_pc_OperationProvidedRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_repository_pc_pc_OperationProvidedRole", type=OperationInterface, multiplicity=Multiplicity(0, 1))
    }
)
providedInterface__InfrastructureProvidedRole268: BinaryAssociation = BinaryAssociation(
    name="providedInterface__InfrastructureProvidedRole268",
    ends={
        Property(name="InfrastructureInterface269", type=pcm_pc_pc_repository_pc_pc_InfrastructureProvidedRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_repository_pc_pc_InfrastructureProvidedRole", type=InfrastructureInterface, multiplicity=Multiplicity(0, 1))
    }
)
parentProvidesComponentTypes270: BinaryAssociation = BinaryAssociation(
    name="parentProvidesComponentTypes270",
    ends={
        Property(name="ProvidesComponentType", type=pcm_pc_pc_repository_pc_pc_CompleteComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_repository_pc_pc_CompleteComponentType", type=ProvidesComponentType, multiplicity=Multiplicity(0, 9999))
    }
)
eventGroup__SourceRole262: BinaryAssociation = BinaryAssociation(
    name="eventGroup__SourceRole262",
    ends={
        Property(name="EventGroup263", type=pcm_pc_pc_repository_pc_pc_SourceRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_repository_pc_pc_SourceRole", type=EventGroup, multiplicity=Multiplicity(0, 1))
    }
)
eventGroup__SinkRole264: BinaryAssociation = BinaryAssociation(
    name="eventGroup__SinkRole264",
    ends={
        Property(name="EventGroup265", type=pcm_pc_pc_repository_pc_pc_SinkRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_repository_pc_pc_SinkRole", type=EventGroup, multiplicity=Multiplicity(0, 1))
    }
)
innerType_CollectionDataType271: BinaryAssociation = BinaryAssociation(
    name="innerType_CollectionDataType271",
    ends={
        Property(name="DataType272", type=pcm_pc_pc_repository_pc_pc_CollectionDataType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_repository_pc_pc_CollectionDataType", type=DataType, multiplicity=Multiplicity(0, 1))
    }
)
innerDeclaration_CompositeDataType274: BinaryAssociation = BinaryAssociation(
    name="innerDeclaration_CompositeDataType274",
    ends={
        Property(name="InnerDeclaration", type=pcm_pc_pc_repository_pc_pc_CompositeDataType, multiplicity=Multiplicity(1, 1)),
        Property(name="compositeDataType_InnerDeclaration", type=InnerDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
datatype_InnerDeclaration275: BinaryAssociation = BinaryAssociation(
    name="datatype_InnerDeclaration275",
    ends={
        Property(name="DataType276", type=pcm_pc_pc_repository_pc_pc_InnerDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_repository_pc_pc_InnerDeclaration", type=DataType, multiplicity=Multiplicity(0, 1))
    }
)
compositeDataType_InnerDeclaration277: BinaryAssociation = BinaryAssociation(
    name="compositeDataType_InnerDeclaration277",
    ends={
        Property(name="CompositeDataType278", type=pcm_pc_pc_repository_pc_pc_InnerDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="innerDeclaration_CompositeDataType", type=CompositeDataType, multiplicity=Multiplicity(0, 1))
    }
)
parameter__ResourceSignature279: BinaryAssociation = BinaryAssociation(
    name="parameter__ResourceSignature279",
    ends={
        Property(name="Parameter280", type=pcm_pc_pc_resourcetype_pc_pc_ResourceSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceSignature__Parameter", type=Parameter_, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resourceInterface__ResourceSignature281: BinaryAssociation = BinaryAssociation(
    name="resourceInterface__ResourceSignature281",
    ends={
        Property(name="ResourceInterface282", type=pcm_pc_pc_resourcetype_pc_pc_ResourceSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceSignatures__ResourceInterface", type=ResourceInterface, multiplicity=Multiplicity(0, 1))
    }
)
hardwareInducedFailureType__ProcessingResourceType283: BinaryAssociation = BinaryAssociation(
    name="hardwareInducedFailureType__ProcessingResourceType283",
    ends={
        Property(name="HardwareInducedFailureType", type=pcm_pc_pc_resourcetype_pc_pc_ProcessingResourceType, multiplicity=Multiplicity(1, 1)),
        Property(name="processingResourceType__HardwareInducedFailureType", type=HardwareInducedFailureType, multiplicity=Multiplicity(0, 1))
    }
)
parentType_CompositeDataType273: BinaryAssociation = BinaryAssociation(
    name="parentType_CompositeDataType273",
    ends={
        Property(name="CompositeDataType", type=pcm_pc_pc_repository_pc_pc_CompositeDataType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_repository_pc_pc_CompositeDataType", type=CompositeDataType, multiplicity=Multiplicity(0, 9999))
    }
)
resourceInterfaces__ResourceRepository285: BinaryAssociation = BinaryAssociation(
    name="resourceInterfaces__ResourceRepository285",
    ends={
        Property(name="ResourceInterface286", type=pcm_pc_pc_resourcetype_pc_pc_ResourceRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceRepository__ResourceInterface", type=ResourceInterface, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
schedulingPolicies__ResourceRepository287: BinaryAssociation = BinaryAssociation(
    name="schedulingPolicies__ResourceRepository287",
    ends={
        Property(name="SchedulingPolicy", type=pcm_pc_pc_resourcetype_pc_pc_ResourceRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceRepository__SchedulingPolicy", type=SchedulingPolicy, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
availableResourceTypes_ResourceRepository288: BinaryAssociation = BinaryAssociation(
    name="availableResourceTypes_ResourceRepository288",
    ends={
        Property(name="ResourceType", type=pcm_pc_pc_resourcetype_pc_pc_ResourceRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceRepository_ResourceType", type=ResourceType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceRepository__SchedulingPolicy289: BinaryAssociation = BinaryAssociation(
    name="resourceRepository__SchedulingPolicy289",
    ends={
        Property(name="ResourceRepository290", type=pcm_pc_pc_resourcetype_pc_pc_SchedulingPolicy, multiplicity=Multiplicity(1, 1)),
        Property(name="schedulingPolicies__ResourceRepository", type=ResourceRepository, multiplicity=Multiplicity(0, 1))
    }
)
networkInducedFailureType__CommunicationLinkResourceType291: BinaryAssociation = BinaryAssociation(
    name="networkInducedFailureType__CommunicationLinkResourceType291",
    ends={
        Property(name="NetworkInducedFailureType", type=pcm_pc_pc_resourcetype_pc_pc_CommunicationLinkResourceType, multiplicity=Multiplicity(1, 1)),
        Property(name="communicationLinkResourceType__NetworkInducedFailureType", type=NetworkInducedFailureType, multiplicity=Multiplicity(0, 1))
    }
)
resourceRepository__ResourceInterface292: BinaryAssociation = BinaryAssociation(
    name="resourceRepository__ResourceInterface292",
    ends={
        Property(name="ResourceRepository293", type=pcm_pc_pc_resourcetype_pc_pc_ResourceInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceInterfaces__ResourceRepository", type=ResourceRepository, multiplicity=Multiplicity(0, 1))
    }
)
resourceSignatures__ResourceInterface294: BinaryAssociation = BinaryAssociation(
    name="resourceSignatures__ResourceInterface294",
    ends={
        Property(name="ResourceSignature295", type=pcm_pc_pc_resourcetype_pc_pc_ResourceInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceInterface__ResourceSignature", type=ResourceSignature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceRepository_ResourceType284: BinaryAssociation = BinaryAssociation(
    name="resourceRepository_ResourceType284",
    ends={
        Property(name="ResourceRepository", type=pcm_pc_pc_resourcetype_pc_pc_ResourceType, multiplicity=Multiplicity(1, 1)),
        Property(name="availableResourceTypes_ResourceRepository", type=ResourceRepository, multiplicity=Multiplicity(0, 1))
    }
)
userData_VariableUsage298: BinaryAssociation = BinaryAssociation(
    name="userData_VariableUsage298",
    ends={
        Property(name="UserData299", type=pcm_pc_pc_parameter_pc_pc_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="userDataParameterUsages_UserData", type=UserData, multiplicity=Multiplicity(0, 1))
    }
)
callAction__VariableUsage300: BinaryAssociation = BinaryAssociation(
    name="callAction__VariableUsage300",
    ends={
        Property(name="CallAction", type=pcm_pc_pc_parameter_pc_pc_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="inputVariableUsages__CallAction", type=CallAction, multiplicity=Multiplicity(0, 1))
    }
)
synchronisationPoint_VariableUsage301: BinaryAssociation = BinaryAssociation(
    name="synchronisationPoint_VariableUsage301",
    ends={
        Property(name="SynchronisationPoint", type=pcm_pc_pc_parameter_pc_pc_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="outputParameterUsage_SynchronisationPoint", type=SynchronisationPoint, multiplicity=Multiplicity(0, 1))
    }
)
callReturnAction__VariableUsage302: BinaryAssociation = BinaryAssociation(
    name="callReturnAction__VariableUsage302",
    ends={
        Property(name="CallReturnAction", type=pcm_pc_pc_parameter_pc_pc_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="returnVariableUsage__CallReturnAction", type=CallReturnAction, multiplicity=Multiplicity(0, 1))
    }
)
setVariableAction_VariableUsage303: BinaryAssociation = BinaryAssociation(
    name="setVariableAction_VariableUsage303",
    ends={
        Property(name="SetVariableAction", type=pcm_pc_pc_parameter_pc_pc_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="localVariableUsages_SetVariableAction", type=SetVariableAction, multiplicity=Multiplicity(0, 1))
    }
)
specifiedOutputParameterAbstraction_expectedExternalOutputs_VariableUsage304: BinaryAssociation = BinaryAssociation(
    name="specifiedOutputParameterAbstraction_expectedExternalOutputs_VariableUsage304",
    ends={
        Property(name="SpecifiedOutputParameterAbstraction", type=pcm_pc_pc_parameter_pc_pc_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="expectedExternalOutputs_SpecifiedOutputParameterAbstraction", type=SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext__VariableUsage305: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__VariableUsage305",
    ends={
        Property(name="AssemblyContext306", type=pcm_pc_pc_parameter_pc_pc_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="configParameterUsages__AssemblyContext", type=composition_pc_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
entryLevelSystemCall_InputParameterUsage307: BinaryAssociation = BinaryAssociation(
    name="entryLevelSystemCall_InputParameterUsage307",
    ends={
        Property(name="EntryLevelSystemCall", type=pcm_pc_pc_parameter_pc_pc_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="inputParameterUsages_EntryLevelSystemCall", type=EntryLevelSystemCall, multiplicity=Multiplicity(0, 1))
    }
)
entryLevelSystemCall_OutputParameterUsage308: BinaryAssociation = BinaryAssociation(
    name="entryLevelSystemCall_OutputParameterUsage308",
    ends={
        Property(name="EntryLevelSystemCall309", type=pcm_pc_pc_parameter_pc_pc_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="outputParameterUsages_EntryLevelSystemCall", type=EntryLevelSystemCall, multiplicity=Multiplicity(0, 1))
    }
)
namedReference__VariableUsage310: BinaryAssociation = BinaryAssociation(
    name="namedReference__VariableUsage310",
    ends={
        Property(name="parameter_pc_pc_pcm_pc_pc_AbstractNamedReference", type=pcm_pc_pc_parameter_pc_pc_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_parameter_pc_pc_VariableUsage", type=parameter_pc_pc_pcm_pc_pc_AbstractNamedReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
specification_VariableCharacterisation311: BinaryAssociation = BinaryAssociation(
    name="specification_VariableCharacterisation311",
    ends={
        Property(name="PCMRandomVariable312", type=pcm_pc_pc_parameter_pc_pc_VariableCharacterisation, multiplicity=Multiplicity(1, 1)),
        Property(name="variableCharacterisation_Specification", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variableCharacterisation_VariableUsage296: BinaryAssociation = BinaryAssociation(
    name="variableCharacterisation_VariableUsage296",
    ends={
        Property(name="VariableCharacterisation297", type=pcm_pc_pc_parameter_pc_pc_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="variableUsage_VariableCharacterisation", type=VariableCharacterisation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variableUsage_VariableCharacterisation313: BinaryAssociation = BinaryAssociation(
    name="variableUsage_VariableCharacterisation313",
    ends={
        Property(name="VariableUsage314", type=pcm_pc_pc_parameter_pc_pc_VariableCharacterisation, multiplicity=Multiplicity(1, 1)),
        Property(name="variableCharacterisation_VariableUsage", type=VariableUsage, multiplicity=Multiplicity(0, 1))
    }
)
internalFailureOccurrenceDescriptions__SoftwareInducedFailureType316: BinaryAssociation = BinaryAssociation(
    name="internalFailureOccurrenceDescriptions__SoftwareInducedFailureType316",
    ends={
        Property(name="InternalFailureOccurrenceDescription", type=pcm_pc_pc_reliability_pc_pc_SoftwareInducedFailureType, multiplicity=Multiplicity(1, 1)),
        Property(name="softwareInducedFailureType__InternalFailureOccurrenceDescription", type=InternalFailureOccurrenceDescription, multiplicity=Multiplicity(0, 9999))
    }
)
internalAction__InternalFailureOccurrenceDescription317: BinaryAssociation = BinaryAssociation(
    name="internalAction__InternalFailureOccurrenceDescription317",
    ends={
        Property(name="InternalAction", type=pcm_pc_pc_reliability_pc_pc_InternalFailureOccurrenceDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="internalFailureOccurrenceDescriptions__InternalAction", type=InternalAction, multiplicity=Multiplicity(0, 1))
    }
)
softwareInducedFailureType__InternalFailureOccurrenceDescription318: BinaryAssociation = BinaryAssociation(
    name="softwareInducedFailureType__InternalFailureOccurrenceDescription318",
    ends={
        Property(name="SoftwareInducedFailureType", type=pcm_pc_pc_reliability_pc_pc_InternalFailureOccurrenceDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="internalFailureOccurrenceDescriptions__SoftwareInducedFailureType", type=SoftwareInducedFailureType, multiplicity=Multiplicity(0, 1))
    }
)
communicationLinkResourceType__NetworkInducedFailureType319: BinaryAssociation = BinaryAssociation(
    name="communicationLinkResourceType__NetworkInducedFailureType319",
    ends={
        Property(name="CommunicationLinkResourceType", type=pcm_pc_pc_reliability_pc_pc_NetworkInducedFailureType, multiplicity=Multiplicity(1, 1)),
        Property(name="networkInducedFailureType__CommunicationLinkResourceType", type=CommunicationLinkResourceType, multiplicity=Multiplicity(0, 1))
    }
)
processingResourceType__HardwareInducedFailureType315: BinaryAssociation = BinaryAssociation(
    name="processingResourceType__HardwareInducedFailureType315",
    ends={
        Property(name="ProcessingResourceType", type=pcm_pc_pc_reliability_pc_pc_HardwareInducedFailureType, multiplicity=Multiplicity(1, 1)),
        Property(name="hardwareInducedFailureType__ProcessingResourceType", type=ProcessingResourceType, multiplicity=Multiplicity(0, 1))
    }
)
passiveResource__ResourceTimeoutFailureType323: BinaryAssociation = BinaryAssociation(
    name="passiveResource__ResourceTimeoutFailureType323",
    ends={
        Property(name="PassiveResource324", type=pcm_pc_pc_reliability_pc_pc_ResourceTimeoutFailureType, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceTimeoutFailureType__PassiveResource", type=PassiveResource, multiplicity=Multiplicity(0, 1))
    }
)
repository__FailureType325: BinaryAssociation = BinaryAssociation(
    name="repository__FailureType325",
    ends={
        Property(name="Repository326", type=pcm_pc_pc_reliability_pc_pc_FailureType, multiplicity=Multiplicity(1, 1)),
        Property(name="failureTypes__Repository", type=Repository, multiplicity=Multiplicity(0, 1))
    }
)
resourceDemand_Action327: BinaryAssociation = BinaryAssociation(
    name="resourceDemand_Action327",
    ends={
        Property(name="ParametricResourceDemand328", type=pcm_pc_pc_seff_pc_pc_AbstractInternalControlFlowAction, multiplicity=Multiplicity(1, 1)),
        Property(name="action_ParametricResourceDemand", type=seff_performance_pc_pc_ParametricResourceDemand, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
infrastructureCall__Action329: BinaryAssociation = BinaryAssociation(
    name="infrastructureCall__Action329",
    ends={
        Property(name="InfrastructureCall330", type=pcm_pc_pc_seff_pc_pc_AbstractInternalControlFlowAction, multiplicity=Multiplicity(1, 1)),
        Property(name="action__InfrastructureCall", type=seff_performance_pc_pc_InfrastructureCall, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceCall__Action331: BinaryAssociation = BinaryAssociation(
    name="resourceCall__Action331",
    ends={
        Property(name="ResourceCall332", type=pcm_pc_pc_seff_pc_pc_AbstractInternalControlFlowAction, multiplicity=Multiplicity(1, 1)),
        Property(name="action__ResourceCall", type=seff_performance_pc_pc_ResourceCall, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specifiedReliabilityAnnotation__ExternalFailureOccurrenceDescription320: BinaryAssociation = BinaryAssociation(
    name="specifiedReliabilityAnnotation__ExternalFailureOccurrenceDescription320",
    ends={
        Property(name="SpecifiedReliabilityAnnotation", type=pcm_pc_pc_reliability_pc_pc_ExternalFailureOccurrenceDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="externalFailureOccurrenceDescriptions__SpecifiedReliabilityAnnotation", type=qos_reliability_pc_pc_SpecifiedReliabilityAnnotation, multiplicity=Multiplicity(0, 1))
    }
)
failureType__ExternalFailureOccurrenceDescription321: BinaryAssociation = BinaryAssociation(
    name="failureType__ExternalFailureOccurrenceDescription321",
    ends={
        Property(name="FailureType322", type=pcm_pc_pc_reliability_pc_pc_ExternalFailureOccurrenceDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_reliability_pc_pc_ExternalFailureOccurrenceDescription", type=FailureType, multiplicity=Multiplicity(0, 1))
    }
)
abstractLoopAction_ResourceDemandingBehaviour337: BinaryAssociation = BinaryAssociation(
    name="abstractLoopAction_ResourceDemandingBehaviour337",
    ends={
        Property(name="AbstractLoopAction", type=pcm_pc_pc_seff_pc_pc_ResourceDemandingBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="bodyBehaviour_Loop338", type=AbstractLoopAction, multiplicity=Multiplicity(0, 1))
    }
)
abstractBranchTransition_ResourceDemandingBehaviour339: BinaryAssociation = BinaryAssociation(
    name="abstractBranchTransition_ResourceDemandingBehaviour339",
    ends={
        Property(name="AbstractBranchTransition", type=pcm_pc_pc_seff_pc_pc_ResourceDemandingBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="branchBehaviour_BranchTransition", type=AbstractBranchTransition, multiplicity=Multiplicity(0, 1))
    }
)
steps_Behaviour340: BinaryAssociation = BinaryAssociation(
    name="steps_Behaviour340",
    ends={
        Property(name="AbstractAction341", type=pcm_pc_pc_seff_pc_pc_ResourceDemandingBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceDemandingBehaviour_AbstractAction", type=AbstractAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bodyBehaviour_Loop342: BinaryAssociation = BinaryAssociation(
    name="bodyBehaviour_Loop342",
    ends={
        Property(name="ResourceDemandingBehaviour343", type=pcm_pc_pc_seff_pc_pc_AbstractLoopAction, multiplicity=Multiplicity(1, 1)),
        Property(name="abstractLoopAction_ResourceDemandingBehaviour", type=ResourceDemandingBehaviour, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
branchAction_AbstractBranchTransition344: BinaryAssociation = BinaryAssociation(
    name="branchAction_AbstractBranchTransition344",
    ends={
        Property(name="BranchAction", type=pcm_pc_pc_seff_pc_pc_AbstractBranchTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="branches_Branch", type=BranchAction, multiplicity=Multiplicity(0, 1))
    }
)
predecessor_AbstractAction333: BinaryAssociation = BinaryAssociation(
    name="predecessor_AbstractAction333",
    ends={
        Property(name="AbstractAction", type=pcm_pc_pc_seff_pc_pc_AbstractAction, multiplicity=Multiplicity(1, 1)),
        Property(name="successor_AbstractAction", type=AbstractAction, multiplicity=Multiplicity(0, 1))
    }
)
successor_AbstractAction334: BinaryAssociation = BinaryAssociation(
    name="successor_AbstractAction334",
    ends={
        Property(name="AbstractAction335", type=pcm_pc_pc_seff_pc_pc_AbstractAction, multiplicity=Multiplicity(1, 1)),
        Property(name="predecessor_AbstractAction", type=AbstractAction, multiplicity=Multiplicity(0, 1))
    }
)
resourceDemandingBehaviour_AbstractAction336: BinaryAssociation = BinaryAssociation(
    name="resourceDemandingBehaviour_AbstractAction336",
    ends={
        Property(name="ResourceDemandingBehaviour", type=pcm_pc_pc_seff_pc_pc_AbstractAction, multiplicity=Multiplicity(1, 1)),
        Property(name="steps_Behaviour", type=ResourceDemandingBehaviour, multiplicity=Multiplicity(0, 1))
    }
)
branches_Branch347: BinaryAssociation = BinaryAssociation(
    name="branches_Branch347",
    ends={
        Property(name="AbstractBranchTransition348", type=pcm_pc_pc_seff_pc_pc_BranchAction, multiplicity=Multiplicity(1, 1)),
        Property(name="branchAction_AbstractBranchTransition", type=AbstractBranchTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputVariableUsages__CallAction349: BinaryAssociation = BinaryAssociation(
    name="inputVariableUsages__CallAction349",
    ends={
        Property(name="VariableUsage350", type=pcm_pc_pc_seff_pc_pc_CallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="callAction__VariableUsage", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
branchBehaviour_BranchTransition345: BinaryAssociation = BinaryAssociation(
    name="branchBehaviour_BranchTransition345",
    ends={
        Property(name="ResourceDemandingBehaviour346", type=pcm_pc_pc_seff_pc_pc_AbstractBranchTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="abstractBranchTransition_ResourceDemandingBehaviour", type=ResourceDemandingBehaviour, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resourceDemandingSEFF_ResourceDemandingInternalBehaviour355: BinaryAssociation = BinaryAssociation(
    name="resourceDemandingSEFF_ResourceDemandingInternalBehaviour355",
    ends={
        Property(name="ResourceDemandingSEFF", type=pcm_pc_pc_seff_pc_pc_ResourceDemandingInternalBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceDemandingInternalBehaviours", type=ResourceDemandingSEFF, multiplicity=Multiplicity(0, 1))
    }
)
passiveResource_ReleaseAction356: BinaryAssociation = BinaryAssociation(
    name="passiveResource_ReleaseAction356",
    ends={
        Property(name="PassiveResource357", type=pcm_pc_pc_seff_pc_pc_ReleaseAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_seff_pc_pc_ReleaseAction", type=PassiveResource, multiplicity=Multiplicity(0, 1))
    }
)
iterationCount_LoopAction358: BinaryAssociation = BinaryAssociation(
    name="iterationCount_LoopAction358",
    ends={
        Property(name="PCMRandomVariable359", type=pcm_pc_pc_seff_pc_pc_LoopAction, multiplicity=Multiplicity(1, 1)),
        Property(name="loopAction_PCMRandomVariable", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
asynchronousForkedBehaviours_ForkAction360: BinaryAssociation = BinaryAssociation(
    name="asynchronousForkedBehaviours_ForkAction360",
    ends={
        Property(name="ForkedBehaviour", type=pcm_pc_pc_seff_pc_pc_ForkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="forkAction_ForkedBehaivour", type=ForkedBehaviour, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
synchronisingBehaviours_ForkAction361: BinaryAssociation = BinaryAssociation(
    name="synchronisingBehaviours_ForkAction361",
    ends={
        Property(name="SynchronisationPoint362", type=pcm_pc_pc_seff_pc_pc_ForkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="forkAction_SynchronisationPoint", type=SynchronisationPoint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
synchronisationPoint_ForkedBehaviour363: BinaryAssociation = BinaryAssociation(
    name="synchronisationPoint_ForkedBehaviour363",
    ends={
        Property(name="SynchronisationPoint364", type=pcm_pc_pc_seff_pc_pc_ForkedBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="synchronousForkedBehaviours_SynchronisationPoint", type=SynchronisationPoint, multiplicity=Multiplicity(0, 1))
    }
)
forkAction_ForkedBehaivour365: BinaryAssociation = BinaryAssociation(
    name="forkAction_ForkedBehaivour365",
    ends={
        Property(name="ForkAction", type=pcm_pc_pc_seff_pc_pc_ForkedBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="asynchronousForkedBehaviours_ForkAction", type=ForkAction, multiplicity=Multiplicity(0, 1))
    }
)
outputParameterUsage_SynchronisationPoint366: BinaryAssociation = BinaryAssociation(
    name="outputParameterUsage_SynchronisationPoint366",
    ends={
        Property(name="VariableUsage367", type=pcm_pc_pc_seff_pc_pc_SynchronisationPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="synchronisationPoint_VariableUsage", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
describedService__SEFF351: BinaryAssociation = BinaryAssociation(
    name="describedService__SEFF351",
    ends={
        Property(name="Signature", type=pcm_pc_pc_seff_pc_pc_ServiceEffectSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_seff_pc_pc_ServiceEffectSpecification", type=Signature, multiplicity=Multiplicity(0, 1))
    }
)
basicComponent_ServiceEffectSpecification352: BinaryAssociation = BinaryAssociation(
    name="basicComponent_ServiceEffectSpecification352",
    ends={
        Property(name="BasicComponent353", type=pcm_pc_pc_seff_pc_pc_ServiceEffectSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="serviceEffectSpecifications__BasicComponent", type=BasicComponent, multiplicity=Multiplicity(0, 1))
    }
)
resourceDemandingInternalBehaviours354: BinaryAssociation = BinaryAssociation(
    name="resourceDemandingInternalBehaviours354",
    ends={
        Property(name="ResourceDemandingInternalBehaviour", type=pcm_pc_pc_seff_pc_pc_ResourceDemandingSEFF, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceDemandingSEFF_ResourceDemandingInternalBehaviour", type=ResourceDemandingInternalBehaviour, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
calledService_ExternalService372: BinaryAssociation = BinaryAssociation(
    name="calledService_ExternalService372",
    ends={
        Property(name="OperationSignature373", type=pcm_pc_pc_seff_pc_pc_ExternalCallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_seff_pc_pc_ExternalCallAction", type=OperationSignature, multiplicity=Multiplicity(0, 1))
    }
)
role_ExternalService374: BinaryAssociation = BinaryAssociation(
    name="role_ExternalService374",
    ends={
        Property(name="OperationRequiredRole376", type=pcm_pc_pc_seff_pc_pc_ExternalCallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_seff_pc_pc_ExternalCallAction375", type=OperationRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
returnVariableUsage__CallReturnAction377: BinaryAssociation = BinaryAssociation(
    name="returnVariableUsage__CallReturnAction377",
    ends={
        Property(name="VariableUsage378", type=pcm_pc_pc_seff_pc_pc_CallReturnAction, multiplicity=Multiplicity(1, 1)),
        Property(name="callReturnAction__VariableUsage", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
forkAction_SynchronisationPoint368: BinaryAssociation = BinaryAssociation(
    name="forkAction_SynchronisationPoint368",
    ends={
        Property(name="ForkAction369", type=pcm_pc_pc_seff_pc_pc_SynchronisationPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="synchronisingBehaviours_ForkAction", type=ForkAction, multiplicity=Multiplicity(0, 1))
    }
)
synchronousForkedBehaviours_SynchronisationPoint370: BinaryAssociation = BinaryAssociation(
    name="synchronousForkedBehaviours_SynchronisationPoint370",
    ends={
        Property(name="ForkedBehaviour371", type=pcm_pc_pc_seff_pc_pc_SynchronisationPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="synchronisationPoint_ForkedBehaviour", type=ForkedBehaviour, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
passiveresource_AcquireAction379: BinaryAssociation = BinaryAssociation(
    name="passiveresource_AcquireAction379",
    ends={
        Property(name="PassiveResource380", type=pcm_pc_pc_seff_pc_pc_AcquireAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_seff_pc_pc_AcquireAction", type=PassiveResource, multiplicity=Multiplicity(0, 1))
    }
)
parameter_CollectionIteratorAction381: BinaryAssociation = BinaryAssociation(
    name="parameter_CollectionIteratorAction381",
    ends={
        Property(name="Parameter382", type=pcm_pc_pc_seff_pc_pc_CollectionIteratorAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_seff_pc_pc_CollectionIteratorAction", type=Parameter_, multiplicity=Multiplicity(0, 1))
    }
)
branchCondition_GuardedBranchTransition383: BinaryAssociation = BinaryAssociation(
    name="branchCondition_GuardedBranchTransition383",
    ends={
        Property(name="PCMRandomVariable384", type=pcm_pc_pc_seff_pc_pc_GuardedBranchTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="guardedBranchTransition_PCMRandomVariable", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
localVariableUsages_SetVariableAction385: BinaryAssociation = BinaryAssociation(
    name="localVariableUsages_SetVariableAction385",
    ends={
        Property(name="VariableUsage386", type=pcm_pc_pc_seff_pc_pc_SetVariableAction, multiplicity=Multiplicity(1, 1)),
        Property(name="setVariableAction_VariableUsage", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
calledResourceDemandingInternalBehaviour387: BinaryAssociation = BinaryAssociation(
    name="calledResourceDemandingInternalBehaviour387",
    ends={
        Property(name="ResourceDemandingInternalBehaviour388", type=pcm_pc_pc_seff_pc_pc_InternalCallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_seff_pc_pc_InternalCallAction", type=ResourceDemandingInternalBehaviour, multiplicity=Multiplicity(0, 1))
    }
)
eventType__EmitEventAction389: BinaryAssociation = BinaryAssociation(
    name="eventType__EmitEventAction389",
    ends={
        Property(name="EventType390", type=pcm_pc_pc_seff_pc_pc_EmitEventAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_seff_pc_pc_EmitEventAction", type=EventType, multiplicity=Multiplicity(0, 1))
    }
)
sourceRole__EmitEventAction391: BinaryAssociation = BinaryAssociation(
    name="sourceRole__EmitEventAction391",
    ends={
        Property(name="SourceRole393", type=pcm_pc_pc_seff_pc_pc_EmitEventAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_seff_pc_pc_EmitEventAction392", type=SourceRole, multiplicity=Multiplicity(0, 1))
    }
)
internalFailureOccurrenceDescriptions__InternalAction394: BinaryAssociation = BinaryAssociation(
    name="internalFailureOccurrenceDescriptions__InternalAction394",
    ends={
        Property(name="InternalFailureOccurrenceDescription395", type=pcm_pc_pc_seff_pc_pc_InternalAction, multiplicity=Multiplicity(1, 1)),
        Property(name="internalAction__InternalFailureOccurrenceDescription", type=InternalFailureOccurrenceDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
signature__InfrastructureCall396: BinaryAssociation = BinaryAssociation(
    name="signature__InfrastructureCall396",
    ends={
        Property(name="InfrastructureSignature397", type=pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall", type=InfrastructureSignature, multiplicity=Multiplicity(0, 1))
    }
)
numberOfCalls__InfrastructureCall398: BinaryAssociation = BinaryAssociation(
    name="numberOfCalls__InfrastructureCall398",
    ends={
        Property(name="PCMRandomVariable399", type=pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="infrastructureCall__PCMRandomVariable", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
action__InfrastructureCall400: BinaryAssociation = BinaryAssociation(
    name="action__InfrastructureCall400",
    ends={
        Property(name="AbstractInternalControlFlowAction", type=pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="infrastructureCall__Action", type=AbstractInternalControlFlowAction, multiplicity=Multiplicity(0, 1))
    }
)
action__ResourceCall404: BinaryAssociation = BinaryAssociation(
    name="action__ResourceCall404",
    ends={
        Property(name="AbstractInternalControlFlowAction405", type=pcm_pc_pc_seff_performance_pc_pc_ResourceCall, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceCall__Action", type=AbstractInternalControlFlowAction, multiplicity=Multiplicity(0, 1))
    }
)
resourceRequiredRole__ResourceCall406: BinaryAssociation = BinaryAssociation(
    name="resourceRequiredRole__ResourceCall406",
    ends={
        Property(name="entity_pc_pc_ResourceRequiredRole407", type=pcm_pc_pc_seff_performance_pc_pc_ResourceCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_seff_performance_pc_pc_ResourceCall", type=entity_pc_pc_ResourceRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
signature__ResourceCall408: BinaryAssociation = BinaryAssociation(
    name="signature__ResourceCall408",
    ends={
        Property(name="ResourceSignature410", type=pcm_pc_pc_seff_performance_pc_pc_ResourceCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_seff_performance_pc_pc_ResourceCall409", type=ResourceSignature, multiplicity=Multiplicity(0, 1))
    }
)
numberOfCalls__ResourceCall411: BinaryAssociation = BinaryAssociation(
    name="numberOfCalls__ResourceCall411",
    ends={
        Property(name="PCMRandomVariable412", type=pcm_pc_pc_seff_performance_pc_pc_ResourceCall, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceCall__PCMRandomVariable", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
specification_ParametericResourceDemand413: BinaryAssociation = BinaryAssociation(
    name="specification_ParametericResourceDemand413",
    ends={
        Property(name="PCMRandomVariable414", type=pcm_pc_pc_seff_performance_pc_pc_ParametricResourceDemand, multiplicity=Multiplicity(1, 1)),
        Property(name="parametricResourceDemand_PCMRandomVariable", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
requiredResource_ParametricResourceDemand415: BinaryAssociation = BinaryAssociation(
    name="requiredResource_ParametricResourceDemand415",
    ends={
        Property(name="ProcessingResourceType416", type=pcm_pc_pc_seff_performance_pc_pc_ParametricResourceDemand, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_seff_performance_pc_pc_ParametricResourceDemand", type=ProcessingResourceType, multiplicity=Multiplicity(0, 1))
    }
)
action_ParametricResourceDemand417: BinaryAssociation = BinaryAssociation(
    name="action_ParametricResourceDemand417",
    ends={
        Property(name="AbstractInternalControlFlowAction418", type=pcm_pc_pc_seff_performance_pc_pc_ParametricResourceDemand, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceDemand_Action", type=AbstractInternalControlFlowAction, multiplicity=Multiplicity(0, 1))
    }
)
requiredRole__InfrastructureCall401: BinaryAssociation = BinaryAssociation(
    name="requiredRole__InfrastructureCall401",
    ends={
        Property(name="InfrastructureRequiredRole403", type=pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall402", type=InfrastructureRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
failureHandlingAlternatives__RecoveryActionBehaviour419: BinaryAssociation = BinaryAssociation(
    name="failureHandlingAlternatives__RecoveryActionBehaviour419",
    ends={
        Property(name="seff_reliability_pc_pc_RecoveryActionBehaviour", type=pcm_pc_pc_seff_reliability_pc_pc_RecoveryActionBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_seff_reliability_pc_pc_RecoveryActionBehaviour", type=seff_reliability_pc_pc_RecoveryActionBehaviour, multiplicity=Multiplicity(0, 9999))
    }
)
recoveryAction__RecoveryActionBehaviour420: BinaryAssociation = BinaryAssociation(
    name="recoveryAction__RecoveryActionBehaviour420",
    ends={
        Property(name="RecoveryAction", type=pcm_pc_pc_seff_reliability_pc_pc_RecoveryActionBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="recoveryActionBehaviours__RecoveryAction", type=seff_reliability_pc_pc_RecoveryAction, multiplicity=Multiplicity(0, 1))
    }
)
primaryBehaviour__RecoveryAction421: BinaryAssociation = BinaryAssociation(
    name="primaryBehaviour__RecoveryAction421",
    ends={
        Property(name="seff_reliability_pc_pc_RecoveryActionBehaviour422", type=pcm_pc_pc_seff_reliability_pc_pc_RecoveryAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_seff_reliability_pc_pc_RecoveryAction", type=seff_reliability_pc_pc_RecoveryActionBehaviour, multiplicity=Multiplicity(0, 1))
    }
)
recoveryActionBehaviours__RecoveryAction423: BinaryAssociation = BinaryAssociation(
    name="recoveryActionBehaviours__RecoveryAction423",
    ends={
        Property(name="RecoveryActionBehaviour", type=pcm_pc_pc_seff_reliability_pc_pc_RecoveryAction, multiplicity=Multiplicity(1, 1)),
        Property(name="recoveryAction__RecoveryActionBehaviour", type=seff_reliability_pc_pc_RecoveryActionBehaviour, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
failureTypes_FailureHandlingEntity424: BinaryAssociation = BinaryAssociation(
    name="failureTypes_FailureHandlingEntity424",
    ends={
        Property(name="FailureType425", type=pcm_pc_pc_seff_reliability_pc_pc_FailureHandlingEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_seff_reliability_pc_pc_FailureHandlingEntity", type=FailureType, multiplicity=Multiplicity(0, 9999))
    }
)
specifiedOutputParameterAbstractions_QoSAnnotations431: BinaryAssociation = BinaryAssociation(
    name="specifiedOutputParameterAbstractions_QoSAnnotations431",
    ends={
        Property(name="SpecifiedOutputParameterAbstraction432", type=pcm_pc_pc_qosannotations_pc_pc_QoSAnnotations, multiplicity=Multiplicity(1, 1)),
        Property(name="qosAnnotations_SpecifiedOutputParameterAbstraction", type=SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
system_QoSAnnotations433: BinaryAssociation = BinaryAssociation(
    name="system_QoSAnnotations433",
    ends={
        Property(name="System", type=pcm_pc_pc_qosannotations_pc_pc_QoSAnnotations, multiplicity=Multiplicity(1, 1)),
        Property(name="qosAnnotations_System", type=System, multiplicity=Multiplicity(0, 1))
    }
)
specifiedQoSAnnotations_QoSAnnotations434: BinaryAssociation = BinaryAssociation(
    name="specifiedQoSAnnotations_QoSAnnotations434",
    ends={
        Property(name="SpecifiedQoSAnnotation", type=pcm_pc_pc_qosannotations_pc_pc_QoSAnnotations, multiplicity=Multiplicity(1, 1)),
        Property(name="qosAnnotations_SpecifiedQoSAnnotation", type=SpecifiedQoSAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
signature_SpecifiedOutputParameterAbstraction435: BinaryAssociation = BinaryAssociation(
    name="signature_SpecifiedOutputParameterAbstraction435",
    ends={
        Property(name="Signature436", type=pcm_pc_pc_qosannotations_pc_pc_SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_qosannotations_pc_pc_SpecifiedOutputParameterAbstraction", type=Signature, multiplicity=Multiplicity(0, 1))
    }
)
role_SpecifiedOutputParameterAbstraction437: BinaryAssociation = BinaryAssociation(
    name="role_SpecifiedOutputParameterAbstraction437",
    ends={
        Property(name="Role439", type=pcm_pc_pc_qosannotations_pc_pc_SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_qosannotations_pc_pc_SpecifiedOutputParameterAbstraction438", type=Role, multiplicity=Multiplicity(0, 1))
    }
)
expectedExternalOutputs_SpecifiedOutputParameterAbstraction440: BinaryAssociation = BinaryAssociation(
    name="expectedExternalOutputs_SpecifiedOutputParameterAbstraction440",
    ends={
        Property(name="VariableUsage441", type=pcm_pc_pc_qosannotations_pc_pc_SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(1, 1)),
        Property(name="specifiedOutputParameterAbstraction_expectedExternalOutputs_VariableUsage", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
qosAnnotations_SpecifiedOutputParameterAbstraction442: BinaryAssociation = BinaryAssociation(
    name="qosAnnotations_SpecifiedOutputParameterAbstraction442",
    ends={
        Property(name="QoSAnnotations443", type=pcm_pc_pc_qosannotations_pc_pc_SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(1, 1)),
        Property(name="specifiedOutputParameterAbstractions_QoSAnnotations", type=QoSAnnotations, multiplicity=Multiplicity(0, 1))
    }
)
signature_SpecifiedQoSAnnation426: BinaryAssociation = BinaryAssociation(
    name="signature_SpecifiedQoSAnnation426",
    ends={
        Property(name="Signature427", type=pcm_pc_pc_qosannotations_pc_pc_SpecifiedQoSAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_qosannotations_pc_pc_SpecifiedQoSAnnotation", type=Signature, multiplicity=Multiplicity(0, 1))
    }
)
role_SpecifiedQoSAnnotation428: BinaryAssociation = BinaryAssociation(
    name="role_SpecifiedQoSAnnotation428",
    ends={
        Property(name="Role", type=pcm_pc_pc_qosannotations_pc_pc_SpecifiedQoSAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_qosannotations_pc_pc_SpecifiedQoSAnnotation429", type=Role, multiplicity=Multiplicity(0, 1))
    }
)
qosAnnotations_SpecifiedQoSAnnotation430: BinaryAssociation = BinaryAssociation(
    name="qosAnnotations_SpecifiedQoSAnnotation430",
    ends={
        Property(name="QoSAnnotations", type=pcm_pc_pc_qosannotations_pc_pc_SpecifiedQoSAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="specifiedQoSAnnotations_QoSAnnotations", type=QoSAnnotations, multiplicity=Multiplicity(0, 1))
    }
)
externalFailureOccurrenceDescriptions__SpecifiedReliabilityAnnotation448: BinaryAssociation = BinaryAssociation(
    name="externalFailureOccurrenceDescriptions__SpecifiedReliabilityAnnotation448",
    ends={
        Property(name="ExternalFailureOccurrenceDescription", type=pcm_pc_pc_qos_reliability_pc_pc_SpecifiedReliabilityAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="specifiedReliabilityAnnotation__ExternalFailureOccurrenceDescription", type=ExternalFailureOccurrenceDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
qosAnnotations_System449: BinaryAssociation = BinaryAssociation(
    name="qosAnnotations_System449",
    ends={
        Property(name="QoSAnnotations450", type=pcm_pc_pc_system_pc_pc_System, multiplicity=Multiplicity(1, 1)),
        Property(name="system_QoSAnnotations", type=QoSAnnotations, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specification_SpecifiedExecutionTime444: BinaryAssociation = BinaryAssociation(
    name="specification_SpecifiedExecutionTime444",
    ends={
        Property(name="PCMRandomVariable445", type=pcm_pc_pc_qos_performance_pc_pc_SpecifiedExecutionTime, multiplicity=Multiplicity(1, 1)),
        Property(name="specifiedExecutionTime_PCMRandomVariable", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assemblyContext_ComponentSpecifiedExecutionTime446: BinaryAssociation = BinaryAssociation(
    name="assemblyContext_ComponentSpecifiedExecutionTime446",
    ends={
        Property(name="composition_pc_pc_AssemblyContext447", type=pcm_pc_pc_qos_performance_pc_pc_ComponentSpecifiedExecutionTime, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_qos_performance_pc_pc_ComponentSpecifiedExecutionTime", type=composition_pc_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
communicationLinkResourceSpecifications_LinkingResource455: BinaryAssociation = BinaryAssociation(
    name="communicationLinkResourceSpecifications_LinkingResource455",
    ends={
        Property(name="CommunicationLinkResourceSpecification456", type=pcm_pc_pc_resourceenvironment_pc_pc_LinkingResource, multiplicity=Multiplicity(1, 1)),
        Property(name="linkingResource_CommunicationLinkResourceSpecification", type=CommunicationLinkResourceSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resourceEnvironment_LinkingResource457: BinaryAssociation = BinaryAssociation(
    name="resourceEnvironment_LinkingResource457",
    ends={
        Property(name="ResourceEnvironment", type=pcm_pc_pc_resourceenvironment_pc_pc_LinkingResource, multiplicity=Multiplicity(1, 1)),
        Property(name="linkingResources__ResourceEnvironment", type=ResourceEnvironment, multiplicity=Multiplicity(0, 1))
    }
)
activeResourceSpecifications_ResourceContainer458: BinaryAssociation = BinaryAssociation(
    name="activeResourceSpecifications_ResourceContainer458",
    ends={
        Property(name="ProcessingResourceSpecification459", type=pcm_pc_pc_resourceenvironment_pc_pc_ResourceContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceContainer_ProcessingResourceSpecification", type=ProcessingResourceSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceEnvironment_ResourceContainer460: BinaryAssociation = BinaryAssociation(
    name="resourceEnvironment_ResourceContainer460",
    ends={
        Property(name="ResourceEnvironment461", type=pcm_pc_pc_resourceenvironment_pc_pc_ResourceContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceContainer_ResourceEnvironment", type=ResourceEnvironment, multiplicity=Multiplicity(0, 1))
    }
)
nestedResourceContainers__ResourceContainer462: BinaryAssociation = BinaryAssociation(
    name="nestedResourceContainers__ResourceContainer462",
    ends={
        Property(name="ResourceContainer463", type=pcm_pc_pc_resourceenvironment_pc_pc_ResourceContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="parentResourceContainer__ResourceContainer", type=ResourceContainer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentResourceContainer__ResourceContainer464: BinaryAssociation = BinaryAssociation(
    name="parentResourceContainer__ResourceContainer464",
    ends={
        Property(name="ResourceContainer465", type=pcm_pc_pc_resourceenvironment_pc_pc_ResourceContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="nestedResourceContainers__ResourceContainer", type=ResourceContainer, multiplicity=Multiplicity(0, 1))
    }
)
schedulingPolicy466: BinaryAssociation = BinaryAssociation(
    name="schedulingPolicy466",
    ends={
        Property(name="SchedulingPolicy467", type=pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification", type=SchedulingPolicy, multiplicity=Multiplicity(0, 1))
    }
)
activeResourceType_ActiveResourceSpecification468: BinaryAssociation = BinaryAssociation(
    name="activeResourceType_ActiveResourceSpecification468",
    ends={
        Property(name="ProcessingResourceType470", type=pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification469", type=ProcessingResourceType, multiplicity=Multiplicity(0, 1))
    }
)
processingRate_ProcessingResourceSpecification471: BinaryAssociation = BinaryAssociation(
    name="processingRate_ProcessingResourceSpecification471",
    ends={
        Property(name="PCMRandomVariable472", type=pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="processingResourceSpecification_processingRate_PCMRandomVariable", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resourceContainer_ProcessingResourceSpecification473: BinaryAssociation = BinaryAssociation(
    name="resourceContainer_ProcessingResourceSpecification473",
    ends={
        Property(name="ResourceContainer474", type=pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="activeResourceSpecifications_ResourceContainer", type=ResourceContainer, multiplicity=Multiplicity(0, 1))
    }
)
linkingResources__ResourceEnvironment451: BinaryAssociation = BinaryAssociation(
    name="linkingResources__ResourceEnvironment451",
    ends={
        Property(name="LinkingResource", type=pcm_pc_pc_resourceenvironment_pc_pc_ResourceEnvironment, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceEnvironment_LinkingResource", type=LinkingResource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceContainer_ResourceEnvironment452: BinaryAssociation = BinaryAssociation(
    name="resourceContainer_ResourceEnvironment452",
    ends={
        Property(name="ResourceContainer", type=pcm_pc_pc_resourceenvironment_pc_pc_ResourceEnvironment, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceEnvironment_ResourceContainer", type=ResourceContainer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connectedResourceContainers_LinkingResource453: BinaryAssociation = BinaryAssociation(
    name="connectedResourceContainers_LinkingResource453",
    ends={
        Property(name="ResourceContainer454", type=pcm_pc_pc_resourceenvironment_pc_pc_LinkingResource, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_resourceenvironment_pc_pc_LinkingResource", type=ResourceContainer, multiplicity=Multiplicity(0, 9999))
    }
)
linkingResource_CommunicationLinkResourceSpecification475: BinaryAssociation = BinaryAssociation(
    name="linkingResource_CommunicationLinkResourceSpecification475",
    ends={
        Property(name="LinkingResource476", type=pcm_pc_pc_resourceenvironment_pc_pc_CommunicationLinkResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="communicationLinkResourceSpecifications_LinkingResource", type=LinkingResource, multiplicity=Multiplicity(0, 1))
    }
)
communicationLinkResourceType_CommunicationLinkResourceSpecification477: BinaryAssociation = BinaryAssociation(
    name="communicationLinkResourceType_CommunicationLinkResourceSpecification477",
    ends={
        Property(name="CommunicationLinkResourceType478", type=pcm_pc_pc_resourceenvironment_pc_pc_CommunicationLinkResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_resourceenvironment_pc_pc_CommunicationLinkResourceSpecification", type=CommunicationLinkResourceType, multiplicity=Multiplicity(0, 1))
    }
)
latency_CommunicationLinkResourceSpecification479: BinaryAssociation = BinaryAssociation(
    name="latency_CommunicationLinkResourceSpecification479",
    ends={
        Property(name="PCMRandomVariable480", type=pcm_pc_pc_resourceenvironment_pc_pc_CommunicationLinkResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="communicationLinkResourceSpecification_latency_PCMRandomVariable", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
throughput_CommunicationLinkResourceSpecification481: BinaryAssociation = BinaryAssociation(
    name="throughput_CommunicationLinkResourceSpecification481",
    ends={
        Property(name="PCMRandomVariable482", type=pcm_pc_pc_resourceenvironment_pc_pc_CommunicationLinkResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="communicationLinkResourceSpecifcation_throughput_PCMRandomVariable", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resourceContainer_AllocationContext483: BinaryAssociation = BinaryAssociation(
    name="resourceContainer_AllocationContext483",
    ends={
        Property(name="ResourceContainer484", type=pcm_pc_pc_allocation_pc_pc_AllocationContext, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_allocation_pc_pc_AllocationContext", type=ResourceContainer, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext_AllocationContext485: BinaryAssociation = BinaryAssociation(
    name="assemblyContext_AllocationContext485",
    ends={
        Property(name="composition_pc_pc_AssemblyContext487", type=pcm_pc_pc_allocation_pc_pc_AllocationContext, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_allocation_pc_pc_AllocationContext486", type=composition_pc_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
eventChannel__AllocationContext489: BinaryAssociation = BinaryAssociation(
    name="eventChannel__AllocationContext489",
    ends={
        Property(name="composition_pc_pc_EventChannel", type=pcm_pc_pc_allocation_pc_pc_AllocationContext, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_allocation_pc_pc_AllocationContext490", type=composition_pc_pc_EventChannel, multiplicity=Multiplicity(0, 1))
    }
)
targetResourceEnvironment_Allocation491: BinaryAssociation = BinaryAssociation(
    name="targetResourceEnvironment_Allocation491",
    ends={
        Property(name="ResourceEnvironment492", type=pcm_pc_pc_allocation_pc_pc_Allocation, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_allocation_pc_pc_Allocation", type=ResourceEnvironment, multiplicity=Multiplicity(0, 1))
    }
)
system_Allocation493: BinaryAssociation = BinaryAssociation(
    name="system_Allocation493",
    ends={
        Property(name="System495", type=pcm_pc_pc_allocation_pc_pc_Allocation, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_allocation_pc_pc_Allocation494", type=System, multiplicity=Multiplicity(0, 1))
    }
)
allocationContexts_Allocation496: BinaryAssociation = BinaryAssociation(
    name="allocationContexts_Allocation496",
    ends={
        Property(name="AllocationContext", type=pcm_pc_pc_allocation_pc_pc_Allocation, multiplicity=Multiplicity(1, 1)),
        Property(name="allocation_AllocationContext", type=AllocationContext, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
completions_CompletionRepository497: BinaryAssociation = BinaryAssociation(
    name="completions_CompletionRepository497",
    ends={
        Property(name="Completion", type=pcm_pc_pc_completions_pc_pc_CompletionRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_completions_pc_pc_CompletionRepository", type=Completion, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
allocation_AllocationContext488: BinaryAssociation = BinaryAssociation(
    name="allocation_AllocationContext488",
    ends={
        Property(name="Allocation", type=pcm_pc_pc_allocation_pc_pc_AllocationContext, multiplicity=Multiplicity(1, 1)),
        Property(name="allocationContexts_Allocation", type=Allocation, multiplicity=Multiplicity(0, 1))
    }
)
requiredCommunicationLinkResource_ParametricResourceDemand498: BinaryAssociation = BinaryAssociation(
    name="requiredCommunicationLinkResource_ParametricResourceDemand498",
    ends={
        Property(name="CommunicationLinkResourceType499", type=pcm_pc_pc_completions_pc_pc_NetworkDemandParametricResourceDemand, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_pc_completions_pc_pc_NetworkDemandParametricResourceDemand", type=CommunicationLinkResourceType, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_pcm_pc_pc_core_pc_pc_PCMRandomVariable_RandomVariable = Generalization(general=RandomVariable, specific=pcm_pc_pc_core_pc_pc_PCMRandomVariable)
gen_pcm_pc_pc_entity_pc_pc_InterfaceProvidingRequiringEntity_entity_pc_pc_InterfaceProvidingEntity = Generalization(general=entity_pc_pc_InterfaceProvidingEntity, specific=pcm_pc_pc_entity_pc_pc_InterfaceProvidingRequiringEntity)
gen_pcm_pc_pc_entity_pc_pc_InterfaceProvidingRequiringEntity_entity_pc_pc_InterfaceRequiringEntity = Generalization(general=entity_pc_pc_InterfaceRequiringEntity, specific=pcm_pc_pc_entity_pc_pc_InterfaceProvidingRequiringEntity)
gen_pcm_pc_pc_entity_pc_pc_InterfaceProvidingEntity_Entity = Generalization(general=Entity, specific=pcm_pc_pc_entity_pc_pc_InterfaceProvidingEntity)
gen_pcm_pc_pc_entity_pc_pc_ResourceProvidedRole_Role = Generalization(general=Role, specific=pcm_pc_pc_entity_pc_pc_ResourceProvidedRole)
gen_pcm_pc_pc_entity_pc_pc_ResourceInterfaceProvidingRequiringEntity_entity_pc_pc_ResourceInterfaceRequiringEntity = Generalization(general=entity_pc_pc_ResourceInterfaceRequiringEntity, specific=pcm_pc_pc_entity_pc_pc_ResourceInterfaceProvidingRequiringEntity)
gen_pcm_pc_pc_entity_pc_pc_ResourceInterfaceProvidingRequiringEntity_entity_pc_pc_ResourceInterfaceProvidingEntity = Generalization(general=entity_pc_pc_ResourceInterfaceProvidingEntity, specific=pcm_pc_pc_entity_pc_pc_ResourceInterfaceProvidingRequiringEntity)
gen_pcm_pc_pc_entity_pc_pc_Entity_Identifier = Generalization(general=Identifier, specific=pcm_pc_pc_entity_pc_pc_Entity)
gen_pcm_pc_pc_entity_pc_pc_Entity_entity_pc_pc_NamedElement = Generalization(general=entity_pc_pc_NamedElement, specific=pcm_pc_pc_entity_pc_pc_Entity)
gen_pcm_pc_pc_composition_pc_pc_DelegationConnector_Connector = Generalization(general=Connector, specific=pcm_pc_pc_composition_pc_pc_DelegationConnector)
gen_pcm_pc_pc_composition_pc_pc_Connector_Entity = Generalization(general=Entity, specific=pcm_pc_pc_composition_pc_pc_Connector)
gen_pcm_pc_pc_entity_pc_pc_InterfaceRequiringEntity_entity_pc_pc_Entity = Generalization(general=entity_pc_pc_Entity, specific=pcm_pc_pc_entity_pc_pc_InterfaceRequiringEntity)
gen_pcm_pc_pc_entity_pc_pc_InterfaceRequiringEntity_entity_pc_pc_ResourceInterfaceRequiringEntity = Generalization(general=entity_pc_pc_ResourceInterfaceRequiringEntity, specific=pcm_pc_pc_entity_pc_pc_InterfaceRequiringEntity)
gen_pcm_pc_pc_entity_pc_pc_ResourceInterfaceRequiringEntity_Entity = Generalization(general=Entity, specific=pcm_pc_pc_entity_pc_pc_ResourceInterfaceRequiringEntity)
gen_pcm_pc_pc_entity_pc_pc_ResourceRequiredRole_Role = Generalization(general=Role, specific=pcm_pc_pc_entity_pc_pc_ResourceRequiredRole)
gen_pcm_pc_pc_entity_pc_pc_ResourceInterfaceProvidingEntity_Entity = Generalization(general=Entity, specific=pcm_pc_pc_entity_pc_pc_ResourceInterfaceProvidingEntity)
gen_pcm_pc_pc_entity_pc_pc_ComposedProvidingRequiringEntity_composition_pc_pc_ComposedStructure = Generalization(general=composition_pc_pc_ComposedStructure, specific=pcm_pc_pc_entity_pc_pc_ComposedProvidingRequiringEntity)
gen_pcm_pc_pc_entity_pc_pc_ComposedProvidingRequiringEntity_entity_pc_pc_InterfaceProvidingRequiringEntity = Generalization(general=entity_pc_pc_InterfaceProvidingRequiringEntity, specific=pcm_pc_pc_entity_pc_pc_ComposedProvidingRequiringEntity)
gen_pcm_pc_pc_composition_pc_pc_ComposedStructure_Entity = Generalization(general=Entity, specific=pcm_pc_pc_composition_pc_pc_ComposedStructure)
gen_pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector)
gen_pcm_pc_pc_composition_pc_pc_EventChannel_Entity = Generalization(general=Entity, specific=pcm_pc_pc_composition_pc_pc_EventChannel)
gen_pcm_pc_pc_composition_pc_pc_EventChannelSourceConnector_Connector = Generalization(general=Connector, specific=pcm_pc_pc_composition_pc_pc_EventChannelSourceConnector)
gen_pcm_pc_pc_composition_pc_pc_EventChannelSinkConnector_Connector = Generalization(general=Connector, specific=pcm_pc_pc_composition_pc_pc_EventChannelSinkConnector)
gen_pcm_pc_pc_composition_pc_pc_AssemblyConnector_Connector = Generalization(general=Connector, specific=pcm_pc_pc_composition_pc_pc_AssemblyConnector)
gen_pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector)
gen_pcm_pc_pc_composition_pc_pc_SourceDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_pc_pc_composition_pc_pc_SourceDelegationConnector)
gen_pcm_pc_pc_composition_pc_pc_SinkDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_pc_pc_composition_pc_pc_SinkDelegationConnector)
gen_pcm_pc_pc_composition_pc_pc_AssemblyInfrastructureConnector_Connector = Generalization(general=Connector, specific=pcm_pc_pc_composition_pc_pc_AssemblyInfrastructureConnector)
gen_pcm_pc_pc_composition_pc_pc_AssemblyEventConnector_Connector = Generalization(general=Connector, specific=pcm_pc_pc_composition_pc_pc_AssemblyEventConnector)
gen_pcm_pc_pc_composition_pc_pc_RequiredResourceDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_pc_pc_composition_pc_pc_RequiredResourceDelegationConnector)
gen_pcm_pc_pc_composition_pc_pc_AssemblyContext_Entity = Generalization(general=Entity, specific=pcm_pc_pc_composition_pc_pc_AssemblyContext)
gen_pcm_pc_pc_usagemodel_pc_pc_UsageScenario_Entity = Generalization(general=Entity, specific=pcm_pc_pc_usagemodel_pc_pc_UsageScenario)
gen_pcm_pc_pc_composition_pc_pc_ProvidedInfrastructureDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_pc_pc_composition_pc_pc_ProvidedInfrastructureDelegationConnector)
gen_pcm_pc_pc_composition_pc_pc_RequiredInfrastructureDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_pc_pc_composition_pc_pc_RequiredInfrastructureDelegationConnector)
gen_pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall)
gen_pcm_pc_pc_usagemodel_pc_pc_AbstractUserAction_Entity = Generalization(general=Entity, specific=pcm_pc_pc_usagemodel_pc_pc_AbstractUserAction)
gen_pcm_pc_pc_usagemodel_pc_pc_ScenarioBehaviour_Entity = Generalization(general=Entity, specific=pcm_pc_pc_usagemodel_pc_pc_ScenarioBehaviour)
gen_pcm_pc_pc_usagemodel_pc_pc_Loop_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_pc_pc_usagemodel_pc_pc_Loop)
gen_pcm_pc_pc_usagemodel_pc_pc_Stop_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_pc_pc_usagemodel_pc_pc_Stop)
gen_pcm_pc_pc_usagemodel_pc_pc_Start_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_pc_pc_usagemodel_pc_pc_Start)
gen_pcm_pc_pc_usagemodel_pc_pc_OpenWorkload_Workload = Generalization(general=Workload, specific=pcm_pc_pc_usagemodel_pc_pc_OpenWorkload)
gen_pcm_pc_pc_usagemodel_pc_pc_Branch_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_pc_pc_usagemodel_pc_pc_Branch)
gen_pcm_pc_pc_usagemodel_pc_pc_ClosedWorkload_Workload = Generalization(general=Workload, specific=pcm_pc_pc_usagemodel_pc_pc_ClosedWorkload)
gen_pcm_pc_pc_repository_pc_pc_PassiveResource_Entity = Generalization(general=Entity, specific=pcm_pc_pc_repository_pc_pc_PassiveResource)
gen_pcm_pc_pc_usagemodel_pc_pc_Delay_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_pc_pc_usagemodel_pc_pc_Delay)
gen_pcm_pc_pc_repository_pc_pc_ImplementationComponentType_RepositoryComponent = Generalization(general=RepositoryComponent, specific=pcm_pc_pc_repository_pc_pc_ImplementationComponentType)
gen_pcm_pc_pc_repository_pc_pc_BasicComponent_ImplementationComponentType = Generalization(general=ImplementationComponentType, specific=pcm_pc_pc_repository_pc_pc_BasicComponent)
gen_pcm_pc_pc_repository_pc_pc_RepositoryComponent_InterfaceProvidingRequiringEntity = Generalization(general=InterfaceProvidingRequiringEntity, specific=pcm_pc_pc_repository_pc_pc_RepositoryComponent)
gen_pcm_pc_pc_repository_pc_pc_ProvidedRole_Role = Generalization(general=Role, specific=pcm_pc_pc_repository_pc_pc_ProvidedRole)
gen_pcm_pc_pc_repository_pc_pc_Repository_Entity = Generalization(general=Entity, specific=pcm_pc_pc_repository_pc_pc_Repository)
gen_pcm_pc_pc_repository_pc_pc_Interface_Entity = Generalization(general=Entity, specific=pcm_pc_pc_repository_pc_pc_Interface)
gen_pcm_pc_pc_repository_pc_pc_EventGroup_Interface = Generalization(general=Interface, specific=pcm_pc_pc_repository_pc_pc_EventGroup)
gen_pcm_pc_pc_repository_pc_pc_EventType_Signature = Generalization(general=Signature, specific=pcm_pc_pc_repository_pc_pc_EventType)
gen_pcm_pc_pc_repository_pc_pc_Signature_Entity = Generalization(general=Entity, specific=pcm_pc_pc_repository_pc_pc_Signature)
gen_pcm_pc_pc_repository_pc_pc_InfrastructureSignature_Signature = Generalization(general=Signature, specific=pcm_pc_pc_repository_pc_pc_InfrastructureSignature)
gen_pcm_pc_pc_repository_pc_pc_InfrastructureInterface_Interface = Generalization(general=Interface, specific=pcm_pc_pc_repository_pc_pc_InfrastructureInterface)
gen_pcm_pc_pc_repository_pc_pc_OperationSignature_Signature = Generalization(general=Signature, specific=pcm_pc_pc_repository_pc_pc_OperationSignature)
gen_pcm_pc_pc_repository_pc_pc_OperationInterface_Interface = Generalization(general=Interface, specific=pcm_pc_pc_repository_pc_pc_OperationInterface)
gen_pcm_pc_pc_repository_pc_pc_OperationRequiredRole_RequiredRole = Generalization(general=RequiredRole, specific=pcm_pc_pc_repository_pc_pc_OperationRequiredRole)
gen_pcm_pc_pc_repository_pc_pc_SourceRole_RequiredRole = Generalization(general=RequiredRole, specific=pcm_pc_pc_repository_pc_pc_SourceRole)
gen_pcm_pc_pc_repository_pc_pc_InfrastructureRequiredRole_RequiredRole = Generalization(general=RequiredRole, specific=pcm_pc_pc_repository_pc_pc_InfrastructureRequiredRole)
gen_pcm_pc_pc_repository_pc_pc_RequiredRole_Role = Generalization(general=Role, specific=pcm_pc_pc_repository_pc_pc_RequiredRole)
gen_pcm_pc_pc_repository_pc_pc_OperationProvidedRole_ProvidedRole = Generalization(general=ProvidedRole, specific=pcm_pc_pc_repository_pc_pc_OperationProvidedRole)
gen_pcm_pc_pc_repository_pc_pc_InfrastructureProvidedRole_ProvidedRole = Generalization(general=ProvidedRole, specific=pcm_pc_pc_repository_pc_pc_InfrastructureProvidedRole)
gen_pcm_pc_pc_repository_pc_pc_CompleteComponentType_RepositoryComponent = Generalization(general=RepositoryComponent, specific=pcm_pc_pc_repository_pc_pc_CompleteComponentType)
gen_pcm_pc_pc_repository_pc_pc_ProvidesComponentType_RepositoryComponent = Generalization(general=RepositoryComponent, specific=pcm_pc_pc_repository_pc_pc_ProvidesComponentType)
gen_pcm_pc_pc_repository_pc_pc_SinkRole_ProvidedRole = Generalization(general=ProvidedRole, specific=pcm_pc_pc_repository_pc_pc_SinkRole)
gen_pcm_pc_pc_repository_pc_pc_PrimitiveDataType_DataType = Generalization(general=DataType, specific=pcm_pc_pc_repository_pc_pc_PrimitiveDataType)
gen_pcm_pc_pc_repository_pc_pc_CollectionDataType_entity_pc_pc_Entity = Generalization(general=entity_pc_pc_Entity, specific=pcm_pc_pc_repository_pc_pc_CollectionDataType)
gen_pcm_pc_pc_repository_pc_pc_CollectionDataType_repository_pc_pc_DataType = Generalization(general=repository_pc_pc_DataType, specific=pcm_pc_pc_repository_pc_pc_CollectionDataType)
gen_pcm_pc_pc_repository_pc_pc_CompositeDataType_entity_pc_pc_Entity = Generalization(general=entity_pc_pc_Entity, specific=pcm_pc_pc_repository_pc_pc_CompositeDataType)
gen_pcm_pc_pc_repository_pc_pc_CompositeDataType_repository_pc_pc_DataType = Generalization(general=repository_pc_pc_DataType, specific=pcm_pc_pc_repository_pc_pc_CompositeDataType)
gen_pcm_pc_pc_repository_pc_pc_CompositeComponent_entity_pc_pc_ComposedProvidingRequiringEntity = Generalization(general=entity_pc_pc_ComposedProvidingRequiringEntity, specific=pcm_pc_pc_repository_pc_pc_CompositeComponent)
gen_pcm_pc_pc_repository_pc_pc_CompositeComponent_repository_pc_pc_ImplementationComponentType = Generalization(general=repository_pc_pc_ImplementationComponentType, specific=pcm_pc_pc_repository_pc_pc_CompositeComponent)
gen_pcm_pc_pc_repository_pc_pc_InnerDeclaration_NamedElement = Generalization(general=NamedElement, specific=pcm_pc_pc_repository_pc_pc_InnerDeclaration)
gen_pcm_pc_pc_repository_pc_pc_Role_Entity = Generalization(general=Entity, specific=pcm_pc_pc_repository_pc_pc_Role)
gen_pcm_pc_pc_resourcetype_pc_pc_ResourceSignature_Entity = Generalization(general=Entity, specific=pcm_pc_pc_resourcetype_pc_pc_ResourceSignature)
gen_pcm_pc_pc_resourcetype_pc_pc_ProcessingResourceType_ResourceType = Generalization(general=ResourceType, specific=pcm_pc_pc_resourcetype_pc_pc_ProcessingResourceType)
gen_pcm_pc_pc_resourcetype_pc_pc_ResourceType_entity_pc_pc_Entity = Generalization(general=entity_pc_pc_Entity, specific=pcm_pc_pc_resourcetype_pc_pc_ResourceType)
gen_pcm_pc_pc_resourcetype_pc_pc_ResourceType_UnitCarryingElement = Generalization(general=UnitCarryingElement, specific=pcm_pc_pc_resourcetype_pc_pc_ResourceType)
gen_pcm_pc_pc_resourcetype_pc_pc_ResourceType_entity_pc_pc_ResourceInterfaceProvidingEntity = Generalization(general=entity_pc_pc_ResourceInterfaceProvidingEntity, specific=pcm_pc_pc_resourcetype_pc_pc_ResourceType)
gen_pcm_pc_pc_resourcetype_pc_pc_SchedulingPolicy_Entity = Generalization(general=Entity, specific=pcm_pc_pc_resourcetype_pc_pc_SchedulingPolicy)
gen_pcm_pc_pc_resourcetype_pc_pc_CommunicationLinkResourceType_ResourceType = Generalization(general=ResourceType, specific=pcm_pc_pc_resourcetype_pc_pc_CommunicationLinkResourceType)
gen_pcm_pc_pc_resourcetype_pc_pc_ResourceInterface_Entity = Generalization(general=Entity, specific=pcm_pc_pc_resourcetype_pc_pc_ResourceInterface)
gen_pcm_pc_pc_reliability_pc_pc_HardwareInducedFailureType_FailureType = Generalization(general=FailureType, specific=pcm_pc_pc_reliability_pc_pc_HardwareInducedFailureType)
gen_pcm_pc_pc_parameter_pc_pc_CharacterisedVariable_Variable = Generalization(general=Variable, specific=pcm_pc_pc_parameter_pc_pc_CharacterisedVariable)
gen_pcm_pc_pc_reliability_pc_pc_InternalFailureOccurrenceDescription_FailureOccurrenceDescription = Generalization(general=FailureOccurrenceDescription, specific=pcm_pc_pc_reliability_pc_pc_InternalFailureOccurrenceDescription)
gen_pcm_pc_pc_reliability_pc_pc_NetworkInducedFailureType_FailureType = Generalization(general=FailureType, specific=pcm_pc_pc_reliability_pc_pc_NetworkInducedFailureType)
gen_pcm_pc_pc_reliability_pc_pc_ExternalFailureOccurrenceDescription_FailureOccurrenceDescription = Generalization(general=FailureOccurrenceDescription, specific=pcm_pc_pc_reliability_pc_pc_ExternalFailureOccurrenceDescription)
gen_pcm_pc_pc_reliability_pc_pc_SoftwareInducedFailureType_FailureType = Generalization(general=FailureType, specific=pcm_pc_pc_reliability_pc_pc_SoftwareInducedFailureType)
gen_pcm_pc_pc_reliability_pc_pc_ResourceTimeoutFailureType_SoftwareInducedFailureType = Generalization(general=SoftwareInducedFailureType, specific=pcm_pc_pc_reliability_pc_pc_ResourceTimeoutFailureType)
gen_pcm_pc_pc_reliability_pc_pc_FailureType_Entity = Generalization(general=Entity, specific=pcm_pc_pc_reliability_pc_pc_FailureType)
gen_pcm_pc_pc_seff_pc_pc_StopAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_pc_pc_seff_pc_pc_StopAction)
gen_pcm_pc_pc_seff_pc_pc_AbstractInternalControlFlowAction_AbstractAction = Generalization(general=AbstractAction, specific=pcm_pc_pc_seff_pc_pc_AbstractInternalControlFlowAction)
gen_pcm_pc_pc_seff_pc_pc_AbstractAction_Entity = Generalization(general=Entity, specific=pcm_pc_pc_seff_pc_pc_AbstractAction)
gen_pcm_pc_pc_seff_pc_pc_AbstractLoopAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_pc_pc_seff_pc_pc_AbstractLoopAction)
gen_pcm_pc_pc_seff_pc_pc_AbstractBranchTransition_Entity = Generalization(general=Entity, specific=pcm_pc_pc_seff_pc_pc_AbstractBranchTransition)
gen_pcm_pc_pc_seff_pc_pc_ResourceDemandingBehaviour_Identifier = Generalization(general=Identifier, specific=pcm_pc_pc_seff_pc_pc_ResourceDemandingBehaviour)
gen_pcm_pc_pc_seff_pc_pc_StartAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_pc_pc_seff_pc_pc_StartAction)
gen_pcm_pc_pc_seff_pc_pc_BranchAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_pc_pc_seff_pc_pc_BranchAction)
gen_pcm_pc_pc_seff_pc_pc_ResourceDemandingInternalBehaviour_ResourceDemandingBehaviour = Generalization(general=ResourceDemandingBehaviour, specific=pcm_pc_pc_seff_pc_pc_ResourceDemandingInternalBehaviour)
gen_pcm_pc_pc_seff_pc_pc_ReleaseAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_pc_pc_seff_pc_pc_ReleaseAction)
gen_pcm_pc_pc_seff_pc_pc_LoopAction_AbstractLoopAction = Generalization(general=AbstractLoopAction, specific=pcm_pc_pc_seff_pc_pc_LoopAction)
gen_pcm_pc_pc_seff_pc_pc_ForkAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_pc_pc_seff_pc_pc_ForkAction)
gen_pcm_pc_pc_seff_pc_pc_ForkedBehaviour_ResourceDemandingBehaviour = Generalization(general=ResourceDemandingBehaviour, specific=pcm_pc_pc_seff_pc_pc_ForkedBehaviour)
gen_pcm_pc_pc_seff_pc_pc_ResourceDemandingSEFF_Identifier = Generalization(general=Identifier, specific=pcm_pc_pc_seff_pc_pc_ResourceDemandingSEFF)
gen_pcm_pc_pc_seff_pc_pc_ResourceDemandingSEFF_seff_pc_pc_ServiceEffectSpecification = Generalization(general=seff_pc_pc_ServiceEffectSpecification, specific=pcm_pc_pc_seff_pc_pc_ResourceDemandingSEFF)
gen_pcm_pc_pc_seff_pc_pc_ResourceDemandingSEFF_seff_pc_pc_ResourceDemandingBehaviour = Generalization(general=seff_pc_pc_ResourceDemandingBehaviour, specific=pcm_pc_pc_seff_pc_pc_ResourceDemandingSEFF)
gen_pcm_pc_pc_seff_pc_pc_ExternalCallAction_seff_pc_pc_CallReturnAction = Generalization(general=seff_pc_pc_CallReturnAction, specific=pcm_pc_pc_seff_pc_pc_ExternalCallAction)
gen_pcm_pc_pc_seff_pc_pc_ExternalCallAction_seff_reliability_pc_pc_FailureHandlingEntity = Generalization(general=seff_reliability_pc_pc_FailureHandlingEntity, specific=pcm_pc_pc_seff_pc_pc_ExternalCallAction)
gen_pcm_pc_pc_seff_pc_pc_CallReturnAction_CallAction = Generalization(general=CallAction, specific=pcm_pc_pc_seff_pc_pc_CallReturnAction)
gen_pcm_pc_pc_seff_pc_pc_ExternalCallAction_seff_pc_pc_AbstractAction = Generalization(general=seff_pc_pc_AbstractAction, specific=pcm_pc_pc_seff_pc_pc_ExternalCallAction)
gen_pcm_pc_pc_seff_pc_pc_CollectionIteratorAction_AbstractLoopAction = Generalization(general=AbstractLoopAction, specific=pcm_pc_pc_seff_pc_pc_CollectionIteratorAction)
gen_pcm_pc_pc_seff_pc_pc_GuardedBranchTransition_AbstractBranchTransition = Generalization(general=AbstractBranchTransition, specific=pcm_pc_pc_seff_pc_pc_GuardedBranchTransition)
gen_pcm_pc_pc_seff_pc_pc_SetVariableAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_pc_pc_seff_pc_pc_SetVariableAction)
gen_pcm_pc_pc_seff_pc_pc_InternalCallAction_seff_pc_pc_CallAction = Generalization(general=seff_pc_pc_CallAction, specific=pcm_pc_pc_seff_pc_pc_InternalCallAction)
gen_pcm_pc_pc_seff_pc_pc_InternalCallAction_seff_pc_pc_AbstractInternalControlFlowAction = Generalization(general=seff_pc_pc_AbstractInternalControlFlowAction, specific=pcm_pc_pc_seff_pc_pc_InternalCallAction)
gen_pcm_pc_pc_seff_pc_pc_EmitEventAction_seff_pc_pc_AbstractAction = Generalization(general=seff_pc_pc_AbstractAction, specific=pcm_pc_pc_seff_pc_pc_EmitEventAction)
gen_pcm_pc_pc_seff_pc_pc_EmitEventAction_seff_pc_pc_CallAction = Generalization(general=seff_pc_pc_CallAction, specific=pcm_pc_pc_seff_pc_pc_EmitEventAction)
gen_pcm_pc_pc_seff_pc_pc_ProbabilisticBranchTransition_AbstractBranchTransition = Generalization(general=AbstractBranchTransition, specific=pcm_pc_pc_seff_pc_pc_ProbabilisticBranchTransition)
gen_pcm_pc_pc_seff_pc_pc_AcquireAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_pc_pc_seff_pc_pc_AcquireAction)
gen_pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall_CallAction = Generalization(general=CallAction, specific=pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall)
gen_pcm_pc_pc_seff_pc_pc_InternalAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_pc_pc_seff_pc_pc_InternalAction)
gen_pcm_pc_pc_seff_reliability_pc_pc_RecoveryActionBehaviour_seff_reliability_pc_pc_FailureHandlingEntity = Generalization(general=seff_reliability_pc_pc_FailureHandlingEntity, specific=pcm_pc_pc_seff_reliability_pc_pc_RecoveryActionBehaviour)
gen_pcm_pc_pc_seff_reliability_pc_pc_RecoveryActionBehaviour_seff_pc_pc_ResourceDemandingBehaviour = Generalization(general=seff_pc_pc_ResourceDemandingBehaviour, specific=pcm_pc_pc_seff_reliability_pc_pc_RecoveryActionBehaviour)
gen_pcm_pc_pc_seff_performance_pc_pc_ResourceCall_CallAction = Generalization(general=CallAction, specific=pcm_pc_pc_seff_performance_pc_pc_ResourceCall)
gen_pcm_pc_pc_seff_reliability_pc_pc_RecoveryAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_pc_pc_seff_reliability_pc_pc_RecoveryAction)
gen_pcm_pc_pc_seff_reliability_pc_pc_FailureHandlingEntity_Entity = Generalization(general=Entity, specific=pcm_pc_pc_seff_reliability_pc_pc_FailureHandlingEntity)
gen_pcm_pc_pc_qos_performance_pc_pc_SystemSpecifiedExecutionTime_SpecifiedExecutionTime = Generalization(general=SpecifiedExecutionTime, specific=pcm_pc_pc_qos_performance_pc_pc_SystemSpecifiedExecutionTime)
gen_pcm_pc_pc_qos_performance_pc_pc_SpecifiedExecutionTime_SpecifiedQoSAnnotation = Generalization(general=SpecifiedQoSAnnotation, specific=pcm_pc_pc_qos_performance_pc_pc_SpecifiedExecutionTime)
gen_pcm_pc_pc_qosannotations_pc_pc_QoSAnnotations_Entity = Generalization(general=Entity, specific=pcm_pc_pc_qosannotations_pc_pc_QoSAnnotations)
gen_pcm_pc_pc_system_pc_pc_System_entity_pc_pc_Entity = Generalization(general=entity_pc_pc_Entity, specific=pcm_pc_pc_system_pc_pc_System)
gen_pcm_pc_pc_system_pc_pc_System_entity_pc_pc_ComposedProvidingRequiringEntity = Generalization(general=entity_pc_pc_ComposedProvidingRequiringEntity, specific=pcm_pc_pc_system_pc_pc_System)
gen_pcm_pc_pc_qos_performance_pc_pc_ComponentSpecifiedExecutionTime_SpecifiedExecutionTime = Generalization(general=SpecifiedExecutionTime, specific=pcm_pc_pc_qos_performance_pc_pc_ComponentSpecifiedExecutionTime)
gen_pcm_pc_pc_qos_reliability_pc_pc_SpecifiedReliabilityAnnotation_SpecifiedQoSAnnotation = Generalization(general=SpecifiedQoSAnnotation, specific=pcm_pc_pc_qos_reliability_pc_pc_SpecifiedReliabilityAnnotation)
gen_pcm_pc_pc_resourceenvironment_pc_pc_ResourceContainer_Entity = Generalization(general=Entity, specific=pcm_pc_pc_resourceenvironment_pc_pc_ResourceContainer)
gen_pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification_Identifier = Generalization(general=Identifier, specific=pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification)
gen_pcm_pc_pc_resourceenvironment_pc_pc_ResourceEnvironment_NamedElement = Generalization(general=NamedElement, specific=pcm_pc_pc_resourceenvironment_pc_pc_ResourceEnvironment)
gen_pcm_pc_pc_resourceenvironment_pc_pc_LinkingResource_Entity = Generalization(general=Entity, specific=pcm_pc_pc_resourceenvironment_pc_pc_LinkingResource)
gen_pcm_pc_pc_allocation_pc_pc_AllocationContext_Entity = Generalization(general=Entity, specific=pcm_pc_pc_allocation_pc_pc_AllocationContext)
gen_pcm_pc_pc_resourceenvironment_pc_pc_CommunicationLinkResourceSpecification_Identifier = Generalization(general=Identifier, specific=pcm_pc_pc_resourceenvironment_pc_pc_CommunicationLinkResourceSpecification)
gen_pcm_pc_pc_allocation_pc_pc_Allocation_Entity = Generalization(general=Entity, specific=pcm_pc_pc_allocation_pc_pc_Allocation)
gen_pcm_pc_pc_subsystem_pc_pc_SubSystem_entity_pc_pc_ComposedProvidingRequiringEntity = Generalization(general=entity_pc_pc_ComposedProvidingRequiringEntity, specific=pcm_pc_pc_subsystem_pc_pc_SubSystem)
gen_pcm_pc_pc_subsystem_pc_pc_SubSystem_repository_pc_pc_RepositoryComponent = Generalization(general=repository_pc_pc_RepositoryComponent, specific=pcm_pc_pc_subsystem_pc_pc_SubSystem)
gen_pcm_pc_pc_completions_pc_pc_Completion_entity_pc_pc_ComposedProvidingRequiringEntity = Generalization(general=entity_pc_pc_ComposedProvidingRequiringEntity, specific=pcm_pc_pc_completions_pc_pc_Completion)
gen_pcm_pc_pc_completions_pc_pc_Completion_repository_pc_pc_ImplementationComponentType = Generalization(general=repository_pc_pc_ImplementationComponentType, specific=pcm_pc_pc_completions_pc_pc_Completion)
gen_pcm_pc_pc_completions_pc_pc_DelegatingExternalCallAction_ExternalCallAction = Generalization(general=ExternalCallAction, specific=pcm_pc_pc_completions_pc_pc_DelegatingExternalCallAction)
gen_pcm_pc_pc_completions_pc_pc_NetworkDemandParametricResourceDemand_ParametricResourceDemand = Generalization(general=ParametricResourceDemand, specific=pcm_pc_pc_completions_pc_pc_NetworkDemandParametricResourceDemand)

# Domain Model
domain_model = DomainModel(
    name="pcm_pc_pc",
    types={seff_performance_pc_pc_ResourceCall, seff_performance_pc_pc_ParametricResourceDemand, LoopAction, GuardedBranchTransition, pcm_pc_pc_DummyClass, pcm_pc_pc_PointcutPointcut, pcm_pc_pc_EObject, pcm_pc_pc_Pointcut, pcm_pc_pc_core_pc_pc_PCMRandomVariable, RandomVariable, ClosedWorkload, PassiveResource, VariableCharacterisation, seff_performance_pc_pc_InfrastructureCall, entity_pc_pc_ResourceInterfaceProvidingEntity, ResourceInterface, pcm_pc_pc_entity_pc_pc_InterfaceProvidingRequiringEntity, entity_pc_pc_InterfaceProvidingEntity, entity_pc_pc_InterfaceRequiringEntity, pcm_pc_pc_entity_pc_pc_InterfaceProvidingEntity, Entity, ProvidedRole, qos_performance_pc_pc_SpecifiedExecutionTime, composition_pc_pc_EventChannelSinkConnector, composition_pc_pc_AssemblyEventConnector, Loop, OpenWorkload, Delay, CommunicationLinkResourceSpecification, ProcessingResourceSpecification, pcm_pc_pc_entity_pc_pc_ResourceProvidedRole, Role, pcm_pc_pc_entity_pc_pc_ResourceInterfaceProvidingRequiringEntity, pcm_pc_pc_entity_pc_pc_Entity, Identifier, entity_pc_pc_NamedElement, pcm_pc_pc_composition_pc_pc_DelegationConnector, Connector, pcm_pc_pc_composition_pc_pc_Connector, pcm_pc_pc_entity_pc_pc_InterfaceRequiringEntity, entity_pc_pc_Entity, entity_pc_pc_ResourceInterfaceRequiringEntity, RequiredRole, pcm_pc_pc_entity_pc_pc_ResourceInterfaceRequiringEntity, entity_pc_pc_ResourceRequiredRole, pcm_pc_pc_entity_pc_pc_ResourceRequiredRole, pcm_pc_pc_entity_pc_pc_ResourceInterfaceProvidingEntity, entity_pc_pc_ResourceProvidedRole, pcm_pc_pc_entity_pc_pc_ComposedProvidingRequiringEntity, composition_pc_pc_ComposedStructure, entity_pc_pc_InterfaceProvidingRequiringEntity, pcm_pc_pc_entity_pc_pc_NamedElement, composition_pc_pc_ResourceRequiredDelegationConnector, composition_pc_pc_EventChannel, composition_pc_pc_Connector, pcm_pc_pc_composition_pc_pc_ResourceRequiredDelegationConnector, pcm_pc_pc_composition_pc_pc_ComposedStructure, composition_pc_pc_AssemblyContext, pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector, DelegationConnector, pcm_pc_pc_composition_pc_pc_EventChannel, EventGroup, composition_pc_pc_EventChannelSourceConnector, pcm_pc_pc_composition_pc_pc_EventChannelSourceConnector, SourceRole, pcm_pc_pc_composition_pc_pc_EventChannelSinkConnector, SinkRole, PCMRandomVariable, OperationRequiredRole, pcm_pc_pc_composition_pc_pc_AssemblyConnector, OperationProvidedRole, pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector, pcm_pc_pc_composition_pc_pc_SourceDelegationConnector, pcm_pc_pc_composition_pc_pc_SinkDelegationConnector, pcm_pc_pc_composition_pc_pc_AssemblyInfrastructureConnector, InfrastructureProvidedRole, InfrastructureRequiredRole, pcm_pc_pc_composition_pc_pc_AssemblyEventConnector, pcm_pc_pc_composition_pc_pc_RequiredResourceDelegationConnector, pcm_pc_pc_composition_pc_pc_AssemblyContext, RepositoryComponent, VariableUsage, pcm_pc_pc_usagemodel_pc_pc_Workload, UsageScenario, pcm_pc_pc_usagemodel_pc_pc_UsageScenario, UsageModel, pcm_pc_pc_composition_pc_pc_ProvidedInfrastructureDelegationConnector, pcm_pc_pc_composition_pc_pc_RequiredInfrastructureDelegationConnector, pcm_pc_pc_usagemodel_pc_pc_UsageModel, UserData, pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall, AbstractUserAction, OperationSignature, pcm_pc_pc_usagemodel_pc_pc_AbstractUserAction, ScenarioBehaviour, Workload, pcm_pc_pc_usagemodel_pc_pc_UserData, BranchTransition, pcm_pc_pc_usagemodel_pc_pc_BranchTransition, pcm_pc_pc_usagemodel_pc_pc_ScenarioBehaviour, pcm_pc_pc_usagemodel_pc_pc_Loop, pcm_pc_pc_usagemodel_pc_pc_Stop, pcm_pc_pc_usagemodel_pc_pc_Start, pcm_pc_pc_usagemodel_pc_pc_OpenWorkload, Branch, pcm_pc_pc_usagemodel_pc_pc_Branch, pcm_pc_pc_usagemodel_pc_pc_ClosedWorkload, pcm_pc_pc_repository_pc_pc_PassiveResource, BasicComponent, ResourceTimeoutFailureType, pcm_pc_pc_usagemodel_pc_pc_Delay, ServiceEffectSpecification, pcm_pc_pc_repository_pc_pc_ImplementationComponentType, pcm_pc_pc_repository_pc_pc_BasicComponent, ImplementationComponentType, CompleteComponentType, pcm_pc_pc_repository_pc_pc_RepositoryComponent, InterfaceProvidingRequiringEntity, Repository, pcm_pc_pc_repository_pc_pc_ProvidedRole, pcm_pc_pc_repository_pc_pc_Parameter, DataType, InfrastructureSignature, EventType, pcm_pc_pc_repository_pc_pc_Repository, Interface, FailureType, pcm_pc_pc_repository_pc_pc_Interface, Protocol, ResourceSignature, pcm_pc_pc_repository_pc_pc_DataType, pcm_pc_pc_repository_pc_pc_RequiredCharacterisation, Parameter_, pcm_pc_pc_repository_pc_pc_EventGroup, pcm_pc_pc_repository_pc_pc_EventType, Signature, pcm_pc_pc_repository_pc_pc_Signature, ExceptionType, pcm_pc_pc_repository_pc_pc_ExceptionType, pcm_pc_pc_repository_pc_pc_InfrastructureSignature, InfrastructureInterface, pcm_pc_pc_repository_pc_pc_InfrastructureInterface, RequiredCharacterisation, pcm_pc_pc_repository_pc_pc_OperationSignature, OperationInterface, pcm_pc_pc_repository_pc_pc_OperationInterface, pcm_pc_pc_repository_pc_pc_OperationRequiredRole, pcm_pc_pc_repository_pc_pc_SourceRole, pcm_pc_pc_repository_pc_pc_InfrastructureRequiredRole, pcm_pc_pc_repository_pc_pc_RequiredRole, pcm_pc_pc_repository_pc_pc_OperationProvidedRole, pcm_pc_pc_repository_pc_pc_InfrastructureProvidedRole, pcm_pc_pc_repository_pc_pc_CompleteComponentType, ProvidesComponentType, pcm_pc_pc_repository_pc_pc_ProvidesComponentType, pcm_pc_pc_repository_pc_pc_SinkRole, pcm_pc_pc_repository_pc_pc_PrimitiveDataType, pcm_pc_pc_repository_pc_pc_CollectionDataType, repository_pc_pc_DataType, pcm_pc_pc_repository_pc_pc_CompositeDataType, pcm_pc_pc_repository_pc_pc_CompositeComponent, entity_pc_pc_ComposedProvidingRequiringEntity, repository_pc_pc_ImplementationComponentType, InnerDeclaration, pcm_pc_pc_repository_pc_pc_InnerDeclaration, NamedElement, pcm_pc_pc_repository_pc_pc_Role, pcm_pc_pc_resourcetype_pc_pc_ResourceSignature, pcm_pc_pc_resourcetype_pc_pc_ProcessingResourceType, ResourceType, HardwareInducedFailureType, pcm_pc_pc_resourcetype_pc_pc_ResourceType, UnitCarryingElement, CompositeDataType, pcm_pc_pc_resourcetype_pc_pc_ResourceRepository, SchedulingPolicy, pcm_pc_pc_resourcetype_pc_pc_SchedulingPolicy, pcm_pc_pc_resourcetype_pc_pc_CommunicationLinkResourceType, NetworkInducedFailureType, pcm_pc_pc_resourcetype_pc_pc_ResourceInterface, pcm_pc_pc_protocol_pc_pc_Protocol, ResourceRepository, CallAction, SynchronisationPoint, CallReturnAction, SetVariableAction, SpecifiedOutputParameterAbstraction, EntryLevelSystemCall, parameter_pc_pc_pcm_pc_pc_AbstractNamedReference, pcm_pc_pc_parameter_pc_pc_VariableCharacterisation, pcm_pc_pc_parameter_pc_pc_VariableUsage, pcm_pc_pc_reliability_pc_pc_FailureOccurrenceDescription, pcm_pc_pc_reliability_pc_pc_HardwareInducedFailureType, pcm_pc_pc_parameter_pc_pc_CharacterisedVariable, Variable, InternalFailureOccurrenceDescription, pcm_pc_pc_reliability_pc_pc_InternalFailureOccurrenceDescription, FailureOccurrenceDescription, InternalAction, SoftwareInducedFailureType, pcm_pc_pc_reliability_pc_pc_NetworkInducedFailureType, CommunicationLinkResourceType, pcm_pc_pc_reliability_pc_pc_ExternalFailureOccurrenceDescription, ProcessingResourceType, pcm_pc_pc_reliability_pc_pc_SoftwareInducedFailureType, pcm_pc_pc_reliability_pc_pc_ResourceTimeoutFailureType, pcm_pc_pc_reliability_pc_pc_FailureType, pcm_pc_pc_seff_pc_pc_StopAction, AbstractInternalControlFlowAction, pcm_pc_pc_seff_pc_pc_AbstractInternalControlFlowAction, AbstractAction, pcm_pc_pc_seff_pc_pc_AbstractAction, qos_reliability_pc_pc_SpecifiedReliabilityAnnotation, AbstractLoopAction, AbstractBranchTransition, pcm_pc_pc_seff_pc_pc_AbstractLoopAction, pcm_pc_pc_seff_pc_pc_AbstractBranchTransition, BranchAction, ResourceDemandingBehaviour, pcm_pc_pc_seff_pc_pc_ResourceDemandingBehaviour, pcm_pc_pc_seff_pc_pc_CallAction, pcm_pc_pc_seff_pc_pc_StartAction, pcm_pc_pc_seff_pc_pc_ServiceEffectSpecification, pcm_pc_pc_seff_pc_pc_BranchAction, pcm_pc_pc_seff_pc_pc_ResourceDemandingInternalBehaviour, ResourceDemandingSEFF, pcm_pc_pc_seff_pc_pc_ReleaseAction, pcm_pc_pc_seff_pc_pc_LoopAction, pcm_pc_pc_seff_pc_pc_ForkAction, ForkedBehaviour, pcm_pc_pc_seff_pc_pc_ForkedBehaviour, ForkAction, pcm_pc_pc_seff_pc_pc_SynchronisationPoint, pcm_pc_pc_seff_pc_pc_ResourceDemandingSEFF, seff_pc_pc_ServiceEffectSpecification, seff_pc_pc_ResourceDemandingBehaviour, ResourceDemandingInternalBehaviour, seff_reliability_pc_pc_FailureHandlingEntity, pcm_pc_pc_seff_pc_pc_CallReturnAction, pcm_pc_pc_seff_pc_pc_ExternalCallAction, seff_pc_pc_AbstractAction, seff_pc_pc_CallReturnAction, pcm_pc_pc_seff_pc_pc_CollectionIteratorAction, pcm_pc_pc_seff_pc_pc_GuardedBranchTransition, pcm_pc_pc_seff_pc_pc_SetVariableAction, pcm_pc_pc_seff_pc_pc_InternalCallAction, seff_pc_pc_CallAction, seff_pc_pc_AbstractInternalControlFlowAction, pcm_pc_pc_seff_pc_pc_EmitEventAction, pcm_pc_pc_seff_pc_pc_InternalAction, pcm_pc_pc_seff_pc_pc_ProbabilisticBranchTransition, pcm_pc_pc_seff_pc_pc_AcquireAction, pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall, pcm_pc_pc_seff_performance_pc_pc_ParametricResourceDemand, pcm_pc_pc_seff_reliability_pc_pc_RecoveryActionBehaviour, pcm_pc_pc_seff_performance_pc_pc_ResourceCall, seff_reliability_pc_pc_RecoveryActionBehaviour, seff_reliability_pc_pc_RecoveryAction, pcm_pc_pc_seff_reliability_pc_pc_RecoveryAction, pcm_pc_pc_seff_reliability_pc_pc_FailureHandlingEntity, pcm_pc_pc_qosannotations_pc_pc_SpecifiedQoSAnnotation, System, SpecifiedQoSAnnotation, pcm_pc_pc_qosannotations_pc_pc_SpecifiedOutputParameterAbstraction, pcm_pc_pc_qos_performance_pc_pc_SystemSpecifiedExecutionTime, SpecifiedExecutionTime, pcm_pc_pc_qos_performance_pc_pc_SpecifiedExecutionTime, QoSAnnotations, pcm_pc_pc_qosannotations_pc_pc_QoSAnnotations, ExternalFailureOccurrenceDescription, pcm_pc_pc_system_pc_pc_System, pcm_pc_pc_qos_performance_pc_pc_ComponentSpecifiedExecutionTime, pcm_pc_pc_qos_reliability_pc_pc_SpecifiedReliabilityAnnotation, ResourceEnvironment, pcm_pc_pc_resourceenvironment_pc_pc_ResourceContainer, pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification, pcm_pc_pc_resourceenvironment_pc_pc_ResourceEnvironment, LinkingResource, ResourceContainer, pcm_pc_pc_resourceenvironment_pc_pc_LinkingResource, pcm_pc_pc_allocation_pc_pc_AllocationContext, pcm_pc_pc_resourceenvironment_pc_pc_CommunicationLinkResourceSpecification, pcm_pc_pc_allocation_pc_pc_Allocation, AllocationContext, pcm_pc_pc_subsystem_pc_pc_SubSystem, repository_pc_pc_RepositoryComponent, pcm_pc_pc_completions_pc_pc_Completion, pcm_pc_pc_completions_pc_pc_CompletionRepository, Completion, Allocation, pcm_pc_pc_completions_pc_pc_DelegatingExternalCallAction, ExternalCallAction, pcm_pc_pc_completions_pc_pc_NetworkDemandParametricResourceDemand, ParametricResourceDemand, ParameterModifier, PrimitiveTypeEnum, ComponentType, VariableCharacterisationType},
    associations={infrastructureCall__PCMRandomVariable6, resourceCall__PCMRandomVariable7, parametricResourceDemand_PCMRandomVariable8, loopAction_PCMRandomVariable9, children0, children1, closedWorkload_PCMRandomVariable3, passiveResource_capacity_PCMRandomVariable4, variableCharacterisation_Specification5, resourceInterfaceProvidingEntity__ResourceProvidedRole21, providedResourceInterface__ResourceProvidedRole22, providedRoles_InterfaceProvidingEntity23, guardedBranchTransition_PCMRandomVariable10, specifiedExecutionTime_PCMRandomVariable11, eventChannelSinkConnector__FilterCondition12, assemblyEventConnector__FilterCondition13, loop_LoopIteration14, openWorkload_PCMRandomVariable15, delay_TimeSpecification16, communicationLinkResourceSpecifcation_throughput_PCMRandomVariable17, processingResourceSpecification_processingRate_PCMRandomVariable18, communicationLinkResourceSpecification_latency_PCMRandomVariable19, requiredRoles_InterfaceRequiringEntity24, resourceRequiredRoles__ResourceInterfaceRequiringEntity25, requiredResourceInterface__ResourceRequiredRole26, resourceInterfaceRequiringEntity__ResourceRequiredRole28, resourceProvidedRoles__ResourceInterfaceProvidingEntity29, resourceRequiredDelegationConnectors_ComposedStructure32, eventChannel__ComposedStructure33, connectors__ComposedStructure34, innerResourceRequiredRole_ResourceRequiredDelegationConnector35, parentStructure__Connector30, assemblyContexts__ComposedStructure31, eventChannel__EventChannelSinkConnector57, outerResourceRequiredRole_ResourceRequiredDelegationConnector36, parentStructure_ResourceRequiredDelegationConnector39, eventGroup__EventChannel41, eventChannelSourceConnector__EventChannel42, eventChannelSinkConnector__EventChannel43, parentStructure__EventChannel45, sourceRole__EventChannelSourceRole47, assemblyContext__EventChannelSourceConnector48, eventChannel__EventChannelSourceConnector50, sinkRole__EventChannelSinkConnector52, filterCondition__EventChannelSinkConnector53, assemblyContext__EventChannelSinkConnector54, innerRequiredRole_RequiredDelegationConnector66, outerRequiredRole_RequiredDelegationConnector67, assemblyContext_RequiredDelegationConnector70, innerProvidedRole_ProvidedDelegationConnector59, outerProvidedRole_ProvidedDelegationConnector60, assemblyContext_ProvidedDelegationConnector63, requiringAssemblyContext_AssemblyConnector73, sourceRole__AssemblyEventConnector86, sinkAssemblyContext__AssemblyEventConnector89, sourceAssemblyContext__AssemblyEventConnector92, filterCondition__AssemblyEventConnector95, innerSourceRole__SourceRole97, outerSourceRole__SourceRole99, assemblyContext__SourceDelegationConnector102, assemblyContext__SinkDelegationConnector105, innerSinkRole__SinkRole107, outerSinkRole__SinkRole110, providedRole__AssemblyInfrastructureConnector113, requiredRole__AssemblyInfrastructureConnector114, providingAssemblyContext__AssemblyInfrastructureConnector116, requiringAssemblyContext__AssemblyInfrastructureConnector119, providingAssemblyContext_AssemblyConnector75, providedRole_AssemblyConnector78, requiredRole_AssemblyConnector81, sinkRole__AssemblyEventConnector84, innerRequiredRole__RequiredInfrastructureDelegationConnector130, outerRequiredRole__RequiredInfrastructureDelegationConnector132, assemblyContext__RequiredInfrastructureDelegationConnector135, assemblyContext__RequiredResourceDelegationConnector138, innerRequiredRole__RequiredResourceDelegationConnector140, outerRequiredRole__RequiredResourceDelegationConnector143, parentStructure__AssemblyContext146, encapsulatedComponent__AssemblyContext148, configParameterUsages__AssemblyContext149, usageScenario_Workload150, usageModel_UsageScenario151, innerProvidedRole__ProvidedInfrastructureDelegationConnector122, outerProvidedRole__ProvidedInfrastructureDelegationConnector124, assemblyContext__ProvidedInfrastructureDelegationConnector127, usageScenario_UsageModel160, userData_UsageModel162, providedRole_EntryLevelSystemCall163, operationSignature__EntryLevelSystemCall165, outputParameterUsages_EntryLevelSystemCall167, inputParameterUsages_EntryLevelSystemCall169, scenarioBehaviour_UsageScenario152, workload_UsageScenario153, assemblyContext_userData154, usageModel_UserData156, userDataParameterUsages_UserData158, usageScenario_SenarioBehaviour176, branchTransition_ScenarioBehaviour178, loop_ScenarioBehaviour179, actions_ScenarioBehaviour181, successor171, predecessor172, scenarioBehaviour_AbstractUserAction174, branchTransitions_Branch186, loopIteration_Loop188, bodyBehaviour_Loop190, branch_BranchTransition183, branchedBehaviour_BranchTransition184, timeSpecification_Delay194, thinkTime_ClosedWorkload196, capacity_PassiveResource198, basicComponent_PassiveResource200, interArrivalTime_OpenWorkload192, serviceEffectSpecifications__BasicComponent202, passiveResource_BasicComponent203, resourceTimeoutFailureType__PassiveResource201, parentCompleteComponentTypes205, componentParameterUsage_ImplementationComponentType206, repository__RepositoryComponent209, providingEntity_ProvidedRole210, dataType__Parameter211, infrastructureSignature__Parameter212, operationSignature__Parameter213, eventType__Parameter215, components__Repository219, interfaces__Repository221, failureTypes__Repository222, dataTypes__Repository223, parentInterfaces__Interface225, protocols__Interface227, resourceSignature__Parameter216, repository__DataType217, parameter232, interface_RequiredCharacterisation233, eventTypes__EventGroup235, parameter__EventType237, eventGroup__EventType239, exceptions__Signature241, failureType242, parameters__InfrastructureSignature245, infrastructureInterface__InfrastructureSignature247, requiredCharacterisations229, repository__Interface230, requiringEntity_RequiredRole252, interface__OperationSignature253, parameters__OperationSignature254, returnType__OperationSignature256, signatures__OperationInterface258, requiredInterface__OperationRequiredRole260, infrastructureSignatures__InfrastructureInterface248, requiredInterface__InfrastructureRequiredRole250, providedInterface__OperationProvidedRole266, providedInterface__InfrastructureProvidedRole268, parentProvidesComponentTypes270, eventGroup__SourceRole262, eventGroup__SinkRole264, innerType_CollectionDataType271, innerDeclaration_CompositeDataType274, datatype_InnerDeclaration275, compositeDataType_InnerDeclaration277, parameter__ResourceSignature279, resourceInterface__ResourceSignature281, hardwareInducedFailureType__ProcessingResourceType283, parentType_CompositeDataType273, resourceInterfaces__ResourceRepository285, schedulingPolicies__ResourceRepository287, availableResourceTypes_ResourceRepository288, resourceRepository__SchedulingPolicy289, networkInducedFailureType__CommunicationLinkResourceType291, resourceRepository__ResourceInterface292, resourceSignatures__ResourceInterface294, resourceRepository_ResourceType284, userData_VariableUsage298, callAction__VariableUsage300, synchronisationPoint_VariableUsage301, callReturnAction__VariableUsage302, setVariableAction_VariableUsage303, specifiedOutputParameterAbstraction_expectedExternalOutputs_VariableUsage304, assemblyContext__VariableUsage305, entryLevelSystemCall_InputParameterUsage307, entryLevelSystemCall_OutputParameterUsage308, namedReference__VariableUsage310, specification_VariableCharacterisation311, variableCharacterisation_VariableUsage296, variableUsage_VariableCharacterisation313, internalFailureOccurrenceDescriptions__SoftwareInducedFailureType316, internalAction__InternalFailureOccurrenceDescription317, softwareInducedFailureType__InternalFailureOccurrenceDescription318, communicationLinkResourceType__NetworkInducedFailureType319, processingResourceType__HardwareInducedFailureType315, passiveResource__ResourceTimeoutFailureType323, repository__FailureType325, resourceDemand_Action327, infrastructureCall__Action329, resourceCall__Action331, specifiedReliabilityAnnotation__ExternalFailureOccurrenceDescription320, failureType__ExternalFailureOccurrenceDescription321, abstractLoopAction_ResourceDemandingBehaviour337, abstractBranchTransition_ResourceDemandingBehaviour339, steps_Behaviour340, bodyBehaviour_Loop342, branchAction_AbstractBranchTransition344, predecessor_AbstractAction333, successor_AbstractAction334, resourceDemandingBehaviour_AbstractAction336, branches_Branch347, inputVariableUsages__CallAction349, branchBehaviour_BranchTransition345, resourceDemandingSEFF_ResourceDemandingInternalBehaviour355, passiveResource_ReleaseAction356, iterationCount_LoopAction358, asynchronousForkedBehaviours_ForkAction360, synchronisingBehaviours_ForkAction361, synchronisationPoint_ForkedBehaviour363, forkAction_ForkedBehaivour365, outputParameterUsage_SynchronisationPoint366, describedService__SEFF351, basicComponent_ServiceEffectSpecification352, resourceDemandingInternalBehaviours354, calledService_ExternalService372, role_ExternalService374, returnVariableUsage__CallReturnAction377, forkAction_SynchronisationPoint368, synchronousForkedBehaviours_SynchronisationPoint370, passiveresource_AcquireAction379, parameter_CollectionIteratorAction381, branchCondition_GuardedBranchTransition383, localVariableUsages_SetVariableAction385, calledResourceDemandingInternalBehaviour387, eventType__EmitEventAction389, sourceRole__EmitEventAction391, internalFailureOccurrenceDescriptions__InternalAction394, signature__InfrastructureCall396, numberOfCalls__InfrastructureCall398, action__InfrastructureCall400, action__ResourceCall404, resourceRequiredRole__ResourceCall406, signature__ResourceCall408, numberOfCalls__ResourceCall411, specification_ParametericResourceDemand413, requiredResource_ParametricResourceDemand415, action_ParametricResourceDemand417, requiredRole__InfrastructureCall401, failureHandlingAlternatives__RecoveryActionBehaviour419, recoveryAction__RecoveryActionBehaviour420, primaryBehaviour__RecoveryAction421, recoveryActionBehaviours__RecoveryAction423, failureTypes_FailureHandlingEntity424, specifiedOutputParameterAbstractions_QoSAnnotations431, system_QoSAnnotations433, specifiedQoSAnnotations_QoSAnnotations434, signature_SpecifiedOutputParameterAbstraction435, role_SpecifiedOutputParameterAbstraction437, expectedExternalOutputs_SpecifiedOutputParameterAbstraction440, qosAnnotations_SpecifiedOutputParameterAbstraction442, signature_SpecifiedQoSAnnation426, role_SpecifiedQoSAnnotation428, qosAnnotations_SpecifiedQoSAnnotation430, externalFailureOccurrenceDescriptions__SpecifiedReliabilityAnnotation448, qosAnnotations_System449, specification_SpecifiedExecutionTime444, assemblyContext_ComponentSpecifiedExecutionTime446, communicationLinkResourceSpecifications_LinkingResource455, resourceEnvironment_LinkingResource457, activeResourceSpecifications_ResourceContainer458, resourceEnvironment_ResourceContainer460, nestedResourceContainers__ResourceContainer462, parentResourceContainer__ResourceContainer464, schedulingPolicy466, activeResourceType_ActiveResourceSpecification468, processingRate_ProcessingResourceSpecification471, resourceContainer_ProcessingResourceSpecification473, linkingResources__ResourceEnvironment451, resourceContainer_ResourceEnvironment452, connectedResourceContainers_LinkingResource453, linkingResource_CommunicationLinkResourceSpecification475, communicationLinkResourceType_CommunicationLinkResourceSpecification477, latency_CommunicationLinkResourceSpecification479, throughput_CommunicationLinkResourceSpecification481, resourceContainer_AllocationContext483, assemblyContext_AllocationContext485, eventChannel__AllocationContext489, targetResourceEnvironment_Allocation491, system_Allocation493, allocationContexts_Allocation496, completions_CompletionRepository497, allocation_AllocationContext488, requiredCommunicationLinkResource_ParametricResourceDemand498},
    generalizations={gen_pcm_pc_pc_core_pc_pc_PCMRandomVariable_RandomVariable, gen_pcm_pc_pc_entity_pc_pc_InterfaceProvidingRequiringEntity_entity_pc_pc_InterfaceProvidingEntity, gen_pcm_pc_pc_entity_pc_pc_InterfaceProvidingRequiringEntity_entity_pc_pc_InterfaceRequiringEntity, gen_pcm_pc_pc_entity_pc_pc_InterfaceProvidingEntity_Entity, gen_pcm_pc_pc_entity_pc_pc_ResourceProvidedRole_Role, gen_pcm_pc_pc_entity_pc_pc_ResourceInterfaceProvidingRequiringEntity_entity_pc_pc_ResourceInterfaceRequiringEntity, gen_pcm_pc_pc_entity_pc_pc_ResourceInterfaceProvidingRequiringEntity_entity_pc_pc_ResourceInterfaceProvidingEntity, gen_pcm_pc_pc_entity_pc_pc_Entity_Identifier, gen_pcm_pc_pc_entity_pc_pc_Entity_entity_pc_pc_NamedElement, gen_pcm_pc_pc_composition_pc_pc_DelegationConnector_Connector, gen_pcm_pc_pc_composition_pc_pc_Connector_Entity, gen_pcm_pc_pc_entity_pc_pc_InterfaceRequiringEntity_entity_pc_pc_Entity, gen_pcm_pc_pc_entity_pc_pc_InterfaceRequiringEntity_entity_pc_pc_ResourceInterfaceRequiringEntity, gen_pcm_pc_pc_entity_pc_pc_ResourceInterfaceRequiringEntity_Entity, gen_pcm_pc_pc_entity_pc_pc_ResourceRequiredRole_Role, gen_pcm_pc_pc_entity_pc_pc_ResourceInterfaceProvidingEntity_Entity, gen_pcm_pc_pc_entity_pc_pc_ComposedProvidingRequiringEntity_composition_pc_pc_ComposedStructure, gen_pcm_pc_pc_entity_pc_pc_ComposedProvidingRequiringEntity_entity_pc_pc_InterfaceProvidingRequiringEntity, gen_pcm_pc_pc_composition_pc_pc_ComposedStructure_Entity, gen_pcm_pc_pc_composition_pc_pc_ProvidedDelegationConnector_DelegationConnector, gen_pcm_pc_pc_composition_pc_pc_EventChannel_Entity, gen_pcm_pc_pc_composition_pc_pc_EventChannelSourceConnector_Connector, gen_pcm_pc_pc_composition_pc_pc_EventChannelSinkConnector_Connector, gen_pcm_pc_pc_composition_pc_pc_AssemblyConnector_Connector, gen_pcm_pc_pc_composition_pc_pc_RequiredDelegationConnector_DelegationConnector, gen_pcm_pc_pc_composition_pc_pc_SourceDelegationConnector_DelegationConnector, gen_pcm_pc_pc_composition_pc_pc_SinkDelegationConnector_DelegationConnector, gen_pcm_pc_pc_composition_pc_pc_AssemblyInfrastructureConnector_Connector, gen_pcm_pc_pc_composition_pc_pc_AssemblyEventConnector_Connector, gen_pcm_pc_pc_composition_pc_pc_RequiredResourceDelegationConnector_DelegationConnector, gen_pcm_pc_pc_composition_pc_pc_AssemblyContext_Entity, gen_pcm_pc_pc_usagemodel_pc_pc_UsageScenario_Entity, gen_pcm_pc_pc_composition_pc_pc_ProvidedInfrastructureDelegationConnector_DelegationConnector, gen_pcm_pc_pc_composition_pc_pc_RequiredInfrastructureDelegationConnector_DelegationConnector, gen_pcm_pc_pc_usagemodel_pc_pc_EntryLevelSystemCall_AbstractUserAction, gen_pcm_pc_pc_usagemodel_pc_pc_AbstractUserAction_Entity, gen_pcm_pc_pc_usagemodel_pc_pc_ScenarioBehaviour_Entity, gen_pcm_pc_pc_usagemodel_pc_pc_Loop_AbstractUserAction, gen_pcm_pc_pc_usagemodel_pc_pc_Stop_AbstractUserAction, gen_pcm_pc_pc_usagemodel_pc_pc_Start_AbstractUserAction, gen_pcm_pc_pc_usagemodel_pc_pc_OpenWorkload_Workload, gen_pcm_pc_pc_usagemodel_pc_pc_Branch_AbstractUserAction, gen_pcm_pc_pc_usagemodel_pc_pc_ClosedWorkload_Workload, gen_pcm_pc_pc_repository_pc_pc_PassiveResource_Entity, gen_pcm_pc_pc_usagemodel_pc_pc_Delay_AbstractUserAction, gen_pcm_pc_pc_repository_pc_pc_ImplementationComponentType_RepositoryComponent, gen_pcm_pc_pc_repository_pc_pc_BasicComponent_ImplementationComponentType, gen_pcm_pc_pc_repository_pc_pc_RepositoryComponent_InterfaceProvidingRequiringEntity, gen_pcm_pc_pc_repository_pc_pc_ProvidedRole_Role, gen_pcm_pc_pc_repository_pc_pc_Repository_Entity, gen_pcm_pc_pc_repository_pc_pc_Interface_Entity, gen_pcm_pc_pc_repository_pc_pc_EventGroup_Interface, gen_pcm_pc_pc_repository_pc_pc_EventType_Signature, gen_pcm_pc_pc_repository_pc_pc_Signature_Entity, gen_pcm_pc_pc_repository_pc_pc_InfrastructureSignature_Signature, gen_pcm_pc_pc_repository_pc_pc_InfrastructureInterface_Interface, gen_pcm_pc_pc_repository_pc_pc_OperationSignature_Signature, gen_pcm_pc_pc_repository_pc_pc_OperationInterface_Interface, gen_pcm_pc_pc_repository_pc_pc_OperationRequiredRole_RequiredRole, gen_pcm_pc_pc_repository_pc_pc_SourceRole_RequiredRole, gen_pcm_pc_pc_repository_pc_pc_InfrastructureRequiredRole_RequiredRole, gen_pcm_pc_pc_repository_pc_pc_RequiredRole_Role, gen_pcm_pc_pc_repository_pc_pc_OperationProvidedRole_ProvidedRole, gen_pcm_pc_pc_repository_pc_pc_InfrastructureProvidedRole_ProvidedRole, gen_pcm_pc_pc_repository_pc_pc_CompleteComponentType_RepositoryComponent, gen_pcm_pc_pc_repository_pc_pc_ProvidesComponentType_RepositoryComponent, gen_pcm_pc_pc_repository_pc_pc_SinkRole_ProvidedRole, gen_pcm_pc_pc_repository_pc_pc_PrimitiveDataType_DataType, gen_pcm_pc_pc_repository_pc_pc_CollectionDataType_entity_pc_pc_Entity, gen_pcm_pc_pc_repository_pc_pc_CollectionDataType_repository_pc_pc_DataType, gen_pcm_pc_pc_repository_pc_pc_CompositeDataType_entity_pc_pc_Entity, gen_pcm_pc_pc_repository_pc_pc_CompositeDataType_repository_pc_pc_DataType, gen_pcm_pc_pc_repository_pc_pc_CompositeComponent_entity_pc_pc_ComposedProvidingRequiringEntity, gen_pcm_pc_pc_repository_pc_pc_CompositeComponent_repository_pc_pc_ImplementationComponentType, gen_pcm_pc_pc_repository_pc_pc_InnerDeclaration_NamedElement, gen_pcm_pc_pc_repository_pc_pc_Role_Entity, gen_pcm_pc_pc_resourcetype_pc_pc_ResourceSignature_Entity, gen_pcm_pc_pc_resourcetype_pc_pc_ProcessingResourceType_ResourceType, gen_pcm_pc_pc_resourcetype_pc_pc_ResourceType_entity_pc_pc_Entity, gen_pcm_pc_pc_resourcetype_pc_pc_ResourceType_UnitCarryingElement, gen_pcm_pc_pc_resourcetype_pc_pc_ResourceType_entity_pc_pc_ResourceInterfaceProvidingEntity, gen_pcm_pc_pc_resourcetype_pc_pc_SchedulingPolicy_Entity, gen_pcm_pc_pc_resourcetype_pc_pc_CommunicationLinkResourceType_ResourceType, gen_pcm_pc_pc_resourcetype_pc_pc_ResourceInterface_Entity, gen_pcm_pc_pc_reliability_pc_pc_HardwareInducedFailureType_FailureType, gen_pcm_pc_pc_parameter_pc_pc_CharacterisedVariable_Variable, gen_pcm_pc_pc_reliability_pc_pc_InternalFailureOccurrenceDescription_FailureOccurrenceDescription, gen_pcm_pc_pc_reliability_pc_pc_NetworkInducedFailureType_FailureType, gen_pcm_pc_pc_reliability_pc_pc_ExternalFailureOccurrenceDescription_FailureOccurrenceDescription, gen_pcm_pc_pc_reliability_pc_pc_SoftwareInducedFailureType_FailureType, gen_pcm_pc_pc_reliability_pc_pc_ResourceTimeoutFailureType_SoftwareInducedFailureType, gen_pcm_pc_pc_reliability_pc_pc_FailureType_Entity, gen_pcm_pc_pc_seff_pc_pc_StopAction_AbstractInternalControlFlowAction, gen_pcm_pc_pc_seff_pc_pc_AbstractInternalControlFlowAction_AbstractAction, gen_pcm_pc_pc_seff_pc_pc_AbstractAction_Entity, gen_pcm_pc_pc_seff_pc_pc_AbstractLoopAction_AbstractInternalControlFlowAction, gen_pcm_pc_pc_seff_pc_pc_AbstractBranchTransition_Entity, gen_pcm_pc_pc_seff_pc_pc_ResourceDemandingBehaviour_Identifier, gen_pcm_pc_pc_seff_pc_pc_StartAction_AbstractInternalControlFlowAction, gen_pcm_pc_pc_seff_pc_pc_BranchAction_AbstractInternalControlFlowAction, gen_pcm_pc_pc_seff_pc_pc_ResourceDemandingInternalBehaviour_ResourceDemandingBehaviour, gen_pcm_pc_pc_seff_pc_pc_ReleaseAction_AbstractInternalControlFlowAction, gen_pcm_pc_pc_seff_pc_pc_LoopAction_AbstractLoopAction, gen_pcm_pc_pc_seff_pc_pc_ForkAction_AbstractInternalControlFlowAction, gen_pcm_pc_pc_seff_pc_pc_ForkedBehaviour_ResourceDemandingBehaviour, gen_pcm_pc_pc_seff_pc_pc_ResourceDemandingSEFF_Identifier, gen_pcm_pc_pc_seff_pc_pc_ResourceDemandingSEFF_seff_pc_pc_ServiceEffectSpecification, gen_pcm_pc_pc_seff_pc_pc_ResourceDemandingSEFF_seff_pc_pc_ResourceDemandingBehaviour, gen_pcm_pc_pc_seff_pc_pc_ExternalCallAction_seff_pc_pc_CallReturnAction, gen_pcm_pc_pc_seff_pc_pc_ExternalCallAction_seff_reliability_pc_pc_FailureHandlingEntity, gen_pcm_pc_pc_seff_pc_pc_CallReturnAction_CallAction, gen_pcm_pc_pc_seff_pc_pc_ExternalCallAction_seff_pc_pc_AbstractAction, gen_pcm_pc_pc_seff_pc_pc_CollectionIteratorAction_AbstractLoopAction, gen_pcm_pc_pc_seff_pc_pc_GuardedBranchTransition_AbstractBranchTransition, gen_pcm_pc_pc_seff_pc_pc_SetVariableAction_AbstractInternalControlFlowAction, gen_pcm_pc_pc_seff_pc_pc_InternalCallAction_seff_pc_pc_CallAction, gen_pcm_pc_pc_seff_pc_pc_InternalCallAction_seff_pc_pc_AbstractInternalControlFlowAction, gen_pcm_pc_pc_seff_pc_pc_EmitEventAction_seff_pc_pc_AbstractAction, gen_pcm_pc_pc_seff_pc_pc_EmitEventAction_seff_pc_pc_CallAction, gen_pcm_pc_pc_seff_pc_pc_ProbabilisticBranchTransition_AbstractBranchTransition, gen_pcm_pc_pc_seff_pc_pc_AcquireAction_AbstractInternalControlFlowAction, gen_pcm_pc_pc_seff_performance_pc_pc_InfrastructureCall_CallAction, gen_pcm_pc_pc_seff_pc_pc_InternalAction_AbstractInternalControlFlowAction, gen_pcm_pc_pc_seff_reliability_pc_pc_RecoveryActionBehaviour_seff_reliability_pc_pc_FailureHandlingEntity, gen_pcm_pc_pc_seff_reliability_pc_pc_RecoveryActionBehaviour_seff_pc_pc_ResourceDemandingBehaviour, gen_pcm_pc_pc_seff_performance_pc_pc_ResourceCall_CallAction, gen_pcm_pc_pc_seff_reliability_pc_pc_RecoveryAction_AbstractInternalControlFlowAction, gen_pcm_pc_pc_seff_reliability_pc_pc_FailureHandlingEntity_Entity, gen_pcm_pc_pc_qos_performance_pc_pc_SystemSpecifiedExecutionTime_SpecifiedExecutionTime, gen_pcm_pc_pc_qos_performance_pc_pc_SpecifiedExecutionTime_SpecifiedQoSAnnotation, gen_pcm_pc_pc_qosannotations_pc_pc_QoSAnnotations_Entity, gen_pcm_pc_pc_system_pc_pc_System_entity_pc_pc_Entity, gen_pcm_pc_pc_system_pc_pc_System_entity_pc_pc_ComposedProvidingRequiringEntity, gen_pcm_pc_pc_qos_performance_pc_pc_ComponentSpecifiedExecutionTime_SpecifiedExecutionTime, gen_pcm_pc_pc_qos_reliability_pc_pc_SpecifiedReliabilityAnnotation_SpecifiedQoSAnnotation, gen_pcm_pc_pc_resourceenvironment_pc_pc_ResourceContainer_Entity, gen_pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification_Identifier, gen_pcm_pc_pc_resourceenvironment_pc_pc_ResourceEnvironment_NamedElement, gen_pcm_pc_pc_resourceenvironment_pc_pc_LinkingResource_Entity, gen_pcm_pc_pc_allocation_pc_pc_AllocationContext_Entity, gen_pcm_pc_pc_resourceenvironment_pc_pc_CommunicationLinkResourceSpecification_Identifier, gen_pcm_pc_pc_allocation_pc_pc_Allocation_Entity, gen_pcm_pc_pc_subsystem_pc_pc_SubSystem_entity_pc_pc_ComposedProvidingRequiringEntity, gen_pcm_pc_pc_subsystem_pc_pc_SubSystem_repository_pc_pc_RepositoryComponent, gen_pcm_pc_pc_completions_pc_pc_Completion_entity_pc_pc_ComposedProvidingRequiringEntity, gen_pcm_pc_pc_completions_pc_pc_Completion_repository_pc_pc_ImplementationComponentType, gen_pcm_pc_pc_completions_pc_pc_DelegatingExternalCallAction_ExternalCallAction, gen_pcm_pc_pc_completions_pc_pc_NetworkDemandParametricResourceDemand_ParametricResourceDemand},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)