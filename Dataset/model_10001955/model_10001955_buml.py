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
Actor_Actor = Class(name="Actor_Actor")
User_Actor = Class(name="User_Actor")
Routing_System_Actor = Class(name="Routing_System_Actor")
Class_ = Class(name="Class")
Route = Class(name="Route")

# Actor_Actor class attributes and methods

# User_Actor class attributes and methods

# Routing_System_Actor class attributes and methods

# Class class attributes and methods

# Route class attributes and methods

# Domain Model
domain_model = DomainModel(
    name="_fbiFUJCOEeeaCsv2qBF4QA",
    types={Actor_Actor, User_Actor, Routing_System_Actor, Class_, Route},
    associations={},
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