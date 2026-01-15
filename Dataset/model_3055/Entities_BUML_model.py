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
entities_Model = Class(name="entities::Model")
entities_Entity = Class(name="entities::Entity")
entities_Property = Class(name="entities::Property")
entities_SimpleProperty = Class(name="entities::SimpleProperty")
Property_ = Class(name="Property")
entities_ReferenceProperty = Class(name="entities::ReferenceProperty")

# entities_Model class attributes and methods

# entities_Entity class attributes and methods
entities_Entity_name: Property = Property(name="name", type=StringType)
entities_Entity.attributes={entities_Entity_name}

# entities_Property class attributes and methods
entities_Property_name: Property = Property(name="name", type=StringType)
entities_Property.attributes={entities_Property_name}

# entities_SimpleProperty class attributes and methods
entities_SimpleProperty_type: Property = Property(name="type", type=StringType)
entities_SimpleProperty.attributes={entities_SimpleProperty_type}

# Property class attributes and methods

# entities_ReferenceProperty class attributes and methods
entities_ReferenceProperty_many: Property = Property(name="many", type=BooleanType)
entities_ReferenceProperty.attributes={entities_ReferenceProperty_many}

# Relationships
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
properties4: BinaryAssociation = BinaryAssociation(
    name="properties4",
    ends={
        Property(name="entities_Property", type=entities_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="entities_Entity5", type=entities_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type6: BinaryAssociation = BinaryAssociation(
    name="type6",
    ends={
        Property(name="entities_Entity7", type=entities_ReferenceProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="entities_ReferenceProperty", type=entities_Entity, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_entities_SimpleProperty_Property = Generalization(general=Property_, specific=entities_SimpleProperty)
gen_entities_ReferenceProperty_Property = Generalization(general=Property_, specific=entities_ReferenceProperty)

# Domain Model
domain_model = DomainModel(
    name="entities",
    types={entities_Model, entities_Entity, entities_Property, entities_SimpleProperty, Property_, entities_ReferenceProperty},
    associations={entities0, superType2, properties4, type6},
    generalizations={gen_entities_SimpleProperty_Property, gen_entities_ReferenceProperty_Property},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)