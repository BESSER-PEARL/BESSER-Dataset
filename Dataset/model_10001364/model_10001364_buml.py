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
public = Class(name="public")
secret = Class(name="secret")
Message = Class(name="Message")
Friend = Class(name="Friend")
Registration = Class(name="Registration")
Login = Class(name="Login")

# User class attributes and methods
User_name: Property = Property(name="name", type=StringType)
User.attributes={User_name}

# Profile class attributes and methods
Profile_username: Property = Property(name="username", type=StringType)
Profile_password: Property = Property(name="password", type=StringType)
Profile_photo: Property = Property(name="photo", type=StringType)
Profile.attributes={Profile_username, Profile_photo, Profile_password}

# Post class attributes and methods
Post_info: Property = Property(name="info", type=StringType)
Post_likes: Property = Property(name="likes", type=IntegerType)
Post.attributes={Post_likes, Post_info}

# public class attributes and methods
public_name: Property = Property(name="name", type=StringType)
public.attributes={public_name}

# secret class attributes and methods
secret_name: Property = Property(name="name", type=StringType)
secret.attributes={secret_name}

# Message class attributes and methods
Message_maxChars: Property = Property(name="maxChars", type=StringType)
Message.attributes={Message_maxChars}

# Friend class attributes and methods

# Registration class attributes and methods
Registration_name: Property = Property(name="name", type=StringType)
Registration_password: Property = Property(name="password", type=secret)
Registration_email: Property = Property(name="email", type=StringType)
Registration.attributes={Registration_name, Registration_password, Registration_email}

# Login class attributes and methods
Login_email: Property = Property(name="email", type=StringType)
Login_password: Property = Property(name="password", type=StringType)
Login.attributes={Login_password, Login_email}

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
User_Friends: BinaryAssociation = BinaryAssociation(
    name="User_Friends",
    ends={
        Property(name="friends10", type=Friend, multiplicity=Multiplicity(0, 9999)),
        Property(name="user11", type=User, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_2VJfsBFYEeqDmNBP3mfLQg",
    types={User, Profile, Post, public, secret, Message, Friend, Registration, Login},
    associations={User_Myprofile, User_Post, User_Login, User_Registeration, User_Message, User_Friends},
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