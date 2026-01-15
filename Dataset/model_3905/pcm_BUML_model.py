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
pcm_entity_InterfaceRequiringEntity = Class(name="pcm::entity::InterfaceRequiringEntity", is_abstract=True)
RequiredRole = Class(name="RequiredRole")
pcm_core_PCMRandomVariable = Class(name="pcm::core::PCMRandomVariable")
RandomVariable = Class(name="RandomVariable")
pcm_composition_AssemblyContext = Class(name="pcm::composition::AssemblyContext")
ProvidesComponentType = Class(name="ProvidesComponentType")
VariableUsage = Class(name="VariableUsage")
pcm_composition_RequiredDelegationConnector = Class(name="pcm::composition::RequiredDelegationConnector")
pcm_entity_ComposedProvidingRequiringEntity = Class(name="pcm::entity::ComposedProvidingRequiringEntity", is_abstract=True)
composition_ComposedStructure = Class(name="composition::ComposedStructure")
entity_InterfaceProvidingRequiringEntity = Class(name="entity::InterfaceProvidingRequiringEntity")
pcm_connectors_Connector = Class(name="pcm::connectors::Connector", is_abstract=True)
pcm_composition_ProvidedDelegationConnector = Class(name="pcm::composition::ProvidedDelegationConnector")
DelegationConnector = Class(name="DelegationConnector")
pcm_composition_ComposedStructure = Class(name="pcm::composition::ComposedStructure", is_abstract=True)
composition_AssemblyContext = Class(name="composition::AssemblyContext")
composition_ProvidedDelegationConnector = Class(name="composition::ProvidedDelegationConnector")
composition_RequiredDelegationConnector = Class(name="composition::RequiredDelegationConnector")
composition_AssemblyConnector = Class(name="composition::AssemblyConnector")
pcm_repository_PassiveResource = Class(name="pcm::repository::PassiveResource")
PCMRandomVariable = Class(name="PCMRandomVariable")
pcm_composition_AssemblyConnector = Class(name="pcm::composition::AssemblyConnector")
connectors_Connector = Class(name="connectors::Connector")
entity_Entity = Class(name="entity::Entity")
DataType = Class(name="DataType")
ExceptionType = Class(name="ExceptionType")
pcm_repository_Parameter = Class(name="pcm::repository::Parameter")
Signature = Class(name="Signature")
pcm_repository_DataType = Class(name="pcm::repository::DataType", is_abstract=True)
Repository = Class(name="Repository")
pcm_repository_Repository = Class(name="pcm::repository::Repository")
pcm_repository_ProvidesComponentType = Class(name="pcm::repository::ProvidesComponentType")
pcm_repository_Signature = Class(name="pcm::repository::Signature")
Parameter_ = Class(name="Parameter")
Interface = Class(name="Interface")
pcm_repository_Role = Class(name="pcm::repository::Role", is_abstract=True)
pcm_repository_Interface = Class(name="pcm::repository::Interface")
Protocol = Class(name="Protocol")
pcm_repository_ExceptionType = Class(name="pcm::repository::ExceptionType")
pcm_repository_ImplementationComponentType = Class(name="pcm::repository::ImplementationComponentType", is_abstract=True)
CompleteComponentType = Class(name="CompleteComponentType")
pcm_repository_RequiredRole = Class(name="pcm::repository::RequiredRole")
Role = Class(name="Role")
pcm_repository_CompleteComponentType = Class(name="pcm::repository::CompleteComponentType")
pcm_repository_DelegationConnector = Class(name="pcm::repository::DelegationConnector", is_abstract=True)
Connector = Class(name="Connector")
pcm_repository_CompositeComponent = Class(name="pcm::repository::CompositeComponent")
repository_ImplementationComponentType = Class(name="repository::ImplementationComponentType")
entity_ComposedProvidingRequiringEntity = Class(name="entity::ComposedProvidingRequiringEntity")
ServiceEffectSpecification = Class(name="ServiceEffectSpecification")
PassiveResource = Class(name="PassiveResource")
pcm_repository_PrimitiveDataType = Class(name="pcm::repository::PrimitiveDataType")
pcm_repository_CollectionDataType = Class(name="pcm::repository::CollectionDataType")
repository_DataType = Class(name="repository::DataType")
pcm_repository_CompositeDataType = Class(name="pcm::repository::CompositeDataType")
ImplementationComponentType = Class(name="ImplementationComponentType")
pcm_repository_BasicComponent = Class(name="pcm::repository::BasicComponent")
pcm_repository_ProvidedRole = Class(name="pcm::repository::ProvidedRole")
pcm_protocol_ServiceCall = Class(name="pcm::protocol::ServiceCall", is_abstract=True)
pcm_protocol_Protocol = Class(name="pcm::protocol::Protocol", is_abstract=True)
pcm_parameter_VariableCharacterisation = Class(name="pcm::parameter::VariableCharacterisation")
pcm_parameter_CharacterisedVariable = Class(name="pcm::parameter::CharacterisedVariable")
Variable = Class(name="Variable")
pcm_parameter_VariableUsage = Class(name="pcm::parameter::VariableUsage")
VariableCharacterisation = Class(name="VariableCharacterisation")
parameter_pcm_AbstractNamedReference = Class(name="parameter::pcm::AbstractNamedReference")
pcm_seff_StopAction = Class(name="pcm::seff::StopAction")
AbstractResourceDemandingAction = Class(name="AbstractResourceDemandingAction")
CompositeDataType = Class(name="CompositeDataType")
InnerDeclaration = Class(name="InnerDeclaration")
pcm_repository_InnerDeclaration = Class(name="pcm::repository::InnerDeclaration")
ParametricResourceDemand = Class(name="ParametricResourceDemand")
NamedElement = Class(name="NamedElement")
pcm_seff_AbstractAction = Class(name="pcm::seff::AbstractAction", is_abstract=True)
pcm_seff_ParametricResourceDemand = Class(name="pcm::seff::ParametricResourceDemand")
ProcessingResourceType = Class(name="ProcessingResourceType")
pcm_seff_StartAction = Class(name="pcm::seff::StartAction")
pcm_seff_ResourceDemandingSEFF = Class(name="pcm::seff::ResourceDemandingSEFF")
seff_ServiceEffectSpecification = Class(name="seff::ServiceEffectSpecification")
seff_ResourceDemandingBehaviour = Class(name="seff::ResourceDemandingBehaviour")
pcm_seff_AbstractResourceDemandingAction = Class(name="pcm::seff::AbstractResourceDemandingAction", is_abstract=True)
AbstractAction = Class(name="AbstractAction")
pcm_seff_ResourceDemandingBehaviour = Class(name="pcm::seff::ResourceDemandingBehaviour")
pcm_seff_ReleaseAction = Class(name="pcm::seff::ReleaseAction")
pcm_seff_LoopAction = Class(name="pcm::seff::LoopAction")
AbstractLoopAction = Class(name="AbstractLoopAction")
pcm_seff_AbstractLoopAction = Class(name="pcm::seff::AbstractLoopAction", is_abstract=True)
ResourceDemandingBehaviour = Class(name="ResourceDemandingBehaviour")
pcm_seff_InternalAction = Class(name="pcm::seff::InternalAction")
SynchronisationPoint = Class(name="SynchronisationPoint")
pcm_seff_ForkedBehaviour = Class(name="pcm::seff::ForkedBehaviour")
pcm_seff_SynchronisationPoint = Class(name="pcm::seff::SynchronisationPoint")
pcm_seff_ExternalCallAction = Class(name="pcm::seff::ExternalCallAction")
pcm_seff_ProbabilisticBranchTransition = Class(name="pcm::seff::ProbabilisticBranchTransition")
AbstractBranchTransition = Class(name="AbstractBranchTransition")
pcm_seff_AbstractBranchTransition = Class(name="pcm::seff::AbstractBranchTransition", is_abstract=True)
pcm_seff_BranchAction = Class(name="pcm::seff::BranchAction")
pcm_seff_ForkAction = Class(name="pcm::seff::ForkAction")
ForkedBehaviour = Class(name="ForkedBehaviour")
pcm_seff_CollectionIteratorAction = Class(name="pcm::seff::CollectionIteratorAction")
pcm_seff_GuardedBranchTransition = Class(name="pcm::seff::GuardedBranchTransition")
pcm_seff_SetVariableAction = Class(name="pcm::seff::SetVariableAction")
pcm_seff_ServiceEffectSpecification = Class(name="pcm::seff::ServiceEffectSpecification", is_abstract=True)
pcm_resourcetype_ResourceType = Class(name="pcm::resourcetype::ResourceType", is_abstract=True)
UnitCarryingElement = Class(name="UnitCarryingElement")
pcm_resourcetype_ResourceRepository = Class(name="pcm::resourcetype::ResourceRepository")
ResourceType = Class(name="ResourceType")
pcm_resourcetype_CommunicationLinkResourceType = Class(name="pcm::resourcetype::CommunicationLinkResourceType")
pcm_resourcetype_ProcessingResourceType = Class(name="pcm::resourcetype::ProcessingResourceType")
pcm_allocation_AllocationContext = Class(name="pcm::allocation::AllocationContext")
ResourceContainer = Class(name="ResourceContainer")
pcm_allocation_Allocation = Class(name="pcm::allocation::Allocation")
AllocationContext = Class(name="AllocationContext")
ResourceEnvironment = Class(name="ResourceEnvironment")
pcm_seff_AcquireAction = Class(name="pcm::seff::AcquireAction")
pcm_resourceenvironment_ResourceEnvironment = Class(name="pcm::resourceenvironment::ResourceEnvironment")
LinkingResource = Class(name="LinkingResource")
pcm_resourceenvironment_LinkingResource = Class(name="pcm::resourceenvironment::LinkingResource")
CommunicationLinkResourceSpecification = Class(name="CommunicationLinkResourceSpecification")
pcm_resourceenvironment_CommunicationLinkResourceSpecification = Class(name="pcm::resourceenvironment::CommunicationLinkResourceSpecification")
CommunicationLinkResourceType = Class(name="CommunicationLinkResourceType")
pcm_resourceenvironment_ProcessingResourceSpecification = Class(name="pcm::resourceenvironment::ProcessingResourceSpecification")
pcm_resourceenvironment_ResourceContainer = Class(name="pcm::resourceenvironment::ResourceContainer")
ProcessingResourceSpecification = Class(name="ProcessingResourceSpecification")
pcm_system_System = Class(name="pcm::system::System")
pcm_qosannotations_SpecifiedFailureProbability = Class(name="pcm::qosannotations::SpecifiedFailureProbability")
System = Class(name="System")
pcm_qosannotations_SystemSpecifiedExecutionTime = Class(name="pcm::qosannotations::SystemSpecifiedExecutionTime")
SpecifiedExecutionTime = Class(name="SpecifiedExecutionTime")
pcm_qosannotations_ComponentSpecifiedExecutionTime = Class(name="pcm::qosannotations::ComponentSpecifiedExecutionTime")
pcm_qosannotations_SpecifiedOutputParameterAbstraction = Class(name="pcm::qosannotations::SpecifiedOutputParameterAbstraction")
pcm_qosannotations_QoSAnnotations = Class(name="pcm::qosannotations::QoSAnnotations")
SpecifiedOutputParameterAbstraction = Class(name="SpecifiedOutputParameterAbstraction")
pcm_usagemodel_Workload = Class(name="pcm::usagemodel::Workload", is_abstract=True)
pcm_usagemodel_UsageScenario = Class(name="pcm::usagemodel::UsageScenario")
Workload = Class(name="Workload")
ScenarioBehaviour = Class(name="ScenarioBehaviour")
pcm_usagemodel_ScenarioBehaviour = Class(name="pcm::usagemodel::ScenarioBehaviour")
QoSAnnotations = Class(name="QoSAnnotations")
pcm_qosannotations_SpecifiedExecutionTime = Class(name="pcm::qosannotations::SpecifiedExecutionTime", is_abstract=True)
AbstractUserAction = Class(name="AbstractUserAction")
pcm_usagemodel_AbstractUserAction = Class(name="pcm::usagemodel::AbstractUserAction", is_abstract=True)
pcm_usagemodel_UsageModel = Class(name="pcm::usagemodel::UsageModel")
UsageScenario = Class(name="UsageScenario")
UserData = Class(name="UserData")
pcm_usagemodel_UserData = Class(name="pcm::usagemodel::UserData")
pcm_usagemodel_Stop = Class(name="pcm::usagemodel::Stop")
pcm_usagemodel_Start = Class(name="pcm::usagemodel::Start")
pcm_usagemodel_Loop = Class(name="pcm::usagemodel::Loop")
pcm_usagemodel_EntryLevelSystemCall = Class(name="pcm::usagemodel::EntryLevelSystemCall")
pcm_usagemodel_ClosedWorkload = Class(name="pcm::usagemodel::ClosedWorkload")
pcm_usagemodel_OpenWorkload = Class(name="pcm::usagemodel::OpenWorkload")
BranchTransition = Class(name="BranchTransition")
pcm_usagemodel_BranchTransition = Class(name="pcm::usagemodel::BranchTransition")
pcm_usagemodel_Delay = Class(name="pcm::usagemodel::Delay")
pcm_usagemodel_Branch = Class(name="pcm::usagemodel::Branch")

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

# pcm_core_PCMRandomVariable class attributes and methods
pcm_core_PCMRandomVariable_m_SpecificationMustNotBeNULL: Method = Method(name="SpecificationMustNotBeNULL", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_core_PCMRandomVariable.methods={pcm_core_PCMRandomVariable_m_SpecificationMustNotBeNULL}

# RandomVariable class attributes and methods

# pcm_composition_AssemblyContext class attributes and methods

# ProvidesComponentType class attributes and methods

# VariableUsage class attributes and methods

# pcm_composition_RequiredDelegationConnector class attributes and methods
pcm_composition_RequiredDelegationConnector_m_RequiredDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure: Method = Method(name="RequiredDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_composition_RequiredDelegationConnector_m_ComponentOfChildComponentContextAndInnerRoleRequiringComponentNeedToBeTheSame: Method = Method(name="ComponentOfChildComponentContextAndInnerRoleRequiringComponentNeedToBeTheSame", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_composition_RequiredDelegationConnector.methods={pcm_composition_RequiredDelegationConnector_m_RequiredDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure, pcm_composition_RequiredDelegationConnector_m_ComponentOfChildComponentContextAndInnerRoleRequiringComponentNeedToBeTheSame}

# pcm_entity_ComposedProvidingRequiringEntity class attributes and methods

# composition_ComposedStructure class attributes and methods

# entity_InterfaceProvidingRequiringEntity class attributes and methods

# pcm_connectors_Connector class attributes and methods

# pcm_composition_ProvidedDelegationConnector class attributes and methods
pcm_composition_ProvidedDelegationConnector_m_ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure: Method = Method(name="ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_composition_ProvidedDelegationConnector_m_ComponentOfChildComponentContextAndInnerRoleProvidingComponentNeedToBeTheSame: Method = Method(name="ComponentOfChildComponentContextAndInnerRoleProvidingComponentNeedToBeTheSame", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_composition_ProvidedDelegationConnector.methods={pcm_composition_ProvidedDelegationConnector_m_ComponentOfChildComponentContextAndInnerRoleProvidingComponentNeedToBeTheSame, pcm_composition_ProvidedDelegationConnector_m_ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure}

# DelegationConnector class attributes and methods

# pcm_composition_ComposedStructure class attributes and methods

# composition_AssemblyContext class attributes and methods

# composition_ProvidedDelegationConnector class attributes and methods

# composition_RequiredDelegationConnector class attributes and methods

# composition_AssemblyConnector class attributes and methods

# pcm_repository_PassiveResource class attributes and methods

# PCMRandomVariable class attributes and methods

# pcm_composition_AssemblyConnector class attributes and methods

# connectors_Connector class attributes and methods

# entity_Entity class attributes and methods

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
pcm_repository_ProvidesComponentType_m_AtLeastOneInterfaceHasToBeProvidedByAUsefullProvidesComponentType: Method = Method(name="AtLeastOneInterfaceHasToBeProvidedByAUsefullProvidesComponentType", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_repository_ProvidesComponentType.methods={pcm_repository_ProvidesComponentType_m_AtLeastOneInterfaceHasToBeProvidedByAUsefullProvidesComponentType}

# pcm_repository_Signature class attributes and methods
pcm_repository_Signature_serviceName: Property = Property(name="serviceName", type=StringType)
pcm_repository_Signature_m_ParameterNamesHaveToBeUniqueForASignature: Method = Method(name="ParameterNamesHaveToBeUniqueForASignature", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_repository_Signature.attributes={pcm_repository_Signature_serviceName}
pcm_repository_Signature.methods={pcm_repository_Signature_m_ParameterNamesHaveToBeUniqueForASignature}

# Parameter class attributes and methods

# Interface class attributes and methods

# pcm_repository_Role class attributes and methods

# pcm_repository_Interface class attributes and methods
pcm_repository_Interface_m_NoProtocolTypeIDUsedTwice: Method = Method(name="NoProtocolTypeIDUsedTwice", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_repository_Interface_m_SignaturesHaveToBeUniqueForAnInterface: Method = Method(name="SignaturesHaveToBeUniqueForAnInterface", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_repository_Interface.methods={pcm_repository_Interface_m_SignaturesHaveToBeUniqueForAnInterface, pcm_repository_Interface_m_NoProtocolTypeIDUsedTwice}

# Protocol class attributes and methods

# pcm_repository_ExceptionType class attributes and methods
pcm_repository_ExceptionType_exceptionName: Property = Property(name="exceptionName", type=StringType)
pcm_repository_ExceptionType_exceptionMessage: Property = Property(name="exceptionMessage", type=StringType)
pcm_repository_ExceptionType.attributes={pcm_repository_ExceptionType_exceptionMessage, pcm_repository_ExceptionType_exceptionName}

# pcm_repository_ImplementationComponentType class attributes and methods
pcm_repository_ImplementationComponentType_m_RequiredInterfacesHaveToConformToCompleteType: Method = Method(name="RequiredInterfacesHaveToConformToCompleteType", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_repository_ImplementationComponentType_m_providedInterfacesHaveToConformToCompleteType: Method = Method(name="providedInterfacesHaveToConformToCompleteType", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_repository_ImplementationComponentType.methods={pcm_repository_ImplementationComponentType_m_providedInterfacesHaveToConformToCompleteType, pcm_repository_ImplementationComponentType_m_RequiredInterfacesHaveToConformToCompleteType}

# CompleteComponentType class attributes and methods

# pcm_repository_RequiredRole class attributes and methods

# Role class attributes and methods

# pcm_repository_CompleteComponentType class attributes and methods
pcm_repository_CompleteComponentType_m_AtLeastOneInterfaceHasToBeProvidedOrRequiredByAUsefullCompleteComponentType: Method = Method(name="AtLeastOneInterfaceHasToBeProvidedOrRequiredByAUsefullCompleteComponentType", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_repository_CompleteComponentType_m_providedInterfacesHaveToConformToProvidedType2: Method = Method(name="providedInterfacesHaveToConformToProvidedType2", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_repository_CompleteComponentType.methods={pcm_repository_CompleteComponentType_m_AtLeastOneInterfaceHasToBeProvidedOrRequiredByAUsefullCompleteComponentType, pcm_repository_CompleteComponentType_m_providedInterfacesHaveToConformToProvidedType2}

# pcm_repository_DelegationConnector class attributes and methods

# Connector class attributes and methods

# pcm_repository_CompositeComponent class attributes and methods
pcm_repository_CompositeComponent_m_ProvideSameInterfaces: Method = Method(name="ProvideSameInterfaces", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_repository_CompositeComponent_m_RequireSameInterfaces: Method = Method(name="RequireSameInterfaces", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_repository_CompositeComponent.methods={pcm_repository_CompositeComponent_m_ProvideSameInterfaces, pcm_repository_CompositeComponent_m_RequireSameInterfaces}

# repository_ImplementationComponentType class attributes and methods

# entity_ComposedProvidingRequiringEntity class attributes and methods

# ServiceEffectSpecification class attributes and methods

# PassiveResource class attributes and methods

# pcm_repository_PrimitiveDataType class attributes and methods
pcm_repository_PrimitiveDataType_type: Property = Property(name="type", type=StringType)
pcm_repository_PrimitiveDataType.attributes={pcm_repository_PrimitiveDataType_type}

# pcm_repository_CollectionDataType class attributes and methods

# repository_DataType class attributes and methods

# pcm_repository_CompositeDataType class attributes and methods

# ImplementationComponentType class attributes and methods

# pcm_repository_BasicComponent class attributes and methods
pcm_repository_BasicComponent_m_ProvideSameInterfacesAsImplementationType: Method = Method(name="ProvideSameInterfacesAsImplementationType", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_repository_BasicComponent_m_RequireSameInterfacesAsImplementationType: Method = Method(name="RequireSameInterfacesAsImplementationType", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_repository_BasicComponent_m_NoSeffTypeUsedTwice: Method = Method(name="NoSeffTypeUsedTwice", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_repository_BasicComponent.methods={pcm_repository_BasicComponent_m_RequireSameInterfacesAsImplementationType, pcm_repository_BasicComponent_m_ProvideSameInterfacesAsImplementationType, pcm_repository_BasicComponent_m_NoSeffTypeUsedTwice}

# pcm_repository_ProvidedRole class attributes and methods

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
pcm_seff_StopAction_m_StopActionSuccessorMustNotBeDefined: Method = Method(name="StopActionSuccessorMustNotBeDefined", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_seff_StopAction.methods={pcm_seff_StopAction_m_StopActionSuccessorMustNotBeDefined}

# AbstractResourceDemandingAction class attributes and methods

# CompositeDataType class attributes and methods

# InnerDeclaration class attributes and methods

# pcm_repository_InnerDeclaration class attributes and methods

# ParametricResourceDemand class attributes and methods

# NamedElement class attributes and methods

# pcm_seff_AbstractAction class attributes and methods

# pcm_seff_ParametricResourceDemand class attributes and methods

# ProcessingResourceType class attributes and methods

# pcm_seff_StartAction class attributes and methods
pcm_seff_StartAction_m_StartActionPredecessorMustNotBeDefined: Method = Method(name="StartActionPredecessorMustNotBeDefined", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_seff_StartAction.methods={pcm_seff_StartAction_m_StartActionPredecessorMustNotBeDefined}

# pcm_seff_ResourceDemandingSEFF class attributes and methods

# seff_ServiceEffectSpecification class attributes and methods

# seff_ResourceDemandingBehaviour class attributes and methods

# pcm_seff_AbstractResourceDemandingAction class attributes and methods

# AbstractAction class attributes and methods

# pcm_seff_ResourceDemandingBehaviour class attributes and methods
pcm_seff_ResourceDemandingBehaviour_m_ExactlyOneStopAction: Method = Method(name="ExactlyOneStopAction", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_seff_ResourceDemandingBehaviour_m_ExactlyOneStartAction: Method = Method(name="ExactlyOneStartAction", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_seff_ResourceDemandingBehaviour_m_EachActionExceptStartActionandStopActionMustHhaveAPredecessorAndSuccessor: Method = Method(name="EachActionExceptStartActionandStopActionMustHhaveAPredecessorAndSuccessor", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_seff_ResourceDemandingBehaviour.methods={pcm_seff_ResourceDemandingBehaviour_m_ExactlyOneStartAction, pcm_seff_ResourceDemandingBehaviour_m_EachActionExceptStartActionandStopActionMustHhaveAPredecessorAndSuccessor, pcm_seff_ResourceDemandingBehaviour_m_ExactlyOneStopAction}

# pcm_seff_ReleaseAction class attributes and methods

# pcm_seff_LoopAction class attributes and methods

# AbstractLoopAction class attributes and methods

# pcm_seff_AbstractLoopAction class attributes and methods

# ResourceDemandingBehaviour class attributes and methods

# pcm_seff_InternalAction class attributes and methods
pcm_seff_InternalAction_failureProbability: Property = Property(name="failureProbability", type=StringType)
pcm_seff_InternalAction.attributes={pcm_seff_InternalAction_failureProbability}

# SynchronisationPoint class attributes and methods

# pcm_seff_ForkedBehaviour class attributes and methods

# pcm_seff_SynchronisationPoint class attributes and methods

# pcm_seff_ExternalCallAction class attributes and methods

# pcm_seff_ProbabilisticBranchTransition class attributes and methods
pcm_seff_ProbabilisticBranchTransition_branchProbability: Property = Property(name="branchProbability", type=FloatType)
pcm_seff_ProbabilisticBranchTransition.attributes={pcm_seff_ProbabilisticBranchTransition_branchProbability}

# AbstractBranchTransition class attributes and methods

# pcm_seff_AbstractBranchTransition class attributes and methods

# pcm_seff_BranchAction class attributes and methods
pcm_seff_BranchAction_m_EitherGuardedBranchesOrProbabilisiticBranchTransitions: Method = Method(name="EitherGuardedBranchesOrProbabilisiticBranchTransitions", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_seff_BranchAction_m_AllProbabilisticBranchProbabilitiesMustSumUpTo1: Method = Method(name="AllProbabilisticBranchProbabilitiesMustSumUpTo1", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_seff_BranchAction.methods={pcm_seff_BranchAction_m_AllProbabilisticBranchProbabilitiesMustSumUpTo1, pcm_seff_BranchAction_m_EitherGuardedBranchesOrProbabilisiticBranchTransitions}

# pcm_seff_ForkAction class attributes and methods

# ForkedBehaviour class attributes and methods

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

# ResourceContainer class attributes and methods

# pcm_allocation_Allocation class attributes and methods
pcm_allocation_Allocation_m_EachAssemblyContextWithinSystemHasToBeAllocatedExactlyOnce: Method = Method(name="EachAssemblyContextWithinSystemHasToBeAllocatedExactlyOnce", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_allocation_Allocation.methods={pcm_allocation_Allocation_m_EachAssemblyContextWithinSystemHasToBeAllocatedExactlyOnce}

# AllocationContext class attributes and methods

# ResourceEnvironment class attributes and methods

# pcm_seff_AcquireAction class attributes and methods

# pcm_resourceenvironment_ResourceEnvironment class attributes and methods

# LinkingResource class attributes and methods

# pcm_resourceenvironment_LinkingResource class attributes and methods

# CommunicationLinkResourceSpecification class attributes and methods

# pcm_resourceenvironment_CommunicationLinkResourceSpecification class attributes and methods

# CommunicationLinkResourceType class attributes and methods

# pcm_resourceenvironment_ProcessingResourceSpecification class attributes and methods
pcm_resourceenvironment_ProcessingResourceSpecification_schedulingPolicy: Property = Property(name="schedulingPolicy", type=StringType)
pcm_resourceenvironment_ProcessingResourceSpecification.attributes={pcm_resourceenvironment_ProcessingResourceSpecification_schedulingPolicy}

# pcm_resourceenvironment_ResourceContainer class attributes and methods

# ProcessingResourceSpecification class attributes and methods

# pcm_system_System class attributes and methods

# pcm_qosannotations_SpecifiedFailureProbability class attributes and methods

# System class attributes and methods

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
pcm_usagemodel_ScenarioBehaviour_m_Exactlyonestart: Method = Method(name="Exactlyonestart", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_usagemodel_ScenarioBehaviour_m_Exactlyonestop: Method = Method(name="Exactlyonestop", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_usagemodel_ScenarioBehaviour_m_EachuseractionexceptStartandStopmusthaveapredecessorandsuccessor: Method = Method(name="EachuseractionexceptStartandStopmusthaveapredecessorandsuccessor", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_usagemodel_ScenarioBehaviour.methods={pcm_usagemodel_ScenarioBehaviour_m_EachuseractionexceptStartandStopmusthaveapredecessorandsuccessor, pcm_usagemodel_ScenarioBehaviour_m_Exactlyonestart, pcm_usagemodel_ScenarioBehaviour_m_Exactlyonestop}

# QoSAnnotations class attributes and methods

# pcm_qosannotations_SpecifiedExecutionTime class attributes and methods

# AbstractUserAction class attributes and methods

# pcm_usagemodel_AbstractUserAction class attributes and methods

# pcm_usagemodel_UsageModel class attributes and methods

# UsageScenario class attributes and methods

# UserData class attributes and methods

# pcm_usagemodel_UserData class attributes and methods

# pcm_usagemodel_Stop class attributes and methods
pcm_usagemodel_Stop_m_StopHasNoSuccessor: Method = Method(name="StopHasNoSuccessor", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_usagemodel_Stop.methods={pcm_usagemodel_Stop_m_StopHasNoSuccessor}

# pcm_usagemodel_Start class attributes and methods
pcm_usagemodel_Start_m_StartHasNoPredecessor: Method = Method(name="StartHasNoPredecessor", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_usagemodel_Start.methods={pcm_usagemodel_Start_m_StartHasNoPredecessor}

# pcm_usagemodel_Loop class attributes and methods

# pcm_usagemodel_EntryLevelSystemCall class attributes and methods

# pcm_usagemodel_ClosedWorkload class attributes and methods
pcm_usagemodel_ClosedWorkload_population: Property = Property(name="population", type=IntegerType)
pcm_usagemodel_ClosedWorkload_m_PopulationInClosedWorkloadNeedsToBeSpecified: Method = Method(name="PopulationInClosedWorkloadNeedsToBeSpecified", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_usagemodel_ClosedWorkload_m_ThinkTimeInClosedWorkloadNeedsToBeSpecified: Method = Method(name="ThinkTimeInClosedWorkloadNeedsToBeSpecified", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pcm_usagemodel_ClosedWorkload.attributes={pcm_usagemodel_ClosedWorkload_population}
pcm_usagemodel_ClosedWorkload.methods={pcm_usagemodel_ClosedWorkload_m_PopulationInClosedWorkloadNeedsToBeSpecified, pcm_usagemodel_ClosedWorkload_m_ThinkTimeInClosedWorkloadNeedsToBeSpecified}

# pcm_usagemodel_OpenWorkload class attributes and methods
pcm_usagemodel_OpenWorkload_m_InterArrivalTimeInOpenWorkloadNeedsToBeSpecified: Method = Method(name="InterArrivalTimeInOpenWorkloadNeedsToBeSpecified", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_usagemodel_OpenWorkload.methods={pcm_usagemodel_OpenWorkload_m_InterArrivalTimeInOpenWorkloadNeedsToBeSpecified}

# BranchTransition class attributes and methods

# pcm_usagemodel_BranchTransition class attributes and methods
pcm_usagemodel_BranchTransition_branchProbability: Property = Property(name="branchProbability", type=FloatType)
pcm_usagemodel_BranchTransition.attributes={pcm_usagemodel_BranchTransition_branchProbability}

# pcm_usagemodel_Delay class attributes and methods

# pcm_usagemodel_Branch class attributes and methods
pcm_usagemodel_Branch_m_AllBranchProbabilitiesMustSumUpTo1: Method = Method(name="AllBranchProbabilitiesMustSumUpTo1", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pcm_usagemodel_Branch.methods={pcm_usagemodel_Branch_m_AllBranchProbabilitiesMustSumUpTo1}

# Relationships
providedRoles_InterfaceProvidingEntity0: BinaryAssociation = BinaryAssociation(
    name="providedRoles_InterfaceProvidingEntity0",
    ends={
        Property(name="repository", type=pcm_entity_InterfaceProvidingEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="ProvidedRole", type=ProvidedRole, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredRoles_InterfaceRequiringEntity1: BinaryAssociation = BinaryAssociation(
    name="requiredRoles_InterfaceRequiringEntity1",
    ends={
        Property(name="repository2", type=pcm_entity_InterfaceRequiringEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="RequiredRole", type=RequiredRole, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentStructure_ProvidedDelegationConnector10: BinaryAssociation = BinaryAssociation(
    name="parentStructure_ProvidedDelegationConnector10",
    ends={
        Property(name="core", type=pcm_composition_ProvidedDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="composition", type=composition_ComposedStructure, multiplicity=Multiplicity(1, 1))
    }
)
encapsulatedComponent_ChildComponentContext11: BinaryAssociation = BinaryAssociation(
    name="encapsulatedComponent_ChildComponentContext11",
    ends={
        Property(name="ProvidesComponentType", type=pcm_composition_AssemblyContext, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_composition_AssemblyContext", type=ProvidesComponentType, multiplicity=Multiplicity(1, 1))
    }
)
parentStructure_AssemblyContext12: BinaryAssociation = BinaryAssociation(
    name="parentStructure_AssemblyContext12",
    ends={
        Property(name="core14", type=pcm_composition_AssemblyContext, multiplicity=Multiplicity(1, 1)),
        Property(name="composition13", type=composition_ComposedStructure, multiplicity=Multiplicity(1, 1))
    }
)
configParameterUsages_AssemblyContext15: BinaryAssociation = BinaryAssociation(
    name="configParameterUsages_AssemblyContext15",
    ends={
        Property(name="VariableUsage", type=pcm_composition_AssemblyContext, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_composition_AssemblyContext16", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
childComponentContexts_ComposedStructure42: BinaryAssociation = BinaryAssociation(
    name="childComponentContexts_ComposedStructure42",
    ends={
        Property(name="core44", type=pcm_composition_ComposedStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="composition43", type=composition_AssemblyContext, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
childComponentContext_ProvidedDelegationConnector8: BinaryAssociation = BinaryAssociation(
    name="childComponentContext_ProvidedDelegationConnector8",
    ends={
        Property(name="composition_AssemblyContext", type=pcm_composition_ProvidedDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_composition_ProvidedDelegationConnector9", type=composition_AssemblyContext, multiplicity=Multiplicity(1, 1))
    }
)
providedDelegationConnectors_ComposedStructure45: BinaryAssociation = BinaryAssociation(
    name="providedDelegationConnectors_ComposedStructure45",
    ends={
        Property(name="core47", type=pcm_composition_ComposedStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="composition46", type=composition_ProvidedDelegationConnector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredDelegationConnectors_ComposedStructure48: BinaryAssociation = BinaryAssociation(
    name="requiredDelegationConnectors_ComposedStructure48",
    ends={
        Property(name="core50", type=pcm_composition_ComposedStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="composition49", type=composition_RequiredDelegationConnector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
compositeAssemblyConnectors_ComposedStructure51: BinaryAssociation = BinaryAssociation(
    name="compositeAssemblyConnectors_ComposedStructure51",
    ends={
        Property(name="core53", type=pcm_composition_ComposedStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="composition52", type=composition_AssemblyConnector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
capacity_PassiveResource54: BinaryAssociation = BinaryAssociation(
    name="capacity_PassiveResource54",
    ends={
        Property(name="PCMRandomVariable", type=pcm_repository_PassiveResource, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_repository_PassiveResource", type=PCMRandomVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
innerRequiredRole_RequiredDelegationConnector17: BinaryAssociation = BinaryAssociation(
    name="innerRequiredRole_RequiredDelegationConnector17",
    ends={
        Property(name="RequiredRole18", type=pcm_composition_RequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_composition_RequiredDelegationConnector", type=RequiredRole, multiplicity=Multiplicity(1, 1))
    }
)
outerRequiredRole_RequiredDelegationConnector19: BinaryAssociation = BinaryAssociation(
    name="outerRequiredRole_RequiredDelegationConnector19",
    ends={
        Property(name="RequiredRole21", type=pcm_composition_RequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_composition_RequiredDelegationConnector20", type=RequiredRole, multiplicity=Multiplicity(1, 1))
    }
)
childComponentContext_RequiredDelegationConnector22: BinaryAssociation = BinaryAssociation(
    name="childComponentContext_RequiredDelegationConnector22",
    ends={
        Property(name="composition_AssemblyContext24", type=pcm_composition_RequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_composition_RequiredDelegationConnector23", type=composition_AssemblyContext, multiplicity=Multiplicity(1, 1))
    }
)
parentStructure_RequiredDelegationConnector25: BinaryAssociation = BinaryAssociation(
    name="parentStructure_RequiredDelegationConnector25",
    ends={
        Property(name="core27", type=pcm_composition_RequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="composition26", type=composition_ComposedStructure, multiplicity=Multiplicity(1, 1))
    }
)
requiringChildComponentContext_CompositeAssemblyConnector28: BinaryAssociation = BinaryAssociation(
    name="requiringChildComponentContext_CompositeAssemblyConnector28",
    ends={
        Property(name="composition_AssemblyContext29", type=pcm_composition_AssemblyConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_composition_AssemblyConnector", type=composition_AssemblyContext, multiplicity=Multiplicity(1, 1))
    }
)
providingChildComponentContext_CompositeAssemblyConnector30: BinaryAssociation = BinaryAssociation(
    name="providingChildComponentContext_CompositeAssemblyConnector30",
    ends={
        Property(name="composition_AssemblyContext32", type=pcm_composition_AssemblyConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_composition_AssemblyConnector31", type=composition_AssemblyContext, multiplicity=Multiplicity(1, 1))
    }
)
providedRole_CompositeAssemblyConnector33: BinaryAssociation = BinaryAssociation(
    name="providedRole_CompositeAssemblyConnector33",
    ends={
        Property(name="ProvidedRole35", type=pcm_composition_AssemblyConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_composition_AssemblyConnector34", type=ProvidedRole, multiplicity=Multiplicity(1, 1))
    }
)
requiredRole_CompositeAssemblyConnector36: BinaryAssociation = BinaryAssociation(
    name="requiredRole_CompositeAssemblyConnector36",
    ends={
        Property(name="RequiredRole38", type=pcm_composition_AssemblyConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_composition_AssemblyConnector37", type=RequiredRole, multiplicity=Multiplicity(1, 1))
    }
)
parentStructure_AssemblyConnector39: BinaryAssociation = BinaryAssociation(
    name="parentStructure_AssemblyConnector39",
    ends={
        Property(name="core41", type=pcm_composition_AssemblyConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="composition40", type=composition_ComposedStructure, multiplicity=Multiplicity(1, 1))
    }
)
returntype__Signature59: BinaryAssociation = BinaryAssociation(
    name="returntype__Signature59",
    ends={
        Property(name="DataType", type=pcm_repository_Signature, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_repository_Signature", type=DataType, multiplicity=Multiplicity(0, 1))
    }
)
exceptions__Signature60: BinaryAssociation = BinaryAssociation(
    name="exceptions__Signature60",
    ends={
        Property(name="ExceptionType", type=pcm_repository_Signature, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_repository_Signature61", type=ExceptionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
datatype__Parameter62: BinaryAssociation = BinaryAssociation(
    name="datatype__Parameter62",
    ends={
        Property(name="DataType63", type=pcm_repository_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_repository_Parameter", type=DataType, multiplicity=Multiplicity(1, 1))
    }
)
signature_Parameter64: BinaryAssociation = BinaryAssociation(
    name="signature_Parameter64",
    ends={
        Property(name="repository65", type=pcm_repository_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="Signature", type=Signature, multiplicity=Multiplicity(1, 1))
    }
)
repository_DataType66: BinaryAssociation = BinaryAssociation(
    name="repository_DataType66",
    ends={
        Property(name="repository67", type=pcm_repository_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="Repository", type=Repository, multiplicity=Multiplicity(1, 1))
    }
)
components__Repository68: BinaryAssociation = BinaryAssociation(
    name="components__Repository68",
    ends={
        Property(name="repository70", type=pcm_repository_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="ProvidesComponentType69", type=ProvidesComponentType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
interfaces__Repository71: BinaryAssociation = BinaryAssociation(
    name="interfaces__Repository71",
    ends={
        Property(name="repository73", type=pcm_repository_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="Interface72", type=Interface, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
datatypes_Repository74: BinaryAssociation = BinaryAssociation(
    name="datatypes_Repository74",
    ends={
        Property(name="repository76", type=pcm_repository_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="DataType75", type=DataType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters__Signature55: BinaryAssociation = BinaryAssociation(
    name="parameters__Signature55",
    ends={
        Property(name="repository56", type=pcm_repository_Signature, multiplicity=Multiplicity(1, 1)),
        Property(name="Parameter", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
interface_Signature57: BinaryAssociation = BinaryAssociation(
    name="interface_Signature57",
    ends={
        Property(name="repository58", type=pcm_repository_Signature, multiplicity=Multiplicity(1, 1)),
        Property(name="Interface", type=Interface, multiplicity=Multiplicity(1, 1))
    }
)
requiringEntity_RequiredRole82: BinaryAssociation = BinaryAssociation(
    name="requiringEntity_RequiredRole82",
    ends={
        Property(name="core83", type=pcm_repository_RequiredRole, multiplicity=Multiplicity(1, 1)),
        Property(name="entity", type=entity_InterfaceRequiringEntity, multiplicity=Multiplicity(1, 1))
    }
)
parentInterface__Interface84: BinaryAssociation = BinaryAssociation(
    name="parentInterface__Interface84",
    ends={
        Property(name="Interface85", type=pcm_repository_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_repository_Interface", type=Interface, multiplicity=Multiplicity(0, 9999))
    }
)
anchestorInterfaces_Interface86: BinaryAssociation = BinaryAssociation(
    name="anchestorInterfaces_Interface86",
    ends={
        Property(name="Interface88", type=pcm_repository_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_repository_Interface87", type=Interface, multiplicity=Multiplicity(0, 9999))
    }
)
protocols__Interface89: BinaryAssociation = BinaryAssociation(
    name="protocols__Interface89",
    ends={
        Property(name="Protocol", type=pcm_repository_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_repository_Interface90", type=Protocol, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
signatures__Interface91: BinaryAssociation = BinaryAssociation(
    name="signatures__Interface91",
    ends={
        Property(name="repository93", type=pcm_repository_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="Signature92", type=Signature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
repository_Interface94: BinaryAssociation = BinaryAssociation(
    name="repository_Interface94",
    ends={
        Property(name="repository96", type=pcm_repository_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="Repository95", type=Repository, multiplicity=Multiplicity(1, 1))
    }
)
repository_ProvidesComponentType77: BinaryAssociation = BinaryAssociation(
    name="repository_ProvidesComponentType77",
    ends={
        Property(name="repository79", type=pcm_repository_ProvidesComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="Repository78", type=Repository, multiplicity=Multiplicity(1, 1))
    }
)
requiredInterface__RequiredRole80: BinaryAssociation = BinaryAssociation(
    name="requiredInterface__RequiredRole80",
    ends={
        Property(name="Interface81", type=pcm_repository_RequiredRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_repository_RequiredRole", type=Interface, multiplicity=Multiplicity(1, 1))
    }
)
parentCompleteComponentTypes97: BinaryAssociation = BinaryAssociation(
    name="parentCompleteComponentTypes97",
    ends={
        Property(name="CompleteComponentType", type=pcm_repository_ImplementationComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_repository_ImplementationComponentType", type=CompleteComponentType, multiplicity=Multiplicity(0, 9999))
    }
)
componentParameterUsage_ImplementationComponentType98: BinaryAssociation = BinaryAssociation(
    name="componentParameterUsage_ImplementationComponentType98",
    ends={
        Property(name="VariableUsage100", type=pcm_repository_ImplementationComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_repository_ImplementationComponentType99", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentProvidesComponentTypes101: BinaryAssociation = BinaryAssociation(
    name="parentProvidesComponentTypes101",
    ends={
        Property(name="ProvidesComponentType102", type=pcm_repository_CompleteComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_repository_CompleteComponentType", type=ProvidesComponentType, multiplicity=Multiplicity(0, 9999))
    }
)
implementationComponentType104: BinaryAssociation = BinaryAssociation(
    name="implementationComponentType104",
    ends={
        Property(name="ImplementationComponentType105", type=pcm_repository_BasicComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_repository_BasicComponent", type=ImplementationComponentType, multiplicity=Multiplicity(0, 1))
    }
)
serviceEffectSpecifications__BasicComponent106: BinaryAssociation = BinaryAssociation(
    name="serviceEffectSpecifications__BasicComponent106",
    ends={
        Property(name="ServiceEffectSpecification", type=pcm_repository_BasicComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_repository_BasicComponent107", type=ServiceEffectSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
passiveResource_BasicComponent108: BinaryAssociation = BinaryAssociation(
    name="passiveResource_BasicComponent108",
    ends={
        Property(name="PassiveResource", type=pcm_repository_BasicComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_repository_BasicComponent109", type=PassiveResource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
innerType_CollectionDataType110: BinaryAssociation = BinaryAssociation(
    name="innerType_CollectionDataType110",
    ends={
        Property(name="DataType111", type=pcm_repository_CollectionDataType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_repository_CollectionDataType", type=DataType, multiplicity=Multiplicity(1, 1))
    }
)
implementationComponentType103: BinaryAssociation = BinaryAssociation(
    name="implementationComponentType103",
    ends={
        Property(name="ImplementationComponentType", type=pcm_repository_CompositeComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_repository_CompositeComponent", type=ImplementationComponentType, multiplicity=Multiplicity(0, 1))
    }
)
datatype_InnerDeclaration115: BinaryAssociation = BinaryAssociation(
    name="datatype_InnerDeclaration115",
    ends={
        Property(name="DataType116", type=pcm_repository_InnerDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_repository_InnerDeclaration", type=DataType, multiplicity=Multiplicity(1, 1))
    }
)
providedInterface__ProvidedRole117: BinaryAssociation = BinaryAssociation(
    name="providedInterface__ProvidedRole117",
    ends={
        Property(name="Interface118", type=pcm_repository_ProvidedRole, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_repository_ProvidedRole", type=Interface, multiplicity=Multiplicity(1, 1))
    }
)
providingEntity_ProvidedRole119: BinaryAssociation = BinaryAssociation(
    name="providingEntity_ProvidedRole119",
    ends={
        Property(name="core121", type=pcm_repository_ProvidedRole, multiplicity=Multiplicity(1, 1)),
        Property(name="entity120", type=entity_InterfaceProvidingEntity, multiplicity=Multiplicity(1, 1))
    }
)
signature__ServiceCall122: BinaryAssociation = BinaryAssociation(
    name="signature__ServiceCall122",
    ends={
        Property(name="Signature123", type=pcm_protocol_ServiceCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_protocol_ServiceCall", type=Signature, multiplicity=Multiplicity(1, 1))
    }
)
specification_VariableCharacterisation124: BinaryAssociation = BinaryAssociation(
    name="specification_VariableCharacterisation124",
    ends={
        Property(name="PCMRandomVariable125", type=pcm_parameter_VariableCharacterisation, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_parameter_VariableCharacterisation", type=PCMRandomVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variableCharacterisation_VariableUsage126: BinaryAssociation = BinaryAssociation(
    name="variableCharacterisation_VariableUsage126",
    ends={
        Property(name="VariableCharacterisation", type=pcm_parameter_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_parameter_VariableUsage", type=VariableCharacterisation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
namedReference_VariableUsage127: BinaryAssociation = BinaryAssociation(
    name="namedReference_VariableUsage127",
    ends={
        Property(name="parameter_pcm_AbstractNamedReference", type=pcm_parameter_VariableUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_parameter_VariableUsage128", type=parameter_pcm_AbstractNamedReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parentType_CompositeDataType112: BinaryAssociation = BinaryAssociation(
    name="parentType_CompositeDataType112",
    ends={
        Property(name="CompositeDataType", type=pcm_repository_CompositeDataType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_repository_CompositeDataType", type=CompositeDataType, multiplicity=Multiplicity(0, 9999))
    }
)
innerDeclaration_CompositeDataType113: BinaryAssociation = BinaryAssociation(
    name="innerDeclaration_CompositeDataType113",
    ends={
        Property(name="InnerDeclaration", type=pcm_repository_CompositeDataType, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_repository_CompositeDataType114", type=InnerDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceDemand_Action129: BinaryAssociation = BinaryAssociation(
    name="resourceDemand_Action129",
    ends={
        Property(name="seff", type=pcm_seff_AbstractResourceDemandingAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ParametricResourceDemand", type=ParametricResourceDemand, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
predecessor_AbstractAction130: BinaryAssociation = BinaryAssociation(
    name="predecessor_AbstractAction130",
    ends={
        Property(name="seff131", type=pcm_seff_AbstractAction, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractAction", type=AbstractAction, multiplicity=Multiplicity(0, 1))
    }
)
successor_AbstractAction132: BinaryAssociation = BinaryAssociation(
    name="successor_AbstractAction132",
    ends={
        Property(name="seff134", type=pcm_seff_AbstractAction, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractAction133", type=AbstractAction, multiplicity=Multiplicity(0, 1))
    }
)
requiredResource_ParametricResourceDemand135: BinaryAssociation = BinaryAssociation(
    name="requiredResource_ParametricResourceDemand135",
    ends={
        Property(name="ProcessingResourceType", type=pcm_seff_ParametricResourceDemand, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_seff_ParametricResourceDemand", type=ProcessingResourceType, multiplicity=Multiplicity(1, 1))
    }
)
specification_ParametericResourceDemand136: BinaryAssociation = BinaryAssociation(
    name="specification_ParametericResourceDemand136",
    ends={
        Property(name="PCMRandomVariable138", type=pcm_seff_ParametricResourceDemand, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_seff_ParametricResourceDemand137", type=PCMRandomVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
action_ParametricResourceDemand139: BinaryAssociation = BinaryAssociation(
    name="action_ParametricResourceDemand139",
    ends={
        Property(name="seff140", type=pcm_seff_ParametricResourceDemand, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractResourceDemandingAction", type=AbstractResourceDemandingAction, multiplicity=Multiplicity(1, 1))
    }
)
steps_Behaviour141: BinaryAssociation = BinaryAssociation(
    name="steps_Behaviour141",
    ends={
        Property(name="AbstractAction142", type=pcm_seff_ResourceDemandingBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_seff_ResourceDemandingBehaviour", type=AbstractAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
passiveResource_ReleaseAction143: BinaryAssociation = BinaryAssociation(
    name="passiveResource_ReleaseAction143",
    ends={
        Property(name="PassiveResource144", type=pcm_seff_ReleaseAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_seff_ReleaseAction", type=PassiveResource, multiplicity=Multiplicity(1, 1))
    }
)
iterationCount_LoopAction145: BinaryAssociation = BinaryAssociation(
    name="iterationCount_LoopAction145",
    ends={
        Property(name="PCMRandomVariable146", type=pcm_seff_LoopAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_seff_LoopAction", type=PCMRandomVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
bodyBehaviour_Loop147: BinaryAssociation = BinaryAssociation(
    name="bodyBehaviour_Loop147",
    ends={
        Property(name="ResourceDemandingBehaviour", type=pcm_seff_AbstractLoopAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_seff_AbstractLoopAction", type=ResourceDemandingBehaviour, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
synchronisingBehaviours_ForkAction149: BinaryAssociation = BinaryAssociation(
    name="synchronisingBehaviours_ForkAction149",
    ends={
        Property(name="SynchronisationPoint", type=pcm_seff_ForkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_seff_ForkAction150", type=SynchronisationPoint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
synchronousForkedBehaviours_SynchronisationPoint151: BinaryAssociation = BinaryAssociation(
    name="synchronousForkedBehaviours_SynchronisationPoint151",
    ends={
        Property(name="ForkedBehaviour152", type=pcm_seff_SynchronisationPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_seff_SynchronisationPoint", type=ForkedBehaviour, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
outputParameterUsage_SynchronisationPoint153: BinaryAssociation = BinaryAssociation(
    name="outputParameterUsage_SynchronisationPoint153",
    ends={
        Property(name="VariableUsage155", type=pcm_seff_SynchronisationPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_seff_SynchronisationPoint154", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
calledService_ExternalService156: BinaryAssociation = BinaryAssociation(
    name="calledService_ExternalService156",
    ends={
        Property(name="Signature157", type=pcm_seff_ExternalCallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_seff_ExternalCallAction", type=Signature, multiplicity=Multiplicity(1, 1))
    }
)
inputParameterUsages_ExternalCallAction158: BinaryAssociation = BinaryAssociation(
    name="inputParameterUsages_ExternalCallAction158",
    ends={
        Property(name="VariableUsage160", type=pcm_seff_ExternalCallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_seff_ExternalCallAction159", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputVariableUsages_ExternalCallAction161: BinaryAssociation = BinaryAssociation(
    name="outputVariableUsages_ExternalCallAction161",
    ends={
        Property(name="VariableUsage163", type=pcm_seff_ExternalCallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_seff_ExternalCallAction162", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
role_ExternalService164: BinaryAssociation = BinaryAssociation(
    name="role_ExternalService164",
    ends={
        Property(name="Role", type=pcm_seff_ExternalCallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_seff_ExternalCallAction165", type=Role, multiplicity=Multiplicity(1, 1))
    }
)
branchBehaviour_BranchTransition166: BinaryAssociation = BinaryAssociation(
    name="branchBehaviour_BranchTransition166",
    ends={
        Property(name="ResourceDemandingBehaviour167", type=pcm_seff_AbstractBranchTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_seff_AbstractBranchTransition", type=ResourceDemandingBehaviour, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
asynchronousForkedBehaviours_ForkAction148: BinaryAssociation = BinaryAssociation(
    name="asynchronousForkedBehaviours_ForkAction148",
    ends={
        Property(name="ForkedBehaviour", type=pcm_seff_ForkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_seff_ForkAction", type=ForkedBehaviour, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameter_CollectionIteratorAction171: BinaryAssociation = BinaryAssociation(
    name="parameter_CollectionIteratorAction171",
    ends={
        Property(name="Parameter172", type=pcm_seff_CollectionIteratorAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_seff_CollectionIteratorAction", type=Parameter_, multiplicity=Multiplicity(1, 1))
    }
)
branchCondition_GuardedBranchTransition173: BinaryAssociation = BinaryAssociation(
    name="branchCondition_GuardedBranchTransition173",
    ends={
        Property(name="PCMRandomVariable174", type=pcm_seff_GuardedBranchTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_seff_GuardedBranchTransition", type=PCMRandomVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
localVariableUsages_SetVariableAction175: BinaryAssociation = BinaryAssociation(
    name="localVariableUsages_SetVariableAction175",
    ends={
        Property(name="VariableUsage176", type=pcm_seff_SetVariableAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_seff_SetVariableAction", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
describedService__SEFF177: BinaryAssociation = BinaryAssociation(
    name="describedService__SEFF177",
    ends={
        Property(name="Signature178", type=pcm_seff_ServiceEffectSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_seff_ServiceEffectSpecification", type=Signature, multiplicity=Multiplicity(1, 1))
    }
)
availableResourceTypes_ResourceRepository179: BinaryAssociation = BinaryAssociation(
    name="availableResourceTypes_ResourceRepository179",
    ends={
        Property(name="ResourceType", type=pcm_resourcetype_ResourceRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_resourcetype_ResourceRepository", type=ResourceType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceContainer_AllocationContext180: BinaryAssociation = BinaryAssociation(
    name="resourceContainer_AllocationContext180",
    ends={
        Property(name="ResourceContainer", type=pcm_allocation_AllocationContext, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_allocation_AllocationContext", type=ResourceContainer, multiplicity=Multiplicity(1, 1))
    }
)
assemblyContext_AllocationContext181: BinaryAssociation = BinaryAssociation(
    name="assemblyContext_AllocationContext181",
    ends={
        Property(name="composition_AssemblyContext183", type=pcm_allocation_AllocationContext, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_allocation_AllocationContext182", type=composition_AssemblyContext, multiplicity=Multiplicity(1, 1))
    }
)
allocationContexts_Allocation184: BinaryAssociation = BinaryAssociation(
    name="allocationContexts_Allocation184",
    ends={
        Property(name="AllocationContext", type=pcm_allocation_Allocation, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_allocation_Allocation", type=AllocationContext, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
branches_Branch168: BinaryAssociation = BinaryAssociation(
    name="branches_Branch168",
    ends={
        Property(name="AbstractBranchTransition", type=pcm_seff_BranchAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_seff_BranchAction", type=AbstractBranchTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
passiveresource_AcquireAction169: BinaryAssociation = BinaryAssociation(
    name="passiveresource_AcquireAction169",
    ends={
        Property(name="PassiveResource170", type=pcm_seff_AcquireAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_seff_AcquireAction", type=PassiveResource, multiplicity=Multiplicity(1, 1))
    }
)
linkingresource189: BinaryAssociation = BinaryAssociation(
    name="linkingresource189",
    ends={
        Property(name="LinkingResource", type=pcm_resourceenvironment_ResourceEnvironment, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_resourceenvironment_ResourceEnvironment", type=LinkingResource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceContainer_ResourceEnvironment190: BinaryAssociation = BinaryAssociation(
    name="resourceContainer_ResourceEnvironment190",
    ends={
        Property(name="ResourceContainer192", type=pcm_resourceenvironment_ResourceEnvironment, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_resourceenvironment_ResourceEnvironment191", type=ResourceContainer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
toResourceContainer_LinkingResource193: BinaryAssociation = BinaryAssociation(
    name="toResourceContainer_LinkingResource193",
    ends={
        Property(name="ResourceContainer194", type=pcm_resourceenvironment_LinkingResource, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_resourceenvironment_LinkingResource", type=ResourceContainer, multiplicity=Multiplicity(0, 9999))
    }
)
fromResourceContainer_LinkingResource195: BinaryAssociation = BinaryAssociation(
    name="fromResourceContainer_LinkingResource195",
    ends={
        Property(name="ResourceContainer197", type=pcm_resourceenvironment_LinkingResource, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_resourceenvironment_LinkingResource196", type=ResourceContainer, multiplicity=Multiplicity(0, 9999))
    }
)
communicationLinkResourceSpecifications_LinkingResource198: BinaryAssociation = BinaryAssociation(
    name="communicationLinkResourceSpecifications_LinkingResource198",
    ends={
        Property(name="CommunicationLinkResourceSpecification", type=pcm_resourceenvironment_LinkingResource, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_resourceenvironment_LinkingResource199", type=CommunicationLinkResourceSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
communicationLinkResourceType_CommunicationLinkResourceSpecification200: BinaryAssociation = BinaryAssociation(
    name="communicationLinkResourceType_CommunicationLinkResourceSpecification200",
    ends={
        Property(name="CommunicationLinkResourceType", type=pcm_resourceenvironment_CommunicationLinkResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_resourceenvironment_CommunicationLinkResourceSpecification", type=CommunicationLinkResourceType, multiplicity=Multiplicity(1, 1))
    }
)
latency_CommunicationLinkResourceSpecification201: BinaryAssociation = BinaryAssociation(
    name="latency_CommunicationLinkResourceSpecification201",
    ends={
        Property(name="PCMRandomVariable203", type=pcm_resourceenvironment_CommunicationLinkResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_resourceenvironment_CommunicationLinkResourceSpecification202", type=PCMRandomVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
throughput_CommunicationLinkResourceSpecification204: BinaryAssociation = BinaryAssociation(
    name="throughput_CommunicationLinkResourceSpecification204",
    ends={
        Property(name="PCMRandomVariable206", type=pcm_resourceenvironment_CommunicationLinkResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_resourceenvironment_CommunicationLinkResourceSpecification205", type=PCMRandomVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
activeResourceType_ActiveResourceSpecification207: BinaryAssociation = BinaryAssociation(
    name="activeResourceType_ActiveResourceSpecification207",
    ends={
        Property(name="ProcessingResourceType208", type=pcm_resourceenvironment_ProcessingResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_resourceenvironment_ProcessingResourceSpecification", type=ProcessingResourceType, multiplicity=Multiplicity(1, 1))
    }
)
processingRate_ProcessingResourceSpecification209: BinaryAssociation = BinaryAssociation(
    name="processingRate_ProcessingResourceSpecification209",
    ends={
        Property(name="PCMRandomVariable211", type=pcm_resourceenvironment_ProcessingResourceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_resourceenvironment_ProcessingResourceSpecification210", type=PCMRandomVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
activeResourceSpecifications_ResourceContainer212: BinaryAssociation = BinaryAssociation(
    name="activeResourceSpecifications_ResourceContainer212",
    ends={
        Property(name="ProcessingResourceSpecification", type=pcm_resourceenvironment_ResourceContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_resourceenvironment_ResourceContainer", type=ProcessingResourceSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
targetResourceEnvironment_Allocation185: BinaryAssociation = BinaryAssociation(
    name="targetResourceEnvironment_Allocation185",
    ends={
        Property(name="ResourceEnvironment", type=pcm_allocation_Allocation, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_allocation_Allocation186", type=ResourceEnvironment, multiplicity=Multiplicity(0, 1))
    }
)
system_Allocation187: BinaryAssociation = BinaryAssociation(
    name="system_Allocation187",
    ends={
        Property(name="System", type=pcm_allocation_Allocation, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_allocation_Allocation188", type=System, multiplicity=Multiplicity(1, 1))
    }
)
assemblyContext_ComponentSpecifiedExecutionTime222: BinaryAssociation = BinaryAssociation(
    name="assemblyContext_ComponentSpecifiedExecutionTime222",
    ends={
        Property(name="composition_AssemblyContext223", type=pcm_qosannotations_ComponentSpecifiedExecutionTime, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_qosannotations_ComponentSpecifiedExecutionTime", type=composition_AssemblyContext, multiplicity=Multiplicity(1, 1))
    }
)
signature_SpecifiedOutputParameterAbstraction224: BinaryAssociation = BinaryAssociation(
    name="signature_SpecifiedOutputParameterAbstraction224",
    ends={
        Property(name="Signature225", type=pcm_qosannotations_SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_qosannotations_SpecifiedOutputParameterAbstraction", type=Signature, multiplicity=Multiplicity(1, 1))
    }
)
role_SpecifiedOutputParameterAbstraction226: BinaryAssociation = BinaryAssociation(
    name="role_SpecifiedOutputParameterAbstraction226",
    ends={
        Property(name="Role228", type=pcm_qosannotations_SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_qosannotations_SpecifiedOutputParameterAbstraction227", type=Role, multiplicity=Multiplicity(1, 1))
    }
)
expectedExternalOutputs_SpecifiedOutputParameterAbstraction229: BinaryAssociation = BinaryAssociation(
    name="expectedExternalOutputs_SpecifiedOutputParameterAbstraction229",
    ends={
        Property(name="VariableUsage231", type=pcm_qosannotations_SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_qosannotations_SpecifiedOutputParameterAbstraction230", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specifiedExecutionTimes_QoSAnnotations232: BinaryAssociation = BinaryAssociation(
    name="specifiedExecutionTimes_QoSAnnotations232",
    ends={
        Property(name="SpecifiedExecutionTime", type=pcm_qosannotations_QoSAnnotations, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_qosannotations_QoSAnnotations", type=SpecifiedExecutionTime, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specifiedOutputParameterAbstractions_QoSAnnotations233: BinaryAssociation = BinaryAssociation(
    name="specifiedOutputParameterAbstractions_QoSAnnotations233",
    ends={
        Property(name="SpecifiedOutputParameterAbstraction", type=pcm_qosannotations_QoSAnnotations, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_qosannotations_QoSAnnotations234", type=SpecifiedOutputParameterAbstraction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
workload_UsageScenario235: BinaryAssociation = BinaryAssociation(
    name="workload_UsageScenario235",
    ends={
        Property(name="Workload", type=pcm_usagemodel_UsageScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_usagemodel_UsageScenario", type=Workload, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
scenarioBehaviour_UsageScenario236: BinaryAssociation = BinaryAssociation(
    name="scenarioBehaviour_UsageScenario236",
    ends={
        Property(name="ScenarioBehaviour", type=pcm_usagemodel_UsageScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_usagemodel_UsageScenario237", type=ScenarioBehaviour, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
qosAnnotations_System213: BinaryAssociation = BinaryAssociation(
    name="qosAnnotations_System213",
    ends={
        Property(name="QoSAnnotations", type=pcm_system_System, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_system_System", type=QoSAnnotations, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
signature_SpecifiedTimeConsumption214: BinaryAssociation = BinaryAssociation(
    name="signature_SpecifiedTimeConsumption214",
    ends={
        Property(name="Signature215", type=pcm_qosannotations_SpecifiedExecutionTime, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_qosannotations_SpecifiedExecutionTime", type=Signature, multiplicity=Multiplicity(1, 1))
    }
)
role_SpecifiedExecutionTime216: BinaryAssociation = BinaryAssociation(
    name="role_SpecifiedExecutionTime216",
    ends={
        Property(name="Role218", type=pcm_qosannotations_SpecifiedExecutionTime, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_qosannotations_SpecifiedExecutionTime217", type=Role, multiplicity=Multiplicity(1, 1))
    }
)
specification_SpecifiedExecutionTime219: BinaryAssociation = BinaryAssociation(
    name="specification_SpecifiedExecutionTime219",
    ends={
        Property(name="PCMRandomVariable221", type=pcm_qosannotations_SpecifiedExecutionTime, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_qosannotations_SpecifiedExecutionTime220", type=PCMRandomVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
actions_ScenarioBehaviour238: BinaryAssociation = BinaryAssociation(
    name="actions_ScenarioBehaviour238",
    ends={
        Property(name="AbstractUserAction", type=pcm_usagemodel_ScenarioBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_usagemodel_ScenarioBehaviour", type=AbstractUserAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
successor239: BinaryAssociation = BinaryAssociation(
    name="successor239",
    ends={
        Property(name="usagemodel", type=pcm_usagemodel_AbstractUserAction, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractUserAction240", type=AbstractUserAction, multiplicity=Multiplicity(0, 1))
    }
)
predecessor241: BinaryAssociation = BinaryAssociation(
    name="predecessor241",
    ends={
        Property(name="usagemodel243", type=pcm_usagemodel_AbstractUserAction, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractUserAction242", type=AbstractUserAction, multiplicity=Multiplicity(0, 1))
    }
)
usageScenario_UsageModel244: BinaryAssociation = BinaryAssociation(
    name="usageScenario_UsageModel244",
    ends={
        Property(name="UsageScenario", type=pcm_usagemodel_UsageModel, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_usagemodel_UsageModel", type=UsageScenario, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
userData_UsageModel245: BinaryAssociation = BinaryAssociation(
    name="userData_UsageModel245",
    ends={
        Property(name="UserData", type=pcm_usagemodel_UsageModel, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_usagemodel_UsageModel246", type=UserData, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
userDataParameterUsages_UserData247: BinaryAssociation = BinaryAssociation(
    name="userDataParameterUsages_UserData247",
    ends={
        Property(name="VariableUsage248", type=pcm_usagemodel_UserData, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_usagemodel_UserData", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
assemblyContext_userData249: BinaryAssociation = BinaryAssociation(
    name="assemblyContext_userData249",
    ends={
        Property(name="composition_AssemblyContext251", type=pcm_usagemodel_UserData, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_usagemodel_UserData250", type=composition_AssemblyContext, multiplicity=Multiplicity(1, 1))
    }
)
interArrivalTime_OpenWorkload252: BinaryAssociation = BinaryAssociation(
    name="interArrivalTime_OpenWorkload252",
    ends={
        Property(name="PCMRandomVariable253", type=pcm_usagemodel_OpenWorkload, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_usagemodel_OpenWorkload", type=PCMRandomVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
bodyBehaviour_Loop254: BinaryAssociation = BinaryAssociation(
    name="bodyBehaviour_Loop254",
    ends={
        Property(name="ScenarioBehaviour255", type=pcm_usagemodel_Loop, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_usagemodel_Loop", type=ScenarioBehaviour, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
loopIteration_Loop256: BinaryAssociation = BinaryAssociation(
    name="loopIteration_Loop256",
    ends={
        Property(name="PCMRandomVariable258", type=pcm_usagemodel_Loop, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_usagemodel_Loop257", type=PCMRandomVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
inputParameterUsages_EntryLevelSystemCall259: BinaryAssociation = BinaryAssociation(
    name="inputParameterUsages_EntryLevelSystemCall259",
    ends={
        Property(name="VariableUsage260", type=pcm_usagemodel_EntryLevelSystemCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_usagemodel_EntryLevelSystemCall", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
providedRole_EntryLevelSystemCall261: BinaryAssociation = BinaryAssociation(
    name="providedRole_EntryLevelSystemCall261",
    ends={
        Property(name="ProvidedRole263", type=pcm_usagemodel_EntryLevelSystemCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_usagemodel_EntryLevelSystemCall262", type=ProvidedRole, multiplicity=Multiplicity(1, 1))
    }
)
signature_EntryLevelSystemCall264: BinaryAssociation = BinaryAssociation(
    name="signature_EntryLevelSystemCall264",
    ends={
        Property(name="Signature266", type=pcm_usagemodel_EntryLevelSystemCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_usagemodel_EntryLevelSystemCall265", type=Signature, multiplicity=Multiplicity(1, 1))
    }
)
outputParameterUsages_EntryLevelSystemCall267: BinaryAssociation = BinaryAssociation(
    name="outputParameterUsages_EntryLevelSystemCall267",
    ends={
        Property(name="VariableUsage269", type=pcm_usagemodel_EntryLevelSystemCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_usagemodel_EntryLevelSystemCall268", type=VariableUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
branchTransitions_Branch272: BinaryAssociation = BinaryAssociation(
    name="branchTransitions_Branch272",
    ends={
        Property(name="BranchTransition", type=pcm_usagemodel_Branch, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_usagemodel_Branch", type=BranchTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
branchedBehaviour_BranchTransition273: BinaryAssociation = BinaryAssociation(
    name="branchedBehaviour_BranchTransition273",
    ends={
        Property(name="ScenarioBehaviour274", type=pcm_usagemodel_BranchTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_usagemodel_BranchTransition", type=ScenarioBehaviour, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
timeSpecification_Delay275: BinaryAssociation = BinaryAssociation(
    name="timeSpecification_Delay275",
    ends={
        Property(name="PCMRandomVariable276", type=pcm_usagemodel_Delay, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_usagemodel_Delay", type=PCMRandomVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thinkTime_ClosedWorkload270: BinaryAssociation = BinaryAssociation(
    name="thinkTime_ClosedWorkload270",
    ends={
        Property(name="PCMRandomVariable271", type=pcm_usagemodel_ClosedWorkload, multiplicity=Multiplicity(1, 1)),
        Property(name="pcm_usagemodel_ClosedWorkload", type=PCMRandomVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_pcm_entity_Entity_Identifier = Generalization(general=Identifier, specific=pcm_entity_Entity)
gen_pcm_entity_Entity_entity_NamedElement = Generalization(general=entity_NamedElement, specific=pcm_entity_Entity)
gen_pcm_entity_InterfaceProvidingEntity_Entity = Generalization(general=Entity, specific=pcm_entity_InterfaceProvidingEntity)
gen_pcm_entity_InterfaceProvidingRequiringEntity_entity_InterfaceProvidingEntity = Generalization(general=entity_InterfaceProvidingEntity, specific=pcm_entity_InterfaceProvidingRequiringEntity)
gen_pcm_entity_InterfaceProvidingRequiringEntity_entity_InterfaceRequiringEntity = Generalization(general=entity_InterfaceRequiringEntity, specific=pcm_entity_InterfaceProvidingRequiringEntity)
gen_pcm_entity_InterfaceRequiringEntity_Entity = Generalization(general=Entity, specific=pcm_entity_InterfaceRequiringEntity)
gen_pcm_core_PCMRandomVariable_RandomVariable = Generalization(general=RandomVariable, specific=pcm_core_PCMRandomVariable)
gen_pcm_composition_AssemblyContext_Entity = Generalization(general=Entity, specific=pcm_composition_AssemblyContext)
gen_pcm_composition_RequiredDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_composition_RequiredDelegationConnector)
gen_pcm_entity_ComposedProvidingRequiringEntity_composition_ComposedStructure = Generalization(general=composition_ComposedStructure, specific=pcm_entity_ComposedProvidingRequiringEntity)
gen_pcm_entity_ComposedProvidingRequiringEntity_entity_InterfaceProvidingRequiringEntity = Generalization(general=entity_InterfaceProvidingRequiringEntity, specific=pcm_entity_ComposedProvidingRequiringEntity)
gen_pcm_connectors_Connector_Entity = Generalization(general=Entity, specific=pcm_connectors_Connector)
gen_pcm_composition_ProvidedDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=pcm_composition_ProvidedDelegationConnector)
gen_pcm_composition_ComposedStructure_Entity = Generalization(general=Entity, specific=pcm_composition_ComposedStructure)
gen_pcm_repository_PassiveResource_Entity = Generalization(general=Entity, specific=pcm_repository_PassiveResource)
gen_pcm_composition_AssemblyConnector_connectors_Connector = Generalization(general=connectors_Connector, specific=pcm_composition_AssemblyConnector)
gen_pcm_composition_AssemblyConnector_entity_Entity = Generalization(general=entity_Entity, specific=pcm_composition_AssemblyConnector)
gen_pcm_repository_Repository_Entity = Generalization(general=Entity, specific=pcm_repository_Repository)
gen_pcm_repository_ProvidesComponentType_entity_Entity = Generalization(general=entity_Entity, specific=pcm_repository_ProvidesComponentType)
gen_pcm_repository_ProvidesComponentType_entity_InterfaceProvidingRequiringEntity = Generalization(general=entity_InterfaceProvidingRequiringEntity, specific=pcm_repository_ProvidesComponentType)
gen_pcm_repository_Role_Entity = Generalization(general=Entity, specific=pcm_repository_Role)
gen_pcm_repository_Interface_Entity = Generalization(general=Entity, specific=pcm_repository_Interface)
gen_pcm_repository_ImplementationComponentType_CompleteComponentType = Generalization(general=CompleteComponentType, specific=pcm_repository_ImplementationComponentType)
gen_pcm_repository_RequiredRole_Role = Generalization(general=Role, specific=pcm_repository_RequiredRole)
gen_pcm_repository_CompleteComponentType_ProvidesComponentType = Generalization(general=ProvidesComponentType, specific=pcm_repository_CompleteComponentType)
gen_pcm_repository_DelegationConnector_Connector = Generalization(general=Connector, specific=pcm_repository_DelegationConnector)
gen_pcm_repository_CompositeComponent_repository_ImplementationComponentType = Generalization(general=repository_ImplementationComponentType, specific=pcm_repository_CompositeComponent)
gen_pcm_repository_CompositeComponent_entity_ComposedProvidingRequiringEntity = Generalization(general=entity_ComposedProvidingRequiringEntity, specific=pcm_repository_CompositeComponent)
gen_pcm_repository_PrimitiveDataType_DataType = Generalization(general=DataType, specific=pcm_repository_PrimitiveDataType)
gen_pcm_repository_CollectionDataType_entity_Entity = Generalization(general=entity_Entity, specific=pcm_repository_CollectionDataType)
gen_pcm_repository_CollectionDataType_repository_DataType = Generalization(general=repository_DataType, specific=pcm_repository_CollectionDataType)
gen_pcm_repository_CompositeDataType_entity_Entity = Generalization(general=entity_Entity, specific=pcm_repository_CompositeDataType)
gen_pcm_repository_BasicComponent_ImplementationComponentType = Generalization(general=ImplementationComponentType, specific=pcm_repository_BasicComponent)
gen_pcm_repository_ProvidedRole_Role = Generalization(general=Role, specific=pcm_repository_ProvidedRole)
gen_pcm_parameter_CharacterisedVariable_Variable = Generalization(general=Variable, specific=pcm_parameter_CharacterisedVariable)
gen_pcm_seff_StopAction_AbstractResourceDemandingAction = Generalization(general=AbstractResourceDemandingAction, specific=pcm_seff_StopAction)
gen_pcm_repository_CompositeDataType_repository_DataType = Generalization(general=repository_DataType, specific=pcm_repository_CompositeDataType)
gen_pcm_repository_InnerDeclaration_NamedElement = Generalization(general=NamedElement, specific=pcm_repository_InnerDeclaration)
gen_pcm_seff_AbstractAction_Entity = Generalization(general=Entity, specific=pcm_seff_AbstractAction)
gen_pcm_seff_StartAction_AbstractResourceDemandingAction = Generalization(general=AbstractResourceDemandingAction, specific=pcm_seff_StartAction)
gen_pcm_seff_ResourceDemandingSEFF_Identifier = Generalization(general=Identifier, specific=pcm_seff_ResourceDemandingSEFF)
gen_pcm_seff_ResourceDemandingSEFF_seff_ServiceEffectSpecification = Generalization(general=seff_ServiceEffectSpecification, specific=pcm_seff_ResourceDemandingSEFF)
gen_pcm_seff_ResourceDemandingSEFF_seff_ResourceDemandingBehaviour = Generalization(general=seff_ResourceDemandingBehaviour, specific=pcm_seff_ResourceDemandingSEFF)
gen_pcm_seff_AbstractResourceDemandingAction_AbstractAction = Generalization(general=AbstractAction, specific=pcm_seff_AbstractResourceDemandingAction)
gen_pcm_seff_ReleaseAction_AbstractResourceDemandingAction = Generalization(general=AbstractResourceDemandingAction, specific=pcm_seff_ReleaseAction)
gen_pcm_seff_LoopAction_AbstractLoopAction = Generalization(general=AbstractLoopAction, specific=pcm_seff_LoopAction)
gen_pcm_seff_AbstractLoopAction_AbstractResourceDemandingAction = Generalization(general=AbstractResourceDemandingAction, specific=pcm_seff_AbstractLoopAction)
gen_pcm_seff_InternalAction_AbstractResourceDemandingAction = Generalization(general=AbstractResourceDemandingAction, specific=pcm_seff_InternalAction)
gen_pcm_seff_ForkedBehaviour_ResourceDemandingBehaviour = Generalization(general=ResourceDemandingBehaviour, specific=pcm_seff_ForkedBehaviour)
gen_pcm_seff_ExternalCallAction_AbstractAction = Generalization(general=AbstractAction, specific=pcm_seff_ExternalCallAction)
gen_pcm_seff_ProbabilisticBranchTransition_AbstractBranchTransition = Generalization(general=AbstractBranchTransition, specific=pcm_seff_ProbabilisticBranchTransition)
gen_pcm_seff_AbstractBranchTransition_Identifier = Generalization(general=Identifier, specific=pcm_seff_AbstractBranchTransition)
gen_pcm_seff_BranchAction_AbstractResourceDemandingAction = Generalization(general=AbstractResourceDemandingAction, specific=pcm_seff_BranchAction)
gen_pcm_seff_ForkAction_AbstractResourceDemandingAction = Generalization(general=AbstractResourceDemandingAction, specific=pcm_seff_ForkAction)
gen_pcm_seff_CollectionIteratorAction_AbstractLoopAction = Generalization(general=AbstractLoopAction, specific=pcm_seff_CollectionIteratorAction)
gen_pcm_seff_GuardedBranchTransition_AbstractBranchTransition = Generalization(general=AbstractBranchTransition, specific=pcm_seff_GuardedBranchTransition)
gen_pcm_seff_SetVariableAction_AbstractResourceDemandingAction = Generalization(general=AbstractResourceDemandingAction, specific=pcm_seff_SetVariableAction)
gen_pcm_resourcetype_ResourceType_entity_Entity = Generalization(general=entity_Entity, specific=pcm_resourcetype_ResourceType)
gen_pcm_resourcetype_ResourceType_UnitCarryingElement = Generalization(general=UnitCarryingElement, specific=pcm_resourcetype_ResourceType)
gen_pcm_resourcetype_CommunicationLinkResourceType_ProcessingResourceType = Generalization(general=ProcessingResourceType, specific=pcm_resourcetype_CommunicationLinkResourceType)
gen_pcm_resourcetype_ProcessingResourceType_ResourceType = Generalization(general=ResourceType, specific=pcm_resourcetype_ProcessingResourceType)
gen_pcm_allocation_AllocationContext_Entity = Generalization(general=Entity, specific=pcm_allocation_AllocationContext)
gen_pcm_allocation_Allocation_Entity = Generalization(general=Entity, specific=pcm_allocation_Allocation)
gen_pcm_seff_AcquireAction_AbstractResourceDemandingAction = Generalization(general=AbstractResourceDemandingAction, specific=pcm_seff_AcquireAction)
gen_pcm_resourceenvironment_LinkingResource_Entity = Generalization(general=Entity, specific=pcm_resourceenvironment_LinkingResource)
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
gen_pcm_usagemodel_Loop_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_usagemodel_Loop)
gen_pcm_usagemodel_EntryLevelSystemCall_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_usagemodel_EntryLevelSystemCall)
gen_pcm_usagemodel_ClosedWorkload_Workload = Generalization(general=Workload, specific=pcm_usagemodel_ClosedWorkload)
gen_pcm_usagemodel_OpenWorkload_Workload = Generalization(general=Workload, specific=pcm_usagemodel_OpenWorkload)
gen_pcm_usagemodel_Delay_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_usagemodel_Delay)
gen_pcm_usagemodel_Branch_AbstractUserAction = Generalization(general=AbstractUserAction, specific=pcm_usagemodel_Branch)

# Domain Model
domain_model = DomainModel(
    name="pcm",
    types={pcm_entity_Entity, Identifier, entity_NamedElement, pcm_entity_NamedElement, pcm_entity_InterfaceProvidingEntity, Entity, ProvidedRole, pcm_entity_InterfaceProvidingRequiringEntity, entity_InterfaceProvidingEntity, entity_InterfaceRequiringEntity, pcm_entity_InterfaceRequiringEntity, RequiredRole, pcm_core_PCMRandomVariable, RandomVariable, pcm_composition_AssemblyContext, ProvidesComponentType, VariableUsage, pcm_composition_RequiredDelegationConnector, pcm_entity_ComposedProvidingRequiringEntity, composition_ComposedStructure, entity_InterfaceProvidingRequiringEntity, pcm_connectors_Connector, pcm_composition_ProvidedDelegationConnector, DelegationConnector, pcm_composition_ComposedStructure, composition_AssemblyContext, composition_ProvidedDelegationConnector, composition_RequiredDelegationConnector, composition_AssemblyConnector, pcm_repository_PassiveResource, PCMRandomVariable, pcm_composition_AssemblyConnector, connectors_Connector, entity_Entity, DataType, ExceptionType, pcm_repository_Parameter, Signature, pcm_repository_DataType, Repository, pcm_repository_Repository, pcm_repository_ProvidesComponentType, pcm_repository_Signature, Parameter_, Interface, pcm_repository_Role, pcm_repository_Interface, Protocol, pcm_repository_ExceptionType, pcm_repository_ImplementationComponentType, CompleteComponentType, pcm_repository_RequiredRole, Role, pcm_repository_CompleteComponentType, pcm_repository_DelegationConnector, Connector, pcm_repository_CompositeComponent, repository_ImplementationComponentType, entity_ComposedProvidingRequiringEntity, ServiceEffectSpecification, PassiveResource, pcm_repository_PrimitiveDataType, pcm_repository_CollectionDataType, repository_DataType, pcm_repository_CompositeDataType, ImplementationComponentType, pcm_repository_BasicComponent, pcm_repository_ProvidedRole, pcm_protocol_ServiceCall, pcm_protocol_Protocol, pcm_parameter_VariableCharacterisation, pcm_parameter_CharacterisedVariable, Variable, pcm_parameter_VariableUsage, VariableCharacterisation, parameter_pcm_AbstractNamedReference, pcm_seff_StopAction, AbstractResourceDemandingAction, CompositeDataType, InnerDeclaration, pcm_repository_InnerDeclaration, ParametricResourceDemand, NamedElement, pcm_seff_AbstractAction, pcm_seff_ParametricResourceDemand, ProcessingResourceType, pcm_seff_StartAction, pcm_seff_ResourceDemandingSEFF, seff_ServiceEffectSpecification, seff_ResourceDemandingBehaviour, pcm_seff_AbstractResourceDemandingAction, AbstractAction, pcm_seff_ResourceDemandingBehaviour, pcm_seff_ReleaseAction, pcm_seff_LoopAction, AbstractLoopAction, pcm_seff_AbstractLoopAction, ResourceDemandingBehaviour, pcm_seff_InternalAction, SynchronisationPoint, pcm_seff_ForkedBehaviour, pcm_seff_SynchronisationPoint, pcm_seff_ExternalCallAction, pcm_seff_ProbabilisticBranchTransition, AbstractBranchTransition, pcm_seff_AbstractBranchTransition, pcm_seff_BranchAction, pcm_seff_ForkAction, ForkedBehaviour, pcm_seff_CollectionIteratorAction, pcm_seff_GuardedBranchTransition, pcm_seff_SetVariableAction, pcm_seff_ServiceEffectSpecification, pcm_resourcetype_ResourceType, UnitCarryingElement, pcm_resourcetype_ResourceRepository, ResourceType, pcm_resourcetype_CommunicationLinkResourceType, pcm_resourcetype_ProcessingResourceType, pcm_allocation_AllocationContext, ResourceContainer, pcm_allocation_Allocation, AllocationContext, ResourceEnvironment, pcm_seff_AcquireAction, pcm_resourceenvironment_ResourceEnvironment, LinkingResource, pcm_resourceenvironment_LinkingResource, CommunicationLinkResourceSpecification, pcm_resourceenvironment_CommunicationLinkResourceSpecification, CommunicationLinkResourceType, pcm_resourceenvironment_ProcessingResourceSpecification, pcm_resourceenvironment_ResourceContainer, ProcessingResourceSpecification, pcm_system_System, pcm_qosannotations_SpecifiedFailureProbability, System, pcm_qosannotations_SystemSpecifiedExecutionTime, SpecifiedExecutionTime, pcm_qosannotations_ComponentSpecifiedExecutionTime, pcm_qosannotations_SpecifiedOutputParameterAbstraction, pcm_qosannotations_QoSAnnotations, SpecifiedOutputParameterAbstraction, pcm_usagemodel_Workload, pcm_usagemodel_UsageScenario, Workload, ScenarioBehaviour, pcm_usagemodel_ScenarioBehaviour, QoSAnnotations, pcm_qosannotations_SpecifiedExecutionTime, AbstractUserAction, pcm_usagemodel_AbstractUserAction, pcm_usagemodel_UsageModel, UsageScenario, UserData, pcm_usagemodel_UserData, pcm_usagemodel_Stop, pcm_usagemodel_Start, pcm_usagemodel_Loop, pcm_usagemodel_EntryLevelSystemCall, pcm_usagemodel_ClosedWorkload, pcm_usagemodel_OpenWorkload, BranchTransition, pcm_usagemodel_BranchTransition, pcm_usagemodel_Delay, pcm_usagemodel_Branch, ParameterModifier, PrimitiveTypeEnum, VariableCharacterisationType, SchedulingPolicy},
    associations={providedRoles_InterfaceProvidingEntity0, requiredRoles_InterfaceRequiringEntity1, parentStructure_ProvidedDelegationConnector10, encapsulatedComponent_ChildComponentContext11, parentStructure_AssemblyContext12, configParameterUsages_AssemblyContext15, innerProvidedRole_ProvidedDelegationConnector3, outerProvidedRole_ProvidedDelegationConnector5, childComponentContexts_ComposedStructure42, childComponentContext_ProvidedDelegationConnector8, providedDelegationConnectors_ComposedStructure45, requiredDelegationConnectors_ComposedStructure48, compositeAssemblyConnectors_ComposedStructure51, capacity_PassiveResource54, innerRequiredRole_RequiredDelegationConnector17, outerRequiredRole_RequiredDelegationConnector19, childComponentContext_RequiredDelegationConnector22, parentStructure_RequiredDelegationConnector25, requiringChildComponentContext_CompositeAssemblyConnector28, providingChildComponentContext_CompositeAssemblyConnector30, providedRole_CompositeAssemblyConnector33, requiredRole_CompositeAssemblyConnector36, parentStructure_AssemblyConnector39, returntype__Signature59, exceptions__Signature60, datatype__Parameter62, signature_Parameter64, repository_DataType66, components__Repository68, interfaces__Repository71, datatypes_Repository74, parameters__Signature55, interface_Signature57, requiringEntity_RequiredRole82, parentInterface__Interface84, anchestorInterfaces_Interface86, protocols__Interface89, signatures__Interface91, repository_Interface94, repository_ProvidesComponentType77, requiredInterface__RequiredRole80, parentCompleteComponentTypes97, componentParameterUsage_ImplementationComponentType98, parentProvidesComponentTypes101, implementationComponentType104, serviceEffectSpecifications__BasicComponent106, passiveResource_BasicComponent108, innerType_CollectionDataType110, implementationComponentType103, datatype_InnerDeclaration115, providedInterface__ProvidedRole117, providingEntity_ProvidedRole119, signature__ServiceCall122, specification_VariableCharacterisation124, variableCharacterisation_VariableUsage126, namedReference_VariableUsage127, parentType_CompositeDataType112, innerDeclaration_CompositeDataType113, resourceDemand_Action129, predecessor_AbstractAction130, successor_AbstractAction132, requiredResource_ParametricResourceDemand135, specification_ParametericResourceDemand136, action_ParametricResourceDemand139, steps_Behaviour141, passiveResource_ReleaseAction143, iterationCount_LoopAction145, bodyBehaviour_Loop147, synchronisingBehaviours_ForkAction149, synchronousForkedBehaviours_SynchronisationPoint151, outputParameterUsage_SynchronisationPoint153, calledService_ExternalService156, inputParameterUsages_ExternalCallAction158, outputVariableUsages_ExternalCallAction161, role_ExternalService164, branchBehaviour_BranchTransition166, asynchronousForkedBehaviours_ForkAction148, parameter_CollectionIteratorAction171, branchCondition_GuardedBranchTransition173, localVariableUsages_SetVariableAction175, describedService__SEFF177, availableResourceTypes_ResourceRepository179, resourceContainer_AllocationContext180, assemblyContext_AllocationContext181, allocationContexts_Allocation184, branches_Branch168, passiveresource_AcquireAction169, linkingresource189, resourceContainer_ResourceEnvironment190, toResourceContainer_LinkingResource193, fromResourceContainer_LinkingResource195, communicationLinkResourceSpecifications_LinkingResource198, communicationLinkResourceType_CommunicationLinkResourceSpecification200, latency_CommunicationLinkResourceSpecification201, throughput_CommunicationLinkResourceSpecification204, activeResourceType_ActiveResourceSpecification207, processingRate_ProcessingResourceSpecification209, activeResourceSpecifications_ResourceContainer212, targetResourceEnvironment_Allocation185, system_Allocation187, assemblyContext_ComponentSpecifiedExecutionTime222, signature_SpecifiedOutputParameterAbstraction224, role_SpecifiedOutputParameterAbstraction226, expectedExternalOutputs_SpecifiedOutputParameterAbstraction229, specifiedExecutionTimes_QoSAnnotations232, specifiedOutputParameterAbstractions_QoSAnnotations233, workload_UsageScenario235, scenarioBehaviour_UsageScenario236, qosAnnotations_System213, signature_SpecifiedTimeConsumption214, role_SpecifiedExecutionTime216, specification_SpecifiedExecutionTime219, actions_ScenarioBehaviour238, successor239, predecessor241, usageScenario_UsageModel244, userData_UsageModel245, userDataParameterUsages_UserData247, assemblyContext_userData249, interArrivalTime_OpenWorkload252, bodyBehaviour_Loop254, loopIteration_Loop256, inputParameterUsages_EntryLevelSystemCall259, providedRole_EntryLevelSystemCall261, signature_EntryLevelSystemCall264, outputParameterUsages_EntryLevelSystemCall267, branchTransitions_Branch272, branchedBehaviour_BranchTransition273, timeSpecification_Delay275, thinkTime_ClosedWorkload270},
    generalizations={gen_pcm_entity_Entity_Identifier, gen_pcm_entity_Entity_entity_NamedElement, gen_pcm_entity_InterfaceProvidingEntity_Entity, gen_pcm_entity_InterfaceProvidingRequiringEntity_entity_InterfaceProvidingEntity, gen_pcm_entity_InterfaceProvidingRequiringEntity_entity_InterfaceRequiringEntity, gen_pcm_entity_InterfaceRequiringEntity_Entity, gen_pcm_core_PCMRandomVariable_RandomVariable, gen_pcm_composition_AssemblyContext_Entity, gen_pcm_composition_RequiredDelegationConnector_DelegationConnector, gen_pcm_entity_ComposedProvidingRequiringEntity_composition_ComposedStructure, gen_pcm_entity_ComposedProvidingRequiringEntity_entity_InterfaceProvidingRequiringEntity, gen_pcm_connectors_Connector_Entity, gen_pcm_composition_ProvidedDelegationConnector_DelegationConnector, gen_pcm_composition_ComposedStructure_Entity, gen_pcm_repository_PassiveResource_Entity, gen_pcm_composition_AssemblyConnector_connectors_Connector, gen_pcm_composition_AssemblyConnector_entity_Entity, gen_pcm_repository_Repository_Entity, gen_pcm_repository_ProvidesComponentType_entity_Entity, gen_pcm_repository_ProvidesComponentType_entity_InterfaceProvidingRequiringEntity, gen_pcm_repository_Role_Entity, gen_pcm_repository_Interface_Entity, gen_pcm_repository_ImplementationComponentType_CompleteComponentType, gen_pcm_repository_RequiredRole_Role, gen_pcm_repository_CompleteComponentType_ProvidesComponentType, gen_pcm_repository_DelegationConnector_Connector, gen_pcm_repository_CompositeComponent_repository_ImplementationComponentType, gen_pcm_repository_CompositeComponent_entity_ComposedProvidingRequiringEntity, gen_pcm_repository_PrimitiveDataType_DataType, gen_pcm_repository_CollectionDataType_entity_Entity, gen_pcm_repository_CollectionDataType_repository_DataType, gen_pcm_repository_CompositeDataType_entity_Entity, gen_pcm_repository_BasicComponent_ImplementationComponentType, gen_pcm_repository_ProvidedRole_Role, gen_pcm_parameter_CharacterisedVariable_Variable, gen_pcm_seff_StopAction_AbstractResourceDemandingAction, gen_pcm_repository_CompositeDataType_repository_DataType, gen_pcm_repository_InnerDeclaration_NamedElement, gen_pcm_seff_AbstractAction_Entity, gen_pcm_seff_StartAction_AbstractResourceDemandingAction, gen_pcm_seff_ResourceDemandingSEFF_Identifier, gen_pcm_seff_ResourceDemandingSEFF_seff_ServiceEffectSpecification, gen_pcm_seff_ResourceDemandingSEFF_seff_ResourceDemandingBehaviour, gen_pcm_seff_AbstractResourceDemandingAction_AbstractAction, gen_pcm_seff_ReleaseAction_AbstractResourceDemandingAction, gen_pcm_seff_LoopAction_AbstractLoopAction, gen_pcm_seff_AbstractLoopAction_AbstractResourceDemandingAction, gen_pcm_seff_InternalAction_AbstractResourceDemandingAction, gen_pcm_seff_ForkedBehaviour_ResourceDemandingBehaviour, gen_pcm_seff_ExternalCallAction_AbstractAction, gen_pcm_seff_ProbabilisticBranchTransition_AbstractBranchTransition, gen_pcm_seff_AbstractBranchTransition_Identifier, gen_pcm_seff_BranchAction_AbstractResourceDemandingAction, gen_pcm_seff_ForkAction_AbstractResourceDemandingAction, gen_pcm_seff_CollectionIteratorAction_AbstractLoopAction, gen_pcm_seff_GuardedBranchTransition_AbstractBranchTransition, gen_pcm_seff_SetVariableAction_AbstractResourceDemandingAction, gen_pcm_resourcetype_ResourceType_entity_Entity, gen_pcm_resourcetype_ResourceType_UnitCarryingElement, gen_pcm_resourcetype_CommunicationLinkResourceType_ProcessingResourceType, gen_pcm_resourcetype_ProcessingResourceType_ResourceType, gen_pcm_allocation_AllocationContext_Entity, gen_pcm_allocation_Allocation_Entity, gen_pcm_seff_AcquireAction_AbstractResourceDemandingAction, gen_pcm_resourceenvironment_LinkingResource_Entity, gen_pcm_resourceenvironment_ResourceContainer_Entity, gen_pcm_system_System_entity_Entity, gen_pcm_system_System_entity_ComposedProvidingRequiringEntity, gen_pcm_qosannotations_SystemSpecifiedExecutionTime_SpecifiedExecutionTime, gen_pcm_qosannotations_ComponentSpecifiedExecutionTime_SpecifiedExecutionTime, gen_pcm_qosannotations_QoSAnnotations_Entity, gen_pcm_usagemodel_UsageScenario_Entity, gen_pcm_usagemodel_ScenarioBehaviour_Entity, gen_pcm_usagemodel_AbstractUserAction_Entity, gen_pcm_usagemodel_Stop_AbstractUserAction, gen_pcm_usagemodel_Start_AbstractUserAction, gen_pcm_usagemodel_Loop_AbstractUserAction, gen_pcm_usagemodel_EntryLevelSystemCall_AbstractUserAction, gen_pcm_usagemodel_ClosedWorkload_Workload, gen_pcm_usagemodel_OpenWorkload_Workload, gen_pcm_usagemodel_Delay_AbstractUserAction, gen_pcm_usagemodel_Branch_AbstractUserAction},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)