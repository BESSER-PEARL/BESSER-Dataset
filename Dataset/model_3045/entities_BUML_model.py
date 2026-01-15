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
entities_Feature = Class(name="entities::Feature")
entities_DomainModel = Class(name="entities::DomainModel")
entities_Entity = Class(name="entities::Entity")

# entities_Feature class attributes and methods
entities_Feature_name: Property = Property(name="name", type=StringType)
entities_Feature_many: Property = Property(name="many", type=BooleanType)
entities_Feature.attributes={entities_Feature_many, entities_Feature_name}

# entities_DomainModel class attributes and methods

# entities_Entity class attributes and methods
entities_Entity_name: Property = Property(name="name", type=StringType)
entities_Entity.attributes={entities_Entity_name}

# Relationships
superType2: BinaryAssociation = BinaryAssociation(
    name="superType2",
    ends={
        Property(name="entities_Entity3", type=entities_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="entities_Entity1", type=entities_Entity, multiplicity=Multiplicity(0, 1))
    }
)
features4: BinaryAssociation = BinaryAssociation(
    name="features4",
    ends={
        Property(name="entities_Feature", type=entities_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="entities_Entity5", type=entities_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type6: BinaryAssociation = BinaryAssociation(
    name="type6",
    ends={
        Property(name="entities_Entity8", type=entities_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="entities_Feature7", type=entities_Entity, multiplicity=Multiplicity(0, 1))
    }
)
entities0: BinaryAssociation = BinaryAssociation(
    name="entities0",
    ends={
        Property(name="entities_Entity", type=entities_DomainModel, multiplicity=Multiplicity(1, 1)),
        Property(name="entities_DomainModel", type=entities_Entity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="entities",
    types={entities_Feature, entities_DomainModel, entities_Entity},
    associations={superType2, features4, type6, entities0},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)