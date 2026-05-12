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

loan_ApplicationStatus: Enumeration = Enumeration(
    name="loan_ApplicationStatus",
    literals={
            
    }
)

loan_LoanType: Enumeration = Enumeration(
    name="loan_LoanType",
    literals={
            
    }
)

loan_LoanStatus: Enumeration = Enumeration(
    name="loan_LoanStatus",
    literals={
            
    }
)

TransactionType: Enumeration = Enumeration(
    name="TransactionType",
    literals={
            
    }
)

# Classes
Profile = Class(name="Profile")
User = Class(name="User")
transaction_Transaction = Class(name="transaction_Transaction")
transaction_DepositTransaction = Class(name="transaction_DepositTransaction")
transaction_TransferTransaction = Class(name="transaction_TransferTransaction")
transaction_PaybillsTransaction = Class(name="transaction_PaybillsTransaction")
transaction_ExternalAccount = Class(name="transaction_ExternalAccount")
transaction_Payee = Class(name="transaction_Payee")
transaction_LoanPayment = Class(name="transaction_LoanPayment")
account_SavingsAccount = Class(name="account_SavingsAccount")
account_Account = Class(name="account_Account")
loan_LoanApplication = Class(name="loan_LoanApplication")
loan_Loan = Class(name="loan_Loan")
loan_LoanApplicationFile = Class(name="loan_LoanApplicationFile")
String = Class(name="String")
Account = Class(name="Account")
Transaction = Class(name="Transaction")
Transaction2 = Class(name="Transaction2")
Account1 = Class(name="Account1")
Transaction1 = Class(name="Transaction1")
Account2 = Class(name="Account2")
Transaction3 = Class(name="Transaction3")
TransferTransaction = Class(name="TransferTransaction")
ExternalAccount = Class(name="ExternalAccount")

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
Profile.attributes={Profile_phoneNumber, Profile_IDNum, Profile_address2, Profile_address1, Profile_dateOfBirth, Profile_city, Profile_zipcode, Profile_userID, Profile_email, Profile_lastname, Profile_country, Profile_state, Profile_firstname, Profile_IDType}

# User class attributes and methods
User_userID: Property = Property(name="userID", type=StringType)
User_username: Property = Property(name="username", type=StringType)
User_password: Property = Property(name="password", type=StringType)
User_lastLoginTime: Property = Property(name="lastLoginTime", type=StringType)
User.attributes={User_lastLoginTime, User_username, User_password, User_userID}

# transaction_Transaction class attributes and methods
transaction_Transaction_transactionID: Property = Property(name="transactionID", type=StringType)
transaction_Transaction_type: Property = Property(name="type", type=transaction_TransactionType)
transaction_Transaction_time: Property = Property(name="time", type=StringType)
transaction_Transaction_amount: Property = Property(name="amount", type=FloatType)
transaction_Transaction_sourceAccountNum: Property = Property(name="sourceAccountNum", type=StringType)
transaction_Transaction_destinationAccountNum: Property = Property(name="destinationAccountNum", type=StringType)
transaction_Transaction_description: Property = Property(name="description", type=StringType)
transaction_Transaction_comment: Property = Property(name="comment", type=StringType)
transaction_Transaction.attributes={transaction_Transaction_amount, transaction_Transaction_transactionID, transaction_Transaction_type, transaction_Transaction_time, transaction_Transaction_destinationAccountNum, transaction_Transaction_comment, transaction_Transaction_description, transaction_Transaction_sourceAccountNum}

# transaction_DepositTransaction class attributes and methods

# transaction_TransferTransaction class attributes and methods

# transaction_PaybillsTransaction class attributes and methods

# transaction_ExternalAccount class attributes and methods
transaction_ExternalAccount_routingNum: Property = Property(name="routingNum", type=StringType)
transaction_ExternalAccount_accountNum: Property = Property(name="accountNum", type=StringType)
transaction_ExternalAccount_associatedAccount: Property = Property(name="associatedAccount", type=StringType)
transaction_ExternalAccount.attributes={transaction_ExternalAccount_accountNum, transaction_ExternalAccount_routingNum, transaction_ExternalAccount_associatedAccount}

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
transaction_Payee_userID: Property = Property(name="userID", type=StringType)
transaction_Payee.attributes={transaction_Payee_address2, transaction_Payee_accountNum, transaction_Payee_address1, transaction_Payee_zipcode, transaction_Payee_name, transaction_Payee_email, transaction_Payee_state, transaction_Payee_country, transaction_Payee_city, transaction_Payee_userID, transaction_Payee_phoneNum}

# transaction_LoanPayment class attributes and methods
transaction_LoanPayment_principal: Property = Property(name="principal", type=FloatType)
transaction_LoanPayment_interest: Property = Property(name="interest", type=FloatType)
transaction_LoanPayment_loanID: Property = Property(name="loanID", type=StringType)
transaction_LoanPayment.attributes={transaction_LoanPayment_principal, transaction_LoanPayment_loanID, transaction_LoanPayment_interest}

# account_SavingsAccount class attributes and methods
account_SavingsAccount_interestRate: Property = Property(name="interestRate", type=FloatType)
account_SavingsAccount.attributes={account_SavingsAccount_interestRate}

# account_Account class attributes and methods
account_Account_userID: Property = Property(name="userID", type=StringType)
account_Account_accountNum: Property = Property(name="accountNum", type=StringType)
account_Account_type: Property = Property(name="type", type=account_AccountType)
account_Account_pin: Property = Property(name="pin", type=StringType)
account_Account_balance: Property = Property(name="balance", type=FloatType)
account_Account.attributes={account_Account_pin, account_Account_userID, account_Account_accountNum, account_Account_balance, account_Account_type}

# loan_LoanApplication class attributes and methods
loan_LoanApplication_applicationID: Property = Property(name="applicationID", type=StringType)
loan_LoanApplication_amount: Property = Property(name="amount", type=FloatType)
loan_LoanApplication_term: Property = Property(name="term", type=IntegerType)
loan_LoanApplication_interestRate: Property = Property(name="interestRate", type=FloatType)
loan_LoanApplication_status: Property = Property(name="status", type=loan_ApplicationStatus)
loan_LoanApplication_submissionTime: Property = Property(name="submissionTime", type=StringType)
loan_LoanApplication_type: Property = Property(name="type", type=loan_LoanType)
loan_LoanApplication_userID: Property = Property(name="userID", type=StringType)
loan_LoanApplication.attributes={loan_LoanApplication_submissionTime, loan_LoanApplication_amount, loan_LoanApplication_applicationID, loan_LoanApplication_type, loan_LoanApplication_interestRate, loan_LoanApplication_status, loan_LoanApplication_term, loan_LoanApplication_userID}

# loan_Loan class attributes and methods
loan_Loan_loanID: Property = Property(name="loanID", type=StringType)
loan_Loan_amount: Property = Property(name="amount", type=FloatType)
loan_Loan_term: Property = Property(name="term", type=IntegerType)
loan_Loan_interestRate: Property = Property(name="interestRate", type=FloatType)
loan_Loan_status: Property = Property(name="status", type=loan_ApplicationStatus)
loan_Loan_submissionTime: Property = Property(name="submissionTime", type=StringType)
loan_Loan_type: Property = Property(name="type", type=loan_LoanStatus)
loan_Loan_userID: Property = Property(name="userID", type=StringType)
loan_Loan.attributes={loan_Loan_loanID, loan_Loan_interestRate, loan_Loan_status, loan_Loan_submissionTime, loan_Loan_amount, loan_Loan_term, loan_Loan_type, loan_Loan_userID}

# loan_LoanApplicationFile class attributes and methods
loan_LoanApplicationFile_fileID: Property = Property(name="fileID", type=StringType)
loan_LoanApplicationFile_applicationID: Property = Property(name="applicationID", type=StringType)
loan_LoanApplicationFile.attributes={loan_LoanApplicationFile_applicationID, loan_LoanApplicationFile_fileID}

# String class attributes and methods

# Account class attributes and methods
Account_userID: Property = Property(name="userID", type=StringType)
Account_accountNum: Property = Property(name="accountNum", type=StringType)
Account_type: Property = Property(name="type", type=account_AccountType)
Account_pin: Property = Property(name="pin", type=StringType)
Account_balance: Property = Property(name="balance", type=FloatType)
Account.attributes={Account_balance, Account_pin, Account_type, Account_userID, Account_accountNum}

# Transaction class attributes and methods
Transaction_transactionID: Property = Property(name="transactionID", type=StringType)
Transaction_type: Property = Property(name="type", type=transaction_TransactionType)
Transaction_time: Property = Property(name="time", type=StringType)
Transaction_amount: Property = Property(name="amount", type=FloatType)
Transaction_sourceAccountNum: Property = Property(name="sourceAccountNum", type=StringType)
Transaction_destinationAccountNum: Property = Property(name="destinationAccountNum", type=StringType)
Transaction_description: Property = Property(name="description", type=StringType)
Transaction_comment: Property = Property(name="comment", type=StringType)
Transaction.attributes={Transaction_sourceAccountNum, Transaction_comment, Transaction_time, Transaction_description, Transaction_destinationAccountNum, Transaction_amount, Transaction_type, Transaction_transactionID}

# Transaction2 class attributes and methods
Transaction2_type: Property = Property(name="type", type=transaction_TransactionType)
Transaction2_time: Property = Property(name="time", type=StringType)
Transaction2_amount: Property = Property(name="amount", type=FloatType)
Transaction2_sourceAccountNum: Property = Property(name="sourceAccountNum", type=StringType)
Transaction2_destinationAccountNum: Property = Property(name="destinationAccountNum", type=StringType)
Transaction2_description: Property = Property(name="description", type=StringType)
Transaction2_comment: Property = Property(name="comment", type=StringType)
Transaction2_transactionID: Property = Property(name="transactionID", type=StringType)
Transaction2.attributes={Transaction2_time, Transaction2_comment, Transaction2_transactionID, Transaction2_type, Transaction2_description, Transaction2_sourceAccountNum, Transaction2_destinationAccountNum, Transaction2_amount}

# Account1 class attributes and methods
Account1_userID: Property = Property(name="userID", type=StringType)
Account1_accountNum: Property = Property(name="accountNum", type=StringType)
Account1_type: Property = Property(name="type", type=account_AccountType)
Account1_pin: Property = Property(name="pin", type=StringType)
Account1_balance: Property = Property(name="balance", type=FloatType)
Account1.attributes={Account1_type, Account1_balance, Account1_pin, Account1_accountNum, Account1_userID}

# Transaction1 class attributes and methods
Transaction1_transactionID: Property = Property(name="transactionID", type=StringType)
Transaction1_type: Property = Property(name="type", type=transaction_TransactionType)
Transaction1_time: Property = Property(name="time", type=StringType)
Transaction1_amount: Property = Property(name="amount", type=FloatType)
Transaction1_sourceAccountNum: Property = Property(name="sourceAccountNum", type=StringType)
Transaction1_destinationAccountNum: Property = Property(name="destinationAccountNum", type=StringType)
Transaction1_description: Property = Property(name="description", type=StringType)
Transaction1_comment: Property = Property(name="comment", type=StringType)
Transaction1.attributes={Transaction1_transactionID, Transaction1_sourceAccountNum, Transaction1_amount, Transaction1_description, Transaction1_time, Transaction1_comment, Transaction1_destinationAccountNum, Transaction1_type}

# Account2 class attributes and methods
Account2_userID: Property = Property(name="userID", type=StringType)
Account2_accountNum: Property = Property(name="accountNum", type=StringType)
Account2_type: Property = Property(name="type", type=account_AccountType)
Account2_pin: Property = Property(name="pin", type=StringType)
Account2_balance: Property = Property(name="balance", type=FloatType)
Account2.attributes={Account2_accountNum, Account2_type, Account2_pin, Account2_userID, Account2_balance}

# Transaction3 class attributes and methods
Transaction3_amount: Property = Property(name="amount", type=FloatType)
Transaction3_sourceAccountNum: Property = Property(name="sourceAccountNum", type=StringType)
Transaction3_destinationAccountNum: Property = Property(name="destinationAccountNum", type=StringType)
Transaction3_description: Property = Property(name="description", type=StringType)
Transaction3_comment: Property = Property(name="comment", type=StringType)
Transaction3_transactionID: Property = Property(name="transactionID", type=StringType)
Transaction3_type: Property = Property(name="type", type=transaction_TransactionType)
Transaction3_time: Property = Property(name="time", type=StringType)
Transaction3.attributes={Transaction3_sourceAccountNum, Transaction3_description, Transaction3_destinationAccountNum, Transaction3_type, Transaction3_comment, Transaction3_transactionID, Transaction3_amount, Transaction3_time}

# TransferTransaction class attributes and methods

# ExternalAccount class attributes and methods
ExternalAccount_routingNum: Property = Property(name="routingNum", type=StringType)
ExternalAccount_accountNum: Property = Property(name="accountNum", type=StringType)
ExternalAccount_associatedAccount: Property = Property(name="associatedAccount", type=StringType)
ExternalAccount.attributes={ExternalAccount_routingNum, ExternalAccount_associatedAccount, ExternalAccount_accountNum}

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
LoanApplication_LoanApplicationFile: BinaryAssociation = BinaryAssociation(
    name="LoanApplication_LoanApplicationFile",
    ends={
        Property(name="loanApplicationFile10", type=loan_LoanApplicationFile, multiplicity=Multiplicity(0, 5)),
        Property(name="loanApplication11", type=loan_LoanApplication, multiplicity=Multiplicity(1, 1))
    }
)
LoanApplication_Loan: BinaryAssociation = BinaryAssociation(
    name="LoanApplication_Loan",
    ends={
        Property(name="loan12", type=loan_Loan, multiplicity=Multiplicity(0, 1)),
        Property(name="loanApplication13", type=loan_LoanApplication, multiplicity=Multiplicity(0, 1))
    }
)
Profile_LoanApplication: BinaryAssociation = BinaryAssociation(
    name="Profile_LoanApplication",
    ends={
        Property(name="loanApplication14", type=loan_LoanApplication, multiplicity=Multiplicity(0, 9999)),
        Property(name="profile15", type=Profile, multiplicity=Multiplicity(1, 1))
    }
)
Transaction_Account1: BinaryAssociation = BinaryAssociation(
    name="Transaction_Account1",
    ends={
        Property(name="account16", type=Account1, multiplicity=Multiplicity(0, 1)),
        Property(name="transaction17", type=Transaction1, multiplicity=Multiplicity(0, 9999))
    }
)
Transaction_Account2: BinaryAssociation = BinaryAssociation(
    name="Transaction_Account2",
    ends={
        Property(name="account18", type=Account2, multiplicity=Multiplicity(0, 1)),
        Property(name="transaction19", type=Transaction3, multiplicity=Multiplicity(0, 9999))
    }
)
ExternalAccount_TransferTransaction: BinaryAssociation = BinaryAssociation(
    name="ExternalAccount_TransferTransaction",
    ends={
        Property(name="transferTransaction20", type=TransferTransaction, multiplicity=Multiplicity(0, 9999)),
        Property(name="externalAccount21", type=ExternalAccount, multiplicity=Multiplicity(0, 1))
    }
)
ExternalAccount_Account: BinaryAssociation = BinaryAssociation(
    name="ExternalAccount_Account",
    ends={
        Property(name="account22", type=Account2, multiplicity=Multiplicity(1, 1)),
        Property(name="externalAccount23", type=ExternalAccount, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_57f9c904_78c4_4787_a7b7_65b46f1251d3",
    types={Profile, User, transaction_Transaction, transaction_DepositTransaction, transaction_TransferTransaction, transaction_PaybillsTransaction, transaction_ExternalAccount, transaction_Payee, transaction_LoanPayment, account_SavingsAccount, account_Account, loan_LoanApplication, loan_Loan, loan_LoanApplicationFile, String, Account, Transaction, Transaction2, Account1, Transaction1, Account2, Transaction3, TransferTransaction, ExternalAccount, transaction_TransactionType, account_AccountType, loan_ApplicationStatus, loan_LoanType, loan_LoanStatus, TransactionType},
    associations={Transaction_Account, TransferTransaction_ExternalAccount, PaybillsTransaction_Payee, Profile_User, Profile_Account, LoanApplication_LoanApplicationFile, LoanApplication_Loan, Profile_LoanApplication, Transaction_Account1, Transaction_Account2, ExternalAccount_TransferTransaction, ExternalAccount_Account},
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