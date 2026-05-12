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
BankAccount = Class(name="BankAccount")
SavingsAccount = Class(name="SavingsAccount")
FixedAccount = Class(name="FixedAccount")

# Bank class attributes and methods
Bank_name: Property = Property(name="name", type=StringType)
Bank.attributes={Bank_name}

# BankAccount class attributes and methods
BankAccount_accountNumber: Property = Property(name="accountNumber", type=IntegerType)
BankAccount_accountHolder: Property = Property(name="accountHolder", type=StringType)
BankAccount_balance: Property = Property(name="balance", type=FloatType)
BankAccount.attributes={BankAccount_accountHolder, BankAccount_balance, BankAccount_accountNumber}

# SavingsAccount class attributes and methods
SavingsAccount_interestRate: Property = Property(name="interestRate", type=FloatType)
SavingsAccount_noticeGiven: Property = Property(name="noticeGiven", type=BooleanType)
SavingsAccount.attributes={SavingsAccount_interestRate, SavingsAccount_noticeGiven}

# FixedAccount class attributes and methods
FixedAccount_chequeBookNo: Property = Property(name="chequeBookNo", type=StringType)
FixedAccount.attributes={FixedAccount_chequeBookNo}

# Relationships
Bank_BankAccount: BinaryAssociation = BinaryAssociation(
    name="Bank_BankAccount",
    ends={
        Property(name="bankAccount0", type=BankAccount, multiplicity=Multiplicity(0, 9999)),
        Property(name="bank1", type=Bank, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_38d4887b_f28c_48b9_9dc2_df0889e33807",
    types={Bank, BankAccount, SavingsAccount, FixedAccount},
    associations={Bank_BankAccount},
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