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
complworld_Mars = Class(name="complworld::Mars")
complworld_Satellite = Class(name="complworld::Satellite")
complworld_World = Class(name="complworld::World")
complworld_Thing = Class(name="complworld::Thing")

# complworld_Mars class attributes and methods

# complworld_Satellite class attributes and methods
complworld_Satellite_name: Property = Property(name="name", type=StringType)
complworld_Satellite.attributes={complworld_Satellite_name}

# complworld_World class attributes and methods

# complworld_Thing class attributes and methods
complworld_Thing_name: Property = Property(name="name", type=StringType)
complworld_Thing.attributes={complworld_Thing_name}

# Relationships
satellites1: BinaryAssociation = BinaryAssociation(
    name="satellites1",
    ends={
        Property(name="complworld_Satellite", type=complworld_Mars, multiplicity=Multiplicity(1, 1)),
        Property(name="complworld_Mars", type=complworld_Satellite, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
things0: BinaryAssociation = BinaryAssociation(
    name="things0",
    ends={
        Property(name="complworld_Thing", type=complworld_World, multiplicity=Multiplicity(1, 1)),
        Property(name="complworld_World", type=complworld_Thing, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="complworld",
    types={complworld_Mars, complworld_Satellite, complworld_World, complworld_Thing},
    associations={satellites1, things0},
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