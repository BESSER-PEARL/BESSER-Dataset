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
Others = Class(name="Others")
public = Class(name="public")
secret = Class(name="secret")
Registration = Class(name="Registration")
Login = Class(name="Login")

# User class attributes and methods
User_name: Property = Property(name="name", type=StringType)
User.attributes={User_name}

# Profile class attributes and methods
Profile_username: Property = Property(name="username", type=StringType)
Profile_password: Property = Property(name="password", type=StringType)
Profile_about: Property = Property(name="about", type=StringType)
Profile.attributes={Profile_about, Profile_password, Profile_username}

# Post class attributes and methods
Post_privacy: Property = Property(name="privacy", type=StringType)
Post_info: Property = Property(name="info", type=StringType)
Post.attributes={Post_privacy, Post_info}

# Others class attributes and methods
Others_name: Property = Property(name="name", type=StringType)
Others_discription: Property = Property(name="discription", type=StringType)
Others.attributes={Others_name, Others_discription}

# public class attributes and methods
public_name: Property = Property(name="name", type=StringType)
public.attributes={public_name}

# secret class attributes and methods
secret_name: Property = Property(name="name", type=StringType)
secret.attributes={secret_name}

# Registration class attributes and methods
Registration_fname: Property = Property(name="fname", type=StringType)
Registration_lname: Property = Property(name="lname", type=StringType)
Registration_password: Property = Property(name="password", type=secret)
Registration_userName: Property = Property(name="userName", type=StringType)
Registration.attributes={Registration_userName, Registration_password, Registration_lname, Registration_fname}

# Login class attributes and methods
Login_username: Property = Property(name="username", type=StringType)
Login_password: Property = Property(name="password", type=StringType)
Login.attributes={Login_password, Login_username}

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
User_Group: BinaryAssociation = BinaryAssociation(
    name="User_Group",
    ends={
        Property(name="group4", type=Others, multiplicity=Multiplicity(0, 9999)),
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

# Domain Model
domain_model = DomainModel(
    name="_kpN0UIoIEeq3N_Xh6gsEIQ",
    types={User, Profile, Post, Others, public, secret, Registration, Login},
    associations={User_Myprofile, User_Post, User_Group, User_Registeration},
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