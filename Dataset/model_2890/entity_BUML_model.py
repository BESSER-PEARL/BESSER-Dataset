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
entity_Domain = Class(name="entity::Domain")
entity_Type = Class(name="entity::Type", is_abstract=True)
entity_Datatype = Class(name="entity::Datatype")
Type = Class(name="Type")
entity_Entity = Class(name="entity::Entity")
entity_Feature = Class(name="entity::Feature")

# entity_Domain class attributes and methods
entity_Domain_name: Property = Property(name="name", type=StringType)
entity_Domain.attributes={entity_Domain_name}

# entity_Type class attributes and methods
entity_Type_name: Property = Property(name="name", type=StringType)
entity_Type.attributes={entity_Type_name}

# entity_Datatype class attributes and methods

# Type class attributes and methods

# entity_Entity class attributes and methods

# entity_Feature class attributes and methods
entity_Feature_name: Property = Property(name="name", type=StringType)
entity_Feature.attributes={entity_Feature_name}

# Relationships
types0: BinaryAssociation = BinaryAssociation(
    name="types0",
    ends={
        Property(name="entity_Type", type=entity_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="entity_Domain", type=entity_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
features1: BinaryAssociation = BinaryAssociation(
    name="features1",
    ends={
        Property(name="entity_Feature", type=entity_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="entity_Entity", type=entity_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type2: BinaryAssociation = BinaryAssociation(
    name="type2",
    ends={
        Property(name="entity_Type4", type=entity_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="entity_Feature3", type=entity_Type, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_entity_Datatype_Type = Generalization(general=Type, specific=entity_Datatype)
gen_entity_Entity_Type = Generalization(general=Type, specific=entity_Entity)

# Domain Model
domain_model = DomainModel(
    name="entity",
    types={entity_Domain, entity_Type, entity_Datatype, Type, entity_Entity, entity_Feature},
    associations={types0, features1, type2},
    generalizations={gen_entity_Datatype_Type, gen_entity_Entity_Type},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)