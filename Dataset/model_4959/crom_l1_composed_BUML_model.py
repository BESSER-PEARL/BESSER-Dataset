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
Direction: Enumeration = Enumeration(
    name="Direction",
    literals={
            EnumerationLiteral(name="Undirected"),
			EnumerationLiteral(name="FirstToSecond"),
			EnumerationLiteral(name="SecondToFirst")
    }
)

Parthood: Enumeration = Enumeration(
    name="Parthood",
    literals={
            EnumerationLiteral(name="Unconstrained"),
			EnumerationLiteral(name="ExclusivePart"),
			EnumerationLiteral(name="SharablePart"),
			EnumerationLiteral(name="EssentialPart"),
			EnumerationLiteral(name="MandatoryPart"),
			EnumerationLiteral(name="InseparablePart")
    }
)

# Classes
crom_l1_composed_NamedElement = Class(name="crom::l1::composed::NamedElement", is_abstract=True)
crom_l1_composed_NaturalType = Class(name="crom::l1::composed::NaturalType")
crom_l1_composed_CompartmentType = Class(name="crom::l1::composed::CompartmentType")
crom_l1_composed_Part = Class(name="crom::l1::composed::Part")
crom_l1_composed_ModelElement = Class(name="crom::l1::composed::ModelElement", is_abstract=True)
NamedElement = Class(name="NamedElement")
crom_l1_composed_Model = Class(name="crom::l1::composed::Model")
crom_l1_composed_Relation = Class(name="crom::l1::composed::Relation", is_abstract=True)
crom_l1_composed_RigidType = Class(name="crom::l1::composed::RigidType")
Type = Class(name="Type")
ModelElement = Class(name="ModelElement")
crom_l1_composed_Group = Class(name="crom::l1::composed::Group")
Model = Class(name="Model")
crom_l1_composed_Parameter = Class(name="crom::l1::composed::Parameter")
TypedElement = Class(name="TypedElement")
crom_l1_composed_Operation = Class(name="crom::l1::composed::Operation")
crom_l1_composed_Type = Class(name="crom::l1::composed::Type")
crom_l1_composed_Attribute = Class(name="crom::l1::composed::Attribute")
RelationTarget = Class(name="RelationTarget")
crom_l1_composed_DataType = Class(name="crom::l1::composed::DataType")
RigidType = Class(name="RigidType")
crom_l1_composed_RelationshipConstraint = Class(name="crom::l1::composed::RelationshipConstraint")
crom_l1_composed_Relationship = Class(name="crom::l1::composed::Relationship")
crom_l1_composed_Constraint = Class(name="crom::l1::composed::Constraint")
crom_l1_composed_AntiRigidType = Class(name="crom::l1::composed::AntiRigidType")
crom_l1_composed_RoleType = Class(name="crom::l1::composed::RoleType")
AntiRigidType = Class(name="AntiRigidType")
AbstractRole = Class(name="AbstractRole")
Relation = Class(name="Relation")
crom_l1_composed_Place = Class(name="crom::l1::composed::Place")
crom_l1_composed_IntraRelationshipConstraint = Class(name="crom::l1::composed::IntraRelationshipConstraint")
crom_l1_composed_Fulfillment = Class(name="crom::l1::composed::Fulfillment")
crom_l1_composed_AbstractRole = Class(name="crom::l1::composed::AbstractRole", is_abstract=True)
crom_l1_composed_Inheritance = Class(name="crom::l1::composed::Inheritance")
crom_l1_composed_RoleConstraint = Class(name="crom::l1::composed::RoleConstraint")
Constraint = Class(name="Constraint")
RelationshipConstraint = Class(name="RelationshipConstraint")
crom_l1_composed_InterRelationshipConstraint = Class(name="crom::l1::composed::InterRelationshipConstraint")
crom_l1_composed_ComplexConstraint = Class(name="crom::l1::composed::ComplexConstraint")
crom_l1_composed_DataInheritance = Class(name="crom::l1::composed::DataInheritance")
Inheritance = Class(name="Inheritance")
crom_l1_composed_NaturalInheritance = Class(name="crom::l1::composed::NaturalInheritance")
crom_l1_composed_CompartmentInheritance = Class(name="crom::l1::composed::CompartmentInheritance")
RoleConstraint = Class(name="RoleConstraint")
crom_l1_composed_RoleEquivalence = Class(name="crom::l1::composed::RoleEquivalence")
crom_l1_composed_RoleProhibition = Class(name="crom::l1::composed::RoleProhibition")
crom_l1_composed_RoleInheritance = Class(name="crom::l1::composed::RoleInheritance")
crom_l1_composed_RelationshipImplication = Class(name="crom::l1::composed::RelationshipImplication")
InterRelationshipConstraint = Class(name="InterRelationshipConstraint")
crom_l1_composed_RelationTarget = Class(name="crom::l1::composed::RelationTarget", is_abstract=True)
crom_l1_composed_Irreflexive = Class(name="crom::l1::composed::Irreflexive")
IntraRelationshipConstraint = Class(name="IntraRelationshipConstraint")
crom_l1_composed_Cyclic = Class(name="crom::l1::composed::Cyclic")
crom_l1_composed_Total = Class(name="crom::l1::composed::Total")
RoleGroupElement = Class(name="RoleGroupElement")
crom_l1_composed_RoleGroup = Class(name="crom::l1::composed::RoleGroup")
crom_l1_composed_RoleGroupElement = Class(name="crom::l1::composed::RoleGroupElement", is_abstract=True)
crom_l1_composed_RoleImplication = Class(name="crom::l1::composed::RoleImplication")
crom_l1_composed_TypedElement = Class(name="crom::l1::composed::TypedElement", is_abstract=True)
crom_l1_composed_ParthoodConstraint = Class(name="crom::l1::composed::ParthoodConstraint")
crom_l1_composed_AbstractRoleRef = Class(name="crom::l1::composed::AbstractRoleRef")

# crom_l1_composed_NamedElement class attributes and methods
crom_l1_composed_NamedElement_name: Property = Property(name="name", type=StringType)
crom_l1_composed_NamedElement.attributes={crom_l1_composed_NamedElement_name}

# crom_l1_composed_NaturalType class attributes and methods

# crom_l1_composed_CompartmentType class attributes and methods

# crom_l1_composed_Part class attributes and methods
crom_l1_composed_Part_lower: Property = Property(name="lower", type=IntegerType)
crom_l1_composed_Part_upper: Property = Property(name="upper", type=IntegerType)
crom_l1_composed_Part.attributes={crom_l1_composed_Part_lower, crom_l1_composed_Part_upper}

# crom_l1_composed_ModelElement class attributes and methods

# NamedElement class attributes and methods

# crom_l1_composed_Model class attributes and methods

# crom_l1_composed_Relation class attributes and methods
crom_l1_composed_Relation_m_getSource: Method = Method(name="getSource", parameters={}, type=StringType)
crom_l1_composed_Relation_m_getTarget: Method = Method(name="getTarget", parameters={}, type=StringType)
crom_l1_composed_Relation.methods={crom_l1_composed_Relation_m_getTarget, crom_l1_composed_Relation_m_getSource}

# crom_l1_composed_RigidType class attributes and methods

# Type class attributes and methods

# ModelElement class attributes and methods

# crom_l1_composed_Group class attributes and methods

# Model class attributes and methods

# crom_l1_composed_Parameter class attributes and methods

# TypedElement class attributes and methods

# crom_l1_composed_Operation class attributes and methods
crom_l1_composed_Operation_operation: Property = Property(name="operation", type=StringType)
crom_l1_composed_Operation.attributes={crom_l1_composed_Operation_operation}

# crom_l1_composed_Type class attributes and methods

# crom_l1_composed_Attribute class attributes and methods

# RelationTarget class attributes and methods

# crom_l1_composed_DataType class attributes and methods
crom_l1_composed_DataType_serializable: Property = Property(name="serializable", type=BooleanType)
crom_l1_composed_DataType.attributes={crom_l1_composed_DataType_serializable}

# RigidType class attributes and methods

# crom_l1_composed_RelationshipConstraint class attributes and methods

# crom_l1_composed_Relationship class attributes and methods
crom_l1_composed_Relationship_direction: Property = Property(name="direction", type=StringType)
crom_l1_composed_Relationship.attributes={crom_l1_composed_Relationship_direction}

# crom_l1_composed_Constraint class attributes and methods

# crom_l1_composed_AntiRigidType class attributes and methods

# crom_l1_composed_RoleType class attributes and methods

# AntiRigidType class attributes and methods

# AbstractRole class attributes and methods

# Relation class attributes and methods

# crom_l1_composed_Place class attributes and methods
crom_l1_composed_Place_lower: Property = Property(name="lower", type=IntegerType)
crom_l1_composed_Place_upper: Property = Property(name="upper", type=IntegerType)
crom_l1_composed_Place.attributes={crom_l1_composed_Place_lower, crom_l1_composed_Place_upper}

# crom_l1_composed_IntraRelationshipConstraint class attributes and methods

# crom_l1_composed_Fulfillment class attributes and methods

# crom_l1_composed_AbstractRole class attributes and methods

# crom_l1_composed_Inheritance class attributes and methods

# crom_l1_composed_RoleConstraint class attributes and methods

# Constraint class attributes and methods

# RelationshipConstraint class attributes and methods

# crom_l1_composed_InterRelationshipConstraint class attributes and methods

# crom_l1_composed_ComplexConstraint class attributes and methods
crom_l1_composed_ComplexConstraint_expression: Property = Property(name="expression", type=StringType)
crom_l1_composed_ComplexConstraint.attributes={crom_l1_composed_ComplexConstraint_expression}

# crom_l1_composed_DataInheritance class attributes and methods

# Inheritance class attributes and methods

# crom_l1_composed_NaturalInheritance class attributes and methods

# crom_l1_composed_CompartmentInheritance class attributes and methods

# RoleConstraint class attributes and methods

# crom_l1_composed_RoleEquivalence class attributes and methods

# crom_l1_composed_RoleProhibition class attributes and methods

# crom_l1_composed_RoleInheritance class attributes and methods

# crom_l1_composed_RelationshipImplication class attributes and methods

# InterRelationshipConstraint class attributes and methods

# crom_l1_composed_RelationTarget class attributes and methods

# crom_l1_composed_Irreflexive class attributes and methods

# IntraRelationshipConstraint class attributes and methods

# crom_l1_composed_Cyclic class attributes and methods

# crom_l1_composed_Total class attributes and methods

# RoleGroupElement class attributes and methods

# crom_l1_composed_RoleGroup class attributes and methods
crom_l1_composed_RoleGroup_lower: Property = Property(name="lower", type=IntegerType)
crom_l1_composed_RoleGroup_upper: Property = Property(name="upper", type=IntegerType)
crom_l1_composed_RoleGroup.attributes={crom_l1_composed_RoleGroup_lower, crom_l1_composed_RoleGroup_upper}

# crom_l1_composed_RoleGroupElement class attributes and methods

# crom_l1_composed_RoleImplication class attributes and methods

# crom_l1_composed_TypedElement class attributes and methods

# crom_l1_composed_ParthoodConstraint class attributes and methods
crom_l1_composed_ParthoodConstraint_kind: Property = Property(name="kind", type=StringType)
crom_l1_composed_ParthoodConstraint.attributes={crom_l1_composed_ParthoodConstraint_kind}

# crom_l1_composed_AbstractRoleRef class attributes and methods

# Relationships
tr_extends13: BinaryAssociation = BinaryAssociation(
    name="tr_extends13",
    ends={
        Property(name="crom_l1_composed_NaturalType", type=crom_l1_composed_NaturalType, multiplicity=Multiplicity(1, 1)),
        Property(name="crom_l1_composed_NaturalType12", type=crom_l1_composed_NaturalType, multiplicity=Multiplicity(0, 1))
    }
)
parts14: BinaryAssociation = BinaryAssociation(
    name="parts14",
    ends={
        Property(name="Part", type=crom_l1_composed_CompartmentType, multiplicity=Multiplicity(1, 1)),
        Property(name="whole", type=crom_l1_composed_Part, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="crom_l1_composed_ModelElement", type=crom_l1_composed_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="crom_l1_composed_Model", type=crom_l1_composed_ModelElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relations1: BinaryAssociation = BinaryAssociation(
    name="relations1",
    ends={
        Property(name="crom_l1_composed_Relation", type=crom_l1_composed_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="crom_l1_composed_Model2", type=crom_l1_composed_Relation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
params3: BinaryAssociation = BinaryAssociation(
    name="params3",
    ends={
        Property(name="crom_l1_composed_Parameter", type=crom_l1_composed_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="crom_l1_composed_Operation", type=crom_l1_composed_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owner4: BinaryAssociation = BinaryAssociation(
    name="owner4",
    ends={
        Property(name="Type", type=crom_l1_composed_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="operations", type=crom_l1_composed_Type, multiplicity=Multiplicity(1, 1))
    }
)
owner5: BinaryAssociation = BinaryAssociation(
    name="owner5",
    ends={
        Property(name="Type6", type=crom_l1_composed_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="attributes", type=crom_l1_composed_Type, multiplicity=Multiplicity(1, 1))
    }
)
attributes7: BinaryAssociation = BinaryAssociation(
    name="attributes7",
    ends={
        Property(name="Attribute", type=crom_l1_composed_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=crom_l1_composed_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operations8: BinaryAssociation = BinaryAssociation(
    name="operations8",
    ends={
        Property(name="Operation", type=crom_l1_composed_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="owner9", type=crom_l1_composed_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tr_extends11: BinaryAssociation = BinaryAssociation(
    name="tr_extends11",
    ends={
        Property(name="crom_l1_composed_DataType", type=crom_l1_composed_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="crom_l1_composed_DataType10", type=crom_l1_composed_DataType, multiplicity=Multiplicity(0, 1))
    }
)
relationships15: BinaryAssociation = BinaryAssociation(
    name="relationships15",
    ends={
        Property(name="crom_l1_composed_Relationship", type=crom_l1_composed_CompartmentType, multiplicity=Multiplicity(1, 1)),
        Property(name="crom_l1_composed_CompartmentType", type=crom_l1_composed_Relationship, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constraints16: BinaryAssociation = BinaryAssociation(
    name="constraints16",
    ends={
        Property(name="crom_l1_composed_Constraint", type=crom_l1_composed_CompartmentType, multiplicity=Multiplicity(1, 1)),
        Property(name="crom_l1_composed_CompartmentType17", type=crom_l1_composed_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tr_extends19: BinaryAssociation = BinaryAssociation(
    name="tr_extends19",
    ends={
        Property(name="crom_l1_composed_CompartmentType20", type=crom_l1_composed_CompartmentType, multiplicity=Multiplicity(1, 1)),
        Property(name="crom_l1_composed_CompartmentType18", type=crom_l1_composed_CompartmentType, multiplicity=Multiplicity(0, 1))
    }
)
tr_extends22: BinaryAssociation = BinaryAssociation(
    name="tr_extends22",
    ends={
        Property(name="crom_l1_composed_RoleType", type=crom_l1_composed_RoleType, multiplicity=Multiplicity(1, 1)),
        Property(name="crom_l1_composed_RoleType21", type=crom_l1_composed_RoleType, multiplicity=Multiplicity(0, 1))
    }
)
first23: BinaryAssociation = BinaryAssociation(
    name="first23",
    ends={
        Property(name="crom_l1_composed_Place", type=crom_l1_composed_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="crom_l1_composed_Relationship24", type=crom_l1_composed_Place, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
second25: BinaryAssociation = BinaryAssociation(
    name="second25",
    ends={
        Property(name="crom_l1_composed_Place27", type=crom_l1_composed_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="crom_l1_composed_Relationship26", type=crom_l1_composed_Place, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tr_constraints28: BinaryAssociation = BinaryAssociation(
    name="tr_constraints28",
    ends={
        Property(name="crom_l1_composed_IntraRelationshipConstraint", type=crom_l1_composed_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="crom_l1_composed_Relationship29", type=crom_l1_composed_IntraRelationshipConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
filled30: BinaryAssociation = BinaryAssociation(
    name="filled30",
    ends={
        Property(name="crom_l1_composed_AbstractRole", type=crom_l1_composed_Fulfillment, multiplicity=Multiplicity(1, 1)),
        Property(name="crom_l1_composed_Fulfillment", type=crom_l1_composed_AbstractRole, multiplicity=Multiplicity(1, 1))
    }
)
filler31: BinaryAssociation = BinaryAssociation(
    name="filler31",
    ends={
        Property(name="crom_l1_composed_RigidType", type=crom_l1_composed_Fulfillment, multiplicity=Multiplicity(1, 1)),
        Property(name="crom_l1_composed_Fulfillment32", type=crom_l1_composed_RigidType, multiplicity=Multiplicity(1, 1))
    }
)
sub60: BinaryAssociation = BinaryAssociation(
    name="sub60",
    ends={
        Property(name="crom_l1_composed_CompartmentInheritance61", type=crom_l1_composed_CompartmentType, multiplicity=Multiplicity(1, 1)),
        Property(name="crom_l1_composed_CompartmentType62", type=crom_l1_composed_CompartmentInheritance, multiplicity=Multiplicity(1, 1))
    }
)
first33: BinaryAssociation = BinaryAssociation(
    name="first33",
    ends={
        Property(name="crom_l1_composed_AbstractRole34", type=crom_l1_composed_RoleConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="crom_l1_composed_RoleConstraint", type=crom_l1_composed_AbstractRole, multiplicity=Multiplicity(1, 1))
    }
)
second35: BinaryAssociation = BinaryAssociation(
    name="second35",
    ends={
        Property(name="crom_l1_composed_AbstractRole37", type=crom_l1_composed_RoleConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="crom_l1_composed_RoleConstraint36", type=crom_l1_composed_AbstractRole, multiplicity=Multiplicity(1, 1))
    }
)
relation38: BinaryAssociation = BinaryAssociation(
    name="relation38",
    ends={
        Property(name="crom_l1_composed_Relationship40", type=crom_l1_composed_IntraRelationshipConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="crom_l1_composed_IntraRelationshipConstraint39", type=crom_l1_composed_Relationship, multiplicity=Multiplicity(0, 1))
    }
)
first41: BinaryAssociation = BinaryAssociation(
    name="first41",
    ends={
        Property(name="crom_l1_composed_Relationship42", type=crom_l1_composed_InterRelationshipConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="crom_l1_composed_InterRelationshipConstraint", type=crom_l1_composed_Relationship, multiplicity=Multiplicity(1, 1))
    }
)
second43: BinaryAssociation = BinaryAssociation(
    name="second43",
    ends={
        Property(name="crom_l1_composed_Relationship45", type=crom_l1_composed_InterRelationshipConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="crom_l1_composed_InterRelationshipConstraint44", type=crom_l1_composed_Relationship, multiplicity=Multiplicity(1, 1))
    }
)
targets46: BinaryAssociation = BinaryAssociation(
    name="targets46",
    ends={
        Property(name="crom_l1_composed_AbstractRole47", type=crom_l1_composed_ComplexConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="crom_l1_composed_ComplexConstraint", type=crom_l1_composed_AbstractRole, multiplicity=Multiplicity(1, 9999))
    }
)
super48: BinaryAssociation = BinaryAssociation(
    name="super48",
    ends={
        Property(name="crom_l1_composed_DataType49", type=crom_l1_composed_DataInheritance, multiplicity=Multiplicity(1, 1)),
        Property(name="crom_l1_composed_DataInheritance", type=crom_l1_composed_DataType, multiplicity=Multiplicity(1, 1))
    }
)
sub50: BinaryAssociation = BinaryAssociation(
    name="sub50",
    ends={
        Property(name="crom_l1_composed_DataType52", type=crom_l1_composed_DataInheritance, multiplicity=Multiplicity(1, 1)),
        Property(name="crom_l1_composed_DataInheritance51", type=crom_l1_composed_DataType, multiplicity=Multiplicity(1, 1))
    }
)
super53: BinaryAssociation = BinaryAssociation(
    name="super53",
    ends={
        Property(name="crom_l1_composed_NaturalType54", type=crom_l1_composed_NaturalInheritance, multiplicity=Multiplicity(1, 1)),
        Property(name="crom_l1_composed_NaturalInheritance", type=crom_l1_composed_NaturalType, multiplicity=Multiplicity(1, 1))
    }
)
sub55: BinaryAssociation = BinaryAssociation(
    name="sub55",
    ends={
        Property(name="crom_l1_composed_NaturalType57", type=crom_l1_composed_NaturalInheritance, multiplicity=Multiplicity(1, 1)),
        Property(name="crom_l1_composed_NaturalInheritance56", type=crom_l1_composed_NaturalType, multiplicity=Multiplicity(1, 1))
    }
)
super58: BinaryAssociation = BinaryAssociation(
    name="super58",
    ends={
        Property(name="crom_l1_composed_CompartmentType59", type=crom_l1_composed_CompartmentInheritance, multiplicity=Multiplicity(1, 1)),
        Property(name="crom_l1_composed_CompartmentInheritance", type=crom_l1_composed_CompartmentType, multiplicity=Multiplicity(1, 1))
    }
)
super63: BinaryAssociation = BinaryAssociation(
    name="super63",
    ends={
        Property(name="crom_l1_composed_RoleType64", type=crom_l1_composed_RoleInheritance, multiplicity=Multiplicity(1, 1)),
        Property(name="crom_l1_composed_RoleInheritance", type=crom_l1_composed_RoleType, multiplicity=Multiplicity(1, 1))
    }
)
sub65: BinaryAssociation = BinaryAssociation(
    name="sub65",
    ends={
        Property(name="crom_l1_composed_RoleType67", type=crom_l1_composed_RoleInheritance, multiplicity=Multiplicity(1, 1)),
        Property(name="crom_l1_composed_RoleInheritance66", type=crom_l1_composed_RoleType, multiplicity=Multiplicity(1, 1))
    }
)
holder68: BinaryAssociation = BinaryAssociation(
    name="holder68",
    ends={
        Property(name="crom_l1_composed_RoleType70", type=crom_l1_composed_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="crom_l1_composed_Place69", type=crom_l1_composed_RoleType, multiplicity=Multiplicity(1, 1))
    }
)
incoming71: BinaryAssociation = BinaryAssociation(
    name="incoming71",
    ends={
        Property(name="crom_l1_composed_Relation72", type=crom_l1_composed_RelationTarget, multiplicity=Multiplicity(1, 1)),
        Property(name="crom_l1_composed_RelationTarget", type=crom_l1_composed_Relation, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing73: BinaryAssociation = BinaryAssociation(
    name="outgoing73",
    ends={
        Property(name="crom_l1_composed_Relation75", type=crom_l1_composed_RelationTarget, multiplicity=Multiplicity(1, 1)),
        Property(name="crom_l1_composed_RelationTarget74", type=crom_l1_composed_Relation, multiplicity=Multiplicity(0, 9999))
    }
)
elements76: BinaryAssociation = BinaryAssociation(
    name="elements76",
    ends={
        Property(name="crom_l1_composed_RoleGroupElement", type=crom_l1_composed_RoleGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="crom_l1_composed_RoleGroup", type=crom_l1_composed_RoleGroupElement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
whole77: BinaryAssociation = BinaryAssociation(
    name="whole77",
    ends={
        Property(name="CompartmentType", type=crom_l1_composed_Part, multiplicity=Multiplicity(1, 1)),
        Property(name="parts", type=crom_l1_composed_CompartmentType, multiplicity=Multiplicity(1, 1))
    }
)
role78: BinaryAssociation = BinaryAssociation(
    name="role78",
    ends={
        Property(name="crom_l1_composed_AbstractRole79", type=crom_l1_composed_Part, multiplicity=Multiplicity(1, 1)),
        Property(name="crom_l1_composed_Part", type=crom_l1_composed_AbstractRole, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type80: BinaryAssociation = BinaryAssociation(
    name="type80",
    ends={
        Property(name="crom_l1_composed_RigidType81", type=crom_l1_composed_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="crom_l1_composed_TypedElement", type=crom_l1_composed_RigidType, multiplicity=Multiplicity(1, 1))
    }
)
ref82: BinaryAssociation = BinaryAssociation(
    name="ref82",
    ends={
        Property(name="crom_l1_composed_AbstractRole83", type=crom_l1_composed_AbstractRoleRef, multiplicity=Multiplicity(1, 1)),
        Property(name="crom_l1_composed_AbstractRoleRef", type=crom_l1_composed_AbstractRole, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_crom_l1_composed_NaturalType_RigidType = Generalization(general=RigidType, specific=crom_l1_composed_NaturalType)
gen_crom_l1_composed_CompartmentType_RigidType = Generalization(general=RigidType, specific=crom_l1_composed_CompartmentType)
gen_crom_l1_composed_ModelElement_NamedElement = Generalization(general=NamedElement, specific=crom_l1_composed_ModelElement)
gen_crom_l1_composed_RigidType_Type = Generalization(general=Type, specific=crom_l1_composed_RigidType)
gen_crom_l1_composed_RigidType_ModelElement = Generalization(general=ModelElement, specific=crom_l1_composed_RigidType)
gen_crom_l1_composed_Group_ModelElement = Generalization(general=ModelElement, specific=crom_l1_composed_Group)
gen_crom_l1_composed_Group_Model = Generalization(general=Model, specific=crom_l1_composed_Group)
gen_crom_l1_composed_Parameter_TypedElement = Generalization(general=TypedElement, specific=crom_l1_composed_Parameter)
gen_crom_l1_composed_Operation_TypedElement = Generalization(general=TypedElement, specific=crom_l1_composed_Operation)
gen_crom_l1_composed_Attribute_TypedElement = Generalization(general=TypedElement, specific=crom_l1_composed_Attribute)
gen_crom_l1_composed_Type_RelationTarget = Generalization(general=RelationTarget, specific=crom_l1_composed_Type)
gen_crom_l1_composed_DataType_RigidType = Generalization(general=RigidType, specific=crom_l1_composed_DataType)
gen_crom_l1_composed_RelationshipConstraint_Constraint = Generalization(general=Constraint, specific=crom_l1_composed_RelationshipConstraint)
gen_crom_l1_composed_AntiRigidType_Type = Generalization(general=Type, specific=crom_l1_composed_AntiRigidType)
gen_crom_l1_composed_RoleType_AntiRigidType = Generalization(general=AntiRigidType, specific=crom_l1_composed_RoleType)
gen_crom_l1_composed_RoleType_AbstractRole = Generalization(general=AbstractRole, specific=crom_l1_composed_RoleType)
gen_crom_l1_composed_Relationship_Relation = Generalization(general=Relation, specific=crom_l1_composed_Relationship)
gen_crom_l1_composed_Relationship_NamedElement = Generalization(general=NamedElement, specific=crom_l1_composed_Relationship)
gen_crom_l1_composed_Fulfillment_Relation = Generalization(general=Relation, specific=crom_l1_composed_Fulfillment)
gen_crom_l1_composed_Inheritance_Relation = Generalization(general=Relation, specific=crom_l1_composed_Inheritance)
gen_crom_l1_composed_Constraint_Relation = Generalization(general=Relation, specific=crom_l1_composed_Constraint)
gen_crom_l1_composed_RoleConstraint_Constraint = Generalization(general=Constraint, specific=crom_l1_composed_RoleConstraint)
gen_crom_l1_composed_IntraRelationshipConstraint_RelationshipConstraint = Generalization(general=RelationshipConstraint, specific=crom_l1_composed_IntraRelationshipConstraint)
gen_crom_l1_composed_InterRelationshipConstraint_RelationshipConstraint = Generalization(general=RelationshipConstraint, specific=crom_l1_composed_InterRelationshipConstraint)
gen_crom_l1_composed_ComplexConstraint_Constraint = Generalization(general=Constraint, specific=crom_l1_composed_ComplexConstraint)
gen_crom_l1_composed_DataInheritance_Inheritance = Generalization(general=Inheritance, specific=crom_l1_composed_DataInheritance)
gen_crom_l1_composed_NaturalInheritance_Inheritance = Generalization(general=Inheritance, specific=crom_l1_composed_NaturalInheritance)
gen_crom_l1_composed_CompartmentInheritance_Inheritance = Generalization(general=Inheritance, specific=crom_l1_composed_CompartmentInheritance)
gen_crom_l1_composed_RoleImplication_RoleConstraint = Generalization(general=RoleConstraint, specific=crom_l1_composed_RoleImplication)
gen_crom_l1_composed_RoleEquivalence_RoleConstraint = Generalization(general=RoleConstraint, specific=crom_l1_composed_RoleEquivalence)
gen_crom_l1_composed_RoleInheritance_Inheritance = Generalization(general=Inheritance, specific=crom_l1_composed_RoleInheritance)
gen_crom_l1_composed_RelationshipImplication_InterRelationshipConstraint = Generalization(general=InterRelationshipConstraint, specific=crom_l1_composed_RelationshipImplication)
gen_crom_l1_composed_RelationTarget_NamedElement = Generalization(general=NamedElement, specific=crom_l1_composed_RelationTarget)
gen_crom_l1_composed_Irreflexive_IntraRelationshipConstraint = Generalization(general=IntraRelationshipConstraint, specific=crom_l1_composed_Irreflexive)
gen_crom_l1_composed_Cyclic_IntraRelationshipConstraint = Generalization(general=IntraRelationshipConstraint, specific=crom_l1_composed_Cyclic)
gen_crom_l1_composed_Total_IntraRelationshipConstraint = Generalization(general=IntraRelationshipConstraint, specific=crom_l1_composed_Total)
gen_crom_l1_composed_AbstractRole_RoleGroupElement = Generalization(general=RoleGroupElement, specific=crom_l1_composed_AbstractRole)
gen_crom_l1_composed_RoleGroup_AbstractRole = Generalization(general=AbstractRole, specific=crom_l1_composed_RoleGroup)
gen_crom_l1_composed_RoleGroup_RelationTarget = Generalization(general=RelationTarget, specific=crom_l1_composed_RoleGroup)
gen_crom_l1_composed_RoleProhibition_RoleConstraint = Generalization(general=RoleConstraint, specific=crom_l1_composed_RoleProhibition)
gen_crom_l1_composed_TypedElement_NamedElement = Generalization(general=NamedElement, specific=crom_l1_composed_TypedElement)
gen_crom_l1_composed_ParthoodConstraint_IntraRelationshipConstraint = Generalization(general=IntraRelationshipConstraint, specific=crom_l1_composed_ParthoodConstraint)
gen_crom_l1_composed_AbstractRoleRef_RoleGroupElement = Generalization(general=RoleGroupElement, specific=crom_l1_composed_AbstractRoleRef)

# Domain Model
domain_model = DomainModel(
    name="crom_l1_composed",
    types={crom_l1_composed_NamedElement, crom_l1_composed_NaturalType, crom_l1_composed_CompartmentType, crom_l1_composed_Part, crom_l1_composed_ModelElement, NamedElement, crom_l1_composed_Model, crom_l1_composed_Relation, crom_l1_composed_RigidType, Type, ModelElement, crom_l1_composed_Group, Model, crom_l1_composed_Parameter, TypedElement, crom_l1_composed_Operation, crom_l1_composed_Type, crom_l1_composed_Attribute, RelationTarget, crom_l1_composed_DataType, RigidType, crom_l1_composed_RelationshipConstraint, crom_l1_composed_Relationship, crom_l1_composed_Constraint, crom_l1_composed_AntiRigidType, crom_l1_composed_RoleType, AntiRigidType, AbstractRole, Relation, crom_l1_composed_Place, crom_l1_composed_IntraRelationshipConstraint, crom_l1_composed_Fulfillment, crom_l1_composed_AbstractRole, crom_l1_composed_Inheritance, crom_l1_composed_RoleConstraint, Constraint, RelationshipConstraint, crom_l1_composed_InterRelationshipConstraint, crom_l1_composed_ComplexConstraint, crom_l1_composed_DataInheritance, Inheritance, crom_l1_composed_NaturalInheritance, crom_l1_composed_CompartmentInheritance, RoleConstraint, crom_l1_composed_RoleEquivalence, crom_l1_composed_RoleProhibition, crom_l1_composed_RoleInheritance, crom_l1_composed_RelationshipImplication, InterRelationshipConstraint, crom_l1_composed_RelationTarget, crom_l1_composed_Irreflexive, IntraRelationshipConstraint, crom_l1_composed_Cyclic, crom_l1_composed_Total, RoleGroupElement, crom_l1_composed_RoleGroup, crom_l1_composed_RoleGroupElement, crom_l1_composed_RoleImplication, crom_l1_composed_TypedElement, crom_l1_composed_ParthoodConstraint, crom_l1_composed_AbstractRoleRef, Direction, Parthood},
    associations={tr_extends13, parts14, elements0, relations1, params3, owner4, owner5, attributes7, operations8, tr_extends11, relationships15, constraints16, tr_extends19, tr_extends22, first23, second25, tr_constraints28, filled30, filler31, sub60, first33, second35, relation38, first41, second43, targets46, super48, sub50, super53, sub55, super58, super63, sub65, holder68, incoming71, outgoing73, elements76, whole77, role78, type80, ref82},
    generalizations={gen_crom_l1_composed_NaturalType_RigidType, gen_crom_l1_composed_CompartmentType_RigidType, gen_crom_l1_composed_ModelElement_NamedElement, gen_crom_l1_composed_RigidType_Type, gen_crom_l1_composed_RigidType_ModelElement, gen_crom_l1_composed_Group_ModelElement, gen_crom_l1_composed_Group_Model, gen_crom_l1_composed_Parameter_TypedElement, gen_crom_l1_composed_Operation_TypedElement, gen_crom_l1_composed_Attribute_TypedElement, gen_crom_l1_composed_Type_RelationTarget, gen_crom_l1_composed_DataType_RigidType, gen_crom_l1_composed_RelationshipConstraint_Constraint, gen_crom_l1_composed_AntiRigidType_Type, gen_crom_l1_composed_RoleType_AntiRigidType, gen_crom_l1_composed_RoleType_AbstractRole, gen_crom_l1_composed_Relationship_Relation, gen_crom_l1_composed_Relationship_NamedElement, gen_crom_l1_composed_Fulfillment_Relation, gen_crom_l1_composed_Inheritance_Relation, gen_crom_l1_composed_Constraint_Relation, gen_crom_l1_composed_RoleConstraint_Constraint, gen_crom_l1_composed_IntraRelationshipConstraint_RelationshipConstraint, gen_crom_l1_composed_InterRelationshipConstraint_RelationshipConstraint, gen_crom_l1_composed_ComplexConstraint_Constraint, gen_crom_l1_composed_DataInheritance_Inheritance, gen_crom_l1_composed_NaturalInheritance_Inheritance, gen_crom_l1_composed_CompartmentInheritance_Inheritance, gen_crom_l1_composed_RoleImplication_RoleConstraint, gen_crom_l1_composed_RoleEquivalence_RoleConstraint, gen_crom_l1_composed_RoleInheritance_Inheritance, gen_crom_l1_composed_RelationshipImplication_InterRelationshipConstraint, gen_crom_l1_composed_RelationTarget_NamedElement, gen_crom_l1_composed_Irreflexive_IntraRelationshipConstraint, gen_crom_l1_composed_Cyclic_IntraRelationshipConstraint, gen_crom_l1_composed_Total_IntraRelationshipConstraint, gen_crom_l1_composed_AbstractRole_RoleGroupElement, gen_crom_l1_composed_RoleGroup_AbstractRole, gen_crom_l1_composed_RoleGroup_RelationTarget, gen_crom_l1_composed_RoleProhibition_RoleConstraint, gen_crom_l1_composed_TypedElement_NamedElement, gen_crom_l1_composed_ParthoodConstraint_IntraRelationshipConstraint, gen_crom_l1_composed_AbstractRoleRef_RoleGroupElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)