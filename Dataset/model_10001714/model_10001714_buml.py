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
EnumAccountType: Enumeration = Enumeration(
    name="EnumAccountType",
    literals={
            
    }
)

TransactionType: Enumeration = Enumeration(
    name="TransactionType",
    literals={
            
    }
)

# Classes
Account = Class(name="Account")
Customer = Class(name="Customer")
Transaction = Class(name="Transaction")
checkingAccount = Class(name="checkingAccount")
savingAccount = Class(name="savingAccount")
IcalculateExtraFee_Interface = Class(name="IcalculateExtraFee_Interface")

# Account class attributes and methods
Account_accountNo: Property = Property(name="accountNo", type=IntegerType)
Account_PIN: Property = Property(name="PIN", type=IntegerType)
Account_accountType: Property = Property(name="accountType", type=EnumAccountType)
Account_openedDate: Property = Property(name="openedDate", type=StringType)
Account_availableBalance: Property = Property(name="availableBalance", type=StringType)
Account.attributes={Account_availableBalance, Account_accountType, Account_openedDate, Account_accountNo, Account_PIN}

# Customer class attributes and methods
Customer_custId: Property = Property(name="custId", type=IntegerType)
Customer_accountNo: Property = Property(name="accountNo", type=IntegerType)
Customer_firstName: Property = Property(name="firstName", type=StringType)
Customer_lastName: Property = Property(name="lastName", type=StringType)
Customer_address: Property = Property(name="address", type=StringType)
Customer.attributes={Customer_firstName, Customer_accountNo, Customer_address, Customer_lastName, Customer_custId}

# Transaction class attributes and methods
Transaction_accountNo: Property = Property(name="accountNo", type=IntegerType)
Transaction_transactionId: Property = Property(name="transactionId", type=IntegerType)
Transaction_description: Property = Property(name="description", type=StringType)
Transaction_transactionDate: Property = Property(name="transactionDate", type=StringType)
Transaction_amount: Property = Property(name="amount", type=StringType)
Transaction_transactionType: Property = Property(name="transactionType", type=TransactionType)
Transaction.attributes={Transaction_accountNo, Transaction_description, Transaction_transactionDate, Transaction_transactionId, Transaction_amount, Transaction_transactionType}

# checkingAccount class attributes and methods
checkingAccount_accountNo: Property = Property(name="accountNo", type=IntegerType)
checkingAccount_noOfTransactions: Property = Property(name="noOfTransactions", type=IntegerType)
checkingAccount.attributes={checkingAccount_accountNo, checkingAccount_noOfTransactions}

# savingAccount class attributes and methods
savingAccount_annualInterestRate: Property = Property(name="annualInterestRate", type=StringType)
savingAccount_annualGain: Property = Property(name="annualGain", type=StringType)
savingAccount_extraFee: Property = Property(name="extraFee", type=StringType)
savingAccount.attributes={savingAccount_annualGain, savingAccount_annualInterestRate, savingAccount_extraFee}

# IcalculateExtraFee_Interface class attributes and methods

# Domain Model
domain_model = DomainModel(
    name="_QHp0wOYcEeiyGtLb2crGgA",
    types={Account, Customer, Transaction, checkingAccount, savingAccount, IcalculateExtraFee_Interface, EnumAccountType, TransactionType},
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