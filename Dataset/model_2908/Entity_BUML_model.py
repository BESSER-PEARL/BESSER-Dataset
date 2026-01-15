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
entity_TypeDef = Class(name="entity::TypeDef")
Type = Class(name="Type")
entity_JAVAID = Class(name="entity::JAVAID")
entity_Model = Class(name="entity::Model")
entity_Type = Class(name="entity::Type")
entity_Entity = Class(name="entity::Entity")
entity_Attribute = Class(name="entity::Attribute")

# entity_TypeDef class attributes and methods

# Type class attributes and methods

# entity_JAVAID class attributes and methods
entity_JAVAID_name: Property = Property(name="name", type=StringType)
entity_JAVAID.attributes={entity_JAVAID_name}

# entity_Model class attributes and methods

# entity_Type class attributes and methods
entity_Type_name: Property = Property(name="name", type=StringType)
entity_Type.attributes={entity_Type_name}

# entity_Entity class attributes and methods

# entity_Attribute class attributes and methods
entity_Attribute_many: Property = Property(name="many", type=BooleanType)
entity_Attribute_name: Property = Property(name="name", type=StringType)
entity_Attribute.attributes={entity_Attribute_name, entity_Attribute_many}

# Relationships
mappedType1: BinaryAssociation = BinaryAssociation(
    name="mappedType1",
    ends={
        Property(name="entity_JAVAID", type=entity_TypeDef, multiplicity=Multiplicity(1, 1)),
        Property(name="entity_TypeDef", type=entity_JAVAID, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
types0: BinaryAssociation = BinaryAssociation(
    name="types0",
    ends={
        Property(name="entity_Type", type=entity_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="entity_Model", type=entity_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type6: BinaryAssociation = BinaryAssociation(
    name="type6",
    ends={
        Property(name="entity_Type8", type=entity_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="entity_Attribute7", type=entity_Type, multiplicity=Multiplicity(0, 1))
    }
)
superEntity3: BinaryAssociation = BinaryAssociation(
    name="superEntity3",
    ends={
        Property(name="entity_Entity", type=entity_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="entity_Entity2", type=entity_Entity, multiplicity=Multiplicity(0, 1))
    }
)
attributes4: BinaryAssociation = BinaryAssociation(
    name="attributes4",
    ends={
        Property(name="entity_Attribute", type=entity_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="entity_Entity5", type=entity_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_entity_TypeDef_Type = Generalization(general=Type, specific=entity_TypeDef)
gen_entity_Entity_Type = Generalization(general=Type, specific=entity_Entity)

# Domain Model
domain_model = DomainModel(
    name="entity",
    types={entity_TypeDef, Type, entity_JAVAID, entity_Model, entity_Type, entity_Entity, entity_Attribute},
    associations={mappedType1, types0, type6, superEntity3, attributes4},
    generalizations={gen_entity_TypeDef_Type, gen_entity_Entity_Type},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)