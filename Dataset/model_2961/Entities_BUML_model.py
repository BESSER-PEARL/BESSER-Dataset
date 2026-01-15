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
entities_AttributeType = Class(name="entities::AttributeType")
entities_Model = Class(name="entities::Model")
entities_Entity = Class(name="entities::Entity")
entities_Attribute = Class(name="entities::Attribute")
entities_ElementType = Class(name="entities::ElementType")
entities_BasicType = Class(name="entities::BasicType")
ElementType = Class(name="ElementType")
entities_EntityType = Class(name="entities::EntityType")

# entities_AttributeType class attributes and methods
entities_AttributeType_array: Property = Property(name="array", type=BooleanType)
entities_AttributeType_length: Property = Property(name="length", type=IntegerType)
entities_AttributeType.attributes={entities_AttributeType_length, entities_AttributeType_array}

# entities_Model class attributes and methods

# entities_Entity class attributes and methods
entities_Entity_name_id: Property = Property(name="name_id", type=StringType)
entities_Entity.attributes={entities_Entity_name_id}

# entities_Attribute class attributes and methods
entities_Attribute_name: Property = Property(name="name", type=StringType)
entities_Attribute.attributes={entities_Attribute_name}

# entities_ElementType class attributes and methods

# entities_BasicType class attributes and methods
entities_BasicType_typeName: Property = Property(name="typeName", type=StringType)
entities_BasicType.attributes={entities_BasicType_typeName}

# ElementType class attributes and methods

# entities_EntityType class attributes and methods

# Relationships
type6: BinaryAssociation = BinaryAssociation(
    name="type6",
    ends={
        Property(name="entities_AttributeType", type=entities_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="entities_Attribute7", type=entities_AttributeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entities0: BinaryAssociation = BinaryAssociation(
    name="entities0",
    ends={
        Property(name="entities_Entity", type=entities_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="entities_Model", type=entities_Entity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superType2: BinaryAssociation = BinaryAssociation(
    name="superType2",
    ends={
        Property(name="entities_Entity3", type=entities_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="entities_Entity1", type=entities_Entity, multiplicity=Multiplicity(0, 1))
    }
)
attributes4: BinaryAssociation = BinaryAssociation(
    name="attributes4",
    ends={
        Property(name="entities_Attribute", type=entities_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="entities_Entity5", type=entities_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elementType8: BinaryAssociation = BinaryAssociation(
    name="elementType8",
    ends={
        Property(name="entities_ElementType", type=entities_AttributeType, multiplicity=Multiplicity(1, 1)),
        Property(name="entities_AttributeType9", type=entities_ElementType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entity10: BinaryAssociation = BinaryAssociation(
    name="entity10",
    ends={
        Property(name="entities_Entity11", type=entities_EntityType, multiplicity=Multiplicity(1, 1)),
        Property(name="entities_EntityType", type=entities_Entity, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_entities_BasicType_ElementType = Generalization(general=ElementType, specific=entities_BasicType)
gen_entities_EntityType_ElementType = Generalization(general=ElementType, specific=entities_EntityType)

# Domain Model
domain_model = DomainModel(
    name="entities",
    types={entities_AttributeType, entities_Model, entities_Entity, entities_Attribute, entities_ElementType, entities_BasicType, ElementType, entities_EntityType},
    associations={type6, entities0, superType2, attributes4, elementType8, entity10},
    generalizations={gen_entities_BasicType_ElementType, gen_entities_EntityType_ElementType},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)