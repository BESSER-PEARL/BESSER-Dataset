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
Student = Class(name="Student")
Friend = Class(name="Friend")
Message = Class(name="Message")
HomePage = Class(name="HomePage")
Admin = Class(name="Admin")
Alumni = Class(name="Alumni")

# Account class attributes and methods
Account_name: Property = Property(name="name", type=StringType)
Account_email: Property = Property(name="email", type=StringType)
Account_password: Property = Property(name="password", type=StringType)
Account_Department: Property = Property(name="Department", type=StringType)
Account_class: Property = Property(name="class", type=StringType)
Account_Branch: Property = Property(name="Branch", type=StringType)
Account.attributes={Account_password, Account_Department, Account_name, Account_class, Account_email, Account_Branch}

# Student class attributes and methods
Student__F: Property = Property(name="_F", type=Friend)
Student___M: Property = Property(name="__M", type=Message)
Student_Report: Property = Property(name="Report", type=Message)
Student.attributes={Student_Report, Student___M, Student__F}

# Friend class attributes and methods
Friend_friend____: Property = Property(name="friend____", type=StringType)
Friend_acceptornot: Property = Property(name="acceptornot", type=BooleanType)
Friend.attributes={Friend_acceptornot, Friend_friend____}

# Message class attributes and methods
Message_sender: Property = Property(name="sender", type=StringType)
Message_message: Property = Property(name="message", type=StringType)
Message_reciver: Property = Property(name="reciver", type=StringType)
Message.attributes={Message_message, Message_sender, Message_reciver}

# HomePage class attributes and methods
HomePage___friendpost: Property = Property(name="__friendpost", type=HomePage)
HomePage.attributes={HomePage___friendpost}

# Admin class attributes and methods

# Alumni class attributes and methods
Alumni__F: Property = Property(name="_F", type=Friend)
Alumni___M: Property = Property(name="__M", type=Message)
Alumni_Report: Property = Property(name="Report", type=Message)
Alumni.attributes={Alumni__F, Alumni___M, Alumni_Report}

# Relationships
User_Friend: BinaryAssociation = BinaryAssociation(
    name="User_Friend",
    ends={
        Property(name="friend0", type=Friend, multiplicity=Multiplicity(0, 1)),
        Property(name="user1", type=Student, multiplicity=Multiplicity(0, 1))
    }
)
User_HomePage: BinaryAssociation = BinaryAssociation(
    name="User_HomePage",
    ends={
        Property(name="homePage2", type=HomePage, multiplicity=Multiplicity(0, 1)),
        Property(name="user3", type=Student, multiplicity=Multiplicity(0, 1))
    }
)
User_Message: BinaryAssociation = BinaryAssociation(
    name="User_Message",
    ends={
        Property(name="message4", type=Message, multiplicity=Multiplicity(0, 1)),
        Property(name="user5", type=Student, multiplicity=Multiplicity(0, 1))
    }
)
Alumni_HomePage: BinaryAssociation = BinaryAssociation(
    name="Alumni_HomePage",
    ends={
        Property(name="homePage6", type=HomePage, multiplicity=Multiplicity(0, 1)),
        Property(name="alumni7", type=Alumni, multiplicity=Multiplicity(0, 1))
    }
)
Alumni_Message: BinaryAssociation = BinaryAssociation(
    name="Alumni_Message",
    ends={
        Property(name="message8", type=Message, multiplicity=Multiplicity(0, 1)),
        Property(name="alumni9", type=Alumni, multiplicity=Multiplicity(0, 1))
    }
)
Account_Alumni: BinaryAssociation = BinaryAssociation(
    name="Account_Alumni",
    ends={
        Property(name="alumni10", type=Alumni, multiplicity=Multiplicity(0, 1)),
        Property(name="account11", type=Account, multiplicity=Multiplicity(0, 1))
    }
)
Student_Admin: BinaryAssociation = BinaryAssociation(
    name="Student_Admin",
    ends={
        Property(name="admin12", type=Admin, multiplicity=Multiplicity(0, 1)),
        Property(name="student13", type=Student, multiplicity=Multiplicity(0, 1))
    }
)
Account_Admin: BinaryAssociation = BinaryAssociation(
    name="Account_Admin",
    ends={
        Property(name="admin14", type=Admin, multiplicity=Multiplicity(0, 1)),
        Property(name="account15", type=Account, multiplicity=Multiplicity(0, 1))
    }
)
Alumni_Admin: BinaryAssociation = BinaryAssociation(
    name="Alumni_Admin",
    ends={
        Property(name="admin16", type=Admin, multiplicity=Multiplicity(0, 1)),
        Property(name="alumni17", type=Alumni, multiplicity=Multiplicity(0, 1))
    }
)
HomePage_Admin: BinaryAssociation = BinaryAssociation(
    name="HomePage_Admin",
    ends={
        Property(name="admin18", type=Admin, multiplicity=Multiplicity(0, 1)),
        Property(name="homePage19", type=HomePage, multiplicity=Multiplicity(0, 1))
    }
)
Message_Admin: BinaryAssociation = BinaryAssociation(
    name="Message_Admin",
    ends={
        Property(name="admin20", type=Admin, multiplicity=Multiplicity(0, 1)),
        Property(name="message21", type=Message, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_27a525ad_5b57_4571_bffb_75cb48746857",
    types={Account, Student, Friend, Message, HomePage, Admin, Alumni},
    associations={User_Friend, User_HomePage, User_Message, Alumni_HomePage, Alumni_Message, Account_Alumni, Student_Admin, Account_Admin, Alumni_Admin, HomePage_Admin, Message_Admin},
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