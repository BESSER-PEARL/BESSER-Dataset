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

# Enumerations
virtualtour_TransactionType: Enumeration = Enumeration(
    name="virtualtour_TransactionType",
    literals={
            
    }
)

# Classes
Client = Class(name="Client")
Login = Class(name="Login")
virtualtour_Transaction = Class(name="virtualtour_Transaction")
virtualtour_UploadFloorplan = Class(name="virtualtour_UploadFloorplan")
virtualtour_UploadPicture = Class(name="virtualtour_UploadPicture")
virtualtour_TakePicture = Class(name="virtualtour_TakePicture")
virtualtour_LinkVirtual = Class(name="virtualtour_LinkVirtual")
virtualtour_ArchiveVirtual = Class(name="virtualtour_ArchiveVirtual")
client_HomeOwner = Class(name="client_HomeOwner")
client_Realtor = Class(name="client_Realtor")
client_ClientAccount = Class(name="client_ClientAccount")
ClientType = Class(name="ClientType")

# Client class attributes and methods
Client_name: Property = Property(name="name", type=StringType)
Client_dateOfBirth: Property = Property(name="dateOfBirth", type=DateType)
Client_address: Property = Property(name="address", type=StringType)
Client_phoneNumber: Property = Property(name="phoneNumber", type=StringType)
Client_emailAddress: Property = Property(name="emailAddress", type=StringType)
Client.attributes={Client_address, Client_phoneNumber, Client_dateOfBirth, Client_emailAddress, Client_name}

# Login class attributes and methods
Login_username: Property = Property(name="username", type=StringType)
Login_securityAnswer: Property = Property(name="securityAnswer", type=StringType)
Login_password: Property = Property(name="password", type=StringType)
Login_securityQuestion: Property = Property(name="securityQuestion", type=StringType)
Login_lastLoginTime: Property = Property(name="lastLoginTime", type=DateType)
Login.attributes={Login_lastLoginTime, Login_securityAnswer, Login_username, Login_password, Login_securityQuestion}

# virtualtour_Transaction class attributes and methods
virtualtour_Transaction_id: Property = Property(name="id", type=IntegerType)
virtualtour_Transaction_type: Property = Property(name="type", type=virtualtour_TransactionType)
virtualtour_Transaction_transactionTime: Property = Property(name="transactionTime", type=DateType)
virtualtour_Transaction.attributes={virtualtour_Transaction_type, virtualtour_Transaction_transactionTime, virtualtour_Transaction_id}

# virtualtour_UploadFloorplan class attributes and methods

# virtualtour_UploadPicture class attributes and methods

# virtualtour_TakePicture class attributes and methods

# virtualtour_LinkVirtual class attributes and methods

# virtualtour_ArchiveVirtual class attributes and methods

# client_HomeOwner class attributes and methods
client_HomeOwner_name: Property = Property(name="name", type=StringType)
client_HomeOwner.attributes={client_HomeOwner_name}

# client_Realtor class attributes and methods
client_Realtor_name: Property = Property(name="name", type=StringType)
client_Realtor.attributes={client_Realtor_name}

# client_ClientAccount class attributes and methods
client_ClientAccount_clientNo: Property = Property(name="clientNo", type=StringType)
client_ClientAccount_type: Property = Property(name="type", type=ClientType)
client_ClientAccount.attributes={client_ClientAccount_clientNo, client_ClientAccount_type}

# ClientType class attributes and methods

# Relationships
association2: BinaryAssociation = BinaryAssociation(
    name="association2",
    ends={
        Property(name="client0", type=Client, multiplicity=Multiplicity(1, 1)),
        Property(name="a1", type=client_ClientAccount, multiplicity=Multiplicity(1, 9999))
    }
)
Account_Transaction: BinaryAssociation = BinaryAssociation(
    name="Account_Transaction",
    ends={
        Property(name="transactions2", type=virtualtour_Transaction, multiplicity=Multiplicity(0, 9999)),
        Property(name="account3", type=client_ClientAccount, multiplicity=Multiplicity(1, 1))
    }
)
Customer_Login: BinaryAssociation = BinaryAssociation(
    name="Customer_Login",
    ends={
        Property(name="login4", type=Login, multiplicity=Multiplicity(0, 1)),
        Property(name="client5", type=Client, multiplicity=Multiplicity(1, 1))
    }
)
LinkVirtual_Transaction: BinaryAssociation = BinaryAssociation(
    name="LinkVirtual_Transaction",
    ends={
        Property(name="transaction6", type=virtualtour_Transaction, multiplicity=Multiplicity(0, 1)),
        Property(name="linkVirtual7", type=virtualtour_LinkVirtual, multiplicity=Multiplicity(0, 1))
    }
)
ArchiveVirtual_Transaction: BinaryAssociation = BinaryAssociation(
    name="ArchiveVirtual_Transaction",
    ends={
        Property(name="transaction8", type=virtualtour_Transaction, multiplicity=Multiplicity(0, 1)),
        Property(name="archiveVirtual9", type=virtualtour_ArchiveVirtual, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_4f8563cc_941a_4c89_947b_4c6713a855dc",
    types={Client, Login, virtualtour_Transaction, virtualtour_UploadFloorplan, virtualtour_UploadPicture, virtualtour_TakePicture, virtualtour_LinkVirtual, virtualtour_ArchiveVirtual, client_HomeOwner, client_Realtor, client_ClientAccount, ClientType, virtualtour_TransactionType},
    associations={association2, Account_Transaction, Customer_Login, LinkVirtual_Transaction, ArchiveVirtual_Transaction},
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