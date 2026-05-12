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
Account = Class(name="Account", is_abstract=True)
Transaction = Class(name="Transaction")
CheckTransaction = Class(name="CheckTransaction")
CoDTransaction = Class(name="CoDTransaction")
SavingAccount = Class(name="SavingAccount")
CheckingAccount = Class(name="CheckingAccount")

# Bank class attributes and methods

# Customer class attributes and methods
Customer_taxId: Property = Property(name="taxId", type=StringType)
Customer_name: Property = Property(name="name", type=StringType)
Customer.attributes={Customer_taxId, Customer_name}

# Account class attributes and methods
Account_accId: Property = Property(name="accId", type=StringType)
Account_accNumber: Property = Property(name="accNumber", type=StringType)
Account_openDate: Property = Property(name="openDate", type=StringType)
Account_balance: Property = Property(name="balance", type=StringType)
Account_MAX_HOLDERS: Property = Property(name="MAX_HOLDERS", type=StringType)
Account.attributes={Account_accId, Account_openDate, Account_MAX_HOLDERS, Account_balance, Account_accNumber}

# Transaction class attributes and methods
Transaction_transactionDate: Property = Property(name="transactionDate", type=StringType)
Transaction_holder: Property = Property(name="holder", type=Customer)
Transaction_transactionType: Property = Property(name="transactionType", type=StringType)
Transaction_transactionAmount: Property = Property(name="transactionAmount", type=StringType)
Transaction.attributes={Transaction_transactionAmount, Transaction_transactionDate, Transaction_transactionType, Transaction_holder}

# CheckTransaction class attributes and methods
CheckTransaction_memo: Property = Property(name="memo", type=StringType)
CheckTransaction.attributes={CheckTransaction_memo}

# CoDTransaction class attributes and methods
CoDTransaction_startDate: Property = Property(name="startDate", type=StringType)
CoDTransaction_endDate: Property = Property(name="endDate", type=StringType)
CoDTransaction_interestRate: Property = Property(name="interestRate", type=StringType)
CoDTransaction.attributes={CoDTransaction_interestRate, CoDTransaction_startDate, CoDTransaction_endDate}

# SavingAccount class attributes and methods

# CheckingAccount class attributes and methods

# Relationships
Bank_Customer: BinaryAssociation = BinaryAssociation(
    name="Bank_Customer",
    ends={
        Property(name="customer0", type=Customer, multiplicity=Multiplicity(0, 9999)),
        Property(name="bank1", type=Bank, multiplicity=Multiplicity(1, 1))
    }
)
Account_Transaction: BinaryAssociation = BinaryAssociation(
    name="Account_Transaction",
    ends={
        Property(name="transaction2", type=Transaction, multiplicity=Multiplicity(0, 9999)),
        Property(name="account3", type=Account, multiplicity=Multiplicity(1, 2))
    }
)
Bank_Account: BinaryAssociation = BinaryAssociation(
    name="Bank_Account",
    ends={
        Property(name="account4", type=Account, multiplicity=Multiplicity(0, 9999)),
        Property(name="bank5", type=Bank, multiplicity=Multiplicity(1, 1))
    }
)
is_owner_of: BinaryAssociation = BinaryAssociation(
    name="is_owner_of",
    ends={
        Property(name="account6", type=Account, multiplicity=Multiplicity(1, 9999)),
        Property(name="customer7", type=Customer, multiplicity=Multiplicity(1, 2))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_7f1f8469_b086_4eb1_b1f2_c195a92fb18f",
    types={Bank, Customer, Account, Transaction, CheckTransaction, CoDTransaction, SavingAccount, CheckingAccount},
    associations={Bank_Customer, Account_Transaction, Bank_Account, is_owner_of},
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