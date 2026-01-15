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
Origem: Enumeration = Enumeration(
    name="Origem",
    literals={
            EnumerationLiteral(name="Sentida"),
			EnumerationLiteral(name="Usuario"),
			EnumerationLiteral(name="Perfil"),
			EnumerationLiteral(name="Derivada")
    }
)

Validade: Enumeration = Enumeration(
    name="Validade",
    literals={
            EnumerationLiteral(name="Volatil"),
			EnumerationLiteral(name="Frequente"),
			EnumerationLiteral(name="Raramente"),
			EnumerationLiteral(name="Permanente")
    }
)

Qualidade: Enumeration = Enumeration(
    name="Qualidade",
    literals={
            EnumerationLiteral(name="Baixo"),
			EnumerationLiteral(name="Alto")
    }
)

TipoValor: Enumeration = Enumeration(
    name="TipoValor",
    literals={
            EnumerationLiteral(name="TInteger"),
			EnumerationLiteral(name="TString"),
			EnumerationLiteral(name="TFloat"),
			EnumerationLiteral(name="TBoolean")
    }
)

OperadorLogico: Enumeration = Enumeration(
    name="OperadorLogico",
    literals={
            EnumerationLiteral(name="AND"),
			EnumerationLiteral(name="OR")
    }
)

Presenca: Enumeration = Enumeration(
    name="Presenca",
    literals={
            EnumerationLiteral(name="PRESENTE"),
			EnumerationLiteral(name="AUSENTE")
    }
)

OperadorAcaoLogico: Enumeration = Enumeration(
    name="OperadorAcaoLogico",
    literals={
            EnumerationLiteral(name="AND")
    }
)

CardinalidadeMaxima: Enumeration = Enumeration(
    name="CardinalidadeMaxima",
    literals={
            EnumerationLiteral(name="OR"),
			EnumerationLiteral(name="XOR")
    }
)

OperadorRelacional: Enumeration = Enumeration(
    name="OperadorRelacional",
    literals={
            EnumerationLiteral(name="MENORIGUAL"),
			EnumerationLiteral(name="DIFERENTE"),
			EnumerationLiteral(name="MAIOR"),
			EnumerationLiteral(name="MENOR"),
			EnumerationLiteral(name="IGUAL"),
			EnumerationLiteral(name="MAIORIGUAL")
    }
)

# Classes
caracteristica_LPS = Class(name="caracteristica::LPS")
caracteristica_Elemento = Class(name="caracteristica::Elemento")
caracteristica_ElementoCaracteristico = Class(name="caracteristica::ElementoCaracteristico")
Elemento = Class(name="Elemento")
caracteristica_Variacao = Class(name="caracteristica::Variacao")
caracteristica_CaracteristicaRaiz = Class(name="caracteristica::CaracteristicaRaiz")
Caracteristica = Class(name="Caracteristica")
caracteristica_CaracteristicaOpcional = Class(name="caracteristica::CaracteristicaOpcional")
ElementoCaracteristico = Class(name="ElementoCaracteristico")
caracteristica_CaracteristicaAgrupada = Class(name="caracteristica::CaracteristicaAgrupada")
caracteristica_Atributo = Class(name="caracteristica::Atributo")
caracteristica_Caracteristica = Class(name="caracteristica::Caracteristica")
caracteristica_PontoDeVariacao = Class(name="caracteristica::PontoDeVariacao")
PontoDeVariacao = Class(name="PontoDeVariacao")
caracteristica_Variante = Class(name="caracteristica::Variante")
caracteristica_CaracteristicaMandatoria = Class(name="caracteristica::CaracteristicaMandatoria")
caracteristica_VariacaoDois = Class(name="caracteristica::VariacaoDois")

# caracteristica_LPS class attributes and methods
caracteristica_LPS_nome: Property = Property(name="nome", type=StringType)
caracteristica_LPS.attributes={caracteristica_LPS_nome}

# caracteristica_Elemento class attributes and methods
caracteristica_Elemento_nome: Property = Property(name="nome", type=StringType)
caracteristica_Elemento.attributes={caracteristica_Elemento_nome}

# caracteristica_ElementoCaracteristico class attributes and methods

# Elemento class attributes and methods

# caracteristica_Variacao class attributes and methods
caracteristica_Variacao_cardinalidadeMinima: Property = Property(name="cardinalidadeMinima", type=StringType)
caracteristica_Variacao_cardinalidadeMaxima: Property = Property(name="cardinalidadeMaxima", type=StringType)
caracteristica_Variacao.attributes={caracteristica_Variacao_cardinalidadeMaxima, caracteristica_Variacao_cardinalidadeMinima}

# caracteristica_CaracteristicaRaiz class attributes and methods

# Caracteristica class attributes and methods

# caracteristica_CaracteristicaOpcional class attributes and methods

# ElementoCaracteristico class attributes and methods

# caracteristica_CaracteristicaAgrupada class attributes and methods

# caracteristica_Atributo class attributes and methods
caracteristica_Atributo_tipoValor: Property = Property(name="tipoValor", type=StringType)
caracteristica_Atributo.attributes={caracteristica_Atributo_tipoValor}

# caracteristica_Caracteristica class attributes and methods

# caracteristica_PontoDeVariacao class attributes and methods

# PontoDeVariacao class attributes and methods

# caracteristica_Variante class attributes and methods

# caracteristica_CaracteristicaMandatoria class attributes and methods

# caracteristica_VariacaoDois class attributes and methods
caracteristica_VariacaoDois_cardinalidadeMaxima: Property = Property(name="cardinalidadeMaxima", type=StringType)
caracteristica_VariacaoDois_cardinalidadeMinimaOr: Property = Property(name="cardinalidadeMinimaOr", type=StringType)
caracteristica_VariacaoDois_cardinalidadeMaximaOr: Property = Property(name="cardinalidadeMaximaOr", type=StringType)
caracteristica_VariacaoDois.attributes={caracteristica_VariacaoDois_cardinalidadeMaxima, caracteristica_VariacaoDois_cardinalidadeMinimaOr, caracteristica_VariacaoDois_cardinalidadeMaximaOr}

# Relationships
elementos0: BinaryAssociation = BinaryAssociation(
    name="elementos0",
    ends={
        Property(name="caracteristica_Elemento", type=caracteristica_LPS, multiplicity=Multiplicity(1, 1)),
        Property(name="caracteristica_LPS", type=caracteristica_Elemento, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
caracteristicaPai3: BinaryAssociation = BinaryAssociation(
    name="caracteristicaPai3",
    ends={
        Property(name="Caracteristica4", type=caracteristica_Caracteristica, multiplicity=Multiplicity(1, 1)),
        Property(name="caracteristicaFilha", type=caracteristica_Caracteristica, multiplicity=Multiplicity(0, 1))
    }
)
caracteristicaFilha6: BinaryAssociation = BinaryAssociation(
    name="caracteristicaFilha6",
    ends={
        Property(name="Caracteristica7", type=caracteristica_Caracteristica, multiplicity=Multiplicity(1, 1)),
        Property(name="caracteristicaPai", type=caracteristica_Caracteristica, multiplicity=Multiplicity(0, 9999))
    }
)
variacoes8: BinaryAssociation = BinaryAssociation(
    name="variacoes8",
    ends={
        Property(name="Variacao", type=caracteristica_Caracteristica, multiplicity=Multiplicity(1, 1)),
        Property(name="caracteristicaPai9", type=caracteristica_Variacao, multiplicity=Multiplicity(0, 9999))
    }
)
atributo10: BinaryAssociation = BinaryAssociation(
    name="atributo10",
    ends={
        Property(name="Atributo", type=caracteristica_Caracteristica, multiplicity=Multiplicity(1, 1)),
        Property(name="caracteristicaPai11", type=caracteristica_Atributo, multiplicity=Multiplicity(0, 9999))
    }
)
LpsDoSistema12: BinaryAssociation = BinaryAssociation(
    name="LpsDoSistema12",
    ends={
        Property(name="caracteristica_LPS13", type=caracteristica_CaracteristicaRaiz, multiplicity=Multiplicity(1, 1)),
        Property(name="caracteristica_CaracteristicaRaiz", type=caracteristica_LPS, multiplicity=Multiplicity(1, 1))
    }
)
caracteristicaPai1: BinaryAssociation = BinaryAssociation(
    name="caracteristicaPai1",
    ends={
        Property(name="Caracteristica", type=caracteristica_Atributo, multiplicity=Multiplicity(1, 1)),
        Property(name="atributo", type=caracteristica_Caracteristica, multiplicity=Multiplicity(0, 1))
    }
)
variantes14: BinaryAssociation = BinaryAssociation(
    name="variantes14",
    ends={
        Property(name="Variante", type=caracteristica_Variacao, multiplicity=Multiplicity(1, 1)),
        Property(name="variacaoPai", type=caracteristica_Variante, multiplicity=Multiplicity(0, 9999))
    }
)
caracteristicaPai15: BinaryAssociation = BinaryAssociation(
    name="caracteristicaPai15",
    ends={
        Property(name="Caracteristica16", type=caracteristica_Variacao, multiplicity=Multiplicity(1, 1)),
        Property(name="variacoes", type=caracteristica_Caracteristica, multiplicity=Multiplicity(0, 1))
    }
)
variacaoPai17: BinaryAssociation = BinaryAssociation(
    name="variacaoPai17",
    ends={
        Property(name="Variacao18", type=caracteristica_Variante, multiplicity=Multiplicity(1, 1)),
        Property(name="variantes", type=caracteristica_Variacao, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_caracteristica_Caracteristica_Elemento = Generalization(general=Elemento, specific=caracteristica_Caracteristica)
gen_caracteristica_CaracteristicaRaiz_Caracteristica = Generalization(general=Caracteristica, specific=caracteristica_CaracteristicaRaiz)
gen_caracteristica_CaracteristicaOpcional_Caracteristica = Generalization(general=Caracteristica, specific=caracteristica_CaracteristicaOpcional)
gen_caracteristica_CaracteristicaOpcional_ElementoCaracteristico = Generalization(general=ElementoCaracteristico, specific=caracteristica_CaracteristicaOpcional)
gen_caracteristica_CaracteristicaAgrupada_Caracteristica = Generalization(general=Caracteristica, specific=caracteristica_CaracteristicaAgrupada)
gen_caracteristica_CaracteristicaAgrupada_ElementoCaracteristico = Generalization(general=ElementoCaracteristico, specific=caracteristica_CaracteristicaAgrupada)
gen_caracteristica_ElementoCaracteristico_Elemento = Generalization(general=Elemento, specific=caracteristica_ElementoCaracteristico)
gen_caracteristica_Atributo_Elemento = Generalization(general=Elemento, specific=caracteristica_Atributo)
gen_caracteristica_Variacao_PontoDeVariacao = Generalization(general=PontoDeVariacao, specific=caracteristica_Variacao)
gen_caracteristica_Variacao_Elemento = Generalization(general=Elemento, specific=caracteristica_Variacao)
gen_caracteristica_Variante_PontoDeVariacao = Generalization(general=PontoDeVariacao, specific=caracteristica_Variante)
gen_caracteristica_Variante_ElementoCaracteristico = Generalization(general=ElementoCaracteristico, specific=caracteristica_Variante)
gen_caracteristica_Variante_Caracteristica = Generalization(general=Caracteristica, specific=caracteristica_Variante)
gen_caracteristica_CaracteristicaMandatoria_Caracteristica = Generalization(general=Caracteristica, specific=caracteristica_CaracteristicaMandatoria)
gen_caracteristica_VariacaoDois_Caracteristica = Generalization(general=Caracteristica, specific=caracteristica_VariacaoDois)
gen_caracteristica_VariacaoDois_ElementoCaracteristico = Generalization(general=ElementoCaracteristico, specific=caracteristica_VariacaoDois)

# Domain Model
domain_model = DomainModel(
    name="caracteristica",
    types={caracteristica_LPS, caracteristica_Elemento, caracteristica_ElementoCaracteristico, Elemento, caracteristica_Variacao, caracteristica_CaracteristicaRaiz, Caracteristica, caracteristica_CaracteristicaOpcional, ElementoCaracteristico, caracteristica_CaracteristicaAgrupada, caracteristica_Atributo, caracteristica_Caracteristica, caracteristica_PontoDeVariacao, PontoDeVariacao, caracteristica_Variante, caracteristica_CaracteristicaMandatoria, caracteristica_VariacaoDois, Origem, Validade, Qualidade, TipoValor, OperadorLogico, Presenca, OperadorAcaoLogico, CardinalidadeMaxima, OperadorRelacional},
    associations={elementos0, caracteristicaPai3, caracteristicaFilha6, variacoes8, atributo10, LpsDoSistema12, caracteristicaPai1, variantes14, caracteristicaPai15, variacaoPai17},
    generalizations={gen_caracteristica_Caracteristica_Elemento, gen_caracteristica_CaracteristicaRaiz_Caracteristica, gen_caracteristica_CaracteristicaOpcional_Caracteristica, gen_caracteristica_CaracteristicaOpcional_ElementoCaracteristico, gen_caracteristica_CaracteristicaAgrupada_Caracteristica, gen_caracteristica_CaracteristicaAgrupada_ElementoCaracteristico, gen_caracteristica_ElementoCaracteristico_Elemento, gen_caracteristica_Atributo_Elemento, gen_caracteristica_Variacao_PontoDeVariacao, gen_caracteristica_Variacao_Elemento, gen_caracteristica_Variante_PontoDeVariacao, gen_caracteristica_Variante_ElementoCaracteristico, gen_caracteristica_Variante_Caracteristica, gen_caracteristica_CaracteristicaMandatoria_Caracteristica, gen_caracteristica_VariacaoDois_Caracteristica, gen_caracteristica_VariacaoDois_ElementoCaracteristico},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)