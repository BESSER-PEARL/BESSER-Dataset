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
pcm_entity_InterfaceRequiringEntity = Class(name="pcm_entity_InterfaceRequiringEntity", is_abstract=True)
RequiredRole = Class(name="RequiredRole")
pcm_entity_ComposedProvidingRequiringEntity = Class(name="pcm_entity_ComposedProvidingRequiringEntity", is_abstract=True)
composition_ComposedStructure = Class(name="composition_ComposedStructure")
entity_InterfaceProvidingRequiringEntity = Class(name="entity_InterfaceProvidingRequiringEntity")
pcm_connectors_Connector = Class(name="pcm_connectors_Connector", is_abstract=True)
pcm_composition_ProvidedDelegationConnector = Class(name="pcm_composition_ProvidedDelegationConnector")
DelegationConnector = Class(name="DelegationConnector")
composition_AssemblyContext = Class(name="composition_AssemblyContext")
pcm_composition_AssemblyContext = Class(name="pcm_composition_AssemblyContext")
ProvidesComponentType = Class(name="ProvidesComponentType")
VariableUsage = Class(name="VariableUsage")
pcm_composition_RequiredDelegationConnector = Class(name="pcm_composition_RequiredDelegationConnector")
pcm_composition_AssemblyConnector = Class(name="pcm_composition_AssemblyConnector")
connectors_Connector = Class(name="connectors_Connector")
entity_Entity = Class(name="entity_Entity")
pcm_composition_ComposedStructure = Class(name="pcm_composition_ComposedStructure", is_abstract=True)
composition_ProvidedDelegationConnector = Class(name="composition_ProvidedDelegationConnector")
composition_RequiredDelegationConnector = Class(name="composition_RequiredDelegationConnector")
composition_AssemblyConnector = Class(name="composition_AssemblyConnector")
pcm_repository_PassiveResource = Class(name="pcm_repository_PassiveResource")
PCMRandomVariable = Class(name="PCMRandomVariable")
pcm_repository_Signature = Class(name="pcm_repository_Signature")
Parameter_ = Class(name="Parameter")
Interface = Class(name="Interface")
DataType = Class(name="DataType")
ExceptionType = Class(name="ExceptionType")
pcm_repository_Parameter = Class(name="pcm_repository_Parameter")
Signature = Class(name="Signature")
pcm_repository_DataType = Class(name="pcm_repository_DataType", is_abstract=True)
Repository = Class(name="Repository")
pcm_repository_Repository = Class(name="pcm_repository_Repository")
pcm_repository_ProvidesComponentType = Class(name="pcm_repository_ProvidesComponentType")
pcm_repository_RequiredRole = Class(name="pcm_repository_RequiredRole")
Role = Class(name="Role")
pcm_repository_Role = Class(name="pcm_repository_Role", is_abstract=True)
pcm_repository_Interface = Class(name="pcm_repository_Interface")
Protocol = Class(name="Protocol")
pcm_repository_ExceptionType = Class(name="pcm_repository_ExceptionType")
pcm_repository_ImplementationComponentType = Class(name="pcm_repository_ImplementationComponentType", is_abstract=True)
CompleteComponentType = Class(name="CompleteComponentType")
pcm_repository_CompleteComponentType = Class(name="pcm_repository_CompleteComponentType")
pcm_repository_DelegationConnector = Class(name="pcm_repository_DelegationConnector", is_abstract=True)
Connector = Class(name="Connector")
pcm_repository_CompositeComponent = Class(name="pcm_repository_CompositeComponent")
repository_ImplementationComponentType = Class(name="repository_ImplementationComponentType")
entity_ComposedProvidingRequiringEntity = Class(name="entity_ComposedProvidingRequiringEntity")
ImplementationComponentType = Class(name="ImplementationComponentType")
pcm_repository_CollectionDataType = Class(name="pcm_repository_CollectionDataType")
pcm_repository_BasicComponent = Class(name="pcm_repository_BasicComponent")
ServiceEffectSpecification = Class(name="ServiceEffectSpecification")
PassiveResource = Class(name="PassiveResource")
pcm_repository_PrimitiveDataType = Class(name="pcm_repository_PrimitiveDataType")
repository_DataType = Class(name="repository_DataType")
pcm_repository_CompositeDataType = Class(name="pcm_repository_CompositeDataType")
CompositeDataType = Class(name="CompositeDataType")
InnerDeclaration = Class(name="InnerDeclaration")
pcm_repository_InnerDeclaration = Class(name="pcm_repository_InnerDeclaration")
NamedElement = Class(name="NamedElement")
pcm_repository_ProvidedRole = Class(name="pcm_repository_ProvidedRole")
ParametricResourceDemand = Class(name="ParametricResourceDemand")
pcm_protocol_ServiceCall = Class(name="pcm_protocol_ServiceCall", is_abstract=True)
pcm_protocol_Protocol = Class(name="pcm_protocol_Protocol", is_abstract=True)
pcm_parameter_VariableCharacterisation = Class(name="pcm_parameter_VariableCharacterisation")
pcm_parameter_CharacterisedVariable = Class(name="pcm_parameter_CharacterisedVariable")
Variable = Class(name="Variable")
pcm_parameter_VariableUsage = Class(name="pcm_parameter_VariableUsage")
VariableCharacterisation = Class(name="VariableCharacterisation")
parameter_pcm_AbstractNamedReference = Class(name="parameter_pcm_AbstractNamedReference")
pcm_seff_StopAction = Class(name="pcm_seff_StopAction")
AbstractResourceDemandingAction = Class(name="AbstractResourceDemandingAction")
pcm_seff_AbstractResourceDemandingAction = Class(name="pcm_seff_AbstractResourceDemandingAction", is_abstract=True)
AbstractAction = Class(name="AbstractAction")
pcm_seff_AbstractAction = Class(name="pcm_seff_AbstractAction", is_abstract=True)
pcm_seff_ParametricResourceDemand = Class(name="pcm_seff_ParametricResourceDemand")
ProcessingResourceType = Class(name="ProcessingResourceType")
pcm_seff_StartAction = Class(name="pcm_seff_StartAction")
pcm_seff_ResourceDemandingSEFF = Class(name="pcm_seff_ResourceDemandingSEFF")
seff_ServiceEffectSpecification = Class(name="seff_ServiceEffectSpecification")
seff_ResourceDemandingBehaviour = Class(name="seff_ResourceDemandingBehaviour")
pcm_seff_ResourceDemandingBehaviour = Class(name="pcm_seff_ResourceDemandingBehaviour")
pcm_seff_SynchronisationPoint = Class(name="pcm_seff_SynchronisationPoint")
pcm_seff_ReleaseAction = Class(name="pcm_seff_ReleaseAction")
pcm_seff_LoopAction = Class(name="pcm_seff_LoopAction")
AbstractLoopAction = Class(name="AbstractLoopAction")
pcm_seff_AbstractLoopAction = Class(name="pcm_seff_AbstractLoopAction", is_abstract=True)
ResourceDemandingBehaviour = Class(name="ResourceDemandingBehaviour")
pcm_seff_InternalAction = Class(name="pcm_seff_InternalAction")
pcm_seff_ForkAction = Class(name="pcm_seff_ForkAction")
ForkedBehaviour = Class(name="ForkedBehaviour")
SynchronisationPoint = Class(name="SynchronisationPoint")
pcm_seff_ForkedBehaviour = Class(name="pcm_seff_ForkedBehaviour")
pcm_seff_ExternalCallAction = Class(name="pcm_seff_ExternalCallAction")
pcm_seff_ProbabilisticBranchTransition = Class(name="pcm_seff_ProbabilisticBranchTransition")
AbstractBranchTransition = Class(name="AbstractBranchTransition")
pcm_seff_AbstractBranchTransition = Class(name="pcm_seff_AbstractBranchTransition", is_abstract=True)
pcm_seff_BranchAction = Class(name="pcm_seff_BranchAction")
pcm_seff_AcquireAction = Class(name="pcm_seff_AcquireAction")
pcm_seff_CollectionIteratorAction = Class(name="pcm_seff_CollectionIteratorAction")
pcm_seff_GuardedBranchTransition = Class(name="pcm_seff_GuardedBranchTransition")
pcm_seff_SetVariableAction = Class(name="pcm_seff_SetVariableAction")
pcm_seff_ServiceEffectSpecification = Class(name="pcm_seff_ServiceEffectSpecification", is_abstract=True)
pcm_resourcetype_ResourceType = Class(name="pcm_resourcetype_ResourceType", is_abstract=True)
UnitCarryingElement = Class(name="UnitCarryingElement")
pcm_resourcetype_ResourceRepository = Class(name="pcm_resourcetype_ResourceRepository")
ResourceType = Class(name="ResourceType")
pcm_resourcetype_CommunicationLinkResourceType = Class(name="pcm_resourcetype_CommunicationLinkResourceType")
pcm_resourcetype_ProcessingResourceType = Class(name="pcm_resourcetype_ProcessingResourceType")
pcm_allocation_AllocationContext = Class(name="pcm_allocation_AllocationContext")
pcm_resourceenvironment_LinkingResource = Class(name="pcm_resourceenvironment_LinkingResource")
ResourceContainer = Class(name="ResourceContainer")
pcm_allocation_Allocation = Class(name="pcm_allocation_Allocation")
AllocationContext = Class(name="AllocationContext")
ResourceEnvironment = Class(name="ResourceEnvironment")
System = Class(name="System")
pcm_resourceenvironment_ResourceEnvironment = Class(name="pcm_resourceenvironment_ResourceEnvironment")
LinkingResource = Class(name="LinkingResource")
CommunicationLinkResourceSpecification = Class(name="CommunicationLinkResourceSpecification")
pcm_resourceenvironment_CommunicationLinkResourceSpecification = Class(name="pcm_resourceenvironment_CommunicationLinkResourceSpecification")
CommunicationLinkResourceType = Class(name="CommunicationLinkResourceType")
pcm_resourceenvironment_ProcessingResourceSpecification = Class(name="pcm_resourceenvironment_ProcessingResourceSpecification")
pcm_resourceenvironment_ResourceContainer = Class(name="pcm_resourceenvironment_ResourceContainer")
ProcessingResourceSpecification = Class(name="ProcessingResourceSpecification")
pcm_system_System = Class(name="pcm_system_System")
QoSAnnotations = Class(name="QoSAnnotations")
pcm_qosannotations_SpecifiedExecutionTime = Class(name="pcm_qosannotations_SpecifiedExecutionTime", is_abstract=True)
pcm_qosannotations_SpecifiedFailureProbability = Class(name="pcm_qosannotations_SpecifiedFailureProbability")
pcm_qosannotations_SystemSpecifiedExecutionTime = Class(name="pcm_qosannotations_SystemSpecifiedExecutionTime")
SpecifiedExecutionTime = Class(name="SpecifiedExecutionTime")
pcm_qosannotations_ComponentSpecifiedExecutionTime = Class(name="pcm_qosannotations_ComponentSpecifiedExecutionTime")
pcm_qosannotations_SpecifiedOutputParameterAbstraction = Class(name="pcm_qosannotations_SpecifiedOutputParameterAbstraction")
pcm_qosannotations_QoSAnnotations = Class(name="pcm_qosannotations_QoSAnnotations")
SpecifiedOutputParameterAbstraction = Class(name="SpecifiedOutputParameterAbstraction")
pcm_usagemodel_Workload = Class(name="pcm_usagemodel_Workload", is_abstract=True)
pcm_usagemodel_UsageScenario = Class(name="pcm_usagemodel_UsageScenario")
Workload = Class(name="Workload")
ScenarioBehaviour = Class(name="ScenarioBehaviour")
pcm_usagemodel_ScenarioBehaviour = Class(name="pcm_usagemodel_ScenarioBehaviour")
AbstractUserAction = Class(name="AbstractUserAction")
pcm_usagemodel_AbstractUserAction = Class(name="pcm_usagemodel_AbstractUserAction", is_abstract=True)
pcm_usagemodel_UsageModel = Class(name="pcm_usagemodel_UsageModel")
UsageScenario = Class(name="UsageScenario")
UserData = Class(name="UserData")
pcm_usagemodel_UserData = Class(name="pcm_usagemodel_UserData")
pcm_usagemodel_Stop = Class(name="pcm_usagemodel_Stop")
pcm_usagemodel_Start = Class(name="pcm_usagemodel_Start")
pcm_usagemodel_ClosedWorkload = Class(name="pcm_usagemodel_ClosedWorkload")
pcm_usagemodel_OpenWorkload = Class(name="pcm_usagemodel_OpenWorkload")
pcm_usagemodel_Loop = Class(name="pcm_usagemodel_Loop")
pcm_usagemodel_EntryLevelSystemCall = Class(name="pcm_usagemodel_EntryLevelSystemCall")
BranchTransition = Class(name="BranchTransition")
pcm_usagemodel_BranchTransition = Class(name="pcm_usagemodel_BranchTransition")
pcm_usagemodel_Delay = Class(name="pcm_usagemodel_Delay")
pcm_usagemodel_Branch = Class(name="pcm_usagemodel_Branch")

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

# pcm_entity_InterfaceRequiringEntity class attributes and methods

# RequiredRole class attributes and methods

# pcm_entity_ComposedProvidingRequiringEntity class attributes and methods

# composition_ComposedStructure class attributes and methods

# entity_InterfaceProvidingRequiringEntity class attributes and methods

# pcm_connectors_Connector class attributes and methods

# pcm_composition_ProvidedDelegationConnector class attributes and methods
pcm_composition_ProvidedDelegationConnector_m_ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure: Method = Method(name="ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure", parameters={Parameter(name='pcm_context', type=StringType), Parameter(name='pcm_diagnostics', type=StringType)}, type=BooleanType)
pcm_composition_ProvidedDelegationConnector_m_ComponentOfChildComponentContextAndInnerRoleProvidingComponentNeedToBeTheSame: Method = Method(name="ComponentOfChildComponentContextAndInnerRoleProvidingComponentNeedToBeTheSame", parameters={Parameter(name='pcm_diagnostics', type=StringType), Parameter(name='pcm_context', type=StringType)}, type=BooleanType)
pcm_composition_ProvidedDelegationConnector.methods={pcm_composition_ProvidedDelegationConnector_m_ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure, pcm_composition_ProvidedDelegationConnector_m_ComponentOfChildComponentContextAndInnerRoleProvidingComponentNeedToBeTheSame}

# DelegationConnector class attributes and methods

# composition_AssemblyContext class attributes and methods

# pcm_composition_AssemblyContext class attributes and methods

# ProvidesComponentType class attributes and methods

# VariableUsage class attributes and methods

# pcm_composition_RequiredDelegationConnector class attributes and methods
pcm_composition_RequiredDelegationConnector_m_RequiredDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure: Method = Method(name="RequiredDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure", parameters={Parameter(name='pcm_context', type=StringType), Parameter(name='pcm_diagnostics', type=StringType)}, type=BooleanType)
pcm_composition_RequiredDelegationConnector_m_ComponentOfChildComponentContextAndInnerRoleRequiringComponentNeedToBeTheSame: Method = Method(name="ComponentOfChildComponentContextAndInnerRoleRequiringComponentNeedToBeTheSame", parameters={Parameter(name='pcm_context', type=StringType), Parameter(name='pcm_diagnostics', type=StringType)}, type=BooleanType)
pcm_composition_RequiredDelegationConnector.methods={pcm_composition_RequiredDelegationConnector_m_RequiredDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure, pcm_composition_RequiredDelegationConnector_m_ComponentOfChildComponentContextAndInnerRoleRequiringComponentNeedToBeTheSame}

# pcm_composition_AssemblyConnector class attributes and methods

# connectors_Connector class attributes and methods

# entity_Entity class attributes and methods

# pcm_composition_ComposedStructure class attributes and methods

# composition_ProvidedDelegationConnector class attributes and methods

# composition_RequiredDelegationConnector class attributes and methods

# composition_AssemblyConnector class attributes and methods

# pcm_repository_PassiveResource class attributes and methods

# PCMRandomVariable class attributes and methods

# pcm_repository_Signature class attributes and methods
pcm_repository_Signature_serviceName: Property = Property(name="serviceName", type=StringType)
pcm_repository_Signature_m_ParameterNamesHaveToBeUniqueForASignature: Method = Method(name="ParameterNamesHaveToBeUniqueForASignature", parameters={Parameter(name='pcm_diagnostics', type=StringType), Parameter(name='pcm_context', type=StringType)}, type=BooleanType)
pcm_repository_Signature.attributes={pcm_repository_Signature_serviceName}
pcm_repository_Signature.methods={pcm_repository_Signature_m_ParameterNamesHaveToBeUniqueForASignature}

# Parameter class attributes and methods

# Interface class attributes and methods

# DataType class attributes and methods

# ExceptionType class attributes and methods

# pcm_repository_Parameter class attributes and methods
pcm_repository_Parameter_parameterName: Property = Property(name="parameterName", type=StringType)
pcm_repository_Parameter_modifier__Parameter: Property = Property(name="modifier__Parameter", type=StringType)
pcm_repository_Parameter.attributes={pcm_repository_Parameter_parameterName, pcm_repository_Parameter_modifier__Parameter}

# Signature class attributes and methods

# pcm_repository_DataType class attributes and methods

# Repository class attributes and methods

# pcm_repository_Repository class attributes and methods
pcm_repository_Repository_repositoryDescription: Property = Property(name="repositoryDescription", type=StringType)
pcm_repository_Repository.attributes={pcm_repository_Repository_repositoryDescription}

# pcm_repository_ProvidesComponentType class attributes and methods
pcm_repository_ProvidesComponentType_m_AtLeastOneInterfaceHasToBeProvidedByAUsefullProvidesComponentType: Method = Method(name="AtLeastOneInterfaceHasToBeProvidedByAUsefullProvidesComponentType", parameters={Parameter(name='pcm_diagnostics', type=StringType), Parameter(name='pcm_context', type=StringType)}, type=BooleanType)
pcm_repository_ProvidesComponentType.methods={pcm_repository_ProvidesComponentType_m_AtLeastOneInterfaceHasToBeProvidedByAUsefullProvidesComponentType}

# pcm_repository_RequiredRole class attributes and methods

# Role class attributes and methods

# pcm_repository_Role class attributes and methods

# pcm_repository_Interface class attributes and methods
pcm_repository_Interface_m_NoProtocolTypeIDUsedTwice: Method = Method(name="NoProtocolTypeIDUsedTwice", parameters={Parameter(name='pcm_context', type=StringType), Parameter(name='pcm_diagnostics', type=StringType)}, type=BooleanType)
pcm_repository_Interface_m_SignaturesHaveToBeUniqueForAnInterface: Method = Method(name="SignaturesHaveToBeUniqueForAnInterface", parameters={Parameter(name='pcm_diagnostics', type=StringType), Parameter(name='pcm_context', type=StringType)}, type=BooleanType)
pcm_repository_Interface.methods={pcm_repository_Interface_m_NoProtocolTypeIDUsedTwice, pcm_repository_Interface_m_SignaturesHaveToBeUniqueForAnInterface}

# Protocol class attributes and methods

# pcm_repository_ExceptionType class attributes and methods
pcm_repository_ExceptionType_exceptionName: Property = Property(name="exceptionName", type=StringType)
pcm_repository_ExceptionType_exceptionMessage: Property = Property(name="exceptionMessage", type=StringType)
pcm_repository_ExceptionType.attributes={pcm_repository_ExceptionType_exceptionMessage, pcm_repository_ExceptionType_exceptionName}

# pcm_repository_ImplementationComponentType class attributes and methods
pcm_repository_ImplementationComponentType_m_RequiredInterfacesHaveToConformToCompleteType: Method = Method(name="RequiredInterfacesHaveToConformToCompleteType", parameters={Parameter(name='pcm_context', type=StringType), Parameter(name='pcm_diagnostics', type=StringType)}, type=BooleanType)
pcm_repository_ImplementationComponentType_m_providedInterfacesHaveToConformToCompleteType: Method = Method(name="providedInterfacesHaveToConformToCompleteType", parameters={Parameter(name='pcm_context', type=StringType), Parameter(name='pcm_diagnostics', type=StringType)}, type=BooleanType)
pcm_repository_ImplementationComponentType.methods={pcm_repository_ImplementationComponentType_m_RequiredInterfacesHaveToConformToCompleteType, pcm_repository_ImplementationComponentType_m_providedInterfacesHaveToConformToCompleteType}

# CompleteComponentType class attributes and methods

# pcm_repository_CompleteComponentType class attributes and methods
pcm_repository_CompleteComponentType_m_AtLeastOneInterfaceHasToBeProvidedOrRequiredByAUsefullCompleteComponentType: Method = Method(name="AtLeastOneInterfaceHasToBeProvidedOrRequiredByAUsefullCompleteComponentType", parameters={Parameter(name='pcm_context', type=StringType), Parameter(name='pcm_diagnostics', type=StringType)}, type=BooleanType)
pcm_repository_CompleteComponentType_m_providedInterfacesHaveToConformToProvidedType2: Method = Method(name="providedInterfacesHaveToConformToProvidedType2", parameters={Parameter(name='pcm_diagnostics', type=StringType), Parameter(name='pcm_context', type=StringType)}, type=BooleanType)
pcm_repository_CompleteComponentType.methods={pcm_repository_CompleteComponentType_m_AtLeastOneInterfaceHasToBeProvidedOrRequiredByAUsefullCompleteComponentType, pcm_repository_CompleteComponentType_m_providedInterfacesHaveToConformToProvidedType2}

# pcm_repository_DelegationConnector class attributes and methods

# Connector class attributes and methods

# pcm_repository_CompositeComponent class attributes and methods
pcm_repository_CompositeComponent_m_ProvideSameInterfaces: Method = Method(name="ProvideSameInterfaces", parameters={Parameter(name='pcm_context', type=StringType), Parameter(name='pcm_diagnostics', type=StringType)}, type=BooleanType)
pcm_repository_CompositeComponent_m_RequireSameInterfaces: Method = Method(name="RequireSameInterfaces", parameters={Parameter(name='pcm_diagnostics', type=StringType), Parameter(name='pcm_context', type=StringType)}, type=BooleanType)
pcm_repository_CompositeComponent.methods={pcm_repository_CompositeComponent_m_RequireSameInterfaces, pcm_repository_CompositeComponent_m_ProvideSameInterfaces}

# repository_ImplementationComponentType class attributes and methods

# entity_ComposedProvidingRequiringEntity class attributes and methods

# ImplementationComponentType class attributes and methods

# pcm_repository_CollectionDataType class attributes and methods

# pcm_repository_BasicComponent class attributes and methods
pcm_repository_BasicComponent_m_NoSeffTypeUsedTwice: Method = Method(name="NoSeffTypeUsedTwice", parameters={Parameter(name='pcm_diagnostics', type=StringType), Parameter(name='pcm_context', type=StringType)}, type=BooleanType)
pcm_repository_BasicComponent_m_ProvideSameInterfacesAsImplementationType: Method = Method(name="ProvideSameInterfacesAsImplementationType", parameters={Parameter(name='pcm_context', type=StringType), Parameter(name='pcm_diagnostics', type=StringType)}, type=BooleanType)
pcm_repository_BasicComponent_m_RequireSameInterfacesAsImplementationType: Method = Method(name="RequireSameInterfacesAsImplementationType", parameters={Parameter(name='pcm_context', type=StringType), Parameter(name='pcm_diagnostics', type=StringType)}, type=BooleanType)
pcm_repository_BasicComponent.methods={pcm_repository_BasicComponent_m_NoSeffTypeUsedTwice, pcm_repository_BasicComponent_m_RequireSameInterfacesAsImplementationType, pcm_repository_BasicComponent_m_ProvideSameInterfacesAsImplementationType}

# ServiceEffectSpecification class attributes and methods

# PassiveResource class attributes and methods

# pcm_repository_PrimitiveDataType class attributes and methods
pcm_repository_PrimitiveDataType_type: Property = Property(name="type", type=StringType)
pcm_repository_PrimitiveDataType.attributes={pcm_repository_PrimitiveDataType_type}

# repository_DataType class attributes and methods

# pcm_repository_CompositeDataType class attributes and methods

# CompositeDataType class attributes and methods

# InnerDeclaration class attributes and methods

# pcm_repository_InnerDeclaration class attributes and methods

# NamedElement class attributes and methods

# pcm_repository_ProvidedRole class attributes and methods

# ParametricResourceDemand class attributes and methods

# pcm_protocol_ServiceCall class attributes and methods

# pcm_protocol_Protocol class attributes and methods
pcm_protocol_Protocol_protocolTypeID: Property = Property(name="protocolTypeID", type=StringType)
pcm_protocol_Protocol.attributes={pcm_protocol_Protocol_protocolTypeID}

# pcm_parameter_VariableCharacterisation class attributes and methods
pcm_parameter_VariableCharacterisation_type: Property = Property(name="type", type=StringType)
pcm_parameter_VariableCharacterisation.attributes={pcm_parameter_VariableCharacterisation_type}

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

# AbstractResourceDemandingAction class attributes and methods

# pcm_seff_AbstractResourceDemandingAction class attributes and methods

# AbstractAction class attributes and methods

# pcm_seff_AbstractAction class attributes and methods

# pcm_seff_ParametricResourceDemand class attributes and methods

# ProcessingResourceType class attributes and methods

# pcm_seff_StartAction class attributes and methods
pcm_seff_StartAction_m_StartActionPredecessorMustNotBeDefined: Method = Method(name="StartActionPredecessorMustNotBeDefined", parameters={Parameter(name='pcm_diagnostics', type=StringType), Parameter(name='pcm_context', type=StringType)}, type=BooleanType)
pcm_seff_StartAction.methods={pcm_seff_StartAction_m_StartActionPredecessorMustNotBeDefined}

# pcm_seff_ResourceDemandingSEFF class attributes and methods

# seff_ServiceEffectSpecification class attributes and methods

# seff_ResourceDemandingBehaviour class attributes and methods

# pcm_seff_ResourceDemandingBehaviour class attributes and methods
pcm_seff_ResourceDemandingBehaviour_m_ExactlyOneStopAction: Method = Method(name="ExactlyOneStopAction", parameters={Parameter(name='pcm_context', type=StringType), Parameter(name='pcm_diagnostics', type=StringType)}, type=BooleanType)
pcm_seff_ResourceDemandingBehaviour_m_ExactlyOneStartAction: Method = Method(name="ExactlyOneStartAction", parameters={Parameter(name='pcm_diagnostics', type=StringType), Parameter(name='pcm_context', type=StringType)}, type=BooleanType)
pcm_seff_ResourceDemandingBehaviour_m_EachActionExceptStartActionandStopActionMustHhaveAPredecessorAndSuccessor: Method = Method(name="EachActionExceptStartActionandStopActionMustHhaveAPredecessorAndSuccessor", parameters={Parameter(name='pcm_diagnostics', type=StringType), Parameter(name='pcm_context', type=StringType)}, type=BooleanType)
pcm_seff_ResourceDemandingBehaviour.methods={pcm_seff_ResourceDemandingBehaviour_m_ExactlyOneStartAction, pcm_seff_ResourceDemandingBehaviour_m_ExactlyOneStopAction, pcm_seff_ResourceDemandingBehaviour_m_EachActionExceptStartActionandStopActionMustHhaveAPredecessorAndSuccessor}

# pcm_seff_SynchronisationPoint class attributes and methods

# pcm_seff_ReleaseAction class attributes and methods

# pcm_seff_LoopAction class attributes and methods

# AbstractLoopAction class attributes and methods

# pcm_seff_AbstractLoopAction class attributes and methods

# ResourceDemandingBehaviour class attributes and methods

# pcm_seff_InternalAction class attributes and methods
pcm_seff_InternalAction_failureProbability: Property = Property(name="failureProbability", type=StringType)
pcm_seff_InternalAction.attributes={pcm_seff_InternalAction_failureProbability}

# pcm_seff_ForkAction class attributes and methods

# ForkedBehaviour class attributes and methods

# SynchronisationPoint class attributes and methods

# pcm_seff_ForkedBehaviour class attributes and methods

# pcm_seff_ExternalCallAction class attributes and methods

# pcm_seff_ProbabilisticBranchTransition class attributes and methods
pcm_seff_ProbabilisticBranchTransition_branchProbability: Property = Property(name="branchProbability", type=FloatType)
pcm_seff_ProbabilisticBranchTransition.attributes={pcm_seff_ProbabilisticBranchTransition_branchProbability}

# AbstractBranchTransition class attributes and methods

# pcm_seff_AbstractBranchTransition class attributes and methods

# pcm_seff_BranchAction class attributes and methods
pcm_seff_BranchAction_m_EitherGuardedBranchesOrProbabilisiticBranchTransitions: Method = Method(name="EitherGuardedBranchesOrProbabilisiticBranchTransitions", parameters={Parameter(name='pcm_context', type=StringType), Parameter(name='pcm_diagnostics', type=StringType)}, type=BooleanType)
pcm_seff_BranchAction_m_AllProbabilisticBranchProbabilitiesMustSumUpTo1: Method = Method(name="AllProbabilisticBranchProbabilitiesMustSumUpTo1", parameters={Parameter(name='pcm_context', type=StringType), Parameter(name='pcm_diagnostics', type=StringType)}, type=BooleanType)
pcm_seff_BranchAction.methods={pcm_seff_BranchAction_m_AllProbabilisticBranchProbabilitiesMustSumUpTo1, pcm_seff_BranchAction_m_EitherGuardedBranchesOrProbabilisiticBranchTransitions}

# pcm_seff_AcquireAction class attributes and methods

# pcm_seff_CollectionIteratorAction class attributes and methods

# pcm_seff_GuardedBranchTransition class attributes and methods

# pcm_seff_SetVariableAction class attributes and methods

# pcm_seff_ServiceEffectSpecification class attributes and methods
pcm_seff_ServiceEffectSpecification_seffTypeID: Property = Property(name="seffTypeID", type=StringType)
pcm_seff_ServiceEffectSpecification.attributes={pcm_seff_ServiceEffectSpecification_seffTypeID}

# pcm_resourcetype_ResourceType class attributes and methods

# UnitCarryingElement class attributes and methods

# pcm_resourcetype_ResourceRepository class attributes and methods

# ResourceType class attributes and methods

# pcm_resourcetype_CommunicationLinkResourceType class attributes and methods

# pcm_resourcetype_ProcessingResourceType class attributes and methods

# pcm_allocation_AllocationContext class attributes and methods

# pcm_resourceenvironment_LinkingResource class attributes and methods

# ResourceContainer class attributes and methods

# pcm_allocation_Allocation class attributes and methods
pcm_allocation_Allocation_m_EachAssemblyContextWithinSystemHasToBeAllocatedExactlyOnce: Method = Method(name="EachAssemblyContextWithinSystemHasToBeAllocatedExactlyOnce", parameters={Parameter(name='pcm_context', type=StringType), Parameter(name='pcm_diagnostics', type=StringType)}, type=BooleanType)
pcm_allocation_Allocation.methods={pcm_allocation_Allocation_m_EachAssemblyContextWithinSystemHasToBeAllocatedExactlyOnce}

# AllocationContext class attributes and methods

# ResourceEnvironment class attributes and methods

# System class attributes and methods

# pcm_resourceenvironment_ResourceEnvironment class attributes and methods

# LinkingResource class attributes and methods

# CommunicationLinkResourceSpecification class attributes and methods

# pcm_resourceenvironment_CommunicationLinkResourceSpecification class attributes and methods

# CommunicationLinkResourceType class attributes and methods

# pcm_resourceenvironment_ProcessingResourceSpecification class attributes and methods
pcm_resourceenvironment_ProcessingResourceSpecification_schedulingPolicy: Property = Property(name="schedulingPolicy", type=StringType)
pcm_resourceenvironment_ProcessingResourceSpecification.attributes={pcm_resourceenvironment_ProcessingResourceSpecification_schedulingPolicy}

# pcm_resourceenvironment_ResourceContainer class attributes and methods

# ProcessingResourceSpecification class attributes and methods

# pcm_system_System class attributes and methods

# QoSAnnotations class attributes and methods

# pcm_qosannotations_SpecifiedExecutionTime class attributes and methods

# pcm_qosannotations_SpecifiedFailureProbability class attributes and methods

# pcm_qosannotations_SystemSpecifiedExecutionTime class attributes and methods

# SpecifiedExecutionTime class attributes and methods

# pcm_qosannotations_ComponentSpecifiedExecutionTime class attributes and methods

# pcm_qosannotations_SpecifiedOutputParameterAbstraction class attributes and methods

# pcm_qosannotations_QoSAnnotations class attributes and methods

# SpecifiedOutputParameterAbstraction class attributes and methods

# pcm_usagemodel_Workload class attributes and methods

# pcm_usagemodel_UsageScenario class attributes and methods

# Workload class attributes and methods

# ScenarioBehaviour class attributes and methods

# pcm_usagemodel_ScenarioBehaviour class attributes and methods
pcm_usagemodel_ScenarioBehaviour_m_Exactlyonestart: Method = Method(name="Exactlyonestart", parameters={Parameter(name='pcm_context', type=StringType), Parameter(name='pcm_diagnostics', type=StringType)}, type=BooleanType)
pcm_usagemodel_ScenarioBehaviour_m_Exactlyonestop: Method = Method(name="Exactlyonestop", parameters={Parameter(name='pcm_diagnostics', type=StringType), Parameter(name='pcm_context', type=StringType)}, type=BooleanType)
pcm_usagemodel_ScenarioBehaviour_m_EachuseractionexceptStartandStopmusthaveapredecessorandsuccessor: Method = Method(name="EachuseractionexceptStartandStopmusthaveapredecessorandsuccessor", parameters={Parameter(name='pcm_context', type=StringType), Parameter(name='pcm_diagnostics', type=StringType)}, type=BooleanType)
pcm_usagemodel_ScenarioBehaviour.methods={pcm_usagemodel_ScenarioBehaviour_m_Exactlyonestart, pcm_usagemodel_ScenarioBehaviour_m_EachuseractionexceptStartandStopmusthaveapredecessorandsuccessor, pcm_usagemodel_ScenarioBehaviour_m_Exactlyonestop}

# AbstractUserAction class attributes and methods

# pcm_usagemodel_AbstractUserAction class attributes and methods

# pcm_usagemodel_UsageModel class attributes and methods

# UsageScenario class attributes and methods

# UserData class attributes and methods

# pcm_usagemodel_UserData class attributes and methods

# pcm_usagemodel_Stop class attributes and methods
pcm_usagemodel_Stop_m_StopHasNoSuccessor: Method = Method(name="StopHasNoSuccessor", parameters={Parameter(name='pcm_context', type=StringType), Parameter(name='pcm_diagnostics', type=StringType)}, type=BooleanType)
pcm_usagemodel_Stop.methods={pcm_usagemodel_Stop_m_StopHasNoSuccessor}

# pcm_usagemodel_Start class attributes and methods
pcm_usagemodel_Start_m_StartHasNoPredecessor: Method = Method(name="StartHasNoPredecessor", parameters={Parameter(name='pcm_context', type=StringType), Parameter(name='pcm_diagnostics', type=StringType)}, type=BooleanType)
pcm_usagemodel_Start.methods={pcm_usagemodel_Start_m_StartHasNoPredecessor}

# pcm_usagemodel_ClosedWorkload class attributes and methods
pcm_usagemodel_ClosedWorkload_population: Property = Property(name="population", type=IntegerType)
pcm_usagemodel_ClosedWorkload_m_PopulationInClosedWorkloadNeedsToBeSpecified: Method = Method(name="PopulationInClosedWorkloadNeedsToBeSpecified", parameters={Parameter(name='pcm_context', type=StringType), Parameter(name='pcm_diagnostics', type=StringType)}, type=BooleanType)
pcm_usagemodel_ClosedWorkload_m_ThinkTimeInClosedWorkloadNeedsToBeSpecified: Method = Method(name="ThinkTimeInClosedWorkloadNeedsToBeSpecified", parameters={Parameter(name='pcm_diagnostics', type=StringType), Parameter(name='pcm_context', type=StringType)}, type=BooleanType)
pcm_usagemodel_ClosedWorkload.attributes={pcm_usagemodel_ClosedWorkload_population}
pcm_usagemodel_ClosedWorkload.methods={pcm_usagemodel_ClosedWorkload_m_PopulationInClosedWorkloadNeedsToBeSpecified, pcm_usagemodel_ClosedWorkload_m_ThinkTimeInClosedWorkloadNeedsToBeSpecified}

# pcm_usagemodel_OpenWorkload class attributes and methods
pcm_usagemodel_OpenWorkload_m_InterArrivalTimeInOpenWorkloadNeedsToBeSpecified: Method = Method(name="InterArrivalTimeInOpenWorkloadNeedsToBeSpecified", parameters={Parameter(name='pcm_context', type=StringType), Parameter(name='pcm_diagnostics', type=StringType)}, type=BooleanType)
pcm_usagemodel_OpenWorkload.methods={pcm_usagemodel_OpenWorkload_m_InterArrivalTimeInOpenWorkloadNeedsToBeSpecified}

# pcm_usagemodel_Loop class attributes and methods

# pcm_usagemodel_EntryLevelSystemCall class attributes and methods

# BranchTransition class attributes and methods

# pcm_usagemodel_BranchTransition class attributes and methods
pcm_usagemodel_BranchTransition_branchProbability: Property = Property(name="branchProbability", type=FloatType)
pcm_usagemodel_BranchTransition.attributes={pcm_usagemodel_BranchTransition_branchProbability}

# pcm_usagemodel_Delay class attributes and methods

# pcm_usagemodel_Branch class attributes and methods
pcm_usagemodel_Branch_m_AllBranchProbabilitiesMustSumUpTo1: Method = Method(name="AllBranchProbabilitiesMustSumUpTo1", parameters={Parameter(name='pcm_context', type=StringType), Parameter(name='pcm_diagnostics', type=StringType)}, type=BooleanType)
pcm_usagemodel_Branch.methods={pcm_usagemodel_Branch_m_AllBranchProbabilitiesMustSumUpTo1}

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
innerProvidedRole_ProvidedDelegationConnector2: BinaryAssociation = BinaryAssociation(
    name="innerProvidedRole_ProvidedDelegationConnector2",
    ends={
        Property(name="ProvidedRole3", type=pcm_composition_ProvidedDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_composition_ProvidedDelegationConnector", type=ProvidedRole, multiplicity=Multiplicity(1, 1))
    }
)
outerProvidedRole_ProvidedDelegationConnector4: BinaryAssociation = BinaryAssociation(
    name="outerProvidedRole_ProvidedDelegationConnector4",
    ends={
        Property(name="ProvidedRole6", type=pcm_composition_ProvidedDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_composition_ProvidedDelegationConnector5", type=ProvidedRole, multiplicity=Multiplicity(1, 1))
    }
)
childComponentContext_ProvidedDelegationConnector7: BinaryAssociation = BinaryAssociation(
    name="childComponentContext_ProvidedDelegationConnector7",
    ends={
        Property(name="composition_AssemblyContext", type=pcm_composition_ProvidedDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_composition_ProvidedDelegationConnector8", type=composition_AssemblyContext, multiplicity=Multiplicity(1, 1))
    }
)
parentStructure_ProvidedDelegationConnector9: BinaryAssociation = BinaryAssociation(
    name="parentStructure_ProvidedDelegationConnector9",
    ends={
        Property(name="ComposedStructure", type=pcm_composition_ProvidedDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="providedDelegationConnectors_ComposedStructure", type=composition_ComposedStructure, multiplicity=Multiplicity(1, 1))
    }
)
encapsulatedComponent_ChildComponentContext10: BinaryAssociation = BinaryAssociation(
    name="encapsulatedComponent_ChildComponentContext10",
    ends={
        Property(name="ProvidesComponentType", type=pcm_composition_AssemblyContext, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_composition_AssemblyContext", type=ProvidesComponentType, multiplicity=Multiplicity(1, 1))
    }
)
parentStructure_AssemblyContext11: BinaryAssociation = BinaryAssociation(
    name="parentStructure_AssemblyContext11",
    ends={
        Property(name="ComposedStructure12", type=pcm_composition_AssemblyContext, multiplicity=Multiplicity(1, 1)),
        Property(name="childComponentContexts_ComposedStructure", type=composition_ComposedStructure, multiplicity=Multiplicity(1, 1))
    }
)
configParameterUsages_AssemblyContext13: BinaryAssociation = BinaryAssociation(
    name="configParameterUsages_AssemblyContext13",
    ends={
        Property(name="VariableUsage", type=pcm_composition_AssemblyContext, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_composition_AssemblyContext14", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
innerRequiredRole_RequiredDelegationConnector15: BinaryAssociation = BinaryAssociation(
    name="innerRequiredRole_RequiredDelegationConnector15",
    ends={
        Property(name="RequiredRole16", type=pcm_composition_RequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_composition_RequiredDelegationConnector", type=RequiredRole, multiplicity=Multiplicity(1, 1))
    }
)
outerRequiredRole_RequiredDelegationConnector17: BinaryAssociation = BinaryAssociation(
    name="outerRequiredRole_RequiredDelegationConnector17",
    ends={
        Property(name="RequiredRole19", type=pcm_composition_RequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_composition_RequiredDelegationConnector18", type=RequiredRole, multiplicity=Multiplicity(1, 1))
    }
)
childComponentContext_RequiredDelegationConnector20: BinaryAssociation = BinaryAssociation(
    name="childComponentContext_RequiredDelegationConnector20",
    ends={
        Property(name="composition_AssemblyContext22", type=pcm_composition_RequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_composition_RequiredDelegationConnector21", type=composition_AssemblyContext, multiplicity=Multiplicity(1, 1))
    }
)
parentStructure_RequiredDelegationConnector23: BinaryAssociation = BinaryAssociation(
    name="parentStructure_RequiredDelegationConnector23",
    ends={
        Property(name="ComposedStructure24", type=pcm_composition_RequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="requiredDelegationConnectors_ComposedStructure", type=composition_ComposedStructure, multiplicity=Multiplicity(1, 1))
    }
)
requiringChildComponentContext_CompositeAssemblyConnector25: BinaryAssociation = BinaryAssociation(
    name="requiringChildComponentContext_CompositeAssemblyConnector25",
    ends={
        Property(name="composition_AssemblyContext26", type=pcm_composition_AssemblyConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_composition_AssemblyConnector", type=composition_AssemblyContext, multiplicity=Multiplicity(1, 1))
    }
)
providingChildComponentContext_CompositeAssemblyConnector27: BinaryAssociation = BinaryAssociation(
    name="providingChildComponentContext_CompositeAssemblyConnector27",
    ends={
        Property(name="composition_AssemblyContext29", type=pcm_composition_AssemblyConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_composition_AssemblyConnector28", type=composition_AssemblyContext, multiplicity=Multiplicity(1, 1))
    }
)
providedRole_CompositeAssemblyConnector30: BinaryAssociation = BinaryAssociation(
    name="providedRole_CompositeAssemblyConnector30",
    ends={
        Property(name="ProvidedRole32", type=pcm_composition_AssemblyConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_composition_AssemblyConnector31", type=ProvidedRole, multiplicity=Multiplicity(1, 1))
    }
)
requiredRole_CompositeAssemblyConnector33: BinaryAssociation = BinaryAssociation(
    name="requiredRole_CompositeAssemblyConnector33",
    ends={
        Property(name="RequiredRole35", type=pcm_composition_AssemblyConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_composition_AssemblyConnector34", type=RequiredRole, multiplicity=Multiplicity(1, 1))
    }
)
parentStructure_AssemblyConnector36: BinaryAssociation = BinaryAssociation(
    name="parentStructure_AssemblyConnector36",
    ends={
        Property(name="ComposedStructure37", type=pcm_composition_AssemblyConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="compositeAssemblyConnectors_ComposedStructure", type=composition_ComposedStructure, multiplicity=Multiplicity(1, 1))
    }
)
childComponentContexts_ComposedStructure38: BinaryAssociation = BinaryAssociation(
    name="childComponentContexts_ComposedStructure38",
    ends={
        Property(name="AssemblyContext", type=pcm_composition_ComposedStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="parentStructure_AssemblyContext", type=composition_AssemblyContext, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
providedDelegationConnectors_ComposedStructure39: BinaryAssociation = BinaryAssociation(
    name="providedDelegationConnectors_ComposedStructure39",
    ends={
        Property(name="ProvidedDelegationConnector", type=pcm_composition_ComposedStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="parentStructure_ProvidedDelegationConnector", type=composition_ProvidedDelegationConnector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredDelegationConnectors_ComposedStructure40: BinaryAssociation = BinaryAssociation(
    name="requiredDelegationConnectors_ComposedStructure40",
    ends={
        Property(name="RequiredDelegationConnector", type=pcm_composition_ComposedStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="parentStructure_RequiredDelegationConnector", type=composition_RequiredDelegationConnector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
compositeAssemblyConnectors_ComposedStructure41: BinaryAssociation = BinaryAssociation(
    name="compositeAssemblyConnectors_ComposedStructure41",
    ends={
        Property(name="AssemblyConnector", type=pcm_composition_ComposedStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="parentStructure_AssemblyConnector", type=composition_AssemblyConnector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
capacity_PassiveResource42: BinaryAssociation = BinaryAssociation(
    name="capacity_PassiveResource42",
    ends={
        Property(name="PCMRandomVariable", type=pcm_repository_PassiveResource, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_repository_PassiveResource", type=PCMRandomVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters__Signature43: BinaryAssociation = BinaryAssociation(
    name="parameters__Signature43",
    ends={
        Property(name="Parameter", type=pcm_repository_Signature, multiplicity=Multiplicity(1, 1)),
        Property(name="signature_Parameter", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
interface_Signature44: BinaryAssociation = BinaryAssociation(
    name="interface_Signature44",
    ends={
        Property(name="Interface", type=pcm_repository_Signature, multiplicity=Multiplicity(1, 1)),
        Property(name="signatures__Interface", type=Interface, multiplicity=Multiplicity(1, 1))
    }
)
returntype__Signature45: BinaryAssociation = BinaryAssociation(
    name="returntype__Signature45",
    ends={
        Property(name="DataType", type=pcm_repository_Signature, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_repository_Signature", type=DataType, multiplicity=Multiplicity(0, 1))
    }
)
exceptions__Signature46: BinaryAssociation = BinaryAssociation(
    name="exceptions__Signature46",
    ends={
        Property(name="ExceptionType", type=pcm_repository_Signature, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_repository_Signature47", type=ExceptionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
datatype__Parameter48: BinaryAssociation = BinaryAssociation(
    name="datatype__Parameter48",
    ends={
        Property(name="DataType49", type=pcm_repository_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_repository_Parameter", type=DataType, multiplicity=Multiplicity(1, 1))
    }
)
signature_Parameter50: BinaryAssociation = BinaryAssociation(
    name="signature_Parameter50",
    ends={
        Property(name="Signature", type=pcm_repository_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameters__Signature", type=Signature, multiplicity=Multiplicity(1, 1))
    }
)
repository_DataType51: BinaryAssociation = BinaryAssociation(
    name="repository_DataType51",
    ends={
        Property(name="Repository", type=pcm_repository_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="datatypes_Repository", type=Repository, multiplicity=Multiplicity(1, 1))
    }
)
components__Repository52: BinaryAssociation = BinaryAssociation(
    name="components__Repository52",
    ends={
        Property(name="ProvidesComponentType53", type=pcm_repository_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="repository_ProvidesComponentType", type=ProvidesComponentType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
interfaces__Repository54: BinaryAssociation = BinaryAssociation(
    name="interfaces__Repository54",
    ends={
        Property(name="Interface55", type=pcm_repository_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="repository_Interface", type=Interface, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
datatypes_Repository56: BinaryAssociation = BinaryAssociation(
    name="datatypes_Repository56",
    ends={
        Property(name="DataType57", type=pcm_repository_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="repository_DataType", type=DataType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
repository_ProvidesComponentType58: BinaryAssociation = BinaryAssociation(
    name="repository_ProvidesComponentType58",
    ends={
        Property(name="Repository59", type=pcm_repository_ProvidesComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="components__Repository", type=Repository, multiplicity=Multiplicity(1, 1))
    }
)
requiredInterface__RequiredRole60: BinaryAssociation = BinaryAssociation(
    name="requiredInterface__RequiredRole60",
    ends={
        Property(name="Interface61", type=pcm_repository_RequiredRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_repository_RequiredRole", type=Interface, multiplicity=Multiplicity(1, 1))
    }
)
requiringEntity_RequiredRole62: BinaryAssociation = BinaryAssociation(
    name="requiringEntity_RequiredRole62",
    ends={
        Property(name="InterfaceRequiringEntity", type=pcm_repository_RequiredRole, multiplicity=Multiplicity(1, 1)),
        Property(name="requiredRoles_InterfaceRequiringEntity", type=entity_InterfaceRequiringEntity, multiplicity=Multiplicity(1, 1))
    }
)
parentInterface__Interface63: BinaryAssociation = BinaryAssociation(
    name="parentInterface__Interface63",
    ends={
        Property(name="Interface64", type=pcm_repository_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_repository_Interface", type=Interface, multiplicity=Multiplicity(0, 9999))
    }
)
anchestorInterfaces_Interface65: BinaryAssociation = BinaryAssociation(
    name="anchestorInterfaces_Interface65",
    ends={
        Property(name="Interface67", type=pcm_repository_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_repository_Interface66", type=Interface, multiplicity=Multiplicity(0, 9999))
    }
)
protocols__Interface68: BinaryAssociation = BinaryAssociation(
    name="protocols__Interface68",
    ends={
        Property(name="Protocol", type=pcm_repository_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_repository_Interface69", type=Protocol, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
signatures__Interface70: BinaryAssociation = BinaryAssociation(
    name="signatures__Interface70",
    ends={
        Property(name="Signature71", type=pcm_repository_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="interface_Signature", type=Signature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
repository_Interface72: BinaryAssociation = BinaryAssociation(
    name="repository_Interface72",
    ends={
        Property(name="Repository73", type=pcm_repository_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="interfaces__Repository", type=Repository, multiplicity=Multiplicity(1, 1))
    }
)
implementationComponentType80: BinaryAssociation = BinaryAssociation(
    name="implementationComponentType80",
    ends={
        Property(name="ImplementationComponentType", type=pcm_repository_CompositeComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_repository_CompositeComponent", type=ImplementationComponentType, multiplicity=Multiplicity(0, 1))
    }
)
parentCompleteComponentTypes74: BinaryAssociation = BinaryAssociation(
    name="parentCompleteComponentTypes74",
    ends={
        Property(name="CompleteComponentType", type=pcm_repository_ImplementationComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_repository_ImplementationComponentType", type=CompleteComponentType, multiplicity=Multiplicity(0, 9999))
    }
)
componentParameterUsage_ImplementationComponentType75: BinaryAssociation = BinaryAssociation(
    name="componentParameterUsage_ImplementationComponentType75",
    ends={
        Property(name="VariableUsage77", type=pcm_repository_ImplementationComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_repository_ImplementationComponentType76", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentProvidesComponentTypes78: BinaryAssociation = BinaryAssociation(
    name="parentProvidesComponentTypes78",
    ends={
        Property(name="ProvidesComponentType79", type=pcm_repository_CompleteComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_repository_CompleteComponentType", type=ProvidesComponentType, multiplicity=Multiplicity(0, 9999))
    }
)
implementationComponentType81: BinaryAssociation = BinaryAssociation(
    name="implementationComponentType81",
    ends={
        Property(name="ImplementationComponentType82", type=pcm_repository_BasicComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_repository_BasicComponent", type=ImplementationComponentType, multiplicity=Multiplicity(0, 1))
    }
)
serviceEffectSpecifications__BasicComponent83: BinaryAssociation = BinaryAssociation(
    name="serviceEffectSpecifications__BasicComponent83",
    ends={
        Property(name="ServiceEffectSpecification", type=pcm_repository_BasicComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_repository_BasicComponent84", type=ServiceEffectSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
passiveResource_BasicComponent85: BinaryAssociation = BinaryAssociation(
    name="passiveResource_BasicComponent85",
    ends={
        Property(name="PassiveResource", type=pcm_repository_BasicComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_repository_BasicComponent86", type=PassiveResource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
innerType_CollectionDataType87: BinaryAssociation = BinaryAssociation(
    name="innerType_CollectionDataType87",
    ends={
        Property(name="DataType88", type=pcm_repository_CollectionDataType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_repository_CollectionDataType", type=DataType, multiplicity=Multiplicity(1, 1))
    }
)
parentType_CompositeDataType89: BinaryAssociation = BinaryAssociation(
    name="parentType_CompositeDataType89",
    ends={
        Property(name="CompositeDataType", type=pcm_repository_CompositeDataType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_repository_CompositeDataType", type=CompositeDataType, multiplicity=Multiplicity(0, 9999))
    }
)
innerDeclaration_CompositeDataType90: BinaryAssociation = BinaryAssociation(
    name="innerDeclaration_CompositeDataType90",
    ends={
        Property(name="InnerDeclaration", type=pcm_repository_CompositeDataType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_repository_CompositeDataType91", type=InnerDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
datatype_InnerDeclaration92: BinaryAssociation = BinaryAssociation(
    name="datatype_InnerDeclaration92",
    ends={
        Property(name="DataType93", type=pcm_repository_InnerDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_repository_InnerDeclaration", type=DataType, multiplicity=Multiplicity(1, 1))
    }
)
providedInterface__ProvidedRole94: BinaryAssociation = BinaryAssociation(
    name="providedInterface__ProvidedRole94",
    ends={
        Property(name="Interface95", type=pcm_repository_ProvidedRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_repository_ProvidedRole", type=Interface, multiplicity=Multiplicity(1, 1))
    }
)
providingEntity_ProvidedRole96: BinaryAssociation = BinaryAssociation(
    name="providingEntity_ProvidedRole96",
    ends={
        Property(name="InterfaceProvidingEntity", type=pcm_repository_ProvidedRole, multiplicity=Multiplicity(1, 1)),
        Property(name="providedRoles_InterfaceProvidingEntity", type=entity_InterfaceProvidingEntity, multiplicity=Multiplicity(1, 1))
    }
)
signature__ServiceCall97: BinaryAssociation = BinaryAssociation(
    name="signature__ServiceCall97",
    ends={
        Property(name="Signature98", type=pcm_protocol_ServiceCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_protocol_ServiceCall", type=Signature, multiplicity=Multiplicity(1, 1))
    }
)
specification_VariableCharacterisation99: BinaryAssociation = BinaryAssociation(
    name="specification_VariableCharacterisation99",
    ends={
        Property(name="PCMRandomVariable100", type=pcm_parameter_VariableCharacterisation, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_parameter_VariableCharacterisation", type=PCMRandomVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variableCharacterisation_VariableUsage101: BinaryAssociation = BinaryAssociation(
    name="variableCharacterisation_VariableUsage101",
    ends={
        Property(name="VariableCharacterisation", type=pcm_parameter_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_parameter_VariableUsage", type=VariableCharacterisation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
namedReference_VariableUsage102: BinaryAssociation = BinaryAssociation(
    name="namedReference_VariableUsage102",
    ends={
        Property(name="parameter_pcm_AbstractNamedReference", type=pcm_parameter_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_parameter_VariableUsage103", type=parameter_pcm_AbstractNamedReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
resourceDemand_Action104: BinaryAssociation = BinaryAssociation(
    name="resourceDemand_Action104",
    ends={
        Property(name="ParametricResourceDemand", type=pcm_seff_AbstractResourceDemandingAction, multiplicity=Multiplicity(1, 1)),
        Property(name="action_ParametricResourceDemand", type=ParametricResourceDemand, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
predecessor_AbstractAction105: BinaryAssociation = BinaryAssociation(
    name="predecessor_AbstractAction105",
    ends={
        Property(name="AbstractAction", type=pcm_seff_AbstractAction, multiplicity=Multiplicity(1, 1)),
        Property(name="successor_AbstractAction", type=AbstractAction, multiplicity=Multiplicity(0, 1))
    }
)
successor_AbstractAction106: BinaryAssociation = BinaryAssociation(
    name="successor_AbstractAction106",
    ends={
        Property(name="AbstractAction107", type=pcm_seff_AbstractAction, multiplicity=Multiplicity(1, 1)),
        Property(name="predecessor_AbstractAction", type=AbstractAction, multiplicity=Multiplicity(0, 1))
    }
)
requiredResource_ParametricResourceDemand108: BinaryAssociation = BinaryAssociation(
    name="requiredResource_ParametricResourceDemand108",
    ends={
        Property(name="ProcessingResourceType", type=pcm_seff_ParametricResourceDemand, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_seff_ParametricResourceDemand", type=ProcessingResourceType, multiplicity=Multiplicity(1, 1))
    }
)
specification_ParametericResourceDemand109: BinaryAssociation = BinaryAssociation(
    name="specification_ParametericResourceDemand109",
    ends={
        Property(name="PCMRandomVariable111", type=pcm_seff_ParametricResourceDemand, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_seff_ParametricResourceDemand110", type=PCMRandomVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
action_ParametricResourceDemand112: BinaryAssociation = BinaryAssociation(
    name="action_ParametricResourceDemand112",
    ends={
        Property(name="AbstractResourceDemandingAction", type=pcm_seff_ParametricResourceDemand, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceDemand_Action", type=AbstractResourceDemandingAction, multiplicity=Multiplicity(1, 1))
    }
)
steps_Behaviour113: BinaryAssociation = BinaryAssociation(
    name="steps_Behaviour113",
    ends={
        Property(name="AbstractAction114", type=pcm_seff_ResourceDemandingBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_seff_ResourceDemandingBehaviour", type=AbstractAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
passiveResource_ReleaseAction115: BinaryAssociation = BinaryAssociation(
    name="passiveResource_ReleaseAction115",
    ends={
        Property(name="PassiveResource116", type=pcm_seff_ReleaseAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_seff_ReleaseAction", type=PassiveResource, multiplicity=Multiplicity(1, 1))
    }
)
iterationCount_LoopAction117: BinaryAssociation = BinaryAssociation(
    name="iterationCount_LoopAction117",
    ends={
        Property(name="PCMRandomVariable118", type=pcm_seff_LoopAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_seff_LoopAction", type=PCMRandomVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
bodyBehaviour_Loop119: BinaryAssociation = BinaryAssociation(
    name="bodyBehaviour_Loop119",
    ends={
        Property(name="ResourceDemandingBehaviour", type=pcm_seff_AbstractLoopAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_seff_AbstractLoopAction", type=ResourceDemandingBehaviour, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
asynchronousForkedBehaviours_ForkAction120: BinaryAssociation = BinaryAssociation(
    name="asynchronousForkedBehaviours_ForkAction120",
    ends={
        Property(name="ForkedBehaviour", type=pcm_seff_ForkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_seff_ForkAction", type=ForkedBehaviour, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
synchronisingBehaviours_ForkAction121: BinaryAssociation = BinaryAssociation(
    name="synchronisingBehaviours_ForkAction121",
    ends={
        Property(name="SynchronisationPoint", type=pcm_seff_ForkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_seff_ForkAction122", type=SynchronisationPoint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
synchronousForkedBehaviours_SynchronisationPoint123: BinaryAssociation = BinaryAssociation(
    name="synchronousForkedBehaviours_SynchronisationPoint123",
    ends={
        Property(name="ForkedBehaviour124", type=pcm_seff_SynchronisationPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_seff_SynchronisationPoint", type=ForkedBehaviour, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
outputParameterUsage_SynchronisationPoint125: BinaryAssociation = BinaryAssociation(
    name="outputParameterUsage_SynchronisationPoint125",
    ends={
        Property(name="VariableUsage127", type=pcm_seff_SynchronisationPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_seff_SynchronisationPoint126", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
calledService_ExternalService128: BinaryAssociation = BinaryAssociation(
    name="calledService_ExternalService128",
    ends={
        Property(name="Signature129", type=pcm_seff_ExternalCallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_seff_ExternalCallAction", type=Signature, multiplicity=Multiplicity(1, 1))
    }
)
inputParameterUsages_ExternalCallAction130: BinaryAssociation = BinaryAssociation(
    name="inputParameterUsages_ExternalCallAction130",
    ends={
        Property(name="VariableUsage132", type=pcm_seff_ExternalCallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_seff_ExternalCallAction131", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputVariableUsages_ExternalCallAction133: BinaryAssociation = BinaryAssociation(
    name="outputVariableUsages_ExternalCallAction133",
    ends={
        Property(name="VariableUsage135", type=pcm_seff_ExternalCallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_seff_ExternalCallAction134", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
role_ExternalService136: BinaryAssociation = BinaryAssociation(
    name="role_ExternalService136",
    ends={
        Property(name="Role", type=pcm_seff_ExternalCallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_seff_ExternalCallAction137", type=Role, multiplicity=Multiplicity(1, 1))
    }
)
branchBehaviour_BranchTransition138: BinaryAssociation = BinaryAssociation(
    name="branchBehaviour_BranchTransition138",
    ends={
        Property(name="ResourceDemandingBehaviour139", type=pcm_seff_AbstractBranchTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_seff_AbstractBranchTransition", type=ResourceDemandingBehaviour, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
branches_Branch140: BinaryAssociation = BinaryAssociation(
    name="branches_Branch140",
    ends={
        Property(name="AbstractBranchTransition", type=pcm_seff_BranchAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_seff_BranchAction", type=AbstractBranchTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
passiveresource_AcquireAction141: BinaryAssociation = BinaryAssociation(
    name="passiveresource_AcquireAction141",
    ends={
        Property(name="PassiveResource142", type=pcm_seff_AcquireAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_seff_AcquireAction", type=PassiveResource, multiplicity=Multiplicity(1, 1))
    }
)
parameter_CollectionIteratorAction143: BinaryAssociation = BinaryAssociation(
    name="parameter_CollectionIteratorAction143",
    ends={
        Property(name="Parameter144", type=pcm_seff_CollectionIteratorAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_seff_CollectionIteratorAction", type=Parameter_, multiplicity=Multiplicity(1, 1))
    }
)
branchCondition_GuardedBranchTransition145: BinaryAssociation = BinaryAssociation(
    name="branchCondition_GuardedBranchTransition145",
    ends={
        Property(name="PCMRandomVariable146", type=pcm_seff_GuardedBranchTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_seff_GuardedBranchTransition", type=PCMRandomVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
localVariableUsages_SetVariableAction147: BinaryAssociation = BinaryAssociation(
    name="localVariableUsages_SetVariableAction147",
    ends={
        Property(name="VariableUsage148", type=pcm_seff_SetVariableAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_seff_SetVariableAction", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
describedService__SEFF149: BinaryAssociation = BinaryAssociation(
    name="describedService__SEFF149",
    ends={
        Property(name="Signature150", type=pcm_seff_ServiceEffectSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_seff_ServiceEffectSpecification", type=Signature, multiplicity=Multiplicity(1, 1))
    }
)
availableResourceTypes_ResourceRepository151: BinaryAssociation = BinaryAssociation(
    name="availableResourceTypes_ResourceRepository151",
    ends={
        Property(name="ResourceType", type=pcm_resourcetype_ResourceRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_resourcetype_ResourceRepository", type=ResourceType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceContainer_AllocationContext152: BinaryAssociation = BinaryAssociation(
    name="resourceContainer_AllocationContext152",
    ends={
        Property(name="ResourceContainer", type=pcm_allocation_AllocationContext, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_allocation_AllocationContext", type=ResourceContainer, multiplicity=Multiplicity(1, 1))
    }
)
assemblyContext_AllocationContext153: BinaryAssociation = BinaryAssociation(
    name="assemblyContext_AllocationContext153",
    ends={
        Property(name="composition_AssemblyContext155", type=pcm_allocation_AllocationContext, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_allocation_AllocationContext154", type=composition_AssemblyContext, multiplicity=Multiplicity(1, 1))
    }
)
allocationContexts_Allocation156: BinaryAssociation = BinaryAssociation(
    name="allocationContexts_Allocation156",
    ends={
        Property(name="AllocationContext", type=pcm_allocation_Allocation, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_allocation_Allocation", type=AllocationContext, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
targetResourceEnvironment_Allocation157: BinaryAssociation = BinaryAssociation(
    name="targetResourceEnvironment_Allocation157",
    ends={
        Property(name="ResourceEnvironment", type=pcm_allocation_Allocation, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_allocation_Allocation158", type=ResourceEnvironment, multiplicity=Multiplicity(0, 1))
    }
)
system_Allocation159: BinaryAssociation = BinaryAssociation(
    name="system_Allocation159",
    ends={
        Property(name="System", type=pcm_allocation_Allocation, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_allocation_Allocation160", type=System, multiplicity=Multiplicity(1, 1))
    }
)
linkingresource161: BinaryAssociation = BinaryAssociation(
    name="linkingresource161",
    ends={
        Property(name="LinkingResource", type=pcm_resourceenvironment_ResourceEnvironment, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_resourceenvironment_ResourceEnvironment", type=LinkingResource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceContainer_ResourceEnvironment162: BinaryAssociation = BinaryAssociation(
    name="resourceContainer_ResourceEnvironment162",
    ends={
        Property(name="ResourceContainer164", type=pcm_resourceenvironment_ResourceEnvironment, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_resourceenvironment_ResourceEnvironment163", type=ResourceContainer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
toResourceContainer_LinkingResource165: BinaryAssociation = BinaryAssociation(
    name="toResourceContainer_LinkingResource165",
    ends={
        Property(name="ResourceContainer166", type=pcm_resourceenvironment_LinkingResource, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_resourceenvironment_LinkingResource", type=ResourceContainer, multiplicity=Multiplicity(0, 9999))
    }
)
fromResourceContainer_LinkingResource167: BinaryAssociation = BinaryAssociation(
    name="fromResourceContainer_LinkingResource167",
    ends={
        Property(name="ResourceContainer169", type=pcm_resourceenvironment_LinkingResource, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_resourceenvironment_LinkingResource168", type=ResourceContainer, multiplicity=Multiplicity(0, 9999))
    }
)
communicationLinkResourceSpecifications_LinkingResource170: BinaryAssociation = BinaryAssociation(
    name="communicationLinkResourceSpecifications_LinkingResource170",
    ends={
        Property(name="CommunicationLinkResourceSpecification", type=pcm_resourceenvironment_LinkingResource, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_resourceenvironment_LinkingResource171", type=CommunicationLinkResourceSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
communicationLinkResourceType_CommunicationLinkResourceSpecification172: BinaryAssociation = BinaryAssociation(
    name="communicationLinkResourceType_CommunicationLinkResourceSpecification172",
    ends={
        Property(name="CommunicationLinkResourceType", type=pcm_resourceenvironment_CommunicationLinkResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_resourceenvironment_CommunicationLinkResourceSpecification", type=CommunicationLinkResourceType, multiplicity=Multiplicity(1, 1))
    }
)
latency_CommunicationLinkResourceSpecification173: BinaryAssociation = BinaryAssociation(
    name="latency_CommunicationLinkResourceSpecification173",
    ends={
        Property(name="PCMRandomVariable175", type=pcm_resourceenvironment_CommunicationLinkResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_resourceenvironment_CommunicationLinkResourceSpecification174", type=PCMRandomVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
throughput_CommunicationLinkResourceSpecification176: BinaryAssociation = BinaryAssociation(
    name="throughput_CommunicationLinkResourceSpecification176",
    ends={
        Property(name="PCMRandomVariable178", type=pcm_resourceenvironment_CommunicationLinkResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_resourceenvironment_CommunicationLinkResourceSpecification177", type=PCMRandomVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
activeResourceType_ActiveResourceSpecification179: BinaryAssociation = BinaryAssociation(
    name="activeResourceType_ActiveResourceSpecification179",
    ends={
        Property(name="ProcessingResourceType180", type=pcm_resourceenvironment_ProcessingResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_resourceenvironment_ProcessingResourceSpecification", type=ProcessingResourceType, multiplicity=Multiplicity(1, 1))
    }
)
processingRate_ProcessingResourceSpecification181: BinaryAssociation = BinaryAssociation(
    name="processingRate_ProcessingResourceSpecification181",
    ends={
        Property(name="PCMRandomVariable183", type=pcm_resourceenvironment_ProcessingResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_resourceenvironment_ProcessingResourceSpecification182", type=PCMRandomVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
activeResourceSpecifications_ResourceContainer184: BinaryAssociation = BinaryAssociation(
    name="activeResourceSpecifications_ResourceContainer184",
    ends={
        Property(name="ProcessingResourceSpecification", type=pcm_resourceenvironment_ResourceContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_resourceenvironment_ResourceContainer", type=ProcessingResourceSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
qosAnnotations_System185: BinaryAssociation = BinaryAssociation(
    name="qosAnnotations_System185",
    ends={
        Property(name="QoSAnnotations", type=pcm_system_System, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_system_System", type=QoSAnnotations, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
signature_SpecifiedTimeConsumption186: BinaryAssociation = BinaryAssociation(
    name="signature_SpecifiedTimeConsumption186",
    ends={
        Property(name="Signature187", type=pcm_qosannotations_SpecifiedExecutionTime, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_qosannotations_SpecifiedExecutionTime", type=Signature, multiplicity=Multiplicity(1, 1))
    }
)
role_SpecifiedExecutionTime188: BinaryAssociation = BinaryAssociation(
    name="role_SpecifiedExecutionTime188",
    ends={
        Property(name="Role190", type=pcm_qosannotations_SpecifiedExecutionTime, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_qosannotations_SpecifiedExecutionTime189", type=Role, multiplicity=Multiplicity(1, 1))
    }
)
specification_SpecifiedExecutionTime191: BinaryAssociation = BinaryAssociation(
    name="specification_SpecifiedExecutionTime191",
    ends={
        Property(name="PCMRandomVariable193", type=pcm_qosannotations_SpecifiedExecutionTime, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_qosannotations_SpecifiedExecutionTime192", type=PCMRandomVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
assemblyContext_ComponentSpecifiedExecutionTime194: BinaryAssociation = BinaryAssociation(
    name="assemblyContext_ComponentSpecifiedExecutionTime194",
    ends={
        Property(name="composition_AssemblyContext195", type=pcm_qosannotations_ComponentSpecifiedExecutionTime, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_qosannotations_ComponentSpecifiedExecutionTime", type=composition_AssemblyContext, multiplicity=Multiplicity(1, 1))
    }
)
signature_SpecifiedOutputParameterAbstraction196: BinaryAssociation = BinaryAssociation(
    name="signature_SpecifiedOutputParameterAbstraction196",
    ends={
        Property(name="Signature197", type=pcm_qosannotations_SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_qosannotations_SpecifiedOutputParameterAbstraction", type=Signature, multiplicity=Multiplicity(1, 1))
    }
)
role_SpecifiedOutputParameterAbstraction198: BinaryAssociation = BinaryAssociation(
    name="role_SpecifiedOutputParameterAbstraction198",
    ends={
        Property(name="Role200", type=pcm_qosannotations_SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_qosannotations_SpecifiedOutputParameterAbstraction199", type=Role, multiplicity=Multiplicity(1, 1))
    }
)
expectedExternalOutputs_SpecifiedOutputParameterAbstraction201: BinaryAssociation = BinaryAssociation(
    name="expectedExternalOutputs_SpecifiedOutputParameterAbstraction201",
    ends={
        Property(name="VariableUsage203", type=pcm_qosannotations_SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_qosannotations_SpecifiedOutputParameterAbstraction202", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specifiedExecutionTimes_QoSAnnotations204: BinaryAssociation = BinaryAssociation(
    name="specifiedExecutionTimes_QoSAnnotations204",
    ends={
        Property(name="SpecifiedExecutionTime", type=pcm_qosannotations_QoSAnnotations, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_qosannotations_QoSAnnotations", type=SpecifiedExecutionTime, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specifiedOutputParameterAbstractions_QoSAnnotations205: BinaryAssociation = BinaryAssociation(
    name="specifiedOutputParameterAbstractions_QoSAnnotations205",
    ends={
        Property(name="SpecifiedOutputParameterAbstraction", type=pcm_qosannotations_QoSAnnotations, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_qosannotations_QoSAnnotations206", type=SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
workload_UsageScenario207: BinaryAssociation = BinaryAssociation(
    name="workload_UsageScenario207",
    ends={
        Property(name="Workload", type=pcm_usagemodel_UsageScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_usagemodel_UsageScenario", type=Workload, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
scenarioBehaviour_UsageScenario208: BinaryAssociation = BinaryAssociation(
    name="scenarioBehaviour_UsageScenario208",
    ends={
        Property(name="ScenarioBehaviour", type=pcm_usagemodel_UsageScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_usagemodel_UsageScenario209", type=ScenarioBehaviour, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
successor211: BinaryAssociation = BinaryAssociation(
    name="successor211",
    ends={
        Property(name="predecessor", type=AbstractUserAction, multiplicity=Multiplicity(0, 1)),
        Property(name="AbstractUserAction212", type=pcm_usagemodel_AbstractUserAction, multiplicity=Multiplicity(1, 1))
    }
)
actions_ScenarioBehaviour210: BinaryAssociation = BinaryAssociation(
    name="actions_ScenarioBehaviour210",
    ends={
        Property(name="AbstractUserAction", type=pcm_usagemodel_ScenarioBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_usagemodel_ScenarioBehaviour", type=AbstractUserAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
predecessor213: BinaryAssociation = BinaryAssociation(
    name="predecessor213",
    ends={
        Property(name="AbstractUserAction214", type=pcm_usagemodel_AbstractUserAction, multiplicity=Multiplicity(1, 1)),
        Property(name="successor", type=AbstractUserAction, multiplicity=Multiplicity(0, 1))
    }
)
usageScenario_UsageModel215: BinaryAssociation = BinaryAssociation(
    name="usageScenario_UsageModel215",
    ends={
        Property(name="UsageScenario", type=pcm_usagemodel_UsageModel, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_usagemodel_UsageModel", type=UsageScenario, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
userData_UsageModel216: BinaryAssociation = BinaryAssociation(
    name="userData_UsageModel216",
    ends={
        Property(name="UserData", type=pcm_usagemodel_UsageModel, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_usagemodel_UsageModel217", type=UserData, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
userDataParameterUsages_UserData218: BinaryAssociation = BinaryAssociation(
    name="userDataParameterUsages_UserData218",
    ends={
        Property(name="VariableUsage219", type=pcm_usagemodel_UserData, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_usagemodel_UserData", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
assemblyContext_userData220: BinaryAssociation = BinaryAssociation(
    name="assemblyContext_userData220",
    ends={
        Property(name="composition_AssemblyContext222", type=pcm_usagemodel_UserData, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_usagemodel_UserData221", type=composition_AssemblyContext, multiplicity=Multiplicity(1, 1))
    }
)
inputParameterUsages_EntryLevelSystemCall230: BinaryAssociation = BinaryAssociation(
    name="inputParameterUsages_EntryLevelSystemCall230",
    ends={
        Property(name="VariableUsage231", type=pcm_usagemodel_EntryLevelSystemCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_usagemodel_EntryLevelSystemCall", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
providedRole_EntryLevelSystemCall232: BinaryAssociation = BinaryAssociation(
    name="providedRole_EntryLevelSystemCall232",
    ends={
        Property(name="ProvidedRole234", type=pcm_usagemodel_EntryLevelSystemCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_usagemodel_EntryLevelSystemCall233", type=ProvidedRole, multiplicity=Multiplicity(1, 1))
    }
)
signature_EntryLevelSystemCall235: BinaryAssociation = BinaryAssociation(
    name="signature_EntryLevelSystemCall235",
    ends={
        Property(name="Signature237", type=pcm_usagemodel_EntryLevelSystemCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_usagemodel_EntryLevelSystemCall236", type=Signature, multiplicity=Multiplicity(1, 1))
    }
)
outputParameterUsages_EntryLevelSystemCall238: BinaryAssociation = BinaryAssociation(
    name="outputParameterUsages_EntryLevelSystemCall238",
    ends={
        Property(name="VariableUsage240", type=pcm_usagemodel_EntryLevelSystemCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_usagemodel_EntryLevelSystemCall239", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
interArrivalTime_OpenWorkload223: BinaryAssociation = BinaryAssociation(
    name="interArrivalTime_OpenWorkload223",
    ends={
        Property(name="PCMRandomVariable224", type=pcm_usagemodel_OpenWorkload, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_usagemodel_OpenWorkload", type=PCMRandomVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
bodyBehaviour_Loop225: BinaryAssociation = BinaryAssociation(
    name="bodyBehaviour_Loop225",
    ends={
        Property(name="ScenarioBehaviour226", type=pcm_usagemodel_Loop, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_usagemodel_Loop", type=ScenarioBehaviour, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
loopIteration_Loop227: BinaryAssociation = BinaryAssociation(
    name="loopIteration_Loop227",
    ends={
        Property(name="PCMRandomVariable229", type=pcm_usagemodel_Loop, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_usagemodel_Loop228", type=PCMRandomVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
branchTransitions_Branch243: BinaryAssociation = BinaryAssociation(
    name="branchTransitions_Branch243",
    ends={
        Property(name="BranchTransition", type=pcm_usagemodel_Branch, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_usagemodel_Branch", type=BranchTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
branchedBehaviour_BranchTransition244: BinaryAssociation = BinaryAssociation(
    name="branchedBehaviour_BranchTransition244",
    ends={
        Property(name="ScenarioBehaviour245", type=pcm_usagemodel_BranchTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_usagemodel_BranchTransition", type=ScenarioBehaviour, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
timeSpecification_Delay246: BinaryAssociation = BinaryAssociation(
    name="timeSpecification_Delay246",
    ends={
        Property(name="PCMRandomVariable247", type=pcm_usagemodel_Delay, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_usagemodel_Delay", type=PCMRandomVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thinkTime_ClosedWorkload241: BinaryAssociation = BinaryAssociation(
    name="thinkTime_ClosedWorkload241",
    ends={
        Property(name="PCMRandomVariable242", type=pcm_usagemodel_ClosedWorkload, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_usagemodel_ClosedWorkload", type=PCMRandomVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_pcm_core_PCMRandomVariable_RandomVariable = Generalization(general=RandomVariable, specific=pcm_core_PCMRandomVariable)
gen_pcm_entity_Entity_Identifier = Generalization(general=Identifier, specific=pcm_entity_Entity)
gen_pcm_entity_Entity_entity_NamedElement = Generalization(general=entity_NamedElement, specific=pcm_entity_Entity)
gen_pcm_entity_InterfaceProvidingEntity_Entity = Generalization(general=Entity, specific=pcm_entity_InterfaceProvidingEntity)
gen_pcm_entity_InterfaceProvidingRequiringEntity_entity_InterfaceProvidingEntity = Generalization(general=entity_InterfaceProvidingEntity, specific=pcm_entity_InterfaceProvidingRequiringEntity)
gen_pcm_entity_InterfaceProvidingRequiringEntity_entity_InterfaceRequiringEntity = Generalization(general=entity_InterfaceRequiringEntity, specific=pcm_entity_InterfaceProvidingRequiringEntity)
gen_pcm_entity_InterfaceRequiringEntity_Entity = Generalization(general=Entity, specific=pcm_entity_InterfaceRequiringEntity)
gen_pcm_entity_ComposedProvidingRequiringEntity_composition_ComposedStructure = Generalization(general=composition_ComposedStructure, specific=pcm_entity_ComposedProvidingRequiringEntity)
gen_pcm_entity_ComposedProvidingRequiringEntity_entity_InterfaceProvidingRequiringEntity = Generalization(general=entity_InterfaceProvidingRequiringEntity, specific=pcm_entity_ComposedProvidingRequiringEntity)
gen_pcm_connectors_Connector_Entity = Generalization(general=Entity, specific=pcm_connectors_Connector)
gen_pcm_composition_ProvidedDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_composition_ProvidedDelegationConnector)
gen_pcm_composition_AssemblyContext_Entity = Generalization(general=Entity, specific=pcm_composition_AssemblyContext)
gen_pcm_composition_RequiredDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_composition_RequiredDelegationConnector)
gen_pcm_composition_ComposedStructure_Entity = Generalization(general=Entity, specific=pcm_composition_ComposedStructure)
gen_pcm_composition_AssemblyConnector_connectors_Connector = Generalization(general=connectors_Connector, specific=pcm_composition_AssemblyConnector)
gen_pcm_composition_AssemblyConnector_entity_Entity = Generalization(general=entity_Entity, specific=pcm_composition_AssemblyConnector)
gen_pcm_repository_PassiveResource_Entity = Generalization(general=Entity, specific=pcm_repository_PassiveResource)
gen_pcm_repository_Repository_Entity = Generalization(general=Entity, specific=pcm_repository_Repository)
gen_pcm_repository_ProvidesComponentType_entity_Entity = Generalization(general=entity_Entity, specific=pcm_repository_ProvidesComponentType)
gen_pcm_repository_ProvidesComponentType_entity_InterfaceProvidingRequiringEntity = Generalization(general=entity_InterfaceProvidingRequiringEntity, specific=pcm_repository_ProvidesComponentType)
gen_pcm_repository_RequiredRole_Role = Generalization(general=Role, specific=pcm_repository_RequiredRole)
gen_pcm_repository_Role_Entity = Generalization(general=Entity, specific=pcm_repository_Role)
gen_pcm_repository_Interface_Entity = Generalization(general=Entity, specific=pcm_repository_Interface)
gen_pcm_repository_ImplementationComponentType_CompleteComponentType = Generalization(general=CompleteComponentType, specific=pcm_repository_ImplementationComponentType)
gen_pcm_repository_CompleteComponentType_ProvidesComponentType = Generalization(general=ProvidesComponentType, specific=pcm_repository_CompleteComponentType)
gen_pcm_repository_DelegationConnector_Connector = Generalization(general=Connector, specific=pcm_repository_DelegationConnector)
gen_pcm_repository_CompositeComponent_repository_ImplementationComponentType = Generalization(general=repository_ImplementationComponentType, specific=pcm_repository_CompositeComponent)
gen_pcm_repository_CompositeComponent_entity_ComposedProvidingRequiringEntity = Generalization(general=entity_ComposedProvidingRequiringEntity, specific=pcm_repository_CompositeComponent)
gen_pcm_repository_BasicComponent_ImplementationComponentType = Generalization(general=ImplementationComponentType, specific=pcm_repository_BasicComponent)
gen_pcm_repository_PrimitiveDataType_DataType = Generalization(general=DataType, specific=pcm_repository_PrimitiveDataType)
gen_pcm_repository_CollectionDataType_entity_Entity = Generalization(general=entity_Entity, specific=pcm_repository_CollectionDataType)
gen_pcm_repository_CollectionDataType_repository_DataType = Generalization(general=repository_DataType, specific=pcm_repository_CollectionDataType)
gen_pcm_repository_CompositeDataType_entity_Entity = Generalization(general=entity_Entity, specific=pcm_repository_CompositeDataType)
gen_pcm_repository_CompositeDataType_repository_DataType = Generalization(general=repository_DataType, specific=pcm_repository_CompositeDataType)
gen_pcm_repository_InnerDeclaration_NamedElement = Generalization(general=NamedElement, specific=pcm_repository_InnerDeclaration)
gen_pcm_repository_ProvidedRole_Role = Generalization(general=Role, specific=pcm_repository_ProvidedRole)
gen_pcm_parameter_CharacterisedVariable_Variable = Generalization(general=Variable, specific=pcm_parameter_CharacterisedVariable)
gen_pcm_seff_StopAction_AbstractResourceDemandingAction = Generalization(general=AbstractResourceDemandingAction, specific=pcm_seff_StopAction)
gen_pcm_seff_AbstractResourceDemandingAction_AbstractAction = Generalization(general=AbstractAction, specific=pcm_seff_AbstractResourceDemandingAction)
gen_pcm_seff_AbstractAction_Entity = Generalization(general=Entity, specific=pcm_seff_AbstractAction)
gen_pcm_seff_StartAction_AbstractResourceDemandingAction = Generalization(general=AbstractResourceDemandingAction, specific=pcm_seff_StartAction)
gen_pcm_seff_ResourceDemandingSEFF_Identifier = Generalization(general=Identifier, specific=pcm_seff_ResourceDemandingSEFF)
gen_pcm_seff_ResourceDemandingSEFF_seff_ServiceEffectSpecification = Generalization(general=seff_ServiceEffectSpecification, specific=pcm_seff_ResourceDemandingSEFF)
gen_pcm_seff_ResourceDemandingSEFF_seff_ResourceDemandingBehaviour = Generalization(general=seff_ResourceDemandingBehaviour, specific=pcm_seff_ResourceDemandingSEFF)
gen_pcm_seff_ForkedBehaviour_ResourceDemandingBehaviour = Generalization(general=ResourceDemandingBehaviour, specific=pcm_seff_ForkedBehaviour)
gen_pcm_seff_ReleaseAction_AbstractResourceDemandingAction = Generalization(general=AbstractResourceDemandingAction, specific=pcm_seff_ReleaseAction)
gen_pcm_seff_LoopAction_AbstractLoopAction = Generalization(general=AbstractLoopAction, specific=pcm_seff_LoopAction)
gen_pcm_seff_AbstractLoopAction_AbstractResourceDemandingAction = Generalization(general=AbstractResourceDemandingAction, specific=pcm_seff_AbstractLoopAction)
gen_pcm_seff_InternalAction_AbstractResourceDemandingAction = Generalization(general=AbstractResourceDemandingAction, specific=pcm_seff_InternalAction)
gen_pcm_seff_ForkAction_AbstractResourceDemandingAction = Generalization(general=AbstractResourceDemandingAction, specific=pcm_seff_ForkAction)
gen_pcm_seff_ExternalCallAction_AbstractAction = Generalization(general=AbstractAction, specific=pcm_seff_ExternalCallAction)
gen_pcm_seff_ProbabilisticBranchTransition_AbstractBranchTransition = Generalization(general=AbstractBranchTransition, specific=pcm_seff_ProbabilisticBranchTransition)
gen_pcm_seff_AbstractBranchTransition_Identifier = Generalization(general=Identifier, specific=pcm_seff_AbstractBranchTransition)
gen_pcm_seff_BranchAction_AbstractResourceDemandingAction = Generalization(general=AbstractResourceDemandingAction, specific=pcm_seff_BranchAction)
gen_pcm_seff_AcquireAction_AbstractResourceDemandingAction = Generalization(general=AbstractResourceDemandingAction, specific=pcm_seff_AcquireAction)
gen_pcm_allocation_AllocationContext_Entity = Generalization(general=Entity, specific=pcm_allocation_AllocationContext)
gen_pcm_seff_CollectionIteratorAction_AbstractLoopAction = Generalization(general=AbstractLoopAction, specific=pcm_seff_CollectionIteratorAction)
gen_pcm_seff_GuardedBranchTransition_AbstractBranchTransition = Generalization(general=AbstractBranchTransition, specific=pcm_seff_GuardedBranchTransition)
gen_pcm_seff_SetVariableAction_AbstractResourceDemandingAction = Generalization(general=AbstractResourceDemandingAction, specific=pcm_seff_SetVariableAction)
gen_pcm_resourcetype_ResourceType_entity_Entity = Generalization(general=entity_Entity, specific=pcm_resourcetype_ResourceType)
gen_pcm_resourcetype_ResourceType_UnitCarryingElement = Generalization(general=UnitCarryingElement, specific=pcm_resourcetype_ResourceType)
gen_pcm_resourcetype_CommunicationLinkResourceType_ProcessingResourceType = Generalization(general=ProcessingResourceType, specific=pcm_resourcetype_CommunicationLinkResourceType)
gen_pcm_resourcetype_ProcessingResourceType_ResourceType = Generalization(general=ResourceType, specific=pcm_resourcetype_ProcessingResourceType)
gen_pcm_resourceenvironment_LinkingResource_Entity = Generalization(general=Entity, specific=pcm_resourceenvironment_LinkingResource)
gen_pcm_allocation_Allocation_Entity = Generalization(general=Entity, specific=pcm_allocation_Allocation)
gen_pcm_resourceenvironment_ResourceContainer_Entity = Generalization(general=Entity, specific=pcm_resourceenvironment_ResourceContainer)
gen_pcm_system_System_entity_Entity = Generalization(general=entity_Entity, specific=pcm_system_System)
gen_pcm_system_System_entity_ComposedProvidingRequiringEntity = Generalization(general=entity_ComposedProvidingRequiringEntity, specific=pcm_system_System)
gen_pcm_qosannotations_SystemSpecifiedExecutionTime_SpecifiedExecutionTime = Generalization(general=SpecifiedExecutionTime, specific=pcm_qosannotations_SystemSpecifiedExecutionTime)
gen_pcm_qosannotations_ComponentSpecifiedExecutionTime_SpecifiedExecutionTime = Generalization(general=SpecifiedExecutionTime, specific=pcm_qosannotations_ComponentSpecifiedExecutionTime)
gen_pcm_qosannotations_QoSAnnotations_Entity = Generalization(general=Entity, specific=pcm_qosannotations_QoSAnnotations)
gen_pcm_usagemodel_UsageScenario_Entity = Generalization(general=Entity, specific=pcm_usagemodel_UsageScenario)
gen_pcm_usagemodel_ScenarioBehaviour_Entity = Generalization(general=Entity, specific=pcm_usagemodel_ScenarioBehaviour)
gen_pcm_usagemodel_AbstractUserAction_Entity = Generalization(general=Entity, specific=pcm_usagemodel_AbstractUserAction)
gen_pcm_usagemodel_Stop_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_usagemodel_Stop)
gen_pcm_usagemodel_Start_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_usagemodel_Start)
gen_pcm_usagemodel_ClosedWorkload_Workload = Generalization(general=Workload, specific=pcm_usagemodel_ClosedWorkload)
gen_pcm_usagemodel_OpenWorkload_Workload = Generalization(general=Workload, specific=pcm_usagemodel_OpenWorkload)
gen_pcm_usagemodel_Loop_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_usagemodel_Loop)
gen_pcm_usagemodel_EntryLevelSystemCall_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_usagemodel_EntryLevelSystemCall)
gen_pcm_usagemodel_Delay_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_usagemodel_Delay)
gen_pcm_usagemodel_Branch_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_usagemodel_Branch)

# Domain Model
domain_model = DomainModel(
    name="pcm",
    types={pcm_core_PCMRandomVariable, RandomVariable, pcm_entity_Entity, Identifier, entity_NamedElement, pcm_entity_NamedElement, pcm_entity_InterfaceProvidingEntity, Entity, ProvidedRole, pcm_entity_InterfaceProvidingRequiringEntity, entity_InterfaceProvidingEntity, entity_InterfaceRequiringEntity, pcm_entity_InterfaceRequiringEntity, RequiredRole, pcm_entity_ComposedProvidingRequiringEntity, composition_ComposedStructure, entity_InterfaceProvidingRequiringEntity, pcm_connectors_Connector, pcm_composition_ProvidedDelegationConnector, DelegationConnector, composition_AssemblyContext, pcm_composition_AssemblyContext, ProvidesComponentType, VariableUsage, pcm_composition_RequiredDelegationConnector, pcm_composition_AssemblyConnector, connectors_Connector, entity_Entity, pcm_composition_ComposedStructure, composition_ProvidedDelegationConnector, composition_RequiredDelegationConnector, composition_AssemblyConnector, pcm_repository_PassiveResource, PCMRandomVariable, pcm_repository_Signature, Parameter_, Interface, DataType, ExceptionType, pcm_repository_Parameter, Signature, pcm_repository_DataType, Repository, pcm_repository_Repository, pcm_repository_ProvidesComponentType, pcm_repository_RequiredRole, Role, pcm_repository_Role, pcm_repository_Interface, Protocol, pcm_repository_ExceptionType, pcm_repository_ImplementationComponentType, CompleteComponentType, pcm_repository_CompleteComponentType, pcm_repository_DelegationConnector, Connector, pcm_repository_CompositeComponent, repository_ImplementationComponentType, entity_ComposedProvidingRequiringEntity, ImplementationComponentType, pcm_repository_CollectionDataType, pcm_repository_BasicComponent, ServiceEffectSpecification, PassiveResource, pcm_repository_PrimitiveDataType, repository_DataType, pcm_repository_CompositeDataType, CompositeDataType, InnerDeclaration, pcm_repository_InnerDeclaration, NamedElement, pcm_repository_ProvidedRole, ParametricResourceDemand, pcm_protocol_ServiceCall, pcm_protocol_Protocol, pcm_parameter_VariableCharacterisation, pcm_parameter_CharacterisedVariable, Variable, pcm_parameter_VariableUsage, VariableCharacterisation, parameter_pcm_AbstractNamedReference, pcm_seff_StopAction, AbstractResourceDemandingAction, pcm_seff_AbstractResourceDemandingAction, AbstractAction, pcm_seff_AbstractAction, pcm_seff_ParametricResourceDemand, ProcessingResourceType, pcm_seff_StartAction, pcm_seff_ResourceDemandingSEFF, seff_ServiceEffectSpecification, seff_ResourceDemandingBehaviour, pcm_seff_ResourceDemandingBehaviour, pcm_seff_SynchronisationPoint, pcm_seff_ReleaseAction, pcm_seff_LoopAction, AbstractLoopAction, pcm_seff_AbstractLoopAction, ResourceDemandingBehaviour, pcm_seff_InternalAction, pcm_seff_ForkAction, ForkedBehaviour, SynchronisationPoint, pcm_seff_ForkedBehaviour, pcm_seff_ExternalCallAction, pcm_seff_ProbabilisticBranchTransition, AbstractBranchTransition, pcm_seff_AbstractBranchTransition, pcm_seff_BranchAction, pcm_seff_AcquireAction, pcm_seff_CollectionIteratorAction, pcm_seff_GuardedBranchTransition, pcm_seff_SetVariableAction, pcm_seff_ServiceEffectSpecification, pcm_resourcetype_ResourceType, UnitCarryingElement, pcm_resourcetype_ResourceRepository, ResourceType, pcm_resourcetype_CommunicationLinkResourceType, pcm_resourcetype_ProcessingResourceType, pcm_allocation_AllocationContext, pcm_resourceenvironment_LinkingResource, ResourceContainer, pcm_allocation_Allocation, AllocationContext, ResourceEnvironment, System, pcm_resourceenvironment_ResourceEnvironment, LinkingResource, CommunicationLinkResourceSpecification, pcm_resourceenvironment_CommunicationLinkResourceSpecification, CommunicationLinkResourceType, pcm_resourceenvironment_ProcessingResourceSpecification, pcm_resourceenvironment_ResourceContainer, ProcessingResourceSpecification, pcm_system_System, QoSAnnotations, pcm_qosannotations_SpecifiedExecutionTime, pcm_qosannotations_SpecifiedFailureProbability, pcm_qosannotations_SystemSpecifiedExecutionTime, SpecifiedExecutionTime, pcm_qosannotations_ComponentSpecifiedExecutionTime, pcm_qosannotations_SpecifiedOutputParameterAbstraction, pcm_qosannotations_QoSAnnotations, SpecifiedOutputParameterAbstraction, pcm_usagemodel_Workload, pcm_usagemodel_UsageScenario, Workload, ScenarioBehaviour, pcm_usagemodel_ScenarioBehaviour, AbstractUserAction, pcm_usagemodel_AbstractUserAction, pcm_usagemodel_UsageModel, UsageScenario, UserData, pcm_usagemodel_UserData, pcm_usagemodel_Stop, pcm_usagemodel_Start, pcm_usagemodel_ClosedWorkload, pcm_usagemodel_OpenWorkload, pcm_usagemodel_Loop, pcm_usagemodel_EntryLevelSystemCall, BranchTransition, pcm_usagemodel_BranchTransition, pcm_usagemodel_Delay, pcm_usagemodel_Branch, ParameterModifier, PrimitiveTypeEnum, VariableCharacterisationType, SchedulingPolicy},
    associations={providedRoles_InterfaceProvidingEntity0, requiredRoles_InterfaceRequiringEntity1, innerProvidedRole_ProvidedDelegationConnector2, outerProvidedRole_ProvidedDelegationConnector4, childComponentContext_ProvidedDelegationConnector7, parentStructure_ProvidedDelegationConnector9, encapsulatedComponent_ChildComponentContext10, parentStructure_AssemblyContext11, configParameterUsages_AssemblyContext13, innerRequiredRole_RequiredDelegationConnector15, outerRequiredRole_RequiredDelegationConnector17, childComponentContext_RequiredDelegationConnector20, parentStructure_RequiredDelegationConnector23, requiringChildComponentContext_CompositeAssemblyConnector25, providingChildComponentContext_CompositeAssemblyConnector27, providedRole_CompositeAssemblyConnector30, requiredRole_CompositeAssemblyConnector33, parentStructure_AssemblyConnector36, childComponentContexts_ComposedStructure38, providedDelegationConnectors_ComposedStructure39, requiredDelegationConnectors_ComposedStructure40, compositeAssemblyConnectors_ComposedStructure41, capacity_PassiveResource42, parameters__Signature43, interface_Signature44, returntype__Signature45, exceptions__Signature46, datatype__Parameter48, signature_Parameter50, repository_DataType51, components__Repository52, interfaces__Repository54, datatypes_Repository56, repository_ProvidesComponentType58, requiredInterface__RequiredRole60, requiringEntity_RequiredRole62, parentInterface__Interface63, anchestorInterfaces_Interface65, protocols__Interface68, signatures__Interface70, repository_Interface72, implementationComponentType80, parentCompleteComponentTypes74, componentParameterUsage_ImplementationComponentType75, parentProvidesComponentTypes78, implementationComponentType81, serviceEffectSpecifications__BasicComponent83, passiveResource_BasicComponent85, innerType_CollectionDataType87, parentType_CompositeDataType89, innerDeclaration_CompositeDataType90, datatype_InnerDeclaration92, providedInterface__ProvidedRole94, providingEntity_ProvidedRole96, signature__ServiceCall97, specification_VariableCharacterisation99, variableCharacterisation_VariableUsage101, namedReference_VariableUsage102, resourceDemand_Action104, predecessor_AbstractAction105, successor_AbstractAction106, requiredResource_ParametricResourceDemand108, specification_ParametericResourceDemand109, action_ParametricResourceDemand112, steps_Behaviour113, passiveResource_ReleaseAction115, iterationCount_LoopAction117, bodyBehaviour_Loop119, asynchronousForkedBehaviours_ForkAction120, synchronisingBehaviours_ForkAction121, synchronousForkedBehaviours_SynchronisationPoint123, outputParameterUsage_SynchronisationPoint125, calledService_ExternalService128, inputParameterUsages_ExternalCallAction130, outputVariableUsages_ExternalCallAction133, role_ExternalService136, branchBehaviour_BranchTransition138, branches_Branch140, passiveresource_AcquireAction141, parameter_CollectionIteratorAction143, branchCondition_GuardedBranchTransition145, localVariableUsages_SetVariableAction147, describedService__SEFF149, availableResourceTypes_ResourceRepository151, resourceContainer_AllocationContext152, assemblyContext_AllocationContext153, allocationContexts_Allocation156, targetResourceEnvironment_Allocation157, system_Allocation159, linkingresource161, resourceContainer_ResourceEnvironment162, toResourceContainer_LinkingResource165, fromResourceContainer_LinkingResource167, communicationLinkResourceSpecifications_LinkingResource170, communicationLinkResourceType_CommunicationLinkResourceSpecification172, latency_CommunicationLinkResourceSpecification173, throughput_CommunicationLinkResourceSpecification176, activeResourceType_ActiveResourceSpecification179, processingRate_ProcessingResourceSpecification181, activeResourceSpecifications_ResourceContainer184, qosAnnotations_System185, signature_SpecifiedTimeConsumption186, role_SpecifiedExecutionTime188, specification_SpecifiedExecutionTime191, assemblyContext_ComponentSpecifiedExecutionTime194, signature_SpecifiedOutputParameterAbstraction196, role_SpecifiedOutputParameterAbstraction198, expectedExternalOutputs_SpecifiedOutputParameterAbstraction201, specifiedExecutionTimes_QoSAnnotations204, specifiedOutputParameterAbstractions_QoSAnnotations205, workload_UsageScenario207, scenarioBehaviour_UsageScenario208, successor211, actions_ScenarioBehaviour210, predecessor213, usageScenario_UsageModel215, userData_UsageModel216, userDataParameterUsages_UserData218, assemblyContext_userData220, inputParameterUsages_EntryLevelSystemCall230, providedRole_EntryLevelSystemCall232, signature_EntryLevelSystemCall235, outputParameterUsages_EntryLevelSystemCall238, interArrivalTime_OpenWorkload223, bodyBehaviour_Loop225, loopIteration_Loop227, branchTransitions_Branch243, branchedBehaviour_BranchTransition244, timeSpecification_Delay246, thinkTime_ClosedWorkload241},
    generalizations={gen_pcm_core_PCMRandomVariable_RandomVariable, gen_pcm_entity_Entity_Identifier, gen_pcm_entity_Entity_entity_NamedElement, gen_pcm_entity_InterfaceProvidingEntity_Entity, gen_pcm_entity_InterfaceProvidingRequiringEntity_entity_InterfaceProvidingEntity, gen_pcm_entity_InterfaceProvidingRequiringEntity_entity_InterfaceRequiringEntity, gen_pcm_entity_InterfaceRequiringEntity_Entity, gen_pcm_entity_ComposedProvidingRequiringEntity_composition_ComposedStructure, gen_pcm_entity_ComposedProvidingRequiringEntity_entity_InterfaceProvidingRequiringEntity, gen_pcm_connectors_Connector_Entity, gen_pcm_composition_ProvidedDelegationConnector_DelegationConnector, gen_pcm_composition_AssemblyContext_Entity, gen_pcm_composition_RequiredDelegationConnector_DelegationConnector, gen_pcm_composition_ComposedStructure_Entity, gen_pcm_composition_AssemblyConnector_connectors_Connector, gen_pcm_composition_AssemblyConnector_entity_Entity, gen_pcm_repository_PassiveResource_Entity, gen_pcm_repository_Repository_Entity, gen_pcm_repository_ProvidesComponentType_entity_Entity, gen_pcm_repository_ProvidesComponentType_entity_InterfaceProvidingRequiringEntity, gen_pcm_repository_RequiredRole_Role, gen_pcm_repository_Role_Entity, gen_pcm_repository_Interface_Entity, gen_pcm_repository_ImplementationComponentType_CompleteComponentType, gen_pcm_repository_CompleteComponentType_ProvidesComponentType, gen_pcm_repository_DelegationConnector_Connector, gen_pcm_repository_CompositeComponent_repository_ImplementationComponentType, gen_pcm_repository_CompositeComponent_entity_ComposedProvidingRequiringEntity, gen_pcm_repository_BasicComponent_ImplementationComponentType, gen_pcm_repository_PrimitiveDataType_DataType, gen_pcm_repository_CollectionDataType_entity_Entity, gen_pcm_repository_CollectionDataType_repository_DataType, gen_pcm_repository_CompositeDataType_entity_Entity, gen_pcm_repository_CompositeDataType_repository_DataType, gen_pcm_repository_InnerDeclaration_NamedElement, gen_pcm_repository_ProvidedRole_Role, gen_pcm_parameter_CharacterisedVariable_Variable, gen_pcm_seff_StopAction_AbstractResourceDemandingAction, gen_pcm_seff_AbstractResourceDemandingAction_AbstractAction, gen_pcm_seff_AbstractAction_Entity, gen_pcm_seff_StartAction_AbstractResourceDemandingAction, gen_pcm_seff_ResourceDemandingSEFF_Identifier, gen_pcm_seff_ResourceDemandingSEFF_seff_ServiceEffectSpecification, gen_pcm_seff_ResourceDemandingSEFF_seff_ResourceDemandingBehaviour, gen_pcm_seff_ForkedBehaviour_ResourceDemandingBehaviour, gen_pcm_seff_ReleaseAction_AbstractResourceDemandingAction, gen_pcm_seff_LoopAction_AbstractLoopAction, gen_pcm_seff_AbstractLoopAction_AbstractResourceDemandingAction, gen_pcm_seff_InternalAction_AbstractResourceDemandingAction, gen_pcm_seff_ForkAction_AbstractResourceDemandingAction, gen_pcm_seff_ExternalCallAction_AbstractAction, gen_pcm_seff_ProbabilisticBranchTransition_AbstractBranchTransition, gen_pcm_seff_AbstractBranchTransition_Identifier, gen_pcm_seff_BranchAction_AbstractResourceDemandingAction, gen_pcm_seff_AcquireAction_AbstractResourceDemandingAction, gen_pcm_allocation_AllocationContext_Entity, gen_pcm_seff_CollectionIteratorAction_AbstractLoopAction, gen_pcm_seff_GuardedBranchTransition_AbstractBranchTransition, gen_pcm_seff_SetVariableAction_AbstractResourceDemandingAction, gen_pcm_resourcetype_ResourceType_entity_Entity, gen_pcm_resourcetype_ResourceType_UnitCarryingElement, gen_pcm_resourcetype_CommunicationLinkResourceType_ProcessingResourceType, gen_pcm_resourcetype_ProcessingResourceType_ResourceType, gen_pcm_resourceenvironment_LinkingResource_Entity, gen_pcm_allocation_Allocation_Entity, gen_pcm_resourceenvironment_ResourceContainer_Entity, gen_pcm_system_System_entity_Entity, gen_pcm_system_System_entity_ComposedProvidingRequiringEntity, gen_pcm_qosannotations_SystemSpecifiedExecutionTime_SpecifiedExecutionTime, gen_pcm_qosannotations_ComponentSpecifiedExecutionTime_SpecifiedExecutionTime, gen_pcm_qosannotations_QoSAnnotations_Entity, gen_pcm_usagemodel_UsageScenario_Entity, gen_pcm_usagemodel_ScenarioBehaviour_Entity, gen_pcm_usagemodel_AbstractUserAction_Entity, gen_pcm_usagemodel_Stop_AbstractUserAction, gen_pcm_usagemodel_Start_AbstractUserAction, gen_pcm_usagemodel_ClosedWorkload_Workload, gen_pcm_usagemodel_OpenWorkload_Workload, gen_pcm_usagemodel_Loop_AbstractUserAction, gen_pcm_usagemodel_EntryLevelSystemCall_AbstractUserAction, gen_pcm_usagemodel_Delay_AbstractUserAction, gen_pcm_usagemodel_Branch_AbstractUserAction},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)