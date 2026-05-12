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
Accounts = Class(name="Accounts")
BankEmployee = Class(name="BankEmployee")
AccountHolder = Class(name="AccountHolder")
ATM_s = Class(name="ATM_s")
CurrentAccount = Class(name="CurrentAccount")
Savings_Account = Class(name="Savings_Account")
Loan_Account = Class(name="Loan_Account")

# Bank class attributes and methods
Bank_Name_string: Property = Property(name="Name_string", type=StringType)
Bank_Name: Property = Property(name="Name", type=StringType)
Bank_ID: Property = Property(name="ID", type=IntegerType)
Bank_locality: Property = Property(name="locality", type=StringType)
Bank.attributes={Bank_Name, Bank_ID, Bank_locality, Bank_Name_string}

# Accounts class attributes and methods
Accounts_AccountNo: Property = Property(name="AccountNo", type=IntegerType)
Accounts_branchCode: Property = Property(name="branchCode", type=StringType)
Accounts.attributes={Accounts_branchCode, Accounts_AccountNo}

# BankEmployee class attributes and methods
BankEmployee_Name: Property = Property(name="Name", type=StringType)
BankEmployee_EmployeeID: Property = Property(name="EmployeeID", type=IntegerType)
BankEmployee_EmpAdd: Property = Property(name="EmpAdd", type=StringType)
BankEmployee_Salary: Property = Property(name="Salary", type=IntegerType)
BankEmployee.attributes={BankEmployee_Salary, BankEmployee_Name, BankEmployee_EmployeeID, BankEmployee_EmpAdd}

# AccountHolder class attributes and methods
AccountHolder_Name: Property = Property(name="Name", type=StringType)
AccountHolder_AccNo: Property = Property(name="AccNo", type=IntegerType)
AccountHolder_Address: Property = Property(name="Address", type=StringType)
AccountHolder.attributes={AccountHolder_AccNo, AccountHolder_Name, AccountHolder_Address}

# ATM_s class attributes and methods
ATM_s_PIN: Property = Property(name="PIN", type=IntegerType)
ATM_s_OperatorName: Property = Property(name="OperatorName", type=StringType)
ATM_s_Withdrawn: Property = Property(name="Withdrawn", type=IntegerType)
ATM_s.attributes={ATM_s_PIN, ATM_s_Withdrawn, ATM_s_OperatorName}

# CurrentAccount class attributes and methods
CurrentAccount_HolderName: Property = Property(name="HolderName", type=StringType)
CurrentAccount_AccNo: Property = Property(name="AccNo", type=IntegerType)
CurrentAccount_PIn: Property = Property(name="PIn", type=IntegerType)
CurrentAccount.attributes={CurrentAccount_PIn, CurrentAccount_AccNo, CurrentAccount_HolderName}

# Savings_Account class attributes and methods
Savings_Account_Holder_Name: Property = Property(name="Holder_Name", type=StringType)
Savings_Account_AccNo: Property = Property(name="AccNo", type=IntegerType)
Savings_Account_PIn: Property = Property(name="PIn", type=Savings_Account)
Savings_Account.attributes={Savings_Account_PIn, Savings_Account_AccNo, Savings_Account_Holder_Name}

# Loan_Account class attributes and methods
Loan_Account_HolderName: Property = Property(name="HolderName", type=StringType)
Loan_Account_Acc_No: Property = Property(name="Acc_No", type=IntegerType)
Loan_Account_Loan_No: Property = Property(name="Loan_No", type=IntegerType)
Loan_Account_Type: Property = Property(name="Type", type=StringType)
Loan_Account.attributes={Loan_Account_HolderName, Loan_Account_Type, Loan_Account_Loan_No, Loan_Account_Acc_No}

# Relationships
Bank_ATM_s: BinaryAssociation = BinaryAssociation(
    name="Bank_ATM_s",
    ends={
        Property(name="aTM_s0", type=ATM_s, multiplicity=Multiplicity(0, 1)),
        Property(name="bank1", type=Bank, multiplicity=Multiplicity(0, 1))
    }
)
Bank_BankEmployee: BinaryAssociation = BinaryAssociation(
    name="Bank_BankEmployee",
    ends={
        Property(name="bankEmployee2", type=BankEmployee, multiplicity=Multiplicity(0, 1)),
        Property(name="bank3", type=Bank, multiplicity=Multiplicity(0, 1))
    }
)
Accounts_Bank: BinaryAssociation = BinaryAssociation(
    name="Accounts_Bank",
    ends={
        Property(name="bank4", type=Bank, multiplicity=Multiplicity(0, 1)),
        Property(name="accounts5", type=Accounts, multiplicity=Multiplicity(0, 1))
    }
)
Accounts_AccountHolder: BinaryAssociation = BinaryAssociation(
    name="Accounts_AccountHolder",
    ends={
        Property(name="accountHolder6", type=AccountHolder, multiplicity=Multiplicity(0, 1)),
        Property(name="accounts7", type=Accounts, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_sxP4gCzqEeiH4_FjHpTbtQ",
    types={Bank, Accounts, BankEmployee, AccountHolder, ATM_s, CurrentAccount, Savings_Account, Loan_Account},
    associations={Bank_ATM_s, Bank_BankEmployee, Accounts_Bank, Accounts_AccountHolder},
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