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
User = Class(name="User")
Club = Class(name="Club")
Post = Class(name="Post")
Login = Class(name="Login")
Search = Class(name="Search")
reply = Class(name="reply")

# Actor_Actor class attributes and methods

# User class attributes and methods

# Club class attributes and methods

# Post class attributes and methods

# Login class attributes and methods

# Search class attributes and methods

# reply class attributes and methods

# Domain Model
domain_model = DomainModel(
    name="_LD5PQAG5EeqF_c9bu8KhDg",
    types={Actor_Actor, User, Club, Post, Login, Search, reply},
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