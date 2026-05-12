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
Cirurgiao = Class(name="Cirurgiao")
Cliente = Class(name="Cliente")
Consulta = Class(name="Consulta")
Cliente_Actor = Class(name="Cliente_Actor")
Cirurgi_o_Actor = Class(name="Cirurgi_o_Actor")
Cl_nica_Component = Class(name="Cl_nica_Component")
Cancelar_Consulta_external = Class(name="Cancelar_Consulta_external")
Ver_consultas_external = Class(name="Ver_consultas_external")
Marcar_consulta_external = Class(name="Marcar_consulta_external")
Confirmar_Consulta_external = Class(name="Confirmar_Consulta_external")

# Cirurgiao class attributes and methods
Cirurgiao_CirurgiaoId: Property = Property(name="CirurgiaoId", type=IntegerType)
Cirurgiao_Nome: Property = Property(name="Nome", type=StringType)
Cirurgiao_Especialidade: Property = Property(name="Especialidade", type=StringType)
Cirurgiao.attributes={Cirurgiao_Especialidade, Cirurgiao_CirurgiaoId, Cirurgiao_Nome}

# Cliente class attributes and methods
Cliente_ClienteId: Property = Property(name="ClienteId", type=IntegerType)
Cliente_Nome: Property = Property(name="Nome", type=StringType)
Cliente_Cpf: Property = Property(name="Cpf", type=StringType)
Cliente_Email: Property = Property(name="Email", type=StringType)
Cliente_Telefone: Property = Property(name="Telefone", type=StringType)
Cliente.attributes={Cliente_Cpf, Cliente_Nome, Cliente_ClienteId, Cliente_Telefone, Cliente_Email}

# Consulta class attributes and methods
Consulta_ConsultaId: Property = Property(name="ConsultaId", type=IntegerType)
Consulta_DataHora: Property = Property(name="DataHora", type=StringType)
Consulta_Cliente: Property = Property(name="Cliente", type=Cliente)
Consulta_Cirurgiao: Property = Property(name="Cirurgiao", type=Cirurgiao)
Consulta_Observacoes: Property = Property(name="Observacoes", type=StringType)
Consulta_Situacao: Property = Property(name="Situacao", type=StringType)
Consulta.attributes={Consulta_Cirurgiao, Consulta_Cliente, Consulta_ConsultaId, Consulta_Observacoes, Consulta_DataHora, Consulta_Situacao}

# Cliente_Actor class attributes and methods

# Cirurgi_o_Actor class attributes and methods

# Cl_nica_Component class attributes and methods

# Cancelar_Consulta_external class attributes and methods

# Ver_consultas_external class attributes and methods

# Marcar_consulta_external class attributes and methods

# Confirmar_Consulta_external class attributes and methods

# Relationships
Consulta_Cliente: BinaryAssociation = BinaryAssociation(
    name="Consulta_Cliente",
    ends={
        Property(name="cliente0", type=Cliente, multiplicity=Multiplicity(1, 1)),
        Property(name="consulta1", type=Consulta, multiplicity=Multiplicity(0, 9999))
    }
)
Cirurgiao_Consulta: BinaryAssociation = BinaryAssociation(
    name="Cirurgiao_Consulta",
    ends={
        Property(name="consulta2", type=Consulta, multiplicity=Multiplicity(0, 9999)),
        Property(name="cirurgiao3", type=Cirurgiao, multiplicity=Multiplicity(1, 1))
    }
)
Cancelar_Consulta_Cirurgi_o: BinaryAssociation = BinaryAssociation(
    name="Cancelar_Consulta_Cirurgi_o",
    ends={
        Property(name="cirurgi_o4", type=Cirurgi_o_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="cancelar_Consulta5", type=Cancelar_Consulta_external, multiplicity=Multiplicity(0, 1))
    }
)
Cancelar_Consulta_Cliente: BinaryAssociation = BinaryAssociation(
    name="Cancelar_Consulta_Cliente",
    ends={
        Property(name="cliente6", type=Cliente_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="cancelar_Consulta7", type=Cancelar_Consulta_external, multiplicity=Multiplicity(0, 1))
    }
)
Cliente_Ver_consultas: BinaryAssociation = BinaryAssociation(
    name="Cliente_Ver_consultas",
    ends={
        Property(name="ver_consultas8", type=Ver_consultas_external, multiplicity=Multiplicity(0, 1)),
        Property(name="cliente9", type=Cliente_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Cirurgi_o_Ver_consultas: BinaryAssociation = BinaryAssociation(
    name="Cirurgi_o_Ver_consultas",
    ends={
        Property(name="ver_consultas10", type=Ver_consultas_external, multiplicity=Multiplicity(0, 1)),
        Property(name="cirurgi_o11", type=Cirurgi_o_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Cliente_Marcar_consulta: BinaryAssociation = BinaryAssociation(
    name="Cliente_Marcar_consulta",
    ends={
        Property(name="marcar_consulta12", type=Marcar_consulta_external, multiplicity=Multiplicity(0, 1)),
        Property(name="cliente13", type=Cliente_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Cirurgi_o_Confirmar_Consulta: BinaryAssociation = BinaryAssociation(
    name="Cirurgi_o_Confirmar_Consulta",
    ends={
        Property(name="confirmar_Consulta14", type=Confirmar_Consulta_external, multiplicity=Multiplicity(0, 1)),
        Property(name="cirurgi_o15", type=Cirurgi_o_Actor, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_aG68INYeEeehRMl7r1_c5g",
    types={Cirurgiao, Cliente, Consulta, Cliente_Actor, Cirurgi_o_Actor, Cl_nica_Component, Cancelar_Consulta_external, Ver_consultas_external, Marcar_consulta_external, Confirmar_Consulta_external},
    associations={Consulta_Cliente, Cirurgiao_Consulta, Cancelar_Consulta_Cirurgi_o, Cancelar_Consulta_Cliente, Cliente_Ver_consultas, Cirurgi_o_Ver_consultas, Cliente_Marcar_consulta, Cirurgi_o_Confirmar_Consulta},
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