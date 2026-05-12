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
Rol = Class(name="Rol")
Post = Class(name="Post")
Comment = Class(name="Comment")
Vote = Class(name="Vote")
Message = Class(name="Message")
Group = Class(name="Group")
Topic = Class(name="Topic")
CommentTopic = Class(name="CommentTopic")
Tag = Class(name="Tag")
Invitation = Class(name="Invitation")

# User class attributes and methods
User_userName: Property = Property(name="userName", type=StringType)
User_email: Property = Property(name="email", type=StringType)
User_password: Property = Property(name="password", type=StringType)
User.attributes={User_password, User_email, User_userName}

# Rol class attributes and methods
Rol_nombre: Property = Property(name="nombre", type=StringType)
Rol.attributes={Rol_nombre}

# Post class attributes and methods
Post_userName: Property = Property(name="userName", type=StringType)
Post_content: Property = Property(name="content", type=StringType)
Post_Date: Property = Property(name="Date", type=StringType)
Post.attributes={Post_userName, Post_Date, Post_content}

# Comment class attributes and methods
Comment_userName: Property = Property(name="userName", type=StringType)
Comment_comment: Property = Property(name="comment", type=StringType)
Comment_date: Property = Property(name="date", type=StringType)
Comment.attributes={Comment_comment, Comment_userName, Comment_date}

# Vote class attributes and methods
Vote_tipo: Property = Property(name="tipo", type=BooleanType)
Vote.attributes={Vote_tipo}

# Message class attributes and methods

# Group class attributes and methods

# Topic class attributes and methods

# CommentTopic class attributes and methods

# Tag class attributes and methods

# Invitation class attributes and methods

# Relationships
Rol_User: BinaryAssociation = BinaryAssociation(
    name="Rol_User",
    ends={
        Property(name="user0", type=User, multiplicity=Multiplicity(0, 9999)),
        Property(name="rol1", type=Rol, multiplicity=Multiplicity(1, 1))
    }
)
User_Post: BinaryAssociation = BinaryAssociation(
    name="User_Post",
    ends={
        Property(name="user3", type=User, multiplicity=Multiplicity(1, 1)),
        Property(name="post2", type=Post, multiplicity=Multiplicity(0, 9999))
    }
)
Post_Vote: BinaryAssociation = BinaryAssociation(
    name="Post_Vote",
    ends={
        Property(name="vote4", type=Vote, multiplicity=Multiplicity(0, 9999)),
        Property(name="post5", type=Post, multiplicity=Multiplicity(0, 1))
    }
)
Comments_Vote: BinaryAssociation = BinaryAssociation(
    name="Comments_Vote",
    ends={
        Property(name="vote6", type=Vote, multiplicity=Multiplicity(0, 9999)),
        Property(name="comment7", type=Comment, multiplicity=Multiplicity(0, 1))
    }
)
User_Message: BinaryAssociation = BinaryAssociation(
    name="User_Message",
    ends={
        Property(name="message8", type=Message, multiplicity=Multiplicity(0, 9999)),
        Property(name="user9", type=User, multiplicity=Multiplicity(1, 1))
    }
)
Group_User: BinaryAssociation = BinaryAssociation(
    name="Group_User",
    ends={
        Property(name="user10", type=User, multiplicity=Multiplicity(0, 9999)),
        Property(name="group11", type=Group, multiplicity=Multiplicity(0, 9999))
    }
)
Topic_Vote: BinaryAssociation = BinaryAssociation(
    name="Topic_Vote",
    ends={
        Property(name="vote12", type=Vote, multiplicity=Multiplicity(0, 9999)),
        Property(name="topic13", type=Topic, multiplicity=Multiplicity(0, 1))
    }
)
Post_Comment: BinaryAssociation = BinaryAssociation(
    name="Post_Comment",
    ends={
        Property(name="comment14", type=Comment, multiplicity=Multiplicity(0, 9999)),
        Property(name="post15", type=Post, multiplicity=Multiplicity(1, 1))
    }
)
Topic_CommentTopic: BinaryAssociation = BinaryAssociation(
    name="Topic_CommentTopic",
    ends={
        Property(name="comment16", type=CommentTopic, multiplicity=Multiplicity(0, 9999)),
        Property(name="topic17", type=Topic, multiplicity=Multiplicity(1, 1))
    }
)
Topic_Tag: BinaryAssociation = BinaryAssociation(
    name="Topic_Tag",
    ends={
        Property(name="tag18", type=Tag, multiplicity=Multiplicity(0, 9999)),
        Property(name="topic19", type=Topic, multiplicity=Multiplicity(1, 1))
    }
)
User_User: BinaryAssociation = BinaryAssociation(
    name="User_User",
    ends={
        Property(name="user20", type=User, multiplicity=Multiplicity(1, 1)),
        Property(name="friends21", type=User, multiplicity=Multiplicity(0, 9999))
    }
)
User_Invitation: BinaryAssociation = BinaryAssociation(
    name="User_Invitation",
    ends={
        Property(name="invitation22", type=Invitation, multiplicity=Multiplicity(0, 9999)),
        Property(name="user23", type=User, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_8ySDENx5Eeia2L8p9znULA",
    types={User, Rol, Post, Comment, Vote, Message, Group, Topic, CommentTopic, Tag, Invitation},
    associations={Rol_User, User_Post, Post_Vote, Comments_Vote, User_Message, Group_User, Topic_Vote, Post_Comment, Topic_CommentTopic, Topic_Tag, User_User, User_Invitation},
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