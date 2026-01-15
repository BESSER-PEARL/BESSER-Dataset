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
metamodel_Robot = Class(name="metamodel::Robot")
metamodel_Behaviour = Class(name="metamodel::Behaviour")
metamodel_Sensor = Class(name="metamodel::Sensor", is_abstract=True)
metamodel_Actuator = Class(name="metamodel::Actuator", is_abstract=True)
metamodel_Action = Class(name="metamodel::Action", is_abstract=True)
metamodel_DifferentialWheel = Class(name="metamodel::DifferentialWheel")
Actuator = Class(name="Actuator")
metamodel_Group = Class(name="metamodel::Group")
metamodel_ActionWheel = Class(name="metamodel::ActionWheel", is_abstract=True)
Action = Class(name="Action")
metamodel_TurnLeft = Class(name="metamodel::TurnLeft")
ActionWheel = Class(name="ActionWheel")
metamodel_Forward = Class(name="metamodel::Forward")
metamodel_Stopping = Class(name="metamodel::Stopping")
metamodel_Backward = Class(name="metamodel::Backward")
metamodel_TurnRight = Class(name="metamodel::TurnRight")
metamodel_DistanceSensor = Class(name="metamodel::DistanceSensor")
Sensor = Class(name="Sensor")
metamodel_LightSensor = Class(name="metamodel::LightSensor")
metamodel_Value = Class(name="metamodel::Value")
metamodel_Type = Class(name="metamodel::Type", is_abstract=True)
metamodel_BoolVal = Class(name="metamodel::BoolVal")
Type = Class(name="Type")
metamodel_FloatVal = Class(name="metamodel::FloatVal")
metamodel_IntVal = Class(name="metamodel::IntVal")
metamodel_StateMachine = Class(name="metamodel::StateMachine")
metamodel_State = Class(name="metamodel::State")
metamodel_Transition = Class(name="metamodel::Transition")
metamodel_UnaryOperator = Class(name="metamodel::UnaryOperator", is_abstract=True)
Operator = Class(name="Operator")
metamodel_BinaryOperator = Class(name="metamodel::BinaryOperator", is_abstract=True)
metamodel_Operator = Class(name="metamodel::Operator", is_abstract=True)
metamodel_BinaryCond = Class(name="metamodel::BinaryCond", is_abstract=True)
Condition = Class(name="Condition")
metamodel_Or = Class(name="metamodel::Or")
BinaryCond = Class(name="BinaryCond")
metamodel_And = Class(name="metamodel::And")
metamodel_UnaryCond = Class(name="metamodel::UnaryCond", is_abstract=True)
metamodel_Negation = Class(name="metamodel::Negation")
UnaryCond = Class(name="UnaryCond")
metamodel_Equal = Class(name="metamodel::Equal")
BinaryOperator = Class(name="BinaryOperator")
metamodel_Less = Class(name="metamodel::Less")
metamodel_More = Class(name="metamodel::More")
metamodel_Different = Class(name="metamodel::Different")
metamodel_LessOrEqual = Class(name="metamodel::LessOrEqual")
metamodel_MoreOrEqual = Class(name="metamodel::MoreOrEqual")
metamodel_Add = Class(name="metamodel::Add")
metamodel_Sub = Class(name="metamodel::Sub")
metamodel_Negative = Class(name="metamodel::Negative")
UnaryOperator = Class(name="UnaryOperator")
metamodel_Positive = Class(name="metamodel::Positive")
metamodel_Condition = Class(name="metamodel::Condition", is_abstract=True)

# metamodel_Robot class attributes and methods
metamodel_Robot_name: Property = Property(name="name", type=StringType)
metamodel_Robot.attributes={metamodel_Robot_name}

# metamodel_Behaviour class attributes and methods
metamodel_Behaviour_name: Property = Property(name="name", type=StringType)
metamodel_Behaviour_priority: Property = Property(name="priority", type=IntegerType)
metamodel_Behaviour.attributes={metamodel_Behaviour_priority, metamodel_Behaviour_name}

# metamodel_Sensor class attributes and methods
metamodel_Sensor_name: Property = Property(name="name", type=StringType)
metamodel_Sensor_sensorName: Property = Property(name="sensorName", type=StringType)
metamodel_Sensor.attributes={metamodel_Sensor_name, metamodel_Sensor_sensorName}

# metamodel_Actuator class attributes and methods
metamodel_Actuator_name: Property = Property(name="name", type=StringType)
metamodel_Actuator.attributes={metamodel_Actuator_name}

# metamodel_Action class attributes and methods

# metamodel_DifferentialWheel class attributes and methods
metamodel_DifferentialWheel_isLeft: Property = Property(name="isLeft", type=BooleanType)
metamodel_DifferentialWheel_speed: Property = Property(name="speed", type=IntegerType)
metamodel_DifferentialWheel.attributes={metamodel_DifferentialWheel_speed, metamodel_DifferentialWheel_isLeft}

# Actuator class attributes and methods

# metamodel_Group class attributes and methods

# metamodel_ActionWheel class attributes and methods
metamodel_ActionWheel_speed: Property = Property(name="speed", type=IntegerType)
metamodel_ActionWheel.attributes={metamodel_ActionWheel_speed}

# Action class attributes and methods

# metamodel_TurnLeft class attributes and methods

# ActionWheel class attributes and methods

# metamodel_Forward class attributes and methods

# metamodel_Stopping class attributes and methods

# metamodel_Backward class attributes and methods

# metamodel_TurnRight class attributes and methods

# metamodel_DistanceSensor class attributes and methods

# Sensor class attributes and methods

# metamodel_LightSensor class attributes and methods

# metamodel_Value class attributes and methods
metamodel_Value_name: Property = Property(name="name", type=StringType)
metamodel_Value.attributes={metamodel_Value_name}

# metamodel_Type class attributes and methods

# metamodel_BoolVal class attributes and methods
metamodel_BoolVal_value: Property = Property(name="value", type=BooleanType)
metamodel_BoolVal.attributes={metamodel_BoolVal_value}

# Type class attributes and methods

# metamodel_FloatVal class attributes and methods
metamodel_FloatVal_value: Property = Property(name="value", type=FloatType)
metamodel_FloatVal.attributes={metamodel_FloatVal_value}

# metamodel_IntVal class attributes and methods
metamodel_IntVal_value: Property = Property(name="value", type=IntegerType)
metamodel_IntVal.attributes={metamodel_IntVal_value}

# metamodel_StateMachine class attributes and methods
metamodel_StateMachine_name: Property = Property(name="name", type=StringType)
metamodel_StateMachine.attributes={metamodel_StateMachine_name}

# metamodel_State class attributes and methods
metamodel_State_name: Property = Property(name="name", type=StringType)
metamodel_State_isInitial: Property = Property(name="isInitial", type=BooleanType)
metamodel_State_uid: Property = Property(name="uid", type=IntegerType)
metamodel_State.attributes={metamodel_State_uid, metamodel_State_isInitial, metamodel_State_name}

# metamodel_Transition class attributes and methods
metamodel_Transition_nameIn: Property = Property(name="nameIn", type=StringType)
metamodel_Transition.attributes={metamodel_Transition_nameIn}

# metamodel_UnaryOperator class attributes and methods

# Operator class attributes and methods

# metamodel_BinaryOperator class attributes and methods

# metamodel_Operator class attributes and methods

# metamodel_BinaryCond class attributes and methods

# Condition class attributes and methods

# metamodel_Or class attributes and methods

# BinaryCond class attributes and methods

# metamodel_And class attributes and methods

# metamodel_UnaryCond class attributes and methods

# metamodel_Negation class attributes and methods

# UnaryCond class attributes and methods

# metamodel_Equal class attributes and methods

# BinaryOperator class attributes and methods

# metamodel_Less class attributes and methods

# metamodel_More class attributes and methods

# metamodel_Different class attributes and methods

# metamodel_LessOrEqual class attributes and methods

# metamodel_MoreOrEqual class attributes and methods

# metamodel_Add class attributes and methods

# metamodel_Sub class attributes and methods

# metamodel_Negative class attributes and methods

# UnaryOperator class attributes and methods

# metamodel_Positive class attributes and methods

# metamodel_Condition class attributes and methods

# Relationships
behaviours0: BinaryAssociation = BinaryAssociation(
    name="behaviours0",
    ends={
        Property(name="metamodel_Behaviour", type=metamodel_Robot, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel_Robot", type=metamodel_Behaviour, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sensors1: BinaryAssociation = BinaryAssociation(
    name="sensors1",
    ends={
        Property(name="metamodel_Sensor", type=metamodel_Robot, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel_Robot2", type=metamodel_Sensor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actuators3: BinaryAssociation = BinaryAssociation(
    name="actuators3",
    ends={
        Property(name="metamodel_Actuator", type=metamodel_Robot, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel_Robot4", type=metamodel_Actuator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actions5: BinaryAssociation = BinaryAssociation(
    name="actions5",
    ends={
        Property(name="metamodel_Action", type=metamodel_Robot, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel_Robot6", type=metamodel_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
wheels7: BinaryAssociation = BinaryAssociation(
    name="wheels7",
    ends={
        Property(name="metamodel_DifferentialWheel", type=metamodel_Group, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel_Group", type=metamodel_DifferentialWheel, multiplicity=Multiplicity(2, 2))
    }
)
group8: BinaryAssociation = BinaryAssociation(
    name="group8",
    ends={
        Property(name="metamodel_Group9", type=metamodel_ActionWheel, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel_ActionWheel", type=metamodel_Group, multiplicity=Multiplicity(1, 1))
    }
)
value10: BinaryAssociation = BinaryAssociation(
    name="value10",
    ends={
        Property(name="metamodel_Value", type=metamodel_Sensor, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel_Sensor11", type=metamodel_Value, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value12: BinaryAssociation = BinaryAssociation(
    name="value12",
    ends={
        Property(name="metamodel_Type", type=metamodel_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel_Value13", type=metamodel_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
stateMachine14: BinaryAssociation = BinaryAssociation(
    name="stateMachine14",
    ends={
        Property(name="metamodel_StateMachine", type=metamodel_Behaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel_Behaviour15", type=metamodel_StateMachine, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
states16: BinaryAssociation = BinaryAssociation(
    name="states16",
    ends={
        Property(name="metamodel_State", type=metamodel_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel_StateMachine17", type=metamodel_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constants18: BinaryAssociation = BinaryAssociation(
    name="constants18",
    ends={
        Property(name="metamodel_Value20", type=metamodel_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel_StateMachine19", type=metamodel_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions21: BinaryAssociation = BinaryAssociation(
    name="transitions21",
    ends={
        Property(name="metamodel_Transition", type=metamodel_State, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel_State22", type=metamodel_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
workingAction23: BinaryAssociation = BinaryAssociation(
    name="workingAction23",
    ends={
        Property(name="metamodel_Action25", type=metamodel_State, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel_State24", type=metamodel_Action, multiplicity=Multiplicity(0, 1))
    }
)
onEnterAction26: BinaryAssociation = BinaryAssociation(
    name="onEnterAction26",
    ends={
        Property(name="metamodel_Action28", type=metamodel_State, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel_State27", type=metamodel_Action, multiplicity=Multiplicity(0, 1))
    }
)
onLeaveAction29: BinaryAssociation = BinaryAssociation(
    name="onLeaveAction29",
    ends={
        Property(name="metamodel_Action31", type=metamodel_State, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel_State30", type=metamodel_Action, multiplicity=Multiplicity(0, 1))
    }
)
dstId32: BinaryAssociation = BinaryAssociation(
    name="dstId32",
    ends={
        Property(name="metamodel_State34", type=metamodel_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel_Transition33", type=metamodel_State, multiplicity=Multiplicity(1, 1))
    }
)
valeur37: BinaryAssociation = BinaryAssociation(
    name="valeur37",
    ends={
        Property(name="metamodel_Value38", type=metamodel_UnaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel_UnaryOperator", type=metamodel_Value, multiplicity=Multiplicity(1, 1))
    }
)
operandLeft39: BinaryAssociation = BinaryAssociation(
    name="operandLeft39",
    ends={
        Property(name="metamodel_Operator", type=metamodel_BinaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel_BinaryOperator", type=metamodel_Operator, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
OperandRight40: BinaryAssociation = BinaryAssociation(
    name="OperandRight40",
    ends={
        Property(name="metamodel_Operator42", type=metamodel_BinaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel_BinaryOperator41", type=metamodel_Operator, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operandRight43: BinaryAssociation = BinaryAssociation(
    name="operandRight43",
    ends={
        Property(name="metamodel_Condition44", type=metamodel_BinaryCond, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel_BinaryCond", type=metamodel_Condition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operandLeft45: BinaryAssociation = BinaryAssociation(
    name="operandLeft45",
    ends={
        Property(name="metamodel_Condition47", type=metamodel_BinaryCond, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel_BinaryCond46", type=metamodel_Condition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
child48: BinaryAssociation = BinaryAssociation(
    name="child48",
    ends={
        Property(name="metamodel_Condition49", type=metamodel_UnaryCond, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel_UnaryCond", type=metamodel_Condition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
cond35: BinaryAssociation = BinaryAssociation(
    name="cond35",
    ends={
        Property(name="metamodel_Condition", type=metamodel_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel_Transition36", type=metamodel_Condition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_metamodel_DifferentialWheel_Actuator = Generalization(general=Actuator, specific=metamodel_DifferentialWheel)
gen_metamodel_Group_Actuator = Generalization(general=Actuator, specific=metamodel_Group)
gen_metamodel_ActionWheel_Action = Generalization(general=Action, specific=metamodel_ActionWheel)
gen_metamodel_TurnLeft_ActionWheel = Generalization(general=ActionWheel, specific=metamodel_TurnLeft)
gen_metamodel_Forward_ActionWheel = Generalization(general=ActionWheel, specific=metamodel_Forward)
gen_metamodel_Stopping_ActionWheel = Generalization(general=ActionWheel, specific=metamodel_Stopping)
gen_metamodel_Backward_ActionWheel = Generalization(general=ActionWheel, specific=metamodel_Backward)
gen_metamodel_TurnRight_ActionWheel = Generalization(general=ActionWheel, specific=metamodel_TurnRight)
gen_metamodel_DistanceSensor_Sensor = Generalization(general=Sensor, specific=metamodel_DistanceSensor)
gen_metamodel_LightSensor_Sensor = Generalization(general=Sensor, specific=metamodel_LightSensor)
gen_metamodel_BoolVal_Type = Generalization(general=Type, specific=metamodel_BoolVal)
gen_metamodel_FloatVal_Type = Generalization(general=Type, specific=metamodel_FloatVal)
gen_metamodel_IntVal_Type = Generalization(general=Type, specific=metamodel_IntVal)
gen_metamodel_UnaryOperator_Operator = Generalization(general=Operator, specific=metamodel_UnaryOperator)
gen_metamodel_BinaryOperator_Operator = Generalization(general=Operator, specific=metamodel_BinaryOperator)
gen_metamodel_BinaryCond_Condition = Generalization(general=Condition, specific=metamodel_BinaryCond)
gen_metamodel_Or_BinaryCond = Generalization(general=BinaryCond, specific=metamodel_Or)
gen_metamodel_And_BinaryCond = Generalization(general=BinaryCond, specific=metamodel_And)
gen_metamodel_UnaryCond_Condition = Generalization(general=Condition, specific=metamodel_UnaryCond)
gen_metamodel_Negation_UnaryCond = Generalization(general=UnaryCond, specific=metamodel_Negation)
gen_metamodel_Equal_BinaryOperator = Generalization(general=BinaryOperator, specific=metamodel_Equal)
gen_metamodel_Less_BinaryOperator = Generalization(general=BinaryOperator, specific=metamodel_Less)
gen_metamodel_More_BinaryOperator = Generalization(general=BinaryOperator, specific=metamodel_More)
gen_metamodel_Different_BinaryOperator = Generalization(general=BinaryOperator, specific=metamodel_Different)
gen_metamodel_LessOrEqual_BinaryOperator = Generalization(general=BinaryOperator, specific=metamodel_LessOrEqual)
gen_metamodel_MoreOrEqual_BinaryOperator = Generalization(general=BinaryOperator, specific=metamodel_MoreOrEqual)
gen_metamodel_Add_BinaryOperator = Generalization(general=BinaryOperator, specific=metamodel_Add)
gen_metamodel_Sub_BinaryOperator = Generalization(general=BinaryOperator, specific=metamodel_Sub)
gen_metamodel_Negative_UnaryOperator = Generalization(general=UnaryOperator, specific=metamodel_Negative)
gen_metamodel_Positive_UnaryOperator = Generalization(general=UnaryOperator, specific=metamodel_Positive)
gen_metamodel_Operator_Condition = Generalization(general=Condition, specific=metamodel_Operator)

# Domain Model
domain_model = DomainModel(
    name="metamodel",
    types={metamodel_Robot, metamodel_Behaviour, metamodel_Sensor, metamodel_Actuator, metamodel_Action, metamodel_DifferentialWheel, Actuator, metamodel_Group, metamodel_ActionWheel, Action, metamodel_TurnLeft, ActionWheel, metamodel_Forward, metamodel_Stopping, metamodel_Backward, metamodel_TurnRight, metamodel_DistanceSensor, Sensor, metamodel_LightSensor, metamodel_Value, metamodel_Type, metamodel_BoolVal, Type, metamodel_FloatVal, metamodel_IntVal, metamodel_StateMachine, metamodel_State, metamodel_Transition, metamodel_UnaryOperator, Operator, metamodel_BinaryOperator, metamodel_Operator, metamodel_BinaryCond, Condition, metamodel_Or, BinaryCond, metamodel_And, metamodel_UnaryCond, metamodel_Negation, UnaryCond, metamodel_Equal, BinaryOperator, metamodel_Less, metamodel_More, metamodel_Different, metamodel_LessOrEqual, metamodel_MoreOrEqual, metamodel_Add, metamodel_Sub, metamodel_Negative, UnaryOperator, metamodel_Positive, metamodel_Condition},
    associations={behaviours0, sensors1, actuators3, actions5, wheels7, group8, value10, value12, stateMachine14, states16, constants18, transitions21, workingAction23, onEnterAction26, onLeaveAction29, dstId32, valeur37, operandLeft39, OperandRight40, operandRight43, operandLeft45, child48, cond35},
    generalizations={gen_metamodel_DifferentialWheel_Actuator, gen_metamodel_Group_Actuator, gen_metamodel_ActionWheel_Action, gen_metamodel_TurnLeft_ActionWheel, gen_metamodel_Forward_ActionWheel, gen_metamodel_Stopping_ActionWheel, gen_metamodel_Backward_ActionWheel, gen_metamodel_TurnRight_ActionWheel, gen_metamodel_DistanceSensor_Sensor, gen_metamodel_LightSensor_Sensor, gen_metamodel_BoolVal_Type, gen_metamodel_FloatVal_Type, gen_metamodel_IntVal_Type, gen_metamodel_UnaryOperator_Operator, gen_metamodel_BinaryOperator_Operator, gen_metamodel_BinaryCond_Condition, gen_metamodel_Or_BinaryCond, gen_metamodel_And_BinaryCond, gen_metamodel_UnaryCond_Condition, gen_metamodel_Negation_UnaryCond, gen_metamodel_Equal_BinaryOperator, gen_metamodel_Less_BinaryOperator, gen_metamodel_More_BinaryOperator, gen_metamodel_Different_BinaryOperator, gen_metamodel_LessOrEqual_BinaryOperator, gen_metamodel_MoreOrEqual_BinaryOperator, gen_metamodel_Add_BinaryOperator, gen_metamodel_Sub_BinaryOperator, gen_metamodel_Negative_UnaryOperator, gen_metamodel_Positive_UnaryOperator, gen_metamodel_Operator_Condition},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)