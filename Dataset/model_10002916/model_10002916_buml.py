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
LOGIN = Class(name="LOGIN")
RequestOTPAuthentication = Class(name="RequestOTPAuthentication")
Authentication = Class(name="Authentication")
LoginAuthenticationProcessor = Class(name="LoginAuthenticationProcessor")
Database = Class(name="Database")
OPT_AuthenticationProcessor = Class(name="OPT_AuthenticationProcessor")

# Customer class attributes and methods
Customer_name: Property = Property(name="name", type=StringType)
Customer_dateOfBirth: Property = Property(name="dateOfBirth", type=DateType)
Customer_address: Property = Property(name="address", type=StringType)
Customer_phoneNumber: Property = Property(name="phoneNumber", type=StringType)
Customer_emailAddress: Property = Property(name="emailAddress", type=StringType)
Customer.attributes={Customer_address, Customer_phoneNumber, Customer_dateOfBirth, Customer_emailAddress, Customer_name}

# Login class attributes and methods
Login_username: Property = Property(name="username", type=StringType)
Login_securityAnswer: Property = Property(name="securityAnswer", type=StringType)
Login_password: Property = Property(name="password", type=StringType)
Login_securityQuestion: Property = Property(name="securityQuestion", type=StringType)
Login_lastLoginTime: Property = Property(name="lastLoginTime", type=DateType)
Login.attributes={Login_username, Login_securityAnswer, Login_password, Login_securityQuestion, Login_lastLoginTime}

# transaction_Transaction class attributes and methods
transaction_Transaction_amount: Property = Property(name="amount", type=FloatType)
transaction_Transaction_id: Property = Property(name="id", type=IntegerType)
transaction_Transaction_type: Property = Property(name="type", type=transaction_TransactionType)
transaction_Transaction_transactionTime: Property = Property(name="transactionTime", type=DateType)
transaction_Transaction.attributes={transaction_Transaction_id, transaction_Transaction_amount, transaction_Transaction_transactionTime, transaction_Transaction_type}

# transaction_DepositTransaction class attributes and methods

# transaction_WithdrawTransaction class attributes and methods

# transaction_TransferTransaction class attributes and methods
transaction_TransferTransaction_targetAccount: Property = Property(name="targetAccount", type=account_Account)
transaction_TransferTransaction_sourceAccount: Property = Property(name="sourceAccount", type=account_Account)
transaction_TransferTransaction.attributes={transaction_TransferTransaction_targetAccount, transaction_TransferTransaction_sourceAccount}

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
account_Account.attributes={account_Account_balance, account_Account_type, account_Account_accountNo}

# LOGIN class attributes and methods
LOGIN_UserID: Property = Property(name="UserID", type=StringType)
LOGIN_UserPassWord: Property = Property(name="UserPassWord", type=StringType)
LOGIN.attributes={LOGIN_UserID, LOGIN_UserPassWord}

# RequestOTPAuthentication class attributes and methods
RequestOTPAuthentication_UserID: Property = Property(name="UserID", type=StringType)
RequestOTPAuthentication_UserEmail: Property = Property(name="UserEmail", type=StringType)
RequestOTPAuthentication.attributes={RequestOTPAuthentication_UserEmail, RequestOTPAuthentication_UserID}

# Authentication class attributes and methods
Authentication_UserID: Property = Property(name="UserID", type=StringType)
Authentication_UserPassWord: Property = Property(name="UserPassWord", type=StringType)
Authentication_UserEmail: Property = Property(name="UserEmail", type=StringType)
Authentication_Authentication_Result: Property = Property(name="Authentication_Result", type=BooleanType)
Authentication_AuthenticationType: Property = Property(name="AuthenticationType", type=IntegerType)
Authentication_UserPassWord1: Property = Property(name="UserPassWord1", type=StringType)
Authentication.attributes={Authentication_UserEmail, Authentication_Authentication_Result, Authentication_UserID, Authentication_AuthenticationType, Authentication_UserPassWord1, Authentication_UserPassWord}

# LoginAuthenticationProcessor class attributes and methods
LoginAuthenticationProcessor_UserPassWord: Property = Property(name="UserPassWord", type=StringType)
LoginAuthenticationProcessor_UserID: Property = Property(name="UserID", type=StringType)
LoginAuthenticationProcessor_Authentication_Result: Property = Property(name="Authentication_Result", type=BooleanType)
LoginAuthenticationProcessor.attributes={LoginAuthenticationProcessor_UserID, LoginAuthenticationProcessor_Authentication_Result, LoginAuthenticationProcessor_UserPassWord}

# Database class attributes and methods

# OPT_AuthenticationProcessor class attributes and methods
OPT_AuthenticationProcessor_UserEmail: Property = Property(name="UserEmail", type=StringType)
OPT_AuthenticationProcessor_Authentication_Result: Property = Property(name="Authentication_Result", type=BooleanType)
OPT_AuthenticationProcessor.attributes={OPT_AuthenticationProcessor_Authentication_Result, OPT_AuthenticationProcessor_UserEmail}

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
Database_Authentication: BinaryAssociation = BinaryAssociation(
    name="Database_Authentication",
    ends={
        Property(name="authentication6", type=Authentication, multiplicity=Multiplicity(0, 1)),
        Property(name="database7", type=Database, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="e94abfa1_bb1b_4fb8_8488_eff4882e50e5",
    types={Customer, Login, transaction_Transaction, transaction_DepositTransaction, transaction_WithdrawTransaction, transaction_TransferTransaction, account_SavingsAccount, account_CertificatesOfDepositAccount, account_CheckingAccount, account_Account, LOGIN, RequestOTPAuthentication, Authentication, LoginAuthenticationProcessor, Database, OPT_AuthenticationProcessor, transaction_TransactionType, account_AccountType},
    associations={association2, Account_Transaction, Customer_Login, Database_Authentication},
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