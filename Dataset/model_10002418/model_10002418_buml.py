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
BANK = Class(name="BANK")
Customer = Class(name="Customer")
Account = Class(name="Account")
ATM = Class(name="ATM")
ATM__Transactions = Class(name="ATM__Transactions")
Current_Account = Class(name="Current_Account")
Savings_Account = Class(name="Savings_Account")

# BANK class attributes and methods
BANK_Code: Property = Property(name="Code", type=StringType)
BANK_Address: Property = Property(name="Address", type=StringType)
BANK.attributes={BANK_Address, BANK_Code}

# Customer class attributes and methods
Customer_Name: Property = Property(name="Name", type=StringType)
Customer_Date_of_birth: Property = Property(name="Date_of_birth", type=StringType)
Customer_Pin: Property = Property(name="Pin", type=IntegerType)
Customer_Card_number: Property = Property(name="Card_number", type=IntegerType)
Customer.attributes={Customer_Pin, Customer_Card_number, Customer_Name, Customer_Date_of_birth}

# Account class attributes and methods
Account_AccountNumber: Property = Property(name="AccountNumber", type=IntegerType)
Account_Balance: Property = Property(name="Balance", type=IntegerType)
Account.attributes={Account_Balance, Account_AccountNumber}

# ATM class attributes and methods
ATM_location: Property = Property(name="location", type=StringType)
ATM_ManagedBy: Property = Property(name="ManagedBy", type=StringType)
ATM.attributes={ATM_location, ATM_ManagedBy}

# ATM__Transactions class attributes and methods
ATM__Transactions_Transaction_id: Property = Property(name="Transaction_id", type=StringType)
ATM__Transactions_Type: Property = Property(name="Type", type=StringType)
ATM__Transactions_Transaction_amount: Property = Property(name="Transaction_amount", type=IntegerType)
ATM__Transactions_Remaining_balance: Property = Property(name="Remaining_balance", type=IntegerType)
ATM__Transactions.attributes={ATM__Transactions_Type, ATM__Transactions_Remaining_balance, ATM__Transactions_Transaction_amount, ATM__Transactions_Transaction_id}

# Current_Account class attributes and methods
Current_Account_AccountNumber: Property = Property(name="AccountNumber", type=IntegerType)
Current_Account_Balance: Property = Property(name="Balance", type=IntegerType)
Current_Account.attributes={Current_Account_AccountNumber, Current_Account_Balance}

# Savings_Account class attributes and methods
Savings_Account_AccountNumber: Property = Property(name="AccountNumber", type=IntegerType)
Savings_Account_Balance: Property = Property(name="Balance", type=IntegerType)
Savings_Account.attributes={Savings_Account_AccountNumber, Savings_Account_Balance}

# Relationships
Account_ATM__Transactions: BinaryAssociation = BinaryAssociation(
    name="Account_ATM__Transactions",
    ends={
        Property(name="aTM__Transactions6", type=ATM__Transactions, multiplicity=Multiplicity(0, 1)),
        Property(name="account7", type=Account, multiplicity=Multiplicity(0, 1))
    }
)
Current_Account_Savings_Account: BinaryAssociation = BinaryAssociation(
    name="Current_Account_Savings_Account",
    ends={
        Property(name="savings_Account8", type=Savings_Account, multiplicity=Multiplicity(0, 1)),
        Property(name="current_Account9", type=Current_Account, multiplicity=Multiplicity(0, 1))
    }
)
BANK_ATM: BinaryAssociation = BinaryAssociation(
    name="BANK_ATM",
    ends={
        Property(name="aTM0", type=ATM, multiplicity=Multiplicity(0, 1)),
        Property(name="bANK1", type=BANK, multiplicity=Multiplicity(0, 1))
    }
)
BANK_Account: BinaryAssociation = BinaryAssociation(
    name="BANK_Account",
    ends={
        Property(name="account2", type=Account, multiplicity=Multiplicity(0, 1)),
        Property(name="bANK3", type=BANK, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Account: BinaryAssociation = BinaryAssociation(
    name="Customer_Account",
    ends={
        Property(name="account4", type=Account, multiplicity=Multiplicity(0, 1)),
        Property(name="customer5", type=Customer, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="b1a8d10a_055b_479d_af20_dc46aaaa1da1",
    types={BANK, Customer, Account, ATM, ATM__Transactions, Current_Account, Savings_Account},
    associations={Account_ATM__Transactions, Current_Account_Savings_Account, BANK_ATM, BANK_Account, Customer_Account},
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