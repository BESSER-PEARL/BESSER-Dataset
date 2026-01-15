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
farrusco_Robot = Class(name="farrusco::Robot")
farrusco_Node = Class(name="farrusco::Node")
farrusco_Filho = Class(name="farrusco::Filho")
farrusco_Irmao = Class(name="farrusco::Irmao")
farrusco_Behavior = Class(name="farrusco::Behavior", is_abstract=True)
farrusco_Prioridade = Class(name="farrusco::Prioridade")
Behavior = Class(name="Behavior")
farrusco_Paralelo = Class(name="farrusco::Paralelo")
farrusco_AlterarEstado = Class(name="farrusco::AlterarEstado")
farrusco_Action = Class(name="farrusco::Action", is_abstract=True)
farrusco_Condition = Class(name="farrusco::Condition", is_abstract=True)
Action = Class(name="Action")
farrusco_Distancia = Class(name="farrusco::Distancia")
Condition = Class(name="Condition")
farrusco_BumperDireito = Class(name="farrusco::BumperDireito")
farrusco_BumperEsquerdo = Class(name="farrusco::BumperEsquerdo")
farrusco_Espera = Class(name="farrusco::Espera")
Node = Class(name="Node")
farrusco_Servo = Class(name="farrusco::Servo")
farrusco_LED = Class(name="farrusco::LED")
farrusco_Actuate = Class(name="farrusco::Actuate", is_abstract=True)
farrusco_Motor = Class(name="farrusco::Motor")
Actuate = Class(name="Actuate")

# farrusco_Robot class attributes and methods
farrusco_Robot_Name: Property = Property(name="Name", type=StringType)
farrusco_Robot.attributes={farrusco_Robot_Name}

# farrusco_Node class attributes and methods

# farrusco_Filho class attributes and methods

# farrusco_Irmao class attributes and methods

# farrusco_Behavior class attributes and methods
farrusco_Behavior_Name: Property = Property(name="Name", type=StringType)
farrusco_Behavior.attributes={farrusco_Behavior_Name}

# farrusco_Prioridade class attributes and methods

# Behavior class attributes and methods

# farrusco_Paralelo class attributes and methods

# farrusco_AlterarEstado class attributes and methods
farrusco_AlterarEstado_succ_policy: Property = Property(name="succ_policy", type=IntegerType)
farrusco_AlterarEstado_fail_policy: Property = Property(name="fail_policy", type=IntegerType)
farrusco_AlterarEstado_runn_policy: Property = Property(name="runn_policy", type=IntegerType)
farrusco_AlterarEstado.attributes={farrusco_AlterarEstado_succ_policy, farrusco_AlterarEstado_runn_policy, farrusco_AlterarEstado_fail_policy}

# farrusco_Action class attributes and methods
farrusco_Action_name: Property = Property(name="name", type=StringType)
farrusco_Action.attributes={farrusco_Action_name}

# farrusco_Condition class attributes and methods

# Action class attributes and methods

# farrusco_Distancia class attributes and methods
farrusco_Distancia_distancia: Property = Property(name="distancia", type=IntegerType)
farrusco_Distancia_how_sucess: Property = Property(name="how_sucess", type=BooleanType)
farrusco_Distancia.attributes={farrusco_Distancia_distancia, farrusco_Distancia_how_sucess}

# Condition class attributes and methods

# farrusco_BumperDireito class attributes and methods

# farrusco_BumperEsquerdo class attributes and methods

# farrusco_Espera class attributes and methods
farrusco_Espera_time: Property = Property(name="time", type=IntegerType)
farrusco_Espera.attributes={farrusco_Espera_time}

# Node class attributes and methods

# farrusco_Servo class attributes and methods
farrusco_Servo_min: Property = Property(name="min", type=IntegerType)
farrusco_Servo_max: Property = Property(name="max", type=IntegerType)
farrusco_Servo_inc: Property = Property(name="inc", type=IntegerType)
farrusco_Servo.attributes={farrusco_Servo_min, farrusco_Servo_inc, farrusco_Servo_max}

# farrusco_LED class attributes and methods
farrusco_LED_on_off: Property = Property(name="on_off", type=BooleanType)
farrusco_LED.attributes={farrusco_LED_on_off}

# farrusco_Actuate class attributes and methods

# farrusco_Motor class attributes and methods
farrusco_Motor_MotorRight: Property = Property(name="MotorRight", type=IntegerType)
farrusco_Motor_MotorLeft: Property = Property(name="MotorLeft", type=IntegerType)
farrusco_Motor.attributes={farrusco_Motor_MotorRight, farrusco_Motor_MotorLeft}

# Actuate class attributes and methods

# Relationships
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

# Generalizations
gen_farrusco_Prioridade_Behavior = Generalization(general=Behavior, specific=farrusco_Prioridade)
gen_farrusco_Paralelo_Behavior = Generalization(general=Behavior, specific=farrusco_Paralelo)
gen_farrusco_AlterarEstado_Behavior = Generalization(general=Behavior, specific=farrusco_AlterarEstado)
gen_farrusco_Action_Node = Generalization(general=Node, specific=farrusco_Action)
gen_farrusco_Condition_Action = Generalization(general=Action, specific=farrusco_Condition)
gen_farrusco_Distancia_Condition = Generalization(general=Condition, specific=farrusco_Distancia)
gen_farrusco_BumperDireito_Condition = Generalization(general=Condition, specific=farrusco_BumperDireito)
gen_farrusco_BumperEsquerdo_Condition = Generalization(general=Condition, specific=farrusco_BumperEsquerdo)
gen_farrusco_Espera_Condition = Generalization(general=Condition, specific=farrusco_Espera)
gen_farrusco_Behavior_Node = Generalization(general=Node, specific=farrusco_Behavior)
gen_farrusco_Servo_Actuate = Generalization(general=Actuate, specific=farrusco_Servo)
gen_farrusco_LED_Actuate = Generalization(general=Actuate, specific=farrusco_LED)
gen_farrusco_Actuate_Action = Generalization(general=Action, specific=farrusco_Actuate)
gen_farrusco_Motor_Actuate = Generalization(general=Actuate, specific=farrusco_Motor)

# Domain Model
domain_model = DomainModel(
    name="farrusco",
    types={farrusco_Robot, farrusco_Node, farrusco_Filho, farrusco_Irmao, farrusco_Behavior, farrusco_Prioridade, Behavior, farrusco_Paralelo, farrusco_AlterarEstado, farrusco_Action, farrusco_Condition, Action, farrusco_Distancia, Condition, farrusco_BumperDireito, farrusco_BumperEsquerdo, farrusco_Espera, Node, farrusco_Servo, farrusco_LED, farrusco_Actuate, farrusco_Motor, Actuate},
    associations={nodes0, child1, next3, source5, target7, source10, target13},
    generalizations={gen_farrusco_Prioridade_Behavior, gen_farrusco_Paralelo_Behavior, gen_farrusco_AlterarEstado_Behavior, gen_farrusco_Action_Node, gen_farrusco_Condition_Action, gen_farrusco_Distancia_Condition, gen_farrusco_BumperDireito_Condition, gen_farrusco_BumperEsquerdo_Condition, gen_farrusco_Espera_Condition, gen_farrusco_Behavior_Node, gen_farrusco_Servo_Actuate, gen_farrusco_LED_Actuate, gen_farrusco_Actuate_Action, gen_farrusco_Motor_Actuate},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)