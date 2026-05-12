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
transaction_TransactionType: Enumeration = Enumeration(
    name="transaction_TransactionType",
    literals={
            
    }
)

Conta_AccountType: Enumeration = Enumeration(
    name="Conta_AccountType",
    literals={
            
    }
)

# Classes
Cliente = Class(name="Cliente")
Login = Class(name="Login")
transaction_Transaction = Class(name="transaction_Transaction")
transaction_DepositTransaction = Class(name="transaction_DepositTransaction")
transaction_WithdrawTransaction = Class(name="transaction_WithdrawTransaction")
transaction_TransferTransaction = Class(name="transaction_TransferTransaction")
Conta_SavingsAccount = Class(name="Conta_SavingsAccount")
Conta_CertificatesOfDepositAccount = Class(name="Conta_CertificatesOfDepositAccount")
Conta_CheckingAccount = Class(name="Conta_CheckingAccount")
Conta_Conta = Class(name="Conta_Conta")

# Cliente class attributes and methods
Cliente_name: Property = Property(name="name", type=StringType)
Cliente_dateOfBirth: Property = Property(name="dateOfBirth", type=DateType)
Cliente_address: Property = Property(name="address", type=StringType)
Cliente_phoneNumber: Property = Property(name="phoneNumber", type=StringType)
Cliente_emailAddress: Property = Property(name="emailAddress", type=StringType)
Cliente.attributes={Cliente_dateOfBirth, Cliente_name, Cliente_phoneNumber, Cliente_address, Cliente_emailAddress}

# Login class attributes and methods
Login_username: Property = Property(name="username", type=StringType)
Login_securityAnswer: Property = Property(name="securityAnswer", type=StringType)
Login_password: Property = Property(name="password", type=StringType)
Login_securityQuestion: Property = Property(name="securityQuestion", type=StringType)
Login_lastLoginTime: Property = Property(name="lastLoginTime", type=DateType)
Login.attributes={Login_password, Login_securityQuestion, Login_lastLoginTime, Login_securityAnswer, Login_username}

# transaction_Transaction class attributes and methods
transaction_Transaction_id: Property = Property(name="id", type=IntegerType)
transaction_Transaction_type: Property = Property(name="type", type=transaction_TransactionType)
transaction_Transaction_transactionTime: Property = Property(name="transactionTime", type=DateType)
transaction_Transaction_amount: Property = Property(name="amount", type=FloatType)
transaction_Transaction.attributes={transaction_Transaction_id, transaction_Transaction_type, transaction_Transaction_amount, transaction_Transaction_transactionTime}

# transaction_DepositTransaction class attributes and methods

# transaction_WithdrawTransaction class attributes and methods

# transaction_TransferTransaction class attributes and methods
transaction_TransferTransaction_targetAccount: Property = Property(name="targetAccount", type=Conta_Conta)
transaction_TransferTransaction_sourceAccount: Property = Property(name="sourceAccount", type=Conta_Conta)
transaction_TransferTransaction.attributes={transaction_TransferTransaction_sourceAccount, transaction_TransferTransaction_targetAccount}

# Conta_SavingsAccount class attributes and methods
Conta_SavingsAccount_interestRate: Property = Property(name="interestRate", type=FloatType)
Conta_SavingsAccount.attributes={Conta_SavingsAccount_interestRate}

# Conta_CertificatesOfDepositAccount class attributes and methods
Conta_CertificatesOfDepositAccount_timePeriod: Property = Property(name="timePeriod", type=IntegerType)
Conta_CertificatesOfDepositAccount_interestRate: Property = Property(name="interestRate", type=FloatType)
Conta_CertificatesOfDepositAccount.attributes={Conta_CertificatesOfDepositAccount_interestRate, Conta_CertificatesOfDepositAccount_timePeriod}

# Conta_CheckingAccount class attributes and methods
Conta_CheckingAccount_name: Property = Property(name="name", type=StringType)
Conta_CheckingAccount.attributes={Conta_CheckingAccount_name}

# Conta_Conta class attributes and methods
Conta_Conta_contanum: Property = Property(name="contanum", type=StringType)
Conta_Conta_type: Property = Property(name="type", type=Conta_AccountType)
Conta_Conta_balance: Property = Property(name="balance", type=FloatType)
Conta_Conta.attributes={Conta_Conta_balance, Conta_Conta_type, Conta_Conta_contanum}

# Relationships
association2: BinaryAssociation = BinaryAssociation(
    name="association2",
    ends={
        Property(name="customer0", type=Cliente, multiplicity=Multiplicity(1, 1)),
        Property(name="a1", type=Conta_Conta, multiplicity=Multiplicity(1, 9999))
    }
)
Account_Transaction: BinaryAssociation = BinaryAssociation(
    name="Account_Transaction",
    ends={
        Property(name="transactions2", type=transaction_Transaction, multiplicity=Multiplicity(0, 9999)),
        Property(name="account3", type=Conta_Conta, multiplicity=Multiplicity(1, 1))
    }
)
Customer_Login: BinaryAssociation = BinaryAssociation(
    name="Customer_Login",
    ends={
        Property(name="login4", type=Login, multiplicity=Multiplicity(0, 1)),
        Property(name="customer5", type=Cliente, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_99b214c4_0a80_4d05_bfcd_5913689b3422",
    types={Cliente, Login, transaction_Transaction, transaction_DepositTransaction, transaction_WithdrawTransaction, transaction_TransferTransaction, Conta_SavingsAccount, Conta_CertificatesOfDepositAccount, Conta_CheckingAccount, Conta_Conta, transaction_TransactionType, Conta_AccountType},
    associations={association2, Account_Transaction, Customer_Login},
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