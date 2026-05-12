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
Interest = Class(name="Interest")
Notification = Class(name="Notification")
Event = Class(name="Event")
Registration = Class(name="Registration")
Login = Class(name="Login")

# User class attributes and methods
User_fname: Property = Property(name="fname", type=StringType)
User_lname: Property = Property(name="lname", type=StringType)
User_username: Property = Property(name="username", type=StringType)
User.attributes={User_username, User_fname, User_lname}

# Profile class attributes and methods
Profile_username: Property = Property(name="username", type=StringType)
Profile_password: Property = Property(name="password", type=StringType)
Profile_interests: Property = Property(name="interests", type=StringType)
Profile.attributes={Profile_interests, Profile_username, Profile_password}

# Post class attributes and methods
Post_info: Property = Property(name="info", type=StringType)
Post.attributes={Post_info}

# Interest class attributes and methods
Interest_name: Property = Property(name="name", type=StringType)
Interest_discription: Property = Property(name="discription", type=StringType)
Interest.attributes={Interest_discription, Interest_name}

# Notification class attributes and methods
Notification_update: Property = Property(name="update", type=StringType)
Notification.attributes={Notification_update}

# Event class attributes and methods
Event_name: Property = Property(name="name", type=StringType)
Event_location: Property = Property(name="location", type=StringType)
Event_time: Property = Property(name="time", type=StringType)
Event.attributes={Event_location, Event_name, Event_time}

# Registration class attributes and methods
Registration_password: Property = Property(name="password", type=StringType)
Registration_fname: Property = Property(name="fname", type=StringType)
Registration_userName: Property = Property(name="userName", type=StringType)
Registration_lname: Property = Property(name="lname", type=StringType)
Registration.attributes={Registration_fname, Registration_password, Registration_lname, Registration_userName}

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
User_Login: BinaryAssociation = BinaryAssociation(
    name="User_Login",
    ends={
        Property(name="login2", type=Login, multiplicity=Multiplicity(1, 1)),
        Property(name="user3", type=User, multiplicity=Multiplicity(1, 1))
    }
)
User_Group: BinaryAssociation = BinaryAssociation(
    name="User_Group",
    ends={
        Property(name="group4", type=Interest, multiplicity=Multiplicity(0, 9999)),
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
        Property(name="message8", type=Event, multiplicity=Multiplicity(0, 9999)),
        Property(name="user9", type=User, multiplicity=Multiplicity(1, 1))
    }
)
User_Friends: BinaryAssociation = BinaryAssociation(
    name="User_Friends",
    ends={
        Property(name="friends10", type=Notification, multiplicity=Multiplicity(0, 9999)),
        Property(name="user11", type=User, multiplicity=Multiplicity(1, 1))
    }
)
User_Pages: BinaryAssociation = BinaryAssociation(
    name="User_Pages",
    ends={
        Property(name="pages12", type=Post, multiplicity=Multiplicity(0, 9999)),
        Property(name="user13", type=Interest, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="__xgYMPppEemPd5ZtCQMxVQ",
    types={User, Profile, Post, Interest, Notification, Event, Registration, Login},
    associations={User_Myprofile, User_Login, User_Group, User_Registeration, User_Message, User_Friends, User_Pages},
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