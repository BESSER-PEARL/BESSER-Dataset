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
AccountType: Enumeration = Enumeration(
    name="AccountType",
    literals={
            
    }
)

TransactionType: Enumeration = Enumeration(
    name="TransactionType",
    literals={
            
    }
)

# Classes
Customer = Class(name="Customer")
Account = Class(name="Account")
Transaction = Class(name="Transaction")
SavingsAccount = Class(name="SavingsAccount")
Login = Class(name="Login")
TransferTransaction = Class(name="TransferTransaction")
CertificatesOfDepositAccount = Class(name="CertificatesOfDepositAccount")

# Customer class attributes and methods
Customer_name: Property = Property(name="name", type=StringType)
Customer_dateOfBirth: Property = Property(name="dateOfBirth", type=DateType)
Customer_address: Property = Property(name="address", type=StringType)
Customer_phoneNumber: Property = Property(name="phoneNumber", type=StringType)
Customer_emailAddress: Property = Property(name="emailAddress", type=StringType)
Customer.attributes={Customer_name, Customer_emailAddress, Customer_phoneNumber, Customer_address, Customer_dateOfBirth}

# Account class attributes and methods
Account_accountNo: Property = Property(name="accountNo", type=StringType)
Account_type: Property = Property(name="type", type=AccountType)
Account_balance: Property = Property(name="balance", type=FloatType)
Account.attributes={Account_type, Account_balance, Account_accountNo}

# Transaction class attributes and methods
Transaction_id: Property = Property(name="id", type=IntegerType)
Transaction_type: Property = Property(name="type", type=TransactionType)
Transaction_transactionTime: Property = Property(name="transactionTime", type=DateType)
Transaction_amount: Property = Property(name="amount", type=FloatType)
Transaction.attributes={Transaction_transactionTime, Transaction_id, Transaction_type, Transaction_amount}

# SavingsAccount class attributes and methods
SavingsAccount_interestRate: Property = Property(name="interestRate", type=FloatType)
SavingsAccount.attributes={SavingsAccount_interestRate}

# Login class attributes and methods
Login_username: Property = Property(name="username", type=StringType)
Login_password: Property = Property(name="password", type=StringType)
Login_securityQuestion: Property = Property(name="securityQuestion", type=StringType)
Login_securityAnswer: Property = Property(name="securityAnswer", type=StringType)
Login_lastLoginTime: Property = Property(name="lastLoginTime", type=DateType)
Login.attributes={Login_username, Login_securityQuestion, Login_securityAnswer, Login_lastLoginTime, Login_password}

# TransferTransaction class attributes and methods
TransferTransaction_targetAccount: Property = Property(name="targetAccount", type=Account)
TransferTransaction_sourceAccount: Property = Property(name="sourceAccount", type=Account)
TransferTransaction.attributes={TransferTransaction_targetAccount, TransferTransaction_sourceAccount}

# CertificatesOfDepositAccount class attributes and methods
CertificatesOfDepositAccount_interestRate: Property = Property(name="interestRate", type=FloatType)
CertificatesOfDepositAccount_timePeriod: Property = Property(name="timePeriod", type=IntegerType)
CertificatesOfDepositAccount.attributes={CertificatesOfDepositAccount_interestRate, CertificatesOfDepositAccount_timePeriod}

# Relationships
Customer_Login: BinaryAssociation = BinaryAssociation(
    name="Customer_Login",
    ends={
        Property(name="login4", type=Login, multiplicity=Multiplicity(0, 1)),
        Property(name="customer5", type=Customer, multiplicity=Multiplicity(1, 1))
    }
)
association2: BinaryAssociation = BinaryAssociation(
    name="association2",
    ends={
        Property(name="c0", type=Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="a1", type=Account, multiplicity=Multiplicity(1, 9999))
    }
)
Account_Transaction: BinaryAssociation = BinaryAssociation(
    name="Account_Transaction",
    ends={
        Property(name="transactions2", type=Transaction, multiplicity=Multiplicity(0, 9999)),
        Property(name="account3", type=Account, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="__UPH8FzCEeqK2M3E1LfZ7Q",
    types={Customer, Account, Transaction, SavingsAccount, Login, TransferTransaction, CertificatesOfDepositAccount, AccountType, TransactionType},
    associations={Customer_Login, association2, Account_Transaction},
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