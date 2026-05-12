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
Enumeration_: Enumeration = Enumeration(
    name="Enumeration",
    literals={
            
    }
)

# Classes
Banco = Class(name="Banco")
ContaBancaria = Class(name="ContaBancaria")
SalvarConta = Class(name="SalvarConta")
FixedAccount = Class(name="FixedAccount")
SistemaInterno = Class(name="SistemaInterno")
IAutenticavel = Class(name="IAutenticavel")
Autenticavel = Class(name="Autenticavel")
Class_ = Class(name="Class")
Conta_Corrente = Class(name="Conta_Corrente")
Conta_Poupan_a = Class(name="Conta_Poupan_a")
CRUD = Class(name="CRUD")
Remover_Conta = Class(name="Remover_Conta")
Conta_Conjunta = Class(name="Conta_Conjunta")
Conta_Normal = Class(name="Conta_Normal")
Emprestimo = Class(name="Emprestimo")
Cofre = Class(name="Cofre")
Transferencia = Class(name="Transferencia")
Deposito = Class(name="Deposito")

# Banco class attributes and methods
Banco_NomeBanco: Property = Property(name="NomeBanco", type=StringType)
Banco.attributes={Banco_NomeBanco}

# ContaBancaria class attributes and methods
ContaBancaria_NumeroConta: Property = Property(name="NumeroConta", type=IntegerType)
ContaBancaria_NomeConta: Property = Property(name="NomeConta", type=StringType)
ContaBancaria_Saldo: Property = Property(name="Saldo", type=FloatType)
ContaBancaria.attributes={ContaBancaria_NomeConta, ContaBancaria_NumeroConta, ContaBancaria_Saldo}

# SalvarConta class attributes and methods
SalvarConta_interestRate: Property = Property(name="interestRate", type=FloatType)
SalvarConta_noticeGiven: Property = Property(name="noticeGiven", type=BooleanType)
SalvarConta.attributes={SalvarConta_interestRate, SalvarConta_noticeGiven}

# FixedAccount class attributes and methods
FixedAccount_chequeBookNo: Property = Property(name="chequeBookNo", type=StringType)
FixedAccount.attributes={FixedAccount_chequeBookNo}

# SistemaInterno class attributes and methods
SistemaInterno_Entrar: Property = Property(name="Entrar", type=IAutenticavel)
SistemaInterno__attr: Property = Property(name="_attr", type=IAutenticavel)
SistemaInterno__attr1: Property = Property(name="_attr1", type=StringType)
SistemaInterno.attributes={SistemaInterno__attr, SistemaInterno__attr1, SistemaInterno_Entrar}

# IAutenticavel class attributes and methods
IAutenticavel_Autenticar: Property = Property(name="Autenticar", type=StringType)
IAutenticavel.attributes={IAutenticavel_Autenticar}

# Autenticavel class attributes and methods
Autenticavel_Autenticar: Property = Property(name="Autenticar", type=StringType)
Autenticavel_Senha: Property = Property(name="Senha", type=StringType)
Autenticavel.attributes={Autenticavel_Senha, Autenticavel_Autenticar}

# Class class attributes and methods

# Conta_Corrente class attributes and methods
Conta_Corrente_Nome: Property = Property(name="Nome", type=StringType)
Conta_Corrente_CPF: Property = Property(name="CPF", type=IntegerType)
Conta_Corrente_Senha: Property = Property(name="Senha", type=FloatType)
Conta_Corrente_Taxa_de_Movimenta__o: Property = Property(name="Taxa_de_Movimenta__o", type=FloatType)
Conta_Corrente.attributes={Conta_Corrente_CPF, Conta_Corrente_Nome, Conta_Corrente_Senha, Conta_Corrente_Taxa_de_Movimenta__o}

# Conta_Poupan_a class attributes and methods
Conta_Poupan_a_Nome: Property = Property(name="Nome", type=StringType)
Conta_Poupan_a_CPF: Property = Property(name="CPF", type=IntegerType)
Conta_Poupan_a_Senha: Property = Property(name="Senha", type=FloatType)
Conta_Poupan_a.attributes={Conta_Poupan_a_CPF, Conta_Poupan_a_Senha, Conta_Poupan_a_Nome}

# CRUD class attributes and methods
CRUD_Adicionar_Conta: Property = Property(name="Adicionar_Conta", type=StringType)
CRUD_Remover_Conta: Property = Property(name="Remover_Conta", type=StringType)
CRUD.attributes={CRUD_Remover_Conta, CRUD_Adicionar_Conta}

# Remover_Conta class attributes and methods

# Conta_Conjunta class attributes and methods
Conta_Conjunta_id: Property = Property(name="id", type=IntegerType)
Conta_Conjunta.attributes={Conta_Conjunta_id}

# Conta_Normal class attributes and methods
Conta_Normal_id: Property = Property(name="id", type=IntegerType)
Conta_Normal.attributes={Conta_Normal_id}

# Emprestimo class attributes and methods
Emprestimo_Valor: Property = Property(name="Valor", type=FloatType)
Emprestimo.attributes={Emprestimo_Valor}

# Cofre class attributes and methods
Cofre_Dinheiro_Armazenado: Property = Property(name="Dinheiro_Armazenado", type=FloatType)
Cofre_Emprestimo_Total: Property = Property(name="Emprestimo_Total", type=FloatType)
Cofre.attributes={Cofre_Emprestimo_Total, Cofre_Dinheiro_Armazenado}

# Transferencia class attributes and methods
Transferencia_Nome: Property = Property(name="Nome", type=StringType)
Transferencia_Valor: Property = Property(name="Valor", type=FloatType)
Transferencia.attributes={Transferencia_Nome, Transferencia_Valor}

# Deposito class attributes and methods
Deposito_Nome: Property = Property(name="Nome", type=StringType)
Deposito_Valor: Property = Property(name="Valor", type=FloatType)
Deposito.attributes={Deposito_Valor, Deposito_Nome}

# Relationships
Bank_BankAccount: BinaryAssociation = BinaryAssociation(
    name="Bank_BankAccount",
    ends={
        Property(name="bankAccount0", type=ContaBancaria, multiplicity=Multiplicity(0, 9999)),
        Property(name="bank1", type=Banco, multiplicity=Multiplicity(1, 1))
    }
)
I_I: BinaryAssociation = BinaryAssociation(
    name="I_I",
    ends={
        Property(name="i2", type=IAutenticavel, multiplicity=Multiplicity(0, 1)),
        Property(name="i3", type=IAutenticavel, multiplicity=Multiplicity(0, 1))
    }
)
Autenticavel_ContaBancaria: BinaryAssociation = BinaryAssociation(
    name="Autenticavel_ContaBancaria",
    ends={
        Property(name="contaBancaria4", type=ContaBancaria, multiplicity=Multiplicity(0, 1)),
        Property(name="autenticavel5", type=Autenticavel, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_2a19a040_41c3_4ba4_a4a2_c377630c7ad0",
    types={Banco, ContaBancaria, SalvarConta, FixedAccount, SistemaInterno, IAutenticavel, Autenticavel, Class_, Conta_Corrente, Conta_Poupan_a, CRUD, Remover_Conta, Conta_Conjunta, Conta_Normal, Emprestimo, Cofre, Transferencia, Deposito, Enumeration_},
    associations={Bank_BankAccount, I_I, Autenticavel_ContaBancaria},
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