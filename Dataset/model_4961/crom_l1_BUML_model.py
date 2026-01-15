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
crom_l1_Attribute = Class(name="crom::l1::Attribute")
RelationTarget = Class(name="RelationTarget")
crom_l1_NaturalType = Class(name="crom::l1::NaturalType")
RigidType = Class(name="RigidType")
Player = Class(name="Player")
crom_l1_RoleType = Class(name="crom::l1::RoleType")
AbstractRole = Class(name="AbstractRole")
crom_l1_NamedElement = Class(name="crom::l1::NamedElement", is_abstract=True)
crom_l1_ModelElement = Class(name="crom::l1::ModelElement", is_abstract=True)
NamedElement = Class(name="NamedElement")
crom_l1_Relation = Class(name="crom::l1::Relation", is_abstract=True)
crom_l1_Model = Class(name="crom::l1::Model")
crom_l1_RigidType = Class(name="crom::l1::RigidType")
Type = Class(name="Type")
ModelElement = Class(name="ModelElement")
crom_l1_Group = Class(name="crom::l1::Group")
Model = Class(name="Model")
crom_l1_Parameter = Class(name="crom::l1::Parameter")
TypedElement = Class(name="TypedElement")
crom_l1_Operation = Class(name="crom::l1::Operation")
crom_l1_Type = Class(name="crom::l1::Type")
crom_l1_Fulfillment = Class(name="crom::l1::Fulfillment")
Relation = Class(name="Relation")
crom_l1_AbstractRole = Class(name="crom::l1::AbstractRole", is_abstract=True)
crom_l1_Player = Class(name="crom::l1::Player", is_abstract=True)
crom_l1_Inheritance = Class(name="crom::l1::Inheritance")
crom_l1_NaturalInheritance = Class(name="crom::l1::NaturalInheritance")
Inheritance = Class(name="Inheritance")
crom_l1_RelationTarget = Class(name="crom::l1::RelationTarget", is_abstract=True)
crom_l1_TypedElement = Class(name="crom::l1::TypedElement", is_abstract=True)
crom_l1_Part = Class(name="crom::l1::Part")
crom_l1_CompartmentType = Class(name="crom::l1::CompartmentType")

# crom_l1_Attribute class attributes and methods

# RelationTarget class attributes and methods

# crom_l1_NaturalType class attributes and methods

# RigidType class attributes and methods

# Player class attributes and methods

# crom_l1_RoleType class attributes and methods

# AbstractRole class attributes and methods

# crom_l1_NamedElement class attributes and methods
crom_l1_NamedElement_name: Property = Property(name="name", type=StringType)
crom_l1_NamedElement.attributes={crom_l1_NamedElement_name}

# crom_l1_ModelElement class attributes and methods

# NamedElement class attributes and methods

# crom_l1_Relation class attributes and methods

# crom_l1_Model class attributes and methods

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

# crom_l1_Fulfillment class attributes and methods

# Relation class attributes and methods

# crom_l1_AbstractRole class attributes and methods

# crom_l1_Player class attributes and methods

# crom_l1_Inheritance class attributes and methods

# crom_l1_NaturalInheritance class attributes and methods

# Inheritance class attributes and methods

# crom_l1_RelationTarget class attributes and methods

# crom_l1_TypedElement class attributes and methods

# crom_l1_Part class attributes and methods

# crom_l1_CompartmentType class attributes and methods

# Relationships
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
relations0: BinaryAssociation = BinaryAssociation(
    name="relations0",
    ends={
        Property(name="crom_l1_Relation", type=crom_l1_ModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="crom_l1_ModelElement", type=crom_l1_Relation, multiplicity=Multiplicity(0, 9999))
    }
)
elements1: BinaryAssociation = BinaryAssociation(
    name="elements1",
    ends={
        Property(name="crom_l1_ModelElement2", type=crom_l1_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="crom_l1_Model", type=crom_l1_ModelElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
contains28: BinaryAssociation = BinaryAssociation(
    name="contains28",
    ends={
        Property(name="crom_l1_CompartmentType", type=crom_l1_CompartmentType, multiplicity=Multiplicity(1, 1)),
        Property(name="crom_l1_CompartmentType27", type=crom_l1_CompartmentType, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
fulfillments29: BinaryAssociation = BinaryAssociation(
    name="fulfillments29",
    ends={
        Property(name="crom_l1_Fulfillment31", type=crom_l1_CompartmentType, multiplicity=Multiplicity(1, 1)),
        Property(name="crom_l1_CompartmentType30", type=crom_l1_Fulfillment, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
roles23: BinaryAssociation = BinaryAssociation(
    name="roles23",
    ends={
        Property(name="crom_l1_AbstractRole24", type=crom_l1_Part, multiplicity=Multiplicity(1, 1)),
        Property(name="crom_l1_Part", type=crom_l1_AbstractRole, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
whole25: BinaryAssociation = BinaryAssociation(
    name="whole25",
    ends={
        Property(name="CompartmentType", type=crom_l1_Part, multiplicity=Multiplicity(1, 1)),
        Property(name="parts", type=crom_l1_CompartmentType, multiplicity=Multiplicity(1, 1))
    }
)
parts26: BinaryAssociation = BinaryAssociation(
    name="parts26",
    ends={
        Property(name="Part", type=crom_l1_CompartmentType, multiplicity=Multiplicity(1, 1)),
        Property(name="whole", type=crom_l1_Part, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_crom_l1_Attribute_TypedElement = Generalization(general=TypedElement, specific=crom_l1_Attribute)
gen_crom_l1_Type_RelationTarget = Generalization(general=RelationTarget, specific=crom_l1_Type)
gen_crom_l1_NaturalType_RigidType = Generalization(general=RigidType, specific=crom_l1_NaturalType)
gen_crom_l1_NaturalType_Player = Generalization(general=Player, specific=crom_l1_NaturalType)
gen_crom_l1_RoleType_AbstractRole = Generalization(general=AbstractRole, specific=crom_l1_RoleType)
gen_crom_l1_RoleType_RelationTarget = Generalization(general=RelationTarget, specific=crom_l1_RoleType)
gen_crom_l1_RoleType_Player = Generalization(general=Player, specific=crom_l1_RoleType)
gen_crom_l1_ModelElement_NamedElement = Generalization(general=NamedElement, specific=crom_l1_ModelElement)
gen_crom_l1_RigidType_Type = Generalization(general=Type, specific=crom_l1_RigidType)
gen_crom_l1_RigidType_ModelElement = Generalization(general=ModelElement, specific=crom_l1_RigidType)
gen_crom_l1_Group_ModelElement = Generalization(general=ModelElement, specific=crom_l1_Group)
gen_crom_l1_Group_Model = Generalization(general=Model, specific=crom_l1_Group)
gen_crom_l1_Parameter_TypedElement = Generalization(general=TypedElement, specific=crom_l1_Parameter)
gen_crom_l1_Operation_TypedElement = Generalization(general=TypedElement, specific=crom_l1_Operation)
gen_crom_l1_Fulfillment_Relation = Generalization(general=Relation, specific=crom_l1_Fulfillment)
gen_crom_l1_Inheritance_Relation = Generalization(general=Relation, specific=crom_l1_Inheritance)
gen_crom_l1_NaturalInheritance_Inheritance = Generalization(general=Inheritance, specific=crom_l1_NaturalInheritance)
gen_crom_l1_RelationTarget_NamedElement = Generalization(general=NamedElement, specific=crom_l1_RelationTarget)
gen_crom_l1_TypedElement_NamedElement = Generalization(general=NamedElement, specific=crom_l1_TypedElement)
gen_crom_l1_CompartmentType_RelationTarget = Generalization(general=RelationTarget, specific=crom_l1_CompartmentType)
gen_crom_l1_CompartmentType_ModelElement = Generalization(general=ModelElement, specific=crom_l1_CompartmentType)
gen_crom_l1_CompartmentType_Player = Generalization(general=Player, specific=crom_l1_CompartmentType)

# Domain Model
domain_model = DomainModel(
    name="crom_l1",
    types={crom_l1_Attribute, RelationTarget, crom_l1_NaturalType, RigidType, Player, crom_l1_RoleType, AbstractRole, crom_l1_NamedElement, crom_l1_ModelElement, NamedElement, crom_l1_Relation, crom_l1_Model, crom_l1_RigidType, Type, ModelElement, crom_l1_Group, Model, crom_l1_Parameter, TypedElement, crom_l1_Operation, crom_l1_Type, crom_l1_Fulfillment, Relation, crom_l1_AbstractRole, crom_l1_Player, crom_l1_Inheritance, crom_l1_NaturalInheritance, Inheritance, crom_l1_RelationTarget, crom_l1_TypedElement, crom_l1_Part, crom_l1_CompartmentType},
    associations={owner5, attributes7, operations8, relations0, elements1, params3, owner4, contains28, fulfillments29, filled10, filler11, super13, sub14, incoming17, outgoing19, type22, roles23, whole25, parts26},
    generalizations={gen_crom_l1_Attribute_TypedElement, gen_crom_l1_Type_RelationTarget, gen_crom_l1_NaturalType_RigidType, gen_crom_l1_NaturalType_Player, gen_crom_l1_RoleType_AbstractRole, gen_crom_l1_RoleType_RelationTarget, gen_crom_l1_RoleType_Player, gen_crom_l1_ModelElement_NamedElement, gen_crom_l1_RigidType_Type, gen_crom_l1_RigidType_ModelElement, gen_crom_l1_Group_ModelElement, gen_crom_l1_Group_Model, gen_crom_l1_Parameter_TypedElement, gen_crom_l1_Operation_TypedElement, gen_crom_l1_Fulfillment_Relation, gen_crom_l1_Inheritance_Relation, gen_crom_l1_NaturalInheritance_Inheritance, gen_crom_l1_RelationTarget_NamedElement, gen_crom_l1_TypedElement_NamedElement, gen_crom_l1_CompartmentType_RelationTarget, gen_crom_l1_CompartmentType_ModelElement, gen_crom_l1_CompartmentType_Player},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)