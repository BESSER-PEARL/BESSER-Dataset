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
TransactionType: Enumeration = Enumeration(
    name="TransactionType",
    literals={
            
    }
)

# Classes
Bank = Class(name="Bank")
Branch = Class(name="Branch")
Account = Class(name="Account")
Saving_Account = Class(name="Saving_Account")
Current_Account = Class(name="Current_Account")
Customer = Class(name="Customer")
User = Class(name="User")
Employee = Class(name="Employee")
Manager = Class(name="Manager")
Transaction = Class(name="Transaction")
Setting = Class(name="Setting")

# Bank class attributes and methods
Bank_Name: Property = Property(name="Name", type=StringType)
Bank_Code: Property = Property(name="Code", type=StringType)
Bank.attributes={Bank_Code, Bank_Name}

# Branch class attributes and methods
Branch_Branch_code: Property = Property(name="Branch_code", type=StringType)
Branch_City: Property = Property(name="City", type=StringType)
Branch.attributes={Branch_Branch_code, Branch_City}

# Account class attributes and methods
Account_Acc_no: Property = Property(name="Acc_no", type=IntegerType)
Account_Balance: Property = Property(name="Balance", type=IntegerType)
Account_date_Of_Opening: Property = Property(name="date_Of_Opening", type=StringType)
Account_min_Balance: Property = Property(name="min_Balance", type=IntegerType)
Account.attributes={Account_Balance, Account_date_Of_Opening, Account_Acc_no, Account_min_Balance}

# Saving_Account class attributes and methods
Saving_Account_interest_Rate: Property = Property(name="interest_Rate", type=IntegerType)
Saving_Account.attributes={Saving_Account_interest_Rate}

# Current_Account class attributes and methods

# Customer class attributes and methods
Customer_Cust_id: Property = Property(name="Cust_id", type=StringType)
Customer_name: Property = Property(name="name", type=StringType)
Customer_address: Property = Property(name="address", type=StringType)
Customer_phone: Property = Property(name="phone", type=StringType)
Customer.attributes={Customer_name, Customer_Cust_id, Customer_address, Customer_phone}

# User class attributes and methods
User_uid: Property = Property(name="uid", type=IntegerType)
User_name: Property = Property(name="name", type=StringType)
User_family: Property = Property(name="family", type=StringType)
User_userName: Property = Property(name="userName", type=StringType)
User_password: Property = Property(name="password", type=StringType)
User.attributes={User_userName, User_name, User_uid, User_password, User_family}

# Employee class attributes and methods
Employee_Eid: Property = Property(name="Eid", type=IntegerType)
Employee_Mid: Property = Property(name="Mid", type=IntegerType)
Employee.attributes={Employee_Mid, Employee_Eid}

# Manager class attributes and methods

# Transaction class attributes and methods
Transaction_TranId: Property = Property(name="TranId", type=IntegerType)
Transaction_Acc_num: Property = Property(name="Acc_num", type=IntegerType)
Transaction_date: Property = Property(name="date", type=StringType)
Transaction_type: Property = Property(name="type", type=TransactionType)
Transaction_amount: Property = Property(name="amount", type=IntegerType)
Transaction_prevBalance: Property = Property(name="prevBalance", type=IntegerType)
Transaction_currentBalance: Property = Property(name="currentBalance", type=IntegerType)
Transaction_status: Property = Property(name="status", type=StringType)
Transaction.attributes={Transaction_currentBalance, Transaction_Acc_num, Transaction_date, Transaction_type, Transaction_TranId, Transaction_prevBalance, Transaction_status, Transaction_amount}

# Setting class attributes and methods

# Relationships
Bank_Branch: BinaryAssociation = BinaryAssociation(
    name="Bank_Branch",
    ends={
        Property(name="branch0", type=Branch, multiplicity=Multiplicity(0, 9999)),
        Property(name="bank1", type=Bank, multiplicity=Multiplicity(1, 1))
    }
)
Branch_Account: BinaryAssociation = BinaryAssociation(
    name="Branch_Account",
    ends={
        Property(name="account2", type=Account, multiplicity=Multiplicity(0, 9999)),
        Property(name="branch3", type=Branch, multiplicity=Multiplicity(1, 1))
    }
)
Saving_Account_Customer: BinaryAssociation = BinaryAssociation(
    name="Saving_Account_Customer",
    ends={
        Property(name="customer4", type=Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="saving_Account5", type=Saving_Account, multiplicity=Multiplicity(0, 1))
    }
)
Current_Account_Customer: BinaryAssociation = BinaryAssociation(
    name="Current_Account_Customer",
    ends={
        Property(name="customer6", type=Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="current_Account7", type=Current_Account, multiplicity=Multiplicity(0, 1))
    }
)
Employee_Manager: BinaryAssociation = BinaryAssociation(
    name="Employee_Manager",
    ends={
        Property(name="manager8", type=Manager, multiplicity=Multiplicity(1, 1)),
        Property(name="employee9", type=Employee, multiplicity=Multiplicity(1, 9999))
    }
)
Account_Transaction: BinaryAssociation = BinaryAssociation(
    name="Account_Transaction",
    ends={
        Property(name="transaction10", type=Transaction, multiplicity=Multiplicity(0, 9999)),
        Property(name="account11", type=Account, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="fbb392bc_e364_4945_999d_75ab23517a07",
    types={Bank, Branch, Account, Saving_Account, Current_Account, Customer, User, Employee, Manager, Transaction, Setting, TransactionType},
    associations={Bank_Branch, Branch_Account, Saving_Account_Customer, Current_Account_Customer, Employee_Manager, Account_Transaction},
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