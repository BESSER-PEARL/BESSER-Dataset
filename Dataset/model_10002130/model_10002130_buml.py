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
Home = Class(name="Home")
Locatable = Class(name="Locatable")
Post = Class(name="Post")
Group = Class(name="Group")
Message = Class(name="Message")
Friend = Class(name="Friend")
Login = Class(name="Login")
Locatable_Interface = Class(name="Locatable_Interface")

# Home class attributes and methods

# Locatable class attributes and methods

# Post class attributes and methods

# Group class attributes and methods

# Message class attributes and methods

# Friend class attributes and methods

# Login class attributes and methods

# Locatable_Interface class attributes and methods

# Relationships
User_Myprofile: BinaryAssociation = BinaryAssociation(
    name="User_Myprofile",
    ends={
        Property(name="myprofile0", type=Locatable, multiplicity=Multiplicity(1, 1)),
        Property(name="user1", type=Home, multiplicity=Multiplicity(1, 1))
    }
)
User_Post: BinaryAssociation = BinaryAssociation(
    name="User_Post",
    ends={
        Property(name="post2", type=Post, multiplicity=Multiplicity(0, 9999)),
        Property(name="user3", type=Home, multiplicity=Multiplicity(1, 1))
    }
)
User_Login: BinaryAssociation = BinaryAssociation(
    name="User_Login",
    ends={
        Property(name="login4", type=Login, multiplicity=Multiplicity(1, 1)),
        Property(name="user5", type=Home, multiplicity=Multiplicity(1, 1))
    }
)
User_Group: BinaryAssociation = BinaryAssociation(
    name="User_Group",
    ends={
        Property(name="group6", type=Group, multiplicity=Multiplicity(0, 9999)),
        Property(name="user7", type=Home, multiplicity=Multiplicity(1, 1))
    }
)
User_Message: BinaryAssociation = BinaryAssociation(
    name="User_Message",
    ends={
        Property(name="message8", type=Message, multiplicity=Multiplicity(0, 9999)),
        Property(name="user9", type=Home, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_qXGiIHnLEeqeQcxm9hmzHw",
    types={Home, Locatable, Post, Group, Message, Friend, Login, Locatable_Interface},
    associations={User_Myprofile, User_Post, User_Login, User_Group, User_Message},
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