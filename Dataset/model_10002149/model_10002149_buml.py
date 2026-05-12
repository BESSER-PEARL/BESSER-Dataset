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
Pessoa = Class(name="Pessoa")
Paciente = Class(name="Paciente")
Medico = Class(name="Medico")
Enfermeira = Class(name="Enfermeira")
Triagem = Class(name="Triagem")
String_Interface = Class(name="String_Interface")
Consulta = Class(name="Consulta")
Atestado = Class(name="Atestado")

# Pessoa class attributes and methods
Pessoa_nome: Property = Property(name="nome", type=StringType)
Pessoa_dataNascimento: Property = Property(name="dataNascimento", type=StringType)
Pessoa_cpf: Property = Property(name="cpf", type=StringType)
Pessoa_rg: Property = Property(name="rg", type=StringType)
Pessoa_endereco: Property = Property(name="endereco", type=StringType)
Pessoa_telefone: Property = Property(name="telefone", type=StringType)
Pessoa_estadoCivil: Property = Property(name="estadoCivil", type=StringType)
Pessoa_sexo: Property = Property(name="sexo", type=StringType)
Pessoa.attributes={Pessoa_estadoCivil, Pessoa_cpf, Pessoa_telefone, Pessoa_rg, Pessoa_endereco, Pessoa_sexo, Pessoa_nome, Pessoa_dataNascimento}

# Paciente class attributes and methods
Paciente_id: Property = Property(name="id", type=StringType)
Paciente_numeroSus: Property = Property(name="numeroSus", type=StringType)
Paciente_responsavel: Property = Property(name="responsavel", type=Pessoa)
Paciente.attributes={Paciente_responsavel, Paciente_numeroSus, Paciente_id}

# Medico class attributes and methods
Medico_crm: Property = Property(name="crm", type=StringType)
Medico_especialidade: Property = Property(name="especialidade", type=StringType)
Medico_setor: Property = Property(name="setor", type=StringType)
Medico.attributes={Medico_crm, Medico_setor, Medico_especialidade}

# Enfermeira class attributes and methods
Enfermeira_cofen: Property = Property(name="cofen", type=StringType)
Enfermeira_setor: Property = Property(name="setor", type=StringType)
Enfermeira.attributes={Enfermeira_cofen, Enfermeira_setor}

# Triagem class attributes and methods
Triagem_enfermeira: Property = Property(name="enfermeira", type=Enfermeira)
Triagem_paciente: Property = Property(name="paciente", type=Paciente)
Triagem_pressao: Property = Property(name="pressao", type=String_Interface)
Triagem_temperatura: Property = Property(name="temperatura", type=StringType)
Triagem_sintoma: Property = Property(name="sintoma", type=StringType)
Triagem_alergias: Property = Property(name="alergias", type=StringType)
Triagem_peso: Property = Property(name="peso", type=StringType)
Triagem_altura: Property = Property(name="altura", type=StringType)
Triagem_IMC: Property = Property(name="IMC", type=StringType)
Triagem_febre: Property = Property(name="febre", type=BooleanType)
Triagem.attributes={Triagem_sintoma, Triagem_peso, Triagem_paciente, Triagem_febre, Triagem_alergias, Triagem_pressao, Triagem_enfermeira, Triagem_altura, Triagem_temperatura, Triagem_IMC}

# String_Interface class attributes and methods

# Consulta class attributes and methods
Consulta_triagem: Property = Property(name="triagem", type=Triagem)
Consulta_medico: Property = Property(name="medico", type=Medico)
Consulta_medicamentos: Property = Property(name="medicamentos", type=StringType)
Consulta_diagnostico: Property = Property(name="diagnostico", type=StringType)
Consulta_atestado: Property = Property(name="atestado", type=BooleanType)
Consulta_codigoDiagnostico: Property = Property(name="codigoDiagnostico", type=StringType)
Consulta.attributes={Consulta_triagem, Consulta_codigoDiagnostico, Consulta_medico, Consulta_diagnostico, Consulta_medicamentos, Consulta_atestado}

# Atestado class attributes and methods
Atestado_dataInicioDoAtestado: Property = Property(name="dataInicioDoAtestado", type=StringType)
Atestado_dataFimDoAtestado: Property = Property(name="dataFimDoAtestado", type=StringType)
Atestado_consulta: Property = Property(name="consulta", type=Consulta)
Atestado_quantidadeDias: Property = Property(name="quantidadeDias", type=StringType)
Atestado.attributes={Atestado_consulta, Atestado_quantidadeDias, Atestado_dataInicioDoAtestado, Atestado_dataFimDoAtestado}

# Relationships
Triagem_Paciente: BinaryAssociation = BinaryAssociation(
    name="Triagem_Paciente",
    ends={
        Property(name="paciente20", type=Paciente, multiplicity=Multiplicity(0, 1)),
        Property(name="triagem1", type=Triagem, multiplicity=Multiplicity(0, 1))
    }
)
Triagem_Enfermeira: BinaryAssociation = BinaryAssociation(
    name="Triagem_Enfermeira",
    ends={
        Property(name="enfermeira22", type=Enfermeira, multiplicity=Multiplicity(0, 1)),
        Property(name="triagem3", type=Triagem, multiplicity=Multiplicity(0, 1))
    }
)
Consulta_Medico: BinaryAssociation = BinaryAssociation(
    name="Consulta_Medico",
    ends={
        Property(name="medico24", type=Medico, multiplicity=Multiplicity(0, 1)),
        Property(name="consulta5", type=Consulta, multiplicity=Multiplicity(0, 1))
    }
)
Consulta_Triagem: BinaryAssociation = BinaryAssociation(
    name="Consulta_Triagem",
    ends={
        Property(name="triagem26", type=Triagem, multiplicity=Multiplicity(0, 1)),
        Property(name="consulta7", type=Consulta, multiplicity=Multiplicity(0, 1))
    }
)
Atestado_Consulta: BinaryAssociation = BinaryAssociation(
    name="Atestado_Consulta",
    ends={
        Property(name="consulta28", type=Consulta, multiplicity=Multiplicity(0, 1)),
        Property(name="atestado29", type=Atestado, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_sXYLwF_GEeiba6mIiOhFVA",
    types={Pessoa, Paciente, Medico, Enfermeira, Triagem, String_Interface, Consulta, Atestado},
    associations={Triagem_Paciente, Triagem_Enfermeira, Consulta_Medico, Consulta_Triagem, Atestado_Consulta},
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