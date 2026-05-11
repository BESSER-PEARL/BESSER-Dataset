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
entities_SimpleType = Class(name="entities_SimpleType")
Type = Class(name="Type")
entities_Entity = Class(name="entities_Entity")
entities_Property = Class(name="entities_Property")
entities_Model = Class(name="entities_Model")
entities_Type = Class(name="entities_Type")

# entities_SimpleType class attributes and methods

# Type class attributes and methods

# entities_Entity class attributes and methods

# entities_Property class attributes and methods
entities_Property_name: Property = Property(name="name", type=StringType)
entities_Property_many: Property = Property(name="many", type=BooleanType)
entities_Property.attributes={entities_Property_name, entities_Property_many}

# entities_Model class attributes and methods

# entities_Type class attributes and methods
entities_Type_name: Property = Property(name="name", type=StringType)
entities_Type.attributes={entities_Type_name}

# Relationships
properties1: BinaryAssociation = BinaryAssociation(
    name="properties1",
    ends={
        Property(name="entities_Property", type=entities_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="entities_Entity", type=entities_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extends3: BinaryAssociation = BinaryAssociation(
    name="extends3",
    ends={
        Property(name="entities_Entity4", type=entities_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="entities_Entity2", type=entities_Entity, multiplicity=Multiplicity(0, 1))
    }
)
type5: BinaryAssociation = BinaryAssociation(
    name="type5",
    ends={
        Property(name="entities_Type7", type=entities_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="entities_Property6", type=entities_Type, multiplicity=Multiplicity(0, 1))
    }
)
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="entities_Type", type=entities_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="entities_Model", type=entities_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_entities_SimpleType_Type = Generalization(general=Type, specific=entities_SimpleType)
gen_entities_Entity_Type = Generalization(general=Type, specific=entities_Entity)

# Domain Model
domain_model = DomainModel(
    name="entities",
    types={entities_SimpleType, Type, entities_Entity, entities_Property, entities_Model, entities_Type},
    associations={properties1, extends3, type5, elements0},
    generalizations={gen_entities_SimpleType_Type, gen_entities_Entity_Type},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)