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

# Actor_Actor class attributes and methods

# ApplicationController class attributes and methods

# CredentialsAuthController class attributes and methods

# CredentialsProvider class attributes and methods

# UserService class attributes and methods

# Environment_User__CookieAuthenticator_ class attributes and methods

# PrescriberController class attributes and methods

# Domain Model
domain_model = DomainModel(
    name="_114a3966_e7c5_411d_8b77_bec5cc647bb9",
    types={Actor_Actor, ApplicationController, CredentialsAuthController, CredentialsProvider, UserService, Environment_User__CookieAuthenticator_, PrescriberController},
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