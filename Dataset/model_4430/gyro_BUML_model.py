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
LightStatus: Enumeration = Enumeration(
    name="LightStatus",
    literals={
            EnumerationLiteral(name="On"),
			EnumerationLiteral(name="Off")
    }
)

SuccessState: Enumeration = Enumeration(
    name="SuccessState",
    literals={
            EnumerationLiteral(name="Success"),
			EnumerationLiteral(name="Failure"),
			EnumerationLiteral(name="Running")
    }
)

FailureState: Enumeration = Enumeration(
    name="FailureState",
    literals={
            EnumerationLiteral(name="Failure"),
			EnumerationLiteral(name="Success"),
			EnumerationLiteral(name="Running")
    }
)

RunningState: Enumeration = Enumeration(
    name="RunningState",
    literals={
            EnumerationLiteral(name="Success"),
			EnumerationLiteral(name="Failure"),
			EnumerationLiteral(name="Running")
    }
)

BumperKind: Enumeration = Enumeration(
    name="BumperKind",
    literals={
            EnumerationLiteral(name="Left"),
			EnumerationLiteral(name="Right")
    }
)

DistanceKind: Enumeration = Enumeration(
    name="DistanceKind",
    literals={
            EnumerationLiteral(name="Minor"),
			EnumerationLiteral(name="Major")
    }
)

# Classes
gyro_GyroSpecification = Class(name="gyro::GyroSpecification")
Node = Class(name="Node")
gyro_Priority = Class(name="gyro::Priority")
Behavior = Class(name="Behavior")
gyro_Parallel = Class(name="gyro::Parallel")
gyro_Sequential = Class(name="gyro::Sequential")
gyro_StatusChange = Class(name="gyro::StatusChange")
gyro_Action = Class(name="gyro::Action", is_abstract=True)
gyro_Condition = Class(name="gyro::Condition", is_abstract=True)
Action = Class(name="Action")
gyro_Distance = Class(name="gyro::Distance")
Condition = Class(name="Condition")
gyro_Node = Class(name="gyro::Node", is_abstract=True)
gyro_Child = Class(name="gyro::Child")
gyro_Sibling = Class(name="gyro::Sibling")
gyro_Behavior = Class(name="gyro::Behavior", is_abstract=True)
gyro_Bumpers = Class(name="gyro::Bumpers")
gyro_Waiting = Class(name="gyro::Waiting")
gyro_Actuate = Class(name="gyro::Actuate", is_abstract=True)
gyro_Motor = Class(name="gyro::Motor")
Actuate = Class(name="Actuate")
gyro_Servo = Class(name="gyro::Servo")
gyro_LED = Class(name="gyro::LED")

# gyro_GyroSpecification class attributes and methods
gyro_GyroSpecification_name: Property = Property(name="name", type=StringType)
gyro_GyroSpecification.attributes={gyro_GyroSpecification_name}

# Node class attributes and methods

# gyro_Priority class attributes and methods

# Behavior class attributes and methods

# gyro_Parallel class attributes and methods

# gyro_Sequential class attributes and methods

# gyro_StatusChange class attributes and methods
gyro_StatusChange_changeSuccess: Property = Property(name="changeSuccess", type=StringType)
gyro_StatusChange_changeFailure: Property = Property(name="changeFailure", type=StringType)
gyro_StatusChange_changeRunning: Property = Property(name="changeRunning", type=StringType)
gyro_StatusChange.attributes={gyro_StatusChange_changeRunning, gyro_StatusChange_changeSuccess, gyro_StatusChange_changeFailure}

# gyro_Action class attributes and methods

# gyro_Condition class attributes and methods

# Action class attributes and methods

# gyro_Distance class attributes and methods
gyro_Distance_value: Property = Property(name="value", type=IntegerType)
gyro_Distance_kind: Property = Property(name="kind", type=StringType)
gyro_Distance.attributes={gyro_Distance_kind, gyro_Distance_value}

# Condition class attributes and methods

# gyro_Node class attributes and methods
gyro_Node_name: Property = Property(name="name", type=StringType)
gyro_Node.attributes={gyro_Node_name}

# gyro_Child class attributes and methods

# gyro_Sibling class attributes and methods

# gyro_Behavior class attributes and methods

# gyro_Bumpers class attributes and methods
gyro_Bumpers_bumperKind: Property = Property(name="bumperKind", type=StringType)
gyro_Bumpers.attributes={gyro_Bumpers_bumperKind}

# gyro_Waiting class attributes and methods
gyro_Waiting_time: Property = Property(name="time", type=IntegerType)
gyro_Waiting.attributes={gyro_Waiting_time}

# gyro_Actuate class attributes and methods

# gyro_Motor class attributes and methods
gyro_Motor_leftMotor: Property = Property(name="leftMotor", type=IntegerType)
gyro_Motor_rightMotor: Property = Property(name="rightMotor", type=IntegerType)
gyro_Motor.attributes={gyro_Motor_leftMotor, gyro_Motor_rightMotor}

# Actuate class attributes and methods

# gyro_Servo class attributes and methods
gyro_Servo_minimalPosition: Property = Property(name="minimalPosition", type=IntegerType)
gyro_Servo_maximalPosition: Property = Property(name="maximalPosition", type=IntegerType)
gyro_Servo_step: Property = Property(name="step", type=IntegerType)
gyro_Servo.attributes={gyro_Servo_step, gyro_Servo_minimalPosition, gyro_Servo_maximalPosition}

# gyro_LED class attributes and methods
gyro_LED_status: Property = Property(name="status", type=StringType)
gyro_LED.attributes={gyro_LED_status}

# Relationships
target7: BinaryAssociation = BinaryAssociation(
    name="target7",
    ends={
        Property(name="gyro_Node9", type=gyro_Child, multiplicity=Multiplicity(1, 1)),
        Property(name="gyro_Child8", type=gyro_Node, multiplicity=Multiplicity(0, 9999))
    }
)
source10: BinaryAssociation = BinaryAssociation(
    name="source10",
    ends={
        Property(name="gyro_Node12", type=gyro_Sibling, multiplicity=Multiplicity(1, 1)),
        Property(name="gyro_Sibling11", type=gyro_Node, multiplicity=Multiplicity(0, 9999))
    }
)
target13: BinaryAssociation = BinaryAssociation(
    name="target13",
    ends={
        Property(name="gyro_Node15", type=gyro_Sibling, multiplicity=Multiplicity(1, 1)),
        Property(name="gyro_Sibling14", type=gyro_Node, multiplicity=Multiplicity(0, 9999))
    }
)
nodes0: BinaryAssociation = BinaryAssociation(
    name="nodes0",
    ends={
        Property(name="gyro_Node", type=gyro_GyroSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="gyro_GyroSpecification", type=gyro_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
child1: BinaryAssociation = BinaryAssociation(
    name="child1",
    ends={
        Property(name="gyro_Child", type=gyro_GyroSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="gyro_GyroSpecification2", type=gyro_Child, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
next3: BinaryAssociation = BinaryAssociation(
    name="next3",
    ends={
        Property(name="gyro_Sibling", type=gyro_GyroSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="gyro_GyroSpecification4", type=gyro_Sibling, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source5: BinaryAssociation = BinaryAssociation(
    name="source5",
    ends={
        Property(name="gyro_Behavior", type=gyro_Child, multiplicity=Multiplicity(1, 1)),
        Property(name="gyro_Child6", type=gyro_Behavior, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_gyro_Behavior_Node = Generalization(general=Node, specific=gyro_Behavior)
gen_gyro_Priority_Behavior = Generalization(general=Behavior, specific=gyro_Priority)
gen_gyro_Parallel_Behavior = Generalization(general=Behavior, specific=gyro_Parallel)
gen_gyro_Sequential_Behavior = Generalization(general=Behavior, specific=gyro_Sequential)
gen_gyro_StatusChange_Behavior = Generalization(general=Behavior, specific=gyro_StatusChange)
gen_gyro_Action_Node = Generalization(general=Node, specific=gyro_Action)
gen_gyro_Condition_Action = Generalization(general=Action, specific=gyro_Condition)
gen_gyro_Distance_Condition = Generalization(general=Condition, specific=gyro_Distance)
gen_gyro_Bumpers_Condition = Generalization(general=Condition, specific=gyro_Bumpers)
gen_gyro_Waiting_Condition = Generalization(general=Condition, specific=gyro_Waiting)
gen_gyro_Actuate_Action = Generalization(general=Action, specific=gyro_Actuate)
gen_gyro_Motor_Actuate = Generalization(general=Actuate, specific=gyro_Motor)
gen_gyro_Servo_Actuate = Generalization(general=Actuate, specific=gyro_Servo)
gen_gyro_LED_Actuate = Generalization(general=Actuate, specific=gyro_LED)

# Domain Model
domain_model = DomainModel(
    name="gyro",
    types={gyro_GyroSpecification, Node, gyro_Priority, Behavior, gyro_Parallel, gyro_Sequential, gyro_StatusChange, gyro_Action, gyro_Condition, Action, gyro_Distance, Condition, gyro_Node, gyro_Child, gyro_Sibling, gyro_Behavior, gyro_Bumpers, gyro_Waiting, gyro_Actuate, gyro_Motor, Actuate, gyro_Servo, gyro_LED, LightStatus, SuccessState, FailureState, RunningState, BumperKind, DistanceKind},
    associations={target7, source10, target13, nodes0, child1, next3, source5},
    generalizations={gen_gyro_Behavior_Node, gen_gyro_Priority_Behavior, gen_gyro_Parallel_Behavior, gen_gyro_Sequential_Behavior, gen_gyro_StatusChange_Behavior, gen_gyro_Action_Node, gen_gyro_Condition_Action, gen_gyro_Distance_Condition, gen_gyro_Bumpers_Condition, gen_gyro_Waiting_Condition, gen_gyro_Actuate_Action, gen_gyro_Motor_Actuate, gen_gyro_Servo_Actuate, gen_gyro_LED_Actuate},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)