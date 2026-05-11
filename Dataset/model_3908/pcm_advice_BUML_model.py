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
GuardedBranchTransition = Class(name="GuardedBranchTransition")
qos_performance_av_SpecifiedExecutionTime = Class(name="qos_performance_av_SpecifiedExecutionTime")
pcm_av_DummyClass = Class(name="pcm_av_DummyClass")
pcm_av_Advice = Class(name="pcm_av_Advice")
pcm_av_EObject = Class(name="pcm_av_EObject")
pcm_av_GlobalScope = Class(name="pcm_av_GlobalScope")
pcm_av_PerJoinPointScope = Class(name="pcm_av_PerJoinPointScope")
pcm_av_core_av_PCMRandomVariable = Class(name="pcm_av_core_av_PCMRandomVariable")
RandomVariable = Class(name="RandomVariable")
ClosedWorkload = Class(name="ClosedWorkload")
PassiveResource = Class(name="PassiveResource")
VariableCharacterisation = Class(name="VariableCharacterisation")
seff_performance_av_InfrastructureCall = Class(name="seff_performance_av_InfrastructureCall")
seff_performance_av_ResourceCall = Class(name="seff_performance_av_ResourceCall")
seff_performance_av_ParametricResourceDemand = Class(name="seff_performance_av_ParametricResourceDemand")
LoopAction = Class(name="LoopAction")
entity_av_ResourceRequiredRole = Class(name="entity_av_ResourceRequiredRole")
pcm_av_entity_av_ResourceRequiredRole = Class(name="pcm_av_entity_av_ResourceRequiredRole")
composition_av_EventChannelSinkConnector = Class(name="composition_av_EventChannelSinkConnector")
composition_av_AssemblyEventConnector = Class(name="composition_av_AssemblyEventConnector")
Loop = Class(name="Loop")
OpenWorkload = Class(name="OpenWorkload")
Delay = Class(name="Delay")
CommunicationLinkResourceSpecification = Class(name="CommunicationLinkResourceSpecification")
ProcessingResourceSpecification = Class(name="ProcessingResourceSpecification")
pcm_av_entity_av_ResourceProvidedRole = Class(name="pcm_av_entity_av_ResourceProvidedRole")
Role = Class(name="Role")
entity_av_ResourceInterfaceProvidingEntity = Class(name="entity_av_ResourceInterfaceProvidingEntity")
ResourceInterface = Class(name="ResourceInterface")
pcm_av_entity_av_InterfaceProvidingRequiringEntity = Class(name="pcm_av_entity_av_InterfaceProvidingRequiringEntity")
entity_av_InterfaceProvidingEntity = Class(name="entity_av_InterfaceProvidingEntity")
entity_av_InterfaceRequiringEntity = Class(name="entity_av_InterfaceRequiringEntity")
pcm_av_entity_av_InterfaceProvidingEntity = Class(name="pcm_av_entity_av_InterfaceProvidingEntity")
Entity = Class(name="Entity")
ProvidedRole = Class(name="ProvidedRole")
pcm_av_entity_av_InterfaceRequiringEntity = Class(name="pcm_av_entity_av_InterfaceRequiringEntity")
entity_av_Entity = Class(name="entity_av_Entity")
entity_av_ResourceInterfaceRequiringEntity = Class(name="entity_av_ResourceInterfaceRequiringEntity")
RequiredRole = Class(name="RequiredRole")
pcm_av_entity_av_ResourceInterfaceRequiringEntity = Class(name="pcm_av_entity_av_ResourceInterfaceRequiringEntity")
pcm_av_entity_av_ResourceInterfaceProvidingEntity = Class(name="pcm_av_entity_av_ResourceInterfaceProvidingEntity")
entity_av_ResourceProvidedRole = Class(name="entity_av_ResourceProvidedRole")
pcm_av_entity_av_ComposedProvidingRequiringEntity = Class(name="pcm_av_entity_av_ComposedProvidingRequiringEntity")
composition_av_ComposedStructure = Class(name="composition_av_ComposedStructure")
entity_av_InterfaceProvidingRequiringEntity = Class(name="entity_av_InterfaceProvidingRequiringEntity")
pcm_av_entity_av_NamedElement = Class(name="pcm_av_entity_av_NamedElement")
pcm_av_entity_av_ResourceInterfaceProvidingRequiringEntity = Class(name="pcm_av_entity_av_ResourceInterfaceProvidingRequiringEntity")
pcm_av_entity_av_Entity = Class(name="pcm_av_entity_av_Entity")
Identifier = Class(name="Identifier")
entity_av_NamedElement = Class(name="entity_av_NamedElement")
pcm_av_composition_av_DelegationConnector = Class(name="pcm_av_composition_av_DelegationConnector")
Connector = Class(name="Connector")
pcm_av_composition_av_Connector = Class(name="pcm_av_composition_av_Connector")
pcm_av_composition_av_ComposedStructure = Class(name="pcm_av_composition_av_ComposedStructure")
pcm_av_composition_av_ProvidedDelegationConnector = Class(name="pcm_av_composition_av_ProvidedDelegationConnector")
DelegationConnector = Class(name="DelegationConnector")
composition_av_AssemblyContext = Class(name="composition_av_AssemblyContext")
composition_av_ResourceRequiredDelegationConnector = Class(name="composition_av_ResourceRequiredDelegationConnector")
composition_av_EventChannel = Class(name="composition_av_EventChannel")
composition_av_Connector = Class(name="composition_av_Connector")
pcm_av_composition_av_ResourceRequiredDelegationConnector = Class(name="pcm_av_composition_av_ResourceRequiredDelegationConnector")
pcm_av_composition_av_EventChannel = Class(name="pcm_av_composition_av_EventChannel")
EventGroup = Class(name="EventGroup")
composition_av_EventChannelSourceConnector = Class(name="composition_av_EventChannelSourceConnector")
pcm_av_composition_av_EventChannelSourceConnector = Class(name="pcm_av_composition_av_EventChannelSourceConnector")
SourceRole = Class(name="SourceRole")
pcm_av_composition_av_EventChannelSinkConnector = Class(name="pcm_av_composition_av_EventChannelSinkConnector")
SinkRole = Class(name="SinkRole")
PCMRandomVariable = Class(name="PCMRandomVariable")
OperationProvidedRole = Class(name="OperationProvidedRole")
pcm_av_composition_av_RequiredDelegationConnector = Class(name="pcm_av_composition_av_RequiredDelegationConnector")
OperationRequiredRole = Class(name="OperationRequiredRole")
pcm_av_composition_av_AssemblyConnector = Class(name="pcm_av_composition_av_AssemblyConnector")
pcm_av_composition_av_SinkDelegationConnector = Class(name="pcm_av_composition_av_SinkDelegationConnector")
pcm_av_composition_av_AssemblyEventConnector = Class(name="pcm_av_composition_av_AssemblyEventConnector")
pcm_av_composition_av_SourceDelegationConnector = Class(name="pcm_av_composition_av_SourceDelegationConnector")
pcm_av_composition_av_AssemblyInfrastructureConnector = Class(name="pcm_av_composition_av_AssemblyInfrastructureConnector")
InfrastructureProvidedRole = Class(name="InfrastructureProvidedRole")
InfrastructureRequiredRole = Class(name="InfrastructureRequiredRole")
pcm_av_composition_av_ProvidedInfrastructureDelegationConnector = Class(name="pcm_av_composition_av_ProvidedInfrastructureDelegationConnector")
pcm_av_composition_av_RequiredInfrastructureDelegationConnector = Class(name="pcm_av_composition_av_RequiredInfrastructureDelegationConnector")
pcm_av_composition_av_RequiredResourceDelegationConnector = Class(name="pcm_av_composition_av_RequiredResourceDelegationConnector")
pcm_av_composition_av_AssemblyContext = Class(name="pcm_av_composition_av_AssemblyContext")
RepositoryComponent = Class(name="RepositoryComponent")
VariableUsage = Class(name="VariableUsage")
OperationSignature = Class(name="OperationSignature")
pcm_av_usagemodel_av_Workload = Class(name="pcm_av_usagemodel_av_Workload")
UsageScenario = Class(name="UsageScenario")
pcm_av_usagemodel_av_UsageScenario = Class(name="pcm_av_usagemodel_av_UsageScenario")
UsageModel = Class(name="UsageModel")
ScenarioBehaviour = Class(name="ScenarioBehaviour")
Workload = Class(name="Workload")
pcm_av_usagemodel_av_UserData = Class(name="pcm_av_usagemodel_av_UserData")
pcm_av_usagemodel_av_UsageModel = Class(name="pcm_av_usagemodel_av_UsageModel")
UserData = Class(name="UserData")
pcm_av_usagemodel_av_EntryLevelSystemCall = Class(name="pcm_av_usagemodel_av_EntryLevelSystemCall")
AbstractUserAction = Class(name="AbstractUserAction")
pcm_av_usagemodel_av_BranchTransition = Class(name="pcm_av_usagemodel_av_BranchTransition")
Branch = Class(name="Branch")
pcm_av_usagemodel_av_AbstractUserAction = Class(name="pcm_av_usagemodel_av_AbstractUserAction")
pcm_av_usagemodel_av_ScenarioBehaviour = Class(name="pcm_av_usagemodel_av_ScenarioBehaviour")
BranchTransition = Class(name="BranchTransition")
pcm_av_usagemodel_av_Branch = Class(name="pcm_av_usagemodel_av_Branch")
pcm_av_usagemodel_av_Loop = Class(name="pcm_av_usagemodel_av_Loop")
pcm_av_usagemodel_av_Stop = Class(name="pcm_av_usagemodel_av_Stop")
pcm_av_usagemodel_av_Start = Class(name="pcm_av_usagemodel_av_Start")
pcm_av_usagemodel_av_OpenWorkload = Class(name="pcm_av_usagemodel_av_OpenWorkload")
pcm_av_usagemodel_av_Delay = Class(name="pcm_av_usagemodel_av_Delay")
pcm_av_usagemodel_av_ClosedWorkload = Class(name="pcm_av_usagemodel_av_ClosedWorkload")
pcm_av_repository_av_PassiveResource = Class(name="pcm_av_repository_av_PassiveResource")
BasicComponent = Class(name="BasicComponent")
ResourceTimeoutFailureType = Class(name="ResourceTimeoutFailureType")
pcm_av_repository_av_BasicComponent = Class(name="pcm_av_repository_av_BasicComponent")
ImplementationComponentType = Class(name="ImplementationComponentType")
ServiceEffectSpecification = Class(name="ServiceEffectSpecification")
pcm_av_repository_av_ImplementationComponentType = Class(name="pcm_av_repository_av_ImplementationComponentType")
InfrastructureSignature = Class(name="InfrastructureSignature")
CompleteComponentType = Class(name="CompleteComponentType")
pcm_av_repository_av_RepositoryComponent = Class(name="pcm_av_repository_av_RepositoryComponent")
InterfaceProvidingRequiringEntity = Class(name="InterfaceProvidingRequiringEntity")
Repository = Class(name="Repository")
pcm_av_repository_av_ProvidedRole = Class(name="pcm_av_repository_av_ProvidedRole")
pcm_av_repository_av_Parameter = Class(name="pcm_av_repository_av_Parameter")
DataType = Class(name="DataType")
EventType = Class(name="EventType")
ResourceSignature = Class(name="ResourceSignature")
pcm_av_repository_av_DataType = Class(name="pcm_av_repository_av_DataType")
pcm_av_repository_av_Repository = Class(name="pcm_av_repository_av_Repository")
Interface = Class(name="Interface")
FailureType = Class(name="FailureType")
pcm_av_repository_av_Interface = Class(name="pcm_av_repository_av_Interface")
pcm_av_repository_av_InfrastructureSignature = Class(name="pcm_av_repository_av_InfrastructureSignature")
InfrastructureInterface = Class(name="InfrastructureInterface")
Protocol = Class(name="Protocol")
RequiredCharacterisation = Class(name="RequiredCharacterisation")
pcm_av_repository_av_RequiredCharacterisation = Class(name="pcm_av_repository_av_RequiredCharacterisation")
Parameter_ = Class(name="Parameter")
pcm_av_repository_av_EventGroup = Class(name="pcm_av_repository_av_EventGroup")
pcm_av_repository_av_EventType = Class(name="pcm_av_repository_av_EventType")
Signature = Class(name="Signature")
pcm_av_repository_av_Signature = Class(name="pcm_av_repository_av_Signature")
ExceptionType = Class(name="ExceptionType")
pcm_av_repository_av_ExceptionType = Class(name="pcm_av_repository_av_ExceptionType")
pcm_av_repository_av_OperationRequiredRole = Class(name="pcm_av_repository_av_OperationRequiredRole")
pcm_av_repository_av_InfrastructureInterface = Class(name="pcm_av_repository_av_InfrastructureInterface")
pcm_av_repository_av_InfrastructureRequiredRole = Class(name="pcm_av_repository_av_InfrastructureRequiredRole")
pcm_av_repository_av_RequiredRole = Class(name="pcm_av_repository_av_RequiredRole")
pcm_av_repository_av_OperationSignature = Class(name="pcm_av_repository_av_OperationSignature")
OperationInterface = Class(name="OperationInterface")
pcm_av_repository_av_OperationInterface = Class(name="pcm_av_repository_av_OperationInterface")
ProvidesComponentType = Class(name="ProvidesComponentType")
pcm_av_repository_av_ProvidesComponentType = Class(name="pcm_av_repository_av_ProvidesComponentType")
pcm_av_repository_av_SourceRole = Class(name="pcm_av_repository_av_SourceRole")
pcm_av_repository_av_SinkRole = Class(name="pcm_av_repository_av_SinkRole")
pcm_av_repository_av_OperationProvidedRole = Class(name="pcm_av_repository_av_OperationProvidedRole")
pcm_av_repository_av_InfrastructureProvidedRole = Class(name="pcm_av_repository_av_InfrastructureProvidedRole")
pcm_av_repository_av_CompleteComponentType = Class(name="pcm_av_repository_av_CompleteComponentType")
pcm_av_repository_av_PrimitiveDataType = Class(name="pcm_av_repository_av_PrimitiveDataType")
pcm_av_repository_av_CompositeComponent = Class(name="pcm_av_repository_av_CompositeComponent")
entity_av_ComposedProvidingRequiringEntity = Class(name="entity_av_ComposedProvidingRequiringEntity")
repository_av_ImplementationComponentType = Class(name="repository_av_ImplementationComponentType")
pcm_av_repository_av_CollectionDataType = Class(name="pcm_av_repository_av_CollectionDataType")
repository_av_DataType = Class(name="repository_av_DataType")
pcm_av_repository_av_CompositeDataType = Class(name="pcm_av_repository_av_CompositeDataType")
CompositeDataType = Class(name="CompositeDataType")
InnerDeclaration = Class(name="InnerDeclaration")
pcm_av_repository_av_InnerDeclaration = Class(name="pcm_av_repository_av_InnerDeclaration")
NamedElement = Class(name="NamedElement")
pcm_av_repository_av_Role = Class(name="pcm_av_repository_av_Role")
pcm_av_resourcetype_av_ResourceSignature = Class(name="pcm_av_resourcetype_av_ResourceSignature")
pcm_av_resourcetype_av_ProcessingResourceType = Class(name="pcm_av_resourcetype_av_ProcessingResourceType")
ResourceType = Class(name="ResourceType")
HardwareInducedFailureType = Class(name="HardwareInducedFailureType")
pcm_av_resourcetype_av_ResourceType = Class(name="pcm_av_resourcetype_av_ResourceType")
UnitCarryingElement = Class(name="UnitCarryingElement")
ResourceRepository = Class(name="ResourceRepository")
pcm_av_resourcetype_av_ResourceRepository = Class(name="pcm_av_resourcetype_av_ResourceRepository")
SchedulingPolicy = Class(name="SchedulingPolicy")
pcm_av_resourcetype_av_SchedulingPolicy = Class(name="pcm_av_resourcetype_av_SchedulingPolicy")
pcm_av_resourcetype_av_CommunicationLinkResourceType = Class(name="pcm_av_resourcetype_av_CommunicationLinkResourceType")
NetworkInducedFailureType = Class(name="NetworkInducedFailureType")
pcm_av_resourcetype_av_ResourceInterface = Class(name="pcm_av_resourcetype_av_ResourceInterface")
EntryLevelSystemCall = Class(name="EntryLevelSystemCall")
pcm_av_protocol_av_Protocol = Class(name="pcm_av_protocol_av_Protocol")
pcm_av_parameter_av_VariableUsage = Class(name="pcm_av_parameter_av_VariableUsage")
CallAction = Class(name="CallAction")
SynchronisationPoint = Class(name="SynchronisationPoint")
CallReturnAction = Class(name="CallReturnAction")
SetVariableAction = Class(name="SetVariableAction")
SpecifiedOutputParameterAbstraction = Class(name="SpecifiedOutputParameterAbstraction")
pcm_av_reliability_av_FailureOccurrenceDescription = Class(name="pcm_av_reliability_av_FailureOccurrenceDescription")
parameter_av_pcm_av_AbstractNamedReference = Class(name="parameter_av_pcm_av_AbstractNamedReference")
pcm_av_parameter_av_VariableCharacterisation = Class(name="pcm_av_parameter_av_VariableCharacterisation")
pcm_av_parameter_av_CharacterisedVariable = Class(name="pcm_av_parameter_av_CharacterisedVariable")
Variable = Class(name="Variable")
pcm_av_reliability_av_HardwareInducedFailureType = Class(name="pcm_av_reliability_av_HardwareInducedFailureType")
ProcessingResourceType = Class(name="ProcessingResourceType")
pcm_av_reliability_av_SoftwareInducedFailureType = Class(name="pcm_av_reliability_av_SoftwareInducedFailureType")
InternalFailureOccurrenceDescription = Class(name="InternalFailureOccurrenceDescription")
pcm_av_reliability_av_InternalFailureOccurrenceDescription = Class(name="pcm_av_reliability_av_InternalFailureOccurrenceDescription")
FailureOccurrenceDescription = Class(name="FailureOccurrenceDescription")
InternalAction = Class(name="InternalAction")
SoftwareInducedFailureType = Class(name="SoftwareInducedFailureType")
pcm_av_reliability_av_NetworkInducedFailureType = Class(name="pcm_av_reliability_av_NetworkInducedFailureType")
pcm_av_seff_av_AbstractAction = Class(name="pcm_av_seff_av_AbstractAction")
CommunicationLinkResourceType = Class(name="CommunicationLinkResourceType")
pcm_av_reliability_av_ExternalFailureOccurrenceDescription = Class(name="pcm_av_reliability_av_ExternalFailureOccurrenceDescription")
qos_reliability_av_SpecifiedReliabilityAnnotation = Class(name="qos_reliability_av_SpecifiedReliabilityAnnotation")
pcm_av_reliability_av_ResourceTimeoutFailureType = Class(name="pcm_av_reliability_av_ResourceTimeoutFailureType")
pcm_av_reliability_av_FailureType = Class(name="pcm_av_reliability_av_FailureType")
pcm_av_seff_av_StopAction = Class(name="pcm_av_seff_av_StopAction")
AbstractInternalControlFlowAction = Class(name="AbstractInternalControlFlowAction")
pcm_av_seff_av_AbstractInternalControlFlowAction = Class(name="pcm_av_seff_av_AbstractInternalControlFlowAction")
AbstractAction = Class(name="AbstractAction")
pcm_av_seff_av_AbstractBranchTransition = Class(name="pcm_av_seff_av_AbstractBranchTransition")
BranchAction = Class(name="BranchAction")
ResourceDemandingBehaviour = Class(name="ResourceDemandingBehaviour")
pcm_av_seff_av_ResourceDemandingBehaviour = Class(name="pcm_av_seff_av_ResourceDemandingBehaviour")
AbstractLoopAction = Class(name="AbstractLoopAction")
AbstractBranchTransition = Class(name="AbstractBranchTransition")
pcm_av_seff_av_AbstractLoopAction = Class(name="pcm_av_seff_av_AbstractLoopAction")
pcm_av_seff_av_ResourceDemandingSEFF = Class(name="pcm_av_seff_av_ResourceDemandingSEFF")
seff_av_ServiceEffectSpecification = Class(name="seff_av_ServiceEffectSpecification")
pcm_av_seff_av_BranchAction = Class(name="pcm_av_seff_av_BranchAction")
pcm_av_seff_av_CallAction = Class(name="pcm_av_seff_av_CallAction")
pcm_av_seff_av_StartAction = Class(name="pcm_av_seff_av_StartAction")
pcm_av_seff_av_ServiceEffectSpecification = Class(name="pcm_av_seff_av_ServiceEffectSpecification")
pcm_av_seff_av_ExternalCallAction = Class(name="pcm_av_seff_av_ExternalCallAction")
seff_av_AbstractAction = Class(name="seff_av_AbstractAction")
seff_av_CallReturnAction = Class(name="seff_av_CallReturnAction")
seff_reliability_av_FailureHandlingEntity = Class(name="seff_reliability_av_FailureHandlingEntity")
seff_av_ResourceDemandingBehaviour = Class(name="seff_av_ResourceDemandingBehaviour")
ResourceDemandingInternalBehaviour = Class(name="ResourceDemandingInternalBehaviour")
pcm_av_seff_av_ResourceDemandingInternalBehaviour = Class(name="pcm_av_seff_av_ResourceDemandingInternalBehaviour")
ResourceDemandingSEFF = Class(name="ResourceDemandingSEFF")
pcm_av_seff_av_ReleaseAction = Class(name="pcm_av_seff_av_ReleaseAction")
pcm_av_seff_av_LoopAction = Class(name="pcm_av_seff_av_LoopAction")
pcm_av_seff_av_ForkAction = Class(name="pcm_av_seff_av_ForkAction")
ForkedBehaviour = Class(name="ForkedBehaviour")
pcm_av_seff_av_ForkedBehaviour = Class(name="pcm_av_seff_av_ForkedBehaviour")
ForkAction = Class(name="ForkAction")
pcm_av_seff_av_SynchronisationPoint = Class(name="pcm_av_seff_av_SynchronisationPoint")
pcm_av_seff_av_CallReturnAction = Class(name="pcm_av_seff_av_CallReturnAction")
pcm_av_seff_av_ProbabilisticBranchTransition = Class(name="pcm_av_seff_av_ProbabilisticBranchTransition")
pcm_av_seff_av_AcquireAction = Class(name="pcm_av_seff_av_AcquireAction")
pcm_av_seff_av_CollectionIteratorAction = Class(name="pcm_av_seff_av_CollectionIteratorAction")
pcm_av_seff_av_GuardedBranchTransition = Class(name="pcm_av_seff_av_GuardedBranchTransition")
pcm_av_seff_av_SetVariableAction = Class(name="pcm_av_seff_av_SetVariableAction")
pcm_av_seff_av_InternalCallAction = Class(name="pcm_av_seff_av_InternalCallAction")
seff_av_CallAction = Class(name="seff_av_CallAction")
seff_av_AbstractInternalControlFlowAction = Class(name="seff_av_AbstractInternalControlFlowAction")
pcm_av_seff_av_EmitEventAction = Class(name="pcm_av_seff_av_EmitEventAction")
pcm_av_seff_av_InternalAction = Class(name="pcm_av_seff_av_InternalAction")
pcm_av_seff_performance_av_ResourceCall = Class(name="pcm_av_seff_performance_av_ResourceCall")
pcm_av_seff_performance_av_InfrastructureCall = Class(name="pcm_av_seff_performance_av_InfrastructureCall")
pcm_av_seff_reliability_av_RecoveryActionBehaviour = Class(name="pcm_av_seff_reliability_av_RecoveryActionBehaviour")
pcm_av_seff_performance_av_ParametricResourceDemand = Class(name="pcm_av_seff_performance_av_ParametricResourceDemand")
pcm_av_seff_reliability_av_FailureHandlingEntity = Class(name="pcm_av_seff_reliability_av_FailureHandlingEntity")
seff_reliability_av_RecoveryActionBehaviour = Class(name="seff_reliability_av_RecoveryActionBehaviour")
seff_reliability_av_RecoveryAction = Class(name="seff_reliability_av_RecoveryAction")
pcm_av_seff_reliability_av_RecoveryAction = Class(name="pcm_av_seff_reliability_av_RecoveryAction")
pcm_av_qos_performance_av_SystemSpecifiedExecutionTime = Class(name="pcm_av_qos_performance_av_SystemSpecifiedExecutionTime")
SpecifiedExecutionTime = Class(name="SpecifiedExecutionTime")
pcm_av_qosannotations_av_SpecifiedQoSAnnotation = Class(name="pcm_av_qosannotations_av_SpecifiedQoSAnnotation")
QoSAnnotations = Class(name="QoSAnnotations")
pcm_av_qosannotations_av_QoSAnnotations = Class(name="pcm_av_qosannotations_av_QoSAnnotations")
System = Class(name="System")
SpecifiedQoSAnnotation = Class(name="SpecifiedQoSAnnotation")
pcm_av_qosannotations_av_SpecifiedOutputParameterAbstraction = Class(name="pcm_av_qosannotations_av_SpecifiedOutputParameterAbstraction")
pcm_av_system_av_System = Class(name="pcm_av_system_av_System")
pcm_av_qos_performance_av_SpecifiedExecutionTime = Class(name="pcm_av_qos_performance_av_SpecifiedExecutionTime")
pcm_av_qos_performance_av_ComponentSpecifiedExecutionTime = Class(name="pcm_av_qos_performance_av_ComponentSpecifiedExecutionTime")
pcm_av_qos_reliability_av_SpecifiedReliabilityAnnotation = Class(name="pcm_av_qos_reliability_av_SpecifiedReliabilityAnnotation")
ExternalFailureOccurrenceDescription = Class(name="ExternalFailureOccurrenceDescription")
pcm_av_resourceenvironment_av_ProcessingResourceSpecification = Class(name="pcm_av_resourceenvironment_av_ProcessingResourceSpecification")
pcm_av_resourceenvironment_av_ResourceEnvironment = Class(name="pcm_av_resourceenvironment_av_ResourceEnvironment")
LinkingResource = Class(name="LinkingResource")
ResourceContainer = Class(name="ResourceContainer")
pcm_av_resourceenvironment_av_LinkingResource = Class(name="pcm_av_resourceenvironment_av_LinkingResource")
ResourceEnvironment = Class(name="ResourceEnvironment")
pcm_av_resourceenvironment_av_ResourceContainer = Class(name="pcm_av_resourceenvironment_av_ResourceContainer")
Allocation = Class(name="Allocation")
pcm_av_allocation_av_Allocation = Class(name="pcm_av_allocation_av_Allocation")
pcm_av_resourceenvironment_av_CommunicationLinkResourceSpecification = Class(name="pcm_av_resourceenvironment_av_CommunicationLinkResourceSpecification")
pcm_av_allocation_av_AllocationContext = Class(name="pcm_av_allocation_av_AllocationContext")
pcm_av_completions_av_Completion = Class(name="pcm_av_completions_av_Completion")
pcm_av_completions_av_CompletionRepository = Class(name="pcm_av_completions_av_CompletionRepository")
Completion = Class(name="Completion")
pcm_av_completions_av_DelegatingExternalCallAction = Class(name="pcm_av_completions_av_DelegatingExternalCallAction")
ExternalCallAction = Class(name="ExternalCallAction")
pcm_av_completions_av_NetworkDemandParametricResourceDemand = Class(name="pcm_av_completions_av_NetworkDemandParametricResourceDemand")
ParametricResourceDemand = Class(name="ParametricResourceDemand")
AllocationContext = Class(name="AllocationContext")
pcm_av_subsystem_av_SubSystem = Class(name="pcm_av_subsystem_av_SubSystem")
repository_av_RepositoryComponent = Class(name="repository_av_RepositoryComponent")

# GuardedBranchTransition class attributes and methods

# qos_performance_av_SpecifiedExecutionTime class attributes and methods

# pcm_av_DummyClass class attributes and methods

# pcm_av_Advice class attributes and methods

# pcm_av_EObject class attributes and methods

# pcm_av_GlobalScope class attributes and methods

# pcm_av_PerJoinPointScope class attributes and methods

# pcm_av_core_av_PCMRandomVariable class attributes and methods
pcm_av_core_av_PCMRandomVariable_m_SpecificationMustNotBeNULL: Method = Method(name="SpecificationMustNotBeNULL", parameters={Parameter(name='pcm_av_diagnostics', type=StringType), Parameter(name='pcm_av_context', type=StringType)}, type=BooleanType)
pcm_av_core_av_PCMRandomVariable.methods={pcm_av_core_av_PCMRandomVariable_m_SpecificationMustNotBeNULL}

# RandomVariable class attributes and methods

# ClosedWorkload class attributes and methods

# PassiveResource class attributes and methods

# VariableCharacterisation class attributes and methods

# seff_performance_av_InfrastructureCall class attributes and methods

# seff_performance_av_ResourceCall class attributes and methods

# seff_performance_av_ParametricResourceDemand class attributes and methods

# LoopAction class attributes and methods

# entity_av_ResourceRequiredRole class attributes and methods

# pcm_av_entity_av_ResourceRequiredRole class attributes and methods

# composition_av_EventChannelSinkConnector class attributes and methods

# composition_av_AssemblyEventConnector class attributes and methods

# Loop class attributes and methods

# OpenWorkload class attributes and methods

# Delay class attributes and methods

# CommunicationLinkResourceSpecification class attributes and methods

# ProcessingResourceSpecification class attributes and methods

# pcm_av_entity_av_ResourceProvidedRole class attributes and methods

# Role class attributes and methods

# entity_av_ResourceInterfaceProvidingEntity class attributes and methods

# ResourceInterface class attributes and methods

# pcm_av_entity_av_InterfaceProvidingRequiringEntity class attributes and methods

# entity_av_InterfaceProvidingEntity class attributes and methods

# entity_av_InterfaceRequiringEntity class attributes and methods

# pcm_av_entity_av_InterfaceProvidingEntity class attributes and methods

# Entity class attributes and methods

# ProvidedRole class attributes and methods

# pcm_av_entity_av_InterfaceRequiringEntity class attributes and methods

# entity_av_Entity class attributes and methods

# entity_av_ResourceInterfaceRequiringEntity class attributes and methods

# RequiredRole class attributes and methods

# pcm_av_entity_av_ResourceInterfaceRequiringEntity class attributes and methods

# pcm_av_entity_av_ResourceInterfaceProvidingEntity class attributes and methods

# entity_av_ResourceProvidedRole class attributes and methods

# pcm_av_entity_av_ComposedProvidingRequiringEntity class attributes and methods
pcm_av_entity_av_ComposedProvidingRequiringEntity_m_ProvidedRolesMustBeBound: Method = Method(name="ProvidedRolesMustBeBound", parameters={Parameter(name='pcm_av_diagnostics', type=StringType), Parameter(name='pcm_av_context', type=StringType)}, type=BooleanType)
pcm_av_entity_av_ComposedProvidingRequiringEntity.methods={pcm_av_entity_av_ComposedProvidingRequiringEntity_m_ProvidedRolesMustBeBound}

# composition_av_ComposedStructure class attributes and methods

# entity_av_InterfaceProvidingRequiringEntity class attributes and methods

# pcm_av_entity_av_NamedElement class attributes and methods
pcm_av_entity_av_NamedElement_entityName: Property = Property(name="entityName", type=StringType)
pcm_av_entity_av_NamedElement.attributes={pcm_av_entity_av_NamedElement_entityName}

# pcm_av_entity_av_ResourceInterfaceProvidingRequiringEntity class attributes and methods

# pcm_av_entity_av_Entity class attributes and methods

# Identifier class attributes and methods

# entity_av_NamedElement class attributes and methods

# pcm_av_composition_av_DelegationConnector class attributes and methods

# Connector class attributes and methods

# pcm_av_composition_av_Connector class attributes and methods

# pcm_av_composition_av_ComposedStructure class attributes and methods
pcm_av_composition_av_ComposedStructure_m_MultipleConnectorsConstraintForAssemblyConnectors: Method = Method(name="MultipleConnectorsConstraintForAssemblyConnectors", parameters={Parameter(name='pcm_av_diagnostics', type=StringType), Parameter(name='pcm_av_context', type=StringType)}, type=BooleanType)
pcm_av_composition_av_ComposedStructure_m_MultipleConnectorsConstraint: Method = Method(name="MultipleConnectorsConstraint", parameters={Parameter(name='pcm_av_diagnostics', type=StringType), Parameter(name='pcm_av_context', type=StringType)}, type=BooleanType)
pcm_av_composition_av_ComposedStructure.methods={pcm_av_composition_av_ComposedStructure_m_MultipleConnectorsConstraint, pcm_av_composition_av_ComposedStructure_m_MultipleConnectorsConstraintForAssemblyConnectors}

# pcm_av_composition_av_ProvidedDelegationConnector class attributes and methods
pcm_av_composition_av_ProvidedDelegationConnector_m_ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure: Method = Method(name="ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure", parameters={Parameter(name='pcm_av_context', type=StringType), Parameter(name='pcm_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_composition_av_ProvidedDelegationConnector_m_ComponentOfAssemblyContextAndInnerRoleProvidingComponentNeedToBeTheSame: Method = Method(name="ComponentOfAssemblyContextAndInnerRoleProvidingComponentNeedToBeTheSame", parameters={Parameter(name='pcm_av_context', type=StringType), Parameter(name='pcm_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_composition_av_ProvidedDelegationConnector.methods={pcm_av_composition_av_ProvidedDelegationConnector_m_ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure, pcm_av_composition_av_ProvidedDelegationConnector_m_ComponentOfAssemblyContextAndInnerRoleProvidingComponentNeedToBeTheSame}

# DelegationConnector class attributes and methods

# composition_av_AssemblyContext class attributes and methods

# composition_av_ResourceRequiredDelegationConnector class attributes and methods

# composition_av_EventChannel class attributes and methods

# composition_av_Connector class attributes and methods

# pcm_av_composition_av_ResourceRequiredDelegationConnector class attributes and methods

# pcm_av_composition_av_EventChannel class attributes and methods

# EventGroup class attributes and methods

# composition_av_EventChannelSourceConnector class attributes and methods

# pcm_av_composition_av_EventChannelSourceConnector class attributes and methods

# SourceRole class attributes and methods

# pcm_av_composition_av_EventChannelSinkConnector class attributes and methods

# SinkRole class attributes and methods

# PCMRandomVariable class attributes and methods

# OperationProvidedRole class attributes and methods

# pcm_av_composition_av_RequiredDelegationConnector class attributes and methods
pcm_av_composition_av_RequiredDelegationConnector_m_RequiredDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure: Method = Method(name="RequiredDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure", parameters={Parameter(name='pcm_av_diagnostics', type=StringType), Parameter(name='pcm_av_context', type=StringType)}, type=BooleanType)
pcm_av_composition_av_RequiredDelegationConnector_m_ComponentOfAssemblyContextAndInnerRoleRequiringComponentNeedToBeTheSame: Method = Method(name="ComponentOfAssemblyContextAndInnerRoleRequiringComponentNeedToBeTheSame", parameters={Parameter(name='pcm_av_diagnostics', type=StringType), Parameter(name='pcm_av_context', type=StringType)}, type=BooleanType)
pcm_av_composition_av_RequiredDelegationConnector_m_RequiringEntityOfOuterRequiredRoleMustBeTheSameAsTheParentOfTheRequiredDelegationConnector: Method = Method(name="RequiringEntityOfOuterRequiredRoleMustBeTheSameAsTheParentOfTheRequiredDelegationConnector", parameters={Parameter(name='pcm_av_context', type=StringType), Parameter(name='pcm_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_composition_av_RequiredDelegationConnector.methods={pcm_av_composition_av_RequiredDelegationConnector_m_ComponentOfAssemblyContextAndInnerRoleRequiringComponentNeedToBeTheSame, pcm_av_composition_av_RequiredDelegationConnector_m_RequiredDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure, pcm_av_composition_av_RequiredDelegationConnector_m_RequiringEntityOfOuterRequiredRoleMustBeTheSameAsTheParentOfTheRequiredDelegationConnector}

# OperationRequiredRole class attributes and methods

# pcm_av_composition_av_AssemblyConnector class attributes and methods
pcm_av_composition_av_AssemblyConnector_m_AssemblyConnectorsReferencedProvidedRolesAndChildContextMustMatch: Method = Method(name="AssemblyConnectorsReferencedProvidedRolesAndChildContextMustMatch", parameters={Parameter(name='pcm_av_context', type=StringType), Parameter(name='pcm_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_composition_av_AssemblyConnector_m_AssemblyConnectorsReferencedRequiredRoleAndChildContextMustMatch: Method = Method(name="AssemblyConnectorsReferencedRequiredRoleAndChildContextMustMatch", parameters={Parameter(name='pcm_av_diagnostics', type=StringType), Parameter(name='pcm_av_context', type=StringType)}, type=BooleanType)
pcm_av_composition_av_AssemblyConnector_m_AssemblyConnectorsReferencedInterfacesMustMatch: Method = Method(name="AssemblyConnectorsReferencedInterfacesMustMatch", parameters={Parameter(name='pcm_av_diagnostics', type=StringType), Parameter(name='pcm_av_context', type=StringType)}, type=BooleanType)
pcm_av_composition_av_AssemblyConnector.methods={pcm_av_composition_av_AssemblyConnector_m_AssemblyConnectorsReferencedInterfacesMustMatch, pcm_av_composition_av_AssemblyConnector_m_AssemblyConnectorsReferencedProvidedRolesAndChildContextMustMatch, pcm_av_composition_av_AssemblyConnector_m_AssemblyConnectorsReferencedRequiredRoleAndChildContextMustMatch}

# pcm_av_composition_av_SinkDelegationConnector class attributes and methods

# pcm_av_composition_av_AssemblyEventConnector class attributes and methods

# pcm_av_composition_av_SourceDelegationConnector class attributes and methods

# pcm_av_composition_av_AssemblyInfrastructureConnector class attributes and methods

# InfrastructureProvidedRole class attributes and methods

# InfrastructureRequiredRole class attributes and methods

# pcm_av_composition_av_ProvidedInfrastructureDelegationConnector class attributes and methods

# pcm_av_composition_av_RequiredInfrastructureDelegationConnector class attributes and methods

# pcm_av_composition_av_RequiredResourceDelegationConnector class attributes and methods

# pcm_av_composition_av_AssemblyContext class attributes and methods

# RepositoryComponent class attributes and methods

# VariableUsage class attributes and methods

# OperationSignature class attributes and methods

# pcm_av_usagemodel_av_Workload class attributes and methods

# UsageScenario class attributes and methods

# pcm_av_usagemodel_av_UsageScenario class attributes and methods

# UsageModel class attributes and methods

# ScenarioBehaviour class attributes and methods

# Workload class attributes and methods

# pcm_av_usagemodel_av_UserData class attributes and methods

# pcm_av_usagemodel_av_UsageModel class attributes and methods

# UserData class attributes and methods

# pcm_av_usagemodel_av_EntryLevelSystemCall class attributes and methods
pcm_av_usagemodel_av_EntryLevelSystemCall_priority: Property = Property(name="priority", type=IntegerType)
pcm_av_usagemodel_av_EntryLevelSystemCall_m_EntryLevelSystemCallMustReferenceProvidedRoleOfASystem: Method = Method(name="EntryLevelSystemCallMustReferenceProvidedRoleOfASystem", parameters={Parameter(name='pcm_av_diagnostics', type=StringType), Parameter(name='pcm_av_context', type=StringType)}, type=BooleanType)
pcm_av_usagemodel_av_EntryLevelSystemCall_m_EntryLevelSystemCallSignatureMustMatchItsProvidedRole: Method = Method(name="EntryLevelSystemCallSignatureMustMatchItsProvidedRole", parameters={Parameter(name='pcm_av_diagnostics', type=StringType), Parameter(name='pcm_av_context', type=StringType)}, type=BooleanType)
pcm_av_usagemodel_av_EntryLevelSystemCall.attributes={pcm_av_usagemodel_av_EntryLevelSystemCall_priority}
pcm_av_usagemodel_av_EntryLevelSystemCall.methods={pcm_av_usagemodel_av_EntryLevelSystemCall_m_EntryLevelSystemCallSignatureMustMatchItsProvidedRole, pcm_av_usagemodel_av_EntryLevelSystemCall_m_EntryLevelSystemCallMustReferenceProvidedRoleOfASystem}

# AbstractUserAction class attributes and methods

# pcm_av_usagemodel_av_BranchTransition class attributes and methods
pcm_av_usagemodel_av_BranchTransition_branchProbability: Property = Property(name="branchProbability", type=FloatType)
pcm_av_usagemodel_av_BranchTransition.attributes={pcm_av_usagemodel_av_BranchTransition_branchProbability}

# Branch class attributes and methods

# pcm_av_usagemodel_av_AbstractUserAction class attributes and methods

# pcm_av_usagemodel_av_ScenarioBehaviour class attributes and methods
pcm_av_usagemodel_av_ScenarioBehaviour_m_Exactlyonestart: Method = Method(name="Exactlyonestart", parameters={Parameter(name='pcm_av_context', type=StringType), Parameter(name='pcm_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_usagemodel_av_ScenarioBehaviour_m_Exactlyonestop: Method = Method(name="Exactlyonestop", parameters={Parameter(name='pcm_av_diagnostics', type=StringType), Parameter(name='pcm_av_context', type=StringType)}, type=BooleanType)
pcm_av_usagemodel_av_ScenarioBehaviour_m_EachuseractionexceptStartandStopmusthaveapredecessorandsuccessor: Method = Method(name="EachuseractionexceptStartandStopmusthaveapredecessorandsuccessor", parameters={Parameter(name='pcm_av_context', type=StringType), Parameter(name='pcm_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_usagemodel_av_ScenarioBehaviour.methods={pcm_av_usagemodel_av_ScenarioBehaviour_m_EachuseractionexceptStartandStopmusthaveapredecessorandsuccessor, pcm_av_usagemodel_av_ScenarioBehaviour_m_Exactlyonestart, pcm_av_usagemodel_av_ScenarioBehaviour_m_Exactlyonestop}

# BranchTransition class attributes and methods

# pcm_av_usagemodel_av_Branch class attributes and methods
pcm_av_usagemodel_av_Branch_m_AllBranchProbabilitiesMustSumUpTo1: Method = Method(name="AllBranchProbabilitiesMustSumUpTo1", parameters={Parameter(name='pcm_av_diagnostics', type=StringType), Parameter(name='pcm_av_context', type=StringType)}, type=BooleanType)
pcm_av_usagemodel_av_Branch.methods={pcm_av_usagemodel_av_Branch_m_AllBranchProbabilitiesMustSumUpTo1}

# pcm_av_usagemodel_av_Loop class attributes and methods

# pcm_av_usagemodel_av_Stop class attributes and methods
pcm_av_usagemodel_av_Stop_m_StopHasNoSuccessor: Method = Method(name="StopHasNoSuccessor", parameters={Parameter(name='pcm_av_context', type=StringType), Parameter(name='pcm_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_usagemodel_av_Stop.methods={pcm_av_usagemodel_av_Stop_m_StopHasNoSuccessor}

# pcm_av_usagemodel_av_Start class attributes and methods
pcm_av_usagemodel_av_Start_m_StartHasNoPredecessor: Method = Method(name="StartHasNoPredecessor", parameters={Parameter(name='pcm_av_context', type=StringType), Parameter(name='pcm_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_usagemodel_av_Start.methods={pcm_av_usagemodel_av_Start_m_StartHasNoPredecessor}

# pcm_av_usagemodel_av_OpenWorkload class attributes and methods
pcm_av_usagemodel_av_OpenWorkload_m_InterArrivalTimeInOpenWorkloadNeedsToBeSpecified: Method = Method(name="InterArrivalTimeInOpenWorkloadNeedsToBeSpecified", parameters={Parameter(name='pcm_av_context', type=StringType), Parameter(name='pcm_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_usagemodel_av_OpenWorkload.methods={pcm_av_usagemodel_av_OpenWorkload_m_InterArrivalTimeInOpenWorkloadNeedsToBeSpecified}

# pcm_av_usagemodel_av_Delay class attributes and methods

# pcm_av_usagemodel_av_ClosedWorkload class attributes and methods
pcm_av_usagemodel_av_ClosedWorkload_population: Property = Property(name="population", type=IntegerType)
pcm_av_usagemodel_av_ClosedWorkload_m_PopulationInClosedWorkloadNeedsToBeSpecified: Method = Method(name="PopulationInClosedWorkloadNeedsToBeSpecified", parameters={Parameter(name='pcm_av_context', type=StringType), Parameter(name='pcm_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_usagemodel_av_ClosedWorkload_m_ThinkTimeInClosedWorkloadNeedsToBeSpecified: Method = Method(name="ThinkTimeInClosedWorkloadNeedsToBeSpecified", parameters={Parameter(name='pcm_av_context', type=StringType), Parameter(name='pcm_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_usagemodel_av_ClosedWorkload.attributes={pcm_av_usagemodel_av_ClosedWorkload_population}
pcm_av_usagemodel_av_ClosedWorkload.methods={pcm_av_usagemodel_av_ClosedWorkload_m_ThinkTimeInClosedWorkloadNeedsToBeSpecified, pcm_av_usagemodel_av_ClosedWorkload_m_PopulationInClosedWorkloadNeedsToBeSpecified}

# pcm_av_repository_av_PassiveResource class attributes and methods

# BasicComponent class attributes and methods

# ResourceTimeoutFailureType class attributes and methods

# pcm_av_repository_av_BasicComponent class attributes and methods
pcm_av_repository_av_BasicComponent_m_NoSeffTypeUsedTwice: Method = Method(name="NoSeffTypeUsedTwice", parameters={Parameter(name='pcm_av_diagnostics', type=StringType), Parameter(name='pcm_av_context', type=StringType)}, type=BooleanType)
pcm_av_repository_av_BasicComponent_m_ProvideSameInterfacesAsImplementationType: Method = Method(name="ProvideSameInterfacesAsImplementationType", parameters={Parameter(name='pcm_av_context', type=StringType), Parameter(name='pcm_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_repository_av_BasicComponent_m_RequireSameInterfacesAsImplementationType: Method = Method(name="RequireSameInterfacesAsImplementationType", parameters={Parameter(name='pcm_av_diagnostics', type=StringType), Parameter(name='pcm_av_context', type=StringType)}, type=BooleanType)
pcm_av_repository_av_BasicComponent.methods={pcm_av_repository_av_BasicComponent_m_ProvideSameInterfacesAsImplementationType, pcm_av_repository_av_BasicComponent_m_RequireSameInterfacesAsImplementationType, pcm_av_repository_av_BasicComponent_m_NoSeffTypeUsedTwice}

# ImplementationComponentType class attributes and methods

# ServiceEffectSpecification class attributes and methods

# pcm_av_repository_av_ImplementationComponentType class attributes and methods
pcm_av_repository_av_ImplementationComponentType_componentType: Property = Property(name="componentType", type=StringType)
pcm_av_repository_av_ImplementationComponentType_m_RequiredInterfacesHaveToConformToCompleteType: Method = Method(name="RequiredInterfacesHaveToConformToCompleteType", parameters={Parameter(name='pcm_av_context', type=StringType), Parameter(name='pcm_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_repository_av_ImplementationComponentType_m_providedInterfacesHaveToConformToCompleteType: Method = Method(name="providedInterfacesHaveToConformToCompleteType", parameters={Parameter(name='pcm_av_context', type=StringType), Parameter(name='pcm_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_repository_av_ImplementationComponentType_m_ProvidedInterfaceHaveToConformToComponentType: Method = Method(name="ProvidedInterfaceHaveToConformToComponentType", parameters={Parameter(name='pcm_av_diagnostics', type=StringType), Parameter(name='pcm_av_context', type=StringType)}, type=BooleanType)
pcm_av_repository_av_ImplementationComponentType.attributes={pcm_av_repository_av_ImplementationComponentType_componentType}
pcm_av_repository_av_ImplementationComponentType.methods={pcm_av_repository_av_ImplementationComponentType_m_RequiredInterfacesHaveToConformToCompleteType, pcm_av_repository_av_ImplementationComponentType_m_providedInterfacesHaveToConformToCompleteType, pcm_av_repository_av_ImplementationComponentType_m_ProvidedInterfaceHaveToConformToComponentType}

# InfrastructureSignature class attributes and methods

# CompleteComponentType class attributes and methods

# pcm_av_repository_av_RepositoryComponent class attributes and methods

# InterfaceProvidingRequiringEntity class attributes and methods

# Repository class attributes and methods

# pcm_av_repository_av_ProvidedRole class attributes and methods

# pcm_av_repository_av_Parameter class attributes and methods
pcm_av_repository_av_Parameter_parameterName: Property = Property(name="parameterName", type=StringType)
pcm_av_repository_av_Parameter_modifier__Parameter: Property = Property(name="modifier__Parameter", type=StringType)
pcm_av_repository_av_Parameter.attributes={pcm_av_repository_av_Parameter_modifier__Parameter, pcm_av_repository_av_Parameter_parameterName}

# DataType class attributes and methods

# EventType class attributes and methods

# ResourceSignature class attributes and methods

# pcm_av_repository_av_DataType class attributes and methods

# pcm_av_repository_av_Repository class attributes and methods
pcm_av_repository_av_Repository_repositoryDescription: Property = Property(name="repositoryDescription", type=StringType)
pcm_av_repository_av_Repository.attributes={pcm_av_repository_av_Repository_repositoryDescription}

# Interface class attributes and methods

# FailureType class attributes and methods

# pcm_av_repository_av_Interface class attributes and methods
pcm_av_repository_av_Interface_m_NoProtocolTypeIDUsedTwice: Method = Method(name="NoProtocolTypeIDUsedTwice", parameters={Parameter(name='pcm_av_diagnostics', type=StringType), Parameter(name='pcm_av_context', type=StringType)}, type=BooleanType)
pcm_av_repository_av_Interface.methods={pcm_av_repository_av_Interface_m_NoProtocolTypeIDUsedTwice}

# pcm_av_repository_av_InfrastructureSignature class attributes and methods

# InfrastructureInterface class attributes and methods

# Protocol class attributes and methods

# RequiredCharacterisation class attributes and methods

# pcm_av_repository_av_RequiredCharacterisation class attributes and methods
pcm_av_repository_av_RequiredCharacterisation_type: Property = Property(name="type", type=StringType)
pcm_av_repository_av_RequiredCharacterisation.attributes={pcm_av_repository_av_RequiredCharacterisation_type}

# Parameter class attributes and methods

# pcm_av_repository_av_EventGroup class attributes and methods

# pcm_av_repository_av_EventType class attributes and methods

# Signature class attributes and methods

# pcm_av_repository_av_Signature class attributes and methods

# ExceptionType class attributes and methods

# pcm_av_repository_av_ExceptionType class attributes and methods
pcm_av_repository_av_ExceptionType_exceptionName: Property = Property(name="exceptionName", type=StringType)
pcm_av_repository_av_ExceptionType_exceptionMessage: Property = Property(name="exceptionMessage", type=StringType)
pcm_av_repository_av_ExceptionType.attributes={pcm_av_repository_av_ExceptionType_exceptionName, pcm_av_repository_av_ExceptionType_exceptionMessage}

# pcm_av_repository_av_OperationRequiredRole class attributes and methods

# pcm_av_repository_av_InfrastructureInterface class attributes and methods

# pcm_av_repository_av_InfrastructureRequiredRole class attributes and methods

# pcm_av_repository_av_RequiredRole class attributes and methods

# pcm_av_repository_av_OperationSignature class attributes and methods
pcm_av_repository_av_OperationSignature_m_ParameterNamesHaveToBeUniqueForASignature: Method = Method(name="ParameterNamesHaveToBeUniqueForASignature", parameters={Parameter(name='pcm_av_context', type=StringType), Parameter(name='pcm_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_repository_av_OperationSignature.methods={pcm_av_repository_av_OperationSignature_m_ParameterNamesHaveToBeUniqueForASignature}

# OperationInterface class attributes and methods

# pcm_av_repository_av_OperationInterface class attributes and methods
pcm_av_repository_av_OperationInterface_m_SignaturesHaveToBeUniqueForAnInterface: Method = Method(name="SignaturesHaveToBeUniqueForAnInterface", parameters={Parameter(name='pcm_av_diagnostics', type=StringType), Parameter(name='pcm_av_context', type=StringType)}, type=BooleanType)
pcm_av_repository_av_OperationInterface.methods={pcm_av_repository_av_OperationInterface_m_SignaturesHaveToBeUniqueForAnInterface}

# ProvidesComponentType class attributes and methods

# pcm_av_repository_av_ProvidesComponentType class attributes and methods
pcm_av_repository_av_ProvidesComponentType_m_AtLeastOneInterfaceHasToBeProvidedByAUsefullProvidesComponentType: Method = Method(name="AtLeastOneInterfaceHasToBeProvidedByAUsefullProvidesComponentType", parameters={Parameter(name='pcm_av_context', type=StringType), Parameter(name='pcm_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_repository_av_ProvidesComponentType.methods={pcm_av_repository_av_ProvidesComponentType_m_AtLeastOneInterfaceHasToBeProvidedByAUsefullProvidesComponentType}

# pcm_av_repository_av_SourceRole class attributes and methods

# pcm_av_repository_av_SinkRole class attributes and methods

# pcm_av_repository_av_OperationProvidedRole class attributes and methods

# pcm_av_repository_av_InfrastructureProvidedRole class attributes and methods

# pcm_av_repository_av_CompleteComponentType class attributes and methods
pcm_av_repository_av_CompleteComponentType_m_AtLeastOneInterfaceHasToBeProvidedOrRequiredByAUsefullCompleteComponentType: Method = Method(name="AtLeastOneInterfaceHasToBeProvidedOrRequiredByAUsefullCompleteComponentType", parameters={Parameter(name='pcm_av_context', type=StringType), Parameter(name='pcm_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_repository_av_CompleteComponentType_m_providedInterfacesHaveToConformToProvidedType2: Method = Method(name="providedInterfacesHaveToConformToProvidedType2", parameters={Parameter(name='pcm_av_diagnostics', type=StringType), Parameter(name='pcm_av_context', type=StringType)}, type=BooleanType)
pcm_av_repository_av_CompleteComponentType.methods={pcm_av_repository_av_CompleteComponentType_m_AtLeastOneInterfaceHasToBeProvidedOrRequiredByAUsefullCompleteComponentType, pcm_av_repository_av_CompleteComponentType_m_providedInterfacesHaveToConformToProvidedType2}

# pcm_av_repository_av_PrimitiveDataType class attributes and methods
pcm_av_repository_av_PrimitiveDataType_type: Property = Property(name="type", type=StringType)
pcm_av_repository_av_PrimitiveDataType.attributes={pcm_av_repository_av_PrimitiveDataType_type}

# pcm_av_repository_av_CompositeComponent class attributes and methods
pcm_av_repository_av_CompositeComponent_m_ProvideSameInterfaces: Method = Method(name="ProvideSameInterfaces", parameters={Parameter(name='pcm_av_context', type=StringType), Parameter(name='pcm_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_repository_av_CompositeComponent_m_RequireSameInterfaces: Method = Method(name="RequireSameInterfaces", parameters={Parameter(name='pcm_av_context', type=StringType), Parameter(name='pcm_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_repository_av_CompositeComponent.methods={pcm_av_repository_av_CompositeComponent_m_RequireSameInterfaces, pcm_av_repository_av_CompositeComponent_m_ProvideSameInterfaces}

# entity_av_ComposedProvidingRequiringEntity class attributes and methods

# repository_av_ImplementationComponentType class attributes and methods

# pcm_av_repository_av_CollectionDataType class attributes and methods

# repository_av_DataType class attributes and methods

# pcm_av_repository_av_CompositeDataType class attributes and methods

# CompositeDataType class attributes and methods

# InnerDeclaration class attributes and methods

# pcm_av_repository_av_InnerDeclaration class attributes and methods

# NamedElement class attributes and methods

# pcm_av_repository_av_Role class attributes and methods

# pcm_av_resourcetype_av_ResourceSignature class attributes and methods
pcm_av_resourcetype_av_ResourceSignature_resourceServiceId: Property = Property(name="resourceServiceId", type=IntegerType)
pcm_av_resourcetype_av_ResourceSignature.attributes={pcm_av_resourcetype_av_ResourceSignature_resourceServiceId}

# pcm_av_resourcetype_av_ProcessingResourceType class attributes and methods

# ResourceType class attributes and methods

# HardwareInducedFailureType class attributes and methods

# pcm_av_resourcetype_av_ResourceType class attributes and methods

# UnitCarryingElement class attributes and methods

# ResourceRepository class attributes and methods

# pcm_av_resourcetype_av_ResourceRepository class attributes and methods

# SchedulingPolicy class attributes and methods

# pcm_av_resourcetype_av_SchedulingPolicy class attributes and methods

# pcm_av_resourcetype_av_CommunicationLinkResourceType class attributes and methods

# NetworkInducedFailureType class attributes and methods

# pcm_av_resourcetype_av_ResourceInterface class attributes and methods

# EntryLevelSystemCall class attributes and methods

# pcm_av_protocol_av_Protocol class attributes and methods
pcm_av_protocol_av_Protocol_protocolTypeID: Property = Property(name="protocolTypeID", type=StringType)
pcm_av_protocol_av_Protocol.attributes={pcm_av_protocol_av_Protocol_protocolTypeID}

# pcm_av_parameter_av_VariableUsage class attributes and methods

# CallAction class attributes and methods

# SynchronisationPoint class attributes and methods

# CallReturnAction class attributes and methods

# SetVariableAction class attributes and methods

# SpecifiedOutputParameterAbstraction class attributes and methods

# pcm_av_reliability_av_FailureOccurrenceDescription class attributes and methods
pcm_av_reliability_av_FailureOccurrenceDescription_failureProbability: Property = Property(name="failureProbability", type=FloatType)
pcm_av_reliability_av_FailureOccurrenceDescription_m_EnsureValidFailureProbabilityRange: Method = Method(name="EnsureValidFailureProbabilityRange", parameters={Parameter(name='pcm_av_context', type=StringType), Parameter(name='pcm_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_reliability_av_FailureOccurrenceDescription.attributes={pcm_av_reliability_av_FailureOccurrenceDescription_failureProbability}
pcm_av_reliability_av_FailureOccurrenceDescription.methods={pcm_av_reliability_av_FailureOccurrenceDescription_m_EnsureValidFailureProbabilityRange}

# parameter_av_pcm_av_AbstractNamedReference class attributes and methods

# pcm_av_parameter_av_VariableCharacterisation class attributes and methods
pcm_av_parameter_av_VariableCharacterisation_type: Property = Property(name="type", type=StringType)
pcm_av_parameter_av_VariableCharacterisation.attributes={pcm_av_parameter_av_VariableCharacterisation_type}

# pcm_av_parameter_av_CharacterisedVariable class attributes and methods
pcm_av_parameter_av_CharacterisedVariable_characterisationType: Property = Property(name="characterisationType", type=StringType)
pcm_av_parameter_av_CharacterisedVariable.attributes={pcm_av_parameter_av_CharacterisedVariable_characterisationType}

# Variable class attributes and methods

# pcm_av_reliability_av_HardwareInducedFailureType class attributes and methods
pcm_av_reliability_av_HardwareInducedFailureType_m_HardwareInducedFailureTypeHasProcessingResourceType: Method = Method(name="HardwareInducedFailureTypeHasProcessingResourceType", parameters={Parameter(name='pcm_av_diagnostics', type=StringType), Parameter(name='pcm_av_context', type=StringType)}, type=BooleanType)
pcm_av_reliability_av_HardwareInducedFailureType.methods={pcm_av_reliability_av_HardwareInducedFailureType_m_HardwareInducedFailureTypeHasProcessingResourceType}

# ProcessingResourceType class attributes and methods

# pcm_av_reliability_av_SoftwareInducedFailureType class attributes and methods

# InternalFailureOccurrenceDescription class attributes and methods

# pcm_av_reliability_av_InternalFailureOccurrenceDescription class attributes and methods
pcm_av_reliability_av_InternalFailureOccurrenceDescription_m_NoResourceTimeoutFailureAllowedForInternalFailureOccurrenceDescription: Method = Method(name="NoResourceTimeoutFailureAllowedForInternalFailureOccurrenceDescription", parameters={Parameter(name='pcm_av_context', type=StringType), Parameter(name='pcm_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_reliability_av_InternalFailureOccurrenceDescription.methods={pcm_av_reliability_av_InternalFailureOccurrenceDescription_m_NoResourceTimeoutFailureAllowedForInternalFailureOccurrenceDescription}

# FailureOccurrenceDescription class attributes and methods

# InternalAction class attributes and methods

# SoftwareInducedFailureType class attributes and methods

# pcm_av_reliability_av_NetworkInducedFailureType class attributes and methods
pcm_av_reliability_av_NetworkInducedFailureType_m_NetworkInducedFailureTypeHasCommunicationLinkResourceType: Method = Method(name="NetworkInducedFailureTypeHasCommunicationLinkResourceType", parameters={Parameter(name='pcm_av_diagnostics', type=StringType), Parameter(name='pcm_av_context', type=StringType)}, type=BooleanType)
pcm_av_reliability_av_NetworkInducedFailureType.methods={pcm_av_reliability_av_NetworkInducedFailureType_m_NetworkInducedFailureTypeHasCommunicationLinkResourceType}

# pcm_av_seff_av_AbstractAction class attributes and methods

# CommunicationLinkResourceType class attributes and methods

# pcm_av_reliability_av_ExternalFailureOccurrenceDescription class attributes and methods
pcm_av_reliability_av_ExternalFailureOccurrenceDescription_m_NoResourceTimeoutFailureAllowedForExternalFailureOccurrenceDescription: Method = Method(name="NoResourceTimeoutFailureAllowedForExternalFailureOccurrenceDescription", parameters={Parameter(name='pcm_av_context', type=StringType), Parameter(name='pcm_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_reliability_av_ExternalFailureOccurrenceDescription.methods={pcm_av_reliability_av_ExternalFailureOccurrenceDescription_m_NoResourceTimeoutFailureAllowedForExternalFailureOccurrenceDescription}

# qos_reliability_av_SpecifiedReliabilityAnnotation class attributes and methods

# pcm_av_reliability_av_ResourceTimeoutFailureType class attributes and methods

# pcm_av_reliability_av_FailureType class attributes and methods

# pcm_av_seff_av_StopAction class attributes and methods
pcm_av_seff_av_StopAction_m_StopActionSuccessorMustNotBeDefined: Method = Method(name="StopActionSuccessorMustNotBeDefined", parameters={Parameter(name='pcm_av_context', type=StringType), Parameter(name='pcm_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_seff_av_StopAction.methods={pcm_av_seff_av_StopAction_m_StopActionSuccessorMustNotBeDefined}

# AbstractInternalControlFlowAction class attributes and methods

# pcm_av_seff_av_AbstractInternalControlFlowAction class attributes and methods

# AbstractAction class attributes and methods

# pcm_av_seff_av_AbstractBranchTransition class attributes and methods

# BranchAction class attributes and methods

# ResourceDemandingBehaviour class attributes and methods

# pcm_av_seff_av_ResourceDemandingBehaviour class attributes and methods
pcm_av_seff_av_ResourceDemandingBehaviour_m_ExactlyOneStopAction: Method = Method(name="ExactlyOneStopAction", parameters={Parameter(name='pcm_av_context', type=StringType), Parameter(name='pcm_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_seff_av_ResourceDemandingBehaviour_m_ExactlyOneStartAction: Method = Method(name="ExactlyOneStartAction", parameters={Parameter(name='pcm_av_context', type=StringType), Parameter(name='pcm_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_seff_av_ResourceDemandingBehaviour_m_EachActionExceptStartActionandStopActionMustHhaveAPredecessorAndSuccessor: Method = Method(name="EachActionExceptStartActionandStopActionMustHhaveAPredecessorAndSuccessor", parameters={Parameter(name='pcm_av_context', type=StringType), Parameter(name='pcm_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_seff_av_ResourceDemandingBehaviour.methods={pcm_av_seff_av_ResourceDemandingBehaviour_m_ExactlyOneStopAction, pcm_av_seff_av_ResourceDemandingBehaviour_m_EachActionExceptStartActionandStopActionMustHhaveAPredecessorAndSuccessor, pcm_av_seff_av_ResourceDemandingBehaviour_m_ExactlyOneStartAction}

# AbstractLoopAction class attributes and methods

# AbstractBranchTransition class attributes and methods

# pcm_av_seff_av_AbstractLoopAction class attributes and methods

# pcm_av_seff_av_ResourceDemandingSEFF class attributes and methods

# seff_av_ServiceEffectSpecification class attributes and methods

# pcm_av_seff_av_BranchAction class attributes and methods
pcm_av_seff_av_BranchAction_m_EitherGuardedBranchesOrProbabilisiticBranchTransitions: Method = Method(name="EitherGuardedBranchesOrProbabilisiticBranchTransitions", parameters={Parameter(name='pcm_av_diagnostics', type=StringType), Parameter(name='pcm_av_context', type=StringType)}, type=BooleanType)
pcm_av_seff_av_BranchAction_m_AllProbabilisticBranchProbabilitiesMustSumUpTo1: Method = Method(name="AllProbabilisticBranchProbabilitiesMustSumUpTo1", parameters={Parameter(name='pcm_av_context', type=StringType), Parameter(name='pcm_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_seff_av_BranchAction.methods={pcm_av_seff_av_BranchAction_m_EitherGuardedBranchesOrProbabilisiticBranchTransitions, pcm_av_seff_av_BranchAction_m_AllProbabilisticBranchProbabilitiesMustSumUpTo1}

# pcm_av_seff_av_CallAction class attributes and methods

# pcm_av_seff_av_StartAction class attributes and methods
pcm_av_seff_av_StartAction_m_StartActionPredecessorMustNotBeDefined: Method = Method(name="StartActionPredecessorMustNotBeDefined", parameters={Parameter(name='pcm_av_diagnostics', type=StringType), Parameter(name='pcm_av_context', type=StringType)}, type=BooleanType)
pcm_av_seff_av_StartAction.methods={pcm_av_seff_av_StartAction_m_StartActionPredecessorMustNotBeDefined}

# pcm_av_seff_av_ServiceEffectSpecification class attributes and methods
pcm_av_seff_av_ServiceEffectSpecification_seffTypeID: Property = Property(name="seffTypeID", type=StringType)
pcm_av_seff_av_ServiceEffectSpecification_m_ReferencedSignatureMustBelongToInterfaceReferencedByProvidedRole: Method = Method(name="ReferencedSignatureMustBelongToInterfaceReferencedByProvidedRole", parameters={Parameter(name='pcm_av_context', type=StringType), Parameter(name='pcm_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_seff_av_ServiceEffectSpecification.attributes={pcm_av_seff_av_ServiceEffectSpecification_seffTypeID}
pcm_av_seff_av_ServiceEffectSpecification.methods={pcm_av_seff_av_ServiceEffectSpecification_m_ReferencedSignatureMustBelongToInterfaceReferencedByProvidedRole}

# pcm_av_seff_av_ExternalCallAction class attributes and methods
pcm_av_seff_av_ExternalCallAction_retryCount: Property = Property(name="retryCount", type=IntegerType)
pcm_av_seff_av_ExternalCallAction_m_SignatureBelongsToRole: Method = Method(name="SignatureBelongsToRole", parameters={Parameter(name='pcm_av_context', type=StringType), Parameter(name='pcm_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_seff_av_ExternalCallAction_m_OperationRequiredRoleMustBeReferencedByContainer: Method = Method(name="OperationRequiredRoleMustBeReferencedByContainer", parameters={Parameter(name='pcm_av_context', type=StringType), Parameter(name='pcm_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_seff_av_ExternalCallAction.attributes={pcm_av_seff_av_ExternalCallAction_retryCount}
pcm_av_seff_av_ExternalCallAction.methods={pcm_av_seff_av_ExternalCallAction_m_OperationRequiredRoleMustBeReferencedByContainer, pcm_av_seff_av_ExternalCallAction_m_SignatureBelongsToRole}

# seff_av_AbstractAction class attributes and methods

# seff_av_CallReturnAction class attributes and methods

# seff_reliability_av_FailureHandlingEntity class attributes and methods

# seff_av_ResourceDemandingBehaviour class attributes and methods

# ResourceDemandingInternalBehaviour class attributes and methods

# pcm_av_seff_av_ResourceDemandingInternalBehaviour class attributes and methods

# ResourceDemandingSEFF class attributes and methods

# pcm_av_seff_av_ReleaseAction class attributes and methods

# pcm_av_seff_av_LoopAction class attributes and methods

# pcm_av_seff_av_ForkAction class attributes and methods

# ForkedBehaviour class attributes and methods

# pcm_av_seff_av_ForkedBehaviour class attributes and methods

# ForkAction class attributes and methods

# pcm_av_seff_av_SynchronisationPoint class attributes and methods

# pcm_av_seff_av_CallReturnAction class attributes and methods

# pcm_av_seff_av_ProbabilisticBranchTransition class attributes and methods
pcm_av_seff_av_ProbabilisticBranchTransition_branchProbability: Property = Property(name="branchProbability", type=FloatType)
pcm_av_seff_av_ProbabilisticBranchTransition.attributes={pcm_av_seff_av_ProbabilisticBranchTransition_branchProbability}

# pcm_av_seff_av_AcquireAction class attributes and methods
pcm_av_seff_av_AcquireAction_timeout: Property = Property(name="timeout", type=BooleanType)
pcm_av_seff_av_AcquireAction_timeoutValue: Property = Property(name="timeoutValue", type=FloatType)
pcm_av_seff_av_AcquireAction_m_TimeoutValueOfAcquireActionMustNotBeNegative: Method = Method(name="TimeoutValueOfAcquireActionMustNotBeNegative", parameters={Parameter(name='pcm_av_context', type=StringType), Parameter(name='pcm_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_seff_av_AcquireAction.attributes={pcm_av_seff_av_AcquireAction_timeout, pcm_av_seff_av_AcquireAction_timeoutValue}
pcm_av_seff_av_AcquireAction.methods={pcm_av_seff_av_AcquireAction_m_TimeoutValueOfAcquireActionMustNotBeNegative}

# pcm_av_seff_av_CollectionIteratorAction class attributes and methods

# pcm_av_seff_av_GuardedBranchTransition class attributes and methods

# pcm_av_seff_av_SetVariableAction class attributes and methods

# pcm_av_seff_av_InternalCallAction class attributes and methods

# seff_av_CallAction class attributes and methods

# seff_av_AbstractInternalControlFlowAction class attributes and methods

# pcm_av_seff_av_EmitEventAction class attributes and methods

# pcm_av_seff_av_InternalAction class attributes and methods
pcm_av_seff_av_InternalAction_m_SumOfInternalActionFailureProbabilitiesMustNotExceed1: Method = Method(name="SumOfInternalActionFailureProbabilitiesMustNotExceed1", parameters={Parameter(name='pcm_av_diagnostics', type=StringType), Parameter(name='pcm_av_context', type=StringType)}, type=BooleanType)
pcm_av_seff_av_InternalAction_m_MultipleInternalOccurrenceDescriptionsPerFailureTypeNotAllowed: Method = Method(name="MultipleInternalOccurrenceDescriptionsPerFailureTypeNotAllowed", parameters={Parameter(name='pcm_av_context', type=StringType), Parameter(name='pcm_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_seff_av_InternalAction.methods={pcm_av_seff_av_InternalAction_m_MultipleInternalOccurrenceDescriptionsPerFailureTypeNotAllowed, pcm_av_seff_av_InternalAction_m_SumOfInternalActionFailureProbabilitiesMustNotExceed1}

# pcm_av_seff_performance_av_ResourceCall class attributes and methods
pcm_av_seff_performance_av_ResourceCall_m_ResourceSignatureBelongsToResourceRequiredRole: Method = Method(name="ResourceSignatureBelongsToResourceRequiredRole", parameters={Parameter(name='pcm_av_context', type=StringType), Parameter(name='pcm_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_seff_performance_av_ResourceCall_m_ResourceRequiredRoleMustBeReferencedByComponent: Method = Method(name="ResourceRequiredRoleMustBeReferencedByComponent", parameters={Parameter(name='pcm_av_context', type=StringType), Parameter(name='pcm_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_seff_performance_av_ResourceCall_m_SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction: Method = Method(name="SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction", parameters={Parameter(name='pcm_av_context', type=StringType), Parameter(name='pcm_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_seff_performance_av_ResourceCall.methods={pcm_av_seff_performance_av_ResourceCall_m_SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction, pcm_av_seff_performance_av_ResourceCall_m_ResourceRequiredRoleMustBeReferencedByComponent, pcm_av_seff_performance_av_ResourceCall_m_ResourceSignatureBelongsToResourceRequiredRole}

# pcm_av_seff_performance_av_InfrastructureCall class attributes and methods
pcm_av_seff_performance_av_InfrastructureCall_m_SignatureMustBelongToUsedRequiredRole: Method = Method(name="SignatureMustBelongToUsedRequiredRole", parameters={Parameter(name='pcm_av_context', type=StringType), Parameter(name='pcm_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_seff_performance_av_InfrastructureCall_m_ReferencedRequiredRoleMustBeRequiredByComponent: Method = Method(name="ReferencedRequiredRoleMustBeRequiredByComponent", parameters={Parameter(name='pcm_av_diagnostics', type=StringType), Parameter(name='pcm_av_context', type=StringType)}, type=BooleanType)
pcm_av_seff_performance_av_InfrastructureCall_m_SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction: Method = Method(name="SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction", parameters={Parameter(name='pcm_av_diagnostics', type=StringType), Parameter(name='pcm_av_context', type=StringType)}, type=BooleanType)
pcm_av_seff_performance_av_InfrastructureCall.methods={pcm_av_seff_performance_av_InfrastructureCall_m_SignatureMustBelongToUsedRequiredRole, pcm_av_seff_performance_av_InfrastructureCall_m_SignatureRoleCombinationMustBeUniqueWithinAbstractInternalControlFlowAction, pcm_av_seff_performance_av_InfrastructureCall_m_ReferencedRequiredRoleMustBeRequiredByComponent}

# pcm_av_seff_reliability_av_RecoveryActionBehaviour class attributes and methods
pcm_av_seff_reliability_av_RecoveryActionBehaviour_m_RecoveryActionBehaviourHasOnlyOnePredecessor: Method = Method(name="RecoveryActionBehaviourHasOnlyOnePredecessor", parameters={Parameter(name='pcm_av_context', type=StringType), Parameter(name='pcm_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_seff_reliability_av_RecoveryActionBehaviour_m_RecoveryActionBehaviourIsNotSuccessorOfItself: Method = Method(name="RecoveryActionBehaviourIsNotSuccessorOfItself", parameters={Parameter(name='pcm_av_context', type=StringType), Parameter(name='pcm_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_seff_reliability_av_RecoveryActionBehaviour_m_SuccessorsOfRecoveryActionBehaviourHandleDisjointFailureTypes: Method = Method(name="SuccessorsOfRecoveryActionBehaviourHandleDisjointFailureTypes", parameters={Parameter(name='pcm_av_diagnostics', type=StringType), Parameter(name='pcm_av_context', type=StringType)}, type=BooleanType)
pcm_av_seff_reliability_av_RecoveryActionBehaviour.methods={pcm_av_seff_reliability_av_RecoveryActionBehaviour_m_RecoveryActionBehaviourIsNotSuccessorOfItself, pcm_av_seff_reliability_av_RecoveryActionBehaviour_m_RecoveryActionBehaviourHasOnlyOnePredecessor, pcm_av_seff_reliability_av_RecoveryActionBehaviour_m_SuccessorsOfRecoveryActionBehaviourHandleDisjointFailureTypes}

# pcm_av_seff_performance_av_ParametricResourceDemand class attributes and methods
pcm_av_seff_performance_av_ParametricResourceDemand_m_DemandedProcessingResourceMustBeUniqueWithinAbstractInternalControlFlowAction: Method = Method(name="DemandedProcessingResourceMustBeUniqueWithinAbstractInternalControlFlowAction", parameters={Parameter(name='pcm_av_context', type=StringType), Parameter(name='pcm_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_seff_performance_av_ParametricResourceDemand.methods={pcm_av_seff_performance_av_ParametricResourceDemand_m_DemandedProcessingResourceMustBeUniqueWithinAbstractInternalControlFlowAction}

# pcm_av_seff_reliability_av_FailureHandlingEntity class attributes and methods

# seff_reliability_av_RecoveryActionBehaviour class attributes and methods

# seff_reliability_av_RecoveryAction class attributes and methods

# pcm_av_seff_reliability_av_RecoveryAction class attributes and methods
pcm_av_seff_reliability_av_RecoveryAction_m_PrimaryBehaviourOfRecoveryActionMustBeSet: Method = Method(name="PrimaryBehaviourOfRecoveryActionMustBeSet", parameters={Parameter(name='pcm_av_context', type=StringType), Parameter(name='pcm_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_seff_reliability_av_RecoveryAction.methods={pcm_av_seff_reliability_av_RecoveryAction_m_PrimaryBehaviourOfRecoveryActionMustBeSet}

# pcm_av_qos_performance_av_SystemSpecifiedExecutionTime class attributes and methods
pcm_av_qos_performance_av_SystemSpecifiedExecutionTime_m_SystemSpecifiedExecutionTimeMustReferenceRequiredRoleOfASystem: Method = Method(name="SystemSpecifiedExecutionTimeMustReferenceRequiredRoleOfASystem", parameters={Parameter(name='pcm_av_context', type=StringType), Parameter(name='pcm_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_qos_performance_av_SystemSpecifiedExecutionTime.methods={pcm_av_qos_performance_av_SystemSpecifiedExecutionTime_m_SystemSpecifiedExecutionTimeMustReferenceRequiredRoleOfASystem}

# SpecifiedExecutionTime class attributes and methods

# pcm_av_qosannotations_av_SpecifiedQoSAnnotation class attributes and methods

# QoSAnnotations class attributes and methods

# pcm_av_qosannotations_av_QoSAnnotations class attributes and methods
pcm_av_qosannotations_av_QoSAnnotations_m_MultipleReliabilityAnnotationsPerExternalCallNotAllowed: Method = Method(name="MultipleReliabilityAnnotationsPerExternalCallNotAllowed", parameters={Parameter(name='pcm_av_context', type=StringType), Parameter(name='pcm_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_qosannotations_av_QoSAnnotations.methods={pcm_av_qosannotations_av_QoSAnnotations_m_MultipleReliabilityAnnotationsPerExternalCallNotAllowed}

# System class attributes and methods

# SpecifiedQoSAnnotation class attributes and methods

# pcm_av_qosannotations_av_SpecifiedOutputParameterAbstraction class attributes and methods

# pcm_av_system_av_System class attributes and methods
pcm_av_system_av_System_m_SystemMustHaveAtLeastOneProvidedRole: Method = Method(name="SystemMustHaveAtLeastOneProvidedRole", parameters={Parameter(name='pcm_av_context', type=StringType), Parameter(name='pcm_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_system_av_System.methods={pcm_av_system_av_System_m_SystemMustHaveAtLeastOneProvidedRole}

# pcm_av_qos_performance_av_SpecifiedExecutionTime class attributes and methods

# pcm_av_qos_performance_av_ComponentSpecifiedExecutionTime class attributes and methods

# pcm_av_qos_reliability_av_SpecifiedReliabilityAnnotation class attributes and methods
pcm_av_qos_reliability_av_SpecifiedReliabilityAnnotation_m_SpecifiedReliabilityAnnotationMustReferenceRequiredRoleOfASystem: Method = Method(name="SpecifiedReliabilityAnnotationMustReferenceRequiredRoleOfASystem", parameters={Parameter(name='pcm_av_diagnostics', type=StringType), Parameter(name='pcm_av_context', type=StringType)}, type=BooleanType)
pcm_av_qos_reliability_av_SpecifiedReliabilityAnnotation_m_SumOfReliabilityAnnotationFailureProbabilitiesMustNotExceed1: Method = Method(name="SumOfReliabilityAnnotationFailureProbabilitiesMustNotExceed1", parameters={Parameter(name='pcm_av_diagnostics', type=StringType), Parameter(name='pcm_av_context', type=StringType)}, type=BooleanType)
pcm_av_qos_reliability_av_SpecifiedReliabilityAnnotation_m_MultipleExternalOccurrenceDescriptionsPerFailureTypeNotAllowed: Method = Method(name="MultipleExternalOccurrenceDescriptionsPerFailureTypeNotAllowed", parameters={Parameter(name='pcm_av_context', type=StringType), Parameter(name='pcm_av_diagnostics', type=StringType)}, type=BooleanType)
pcm_av_qos_reliability_av_SpecifiedReliabilityAnnotation.methods={pcm_av_qos_reliability_av_SpecifiedReliabilityAnnotation_m_MultipleExternalOccurrenceDescriptionsPerFailureTypeNotAllowed, pcm_av_qos_reliability_av_SpecifiedReliabilityAnnotation_m_SpecifiedReliabilityAnnotationMustReferenceRequiredRoleOfASystem, pcm_av_qos_reliability_av_SpecifiedReliabilityAnnotation_m_SumOfReliabilityAnnotationFailureProbabilitiesMustNotExceed1}

# ExternalFailureOccurrenceDescription class attributes and methods

# pcm_av_resourceenvironment_av_ProcessingResourceSpecification class attributes and methods
pcm_av_resourceenvironment_av_ProcessingResourceSpecification_MTTR: Property = Property(name="MTTR", type=FloatType)
pcm_av_resourceenvironment_av_ProcessingResourceSpecification_MTTF: Property = Property(name="MTTF", type=FloatType)
pcm_av_resourceenvironment_av_ProcessingResourceSpecification_requiredByContainer: Property = Property(name="requiredByContainer", type=BooleanType)
pcm_av_resourceenvironment_av_ProcessingResourceSpecification_numberOfReplicas: Property = Property(name="numberOfReplicas", type=IntegerType)
pcm_av_resourceenvironment_av_ProcessingResourceSpecification.attributes={pcm_av_resourceenvironment_av_ProcessingResourceSpecification_MTTF, pcm_av_resourceenvironment_av_ProcessingResourceSpecification_requiredByContainer, pcm_av_resourceenvironment_av_ProcessingResourceSpecification_numberOfReplicas, pcm_av_resourceenvironment_av_ProcessingResourceSpecification_MTTR}

# pcm_av_resourceenvironment_av_ResourceEnvironment class attributes and methods

# LinkingResource class attributes and methods

# ResourceContainer class attributes and methods

# pcm_av_resourceenvironment_av_LinkingResource class attributes and methods

# ResourceEnvironment class attributes and methods

# pcm_av_resourceenvironment_av_ResourceContainer class attributes and methods

# Allocation class attributes and methods

# pcm_av_allocation_av_Allocation class attributes and methods
pcm_av_allocation_av_Allocation_m_EachAssemblyContextWithinSystemHasToBeAllocatedExactlyOnce: Method = Method(name="EachAssemblyContextWithinSystemHasToBeAllocatedExactlyOnce", parameters={Parameter(name='pcm_av_diagnostics', type=StringType), Parameter(name='pcm_av_context', type=StringType)}, type=BooleanType)
pcm_av_allocation_av_Allocation_m_CommunicatingServersHaveToBeConnectedByLinkingResource: Method = Method(name="CommunicatingServersHaveToBeConnectedByLinkingResource", parameters={Parameter(name='pcm_av_diagnostics', type=StringType), Parameter(name='pcm_av_context', type=StringType)}, type=BooleanType)
pcm_av_allocation_av_Allocation.methods={pcm_av_allocation_av_Allocation_m_EachAssemblyContextWithinSystemHasToBeAllocatedExactlyOnce, pcm_av_allocation_av_Allocation_m_CommunicatingServersHaveToBeConnectedByLinkingResource}

# pcm_av_resourceenvironment_av_CommunicationLinkResourceSpecification class attributes and methods
pcm_av_resourceenvironment_av_CommunicationLinkResourceSpecification_failureProbability: Property = Property(name="failureProbability", type=FloatType)
pcm_av_resourceenvironment_av_CommunicationLinkResourceSpecification.attributes={pcm_av_resourceenvironment_av_CommunicationLinkResourceSpecification_failureProbability}

# pcm_av_allocation_av_AllocationContext class attributes and methods
pcm_av_allocation_av_AllocationContext_m_OneAssemblyContextOrOneEventChannelShouldBeReferred: Method = Method(name="OneAssemblyContextOrOneEventChannelShouldBeReferred", parameters={Parameter(name='pcm_av_diagnostics', type=StringType), Parameter(name='pcm_av_context', type=StringType)}, type=BooleanType)
pcm_av_allocation_av_AllocationContext.methods={pcm_av_allocation_av_AllocationContext_m_OneAssemblyContextOrOneEventChannelShouldBeReferred}

# pcm_av_completions_av_Completion class attributes and methods

# pcm_av_completions_av_CompletionRepository class attributes and methods

# Completion class attributes and methods

# pcm_av_completions_av_DelegatingExternalCallAction class attributes and methods

# ExternalCallAction class attributes and methods

# pcm_av_completions_av_NetworkDemandParametricResourceDemand class attributes and methods

# ParametricResourceDemand class attributes and methods

# AllocationContext class attributes and methods

# pcm_av_subsystem_av_SubSystem class attributes and methods

# repository_av_RepositoryComponent class attributes and methods

# Relationships
guardedBranchTransition_PCMRandomVariable12: BinaryAssociation = BinaryAssociation(
    name="guardedBranchTransition_PCMRandomVariable12",
    ends={
        Property(name="GuardedBranchTransition", type=pcm_av_core_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="branchCondition_GuardedBranchTransition", type=GuardedBranchTransition, multiplicity=Multiplicity(0, 1))
    }
)
children0: BinaryAssociation = BinaryAssociation(
    name="children0",
    ends={
        Property(name="pcm_av_EObject", type=pcm_av_Advice, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_Advice", type=pcm_av_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
scopedObject1: BinaryAssociation = BinaryAssociation(
    name="scopedObject1",
    ends={
        Property(name="pcm_av_EObject2", type=pcm_av_GlobalScope, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_GlobalScope", type=pcm_av_EObject, multiplicity=Multiplicity(1, 1))
    }
)
scopedObject3: BinaryAssociation = BinaryAssociation(
    name="scopedObject3",
    ends={
        Property(name="pcm_av_EObject4", type=pcm_av_PerJoinPointScope, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_PerJoinPointScope", type=pcm_av_EObject, multiplicity=Multiplicity(1, 1))
    }
)
closedWorkload_PCMRandomVariable5: BinaryAssociation = BinaryAssociation(
    name="closedWorkload_PCMRandomVariable5",
    ends={
        Property(name="ClosedWorkload", type=pcm_av_core_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="thinkTime_ClosedWorkload", type=ClosedWorkload, multiplicity=Multiplicity(0, 1))
    }
)
passiveResource_capacity_PCMRandomVariable6: BinaryAssociation = BinaryAssociation(
    name="passiveResource_capacity_PCMRandomVariable6",
    ends={
        Property(name="PassiveResource", type=pcm_av_core_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="capacity_PassiveResource", type=PassiveResource, multiplicity=Multiplicity(0, 1))
    }
)
variableCharacterisation_Specification7: BinaryAssociation = BinaryAssociation(
    name="variableCharacterisation_Specification7",
    ends={
        Property(name="VariableCharacterisation", type=pcm_av_core_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="specification_VariableCharacterisation", type=VariableCharacterisation, multiplicity=Multiplicity(0, 1))
    }
)
infrastructureCall__PCMRandomVariable8: BinaryAssociation = BinaryAssociation(
    name="infrastructureCall__PCMRandomVariable8",
    ends={
        Property(name="InfrastructureCall", type=pcm_av_core_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="numberOfCalls__InfrastructureCall", type=seff_performance_av_InfrastructureCall, multiplicity=Multiplicity(0, 1))
    }
)
resourceCall__PCMRandomVariable9: BinaryAssociation = BinaryAssociation(
    name="resourceCall__PCMRandomVariable9",
    ends={
        Property(name="ResourceCall", type=pcm_av_core_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="numberOfCalls__ResourceCall", type=seff_performance_av_ResourceCall, multiplicity=Multiplicity(0, 1))
    }
)
parametricResourceDemand_PCMRandomVariable10: BinaryAssociation = BinaryAssociation(
    name="parametricResourceDemand_PCMRandomVariable10",
    ends={
        Property(name="ParametricResourceDemand", type=pcm_av_core_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="specification_ParametericResourceDemand", type=seff_performance_av_ParametricResourceDemand, multiplicity=Multiplicity(0, 1))
    }
)
loopAction_PCMRandomVariable11: BinaryAssociation = BinaryAssociation(
    name="loopAction_PCMRandomVariable11",
    ends={
        Property(name="LoopAction", type=pcm_av_core_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="iterationCount_LoopAction", type=LoopAction, multiplicity=Multiplicity(0, 1))
    }
)
resourceRequiredRoles__ResourceInterfaceRequiringEntity27: BinaryAssociation = BinaryAssociation(
    name="resourceRequiredRoles__ResourceInterfaceRequiringEntity27",
    ends={
        Property(name="ResourceRequiredRole", type=pcm_av_entity_av_ResourceInterfaceRequiringEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceInterfaceRequiringEntity__ResourceRequiredRole", type=entity_av_ResourceRequiredRole, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specifiedExecutionTime_PCMRandomVariable13: BinaryAssociation = BinaryAssociation(
    name="specifiedExecutionTime_PCMRandomVariable13",
    ends={
        Property(name="SpecifiedExecutionTime", type=pcm_av_core_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="specification_SpecifiedExecutionTime", type=qos_performance_av_SpecifiedExecutionTime, multiplicity=Multiplicity(0, 1))
    }
)
eventChannelSinkConnector__FilterCondition14: BinaryAssociation = BinaryAssociation(
    name="eventChannelSinkConnector__FilterCondition14",
    ends={
        Property(name="EventChannelSinkConnector", type=pcm_av_core_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="filterCondition__EventChannelSinkConnector", type=composition_av_EventChannelSinkConnector, multiplicity=Multiplicity(0, 1))
    }
)
assemblyEventConnector__FilterCondition15: BinaryAssociation = BinaryAssociation(
    name="assemblyEventConnector__FilterCondition15",
    ends={
        Property(name="AssemblyEventConnector", type=pcm_av_core_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="filterCondition__AssemblyEventConnector", type=composition_av_AssemblyEventConnector, multiplicity=Multiplicity(0, 1))
    }
)
loop_LoopIteration16: BinaryAssociation = BinaryAssociation(
    name="loop_LoopIteration16",
    ends={
        Property(name="Loop", type=pcm_av_core_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="loopIteration_Loop", type=Loop, multiplicity=Multiplicity(0, 1))
    }
)
openWorkload_PCMRandomVariable17: BinaryAssociation = BinaryAssociation(
    name="openWorkload_PCMRandomVariable17",
    ends={
        Property(name="OpenWorkload", type=pcm_av_core_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="interArrivalTime_OpenWorkload", type=OpenWorkload, multiplicity=Multiplicity(0, 1))
    }
)
delay_TimeSpecification18: BinaryAssociation = BinaryAssociation(
    name="delay_TimeSpecification18",
    ends={
        Property(name="Delay", type=pcm_av_core_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="timeSpecification_Delay", type=Delay, multiplicity=Multiplicity(0, 1))
    }
)
communicationLinkResourceSpecifcation_throughput_PCMRandomVariable19: BinaryAssociation = BinaryAssociation(
    name="communicationLinkResourceSpecifcation_throughput_PCMRandomVariable19",
    ends={
        Property(name="CommunicationLinkResourceSpecification", type=pcm_av_core_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="throughput_CommunicationLinkResourceSpecification", type=CommunicationLinkResourceSpecification, multiplicity=Multiplicity(0, 1))
    }
)
processingResourceSpecification_processingRate_PCMRandomVariable20: BinaryAssociation = BinaryAssociation(
    name="processingResourceSpecification_processingRate_PCMRandomVariable20",
    ends={
        Property(name="ProcessingResourceSpecification", type=pcm_av_core_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="processingRate_ProcessingResourceSpecification", type=ProcessingResourceSpecification, multiplicity=Multiplicity(0, 1))
    }
)
communicationLinkResourceSpecification_latency_PCMRandomVariable21: BinaryAssociation = BinaryAssociation(
    name="communicationLinkResourceSpecification_latency_PCMRandomVariable21",
    ends={
        Property(name="CommunicationLinkResourceSpecification22", type=pcm_av_core_av_PCMRandomVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="latency_CommunicationLinkResourceSpecification", type=CommunicationLinkResourceSpecification, multiplicity=Multiplicity(0, 1))
    }
)
resourceInterfaceProvidingEntity__ResourceProvidedRole23: BinaryAssociation = BinaryAssociation(
    name="resourceInterfaceProvidingEntity__ResourceProvidedRole23",
    ends={
        Property(name="ResourceInterfaceProvidingEntity", type=pcm_av_entity_av_ResourceProvidedRole, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceProvidedRoles__ResourceInterfaceProvidingEntity", type=entity_av_ResourceInterfaceProvidingEntity, multiplicity=Multiplicity(0, 1))
    }
)
providedResourceInterface__ResourceProvidedRole24: BinaryAssociation = BinaryAssociation(
    name="providedResourceInterface__ResourceProvidedRole24",
    ends={
        Property(name="ResourceInterface", type=pcm_av_entity_av_ResourceProvidedRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_entity_av_ResourceProvidedRole", type=ResourceInterface, multiplicity=Multiplicity(0, 1))
    }
)
providedRoles_InterfaceProvidingEntity25: BinaryAssociation = BinaryAssociation(
    name="providedRoles_InterfaceProvidingEntity25",
    ends={
        Property(name="ProvidedRole", type=pcm_av_entity_av_InterfaceProvidingEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="providingEntity_ProvidedRole", type=ProvidedRole, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredRoles_InterfaceRequiringEntity26: BinaryAssociation = BinaryAssociation(
    name="requiredRoles_InterfaceRequiringEntity26",
    ends={
        Property(name="RequiredRole", type=pcm_av_entity_av_InterfaceRequiringEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="requiringEntity_RequiredRole", type=RequiredRole, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredResourceInterface__ResourceRequiredRole28: BinaryAssociation = BinaryAssociation(
    name="requiredResourceInterface__ResourceRequiredRole28",
    ends={
        Property(name="ResourceInterface29", type=pcm_av_entity_av_ResourceRequiredRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_entity_av_ResourceRequiredRole", type=ResourceInterface, multiplicity=Multiplicity(0, 1))
    }
)
resourceInterfaceRequiringEntity__ResourceRequiredRole30: BinaryAssociation = BinaryAssociation(
    name="resourceInterfaceRequiringEntity__ResourceRequiredRole30",
    ends={
        Property(name="ResourceInterfaceRequiringEntity", type=pcm_av_entity_av_ResourceRequiredRole, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceRequiredRoles__ResourceInterfaceRequiringEntity", type=entity_av_ResourceInterfaceRequiringEntity, multiplicity=Multiplicity(0, 1))
    }
)
resourceProvidedRoles__ResourceInterfaceProvidingEntity31: BinaryAssociation = BinaryAssociation(
    name="resourceProvidedRoles__ResourceInterfaceProvidingEntity31",
    ends={
        Property(name="ResourceProvidedRole", type=pcm_av_entity_av_ResourceInterfaceProvidingEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceInterfaceProvidingEntity__ResourceProvidedRole", type=entity_av_ResourceProvidedRole, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentStructure__Connector32: BinaryAssociation = BinaryAssociation(
    name="parentStructure__Connector32",
    ends={
        Property(name="ComposedStructure", type=pcm_av_composition_av_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="connectors__ComposedStructure", type=composition_av_ComposedStructure, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContexts__ComposedStructure33: BinaryAssociation = BinaryAssociation(
    name="assemblyContexts__ComposedStructure33",
    ends={
        Property(name="AssemblyContext", type=pcm_av_composition_av_ComposedStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="parentStructure__AssemblyContext", type=composition_av_AssemblyContext, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceRequiredDelegationConnectors_ComposedStructure34: BinaryAssociation = BinaryAssociation(
    name="resourceRequiredDelegationConnectors_ComposedStructure34",
    ends={
        Property(name="ResourceRequiredDelegationConnector", type=pcm_av_composition_av_ComposedStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="parentStructure_ResourceRequiredDelegationConnector", type=composition_av_ResourceRequiredDelegationConnector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eventChannel__ComposedStructure35: BinaryAssociation = BinaryAssociation(
    name="eventChannel__ComposedStructure35",
    ends={
        Property(name="EventChannel", type=pcm_av_composition_av_ComposedStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="parentStructure__EventChannel", type=composition_av_EventChannel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connectors__ComposedStructure36: BinaryAssociation = BinaryAssociation(
    name="connectors__ComposedStructure36",
    ends={
        Property(name="Connector", type=pcm_av_composition_av_ComposedStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="parentStructure__Connector", type=composition_av_Connector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
innerResourceRequiredRole_ResourceRequiredDelegationConnector37: BinaryAssociation = BinaryAssociation(
    name="innerResourceRequiredRole_ResourceRequiredDelegationConnector37",
    ends={
        Property(name="entity_av_ResourceRequiredRole", type=pcm_av_composition_av_ResourceRequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_composition_av_ResourceRequiredDelegationConnector", type=entity_av_ResourceRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
outerResourceRequiredRole_ResourceRequiredDelegationConnector38: BinaryAssociation = BinaryAssociation(
    name="outerResourceRequiredRole_ResourceRequiredDelegationConnector38",
    ends={
        Property(name="entity_av_ResourceRequiredRole40", type=pcm_av_composition_av_ResourceRequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_composition_av_ResourceRequiredDelegationConnector39", type=entity_av_ResourceRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
parentStructure_ResourceRequiredDelegationConnector41: BinaryAssociation = BinaryAssociation(
    name="parentStructure_ResourceRequiredDelegationConnector41",
    ends={
        Property(name="ComposedStructure42", type=pcm_av_composition_av_ResourceRequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceRequiredDelegationConnectors_ComposedStructure", type=composition_av_ComposedStructure, multiplicity=Multiplicity(0, 1))
    }
)
eventGroup__EventChannel43: BinaryAssociation = BinaryAssociation(
    name="eventGroup__EventChannel43",
    ends={
        Property(name="EventGroup", type=pcm_av_composition_av_EventChannel, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_composition_av_EventChannel", type=EventGroup, multiplicity=Multiplicity(0, 1))
    }
)
eventChannelSourceConnector__EventChannel44: BinaryAssociation = BinaryAssociation(
    name="eventChannelSourceConnector__EventChannel44",
    ends={
        Property(name="EventChannelSourceConnector", type=pcm_av_composition_av_EventChannel, multiplicity=Multiplicity(1, 1)),
        Property(name="eventChannel__EventChannelSourceConnector", type=composition_av_EventChannelSourceConnector, multiplicity=Multiplicity(0, 9999))
    }
)
eventChannelSinkConnector__EventChannel45: BinaryAssociation = BinaryAssociation(
    name="eventChannelSinkConnector__EventChannel45",
    ends={
        Property(name="EventChannelSinkConnector46", type=pcm_av_composition_av_EventChannel, multiplicity=Multiplicity(1, 1)),
        Property(name="eventChannel__EventChannelSinkConnector", type=composition_av_EventChannelSinkConnector, multiplicity=Multiplicity(0, 9999))
    }
)
parentStructure__EventChannel47: BinaryAssociation = BinaryAssociation(
    name="parentStructure__EventChannel47",
    ends={
        Property(name="ComposedStructure48", type=pcm_av_composition_av_EventChannel, multiplicity=Multiplicity(1, 1)),
        Property(name="eventChannel__ComposedStructure", type=composition_av_ComposedStructure, multiplicity=Multiplicity(0, 1))
    }
)
sourceRole__EventChannelSourceRole49: BinaryAssociation = BinaryAssociation(
    name="sourceRole__EventChannelSourceRole49",
    ends={
        Property(name="SourceRole", type=pcm_av_composition_av_EventChannelSourceConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_composition_av_EventChannelSourceConnector", type=SourceRole, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext__EventChannelSourceConnector50: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__EventChannelSourceConnector50",
    ends={
        Property(name="composition_av_AssemblyContext", type=pcm_av_composition_av_EventChannelSourceConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_composition_av_EventChannelSourceConnector51", type=composition_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
eventChannel__EventChannelSourceConnector52: BinaryAssociation = BinaryAssociation(
    name="eventChannel__EventChannelSourceConnector52",
    ends={
        Property(name="EventChannel53", type=pcm_av_composition_av_EventChannelSourceConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="eventChannelSourceConnector__EventChannel", type=composition_av_EventChannel, multiplicity=Multiplicity(0, 1))
    }
)
sinkRole__EventChannelSinkConnector54: BinaryAssociation = BinaryAssociation(
    name="sinkRole__EventChannelSinkConnector54",
    ends={
        Property(name="SinkRole", type=pcm_av_composition_av_EventChannelSinkConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_composition_av_EventChannelSinkConnector", type=SinkRole, multiplicity=Multiplicity(0, 1))
    }
)
filterCondition__EventChannelSinkConnector55: BinaryAssociation = BinaryAssociation(
    name="filterCondition__EventChannelSinkConnector55",
    ends={
        Property(name="PCMRandomVariable", type=pcm_av_composition_av_EventChannelSinkConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="eventChannelSinkConnector__FilterCondition", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assemblyContext__EventChannelSinkConnector56: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__EventChannelSinkConnector56",
    ends={
        Property(name="composition_av_AssemblyContext58", type=pcm_av_composition_av_EventChannelSinkConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_composition_av_EventChannelSinkConnector57", type=composition_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
eventChannel__EventChannelSinkConnector59: BinaryAssociation = BinaryAssociation(
    name="eventChannel__EventChannelSinkConnector59",
    ends={
        Property(name="EventChannel60", type=pcm_av_composition_av_EventChannelSinkConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="eventChannelSinkConnector__EventChannel", type=composition_av_EventChannel, multiplicity=Multiplicity(0, 1))
    }
)
innerProvidedRole_ProvidedDelegationConnector61: BinaryAssociation = BinaryAssociation(
    name="innerProvidedRole_ProvidedDelegationConnector61",
    ends={
        Property(name="OperationProvidedRole", type=pcm_av_composition_av_ProvidedDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_composition_av_ProvidedDelegationConnector", type=OperationProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
outerProvidedRole_ProvidedDelegationConnector62: BinaryAssociation = BinaryAssociation(
    name="outerProvidedRole_ProvidedDelegationConnector62",
    ends={
        Property(name="OperationProvidedRole64", type=pcm_av_composition_av_ProvidedDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_composition_av_ProvidedDelegationConnector63", type=OperationProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext_ProvidedDelegationConnector65: BinaryAssociation = BinaryAssociation(
    name="assemblyContext_ProvidedDelegationConnector65",
    ends={
        Property(name="composition_av_AssemblyContext67", type=pcm_av_composition_av_ProvidedDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_composition_av_ProvidedDelegationConnector66", type=composition_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
innerRequiredRole_RequiredDelegationConnector68: BinaryAssociation = BinaryAssociation(
    name="innerRequiredRole_RequiredDelegationConnector68",
    ends={
        Property(name="OperationRequiredRole", type=pcm_av_composition_av_RequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_composition_av_RequiredDelegationConnector", type=OperationRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
outerRequiredRole_RequiredDelegationConnector69: BinaryAssociation = BinaryAssociation(
    name="outerRequiredRole_RequiredDelegationConnector69",
    ends={
        Property(name="OperationRequiredRole71", type=pcm_av_composition_av_RequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_composition_av_RequiredDelegationConnector70", type=OperationRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext_RequiredDelegationConnector72: BinaryAssociation = BinaryAssociation(
    name="assemblyContext_RequiredDelegationConnector72",
    ends={
        Property(name="composition_av_AssemblyContext74", type=pcm_av_composition_av_RequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_composition_av_RequiredDelegationConnector73", type=composition_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext__SinkDelegationConnector107: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__SinkDelegationConnector107",
    ends={
        Property(name="composition_av_AssemblyContext108", type=pcm_av_composition_av_SinkDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_composition_av_SinkDelegationConnector", type=composition_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
requiringAssemblyContext_AssemblyConnector75: BinaryAssociation = BinaryAssociation(
    name="requiringAssemblyContext_AssemblyConnector75",
    ends={
        Property(name="composition_av_AssemblyContext76", type=pcm_av_composition_av_AssemblyConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_composition_av_AssemblyConnector", type=composition_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
providingAssemblyContext_AssemblyConnector77: BinaryAssociation = BinaryAssociation(
    name="providingAssemblyContext_AssemblyConnector77",
    ends={
        Property(name="composition_av_AssemblyContext79", type=pcm_av_composition_av_AssemblyConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_composition_av_AssemblyConnector78", type=composition_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
providedRole_AssemblyConnector80: BinaryAssociation = BinaryAssociation(
    name="providedRole_AssemblyConnector80",
    ends={
        Property(name="OperationProvidedRole82", type=pcm_av_composition_av_AssemblyConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_composition_av_AssemblyConnector81", type=OperationProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
requiredRole_AssemblyConnector83: BinaryAssociation = BinaryAssociation(
    name="requiredRole_AssemblyConnector83",
    ends={
        Property(name="OperationRequiredRole85", type=pcm_av_composition_av_AssemblyConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_composition_av_AssemblyConnector84", type=OperationRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
sinkRole__AssemblyEventConnector86: BinaryAssociation = BinaryAssociation(
    name="sinkRole__AssemblyEventConnector86",
    ends={
        Property(name="SinkRole87", type=pcm_av_composition_av_AssemblyEventConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_composition_av_AssemblyEventConnector", type=SinkRole, multiplicity=Multiplicity(0, 1))
    }
)
sourceRole__AssemblyEventConnector88: BinaryAssociation = BinaryAssociation(
    name="sourceRole__AssemblyEventConnector88",
    ends={
        Property(name="SourceRole90", type=pcm_av_composition_av_AssemblyEventConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_composition_av_AssemblyEventConnector89", type=SourceRole, multiplicity=Multiplicity(0, 1))
    }
)
sinkAssemblyContext__AssemblyEventConnector91: BinaryAssociation = BinaryAssociation(
    name="sinkAssemblyContext__AssemblyEventConnector91",
    ends={
        Property(name="composition_av_AssemblyContext93", type=pcm_av_composition_av_AssemblyEventConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_composition_av_AssemblyEventConnector92", type=composition_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
sourceAssemblyContext__AssemblyEventConnector94: BinaryAssociation = BinaryAssociation(
    name="sourceAssemblyContext__AssemblyEventConnector94",
    ends={
        Property(name="composition_av_AssemblyContext96", type=pcm_av_composition_av_AssemblyEventConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_composition_av_AssemblyEventConnector95", type=composition_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
filterCondition__AssemblyEventConnector97: BinaryAssociation = BinaryAssociation(
    name="filterCondition__AssemblyEventConnector97",
    ends={
        Property(name="PCMRandomVariable98", type=pcm_av_composition_av_AssemblyEventConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="assemblyEventConnector__FilterCondition", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
innerSourceRole__SourceRole99: BinaryAssociation = BinaryAssociation(
    name="innerSourceRole__SourceRole99",
    ends={
        Property(name="SourceRole100", type=pcm_av_composition_av_SourceDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_composition_av_SourceDelegationConnector", type=SourceRole, multiplicity=Multiplicity(0, 1))
    }
)
outerSourceRole__SourceRole101: BinaryAssociation = BinaryAssociation(
    name="outerSourceRole__SourceRole101",
    ends={
        Property(name="SourceRole103", type=pcm_av_composition_av_SourceDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_composition_av_SourceDelegationConnector102", type=SourceRole, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext__SourceDelegationConnector104: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__SourceDelegationConnector104",
    ends={
        Property(name="composition_av_AssemblyContext106", type=pcm_av_composition_av_SourceDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_composition_av_SourceDelegationConnector105", type=composition_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
configParameterUsages__AssemblyContext151: BinaryAssociation = BinaryAssociation(
    name="configParameterUsages__AssemblyContext151",
    ends={
        Property(name="VariableUsage", type=pcm_av_composition_av_AssemblyContext, multiplicity=Multiplicity(1, 1)),
        Property(name="assemblyContext__VariableUsage", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
innerSinkRole__SinkRole109: BinaryAssociation = BinaryAssociation(
    name="innerSinkRole__SinkRole109",
    ends={
        Property(name="SinkRole111", type=pcm_av_composition_av_SinkDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_composition_av_SinkDelegationConnector110", type=SinkRole, multiplicity=Multiplicity(0, 1))
    }
)
outerSinkRole__SinkRole112: BinaryAssociation = BinaryAssociation(
    name="outerSinkRole__SinkRole112",
    ends={
        Property(name="SinkRole114", type=pcm_av_composition_av_SinkDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_composition_av_SinkDelegationConnector113", type=SinkRole, multiplicity=Multiplicity(0, 1))
    }
)
providedRole__AssemblyInfrastructureConnector115: BinaryAssociation = BinaryAssociation(
    name="providedRole__AssemblyInfrastructureConnector115",
    ends={
        Property(name="InfrastructureProvidedRole", type=pcm_av_composition_av_AssemblyInfrastructureConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_composition_av_AssemblyInfrastructureConnector", type=InfrastructureProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
requiredRole__AssemblyInfrastructureConnector116: BinaryAssociation = BinaryAssociation(
    name="requiredRole__AssemblyInfrastructureConnector116",
    ends={
        Property(name="InfrastructureRequiredRole", type=pcm_av_composition_av_AssemblyInfrastructureConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_composition_av_AssemblyInfrastructureConnector117", type=InfrastructureRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
providingAssemblyContext__AssemblyInfrastructureConnector118: BinaryAssociation = BinaryAssociation(
    name="providingAssemblyContext__AssemblyInfrastructureConnector118",
    ends={
        Property(name="composition_av_AssemblyContext120", type=pcm_av_composition_av_AssemblyInfrastructureConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_composition_av_AssemblyInfrastructureConnector119", type=composition_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
requiringAssemblyContext__AssemblyInfrastructureConnector121: BinaryAssociation = BinaryAssociation(
    name="requiringAssemblyContext__AssemblyInfrastructureConnector121",
    ends={
        Property(name="composition_av_AssemblyContext123", type=pcm_av_composition_av_AssemblyInfrastructureConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_composition_av_AssemblyInfrastructureConnector122", type=composition_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
innerProvidedRole__ProvidedInfrastructureDelegationConnector124: BinaryAssociation = BinaryAssociation(
    name="innerProvidedRole__ProvidedInfrastructureDelegationConnector124",
    ends={
        Property(name="InfrastructureProvidedRole125", type=pcm_av_composition_av_ProvidedInfrastructureDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_composition_av_ProvidedInfrastructureDelegationConnector", type=InfrastructureProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
outerProvidedRole__ProvidedInfrastructureDelegationConnector126: BinaryAssociation = BinaryAssociation(
    name="outerProvidedRole__ProvidedInfrastructureDelegationConnector126",
    ends={
        Property(name="InfrastructureProvidedRole128", type=pcm_av_composition_av_ProvidedInfrastructureDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_composition_av_ProvidedInfrastructureDelegationConnector127", type=InfrastructureProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext__ProvidedInfrastructureDelegationConnector129: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__ProvidedInfrastructureDelegationConnector129",
    ends={
        Property(name="composition_av_AssemblyContext131", type=pcm_av_composition_av_ProvidedInfrastructureDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_composition_av_ProvidedInfrastructureDelegationConnector130", type=composition_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
innerRequiredRole__RequiredInfrastructureDelegationConnector132: BinaryAssociation = BinaryAssociation(
    name="innerRequiredRole__RequiredInfrastructureDelegationConnector132",
    ends={
        Property(name="InfrastructureRequiredRole133", type=pcm_av_composition_av_RequiredInfrastructureDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_composition_av_RequiredInfrastructureDelegationConnector", type=InfrastructureRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
outerRequiredRole__RequiredInfrastructureDelegationConnector134: BinaryAssociation = BinaryAssociation(
    name="outerRequiredRole__RequiredInfrastructureDelegationConnector134",
    ends={
        Property(name="InfrastructureRequiredRole136", type=pcm_av_composition_av_RequiredInfrastructureDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_composition_av_RequiredInfrastructureDelegationConnector135", type=InfrastructureRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext__RequiredInfrastructureDelegationConnector137: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__RequiredInfrastructureDelegationConnector137",
    ends={
        Property(name="composition_av_AssemblyContext139", type=pcm_av_composition_av_RequiredInfrastructureDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_composition_av_RequiredInfrastructureDelegationConnector138", type=composition_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext__RequiredResourceDelegationConnector140: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__RequiredResourceDelegationConnector140",
    ends={
        Property(name="composition_av_AssemblyContext141", type=pcm_av_composition_av_RequiredResourceDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_composition_av_RequiredResourceDelegationConnector", type=composition_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
innerRequiredRole__RequiredResourceDelegationConnector142: BinaryAssociation = BinaryAssociation(
    name="innerRequiredRole__RequiredResourceDelegationConnector142",
    ends={
        Property(name="entity_av_ResourceRequiredRole144", type=pcm_av_composition_av_RequiredResourceDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_composition_av_RequiredResourceDelegationConnector143", type=entity_av_ResourceRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
outerRequiredRole__RequiredResourceDelegationConnector145: BinaryAssociation = BinaryAssociation(
    name="outerRequiredRole__RequiredResourceDelegationConnector145",
    ends={
        Property(name="entity_av_ResourceRequiredRole147", type=pcm_av_composition_av_RequiredResourceDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_composition_av_RequiredResourceDelegationConnector146", type=entity_av_ResourceRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
parentStructure__AssemblyContext148: BinaryAssociation = BinaryAssociation(
    name="parentStructure__AssemblyContext148",
    ends={
        Property(name="ComposedStructure149", type=pcm_av_composition_av_AssemblyContext, multiplicity=Multiplicity(1, 1)),
        Property(name="assemblyContexts__ComposedStructure", type=composition_av_ComposedStructure, multiplicity=Multiplicity(0, 1))
    }
)
encapsulatedComponent__AssemblyContext150: BinaryAssociation = BinaryAssociation(
    name="encapsulatedComponent__AssemblyContext150",
    ends={
        Property(name="RepositoryComponent", type=pcm_av_composition_av_AssemblyContext, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_composition_av_AssemblyContext", type=RepositoryComponent, multiplicity=Multiplicity(0, 1))
    }
)
providedRole_EntryLevelSystemCall165: BinaryAssociation = BinaryAssociation(
    name="providedRole_EntryLevelSystemCall165",
    ends={
        Property(name="pcm_av_usagemodel_av_EntryLevelSystemCall", type=OperationProvidedRole, multiplicity=Multiplicity(0, 1)),
        Property(name="OperationProvidedRole166", type=pcm_av_usagemodel_av_EntryLevelSystemCall, multiplicity=Multiplicity(1, 1))
    }
)
operationSignature__EntryLevelSystemCall167: BinaryAssociation = BinaryAssociation(
    name="operationSignature__EntryLevelSystemCall167",
    ends={
        Property(name="OperationSignature", type=pcm_av_usagemodel_av_EntryLevelSystemCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_usagemodel_av_EntryLevelSystemCall168", type=OperationSignature, multiplicity=Multiplicity(0, 1))
    }
)
outputParameterUsages_EntryLevelSystemCall169: BinaryAssociation = BinaryAssociation(
    name="outputParameterUsages_EntryLevelSystemCall169",
    ends={
        Property(name="VariableUsage170", type=pcm_av_usagemodel_av_EntryLevelSystemCall, multiplicity=Multiplicity(1, 1)),
        Property(name="entryLevelSystemCall_OutputParameterUsage", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
usageScenario_Workload152: BinaryAssociation = BinaryAssociation(
    name="usageScenario_Workload152",
    ends={
        Property(name="UsageScenario", type=pcm_av_usagemodel_av_Workload, multiplicity=Multiplicity(1, 1)),
        Property(name="workload_UsageScenario", type=UsageScenario, multiplicity=Multiplicity(0, 1))
    }
)
usageModel_UsageScenario153: BinaryAssociation = BinaryAssociation(
    name="usageModel_UsageScenario153",
    ends={
        Property(name="UsageModel", type=pcm_av_usagemodel_av_UsageScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="usageScenario_UsageModel", type=UsageModel, multiplicity=Multiplicity(0, 1))
    }
)
scenarioBehaviour_UsageScenario154: BinaryAssociation = BinaryAssociation(
    name="scenarioBehaviour_UsageScenario154",
    ends={
        Property(name="ScenarioBehaviour", type=pcm_av_usagemodel_av_UsageScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="usageScenario_SenarioBehaviour", type=ScenarioBehaviour, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
workload_UsageScenario155: BinaryAssociation = BinaryAssociation(
    name="workload_UsageScenario155",
    ends={
        Property(name="Workload", type=pcm_av_usagemodel_av_UsageScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="usageScenario_Workload", type=Workload, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assemblyContext_userData156: BinaryAssociation = BinaryAssociation(
    name="assemblyContext_userData156",
    ends={
        Property(name="composition_av_AssemblyContext157", type=pcm_av_usagemodel_av_UserData, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_usagemodel_av_UserData", type=composition_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
usageModel_UserData158: BinaryAssociation = BinaryAssociation(
    name="usageModel_UserData158",
    ends={
        Property(name="UsageModel159", type=pcm_av_usagemodel_av_UserData, multiplicity=Multiplicity(1, 1)),
        Property(name="userData_UsageModel", type=UsageModel, multiplicity=Multiplicity(0, 1))
    }
)
userDataParameterUsages_UserData160: BinaryAssociation = BinaryAssociation(
    name="userDataParameterUsages_UserData160",
    ends={
        Property(name="VariableUsage161", type=pcm_av_usagemodel_av_UserData, multiplicity=Multiplicity(1, 1)),
        Property(name="userData_VariableUsage", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
usageScenario_UsageModel162: BinaryAssociation = BinaryAssociation(
    name="usageScenario_UsageModel162",
    ends={
        Property(name="UsageScenario163", type=pcm_av_usagemodel_av_UsageModel, multiplicity=Multiplicity(1, 1)),
        Property(name="usageModel_UsageScenario", type=UsageScenario, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
userData_UsageModel164: BinaryAssociation = BinaryAssociation(
    name="userData_UsageModel164",
    ends={
        Property(name="UserData", type=pcm_av_usagemodel_av_UsageModel, multiplicity=Multiplicity(1, 1)),
        Property(name="usageModel_UserData", type=UserData, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputParameterUsages_EntryLevelSystemCall171: BinaryAssociation = BinaryAssociation(
    name="inputParameterUsages_EntryLevelSystemCall171",
    ends={
        Property(name="VariableUsage172", type=pcm_av_usagemodel_av_EntryLevelSystemCall, multiplicity=Multiplicity(1, 1)),
        Property(name="entryLevelSystemCall_InputParameterUsage", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
successor173: BinaryAssociation = BinaryAssociation(
    name="successor173",
    ends={
        Property(name="AbstractUserAction", type=pcm_av_usagemodel_av_AbstractUserAction, multiplicity=Multiplicity(1, 1)),
        Property(name="predecessor", type=AbstractUserAction, multiplicity=Multiplicity(0, 1))
    }
)
predecessor174: BinaryAssociation = BinaryAssociation(
    name="predecessor174",
    ends={
        Property(name="AbstractUserAction175", type=pcm_av_usagemodel_av_AbstractUserAction, multiplicity=Multiplicity(1, 1)),
        Property(name="successor", type=AbstractUserAction, multiplicity=Multiplicity(0, 1))
    }
)
scenarioBehaviour_AbstractUserAction176: BinaryAssociation = BinaryAssociation(
    name="scenarioBehaviour_AbstractUserAction176",
    ends={
        Property(name="ScenarioBehaviour177", type=pcm_av_usagemodel_av_AbstractUserAction, multiplicity=Multiplicity(1, 1)),
        Property(name="actions_ScenarioBehaviour", type=ScenarioBehaviour, multiplicity=Multiplicity(0, 1))
    }
)
usageScenario_SenarioBehaviour178: BinaryAssociation = BinaryAssociation(
    name="usageScenario_SenarioBehaviour178",
    ends={
        Property(name="UsageScenario179", type=pcm_av_usagemodel_av_ScenarioBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="scenarioBehaviour_UsageScenario", type=UsageScenario, multiplicity=Multiplicity(0, 1))
    }
)
branchTransition_ScenarioBehaviour180: BinaryAssociation = BinaryAssociation(
    name="branchTransition_ScenarioBehaviour180",
    ends={
        Property(name="BranchTransition", type=pcm_av_usagemodel_av_ScenarioBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="branchedBehaviour_BranchTransition", type=BranchTransition, multiplicity=Multiplicity(0, 1))
    }
)
loop_ScenarioBehaviour181: BinaryAssociation = BinaryAssociation(
    name="loop_ScenarioBehaviour181",
    ends={
        Property(name="Loop182", type=pcm_av_usagemodel_av_ScenarioBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="bodyBehaviour_Loop", type=Loop, multiplicity=Multiplicity(0, 1))
    }
)
actions_ScenarioBehaviour183: BinaryAssociation = BinaryAssociation(
    name="actions_ScenarioBehaviour183",
    ends={
        Property(name="AbstractUserAction184", type=pcm_av_usagemodel_av_ScenarioBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="scenarioBehaviour_AbstractUserAction", type=AbstractUserAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
branch_BranchTransition185: BinaryAssociation = BinaryAssociation(
    name="branch_BranchTransition185",
    ends={
        Property(name="Branch", type=pcm_av_usagemodel_av_BranchTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="branchTransitions_Branch", type=Branch, multiplicity=Multiplicity(0, 1))
    }
)
branchedBehaviour_BranchTransition186: BinaryAssociation = BinaryAssociation(
    name="branchedBehaviour_BranchTransition186",
    ends={
        Property(name="ScenarioBehaviour187", type=pcm_av_usagemodel_av_BranchTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="branchTransition_ScenarioBehaviour", type=ScenarioBehaviour, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
branchTransitions_Branch188: BinaryAssociation = BinaryAssociation(
    name="branchTransitions_Branch188",
    ends={
        Property(name="BranchTransition189", type=pcm_av_usagemodel_av_Branch, multiplicity=Multiplicity(1, 1)),
        Property(name="branch_BranchTransition", type=BranchTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
loopIteration_Loop190: BinaryAssociation = BinaryAssociation(
    name="loopIteration_Loop190",
    ends={
        Property(name="PCMRandomVariable191", type=pcm_av_usagemodel_av_Loop, multiplicity=Multiplicity(1, 1)),
        Property(name="loop_LoopIteration", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bodyBehaviour_Loop192: BinaryAssociation = BinaryAssociation(
    name="bodyBehaviour_Loop192",
    ends={
        Property(name="ScenarioBehaviour193", type=pcm_av_usagemodel_av_Loop, multiplicity=Multiplicity(1, 1)),
        Property(name="loop_ScenarioBehaviour", type=ScenarioBehaviour, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
interArrivalTime_OpenWorkload194: BinaryAssociation = BinaryAssociation(
    name="interArrivalTime_OpenWorkload194",
    ends={
        Property(name="PCMRandomVariable195", type=pcm_av_usagemodel_av_OpenWorkload, multiplicity=Multiplicity(1, 1)),
        Property(name="openWorkload_PCMRandomVariable", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
timeSpecification_Delay196: BinaryAssociation = BinaryAssociation(
    name="timeSpecification_Delay196",
    ends={
        Property(name="PCMRandomVariable197", type=pcm_av_usagemodel_av_Delay, multiplicity=Multiplicity(1, 1)),
        Property(name="delay_TimeSpecification", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thinkTime_ClosedWorkload198: BinaryAssociation = BinaryAssociation(
    name="thinkTime_ClosedWorkload198",
    ends={
        Property(name="PCMRandomVariable199", type=pcm_av_usagemodel_av_ClosedWorkload, multiplicity=Multiplicity(1, 1)),
        Property(name="closedWorkload_PCMRandomVariable", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
capacity_PassiveResource200: BinaryAssociation = BinaryAssociation(
    name="capacity_PassiveResource200",
    ends={
        Property(name="PCMRandomVariable201", type=pcm_av_repository_av_PassiveResource, multiplicity=Multiplicity(1, 1)),
        Property(name="passiveResource_capacity_PCMRandomVariable", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
basicComponent_PassiveResource202: BinaryAssociation = BinaryAssociation(
    name="basicComponent_PassiveResource202",
    ends={
        Property(name="BasicComponent", type=pcm_av_repository_av_PassiveResource, multiplicity=Multiplicity(1, 1)),
        Property(name="passiveResource_BasicComponent", type=BasicComponent, multiplicity=Multiplicity(0, 1))
    }
)
resourceTimeoutFailureType__PassiveResource203: BinaryAssociation = BinaryAssociation(
    name="resourceTimeoutFailureType__PassiveResource203",
    ends={
        Property(name="ResourceTimeoutFailureType", type=pcm_av_repository_av_PassiveResource, multiplicity=Multiplicity(1, 1)),
        Property(name="passiveResource__ResourceTimeoutFailureType", type=ResourceTimeoutFailureType, multiplicity=Multiplicity(0, 1))
    }
)
serviceEffectSpecifications__BasicComponent204: BinaryAssociation = BinaryAssociation(
    name="serviceEffectSpecifications__BasicComponent204",
    ends={
        Property(name="ServiceEffectSpecification", type=pcm_av_repository_av_BasicComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="basicComponent_ServiceEffectSpecification", type=ServiceEffectSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
passiveResource_BasicComponent205: BinaryAssociation = BinaryAssociation(
    name="passiveResource_BasicComponent205",
    ends={
        Property(name="PassiveResource206", type=pcm_av_repository_av_BasicComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="basicComponent_PassiveResource", type=PassiveResource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
infrastructureSignature__Parameter214: BinaryAssociation = BinaryAssociation(
    name="infrastructureSignature__Parameter214",
    ends={
        Property(name="InfrastructureSignature", type=pcm_av_repository_av_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameters__InfrastructureSignature", type=InfrastructureSignature, multiplicity=Multiplicity(0, 1))
    }
)
operationSignature__Parameter215: BinaryAssociation = BinaryAssociation(
    name="operationSignature__Parameter215",
    ends={
        Property(name="OperationSignature216", type=pcm_av_repository_av_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameters__OperationSignature", type=OperationSignature, multiplicity=Multiplicity(0, 1))
    }
)
parentCompleteComponentTypes207: BinaryAssociation = BinaryAssociation(
    name="parentCompleteComponentTypes207",
    ends={
        Property(name="CompleteComponentType", type=pcm_av_repository_av_ImplementationComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_repository_av_ImplementationComponentType", type=CompleteComponentType, multiplicity=Multiplicity(0, 9999))
    }
)
componentParameterUsage_ImplementationComponentType208: BinaryAssociation = BinaryAssociation(
    name="componentParameterUsage_ImplementationComponentType208",
    ends={
        Property(name="VariableUsage210", type=pcm_av_repository_av_ImplementationComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_repository_av_ImplementationComponentType209", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
repository__RepositoryComponent211: BinaryAssociation = BinaryAssociation(
    name="repository__RepositoryComponent211",
    ends={
        Property(name="Repository", type=pcm_av_repository_av_RepositoryComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="components__Repository", type=Repository, multiplicity=Multiplicity(0, 1))
    }
)
providingEntity_ProvidedRole212: BinaryAssociation = BinaryAssociation(
    name="providingEntity_ProvidedRole212",
    ends={
        Property(name="InterfaceProvidingEntity", type=pcm_av_repository_av_ProvidedRole, multiplicity=Multiplicity(1, 1)),
        Property(name="providedRoles_InterfaceProvidingEntity", type=entity_av_InterfaceProvidingEntity, multiplicity=Multiplicity(0, 1))
    }
)
dataType__Parameter213: BinaryAssociation = BinaryAssociation(
    name="dataType__Parameter213",
    ends={
        Property(name="DataType", type=pcm_av_repository_av_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_repository_av_Parameter", type=DataType, multiplicity=Multiplicity(0, 1))
    }
)
eventType__Parameter217: BinaryAssociation = BinaryAssociation(
    name="eventType__Parameter217",
    ends={
        Property(name="EventType", type=pcm_av_repository_av_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameter__EventType", type=EventType, multiplicity=Multiplicity(0, 1))
    }
)
resourceSignature__Parameter218: BinaryAssociation = BinaryAssociation(
    name="resourceSignature__Parameter218",
    ends={
        Property(name="ResourceSignature", type=pcm_av_repository_av_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameter__ResourceSignature", type=ResourceSignature, multiplicity=Multiplicity(0, 1))
    }
)
repository__DataType219: BinaryAssociation = BinaryAssociation(
    name="repository__DataType219",
    ends={
        Property(name="Repository220", type=pcm_av_repository_av_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="dataTypes__Repository", type=Repository, multiplicity=Multiplicity(0, 1))
    }
)
components__Repository221: BinaryAssociation = BinaryAssociation(
    name="components__Repository221",
    ends={
        Property(name="RepositoryComponent222", type=pcm_av_repository_av_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="repository__RepositoryComponent", type=RepositoryComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
interfaces__Repository223: BinaryAssociation = BinaryAssociation(
    name="interfaces__Repository223",
    ends={
        Property(name="Interface", type=pcm_av_repository_av_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="repository__Interface", type=Interface, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
failureTypes__Repository224: BinaryAssociation = BinaryAssociation(
    name="failureTypes__Repository224",
    ends={
        Property(name="FailureType", type=pcm_av_repository_av_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="repository__FailureType", type=FailureType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataTypes__Repository225: BinaryAssociation = BinaryAssociation(
    name="dataTypes__Repository225",
    ends={
        Property(name="DataType226", type=pcm_av_repository_av_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="repository__DataType", type=DataType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters__InfrastructureSignature247: BinaryAssociation = BinaryAssociation(
    name="parameters__InfrastructureSignature247",
    ends={
        Property(name="Parameter248", type=pcm_av_repository_av_InfrastructureSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="infrastructureSignature__Parameter", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentInterfaces__Interface227: BinaryAssociation = BinaryAssociation(
    name="parentInterfaces__Interface227",
    ends={
        Property(name="Interface228", type=pcm_av_repository_av_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_repository_av_Interface", type=Interface, multiplicity=Multiplicity(0, 9999))
    }
)
protocols__Interface229: BinaryAssociation = BinaryAssociation(
    name="protocols__Interface229",
    ends={
        Property(name="Protocol", type=pcm_av_repository_av_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_repository_av_Interface230", type=Protocol, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredCharacterisations231: BinaryAssociation = BinaryAssociation(
    name="requiredCharacterisations231",
    ends={
        Property(name="RequiredCharacterisation", type=pcm_av_repository_av_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="interface_RequiredCharacterisation", type=RequiredCharacterisation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
repository__Interface232: BinaryAssociation = BinaryAssociation(
    name="repository__Interface232",
    ends={
        Property(name="Repository233", type=pcm_av_repository_av_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="interfaces__Repository", type=Repository, multiplicity=Multiplicity(0, 1))
    }
)
parameter234: BinaryAssociation = BinaryAssociation(
    name="parameter234",
    ends={
        Property(name="Parameter", type=pcm_av_repository_av_RequiredCharacterisation, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_repository_av_RequiredCharacterisation", type=Parameter_, multiplicity=Multiplicity(0, 1))
    }
)
interface_RequiredCharacterisation235: BinaryAssociation = BinaryAssociation(
    name="interface_RequiredCharacterisation235",
    ends={
        Property(name="Interface236", type=pcm_av_repository_av_RequiredCharacterisation, multiplicity=Multiplicity(1, 1)),
        Property(name="requiredCharacterisations", type=Interface, multiplicity=Multiplicity(0, 1))
    }
)
eventTypes__EventGroup237: BinaryAssociation = BinaryAssociation(
    name="eventTypes__EventGroup237",
    ends={
        Property(name="EventType238", type=pcm_av_repository_av_EventGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="eventGroup__EventType", type=EventType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameter__EventType239: BinaryAssociation = BinaryAssociation(
    name="parameter__EventType239",
    ends={
        Property(name="Parameter240", type=pcm_av_repository_av_EventType, multiplicity=Multiplicity(1, 1)),
        Property(name="eventType__Parameter", type=Parameter_, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eventGroup__EventType241: BinaryAssociation = BinaryAssociation(
    name="eventGroup__EventType241",
    ends={
        Property(name="EventGroup242", type=pcm_av_repository_av_EventType, multiplicity=Multiplicity(1, 1)),
        Property(name="eventTypes__EventGroup", type=EventGroup, multiplicity=Multiplicity(0, 1))
    }
)
exceptions__Signature243: BinaryAssociation = BinaryAssociation(
    name="exceptions__Signature243",
    ends={
        Property(name="ExceptionType", type=pcm_av_repository_av_Signature, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_repository_av_Signature", type=ExceptionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
failureType244: BinaryAssociation = BinaryAssociation(
    name="failureType244",
    ends={
        Property(name="FailureType246", type=pcm_av_repository_av_Signature, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_repository_av_Signature245", type=FailureType, multiplicity=Multiplicity(0, 9999))
    }
)
signatures__OperationInterface260: BinaryAssociation = BinaryAssociation(
    name="signatures__OperationInterface260",
    ends={
        Property(name="OperationSignature261", type=pcm_av_repository_av_OperationInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="interface__OperationSignature", type=OperationSignature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
infrastructureInterface__InfrastructureSignature249: BinaryAssociation = BinaryAssociation(
    name="infrastructureInterface__InfrastructureSignature249",
    ends={
        Property(name="InfrastructureInterface", type=pcm_av_repository_av_InfrastructureSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="infrastructureSignatures__InfrastructureInterface", type=InfrastructureInterface, multiplicity=Multiplicity(0, 1))
    }
)
infrastructureSignatures__InfrastructureInterface250: BinaryAssociation = BinaryAssociation(
    name="infrastructureSignatures__InfrastructureInterface250",
    ends={
        Property(name="InfrastructureSignature251", type=pcm_av_repository_av_InfrastructureInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="infrastructureInterface__InfrastructureSignature", type=InfrastructureSignature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredInterface__InfrastructureRequiredRole252: BinaryAssociation = BinaryAssociation(
    name="requiredInterface__InfrastructureRequiredRole252",
    ends={
        Property(name="InfrastructureInterface253", type=pcm_av_repository_av_InfrastructureRequiredRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_repository_av_InfrastructureRequiredRole", type=InfrastructureInterface, multiplicity=Multiplicity(0, 1))
    }
)
requiringEntity_RequiredRole254: BinaryAssociation = BinaryAssociation(
    name="requiringEntity_RequiredRole254",
    ends={
        Property(name="InterfaceRequiringEntity", type=pcm_av_repository_av_RequiredRole, multiplicity=Multiplicity(1, 1)),
        Property(name="requiredRoles_InterfaceRequiringEntity", type=entity_av_InterfaceRequiringEntity, multiplicity=Multiplicity(0, 1))
    }
)
interface__OperationSignature255: BinaryAssociation = BinaryAssociation(
    name="interface__OperationSignature255",
    ends={
        Property(name="OperationInterface", type=pcm_av_repository_av_OperationSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="signatures__OperationInterface", type=OperationInterface, multiplicity=Multiplicity(0, 1))
    }
)
parameters__OperationSignature256: BinaryAssociation = BinaryAssociation(
    name="parameters__OperationSignature256",
    ends={
        Property(name="Parameter257", type=pcm_av_repository_av_OperationSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="operationSignature__Parameter", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnType__OperationSignature258: BinaryAssociation = BinaryAssociation(
    name="returnType__OperationSignature258",
    ends={
        Property(name="DataType259", type=pcm_av_repository_av_OperationSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_repository_av_OperationSignature", type=DataType, multiplicity=Multiplicity(0, 1))
    }
)
parentProvidesComponentTypes272: BinaryAssociation = BinaryAssociation(
    name="parentProvidesComponentTypes272",
    ends={
        Property(name="ProvidesComponentType", type=pcm_av_repository_av_CompleteComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_repository_av_CompleteComponentType", type=ProvidesComponentType, multiplicity=Multiplicity(0, 9999))
    }
)
requiredInterface__OperationRequiredRole262: BinaryAssociation = BinaryAssociation(
    name="requiredInterface__OperationRequiredRole262",
    ends={
        Property(name="OperationInterface263", type=pcm_av_repository_av_OperationRequiredRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_repository_av_OperationRequiredRole", type=OperationInterface, multiplicity=Multiplicity(0, 1))
    }
)
eventGroup__SourceRole264: BinaryAssociation = BinaryAssociation(
    name="eventGroup__SourceRole264",
    ends={
        Property(name="EventGroup265", type=pcm_av_repository_av_SourceRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_repository_av_SourceRole", type=EventGroup, multiplicity=Multiplicity(0, 1))
    }
)
eventGroup__SinkRole266: BinaryAssociation = BinaryAssociation(
    name="eventGroup__SinkRole266",
    ends={
        Property(name="EventGroup267", type=pcm_av_repository_av_SinkRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_repository_av_SinkRole", type=EventGroup, multiplicity=Multiplicity(0, 1))
    }
)
providedInterface__OperationProvidedRole268: BinaryAssociation = BinaryAssociation(
    name="providedInterface__OperationProvidedRole268",
    ends={
        Property(name="OperationInterface269", type=pcm_av_repository_av_OperationProvidedRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_repository_av_OperationProvidedRole", type=OperationInterface, multiplicity=Multiplicity(0, 1))
    }
)
providedInterface__InfrastructureProvidedRole270: BinaryAssociation = BinaryAssociation(
    name="providedInterface__InfrastructureProvidedRole270",
    ends={
        Property(name="InfrastructureInterface271", type=pcm_av_repository_av_InfrastructureProvidedRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_repository_av_InfrastructureProvidedRole", type=InfrastructureInterface, multiplicity=Multiplicity(0, 1))
    }
)
parameter__ResourceSignature281: BinaryAssociation = BinaryAssociation(
    name="parameter__ResourceSignature281",
    ends={
        Property(name="Parameter282", type=pcm_av_resourcetype_av_ResourceSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceSignature__Parameter", type=Parameter_, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
innerType_CollectionDataType273: BinaryAssociation = BinaryAssociation(
    name="innerType_CollectionDataType273",
    ends={
        Property(name="DataType274", type=pcm_av_repository_av_CollectionDataType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_repository_av_CollectionDataType", type=DataType, multiplicity=Multiplicity(0, 1))
    }
)
parentType_CompositeDataType275: BinaryAssociation = BinaryAssociation(
    name="parentType_CompositeDataType275",
    ends={
        Property(name="CompositeDataType", type=pcm_av_repository_av_CompositeDataType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_repository_av_CompositeDataType", type=CompositeDataType, multiplicity=Multiplicity(0, 9999))
    }
)
innerDeclaration_CompositeDataType276: BinaryAssociation = BinaryAssociation(
    name="innerDeclaration_CompositeDataType276",
    ends={
        Property(name="InnerDeclaration", type=pcm_av_repository_av_CompositeDataType, multiplicity=Multiplicity(1, 1)),
        Property(name="compositeDataType_InnerDeclaration", type=InnerDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
datatype_InnerDeclaration277: BinaryAssociation = BinaryAssociation(
    name="datatype_InnerDeclaration277",
    ends={
        Property(name="DataType278", type=pcm_av_repository_av_InnerDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_repository_av_InnerDeclaration", type=DataType, multiplicity=Multiplicity(0, 1))
    }
)
compositeDataType_InnerDeclaration279: BinaryAssociation = BinaryAssociation(
    name="compositeDataType_InnerDeclaration279",
    ends={
        Property(name="CompositeDataType280", type=pcm_av_repository_av_InnerDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="innerDeclaration_CompositeDataType", type=CompositeDataType, multiplicity=Multiplicity(0, 1))
    }
)
resourceSignatures__ResourceInterface296: BinaryAssociation = BinaryAssociation(
    name="resourceSignatures__ResourceInterface296",
    ends={
        Property(name="ResourceSignature297", type=pcm_av_resourcetype_av_ResourceInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceInterface__ResourceSignature", type=ResourceSignature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceInterface__ResourceSignature283: BinaryAssociation = BinaryAssociation(
    name="resourceInterface__ResourceSignature283",
    ends={
        Property(name="ResourceInterface284", type=pcm_av_resourcetype_av_ResourceSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceSignatures__ResourceInterface", type=ResourceInterface, multiplicity=Multiplicity(0, 1))
    }
)
hardwareInducedFailureType__ProcessingResourceType285: BinaryAssociation = BinaryAssociation(
    name="hardwareInducedFailureType__ProcessingResourceType285",
    ends={
        Property(name="HardwareInducedFailureType", type=pcm_av_resourcetype_av_ProcessingResourceType, multiplicity=Multiplicity(1, 1)),
        Property(name="processingResourceType__HardwareInducedFailureType", type=HardwareInducedFailureType, multiplicity=Multiplicity(0, 1))
    }
)
resourceRepository_ResourceType286: BinaryAssociation = BinaryAssociation(
    name="resourceRepository_ResourceType286",
    ends={
        Property(name="ResourceRepository", type=pcm_av_resourcetype_av_ResourceType, multiplicity=Multiplicity(1, 1)),
        Property(name="availableResourceTypes_ResourceRepository", type=ResourceRepository, multiplicity=Multiplicity(0, 1))
    }
)
resourceInterfaces__ResourceRepository287: BinaryAssociation = BinaryAssociation(
    name="resourceInterfaces__ResourceRepository287",
    ends={
        Property(name="ResourceInterface288", type=pcm_av_resourcetype_av_ResourceRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceRepository__ResourceInterface", type=ResourceInterface, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
schedulingPolicies__ResourceRepository289: BinaryAssociation = BinaryAssociation(
    name="schedulingPolicies__ResourceRepository289",
    ends={
        Property(name="SchedulingPolicy", type=pcm_av_resourcetype_av_ResourceRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceRepository__SchedulingPolicy", type=SchedulingPolicy, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
availableResourceTypes_ResourceRepository290: BinaryAssociation = BinaryAssociation(
    name="availableResourceTypes_ResourceRepository290",
    ends={
        Property(name="ResourceType", type=pcm_av_resourcetype_av_ResourceRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceRepository_ResourceType", type=ResourceType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceRepository__SchedulingPolicy291: BinaryAssociation = BinaryAssociation(
    name="resourceRepository__SchedulingPolicy291",
    ends={
        Property(name="ResourceRepository292", type=pcm_av_resourcetype_av_SchedulingPolicy, multiplicity=Multiplicity(1, 1)),
        Property(name="schedulingPolicies__ResourceRepository", type=ResourceRepository, multiplicity=Multiplicity(0, 1))
    }
)
networkInducedFailureType__CommunicationLinkResourceType293: BinaryAssociation = BinaryAssociation(
    name="networkInducedFailureType__CommunicationLinkResourceType293",
    ends={
        Property(name="NetworkInducedFailureType", type=pcm_av_resourcetype_av_CommunicationLinkResourceType, multiplicity=Multiplicity(1, 1)),
        Property(name="communicationLinkResourceType__NetworkInducedFailureType", type=NetworkInducedFailureType, multiplicity=Multiplicity(0, 1))
    }
)
resourceRepository__ResourceInterface294: BinaryAssociation = BinaryAssociation(
    name="resourceRepository__ResourceInterface294",
    ends={
        Property(name="ResourceRepository295", type=pcm_av_resourcetype_av_ResourceInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceInterfaces__ResourceRepository", type=ResourceRepository, multiplicity=Multiplicity(0, 1))
    }
)
assemblyContext__VariableUsage307: BinaryAssociation = BinaryAssociation(
    name="assemblyContext__VariableUsage307",
    ends={
        Property(name="AssemblyContext308", type=pcm_av_parameter_av_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="configParameterUsages__AssemblyContext", type=composition_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
variableCharacterisation_VariableUsage298: BinaryAssociation = BinaryAssociation(
    name="variableCharacterisation_VariableUsage298",
    ends={
        Property(name="VariableCharacterisation299", type=pcm_av_parameter_av_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="variableUsage_VariableCharacterisation", type=VariableCharacterisation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
userData_VariableUsage300: BinaryAssociation = BinaryAssociation(
    name="userData_VariableUsage300",
    ends={
        Property(name="UserData301", type=pcm_av_parameter_av_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="userDataParameterUsages_UserData", type=UserData, multiplicity=Multiplicity(0, 1))
    }
)
callAction__VariableUsage302: BinaryAssociation = BinaryAssociation(
    name="callAction__VariableUsage302",
    ends={
        Property(name="CallAction", type=pcm_av_parameter_av_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="inputVariableUsages__CallAction", type=CallAction, multiplicity=Multiplicity(0, 1))
    }
)
synchronisationPoint_VariableUsage303: BinaryAssociation = BinaryAssociation(
    name="synchronisationPoint_VariableUsage303",
    ends={
        Property(name="SynchronisationPoint", type=pcm_av_parameter_av_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="outputParameterUsage_SynchronisationPoint", type=SynchronisationPoint, multiplicity=Multiplicity(0, 1))
    }
)
callReturnAction__VariableUsage304: BinaryAssociation = BinaryAssociation(
    name="callReturnAction__VariableUsage304",
    ends={
        Property(name="CallReturnAction", type=pcm_av_parameter_av_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="returnVariableUsage__CallReturnAction", type=CallReturnAction, multiplicity=Multiplicity(0, 1))
    }
)
setVariableAction_VariableUsage305: BinaryAssociation = BinaryAssociation(
    name="setVariableAction_VariableUsage305",
    ends={
        Property(name="SetVariableAction", type=pcm_av_parameter_av_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="localVariableUsages_SetVariableAction", type=SetVariableAction, multiplicity=Multiplicity(0, 1))
    }
)
specifiedOutputParameterAbstraction_expectedExternalOutputs_VariableUsage306: BinaryAssociation = BinaryAssociation(
    name="specifiedOutputParameterAbstraction_expectedExternalOutputs_VariableUsage306",
    ends={
        Property(name="SpecifiedOutputParameterAbstraction", type=pcm_av_parameter_av_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="expectedExternalOutputs_SpecifiedOutputParameterAbstraction", type=SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(0, 1))
    }
)
entryLevelSystemCall_InputParameterUsage309: BinaryAssociation = BinaryAssociation(
    name="entryLevelSystemCall_InputParameterUsage309",
    ends={
        Property(name="EntryLevelSystemCall", type=pcm_av_parameter_av_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="inputParameterUsages_EntryLevelSystemCall", type=EntryLevelSystemCall, multiplicity=Multiplicity(0, 1))
    }
)
entryLevelSystemCall_OutputParameterUsage310: BinaryAssociation = BinaryAssociation(
    name="entryLevelSystemCall_OutputParameterUsage310",
    ends={
        Property(name="EntryLevelSystemCall311", type=pcm_av_parameter_av_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="outputParameterUsages_EntryLevelSystemCall", type=EntryLevelSystemCall, multiplicity=Multiplicity(0, 1))
    }
)
namedReference__VariableUsage312: BinaryAssociation = BinaryAssociation(
    name="namedReference__VariableUsage312",
    ends={
        Property(name="parameter_av_pcm_av_AbstractNamedReference", type=pcm_av_parameter_av_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_parameter_av_VariableUsage", type=parameter_av_pcm_av_AbstractNamedReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
specification_VariableCharacterisation313: BinaryAssociation = BinaryAssociation(
    name="specification_VariableCharacterisation313",
    ends={
        Property(name="PCMRandomVariable314", type=pcm_av_parameter_av_VariableCharacterisation, multiplicity=Multiplicity(1, 1)),
        Property(name="variableCharacterisation_Specification", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variableUsage_VariableCharacterisation315: BinaryAssociation = BinaryAssociation(
    name="variableUsage_VariableCharacterisation315",
    ends={
        Property(name="VariableUsage316", type=pcm_av_parameter_av_VariableCharacterisation, multiplicity=Multiplicity(1, 1)),
        Property(name="variableCharacterisation_VariableUsage", type=VariableUsage, multiplicity=Multiplicity(0, 1))
    }
)
processingResourceType__HardwareInducedFailureType317: BinaryAssociation = BinaryAssociation(
    name="processingResourceType__HardwareInducedFailureType317",
    ends={
        Property(name="ProcessingResourceType", type=pcm_av_reliability_av_HardwareInducedFailureType, multiplicity=Multiplicity(1, 1)),
        Property(name="hardwareInducedFailureType__ProcessingResourceType", type=ProcessingResourceType, multiplicity=Multiplicity(0, 1))
    }
)
internalFailureOccurrenceDescriptions__SoftwareInducedFailureType318: BinaryAssociation = BinaryAssociation(
    name="internalFailureOccurrenceDescriptions__SoftwareInducedFailureType318",
    ends={
        Property(name="InternalFailureOccurrenceDescription", type=pcm_av_reliability_av_SoftwareInducedFailureType, multiplicity=Multiplicity(1, 1)),
        Property(name="softwareInducedFailureType__InternalFailureOccurrenceDescription", type=InternalFailureOccurrenceDescription, multiplicity=Multiplicity(0, 9999))
    }
)
internalAction__InternalFailureOccurrenceDescription319: BinaryAssociation = BinaryAssociation(
    name="internalAction__InternalFailureOccurrenceDescription319",
    ends={
        Property(name="InternalAction", type=pcm_av_reliability_av_InternalFailureOccurrenceDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="internalFailureOccurrenceDescriptions__InternalAction", type=InternalAction, multiplicity=Multiplicity(0, 1))
    }
)
softwareInducedFailureType__InternalFailureOccurrenceDescription320: BinaryAssociation = BinaryAssociation(
    name="softwareInducedFailureType__InternalFailureOccurrenceDescription320",
    ends={
        Property(name="SoftwareInducedFailureType", type=pcm_av_reliability_av_InternalFailureOccurrenceDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="internalFailureOccurrenceDescriptions__SoftwareInducedFailureType", type=SoftwareInducedFailureType, multiplicity=Multiplicity(0, 1))
    }
)
resourceCall__Action333: BinaryAssociation = BinaryAssociation(
    name="resourceCall__Action333",
    ends={
        Property(name="ResourceCall334", type=pcm_av_seff_av_AbstractInternalControlFlowAction, multiplicity=Multiplicity(1, 1)),
        Property(name="action__ResourceCall", type=seff_performance_av_ResourceCall, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
predecessor_AbstractAction335: BinaryAssociation = BinaryAssociation(
    name="predecessor_AbstractAction335",
    ends={
        Property(name="AbstractAction", type=pcm_av_seff_av_AbstractAction, multiplicity=Multiplicity(1, 1)),
        Property(name="successor_AbstractAction", type=AbstractAction, multiplicity=Multiplicity(0, 1))
    }
)
communicationLinkResourceType__NetworkInducedFailureType321: BinaryAssociation = BinaryAssociation(
    name="communicationLinkResourceType__NetworkInducedFailureType321",
    ends={
        Property(name="CommunicationLinkResourceType", type=pcm_av_reliability_av_NetworkInducedFailureType, multiplicity=Multiplicity(1, 1)),
        Property(name="networkInducedFailureType__CommunicationLinkResourceType", type=CommunicationLinkResourceType, multiplicity=Multiplicity(0, 1))
    }
)
specifiedReliabilityAnnotation__ExternalFailureOccurrenceDescription322: BinaryAssociation = BinaryAssociation(
    name="specifiedReliabilityAnnotation__ExternalFailureOccurrenceDescription322",
    ends={
        Property(name="SpecifiedReliabilityAnnotation", type=pcm_av_reliability_av_ExternalFailureOccurrenceDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="externalFailureOccurrenceDescriptions__SpecifiedReliabilityAnnotation", type=qos_reliability_av_SpecifiedReliabilityAnnotation, multiplicity=Multiplicity(0, 1))
    }
)
failureType__ExternalFailureOccurrenceDescription323: BinaryAssociation = BinaryAssociation(
    name="failureType__ExternalFailureOccurrenceDescription323",
    ends={
        Property(name="FailureType324", type=pcm_av_reliability_av_ExternalFailureOccurrenceDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_reliability_av_ExternalFailureOccurrenceDescription", type=FailureType, multiplicity=Multiplicity(0, 1))
    }
)
passiveResource__ResourceTimeoutFailureType325: BinaryAssociation = BinaryAssociation(
    name="passiveResource__ResourceTimeoutFailureType325",
    ends={
        Property(name="PassiveResource326", type=pcm_av_reliability_av_ResourceTimeoutFailureType, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceTimeoutFailureType__PassiveResource", type=PassiveResource, multiplicity=Multiplicity(0, 1))
    }
)
repository__FailureType327: BinaryAssociation = BinaryAssociation(
    name="repository__FailureType327",
    ends={
        Property(name="Repository328", type=pcm_av_reliability_av_FailureType, multiplicity=Multiplicity(1, 1)),
        Property(name="failureTypes__Repository", type=Repository, multiplicity=Multiplicity(0, 1))
    }
)
resourceDemand_Action329: BinaryAssociation = BinaryAssociation(
    name="resourceDemand_Action329",
    ends={
        Property(name="ParametricResourceDemand330", type=pcm_av_seff_av_AbstractInternalControlFlowAction, multiplicity=Multiplicity(1, 1)),
        Property(name="action_ParametricResourceDemand", type=seff_performance_av_ParametricResourceDemand, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
infrastructureCall__Action331: BinaryAssociation = BinaryAssociation(
    name="infrastructureCall__Action331",
    ends={
        Property(name="InfrastructureCall332", type=pcm_av_seff_av_AbstractInternalControlFlowAction, multiplicity=Multiplicity(1, 1)),
        Property(name="action__InfrastructureCall", type=seff_performance_av_InfrastructureCall, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bodyBehaviour_Loop344: BinaryAssociation = BinaryAssociation(
    name="bodyBehaviour_Loop344",
    ends={
        Property(name="ResourceDemandingBehaviour345", type=pcm_av_seff_av_AbstractLoopAction, multiplicity=Multiplicity(1, 1)),
        Property(name="abstractLoopAction_ResourceDemandingBehaviour", type=ResourceDemandingBehaviour, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
branchAction_AbstractBranchTransition346: BinaryAssociation = BinaryAssociation(
    name="branchAction_AbstractBranchTransition346",
    ends={
        Property(name="BranchAction", type=pcm_av_seff_av_AbstractBranchTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="branches_Branch", type=BranchAction, multiplicity=Multiplicity(0, 1))
    }
)
branchBehaviour_BranchTransition347: BinaryAssociation = BinaryAssociation(
    name="branchBehaviour_BranchTransition347",
    ends={
        Property(name="ResourceDemandingBehaviour348", type=pcm_av_seff_av_AbstractBranchTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="abstractBranchTransition_ResourceDemandingBehaviour", type=ResourceDemandingBehaviour, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
successor_AbstractAction336: BinaryAssociation = BinaryAssociation(
    name="successor_AbstractAction336",
    ends={
        Property(name="AbstractAction337", type=pcm_av_seff_av_AbstractAction, multiplicity=Multiplicity(1, 1)),
        Property(name="predecessor_AbstractAction", type=AbstractAction, multiplicity=Multiplicity(0, 1))
    }
)
resourceDemandingBehaviour_AbstractAction338: BinaryAssociation = BinaryAssociation(
    name="resourceDemandingBehaviour_AbstractAction338",
    ends={
        Property(name="ResourceDemandingBehaviour", type=pcm_av_seff_av_AbstractAction, multiplicity=Multiplicity(1, 1)),
        Property(name="steps_Behaviour", type=ResourceDemandingBehaviour, multiplicity=Multiplicity(0, 1))
    }
)
abstractLoopAction_ResourceDemandingBehaviour339: BinaryAssociation = BinaryAssociation(
    name="abstractLoopAction_ResourceDemandingBehaviour339",
    ends={
        Property(name="AbstractLoopAction", type=pcm_av_seff_av_ResourceDemandingBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="bodyBehaviour_Loop340", type=AbstractLoopAction, multiplicity=Multiplicity(0, 1))
    }
)
abstractBranchTransition_ResourceDemandingBehaviour341: BinaryAssociation = BinaryAssociation(
    name="abstractBranchTransition_ResourceDemandingBehaviour341",
    ends={
        Property(name="AbstractBranchTransition", type=pcm_av_seff_av_ResourceDemandingBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="branchBehaviour_BranchTransition", type=AbstractBranchTransition, multiplicity=Multiplicity(0, 1))
    }
)
steps_Behaviour342: BinaryAssociation = BinaryAssociation(
    name="steps_Behaviour342",
    ends={
        Property(name="AbstractAction343", type=pcm_av_seff_av_ResourceDemandingBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceDemandingBehaviour_AbstractAction", type=AbstractAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
describedService__SEFF353: BinaryAssociation = BinaryAssociation(
    name="describedService__SEFF353",
    ends={
        Property(name="Signature", type=pcm_av_seff_av_ServiceEffectSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_seff_av_ServiceEffectSpecification", type=Signature, multiplicity=Multiplicity(0, 1))
    }
)
basicComponent_ServiceEffectSpecification354: BinaryAssociation = BinaryAssociation(
    name="basicComponent_ServiceEffectSpecification354",
    ends={
        Property(name="BasicComponent355", type=pcm_av_seff_av_ServiceEffectSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="serviceEffectSpecifications__BasicComponent", type=BasicComponent, multiplicity=Multiplicity(0, 1))
    }
)
branches_Branch349: BinaryAssociation = BinaryAssociation(
    name="branches_Branch349",
    ends={
        Property(name="AbstractBranchTransition350", type=pcm_av_seff_av_BranchAction, multiplicity=Multiplicity(1, 1)),
        Property(name="branchAction_AbstractBranchTransition", type=AbstractBranchTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputVariableUsages__CallAction351: BinaryAssociation = BinaryAssociation(
    name="inputVariableUsages__CallAction351",
    ends={
        Property(name="VariableUsage352", type=pcm_av_seff_av_CallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="callAction__VariableUsage", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputParameterUsage_SynchronisationPoint368: BinaryAssociation = BinaryAssociation(
    name="outputParameterUsage_SynchronisationPoint368",
    ends={
        Property(name="VariableUsage369", type=pcm_av_seff_av_SynchronisationPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="synchronisationPoint_VariableUsage", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
forkAction_SynchronisationPoint370: BinaryAssociation = BinaryAssociation(
    name="forkAction_SynchronisationPoint370",
    ends={
        Property(name="ForkAction371", type=pcm_av_seff_av_SynchronisationPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="synchronisingBehaviours_ForkAction", type=ForkAction, multiplicity=Multiplicity(0, 1))
    }
)
synchronousForkedBehaviours_SynchronisationPoint372: BinaryAssociation = BinaryAssociation(
    name="synchronousForkedBehaviours_SynchronisationPoint372",
    ends={
        Property(name="ForkedBehaviour373", type=pcm_av_seff_av_SynchronisationPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="synchronisationPoint_ForkedBehaviour", type=ForkedBehaviour, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceDemandingInternalBehaviours356: BinaryAssociation = BinaryAssociation(
    name="resourceDemandingInternalBehaviours356",
    ends={
        Property(name="ResourceDemandingInternalBehaviour", type=pcm_av_seff_av_ResourceDemandingSEFF, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceDemandingSEFF_ResourceDemandingInternalBehaviour", type=ResourceDemandingInternalBehaviour, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceDemandingSEFF_ResourceDemandingInternalBehaviour357: BinaryAssociation = BinaryAssociation(
    name="resourceDemandingSEFF_ResourceDemandingInternalBehaviour357",
    ends={
        Property(name="ResourceDemandingSEFF", type=pcm_av_seff_av_ResourceDemandingInternalBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceDemandingInternalBehaviours", type=ResourceDemandingSEFF, multiplicity=Multiplicity(0, 1))
    }
)
passiveResource_ReleaseAction358: BinaryAssociation = BinaryAssociation(
    name="passiveResource_ReleaseAction358",
    ends={
        Property(name="PassiveResource359", type=pcm_av_seff_av_ReleaseAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_seff_av_ReleaseAction", type=PassiveResource, multiplicity=Multiplicity(0, 1))
    }
)
iterationCount_LoopAction360: BinaryAssociation = BinaryAssociation(
    name="iterationCount_LoopAction360",
    ends={
        Property(name="PCMRandomVariable361", type=pcm_av_seff_av_LoopAction, multiplicity=Multiplicity(1, 1)),
        Property(name="loopAction_PCMRandomVariable", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
asynchronousForkedBehaviours_ForkAction362: BinaryAssociation = BinaryAssociation(
    name="asynchronousForkedBehaviours_ForkAction362",
    ends={
        Property(name="ForkedBehaviour", type=pcm_av_seff_av_ForkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="forkAction_ForkedBehaivour", type=ForkedBehaviour, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
synchronisingBehaviours_ForkAction363: BinaryAssociation = BinaryAssociation(
    name="synchronisingBehaviours_ForkAction363",
    ends={
        Property(name="SynchronisationPoint364", type=pcm_av_seff_av_ForkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="forkAction_SynchronisationPoint", type=SynchronisationPoint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
synchronisationPoint_ForkedBehaviour365: BinaryAssociation = BinaryAssociation(
    name="synchronisationPoint_ForkedBehaviour365",
    ends={
        Property(name="SynchronisationPoint366", type=pcm_av_seff_av_ForkedBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="synchronousForkedBehaviours_SynchronisationPoint", type=SynchronisationPoint, multiplicity=Multiplicity(0, 1))
    }
)
forkAction_ForkedBehaivour367: BinaryAssociation = BinaryAssociation(
    name="forkAction_ForkedBehaivour367",
    ends={
        Property(name="ForkAction", type=pcm_av_seff_av_ForkedBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="asynchronousForkedBehaviours_ForkAction", type=ForkAction, multiplicity=Multiplicity(0, 1))
    }
)
calledService_ExternalService374: BinaryAssociation = BinaryAssociation(
    name="calledService_ExternalService374",
    ends={
        Property(name="OperationSignature375", type=pcm_av_seff_av_ExternalCallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_seff_av_ExternalCallAction", type=OperationSignature, multiplicity=Multiplicity(0, 1))
    }
)
role_ExternalService376: BinaryAssociation = BinaryAssociation(
    name="role_ExternalService376",
    ends={
        Property(name="OperationRequiredRole378", type=pcm_av_seff_av_ExternalCallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_seff_av_ExternalCallAction377", type=OperationRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
passiveresource_AcquireAction381: BinaryAssociation = BinaryAssociation(
    name="passiveresource_AcquireAction381",
    ends={
        Property(name="PassiveResource382", type=pcm_av_seff_av_AcquireAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_seff_av_AcquireAction", type=PassiveResource, multiplicity=Multiplicity(0, 1))
    }
)
returnVariableUsage__CallReturnAction379: BinaryAssociation = BinaryAssociation(
    name="returnVariableUsage__CallReturnAction379",
    ends={
        Property(name="VariableUsage380", type=pcm_av_seff_av_CallReturnAction, multiplicity=Multiplicity(1, 1)),
        Property(name="callReturnAction__VariableUsage", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameter_CollectionIteratorAction383: BinaryAssociation = BinaryAssociation(
    name="parameter_CollectionIteratorAction383",
    ends={
        Property(name="Parameter384", type=pcm_av_seff_av_CollectionIteratorAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_seff_av_CollectionIteratorAction", type=Parameter_, multiplicity=Multiplicity(0, 1))
    }
)
branchCondition_GuardedBranchTransition385: BinaryAssociation = BinaryAssociation(
    name="branchCondition_GuardedBranchTransition385",
    ends={
        Property(name="PCMRandomVariable386", type=pcm_av_seff_av_GuardedBranchTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="guardedBranchTransition_PCMRandomVariable", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
localVariableUsages_SetVariableAction387: BinaryAssociation = BinaryAssociation(
    name="localVariableUsages_SetVariableAction387",
    ends={
        Property(name="VariableUsage388", type=pcm_av_seff_av_SetVariableAction, multiplicity=Multiplicity(1, 1)),
        Property(name="setVariableAction_VariableUsage", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
calledResourceDemandingInternalBehaviour389: BinaryAssociation = BinaryAssociation(
    name="calledResourceDemandingInternalBehaviour389",
    ends={
        Property(name="ResourceDemandingInternalBehaviour390", type=pcm_av_seff_av_InternalCallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_seff_av_InternalCallAction", type=ResourceDemandingInternalBehaviour, multiplicity=Multiplicity(0, 1))
    }
)
eventType__EmitEventAction391: BinaryAssociation = BinaryAssociation(
    name="eventType__EmitEventAction391",
    ends={
        Property(name="EventType392", type=pcm_av_seff_av_EmitEventAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_seff_av_EmitEventAction", type=EventType, multiplicity=Multiplicity(0, 1))
    }
)
sourceRole__EmitEventAction393: BinaryAssociation = BinaryAssociation(
    name="sourceRole__EmitEventAction393",
    ends={
        Property(name="SourceRole395", type=pcm_av_seff_av_EmitEventAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_seff_av_EmitEventAction394", type=SourceRole, multiplicity=Multiplicity(0, 1))
    }
)
action__InfrastructureCall402: BinaryAssociation = BinaryAssociation(
    name="action__InfrastructureCall402",
    ends={
        Property(name="AbstractInternalControlFlowAction", type=pcm_av_seff_performance_av_InfrastructureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="infrastructureCall__Action", type=AbstractInternalControlFlowAction, multiplicity=Multiplicity(0, 1))
    }
)
requiredRole__InfrastructureCall403: BinaryAssociation = BinaryAssociation(
    name="requiredRole__InfrastructureCall403",
    ends={
        Property(name="InfrastructureRequiredRole405", type=pcm_av_seff_performance_av_InfrastructureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_seff_performance_av_InfrastructureCall404", type=InfrastructureRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
internalFailureOccurrenceDescriptions__InternalAction396: BinaryAssociation = BinaryAssociation(
    name="internalFailureOccurrenceDescriptions__InternalAction396",
    ends={
        Property(name="InternalFailureOccurrenceDescription397", type=pcm_av_seff_av_InternalAction, multiplicity=Multiplicity(1, 1)),
        Property(name="internalAction__InternalFailureOccurrenceDescription", type=InternalFailureOccurrenceDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
signature__InfrastructureCall398: BinaryAssociation = BinaryAssociation(
    name="signature__InfrastructureCall398",
    ends={
        Property(name="InfrastructureSignature399", type=pcm_av_seff_performance_av_InfrastructureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_seff_performance_av_InfrastructureCall", type=InfrastructureSignature, multiplicity=Multiplicity(0, 1))
    }
)
numberOfCalls__InfrastructureCall400: BinaryAssociation = BinaryAssociation(
    name="numberOfCalls__InfrastructureCall400",
    ends={
        Property(name="PCMRandomVariable401", type=pcm_av_seff_performance_av_InfrastructureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="infrastructureCall__PCMRandomVariable", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
specification_ParametericResourceDemand415: BinaryAssociation = BinaryAssociation(
    name="specification_ParametericResourceDemand415",
    ends={
        Property(name="PCMRandomVariable416", type=pcm_av_seff_performance_av_ParametricResourceDemand, multiplicity=Multiplicity(1, 1)),
        Property(name="parametricResourceDemand_PCMRandomVariable", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
requiredResource_ParametricResourceDemand417: BinaryAssociation = BinaryAssociation(
    name="requiredResource_ParametricResourceDemand417",
    ends={
        Property(name="ProcessingResourceType418", type=pcm_av_seff_performance_av_ParametricResourceDemand, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_seff_performance_av_ParametricResourceDemand", type=ProcessingResourceType, multiplicity=Multiplicity(0, 1))
    }
)
action_ParametricResourceDemand419: BinaryAssociation = BinaryAssociation(
    name="action_ParametricResourceDemand419",
    ends={
        Property(name="AbstractInternalControlFlowAction420", type=pcm_av_seff_performance_av_ParametricResourceDemand, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceDemand_Action", type=AbstractInternalControlFlowAction, multiplicity=Multiplicity(0, 1))
    }
)
action__ResourceCall406: BinaryAssociation = BinaryAssociation(
    name="action__ResourceCall406",
    ends={
        Property(name="AbstractInternalControlFlowAction407", type=pcm_av_seff_performance_av_ResourceCall, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceCall__Action", type=AbstractInternalControlFlowAction, multiplicity=Multiplicity(0, 1))
    }
)
resourceRequiredRole__ResourceCall408: BinaryAssociation = BinaryAssociation(
    name="resourceRequiredRole__ResourceCall408",
    ends={
        Property(name="entity_av_ResourceRequiredRole409", type=pcm_av_seff_performance_av_ResourceCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_seff_performance_av_ResourceCall", type=entity_av_ResourceRequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
signature__ResourceCall410: BinaryAssociation = BinaryAssociation(
    name="signature__ResourceCall410",
    ends={
        Property(name="ResourceSignature412", type=pcm_av_seff_performance_av_ResourceCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_seff_performance_av_ResourceCall411", type=ResourceSignature, multiplicity=Multiplicity(0, 1))
    }
)
numberOfCalls__ResourceCall413: BinaryAssociation = BinaryAssociation(
    name="numberOfCalls__ResourceCall413",
    ends={
        Property(name="PCMRandomVariable414", type=pcm_av_seff_performance_av_ResourceCall, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceCall__PCMRandomVariable", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
primaryBehaviour__RecoveryAction423: BinaryAssociation = BinaryAssociation(
    name="primaryBehaviour__RecoveryAction423",
    ends={
        Property(name="seff_reliability_av_RecoveryActionBehaviour424", type=pcm_av_seff_reliability_av_RecoveryAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_seff_reliability_av_RecoveryAction", type=seff_reliability_av_RecoveryActionBehaviour, multiplicity=Multiplicity(0, 1))
    }
)
recoveryActionBehaviours__RecoveryAction425: BinaryAssociation = BinaryAssociation(
    name="recoveryActionBehaviours__RecoveryAction425",
    ends={
        Property(name="RecoveryActionBehaviour", type=pcm_av_seff_reliability_av_RecoveryAction, multiplicity=Multiplicity(1, 1)),
        Property(name="recoveryAction__RecoveryActionBehaviour", type=seff_reliability_av_RecoveryActionBehaviour, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
failureTypes_FailureHandlingEntity426: BinaryAssociation = BinaryAssociation(
    name="failureTypes_FailureHandlingEntity426",
    ends={
        Property(name="FailureType427", type=pcm_av_seff_reliability_av_FailureHandlingEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_seff_reliability_av_FailureHandlingEntity", type=FailureType, multiplicity=Multiplicity(0, 9999))
    }
)
failureHandlingAlternatives__RecoveryActionBehaviour421: BinaryAssociation = BinaryAssociation(
    name="failureHandlingAlternatives__RecoveryActionBehaviour421",
    ends={
        Property(name="seff_reliability_av_RecoveryActionBehaviour", type=pcm_av_seff_reliability_av_RecoveryActionBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_seff_reliability_av_RecoveryActionBehaviour", type=seff_reliability_av_RecoveryActionBehaviour, multiplicity=Multiplicity(0, 9999))
    }
)
recoveryAction__RecoveryActionBehaviour422: BinaryAssociation = BinaryAssociation(
    name="recoveryAction__RecoveryActionBehaviour422",
    ends={
        Property(name="RecoveryAction", type=pcm_av_seff_reliability_av_RecoveryActionBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="recoveryActionBehaviours__RecoveryAction", type=seff_reliability_av_RecoveryAction, multiplicity=Multiplicity(0, 1))
    }
)
qosAnnotations_SpecifiedOutputParameterAbstraction444: BinaryAssociation = BinaryAssociation(
    name="qosAnnotations_SpecifiedOutputParameterAbstraction444",
    ends={
        Property(name="QoSAnnotations445", type=pcm_av_qosannotations_av_SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(1, 1)),
        Property(name="specifiedOutputParameterAbstractions_QoSAnnotations", type=QoSAnnotations, multiplicity=Multiplicity(0, 1))
    }
)
signature_SpecifiedQoSAnnation428: BinaryAssociation = BinaryAssociation(
    name="signature_SpecifiedQoSAnnation428",
    ends={
        Property(name="Signature429", type=pcm_av_qosannotations_av_SpecifiedQoSAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_qosannotations_av_SpecifiedQoSAnnotation", type=Signature, multiplicity=Multiplicity(0, 1))
    }
)
role_SpecifiedQoSAnnotation430: BinaryAssociation = BinaryAssociation(
    name="role_SpecifiedQoSAnnotation430",
    ends={
        Property(name="Role", type=pcm_av_qosannotations_av_SpecifiedQoSAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_qosannotations_av_SpecifiedQoSAnnotation431", type=Role, multiplicity=Multiplicity(0, 1))
    }
)
qosAnnotations_SpecifiedQoSAnnotation432: BinaryAssociation = BinaryAssociation(
    name="qosAnnotations_SpecifiedQoSAnnotation432",
    ends={
        Property(name="QoSAnnotations", type=pcm_av_qosannotations_av_SpecifiedQoSAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="specifiedQoSAnnotations_QoSAnnotations", type=QoSAnnotations, multiplicity=Multiplicity(0, 1))
    }
)
specifiedOutputParameterAbstractions_QoSAnnotations433: BinaryAssociation = BinaryAssociation(
    name="specifiedOutputParameterAbstractions_QoSAnnotations433",
    ends={
        Property(name="SpecifiedOutputParameterAbstraction434", type=pcm_av_qosannotations_av_QoSAnnotations, multiplicity=Multiplicity(1, 1)),
        Property(name="qosAnnotations_SpecifiedOutputParameterAbstraction", type=SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
system_QoSAnnotations435: BinaryAssociation = BinaryAssociation(
    name="system_QoSAnnotations435",
    ends={
        Property(name="System", type=pcm_av_qosannotations_av_QoSAnnotations, multiplicity=Multiplicity(1, 1)),
        Property(name="qosAnnotations_System", type=System, multiplicity=Multiplicity(0, 1))
    }
)
specifiedQoSAnnotations_QoSAnnotations436: BinaryAssociation = BinaryAssociation(
    name="specifiedQoSAnnotations_QoSAnnotations436",
    ends={
        Property(name="SpecifiedQoSAnnotation", type=pcm_av_qosannotations_av_QoSAnnotations, multiplicity=Multiplicity(1, 1)),
        Property(name="qosAnnotations_SpecifiedQoSAnnotation", type=SpecifiedQoSAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
signature_SpecifiedOutputParameterAbstraction437: BinaryAssociation = BinaryAssociation(
    name="signature_SpecifiedOutputParameterAbstraction437",
    ends={
        Property(name="Signature438", type=pcm_av_qosannotations_av_SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_qosannotations_av_SpecifiedOutputParameterAbstraction", type=Signature, multiplicity=Multiplicity(0, 1))
    }
)
role_SpecifiedOutputParameterAbstraction439: BinaryAssociation = BinaryAssociation(
    name="role_SpecifiedOutputParameterAbstraction439",
    ends={
        Property(name="Role441", type=pcm_av_qosannotations_av_SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_qosannotations_av_SpecifiedOutputParameterAbstraction440", type=Role, multiplicity=Multiplicity(0, 1))
    }
)
expectedExternalOutputs_SpecifiedOutputParameterAbstraction442: BinaryAssociation = BinaryAssociation(
    name="expectedExternalOutputs_SpecifiedOutputParameterAbstraction442",
    ends={
        Property(name="VariableUsage443", type=pcm_av_qosannotations_av_SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(1, 1)),
        Property(name="specifiedOutputParameterAbstraction_expectedExternalOutputs_VariableUsage", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
externalFailureOccurrenceDescriptions__SpecifiedReliabilityAnnotation450: BinaryAssociation = BinaryAssociation(
    name="externalFailureOccurrenceDescriptions__SpecifiedReliabilityAnnotation450",
    ends={
        Property(name="specifiedReliabilityAnnotation__ExternalFailureOccurrenceDescription", type=ExternalFailureOccurrenceDescription, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="ExternalFailureOccurrenceDescription", type=pcm_av_qos_reliability_av_SpecifiedReliabilityAnnotation, multiplicity=Multiplicity(1, 1))
    }
)
specification_SpecifiedExecutionTime446: BinaryAssociation = BinaryAssociation(
    name="specification_SpecifiedExecutionTime446",
    ends={
        Property(name="PCMRandomVariable447", type=pcm_av_qos_performance_av_SpecifiedExecutionTime, multiplicity=Multiplicity(1, 1)),
        Property(name="specifiedExecutionTime_PCMRandomVariable", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assemblyContext_ComponentSpecifiedExecutionTime448: BinaryAssociation = BinaryAssociation(
    name="assemblyContext_ComponentSpecifiedExecutionTime448",
    ends={
        Property(name="composition_av_AssemblyContext449", type=pcm_av_qos_performance_av_ComponentSpecifiedExecutionTime, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_qos_performance_av_ComponentSpecifiedExecutionTime", type=composition_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
qosAnnotations_System451: BinaryAssociation = BinaryAssociation(
    name="qosAnnotations_System451",
    ends={
        Property(name="QoSAnnotations452", type=pcm_av_system_av_System, multiplicity=Multiplicity(1, 1)),
        Property(name="system_QoSAnnotations", type=QoSAnnotations, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
linkingResources__ResourceEnvironment453: BinaryAssociation = BinaryAssociation(
    name="linkingResources__ResourceEnvironment453",
    ends={
        Property(name="LinkingResource", type=pcm_av_resourceenvironment_av_ResourceEnvironment, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceEnvironment_LinkingResource", type=LinkingResource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceContainer_ResourceEnvironment454: BinaryAssociation = BinaryAssociation(
    name="resourceContainer_ResourceEnvironment454",
    ends={
        Property(name="ResourceContainer", type=pcm_av_resourceenvironment_av_ResourceEnvironment, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceEnvironment_ResourceContainer", type=ResourceContainer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connectedResourceContainers_LinkingResource455: BinaryAssociation = BinaryAssociation(
    name="connectedResourceContainers_LinkingResource455",
    ends={
        Property(name="ResourceContainer456", type=pcm_av_resourceenvironment_av_LinkingResource, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_resourceenvironment_av_LinkingResource", type=ResourceContainer, multiplicity=Multiplicity(0, 9999))
    }
)
communicationLinkResourceSpecifications_LinkingResource457: BinaryAssociation = BinaryAssociation(
    name="communicationLinkResourceSpecifications_LinkingResource457",
    ends={
        Property(name="CommunicationLinkResourceSpecification458", type=pcm_av_resourceenvironment_av_LinkingResource, multiplicity=Multiplicity(1, 1)),
        Property(name="linkingResource_CommunicationLinkResourceSpecification", type=CommunicationLinkResourceSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resourceEnvironment_LinkingResource459: BinaryAssociation = BinaryAssociation(
    name="resourceEnvironment_LinkingResource459",
    ends={
        Property(name="ResourceEnvironment", type=pcm_av_resourceenvironment_av_LinkingResource, multiplicity=Multiplicity(1, 1)),
        Property(name="linkingResources__ResourceEnvironment", type=ResourceEnvironment, multiplicity=Multiplicity(0, 1))
    }
)
activeResourceSpecifications_ResourceContainer460: BinaryAssociation = BinaryAssociation(
    name="activeResourceSpecifications_ResourceContainer460",
    ends={
        Property(name="ProcessingResourceSpecification461", type=pcm_av_resourceenvironment_av_ResourceContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceContainer_ProcessingResourceSpecification", type=ProcessingResourceSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceEnvironment_ResourceContainer462: BinaryAssociation = BinaryAssociation(
    name="resourceEnvironment_ResourceContainer462",
    ends={
        Property(name="ResourceEnvironment463", type=pcm_av_resourceenvironment_av_ResourceContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceContainer_ResourceEnvironment", type=ResourceEnvironment, multiplicity=Multiplicity(0, 1))
    }
)
nestedResourceContainers__ResourceContainer464: BinaryAssociation = BinaryAssociation(
    name="nestedResourceContainers__ResourceContainer464",
    ends={
        Property(name="ResourceContainer465", type=pcm_av_resourceenvironment_av_ResourceContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="parentResourceContainer__ResourceContainer", type=ResourceContainer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentResourceContainer__ResourceContainer466: BinaryAssociation = BinaryAssociation(
    name="parentResourceContainer__ResourceContainer466",
    ends={
        Property(name="ResourceContainer467", type=pcm_av_resourceenvironment_av_ResourceContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="nestedResourceContainers__ResourceContainer", type=ResourceContainer, multiplicity=Multiplicity(0, 1))
    }
)
resourceContainer_AllocationContext485: BinaryAssociation = BinaryAssociation(
    name="resourceContainer_AllocationContext485",
    ends={
        Property(name="pcm_av_allocation_av_AllocationContext", type=ResourceContainer, multiplicity=Multiplicity(0, 1)),
        Property(name="ResourceContainer486", type=pcm_av_allocation_av_AllocationContext, multiplicity=Multiplicity(1, 1))
    }
)
assemblyContext_AllocationContext487: BinaryAssociation = BinaryAssociation(
    name="assemblyContext_AllocationContext487",
    ends={
        Property(name="composition_av_AssemblyContext489", type=pcm_av_allocation_av_AllocationContext, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_allocation_av_AllocationContext488", type=composition_av_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
allocation_AllocationContext490: BinaryAssociation = BinaryAssociation(
    name="allocation_AllocationContext490",
    ends={
        Property(name="Allocation", type=pcm_av_allocation_av_AllocationContext, multiplicity=Multiplicity(1, 1)),
        Property(name="allocationContexts_Allocation", type=Allocation, multiplicity=Multiplicity(0, 1))
    }
)
eventChannel__AllocationContext491: BinaryAssociation = BinaryAssociation(
    name="eventChannel__AllocationContext491",
    ends={
        Property(name="composition_av_EventChannel", type=pcm_av_allocation_av_AllocationContext, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_allocation_av_AllocationContext492", type=composition_av_EventChannel, multiplicity=Multiplicity(0, 1))
    }
)
schedulingPolicy468: BinaryAssociation = BinaryAssociation(
    name="schedulingPolicy468",
    ends={
        Property(name="SchedulingPolicy469", type=pcm_av_resourceenvironment_av_ProcessingResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_resourceenvironment_av_ProcessingResourceSpecification", type=SchedulingPolicy, multiplicity=Multiplicity(0, 1))
    }
)
activeResourceType_ActiveResourceSpecification470: BinaryAssociation = BinaryAssociation(
    name="activeResourceType_ActiveResourceSpecification470",
    ends={
        Property(name="ProcessingResourceType472", type=pcm_av_resourceenvironment_av_ProcessingResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_resourceenvironment_av_ProcessingResourceSpecification471", type=ProcessingResourceType, multiplicity=Multiplicity(0, 1))
    }
)
processingRate_ProcessingResourceSpecification473: BinaryAssociation = BinaryAssociation(
    name="processingRate_ProcessingResourceSpecification473",
    ends={
        Property(name="PCMRandomVariable474", type=pcm_av_resourceenvironment_av_ProcessingResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="processingResourceSpecification_processingRate_PCMRandomVariable", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resourceContainer_ProcessingResourceSpecification475: BinaryAssociation = BinaryAssociation(
    name="resourceContainer_ProcessingResourceSpecification475",
    ends={
        Property(name="ResourceContainer476", type=pcm_av_resourceenvironment_av_ProcessingResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="activeResourceSpecifications_ResourceContainer", type=ResourceContainer, multiplicity=Multiplicity(0, 1))
    }
)
linkingResource_CommunicationLinkResourceSpecification477: BinaryAssociation = BinaryAssociation(
    name="linkingResource_CommunicationLinkResourceSpecification477",
    ends={
        Property(name="LinkingResource478", type=pcm_av_resourceenvironment_av_CommunicationLinkResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="communicationLinkResourceSpecifications_LinkingResource", type=LinkingResource, multiplicity=Multiplicity(0, 1))
    }
)
communicationLinkResourceType_CommunicationLinkResourceSpecification479: BinaryAssociation = BinaryAssociation(
    name="communicationLinkResourceType_CommunicationLinkResourceSpecification479",
    ends={
        Property(name="CommunicationLinkResourceType480", type=pcm_av_resourceenvironment_av_CommunicationLinkResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_resourceenvironment_av_CommunicationLinkResourceSpecification", type=CommunicationLinkResourceType, multiplicity=Multiplicity(0, 1))
    }
)
latency_CommunicationLinkResourceSpecification481: BinaryAssociation = BinaryAssociation(
    name="latency_CommunicationLinkResourceSpecification481",
    ends={
        Property(name="PCMRandomVariable482", type=pcm_av_resourceenvironment_av_CommunicationLinkResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="communicationLinkResourceSpecification_latency_PCMRandomVariable", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
throughput_CommunicationLinkResourceSpecification483: BinaryAssociation = BinaryAssociation(
    name="throughput_CommunicationLinkResourceSpecification483",
    ends={
        Property(name="PCMRandomVariable484", type=pcm_av_resourceenvironment_av_CommunicationLinkResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="communicationLinkResourceSpecifcation_throughput_PCMRandomVariable", type=PCMRandomVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
completions_CompletionRepository499: BinaryAssociation = BinaryAssociation(
    name="completions_CompletionRepository499",
    ends={
        Property(name="Completion", type=pcm_av_completions_av_CompletionRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_completions_av_CompletionRepository", type=Completion, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
targetResourceEnvironment_Allocation493: BinaryAssociation = BinaryAssociation(
    name="targetResourceEnvironment_Allocation493",
    ends={
        Property(name="ResourceEnvironment494", type=pcm_av_allocation_av_Allocation, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_allocation_av_Allocation", type=ResourceEnvironment, multiplicity=Multiplicity(0, 1))
    }
)
system_Allocation495: BinaryAssociation = BinaryAssociation(
    name="system_Allocation495",
    ends={
        Property(name="System497", type=pcm_av_allocation_av_Allocation, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_allocation_av_Allocation496", type=System, multiplicity=Multiplicity(0, 1))
    }
)
allocationContexts_Allocation498: BinaryAssociation = BinaryAssociation(
    name="allocationContexts_Allocation498",
    ends={
        Property(name="AllocationContext", type=pcm_av_allocation_av_Allocation, multiplicity=Multiplicity(1, 1)),
        Property(name="allocation_AllocationContext", type=AllocationContext, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredCommunicationLinkResource_ParametricResourceDemand500: BinaryAssociation = BinaryAssociation(
    name="requiredCommunicationLinkResource_ParametricResourceDemand500",
    ends={
        Property(name="CommunicationLinkResourceType501", type=pcm_av_completions_av_NetworkDemandParametricResourceDemand, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_av_completions_av_NetworkDemandParametricResourceDemand", type=CommunicationLinkResourceType, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_pcm_av_core_av_PCMRandomVariable_RandomVariable = Generalization(general=RandomVariable, specific=pcm_av_core_av_PCMRandomVariable)
gen_pcm_av_entity_av_ResourceInterfaceRequiringEntity_Entity = Generalization(general=Entity, specific=pcm_av_entity_av_ResourceInterfaceRequiringEntity)
gen_pcm_av_entity_av_ResourceRequiredRole_Role = Generalization(general=Role, specific=pcm_av_entity_av_ResourceRequiredRole)
gen_pcm_av_entity_av_ResourceProvidedRole_Role = Generalization(general=Role, specific=pcm_av_entity_av_ResourceProvidedRole)
gen_pcm_av_entity_av_InterfaceProvidingRequiringEntity_entity_av_InterfaceProvidingEntity = Generalization(general=entity_av_InterfaceProvidingEntity, specific=pcm_av_entity_av_InterfaceProvidingRequiringEntity)
gen_pcm_av_entity_av_InterfaceProvidingRequiringEntity_entity_av_InterfaceRequiringEntity = Generalization(general=entity_av_InterfaceRequiringEntity, specific=pcm_av_entity_av_InterfaceProvidingRequiringEntity)
gen_pcm_av_entity_av_InterfaceProvidingEntity_Entity = Generalization(general=Entity, specific=pcm_av_entity_av_InterfaceProvidingEntity)
gen_pcm_av_entity_av_InterfaceRequiringEntity_entity_av_Entity = Generalization(general=entity_av_Entity, specific=pcm_av_entity_av_InterfaceRequiringEntity)
gen_pcm_av_entity_av_InterfaceRequiringEntity_entity_av_ResourceInterfaceRequiringEntity = Generalization(general=entity_av_ResourceInterfaceRequiringEntity, specific=pcm_av_entity_av_InterfaceRequiringEntity)
gen_pcm_av_entity_av_ResourceInterfaceProvidingEntity_Entity = Generalization(general=Entity, specific=pcm_av_entity_av_ResourceInterfaceProvidingEntity)
gen_pcm_av_entity_av_ComposedProvidingRequiringEntity_composition_av_ComposedStructure = Generalization(general=composition_av_ComposedStructure, specific=pcm_av_entity_av_ComposedProvidingRequiringEntity)
gen_pcm_av_entity_av_ComposedProvidingRequiringEntity_entity_av_InterfaceProvidingRequiringEntity = Generalization(general=entity_av_InterfaceProvidingRequiringEntity, specific=pcm_av_entity_av_ComposedProvidingRequiringEntity)
gen_pcm_av_entity_av_ResourceInterfaceProvidingRequiringEntity_entity_av_ResourceInterfaceRequiringEntity = Generalization(general=entity_av_ResourceInterfaceRequiringEntity, specific=pcm_av_entity_av_ResourceInterfaceProvidingRequiringEntity)
gen_pcm_av_entity_av_ResourceInterfaceProvidingRequiringEntity_entity_av_ResourceInterfaceProvidingEntity = Generalization(general=entity_av_ResourceInterfaceProvidingEntity, specific=pcm_av_entity_av_ResourceInterfaceProvidingRequiringEntity)
gen_pcm_av_entity_av_Entity_Identifier = Generalization(general=Identifier, specific=pcm_av_entity_av_Entity)
gen_pcm_av_entity_av_Entity_entity_av_NamedElement = Generalization(general=entity_av_NamedElement, specific=pcm_av_entity_av_Entity)
gen_pcm_av_composition_av_DelegationConnector_Connector = Generalization(general=Connector, specific=pcm_av_composition_av_DelegationConnector)
gen_pcm_av_composition_av_Connector_Entity = Generalization(general=Entity, specific=pcm_av_composition_av_Connector)
gen_pcm_av_composition_av_ComposedStructure_Entity = Generalization(general=Entity, specific=pcm_av_composition_av_ComposedStructure)
gen_pcm_av_composition_av_ProvidedDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_av_composition_av_ProvidedDelegationConnector)
gen_pcm_av_composition_av_EventChannel_Entity = Generalization(general=Entity, specific=pcm_av_composition_av_EventChannel)
gen_pcm_av_composition_av_EventChannelSourceConnector_Connector = Generalization(general=Connector, specific=pcm_av_composition_av_EventChannelSourceConnector)
gen_pcm_av_composition_av_EventChannelSinkConnector_Connector = Generalization(general=Connector, specific=pcm_av_composition_av_EventChannelSinkConnector)
gen_pcm_av_composition_av_RequiredDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_av_composition_av_RequiredDelegationConnector)
gen_pcm_av_composition_av_AssemblyConnector_Connector = Generalization(general=Connector, specific=pcm_av_composition_av_AssemblyConnector)
gen_pcm_av_composition_av_SinkDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_av_composition_av_SinkDelegationConnector)
gen_pcm_av_composition_av_AssemblyEventConnector_Connector = Generalization(general=Connector, specific=pcm_av_composition_av_AssemblyEventConnector)
gen_pcm_av_composition_av_SourceDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_av_composition_av_SourceDelegationConnector)
gen_pcm_av_composition_av_AssemblyInfrastructureConnector_Connector = Generalization(general=Connector, specific=pcm_av_composition_av_AssemblyInfrastructureConnector)
gen_pcm_av_composition_av_ProvidedInfrastructureDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_av_composition_av_ProvidedInfrastructureDelegationConnector)
gen_pcm_av_composition_av_RequiredInfrastructureDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_av_composition_av_RequiredInfrastructureDelegationConnector)
gen_pcm_av_composition_av_RequiredResourceDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_av_composition_av_RequiredResourceDelegationConnector)
gen_pcm_av_composition_av_AssemblyContext_Entity = Generalization(general=Entity, specific=pcm_av_composition_av_AssemblyContext)
gen_pcm_av_usagemodel_av_UsageScenario_Entity = Generalization(general=Entity, specific=pcm_av_usagemodel_av_UsageScenario)
gen_pcm_av_usagemodel_av_EntryLevelSystemCall_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_av_usagemodel_av_EntryLevelSystemCall)
gen_pcm_av_usagemodel_av_AbstractUserAction_Entity = Generalization(general=Entity, specific=pcm_av_usagemodel_av_AbstractUserAction)
gen_pcm_av_usagemodel_av_ScenarioBehaviour_Entity = Generalization(general=Entity, specific=pcm_av_usagemodel_av_ScenarioBehaviour)
gen_pcm_av_usagemodel_av_Branch_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_av_usagemodel_av_Branch)
gen_pcm_av_usagemodel_av_Loop_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_av_usagemodel_av_Loop)
gen_pcm_av_usagemodel_av_Stop_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_av_usagemodel_av_Stop)
gen_pcm_av_usagemodel_av_Start_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_av_usagemodel_av_Start)
gen_pcm_av_usagemodel_av_OpenWorkload_Workload = Generalization(general=Workload, specific=pcm_av_usagemodel_av_OpenWorkload)
gen_pcm_av_usagemodel_av_Delay_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_av_usagemodel_av_Delay)
gen_pcm_av_usagemodel_av_ClosedWorkload_Workload = Generalization(general=Workload, specific=pcm_av_usagemodel_av_ClosedWorkload)
gen_pcm_av_repository_av_PassiveResource_Entity = Generalization(general=Entity, specific=pcm_av_repository_av_PassiveResource)
gen_pcm_av_repository_av_BasicComponent_ImplementationComponentType = Generalization(general=ImplementationComponentType, specific=pcm_av_repository_av_BasicComponent)
gen_pcm_av_repository_av_ImplementationComponentType_RepositoryComponent = Generalization(general=RepositoryComponent, specific=pcm_av_repository_av_ImplementationComponentType)
gen_pcm_av_repository_av_RepositoryComponent_InterfaceProvidingRequiringEntity = Generalization(general=InterfaceProvidingRequiringEntity, specific=pcm_av_repository_av_RepositoryComponent)
gen_pcm_av_repository_av_ProvidedRole_Role = Generalization(general=Role, specific=pcm_av_repository_av_ProvidedRole)
gen_pcm_av_repository_av_Repository_Entity = Generalization(general=Entity, specific=pcm_av_repository_av_Repository)
gen_pcm_av_repository_av_Interface_Entity = Generalization(general=Entity, specific=pcm_av_repository_av_Interface)
gen_pcm_av_repository_av_InfrastructureSignature_Signature = Generalization(general=Signature, specific=pcm_av_repository_av_InfrastructureSignature)
gen_pcm_av_repository_av_EventGroup_Interface = Generalization(general=Interface, specific=pcm_av_repository_av_EventGroup)
gen_pcm_av_repository_av_EventType_Signature = Generalization(general=Signature, specific=pcm_av_repository_av_EventType)
gen_pcm_av_repository_av_Signature_Entity = Generalization(general=Entity, specific=pcm_av_repository_av_Signature)
gen_pcm_av_repository_av_OperationRequiredRole_RequiredRole = Generalization(general=RequiredRole, specific=pcm_av_repository_av_OperationRequiredRole)
gen_pcm_av_repository_av_InfrastructureInterface_Interface = Generalization(general=Interface, specific=pcm_av_repository_av_InfrastructureInterface)
gen_pcm_av_repository_av_InfrastructureRequiredRole_RequiredRole = Generalization(general=RequiredRole, specific=pcm_av_repository_av_InfrastructureRequiredRole)
gen_pcm_av_repository_av_RequiredRole_Role = Generalization(general=Role, specific=pcm_av_repository_av_RequiredRole)
gen_pcm_av_repository_av_OperationSignature_Signature = Generalization(general=Signature, specific=pcm_av_repository_av_OperationSignature)
gen_pcm_av_repository_av_OperationInterface_Interface = Generalization(general=Interface, specific=pcm_av_repository_av_OperationInterface)
gen_pcm_av_repository_av_ProvidesComponentType_RepositoryComponent = Generalization(general=RepositoryComponent, specific=pcm_av_repository_av_ProvidesComponentType)
gen_pcm_av_repository_av_SourceRole_RequiredRole = Generalization(general=RequiredRole, specific=pcm_av_repository_av_SourceRole)
gen_pcm_av_repository_av_SinkRole_ProvidedRole = Generalization(general=ProvidedRole, specific=pcm_av_repository_av_SinkRole)
gen_pcm_av_repository_av_OperationProvidedRole_ProvidedRole = Generalization(general=ProvidedRole, specific=pcm_av_repository_av_OperationProvidedRole)
gen_pcm_av_repository_av_InfrastructureProvidedRole_ProvidedRole = Generalization(general=ProvidedRole, specific=pcm_av_repository_av_InfrastructureProvidedRole)
gen_pcm_av_repository_av_CompleteComponentType_RepositoryComponent = Generalization(general=RepositoryComponent, specific=pcm_av_repository_av_CompleteComponentType)
gen_pcm_av_repository_av_PrimitiveDataType_DataType = Generalization(general=DataType, specific=pcm_av_repository_av_PrimitiveDataType)
gen_pcm_av_repository_av_CompositeComponent_entity_av_ComposedProvidingRequiringEntity = Generalization(general=entity_av_ComposedProvidingRequiringEntity, specific=pcm_av_repository_av_CompositeComponent)
gen_pcm_av_repository_av_CompositeComponent_repository_av_ImplementationComponentType = Generalization(general=repository_av_ImplementationComponentType, specific=pcm_av_repository_av_CompositeComponent)
gen_pcm_av_resourcetype_av_ResourceSignature_Entity = Generalization(general=Entity, specific=pcm_av_resourcetype_av_ResourceSignature)
gen_pcm_av_repository_av_CollectionDataType_entity_av_Entity = Generalization(general=entity_av_Entity, specific=pcm_av_repository_av_CollectionDataType)
gen_pcm_av_repository_av_CollectionDataType_repository_av_DataType = Generalization(general=repository_av_DataType, specific=pcm_av_repository_av_CollectionDataType)
gen_pcm_av_repository_av_CompositeDataType_entity_av_Entity = Generalization(general=entity_av_Entity, specific=pcm_av_repository_av_CompositeDataType)
gen_pcm_av_repository_av_CompositeDataType_repository_av_DataType = Generalization(general=repository_av_DataType, specific=pcm_av_repository_av_CompositeDataType)
gen_pcm_av_repository_av_InnerDeclaration_NamedElement = Generalization(general=NamedElement, specific=pcm_av_repository_av_InnerDeclaration)
gen_pcm_av_repository_av_Role_Entity = Generalization(general=Entity, specific=pcm_av_repository_av_Role)
gen_pcm_av_resourcetype_av_ProcessingResourceType_ResourceType = Generalization(general=ResourceType, specific=pcm_av_resourcetype_av_ProcessingResourceType)
gen_pcm_av_resourcetype_av_ResourceType_entity_av_Entity = Generalization(general=entity_av_Entity, specific=pcm_av_resourcetype_av_ResourceType)
gen_pcm_av_resourcetype_av_ResourceType_UnitCarryingElement = Generalization(general=UnitCarryingElement, specific=pcm_av_resourcetype_av_ResourceType)
gen_pcm_av_resourcetype_av_ResourceType_entity_av_ResourceInterfaceProvidingEntity = Generalization(general=entity_av_ResourceInterfaceProvidingEntity, specific=pcm_av_resourcetype_av_ResourceType)
gen_pcm_av_resourcetype_av_SchedulingPolicy_Entity = Generalization(general=Entity, specific=pcm_av_resourcetype_av_SchedulingPolicy)
gen_pcm_av_resourcetype_av_CommunicationLinkResourceType_ResourceType = Generalization(general=ResourceType, specific=pcm_av_resourcetype_av_CommunicationLinkResourceType)
gen_pcm_av_resourcetype_av_ResourceInterface_Entity = Generalization(general=Entity, specific=pcm_av_resourcetype_av_ResourceInterface)
gen_pcm_av_parameter_av_CharacterisedVariable_Variable = Generalization(general=Variable, specific=pcm_av_parameter_av_CharacterisedVariable)
gen_pcm_av_reliability_av_HardwareInducedFailureType_FailureType = Generalization(general=FailureType, specific=pcm_av_reliability_av_HardwareInducedFailureType)
gen_pcm_av_reliability_av_SoftwareInducedFailureType_FailureType = Generalization(general=FailureType, specific=pcm_av_reliability_av_SoftwareInducedFailureType)
gen_pcm_av_reliability_av_InternalFailureOccurrenceDescription_FailureOccurrenceDescription = Generalization(general=FailureOccurrenceDescription, specific=pcm_av_reliability_av_InternalFailureOccurrenceDescription)
gen_pcm_av_reliability_av_NetworkInducedFailureType_FailureType = Generalization(general=FailureType, specific=pcm_av_reliability_av_NetworkInducedFailureType)
gen_pcm_av_seff_av_AbstractAction_Entity = Generalization(general=Entity, specific=pcm_av_seff_av_AbstractAction)
gen_pcm_av_reliability_av_ExternalFailureOccurrenceDescription_FailureOccurrenceDescription = Generalization(general=FailureOccurrenceDescription, specific=pcm_av_reliability_av_ExternalFailureOccurrenceDescription)
gen_pcm_av_reliability_av_ResourceTimeoutFailureType_SoftwareInducedFailureType = Generalization(general=SoftwareInducedFailureType, specific=pcm_av_reliability_av_ResourceTimeoutFailureType)
gen_pcm_av_reliability_av_FailureType_Entity = Generalization(general=Entity, specific=pcm_av_reliability_av_FailureType)
gen_pcm_av_seff_av_StopAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_av_seff_av_StopAction)
gen_pcm_av_seff_av_AbstractInternalControlFlowAction_AbstractAction = Generalization(general=AbstractAction, specific=pcm_av_seff_av_AbstractInternalControlFlowAction)
gen_pcm_av_seff_av_AbstractBranchTransition_Entity = Generalization(general=Entity, specific=pcm_av_seff_av_AbstractBranchTransition)
gen_pcm_av_seff_av_ResourceDemandingBehaviour_Identifier = Generalization(general=Identifier, specific=pcm_av_seff_av_ResourceDemandingBehaviour)
gen_pcm_av_seff_av_AbstractLoopAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_av_seff_av_AbstractLoopAction)
gen_pcm_av_seff_av_ResourceDemandingSEFF_Identifier = Generalization(general=Identifier, specific=pcm_av_seff_av_ResourceDemandingSEFF)
gen_pcm_av_seff_av_ResourceDemandingSEFF_seff_av_ServiceEffectSpecification = Generalization(general=seff_av_ServiceEffectSpecification, specific=pcm_av_seff_av_ResourceDemandingSEFF)
gen_pcm_av_seff_av_BranchAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_av_seff_av_BranchAction)
gen_pcm_av_seff_av_StartAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_av_seff_av_StartAction)
gen_pcm_av_seff_av_ExternalCallAction_seff_av_AbstractAction = Generalization(general=seff_av_AbstractAction, specific=pcm_av_seff_av_ExternalCallAction)
gen_pcm_av_seff_av_ExternalCallAction_seff_av_CallReturnAction = Generalization(general=seff_av_CallReturnAction, specific=pcm_av_seff_av_ExternalCallAction)
gen_pcm_av_seff_av_ExternalCallAction_seff_reliability_av_FailureHandlingEntity = Generalization(general=seff_reliability_av_FailureHandlingEntity, specific=pcm_av_seff_av_ExternalCallAction)
gen_pcm_av_seff_av_ResourceDemandingSEFF_seff_av_ResourceDemandingBehaviour = Generalization(general=seff_av_ResourceDemandingBehaviour, specific=pcm_av_seff_av_ResourceDemandingSEFF)
gen_pcm_av_seff_av_ResourceDemandingInternalBehaviour_ResourceDemandingBehaviour = Generalization(general=ResourceDemandingBehaviour, specific=pcm_av_seff_av_ResourceDemandingInternalBehaviour)
gen_pcm_av_seff_av_ReleaseAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_av_seff_av_ReleaseAction)
gen_pcm_av_seff_av_LoopAction_AbstractLoopAction = Generalization(general=AbstractLoopAction, specific=pcm_av_seff_av_LoopAction)
gen_pcm_av_seff_av_ForkAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_av_seff_av_ForkAction)
gen_pcm_av_seff_av_ForkedBehaviour_ResourceDemandingBehaviour = Generalization(general=ResourceDemandingBehaviour, specific=pcm_av_seff_av_ForkedBehaviour)
gen_pcm_av_seff_av_CallReturnAction_CallAction = Generalization(general=CallAction, specific=pcm_av_seff_av_CallReturnAction)
gen_pcm_av_seff_av_ProbabilisticBranchTransition_AbstractBranchTransition = Generalization(general=AbstractBranchTransition, specific=pcm_av_seff_av_ProbabilisticBranchTransition)
gen_pcm_av_seff_av_AcquireAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_av_seff_av_AcquireAction)
gen_pcm_av_seff_av_CollectionIteratorAction_AbstractLoopAction = Generalization(general=AbstractLoopAction, specific=pcm_av_seff_av_CollectionIteratorAction)
gen_pcm_av_seff_av_GuardedBranchTransition_AbstractBranchTransition = Generalization(general=AbstractBranchTransition, specific=pcm_av_seff_av_GuardedBranchTransition)
gen_pcm_av_seff_av_SetVariableAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_av_seff_av_SetVariableAction)
gen_pcm_av_seff_av_InternalCallAction_seff_av_CallAction = Generalization(general=seff_av_CallAction, specific=pcm_av_seff_av_InternalCallAction)
gen_pcm_av_seff_av_InternalCallAction_seff_av_AbstractInternalControlFlowAction = Generalization(general=seff_av_AbstractInternalControlFlowAction, specific=pcm_av_seff_av_InternalCallAction)
gen_pcm_av_seff_av_EmitEventAction_seff_av_AbstractAction = Generalization(general=seff_av_AbstractAction, specific=pcm_av_seff_av_EmitEventAction)
gen_pcm_av_seff_av_EmitEventAction_seff_av_CallAction = Generalization(general=seff_av_CallAction, specific=pcm_av_seff_av_EmitEventAction)
gen_pcm_av_seff_av_InternalAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_av_seff_av_InternalAction)
gen_pcm_av_seff_performance_av_ResourceCall_CallAction = Generalization(general=CallAction, specific=pcm_av_seff_performance_av_ResourceCall)
gen_pcm_av_seff_performance_av_InfrastructureCall_CallAction = Generalization(general=CallAction, specific=pcm_av_seff_performance_av_InfrastructureCall)
gen_pcm_av_seff_reliability_av_RecoveryActionBehaviour_seff_reliability_av_FailureHandlingEntity = Generalization(general=seff_reliability_av_FailureHandlingEntity, specific=pcm_av_seff_reliability_av_RecoveryActionBehaviour)
gen_pcm_av_seff_reliability_av_RecoveryActionBehaviour_seff_av_ResourceDemandingBehaviour = Generalization(general=seff_av_ResourceDemandingBehaviour, specific=pcm_av_seff_reliability_av_RecoveryActionBehaviour)
gen_pcm_av_seff_reliability_av_FailureHandlingEntity_Entity = Generalization(general=Entity, specific=pcm_av_seff_reliability_av_FailureHandlingEntity)
gen_pcm_av_seff_reliability_av_RecoveryAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_av_seff_reliability_av_RecoveryAction)
gen_pcm_av_qos_performance_av_SystemSpecifiedExecutionTime_SpecifiedExecutionTime = Generalization(general=SpecifiedExecutionTime, specific=pcm_av_qos_performance_av_SystemSpecifiedExecutionTime)
gen_pcm_av_qosannotations_av_QoSAnnotations_Entity = Generalization(general=Entity, specific=pcm_av_qosannotations_av_QoSAnnotations)
gen_pcm_av_system_av_System_entity_av_Entity = Generalization(general=entity_av_Entity, specific=pcm_av_system_av_System)
gen_pcm_av_system_av_System_entity_av_ComposedProvidingRequiringEntity = Generalization(general=entity_av_ComposedProvidingRequiringEntity, specific=pcm_av_system_av_System)
gen_pcm_av_qos_performance_av_SpecifiedExecutionTime_SpecifiedQoSAnnotation = Generalization(general=SpecifiedQoSAnnotation, specific=pcm_av_qos_performance_av_SpecifiedExecutionTime)
gen_pcm_av_qos_performance_av_ComponentSpecifiedExecutionTime_SpecifiedExecutionTime = Generalization(general=SpecifiedExecutionTime, specific=pcm_av_qos_performance_av_ComponentSpecifiedExecutionTime)
gen_pcm_av_qos_reliability_av_SpecifiedReliabilityAnnotation_SpecifiedQoSAnnotation = Generalization(general=SpecifiedQoSAnnotation, specific=pcm_av_qos_reliability_av_SpecifiedReliabilityAnnotation)
gen_pcm_av_resourceenvironment_av_ProcessingResourceSpecification_Identifier = Generalization(general=Identifier, specific=pcm_av_resourceenvironment_av_ProcessingResourceSpecification)
gen_pcm_av_resourceenvironment_av_ResourceEnvironment_NamedElement = Generalization(general=NamedElement, specific=pcm_av_resourceenvironment_av_ResourceEnvironment)
gen_pcm_av_resourceenvironment_av_LinkingResource_Entity = Generalization(general=Entity, specific=pcm_av_resourceenvironment_av_LinkingResource)
gen_pcm_av_resourceenvironment_av_ResourceContainer_Entity = Generalization(general=Entity, specific=pcm_av_resourceenvironment_av_ResourceContainer)
gen_pcm_av_resourceenvironment_av_CommunicationLinkResourceSpecification_Identifier = Generalization(general=Identifier, specific=pcm_av_resourceenvironment_av_CommunicationLinkResourceSpecification)
gen_pcm_av_allocation_av_AllocationContext_Entity = Generalization(general=Entity, specific=pcm_av_allocation_av_AllocationContext)
gen_pcm_av_completions_av_Completion_entity_av_ComposedProvidingRequiringEntity = Generalization(general=entity_av_ComposedProvidingRequiringEntity, specific=pcm_av_completions_av_Completion)
gen_pcm_av_completions_av_Completion_repository_av_ImplementationComponentType = Generalization(general=repository_av_ImplementationComponentType, specific=pcm_av_completions_av_Completion)
gen_pcm_av_completions_av_DelegatingExternalCallAction_ExternalCallAction = Generalization(general=ExternalCallAction, specific=pcm_av_completions_av_DelegatingExternalCallAction)
gen_pcm_av_completions_av_NetworkDemandParametricResourceDemand_ParametricResourceDemand = Generalization(general=ParametricResourceDemand, specific=pcm_av_completions_av_NetworkDemandParametricResourceDemand)
gen_pcm_av_allocation_av_Allocation_Entity = Generalization(general=Entity, specific=pcm_av_allocation_av_Allocation)
gen_pcm_av_subsystem_av_SubSystem_entity_av_ComposedProvidingRequiringEntity = Generalization(general=entity_av_ComposedProvidingRequiringEntity, specific=pcm_av_subsystem_av_SubSystem)
gen_pcm_av_subsystem_av_SubSystem_repository_av_RepositoryComponent = Generalization(general=repository_av_RepositoryComponent, specific=pcm_av_subsystem_av_SubSystem)

# Domain Model
domain_model = DomainModel(
    name="pcm_av",
    types={GuardedBranchTransition, qos_performance_av_SpecifiedExecutionTime, pcm_av_DummyClass, pcm_av_Advice, pcm_av_EObject, pcm_av_GlobalScope, pcm_av_PerJoinPointScope, pcm_av_core_av_PCMRandomVariable, RandomVariable, ClosedWorkload, PassiveResource, VariableCharacterisation, seff_performance_av_InfrastructureCall, seff_performance_av_ResourceCall, seff_performance_av_ParametricResourceDemand, LoopAction, entity_av_ResourceRequiredRole, pcm_av_entity_av_ResourceRequiredRole, composition_av_EventChannelSinkConnector, composition_av_AssemblyEventConnector, Loop, OpenWorkload, Delay, CommunicationLinkResourceSpecification, ProcessingResourceSpecification, pcm_av_entity_av_ResourceProvidedRole, Role, entity_av_ResourceInterfaceProvidingEntity, ResourceInterface, pcm_av_entity_av_InterfaceProvidingRequiringEntity, entity_av_InterfaceProvidingEntity, entity_av_InterfaceRequiringEntity, pcm_av_entity_av_InterfaceProvidingEntity, Entity, ProvidedRole, pcm_av_entity_av_InterfaceRequiringEntity, entity_av_Entity, entity_av_ResourceInterfaceRequiringEntity, RequiredRole, pcm_av_entity_av_ResourceInterfaceRequiringEntity, pcm_av_entity_av_ResourceInterfaceProvidingEntity, entity_av_ResourceProvidedRole, pcm_av_entity_av_ComposedProvidingRequiringEntity, composition_av_ComposedStructure, entity_av_InterfaceProvidingRequiringEntity, pcm_av_entity_av_NamedElement, pcm_av_entity_av_ResourceInterfaceProvidingRequiringEntity, pcm_av_entity_av_Entity, Identifier, entity_av_NamedElement, pcm_av_composition_av_DelegationConnector, Connector, pcm_av_composition_av_Connector, pcm_av_composition_av_ComposedStructure, pcm_av_composition_av_ProvidedDelegationConnector, DelegationConnector, composition_av_AssemblyContext, composition_av_ResourceRequiredDelegationConnector, composition_av_EventChannel, composition_av_Connector, pcm_av_composition_av_ResourceRequiredDelegationConnector, pcm_av_composition_av_EventChannel, EventGroup, composition_av_EventChannelSourceConnector, pcm_av_composition_av_EventChannelSourceConnector, SourceRole, pcm_av_composition_av_EventChannelSinkConnector, SinkRole, PCMRandomVariable, OperationProvidedRole, pcm_av_composition_av_RequiredDelegationConnector, OperationRequiredRole, pcm_av_composition_av_AssemblyConnector, pcm_av_composition_av_SinkDelegationConnector, pcm_av_composition_av_AssemblyEventConnector, pcm_av_composition_av_SourceDelegationConnector, pcm_av_composition_av_AssemblyInfrastructureConnector, InfrastructureProvidedRole, InfrastructureRequiredRole, pcm_av_composition_av_ProvidedInfrastructureDelegationConnector, pcm_av_composition_av_RequiredInfrastructureDelegationConnector, pcm_av_composition_av_RequiredResourceDelegationConnector, pcm_av_composition_av_AssemblyContext, RepositoryComponent, VariableUsage, OperationSignature, pcm_av_usagemodel_av_Workload, UsageScenario, pcm_av_usagemodel_av_UsageScenario, UsageModel, ScenarioBehaviour, Workload, pcm_av_usagemodel_av_UserData, pcm_av_usagemodel_av_UsageModel, UserData, pcm_av_usagemodel_av_EntryLevelSystemCall, AbstractUserAction, pcm_av_usagemodel_av_BranchTransition, Branch, pcm_av_usagemodel_av_AbstractUserAction, pcm_av_usagemodel_av_ScenarioBehaviour, BranchTransition, pcm_av_usagemodel_av_Branch, pcm_av_usagemodel_av_Loop, pcm_av_usagemodel_av_Stop, pcm_av_usagemodel_av_Start, pcm_av_usagemodel_av_OpenWorkload, pcm_av_usagemodel_av_Delay, pcm_av_usagemodel_av_ClosedWorkload, pcm_av_repository_av_PassiveResource, BasicComponent, ResourceTimeoutFailureType, pcm_av_repository_av_BasicComponent, ImplementationComponentType, ServiceEffectSpecification, pcm_av_repository_av_ImplementationComponentType, InfrastructureSignature, CompleteComponentType, pcm_av_repository_av_RepositoryComponent, InterfaceProvidingRequiringEntity, Repository, pcm_av_repository_av_ProvidedRole, pcm_av_repository_av_Parameter, DataType, EventType, ResourceSignature, pcm_av_repository_av_DataType, pcm_av_repository_av_Repository, Interface, FailureType, pcm_av_repository_av_Interface, pcm_av_repository_av_InfrastructureSignature, InfrastructureInterface, Protocol, RequiredCharacterisation, pcm_av_repository_av_RequiredCharacterisation, Parameter_, pcm_av_repository_av_EventGroup, pcm_av_repository_av_EventType, Signature, pcm_av_repository_av_Signature, ExceptionType, pcm_av_repository_av_ExceptionType, pcm_av_repository_av_OperationRequiredRole, pcm_av_repository_av_InfrastructureInterface, pcm_av_repository_av_InfrastructureRequiredRole, pcm_av_repository_av_RequiredRole, pcm_av_repository_av_OperationSignature, OperationInterface, pcm_av_repository_av_OperationInterface, ProvidesComponentType, pcm_av_repository_av_ProvidesComponentType, pcm_av_repository_av_SourceRole, pcm_av_repository_av_SinkRole, pcm_av_repository_av_OperationProvidedRole, pcm_av_repository_av_InfrastructureProvidedRole, pcm_av_repository_av_CompleteComponentType, pcm_av_repository_av_PrimitiveDataType, pcm_av_repository_av_CompositeComponent, entity_av_ComposedProvidingRequiringEntity, repository_av_ImplementationComponentType, pcm_av_repository_av_CollectionDataType, repository_av_DataType, pcm_av_repository_av_CompositeDataType, CompositeDataType, InnerDeclaration, pcm_av_repository_av_InnerDeclaration, NamedElement, pcm_av_repository_av_Role, pcm_av_resourcetype_av_ResourceSignature, pcm_av_resourcetype_av_ProcessingResourceType, ResourceType, HardwareInducedFailureType, pcm_av_resourcetype_av_ResourceType, UnitCarryingElement, ResourceRepository, pcm_av_resourcetype_av_ResourceRepository, SchedulingPolicy, pcm_av_resourcetype_av_SchedulingPolicy, pcm_av_resourcetype_av_CommunicationLinkResourceType, NetworkInducedFailureType, pcm_av_resourcetype_av_ResourceInterface, EntryLevelSystemCall, pcm_av_protocol_av_Protocol, pcm_av_parameter_av_VariableUsage, CallAction, SynchronisationPoint, CallReturnAction, SetVariableAction, SpecifiedOutputParameterAbstraction, pcm_av_reliability_av_FailureOccurrenceDescription, parameter_av_pcm_av_AbstractNamedReference, pcm_av_parameter_av_VariableCharacterisation, pcm_av_parameter_av_CharacterisedVariable, Variable, pcm_av_reliability_av_HardwareInducedFailureType, ProcessingResourceType, pcm_av_reliability_av_SoftwareInducedFailureType, InternalFailureOccurrenceDescription, pcm_av_reliability_av_InternalFailureOccurrenceDescription, FailureOccurrenceDescription, InternalAction, SoftwareInducedFailureType, pcm_av_reliability_av_NetworkInducedFailureType, pcm_av_seff_av_AbstractAction, CommunicationLinkResourceType, pcm_av_reliability_av_ExternalFailureOccurrenceDescription, qos_reliability_av_SpecifiedReliabilityAnnotation, pcm_av_reliability_av_ResourceTimeoutFailureType, pcm_av_reliability_av_FailureType, pcm_av_seff_av_StopAction, AbstractInternalControlFlowAction, pcm_av_seff_av_AbstractInternalControlFlowAction, AbstractAction, pcm_av_seff_av_AbstractBranchTransition, BranchAction, ResourceDemandingBehaviour, pcm_av_seff_av_ResourceDemandingBehaviour, AbstractLoopAction, AbstractBranchTransition, pcm_av_seff_av_AbstractLoopAction, pcm_av_seff_av_ResourceDemandingSEFF, seff_av_ServiceEffectSpecification, pcm_av_seff_av_BranchAction, pcm_av_seff_av_CallAction, pcm_av_seff_av_StartAction, pcm_av_seff_av_ServiceEffectSpecification, pcm_av_seff_av_ExternalCallAction, seff_av_AbstractAction, seff_av_CallReturnAction, seff_reliability_av_FailureHandlingEntity, seff_av_ResourceDemandingBehaviour, ResourceDemandingInternalBehaviour, pcm_av_seff_av_ResourceDemandingInternalBehaviour, ResourceDemandingSEFF, pcm_av_seff_av_ReleaseAction, pcm_av_seff_av_LoopAction, pcm_av_seff_av_ForkAction, ForkedBehaviour, pcm_av_seff_av_ForkedBehaviour, ForkAction, pcm_av_seff_av_SynchronisationPoint, pcm_av_seff_av_CallReturnAction, pcm_av_seff_av_ProbabilisticBranchTransition, pcm_av_seff_av_AcquireAction, pcm_av_seff_av_CollectionIteratorAction, pcm_av_seff_av_GuardedBranchTransition, pcm_av_seff_av_SetVariableAction, pcm_av_seff_av_InternalCallAction, seff_av_CallAction, seff_av_AbstractInternalControlFlowAction, pcm_av_seff_av_EmitEventAction, pcm_av_seff_av_InternalAction, pcm_av_seff_performance_av_ResourceCall, pcm_av_seff_performance_av_InfrastructureCall, pcm_av_seff_reliability_av_RecoveryActionBehaviour, pcm_av_seff_performance_av_ParametricResourceDemand, pcm_av_seff_reliability_av_FailureHandlingEntity, seff_reliability_av_RecoveryActionBehaviour, seff_reliability_av_RecoveryAction, pcm_av_seff_reliability_av_RecoveryAction, pcm_av_qos_performance_av_SystemSpecifiedExecutionTime, SpecifiedExecutionTime, pcm_av_qosannotations_av_SpecifiedQoSAnnotation, QoSAnnotations, pcm_av_qosannotations_av_QoSAnnotations, System, SpecifiedQoSAnnotation, pcm_av_qosannotations_av_SpecifiedOutputParameterAbstraction, pcm_av_system_av_System, pcm_av_qos_performance_av_SpecifiedExecutionTime, pcm_av_qos_performance_av_ComponentSpecifiedExecutionTime, pcm_av_qos_reliability_av_SpecifiedReliabilityAnnotation, ExternalFailureOccurrenceDescription, pcm_av_resourceenvironment_av_ProcessingResourceSpecification, pcm_av_resourceenvironment_av_ResourceEnvironment, LinkingResource, ResourceContainer, pcm_av_resourceenvironment_av_LinkingResource, ResourceEnvironment, pcm_av_resourceenvironment_av_ResourceContainer, Allocation, pcm_av_allocation_av_Allocation, pcm_av_resourceenvironment_av_CommunicationLinkResourceSpecification, pcm_av_allocation_av_AllocationContext, pcm_av_completions_av_Completion, pcm_av_completions_av_CompletionRepository, Completion, pcm_av_completions_av_DelegatingExternalCallAction, ExternalCallAction, pcm_av_completions_av_NetworkDemandParametricResourceDemand, ParametricResourceDemand, AllocationContext, pcm_av_subsystem_av_SubSystem, repository_av_RepositoryComponent, ParameterModifier, ComponentType, PrimitiveTypeEnum, VariableCharacterisationType},
    associations={guardedBranchTransition_PCMRandomVariable12, children0, scopedObject1, scopedObject3, closedWorkload_PCMRandomVariable5, passiveResource_capacity_PCMRandomVariable6, variableCharacterisation_Specification7, infrastructureCall__PCMRandomVariable8, resourceCall__PCMRandomVariable9, parametricResourceDemand_PCMRandomVariable10, loopAction_PCMRandomVariable11, resourceRequiredRoles__ResourceInterfaceRequiringEntity27, specifiedExecutionTime_PCMRandomVariable13, eventChannelSinkConnector__FilterCondition14, assemblyEventConnector__FilterCondition15, loop_LoopIteration16, openWorkload_PCMRandomVariable17, delay_TimeSpecification18, communicationLinkResourceSpecifcation_throughput_PCMRandomVariable19, processingResourceSpecification_processingRate_PCMRandomVariable20, communicationLinkResourceSpecification_latency_PCMRandomVariable21, resourceInterfaceProvidingEntity__ResourceProvidedRole23, providedResourceInterface__ResourceProvidedRole24, providedRoles_InterfaceProvidingEntity25, requiredRoles_InterfaceRequiringEntity26, requiredResourceInterface__ResourceRequiredRole28, resourceInterfaceRequiringEntity__ResourceRequiredRole30, resourceProvidedRoles__ResourceInterfaceProvidingEntity31, parentStructure__Connector32, assemblyContexts__ComposedStructure33, resourceRequiredDelegationConnectors_ComposedStructure34, eventChannel__ComposedStructure35, connectors__ComposedStructure36, innerResourceRequiredRole_ResourceRequiredDelegationConnector37, outerResourceRequiredRole_ResourceRequiredDelegationConnector38, parentStructure_ResourceRequiredDelegationConnector41, eventGroup__EventChannel43, eventChannelSourceConnector__EventChannel44, eventChannelSinkConnector__EventChannel45, parentStructure__EventChannel47, sourceRole__EventChannelSourceRole49, assemblyContext__EventChannelSourceConnector50, eventChannel__EventChannelSourceConnector52, sinkRole__EventChannelSinkConnector54, filterCondition__EventChannelSinkConnector55, assemblyContext__EventChannelSinkConnector56, eventChannel__EventChannelSinkConnector59, innerProvidedRole_ProvidedDelegationConnector61, outerProvidedRole_ProvidedDelegationConnector62, assemblyContext_ProvidedDelegationConnector65, innerRequiredRole_RequiredDelegationConnector68, outerRequiredRole_RequiredDelegationConnector69, assemblyContext_RequiredDelegationConnector72, assemblyContext__SinkDelegationConnector107, requiringAssemblyContext_AssemblyConnector75, providingAssemblyContext_AssemblyConnector77, providedRole_AssemblyConnector80, requiredRole_AssemblyConnector83, sinkRole__AssemblyEventConnector86, sourceRole__AssemblyEventConnector88, sinkAssemblyContext__AssemblyEventConnector91, sourceAssemblyContext__AssemblyEventConnector94, filterCondition__AssemblyEventConnector97, innerSourceRole__SourceRole99, outerSourceRole__SourceRole101, assemblyContext__SourceDelegationConnector104, configParameterUsages__AssemblyContext151, innerSinkRole__SinkRole109, outerSinkRole__SinkRole112, providedRole__AssemblyInfrastructureConnector115, requiredRole__AssemblyInfrastructureConnector116, providingAssemblyContext__AssemblyInfrastructureConnector118, requiringAssemblyContext__AssemblyInfrastructureConnector121, innerProvidedRole__ProvidedInfrastructureDelegationConnector124, outerProvidedRole__ProvidedInfrastructureDelegationConnector126, assemblyContext__ProvidedInfrastructureDelegationConnector129, innerRequiredRole__RequiredInfrastructureDelegationConnector132, outerRequiredRole__RequiredInfrastructureDelegationConnector134, assemblyContext__RequiredInfrastructureDelegationConnector137, assemblyContext__RequiredResourceDelegationConnector140, innerRequiredRole__RequiredResourceDelegationConnector142, outerRequiredRole__RequiredResourceDelegationConnector145, parentStructure__AssemblyContext148, encapsulatedComponent__AssemblyContext150, providedRole_EntryLevelSystemCall165, operationSignature__EntryLevelSystemCall167, outputParameterUsages_EntryLevelSystemCall169, usageScenario_Workload152, usageModel_UsageScenario153, scenarioBehaviour_UsageScenario154, workload_UsageScenario155, assemblyContext_userData156, usageModel_UserData158, userDataParameterUsages_UserData160, usageScenario_UsageModel162, userData_UsageModel164, inputParameterUsages_EntryLevelSystemCall171, successor173, predecessor174, scenarioBehaviour_AbstractUserAction176, usageScenario_SenarioBehaviour178, branchTransition_ScenarioBehaviour180, loop_ScenarioBehaviour181, actions_ScenarioBehaviour183, branch_BranchTransition185, branchedBehaviour_BranchTransition186, branchTransitions_Branch188, loopIteration_Loop190, bodyBehaviour_Loop192, interArrivalTime_OpenWorkload194, timeSpecification_Delay196, thinkTime_ClosedWorkload198, capacity_PassiveResource200, basicComponent_PassiveResource202, resourceTimeoutFailureType__PassiveResource203, serviceEffectSpecifications__BasicComponent204, passiveResource_BasicComponent205, infrastructureSignature__Parameter214, operationSignature__Parameter215, parentCompleteComponentTypes207, componentParameterUsage_ImplementationComponentType208, repository__RepositoryComponent211, providingEntity_ProvidedRole212, dataType__Parameter213, eventType__Parameter217, resourceSignature__Parameter218, repository__DataType219, components__Repository221, interfaces__Repository223, failureTypes__Repository224, dataTypes__Repository225, parameters__InfrastructureSignature247, parentInterfaces__Interface227, protocols__Interface229, requiredCharacterisations231, repository__Interface232, parameter234, interface_RequiredCharacterisation235, eventTypes__EventGroup237, parameter__EventType239, eventGroup__EventType241, exceptions__Signature243, failureType244, signatures__OperationInterface260, infrastructureInterface__InfrastructureSignature249, infrastructureSignatures__InfrastructureInterface250, requiredInterface__InfrastructureRequiredRole252, requiringEntity_RequiredRole254, interface__OperationSignature255, parameters__OperationSignature256, returnType__OperationSignature258, parentProvidesComponentTypes272, requiredInterface__OperationRequiredRole262, eventGroup__SourceRole264, eventGroup__SinkRole266, providedInterface__OperationProvidedRole268, providedInterface__InfrastructureProvidedRole270, parameter__ResourceSignature281, innerType_CollectionDataType273, parentType_CompositeDataType275, innerDeclaration_CompositeDataType276, datatype_InnerDeclaration277, compositeDataType_InnerDeclaration279, resourceSignatures__ResourceInterface296, resourceInterface__ResourceSignature283, hardwareInducedFailureType__ProcessingResourceType285, resourceRepository_ResourceType286, resourceInterfaces__ResourceRepository287, schedulingPolicies__ResourceRepository289, availableResourceTypes_ResourceRepository290, resourceRepository__SchedulingPolicy291, networkInducedFailureType__CommunicationLinkResourceType293, resourceRepository__ResourceInterface294, assemblyContext__VariableUsage307, variableCharacterisation_VariableUsage298, userData_VariableUsage300, callAction__VariableUsage302, synchronisationPoint_VariableUsage303, callReturnAction__VariableUsage304, setVariableAction_VariableUsage305, specifiedOutputParameterAbstraction_expectedExternalOutputs_VariableUsage306, entryLevelSystemCall_InputParameterUsage309, entryLevelSystemCall_OutputParameterUsage310, namedReference__VariableUsage312, specification_VariableCharacterisation313, variableUsage_VariableCharacterisation315, processingResourceType__HardwareInducedFailureType317, internalFailureOccurrenceDescriptions__SoftwareInducedFailureType318, internalAction__InternalFailureOccurrenceDescription319, softwareInducedFailureType__InternalFailureOccurrenceDescription320, resourceCall__Action333, predecessor_AbstractAction335, communicationLinkResourceType__NetworkInducedFailureType321, specifiedReliabilityAnnotation__ExternalFailureOccurrenceDescription322, failureType__ExternalFailureOccurrenceDescription323, passiveResource__ResourceTimeoutFailureType325, repository__FailureType327, resourceDemand_Action329, infrastructureCall__Action331, bodyBehaviour_Loop344, branchAction_AbstractBranchTransition346, branchBehaviour_BranchTransition347, successor_AbstractAction336, resourceDemandingBehaviour_AbstractAction338, abstractLoopAction_ResourceDemandingBehaviour339, abstractBranchTransition_ResourceDemandingBehaviour341, steps_Behaviour342, describedService__SEFF353, basicComponent_ServiceEffectSpecification354, branches_Branch349, inputVariableUsages__CallAction351, outputParameterUsage_SynchronisationPoint368, forkAction_SynchronisationPoint370, synchronousForkedBehaviours_SynchronisationPoint372, resourceDemandingInternalBehaviours356, resourceDemandingSEFF_ResourceDemandingInternalBehaviour357, passiveResource_ReleaseAction358, iterationCount_LoopAction360, asynchronousForkedBehaviours_ForkAction362, synchronisingBehaviours_ForkAction363, synchronisationPoint_ForkedBehaviour365, forkAction_ForkedBehaivour367, calledService_ExternalService374, role_ExternalService376, passiveresource_AcquireAction381, returnVariableUsage__CallReturnAction379, parameter_CollectionIteratorAction383, branchCondition_GuardedBranchTransition385, localVariableUsages_SetVariableAction387, calledResourceDemandingInternalBehaviour389, eventType__EmitEventAction391, sourceRole__EmitEventAction393, action__InfrastructureCall402, requiredRole__InfrastructureCall403, internalFailureOccurrenceDescriptions__InternalAction396, signature__InfrastructureCall398, numberOfCalls__InfrastructureCall400, specification_ParametericResourceDemand415, requiredResource_ParametricResourceDemand417, action_ParametricResourceDemand419, action__ResourceCall406, resourceRequiredRole__ResourceCall408, signature__ResourceCall410, numberOfCalls__ResourceCall413, primaryBehaviour__RecoveryAction423, recoveryActionBehaviours__RecoveryAction425, failureTypes_FailureHandlingEntity426, failureHandlingAlternatives__RecoveryActionBehaviour421, recoveryAction__RecoveryActionBehaviour422, qosAnnotations_SpecifiedOutputParameterAbstraction444, signature_SpecifiedQoSAnnation428, role_SpecifiedQoSAnnotation430, qosAnnotations_SpecifiedQoSAnnotation432, specifiedOutputParameterAbstractions_QoSAnnotations433, system_QoSAnnotations435, specifiedQoSAnnotations_QoSAnnotations436, signature_SpecifiedOutputParameterAbstraction437, role_SpecifiedOutputParameterAbstraction439, expectedExternalOutputs_SpecifiedOutputParameterAbstraction442, externalFailureOccurrenceDescriptions__SpecifiedReliabilityAnnotation450, specification_SpecifiedExecutionTime446, assemblyContext_ComponentSpecifiedExecutionTime448, qosAnnotations_System451, linkingResources__ResourceEnvironment453, resourceContainer_ResourceEnvironment454, connectedResourceContainers_LinkingResource455, communicationLinkResourceSpecifications_LinkingResource457, resourceEnvironment_LinkingResource459, activeResourceSpecifications_ResourceContainer460, resourceEnvironment_ResourceContainer462, nestedResourceContainers__ResourceContainer464, parentResourceContainer__ResourceContainer466, resourceContainer_AllocationContext485, assemblyContext_AllocationContext487, allocation_AllocationContext490, eventChannel__AllocationContext491, schedulingPolicy468, activeResourceType_ActiveResourceSpecification470, processingRate_ProcessingResourceSpecification473, resourceContainer_ProcessingResourceSpecification475, linkingResource_CommunicationLinkResourceSpecification477, communicationLinkResourceType_CommunicationLinkResourceSpecification479, latency_CommunicationLinkResourceSpecification481, throughput_CommunicationLinkResourceSpecification483, completions_CompletionRepository499, targetResourceEnvironment_Allocation493, system_Allocation495, allocationContexts_Allocation498, requiredCommunicationLinkResource_ParametricResourceDemand500},
    generalizations={gen_pcm_av_core_av_PCMRandomVariable_RandomVariable, gen_pcm_av_entity_av_ResourceInterfaceRequiringEntity_Entity, gen_pcm_av_entity_av_ResourceRequiredRole_Role, gen_pcm_av_entity_av_ResourceProvidedRole_Role, gen_pcm_av_entity_av_InterfaceProvidingRequiringEntity_entity_av_InterfaceProvidingEntity, gen_pcm_av_entity_av_InterfaceProvidingRequiringEntity_entity_av_InterfaceRequiringEntity, gen_pcm_av_entity_av_InterfaceProvidingEntity_Entity, gen_pcm_av_entity_av_InterfaceRequiringEntity_entity_av_Entity, gen_pcm_av_entity_av_InterfaceRequiringEntity_entity_av_ResourceInterfaceRequiringEntity, gen_pcm_av_entity_av_ResourceInterfaceProvidingEntity_Entity, gen_pcm_av_entity_av_ComposedProvidingRequiringEntity_composition_av_ComposedStructure, gen_pcm_av_entity_av_ComposedProvidingRequiringEntity_entity_av_InterfaceProvidingRequiringEntity, gen_pcm_av_entity_av_ResourceInterfaceProvidingRequiringEntity_entity_av_ResourceInterfaceRequiringEntity, gen_pcm_av_entity_av_ResourceInterfaceProvidingRequiringEntity_entity_av_ResourceInterfaceProvidingEntity, gen_pcm_av_entity_av_Entity_Identifier, gen_pcm_av_entity_av_Entity_entity_av_NamedElement, gen_pcm_av_composition_av_DelegationConnector_Connector, gen_pcm_av_composition_av_Connector_Entity, gen_pcm_av_composition_av_ComposedStructure_Entity, gen_pcm_av_composition_av_ProvidedDelegationConnector_DelegationConnector, gen_pcm_av_composition_av_EventChannel_Entity, gen_pcm_av_composition_av_EventChannelSourceConnector_Connector, gen_pcm_av_composition_av_EventChannelSinkConnector_Connector, gen_pcm_av_composition_av_RequiredDelegationConnector_DelegationConnector, gen_pcm_av_composition_av_AssemblyConnector_Connector, gen_pcm_av_composition_av_SinkDelegationConnector_DelegationConnector, gen_pcm_av_composition_av_AssemblyEventConnector_Connector, gen_pcm_av_composition_av_SourceDelegationConnector_DelegationConnector, gen_pcm_av_composition_av_AssemblyInfrastructureConnector_Connector, gen_pcm_av_composition_av_ProvidedInfrastructureDelegationConnector_DelegationConnector, gen_pcm_av_composition_av_RequiredInfrastructureDelegationConnector_DelegationConnector, gen_pcm_av_composition_av_RequiredResourceDelegationConnector_DelegationConnector, gen_pcm_av_composition_av_AssemblyContext_Entity, gen_pcm_av_usagemodel_av_UsageScenario_Entity, gen_pcm_av_usagemodel_av_EntryLevelSystemCall_AbstractUserAction, gen_pcm_av_usagemodel_av_AbstractUserAction_Entity, gen_pcm_av_usagemodel_av_ScenarioBehaviour_Entity, gen_pcm_av_usagemodel_av_Branch_AbstractUserAction, gen_pcm_av_usagemodel_av_Loop_AbstractUserAction, gen_pcm_av_usagemodel_av_Stop_AbstractUserAction, gen_pcm_av_usagemodel_av_Start_AbstractUserAction, gen_pcm_av_usagemodel_av_OpenWorkload_Workload, gen_pcm_av_usagemodel_av_Delay_AbstractUserAction, gen_pcm_av_usagemodel_av_ClosedWorkload_Workload, gen_pcm_av_repository_av_PassiveResource_Entity, gen_pcm_av_repository_av_BasicComponent_ImplementationComponentType, gen_pcm_av_repository_av_ImplementationComponentType_RepositoryComponent, gen_pcm_av_repository_av_RepositoryComponent_InterfaceProvidingRequiringEntity, gen_pcm_av_repository_av_ProvidedRole_Role, gen_pcm_av_repository_av_Repository_Entity, gen_pcm_av_repository_av_Interface_Entity, gen_pcm_av_repository_av_InfrastructureSignature_Signature, gen_pcm_av_repository_av_EventGroup_Interface, gen_pcm_av_repository_av_EventType_Signature, gen_pcm_av_repository_av_Signature_Entity, gen_pcm_av_repository_av_OperationRequiredRole_RequiredRole, gen_pcm_av_repository_av_InfrastructureInterface_Interface, gen_pcm_av_repository_av_InfrastructureRequiredRole_RequiredRole, gen_pcm_av_repository_av_RequiredRole_Role, gen_pcm_av_repository_av_OperationSignature_Signature, gen_pcm_av_repository_av_OperationInterface_Interface, gen_pcm_av_repository_av_ProvidesComponentType_RepositoryComponent, gen_pcm_av_repository_av_SourceRole_RequiredRole, gen_pcm_av_repository_av_SinkRole_ProvidedRole, gen_pcm_av_repository_av_OperationProvidedRole_ProvidedRole, gen_pcm_av_repository_av_InfrastructureProvidedRole_ProvidedRole, gen_pcm_av_repository_av_CompleteComponentType_RepositoryComponent, gen_pcm_av_repository_av_PrimitiveDataType_DataType, gen_pcm_av_repository_av_CompositeComponent_entity_av_ComposedProvidingRequiringEntity, gen_pcm_av_repository_av_CompositeComponent_repository_av_ImplementationComponentType, gen_pcm_av_resourcetype_av_ResourceSignature_Entity, gen_pcm_av_repository_av_CollectionDataType_entity_av_Entity, gen_pcm_av_repository_av_CollectionDataType_repository_av_DataType, gen_pcm_av_repository_av_CompositeDataType_entity_av_Entity, gen_pcm_av_repository_av_CompositeDataType_repository_av_DataType, gen_pcm_av_repository_av_InnerDeclaration_NamedElement, gen_pcm_av_repository_av_Role_Entity, gen_pcm_av_resourcetype_av_ProcessingResourceType_ResourceType, gen_pcm_av_resourcetype_av_ResourceType_entity_av_Entity, gen_pcm_av_resourcetype_av_ResourceType_UnitCarryingElement, gen_pcm_av_resourcetype_av_ResourceType_entity_av_ResourceInterfaceProvidingEntity, gen_pcm_av_resourcetype_av_SchedulingPolicy_Entity, gen_pcm_av_resourcetype_av_CommunicationLinkResourceType_ResourceType, gen_pcm_av_resourcetype_av_ResourceInterface_Entity, gen_pcm_av_parameter_av_CharacterisedVariable_Variable, gen_pcm_av_reliability_av_HardwareInducedFailureType_FailureType, gen_pcm_av_reliability_av_SoftwareInducedFailureType_FailureType, gen_pcm_av_reliability_av_InternalFailureOccurrenceDescription_FailureOccurrenceDescription, gen_pcm_av_reliability_av_NetworkInducedFailureType_FailureType, gen_pcm_av_seff_av_AbstractAction_Entity, gen_pcm_av_reliability_av_ExternalFailureOccurrenceDescription_FailureOccurrenceDescription, gen_pcm_av_reliability_av_ResourceTimeoutFailureType_SoftwareInducedFailureType, gen_pcm_av_reliability_av_FailureType_Entity, gen_pcm_av_seff_av_StopAction_AbstractInternalControlFlowAction, gen_pcm_av_seff_av_AbstractInternalControlFlowAction_AbstractAction, gen_pcm_av_seff_av_AbstractBranchTransition_Entity, gen_pcm_av_seff_av_ResourceDemandingBehaviour_Identifier, gen_pcm_av_seff_av_AbstractLoopAction_AbstractInternalControlFlowAction, gen_pcm_av_seff_av_ResourceDemandingSEFF_Identifier, gen_pcm_av_seff_av_ResourceDemandingSEFF_seff_av_ServiceEffectSpecification, gen_pcm_av_seff_av_BranchAction_AbstractInternalControlFlowAction, gen_pcm_av_seff_av_StartAction_AbstractInternalControlFlowAction, gen_pcm_av_seff_av_ExternalCallAction_seff_av_AbstractAction, gen_pcm_av_seff_av_ExternalCallAction_seff_av_CallReturnAction, gen_pcm_av_seff_av_ExternalCallAction_seff_reliability_av_FailureHandlingEntity, gen_pcm_av_seff_av_ResourceDemandingSEFF_seff_av_ResourceDemandingBehaviour, gen_pcm_av_seff_av_ResourceDemandingInternalBehaviour_ResourceDemandingBehaviour, gen_pcm_av_seff_av_ReleaseAction_AbstractInternalControlFlowAction, gen_pcm_av_seff_av_LoopAction_AbstractLoopAction, gen_pcm_av_seff_av_ForkAction_AbstractInternalControlFlowAction, gen_pcm_av_seff_av_ForkedBehaviour_ResourceDemandingBehaviour, gen_pcm_av_seff_av_CallReturnAction_CallAction, gen_pcm_av_seff_av_ProbabilisticBranchTransition_AbstractBranchTransition, gen_pcm_av_seff_av_AcquireAction_AbstractInternalControlFlowAction, gen_pcm_av_seff_av_CollectionIteratorAction_AbstractLoopAction, gen_pcm_av_seff_av_GuardedBranchTransition_AbstractBranchTransition, gen_pcm_av_seff_av_SetVariableAction_AbstractInternalControlFlowAction, gen_pcm_av_seff_av_InternalCallAction_seff_av_CallAction, gen_pcm_av_seff_av_InternalCallAction_seff_av_AbstractInternalControlFlowAction, gen_pcm_av_seff_av_EmitEventAction_seff_av_AbstractAction, gen_pcm_av_seff_av_EmitEventAction_seff_av_CallAction, gen_pcm_av_seff_av_InternalAction_AbstractInternalControlFlowAction, gen_pcm_av_seff_performance_av_ResourceCall_CallAction, gen_pcm_av_seff_performance_av_InfrastructureCall_CallAction, gen_pcm_av_seff_reliability_av_RecoveryActionBehaviour_seff_reliability_av_FailureHandlingEntity, gen_pcm_av_seff_reliability_av_RecoveryActionBehaviour_seff_av_ResourceDemandingBehaviour, gen_pcm_av_seff_reliability_av_FailureHandlingEntity_Entity, gen_pcm_av_seff_reliability_av_RecoveryAction_AbstractInternalControlFlowAction, gen_pcm_av_qos_performance_av_SystemSpecifiedExecutionTime_SpecifiedExecutionTime, gen_pcm_av_qosannotations_av_QoSAnnotations_Entity, gen_pcm_av_system_av_System_entity_av_Entity, gen_pcm_av_system_av_System_entity_av_ComposedProvidingRequiringEntity, gen_pcm_av_qos_performance_av_SpecifiedExecutionTime_SpecifiedQoSAnnotation, gen_pcm_av_qos_performance_av_ComponentSpecifiedExecutionTime_SpecifiedExecutionTime, gen_pcm_av_qos_reliability_av_SpecifiedReliabilityAnnotation_SpecifiedQoSAnnotation, gen_pcm_av_resourceenvironment_av_ProcessingResourceSpecification_Identifier, gen_pcm_av_resourceenvironment_av_ResourceEnvironment_NamedElement, gen_pcm_av_resourceenvironment_av_LinkingResource_Entity, gen_pcm_av_resourceenvironment_av_ResourceContainer_Entity, gen_pcm_av_resourceenvironment_av_CommunicationLinkResourceSpecification_Identifier, gen_pcm_av_allocation_av_AllocationContext_Entity, gen_pcm_av_completions_av_Completion_entity_av_ComposedProvidingRequiringEntity, gen_pcm_av_completions_av_Completion_repository_av_ImplementationComponentType, gen_pcm_av_completions_av_DelegatingExternalCallAction_ExternalCallAction, gen_pcm_av_completions_av_NetworkDemandParametricResourceDemand_ParametricResourceDemand, gen_pcm_av_allocation_av_Allocation_Entity, gen_pcm_av_subsystem_av_SubSystem_entity_av_ComposedProvidingRequiringEntity, gen_pcm_av_subsystem_av_SubSystem_repository_av_RepositoryComponent},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)