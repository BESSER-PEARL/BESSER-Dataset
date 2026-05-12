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
Group = Class(name="Group")
Secret = Class(name="Secret")
Public = Class(name="Public")
Login = Class(name="Login")
Registration = Class(name="Registration")
Post = Class(name="Post")
Profile = Class(name="Profile")
Team_Timeline = Class(name="Team_Timeline")
Chat = Class(name="Chat")
Friend = Class(name="Friend")
Media = Class(name="Media")
Review = Class(name="Review")

# User class attributes and methods
User_Name: Property = Property(name="Name", type=StringType)
User.attributes={User_Name}

# Group class attributes and methods
Group_Name: Property = Property(name="Name", type=StringType)
Group_Description: Property = Property(name="Description", type=StringType)
Group.attributes={Group_Description, Group_Name}

# Secret class attributes and methods
Secret_Name: Property = Property(name="Name", type=StringType)
Secret.attributes={Secret_Name}

# Public class attributes and methods
Public_Name: Property = Property(name="Name", type=StringType)
Public.attributes={Public_Name}

# Login class attributes and methods
Login_Username: Property = Property(name="Username", type=StringType)
Login_Password: Property = Property(name="Password", type=StringType)
Login.attributes={Login_Password, Login_Username}

# Registration class attributes and methods
Registration_Password: Property = Property(name="Password", type=Secret)
Registration_Username: Property = Property(name="Username", type=StringType)
Registration.attributes={Registration_Username, Registration_Password}

# Post class attributes and methods
Post_PostContent: Property = Property(name="PostContent", type=StringType)
Post.attributes={Post_PostContent}

# Profile class attributes and methods
Profile_Username: Property = Property(name="Username", type=StringType)
Profile_Password: Property = Property(name="Password", type=StringType)
Profile_About: Property = Property(name="About", type=StringType)
Profile.attributes={Profile_Password, Profile_About, Profile_Username}

# Team_Timeline class attributes and methods
Team_Timeline_Name: Property = Property(name="Name", type=StringType)
Team_Timeline.attributes={Team_Timeline_Name}

# Chat class attributes and methods

# Friend class attributes and methods

# Media class attributes and methods
Media_MediaPath: Property = Property(name="MediaPath", type=StringType)
Media.attributes={Media_MediaPath}

# Review class attributes and methods
Review_PostContent: Property = Property(name="PostContent", type=StringType)
Review.attributes={Review_PostContent}

# Relationships
Login_User: BinaryAssociation = BinaryAssociation(
    name="Login_User",
    ends={
        Property(name="Login_User_04", type=User, multiplicity=Multiplicity(1, 1)),
        Property(name="Login_User_15", type=Login, multiplicity=Multiplicity(1, 1))
    }
)
User_Post: BinaryAssociation = BinaryAssociation(
    name="User_Post",
    ends={
        Property(name="User_Post_06", type=Post, multiplicity=Multiplicity(0, 9999)),
        Property(name="User_Post_17", type=User, multiplicity=Multiplicity(1, 1))
    }
)
User_Profile: BinaryAssociation = BinaryAssociation(
    name="User_Profile",
    ends={
        Property(name="User_Profile_08", type=Profile, multiplicity=Multiplicity(1, 1)),
        Property(name="User_Profile_19", type=User, multiplicity=Multiplicity(1, 1))
    }
)
User_Friend: BinaryAssociation = BinaryAssociation(
    name="User_Friend",
    ends={
        Property(name="friend10", type=Friend, multiplicity=Multiplicity(0, 9999)),
        Property(name="User_Friend_111", type=User, multiplicity=Multiplicity(1, 1))
    }
)
User_Chat: BinaryAssociation = BinaryAssociation(
    name="User_Chat",
    ends={
        Property(name="User_Chat_012", type=Chat, multiplicity=Multiplicity(0, 9999)),
        Property(name="User_Chat_113", type=User, multiplicity=Multiplicity(1, 1))
    }
)
User_Timeline: BinaryAssociation = BinaryAssociation(
    name="User_Timeline",
    ends={
        Property(name="timeline14", type=Team_Timeline, multiplicity=Multiplicity(1, 1)),
        Property(name="User_Timeline_115", type=User, multiplicity=Multiplicity(1, 1))
    }
)
Post_ImagePost: BinaryAssociation = BinaryAssociation(
    name="Post_ImagePost",
    ends={
        Property(name="Post_ImagePost_016", type=Media, multiplicity=Multiplicity(0, 9999)),
        Property(name="Post_ImagePost_117", type=Post, multiplicity=Multiplicity(1, 1))
    }
)
Review_User: BinaryAssociation = BinaryAssociation(
    name="Review_User",
    ends={
        Property(name="Review_User_018", type=User, multiplicity=Multiplicity(1, 1)),
        Property(name="Review_User_119", type=Review, multiplicity=Multiplicity(1, 1))
    }
)
User_Group: BinaryAssociation = BinaryAssociation(
    name="User_Group",
    ends={
        Property(name="User_Group_00", type=Group, multiplicity=Multiplicity(0, 9999)),
        Property(name="User_Group_11", type=User, multiplicity=Multiplicity(1, 1))
    }
)
Registration_User: BinaryAssociation = BinaryAssociation(
    name="Registration_User",
    ends={
        Property(name="Registration_User_02", type=User, multiplicity=Multiplicity(1, 1)),
        Property(name="Registration_User_13", type=Registration, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="c3fb2bf0_3a4d_43b3_ac4d_bb9d9fc25929",
    types={User, Group, Secret, Public, Login, Registration, Post, Profile, Team_Timeline, Chat, Friend, Media, Review},
    associations={Login_User, User_Post, User_Profile, User_Friend, User_Chat, User_Timeline, Post_ImagePost, Review_User, User_Group, Registration_User},
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