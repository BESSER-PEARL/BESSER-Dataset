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
transaction_TransferTransaction = Class(name="transaction_TransferTransaction")
transaction_PaybillsTransaction = Class(name="transaction_PaybillsTransaction")
transaction_ExternalAccount = Class(name="transaction_ExternalAccount")
transaction_Payee = Class(name="transaction_Payee")
account_SavingsAccount = Class(name="account_SavingsAccount")
account_Account = Class(name="account_Account")
Profile = Class(name="Profile")
User = Class(name="User")
transaction_Transaction = Class(name="transaction_Transaction")
transaction_DepositTransaction = Class(name="transaction_DepositTransaction")

# transaction_TransferTransaction class attributes and methods

# transaction_PaybillsTransaction class attributes and methods

# transaction_ExternalAccount class attributes and methods
transaction_ExternalAccount_routingNum: Property = Property(name="routingNum", type=StringType)
transaction_ExternalAccount_accountNum: Property = Property(name="accountNum", type=StringType)
transaction_ExternalAccount_associatedAccount: Property = Property(name="associatedAccount", type=StringType)
transaction_ExternalAccount.attributes={transaction_ExternalAccount_routingNum, transaction_ExternalAccount_accountNum, transaction_ExternalAccount_associatedAccount}

# transaction_Payee class attributes and methods
transaction_Payee_accountNum: Property = Property(name="accountNum", type=StringType)
transaction_Payee_name: Property = Property(name="name", type=StringType)
transaction_Payee_address1: Property = Property(name="address1", type=StringType)
transaction_Payee_address2: Property = Property(name="address2", type=StringType)
transaction_Payee_city: Property = Property(name="city", type=StringType)
transaction_Payee_state: Property = Property(name="state", type=StringType)
transaction_Payee_country: Property = Property(name="country", type=StringType)
transaction_Payee_zipcode: Property = Property(name="zipcode", type=StringType)
transaction_Payee_phoneNum: Property = Property(name="phoneNum", type=StringType)
transaction_Payee_email: Property = Property(name="email", type=StringType)
transaction_Payee.attributes={transaction_Payee_accountNum, transaction_Payee_country, transaction_Payee_state, transaction_Payee_address1, transaction_Payee_email, transaction_Payee_address2, transaction_Payee_phoneNum, transaction_Payee_city, transaction_Payee_zipcode, transaction_Payee_name}

# account_SavingsAccount class attributes and methods
account_SavingsAccount_interestRate: Property = Property(name="interestRate", type=FloatType)
account_SavingsAccount.attributes={account_SavingsAccount_interestRate}

# account_Account class attributes and methods
account_Account_userID: Property = Property(name="userID", type=StringType)
account_Account_accountNum: Property = Property(name="accountNum", type=StringType)
account_Account_type: Property = Property(name="type", type=account_AccountType)
account_Account_pin: Property = Property(name="pin", type=StringType)
account_Account_balance: Property = Property(name="balance", type=FloatType)
account_Account.attributes={account_Account_balance, account_Account_accountNum, account_Account_pin, account_Account_userID, account_Account_type}

# Profile class attributes and methods
Profile_userID: Property = Property(name="userID", type=StringType)
Profile_firstname: Property = Property(name="firstname", type=StringType)
Profile_lastname: Property = Property(name="lastname", type=StringType)
Profile_dateOfBirth: Property = Property(name="dateOfBirth", type=DateType)
Profile_address1: Property = Property(name="address1", type=StringType)
Profile_address2: Property = Property(name="address2", type=StringType)
Profile_city: Property = Property(name="city", type=StringType)
Profile_state: Property = Property(name="state", type=StringType)
Profile_country: Property = Property(name="country", type=StringType)
Profile_zipcode: Property = Property(name="zipcode", type=StringType)
Profile_phoneNumber: Property = Property(name="phoneNumber", type=StringType)
Profile_email: Property = Property(name="email", type=StringType)
Profile_IDType: Property = Property(name="IDType", type=IntegerType)
Profile_IDNum: Property = Property(name="IDNum", type=StringType)
Profile.attributes={Profile_firstname, Profile_city, Profile_email, Profile_IDType, Profile_zipcode, Profile_address2, Profile_address1, Profile_dateOfBirth, Profile_state, Profile_phoneNumber, Profile_IDNum, Profile_userID, Profile_country, Profile_lastname}

# User class attributes and methods
User_userID: Property = Property(name="userID", type=StringType)
User_username: Property = Property(name="username", type=StringType)
User_password: Property = Property(name="password", type=StringType)
User_lastLoginTime: Property = Property(name="lastLoginTime", type=StringType)
User.attributes={User_userID, User_lastLoginTime, User_password, User_username}

# transaction_Transaction class attributes and methods
transaction_Transaction_transactionID: Property = Property(name="transactionID", type=StringType)
transaction_Transaction_type: Property = Property(name="type", type=transaction_TransactionType)
transaction_Transaction_time: Property = Property(name="time", type=StringType)
transaction_Transaction_amount: Property = Property(name="amount", type=FloatType)
transaction_Transaction_sourceAccountNum: Property = Property(name="sourceAccountNum", type=StringType)
transaction_Transaction_destinationAccountNum: Property = Property(name="destinationAccountNum", type=StringType)
transaction_Transaction_description: Property = Property(name="description", type=StringType)
transaction_Transaction_comment: Property = Property(name="comment", type=StringType)
transaction_Transaction.attributes={transaction_Transaction_time, transaction_Transaction_amount, transaction_Transaction_description, transaction_Transaction_transactionID, transaction_Transaction_sourceAccountNum, transaction_Transaction_destinationAccountNum, transaction_Transaction_comment, transaction_Transaction_type}

# transaction_DepositTransaction class attributes and methods

# Relationships
Transaction_Account: BinaryAssociation = BinaryAssociation(
    name="Transaction_Account",
    ends={
        Property(name="account0", type=account_Account, multiplicity=Multiplicity(0, 1)),
        Property(name="transaction1", type=transaction_Transaction, multiplicity=Multiplicity(0, 9999))
    }
)
TransferTransaction_ExternalAccount: BinaryAssociation = BinaryAssociation(
    name="TransferTransaction_ExternalAccount",
    ends={
        Property(name="externalAccount2", type=transaction_ExternalAccount, multiplicity=Multiplicity(0, 1)),
        Property(name="transferTransaction3", type=transaction_TransferTransaction, multiplicity=Multiplicity(0, 9999))
    }
)
PaybillsTransaction_Payee: BinaryAssociation = BinaryAssociation(
    name="PaybillsTransaction_Payee",
    ends={
        Property(name="payee4", type=transaction_Payee, multiplicity=Multiplicity(0, 1)),
        Property(name="paybillsTransaction5", type=transaction_PaybillsTransaction, multiplicity=Multiplicity(0, 9999))
    }
)
Profile_User: BinaryAssociation = BinaryAssociation(
    name="Profile_User",
    ends={
        Property(name="user6", type=User, multiplicity=Multiplicity(0, 1)),
        Property(name="profile7", type=Profile, multiplicity=Multiplicity(0, 1))
    }
)
Profile_Account: BinaryAssociation = BinaryAssociation(
    name="Profile_Account",
    ends={
        Property(name="account8", type=account_Account, multiplicity=Multiplicity(0, 9999)),
        Property(name="profile9", type=Profile, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_9728eaef_2cc7_4562_ab25_78d2c1bbdefd",
    types={transaction_TransferTransaction, transaction_PaybillsTransaction, transaction_ExternalAccount, transaction_Payee, account_SavingsAccount, account_Account, Profile, User, transaction_Transaction, transaction_DepositTransaction, transaction_TransactionType, account_AccountType},
    associations={Transaction_Account, TransferTransaction_ExternalAccount, PaybillsTransaction_Payee, Profile_User, Profile_Account},
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