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
Exame = Class(name="Exame")
Paciente = Class(name="Paciente")
Consulta = Class(name="Consulta")
Funcion_rio = Class(name="Funcion_rio")
Agendamento = Class(name="Agendamento")
M_dico = Class(name="M_dico")

# Exame class attributes and methods
Exame_TipoExame: Property = Property(name="TipoExame", type=StringType)
Exame_Especialista: Property = Property(name="Especialista", type=StringType)
Exame_Medico: Property = Property(name="Medico", type=StringType)
Exame_Sede: Property = Property(name="Sede", type=StringType)
Exame.attributes={Exame_Especialista, Exame_Sede, Exame_TipoExame, Exame_Medico}

# Paciente class attributes and methods
Paciente_CPF: Property = Property(name="CPF", type=Paciente)
Paciente_Nome: Property = Property(name="Nome", type=StringType)
Paciente_Sobrenome: Property = Property(name="Sobrenome", type=StringType)
Paciente_DataNascimento: Property = Property(name="DataNascimento", type=StringType)
Paciente_CPF1: Property = Property(name="CPF1", type=IntegerType)
Paciente_RG: Property = Property(name="RG", type=IntegerType)
Paciente_Nacionalidade: Property = Property(name="Nacionalidade", type=StringType)
Paciente_Estado: Property = Property(name="Estado", type=StringType)
Paciente_Cidade: Property = Property(name="Cidade", type=StringType)
Paciente_CEP: Property = Property(name="CEP", type=IntegerType)
Paciente_Endereco: Property = Property(name="Endereco", type=StringType)
Paciente_Sexo: Property = Property(name="Sexo", type=StringType)
Paciente_EstadoCivil: Property = Property(name="EstadoCivil", type=StringType)
Paciente_Telefone: Property = Property(name="Telefone", type=IntegerType)
Paciente_Celular: Property = Property(name="Celular", type=IntegerType)
Paciente_Email: Property = Property(name="Email", type=StringType)
Paciente_ConvenioMedico: Property = Property(name="ConvenioMedico", type=StringType)
Paciente.attributes={Paciente_Telefone, Paciente_ConvenioMedico, Paciente_Celular, Paciente_Endereco, Paciente_CPF, Paciente_Cidade, Paciente_CEP, Paciente_Sexo, Paciente_CPF1, Paciente_Nacionalidade, Paciente_Nome, Paciente_Estado, Paciente_RG, Paciente_Email, Paciente_DataNascimento, Paciente_EstadoCivil, Paciente_Sobrenome}

# Consulta class attributes and methods
Consulta_TipoConsulta: Property = Property(name="TipoConsulta", type=StringType)
Consulta_Especialista: Property = Property(name="Especialista", type=StringType)
Consulta_Medico: Property = Property(name="Medico", type=StringType)
Consulta_Sede: Property = Property(name="Sede", type=StringType)
Consulta.attributes={Consulta_Sede, Consulta_Medico, Consulta_Especialista, Consulta_TipoConsulta}

# Funcion_rio class attributes and methods
Funcion_rio_Usuario: Property = Property(name="Usuario", type=StringType)
Funcion_rio_Senha: Property = Property(name="Senha", type=StringType)
Funcion_rio.attributes={Funcion_rio_Usuario, Funcion_rio_Senha}

# Agendamento class attributes and methods
Agendamento_TipoAgendamento: Property = Property(name="TipoAgendamento", type=StringType)
Agendamento_Especialista: Property = Property(name="Especialista", type=StringType)
Agendamento_Sede: Property = Property(name="Sede", type=StringType)
Agendamento_Medico: Property = Property(name="Medico", type=StringType)
Agendamento_Dia_e_Horario: Property = Property(name="Dia_e_Horario", type=StringType)
Agendamento.attributes={Agendamento_TipoAgendamento, Agendamento_Especialista, Agendamento_Dia_e_Horario, Agendamento_Sede, Agendamento_Medico}

# M_dico class attributes and methods
M_dico_Nome: Property = Property(name="Nome", type=StringType)
M_dico_Especialidade: Property = Property(name="Especialidade", type=StringType)
M_dico_CPF: Property = Property(name="CPF", type=IntegerType)
M_dico.attributes={M_dico_CPF, M_dico_Nome, M_dico_Especialidade}

# Relationships
Agendamento_Exame: BinaryAssociation = BinaryAssociation(
    name="Agendamento_Exame",
    ends={
        Property(name="exame0", type=Exame, multiplicity=Multiplicity(0, 1)),
        Property(name="agendamento1", type=Agendamento, multiplicity=Multiplicity(0, 1))
    }
)
Agendamento_Consulta: BinaryAssociation = BinaryAssociation(
    name="Agendamento_Consulta",
    ends={
        Property(name="consulta2", type=Consulta, multiplicity=Multiplicity(0, 1)),
        Property(name="agendamento3", type=Agendamento, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_Wf158HN2Eem42bdoMoG80w",
    types={Exame, Paciente, Consulta, Funcion_rio, Agendamento, M_dico},
    associations={Agendamento_Exame, Agendamento_Consulta},
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