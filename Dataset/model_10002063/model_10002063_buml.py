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
Paciente = Class(name="Paciente")
Cidade = Class(name="Cidade")
UF = Class(name="UF")
Pedido_Exame = Class(name="Pedido_Exame")
Medico = Class(name="Medico")
Exame = Class(name="Exame")
float = Class(name="float")

# Paciente class attributes and methods
Paciente_codigo: Property = Property(name="codigo", type=IntegerType)
Paciente_nome: Property = Property(name="nome", type=StringType)
Paciente_endereco: Property = Property(name="endereco", type=StringType)
Paciente_cep: Property = Property(name="cep", type=StringType)
Paciente_telefone: Property = Property(name="telefone", type=StringType)
Paciente_dataNascimento: Property = Property(name="dataNascimento", type=StringType)
Paciente_rg: Property = Property(name="rg", type=StringType)
Paciente_cpf: Property = Property(name="cpf", type=StringType)
Paciente.attributes={Paciente_nome, Paciente_telefone, Paciente_dataNascimento, Paciente_rg, Paciente_endereco, Paciente_cep, Paciente_cpf, Paciente_codigo}

# Cidade class attributes and methods
Cidade_codigo: Property = Property(name="codigo", type=IntegerType)
Cidade_nome: Property = Property(name="nome", type=StringType)
Cidade_ddd: Property = Property(name="ddd", type=IntegerType)
Cidade.attributes={Cidade_nome, Cidade_codigo, Cidade_ddd}

# UF class attributes and methods
UF_sigla: Property = Property(name="sigla", type=StringType)
UF_nome: Property = Property(name="nome", type=StringType)
UF.attributes={UF_nome, UF_sigla}

# Pedido_Exame class attributes and methods
Pedido_Exame_codigo: Property = Property(name="codigo", type=IntegerType)
Pedido_Exame.attributes={Pedido_Exame_codigo}

# Medico class attributes and methods
Medico_crm: Property = Property(name="crm", type=IntegerType)
Medico_nome: Property = Property(name="nome", type=StringType)
Medico.attributes={Medico_crm, Medico_nome}

# Exame class attributes and methods
Exame_codigo: Property = Property(name="codigo", type=IntegerType)
Exame_descricao: Property = Property(name="descricao", type=StringType)
Exame_valor: Property = Property(name="valor", type=FloatType)
Exame_procedimentos: Property = Property(name="procedimentos", type=StringType)
Exame.attributes={Exame_valor, Exame_procedimentos, Exame_descricao, Exame_codigo}

# float class attributes and methods

# Relationships
Cidade_Paciente: BinaryAssociation = BinaryAssociation(
    name="Cidade_Paciente",
    ends={
        Property(name="paciente0", type=Paciente, multiplicity=Multiplicity(1, 9999)),
        Property(name="cidade1", type=Cidade, multiplicity=Multiplicity(1, 1))
    }
)
MyClass_Cidade: BinaryAssociation = BinaryAssociation(
    name="MyClass_Cidade",
    ends={
        Property(name="cidade2", type=Cidade, multiplicity=Multiplicity(1, 1)),
        Property(name="UF3", type=UF, multiplicity=Multiplicity(1, 1))
    }
)
Pedido_Exame_Paciente: BinaryAssociation = BinaryAssociation(
    name="Pedido_Exame_Paciente",
    ends={
        Property(name="paciente4", type=Paciente, multiplicity=Multiplicity(1, 1)),
        Property(name="pedido_Exame5", type=Pedido_Exame, multiplicity=Multiplicity(1, 9999))
    }
)
Medico_Pedido_Exame: BinaryAssociation = BinaryAssociation(
    name="Medico_Pedido_Exame",
    ends={
        Property(name="pedido_Exame6", type=Pedido_Exame, multiplicity=Multiplicity(0, 9999)),
        Property(name="medico7", type=Medico, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_mNg38JPaEeeaCsv2qBF4QA",
    types={Paciente, Cidade, UF, Pedido_Exame, Medico, Exame, float},
    associations={Cidade_Paciente, MyClass_Cidade, Pedido_Exame_Paciente, Medico_Pedido_Exame},
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