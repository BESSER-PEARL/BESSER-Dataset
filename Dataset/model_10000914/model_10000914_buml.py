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

account_AccountType: Enumeration = Enumeration(
    name="account_AccountType",
    literals={
            
    }
)

# Classes
Customer = Class(name="Customer")
Login = Class(name="Login")
transaction_Transaction = Class(name="transaction_Transaction")
transaction_DepositTransaction = Class(name="transaction_DepositTransaction")
transaction_WithdrawTransaction = Class(name="transaction_WithdrawTransaction")
transaction_TransferTransaction = Class(name="transaction_TransferTransaction")
account_SavingsAccount = Class(name="account_SavingsAccount")
account_CertificatesOfDepositAccount = Class(name="account_CertificatesOfDepositAccount")
account_CheckingAccount = Class(name="account_CheckingAccount")
account_Account = Class(name="account_Account")
Class_ = Class(name="Class")
gerente = Class(name="gerente")
Cliente = Class(name="Cliente")
Login1 = Class(name="Login1")
Personas = Class(name="Personas")
Direccion = Class(name="Direccion")

# Customer class attributes and methods
Customer_name: Property = Property(name="name", type=StringType)
Customer_dateOfBirth: Property = Property(name="dateOfBirth", type=DateType)
Customer_address: Property = Property(name="address", type=StringType)
Customer_phoneNumber: Property = Property(name="phoneNumber", type=StringType)
Customer_emailAddress: Property = Property(name="emailAddress", type=StringType)
Customer.attributes={Customer_name, Customer_address, Customer_dateOfBirth, Customer_phoneNumber, Customer_emailAddress}

# Login class attributes and methods
Login_username: Property = Property(name="username", type=StringType)
Login_securityAnswer: Property = Property(name="securityAnswer", type=StringType)
Login_password: Property = Property(name="password", type=StringType)
Login_securityQuestion: Property = Property(name="securityQuestion", type=StringType)
Login_lastLoginTime: Property = Property(name="lastLoginTime", type=DateType)
Login.attributes={Login_securityAnswer, Login_username, Login_lastLoginTime, Login_securityQuestion, Login_password}

# transaction_Transaction class attributes and methods
transaction_Transaction_id: Property = Property(name="id", type=IntegerType)
transaction_Transaction_type: Property = Property(name="type", type=transaction_TransactionType)
transaction_Transaction_transactionTime: Property = Property(name="transactionTime", type=DateType)
transaction_Transaction_amount: Property = Property(name="amount", type=FloatType)
transaction_Transaction.attributes={transaction_Transaction_type, transaction_Transaction_id, transaction_Transaction_transactionTime, transaction_Transaction_amount}

# transaction_DepositTransaction class attributes and methods

# transaction_WithdrawTransaction class attributes and methods

# transaction_TransferTransaction class attributes and methods
transaction_TransferTransaction_targetAccount: Property = Property(name="targetAccount", type=account_Account)
transaction_TransferTransaction_sourceAccount: Property = Property(name="sourceAccount", type=account_Account)
transaction_TransferTransaction.attributes={transaction_TransferTransaction_sourceAccount, transaction_TransferTransaction_targetAccount}

# account_SavingsAccount class attributes and methods
account_SavingsAccount_interestRate: Property = Property(name="interestRate", type=FloatType)
account_SavingsAccount.attributes={account_SavingsAccount_interestRate}

# account_CertificatesOfDepositAccount class attributes and methods
account_CertificatesOfDepositAccount_timePeriod: Property = Property(name="timePeriod", type=IntegerType)
account_CertificatesOfDepositAccount_interestRate: Property = Property(name="interestRate", type=FloatType)
account_CertificatesOfDepositAccount.attributes={account_CertificatesOfDepositAccount_timePeriod, account_CertificatesOfDepositAccount_interestRate}

# account_CheckingAccount class attributes and methods
account_CheckingAccount_name: Property = Property(name="name", type=StringType)
account_CheckingAccount.attributes={account_CheckingAccount_name}

# account_Account class attributes and methods
account_Account_accountNo: Property = Property(name="accountNo", type=StringType)
account_Account_type: Property = Property(name="type", type=account_AccountType)
account_Account_balance: Property = Property(name="balance", type=FloatType)
account_Account.attributes={account_Account_balance, account_Account_type, account_Account_accountNo}

# Class class attributes and methods
Class__attribute: Property = Property(name="attribute", type=StringType)
Class__attribute2: Property = Property(name="attribute2", type=StringType)
Class_.attributes={Class__attribute2, Class__attribute}

# gerente class attributes and methods
gerente_idGerente: Property = Property(name="idGerente", type=IntegerType)
gerente_idPersona: Property = Property(name="idPersona", type=StringType)
gerente_id: Property = Property(name="id", type=StringType)
gerente_idZona: Property = Property(name="idZona", type=IntegerType)
gerente_idUsuario: Property = Property(name="idUsuario", type=IntegerType)
gerente.attributes={gerente_idUsuario, gerente_idZona, gerente_id, gerente_idPersona, gerente_idGerente}

# Cliente class attributes and methods
Cliente_idCliente: Property = Property(name="idCliente", type=IntegerType)
Cliente_noTarjeta: Property = Property(name="noTarjeta", type=StringType)
Cliente_idPersona: Property = Property(name="idPersona", type=IntegerType)
Cliente_idDireccion: Property = Property(name="idDireccion", type=IntegerType)
Cliente_idPrestamo: Property = Property(name="idPrestamo", type=IntegerType)
Cliente_idDiaPago: Property = Property(name="idDiaPago", type=IntegerType)
Cliente_idAval: Property = Property(name="idAval", type=IntegerType)
Cliente_contactoReferencia: Property = Property(name="contactoReferencia", type=StringType)
Cliente_fechaInicio: Property = Property(name="fechaInicio", type=DateType)
Cliente.attributes={Cliente_idAval, Cliente_idCliente, Cliente_idPrestamo, Cliente_noTarjeta, Cliente_idDireccion, Cliente_idDiaPago, Cliente_idPersona, Cliente_contactoReferencia, Cliente_fechaInicio}

# Login1 class attributes and methods
Login1_usuario: Property = Property(name="usuario", type=StringType)
Login1_password: Property = Property(name="password", type=StringType)
Login1.attributes={Login1_usuario, Login1_password}

# Personas class attributes and methods
Personas_idPersona: Property = Property(name="idPersona", type=IntegerType)
Personas_nombre: Property = Property(name="nombre", type=StringType)
Personas_aPaterno: Property = Property(name="aPaterno", type=StringType)
Personas_aMaterno: Property = Property(name="aMaterno", type=StringType)
Personas_telefono: Property = Property(name="telefono", type=StringType)
Personas_estado: Property = Property(name="estado", type=StringType)
Personas.attributes={Personas_aMaterno, Personas_aPaterno, Personas_telefono, Personas_nombre, Personas_estado, Personas_idPersona}

# Direccion class attributes and methods
Direccion_idDireccion: Property = Property(name="idDireccion", type=IntegerType)
Direccion_idEstado: Property = Property(name="idEstado", type=IntegerType)
Direccion_estado: Property = Property(name="estado", type=StringType)
Direccion_idMunicipio: Property = Property(name="idMunicipio", type=IntegerType)
Direccion_municipio: Property = Property(name="municipio", type=StringType)
Direccion_ciudad: Property = Property(name="ciudad", type=StringType)
Direccion_zona: Property = Property(name="zona", type=StringType)
Direccion_cp: Property = Property(name="cp", type=IntegerType)
Direccion_asentamiento: Property = Property(name="asentamiento", type=StringType)
Direccion_tipo: Property = Property(name="tipo", type=StringType)
Direccion.attributes={Direccion_idDireccion, Direccion_zona, Direccion_ciudad, Direccion_tipo, Direccion_estado, Direccion_idMunicipio, Direccion_idEstado, Direccion_municipio, Direccion_cp, Direccion_asentamiento}

# Relationships
association2: BinaryAssociation = BinaryAssociation(
    name="association2",
    ends={
        Property(name="customer0", type=Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="a1", type=account_Account, multiplicity=Multiplicity(1, 9999))
    }
)
Account_Transaction: BinaryAssociation = BinaryAssociation(
    name="Account_Transaction",
    ends={
        Property(name="transactions2", type=transaction_Transaction, multiplicity=Multiplicity(0, 9999)),
        Property(name="account3", type=account_Account, multiplicity=Multiplicity(1, 1))
    }
)
Customer_Login: BinaryAssociation = BinaryAssociation(
    name="Customer_Login",
    ends={
        Property(name="login4", type=Login, multiplicity=Multiplicity(0, 1)),
        Property(name="customer5", type=Customer, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_6f173e09_8bba_4529_844e_39b6a1ca68c9",
    types={Customer, Login, transaction_Transaction, transaction_DepositTransaction, transaction_WithdrawTransaction, transaction_TransferTransaction, account_SavingsAccount, account_CertificatesOfDepositAccount, account_CheckingAccount, account_Account, Class_, gerente, Cliente, Login1, Personas, Direccion, transaction_TransactionType, account_AccountType},
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