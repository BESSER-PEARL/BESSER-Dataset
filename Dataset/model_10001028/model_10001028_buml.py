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
WmMediaPager_Mini_App_TransactionType: Enumeration = Enumeration(
    name="WmMediaPager_Mini_App_TransactionType",
    literals={
            
    }
)

Native_App_AccountType: Enumeration = Enumeration(
    name="Native_App_AccountType",
    literals={
            
    }
)

# Classes
WmMediaPager_Mini_App_WmMediaPager = Class(name="WmMediaPager_Mini_App_WmMediaPager")
WmMediaPager_Mini_App_DepositTransaction = Class(name="WmMediaPager_Mini_App_DepositTransaction")
WmMediaPager_Mini_App_WithdrawTransaction = Class(name="WmMediaPager_Mini_App_WithdrawTransaction")
WmMediaPager_Mini_App_TransferTransaction = Class(name="WmMediaPager_Mini_App_TransferTransaction")
WmMediaPager_Mini_App_WmMediaPagerEvents = Class(name="WmMediaPager_Mini_App_WmMediaPagerEvents")
Native_App_SavingsAccount = Class(name="Native_App_SavingsAccount")
Native_App_CertificatesOfDepositAccount = Class(name="Native_App_CertificatesOfDepositAccount")
Native_App_CheckingAccount = Class(name="Native_App_CheckingAccount")
Native_App_Activity___ViewController___WmMediaPagerEvents = Class(name="Native_App_Activity___ViewController___WmMediaPagerEvents")
Customer = Class(name="Customer")
Login = Class(name="Login")

# WmMediaPager_Mini_App_WmMediaPager class attributes and methods
WmMediaPager_Mini_App_WmMediaPager_id: Property = Property(name="id", type=IntegerType)
WmMediaPager_Mini_App_WmMediaPager_type: Property = Property(name="type", type=WmMediaPager_Mini_App_TransactionType)
WmMediaPager_Mini_App_WmMediaPager_transactionTime: Property = Property(name="transactionTime", type=DateType)
WmMediaPager_Mini_App_WmMediaPager_amount: Property = Property(name="amount", type=FloatType)
WmMediaPager_Mini_App_WmMediaPager.attributes={WmMediaPager_Mini_App_WmMediaPager_type, WmMediaPager_Mini_App_WmMediaPager_transactionTime, WmMediaPager_Mini_App_WmMediaPager_id, WmMediaPager_Mini_App_WmMediaPager_amount}

# WmMediaPager_Mini_App_DepositTransaction class attributes and methods

# WmMediaPager_Mini_App_WithdrawTransaction class attributes and methods

# WmMediaPager_Mini_App_TransferTransaction class attributes and methods
WmMediaPager_Mini_App_TransferTransaction_targetAccount: Property = Property(name="targetAccount", type=Native_App_Activity___ViewController___WmMediaPagerEvents)
WmMediaPager_Mini_App_TransferTransaction_sourceAccount: Property = Property(name="sourceAccount", type=Native_App_Activity___ViewController___WmMediaPagerEvents)
WmMediaPager_Mini_App_TransferTransaction.attributes={WmMediaPager_Mini_App_TransferTransaction_targetAccount, WmMediaPager_Mini_App_TransferTransaction_sourceAccount}

# WmMediaPager_Mini_App_WmMediaPagerEvents class attributes and methods
WmMediaPager_Mini_App_WmMediaPagerEvents_id: Property = Property(name="id", type=IntegerType)
WmMediaPager_Mini_App_WmMediaPagerEvents_type: Property = Property(name="type", type=WmMediaPager_Mini_App_TransactionType)
WmMediaPager_Mini_App_WmMediaPagerEvents_transactionTime: Property = Property(name="transactionTime", type=DateType)
WmMediaPager_Mini_App_WmMediaPagerEvents_amount: Property = Property(name="amount", type=FloatType)
WmMediaPager_Mini_App_WmMediaPagerEvents.attributes={WmMediaPager_Mini_App_WmMediaPagerEvents_amount, WmMediaPager_Mini_App_WmMediaPagerEvents_id, WmMediaPager_Mini_App_WmMediaPagerEvents_transactionTime, WmMediaPager_Mini_App_WmMediaPagerEvents_type}

# Native_App_SavingsAccount class attributes and methods
Native_App_SavingsAccount_interestRate: Property = Property(name="interestRate", type=FloatType)
Native_App_SavingsAccount.attributes={Native_App_SavingsAccount_interestRate}

# Native_App_CertificatesOfDepositAccount class attributes and methods
Native_App_CertificatesOfDepositAccount_timePeriod: Property = Property(name="timePeriod", type=IntegerType)
Native_App_CertificatesOfDepositAccount_interestRate: Property = Property(name="interestRate", type=FloatType)
Native_App_CertificatesOfDepositAccount.attributes={Native_App_CertificatesOfDepositAccount_interestRate, Native_App_CertificatesOfDepositAccount_timePeriod}

# Native_App_CheckingAccount class attributes and methods
Native_App_CheckingAccount_name: Property = Property(name="name", type=StringType)
Native_App_CheckingAccount.attributes={Native_App_CheckingAccount_name}

# Native_App_Activity___ViewController___WmMediaPagerEvents class attributes and methods
Native_App_Activity___ViewController___WmMediaPagerEvents_accountNo: Property = Property(name="accountNo", type=StringType)
Native_App_Activity___ViewController___WmMediaPagerEvents_type: Property = Property(name="type", type=Native_App_AccountType)
Native_App_Activity___ViewController___WmMediaPagerEvents_balance: Property = Property(name="balance", type=FloatType)
Native_App_Activity___ViewController___WmMediaPagerEvents.attributes={Native_App_Activity___ViewController___WmMediaPagerEvents_type, Native_App_Activity___ViewController___WmMediaPagerEvents_accountNo, Native_App_Activity___ViewController___WmMediaPagerEvents_balance}

# Customer class attributes and methods
Customer_name: Property = Property(name="name", type=StringType)
Customer_dateOfBirth: Property = Property(name="dateOfBirth", type=DateType)
Customer_address: Property = Property(name="address", type=StringType)
Customer_phoneNumber: Property = Property(name="phoneNumber", type=StringType)
Customer_emailAddress: Property = Property(name="emailAddress", type=StringType)
Customer.attributes={Customer_emailAddress, Customer_phoneNumber, Customer_address, Customer_dateOfBirth, Customer_name}

# Login class attributes and methods
Login_username: Property = Property(name="username", type=StringType)
Login_securityAnswer: Property = Property(name="securityAnswer", type=StringType)
Login_password: Property = Property(name="password", type=StringType)
Login_securityQuestion: Property = Property(name="securityQuestion", type=StringType)
Login_lastLoginTime: Property = Property(name="lastLoginTime", type=DateType)
Login.attributes={Login_username, Login_securityAnswer, Login_password, Login_lastLoginTime, Login_securityQuestion}

# Relationships
association2: BinaryAssociation = BinaryAssociation(
    name="association2",
    ends={
        Property(name="customer0", type=Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="a1", type=Native_App_Activity___ViewController___WmMediaPagerEvents, multiplicity=Multiplicity(1, 9999))
    }
)
Account_Transaction: BinaryAssociation = BinaryAssociation(
    name="Account_Transaction",
    ends={
        Property(name="transactions2", type=WmMediaPager_Mini_App_WmMediaPager, multiplicity=Multiplicity(0, 9999)),
        Property(name="account3", type=Native_App_Activity___ViewController___WmMediaPagerEvents, multiplicity=Multiplicity(1, 1))
    }
)
Customer_Login: BinaryAssociation = BinaryAssociation(
    name="Customer_Login",
    ends={
        Property(name="login4", type=Login, multiplicity=Multiplicity(0, 1)),
        Property(name="customer5", type=Customer, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_7c9f6f7e_0389_489d_ae70_962700067563",
    types={WmMediaPager_Mini_App_WmMediaPager, WmMediaPager_Mini_App_DepositTransaction, WmMediaPager_Mini_App_WithdrawTransaction, WmMediaPager_Mini_App_TransferTransaction, WmMediaPager_Mini_App_WmMediaPagerEvents, Native_App_SavingsAccount, Native_App_CertificatesOfDepositAccount, Native_App_CheckingAccount, Native_App_Activity___ViewController___WmMediaPagerEvents, Customer, Login, WmMediaPager_Mini_App_TransactionType, Native_App_AccountType},
    associations={association2, Account_Transaction, Customer_Login},
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