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
Profile = Class(name="Profile")
User = Class(name="User")
Post = Class(name="Post")
Group = Class(name="Group")
Message = Class(name="Message")
Page = Class(name="Page")

# Profile class attributes and methods
Profile_About: Property = Property(name="About", type=StringType)
Profile_ID_Profile: Property = Property(name="ID_Profile", type=StringType)
Profile_User_Name: Property = Property(name="User_Name", type=StringType)
Profile_Password: Property = Property(name="Password", type=StringType)
Profile.attributes={Profile_ID_Profile, Profile_Password, Profile_About, Profile_User_Name}

# User class attributes and methods
User_ID_User: Property = Property(name="ID_User", type=IntegerType)
User_Name: Property = Property(name="Name", type=StringType)
User_Fist_Name: Property = Property(name="Fist_Name", type=StringType)
User_Mail: Property = Property(name="Mail", type=StringType)
User.attributes={User_Mail, User_ID_User, User_Name, User_Fist_Name}

# Post class attributes and methods
Post_ID_Post: Property = Property(name="ID_Post", type=IntegerType)
Post_Privacy: Property = Property(name="Privacy", type=StringType)
Post_Info: Property = Property(name="Info", type=StringType)
Post_Mail: Property = Property(name="Mail", type=StringType)
Post_ID_Page: Property = Property(name="ID_Page", type=IntegerType)
Post.attributes={Post_Privacy, Post_Info, Post_ID_Page, Post_ID_Post, Post_Mail}

# Group class attributes and methods
Group_ID_Group: Property = Property(name="ID_Group", type=IntegerType)
Group_Name: Property = Property(name="Name", type=StringType)
Group_Description: Property = Property(name="Description", type=StringType)
Group_ID_User: Property = Property(name="ID_User", type=IntegerType)
Group.attributes={Group_Name, Group_Description, Group_ID_Group, Group_ID_User}

# Message class attributes and methods
Message_ID_Message: Property = Property(name="ID_Message", type=IntegerType)
Message_Max_Chars: Property = Property(name="Max_Chars", type=StringType)
Message_Mail: Property = Property(name="Mail", type=StringType)
Message_ID_User: Property = Property(name="ID_User", type=IntegerType)
Message.attributes={Message_Max_Chars, Message_ID_User, Message_Mail, Message_ID_Message}

# Page class attributes and methods
Page_ID_Page: Property = Property(name="ID_Page", type=IntegerType)
Page_Name: Property = Property(name="Name", type=StringType)
Page_Description: Property = Property(name="Description", type=StringType)
Page_ID_User: Property = Property(name="ID_User", type=IntegerType)
Page.attributes={Page_Name, Page_ID_User, Page_Description, Page_ID_Page}

# Relationships
Profile_User: BinaryAssociation = BinaryAssociation(
    name="Profile_User",
    ends={
        Property(name="user0", type=User, multiplicity=Multiplicity(1, 1)),
        Property(name="profile1", type=Profile, multiplicity=Multiplicity(1, 1))
    }
)
User_Page: BinaryAssociation = BinaryAssociation(
    name="User_Page",
    ends={
        Property(name="page2", type=Page, multiplicity=Multiplicity(0, 9999)),
        Property(name="user3", type=User, multiplicity=Multiplicity(1, 1))
    }
)
User_Message: BinaryAssociation = BinaryAssociation(
    name="User_Message",
    ends={
        Property(name="message4", type=Message, multiplicity=Multiplicity(0, 9999)),
        Property(name="user5", type=User, multiplicity=Multiplicity(1, 1))
    }
)
User_Group: BinaryAssociation = BinaryAssociation(
    name="User_Group",
    ends={
        Property(name="group6", type=Group, multiplicity=Multiplicity(0, 9999)),
        Property(name="user7", type=User, multiplicity=Multiplicity(1, 1))
    }
)
Page_Post: BinaryAssociation = BinaryAssociation(
    name="Page_Post",
    ends={
        Property(name="post8", type=Post, multiplicity=Multiplicity(0, 9999)),
        Property(name="page9", type=Page, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_fYTTwLejEem8I_zdXKdSGw",
    types={Profile, User, Post, Group, Message, Page},
    associations={Profile_User, User_Page, User_Message, User_Group, Page_Post},
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