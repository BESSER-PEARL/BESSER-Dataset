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
helloworld_World = Class(name="helloworld::World")
helloworld_Thing = Class(name="helloworld::Thing")

# helloworld_World class attributes and methods

# helloworld_Thing class attributes and methods
helloworld_Thing_name: Property = Property(name="name", type=StringType)
helloworld_Thing.attributes={helloworld_Thing_name}

# Relationships
things0: BinaryAssociation = BinaryAssociation(
    name="things0",
    ends={
        Property(name="helloworld_Thing", type=helloworld_World, multiplicity=Multiplicity(1, 1)),
        Property(name="helloworld_World", type=helloworld_Thing, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relations5: BinaryAssociation = BinaryAssociation(
    name="relations5",
    ends={
        Property(name="helloworld_Thing4", type=helloworld_Thing, multiplicity=Multiplicity(0, 9999)),
        Property(name="helloworld_Thing6", type=helloworld_Thing, multiplicity=Multiplicity(1, 1))
    }
)
things2: BinaryAssociation = BinaryAssociation(
    name="things2",
    ends={
        Property(name="helloworld_Thing3", type=helloworld_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="helloworld_Thing1", type=helloworld_Thing, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="helloworld",
    types={helloworld_World, helloworld_Thing},
    associations={things0, relations5, things2},
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