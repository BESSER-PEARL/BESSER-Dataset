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
ADMIN = Class(name="ADMIN")
Customer = Class(name="Customer")
Account = Class(name="Account")
ATM = Class(name="ATM")
ATM__Transactions = Class(name="ATM__Transactions")
Current_Account = Class(name="Current_Account")
Savings_Account = Class(name="Savings_Account")

# ADMIN class attributes and methods
ADMIN_Code: Property = Property(name="Code", type=StringType)
ADMIN_Address: Property = Property(name="Address", type=StringType)
ADMIN.attributes={ADMIN_Code, ADMIN_Address}

# Customer class attributes and methods
Customer_Name: Property = Property(name="Name", type=StringType)
Customer_DOB: Property = Property(name="DOB", type=StringType)
Customer_Pin: Property = Property(name="Pin", type=IntegerType)
Customer_Card_num: Property = Property(name="Card_num", type=IntegerType)
Customer.attributes={Customer_Name, Customer_Card_num, Customer_Pin, Customer_DOB}

# Account class attributes and methods
Account_AccountNumber: Property = Property(name="AccountNumber", type=StringType)
Account_Balance: Property = Property(name="Balance", type=StringType)
Account.attributes={Account_Balance, Account_AccountNumber}

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
ATM__Transactions.attributes={ATM__Transactions_Type, ATM__Transactions_Post_balance, ATM__Transactions_Date, ATM__Transactions_Transaction_id, ATM__Transactions_Amount}

# Current_Account class attributes and methods
Current_Account_AccountNumber: Property = Property(name="AccountNumber", type=StringType)
Current_Account_Balance: Property = Property(name="Balance", type=StringType)
Current_Account.attributes={Current_Account_Balance, Current_Account_AccountNumber}

# Savings_Account class attributes and methods
Savings_Account_AccountNumber: Property = Property(name="AccountNumber", type=StringType)
Savings_Account_Balance: Property = Property(name="Balance", type=StringType)
Savings_Account.attributes={Savings_Account_AccountNumber, Savings_Account_Balance}

# Relationships
BANK_ATM: BinaryAssociation = BinaryAssociation(
    name="BANK_ATM",
    ends={
        Property(name="aTM0", type=ATM, multiplicity=Multiplicity(0, 1)),
        Property(name="bANK1", type=ADMIN, multiplicity=Multiplicity(0, 1))
    }
)
BANK_Account: BinaryAssociation = BinaryAssociation(
    name="BANK_Account",
    ends={
        Property(name="account2", type=Account, multiplicity=Multiplicity(0, 1)),
        Property(name="bANK3", type=ADMIN, multiplicity=Multiplicity(0, 1))
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

# Domain Model
domain_model = DomainModel(
    name="ea503200_76a5_4fba_846a_f7e5dd9e670a",
    types={ADMIN, Customer, Account, ATM, ATM__Transactions, Current_Account, Savings_Account},
    associations={BANK_ATM, BANK_Account, Customer_Account, Account_ATM__Transactions, Current_Account_Savings_Account},
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