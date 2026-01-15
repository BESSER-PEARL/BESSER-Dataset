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
basic2_World = Class(name="basic2::World")
basic2_Thing = Class(name="basic2::Thing")

# basic2_World class attributes and methods

# basic2_Thing class attributes and methods
basic2_Thing_id: Property = Property(name="id", type=IntegerType)
basic2_Thing.attributes={basic2_Thing_id}

# Relationships
things0: BinaryAssociation = BinaryAssociation(
    name="things0",
    ends={
        Property(name="basic2_Thing", type=basic2_World, multiplicity=Multiplicity(1, 1)),
        Property(name="basic2_World", type=basic2_Thing, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
things2: BinaryAssociation = BinaryAssociation(
    name="things2",
    ends={
        Property(name="basic2_Thing3", type=basic2_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="basic2_Thing1", type=basic2_Thing, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="basic2",
    types={basic2_World, basic2_Thing},
    associations={things0, things2},
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