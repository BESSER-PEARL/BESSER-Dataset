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
NamedElement = Class(name="NamedElement")
crom_l1_Model = Class(name="crom::l1::Model")
crom_l1_Relation = Class(name="crom::l1::Relation", is_abstract=True)
crom_l1_RigidType = Class(name="crom::l1::RigidType")
Type = Class(name="Type")
ModelElement = Class(name="ModelElement")
crom_l1_Group = Class(name="crom::l1::Group")
Model = Class(name="Model")
crom_l1_Parameter = Class(name="crom::l1::Parameter")
TypedElement = Class(name="TypedElement")
crom_l1_Operation = Class(name="crom::l1::Operation")
crom_l1_Type = Class(name="crom::l1::Type")
crom_l1_Attribute = Class(name="crom::l1::Attribute")
RelationTarget = Class(name="RelationTarget")
crom_l1_NaturalType = Class(name="crom::l1::NaturalType")
crom_l1_NamedElement = Class(name="crom::l1::NamedElement", is_abstract=True)
crom_l1_ModelElement = Class(name="crom::l1::ModelElement", is_abstract=True)
crom_l1_NaturalInheritance = Class(name="crom::l1::NaturalInheritance")
Inheritance = Class(name="Inheritance")
crom_l1_RelationTarget = Class(name="crom::l1::RelationTarget", is_abstract=True)
RoleGroupElement = Class(name="RoleGroupElement")
crom_l1_TypedElement = Class(name="crom::l1::TypedElement", is_abstract=True)
crom_l1_DataType = Class(name="crom::l1::DataType")
RigidType = Class(name="RigidType")
Player = Class(name="Player")
crom_l1_RoleType = Class(name="crom::l1::RoleType")
AbstractRole = Class(name="AbstractRole")
AntiRigidType = Class(name="AntiRigidType")
crom_l1_Fulfillment = Class(name="crom::l1::Fulfillment")
Relation = Class(name="Relation")
crom_l1_AbstractRole = Class(name="crom::l1::AbstractRole", is_abstract=True)
crom_l1_Player = Class(name="crom::l1::Player", is_abstract=True)
crom_l1_Inheritance = Class(name="crom::l1::Inheritance")
crom_l1_AbstractRoleRef = Class(name="crom::l1::AbstractRoleRef")
crom_l1_AntiRigidType = Class(name="crom::l1::AntiRigidType")
crom_l1_Part = Class(name="crom::l1::Part")
crom_l1_CompartmentType = Class(name="crom::l1::CompartmentType")
crom_l1_RoleConstraint = Class(name="crom::l1::RoleConstraint")
Constraint = Class(name="Constraint")
crom_l1_Test = Class(name="crom::l1::Test")
crom_l1_Constraint = Class(name="crom::l1::Constraint")
crom_l1_RoleGroup = Class(name="crom::l1::RoleGroup")
crom_l1_RoleGroupElement = Class(name="crom::l1::RoleGroupElement", is_abstract=True)
crom_l1_RoleImplication = Class(name="crom::l1::RoleImplication")
RoleConstraint = Class(name="RoleConstraint")
crom_l1_CompartmentInheritance = Class(name="crom::l1::CompartmentInheritance")
crom_l1_RoleEquivalence = Class(name="crom::l1::RoleEquivalence")
crom_l1_RoleProhibition = Class(name="crom::l1::RoleProhibition")
crom_l1_DataInheritance = Class(name="crom::l1::DataInheritance")

# NamedElement class attributes and methods

# crom_l1_Model class attributes and methods

# crom_l1_Relation class attributes and methods

# crom_l1_RigidType class attributes and methods

# Type class attributes and methods

# ModelElement class attributes and methods

# crom_l1_Group class attributes and methods

# Model class attributes and methods

# crom_l1_Parameter class attributes and methods

# TypedElement class attributes and methods

# crom_l1_Operation class attributes and methods
crom_l1_Operation_operation: Property = Property(name="operation", type=StringType)
crom_l1_Operation.attributes={crom_l1_Operation_operation}

# crom_l1_Type class attributes and methods

# crom_l1_Attribute class attributes and methods

# RelationTarget class attributes and methods

# crom_l1_NaturalType class attributes and methods

# crom_l1_NamedElement class attributes and methods
crom_l1_NamedElement_name: Property = Property(name="name", type=StringType)
crom_l1_NamedElement.attributes={crom_l1_NamedElement_name}

# crom_l1_ModelElement class attributes and methods

# crom_l1_NaturalInheritance class attributes and methods

# Inheritance class attributes and methods

# crom_l1_RelationTarget class attributes and methods

# RoleGroupElement class attributes and methods

# crom_l1_TypedElement class attributes and methods

# crom_l1_DataType class attributes and methods

# RigidType class attributes and methods

# Player class attributes and methods

# crom_l1_RoleType class attributes and methods

# AbstractRole class attributes and methods

# AntiRigidType class attributes and methods

# crom_l1_Fulfillment class attributes and methods

# Relation class attributes and methods

# crom_l1_AbstractRole class attributes and methods

# crom_l1_Player class attributes and methods

# crom_l1_Inheritance class attributes and methods

# crom_l1_AbstractRoleRef class attributes and methods

# crom_l1_AntiRigidType class attributes and methods

# crom_l1_Part class attributes and methods
crom_l1_Part_lower: Property = Property(name="lower", type=IntegerType)
crom_l1_Part_upper: Property = Property(name="upper", type=IntegerType)
crom_l1_Part.attributes={crom_l1_Part_lower, crom_l1_Part_upper}

# crom_l1_CompartmentType class attributes and methods

# crom_l1_RoleConstraint class attributes and methods

# Constraint class attributes and methods

# crom_l1_Test class attributes and methods

# crom_l1_Constraint class attributes and methods

# crom_l1_RoleGroup class attributes and methods
crom_l1_RoleGroup_lower: Property = Property(name="lower", type=IntegerType)
crom_l1_RoleGroup_upper: Property = Property(name="upper", type=IntegerType)
crom_l1_RoleGroup.attributes={crom_l1_RoleGroup_upper, crom_l1_RoleGroup_lower}

# crom_l1_RoleGroupElement class attributes and methods

# crom_l1_RoleImplication class attributes and methods

# RoleConstraint class attributes and methods

# crom_l1_CompartmentInheritance class attributes and methods

# crom_l1_RoleEquivalence class attributes and methods

# crom_l1_RoleProhibition class attributes and methods

# crom_l1_DataInheritance class attributes and methods

# Relationships
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="crom_l1_ModelElement", type=crom_l1_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="crom_l1_Model", type=crom_l1_ModelElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relations1: BinaryAssociation = BinaryAssociation(
    name="relations1",
    ends={
        Property(name="crom_l1_Relation", type=crom_l1_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="crom_l1_Model2", type=crom_l1_Relation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
params3: BinaryAssociation = BinaryAssociation(
    name="params3",
    ends={
        Property(name="crom_l1_Parameter", type=crom_l1_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="crom_l1_Operation", type=crom_l1_Parameter, multiplicity=Multiplicity(0, 9999))
    }
)
owner4: BinaryAssociation = BinaryAssociation(
    name="owner4",
    ends={
        Property(name="Type", type=crom_l1_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="operations", type=crom_l1_Type, multiplicity=Multiplicity(1, 1))
    }
)
owner5: BinaryAssociation = BinaryAssociation(
    name="owner5",
    ends={
        Property(name="Type6", type=crom_l1_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="attributes", type=crom_l1_Type, multiplicity=Multiplicity(1, 1))
    }
)
attributes7: BinaryAssociation = BinaryAssociation(
    name="attributes7",
    ends={
        Property(name="Attribute", type=crom_l1_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=crom_l1_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operations8: BinaryAssociation = BinaryAssociation(
    name="operations8",
    ends={
        Property(name="Operation", type=crom_l1_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="owner9", type=crom_l1_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
super13: BinaryAssociation = BinaryAssociation(
    name="super13",
    ends={
        Property(name="crom_l1_NaturalType", type=crom_l1_NaturalInheritance, multiplicity=Multiplicity(1, 1)),
        Property(name="crom_l1_NaturalInheritance", type=crom_l1_NaturalType, multiplicity=Multiplicity(1, 1))
    }
)
sub14: BinaryAssociation = BinaryAssociation(
    name="sub14",
    ends={
        Property(name="crom_l1_NaturalType16", type=crom_l1_NaturalInheritance, multiplicity=Multiplicity(1, 1)),
        Property(name="crom_l1_NaturalInheritance15", type=crom_l1_NaturalType, multiplicity=Multiplicity(1, 1))
    }
)
incoming17: BinaryAssociation = BinaryAssociation(
    name="incoming17",
    ends={
        Property(name="crom_l1_Relation18", type=crom_l1_RelationTarget, multiplicity=Multiplicity(1, 1)),
        Property(name="crom_l1_RelationTarget", type=crom_l1_Relation, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing19: BinaryAssociation = BinaryAssociation(
    name="outgoing19",
    ends={
        Property(name="crom_l1_Relation21", type=crom_l1_RelationTarget, multiplicity=Multiplicity(1, 1)),
        Property(name="crom_l1_RelationTarget20", type=crom_l1_Relation, multiplicity=Multiplicity(0, 9999))
    }
)
type22: BinaryAssociation = BinaryAssociation(
    name="type22",
    ends={
        Property(name="crom_l1_Type", type=crom_l1_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="crom_l1_TypedElement", type=crom_l1_Type, multiplicity=Multiplicity(1, 1))
    }
)
filled10: BinaryAssociation = BinaryAssociation(
    name="filled10",
    ends={
        Property(name="crom_l1_AbstractRole", type=crom_l1_Fulfillment, multiplicity=Multiplicity(1, 1)),
        Property(name="crom_l1_Fulfillment", type=crom_l1_AbstractRole, multiplicity=Multiplicity(1, 1))
    }
)
filler11: BinaryAssociation = BinaryAssociation(
    name="filler11",
    ends={
        Property(name="crom_l1_Player", type=crom_l1_Fulfillment, multiplicity=Multiplicity(1, 1)),
        Property(name="crom_l1_Fulfillment12", type=crom_l1_Player, multiplicity=Multiplicity(1, 1))
    }
)
elements23: BinaryAssociation = BinaryAssociation(
    name="elements23",
    ends={
        Property(name="crom_l1_RoleGroupElement", type=crom_l1_RoleGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="crom_l1_RoleGroup", type=crom_l1_RoleGroupElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ref24: BinaryAssociation = BinaryAssociation(
    name="ref24",
    ends={
        Property(name="crom_l1_AbstractRole25", type=crom_l1_AbstractRoleRef, multiplicity=Multiplicity(1, 1)),
        Property(name="crom_l1_AbstractRoleRef", type=crom_l1_AbstractRole, multiplicity=Multiplicity(1, 1))
    }
)
roles26: BinaryAssociation = BinaryAssociation(
    name="roles26",
    ends={
        Property(name="crom_l1_AbstractRole27", type=crom_l1_Part, multiplicity=Multiplicity(1, 1)),
        Property(name="crom_l1_Part", type=crom_l1_AbstractRole, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
whole28: BinaryAssociation = BinaryAssociation(
    name="whole28",
    ends={
        Property(name="CompartmentType", type=crom_l1_Part, multiplicity=Multiplicity(1, 1)),
        Property(name="parts", type=crom_l1_CompartmentType, multiplicity=Multiplicity(1, 1))
    }
)
parts29: BinaryAssociation = BinaryAssociation(
    name="parts29",
    ends={
        Property(name="Part", type=crom_l1_CompartmentType, multiplicity=Multiplicity(1, 1)),
        Property(name="whole", type=crom_l1_Part, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
super34: BinaryAssociation = BinaryAssociation(
    name="super34",
    ends={
        Property(name="crom_l1_DataType", type=crom_l1_DataInheritance, multiplicity=Multiplicity(1, 1)),
        Property(name="crom_l1_DataInheritance", type=crom_l1_DataType, multiplicity=Multiplicity(1, 1))
    }
)
sub35: BinaryAssociation = BinaryAssociation(
    name="sub35",
    ends={
        Property(name="crom_l1_DataType37", type=crom_l1_DataInheritance, multiplicity=Multiplicity(1, 1)),
        Property(name="crom_l1_DataInheritance36", type=crom_l1_DataType, multiplicity=Multiplicity(1, 1))
    }
)
super38: BinaryAssociation = BinaryAssociation(
    name="super38",
    ends={
        Property(name="crom_l1_CompartmentType39", type=crom_l1_CompartmentInheritance, multiplicity=Multiplicity(1, 1)),
        Property(name="crom_l1_CompartmentInheritance", type=crom_l1_CompartmentType, multiplicity=Multiplicity(1, 1))
    }
)
sub40: BinaryAssociation = BinaryAssociation(
    name="sub40",
    ends={
        Property(name="crom_l1_CompartmentType42", type=crom_l1_CompartmentInheritance, multiplicity=Multiplicity(1, 1)),
        Property(name="crom_l1_CompartmentInheritance41", type=crom_l1_CompartmentType, multiplicity=Multiplicity(1, 1))
    }
)
constraints30: BinaryAssociation = BinaryAssociation(
    name="constraints30",
    ends={
        Property(name="crom_l1_Constraint", type=crom_l1_CompartmentType, multiplicity=Multiplicity(1, 1)),
        Property(name="crom_l1_CompartmentType", type=crom_l1_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contains32: BinaryAssociation = BinaryAssociation(
    name="contains32",
    ends={
        Property(name="crom_l1_CompartmentType33", type=crom_l1_CompartmentType, multiplicity=Multiplicity(1, 1)),
        Property(name="crom_l1_CompartmentType31", type=crom_l1_CompartmentType, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)

# Generalizations
gen_crom_l1_ModelElement_NamedElement = Generalization(general=NamedElement, specific=crom_l1_ModelElement)
gen_crom_l1_RigidType_Type = Generalization(general=Type, specific=crom_l1_RigidType)
gen_crom_l1_RigidType_ModelElement = Generalization(general=ModelElement, specific=crom_l1_RigidType)
gen_crom_l1_Group_ModelElement = Generalization(general=ModelElement, specific=crom_l1_Group)
gen_crom_l1_Group_Model = Generalization(general=Model, specific=crom_l1_Group)
gen_crom_l1_Parameter_TypedElement = Generalization(general=TypedElement, specific=crom_l1_Parameter)
gen_crom_l1_Operation_TypedElement = Generalization(general=TypedElement, specific=crom_l1_Operation)
gen_crom_l1_Attribute_TypedElement = Generalization(general=TypedElement, specific=crom_l1_Attribute)
gen_crom_l1_Type_RelationTarget = Generalization(general=RelationTarget, specific=crom_l1_Type)
gen_crom_l1_Inheritance_Relation = Generalization(general=Relation, specific=crom_l1_Inheritance)
gen_crom_l1_NaturalInheritance_Inheritance = Generalization(general=Inheritance, specific=crom_l1_NaturalInheritance)
gen_crom_l1_RelationTarget_NamedElement = Generalization(general=NamedElement, specific=crom_l1_RelationTarget)
gen_crom_l1_AbstractRole_RoleGroupElement = Generalization(general=RoleGroupElement, specific=crom_l1_AbstractRole)
gen_crom_l1_TypedElement_NamedElement = Generalization(general=NamedElement, specific=crom_l1_TypedElement)
gen_crom_l1_DataType_RigidType = Generalization(general=RigidType, specific=crom_l1_DataType)
gen_crom_l1_NaturalType_RigidType = Generalization(general=RigidType, specific=crom_l1_NaturalType)
gen_crom_l1_NaturalType_Player = Generalization(general=Player, specific=crom_l1_NaturalType)
gen_crom_l1_RoleType_AbstractRole = Generalization(general=AbstractRole, specific=crom_l1_RoleType)
gen_crom_l1_RoleType_RelationTarget = Generalization(general=RelationTarget, specific=crom_l1_RoleType)
gen_crom_l1_RoleType_AntiRigidType = Generalization(general=AntiRigidType, specific=crom_l1_RoleType)
gen_crom_l1_Fulfillment_Relation = Generalization(general=Relation, specific=crom_l1_Fulfillment)
gen_crom_l1_AbstractRoleRef_RoleGroupElement = Generalization(general=RoleGroupElement, specific=crom_l1_AbstractRoleRef)
gen_crom_l1_AntiRigidType_Type = Generalization(general=Type, specific=crom_l1_AntiRigidType)
gen_crom_l1_RoleConstraint_Constraint = Generalization(general=Constraint, specific=crom_l1_RoleConstraint)
gen_crom_l1_Test_Constraint = Generalization(general=Constraint, specific=crom_l1_Test)
gen_crom_l1_CompartmentType_Player = Generalization(general=Player, specific=crom_l1_CompartmentType)
gen_crom_l1_CompartmentType_RigidType = Generalization(general=RigidType, specific=crom_l1_CompartmentType)
gen_crom_l1_RoleGroup_AbstractRole = Generalization(general=AbstractRole, specific=crom_l1_RoleGroup)
gen_crom_l1_RoleGroup_RelationTarget = Generalization(general=RelationTarget, specific=crom_l1_RoleGroup)
gen_crom_l1_RoleImplication_RoleConstraint = Generalization(general=RoleConstraint, specific=crom_l1_RoleImplication)
gen_crom_l1_CompartmentInheritance_Inheritance = Generalization(general=Inheritance, specific=crom_l1_CompartmentInheritance)
gen_crom_l1_RoleEquivalence_RoleConstraint = Generalization(general=RoleConstraint, specific=crom_l1_RoleEquivalence)
gen_crom_l1_RoleProhibition_RoleConstraint = Generalization(general=RoleConstraint, specific=crom_l1_RoleProhibition)
gen_crom_l1_DataInheritance_Inheritance = Generalization(general=Inheritance, specific=crom_l1_DataInheritance)

# Domain Model
domain_model = DomainModel(
    name="crom_l1",
    types={NamedElement, crom_l1_Model, crom_l1_Relation, crom_l1_RigidType, Type, ModelElement, crom_l1_Group, Model, crom_l1_Parameter, TypedElement, crom_l1_Operation, crom_l1_Type, crom_l1_Attribute, RelationTarget, crom_l1_NaturalType, crom_l1_NamedElement, crom_l1_ModelElement, crom_l1_NaturalInheritance, Inheritance, crom_l1_RelationTarget, RoleGroupElement, crom_l1_TypedElement, crom_l1_DataType, RigidType, Player, crom_l1_RoleType, AbstractRole, AntiRigidType, crom_l1_Fulfillment, Relation, crom_l1_AbstractRole, crom_l1_Player, crom_l1_Inheritance, crom_l1_AbstractRoleRef, crom_l1_AntiRigidType, crom_l1_Part, crom_l1_CompartmentType, crom_l1_RoleConstraint, Constraint, crom_l1_Test, crom_l1_Constraint, crom_l1_RoleGroup, crom_l1_RoleGroupElement, crom_l1_RoleImplication, RoleConstraint, crom_l1_CompartmentInheritance, crom_l1_RoleEquivalence, crom_l1_RoleProhibition, crom_l1_DataInheritance},
    associations={elements0, relations1, params3, owner4, owner5, attributes7, operations8, super13, sub14, incoming17, outgoing19, type22, filled10, filler11, elements23, ref24, roles26, whole28, parts29, super34, sub35, super38, sub40, constraints30, contains32},
    generalizations={gen_crom_l1_ModelElement_NamedElement, gen_crom_l1_RigidType_Type, gen_crom_l1_RigidType_ModelElement, gen_crom_l1_Group_ModelElement, gen_crom_l1_Group_Model, gen_crom_l1_Parameter_TypedElement, gen_crom_l1_Operation_TypedElement, gen_crom_l1_Attribute_TypedElement, gen_crom_l1_Type_RelationTarget, gen_crom_l1_Inheritance_Relation, gen_crom_l1_NaturalInheritance_Inheritance, gen_crom_l1_RelationTarget_NamedElement, gen_crom_l1_AbstractRole_RoleGroupElement, gen_crom_l1_TypedElement_NamedElement, gen_crom_l1_DataType_RigidType, gen_crom_l1_NaturalType_RigidType, gen_crom_l1_NaturalType_Player, gen_crom_l1_RoleType_AbstractRole, gen_crom_l1_RoleType_RelationTarget, gen_crom_l1_RoleType_AntiRigidType, gen_crom_l1_Fulfillment_Relation, gen_crom_l1_AbstractRoleRef_RoleGroupElement, gen_crom_l1_AntiRigidType_Type, gen_crom_l1_RoleConstraint_Constraint, gen_crom_l1_Test_Constraint, gen_crom_l1_CompartmentType_Player, gen_crom_l1_CompartmentType_RigidType, gen_crom_l1_RoleGroup_AbstractRole, gen_crom_l1_RoleGroup_RelationTarget, gen_crom_l1_RoleImplication_RoleConstraint, gen_crom_l1_CompartmentInheritance_Inheritance, gen_crom_l1_RoleEquivalence_RoleConstraint, gen_crom_l1_RoleProhibition_RoleConstraint, gen_crom_l1_DataInheritance_Inheritance},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)