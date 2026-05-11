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
cm_repository_BasicComponent = Class(name="cm_repository_BasicComponent")
ComponentTypeImplementation = Class(name="ComponentTypeImplementation")
ServiceEffectSpecification = Class(name="ServiceEffectSpecification")
cm_repository_ComponentTypeImplementation = Class(name="cm_repository_ComponentTypeImplementation", is_abstract=True)
RepositoryComponent = Class(name="RepositoryComponent")
Repository = Class(name="Repository")
cm_repository_ComponentType = Class(name="cm_repository_ComponentType")
cm_repository_ProvidedRole = Class(name="cm_repository_ProvidedRole")
Role = Class(name="Role")
InterfaceProvidingEntity = Class(name="InterfaceProvidingEntity")
Interface = Class(name="Interface")
cm_repository_Parameter = Class(name="cm_repository_Parameter")
DataType = Class(name="DataType")
Signature = Class(name="Signature")
cm_repository_DataType = Class(name="cm_repository_DataType", is_abstract=True)
cm_repository_Role = Class(name="cm_repository_Role", is_abstract=True)
Entity = Class(name="Entity")
cm_repository_Repository = Class(name="cm_repository_Repository")
ComponentType = Class(name="ComponentType")
cm_repository_RepositoryComponent = Class(name="cm_repository_RepositoryComponent", is_abstract=True)
InterfaceProvidingRequiringEntity = Class(name="InterfaceProvidingRequiringEntity")
cm_repository_Interface = Class(name="cm_repository_Interface")
cm_repository_Signature = Class(name="cm_repository_Signature")
ExceptionType = Class(name="ExceptionType")
Parameter_ = Class(name="Parameter")
cm_repository_ExceptionType = Class(name="cm_repository_ExceptionType")
cm_repository_RequiredRole = Class(name="cm_repository_RequiredRole")
InterfaceRequiringEntity = Class(name="InterfaceRequiringEntity")
cm_repository_CompositeComponent = Class(name="cm_repository_CompositeComponent")
composition_ComposedProvidingRequiringEntity = Class(name="composition_ComposedProvidingRequiringEntity")
repository_ComponentTypeImplementation = Class(name="repository_ComponentTypeImplementation")
cm_repository_PrimitiveDataType = Class(name="cm_repository_PrimitiveDataType")
cm_repository_CollectionDataType = Class(name="cm_repository_CollectionDataType")
composition_Entity = Class(name="composition_Entity")
repository_DataType = Class(name="repository_DataType")
cm_repository_CompositeDataType = Class(name="cm_repository_CompositeDataType")
CompositeDataType = Class(name="CompositeDataType")
InnerDeclaration = Class(name="InnerDeclaration")
cm_repository_InnerDeclaration = Class(name="cm_repository_InnerDeclaration")
NamedElement = Class(name="NamedElement")
Connector = Class(name="Connector")
cm_composition_Connector = Class(name="cm_composition_Connector", is_abstract=True)
ComposedStructure = Class(name="ComposedStructure")
cm_composition_ComposedStructure = Class(name="cm_composition_ComposedStructure", is_abstract=True)
AssemblyContext = Class(name="AssemblyContext")
cm_composition_ProvidedDelegationConnector = Class(name="cm_composition_ProvidedDelegationConnector")
DelegationConnector = Class(name="DelegationConnector")
RequiredRole = Class(name="RequiredRole")
cm_composition_DelegationConnector = Class(name="cm_composition_DelegationConnector", is_abstract=True)
cm_composition_AssemblyConnector = Class(name="cm_composition_AssemblyConnector")
cm_composition_InterfaceRequiringEntity = Class(name="cm_composition_InterfaceRequiringEntity", is_abstract=True)
cm_composition_ComposedProvidingRequiringEntity = Class(name="cm_composition_ComposedProvidingRequiringEntity", is_abstract=True)
composition_ComposedStructure = Class(name="composition_ComposedStructure")
composition_InterfaceProvidingRequiringEntity = Class(name="composition_InterfaceProvidingRequiringEntity")
cm_composition_NamedElement = Class(name="cm_composition_NamedElement", is_abstract=True)
cm_composition_Entity = Class(name="cm_composition_Entity", is_abstract=True)
composition_NamedElement = Class(name="composition_NamedElement")
composition_Identifier = Class(name="composition_Identifier")
ProvidedRole = Class(name="ProvidedRole")
cm_composition_RequiredDelegationConnector = Class(name="cm_composition_RequiredDelegationConnector")
cm_composition_AssemblyContext = Class(name="cm_composition_AssemblyContext")
cm_composition_System = Class(name="cm_composition_System")
cm_composition_SubSystem = Class(name="cm_composition_SubSystem")
repository_RepositoryComponent = Class(name="repository_RepositoryComponent")
cm_composition_InterfaceProvidingRequiringEntity = Class(name="cm_composition_InterfaceProvidingRequiringEntity", is_abstract=True)
composition_InterfaceProvidingEntity = Class(name="composition_InterfaceProvidingEntity")
composition_InterfaceRequiringEntity = Class(name="composition_InterfaceRequiringEntity")
cm_composition_InterfaceProvidingEntity = Class(name="cm_composition_InterfaceProvidingEntity", is_abstract=True)
Automaton = Class(name="Automaton")
cm_seff_StartAction = Class(name="cm_seff_StartAction")
cm_seff_StopAction = Class(name="cm_seff_StopAction")
cm_seff_ExternalCallAction = Class(name="cm_seff_ExternalCallAction")
cm_composition_Identifier = Class(name="cm_composition_Identifier", is_abstract=True)
cm_seff_ServiceEffectSpecification = Class(name="cm_seff_ServiceEffectSpecification", is_abstract=True)
BasicComponent = Class(name="BasicComponent")
InternalBehaviour = Class(name="InternalBehaviour")
cm_seff_InternalBehaviour = Class(name="cm_seff_InternalBehaviour")
ProbabilisticBranchTransition = Class(name="ProbabilisticBranchTransition")
AbstractAction = Class(name="AbstractAction")
cm_seff_AbstractAction = Class(name="cm_seff_AbstractAction", is_abstract=True)
cm_seff_BranchAction = Class(name="cm_seff_BranchAction")
cm_seff_ProbabilisticBranchTransition = Class(name="cm_seff_ProbabilisticBranchTransition")
seff_Automaton = Class(name="seff_Automaton")
BranchAction = Class(name="BranchAction")
cm_seff_SimpleBehaviorSpecification = Class(name="cm_seff_SimpleBehaviorSpecification")
seff_ServiceEffectSpecification = Class(name="seff_ServiceEffectSpecification")
cm_seff_InternalAction = Class(name="cm_seff_InternalAction")
cm_seff_Automaton = Class(name="cm_seff_Automaton", is_abstract=True)

# cm_repository_BasicComponent class attributes and methods

# ComponentTypeImplementation class attributes and methods

# ServiceEffectSpecification class attributes and methods

# cm_repository_ComponentTypeImplementation class attributes and methods

# RepositoryComponent class attributes and methods

# Repository class attributes and methods

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

# cm_repository_Role class attributes and methods

# Entity class attributes and methods

# cm_repository_Repository class attributes and methods
cm_repository_Repository_description: Property = Property(name="description", type=StringType)
cm_repository_Repository.attributes={cm_repository_Repository_description}

# ComponentType class attributes and methods

# cm_repository_RepositoryComponent class attributes and methods

# InterfaceProvidingRequiringEntity class attributes and methods

# cm_repository_Interface class attributes and methods

# cm_repository_Signature class attributes and methods

# ExceptionType class attributes and methods

# Parameter class attributes and methods

# cm_repository_ExceptionType class attributes and methods
cm_repository_ExceptionType_name: Property = Property(name="name", type=StringType)
cm_repository_ExceptionType_message: Property = Property(name="message", type=StringType)
cm_repository_ExceptionType.attributes={cm_repository_ExceptionType_name, cm_repository_ExceptionType_message}

# cm_repository_RequiredRole class attributes and methods

# InterfaceRequiringEntity class attributes and methods

# cm_repository_CompositeComponent class attributes and methods
cm_repository_CompositeComponent_m_RequireSameInterfaces: Method = Method(name="RequireSameInterfaces", parameters={Parameter(name='cm_context', type=StringType), Parameter(name='cm_diagnostics', type=StringType)}, type=BooleanType)
cm_repository_CompositeComponent_m_ProvideSameInterfaces: Method = Method(name="ProvideSameInterfaces", parameters={Parameter(name='cm_context', type=StringType), Parameter(name='cm_diagnostics', type=StringType)}, type=BooleanType)
cm_repository_CompositeComponent.methods={cm_repository_CompositeComponent_m_ProvideSameInterfaces, cm_repository_CompositeComponent_m_RequireSameInterfaces}

# composition_ComposedProvidingRequiringEntity class attributes and methods

# repository_ComponentTypeImplementation class attributes and methods

# cm_repository_PrimitiveDataType class attributes and methods
cm_repository_PrimitiveDataType_type: Property = Property(name="type", type=StringType)
cm_repository_PrimitiveDataType.attributes={cm_repository_PrimitiveDataType_type}

# cm_repository_CollectionDataType class attributes and methods

# composition_Entity class attributes and methods

# repository_DataType class attributes and methods

# cm_repository_CompositeDataType class attributes and methods

# CompositeDataType class attributes and methods

# InnerDeclaration class attributes and methods

# cm_repository_InnerDeclaration class attributes and methods

# NamedElement class attributes and methods

# Connector class attributes and methods

# cm_composition_Connector class attributes and methods

# ComposedStructure class attributes and methods

# cm_composition_ComposedStructure class attributes and methods
cm_composition_ComposedStructure_m_MultipleConnectorsConstraint: Method = Method(name="MultipleConnectorsConstraint", parameters={Parameter(name='cm_diagnostics', type=StringType), Parameter(name='cm_context', type=StringType)}, type=BooleanType)
cm_composition_ComposedStructure_m_MultipleConnectorsConstraintForAssemblyConnectors: Method = Method(name="MultipleConnectorsConstraintForAssemblyConnectors", parameters={Parameter(name='cm_diagnostics', type=StringType), Parameter(name='cm_context', type=StringType)}, type=BooleanType)
cm_composition_ComposedStructure.methods={cm_composition_ComposedStructure_m_MultipleConnectorsConstraintForAssemblyConnectors, cm_composition_ComposedStructure_m_MultipleConnectorsConstraint}

# AssemblyContext class attributes and methods

# cm_composition_ProvidedDelegationConnector class attributes and methods
cm_composition_ProvidedDelegationConnector_m_ComponentOfAssemblyContextAndInnerRoleProvidingComponentNeedToBeTheSame: Method = Method(name="ComponentOfAssemblyContextAndInnerRoleProvidingComponentNeedToBeTheSame", parameters={Parameter(name='cm_diagnostics', type=StringType), Parameter(name='cm_context', type=StringType)}, type=BooleanType)
cm_composition_ProvidedDelegationConnector_m_ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure: Method = Method(name="ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure", parameters={Parameter(name='cm_diagnostics', type=StringType), Parameter(name='cm_context', type=StringType)}, type=BooleanType)
cm_composition_ProvidedDelegationConnector.methods={cm_composition_ProvidedDelegationConnector_m_ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure, cm_composition_ProvidedDelegationConnector_m_ComponentOfAssemblyContextAndInnerRoleProvidingComponentNeedToBeTheSame}

# DelegationConnector class attributes and methods

# RequiredRole class attributes and methods

# cm_composition_DelegationConnector class attributes and methods

# cm_composition_AssemblyConnector class attributes and methods
cm_composition_AssemblyConnector_m_AssemblyConnectorsReferencedProvidedRolesAndChildContextMustMatch: Method = Method(name="AssemblyConnectorsReferencedProvidedRolesAndChildContextMustMatch", parameters={Parameter(name='cm_diagnostics', type=StringType), Parameter(name='cm_context', type=StringType)}, type=BooleanType)
cm_composition_AssemblyConnector_m_AssemblyConnectorsReferencedInterfacesMustMatch: Method = Method(name="AssemblyConnectorsReferencedInterfacesMustMatch", parameters={Parameter(name='cm_context', type=StringType), Parameter(name='cm_diagnostics', type=StringType)}, type=BooleanType)
cm_composition_AssemblyConnector_m_AssemblyConnectorsReferencedRequiredRoleAndChildContextMustMatch: Method = Method(name="AssemblyConnectorsReferencedRequiredRoleAndChildContextMustMatch", parameters={Parameter(name='cm_context', type=StringType), Parameter(name='cm_diagnostics', type=StringType)}, type=BooleanType)
cm_composition_AssemblyConnector.methods={cm_composition_AssemblyConnector_m_AssemblyConnectorsReferencedRequiredRoleAndChildContextMustMatch, cm_composition_AssemblyConnector_m_AssemblyConnectorsReferencedInterfacesMustMatch, cm_composition_AssemblyConnector_m_AssemblyConnectorsReferencedProvidedRolesAndChildContextMustMatch}

# cm_composition_InterfaceRequiringEntity class attributes and methods

# cm_composition_ComposedProvidingRequiringEntity class attributes and methods

# composition_ComposedStructure class attributes and methods

# composition_InterfaceProvidingRequiringEntity class attributes and methods

# cm_composition_NamedElement class attributes and methods
cm_composition_NamedElement_entityName: Property = Property(name="entityName", type=StringType)
cm_composition_NamedElement.attributes={cm_composition_NamedElement_entityName}

# cm_composition_Entity class attributes and methods

# composition_NamedElement class attributes and methods

# composition_Identifier class attributes and methods

# ProvidedRole class attributes and methods

# cm_composition_RequiredDelegationConnector class attributes and methods

# cm_composition_AssemblyContext class attributes and methods

# cm_composition_System class attributes and methods
cm_composition_System_m_SystemMustHaveAtLeastOneProvidedRole: Method = Method(name="SystemMustHaveAtLeastOneProvidedRole", parameters={Parameter(name='cm_context', type=StringType), Parameter(name='cm_diagnostics', type=StringType)}, type=BooleanType)
cm_composition_System.methods={cm_composition_System_m_SystemMustHaveAtLeastOneProvidedRole}

# cm_composition_SubSystem class attributes and methods

# repository_RepositoryComponent class attributes and methods

# cm_composition_InterfaceProvidingRequiringEntity class attributes and methods

# composition_InterfaceProvidingEntity class attributes and methods

# composition_InterfaceRequiringEntity class attributes and methods

# cm_composition_InterfaceProvidingEntity class attributes and methods

# Automaton class attributes and methods

# cm_seff_StartAction class attributes and methods

# cm_seff_StopAction class attributes and methods

# cm_seff_ExternalCallAction class attributes and methods

# cm_composition_Identifier class attributes and methods
cm_composition_Identifier_id: Property = Property(name="id", type=StringType)
cm_composition_Identifier_m_idHasToBeUnique: Method = Method(name="idHasToBeUnique", parameters={Parameter(name='cm_diagnostics', type=StringType), Parameter(name='cm_context', type=StringType)}, type=BooleanType)
cm_composition_Identifier.attributes={cm_composition_Identifier_id}
cm_composition_Identifier.methods={cm_composition_Identifier_m_idHasToBeUnique}

# cm_seff_ServiceEffectSpecification class attributes and methods

# BasicComponent class attributes and methods

# InternalBehaviour class attributes and methods

# cm_seff_InternalBehaviour class attributes and methods

# ProbabilisticBranchTransition class attributes and methods

# AbstractAction class attributes and methods

# cm_seff_AbstractAction class attributes and methods

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

# Relationships
serviceEffectSpecifications0: BinaryAssociation = BinaryAssociation(
    name="serviceEffectSpecifications0",
    ends={
        Property(name="ServiceEffectSpecification", type=cm_repository_BasicComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="basicComponent", type=ServiceEffectSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
repository2: BinaryAssociation = BinaryAssociation(
    name="repository2",
    ends={
        Property(name="Repository", type=cm_repository_RepositoryComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="components", type=Repository, multiplicity=Multiplicity(1, 1))
    }
)
providingEntity3: BinaryAssociation = BinaryAssociation(
    name="providingEntity3",
    ends={
        Property(name="InterfaceProvidingEntity", type=cm_repository_ProvidedRole, multiplicity=Multiplicity(1, 1)),
        Property(name="providedRoles", type=InterfaceProvidingEntity, multiplicity=Multiplicity(1, 1))
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
        Property(name="Signature", type=cm_repository_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameters", type=Signature, multiplicity=Multiplicity(0, 1))
    }
)
repository7: BinaryAssociation = BinaryAssociation(
    name="repository7",
    ends={
        Property(name="Repository8", type=cm_repository_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="dataTypes", type=Repository, multiplicity=Multiplicity(1, 1))
    }
)
components9: BinaryAssociation = BinaryAssociation(
    name="components9",
    ends={
        Property(name="RepositoryComponent", type=cm_repository_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="repository", type=RepositoryComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
implementedComponentTypes1: BinaryAssociation = BinaryAssociation(
    name="implementedComponentTypes1",
    ends={
        Property(name="ComponentType", type=cm_repository_ComponentTypeImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="cm_repository_ComponentTypeImplementation", type=ComponentType, multiplicity=Multiplicity(0, 9999))
    }
)
parentInterfaces16: BinaryAssociation = BinaryAssociation(
    name="parentInterfaces16",
    ends={
        Property(name="Interface17", type=cm_repository_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="cm_repository_Interface", type=Interface, multiplicity=Multiplicity(0, 9999))
    }
)
repository18: BinaryAssociation = BinaryAssociation(
    name="repository18",
    ends={
        Property(name="Repository19", type=cm_repository_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="interfaces", type=Repository, multiplicity=Multiplicity(1, 1))
    }
)
signatures20: BinaryAssociation = BinaryAssociation(
    name="signatures20",
    ends={
        Property(name="Signature21", type=cm_repository_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="interface", type=Signature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exceptions22: BinaryAssociation = BinaryAssociation(
    name="exceptions22",
    ends={
        Property(name="ExceptionType", type=cm_repository_Signature, multiplicity=Multiplicity(1, 1)),
        Property(name="cm_repository_Signature", type=ExceptionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters23: BinaryAssociation = BinaryAssociation(
    name="parameters23",
    ends={
        Property(name="Parameter", type=cm_repository_Signature, multiplicity=Multiplicity(1, 1)),
        Property(name="signature", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnType24: BinaryAssociation = BinaryAssociation(
    name="returnType24",
    ends={
        Property(name="DataType26", type=cm_repository_Signature, multiplicity=Multiplicity(1, 1)),
        Property(name="cm_repository_Signature25", type=DataType, multiplicity=Multiplicity(0, 1))
    }
)
interface27: BinaryAssociation = BinaryAssociation(
    name="interface27",
    ends={
        Property(name="Interface28", type=cm_repository_Signature, multiplicity=Multiplicity(1, 1)),
        Property(name="signatures", type=Interface, multiplicity=Multiplicity(1, 1))
    }
)
requiringEntity29: BinaryAssociation = BinaryAssociation(
    name="requiringEntity29",
    ends={
        Property(name="InterfaceRequiringEntity", type=cm_repository_RequiredRole, multiplicity=Multiplicity(1, 1)),
        Property(name="requiredRoles", type=InterfaceRequiringEntity, multiplicity=Multiplicity(1, 1))
    }
)
requiredInterface30: BinaryAssociation = BinaryAssociation(
    name="requiredInterface30",
    ends={
        Property(name="Interface31", type=cm_repository_RequiredRole, multiplicity=Multiplicity(1, 1)),
        Property(name="cm_repository_RequiredRole", type=Interface, multiplicity=Multiplicity(1, 1))
    }
)
interfaces10: BinaryAssociation = BinaryAssociation(
    name="interfaces10",
    ends={
        Property(name="Interface12", type=cm_repository_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="repository11", type=Interface, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataTypes13: BinaryAssociation = BinaryAssociation(
    name="dataTypes13",
    ends={
        Property(name="DataType15", type=cm_repository_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="repository14", type=DataType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
innerType32: BinaryAssociation = BinaryAssociation(
    name="innerType32",
    ends={
        Property(name="DataType33", type=cm_repository_CollectionDataType, multiplicity=Multiplicity(1, 1)),
        Property(name="cm_repository_CollectionDataType", type=DataType, multiplicity=Multiplicity(1, 1))
    }
)
parentType34: BinaryAssociation = BinaryAssociation(
    name="parentType34",
    ends={
        Property(name="CompositeDataType", type=cm_repository_CompositeDataType, multiplicity=Multiplicity(1, 1)),
        Property(name="cm_repository_CompositeDataType", type=CompositeDataType, multiplicity=Multiplicity(0, 9999))
    }
)
innerDeclaration35: BinaryAssociation = BinaryAssociation(
    name="innerDeclaration35",
    ends={
        Property(name="InnerDeclaration", type=cm_repository_CompositeDataType, multiplicity=Multiplicity(1, 1)),
        Property(name="compositeDataType", type=InnerDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataType36: BinaryAssociation = BinaryAssociation(
    name="dataType36",
    ends={
        Property(name="DataType37", type=cm_repository_InnerDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="cm_repository_InnerDeclaration", type=DataType, multiplicity=Multiplicity(1, 1))
    }
)
compositeDataType38: BinaryAssociation = BinaryAssociation(
    name="compositeDataType38",
    ends={
        Property(name="CompositeDataType39", type=cm_repository_InnerDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="innerDeclaration", type=CompositeDataType, multiplicity=Multiplicity(1, 1))
    }
)
parentStructure40: BinaryAssociation = BinaryAssociation(
    name="parentStructure40",
    ends={
        Property(name="ComposedStructure", type=cm_composition_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="connectors", type=ComposedStructure, multiplicity=Multiplicity(1, 1))
    }
)
assemblyContexts41: BinaryAssociation = BinaryAssociation(
    name="assemblyContexts41",
    ends={
        Property(name="AssemblyContext", type=cm_composition_ComposedStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="parentStructure", type=AssemblyContext, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connectors42: BinaryAssociation = BinaryAssociation(
    name="connectors42",
    ends={
        Property(name="Connector", type=cm_composition_ComposedStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="parentStructure43", type=Connector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
innerRequiredRole51: BinaryAssociation = BinaryAssociation(
    name="innerRequiredRole51",
    ends={
        Property(name="RequiredRole", type=cm_composition_RequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="cm_composition_RequiredDelegationConnector", type=RequiredRole, multiplicity=Multiplicity(1, 1))
    }
)
outerRequiredRole52: BinaryAssociation = BinaryAssociation(
    name="outerRequiredRole52",
    ends={
        Property(name="RequiredRole54", type=cm_composition_RequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="cm_composition_RequiredDelegationConnector53", type=RequiredRole, multiplicity=Multiplicity(1, 1))
    }
)
assemblyContext55: BinaryAssociation = BinaryAssociation(
    name="assemblyContext55",
    ends={
        Property(name="AssemblyContext57", type=cm_composition_RequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="cm_composition_RequiredDelegationConnector56", type=AssemblyContext, multiplicity=Multiplicity(1, 1))
    }
)
providedRoles73: BinaryAssociation = BinaryAssociation(
    name="providedRoles73",
    ends={
        Property(name="ProvidedRole74", type=cm_composition_InterfaceProvidingEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="providingEntity", type=ProvidedRole, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredRoles75: BinaryAssociation = BinaryAssociation(
    name="requiredRoles75",
    ends={
        Property(name="RequiredRole76", type=cm_composition_InterfaceRequiringEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="requiringEntity", type=RequiredRole, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
innerProvidedRole44: BinaryAssociation = BinaryAssociation(
    name="innerProvidedRole44",
    ends={
        Property(name="ProvidedRole", type=cm_composition_ProvidedDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="cm_composition_ProvidedDelegationConnector", type=ProvidedRole, multiplicity=Multiplicity(1, 1))
    }
)
outerProvidedRole45: BinaryAssociation = BinaryAssociation(
    name="outerProvidedRole45",
    ends={
        Property(name="ProvidedRole47", type=cm_composition_ProvidedDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="cm_composition_ProvidedDelegationConnector46", type=ProvidedRole, multiplicity=Multiplicity(1, 1))
    }
)
assemblyContext48: BinaryAssociation = BinaryAssociation(
    name="assemblyContext48",
    ends={
        Property(name="AssemblyContext50", type=cm_composition_ProvidedDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="cm_composition_ProvidedDelegationConnector49", type=AssemblyContext, multiplicity=Multiplicity(1, 1))
    }
)
requiringAssemblyContext58: BinaryAssociation = BinaryAssociation(
    name="requiringAssemblyContext58",
    ends={
        Property(name="AssemblyContext59", type=cm_composition_AssemblyConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="cm_composition_AssemblyConnector", type=AssemblyContext, multiplicity=Multiplicity(1, 1))
    }
)
providingAssemblyContext60: BinaryAssociation = BinaryAssociation(
    name="providingAssemblyContext60",
    ends={
        Property(name="AssemblyContext62", type=cm_composition_AssemblyConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="cm_composition_AssemblyConnector61", type=AssemblyContext, multiplicity=Multiplicity(1, 1))
    }
)
providedRole63: BinaryAssociation = BinaryAssociation(
    name="providedRole63",
    ends={
        Property(name="ProvidedRole65", type=cm_composition_AssemblyConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="cm_composition_AssemblyConnector64", type=ProvidedRole, multiplicity=Multiplicity(1, 1))
    }
)
requiredRole66: BinaryAssociation = BinaryAssociation(
    name="requiredRole66",
    ends={
        Property(name="RequiredRole68", type=cm_composition_AssemblyConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="cm_composition_AssemblyConnector67", type=RequiredRole, multiplicity=Multiplicity(1, 1))
    }
)
parentStructure69: BinaryAssociation = BinaryAssociation(
    name="parentStructure69",
    ends={
        Property(name="ComposedStructure70", type=cm_composition_AssemblyContext, multiplicity=Multiplicity(1, 1)),
        Property(name="assemblyContexts", type=ComposedStructure, multiplicity=Multiplicity(1, 1))
    }
)
encapsulatedComponent71: BinaryAssociation = BinaryAssociation(
    name="encapsulatedComponent71",
    ends={
        Property(name="RepositoryComponent72", type=cm_composition_AssemblyContext, multiplicity=Multiplicity(1, 1)),
        Property(name="cm_composition_AssemblyContext", type=RepositoryComponent, multiplicity=Multiplicity(1, 1))
    }
)
successor88: BinaryAssociation = BinaryAssociation(
    name="successor88",
    ends={
        Property(name="AbstractAction89", type=cm_seff_AbstractAction, multiplicity=Multiplicity(1, 1)),
        Property(name="predecessor", type=AbstractAction, multiplicity=Multiplicity(0, 1))
    }
)
internalBehaviour90: BinaryAssociation = BinaryAssociation(
    name="internalBehaviour90",
    ends={
        Property(name="InternalBehaviour91", type=cm_seff_AbstractAction, multiplicity=Multiplicity(1, 1)),
        Property(name="steps", type=InternalBehaviour, multiplicity=Multiplicity(0, 1))
    }
)
specification92: BinaryAssociation = BinaryAssociation(
    name="specification92",
    ends={
        Property(name="Automaton", type=cm_seff_AbstractAction, multiplicity=Multiplicity(1, 1)),
        Property(name="steps93", type=Automaton, multiplicity=Multiplicity(0, 1))
    }
)
calledService94: BinaryAssociation = BinaryAssociation(
    name="calledService94",
    ends={
        Property(name="Signature95", type=cm_seff_ExternalCallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="cm_seff_ExternalCallAction", type=Signature, multiplicity=Multiplicity(1, 1))
    }
)
describedService77: BinaryAssociation = BinaryAssociation(
    name="describedService77",
    ends={
        Property(name="Signature78", type=cm_seff_ServiceEffectSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="cm_seff_ServiceEffectSpecification", type=Signature, multiplicity=Multiplicity(1, 1))
    }
)
basicComponent79: BinaryAssociation = BinaryAssociation(
    name="basicComponent79",
    ends={
        Property(name="BasicComponent", type=cm_seff_ServiceEffectSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="serviceEffectSpecifications", type=BasicComponent, multiplicity=Multiplicity(1, 1))
    }
)
internalBehaviours80: BinaryAssociation = BinaryAssociation(
    name="internalBehaviours80",
    ends={
        Property(name="InternalBehaviour", type=cm_seff_ServiceEffectSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="serviceEffectSpecifications81", type=InternalBehaviour, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
serviceEffectSpecifications82: BinaryAssociation = BinaryAssociation(
    name="serviceEffectSpecifications82",
    ends={
        Property(name="ServiceEffectSpecification83", type=cm_seff_InternalBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="internalBehaviours", type=ServiceEffectSpecification, multiplicity=Multiplicity(1, 1))
    }
)
branchTransition84: BinaryAssociation = BinaryAssociation(
    name="branchTransition84",
    ends={
        Property(name="ProbabilisticBranchTransition", type=cm_seff_InternalBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="cm_seff_InternalBehaviour", type=ProbabilisticBranchTransition, multiplicity=Multiplicity(0, 1))
    }
)
steps85: BinaryAssociation = BinaryAssociation(
    name="steps85",
    ends={
        Property(name="AbstractAction", type=cm_seff_InternalBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="internalBehaviour", type=AbstractAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
predecessor86: BinaryAssociation = BinaryAssociation(
    name="predecessor86",
    ends={
        Property(name="AbstractAction87", type=cm_seff_AbstractAction, multiplicity=Multiplicity(1, 1)),
        Property(name="successor", type=AbstractAction, multiplicity=Multiplicity(0, 1))
    }
)
role96: BinaryAssociation = BinaryAssociation(
    name="role96",
    ends={
        Property(name="RequiredRole98", type=cm_seff_ExternalCallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="cm_seff_ExternalCallAction97", type=RequiredRole, multiplicity=Multiplicity(1, 1))
    }
)
branchTransitions99: BinaryAssociation = BinaryAssociation(
    name="branchTransitions99",
    ends={
        Property(name="ProbabilisticBranchTransition100", type=cm_seff_BranchAction, multiplicity=Multiplicity(1, 1)),
        Property(name="branchAction", type=ProbabilisticBranchTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
branchAction101: BinaryAssociation = BinaryAssociation(
    name="branchAction101",
    ends={
        Property(name="BranchAction", type=cm_seff_ProbabilisticBranchTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="branchTransitions", type=BranchAction, multiplicity=Multiplicity(1, 1))
    }
)
transition102: BinaryAssociation = BinaryAssociation(
    name="transition102",
    ends={
        Property(name="ProbabilisticBranchTransition103", type=cm_seff_SimpleBehaviorSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="cm_seff_SimpleBehaviorSpecification", type=ProbabilisticBranchTransition, multiplicity=Multiplicity(0, 1))
    }
)
steps104: BinaryAssociation = BinaryAssociation(
    name="steps104",
    ends={
        Property(name="AbstractAction105", type=cm_seff_Automaton, multiplicity=Multiplicity(1, 1)),
        Property(name="specification", type=AbstractAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_cm_repository_BasicComponent_ComponentTypeImplementation = Generalization(general=ComponentTypeImplementation, specific=cm_repository_BasicComponent)
gen_cm_repository_ComponentTypeImplementation_RepositoryComponent = Generalization(general=RepositoryComponent, specific=cm_repository_ComponentTypeImplementation)
gen_cm_repository_ComponentType_RepositoryComponent = Generalization(general=RepositoryComponent, specific=cm_repository_ComponentType)
gen_cm_repository_ProvidedRole_Role = Generalization(general=Role, specific=cm_repository_ProvidedRole)
gen_cm_repository_Role_Entity = Generalization(general=Entity, specific=cm_repository_Role)
gen_cm_repository_Repository_Entity = Generalization(general=Entity, specific=cm_repository_Repository)
gen_cm_repository_RepositoryComponent_InterfaceProvidingRequiringEntity = Generalization(general=InterfaceProvidingRequiringEntity, specific=cm_repository_RepositoryComponent)
gen_cm_repository_Interface_Entity = Generalization(general=Entity, specific=cm_repository_Interface)
gen_cm_repository_Signature_Entity = Generalization(general=Entity, specific=cm_repository_Signature)
gen_cm_repository_RequiredRole_Role = Generalization(general=Role, specific=cm_repository_RequiredRole)
gen_cm_repository_CompositeComponent_composition_ComposedProvidingRequiringEntity = Generalization(general=composition_ComposedProvidingRequiringEntity, specific=cm_repository_CompositeComponent)
gen_cm_repository_CompositeComponent_repository_ComponentTypeImplementation = Generalization(general=repository_ComponentTypeImplementation, specific=cm_repository_CompositeComponent)
gen_cm_repository_PrimitiveDataType_DataType = Generalization(general=DataType, specific=cm_repository_PrimitiveDataType)
gen_cm_repository_CollectionDataType_composition_Entity = Generalization(general=composition_Entity, specific=cm_repository_CollectionDataType)
gen_cm_repository_CollectionDataType_repository_DataType = Generalization(general=repository_DataType, specific=cm_repository_CollectionDataType)
gen_cm_repository_CompositeDataType_composition_Entity = Generalization(general=composition_Entity, specific=cm_repository_CompositeDataType)
gen_cm_repository_CompositeDataType_repository_DataType = Generalization(general=repository_DataType, specific=cm_repository_CompositeDataType)
gen_cm_repository_InnerDeclaration_NamedElement = Generalization(general=NamedElement, specific=cm_repository_InnerDeclaration)
gen_cm_composition_DelegationConnector_Connector = Generalization(general=Connector, specific=cm_composition_DelegationConnector)
gen_cm_composition_Connector_Entity = Generalization(general=Entity, specific=cm_composition_Connector)
gen_cm_composition_ComposedStructure_Entity = Generalization(general=Entity, specific=cm_composition_ComposedStructure)
gen_cm_composition_ProvidedDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=cm_composition_ProvidedDelegationConnector)
gen_cm_composition_RequiredDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=cm_composition_RequiredDelegationConnector)
gen_cm_composition_AssemblyConnector_Connector = Generalization(general=Connector, specific=cm_composition_AssemblyConnector)
gen_cm_composition_InterfaceRequiringEntity_Entity = Generalization(general=Entity, specific=cm_composition_InterfaceRequiringEntity)
gen_cm_composition_ComposedProvidingRequiringEntity_composition_ComposedStructure = Generalization(general=composition_ComposedStructure, specific=cm_composition_ComposedProvidingRequiringEntity)
gen_cm_composition_ComposedProvidingRequiringEntity_composition_InterfaceProvidingRequiringEntity = Generalization(general=composition_InterfaceProvidingRequiringEntity, specific=cm_composition_ComposedProvidingRequiringEntity)
gen_cm_composition_Entity_composition_NamedElement = Generalization(general=composition_NamedElement, specific=cm_composition_Entity)
gen_cm_composition_Entity_composition_Identifier = Generalization(general=composition_Identifier, specific=cm_composition_Entity)
gen_cm_composition_AssemblyContext_Entity = Generalization(general=Entity, specific=cm_composition_AssemblyContext)
gen_cm_composition_System_composition_Entity = Generalization(general=composition_Entity, specific=cm_composition_System)
gen_cm_composition_System_composition_ComposedProvidingRequiringEntity = Generalization(general=composition_ComposedProvidingRequiringEntity, specific=cm_composition_System)
gen_cm_composition_SubSystem_composition_ComposedProvidingRequiringEntity = Generalization(general=composition_ComposedProvidingRequiringEntity, specific=cm_composition_SubSystem)
gen_cm_composition_SubSystem_repository_RepositoryComponent = Generalization(general=repository_RepositoryComponent, specific=cm_composition_SubSystem)
gen_cm_composition_InterfaceProvidingRequiringEntity_composition_InterfaceProvidingEntity = Generalization(general=composition_InterfaceProvidingEntity, specific=cm_composition_InterfaceProvidingRequiringEntity)
gen_cm_composition_InterfaceProvidingRequiringEntity_composition_InterfaceRequiringEntity = Generalization(general=composition_InterfaceRequiringEntity, specific=cm_composition_InterfaceProvidingRequiringEntity)
gen_cm_composition_InterfaceProvidingEntity_Entity = Generalization(general=Entity, specific=cm_composition_InterfaceProvidingEntity)
gen_cm_seff_StartAction_AbstractAction = Generalization(general=AbstractAction, specific=cm_seff_StartAction)
gen_cm_seff_StopAction_AbstractAction = Generalization(general=AbstractAction, specific=cm_seff_StopAction)
gen_cm_seff_ExternalCallAction_AbstractAction = Generalization(general=AbstractAction, specific=cm_seff_ExternalCallAction)
gen_cm_seff_AbstractAction_Entity = Generalization(general=Entity, specific=cm_seff_AbstractAction)
gen_cm_seff_BranchAction_AbstractAction = Generalization(general=AbstractAction, specific=cm_seff_BranchAction)
gen_cm_seff_ProbabilisticBranchTransition_composition_Entity = Generalization(general=composition_Entity, specific=cm_seff_ProbabilisticBranchTransition)
gen_cm_seff_ProbabilisticBranchTransition_seff_Automaton = Generalization(general=seff_Automaton, specific=cm_seff_ProbabilisticBranchTransition)
gen_cm_seff_SimpleBehaviorSpecification_seff_ServiceEffectSpecification = Generalization(general=seff_ServiceEffectSpecification, specific=cm_seff_SimpleBehaviorSpecification)
gen_cm_seff_SimpleBehaviorSpecification_seff_Automaton = Generalization(general=seff_Automaton, specific=cm_seff_SimpleBehaviorSpecification)
gen_cm_seff_InternalAction_AbstractAction = Generalization(general=AbstractAction, specific=cm_seff_InternalAction)

# Domain Model
domain_model = DomainModel(
    name="cm",
    types={cm_repository_BasicComponent, ComponentTypeImplementation, ServiceEffectSpecification, cm_repository_ComponentTypeImplementation, RepositoryComponent, Repository, cm_repository_ComponentType, cm_repository_ProvidedRole, Role, InterfaceProvidingEntity, Interface, cm_repository_Parameter, DataType, Signature, cm_repository_DataType, cm_repository_Role, Entity, cm_repository_Repository, ComponentType, cm_repository_RepositoryComponent, InterfaceProvidingRequiringEntity, cm_repository_Interface, cm_repository_Signature, ExceptionType, Parameter_, cm_repository_ExceptionType, cm_repository_RequiredRole, InterfaceRequiringEntity, cm_repository_CompositeComponent, composition_ComposedProvidingRequiringEntity, repository_ComponentTypeImplementation, cm_repository_PrimitiveDataType, cm_repository_CollectionDataType, composition_Entity, repository_DataType, cm_repository_CompositeDataType, CompositeDataType, InnerDeclaration, cm_repository_InnerDeclaration, NamedElement, Connector, cm_composition_Connector, ComposedStructure, cm_composition_ComposedStructure, AssemblyContext, cm_composition_ProvidedDelegationConnector, DelegationConnector, RequiredRole, cm_composition_DelegationConnector, cm_composition_AssemblyConnector, cm_composition_InterfaceRequiringEntity, cm_composition_ComposedProvidingRequiringEntity, composition_ComposedStructure, composition_InterfaceProvidingRequiringEntity, cm_composition_NamedElement, cm_composition_Entity, composition_NamedElement, composition_Identifier, ProvidedRole, cm_composition_RequiredDelegationConnector, cm_composition_AssemblyContext, cm_composition_System, cm_composition_SubSystem, repository_RepositoryComponent, cm_composition_InterfaceProvidingRequiringEntity, composition_InterfaceProvidingEntity, composition_InterfaceRequiringEntity, cm_composition_InterfaceProvidingEntity, Automaton, cm_seff_StartAction, cm_seff_StopAction, cm_seff_ExternalCallAction, cm_composition_Identifier, cm_seff_ServiceEffectSpecification, BasicComponent, InternalBehaviour, cm_seff_InternalBehaviour, ProbabilisticBranchTransition, AbstractAction, cm_seff_AbstractAction, cm_seff_BranchAction, cm_seff_ProbabilisticBranchTransition, seff_Automaton, BranchAction, cm_seff_SimpleBehaviorSpecification, seff_ServiceEffectSpecification, cm_seff_InternalAction, cm_seff_Automaton, PrimitiveType},
    associations={serviceEffectSpecifications0, repository2, providingEntity3, providedInterface4, dataType5, signature6, repository7, components9, implementedComponentTypes1, parentInterfaces16, repository18, signatures20, exceptions22, parameters23, returnType24, interface27, requiringEntity29, requiredInterface30, interfaces10, dataTypes13, innerType32, parentType34, innerDeclaration35, dataType36, compositeDataType38, parentStructure40, assemblyContexts41, connectors42, innerRequiredRole51, outerRequiredRole52, assemblyContext55, providedRoles73, requiredRoles75, innerProvidedRole44, outerProvidedRole45, assemblyContext48, requiringAssemblyContext58, providingAssemblyContext60, providedRole63, requiredRole66, parentStructure69, encapsulatedComponent71, successor88, internalBehaviour90, specification92, calledService94, describedService77, basicComponent79, internalBehaviours80, serviceEffectSpecifications82, branchTransition84, steps85, predecessor86, role96, branchTransitions99, branchAction101, transition102, steps104},
    generalizations={gen_cm_repository_BasicComponent_ComponentTypeImplementation, gen_cm_repository_ComponentTypeImplementation_RepositoryComponent, gen_cm_repository_ComponentType_RepositoryComponent, gen_cm_repository_ProvidedRole_Role, gen_cm_repository_Role_Entity, gen_cm_repository_Repository_Entity, gen_cm_repository_RepositoryComponent_InterfaceProvidingRequiringEntity, gen_cm_repository_Interface_Entity, gen_cm_repository_Signature_Entity, gen_cm_repository_RequiredRole_Role, gen_cm_repository_CompositeComponent_composition_ComposedProvidingRequiringEntity, gen_cm_repository_CompositeComponent_repository_ComponentTypeImplementation, gen_cm_repository_PrimitiveDataType_DataType, gen_cm_repository_CollectionDataType_composition_Entity, gen_cm_repository_CollectionDataType_repository_DataType, gen_cm_repository_CompositeDataType_composition_Entity, gen_cm_repository_CompositeDataType_repository_DataType, gen_cm_repository_InnerDeclaration_NamedElement, gen_cm_composition_DelegationConnector_Connector, gen_cm_composition_Connector_Entity, gen_cm_composition_ComposedStructure_Entity, gen_cm_composition_ProvidedDelegationConnector_DelegationConnector, gen_cm_composition_RequiredDelegationConnector_DelegationConnector, gen_cm_composition_AssemblyConnector_Connector, gen_cm_composition_InterfaceRequiringEntity_Entity, gen_cm_composition_ComposedProvidingRequiringEntity_composition_ComposedStructure, gen_cm_composition_ComposedProvidingRequiringEntity_composition_InterfaceProvidingRequiringEntity, gen_cm_composition_Entity_composition_NamedElement, gen_cm_composition_Entity_composition_Identifier, gen_cm_composition_AssemblyContext_Entity, gen_cm_composition_System_composition_Entity, gen_cm_composition_System_composition_ComposedProvidingRequiringEntity, gen_cm_composition_SubSystem_composition_ComposedProvidingRequiringEntity, gen_cm_composition_SubSystem_repository_RepositoryComponent, gen_cm_composition_InterfaceProvidingRequiringEntity_composition_InterfaceProvidingEntity, gen_cm_composition_InterfaceProvidingRequiringEntity_composition_InterfaceRequiringEntity, gen_cm_composition_InterfaceProvidingEntity_Entity, gen_cm_seff_StartAction_AbstractAction, gen_cm_seff_StopAction_AbstractAction, gen_cm_seff_ExternalCallAction_AbstractAction, gen_cm_seff_AbstractAction_Entity, gen_cm_seff_BranchAction_AbstractAction, gen_cm_seff_ProbabilisticBranchTransition_composition_Entity, gen_cm_seff_ProbabilisticBranchTransition_seff_Automaton, gen_cm_seff_SimpleBehaviorSpecification_seff_ServiceEffectSpecification, gen_cm_seff_SimpleBehaviorSpecification_seff_Automaton, gen_cm_seff_InternalAction_AbstractAction},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)