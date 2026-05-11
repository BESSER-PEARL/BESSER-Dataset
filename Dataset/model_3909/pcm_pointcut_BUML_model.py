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
pcm_pc_DummyClass = Class(name="pcm_pc_DummyClass")
pcm_pc_Pointcut = Class(name="pcm_pc_Pointcut")
pcm_pc_EObject = Class(name="pcm_pc_EObject")
pcm_pc_core_pc_PCMRandomVariable = Class(name="pcm_pc_core_pc_PCMRandomVariable")
RandomVariable = Class(name="RandomVariable")
VariableCharacterisation = Class(name="VariableCharacterisation")
seff_performance_pc_InfrastructureCall = Class(name="seff_performance_pc_InfrastructureCall")
seff_performance_pc_ResourceCall = Class(name="seff_performance_pc_ResourceCall")
seff_performance_pc_ParametricResourceDemand = Class(name="seff_performance_pc_ParametricResourceDemand")
LoopAction = Class(name="LoopAction")
GuardedBranchTransition = Class(name="GuardedBranchTransition")
qos_performance_pc_SpecifiedExecutionTime = Class(name="qos_performance_pc_SpecifiedExecutionTime")
composition_pc_EventChannelSinkConnector = Class(name="composition_pc_EventChannelSinkConnector")
ClosedWorkload = Class(name="ClosedWorkload")
PassiveResource = Class(name="PassiveResource")
CommunicationLinkResourceSpecification = Class(name="CommunicationLinkResourceSpecification")
ProcessingResourceSpecification = Class(name="ProcessingResourceSpecification")
pcm_pc_entity_pc_ResourceProvidedRole = Class(name="pcm_pc_entity_pc_ResourceProvidedRole")
Role = Class(name="Role")
entity_pc_ResourceInterfaceProvidingEntity = Class(name="entity_pc_ResourceInterfaceProvidingEntity")
ResourceInterface = Class(name="ResourceInterface")
pcm_pc_entity_pc_InterfaceProvidingRequiringEntity = Class(name="pcm_pc_entity_pc_InterfaceProvidingRequiringEntity")
entity_pc_InterfaceProvidingEntity = Class(name="entity_pc_InterfaceProvidingEntity")
entity_pc_InterfaceRequiringEntity = Class(name="entity_pc_InterfaceRequiringEntity")
composition_pc_AssemblyEventConnector = Class(name="composition_pc_AssemblyEventConnector")
pcm_pc_entity_pc_InterfaceProvidingEntity = Class(name="pcm_pc_entity_pc_InterfaceProvidingEntity")
Loop = Class(name="Loop")
Entity = Class(name="Entity")
OpenWorkload = Class(name="OpenWorkload")
ProvidedRole = Class(name="ProvidedRole")
pcm_pc_entity_pc_InterfaceRequiringEntity = Class(name="pcm_pc_entity_pc_InterfaceRequiringEntity")
Delay = Class(name="Delay")
RequiredRole = Class(name="RequiredRole")
pcm_pc_entity_pc_ResourceInterfaceRequiringEntity = Class(name="pcm_pc_entity_pc_ResourceInterfaceRequiringEntity")
entity_pc_ResourceRequiredRole = Class(name="entity_pc_ResourceRequiredRole")
pcm_pc_entity_pc_ResourceRequiredRole = Class(name="pcm_pc_entity_pc_ResourceRequiredRole")
pcm_pc_entity_pc_ResourceInterfaceProvidingEntity = Class(name="pcm_pc_entity_pc_ResourceInterfaceProvidingEntity")
entity_pc_ResourceProvidedRole = Class(name="entity_pc_ResourceProvidedRole")
entity_pc_Entity = Class(name="entity_pc_Entity")
entity_pc_ResourceInterfaceRequiringEntity = Class(name="entity_pc_ResourceInterfaceRequiringEntity")
pcm_pc_entity_pc_NamedElement = Class(name="pcm_pc_entity_pc_NamedElement")
pcm_pc_entity_pc_ResourceInterfaceProvidingRequiringEntity = Class(name="pcm_pc_entity_pc_ResourceInterfaceProvidingRequiringEntity")
pcm_pc_entity_pc_Entity = Class(name="pcm_pc_entity_pc_Entity")
Identifier = Class(name="Identifier")
entity_pc_NamedElement = Class(name="entity_pc_NamedElement")
pcm_pc_composition_pc_DelegationConnector = Class(name="pcm_pc_composition_pc_DelegationConnector")
Connector = Class(name="Connector")
pcm_pc_composition_pc_Connector = Class(name="pcm_pc_composition_pc_Connector")
pcm_pc_composition_pc_ComposedStructure = Class(name="pcm_pc_composition_pc_ComposedStructure")
pcm_pc_entity_pc_ComposedProvidingRequiringEntity = Class(name="pcm_pc_entity_pc_ComposedProvidingRequiringEntity")
composition_pc_ComposedStructure = Class(name="composition_pc_ComposedStructure")
entity_pc_InterfaceProvidingRequiringEntity = Class(name="entity_pc_InterfaceProvidingRequiringEntity")
composition_pc_AssemblyContext = Class(name="composition_pc_AssemblyContext")
composition_pc_ResourceRequiredDelegationConnector = Class(name="composition_pc_ResourceRequiredDelegationConnector")
composition_pc_EventChannel = Class(name="composition_pc_EventChannel")
composition_pc_Connector = Class(name="composition_pc_Connector")
EventGroup = Class(name="EventGroup")
composition_pc_EventChannelSourceConnector = Class(name="composition_pc_EventChannelSourceConnector")
pcm_pc_composition_pc_EventChannelSourceConnector = Class(name="pcm_pc_composition_pc_EventChannelSourceConnector")
SourceRole = Class(name="SourceRole")
pcm_pc_composition_pc_EventChannelSinkConnector = Class(name="pcm_pc_composition_pc_EventChannelSinkConnector")
SinkRole = Class(name="SinkRole")
PCMRandomVariable = Class(name="PCMRandomVariable")
pcm_pc_composition_pc_ProvidedDelegationConnector = Class(name="pcm_pc_composition_pc_ProvidedDelegationConnector")
DelegationConnector = Class(name="DelegationConnector")
pcm_pc_composition_pc_ResourceRequiredDelegationConnector = Class(name="pcm_pc_composition_pc_ResourceRequiredDelegationConnector")
pcm_pc_composition_pc_EventChannel = Class(name="pcm_pc_composition_pc_EventChannel")
OperationProvidedRole = Class(name="OperationProvidedRole")
pcm_pc_composition_pc_RequiredDelegationConnector = Class(name="pcm_pc_composition_pc_RequiredDelegationConnector")
OperationRequiredRole = Class(name="OperationRequiredRole")
pcm_pc_composition_pc_AssemblyEventConnector = Class(name="pcm_pc_composition_pc_AssemblyEventConnector")
pcm_pc_composition_pc_AssemblyConnector = Class(name="pcm_pc_composition_pc_AssemblyConnector")
pcm_pc_composition_pc_SourceDelegationConnector = Class(name="pcm_pc_composition_pc_SourceDelegationConnector")
pcm_pc_composition_pc_SinkDelegationConnector = Class(name="pcm_pc_composition_pc_SinkDelegationConnector")
pcm_pc_composition_pc_AssemblyInfrastructureConnector = Class(name="pcm_pc_composition_pc_AssemblyInfrastructureConnector")
InfrastructureProvidedRole = Class(name="InfrastructureProvidedRole")
InfrastructureRequiredRole = Class(name="InfrastructureRequiredRole")
pcm_pc_composition_pc_ProvidedInfrastructureDelegationConnector = Class(name="pcm_pc_composition_pc_ProvidedInfrastructureDelegationConnector")
pcm_pc_composition_pc_RequiredResourceDelegationConnector = Class(name="pcm_pc_composition_pc_RequiredResourceDelegationConnector")
pcm_pc_composition_pc_AssemblyContext = Class(name="pcm_pc_composition_pc_AssemblyContext")
RepositoryComponent = Class(name="RepositoryComponent")
VariableUsage = Class(name="VariableUsage")
pcm_pc_usagemodel_pc_Workload = Class(name="pcm_pc_usagemodel_pc_Workload")
UsageScenario = Class(name="UsageScenario")
pcm_pc_usagemodel_pc_UsageScenario = Class(name="pcm_pc_usagemodel_pc_UsageScenario")
UsageModel = Class(name="UsageModel")
ScenarioBehaviour = Class(name="ScenarioBehaviour")
Workload = Class(name="Workload")
pcm_pc_usagemodel_pc_UserData = Class(name="pcm_pc_usagemodel_pc_UserData")
pcm_pc_composition_pc_RequiredInfrastructureDelegationConnector = Class(name="pcm_pc_composition_pc_RequiredInfrastructureDelegationConnector")
UserData = Class(name="UserData")
pcm_pc_usagemodel_pc_UsageModel = Class(name="pcm_pc_usagemodel_pc_UsageModel")
OperationSignature = Class(name="OperationSignature")
pcm_pc_usagemodel_pc_AbstractUserAction = Class(name="pcm_pc_usagemodel_pc_AbstractUserAction")
pcm_pc_usagemodel_pc_EntryLevelSystemCall = Class(name="pcm_pc_usagemodel_pc_EntryLevelSystemCall")
AbstractUserAction = Class(name="AbstractUserAction")
pcm_pc_usagemodel_pc_ScenarioBehaviour = Class(name="pcm_pc_usagemodel_pc_ScenarioBehaviour")
BranchTransition = Class(name="BranchTransition")
pcm_pc_usagemodel_pc_BranchTransition = Class(name="pcm_pc_usagemodel_pc_BranchTransition")
pcm_pc_usagemodel_pc_Loop = Class(name="pcm_pc_usagemodel_pc_Loop")
pcm_pc_usagemodel_pc_Stop = Class(name="pcm_pc_usagemodel_pc_Stop")
pcm_pc_usagemodel_pc_Start = Class(name="pcm_pc_usagemodel_pc_Start")
Branch = Class(name="Branch")
pcm_pc_usagemodel_pc_Branch = Class(name="pcm_pc_usagemodel_pc_Branch")
pcm_pc_usagemodel_pc_Delay = Class(name="pcm_pc_usagemodel_pc_Delay")
pcm_pc_usagemodel_pc_ClosedWorkload = Class(name="pcm_pc_usagemodel_pc_ClosedWorkload")
pcm_pc_repository_pc_PassiveResource = Class(name="pcm_pc_repository_pc_PassiveResource")
pcm_pc_usagemodel_pc_OpenWorkload = Class(name="pcm_pc_usagemodel_pc_OpenWorkload")
ResourceTimeoutFailureType = Class(name="ResourceTimeoutFailureType")
pcm_pc_repository_pc_BasicComponent = Class(name="pcm_pc_repository_pc_BasicComponent")
ImplementationComponentType = Class(name="ImplementationComponentType")
ServiceEffectSpecification = Class(name="ServiceEffectSpecification")
pcm_pc_repository_pc_ImplementationComponentType = Class(name="pcm_pc_repository_pc_ImplementationComponentType")
BasicComponent = Class(name="BasicComponent")
CompleteComponentType = Class(name="CompleteComponentType")
pcm_pc_repository_pc_RepositoryComponent = Class(name="pcm_pc_repository_pc_RepositoryComponent")
InterfaceProvidingRequiringEntity = Class(name="InterfaceProvidingRequiringEntity")
Repository = Class(name="Repository")
pcm_pc_repository_pc_ProvidedRole = Class(name="pcm_pc_repository_pc_ProvidedRole")
pcm_pc_repository_pc_Parameter = Class(name="pcm_pc_repository_pc_Parameter")
DataType = Class(name="DataType")
EventType = Class(name="EventType")
ResourceSignature = Class(name="ResourceSignature")
pcm_pc_repository_pc_DataType = Class(name="pcm_pc_repository_pc_DataType")
pcm_pc_repository_pc_Repository = Class(name="pcm_pc_repository_pc_Repository")
Interface = Class(name="Interface")
FailureType = Class(name="FailureType")
pcm_pc_repository_pc_Interface = Class(name="pcm_pc_repository_pc_Interface")
InfrastructureSignature = Class(name="InfrastructureSignature")
Protocol = Class(name="Protocol")
RequiredCharacterisation = Class(name="RequiredCharacterisation")
pcm_pc_repository_pc_RequiredCharacterisation = Class(name="pcm_pc_repository_pc_RequiredCharacterisation")
Parameter_ = Class(name="Parameter")
pcm_pc_repository_pc_EventGroup = Class(name="pcm_pc_repository_pc_EventGroup")
pcm_pc_repository_pc_EventType = Class(name="pcm_pc_repository_pc_EventType")
Signature = Class(name="Signature")
pcm_pc_repository_pc_Signature = Class(name="pcm_pc_repository_pc_Signature")
ExceptionType = Class(name="ExceptionType")
pcm_pc_repository_pc_InfrastructureSignature = Class(name="pcm_pc_repository_pc_InfrastructureSignature")
InfrastructureInterface = Class(name="InfrastructureInterface")
pcm_pc_repository_pc_InfrastructureInterface = Class(name="pcm_pc_repository_pc_InfrastructureInterface")
pcm_pc_repository_pc_InfrastructureRequiredRole = Class(name="pcm_pc_repository_pc_InfrastructureRequiredRole")
pcm_pc_repository_pc_RequiredRole = Class(name="pcm_pc_repository_pc_RequiredRole")
pcm_pc_repository_pc_OperationSignature = Class(name="pcm_pc_repository_pc_OperationSignature")
OperationInterface = Class(name="OperationInterface")
pcm_pc_repository_pc_ExceptionType = Class(name="pcm_pc_repository_pc_ExceptionType")
pcm_pc_repository_pc_OperationInterface = Class(name="pcm_pc_repository_pc_OperationInterface")
pcm_pc_repository_pc_OperationRequiredRole = Class(name="pcm_pc_repository_pc_OperationRequiredRole")
pcm_pc_repository_pc_SourceRole = Class(name="pcm_pc_repository_pc_SourceRole")
pcm_pc_repository_pc_SinkRole = Class(name="pcm_pc_repository_pc_SinkRole")
pcm_pc_repository_pc_InfrastructureProvidedRole = Class(name="pcm_pc_repository_pc_InfrastructureProvidedRole")
pcm_pc_repository_pc_CompleteComponentType = Class(name="pcm_pc_repository_pc_CompleteComponentType")
ProvidesComponentType = Class(name="ProvidesComponentType")
pcm_pc_repository_pc_ProvidesComponentType = Class(name="pcm_pc_repository_pc_ProvidesComponentType")
pcm_pc_repository_pc_OperationProvidedRole = Class(name="pcm_pc_repository_pc_OperationProvidedRole")
pcm_pc_repository_pc_CompositeComponent = Class(name="pcm_pc_repository_pc_CompositeComponent")
entity_pc_ComposedProvidingRequiringEntity = Class(name="entity_pc_ComposedProvidingRequiringEntity")
repository_pc_ImplementationComponentType = Class(name="repository_pc_ImplementationComponentType")
pcm_pc_repository_pc_PrimitiveDataType = Class(name="pcm_pc_repository_pc_PrimitiveDataType")
pcm_pc_repository_pc_CollectionDataType = Class(name="pcm_pc_repository_pc_CollectionDataType")
repository_pc_DataType = Class(name="repository_pc_DataType")
pcm_pc_repository_pc_CompositeDataType = Class(name="pcm_pc_repository_pc_CompositeDataType")
CompositeDataType = Class(name="CompositeDataType")
pcm_pc_repository_pc_Role = Class(name="pcm_pc_repository_pc_Role")
pcm_pc_resourcetype_pc_ResourceSignature = Class(name="pcm_pc_resourcetype_pc_ResourceSignature")
pcm_pc_resourcetype_pc_ProcessingResourceType = Class(name="pcm_pc_resourcetype_pc_ProcessingResourceType")
ResourceType = Class(name="ResourceType")
HardwareInducedFailureType = Class(name="HardwareInducedFailureType")
pcm_pc_resourcetype_pc_ResourceType = Class(name="pcm_pc_resourcetype_pc_ResourceType")
UnitCarryingElement = Class(name="UnitCarryingElement")
ResourceRepository = Class(name="ResourceRepository")
pcm_pc_resourcetype_pc_ResourceRepository = Class(name="pcm_pc_resourcetype_pc_ResourceRepository")
SchedulingPolicy = Class(name="SchedulingPolicy")
pcm_pc_resourcetype_pc_SchedulingPolicy = Class(name="pcm_pc_resourcetype_pc_SchedulingPolicy")
InnerDeclaration = Class(name="InnerDeclaration")
pcm_pc_repository_pc_InnerDeclaration = Class(name="pcm_pc_repository_pc_InnerDeclaration")
NamedElement = Class(name="NamedElement")
pcm_pc_protocol_pc_Protocol = Class(name="pcm_pc_protocol_pc_Protocol")
pcm_pc_parameter_pc_VariableUsage = Class(name="pcm_pc_parameter_pc_VariableUsage")
CallAction = Class(name="CallAction")
SynchronisationPoint = Class(name="SynchronisationPoint")
CallReturnAction = Class(name="CallReturnAction")
SetVariableAction = Class(name="SetVariableAction")
SpecifiedOutputParameterAbstraction = Class(name="SpecifiedOutputParameterAbstraction")
EntryLevelSystemCall = Class(name="EntryLevelSystemCall")
parameter_pc_pcm_pc_AbstractNamedReference = Class(name="parameter_pc_pcm_pc_AbstractNamedReference")
pcm_pc_parameter_pc_VariableCharacterisation = Class(name="pcm_pc_parameter_pc_VariableCharacterisation")
pcm_pc_resourcetype_pc_CommunicationLinkResourceType = Class(name="pcm_pc_resourcetype_pc_CommunicationLinkResourceType")
NetworkInducedFailureType = Class(name="NetworkInducedFailureType")
pcm_pc_resourcetype_pc_ResourceInterface = Class(name="pcm_pc_resourcetype_pc_ResourceInterface")
pcm_pc_parameter_pc_CharacterisedVariable = Class(name="pcm_pc_parameter_pc_CharacterisedVariable")
Variable = Class(name="Variable")
pcm_pc_reliability_pc_FailureOccurrenceDescription = Class(name="pcm_pc_reliability_pc_FailureOccurrenceDescription")
pcm_pc_reliability_pc_HardwareInducedFailureType = Class(name="pcm_pc_reliability_pc_HardwareInducedFailureType")
ProcessingResourceType = Class(name="ProcessingResourceType")
InternalFailureOccurrenceDescription = Class(name="InternalFailureOccurrenceDescription")
pcm_pc_reliability_pc_InternalFailureOccurrenceDescription = Class(name="pcm_pc_reliability_pc_InternalFailureOccurrenceDescription")
FailureOccurrenceDescription = Class(name="FailureOccurrenceDescription")
InternalAction = Class(name="InternalAction")
SoftwareInducedFailureType = Class(name="SoftwareInducedFailureType")
pcm_pc_reliability_pc_NetworkInducedFailureType = Class(name="pcm_pc_reliability_pc_NetworkInducedFailureType")
CommunicationLinkResourceType = Class(name="CommunicationLinkResourceType")
pcm_pc_reliability_pc_ExternalFailureOccurrenceDescription = Class(name="pcm_pc_reliability_pc_ExternalFailureOccurrenceDescription")
qos_reliability_pc_SpecifiedReliabilityAnnotation = Class(name="qos_reliability_pc_SpecifiedReliabilityAnnotation")
pcm_pc_reliability_pc_SoftwareInducedFailureType = Class(name="pcm_pc_reliability_pc_SoftwareInducedFailureType")
pcm_pc_reliability_pc_FailureType = Class(name="pcm_pc_reliability_pc_FailureType")
pcm_pc_seff_pc_StopAction = Class(name="pcm_pc_seff_pc_StopAction")
AbstractInternalControlFlowAction = Class(name="AbstractInternalControlFlowAction")
pcm_pc_seff_pc_AbstractInternalControlFlowAction = Class(name="pcm_pc_seff_pc_AbstractInternalControlFlowAction")
AbstractAction = Class(name="AbstractAction")
pcm_pc_seff_pc_AbstractAction = Class(name="pcm_pc_seff_pc_AbstractAction")
ResourceDemandingBehaviour = Class(name="ResourceDemandingBehaviour")
pcm_pc_reliability_pc_ResourceTimeoutFailureType = Class(name="pcm_pc_reliability_pc_ResourceTimeoutFailureType")
AbstractLoopAction = Class(name="AbstractLoopAction")
AbstractBranchTransition = Class(name="AbstractBranchTransition")
pcm_pc_seff_pc_AbstractLoopAction = Class(name="pcm_pc_seff_pc_AbstractLoopAction")
pcm_pc_seff_pc_AbstractBranchTransition = Class(name="pcm_pc_seff_pc_AbstractBranchTransition")
pcm_pc_seff_pc_ResourceDemandingBehaviour = Class(name="pcm_pc_seff_pc_ResourceDemandingBehaviour")
BranchAction = Class(name="BranchAction")
pcm_pc_seff_pc_BranchAction = Class(name="pcm_pc_seff_pc_BranchAction")
pcm_pc_seff_pc_CallAction = Class(name="pcm_pc_seff_pc_CallAction")
pcm_pc_seff_pc_StartAction = Class(name="pcm_pc_seff_pc_StartAction")
pcm_pc_seff_pc_ServiceEffectSpecification = Class(name="pcm_pc_seff_pc_ServiceEffectSpecification")
pcm_pc_seff_pc_ResourceDemandingSEFF = Class(name="pcm_pc_seff_pc_ResourceDemandingSEFF")
ResourceDemandingInternalBehaviour = Class(name="ResourceDemandingInternalBehaviour")
pcm_pc_seff_pc_ResourceDemandingInternalBehaviour = Class(name="pcm_pc_seff_pc_ResourceDemandingInternalBehaviour")
ResourceDemandingSEFF = Class(name="ResourceDemandingSEFF")
pcm_pc_seff_pc_ReleaseAction = Class(name="pcm_pc_seff_pc_ReleaseAction")
pcm_pc_seff_pc_LoopAction = Class(name="pcm_pc_seff_pc_LoopAction")
pcm_pc_seff_pc_ForkAction = Class(name="pcm_pc_seff_pc_ForkAction")
ForkedBehaviour = Class(name="ForkedBehaviour")
pcm_pc_seff_pc_ForkedBehaviour = Class(name="pcm_pc_seff_pc_ForkedBehaviour")
pcm_pc_seff_pc_CallReturnAction = Class(name="pcm_pc_seff_pc_CallReturnAction")
seff_pc_ServiceEffectSpecification = Class(name="seff_pc_ServiceEffectSpecification")
seff_pc_ResourceDemandingBehaviour = Class(name="seff_pc_ResourceDemandingBehaviour")
pcm_pc_seff_pc_ProbabilisticBranchTransition = Class(name="pcm_pc_seff_pc_ProbabilisticBranchTransition")
pcm_pc_seff_pc_AcquireAction = Class(name="pcm_pc_seff_pc_AcquireAction")
ForkAction = Class(name="ForkAction")
pcm_pc_seff_pc_SynchronisationPoint = Class(name="pcm_pc_seff_pc_SynchronisationPoint")
pcm_pc_seff_pc_ExternalCallAction = Class(name="pcm_pc_seff_pc_ExternalCallAction")
seff_pc_AbstractAction = Class(name="seff_pc_AbstractAction")
seff_pc_CallReturnAction = Class(name="seff_pc_CallReturnAction")
seff_reliability_pc_FailureHandlingEntity = Class(name="seff_reliability_pc_FailureHandlingEntity")
pcm_pc_seff_pc_SetVariableAction = Class(name="pcm_pc_seff_pc_SetVariableAction")
pcm_pc_seff_pc_InternalCallAction = Class(name="pcm_pc_seff_pc_InternalCallAction")
seff_pc_CallAction = Class(name="seff_pc_CallAction")
seff_pc_AbstractInternalControlFlowAction = Class(name="seff_pc_AbstractInternalControlFlowAction")
pcm_pc_seff_pc_EmitEventAction = Class(name="pcm_pc_seff_pc_EmitEventAction")
pcm_pc_seff_pc_InternalAction = Class(name="pcm_pc_seff_pc_InternalAction")
pcm_pc_seff_pc_CollectionIteratorAction = Class(name="pcm_pc_seff_pc_CollectionIteratorAction")
pcm_pc_seff_pc_GuardedBranchTransition = Class(name="pcm_pc_seff_pc_GuardedBranchTransition")
pcm_pc_seff_performance_pc_ResourceCall = Class(name="pcm_pc_seff_performance_pc_ResourceCall")
pcm_pc_seff_performance_pc_InfrastructureCall = Class(name="pcm_pc_seff_performance_pc_InfrastructureCall")
pcm_pc_seff_reliability_pc_RecoveryActionBehaviour = Class(name="pcm_pc_seff_reliability_pc_RecoveryActionBehaviour")
pcm_pc_seff_performance_pc_ParametricResourceDemand = Class(name="pcm_pc_seff_performance_pc_ParametricResourceDemand")
pcm_pc_seff_reliability_pc_FailureHandlingEntity = Class(name="pcm_pc_seff_reliability_pc_FailureHandlingEntity")
pcm_pc_qosannotations_pc_SpecifiedQoSAnnotation = Class(name="pcm_pc_qosannotations_pc_SpecifiedQoSAnnotation")
QoSAnnotations = Class(name="QoSAnnotations")
pcm_pc_qosannotations_pc_QoSAnnotations = Class(name="pcm_pc_qosannotations_pc_QoSAnnotations")
seff_reliability_pc_RecoveryActionBehaviour = Class(name="seff_reliability_pc_RecoveryActionBehaviour")
seff_reliability_pc_RecoveryAction = Class(name="seff_reliability_pc_RecoveryAction")
pcm_pc_seff_reliability_pc_RecoveryAction = Class(name="pcm_pc_seff_reliability_pc_RecoveryAction")
System = Class(name="System")
SpecifiedQoSAnnotation = Class(name="SpecifiedQoSAnnotation")
pcm_pc_qosannotations_pc_SpecifiedOutputParameterAbstraction = Class(name="pcm_pc_qosannotations_pc_SpecifiedOutputParameterAbstraction")
pcm_pc_qos_performance_pc_SystemSpecifiedExecutionTime = Class(name="pcm_pc_qos_performance_pc_SystemSpecifiedExecutionTime")
SpecifiedExecutionTime = Class(name="SpecifiedExecutionTime")
ExternalFailureOccurrenceDescription = Class(name="ExternalFailureOccurrenceDescription")
pcm_pc_system_pc_System = Class(name="pcm_pc_system_pc_System")
pcm_pc_qos_performance_pc_SpecifiedExecutionTime = Class(name="pcm_pc_qos_performance_pc_SpecifiedExecutionTime")
pcm_pc_qos_performance_pc_ComponentSpecifiedExecutionTime = Class(name="pcm_pc_qos_performance_pc_ComponentSpecifiedExecutionTime")
pcm_pc_qos_reliability_pc_SpecifiedReliabilityAnnotation = Class(name="pcm_pc_qos_reliability_pc_SpecifiedReliabilityAnnotation")
pcm_pc_resourceenvironment_pc_LinkingResource = Class(name="pcm_pc_resourceenvironment_pc_LinkingResource")
ResourceEnvironment = Class(name="ResourceEnvironment")
pcm_pc_resourceenvironment_pc_ResourceContainer = Class(name="pcm_pc_resourceenvironment_pc_ResourceContainer")
pcm_pc_resourceenvironment_pc_ProcessingResourceSpecification = Class(name="pcm_pc_resourceenvironment_pc_ProcessingResourceSpecification")
pcm_pc_resourceenvironment_pc_ResourceEnvironment = Class(name="pcm_pc_resourceenvironment_pc_ResourceEnvironment")
LinkingResource = Class(name="LinkingResource")
ResourceContainer = Class(name="ResourceContainer")
pcm_pc_allocation_pc_AllocationContext = Class(name="pcm_pc_allocation_pc_AllocationContext")
Allocation = Class(name="Allocation")
pcm_pc_allocation_pc_Allocation = Class(name="pcm_pc_allocation_pc_Allocation")
pcm_pc_resourceenvironment_pc_CommunicationLinkResourceSpecification = Class(name="pcm_pc_resourceenvironment_pc_CommunicationLinkResourceSpecification")
AllocationContext = Class(name="AllocationContext")
pcm_pc_subsystem_pc_SubSystem = Class(name="pcm_pc_subsystem_pc_SubSystem")
repository_pc_RepositoryComponent = Class(name="repository_pc_RepositoryComponent")
pcm_pc_completions_pc_Completion = Class(name="pcm_pc_completions_pc_Completion")
pcm_pc_completions_pc_CompletionRepository = Class(name="pcm_pc_completions_pc_CompletionRepository")
Completion = Class(name="Completion")
pcm_pc_completions_pc_DelegatingExternalCallAction = Class(name="pcm_pc_completions_pc_DelegatingExternalCallAction")
ExternalCallAction = Class(name="ExternalCallAction")
pcm_pc_completions_pc_NetworkDemandParametricResourceDemand = Class(name="pcm_pc_completions_pc_NetworkDemandParametricResourceDemand")
ParametricResourceDemand = Class(name="ParametricResourceDemand")

# pcm_pc_DummyClass class attributes and methods

# pcm_pc_Pointcut class attributes and methods

# pcm_pc_EObject class attributes and methods

# pcm_pc_core_pc_PCMRandomVariable class attributes and methods
pcm_pc_core_pc_PCMRandomVariable_m_SpecificationMustNotBeNULL: Method = Method(name="SpecificationMustNotBeNULL", parameters={Parameter(name='pcm_pc_context', type=StringType), Parameter(name='pcm_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_core_pc_PCMRandomVariable.methods={pcm_pc_core_pc_PCMRandomVariable_m_SpecificationMustNotBeNULL}

# RandomVariable class attributes and methods

# VariableCharacterisation class attributes and methods

# seff_performance_pc_InfrastructureCall class attributes and methods

# seff_performance_pc_ResourceCall class attributes and methods

# seff_performance_pc_ParametricResourceDemand class attributes and methods

# LoopAction class attributes and methods

# GuardedBranchTransition class attributes and methods

# qos_performance_pc_SpecifiedExecutionTime class attributes and methods

# composition_pc_EventChannelSinkConnector class attributes and methods

# ClosedWorkload class attributes and methods

# PassiveResource class attributes and methods

# CommunicationLinkResourceSpecification class attributes and methods

# ProcessingResourceSpecification class attributes and methods

# pcm_pc_entity_pc_ResourceProvidedRole class attributes and methods

# Role class attributes and methods

# entity_pc_ResourceInterfaceProvidingEntity class attributes and methods

# ResourceInterface class attributes and methods

# pcm_pc_entity_pc_InterfaceProvidingRequiringEntity class attributes and methods

# entity_pc_InterfaceProvidingEntity class attributes and methods

# entity_pc_InterfaceRequiringEntity class attributes and methods

# composition_pc_AssemblyEventConnector class attributes and methods

# pcm_pc_entity_pc_InterfaceProvidingEntity class attributes and methods

# Loop class attributes and methods

# Entity class attributes and methods

# OpenWorkload class attributes and methods

# ProvidedRole class attributes and methods

# pcm_pc_entity_pc_InterfaceRequiringEntity class attributes and methods

# Delay class attributes and methods

# RequiredRole class attributes and methods

# pcm_pc_entity_pc_ResourceInterfaceRequiringEntity class attributes and methods

# entity_pc_ResourceRequiredRole class attributes and methods

# pcm_pc_entity_pc_ResourceRequiredRole class attributes and methods

# pcm_pc_entity_pc_ResourceInterfaceProvidingEntity class attributes and methods

# entity_pc_ResourceProvidedRole class attributes and methods

# entity_pc_Entity class attributes and methods

# entity_pc_ResourceInterfaceRequiringEntity class attributes and methods

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
pcm_pc_composition_pc_ComposedStructure_m_MultipleConnectorsConstraint: Method = Method(name="MultipleConnectorsConstraint", parameters={Parameter(name='pcm_pc_context', type=StringType), Parameter(name='pcm_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_composition_pc_ComposedStructure_m_MultipleConnectorsConstraintForAssemblyConnectors: Method = Method(name="MultipleConnectorsConstraintForAssemblyConnectors", parameters={Parameter(name='pcm_pc_context', type=StringType), Parameter(name='pcm_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_composition_pc_ComposedStructure.methods={pcm_pc_composition_pc_ComposedStructure_m_MultipleConnectorsConstraintForAssemblyConnectors, pcm_pc_composition_pc_ComposedStructure_m_MultipleConnectorsConstraint}

# pcm_pc_entity_pc_ComposedProvidingRequiringEntity class attributes and methods
pcm_pc_entity_pc_ComposedProvidingRequiringEntity_m_ProvidedRolesMustBeBound: Method = Method(name="ProvidedRolesMustBeBound", parameters={Parameter(name='pcm_pc_context', type=StringType), Parameter(name='pcm_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_entity_pc_ComposedProvidingRequiringEntity.methods={pcm_pc_entity_pc_ComposedProvidingRequiringEntity_m_ProvidedRolesMustBeBound}

# composition_pc_ComposedStructure class attributes and methods

# entity_pc_InterfaceProvidingRequiringEntity class attributes and methods

# composition_pc_AssemblyContext class attributes and methods

# composition_pc_ResourceRequiredDelegationConnector class attributes and methods

# composition_pc_EventChannel class attributes and methods

# composition_pc_Connector class attributes and methods

# EventGroup class attributes and methods

# composition_pc_EventChannelSourceConnector class attributes and methods

# pcm_pc_composition_pc_EventChannelSourceConnector class attributes and methods

# SourceRole class attributes and methods

# pcm_pc_composition_pc_EventChannelSinkConnector class attributes and methods

# SinkRole class attributes and methods

# PCMRandomVariable class attributes and methods

# pcm_pc_composition_pc_ProvidedDelegationConnector class attributes and methods
pcm_pc_composition_pc_ProvidedDelegationConnector_m_ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure: Method = Method(name="ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure", parameters={Parameter(name='pcm_pc_context', type=StringType), Parameter(name='pcm_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_composition_pc_ProvidedDelegationConnector_m_ComponentOfAssemblyContextAndInnerRoleProvidingComponentNeedToBeTheSame: Method = Method(name="ComponentOfAssemblyContextAndInnerRoleProvidingComponentNeedToBeTheSame", parameters={Parameter(name='pcm_pc_diagnostics', type=StringType), Parameter(name='pcm_pc_context', type=StringType)}, type=BooleanType)
pcm_pc_composition_pc_ProvidedDelegationConnector.methods={pcm_pc_composition_pc_ProvidedDelegationConnector_m_ComponentOfAssemblyContextAndInnerRoleProvidingComponentNeedToBeTheSame, pcm_pc_composition_pc_ProvidedDelegationConnector_m_ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure}

# DelegationConnector class attributes and methods

# pcm_pc_composition_pc_ResourceRequiredDelegationConnector class attributes and methods

# pcm_pc_composition_pc_EventChannel class attributes and methods

# OperationProvidedRole class attributes and methods

# pcm_pc_composition_pc_RequiredDelegationConnector class attributes and methods
pcm_pc_composition_pc_RequiredDelegationConnector_m_RequiredDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure: Method = Method(name="RequiredDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure", parameters={Parameter(name='pcm_pc_diagnostics', type=StringType), Parameter(name='pcm_pc_context', type=StringType)}, type=BooleanType)
pcm_pc_composition_pc_RequiredDelegationConnector_m_ComponentOfAssemblyContextAndInnerRoleRequiringComponentNeedToBeTheSame: Method = Method(name="ComponentOfAssemblyContextAndInnerRoleRequiringComponentNeedToBeTheSame", parameters={Parameter(name='pcm_pc_context', type=StringType), Parameter(name='pcm_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_composition_pc_RequiredDelegationConnector_m_RequiringEntityOfOuterRequiredRoleMustBeTheSameAsTheParentOfTheRequiredDelegationConnector: Method = Method(name="RequiringEntityOfOuterRequiredRoleMustBeTheSameAsTheParentOfTheRequiredDelegationConnector", parameters={Parameter(name='pcm_pc_diagnostics', type=StringType), Parameter(name='pcm_pc_context', type=StringType)}, type=BooleanType)
pcm_pc_composition_pc_RequiredDelegationConnector.methods={pcm_pc_composition_pc_RequiredDelegationConnector_m_ComponentOfAssemblyContextAndInnerRoleRequiringComponentNeedToBeTheSame, pcm_pc_composition_pc_RequiredDelegationConnector_m_RequiringEntityOfOuterRequiredRoleMustBeTheSameAsTheParentOfTheRequiredDelegationConnector, pcm_pc_composition_pc_RequiredDelegationConnector_m_RequiredDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure}

# OperationRequiredRole class attributes and methods

# pcm_pc_composition_pc_AssemblyEventConnector class attributes and methods

# pcm_pc_composition_pc_AssemblyConnector class attributes and methods
pcm_pc_composition_pc_AssemblyConnector_m_AssemblyConnectorsReferencedRequiredRoleAndChildContextMustMatch: Method = Method(name="AssemblyConnectorsReferencedRequiredRoleAndChildContextMustMatch", parameters={Parameter(name='pcm_pc_diagnostics', type=StringType), Parameter(name='pcm_pc_context', type=StringType)}, type=BooleanType)
pcm_pc_composition_pc_AssemblyConnector_m_AssemblyConnectorsReferencedInterfacesMustMatch: Method = Method(name="AssemblyConnectorsReferencedInterfacesMustMatch", parameters={Parameter(name='pcm_pc_diagnostics', type=StringType), Parameter(name='pcm_pc_context', type=StringType)}, type=BooleanType)
pcm_pc_composition_pc_AssemblyConnector_m_AssemblyConnectorsReferencedProvidedRolesAndChildContextMustMatch: Method = Method(name="AssemblyConnectorsReferencedProvidedRolesAndChildContextMustMatch", parameters={Parameter(name='pcm_pc_context', type=StringType), Parameter(name='pcm_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_composition_pc_AssemblyConnector.methods={pcm_pc_composition_pc_AssemblyConnector_m_AssemblyConnectorsReferencedProvidedRolesAndChildContextMustMatch, pcm_pc_composition_pc_AssemblyConnector_m_AssemblyConnectorsReferencedRequiredRoleAndChildContextMustMatch, pcm_pc_composition_pc_AssemblyConnector_m_AssemblyConnectorsReferencedInterfacesMustMatch}

# pcm_pc_composition_pc_SourceDelegationConnector class attributes and methods

# pcm_pc_composition_pc_SinkDelegationConnector class attributes and methods

# pcm_pc_composition_pc_AssemblyInfrastructureConnector class attributes and methods

# InfrastructureProvidedRole class attributes and methods

# InfrastructureRequiredRole class attributes and methods

# pcm_pc_composition_pc_ProvidedInfrastructureDelegationConnector class attributes and methods

# pcm_pc_composition_pc_RequiredResourceDelegationConnector class attributes and methods

# pcm_pc_composition_pc_AssemblyContext class attributes and methods

# RepositoryComponent class attributes and methods

# VariableUsage class attributes and methods

# pcm_pc_usagemodel_pc_Workload class attributes and methods

# UsageScenario class attributes and methods

# pcm_pc_usagemodel_pc_UsageScenario class attributes and methods

# UsageModel class attributes and methods

# ScenarioBehaviour class attributes and methods

# Workload class attributes and methods

# pcm_pc_usagemodel_pc_UserData class attributes and methods

# pcm_pc_composition_pc_RequiredInfrastructureDelegationConnector class attributes and methods

# UserData class attributes and methods

# pcm_pc_usagemodel_pc_UsageModel class attributes and methods

# OperationSignature class attributes and methods

# pcm_pc_usagemodel_pc_AbstractUserAction class attributes and methods

# pcm_pc_usagemodel_pc_EntryLevelSystemCall class attributes and methods
pcm_pc_usagemodel_pc_EntryLevelSystemCall_priority: Property = Property(name="priority", type=IntegerType)
pcm_pc_usagemodel_pc_EntryLevelSystemCall_m_EntryLevelSystemCallSignatureMustMatchItsProvidedRole: Method = Method(name="EntryLevelSystemCallSignatureMustMatchItsProvidedRole", parameters={Parameter(name='pcm_pc_diagnostics', type=StringType), Parameter(name='pcm_pc_context', type=StringType)}, type=BooleanType)
pcm_pc_usagemodel_pc_EntryLevelSystemCall_m_EntryLevelSystemCallMustReferenceProvidedRoleOfASystem: Method = Method(name="EntryLevelSystemCallMustReferenceProvidedRoleOfASystem", parameters={Parameter(name='pcm_pc_diagnostics', type=StringType), Parameter(name='pcm_pc_context', type=StringType)}, type=BooleanType)
pcm_pc_usagemodel_pc_EntryLevelSystemCall.attributes={pcm_pc_usagemodel_pc_EntryLevelSystemCall_priority}
pcm_pc_usagemodel_pc_EntryLevelSystemCall.methods={pcm_pc_usagemodel_pc_EntryLevelSystemCall_m_EntryLevelSystemCallSignatureMustMatchItsProvidedRole, pcm_pc_usagemodel_pc_EntryLevelSystemCall_m_EntryLevelSystemCallMustReferenceProvidedRoleOfASystem}

# AbstractUserAction class attributes and methods

# pcm_pc_usagemodel_pc_ScenarioBehaviour class attributes and methods
pcm_pc_usagemodel_pc_ScenarioBehaviour_m_Exactlyonestart: Method = Method(name="Exactlyonestart", parameters={Parameter(name='pcm_pc_diagnostics', type=StringType), Parameter(name='pcm_pc_context', type=StringType)}, type=BooleanType)
pcm_pc_usagemodel_pc_ScenarioBehaviour_m_Exactlyonestop: Method = Method(name="Exactlyonestop", parameters={Parameter(name='pcm_pc_context', type=StringType), Parameter(name='pcm_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_usagemodel_pc_ScenarioBehaviour_m_EachuseractionexceptStartandStopmusthaveapredecessorandsuccessor: Method = Method(name="EachuseractionexceptStartandStopmusthaveapredecessorandsuccessor", parameters={Parameter(name='pcm_pc_diagnostics', type=StringType), Parameter(name='pcm_pc_context', type=StringType)}, type=BooleanType)
pcm_pc_usagemodel_pc_ScenarioBehaviour.methods={pcm_pc_usagemodel_pc_ScenarioBehaviour_m_Exactlyonestart, pcm_pc_usagemodel_pc_ScenarioBehaviour_m_EachuseractionexceptStartandStopmusthaveapredecessorandsuccessor, pcm_pc_usagemodel_pc_ScenarioBehaviour_m_Exactlyonestop}

# BranchTransition class attributes and methods

# pcm_pc_usagemodel_pc_BranchTransition class attributes and methods
pcm_pc_usagemodel_pc_BranchTransition_branchProbability: Property = Property(name="branchProbability", type=FloatType)
pcm_pc_usagemodel_pc_BranchTransition.attributes={pcm_pc_usagemodel_pc_BranchTransition_branchProbability}

# pcm_pc_usagemodel_pc_Loop class attributes and methods

# pcm_pc_usagemodel_pc_Stop class attributes and methods
pcm_pc_usagemodel_pc_Stop_m_StopHasNoSuccessor: Method = Method(name="StopHasNoSuccessor", parameters={Parameter(name='pcm_pc_context', type=StringType), Parameter(name='pcm_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_usagemodel_pc_Stop.methods={pcm_pc_usagemodel_pc_Stop_m_StopHasNoSuccessor}

# pcm_pc_usagemodel_pc_Start class attributes and methods
pcm_pc_usagemodel_pc_Start_m_StartHasNoPredecessor: Method = Method(name="StartHasNoPredecessor", parameters={Parameter(name='pcm_pc_context', type=StringType), Parameter(name='pcm_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_usagemodel_pc_Start.methods={pcm_pc_usagemodel_pc_Start_m_StartHasNoPredecessor}

# Branch class attributes and methods

# pcm_pc_usagemodel_pc_Branch class attributes and methods
pcm_pc_usagemodel_pc_Branch_m_AllBranchProbabilitiesMustSumUpTo1: Method = Method(name="AllBranchProbabilitiesMustSumUpTo1", parameters={Parameter(name='pcm_pc_diagnostics', type=StringType), Parameter(name='pcm_pc_context', type=StringType)}, type=BooleanType)
pcm_pc_usagemodel_pc_Branch.methods={pcm_pc_usagemodel_pc_Branch_m_AllBranchProbabilitiesMustSumUpTo1}

# pcm_pc_usagemodel_pc_Delay class attributes and methods

# pcm_pc_usagemodel_pc_ClosedWorkload class attributes and methods
pcm_pc_usagemodel_pc_ClosedWorkload_population: Property = Property(name="population", type=IntegerType)
pcm_pc_usagemodel_pc_ClosedWorkload_m_PopulationInClosedWorkloadNeedsToBeSpecified: Method = Method(name="PopulationInClosedWorkloadNeedsToBeSpecified", parameters={Parameter(name='pcm_pc_diagnostics', type=StringType), Parameter(name='pcm_pc_context', type=StringType)}, type=BooleanType)
pcm_pc_usagemodel_pc_ClosedWorkload_m_ThinkTimeInClosedWorkloadNeedsToBeSpecified: Method = Method(name="ThinkTimeInClosedWorkloadNeedsToBeSpecified", parameters={Parameter(name='pcm_pc_context', type=StringType), Parameter(name='pcm_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_usagemodel_pc_ClosedWorkload.attributes={pcm_pc_usagemodel_pc_ClosedWorkload_population}
pcm_pc_usagemodel_pc_ClosedWorkload.methods={pcm_pc_usagemodel_pc_ClosedWorkload_m_PopulationInClosedWorkloadNeedsToBeSpecified, pcm_pc_usagemodel_pc_ClosedWorkload_m_ThinkTimeInClosedWorkloadNeedsToBeSpecified}

# pcm_pc_repository_pc_PassiveResource class attributes and methods

# pcm_pc_usagemodel_pc_OpenWorkload class attributes and methods
pcm_pc_usagemodel_pc_OpenWorkload_m_InterArrivalTimeInOpenWorkloadNeedsToBeSpecified: Method = Method(name="InterArrivalTimeInOpenWorkloadNeedsToBeSpecified", parameters={Parameter(name='pcm_pc_context', type=StringType), Parameter(name='pcm_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_usagemodel_pc_OpenWorkload.methods={pcm_pc_usagemodel_pc_OpenWorkload_m_InterArrivalTimeInOpenWorkloadNeedsToBeSpecified}

# ResourceTimeoutFailureType class attributes and methods

# pcm_pc_repository_pc_BasicComponent class attributes and methods
pcm_pc_repository_pc_BasicComponent_m_NoSeffTypeUsedTwice: Method = Method(name="NoSeffTypeUsedTwice", parameters={Parameter(name='pcm_pc_diagnostics', type=StringType), Parameter(name='pcm_pc_context', type=StringType)}, type=BooleanType)
pcm_pc_repository_pc_BasicComponent_m_ProvideSameInterfacesAsImplementationType: Method = Method(name="ProvideSameInterfacesAsImplementationType", parameters={Parameter(name='pcm_pc_context', type=StringType), Parameter(name='pcm_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_repository_pc_BasicComponent_m_RequireSameInterfacesAsImplementationType: Method = Method(name="RequireSameInterfacesAsImplementationType", parameters={Parameter(name='pcm_pc_context', type=StringType), Parameter(name='pcm_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_repository_pc_BasicComponent.methods={pcm_pc_repository_pc_BasicComponent_m_RequireSameInterfacesAsImplementationType, pcm_pc_repository_pc_BasicComponent_m_ProvideSameInterfacesAsImplementationType, pcm_pc_repository_pc_BasicComponent_m_NoSeffTypeUsedTwice}

# ImplementationComponentType class attributes and methods

# ServiceEffectSpecification class attributes and methods

# pcm_pc_repository_pc_ImplementationComponentType class attributes and methods
pcm_pc_repository_pc_ImplementationComponentType_componentType: Property = Property(name="componentType", type=StringType)
pcm_pc_repository_pc_ImplementationComponentType_m_RequiredInterfacesHaveToConformToCompleteType: Method = Method(name="RequiredInterfacesHaveToConformToCompleteType", parameters={Parameter(name='pcm_pc_diagnostics', type=StringType), Parameter(name='pcm_pc_context', type=StringType)}, type=BooleanType)
pcm_pc_repository_pc_ImplementationComponentType_m_providedInterfacesHaveToConformToCompleteType: Method = Method(name="providedInterfacesHaveToConformToCompleteType", parameters={Parameter(name='pcm_pc_diagnostics', type=StringType), Parameter(name='pcm_pc_context', type=StringType)}, type=BooleanType)
pcm_pc_repository_pc_ImplementationComponentType_m_ProvidedInterfaceHaveToConformToComponentType: Method = Method(name="ProvidedInterfaceHaveToConformToComponentType", parameters={Parameter(name='pcm_pc_context', type=StringType), Parameter(name='pcm_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_repository_pc_ImplementationComponentType.attributes={pcm_pc_repository_pc_ImplementationComponentType_componentType}
pcm_pc_repository_pc_ImplementationComponentType.methods={pcm_pc_repository_pc_ImplementationComponentType_m_ProvidedInterfaceHaveToConformToComponentType, pcm_pc_repository_pc_ImplementationComponentType_m_providedInterfacesHaveToConformToCompleteType, pcm_pc_repository_pc_ImplementationComponentType_m_RequiredInterfacesHaveToConformToCompleteType}

# BasicComponent class attributes and methods

# CompleteComponentType class attributes and methods

# pcm_pc_repository_pc_RepositoryComponent class attributes and methods

# InterfaceProvidingRequiringEntity class attributes and methods

# Repository class attributes and methods

# pcm_pc_repository_pc_ProvidedRole class attributes and methods

# pcm_pc_repository_pc_Parameter class attributes and methods
pcm_pc_repository_pc_Parameter_parameterName: Property = Property(name="parameterName", type=StringType)
pcm_pc_repository_pc_Parameter_modifier__Parameter: Property = Property(name="modifier__Parameter", type=StringType)
pcm_pc_repository_pc_Parameter.attributes={pcm_pc_repository_pc_Parameter_modifier__Parameter, pcm_pc_repository_pc_Parameter_parameterName}

# DataType class attributes and methods

# EventType class attributes and methods

# ResourceSignature class attributes and methods

# pcm_pc_repository_pc_DataType class attributes and methods

# pcm_pc_repository_pc_Repository class attributes and methods
pcm_pc_repository_pc_Repository_repositoryDescription: Property = Property(name="repositoryDescription", type=StringType)
pcm_pc_repository_pc_Repository.attributes={pcm_pc_repository_pc_Repository_repositoryDescription}

# Interface class attributes and methods

# FailureType class attributes and methods

# pcm_pc_repository_pc_Interface class attributes and methods
pcm_pc_repository_pc_Interface_m_NoProtocolTypeIDUsedTwice: Method = Method(name="NoProtocolTypeIDUsedTwice", parameters={Parameter(name='pcm_pc_diagnostics', type=StringType), Parameter(name='pcm_pc_context', type=StringType)}, type=BooleanType)
pcm_pc_repository_pc_Interface.methods={pcm_pc_repository_pc_Interface_m_NoProtocolTypeIDUsedTwice}

# InfrastructureSignature class attributes and methods

# Protocol class attributes and methods

# RequiredCharacterisation class attributes and methods

# pcm_pc_repository_pc_RequiredCharacterisation class attributes and methods
pcm_pc_repository_pc_RequiredCharacterisation_type: Property = Property(name="type", type=StringType)
pcm_pc_repository_pc_RequiredCharacterisation.attributes={pcm_pc_repository_pc_RequiredCharacterisation_type}

# Parameter class attributes and methods

# pcm_pc_repository_pc_EventGroup class attributes and methods

# pcm_pc_repository_pc_EventType class attributes and methods

# Signature class attributes and methods

# pcm_pc_repository_pc_Signature class attributes and methods

# ExceptionType class attributes and methods

# pcm_pc_repository_pc_InfrastructureSignature class attributes and methods

# InfrastructureInterface class attributes and methods

# pcm_pc_repository_pc_InfrastructureInterface class attributes and methods

# pcm_pc_repository_pc_InfrastructureRequiredRole class attributes and methods

# pcm_pc_repository_pc_RequiredRole class attributes and methods

# pcm_pc_repository_pc_OperationSignature class attributes and methods
pcm_pc_repository_pc_OperationSignature_m_ParameterNamesHaveToBeUniqueForASignature: Method = Method(name="ParameterNamesHaveToBeUniqueForASignature", parameters={Parameter(name='pcm_pc_context', type=StringType), Parameter(name='pcm_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_repository_pc_OperationSignature.methods={pcm_pc_repository_pc_OperationSignature_m_ParameterNamesHaveToBeUniqueForASignature}

# OperationInterface class attributes and methods

# pcm_pc_repository_pc_ExceptionType class attributes and methods
pcm_pc_repository_pc_ExceptionType_exceptionName: Property = Property(name="exceptionName", type=StringType)
pcm_pc_repository_pc_ExceptionType_exceptionMessage: Property = Property(name="exceptionMessage", type=StringType)
pcm_pc_repository_pc_ExceptionType.attributes={pcm_pc_repository_pc_ExceptionType_exceptionName, pcm_pc_repository_pc_ExceptionType_exceptionMessage}

# pcm_pc_repository_pc_OperationInterface class attributes and methods
pcm_pc_repository_pc_OperationInterface_m_SignaturesHaveToBeUniqueForAnInterface: Method = Method(name="SignaturesHaveToBeUniqueForAnInterface", parameters={Parameter(name='pcm_pc_context', type=StringType), Parameter(name='pcm_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_repository_pc_OperationInterface.methods={pcm_pc_repository_pc_OperationInterface_m_SignaturesHaveToBeUniqueForAnInterface}

# pcm_pc_repository_pc_OperationRequiredRole class attributes and methods

# pcm_pc_repository_pc_SourceRole class attributes and methods

# pcm_pc_repository_pc_SinkRole class attributes and methods

# pcm_pc_repository_pc_InfrastructureProvidedRole class attributes and methods

# pcm_pc_repository_pc_CompleteComponentType class attributes and methods
pcm_pc_repository_pc_CompleteComponentType_m_AtLeastOneInterfaceHasToBeProvidedOrRequiredByAUsefullCompleteComponentType: Method = Method(name="AtLeastOneInterfaceHasToBeProvidedOrRequiredByAUsefullCompleteComponentType", parameters={Parameter(name='pcm_pc_context', type=StringType), Parameter(name='pcm_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_repository_pc_CompleteComponentType_m_providedInterfacesHaveToConformToProvidedType2: Method = Method(name="providedInterfacesHaveToConformToProvidedType2", parameters={Parameter(name='pcm_pc_context', type=StringType), Parameter(name='pcm_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_repository_pc_CompleteComponentType.methods={pcm_pc_repository_pc_CompleteComponentType_m_AtLeastOneInterfaceHasToBeProvidedOrRequiredByAUsefullCompleteComponentType, pcm_pc_repository_pc_CompleteComponentType_m_providedInterfacesHaveToConformToProvidedType2}

# ProvidesComponentType class attributes and methods

# pcm_pc_repository_pc_ProvidesComponentType class attributes and methods
pcm_pc_repository_pc_ProvidesComponentType_m_AtLeastOneInterfaceHasToBeProvidedByAUsefullProvidesComponentType: Method = Method(name="AtLeastOneInterfaceHasToBeProvidedByAUsefullProvidesComponentType", parameters={Parameter(name='pcm_pc_context', type=StringType), Parameter(name='pcm_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_repository_pc_ProvidesComponentType.methods={pcm_pc_repository_pc_ProvidesComponentType_m_AtLeastOneInterfaceHasToBeProvidedByAUsefullProvidesComponentType}

# pcm_pc_repository_pc_OperationProvidedRole class attributes and methods

# pcm_pc_repository_pc_CompositeComponent class attributes and methods
pcm_pc_repository_pc_CompositeComponent_m_ProvideSameInterfaces: Method = Method(name="ProvideSameInterfaces", parameters={Parameter(name='pcm_pc_context', type=StringType), Parameter(name='pcm_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_repository_pc_CompositeComponent_m_RequireSameInterfaces: Method = Method(name="RequireSameInterfaces", parameters={Parameter(name='pcm_pc_diagnostics', type=StringType), Parameter(name='pcm_pc_context', type=StringType)}, type=BooleanType)
pcm_pc_repository_pc_CompositeComponent.methods={pcm_pc_repository_pc_CompositeComponent_m_RequireSameInterfaces, pcm_pc_repository_pc_CompositeComponent_m_ProvideSameInterfaces}

# entity_pc_ComposedProvidingRequiringEntity class attributes and methods

# repository_pc_ImplementationComponentType class attributes and methods

# pcm_pc_repository_pc_PrimitiveDataType class attributes and methods
pcm_pc_repository_pc_PrimitiveDataType_type: Property = Property(name="type", type=StringType)
pcm_pc_repository_pc_PrimitiveDataType.attributes={pcm_pc_repository_pc_PrimitiveDataType_type}

# pcm_pc_repository_pc_CollectionDataType class attributes and methods

# repository_pc_DataType class attributes and methods

# pcm_pc_repository_pc_CompositeDataType class attributes and methods

# CompositeDataType class attributes and methods

# pcm_pc_repository_pc_Role class attributes and methods

# pcm_pc_resourcetype_pc_ResourceSignature class attributes and methods
pcm_pc_resourcetype_pc_ResourceSignature_resourceServiceId: Property = Property(name="resourceServiceId", type=IntegerType)
pcm_pc_resourcetype_pc_ResourceSignature.attributes={pcm_pc_resourcetype_pc_ResourceSignature_resourceServiceId}

# pcm_pc_resourcetype_pc_ProcessingResourceType class attributes and methods

# ResourceType class attributes and methods

# HardwareInducedFailureType class attributes and methods

# pcm_pc_resourcetype_pc_ResourceType class attributes and methods

# UnitCarryingElement class attributes and methods

# ResourceRepository class attributes and methods

# pcm_pc_resourcetype_pc_ResourceRepository class attributes and methods

# SchedulingPolicy class attributes and methods

# pcm_pc_resourcetype_pc_SchedulingPolicy class attributes and methods

# InnerDeclaration class attributes and methods

# pcm_pc_repository_pc_InnerDeclaration class attributes and methods

# NamedElement class attributes and methods

# pcm_pc_protocol_pc_Protocol class attributes and methods
pcm_pc_protocol_pc_Protocol_protocolTypeID: Property = Property(name="protocolTypeID", type=StringType)
pcm_pc_protocol_pc_Protocol.attributes={pcm_pc_protocol_pc_Protocol_protocolTypeID}

# pcm_pc_parameter_pc_VariableUsage class attributes and methods

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

# pcm_pc_resourcetype_pc_CommunicationLinkResourceType class attributes and methods

# NetworkInducedFailureType class attributes and methods

# pcm_pc_resourcetype_pc_ResourceInterface class attributes and methods

# pcm_pc_parameter_pc_CharacterisedVariable class attributes and methods
pcm_pc_parameter_pc_CharacterisedVariable_characterisationType: Property = Property(name="characterisationType", type=StringType)
pcm_pc_parameter_pc_CharacterisedVariable.attributes={pcm_pc_parameter_pc_CharacterisedVariable_characterisationType}

# Variable class attributes and methods

# pcm_pc_reliability_pc_FailureOccurrenceDescription class attributes and methods
pcm_pc_reliability_pc_FailureOccurrenceDescription_failureProbability: Property = Property(name="failureProbability", type=FloatType)
pcm_pc_reliability_pc_FailureOccurrenceDescription_m_EnsureValidFailureProbabilityRange: Method = Method(name="EnsureValidFailureProbabilityRange", parameters={Parameter(name='pcm_pc_diagnostics', type=StringType), Parameter(name='pcm_pc_context', type=StringType)}, type=BooleanType)
pcm_pc_reliability_pc_FailureOccurrenceDescription.attributes={pcm_pc_reliability_pc_FailureOccurrenceDescription_failureProbability}
pcm_pc_reliability_pc_FailureOccurrenceDescription.methods={pcm_pc_reliability_pc_FailureOccurrenceDescription_m_EnsureValidFailureProbabilityRange}

# pcm_pc_reliability_pc_HardwareInducedFailureType class attributes and methods
pcm_pc_reliability_pc_HardwareInducedFailureType_m_HardwareInducedFailureTypeHasProcessingResourceType: Method = Method(name="HardwareInducedFailureTypeHasProcessingResourceType", parameters={Parameter(name='pcm_pc_diagnostics', type=StringType), Parameter(name='pcm_pc_context', type=StringType)}, type=BooleanType)
pcm_pc_reliability_pc_HardwareInducedFailureType.methods={pcm_pc_reliability_pc_HardwareInducedFailureType_m_HardwareInducedFailureTypeHasProcessingResourceType}

# ProcessingResourceType class attributes and methods

# InternalFailureOccurrenceDescription class attributes and methods

# pcm_pc_reliability_pc_InternalFailureOccurrenceDescription class attributes and methods
pcm_pc_reliability_pc_InternalFailureOccurrenceDescription_m_NoResourceTimeoutFailureAllowedForInternalFailureOccurrenceDescription: Method = Method(name="NoResourceTimeoutFailureAllowedForInternalFailureOccurrenceDescription", parameters={Parameter(name='pcm_pc_diagnostics', type=StringType), Parameter(name='pcm_pc_context', type=StringType)}, type=BooleanType)
pcm_pc_reliability_pc_InternalFailureOccurrenceDescription.methods={pcm_pc_reliability_pc_InternalFailureOccurrenceDescription_m_NoResourceTimeoutFailureAllowedForInternalFailureOccurrenceDescription}

# FailureOccurrenceDescription class attributes and methods

# InternalAction class attributes and methods

# SoftwareInducedFailureType class attributes and methods

# pcm_pc_reliability_pc_NetworkInducedFailureType class attributes and methods
pcm_pc_reliability_pc_NetworkInducedFailureType_m_NetworkInducedFailureTypeHasCommunicationLinkResourceType: Method = Method(name="NetworkInducedFailureTypeHasCommunicationLinkResourceType", parameters={Parameter(name='pcm_pc_context', type=StringType), Parameter(name='pcm_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_reliability_pc_NetworkInducedFailureType.methods={pcm_pc_reliability_pc_NetworkInducedFailureType_m_NetworkInducedFailureTypeHasCommunicationLinkResourceType}

# CommunicationLinkResourceType class attributes and methods

# pcm_pc_reliability_pc_ExternalFailureOccurrenceDescription class attributes and methods
pcm_pc_reliability_pc_ExternalFailureOccurrenceDescription_m_NoResourceTimeoutFailureAllowedForExternalFailureOccurrenceDescription: Method = Method(name="NoResourceTimeoutFailureAllowedForExternalFailureOccurrenceDescription", parameters={Parameter(name='pcm_pc_context', type=StringType), Parameter(name='pcm_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_reliability_pc_ExternalFailureOccurrenceDescription.methods={pcm_pc_reliability_pc_ExternalFailureOccurrenceDescription_m_NoResourceTimeoutFailureAllowedForExternalFailureOccurrenceDescription}

# qos_reliability_pc_SpecifiedReliabilityAnnotation class attributes and methods

# pcm_pc_reliability_pc_SoftwareInducedFailureType class attributes and methods

# pcm_pc_reliability_pc_FailureType class attributes and methods

# pcm_pc_seff_pc_StopAction class attributes and methods
pcm_pc_seff_pc_StopAction_m_StopActionSuccessorMustNotBeDefined: Method = Method(name="StopActionSuccessorMustNotBeDefined", parameters={Parameter(name='pcm_pc_context', type=StringType), Parameter(name='pcm_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_seff_pc_StopAction.methods={pcm_pc_seff_pc_StopAction_m_StopActionSuccessorMustNotBeDefined}

# AbstractInternalControlFlowAction class attributes and methods

# pcm_pc_seff_pc_AbstractInternalControlFlowAction class attributes and methods

# AbstractAction class attributes and methods

# pcm_pc_seff_pc_AbstractAction class attributes and methods

# ResourceDemandingBehaviour class attributes and methods

# pcm_pc_reliability_pc_ResourceTimeoutFailureType class attributes and methods

# AbstractLoopAction class attributes and methods

# AbstractBranchTransition class attributes and methods

# pcm_pc_seff_pc_AbstractLoopAction class attributes and methods

# pcm_pc_seff_pc_AbstractBranchTransition class attributes and methods

# pcm_pc_seff_pc_ResourceDemandingBehaviour class attributes and methods
pcm_pc_seff_pc_ResourceDemandingBehaviour_m_ExactlyOneStartAction: Method = Method(name="ExactlyOneStartAction", parameters={Parameter(name='pcm_pc_diagnostics', type=StringType), Parameter(name='pcm_pc_context', type=StringType)}, type=BooleanType)
pcm_pc_seff_pc_ResourceDemandingBehaviour_m_EachActionExceptStartActionandStopActionMustHhaveAPredecessorAndSuccessor: Method = Method(name="EachActionExceptStartActionandStopActionMustHhaveAPredecessorAndSuccessor", parameters={Parameter(name='pcm_pc_diagnostics', type=StringType), Parameter(name='pcm_pc_context', type=StringType)}, type=BooleanType)
pcm_pc_seff_pc_ResourceDemandingBehaviour_m_ExactlyOneStopAction: Method = Method(name="ExactlyOneStopAction", parameters={Parameter(name='pcm_pc_context', type=StringType), Parameter(name='pcm_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_seff_pc_ResourceDemandingBehaviour.methods={pcm_pc_seff_pc_ResourceDemandingBehaviour_m_ExactlyOneStartAction, pcm_pc_seff_pc_ResourceDemandingBehaviour_m_EachActionExceptStartActionandStopActionMustHhaveAPredecessorAndSuccessor, pcm_pc_seff_pc_ResourceDemandingBehaviour_m_ExactlyOneStopAction}

# BranchAction class attributes and methods

# pcm_pc_seff_pc_BranchAction class attributes and methods
pcm_pc_seff_pc_BranchAction_m_EitherGuardedBranchesOrProbabilisiticBranchTransitions: Method = Method(name="EitherGuardedBranchesOrProbabilisiticBranchTransitions", parameters={Parameter(name='pcm_pc_context', type=StringType), Parameter(name='pcm_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_seff_pc_BranchAction_m_AllProbabilisticBranchProbabilitiesMustSumUpTo1: Method = Method(name="AllProbabilisticBranchProbabilitiesMustSumUpTo1", parameters={Parameter(name='pcm_pc_context', type=StringType), Parameter(name='pcm_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_seff_pc_BranchAction.methods={pcm_pc_seff_pc_BranchAction_m_EitherGuardedBranchesOrProbabilisiticBranchTransitions, pcm_pc_seff_pc_BranchAction_m_AllProbabilisticBranchProbabilitiesMustSumUpTo1}

# pcm_pc_seff_pc_CallAction class attributes and methods

# pcm_pc_seff_pc_StartAction class attributes and methods
pcm_pc_seff_pc_StartAction_m_StartActionPredecessorMustNotBeDefined: Method = Method(name="StartActionPredecessorMustNotBeDefined", parameters={Parameter(name='pcm_pc_diagnostics', type=StringType), Parameter(name='pcm_pc_context', type=StringType)}, type=BooleanType)
pcm_pc_seff_pc_StartAction.methods={pcm_pc_seff_pc_StartAction_m_StartActionPredecessorMustNotBeDefined}

# pcm_pc_seff_pc_ServiceEffectSpecification class attributes and methods
pcm_pc_seff_pc_ServiceEffectSpecification_seffTypeID: Property = Property(name="seffTypeID", type=StringType)
pcm_pc_seff_pc_ServiceEffectSpecification_m_ReferencedSignatureMustBelongToInterfaceReferencedByProvidedRole: Method = Method(name="ReferencedSignatureMustBelongToInterfaceReferencedByProvidedRole", parameters={Parameter(name='pcm_pc_context', type=StringType), Parameter(name='pcm_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_seff_pc_ServiceEffectSpecification.attributes={pcm_pc_seff_pc_ServiceEffectSpecification_seffTypeID}
pcm_pc_seff_pc_ServiceEffectSpecification.methods={pcm_pc_seff_pc_ServiceEffectSpecification_m_ReferencedSignatureMustBelongToInterfaceReferencedByProvidedRole}

# pcm_pc_seff_pc_ResourceDemandingSEFF class attributes and methods

# ResourceDemandingInternalBehaviour class attributes and methods

# pcm_pc_seff_pc_ResourceDemandingInternalBehaviour class attributes and methods

# ResourceDemandingSEFF class attributes and methods

# pcm_pc_seff_pc_ReleaseAction class attributes and methods

# pcm_pc_seff_pc_LoopAction class attributes and methods

# pcm_pc_seff_pc_ForkAction class attributes and methods

# ForkedBehaviour class attributes and methods

# pcm_pc_seff_pc_ForkedBehaviour class attributes and methods

# pcm_pc_seff_pc_CallReturnAction class attributes and methods

# seff_pc_ServiceEffectSpecification class attributes and methods

# seff_pc_ResourceDemandingBehaviour class attributes and methods

# pcm_pc_seff_pc_ProbabilisticBranchTransition class attributes and methods
pcm_pc_seff_pc_ProbabilisticBranchTransition_branchProbability: Property = Property(name="branchProbability", type=FloatType)
pcm_pc_seff_pc_ProbabilisticBranchTransition.attributes={pcm_pc_seff_pc_ProbabilisticBranchTransition_branchProbability}

# pcm_pc_seff_pc_AcquireAction class attributes and methods
pcm_pc_seff_pc_AcquireAction_timeout: Property = Property(name="timeout", type=BooleanType)
pcm_pc_seff_pc_AcquireAction_timeoutValue: Property = Property(name="timeoutValue", type=FloatType)
pcm_pc_seff_pc_AcquireAction_m_TimeoutValueOfAcquireActionMustNotBeNegative: Method = Method(name="TimeoutValueOfAcquireActionMustNotBeNegative", parameters={Parameter(name='pcm_pc_context', type=StringType), Parameter(name='pcm_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_seff_pc_AcquireAction.attributes={pcm_pc_seff_pc_AcquireAction_timeoutValue, pcm_pc_seff_pc_AcquireAction_timeout}
pcm_pc_seff_pc_AcquireAction.methods={pcm_pc_seff_pc_AcquireAction_m_TimeoutValueOfAcquireActionMustNotBeNegative}

# ForkAction class attributes and methods

# pcm_pc_seff_pc_SynchronisationPoint class attributes and methods

# pcm_pc_seff_pc_ExternalCallAction class attributes and methods
pcm_pc_seff_pc_ExternalCallAction_retryCount: Property = Property(name="retryCount", type=IntegerType)
pcm_pc_seff_pc_ExternalCallAction_m_OperationRequiredRoleMustBeReferencedByContainer: Method = Method(name="OperationRequiredRoleMustBeReferencedByContainer", parameters={Parameter(name='pcm_pc_context', type=StringType), Parameter(name='pcm_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_seff_pc_ExternalCallAction_m_SignatureBelongsToRole: Method = Method(name="SignatureBelongsToRole", parameters={Parameter(name='pcm_pc_context', type=StringType), Parameter(name='pcm_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_seff_pc_ExternalCallAction.attributes={pcm_pc_seff_pc_ExternalCallAction_retryCount}
pcm_pc_seff_pc_ExternalCallAction.methods={pcm_pc_seff_pc_ExternalCallAction_m_OperationRequiredRoleMustBeReferencedByContainer, pcm_pc_seff_pc_ExternalCallAction_m_SignatureBelongsToRole}

# seff_pc_AbstractAction class attributes and methods

# seff_pc_CallReturnAction class attributes and methods

# seff_reliability_pc_FailureHandlingEntity class attributes and methods

# pcm_pc_seff_pc_SetVariableAction class attributes and methods

# pcm_pc_seff_pc_InternalCallAction class attributes and methods

# seff_pc_CallAction class attributes and methods

# seff_pc_AbstractInternalControlFlowAction class attributes and methods

# pcm_pc_seff_pc_EmitEventAction class attributes and methods

# pcm_pc_seff_pc_InternalAction class attributes and methods
pcm_pc_seff_pc_InternalAction_m_MultipleInternalOccurrenceDescriptionsPerFailureTypeNotAllowed: Method = Method(name="MultipleInternalOccurrenceDescriptionsPerFailureTypeNotAllowed", parameters={Parameter(name='pcm_pc_diagnostics', type=StringType), Parameter(name='pcm_pc_context', type=StringType)}, type=BooleanType)
pcm_pc_seff_pc_InternalAction_m_SumOfInternalActionFailureProbabilitiesMustNotExceed1: Method = Method(name="SumOfInternalActionFailureProbabilitiesMustNotExceed1", parameters={Parameter(name='pcm_pc_diagnostics', type=StringType), Parameter(name='pcm_pc_context', type=StringType)}, type=BooleanType)
pcm_pc_seff_pc_InternalAction.methods={pcm_pc_seff_pc_InternalAction_m_MultipleInternalOccurrenceDescriptionsPerFailureTypeNotAllowed, pcm_pc_seff_pc_InternalAction_m_SumOfInternalActionFailureProbabilitiesMustNotExceed1}

# pcm_pc_seff_pc_CollectionIteratorAction class attributes and methods

# pcm_pc_seff_pc_GuardedBranchTransition class attributes and methods

# pcm_pc_seff_performance_pc_ResourceCall class attributes and methods
pcm_pc_seff_performance_pc_ResourceCall_m_ResourceSignatureBelongsToResourceRequiredRole: Method = Method(name="ResourceSignatureBelongsToResourceRequiredRole", parameters={Parameter(name='pcm_pc_context', type=StringType), Parameter(name='pcm_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_seff_performance_pc_ResourceCall_m_ResourceRequiredRoleMustBeReferencedByComponent: Method = Method(name="ResourceRequiredRoleMustBeReferencedByComponent", parameters={Parameter(name='pcm_pc_context', type=StringType), Parameter(name='pcm_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_seff_performance_pc_ResourceCall_m_SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction: Method = Method(name="SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction", parameters={Parameter(name='pcm_pc_context', type=StringType), Parameter(name='pcm_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_seff_performance_pc_ResourceCall.methods={pcm_pc_seff_performance_pc_ResourceCall_m_ResourceSignatureBelongsToResourceRequiredRole, pcm_pc_seff_performance_pc_ResourceCall_m_ResourceRequiredRoleMustBeReferencedByComponent, pcm_pc_seff_performance_pc_ResourceCall_m_SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction}

# pcm_pc_seff_performance_pc_InfrastructureCall class attributes and methods
pcm_pc_seff_performance_pc_InfrastructureCall_m_SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction: Method = Method(name="SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction", parameters={Parameter(name='pcm_pc_context', type=StringType), Parameter(name='pcm_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_seff_performance_pc_InfrastructureCall_m_SignatureMustBelongToUsedRequiredRole: Method = Method(name="SignatureMustBelongToUsedRequiredRole", parameters={Parameter(name='pcm_pc_diagnostics', type=StringType), Parameter(name='pcm_pc_context', type=StringType)}, type=BooleanType)
pcm_pc_seff_performance_pc_InfrastructureCall_m_ReferencedRequiredRoleMustBeRequiredByComponent: Method = Method(name="ReferencedRequiredRoleMustBeRequiredByComponent", parameters={Parameter(name='pcm_pc_context', type=StringType), Parameter(name='pcm_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_seff_performance_pc_InfrastructureCall.methods={pcm_pc_seff_performance_pc_InfrastructureCall_m_SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction, pcm_pc_seff_performance_pc_InfrastructureCall_m_SignatureMustBelongToUsedRequiredRole, pcm_pc_seff_performance_pc_InfrastructureCall_m_ReferencedRequiredRoleMustBeRequiredByComponent}

# pcm_pc_seff_reliability_pc_RecoveryActionBehaviour class attributes and methods
pcm_pc_seff_reliability_pc_RecoveryActionBehaviour_m_RecoveryActionBehaviourHasOnlyOnePredecessor: Method = Method(name="RecoveryActionBehaviourHasOnlyOnePredecessor", parameters={Parameter(name='pcm_pc_diagnostics', type=StringType), Parameter(name='pcm_pc_context', type=StringType)}, type=BooleanType)
pcm_pc_seff_reliability_pc_RecoveryActionBehaviour_m_RecoveryActionBehaviourIsNotSuccessorOfItself: Method = Method(name="RecoveryActionBehaviourIsNotSuccessorOfItself", parameters={Parameter(name='pcm_pc_diagnostics', type=StringType), Parameter(name='pcm_pc_context', type=StringType)}, type=BooleanType)
pcm_pc_seff_reliability_pc_RecoveryActionBehaviour_m_SuccessorsOfRecoveryActionBehaviourHandleDisjointFailureTypes: Method = Method(name="SuccessorsOfRecoveryActionBehaviourHandleDisjointFailureTypes", parameters={Parameter(name='pcm_pc_context', type=StringType), Parameter(name='pcm_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_seff_reliability_pc_RecoveryActionBehaviour.methods={pcm_pc_seff_reliability_pc_RecoveryActionBehaviour_m_RecoveryActionBehaviourIsNotSuccessorOfItself, pcm_pc_seff_reliability_pc_RecoveryActionBehaviour_m_RecoveryActionBehaviourHasOnlyOnePredecessor, pcm_pc_seff_reliability_pc_RecoveryActionBehaviour_m_SuccessorsOfRecoveryActionBehaviourHandleDisjointFailureTypes}

# pcm_pc_seff_performance_pc_ParametricResourceDemand class attributes and methods
pcm_pc_seff_performance_pc_ParametricResourceDemand_m_DemandedProcessingResourceMustBeUniqueWithinAbstractInternalControlFlowAction: Method = Method(name="DemandedProcessingResourceMustBeUniqueWithinAbstractInternalControlFlowAction", parameters={Parameter(name='pcm_pc_diagnostics', type=StringType), Parameter(name='pcm_pc_context', type=StringType)}, type=BooleanType)
pcm_pc_seff_performance_pc_ParametricResourceDemand.methods={pcm_pc_seff_performance_pc_ParametricResourceDemand_m_DemandedProcessingResourceMustBeUniqueWithinAbstractInternalControlFlowAction}

# pcm_pc_seff_reliability_pc_FailureHandlingEntity class attributes and methods

# pcm_pc_qosannotations_pc_SpecifiedQoSAnnotation class attributes and methods

# QoSAnnotations class attributes and methods

# pcm_pc_qosannotations_pc_QoSAnnotations class attributes and methods
pcm_pc_qosannotations_pc_QoSAnnotations_m_MultipleReliabilityAnnotationsPerExternalCallNotAllowed: Method = Method(name="MultipleReliabilityAnnotationsPerExternalCallNotAllowed", parameters={Parameter(name='pcm_pc_context', type=StringType), Parameter(name='pcm_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_qosannotations_pc_QoSAnnotations.methods={pcm_pc_qosannotations_pc_QoSAnnotations_m_MultipleReliabilityAnnotationsPerExternalCallNotAllowed}

# seff_reliability_pc_RecoveryActionBehaviour class attributes and methods

# seff_reliability_pc_RecoveryAction class attributes and methods

# pcm_pc_seff_reliability_pc_RecoveryAction class attributes and methods
pcm_pc_seff_reliability_pc_RecoveryAction_m_PrimaryBehaviourOfRecoveryActionMustBeSet: Method = Method(name="PrimaryBehaviourOfRecoveryActionMustBeSet", parameters={Parameter(name='pcm_pc_diagnostics', type=StringType), Parameter(name='pcm_pc_context', type=StringType)}, type=BooleanType)
pcm_pc_seff_reliability_pc_RecoveryAction.methods={pcm_pc_seff_reliability_pc_RecoveryAction_m_PrimaryBehaviourOfRecoveryActionMustBeSet}

# System class attributes and methods

# SpecifiedQoSAnnotation class attributes and methods

# pcm_pc_qosannotations_pc_SpecifiedOutputParameterAbstraction class attributes and methods

# pcm_pc_qos_performance_pc_SystemSpecifiedExecutionTime class attributes and methods
pcm_pc_qos_performance_pc_SystemSpecifiedExecutionTime_m_SystemSpecifiedExecutionTimeMustReferenceRequiredRoleOfASystem: Method = Method(name="SystemSpecifiedExecutionTimeMustReferenceRequiredRoleOfASystem", parameters={Parameter(name='pcm_pc_diagnostics', type=StringType), Parameter(name='pcm_pc_context', type=StringType)}, type=BooleanType)
pcm_pc_qos_performance_pc_SystemSpecifiedExecutionTime.methods={pcm_pc_qos_performance_pc_SystemSpecifiedExecutionTime_m_SystemSpecifiedExecutionTimeMustReferenceRequiredRoleOfASystem}

# SpecifiedExecutionTime class attributes and methods

# ExternalFailureOccurrenceDescription class attributes and methods

# pcm_pc_system_pc_System class attributes and methods
pcm_pc_system_pc_System_m_SystemMustHaveAtLeastOneProvidedRole: Method = Method(name="SystemMustHaveAtLeastOneProvidedRole", parameters={Parameter(name='pcm_pc_context', type=StringType), Parameter(name='pcm_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_system_pc_System.methods={pcm_pc_system_pc_System_m_SystemMustHaveAtLeastOneProvidedRole}

# pcm_pc_qos_performance_pc_SpecifiedExecutionTime class attributes and methods

# pcm_pc_qos_performance_pc_ComponentSpecifiedExecutionTime class attributes and methods

# pcm_pc_qos_reliability_pc_SpecifiedReliabilityAnnotation class attributes and methods
pcm_pc_qos_reliability_pc_SpecifiedReliabilityAnnotation_m_SpecifiedReliabilityAnnotationMustReferenceRequiredRoleOfASystem: Method = Method(name="SpecifiedReliabilityAnnotationMustReferenceRequiredRoleOfASystem", parameters={Parameter(name='pcm_pc_context', type=StringType), Parameter(name='pcm_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_qos_reliability_pc_SpecifiedReliabilityAnnotation_m_SumOfReliabilityAnnotationFailureProbabilitiesMustNotExceed1: Method = Method(name="SumOfReliabilityAnnotationFailureProbabilitiesMustNotExceed1", parameters={Parameter(name='pcm_pc_context', type=StringType), Parameter(name='pcm_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_qos_reliability_pc_SpecifiedReliabilityAnnotation_m_MultipleExternalOccurrenceDescriptionsPerFailureTypeNotAllowed: Method = Method(name="MultipleExternalOccurrenceDescriptionsPerFailureTypeNotAllowed", parameters={Parameter(name='pcm_pc_context', type=StringType), Parameter(name='pcm_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_qos_reliability_pc_SpecifiedReliabilityAnnotation.methods={pcm_pc_qos_reliability_pc_SpecifiedReliabilityAnnotation_m_SumOfReliabilityAnnotationFailureProbabilitiesMustNotExceed1, pcm_pc_qos_reliability_pc_SpecifiedReliabilityAnnotation_m_SpecifiedReliabilityAnnotationMustReferenceRequiredRoleOfASystem, pcm_pc_qos_reliability_pc_SpecifiedReliabilityAnnotation_m_MultipleExternalOccurrenceDescriptionsPerFailureTypeNotAllowed}

# pcm_pc_resourceenvironment_pc_LinkingResource class attributes and methods

# ResourceEnvironment class attributes and methods

# pcm_pc_resourceenvironment_pc_ResourceContainer class attributes and methods

# pcm_pc_resourceenvironment_pc_ProcessingResourceSpecification class attributes and methods
pcm_pc_resourceenvironment_pc_ProcessingResourceSpecification_MTTR: Property = Property(name="MTTR", type=FloatType)
pcm_pc_resourceenvironment_pc_ProcessingResourceSpecification_MTTF: Property = Property(name="MTTF", type=FloatType)
pcm_pc_resourceenvironment_pc_ProcessingResourceSpecification_requiredByContainer: Property = Property(name="requiredByContainer", type=BooleanType)
pcm_pc_resourceenvironment_pc_ProcessingResourceSpecification_numberOfReplicas: Property = Property(name="numberOfReplicas", type=IntegerType)
pcm_pc_resourceenvironment_pc_ProcessingResourceSpecification.attributes={pcm_pc_resourceenvironment_pc_ProcessingResourceSpecification_numberOfReplicas, pcm_pc_resourceenvironment_pc_ProcessingResourceSpecification_MTTF, pcm_pc_resourceenvironment_pc_ProcessingResourceSpecification_requiredByContainer, pcm_pc_resourceenvironment_pc_ProcessingResourceSpecification_MTTR}

# pcm_pc_resourceenvironment_pc_ResourceEnvironment class attributes and methods

# LinkingResource class attributes and methods

# ResourceContainer class attributes and methods

# pcm_pc_allocation_pc_AllocationContext class attributes and methods
pcm_pc_allocation_pc_AllocationContext_m_OneAssemblyContextOrOneEventChannelShouldBeReferred: Method = Method(name="OneAssemblyContextOrOneEventChannelShouldBeReferred", parameters={Parameter(name='pcm_pc_diagnostics', type=StringType), Parameter(name='pcm_pc_context', type=StringType)}, type=BooleanType)
pcm_pc_allocation_pc_AllocationContext.methods={pcm_pc_allocation_pc_AllocationContext_m_OneAssemblyContextOrOneEventChannelShouldBeReferred}

# Allocation class attributes and methods

# pcm_pc_allocation_pc_Allocation class attributes and methods
pcm_pc_allocation_pc_Allocation_m_EachAssemblyContextWithinSystemHasToBeAllocatedExactlyOnce: Method = Method(name="EachAssemblyContextWithinSystemHasToBeAllocatedExactlyOnce", parameters={Parameter(name='pcm_pc_diagnostics', type=StringType), Parameter(name='pcm_pc_context', type=StringType)}, type=BooleanType)
pcm_pc_allocation_pc_Allocation_m_CommunicatingServersHaveToBeConnectedByLinkingResource: Method = Method(name="CommunicatingServersHaveToBeConnectedByLinkingResource", parameters={Parameter(name='pcm_pc_context', type=StringType), Parameter(name='pcm_pc_diagnostics', type=StringType)}, type=BooleanType)
pcm_pc_allocation_pc_Allocation.methods={pcm_pc_allocation_pc_Allocation_m_EachAssemblyContextWithinSystemHasToBeAllocatedExactlyOnce, pcm_pc_allocation_pc_Allocation_m_CommunicatingServersHaveToBeConnectedByLinkingResource}

# pcm_pc_resourceenvironment_pc_CommunicationLinkResourceSpecification class attributes and methods
pcm_pc_resourceenvironment_pc_CommunicationLinkResourceSpecification_failureProbability: Property = Property(name="failureProbability", type=FloatType)
pcm_pc_resourceenvironment_pc_CommunicationLinkResourceSpecification.attributes={pcm_pc_resourceenvironment_pc_CommunicationLinkResourceSpecification_failureProbability}

# AllocationContext class attributes and methods

# pcm_pc_subsystem_pc_SubSystem class attributes and methods

# repository_pc_RepositoryComponent class attributes and methods

# pcm_pc_completions_pc_Completion class attributes and methods

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
passiveResource_capacity_PCMRandomVariable2: BinaryAssociation = BinaryAssociation(
    name="passiveResource_capacity_PCMRandomVariable2",
    ends={
        Property(name="capacity_PassiveResource", type=PassiveResource, multiplicity=Multiplicity(0, 1)),
        Property(name="PassiveResource", type=pcm_pc_core_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1))
    }
)
variableCharacterisation_Specification3: BinaryAssociation = BinaryAssociation(
    name="variableCharacterisation_Specification3",
    ends={
        Property(name="VariableCharacterisation", type=pcm_pc_core_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="specification_VariableCharacterisation", type=VariableCharacterisation, multiplicity=Multiplicity(0, 1))
    }
)
infrastructureCall__PCMRandomVariable4: BinaryAssociation = BinaryAssociation(
    name="infrastructureCall__PCMRandomVariable4",
    ends={
        Property(name="InfrastructureCall", type=pcm_pc_core_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="numberOfCalls__InfrastructureCall", type=seff_performance_pc_InfrastructureCall, multiplicity=Multiplicity(0, 1))
    }
)
resourceCall__PCMRandomVariable5: BinaryAssociation = BinaryAssociation(
    name="resourceCall__PCMRandomVariable5",
    ends={
        Property(name="ResourceCall", type=pcm_pc_core_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="numberOfCalls__ResourceCall", type=seff_performance_pc_ResourceCall, multiplicity=Multiplicity(0, 1))
    }
)
parametricResourceDemand_PCMRandomVariable6: BinaryAssociation = BinaryAssociation(
    name="parametricResourceDemand_PCMRandomVariable6",
    ends={
        Property(name="ParametricResourceDemand", type=pcm_pc_core_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="specification_ParametericResourceDemand", type=seff_performance_pc_ParametricResourceDemand, multiplicity=Multiplicity(0, 1))
    }
)
loopAction_PCMRandomVariable7: BinaryAssociation = BinaryAssociation(
    name="loopAction_PCMRandomVariable7",
    ends={
        Property(name="LoopAction", type=pcm_pc_core_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="iterationCount_LoopAction", type=LoopAction, multiplicity=Multiplicity(0, 1))
    }
)
guardedBranchTransition_PCMRandomVariable8: BinaryAssociation = BinaryAssociation(
    name="guardedBranchTransition_PCMRandomVariable8",
    ends={
        Property(name="GuardedBranchTransition", type=pcm_pc_core_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="branchCondition_GuardedBranchTransition", type=GuardedBranchTransition, multiplicity=Multiplicity(0, 1))
    }
)
specifiedExecutionTime_PCMRandomVariable9: BinaryAssociation = BinaryAssociation(
    name="specifiedExecutionTime_PCMRandomVariable9",
    ends={
        Property(name="SpecifiedExecutionTime", type=pcm_pc_core_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="specification_SpecifiedExecutionTime", type=qos_performance_pc_SpecifiedExecutionTime, multiplicity=Multiplicity(0, 1))
    }
)
eventChannelSinkConnector__FilterCondition10: BinaryAssociation = BinaryAssociation(
    name="eventChannelSinkConnector__FilterCondition10",
    ends={
        Property(name="EventChannelSinkConnector", type=pcm_pc_core_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="filterCondition__EventChannelSinkConnector", type=composition_pc_EventChannelSinkConnector, multiplicity=Multiplicity(0, 1))
    }
)
closedWorkload_PCMRandomVariable1: BinaryAssociation = BinaryAssociation(
    name="closedWorkload_PCMRandomVariable1",
    ends={
        Property(name="ClosedWorkload", type=pcm_pc_core_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="thinkTime_ClosedWorkload", type=ClosedWorkload, multiplicity=Multiplicity(0, 1))
    }
)
communicationLinkResourceSpecifcation_throughput_PCMRandomVariable15: BinaryAssociation = BinaryAssociation(
    name="communicationLinkResourceSpecifcation_throughput_PCMRandomVariable15",
    ends={
        Property(name="CommunicationLinkResourceSpecification", type=pcm_pc_core_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="throughput_CommunicationLinkResourceSpecification", type=CommunicationLinkResourceSpecification, multiplicity=Multiplicity(0, 1))
    }
)
processingResourceSpecification_processingRate_PCMRandomVariable16: BinaryAssociation = BinaryAssociation(
    name="processingResourceSpecification_processingRate_PCMRandomVariable16",
    ends={
        Property(name="ProcessingResourceSpecification", type=pcm_pc_core_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="processingRate_ProcessingResourceSpecification", type=ProcessingResourceSpecification, multiplicity=Multiplicity(0, 1))
    }
)
communicationLinkResourceSpecification_latency_PCMRandomVariable17: BinaryAssociation = BinaryAssociation(
    name="communicationLinkResourceSpecification_latency_PCMRandomVariable17",
    ends={
        Property(name="CommunicationLinkResourceSpecification18", type=pcm_pc_core_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="latency_CommunicationLinkResourceSpecification", type=CommunicationLinkResourceSpecification, multiplicity=Multiplicity(0, 1))
    }
)
resourceInterfaceProvidingEntity__ResourceProvidedRole19: BinaryAssociation = BinaryAssociation(
    name="resourceInterfaceProvidingEntity__ResourceProvidedRole19",
    ends={
        Property(name="ResourceInterfaceProvidingEntity", type=pcm_pc_entity_pc_ResourceProvidedRole, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceProvidedRoles__ResourceInterfaceProvidingEntity", type=entity_pc_ResourceInterfaceProvidingEntity, multiplicity=Multiplicity(0, 1))
    }
)
providedResourceInterface__ResourceProvidedRole20: BinaryAssociation = BinaryAssociation(
    name="providedResourceInterface__ResourceProvidedRole20",
    ends={
        Property(name="ResourceInterface", type=pcm_pc_entity_pc_ResourceProvidedRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_entity_pc_ResourceProvidedRole", type=ResourceInterface, multiplicity=Multiplicity(0, 1))
    }
)
assemblyEventConnector__FilterCondition11: BinaryAssociation = BinaryAssociation(
    name="assemblyEventConnector__FilterCondition11",
    ends={
        Property(name="AssemblyEventConnector", type=pcm_pc_core_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="filterCondition__AssemblyEventConnector", type=composition_pc_AssemblyEventConnector, multiplicity=Multiplicity(0, 1))
    }
)
loop_LoopIteration12: BinaryAssociation = BinaryAssociation(
    name="loop_LoopIteration12",
    ends={
        Property(name="Loop", type=pcm_pc_core_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="loopIteration_Loop", type=Loop, multiplicity=Multiplicity(0, 1))
    }
)
openWorkload_PCMRandomVariable13: BinaryAssociation = BinaryAssociation(
    name="openWorkload_PCMRandomVariable13",
    ends={
        Property(name="OpenWorkload", type=pcm_pc_core_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="interArrivalTime_OpenWorkload", type=OpenWorkload, multiplicity=Multiplicity(0, 1))
    }
)
providedRoles_InterfaceProvidingEntity21: BinaryAssociation = BinaryAssociation(
    name="providedRoles_InterfaceProvidingEntity21",
    ends={
        Property(name="ProvidedRole", type=pcm_pc_entity_pc_InterfaceProvidingEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="providingEntity_ProvidedRole", type=ProvidedRole, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
delay_TimeSpecification14: BinaryAssociation = BinaryAssociation(
    name="delay_TimeSpecification14",
    ends={
        Property(name="Delay", type=pcm_pc_core_pc_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="timeSpecification_Delay", type=Delay, multiplicity=Multiplicity(0, 1))
    }
)
requiredRoles_InterfaceRequiringEntity22: BinaryAssociation = BinaryAssociation(
    name="requiredRoles_InterfaceRequiringEntity22",
    ends={
        Property(name="RequiredRole", type=pcm_pc_entity_pc_InterfaceRequiringEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="requiringEntity_RequiredRole", type=RequiredRole, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceRequiredRoles__ResourceInterfaceRequiringEntity23: BinaryAssociation = BinaryAssociation(
    name="resourceRequiredRoles__ResourceInterfaceRequiringEntity23",
    ends={
        Property(name="ResourceRequiredRole", type=pcm_pc_entity_pc_ResourceInterfaceRequiringEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceInterfaceRequiringEntity__ResourceRequiredRole", type=entity_pc_ResourceRequiredRole, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredResourceInterface__ResourceRequiredRole24: BinaryAssociation = BinaryAssociation(
    name="requiredResourceInterface__ResourceRequiredRole24",
    ends={
        Property(name="ResourceInterface25", type=pcm_pc_entity_pc_ResourceRequiredRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_entity_pc_ResourceRequiredRole", type=ResourceInterface, multiplicity=Multiplicity(0, 1))
    }
)
resourceInterfaceRequiringEntity__ResourceRequiredRole26: BinaryAssociation = BinaryAssociation(
    name="resourceInterfaceRequiringEntity__ResourceRequiredRole26",
    ends={
        Property(name="ResourceInterfaceRequiringEntity", type=pcm_pc_entity_pc_ResourceRequiredRole, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceRequiredRoles__ResourceInterfaceRequiringEntity", type=entity_pc_ResourceInterfaceRequiringEntity, multiplicity=Multiplicity(0, 1))
    }
)
resourceProvidedRoles__ResourceInterfaceProvidingEntity27: BinaryAssociation = BinaryAssociation(
    name="resourceProvidedRoles__ResourceInterfaceProvidingEntity27",
    ends={
        Property(name="ResourceProvidedRole", type=pcm_pc_entity_pc_ResourceInterfaceProvidingEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceInterfaceProvidingEntity__ResourceProvidedRole", type=entity_pc_ResourceProvidedRole, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentStructure__Connector28: BinaryAssociation = BinaryAssociation(
    name="parentStructure__Connector28",
    ends={
        Property(name="ComposedStructure", type=pcm_pc_composition_pc_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="connectors__ComposedStructure", type=composition_pc_ComposedStructure, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContexts__ComposedStructure29: BinaryAssociation = BinaryAssociation(
    name="assemblyContexts__ComposedStructure29",
    ends={
        Property(name="AssemblyContext", type=pcm_pc_composition_pc_ComposedStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="parentStructure__AssemblyContext", type=composition_pc_AssemblyContext, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceRequiredDelegationConnectors_ComposedStructure30: BinaryAssociation = BinaryAssociation(
    name="resourceRequiredDelegationConnectors_ComposedStructure30",
    ends={
        Property(name="ResourceRequiredDelegationConnector", type=pcm_pc_composition_pc_ComposedStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="parentStructure_ResourceRequiredDelegationConnector", type=composition_pc_ResourceRequiredDelegationConnector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eventChannel__ComposedStructure31: BinaryAssociation = BinaryAssociation(
    name="eventChannel__ComposedStructure31",
    ends={
        Property(name="EventChannel", type=pcm_pc_composition_pc_ComposedStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="parentStructure__EventChannel", type=composition_pc_EventChannel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connectors__ComposedStructure32: BinaryAssociation = BinaryAssociation(
    name="connectors__ComposedStructure32",
    ends={
        Property(name="Connector", type=pcm_pc_composition_pc_ComposedStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="parentStructure__Connector", type=composition_pc_Connector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eventGroup__EventChannel39: BinaryAssociation = BinaryAssociation(
    name="eventGroup__EventChannel39",
    ends={
        Property(name="EventGroup", type=pcm_pc_composition_pc_EventChannel, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_composition_pc_EventChannel", type=EventGroup, multiplicity=Multiplicity(0, 1))
    }
)
eventChannelSourceConnector__EventChannel40: BinaryAssociation = BinaryAssociation(
    name="eventChannelSourceConnector__EventChannel40",
    ends={
        Property(name="EventChannelSourceConnector", type=pcm_pc_composition_pc_EventChannel, multiplicity=Multiplicity(1, 1)),
        Property(name="eventChannel__EventChannelSourceConnector", type=composition_pc_EventChannelSourceConnector, multiplicity=Multiplicity(0, 9999))
    }
)
eventChannelSinkConnector__EventChannel41: BinaryAssociation = BinaryAssociation(
    name="eventChannelSinkConnector__EventChannel41",
    ends={
        Property(name="EventChannelSinkConnector42", type=pcm_pc_composition_pc_EventChannel, multiplicity=Multiplicity(1, 1)),
        Property(name="eventChannel__EventChannelSinkConnector", type=composition_pc_EventChannelSinkConnector, multiplicity=Multiplicity(0, 9999))
    }
)
parentStructure__EventChannel43: BinaryAssociation = BinaryAssociation(
    name="parentStructure__EventChannel43",
    ends={
        Property(name="ComposedStructure44", type=pcm_pc_composition_pc_EventChannel, multiplicity=Multiplicity(1, 1)),
        Property(name="eventChannel__ComposedStructure", type=composition_pc_ComposedStructure, multiplicity=Multiplicity(0, 1))
    }
)
sourceRole__EventChannelSourceRole45: BinaryAssociation = BinaryAssociation(
    name="sourceRole__EventChannelSourceRole45",
    ends={
        Property(name="SourceRole", type=pcm_pc_composition_pc_EventChannelSourceConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_composition_pc_EventChannelSourceConnector", type=SourceRole, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext__EventChannelSourceConnector46: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__EventChannelSourceConnector46",
    ends={
        Property(name="composition_pc_AssemblyContext", type=pcm_pc_composition_pc_EventChannelSourceConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_composition_pc_EventChannelSourceConnector47", type=composition_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
eventChannel__EventChannelSourceConnector48: BinaryAssociation = BinaryAssociation(
    name="eventChannel__EventChannelSourceConnector48",
    ends={
        Property(name="EventChannel49", type=pcm_pc_composition_pc_EventChannelSourceConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="eventChannelSourceConnector__EventChannel", type=composition_pc_EventChannel, multiplicity=Multiplicity(0, 1))
    }
)
sinkRole__EventChannelSinkConnector50: BinaryAssociation = BinaryAssociation(
    name="sinkRole__EventChannelSinkConnector50",
    ends={
        Property(name="SinkRole", type=pcm_pc_composition_pc_EventChannelSinkConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_composition_pc_EventChannelSinkConnector", type=SinkRole, multiplicity=Multiplicity(0, 1))
    }
)
filterCondition__EventChannelSinkConnector51: BinaryAssociation = BinaryAssociation(
    name="filterCondition__EventChannelSinkConnector51",
    ends={
        Property(name="PCMRandomVariable", type=pcm_pc_composition_pc_EventChannelSinkConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="eventChannelSinkConnector__FilterCondition", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assemblyContext__EventChannelSinkConnector52: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__EventChannelSinkConnector52",
    ends={
        Property(name="composition_pc_AssemblyContext54", type=pcm_pc_composition_pc_EventChannelSinkConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_composition_pc_EventChannelSinkConnector53", type=composition_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
eventChannel__EventChannelSinkConnector55: BinaryAssociation = BinaryAssociation(
    name="eventChannel__EventChannelSinkConnector55",
    ends={
        Property(name="EventChannel56", type=pcm_pc_composition_pc_EventChannelSinkConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="eventChannelSinkConnector__EventChannel", type=composition_pc_EventChannel, multiplicity=Multiplicity(0, 1))
    }
)
innerResourceRequiredRole_ResourceRequiredDelegationConnector33: BinaryAssociation = BinaryAssociation(
    name="innerResourceRequiredRole_ResourceRequiredDelegationConnector33",
    ends={
        Property(name="entity_pc_ResourceRequiredRole", type=pcm_pc_composition_pc_ResourceRequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_composition_pc_ResourceRequiredDelegationConnector", type=entity_pc_ResourceRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
outerResourceRequiredRole_ResourceRequiredDelegationConnector34: BinaryAssociation = BinaryAssociation(
    name="outerResourceRequiredRole_ResourceRequiredDelegationConnector34",
    ends={
        Property(name="entity_pc_ResourceRequiredRole36", type=pcm_pc_composition_pc_ResourceRequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_composition_pc_ResourceRequiredDelegationConnector35", type=entity_pc_ResourceRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
parentStructure_ResourceRequiredDelegationConnector37: BinaryAssociation = BinaryAssociation(
    name="parentStructure_ResourceRequiredDelegationConnector37",
    ends={
        Property(name="ComposedStructure38", type=pcm_pc_composition_pc_ResourceRequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceRequiredDelegationConnectors_ComposedStructure", type=composition_pc_ComposedStructure, multiplicity=Multiplicity(0, 1))
    }
)
innerProvidedRole_ProvidedDelegationConnector57: BinaryAssociation = BinaryAssociation(
    name="innerProvidedRole_ProvidedDelegationConnector57",
    ends={
        Property(name="OperationProvidedRole", type=pcm_pc_composition_pc_ProvidedDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_composition_pc_ProvidedDelegationConnector", type=OperationProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
outerProvidedRole_ProvidedDelegationConnector58: BinaryAssociation = BinaryAssociation(
    name="outerProvidedRole_ProvidedDelegationConnector58",
    ends={
        Property(name="OperationProvidedRole60", type=pcm_pc_composition_pc_ProvidedDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_composition_pc_ProvidedDelegationConnector59", type=OperationProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext_ProvidedDelegationConnector61: BinaryAssociation = BinaryAssociation(
    name="assemblyContext_ProvidedDelegationConnector61",
    ends={
        Property(name="composition_pc_AssemblyContext63", type=pcm_pc_composition_pc_ProvidedDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_composition_pc_ProvidedDelegationConnector62", type=composition_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
innerRequiredRole_RequiredDelegationConnector64: BinaryAssociation = BinaryAssociation(
    name="innerRequiredRole_RequiredDelegationConnector64",
    ends={
        Property(name="OperationRequiredRole", type=pcm_pc_composition_pc_RequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_composition_pc_RequiredDelegationConnector", type=OperationRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
outerRequiredRole_RequiredDelegationConnector65: BinaryAssociation = BinaryAssociation(
    name="outerRequiredRole_RequiredDelegationConnector65",
    ends={
        Property(name="OperationRequiredRole67", type=pcm_pc_composition_pc_RequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_composition_pc_RequiredDelegationConnector66", type=OperationRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
requiringAssemblyContext_AssemblyConnector71: BinaryAssociation = BinaryAssociation(
    name="requiringAssemblyContext_AssemblyConnector71",
    ends={
        Property(name="composition_pc_AssemblyContext72", type=pcm_pc_composition_pc_AssemblyConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_composition_pc_AssemblyConnector", type=composition_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
providingAssemblyContext_AssemblyConnector73: BinaryAssociation = BinaryAssociation(
    name="providingAssemblyContext_AssemblyConnector73",
    ends={
        Property(name="composition_pc_AssemblyContext75", type=pcm_pc_composition_pc_AssemblyConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_composition_pc_AssemblyConnector74", type=composition_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
providedRole_AssemblyConnector76: BinaryAssociation = BinaryAssociation(
    name="providedRole_AssemblyConnector76",
    ends={
        Property(name="OperationProvidedRole78", type=pcm_pc_composition_pc_AssemblyConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_composition_pc_AssemblyConnector77", type=OperationProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
requiredRole_AssemblyConnector79: BinaryAssociation = BinaryAssociation(
    name="requiredRole_AssemblyConnector79",
    ends={
        Property(name="OperationRequiredRole81", type=pcm_pc_composition_pc_AssemblyConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_composition_pc_AssemblyConnector80", type=OperationRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
sinkRole__AssemblyEventConnector82: BinaryAssociation = BinaryAssociation(
    name="sinkRole__AssemblyEventConnector82",
    ends={
        Property(name="SinkRole83", type=pcm_pc_composition_pc_AssemblyEventConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_composition_pc_AssemblyEventConnector", type=SinkRole, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext_RequiredDelegationConnector68: BinaryAssociation = BinaryAssociation(
    name="assemblyContext_RequiredDelegationConnector68",
    ends={
        Property(name="composition_pc_AssemblyContext70", type=pcm_pc_composition_pc_RequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_composition_pc_RequiredDelegationConnector69", type=composition_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
filterCondition__AssemblyEventConnector93: BinaryAssociation = BinaryAssociation(
    name="filterCondition__AssemblyEventConnector93",
    ends={
        Property(name="PCMRandomVariable94", type=pcm_pc_composition_pc_AssemblyEventConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="assemblyEventConnector__FilterCondition", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
innerSourceRole__SourceRole95: BinaryAssociation = BinaryAssociation(
    name="innerSourceRole__SourceRole95",
    ends={
        Property(name="SourceRole96", type=pcm_pc_composition_pc_SourceDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_composition_pc_SourceDelegationConnector", type=SourceRole, multiplicity=Multiplicity(0, 1))
    }
)
outerSourceRole__SourceRole97: BinaryAssociation = BinaryAssociation(
    name="outerSourceRole__SourceRole97",
    ends={
        Property(name="SourceRole99", type=pcm_pc_composition_pc_SourceDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_composition_pc_SourceDelegationConnector98", type=SourceRole, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext__SourceDelegationConnector100: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__SourceDelegationConnector100",
    ends={
        Property(name="composition_pc_AssemblyContext102", type=pcm_pc_composition_pc_SourceDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_composition_pc_SourceDelegationConnector101", type=composition_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext__SinkDelegationConnector103: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__SinkDelegationConnector103",
    ends={
        Property(name="composition_pc_AssemblyContext104", type=pcm_pc_composition_pc_SinkDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_composition_pc_SinkDelegationConnector", type=composition_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
innerSinkRole__SinkRole105: BinaryAssociation = BinaryAssociation(
    name="innerSinkRole__SinkRole105",
    ends={
        Property(name="SinkRole107", type=pcm_pc_composition_pc_SinkDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_composition_pc_SinkDelegationConnector106", type=SinkRole, multiplicity=Multiplicity(0, 1))
    }
)
outerSinkRole__SinkRole108: BinaryAssociation = BinaryAssociation(
    name="outerSinkRole__SinkRole108",
    ends={
        Property(name="SinkRole110", type=pcm_pc_composition_pc_SinkDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_composition_pc_SinkDelegationConnector109", type=SinkRole, multiplicity=Multiplicity(0, 1))
    }
)
providedRole__AssemblyInfrastructureConnector111: BinaryAssociation = BinaryAssociation(
    name="providedRole__AssemblyInfrastructureConnector111",
    ends={
        Property(name="InfrastructureProvidedRole", type=pcm_pc_composition_pc_AssemblyInfrastructureConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_composition_pc_AssemblyInfrastructureConnector", type=InfrastructureProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
requiredRole__AssemblyInfrastructureConnector112: BinaryAssociation = BinaryAssociation(
    name="requiredRole__AssemblyInfrastructureConnector112",
    ends={
        Property(name="InfrastructureRequiredRole", type=pcm_pc_composition_pc_AssemblyInfrastructureConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_composition_pc_AssemblyInfrastructureConnector113", type=InfrastructureRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
providingAssemblyContext__AssemblyInfrastructureConnector114: BinaryAssociation = BinaryAssociation(
    name="providingAssemblyContext__AssemblyInfrastructureConnector114",
    ends={
        Property(name="composition_pc_AssemblyContext116", type=pcm_pc_composition_pc_AssemblyInfrastructureConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_composition_pc_AssemblyInfrastructureConnector115", type=composition_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
requiringAssemblyContext__AssemblyInfrastructureConnector117: BinaryAssociation = BinaryAssociation(
    name="requiringAssemblyContext__AssemblyInfrastructureConnector117",
    ends={
        Property(name="composition_pc_AssemblyContext119", type=pcm_pc_composition_pc_AssemblyInfrastructureConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_composition_pc_AssemblyInfrastructureConnector118", type=composition_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
innerProvidedRole__ProvidedInfrastructureDelegationConnector120: BinaryAssociation = BinaryAssociation(
    name="innerProvidedRole__ProvidedInfrastructureDelegationConnector120",
    ends={
        Property(name="InfrastructureProvidedRole121", type=pcm_pc_composition_pc_ProvidedInfrastructureDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_composition_pc_ProvidedInfrastructureDelegationConnector", type=InfrastructureProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
outerProvidedRole__ProvidedInfrastructureDelegationConnector122: BinaryAssociation = BinaryAssociation(
    name="outerProvidedRole__ProvidedInfrastructureDelegationConnector122",
    ends={
        Property(name="InfrastructureProvidedRole124", type=pcm_pc_composition_pc_ProvidedInfrastructureDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_composition_pc_ProvidedInfrastructureDelegationConnector123", type=InfrastructureProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext__ProvidedInfrastructureDelegationConnector125: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__ProvidedInfrastructureDelegationConnector125",
    ends={
        Property(name="composition_pc_AssemblyContext127", type=pcm_pc_composition_pc_ProvidedInfrastructureDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_composition_pc_ProvidedInfrastructureDelegationConnector126", type=composition_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
sourceRole__AssemblyEventConnector84: BinaryAssociation = BinaryAssociation(
    name="sourceRole__AssemblyEventConnector84",
    ends={
        Property(name="SourceRole86", type=pcm_pc_composition_pc_AssemblyEventConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_composition_pc_AssemblyEventConnector85", type=SourceRole, multiplicity=Multiplicity(0, 1))
    }
)
sinkAssemblyContext__AssemblyEventConnector87: BinaryAssociation = BinaryAssociation(
    name="sinkAssemblyContext__AssemblyEventConnector87",
    ends={
        Property(name="composition_pc_AssemblyContext89", type=pcm_pc_composition_pc_AssemblyEventConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_composition_pc_AssemblyEventConnector88", type=composition_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
sourceAssemblyContext__AssemblyEventConnector90: BinaryAssociation = BinaryAssociation(
    name="sourceAssemblyContext__AssemblyEventConnector90",
    ends={
        Property(name="composition_pc_AssemblyContext92", type=pcm_pc_composition_pc_AssemblyEventConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_composition_pc_AssemblyEventConnector91", type=composition_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext__RequiredResourceDelegationConnector136: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__RequiredResourceDelegationConnector136",
    ends={
        Property(name="composition_pc_AssemblyContext137", type=pcm_pc_composition_pc_RequiredResourceDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_composition_pc_RequiredResourceDelegationConnector", type=composition_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
innerRequiredRole__RequiredResourceDelegationConnector138: BinaryAssociation = BinaryAssociation(
    name="innerRequiredRole__RequiredResourceDelegationConnector138",
    ends={
        Property(name="entity_pc_ResourceRequiredRole140", type=pcm_pc_composition_pc_RequiredResourceDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_composition_pc_RequiredResourceDelegationConnector139", type=entity_pc_ResourceRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
outerRequiredRole__RequiredResourceDelegationConnector141: BinaryAssociation = BinaryAssociation(
    name="outerRequiredRole__RequiredResourceDelegationConnector141",
    ends={
        Property(name="entity_pc_ResourceRequiredRole143", type=pcm_pc_composition_pc_RequiredResourceDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_composition_pc_RequiredResourceDelegationConnector142", type=entity_pc_ResourceRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
parentStructure__AssemblyContext144: BinaryAssociation = BinaryAssociation(
    name="parentStructure__AssemblyContext144",
    ends={
        Property(name="ComposedStructure145", type=pcm_pc_composition_pc_AssemblyContext, multiplicity=Multiplicity(1, 1)),
        Property(name="assemblyContexts__ComposedStructure", type=composition_pc_ComposedStructure, multiplicity=Multiplicity(0, 1))
    }
)
encapsulatedComponent__AssemblyContext146: BinaryAssociation = BinaryAssociation(
    name="encapsulatedComponent__AssemblyContext146",
    ends={
        Property(name="RepositoryComponent", type=pcm_pc_composition_pc_AssemblyContext, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_composition_pc_AssemblyContext", type=RepositoryComponent, multiplicity=Multiplicity(0, 1))
    }
)
configParameterUsages__AssemblyContext147: BinaryAssociation = BinaryAssociation(
    name="configParameterUsages__AssemblyContext147",
    ends={
        Property(name="VariableUsage", type=pcm_pc_composition_pc_AssemblyContext, multiplicity=Multiplicity(1, 1)),
        Property(name="assemblyContext__VariableUsage", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
usageScenario_Workload148: BinaryAssociation = BinaryAssociation(
    name="usageScenario_Workload148",
    ends={
        Property(name="UsageScenario", type=pcm_pc_usagemodel_pc_Workload, multiplicity=Multiplicity(1, 1)),
        Property(name="workload_UsageScenario", type=UsageScenario, multiplicity=Multiplicity(0, 1))
    }
)
usageModel_UsageScenario149: BinaryAssociation = BinaryAssociation(
    name="usageModel_UsageScenario149",
    ends={
        Property(name="UsageModel", type=pcm_pc_usagemodel_pc_UsageScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="usageScenario_UsageModel", type=UsageModel, multiplicity=Multiplicity(0, 1))
    }
)
scenarioBehaviour_UsageScenario150: BinaryAssociation = BinaryAssociation(
    name="scenarioBehaviour_UsageScenario150",
    ends={
        Property(name="ScenarioBehaviour", type=pcm_pc_usagemodel_pc_UsageScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="usageScenario_SenarioBehaviour", type=ScenarioBehaviour, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
workload_UsageScenario151: BinaryAssociation = BinaryAssociation(
    name="workload_UsageScenario151",
    ends={
        Property(name="Workload", type=pcm_pc_usagemodel_pc_UsageScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="usageScenario_Workload", type=Workload, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
innerRequiredRole__RequiredInfrastructureDelegationConnector128: BinaryAssociation = BinaryAssociation(
    name="innerRequiredRole__RequiredInfrastructureDelegationConnector128",
    ends={
        Property(name="InfrastructureRequiredRole129", type=pcm_pc_composition_pc_RequiredInfrastructureDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_composition_pc_RequiredInfrastructureDelegationConnector", type=InfrastructureRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
outerRequiredRole__RequiredInfrastructureDelegationConnector130: BinaryAssociation = BinaryAssociation(
    name="outerRequiredRole__RequiredInfrastructureDelegationConnector130",
    ends={
        Property(name="InfrastructureRequiredRole132", type=pcm_pc_composition_pc_RequiredInfrastructureDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_composition_pc_RequiredInfrastructureDelegationConnector131", type=InfrastructureRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext__RequiredInfrastructureDelegationConnector133: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__RequiredInfrastructureDelegationConnector133",
    ends={
        Property(name="composition_pc_AssemblyContext135", type=pcm_pc_composition_pc_RequiredInfrastructureDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_composition_pc_RequiredInfrastructureDelegationConnector134", type=composition_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
usageScenario_UsageModel158: BinaryAssociation = BinaryAssociation(
    name="usageScenario_UsageModel158",
    ends={
        Property(name="UsageScenario159", type=pcm_pc_usagemodel_pc_UsageModel, multiplicity=Multiplicity(1, 1)),
        Property(name="usageModel_UsageScenario", type=UsageScenario, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
assemblyContext_userData152: BinaryAssociation = BinaryAssociation(
    name="assemblyContext_userData152",
    ends={
        Property(name="composition_pc_AssemblyContext153", type=pcm_pc_usagemodel_pc_UserData, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_usagemodel_pc_UserData", type=composition_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
usageModel_UserData154: BinaryAssociation = BinaryAssociation(
    name="usageModel_UserData154",
    ends={
        Property(name="UsageModel155", type=pcm_pc_usagemodel_pc_UserData, multiplicity=Multiplicity(1, 1)),
        Property(name="userData_UsageModel", type=UsageModel, multiplicity=Multiplicity(0, 1))
    }
)
userDataParameterUsages_UserData156: BinaryAssociation = BinaryAssociation(
    name="userDataParameterUsages_UserData156",
    ends={
        Property(name="VariableUsage157", type=pcm_pc_usagemodel_pc_UserData, multiplicity=Multiplicity(1, 1)),
        Property(name="userData_VariableUsage", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
providedRole_EntryLevelSystemCall161: BinaryAssociation = BinaryAssociation(
    name="providedRole_EntryLevelSystemCall161",
    ends={
        Property(name="OperationProvidedRole162", type=pcm_pc_usagemodel_pc_EntryLevelSystemCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_usagemodel_pc_EntryLevelSystemCall", type=OperationProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
operationSignature__EntryLevelSystemCall163: BinaryAssociation = BinaryAssociation(
    name="operationSignature__EntryLevelSystemCall163",
    ends={
        Property(name="OperationSignature", type=pcm_pc_usagemodel_pc_EntryLevelSystemCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_usagemodel_pc_EntryLevelSystemCall164", type=OperationSignature, multiplicity=Multiplicity(0, 1))
    }
)
outputParameterUsages_EntryLevelSystemCall165: BinaryAssociation = BinaryAssociation(
    name="outputParameterUsages_EntryLevelSystemCall165",
    ends={
        Property(name="VariableUsage166", type=pcm_pc_usagemodel_pc_EntryLevelSystemCall, multiplicity=Multiplicity(1, 1)),
        Property(name="entryLevelSystemCall_OutputParameterUsage", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputParameterUsages_EntryLevelSystemCall167: BinaryAssociation = BinaryAssociation(
    name="inputParameterUsages_EntryLevelSystemCall167",
    ends={
        Property(name="VariableUsage168", type=pcm_pc_usagemodel_pc_EntryLevelSystemCall, multiplicity=Multiplicity(1, 1)),
        Property(name="entryLevelSystemCall_InputParameterUsage", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
userData_UsageModel160: BinaryAssociation = BinaryAssociation(
    name="userData_UsageModel160",
    ends={
        Property(name="UserData", type=pcm_pc_usagemodel_pc_UsageModel, multiplicity=Multiplicity(1, 1)),
        Property(name="usageModel_UserData", type=UserData, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
usageScenario_SenarioBehaviour174: BinaryAssociation = BinaryAssociation(
    name="usageScenario_SenarioBehaviour174",
    ends={
        Property(name="UsageScenario175", type=pcm_pc_usagemodel_pc_ScenarioBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="scenarioBehaviour_UsageScenario", type=UsageScenario, multiplicity=Multiplicity(0, 1))
    }
)
branchTransition_ScenarioBehaviour176: BinaryAssociation = BinaryAssociation(
    name="branchTransition_ScenarioBehaviour176",
    ends={
        Property(name="BranchTransition", type=pcm_pc_usagemodel_pc_ScenarioBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="branchedBehaviour_BranchTransition", type=BranchTransition, multiplicity=Multiplicity(0, 1))
    }
)
loop_ScenarioBehaviour177: BinaryAssociation = BinaryAssociation(
    name="loop_ScenarioBehaviour177",
    ends={
        Property(name="Loop178", type=pcm_pc_usagemodel_pc_ScenarioBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="bodyBehaviour_Loop", type=Loop, multiplicity=Multiplicity(0, 1))
    }
)
actions_ScenarioBehaviour179: BinaryAssociation = BinaryAssociation(
    name="actions_ScenarioBehaviour179",
    ends={
        Property(name="AbstractUserAction180", type=pcm_pc_usagemodel_pc_ScenarioBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="scenarioBehaviour_AbstractUserAction", type=AbstractUserAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
successor169: BinaryAssociation = BinaryAssociation(
    name="successor169",
    ends={
        Property(name="AbstractUserAction", type=pcm_pc_usagemodel_pc_AbstractUserAction, multiplicity=Multiplicity(1, 1)),
        Property(name="predecessor", type=AbstractUserAction, multiplicity=Multiplicity(0, 1))
    }
)
predecessor170: BinaryAssociation = BinaryAssociation(
    name="predecessor170",
    ends={
        Property(name="AbstractUserAction171", type=pcm_pc_usagemodel_pc_AbstractUserAction, multiplicity=Multiplicity(1, 1)),
        Property(name="successor", type=AbstractUserAction, multiplicity=Multiplicity(0, 1))
    }
)
scenarioBehaviour_AbstractUserAction172: BinaryAssociation = BinaryAssociation(
    name="scenarioBehaviour_AbstractUserAction172",
    ends={
        Property(name="ScenarioBehaviour173", type=pcm_pc_usagemodel_pc_AbstractUserAction, multiplicity=Multiplicity(1, 1)),
        Property(name="actions_ScenarioBehaviour", type=ScenarioBehaviour, multiplicity=Multiplicity(0, 1))
    }
)
branchTransitions_Branch184: BinaryAssociation = BinaryAssociation(
    name="branchTransitions_Branch184",
    ends={
        Property(name="BranchTransition185", type=pcm_pc_usagemodel_pc_Branch, multiplicity=Multiplicity(1, 1)),
        Property(name="branch_BranchTransition", type=BranchTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
loopIteration_Loop186: BinaryAssociation = BinaryAssociation(
    name="loopIteration_Loop186",
    ends={
        Property(name="PCMRandomVariable187", type=pcm_pc_usagemodel_pc_Loop, multiplicity=Multiplicity(1, 1)),
        Property(name="loop_LoopIteration", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bodyBehaviour_Loop188: BinaryAssociation = BinaryAssociation(
    name="bodyBehaviour_Loop188",
    ends={
        Property(name="ScenarioBehaviour189", type=pcm_pc_usagemodel_pc_Loop, multiplicity=Multiplicity(1, 1)),
        Property(name="loop_ScenarioBehaviour", type=ScenarioBehaviour, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
branch_BranchTransition181: BinaryAssociation = BinaryAssociation(
    name="branch_BranchTransition181",
    ends={
        Property(name="Branch", type=pcm_pc_usagemodel_pc_BranchTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="branchTransitions_Branch", type=Branch, multiplicity=Multiplicity(0, 1))
    }
)
branchedBehaviour_BranchTransition182: BinaryAssociation = BinaryAssociation(
    name="branchedBehaviour_BranchTransition182",
    ends={
        Property(name="ScenarioBehaviour183", type=pcm_pc_usagemodel_pc_BranchTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="branchTransition_ScenarioBehaviour", type=ScenarioBehaviour, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
interArrivalTime_OpenWorkload190: BinaryAssociation = BinaryAssociation(
    name="interArrivalTime_OpenWorkload190",
    ends={
        Property(name="PCMRandomVariable191", type=pcm_pc_usagemodel_pc_OpenWorkload, multiplicity=Multiplicity(1, 1)),
        Property(name="openWorkload_PCMRandomVariable", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
timeSpecification_Delay192: BinaryAssociation = BinaryAssociation(
    name="timeSpecification_Delay192",
    ends={
        Property(name="PCMRandomVariable193", type=pcm_pc_usagemodel_pc_Delay, multiplicity=Multiplicity(1, 1)),
        Property(name="delay_TimeSpecification", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thinkTime_ClosedWorkload194: BinaryAssociation = BinaryAssociation(
    name="thinkTime_ClosedWorkload194",
    ends={
        Property(name="PCMRandomVariable195", type=pcm_pc_usagemodel_pc_ClosedWorkload, multiplicity=Multiplicity(1, 1)),
        Property(name="closedWorkload_PCMRandomVariable", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resourceTimeoutFailureType__PassiveResource199: BinaryAssociation = BinaryAssociation(
    name="resourceTimeoutFailureType__PassiveResource199",
    ends={
        Property(name="ResourceTimeoutFailureType", type=pcm_pc_repository_pc_PassiveResource, multiplicity=Multiplicity(1, 1)),
        Property(name="passiveResource__ResourceTimeoutFailureType", type=ResourceTimeoutFailureType, multiplicity=Multiplicity(0, 1))
    }
)
serviceEffectSpecifications__BasicComponent200: BinaryAssociation = BinaryAssociation(
    name="serviceEffectSpecifications__BasicComponent200",
    ends={
        Property(name="ServiceEffectSpecification", type=pcm_pc_repository_pc_BasicComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="basicComponent_ServiceEffectSpecification", type=ServiceEffectSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
passiveResource_BasicComponent201: BinaryAssociation = BinaryAssociation(
    name="passiveResource_BasicComponent201",
    ends={
        Property(name="PassiveResource202", type=pcm_pc_repository_pc_BasicComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="basicComponent_PassiveResource", type=PassiveResource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
capacity_PassiveResource196: BinaryAssociation = BinaryAssociation(
    name="capacity_PassiveResource196",
    ends={
        Property(name="PCMRandomVariable197", type=pcm_pc_repository_pc_PassiveResource, multiplicity=Multiplicity(1, 1)),
        Property(name="passiveResource_capacity_PCMRandomVariable", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
basicComponent_PassiveResource198: BinaryAssociation = BinaryAssociation(
    name="basicComponent_PassiveResource198",
    ends={
        Property(name="BasicComponent", type=pcm_pc_repository_pc_PassiveResource, multiplicity=Multiplicity(1, 1)),
        Property(name="passiveResource_BasicComponent", type=BasicComponent, multiplicity=Multiplicity(0, 1))
    }
)
parentCompleteComponentTypes203: BinaryAssociation = BinaryAssociation(
    name="parentCompleteComponentTypes203",
    ends={
        Property(name="CompleteComponentType", type=pcm_pc_repository_pc_ImplementationComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_repository_pc_ImplementationComponentType", type=CompleteComponentType, multiplicity=Multiplicity(0, 9999))
    }
)
componentParameterUsage_ImplementationComponentType204: BinaryAssociation = BinaryAssociation(
    name="componentParameterUsage_ImplementationComponentType204",
    ends={
        Property(name="VariableUsage206", type=pcm_pc_repository_pc_ImplementationComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_repository_pc_ImplementationComponentType205", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
repository__RepositoryComponent207: BinaryAssociation = BinaryAssociation(
    name="repository__RepositoryComponent207",
    ends={
        Property(name="Repository", type=pcm_pc_repository_pc_RepositoryComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="components__Repository", type=Repository, multiplicity=Multiplicity(0, 1))
    }
)
providingEntity_ProvidedRole208: BinaryAssociation = BinaryAssociation(
    name="providingEntity_ProvidedRole208",
    ends={
        Property(name="InterfaceProvidingEntity", type=pcm_pc_repository_pc_ProvidedRole, multiplicity=Multiplicity(1, 1)),
        Property(name="providedRoles_InterfaceProvidingEntity", type=entity_pc_InterfaceProvidingEntity, multiplicity=Multiplicity(0, 1))
    }
)
dataType__Parameter209: BinaryAssociation = BinaryAssociation(
    name="dataType__Parameter209",
    ends={
        Property(name="DataType", type=pcm_pc_repository_pc_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_repository_pc_Parameter", type=DataType, multiplicity=Multiplicity(0, 1))
    }
)
eventType__Parameter213: BinaryAssociation = BinaryAssociation(
    name="eventType__Parameter213",
    ends={
        Property(name="EventType", type=pcm_pc_repository_pc_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameter__EventType", type=EventType, multiplicity=Multiplicity(0, 1))
    }
)
resourceSignature__Parameter214: BinaryAssociation = BinaryAssociation(
    name="resourceSignature__Parameter214",
    ends={
        Property(name="ResourceSignature", type=pcm_pc_repository_pc_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameter__ResourceSignature", type=ResourceSignature, multiplicity=Multiplicity(0, 1))
    }
)
repository__DataType215: BinaryAssociation = BinaryAssociation(
    name="repository__DataType215",
    ends={
        Property(name="Repository216", type=pcm_pc_repository_pc_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="dataTypes__Repository", type=Repository, multiplicity=Multiplicity(0, 1))
    }
)
components__Repository217: BinaryAssociation = BinaryAssociation(
    name="components__Repository217",
    ends={
        Property(name="RepositoryComponent218", type=pcm_pc_repository_pc_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="repository__RepositoryComponent", type=RepositoryComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
interfaces__Repository219: BinaryAssociation = BinaryAssociation(
    name="interfaces__Repository219",
    ends={
        Property(name="Interface", type=pcm_pc_repository_pc_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="repository__Interface", type=Interface, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
failureTypes__Repository220: BinaryAssociation = BinaryAssociation(
    name="failureTypes__Repository220",
    ends={
        Property(name="FailureType", type=pcm_pc_repository_pc_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="repository__FailureType", type=FailureType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataTypes__Repository221: BinaryAssociation = BinaryAssociation(
    name="dataTypes__Repository221",
    ends={
        Property(name="DataType222", type=pcm_pc_repository_pc_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="repository__DataType", type=DataType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
infrastructureSignature__Parameter210: BinaryAssociation = BinaryAssociation(
    name="infrastructureSignature__Parameter210",
    ends={
        Property(name="InfrastructureSignature", type=pcm_pc_repository_pc_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameters__InfrastructureSignature", type=InfrastructureSignature, multiplicity=Multiplicity(0, 1))
    }
)
operationSignature__Parameter211: BinaryAssociation = BinaryAssociation(
    name="operationSignature__Parameter211",
    ends={
        Property(name="OperationSignature212", type=pcm_pc_repository_pc_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameters__OperationSignature", type=OperationSignature, multiplicity=Multiplicity(0, 1))
    }
)
protocols__Interface225: BinaryAssociation = BinaryAssociation(
    name="protocols__Interface225",
    ends={
        Property(name="Protocol", type=pcm_pc_repository_pc_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_repository_pc_Interface226", type=Protocol, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredCharacterisations227: BinaryAssociation = BinaryAssociation(
    name="requiredCharacterisations227",
    ends={
        Property(name="RequiredCharacterisation", type=pcm_pc_repository_pc_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="interface_RequiredCharacterisation", type=RequiredCharacterisation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
repository__Interface228: BinaryAssociation = BinaryAssociation(
    name="repository__Interface228",
    ends={
        Property(name="Repository229", type=pcm_pc_repository_pc_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="interfaces__Repository", type=Repository, multiplicity=Multiplicity(0, 1))
    }
)
parameter230: BinaryAssociation = BinaryAssociation(
    name="parameter230",
    ends={
        Property(name="Parameter", type=pcm_pc_repository_pc_RequiredCharacterisation, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_repository_pc_RequiredCharacterisation", type=Parameter_, multiplicity=Multiplicity(0, 1))
    }
)
interface_RequiredCharacterisation231: BinaryAssociation = BinaryAssociation(
    name="interface_RequiredCharacterisation231",
    ends={
        Property(name="Interface232", type=pcm_pc_repository_pc_RequiredCharacterisation, multiplicity=Multiplicity(1, 1)),
        Property(name="requiredCharacterisations", type=Interface, multiplicity=Multiplicity(0, 1))
    }
)
eventTypes__EventGroup233: BinaryAssociation = BinaryAssociation(
    name="eventTypes__EventGroup233",
    ends={
        Property(name="EventType234", type=pcm_pc_repository_pc_EventGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="eventGroup__EventType", type=EventType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameter__EventType235: BinaryAssociation = BinaryAssociation(
    name="parameter__EventType235",
    ends={
        Property(name="Parameter236", type=pcm_pc_repository_pc_EventType, multiplicity=Multiplicity(1, 1)),
        Property(name="eventType__Parameter", type=Parameter_, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eventGroup__EventType237: BinaryAssociation = BinaryAssociation(
    name="eventGroup__EventType237",
    ends={
        Property(name="EventGroup238", type=pcm_pc_repository_pc_EventType, multiplicity=Multiplicity(1, 1)),
        Property(name="eventTypes__EventGroup", type=EventGroup, multiplicity=Multiplicity(0, 1))
    }
)
exceptions__Signature239: BinaryAssociation = BinaryAssociation(
    name="exceptions__Signature239",
    ends={
        Property(name="ExceptionType", type=pcm_pc_repository_pc_Signature, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_repository_pc_Signature", type=ExceptionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
failureType240: BinaryAssociation = BinaryAssociation(
    name="failureType240",
    ends={
        Property(name="FailureType242", type=pcm_pc_repository_pc_Signature, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_repository_pc_Signature241", type=FailureType, multiplicity=Multiplicity(0, 9999))
    }
)
parentInterfaces__Interface223: BinaryAssociation = BinaryAssociation(
    name="parentInterfaces__Interface223",
    ends={
        Property(name="Interface224", type=pcm_pc_repository_pc_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_repository_pc_Interface", type=Interface, multiplicity=Multiplicity(0, 9999))
    }
)
parameters__InfrastructureSignature243: BinaryAssociation = BinaryAssociation(
    name="parameters__InfrastructureSignature243",
    ends={
        Property(name="Parameter244", type=pcm_pc_repository_pc_InfrastructureSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="infrastructureSignature__Parameter", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
infrastructureInterface__InfrastructureSignature245: BinaryAssociation = BinaryAssociation(
    name="infrastructureInterface__InfrastructureSignature245",
    ends={
        Property(name="InfrastructureInterface", type=pcm_pc_repository_pc_InfrastructureSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="infrastructureSignatures__InfrastructureInterface", type=InfrastructureInterface, multiplicity=Multiplicity(0, 1))
    }
)
infrastructureSignatures__InfrastructureInterface246: BinaryAssociation = BinaryAssociation(
    name="infrastructureSignatures__InfrastructureInterface246",
    ends={
        Property(name="InfrastructureSignature247", type=pcm_pc_repository_pc_InfrastructureInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="infrastructureInterface__InfrastructureSignature", type=InfrastructureSignature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredInterface__InfrastructureRequiredRole248: BinaryAssociation = BinaryAssociation(
    name="requiredInterface__InfrastructureRequiredRole248",
    ends={
        Property(name="InfrastructureInterface249", type=pcm_pc_repository_pc_InfrastructureRequiredRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_repository_pc_InfrastructureRequiredRole", type=InfrastructureInterface, multiplicity=Multiplicity(0, 1))
    }
)
requiringEntity_RequiredRole250: BinaryAssociation = BinaryAssociation(
    name="requiringEntity_RequiredRole250",
    ends={
        Property(name="InterfaceRequiringEntity", type=pcm_pc_repository_pc_RequiredRole, multiplicity=Multiplicity(1, 1)),
        Property(name="requiredRoles_InterfaceRequiringEntity", type=entity_pc_InterfaceRequiringEntity, multiplicity=Multiplicity(0, 1))
    }
)
interface__OperationSignature251: BinaryAssociation = BinaryAssociation(
    name="interface__OperationSignature251",
    ends={
        Property(name="OperationInterface", type=pcm_pc_repository_pc_OperationSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="signatures__OperationInterface", type=OperationInterface, multiplicity=Multiplicity(0, 1))
    }
)
parameters__OperationSignature252: BinaryAssociation = BinaryAssociation(
    name="parameters__OperationSignature252",
    ends={
        Property(name="Parameter253", type=pcm_pc_repository_pc_OperationSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="operationSignature__Parameter", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
signatures__OperationInterface256: BinaryAssociation = BinaryAssociation(
    name="signatures__OperationInterface256",
    ends={
        Property(name="OperationSignature257", type=pcm_pc_repository_pc_OperationInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="interface__OperationSignature", type=OperationSignature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredInterface__OperationRequiredRole258: BinaryAssociation = BinaryAssociation(
    name="requiredInterface__OperationRequiredRole258",
    ends={
        Property(name="OperationInterface259", type=pcm_pc_repository_pc_OperationRequiredRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_repository_pc_OperationRequiredRole", type=OperationInterface, multiplicity=Multiplicity(0, 1))
    }
)
eventGroup__SourceRole260: BinaryAssociation = BinaryAssociation(
    name="eventGroup__SourceRole260",
    ends={
        Property(name="EventGroup261", type=pcm_pc_repository_pc_SourceRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_repository_pc_SourceRole", type=EventGroup, multiplicity=Multiplicity(0, 1))
    }
)
returnType__OperationSignature254: BinaryAssociation = BinaryAssociation(
    name="returnType__OperationSignature254",
    ends={
        Property(name="DataType255", type=pcm_pc_repository_pc_OperationSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_repository_pc_OperationSignature", type=DataType, multiplicity=Multiplicity(0, 1))
    }
)
providedInterface__OperationProvidedRole264: BinaryAssociation = BinaryAssociation(
    name="providedInterface__OperationProvidedRole264",
    ends={
        Property(name="OperationInterface265", type=pcm_pc_repository_pc_OperationProvidedRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_repository_pc_OperationProvidedRole", type=OperationInterface, multiplicity=Multiplicity(0, 1))
    }
)
providedInterface__InfrastructureProvidedRole266: BinaryAssociation = BinaryAssociation(
    name="providedInterface__InfrastructureProvidedRole266",
    ends={
        Property(name="InfrastructureInterface267", type=pcm_pc_repository_pc_InfrastructureProvidedRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_repository_pc_InfrastructureProvidedRole", type=InfrastructureInterface, multiplicity=Multiplicity(0, 1))
    }
)
parentProvidesComponentTypes268: BinaryAssociation = BinaryAssociation(
    name="parentProvidesComponentTypes268",
    ends={
        Property(name="ProvidesComponentType", type=pcm_pc_repository_pc_CompleteComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_repository_pc_CompleteComponentType", type=ProvidesComponentType, multiplicity=Multiplicity(0, 9999))
    }
)
eventGroup__SinkRole262: BinaryAssociation = BinaryAssociation(
    name="eventGroup__SinkRole262",
    ends={
        Property(name="EventGroup263", type=pcm_pc_repository_pc_SinkRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_repository_pc_SinkRole", type=EventGroup, multiplicity=Multiplicity(0, 1))
    }
)
innerType_CollectionDataType269: BinaryAssociation = BinaryAssociation(
    name="innerType_CollectionDataType269",
    ends={
        Property(name="DataType270", type=pcm_pc_repository_pc_CollectionDataType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_repository_pc_CollectionDataType", type=DataType, multiplicity=Multiplicity(0, 1))
    }
)
parentType_CompositeDataType271: BinaryAssociation = BinaryAssociation(
    name="parentType_CompositeDataType271",
    ends={
        Property(name="CompositeDataType", type=pcm_pc_repository_pc_CompositeDataType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_repository_pc_CompositeDataType", type=CompositeDataType, multiplicity=Multiplicity(0, 9999))
    }
)
datatype_InnerDeclaration273: BinaryAssociation = BinaryAssociation(
    name="datatype_InnerDeclaration273",
    ends={
        Property(name="DataType274", type=pcm_pc_repository_pc_InnerDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_repository_pc_InnerDeclaration", type=DataType, multiplicity=Multiplicity(0, 1))
    }
)
compositeDataType_InnerDeclaration275: BinaryAssociation = BinaryAssociation(
    name="compositeDataType_InnerDeclaration275",
    ends={
        Property(name="CompositeDataType276", type=pcm_pc_repository_pc_InnerDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="innerDeclaration_CompositeDataType", type=CompositeDataType, multiplicity=Multiplicity(0, 1))
    }
)
parameter__ResourceSignature277: BinaryAssociation = BinaryAssociation(
    name="parameter__ResourceSignature277",
    ends={
        Property(name="Parameter278", type=pcm_pc_resourcetype_pc_ResourceSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceSignature__Parameter", type=Parameter_, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resourceInterface__ResourceSignature279: BinaryAssociation = BinaryAssociation(
    name="resourceInterface__ResourceSignature279",
    ends={
        Property(name="ResourceInterface280", type=pcm_pc_resourcetype_pc_ResourceSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceSignatures__ResourceInterface", type=ResourceInterface, multiplicity=Multiplicity(0, 1))
    }
)
hardwareInducedFailureType__ProcessingResourceType281: BinaryAssociation = BinaryAssociation(
    name="hardwareInducedFailureType__ProcessingResourceType281",
    ends={
        Property(name="HardwareInducedFailureType", type=pcm_pc_resourcetype_pc_ProcessingResourceType, multiplicity=Multiplicity(1, 1)),
        Property(name="processingResourceType__HardwareInducedFailureType", type=HardwareInducedFailureType, multiplicity=Multiplicity(0, 1))
    }
)
resourceRepository_ResourceType282: BinaryAssociation = BinaryAssociation(
    name="resourceRepository_ResourceType282",
    ends={
        Property(name="ResourceRepository", type=pcm_pc_resourcetype_pc_ResourceType, multiplicity=Multiplicity(1, 1)),
        Property(name="availableResourceTypes_ResourceRepository", type=ResourceRepository, multiplicity=Multiplicity(0, 1))
    }
)
resourceInterfaces__ResourceRepository283: BinaryAssociation = BinaryAssociation(
    name="resourceInterfaces__ResourceRepository283",
    ends={
        Property(name="ResourceInterface284", type=pcm_pc_resourcetype_pc_ResourceRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceRepository__ResourceInterface", type=ResourceInterface, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
schedulingPolicies__ResourceRepository285: BinaryAssociation = BinaryAssociation(
    name="schedulingPolicies__ResourceRepository285",
    ends={
        Property(name="SchedulingPolicy", type=pcm_pc_resourcetype_pc_ResourceRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceRepository__SchedulingPolicy", type=SchedulingPolicy, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
availableResourceTypes_ResourceRepository286: BinaryAssociation = BinaryAssociation(
    name="availableResourceTypes_ResourceRepository286",
    ends={
        Property(name="ResourceType", type=pcm_pc_resourcetype_pc_ResourceRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceRepository_ResourceType", type=ResourceType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceRepository__SchedulingPolicy287: BinaryAssociation = BinaryAssociation(
    name="resourceRepository__SchedulingPolicy287",
    ends={
        Property(name="ResourceRepository288", type=pcm_pc_resourcetype_pc_SchedulingPolicy, multiplicity=Multiplicity(1, 1)),
        Property(name="schedulingPolicies__ResourceRepository", type=ResourceRepository, multiplicity=Multiplicity(0, 1))
    }
)
innerDeclaration_CompositeDataType272: BinaryAssociation = BinaryAssociation(
    name="innerDeclaration_CompositeDataType272",
    ends={
        Property(name="InnerDeclaration", type=pcm_pc_repository_pc_CompositeDataType, multiplicity=Multiplicity(1, 1)),
        Property(name="compositeDataType_InnerDeclaration", type=InnerDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceRepository__ResourceInterface290: BinaryAssociation = BinaryAssociation(
    name="resourceRepository__ResourceInterface290",
    ends={
        Property(name="ResourceRepository291", type=pcm_pc_resourcetype_pc_ResourceInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceInterfaces__ResourceRepository", type=ResourceRepository, multiplicity=Multiplicity(0, 1))
    }
)
resourceSignatures__ResourceInterface292: BinaryAssociation = BinaryAssociation(
    name="resourceSignatures__ResourceInterface292",
    ends={
        Property(name="ResourceSignature293", type=pcm_pc_resourcetype_pc_ResourceInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceInterface__ResourceSignature", type=ResourceSignature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variableCharacterisation_VariableUsage294: BinaryAssociation = BinaryAssociation(
    name="variableCharacterisation_VariableUsage294",
    ends={
        Property(name="VariableCharacterisation295", type=pcm_pc_parameter_pc_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="variableUsage_VariableCharacterisation", type=VariableCharacterisation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
userData_VariableUsage296: BinaryAssociation = BinaryAssociation(
    name="userData_VariableUsage296",
    ends={
        Property(name="UserData297", type=pcm_pc_parameter_pc_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="userDataParameterUsages_UserData", type=UserData, multiplicity=Multiplicity(0, 1))
    }
)
callAction__VariableUsage298: BinaryAssociation = BinaryAssociation(
    name="callAction__VariableUsage298",
    ends={
        Property(name="CallAction", type=pcm_pc_parameter_pc_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="inputVariableUsages__CallAction", type=CallAction, multiplicity=Multiplicity(0, 1))
    }
)
synchronisationPoint_VariableUsage299: BinaryAssociation = BinaryAssociation(
    name="synchronisationPoint_VariableUsage299",
    ends={
        Property(name="SynchronisationPoint", type=pcm_pc_parameter_pc_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="outputParameterUsage_SynchronisationPoint", type=SynchronisationPoint, multiplicity=Multiplicity(0, 1))
    }
)
callReturnAction__VariableUsage300: BinaryAssociation = BinaryAssociation(
    name="callReturnAction__VariableUsage300",
    ends={
        Property(name="CallReturnAction", type=pcm_pc_parameter_pc_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="returnVariableUsage__CallReturnAction", type=CallReturnAction, multiplicity=Multiplicity(0, 1))
    }
)
setVariableAction_VariableUsage301: BinaryAssociation = BinaryAssociation(
    name="setVariableAction_VariableUsage301",
    ends={
        Property(name="SetVariableAction", type=pcm_pc_parameter_pc_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="localVariableUsages_SetVariableAction", type=SetVariableAction, multiplicity=Multiplicity(0, 1))
    }
)
specifiedOutputParameterAbstraction_expectedExternalOutputs_VariableUsage302: BinaryAssociation = BinaryAssociation(
    name="specifiedOutputParameterAbstraction_expectedExternalOutputs_VariableUsage302",
    ends={
        Property(name="SpecifiedOutputParameterAbstraction", type=pcm_pc_parameter_pc_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="expectedExternalOutputs_SpecifiedOutputParameterAbstraction", type=SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext__VariableUsage303: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__VariableUsage303",
    ends={
        Property(name="AssemblyContext304", type=pcm_pc_parameter_pc_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="configParameterUsages__AssemblyContext", type=composition_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
entryLevelSystemCall_InputParameterUsage305: BinaryAssociation = BinaryAssociation(
    name="entryLevelSystemCall_InputParameterUsage305",
    ends={
        Property(name="EntryLevelSystemCall", type=pcm_pc_parameter_pc_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="inputParameterUsages_EntryLevelSystemCall", type=EntryLevelSystemCall, multiplicity=Multiplicity(0, 1))
    }
)
entryLevelSystemCall_OutputParameterUsage306: BinaryAssociation = BinaryAssociation(
    name="entryLevelSystemCall_OutputParameterUsage306",
    ends={
        Property(name="EntryLevelSystemCall307", type=pcm_pc_parameter_pc_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="outputParameterUsages_EntryLevelSystemCall", type=EntryLevelSystemCall, multiplicity=Multiplicity(0, 1))
    }
)
namedReference__VariableUsage308: BinaryAssociation = BinaryAssociation(
    name="namedReference__VariableUsage308",
    ends={
        Property(name="parameter_pc_pcm_pc_AbstractNamedReference", type=pcm_pc_parameter_pc_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_parameter_pc_VariableUsage", type=parameter_pc_pcm_pc_AbstractNamedReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
networkInducedFailureType__CommunicationLinkResourceType289: BinaryAssociation = BinaryAssociation(
    name="networkInducedFailureType__CommunicationLinkResourceType289",
    ends={
        Property(name="NetworkInducedFailureType", type=pcm_pc_resourcetype_pc_CommunicationLinkResourceType, multiplicity=Multiplicity(1, 1)),
        Property(name="communicationLinkResourceType__NetworkInducedFailureType", type=NetworkInducedFailureType, multiplicity=Multiplicity(0, 1))
    }
)
variableUsage_VariableCharacterisation311: BinaryAssociation = BinaryAssociation(
    name="variableUsage_VariableCharacterisation311",
    ends={
        Property(name="VariableUsage312", type=pcm_pc_parameter_pc_VariableCharacterisation, multiplicity=Multiplicity(1, 1)),
        Property(name="variableCharacterisation_VariableUsage", type=VariableUsage, multiplicity=Multiplicity(0, 1))
    }
)
specification_VariableCharacterisation309: BinaryAssociation = BinaryAssociation(
    name="specification_VariableCharacterisation309",
    ends={
        Property(name="PCMRandomVariable310", type=pcm_pc_parameter_pc_VariableCharacterisation, multiplicity=Multiplicity(1, 1)),
        Property(name="variableCharacterisation_Specification", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
internalFailureOccurrenceDescriptions__SoftwareInducedFailureType314: BinaryAssociation = BinaryAssociation(
    name="internalFailureOccurrenceDescriptions__SoftwareInducedFailureType314",
    ends={
        Property(name="InternalFailureOccurrenceDescription", type=pcm_pc_reliability_pc_SoftwareInducedFailureType, multiplicity=Multiplicity(1, 1)),
        Property(name="softwareInducedFailureType__InternalFailureOccurrenceDescription", type=InternalFailureOccurrenceDescription, multiplicity=Multiplicity(0, 9999))
    }
)
internalAction__InternalFailureOccurrenceDescription315: BinaryAssociation = BinaryAssociation(
    name="internalAction__InternalFailureOccurrenceDescription315",
    ends={
        Property(name="InternalAction", type=pcm_pc_reliability_pc_InternalFailureOccurrenceDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="internalFailureOccurrenceDescriptions__InternalAction", type=InternalAction, multiplicity=Multiplicity(0, 1))
    }
)
softwareInducedFailureType__InternalFailureOccurrenceDescription316: BinaryAssociation = BinaryAssociation(
    name="softwareInducedFailureType__InternalFailureOccurrenceDescription316",
    ends={
        Property(name="SoftwareInducedFailureType", type=pcm_pc_reliability_pc_InternalFailureOccurrenceDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="internalFailureOccurrenceDescriptions__SoftwareInducedFailureType", type=SoftwareInducedFailureType, multiplicity=Multiplicity(0, 1))
    }
)
communicationLinkResourceType__NetworkInducedFailureType317: BinaryAssociation = BinaryAssociation(
    name="communicationLinkResourceType__NetworkInducedFailureType317",
    ends={
        Property(name="CommunicationLinkResourceType", type=pcm_pc_reliability_pc_NetworkInducedFailureType, multiplicity=Multiplicity(1, 1)),
        Property(name="networkInducedFailureType__CommunicationLinkResourceType", type=CommunicationLinkResourceType, multiplicity=Multiplicity(0, 1))
    }
)
specifiedReliabilityAnnotation__ExternalFailureOccurrenceDescription318: BinaryAssociation = BinaryAssociation(
    name="specifiedReliabilityAnnotation__ExternalFailureOccurrenceDescription318",
    ends={
        Property(name="SpecifiedReliabilityAnnotation", type=pcm_pc_reliability_pc_ExternalFailureOccurrenceDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="externalFailureOccurrenceDescriptions__SpecifiedReliabilityAnnotation", type=qos_reliability_pc_SpecifiedReliabilityAnnotation, multiplicity=Multiplicity(0, 1))
    }
)
processingResourceType__HardwareInducedFailureType313: BinaryAssociation = BinaryAssociation(
    name="processingResourceType__HardwareInducedFailureType313",
    ends={
        Property(name="ProcessingResourceType", type=pcm_pc_reliability_pc_HardwareInducedFailureType, multiplicity=Multiplicity(1, 1)),
        Property(name="hardwareInducedFailureType__ProcessingResourceType", type=ProcessingResourceType, multiplicity=Multiplicity(0, 1))
    }
)
failureType__ExternalFailureOccurrenceDescription319: BinaryAssociation = BinaryAssociation(
    name="failureType__ExternalFailureOccurrenceDescription319",
    ends={
        Property(name="FailureType320", type=pcm_pc_reliability_pc_ExternalFailureOccurrenceDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_reliability_pc_ExternalFailureOccurrenceDescription", type=FailureType, multiplicity=Multiplicity(0, 1))
    }
)
passiveResource__ResourceTimeoutFailureType321: BinaryAssociation = BinaryAssociation(
    name="passiveResource__ResourceTimeoutFailureType321",
    ends={
        Property(name="PassiveResource322", type=pcm_pc_reliability_pc_ResourceTimeoutFailureType, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceTimeoutFailureType__PassiveResource", type=PassiveResource, multiplicity=Multiplicity(0, 1))
    }
)
repository__FailureType323: BinaryAssociation = BinaryAssociation(
    name="repository__FailureType323",
    ends={
        Property(name="Repository324", type=pcm_pc_reliability_pc_FailureType, multiplicity=Multiplicity(1, 1)),
        Property(name="failureTypes__Repository", type=Repository, multiplicity=Multiplicity(0, 1))
    }
)
resourceDemand_Action325: BinaryAssociation = BinaryAssociation(
    name="resourceDemand_Action325",
    ends={
        Property(name="ParametricResourceDemand326", type=pcm_pc_seff_pc_AbstractInternalControlFlowAction, multiplicity=Multiplicity(1, 1)),
        Property(name="action_ParametricResourceDemand", type=seff_performance_pc_ParametricResourceDemand, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
infrastructureCall__Action327: BinaryAssociation = BinaryAssociation(
    name="infrastructureCall__Action327",
    ends={
        Property(name="InfrastructureCall328", type=pcm_pc_seff_pc_AbstractInternalControlFlowAction, multiplicity=Multiplicity(1, 1)),
        Property(name="action__InfrastructureCall", type=seff_performance_pc_InfrastructureCall, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceCall__Action329: BinaryAssociation = BinaryAssociation(
    name="resourceCall__Action329",
    ends={
        Property(name="ResourceCall330", type=pcm_pc_seff_pc_AbstractInternalControlFlowAction, multiplicity=Multiplicity(1, 1)),
        Property(name="action__ResourceCall", type=seff_performance_pc_ResourceCall, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
predecessor_AbstractAction331: BinaryAssociation = BinaryAssociation(
    name="predecessor_AbstractAction331",
    ends={
        Property(name="AbstractAction", type=pcm_pc_seff_pc_AbstractAction, multiplicity=Multiplicity(1, 1)),
        Property(name="successor_AbstractAction", type=AbstractAction, multiplicity=Multiplicity(0, 1))
    }
)
successor_AbstractAction332: BinaryAssociation = BinaryAssociation(
    name="successor_AbstractAction332",
    ends={
        Property(name="AbstractAction333", type=pcm_pc_seff_pc_AbstractAction, multiplicity=Multiplicity(1, 1)),
        Property(name="predecessor_AbstractAction", type=AbstractAction, multiplicity=Multiplicity(0, 1))
    }
)
resourceDemandingBehaviour_AbstractAction334: BinaryAssociation = BinaryAssociation(
    name="resourceDemandingBehaviour_AbstractAction334",
    ends={
        Property(name="ResourceDemandingBehaviour", type=pcm_pc_seff_pc_AbstractAction, multiplicity=Multiplicity(1, 1)),
        Property(name="steps_Behaviour", type=ResourceDemandingBehaviour, multiplicity=Multiplicity(0, 1))
    }
)
abstractLoopAction_ResourceDemandingBehaviour335: BinaryAssociation = BinaryAssociation(
    name="abstractLoopAction_ResourceDemandingBehaviour335",
    ends={
        Property(name="AbstractLoopAction", type=pcm_pc_seff_pc_ResourceDemandingBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="bodyBehaviour_Loop336", type=AbstractLoopAction, multiplicity=Multiplicity(0, 1))
    }
)
abstractBranchTransition_ResourceDemandingBehaviour337: BinaryAssociation = BinaryAssociation(
    name="abstractBranchTransition_ResourceDemandingBehaviour337",
    ends={
        Property(name="AbstractBranchTransition", type=pcm_pc_seff_pc_ResourceDemandingBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="branchBehaviour_BranchTransition", type=AbstractBranchTransition, multiplicity=Multiplicity(0, 1))
    }
)
steps_Behaviour338: BinaryAssociation = BinaryAssociation(
    name="steps_Behaviour338",
    ends={
        Property(name="AbstractAction339", type=pcm_pc_seff_pc_ResourceDemandingBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceDemandingBehaviour_AbstractAction", type=AbstractAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bodyBehaviour_Loop340: BinaryAssociation = BinaryAssociation(
    name="bodyBehaviour_Loop340",
    ends={
        Property(name="ResourceDemandingBehaviour341", type=pcm_pc_seff_pc_AbstractLoopAction, multiplicity=Multiplicity(1, 1)),
        Property(name="abstractLoopAction_ResourceDemandingBehaviour", type=ResourceDemandingBehaviour, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
branchAction_AbstractBranchTransition342: BinaryAssociation = BinaryAssociation(
    name="branchAction_AbstractBranchTransition342",
    ends={
        Property(name="BranchAction", type=pcm_pc_seff_pc_AbstractBranchTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="branches_Branch", type=BranchAction, multiplicity=Multiplicity(0, 1))
    }
)
branches_Branch345: BinaryAssociation = BinaryAssociation(
    name="branches_Branch345",
    ends={
        Property(name="AbstractBranchTransition346", type=pcm_pc_seff_pc_BranchAction, multiplicity=Multiplicity(1, 1)),
        Property(name="branchAction_AbstractBranchTransition", type=AbstractBranchTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputVariableUsages__CallAction347: BinaryAssociation = BinaryAssociation(
    name="inputVariableUsages__CallAction347",
    ends={
        Property(name="VariableUsage348", type=pcm_pc_seff_pc_CallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="callAction__VariableUsage", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
describedService__SEFF349: BinaryAssociation = BinaryAssociation(
    name="describedService__SEFF349",
    ends={
        Property(name="Signature", type=pcm_pc_seff_pc_ServiceEffectSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_seff_pc_ServiceEffectSpecification", type=Signature, multiplicity=Multiplicity(0, 1))
    }
)
basicComponent_ServiceEffectSpecification350: BinaryAssociation = BinaryAssociation(
    name="basicComponent_ServiceEffectSpecification350",
    ends={
        Property(name="BasicComponent351", type=pcm_pc_seff_pc_ServiceEffectSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="serviceEffectSpecifications__BasicComponent", type=BasicComponent, multiplicity=Multiplicity(0, 1))
    }
)
branchBehaviour_BranchTransition343: BinaryAssociation = BinaryAssociation(
    name="branchBehaviour_BranchTransition343",
    ends={
        Property(name="ResourceDemandingBehaviour344", type=pcm_pc_seff_pc_AbstractBranchTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="abstractBranchTransition_ResourceDemandingBehaviour", type=ResourceDemandingBehaviour, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resourceDemandingInternalBehaviours352: BinaryAssociation = BinaryAssociation(
    name="resourceDemandingInternalBehaviours352",
    ends={
        Property(name="ResourceDemandingInternalBehaviour", type=pcm_pc_seff_pc_ResourceDemandingSEFF, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceDemandingSEFF_ResourceDemandingInternalBehaviour", type=ResourceDemandingInternalBehaviour, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceDemandingSEFF_ResourceDemandingInternalBehaviour353: BinaryAssociation = BinaryAssociation(
    name="resourceDemandingSEFF_ResourceDemandingInternalBehaviour353",
    ends={
        Property(name="ResourceDemandingSEFF", type=pcm_pc_seff_pc_ResourceDemandingInternalBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceDemandingInternalBehaviours", type=ResourceDemandingSEFF, multiplicity=Multiplicity(0, 1))
    }
)
passiveResource_ReleaseAction354: BinaryAssociation = BinaryAssociation(
    name="passiveResource_ReleaseAction354",
    ends={
        Property(name="PassiveResource355", type=pcm_pc_seff_pc_ReleaseAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_seff_pc_ReleaseAction", type=PassiveResource, multiplicity=Multiplicity(0, 1))
    }
)
iterationCount_LoopAction356: BinaryAssociation = BinaryAssociation(
    name="iterationCount_LoopAction356",
    ends={
        Property(name="PCMRandomVariable357", type=pcm_pc_seff_pc_LoopAction, multiplicity=Multiplicity(1, 1)),
        Property(name="loopAction_PCMRandomVariable", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
asynchronousForkedBehaviours_ForkAction358: BinaryAssociation = BinaryAssociation(
    name="asynchronousForkedBehaviours_ForkAction358",
    ends={
        Property(name="ForkedBehaviour", type=pcm_pc_seff_pc_ForkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="forkAction_ForkedBehaivour", type=ForkedBehaviour, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
synchronisingBehaviours_ForkAction359: BinaryAssociation = BinaryAssociation(
    name="synchronisingBehaviours_ForkAction359",
    ends={
        Property(name="SynchronisationPoint360", type=pcm_pc_seff_pc_ForkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="forkAction_SynchronisationPoint", type=SynchronisationPoint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
synchronisationPoint_ForkedBehaviour361: BinaryAssociation = BinaryAssociation(
    name="synchronisationPoint_ForkedBehaviour361",
    ends={
        Property(name="SynchronisationPoint362", type=pcm_pc_seff_pc_ForkedBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="synchronousForkedBehaviours_SynchronisationPoint", type=SynchronisationPoint, multiplicity=Multiplicity(0, 1))
    }
)
calledService_ExternalService370: BinaryAssociation = BinaryAssociation(
    name="calledService_ExternalService370",
    ends={
        Property(name="OperationSignature371", type=pcm_pc_seff_pc_ExternalCallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_seff_pc_ExternalCallAction", type=OperationSignature, multiplicity=Multiplicity(0, 1))
    }
)
role_ExternalService372: BinaryAssociation = BinaryAssociation(
    name="role_ExternalService372",
    ends={
        Property(name="OperationRequiredRole374", type=pcm_pc_seff_pc_ExternalCallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_seff_pc_ExternalCallAction373", type=OperationRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
returnVariableUsage__CallReturnAction375: BinaryAssociation = BinaryAssociation(
    name="returnVariableUsage__CallReturnAction375",
    ends={
        Property(name="VariableUsage376", type=pcm_pc_seff_pc_CallReturnAction, multiplicity=Multiplicity(1, 1)),
        Property(name="callReturnAction__VariableUsage", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
forkAction_ForkedBehaivour363: BinaryAssociation = BinaryAssociation(
    name="forkAction_ForkedBehaivour363",
    ends={
        Property(name="ForkAction", type=pcm_pc_seff_pc_ForkedBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="asynchronousForkedBehaviours_ForkAction", type=ForkAction, multiplicity=Multiplicity(0, 1))
    }
)
passiveresource_AcquireAction377: BinaryAssociation = BinaryAssociation(
    name="passiveresource_AcquireAction377",
    ends={
        Property(name="PassiveResource378", type=pcm_pc_seff_pc_AcquireAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_seff_pc_AcquireAction", type=PassiveResource, multiplicity=Multiplicity(0, 1))
    }
)
outputParameterUsage_SynchronisationPoint364: BinaryAssociation = BinaryAssociation(
    name="outputParameterUsage_SynchronisationPoint364",
    ends={
        Property(name="VariableUsage365", type=pcm_pc_seff_pc_SynchronisationPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="synchronisationPoint_VariableUsage", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
forkAction_SynchronisationPoint366: BinaryAssociation = BinaryAssociation(
    name="forkAction_SynchronisationPoint366",
    ends={
        Property(name="ForkAction367", type=pcm_pc_seff_pc_SynchronisationPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="synchronisingBehaviours_ForkAction", type=ForkAction, multiplicity=Multiplicity(0, 1))
    }
)
synchronousForkedBehaviours_SynchronisationPoint368: BinaryAssociation = BinaryAssociation(
    name="synchronousForkedBehaviours_SynchronisationPoint368",
    ends={
        Property(name="ForkedBehaviour369", type=pcm_pc_seff_pc_SynchronisationPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="synchronisationPoint_ForkedBehaviour", type=ForkedBehaviour, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
localVariableUsages_SetVariableAction383: BinaryAssociation = BinaryAssociation(
    name="localVariableUsages_SetVariableAction383",
    ends={
        Property(name="VariableUsage384", type=pcm_pc_seff_pc_SetVariableAction, multiplicity=Multiplicity(1, 1)),
        Property(name="setVariableAction_VariableUsage", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
calledResourceDemandingInternalBehaviour385: BinaryAssociation = BinaryAssociation(
    name="calledResourceDemandingInternalBehaviour385",
    ends={
        Property(name="ResourceDemandingInternalBehaviour386", type=pcm_pc_seff_pc_InternalCallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_seff_pc_InternalCallAction", type=ResourceDemandingInternalBehaviour, multiplicity=Multiplicity(0, 1))
    }
)
eventType__EmitEventAction387: BinaryAssociation = BinaryAssociation(
    name="eventType__EmitEventAction387",
    ends={
        Property(name="EventType388", type=pcm_pc_seff_pc_EmitEventAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_seff_pc_EmitEventAction", type=EventType, multiplicity=Multiplicity(0, 1))
    }
)
sourceRole__EmitEventAction389: BinaryAssociation = BinaryAssociation(
    name="sourceRole__EmitEventAction389",
    ends={
        Property(name="SourceRole391", type=pcm_pc_seff_pc_EmitEventAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_seff_pc_EmitEventAction390", type=SourceRole, multiplicity=Multiplicity(0, 1))
    }
)
internalFailureOccurrenceDescriptions__InternalAction392: BinaryAssociation = BinaryAssociation(
    name="internalFailureOccurrenceDescriptions__InternalAction392",
    ends={
        Property(name="InternalFailureOccurrenceDescription393", type=pcm_pc_seff_pc_InternalAction, multiplicity=Multiplicity(1, 1)),
        Property(name="internalAction__InternalFailureOccurrenceDescription", type=InternalFailureOccurrenceDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameter_CollectionIteratorAction379: BinaryAssociation = BinaryAssociation(
    name="parameter_CollectionIteratorAction379",
    ends={
        Property(name="Parameter380", type=pcm_pc_seff_pc_CollectionIteratorAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_seff_pc_CollectionIteratorAction", type=Parameter_, multiplicity=Multiplicity(0, 1))
    }
)
branchCondition_GuardedBranchTransition381: BinaryAssociation = BinaryAssociation(
    name="branchCondition_GuardedBranchTransition381",
    ends={
        Property(name="PCMRandomVariable382", type=pcm_pc_seff_pc_GuardedBranchTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="guardedBranchTransition_PCMRandomVariable", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
signature__InfrastructureCall394: BinaryAssociation = BinaryAssociation(
    name="signature__InfrastructureCall394",
    ends={
        Property(name="InfrastructureSignature395", type=pcm_pc_seff_performance_pc_InfrastructureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_seff_performance_pc_InfrastructureCall", type=InfrastructureSignature, multiplicity=Multiplicity(0, 1))
    }
)
numberOfCalls__InfrastructureCall396: BinaryAssociation = BinaryAssociation(
    name="numberOfCalls__InfrastructureCall396",
    ends={
        Property(name="PCMRandomVariable397", type=pcm_pc_seff_performance_pc_InfrastructureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="infrastructureCall__PCMRandomVariable", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
action__InfrastructureCall398: BinaryAssociation = BinaryAssociation(
    name="action__InfrastructureCall398",
    ends={
        Property(name="AbstractInternalControlFlowAction", type=pcm_pc_seff_performance_pc_InfrastructureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="infrastructureCall__Action", type=AbstractInternalControlFlowAction, multiplicity=Multiplicity(0, 1))
    }
)
requiredRole__InfrastructureCall399: BinaryAssociation = BinaryAssociation(
    name="requiredRole__InfrastructureCall399",
    ends={
        Property(name="InfrastructureRequiredRole401", type=pcm_pc_seff_performance_pc_InfrastructureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_seff_performance_pc_InfrastructureCall400", type=InfrastructureRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
specification_ParametericResourceDemand411: BinaryAssociation = BinaryAssociation(
    name="specification_ParametericResourceDemand411",
    ends={
        Property(name="PCMRandomVariable412", type=pcm_pc_seff_performance_pc_ParametricResourceDemand, multiplicity=Multiplicity(1, 1)),
        Property(name="parametricResourceDemand_PCMRandomVariable", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
requiredResource_ParametricResourceDemand413: BinaryAssociation = BinaryAssociation(
    name="requiredResource_ParametricResourceDemand413",
    ends={
        Property(name="ProcessingResourceType414", type=pcm_pc_seff_performance_pc_ParametricResourceDemand, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_seff_performance_pc_ParametricResourceDemand", type=ProcessingResourceType, multiplicity=Multiplicity(0, 1))
    }
)
action_ParametricResourceDemand415: BinaryAssociation = BinaryAssociation(
    name="action_ParametricResourceDemand415",
    ends={
        Property(name="AbstractInternalControlFlowAction416", type=pcm_pc_seff_performance_pc_ParametricResourceDemand, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceDemand_Action", type=AbstractInternalControlFlowAction, multiplicity=Multiplicity(0, 1))
    }
)
action__ResourceCall402: BinaryAssociation = BinaryAssociation(
    name="action__ResourceCall402",
    ends={
        Property(name="AbstractInternalControlFlowAction403", type=pcm_pc_seff_performance_pc_ResourceCall, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceCall__Action", type=AbstractInternalControlFlowAction, multiplicity=Multiplicity(0, 1))
    }
)
resourceRequiredRole__ResourceCall404: BinaryAssociation = BinaryAssociation(
    name="resourceRequiredRole__ResourceCall404",
    ends={
        Property(name="entity_pc_ResourceRequiredRole405", type=pcm_pc_seff_performance_pc_ResourceCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_seff_performance_pc_ResourceCall", type=entity_pc_ResourceRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
signature__ResourceCall406: BinaryAssociation = BinaryAssociation(
    name="signature__ResourceCall406",
    ends={
        Property(name="ResourceSignature408", type=pcm_pc_seff_performance_pc_ResourceCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_seff_performance_pc_ResourceCall407", type=ResourceSignature, multiplicity=Multiplicity(0, 1))
    }
)
numberOfCalls__ResourceCall409: BinaryAssociation = BinaryAssociation(
    name="numberOfCalls__ResourceCall409",
    ends={
        Property(name="PCMRandomVariable410", type=pcm_pc_seff_performance_pc_ResourceCall, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceCall__PCMRandomVariable", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
primaryBehaviour__RecoveryAction419: BinaryAssociation = BinaryAssociation(
    name="primaryBehaviour__RecoveryAction419",
    ends={
        Property(name="seff_reliability_pc_RecoveryActionBehaviour420", type=pcm_pc_seff_reliability_pc_RecoveryAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_seff_reliability_pc_RecoveryAction", type=seff_reliability_pc_RecoveryActionBehaviour, multiplicity=Multiplicity(0, 1))
    }
)
recoveryActionBehaviours__RecoveryAction421: BinaryAssociation = BinaryAssociation(
    name="recoveryActionBehaviours__RecoveryAction421",
    ends={
        Property(name="RecoveryActionBehaviour", type=pcm_pc_seff_reliability_pc_RecoveryAction, multiplicity=Multiplicity(1, 1)),
        Property(name="recoveryAction__RecoveryActionBehaviour", type=seff_reliability_pc_RecoveryActionBehaviour, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
failureTypes_FailureHandlingEntity422: BinaryAssociation = BinaryAssociation(
    name="failureTypes_FailureHandlingEntity422",
    ends={
        Property(name="FailureType423", type=pcm_pc_seff_reliability_pc_FailureHandlingEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_seff_reliability_pc_FailureHandlingEntity", type=FailureType, multiplicity=Multiplicity(0, 9999))
    }
)
signature_SpecifiedQoSAnnation424: BinaryAssociation = BinaryAssociation(
    name="signature_SpecifiedQoSAnnation424",
    ends={
        Property(name="Signature425", type=pcm_pc_qosannotations_pc_SpecifiedQoSAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_qosannotations_pc_SpecifiedQoSAnnotation", type=Signature, multiplicity=Multiplicity(0, 1))
    }
)
role_SpecifiedQoSAnnotation426: BinaryAssociation = BinaryAssociation(
    name="role_SpecifiedQoSAnnotation426",
    ends={
        Property(name="Role", type=pcm_pc_qosannotations_pc_SpecifiedQoSAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_qosannotations_pc_SpecifiedQoSAnnotation427", type=Role, multiplicity=Multiplicity(0, 1))
    }
)
qosAnnotations_SpecifiedQoSAnnotation428: BinaryAssociation = BinaryAssociation(
    name="qosAnnotations_SpecifiedQoSAnnotation428",
    ends={
        Property(name="QoSAnnotations", type=pcm_pc_qosannotations_pc_SpecifiedQoSAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="specifiedQoSAnnotations_QoSAnnotations", type=QoSAnnotations, multiplicity=Multiplicity(0, 1))
    }
)
failureHandlingAlternatives__RecoveryActionBehaviour417: BinaryAssociation = BinaryAssociation(
    name="failureHandlingAlternatives__RecoveryActionBehaviour417",
    ends={
        Property(name="seff_reliability_pc_RecoveryActionBehaviour", type=pcm_pc_seff_reliability_pc_RecoveryActionBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_seff_reliability_pc_RecoveryActionBehaviour", type=seff_reliability_pc_RecoveryActionBehaviour, multiplicity=Multiplicity(0, 9999))
    }
)
recoveryAction__RecoveryActionBehaviour418: BinaryAssociation = BinaryAssociation(
    name="recoveryAction__RecoveryActionBehaviour418",
    ends={
        Property(name="RecoveryAction", type=pcm_pc_seff_reliability_pc_RecoveryActionBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="recoveryActionBehaviours__RecoveryAction", type=seff_reliability_pc_RecoveryAction, multiplicity=Multiplicity(0, 1))
    }
)
specifiedOutputParameterAbstractions_QoSAnnotations429: BinaryAssociation = BinaryAssociation(
    name="specifiedOutputParameterAbstractions_QoSAnnotations429",
    ends={
        Property(name="SpecifiedOutputParameterAbstraction430", type=pcm_pc_qosannotations_pc_QoSAnnotations, multiplicity=Multiplicity(1, 1)),
        Property(name="qosAnnotations_SpecifiedOutputParameterAbstraction", type=SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
system_QoSAnnotations431: BinaryAssociation = BinaryAssociation(
    name="system_QoSAnnotations431",
    ends={
        Property(name="System", type=pcm_pc_qosannotations_pc_QoSAnnotations, multiplicity=Multiplicity(1, 1)),
        Property(name="qosAnnotations_System", type=System, multiplicity=Multiplicity(0, 1))
    }
)
specifiedQoSAnnotations_QoSAnnotations432: BinaryAssociation = BinaryAssociation(
    name="specifiedQoSAnnotations_QoSAnnotations432",
    ends={
        Property(name="SpecifiedQoSAnnotation", type=pcm_pc_qosannotations_pc_QoSAnnotations, multiplicity=Multiplicity(1, 1)),
        Property(name="qosAnnotations_SpecifiedQoSAnnotation", type=SpecifiedQoSAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
signature_SpecifiedOutputParameterAbstraction433: BinaryAssociation = BinaryAssociation(
    name="signature_SpecifiedOutputParameterAbstraction433",
    ends={
        Property(name="Signature434", type=pcm_pc_qosannotations_pc_SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_qosannotations_pc_SpecifiedOutputParameterAbstraction", type=Signature, multiplicity=Multiplicity(0, 1))
    }
)
role_SpecifiedOutputParameterAbstraction435: BinaryAssociation = BinaryAssociation(
    name="role_SpecifiedOutputParameterAbstraction435",
    ends={
        Property(name="Role437", type=pcm_pc_qosannotations_pc_SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_qosannotations_pc_SpecifiedOutputParameterAbstraction436", type=Role, multiplicity=Multiplicity(0, 1))
    }
)
expectedExternalOutputs_SpecifiedOutputParameterAbstraction438: BinaryAssociation = BinaryAssociation(
    name="expectedExternalOutputs_SpecifiedOutputParameterAbstraction438",
    ends={
        Property(name="VariableUsage439", type=pcm_pc_qosannotations_pc_SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(1, 1)),
        Property(name="specifiedOutputParameterAbstraction_expectedExternalOutputs_VariableUsage", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
qosAnnotations_SpecifiedOutputParameterAbstraction440: BinaryAssociation = BinaryAssociation(
    name="qosAnnotations_SpecifiedOutputParameterAbstraction440",
    ends={
        Property(name="QoSAnnotations441", type=pcm_pc_qosannotations_pc_SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(1, 1)),
        Property(name="specifiedOutputParameterAbstractions_QoSAnnotations", type=QoSAnnotations, multiplicity=Multiplicity(0, 1))
    }
)
externalFailureOccurrenceDescriptions__SpecifiedReliabilityAnnotation446: BinaryAssociation = BinaryAssociation(
    name="externalFailureOccurrenceDescriptions__SpecifiedReliabilityAnnotation446",
    ends={
        Property(name="ExternalFailureOccurrenceDescription", type=pcm_pc_qos_reliability_pc_SpecifiedReliabilityAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="specifiedReliabilityAnnotation__ExternalFailureOccurrenceDescription", type=ExternalFailureOccurrenceDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specification_SpecifiedExecutionTime442: BinaryAssociation = BinaryAssociation(
    name="specification_SpecifiedExecutionTime442",
    ends={
        Property(name="PCMRandomVariable443", type=pcm_pc_qos_performance_pc_SpecifiedExecutionTime, multiplicity=Multiplicity(1, 1)),
        Property(name="specifiedExecutionTime_PCMRandomVariable", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assemblyContext_ComponentSpecifiedExecutionTime444: BinaryAssociation = BinaryAssociation(
    name="assemblyContext_ComponentSpecifiedExecutionTime444",
    ends={
        Property(name="composition_pc_AssemblyContext445", type=pcm_pc_qos_performance_pc_ComponentSpecifiedExecutionTime, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_qos_performance_pc_ComponentSpecifiedExecutionTime", type=composition_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
connectedResourceContainers_LinkingResource451: BinaryAssociation = BinaryAssociation(
    name="connectedResourceContainers_LinkingResource451",
    ends={
        Property(name="ResourceContainer452", type=pcm_pc_resourceenvironment_pc_LinkingResource, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_resourceenvironment_pc_LinkingResource", type=ResourceContainer, multiplicity=Multiplicity(0, 9999))
    }
)
communicationLinkResourceSpecifications_LinkingResource453: BinaryAssociation = BinaryAssociation(
    name="communicationLinkResourceSpecifications_LinkingResource453",
    ends={
        Property(name="CommunicationLinkResourceSpecification454", type=pcm_pc_resourceenvironment_pc_LinkingResource, multiplicity=Multiplicity(1, 1)),
        Property(name="linkingResource_CommunicationLinkResourceSpecification", type=CommunicationLinkResourceSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resourceEnvironment_LinkingResource455: BinaryAssociation = BinaryAssociation(
    name="resourceEnvironment_LinkingResource455",
    ends={
        Property(name="ResourceEnvironment", type=pcm_pc_resourceenvironment_pc_LinkingResource, multiplicity=Multiplicity(1, 1)),
        Property(name="linkingResources__ResourceEnvironment", type=ResourceEnvironment, multiplicity=Multiplicity(0, 1))
    }
)
activeResourceSpecifications_ResourceContainer456: BinaryAssociation = BinaryAssociation(
    name="activeResourceSpecifications_ResourceContainer456",
    ends={
        Property(name="ProcessingResourceSpecification457", type=pcm_pc_resourceenvironment_pc_ResourceContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceContainer_ProcessingResourceSpecification", type=ProcessingResourceSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceEnvironment_ResourceContainer458: BinaryAssociation = BinaryAssociation(
    name="resourceEnvironment_ResourceContainer458",
    ends={
        Property(name="ResourceEnvironment459", type=pcm_pc_resourceenvironment_pc_ResourceContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceContainer_ResourceEnvironment", type=ResourceEnvironment, multiplicity=Multiplicity(0, 1))
    }
)
nestedResourceContainers__ResourceContainer460: BinaryAssociation = BinaryAssociation(
    name="nestedResourceContainers__ResourceContainer460",
    ends={
        Property(name="ResourceContainer461", type=pcm_pc_resourceenvironment_pc_ResourceContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="parentResourceContainer__ResourceContainer", type=ResourceContainer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentResourceContainer__ResourceContainer462: BinaryAssociation = BinaryAssociation(
    name="parentResourceContainer__ResourceContainer462",
    ends={
        Property(name="ResourceContainer463", type=pcm_pc_resourceenvironment_pc_ResourceContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="nestedResourceContainers__ResourceContainer", type=ResourceContainer, multiplicity=Multiplicity(0, 1))
    }
)
schedulingPolicy464: BinaryAssociation = BinaryAssociation(
    name="schedulingPolicy464",
    ends={
        Property(name="SchedulingPolicy465", type=pcm_pc_resourceenvironment_pc_ProcessingResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_resourceenvironment_pc_ProcessingResourceSpecification", type=SchedulingPolicy, multiplicity=Multiplicity(0, 1))
    }
)
qosAnnotations_System447: BinaryAssociation = BinaryAssociation(
    name="qosAnnotations_System447",
    ends={
        Property(name="QoSAnnotations448", type=pcm_pc_system_pc_System, multiplicity=Multiplicity(1, 1)),
        Property(name="system_QoSAnnotations", type=QoSAnnotations, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
linkingResources__ResourceEnvironment449: BinaryAssociation = BinaryAssociation(
    name="linkingResources__ResourceEnvironment449",
    ends={
        Property(name="LinkingResource", type=pcm_pc_resourceenvironment_pc_ResourceEnvironment, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceEnvironment_LinkingResource", type=LinkingResource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceContainer_ResourceEnvironment450: BinaryAssociation = BinaryAssociation(
    name="resourceContainer_ResourceEnvironment450",
    ends={
        Property(name="ResourceContainer", type=pcm_pc_resourceenvironment_pc_ResourceEnvironment, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceEnvironment_ResourceContainer", type=ResourceContainer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
communicationLinkResourceType_CommunicationLinkResourceSpecification475: BinaryAssociation = BinaryAssociation(
    name="communicationLinkResourceType_CommunicationLinkResourceSpecification475",
    ends={
        Property(name="CommunicationLinkResourceType476", type=pcm_pc_resourceenvironment_pc_CommunicationLinkResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_resourceenvironment_pc_CommunicationLinkResourceSpecification", type=CommunicationLinkResourceType, multiplicity=Multiplicity(0, 1))
    }
)
latency_CommunicationLinkResourceSpecification477: BinaryAssociation = BinaryAssociation(
    name="latency_CommunicationLinkResourceSpecification477",
    ends={
        Property(name="PCMRandomVariable478", type=pcm_pc_resourceenvironment_pc_CommunicationLinkResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="communicationLinkResourceSpecification_latency_PCMRandomVariable", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
throughput_CommunicationLinkResourceSpecification479: BinaryAssociation = BinaryAssociation(
    name="throughput_CommunicationLinkResourceSpecification479",
    ends={
        Property(name="PCMRandomVariable480", type=pcm_pc_resourceenvironment_pc_CommunicationLinkResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="communicationLinkResourceSpecifcation_throughput_PCMRandomVariable", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resourceContainer_AllocationContext481: BinaryAssociation = BinaryAssociation(
    name="resourceContainer_AllocationContext481",
    ends={
        Property(name="ResourceContainer482", type=pcm_pc_allocation_pc_AllocationContext, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_allocation_pc_AllocationContext", type=ResourceContainer, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext_AllocationContext483: BinaryAssociation = BinaryAssociation(
    name="assemblyContext_AllocationContext483",
    ends={
        Property(name="composition_pc_AssemblyContext485", type=pcm_pc_allocation_pc_AllocationContext, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_allocation_pc_AllocationContext484", type=composition_pc_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
allocation_AllocationContext486: BinaryAssociation = BinaryAssociation(
    name="allocation_AllocationContext486",
    ends={
        Property(name="Allocation", type=pcm_pc_allocation_pc_AllocationContext, multiplicity=Multiplicity(1, 1)),
        Property(name="allocationContexts_Allocation", type=Allocation, multiplicity=Multiplicity(0, 1))
    }
)
eventChannel__AllocationContext487: BinaryAssociation = BinaryAssociation(
    name="eventChannel__AllocationContext487",
    ends={
        Property(name="composition_pc_EventChannel", type=pcm_pc_allocation_pc_AllocationContext, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_allocation_pc_AllocationContext488", type=composition_pc_EventChannel, multiplicity=Multiplicity(0, 1))
    }
)
activeResourceType_ActiveResourceSpecification466: BinaryAssociation = BinaryAssociation(
    name="activeResourceType_ActiveResourceSpecification466",
    ends={
        Property(name="ProcessingResourceType468", type=pcm_pc_resourceenvironment_pc_ProcessingResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_resourceenvironment_pc_ProcessingResourceSpecification467", type=ProcessingResourceType, multiplicity=Multiplicity(0, 1))
    }
)
processingRate_ProcessingResourceSpecification469: BinaryAssociation = BinaryAssociation(
    name="processingRate_ProcessingResourceSpecification469",
    ends={
        Property(name="PCMRandomVariable470", type=pcm_pc_resourceenvironment_pc_ProcessingResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="processingResourceSpecification_processingRate_PCMRandomVariable", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resourceContainer_ProcessingResourceSpecification471: BinaryAssociation = BinaryAssociation(
    name="resourceContainer_ProcessingResourceSpecification471",
    ends={
        Property(name="ResourceContainer472", type=pcm_pc_resourceenvironment_pc_ProcessingResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="activeResourceSpecifications_ResourceContainer", type=ResourceContainer, multiplicity=Multiplicity(0, 1))
    }
)
linkingResource_CommunicationLinkResourceSpecification473: BinaryAssociation = BinaryAssociation(
    name="linkingResource_CommunicationLinkResourceSpecification473",
    ends={
        Property(name="LinkingResource474", type=pcm_pc_resourceenvironment_pc_CommunicationLinkResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="communicationLinkResourceSpecifications_LinkingResource", type=LinkingResource, multiplicity=Multiplicity(0, 1))
    }
)
targetResourceEnvironment_Allocation489: BinaryAssociation = BinaryAssociation(
    name="targetResourceEnvironment_Allocation489",
    ends={
        Property(name="ResourceEnvironment490", type=pcm_pc_allocation_pc_Allocation, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_allocation_pc_Allocation", type=ResourceEnvironment, multiplicity=Multiplicity(0, 1))
    }
)
system_Allocation491: BinaryAssociation = BinaryAssociation(
    name="system_Allocation491",
    ends={
        Property(name="System493", type=pcm_pc_allocation_pc_Allocation, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_allocation_pc_Allocation492", type=System, multiplicity=Multiplicity(0, 1))
    }
)
allocationContexts_Allocation494: BinaryAssociation = BinaryAssociation(
    name="allocationContexts_Allocation494",
    ends={
        Property(name="AllocationContext", type=pcm_pc_allocation_pc_Allocation, multiplicity=Multiplicity(1, 1)),
        Property(name="allocation_AllocationContext", type=AllocationContext, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
completions_CompletionRepository495: BinaryAssociation = BinaryAssociation(
    name="completions_CompletionRepository495",
    ends={
        Property(name="Completion", type=pcm_pc_completions_pc_CompletionRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_completions_pc_CompletionRepository", type=Completion, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredCommunicationLinkResource_ParametricResourceDemand496: BinaryAssociation = BinaryAssociation(
    name="requiredCommunicationLinkResource_ParametricResourceDemand496",
    ends={
        Property(name="CommunicationLinkResourceType497", type=pcm_pc_completions_pc_NetworkDemandParametricResourceDemand, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_pc_completions_pc_NetworkDemandParametricResourceDemand", type=CommunicationLinkResourceType, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_pcm_pc_core_pc_PCMRandomVariable_RandomVariable = Generalization(general=RandomVariable, specific=pcm_pc_core_pc_PCMRandomVariable)
gen_pcm_pc_entity_pc_ResourceProvidedRole_Role = Generalization(general=Role, specific=pcm_pc_entity_pc_ResourceProvidedRole)
gen_pcm_pc_entity_pc_InterfaceProvidingRequiringEntity_entity_pc_InterfaceProvidingEntity = Generalization(general=entity_pc_InterfaceProvidingEntity, specific=pcm_pc_entity_pc_InterfaceProvidingRequiringEntity)
gen_pcm_pc_entity_pc_InterfaceProvidingRequiringEntity_entity_pc_InterfaceRequiringEntity = Generalization(general=entity_pc_InterfaceRequiringEntity, specific=pcm_pc_entity_pc_InterfaceProvidingRequiringEntity)
gen_pcm_pc_entity_pc_InterfaceProvidingEntity_Entity = Generalization(general=Entity, specific=pcm_pc_entity_pc_InterfaceProvidingEntity)
gen_pcm_pc_entity_pc_ResourceInterfaceRequiringEntity_Entity = Generalization(general=Entity, specific=pcm_pc_entity_pc_ResourceInterfaceRequiringEntity)
gen_pcm_pc_entity_pc_ResourceRequiredRole_Role = Generalization(general=Role, specific=pcm_pc_entity_pc_ResourceRequiredRole)
gen_pcm_pc_entity_pc_ResourceInterfaceProvidingEntity_Entity = Generalization(general=Entity, specific=pcm_pc_entity_pc_ResourceInterfaceProvidingEntity)
gen_pcm_pc_entity_pc_InterfaceRequiringEntity_entity_pc_Entity = Generalization(general=entity_pc_Entity, specific=pcm_pc_entity_pc_InterfaceRequiringEntity)
gen_pcm_pc_entity_pc_InterfaceRequiringEntity_entity_pc_ResourceInterfaceRequiringEntity = Generalization(general=entity_pc_ResourceInterfaceRequiringEntity, specific=pcm_pc_entity_pc_InterfaceRequiringEntity)
gen_pcm_pc_entity_pc_ResourceInterfaceProvidingRequiringEntity_entity_pc_ResourceInterfaceRequiringEntity = Generalization(general=entity_pc_ResourceInterfaceRequiringEntity, specific=pcm_pc_entity_pc_ResourceInterfaceProvidingRequiringEntity)
gen_pcm_pc_entity_pc_ResourceInterfaceProvidingRequiringEntity_entity_pc_ResourceInterfaceProvidingEntity = Generalization(general=entity_pc_ResourceInterfaceProvidingEntity, specific=pcm_pc_entity_pc_ResourceInterfaceProvidingRequiringEntity)
gen_pcm_pc_entity_pc_Entity_Identifier = Generalization(general=Identifier, specific=pcm_pc_entity_pc_Entity)
gen_pcm_pc_entity_pc_Entity_entity_pc_NamedElement = Generalization(general=entity_pc_NamedElement, specific=pcm_pc_entity_pc_Entity)
gen_pcm_pc_composition_pc_DelegationConnector_Connector = Generalization(general=Connector, specific=pcm_pc_composition_pc_DelegationConnector)
gen_pcm_pc_composition_pc_Connector_Entity = Generalization(general=Entity, specific=pcm_pc_composition_pc_Connector)
gen_pcm_pc_composition_pc_ComposedStructure_Entity = Generalization(general=Entity, specific=pcm_pc_composition_pc_ComposedStructure)
gen_pcm_pc_entity_pc_ComposedProvidingRequiringEntity_composition_pc_ComposedStructure = Generalization(general=composition_pc_ComposedStructure, specific=pcm_pc_entity_pc_ComposedProvidingRequiringEntity)
gen_pcm_pc_entity_pc_ComposedProvidingRequiringEntity_entity_pc_InterfaceProvidingRequiringEntity = Generalization(general=entity_pc_InterfaceProvidingRequiringEntity, specific=pcm_pc_entity_pc_ComposedProvidingRequiringEntity)
gen_pcm_pc_composition_pc_EventChannel_Entity = Generalization(general=Entity, specific=pcm_pc_composition_pc_EventChannel)
gen_pcm_pc_composition_pc_EventChannelSourceConnector_Connector = Generalization(general=Connector, specific=pcm_pc_composition_pc_EventChannelSourceConnector)
gen_pcm_pc_composition_pc_EventChannelSinkConnector_Connector = Generalization(general=Connector, specific=pcm_pc_composition_pc_EventChannelSinkConnector)
gen_pcm_pc_composition_pc_ProvidedDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_pc_composition_pc_ProvidedDelegationConnector)
gen_pcm_pc_composition_pc_RequiredDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_pc_composition_pc_RequiredDelegationConnector)
gen_pcm_pc_composition_pc_AssemblyEventConnector_Connector = Generalization(general=Connector, specific=pcm_pc_composition_pc_AssemblyEventConnector)
gen_pcm_pc_composition_pc_AssemblyConnector_Connector = Generalization(general=Connector, specific=pcm_pc_composition_pc_AssemblyConnector)
gen_pcm_pc_composition_pc_SourceDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_pc_composition_pc_SourceDelegationConnector)
gen_pcm_pc_composition_pc_SinkDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_pc_composition_pc_SinkDelegationConnector)
gen_pcm_pc_composition_pc_AssemblyInfrastructureConnector_Connector = Generalization(general=Connector, specific=pcm_pc_composition_pc_AssemblyInfrastructureConnector)
gen_pcm_pc_composition_pc_ProvidedInfrastructureDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_pc_composition_pc_ProvidedInfrastructureDelegationConnector)
gen_pcm_pc_composition_pc_RequiredResourceDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_pc_composition_pc_RequiredResourceDelegationConnector)
gen_pcm_pc_composition_pc_AssemblyContext_Entity = Generalization(general=Entity, specific=pcm_pc_composition_pc_AssemblyContext)
gen_pcm_pc_usagemodel_pc_UsageScenario_Entity = Generalization(general=Entity, specific=pcm_pc_usagemodel_pc_UsageScenario)
gen_pcm_pc_composition_pc_RequiredInfrastructureDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_pc_composition_pc_RequiredInfrastructureDelegationConnector)
gen_pcm_pc_usagemodel_pc_AbstractUserAction_Entity = Generalization(general=Entity, specific=pcm_pc_usagemodel_pc_AbstractUserAction)
gen_pcm_pc_usagemodel_pc_EntryLevelSystemCall_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_pc_usagemodel_pc_EntryLevelSystemCall)
gen_pcm_pc_usagemodel_pc_ScenarioBehaviour_Entity = Generalization(general=Entity, specific=pcm_pc_usagemodel_pc_ScenarioBehaviour)
gen_pcm_pc_usagemodel_pc_Loop_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_pc_usagemodel_pc_Loop)
gen_pcm_pc_usagemodel_pc_Stop_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_pc_usagemodel_pc_Stop)
gen_pcm_pc_usagemodel_pc_Start_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_pc_usagemodel_pc_Start)
gen_pcm_pc_usagemodel_pc_Branch_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_pc_usagemodel_pc_Branch)
gen_pcm_pc_usagemodel_pc_Delay_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_pc_usagemodel_pc_Delay)
gen_pcm_pc_usagemodel_pc_ClosedWorkload_Workload = Generalization(general=Workload, specific=pcm_pc_usagemodel_pc_ClosedWorkload)
gen_pcm_pc_repository_pc_PassiveResource_Entity = Generalization(general=Entity, specific=pcm_pc_repository_pc_PassiveResource)
gen_pcm_pc_usagemodel_pc_OpenWorkload_Workload = Generalization(general=Workload, specific=pcm_pc_usagemodel_pc_OpenWorkload)
gen_pcm_pc_repository_pc_BasicComponent_ImplementationComponentType = Generalization(general=ImplementationComponentType, specific=pcm_pc_repository_pc_BasicComponent)
gen_pcm_pc_repository_pc_ImplementationComponentType_RepositoryComponent = Generalization(general=RepositoryComponent, specific=pcm_pc_repository_pc_ImplementationComponentType)
gen_pcm_pc_repository_pc_RepositoryComponent_InterfaceProvidingRequiringEntity = Generalization(general=InterfaceProvidingRequiringEntity, specific=pcm_pc_repository_pc_RepositoryComponent)
gen_pcm_pc_repository_pc_ProvidedRole_Role = Generalization(general=Role, specific=pcm_pc_repository_pc_ProvidedRole)
gen_pcm_pc_repository_pc_Repository_Entity = Generalization(general=Entity, specific=pcm_pc_repository_pc_Repository)
gen_pcm_pc_repository_pc_Interface_Entity = Generalization(general=Entity, specific=pcm_pc_repository_pc_Interface)
gen_pcm_pc_repository_pc_EventGroup_Interface = Generalization(general=Interface, specific=pcm_pc_repository_pc_EventGroup)
gen_pcm_pc_repository_pc_EventType_Signature = Generalization(general=Signature, specific=pcm_pc_repository_pc_EventType)
gen_pcm_pc_repository_pc_Signature_Entity = Generalization(general=Entity, specific=pcm_pc_repository_pc_Signature)
gen_pcm_pc_repository_pc_InfrastructureSignature_Signature = Generalization(general=Signature, specific=pcm_pc_repository_pc_InfrastructureSignature)
gen_pcm_pc_repository_pc_InfrastructureInterface_Interface = Generalization(general=Interface, specific=pcm_pc_repository_pc_InfrastructureInterface)
gen_pcm_pc_repository_pc_InfrastructureRequiredRole_RequiredRole = Generalization(general=RequiredRole, specific=pcm_pc_repository_pc_InfrastructureRequiredRole)
gen_pcm_pc_repository_pc_RequiredRole_Role = Generalization(general=Role, specific=pcm_pc_repository_pc_RequiredRole)
gen_pcm_pc_repository_pc_OperationSignature_Signature = Generalization(general=Signature, specific=pcm_pc_repository_pc_OperationSignature)
gen_pcm_pc_repository_pc_OperationInterface_Interface = Generalization(general=Interface, specific=pcm_pc_repository_pc_OperationInterface)
gen_pcm_pc_repository_pc_OperationRequiredRole_RequiredRole = Generalization(general=RequiredRole, specific=pcm_pc_repository_pc_OperationRequiredRole)
gen_pcm_pc_repository_pc_SourceRole_RequiredRole = Generalization(general=RequiredRole, specific=pcm_pc_repository_pc_SourceRole)
gen_pcm_pc_repository_pc_InfrastructureProvidedRole_ProvidedRole = Generalization(general=ProvidedRole, specific=pcm_pc_repository_pc_InfrastructureProvidedRole)
gen_pcm_pc_repository_pc_CompleteComponentType_RepositoryComponent = Generalization(general=RepositoryComponent, specific=pcm_pc_repository_pc_CompleteComponentType)
gen_pcm_pc_repository_pc_ProvidesComponentType_RepositoryComponent = Generalization(general=RepositoryComponent, specific=pcm_pc_repository_pc_ProvidesComponentType)
gen_pcm_pc_repository_pc_SinkRole_ProvidedRole = Generalization(general=ProvidedRole, specific=pcm_pc_repository_pc_SinkRole)
gen_pcm_pc_repository_pc_OperationProvidedRole_ProvidedRole = Generalization(general=ProvidedRole, specific=pcm_pc_repository_pc_OperationProvidedRole)
gen_pcm_pc_repository_pc_CompositeComponent_entity_pc_ComposedProvidingRequiringEntity = Generalization(general=entity_pc_ComposedProvidingRequiringEntity, specific=pcm_pc_repository_pc_CompositeComponent)
gen_pcm_pc_repository_pc_CompositeComponent_repository_pc_ImplementationComponentType = Generalization(general=repository_pc_ImplementationComponentType, specific=pcm_pc_repository_pc_CompositeComponent)
gen_pcm_pc_repository_pc_PrimitiveDataType_DataType = Generalization(general=DataType, specific=pcm_pc_repository_pc_PrimitiveDataType)
gen_pcm_pc_repository_pc_CollectionDataType_entity_pc_Entity = Generalization(general=entity_pc_Entity, specific=pcm_pc_repository_pc_CollectionDataType)
gen_pcm_pc_repository_pc_CollectionDataType_repository_pc_DataType = Generalization(general=repository_pc_DataType, specific=pcm_pc_repository_pc_CollectionDataType)
gen_pcm_pc_repository_pc_CompositeDataType_entity_pc_Entity = Generalization(general=entity_pc_Entity, specific=pcm_pc_repository_pc_CompositeDataType)
gen_pcm_pc_repository_pc_CompositeDataType_repository_pc_DataType = Generalization(general=repository_pc_DataType, specific=pcm_pc_repository_pc_CompositeDataType)
gen_pcm_pc_repository_pc_Role_Entity = Generalization(general=Entity, specific=pcm_pc_repository_pc_Role)
gen_pcm_pc_resourcetype_pc_ResourceSignature_Entity = Generalization(general=Entity, specific=pcm_pc_resourcetype_pc_ResourceSignature)
gen_pcm_pc_resourcetype_pc_ProcessingResourceType_ResourceType = Generalization(general=ResourceType, specific=pcm_pc_resourcetype_pc_ProcessingResourceType)
gen_pcm_pc_resourcetype_pc_ResourceType_entity_pc_Entity = Generalization(general=entity_pc_Entity, specific=pcm_pc_resourcetype_pc_ResourceType)
gen_pcm_pc_resourcetype_pc_ResourceType_UnitCarryingElement = Generalization(general=UnitCarryingElement, specific=pcm_pc_resourcetype_pc_ResourceType)
gen_pcm_pc_resourcetype_pc_ResourceType_entity_pc_ResourceInterfaceProvidingEntity = Generalization(general=entity_pc_ResourceInterfaceProvidingEntity, specific=pcm_pc_resourcetype_pc_ResourceType)
gen_pcm_pc_resourcetype_pc_SchedulingPolicy_Entity = Generalization(general=Entity, specific=pcm_pc_resourcetype_pc_SchedulingPolicy)
gen_pcm_pc_repository_pc_InnerDeclaration_NamedElement = Generalization(general=NamedElement, specific=pcm_pc_repository_pc_InnerDeclaration)
gen_pcm_pc_resourcetype_pc_CommunicationLinkResourceType_ResourceType = Generalization(general=ResourceType, specific=pcm_pc_resourcetype_pc_CommunicationLinkResourceType)
gen_pcm_pc_resourcetype_pc_ResourceInterface_Entity = Generalization(general=Entity, specific=pcm_pc_resourcetype_pc_ResourceInterface)
gen_pcm_pc_parameter_pc_CharacterisedVariable_Variable = Generalization(general=Variable, specific=pcm_pc_parameter_pc_CharacterisedVariable)
gen_pcm_pc_reliability_pc_HardwareInducedFailureType_FailureType = Generalization(general=FailureType, specific=pcm_pc_reliability_pc_HardwareInducedFailureType)
gen_pcm_pc_reliability_pc_InternalFailureOccurrenceDescription_FailureOccurrenceDescription = Generalization(general=FailureOccurrenceDescription, specific=pcm_pc_reliability_pc_InternalFailureOccurrenceDescription)
gen_pcm_pc_reliability_pc_NetworkInducedFailureType_FailureType = Generalization(general=FailureType, specific=pcm_pc_reliability_pc_NetworkInducedFailureType)
gen_pcm_pc_reliability_pc_ExternalFailureOccurrenceDescription_FailureOccurrenceDescription = Generalization(general=FailureOccurrenceDescription, specific=pcm_pc_reliability_pc_ExternalFailureOccurrenceDescription)
gen_pcm_pc_reliability_pc_SoftwareInducedFailureType_FailureType = Generalization(general=FailureType, specific=pcm_pc_reliability_pc_SoftwareInducedFailureType)
gen_pcm_pc_reliability_pc_FailureType_Entity = Generalization(general=Entity, specific=pcm_pc_reliability_pc_FailureType)
gen_pcm_pc_seff_pc_StopAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_pc_seff_pc_StopAction)
gen_pcm_pc_seff_pc_AbstractInternalControlFlowAction_AbstractAction = Generalization(general=AbstractAction, specific=pcm_pc_seff_pc_AbstractInternalControlFlowAction)
gen_pcm_pc_seff_pc_AbstractAction_Entity = Generalization(general=Entity, specific=pcm_pc_seff_pc_AbstractAction)
gen_pcm_pc_reliability_pc_ResourceTimeoutFailureType_SoftwareInducedFailureType = Generalization(general=SoftwareInducedFailureType, specific=pcm_pc_reliability_pc_ResourceTimeoutFailureType)
gen_pcm_pc_seff_pc_AbstractLoopAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_pc_seff_pc_AbstractLoopAction)
gen_pcm_pc_seff_pc_AbstractBranchTransition_Entity = Generalization(general=Entity, specific=pcm_pc_seff_pc_AbstractBranchTransition)
gen_pcm_pc_seff_pc_ResourceDemandingBehaviour_Identifier = Generalization(general=Identifier, specific=pcm_pc_seff_pc_ResourceDemandingBehaviour)
gen_pcm_pc_seff_pc_BranchAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_pc_seff_pc_BranchAction)
gen_pcm_pc_seff_pc_StartAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_pc_seff_pc_StartAction)
gen_pcm_pc_seff_pc_ResourceDemandingSEFF_Identifier = Generalization(general=Identifier, specific=pcm_pc_seff_pc_ResourceDemandingSEFF)
gen_pcm_pc_seff_pc_ResourceDemandingInternalBehaviour_ResourceDemandingBehaviour = Generalization(general=ResourceDemandingBehaviour, specific=pcm_pc_seff_pc_ResourceDemandingInternalBehaviour)
gen_pcm_pc_seff_pc_ReleaseAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_pc_seff_pc_ReleaseAction)
gen_pcm_pc_seff_pc_LoopAction_AbstractLoopAction = Generalization(general=AbstractLoopAction, specific=pcm_pc_seff_pc_LoopAction)
gen_pcm_pc_seff_pc_ForkAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_pc_seff_pc_ForkAction)
gen_pcm_pc_seff_pc_ForkedBehaviour_ResourceDemandingBehaviour = Generalization(general=ResourceDemandingBehaviour, specific=pcm_pc_seff_pc_ForkedBehaviour)
gen_pcm_pc_seff_pc_CallReturnAction_CallAction = Generalization(general=CallAction, specific=pcm_pc_seff_pc_CallReturnAction)
gen_pcm_pc_seff_pc_ResourceDemandingSEFF_seff_pc_ServiceEffectSpecification = Generalization(general=seff_pc_ServiceEffectSpecification, specific=pcm_pc_seff_pc_ResourceDemandingSEFF)
gen_pcm_pc_seff_pc_ResourceDemandingSEFF_seff_pc_ResourceDemandingBehaviour = Generalization(general=seff_pc_ResourceDemandingBehaviour, specific=pcm_pc_seff_pc_ResourceDemandingSEFF)
gen_pcm_pc_seff_pc_ProbabilisticBranchTransition_AbstractBranchTransition = Generalization(general=AbstractBranchTransition, specific=pcm_pc_seff_pc_ProbabilisticBranchTransition)
gen_pcm_pc_seff_pc_AcquireAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_pc_seff_pc_AcquireAction)
gen_pcm_pc_seff_pc_ExternalCallAction_seff_pc_AbstractAction = Generalization(general=seff_pc_AbstractAction, specific=pcm_pc_seff_pc_ExternalCallAction)
gen_pcm_pc_seff_pc_ExternalCallAction_seff_pc_CallReturnAction = Generalization(general=seff_pc_CallReturnAction, specific=pcm_pc_seff_pc_ExternalCallAction)
gen_pcm_pc_seff_pc_ExternalCallAction_seff_reliability_pc_FailureHandlingEntity = Generalization(general=seff_reliability_pc_FailureHandlingEntity, specific=pcm_pc_seff_pc_ExternalCallAction)
gen_pcm_pc_seff_pc_SetVariableAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_pc_seff_pc_SetVariableAction)
gen_pcm_pc_seff_pc_InternalCallAction_seff_pc_CallAction = Generalization(general=seff_pc_CallAction, specific=pcm_pc_seff_pc_InternalCallAction)
gen_pcm_pc_seff_pc_InternalCallAction_seff_pc_AbstractInternalControlFlowAction = Generalization(general=seff_pc_AbstractInternalControlFlowAction, specific=pcm_pc_seff_pc_InternalCallAction)
gen_pcm_pc_seff_pc_EmitEventAction_seff_pc_AbstractAction = Generalization(general=seff_pc_AbstractAction, specific=pcm_pc_seff_pc_EmitEventAction)
gen_pcm_pc_seff_pc_EmitEventAction_seff_pc_CallAction = Generalization(general=seff_pc_CallAction, specific=pcm_pc_seff_pc_EmitEventAction)
gen_pcm_pc_seff_pc_InternalAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_pc_seff_pc_InternalAction)
gen_pcm_pc_seff_pc_CollectionIteratorAction_AbstractLoopAction = Generalization(general=AbstractLoopAction, specific=pcm_pc_seff_pc_CollectionIteratorAction)
gen_pcm_pc_seff_pc_GuardedBranchTransition_AbstractBranchTransition = Generalization(general=AbstractBranchTransition, specific=pcm_pc_seff_pc_GuardedBranchTransition)
gen_pcm_pc_seff_performance_pc_ResourceCall_CallAction = Generalization(general=CallAction, specific=pcm_pc_seff_performance_pc_ResourceCall)
gen_pcm_pc_seff_performance_pc_InfrastructureCall_CallAction = Generalization(general=CallAction, specific=pcm_pc_seff_performance_pc_InfrastructureCall)
gen_pcm_pc_seff_reliability_pc_RecoveryActionBehaviour_seff_reliability_pc_FailureHandlingEntity = Generalization(general=seff_reliability_pc_FailureHandlingEntity, specific=pcm_pc_seff_reliability_pc_RecoveryActionBehaviour)
gen_pcm_pc_seff_reliability_pc_RecoveryActionBehaviour_seff_pc_ResourceDemandingBehaviour = Generalization(general=seff_pc_ResourceDemandingBehaviour, specific=pcm_pc_seff_reliability_pc_RecoveryActionBehaviour)
gen_pcm_pc_seff_reliability_pc_FailureHandlingEntity_Entity = Generalization(general=Entity, specific=pcm_pc_seff_reliability_pc_FailureHandlingEntity)
gen_pcm_pc_qosannotations_pc_QoSAnnotations_Entity = Generalization(general=Entity, specific=pcm_pc_qosannotations_pc_QoSAnnotations)
gen_pcm_pc_seff_reliability_pc_RecoveryAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_pc_seff_reliability_pc_RecoveryAction)
gen_pcm_pc_qos_performance_pc_SystemSpecifiedExecutionTime_SpecifiedExecutionTime = Generalization(general=SpecifiedExecutionTime, specific=pcm_pc_qos_performance_pc_SystemSpecifiedExecutionTime)
gen_pcm_pc_system_pc_System_entity_pc_Entity = Generalization(general=entity_pc_Entity, specific=pcm_pc_system_pc_System)
gen_pcm_pc_system_pc_System_entity_pc_ComposedProvidingRequiringEntity = Generalization(general=entity_pc_ComposedProvidingRequiringEntity, specific=pcm_pc_system_pc_System)
gen_pcm_pc_qos_performance_pc_SpecifiedExecutionTime_SpecifiedQoSAnnotation = Generalization(general=SpecifiedQoSAnnotation, specific=pcm_pc_qos_performance_pc_SpecifiedExecutionTime)
gen_pcm_pc_qos_performance_pc_ComponentSpecifiedExecutionTime_SpecifiedExecutionTime = Generalization(general=SpecifiedExecutionTime, specific=pcm_pc_qos_performance_pc_ComponentSpecifiedExecutionTime)
gen_pcm_pc_qos_reliability_pc_SpecifiedReliabilityAnnotation_SpecifiedQoSAnnotation = Generalization(general=SpecifiedQoSAnnotation, specific=pcm_pc_qos_reliability_pc_SpecifiedReliabilityAnnotation)
gen_pcm_pc_resourceenvironment_pc_LinkingResource_Entity = Generalization(general=Entity, specific=pcm_pc_resourceenvironment_pc_LinkingResource)
gen_pcm_pc_resourceenvironment_pc_ResourceContainer_Entity = Generalization(general=Entity, specific=pcm_pc_resourceenvironment_pc_ResourceContainer)
gen_pcm_pc_resourceenvironment_pc_ProcessingResourceSpecification_Identifier = Generalization(general=Identifier, specific=pcm_pc_resourceenvironment_pc_ProcessingResourceSpecification)
gen_pcm_pc_resourceenvironment_pc_ResourceEnvironment_NamedElement = Generalization(general=NamedElement, specific=pcm_pc_resourceenvironment_pc_ResourceEnvironment)
gen_pcm_pc_allocation_pc_AllocationContext_Entity = Generalization(general=Entity, specific=pcm_pc_allocation_pc_AllocationContext)
gen_pcm_pc_allocation_pc_Allocation_Entity = Generalization(general=Entity, specific=pcm_pc_allocation_pc_Allocation)
gen_pcm_pc_resourceenvironment_pc_CommunicationLinkResourceSpecification_Identifier = Generalization(general=Identifier, specific=pcm_pc_resourceenvironment_pc_CommunicationLinkResourceSpecification)
gen_pcm_pc_subsystem_pc_SubSystem_entity_pc_ComposedProvidingRequiringEntity = Generalization(general=entity_pc_ComposedProvidingRequiringEntity, specific=pcm_pc_subsystem_pc_SubSystem)
gen_pcm_pc_subsystem_pc_SubSystem_repository_pc_RepositoryComponent = Generalization(general=repository_pc_RepositoryComponent, specific=pcm_pc_subsystem_pc_SubSystem)
gen_pcm_pc_completions_pc_Completion_entity_pc_ComposedProvidingRequiringEntity = Generalization(general=entity_pc_ComposedProvidingRequiringEntity, specific=pcm_pc_completions_pc_Completion)
gen_pcm_pc_completions_pc_Completion_repository_pc_ImplementationComponentType = Generalization(general=repository_pc_ImplementationComponentType, specific=pcm_pc_completions_pc_Completion)
gen_pcm_pc_completions_pc_DelegatingExternalCallAction_ExternalCallAction = Generalization(general=ExternalCallAction, specific=pcm_pc_completions_pc_DelegatingExternalCallAction)
gen_pcm_pc_completions_pc_NetworkDemandParametricResourceDemand_ParametricResourceDemand = Generalization(general=ParametricResourceDemand, specific=pcm_pc_completions_pc_NetworkDemandParametricResourceDemand)

# Domain Model
domain_model = DomainModel(
    name="pcm_pc",
    types={pcm_pc_DummyClass, pcm_pc_Pointcut, pcm_pc_EObject, pcm_pc_core_pc_PCMRandomVariable, RandomVariable, VariableCharacterisation, seff_performance_pc_InfrastructureCall, seff_performance_pc_ResourceCall, seff_performance_pc_ParametricResourceDemand, LoopAction, GuardedBranchTransition, qos_performance_pc_SpecifiedExecutionTime, composition_pc_EventChannelSinkConnector, ClosedWorkload, PassiveResource, CommunicationLinkResourceSpecification, ProcessingResourceSpecification, pcm_pc_entity_pc_ResourceProvidedRole, Role, entity_pc_ResourceInterfaceProvidingEntity, ResourceInterface, pcm_pc_entity_pc_InterfaceProvidingRequiringEntity, entity_pc_InterfaceProvidingEntity, entity_pc_InterfaceRequiringEntity, composition_pc_AssemblyEventConnector, pcm_pc_entity_pc_InterfaceProvidingEntity, Loop, Entity, OpenWorkload, ProvidedRole, pcm_pc_entity_pc_InterfaceRequiringEntity, Delay, RequiredRole, pcm_pc_entity_pc_ResourceInterfaceRequiringEntity, entity_pc_ResourceRequiredRole, pcm_pc_entity_pc_ResourceRequiredRole, pcm_pc_entity_pc_ResourceInterfaceProvidingEntity, entity_pc_ResourceProvidedRole, entity_pc_Entity, entity_pc_ResourceInterfaceRequiringEntity, pcm_pc_entity_pc_NamedElement, pcm_pc_entity_pc_ResourceInterfaceProvidingRequiringEntity, pcm_pc_entity_pc_Entity, Identifier, entity_pc_NamedElement, pcm_pc_composition_pc_DelegationConnector, Connector, pcm_pc_composition_pc_Connector, pcm_pc_composition_pc_ComposedStructure, pcm_pc_entity_pc_ComposedProvidingRequiringEntity, composition_pc_ComposedStructure, entity_pc_InterfaceProvidingRequiringEntity, composition_pc_AssemblyContext, composition_pc_ResourceRequiredDelegationConnector, composition_pc_EventChannel, composition_pc_Connector, EventGroup, composition_pc_EventChannelSourceConnector, pcm_pc_composition_pc_EventChannelSourceConnector, SourceRole, pcm_pc_composition_pc_EventChannelSinkConnector, SinkRole, PCMRandomVariable, pcm_pc_composition_pc_ProvidedDelegationConnector, DelegationConnector, pcm_pc_composition_pc_ResourceRequiredDelegationConnector, pcm_pc_composition_pc_EventChannel, OperationProvidedRole, pcm_pc_composition_pc_RequiredDelegationConnector, OperationRequiredRole, pcm_pc_composition_pc_AssemblyEventConnector, pcm_pc_composition_pc_AssemblyConnector, pcm_pc_composition_pc_SourceDelegationConnector, pcm_pc_composition_pc_SinkDelegationConnector, pcm_pc_composition_pc_AssemblyInfrastructureConnector, InfrastructureProvidedRole, InfrastructureRequiredRole, pcm_pc_composition_pc_ProvidedInfrastructureDelegationConnector, pcm_pc_composition_pc_RequiredResourceDelegationConnector, pcm_pc_composition_pc_AssemblyContext, RepositoryComponent, VariableUsage, pcm_pc_usagemodel_pc_Workload, UsageScenario, pcm_pc_usagemodel_pc_UsageScenario, UsageModel, ScenarioBehaviour, Workload, pcm_pc_usagemodel_pc_UserData, pcm_pc_composition_pc_RequiredInfrastructureDelegationConnector, UserData, pcm_pc_usagemodel_pc_UsageModel, OperationSignature, pcm_pc_usagemodel_pc_AbstractUserAction, pcm_pc_usagemodel_pc_EntryLevelSystemCall, AbstractUserAction, pcm_pc_usagemodel_pc_ScenarioBehaviour, BranchTransition, pcm_pc_usagemodel_pc_BranchTransition, pcm_pc_usagemodel_pc_Loop, pcm_pc_usagemodel_pc_Stop, pcm_pc_usagemodel_pc_Start, Branch, pcm_pc_usagemodel_pc_Branch, pcm_pc_usagemodel_pc_Delay, pcm_pc_usagemodel_pc_ClosedWorkload, pcm_pc_repository_pc_PassiveResource, pcm_pc_usagemodel_pc_OpenWorkload, ResourceTimeoutFailureType, pcm_pc_repository_pc_BasicComponent, ImplementationComponentType, ServiceEffectSpecification, pcm_pc_repository_pc_ImplementationComponentType, BasicComponent, CompleteComponentType, pcm_pc_repository_pc_RepositoryComponent, InterfaceProvidingRequiringEntity, Repository, pcm_pc_repository_pc_ProvidedRole, pcm_pc_repository_pc_Parameter, DataType, EventType, ResourceSignature, pcm_pc_repository_pc_DataType, pcm_pc_repository_pc_Repository, Interface, FailureType, pcm_pc_repository_pc_Interface, InfrastructureSignature, Protocol, RequiredCharacterisation, pcm_pc_repository_pc_RequiredCharacterisation, Parameter_, pcm_pc_repository_pc_EventGroup, pcm_pc_repository_pc_EventType, Signature, pcm_pc_repository_pc_Signature, ExceptionType, pcm_pc_repository_pc_InfrastructureSignature, InfrastructureInterface, pcm_pc_repository_pc_InfrastructureInterface, pcm_pc_repository_pc_InfrastructureRequiredRole, pcm_pc_repository_pc_RequiredRole, pcm_pc_repository_pc_OperationSignature, OperationInterface, pcm_pc_repository_pc_ExceptionType, pcm_pc_repository_pc_OperationInterface, pcm_pc_repository_pc_OperationRequiredRole, pcm_pc_repository_pc_SourceRole, pcm_pc_repository_pc_SinkRole, pcm_pc_repository_pc_InfrastructureProvidedRole, pcm_pc_repository_pc_CompleteComponentType, ProvidesComponentType, pcm_pc_repository_pc_ProvidesComponentType, pcm_pc_repository_pc_OperationProvidedRole, pcm_pc_repository_pc_CompositeComponent, entity_pc_ComposedProvidingRequiringEntity, repository_pc_ImplementationComponentType, pcm_pc_repository_pc_PrimitiveDataType, pcm_pc_repository_pc_CollectionDataType, repository_pc_DataType, pcm_pc_repository_pc_CompositeDataType, CompositeDataType, pcm_pc_repository_pc_Role, pcm_pc_resourcetype_pc_ResourceSignature, pcm_pc_resourcetype_pc_ProcessingResourceType, ResourceType, HardwareInducedFailureType, pcm_pc_resourcetype_pc_ResourceType, UnitCarryingElement, ResourceRepository, pcm_pc_resourcetype_pc_ResourceRepository, SchedulingPolicy, pcm_pc_resourcetype_pc_SchedulingPolicy, InnerDeclaration, pcm_pc_repository_pc_InnerDeclaration, NamedElement, pcm_pc_protocol_pc_Protocol, pcm_pc_parameter_pc_VariableUsage, CallAction, SynchronisationPoint, CallReturnAction, SetVariableAction, SpecifiedOutputParameterAbstraction, EntryLevelSystemCall, parameter_pc_pcm_pc_AbstractNamedReference, pcm_pc_parameter_pc_VariableCharacterisation, pcm_pc_resourcetype_pc_CommunicationLinkResourceType, NetworkInducedFailureType, pcm_pc_resourcetype_pc_ResourceInterface, pcm_pc_parameter_pc_CharacterisedVariable, Variable, pcm_pc_reliability_pc_FailureOccurrenceDescription, pcm_pc_reliability_pc_HardwareInducedFailureType, ProcessingResourceType, InternalFailureOccurrenceDescription, pcm_pc_reliability_pc_InternalFailureOccurrenceDescription, FailureOccurrenceDescription, InternalAction, SoftwareInducedFailureType, pcm_pc_reliability_pc_NetworkInducedFailureType, CommunicationLinkResourceType, pcm_pc_reliability_pc_ExternalFailureOccurrenceDescription, qos_reliability_pc_SpecifiedReliabilityAnnotation, pcm_pc_reliability_pc_SoftwareInducedFailureType, pcm_pc_reliability_pc_FailureType, pcm_pc_seff_pc_StopAction, AbstractInternalControlFlowAction, pcm_pc_seff_pc_AbstractInternalControlFlowAction, AbstractAction, pcm_pc_seff_pc_AbstractAction, ResourceDemandingBehaviour, pcm_pc_reliability_pc_ResourceTimeoutFailureType, AbstractLoopAction, AbstractBranchTransition, pcm_pc_seff_pc_AbstractLoopAction, pcm_pc_seff_pc_AbstractBranchTransition, pcm_pc_seff_pc_ResourceDemandingBehaviour, BranchAction, pcm_pc_seff_pc_BranchAction, pcm_pc_seff_pc_CallAction, pcm_pc_seff_pc_StartAction, pcm_pc_seff_pc_ServiceEffectSpecification, pcm_pc_seff_pc_ResourceDemandingSEFF, ResourceDemandingInternalBehaviour, pcm_pc_seff_pc_ResourceDemandingInternalBehaviour, ResourceDemandingSEFF, pcm_pc_seff_pc_ReleaseAction, pcm_pc_seff_pc_LoopAction, pcm_pc_seff_pc_ForkAction, ForkedBehaviour, pcm_pc_seff_pc_ForkedBehaviour, pcm_pc_seff_pc_CallReturnAction, seff_pc_ServiceEffectSpecification, seff_pc_ResourceDemandingBehaviour, pcm_pc_seff_pc_ProbabilisticBranchTransition, pcm_pc_seff_pc_AcquireAction, ForkAction, pcm_pc_seff_pc_SynchronisationPoint, pcm_pc_seff_pc_ExternalCallAction, seff_pc_AbstractAction, seff_pc_CallReturnAction, seff_reliability_pc_FailureHandlingEntity, pcm_pc_seff_pc_SetVariableAction, pcm_pc_seff_pc_InternalCallAction, seff_pc_CallAction, seff_pc_AbstractInternalControlFlowAction, pcm_pc_seff_pc_EmitEventAction, pcm_pc_seff_pc_InternalAction, pcm_pc_seff_pc_CollectionIteratorAction, pcm_pc_seff_pc_GuardedBranchTransition, pcm_pc_seff_performance_pc_ResourceCall, pcm_pc_seff_performance_pc_InfrastructureCall, pcm_pc_seff_reliability_pc_RecoveryActionBehaviour, pcm_pc_seff_performance_pc_ParametricResourceDemand, pcm_pc_seff_reliability_pc_FailureHandlingEntity, pcm_pc_qosannotations_pc_SpecifiedQoSAnnotation, QoSAnnotations, pcm_pc_qosannotations_pc_QoSAnnotations, seff_reliability_pc_RecoveryActionBehaviour, seff_reliability_pc_RecoveryAction, pcm_pc_seff_reliability_pc_RecoveryAction, System, SpecifiedQoSAnnotation, pcm_pc_qosannotations_pc_SpecifiedOutputParameterAbstraction, pcm_pc_qos_performance_pc_SystemSpecifiedExecutionTime, SpecifiedExecutionTime, ExternalFailureOccurrenceDescription, pcm_pc_system_pc_System, pcm_pc_qos_performance_pc_SpecifiedExecutionTime, pcm_pc_qos_performance_pc_ComponentSpecifiedExecutionTime, pcm_pc_qos_reliability_pc_SpecifiedReliabilityAnnotation, pcm_pc_resourceenvironment_pc_LinkingResource, ResourceEnvironment, pcm_pc_resourceenvironment_pc_ResourceContainer, pcm_pc_resourceenvironment_pc_ProcessingResourceSpecification, pcm_pc_resourceenvironment_pc_ResourceEnvironment, LinkingResource, ResourceContainer, pcm_pc_allocation_pc_AllocationContext, Allocation, pcm_pc_allocation_pc_Allocation, pcm_pc_resourceenvironment_pc_CommunicationLinkResourceSpecification, AllocationContext, pcm_pc_subsystem_pc_SubSystem, repository_pc_RepositoryComponent, pcm_pc_completions_pc_Completion, pcm_pc_completions_pc_CompletionRepository, Completion, pcm_pc_completions_pc_DelegatingExternalCallAction, ExternalCallAction, pcm_pc_completions_pc_NetworkDemandParametricResourceDemand, ParametricResourceDemand, ParameterModifier, ComponentType, PrimitiveTypeEnum, VariableCharacterisationType},
    associations={children0, passiveResource_capacity_PCMRandomVariable2, variableCharacterisation_Specification3, infrastructureCall__PCMRandomVariable4, resourceCall__PCMRandomVariable5, parametricResourceDemand_PCMRandomVariable6, loopAction_PCMRandomVariable7, guardedBranchTransition_PCMRandomVariable8, specifiedExecutionTime_PCMRandomVariable9, eventChannelSinkConnector__FilterCondition10, closedWorkload_PCMRandomVariable1, communicationLinkResourceSpecifcation_throughput_PCMRandomVariable15, processingResourceSpecification_processingRate_PCMRandomVariable16, communicationLinkResourceSpecification_latency_PCMRandomVariable17, resourceInterfaceProvidingEntity__ResourceProvidedRole19, providedResourceInterface__ResourceProvidedRole20, assemblyEventConnector__FilterCondition11, loop_LoopIteration12, openWorkload_PCMRandomVariable13, providedRoles_InterfaceProvidingEntity21, delay_TimeSpecification14, requiredRoles_InterfaceRequiringEntity22, resourceRequiredRoles__ResourceInterfaceRequiringEntity23, requiredResourceInterface__ResourceRequiredRole24, resourceInterfaceRequiringEntity__ResourceRequiredRole26, resourceProvidedRoles__ResourceInterfaceProvidingEntity27, parentStructure__Connector28, assemblyContexts__ComposedStructure29, resourceRequiredDelegationConnectors_ComposedStructure30, eventChannel__ComposedStructure31, connectors__ComposedStructure32, eventGroup__EventChannel39, eventChannelSourceConnector__EventChannel40, eventChannelSinkConnector__EventChannel41, parentStructure__EventChannel43, sourceRole__EventChannelSourceRole45, assemblyContext__EventChannelSourceConnector46, eventChannel__EventChannelSourceConnector48, sinkRole__EventChannelSinkConnector50, filterCondition__EventChannelSinkConnector51, assemblyContext__EventChannelSinkConnector52, eventChannel__EventChannelSinkConnector55, innerResourceRequiredRole_ResourceRequiredDelegationConnector33, outerResourceRequiredRole_ResourceRequiredDelegationConnector34, parentStructure_ResourceRequiredDelegationConnector37, innerProvidedRole_ProvidedDelegationConnector57, outerProvidedRole_ProvidedDelegationConnector58, assemblyContext_ProvidedDelegationConnector61, innerRequiredRole_RequiredDelegationConnector64, outerRequiredRole_RequiredDelegationConnector65, requiringAssemblyContext_AssemblyConnector71, providingAssemblyContext_AssemblyConnector73, providedRole_AssemblyConnector76, requiredRole_AssemblyConnector79, sinkRole__AssemblyEventConnector82, assemblyContext_RequiredDelegationConnector68, filterCondition__AssemblyEventConnector93, innerSourceRole__SourceRole95, outerSourceRole__SourceRole97, assemblyContext__SourceDelegationConnector100, assemblyContext__SinkDelegationConnector103, innerSinkRole__SinkRole105, outerSinkRole__SinkRole108, providedRole__AssemblyInfrastructureConnector111, requiredRole__AssemblyInfrastructureConnector112, providingAssemblyContext__AssemblyInfrastructureConnector114, requiringAssemblyContext__AssemblyInfrastructureConnector117, innerProvidedRole__ProvidedInfrastructureDelegationConnector120, outerProvidedRole__ProvidedInfrastructureDelegationConnector122, assemblyContext__ProvidedInfrastructureDelegationConnector125, sourceRole__AssemblyEventConnector84, sinkAssemblyContext__AssemblyEventConnector87, sourceAssemblyContext__AssemblyEventConnector90, assemblyContext__RequiredResourceDelegationConnector136, innerRequiredRole__RequiredResourceDelegationConnector138, outerRequiredRole__RequiredResourceDelegationConnector141, parentStructure__AssemblyContext144, encapsulatedComponent__AssemblyContext146, configParameterUsages__AssemblyContext147, usageScenario_Workload148, usageModel_UsageScenario149, scenarioBehaviour_UsageScenario150, workload_UsageScenario151, innerRequiredRole__RequiredInfrastructureDelegationConnector128, outerRequiredRole__RequiredInfrastructureDelegationConnector130, assemblyContext__RequiredInfrastructureDelegationConnector133, usageScenario_UsageModel158, assemblyContext_userData152, usageModel_UserData154, userDataParameterUsages_UserData156, providedRole_EntryLevelSystemCall161, operationSignature__EntryLevelSystemCall163, outputParameterUsages_EntryLevelSystemCall165, inputParameterUsages_EntryLevelSystemCall167, userData_UsageModel160, usageScenario_SenarioBehaviour174, branchTransition_ScenarioBehaviour176, loop_ScenarioBehaviour177, actions_ScenarioBehaviour179, successor169, predecessor170, scenarioBehaviour_AbstractUserAction172, branchTransitions_Branch184, loopIteration_Loop186, bodyBehaviour_Loop188, branch_BranchTransition181, branchedBehaviour_BranchTransition182, interArrivalTime_OpenWorkload190, timeSpecification_Delay192, thinkTime_ClosedWorkload194, resourceTimeoutFailureType__PassiveResource199, serviceEffectSpecifications__BasicComponent200, passiveResource_BasicComponent201, capacity_PassiveResource196, basicComponent_PassiveResource198, parentCompleteComponentTypes203, componentParameterUsage_ImplementationComponentType204, repository__RepositoryComponent207, providingEntity_ProvidedRole208, dataType__Parameter209, eventType__Parameter213, resourceSignature__Parameter214, repository__DataType215, components__Repository217, interfaces__Repository219, failureTypes__Repository220, dataTypes__Repository221, infrastructureSignature__Parameter210, operationSignature__Parameter211, protocols__Interface225, requiredCharacterisations227, repository__Interface228, parameter230, interface_RequiredCharacterisation231, eventTypes__EventGroup233, parameter__EventType235, eventGroup__EventType237, exceptions__Signature239, failureType240, parentInterfaces__Interface223, parameters__InfrastructureSignature243, infrastructureInterface__InfrastructureSignature245, infrastructureSignatures__InfrastructureInterface246, requiredInterface__InfrastructureRequiredRole248, requiringEntity_RequiredRole250, interface__OperationSignature251, parameters__OperationSignature252, signatures__OperationInterface256, requiredInterface__OperationRequiredRole258, eventGroup__SourceRole260, returnType__OperationSignature254, providedInterface__OperationProvidedRole264, providedInterface__InfrastructureProvidedRole266, parentProvidesComponentTypes268, eventGroup__SinkRole262, innerType_CollectionDataType269, parentType_CompositeDataType271, datatype_InnerDeclaration273, compositeDataType_InnerDeclaration275, parameter__ResourceSignature277, resourceInterface__ResourceSignature279, hardwareInducedFailureType__ProcessingResourceType281, resourceRepository_ResourceType282, resourceInterfaces__ResourceRepository283, schedulingPolicies__ResourceRepository285, availableResourceTypes_ResourceRepository286, resourceRepository__SchedulingPolicy287, innerDeclaration_CompositeDataType272, resourceRepository__ResourceInterface290, resourceSignatures__ResourceInterface292, variableCharacterisation_VariableUsage294, userData_VariableUsage296, callAction__VariableUsage298, synchronisationPoint_VariableUsage299, callReturnAction__VariableUsage300, setVariableAction_VariableUsage301, specifiedOutputParameterAbstraction_expectedExternalOutputs_VariableUsage302, assemblyContext__VariableUsage303, entryLevelSystemCall_InputParameterUsage305, entryLevelSystemCall_OutputParameterUsage306, namedReference__VariableUsage308, networkInducedFailureType__CommunicationLinkResourceType289, variableUsage_VariableCharacterisation311, specification_VariableCharacterisation309, internalFailureOccurrenceDescriptions__SoftwareInducedFailureType314, internalAction__InternalFailureOccurrenceDescription315, softwareInducedFailureType__InternalFailureOccurrenceDescription316, communicationLinkResourceType__NetworkInducedFailureType317, specifiedReliabilityAnnotation__ExternalFailureOccurrenceDescription318, processingResourceType__HardwareInducedFailureType313, failureType__ExternalFailureOccurrenceDescription319, passiveResource__ResourceTimeoutFailureType321, repository__FailureType323, resourceDemand_Action325, infrastructureCall__Action327, resourceCall__Action329, predecessor_AbstractAction331, successor_AbstractAction332, resourceDemandingBehaviour_AbstractAction334, abstractLoopAction_ResourceDemandingBehaviour335, abstractBranchTransition_ResourceDemandingBehaviour337, steps_Behaviour338, bodyBehaviour_Loop340, branchAction_AbstractBranchTransition342, branches_Branch345, inputVariableUsages__CallAction347, describedService__SEFF349, basicComponent_ServiceEffectSpecification350, branchBehaviour_BranchTransition343, resourceDemandingInternalBehaviours352, resourceDemandingSEFF_ResourceDemandingInternalBehaviour353, passiveResource_ReleaseAction354, iterationCount_LoopAction356, asynchronousForkedBehaviours_ForkAction358, synchronisingBehaviours_ForkAction359, synchronisationPoint_ForkedBehaviour361, calledService_ExternalService370, role_ExternalService372, returnVariableUsage__CallReturnAction375, forkAction_ForkedBehaivour363, passiveresource_AcquireAction377, outputParameterUsage_SynchronisationPoint364, forkAction_SynchronisationPoint366, synchronousForkedBehaviours_SynchronisationPoint368, localVariableUsages_SetVariableAction383, calledResourceDemandingInternalBehaviour385, eventType__EmitEventAction387, sourceRole__EmitEventAction389, internalFailureOccurrenceDescriptions__InternalAction392, parameter_CollectionIteratorAction379, branchCondition_GuardedBranchTransition381, signature__InfrastructureCall394, numberOfCalls__InfrastructureCall396, action__InfrastructureCall398, requiredRole__InfrastructureCall399, specification_ParametericResourceDemand411, requiredResource_ParametricResourceDemand413, action_ParametricResourceDemand415, action__ResourceCall402, resourceRequiredRole__ResourceCall404, signature__ResourceCall406, numberOfCalls__ResourceCall409, primaryBehaviour__RecoveryAction419, recoveryActionBehaviours__RecoveryAction421, failureTypes_FailureHandlingEntity422, signature_SpecifiedQoSAnnation424, role_SpecifiedQoSAnnotation426, qosAnnotations_SpecifiedQoSAnnotation428, failureHandlingAlternatives__RecoveryActionBehaviour417, recoveryAction__RecoveryActionBehaviour418, specifiedOutputParameterAbstractions_QoSAnnotations429, system_QoSAnnotations431, specifiedQoSAnnotations_QoSAnnotations432, signature_SpecifiedOutputParameterAbstraction433, role_SpecifiedOutputParameterAbstraction435, expectedExternalOutputs_SpecifiedOutputParameterAbstraction438, qosAnnotations_SpecifiedOutputParameterAbstraction440, externalFailureOccurrenceDescriptions__SpecifiedReliabilityAnnotation446, specification_SpecifiedExecutionTime442, assemblyContext_ComponentSpecifiedExecutionTime444, connectedResourceContainers_LinkingResource451, communicationLinkResourceSpecifications_LinkingResource453, resourceEnvironment_LinkingResource455, activeResourceSpecifications_ResourceContainer456, resourceEnvironment_ResourceContainer458, nestedResourceContainers__ResourceContainer460, parentResourceContainer__ResourceContainer462, schedulingPolicy464, qosAnnotations_System447, linkingResources__ResourceEnvironment449, resourceContainer_ResourceEnvironment450, communicationLinkResourceType_CommunicationLinkResourceSpecification475, latency_CommunicationLinkResourceSpecification477, throughput_CommunicationLinkResourceSpecification479, resourceContainer_AllocationContext481, assemblyContext_AllocationContext483, allocation_AllocationContext486, eventChannel__AllocationContext487, activeResourceType_ActiveResourceSpecification466, processingRate_ProcessingResourceSpecification469, resourceContainer_ProcessingResourceSpecification471, linkingResource_CommunicationLinkResourceSpecification473, targetResourceEnvironment_Allocation489, system_Allocation491, allocationContexts_Allocation494, completions_CompletionRepository495, requiredCommunicationLinkResource_ParametricResourceDemand496},
    generalizations={gen_pcm_pc_core_pc_PCMRandomVariable_RandomVariable, gen_pcm_pc_entity_pc_ResourceProvidedRole_Role, gen_pcm_pc_entity_pc_InterfaceProvidingRequiringEntity_entity_pc_InterfaceProvidingEntity, gen_pcm_pc_entity_pc_InterfaceProvidingRequiringEntity_entity_pc_InterfaceRequiringEntity, gen_pcm_pc_entity_pc_InterfaceProvidingEntity_Entity, gen_pcm_pc_entity_pc_ResourceInterfaceRequiringEntity_Entity, gen_pcm_pc_entity_pc_ResourceRequiredRole_Role, gen_pcm_pc_entity_pc_ResourceInterfaceProvidingEntity_Entity, gen_pcm_pc_entity_pc_InterfaceRequiringEntity_entity_pc_Entity, gen_pcm_pc_entity_pc_InterfaceRequiringEntity_entity_pc_ResourceInterfaceRequiringEntity, gen_pcm_pc_entity_pc_ResourceInterfaceProvidingRequiringEntity_entity_pc_ResourceInterfaceRequiringEntity, gen_pcm_pc_entity_pc_ResourceInterfaceProvidingRequiringEntity_entity_pc_ResourceInterfaceProvidingEntity, gen_pcm_pc_entity_pc_Entity_Identifier, gen_pcm_pc_entity_pc_Entity_entity_pc_NamedElement, gen_pcm_pc_composition_pc_DelegationConnector_Connector, gen_pcm_pc_composition_pc_Connector_Entity, gen_pcm_pc_composition_pc_ComposedStructure_Entity, gen_pcm_pc_entity_pc_ComposedProvidingRequiringEntity_composition_pc_ComposedStructure, gen_pcm_pc_entity_pc_ComposedProvidingRequiringEntity_entity_pc_InterfaceProvidingRequiringEntity, gen_pcm_pc_composition_pc_EventChannel_Entity, gen_pcm_pc_composition_pc_EventChannelSourceConnector_Connector, gen_pcm_pc_composition_pc_EventChannelSinkConnector_Connector, gen_pcm_pc_composition_pc_ProvidedDelegationConnector_DelegationConnector, gen_pcm_pc_composition_pc_RequiredDelegationConnector_DelegationConnector, gen_pcm_pc_composition_pc_AssemblyEventConnector_Connector, gen_pcm_pc_composition_pc_AssemblyConnector_Connector, gen_pcm_pc_composition_pc_SourceDelegationConnector_DelegationConnector, gen_pcm_pc_composition_pc_SinkDelegationConnector_DelegationConnector, gen_pcm_pc_composition_pc_AssemblyInfrastructureConnector_Connector, gen_pcm_pc_composition_pc_ProvidedInfrastructureDelegationConnector_DelegationConnector, gen_pcm_pc_composition_pc_RequiredResourceDelegationConnector_DelegationConnector, gen_pcm_pc_composition_pc_AssemblyContext_Entity, gen_pcm_pc_usagemodel_pc_UsageScenario_Entity, gen_pcm_pc_composition_pc_RequiredInfrastructureDelegationConnector_DelegationConnector, gen_pcm_pc_usagemodel_pc_AbstractUserAction_Entity, gen_pcm_pc_usagemodel_pc_EntryLevelSystemCall_AbstractUserAction, gen_pcm_pc_usagemodel_pc_ScenarioBehaviour_Entity, gen_pcm_pc_usagemodel_pc_Loop_AbstractUserAction, gen_pcm_pc_usagemodel_pc_Stop_AbstractUserAction, gen_pcm_pc_usagemodel_pc_Start_AbstractUserAction, gen_pcm_pc_usagemodel_pc_Branch_AbstractUserAction, gen_pcm_pc_usagemodel_pc_Delay_AbstractUserAction, gen_pcm_pc_usagemodel_pc_ClosedWorkload_Workload, gen_pcm_pc_repository_pc_PassiveResource_Entity, gen_pcm_pc_usagemodel_pc_OpenWorkload_Workload, gen_pcm_pc_repository_pc_BasicComponent_ImplementationComponentType, gen_pcm_pc_repository_pc_ImplementationComponentType_RepositoryComponent, gen_pcm_pc_repository_pc_RepositoryComponent_InterfaceProvidingRequiringEntity, gen_pcm_pc_repository_pc_ProvidedRole_Role, gen_pcm_pc_repository_pc_Repository_Entity, gen_pcm_pc_repository_pc_Interface_Entity, gen_pcm_pc_repository_pc_EventGroup_Interface, gen_pcm_pc_repository_pc_EventType_Signature, gen_pcm_pc_repository_pc_Signature_Entity, gen_pcm_pc_repository_pc_InfrastructureSignature_Signature, gen_pcm_pc_repository_pc_InfrastructureInterface_Interface, gen_pcm_pc_repository_pc_InfrastructureRequiredRole_RequiredRole, gen_pcm_pc_repository_pc_RequiredRole_Role, gen_pcm_pc_repository_pc_OperationSignature_Signature, gen_pcm_pc_repository_pc_OperationInterface_Interface, gen_pcm_pc_repository_pc_OperationRequiredRole_RequiredRole, gen_pcm_pc_repository_pc_SourceRole_RequiredRole, gen_pcm_pc_repository_pc_InfrastructureProvidedRole_ProvidedRole, gen_pcm_pc_repository_pc_CompleteComponentType_RepositoryComponent, gen_pcm_pc_repository_pc_ProvidesComponentType_RepositoryComponent, gen_pcm_pc_repository_pc_SinkRole_ProvidedRole, gen_pcm_pc_repository_pc_OperationProvidedRole_ProvidedRole, gen_pcm_pc_repository_pc_CompositeComponent_entity_pc_ComposedProvidingRequiringEntity, gen_pcm_pc_repository_pc_CompositeComponent_repository_pc_ImplementationComponentType, gen_pcm_pc_repository_pc_PrimitiveDataType_DataType, gen_pcm_pc_repository_pc_CollectionDataType_entity_pc_Entity, gen_pcm_pc_repository_pc_CollectionDataType_repository_pc_DataType, gen_pcm_pc_repository_pc_CompositeDataType_entity_pc_Entity, gen_pcm_pc_repository_pc_CompositeDataType_repository_pc_DataType, gen_pcm_pc_repository_pc_Role_Entity, gen_pcm_pc_resourcetype_pc_ResourceSignature_Entity, gen_pcm_pc_resourcetype_pc_ProcessingResourceType_ResourceType, gen_pcm_pc_resourcetype_pc_ResourceType_entity_pc_Entity, gen_pcm_pc_resourcetype_pc_ResourceType_UnitCarryingElement, gen_pcm_pc_resourcetype_pc_ResourceType_entity_pc_ResourceInterfaceProvidingEntity, gen_pcm_pc_resourcetype_pc_SchedulingPolicy_Entity, gen_pcm_pc_repository_pc_InnerDeclaration_NamedElement, gen_pcm_pc_resourcetype_pc_CommunicationLinkResourceType_ResourceType, gen_pcm_pc_resourcetype_pc_ResourceInterface_Entity, gen_pcm_pc_parameter_pc_CharacterisedVariable_Variable, gen_pcm_pc_reliability_pc_HardwareInducedFailureType_FailureType, gen_pcm_pc_reliability_pc_InternalFailureOccurrenceDescription_FailureOccurrenceDescription, gen_pcm_pc_reliability_pc_NetworkInducedFailureType_FailureType, gen_pcm_pc_reliability_pc_ExternalFailureOccurrenceDescription_FailureOccurrenceDescription, gen_pcm_pc_reliability_pc_SoftwareInducedFailureType_FailureType, gen_pcm_pc_reliability_pc_FailureType_Entity, gen_pcm_pc_seff_pc_StopAction_AbstractInternalControlFlowAction, gen_pcm_pc_seff_pc_AbstractInternalControlFlowAction_AbstractAction, gen_pcm_pc_seff_pc_AbstractAction_Entity, gen_pcm_pc_reliability_pc_ResourceTimeoutFailureType_SoftwareInducedFailureType, gen_pcm_pc_seff_pc_AbstractLoopAction_AbstractInternalControlFlowAction, gen_pcm_pc_seff_pc_AbstractBranchTransition_Entity, gen_pcm_pc_seff_pc_ResourceDemandingBehaviour_Identifier, gen_pcm_pc_seff_pc_BranchAction_AbstractInternalControlFlowAction, gen_pcm_pc_seff_pc_StartAction_AbstractInternalControlFlowAction, gen_pcm_pc_seff_pc_ResourceDemandingSEFF_Identifier, gen_pcm_pc_seff_pc_ResourceDemandingInternalBehaviour_ResourceDemandingBehaviour, gen_pcm_pc_seff_pc_ReleaseAction_AbstractInternalControlFlowAction, gen_pcm_pc_seff_pc_LoopAction_AbstractLoopAction, gen_pcm_pc_seff_pc_ForkAction_AbstractInternalControlFlowAction, gen_pcm_pc_seff_pc_ForkedBehaviour_ResourceDemandingBehaviour, gen_pcm_pc_seff_pc_CallReturnAction_CallAction, gen_pcm_pc_seff_pc_ResourceDemandingSEFF_seff_pc_ServiceEffectSpecification, gen_pcm_pc_seff_pc_ResourceDemandingSEFF_seff_pc_ResourceDemandingBehaviour, gen_pcm_pc_seff_pc_ProbabilisticBranchTransition_AbstractBranchTransition, gen_pcm_pc_seff_pc_AcquireAction_AbstractInternalControlFlowAction, gen_pcm_pc_seff_pc_ExternalCallAction_seff_pc_AbstractAction, gen_pcm_pc_seff_pc_ExternalCallAction_seff_pc_CallReturnAction, gen_pcm_pc_seff_pc_ExternalCallAction_seff_reliability_pc_FailureHandlingEntity, gen_pcm_pc_seff_pc_SetVariableAction_AbstractInternalControlFlowAction, gen_pcm_pc_seff_pc_InternalCallAction_seff_pc_CallAction, gen_pcm_pc_seff_pc_InternalCallAction_seff_pc_AbstractInternalControlFlowAction, gen_pcm_pc_seff_pc_EmitEventAction_seff_pc_AbstractAction, gen_pcm_pc_seff_pc_EmitEventAction_seff_pc_CallAction, gen_pcm_pc_seff_pc_InternalAction_AbstractInternalControlFlowAction, gen_pcm_pc_seff_pc_CollectionIteratorAction_AbstractLoopAction, gen_pcm_pc_seff_pc_GuardedBranchTransition_AbstractBranchTransition, gen_pcm_pc_seff_performance_pc_ResourceCall_CallAction, gen_pcm_pc_seff_performance_pc_InfrastructureCall_CallAction, gen_pcm_pc_seff_reliability_pc_RecoveryActionBehaviour_seff_reliability_pc_FailureHandlingEntity, gen_pcm_pc_seff_reliability_pc_RecoveryActionBehaviour_seff_pc_ResourceDemandingBehaviour, gen_pcm_pc_seff_reliability_pc_FailureHandlingEntity_Entity, gen_pcm_pc_qosannotations_pc_QoSAnnotations_Entity, gen_pcm_pc_seff_reliability_pc_RecoveryAction_AbstractInternalControlFlowAction, gen_pcm_pc_qos_performance_pc_SystemSpecifiedExecutionTime_SpecifiedExecutionTime, gen_pcm_pc_system_pc_System_entity_pc_Entity, gen_pcm_pc_system_pc_System_entity_pc_ComposedProvidingRequiringEntity, gen_pcm_pc_qos_performance_pc_SpecifiedExecutionTime_SpecifiedQoSAnnotation, gen_pcm_pc_qos_performance_pc_ComponentSpecifiedExecutionTime_SpecifiedExecutionTime, gen_pcm_pc_qos_reliability_pc_SpecifiedReliabilityAnnotation_SpecifiedQoSAnnotation, gen_pcm_pc_resourceenvironment_pc_LinkingResource_Entity, gen_pcm_pc_resourceenvironment_pc_ResourceContainer_Entity, gen_pcm_pc_resourceenvironment_pc_ProcessingResourceSpecification_Identifier, gen_pcm_pc_resourceenvironment_pc_ResourceEnvironment_NamedElement, gen_pcm_pc_allocation_pc_AllocationContext_Entity, gen_pcm_pc_allocation_pc_Allocation_Entity, gen_pcm_pc_resourceenvironment_pc_CommunicationLinkResourceSpecification_Identifier, gen_pcm_pc_subsystem_pc_SubSystem_entity_pc_ComposedProvidingRequiringEntity, gen_pcm_pc_subsystem_pc_SubSystem_repository_pc_RepositoryComponent, gen_pcm_pc_completions_pc_Completion_entity_pc_ComposedProvidingRequiringEntity, gen_pcm_pc_completions_pc_Completion_repository_pc_ImplementationComponentType, gen_pcm_pc_completions_pc_DelegatingExternalCallAction_ExternalCallAction, gen_pcm_pc_completions_pc_NetworkDemandParametricResourceDemand_ParametricResourceDemand},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)