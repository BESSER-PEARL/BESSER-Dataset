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
CustomerType: Enumeration = Enumeration(
    name="CustomerType",
    literals={
            EnumerationLiteral(name="Youth"),
			EnumerationLiteral(name="Adult"),
			EnumerationLiteral(name="Senior")
    }
)

# Classes
BankingSystem_Employee = Class(name="BankingSystem::Employee", is_abstract=True)
BankingSystem_Bank = Class(name="BankingSystem::Bank")
BankingSystem_Branch = Class(name="BankingSystem::Branch")
BankingSystem_Customer = Class(name="BankingSystem::Customer")
BankingSystem_Account = Class(name="BankingSystem::Account", is_abstract=True)
BankingSystem_Loan = Class(name="BankingSystem::Loan")
BankingSystem_Financial_Representative = Class(name="BankingSystem::Financial::Representative")
BankingSystem_Chequing = Class(name="BankingSystem::Chequing")
Account = Class(name="Account")
BankingSystem_Saving = Class(name="BankingSystem::Saving")
Employee = Class(name="Employee")

# BankingSystem_Employee class attributes and methods
BankingSystem_Employee_ename: Property = Property(name="ename", type=StringType)
BankingSystem_Employee_isCustomer: Property = Property(name="isCustomer", type=BooleanType)
BankingSystem_Employee_eage: Property = Property(name="eage", type=IntegerType)
BankingSystem_Employee_eaddress: Property = Property(name="eaddress", type=StringType)
BankingSystem_Employee_ephoneNumber: Property = Property(name="ephoneNumber", type=StringType)
BankingSystem_Employee_eid: Property = Property(name="eid", type=IntegerType)
BankingSystem_Employee.attributes={BankingSystem_Employee_ename, BankingSystem_Employee_eid, BankingSystem_Employee_isCustomer, BankingSystem_Employee_eaddress, BankingSystem_Employee_eage, BankingSystem_Employee_ephoneNumber}

# BankingSystem_Bank class attributes and methods
BankingSystem_Bank_name: Property = Property(name="name", type=StringType)
BankingSystem_Bank_bankId: Property = Property(name="bankId", type=IntegerType)
BankingSystem_Bank_description: Property = Property(name="description", type=StringType)
BankingSystem_Bank.attributes={BankingSystem_Bank_description, BankingSystem_Bank_name, BankingSystem_Bank_bankId}

# BankingSystem_Branch class attributes and methods
BankingSystem_Branch_name: Property = Property(name="name", type=StringType)
BankingSystem_Branch_branchId: Property = Property(name="branchId", type=IntegerType)
BankingSystem_Branch_location: Property = Property(name="location", type=StringType)
BankingSystem_Branch_phoneNumber: Property = Property(name="phoneNumber", type=StringType)
BankingSystem_Branch.attributes={BankingSystem_Branch_name, BankingSystem_Branch_branchId, BankingSystem_Branch_location, BankingSystem_Branch_phoneNumber}

# BankingSystem_Customer class attributes and methods
BankingSystem_Customer_name: Property = Property(name="name", type=StringType)
BankingSystem_Customer_age: Property = Property(name="age", type=IntegerType)
BankingSystem_Customer_address: Property = Property(name="address", type=StringType)
BankingSystem_Customer_phoneNumber: Property = Property(name="phoneNumber", type=StringType)
BankingSystem_Customer_customerType: Property = Property(name="customerType", type=StringType)
BankingSystem_Customer.attributes={BankingSystem_Customer_age, BankingSystem_Customer_name, BankingSystem_Customer_customerType, BankingSystem_Customer_phoneNumber, BankingSystem_Customer_address}

# BankingSystem_Account class attributes and methods
BankingSystem_Account_accountNumber: Property = Property(name="accountNumber", type=StringType)
BankingSystem_Account_balance: Property = Property(name="balance", type=FloatType)
BankingSystem_Account.attributes={BankingSystem_Account_accountNumber, BankingSystem_Account_balance}

# BankingSystem_Loan class attributes and methods
BankingSystem_Loan_loanNumber: Property = Property(name="loanNumber", type=StringType)
BankingSystem_Loan_amount: Property = Property(name="amount", type=FloatType)
BankingSystem_Loan_interestRate: Property = Property(name="interestRate", type=FloatType)
BankingSystem_Loan_duration: Property = Property(name="duration", type=IntegerType)
BankingSystem_Loan.attributes={BankingSystem_Loan_loanNumber, BankingSystem_Loan_duration, BankingSystem_Loan_interestRate, BankingSystem_Loan_amount}

# BankingSystem_Financial_Representative class attributes and methods

# BankingSystem_Chequing class attributes and methods

# Account class attributes and methods

# BankingSystem_Saving class attributes and methods
BankingSystem_Saving_interestRate: Property = Property(name="interestRate", type=FloatType)
BankingSystem_Saving.attributes={BankingSystem_Saving_interestRate}

# Employee class attributes and methods

# Relationships
employees2: BinaryAssociation = BinaryAssociation(
    name="employees2",
    ends={
        Property(name="Employee", type=BankingSystem_Branch, multiplicity=Multiplicity(1, 1)),
        Property(name="branch3", type=BankingSystem_Employee, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
bank4: BinaryAssociation = BinaryAssociation(
    name="bank4",
    ends={
        Property(name="Bank", type=BankingSystem_Branch, multiplicity=Multiplicity(1, 1)),
        Property(name="branches", type=BankingSystem_Bank, multiplicity=Multiplicity(1, 1))
    }
)
branches0: BinaryAssociation = BinaryAssociation(
    name="branches0",
    ends={
        Property(name="Branch", type=BankingSystem_Bank, multiplicity=Multiplicity(1, 1)),
        Property(name="bank", type=BankingSystem_Branch, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
customers1: BinaryAssociation = BinaryAssociation(
    name="customers1",
    ends={
        Property(name="Customer", type=BankingSystem_Branch, multiplicity=Multiplicity(1, 1)),
        Property(name="branch", type=BankingSystem_Customer, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
branch13: BinaryAssociation = BinaryAssociation(
    name="branch13",
    ends={
        Property(name="Branch14", type=BankingSystem_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="employees", type=BankingSystem_Branch, multiplicity=Multiplicity(1, 1))
    }
)
branch5: BinaryAssociation = BinaryAssociation(
    name="branch5",
    ends={
        Property(name="Branch6", type=BankingSystem_Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="customers", type=BankingSystem_Branch, multiplicity=Multiplicity(1, 1))
    }
)
accounts7: BinaryAssociation = BinaryAssociation(
    name="accounts7",
    ends={
        Property(name="Account", type=BankingSystem_Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="customer", type=BankingSystem_Account, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
loans8: BinaryAssociation = BinaryAssociation(
    name="loans8",
    ends={
        Property(name="Loan", type=BankingSystem_Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="customer9", type=BankingSystem_Loan, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
representative10: BinaryAssociation = BinaryAssociation(
    name="representative10",
    ends={
        Property(name="Financial_Representative", type=BankingSystem_Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="a", type=BankingSystem_Financial_Representative, multiplicity=Multiplicity(0, 9999))
    }
)
customer11: BinaryAssociation = BinaryAssociation(
    name="customer11",
    ends={
        Property(name="Customer12", type=BankingSystem_Account, multiplicity=Multiplicity(1, 1)),
        Property(name="accounts", type=BankingSystem_Customer, multiplicity=Multiplicity(1, 1))
    }
)
customer15: BinaryAssociation = BinaryAssociation(
    name="customer15",
    ends={
        Property(name="Customer16", type=BankingSystem_Loan, multiplicity=Multiplicity(1, 1)),
        Property(name="loans", type=BankingSystem_Customer, multiplicity=Multiplicity(1, 1))
    }
)
a17: BinaryAssociation = BinaryAssociation(
    name="a17",
    ends={
        Property(name="Customer18", type=BankingSystem_Financial_Representative, multiplicity=Multiplicity(1, 1)),
        Property(name="representative", type=BankingSystem_Customer, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_BankingSystem_Chequing_Account = Generalization(general=Account, specific=BankingSystem_Chequing)
gen_BankingSystem_Saving_Account = Generalization(general=Account, specific=BankingSystem_Saving)
gen_BankingSystem_Financial_Representative_Employee = Generalization(general=Employee, specific=BankingSystem_Financial_Representative)

# Domain Model
domain_model = DomainModel(
    name="BankingSystem",
    types={BankingSystem_Employee, BankingSystem_Bank, BankingSystem_Branch, BankingSystem_Customer, BankingSystem_Account, BankingSystem_Loan, BankingSystem_Financial_Representative, BankingSystem_Chequing, Account, BankingSystem_Saving, Employee, CustomerType},
    associations={employees2, bank4, branches0, customers1, branch13, branch5, accounts7, loans8, representative10, customer11, customer15, a17},
    generalizations={gen_BankingSystem_Chequing_Account, gen_BankingSystem_Saving_Account, gen_BankingSystem_Financial_Representative_Employee},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)