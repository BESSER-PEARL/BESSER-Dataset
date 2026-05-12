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
User = Class(name="User")
Profile = Class(name="Profile")
Post = Class(name="Post")
Topic = Class(name="Topic")
Comment = Class(name="Comment")
Login = Class(name="Login")

# User class attributes and methods

# Profile class attributes and methods

# Post class attributes and methods

# Topic class attributes and methods

# Comment class attributes and methods

# Login class attributes and methods

# Relationships
User_Myprofile: BinaryAssociation = BinaryAssociation(
    name="User_Myprofile",
    ends={
        Property(name="myprofile0", type=Profile, multiplicity=Multiplicity(1, 1)),
        Property(name="user1", type=User, multiplicity=Multiplicity(1, 1))
    }
)
User_Post: BinaryAssociation = BinaryAssociation(
    name="User_Post",
    ends={
        Property(name="post2", type=Post, multiplicity=Multiplicity(0, 9999)),
        Property(name="user3", type=User, multiplicity=Multiplicity(1, 1))
    }
)
User_Login: BinaryAssociation = BinaryAssociation(
    name="User_Login",
    ends={
        Property(name="login4", type=Login, multiplicity=Multiplicity(1, 1)),
        Property(name="user5", type=User, multiplicity=Multiplicity(1, 1))
    }
)
User_Group: BinaryAssociation = BinaryAssociation(
    name="User_Group",
    ends={
        Property(name="group6", type=Topic, multiplicity=Multiplicity(0, 9999)),
        Property(name="user7", type=User, multiplicity=Multiplicity(1, 1))
    }
)
User_Message: BinaryAssociation = BinaryAssociation(
    name="User_Message",
    ends={
        Property(name="message8", type=Comment, multiplicity=Multiplicity(0, 9999)),
        Property(name="user9", type=User, multiplicity=Multiplicity(1, 1))
    }
)
Topic_Message: BinaryAssociation = BinaryAssociation(
    name="Topic_Message",
    ends={
        Property(name="Topic_Message_010", type=Comment, multiplicity=Multiplicity(0, 9999)),
        Property(name="Topic_Message_111", type=Topic, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_788d37da_d0eb_4ab8_9bea_d9977d37a41d",
    types={User, Profile, Post, Topic, Comment, Login},
    associations={User_Myprofile, User_Post, User_Login, User_Group, User_Message, Topic_Message},
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