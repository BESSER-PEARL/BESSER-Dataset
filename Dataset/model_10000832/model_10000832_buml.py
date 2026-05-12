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
ApplicationController = Class(name="ApplicationController")
CredentialsAuthController = Class(name="CredentialsAuthController")
CredentialsProvider = Class(name="CredentialsProvider")
UserService = Class(name="UserService")
Environment_User__CookieAuthenticator_ = Class(name="Environment_User__CookieAuthenticator_")
PrescriberController = Class(name="PrescriberController")
Class_ = Class(name="Class")

# Actor_Actor class attributes and methods

# ApplicationController class attributes and methods

# CredentialsAuthController class attributes and methods

# CredentialsProvider class attributes and methods

# UserService class attributes and methods

# Environment_User__CookieAuthenticator_ class attributes and methods

# PrescriberController class attributes and methods

# Class class attributes and methods

# Domain Model
domain_model = DomainModel(
    name="_65e8704b_c21d_4c2f_b771_dd7d455d34dd",
    types={Actor_Actor, ApplicationController, CredentialsAuthController, CredentialsProvider, UserService, Environment_User__CookieAuthenticator_, PrescriberController, Class_},
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