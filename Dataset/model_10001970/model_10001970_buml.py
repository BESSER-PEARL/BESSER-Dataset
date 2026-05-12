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
Message = Class(name="Message")
Share = Class(name="Share")
Post = Class(name="Post")
Group = Class(name="Group")
Page = Class(name="Page")
Comment = Class(name="Comment")
Hashtag = Class(name="Hashtag")
Inbox = Class(name="Inbox")

# User class attributes and methods

# Message class attributes and methods

# Share class attributes and methods

# Post class attributes and methods

# Group class attributes and methods

# Page class attributes and methods

# Comment class attributes and methods

# Hashtag class attributes and methods

# Inbox class attributes and methods

# Relationships
Post_User: BinaryAssociation = BinaryAssociation(
    name="Post_User",
    ends={
        Property(name="user0", type=User, multiplicity=Multiplicity(0, 1)),
        Property(name="post1", type=Post, multiplicity=Multiplicity(0, 9999))
    }
)
User_Message: BinaryAssociation = BinaryAssociation(
    name="User_Message",
    ends={
        Property(name="message2", type=Message, multiplicity=Multiplicity(0, 9999)),
        Property(name="user3", type=User, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_gqAh0OaJEeeGy5tFxte9Vg",
    types={User, Message, Share, Post, Group, Page, Comment, Hashtag, Inbox},
    associations={Post_User, User_Message},
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