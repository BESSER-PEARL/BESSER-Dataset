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
Comment = Class(name="Comment")
Hashtag = Class(name="Hashtag")
Registration = Class(name="Registration")
Login = Class(name="Login")
Item = Class(name="Item")
Search = Class(name="Search")
Class_ = Class(name="Class")

# User class attributes and methods
User_name: Property = Property(name="name", type=StringType)
User.attributes={User_name}

# Profile class attributes and methods
Profile_username: Property = Property(name="username", type=StringType)
Profile.attributes={Profile_username}

# Post class attributes and methods
Post_type: Property = Property(name="type", type=StringType)
Post.attributes={Post_type}

# Comment class attributes and methods

# Hashtag class attributes and methods
Hashtag_name: Property = Property(name="name", type=StringType)
Hashtag.attributes={Hashtag_name}

# Registration class attributes and methods
Registration_name: Property = Property(name="name", type=StringType)
Registration_username: Property = Property(name="username", type=StringType)
Registration_password: Property = Property(name="password", type=StringType)
Registration_userName: Property = Property(name="userName", type=StringType)
Registration.attributes={Registration_username, Registration_name, Registration_userName, Registration_password}

# Login class attributes and methods
Login_username: Property = Property(name="username", type=StringType)
Login_password: Property = Property(name="password", type=StringType)
Login.attributes={Login_username, Login_password}

# Item class attributes and methods

# Search class attributes and methods

# Class class attributes and methods

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
User_Friends: BinaryAssociation = BinaryAssociation(
    name="User_Friends",
    ends={
        Property(name="friends8", type=Comment, multiplicity=Multiplicity(0, 9999)),
        Property(name="user9", type=Item, multiplicity=Multiplicity(1, 1))
    }
)
User_Pages: BinaryAssociation = BinaryAssociation(
    name="User_Pages",
    ends={
        Property(name="pages10", type=Item, multiplicity=Multiplicity(0, 9999)),
        Property(name="user11", type=User, multiplicity=Multiplicity(1, 1))
    }
)
Item_Hashtag: BinaryAssociation = BinaryAssociation(
    name="Item_Hashtag",
    ends={
        Property(name="Item_Hashtag_012", type=Hashtag, multiplicity=Multiplicity(0, 9999)),
        Property(name="_113", type=Item, multiplicity=Multiplicity(0, 1))
    }
)
Item_Search: BinaryAssociation = BinaryAssociation(
    name="Item_Search",
    ends={
        Property(name="search14", type=Search, multiplicity=Multiplicity(0, 1)),
        Property(name="item15", type=Item, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_86a3cbeb_75a0_427a_9ad6_ec3b76bdaa1e",
    types={User, Profile, Post, Comment, Hashtag, Registration, Login, Item, Search, Class_},
    associations={User_Myprofile, User_Post, User_Login, User_Registeration, User_Friends, User_Pages, Item_Hashtag, Item_Search},
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