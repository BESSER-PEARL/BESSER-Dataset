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
BankAccount = Class(name="BankAccount")
SavingsAccount = Class(name="SavingsAccount")
FixedAccount = Class(name="FixedAccount")

# BankAccount class attributes and methods
BankAccount_balance: Property = Property(name="balance", type=FloatType)
BankAccount_accountHolderName: Property = Property(name="accountHolderName", type=StringType)
BankAccount.attributes={BankAccount_accountHolderName, BankAccount_balance}

# SavingsAccount class attributes and methods

# FixedAccount class attributes and methods

# Domain Model
domain_model = DomainModel(
    name="_WCRwwNmQEeaNv5kMq1wesg",
    types={BankAccount, SavingsAccount, FixedAccount},
    associations={},
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