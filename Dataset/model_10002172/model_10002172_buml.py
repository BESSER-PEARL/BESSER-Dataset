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
BMS = Class(name="BMS")
Employee = Class(name="Employee")
Customer = Class(name="Customer")
SavingsAccount = Class(name="SavingsAccount")
CheckingAccount = Class(name="CheckingAccount")
Temporary = Class(name="Temporary")
Contractor = Class(name="Contractor")
Permanent = Class(name="Permanent")
Business = Class(name="Business")
Indevidual = Class(name="Indevidual")

# BMS class attributes and methods

# Employee class attributes and methods
Employee_EmpId: Property = Property(name="EmpId", type=IntegerType)
Employee_EmpFName: Property = Property(name="EmpFName", type=StringType)
Employee_EmpLName: Property = Property(name="EmpLName", type=StringType)
Employee_DOB: Property = Property(name="DOB", type=StringType)
Employee_Gender: Property = Property(name="Gender", type=StringType)
Employee_Address: Property = Property(name="Address", type=StringType)
Employee_City: Property = Property(name="City", type=StringType)
Employee_State: Property = Property(name="State", type=StringType)
Employee_Zipcode: Property = Property(name="Zipcode", type=StringType)
Employee_EmpType: Property = Property(name="EmpType", type=StringType)
Employee_Department: Property = Property(name="Department", type=StringType)
Employee.attributes={Employee_EmpLName, Employee_City, Employee_Address, Employee_EmpType, Employee_Gender, Employee_EmpFName, Employee_Zipcode, Employee_Department, Employee_State, Employee_DOB, Employee_EmpId}

# Customer class attributes and methods
Customer_CustId: Property = Property(name="CustId", type=IntegerType)
Customer_FName: Property = Property(name="FName", type=StringType)
Customer_Lname: Property = Property(name="Lname", type=StringType)
Customer_Gender: Property = Property(name="Gender", type=StringType)
Customer_DOB: Property = Property(name="DOB", type=StringType)
Customer_Address: Property = Property(name="Address", type=StringType)
Customer_attribute: Property = Property(name="attribute", type=StringType)
Customer_State: Property = Property(name="State", type=StringType)
Customer_Zipcode: Property = Property(name="Zipcode", type=IntegerType)
Customer_Mobile: Property = Property(name="Mobile", type=IntegerType)
Customer.attributes={Customer_Gender, Customer_CustId, Customer_Address, Customer_DOB, Customer_FName, Customer_attribute, Customer_Lname, Customer_Mobile, Customer_Zipcode, Customer_State}

# SavingsAccount class attributes and methods
SavingsAccount_CustomerId: Property = Property(name="CustomerId", type=IntegerType)
SavingsAccount_AccountNo: Property = Property(name="AccountNo", type=IntegerType)
SavingsAccount_AccountType: Property = Property(name="AccountType", type=StringType)
SavingsAccount_Amount: Property = Property(name="Amount", type=StringType)
SavingsAccount_Cust_Name: Property = Property(name="Cust_Name", type=StringType)
SavingsAccount_Cust_DOB: Property = Property(name="Cust_DOB", type=StringType)
SavingsAccount_Mobile: Property = Property(name="Mobile", type=IntegerType)
SavingsAccount_Withdraw: Property = Property(name="Withdraw", type=StringType)
SavingsAccount_Diposit: Property = Property(name="Diposit", type=StringType)
SavingsAccount.attributes={SavingsAccount_Withdraw, SavingsAccount_AccountType, SavingsAccount_Amount, SavingsAccount_Cust_DOB, SavingsAccount_Cust_Name, SavingsAccount_Mobile, SavingsAccount_AccountNo, SavingsAccount_Diposit, SavingsAccount_CustomerId}

# CheckingAccount class attributes and methods
CheckingAccount_CustomerId: Property = Property(name="CustomerId", type=IntegerType)
CheckingAccount_AccountNo: Property = Property(name="AccountNo", type=IntegerType)
CheckingAccount_AccountType: Property = Property(name="AccountType", type=StringType)
CheckingAccount_Amount: Property = Property(name="Amount", type=StringType)
CheckingAccount_Cust_Name: Property = Property(name="Cust_Name", type=StringType)
CheckingAccount_Cust_DOB: Property = Property(name="Cust_DOB", type=StringType)
CheckingAccount_MobileNo: Property = Property(name="MobileNo", type=IntegerType)
CheckingAccount_Diposit: Property = Property(name="Diposit", type=StringType)
CheckingAccount_Withdraw: Property = Property(name="Withdraw", type=StringType)
CheckingAccount.attributes={CheckingAccount_Diposit, CheckingAccount_CustomerId, CheckingAccount_Cust_DOB, CheckingAccount_Withdraw, CheckingAccount_Cust_Name, CheckingAccount_Amount, CheckingAccount_AccountType, CheckingAccount_MobileNo, CheckingAccount_AccountNo}

# Temporary class attributes and methods

# Contractor class attributes and methods

# Permanent class attributes and methods

# Business class attributes and methods

# Indevidual class attributes and methods

# Relationships
BankManagementSystem_Employee: BinaryAssociation = BinaryAssociation(
    name="BankManagementSystem_Employee",
    ends={
        Property(name="employee0", type=Employee, multiplicity=Multiplicity(0, 1)),
        Property(name="BMS1", type=BMS, multiplicity=Multiplicity(0, 1))
    }
)
BankManagementSystem_Customer: BinaryAssociation = BinaryAssociation(
    name="BankManagementSystem_Customer",
    ends={
        Property(name="customer2", type=Customer, multiplicity=Multiplicity(0, 1)),
        Property(name="BMS3", type=BMS, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Savings_Account: BinaryAssociation = BinaryAssociation(
    name="Customer_Savings_Account",
    ends={
        Property(name="savings_Account4", type=SavingsAccount, multiplicity=Multiplicity(0, 1)),
        Property(name="customer5", type=Customer, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Checking_Account: BinaryAssociation = BinaryAssociation(
    name="Customer_Checking_Account",
    ends={
        Property(name="checking_Account6", type=CheckingAccount, multiplicity=Multiplicity(0, 1)),
        Property(name="customer7", type=Customer, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_uHpJEKnZEemLy_Ni_VW66Q",
    types={BMS, Employee, Customer, SavingsAccount, CheckingAccount, Temporary, Contractor, Permanent, Business, Indevidual},
    associations={BankManagementSystem_Employee, BankManagementSystem_Customer, Customer_Savings_Account, Customer_Checking_Account},
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