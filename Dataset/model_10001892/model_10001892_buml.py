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
Role = Class(name="Role")
Account = Class(name="Account")
Balance = Class(name="Balance")
Country = Class(name="Country")
Location = Class(name="Location")
AttackHistory = Class(name="AttackHistory")
Attack = Class(name="Attack")
Result = Class(name="Result")
StartParam = Class(name="StartParam")
User_Actor = Class(name="User_Actor")
Register_UseCase = Class(name="Register_UseCase")
Authenticate_UseCase = Class(name="Authenticate_UseCase")
View_Home_UseCase = Class(name="View_Home_UseCase")
View_Profile_UseCase = Class(name="View_Profile_UseCase")
Edit_Profile_UseCase = Class(name="Edit_Profile_UseCase")
View_AttackHistory_UseCase = Class(name="View_AttackHistory_UseCase")
ExecuteAttack_UseCase = Class(name="ExecuteAttack_UseCase")
View_AttackNews_UseCase = Class(name="View_AttackNews_UseCase")
Admin_Actor = Class(name="Admin_Actor")
Edit_Profile_UseCase1 = Class(name="Edit_Profile_UseCase1")
View_AttackHistory_UseCase1 = Class(name="View_AttackHistory_UseCase1")
View_AttackNews_UseCase1 = Class(name="View_AttackNews_UseCase1")
Authenticate_UseCase1 = Class(name="Authenticate_UseCase1")
View_Home_UseCase1 = Class(name="View_Home_UseCase1")
View_Profile_UseCase1 = Class(name="View_Profile_UseCase1")

# User class attributes and methods
User_lName: Property = Property(name="lName", type=StringType)
User_birthDate: Property = Property(name="birthDate", type=IntegerType)
User_email: Property = Property(name="email", type=StringType)
User_phoneNumber: Property = Property(name="phoneNumber", type=IntegerType)
User_cin: Property = Property(name="cin", type=StringType)
User_fName: Property = Property(name="fName", type=StringType)
User.attributes={User_email, User_phoneNumber, User_fName, User_cin, User_birthDate, User_lName}

# Role class attributes and methods
Role_type: Property = Property(name="type", type=StringType)
Role.attributes={Role_type}

# Account class attributes and methods
Account_login: Property = Property(name="login", type=StringType)
Account_password: Property = Property(name="password", type=IntegerType)
Account_creationDate: Property = Property(name="creationDate", type=IntegerType)
Account.attributes={Account_password, Account_creationDate, Account_login}

# Balance class attributes and methods
Balance_tokens: Property = Property(name="tokens", type=IntegerType)
Balance.attributes={Balance_tokens}

# Country class attributes and methods
Country_countryName: Property = Property(name="countryName", type=StringType)
Country.attributes={Country_countryName}

# Location class attributes and methods
Location_streetAddress: Property = Property(name="streetAddress", type=StringType)
Location_postalCode: Property = Property(name="postalCode", type=IntegerType)
Location_city: Property = Property(name="city", type=StringType)
Location_stateProvince: Property = Property(name="stateProvince", type=StringType)
Location.attributes={Location_streetAddress, Location_city, Location_postalCode, Location_stateProvince}

# AttackHistory class attributes and methods
AttackHistory_auto: Property = Property(name="auto", type=BooleanType)
AttackHistory_target: Property = Property(name="target", type=StringType)
AttackHistory_date: Property = Property(name="date", type=IntegerType)
AttackHistory.attributes={AttackHistory_auto, AttackHistory_date, AttackHistory_target}

# Attack class attributes and methods
Attack_name: Property = Property(name="name", type=StringType)
Attack_requiredTokens: Property = Property(name="requiredTokens", type=IntegerType)
Attack.attributes={Attack_name, Attack_requiredTokens}

# Result class attributes and methods
Result_value: Property = Property(name="value", type=StringType)
Result.attributes={Result_value}

# StartParam class attributes and methods
StartParam_type: Property = Property(name="type", type=StringType)
StartParam_value: Property = Property(name="value", type=StringType)
StartParam.attributes={StartParam_value, StartParam_type}

# User_Actor class attributes and methods

# Register_UseCase class attributes and methods

# Authenticate_UseCase class attributes and methods

# View_Home_UseCase class attributes and methods

# View_Profile_UseCase class attributes and methods

# Edit_Profile_UseCase class attributes and methods

# View_AttackHistory_UseCase class attributes and methods

# ExecuteAttack_UseCase class attributes and methods

# View_AttackNews_UseCase class attributes and methods

# Admin_Actor class attributes and methods

# Edit_Profile_UseCase1 class attributes and methods

# View_AttackHistory_UseCase1 class attributes and methods

# View_AttackNews_UseCase1 class attributes and methods

# Authenticate_UseCase1 class attributes and methods

# View_Home_UseCase1 class attributes and methods

# View_Profile_UseCase1 class attributes and methods

# Relationships
User_Role: BinaryAssociation = BinaryAssociation(
    name="User_Role",
    ends={
        Property(name="role0", type=Role, multiplicity=Multiplicity(1, 9999)),
        Property(name="user1", type=User, multiplicity=Multiplicity(0, 9999))
    }
)
User_Location: BinaryAssociation = BinaryAssociation(
    name="User_Location",
    ends={
        Property(name="location2", type=Location, multiplicity=Multiplicity(1, 1)),
        Property(name="user3", type=User, multiplicity=Multiplicity(1, 1))
    }
)
User_Account: BinaryAssociation = BinaryAssociation(
    name="User_Account",
    ends={
        Property(name="account4", type=Account, multiplicity=Multiplicity(1, 1)),
        Property(name="user5", type=User, multiplicity=Multiplicity(1, 1))
    }
)
Account_Balance: BinaryAssociation = BinaryAssociation(
    name="Account_Balance",
    ends={
        Property(name="balance6", type=Balance, multiplicity=Multiplicity(1, 1)),
        Property(name="account7", type=Account, multiplicity=Multiplicity(1, 1))
    }
)
Location_Country: BinaryAssociation = BinaryAssociation(
    name="Location_Country",
    ends={
        Property(name="country8", type=Country, multiplicity=Multiplicity(0, 1)),
        Property(name="location9", type=Location, multiplicity=Multiplicity(0, 9999))
    }
)
Attack_AttackHistory: BinaryAssociation = BinaryAssociation(
    name="Attack_AttackHistory",
    ends={
        Property(name="attackHistory10", type=AttackHistory, multiplicity=Multiplicity(0, 9999)),
        Property(name="attack11", type=Attack, multiplicity=Multiplicity(1, 1))
    }
)
StartParam_AttackHistory: BinaryAssociation = BinaryAssociation(
    name="StartParam_AttackHistory",
    ends={
        Property(name="attackHistory12", type=AttackHistory, multiplicity=Multiplicity(0, 9999)),
        Property(name="startParam13", type=StartParam, multiplicity=Multiplicity(1, 1))
    }
)
Result_AttackHistory: BinaryAssociation = BinaryAssociation(
    name="Result_AttackHistory",
    ends={
        Property(name="attackHistory14", type=AttackHistory, multiplicity=Multiplicity(0, 9999)),
        Property(name="result15", type=Result, multiplicity=Multiplicity(1, 1))
    }
)
User_AttackHistory: BinaryAssociation = BinaryAssociation(
    name="User_AttackHistory",
    ends={
        Property(name="attackHistory16", type=AttackHistory, multiplicity=Multiplicity(0, 1)),
        Property(name="user17", type=User, multiplicity=Multiplicity(0, 1))
    }
)
User_View_Home: BinaryAssociation = BinaryAssociation(
    name="User_View_Home",
    ends={
        Property(name="view_Home18", type=View_Home_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="user19", type=User_Actor, multiplicity=Multiplicity(0, 1))
    }
)
User_Edit_Profile: BinaryAssociation = BinaryAssociation(
    name="User_Edit_Profile",
    ends={
        Property(name="edit_Profile20", type=Edit_Profile_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="user21", type=User_Actor, multiplicity=Multiplicity(0, 1))
    }
)
User_View_Profile: BinaryAssociation = BinaryAssociation(
    name="User_View_Profile",
    ends={
        Property(name="view_Profile22", type=View_Profile_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="user23", type=User_Actor, multiplicity=Multiplicity(0, 1))
    }
)
User_View_AttackHistory: BinaryAssociation = BinaryAssociation(
    name="User_View_AttackHistory",
    ends={
        Property(name="view_AttackHistory24", type=View_AttackHistory_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="user25", type=User_Actor, multiplicity=Multiplicity(0, 1))
    }
)
User_ExecuteAttack: BinaryAssociation = BinaryAssociation(
    name="User_ExecuteAttack",
    ends={
        Property(name="executeAttack26", type=ExecuteAttack_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="user27", type=User_Actor, multiplicity=Multiplicity(0, 1))
    }
)
User_Register: BinaryAssociation = BinaryAssociation(
    name="User_Register",
    ends={
        Property(name="register28", type=Register_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="user29", type=User_Actor, multiplicity=Multiplicity(0, 1))
    }
)
User_View_AttackNews: BinaryAssociation = BinaryAssociation(
    name="User_View_AttackNews",
    ends={
        Property(name="view_AttackNews30", type=View_AttackNews_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="user31", type=User_Actor, multiplicity=Multiplicity(0, 1))
    }
)
User_View_Home2: BinaryAssociation = BinaryAssociation(
    name="User_View_Home2",
    ends={
        Property(name="view_Home32", type=View_Home_UseCase1, multiplicity=Multiplicity(0, 1)),
        Property(name="user33", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
User_View_AttackHistory2: BinaryAssociation = BinaryAssociation(
    name="User_View_AttackHistory2",
    ends={
        Property(name="view_AttackHistory34", type=View_AttackHistory_UseCase1, multiplicity=Multiplicity(0, 1)),
        Property(name="user35", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
User_View_Profile2: BinaryAssociation = BinaryAssociation(
    name="User_View_Profile2",
    ends={
        Property(name="view_Profile36", type=View_Profile_UseCase1, multiplicity=Multiplicity(0, 1)),
        Property(name="user37", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
User_Edit_Profile2: BinaryAssociation = BinaryAssociation(
    name="User_Edit_Profile2",
    ends={
        Property(name="edit_Profile38", type=Edit_Profile_UseCase1, multiplicity=Multiplicity(0, 1)),
        Property(name="user39", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
User_View_AttackNews2: BinaryAssociation = BinaryAssociation(
    name="User_View_AttackNews2",
    ends={
        Property(name="view_AttackNews40", type=View_AttackNews_UseCase1, multiplicity=Multiplicity(0, 1)),
        Property(name="user41", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_bw8NAIyAEei5SqevG77dlg",
    types={User, Role, Account, Balance, Country, Location, AttackHistory, Attack, Result, StartParam, User_Actor, Register_UseCase, Authenticate_UseCase, View_Home_UseCase, View_Profile_UseCase, Edit_Profile_UseCase, View_AttackHistory_UseCase, ExecuteAttack_UseCase, View_AttackNews_UseCase, Admin_Actor, Edit_Profile_UseCase1, View_AttackHistory_UseCase1, View_AttackNews_UseCase1, Authenticate_UseCase1, View_Home_UseCase1, View_Profile_UseCase1},
    associations={User_Role, User_Location, User_Account, Account_Balance, Location_Country, Attack_AttackHistory, StartParam_AttackHistory, Result_AttackHistory, User_AttackHistory, User_View_Home, User_Edit_Profile, User_View_Profile, User_View_AttackHistory, User_ExecuteAttack, User_Register, User_View_AttackNews, User_View_Home2, User_View_AttackHistory2, User_View_Profile2, User_Edit_Profile2, User_View_AttackNews2},
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