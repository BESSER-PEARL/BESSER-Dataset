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
transaction_TransactionType: Enumeration = Enumeration(
    name="transaction_TransactionType",
    literals={
            
    }
)

account_AccountType: Enumeration = Enumeration(
    name="account_AccountType",
    literals={
            
    }
)

# Classes
Customer = Class(name="Customer")
Login = Class(name="Login")
transaction_Transaction = Class(name="transaction_Transaction")
transaction_DepositTransaction = Class(name="transaction_DepositTransaction")
transaction_WithdrawTransaction = Class(name="transaction_WithdrawTransaction")
transaction_TransferTransaction = Class(name="transaction_TransferTransaction")
account_SavingsAccount = Class(name="account_SavingsAccount")
account_CertificatesOfDepositAccount = Class(name="account_CertificatesOfDepositAccount")
account_CheckingAccount = Class(name="account_CheckingAccount")
account_Account = Class(name="account_Account")

# Customer class attributes and methods
Customer_name: Property = Property(name="name", type=StringType)
Customer_dateOfBirth: Property = Property(name="dateOfBirth", type=DateType)
Customer_address: Property = Property(name="address", type=StringType)
Customer_phoneNumber: Property = Property(name="phoneNumber", type=StringType)
Customer_emailAddress: Property = Property(name="emailAddress", type=StringType)
Customer.attributes={Customer_dateOfBirth, Customer_address, Customer_name, Customer_emailAddress, Customer_phoneNumber}

# Login class attributes and methods
Login_username: Property = Property(name="username", type=StringType)
Login_securityAnswer: Property = Property(name="securityAnswer", type=StringType)
Login_password: Property = Property(name="password", type=StringType)
Login_securityQuestion: Property = Property(name="securityQuestion", type=StringType)
Login_lastLoginTime: Property = Property(name="lastLoginTime", type=DateType)
Login.attributes={Login_securityQuestion, Login_username, Login_lastLoginTime, Login_password, Login_securityAnswer}

# transaction_Transaction class attributes and methods
transaction_Transaction_id: Property = Property(name="id", type=IntegerType)
transaction_Transaction_type: Property = Property(name="type", type=transaction_TransactionType)
transaction_Transaction_transactionTime: Property = Property(name="transactionTime", type=DateType)
transaction_Transaction_amount: Property = Property(name="amount", type=FloatType)
transaction_Transaction.attributes={transaction_Transaction_transactionTime, transaction_Transaction_type, transaction_Transaction_id, transaction_Transaction_amount}

# transaction_DepositTransaction class attributes and methods

# transaction_WithdrawTransaction class attributes and methods

# transaction_TransferTransaction class attributes and methods
transaction_TransferTransaction_targetAccount: Property = Property(name="targetAccount", type=account_Account)
transaction_TransferTransaction_sourceAccount: Property = Property(name="sourceAccount", type=account_Account)
transaction_TransferTransaction.attributes={transaction_TransferTransaction_sourceAccount, transaction_TransferTransaction_targetAccount}

# account_SavingsAccount class attributes and methods
account_SavingsAccount_interestRate: Property = Property(name="interestRate", type=FloatType)
account_SavingsAccount.attributes={account_SavingsAccount_interestRate}

# account_CertificatesOfDepositAccount class attributes and methods
account_CertificatesOfDepositAccount_timePeriod: Property = Property(name="timePeriod", type=IntegerType)
account_CertificatesOfDepositAccount_interestRate: Property = Property(name="interestRate", type=FloatType)
account_CertificatesOfDepositAccount.attributes={account_CertificatesOfDepositAccount_timePeriod, account_CertificatesOfDepositAccount_interestRate}

# account_CheckingAccount class attributes and methods
account_CheckingAccount_name: Property = Property(name="name", type=StringType)
account_CheckingAccount.attributes={account_CheckingAccount_name}

# account_Account class attributes and methods
account_Account_accountNo: Property = Property(name="accountNo", type=StringType)
account_Account_type: Property = Property(name="type", type=account_AccountType)
account_Account_balance: Property = Property(name="balance", type=FloatType)
account_Account.attributes={account_Account_type, account_Account_balance, account_Account_accountNo}

# Relationships
association2: BinaryAssociation = BinaryAssociation(
    name="association2",
    ends={
        Property(name="customer0", type=Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="a1", type=account_Account, multiplicity=Multiplicity(1, 9999))
    }
)
Account_Transaction: BinaryAssociation = BinaryAssociation(
    name="Account_Transaction",
    ends={
        Property(name="transactions2", type=transaction_Transaction, multiplicity=Multiplicity(0, 9999)),
        Property(name="account3", type=account_Account, multiplicity=Multiplicity(1, 1))
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
    name="c252cbac_76f7_490e_a264_e543743046ad",
    types={Customer, Login, transaction_Transaction, transaction_DepositTransaction, transaction_WithdrawTransaction, transaction_TransferTransaction, account_SavingsAccount, account_CertificatesOfDepositAccount, account_CheckingAccount, account_Account, transaction_TransactionType, account_AccountType},
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