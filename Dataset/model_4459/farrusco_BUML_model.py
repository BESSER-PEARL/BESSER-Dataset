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
farrusco_Action = Class(name="farrusco_Action", is_abstract=True)
Node = Class(name="Node")
farrusco_Robot = Class(name="farrusco_Robot")
farrusco_Node = Class(name="farrusco_Node")
farrusco_ActionChild = Class(name="farrusco_ActionChild")
farrusco_Child = Class(name="farrusco_Child")
farrusco_Next = Class(name="farrusco_Next")
farrusco_Behavior = Class(name="farrusco_Behavior", is_abstract=True)
farrusco_Condition = Class(name="farrusco_Condition", is_abstract=True)
Action = Class(name="Action")
farrusco_IRdist = Class(name="farrusco_IRdist")
Condition = Class(name="Condition")
farrusco_Prior = Class(name="farrusco_Prior")
Behavior = Class(name="Behavior")
farrusco_Paralell = Class(name="farrusco_Paralell")
farrusco_Sequential = Class(name="farrusco_Sequential")
farrusco_StateOverride = Class(name="farrusco_StateOverride")
farrusco_LED = Class(name="farrusco_LED")
farrusco_RightBumper = Class(name="farrusco_RightBumper")
farrusco_LeftBumper = Class(name="farrusco_LeftBumper")
farrusco_Wait = Class(name="farrusco_Wait")
farrusco_Actuate = Class(name="farrusco_Actuate", is_abstract=True)
farrusco_Motors = Class(name="farrusco_Motors")
Actuate = Class(name="Actuate")
farrusco_ServoRange = Class(name="farrusco_ServoRange")

# farrusco_Action class attributes and methods
farrusco_Action_name: Property = Property(name="name", type=StringType)
farrusco_Action.attributes={farrusco_Action_name}

# Node class attributes and methods

# farrusco_Robot class attributes and methods
farrusco_Robot_Name: Property = Property(name="Name", type=StringType)
farrusco_Robot.attributes={farrusco_Robot_Name}

# farrusco_Node class attributes and methods

# farrusco_ActionChild class attributes and methods

# farrusco_Child class attributes and methods

# farrusco_Next class attributes and methods

# farrusco_Behavior class attributes and methods
farrusco_Behavior_Name: Property = Property(name="Name", type=StringType)
farrusco_Behavior.attributes={farrusco_Behavior_Name}

# farrusco_Condition class attributes and methods

# Action class attributes and methods

# farrusco_IRdist class attributes and methods
farrusco_IRdist_distancia: Property = Property(name="distancia", type=IntegerType)
farrusco_IRdist_how_sucess: Property = Property(name="how_sucess", type=BooleanType)
farrusco_IRdist.attributes={farrusco_IRdist_how_sucess, farrusco_IRdist_distancia}

# Condition class attributes and methods

# farrusco_Prior class attributes and methods

# Behavior class attributes and methods

# farrusco_Paralell class attributes and methods

# farrusco_Sequential class attributes and methods

# farrusco_StateOverride class attributes and methods
farrusco_StateOverride_fail_policy: Property = Property(name="fail_policy", type=IntegerType)
farrusco_StateOverride_runn_policy: Property = Property(name="runn_policy", type=IntegerType)
farrusco_StateOverride_succ_policy: Property = Property(name="succ_policy", type=IntegerType)
farrusco_StateOverride.attributes={farrusco_StateOverride_runn_policy, farrusco_StateOverride_fail_policy, farrusco_StateOverride_succ_policy}

# farrusco_LED class attributes and methods
farrusco_LED_on_off: Property = Property(name="on_off", type=BooleanType)
farrusco_LED.attributes={farrusco_LED_on_off}

# farrusco_RightBumper class attributes and methods

# farrusco_LeftBumper class attributes and methods

# farrusco_Wait class attributes and methods
farrusco_Wait_time: Property = Property(name="time", type=IntegerType)
farrusco_Wait.attributes={farrusco_Wait_time}

# farrusco_Actuate class attributes and methods

# farrusco_Motors class attributes and methods
farrusco_Motors_MotorLeft: Property = Property(name="MotorLeft", type=IntegerType)
farrusco_Motors_MotorRight: Property = Property(name="MotorRight", type=IntegerType)
farrusco_Motors.attributes={farrusco_Motors_MotorRight, farrusco_Motors_MotorLeft}

# Actuate class attributes and methods

# farrusco_ServoRange class attributes and methods
farrusco_ServoRange_max: Property = Property(name="max", type=IntegerType)
farrusco_ServoRange_inc: Property = Property(name="inc", type=IntegerType)
farrusco_ServoRange_min: Property = Property(name="min", type=IntegerType)
farrusco_ServoRange.attributes={farrusco_ServoRange_max, farrusco_ServoRange_min, farrusco_ServoRange_inc}

# Relationships
source12: BinaryAssociation = BinaryAssociation(
    name="source12",
    ends={
        Property(name="farrusco_Node14", type=farrusco_Next, multiplicity=Multiplicity(1, 1)),
        Property(name="farrusco_Next13", type=farrusco_Node, multiplicity=Multiplicity(0, 9999))
    }
)
target15: BinaryAssociation = BinaryAssociation(
    name="target15",
    ends={
        Property(name="farrusco_Node17", type=farrusco_Next, multiplicity=Multiplicity(1, 1)),
        Property(name="farrusco_Next16", type=farrusco_Node, multiplicity=Multiplicity(0, 9999))
    }
)
source18: BinaryAssociation = BinaryAssociation(
    name="source18",
    ends={
        Property(name="farrusco_Behavior20", type=farrusco_ActionChild, multiplicity=Multiplicity(1, 1)),
        Property(name="farrusco_ActionChild19", type=farrusco_Behavior, multiplicity=Multiplicity(0, 1))
    }
)
target21: BinaryAssociation = BinaryAssociation(
    name="target21",
    ends={
        Property(name="farrusco_Action", type=farrusco_ActionChild, multiplicity=Multiplicity(1, 1)),
        Property(name="farrusco_ActionChild22", type=farrusco_Action, multiplicity=Multiplicity(0, 9999))
    }
)
nodes0: BinaryAssociation = BinaryAssociation(
    name="nodes0",
    ends={
        Property(name="farrusco_Node", type=farrusco_Robot, multiplicity=Multiplicity(1, 1)),
        Property(name="farrusco_Robot", type=farrusco_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actionChild1: BinaryAssociation = BinaryAssociation(
    name="actionChild1",
    ends={
        Property(name="farrusco_ActionChild", type=farrusco_Robot, multiplicity=Multiplicity(1, 1)),
        Property(name="farrusco_Robot2", type=farrusco_ActionChild, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
child3: BinaryAssociation = BinaryAssociation(
    name="child3",
    ends={
        Property(name="farrusco_Child", type=farrusco_Robot, multiplicity=Multiplicity(1, 1)),
        Property(name="farrusco_Robot4", type=farrusco_Child, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
next5: BinaryAssociation = BinaryAssociation(
    name="next5",
    ends={
        Property(name="farrusco_Next", type=farrusco_Robot, multiplicity=Multiplicity(1, 1)),
        Property(name="farrusco_Robot6", type=farrusco_Next, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source7: BinaryAssociation = BinaryAssociation(
    name="source7",
    ends={
        Property(name="farrusco_Behavior", type=farrusco_Child, multiplicity=Multiplicity(1, 1)),
        Property(name="farrusco_Child8", type=farrusco_Behavior, multiplicity=Multiplicity(0, 9999))
    }
)
target9: BinaryAssociation = BinaryAssociation(
    name="target9",
    ends={
        Property(name="farrusco_Behavior11", type=farrusco_Child, multiplicity=Multiplicity(1, 1)),
        Property(name="farrusco_Child10", type=farrusco_Behavior, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_farrusco_Action_Node = Generalization(general=Node, specific=farrusco_Action)
gen_farrusco_Condition_Action = Generalization(general=Action, specific=farrusco_Condition)
gen_farrusco_IRdist_Condition = Generalization(general=Condition, specific=farrusco_IRdist)
gen_farrusco_Behavior_Node = Generalization(general=Node, specific=farrusco_Behavior)
gen_farrusco_Prior_Behavior = Generalization(general=Behavior, specific=farrusco_Prior)
gen_farrusco_Paralell_Behavior = Generalization(general=Behavior, specific=farrusco_Paralell)
gen_farrusco_Sequential_Behavior = Generalization(general=Behavior, specific=farrusco_Sequential)
gen_farrusco_StateOverride_Behavior = Generalization(general=Behavior, specific=farrusco_StateOverride)
gen_farrusco_LED_Actuate = Generalization(general=Actuate, specific=farrusco_LED)
gen_farrusco_RightBumper_Condition = Generalization(general=Condition, specific=farrusco_RightBumper)
gen_farrusco_LeftBumper_Condition = Generalization(general=Condition, specific=farrusco_LeftBumper)
gen_farrusco_Wait_Condition = Generalization(general=Condition, specific=farrusco_Wait)
gen_farrusco_Actuate_Action = Generalization(general=Action, specific=farrusco_Actuate)
gen_farrusco_Motors_Actuate = Generalization(general=Actuate, specific=farrusco_Motors)
gen_farrusco_ServoRange_Actuate = Generalization(general=Actuate, specific=farrusco_ServoRange)

# Domain Model
domain_model = DomainModel(
    name="farrusco",
    types={farrusco_Action, Node, farrusco_Robot, farrusco_Node, farrusco_ActionChild, farrusco_Child, farrusco_Next, farrusco_Behavior, farrusco_Condition, Action, farrusco_IRdist, Condition, farrusco_Prior, Behavior, farrusco_Paralell, farrusco_Sequential, farrusco_StateOverride, farrusco_LED, farrusco_RightBumper, farrusco_LeftBumper, farrusco_Wait, farrusco_Actuate, farrusco_Motors, Actuate, farrusco_ServoRange},
    associations={source12, target15, source18, target21, nodes0, actionChild1, child3, next5, source7, target9},
    generalizations={gen_farrusco_Action_Node, gen_farrusco_Condition_Action, gen_farrusco_IRdist_Condition, gen_farrusco_Behavior_Node, gen_farrusco_Prior_Behavior, gen_farrusco_Paralell_Behavior, gen_farrusco_Sequential_Behavior, gen_farrusco_StateOverride_Behavior, gen_farrusco_LED_Actuate, gen_farrusco_RightBumper_Condition, gen_farrusco_LeftBumper_Condition, gen_farrusco_Wait_Condition, gen_farrusco_Actuate_Action, gen_farrusco_Motors_Actuate, gen_farrusco_ServoRange_Actuate},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)