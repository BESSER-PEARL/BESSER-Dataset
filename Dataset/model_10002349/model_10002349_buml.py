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

Medical_Record_AccountType: Enumeration = Enumeration(
    name="Medical_Record_AccountType",
    literals={
            
    }
)

# Classes
transaction_Interface = Class(name="transaction_Interface")
transaction_Mental_Health_Trust = Class(name="transaction_Mental_Health_Trust")
transaction_Acute_Hospital = Class(name="transaction_Acute_Hospital")
transaction_Community_Hospital = Class(name="transaction_Community_Hospital")
Medical_Record_SavingsAccount = Class(name="Medical_Record_SavingsAccount")
Medical_Record_CertificatesOfDepositAccount = Class(name="Medical_Record_CertificatesOfDepositAccount")
Medical_Record_CheckingAccount = Class(name="Medical_Record_CheckingAccount")
Medical_Record_NHS_Number = Class(name="Medical_Record_NHS_Number")
MyInterface_Interface = Class(name="MyInterface_Interface")
Patient = Class(name="Patient")
Login = Class(name="Login")

# transaction_Interface class attributes and methods
transaction_Interface_id: Property = Property(name="id", type=IntegerType)
transaction_Interface_type: Property = Property(name="type", type=transaction_TransactionType)
transaction_Interface_transactionTime: Property = Property(name="transactionTime", type=DateType)
transaction_Interface_amount: Property = Property(name="amount", type=FloatType)
transaction_Interface.attributes={transaction_Interface_transactionTime, transaction_Interface_id, transaction_Interface_type, transaction_Interface_amount}

# transaction_Mental_Health_Trust class attributes and methods

# transaction_Acute_Hospital class attributes and methods

# transaction_Community_Hospital class attributes and methods
transaction_Community_Hospital_targetAccount: Property = Property(name="targetAccount", type=Medical_Record_NHS_Number)
transaction_Community_Hospital_sourceAccount: Property = Property(name="sourceAccount", type=Medical_Record_NHS_Number)
transaction_Community_Hospital.attributes={transaction_Community_Hospital_targetAccount, transaction_Community_Hospital_sourceAccount}

# Medical_Record_SavingsAccount class attributes and methods
Medical_Record_SavingsAccount_interestRate: Property = Property(name="interestRate", type=FloatType)
Medical_Record_SavingsAccount.attributes={Medical_Record_SavingsAccount_interestRate}

# Medical_Record_CertificatesOfDepositAccount class attributes and methods
Medical_Record_CertificatesOfDepositAccount_timePeriod: Property = Property(name="timePeriod", type=IntegerType)
Medical_Record_CertificatesOfDepositAccount_interestRate: Property = Property(name="interestRate", type=FloatType)
Medical_Record_CertificatesOfDepositAccount.attributes={Medical_Record_CertificatesOfDepositAccount_timePeriod, Medical_Record_CertificatesOfDepositAccount_interestRate}

# Medical_Record_CheckingAccount class attributes and methods
Medical_Record_CheckingAccount_name: Property = Property(name="name", type=StringType)
Medical_Record_CheckingAccount.attributes={Medical_Record_CheckingAccount_name}

# Medical_Record_NHS_Number class attributes and methods
Medical_Record_NHS_Number_accountNo: Property = Property(name="accountNo", type=StringType)
Medical_Record_NHS_Number_type: Property = Property(name="type", type=Medical_Record_AccountType)
Medical_Record_NHS_Number_balance: Property = Property(name="balance", type=FloatType)
Medical_Record_NHS_Number.attributes={Medical_Record_NHS_Number_balance, Medical_Record_NHS_Number_accountNo, Medical_Record_NHS_Number_type}

# MyInterface_Interface class attributes and methods

# Patient class attributes and methods
Patient_name: Property = Property(name="name", type=StringType)
Patient_dateOfBirth: Property = Property(name="dateOfBirth", type=DateType)
Patient_address: Property = Property(name="address", type=StringType)
Patient_phoneNumber: Property = Property(name="phoneNumber", type=StringType)
Patient_emailAddress: Property = Property(name="emailAddress", type=StringType)
Patient_GP_Address: Property = Property(name="GP_Address", type=StringType)
Patient.attributes={Patient_GP_Address, Patient_name, Patient_address, Patient_emailAddress, Patient_dateOfBirth, Patient_phoneNumber}

# Login class attributes and methods
Login_username: Property = Property(name="username", type=StringType)
Login_securityAnswer: Property = Property(name="securityAnswer", type=StringType)
Login_password: Property = Property(name="password", type=StringType)
Login_securityQuestion: Property = Property(name="securityQuestion", type=StringType)
Login_lastLoginTime: Property = Property(name="lastLoginTime", type=DateType)
Login.attributes={Login_password, Login_lastLoginTime, Login_username, Login_securityAnswer, Login_securityQuestion}

# Relationships
association2: BinaryAssociation = BinaryAssociation(
    name="association2",
    ends={
        Property(name="Patient0", type=Patient, multiplicity=Multiplicity(1, 1)),
        Property(name="a1", type=Medical_Record_NHS_Number, multiplicity=Multiplicity(1, 9999))
    }
)
Account_Transaction: BinaryAssociation = BinaryAssociation(
    name="Account_Transaction",
    ends={
        Property(name="record_search2", type=transaction_Interface, multiplicity=Multiplicity(0, 9999)),
        Property(name="account3", type=Medical_Record_NHS_Number, multiplicity=Multiplicity(1, 1))
    }
)
Customer_Login: BinaryAssociation = BinaryAssociation(
    name="Customer_Login",
    ends={
        Property(name="login4", type=Login, multiplicity=Multiplicity(0, 1)),
        Property(name="customer5", type=Patient, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="ab137531_5b5d_4bbe_a6d0_c6bb16400b55",
    types={transaction_Interface, transaction_Mental_Health_Trust, transaction_Acute_Hospital, transaction_Community_Hospital, Medical_Record_SavingsAccount, Medical_Record_CertificatesOfDepositAccount, Medical_Record_CheckingAccount, Medical_Record_NHS_Number, MyInterface_Interface, Patient, Login, transaction_TransactionType, Medical_Record_AccountType},
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