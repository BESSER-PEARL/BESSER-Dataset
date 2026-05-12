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
transacao_TransactionType: Enumeration = Enumeration(
    name="transacao_TransactionType",
    literals={
            
    }
)

conta_AccountType: Enumeration = Enumeration(
    name="conta_AccountType",
    literals={
            
    }
)

# Classes
cliente_Customer = Class(name="cliente_Customer")
transacao_transacao = Class(name="transacao_transacao")
transacao_deposito = Class(name="transacao_deposito")
transacao_saque = Class(name="transacao_saque")
transacao_transferencia = Class(name="transacao_transferencia")
transacao_Class = Class(name="transacao_Class")
conta_investimento = Class(name="conta_investimento")
conta_Poupan_a = Class(name="conta_Poupan_a")
conta_CheckingAccount = Class(name="conta_CheckingAccount")
conta_Conta = Class(name="conta_Conta")
conta = Class(name="conta")
Login = Class(name="Login")
NewClass = Class(name="NewClass")

# cliente_Customer class attributes and methods
cliente_Customer_nome: Property = Property(name="nome", type=StringType)
cliente_Customer_dataNascimento: Property = Property(name="dataNascimento", type=DateType)
cliente_Customer_endere_o: Property = Property(name="endere_o", type=StringType)
cliente_Customer_numeroTel: Property = Property(name="numeroTel", type=StringType)
cliente_Customer_email: Property = Property(name="email", type=StringType)
cliente_Customer.attributes={cliente_Customer_dataNascimento, cliente_Customer_numeroTel, cliente_Customer_nome, cliente_Customer_email, cliente_Customer_endere_o}

# transacao_transacao class attributes and methods
transacao_transacao_id: Property = Property(name="id", type=IntegerType)
transacao_transacao_type: Property = Property(name="type", type=StringType)
transacao_transacao_amount: Property = Property(name="amount", type=FloatType)
transacao_transacao.attributes={transacao_transacao_id, transacao_transacao_type, transacao_transacao_amount}

# transacao_deposito class attributes and methods
transacao_deposito_valor: Property = Property(name="valor", type=StringType)
transacao_deposito.attributes={transacao_deposito_valor}

# transacao_saque class attributes and methods
transacao_saque_valor: Property = Property(name="valor", type=StringType)
transacao_saque.attributes={transacao_saque_valor}

# transacao_transferencia class attributes and methods
transacao_transferencia_contaAlvo: Property = Property(name="contaAlvo", type=conta_Conta)
transacao_transferencia_contaOrigem: Property = Property(name="contaOrigem", type=conta_Conta)
transacao_transferencia.attributes={transacao_transferencia_contaAlvo, transacao_transferencia_contaOrigem}

# transacao_Class class attributes and methods

# conta_investimento class attributes and methods
conta_investimento_taxaDeJuros: Property = Property(name="taxaDeJuros", type=FloatType)
conta_investimento.attributes={conta_investimento_taxaDeJuros}

# conta_Poupan_a class attributes and methods
conta_Poupan_a_juros: Property = Property(name="juros", type=FloatType)
conta_Poupan_a_tempo: Property = Property(name="tempo", type=IntegerType)
conta_Poupan_a.attributes={conta_Poupan_a_tempo, conta_Poupan_a_juros}

# conta_CheckingAccount class attributes and methods

# conta_Conta class attributes and methods
conta_Conta_tipo: Property = Property(name="tipo", type=conta_AccountType)
conta_Conta_saldo: Property = Property(name="saldo", type=FloatType)
conta_Conta.attributes={conta_Conta_tipo, conta_Conta_saldo}

# conta class attributes and methods
conta__attr: Property = Property(name="_attr", type=StringType)
conta.attributes={conta__attr}

# Login class attributes and methods
Login_username: Property = Property(name="username", type=StringType)
Login_password: Property = Property(name="password", type=StringType)
Login_lastLoginTime: Property = Property(name="lastLoginTime", type=DateType)
Login.attributes={Login_password, Login_username, Login_lastLoginTime}

# NewClass class attributes and methods

# Relationships
association2: BinaryAssociation = BinaryAssociation(
    name="association2",
    ends={
        Property(name="cliente0", type=cliente_Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="conta1", type=conta_Conta, multiplicity=Multiplicity(1, 9999))
    }
)
Customer_Login: BinaryAssociation = BinaryAssociation(
    name="Customer_Login",
    ends={
        Property(name="login2", type=Login, multiplicity=Multiplicity(0, 1)),
        Property(name="cliente3", type=cliente_Customer, multiplicity=Multiplicity(1, 1))
    }
)
Account_Transaction: BinaryAssociation = BinaryAssociation(
    name="Account_Transaction",
    ends={
        Property(name="transacao4", type=transacao_transacao, multiplicity=Multiplicity(0, 9999)),
        Property(name="conta5", type=conta_Conta, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_Pj1tMBQAEeqDmNBP3mfLQg",
    types={cliente_Customer, transacao_transacao, transacao_deposito, transacao_saque, transacao_transferencia, transacao_Class, conta_investimento, conta_Poupan_a, conta_CheckingAccount, conta_Conta, conta, Login, NewClass, transacao_TransactionType, conta_AccountType},
    associations={association2, Customer_Login, Account_Transaction},
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