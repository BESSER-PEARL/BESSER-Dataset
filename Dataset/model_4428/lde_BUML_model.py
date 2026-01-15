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
arduino_Acao = Class(name="arduino::Acao", is_abstract=True)
arduino_Transicoes = Class(name="arduino::Transicoes")
arduino_Condicao = Class(name="arduino::Condicao", is_abstract=True)
arduino_Virar_Esquerda = Class(name="arduino::Virar::Esquerda")
Corpo = Class(name="Corpo")
arduino_Mover_Frente = Class(name="arduino::Mover::Frente")
arduino_Robo = Class(name="arduino::Robo")
arduino_Rodar_Direita_Tempo = Class(name="arduino::Rodar::Direita::Tempo")
arduino_Acoes_Predefinidas = Class(name="arduino::Acoes::Predefinidas", is_abstract=True)
Acao = Class(name="Acao")
arduino_Acoes_Modificaveis = Class(name="arduino::Acoes::Modificaveis", is_abstract=True)
arduino_Mover_Frente_Tempo = Class(name="arduino::Mover::Frente::Tempo")
arduino_Mover_Tras_Tempo = Class(name="arduino::Mover::Tras::Tempo")
arduino_Virar_para_X_Graus = Class(name="arduino::Virar::para::X::Graus")
Cabeca_Modificavel = Class(name="Cabeca::Modificavel")
arduino_Virar_Max_Drt = Class(name="arduino::Virar::Max::Drt")
Cabeca = Class(name="Cabeca")
arduino_Virar_Max_Esq = Class(name="arduino::Virar::Max::Esq")
arduino_Centrar = Class(name="arduino::Centrar")
arduino_Mover_Tras = Class(name="arduino::Mover::Tras")
arduino_Virar_Direita = Class(name="arduino::Virar::Direita")
arduino_Rodar_Esquerda_Tempo = Class(name="arduino::Rodar::Esquerda::Tempo")
Corpo_Modificavel = Class(name="Corpo::Modificavel")
arduino_Mover_Aleatoriamente = Class(name="arduino::Mover::Aleatoriamente")
arduino_LED = Class(name="arduino::LED", is_abstract=True)
Acoes_Predefinidas = Class(name="Acoes::Predefinidas")
arduino_Verde = Class(name="arduino::Verde", is_abstract=True)
LED = Class(name="LED")
arduino_Tricolor = Class(name="arduino::Tricolor", is_abstract=True)
arduino_Ligar_LED_Verde = Class(name="arduino::Ligar::LED::Verde")
Verde = Class(name="Verde")
arduino_Desligar_LED_Verde = Class(name="arduino::Desligar::LED::Verde")
arduino_Ligar_Intermitencia = Class(name="arduino::Ligar::Intermitencia")
arduino_Desligar_Intermitencia = Class(name="arduino::Desligar::Intermitencia")
arduino_Varias_Cores = Class(name="arduino::Varias::Cores", is_abstract=True)
Tricolor = Class(name="Tricolor")
arduino_Unica_Cor = Class(name="arduino::Unica::Cor", is_abstract=True)
arduino_Virar_45_Esq = Class(name="arduino::Virar::45::Esq")
arduino_Virar_45_Drt = Class(name="arduino::Virar::45::Drt")
arduino_Ligar_Verde = Class(name="arduino::Ligar::Verde")
arduino_Ligar_Vermelho = Class(name="arduino::Ligar::Vermelho")
arduino_Desligar_Cor = Class(name="arduino::Desligar::Cor")
arduino_Desligar_Cores = Class(name="arduino::Desligar::Cores")
arduino_Acoes_Condicionais = Class(name="arduino::Acoes::Condicionais", is_abstract=True)
arduino_While = Class(name="arduino::While")
Acoes_Condicionais = Class(name="Acoes::Condicionais")
arduino_Ligar_Cores_Policia = Class(name="arduino::Ligar::Cores::Policia")
Varias_Cores = Class(name="Varias::Cores")
arduino_Ligar_Cores_Arco_Iris = Class(name="arduino::Ligar::Cores::Arco::Iris")
arduino_Ligar_Azul = Class(name="arduino::Ligar::Azul")
arduino_Bumper_Pressionado = Class(name="arduino::Bumper::Pressionado")
Unica_Cor = Class(name="Unica::Cor")
Condicao = Class(name="Condicao")
arduino_Distancia_Infra_Vermelhos = Class(name="arduino::Distancia::Infra::Vermelhos")
arduino_Corpo = Class(name="arduino::Corpo", is_abstract=True)
arduino_Corpo_Modificavel = Class(name="arduino::Corpo::Modificavel", is_abstract=True)
Acoes_Modificaveis = Class(name="Acoes::Modificaveis")
arduino_Cabeca = Class(name="arduino::Cabeca", is_abstract=True)
arduino_Cabeca_Modificavel = Class(name="arduino::Cabeca::Modificavel", is_abstract=True)
arduino_Inicio = Class(name="arduino::Inicio")
arduino_Fim = Class(name="arduino::Fim")
arduino_Parar = Class(name="arduino::Parar")
arduino_If = Class(name="arduino::If")
arduino_Parar_Tempo = Class(name="arduino::Parar::Tempo")

# arduino_Acao class attributes and methods

# arduino_Transicoes class attributes and methods

# arduino_Condicao class attributes and methods

# arduino_Virar_Esquerda class attributes and methods
arduino_Virar_Esquerda_nome: Property = Property(name="nome", type=StringType)
arduino_Virar_Esquerda.attributes={arduino_Virar_Esquerda_nome}

# Corpo class attributes and methods

# arduino_Mover_Frente class attributes and methods
arduino_Mover_Frente_nome: Property = Property(name="nome", type=StringType)
arduino_Mover_Frente.attributes={arduino_Mover_Frente_nome}

# arduino_Robo class attributes and methods
arduino_Robo_Nome: Property = Property(name="Nome", type=StringType)
arduino_Robo.attributes={arduino_Robo_Nome}

# arduino_Rodar_Direita_Tempo class attributes and methods

# arduino_Acoes_Predefinidas class attributes and methods

# Acao class attributes and methods

# arduino_Acoes_Modificaveis class attributes and methods

# arduino_Mover_Frente_Tempo class attributes and methods

# arduino_Mover_Tras_Tempo class attributes and methods

# arduino_Virar_para_X_Graus class attributes and methods

# Cabeca_Modificavel class attributes and methods

# arduino_Virar_Max_Drt class attributes and methods
arduino_Virar_Max_Drt_nome: Property = Property(name="nome", type=StringType)
arduino_Virar_Max_Drt.attributes={arduino_Virar_Max_Drt_nome}

# Cabeca class attributes and methods

# arduino_Virar_Max_Esq class attributes and methods
arduino_Virar_Max_Esq_nome: Property = Property(name="nome", type=StringType)
arduino_Virar_Max_Esq.attributes={arduino_Virar_Max_Esq_nome}

# arduino_Centrar class attributes and methods
arduino_Centrar_nome: Property = Property(name="nome", type=StringType)
arduino_Centrar.attributes={arduino_Centrar_nome}

# arduino_Mover_Tras class attributes and methods
arduino_Mover_Tras_nome: Property = Property(name="nome", type=StringType)
arduino_Mover_Tras.attributes={arduino_Mover_Tras_nome}

# arduino_Virar_Direita class attributes and methods
arduino_Virar_Direita_nome: Property = Property(name="nome", type=StringType)
arduino_Virar_Direita.attributes={arduino_Virar_Direita_nome}

# arduino_Rodar_Esquerda_Tempo class attributes and methods

# Corpo_Modificavel class attributes and methods

# arduino_Mover_Aleatoriamente class attributes and methods
arduino_Mover_Aleatoriamente_nome: Property = Property(name="nome", type=StringType)
arduino_Mover_Aleatoriamente.attributes={arduino_Mover_Aleatoriamente_nome}

# arduino_LED class attributes and methods

# Acoes_Predefinidas class attributes and methods

# arduino_Verde class attributes and methods

# LED class attributes and methods

# arduino_Tricolor class attributes and methods

# arduino_Ligar_LED_Verde class attributes and methods
arduino_Ligar_LED_Verde_nome: Property = Property(name="nome", type=StringType)
arduino_Ligar_LED_Verde.attributes={arduino_Ligar_LED_Verde_nome}

# Verde class attributes and methods

# arduino_Desligar_LED_Verde class attributes and methods
arduino_Desligar_LED_Verde_nome: Property = Property(name="nome", type=StringType)
arduino_Desligar_LED_Verde.attributes={arduino_Desligar_LED_Verde_nome}

# arduino_Ligar_Intermitencia class attributes and methods
arduino_Ligar_Intermitencia_nome: Property = Property(name="nome", type=StringType)
arduino_Ligar_Intermitencia.attributes={arduino_Ligar_Intermitencia_nome}

# arduino_Desligar_Intermitencia class attributes and methods
arduino_Desligar_Intermitencia_nome: Property = Property(name="nome", type=StringType)
arduino_Desligar_Intermitencia.attributes={arduino_Desligar_Intermitencia_nome}

# arduino_Varias_Cores class attributes and methods

# Tricolor class attributes and methods

# arduino_Unica_Cor class attributes and methods

# arduino_Virar_45_Esq class attributes and methods
arduino_Virar_45_Esq_nome: Property = Property(name="nome", type=StringType)
arduino_Virar_45_Esq.attributes={arduino_Virar_45_Esq_nome}

# arduino_Virar_45_Drt class attributes and methods
arduino_Virar_45_Drt_nome: Property = Property(name="nome", type=StringType)
arduino_Virar_45_Drt.attributes={arduino_Virar_45_Drt_nome}

# arduino_Ligar_Verde class attributes and methods
arduino_Ligar_Verde_nome: Property = Property(name="nome", type=StringType)
arduino_Ligar_Verde.attributes={arduino_Ligar_Verde_nome}

# arduino_Ligar_Vermelho class attributes and methods
arduino_Ligar_Vermelho_nome: Property = Property(name="nome", type=StringType)
arduino_Ligar_Vermelho.attributes={arduino_Ligar_Vermelho_nome}

# arduino_Desligar_Cor class attributes and methods
arduino_Desligar_Cor_nome: Property = Property(name="nome", type=StringType)
arduino_Desligar_Cor.attributes={arduino_Desligar_Cor_nome}

# arduino_Desligar_Cores class attributes and methods
arduino_Desligar_Cores_nome: Property = Property(name="nome", type=StringType)
arduino_Desligar_Cores.attributes={arduino_Desligar_Cores_nome}

# arduino_Acoes_Condicionais class attributes and methods

# arduino_While class attributes and methods
arduino_While_nome: Property = Property(name="nome", type=StringType)
arduino_While.attributes={arduino_While_nome}

# Acoes_Condicionais class attributes and methods

# arduino_Ligar_Cores_Policia class attributes and methods
arduino_Ligar_Cores_Policia_nome: Property = Property(name="nome", type=StringType)
arduino_Ligar_Cores_Policia.attributes={arduino_Ligar_Cores_Policia_nome}

# Varias_Cores class attributes and methods

# arduino_Ligar_Cores_Arco_Iris class attributes and methods
arduino_Ligar_Cores_Arco_Iris_nome: Property = Property(name="nome", type=StringType)
arduino_Ligar_Cores_Arco_Iris.attributes={arduino_Ligar_Cores_Arco_Iris_nome}

# arduino_Ligar_Azul class attributes and methods
arduino_Ligar_Azul_nome: Property = Property(name="nome", type=StringType)
arduino_Ligar_Azul.attributes={arduino_Ligar_Azul_nome}

# arduino_Bumper_Pressionado class attributes and methods
arduino_Bumper_Pressionado_nome: Property = Property(name="nome", type=StringType)
arduino_Bumper_Pressionado.attributes={arduino_Bumper_Pressionado_nome}

# Unica_Cor class attributes and methods

# Condicao class attributes and methods

# arduino_Distancia_Infra_Vermelhos class attributes and methods
arduino_Distancia_Infra_Vermelhos_distancia: Property = Property(name="distancia", type=IntegerType)
arduino_Distancia_Infra_Vermelhos.attributes={arduino_Distancia_Infra_Vermelhos_distancia}

# arduino_Corpo class attributes and methods
arduino_Corpo_evitarObstaculo: Property = Property(name="evitarObstaculo", type=BooleanType)
arduino_Corpo.attributes={arduino_Corpo_evitarObstaculo}

# arduino_Corpo_Modificavel class attributes and methods
arduino_Corpo_Modificavel_tempo: Property = Property(name="tempo", type=IntegerType)
arduino_Corpo_Modificavel_evitarObstaculo: Property = Property(name="evitarObstaculo", type=BooleanType)
arduino_Corpo_Modificavel.attributes={arduino_Corpo_Modificavel_evitarObstaculo, arduino_Corpo_Modificavel_tempo}

# Acoes_Modificaveis class attributes and methods

# arduino_Cabeca class attributes and methods

# arduino_Cabeca_Modificavel class attributes and methods
arduino_Cabeca_Modificavel_graus: Property = Property(name="graus", type=IntegerType)
arduino_Cabeca_Modificavel.attributes={arduino_Cabeca_Modificavel_graus}

# arduino_Inicio class attributes and methods
arduino_Inicio_nome: Property = Property(name="nome", type=StringType)
arduino_Inicio_evitarObstaculo: Property = Property(name="evitarObstaculo", type=BooleanType)
arduino_Inicio.attributes={arduino_Inicio_evitarObstaculo, arduino_Inicio_nome}

# arduino_Fim class attributes and methods
arduino_Fim_nome: Property = Property(name="nome", type=StringType)
arduino_Fim.attributes={arduino_Fim_nome}

# arduino_Parar class attributes and methods
arduino_Parar_nome: Property = Property(name="nome", type=StringType)
arduino_Parar.attributes={arduino_Parar_nome}

# arduino_If class attributes and methods
arduino_If_nome: Property = Property(name="nome", type=StringType)
arduino_If.attributes={arduino_If_nome}

# arduino_Parar_Tempo class attributes and methods

# Relationships
temAcoes0: BinaryAssociation = BinaryAssociation(
    name="temAcoes0",
    ends={
        Property(name="arduino_Acao", type=arduino_Robo, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Robo", type=arduino_Acao, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
temTransicoes1: BinaryAssociation = BinaryAssociation(
    name="temTransicoes1",
    ends={
        Property(name="arduino_Transicoes", type=arduino_Robo, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Robo2", type=arduino_Transicoes, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
temCondicoes3: BinaryAssociation = BinaryAssociation(
    name="temCondicoes3",
    ends={
        Property(name="arduino_Condicao", type=arduino_Robo, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Robo4", type=arduino_Condicao, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Transicao_de_Entrada5: BinaryAssociation = BinaryAssociation(
    name="Transicao_de_Entrada5",
    ends={
        Property(name="Transicoes", type=arduino_Acao, multiplicity=Multiplicity(1, 1)),
        Property(name="Acao_de_Saida", type=arduino_Transicoes, multiplicity=Multiplicity(0, 1))
    }
)
Transicao_de_Saida6: BinaryAssociation = BinaryAssociation(
    name="Transicao_de_Saida6",
    ends={
        Property(name="Transicoes7", type=arduino_Acao, multiplicity=Multiplicity(1, 1)),
        Property(name="Acao_de_Entrada", type=arduino_Transicoes, multiplicity=Multiplicity(0, 1))
    }
)
Acao_de_Entrada8: BinaryAssociation = BinaryAssociation(
    name="Acao_de_Entrada8",
    ends={
        Property(name="Acao", type=arduino_Transicoes, multiplicity=Multiplicity(1, 1)),
        Property(name="Transicao_de_Saida", type=arduino_Acao, multiplicity=Multiplicity(0, 1))
    }
)
Acao_de_Saida9: BinaryAssociation = BinaryAssociation(
    name="Acao_de_Saida9",
    ends={
        Property(name="Acao10", type=arduino_Transicoes, multiplicity=Multiplicity(1, 1)),
        Property(name="Transicao_de_Entrada", type=arduino_Acao, multiplicity=Multiplicity(0, 1))
    }
)
tem11: BinaryAssociation = BinaryAssociation(
    name="tem11",
    ends={
        Property(name="arduino_Condicao12", type=arduino_Acoes_Condicionais, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Acoes_Condicionais", type=arduino_Condicao, multiplicity=Multiplicity(1, 1))
    }
)
corpo13: BinaryAssociation = BinaryAssociation(
    name="corpo13",
    ends={
        Property(name="arduino_Acao14", type=arduino_While, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_While", type=arduino_Acao, multiplicity=Multiplicity(1, 1))
    }
)
then15: BinaryAssociation = BinaryAssociation(
    name="then15",
    ends={
        Property(name="arduino_Acao16", type=arduino_If, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_If", type=arduino_Acao, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_arduino_Virar_Esquerda_Corpo = Generalization(general=Corpo, specific=arduino_Virar_Esquerda)
gen_arduino_Mover_Frente_Corpo = Generalization(general=Corpo, specific=arduino_Mover_Frente)
gen_arduino_Rodar_Direita_Tempo_Corpo_Modificavel = Generalization(general=Corpo_Modificavel, specific=arduino_Rodar_Direita_Tempo)
gen_arduino_Acoes_Predefinidas_Acao = Generalization(general=Acao, specific=arduino_Acoes_Predefinidas)
gen_arduino_Acoes_Modificaveis_Acao = Generalization(general=Acao, specific=arduino_Acoes_Modificaveis)
gen_arduino_Mover_Frente_Tempo_Corpo_Modificavel = Generalization(general=Corpo_Modificavel, specific=arduino_Mover_Frente_Tempo)
gen_arduino_Mover_Tras_Tempo_Corpo_Modificavel = Generalization(general=Corpo_Modificavel, specific=arduino_Mover_Tras_Tempo)
gen_arduino_Virar_para_X_Graus_Cabeca_Modificavel = Generalization(general=Cabeca_Modificavel, specific=arduino_Virar_para_X_Graus)
gen_arduino_Virar_Max_Drt_Cabeca = Generalization(general=Cabeca, specific=arduino_Virar_Max_Drt)
gen_arduino_Virar_Max_Esq_Cabeca = Generalization(general=Cabeca, specific=arduino_Virar_Max_Esq)
gen_arduino_Centrar_Cabeca = Generalization(general=Cabeca, specific=arduino_Centrar)
gen_arduino_Mover_Tras_Corpo = Generalization(general=Corpo, specific=arduino_Mover_Tras)
gen_arduino_Virar_Direita_Corpo = Generalization(general=Corpo, specific=arduino_Virar_Direita)
gen_arduino_Rodar_Esquerda_Tempo_Corpo_Modificavel = Generalization(general=Corpo_Modificavel, specific=arduino_Rodar_Esquerda_Tempo)
gen_arduino_Mover_Aleatoriamente_Corpo = Generalization(general=Corpo, specific=arduino_Mover_Aleatoriamente)
gen_arduino_LED_Acoes_Predefinidas = Generalization(general=Acoes_Predefinidas, specific=arduino_LED)
gen_arduino_Verde_LED = Generalization(general=LED, specific=arduino_Verde)
gen_arduino_Tricolor_LED = Generalization(general=LED, specific=arduino_Tricolor)
gen_arduino_Ligar_LED_Verde_Verde = Generalization(general=Verde, specific=arduino_Ligar_LED_Verde)
gen_arduino_Desligar_LED_Verde_Verde = Generalization(general=Verde, specific=arduino_Desligar_LED_Verde)
gen_arduino_Ligar_Intermitencia_Verde = Generalization(general=Verde, specific=arduino_Ligar_Intermitencia)
gen_arduino_Desligar_Intermitencia_Verde = Generalization(general=Verde, specific=arduino_Desligar_Intermitencia)
gen_arduino_Varias_Cores_Tricolor = Generalization(general=Tricolor, specific=arduino_Varias_Cores)
gen_arduino_Unica_Cor_Tricolor = Generalization(general=Tricolor, specific=arduino_Unica_Cor)
gen_arduino_Virar_45_Esq_Cabeca = Generalization(general=Cabeca, specific=arduino_Virar_45_Esq)
gen_arduino_Virar_45_Drt_Cabeca = Generalization(general=Cabeca, specific=arduino_Virar_45_Drt)
gen_arduino_Ligar_Azul_Unica_Cor = Generalization(general=Unica_Cor, specific=arduino_Ligar_Azul)
gen_arduino_Ligar_Verde_Unica_Cor = Generalization(general=Unica_Cor, specific=arduino_Ligar_Verde)
gen_arduino_Ligar_Vermelho_Unica_Cor = Generalization(general=Unica_Cor, specific=arduino_Ligar_Vermelho)
gen_arduino_Desligar_Cor_Unica_Cor = Generalization(general=Unica_Cor, specific=arduino_Desligar_Cor)
gen_arduino_Desligar_Cores_Varias_Cores = Generalization(general=Varias_Cores, specific=arduino_Desligar_Cores)
gen_arduino_Acoes_Condicionais_Acao = Generalization(general=Acao, specific=arduino_Acoes_Condicionais)
gen_arduino_While_Acoes_Condicionais = Generalization(general=Acoes_Condicionais, specific=arduino_While)
gen_arduino_Ligar_Cores_Policia_Varias_Cores = Generalization(general=Varias_Cores, specific=arduino_Ligar_Cores_Policia)
gen_arduino_Ligar_Cores_Arco_Iris_Varias_Cores = Generalization(general=Varias_Cores, specific=arduino_Ligar_Cores_Arco_Iris)
gen_arduino_Bumper_Pressionado_Condicao = Generalization(general=Condicao, specific=arduino_Bumper_Pressionado)
gen_arduino_Distancia_Infra_Vermelhos_Condicao = Generalization(general=Condicao, specific=arduino_Distancia_Infra_Vermelhos)
gen_arduino_Corpo_Acoes_Predefinidas = Generalization(general=Acoes_Predefinidas, specific=arduino_Corpo)
gen_arduino_Corpo_Modificavel_Acoes_Modificaveis = Generalization(general=Acoes_Modificaveis, specific=arduino_Corpo_Modificavel)
gen_arduino_Cabeca_Acoes_Predefinidas = Generalization(general=Acoes_Predefinidas, specific=arduino_Cabeca)
gen_arduino_Cabeca_Modificavel_Acoes_Modificaveis = Generalization(general=Acoes_Modificaveis, specific=arduino_Cabeca_Modificavel)
gen_arduino_Inicio_Acao = Generalization(general=Acao, specific=arduino_Inicio)
gen_arduino_Fim_Acao = Generalization(general=Acao, specific=arduino_Fim)
gen_arduino_Parar_Corpo = Generalization(general=Corpo, specific=arduino_Parar)
gen_arduino_If_Acoes_Condicionais = Generalization(general=Acoes_Condicionais, specific=arduino_If)
gen_arduino_Parar_Tempo_Corpo_Modificavel = Generalization(general=Corpo_Modificavel, specific=arduino_Parar_Tempo)

# Domain Model
domain_model = DomainModel(
    name="arduino",
    types={arduino_Acao, arduino_Transicoes, arduino_Condicao, arduino_Virar_Esquerda, Corpo, arduino_Mover_Frente, arduino_Robo, arduino_Rodar_Direita_Tempo, arduino_Acoes_Predefinidas, Acao, arduino_Acoes_Modificaveis, arduino_Mover_Frente_Tempo, arduino_Mover_Tras_Tempo, arduino_Virar_para_X_Graus, Cabeca_Modificavel, arduino_Virar_Max_Drt, Cabeca, arduino_Virar_Max_Esq, arduino_Centrar, arduino_Mover_Tras, arduino_Virar_Direita, arduino_Rodar_Esquerda_Tempo, Corpo_Modificavel, arduino_Mover_Aleatoriamente, arduino_LED, Acoes_Predefinidas, arduino_Verde, LED, arduino_Tricolor, arduino_Ligar_LED_Verde, Verde, arduino_Desligar_LED_Verde, arduino_Ligar_Intermitencia, arduino_Desligar_Intermitencia, arduino_Varias_Cores, Tricolor, arduino_Unica_Cor, arduino_Virar_45_Esq, arduino_Virar_45_Drt, arduino_Ligar_Verde, arduino_Ligar_Vermelho, arduino_Desligar_Cor, arduino_Desligar_Cores, arduino_Acoes_Condicionais, arduino_While, Acoes_Condicionais, arduino_Ligar_Cores_Policia, Varias_Cores, arduino_Ligar_Cores_Arco_Iris, arduino_Ligar_Azul, arduino_Bumper_Pressionado, Unica_Cor, Condicao, arduino_Distancia_Infra_Vermelhos, arduino_Corpo, arduino_Corpo_Modificavel, Acoes_Modificaveis, arduino_Cabeca, arduino_Cabeca_Modificavel, arduino_Inicio, arduino_Fim, arduino_Parar, arduino_If, arduino_Parar_Tempo},
    associations={temAcoes0, temTransicoes1, temCondicoes3, Transicao_de_Entrada5, Transicao_de_Saida6, Acao_de_Entrada8, Acao_de_Saida9, tem11, corpo13, then15},
    generalizations={gen_arduino_Virar_Esquerda_Corpo, gen_arduino_Mover_Frente_Corpo, gen_arduino_Rodar_Direita_Tempo_Corpo_Modificavel, gen_arduino_Acoes_Predefinidas_Acao, gen_arduino_Acoes_Modificaveis_Acao, gen_arduino_Mover_Frente_Tempo_Corpo_Modificavel, gen_arduino_Mover_Tras_Tempo_Corpo_Modificavel, gen_arduino_Virar_para_X_Graus_Cabeca_Modificavel, gen_arduino_Virar_Max_Drt_Cabeca, gen_arduino_Virar_Max_Esq_Cabeca, gen_arduino_Centrar_Cabeca, gen_arduino_Mover_Tras_Corpo, gen_arduino_Virar_Direita_Corpo, gen_arduino_Rodar_Esquerda_Tempo_Corpo_Modificavel, gen_arduino_Mover_Aleatoriamente_Corpo, gen_arduino_LED_Acoes_Predefinidas, gen_arduino_Verde_LED, gen_arduino_Tricolor_LED, gen_arduino_Ligar_LED_Verde_Verde, gen_arduino_Desligar_LED_Verde_Verde, gen_arduino_Ligar_Intermitencia_Verde, gen_arduino_Desligar_Intermitencia_Verde, gen_arduino_Varias_Cores_Tricolor, gen_arduino_Unica_Cor_Tricolor, gen_arduino_Virar_45_Esq_Cabeca, gen_arduino_Virar_45_Drt_Cabeca, gen_arduino_Ligar_Azul_Unica_Cor, gen_arduino_Ligar_Verde_Unica_Cor, gen_arduino_Ligar_Vermelho_Unica_Cor, gen_arduino_Desligar_Cor_Unica_Cor, gen_arduino_Desligar_Cores_Varias_Cores, gen_arduino_Acoes_Condicionais_Acao, gen_arduino_While_Acoes_Condicionais, gen_arduino_Ligar_Cores_Policia_Varias_Cores, gen_arduino_Ligar_Cores_Arco_Iris_Varias_Cores, gen_arduino_Bumper_Pressionado_Condicao, gen_arduino_Distancia_Infra_Vermelhos_Condicao, gen_arduino_Corpo_Acoes_Predefinidas, gen_arduino_Corpo_Modificavel_Acoes_Modificaveis, gen_arduino_Cabeca_Acoes_Predefinidas, gen_arduino_Cabeca_Modificavel_Acoes_Modificaveis, gen_arduino_Inicio_Acao, gen_arduino_Fim_Acao, gen_arduino_Parar_Corpo, gen_arduino_If_Acoes_Condicionais, gen_arduino_Parar_Tempo_Corpo_Modificavel},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)