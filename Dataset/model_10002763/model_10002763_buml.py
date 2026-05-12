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

# BANK class attributes and methods
BANK_Code: Property = Property(name="Code", type=StringType)
BANK_Address: Property = Property(name="Address", type=StringType)
BANK.attributes={BANK_Code, BANK_Address}

# Customer class attributes and methods
Customer_Name: Property = Property(name="Name", type=StringType)
Customer_DOB: Property = Property(name="DOB", type=StringType)
Customer_Pin: Property = Property(name="Pin", type=IntegerType)
Customer_Card_num: Property = Property(name="Card_num", type=IntegerType)
Customer.attributes={Customer_DOB, Customer_Pin, Customer_Name, Customer_Card_num}

# Account class attributes and methods
Account_AccountNumber: Property = Property(name="AccountNumber", type=StringType)
Account_Balance: Property = Property(name="Balance", type=StringType)
Account.attributes={Account_AccountNumber, Account_Balance}

# ATM class attributes and methods
ATM_location: Property = Property(name="location", type=StringType)
ATM_ManagedBy: Property = Property(name="ManagedBy", type=StringType)
ATM.attributes={ATM_location, ATM_ManagedBy}

# ATM__Transactions class attributes and methods
ATM__Transactions_Transaction_id: Property = Property(name="Transaction_id", type=StringType)
ATM__Transactions_Date: Property = Property(name="Date", type=StringType)
ATM__Transactions_Type: Property = Property(name="Type", type=StringType)
ATM__Transactions_Amount: Property = Property(name="Amount", type=StringType)
ATM__Transactions_Post_balance: Property = Property(name="Post_balance", type=StringType)
ATM__Transactions.attributes={ATM__Transactions_Date, ATM__Transactions_Post_balance, ATM__Transactions_Transaction_id, ATM__Transactions_Amount, ATM__Transactions_Type}

# Relationships
BANK_ATM: BinaryAssociation = BinaryAssociation(
    name="BANK_ATM",
    ends={
        Property(name="atm0", type=ATM, multiplicity=Multiplicity(0, 1)),
        Property(name="bANK1", type=BANK, multiplicity=Multiplicity(1, 1))
    }
)
BANK_Account: BinaryAssociation = BinaryAssociation(
    name="BANK_Account",
    ends={
        Property(name="account2", type=Account, multiplicity=Multiplicity(0, 1)),
        Property(name="bank3", type=BANK, multiplicity=Multiplicity(1, 1))
    }
)
Customer_Account: BinaryAssociation = BinaryAssociation(
    name="Customer_Account",
    ends={
        Property(name="account4", type=Account, multiplicity=Multiplicity(0, 1)),
        Property(name="customer5", type=Customer, multiplicity=Multiplicity(0, 1))
    }
)
Account_ATM__Transactions: BinaryAssociation = BinaryAssociation(
    name="Account_ATM__Transactions",
    ends={
        Property(name="atm__Transactions6", type=ATM__Transactions, multiplicity=Multiplicity(0, 1)),
        Property(name="account7", type=Account, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="d741fd10_c6f4_46cf_a07d_c9484bd3da04",
    types={BANK, Customer, Account, ATM, ATM__Transactions},
    associations={BANK_ATM, BANK_Account, Customer_Account, Account_ATM__Transactions},
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