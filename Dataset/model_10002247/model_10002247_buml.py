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
enu: Enumeration = Enumeration(
    name="enu",
    literals={
            
    }
)

# Classes
Interacao = Class(name="Interacao")
TipoSanguineo = Class(name="TipoSanguineo")
TipoMedicamento = Class(name="TipoMedicamento")
LocalExame = Class(name="LocalExame")
Exame = Class(name="Exame")
Endereco = Class(name="Endereco")
Pessoa = Class(name="Pessoa")
Telefone = Class(name="Telefone")
Paciente = Class(name="Paciente")
Medicamento = Class(name="Medicamento")
Naturalidade = Class(name="Naturalidade")
ProfissionalSaude = Class(name="ProfissionalSaude")
Mensagem = Class(name="Mensagem")
LinhaCuidado = Class(name="LinhaCuidado")

# Interacao class attributes and methods

# TipoSanguineo class attributes and methods
TipoSanguineo_nome: Property = Property(name="nome", type=StringType)
TipoSanguineo.attributes={TipoSanguineo_nome}

# TipoMedicamento class attributes and methods
TipoMedicamento_nome: Property = Property(name="nome", type=StringType)
TipoMedicamento.attributes={TipoMedicamento_nome}

# LocalExame class attributes and methods
LocalExame_nome: Property = Property(name="nome", type=StringType)
LocalExame.attributes={LocalExame_nome}

# Exame class attributes and methods
Exame_data: Property = Property(name="data", type=StringType)
Exame_nome: Property = Property(name="nome", type=StringType)
Exame_descricao: Property = Property(name="descricao", type=StringType)
Exame.attributes={Exame_data, Exame_nome, Exame_descricao}

# Endereco class attributes and methods
Endereco_numero: Property = Property(name="numero", type=IntegerType)
Endereco_logradouro: Property = Property(name="logradouro", type=StringType)
Endereco_bairro: Property = Property(name="bairro", type=StringType)
Endereco_cidade: Property = Property(name="cidade", type=StringType)
Endereco_cep: Property = Property(name="cep", type=StringType)
Endereco.attributes={Endereco_cep, Endereco_cidade, Endereco_logradouro, Endereco_numero, Endereco_bairro}

# Pessoa class attributes and methods
Pessoa_dataNascimento: Property = Property(name="dataNascimento", type=StringType)
Pessoa_cpf: Property = Property(name="cpf", type=StringType)
Pessoa_dataInclusao: Property = Property(name="dataInclusao", type=StringType)
Pessoa_sexo: Property = Property(name="sexo", type=StringType)
Pessoa_email: Property = Property(name="email", type=StringType)
Pessoa_senha: Property = Property(name="senha", type=StringType)
Pessoa_ultimoAcesso: Property = Property(name="ultimoAcesso", type=StringType)
Pessoa.attributes={Pessoa_dataNascimento, Pessoa_sexo, Pessoa_ultimoAcesso, Pessoa_email, Pessoa_senha, Pessoa_cpf, Pessoa_dataInclusao}

# Telefone class attributes and methods
Telefone_ddd: Property = Property(name="ddd", type=IntegerType)
Telefone_tipo: Property = Property(name="tipo", type=StringType)
Telefone_numero: Property = Property(name="numero", type=StringType)
Telefone.attributes={Telefone_ddd, Telefone_numero, Telefone_tipo}

# Paciente class attributes and methods

# Medicamento class attributes and methods
Medicamento_nome: Property = Property(name="nome", type=StringType)
Medicamento_descricao: Property = Property(name="descricao", type=StringType)
Medicamento_horaInicial: Property = Property(name="horaInicial", type=StringType)
Medicamento_ativo: Property = Property(name="ativo", type=BooleanType)
Medicamento_intervaloTempo: Property = Property(name="intervaloTempo", type=IntegerType)
Medicamento_dataInicio: Property = Property(name="dataInicio", type=StringType)
Medicamento_dataFim: Property = Property(name="dataFim", type=StringType)
Medicamento.attributes={Medicamento_descricao, Medicamento_intervaloTempo, Medicamento_ativo, Medicamento_horaInicial, Medicamento_dataInicio, Medicamento_dataFim, Medicamento_nome}

# Naturalidade class attributes and methods
Naturalidade_naturalidade: Property = Property(name="naturalidade", type=StringType)
Naturalidade.attributes={Naturalidade_naturalidade}

# ProfissionalSaude class attributes and methods

# Mensagem class attributes and methods
Mensagem_assunto: Property = Property(name="assunto", type=StringType)
Mensagem_mensagem: Property = Property(name="mensagem", type=StringType)
Mensagem_dataEnvio: Property = Property(name="dataEnvio", type=StringType)
Mensagem_geral: Property = Property(name="geral", type=BooleanType)
Mensagem.attributes={Mensagem_mensagem, Mensagem_assunto, Mensagem_geral, Mensagem_dataEnvio}

# LinhaCuidado class attributes and methods
LinhaCuidado_nome: Property = Property(name="nome", type=StringType)
LinhaCuidado_descricao: Property = Property(name="descricao", type=IntegerType)
LinhaCuidado.attributes={LinhaCuidado_descricao, LinhaCuidado_nome}

# Relationships
Est__em: BinaryAssociation = BinaryAssociation(
    name="Est__em",
    ends={
        Property(name="exame0", type=Exame, multiplicity=Multiplicity(0, 9999)),
        Property(name="localExame1", type=LocalExame, multiplicity=Multiplicity(1, 1))
    }
)
LocalExame_Endereco: BinaryAssociation = BinaryAssociation(
    name="LocalExame_Endereco",
    ends={
        Property(name="endereco2", type=Endereco, multiplicity=Multiplicity(1, 1)),
        Property(name="localExame3", type=LocalExame, multiplicity=Multiplicity(1, 1))
    }
)
Endereco_Pessoa: BinaryAssociation = BinaryAssociation(
    name="Endereco_Pessoa",
    ends={
        Property(name="pessoa4", type=Pessoa, multiplicity=Multiplicity(1, 1)),
        Property(name="endereco5", type=Endereco, multiplicity=Multiplicity(1, 1))
    }
)
Pessoa_Telefone: BinaryAssociation = BinaryAssociation(
    name="Pessoa_Telefone",
    ends={
        Property(name="telefone6", type=Telefone, multiplicity=Multiplicity(0, 1)),
        Property(name="pessoa7", type=Pessoa, multiplicity=Multiplicity(0, 1))
    }
)
Mensagem_LinhaCuidado: BinaryAssociation = BinaryAssociation(
    name="Mensagem_LinhaCuidado",
    ends={
        Property(name="linhaCuidado14", type=LinhaCuidado, multiplicity=Multiplicity(0, 1)),
        Property(name="mensagem15", type=Mensagem, multiplicity=Multiplicity(0, 9999))
    }
)
Interacao_Mensagem: BinaryAssociation = BinaryAssociation(
    name="Interacao_Mensagem",
    ends={
        Property(name="mensagem16", type=Mensagem, multiplicity=Multiplicity(0, 1)),
        Property(name="interacao17", type=Interacao, multiplicity=Multiplicity(0, 9999))
    }
)
Paciente_Interacao: BinaryAssociation = BinaryAssociation(
    name="Paciente_Interacao",
    ends={
        Property(name="interacao18", type=Interacao, multiplicity=Multiplicity(0, 9999)),
        Property(name="paciente19", type=Paciente, multiplicity=Multiplicity(1, 1))
    }
)
Paciente_Mensagem: BinaryAssociation = BinaryAssociation(
    name="Paciente_Mensagem",
    ends={
        Property(name="mensagem20", type=Mensagem, multiplicity=Multiplicity(0, 1)),
        Property(name="paciente21", type=Paciente, multiplicity=Multiplicity(0, 1))
    }
)
TipoSanguineo_Paciente: BinaryAssociation = BinaryAssociation(
    name="TipoSanguineo_Paciente",
    ends={
        Property(name="paciente22", type=Paciente, multiplicity=Multiplicity(0, 9999)),
        Property(name="tipoSanguineo23", type=TipoSanguineo, multiplicity=Multiplicity(0, 1))
    }
)
Paciente_Medicamento: BinaryAssociation = BinaryAssociation(
    name="Paciente_Medicamento",
    ends={
        Property(name="medicamento8", type=Medicamento, multiplicity=Multiplicity(0, 9999)),
        Property(name="paciente9", type=Paciente, multiplicity=Multiplicity(1, 1))
    }
)
Pessoa_Naturalidade: BinaryAssociation = BinaryAssociation(
    name="Pessoa_Naturalidade",
    ends={
        Property(name="naturalidade10", type=Naturalidade, multiplicity=Multiplicity(1, 1)),
        Property(name="pessoa11", type=Pessoa, multiplicity=Multiplicity(0, 9999))
    }
)
ProfissioanlSaude_Mensagem: BinaryAssociation = BinaryAssociation(
    name="ProfissioanlSaude_Mensagem",
    ends={
        Property(name="mensagem12", type=Mensagem, multiplicity=Multiplicity(0, 9999)),
        Property(name="profissionalSaude13", type=ProfissionalSaude, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_zDFX4Mt4Eeib_M6EW71F_A",
    types={Interacao, TipoSanguineo, TipoMedicamento, LocalExame, Exame, Endereco, Pessoa, Telefone, Paciente, Medicamento, Naturalidade, ProfissionalSaude, Mensagem, LinhaCuidado, enu},
    associations={Est__em, LocalExame_Endereco, Endereco_Pessoa, Pessoa_Telefone, Mensagem_LinhaCuidado, Interacao_Mensagem, Paciente_Interacao, Paciente_Mensagem, TipoSanguineo_Paciente, Paciente_Medicamento, Pessoa_Naturalidade, ProfissioanlSaude_Mensagem},
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