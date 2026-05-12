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
Medico = Class(name="Medico")
Paciente = Class(name="Paciente")
Especialidade = Class(name="Especialidade")
Consulta = Class(name="Consulta")

# Medico class attributes and methods
Medico_nome: Property = Property(name="nome", type=StringType)
Medico_endereco: Property = Property(name="endereco", type=StringType)
Medico_crm: Property = Property(name="crm", type=StringType)
Medico_foto: Property = Property(name="foto", type=StringType)
Medico.attributes={Medico_crm, Medico_nome, Medico_foto, Medico_endereco}

# Paciente class attributes and methods
Paciente_nome: Property = Property(name="nome", type=StringType)
Paciente_celular: Property = Property(name="celular", type=StringType)
Paciente_endere_o: Property = Property(name="endere_o", type=StringType)
Paciente.attributes={Paciente_celular, Paciente_endere_o, Paciente_nome}

# Especialidade class attributes and methods
Especialidade_descricao: Property = Property(name="descricao", type=StringType)
Especialidade.attributes={Especialidade_descricao}

# Consulta class attributes and methods
Consulta_data: Property = Property(name="data", type=StringType)
Consulta_pre_o: Property = Property(name="pre_o", type=StringType)
Consulta.attributes={Consulta_data, Consulta_pre_o}

# Relationships
Medico_Especialidade: BinaryAssociation = BinaryAssociation(
    name="Medico_Especialidade",
    ends={
        Property(name="especialidade0", type=Especialidade, multiplicity=Multiplicity(0, 1)),
        Property(name="medico1", type=Medico, multiplicity=Multiplicity(0, 1))
    }
)
Consulta_Medico: BinaryAssociation = BinaryAssociation(
    name="Consulta_Medico",
    ends={
        Property(name="medico2", type=Medico, multiplicity=Multiplicity(0, 1)),
        Property(name="consulta3", type=Consulta, multiplicity=Multiplicity(0, 1))
    }
)
Paciente_Consulta: BinaryAssociation = BinaryAssociation(
    name="Paciente_Consulta",
    ends={
        Property(name="consulta4", type=Consulta, multiplicity=Multiplicity(0, 1)),
        Property(name="paciente5", type=Paciente, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_f6_4UOhFEeiV94kHgjpOMg",
    types={Medico, Paciente, Especialidade, Consulta},
    associations={Medico_Especialidade, Consulta_Medico, Paciente_Consulta},
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