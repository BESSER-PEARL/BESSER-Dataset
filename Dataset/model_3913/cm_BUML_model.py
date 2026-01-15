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
PrimitiveType: Enumeration = Enumeration(
    name="PrimitiveType",
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

# Classes
cm_repository_BasicComponent = Class(name="cm::repository::BasicComponent")
ComponentTypeImplementation = Class(name="ComponentTypeImplementation")
cm_repository_ComponentType = Class(name="cm::repository::ComponentType")
cm_repository_ProvidedRole = Class(name="cm::repository::ProvidedRole")
Role = Class(name="Role")
InterfaceProvidingEntity = Class(name="InterfaceProvidingEntity")
Interface = Class(name="Interface")
cm_repository_Parameter = Class(name="cm::repository::Parameter")
DataType = Class(name="DataType")
Signature = Class(name="Signature")
cm_repository_DataType = Class(name="cm::repository::DataType", is_abstract=True)
ServiceEffectSpecification = Class(name="ServiceEffectSpecification")
cm_repository_ComponentTypeImplementation = Class(name="cm::repository::ComponentTypeImplementation", is_abstract=True)
RepositoryComponent = Class(name="RepositoryComponent")
ComponentType = Class(name="ComponentType")
cm_repository_RepositoryComponent = Class(name="cm::repository::RepositoryComponent", is_abstract=True)
InterfaceProvidingRequiringEntity = Class(name="InterfaceProvidingRequiringEntity")
Repository = Class(name="Repository")
cm_repository_Interface = Class(name="cm::repository::Interface")
cm_repository_Role = Class(name="cm::repository::Role", is_abstract=True)
Entity = Class(name="Entity")
cm_repository_Repository = Class(name="cm::repository::Repository")
cm_repository_ExceptionType = Class(name="cm::repository::ExceptionType")
cm_repository_RequiredRole = Class(name="cm::repository::RequiredRole")
InterfaceRequiringEntity = Class(name="InterfaceRequiringEntity")
cm_repository_CompositeComponent = Class(name="cm::repository::CompositeComponent")
composition_ComposedProvidingRequiringEntity = Class(name="composition::ComposedProvidingRequiringEntity")
repository_ComponentTypeImplementation = Class(name="repository::ComponentTypeImplementation")
cm_repository_Signature = Class(name="cm::repository::Signature")
ExceptionType = Class(name="ExceptionType")
Parameter_ = Class(name="Parameter")
cm_repository_PrimitiveDataType = Class(name="cm::repository::PrimitiveDataType")
cm_repository_CollectionDataType = Class(name="cm::repository::CollectionDataType")
composition_Entity = Class(name="composition::Entity")
repository_DataType = Class(name="repository::DataType")
cm_composition_DelegationConnector = Class(name="cm::composition::DelegationConnector", is_abstract=True)
Connector = Class(name="Connector")
cm_composition_Connector = Class(name="cm::composition::Connector", is_abstract=True)
ComposedStructure = Class(name="ComposedStructure")
cm_composition_ComposedStructure = Class(name="cm::composition::ComposedStructure", is_abstract=True)
AssemblyContext = Class(name="AssemblyContext")
cm_composition_ProvidedDelegationConnector = Class(name="cm::composition::ProvidedDelegationConnector")
DelegationConnector = Class(name="DelegationConnector")
cm_repository_CompositeDataType = Class(name="cm::repository::CompositeDataType")
CompositeDataType = Class(name="CompositeDataType")
InnerDeclaration = Class(name="InnerDeclaration")
cm_repository_InnerDeclaration = Class(name="cm::repository::InnerDeclaration")
NamedElement = Class(name="NamedElement")
cm_composition_AssemblyConnector = Class(name="cm::composition::AssemblyConnector")
cm_composition_AssemblyContext = Class(name="cm::composition::AssemblyContext")
cm_composition_System = Class(name="cm::composition::System")
ProvidedRole = Class(name="ProvidedRole")
cm_composition_RequiredDelegationConnector = Class(name="cm::composition::RequiredDelegationConnector")
RequiredRole = Class(name="RequiredRole")
cm_composition_ComposedProvidingRequiringEntity = Class(name="cm::composition::ComposedProvidingRequiringEntity", is_abstract=True)
composition_ComposedStructure = Class(name="composition::ComposedStructure")
composition_InterfaceProvidingRequiringEntity = Class(name="composition::InterfaceProvidingRequiringEntity")
cm_composition_NamedElement = Class(name="cm::composition::NamedElement", is_abstract=True)
cm_composition_Entity = Class(name="cm::composition::Entity", is_abstract=True)
composition_NamedElement = Class(name="composition::NamedElement")
composition_Identifier = Class(name="composition::Identifier")
cm_composition_Identifier = Class(name="cm::composition::Identifier", is_abstract=True)
cm_seff_ServiceEffectSpecification = Class(name="cm::seff::ServiceEffectSpecification", is_abstract=True)
BasicComponent = Class(name="BasicComponent")
cm_composition_SubSystem = Class(name="cm::composition::SubSystem")
repository_RepositoryComponent = Class(name="repository::RepositoryComponent")
cm_composition_InterfaceProvidingRequiringEntity = Class(name="cm::composition::InterfaceProvidingRequiringEntity", is_abstract=True)
composition_InterfaceProvidingEntity = Class(name="composition::InterfaceProvidingEntity")
composition_InterfaceRequiringEntity = Class(name="composition::InterfaceRequiringEntity")
cm_composition_InterfaceProvidingEntity = Class(name="cm::composition::InterfaceProvidingEntity", is_abstract=True)
cm_composition_InterfaceRequiringEntity = Class(name="cm::composition::InterfaceRequiringEntity", is_abstract=True)
cm_seff_StartAction = Class(name="cm::seff::StartAction")
cm_seff_StopAction = Class(name="cm::seff::StopAction")
cm_seff_ExternalCallAction = Class(name="cm::seff::ExternalCallAction")
cm_seff_BranchAction = Class(name="cm::seff::BranchAction")
cm_seff_ProbabilisticBranchTransition = Class(name="cm::seff::ProbabilisticBranchTransition")
seff_Automaton = Class(name="seff::Automaton")
BranchAction = Class(name="BranchAction")
cm_seff_SimpleBehaviorSpecification = Class(name="cm::seff::SimpleBehaviorSpecification")
seff_ServiceEffectSpecification = Class(name="seff::ServiceEffectSpecification")
cm_seff_InternalAction = Class(name="cm::seff::InternalAction")
cm_seff_Automaton = Class(name="cm::seff::Automaton", is_abstract=True)
InternalBehaviour = Class(name="InternalBehaviour")
cm_seff_InternalBehaviour = Class(name="cm::seff::InternalBehaviour")
ProbabilisticBranchTransition = Class(name="ProbabilisticBranchTransition")
AbstractAction = Class(name="AbstractAction")
cm_seff_AbstractAction = Class(name="cm::seff::AbstractAction", is_abstract=True)
Automaton = Class(name="Automaton")

# cm_repository_BasicComponent class attributes and methods

# ComponentTypeImplementation class attributes and methods

# cm_repository_ComponentType class attributes and methods

# cm_repository_ProvidedRole class attributes and methods

# Role class attributes and methods

# InterfaceProvidingEntity class attributes and methods

# Interface class attributes and methods

# cm_repository_Parameter class attributes and methods
cm_repository_Parameter_name: Property = Property(name="name", type=StringType)
cm_repository_Parameter.attributes={cm_repository_Parameter_name}

# DataType class attributes and methods

# Signature class attributes and methods

# cm_repository_DataType class attributes and methods

# ServiceEffectSpecification class attributes and methods

# cm_repository_ComponentTypeImplementation class attributes and methods

# RepositoryComponent class attributes and methods

# ComponentType class attributes and methods

# cm_repository_RepositoryComponent class attributes and methods

# InterfaceProvidingRequiringEntity class attributes and methods

# Repository class attributes and methods

# cm_repository_Interface class attributes and methods

# cm_repository_Role class attributes and methods

# Entity class attributes and methods

# cm_repository_Repository class attributes and methods
cm_repository_Repository_description: Property = Property(name="description", type=StringType)
cm_repository_Repository.attributes={cm_repository_Repository_description}

# cm_repository_ExceptionType class attributes and methods
cm_repository_ExceptionType_name: Property = Property(name="name", type=StringType)
cm_repository_ExceptionType_message: Property = Property(name="message", type=StringType)
cm_repository_ExceptionType.attributes={cm_repository_ExceptionType_message, cm_repository_ExceptionType_name}

# cm_repository_RequiredRole class attributes and methods

# InterfaceRequiringEntity class attributes and methods

# cm_repository_CompositeComponent class attributes and methods
cm_repository_CompositeComponent_m_ProvideSameInterfaces: Method = Method(name="ProvideSameInterfaces", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
cm_repository_CompositeComponent_m_RequireSameInterfaces: Method = Method(name="RequireSameInterfaces", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
cm_repository_CompositeComponent.methods={cm_repository_CompositeComponent_m_ProvideSameInterfaces, cm_repository_CompositeComponent_m_RequireSameInterfaces}

# composition_ComposedProvidingRequiringEntity class attributes and methods

# repository_ComponentTypeImplementation class attributes and methods

# cm_repository_Signature class attributes and methods

# ExceptionType class attributes and methods

# Parameter class attributes and methods

# cm_repository_PrimitiveDataType class attributes and methods
cm_repository_PrimitiveDataType_type: Property = Property(name="type", type=StringType)
cm_repository_PrimitiveDataType.attributes={cm_repository_PrimitiveDataType_type}

# cm_repository_CollectionDataType class attributes and methods

# composition_Entity class attributes and methods

# repository_DataType class attributes and methods

# cm_composition_DelegationConnector class attributes and methods

# Connector class attributes and methods

# cm_composition_Connector class attributes and methods

# ComposedStructure class attributes and methods

# cm_composition_ComposedStructure class attributes and methods
cm_composition_ComposedStructure_m_MultipleConnectorsConstraint: Method = Method(name="MultipleConnectorsConstraint", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
cm_composition_ComposedStructure_m_MultipleConnectorsConstraintForAssemblyConnectors: Method = Method(name="MultipleConnectorsConstraintForAssemblyConnectors", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
cm_composition_ComposedStructure.methods={cm_composition_ComposedStructure_m_MultipleConnectorsConstraintForAssemblyConnectors, cm_composition_ComposedStructure_m_MultipleConnectorsConstraint}

# AssemblyContext class attributes and methods

# cm_composition_ProvidedDelegationConnector class attributes and methods
cm_composition_ProvidedDelegationConnector_m_ComponentOfAssemblyContextAndInnerRoleProvidingComponentNeedToBeTheSame: Method = Method(name="ComponentOfAssemblyContextAndInnerRoleProvidingComponentNeedToBeTheSame", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
cm_composition_ProvidedDelegationConnector_m_ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure: Method = Method(name="ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
cm_composition_ProvidedDelegationConnector.methods={cm_composition_ProvidedDelegationConnector_m_ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure, cm_composition_ProvidedDelegationConnector_m_ComponentOfAssemblyContextAndInnerRoleProvidingComponentNeedToBeTheSame}

# DelegationConnector class attributes and methods

# cm_repository_CompositeDataType class attributes and methods

# CompositeDataType class attributes and methods

# InnerDeclaration class attributes and methods

# cm_repository_InnerDeclaration class attributes and methods

# NamedElement class attributes and methods

# cm_composition_AssemblyConnector class attributes and methods
cm_composition_AssemblyConnector_m_AssemblyConnectorsReferencedProvidedRolesAndChildContextMustMatch: Method = Method(name="AssemblyConnectorsReferencedProvidedRolesAndChildContextMustMatch", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
cm_composition_AssemblyConnector_m_AssemblyConnectorsReferencedInterfacesMustMatch: Method = Method(name="AssemblyConnectorsReferencedInterfacesMustMatch", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
cm_composition_AssemblyConnector_m_AssemblyConnectorsReferencedRequiredRoleAndChildContextMustMatch: Method = Method(name="AssemblyConnectorsReferencedRequiredRoleAndChildContextMustMatch", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
cm_composition_AssemblyConnector.methods={cm_composition_AssemblyConnector_m_AssemblyConnectorsReferencedInterfacesMustMatch, cm_composition_AssemblyConnector_m_AssemblyConnectorsReferencedProvidedRolesAndChildContextMustMatch, cm_composition_AssemblyConnector_m_AssemblyConnectorsReferencedRequiredRoleAndChildContextMustMatch}

# cm_composition_AssemblyContext class attributes and methods

# cm_composition_System class attributes and methods
cm_composition_System_m_SystemMustHaveAtLeastOneProvidedRole: Method = Method(name="SystemMustHaveAtLeastOneProvidedRole", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
cm_composition_System.methods={cm_composition_System_m_SystemMustHaveAtLeastOneProvidedRole}

# ProvidedRole class attributes and methods

# cm_composition_RequiredDelegationConnector class attributes and methods

# RequiredRole class attributes and methods

# cm_composition_ComposedProvidingRequiringEntity class attributes and methods

# composition_ComposedStructure class attributes and methods

# composition_InterfaceProvidingRequiringEntity class attributes and methods

# cm_composition_NamedElement class attributes and methods
cm_composition_NamedElement_entityName: Property = Property(name="entityName", type=StringType)
cm_composition_NamedElement.attributes={cm_composition_NamedElement_entityName}

# cm_composition_Entity class attributes and methods

# composition_NamedElement class attributes and methods

# composition_Identifier class attributes and methods

# cm_composition_Identifier class attributes and methods
cm_composition_Identifier_id: Property = Property(name="id", type=StringType)
cm_composition_Identifier_m_idHasToBeUnique: Method = Method(name="idHasToBeUnique", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
cm_composition_Identifier.attributes={cm_composition_Identifier_id}
cm_composition_Identifier.methods={cm_composition_Identifier_m_idHasToBeUnique}

# cm_seff_ServiceEffectSpecification class attributes and methods

# BasicComponent class attributes and methods

# cm_composition_SubSystem class attributes and methods

# repository_RepositoryComponent class attributes and methods

# cm_composition_InterfaceProvidingRequiringEntity class attributes and methods

# composition_InterfaceProvidingEntity class attributes and methods

# composition_InterfaceRequiringEntity class attributes and methods

# cm_composition_InterfaceProvidingEntity class attributes and methods

# cm_composition_InterfaceRequiringEntity class attributes and methods

# cm_seff_StartAction class attributes and methods

# cm_seff_StopAction class attributes and methods

# cm_seff_ExternalCallAction class attributes and methods

# cm_seff_BranchAction class attributes and methods

# cm_seff_ProbabilisticBranchTransition class attributes and methods
cm_seff_ProbabilisticBranchTransition_branchProbability: Property = Property(name="branchProbability", type=FloatType)
cm_seff_ProbabilisticBranchTransition.attributes={cm_seff_ProbabilisticBranchTransition_branchProbability}

# seff_Automaton class attributes and methods

# BranchAction class attributes and methods

# cm_seff_SimpleBehaviorSpecification class attributes and methods

# seff_ServiceEffectSpecification class attributes and methods

# cm_seff_InternalAction class attributes and methods

# cm_seff_Automaton class attributes and methods

# InternalBehaviour class attributes and methods

# cm_seff_InternalBehaviour class attributes and methods

# ProbabilisticBranchTransition class attributes and methods

# AbstractAction class attributes and methods

# cm_seff_AbstractAction class attributes and methods

# Automaton class attributes and methods

# Relationships
providingEntity3: BinaryAssociation = BinaryAssociation(
    name="providingEntity3",
    ends={
        Property(name="composition", type=cm_repository_ProvidedRole, multiplicity=Multiplicity(1, 1)),
        Property(name="InterfaceProvidingEntity", type=InterfaceProvidingEntity, multiplicity=Multiplicity(1, 1))
    }
)
providedInterface4: BinaryAssociation = BinaryAssociation(
    name="providedInterface4",
    ends={
        Property(name="Interface", type=cm_repository_ProvidedRole, multiplicity=Multiplicity(1, 1)),
        Property(name="cm_repository_ProvidedRole", type=Interface, multiplicity=Multiplicity(1, 1))
    }
)
dataType5: BinaryAssociation = BinaryAssociation(
    name="dataType5",
    ends={
        Property(name="DataType", type=cm_repository_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="cm_repository_Parameter", type=DataType, multiplicity=Multiplicity(1, 1))
    }
)
signature6: BinaryAssociation = BinaryAssociation(
    name="signature6",
    ends={
        Property(name="repository7", type=cm_repository_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="Signature", type=Signature, multiplicity=Multiplicity(0, 1))
    }
)
repository8: BinaryAssociation = BinaryAssociation(
    name="repository8",
    ends={
        Property(name="repository10", type=cm_repository_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="Repository9", type=Repository, multiplicity=Multiplicity(1, 1))
    }
)
serviceEffectSpecifications0: BinaryAssociation = BinaryAssociation(
    name="serviceEffectSpecifications0",
    ends={
        Property(name="seff", type=cm_repository_BasicComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="ServiceEffectSpecification", type=ServiceEffectSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
implementedComponentTypes1: BinaryAssociation = BinaryAssociation(
    name="implementedComponentTypes1",
    ends={
        Property(name="ComponentType", type=cm_repository_ComponentTypeImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="cm_repository_ComponentTypeImplementation", type=ComponentType, multiplicity=Multiplicity(0, 9999))
    }
)
repository2: BinaryAssociation = BinaryAssociation(
    name="repository2",
    ends={
        Property(name="repository", type=cm_repository_RepositoryComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="Repository", type=Repository, multiplicity=Multiplicity(1, 1))
    }
)
interfaces13: BinaryAssociation = BinaryAssociation(
    name="interfaces13",
    ends={
        Property(name="repository15", type=cm_repository_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="Interface14", type=Interface, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataTypes16: BinaryAssociation = BinaryAssociation(
    name="dataTypes16",
    ends={
        Property(name="repository18", type=cm_repository_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="DataType17", type=DataType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentInterfaces19: BinaryAssociation = BinaryAssociation(
    name="parentInterfaces19",
    ends={
        Property(name="Interface20", type=cm_repository_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="cm_repository_Interface", type=Interface, multiplicity=Multiplicity(0, 9999))
    }
)
repository21: BinaryAssociation = BinaryAssociation(
    name="repository21",
    ends={
        Property(name="repository23", type=cm_repository_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="Repository22", type=Repository, multiplicity=Multiplicity(1, 1))
    }
)
components11: BinaryAssociation = BinaryAssociation(
    name="components11",
    ends={
        Property(name="repository12", type=cm_repository_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="RepositoryComponent", type=RepositoryComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiringEntity36: BinaryAssociation = BinaryAssociation(
    name="requiringEntity36",
    ends={
        Property(name="composition37", type=cm_repository_RequiredRole, multiplicity=Multiplicity(1, 1)),
        Property(name="InterfaceRequiringEntity", type=InterfaceRequiringEntity, multiplicity=Multiplicity(1, 1))
    }
)
requiredInterface38: BinaryAssociation = BinaryAssociation(
    name="requiredInterface38",
    ends={
        Property(name="Interface39", type=cm_repository_RequiredRole, multiplicity=Multiplicity(1, 1)),
        Property(name="cm_repository_RequiredRole", type=Interface, multiplicity=Multiplicity(1, 1))
    }
)
signatures24: BinaryAssociation = BinaryAssociation(
    name="signatures24",
    ends={
        Property(name="repository26", type=cm_repository_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="Signature25", type=Signature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exceptions27: BinaryAssociation = BinaryAssociation(
    name="exceptions27",
    ends={
        Property(name="ExceptionType", type=cm_repository_Signature, multiplicity=Multiplicity(1, 1)),
        Property(name="cm_repository_Signature", type=ExceptionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters28: BinaryAssociation = BinaryAssociation(
    name="parameters28",
    ends={
        Property(name="repository29", type=cm_repository_Signature, multiplicity=Multiplicity(1, 1)),
        Property(name="Parameter", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnType30: BinaryAssociation = BinaryAssociation(
    name="returnType30",
    ends={
        Property(name="DataType32", type=cm_repository_Signature, multiplicity=Multiplicity(1, 1)),
        Property(name="cm_repository_Signature31", type=DataType, multiplicity=Multiplicity(0, 1))
    }
)
interface33: BinaryAssociation = BinaryAssociation(
    name="interface33",
    ends={
        Property(name="repository35", type=cm_repository_Signature, multiplicity=Multiplicity(1, 1)),
        Property(name="Interface34", type=Interface, multiplicity=Multiplicity(1, 1))
    }
)
innerType40: BinaryAssociation = BinaryAssociation(
    name="innerType40",
    ends={
        Property(name="DataType41", type=cm_repository_CollectionDataType, multiplicity=Multiplicity(1, 1)),
        Property(name="cm_repository_CollectionDataType", type=DataType, multiplicity=Multiplicity(1, 1))
    }
)
parentStructure50: BinaryAssociation = BinaryAssociation(
    name="parentStructure50",
    ends={
        Property(name="composition51", type=cm_composition_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="ComposedStructure", type=ComposedStructure, multiplicity=Multiplicity(1, 1))
    }
)
assemblyContexts52: BinaryAssociation = BinaryAssociation(
    name="assemblyContexts52",
    ends={
        Property(name="composition53", type=cm_composition_ComposedStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="AssemblyContext", type=AssemblyContext, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connectors54: BinaryAssociation = BinaryAssociation(
    name="connectors54",
    ends={
        Property(name="composition55", type=cm_composition_ComposedStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="Connector", type=Connector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentType42: BinaryAssociation = BinaryAssociation(
    name="parentType42",
    ends={
        Property(name="CompositeDataType", type=cm_repository_CompositeDataType, multiplicity=Multiplicity(1, 1)),
        Property(name="cm_repository_CompositeDataType", type=CompositeDataType, multiplicity=Multiplicity(0, 9999))
    }
)
innerDeclaration43: BinaryAssociation = BinaryAssociation(
    name="innerDeclaration43",
    ends={
        Property(name="repository44", type=cm_repository_CompositeDataType, multiplicity=Multiplicity(1, 1)),
        Property(name="InnerDeclaration", type=InnerDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataType45: BinaryAssociation = BinaryAssociation(
    name="dataType45",
    ends={
        Property(name="DataType46", type=cm_repository_InnerDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="cm_repository_InnerDeclaration", type=DataType, multiplicity=Multiplicity(1, 1))
    }
)
compositeDataType47: BinaryAssociation = BinaryAssociation(
    name="compositeDataType47",
    ends={
        Property(name="repository49", type=cm_repository_InnerDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="CompositeDataType48", type=CompositeDataType, multiplicity=Multiplicity(1, 1))
    }
)
requiringAssemblyContext70: BinaryAssociation = BinaryAssociation(
    name="requiringAssemblyContext70",
    ends={
        Property(name="AssemblyContext71", type=cm_composition_AssemblyConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="cm_composition_AssemblyConnector", type=AssemblyContext, multiplicity=Multiplicity(1, 1))
    }
)
providingAssemblyContext72: BinaryAssociation = BinaryAssociation(
    name="providingAssemblyContext72",
    ends={
        Property(name="AssemblyContext74", type=cm_composition_AssemblyConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="cm_composition_AssemblyConnector73", type=AssemblyContext, multiplicity=Multiplicity(1, 1))
    }
)
providedRole75: BinaryAssociation = BinaryAssociation(
    name="providedRole75",
    ends={
        Property(name="ProvidedRole77", type=cm_composition_AssemblyConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="cm_composition_AssemblyConnector76", type=ProvidedRole, multiplicity=Multiplicity(1, 1))
    }
)
requiredRole78: BinaryAssociation = BinaryAssociation(
    name="requiredRole78",
    ends={
        Property(name="RequiredRole80", type=cm_composition_AssemblyConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="cm_composition_AssemblyConnector79", type=RequiredRole, multiplicity=Multiplicity(1, 1))
    }
)
parentStructure81: BinaryAssociation = BinaryAssociation(
    name="parentStructure81",
    ends={
        Property(name="composition83", type=cm_composition_AssemblyContext, multiplicity=Multiplicity(1, 1)),
        Property(name="ComposedStructure82", type=ComposedStructure, multiplicity=Multiplicity(1, 1))
    }
)
encapsulatedComponent84: BinaryAssociation = BinaryAssociation(
    name="encapsulatedComponent84",
    ends={
        Property(name="RepositoryComponent85", type=cm_composition_AssemblyContext, multiplicity=Multiplicity(1, 1)),
        Property(name="cm_composition_AssemblyContext", type=RepositoryComponent, multiplicity=Multiplicity(1, 1))
    }
)
innerProvidedRole56: BinaryAssociation = BinaryAssociation(
    name="innerProvidedRole56",
    ends={
        Property(name="ProvidedRole", type=cm_composition_ProvidedDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="cm_composition_ProvidedDelegationConnector", type=ProvidedRole, multiplicity=Multiplicity(1, 1))
    }
)
outerProvidedRole57: BinaryAssociation = BinaryAssociation(
    name="outerProvidedRole57",
    ends={
        Property(name="ProvidedRole59", type=cm_composition_ProvidedDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="cm_composition_ProvidedDelegationConnector58", type=ProvidedRole, multiplicity=Multiplicity(1, 1))
    }
)
assemblyContext60: BinaryAssociation = BinaryAssociation(
    name="assemblyContext60",
    ends={
        Property(name="AssemblyContext62", type=cm_composition_ProvidedDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="cm_composition_ProvidedDelegationConnector61", type=AssemblyContext, multiplicity=Multiplicity(1, 1))
    }
)
innerRequiredRole63: BinaryAssociation = BinaryAssociation(
    name="innerRequiredRole63",
    ends={
        Property(name="RequiredRole", type=cm_composition_RequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="cm_composition_RequiredDelegationConnector", type=RequiredRole, multiplicity=Multiplicity(1, 1))
    }
)
outerRequiredRole64: BinaryAssociation = BinaryAssociation(
    name="outerRequiredRole64",
    ends={
        Property(name="RequiredRole66", type=cm_composition_RequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="cm_composition_RequiredDelegationConnector65", type=RequiredRole, multiplicity=Multiplicity(1, 1))
    }
)
assemblyContext67: BinaryAssociation = BinaryAssociation(
    name="assemblyContext67",
    ends={
        Property(name="AssemblyContext69", type=cm_composition_RequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="cm_composition_RequiredDelegationConnector68", type=AssemblyContext, multiplicity=Multiplicity(1, 1))
    }
)
describedService92: BinaryAssociation = BinaryAssociation(
    name="describedService92",
    ends={
        Property(name="Signature93", type=cm_seff_ServiceEffectSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="cm_seff_ServiceEffectSpecification", type=Signature, multiplicity=Multiplicity(1, 1))
    }
)
basicComponent94: BinaryAssociation = BinaryAssociation(
    name="basicComponent94",
    ends={
        Property(name="repository95", type=cm_seff_ServiceEffectSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="BasicComponent", type=BasicComponent, multiplicity=Multiplicity(1, 1))
    }
)
providedRoles86: BinaryAssociation = BinaryAssociation(
    name="providedRoles86",
    ends={
        Property(name="repository88", type=cm_composition_InterfaceProvidingEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="ProvidedRole87", type=ProvidedRole, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredRoles89: BinaryAssociation = BinaryAssociation(
    name="requiredRoles89",
    ends={
        Property(name="repository91", type=cm_composition_InterfaceRequiringEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="RequiredRole90", type=RequiredRole, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
calledService115: BinaryAssociation = BinaryAssociation(
    name="calledService115",
    ends={
        Property(name="Signature116", type=cm_seff_ExternalCallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="cm_seff_ExternalCallAction", type=Signature, multiplicity=Multiplicity(1, 1))
    }
)
role117: BinaryAssociation = BinaryAssociation(
    name="role117",
    ends={
        Property(name="RequiredRole119", type=cm_seff_ExternalCallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="cm_seff_ExternalCallAction118", type=RequiredRole, multiplicity=Multiplicity(1, 1))
    }
)
branchTransitions120: BinaryAssociation = BinaryAssociation(
    name="branchTransitions120",
    ends={
        Property(name="seff122", type=cm_seff_BranchAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ProbabilisticBranchTransition121", type=ProbabilisticBranchTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
branchAction123: BinaryAssociation = BinaryAssociation(
    name="branchAction123",
    ends={
        Property(name="seff124", type=cm_seff_ProbabilisticBranchTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="BranchAction", type=BranchAction, multiplicity=Multiplicity(1, 1))
    }
)
transition125: BinaryAssociation = BinaryAssociation(
    name="transition125",
    ends={
        Property(name="ProbabilisticBranchTransition126", type=cm_seff_SimpleBehaviorSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="cm_seff_SimpleBehaviorSpecification", type=ProbabilisticBranchTransition, multiplicity=Multiplicity(0, 1))
    }
)
steps127: BinaryAssociation = BinaryAssociation(
    name="steps127",
    ends={
        Property(name="seff129", type=cm_seff_Automaton, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractAction128", type=AbstractAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
internalBehaviours96: BinaryAssociation = BinaryAssociation(
    name="internalBehaviours96",
    ends={
        Property(name="seff97", type=cm_seff_ServiceEffectSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="InternalBehaviour", type=InternalBehaviour, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
serviceEffectSpecifications98: BinaryAssociation = BinaryAssociation(
    name="serviceEffectSpecifications98",
    ends={
        Property(name="seff100", type=cm_seff_InternalBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="ServiceEffectSpecification99", type=ServiceEffectSpecification, multiplicity=Multiplicity(1, 1))
    }
)
branchTransition101: BinaryAssociation = BinaryAssociation(
    name="branchTransition101",
    ends={
        Property(name="ProbabilisticBranchTransition", type=cm_seff_InternalBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="cm_seff_InternalBehaviour", type=ProbabilisticBranchTransition, multiplicity=Multiplicity(0, 1))
    }
)
steps102: BinaryAssociation = BinaryAssociation(
    name="steps102",
    ends={
        Property(name="seff103", type=cm_seff_InternalBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractAction", type=AbstractAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
predecessor104: BinaryAssociation = BinaryAssociation(
    name="predecessor104",
    ends={
        Property(name="seff106", type=cm_seff_AbstractAction, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractAction105", type=AbstractAction, multiplicity=Multiplicity(0, 1))
    }
)
successor107: BinaryAssociation = BinaryAssociation(
    name="successor107",
    ends={
        Property(name="seff109", type=cm_seff_AbstractAction, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractAction108", type=AbstractAction, multiplicity=Multiplicity(0, 1))
    }
)
internalBehaviour110: BinaryAssociation = BinaryAssociation(
    name="internalBehaviour110",
    ends={
        Property(name="seff112", type=cm_seff_AbstractAction, multiplicity=Multiplicity(1, 1)),
        Property(name="InternalBehaviour111", type=InternalBehaviour, multiplicity=Multiplicity(0, 1))
    }
)
specification113: BinaryAssociation = BinaryAssociation(
    name="specification113",
    ends={
        Property(name="seff114", type=cm_seff_AbstractAction, multiplicity=Multiplicity(1, 1)),
        Property(name="Automaton", type=Automaton, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_cm_repository_BasicComponent_ComponentTypeImplementation = Generalization(general=ComponentTypeImplementation, specific=cm_repository_BasicComponent)
gen_cm_repository_ComponentType_RepositoryComponent = Generalization(general=RepositoryComponent, specific=cm_repository_ComponentType)
gen_cm_repository_ProvidedRole_Role = Generalization(general=Role, specific=cm_repository_ProvidedRole)
gen_cm_repository_ComponentTypeImplementation_RepositoryComponent = Generalization(general=RepositoryComponent, specific=cm_repository_ComponentTypeImplementation)
gen_cm_repository_RepositoryComponent_InterfaceProvidingRequiringEntity = Generalization(general=InterfaceProvidingRequiringEntity, specific=cm_repository_RepositoryComponent)
gen_cm_repository_Interface_Entity = Generalization(general=Entity, specific=cm_repository_Interface)
gen_cm_repository_Role_Entity = Generalization(general=Entity, specific=cm_repository_Role)
gen_cm_repository_Repository_Entity = Generalization(general=Entity, specific=cm_repository_Repository)
gen_cm_repository_RequiredRole_Role = Generalization(general=Role, specific=cm_repository_RequiredRole)
gen_cm_repository_CompositeComponent_composition_ComposedProvidingRequiringEntity = Generalization(general=composition_ComposedProvidingRequiringEntity, specific=cm_repository_CompositeComponent)
gen_cm_repository_CompositeComponent_repository_ComponentTypeImplementation = Generalization(general=repository_ComponentTypeImplementation, specific=cm_repository_CompositeComponent)
gen_cm_repository_Signature_Entity = Generalization(general=Entity, specific=cm_repository_Signature)
gen_cm_repository_PrimitiveDataType_DataType = Generalization(general=DataType, specific=cm_repository_PrimitiveDataType)
gen_cm_repository_CollectionDataType_composition_Entity = Generalization(general=composition_Entity, specific=cm_repository_CollectionDataType)
gen_cm_repository_CollectionDataType_repository_DataType = Generalization(general=repository_DataType, specific=cm_repository_CollectionDataType)
gen_cm_composition_DelegationConnector_Connector = Generalization(general=Connector, specific=cm_composition_DelegationConnector)
gen_cm_composition_Connector_Entity = Generalization(general=Entity, specific=cm_composition_Connector)
gen_cm_composition_ComposedStructure_Entity = Generalization(general=Entity, specific=cm_composition_ComposedStructure)
gen_cm_composition_ProvidedDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=cm_composition_ProvidedDelegationConnector)
gen_cm_repository_CompositeDataType_composition_Entity = Generalization(general=composition_Entity, specific=cm_repository_CompositeDataType)
gen_cm_repository_CompositeDataType_repository_DataType = Generalization(general=repository_DataType, specific=cm_repository_CompositeDataType)
gen_cm_repository_InnerDeclaration_NamedElement = Generalization(general=NamedElement, specific=cm_repository_InnerDeclaration)
gen_cm_composition_AssemblyConnector_Connector = Generalization(general=Connector, specific=cm_composition_AssemblyConnector)
gen_cm_composition_AssemblyContext_Entity = Generalization(general=Entity, specific=cm_composition_AssemblyContext)
gen_cm_composition_System_composition_Entity = Generalization(general=composition_Entity, specific=cm_composition_System)
gen_cm_composition_RequiredDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=cm_composition_RequiredDelegationConnector)
gen_cm_composition_ComposedProvidingRequiringEntity_composition_ComposedStructure = Generalization(general=composition_ComposedStructure, specific=cm_composition_ComposedProvidingRequiringEntity)
gen_cm_composition_ComposedProvidingRequiringEntity_composition_InterfaceProvidingRequiringEntity = Generalization(general=composition_InterfaceProvidingRequiringEntity, specific=cm_composition_ComposedProvidingRequiringEntity)
gen_cm_composition_Entity_composition_NamedElement = Generalization(general=composition_NamedElement, specific=cm_composition_Entity)
gen_cm_composition_Entity_composition_Identifier = Generalization(general=composition_Identifier, specific=cm_composition_Entity)
gen_cm_composition_System_composition_ComposedProvidingRequiringEntity = Generalization(general=composition_ComposedProvidingRequiringEntity, specific=cm_composition_System)
gen_cm_composition_SubSystem_composition_ComposedProvidingRequiringEntity = Generalization(general=composition_ComposedProvidingRequiringEntity, specific=cm_composition_SubSystem)
gen_cm_composition_SubSystem_repository_RepositoryComponent = Generalization(general=repository_RepositoryComponent, specific=cm_composition_SubSystem)
gen_cm_composition_InterfaceProvidingRequiringEntity_composition_InterfaceProvidingEntity = Generalization(general=composition_InterfaceProvidingEntity, specific=cm_composition_InterfaceProvidingRequiringEntity)
gen_cm_composition_InterfaceProvidingRequiringEntity_composition_InterfaceRequiringEntity = Generalization(general=composition_InterfaceRequiringEntity, specific=cm_composition_InterfaceProvidingRequiringEntity)
gen_cm_composition_InterfaceProvidingEntity_Entity = Generalization(general=Entity, specific=cm_composition_InterfaceProvidingEntity)
gen_cm_composition_InterfaceRequiringEntity_Entity = Generalization(general=Entity, specific=cm_composition_InterfaceRequiringEntity)
gen_cm_seff_StartAction_AbstractAction = Generalization(general=AbstractAction, specific=cm_seff_StartAction)
gen_cm_seff_StopAction_AbstractAction = Generalization(general=AbstractAction, specific=cm_seff_StopAction)
gen_cm_seff_ExternalCallAction_AbstractAction = Generalization(general=AbstractAction, specific=cm_seff_ExternalCallAction)
gen_cm_seff_BranchAction_AbstractAction = Generalization(general=AbstractAction, specific=cm_seff_BranchAction)
gen_cm_seff_ProbabilisticBranchTransition_composition_Entity = Generalization(general=composition_Entity, specific=cm_seff_ProbabilisticBranchTransition)
gen_cm_seff_ProbabilisticBranchTransition_seff_Automaton = Generalization(general=seff_Automaton, specific=cm_seff_ProbabilisticBranchTransition)
gen_cm_seff_SimpleBehaviorSpecification_seff_ServiceEffectSpecification = Generalization(general=seff_ServiceEffectSpecification, specific=cm_seff_SimpleBehaviorSpecification)
gen_cm_seff_SimpleBehaviorSpecification_seff_Automaton = Generalization(general=seff_Automaton, specific=cm_seff_SimpleBehaviorSpecification)
gen_cm_seff_InternalAction_AbstractAction = Generalization(general=AbstractAction, specific=cm_seff_InternalAction)
gen_cm_seff_AbstractAction_Entity = Generalization(general=Entity, specific=cm_seff_AbstractAction)

# Domain Model
domain_model = DomainModel(
    name="cm",
    types={cm_repository_BasicComponent, ComponentTypeImplementation, cm_repository_ComponentType, cm_repository_ProvidedRole, Role, InterfaceProvidingEntity, Interface, cm_repository_Parameter, DataType, Signature, cm_repository_DataType, ServiceEffectSpecification, cm_repository_ComponentTypeImplementation, RepositoryComponent, ComponentType, cm_repository_RepositoryComponent, InterfaceProvidingRequiringEntity, Repository, cm_repository_Interface, cm_repository_Role, Entity, cm_repository_Repository, cm_repository_ExceptionType, cm_repository_RequiredRole, InterfaceRequiringEntity, cm_repository_CompositeComponent, composition_ComposedProvidingRequiringEntity, repository_ComponentTypeImplementation, cm_repository_Signature, ExceptionType, Parameter_, cm_repository_PrimitiveDataType, cm_repository_CollectionDataType, composition_Entity, repository_DataType, cm_composition_DelegationConnector, Connector, cm_composition_Connector, ComposedStructure, cm_composition_ComposedStructure, AssemblyContext, cm_composition_ProvidedDelegationConnector, DelegationConnector, cm_repository_CompositeDataType, CompositeDataType, InnerDeclaration, cm_repository_InnerDeclaration, NamedElement, cm_composition_AssemblyConnector, cm_composition_AssemblyContext, cm_composition_System, ProvidedRole, cm_composition_RequiredDelegationConnector, RequiredRole, cm_composition_ComposedProvidingRequiringEntity, composition_ComposedStructure, composition_InterfaceProvidingRequiringEntity, cm_composition_NamedElement, cm_composition_Entity, composition_NamedElement, composition_Identifier, cm_composition_Identifier, cm_seff_ServiceEffectSpecification, BasicComponent, cm_composition_SubSystem, repository_RepositoryComponent, cm_composition_InterfaceProvidingRequiringEntity, composition_InterfaceProvidingEntity, composition_InterfaceRequiringEntity, cm_composition_InterfaceProvidingEntity, cm_composition_InterfaceRequiringEntity, cm_seff_StartAction, cm_seff_StopAction, cm_seff_ExternalCallAction, cm_seff_BranchAction, cm_seff_ProbabilisticBranchTransition, seff_Automaton, BranchAction, cm_seff_SimpleBehaviorSpecification, seff_ServiceEffectSpecification, cm_seff_InternalAction, cm_seff_Automaton, InternalBehaviour, cm_seff_InternalBehaviour, ProbabilisticBranchTransition, AbstractAction, cm_seff_AbstractAction, Automaton, PrimitiveType},
    associations={providingEntity3, providedInterface4, dataType5, signature6, repository8, serviceEffectSpecifications0, implementedComponentTypes1, repository2, interfaces13, dataTypes16, parentInterfaces19, repository21, components11, requiringEntity36, requiredInterface38, signatures24, exceptions27, parameters28, returnType30, interface33, innerType40, parentStructure50, assemblyContexts52, connectors54, parentType42, innerDeclaration43, dataType45, compositeDataType47, requiringAssemblyContext70, providingAssemblyContext72, providedRole75, requiredRole78, parentStructure81, encapsulatedComponent84, innerProvidedRole56, outerProvidedRole57, assemblyContext60, innerRequiredRole63, outerRequiredRole64, assemblyContext67, describedService92, basicComponent94, providedRoles86, requiredRoles89, calledService115, role117, branchTransitions120, branchAction123, transition125, steps127, internalBehaviours96, serviceEffectSpecifications98, branchTransition101, steps102, predecessor104, successor107, internalBehaviour110, specification113},
    generalizations={gen_cm_repository_BasicComponent_ComponentTypeImplementation, gen_cm_repository_ComponentType_RepositoryComponent, gen_cm_repository_ProvidedRole_Role, gen_cm_repository_ComponentTypeImplementation_RepositoryComponent, gen_cm_repository_RepositoryComponent_InterfaceProvidingRequiringEntity, gen_cm_repository_Interface_Entity, gen_cm_repository_Role_Entity, gen_cm_repository_Repository_Entity, gen_cm_repository_RequiredRole_Role, gen_cm_repository_CompositeComponent_composition_ComposedProvidingRequiringEntity, gen_cm_repository_CompositeComponent_repository_ComponentTypeImplementation, gen_cm_repository_Signature_Entity, gen_cm_repository_PrimitiveDataType_DataType, gen_cm_repository_CollectionDataType_composition_Entity, gen_cm_repository_CollectionDataType_repository_DataType, gen_cm_composition_DelegationConnector_Connector, gen_cm_composition_Connector_Entity, gen_cm_composition_ComposedStructure_Entity, gen_cm_composition_ProvidedDelegationConnector_DelegationConnector, gen_cm_repository_CompositeDataType_composition_Entity, gen_cm_repository_CompositeDataType_repository_DataType, gen_cm_repository_InnerDeclaration_NamedElement, gen_cm_composition_AssemblyConnector_Connector, gen_cm_composition_AssemblyContext_Entity, gen_cm_composition_System_composition_Entity, gen_cm_composition_RequiredDelegationConnector_DelegationConnector, gen_cm_composition_ComposedProvidingRequiringEntity_composition_ComposedStructure, gen_cm_composition_ComposedProvidingRequiringEntity_composition_InterfaceProvidingRequiringEntity, gen_cm_composition_Entity_composition_NamedElement, gen_cm_composition_Entity_composition_Identifier, gen_cm_composition_System_composition_ComposedProvidingRequiringEntity, gen_cm_composition_SubSystem_composition_ComposedProvidingRequiringEntity, gen_cm_composition_SubSystem_repository_RepositoryComponent, gen_cm_composition_InterfaceProvidingRequiringEntity_composition_InterfaceProvidingEntity, gen_cm_composition_InterfaceProvidingRequiringEntity_composition_InterfaceRequiringEntity, gen_cm_composition_InterfaceProvidingEntity_Entity, gen_cm_composition_InterfaceRequiringEntity_Entity, gen_cm_seff_StartAction_AbstractAction, gen_cm_seff_StopAction_AbstractAction, gen_cm_seff_ExternalCallAction_AbstractAction, gen_cm_seff_BranchAction_AbstractAction, gen_cm_seff_ProbabilisticBranchTransition_composition_Entity, gen_cm_seff_ProbabilisticBranchTransition_seff_Automaton, gen_cm_seff_SimpleBehaviorSpecification_seff_ServiceEffectSpecification, gen_cm_seff_SimpleBehaviorSpecification_seff_Automaton, gen_cm_seff_InternalAction_AbstractAction, gen_cm_seff_AbstractAction_Entity},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)