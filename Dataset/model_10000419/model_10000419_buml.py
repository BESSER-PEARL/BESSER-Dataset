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
transactions_TransactionType: Enumeration = Enumeration(
    name="transactions_TransactionType",
    literals={
            
    }
)

account_AccountType: Enumeration = Enumeration(
    name="account_AccountType",
    literals={
            
    }
)

# Classes
account_Account = Class(name="account_Account")
mypackage_Login = Class(name="mypackage_Login")
mypackage_Customer = Class(name="mypackage_Customer")
Class_ = Class(name="Class")
transactions_Transaction = Class(name="transactions_Transaction")
transactions_DepositTransaction = Class(name="transactions_DepositTransaction")
transactions_WithdrawTransaction = Class(name="transactions_WithdrawTransaction")
transactions_TransferTransaction = Class(name="transactions_TransferTransaction")
account_SavingsAccount = Class(name="account_SavingsAccount")
account_CertificatesOfDepositAccount = Class(name="account_CertificatesOfDepositAccount")
account_CheckingAccount = Class(name="account_CheckingAccount")

# account_Account class attributes and methods
account_Account_accountNo: Property = Property(name="accountNo", type=StringType)
account_Account_type: Property = Property(name="type", type=account_AccountType)
account_Account_balance: Property = Property(name="balance", type=FloatType)
account_Account.attributes={account_Account_type, account_Account_accountNo, account_Account_balance}

# mypackage_Login class attributes and methods
mypackage_Login_username: Property = Property(name="username", type=StringType)
mypackage_Login_password: Property = Property(name="password", type=StringType)
mypackage_Login_securityQuestion: Property = Property(name="securityQuestion", type=StringType)
mypackage_Login_securityAnswer: Property = Property(name="securityAnswer", type=StringType)
mypackage_Login_lastLoginTime: Property = Property(name="lastLoginTime", type=DateType)
mypackage_Login.attributes={mypackage_Login_securityAnswer, mypackage_Login_username, mypackage_Login_password, mypackage_Login_securityQuestion, mypackage_Login_lastLoginTime}

# mypackage_Customer class attributes and methods
mypackage_Customer_name: Property = Property(name="name", type=StringType)
mypackage_Customer_dateOfBirth: Property = Property(name="dateOfBirth", type=DateType)
mypackage_Customer_address: Property = Property(name="address", type=StringType)
mypackage_Customer_phoneNumber: Property = Property(name="phoneNumber", type=StringType)
mypackage_Customer_emailAddress: Property = Property(name="emailAddress", type=StringType)
mypackage_Customer.attributes={mypackage_Customer_dateOfBirth, mypackage_Customer_name, mypackage_Customer_emailAddress, mypackage_Customer_address, mypackage_Customer_phoneNumber}

# Class class attributes and methods

# transactions_Transaction class attributes and methods
transactions_Transaction_id: Property = Property(name="id", type=IntegerType)
transactions_Transaction_type: Property = Property(name="type", type=transactions_TransactionType)
transactions_Transaction_transactionTime: Property = Property(name="transactionTime", type=DateType)
transactions_Transaction_amount: Property = Property(name="amount", type=FloatType)
transactions_Transaction.attributes={transactions_Transaction_type, transactions_Transaction_amount, transactions_Transaction_transactionTime, transactions_Transaction_id}

# transactions_DepositTransaction class attributes and methods

# transactions_WithdrawTransaction class attributes and methods

# transactions_TransferTransaction class attributes and methods
transactions_TransferTransaction_targetAccount: Property = Property(name="targetAccount", type=account_Account)
transactions_TransferTransaction_sourceAccount: Property = Property(name="sourceAccount", type=account_Account)
transactions_TransferTransaction.attributes={transactions_TransferTransaction_targetAccount, transactions_TransferTransaction_sourceAccount}

# account_SavingsAccount class attributes and methods
account_SavingsAccount_interestRate: Property = Property(name="interestRate", type=FloatType)
account_SavingsAccount.attributes={account_SavingsAccount_interestRate}

# account_CertificatesOfDepositAccount class attributes and methods
account_CertificatesOfDepositAccount_interestRate: Property = Property(name="interestRate", type=FloatType)
account_CertificatesOfDepositAccount_timePeriod: Property = Property(name="timePeriod", type=IntegerType)
account_CertificatesOfDepositAccount.attributes={account_CertificatesOfDepositAccount_interestRate, account_CertificatesOfDepositAccount_timePeriod}

# account_CheckingAccount class attributes and methods

# Relationships
association2: BinaryAssociation = BinaryAssociation(
    name="association2",
    ends={
        Property(name="customer0", type=mypackage_Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="account1", type=account_Account, multiplicity=Multiplicity(1, 9999))
    }
)
Account_Transaction: BinaryAssociation = BinaryAssociation(
    name="Account_Transaction",
    ends={
        Property(name="transactions2", type=transactions_Transaction, multiplicity=Multiplicity(0, 9999)),
        Property(name="account3", type=account_Account, multiplicity=Multiplicity(1, 1))
    }
)
Customer_Login: BinaryAssociation = BinaryAssociation(
    name="Customer_Login",
    ends={
        Property(name="login4", type=mypackage_Login, multiplicity=Multiplicity(0, 1)),
        Property(name="customer5", type=mypackage_Customer, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_34c8ab9e_8514_44f6_bf07_3a5858dbe5e4",
    types={account_Account, mypackage_Login, mypackage_Customer, Class_, transactions_Transaction, transactions_DepositTransaction, transactions_WithdrawTransaction, transactions_TransferTransaction, account_SavingsAccount, account_CertificatesOfDepositAccount, account_CheckingAccount, transactions_TransactionType, account_AccountType},
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