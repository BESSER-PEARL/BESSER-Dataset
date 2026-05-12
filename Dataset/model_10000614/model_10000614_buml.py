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
Component_Component = Class(name="Component_Component")
T = Class(name="T")
ATM_Machine__Component = Class(name="ATM_Machine__Component")
Component3_Component = Class(name="Component3_Component")
Component32_Component = Class(name="Component32_Component")
Component322_Component = Class(name="Component322_Component")
Component323_Component = Class(name="Component323_Component")
Component3232_Component = Class(name="Component3232_Component")
Component32322_Component = Class(name="Component32322_Component")

# BANK class attributes and methods
BANK_Code: Property = Property(name="Code", type=StringType)
BANK_Address: Property = Property(name="Address", type=StringType)
BANK.attributes={BANK_Address, BANK_Code}

# Customer class attributes and methods
Customer_Name: Property = Property(name="Name", type=StringType)
Customer_DOB: Property = Property(name="DOB", type=StringType)
Customer_Pin: Property = Property(name="Pin", type=IntegerType)
Customer_Card_num: Property = Property(name="Card_num", type=IntegerType)
Customer.attributes={Customer_Card_num, Customer_Name, Customer_Pin, Customer_DOB}

# Account class attributes and methods
Account_AccountNumber: Property = Property(name="AccountNumber", type=StringType)
Account_Balance: Property = Property(name="Balance", type=StringType)
Account.attributes={Account_Balance, Account_AccountNumber}

# ATM class attributes and methods
ATM_location: Property = Property(name="location", type=StringType)
ATM_ManagedBy: Property = Property(name="ManagedBy", type=StringType)
ATM.attributes={ATM_ManagedBy, ATM_location}

# ATM__Transactions class attributes and methods
ATM__Transactions_Transaction_id: Property = Property(name="Transaction_id", type=StringType)
ATM__Transactions_Date: Property = Property(name="Date", type=StringType)
ATM__Transactions_Type: Property = Property(name="Type", type=StringType)
ATM__Transactions_Amount: Property = Property(name="Amount", type=StringType)
ATM__Transactions_Post_balance: Property = Property(name="Post_balance", type=StringType)
ATM__Transactions.attributes={ATM__Transactions_Post_balance, ATM__Transactions_Transaction_id, ATM__Transactions_Type, ATM__Transactions_Amount, ATM__Transactions_Date}

# Component_Component class attributes and methods

# T class attributes and methods

# ATM_Machine__Component class attributes and methods

# Component3_Component class attributes and methods

# Component32_Component class attributes and methods

# Component322_Component class attributes and methods

# Component323_Component class attributes and methods

# Component3232_Component class attributes and methods

# Component32322_Component class attributes and methods

# Relationships
BANK_ATM: BinaryAssociation = BinaryAssociation(
    name="BANK_ATM",
    ends={
        Property(name="ATM0", type=ATM, multiplicity=Multiplicity(0, 9999)),
        Property(name="BANK1", type=BANK, multiplicity=Multiplicity(0, 1))
    }
)
BANK_Account: BinaryAssociation = BinaryAssociation(
    name="BANK_Account",
    ends={
        Property(name="account2", type=Account, multiplicity=Multiplicity(0, 9999)),
        Property(name="BANK3", type=BANK, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Account: BinaryAssociation = BinaryAssociation(
    name="Customer_Account",
    ends={
        Property(name="account4", type=Account, multiplicity=Multiplicity(0, 9999)),
        Property(name="customer5", type=Customer, multiplicity=Multiplicity(0, 1))
    }
)
Account_ATM__Transactions: BinaryAssociation = BinaryAssociation(
    name="Account_ATM__Transactions",
    ends={
        Property(name="ATM__Transactions6", type=ATM__Transactions, multiplicity=Multiplicity(0, 1)),
        Property(name="account7", type=Account, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_4b424ab7_c43b_4086_9d9c_aff0aa83ac82",
    types={BANK, Customer, Account, ATM, ATM__Transactions, Component_Component, T, ATM_Machine__Component, Component3_Component, Component32_Component, Component322_Component, Component323_Component, Component3232_Component, Component32322_Component},
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