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
Message = Class(name="Message")
Hashtag = Class(name="Hashtag")
Page = Class(name="Page")
Registration = Class(name="Registration")
Login = Class(name="Login")

# User class attributes and methods
User_name: Property = Property(name="name", type=StringType)
User.attributes={User_name}

# Profile class attributes and methods
Profile_username: Property = Property(name="username", type=StringType)
Profile_password: Property = Property(name="password", type=StringType)
Profile.attributes={Profile_password, Profile_username}

# Post class attributes and methods
Post_privacy: Property = Property(name="privacy", type=StringType)
Post_info: Property = Property(name="info", type=StringType)
Post.attributes={Post_privacy, Post_info}

# Message class attributes and methods
Message_maxChars: Property = Property(name="maxChars", type=StringType)
Message.attributes={Message_maxChars}

# Hashtag class attributes and methods
Hashtag_name: Property = Property(name="name", type=StringType)
Hashtag_numOfRepeat: Property = Property(name="numOfRepeat", type=IntegerType)
Hashtag.attributes={Hashtag_name, Hashtag_numOfRepeat}

# Page class attributes and methods
Page_name: Property = Property(name="name", type=StringType)
Page.attributes={Page_name}

# Registration class attributes and methods
Registration_fullname: Property = Property(name="fullname", type=StringType)
Registration_password: Property = Property(name="password", type=StringType)
Registration_userName: Property = Property(name="userName", type=StringType)
Registration.attributes={Registration_userName, Registration_fullname, Registration_password}

# Login class attributes and methods
Login_username: Property = Property(name="username", type=StringType)
Login_password: Property = Property(name="password", type=StringType)
Login.attributes={Login_username, Login_password}

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
User_Registeration: BinaryAssociation = BinaryAssociation(
    name="User_Registeration",
    ends={
        Property(name="registeration6", type=Registration, multiplicity=Multiplicity(1, 1)),
        Property(name="user7", type=User, multiplicity=Multiplicity(1, 1))
    }
)
User_Message: BinaryAssociation = BinaryAssociation(
    name="User_Message",
    ends={
        Property(name="message8", type=Message, multiplicity=Multiplicity(0, 9999)),
        Property(name="user9", type=User, multiplicity=Multiplicity(1, 1))
    }
)
User_Hashtag: BinaryAssociation = BinaryAssociation(
    name="User_Hashtag",
    ends={
        Property(name="hashtag10", type=Hashtag, multiplicity=Multiplicity(0, 9999)),
        Property(name="user11", type=User, multiplicity=Multiplicity(1, 1))
    }
)
User_Pages: BinaryAssociation = BinaryAssociation(
    name="User_Pages",
    ends={
        Property(name="pages12", type=Page, multiplicity=Multiplicity(0, 9999)),
        Property(name="user13", type=User, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_oOWNMGSTEeqK2M3E1LfZ7Q",
    types={User, Profile, Post, Message, Hashtag, Page, Registration, Login},
    associations={User_Myprofile, User_Post, User_Login, User_Registeration, User_Message, User_Hashtag, User_Pages},
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