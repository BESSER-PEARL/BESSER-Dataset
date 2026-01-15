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
myDsl_Model = Class(name="myDsl::Model")
myDsl_Greeting = Class(name="myDsl::Greeting")
myDsl_Api = Class(name="myDsl::Api")
myDsl_ApiNome = Class(name="myDsl::ApiNome")
myDsl_Entidades = Class(name="myDsl::Entidades")
myDsl_Entidade = Class(name="myDsl::Entidade")
myDsl_Nome = Class(name="myDsl::Nome")
myDsl_Atributos = Class(name="myDsl::Atributos")
myDsl_Nome_Atributo = Class(name="myDsl::Nome::Atributo")
myDsl_AtributoTipo = Class(name="myDsl::AtributoTipo")
myDsl_Associacao = Class(name="myDsl::Associacao")
myDsl_Operacao = Class(name="myDsl::Operacao")
myDsl_OperacaoCascada = Class(name="myDsl::OperacaoCascada")
myDsl_Atributo = Class(name="myDsl::Atributo")

# myDsl_Model class attributes and methods

# myDsl_Greeting class attributes and methods

# myDsl_Api class attributes and methods

# myDsl_ApiNome class attributes and methods
myDsl_ApiNome_nome: Property = Property(name="nome", type=StringType)
myDsl_ApiNome.attributes={myDsl_ApiNome_nome}

# myDsl_Entidades class attributes and methods

# myDsl_Entidade class attributes and methods

# myDsl_Nome class attributes and methods
myDsl_Nome_nome: Property = Property(name="nome", type=StringType)
myDsl_Nome.attributes={myDsl_Nome_nome}

# myDsl_Atributos class attributes and methods

# myDsl_Nome_Atributo class attributes and methods
myDsl_Nome_Atributo_nome: Property = Property(name="nome", type=StringType)
myDsl_Nome_Atributo.attributes={myDsl_Nome_Atributo_nome}

# myDsl_AtributoTipo class attributes and methods
myDsl_AtributoTipo_tipoPrimitivo: Property = Property(name="tipoPrimitivo", type=StringType)
myDsl_AtributoTipo_tipoColecao: Property = Property(name="tipoColecao", type=StringType)
myDsl_AtributoTipo_tipoObjeto: Property = Property(name="tipoObjeto", type=StringType)
myDsl_AtributoTipo.attributes={myDsl_AtributoTipo_tipoColecao, myDsl_AtributoTipo_tipoPrimitivo, myDsl_AtributoTipo_tipoObjeto}

# myDsl_Associacao class attributes and methods
myDsl_Associacao_associacao: Property = Property(name="associacao", type=StringType)
myDsl_Associacao.attributes={myDsl_Associacao_associacao}

# myDsl_Operacao class attributes and methods

# myDsl_OperacaoCascada class attributes and methods
myDsl_OperacaoCascada_operacao: Property = Property(name="operacao", type=StringType)
myDsl_OperacaoCascada.attributes={myDsl_OperacaoCascada_operacao}

# myDsl_Atributo class attributes and methods

# Relationships
greetings0: BinaryAssociation = BinaryAssociation(
    name="greetings0",
    ends={
        Property(name="myDsl_Greeting", type=myDsl_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Model", type=myDsl_Greeting, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
api1: BinaryAssociation = BinaryAssociation(
    name="api1",
    ends={
        Property(name="myDsl_Api", type=myDsl_Greeting, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Greeting2", type=myDsl_Api, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nomeApi3: BinaryAssociation = BinaryAssociation(
    name="nomeApi3",
    ends={
        Property(name="myDsl_ApiNome", type=myDsl_Api, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Api4", type=myDsl_ApiNome, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entidades5: BinaryAssociation = BinaryAssociation(
    name="entidades5",
    ends={
        Property(name="myDsl_Entidades", type=myDsl_Api, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Api6", type=myDsl_Entidades, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entidade7: BinaryAssociation = BinaryAssociation(
    name="entidade7",
    ends={
        Property(name="myDsl_Entidade", type=myDsl_Entidades, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Entidades8", type=myDsl_Entidade, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entidadeMais9: BinaryAssociation = BinaryAssociation(
    name="entidadeMais9",
    ends={
        Property(name="myDsl_Entidade11", type=myDsl_Entidades, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Entidades10", type=myDsl_Entidade, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nomeEntidade12: BinaryAssociation = BinaryAssociation(
    name="nomeEntidade12",
    ends={
        Property(name="myDsl_Nome", type=myDsl_Entidade, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Entidade13", type=myDsl_Nome, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
atributos14: BinaryAssociation = BinaryAssociation(
    name="atributos14",
    ends={
        Property(name="myDsl_Atributos", type=myDsl_Entidade, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Entidade15", type=myDsl_Atributos, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
atributoMais18: BinaryAssociation = BinaryAssociation(
    name="atributoMais18",
    ends={
        Property(name="myDsl_Atributo20", type=myDsl_Atributos, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Atributos19", type=myDsl_Atributo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nomeAtributo21: BinaryAssociation = BinaryAssociation(
    name="nomeAtributo21",
    ends={
        Property(name="myDsl_Nome_Atributo", type=myDsl_Atributo, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Atributo22", type=myDsl_Nome_Atributo, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
atributoTipo23: BinaryAssociation = BinaryAssociation(
    name="atributoTipo23",
    ends={
        Property(name="myDsl_AtributoTipo", type=myDsl_Atributo, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Atributo24", type=myDsl_AtributoTipo, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
associacao25: BinaryAssociation = BinaryAssociation(
    name="associacao25",
    ends={
        Property(name="myDsl_Associacao", type=myDsl_Atributo, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Atributo26", type=myDsl_Associacao, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operacao27: BinaryAssociation = BinaryAssociation(
    name="operacao27",
    ends={
        Property(name="myDsl_Operacao", type=myDsl_Atributo, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Atributo28", type=myDsl_Operacao, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
opCascada29: BinaryAssociation = BinaryAssociation(
    name="opCascada29",
    ends={
        Property(name="myDsl_OperacaoCascada", type=myDsl_Operacao, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Operacao30", type=myDsl_OperacaoCascada, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
opCascadaMais31: BinaryAssociation = BinaryAssociation(
    name="opCascadaMais31",
    ends={
        Property(name="myDsl_OperacaoCascada33", type=myDsl_Operacao, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Operacao32", type=myDsl_OperacaoCascada, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
atributo16: BinaryAssociation = BinaryAssociation(
    name="atributo16",
    ends={
        Property(name="myDsl_Atributo", type=myDsl_Atributos, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Atributos17", type=myDsl_Atributo, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="myDsl",
    types={myDsl_Model, myDsl_Greeting, myDsl_Api, myDsl_ApiNome, myDsl_Entidades, myDsl_Entidade, myDsl_Nome, myDsl_Atributos, myDsl_Nome_Atributo, myDsl_AtributoTipo, myDsl_Associacao, myDsl_Operacao, myDsl_OperacaoCascada, myDsl_Atributo},
    associations={greetings0, api1, nomeApi3, entidades5, entidade7, entidadeMais9, nomeEntidade12, atributos14, atributoMais18, nomeAtributo21, atributoTipo23, associacao25, operacao27, opCascada29, opCascadaMais31, atributo16},
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