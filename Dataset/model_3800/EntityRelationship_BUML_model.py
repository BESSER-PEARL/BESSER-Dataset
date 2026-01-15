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
TypeEntity: Enumeration = Enumeration(
    name="TypeEntity",
    literals={
            EnumerationLiteral(name="Weak"),
			EnumerationLiteral(name="Regular")
    }
)

TypeAttribute: Enumeration = Enumeration(
    name="TypeAttribute",
    literals={
            EnumerationLiteral(name="Normal"),
			EnumerationLiteral(name="Composite"),
			EnumerationLiteral(name="Multivalued"),
			EnumerationLiteral(name="Optional"),
			EnumerationLiteral(name="Derived"),
			EnumerationLiteral(name="Dependence_in_identification")
    }
)

TypeRestriction: Enumeration = Enumeration(
    name="TypeRestriction",
    literals={
            EnumerationLiteral(name="Exclusion"),
			EnumerationLiteral(name="Inclusion")
    }
)

TypeRestriction2: Enumeration = Enumeration(
    name="TypeRestriction2",
    literals={
            EnumerationLiteral(name="Exclusiveness"),
			EnumerationLiteral(name="Inclusiveness")
    }
)

TypeRestrictionInheritance1: Enumeration = Enumeration(
    name="TypeRestrictionInheritance1",
    literals={
            EnumerationLiteral(name="Total"),
			EnumerationLiteral(name="Partial")
    }
)

TypeRestrictionInheritance2: Enumeration = Enumeration(
    name="TypeRestrictionInheritance2",
    literals={
            EnumerationLiteral(name="Exclusive"),
			EnumerationLiteral(name="Overlapped")
    }
)

TypeIdentifier: Enumeration = Enumeration(
    name="TypeIdentifier",
    literals={
            EnumerationLiteral(name="NoIdentifier"),
			EnumerationLiteral(name="PrimaryIdentifier"),
			EnumerationLiteral(name="AlternativeIdentifier")
    }
)

TypeRelationship: Enumeration = Enumeration(
    name="TypeRelationship",
    literals={
            EnumerationLiteral(name="Regular"),
			EnumerationLiteral(name="Weak_dependence_in_existence"),
			EnumerationLiteral(name="Weak_dependence_in_identification")
    }
)

# Classes
entityrelationship_Connection_Generalization_Entity = Class(name="entityrelationship::Connection::Generalization::Entity")
entityrelationship_Connection_E_R_Restriction = Class(name="entityrelationship::Connection::E::R::Restriction")
entityrelationship_Entity_Relationship_Model = Class(name="entityrelationship::Entity::Relationship::Model")
entityrelationship_Elements_with_Attributes = Class(name="entityrelationship::Elements::with::Attributes")
entityrelationship_Relationships_Restriction = Class(name="entityrelationship::Relationships::Restriction")
entityrelationship_Connection_Entity2Relationship = Class(name="entityrelationship::Connection::Entity2Relationship")
entityrelationship_Connection_Relationship2Entity = Class(name="entityrelationship::Connection::Relationship2Entity")
entityrelationship_Connection_ConnectionEntityRelationship2Attribute = Class(name="entityrelationship::Connection::ConnectionEntityRelationship2Attribute")
entityrelationship_Connection_With_Attribute = Class(name="entityrelationship::Connection::With::Attribute")
entityrelationship_Attribute = Class(name="entityrelationship::Attribute")
entityrelationship_Generalization = Class(name="entityrelationship::Generalization")
entityrelationship_Entity = Class(name="entityrelationship::Entity")
Elements_with_Attributes = Class(name="Elements::with::Attributes")
entityrelationship_Attribute_Composite = Class(name="entityrelationship::Attribute::Composite")
entityrelationship_Relationship = Class(name="entityrelationship::Relationship")
entityrelationship_Connection_EntityRelationship = Class(name="entityrelationship::Connection::EntityRelationship", is_abstract=True)
Connection_EntityRelationship = Class(name="Connection::EntityRelationship")

# entityrelationship_Connection_Generalization_Entity class attributes and methods
entityrelationship_Connection_Generalization_Entity_minimum_cardinality: Property = Property(name="minimum_cardinality", type=StringType)
entityrelationship_Connection_Generalization_Entity_maximum_cardinality: Property = Property(name="maximum_cardinality", type=StringType)
entityrelationship_Connection_Generalization_Entity.attributes={entityrelationship_Connection_Generalization_Entity_maximum_cardinality, entityrelationship_Connection_Generalization_Entity_minimum_cardinality}

# entityrelationship_Connection_E_R_Restriction class attributes and methods
entityrelationship_Connection_E_R_Restriction_type_restriction: Property = Property(name="type_restriction", type=StringType)
entityrelationship_Connection_E_R_Restriction.attributes={entityrelationship_Connection_E_R_Restriction_type_restriction}

# entityrelationship_Entity_Relationship_Model class attributes and methods
entityrelationship_Entity_Relationship_Model_name: Property = Property(name="name", type=StringType)
entityrelationship_Entity_Relationship_Model.attributes={entityrelationship_Entity_Relationship_Model_name}

# entityrelationship_Elements_with_Attributes class attributes and methods

# entityrelationship_Relationships_Restriction class attributes and methods
entityrelationship_Relationships_Restriction_type_restriction: Property = Property(name="type_restriction", type=StringType)
entityrelationship_Relationships_Restriction.attributes={entityrelationship_Relationships_Restriction_type_restriction}

# entityrelationship_Connection_Entity2Relationship class attributes and methods

# entityrelationship_Connection_Relationship2Entity class attributes and methods

# entityrelationship_Connection_ConnectionEntityRelationship2Attribute class attributes and methods

# entityrelationship_Connection_With_Attribute class attributes and methods
entityrelationship_Connection_With_Attribute_type_attribute: Property = Property(name="type_attribute", type=StringType)
entityrelationship_Connection_With_Attribute.attributes={entityrelationship_Connection_With_Attribute_type_attribute}

# entityrelationship_Attribute class attributes and methods
entityrelationship_Attribute_name_attribute: Property = Property(name="name_attribute", type=StringType)
entityrelationship_Attribute_identifier: Property = Property(name="identifier", type=StringType)
entityrelationship_Attribute.attributes={entityrelationship_Attribute_name_attribute, entityrelationship_Attribute_identifier}

# entityrelationship_Generalization class attributes and methods
entityrelationship_Generalization_restriction_inheritance_1: Property = Property(name="restriction_inheritance_1", type=StringType)
entityrelationship_Generalization_restriction_inheritance_2: Property = Property(name="restriction_inheritance_2", type=StringType)
entityrelationship_Generalization.attributes={entityrelationship_Generalization_restriction_inheritance_2, entityrelationship_Generalization_restriction_inheritance_1}

# entityrelationship_Entity class attributes and methods
entityrelationship_Entity_name_entity: Property = Property(name="name_entity", type=StringType)
entityrelationship_Entity_type_entity: Property = Property(name="type_entity", type=StringType)
entityrelationship_Entity.attributes={entityrelationship_Entity_type_entity, entityrelationship_Entity_name_entity}

# Elements_with_Attributes class attributes and methods

# entityrelationship_Attribute_Composite class attributes and methods
entityrelationship_Attribute_Composite_name_at_composite: Property = Property(name="name_at_composite", type=StringType)
entityrelationship_Attribute_Composite_identifier_at_composite: Property = Property(name="identifier_at_composite", type=StringType)
entityrelationship_Attribute_Composite.attributes={entityrelationship_Attribute_Composite_identifier_at_composite, entityrelationship_Attribute_Composite_name_at_composite}

# entityrelationship_Relationship class attributes and methods
entityrelationship_Relationship_name_relationship: Property = Property(name="name_relationship", type=StringType)
entityrelationship_Relationship_order: Property = Property(name="order", type=IntegerType)
entityrelationship_Relationship_cardinality: Property = Property(name="cardinality", type=StringType)
entityrelationship_Relationship_type_relationship: Property = Property(name="type_relationship", type=StringType)
entityrelationship_Relationship.attributes={entityrelationship_Relationship_order, entityrelationship_Relationship_cardinality, entityrelationship_Relationship_type_relationship, entityrelationship_Relationship_name_relationship}

# entityrelationship_Connection_EntityRelationship class attributes and methods
entityrelationship_Connection_EntityRelationship_role: Property = Property(name="role", type=StringType)
entityrelationship_Connection_EntityRelationship_minimum_cardinality: Property = Property(name="minimum_cardinality", type=StringType)
entityrelationship_Connection_EntityRelationship_maximum_cardinality: Property = Property(name="maximum_cardinality", type=StringType)
entityrelationship_Connection_EntityRelationship.attributes={entityrelationship_Connection_EntityRelationship_maximum_cardinality, entityrelationship_Connection_EntityRelationship_role, entityrelationship_Connection_EntityRelationship_minimum_cardinality}

# Connection_EntityRelationship class attributes and methods

# Relationships
ERM_Has_Gen9: BinaryAssociation = BinaryAssociation(
    name="ERM_Has_Gen9",
    ends={
        Property(name="Connection_Generalization_Entity", type=entityrelationship_Entity_Relationship_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="inEntityRelationshipModel10", type=entityrelationship_Connection_Generalization_Entity, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
ERM_Has_Rt211: BinaryAssociation = BinaryAssociation(
    name="ERM_Has_Rt211",
    ends={
        Property(name="Connection_E_R_Restriction", type=entityrelationship_Entity_Relationship_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="inEntityRelationshipModel12", type=entityrelationship_Connection_E_R_Restriction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ERM_Has_E0: BinaryAssociation = BinaryAssociation(
    name="ERM_Has_E0",
    ends={
        Property(name="Elements_with_Attributes", type=entityrelationship_Entity_Relationship_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="inEntityRelationshipModel", type=entityrelationship_Elements_with_Attributes, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
ERM_Has_Rt1: BinaryAssociation = BinaryAssociation(
    name="ERM_Has_Rt1",
    ends={
        Property(name="Relationships_Restriction", type=entityrelationship_Entity_Relationship_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="inEntityRelationshipModel2", type=entityrelationship_Relationships_Restriction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ERM_Has_ConnectionEntity2Relationship3: BinaryAssociation = BinaryAssociation(
    name="ERM_Has_ConnectionEntity2Relationship3",
    ends={
        Property(name="Connection_Entity2Relationship", type=entityrelationship_Entity_Relationship_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="inEntityRelationshipModel4", type=entityrelationship_Connection_Entity2Relationship, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ERM_Has_ConnectionRelationship2Entity5: BinaryAssociation = BinaryAssociation(
    name="ERM_Has_ConnectionRelationship2Entity5",
    ends={
        Property(name="Connection_Relationship2Entity", type=entityrelationship_Entity_Relationship_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="inEntityRelationshipModel6", type=entityrelationship_Connection_Relationship2Entity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ERM_HasConnectionEntityRelationship2Attribute7: BinaryAssociation = BinaryAssociation(
    name="ERM_HasConnectionEntityRelationship2Attribute7",
    ends={
        Property(name="Connection_ConnectionEntityRelationship2Attribute", type=entityrelationship_Entity_Relationship_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="inEntityRelationshipModel8", type=entityrelationship_Connection_ConnectionEntityRelationship2Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entity_connected_to_entity2relationship21: BinaryAssociation = BinaryAssociation(
    name="entity_connected_to_entity2relationship21",
    ends={
        Property(name="Connection_Entity2Relationship22", type=entityrelationship_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="source_entity", type=entityrelationship_Connection_Entity2Relationship, multiplicity=Multiplicity(0, 9999))
    }
)
entity_connected_to_relationship2entity23: BinaryAssociation = BinaryAssociation(
    name="entity_connected_to_relationship2entity23",
    ends={
        Property(name="Connection_Relationship2Entity24", type=entityrelationship_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="target_entity", type=entityrelationship_Connection_Relationship2Entity, multiplicity=Multiplicity(0, 9999))
    }
)
ERM_Has_CEA13: BinaryAssociation = BinaryAssociation(
    name="ERM_Has_CEA13",
    ends={
        Property(name="Connection_With_Attribute", type=entityrelationship_Entity_Relationship_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="inEntityRelationshipModel14", type=entityrelationship_Connection_With_Attribute, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
ERM_Has_At15: BinaryAssociation = BinaryAssociation(
    name="ERM_Has_At15",
    ends={
        Property(name="entityrelationship_Attribute", type=entityrelationship_Entity_Relationship_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="entityrelationship_Entity_Relationship_Model", type=entityrelationship_Attribute, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
ERM_Has_G16: BinaryAssociation = BinaryAssociation(
    name="ERM_Has_G16",
    ends={
        Property(name="Generalization", type=entityrelationship_Entity_Relationship_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="inEntityRelationshipModel17", type=entityrelationship_Generalization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connected_with_attribute18: BinaryAssociation = BinaryAssociation(
    name="connected_with_attribute18",
    ends={
        Property(name="Connection_With_Attribute19", type=entityrelationship_Elements_with_Attributes, multiplicity=Multiplicity(1, 1)),
        Property(name="element", type=entityrelationship_Connection_With_Attribute, multiplicity=Multiplicity(0, 9999))
    }
)
inEntityRelationshipModel20: BinaryAssociation = BinaryAssociation(
    name="inEntityRelationshipModel20",
    ends={
        Property(name="Entity_Relationship_Model", type=entityrelationship_Elements_with_Attributes, multiplicity=Multiplicity(1, 1)),
        Property(name="ERM_Has_E", type=entityrelationship_Entity_Relationship_Model, multiplicity=Multiplicity(0, 1))
    }
)
attributes_composites35: BinaryAssociation = BinaryAssociation(
    name="attributes_composites35",
    ends={
        Property(name="Attribute_Composite", type=entityrelationship_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="inAttribute", type=entityrelationship_Attribute_Composite, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subclass_generalizations25: BinaryAssociation = BinaryAssociation(
    name="subclass_generalizations25",
    ends={
        Property(name="Generalization26", type=entityrelationship_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="subclasses", type=entityrelationship_Generalization, multiplicity=Multiplicity(0, 9999))
    }
)
source_restrictions27: BinaryAssociation = BinaryAssociation(
    name="source_restrictions27",
    ends={
        Property(name="entityrelationship_Relationships_Restriction", type=entityrelationship_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="entityrelationship_Relationship", type=entityrelationship_Relationships_Restriction, multiplicity=Multiplicity(0, 1))
    }
)
target_restrictions28: BinaryAssociation = BinaryAssociation(
    name="target_restrictions28",
    ends={
        Property(name="Relationships_Restriction29", type=entityrelationship_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="target_relationship", type=entityrelationship_Relationships_Restriction, multiplicity=Multiplicity(0, 9999))
    }
)
relationship_connected_to_entity2relationship30: BinaryAssociation = BinaryAssociation(
    name="relationship_connected_to_entity2relationship30",
    ends={
        Property(name="Connection_Entity2Relationship32", type=entityrelationship_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="target_relationship31", type=entityrelationship_Connection_Entity2Relationship, multiplicity=Multiplicity(0, 9999))
    }
)
relationship_connected_to_relationship2entity33: BinaryAssociation = BinaryAssociation(
    name="relationship_connected_to_relationship2entity33",
    ends={
        Property(name="Connection_Relationship2Entity34", type=entityrelationship_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="source_relationship", type=entityrelationship_Connection_Relationship2Entity, multiplicity=Multiplicity(0, 9999))
    }
)
source_relationship53: BinaryAssociation = BinaryAssociation(
    name="source_relationship53",
    ends={
        Property(name="entityrelationship_Relationship55", type=entityrelationship_Relationships_Restriction, multiplicity=Multiplicity(1, 1)),
        Property(name="entityrelationship_Relationships_Restriction54", type=entityrelationship_Relationship, multiplicity=Multiplicity(1, 1))
    }
)
attributes_identification37: BinaryAssociation = BinaryAssociation(
    name="attributes_identification37",
    ends={
        Property(name="Attribute", type=entityrelationship_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="inAttribute38", type=entityrelationship_Attribute, multiplicity=Multiplicity(0, 9999))
    }
)
connected39: BinaryAssociation = BinaryAssociation(
    name="connected39",
    ends={
        Property(name="Connection_With_Attribute40", type=entityrelationship_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="connection_attribute", type=entityrelationship_Connection_With_Attribute, multiplicity=Multiplicity(1, 1))
    }
)
inAttribute42: BinaryAssociation = BinaryAssociation(
    name="inAttribute42",
    ends={
        Property(name="Attribute43", type=entityrelationship_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="attributes_identification", type=entityrelationship_Attribute, multiplicity=Multiplicity(0, 1))
    }
)
inEntityRelationshipModel44: BinaryAssociation = BinaryAssociation(
    name="inEntityRelationshipModel44",
    ends={
        Property(name="entityrelationship_Entity_Relationship_Model46", type=entityrelationship_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="entityrelationship_Attribute45", type=entityrelationship_Entity_Relationship_Model, multiplicity=Multiplicity(0, 1))
    }
)
attribute_connected_to_conection_entityrelationship_to_attribute47: BinaryAssociation = BinaryAssociation(
    name="attribute_connected_to_conection_entityrelationship_to_attribute47",
    ends={
        Property(name="Connection_ConnectionEntityRelationship2Attribute48", type=entityrelationship_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="target_attribute", type=entityrelationship_Connection_ConnectionEntityRelationship2Attribute, multiplicity=Multiplicity(0, 1))
    }
)
attributes49: BinaryAssociation = BinaryAssociation(
    name="attributes49",
    ends={
        Property(name="entityrelationship_Attribute50", type=entityrelationship_Attribute_Composite, multiplicity=Multiplicity(1, 1)),
        Property(name="entityrelationship_Attribute_Composite", type=entityrelationship_Attribute, multiplicity=Multiplicity(1, 1))
    }
)
inAttribute51: BinaryAssociation = BinaryAssociation(
    name="inAttribute51",
    ends={
        Property(name="Attribute52", type=entityrelationship_Attribute_Composite, multiplicity=Multiplicity(1, 1)),
        Property(name="attributes_composites", type=entityrelationship_Attribute, multiplicity=Multiplicity(0, 1))
    }
)
superclass66: BinaryAssociation = BinaryAssociation(
    name="superclass66",
    ends={
        Property(name="entityrelationship_Entity", type=entityrelationship_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="entityrelationship_Generalization", type=entityrelationship_Entity, multiplicity=Multiplicity(1, 1))
    }
)
inEntityRelationshipModel67: BinaryAssociation = BinaryAssociation(
    name="inEntityRelationshipModel67",
    ends={
        Property(name="Entity_Relationship_Model68", type=entityrelationship_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="ERM_Has_G", type=entityrelationship_Entity_Relationship_Model, multiplicity=Multiplicity(0, 1))
    }
)
target_relationship56: BinaryAssociation = BinaryAssociation(
    name="target_relationship56",
    ends={
        Property(name="Relationship", type=entityrelationship_Relationships_Restriction, multiplicity=Multiplicity(1, 1)),
        Property(name="target_restrictions", type=entityrelationship_Relationship, multiplicity=Multiplicity(1, 1))
    }
)
inEntityRelationshipModel57: BinaryAssociation = BinaryAssociation(
    name="inEntityRelationshipModel57",
    ends={
        Property(name="Entity_Relationship_Model58", type=entityrelationship_Relationships_Restriction, multiplicity=Multiplicity(1, 1)),
        Property(name="ERM_Has_Rt", type=entityrelationship_Entity_Relationship_Model, multiplicity=Multiplicity(0, 1))
    }
)
connection_source_entity_relationship59: BinaryAssociation = BinaryAssociation(
    name="connection_source_entity_relationship59",
    ends={
        Property(name="entityrelationship_Connection_EntityRelationship", type=entityrelationship_Connection_E_R_Restriction, multiplicity=Multiplicity(1, 1)),
        Property(name="entityrelationship_Connection_E_R_Restriction", type=entityrelationship_Connection_EntityRelationship, multiplicity=Multiplicity(1, 1))
    }
)
connection_target_entity_relationship60: BinaryAssociation = BinaryAssociation(
    name="connection_target_entity_relationship60",
    ends={
        Property(name="entityrelationship_Connection_EntityRelationship62", type=entityrelationship_Connection_E_R_Restriction, multiplicity=Multiplicity(1, 1)),
        Property(name="entityrelationship_Connection_E_R_Restriction61", type=entityrelationship_Connection_EntityRelationship, multiplicity=Multiplicity(1, 1))
    }
)
inEntityRelationshipModel63: BinaryAssociation = BinaryAssociation(
    name="inEntityRelationshipModel63",
    ends={
        Property(name="Entity_Relationship_Model64", type=entityrelationship_Connection_E_R_Restriction, multiplicity=Multiplicity(1, 1)),
        Property(name="ERM_Has_Rt2", type=entityrelationship_Entity_Relationship_Model, multiplicity=Multiplicity(0, 1))
    }
)
subclasses65: BinaryAssociation = BinaryAssociation(
    name="subclasses65",
    ends={
        Property(name="Entity", type=entityrelationship_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="subclass_generalizations", type=entityrelationship_Entity, multiplicity=Multiplicity(2, 9999))
    }
)
inEntityRelationshipModel80: BinaryAssociation = BinaryAssociation(
    name="inEntityRelationshipModel80",
    ends={
        Property(name="Entity_Relationship_Model81", type=entityrelationship_Connection_Generalization_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="ERM_Has_Gen", type=entityrelationship_Entity_Relationship_Model, multiplicity=Multiplicity(0, 1))
    }
)
connection_attribute69: BinaryAssociation = BinaryAssociation(
    name="connection_attribute69",
    ends={
        Property(name="Attribute70", type=entityrelationship_Connection_With_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="connected", type=entityrelationship_Attribute, multiplicity=Multiplicity(1, 1))
    }
)
element71: BinaryAssociation = BinaryAssociation(
    name="element71",
    ends={
        Property(name="Elements_with_Attributes72", type=entityrelationship_Connection_With_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="connected_with_attribute", type=entityrelationship_Elements_with_Attributes, multiplicity=Multiplicity(1, 1))
    }
)
inEntityRelationshipModel73: BinaryAssociation = BinaryAssociation(
    name="inEntityRelationshipModel73",
    ends={
        Property(name="Entity_Relationship_Model74", type=entityrelationship_Connection_With_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="ERM_Has_CEA", type=entityrelationship_Entity_Relationship_Model, multiplicity=Multiplicity(0, 1))
    }
)
Connection_Generalization75: BinaryAssociation = BinaryAssociation(
    name="Connection_Generalization75",
    ends={
        Property(name="entityrelationship_Generalization76", type=entityrelationship_Connection_Generalization_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="entityrelationship_Connection_Generalization_Entity", type=entityrelationship_Generalization, multiplicity=Multiplicity(1, 1))
    }
)
Connection_Entity77: BinaryAssociation = BinaryAssociation(
    name="Connection_Entity77",
    ends={
        Property(name="entityrelationship_Entity79", type=entityrelationship_Connection_Generalization_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="entityrelationship_Connection_Generalization_Entity78", type=entityrelationship_Entity, multiplicity=Multiplicity(1, 1))
    }
)
source_connection94: BinaryAssociation = BinaryAssociation(
    name="source_connection94",
    ends={
        Property(name="entityrelationship_Connection_EntityRelationship95", type=entityrelationship_Connection_ConnectionEntityRelationship2Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="entityrelationship_Connection_ConnectionEntityRelationship2Attribute", type=entityrelationship_Connection_EntityRelationship, multiplicity=Multiplicity(1, 1))
    }
)
target_attribute96: BinaryAssociation = BinaryAssociation(
    name="target_attribute96",
    ends={
        Property(name="Attribute97", type=entityrelationship_Connection_ConnectionEntityRelationship2Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="attribute_connected_to_conection_entityrelationship_to_attribute", type=entityrelationship_Attribute, multiplicity=Multiplicity(1, 1))
    }
)
inEntityRelationshipModel98: BinaryAssociation = BinaryAssociation(
    name="inEntityRelationshipModel98",
    ends={
        Property(name="Entity_Relationship_Model99", type=entityrelationship_Connection_ConnectionEntityRelationship2Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="ERM_HasConnectionEntityRelationship2Attribute", type=entityrelationship_Entity_Relationship_Model, multiplicity=Multiplicity(0, 1))
    }
)
source_entity82: BinaryAssociation = BinaryAssociation(
    name="source_entity82",
    ends={
        Property(name="Entity83", type=entityrelationship_Connection_Entity2Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="entity_connected_to_entity2relationship", type=entityrelationship_Entity, multiplicity=Multiplicity(0, 1))
    }
)
target_relationship84: BinaryAssociation = BinaryAssociation(
    name="target_relationship84",
    ends={
        Property(name="Relationship85", type=entityrelationship_Connection_Entity2Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="relationship_connected_to_entity2relationship", type=entityrelationship_Relationship, multiplicity=Multiplicity(0, 1))
    }
)
inEntityRelationshipModel86: BinaryAssociation = BinaryAssociation(
    name="inEntityRelationshipModel86",
    ends={
        Property(name="Entity_Relationship_Model87", type=entityrelationship_Connection_Entity2Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="ERM_Has_ConnectionEntity2Relationship", type=entityrelationship_Entity_Relationship_Model, multiplicity=Multiplicity(0, 1))
    }
)
source_relationship88: BinaryAssociation = BinaryAssociation(
    name="source_relationship88",
    ends={
        Property(name="Relationship89", type=entityrelationship_Connection_Relationship2Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="relationship_connected_to_relationship2entity", type=entityrelationship_Relationship, multiplicity=Multiplicity(0, 1))
    }
)
target_entity90: BinaryAssociation = BinaryAssociation(
    name="target_entity90",
    ends={
        Property(name="Entity91", type=entityrelationship_Connection_Relationship2Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="entity_connected_to_relationship2entity", type=entityrelationship_Entity, multiplicity=Multiplicity(0, 1))
    }
)
inEntityRelationshipModel92: BinaryAssociation = BinaryAssociation(
    name="inEntityRelationshipModel92",
    ends={
        Property(name="Entity_Relationship_Model93", type=entityrelationship_Connection_Relationship2Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="ERM_Has_ConnectionRelationship2Entity", type=entityrelationship_Entity_Relationship_Model, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_entityrelationship_Entity_Elements_with_Attributes = Generalization(general=Elements_with_Attributes, specific=entityrelationship_Entity)
gen_entityrelationship_Relationship_Elements_with_Attributes = Generalization(general=Elements_with_Attributes, specific=entityrelationship_Relationship)
gen_entityrelationship_Connection_Entity2Relationship_Connection_EntityRelationship = Generalization(general=Connection_EntityRelationship, specific=entityrelationship_Connection_Entity2Relationship)
gen_entityrelationship_Connection_Relationship2Entity_Connection_EntityRelationship = Generalization(general=Connection_EntityRelationship, specific=entityrelationship_Connection_Relationship2Entity)

# Domain Model
domain_model = DomainModel(
    name="entityrelationship",
    types={entityrelationship_Connection_Generalization_Entity, entityrelationship_Connection_E_R_Restriction, entityrelationship_Entity_Relationship_Model, entityrelationship_Elements_with_Attributes, entityrelationship_Relationships_Restriction, entityrelationship_Connection_Entity2Relationship, entityrelationship_Connection_Relationship2Entity, entityrelationship_Connection_ConnectionEntityRelationship2Attribute, entityrelationship_Connection_With_Attribute, entityrelationship_Attribute, entityrelationship_Generalization, entityrelationship_Entity, Elements_with_Attributes, entityrelationship_Attribute_Composite, entityrelationship_Relationship, entityrelationship_Connection_EntityRelationship, Connection_EntityRelationship, TypeEntity, TypeAttribute, TypeRestriction, TypeRestriction2, TypeRestrictionInheritance1, TypeRestrictionInheritance2, TypeIdentifier, TypeRelationship},
    associations={ERM_Has_Gen9, ERM_Has_Rt211, ERM_Has_E0, ERM_Has_Rt1, ERM_Has_ConnectionEntity2Relationship3, ERM_Has_ConnectionRelationship2Entity5, ERM_HasConnectionEntityRelationship2Attribute7, entity_connected_to_entity2relationship21, entity_connected_to_relationship2entity23, ERM_Has_CEA13, ERM_Has_At15, ERM_Has_G16, connected_with_attribute18, inEntityRelationshipModel20, attributes_composites35, subclass_generalizations25, source_restrictions27, target_restrictions28, relationship_connected_to_entity2relationship30, relationship_connected_to_relationship2entity33, source_relationship53, attributes_identification37, connected39, inAttribute42, inEntityRelationshipModel44, attribute_connected_to_conection_entityrelationship_to_attribute47, attributes49, inAttribute51, superclass66, inEntityRelationshipModel67, target_relationship56, inEntityRelationshipModel57, connection_source_entity_relationship59, connection_target_entity_relationship60, inEntityRelationshipModel63, subclasses65, inEntityRelationshipModel80, connection_attribute69, element71, inEntityRelationshipModel73, Connection_Generalization75, Connection_Entity77, source_connection94, target_attribute96, inEntityRelationshipModel98, source_entity82, target_relationship84, inEntityRelationshipModel86, source_relationship88, target_entity90, inEntityRelationshipModel92},
    generalizations={gen_entityrelationship_Entity_Elements_with_Attributes, gen_entityrelationship_Relationship_Elements_with_Attributes, gen_entityrelationship_Connection_Entity2Relationship_Connection_EntityRelationship, gen_entityrelationship_Connection_Relationship2Entity_Connection_EntityRelationship},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)