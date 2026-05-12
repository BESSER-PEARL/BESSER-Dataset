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
Checking = Class(name="Checking")
Instructor = Class(name="Instructor")
Main = Class(name="Main")
Savings = Class(name="Savings")
Student = Class(name="Student")

# BankAccount class attributes and methods
BankAccount_numOfTransactions: Property = Property(name="numOfTransactions", type=IntegerType)
BankAccount_TRANSACTION_FEE: Property = Property(name="TRANSACTION_FEE", type=IntegerType)
BankAccount_FREE_TRANSACTIONS: Property = Property(name="FREE_TRANSACTIONS", type=IntegerType)
BankAccount_balance: Property = Property(name="balance", type=FloatType)
BankAccount_minimumBalance: Property = Property(name="minimumBalance", type=FloatType)
BankAccount_isActive: Property = Property(name="isActive", type=BooleanType)
BankAccount.attributes={BankAccount_balance, BankAccount_TRANSACTION_FEE, BankAccount_FREE_TRANSACTIONS, BankAccount_minimumBalance, BankAccount_numOfTransactions, BankAccount_isActive}

# Checking class attributes and methods
Checking_OVERDRAFT_LIMIT: Property = Property(name="OVERDRAFT_LIMIT", type=FloatType)
Checking_OVERDRAFT_FEE: Property = Property(name="OVERDRAFT_FEE", type=FloatType)
Checking_isActive: Property = Property(name="isActive", type=BooleanType)
Checking.attributes={Checking_isActive, Checking_OVERDRAFT_FEE, Checking_OVERDRAFT_LIMIT}

# Instructor class attributes and methods
Instructor_name: Property = Property(name="name", type=StringType)
Instructor.attributes={Instructor_name}

# Main class attributes and methods

# Savings class attributes and methods

# Student class attributes and methods
Student_name: Property = Property(name="name", type=StringType)
Student.attributes={Student_name}

# Relationships
Savings_Instructor: BinaryAssociation = BinaryAssociation(
    name="Savings_Instructor",
    ends={
        Property(name="savings7", type=Savings, multiplicity=Multiplicity(0, 1)),
        Property(name="instructor6", type=Instructor, multiplicity=Multiplicity(0, 1))
    }
)
Checking_Student: BinaryAssociation = BinaryAssociation(
    name="Checking_Student",
    ends={
        Property(name="student0", type=Student, multiplicity=Multiplicity(0, 1)),
        Property(name="checking1", type=Checking, multiplicity=Multiplicity(0, 1))
    }
)
Savings_Student: BinaryAssociation = BinaryAssociation(
    name="Savings_Student",
    ends={
        Property(name="student2", type=Student, multiplicity=Multiplicity(0, 1)),
        Property(name="savings3", type=Savings, multiplicity=Multiplicity(0, 1))
    }
)
Checking_Instructor: BinaryAssociation = BinaryAssociation(
    name="Checking_Instructor",
    ends={
        Property(name="instructor4", type=Instructor, multiplicity=Multiplicity(0, 1)),
        Property(name="checking5", type=Checking, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="__Vp8gLeQEee7sYPkE4_GPA",
    types={BankAccount, Checking, Instructor, Main, Savings, Student},
    associations={Savings_Instructor, Checking_Student, Savings_Student, Checking_Instructor},
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