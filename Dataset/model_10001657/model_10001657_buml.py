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
Team = Class(name="Team")
User__ = Class(name="User__")
Post = Class(name="Post")
Page = Class(name="Page")
HashTags = Class(name="HashTags")
User2_Interface = Class(name="User2_Interface")

# User class attributes and methods
User_name: Property = Property(name="name", type=StringType)
User_username: Property = Property(name="username", type=StringType)
User_phone: Property = Property(name="phone", type=StringType)
User_password: Property = Property(name="password", type=StringType)
User_gender: Property = Property(name="gender", type=StringType)
User_pages: Property = Property(name="pages", type=StringType)
User_team: Property = Property(name="team", type=StringType)
User.attributes={User_pages, User_gender, User_phone, User_password, User_username, User_team, User_name}

# Team class attributes and methods
Team_name: Property = Property(name="name", type=StringType)
Team_description: Property = Property(name="description", type=StringType)
Team_admins: Property = Property(name="admins", type=User__)
Team_members: Property = Property(name="members", type=User__)
Team_nMembers: Property = Property(name="nMembers", type=IntegerType)
Team_posts: Property = Property(name="posts", type=StringType)
Team.attributes={Team_posts, Team_admins, Team_nMembers, Team_name, Team_members, Team_description}

# User__ class attributes and methods

# Post class attributes and methods
Post_privateMode: Property = Property(name="privateMode", type=BooleanType)
Post_nLikes: Property = Property(name="nLikes", type=IntegerType)
Post_nComments: Property = Property(name="nComments", type=IntegerType)
Post_nShares: Property = Property(name="nShares", type=IntegerType)
Post_owner: Property = Property(name="owner", type=User)
Post.attributes={Post_privateMode, Post_nShares, Post_owner, Post_nComments, Post_nLikes}

# Page class attributes and methods
Page_name: Property = Property(name="name", type=StringType)
Page_admin: Property = Property(name="admin", type=User)
Page_fans: Property = Property(name="fans", type=User__)
Page_description: Property = Property(name="description", type=StringType)
Page_posts: Property = Property(name="posts", type=StringType)
Page_nFans: Property = Property(name="nFans", type=IntegerType)
Page.attributes={Page_description, Page_name, Page_admin, Page_fans, Page_posts, Page_nFans}

# HashTags class attributes and methods
HashTags_allHashTags: Property = Property(name="allHashTags", type=StringType)
HashTags.attributes={HashTags_allHashTags}

# User2_Interface class attributes and methods

# Relationships
User_Group2: BinaryAssociation = BinaryAssociation(
    name="User_Group2",
    ends={
        Property(name="group0", type=Team, multiplicity=Multiplicity(1, 1)),
        Property(name="user1", type=User, multiplicity=Multiplicity(0, 9999))
    }
)
User_Page: BinaryAssociation = BinaryAssociation(
    name="User_Page",
    ends={
        Property(name="page2", type=Page, multiplicity=Multiplicity(1, 1)),
        Property(name="user3", type=User, multiplicity=Multiplicity(0, 9999))
    }
)
User_Post: BinaryAssociation = BinaryAssociation(
    name="User_Post",
    ends={
        Property(name="post4", type=Post, multiplicity=Multiplicity(1, 1)),
        Property(name="user5", type=User, multiplicity=Multiplicity(1, 1))
    }
)
Post_Group: BinaryAssociation = BinaryAssociation(
    name="Post_Group",
    ends={
        Property(name="group6", type=Team, multiplicity=Multiplicity(0, 1)),
        Property(name="post7", type=Post, multiplicity=Multiplicity(0, 1))
    }
)
Post_HashTags: BinaryAssociation = BinaryAssociation(
    name="Post_HashTags",
    ends={
        Property(name="hashTags8", type=HashTags, multiplicity=Multiplicity(0, 1)),
        Property(name="post9", type=Post, multiplicity=Multiplicity(0, 1))
    }
)
Post_Page: BinaryAssociation = BinaryAssociation(
    name="Post_Page",
    ends={
        Property(name="page10", type=Page, multiplicity=Multiplicity(0, 1)),
        Property(name="post11", type=Post, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_MeKvcHUpEeqHBZyMlFJVZw",
    types={User, Team, User__, Post, Page, HashTags, User2_Interface},
    associations={User_Group2, User_Page, User_Post, Post_Group, Post_HashTags, Post_Page},
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