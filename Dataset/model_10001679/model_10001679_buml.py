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
Bank = Class(name="Bank")
Customer = Class(name="Customer")
Account = Class(name="Account")
ATM = Class(name="ATM")
ATMTransactions = Class(name="ATMTransactions")
CurrentAccount = Class(name="CurrentAccount")
SavingAccount = Class(name="SavingAccount")

# Bank class attributes and methods
Bank_code: Property = Property(name="code", type=IntegerType)
Bank_address: Property = Property(name="address", type=StringType)
Bank.attributes={Bank_address, Bank_code}

# Customer class attributes and methods
Customer_name: Property = Property(name="name", type=StringType)
Customer_address: Property = Property(name="address", type=StringType)
Customer_dob: Property = Property(name="dob", type=StringType)
Customer_cardno: Property = Property(name="cardno", type=IntegerType)
Customer_pin: Property = Property(name="pin", type=IntegerType)
Customer.attributes={Customer_dob, Customer_pin, Customer_name, Customer_address, Customer_cardno}

# Account class attributes and methods
Account_number: Property = Property(name="number", type=IntegerType)
Account_balance: Property = Property(name="balance", type=IntegerType)
Account.attributes={Account_balance, Account_number}

# ATM class attributes and methods
ATM_location: Property = Property(name="location", type=StringType)
ATM_managedBy: Property = Property(name="managedBy", type=StringType)
ATM.attributes={ATM_managedBy, ATM_location}

# ATMTransactions class attributes and methods
ATMTransactions_transactionid: Property = Property(name="transactionid", type=IntegerType)
ATMTransactions_date: Property = Property(name="date", type=StringType)
ATMTransactions_type: Property = Property(name="type", type=StringType)
ATMTransactions_amount: Property = Property(name="amount", type=IntegerType)
ATMTransactions_postBalance: Property = Property(name="postBalance", type=IntegerType)
ATMTransactions.attributes={ATMTransactions_type, ATMTransactions_amount, ATMTransactions_postBalance, ATMTransactions_date, ATMTransactions_transactionid}

# CurrentAccount class attributes and methods
CurrentAccount_accountNo: Property = Property(name="accountNo", type=IntegerType)
CurrentAccount_balance: Property = Property(name="balance", type=IntegerType)
CurrentAccount.attributes={CurrentAccount_accountNo, CurrentAccount_balance}

# SavingAccount class attributes and methods
SavingAccount_accountNo: Property = Property(name="accountNo", type=IntegerType)
SavingAccount_balance: Property = Property(name="balance", type=IntegerType)
SavingAccount.attributes={SavingAccount_accountNo, SavingAccount_balance}

# Relationships
Bank_ATM: BinaryAssociation = BinaryAssociation(
    name="Bank_ATM",
    ends={
        Property(name="aTM0", type=ATM, multiplicity=Multiplicity(0, 1)),
        Property(name="bank1", type=Bank, multiplicity=Multiplicity(0, 1))
    }
)
Bank_Account: BinaryAssociation = BinaryAssociation(
    name="Bank_Account",
    ends={
        Property(name="account2", type=Account, multiplicity=Multiplicity(0, 1)),
        Property(name="bank3", type=Bank, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Account: BinaryAssociation = BinaryAssociation(
    name="Customer_Account",
    ends={
        Property(name="account4", type=Account, multiplicity=Multiplicity(0, 1)),
        Property(name="customer5", type=Customer, multiplicity=Multiplicity(0, 1))
    }
)
Account_ATM_Transactions: BinaryAssociation = BinaryAssociation(
    name="Account_ATM_Transactions",
    ends={
        Property(name="ATMTransactions6", type=ATMTransactions, multiplicity=Multiplicity(0, 1)),
        Property(name="account7", type=Account, multiplicity=Multiplicity(0, 1))
    }
)
CurrentAccount_Saving_Account: BinaryAssociation = BinaryAssociation(
    name="CurrentAccount_Saving_Account",
    ends={
        Property(name="savingchecking8", type=SavingAccount, multiplicity=Multiplicity(0, 1)),
        Property(name="currentAccount9", type=CurrentAccount, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_OJLr4LGMEee6S77dw3LIvQ",
    types={Bank, Customer, Account, ATM, ATMTransactions, CurrentAccount, SavingAccount},
    associations={Bank_ATM, Bank_Account, Customer_Account, Account_ATM_Transactions, CurrentAccount_Saving_Account},
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