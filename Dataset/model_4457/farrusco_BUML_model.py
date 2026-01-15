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
TipoDistancia: Enumeration = Enumeration(
    name="TipoDistancia",
    literals={
            EnumerationLiteral(name="Menor"),
			EnumerationLiteral(name="Maior")
    }
)

EstadoDaLuz: Enumeration = Enumeration(
    name="EstadoDaLuz",
    literals={
            EnumerationLiteral(name="Ligado"),
			EnumerationLiteral(name="Desligado")
    }
)

EstadoSucesso: Enumeration = Enumeration(
    name="EstadoSucesso",
    literals={
            EnumerationLiteral(name="Sucesso"),
			EnumerationLiteral(name="Falha"),
			EnumerationLiteral(name="Decorrer")
    }
)

EstadoFalha: Enumeration = Enumeration(
    name="EstadoFalha",
    literals={
            EnumerationLiteral(name="Falha"),
			EnumerationLiteral(name="Sucesso"),
			EnumerationLiteral(name="Decorrer")
    }
)

EstadoDecorrer: Enumeration = Enumeration(
    name="EstadoDecorrer",
    literals={
            EnumerationLiteral(name="Sucesso"),
			EnumerationLiteral(name="Falha"),
			EnumerationLiteral(name="Decorrer")
    }
)

EscolhaBumper: Enumeration = Enumeration(
    name="EscolhaBumper",
    literals={
            EnumerationLiteral(name="Esquerdo"),
			EnumerationLiteral(name="Direito")
    }
)

# Classes
Node = Class(name="Node")
farrusco_Prioridade = Class(name="farrusco::Prioridade")
farrusco_Robot = Class(name="farrusco::Robot")
farrusco_Node = Class(name="farrusco::Node")
farrusco_Filho = Class(name="farrusco::Filho")
farrusco_Irmao = Class(name="farrusco::Irmao")
farrusco_Behavior = Class(name="farrusco::Behavior")
farrusco_Espera = Class(name="farrusco::Espera")
Behavior = Class(name="Behavior")
farrusco_Paralelo = Class(name="farrusco::Paralelo")
farrusco_Sequencial = Class(name="farrusco::Sequencial")
farrusco_AlterarEstado = Class(name="farrusco::AlterarEstado")
farrusco_Action = Class(name="farrusco::Action", is_abstract=True)
farrusco_Condition = Class(name="farrusco::Condition", is_abstract=True)
Action = Class(name="Action")
farrusco_Distancia = Class(name="farrusco::Distancia")
Condition = Class(name="Condition")
farrusco_Bumpers = Class(name="farrusco::Bumpers")
farrusco_Actuate = Class(name="farrusco::Actuate", is_abstract=True)
farrusco_Motor = Class(name="farrusco::Motor")
Actuate = Class(name="Actuate")
farrusco_Servo = Class(name="farrusco::Servo")
farrusco_LED = Class(name="farrusco::LED")

# Node class attributes and methods

# farrusco_Prioridade class attributes and methods
farrusco_Prioridade_Nome: Property = Property(name="Nome", type=StringType)
farrusco_Prioridade.attributes={farrusco_Prioridade_Nome}

# farrusco_Robot class attributes and methods
farrusco_Robot_Nome: Property = Property(name="Nome", type=StringType)
farrusco_Robot.attributes={farrusco_Robot_Nome}

# farrusco_Node class attributes and methods

# farrusco_Filho class attributes and methods

# farrusco_Irmao class attributes and methods

# farrusco_Behavior class attributes and methods

# farrusco_Espera class attributes and methods
farrusco_Espera_Nome: Property = Property(name="Nome", type=StringType)
farrusco_Espera_Tempo: Property = Property(name="Tempo", type=IntegerType)
farrusco_Espera.attributes={farrusco_Espera_Tempo, farrusco_Espera_Nome}

# Behavior class attributes and methods

# farrusco_Paralelo class attributes and methods
farrusco_Paralelo_Nome: Property = Property(name="Nome", type=StringType)
farrusco_Paralelo.attributes={farrusco_Paralelo_Nome}

# farrusco_Sequencial class attributes and methods
farrusco_Sequencial_Nome: Property = Property(name="Nome", type=StringType)
farrusco_Sequencial.attributes={farrusco_Sequencial_Nome}

# farrusco_AlterarEstado class attributes and methods
farrusco_AlterarEstado_Nome: Property = Property(name="Nome", type=StringType)
farrusco_AlterarEstado_Alterar_Sucesso: Property = Property(name="Alterar_Sucesso", type=StringType)
farrusco_AlterarEstado_Alterar_Falha: Property = Property(name="Alterar_Falha", type=StringType)
farrusco_AlterarEstado_Alterar_Decorrer: Property = Property(name="Alterar_Decorrer", type=StringType)
farrusco_AlterarEstado.attributes={farrusco_AlterarEstado_Nome, farrusco_AlterarEstado_Alterar_Falha, farrusco_AlterarEstado_Alterar_Decorrer, farrusco_AlterarEstado_Alterar_Sucesso}

# farrusco_Action class attributes and methods

# farrusco_Condition class attributes and methods

# Action class attributes and methods

# farrusco_Distancia class attributes and methods
farrusco_Distancia_Nome: Property = Property(name="Nome", type=StringType)
farrusco_Distancia_distancia: Property = Property(name="distancia", type=IntegerType)
farrusco_Distancia_Menor_Maior: Property = Property(name="Menor_Maior", type=StringType)
farrusco_Distancia.attributes={farrusco_Distancia_Menor_Maior, farrusco_Distancia_distancia, farrusco_Distancia_Nome}

# Condition class attributes and methods

# farrusco_Bumpers class attributes and methods
farrusco_Bumpers_Nome: Property = Property(name="Nome", type=StringType)
farrusco_Bumpers_Bumper_Esquerdo_ou_Direito: Property = Property(name="Bumper_Esquerdo_ou_Direito", type=StringType)
farrusco_Bumpers.attributes={farrusco_Bumpers_Nome, farrusco_Bumpers_Bumper_Esquerdo_ou_Direito}

# farrusco_Actuate class attributes and methods

# farrusco_Motor class attributes and methods
farrusco_Motor_Nome: Property = Property(name="Nome", type=StringType)
farrusco_Motor_Motor_Esquerdo: Property = Property(name="Motor_Esquerdo", type=IntegerType)
farrusco_Motor_Motor_Direito: Property = Property(name="Motor_Direito", type=IntegerType)
farrusco_Motor.attributes={farrusco_Motor_Motor_Esquerdo, farrusco_Motor_Motor_Direito, farrusco_Motor_Nome}

# Actuate class attributes and methods

# farrusco_Servo class attributes and methods
farrusco_Servo_Nome: Property = Property(name="Nome", type=StringType)
farrusco_Servo_Posicao_Minima: Property = Property(name="Posicao_Minima", type=IntegerType)
farrusco_Servo_Posicao_Maxima: Property = Property(name="Posicao_Maxima", type=IntegerType)
farrusco_Servo_Passo_a_Passo: Property = Property(name="Passo_a_Passo", type=IntegerType)
farrusco_Servo.attributes={farrusco_Servo_Nome, farrusco_Servo_Posicao_Maxima, farrusco_Servo_Passo_a_Passo, farrusco_Servo_Posicao_Minima}

# farrusco_LED class attributes and methods
farrusco_LED_Nome: Property = Property(name="Nome", type=StringType)
farrusco_LED_Ligado_ou_Desligado: Property = Property(name="Ligado_ou_Desligado", type=StringType)
farrusco_LED.attributes={farrusco_LED_Ligado_ou_Desligado, farrusco_LED_Nome}

# Relationships
source10: BinaryAssociation = BinaryAssociation(
    name="source10",
    ends={
        Property(name="farrusco_Node12", type=farrusco_Irmao, multiplicity=Multiplicity(1, 1)),
        Property(name="farrusco_Irmao11", type=farrusco_Node, multiplicity=Multiplicity(0, 9999))
    }
)
target13: BinaryAssociation = BinaryAssociation(
    name="target13",
    ends={
        Property(name="farrusco_Node15", type=farrusco_Irmao, multiplicity=Multiplicity(1, 1)),
        Property(name="farrusco_Irmao14", type=farrusco_Node, multiplicity=Multiplicity(0, 9999))
    }
)
nodes0: BinaryAssociation = BinaryAssociation(
    name="nodes0",
    ends={
        Property(name="farrusco_Node", type=farrusco_Robot, multiplicity=Multiplicity(1, 1)),
        Property(name="farrusco_Robot", type=farrusco_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
child1: BinaryAssociation = BinaryAssociation(
    name="child1",
    ends={
        Property(name="farrusco_Filho", type=farrusco_Robot, multiplicity=Multiplicity(1, 1)),
        Property(name="farrusco_Robot2", type=farrusco_Filho, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
next3: BinaryAssociation = BinaryAssociation(
    name="next3",
    ends={
        Property(name="farrusco_Irmao", type=farrusco_Robot, multiplicity=Multiplicity(1, 1)),
        Property(name="farrusco_Robot4", type=farrusco_Irmao, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source5: BinaryAssociation = BinaryAssociation(
    name="source5",
    ends={
        Property(name="farrusco_Behavior", type=farrusco_Filho, multiplicity=Multiplicity(1, 1)),
        Property(name="farrusco_Filho6", type=farrusco_Behavior, multiplicity=Multiplicity(0, 9999))
    }
)
target7: BinaryAssociation = BinaryAssociation(
    name="target7",
    ends={
        Property(name="farrusco_Node9", type=farrusco_Filho, multiplicity=Multiplicity(1, 1)),
        Property(name="farrusco_Filho8", type=farrusco_Node, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_farrusco_Behavior_Node = Generalization(general=Node, specific=farrusco_Behavior)
gen_farrusco_Espera_Condition = Generalization(general=Condition, specific=farrusco_Espera)
gen_farrusco_Prioridade_Behavior = Generalization(general=Behavior, specific=farrusco_Prioridade)
gen_farrusco_Paralelo_Behavior = Generalization(general=Behavior, specific=farrusco_Paralelo)
gen_farrusco_Sequencial_Behavior = Generalization(general=Behavior, specific=farrusco_Sequencial)
gen_farrusco_AlterarEstado_Behavior = Generalization(general=Behavior, specific=farrusco_AlterarEstado)
gen_farrusco_Action_Node = Generalization(general=Node, specific=farrusco_Action)
gen_farrusco_Condition_Action = Generalization(general=Action, specific=farrusco_Condition)
gen_farrusco_Distancia_Condition = Generalization(general=Condition, specific=farrusco_Distancia)
gen_farrusco_Bumpers_Condition = Generalization(general=Condition, specific=farrusco_Bumpers)
gen_farrusco_Actuate_Action = Generalization(general=Action, specific=farrusco_Actuate)
gen_farrusco_Motor_Actuate = Generalization(general=Actuate, specific=farrusco_Motor)
gen_farrusco_Servo_Actuate = Generalization(general=Actuate, specific=farrusco_Servo)
gen_farrusco_LED_Actuate = Generalization(general=Actuate, specific=farrusco_LED)

# Domain Model
domain_model = DomainModel(
    name="farrusco",
    types={Node, farrusco_Prioridade, farrusco_Robot, farrusco_Node, farrusco_Filho, farrusco_Irmao, farrusco_Behavior, farrusco_Espera, Behavior, farrusco_Paralelo, farrusco_Sequencial, farrusco_AlterarEstado, farrusco_Action, farrusco_Condition, Action, farrusco_Distancia, Condition, farrusco_Bumpers, farrusco_Actuate, farrusco_Motor, Actuate, farrusco_Servo, farrusco_LED, TipoDistancia, EstadoDaLuz, EstadoSucesso, EstadoFalha, EstadoDecorrer, EscolhaBumper},
    associations={source10, target13, nodes0, child1, next3, source5, target7},
    generalizations={gen_farrusco_Behavior_Node, gen_farrusco_Espera_Condition, gen_farrusco_Prioridade_Behavior, gen_farrusco_Paralelo_Behavior, gen_farrusco_Sequencial_Behavior, gen_farrusco_AlterarEstado_Behavior, gen_farrusco_Action_Node, gen_farrusco_Condition_Action, gen_farrusco_Distancia_Condition, gen_farrusco_Bumpers_Condition, gen_farrusco_Actuate_Action, gen_farrusco_Motor_Actuate, gen_farrusco_Servo_Actuate, gen_farrusco_LED_Actuate},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)