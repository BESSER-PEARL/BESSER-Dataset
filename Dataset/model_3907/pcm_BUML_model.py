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

SchedulingPolicy: Enumeration = Enumeration(
    name="SchedulingPolicy",
    literals={
            EnumerationLiteral(name="DELAY"),
			EnumerationLiteral(name="PROCESSOR_SHARING"),
			EnumerationLiteral(name="FCFS")
    }
)

# Classes
pcm_core_PCMRandomVariable = Class(name="pcm_core_PCMRandomVariable")
RandomVariable = Class(name="RandomVariable")
pcm_entity_Entity = Class(name="pcm_entity_Entity", is_abstract=True)
Identifier = Class(name="Identifier")
entity_NamedElement = Class(name="entity_NamedElement")
pcm_entity_NamedElement = Class(name="pcm_entity_NamedElement", is_abstract=True)
pcm_entity_InterfaceProvidingEntity = Class(name="pcm_entity_InterfaceProvidingEntity", is_abstract=True)
Entity = Class(name="Entity")
ProvidedRole = Class(name="ProvidedRole")
pcm_entity_InterfaceProvidingRequiringEntity = Class(name="pcm_entity_InterfaceProvidingRequiringEntity", is_abstract=True)
entity_InterfaceProvidingEntity = Class(name="entity_InterfaceProvidingEntity")
entity_InterfaceRequiringEntity = Class(name="entity_InterfaceRequiringEntity")
entity_ResourceInterfaceRequiringEntity = Class(name="entity_ResourceInterfaceRequiringEntity")
RequiredRole = Class(name="RequiredRole")
pcm_entity_ResourceInterfaceRequiringEntity = Class(name="pcm_entity_ResourceInterfaceRequiringEntity", is_abstract=True)
ResourceRequiredRole = Class(name="ResourceRequiredRole")
pcm_entity_ComposedProvidingRequiringEntity = Class(name="pcm_entity_ComposedProvidingRequiringEntity", is_abstract=True)
composition_ComposedStructure = Class(name="composition_ComposedStructure")
entity_InterfaceProvidingRequiringEntity = Class(name="entity_InterfaceProvidingRequiringEntity")
pcm_connectors_Connector = Class(name="pcm_connectors_Connector", is_abstract=True)
pcm_composition_ProvidedDelegationConnector = Class(name="pcm_composition_ProvidedDelegationConnector")
DelegationConnector = Class(name="DelegationConnector")
pcm_entity_InterfaceRequiringEntity = Class(name="pcm_entity_InterfaceRequiringEntity", is_abstract=True)
composition_AssemblyContext = Class(name="composition_AssemblyContext")
pcm_composition_AssemblyContext = Class(name="pcm_composition_AssemblyContext")
RepositoryComponent = Class(name="RepositoryComponent")
VariableUsage = Class(name="VariableUsage")
pcm_composition_RequiredDelegationConnector = Class(name="pcm_composition_RequiredDelegationConnector")
pcm_composition_AssemblyConnector = Class(name="pcm_composition_AssemblyConnector")
Connector = Class(name="Connector")
pcm_composition_ResourceRequiredDelegationConnector = Class(name="pcm_composition_ResourceRequiredDelegationConnector")
pcm_composition_ComposedStructure = Class(name="pcm_composition_ComposedStructure", is_abstract=True)
composition_RequiredDelegationConnector = Class(name="composition_RequiredDelegationConnector")
composition_AssemblyConnector = Class(name="composition_AssemblyConnector")
composition_ResourceRequiredDelegationConnector = Class(name="composition_ResourceRequiredDelegationConnector")
pcm_repository_PassiveResource = Class(name="pcm_repository_PassiveResource")
PCMRandomVariable = Class(name="PCMRandomVariable")
pcm_repository_Signature = Class(name="pcm_repository_Signature")
Parameter_ = Class(name="Parameter")
composition_ProvidedDelegationConnector = Class(name="composition_ProvidedDelegationConnector")
DataType = Class(name="DataType")
ExceptionType = Class(name="ExceptionType")
pcm_repository_Parameter = Class(name="pcm_repository_Parameter")
Signature = Class(name="Signature")
pcm_repository_DataType = Class(name="pcm_repository_DataType", is_abstract=True)
Repository = Class(name="Repository")
pcm_repository_Repository = Class(name="pcm_repository_Repository")
Interface = Class(name="Interface")
pcm_repository_RepositoryComponent = Class(name="pcm_repository_RepositoryComponent", is_abstract=True)
InterfaceProvidingRequiringEntity = Class(name="InterfaceProvidingRequiringEntity")
pcm_repository_RequiredRole = Class(name="pcm_repository_RequiredRole")
Role = Class(name="Role")
pcm_repository_Role = Class(name="pcm_repository_Role", is_abstract=True)
pcm_repository_Interface = Class(name="pcm_repository_Interface")
Protocol = Class(name="Protocol")
pcm_repository_ResourceRequiredRole = Class(name="pcm_repository_ResourceRequiredRole")
pcm_repository_ExceptionType = Class(name="pcm_repository_ExceptionType")
pcm_repository_ProvidesComponentType = Class(name="pcm_repository_ProvidesComponentType")
pcm_repository_ImplementationComponentType = Class(name="pcm_repository_ImplementationComponentType", is_abstract=True)
CompleteComponentType = Class(name="CompleteComponentType")
pcm_repository_CompleteComponentType = Class(name="pcm_repository_CompleteComponentType")
pcm_repository_DelegationConnector = Class(name="pcm_repository_DelegationConnector", is_abstract=True)
pcm_repository_CompositeComponent = Class(name="pcm_repository_CompositeComponent")
entity_ComposedProvidingRequiringEntity = Class(name="entity_ComposedProvidingRequiringEntity")
repository_ImplementationComponentType = Class(name="repository_ImplementationComponentType")
pcm_repository_BasicComponent = Class(name="pcm_repository_BasicComponent")
ImplementationComponentType = Class(name="ImplementationComponentType")
ProvidesComponentType = Class(name="ProvidesComponentType")
ServiceEffectSpecification = Class(name="ServiceEffectSpecification")
PassiveResource = Class(name="PassiveResource")
pcm_repository_PrimitiveDataType = Class(name="pcm_repository_PrimitiveDataType")
pcm_repository_CollectionDataType = Class(name="pcm_repository_CollectionDataType")
entity_Entity = Class(name="entity_Entity")
repository_DataType = Class(name="repository_DataType")
pcm_repository_CompositeDataType = Class(name="pcm_repository_CompositeDataType")
CompositeDataType = Class(name="CompositeDataType")
InnerDeclaration = Class(name="InnerDeclaration")
pcm_repository_ProvidedRole = Class(name="pcm_repository_ProvidedRole")
pcm_protocol_ServiceCall = Class(name="pcm_protocol_ServiceCall", is_abstract=True)
pcm_protocol_Protocol = Class(name="pcm_protocol_Protocol", is_abstract=True)
pcm_parameter_VariableCharacterisation = Class(name="pcm_parameter_VariableCharacterisation")
pcm_repository_InnerDeclaration = Class(name="pcm_repository_InnerDeclaration")
NamedElement = Class(name="NamedElement")
pcm_parameter_CharacterisedVariable = Class(name="pcm_parameter_CharacterisedVariable")
Variable = Class(name="Variable")
pcm_parameter_VariableUsage = Class(name="pcm_parameter_VariableUsage")
VariableCharacterisation = Class(name="VariableCharacterisation")
parameter_pcm_AbstractNamedReference = Class(name="parameter_pcm_AbstractNamedReference")
pcm_seff_StopAction = Class(name="pcm_seff_StopAction")
AbstractInternalControlFlowAction = Class(name="AbstractInternalControlFlowAction")
pcm_seff_AbstractInternalControlFlowAction = Class(name="pcm_seff_AbstractInternalControlFlowAction", is_abstract=True)
AbstractAction = Class(name="AbstractAction")
pcm_seff_AbstractAction = Class(name="pcm_seff_AbstractAction", is_abstract=True)
pcm_seff_StartAction = Class(name="pcm_seff_StartAction")
pcm_seff_ResourceDemandingSEFF = Class(name="pcm_seff_ResourceDemandingSEFF")
seff_ServiceEffectSpecification = Class(name="seff_ServiceEffectSpecification")
seff_ResourceDemandingBehaviour = Class(name="seff_ResourceDemandingBehaviour")
pcm_seff_ResourceDemandingBehaviour = Class(name="pcm_seff_ResourceDemandingBehaviour")
performance_ParametricResourceDemand = Class(name="performance_ParametricResourceDemand")
pcm_seff_ForkAction = Class(name="pcm_seff_ForkAction")
pcm_seff_ReleaseAction = Class(name="pcm_seff_ReleaseAction")
pcm_seff_LoopAction = Class(name="pcm_seff_LoopAction")
AbstractLoopAction = Class(name="AbstractLoopAction")
pcm_seff_AbstractLoopAction = Class(name="pcm_seff_AbstractLoopAction", is_abstract=True)
ResourceDemandingBehaviour = Class(name="ResourceDemandingBehaviour")
pcm_seff_InternalAction = Class(name="pcm_seff_InternalAction")
pcm_seff_AbstractBranchTransition = Class(name="pcm_seff_AbstractBranchTransition", is_abstract=True)
ForkedBehaviour = Class(name="ForkedBehaviour")
SynchronisationPoint = Class(name="SynchronisationPoint")
pcm_seff_ForkedBehaviour = Class(name="pcm_seff_ForkedBehaviour")
pcm_seff_SynchronisationPoint = Class(name="pcm_seff_SynchronisationPoint")
pcm_seff_ExternalCallAction = Class(name="pcm_seff_ExternalCallAction")
pcm_seff_ProbabilisticBranchTransition = Class(name="pcm_seff_ProbabilisticBranchTransition")
AbstractBranchTransition = Class(name="AbstractBranchTransition")
pcm_seff_SetVariableAction = Class(name="pcm_seff_SetVariableAction")
pcm_seff_BranchAction = Class(name="pcm_seff_BranchAction")
pcm_seff_AcquireAction = Class(name="pcm_seff_AcquireAction")
pcm_seff_CollectionIteratorAction = Class(name="pcm_seff_CollectionIteratorAction")
pcm_seff_GuardedBranchTransition = Class(name="pcm_seff_GuardedBranchTransition")
pcm_allocation_AllocationContext = Class(name="pcm_allocation_AllocationContext")
ResourceContainer = Class(name="ResourceContainer")
pcm_seff_ServiceEffectSpecification = Class(name="pcm_seff_ServiceEffectSpecification", is_abstract=True)
pcm_performance_ParametricResourceDemand = Class(name="pcm_performance_ParametricResourceDemand")
ProcessingResourceType = Class(name="ProcessingResourceType")
pcm_resourcetype_ResourceType = Class(name="pcm_resourcetype_ResourceType", is_abstract=True)
UnitCarryingElement = Class(name="UnitCarryingElement")
pcm_resourcetype_ResourceRepository = Class(name="pcm_resourcetype_ResourceRepository")
ResourceType = Class(name="ResourceType")
pcm_resourcetype_CommunicationLinkResourceType = Class(name="pcm_resourcetype_CommunicationLinkResourceType")
pcm_resourcetype_ProcessingResourceType = Class(name="pcm_resourcetype_ProcessingResourceType")
pcm_allocation_Allocation = Class(name="pcm_allocation_Allocation")
AllocationContext = Class(name="AllocationContext")
ResourceEnvironment = Class(name="ResourceEnvironment")
System = Class(name="System")
pcm_resourceenvironment_ResourceEnvironment = Class(name="pcm_resourceenvironment_ResourceEnvironment")
LinkingResource = Class(name="LinkingResource")
pcm_resourceenvironment_LinkingResource = Class(name="pcm_resourceenvironment_LinkingResource")
pcm_resourceenvironment_ResourceContainer = Class(name="pcm_resourceenvironment_ResourceContainer")
ProcessingResourceSpecification = Class(name="ProcessingResourceSpecification")
CommunicationLinkResourceSpecification = Class(name="CommunicationLinkResourceSpecification")
pcm_resourceenvironment_CommunicationLinkResourceSpecification = Class(name="pcm_resourceenvironment_CommunicationLinkResourceSpecification")
CommunicationLinkResourceType = Class(name="CommunicationLinkResourceType")
pcm_resourceenvironment_ProcessingResourceSpecification = Class(name="pcm_resourceenvironment_ProcessingResourceSpecification")
pcm_performance_ComponentSpecifiedExecutionTime = Class(name="pcm_performance_ComponentSpecifiedExecutionTime")
pcm_system_System = Class(name="pcm_system_System")
QoSAnnotations = Class(name="QoSAnnotations")
pcm_qosannotations_SpecifiedQoSAnnotation = Class(name="pcm_qosannotations_SpecifiedQoSAnnotation", is_abstract=True)
pcm_qosannotations_SpecifiedOutputParameterAbstraction = Class(name="pcm_qosannotations_SpecifiedOutputParameterAbstraction", is_abstract=True)
pcm_qosannotations_QoSAnnotations = Class(name="pcm_qosannotations_QoSAnnotations")
SpecifiedQoSAnnotation = Class(name="SpecifiedQoSAnnotation")
SpecifiedOutputParameterAbstraction = Class(name="SpecifiedOutputParameterAbstraction")
pcm_performance_SystemSpecifiedExecutionTime = Class(name="pcm_performance_SystemSpecifiedExecutionTime")
pcm_reliability_SpecifiedFailureProbability = Class(name="pcm_reliability_SpecifiedFailureProbability")
pcm_usagemodel_Workload = Class(name="pcm_usagemodel_Workload", is_abstract=True)
pcm_usagemodel_UsageScenario = Class(name="pcm_usagemodel_UsageScenario")
Workload = Class(name="Workload")
ScenarioBehaviour = Class(name="ScenarioBehaviour")
pcm_usagemodel_ScenarioBehaviour = Class(name="pcm_usagemodel_ScenarioBehaviour")
pcm_usagemodel_Start = Class(name="pcm_usagemodel_Start")
AbstractUserAction = Class(name="AbstractUserAction")
pcm_usagemodel_AbstractUserAction = Class(name="pcm_usagemodel_AbstractUserAction", is_abstract=True)
pcm_usagemodel_UsageModel = Class(name="pcm_usagemodel_UsageModel")
UsageScenario = Class(name="UsageScenario")
UserData = Class(name="UserData")
pcm_usagemodel_UserData = Class(name="pcm_usagemodel_UserData")
pcm_usagemodel_Stop = Class(name="pcm_usagemodel_Stop")
pcm_usagemodel_OpenWorkload = Class(name="pcm_usagemodel_OpenWorkload")
pcm_usagemodel_Loop = Class(name="pcm_usagemodel_Loop")
pcm_usagemodel_EntryLevelSystemCall = Class(name="pcm_usagemodel_EntryLevelSystemCall")
pcm_usagemodel_ClosedWorkload = Class(name="pcm_usagemodel_ClosedWorkload")
pcm_usagemodel_Branch = Class(name="pcm_usagemodel_Branch")
BranchTransition = Class(name="BranchTransition")
pcm_usagemodel_BranchTransition = Class(name="pcm_usagemodel_BranchTransition")
pcm_usagemodel_Delay = Class(name="pcm_usagemodel_Delay")
pcm_subsystem_SubSystem = Class(name="pcm_subsystem_SubSystem")
repository_RepositoryComponent = Class(name="repository_RepositoryComponent")

# pcm_core_PCMRandomVariable class attributes and methods
pcm_core_PCMRandomVariable_m_SpecificationMustNotBeNULL: Method = Method(name="SpecificationMustNotBeNULL", parameters={Parameter(name='pcm_diagnostics', type=StringType), Parameter(name='pcm_context', type=StringType)}, type=BooleanType)
pcm_core_PCMRandomVariable.methods={pcm_core_PCMRandomVariable_m_SpecificationMustNotBeNULL}

# RandomVariable class attributes and methods

# pcm_entity_Entity class attributes and methods

# Identifier class attributes and methods

# entity_NamedElement class attributes and methods

# pcm_entity_NamedElement class attributes and methods
pcm_entity_NamedElement_entityName: Property = Property(name="entityName", type=StringType)
pcm_entity_NamedElement.attributes={pcm_entity_NamedElement_entityName}

# pcm_entity_InterfaceProvidingEntity class attributes and methods

# Entity class attributes and methods

# ProvidedRole class attributes and methods

# pcm_entity_InterfaceProvidingRequiringEntity class attributes and methods

# entity_InterfaceProvidingEntity class attributes and methods

# entity_InterfaceRequiringEntity class attributes and methods

# entity_ResourceInterfaceRequiringEntity class attributes and methods

# RequiredRole class attributes and methods

# pcm_entity_ResourceInterfaceRequiringEntity class attributes and methods

# ResourceRequiredRole class attributes and methods

# pcm_entity_ComposedProvidingRequiringEntity class attributes and methods
pcm_entity_ComposedProvidingRequiringEntity_m_ProvidedRolesMustBeBound: Method = Method(name="ProvidedRolesMustBeBound", parameters={Parameter(name='pcm_diagnostics', type=StringType), Parameter(name='pcm_context', type=StringType)}, type=BooleanType)
pcm_entity_ComposedProvidingRequiringEntity.methods={pcm_entity_ComposedProvidingRequiringEntity_m_ProvidedRolesMustBeBound}

# composition_ComposedStructure class attributes and methods

# entity_InterfaceProvidingRequiringEntity class attributes and methods

# pcm_connectors_Connector class attributes and methods

# pcm_composition_ProvidedDelegationConnector class attributes and methods
pcm_composition_ProvidedDelegationConnector_m_ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure: Method = Method(name="ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure", parameters={Parameter(name='pcm_context', type=StringType), Parameter(name='pcm_diagnostics', type=StringType)}, type=BooleanType)
pcm_composition_ProvidedDelegationConnector_m_ComponentOfAssemblyContextAndInnerRoleProvidingComponentNeedToBeTheSame: Method = Method(name="ComponentOfAssemblyContextAndInnerRoleProvidingComponentNeedToBeTheSame", parameters={Parameter(name='pcm_context', type=StringType), Parameter(name='pcm_diagnostics', type=StringType)}, type=BooleanType)
pcm_composition_ProvidedDelegationConnector.methods={pcm_composition_ProvidedDelegationConnector_m_ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure, pcm_composition_ProvidedDelegationConnector_m_ComponentOfAssemblyContextAndInnerRoleProvidingComponentNeedToBeTheSame}

# DelegationConnector class attributes and methods

# pcm_entity_InterfaceRequiringEntity class attributes and methods

# composition_AssemblyContext class attributes and methods

# pcm_composition_AssemblyContext class attributes and methods

# RepositoryComponent class attributes and methods

# VariableUsage class attributes and methods

# pcm_composition_RequiredDelegationConnector class attributes and methods
pcm_composition_RequiredDelegationConnector_m_RequiredDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure: Method = Method(name="RequiredDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure", parameters={Parameter(name='pcm_diagnostics', type=StringType), Parameter(name='pcm_context', type=StringType)}, type=BooleanType)
pcm_composition_RequiredDelegationConnector_m_ComponentOfAssemblyContextAndInnerRoleRequiringComponentNeedToBeTheSame: Method = Method(name="ComponentOfAssemblyContextAndInnerRoleRequiringComponentNeedToBeTheSame", parameters={Parameter(name='pcm_context', type=StringType), Parameter(name='pcm_diagnostics', type=StringType)}, type=BooleanType)
pcm_composition_RequiredDelegationConnector.methods={pcm_composition_RequiredDelegationConnector_m_ComponentOfAssemblyContextAndInnerRoleRequiringComponentNeedToBeTheSame, pcm_composition_RequiredDelegationConnector_m_RequiredDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure}

# pcm_composition_AssemblyConnector class attributes and methods
pcm_composition_AssemblyConnector_m_AssemblyConnectorsReferencedProvidedRolesAndChildContextMustMatch: Method = Method(name="AssemblyConnectorsReferencedProvidedRolesAndChildContextMustMatch", parameters={Parameter(name='pcm_diagnostics', type=StringType), Parameter(name='pcm_context', type=StringType)}, type=BooleanType)
pcm_composition_AssemblyConnector_m_AssemblyConnectorsReferencedRequiredRoleAndChildContextMustMatch: Method = Method(name="AssemblyConnectorsReferencedRequiredRoleAndChildContextMustMatch", parameters={Parameter(name='pcm_diagnostics', type=StringType), Parameter(name='pcm_context', type=StringType)}, type=BooleanType)
pcm_composition_AssemblyConnector.methods={pcm_composition_AssemblyConnector_m_AssemblyConnectorsReferencedRequiredRoleAndChildContextMustMatch, pcm_composition_AssemblyConnector_m_AssemblyConnectorsReferencedProvidedRolesAndChildContextMustMatch}

# Connector class attributes and methods

# pcm_composition_ResourceRequiredDelegationConnector class attributes and methods

# pcm_composition_ComposedStructure class attributes and methods

# composition_RequiredDelegationConnector class attributes and methods

# composition_AssemblyConnector class attributes and methods

# composition_ResourceRequiredDelegationConnector class attributes and methods

# pcm_repository_PassiveResource class attributes and methods

# PCMRandomVariable class attributes and methods

# pcm_repository_Signature class attributes and methods
pcm_repository_Signature_serviceName: Property = Property(name="serviceName", type=StringType)
pcm_repository_Signature_m_ParameterNamesHaveToBeUniqueForASignature: Method = Method(name="ParameterNamesHaveToBeUniqueForASignature", parameters={Parameter(name='pcm_diagnostics', type=StringType), Parameter(name='pcm_context', type=StringType)}, type=BooleanType)
pcm_repository_Signature.attributes={pcm_repository_Signature_serviceName}
pcm_repository_Signature.methods={pcm_repository_Signature_m_ParameterNamesHaveToBeUniqueForASignature}

# Parameter class attributes and methods

# composition_ProvidedDelegationConnector class attributes and methods

# DataType class attributes and methods

# ExceptionType class attributes and methods

# pcm_repository_Parameter class attributes and methods
pcm_repository_Parameter_parameterName: Property = Property(name="parameterName", type=StringType)
pcm_repository_Parameter_modifier__Parameter: Property = Property(name="modifier__Parameter", type=StringType)
pcm_repository_Parameter.attributes={pcm_repository_Parameter_modifier__Parameter, pcm_repository_Parameter_parameterName}

# Signature class attributes and methods

# pcm_repository_DataType class attributes and methods

# Repository class attributes and methods

# pcm_repository_Repository class attributes and methods
pcm_repository_Repository_repositoryDescription: Property = Property(name="repositoryDescription", type=StringType)
pcm_repository_Repository.attributes={pcm_repository_Repository_repositoryDescription}

# Interface class attributes and methods

# pcm_repository_RepositoryComponent class attributes and methods

# InterfaceProvidingRequiringEntity class attributes and methods

# pcm_repository_RequiredRole class attributes and methods

# Role class attributes and methods

# pcm_repository_Role class attributes and methods

# pcm_repository_Interface class attributes and methods
pcm_repository_Interface_m_NoProtocolTypeIDUsedTwice: Method = Method(name="NoProtocolTypeIDUsedTwice", parameters={Parameter(name='pcm_context', type=StringType), Parameter(name='pcm_diagnostics', type=StringType)}, type=BooleanType)
pcm_repository_Interface_m_SignaturesHaveToBeUniqueForAnInterface: Method = Method(name="SignaturesHaveToBeUniqueForAnInterface", parameters={Parameter(name='pcm_context', type=StringType), Parameter(name='pcm_diagnostics', type=StringType)}, type=BooleanType)
pcm_repository_Interface.methods={pcm_repository_Interface_m_SignaturesHaveToBeUniqueForAnInterface, pcm_repository_Interface_m_NoProtocolTypeIDUsedTwice}

# Protocol class attributes and methods

# pcm_repository_ResourceRequiredRole class attributes and methods

# pcm_repository_ExceptionType class attributes and methods
pcm_repository_ExceptionType_exceptionName: Property = Property(name="exceptionName", type=StringType)
pcm_repository_ExceptionType_exceptionMessage: Property = Property(name="exceptionMessage", type=StringType)
pcm_repository_ExceptionType.attributes={pcm_repository_ExceptionType_exceptionName, pcm_repository_ExceptionType_exceptionMessage}

# pcm_repository_ProvidesComponentType class attributes and methods
pcm_repository_ProvidesComponentType_m_AtLeastOneInterfaceHasToBeProvidedByAUsefullProvidesComponentType: Method = Method(name="AtLeastOneInterfaceHasToBeProvidedByAUsefullProvidesComponentType", parameters={Parameter(name='pcm_context', type=StringType), Parameter(name='pcm_diagnostics', type=StringType)}, type=BooleanType)
pcm_repository_ProvidesComponentType.methods={pcm_repository_ProvidesComponentType_m_AtLeastOneInterfaceHasToBeProvidedByAUsefullProvidesComponentType}

# pcm_repository_ImplementationComponentType class attributes and methods
pcm_repository_ImplementationComponentType_m_providedInterfacesHaveToConformToCompleteType: Method = Method(name="providedInterfacesHaveToConformToCompleteType", parameters={Parameter(name='pcm_diagnostics', type=StringType), Parameter(name='pcm_context', type=StringType)}, type=BooleanType)
pcm_repository_ImplementationComponentType_m_RequiredInterfacesHaveToConformToCompleteType: Method = Method(name="RequiredInterfacesHaveToConformToCompleteType", parameters={Parameter(name='pcm_diagnostics', type=StringType), Parameter(name='pcm_context', type=StringType)}, type=BooleanType)
pcm_repository_ImplementationComponentType.methods={pcm_repository_ImplementationComponentType_m_providedInterfacesHaveToConformToCompleteType, pcm_repository_ImplementationComponentType_m_RequiredInterfacesHaveToConformToCompleteType}

# CompleteComponentType class attributes and methods

# pcm_repository_CompleteComponentType class attributes and methods
pcm_repository_CompleteComponentType_m_AtLeastOneInterfaceHasToBeProvidedOrRequiredByAUsefullCompleteComponentType: Method = Method(name="AtLeastOneInterfaceHasToBeProvidedOrRequiredByAUsefullCompleteComponentType", parameters={Parameter(name='pcm_diagnostics', type=StringType), Parameter(name='pcm_context', type=StringType)}, type=BooleanType)
pcm_repository_CompleteComponentType_m_providedInterfacesHaveToConformToProvidedType2: Method = Method(name="providedInterfacesHaveToConformToProvidedType2", parameters={Parameter(name='pcm_context', type=StringType), Parameter(name='pcm_diagnostics', type=StringType)}, type=BooleanType)
pcm_repository_CompleteComponentType.methods={pcm_repository_CompleteComponentType_m_providedInterfacesHaveToConformToProvidedType2, pcm_repository_CompleteComponentType_m_AtLeastOneInterfaceHasToBeProvidedOrRequiredByAUsefullCompleteComponentType}

# pcm_repository_DelegationConnector class attributes and methods

# pcm_repository_CompositeComponent class attributes and methods
pcm_repository_CompositeComponent_m_ProvideSameInterfaces: Method = Method(name="ProvideSameInterfaces", parameters={Parameter(name='pcm_context', type=StringType), Parameter(name='pcm_diagnostics', type=StringType)}, type=BooleanType)
pcm_repository_CompositeComponent_m_RequireSameInterfaces: Method = Method(name="RequireSameInterfaces", parameters={Parameter(name='pcm_diagnostics', type=StringType), Parameter(name='pcm_context', type=StringType)}, type=BooleanType)
pcm_repository_CompositeComponent.methods={pcm_repository_CompositeComponent_m_RequireSameInterfaces, pcm_repository_CompositeComponent_m_ProvideSameInterfaces}

# entity_ComposedProvidingRequiringEntity class attributes and methods

# repository_ImplementationComponentType class attributes and methods

# pcm_repository_BasicComponent class attributes and methods
pcm_repository_BasicComponent_m_NoSeffTypeUsedTwice: Method = Method(name="NoSeffTypeUsedTwice", parameters={Parameter(name='pcm_diagnostics', type=StringType), Parameter(name='pcm_context', type=StringType)}, type=BooleanType)
pcm_repository_BasicComponent_m_ProvideSameInterfacesAsImplementationType: Method = Method(name="ProvideSameInterfacesAsImplementationType", parameters={Parameter(name='pcm_diagnostics', type=StringType), Parameter(name='pcm_context', type=StringType)}, type=BooleanType)
pcm_repository_BasicComponent_m_RequireSameInterfacesAsImplementationType: Method = Method(name="RequireSameInterfacesAsImplementationType", parameters={Parameter(name='pcm_context', type=StringType), Parameter(name='pcm_diagnostics', type=StringType)}, type=BooleanType)
pcm_repository_BasicComponent.methods={pcm_repository_BasicComponent_m_NoSeffTypeUsedTwice, pcm_repository_BasicComponent_m_RequireSameInterfacesAsImplementationType, pcm_repository_BasicComponent_m_ProvideSameInterfacesAsImplementationType}

# ImplementationComponentType class attributes and methods

# ProvidesComponentType class attributes and methods

# ServiceEffectSpecification class attributes and methods

# PassiveResource class attributes and methods

# pcm_repository_PrimitiveDataType class attributes and methods
pcm_repository_PrimitiveDataType_type: Property = Property(name="type", type=StringType)
pcm_repository_PrimitiveDataType.attributes={pcm_repository_PrimitiveDataType_type}

# pcm_repository_CollectionDataType class attributes and methods

# entity_Entity class attributes and methods

# repository_DataType class attributes and methods

# pcm_repository_CompositeDataType class attributes and methods

# CompositeDataType class attributes and methods

# InnerDeclaration class attributes and methods

# pcm_repository_ProvidedRole class attributes and methods

# pcm_protocol_ServiceCall class attributes and methods

# pcm_protocol_Protocol class attributes and methods
pcm_protocol_Protocol_protocolTypeID: Property = Property(name="protocolTypeID", type=StringType)
pcm_protocol_Protocol.attributes={pcm_protocol_Protocol_protocolTypeID}

# pcm_parameter_VariableCharacterisation class attributes and methods
pcm_parameter_VariableCharacterisation_type: Property = Property(name="type", type=StringType)
pcm_parameter_VariableCharacterisation.attributes={pcm_parameter_VariableCharacterisation_type}

# pcm_repository_InnerDeclaration class attributes and methods

# NamedElement class attributes and methods

# pcm_parameter_CharacterisedVariable class attributes and methods
pcm_parameter_CharacterisedVariable_characterisationType: Property = Property(name="characterisationType", type=StringType)
pcm_parameter_CharacterisedVariable.attributes={pcm_parameter_CharacterisedVariable_characterisationType}

# Variable class attributes and methods

# pcm_parameter_VariableUsage class attributes and methods

# VariableCharacterisation class attributes and methods

# parameter_pcm_AbstractNamedReference class attributes and methods

# pcm_seff_StopAction class attributes and methods
pcm_seff_StopAction_m_StopActionSuccessorMustNotBeDefined: Method = Method(name="StopActionSuccessorMustNotBeDefined", parameters={Parameter(name='pcm_context', type=StringType), Parameter(name='pcm_diagnostics', type=StringType)}, type=BooleanType)
pcm_seff_StopAction.methods={pcm_seff_StopAction_m_StopActionSuccessorMustNotBeDefined}

# AbstractInternalControlFlowAction class attributes and methods

# pcm_seff_AbstractInternalControlFlowAction class attributes and methods

# AbstractAction class attributes and methods

# pcm_seff_AbstractAction class attributes and methods

# pcm_seff_StartAction class attributes and methods
pcm_seff_StartAction_m_StartActionPredecessorMustNotBeDefined: Method = Method(name="StartActionPredecessorMustNotBeDefined", parameters={Parameter(name='pcm_context', type=StringType), Parameter(name='pcm_diagnostics', type=StringType)}, type=BooleanType)
pcm_seff_StartAction.methods={pcm_seff_StartAction_m_StartActionPredecessorMustNotBeDefined}

# pcm_seff_ResourceDemandingSEFF class attributes and methods

# seff_ServiceEffectSpecification class attributes and methods

# seff_ResourceDemandingBehaviour class attributes and methods

# pcm_seff_ResourceDemandingBehaviour class attributes and methods
pcm_seff_ResourceDemandingBehaviour_m_ExactlyOneStartAction: Method = Method(name="ExactlyOneStartAction", parameters={Parameter(name='pcm_diagnostics', type=StringType), Parameter(name='pcm_context', type=StringType)}, type=BooleanType)
pcm_seff_ResourceDemandingBehaviour_m_ExactlyOneStopAction: Method = Method(name="ExactlyOneStopAction", parameters={Parameter(name='pcm_diagnostics', type=StringType), Parameter(name='pcm_context', type=StringType)}, type=BooleanType)
pcm_seff_ResourceDemandingBehaviour_m_EachActionExceptStartActionandStopActionMustHhaveAPredecessorAndSuccessor: Method = Method(name="EachActionExceptStartActionandStopActionMustHhaveAPredecessorAndSuccessor", parameters={Parameter(name='pcm_diagnostics', type=StringType), Parameter(name='pcm_context', type=StringType)}, type=BooleanType)
pcm_seff_ResourceDemandingBehaviour.methods={pcm_seff_ResourceDemandingBehaviour_m_ExactlyOneStopAction, pcm_seff_ResourceDemandingBehaviour_m_EachActionExceptStartActionandStopActionMustHhaveAPredecessorAndSuccessor, pcm_seff_ResourceDemandingBehaviour_m_ExactlyOneStartAction}

# performance_ParametricResourceDemand class attributes and methods

# pcm_seff_ForkAction class attributes and methods

# pcm_seff_ReleaseAction class attributes and methods

# pcm_seff_LoopAction class attributes and methods

# AbstractLoopAction class attributes and methods

# pcm_seff_AbstractLoopAction class attributes and methods

# ResourceDemandingBehaviour class attributes and methods

# pcm_seff_InternalAction class attributes and methods
pcm_seff_InternalAction_failureProbability: Property = Property(name="failureProbability", type=FloatType)
pcm_seff_InternalAction.attributes={pcm_seff_InternalAction_failureProbability}

# pcm_seff_AbstractBranchTransition class attributes and methods

# ForkedBehaviour class attributes and methods

# SynchronisationPoint class attributes and methods

# pcm_seff_ForkedBehaviour class attributes and methods

# pcm_seff_SynchronisationPoint class attributes and methods

# pcm_seff_ExternalCallAction class attributes and methods
pcm_seff_ExternalCallAction_retryCount: Property = Property(name="retryCount", type=IntegerType)
pcm_seff_ExternalCallAction.attributes={pcm_seff_ExternalCallAction_retryCount}

# pcm_seff_ProbabilisticBranchTransition class attributes and methods
pcm_seff_ProbabilisticBranchTransition_branchProbability: Property = Property(name="branchProbability", type=FloatType)
pcm_seff_ProbabilisticBranchTransition.attributes={pcm_seff_ProbabilisticBranchTransition_branchProbability}

# AbstractBranchTransition class attributes and methods

# pcm_seff_SetVariableAction class attributes and methods

# pcm_seff_BranchAction class attributes and methods
pcm_seff_BranchAction_m_EitherGuardedBranchesOrProbabilisiticBranchTransitions: Method = Method(name="EitherGuardedBranchesOrProbabilisiticBranchTransitions", parameters={Parameter(name='pcm_diagnostics', type=StringType), Parameter(name='pcm_context', type=StringType)}, type=BooleanType)
pcm_seff_BranchAction_m_AllProbabilisticBranchProbabilitiesMustSumUpTo1: Method = Method(name="AllProbabilisticBranchProbabilitiesMustSumUpTo1", parameters={Parameter(name='pcm_diagnostics', type=StringType), Parameter(name='pcm_context', type=StringType)}, type=BooleanType)
pcm_seff_BranchAction.methods={pcm_seff_BranchAction_m_EitherGuardedBranchesOrProbabilisiticBranchTransitions, pcm_seff_BranchAction_m_AllProbabilisticBranchProbabilitiesMustSumUpTo1}

# pcm_seff_AcquireAction class attributes and methods

# pcm_seff_CollectionIteratorAction class attributes and methods

# pcm_seff_GuardedBranchTransition class attributes and methods

# pcm_allocation_AllocationContext class attributes and methods

# ResourceContainer class attributes and methods

# pcm_seff_ServiceEffectSpecification class attributes and methods
pcm_seff_ServiceEffectSpecification_seffTypeID: Property = Property(name="seffTypeID", type=StringType)
pcm_seff_ServiceEffectSpecification.attributes={pcm_seff_ServiceEffectSpecification_seffTypeID}

# pcm_performance_ParametricResourceDemand class attributes and methods

# ProcessingResourceType class attributes and methods

# pcm_resourcetype_ResourceType class attributes and methods

# UnitCarryingElement class attributes and methods

# pcm_resourcetype_ResourceRepository class attributes and methods

# ResourceType class attributes and methods

# pcm_resourcetype_CommunicationLinkResourceType class attributes and methods

# pcm_resourcetype_ProcessingResourceType class attributes and methods

# pcm_allocation_Allocation class attributes and methods
pcm_allocation_Allocation_m_EachAssemblyContextWithinSystemHasToBeAllocatedExactlyOnce: Method = Method(name="EachAssemblyContextWithinSystemHasToBeAllocatedExactlyOnce", parameters={Parameter(name='pcm_context', type=StringType), Parameter(name='pcm_diagnostics', type=StringType)}, type=BooleanType)
pcm_allocation_Allocation.methods={pcm_allocation_Allocation_m_EachAssemblyContextWithinSystemHasToBeAllocatedExactlyOnce}

# AllocationContext class attributes and methods

# ResourceEnvironment class attributes and methods

# System class attributes and methods

# pcm_resourceenvironment_ResourceEnvironment class attributes and methods

# LinkingResource class attributes and methods

# pcm_resourceenvironment_LinkingResource class attributes and methods

# pcm_resourceenvironment_ResourceContainer class attributes and methods

# ProcessingResourceSpecification class attributes and methods

# CommunicationLinkResourceSpecification class attributes and methods

# pcm_resourceenvironment_CommunicationLinkResourceSpecification class attributes and methods
pcm_resourceenvironment_CommunicationLinkResourceSpecification_failureProbability: Property = Property(name="failureProbability", type=FloatType)
pcm_resourceenvironment_CommunicationLinkResourceSpecification.attributes={pcm_resourceenvironment_CommunicationLinkResourceSpecification_failureProbability}

# CommunicationLinkResourceType class attributes and methods

# pcm_resourceenvironment_ProcessingResourceSpecification class attributes and methods
pcm_resourceenvironment_ProcessingResourceSpecification_MTTR: Property = Property(name="MTTR", type=FloatType)
pcm_resourceenvironment_ProcessingResourceSpecification_MTTF: Property = Property(name="MTTF", type=FloatType)
pcm_resourceenvironment_ProcessingResourceSpecification_schedulingPolicy: Property = Property(name="schedulingPolicy", type=StringType)
pcm_resourceenvironment_ProcessingResourceSpecification.attributes={pcm_resourceenvironment_ProcessingResourceSpecification_schedulingPolicy, pcm_resourceenvironment_ProcessingResourceSpecification_MTTR, pcm_resourceenvironment_ProcessingResourceSpecification_MTTF}

# pcm_performance_ComponentSpecifiedExecutionTime class attributes and methods

# pcm_system_System class attributes and methods

# QoSAnnotations class attributes and methods

# pcm_qosannotations_SpecifiedQoSAnnotation class attributes and methods

# pcm_qosannotations_SpecifiedOutputParameterAbstraction class attributes and methods

# pcm_qosannotations_QoSAnnotations class attributes and methods

# SpecifiedQoSAnnotation class attributes and methods

# SpecifiedOutputParameterAbstraction class attributes and methods

# pcm_performance_SystemSpecifiedExecutionTime class attributes and methods

# pcm_reliability_SpecifiedFailureProbability class attributes and methods
pcm_reliability_SpecifiedFailureProbability_failureProbability: Property = Property(name="failureProbability", type=FloatType)
pcm_reliability_SpecifiedFailureProbability.attributes={pcm_reliability_SpecifiedFailureProbability_failureProbability}

# pcm_usagemodel_Workload class attributes and methods

# pcm_usagemodel_UsageScenario class attributes and methods

# Workload class attributes and methods

# ScenarioBehaviour class attributes and methods

# pcm_usagemodel_ScenarioBehaviour class attributes and methods
pcm_usagemodel_ScenarioBehaviour_m_EachuseractionexceptStartandStopmusthaveapredecessorandsuccessor: Method = Method(name="EachuseractionexceptStartandStopmusthaveapredecessorandsuccessor", parameters={Parameter(name='pcm_context', type=StringType), Parameter(name='pcm_diagnostics', type=StringType)}, type=BooleanType)
pcm_usagemodel_ScenarioBehaviour_m_Exactlyonestart: Method = Method(name="Exactlyonestart", parameters={Parameter(name='pcm_diagnostics', type=StringType), Parameter(name='pcm_context', type=StringType)}, type=BooleanType)
pcm_usagemodel_ScenarioBehaviour_m_Exactlyonestop: Method = Method(name="Exactlyonestop", parameters={Parameter(name='pcm_diagnostics', type=StringType), Parameter(name='pcm_context', type=StringType)}, type=BooleanType)
pcm_usagemodel_ScenarioBehaviour.methods={pcm_usagemodel_ScenarioBehaviour_m_Exactlyonestart, pcm_usagemodel_ScenarioBehaviour_m_EachuseractionexceptStartandStopmusthaveapredecessorandsuccessor, pcm_usagemodel_ScenarioBehaviour_m_Exactlyonestop}

# pcm_usagemodel_Start class attributes and methods
pcm_usagemodel_Start_m_StartHasNoPredecessor: Method = Method(name="StartHasNoPredecessor", parameters={Parameter(name='pcm_diagnostics', type=StringType), Parameter(name='pcm_context', type=StringType)}, type=BooleanType)
pcm_usagemodel_Start.methods={pcm_usagemodel_Start_m_StartHasNoPredecessor}

# AbstractUserAction class attributes and methods

# pcm_usagemodel_AbstractUserAction class attributes and methods

# pcm_usagemodel_UsageModel class attributes and methods

# UsageScenario class attributes and methods

# UserData class attributes and methods

# pcm_usagemodel_UserData class attributes and methods

# pcm_usagemodel_Stop class attributes and methods
pcm_usagemodel_Stop_m_StopHasNoSuccessor: Method = Method(name="StopHasNoSuccessor", parameters={Parameter(name='pcm_context', type=StringType), Parameter(name='pcm_diagnostics', type=StringType)}, type=BooleanType)
pcm_usagemodel_Stop.methods={pcm_usagemodel_Stop_m_StopHasNoSuccessor}

# pcm_usagemodel_OpenWorkload class attributes and methods
pcm_usagemodel_OpenWorkload_m_InterArrivalTimeInOpenWorkloadNeedsToBeSpecified: Method = Method(name="InterArrivalTimeInOpenWorkloadNeedsToBeSpecified", parameters={Parameter(name='pcm_diagnostics', type=StringType), Parameter(name='pcm_context', type=StringType)}, type=BooleanType)
pcm_usagemodel_OpenWorkload.methods={pcm_usagemodel_OpenWorkload_m_InterArrivalTimeInOpenWorkloadNeedsToBeSpecified}

# pcm_usagemodel_Loop class attributes and methods

# pcm_usagemodel_EntryLevelSystemCall class attributes and methods

# pcm_usagemodel_ClosedWorkload class attributes and methods
pcm_usagemodel_ClosedWorkload_population: Property = Property(name="population", type=IntegerType)
pcm_usagemodel_ClosedWorkload_m_PopulationInClosedWorkloadNeedsToBeSpecified: Method = Method(name="PopulationInClosedWorkloadNeedsToBeSpecified", parameters={Parameter(name='pcm_context', type=StringType), Parameter(name='pcm_diagnostics', type=StringType)}, type=BooleanType)
pcm_usagemodel_ClosedWorkload_m_ThinkTimeInClosedWorkloadNeedsToBeSpecified: Method = Method(name="ThinkTimeInClosedWorkloadNeedsToBeSpecified", parameters={Parameter(name='pcm_diagnostics', type=StringType), Parameter(name='pcm_context', type=StringType)}, type=BooleanType)
pcm_usagemodel_ClosedWorkload.attributes={pcm_usagemodel_ClosedWorkload_population}
pcm_usagemodel_ClosedWorkload.methods={pcm_usagemodel_ClosedWorkload_m_PopulationInClosedWorkloadNeedsToBeSpecified, pcm_usagemodel_ClosedWorkload_m_ThinkTimeInClosedWorkloadNeedsToBeSpecified}

# pcm_usagemodel_Branch class attributes and methods
pcm_usagemodel_Branch_m_AllBranchProbabilitiesMustSumUpTo1: Method = Method(name="AllBranchProbabilitiesMustSumUpTo1", parameters={Parameter(name='pcm_context', type=StringType), Parameter(name='pcm_diagnostics', type=StringType)}, type=BooleanType)
pcm_usagemodel_Branch.methods={pcm_usagemodel_Branch_m_AllBranchProbabilitiesMustSumUpTo1}

# BranchTransition class attributes and methods

# pcm_usagemodel_BranchTransition class attributes and methods
pcm_usagemodel_BranchTransition_branchProbability: Property = Property(name="branchProbability", type=FloatType)
pcm_usagemodel_BranchTransition.attributes={pcm_usagemodel_BranchTransition_branchProbability}

# pcm_usagemodel_Delay class attributes and methods

# pcm_subsystem_SubSystem class attributes and methods

# repository_RepositoryComponent class attributes and methods

# Relationships
providedRoles_InterfaceProvidingEntity0: BinaryAssociation = BinaryAssociation(
    name="providedRoles_InterfaceProvidingEntity0",
    ends={
        Property(name="ProvidedRole", type=pcm_entity_InterfaceProvidingEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="providingEntity_ProvidedRole", type=ProvidedRole, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredRoles_InterfaceRequiringEntity1: BinaryAssociation = BinaryAssociation(
    name="requiredRoles_InterfaceRequiringEntity1",
    ends={
        Property(name="RequiredRole", type=pcm_entity_InterfaceRequiringEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="requiringEntity_RequiredRole", type=RequiredRole, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceRequiredRoles_ResourceInterfaceRequiringEntity2: BinaryAssociation = BinaryAssociation(
    name="resourceRequiredRoles_ResourceInterfaceRequiringEntity2",
    ends={
        Property(name="ResourceRequiredRole", type=pcm_entity_ResourceInterfaceRequiringEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceRequiringEntity_ResourceRequiredRole", type=ResourceRequiredRole, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
innerProvidedRole_ProvidedDelegationConnector3: BinaryAssociation = BinaryAssociation(
    name="innerProvidedRole_ProvidedDelegationConnector3",
    ends={
        Property(name="ProvidedRole4", type=pcm_composition_ProvidedDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_composition_ProvidedDelegationConnector", type=ProvidedRole, multiplicity=Multiplicity(1, 1))
    }
)
outerProvidedRole_ProvidedDelegationConnector5: BinaryAssociation = BinaryAssociation(
    name="outerProvidedRole_ProvidedDelegationConnector5",
    ends={
        Property(name="ProvidedRole7", type=pcm_composition_ProvidedDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_composition_ProvidedDelegationConnector6", type=ProvidedRole, multiplicity=Multiplicity(1, 1))
    }
)
assemblyContext_ProvidedDelegationConnector8: BinaryAssociation = BinaryAssociation(
    name="assemblyContext_ProvidedDelegationConnector8",
    ends={
        Property(name="composition_AssemblyContext", type=pcm_composition_ProvidedDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_composition_ProvidedDelegationConnector9", type=composition_AssemblyContext, multiplicity=Multiplicity(1, 1))
    }
)
parentStructure_ProvidedDelegationConnector10: BinaryAssociation = BinaryAssociation(
    name="parentStructure_ProvidedDelegationConnector10",
    ends={
        Property(name="ComposedStructure", type=pcm_composition_ProvidedDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="providedDelegationConnectors_ComposedStructure", type=composition_ComposedStructure, multiplicity=Multiplicity(1, 1))
    }
)
encapsulatedComponent_AssemblyContext11: BinaryAssociation = BinaryAssociation(
    name="encapsulatedComponent_AssemblyContext11",
    ends={
        Property(name="RepositoryComponent", type=pcm_composition_AssemblyContext, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_composition_AssemblyContext", type=RepositoryComponent, multiplicity=Multiplicity(1, 1))
    }
)
parentStructure_AssemblyContext12: BinaryAssociation = BinaryAssociation(
    name="parentStructure_AssemblyContext12",
    ends={
        Property(name="ComposedStructure13", type=pcm_composition_AssemblyContext, multiplicity=Multiplicity(1, 1)),
        Property(name="assemblyContexts_ComposedStructure", type=composition_ComposedStructure, multiplicity=Multiplicity(1, 1))
    }
)
configParameterUsages_AssemblyContext14: BinaryAssociation = BinaryAssociation(
    name="configParameterUsages_AssemblyContext14",
    ends={
        Property(name="VariableUsage", type=pcm_composition_AssemblyContext, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_composition_AssemblyContext15", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
innerRequiredRole_RequiredDelegationConnector16: BinaryAssociation = BinaryAssociation(
    name="innerRequiredRole_RequiredDelegationConnector16",
    ends={
        Property(name="RequiredRole17", type=pcm_composition_RequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_composition_RequiredDelegationConnector", type=RequiredRole, multiplicity=Multiplicity(1, 1))
    }
)
outerRequiredRole_RequiredDelegationConnector18: BinaryAssociation = BinaryAssociation(
    name="outerRequiredRole_RequiredDelegationConnector18",
    ends={
        Property(name="RequiredRole20", type=pcm_composition_RequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_composition_RequiredDelegationConnector19", type=RequiredRole, multiplicity=Multiplicity(1, 1))
    }
)
assemblyContext_RequiredDelegationConnector21: BinaryAssociation = BinaryAssociation(
    name="assemblyContext_RequiredDelegationConnector21",
    ends={
        Property(name="composition_AssemblyContext23", type=pcm_composition_RequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_composition_RequiredDelegationConnector22", type=composition_AssemblyContext, multiplicity=Multiplicity(1, 1))
    }
)
parentStructure_RequiredDelegationConnector24: BinaryAssociation = BinaryAssociation(
    name="parentStructure_RequiredDelegationConnector24",
    ends={
        Property(name="ComposedStructure25", type=pcm_composition_RequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="requiredDelegationConnectors_ComposedStructure", type=composition_ComposedStructure, multiplicity=Multiplicity(1, 1))
    }
)
requiringAssemblyContext_AssemblyConnector26: BinaryAssociation = BinaryAssociation(
    name="requiringAssemblyContext_AssemblyConnector26",
    ends={
        Property(name="composition_AssemblyContext27", type=pcm_composition_AssemblyConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_composition_AssemblyConnector", type=composition_AssemblyContext, multiplicity=Multiplicity(1, 1))
    }
)
providingAssemblyContext_AssemblyConnector28: BinaryAssociation = BinaryAssociation(
    name="providingAssemblyContext_AssemblyConnector28",
    ends={
        Property(name="composition_AssemblyContext30", type=pcm_composition_AssemblyConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_composition_AssemblyConnector29", type=composition_AssemblyContext, multiplicity=Multiplicity(1, 1))
    }
)
providedRole_AssemblyConnector31: BinaryAssociation = BinaryAssociation(
    name="providedRole_AssemblyConnector31",
    ends={
        Property(name="ProvidedRole33", type=pcm_composition_AssemblyConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_composition_AssemblyConnector32", type=ProvidedRole, multiplicity=Multiplicity(1, 1))
    }
)
requiredRole_AssemblyConnector34: BinaryAssociation = BinaryAssociation(
    name="requiredRole_AssemblyConnector34",
    ends={
        Property(name="RequiredRole36", type=pcm_composition_AssemblyConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_composition_AssemblyConnector35", type=RequiredRole, multiplicity=Multiplicity(1, 1))
    }
)
parentStructure_AssemblyConnector37: BinaryAssociation = BinaryAssociation(
    name="parentStructure_AssemblyConnector37",
    ends={
        Property(name="ComposedStructure38", type=pcm_composition_AssemblyConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="assemblyConnectors_ComposedStructure", type=composition_ComposedStructure, multiplicity=Multiplicity(1, 1))
    }
)
parentStructure_ResourceRequiredDelegationConnector39: BinaryAssociation = BinaryAssociation(
    name="parentStructure_ResourceRequiredDelegationConnector39",
    ends={
        Property(name="ComposedStructure40", type=pcm_composition_ResourceRequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceRequiredDelegationConnectors_ComposedStructure", type=composition_ComposedStructure, multiplicity=Multiplicity(1, 1))
    }
)
innerResourceRequiredRole_ResourceRequiredDelegationConnector41: BinaryAssociation = BinaryAssociation(
    name="innerResourceRequiredRole_ResourceRequiredDelegationConnector41",
    ends={
        Property(name="ResourceRequiredRole42", type=pcm_composition_ResourceRequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_composition_ResourceRequiredDelegationConnector", type=ResourceRequiredRole, multiplicity=Multiplicity(1, 1))
    }
)
outerResourceRequiredRole_ResourceRequiredDelegationConnector43: BinaryAssociation = BinaryAssociation(
    name="outerResourceRequiredRole_ResourceRequiredDelegationConnector43",
    ends={
        Property(name="ResourceRequiredRole45", type=pcm_composition_ResourceRequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_composition_ResourceRequiredDelegationConnector44", type=ResourceRequiredRole, multiplicity=Multiplicity(1, 1))
    }
)
assemblyContexts_ComposedStructure46: BinaryAssociation = BinaryAssociation(
    name="assemblyContexts_ComposedStructure46",
    ends={
        Property(name="AssemblyContext", type=pcm_composition_ComposedStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="parentStructure_AssemblyContext", type=composition_AssemblyContext, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredDelegationConnectors_ComposedStructure48: BinaryAssociation = BinaryAssociation(
    name="requiredDelegationConnectors_ComposedStructure48",
    ends={
        Property(name="RequiredDelegationConnector", type=pcm_composition_ComposedStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="parentStructure_RequiredDelegationConnector", type=composition_RequiredDelegationConnector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
assemblyConnectors_ComposedStructure49: BinaryAssociation = BinaryAssociation(
    name="assemblyConnectors_ComposedStructure49",
    ends={
        Property(name="AssemblyConnector", type=pcm_composition_ComposedStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="parentStructure_AssemblyConnector", type=composition_AssemblyConnector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceRequiredDelegationConnectors_ComposedStructure50: BinaryAssociation = BinaryAssociation(
    name="resourceRequiredDelegationConnectors_ComposedStructure50",
    ends={
        Property(name="ResourceRequiredDelegationConnector", type=pcm_composition_ComposedStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="parentStructure_ResourceRequiredDelegationConnector", type=composition_ResourceRequiredDelegationConnector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
capacity_PassiveResource51: BinaryAssociation = BinaryAssociation(
    name="capacity_PassiveResource51",
    ends={
        Property(name="PCMRandomVariable", type=pcm_repository_PassiveResource, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_repository_PassiveResource", type=PCMRandomVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters__Signature52: BinaryAssociation = BinaryAssociation(
    name="parameters__Signature52",
    ends={
        Property(name="Parameter", type=pcm_repository_Signature, multiplicity=Multiplicity(1, 1)),
        Property(name="signature_Parameter", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
providedDelegationConnectors_ComposedStructure47: BinaryAssociation = BinaryAssociation(
    name="providedDelegationConnectors_ComposedStructure47",
    ends={
        Property(name="ProvidedDelegationConnector", type=pcm_composition_ComposedStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="parentStructure_ProvidedDelegationConnector", type=composition_ProvidedDelegationConnector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
interface_Signature53: BinaryAssociation = BinaryAssociation(
    name="interface_Signature53",
    ends={
        Property(name="Interface", type=pcm_repository_Signature, multiplicity=Multiplicity(1, 1)),
        Property(name="signatures__Interface", type=Interface, multiplicity=Multiplicity(1, 1))
    }
)
returntype__Signature54: BinaryAssociation = BinaryAssociation(
    name="returntype__Signature54",
    ends={
        Property(name="DataType", type=pcm_repository_Signature, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_repository_Signature", type=DataType, multiplicity=Multiplicity(0, 1))
    }
)
exceptions__Signature55: BinaryAssociation = BinaryAssociation(
    name="exceptions__Signature55",
    ends={
        Property(name="ExceptionType", type=pcm_repository_Signature, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_repository_Signature56", type=ExceptionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
datatype__Parameter57: BinaryAssociation = BinaryAssociation(
    name="datatype__Parameter57",
    ends={
        Property(name="DataType58", type=pcm_repository_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_repository_Parameter", type=DataType, multiplicity=Multiplicity(1, 1))
    }
)
signature_Parameter59: BinaryAssociation = BinaryAssociation(
    name="signature_Parameter59",
    ends={
        Property(name="Signature", type=pcm_repository_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameters__Signature", type=Signature, multiplicity=Multiplicity(1, 1))
    }
)
repository_DataType60: BinaryAssociation = BinaryAssociation(
    name="repository_DataType60",
    ends={
        Property(name="Repository", type=pcm_repository_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="datatypes_Repository", type=Repository, multiplicity=Multiplicity(1, 1))
    }
)
components__Repository61: BinaryAssociation = BinaryAssociation(
    name="components__Repository61",
    ends={
        Property(name="RepositoryComponent62", type=pcm_repository_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="repository_RepositoryComponent", type=RepositoryComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
interfaces__Repository63: BinaryAssociation = BinaryAssociation(
    name="interfaces__Repository63",
    ends={
        Property(name="Interface64", type=pcm_repository_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="repository_Interface", type=Interface, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
repository_RepositoryComponent67: BinaryAssociation = BinaryAssociation(
    name="repository_RepositoryComponent67",
    ends={
        Property(name="Repository68", type=pcm_repository_RepositoryComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="components__Repository", type=Repository, multiplicity=Multiplicity(1, 1))
    }
)
requiredInterface__RequiredRole69: BinaryAssociation = BinaryAssociation(
    name="requiredInterface__RequiredRole69",
    ends={
        Property(name="Interface70", type=pcm_repository_RequiredRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_repository_RequiredRole", type=Interface, multiplicity=Multiplicity(1, 1))
    }
)
requiringEntity_RequiredRole71: BinaryAssociation = BinaryAssociation(
    name="requiringEntity_RequiredRole71",
    ends={
        Property(name="InterfaceRequiringEntity", type=pcm_repository_RequiredRole, multiplicity=Multiplicity(1, 1)),
        Property(name="requiredRoles_InterfaceRequiringEntity", type=entity_InterfaceRequiringEntity, multiplicity=Multiplicity(1, 1))
    }
)
parentInterface__Interface72: BinaryAssociation = BinaryAssociation(
    name="parentInterface__Interface72",
    ends={
        Property(name="Interface73", type=pcm_repository_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_repository_Interface", type=Interface, multiplicity=Multiplicity(0, 9999))
    }
)
datatypes_Repository65: BinaryAssociation = BinaryAssociation(
    name="datatypes_Repository65",
    ends={
        Property(name="DataType66", type=pcm_repository_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="repository_DataType", type=DataType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
protocols__Interface77: BinaryAssociation = BinaryAssociation(
    name="protocols__Interface77",
    ends={
        Property(name="Protocol", type=pcm_repository_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_repository_Interface78", type=Protocol, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
signatures__Interface79: BinaryAssociation = BinaryAssociation(
    name="signatures__Interface79",
    ends={
        Property(name="Signature80", type=pcm_repository_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="interface_Signature", type=Signature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
repository_Interface81: BinaryAssociation = BinaryAssociation(
    name="repository_Interface81",
    ends={
        Property(name="Repository82", type=pcm_repository_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="interfaces__Repository", type=Repository, multiplicity=Multiplicity(1, 1))
    }
)
requiredInterface_ResourceRequiredRole83: BinaryAssociation = BinaryAssociation(
    name="requiredInterface_ResourceRequiredRole83",
    ends={
        Property(name="Interface84", type=pcm_repository_ResourceRequiredRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_repository_ResourceRequiredRole", type=Interface, multiplicity=Multiplicity(1, 1))
    }
)
resourceRequiringEntity_ResourceRequiredRole85: BinaryAssociation = BinaryAssociation(
    name="resourceRequiringEntity_ResourceRequiredRole85",
    ends={
        Property(name="ResourceInterfaceRequiringEntity", type=pcm_repository_ResourceRequiredRole, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceRequiredRoles_ResourceInterfaceRequiringEntity", type=entity_ResourceInterfaceRequiringEntity, multiplicity=Multiplicity(1, 1))
    }
)
ancestorInterfaces_Interface74: BinaryAssociation = BinaryAssociation(
    name="ancestorInterfaces_Interface74",
    ends={
        Property(name="Interface76", type=pcm_repository_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_repository_Interface75", type=Interface, multiplicity=Multiplicity(0, 9999))
    }
)
parentCompleteComponentTypes86: BinaryAssociation = BinaryAssociation(
    name="parentCompleteComponentTypes86",
    ends={
        Property(name="CompleteComponentType", type=pcm_repository_ImplementationComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_repository_ImplementationComponentType", type=CompleteComponentType, multiplicity=Multiplicity(0, 9999))
    }
)
componentParameterUsage_ImplementationComponentType87: BinaryAssociation = BinaryAssociation(
    name="componentParameterUsage_ImplementationComponentType87",
    ends={
        Property(name="VariableUsage89", type=pcm_repository_ImplementationComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_repository_ImplementationComponentType88", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentProvidesComponentTypes90: BinaryAssociation = BinaryAssociation(
    name="parentProvidesComponentTypes90",
    ends={
        Property(name="ProvidesComponentType", type=pcm_repository_CompleteComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_repository_CompleteComponentType", type=ProvidesComponentType, multiplicity=Multiplicity(0, 9999))
    }
)
serviceEffectSpecifications__BasicComponent91: BinaryAssociation = BinaryAssociation(
    name="serviceEffectSpecifications__BasicComponent91",
    ends={
        Property(name="ServiceEffectSpecification", type=pcm_repository_BasicComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_repository_BasicComponent", type=ServiceEffectSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
passiveResource_BasicComponent92: BinaryAssociation = BinaryAssociation(
    name="passiveResource_BasicComponent92",
    ends={
        Property(name="PassiveResource", type=pcm_repository_BasicComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_repository_BasicComponent93", type=PassiveResource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
innerType_CollectionDataType94: BinaryAssociation = BinaryAssociation(
    name="innerType_CollectionDataType94",
    ends={
        Property(name="DataType95", type=pcm_repository_CollectionDataType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_repository_CollectionDataType", type=DataType, multiplicity=Multiplicity(1, 1))
    }
)
parentType_CompositeDataType96: BinaryAssociation = BinaryAssociation(
    name="parentType_CompositeDataType96",
    ends={
        Property(name="CompositeDataType", type=pcm_repository_CompositeDataType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_repository_CompositeDataType", type=CompositeDataType, multiplicity=Multiplicity(0, 9999))
    }
)
innerDeclaration_CompositeDataType97: BinaryAssociation = BinaryAssociation(
    name="innerDeclaration_CompositeDataType97",
    ends={
        Property(name="InnerDeclaration", type=pcm_repository_CompositeDataType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_repository_CompositeDataType98", type=InnerDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
datatype_InnerDeclaration99: BinaryAssociation = BinaryAssociation(
    name="datatype_InnerDeclaration99",
    ends={
        Property(name="DataType100", type=pcm_repository_InnerDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_repository_InnerDeclaration", type=DataType, multiplicity=Multiplicity(1, 1))
    }
)
providedInterface__ProvidedRole101: BinaryAssociation = BinaryAssociation(
    name="providedInterface__ProvidedRole101",
    ends={
        Property(name="Interface102", type=pcm_repository_ProvidedRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_repository_ProvidedRole", type=Interface, multiplicity=Multiplicity(1, 1))
    }
)
providingEntity_ProvidedRole103: BinaryAssociation = BinaryAssociation(
    name="providingEntity_ProvidedRole103",
    ends={
        Property(name="InterfaceProvidingEntity", type=pcm_repository_ProvidedRole, multiplicity=Multiplicity(1, 1)),
        Property(name="providedRoles_InterfaceProvidingEntity", type=entity_InterfaceProvidingEntity, multiplicity=Multiplicity(1, 1))
    }
)
signature__ServiceCall104: BinaryAssociation = BinaryAssociation(
    name="signature__ServiceCall104",
    ends={
        Property(name="Signature105", type=pcm_protocol_ServiceCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_protocol_ServiceCall", type=Signature, multiplicity=Multiplicity(1, 1))
    }
)
specification_VariableCharacterisation106: BinaryAssociation = BinaryAssociation(
    name="specification_VariableCharacterisation106",
    ends={
        Property(name="PCMRandomVariable107", type=pcm_parameter_VariableCharacterisation, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_parameter_VariableCharacterisation", type=PCMRandomVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variableCharacterisation_VariableUsage108: BinaryAssociation = BinaryAssociation(
    name="variableCharacterisation_VariableUsage108",
    ends={
        Property(name="VariableCharacterisation", type=pcm_parameter_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_parameter_VariableUsage", type=VariableCharacterisation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
namedReference_VariableUsage109: BinaryAssociation = BinaryAssociation(
    name="namedReference_VariableUsage109",
    ends={
        Property(name="parameter_pcm_AbstractNamedReference", type=pcm_parameter_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_parameter_VariableUsage110", type=parameter_pcm_AbstractNamedReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
predecessor_AbstractAction112: BinaryAssociation = BinaryAssociation(
    name="predecessor_AbstractAction112",
    ends={
        Property(name="AbstractAction", type=pcm_seff_AbstractAction, multiplicity=Multiplicity(1, 1)),
        Property(name="successor_AbstractAction", type=AbstractAction, multiplicity=Multiplicity(0, 1))
    }
)
successor_AbstractAction113: BinaryAssociation = BinaryAssociation(
    name="successor_AbstractAction113",
    ends={
        Property(name="AbstractAction114", type=pcm_seff_AbstractAction, multiplicity=Multiplicity(1, 1)),
        Property(name="predecessor_AbstractAction", type=AbstractAction, multiplicity=Multiplicity(0, 1))
    }
)
resourceDemand_Action111: BinaryAssociation = BinaryAssociation(
    name="resourceDemand_Action111",
    ends={
        Property(name="ParametricResourceDemand", type=pcm_seff_AbstractInternalControlFlowAction, multiplicity=Multiplicity(1, 1)),
        Property(name="action_ParametricResourceDemand", type=performance_ParametricResourceDemand, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
steps_Behaviour115: BinaryAssociation = BinaryAssociation(
    name="steps_Behaviour115",
    ends={
        Property(name="AbstractAction116", type=pcm_seff_ResourceDemandingBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_seff_ResourceDemandingBehaviour", type=AbstractAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
passiveResource_ReleaseAction117: BinaryAssociation = BinaryAssociation(
    name="passiveResource_ReleaseAction117",
    ends={
        Property(name="PassiveResource118", type=pcm_seff_ReleaseAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_seff_ReleaseAction", type=PassiveResource, multiplicity=Multiplicity(1, 1))
    }
)
iterationCount_LoopAction119: BinaryAssociation = BinaryAssociation(
    name="iterationCount_LoopAction119",
    ends={
        Property(name="PCMRandomVariable120", type=pcm_seff_LoopAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_seff_LoopAction", type=PCMRandomVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
bodyBehaviour_Loop121: BinaryAssociation = BinaryAssociation(
    name="bodyBehaviour_Loop121",
    ends={
        Property(name="ResourceDemandingBehaviour", type=pcm_seff_AbstractLoopAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_seff_AbstractLoopAction", type=ResourceDemandingBehaviour, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
asynchronousForkedBehaviours_ForkAction122: BinaryAssociation = BinaryAssociation(
    name="asynchronousForkedBehaviours_ForkAction122",
    ends={
        Property(name="ForkedBehaviour", type=pcm_seff_ForkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_seff_ForkAction", type=ForkedBehaviour, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
synchronisingBehaviours_ForkAction123: BinaryAssociation = BinaryAssociation(
    name="synchronisingBehaviours_ForkAction123",
    ends={
        Property(name="SynchronisationPoint", type=pcm_seff_ForkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_seff_ForkAction124", type=SynchronisationPoint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
synchronousForkedBehaviours_SynchronisationPoint125: BinaryAssociation = BinaryAssociation(
    name="synchronousForkedBehaviours_SynchronisationPoint125",
    ends={
        Property(name="ForkedBehaviour126", type=pcm_seff_SynchronisationPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_seff_SynchronisationPoint", type=ForkedBehaviour, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
outputParameterUsage_SynchronisationPoint127: BinaryAssociation = BinaryAssociation(
    name="outputParameterUsage_SynchronisationPoint127",
    ends={
        Property(name="VariableUsage129", type=pcm_seff_SynchronisationPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_seff_SynchronisationPoint128", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
calledService_ExternalService130: BinaryAssociation = BinaryAssociation(
    name="calledService_ExternalService130",
    ends={
        Property(name="Signature131", type=pcm_seff_ExternalCallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_seff_ExternalCallAction", type=Signature, multiplicity=Multiplicity(1, 1))
    }
)
inputParameterUsages_ExternalCallAction132: BinaryAssociation = BinaryAssociation(
    name="inputParameterUsages_ExternalCallAction132",
    ends={
        Property(name="VariableUsage134", type=pcm_seff_ExternalCallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_seff_ExternalCallAction133", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputVariableUsages_ExternalCallAction135: BinaryAssociation = BinaryAssociation(
    name="outputVariableUsages_ExternalCallAction135",
    ends={
        Property(name="VariableUsage137", type=pcm_seff_ExternalCallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_seff_ExternalCallAction136", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
role_ExternalService138: BinaryAssociation = BinaryAssociation(
    name="role_ExternalService138",
    ends={
        Property(name="Role", type=pcm_seff_ExternalCallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_seff_ExternalCallAction139", type=Role, multiplicity=Multiplicity(1, 1))
    }
)
branchBehaviour_BranchTransition140: BinaryAssociation = BinaryAssociation(
    name="branchBehaviour_BranchTransition140",
    ends={
        Property(name="ResourceDemandingBehaviour141", type=pcm_seff_AbstractBranchTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_seff_AbstractBranchTransition", type=ResourceDemandingBehaviour, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
branches_Branch142: BinaryAssociation = BinaryAssociation(
    name="branches_Branch142",
    ends={
        Property(name="AbstractBranchTransition", type=pcm_seff_BranchAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_seff_BranchAction", type=AbstractBranchTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
passiveresource_AcquireAction143: BinaryAssociation = BinaryAssociation(
    name="passiveresource_AcquireAction143",
    ends={
        Property(name="PassiveResource144", type=pcm_seff_AcquireAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_seff_AcquireAction", type=PassiveResource, multiplicity=Multiplicity(1, 1))
    }
)
parameter_CollectionIteratorAction145: BinaryAssociation = BinaryAssociation(
    name="parameter_CollectionIteratorAction145",
    ends={
        Property(name="Parameter146", type=pcm_seff_CollectionIteratorAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_seff_CollectionIteratorAction", type=Parameter_, multiplicity=Multiplicity(1, 1))
    }
)
branchCondition_GuardedBranchTransition147: BinaryAssociation = BinaryAssociation(
    name="branchCondition_GuardedBranchTransition147",
    ends={
        Property(name="PCMRandomVariable148", type=pcm_seff_GuardedBranchTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_seff_GuardedBranchTransition", type=PCMRandomVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
localVariableUsages_SetVariableAction149: BinaryAssociation = BinaryAssociation(
    name="localVariableUsages_SetVariableAction149",
    ends={
        Property(name="VariableUsage150", type=pcm_seff_SetVariableAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_seff_SetVariableAction", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
describedService__SEFF151: BinaryAssociation = BinaryAssociation(
    name="describedService__SEFF151",
    ends={
        Property(name="Signature152", type=pcm_seff_ServiceEffectSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_seff_ServiceEffectSpecification", type=Signature, multiplicity=Multiplicity(1, 1))
    }
)
specification_ParametericResourceDemand153: BinaryAssociation = BinaryAssociation(
    name="specification_ParametericResourceDemand153",
    ends={
        Property(name="PCMRandomVariable154", type=pcm_performance_ParametricResourceDemand, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_performance_ParametricResourceDemand", type=PCMRandomVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
requiredResource_ParametricResourceDemand155: BinaryAssociation = BinaryAssociation(
    name="requiredResource_ParametricResourceDemand155",
    ends={
        Property(name="ProcessingResourceType", type=pcm_performance_ParametricResourceDemand, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_performance_ParametricResourceDemand156", type=ProcessingResourceType, multiplicity=Multiplicity(1, 1))
    }
)
action_ParametricResourceDemand157: BinaryAssociation = BinaryAssociation(
    name="action_ParametricResourceDemand157",
    ends={
        Property(name="AbstractInternalControlFlowAction", type=pcm_performance_ParametricResourceDemand, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceDemand_Action", type=AbstractInternalControlFlowAction, multiplicity=Multiplicity(1, 1))
    }
)
availableResourceTypes_ResourceRepository158: BinaryAssociation = BinaryAssociation(
    name="availableResourceTypes_ResourceRepository158",
    ends={
        Property(name="ResourceType", type=pcm_resourcetype_ResourceRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_resourcetype_ResourceRepository", type=ResourceType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
toResourceContainer_LinkingResource172: BinaryAssociation = BinaryAssociation(
    name="toResourceContainer_LinkingResource172",
    ends={
        Property(name="ResourceContainer173", type=pcm_resourceenvironment_LinkingResource, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_resourceenvironment_LinkingResource", type=ResourceContainer, multiplicity=Multiplicity(0, 9999))
    }
)
fromResourceContainer_LinkingResource174: BinaryAssociation = BinaryAssociation(
    name="fromResourceContainer_LinkingResource174",
    ends={
        Property(name="ResourceContainer176", type=pcm_resourceenvironment_LinkingResource, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_resourceenvironment_LinkingResource175", type=ResourceContainer, multiplicity=Multiplicity(0, 9999))
    }
)
resourceContainer_AllocationContext159: BinaryAssociation = BinaryAssociation(
    name="resourceContainer_AllocationContext159",
    ends={
        Property(name="ResourceContainer", type=pcm_allocation_AllocationContext, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_allocation_AllocationContext", type=ResourceContainer, multiplicity=Multiplicity(1, 1))
    }
)
assemblyContext_AllocationContext160: BinaryAssociation = BinaryAssociation(
    name="assemblyContext_AllocationContext160",
    ends={
        Property(name="composition_AssemblyContext162", type=pcm_allocation_AllocationContext, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_allocation_AllocationContext161", type=composition_AssemblyContext, multiplicity=Multiplicity(1, 1))
    }
)
allocationContexts_Allocation163: BinaryAssociation = BinaryAssociation(
    name="allocationContexts_Allocation163",
    ends={
        Property(name="AllocationContext", type=pcm_allocation_Allocation, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_allocation_Allocation", type=AllocationContext, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
targetResourceEnvironment_Allocation164: BinaryAssociation = BinaryAssociation(
    name="targetResourceEnvironment_Allocation164",
    ends={
        Property(name="ResourceEnvironment", type=pcm_allocation_Allocation, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_allocation_Allocation165", type=ResourceEnvironment, multiplicity=Multiplicity(0, 1))
    }
)
system_Allocation166: BinaryAssociation = BinaryAssociation(
    name="system_Allocation166",
    ends={
        Property(name="System", type=pcm_allocation_Allocation, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_allocation_Allocation167", type=System, multiplicity=Multiplicity(1, 1))
    }
)
linkingresource168: BinaryAssociation = BinaryAssociation(
    name="linkingresource168",
    ends={
        Property(name="LinkingResource", type=pcm_resourceenvironment_ResourceEnvironment, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_resourceenvironment_ResourceEnvironment", type=LinkingResource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceContainer_ResourceEnvironment169: BinaryAssociation = BinaryAssociation(
    name="resourceContainer_ResourceEnvironment169",
    ends={
        Property(name="ResourceContainer171", type=pcm_resourceenvironment_ResourceEnvironment, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_resourceenvironment_ResourceEnvironment170", type=ResourceContainer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
activeResourceSpecifications_ResourceContainer191: BinaryAssociation = BinaryAssociation(
    name="activeResourceSpecifications_ResourceContainer191",
    ends={
        Property(name="ProcessingResourceSpecification", type=pcm_resourceenvironment_ResourceContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_resourceenvironment_ResourceContainer", type=ProcessingResourceSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
communicationLinkResourceSpecifications_LinkingResource177: BinaryAssociation = BinaryAssociation(
    name="communicationLinkResourceSpecifications_LinkingResource177",
    ends={
        Property(name="CommunicationLinkResourceSpecification", type=pcm_resourceenvironment_LinkingResource, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_resourceenvironment_LinkingResource178", type=CommunicationLinkResourceSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
communicationLinkResourceType_CommunicationLinkResourceSpecification179: BinaryAssociation = BinaryAssociation(
    name="communicationLinkResourceType_CommunicationLinkResourceSpecification179",
    ends={
        Property(name="CommunicationLinkResourceType", type=pcm_resourceenvironment_CommunicationLinkResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_resourceenvironment_CommunicationLinkResourceSpecification", type=CommunicationLinkResourceType, multiplicity=Multiplicity(1, 1))
    }
)
latency_CommunicationLinkResourceSpecification180: BinaryAssociation = BinaryAssociation(
    name="latency_CommunicationLinkResourceSpecification180",
    ends={
        Property(name="PCMRandomVariable182", type=pcm_resourceenvironment_CommunicationLinkResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_resourceenvironment_CommunicationLinkResourceSpecification181", type=PCMRandomVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
throughput_CommunicationLinkResourceSpecification183: BinaryAssociation = BinaryAssociation(
    name="throughput_CommunicationLinkResourceSpecification183",
    ends={
        Property(name="PCMRandomVariable185", type=pcm_resourceenvironment_CommunicationLinkResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_resourceenvironment_CommunicationLinkResourceSpecification184", type=PCMRandomVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
activeResourceType_ActiveResourceSpecification186: BinaryAssociation = BinaryAssociation(
    name="activeResourceType_ActiveResourceSpecification186",
    ends={
        Property(name="ProcessingResourceType187", type=pcm_resourceenvironment_ProcessingResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_resourceenvironment_ProcessingResourceSpecification", type=ProcessingResourceType, multiplicity=Multiplicity(1, 1))
    }
)
processingRate_ProcessingResourceSpecification188: BinaryAssociation = BinaryAssociation(
    name="processingRate_ProcessingResourceSpecification188",
    ends={
        Property(name="PCMRandomVariable190", type=pcm_resourceenvironment_ProcessingResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_resourceenvironment_ProcessingResourceSpecification189", type=PCMRandomVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
qosAnnotations_System192: BinaryAssociation = BinaryAssociation(
    name="qosAnnotations_System192",
    ends={
        Property(name="QoSAnnotations", type=pcm_system_System, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_system_System", type=QoSAnnotations, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
signature_SpecifiedQoSAnnation193: BinaryAssociation = BinaryAssociation(
    name="signature_SpecifiedQoSAnnation193",
    ends={
        Property(name="Signature194", type=pcm_qosannotations_SpecifiedQoSAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_qosannotations_SpecifiedQoSAnnotation", type=Signature, multiplicity=Multiplicity(1, 1))
    }
)
role_SpecifiedQoSAnnotation195: BinaryAssociation = BinaryAssociation(
    name="role_SpecifiedQoSAnnotation195",
    ends={
        Property(name="Role197", type=pcm_qosannotations_SpecifiedQoSAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_qosannotations_SpecifiedQoSAnnotation196", type=Role, multiplicity=Multiplicity(1, 1))
    }
)
specification_SpecifiedExecutionTime198: BinaryAssociation = BinaryAssociation(
    name="specification_SpecifiedExecutionTime198",
    ends={
        Property(name="PCMRandomVariable200", type=pcm_qosannotations_SpecifiedQoSAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_qosannotations_SpecifiedQoSAnnotation199", type=PCMRandomVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
signature_SpecifiedOutputParameterAbstraction201: BinaryAssociation = BinaryAssociation(
    name="signature_SpecifiedOutputParameterAbstraction201",
    ends={
        Property(name="Signature202", type=pcm_qosannotations_SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_qosannotations_SpecifiedOutputParameterAbstraction", type=Signature, multiplicity=Multiplicity(1, 1))
    }
)
role_SpecifiedOutputParameterAbstraction203: BinaryAssociation = BinaryAssociation(
    name="role_SpecifiedOutputParameterAbstraction203",
    ends={
        Property(name="Role205", type=pcm_qosannotations_SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_qosannotations_SpecifiedOutputParameterAbstraction204", type=Role, multiplicity=Multiplicity(1, 1))
    }
)
expectedExternalOutputs_SpecifiedOutputParameterAbstraction206: BinaryAssociation = BinaryAssociation(
    name="expectedExternalOutputs_SpecifiedOutputParameterAbstraction206",
    ends={
        Property(name="VariableUsage208", type=pcm_qosannotations_SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_qosannotations_SpecifiedOutputParameterAbstraction207", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specifiedQoSAnnotations_QoSAnnotations209: BinaryAssociation = BinaryAssociation(
    name="specifiedQoSAnnotations_QoSAnnotations209",
    ends={
        Property(name="SpecifiedQoSAnnotation", type=pcm_qosannotations_QoSAnnotations, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_qosannotations_QoSAnnotations", type=SpecifiedQoSAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specifiedOutputParameterAbstractions_QoSAnnotations210: BinaryAssociation = BinaryAssociation(
    name="specifiedOutputParameterAbstractions_QoSAnnotations210",
    ends={
        Property(name="SpecifiedOutputParameterAbstraction", type=pcm_qosannotations_QoSAnnotations, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_qosannotations_QoSAnnotations211", type=SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
assemblyContext_ComponentSpecifiedExecutionTime212: BinaryAssociation = BinaryAssociation(
    name="assemblyContext_ComponentSpecifiedExecutionTime212",
    ends={
        Property(name="composition_AssemblyContext213", type=pcm_performance_ComponentSpecifiedExecutionTime, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_performance_ComponentSpecifiedExecutionTime", type=composition_AssemblyContext, multiplicity=Multiplicity(1, 1))
    }
)
workload_UsageScenario214: BinaryAssociation = BinaryAssociation(
    name="workload_UsageScenario214",
    ends={
        Property(name="Workload", type=pcm_usagemodel_UsageScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_usagemodel_UsageScenario", type=Workload, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
scenarioBehaviour_UsageScenario215: BinaryAssociation = BinaryAssociation(
    name="scenarioBehaviour_UsageScenario215",
    ends={
        Property(name="ScenarioBehaviour", type=pcm_usagemodel_UsageScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_usagemodel_UsageScenario216", type=ScenarioBehaviour, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
actions_ScenarioBehaviour217: BinaryAssociation = BinaryAssociation(
    name="actions_ScenarioBehaviour217",
    ends={
        Property(name="AbstractUserAction", type=pcm_usagemodel_ScenarioBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_usagemodel_ScenarioBehaviour", type=AbstractUserAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
successor218: BinaryAssociation = BinaryAssociation(
    name="successor218",
    ends={
        Property(name="AbstractUserAction219", type=pcm_usagemodel_AbstractUserAction, multiplicity=Multiplicity(1, 1)),
        Property(name="predecessor", type=AbstractUserAction, multiplicity=Multiplicity(0, 1))
    }
)
predecessor220: BinaryAssociation = BinaryAssociation(
    name="predecessor220",
    ends={
        Property(name="AbstractUserAction221", type=pcm_usagemodel_AbstractUserAction, multiplicity=Multiplicity(1, 1)),
        Property(name="successor", type=AbstractUserAction, multiplicity=Multiplicity(0, 1))
    }
)
usageScenario_UsageModel222: BinaryAssociation = BinaryAssociation(
    name="usageScenario_UsageModel222",
    ends={
        Property(name="UsageScenario", type=pcm_usagemodel_UsageModel, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_usagemodel_UsageModel", type=UsageScenario, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
userData_UsageModel223: BinaryAssociation = BinaryAssociation(
    name="userData_UsageModel223",
    ends={
        Property(name="UserData", type=pcm_usagemodel_UsageModel, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_usagemodel_UsageModel224", type=UserData, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
userDataParameterUsages_UserData225: BinaryAssociation = BinaryAssociation(
    name="userDataParameterUsages_UserData225",
    ends={
        Property(name="VariableUsage226", type=pcm_usagemodel_UserData, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_usagemodel_UserData", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
assemblyContext_userData227: BinaryAssociation = BinaryAssociation(
    name="assemblyContext_userData227",
    ends={
        Property(name="composition_AssemblyContext229", type=pcm_usagemodel_UserData, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_usagemodel_UserData228", type=composition_AssemblyContext, multiplicity=Multiplicity(1, 1))
    }
)
providedRole_EntryLevelSystemCall239: BinaryAssociation = BinaryAssociation(
    name="providedRole_EntryLevelSystemCall239",
    ends={
        Property(name="ProvidedRole241", type=pcm_usagemodel_EntryLevelSystemCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_usagemodel_EntryLevelSystemCall240", type=ProvidedRole, multiplicity=Multiplicity(1, 1))
    }
)
interArrivalTime_OpenWorkload230: BinaryAssociation = BinaryAssociation(
    name="interArrivalTime_OpenWorkload230",
    ends={
        Property(name="PCMRandomVariable231", type=pcm_usagemodel_OpenWorkload, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_usagemodel_OpenWorkload", type=PCMRandomVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
bodyBehaviour_Loop232: BinaryAssociation = BinaryAssociation(
    name="bodyBehaviour_Loop232",
    ends={
        Property(name="ScenarioBehaviour233", type=pcm_usagemodel_Loop, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_usagemodel_Loop", type=ScenarioBehaviour, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
loopIteration_Loop234: BinaryAssociation = BinaryAssociation(
    name="loopIteration_Loop234",
    ends={
        Property(name="PCMRandomVariable236", type=pcm_usagemodel_Loop, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_usagemodel_Loop235", type=PCMRandomVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
inputParameterUsages_EntryLevelSystemCall237: BinaryAssociation = BinaryAssociation(
    name="inputParameterUsages_EntryLevelSystemCall237",
    ends={
        Property(name="VariableUsage238", type=pcm_usagemodel_EntryLevelSystemCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_usagemodel_EntryLevelSystemCall", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
signature_EntryLevelSystemCall242: BinaryAssociation = BinaryAssociation(
    name="signature_EntryLevelSystemCall242",
    ends={
        Property(name="Signature244", type=pcm_usagemodel_EntryLevelSystemCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_usagemodel_EntryLevelSystemCall243", type=Signature, multiplicity=Multiplicity(1, 1))
    }
)
outputParameterUsages_EntryLevelSystemCall245: BinaryAssociation = BinaryAssociation(
    name="outputParameterUsages_EntryLevelSystemCall245",
    ends={
        Property(name="VariableUsage247", type=pcm_usagemodel_EntryLevelSystemCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_usagemodel_EntryLevelSystemCall246", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
thinkTime_ClosedWorkload248: BinaryAssociation = BinaryAssociation(
    name="thinkTime_ClosedWorkload248",
    ends={
        Property(name="PCMRandomVariable249", type=pcm_usagemodel_ClosedWorkload, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_usagemodel_ClosedWorkload", type=PCMRandomVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
branchTransitions_Branch250: BinaryAssociation = BinaryAssociation(
    name="branchTransitions_Branch250",
    ends={
        Property(name="BranchTransition", type=pcm_usagemodel_Branch, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_usagemodel_Branch", type=BranchTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
branchedBehaviour_BranchTransition251: BinaryAssociation = BinaryAssociation(
    name="branchedBehaviour_BranchTransition251",
    ends={
        Property(name="ScenarioBehaviour252", type=pcm_usagemodel_BranchTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_usagemodel_BranchTransition", type=ScenarioBehaviour, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
timeSpecification_Delay253: BinaryAssociation = BinaryAssociation(
    name="timeSpecification_Delay253",
    ends={
        Property(name="PCMRandomVariable254", type=pcm_usagemodel_Delay, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_usagemodel_Delay", type=PCMRandomVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_pcm_entity_Entity_Identifier = Generalization(general=Identifier, specific=pcm_entity_Entity)
gen_pcm_entity_Entity_entity_NamedElement = Generalization(general=entity_NamedElement, specific=pcm_entity_Entity)
gen_pcm_entity_InterfaceProvidingEntity_Entity = Generalization(general=Entity, specific=pcm_entity_InterfaceProvidingEntity)
gen_pcm_entity_InterfaceProvidingRequiringEntity_entity_InterfaceProvidingEntity = Generalization(general=entity_InterfaceProvidingEntity, specific=pcm_entity_InterfaceProvidingRequiringEntity)
gen_pcm_entity_InterfaceProvidingRequiringEntity_entity_InterfaceRequiringEntity = Generalization(general=entity_InterfaceRequiringEntity, specific=pcm_entity_InterfaceProvidingRequiringEntity)
gen_pcm_entity_InterfaceProvidingRequiringEntity_entity_ResourceInterfaceRequiringEntity = Generalization(general=entity_ResourceInterfaceRequiringEntity, specific=pcm_entity_InterfaceProvidingRequiringEntity)
gen_pcm_core_PCMRandomVariable_RandomVariable = Generalization(general=RandomVariable, specific=pcm_core_PCMRandomVariable)
gen_pcm_entity_ResourceInterfaceRequiringEntity_Entity = Generalization(general=Entity, specific=pcm_entity_ResourceInterfaceRequiringEntity)
gen_pcm_entity_ComposedProvidingRequiringEntity_composition_ComposedStructure = Generalization(general=composition_ComposedStructure, specific=pcm_entity_ComposedProvidingRequiringEntity)
gen_pcm_entity_ComposedProvidingRequiringEntity_entity_InterfaceProvidingRequiringEntity = Generalization(general=entity_InterfaceProvidingRequiringEntity, specific=pcm_entity_ComposedProvidingRequiringEntity)
gen_pcm_connectors_Connector_Entity = Generalization(general=Entity, specific=pcm_connectors_Connector)
gen_pcm_composition_ProvidedDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_composition_ProvidedDelegationConnector)
gen_pcm_entity_InterfaceRequiringEntity_Entity = Generalization(general=Entity, specific=pcm_entity_InterfaceRequiringEntity)
gen_pcm_composition_AssemblyContext_Entity = Generalization(general=Entity, specific=pcm_composition_AssemblyContext)
gen_pcm_composition_RequiredDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_composition_RequiredDelegationConnector)
gen_pcm_composition_AssemblyConnector_Connector = Generalization(general=Connector, specific=pcm_composition_AssemblyConnector)
gen_pcm_composition_ComposedStructure_Entity = Generalization(general=Entity, specific=pcm_composition_ComposedStructure)
gen_pcm_repository_PassiveResource_Entity = Generalization(general=Entity, specific=pcm_repository_PassiveResource)
gen_pcm_repository_Repository_Entity = Generalization(general=Entity, specific=pcm_repository_Repository)
gen_pcm_repository_RepositoryComponent_InterfaceProvidingRequiringEntity = Generalization(general=InterfaceProvidingRequiringEntity, specific=pcm_repository_RepositoryComponent)
gen_pcm_repository_RequiredRole_Role = Generalization(general=Role, specific=pcm_repository_RequiredRole)
gen_pcm_repository_Role_Entity = Generalization(general=Entity, specific=pcm_repository_Role)
gen_pcm_repository_Interface_Entity = Generalization(general=Entity, specific=pcm_repository_Interface)
gen_pcm_repository_ResourceRequiredRole_Role = Generalization(general=Role, specific=pcm_repository_ResourceRequiredRole)
gen_pcm_repository_ProvidesComponentType_RepositoryComponent = Generalization(general=RepositoryComponent, specific=pcm_repository_ProvidesComponentType)
gen_pcm_repository_ImplementationComponentType_RepositoryComponent = Generalization(general=RepositoryComponent, specific=pcm_repository_ImplementationComponentType)
gen_pcm_repository_CompleteComponentType_RepositoryComponent = Generalization(general=RepositoryComponent, specific=pcm_repository_CompleteComponentType)
gen_pcm_repository_DelegationConnector_Connector = Generalization(general=Connector, specific=pcm_repository_DelegationConnector)
gen_pcm_repository_CompositeComponent_entity_ComposedProvidingRequiringEntity = Generalization(general=entity_ComposedProvidingRequiringEntity, specific=pcm_repository_CompositeComponent)
gen_pcm_repository_CompositeComponent_repository_ImplementationComponentType = Generalization(general=repository_ImplementationComponentType, specific=pcm_repository_CompositeComponent)
gen_pcm_repository_BasicComponent_ImplementationComponentType = Generalization(general=ImplementationComponentType, specific=pcm_repository_BasicComponent)
gen_pcm_repository_PrimitiveDataType_DataType = Generalization(general=DataType, specific=pcm_repository_PrimitiveDataType)
gen_pcm_repository_CollectionDataType_entity_Entity = Generalization(general=entity_Entity, specific=pcm_repository_CollectionDataType)
gen_pcm_repository_CollectionDataType_repository_DataType = Generalization(general=repository_DataType, specific=pcm_repository_CollectionDataType)
gen_pcm_repository_CompositeDataType_entity_Entity = Generalization(general=entity_Entity, specific=pcm_repository_CompositeDataType)
gen_pcm_repository_CompositeDataType_repository_DataType = Generalization(general=repository_DataType, specific=pcm_repository_CompositeDataType)
gen_pcm_repository_ProvidedRole_Role = Generalization(general=Role, specific=pcm_repository_ProvidedRole)
gen_pcm_repository_InnerDeclaration_NamedElement = Generalization(general=NamedElement, specific=pcm_repository_InnerDeclaration)
gen_pcm_parameter_CharacterisedVariable_Variable = Generalization(general=Variable, specific=pcm_parameter_CharacterisedVariable)
gen_pcm_seff_StopAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_seff_StopAction)
gen_pcm_seff_AbstractInternalControlFlowAction_AbstractAction = Generalization(general=AbstractAction, specific=pcm_seff_AbstractInternalControlFlowAction)
gen_pcm_seff_AbstractAction_Entity = Generalization(general=Entity, specific=pcm_seff_AbstractAction)
gen_pcm_seff_StartAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_seff_StartAction)
gen_pcm_seff_ResourceDemandingSEFF_Identifier = Generalization(general=Identifier, specific=pcm_seff_ResourceDemandingSEFF)
gen_pcm_seff_ResourceDemandingSEFF_seff_ServiceEffectSpecification = Generalization(general=seff_ServiceEffectSpecification, specific=pcm_seff_ResourceDemandingSEFF)
gen_pcm_seff_ResourceDemandingSEFF_seff_ResourceDemandingBehaviour = Generalization(general=seff_ResourceDemandingBehaviour, specific=pcm_seff_ResourceDemandingSEFF)
gen_pcm_seff_ReleaseAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_seff_ReleaseAction)
gen_pcm_seff_LoopAction_AbstractLoopAction = Generalization(general=AbstractLoopAction, specific=pcm_seff_LoopAction)
gen_pcm_seff_AbstractLoopAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_seff_AbstractLoopAction)
gen_pcm_seff_InternalAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_seff_InternalAction)
gen_pcm_seff_AbstractBranchTransition_NamedElement = Generalization(general=NamedElement, specific=pcm_seff_AbstractBranchTransition)
gen_pcm_seff_ForkAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_seff_ForkAction)
gen_pcm_seff_ForkedBehaviour_ResourceDemandingBehaviour = Generalization(general=ResourceDemandingBehaviour, specific=pcm_seff_ForkedBehaviour)
gen_pcm_seff_ExternalCallAction_AbstractAction = Generalization(general=AbstractAction, specific=pcm_seff_ExternalCallAction)
gen_pcm_seff_ProbabilisticBranchTransition_AbstractBranchTransition = Generalization(general=AbstractBranchTransition, specific=pcm_seff_ProbabilisticBranchTransition)
gen_pcm_seff_SetVariableAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_seff_SetVariableAction)
gen_pcm_seff_BranchAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_seff_BranchAction)
gen_pcm_seff_AcquireAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_seff_AcquireAction)
gen_pcm_seff_CollectionIteratorAction_AbstractLoopAction = Generalization(general=AbstractLoopAction, specific=pcm_seff_CollectionIteratorAction)
gen_pcm_seff_GuardedBranchTransition_AbstractBranchTransition = Generalization(general=AbstractBranchTransition, specific=pcm_seff_GuardedBranchTransition)
gen_pcm_allocation_AllocationContext_Entity = Generalization(general=Entity, specific=pcm_allocation_AllocationContext)
gen_pcm_resourcetype_ResourceType_entity_Entity = Generalization(general=entity_Entity, specific=pcm_resourcetype_ResourceType)
gen_pcm_resourcetype_ResourceType_UnitCarryingElement = Generalization(general=UnitCarryingElement, specific=pcm_resourcetype_ResourceType)
gen_pcm_resourcetype_CommunicationLinkResourceType_ProcessingResourceType = Generalization(general=ProcessingResourceType, specific=pcm_resourcetype_CommunicationLinkResourceType)
gen_pcm_resourcetype_ProcessingResourceType_ResourceType = Generalization(general=ResourceType, specific=pcm_resourcetype_ProcessingResourceType)
gen_pcm_allocation_Allocation_Entity = Generalization(general=Entity, specific=pcm_allocation_Allocation)
gen_pcm_resourceenvironment_LinkingResource_Entity = Generalization(general=Entity, specific=pcm_resourceenvironment_LinkingResource)
gen_pcm_resourceenvironment_ResourceContainer_Entity = Generalization(general=Entity, specific=pcm_resourceenvironment_ResourceContainer)
gen_pcm_performance_SystemSpecifiedExecutionTime_SpecifiedQoSAnnotation = Generalization(general=SpecifiedQoSAnnotation, specific=pcm_performance_SystemSpecifiedExecutionTime)
gen_pcm_performance_ComponentSpecifiedExecutionTime_SpecifiedQoSAnnotation = Generalization(general=SpecifiedQoSAnnotation, specific=pcm_performance_ComponentSpecifiedExecutionTime)
gen_pcm_system_System_entity_Entity = Generalization(general=entity_Entity, specific=pcm_system_System)
gen_pcm_system_System_entity_ComposedProvidingRequiringEntity = Generalization(general=entity_ComposedProvidingRequiringEntity, specific=pcm_system_System)
gen_pcm_qosannotations_QoSAnnotations_Entity = Generalization(general=Entity, specific=pcm_qosannotations_QoSAnnotations)
gen_pcm_reliability_SpecifiedFailureProbability_SpecifiedQoSAnnotation = Generalization(general=SpecifiedQoSAnnotation, specific=pcm_reliability_SpecifiedFailureProbability)
gen_pcm_usagemodel_UsageScenario_Entity = Generalization(general=Entity, specific=pcm_usagemodel_UsageScenario)
gen_pcm_usagemodel_ScenarioBehaviour_Entity = Generalization(general=Entity, specific=pcm_usagemodel_ScenarioBehaviour)
gen_pcm_usagemodel_Start_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_usagemodel_Start)
gen_pcm_usagemodel_AbstractUserAction_Entity = Generalization(general=Entity, specific=pcm_usagemodel_AbstractUserAction)
gen_pcm_usagemodel_Stop_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_usagemodel_Stop)
gen_pcm_usagemodel_OpenWorkload_Workload = Generalization(general=Workload, specific=pcm_usagemodel_OpenWorkload)
gen_pcm_usagemodel_Loop_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_usagemodel_Loop)
gen_pcm_usagemodel_EntryLevelSystemCall_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_usagemodel_EntryLevelSystemCall)
gen_pcm_usagemodel_ClosedWorkload_Workload = Generalization(general=Workload, specific=pcm_usagemodel_ClosedWorkload)
gen_pcm_usagemodel_Branch_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_usagemodel_Branch)
gen_pcm_usagemodel_Delay_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_usagemodel_Delay)
gen_pcm_subsystem_SubSystem_entity_ComposedProvidingRequiringEntity = Generalization(general=entity_ComposedProvidingRequiringEntity, specific=pcm_subsystem_SubSystem)
gen_pcm_subsystem_SubSystem_repository_RepositoryComponent = Generalization(general=repository_RepositoryComponent, specific=pcm_subsystem_SubSystem)

# Domain Model
domain_model = DomainModel(
    name="pcm",
    types={pcm_core_PCMRandomVariable, RandomVariable, pcm_entity_Entity, Identifier, entity_NamedElement, pcm_entity_NamedElement, pcm_entity_InterfaceProvidingEntity, Entity, ProvidedRole, pcm_entity_InterfaceProvidingRequiringEntity, entity_InterfaceProvidingEntity, entity_InterfaceRequiringEntity, entity_ResourceInterfaceRequiringEntity, RequiredRole, pcm_entity_ResourceInterfaceRequiringEntity, ResourceRequiredRole, pcm_entity_ComposedProvidingRequiringEntity, composition_ComposedStructure, entity_InterfaceProvidingRequiringEntity, pcm_connectors_Connector, pcm_composition_ProvidedDelegationConnector, DelegationConnector, pcm_entity_InterfaceRequiringEntity, composition_AssemblyContext, pcm_composition_AssemblyContext, RepositoryComponent, VariableUsage, pcm_composition_RequiredDelegationConnector, pcm_composition_AssemblyConnector, Connector, pcm_composition_ResourceRequiredDelegationConnector, pcm_composition_ComposedStructure, composition_RequiredDelegationConnector, composition_AssemblyConnector, composition_ResourceRequiredDelegationConnector, pcm_repository_PassiveResource, PCMRandomVariable, pcm_repository_Signature, Parameter_, composition_ProvidedDelegationConnector, DataType, ExceptionType, pcm_repository_Parameter, Signature, pcm_repository_DataType, Repository, pcm_repository_Repository, Interface, pcm_repository_RepositoryComponent, InterfaceProvidingRequiringEntity, pcm_repository_RequiredRole, Role, pcm_repository_Role, pcm_repository_Interface, Protocol, pcm_repository_ResourceRequiredRole, pcm_repository_ExceptionType, pcm_repository_ProvidesComponentType, pcm_repository_ImplementationComponentType, CompleteComponentType, pcm_repository_CompleteComponentType, pcm_repository_DelegationConnector, pcm_repository_CompositeComponent, entity_ComposedProvidingRequiringEntity, repository_ImplementationComponentType, pcm_repository_BasicComponent, ImplementationComponentType, ProvidesComponentType, ServiceEffectSpecification, PassiveResource, pcm_repository_PrimitiveDataType, pcm_repository_CollectionDataType, entity_Entity, repository_DataType, pcm_repository_CompositeDataType, CompositeDataType, InnerDeclaration, pcm_repository_ProvidedRole, pcm_protocol_ServiceCall, pcm_protocol_Protocol, pcm_parameter_VariableCharacterisation, pcm_repository_InnerDeclaration, NamedElement, pcm_parameter_CharacterisedVariable, Variable, pcm_parameter_VariableUsage, VariableCharacterisation, parameter_pcm_AbstractNamedReference, pcm_seff_StopAction, AbstractInternalControlFlowAction, pcm_seff_AbstractInternalControlFlowAction, AbstractAction, pcm_seff_AbstractAction, pcm_seff_StartAction, pcm_seff_ResourceDemandingSEFF, seff_ServiceEffectSpecification, seff_ResourceDemandingBehaviour, pcm_seff_ResourceDemandingBehaviour, performance_ParametricResourceDemand, pcm_seff_ForkAction, pcm_seff_ReleaseAction, pcm_seff_LoopAction, AbstractLoopAction, pcm_seff_AbstractLoopAction, ResourceDemandingBehaviour, pcm_seff_InternalAction, pcm_seff_AbstractBranchTransition, ForkedBehaviour, SynchronisationPoint, pcm_seff_ForkedBehaviour, pcm_seff_SynchronisationPoint, pcm_seff_ExternalCallAction, pcm_seff_ProbabilisticBranchTransition, AbstractBranchTransition, pcm_seff_SetVariableAction, pcm_seff_BranchAction, pcm_seff_AcquireAction, pcm_seff_CollectionIteratorAction, pcm_seff_GuardedBranchTransition, pcm_allocation_AllocationContext, ResourceContainer, pcm_seff_ServiceEffectSpecification, pcm_performance_ParametricResourceDemand, ProcessingResourceType, pcm_resourcetype_ResourceType, UnitCarryingElement, pcm_resourcetype_ResourceRepository, ResourceType, pcm_resourcetype_CommunicationLinkResourceType, pcm_resourcetype_ProcessingResourceType, pcm_allocation_Allocation, AllocationContext, ResourceEnvironment, System, pcm_resourceenvironment_ResourceEnvironment, LinkingResource, pcm_resourceenvironment_LinkingResource, pcm_resourceenvironment_ResourceContainer, ProcessingResourceSpecification, CommunicationLinkResourceSpecification, pcm_resourceenvironment_CommunicationLinkResourceSpecification, CommunicationLinkResourceType, pcm_resourceenvironment_ProcessingResourceSpecification, pcm_performance_ComponentSpecifiedExecutionTime, pcm_system_System, QoSAnnotations, pcm_qosannotations_SpecifiedQoSAnnotation, pcm_qosannotations_SpecifiedOutputParameterAbstraction, pcm_qosannotations_QoSAnnotations, SpecifiedQoSAnnotation, SpecifiedOutputParameterAbstraction, pcm_performance_SystemSpecifiedExecutionTime, pcm_reliability_SpecifiedFailureProbability, pcm_usagemodel_Workload, pcm_usagemodel_UsageScenario, Workload, ScenarioBehaviour, pcm_usagemodel_ScenarioBehaviour, pcm_usagemodel_Start, AbstractUserAction, pcm_usagemodel_AbstractUserAction, pcm_usagemodel_UsageModel, UsageScenario, UserData, pcm_usagemodel_UserData, pcm_usagemodel_Stop, pcm_usagemodel_OpenWorkload, pcm_usagemodel_Loop, pcm_usagemodel_EntryLevelSystemCall, pcm_usagemodel_ClosedWorkload, pcm_usagemodel_Branch, BranchTransition, pcm_usagemodel_BranchTransition, pcm_usagemodel_Delay, pcm_subsystem_SubSystem, repository_RepositoryComponent, ParameterModifier, PrimitiveTypeEnum, VariableCharacterisationType, SchedulingPolicy},
    associations={providedRoles_InterfaceProvidingEntity0, requiredRoles_InterfaceRequiringEntity1, resourceRequiredRoles_ResourceInterfaceRequiringEntity2, innerProvidedRole_ProvidedDelegationConnector3, outerProvidedRole_ProvidedDelegationConnector5, assemblyContext_ProvidedDelegationConnector8, parentStructure_ProvidedDelegationConnector10, encapsulatedComponent_AssemblyContext11, parentStructure_AssemblyContext12, configParameterUsages_AssemblyContext14, innerRequiredRole_RequiredDelegationConnector16, outerRequiredRole_RequiredDelegationConnector18, assemblyContext_RequiredDelegationConnector21, parentStructure_RequiredDelegationConnector24, requiringAssemblyContext_AssemblyConnector26, providingAssemblyContext_AssemblyConnector28, providedRole_AssemblyConnector31, requiredRole_AssemblyConnector34, parentStructure_AssemblyConnector37, parentStructure_ResourceRequiredDelegationConnector39, innerResourceRequiredRole_ResourceRequiredDelegationConnector41, outerResourceRequiredRole_ResourceRequiredDelegationConnector43, assemblyContexts_ComposedStructure46, requiredDelegationConnectors_ComposedStructure48, assemblyConnectors_ComposedStructure49, resourceRequiredDelegationConnectors_ComposedStructure50, capacity_PassiveResource51, parameters__Signature52, providedDelegationConnectors_ComposedStructure47, interface_Signature53, returntype__Signature54, exceptions__Signature55, datatype__Parameter57, signature_Parameter59, repository_DataType60, components__Repository61, interfaces__Repository63, repository_RepositoryComponent67, requiredInterface__RequiredRole69, requiringEntity_RequiredRole71, parentInterface__Interface72, datatypes_Repository65, protocols__Interface77, signatures__Interface79, repository_Interface81, requiredInterface_ResourceRequiredRole83, resourceRequiringEntity_ResourceRequiredRole85, ancestorInterfaces_Interface74, parentCompleteComponentTypes86, componentParameterUsage_ImplementationComponentType87, parentProvidesComponentTypes90, serviceEffectSpecifications__BasicComponent91, passiveResource_BasicComponent92, innerType_CollectionDataType94, parentType_CompositeDataType96, innerDeclaration_CompositeDataType97, datatype_InnerDeclaration99, providedInterface__ProvidedRole101, providingEntity_ProvidedRole103, signature__ServiceCall104, specification_VariableCharacterisation106, variableCharacterisation_VariableUsage108, namedReference_VariableUsage109, predecessor_AbstractAction112, successor_AbstractAction113, resourceDemand_Action111, steps_Behaviour115, passiveResource_ReleaseAction117, iterationCount_LoopAction119, bodyBehaviour_Loop121, asynchronousForkedBehaviours_ForkAction122, synchronisingBehaviours_ForkAction123, synchronousForkedBehaviours_SynchronisationPoint125, outputParameterUsage_SynchronisationPoint127, calledService_ExternalService130, inputParameterUsages_ExternalCallAction132, outputVariableUsages_ExternalCallAction135, role_ExternalService138, branchBehaviour_BranchTransition140, branches_Branch142, passiveresource_AcquireAction143, parameter_CollectionIteratorAction145, branchCondition_GuardedBranchTransition147, localVariableUsages_SetVariableAction149, describedService__SEFF151, specification_ParametericResourceDemand153, requiredResource_ParametricResourceDemand155, action_ParametricResourceDemand157, availableResourceTypes_ResourceRepository158, toResourceContainer_LinkingResource172, fromResourceContainer_LinkingResource174, resourceContainer_AllocationContext159, assemblyContext_AllocationContext160, allocationContexts_Allocation163, targetResourceEnvironment_Allocation164, system_Allocation166, linkingresource168, resourceContainer_ResourceEnvironment169, activeResourceSpecifications_ResourceContainer191, communicationLinkResourceSpecifications_LinkingResource177, communicationLinkResourceType_CommunicationLinkResourceSpecification179, latency_CommunicationLinkResourceSpecification180, throughput_CommunicationLinkResourceSpecification183, activeResourceType_ActiveResourceSpecification186, processingRate_ProcessingResourceSpecification188, qosAnnotations_System192, signature_SpecifiedQoSAnnation193, role_SpecifiedQoSAnnotation195, specification_SpecifiedExecutionTime198, signature_SpecifiedOutputParameterAbstraction201, role_SpecifiedOutputParameterAbstraction203, expectedExternalOutputs_SpecifiedOutputParameterAbstraction206, specifiedQoSAnnotations_QoSAnnotations209, specifiedOutputParameterAbstractions_QoSAnnotations210, assemblyContext_ComponentSpecifiedExecutionTime212, workload_UsageScenario214, scenarioBehaviour_UsageScenario215, actions_ScenarioBehaviour217, successor218, predecessor220, usageScenario_UsageModel222, userData_UsageModel223, userDataParameterUsages_UserData225, assemblyContext_userData227, providedRole_EntryLevelSystemCall239, interArrivalTime_OpenWorkload230, bodyBehaviour_Loop232, loopIteration_Loop234, inputParameterUsages_EntryLevelSystemCall237, signature_EntryLevelSystemCall242, outputParameterUsages_EntryLevelSystemCall245, thinkTime_ClosedWorkload248, branchTransitions_Branch250, branchedBehaviour_BranchTransition251, timeSpecification_Delay253},
    generalizations={gen_pcm_entity_Entity_Identifier, gen_pcm_entity_Entity_entity_NamedElement, gen_pcm_entity_InterfaceProvidingEntity_Entity, gen_pcm_entity_InterfaceProvidingRequiringEntity_entity_InterfaceProvidingEntity, gen_pcm_entity_InterfaceProvidingRequiringEntity_entity_InterfaceRequiringEntity, gen_pcm_entity_InterfaceProvidingRequiringEntity_entity_ResourceInterfaceRequiringEntity, gen_pcm_core_PCMRandomVariable_RandomVariable, gen_pcm_entity_ResourceInterfaceRequiringEntity_Entity, gen_pcm_entity_ComposedProvidingRequiringEntity_composition_ComposedStructure, gen_pcm_entity_ComposedProvidingRequiringEntity_entity_InterfaceProvidingRequiringEntity, gen_pcm_connectors_Connector_Entity, gen_pcm_composition_ProvidedDelegationConnector_DelegationConnector, gen_pcm_entity_InterfaceRequiringEntity_Entity, gen_pcm_composition_AssemblyContext_Entity, gen_pcm_composition_RequiredDelegationConnector_DelegationConnector, gen_pcm_composition_AssemblyConnector_Connector, gen_pcm_composition_ComposedStructure_Entity, gen_pcm_repository_PassiveResource_Entity, gen_pcm_repository_Repository_Entity, gen_pcm_repository_RepositoryComponent_InterfaceProvidingRequiringEntity, gen_pcm_repository_RequiredRole_Role, gen_pcm_repository_Role_Entity, gen_pcm_repository_Interface_Entity, gen_pcm_repository_ResourceRequiredRole_Role, gen_pcm_repository_ProvidesComponentType_RepositoryComponent, gen_pcm_repository_ImplementationComponentType_RepositoryComponent, gen_pcm_repository_CompleteComponentType_RepositoryComponent, gen_pcm_repository_DelegationConnector_Connector, gen_pcm_repository_CompositeComponent_entity_ComposedProvidingRequiringEntity, gen_pcm_repository_CompositeComponent_repository_ImplementationComponentType, gen_pcm_repository_BasicComponent_ImplementationComponentType, gen_pcm_repository_PrimitiveDataType_DataType, gen_pcm_repository_CollectionDataType_entity_Entity, gen_pcm_repository_CollectionDataType_repository_DataType, gen_pcm_repository_CompositeDataType_entity_Entity, gen_pcm_repository_CompositeDataType_repository_DataType, gen_pcm_repository_ProvidedRole_Role, gen_pcm_repository_InnerDeclaration_NamedElement, gen_pcm_parameter_CharacterisedVariable_Variable, gen_pcm_seff_StopAction_AbstractInternalControlFlowAction, gen_pcm_seff_AbstractInternalControlFlowAction_AbstractAction, gen_pcm_seff_AbstractAction_Entity, gen_pcm_seff_StartAction_AbstractInternalControlFlowAction, gen_pcm_seff_ResourceDemandingSEFF_Identifier, gen_pcm_seff_ResourceDemandingSEFF_seff_ServiceEffectSpecification, gen_pcm_seff_ResourceDemandingSEFF_seff_ResourceDemandingBehaviour, gen_pcm_seff_ReleaseAction_AbstractInternalControlFlowAction, gen_pcm_seff_LoopAction_AbstractLoopAction, gen_pcm_seff_AbstractLoopAction_AbstractInternalControlFlowAction, gen_pcm_seff_InternalAction_AbstractInternalControlFlowAction, gen_pcm_seff_AbstractBranchTransition_NamedElement, gen_pcm_seff_ForkAction_AbstractInternalControlFlowAction, gen_pcm_seff_ForkedBehaviour_ResourceDemandingBehaviour, gen_pcm_seff_ExternalCallAction_AbstractAction, gen_pcm_seff_ProbabilisticBranchTransition_AbstractBranchTransition, gen_pcm_seff_SetVariableAction_AbstractInternalControlFlowAction, gen_pcm_seff_BranchAction_AbstractInternalControlFlowAction, gen_pcm_seff_AcquireAction_AbstractInternalControlFlowAction, gen_pcm_seff_CollectionIteratorAction_AbstractLoopAction, gen_pcm_seff_GuardedBranchTransition_AbstractBranchTransition, gen_pcm_allocation_AllocationContext_Entity, gen_pcm_resourcetype_ResourceType_entity_Entity, gen_pcm_resourcetype_ResourceType_UnitCarryingElement, gen_pcm_resourcetype_CommunicationLinkResourceType_ProcessingResourceType, gen_pcm_resourcetype_ProcessingResourceType_ResourceType, gen_pcm_allocation_Allocation_Entity, gen_pcm_resourceenvironment_LinkingResource_Entity, gen_pcm_resourceenvironment_ResourceContainer_Entity, gen_pcm_performance_SystemSpecifiedExecutionTime_SpecifiedQoSAnnotation, gen_pcm_performance_ComponentSpecifiedExecutionTime_SpecifiedQoSAnnotation, gen_pcm_system_System_entity_Entity, gen_pcm_system_System_entity_ComposedProvidingRequiringEntity, gen_pcm_qosannotations_QoSAnnotations_Entity, gen_pcm_reliability_SpecifiedFailureProbability_SpecifiedQoSAnnotation, gen_pcm_usagemodel_UsageScenario_Entity, gen_pcm_usagemodel_ScenarioBehaviour_Entity, gen_pcm_usagemodel_Start_AbstractUserAction, gen_pcm_usagemodel_AbstractUserAction_Entity, gen_pcm_usagemodel_Stop_AbstractUserAction, gen_pcm_usagemodel_OpenWorkload_Workload, gen_pcm_usagemodel_Loop_AbstractUserAction, gen_pcm_usagemodel_EntryLevelSystemCall_AbstractUserAction, gen_pcm_usagemodel_ClosedWorkload_Workload, gen_pcm_usagemodel_Branch_AbstractUserAction, gen_pcm_usagemodel_Delay_AbstractUserAction, gen_pcm_subsystem_SubSystem_entity_ComposedProvidingRequiringEntity, gen_pcm_subsystem_SubSystem_repository_RepositoryComponent},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)