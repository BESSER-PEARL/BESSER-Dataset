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
simpleTypes: Enumeration = Enumeration(
    name="simpleTypes",
    literals={
            EnumerationLiteral(name="int"),
			EnumerationLiteral(name="boolean"),
			EnumerationLiteral(name="char"),
			EnumerationLiteral(name="date"),
			EnumerationLiteral(name="double"),
			EnumerationLiteral(name="float"),
			EnumerationLiteral(name="list"),
			EnumerationLiteral(name="long"),
			EnumerationLiteral(name="map"),
			EnumerationLiteral(name="string")
    }
)

# Classes
componentBasedSystem_ComponentBasedSystem = Class(name="componentBasedSystem::ComponentBasedSystem")
componentBasedSystem_AssemblyContext = Class(name="componentBasedSystem::AssemblyContext")
componentBasedSystem_Service = Class(name="componentBasedSystem::Service")
componentBasedSystem_Interface = Class(name="componentBasedSystem::Interface")
componentBasedSystem_Signature = Class(name="componentBasedSystem::Signature")
componentBasedSystem_CompositeComponent = Class(name="componentBasedSystem::CompositeComponent")
Component = Class(name="Component")
componentBasedSystem_DelegationConnector = Class(name="componentBasedSystem::DelegationConnector")
componentBasedSystem_Container = Class(name="componentBasedSystem::Container")
Type = Class(name="Type")
AssemblyConnector = Class(name="AssemblyConnector")
componentBasedSystem_Allocation = Class(name="componentBasedSystem::Allocation")
componentBasedSystem_Repository = Class(name="componentBasedSystem::Repository")
componentBasedSystem_Environment = Class(name="componentBasedSystem::Environment")
ProvidedRole = Class(name="ProvidedRole")
RequiredRole = Class(name="RequiredRole")
componentBasedSystem_Component = Class(name="componentBasedSystem::Component")
BehaviourDescription = Class(name="BehaviourDescription")
Role = Class(name="Role")
componentBasedSystem_Link = Class(name="componentBasedSystem::Link")
componentBasedSystem_Parameter = Class(name="componentBasedSystem::Parameter")
ReturnType = Class(name="ReturnType")
ParameterType = Class(name="ParameterType")
componentBasedSystem_AllocationContext = Class(name="componentBasedSystem::AllocationContext")
componentBasedSystem_dataTypes_ParameterType = Class(name="componentBasedSystem::dataTypes::ParameterType")
componentBasedSystem_dataTypes_Void = Class(name="componentBasedSystem::dataTypes::Void")
componentBasedSystem_dataTypes_ReturnType = Class(name="componentBasedSystem::dataTypes::ReturnType")
componentBasedSystem_dataTypes_Type = Class(name="componentBasedSystem::dataTypes::Type")
componentBasedSystem_behaviourDescription_DescriptionElement = Class(name="componentBasedSystem::behaviourDescription::DescriptionElement")
componentBasedSystem_behaviourDescription_InternalAction = Class(name="componentBasedSystem::behaviourDescription::InternalAction")
DescriptionElement = Class(name="DescriptionElement")
componentBasedSystem_behaviourDescription_ExternalCall = Class(name="componentBasedSystem::behaviourDescription::ExternalCall")
componentBasedSystem_behaviourDescription_Loop = Class(name="componentBasedSystem::behaviourDescription::Loop")
componentBasedSystem_dataTypes_Simple = Class(name="componentBasedSystem::dataTypes::Simple")
dataTypes_ParameterType = Class(name="dataTypes::ParameterType")
dataTypes_ReturnType = Class(name="dataTypes::ReturnType")
componentBasedSystem_dataTypes_Complex = Class(name="componentBasedSystem::dataTypes::Complex")
Simple = Class(name="Simple")
roles_componentBasedSystem_AssemblyContext = Class(name="roles::componentBasedSystem::AssemblyContext")
componentBasedSystem_behaviourDescription_Branch = Class(name="componentBasedSystem::behaviourDescription::Branch")
componentBasedSystem_behaviourDescription_BehaviourDescription = Class(name="componentBasedSystem::behaviourDescription::BehaviourDescription")
componentBasedSystem_roles_Role = Class(name="componentBasedSystem::roles::Role")
roles_componentBasedSystem_Interface = Class(name="roles::componentBasedSystem::Interface")
componentBasedSystem_roles_RequiredRole = Class(name="componentBasedSystem::roles::RequiredRole")
componentBasedSystem_roles_ProvidedRole = Class(name="componentBasedSystem::roles::ProvidedRole")
componentBasedSystem_roles_AssemblyConnector = Class(name="componentBasedSystem::roles::AssemblyConnector")

# componentBasedSystem_ComponentBasedSystem class attributes and methods
componentBasedSystem_ComponentBasedSystem_m_GetContainerOfContext: Method = Method(name="GetContainerOfContext", parameters={Parameter(name='context')}, type=StringType)
componentBasedSystem_ComponentBasedSystem.methods={componentBasedSystem_ComponentBasedSystem_m_GetContainerOfContext}

# componentBasedSystem_AssemblyContext class attributes and methods
componentBasedSystem_AssemblyContext_name: Property = Property(name="name", type=StringType)
componentBasedSystem_AssemblyContext.attributes={componentBasedSystem_AssemblyContext_name}

# componentBasedSystem_Service class attributes and methods

# componentBasedSystem_Interface class attributes and methods
componentBasedSystem_Interface_name: Property = Property(name="name", type=StringType)
componentBasedSystem_Interface.attributes={componentBasedSystem_Interface_name}

# componentBasedSystem_Signature class attributes and methods
componentBasedSystem_Signature_name: Property = Property(name="name", type=StringType)
componentBasedSystem_Signature.attributes={componentBasedSystem_Signature_name}

# componentBasedSystem_CompositeComponent class attributes and methods

# Component class attributes and methods

# componentBasedSystem_DelegationConnector class attributes and methods
componentBasedSystem_DelegationConnector_name: Property = Property(name="name", type=StringType)
componentBasedSystem_DelegationConnector.attributes={componentBasedSystem_DelegationConnector_name}

# componentBasedSystem_Container class attributes and methods
componentBasedSystem_Container_name: Property = Property(name="name", type=StringType)
componentBasedSystem_Container.attributes={componentBasedSystem_Container_name}

# Type class attributes and methods

# AssemblyConnector class attributes and methods

# componentBasedSystem_Allocation class attributes and methods

# componentBasedSystem_Repository class attributes and methods

# componentBasedSystem_Environment class attributes and methods
componentBasedSystem_Environment_m_IsLinked: Method = Method(name="IsLinked", parameters={Parameter(name='c2'), Parameter(name='c1')}, type=BooleanType)
componentBasedSystem_Environment.methods={componentBasedSystem_Environment_m_IsLinked}

# ProvidedRole class attributes and methods

# RequiredRole class attributes and methods

# componentBasedSystem_Component class attributes and methods
componentBasedSystem_Component_name: Property = Property(name="name", type=StringType)
componentBasedSystem_Component.attributes={componentBasedSystem_Component_name}

# BehaviourDescription class attributes and methods

# Role class attributes and methods

# componentBasedSystem_Link class attributes and methods
componentBasedSystem_Link_name: Property = Property(name="name", type=StringType)
componentBasedSystem_Link.attributes={componentBasedSystem_Link_name}

# componentBasedSystem_Parameter class attributes and methods
componentBasedSystem_Parameter_name: Property = Property(name="name", type=StringType)
componentBasedSystem_Parameter.attributes={componentBasedSystem_Parameter_name}

# ReturnType class attributes and methods

# ParameterType class attributes and methods

# componentBasedSystem_AllocationContext class attributes and methods

# componentBasedSystem_dataTypes_ParameterType class attributes and methods

# componentBasedSystem_dataTypes_Void class attributes and methods

# componentBasedSystem_dataTypes_ReturnType class attributes and methods

# componentBasedSystem_dataTypes_Type class attributes and methods
componentBasedSystem_dataTypes_Type_name: Property = Property(name="name", type=StringType)
componentBasedSystem_dataTypes_Type.attributes={componentBasedSystem_dataTypes_Type_name}

# componentBasedSystem_behaviourDescription_DescriptionElement class attributes and methods

# componentBasedSystem_behaviourDescription_InternalAction class attributes and methods

# DescriptionElement class attributes and methods

# componentBasedSystem_behaviourDescription_ExternalCall class attributes and methods

# componentBasedSystem_behaviourDescription_Loop class attributes and methods

# componentBasedSystem_dataTypes_Simple class attributes and methods
componentBasedSystem_dataTypes_Simple_kind: Property = Property(name="kind", type=StringType)
componentBasedSystem_dataTypes_Simple.attributes={componentBasedSystem_dataTypes_Simple_kind}

# dataTypes_ParameterType class attributes and methods

# dataTypes_ReturnType class attributes and methods

# componentBasedSystem_dataTypes_Complex class attributes and methods

# Simple class attributes and methods

# roles_componentBasedSystem_AssemblyContext class attributes and methods

# componentBasedSystem_behaviourDescription_Branch class attributes and methods

# componentBasedSystem_behaviourDescription_BehaviourDescription class attributes and methods

# componentBasedSystem_roles_Role class attributes and methods
componentBasedSystem_roles_Role_name: Property = Property(name="name", type=StringType)
componentBasedSystem_roles_Role.attributes={componentBasedSystem_roles_Role_name}

# roles_componentBasedSystem_Interface class attributes and methods

# componentBasedSystem_roles_RequiredRole class attributes and methods

# componentBasedSystem_roles_ProvidedRole class attributes and methods

# componentBasedSystem_roles_AssemblyConnector class attributes and methods
componentBasedSystem_roles_AssemblyConnector_name: Property = Property(name="name", type=StringType)
componentBasedSystem_roles_AssemblyConnector.attributes={componentBasedSystem_roles_AssemblyConnector_name}

# Relationships
assemblycontext0: BinaryAssociation = BinaryAssociation(
    name="assemblycontext0",
    ends={
        Property(name="componentBasedSystem_AssemblyContext", type=componentBasedSystem_ComponentBasedSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="componentBasedSystem_ComponentBasedSystem", type=componentBasedSystem_AssemblyContext, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
service16: BinaryAssociation = BinaryAssociation(
    name="service16",
    ends={
        Property(name="componentBasedSystem_Service", type=componentBasedSystem_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="componentBasedSystem_Component17", type=componentBasedSystem_Service, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
requiredrole18: BinaryAssociation = BinaryAssociation(
    name="requiredrole18",
    ends={
        Property(name="RequiredRole20", type=componentBasedSystem_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="componentBasedSystem_Component19", type=RequiredRole, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
providedrole21: BinaryAssociation = BinaryAssociation(
    name="providedrole21",
    ends={
        Property(name="ProvidedRole23", type=componentBasedSystem_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="componentBasedSystem_Component22", type=ProvidedRole, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
signature24: BinaryAssociation = BinaryAssociation(
    name="signature24",
    ends={
        Property(name="componentBasedSystem_Signature", type=componentBasedSystem_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="componentBasedSystem_Interface", type=componentBasedSystem_Signature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
assemblycontext25: BinaryAssociation = BinaryAssociation(
    name="assemblycontext25",
    ends={
        Property(name="componentBasedSystem_AssemblyContext26", type=componentBasedSystem_CompositeComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="componentBasedSystem_CompositeComponent", type=componentBasedSystem_AssemblyContext, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
delegationconnector27: BinaryAssociation = BinaryAssociation(
    name="delegationconnector27",
    ends={
        Property(name="componentBasedSystem_DelegationConnector", type=componentBasedSystem_CompositeComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="componentBasedSystem_CompositeComponent28", type=componentBasedSystem_DelegationConnector, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
type1: BinaryAssociation = BinaryAssociation(
    name="type1",
    ends={
        Property(name="Type", type=componentBasedSystem_ComponentBasedSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="componentBasedSystem_ComponentBasedSystem2", type=Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
assemblyconnector3: BinaryAssociation = BinaryAssociation(
    name="assemblyconnector3",
    ends={
        Property(name="AssemblyConnector", type=componentBasedSystem_ComponentBasedSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="componentBasedSystem_ComponentBasedSystem4", type=AssemblyConnector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
allocation5: BinaryAssociation = BinaryAssociation(
    name="allocation5",
    ends={
        Property(name="componentBasedSystem_Allocation", type=componentBasedSystem_ComponentBasedSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="componentBasedSystem_ComponentBasedSystem6", type=componentBasedSystem_Allocation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
repository7: BinaryAssociation = BinaryAssociation(
    name="repository7",
    ends={
        Property(name="componentBasedSystem_Repository", type=componentBasedSystem_ComponentBasedSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="componentBasedSystem_ComponentBasedSystem8", type=componentBasedSystem_Repository, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
environment9: BinaryAssociation = BinaryAssociation(
    name="environment9",
    ends={
        Property(name="componentBasedSystem_Environment", type=componentBasedSystem_ComponentBasedSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="componentBasedSystem_ComponentBasedSystem10", type=componentBasedSystem_Environment, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
providedrole11: BinaryAssociation = BinaryAssociation(
    name="providedrole11",
    ends={
        Property(name="ProvidedRole", type=componentBasedSystem_ComponentBasedSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="componentBasedSystem_ComponentBasedSystem12", type=ProvidedRole, multiplicity=Multiplicity(1, 9999))
    }
)
requiredrole13: BinaryAssociation = BinaryAssociation(
    name="requiredrole13",
    ends={
        Property(name="RequiredRole", type=componentBasedSystem_ComponentBasedSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="componentBasedSystem_ComponentBasedSystem14", type=RequiredRole, multiplicity=Multiplicity(0, 9999))
    }
)
behaviourdescription15: BinaryAssociation = BinaryAssociation(
    name="behaviourdescription15",
    ends={
        Property(name="BehaviourDescription", type=componentBasedSystem_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="componentBasedSystem_Component", type=BehaviourDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
assemblycontext41: BinaryAssociation = BinaryAssociation(
    name="assemblycontext41",
    ends={
        Property(name="componentBasedSystem_AssemblyContext43", type=componentBasedSystem_AllocationContext, multiplicity=Multiplicity(1, 1)),
        Property(name="componentBasedSystem_AllocationContext42", type=componentBasedSystem_AssemblyContext, multiplicity=Multiplicity(1, 1))
    }
)
role44: BinaryAssociation = BinaryAssociation(
    name="role44",
    ends={
        Property(name="Role", type=componentBasedSystem_DelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="componentBasedSystem_DelegationConnector45", type=Role, multiplicity=Multiplicity(2, 2))
    }
)
container46: BinaryAssociation = BinaryAssociation(
    name="container46",
    ends={
        Property(name="componentBasedSystem_Container48", type=componentBasedSystem_Environment, multiplicity=Multiplicity(1, 1)),
        Property(name="componentBasedSystem_Environment47", type=componentBasedSystem_Container, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
link49: BinaryAssociation = BinaryAssociation(
    name="link49",
    ends={
        Property(name="componentBasedSystem_Link51", type=componentBasedSystem_Environment, multiplicity=Multiplicity(1, 1)),
        Property(name="componentBasedSystem_Environment50", type=componentBasedSystem_Link, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
container29: BinaryAssociation = BinaryAssociation(
    name="container29",
    ends={
        Property(name="componentBasedSystem_Container", type=componentBasedSystem_Link, multiplicity=Multiplicity(1, 1)),
        Property(name="componentBasedSystem_Link", type=componentBasedSystem_Container, multiplicity=Multiplicity(2, 9999))
    }
)
parameter30: BinaryAssociation = BinaryAssociation(
    name="parameter30",
    ends={
        Property(name="componentBasedSystem_Parameter", type=componentBasedSystem_Signature, multiplicity=Multiplicity(1, 1)),
        Property(name="componentBasedSystem_Signature31", type=componentBasedSystem_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returntype32: BinaryAssociation = BinaryAssociation(
    name="returntype32",
    ends={
        Property(name="ReturnType", type=componentBasedSystem_Signature, multiplicity=Multiplicity(1, 1)),
        Property(name="componentBasedSystem_Signature33", type=ReturnType, multiplicity=Multiplicity(1, 1))
    }
)
parametertype34: BinaryAssociation = BinaryAssociation(
    name="parametertype34",
    ends={
        Property(name="ParameterType", type=componentBasedSystem_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="componentBasedSystem_Parameter35", type=ParameterType, multiplicity=Multiplicity(1, 1))
    }
)
component36: BinaryAssociation = BinaryAssociation(
    name="component36",
    ends={
        Property(name="componentBasedSystem_Component38", type=componentBasedSystem_AssemblyContext, multiplicity=Multiplicity(1, 1)),
        Property(name="componentBasedSystem_AssemblyContext37", type=componentBasedSystem_Component, multiplicity=Multiplicity(1, 1))
    }
)
container39: BinaryAssociation = BinaryAssociation(
    name="container39",
    ends={
        Property(name="componentBasedSystem_Container40", type=componentBasedSystem_AllocationContext, multiplicity=Multiplicity(1, 1)),
        Property(name="componentBasedSystem_AllocationContext", type=componentBasedSystem_Container, multiplicity=Multiplicity(1, 1))
    }
)
descriptionelement65: BinaryAssociation = BinaryAssociation(
    name="descriptionelement65",
    ends={
        Property(name="DescriptionElement", type=componentBasedSystem_behaviourDescription_Loop, multiplicity=Multiplicity(1, 1)),
        Property(name="componentBasedSystem_behaviourDescription_Loop", type=DescriptionElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
interface52: BinaryAssociation = BinaryAssociation(
    name="interface52",
    ends={
        Property(name="componentBasedSystem_Interface54", type=componentBasedSystem_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="componentBasedSystem_Repository53", type=componentBasedSystem_Interface, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
component55: BinaryAssociation = BinaryAssociation(
    name="component55",
    ends={
        Property(name="componentBasedSystem_Component57", type=componentBasedSystem_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="componentBasedSystem_Repository56", type=componentBasedSystem_Component, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
allocationcontext58: BinaryAssociation = BinaryAssociation(
    name="allocationcontext58",
    ends={
        Property(name="componentBasedSystem_AllocationContext60", type=componentBasedSystem_Allocation, multiplicity=Multiplicity(1, 1)),
        Property(name="componentBasedSystem_Allocation59", type=componentBasedSystem_AllocationContext, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
correspondingSignatures61: BinaryAssociation = BinaryAssociation(
    name="correspondingSignatures61",
    ends={
        Property(name="componentBasedSystem_Signature63", type=componentBasedSystem_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="componentBasedSystem_Service62", type=componentBasedSystem_Signature, multiplicity=Multiplicity(1, 9999))
    }
)
simple64: BinaryAssociation = BinaryAssociation(
    name="simple64",
    ends={
        Property(name="Simple", type=componentBasedSystem_dataTypes_Complex, multiplicity=Multiplicity(1, 1)),
        Property(name="componentBasedSystem_dataTypes_Complex", type=Simple, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
providedAssemblyContext76: BinaryAssociation = BinaryAssociation(
    name="providedAssemblyContext76",
    ends={
        Property(name="roles_componentBasedSystem_AssemblyContext", type=componentBasedSystem_roles_AssemblyConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="componentBasedSystem_roles_AssemblyConnector77", type=roles_componentBasedSystem_AssemblyContext, multiplicity=Multiplicity(1, 1))
    }
)
requiredAssemblyContext78: BinaryAssociation = BinaryAssociation(
    name="requiredAssemblyContext78",
    ends={
        Property(name="roles_componentBasedSystem_AssemblyContext80", type=componentBasedSystem_roles_AssemblyConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="componentBasedSystem_roles_AssemblyConnector79", type=roles_componentBasedSystem_AssemblyContext, multiplicity=Multiplicity(1, 1))
    }
)
descriptionelement66: BinaryAssociation = BinaryAssociation(
    name="descriptionelement66",
    ends={
        Property(name="DescriptionElement67", type=componentBasedSystem_behaviourDescription_Branch, multiplicity=Multiplicity(1, 1)),
        Property(name="componentBasedSystem_behaviourDescription_Branch", type=DescriptionElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
descriptionelement68: BinaryAssociation = BinaryAssociation(
    name="descriptionelement68",
    ends={
        Property(name="DescriptionElement69", type=componentBasedSystem_behaviourDescription_BehaviourDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="componentBasedSystem_behaviourDescription_BehaviourDescription", type=DescriptionElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
interface70: BinaryAssociation = BinaryAssociation(
    name="interface70",
    ends={
        Property(name="roles_componentBasedSystem_Interface", type=componentBasedSystem_roles_Role, multiplicity=Multiplicity(1, 1)),
        Property(name="componentBasedSystem_roles_Role", type=roles_componentBasedSystem_Interface, multiplicity=Multiplicity(1, 1))
    }
)
providedrole71: BinaryAssociation = BinaryAssociation(
    name="providedrole71",
    ends={
        Property(name="ProvidedRole72", type=componentBasedSystem_roles_AssemblyConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="componentBasedSystem_roles_AssemblyConnector", type=ProvidedRole, multiplicity=Multiplicity(1, 1))
    }
)
requiredrole73: BinaryAssociation = BinaryAssociation(
    name="requiredrole73",
    ends={
        Property(name="RequiredRole75", type=componentBasedSystem_roles_AssemblyConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="componentBasedSystem_roles_AssemblyConnector74", type=RequiredRole, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_componentBasedSystem_CompositeComponent_Component = Generalization(general=Component, specific=componentBasedSystem_CompositeComponent)
gen_componentBasedSystem_dataTypes_ParameterType_Type = Generalization(general=Type, specific=componentBasedSystem_dataTypes_ParameterType)
gen_componentBasedSystem_dataTypes_Void_ReturnType = Generalization(general=ReturnType, specific=componentBasedSystem_dataTypes_Void)
gen_componentBasedSystem_dataTypes_ReturnType_Type = Generalization(general=Type, specific=componentBasedSystem_dataTypes_ReturnType)
gen_componentBasedSystem_behaviourDescription_InternalAction_DescriptionElement = Generalization(general=DescriptionElement, specific=componentBasedSystem_behaviourDescription_InternalAction)
gen_componentBasedSystem_behaviourDescription_ExternalCall_DescriptionElement = Generalization(general=DescriptionElement, specific=componentBasedSystem_behaviourDescription_ExternalCall)
gen_componentBasedSystem_behaviourDescription_Loop_DescriptionElement = Generalization(general=DescriptionElement, specific=componentBasedSystem_behaviourDescription_Loop)
gen_componentBasedSystem_dataTypes_Simple_dataTypes_ParameterType = Generalization(general=dataTypes_ParameterType, specific=componentBasedSystem_dataTypes_Simple)
gen_componentBasedSystem_dataTypes_Simple_dataTypes_ReturnType = Generalization(general=dataTypes_ReturnType, specific=componentBasedSystem_dataTypes_Simple)
gen_componentBasedSystem_dataTypes_Complex_dataTypes_ReturnType = Generalization(general=dataTypes_ReturnType, specific=componentBasedSystem_dataTypes_Complex)
gen_componentBasedSystem_dataTypes_Complex_dataTypes_ParameterType = Generalization(general=dataTypes_ParameterType, specific=componentBasedSystem_dataTypes_Complex)
gen_componentBasedSystem_behaviourDescription_Branch_DescriptionElement = Generalization(general=DescriptionElement, specific=componentBasedSystem_behaviourDescription_Branch)
gen_componentBasedSystem_roles_RequiredRole_Role = Generalization(general=Role, specific=componentBasedSystem_roles_RequiredRole)
gen_componentBasedSystem_roles_ProvidedRole_Role = Generalization(general=Role, specific=componentBasedSystem_roles_ProvidedRole)

# Domain Model
domain_model = DomainModel(
    name="componentBasedSystem",
    types={componentBasedSystem_ComponentBasedSystem, componentBasedSystem_AssemblyContext, componentBasedSystem_Service, componentBasedSystem_Interface, componentBasedSystem_Signature, componentBasedSystem_CompositeComponent, Component, componentBasedSystem_DelegationConnector, componentBasedSystem_Container, Type, AssemblyConnector, componentBasedSystem_Allocation, componentBasedSystem_Repository, componentBasedSystem_Environment, ProvidedRole, RequiredRole, componentBasedSystem_Component, BehaviourDescription, Role, componentBasedSystem_Link, componentBasedSystem_Parameter, ReturnType, ParameterType, componentBasedSystem_AllocationContext, componentBasedSystem_dataTypes_ParameterType, componentBasedSystem_dataTypes_Void, componentBasedSystem_dataTypes_ReturnType, componentBasedSystem_dataTypes_Type, componentBasedSystem_behaviourDescription_DescriptionElement, componentBasedSystem_behaviourDescription_InternalAction, DescriptionElement, componentBasedSystem_behaviourDescription_ExternalCall, componentBasedSystem_behaviourDescription_Loop, componentBasedSystem_dataTypes_Simple, dataTypes_ParameterType, dataTypes_ReturnType, componentBasedSystem_dataTypes_Complex, Simple, roles_componentBasedSystem_AssemblyContext, componentBasedSystem_behaviourDescription_Branch, componentBasedSystem_behaviourDescription_BehaviourDescription, componentBasedSystem_roles_Role, roles_componentBasedSystem_Interface, componentBasedSystem_roles_RequiredRole, componentBasedSystem_roles_ProvidedRole, componentBasedSystem_roles_AssemblyConnector, simpleTypes},
    associations={assemblycontext0, service16, requiredrole18, providedrole21, signature24, assemblycontext25, delegationconnector27, type1, assemblyconnector3, allocation5, repository7, environment9, providedrole11, requiredrole13, behaviourdescription15, assemblycontext41, role44, container46, link49, container29, parameter30, returntype32, parametertype34, component36, container39, descriptionelement65, interface52, component55, allocationcontext58, correspondingSignatures61, simple64, providedAssemblyContext76, requiredAssemblyContext78, descriptionelement66, descriptionelement68, interface70, providedrole71, requiredrole73},
    generalizations={gen_componentBasedSystem_CompositeComponent_Component, gen_componentBasedSystem_dataTypes_ParameterType_Type, gen_componentBasedSystem_dataTypes_Void_ReturnType, gen_componentBasedSystem_dataTypes_ReturnType_Type, gen_componentBasedSystem_behaviourDescription_InternalAction_DescriptionElement, gen_componentBasedSystem_behaviourDescription_ExternalCall_DescriptionElement, gen_componentBasedSystem_behaviourDescription_Loop_DescriptionElement, gen_componentBasedSystem_dataTypes_Simple_dataTypes_ParameterType, gen_componentBasedSystem_dataTypes_Simple_dataTypes_ReturnType, gen_componentBasedSystem_dataTypes_Complex_dataTypes_ReturnType, gen_componentBasedSystem_dataTypes_Complex_dataTypes_ParameterType, gen_componentBasedSystem_behaviourDescription_Branch_DescriptionElement, gen_componentBasedSystem_roles_RequiredRole_Role, gen_componentBasedSystem_roles_ProvidedRole_Role},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)