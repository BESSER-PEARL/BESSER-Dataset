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

OperadorRelacional: Enumeration = Enumeration(
    name="OperadorRelacional",
    literals={
            EnumerationLiteral(name="MAIOR"),
			EnumerationLiteral(name="MENOR"),
			EnumerationLiteral(name="IGUAL"),
			EnumerationLiteral(name="MAIORIGUAL"),
			EnumerationLiteral(name="MENORIGUAL"),
			EnumerationLiteral(name="DIFERENTE")
    }
)

Presenca: Enumeration = Enumeration(
    name="Presenca",
    literals={
            EnumerationLiteral(name="PRESENTE"),
			EnumerationLiteral(name="AUSENTE")
    }
)

OperadorLogico: Enumeration = Enumeration(
    name="OperadorLogico",
    literals={
            EnumerationLiteral(name="AND"),
			EnumerationLiteral(name="OR")
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

# Classes
caracteristica_Produto = Class(name="caracteristica::Produto")
caracteristica_Expressao = Class(name="caracteristica::Expressao")
caracteristica_ElementoDeProduto = Class(name="caracteristica::ElementoDeProduto")
caracteristica_CaracteristicaRaiz = Class(name="caracteristica::CaracteristicaRaiz")
caracteristica_Atributo = Class(name="caracteristica::Atributo")
caracteristica_Simulacao = Class(name="caracteristica::Simulacao")
caracteristica_InconsistenciaRegraAdaptacao = Class(name="caracteristica::InconsistenciaRegraAdaptacao")
caracteristica_CasoDeUso = Class(name="caracteristica::CasoDeUso")
ElementoExterno = Class(name="ElementoExterno")
caracteristica_CasoDeTeste = Class(name="caracteristica::CasoDeTeste")
caracteristica_ElementoCaracteristico = Class(name="caracteristica::ElementoCaracteristico")
Elemento = Class(name="Elemento")
caracteristica_LPS = Class(name="caracteristica::LPS")
caracteristica_PontoDeVariacao = Class(name="caracteristica::PontoDeVariacao")
caracteristica_Elemento = Class(name="caracteristica::Elemento")
caracteristica_ElementoExterno = Class(name="caracteristica::ElementoExterno")
caracteristica_Regra = Class(name="caracteristica::Regra")
caracteristica_Variacao = Class(name="caracteristica::Variacao")
Caracteristica = Class(name="Caracteristica")
caracteristica_CaracteristicaOpcional = Class(name="caracteristica::CaracteristicaOpcional")
ElementoCaracteristico = Class(name="ElementoCaracteristico")
caracteristica_CaracteristicaAgrupada = Class(name="caracteristica::CaracteristicaAgrupada")
caracteristica_Caracteristica = Class(name="caracteristica::Caracteristica")
caracteristica_RaizDeContexto = Class(name="caracteristica::RaizDeContexto")
caracteristica_EntidadeDeContexto = Class(name="caracteristica::EntidadeDeContexto")
caracteristica_InformacaoDeContexto = Class(name="caracteristica::InformacaoDeContexto")
caracteristica_CaracteristicaMandatoria = Class(name="caracteristica::CaracteristicaMandatoria")
caracteristica_VariacaoDois = Class(name="caracteristica::VariacaoDois")
PontoDeVariacao = Class(name="PontoDeVariacao")
caracteristica_Variante = Class(name="caracteristica::Variante")
caracteristica_AtributoProduto = Class(name="caracteristica::AtributoProduto")
caracteristica_CaracteristicaMandatoriaProduto = Class(name="caracteristica::CaracteristicaMandatoriaProduto")
CaracteristicaProduto = Class(name="CaracteristicaProduto")
caracteristica_CaracteristicaOpcionalProduto = Class(name="caracteristica::CaracteristicaOpcionalProduto")
caracteristica_VariacaoDoisProduto = Class(name="caracteristica::VariacaoDoisProduto")
caracteristica_CaracteristicaAgrupadaProduto = Class(name="caracteristica::CaracteristicaAgrupadaProduto")
caracteristica_VariacaoProduto = Class(name="caracteristica::VariacaoProduto")
caracteristica_CaracteristicaProduto = Class(name="caracteristica::CaracteristicaProduto")
ElementoDeProduto = Class(name="ElementoDeProduto")
caracteristica_VarianteProduto = Class(name="caracteristica::VarianteProduto")
caracteristica_RegraDeContexto = Class(name="caracteristica::RegraDeContexto")
caracteristica_Evento = Class(name="caracteristica::Evento")
caracteristica_Acao = Class(name="caracteristica::Acao")
Expressao = Class(name="Expressao")
caracteristica_EventoLogico = Class(name="caracteristica::EventoLogico")
Evento = Class(name="Evento")
caracteristica_EventoRelacional = Class(name="caracteristica::EventoRelacional")
caracteristica_RegraDeComposicao = Class(name="caracteristica::RegraDeComposicao")
Regra = Class(name="Regra")
caracteristica_Antecedente = Class(name="caracteristica::Antecedente")
caracteristica_LiteralAcao = Class(name="caracteristica::LiteralAcao")
caracteristica_Designar = Class(name="caracteristica::Designar")
caracteristica_ExpressaoLogica = Class(name="caracteristica::ExpressaoLogica")
Antecedente = Class(name="Antecedente")
caracteristica_ExpressaoRelacional = Class(name="caracteristica::ExpressaoRelacional")
caracteristica_AcaoLogico = Class(name="caracteristica::AcaoLogico")
Acao = Class(name="Acao")
caracteristica_Transicao = Class(name="caracteristica::Transicao")
caracteristica_Estado = Class(name="caracteristica::Estado")
caracteristica_LiteralComposicao = Class(name="caracteristica::LiteralComposicao")

# caracteristica_Produto class attributes and methods

# caracteristica_Expressao class attributes and methods
caracteristica_Expressao_nome: Property = Property(name="nome", type=StringType)
caracteristica_Expressao.attributes={caracteristica_Expressao_nome}

# caracteristica_ElementoDeProduto class attributes and methods
caracteristica_ElementoDeProduto_nome: Property = Property(name="nome", type=StringType)
caracteristica_ElementoDeProduto.attributes={caracteristica_ElementoDeProduto_nome}

# caracteristica_CaracteristicaRaiz class attributes and methods

# caracteristica_Atributo class attributes and methods
caracteristica_Atributo_tipoValor: Property = Property(name="tipoValor", type=StringType)
caracteristica_Atributo.attributes={caracteristica_Atributo_tipoValor}

# caracteristica_Simulacao class attributes and methods
caracteristica_Simulacao_nome: Property = Property(name="nome", type=StringType)
caracteristica_Simulacao.attributes={caracteristica_Simulacao_nome}

# caracteristica_InconsistenciaRegraAdaptacao class attributes and methods

# caracteristica_CasoDeUso class attributes and methods

# ElementoExterno class attributes and methods

# caracteristica_CasoDeTeste class attributes and methods

# caracteristica_ElementoCaracteristico class attributes and methods

# Elemento class attributes and methods

# caracteristica_LPS class attributes and methods
caracteristica_LPS_valoresContextuais: Property = Property(name="valoresContextuais", type=StringType)
caracteristica_LPS_erro: Property = Property(name="erro", type=StringType)
caracteristica_LPS_nome: Property = Property(name="nome", type=StringType)
caracteristica_LPS.attributes={caracteristica_LPS_nome, caracteristica_LPS_erro, caracteristica_LPS_valoresContextuais}

# caracteristica_PontoDeVariacao class attributes and methods

# caracteristica_Elemento class attributes and methods
caracteristica_Elemento_nome: Property = Property(name="nome", type=StringType)
caracteristica_Elemento.attributes={caracteristica_Elemento_nome}

# caracteristica_ElementoExterno class attributes and methods
caracteristica_ElementoExterno_nome: Property = Property(name="nome", type=StringType)
caracteristica_ElementoExterno.attributes={caracteristica_ElementoExterno_nome}

# caracteristica_Regra class attributes and methods
caracteristica_Regra_nome: Property = Property(name="nome", type=StringType)
caracteristica_Regra_conteudo: Property = Property(name="conteudo", type=StringType)
caracteristica_Regra.attributes={caracteristica_Regra_conteudo, caracteristica_Regra_nome}

# caracteristica_Variacao class attributes and methods
caracteristica_Variacao_cardinalidadeMinima: Property = Property(name="cardinalidadeMinima", type=StringType)
caracteristica_Variacao_cardinalidadeMaxima: Property = Property(name="cardinalidadeMaxima", type=StringType)
caracteristica_Variacao.attributes={caracteristica_Variacao_cardinalidadeMaxima, caracteristica_Variacao_cardinalidadeMinima}

# Caracteristica class attributes and methods

# caracteristica_CaracteristicaOpcional class attributes and methods

# ElementoCaracteristico class attributes and methods

# caracteristica_CaracteristicaAgrupada class attributes and methods

# caracteristica_Caracteristica class attributes and methods

# caracteristica_RaizDeContexto class attributes and methods

# caracteristica_EntidadeDeContexto class attributes and methods

# caracteristica_InformacaoDeContexto class attributes and methods
caracteristica_InformacaoDeContexto_origem: Property = Property(name="origem", type=StringType)
caracteristica_InformacaoDeContexto_validade: Property = Property(name="validade", type=StringType)
caracteristica_InformacaoDeContexto_qualidade: Property = Property(name="qualidade", type=StringType)
caracteristica_InformacaoDeContexto_tipoValor: Property = Property(name="tipoValor", type=StringType)
caracteristica_InformacaoDeContexto_valor: Property = Property(name="valor", type=StringType)
caracteristica_InformacaoDeContexto.attributes={caracteristica_InformacaoDeContexto_validade, caracteristica_InformacaoDeContexto_origem, caracteristica_InformacaoDeContexto_valor, caracteristica_InformacaoDeContexto_tipoValor, caracteristica_InformacaoDeContexto_qualidade}

# caracteristica_CaracteristicaMandatoria class attributes and methods

# caracteristica_VariacaoDois class attributes and methods
caracteristica_VariacaoDois_cardinalidadeMaxima: Property = Property(name="cardinalidadeMaxima", type=StringType)
caracteristica_VariacaoDois_cardinalidadeMinimaOr: Property = Property(name="cardinalidadeMinimaOr", type=StringType)
caracteristica_VariacaoDois_cardinalidadeMaximaOr: Property = Property(name="cardinalidadeMaximaOr", type=StringType)
caracteristica_VariacaoDois.attributes={caracteristica_VariacaoDois_cardinalidadeMinimaOr, caracteristica_VariacaoDois_cardinalidadeMaximaOr, caracteristica_VariacaoDois_cardinalidadeMaxima}

# PontoDeVariacao class attributes and methods

# caracteristica_Variante class attributes and methods

# caracteristica_AtributoProduto class attributes and methods
caracteristica_AtributoProduto_valor: Property = Property(name="valor", type=StringType)
caracteristica_AtributoProduto_tipoValor: Property = Property(name="tipoValor", type=StringType)
caracteristica_AtributoProduto.attributes={caracteristica_AtributoProduto_tipoValor, caracteristica_AtributoProduto_valor}

# caracteristica_CaracteristicaMandatoriaProduto class attributes and methods

# CaracteristicaProduto class attributes and methods

# caracteristica_CaracteristicaOpcionalProduto class attributes and methods

# caracteristica_VariacaoDoisProduto class attributes and methods
caracteristica_VariacaoDoisProduto_cardinalidadeMaxima: Property = Property(name="cardinalidadeMaxima", type=StringType)
caracteristica_VariacaoDoisProduto_cardinalidadeMinimaOr: Property = Property(name="cardinalidadeMinimaOr", type=StringType)
caracteristica_VariacaoDoisProduto_cardinalidadeMaximaOr: Property = Property(name="cardinalidadeMaximaOr", type=StringType)
caracteristica_VariacaoDoisProduto.attributes={caracteristica_VariacaoDoisProduto_cardinalidadeMinimaOr, caracteristica_VariacaoDoisProduto_cardinalidadeMaximaOr, caracteristica_VariacaoDoisProduto_cardinalidadeMaxima}

# caracteristica_CaracteristicaAgrupadaProduto class attributes and methods

# caracteristica_VariacaoProduto class attributes and methods
caracteristica_VariacaoProduto_cardinalidadeMinima: Property = Property(name="cardinalidadeMinima", type=StringType)
caracteristica_VariacaoProduto_cardinalidadeMaxima: Property = Property(name="cardinalidadeMaxima", type=StringType)
caracteristica_VariacaoProduto.attributes={caracteristica_VariacaoProduto_cardinalidadeMinima, caracteristica_VariacaoProduto_cardinalidadeMaxima}

# caracteristica_CaracteristicaProduto class attributes and methods

# ElementoDeProduto class attributes and methods

# caracteristica_VarianteProduto class attributes and methods
caracteristica_VarianteProduto_selecionado: Property = Property(name="selecionado", type=StringType)
caracteristica_VarianteProduto.attributes={caracteristica_VarianteProduto_selecionado}

# caracteristica_RegraDeContexto class attributes and methods

# caracteristica_Evento class attributes and methods

# caracteristica_Acao class attributes and methods

# Expressao class attributes and methods

# caracteristica_EventoLogico class attributes and methods
caracteristica_EventoLogico_operadorLogico: Property = Property(name="operadorLogico", type=StringType)
caracteristica_EventoLogico.attributes={caracteristica_EventoLogico_operadorLogico}

# Evento class attributes and methods

# caracteristica_EventoRelacional class attributes and methods
caracteristica_EventoRelacional_operadorRelacional: Property = Property(name="operadorRelacional", type=StringType)
caracteristica_EventoRelacional_valor: Property = Property(name="valor", type=StringType)
caracteristica_EventoRelacional.attributes={caracteristica_EventoRelacional_operadorRelacional, caracteristica_EventoRelacional_valor}

# caracteristica_RegraDeComposicao class attributes and methods

# Regra class attributes and methods

# caracteristica_Antecedente class attributes and methods

# caracteristica_LiteralAcao class attributes and methods
caracteristica_LiteralAcao_presenca: Property = Property(name="presenca", type=StringType)
caracteristica_LiteralAcao.attributes={caracteristica_LiteralAcao_presenca}

# caracteristica_Designar class attributes and methods
caracteristica_Designar_valor: Property = Property(name="valor", type=StringType)
caracteristica_Designar_tipoValor: Property = Property(name="tipoValor", type=StringType)
caracteristica_Designar.attributes={caracteristica_Designar_valor, caracteristica_Designar_tipoValor}

# caracteristica_ExpressaoLogica class attributes and methods
caracteristica_ExpressaoLogica_operadorLogico: Property = Property(name="operadorLogico", type=StringType)
caracteristica_ExpressaoLogica.attributes={caracteristica_ExpressaoLogica_operadorLogico}

# Antecedente class attributes and methods

# caracteristica_ExpressaoRelacional class attributes and methods
caracteristica_ExpressaoRelacional_operadorRelacional: Property = Property(name="operadorRelacional", type=StringType)
caracteristica_ExpressaoRelacional_valor: Property = Property(name="valor", type=StringType)
caracteristica_ExpressaoRelacional.attributes={caracteristica_ExpressaoRelacional_operadorRelacional, caracteristica_ExpressaoRelacional_valor}

# caracteristica_AcaoLogico class attributes and methods
caracteristica_AcaoLogico_operadorAcaoLogico: Property = Property(name="operadorAcaoLogico", type=StringType)
caracteristica_AcaoLogico.attributes={caracteristica_AcaoLogico_operadorAcaoLogico}

# Acao class attributes and methods

# caracteristica_Transicao class attributes and methods
caracteristica_Transicao_safe: Property = Property(name="safe", type=BooleanType)
caracteristica_Transicao_etiqueta: Property = Property(name="etiqueta", type=StringType)
caracteristica_Transicao.attributes={caracteristica_Transicao_safe, caracteristica_Transicao_etiqueta}

# caracteristica_Estado class attributes and methods
caracteristica_Estado_nome: Property = Property(name="nome", type=StringType)
caracteristica_Estado_safe: Property = Property(name="safe", type=BooleanType)
caracteristica_Estado.attributes={caracteristica_Estado_nome, caracteristica_Estado_safe}

# caracteristica_LiteralComposicao class attributes and methods
caracteristica_LiteralComposicao_presenca: Property = Property(name="presenca", type=StringType)
caracteristica_LiteralComposicao.attributes={caracteristica_LiteralComposicao_presenca}

# Relationships
produtos7: BinaryAssociation = BinaryAssociation(
    name="produtos7",
    ends={
        Property(name="caracteristica_Produto", type=caracteristica_LPS, multiplicity=Multiplicity(1, 1)),
        Property(name="caracteristica_LPS8", type=caracteristica_Produto, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expressoes9: BinaryAssociation = BinaryAssociation(
    name="expressoes9",
    ends={
        Property(name="caracteristica_Expressao", type=caracteristica_LPS, multiplicity=Multiplicity(1, 1)),
        Property(name="caracteristica_LPS10", type=caracteristica_Expressao, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elementosDeProduto11: BinaryAssociation = BinaryAssociation(
    name="elementosDeProduto11",
    ends={
        Property(name="caracteristica_ElementoDeProduto", type=caracteristica_LPS, multiplicity=Multiplicity(1, 1)),
        Property(name="caracteristica_LPS12", type=caracteristica_ElementoDeProduto, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sistema13: BinaryAssociation = BinaryAssociation(
    name="sistema13",
    ends={
        Property(name="CaracteristicaRaiz", type=caracteristica_LPS, multiplicity=Multiplicity(1, 1)),
        Property(name="LpsDoSistema", type=caracteristica_CaracteristicaRaiz, multiplicity=Multiplicity(0, 1))
    }
)
atributos14: BinaryAssociation = BinaryAssociation(
    name="atributos14",
    ends={
        Property(name="caracteristica_Atributo", type=caracteristica_LPS, multiplicity=Multiplicity(1, 1)),
        Property(name="caracteristica_LPS15", type=caracteristica_Atributo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
simulacoes16: BinaryAssociation = BinaryAssociation(
    name="simulacoes16",
    ends={
        Property(name="caracteristica_Simulacao", type=caracteristica_LPS, multiplicity=Multiplicity(1, 1)),
        Property(name="caracteristica_LPS17", type=caracteristica_Simulacao, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inconsistenciaERA18: BinaryAssociation = BinaryAssociation(
    name="inconsistenciaERA18",
    ends={
        Property(name="caracteristica_InconsistenciaRegraAdaptacao", type=caracteristica_LPS, multiplicity=Multiplicity(1, 1)),
        Property(name="caracteristica_LPS19", type=caracteristica_InconsistenciaRegraAdaptacao, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pontosDeVariacao0: BinaryAssociation = BinaryAssociation(
    name="pontosDeVariacao0",
    ends={
        Property(name="caracteristica_PontoDeVariacao", type=caracteristica_LPS, multiplicity=Multiplicity(1, 1)),
        Property(name="caracteristica_LPS", type=caracteristica_PontoDeVariacao, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elementos1: BinaryAssociation = BinaryAssociation(
    name="elementos1",
    ends={
        Property(name="caracteristica_Elemento", type=caracteristica_LPS, multiplicity=Multiplicity(1, 1)),
        Property(name="caracteristica_LPS2", type=caracteristica_Elemento, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
externos3: BinaryAssociation = BinaryAssociation(
    name="externos3",
    ends={
        Property(name="caracteristica_ElementoExterno", type=caracteristica_LPS, multiplicity=Multiplicity(1, 1)),
        Property(name="caracteristica_LPS4", type=caracteristica_ElementoExterno, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
regras5: BinaryAssociation = BinaryAssociation(
    name="regras5",
    ends={
        Property(name="caracteristica_Regra", type=caracteristica_LPS, multiplicity=Multiplicity(1, 1)),
        Property(name="caracteristica_LPS6", type=caracteristica_Regra, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
caracteristicaFilha27: BinaryAssociation = BinaryAssociation(
    name="caracteristicaFilha27",
    ends={
        Property(name="Caracteristica28", type=caracteristica_Caracteristica, multiplicity=Multiplicity(1, 1)),
        Property(name="caracteristicaPai", type=caracteristica_Caracteristica, multiplicity=Multiplicity(0, 9999))
    }
)
variacoes29: BinaryAssociation = BinaryAssociation(
    name="variacoes29",
    ends={
        Property(name="Variacao", type=caracteristica_Caracteristica, multiplicity=Multiplicity(1, 1)),
        Property(name="caracteristicaPai30", type=caracteristica_Variacao, multiplicity=Multiplicity(0, 9999))
    }
)
atributo31: BinaryAssociation = BinaryAssociation(
    name="atributo31",
    ends={
        Property(name="Atributo", type=caracteristica_Caracteristica, multiplicity=Multiplicity(1, 1)),
        Property(name="caracteristicaPai32", type=caracteristica_Atributo, multiplicity=Multiplicity(0, 9999))
    }
)
LpsDoSistema33: BinaryAssociation = BinaryAssociation(
    name="LpsDoSistema33",
    ends={
        Property(name="LPS", type=caracteristica_CaracteristicaRaiz, multiplicity=Multiplicity(1, 1)),
        Property(name="sistema", type=caracteristica_LPS, multiplicity=Multiplicity(1, 1))
    }
)
caracteristicaPai20: BinaryAssociation = BinaryAssociation(
    name="caracteristicaPai20",
    ends={
        Property(name="Caracteristica", type=caracteristica_Atributo, multiplicity=Multiplicity(1, 1)),
        Property(name="atributo", type=caracteristica_Caracteristica, multiplicity=Multiplicity(0, 1))
    }
)
elementosExternos21: BinaryAssociation = BinaryAssociation(
    name="elementosExternos21",
    ends={
        Property(name="caracteristica_ElementoExterno22", type=caracteristica_Caracteristica, multiplicity=Multiplicity(1, 1)),
        Property(name="caracteristica_Caracteristica", type=caracteristica_ElementoExterno, multiplicity=Multiplicity(0, 9999))
    }
)
variantes34: BinaryAssociation = BinaryAssociation(
    name="variantes34",
    ends={
        Property(name="variacaoPai", type=caracteristica_Variante, multiplicity=Multiplicity(0, 9999)),
        Property(name="Variante", type=caracteristica_Variacao, multiplicity=Multiplicity(1, 1))
    }
)
caracteristicaPai24: BinaryAssociation = BinaryAssociation(
    name="caracteristicaPai24",
    ends={
        Property(name="Caracteristica25", type=caracteristica_Caracteristica, multiplicity=Multiplicity(1, 1)),
        Property(name="caracteristicaFilha", type=caracteristica_Caracteristica, multiplicity=Multiplicity(0, 1))
    }
)
caracteristicaPai35: BinaryAssociation = BinaryAssociation(
    name="caracteristicaPai35",
    ends={
        Property(name="Caracteristica36", type=caracteristica_Variacao, multiplicity=Multiplicity(1, 1)),
        Property(name="variacoes", type=caracteristica_Caracteristica, multiplicity=Multiplicity(0, 1))
    }
)
variacaoPai37: BinaryAssociation = BinaryAssociation(
    name="variacaoPai37",
    ends={
        Property(name="Variacao38", type=caracteristica_Variante, multiplicity=Multiplicity(1, 1)),
        Property(name="variantes", type=caracteristica_Variacao, multiplicity=Multiplicity(0, 1))
    }
)
entidadesDeContexto39: BinaryAssociation = BinaryAssociation(
    name="entidadesDeContexto39",
    ends={
        Property(name="EntidadeDeContexto", type=caracteristica_RaizDeContexto, multiplicity=Multiplicity(1, 1)),
        Property(name="raiz", type=caracteristica_EntidadeDeContexto, multiplicity=Multiplicity(0, 9999))
    }
)
raiz40: BinaryAssociation = BinaryAssociation(
    name="raiz40",
    ends={
        Property(name="RaizDeContexto", type=caracteristica_EntidadeDeContexto, multiplicity=Multiplicity(1, 1)),
        Property(name="entidadesDeContexto", type=caracteristica_RaizDeContexto, multiplicity=Multiplicity(0, 1))
    }
)
informacoesDeContexto41: BinaryAssociation = BinaryAssociation(
    name="informacoesDeContexto41",
    ends={
        Property(name="InformacaoDeContexto", type=caracteristica_EntidadeDeContexto, multiplicity=Multiplicity(1, 1)),
        Property(name="elementoPai", type=caracteristica_InformacaoDeContexto, multiplicity=Multiplicity(0, 9999))
    }
)
atributoProduto52: BinaryAssociation = BinaryAssociation(
    name="atributoProduto52",
    ends={
        Property(name="AtributoProduto", type=caracteristica_CaracteristicaProduto, multiplicity=Multiplicity(1, 1)),
        Property(name="caracteristicaProdutoPai53", type=caracteristica_AtributoProduto, multiplicity=Multiplicity(0, 9999))
    }
)
caracteristicaProdutoPai54: BinaryAssociation = BinaryAssociation(
    name="caracteristicaProdutoPai54",
    ends={
        Property(name="CaracteristicaProduto55", type=caracteristica_AtributoProduto, multiplicity=Multiplicity(1, 1)),
        Property(name="atributoProduto", type=caracteristica_CaracteristicaProduto, multiplicity=Multiplicity(0, 1))
    }
)
elementoPai42: BinaryAssociation = BinaryAssociation(
    name="elementoPai42",
    ends={
        Property(name="EntidadeDeContexto43", type=caracteristica_InformacaoDeContexto, multiplicity=Multiplicity(1, 1)),
        Property(name="informacoesDeContexto", type=caracteristica_EntidadeDeContexto, multiplicity=Multiplicity(1, 1))
    }
)
elementoOriginal44: BinaryAssociation = BinaryAssociation(
    name="elementoOriginal44",
    ends={
        Property(name="caracteristica_Elemento46", type=caracteristica_ElementoDeProduto, multiplicity=Multiplicity(1, 1)),
        Property(name="caracteristica_ElementoDeProduto45", type=caracteristica_Elemento, multiplicity=Multiplicity(0, 1))
    }
)
caracteristicaProdutoPai48: BinaryAssociation = BinaryAssociation(
    name="caracteristicaProdutoPai48",
    ends={
        Property(name="CaracteristicaProduto", type=caracteristica_CaracteristicaProduto, multiplicity=Multiplicity(1, 1)),
        Property(name="caracteristicaProdutoFilha", type=caracteristica_CaracteristicaProduto, multiplicity=Multiplicity(0, 1))
    }
)
caracteristicaProdutoFilha50: BinaryAssociation = BinaryAssociation(
    name="caracteristicaProdutoFilha50",
    ends={
        Property(name="CaracteristicaProduto51", type=caracteristica_CaracteristicaProduto, multiplicity=Multiplicity(1, 1)),
        Property(name="caracteristicaProdutoPai", type=caracteristica_CaracteristicaProduto, multiplicity=Multiplicity(0, 9999))
    }
)
caracteristicaProdutoPai57: BinaryAssociation = BinaryAssociation(
    name="caracteristicaProdutoPai57",
    ends={
        Property(name="caracteristica_CaracteristicaProduto", type=caracteristica_VariacaoProduto, multiplicity=Multiplicity(1, 1)),
        Property(name="caracteristica_VariacaoProduto", type=caracteristica_CaracteristicaProduto, multiplicity=Multiplicity(0, 1))
    }
)
variacaoProdutoPai58: BinaryAssociation = BinaryAssociation(
    name="variacaoProdutoPai58",
    ends={
        Property(name="VariacaoProduto", type=caracteristica_VarianteProduto, multiplicity=Multiplicity(1, 1)),
        Property(name="variantesProduto", type=caracteristica_VariacaoProduto, multiplicity=Multiplicity(1, 1))
    }
)
LinhaDoProduto59: BinaryAssociation = BinaryAssociation(
    name="LinhaDoProduto59",
    ends={
        Property(name="caracteristica_CaracteristicaRaiz", type=caracteristica_Produto, multiplicity=Multiplicity(1, 1)),
        Property(name="caracteristica_Produto60", type=caracteristica_CaracteristicaRaiz, multiplicity=Multiplicity(0, 1))
    }
)
variantesProduto56: BinaryAssociation = BinaryAssociation(
    name="variantesProduto56",
    ends={
        Property(name="VarianteProduto", type=caracteristica_VariacaoProduto, multiplicity=Multiplicity(1, 1)),
        Property(name="variacaoProdutoPai", type=caracteristica_VarianteProduto, multiplicity=Multiplicity(0, 9999))
    }
)
evento65: BinaryAssociation = BinaryAssociation(
    name="evento65",
    ends={
        Property(name="caracteristica_Evento", type=caracteristica_RegraDeContexto, multiplicity=Multiplicity(1, 1)),
        Property(name="caracteristica_RegraDeContexto", type=caracteristica_Evento, multiplicity=Multiplicity(0, 1))
    }
)
acao66: BinaryAssociation = BinaryAssociation(
    name="acao66",
    ends={
        Property(name="caracteristica_Acao", type=caracteristica_RegraDeContexto, multiplicity=Multiplicity(1, 1)),
        Property(name="caracteristica_RegraDeContexto67", type=caracteristica_Acao, multiplicity=Multiplicity(0, 1))
    }
)
ladoDireitoEvento68: BinaryAssociation = BinaryAssociation(
    name="ladoDireitoEvento68",
    ends={
        Property(name="caracteristica_Evento69", type=caracteristica_EventoLogico, multiplicity=Multiplicity(1, 1)),
        Property(name="caracteristica_EventoLogico", type=caracteristica_Evento, multiplicity=Multiplicity(0, 1))
    }
)
ladoEsquerdoEvento70: BinaryAssociation = BinaryAssociation(
    name="ladoEsquerdoEvento70",
    ends={
        Property(name="caracteristica_Evento72", type=caracteristica_EventoLogico, multiplicity=Multiplicity(1, 1)),
        Property(name="caracteristica_EventoLogico71", type=caracteristica_Evento, multiplicity=Multiplicity(0, 1))
    }
)
variavelDeContexto73: BinaryAssociation = BinaryAssociation(
    name="variavelDeContexto73",
    ends={
        Property(name="caracteristica_InformacaoDeContexto", type=caracteristica_EventoRelacional, multiplicity=Multiplicity(1, 1)),
        Property(name="caracteristica_EventoRelacional", type=caracteristica_InformacaoDeContexto, multiplicity=Multiplicity(0, 1))
    }
)
antecedente61: BinaryAssociation = BinaryAssociation(
    name="antecedente61",
    ends={
        Property(name="caracteristica_Antecedente", type=caracteristica_RegraDeComposicao, multiplicity=Multiplicity(1, 1)),
        Property(name="caracteristica_RegraDeComposicao", type=caracteristica_Antecedente, multiplicity=Multiplicity(0, 1))
    }
)
consequente62: BinaryAssociation = BinaryAssociation(
    name="consequente62",
    ends={
        Property(name="caracteristica_Antecedente64", type=caracteristica_RegraDeComposicao, multiplicity=Multiplicity(1, 1)),
        Property(name="caracteristica_RegraDeComposicao63", type=caracteristica_Antecedente, multiplicity=Multiplicity(0, 1))
    }
)
elemento79: BinaryAssociation = BinaryAssociation(
    name="elemento79",
    ends={
        Property(name="caracteristica_ElementoCaracteristico", type=caracteristica_LiteralAcao, multiplicity=Multiplicity(1, 1)),
        Property(name="caracteristica_LiteralAcao", type=caracteristica_ElementoCaracteristico, multiplicity=Multiplicity(0, 1))
    }
)
atributo80: BinaryAssociation = BinaryAssociation(
    name="atributo80",
    ends={
        Property(name="caracteristica_Atributo81", type=caracteristica_Designar, multiplicity=Multiplicity(1, 1)),
        Property(name="caracteristica_Designar", type=caracteristica_Atributo, multiplicity=Multiplicity(0, 1))
    }
)
ladoDireitoComposicao82: BinaryAssociation = BinaryAssociation(
    name="ladoDireitoComposicao82",
    ends={
        Property(name="caracteristica_Antecedente83", type=caracteristica_ExpressaoLogica, multiplicity=Multiplicity(1, 1)),
        Property(name="caracteristica_ExpressaoLogica", type=caracteristica_Antecedente, multiplicity=Multiplicity(0, 1))
    }
)
ladoEsquerdoComposicao84: BinaryAssociation = BinaryAssociation(
    name="ladoEsquerdoComposicao84",
    ends={
        Property(name="caracteristica_Antecedente86", type=caracteristica_ExpressaoLogica, multiplicity=Multiplicity(1, 1)),
        Property(name="caracteristica_ExpressaoLogica85", type=caracteristica_Antecedente, multiplicity=Multiplicity(0, 1))
    }
)
variaveldaExpressao87: BinaryAssociation = BinaryAssociation(
    name="variaveldaExpressao87",
    ends={
        Property(name="caracteristica_Atributo88", type=caracteristica_ExpressaoRelacional, multiplicity=Multiplicity(1, 1)),
        Property(name="caracteristica_ExpressaoRelacional", type=caracteristica_Atributo, multiplicity=Multiplicity(0, 1))
    }
)
ladoEsquerdoAcao74: BinaryAssociation = BinaryAssociation(
    name="ladoEsquerdoAcao74",
    ends={
        Property(name="caracteristica_Acao75", type=caracteristica_AcaoLogico, multiplicity=Multiplicity(1, 1)),
        Property(name="caracteristica_AcaoLogico", type=caracteristica_Acao, multiplicity=Multiplicity(1, 1))
    }
)
ladoDireitoAcao76: BinaryAssociation = BinaryAssociation(
    name="ladoDireitoAcao76",
    ends={
        Property(name="caracteristica_Acao78", type=caracteristica_AcaoLogico, multiplicity=Multiplicity(1, 1)),
        Property(name="caracteristica_AcaoLogico77", type=caracteristica_Acao, multiplicity=Multiplicity(1, 1))
    }
)
transicoes91: BinaryAssociation = BinaryAssociation(
    name="transicoes91",
    ends={
        Property(name="caracteristica_Transicao", type=caracteristica_Simulacao, multiplicity=Multiplicity(1, 1)),
        Property(name="caracteristica_Simulacao92", type=caracteristica_Transicao, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
estados93: BinaryAssociation = BinaryAssociation(
    name="estados93",
    ends={
        Property(name="caracteristica_Estado", type=caracteristica_Simulacao, multiplicity=Multiplicity(1, 1)),
        Property(name="caracteristica_Simulacao94", type=caracteristica_Estado, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eAntigo95: BinaryAssociation = BinaryAssociation(
    name="eAntigo95",
    ends={
        Property(name="caracteristica_Estado97", type=caracteristica_Transicao, multiplicity=Multiplicity(1, 1)),
        Property(name="caracteristica_Transicao96", type=caracteristica_Estado, multiplicity=Multiplicity(0, 1))
    }
)
eNovo98: BinaryAssociation = BinaryAssociation(
    name="eNovo98",
    ends={
        Property(name="caracteristica_Estado100", type=caracteristica_Transicao, multiplicity=Multiplicity(1, 1)),
        Property(name="caracteristica_Transicao99", type=caracteristica_Estado, multiplicity=Multiplicity(0, 1))
    }
)
regrasQuebradas101: BinaryAssociation = BinaryAssociation(
    name="regrasQuebradas101",
    ends={
        Property(name="caracteristica_RegraDeComposicao103", type=caracteristica_Transicao, multiplicity=Multiplicity(1, 1)),
        Property(name="caracteristica_Transicao102", type=caracteristica_RegraDeComposicao, multiplicity=Multiplicity(0, 9999))
    }
)
acoes104: BinaryAssociation = BinaryAssociation(
    name="acoes104",
    ends={
        Property(name="caracteristica_Acao106", type=caracteristica_Transicao, multiplicity=Multiplicity(1, 1)),
        Property(name="caracteristica_Transicao105", type=caracteristica_Acao, multiplicity=Multiplicity(0, 9999))
    }
)
produto107: BinaryAssociation = BinaryAssociation(
    name="produto107",
    ends={
        Property(name="caracteristica_CaracteristicaProduto109", type=caracteristica_Estado, multiplicity=Multiplicity(1, 1)),
        Property(name="caracteristica_Estado108", type=caracteristica_CaracteristicaProduto, multiplicity=Multiplicity(0, 1))
    }
)
elemento89: BinaryAssociation = BinaryAssociation(
    name="elemento89",
    ends={
        Property(name="caracteristica_ElementoCaracteristico90", type=caracteristica_LiteralComposicao, multiplicity=Multiplicity(1, 1)),
        Property(name="caracteristica_LiteralComposicao", type=caracteristica_ElementoCaracteristico, multiplicity=Multiplicity(0, 1))
    }
)
regrasInconsistentes110: BinaryAssociation = BinaryAssociation(
    name="regrasInconsistentes110",
    ends={
        Property(name="caracteristica_RegraDeContexto112", type=caracteristica_InconsistenciaRegraAdaptacao, multiplicity=Multiplicity(1, 1)),
        Property(name="caracteristica_InconsistenciaRegraAdaptacao111", type=caracteristica_RegraDeContexto, multiplicity=Multiplicity(0, 9999))
    }
)
literaisInconsistentes113: BinaryAssociation = BinaryAssociation(
    name="literaisInconsistentes113",
    ends={
        Property(name="caracteristica_LiteralAcao115", type=caracteristica_InconsistenciaRegraAdaptacao, multiplicity=Multiplicity(1, 1)),
        Property(name="caracteristica_InconsistenciaRegraAdaptacao114", type=caracteristica_LiteralAcao, multiplicity=Multiplicity(0, 9999))
    }
)
atribuicoesInconsistentes116: BinaryAssociation = BinaryAssociation(
    name="atribuicoesInconsistentes116",
    ends={
        Property(name="caracteristica_Designar118", type=caracteristica_InconsistenciaRegraAdaptacao, multiplicity=Multiplicity(1, 1)),
        Property(name="caracteristica_InconsistenciaRegraAdaptacao117", type=caracteristica_Designar, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_caracteristica_CasoDeUso_ElementoExterno = Generalization(general=ElementoExterno, specific=caracteristica_CasoDeUso)
gen_caracteristica_CasoDeTeste_ElementoExterno = Generalization(general=ElementoExterno, specific=caracteristica_CasoDeTeste)
gen_caracteristica_ElementoCaracteristico_Elemento = Generalization(general=Elemento, specific=caracteristica_ElementoCaracteristico)
gen_caracteristica_Atributo_Elemento = Generalization(general=Elemento, specific=caracteristica_Atributo)
gen_caracteristica_CaracteristicaRaiz_Caracteristica = Generalization(general=Caracteristica, specific=caracteristica_CaracteristicaRaiz)
gen_caracteristica_CaracteristicaOpcional_Caracteristica = Generalization(general=Caracteristica, specific=caracteristica_CaracteristicaOpcional)
gen_caracteristica_CaracteristicaOpcional_ElementoCaracteristico = Generalization(general=ElementoCaracteristico, specific=caracteristica_CaracteristicaOpcional)
gen_caracteristica_CaracteristicaAgrupada_Caracteristica = Generalization(general=Caracteristica, specific=caracteristica_CaracteristicaAgrupada)
gen_caracteristica_CaracteristicaAgrupada_ElementoCaracteristico = Generalization(general=ElementoCaracteristico, specific=caracteristica_CaracteristicaAgrupada)
gen_caracteristica_Caracteristica_Elemento = Generalization(general=Elemento, specific=caracteristica_Caracteristica)
gen_caracteristica_Variante_PontoDeVariacao = Generalization(general=PontoDeVariacao, specific=caracteristica_Variante)
gen_caracteristica_Variante_ElementoCaracteristico = Generalization(general=ElementoCaracteristico, specific=caracteristica_Variante)
gen_caracteristica_Variante_Caracteristica = Generalization(general=Caracteristica, specific=caracteristica_Variante)
gen_caracteristica_RaizDeContexto_Elemento = Generalization(general=Elemento, specific=caracteristica_RaizDeContexto)
gen_caracteristica_EntidadeDeContexto_Elemento = Generalization(general=Elemento, specific=caracteristica_EntidadeDeContexto)
gen_caracteristica_InformacaoDeContexto_Elemento = Generalization(general=Elemento, specific=caracteristica_InformacaoDeContexto)
gen_caracteristica_CaracteristicaMandatoria_Caracteristica = Generalization(general=Caracteristica, specific=caracteristica_CaracteristicaMandatoria)
gen_caracteristica_VariacaoDois_Caracteristica = Generalization(general=Caracteristica, specific=caracteristica_VariacaoDois)
gen_caracteristica_VariacaoDois_ElementoCaracteristico = Generalization(general=ElementoCaracteristico, specific=caracteristica_VariacaoDois)
gen_caracteristica_Variacao_PontoDeVariacao = Generalization(general=PontoDeVariacao, specific=caracteristica_Variacao)
gen_caracteristica_Variacao_Elemento = Generalization(general=Elemento, specific=caracteristica_Variacao)
gen_caracteristica_AtributoProduto_ElementoDeProduto = Generalization(general=ElementoDeProduto, specific=caracteristica_AtributoProduto)
gen_caracteristica_CaracteristicaMandatoriaProduto_CaracteristicaProduto = Generalization(general=CaracteristicaProduto, specific=caracteristica_CaracteristicaMandatoriaProduto)
gen_caracteristica_CaracteristicaOpcionalProduto_CaracteristicaProduto = Generalization(general=CaracteristicaProduto, specific=caracteristica_CaracteristicaOpcionalProduto)
gen_caracteristica_VariacaoDoisProduto_CaracteristicaProduto = Generalization(general=CaracteristicaProduto, specific=caracteristica_VariacaoDoisProduto)
gen_caracteristica_CaracteristicaAgrupadaProduto_CaracteristicaProduto = Generalization(general=CaracteristicaProduto, specific=caracteristica_CaracteristicaAgrupadaProduto)
gen_caracteristica_VariacaoProduto_ElementoDeProduto = Generalization(general=ElementoDeProduto, specific=caracteristica_VariacaoProduto)
gen_caracteristica_CaracteristicaProduto_ElementoDeProduto = Generalization(general=ElementoDeProduto, specific=caracteristica_CaracteristicaProduto)
gen_caracteristica_VarianteProduto_ElementoDeProduto = Generalization(general=ElementoDeProduto, specific=caracteristica_VarianteProduto)
gen_caracteristica_Produto_CaracteristicaProduto = Generalization(general=CaracteristicaProduto, specific=caracteristica_Produto)
gen_caracteristica_RegraDeContexto_Regra = Generalization(general=Regra, specific=caracteristica_RegraDeContexto)
gen_caracteristica_Evento_Expressao = Generalization(general=Expressao, specific=caracteristica_Evento)
gen_caracteristica_EventoLogico_Evento = Generalization(general=Evento, specific=caracteristica_EventoLogico)
gen_caracteristica_EventoRelacional_Evento = Generalization(general=Evento, specific=caracteristica_EventoRelacional)
gen_caracteristica_RegraDeComposicao_Regra = Generalization(general=Regra, specific=caracteristica_RegraDeComposicao)
gen_caracteristica_LiteralAcao_Acao = Generalization(general=Acao, specific=caracteristica_LiteralAcao)
gen_caracteristica_Designar_Acao = Generalization(general=Acao, specific=caracteristica_Designar)
gen_caracteristica_Antecedente_Expressao = Generalization(general=Expressao, specific=caracteristica_Antecedente)
gen_caracteristica_ExpressaoLogica_Antecedente = Generalization(general=Antecedente, specific=caracteristica_ExpressaoLogica)
gen_caracteristica_ExpressaoRelacional_Antecedente = Generalization(general=Antecedente, specific=caracteristica_ExpressaoRelacional)
gen_caracteristica_Acao_Expressao = Generalization(general=Expressao, specific=caracteristica_Acao)
gen_caracteristica_AcaoLogico_Acao = Generalization(general=Acao, specific=caracteristica_AcaoLogico)
gen_caracteristica_LiteralComposicao_Antecedente = Generalization(general=Antecedente, specific=caracteristica_LiteralComposicao)

# Domain Model
domain_model = DomainModel(
    name="caracteristica",
    types={caracteristica_Produto, caracteristica_Expressao, caracteristica_ElementoDeProduto, caracteristica_CaracteristicaRaiz, caracteristica_Atributo, caracteristica_Simulacao, caracteristica_InconsistenciaRegraAdaptacao, caracteristica_CasoDeUso, ElementoExterno, caracteristica_CasoDeTeste, caracteristica_ElementoCaracteristico, Elemento, caracteristica_LPS, caracteristica_PontoDeVariacao, caracteristica_Elemento, caracteristica_ElementoExterno, caracteristica_Regra, caracteristica_Variacao, Caracteristica, caracteristica_CaracteristicaOpcional, ElementoCaracteristico, caracteristica_CaracteristicaAgrupada, caracteristica_Caracteristica, caracteristica_RaizDeContexto, caracteristica_EntidadeDeContexto, caracteristica_InformacaoDeContexto, caracteristica_CaracteristicaMandatoria, caracteristica_VariacaoDois, PontoDeVariacao, caracteristica_Variante, caracteristica_AtributoProduto, caracteristica_CaracteristicaMandatoriaProduto, CaracteristicaProduto, caracteristica_CaracteristicaOpcionalProduto, caracteristica_VariacaoDoisProduto, caracteristica_CaracteristicaAgrupadaProduto, caracteristica_VariacaoProduto, caracteristica_CaracteristicaProduto, ElementoDeProduto, caracteristica_VarianteProduto, caracteristica_RegraDeContexto, caracteristica_Evento, caracteristica_Acao, Expressao, caracteristica_EventoLogico, Evento, caracteristica_EventoRelacional, caracteristica_RegraDeComposicao, Regra, caracteristica_Antecedente, caracteristica_LiteralAcao, caracteristica_Designar, caracteristica_ExpressaoLogica, Antecedente, caracteristica_ExpressaoRelacional, caracteristica_AcaoLogico, Acao, caracteristica_Transicao, caracteristica_Estado, caracteristica_LiteralComposicao, Origem, Validade, Qualidade, TipoValor, OperadorRelacional, Presenca, OperadorLogico, OperadorAcaoLogico, CardinalidadeMaxima},
    associations={produtos7, expressoes9, elementosDeProduto11, sistema13, atributos14, simulacoes16, inconsistenciaERA18, pontosDeVariacao0, elementos1, externos3, regras5, caracteristicaFilha27, variacoes29, atributo31, LpsDoSistema33, caracteristicaPai20, elementosExternos21, variantes34, caracteristicaPai24, caracteristicaPai35, variacaoPai37, entidadesDeContexto39, raiz40, informacoesDeContexto41, atributoProduto52, caracteristicaProdutoPai54, elementoPai42, elementoOriginal44, caracteristicaProdutoPai48, caracteristicaProdutoFilha50, caracteristicaProdutoPai57, variacaoProdutoPai58, LinhaDoProduto59, variantesProduto56, evento65, acao66, ladoDireitoEvento68, ladoEsquerdoEvento70, variavelDeContexto73, antecedente61, consequente62, elemento79, atributo80, ladoDireitoComposicao82, ladoEsquerdoComposicao84, variaveldaExpressao87, ladoEsquerdoAcao74, ladoDireitoAcao76, transicoes91, estados93, eAntigo95, eNovo98, regrasQuebradas101, acoes104, produto107, elemento89, regrasInconsistentes110, literaisInconsistentes113, atribuicoesInconsistentes116},
    generalizations={gen_caracteristica_CasoDeUso_ElementoExterno, gen_caracteristica_CasoDeTeste_ElementoExterno, gen_caracteristica_ElementoCaracteristico_Elemento, gen_caracteristica_Atributo_Elemento, gen_caracteristica_CaracteristicaRaiz_Caracteristica, gen_caracteristica_CaracteristicaOpcional_Caracteristica, gen_caracteristica_CaracteristicaOpcional_ElementoCaracteristico, gen_caracteristica_CaracteristicaAgrupada_Caracteristica, gen_caracteristica_CaracteristicaAgrupada_ElementoCaracteristico, gen_caracteristica_Caracteristica_Elemento, gen_caracteristica_Variante_PontoDeVariacao, gen_caracteristica_Variante_ElementoCaracteristico, gen_caracteristica_Variante_Caracteristica, gen_caracteristica_RaizDeContexto_Elemento, gen_caracteristica_EntidadeDeContexto_Elemento, gen_caracteristica_InformacaoDeContexto_Elemento, gen_caracteristica_CaracteristicaMandatoria_Caracteristica, gen_caracteristica_VariacaoDois_Caracteristica, gen_caracteristica_VariacaoDois_ElementoCaracteristico, gen_caracteristica_Variacao_PontoDeVariacao, gen_caracteristica_Variacao_Elemento, gen_caracteristica_AtributoProduto_ElementoDeProduto, gen_caracteristica_CaracteristicaMandatoriaProduto_CaracteristicaProduto, gen_caracteristica_CaracteristicaOpcionalProduto_CaracteristicaProduto, gen_caracteristica_VariacaoDoisProduto_CaracteristicaProduto, gen_caracteristica_CaracteristicaAgrupadaProduto_CaracteristicaProduto, gen_caracteristica_VariacaoProduto_ElementoDeProduto, gen_caracteristica_CaracteristicaProduto_ElementoDeProduto, gen_caracteristica_VarianteProduto_ElementoDeProduto, gen_caracteristica_Produto_CaracteristicaProduto, gen_caracteristica_RegraDeContexto_Regra, gen_caracteristica_Evento_Expressao, gen_caracteristica_EventoLogico_Evento, gen_caracteristica_EventoRelacional_Evento, gen_caracteristica_RegraDeComposicao_Regra, gen_caracteristica_LiteralAcao_Acao, gen_caracteristica_Designar_Acao, gen_caracteristica_Antecedente_Expressao, gen_caracteristica_ExpressaoLogica_Antecedente, gen_caracteristica_ExpressaoRelacional_Antecedente, gen_caracteristica_Acao_Expressao, gen_caracteristica_AcaoLogico_Acao, gen_caracteristica_LiteralComposicao_Antecedente},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)