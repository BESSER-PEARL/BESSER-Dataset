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
Debit_Card = Class(name="Debit_Card")
Account = Class(name="Account")
ATM_INFO = Class(name="ATM_INFO")
ATM_Transaction = Class(name="ATM_Transaction")
Current_Account = Class(name="Current_Account")
Savings_Account = Class(name="Savings_Account")
Withdraw_Transaction = Class(name="Withdraw_Transaction")
Transfer_Money = Class(name="Transfer_Money")
CheckBalance = Class(name="CheckBalance")

# Bank class attributes and methods
Bank_BankId: Property = Property(name="BankId", type=StringType)
Bank_location: Property = Property(name="location", type=StringType)
Bank.attributes={Bank_location, Bank_BankId}

# Customer class attributes and methods
Customer_Id: Property = Property(name="Id", type=StringType)
Customer_Name: Property = Property(name="Name", type=StringType)
Customer_Address: Property = Property(name="Address", type=StringType)
Customer.attributes={Customer_Address, Customer_Name, Customer_Id}

# Debit_Card class attributes and methods
Debit_Card_Card_No: Property = Property(name="Card_No", type=StringType)
Debit_Card_Owned_By: Property = Property(name="Owned_By", type=StringType)
Debit_Card.attributes={Debit_Card_Owned_By, Debit_Card_Card_No}

# Account class attributes and methods
Account_Type: Property = Property(name="Type", type=StringType)
Account_Owned_by: Property = Property(name="Owned_by", type=StringType)
Account_BranchLocation: Property = Property(name="BranchLocation", type=StringType)
Account.attributes={Account_BranchLocation, Account_Owned_by, Account_Type}

# ATM_INFO class attributes and methods
ATM_INFO_Location: Property = Property(name="Location", type=StringType)
ATM_INFO.attributes={ATM_INFO_Location}

# ATM_Transaction class attributes and methods
ATM_Transaction_TransactionId: Property = Property(name="TransactionId", type=StringType)
ATM_Transaction_Date: Property = Property(name="Date", type=StringType)
ATM_Transaction_Amount: Property = Property(name="Amount", type=IntegerType)
ATM_Transaction.attributes={ATM_Transaction_Amount, ATM_Transaction_Date, ATM_Transaction_TransactionId}

# Current_Account class attributes and methods
Current_Account_Acc_no: Property = Property(name="Acc_no", type=StringType)
Current_Account_Balance: Property = Property(name="Balance", type=StringType)
Current_Account.attributes={Current_Account_Acc_no, Current_Account_Balance}

# Savings_Account class attributes and methods
Savings_Account_Acc_no: Property = Property(name="Acc_no", type=StringType)
Savings_Account_Balance: Property = Property(name="Balance", type=StringType)
Savings_Account.attributes={Savings_Account_Balance, Savings_Account_Acc_no}

# Withdraw_Transaction class attributes and methods
Withdraw_Transaction_amount: Property = Property(name="amount", type=IntegerType)
Withdraw_Transaction.attributes={Withdraw_Transaction_amount}

# Transfer_Money class attributes and methods
Transfer_Money_amount: Property = Property(name="amount", type=IntegerType)
Transfer_Money_ACC_NO: Property = Property(name="ACC_NO", type=StringType)
Transfer_Money.attributes={Transfer_Money_amount, Transfer_Money_ACC_NO}

# CheckBalance class attributes and methods
CheckBalance_Query: Property = Property(name="Query", type=StringType)
CheckBalance.attributes={CheckBalance_Query}

# Relationships
Debit_Card_MyClass: BinaryAssociation = BinaryAssociation(
    name="Debit_Card_MyClass",
    ends={
        Property(name="myClass0", type=Bank, multiplicity=Multiplicity(0, 1)),
        Property(name="debit_Card1", type=Debit_Card, multiplicity=Multiplicity(0, 10000))
    }
)
Debit_Card_Customer: BinaryAssociation = BinaryAssociation(
    name="Debit_Card_Customer",
    ends={
        Property(name="customer2", type=Customer, multiplicity=Multiplicity(0, 1)),
        Property(name="debit_Card3", type=Debit_Card, multiplicity=Multiplicity(0, 5))
    }
)
MyClass_Customer: BinaryAssociation = BinaryAssociation(
    name="MyClass_Customer",
    ends={
        Property(name="customer4", type=Customer, multiplicity=Multiplicity(0, 1000)),
        Property(name="myClass5", type=Bank, multiplicity=Multiplicity(0, 1))
    }
)
MyClass_ATM_INFO: BinaryAssociation = BinaryAssociation(
    name="MyClass_ATM_INFO",
    ends={
        Property(name="aTM_INFO6", type=ATM_INFO, multiplicity=Multiplicity(0, 100)),
        Property(name="myClass7", type=Bank, multiplicity=Multiplicity(0, 1))
    }
)
Debit_Card_Debit_Card: BinaryAssociation = BinaryAssociation(
    name="Debit_Card_Debit_Card",
    ends={
        Property(name="debit_Card8", type=Debit_Card, multiplicity=Multiplicity(0, 1)),
        Property(name="debit_Card9", type=Debit_Card, multiplicity=Multiplicity(0, 1))
    }
)
Debit_Card_Account: BinaryAssociation = BinaryAssociation(
    name="Debit_Card_Account",
    ends={
        Property(name="account10", type=Account, multiplicity=Multiplicity(0, 1)),
        Property(name="debit_Card11", type=Debit_Card, multiplicity=Multiplicity(0, 1))
    }
)
ATM_INFO_ATM_Transaction: BinaryAssociation = BinaryAssociation(
    name="ATM_INFO_ATM_Transaction",
    ends={
        Property(name="aTM_Transaction12", type=ATM_Transaction, multiplicity=Multiplicity(0, 10000)),
        Property(name="aTM_INFO13", type=ATM_INFO, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_AsF4AKzTEee6S77dw3LIvQ",
    types={Bank, Customer, Debit_Card, Account, ATM_INFO, ATM_Transaction, Current_Account, Savings_Account, Withdraw_Transaction, Transfer_Money, CheckBalance},
    associations={Debit_Card_MyClass, Debit_Card_Customer, MyClass_Customer, MyClass_ATM_INFO, Debit_Card_Debit_Card, Debit_Card_Account, ATM_INFO_ATM_Transaction},
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