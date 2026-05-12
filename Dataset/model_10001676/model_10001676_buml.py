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
Friend = Class(name="Friend")
Hashtag = Class(name="Hashtag")
Page = Class(name="Page")
Sign_Up = Class(name="Sign_Up")
Login = Class(name="Login")
User = Class(name="User")
Profile = Class(name="Profile")
Post = Class(name="Post")
Group = Class(name="Group")
public = Class(name="public")
secret = Class(name="secret")
Message = Class(name="Message")

# Friend class attributes and methods

# Hashtag class attributes and methods
Hashtag_name: Property = Property(name="name", type=StringType)
Hashtag_numOfRepeat: Property = Property(name="numOfRepeat", type=IntegerType)
Hashtag.attributes={Hashtag_name, Hashtag_numOfRepeat}

# Page class attributes and methods
Page_name: Property = Property(name="name", type=StringType)
Page.attributes={Page_name}

# Sign_Up class attributes and methods
Sign_Up_fname: Property = Property(name="fname", type=StringType)
Sign_Up_lname: Property = Property(name="lname", type=StringType)
Sign_Up_password: Property = Property(name="password", type=secret)
Sign_Up_userName: Property = Property(name="userName", type=StringType)
Sign_Up.attributes={Sign_Up_lname, Sign_Up_userName, Sign_Up_password, Sign_Up_fname}

# Login class attributes and methods
Login_username: Property = Property(name="username", type=StringType)
Login_password: Property = Property(name="password", type=StringType)
Login.attributes={Login_username, Login_password}

# User class attributes and methods
User_name: Property = Property(name="name", type=StringType)
User.attributes={User_name}

# Profile class attributes and methods
Profile_username: Property = Property(name="username", type=StringType)
Profile_password: Property = Property(name="password", type=StringType)
Profile.attributes={Profile_username, Profile_password}

# Post class attributes and methods
Post_privacy: Property = Property(name="privacy", type=StringType)
Post_info: Property = Property(name="info", type=StringType)
Post.attributes={Post_privacy, Post_info}

# Group class attributes and methods
Group_name: Property = Property(name="name", type=StringType)
Group_discription: Property = Property(name="discription", type=StringType)
Group.attributes={Group_discription, Group_name}

# public class attributes and methods
public_name: Property = Property(name="name", type=StringType)
public.attributes={public_name}

# secret class attributes and methods
secret_name: Property = Property(name="name", type=StringType)
secret.attributes={secret_name}

# Message class attributes and methods
Message_maxChars: Property = Property(name="maxChars", type=StringType)
Message.attributes={Message_maxChars}

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
        Property(name="group6", type=Group, multiplicity=Multiplicity(0, 9999)),
        Property(name="user7", type=User, multiplicity=Multiplicity(1, 1))
    }
)
User_Registeration: BinaryAssociation = BinaryAssociation(
    name="User_Registeration",
    ends={
        Property(name="registeration8", type=Sign_Up, multiplicity=Multiplicity(1, 1)),
        Property(name="user9", type=User, multiplicity=Multiplicity(1, 1))
    }
)
User_Message: BinaryAssociation = BinaryAssociation(
    name="User_Message",
    ends={
        Property(name="message10", type=Message, multiplicity=Multiplicity(0, 9999)),
        Property(name="user11", type=User, multiplicity=Multiplicity(1, 1))
    }
)
User_Friends: BinaryAssociation = BinaryAssociation(
    name="User_Friends",
    ends={
        Property(name="friends12", type=Friend, multiplicity=Multiplicity(0, 9999)),
        Property(name="user13", type=User, multiplicity=Multiplicity(1, 1))
    }
)
User_Hashtag: BinaryAssociation = BinaryAssociation(
    name="User_Hashtag",
    ends={
        Property(name="hashtag14", type=Hashtag, multiplicity=Multiplicity(0, 9999)),
        Property(name="user15", type=User, multiplicity=Multiplicity(1, 1))
    }
)
User_Pages: BinaryAssociation = BinaryAssociation(
    name="User_Pages",
    ends={
        Property(name="pages16", type=Page, multiplicity=Multiplicity(0, 9999)),
        Property(name="user17", type=User, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_OGAaUAcoEeqFfO0RhT_ZfA",
    types={Friend, Hashtag, Page, Sign_Up, Login, User, Profile, Post, Group, public, secret, Message},
    associations={User_Myprofile, User_Post, User_Login, User_Group, User_Registeration, User_Message, User_Friends, User_Hashtag, User_Pages},
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