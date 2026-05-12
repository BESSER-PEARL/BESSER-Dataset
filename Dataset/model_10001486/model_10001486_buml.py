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
Account = Class(name="Account")
User = Class(name="User")
Project = Class(name="Project")
Administrator = Class(name="Administrator")
Comment = Class(name="Comment")
IAcc_Interface = Class(name="IAcc_Interface")

# Account class attributes and methods
Account_UserName: Property = Property(name="UserName", type=StringType)
Account_Info: Property = Property(name="Info", type=StringType)
Account.attributes={Account_Info, Account_UserName}

# User class attributes and methods
User_Id: Property = Property(name="Id", type=IntegerType)
User.attributes={User_Id}

# Project class attributes and methods
Project_Id: Property = Property(name="Id", type=IntegerType)
Project_Title: Property = Property(name="Title", type=StringType)
Project_Info: Property = Property(name="Info", type=StringType)
Project_Access: Property = Property(name="Access", type=StringType)
Project_State: Property = Property(name="State", type=StringType)
Project.attributes={Project_Id, Project_Title, Project_State, Project_Access, Project_Info}

# Administrator class attributes and methods
Administrator_Id: Property = Property(name="Id", type=IntegerType)
Administrator.attributes={Administrator_Id}

# Comment class attributes and methods
Comment_Id: Property = Property(name="Id", type=IntegerType)
Comment_Creator: Property = Property(name="Creator", type=User)
Comment_Title: Property = Property(name="Title", type=StringType)
Comment_Body: Property = Property(name="Body", type=StringType)
Comment_CreationDate: Property = Property(name="CreationDate", type=StringType)
Comment.attributes={Comment_Title, Comment_Creator, Comment_Body, Comment_Id, Comment_CreationDate}

# IAcc_Interface class attributes and methods

# Relationships
User_Project: BinaryAssociation = BinaryAssociation(
    name="User_Project",
    ends={
        Property(name="project4", type=Project, multiplicity=Multiplicity(0, 9999)),
        Property(name="user5", type=User, multiplicity=Multiplicity(1, 1))
    }
)
Account_User: BinaryAssociation = BinaryAssociation(
    name="Account_User",
    ends={
        Property(name="user6", type=User, multiplicity=Multiplicity(1, 1)),
        Property(name="account7", type=Account, multiplicity=Multiplicity(1, 1))
    }
)
Account_Administrator: BinaryAssociation = BinaryAssociation(
    name="Account_Administrator",
    ends={
        Property(name="administrator8", type=Administrator, multiplicity=Multiplicity(1, 1)),
        Property(name="account9", type=Account, multiplicity=Multiplicity(1, 1))
    }
)
Administrator_Comment: BinaryAssociation = BinaryAssociation(
    name="Administrator_Comment",
    ends={
        Property(name="comment0", type=Comment, multiplicity=Multiplicity(0, 9999)),
        Property(name="administrator1", type=Administrator, multiplicity=Multiplicity(1, 1))
    }
)
User_Comment: BinaryAssociation = BinaryAssociation(
    name="User_Comment",
    ends={
        Property(name="comment2", type=Comment, multiplicity=Multiplicity(0, 9999)),
        Property(name="user3", type=User, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_ACUM4P5aEeiq1obLTi0emw",
    types={Account, User, Project, Administrator, Comment, IAcc_Interface},
    associations={User_Project, Account_User, Account_Administrator, Administrator_Comment, User_Comment},
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