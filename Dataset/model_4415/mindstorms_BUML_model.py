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
OperatorKind: Enumeration = Enumeration(
    name="OperatorKind",
    literals={
            EnumerationLiteral(name="equal"),
			EnumerationLiteral(name="notEqual"),
			EnumerationLiteral(name="upperOrEqual"),
			EnumerationLiteral(name="lowerOrEqual")
    }
)

Color: Enumeration = Enumeration(
    name="Color",
    literals={
            EnumerationLiteral(name="GRAY"),
			EnumerationLiteral(name="LIGHT_GRAY"),
			EnumerationLiteral(name="DARK_GRAY"),
			EnumerationLiteral(name="CYAN"),
			EnumerationLiteral(name="BROWN"),
			EnumerationLiteral(name="NONE"),
			EnumerationLiteral(name="RED"),
			EnumerationLiteral(name="GREEN"),
			EnumerationLiteral(name="BLUE"),
			EnumerationLiteral(name="YELLOW"),
			EnumerationLiteral(name="MAGENTA"),
			EnumerationLiteral(name="ORANGE"),
			EnumerationLiteral(name="WHITE"),
			EnumerationLiteral(name="BLACK"),
			EnumerationLiteral(name="PINK")
    }
)

# Classes
mindstorms_NamedElement = Class(name="mindstorms::NamedElement", is_abstract=True)
Condition = Class(name="Condition")
mindstorms_Condition = Class(name="mindstorms::Condition", is_abstract=True)
mindstorms_If = Class(name="mindstorms::If")
Flow = Class(name="Flow")
mindstorms_While = Class(name="mindstorms::While")
mindstorms_GoForward = Class(name="mindstorms::GoForward")
Action = Class(name="Action")
mindstorms_GoBackward = Class(name="mindstorms::GoBackward")
mindstorms_Main = Class(name="mindstorms::Main")
mindstorms_Instruction = Class(name="mindstorms::Instruction", is_abstract=True)
NamedElement = Class(name="NamedElement")
mindstorms_BlockContainer = Class(name="mindstorms::BlockContainer", is_abstract=True)
mindstorms_Block = Class(name="mindstorms::Block", is_abstract=True)
mindstorms_Procedure = Class(name="mindstorms::Procedure")
Instruction = Class(name="Instruction")
BlockContainer = Class(name="BlockContainer")
mindstorms_Arbitrator = Class(name="mindstorms::Arbitrator")
ConditionContainer = Class(name="ConditionContainer")
mindstorms_Behavior = Class(name="mindstorms::Behavior")
mindstorms_ReuseInstruction = Class(name="mindstorms::ReuseInstruction")
mindstorms_Action = Class(name="mindstorms::Action", is_abstract=True)
Block = Class(name="Block")
mindstorms_Flow = Class(name="mindstorms::Flow", is_abstract=True)
mindstorms_Sensor = Class(name="mindstorms::Sensor", is_abstract=True)
mindstorms_ConditionContainer = Class(name="mindstorms::ConditionContainer", is_abstract=True)
mindstorms_GoToEnemy = Class(name="mindstorms::GoToEnemy")
mindstorms_Rotate = Class(name="mindstorms::Rotate")
mindstorms_GoTo = Class(name="mindstorms::GoTo")
mindstorms_ReturnToBase = Class(name="mindstorms::ReturnToBase")
mindstorms_Grab = Class(name="mindstorms::Grab")
mindstorms_Release = Class(name="mindstorms::Release")
mindstorms_Delay = Class(name="mindstorms::Delay")
mindstorms_AvoidObstacle = Class(name="mindstorms::AvoidObstacle")
Behavior = Class(name="Behavior")
mindstorms_ReturnBottleToBase = Class(name="mindstorms::ReturnBottleToBase")
mindstorms_ExploreForward = Class(name="mindstorms::ExploreForward")
mindstorms_TouchSensor = Class(name="mindstorms::TouchSensor")
Sensor = Class(name="Sensor")
mindstorms_UltrasonicSensor = Class(name="mindstorms::UltrasonicSensor")
mindstorms_ColorSensor = Class(name="mindstorms::ColorSensor")

# mindstorms_NamedElement class attributes and methods
mindstorms_NamedElement_name: Property = Property(name="name", type=StringType)
mindstorms_NamedElement.attributes={mindstorms_NamedElement_name}

# Condition class attributes and methods

# mindstorms_Condition class attributes and methods

# mindstorms_If class attributes and methods

# Flow class attributes and methods

# mindstorms_While class attributes and methods

# mindstorms_GoForward class attributes and methods
mindstorms_GoForward_cm: Property = Property(name="cm", type=IntegerType)
mindstorms_GoForward_infinite: Property = Property(name="infinite", type=BooleanType)
mindstorms_GoForward.attributes={mindstorms_GoForward_infinite, mindstorms_GoForward_cm}

# Action class attributes and methods

# mindstorms_GoBackward class attributes and methods
mindstorms_GoBackward_cm: Property = Property(name="cm", type=IntegerType)
mindstorms_GoBackward_infinite: Property = Property(name="infinite", type=BooleanType)
mindstorms_GoBackward.attributes={mindstorms_GoBackward_infinite, mindstorms_GoBackward_cm}

# mindstorms_Main class attributes and methods

# mindstorms_Instruction class attributes and methods

# NamedElement class attributes and methods

# mindstorms_BlockContainer class attributes and methods

# mindstorms_Block class attributes and methods

# mindstorms_Procedure class attributes and methods

# Instruction class attributes and methods

# BlockContainer class attributes and methods

# mindstorms_Arbitrator class attributes and methods

# ConditionContainer class attributes and methods

# mindstorms_Behavior class attributes and methods

# mindstorms_ReuseInstruction class attributes and methods

# mindstorms_Action class attributes and methods

# Block class attributes and methods

# mindstorms_Flow class attributes and methods

# mindstorms_Sensor class attributes and methods

# mindstorms_ConditionContainer class attributes and methods

# mindstorms_GoToEnemy class attributes and methods

# mindstorms_Rotate class attributes and methods
mindstorms_Rotate_degrees: Property = Property(name="degrees", type=IntegerType)
mindstorms_Rotate_random: Property = Property(name="random", type=BooleanType)
mindstorms_Rotate.attributes={mindstorms_Rotate_random, mindstorms_Rotate_degrees}

# mindstorms_GoTo class attributes and methods
mindstorms_GoTo_x: Property = Property(name="x", type=IntegerType)
mindstorms_GoTo_y: Property = Property(name="y", type=IntegerType)
mindstorms_GoTo.attributes={mindstorms_GoTo_y, mindstorms_GoTo_x}

# mindstorms_ReturnToBase class attributes and methods

# mindstorms_Grab class attributes and methods

# mindstorms_Release class attributes and methods

# mindstorms_Delay class attributes and methods
mindstorms_Delay_ms: Property = Property(name="ms", type=IntegerType)
mindstorms_Delay.attributes={mindstorms_Delay_ms}

# mindstorms_AvoidObstacle class attributes and methods

# Behavior class attributes and methods

# mindstorms_ReturnBottleToBase class attributes and methods

# mindstorms_ExploreForward class attributes and methods

# mindstorms_TouchSensor class attributes and methods
mindstorms_TouchSensor_isPressed: Property = Property(name="isPressed", type=BooleanType)
mindstorms_TouchSensor.attributes={mindstorms_TouchSensor_isPressed}

# Sensor class attributes and methods

# mindstorms_UltrasonicSensor class attributes and methods
mindstorms_UltrasonicSensor_operator: Property = Property(name="operator", type=StringType)
mindstorms_UltrasonicSensor_value: Property = Property(name="value", type=FloatType)
mindstorms_UltrasonicSensor.attributes={mindstorms_UltrasonicSensor_operator, mindstorms_UltrasonicSensor_value}

# mindstorms_ColorSensor class attributes and methods
mindstorms_ColorSensor_color: Property = Property(name="color", type=StringType)
mindstorms_ColorSensor.attributes={mindstorms_ColorSensor_color}

# Relationships
instructions0: BinaryAssociation = BinaryAssociation(
    name="instructions0",
    ends={
        Property(name="mindstorms_Instruction", type=mindstorms_Main, multiplicity=Multiplicity(1, 1)),
        Property(name="mindstorms_Main", type=mindstorms_Instruction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
blocks1: BinaryAssociation = BinaryAssociation(
    name="blocks1",
    ends={
        Property(name="mindstorms_Block", type=mindstorms_BlockContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="mindstorms_BlockContainer", type=mindstorms_Block, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
behaviors2: BinaryAssociation = BinaryAssociation(
    name="behaviors2",
    ends={
        Property(name="mindstorms_Behavior", type=mindstorms_Arbitrator, multiplicity=Multiplicity(1, 1)),
        Property(name="mindstorms_Arbitrator", type=mindstorms_Behavior, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reuse3: BinaryAssociation = BinaryAssociation(
    name="reuse3",
    ends={
        Property(name="mindstorms_Behavior5", type=mindstorms_Arbitrator, multiplicity=Multiplicity(1, 1)),
        Property(name="mindstorms_Arbitrator4", type=mindstorms_Behavior, multiplicity=Multiplicity(0, 9999))
    }
)
reuse6: BinaryAssociation = BinaryAssociation(
    name="reuse6",
    ends={
        Property(name="mindstorms_Instruction7", type=mindstorms_ReuseInstruction, multiplicity=Multiplicity(1, 1)),
        Property(name="mindstorms_ReuseInstruction", type=mindstorms_Instruction, multiplicity=Multiplicity(0, 1))
    }
)
condition8: BinaryAssociation = BinaryAssociation(
    name="condition8",
    ends={
        Property(name="mindstorms_Condition", type=mindstorms_ConditionContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="mindstorms_ConditionContainer", type=mindstorms_Condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_mindstorms_Sensor_Condition = Generalization(general=Condition, specific=mindstorms_Sensor)
gen_mindstorms_If_Flow = Generalization(general=Flow, specific=mindstorms_If)
gen_mindstorms_While_Flow = Generalization(general=Flow, specific=mindstorms_While)
gen_mindstorms_GoForward_Action = Generalization(general=Action, specific=mindstorms_GoForward)
gen_mindstorms_GoBackward_Action = Generalization(general=Action, specific=mindstorms_GoBackward)
gen_mindstorms_Instruction_NamedElement = Generalization(general=NamedElement, specific=mindstorms_Instruction)
gen_mindstorms_Procedure_Instruction = Generalization(general=Instruction, specific=mindstorms_Procedure)
gen_mindstorms_Procedure_BlockContainer = Generalization(general=BlockContainer, specific=mindstorms_Procedure)
gen_mindstorms_Arbitrator_Instruction = Generalization(general=Instruction, specific=mindstorms_Arbitrator)
gen_mindstorms_Arbitrator_ConditionContainer = Generalization(general=ConditionContainer, specific=mindstorms_Arbitrator)
gen_mindstorms_Behavior_NamedElement = Generalization(general=NamedElement, specific=mindstorms_Behavior)
gen_mindstorms_Behavior_BlockContainer = Generalization(general=BlockContainer, specific=mindstorms_Behavior)
gen_mindstorms_Behavior_ConditionContainer = Generalization(general=ConditionContainer, specific=mindstorms_Behavior)
gen_mindstorms_ReuseInstruction_Instruction = Generalization(general=Instruction, specific=mindstorms_ReuseInstruction)
gen_mindstorms_Block_Instruction = Generalization(general=Instruction, specific=mindstorms_Block)
gen_mindstorms_Action_Block = Generalization(general=Block, specific=mindstorms_Action)
gen_mindstorms_Flow_Block = Generalization(general=Block, specific=mindstorms_Flow)
gen_mindstorms_Flow_BlockContainer = Generalization(general=BlockContainer, specific=mindstorms_Flow)
gen_mindstorms_Flow_ConditionContainer = Generalization(general=ConditionContainer, specific=mindstorms_Flow)
gen_mindstorms_Sensor_NamedElement = Generalization(general=NamedElement, specific=mindstorms_Sensor)
gen_mindstorms_Rotate_Action = Generalization(general=Action, specific=mindstorms_Rotate)
gen_mindstorms_GoTo_Action = Generalization(general=Action, specific=mindstorms_GoTo)
gen_mindstorms_ReturnToBase_Action = Generalization(general=Action, specific=mindstorms_ReturnToBase)
gen_mindstorms_Grab_Action = Generalization(general=Action, specific=mindstorms_Grab)
gen_mindstorms_Release_Action = Generalization(general=Action, specific=mindstorms_Release)
gen_mindstorms_Delay_Action = Generalization(general=Action, specific=mindstorms_Delay)
gen_mindstorms_AvoidObstacle_Behavior = Generalization(general=Behavior, specific=mindstorms_AvoidObstacle)
gen_mindstorms_ReturnBottleToBase_Behavior = Generalization(general=Behavior, specific=mindstorms_ReturnBottleToBase)
gen_mindstorms_ExploreForward_Behavior = Generalization(general=Behavior, specific=mindstorms_ExploreForward)
gen_mindstorms_TouchSensor_Sensor = Generalization(general=Sensor, specific=mindstorms_TouchSensor)
gen_mindstorms_UltrasonicSensor_Sensor = Generalization(general=Sensor, specific=mindstorms_UltrasonicSensor)
gen_mindstorms_ColorSensor_Sensor = Generalization(general=Sensor, specific=mindstorms_ColorSensor)
gen_mindstorms_GoToEnemy_Action = Generalization(general=Action, specific=mindstorms_GoToEnemy)

# Domain Model
domain_model = DomainModel(
    name="mindstorms",
    types={mindstorms_NamedElement, Condition, mindstorms_Condition, mindstorms_If, Flow, mindstorms_While, mindstorms_GoForward, Action, mindstorms_GoBackward, mindstorms_Main, mindstorms_Instruction, NamedElement, mindstorms_BlockContainer, mindstorms_Block, mindstorms_Procedure, Instruction, BlockContainer, mindstorms_Arbitrator, ConditionContainer, mindstorms_Behavior, mindstorms_ReuseInstruction, mindstorms_Action, Block, mindstorms_Flow, mindstorms_Sensor, mindstorms_ConditionContainer, mindstorms_GoToEnemy, mindstorms_Rotate, mindstorms_GoTo, mindstorms_ReturnToBase, mindstorms_Grab, mindstorms_Release, mindstorms_Delay, mindstorms_AvoidObstacle, Behavior, mindstorms_ReturnBottleToBase, mindstorms_ExploreForward, mindstorms_TouchSensor, Sensor, mindstorms_UltrasonicSensor, mindstorms_ColorSensor, OperatorKind, Color},
    associations={instructions0, blocks1, behaviors2, reuse3, reuse6, condition8},
    generalizations={gen_mindstorms_Sensor_Condition, gen_mindstorms_If_Flow, gen_mindstorms_While_Flow, gen_mindstorms_GoForward_Action, gen_mindstorms_GoBackward_Action, gen_mindstorms_Instruction_NamedElement, gen_mindstorms_Procedure_Instruction, gen_mindstorms_Procedure_BlockContainer, gen_mindstorms_Arbitrator_Instruction, gen_mindstorms_Arbitrator_ConditionContainer, gen_mindstorms_Behavior_NamedElement, gen_mindstorms_Behavior_BlockContainer, gen_mindstorms_Behavior_ConditionContainer, gen_mindstorms_ReuseInstruction_Instruction, gen_mindstorms_Block_Instruction, gen_mindstorms_Action_Block, gen_mindstorms_Flow_Block, gen_mindstorms_Flow_BlockContainer, gen_mindstorms_Flow_ConditionContainer, gen_mindstorms_Sensor_NamedElement, gen_mindstorms_Rotate_Action, gen_mindstorms_GoTo_Action, gen_mindstorms_ReturnToBase_Action, gen_mindstorms_Grab_Action, gen_mindstorms_Release_Action, gen_mindstorms_Delay_Action, gen_mindstorms_AvoidObstacle_Behavior, gen_mindstorms_ReturnBottleToBase_Behavior, gen_mindstorms_ExploreForward_Behavior, gen_mindstorms_TouchSensor_Sensor, gen_mindstorms_UltrasonicSensor_Sensor, gen_mindstorms_ColorSensor_Sensor, gen_mindstorms_GoToEnemy_Action},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)