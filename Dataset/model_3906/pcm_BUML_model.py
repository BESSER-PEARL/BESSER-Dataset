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
pcm_core_PCMRandomVariable = Class(name="pcm::core::PCMRandomVariable")
RandomVariable = Class(name="RandomVariable")
pcm_entity_ResourceInterfaceRequiringEntity = Class(name="pcm::entity::ResourceInterfaceRequiringEntity", is_abstract=True)
ResourceRequiredRole = Class(name="ResourceRequiredRole")
pcm_entity_ComposedProvidingRequiringEntity = Class(name="pcm::entity::ComposedProvidingRequiringEntity", is_abstract=True)
composition_ComposedStructure = Class(name="composition::ComposedStructure")
entity_InterfaceProvidingRequiringEntity = Class(name="entity::InterfaceProvidingRequiringEntity")
pcm_entity_Entity = Class(name="pcm::entity::Entity", is_abstract=True)
Identifier = Class(name="Identifier")
entity_NamedElement = Class(name="entity::NamedElement")
pcm_entity_NamedElement = Class(name="pcm::entity::NamedElement", is_abstract=True)
pcm_entity_InterfaceProvidingEntity = Class(name="pcm::entity::InterfaceProvidingEntity", is_abstract=True)
Entity = Class(name="Entity")
ProvidedRole = Class(name="ProvidedRole")
pcm_entity_InterfaceProvidingRequiringEntity = Class(name="pcm::entity::InterfaceProvidingRequiringEntity", is_abstract=True)
entity_InterfaceProvidingEntity = Class(name="entity::InterfaceProvidingEntity")
entity_InterfaceRequiringEntity = Class(name="entity::InterfaceRequiringEntity")
entity_ResourceInterfaceRequiringEntity = Class(name="entity::ResourceInterfaceRequiringEntity")
pcm_entity_InterfaceRequiringEntity = Class(name="pcm::entity::InterfaceRequiringEntity", is_abstract=True)
RequiredRole = Class(name="RequiredRole")
pcm_composition_AssemblyContext = Class(name="pcm::composition::AssemblyContext")
RepositoryComponent = Class(name="RepositoryComponent")
VariableUsage = Class(name="VariableUsage")
pcm_composition_RequiredDelegationConnector = Class(name="pcm::composition::RequiredDelegationConnector")
pcm_connectors_Connector = Class(name="pcm::connectors::Connector", is_abstract=True)
pcm_composition_ProvidedDelegationConnector = Class(name="pcm::composition::ProvidedDelegationConnector")
DelegationConnector = Class(name="DelegationConnector")
composition_AssemblyContext = Class(name="composition::AssemblyContext")
pcm_composition_AssemblyConnector = Class(name="pcm::composition::AssemblyConnector")
Connector = Class(name="Connector")
pcm_composition_ComposedStructure = Class(name="pcm::composition::ComposedStructure", is_abstract=True)
composition_ProvidedDelegationConnector = Class(name="composition::ProvidedDelegationConnector")
pcm_composition_ResourceRequiredDelegationConnector = Class(name="pcm::composition::ResourceRequiredDelegationConnector")
Parameter_ = Class(name="Parameter")
Interface = Class(name="Interface")
DataType = Class(name="DataType")
composition_RequiredDelegationConnector = Class(name="composition::RequiredDelegationConnector")
ExceptionType = Class(name="ExceptionType")
composition_AssemblyConnector = Class(name="composition::AssemblyConnector")
composition_ResourceRequiredDelegationConnector = Class(name="composition::ResourceRequiredDelegationConnector")
pcm_repository_PassiveResource = Class(name="pcm::repository::PassiveResource")
PCMRandomVariable = Class(name="PCMRandomVariable")
pcm_repository_Signature = Class(name="pcm::repository::Signature")
pcm_repository_RepositoryComponent = Class(name="pcm::repository::RepositoryComponent", is_abstract=True)
InterfaceProvidingRequiringEntity = Class(name="InterfaceProvidingRequiringEntity")
pcm_repository_RequiredRole = Class(name="pcm::repository::RequiredRole")
Role = Class(name="Role")
pcm_repository_Parameter = Class(name="pcm::repository::Parameter")
Signature = Class(name="Signature")
pcm_repository_DataType = Class(name="pcm::repository::DataType", is_abstract=True)
Repository = Class(name="Repository")
pcm_repository_Repository = Class(name="pcm::repository::Repository")
Protocol = Class(name="Protocol")
pcm_repository_ResourceRequiredRole = Class(name="pcm::repository::ResourceRequiredRole")
pcm_repository_Role = Class(name="pcm::repository::Role", is_abstract=True)
pcm_repository_Interface = Class(name="pcm::repository::Interface")
CompleteComponentType = Class(name="CompleteComponentType")
pcm_repository_CompleteComponentType = Class(name="pcm::repository::CompleteComponentType")
pcm_repository_ExceptionType = Class(name="pcm::repository::ExceptionType")
pcm_repository_ProvidesComponentType = Class(name="pcm::repository::ProvidesComponentType")
pcm_repository_ImplementationComponentType = Class(name="pcm::repository::ImplementationComponentType", is_abstract=True)
pcm_repository_BasicComponent = Class(name="pcm::repository::BasicComponent")
ImplementationComponentType = Class(name="ImplementationComponentType")
ProvidesComponentType = Class(name="ProvidesComponentType")
pcm_repository_DelegationConnector = Class(name="pcm::repository::DelegationConnector", is_abstract=True)
pcm_repository_CompositeComponent = Class(name="pcm::repository::CompositeComponent")
entity_ComposedProvidingRequiringEntity = Class(name="entity::ComposedProvidingRequiringEntity")
repository_ImplementationComponentType = Class(name="repository::ImplementationComponentType")
CompositeDataType = Class(name="CompositeDataType")
InnerDeclaration = Class(name="InnerDeclaration")
pcm_repository_InnerDeclaration = Class(name="pcm::repository::InnerDeclaration")
NamedElement = Class(name="NamedElement")
pcm_repository_ProvidedRole = Class(name="pcm::repository::ProvidedRole")
ServiceEffectSpecification = Class(name="ServiceEffectSpecification")
PassiveResource = Class(name="PassiveResource")
pcm_repository_PrimitiveDataType = Class(name="pcm::repository::PrimitiveDataType")
pcm_repository_CollectionDataType = Class(name="pcm::repository::CollectionDataType")
entity_Entity = Class(name="entity::Entity")
repository_DataType = Class(name="repository::DataType")
pcm_repository_CompositeDataType = Class(name="pcm::repository::CompositeDataType")
pcm_parameter_CharacterisedVariable = Class(name="pcm::parameter::CharacterisedVariable")
Variable = Class(name="Variable")
pcm_parameter_VariableUsage = Class(name="pcm::parameter::VariableUsage")
VariableCharacterisation = Class(name="VariableCharacterisation")
parameter_pcm_AbstractNamedReference = Class(name="parameter::pcm::AbstractNamedReference")
pcm_seff_StopAction = Class(name="pcm::seff::StopAction")
AbstractInternalControlFlowAction = Class(name="AbstractInternalControlFlowAction")
pcm_protocol_ServiceCall = Class(name="pcm::protocol::ServiceCall", is_abstract=True)
pcm_protocol_Protocol = Class(name="pcm::protocol::Protocol", is_abstract=True)
pcm_parameter_VariableCharacterisation = Class(name="pcm::parameter::VariableCharacterisation")
pcm_seff_ResourceDemandingBehaviour = Class(name="pcm::seff::ResourceDemandingBehaviour")
pcm_seff_AbstractInternalControlFlowAction = Class(name="pcm::seff::AbstractInternalControlFlowAction", is_abstract=True)
AbstractAction = Class(name="AbstractAction")
performance_ParametricResourceDemand = Class(name="performance::ParametricResourceDemand")
pcm_seff_AbstractAction = Class(name="pcm::seff::AbstractAction", is_abstract=True)
pcm_seff_StartAction = Class(name="pcm::seff::StartAction")
pcm_seff_ResourceDemandingSEFF = Class(name="pcm::seff::ResourceDemandingSEFF")
seff_ServiceEffectSpecification = Class(name="seff::ServiceEffectSpecification")
seff_ResourceDemandingBehaviour = Class(name="seff::ResourceDemandingBehaviour")
ForkedBehaviour = Class(name="ForkedBehaviour")
SynchronisationPoint = Class(name="SynchronisationPoint")
pcm_seff_ForkedBehaviour = Class(name="pcm::seff::ForkedBehaviour")
pcm_seff_SynchronisationPoint = Class(name="pcm::seff::SynchronisationPoint")
pcm_seff_ExternalCallAction = Class(name="pcm::seff::ExternalCallAction")
pcm_seff_ReleaseAction = Class(name="pcm::seff::ReleaseAction")
pcm_seff_LoopAction = Class(name="pcm::seff::LoopAction")
AbstractLoopAction = Class(name="AbstractLoopAction")
pcm_seff_AbstractLoopAction = Class(name="pcm::seff::AbstractLoopAction", is_abstract=True)
ResourceDemandingBehaviour = Class(name="ResourceDemandingBehaviour")
pcm_seff_InternalAction = Class(name="pcm::seff::InternalAction")
pcm_seff_ForkAction = Class(name="pcm::seff::ForkAction")
pcm_seff_AcquireAction = Class(name="pcm::seff::AcquireAction")
pcm_seff_CollectionIteratorAction = Class(name="pcm::seff::CollectionIteratorAction")
pcm_seff_GuardedBranchTransition = Class(name="pcm::seff::GuardedBranchTransition")
pcm_seff_ProbabilisticBranchTransition = Class(name="pcm::seff::ProbabilisticBranchTransition")
AbstractBranchTransition = Class(name="AbstractBranchTransition")
pcm_seff_AbstractBranchTransition = Class(name="pcm::seff::AbstractBranchTransition", is_abstract=True)
pcm_seff_BranchAction = Class(name="pcm::seff::BranchAction")
pcm_resourcetype_ResourceType = Class(name="pcm::resourcetype::ResourceType", is_abstract=True)
UnitCarryingElement = Class(name="UnitCarryingElement")
pcm_resourcetype_ResourceRepository = Class(name="pcm::resourcetype::ResourceRepository")
ResourceType = Class(name="ResourceType")
pcm_resourcetype_CommunicationLinkResourceType = Class(name="pcm::resourcetype::CommunicationLinkResourceType")
pcm_resourcetype_ProcessingResourceType = Class(name="pcm::resourcetype::ProcessingResourceType")
pcm_allocation_AllocationContext = Class(name="pcm::allocation::AllocationContext")
ResourceContainer = Class(name="ResourceContainer")
pcm_allocation_Allocation = Class(name="pcm::allocation::Allocation")
pcm_seff_SetVariableAction = Class(name="pcm::seff::SetVariableAction")
pcm_seff_ServiceEffectSpecification = Class(name="pcm::seff::ServiceEffectSpecification", is_abstract=True)
pcm_performance_ParametricResourceDemand = Class(name="pcm::performance::ParametricResourceDemand")
ProcessingResourceType = Class(name="ProcessingResourceType")
pcm_resourceenvironment_CommunicationLinkResourceSpecification = Class(name="pcm::resourceenvironment::CommunicationLinkResourceSpecification")
CommunicationLinkResourceType = Class(name="CommunicationLinkResourceType")
pcm_resourceenvironment_ProcessingResourceSpecification = Class(name="pcm::resourceenvironment::ProcessingResourceSpecification")
AllocationContext = Class(name="AllocationContext")
ResourceEnvironment = Class(name="ResourceEnvironment")
System = Class(name="System")
pcm_resourceenvironment_ResourceEnvironment = Class(name="pcm::resourceenvironment::ResourceEnvironment")
LinkingResource = Class(name="LinkingResource")
pcm_resourceenvironment_LinkingResource = Class(name="pcm::resourceenvironment::LinkingResource")
CommunicationLinkResourceSpecification = Class(name="CommunicationLinkResourceSpecification")
pcm_qosannotations_SpecifiedOutputParameterAbstraction = Class(name="pcm::qosannotations::SpecifiedOutputParameterAbstraction", is_abstract=True)
pcm_qosannotations_QoSAnnotations = Class(name="pcm::qosannotations::QoSAnnotations")
SpecifiedQoSAnnotation = Class(name="SpecifiedQoSAnnotation")
SpecifiedOutputParameterAbstraction = Class(name="SpecifiedOutputParameterAbstraction")
pcm_resourceenvironment_ResourceContainer = Class(name="pcm::resourceenvironment::ResourceContainer")
ProcessingResourceSpecification = Class(name="ProcessingResourceSpecification")
pcm_system_System = Class(name="pcm::system::System")
QoSAnnotations = Class(name="QoSAnnotations")
pcm_qosannotations_SpecifiedQoSAnnotation = Class(name="pcm::qosannotations::SpecifiedQoSAnnotation", is_abstract=True)
pcm_performance_SystemSpecifiedExecutionTime = Class(name="pcm::performance::SystemSpecifiedExecutionTime")
pcm_performance_ComponentSpecifiedExecutionTime = Class(name="pcm::performance::ComponentSpecifiedExecutionTime")
pcm_reliability_SpecifiedFailureProbability = Class(name="pcm::reliability::SpecifiedFailureProbability")
pcm_usagemodel_Workload = Class(name="pcm::usagemodel::Workload", is_abstract=True)
pcm_usagemodel_UsageScenario = Class(name="pcm::usagemodel::UsageScenario")
Workload = Class(name="Workload")
ScenarioBehaviour = Class(name="ScenarioBehaviour")
pcm_usagemodel_ScenarioBehaviour = Class(name="pcm::usagemodel::ScenarioBehaviour")
pcm_usagemodel_Stop = Class(name="pcm::usagemodel::Stop")
pcm_usagemodel_Start = Class(name="pcm::usagemodel::Start")
AbstractUserAction = Class(name="AbstractUserAction")
pcm_usagemodel_AbstractUserAction = Class(name="pcm::usagemodel::AbstractUserAction", is_abstract=True)
pcm_usagemodel_UsageModel = Class(name="pcm::usagemodel::UsageModel")
UsageScenario = Class(name="UsageScenario")
UserData = Class(name="UserData")
pcm_usagemodel_UserData = Class(name="pcm::usagemodel::UserData")
pcm_usagemodel_Loop = Class(name="pcm::usagemodel::Loop")
pcm_usagemodel_EntryLevelSystemCall = Class(name="pcm::usagemodel::EntryLevelSystemCall")
pcm_usagemodel_OpenWorkload = Class(name="pcm::usagemodel::OpenWorkload")
pcm_usagemodel_ClosedWorkload = Class(name="pcm::usagemodel::ClosedWorkload")
BranchTransition = Class(name="BranchTransition")
pcm_usagemodel_BranchTransition = Class(name="pcm::usagemodel::BranchTransition")
pcm_usagemodel_Delay = Class(name="pcm::usagemodel::Delay")
pcm_subsystem_SubSystem = Class(name="pcm::subsystem::SubSystem")
repository_RepositoryComponent = Class(name="repository::RepositoryComponent")
pcm_usagemodel_Branch = Class(name="pcm::usagemodel::Branch")

# pcm_core_PCMRandomVariable class attributes and methods
pcm_core_PCMRandomVariable_m_SpecificationMustNotBeNULL: Method = Method(name="SpecificationMustNotBeNULL", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_core_PCMRandomVariable.methods={pcm_core_PCMRandomVariable_m_SpecificationMustNotBeNULL}

# RandomVariable class attributes and methods

# pcm_entity_ResourceInterfaceRequiringEntity class attributes and methods

# ResourceRequiredRole class attributes and methods

# pcm_entity_ComposedProvidingRequiringEntity class attributes and methods
pcm_entity_ComposedProvidingRequiringEntity_m_ProvidedRolesMustBeBound: Method = Method(name="ProvidedRolesMustBeBound", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_entity_ComposedProvidingRequiringEntity.methods={pcm_entity_ComposedProvidingRequiringEntity_m_ProvidedRolesMustBeBound}

# composition_ComposedStructure class attributes and methods

# entity_InterfaceProvidingRequiringEntity class attributes and methods

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

# pcm_entity_InterfaceRequiringEntity class attributes and methods

# RequiredRole class attributes and methods

# pcm_composition_AssemblyContext class attributes and methods

# RepositoryComponent class attributes and methods

# VariableUsage class attributes and methods

# pcm_composition_RequiredDelegationConnector class attributes and methods
pcm_composition_RequiredDelegationConnector_m_RequiredDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure: Method = Method(name="RequiredDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_composition_RequiredDelegationConnector_m_ComponentOfAssemblyContextAndInnerRoleRequiringComponentNeedToBeTheSame: Method = Method(name="ComponentOfAssemblyContextAndInnerRoleRequiringComponentNeedToBeTheSame", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_composition_RequiredDelegationConnector.methods={pcm_composition_RequiredDelegationConnector_m_RequiredDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure, pcm_composition_RequiredDelegationConnector_m_ComponentOfAssemblyContextAndInnerRoleRequiringComponentNeedToBeTheSame}

# pcm_connectors_Connector class attributes and methods

# pcm_composition_ProvidedDelegationConnector class attributes and methods
pcm_composition_ProvidedDelegationConnector_m_ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure: Method = Method(name="ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_composition_ProvidedDelegationConnector_m_ComponentOfAssemblyContextAndInnerRoleProvidingComponentNeedToBeTheSame: Method = Method(name="ComponentOfAssemblyContextAndInnerRoleProvidingComponentNeedToBeTheSame", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_composition_ProvidedDelegationConnector.methods={pcm_composition_ProvidedDelegationConnector_m_ComponentOfAssemblyContextAndInnerRoleProvidingComponentNeedToBeTheSame, pcm_composition_ProvidedDelegationConnector_m_ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure}

# DelegationConnector class attributes and methods

# composition_AssemblyContext class attributes and methods

# pcm_composition_AssemblyConnector class attributes and methods
pcm_composition_AssemblyConnector_m_AssemblyConnectorsReferencedRequiredRoleAndChildContextMustMatch: Method = Method(name="AssemblyConnectorsReferencedRequiredRoleAndChildContextMustMatch", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_composition_AssemblyConnector_m_AssemblyConnectorsReferencedProvidedRolesAndChildContextMustMatch: Method = Method(name="AssemblyConnectorsReferencedProvidedRolesAndChildContextMustMatch", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_composition_AssemblyConnector.methods={pcm_composition_AssemblyConnector_m_AssemblyConnectorsReferencedProvidedRolesAndChildContextMustMatch, pcm_composition_AssemblyConnector_m_AssemblyConnectorsReferencedRequiredRoleAndChildContextMustMatch}

# Connector class attributes and methods

# pcm_composition_ComposedStructure class attributes and methods

# composition_ProvidedDelegationConnector class attributes and methods

# pcm_composition_ResourceRequiredDelegationConnector class attributes and methods

# Parameter class attributes and methods

# Interface class attributes and methods

# DataType class attributes and methods

# composition_RequiredDelegationConnector class attributes and methods

# ExceptionType class attributes and methods

# composition_AssemblyConnector class attributes and methods

# composition_ResourceRequiredDelegationConnector class attributes and methods

# pcm_repository_PassiveResource class attributes and methods

# PCMRandomVariable class attributes and methods

# pcm_repository_Signature class attributes and methods
pcm_repository_Signature_serviceName: Property = Property(name="serviceName", type=StringType)
pcm_repository_Signature_m_ParameterNamesHaveToBeUniqueForASignature: Method = Method(name="ParameterNamesHaveToBeUniqueForASignature", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_repository_Signature.attributes={pcm_repository_Signature_serviceName}
pcm_repository_Signature.methods={pcm_repository_Signature_m_ParameterNamesHaveToBeUniqueForASignature}

# pcm_repository_RepositoryComponent class attributes and methods

# InterfaceProvidingRequiringEntity class attributes and methods

# pcm_repository_RequiredRole class attributes and methods

# Role class attributes and methods

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

# Protocol class attributes and methods

# pcm_repository_ResourceRequiredRole class attributes and methods

# pcm_repository_Role class attributes and methods

# pcm_repository_Interface class attributes and methods
pcm_repository_Interface_m_NoProtocolTypeIDUsedTwice: Method = Method(name="NoProtocolTypeIDUsedTwice", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_repository_Interface_m_SignaturesHaveToBeUniqueForAnInterface: Method = Method(name="SignaturesHaveToBeUniqueForAnInterface", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_repository_Interface.methods={pcm_repository_Interface_m_SignaturesHaveToBeUniqueForAnInterface, pcm_repository_Interface_m_NoProtocolTypeIDUsedTwice}

# CompleteComponentType class attributes and methods

# pcm_repository_CompleteComponentType class attributes and methods
pcm_repository_CompleteComponentType_m_AtLeastOneInterfaceHasToBeProvidedOrRequiredByAUsefullCompleteComponentType: Method = Method(name="AtLeastOneInterfaceHasToBeProvidedOrRequiredByAUsefullCompleteComponentType", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_repository_CompleteComponentType_m_providedInterfacesHaveToConformToProvidedType2: Method = Method(name="providedInterfacesHaveToConformToProvidedType2", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_repository_CompleteComponentType.methods={pcm_repository_CompleteComponentType_m_providedInterfacesHaveToConformToProvidedType2, pcm_repository_CompleteComponentType_m_AtLeastOneInterfaceHasToBeProvidedOrRequiredByAUsefullCompleteComponentType}

# pcm_repository_ExceptionType class attributes and methods
pcm_repository_ExceptionType_exceptionName: Property = Property(name="exceptionName", type=StringType)
pcm_repository_ExceptionType_exceptionMessage: Property = Property(name="exceptionMessage", type=StringType)
pcm_repository_ExceptionType.attributes={pcm_repository_ExceptionType_exceptionName, pcm_repository_ExceptionType_exceptionMessage}

# pcm_repository_ProvidesComponentType class attributes and methods
pcm_repository_ProvidesComponentType_m_AtLeastOneInterfaceHasToBeProvidedByAUsefullProvidesComponentType: Method = Method(name="AtLeastOneInterfaceHasToBeProvidedByAUsefullProvidesComponentType", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_repository_ProvidesComponentType.methods={pcm_repository_ProvidesComponentType_m_AtLeastOneInterfaceHasToBeProvidedByAUsefullProvidesComponentType}

# pcm_repository_ImplementationComponentType class attributes and methods
pcm_repository_ImplementationComponentType_m_RequiredInterfacesHaveToConformToCompleteType: Method = Method(name="RequiredInterfacesHaveToConformToCompleteType", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_repository_ImplementationComponentType_m_providedInterfacesHaveToConformToCompleteType: Method = Method(name="providedInterfacesHaveToConformToCompleteType", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_repository_ImplementationComponentType.methods={pcm_repository_ImplementationComponentType_m_RequiredInterfacesHaveToConformToCompleteType, pcm_repository_ImplementationComponentType_m_providedInterfacesHaveToConformToCompleteType}

# pcm_repository_BasicComponent class attributes and methods
pcm_repository_BasicComponent_m_NoSeffTypeUsedTwice: Method = Method(name="NoSeffTypeUsedTwice", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_repository_BasicComponent_m_ProvideSameInterfacesAsImplementationType: Method = Method(name="ProvideSameInterfacesAsImplementationType", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_repository_BasicComponent_m_RequireSameInterfacesAsImplementationType: Method = Method(name="RequireSameInterfacesAsImplementationType", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_repository_BasicComponent.methods={pcm_repository_BasicComponent_m_NoSeffTypeUsedTwice, pcm_repository_BasicComponent_m_ProvideSameInterfacesAsImplementationType, pcm_repository_BasicComponent_m_RequireSameInterfacesAsImplementationType}

# ImplementationComponentType class attributes and methods

# ProvidesComponentType class attributes and methods

# pcm_repository_DelegationConnector class attributes and methods

# pcm_repository_CompositeComponent class attributes and methods
pcm_repository_CompositeComponent_m_ProvideSameInterfaces: Method = Method(name="ProvideSameInterfaces", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_repository_CompositeComponent_m_RequireSameInterfaces: Method = Method(name="RequireSameInterfaces", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_repository_CompositeComponent.methods={pcm_repository_CompositeComponent_m_RequireSameInterfaces, pcm_repository_CompositeComponent_m_ProvideSameInterfaces}

# entity_ComposedProvidingRequiringEntity class attributes and methods

# repository_ImplementationComponentType class attributes and methods

# CompositeDataType class attributes and methods

# InnerDeclaration class attributes and methods

# pcm_repository_InnerDeclaration class attributes and methods

# NamedElement class attributes and methods

# pcm_repository_ProvidedRole class attributes and methods

# ServiceEffectSpecification class attributes and methods

# PassiveResource class attributes and methods

# pcm_repository_PrimitiveDataType class attributes and methods
pcm_repository_PrimitiveDataType_type: Property = Property(name="type", type=StringType)
pcm_repository_PrimitiveDataType.attributes={pcm_repository_PrimitiveDataType_type}

# pcm_repository_CollectionDataType class attributes and methods

# entity_Entity class attributes and methods

# repository_DataType class attributes and methods

# pcm_repository_CompositeDataType class attributes and methods

# pcm_parameter_CharacterisedVariable class attributes and methods
pcm_parameter_CharacterisedVariable_characterisationType: Property = Property(name="characterisationType", type=StringType)
pcm_parameter_CharacterisedVariable.attributes={pcm_parameter_CharacterisedVariable_characterisationType}

# Variable class attributes and methods

# pcm_parameter_VariableUsage class attributes and methods

# VariableCharacterisation class attributes and methods

# parameter_pcm_AbstractNamedReference class attributes and methods

# pcm_seff_StopAction class attributes and methods
pcm_seff_StopAction_m_StopActionSuccessorMustNotBeDefined: Method = Method(name="StopActionSuccessorMustNotBeDefined", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_seff_StopAction.methods={pcm_seff_StopAction_m_StopActionSuccessorMustNotBeDefined}

# AbstractInternalControlFlowAction class attributes and methods

# pcm_protocol_ServiceCall class attributes and methods

# pcm_protocol_Protocol class attributes and methods
pcm_protocol_Protocol_protocolTypeID: Property = Property(name="protocolTypeID", type=StringType)
pcm_protocol_Protocol.attributes={pcm_protocol_Protocol_protocolTypeID}

# pcm_parameter_VariableCharacterisation class attributes and methods
pcm_parameter_VariableCharacterisation_type: Property = Property(name="type", type=StringType)
pcm_parameter_VariableCharacterisation.attributes={pcm_parameter_VariableCharacterisation_type}

# pcm_seff_ResourceDemandingBehaviour class attributes and methods
pcm_seff_ResourceDemandingBehaviour_m_ExactlyOneStopAction: Method = Method(name="ExactlyOneStopAction", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_seff_ResourceDemandingBehaviour_m_ExactlyOneStartAction: Method = Method(name="ExactlyOneStartAction", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_seff_ResourceDemandingBehaviour_m_EachActionExceptStartActionandStopActionMustHhaveAPredecessorAndSuccessor: Method = Method(name="EachActionExceptStartActionandStopActionMustHhaveAPredecessorAndSuccessor", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_seff_ResourceDemandingBehaviour.methods={pcm_seff_ResourceDemandingBehaviour_m_ExactlyOneStopAction, pcm_seff_ResourceDemandingBehaviour_m_EachActionExceptStartActionandStopActionMustHhaveAPredecessorAndSuccessor, pcm_seff_ResourceDemandingBehaviour_m_ExactlyOneStartAction}

# pcm_seff_AbstractInternalControlFlowAction class attributes and methods

# AbstractAction class attributes and methods

# performance_ParametricResourceDemand class attributes and methods

# pcm_seff_AbstractAction class attributes and methods

# pcm_seff_StartAction class attributes and methods
pcm_seff_StartAction_m_StartActionPredecessorMustNotBeDefined: Method = Method(name="StartActionPredecessorMustNotBeDefined", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_seff_StartAction.methods={pcm_seff_StartAction_m_StartActionPredecessorMustNotBeDefined}

# pcm_seff_ResourceDemandingSEFF class attributes and methods

# seff_ServiceEffectSpecification class attributes and methods

# seff_ResourceDemandingBehaviour class attributes and methods

# ForkedBehaviour class attributes and methods

# SynchronisationPoint class attributes and methods

# pcm_seff_ForkedBehaviour class attributes and methods

# pcm_seff_SynchronisationPoint class attributes and methods

# pcm_seff_ExternalCallAction class attributes and methods
pcm_seff_ExternalCallAction_retryCount: Property = Property(name="retryCount", type=IntegerType)
pcm_seff_ExternalCallAction.attributes={pcm_seff_ExternalCallAction_retryCount}

# pcm_seff_ReleaseAction class attributes and methods

# pcm_seff_LoopAction class attributes and methods

# AbstractLoopAction class attributes and methods

# pcm_seff_AbstractLoopAction class attributes and methods

# ResourceDemandingBehaviour class attributes and methods

# pcm_seff_InternalAction class attributes and methods
pcm_seff_InternalAction_failureProbability: Property = Property(name="failureProbability", type=FloatType)
pcm_seff_InternalAction.attributes={pcm_seff_InternalAction_failureProbability}

# pcm_seff_ForkAction class attributes and methods

# pcm_seff_AcquireAction class attributes and methods

# pcm_seff_CollectionIteratorAction class attributes and methods

# pcm_seff_GuardedBranchTransition class attributes and methods

# pcm_seff_ProbabilisticBranchTransition class attributes and methods
pcm_seff_ProbabilisticBranchTransition_branchProbability: Property = Property(name="branchProbability", type=FloatType)
pcm_seff_ProbabilisticBranchTransition.attributes={pcm_seff_ProbabilisticBranchTransition_branchProbability}

# AbstractBranchTransition class attributes and methods

# pcm_seff_AbstractBranchTransition class attributes and methods

# pcm_seff_BranchAction class attributes and methods
pcm_seff_BranchAction_m_AllProbabilisticBranchProbabilitiesMustSumUpTo1: Method = Method(name="AllProbabilisticBranchProbabilitiesMustSumUpTo1", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_seff_BranchAction_m_EitherGuardedBranchesOrProbabilisiticBranchTransitions: Method = Method(name="EitherGuardedBranchesOrProbabilisiticBranchTransitions", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_seff_BranchAction.methods={pcm_seff_BranchAction_m_AllProbabilisticBranchProbabilitiesMustSumUpTo1, pcm_seff_BranchAction_m_EitherGuardedBranchesOrProbabilisiticBranchTransitions}

# pcm_resourcetype_ResourceType class attributes and methods

# UnitCarryingElement class attributes and methods

# pcm_resourcetype_ResourceRepository class attributes and methods

# ResourceType class attributes and methods

# pcm_resourcetype_CommunicationLinkResourceType class attributes and methods

# pcm_resourcetype_ProcessingResourceType class attributes and methods

# pcm_allocation_AllocationContext class attributes and methods

# ResourceContainer class attributes and methods

# pcm_allocation_Allocation class attributes and methods
pcm_allocation_Allocation_m_EachAssemblyContextWithinSystemHasToBeAllocatedExactlyOnce: Method = Method(name="EachAssemblyContextWithinSystemHasToBeAllocatedExactlyOnce", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_allocation_Allocation.methods={pcm_allocation_Allocation_m_EachAssemblyContextWithinSystemHasToBeAllocatedExactlyOnce}

# pcm_seff_SetVariableAction class attributes and methods

# pcm_seff_ServiceEffectSpecification class attributes and methods
pcm_seff_ServiceEffectSpecification_seffTypeID: Property = Property(name="seffTypeID", type=StringType)
pcm_seff_ServiceEffectSpecification.attributes={pcm_seff_ServiceEffectSpecification_seffTypeID}

# pcm_performance_ParametricResourceDemand class attributes and methods

# ProcessingResourceType class attributes and methods

# pcm_resourceenvironment_CommunicationLinkResourceSpecification class attributes and methods
pcm_resourceenvironment_CommunicationLinkResourceSpecification_failureProbability: Property = Property(name="failureProbability", type=FloatType)
pcm_resourceenvironment_CommunicationLinkResourceSpecification.attributes={pcm_resourceenvironment_CommunicationLinkResourceSpecification_failureProbability}

# CommunicationLinkResourceType class attributes and methods

# pcm_resourceenvironment_ProcessingResourceSpecification class attributes and methods
pcm_resourceenvironment_ProcessingResourceSpecification_MTTR: Property = Property(name="MTTR", type=FloatType)
pcm_resourceenvironment_ProcessingResourceSpecification_MTTF: Property = Property(name="MTTF", type=FloatType)
pcm_resourceenvironment_ProcessingResourceSpecification_schedulingPolicy: Property = Property(name="schedulingPolicy", type=StringType)
pcm_resourceenvironment_ProcessingResourceSpecification.attributes={pcm_resourceenvironment_ProcessingResourceSpecification_schedulingPolicy, pcm_resourceenvironment_ProcessingResourceSpecification_MTTR, pcm_resourceenvironment_ProcessingResourceSpecification_MTTF}

# AllocationContext class attributes and methods

# ResourceEnvironment class attributes and methods

# System class attributes and methods

# pcm_resourceenvironment_ResourceEnvironment class attributes and methods

# LinkingResource class attributes and methods

# pcm_resourceenvironment_LinkingResource class attributes and methods

# CommunicationLinkResourceSpecification class attributes and methods

# pcm_qosannotations_SpecifiedOutputParameterAbstraction class attributes and methods

# pcm_qosannotations_QoSAnnotations class attributes and methods

# SpecifiedQoSAnnotation class attributes and methods

# SpecifiedOutputParameterAbstraction class attributes and methods

# pcm_resourceenvironment_ResourceContainer class attributes and methods

# ProcessingResourceSpecification class attributes and methods

# pcm_system_System class attributes and methods

# QoSAnnotations class attributes and methods

# pcm_qosannotations_SpecifiedQoSAnnotation class attributes and methods

# pcm_performance_SystemSpecifiedExecutionTime class attributes and methods

# pcm_performance_ComponentSpecifiedExecutionTime class attributes and methods

# pcm_reliability_SpecifiedFailureProbability class attributes and methods
pcm_reliability_SpecifiedFailureProbability_failureProbability: Property = Property(name="failureProbability", type=FloatType)
pcm_reliability_SpecifiedFailureProbability.attributes={pcm_reliability_SpecifiedFailureProbability_failureProbability}

# pcm_usagemodel_Workload class attributes and methods

# pcm_usagemodel_UsageScenario class attributes and methods

# Workload class attributes and methods

# ScenarioBehaviour class attributes and methods

# pcm_usagemodel_ScenarioBehaviour class attributes and methods
pcm_usagemodel_ScenarioBehaviour_m_Exactlyonestop: Method = Method(name="Exactlyonestop", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_usagemodel_ScenarioBehaviour_m_EachuseractionexceptStartandStopmusthaveapredecessorandsuccessor: Method = Method(name="EachuseractionexceptStartandStopmusthaveapredecessorandsuccessor", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_usagemodel_ScenarioBehaviour_m_Exactlyonestart: Method = Method(name="Exactlyonestart", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_usagemodel_ScenarioBehaviour.methods={pcm_usagemodel_ScenarioBehaviour_m_EachuseractionexceptStartandStopmusthaveapredecessorandsuccessor, pcm_usagemodel_ScenarioBehaviour_m_Exactlyonestart, pcm_usagemodel_ScenarioBehaviour_m_Exactlyonestop}

# pcm_usagemodel_Stop class attributes and methods
pcm_usagemodel_Stop_m_StopHasNoSuccessor: Method = Method(name="StopHasNoSuccessor", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_usagemodel_Stop.methods={pcm_usagemodel_Stop_m_StopHasNoSuccessor}

# pcm_usagemodel_Start class attributes and methods
pcm_usagemodel_Start_m_StartHasNoPredecessor: Method = Method(name="StartHasNoPredecessor", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_usagemodel_Start.methods={pcm_usagemodel_Start_m_StartHasNoPredecessor}

# AbstractUserAction class attributes and methods

# pcm_usagemodel_AbstractUserAction class attributes and methods

# pcm_usagemodel_UsageModel class attributes and methods

# UsageScenario class attributes and methods

# UserData class attributes and methods

# pcm_usagemodel_UserData class attributes and methods

# pcm_usagemodel_Loop class attributes and methods

# pcm_usagemodel_EntryLevelSystemCall class attributes and methods

# pcm_usagemodel_OpenWorkload class attributes and methods
pcm_usagemodel_OpenWorkload_m_InterArrivalTimeInOpenWorkloadNeedsToBeSpecified: Method = Method(name="InterArrivalTimeInOpenWorkloadNeedsToBeSpecified", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_usagemodel_OpenWorkload.methods={pcm_usagemodel_OpenWorkload_m_InterArrivalTimeInOpenWorkloadNeedsToBeSpecified}

# pcm_usagemodel_ClosedWorkload class attributes and methods
pcm_usagemodel_ClosedWorkload_population: Property = Property(name="population", type=IntegerType)
pcm_usagemodel_ClosedWorkload_m_PopulationInClosedWorkloadNeedsToBeSpecified: Method = Method(name="PopulationInClosedWorkloadNeedsToBeSpecified", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_usagemodel_ClosedWorkload_m_ThinkTimeInClosedWorkloadNeedsToBeSpecified: Method = Method(name="ThinkTimeInClosedWorkloadNeedsToBeSpecified", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_usagemodel_ClosedWorkload.attributes={pcm_usagemodel_ClosedWorkload_population}
pcm_usagemodel_ClosedWorkload.methods={pcm_usagemodel_ClosedWorkload_m_ThinkTimeInClosedWorkloadNeedsToBeSpecified, pcm_usagemodel_ClosedWorkload_m_PopulationInClosedWorkloadNeedsToBeSpecified}

# BranchTransition class attributes and methods

# pcm_usagemodel_BranchTransition class attributes and methods
pcm_usagemodel_BranchTransition_branchProbability: Property = Property(name="branchProbability", type=FloatType)
pcm_usagemodel_BranchTransition.attributes={pcm_usagemodel_BranchTransition_branchProbability}

# pcm_usagemodel_Delay class attributes and methods

# pcm_subsystem_SubSystem class attributes and methods

# repository_RepositoryComponent class attributes and methods

# pcm_usagemodel_Branch class attributes and methods
pcm_usagemodel_Branch_m_AllBranchProbabilitiesMustSumUpTo1: Method = Method(name="AllBranchProbabilitiesMustSumUpTo1", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_usagemodel_Branch.methods={pcm_usagemodel_Branch_m_AllBranchProbabilitiesMustSumUpTo1}

# Relationships
requiredRoles_InterfaceRequiringEntity1: BinaryAssociation = BinaryAssociation(
    name="requiredRoles_InterfaceRequiringEntity1",
    ends={
        Property(name="RequiredRole", type=RequiredRole, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="repository2", type=pcm_entity_InterfaceRequiringEntity, multiplicity=Multiplicity(1, 1))
    }
)
resourceRequiredRoles_ResourceInterfaceRequiringEntity3: BinaryAssociation = BinaryAssociation(
    name="resourceRequiredRoles_ResourceInterfaceRequiringEntity3",
    ends={
        Property(name="repository4", type=pcm_entity_ResourceInterfaceRequiringEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="ResourceRequiredRole", type=ResourceRequiredRole, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
providedRoles_InterfaceProvidingEntity0: BinaryAssociation = BinaryAssociation(
    name="providedRoles_InterfaceProvidingEntity0",
    ends={
        Property(name="repository", type=pcm_entity_InterfaceProvidingEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="ProvidedRole", type=ProvidedRole, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
encapsulatedComponent_AssemblyContext13: BinaryAssociation = BinaryAssociation(
    name="encapsulatedComponent_AssemblyContext13",
    ends={
        Property(name="RepositoryComponent", type=pcm_composition_AssemblyContext, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_composition_AssemblyContext", type=RepositoryComponent, multiplicity=Multiplicity(1, 1))
    }
)
parentStructure_AssemblyContext14: BinaryAssociation = BinaryAssociation(
    name="parentStructure_AssemblyContext14",
    ends={
        Property(name="core16", type=pcm_composition_AssemblyContext, multiplicity=Multiplicity(1, 1)),
        Property(name="composition15", type=composition_ComposedStructure, multiplicity=Multiplicity(1, 1))
    }
)
configParameterUsages_AssemblyContext17: BinaryAssociation = BinaryAssociation(
    name="configParameterUsages_AssemblyContext17",
    ends={
        Property(name="VariableUsage", type=pcm_composition_AssemblyContext, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_composition_AssemblyContext18", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
innerProvidedRole_ProvidedDelegationConnector5: BinaryAssociation = BinaryAssociation(
    name="innerProvidedRole_ProvidedDelegationConnector5",
    ends={
        Property(name="ProvidedRole6", type=pcm_composition_ProvidedDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_composition_ProvidedDelegationConnector", type=ProvidedRole, multiplicity=Multiplicity(1, 1))
    }
)
outerProvidedRole_ProvidedDelegationConnector7: BinaryAssociation = BinaryAssociation(
    name="outerProvidedRole_ProvidedDelegationConnector7",
    ends={
        Property(name="ProvidedRole9", type=pcm_composition_ProvidedDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_composition_ProvidedDelegationConnector8", type=ProvidedRole, multiplicity=Multiplicity(1, 1))
    }
)
assemblyContext_ProvidedDelegationConnector10: BinaryAssociation = BinaryAssociation(
    name="assemblyContext_ProvidedDelegationConnector10",
    ends={
        Property(name="composition_AssemblyContext", type=pcm_composition_ProvidedDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_composition_ProvidedDelegationConnector11", type=composition_AssemblyContext, multiplicity=Multiplicity(1, 1))
    }
)
parentStructure_ProvidedDelegationConnector12: BinaryAssociation = BinaryAssociation(
    name="parentStructure_ProvidedDelegationConnector12",
    ends={
        Property(name="core", type=pcm_composition_ProvidedDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="composition", type=composition_ComposedStructure, multiplicity=Multiplicity(1, 1))
    }
)
innerRequiredRole_RequiredDelegationConnector19: BinaryAssociation = BinaryAssociation(
    name="innerRequiredRole_RequiredDelegationConnector19",
    ends={
        Property(name="RequiredRole20", type=pcm_composition_RequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_composition_RequiredDelegationConnector", type=RequiredRole, multiplicity=Multiplicity(1, 1))
    }
)
outerRequiredRole_RequiredDelegationConnector21: BinaryAssociation = BinaryAssociation(
    name="outerRequiredRole_RequiredDelegationConnector21",
    ends={
        Property(name="RequiredRole23", type=pcm_composition_RequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_composition_RequiredDelegationConnector22", type=RequiredRole, multiplicity=Multiplicity(1, 1))
    }
)
assemblyContext_RequiredDelegationConnector24: BinaryAssociation = BinaryAssociation(
    name="assemblyContext_RequiredDelegationConnector24",
    ends={
        Property(name="composition_AssemblyContext26", type=pcm_composition_RequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_composition_RequiredDelegationConnector25", type=composition_AssemblyContext, multiplicity=Multiplicity(1, 1))
    }
)
parentStructure_RequiredDelegationConnector27: BinaryAssociation = BinaryAssociation(
    name="parentStructure_RequiredDelegationConnector27",
    ends={
        Property(name="core29", type=pcm_composition_RequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="composition28", type=composition_ComposedStructure, multiplicity=Multiplicity(1, 1))
    }
)
parentStructure_ResourceRequiredDelegationConnector44: BinaryAssociation = BinaryAssociation(
    name="parentStructure_ResourceRequiredDelegationConnector44",
    ends={
        Property(name="core46", type=pcm_composition_ResourceRequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="composition45", type=composition_ComposedStructure, multiplicity=Multiplicity(1, 1))
    }
)
innerResourceRequiredRole_ResourceRequiredDelegationConnector47: BinaryAssociation = BinaryAssociation(
    name="innerResourceRequiredRole_ResourceRequiredDelegationConnector47",
    ends={
        Property(name="ResourceRequiredRole48", type=pcm_composition_ResourceRequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_composition_ResourceRequiredDelegationConnector", type=ResourceRequiredRole, multiplicity=Multiplicity(1, 1))
    }
)
outerResourceRequiredRole_ResourceRequiredDelegationConnector49: BinaryAssociation = BinaryAssociation(
    name="outerResourceRequiredRole_ResourceRequiredDelegationConnector49",
    ends={
        Property(name="ResourceRequiredRole51", type=pcm_composition_ResourceRequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_composition_ResourceRequiredDelegationConnector50", type=ResourceRequiredRole, multiplicity=Multiplicity(1, 1))
    }
)
assemblyContexts_ComposedStructure52: BinaryAssociation = BinaryAssociation(
    name="assemblyContexts_ComposedStructure52",
    ends={
        Property(name="core54", type=pcm_composition_ComposedStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="composition53", type=composition_AssemblyContext, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
providedDelegationConnectors_ComposedStructure55: BinaryAssociation = BinaryAssociation(
    name="providedDelegationConnectors_ComposedStructure55",
    ends={
        Property(name="core57", type=pcm_composition_ComposedStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="composition56", type=composition_ProvidedDelegationConnector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiringAssemblyContext_AssemblyConnector30: BinaryAssociation = BinaryAssociation(
    name="requiringAssemblyContext_AssemblyConnector30",
    ends={
        Property(name="composition_AssemblyContext31", type=pcm_composition_AssemblyConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_composition_AssemblyConnector", type=composition_AssemblyContext, multiplicity=Multiplicity(1, 1))
    }
)
providingAssemblyContext_AssemblyConnector32: BinaryAssociation = BinaryAssociation(
    name="providingAssemblyContext_AssemblyConnector32",
    ends={
        Property(name="composition_AssemblyContext34", type=pcm_composition_AssemblyConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_composition_AssemblyConnector33", type=composition_AssemblyContext, multiplicity=Multiplicity(1, 1))
    }
)
providedRole_AssemblyConnector35: BinaryAssociation = BinaryAssociation(
    name="providedRole_AssemblyConnector35",
    ends={
        Property(name="ProvidedRole37", type=pcm_composition_AssemblyConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_composition_AssemblyConnector36", type=ProvidedRole, multiplicity=Multiplicity(1, 1))
    }
)
requiredRole_AssemblyConnector38: BinaryAssociation = BinaryAssociation(
    name="requiredRole_AssemblyConnector38",
    ends={
        Property(name="RequiredRole40", type=pcm_composition_AssemblyConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_composition_AssemblyConnector39", type=RequiredRole, multiplicity=Multiplicity(1, 1))
    }
)
parentStructure_AssemblyConnector41: BinaryAssociation = BinaryAssociation(
    name="parentStructure_AssemblyConnector41",
    ends={
        Property(name="core43", type=pcm_composition_AssemblyConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="composition42", type=composition_ComposedStructure, multiplicity=Multiplicity(1, 1))
    }
)
parameters__Signature68: BinaryAssociation = BinaryAssociation(
    name="parameters__Signature68",
    ends={
        Property(name="repository69", type=pcm_repository_Signature, multiplicity=Multiplicity(1, 1)),
        Property(name="Parameter", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
interface_Signature70: BinaryAssociation = BinaryAssociation(
    name="interface_Signature70",
    ends={
        Property(name="repository71", type=pcm_repository_Signature, multiplicity=Multiplicity(1, 1)),
        Property(name="Interface", type=Interface, multiplicity=Multiplicity(1, 1))
    }
)
returntype__Signature72: BinaryAssociation = BinaryAssociation(
    name="returntype__Signature72",
    ends={
        Property(name="DataType", type=pcm_repository_Signature, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_repository_Signature", type=DataType, multiplicity=Multiplicity(0, 1))
    }
)
requiredDelegationConnectors_ComposedStructure58: BinaryAssociation = BinaryAssociation(
    name="requiredDelegationConnectors_ComposedStructure58",
    ends={
        Property(name="core60", type=pcm_composition_ComposedStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="composition59", type=composition_RequiredDelegationConnector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
assemblyConnectors_ComposedStructure61: BinaryAssociation = BinaryAssociation(
    name="assemblyConnectors_ComposedStructure61",
    ends={
        Property(name="core63", type=pcm_composition_ComposedStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="composition62", type=composition_AssemblyConnector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceRequiredDelegationConnectors_ComposedStructure64: BinaryAssociation = BinaryAssociation(
    name="resourceRequiredDelegationConnectors_ComposedStructure64",
    ends={
        Property(name="core66", type=pcm_composition_ComposedStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="composition65", type=composition_ResourceRequiredDelegationConnector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
capacity_PassiveResource67: BinaryAssociation = BinaryAssociation(
    name="capacity_PassiveResource67",
    ends={
        Property(name="PCMRandomVariable", type=pcm_repository_PassiveResource, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_repository_PassiveResource", type=PCMRandomVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
components__Repository81: BinaryAssociation = BinaryAssociation(
    name="components__Repository81",
    ends={
        Property(name="repository83", type=pcm_repository_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="RepositoryComponent82", type=RepositoryComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
interfaces__Repository84: BinaryAssociation = BinaryAssociation(
    name="interfaces__Repository84",
    ends={
        Property(name="repository86", type=pcm_repository_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="Interface85", type=Interface, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
datatypes_Repository87: BinaryAssociation = BinaryAssociation(
    name="datatypes_Repository87",
    ends={
        Property(name="repository89", type=pcm_repository_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="DataType88", type=DataType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
repository_RepositoryComponent90: BinaryAssociation = BinaryAssociation(
    name="repository_RepositoryComponent90",
    ends={
        Property(name="repository92", type=pcm_repository_RepositoryComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="Repository91", type=Repository, multiplicity=Multiplicity(1, 1))
    }
)
exceptions__Signature73: BinaryAssociation = BinaryAssociation(
    name="exceptions__Signature73",
    ends={
        Property(name="ExceptionType", type=pcm_repository_Signature, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_repository_Signature74", type=ExceptionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
datatype__Parameter75: BinaryAssociation = BinaryAssociation(
    name="datatype__Parameter75",
    ends={
        Property(name="DataType76", type=pcm_repository_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_repository_Parameter", type=DataType, multiplicity=Multiplicity(1, 1))
    }
)
signature_Parameter77: BinaryAssociation = BinaryAssociation(
    name="signature_Parameter77",
    ends={
        Property(name="repository78", type=pcm_repository_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="Signature", type=Signature, multiplicity=Multiplicity(1, 1))
    }
)
repository_DataType79: BinaryAssociation = BinaryAssociation(
    name="repository_DataType79",
    ends={
        Property(name="repository80", type=pcm_repository_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="Repository", type=Repository, multiplicity=Multiplicity(1, 1))
    }
)
ancestorInterfaces_Interface99: BinaryAssociation = BinaryAssociation(
    name="ancestorInterfaces_Interface99",
    ends={
        Property(name="Interface101", type=pcm_repository_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_repository_Interface100", type=Interface, multiplicity=Multiplicity(0, 9999))
    }
)
protocols__Interface102: BinaryAssociation = BinaryAssociation(
    name="protocols__Interface102",
    ends={
        Property(name="Protocol", type=pcm_repository_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_repository_Interface103", type=Protocol, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
signatures__Interface104: BinaryAssociation = BinaryAssociation(
    name="signatures__Interface104",
    ends={
        Property(name="repository106", type=pcm_repository_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="Signature105", type=Signature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
repository_Interface107: BinaryAssociation = BinaryAssociation(
    name="repository_Interface107",
    ends={
        Property(name="repository109", type=pcm_repository_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="Repository108", type=Repository, multiplicity=Multiplicity(1, 1))
    }
)
requiredInterface_ResourceRequiredRole110: BinaryAssociation = BinaryAssociation(
    name="requiredInterface_ResourceRequiredRole110",
    ends={
        Property(name="Interface111", type=pcm_repository_ResourceRequiredRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_repository_ResourceRequiredRole", type=Interface, multiplicity=Multiplicity(1, 1))
    }
)
requiredInterface__RequiredRole93: BinaryAssociation = BinaryAssociation(
    name="requiredInterface__RequiredRole93",
    ends={
        Property(name="Interface94", type=pcm_repository_RequiredRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_repository_RequiredRole", type=Interface, multiplicity=Multiplicity(1, 1))
    }
)
requiringEntity_RequiredRole95: BinaryAssociation = BinaryAssociation(
    name="requiringEntity_RequiredRole95",
    ends={
        Property(name="core96", type=pcm_repository_RequiredRole, multiplicity=Multiplicity(1, 1)),
        Property(name="entity", type=entity_InterfaceRequiringEntity, multiplicity=Multiplicity(1, 1))
    }
)
parentInterface__Interface97: BinaryAssociation = BinaryAssociation(
    name="parentInterface__Interface97",
    ends={
        Property(name="Interface98", type=pcm_repository_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_repository_Interface", type=Interface, multiplicity=Multiplicity(0, 9999))
    }
)
parentCompleteComponentTypes115: BinaryAssociation = BinaryAssociation(
    name="parentCompleteComponentTypes115",
    ends={
        Property(name="CompleteComponentType", type=pcm_repository_ImplementationComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_repository_ImplementationComponentType", type=CompleteComponentType, multiplicity=Multiplicity(0, 9999))
    }
)
componentParameterUsage_ImplementationComponentType116: BinaryAssociation = BinaryAssociation(
    name="componentParameterUsage_ImplementationComponentType116",
    ends={
        Property(name="VariableUsage118", type=pcm_repository_ImplementationComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_repository_ImplementationComponentType117", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceRequiringEntity_ResourceRequiredRole112: BinaryAssociation = BinaryAssociation(
    name="resourceRequiringEntity_ResourceRequiredRole112",
    ends={
        Property(name="core114", type=pcm_repository_ResourceRequiredRole, multiplicity=Multiplicity(1, 1)),
        Property(name="entity113", type=entity_ResourceInterfaceRequiringEntity, multiplicity=Multiplicity(1, 1))
    }
)
parentProvidesComponentTypes119: BinaryAssociation = BinaryAssociation(
    name="parentProvidesComponentTypes119",
    ends={
        Property(name="ProvidesComponentType", type=pcm_repository_CompleteComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_repository_CompleteComponentType", type=ProvidesComponentType, multiplicity=Multiplicity(0, 9999))
    }
)
parentType_CompositeDataType125: BinaryAssociation = BinaryAssociation(
    name="parentType_CompositeDataType125",
    ends={
        Property(name="CompositeDataType", type=pcm_repository_CompositeDataType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_repository_CompositeDataType", type=CompositeDataType, multiplicity=Multiplicity(0, 9999))
    }
)
innerDeclaration_CompositeDataType126: BinaryAssociation = BinaryAssociation(
    name="innerDeclaration_CompositeDataType126",
    ends={
        Property(name="InnerDeclaration", type=pcm_repository_CompositeDataType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_repository_CompositeDataType127", type=InnerDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
datatype_InnerDeclaration128: BinaryAssociation = BinaryAssociation(
    name="datatype_InnerDeclaration128",
    ends={
        Property(name="DataType129", type=pcm_repository_InnerDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_repository_InnerDeclaration", type=DataType, multiplicity=Multiplicity(1, 1))
    }
)
providedInterface__ProvidedRole130: BinaryAssociation = BinaryAssociation(
    name="providedInterface__ProvidedRole130",
    ends={
        Property(name="Interface131", type=pcm_repository_ProvidedRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_repository_ProvidedRole", type=Interface, multiplicity=Multiplicity(1, 1))
    }
)
serviceEffectSpecifications__BasicComponent120: BinaryAssociation = BinaryAssociation(
    name="serviceEffectSpecifications__BasicComponent120",
    ends={
        Property(name="ServiceEffectSpecification", type=pcm_repository_BasicComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_repository_BasicComponent", type=ServiceEffectSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
passiveResource_BasicComponent121: BinaryAssociation = BinaryAssociation(
    name="passiveResource_BasicComponent121",
    ends={
        Property(name="PassiveResource", type=pcm_repository_BasicComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_repository_BasicComponent122", type=PassiveResource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
innerType_CollectionDataType123: BinaryAssociation = BinaryAssociation(
    name="innerType_CollectionDataType123",
    ends={
        Property(name="DataType124", type=pcm_repository_CollectionDataType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_repository_CollectionDataType", type=DataType, multiplicity=Multiplicity(1, 1))
    }
)
variableCharacterisation_VariableUsage139: BinaryAssociation = BinaryAssociation(
    name="variableCharacterisation_VariableUsage139",
    ends={
        Property(name="VariableCharacterisation", type=pcm_parameter_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_parameter_VariableUsage", type=VariableCharacterisation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
namedReference_VariableUsage140: BinaryAssociation = BinaryAssociation(
    name="namedReference_VariableUsage140",
    ends={
        Property(name="parameter_pcm_AbstractNamedReference", type=pcm_parameter_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_parameter_VariableUsage141", type=parameter_pcm_AbstractNamedReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
providingEntity_ProvidedRole132: BinaryAssociation = BinaryAssociation(
    name="providingEntity_ProvidedRole132",
    ends={
        Property(name="core134", type=pcm_repository_ProvidedRole, multiplicity=Multiplicity(1, 1)),
        Property(name="entity133", type=entity_InterfaceProvidingEntity, multiplicity=Multiplicity(1, 1))
    }
)
signature__ServiceCall135: BinaryAssociation = BinaryAssociation(
    name="signature__ServiceCall135",
    ends={
        Property(name="Signature136", type=pcm_protocol_ServiceCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_protocol_ServiceCall", type=Signature, multiplicity=Multiplicity(1, 1))
    }
)
specification_VariableCharacterisation137: BinaryAssociation = BinaryAssociation(
    name="specification_VariableCharacterisation137",
    ends={
        Property(name="PCMRandomVariable138", type=pcm_parameter_VariableCharacterisation, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_parameter_VariableCharacterisation", type=PCMRandomVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
resourceDemand_Action142: BinaryAssociation = BinaryAssociation(
    name="resourceDemand_Action142",
    ends={
        Property(name="seff", type=pcm_seff_AbstractInternalControlFlowAction, multiplicity=Multiplicity(1, 1)),
        Property(name="performance", type=performance_ParametricResourceDemand, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
predecessor_AbstractAction143: BinaryAssociation = BinaryAssociation(
    name="predecessor_AbstractAction143",
    ends={
        Property(name="seff144", type=pcm_seff_AbstractAction, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractAction", type=AbstractAction, multiplicity=Multiplicity(0, 1))
    }
)
successor_AbstractAction145: BinaryAssociation = BinaryAssociation(
    name="successor_AbstractAction145",
    ends={
        Property(name="seff147", type=pcm_seff_AbstractAction, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractAction146", type=AbstractAction, multiplicity=Multiplicity(0, 1))
    }
)
asynchronousForkedBehaviours_ForkAction155: BinaryAssociation = BinaryAssociation(
    name="asynchronousForkedBehaviours_ForkAction155",
    ends={
        Property(name="ForkedBehaviour", type=pcm_seff_ForkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_seff_ForkAction", type=ForkedBehaviour, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
synchronisingBehaviours_ForkAction156: BinaryAssociation = BinaryAssociation(
    name="synchronisingBehaviours_ForkAction156",
    ends={
        Property(name="SynchronisationPoint", type=pcm_seff_ForkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_seff_ForkAction157", type=SynchronisationPoint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
synchronousForkedBehaviours_SynchronisationPoint158: BinaryAssociation = BinaryAssociation(
    name="synchronousForkedBehaviours_SynchronisationPoint158",
    ends={
        Property(name="ForkedBehaviour159", type=pcm_seff_SynchronisationPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_seff_SynchronisationPoint", type=ForkedBehaviour, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
outputParameterUsage_SynchronisationPoint160: BinaryAssociation = BinaryAssociation(
    name="outputParameterUsage_SynchronisationPoint160",
    ends={
        Property(name="VariableUsage162", type=pcm_seff_SynchronisationPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_seff_SynchronisationPoint161", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
calledService_ExternalService163: BinaryAssociation = BinaryAssociation(
    name="calledService_ExternalService163",
    ends={
        Property(name="Signature164", type=pcm_seff_ExternalCallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_seff_ExternalCallAction", type=Signature, multiplicity=Multiplicity(1, 1))
    }
)
inputParameterUsages_ExternalCallAction165: BinaryAssociation = BinaryAssociation(
    name="inputParameterUsages_ExternalCallAction165",
    ends={
        Property(name="VariableUsage167", type=pcm_seff_ExternalCallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_seff_ExternalCallAction166", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputVariableUsages_ExternalCallAction168: BinaryAssociation = BinaryAssociation(
    name="outputVariableUsages_ExternalCallAction168",
    ends={
        Property(name="VariableUsage170", type=pcm_seff_ExternalCallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_seff_ExternalCallAction169", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
steps_Behaviour148: BinaryAssociation = BinaryAssociation(
    name="steps_Behaviour148",
    ends={
        Property(name="AbstractAction149", type=pcm_seff_ResourceDemandingBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_seff_ResourceDemandingBehaviour", type=AbstractAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
passiveResource_ReleaseAction150: BinaryAssociation = BinaryAssociation(
    name="passiveResource_ReleaseAction150",
    ends={
        Property(name="PassiveResource151", type=pcm_seff_ReleaseAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_seff_ReleaseAction", type=PassiveResource, multiplicity=Multiplicity(1, 1))
    }
)
iterationCount_LoopAction152: BinaryAssociation = BinaryAssociation(
    name="iterationCount_LoopAction152",
    ends={
        Property(name="PCMRandomVariable153", type=pcm_seff_LoopAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_seff_LoopAction", type=PCMRandomVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
bodyBehaviour_Loop154: BinaryAssociation = BinaryAssociation(
    name="bodyBehaviour_Loop154",
    ends={
        Property(name="ResourceDemandingBehaviour", type=pcm_seff_AbstractLoopAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_seff_AbstractLoopAction", type=ResourceDemandingBehaviour, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
branches_Branch175: BinaryAssociation = BinaryAssociation(
    name="branches_Branch175",
    ends={
        Property(name="AbstractBranchTransition", type=pcm_seff_BranchAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_seff_BranchAction", type=AbstractBranchTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
passiveresource_AcquireAction176: BinaryAssociation = BinaryAssociation(
    name="passiveresource_AcquireAction176",
    ends={
        Property(name="PassiveResource177", type=pcm_seff_AcquireAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_seff_AcquireAction", type=PassiveResource, multiplicity=Multiplicity(1, 1))
    }
)
parameter_CollectionIteratorAction178: BinaryAssociation = BinaryAssociation(
    name="parameter_CollectionIteratorAction178",
    ends={
        Property(name="Parameter179", type=pcm_seff_CollectionIteratorAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_seff_CollectionIteratorAction", type=Parameter_, multiplicity=Multiplicity(1, 1))
    }
)
role_ExternalService171: BinaryAssociation = BinaryAssociation(
    name="role_ExternalService171",
    ends={
        Property(name="Role", type=pcm_seff_ExternalCallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_seff_ExternalCallAction172", type=Role, multiplicity=Multiplicity(1, 1))
    }
)
branchBehaviour_BranchTransition173: BinaryAssociation = BinaryAssociation(
    name="branchBehaviour_BranchTransition173",
    ends={
        Property(name="ResourceDemandingBehaviour174", type=pcm_seff_AbstractBranchTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_seff_AbstractBranchTransition", type=ResourceDemandingBehaviour, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
availableResourceTypes_ResourceRepository192: BinaryAssociation = BinaryAssociation(
    name="availableResourceTypes_ResourceRepository192",
    ends={
        Property(name="ResourceType", type=pcm_resourcetype_ResourceRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_resourcetype_ResourceRepository", type=ResourceType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceContainer_AllocationContext193: BinaryAssociation = BinaryAssociation(
    name="resourceContainer_AllocationContext193",
    ends={
        Property(name="ResourceContainer", type=pcm_allocation_AllocationContext, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_allocation_AllocationContext", type=ResourceContainer, multiplicity=Multiplicity(1, 1))
    }
)
assemblyContext_AllocationContext194: BinaryAssociation = BinaryAssociation(
    name="assemblyContext_AllocationContext194",
    ends={
        Property(name="composition_AssemblyContext196", type=pcm_allocation_AllocationContext, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_allocation_AllocationContext195", type=composition_AssemblyContext, multiplicity=Multiplicity(1, 1))
    }
)
branchCondition_GuardedBranchTransition180: BinaryAssociation = BinaryAssociation(
    name="branchCondition_GuardedBranchTransition180",
    ends={
        Property(name="PCMRandomVariable181", type=pcm_seff_GuardedBranchTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_seff_GuardedBranchTransition", type=PCMRandomVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
localVariableUsages_SetVariableAction182: BinaryAssociation = BinaryAssociation(
    name="localVariableUsages_SetVariableAction182",
    ends={
        Property(name="VariableUsage183", type=pcm_seff_SetVariableAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_seff_SetVariableAction", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
describedService__SEFF184: BinaryAssociation = BinaryAssociation(
    name="describedService__SEFF184",
    ends={
        Property(name="Signature185", type=pcm_seff_ServiceEffectSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_seff_ServiceEffectSpecification", type=Signature, multiplicity=Multiplicity(1, 1))
    }
)
specification_ParametericResourceDemand186: BinaryAssociation = BinaryAssociation(
    name="specification_ParametericResourceDemand186",
    ends={
        Property(name="PCMRandomVariable187", type=pcm_performance_ParametricResourceDemand, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_performance_ParametricResourceDemand", type=PCMRandomVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
requiredResource_ParametricResourceDemand188: BinaryAssociation = BinaryAssociation(
    name="requiredResource_ParametricResourceDemand188",
    ends={
        Property(name="ProcessingResourceType", type=pcm_performance_ParametricResourceDemand, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_performance_ParametricResourceDemand189", type=ProcessingResourceType, multiplicity=Multiplicity(1, 1))
    }
)
action_ParametricResourceDemand190: BinaryAssociation = BinaryAssociation(
    name="action_ParametricResourceDemand190",
    ends={
        Property(name="seff191", type=pcm_performance_ParametricResourceDemand, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractInternalControlFlowAction", type=AbstractInternalControlFlowAction, multiplicity=Multiplicity(1, 1))
    }
)
communicationLinkResourceType_CommunicationLinkResourceSpecification213: BinaryAssociation = BinaryAssociation(
    name="communicationLinkResourceType_CommunicationLinkResourceSpecification213",
    ends={
        Property(name="CommunicationLinkResourceType", type=pcm_resourceenvironment_CommunicationLinkResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_resourceenvironment_CommunicationLinkResourceSpecification", type=CommunicationLinkResourceType, multiplicity=Multiplicity(1, 1))
    }
)
latency_CommunicationLinkResourceSpecification214: BinaryAssociation = BinaryAssociation(
    name="latency_CommunicationLinkResourceSpecification214",
    ends={
        Property(name="PCMRandomVariable216", type=pcm_resourceenvironment_CommunicationLinkResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_resourceenvironment_CommunicationLinkResourceSpecification215", type=PCMRandomVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
throughput_CommunicationLinkResourceSpecification217: BinaryAssociation = BinaryAssociation(
    name="throughput_CommunicationLinkResourceSpecification217",
    ends={
        Property(name="PCMRandomVariable219", type=pcm_resourceenvironment_CommunicationLinkResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_resourceenvironment_CommunicationLinkResourceSpecification218", type=PCMRandomVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
allocationContexts_Allocation197: BinaryAssociation = BinaryAssociation(
    name="allocationContexts_Allocation197",
    ends={
        Property(name="AllocationContext", type=pcm_allocation_Allocation, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_allocation_Allocation", type=AllocationContext, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
targetResourceEnvironment_Allocation198: BinaryAssociation = BinaryAssociation(
    name="targetResourceEnvironment_Allocation198",
    ends={
        Property(name="ResourceEnvironment", type=pcm_allocation_Allocation, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_allocation_Allocation199", type=ResourceEnvironment, multiplicity=Multiplicity(0, 1))
    }
)
system_Allocation200: BinaryAssociation = BinaryAssociation(
    name="system_Allocation200",
    ends={
        Property(name="System", type=pcm_allocation_Allocation, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_allocation_Allocation201", type=System, multiplicity=Multiplicity(1, 1))
    }
)
linkingresource202: BinaryAssociation = BinaryAssociation(
    name="linkingresource202",
    ends={
        Property(name="LinkingResource", type=pcm_resourceenvironment_ResourceEnvironment, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_resourceenvironment_ResourceEnvironment", type=LinkingResource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceContainer_ResourceEnvironment203: BinaryAssociation = BinaryAssociation(
    name="resourceContainer_ResourceEnvironment203",
    ends={
        Property(name="ResourceContainer205", type=pcm_resourceenvironment_ResourceEnvironment, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_resourceenvironment_ResourceEnvironment204", type=ResourceContainer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
toResourceContainer_LinkingResource206: BinaryAssociation = BinaryAssociation(
    name="toResourceContainer_LinkingResource206",
    ends={
        Property(name="ResourceContainer207", type=pcm_resourceenvironment_LinkingResource, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_resourceenvironment_LinkingResource", type=ResourceContainer, multiplicity=Multiplicity(0, 9999))
    }
)
fromResourceContainer_LinkingResource208: BinaryAssociation = BinaryAssociation(
    name="fromResourceContainer_LinkingResource208",
    ends={
        Property(name="ResourceContainer210", type=pcm_resourceenvironment_LinkingResource, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_resourceenvironment_LinkingResource209", type=ResourceContainer, multiplicity=Multiplicity(0, 9999))
    }
)
communicationLinkResourceSpecifications_LinkingResource211: BinaryAssociation = BinaryAssociation(
    name="communicationLinkResourceSpecifications_LinkingResource211",
    ends={
        Property(name="CommunicationLinkResourceSpecification", type=pcm_resourceenvironment_LinkingResource, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_resourceenvironment_LinkingResource212", type=CommunicationLinkResourceSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
role_SpecifiedQoSAnnotation229: BinaryAssociation = BinaryAssociation(
    name="role_SpecifiedQoSAnnotation229",
    ends={
        Property(name="Role231", type=pcm_qosannotations_SpecifiedQoSAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_qosannotations_SpecifiedQoSAnnotation230", type=Role, multiplicity=Multiplicity(1, 1))
    }
)
specification_SpecifiedExecutionTime232: BinaryAssociation = BinaryAssociation(
    name="specification_SpecifiedExecutionTime232",
    ends={
        Property(name="PCMRandomVariable234", type=pcm_qosannotations_SpecifiedQoSAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_qosannotations_SpecifiedQoSAnnotation233", type=PCMRandomVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
signature_SpecifiedOutputParameterAbstraction235: BinaryAssociation = BinaryAssociation(
    name="signature_SpecifiedOutputParameterAbstraction235",
    ends={
        Property(name="Signature236", type=pcm_qosannotations_SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_qosannotations_SpecifiedOutputParameterAbstraction", type=Signature, multiplicity=Multiplicity(1, 1))
    }
)
role_SpecifiedOutputParameterAbstraction237: BinaryAssociation = BinaryAssociation(
    name="role_SpecifiedOutputParameterAbstraction237",
    ends={
        Property(name="Role239", type=pcm_qosannotations_SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_qosannotations_SpecifiedOutputParameterAbstraction238", type=Role, multiplicity=Multiplicity(1, 1))
    }
)
expectedExternalOutputs_SpecifiedOutputParameterAbstraction240: BinaryAssociation = BinaryAssociation(
    name="expectedExternalOutputs_SpecifiedOutputParameterAbstraction240",
    ends={
        Property(name="VariableUsage242", type=pcm_qosannotations_SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_qosannotations_SpecifiedOutputParameterAbstraction241", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specifiedQoSAnnotations_QoSAnnotations243: BinaryAssociation = BinaryAssociation(
    name="specifiedQoSAnnotations_QoSAnnotations243",
    ends={
        Property(name="SpecifiedQoSAnnotation", type=pcm_qosannotations_QoSAnnotations, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_qosannotations_QoSAnnotations", type=SpecifiedQoSAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
activeResourceType_ActiveResourceSpecification220: BinaryAssociation = BinaryAssociation(
    name="activeResourceType_ActiveResourceSpecification220",
    ends={
        Property(name="ProcessingResourceType221", type=pcm_resourceenvironment_ProcessingResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_resourceenvironment_ProcessingResourceSpecification", type=ProcessingResourceType, multiplicity=Multiplicity(1, 1))
    }
)
processingRate_ProcessingResourceSpecification222: BinaryAssociation = BinaryAssociation(
    name="processingRate_ProcessingResourceSpecification222",
    ends={
        Property(name="PCMRandomVariable224", type=pcm_resourceenvironment_ProcessingResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_resourceenvironment_ProcessingResourceSpecification223", type=PCMRandomVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
activeResourceSpecifications_ResourceContainer225: BinaryAssociation = BinaryAssociation(
    name="activeResourceSpecifications_ResourceContainer225",
    ends={
        Property(name="ProcessingResourceSpecification", type=pcm_resourceenvironment_ResourceContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_resourceenvironment_ResourceContainer", type=ProcessingResourceSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
qosAnnotations_System226: BinaryAssociation = BinaryAssociation(
    name="qosAnnotations_System226",
    ends={
        Property(name="QoSAnnotations", type=pcm_system_System, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_system_System", type=QoSAnnotations, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
signature_SpecifiedQoSAnnation227: BinaryAssociation = BinaryAssociation(
    name="signature_SpecifiedQoSAnnation227",
    ends={
        Property(name="Signature228", type=pcm_qosannotations_SpecifiedQoSAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_qosannotations_SpecifiedQoSAnnotation", type=Signature, multiplicity=Multiplicity(1, 1))
    }
)
specifiedOutputParameterAbstractions_QoSAnnotations244: BinaryAssociation = BinaryAssociation(
    name="specifiedOutputParameterAbstractions_QoSAnnotations244",
    ends={
        Property(name="SpecifiedOutputParameterAbstraction", type=pcm_qosannotations_QoSAnnotations, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_qosannotations_QoSAnnotations245", type=SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
assemblyContext_ComponentSpecifiedExecutionTime246: BinaryAssociation = BinaryAssociation(
    name="assemblyContext_ComponentSpecifiedExecutionTime246",
    ends={
        Property(name="composition_AssemblyContext247", type=pcm_performance_ComponentSpecifiedExecutionTime, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_performance_ComponentSpecifiedExecutionTime", type=composition_AssemblyContext, multiplicity=Multiplicity(1, 1))
    }
)
workload_UsageScenario248: BinaryAssociation = BinaryAssociation(
    name="workload_UsageScenario248",
    ends={
        Property(name="Workload", type=pcm_usagemodel_UsageScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_usagemodel_UsageScenario", type=Workload, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
scenarioBehaviour_UsageScenario249: BinaryAssociation = BinaryAssociation(
    name="scenarioBehaviour_UsageScenario249",
    ends={
        Property(name="ScenarioBehaviour", type=pcm_usagemodel_UsageScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_usagemodel_UsageScenario250", type=ScenarioBehaviour, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
userDataParameterUsages_UserData260: BinaryAssociation = BinaryAssociation(
    name="userDataParameterUsages_UserData260",
    ends={
        Property(name="VariableUsage261", type=pcm_usagemodel_UserData, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_usagemodel_UserData", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
assemblyContext_userData262: BinaryAssociation = BinaryAssociation(
    name="assemblyContext_userData262",
    ends={
        Property(name="composition_AssemblyContext264", type=pcm_usagemodel_UserData, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_usagemodel_UserData263", type=composition_AssemblyContext, multiplicity=Multiplicity(1, 1))
    }
)
actions_ScenarioBehaviour251: BinaryAssociation = BinaryAssociation(
    name="actions_ScenarioBehaviour251",
    ends={
        Property(name="AbstractUserAction", type=pcm_usagemodel_ScenarioBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_usagemodel_ScenarioBehaviour", type=AbstractUserAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
successor252: BinaryAssociation = BinaryAssociation(
    name="successor252",
    ends={
        Property(name="usagemodel", type=pcm_usagemodel_AbstractUserAction, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractUserAction253", type=AbstractUserAction, multiplicity=Multiplicity(0, 1))
    }
)
predecessor254: BinaryAssociation = BinaryAssociation(
    name="predecessor254",
    ends={
        Property(name="usagemodel256", type=pcm_usagemodel_AbstractUserAction, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractUserAction255", type=AbstractUserAction, multiplicity=Multiplicity(0, 1))
    }
)
usageScenario_UsageModel257: BinaryAssociation = BinaryAssociation(
    name="usageScenario_UsageModel257",
    ends={
        Property(name="UsageScenario", type=pcm_usagemodel_UsageModel, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_usagemodel_UsageModel", type=UsageScenario, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
userData_UsageModel258: BinaryAssociation = BinaryAssociation(
    name="userData_UsageModel258",
    ends={
        Property(name="UserData", type=pcm_usagemodel_UsageModel, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_usagemodel_UsageModel259", type=UserData, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
interArrivalTime_OpenWorkload265: BinaryAssociation = BinaryAssociation(
    name="interArrivalTime_OpenWorkload265",
    ends={
        Property(name="PCMRandomVariable266", type=pcm_usagemodel_OpenWorkload, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_usagemodel_OpenWorkload", type=PCMRandomVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
bodyBehaviour_Loop267: BinaryAssociation = BinaryAssociation(
    name="bodyBehaviour_Loop267",
    ends={
        Property(name="ScenarioBehaviour268", type=pcm_usagemodel_Loop, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_usagemodel_Loop", type=ScenarioBehaviour, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
loopIteration_Loop269: BinaryAssociation = BinaryAssociation(
    name="loopIteration_Loop269",
    ends={
        Property(name="PCMRandomVariable271", type=pcm_usagemodel_Loop, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_usagemodel_Loop270", type=PCMRandomVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
inputParameterUsages_EntryLevelSystemCall272: BinaryAssociation = BinaryAssociation(
    name="inputParameterUsages_EntryLevelSystemCall272",
    ends={
        Property(name="VariableUsage273", type=pcm_usagemodel_EntryLevelSystemCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_usagemodel_EntryLevelSystemCall", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
providedRole_EntryLevelSystemCall274: BinaryAssociation = BinaryAssociation(
    name="providedRole_EntryLevelSystemCall274",
    ends={
        Property(name="ProvidedRole276", type=pcm_usagemodel_EntryLevelSystemCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_usagemodel_EntryLevelSystemCall275", type=ProvidedRole, multiplicity=Multiplicity(1, 1))
    }
)
signature_EntryLevelSystemCall277: BinaryAssociation = BinaryAssociation(
    name="signature_EntryLevelSystemCall277",
    ends={
        Property(name="Signature279", type=pcm_usagemodel_EntryLevelSystemCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_usagemodel_EntryLevelSystemCall278", type=Signature, multiplicity=Multiplicity(1, 1))
    }
)
outputParameterUsages_EntryLevelSystemCall280: BinaryAssociation = BinaryAssociation(
    name="outputParameterUsages_EntryLevelSystemCall280",
    ends={
        Property(name="VariableUsage282", type=pcm_usagemodel_EntryLevelSystemCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_usagemodel_EntryLevelSystemCall281", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
branchTransitions_Branch285: BinaryAssociation = BinaryAssociation(
    name="branchTransitions_Branch285",
    ends={
        Property(name="BranchTransition", type=pcm_usagemodel_Branch, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_usagemodel_Branch", type=BranchTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
branchedBehaviour_BranchTransition286: BinaryAssociation = BinaryAssociation(
    name="branchedBehaviour_BranchTransition286",
    ends={
        Property(name="ScenarioBehaviour287", type=pcm_usagemodel_BranchTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_usagemodel_BranchTransition", type=ScenarioBehaviour, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
timeSpecification_Delay288: BinaryAssociation = BinaryAssociation(
    name="timeSpecification_Delay288",
    ends={
        Property(name="PCMRandomVariable289", type=pcm_usagemodel_Delay, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_usagemodel_Delay", type=PCMRandomVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thinkTime_ClosedWorkload283: BinaryAssociation = BinaryAssociation(
    name="thinkTime_ClosedWorkload283",
    ends={
        Property(name="PCMRandomVariable284", type=pcm_usagemodel_ClosedWorkload, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_usagemodel_ClosedWorkload", type=PCMRandomVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_pcm_core_PCMRandomVariable_RandomVariable = Generalization(general=RandomVariable, specific=pcm_core_PCMRandomVariable)
gen_pcm_entity_ResourceInterfaceRequiringEntity_Entity = Generalization(general=Entity, specific=pcm_entity_ResourceInterfaceRequiringEntity)
gen_pcm_entity_ComposedProvidingRequiringEntity_composition_ComposedStructure = Generalization(general=composition_ComposedStructure, specific=pcm_entity_ComposedProvidingRequiringEntity)
gen_pcm_entity_ComposedProvidingRequiringEntity_entity_InterfaceProvidingRequiringEntity = Generalization(general=entity_InterfaceProvidingRequiringEntity, specific=pcm_entity_ComposedProvidingRequiringEntity)
gen_pcm_entity_Entity_Identifier = Generalization(general=Identifier, specific=pcm_entity_Entity)
gen_pcm_entity_Entity_entity_NamedElement = Generalization(general=entity_NamedElement, specific=pcm_entity_Entity)
gen_pcm_entity_InterfaceProvidingEntity_Entity = Generalization(general=Entity, specific=pcm_entity_InterfaceProvidingEntity)
gen_pcm_entity_InterfaceProvidingRequiringEntity_entity_InterfaceProvidingEntity = Generalization(general=entity_InterfaceProvidingEntity, specific=pcm_entity_InterfaceProvidingRequiringEntity)
gen_pcm_entity_InterfaceProvidingRequiringEntity_entity_InterfaceRequiringEntity = Generalization(general=entity_InterfaceRequiringEntity, specific=pcm_entity_InterfaceProvidingRequiringEntity)
gen_pcm_entity_InterfaceProvidingRequiringEntity_entity_ResourceInterfaceRequiringEntity = Generalization(general=entity_ResourceInterfaceRequiringEntity, specific=pcm_entity_InterfaceProvidingRequiringEntity)
gen_pcm_entity_InterfaceRequiringEntity_Entity = Generalization(general=Entity, specific=pcm_entity_InterfaceRequiringEntity)
gen_pcm_composition_AssemblyContext_Entity = Generalization(general=Entity, specific=pcm_composition_AssemblyContext)
gen_pcm_composition_RequiredDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_composition_RequiredDelegationConnector)
gen_pcm_connectors_Connector_Entity = Generalization(general=Entity, specific=pcm_connectors_Connector)
gen_pcm_composition_ProvidedDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_composition_ProvidedDelegationConnector)
gen_pcm_composition_AssemblyConnector_Connector = Generalization(general=Connector, specific=pcm_composition_AssemblyConnector)
gen_pcm_composition_ComposedStructure_Entity = Generalization(general=Entity, specific=pcm_composition_ComposedStructure)
gen_pcm_repository_PassiveResource_Entity = Generalization(general=Entity, specific=pcm_repository_PassiveResource)
gen_pcm_repository_RepositoryComponent_InterfaceProvidingRequiringEntity = Generalization(general=InterfaceProvidingRequiringEntity, specific=pcm_repository_RepositoryComponent)
gen_pcm_repository_RequiredRole_Role = Generalization(general=Role, specific=pcm_repository_RequiredRole)
gen_pcm_repository_Repository_Entity = Generalization(general=Entity, specific=pcm_repository_Repository)
gen_pcm_repository_ResourceRequiredRole_Role = Generalization(general=Role, specific=pcm_repository_ResourceRequiredRole)
gen_pcm_repository_Role_Entity = Generalization(general=Entity, specific=pcm_repository_Role)
gen_pcm_repository_Interface_Entity = Generalization(general=Entity, specific=pcm_repository_Interface)
gen_pcm_repository_CompleteComponentType_RepositoryComponent = Generalization(general=RepositoryComponent, specific=pcm_repository_CompleteComponentType)
gen_pcm_repository_ProvidesComponentType_RepositoryComponent = Generalization(general=RepositoryComponent, specific=pcm_repository_ProvidesComponentType)
gen_pcm_repository_ImplementationComponentType_RepositoryComponent = Generalization(general=RepositoryComponent, specific=pcm_repository_ImplementationComponentType)
gen_pcm_repository_BasicComponent_ImplementationComponentType = Generalization(general=ImplementationComponentType, specific=pcm_repository_BasicComponent)
gen_pcm_repository_DelegationConnector_Connector = Generalization(general=Connector, specific=pcm_repository_DelegationConnector)
gen_pcm_repository_CompositeComponent_entity_ComposedProvidingRequiringEntity = Generalization(general=entity_ComposedProvidingRequiringEntity, specific=pcm_repository_CompositeComponent)
gen_pcm_repository_CompositeComponent_repository_ImplementationComponentType = Generalization(general=repository_ImplementationComponentType, specific=pcm_repository_CompositeComponent)
gen_pcm_repository_CompositeDataType_entity_Entity = Generalization(general=entity_Entity, specific=pcm_repository_CompositeDataType)
gen_pcm_repository_CompositeDataType_repository_DataType = Generalization(general=repository_DataType, specific=pcm_repository_CompositeDataType)
gen_pcm_repository_InnerDeclaration_NamedElement = Generalization(general=NamedElement, specific=pcm_repository_InnerDeclaration)
gen_pcm_repository_ProvidedRole_Role = Generalization(general=Role, specific=pcm_repository_ProvidedRole)
gen_pcm_repository_PrimitiveDataType_DataType = Generalization(general=DataType, specific=pcm_repository_PrimitiveDataType)
gen_pcm_repository_CollectionDataType_entity_Entity = Generalization(general=entity_Entity, specific=pcm_repository_CollectionDataType)
gen_pcm_repository_CollectionDataType_repository_DataType = Generalization(general=repository_DataType, specific=pcm_repository_CollectionDataType)
gen_pcm_parameter_CharacterisedVariable_Variable = Generalization(general=Variable, specific=pcm_parameter_CharacterisedVariable)
gen_pcm_seff_StopAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_seff_StopAction)
gen_pcm_seff_AbstractInternalControlFlowAction_AbstractAction = Generalization(general=AbstractAction, specific=pcm_seff_AbstractInternalControlFlowAction)
gen_pcm_seff_AbstractAction_Entity = Generalization(general=Entity, specific=pcm_seff_AbstractAction)
gen_pcm_seff_StartAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_seff_StartAction)
gen_pcm_seff_ResourceDemandingSEFF_Identifier = Generalization(general=Identifier, specific=pcm_seff_ResourceDemandingSEFF)
gen_pcm_seff_ResourceDemandingSEFF_seff_ServiceEffectSpecification = Generalization(general=seff_ServiceEffectSpecification, specific=pcm_seff_ResourceDemandingSEFF)
gen_pcm_seff_ResourceDemandingSEFF_seff_ResourceDemandingBehaviour = Generalization(general=seff_ResourceDemandingBehaviour, specific=pcm_seff_ResourceDemandingSEFF)
gen_pcm_seff_ForkedBehaviour_ResourceDemandingBehaviour = Generalization(general=ResourceDemandingBehaviour, specific=pcm_seff_ForkedBehaviour)
gen_pcm_seff_ExternalCallAction_AbstractAction = Generalization(general=AbstractAction, specific=pcm_seff_ExternalCallAction)
gen_pcm_seff_ReleaseAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_seff_ReleaseAction)
gen_pcm_seff_LoopAction_AbstractLoopAction = Generalization(general=AbstractLoopAction, specific=pcm_seff_LoopAction)
gen_pcm_seff_AbstractLoopAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_seff_AbstractLoopAction)
gen_pcm_seff_InternalAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_seff_InternalAction)
gen_pcm_seff_ForkAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_seff_ForkAction)
gen_pcm_seff_AcquireAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_seff_AcquireAction)
gen_pcm_seff_CollectionIteratorAction_AbstractLoopAction = Generalization(general=AbstractLoopAction, specific=pcm_seff_CollectionIteratorAction)
gen_pcm_seff_GuardedBranchTransition_AbstractBranchTransition = Generalization(general=AbstractBranchTransition, specific=pcm_seff_GuardedBranchTransition)
gen_pcm_seff_ProbabilisticBranchTransition_AbstractBranchTransition = Generalization(general=AbstractBranchTransition, specific=pcm_seff_ProbabilisticBranchTransition)
gen_pcm_seff_AbstractBranchTransition_NamedElement = Generalization(general=NamedElement, specific=pcm_seff_AbstractBranchTransition)
gen_pcm_seff_BranchAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_seff_BranchAction)
gen_pcm_resourcetype_ResourceType_entity_Entity = Generalization(general=entity_Entity, specific=pcm_resourcetype_ResourceType)
gen_pcm_resourcetype_ResourceType_UnitCarryingElement = Generalization(general=UnitCarryingElement, specific=pcm_resourcetype_ResourceType)
gen_pcm_resourcetype_CommunicationLinkResourceType_ProcessingResourceType = Generalization(general=ProcessingResourceType, specific=pcm_resourcetype_CommunicationLinkResourceType)
gen_pcm_resourcetype_ProcessingResourceType_ResourceType = Generalization(general=ResourceType, specific=pcm_resourcetype_ProcessingResourceType)
gen_pcm_allocation_AllocationContext_Entity = Generalization(general=Entity, specific=pcm_allocation_AllocationContext)
gen_pcm_allocation_Allocation_Entity = Generalization(general=Entity, specific=pcm_allocation_Allocation)
gen_pcm_seff_SetVariableAction_AbstractInternalControlFlowAction = Generalization(general=AbstractInternalControlFlowAction, specific=pcm_seff_SetVariableAction)
gen_pcm_resourceenvironment_LinkingResource_Entity = Generalization(general=Entity, specific=pcm_resourceenvironment_LinkingResource)
gen_pcm_qosannotations_QoSAnnotations_Entity = Generalization(general=Entity, specific=pcm_qosannotations_QoSAnnotations)
gen_pcm_resourceenvironment_ResourceContainer_Entity = Generalization(general=Entity, specific=pcm_resourceenvironment_ResourceContainer)
gen_pcm_system_System_entity_Entity = Generalization(general=entity_Entity, specific=pcm_system_System)
gen_pcm_system_System_entity_ComposedProvidingRequiringEntity = Generalization(general=entity_ComposedProvidingRequiringEntity, specific=pcm_system_System)
gen_pcm_performance_SystemSpecifiedExecutionTime_SpecifiedQoSAnnotation = Generalization(general=SpecifiedQoSAnnotation, specific=pcm_performance_SystemSpecifiedExecutionTime)
gen_pcm_performance_ComponentSpecifiedExecutionTime_SpecifiedQoSAnnotation = Generalization(general=SpecifiedQoSAnnotation, specific=pcm_performance_ComponentSpecifiedExecutionTime)
gen_pcm_reliability_SpecifiedFailureProbability_SpecifiedQoSAnnotation = Generalization(general=SpecifiedQoSAnnotation, specific=pcm_reliability_SpecifiedFailureProbability)
gen_pcm_usagemodel_UsageScenario_Entity = Generalization(general=Entity, specific=pcm_usagemodel_UsageScenario)
gen_pcm_usagemodel_ScenarioBehaviour_Entity = Generalization(general=Entity, specific=pcm_usagemodel_ScenarioBehaviour)
gen_pcm_usagemodel_Stop_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_usagemodel_Stop)
gen_pcm_usagemodel_Start_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_usagemodel_Start)
gen_pcm_usagemodel_AbstractUserAction_Entity = Generalization(general=Entity, specific=pcm_usagemodel_AbstractUserAction)
gen_pcm_usagemodel_Loop_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_usagemodel_Loop)
gen_pcm_usagemodel_EntryLevelSystemCall_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_usagemodel_EntryLevelSystemCall)
gen_pcm_usagemodel_OpenWorkload_Workload = Generalization(general=Workload, specific=pcm_usagemodel_OpenWorkload)
gen_pcm_usagemodel_ClosedWorkload_Workload = Generalization(general=Workload, specific=pcm_usagemodel_ClosedWorkload)
gen_pcm_usagemodel_Delay_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_usagemodel_Delay)
gen_pcm_subsystem_SubSystem_entity_ComposedProvidingRequiringEntity = Generalization(general=entity_ComposedProvidingRequiringEntity, specific=pcm_subsystem_SubSystem)
gen_pcm_subsystem_SubSystem_repository_RepositoryComponent = Generalization(general=repository_RepositoryComponent, specific=pcm_subsystem_SubSystem)
gen_pcm_usagemodel_Branch_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_usagemodel_Branch)

# Domain Model
domain_model = DomainModel(
    name="pcm",
    types={pcm_core_PCMRandomVariable, RandomVariable, pcm_entity_ResourceInterfaceRequiringEntity, ResourceRequiredRole, pcm_entity_ComposedProvidingRequiringEntity, composition_ComposedStructure, entity_InterfaceProvidingRequiringEntity, pcm_entity_Entity, Identifier, entity_NamedElement, pcm_entity_NamedElement, pcm_entity_InterfaceProvidingEntity, Entity, ProvidedRole, pcm_entity_InterfaceProvidingRequiringEntity, entity_InterfaceProvidingEntity, entity_InterfaceRequiringEntity, entity_ResourceInterfaceRequiringEntity, pcm_entity_InterfaceRequiringEntity, RequiredRole, pcm_composition_AssemblyContext, RepositoryComponent, VariableUsage, pcm_composition_RequiredDelegationConnector, pcm_connectors_Connector, pcm_composition_ProvidedDelegationConnector, DelegationConnector, composition_AssemblyContext, pcm_composition_AssemblyConnector, Connector, pcm_composition_ComposedStructure, composition_ProvidedDelegationConnector, pcm_composition_ResourceRequiredDelegationConnector, Parameter_, Interface, DataType, composition_RequiredDelegationConnector, ExceptionType, composition_AssemblyConnector, composition_ResourceRequiredDelegationConnector, pcm_repository_PassiveResource, PCMRandomVariable, pcm_repository_Signature, pcm_repository_RepositoryComponent, InterfaceProvidingRequiringEntity, pcm_repository_RequiredRole, Role, pcm_repository_Parameter, Signature, pcm_repository_DataType, Repository, pcm_repository_Repository, Protocol, pcm_repository_ResourceRequiredRole, pcm_repository_Role, pcm_repository_Interface, CompleteComponentType, pcm_repository_CompleteComponentType, pcm_repository_ExceptionType, pcm_repository_ProvidesComponentType, pcm_repository_ImplementationComponentType, pcm_repository_BasicComponent, ImplementationComponentType, ProvidesComponentType, pcm_repository_DelegationConnector, pcm_repository_CompositeComponent, entity_ComposedProvidingRequiringEntity, repository_ImplementationComponentType, CompositeDataType, InnerDeclaration, pcm_repository_InnerDeclaration, NamedElement, pcm_repository_ProvidedRole, ServiceEffectSpecification, PassiveResource, pcm_repository_PrimitiveDataType, pcm_repository_CollectionDataType, entity_Entity, repository_DataType, pcm_repository_CompositeDataType, pcm_parameter_CharacterisedVariable, Variable, pcm_parameter_VariableUsage, VariableCharacterisation, parameter_pcm_AbstractNamedReference, pcm_seff_StopAction, AbstractInternalControlFlowAction, pcm_protocol_ServiceCall, pcm_protocol_Protocol, pcm_parameter_VariableCharacterisation, pcm_seff_ResourceDemandingBehaviour, pcm_seff_AbstractInternalControlFlowAction, AbstractAction, performance_ParametricResourceDemand, pcm_seff_AbstractAction, pcm_seff_StartAction, pcm_seff_ResourceDemandingSEFF, seff_ServiceEffectSpecification, seff_ResourceDemandingBehaviour, ForkedBehaviour, SynchronisationPoint, pcm_seff_ForkedBehaviour, pcm_seff_SynchronisationPoint, pcm_seff_ExternalCallAction, pcm_seff_ReleaseAction, pcm_seff_LoopAction, AbstractLoopAction, pcm_seff_AbstractLoopAction, ResourceDemandingBehaviour, pcm_seff_InternalAction, pcm_seff_ForkAction, pcm_seff_AcquireAction, pcm_seff_CollectionIteratorAction, pcm_seff_GuardedBranchTransition, pcm_seff_ProbabilisticBranchTransition, AbstractBranchTransition, pcm_seff_AbstractBranchTransition, pcm_seff_BranchAction, pcm_resourcetype_ResourceType, UnitCarryingElement, pcm_resourcetype_ResourceRepository, ResourceType, pcm_resourcetype_CommunicationLinkResourceType, pcm_resourcetype_ProcessingResourceType, pcm_allocation_AllocationContext, ResourceContainer, pcm_allocation_Allocation, pcm_seff_SetVariableAction, pcm_seff_ServiceEffectSpecification, pcm_performance_ParametricResourceDemand, ProcessingResourceType, pcm_resourceenvironment_CommunicationLinkResourceSpecification, CommunicationLinkResourceType, pcm_resourceenvironment_ProcessingResourceSpecification, AllocationContext, ResourceEnvironment, System, pcm_resourceenvironment_ResourceEnvironment, LinkingResource, pcm_resourceenvironment_LinkingResource, CommunicationLinkResourceSpecification, pcm_qosannotations_SpecifiedOutputParameterAbstraction, pcm_qosannotations_QoSAnnotations, SpecifiedQoSAnnotation, SpecifiedOutputParameterAbstraction, pcm_resourceenvironment_ResourceContainer, ProcessingResourceSpecification, pcm_system_System, QoSAnnotations, pcm_qosannotations_SpecifiedQoSAnnotation, pcm_performance_SystemSpecifiedExecutionTime, pcm_performance_ComponentSpecifiedExecutionTime, pcm_reliability_SpecifiedFailureProbability, pcm_usagemodel_Workload, pcm_usagemodel_UsageScenario, Workload, ScenarioBehaviour, pcm_usagemodel_ScenarioBehaviour, pcm_usagemodel_Stop, pcm_usagemodel_Start, AbstractUserAction, pcm_usagemodel_AbstractUserAction, pcm_usagemodel_UsageModel, UsageScenario, UserData, pcm_usagemodel_UserData, pcm_usagemodel_Loop, pcm_usagemodel_EntryLevelSystemCall, pcm_usagemodel_OpenWorkload, pcm_usagemodel_ClosedWorkload, BranchTransition, pcm_usagemodel_BranchTransition, pcm_usagemodel_Delay, pcm_subsystem_SubSystem, repository_RepositoryComponent, pcm_usagemodel_Branch, ParameterModifier, PrimitiveTypeEnum, VariableCharacterisationType, SchedulingPolicy},
    associations={requiredRoles_InterfaceRequiringEntity1, resourceRequiredRoles_ResourceInterfaceRequiringEntity3, providedRoles_InterfaceProvidingEntity0, encapsulatedComponent_AssemblyContext13, parentStructure_AssemblyContext14, configParameterUsages_AssemblyContext17, innerProvidedRole_ProvidedDelegationConnector5, outerProvidedRole_ProvidedDelegationConnector7, assemblyContext_ProvidedDelegationConnector10, parentStructure_ProvidedDelegationConnector12, innerRequiredRole_RequiredDelegationConnector19, outerRequiredRole_RequiredDelegationConnector21, assemblyContext_RequiredDelegationConnector24, parentStructure_RequiredDelegationConnector27, parentStructure_ResourceRequiredDelegationConnector44, innerResourceRequiredRole_ResourceRequiredDelegationConnector47, outerResourceRequiredRole_ResourceRequiredDelegationConnector49, assemblyContexts_ComposedStructure52, providedDelegationConnectors_ComposedStructure55, requiringAssemblyContext_AssemblyConnector30, providingAssemblyContext_AssemblyConnector32, providedRole_AssemblyConnector35, requiredRole_AssemblyConnector38, parentStructure_AssemblyConnector41, parameters__Signature68, interface_Signature70, returntype__Signature72, requiredDelegationConnectors_ComposedStructure58, assemblyConnectors_ComposedStructure61, resourceRequiredDelegationConnectors_ComposedStructure64, capacity_PassiveResource67, components__Repository81, interfaces__Repository84, datatypes_Repository87, repository_RepositoryComponent90, exceptions__Signature73, datatype__Parameter75, signature_Parameter77, repository_DataType79, ancestorInterfaces_Interface99, protocols__Interface102, signatures__Interface104, repository_Interface107, requiredInterface_ResourceRequiredRole110, requiredInterface__RequiredRole93, requiringEntity_RequiredRole95, parentInterface__Interface97, parentCompleteComponentTypes115, componentParameterUsage_ImplementationComponentType116, resourceRequiringEntity_ResourceRequiredRole112, parentProvidesComponentTypes119, parentType_CompositeDataType125, innerDeclaration_CompositeDataType126, datatype_InnerDeclaration128, providedInterface__ProvidedRole130, serviceEffectSpecifications__BasicComponent120, passiveResource_BasicComponent121, innerType_CollectionDataType123, variableCharacterisation_VariableUsage139, namedReference_VariableUsage140, providingEntity_ProvidedRole132, signature__ServiceCall135, specification_VariableCharacterisation137, resourceDemand_Action142, predecessor_AbstractAction143, successor_AbstractAction145, asynchronousForkedBehaviours_ForkAction155, synchronisingBehaviours_ForkAction156, synchronousForkedBehaviours_SynchronisationPoint158, outputParameterUsage_SynchronisationPoint160, calledService_ExternalService163, inputParameterUsages_ExternalCallAction165, outputVariableUsages_ExternalCallAction168, steps_Behaviour148, passiveResource_ReleaseAction150, iterationCount_LoopAction152, bodyBehaviour_Loop154, branches_Branch175, passiveresource_AcquireAction176, parameter_CollectionIteratorAction178, role_ExternalService171, branchBehaviour_BranchTransition173, availableResourceTypes_ResourceRepository192, resourceContainer_AllocationContext193, assemblyContext_AllocationContext194, branchCondition_GuardedBranchTransition180, localVariableUsages_SetVariableAction182, describedService__SEFF184, specification_ParametericResourceDemand186, requiredResource_ParametricResourceDemand188, action_ParametricResourceDemand190, communicationLinkResourceType_CommunicationLinkResourceSpecification213, latency_CommunicationLinkResourceSpecification214, throughput_CommunicationLinkResourceSpecification217, allocationContexts_Allocation197, targetResourceEnvironment_Allocation198, system_Allocation200, linkingresource202, resourceContainer_ResourceEnvironment203, toResourceContainer_LinkingResource206, fromResourceContainer_LinkingResource208, communicationLinkResourceSpecifications_LinkingResource211, role_SpecifiedQoSAnnotation229, specification_SpecifiedExecutionTime232, signature_SpecifiedOutputParameterAbstraction235, role_SpecifiedOutputParameterAbstraction237, expectedExternalOutputs_SpecifiedOutputParameterAbstraction240, specifiedQoSAnnotations_QoSAnnotations243, activeResourceType_ActiveResourceSpecification220, processingRate_ProcessingResourceSpecification222, activeResourceSpecifications_ResourceContainer225, qosAnnotations_System226, signature_SpecifiedQoSAnnation227, specifiedOutputParameterAbstractions_QoSAnnotations244, assemblyContext_ComponentSpecifiedExecutionTime246, workload_UsageScenario248, scenarioBehaviour_UsageScenario249, userDataParameterUsages_UserData260, assemblyContext_userData262, actions_ScenarioBehaviour251, successor252, predecessor254, usageScenario_UsageModel257, userData_UsageModel258, interArrivalTime_OpenWorkload265, bodyBehaviour_Loop267, loopIteration_Loop269, inputParameterUsages_EntryLevelSystemCall272, providedRole_EntryLevelSystemCall274, signature_EntryLevelSystemCall277, outputParameterUsages_EntryLevelSystemCall280, branchTransitions_Branch285, branchedBehaviour_BranchTransition286, timeSpecification_Delay288, thinkTime_ClosedWorkload283},
    generalizations={gen_pcm_core_PCMRandomVariable_RandomVariable, gen_pcm_entity_ResourceInterfaceRequiringEntity_Entity, gen_pcm_entity_ComposedProvidingRequiringEntity_composition_ComposedStructure, gen_pcm_entity_ComposedProvidingRequiringEntity_entity_InterfaceProvidingRequiringEntity, gen_pcm_entity_Entity_Identifier, gen_pcm_entity_Entity_entity_NamedElement, gen_pcm_entity_InterfaceProvidingEntity_Entity, gen_pcm_entity_InterfaceProvidingRequiringEntity_entity_InterfaceProvidingEntity, gen_pcm_entity_InterfaceProvidingRequiringEntity_entity_InterfaceRequiringEntity, gen_pcm_entity_InterfaceProvidingRequiringEntity_entity_ResourceInterfaceRequiringEntity, gen_pcm_entity_InterfaceRequiringEntity_Entity, gen_pcm_composition_AssemblyContext_Entity, gen_pcm_composition_RequiredDelegationConnector_DelegationConnector, gen_pcm_connectors_Connector_Entity, gen_pcm_composition_ProvidedDelegationConnector_DelegationConnector, gen_pcm_composition_AssemblyConnector_Connector, gen_pcm_composition_ComposedStructure_Entity, gen_pcm_repository_PassiveResource_Entity, gen_pcm_repository_RepositoryComponent_InterfaceProvidingRequiringEntity, gen_pcm_repository_RequiredRole_Role, gen_pcm_repository_Repository_Entity, gen_pcm_repository_ResourceRequiredRole_Role, gen_pcm_repository_Role_Entity, gen_pcm_repository_Interface_Entity, gen_pcm_repository_CompleteComponentType_RepositoryComponent, gen_pcm_repository_ProvidesComponentType_RepositoryComponent, gen_pcm_repository_ImplementationComponentType_RepositoryComponent, gen_pcm_repository_BasicComponent_ImplementationComponentType, gen_pcm_repository_DelegationConnector_Connector, gen_pcm_repository_CompositeComponent_entity_ComposedProvidingRequiringEntity, gen_pcm_repository_CompositeComponent_repository_ImplementationComponentType, gen_pcm_repository_CompositeDataType_entity_Entity, gen_pcm_repository_CompositeDataType_repository_DataType, gen_pcm_repository_InnerDeclaration_NamedElement, gen_pcm_repository_ProvidedRole_Role, gen_pcm_repository_PrimitiveDataType_DataType, gen_pcm_repository_CollectionDataType_entity_Entity, gen_pcm_repository_CollectionDataType_repository_DataType, gen_pcm_parameter_CharacterisedVariable_Variable, gen_pcm_seff_StopAction_AbstractInternalControlFlowAction, gen_pcm_seff_AbstractInternalControlFlowAction_AbstractAction, gen_pcm_seff_AbstractAction_Entity, gen_pcm_seff_StartAction_AbstractInternalControlFlowAction, gen_pcm_seff_ResourceDemandingSEFF_Identifier, gen_pcm_seff_ResourceDemandingSEFF_seff_ServiceEffectSpecification, gen_pcm_seff_ResourceDemandingSEFF_seff_ResourceDemandingBehaviour, gen_pcm_seff_ForkedBehaviour_ResourceDemandingBehaviour, gen_pcm_seff_ExternalCallAction_AbstractAction, gen_pcm_seff_ReleaseAction_AbstractInternalControlFlowAction, gen_pcm_seff_LoopAction_AbstractLoopAction, gen_pcm_seff_AbstractLoopAction_AbstractInternalControlFlowAction, gen_pcm_seff_InternalAction_AbstractInternalControlFlowAction, gen_pcm_seff_ForkAction_AbstractInternalControlFlowAction, gen_pcm_seff_AcquireAction_AbstractInternalControlFlowAction, gen_pcm_seff_CollectionIteratorAction_AbstractLoopAction, gen_pcm_seff_GuardedBranchTransition_AbstractBranchTransition, gen_pcm_seff_ProbabilisticBranchTransition_AbstractBranchTransition, gen_pcm_seff_AbstractBranchTransition_NamedElement, gen_pcm_seff_BranchAction_AbstractInternalControlFlowAction, gen_pcm_resourcetype_ResourceType_entity_Entity, gen_pcm_resourcetype_ResourceType_UnitCarryingElement, gen_pcm_resourcetype_CommunicationLinkResourceType_ProcessingResourceType, gen_pcm_resourcetype_ProcessingResourceType_ResourceType, gen_pcm_allocation_AllocationContext_Entity, gen_pcm_allocation_Allocation_Entity, gen_pcm_seff_SetVariableAction_AbstractInternalControlFlowAction, gen_pcm_resourceenvironment_LinkingResource_Entity, gen_pcm_qosannotations_QoSAnnotations_Entity, gen_pcm_resourceenvironment_ResourceContainer_Entity, gen_pcm_system_System_entity_Entity, gen_pcm_system_System_entity_ComposedProvidingRequiringEntity, gen_pcm_performance_SystemSpecifiedExecutionTime_SpecifiedQoSAnnotation, gen_pcm_performance_ComponentSpecifiedExecutionTime_SpecifiedQoSAnnotation, gen_pcm_reliability_SpecifiedFailureProbability_SpecifiedQoSAnnotation, gen_pcm_usagemodel_UsageScenario_Entity, gen_pcm_usagemodel_ScenarioBehaviour_Entity, gen_pcm_usagemodel_Stop_AbstractUserAction, gen_pcm_usagemodel_Start_AbstractUserAction, gen_pcm_usagemodel_AbstractUserAction_Entity, gen_pcm_usagemodel_Loop_AbstractUserAction, gen_pcm_usagemodel_EntryLevelSystemCall_AbstractUserAction, gen_pcm_usagemodel_OpenWorkload_Workload, gen_pcm_usagemodel_ClosedWorkload_Workload, gen_pcm_usagemodel_Delay_AbstractUserAction, gen_pcm_subsystem_SubSystem_entity_ComposedProvidingRequiringEntity, gen_pcm_subsystem_SubSystem_repository_RepositoryComponent, gen_pcm_usagemodel_Branch_AbstractUserAction},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)