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

# Classes
componentModel_Interface = Class(name="componentModel::Interface")
componentModel_ServiceEffectSpecification = Class(name="componentModel::ServiceEffectSpecification")
componentModel_InterfaceServiceMapTuple = Class(name="componentModel::InterfaceServiceMapTuple")
componentModel_SystemIndependentViewPoint = Class(name="componentModel::SystemIndependentViewPoint")
ViewPoint = Class(name="ViewPoint")
componentModel_Repository = Class(name="componentModel::Repository")
ViewType = Class(name="ViewType")
componentModel_Component = Class(name="componentModel::Component")
componentModel_RequiredRole = Class(name="componentModel::RequiredRole")
componentModel_AssemblyConnector = Class(name="componentModel::AssemblyConnector")
componentModel_DelegationConnector = Class(name="componentModel::DelegationConnector", is_abstract=True)
componentModel_Service = Class(name="componentModel::Service")
componentModel_Action = Class(name="componentModel::Action")
componentModel_Branch = Class(name="componentModel::Branch")
Action = Class(name="Action")
componentModel_Loop = Class(name="componentModel::Loop")
componentModel_ExternalCall = Class(name="componentModel::ExternalCall")
componentModel_InternalAction = Class(name="componentModel::InternalAction")
componentModel_Signature = Class(name="componentModel::Signature")
componentModel_ViewType = Class(name="componentModel::ViewType", is_abstract=True)
componentModel_AssemblyViewPoint = Class(name="componentModel::AssemblyViewPoint")
componentModel_AssemblyContext = Class(name="componentModel::AssemblyContext")
AssemblyViewType = Class(name="AssemblyViewType")
componentModel_ProvidedRole = Class(name="componentModel::ProvidedRole")
componentModel_ViewPoint = Class(name="componentModel::ViewPoint", is_abstract=True)
componentModel_CompositeComponent = Class(name="componentModel::CompositeComponent")
Component = Class(name="Component")
componentModel_RequiredDelegationConnector = Class(name="componentModel::RequiredDelegationConnector")
DelegationConnector = Class(name="DelegationConnector")
componentModel_Parameter = Class(name="componentModel::Parameter")
componentModel_Type = Class(name="componentModel::Type", is_abstract=True)
componentModel_System = Class(name="componentModel::System")
componentModel_ProvidedDelegationConnector = Class(name="componentModel::ProvidedDelegationConnector")
componentModel_AssemblyViewType = Class(name="componentModel::AssemblyViewType")
componentModel_DeploymentViewPoint = Class(name="componentModel::DeploymentViewPoint")
componentModel_RepositoryViewType = Class(name="componentModel::RepositoryViewType")
componentModel_EnvironmentViewType = Class(name="componentModel::EnvironmentViewType")
componentModel_AllocationViewType = Class(name="componentModel::AllocationViewType")
SimpleParameterType = Class(name="SimpleParameterType")
componentModel_ParameterTyp = Class(name="componentModel::ParameterTyp", is_abstract=True)
componentModel_Boolean = Class(name="componentModel::Boolean")
componentModel_Void = Class(name="componentModel::Void", is_abstract=True)
Type = Class(name="Type")
componentModel_Char = Class(name="componentModel::Char")
componentModel_Date = Class(name="componentModel::Date")
componentModel_Float = Class(name="componentModel::Float")
componentModel_List = Class(name="componentModel::List")
componentModel_Int = Class(name="componentModel::Int")
componentModel_Long = Class(name="componentModel::Long")
componentModel_Map = Class(name="componentModel::Map")
componentModel_String = Class(name="componentModel::String")
componentModel_Double = Class(name="componentModel::Double")
componentModel_ComplexParameterType = Class(name="componentModel::ComplexParameterType")
ParameterTyp = Class(name="ParameterTyp")
componentModel_SimpleParameterType = Class(name="componentModel::SimpleParameterType", is_abstract=True)

# componentModel_Interface class attributes and methods
componentModel_Interface_name: Property = Property(name="name", type=StringType)
componentModel_Interface.attributes={componentModel_Interface_name}

# componentModel_ServiceEffectSpecification class attributes and methods

# componentModel_InterfaceServiceMapTuple class attributes and methods

# componentModel_SystemIndependentViewPoint class attributes and methods

# ViewPoint class attributes and methods

# componentModel_Repository class attributes and methods

# ViewType class attributes and methods

# componentModel_Component class attributes and methods
componentModel_Component_name: Property = Property(name="name", type=StringType)
componentModel_Component.attributes={componentModel_Component_name}

# componentModel_RequiredRole class attributes and methods
componentModel_RequiredRole_name: Property = Property(name="name", type=StringType)
componentModel_RequiredRole.attributes={componentModel_RequiredRole_name}

# componentModel_AssemblyConnector class attributes and methods

# componentModel_DelegationConnector class attributes and methods

# componentModel_Service class attributes and methods

# componentModel_Action class attributes and methods

# componentModel_Branch class attributes and methods

# Action class attributes and methods

# componentModel_Loop class attributes and methods

# componentModel_ExternalCall class attributes and methods

# componentModel_InternalAction class attributes and methods

# componentModel_Signature class attributes and methods
componentModel_Signature_name: Property = Property(name="name", type=StringType)
componentModel_Signature.attributes={componentModel_Signature_name}

# componentModel_ViewType class attributes and methods

# componentModel_AssemblyViewPoint class attributes and methods

# componentModel_AssemblyContext class attributes and methods
componentModel_AssemblyContext_name: Property = Property(name="name", type=StringType)
componentModel_AssemblyContext.attributes={componentModel_AssemblyContext_name}

# AssemblyViewType class attributes and methods

# componentModel_ProvidedRole class attributes and methods
componentModel_ProvidedRole_name: Property = Property(name="name", type=StringType)
componentModel_ProvidedRole.attributes={componentModel_ProvidedRole_name}

# componentModel_ViewPoint class attributes and methods

# componentModel_CompositeComponent class attributes and methods

# Component class attributes and methods

# componentModel_RequiredDelegationConnector class attributes and methods

# DelegationConnector class attributes and methods

# componentModel_Parameter class attributes and methods
componentModel_Parameter_name: Property = Property(name="name", type=StringType)
componentModel_Parameter.attributes={componentModel_Parameter_name}

# componentModel_Type class attributes and methods

# componentModel_System class attributes and methods

# componentModel_ProvidedDelegationConnector class attributes and methods

# componentModel_AssemblyViewType class attributes and methods

# componentModel_DeploymentViewPoint class attributes and methods

# componentModel_RepositoryViewType class attributes and methods

# componentModel_EnvironmentViewType class attributes and methods

# componentModel_AllocationViewType class attributes and methods

# SimpleParameterType class attributes and methods

# componentModel_ParameterTyp class attributes and methods

# componentModel_Boolean class attributes and methods

# componentModel_Void class attributes and methods

# Type class attributes and methods

# componentModel_Char class attributes and methods

# componentModel_Date class attributes and methods

# componentModel_Float class attributes and methods

# componentModel_List class attributes and methods

# componentModel_Int class attributes and methods

# componentModel_Long class attributes and methods

# componentModel_Map class attributes and methods

# componentModel_String class attributes and methods

# componentModel_Double class attributes and methods

# componentModel_ComplexParameterType class attributes and methods

# ParameterTyp class attributes and methods

# componentModel_SimpleParameterType class attributes and methods

# Relationships
interface1: BinaryAssociation = BinaryAssociation(
    name="interface1",
    ends={
        Property(name="componentModel_Interface", type=componentModel_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="componentModel_Repository2", type=componentModel_Interface, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
serviceeffectspecification3: BinaryAssociation = BinaryAssociation(
    name="serviceeffectspecification3",
    ends={
        Property(name="componentModel_ServiceEffectSpecification", type=componentModel_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="componentModel_Component4", type=componentModel_ServiceEffectSpecification, multiplicity=Multiplicity(0, 1))
    }
)
component0: BinaryAssociation = BinaryAssociation(
    name="component0",
    ends={
        Property(name="componentModel_Component", type=componentModel_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="componentModel_Repository", type=componentModel_Component, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredrole27: BinaryAssociation = BinaryAssociation(
    name="requiredrole27",
    ends={
        Property(name="RequiredRole", type=componentModel_AssemblyContext, multiplicity=Multiplicity(1, 1)),
        Property(name="assemblycontext28", type=componentModel_RequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
ownerComponent29: BinaryAssociation = BinaryAssociation(
    name="ownerComponent29",
    ends={
        Property(name="componentModel_Component30", type=componentModel_AssemblyContext, multiplicity=Multiplicity(1, 1)),
        Property(name="componentModel_AssemblyContext", type=componentModel_Component, multiplicity=Multiplicity(0, 1))
    }
)
providedrole31: BinaryAssociation = BinaryAssociation(
    name="providedrole31",
    ends={
        Property(name="componentModel_ProvidedRole", type=componentModel_AssemblyConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="componentModel_AssemblyConnector32", type=componentModel_ProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
interfaceServiceMap5: BinaryAssociation = BinaryAssociation(
    name="interfaceServiceMap5",
    ends={
        Property(name="componentModel_InterfaceServiceMapTuple", type=componentModel_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="componentModel_Component6", type=componentModel_InterfaceServiceMapTuple, multiplicity=Multiplicity(0, 9999))
    }
)
assemblyConnectors7: BinaryAssociation = BinaryAssociation(
    name="assemblyConnectors7",
    ends={
        Property(name="componentModel_AssemblyConnector", type=componentModel_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="componentModel_Component8", type=componentModel_AssemblyConnector, multiplicity=Multiplicity(0, 9999))
    }
)
delegationConnectors9: BinaryAssociation = BinaryAssociation(
    name="delegationConnectors9",
    ends={
        Property(name="componentModel_DelegationConnector", type=componentModel_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="componentModel_Component10", type=componentModel_DelegationConnector, multiplicity=Multiplicity(0, 9999))
    }
)
providedInterface11: BinaryAssociation = BinaryAssociation(
    name="providedInterface11",
    ends={
        Property(name="componentModel_Interface13", type=componentModel_InterfaceServiceMapTuple, multiplicity=Multiplicity(1, 1)),
        Property(name="componentModel_InterfaceServiceMapTuple12", type=componentModel_Interface, multiplicity=Multiplicity(0, 1))
    }
)
service14: BinaryAssociation = BinaryAssociation(
    name="service14",
    ends={
        Property(name="componentModel_Service", type=componentModel_InterfaceServiceMapTuple, multiplicity=Multiplicity(1, 1)),
        Property(name="componentModel_InterfaceServiceMapTuple15", type=componentModel_Service, multiplicity=Multiplicity(0, 9999))
    }
)
actions16: BinaryAssociation = BinaryAssociation(
    name="actions16",
    ends={
        Property(name="componentModel_Action", type=componentModel_ServiceEffectSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="componentModel_ServiceEffectSpecification17", type=componentModel_Action, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
actions18: BinaryAssociation = BinaryAssociation(
    name="actions18",
    ends={
        Property(name="componentModel_Action19", type=componentModel_Branch, multiplicity=Multiplicity(1, 1)),
        Property(name="componentModel_Branch", type=componentModel_Action, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
actions20: BinaryAssociation = BinaryAssociation(
    name="actions20",
    ends={
        Property(name="componentModel_Action21", type=componentModel_Loop, multiplicity=Multiplicity(1, 1)),
        Property(name="componentModel_Loop", type=componentModel_Action, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
requiredService22: BinaryAssociation = BinaryAssociation(
    name="requiredService22",
    ends={
        Property(name="componentModel_Service23", type=componentModel_ExternalCall, multiplicity=Multiplicity(1, 1)),
        Property(name="componentModel_ExternalCall", type=componentModel_Service, multiplicity=Multiplicity(0, 1))
    }
)
signatures24: BinaryAssociation = BinaryAssociation(
    name="signatures24",
    ends={
        Property(name="componentModel_Signature", type=componentModel_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="componentModel_Interface25", type=componentModel_Signature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
providedrole26: BinaryAssociation = BinaryAssociation(
    name="providedrole26",
    ends={
        Property(name="ProvidedRole", type=componentModel_AssemblyContext, multiplicity=Multiplicity(1, 1)),
        Property(name="assemblycontext", type=componentModel_ProvidedRole, multiplicity=Multiplicity(0, 1))
    }
)
providedrole66: BinaryAssociation = BinaryAssociation(
    name="providedrole66",
    ends={
        Property(name="componentModel_ProvidedRole68", type=componentModel_ProvidedDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="componentModel_ProvidedDelegationConnector67", type=componentModel_ProvidedRole, multiplicity=Multiplicity(1, 1))
    }
)
viewTypes69: BinaryAssociation = BinaryAssociation(
    name="viewTypes69",
    ends={
        Property(name="componentModel_ViewType", type=componentModel_ViewPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="componentModel_ViewPoint", type=componentModel_ViewType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredrole33: BinaryAssociation = BinaryAssociation(
    name="requiredrole33",
    ends={
        Property(name="componentModel_RequiredRole", type=componentModel_AssemblyConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="componentModel_AssemblyConnector34", type=componentModel_RequiredRole, multiplicity=Multiplicity(0, 1))
    }
)
requiredrole35: BinaryAssociation = BinaryAssociation(
    name="requiredrole35",
    ends={
        Property(name="componentModel_RequiredRole36", type=componentModel_RequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="componentModel_RequiredDelegationConnector", type=componentModel_RequiredRole, multiplicity=Multiplicity(1, 1))
    }
)
requiredInterface37: BinaryAssociation = BinaryAssociation(
    name="requiredInterface37",
    ends={
        Property(name="componentModel_Interface39", type=componentModel_RequiredDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="componentModel_RequiredDelegationConnector38", type=componentModel_Interface, multiplicity=Multiplicity(1, 1))
    }
)
parameters40: BinaryAssociation = BinaryAssociation(
    name="parameters40",
    ends={
        Property(name="componentModel_Parameter", type=componentModel_Signature, multiplicity=Multiplicity(1, 1)),
        Property(name="componentModel_Signature41", type=componentModel_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnType42: BinaryAssociation = BinaryAssociation(
    name="returnType42",
    ends={
        Property(name="componentModel_Type", type=componentModel_Signature, multiplicity=Multiplicity(1, 1)),
        Property(name="componentModel_Signature43", type=componentModel_Type, multiplicity=Multiplicity(1, 1))
    }
)
required44: BinaryAssociation = BinaryAssociation(
    name="required44",
    ends={
        Property(name="componentModel_Interface46", type=componentModel_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="componentModel_Service45", type=componentModel_Interface, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
correspondence47: BinaryAssociation = BinaryAssociation(
    name="correspondence47",
    ends={
        Property(name="componentModel_Signature49", type=componentModel_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="componentModel_Service48", type=componentModel_Signature, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
assemblycontext50: BinaryAssociation = BinaryAssociation(
    name="assemblycontext50",
    ends={
        Property(name="componentModel_AssemblyContext51", type=componentModel_System, multiplicity=Multiplicity(1, 1)),
        Property(name="componentModel_System", type=componentModel_AssemblyContext, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
interface52: BinaryAssociation = BinaryAssociation(
    name="interface52",
    ends={
        Property(name="componentModel_Interface54", type=componentModel_System, multiplicity=Multiplicity(1, 1)),
        Property(name="componentModel_System53", type=componentModel_Interface, multiplicity=Multiplicity(1, 9999))
    }
)
assemblycontext55: BinaryAssociation = BinaryAssociation(
    name="assemblycontext55",
    ends={
        Property(name="AssemblyContext", type=componentModel_RequiredRole, multiplicity=Multiplicity(1, 1)),
        Property(name="requiredrole", type=componentModel_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
interface56: BinaryAssociation = BinaryAssociation(
    name="interface56",
    ends={
        Property(name="componentModel_Interface58", type=componentModel_RequiredRole, multiplicity=Multiplicity(1, 1)),
        Property(name="componentModel_RequiredRole57", type=componentModel_Interface, multiplicity=Multiplicity(0, 1))
    }
)
assemblycontext59: BinaryAssociation = BinaryAssociation(
    name="assemblycontext59",
    ends={
        Property(name="AssemblyContext60", type=componentModel_ProvidedRole, multiplicity=Multiplicity(1, 1)),
        Property(name="providedrole", type=componentModel_AssemblyContext, multiplicity=Multiplicity(0, 1))
    }
)
interface61: BinaryAssociation = BinaryAssociation(
    name="interface61",
    ends={
        Property(name="componentModel_Interface63", type=componentModel_ProvidedRole, multiplicity=Multiplicity(1, 1)),
        Property(name="componentModel_ProvidedRole62", type=componentModel_Interface, multiplicity=Multiplicity(0, 1))
    }
)
providedInterface64: BinaryAssociation = BinaryAssociation(
    name="providedInterface64",
    ends={
        Property(name="componentModel_Interface65", type=componentModel_ProvidedDelegationConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="componentModel_ProvidedDelegationConnector", type=componentModel_Interface, multiplicity=Multiplicity(1, 1))
    }
)
encapsulated70: BinaryAssociation = BinaryAssociation(
    name="encapsulated70",
    ends={
        Property(name="componentModel_AssemblyContext71", type=componentModel_CompositeComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="componentModel_CompositeComponent", type=componentModel_AssemblyContext, multiplicity=Multiplicity(0, 9999))
    }
)
repositories72: BinaryAssociation = BinaryAssociation(
    name="repositories72",
    ends={
        Property(name="componentModel_Repository73", type=componentModel_RepositoryViewType, multiplicity=Multiplicity(1, 1)),
        Property(name="componentModel_RepositoryViewType", type=componentModel_Repository, multiplicity=Multiplicity(0, 9999))
    }
)
parameterTyp74: BinaryAssociation = BinaryAssociation(
    name="parameterTyp74",
    ends={
        Property(name="componentModel_ParameterTyp", type=componentModel_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="componentModel_Parameter75", type=componentModel_ParameterTyp, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_componentModel_SystemIndependentViewPoint_ViewPoint = Generalization(general=ViewPoint, specific=componentModel_SystemIndependentViewPoint)
gen_componentModel_Repository_ViewType = Generalization(general=ViewType, specific=componentModel_Repository)
gen_componentModel_Branch_Action = Generalization(general=Action, specific=componentModel_Branch)
gen_componentModel_Loop_Action = Generalization(general=Action, specific=componentModel_Loop)
gen_componentModel_ExternalCall_Action = Generalization(general=Action, specific=componentModel_ExternalCall)
gen_componentModel_InternalAction_Action = Generalization(general=Action, specific=componentModel_InternalAction)
gen_componentModel_AssemblyViewPoint_ViewPoint = Generalization(general=ViewPoint, specific=componentModel_AssemblyViewPoint)
gen_componentModel_AssemblyContext_AssemblyViewType = Generalization(general=AssemblyViewType, specific=componentModel_AssemblyContext)
gen_componentModel_CompositeComponent_Component = Generalization(general=Component, specific=componentModel_CompositeComponent)
gen_componentModel_RequiredDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=componentModel_RequiredDelegationConnector)
gen_componentModel_ProvidedDelegationConnector_DelegationConnector = Generalization(general=DelegationConnector, specific=componentModel_ProvidedDelegationConnector)
gen_componentModel_AssemblyViewType_ViewType = Generalization(general=ViewType, specific=componentModel_AssemblyViewType)
gen_componentModel_DeploymentViewPoint_ViewPoint = Generalization(general=ViewPoint, specific=componentModel_DeploymentViewPoint)
gen_componentModel_RepositoryViewType_ViewType = Generalization(general=ViewType, specific=componentModel_RepositoryViewType)
gen_componentModel_EnvironmentViewType_ViewType = Generalization(general=ViewType, specific=componentModel_EnvironmentViewType)
gen_componentModel_AllocationViewType_ViewType = Generalization(general=ViewType, specific=componentModel_AllocationViewType)
gen_componentModel_Parameter_SimpleParameterType = Generalization(general=SimpleParameterType, specific=componentModel_Parameter)
gen_componentModel_Boolean_SimpleParameterType = Generalization(general=SimpleParameterType, specific=componentModel_Boolean)
gen_componentModel_Void_Type = Generalization(general=Type, specific=componentModel_Void)
gen_componentModel_ParameterTyp_Type = Generalization(general=Type, specific=componentModel_ParameterTyp)
gen_componentModel_Char_SimpleParameterType = Generalization(general=SimpleParameterType, specific=componentModel_Char)
gen_componentModel_Date_SimpleParameterType = Generalization(general=SimpleParameterType, specific=componentModel_Date)
gen_componentModel_Float_SimpleParameterType = Generalization(general=SimpleParameterType, specific=componentModel_Float)
gen_componentModel_List_SimpleParameterType = Generalization(general=SimpleParameterType, specific=componentModel_List)
gen_componentModel_Int_SimpleParameterType = Generalization(general=SimpleParameterType, specific=componentModel_Int)
gen_componentModel_Long_SimpleParameterType = Generalization(general=SimpleParameterType, specific=componentModel_Long)
gen_componentModel_Map_SimpleParameterType = Generalization(general=SimpleParameterType, specific=componentModel_Map)
gen_componentModel_String_SimpleParameterType = Generalization(general=SimpleParameterType, specific=componentModel_String)
gen_componentModel_Double_SimpleParameterType = Generalization(general=SimpleParameterType, specific=componentModel_Double)
gen_componentModel_ComplexParameterType_ParameterTyp = Generalization(general=ParameterTyp, specific=componentModel_ComplexParameterType)
gen_componentModel_SimpleParameterType_ParameterTyp = Generalization(general=ParameterTyp, specific=componentModel_SimpleParameterType)

# Domain Model
domain_model = DomainModel(
    name="componentModel",
    types={componentModel_Interface, componentModel_ServiceEffectSpecification, componentModel_InterfaceServiceMapTuple, componentModel_SystemIndependentViewPoint, ViewPoint, componentModel_Repository, ViewType, componentModel_Component, componentModel_RequiredRole, componentModel_AssemblyConnector, componentModel_DelegationConnector, componentModel_Service, componentModel_Action, componentModel_Branch, Action, componentModel_Loop, componentModel_ExternalCall, componentModel_InternalAction, componentModel_Signature, componentModel_ViewType, componentModel_AssemblyViewPoint, componentModel_AssemblyContext, AssemblyViewType, componentModel_ProvidedRole, componentModel_ViewPoint, componentModel_CompositeComponent, Component, componentModel_RequiredDelegationConnector, DelegationConnector, componentModel_Parameter, componentModel_Type, componentModel_System, componentModel_ProvidedDelegationConnector, componentModel_AssemblyViewType, componentModel_DeploymentViewPoint, componentModel_RepositoryViewType, componentModel_EnvironmentViewType, componentModel_AllocationViewType, SimpleParameterType, componentModel_ParameterTyp, componentModel_Boolean, componentModel_Void, Type, componentModel_Char, componentModel_Date, componentModel_Float, componentModel_List, componentModel_Int, componentModel_Long, componentModel_Map, componentModel_String, componentModel_Double, componentModel_ComplexParameterType, ParameterTyp, componentModel_SimpleParameterType},
    associations={interface1, serviceeffectspecification3, component0, requiredrole27, ownerComponent29, providedrole31, interfaceServiceMap5, assemblyConnectors7, delegationConnectors9, providedInterface11, service14, actions16, actions18, actions20, requiredService22, signatures24, providedrole26, providedrole66, viewTypes69, requiredrole33, requiredrole35, requiredInterface37, parameters40, returnType42, required44, correspondence47, assemblycontext50, interface52, assemblycontext55, interface56, assemblycontext59, interface61, providedInterface64, encapsulated70, repositories72, parameterTyp74},
    generalizations={gen_componentModel_SystemIndependentViewPoint_ViewPoint, gen_componentModel_Repository_ViewType, gen_componentModel_Branch_Action, gen_componentModel_Loop_Action, gen_componentModel_ExternalCall_Action, gen_componentModel_InternalAction_Action, gen_componentModel_AssemblyViewPoint_ViewPoint, gen_componentModel_AssemblyContext_AssemblyViewType, gen_componentModel_CompositeComponent_Component, gen_componentModel_RequiredDelegationConnector_DelegationConnector, gen_componentModel_ProvidedDelegationConnector_DelegationConnector, gen_componentModel_AssemblyViewType_ViewType, gen_componentModel_DeploymentViewPoint_ViewPoint, gen_componentModel_RepositoryViewType_ViewType, gen_componentModel_EnvironmentViewType_ViewType, gen_componentModel_AllocationViewType_ViewType, gen_componentModel_Parameter_SimpleParameterType, gen_componentModel_Boolean_SimpleParameterType, gen_componentModel_Void_Type, gen_componentModel_ParameterTyp_Type, gen_componentModel_Char_SimpleParameterType, gen_componentModel_Date_SimpleParameterType, gen_componentModel_Float_SimpleParameterType, gen_componentModel_List_SimpleParameterType, gen_componentModel_Int_SimpleParameterType, gen_componentModel_Long_SimpleParameterType, gen_componentModel_Map_SimpleParameterType, gen_componentModel_String_SimpleParameterType, gen_componentModel_Double_SimpleParameterType, gen_componentModel_ComplexParameterType_ParameterTyp, gen_componentModel_SimpleParameterType_ParameterTyp},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)