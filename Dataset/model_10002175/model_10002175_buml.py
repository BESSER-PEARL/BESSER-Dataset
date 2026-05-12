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

TransactionType2: Enumeration = Enumeration(
    name="TransactionType2",
    literals={
            
    }
)

# Classes
Customer = Class(name="Customer")
Account_Interface = Class(name="Account_Interface")
Savings_Account = Class(name="Savings_Account")
Bank = Class(name="Bank")
Transaction = Class(name="Transaction")
ATM_Card = Class(name="ATM_Card")
WithdrawTransaction = Class(name="WithdrawTransaction")
TransferTransaction = Class(name="TransferTransaction")
DepositTransaction = Class(name="DepositTransaction")
Customer2 = Class(name="Customer2")
Account2_Interface = Class(name="Account2_Interface")
Savings_Account2 = Class(name="Savings_Account2")
Bank2 = Class(name="Bank2")
Transaction2 = Class(name="Transaction2")
ATM_Card2 = Class(name="ATM_Card2")
WithdrawTransaction2 = Class(name="WithdrawTransaction2")
TransferTransaction2 = Class(name="TransferTransaction2")
DepositTransaction2 = Class(name="DepositTransaction2")

# Customer class attributes and methods
Customer_name: Property = Property(name="name", type=StringType)
Customer_dateOfBirth: Property = Property(name="dateOfBirth", type=DateType)
Customer_address: Property = Property(name="address", type=StringType)
Customer_phoneNumber: Property = Property(name="phoneNumber", type=StringType)
Customer_emailAddress: Property = Property(name="emailAddress", type=StringType)
Customer.attributes={Customer_phoneNumber, Customer_dateOfBirth, Customer_address, Customer_emailAddress, Customer_name}

# Account_Interface class attributes and methods

# Savings_Account class attributes and methods
Savings_Account_accountNumber: Property = Property(name="accountNumber", type=StringType)
Savings_Account_balance: Property = Property(name="balance", type=IntegerType)
Savings_Account.attributes={Savings_Account_balance, Savings_Account_accountNumber}

# Bank class attributes and methods
Bank_code: Property = Property(name="code", type=StringType)
Bank_address: Property = Property(name="address", type=StringType)
Bank.attributes={Bank_code, Bank_address}

# Transaction class attributes and methods
Transaction_id: Property = Property(name="id", type=IntegerType)
Transaction_type: Property = Property(name="type", type=TransactionType)
Transaction_transactionTime: Property = Property(name="transactionTime", type=DateType)
Transaction_amount: Property = Property(name="amount", type=FloatType)
Transaction.attributes={Transaction_transactionTime, Transaction_id, Transaction_amount, Transaction_type}

# ATM_Card class attributes and methods
ATM_Card_cardNumber: Property = Property(name="cardNumber", type=StringType)
ATM_Card_pin: Property = Property(name="pin", type=StringType)
ATM_Card.attributes={ATM_Card_pin, ATM_Card_cardNumber}

# WithdrawTransaction class attributes and methods

# TransferTransaction class attributes and methods
TransferTransaction_targetAccount: Property = Property(name="targetAccount", type=StringType)
TransferTransaction_sourceAccount: Property = Property(name="sourceAccount", type=StringType)
TransferTransaction.attributes={TransferTransaction_sourceAccount, TransferTransaction_targetAccount}

# DepositTransaction class attributes and methods

# Customer2 class attributes and methods
Customer2_name: Property = Property(name="name", type=StringType)
Customer2_dateOfBirth: Property = Property(name="dateOfBirth", type=DateType)
Customer2_address: Property = Property(name="address", type=StringType)
Customer2_phoneNumber: Property = Property(name="phoneNumber", type=StringType)
Customer2_emailAddress: Property = Property(name="emailAddress", type=StringType)
Customer2.attributes={Customer2_dateOfBirth, Customer2_address, Customer2_name, Customer2_emailAddress, Customer2_phoneNumber}

# Account2_Interface class attributes and methods

# Savings_Account2 class attributes and methods
Savings_Account2_accountNumber: Property = Property(name="accountNumber", type=StringType)
Savings_Account2_balance: Property = Property(name="balance", type=IntegerType)
Savings_Account2.attributes={Savings_Account2_accountNumber, Savings_Account2_balance}

# Bank2 class attributes and methods
Bank2_code: Property = Property(name="code", type=StringType)
Bank2_address: Property = Property(name="address", type=StringType)
Bank2.attributes={Bank2_address, Bank2_code}

# Transaction2 class attributes and methods
Transaction2_id: Property = Property(name="id", type=IntegerType)
Transaction2_type: Property = Property(name="type", type=TransactionType)
Transaction2_transactionTime: Property = Property(name="transactionTime", type=DateType)
Transaction2_amount: Property = Property(name="amount", type=FloatType)
Transaction2.attributes={Transaction2_id, Transaction2_transactionTime, Transaction2_type, Transaction2_amount}

# ATM_Card2 class attributes and methods
ATM_Card2_cardNumber: Property = Property(name="cardNumber", type=StringType)
ATM_Card2_pin: Property = Property(name="pin", type=StringType)
ATM_Card2.attributes={ATM_Card2_cardNumber, ATM_Card2_pin}

# WithdrawTransaction2 class attributes and methods

# TransferTransaction2 class attributes and methods
TransferTransaction2_targetAccount: Property = Property(name="targetAccount", type=StringType)
TransferTransaction2_sourceAccount: Property = Property(name="sourceAccount", type=StringType)
TransferTransaction2.attributes={TransferTransaction2_sourceAccount, TransferTransaction2_targetAccount}

# DepositTransaction2 class attributes and methods

# Domain Model
domain_model = DomainModel(
    name="_uUXJ0DzVEemQWcstM2zleA",
    types={Customer, Account_Interface, Savings_Account, Bank, Transaction, ATM_Card, WithdrawTransaction, TransferTransaction, DepositTransaction, Customer2, Account2_Interface, Savings_Account2, Bank2, Transaction2, ATM_Card2, WithdrawTransaction2, TransferTransaction2, DepositTransaction2, TransactionType, TransactionType2},
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