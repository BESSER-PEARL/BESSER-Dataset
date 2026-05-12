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
Friend = Class(name="Friend")
Message = Class(name="Message")
Photos = Class(name="Photos")
HomePage = Class(name="HomePage")

# Account class attributes and methods
Account_name: Property = Property(name="name", type=StringType)
Account_email: Property = Property(name="email", type=StringType)
Account_password: Property = Property(name="password", type=StringType)
Account_entity: Property = Property(name="entity", type=StringType)
Account.attributes={Account_entity, Account_email, Account_password, Account_name}

# User class attributes and methods
User__F: Property = Property(name="_F", type=Friend)
User___M: Property = Property(name="__M", type=Message)
User__P: Property = Property(name="_P", type=Photos)
User.attributes={User___M, User__F, User__P}

# Friend class attributes and methods
Friend_friend____: Property = Property(name="friend____", type=StringType)
Friend_acceptornot: Property = Property(name="acceptornot", type=BooleanType)
Friend.attributes={Friend_friend____, Friend_acceptornot}

# Message class attributes and methods
Message_sender: Property = Property(name="sender", type=StringType)
Message_message: Property = Property(name="message", type=StringType)
Message_reciver: Property = Property(name="reciver", type=StringType)
Message.attributes={Message_sender, Message_message, Message_reciver}

# Photos class attributes and methods
Photos___photos: Property = Property(name="__photos", type=StringType)
Photos.attributes={Photos___photos}

# HomePage class attributes and methods
HomePage___status: Property = Property(name="__status", type=StringType)
HomePage___friendStatus: Property = Property(name="__friendStatus", type=StringType)
HomePage_likeorunlike: Property = Property(name="likeorunlike", type=BooleanType)
HomePage.attributes={HomePage_likeorunlike, HomePage___friendStatus, HomePage___status}

# Relationships
User_Friend: BinaryAssociation = BinaryAssociation(
    name="User_Friend",
    ends={
        Property(name="friend0", type=Friend, multiplicity=Multiplicity(0, 1)),
        Property(name="user1", type=User, multiplicity=Multiplicity(0, 1))
    }
)
User_HomePage: BinaryAssociation = BinaryAssociation(
    name="User_HomePage",
    ends={
        Property(name="homePage2", type=HomePage, multiplicity=Multiplicity(0, 1)),
        Property(name="user3", type=User, multiplicity=Multiplicity(0, 1))
    }
)
User_Message: BinaryAssociation = BinaryAssociation(
    name="User_Message",
    ends={
        Property(name="message4", type=Message, multiplicity=Multiplicity(0, 1)),
        Property(name="user5", type=User, multiplicity=Multiplicity(0, 1))
    }
)
User_Photos: BinaryAssociation = BinaryAssociation(
    name="User_Photos",
    ends={
        Property(name="photos6", type=Photos, multiplicity=Multiplicity(0, 1)),
        Property(name="user7", type=User, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="e6d28af2_9eb1_433c_b01d_23ea9db84462",
    types={Account, User, Friend, Message, Photos, HomePage},
    associations={User_Friend, User_HomePage, User_Message, User_Photos},
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