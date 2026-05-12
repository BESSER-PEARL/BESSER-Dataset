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
ATM = Class(name="ATM")
Customer = Class(name="Customer")
Account = Class(name="Account")
Checking_Account = Class(name="Checking_Account")
Savings_Account = Class(name="Savings_Account")
ATM_Transactions = Class(name="ATM_Transactions")

# Bank class attributes and methods
Bank_code: Property = Property(name="code", type=StringType)
Bank_address: Property = Property(name="address", type=StringType)
Bank.attributes={Bank_address, Bank_code}

# ATM class attributes and methods
ATM_location: Property = Property(name="location", type=StringType)
ATM_managedby: Property = Property(name="managedby", type=StringType)
ATM.attributes={ATM_location, ATM_managedby}

# Customer class attributes and methods
Customer_name: Property = Property(name="name", type=StringType)
Customer_address: Property = Property(name="address", type=StringType)
Customer_dob: Property = Property(name="dob", type=StringType)
Customer_card_number: Property = Property(name="card_number", type=StringType)
Customer_pin: Property = Property(name="pin", type=StringType)
Customer.attributes={Customer_card_number, Customer_address, Customer_name, Customer_pin, Customer_dob}

# Account class attributes and methods
Account_number: Property = Property(name="number", type=StringType)
Account_balance: Property = Property(name="balance", type=StringType)
Account.attributes={Account_number, Account_balance}

# Checking_Account class attributes and methods

# Savings_Account class attributes and methods

# ATM_Transactions class attributes and methods
ATM_Transactions_transation_ID: Property = Property(name="transation_ID", type=StringType)
ATM_Transactions_date: Property = Property(name="date", type=StringType)
ATM_Transactions_type: Property = Property(name="type", type=StringType)
ATM_Transactions_amount: Property = Property(name="amount", type=StringType)
ATM_Transactions_post_balance: Property = Property(name="post_balance", type=StringType)
ATM_Transactions.attributes={ATM_Transactions_amount, ATM_Transactions_date, ATM_Transactions_transation_ID, ATM_Transactions_post_balance, ATM_Transactions_type}

# Relationships
Account_ATM_Transactions: BinaryAssociation = BinaryAssociation(
    name="Account_ATM_Transactions",
    ends={
        Property(name="aTM_Transactions0", type=ATM_Transactions, multiplicity=Multiplicity(0, 1)),
        Property(name="account1", type=Account, multiplicity=Multiplicity(0, 1))
    }
)
Bank_ATM: BinaryAssociation = BinaryAssociation(
    name="Bank_ATM",
    ends={
        Property(name="aTM2", type=ATM, multiplicity=Multiplicity(0, 1)),
        Property(name="bank3", type=Bank, multiplicity=Multiplicity(0, 1))
    }
)
Bank_Account: BinaryAssociation = BinaryAssociation(
    name="Bank_Account",
    ends={
        Property(name="account4", type=Account, multiplicity=Multiplicity(0, 1)),
        Property(name="bank5", type=Bank, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Account: BinaryAssociation = BinaryAssociation(
    name="Customer_Account",
    ends={
        Property(name="account6", type=Account, multiplicity=Multiplicity(0, 1)),
        Property(name="customer7", type=Customer, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_O0LuoFX5Eei2efM7H4gIXw",
    types={Bank, ATM, Customer, Account, Checking_Account, Savings_Account, ATM_Transactions},
    associations={Account_ATM_Transactions, Bank_ATM, Bank_Account, Customer_Account},
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