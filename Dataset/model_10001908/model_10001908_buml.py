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
OnlineBanking_AppConfig = Class(name="OnlineBanking_AppConfig")
data_CustomerProfileRepository = Class(name="data_CustomerProfileRepository")
model_Account = Class(name="model_Account", is_abstract=True)
model_AccountAction = Class(name="model_AccountAction")
model_AccountChain_Interface = Class(name="model_AccountChain_Interface")
model_AccountHandler = Class(name="model_AccountHandler")
model_Bank = Class(name="model_Bank")
model_CheckingAccount = Class(name="model_CheckingAccount")
model_CloseAccount = Class(name="model_CloseAccount")
model_CreditAccount = Class(name="model_CreditAccount")
model_Customer = Class(name="model_Customer")
model_Deposit = Class(name="model_Deposit")
model_Loan = Class(name="model_Loan")
model_MakePayment = Class(name="model_MakePayment")
model_OpenAccount = Class(name="model_OpenAccount")
model_SavingsAccount = Class(name="model_SavingsAccount")
model_Transaction = Class(name="model_Transaction")
model_Withdrawal = Class(name="model_Withdrawal")
TestAccountChain = Class(name="TestAccountChain")
genmymodelreverse_org_springframework_ui_Model_Interface = Class(name="genmymodelreverse_org_springframework_ui_Model_Interface", is_abstract=True)
genmymodelreverse_java_util_HashMap = Class(name="genmymodelreverse_java_util_HashMap")
genmymodelreverse_C1 = Class(name="genmymodelreverse_C1")
genmymodelreverse_C2 = Class(name="genmymodelreverse_C2")
genmymodelreverse_java_util_Date = Class(name="genmymodelreverse_java_util_Date")

# OnlineBanking_AppConfig class attributes and methods

# data_CustomerProfileRepository class attributes and methods
data_CustomerProfileRepository_numAccounts: Property = Property(name="numAccounts", type=IntegerType)
data_CustomerProfileRepository_customerProfiles: Property = Property(name="customerProfiles", type=StringType)
data_CustomerProfileRepository.attributes={data_CustomerProfileRepository_customerProfiles, data_CustomerProfileRepository_numAccounts}

# model_Account class attributes and methods
model_Account_customerId: Property = Property(name="customerId", type=IntegerType)
model_Account_accountNumber: Property = Property(name="accountNumber", type=IntegerType)
model_Account_balance: Property = Property(name="balance", type=FloatType)
model_Account_type: Property = Property(name="type", type=StringType)
model_Account.attributes={model_Account_type, model_Account_balance, model_Account_accountNumber, model_Account_customerId}

# model_AccountAction class attributes and methods
model_AccountAction_action: Property = Property(name="action", type=StringType)
model_AccountAction_amount: Property = Property(name="amount", type=FloatType)
model_AccountAction_success: Property = Property(name="success", type=BooleanType)
model_AccountAction.attributes={model_AccountAction_action, model_AccountAction_amount, model_AccountAction_success}

# model_AccountChain_Interface class attributes and methods

# model_AccountHandler class attributes and methods

# model_Bank class attributes and methods
model_Bank_name: Property = Property(name="name", type=StringType)
model_Bank_address: Property = Property(name="address", type=StringType)
model_Bank_customerMap: Property = Property(name="customerMap", type=StringType)
model_Bank.attributes={model_Bank_name, model_Bank_customerMap, model_Bank_address}

# model_CheckingAccount class attributes and methods
model_CheckingAccount_interestRate: Property = Property(name="interestRate", type=FloatType)
model_CheckingAccount_type: Property = Property(name="type", type=StringType)
model_CheckingAccount.attributes={model_CheckingAccount_type, model_CheckingAccount_interestRate}

# model_CloseAccount class attributes and methods

# model_CreditAccount class attributes and methods
model_CreditAccount_minPayment: Property = Property(name="minPayment", type=FloatType)
model_CreditAccount_interestRate: Property = Property(name="interestRate", type=FloatType)
model_CreditAccount_paymentDueDate: Property = Property(name="paymentDueDate", type=StringType)
model_CreditAccount_type: Property = Property(name="type", type=StringType)
model_CreditAccount.attributes={model_CreditAccount_minPayment, model_CreditAccount_paymentDueDate, model_CreditAccount_interestRate, model_CreditAccount_type}

# model_Customer class attributes and methods
model_Customer_name: Property = Property(name="name", type=StringType)
model_Customer_address: Property = Property(name="address", type=StringType)
model_Customer_password: Property = Property(name="password", type=StringType)
model_Customer_dob: Property = Property(name="dob", type=StringType)
model_Customer_accounts: Property = Property(name="accounts", type=StringType)
model_Customer_username: Property = Property(name="username", type=StringType)
model_Customer_id: Property = Property(name="id", type=IntegerType)
model_Customer.attributes={model_Customer_password, model_Customer_accounts, model_Customer_name, model_Customer_address, model_Customer_dob, model_Customer_username, model_Customer_id}

# model_Deposit class attributes and methods

# model_Loan class attributes and methods
model_Loan_interestRate: Property = Property(name="interestRate", type=FloatType)
model_Loan_minPayment: Property = Property(name="minPayment", type=FloatType)
model_Loan_paymentDueDate: Property = Property(name="paymentDueDate", type=StringType)
model_Loan_type: Property = Property(name="type", type=StringType)
model_Loan.attributes={model_Loan_interestRate, model_Loan_paymentDueDate, model_Loan_minPayment, model_Loan_type}

# model_MakePayment class attributes and methods

# model_OpenAccount class attributes and methods

# model_SavingsAccount class attributes and methods
model_SavingsAccount_interestRate: Property = Property(name="interestRate", type=FloatType)
model_SavingsAccount_type: Property = Property(name="type", type=StringType)
model_SavingsAccount.attributes={model_SavingsAccount_type, model_SavingsAccount_interestRate}

# model_Transaction class attributes and methods
model_Transaction_date: Property = Property(name="date", type=genmymodelreverse_java_util_Date)
model_Transaction_ammount: Property = Property(name="ammount", type=FloatType)
model_Transaction.attributes={model_Transaction_ammount, model_Transaction_date}

# model_Withdrawal class attributes and methods

# TestAccountChain class attributes and methods

# genmymodelreverse_org_springframework_ui_Model_Interface class attributes and methods

# genmymodelreverse_java_util_HashMap class attributes and methods

# genmymodelreverse_C1 class attributes and methods

# genmymodelreverse_C2 class attributes and methods

# genmymodelreverse_java_util_Date class attributes and methods

# Relationships
Customer_Account: BinaryAssociation = BinaryAssociation(
    name="Customer_Account",
    ends={
        Property(name="owns0", type=model_Account, multiplicity=Multiplicity(0, 4)),
        Property(name="has1", type=model_Customer, multiplicity=Multiplicity(0, 1))
    }
)
Customer_AccountAction: BinaryAssociation = BinaryAssociation(
    name="Customer_AccountAction",
    ends={
        Property(name="requests2", type=model_AccountAction, multiplicity=Multiplicity(0, 9999)),
        Property(name="customer3", type=model_Customer, multiplicity=Multiplicity(0, 1))
    }
)
AccountChain_AccountChain: BinaryAssociation = BinaryAssociation(
    name="AccountChain_AccountChain",
    ends={
        Property(name="successor4", type=model_AccountChain_Interface, multiplicity=Multiplicity(0, 9999)),
        Property(name="AccountChain_AccountChain_15", type=model_AccountChain_Interface, multiplicity=Multiplicity(0, 1))
    }
)
Account_AccountAction: BinaryAssociation = BinaryAssociation(
    name="Account_AccountAction",
    ends={
        Property(name="accountAction6", type=model_AccountAction, multiplicity=Multiplicity(0, 9999)),
        Property(name="account7", type=model_Account, multiplicity=Multiplicity(0, 9999))
    }
)
next_OpenAccount_AccountChain_5: BinaryAssociation = BinaryAssociation(
    name="next_OpenAccount_AccountChain_5",
    ends={
        Property(name="openaccount8", type=model_OpenAccount, multiplicity=Multiplicity(0, 1)),
        Property(name="next9", type=model_AccountChain_Interface, multiplicity=Multiplicity(0, 1))
    }
)
next_MakePayment_AccountChain_3: BinaryAssociation = BinaryAssociation(
    name="next_MakePayment_AccountChain_3",
    ends={
        Property(name="makepayment10", type=model_MakePayment, multiplicity=Multiplicity(0, 1)),
        Property(name="next11", type=model_AccountChain_Interface, multiplicity=Multiplicity(0, 1))
    }
)
customer_Bank_Customer_6: BinaryAssociation = BinaryAssociation(
    name="customer_Bank_Customer_6",
    ends={
        Property(name="bank12", type=model_Bank, multiplicity=Multiplicity(0, 1)),
        Property(name="customer13", type=model_Customer, multiplicity=Multiplicity(0, 9999))
    }
)
account_Bank_Account_8: BinaryAssociation = BinaryAssociation(
    name="account_Bank_Account_8",
    ends={
        Property(name="bank14", type=model_Bank, multiplicity=Multiplicity(0, 1)),
        Property(name="accounts15", type=model_Account, multiplicity=Multiplicity(0, 9999))
    }
)
next_Withdrawal_AccountChain_1: BinaryAssociation = BinaryAssociation(
    name="next_Withdrawal_AccountChain_1",
    ends={
        Property(name="withdrawal16", type=model_Withdrawal, multiplicity=Multiplicity(0, 1)),
        Property(name="next17", type=model_AccountChain_Interface, multiplicity=Multiplicity(0, 1))
    }
)
next_CloseAccount_AccountChain_4: BinaryAssociation = BinaryAssociation(
    name="next_CloseAccount_AccountChain_4",
    ends={
        Property(name="closeaccount18", type=model_CloseAccount, multiplicity=Multiplicity(0, 1)),
        Property(name="next19", type=model_AccountChain_Interface, multiplicity=Multiplicity(0, 1))
    }
)
next_Deposit_AccountChain_2: BinaryAssociation = BinaryAssociation(
    name="next_Deposit_AccountChain_2",
    ends={
        Property(name="deposit20", type=model_Deposit, multiplicity=Multiplicity(0, 1)),
        Property(name="next21", type=model_AccountChain_Interface, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_c_I54PPYEeiy0d_yUThzLQ",
    types={OnlineBanking_AppConfig, data_CustomerProfileRepository, model_Account, model_AccountAction, model_AccountChain_Interface, model_AccountHandler, model_Bank, model_CheckingAccount, model_CloseAccount, model_CreditAccount, model_Customer, model_Deposit, model_Loan, model_MakePayment, model_OpenAccount, model_SavingsAccount, model_Transaction, model_Withdrawal, TestAccountChain, genmymodelreverse_org_springframework_ui_Model_Interface, genmymodelreverse_java_util_HashMap, genmymodelreverse_C1, genmymodelreverse_C2, genmymodelreverse_java_util_Date},
    associations={Customer_Account, Customer_AccountAction, AccountChain_AccountChain, Account_AccountAction, next_OpenAccount_AccountChain_5, next_MakePayment_AccountChain_3, customer_Bank_Customer_6, account_Bank_Account_8, next_Withdrawal_AccountChain_1, next_CloseAccount_AccountChain_4, next_Deposit_AccountChain_2},
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