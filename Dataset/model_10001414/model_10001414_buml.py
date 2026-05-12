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
Search = Class(name="Search")
user_Actor = Class(name="user_Actor")
Actor1_Actor = Class(name="Actor1_Actor")
Actor_Actor = Class(name="Actor_Actor")
club = Class(name="club")
post = Class(name="post")

# Search class attributes and methods

# user_Actor class attributes and methods

# Actor1_Actor class attributes and methods

# Actor_Actor class attributes and methods

# club class attributes and methods

# post class attributes and methods

# Domain Model
domain_model = DomainModel(
    name="_5TWsQAD8EeqF_c9bu8KhDg",
    types={Search, user_Actor, Actor1_Actor, Actor_Actor, club, post},
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