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
clinicasaudeperfeita_Paciente = Class(name="clinicasaudeperfeita_Paciente")
clinicasaudeperfeita_Compromisso = Class(name="clinicasaudeperfeita_Compromisso")
clinicasaudeperfeita_Consulta = Class(name="clinicasaudeperfeita_Consulta")
clinicasaudeperfeita_Exame = Class(name="clinicasaudeperfeita_Exame")
clinicasaudeperfeita_Medicamento = Class(name="clinicasaudeperfeita_Medicamento")
clinicasaudeperfeita_Recepcionista = Class(name="clinicasaudeperfeita_Recepcionista")
clinicasaudeperfeita_Medico = Class(name="clinicasaudeperfeita_Medico")
Exame = Class(name="Exame")
clinicasaudeperfeita_Paciente_Actor = Class(name="clinicasaudeperfeita_Paciente_Actor")
clinicasaudeperfeita_Analisa_consulta_UseCase = Class(name="clinicasaudeperfeita_Analisa_consulta_UseCase")
clinicasaudeperfeita_Recepcionista_Actor = Class(name="clinicasaudeperfeita_Recepcionista_Actor")
clinicasaudeperfeita_Marca_consulta_UseCase = Class(name="clinicasaudeperfeita_Marca_consulta_UseCase")
clinicasaudeperfeita_Medico_Actor = Class(name="clinicasaudeperfeita_Medico_Actor")
clinicasaudeperfeita_Consulta_UseCase = Class(name="clinicasaudeperfeita_Consulta_UseCase")

# clinicasaudeperfeita_Paciente class attributes and methods
clinicasaudeperfeita_Paciente_nome: Property = Property(name="nome", type=StringType)
clinicasaudeperfeita_Paciente_idade: Property = Property(name="idade", type=IntegerType)
clinicasaudeperfeita_Paciente_cpf: Property = Property(name="cpf", type=StringType)
clinicasaudeperfeita_Paciente_cSus: Property = Property(name="cSus", type=StringType)
clinicasaudeperfeita_Paciente.attributes={clinicasaudeperfeita_Paciente_cpf, clinicasaudeperfeita_Paciente_cSus, clinicasaudeperfeita_Paciente_idade, clinicasaudeperfeita_Paciente_nome}

# clinicasaudeperfeita_Compromisso class attributes and methods
clinicasaudeperfeita_Compromisso_descricao: Property = Property(name="descricao", type=StringType)
clinicasaudeperfeita_Compromisso_data: Property = Property(name="data", type=StringType)
clinicasaudeperfeita_Compromisso_hora: Property = Property(name="hora", type=StringType)
clinicasaudeperfeita_Compromisso.attributes={clinicasaudeperfeita_Compromisso_data, clinicasaudeperfeita_Compromisso_descricao, clinicasaudeperfeita_Compromisso_hora}

# clinicasaudeperfeita_Consulta class attributes and methods
clinicasaudeperfeita_Consulta_problemasPaciente: Property = Property(name="problemasPaciente", type=StringType)
clinicasaudeperfeita_Consulta_orientacoesMedicas: Property = Property(name="orientacoesMedicas", type=StringType)
clinicasaudeperfeita_Consulta_medico: Property = Property(name="medico", type=clinicasaudeperfeita_Medico)
clinicasaudeperfeita_Consulta_paciente: Property = Property(name="paciente", type=clinicasaudeperfeita_Paciente)
clinicasaudeperfeita_Consulta_data: Property = Property(name="data", type=StringType)
clinicasaudeperfeita_Consulta_hora: Property = Property(name="hora", type=StringType)
clinicasaudeperfeita_Consulta_marcada: Property = Property(name="marcada", type=BooleanType)
clinicasaudeperfeita_Consulta_realizada: Property = Property(name="realizada", type=BooleanType)
clinicasaudeperfeita_Consulta_medicamentos: Property = Property(name="medicamentos", type=clinicasaudeperfeita_Medicamento)
clinicasaudeperfeita_Consulta_exame: Property = Property(name="exame", type=Exame)
clinicasaudeperfeita_Consulta.attributes={clinicasaudeperfeita_Consulta_paciente, clinicasaudeperfeita_Consulta_orientacoesMedicas, clinicasaudeperfeita_Consulta_marcada, clinicasaudeperfeita_Consulta_medicamentos, clinicasaudeperfeita_Consulta_hora, clinicasaudeperfeita_Consulta_data, clinicasaudeperfeita_Consulta_problemasPaciente, clinicasaudeperfeita_Consulta_exame, clinicasaudeperfeita_Consulta_realizada, clinicasaudeperfeita_Consulta_medico}

# clinicasaudeperfeita_Exame class attributes and methods
clinicasaudeperfeita_Exame_nome: Property = Property(name="nome", type=StringType)
clinicasaudeperfeita_Exame.attributes={clinicasaudeperfeita_Exame_nome}

# clinicasaudeperfeita_Medicamento class attributes and methods
clinicasaudeperfeita_Medicamento_nome: Property = Property(name="nome", type=StringType)
clinicasaudeperfeita_Medicamento.attributes={clinicasaudeperfeita_Medicamento_nome}

# clinicasaudeperfeita_Recepcionista class attributes and methods
clinicasaudeperfeita_Recepcionista_nome: Property = Property(name="nome", type=StringType)
clinicasaudeperfeita_Recepcionista_idade: Property = Property(name="idade", type=IntegerType)
clinicasaudeperfeita_Recepcionista_cpf: Property = Property(name="cpf", type=StringType)
clinicasaudeperfeita_Recepcionista.attributes={clinicasaudeperfeita_Recepcionista_idade, clinicasaudeperfeita_Recepcionista_nome, clinicasaudeperfeita_Recepcionista_cpf}

# clinicasaudeperfeita_Medico class attributes and methods
clinicasaudeperfeita_Medico_nome: Property = Property(name="nome", type=StringType)
clinicasaudeperfeita_Medico_idade: Property = Property(name="idade", type=IntegerType)
clinicasaudeperfeita_Medico_cpf: Property = Property(name="cpf", type=StringType)
clinicasaudeperfeita_Medico_agenda: Property = Property(name="agenda", type=clinicasaudeperfeita_Compromisso)
clinicasaudeperfeita_Medico.attributes={clinicasaudeperfeita_Medico_agenda, clinicasaudeperfeita_Medico_idade, clinicasaudeperfeita_Medico_cpf, clinicasaudeperfeita_Medico_nome}

# Exame class attributes and methods

# clinicasaudeperfeita_Paciente_Actor class attributes and methods

# clinicasaudeperfeita_Analisa_consulta_UseCase class attributes and methods

# clinicasaudeperfeita_Recepcionista_Actor class attributes and methods

# clinicasaudeperfeita_Marca_consulta_UseCase class attributes and methods

# clinicasaudeperfeita_Medico_Actor class attributes and methods

# clinicasaudeperfeita_Consulta_UseCase class attributes and methods

# Relationships
Medico_Consulta: BinaryAssociation = BinaryAssociation(
    name="Medico_Consulta",
    ends={
        Property(name="prescrita2", type=clinicasaudeperfeita_Consulta, multiplicity=Multiplicity(0, 9999)),
        Property(name="prescreve3", type=clinicasaudeperfeita_Medico, multiplicity=Multiplicity(1, 1))
    }
)
Compromisso_Medico: BinaryAssociation = BinaryAssociation(
    name="Compromisso_Medico",
    ends={
        Property(name="medico4", type=clinicasaudeperfeita_Medico, multiplicity=Multiplicity(0, 1)),
        Property(name="tem5", type=clinicasaudeperfeita_Compromisso, multiplicity=Multiplicity(0, 9999))
    }
)
Medicamento_Consulta: BinaryAssociation = BinaryAssociation(
    name="Medicamento_Consulta",
    ends={
        Property(name="consulta6", type=clinicasaudeperfeita_Consulta, multiplicity=Multiplicity(0, 1)),
        Property(name="prescreve7", type=clinicasaudeperfeita_Medicamento, multiplicity=Multiplicity(0, 9999))
    }
)
Exame_Consulta: BinaryAssociation = BinaryAssociation(
    name="Exame_Consulta",
    ends={
        Property(name="consulta8", type=clinicasaudeperfeita_Consulta, multiplicity=Multiplicity(0, 1)),
        Property(name="solicita9", type=clinicasaudeperfeita_Exame, multiplicity=Multiplicity(0, 9999))
    }
)
Recepcionista_Consulta: BinaryAssociation = BinaryAssociation(
    name="Recepcionista_Consulta",
    ends={
        Property(name="consulta10", type=clinicasaudeperfeita_Consulta, multiplicity=Multiplicity(0, 9999)),
        Property(name="recepcionista11", type=clinicasaudeperfeita_Recepcionista, multiplicity=Multiplicity(1, 1))
    }
)
Paciente_analizaConsulta: BinaryAssociation = BinaryAssociation(
    name="Paciente_analizaConsulta",
    ends={
        Property(name="analizaConsulta12", type=clinicasaudeperfeita_Analisa_consulta_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="paciente13", type=clinicasaudeperfeita_Paciente_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Consulta_Medico: BinaryAssociation = BinaryAssociation(
    name="Consulta_Medico",
    ends={
        Property(name="medico14", type=clinicasaudeperfeita_Medico_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="consulta15", type=clinicasaudeperfeita_Consulta_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Recepcionista_Marca_consulta: BinaryAssociation = BinaryAssociation(
    name="Recepcionista_Marca_consulta",
    ends={
        Property(name="marca_consulta16", type=clinicasaudeperfeita_Marca_consulta_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="recepcionista17", type=clinicasaudeperfeita_Recepcionista_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Paciente_Consulta: BinaryAssociation = BinaryAssociation(
    name="Paciente_Consulta",
    ends={
        Property(name="__consultado0", type=clinicasaudeperfeita_Consulta, multiplicity=Multiplicity(0, 9999)),
        Property(name="consultado1", type=clinicasaudeperfeita_Paciente, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_jpUkAMgUEeiZ3fREAmKE6g",
    types={clinicasaudeperfeita_Paciente, clinicasaudeperfeita_Compromisso, clinicasaudeperfeita_Consulta, clinicasaudeperfeita_Exame, clinicasaudeperfeita_Medicamento, clinicasaudeperfeita_Recepcionista, clinicasaudeperfeita_Medico, Exame, clinicasaudeperfeita_Paciente_Actor, clinicasaudeperfeita_Analisa_consulta_UseCase, clinicasaudeperfeita_Recepcionista_Actor, clinicasaudeperfeita_Marca_consulta_UseCase, clinicasaudeperfeita_Medico_Actor, clinicasaudeperfeita_Consulta_UseCase},
    associations={Medico_Consulta, Compromisso_Medico, Medicamento_Consulta, Exame_Consulta, Recepcionista_Consulta, Paciente_analizaConsulta, Consulta_Medico, Recepcionista_Marca_consulta, Paciente_Consulta},
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