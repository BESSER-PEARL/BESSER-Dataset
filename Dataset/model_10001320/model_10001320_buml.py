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
Funcionario = Class(name="Funcionario")
Agenda = Class(name="Agenda")
Cid = Class(name="Cid")
Exame = Class(name="Exame")
Medicamento = Class(name="Medicamento")
Paciente = Class(name="Paciente")
Consulta = Class(name="Consulta")
ConsultaCid = Class(name="ConsultaCid")
ConsultaMedicamento = Class(name="ConsultaMedicamento")
ConsultaExame = Class(name="ConsultaExame")
Especialidade = Class(name="Especialidade")

# Funcionario class attributes and methods
Funcionario_Id: Property = Property(name="Id", type=IntegerType)
Funcionario_Nome: Property = Property(name="Nome", type=StringType)
Funcionario_Login: Property = Property(name="Login", type=StringType)
Funcionario_Senha: Property = Property(name="Senha", type=StringType)
Funcionario_Perfil: Property = Property(name="Perfil", type=IntegerType)
Funcionario.attributes={Funcionario_Login, Funcionario_Senha, Funcionario_Perfil, Funcionario_Id, Funcionario_Nome}

# Agenda class attributes and methods

# Cid class attributes and methods
Cid_Id: Property = Property(name="Id", type=IntegerType)
Cid_Codigo: Property = Property(name="Codigo", type=StringType)
Cid_Descricao: Property = Property(name="Descricao", type=StringType)
Cid.attributes={Cid_Descricao, Cid_Id, Cid_Codigo}

# Exame class attributes and methods
Exame_Id: Property = Property(name="Id", type=IntegerType)
Exame_Codigo: Property = Property(name="Codigo", type=StringType)
Exame_Descricao: Property = Property(name="Descricao", type=StringType)
Exame.attributes={Exame_Id, Exame_Codigo, Exame_Descricao}

# Medicamento class attributes and methods
Medicamento_Id: Property = Property(name="Id", type=IntegerType)
Medicamento_NomeGenerico: Property = Property(name="NomeGenerico", type=StringType)
Medicamento_NomeComercial: Property = Property(name="NomeComercial", type=StringType)
Medicamento_Fabricante: Property = Property(name="Fabricante", type=StringType)
Medicamento.attributes={Medicamento_NomeComercial, Medicamento_NomeGenerico, Medicamento_Id, Medicamento_Fabricante}

# Paciente class attributes and methods
Paciente_Id: Property = Property(name="Id", type=IntegerType)
Paciente_Nome: Property = Property(name="Nome", type=StringType)
Paciente_NomeMae: Property = Property(name="NomeMae", type=StringType)
Paciente_CPF: Property = Property(name="CPF", type=StringType)
Paciente_DataNascimento: Property = Property(name="DataNascimento", type=StringType)
Paciente.attributes={Paciente_NomeMae, Paciente_DataNascimento, Paciente_Id, Paciente_CPF, Paciente_Nome}

# Consulta class attributes and methods
Consulta_DataHora: Property = Property(name="DataHora", type=StringType)
Consulta_PacienteId: Property = Property(name="PacienteId", type=Paciente)
Consulta_MedicoId: Property = Property(name="MedicoId", type=Funcionario)
Consulta_Queixas: Property = Property(name="Queixas", type=StringType)
Consulta.attributes={Consulta_MedicoId, Consulta_DataHora, Consulta_PacienteId, Consulta_Queixas}

# ConsultaCid class attributes and methods
ConsultaCid_ConsultaId: Property = Property(name="ConsultaId", type=IntegerType)
ConsultaCid_CidId: Property = Property(name="CidId", type=IntegerType)
ConsultaCid.attributes={ConsultaCid_CidId, ConsultaCid_ConsultaId}

# ConsultaMedicamento class attributes and methods
ConsultaMedicamento_Posologia: Property = Property(name="Posologia", type=StringType)
ConsultaMedicamento_MedicamentoId: Property = Property(name="MedicamentoId", type=Medicamento)
ConsultaMedicamento.attributes={ConsultaMedicamento_MedicamentoId, ConsultaMedicamento_Posologia}

# ConsultaExame class attributes and methods
ConsultaExame_Entregue: Property = Property(name="Entregue", type=BooleanType)
ConsultaExame.attributes={ConsultaExame_Entregue}

# Especialidade class attributes and methods
Especialidade_Id: Property = Property(name="Id", type=IntegerType)
Especialidade_Descricao: Property = Property(name="Descricao", type=StringType)
Especialidade.attributes={Especialidade_Id, Especialidade_Descricao}

# Relationships
ConsultaMedicamento_Consulta: BinaryAssociation = BinaryAssociation(
    name="ConsultaMedicamento_Consulta",
    ends={
        Property(name="consulta12", type=Consulta, multiplicity=Multiplicity(0, 1)),
        Property(name="consultaMedicamento13", type=ConsultaMedicamento, multiplicity=Multiplicity(0, 1))
    }
)
Exame_ConsultaExame: BinaryAssociation = BinaryAssociation(
    name="Exame_ConsultaExame",
    ends={
        Property(name="consultaExame14", type=ConsultaExame, multiplicity=Multiplicity(0, 1)),
        Property(name="exame15", type=Exame, multiplicity=Multiplicity(0, 1))
    }
)
Consulta_ConsultaExame: BinaryAssociation = BinaryAssociation(
    name="Consulta_ConsultaExame",
    ends={
        Property(name="consultaExame16", type=ConsultaExame, multiplicity=Multiplicity(0, 1)),
        Property(name="consulta17", type=Consulta, multiplicity=Multiplicity(0, 1))
    }
)
Agenda_Funcionario: BinaryAssociation = BinaryAssociation(
    name="Agenda_Funcionario",
    ends={
        Property(name="funcionario0", type=Funcionario, multiplicity=Multiplicity(1, 1)),
        Property(name="agenda1", type=Agenda, multiplicity=Multiplicity(0, 1))
    }
)
Agenda_Especialidade: BinaryAssociation = BinaryAssociation(
    name="Agenda_Especialidade",
    ends={
        Property(name="especialidade2", type=Especialidade, multiplicity=Multiplicity(1, 1)),
        Property(name="agenda3", type=Agenda, multiplicity=Multiplicity(1, 9999))
    }
)
Paciente_Consulta: BinaryAssociation = BinaryAssociation(
    name="Paciente_Consulta",
    ends={
        Property(name="consulta4", type=Consulta, multiplicity=Multiplicity(0, 9999)),
        Property(name="paciente5", type=Paciente, multiplicity=Multiplicity(0, 1))
    }
)
Consulta_ConsultaCid: BinaryAssociation = BinaryAssociation(
    name="Consulta_ConsultaCid",
    ends={
        Property(name="consultaCid6", type=ConsultaCid, multiplicity=Multiplicity(0, 1)),
        Property(name="consulta7", type=Consulta, multiplicity=Multiplicity(0, 9999))
    }
)
Cid_ConsultaCid: BinaryAssociation = BinaryAssociation(
    name="Cid_ConsultaCid",
    ends={
        Property(name="consultaCid8", type=ConsultaCid, multiplicity=Multiplicity(0, 1)),
        Property(name="cid9", type=Cid, multiplicity=Multiplicity(0, 1))
    }
)
ConsultaMedicamento_Medicamento: BinaryAssociation = BinaryAssociation(
    name="ConsultaMedicamento_Medicamento",
    ends={
        Property(name="medicamento10", type=Medicamento, multiplicity=Multiplicity(0, 1)),
        Property(name="consultaMedicamento11", type=ConsultaMedicamento, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="__jXSIJwuEeiZ_ZsBRXzEyQ",
    types={Funcionario, Agenda, Cid, Exame, Medicamento, Paciente, Consulta, ConsultaCid, ConsultaMedicamento, ConsultaExame, Especialidade},
    associations={ConsultaMedicamento_Consulta, Exame_ConsultaExame, Consulta_ConsultaExame, Agenda_Funcionario, Agenda_Especialidade, Paciente_Consulta, Consulta_ConsultaCid, Cid_ConsultaCid, ConsultaMedicamento_Medicamento},
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