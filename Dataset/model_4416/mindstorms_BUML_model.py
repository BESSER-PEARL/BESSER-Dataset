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
Color: Enumeration = Enumeration(
    name="Color",
    literals={
            EnumerationLiteral(name="RED"),
			EnumerationLiteral(name="BROWN"),
			EnumerationLiteral(name="NONE"),
			EnumerationLiteral(name="GREEN"),
			EnumerationLiteral(name="BLUE"),
			EnumerationLiteral(name="YELLOW"),
			EnumerationLiteral(name="MAGENTA"),
			EnumerationLiteral(name="ORANGE"),
			EnumerationLiteral(name="WHITE"),
			EnumerationLiteral(name="BLACK"),
			EnumerationLiteral(name="PINK"),
			EnumerationLiteral(name="GRAY"),
			EnumerationLiteral(name="LIGHT_GRAY"),
			EnumerationLiteral(name="DARK_GRAY"),
			EnumerationLiteral(name="CYAN")
    }
)

OperatorKind: Enumeration = Enumeration(
    name="OperatorKind",
    literals={
            EnumerationLiteral(name="equal"),
			EnumerationLiteral(name="notEqual"),
			EnumerationLiteral(name="upperOrEqual"),
			EnumerationLiteral(name="lowerOrEqual")
    }
)

# Classes
mindstorms_Instruction = Class(name="mindstorms::Instruction", is_abstract=True)
mindstorms_Flow = Class(name="mindstorms::Flow", is_abstract=True)
Instruction = Class(name="Instruction")
mindstorms_Choregraphy = Class(name="mindstorms::Choregraphy")
Flow = Class(name="Flow")
mindstorms_Reuse = Class(name="mindstorms::Reuse")
mindstorms_Action = Class(name="mindstorms::Action", is_abstract=True)
mindstorms_While = Class(name="mindstorms::While")
mindstorms_GoForward = Class(name="mindstorms::GoForward")
Action = Class(name="Action")
mindstorms_GoBackward = Class(name="mindstorms::GoBackward")
mindstorms_Rotate = Class(name="mindstorms::Rotate")
mindstorms_GoTo = Class(name="mindstorms::GoTo")
mindstorms_ReturnToBase = Class(name="mindstorms::ReturnToBase")
mindstorms_Grab = Class(name="mindstorms::Grab")
mindstorms_Release = Class(name="mindstorms::Release")
mindstorms_Delay = Class(name="mindstorms::Delay")
mindstorms_TouchSensor = Class(name="mindstorms::TouchSensor")
Sensor = Class(name="Sensor")
mindstorms_UltrasonicSensor = Class(name="mindstorms::UltrasonicSensor")
mindstorms_ColorSensor = Class(name="mindstorms::ColorSensor")
mindstorms_ConditionalFlow = Class(name="mindstorms::ConditionalFlow", is_abstract=True)
mindstorms_Condition = Class(name="mindstorms::Condition", is_abstract=True)
mindstorms_Sensor = Class(name="mindstorms::Sensor", is_abstract=True)
Condition = Class(name="Condition")
mindstorms_If = Class(name="mindstorms::If")
ConditionalFlow = Class(name="ConditionalFlow")

# mindstorms_Instruction class attributes and methods

# mindstorms_Flow class attributes and methods

# Instruction class attributes and methods

# mindstorms_Choregraphy class attributes and methods
mindstorms_Choregraphy_name: Property = Property(name="name", type=StringType)
mindstorms_Choregraphy.attributes={mindstorms_Choregraphy_name}

# Flow class attributes and methods

# mindstorms_Reuse class attributes and methods

# mindstorms_Action class attributes and methods

# mindstorms_While class attributes and methods

# mindstorms_GoForward class attributes and methods
mindstorms_GoForward_cm: Property = Property(name="cm", type=IntegerType)
mindstorms_GoForward_infinite: Property = Property(name="infinite", type=BooleanType)
mindstorms_GoForward.attributes={mindstorms_GoForward_infinite, mindstorms_GoForward_cm}

# Action class attributes and methods

# mindstorms_GoBackward class attributes and methods
mindstorms_GoBackward_cm: Property = Property(name="cm", type=IntegerType)
mindstorms_GoBackward_infinite: Property = Property(name="infinite", type=BooleanType)
mindstorms_GoBackward.attributes={mindstorms_GoBackward_cm, mindstorms_GoBackward_infinite}

# mindstorms_Rotate class attributes and methods
mindstorms_Rotate_degrees: Property = Property(name="degrees", type=IntegerType)
mindstorms_Rotate_random: Property = Property(name="random", type=BooleanType)
mindstorms_Rotate.attributes={mindstorms_Rotate_degrees, mindstorms_Rotate_random}

# mindstorms_GoTo class attributes and methods
mindstorms_GoTo_x: Property = Property(name="x", type=IntegerType)
mindstorms_GoTo_y: Property = Property(name="y", type=IntegerType)
mindstorms_GoTo.attributes={mindstorms_GoTo_x, mindstorms_GoTo_y}

# mindstorms_ReturnToBase class attributes and methods

# mindstorms_Grab class attributes and methods

# mindstorms_Release class attributes and methods

# mindstorms_Delay class attributes and methods
mindstorms_Delay_ms: Property = Property(name="ms", type=IntegerType)
mindstorms_Delay.attributes={mindstorms_Delay_ms}

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

# mindstorms_ConditionalFlow class attributes and methods

# mindstorms_Condition class attributes and methods

# mindstorms_Sensor class attributes and methods

# Condition class attributes and methods

# mindstorms_If class attributes and methods

# ConditionalFlow class attributes and methods

# Relationships
next1: BinaryAssociation = BinaryAssociation(
    name="next1",
    ends={
        Property(name="Instruction", type=mindstorms_Instruction, multiplicity=Multiplicity(1, 1)),
        Property(name="previous", type=mindstorms_Instruction, multiplicity=Multiplicity(0, 1))
    }
)
previous3: BinaryAssociation = BinaryAssociation(
    name="previous3",
    ends={
        Property(name="Instruction4", type=mindstorms_Instruction, multiplicity=Multiplicity(1, 1)),
        Property(name="next", type=mindstorms_Instruction, multiplicity=Multiplicity(0, 1))
    }
)
first5: BinaryAssociation = BinaryAssociation(
    name="first5",
    ends={
        Property(name="mindstorms_Instruction", type=mindstorms_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="mindstorms_Flow", type=mindstorms_Instruction, multiplicity=Multiplicity(0, 1))
    }
)
instructions6: BinaryAssociation = BinaryAssociation(
    name="instructions6",
    ends={
        Property(name="mindstorms_Instruction8", type=mindstorms_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="mindstorms_Flow7", type=mindstorms_Instruction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
choregraphy9: BinaryAssociation = BinaryAssociation(
    name="choregraphy9",
    ends={
        Property(name="mindstorms_Choregraphy", type=mindstorms_Reuse, multiplicity=Multiplicity(1, 1)),
        Property(name="mindstorms_Reuse", type=mindstorms_Choregraphy, multiplicity=Multiplicity(0, 1))
    }
)
condition10: BinaryAssociation = BinaryAssociation(
    name="condition10",
    ends={
        Property(name="mindstorms_Condition", type=mindstorms_ConditionalFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="mindstorms_ConditionalFlow", type=mindstorms_Condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elsif12: BinaryAssociation = BinaryAssociation(
    name="elsif12",
    ends={
        Property(name="mindstorms_If", type=mindstorms_If, multiplicity=Multiplicity(1, 1)),
        Property(name="mindstorms_If11", type=mindstorms_If, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_mindstorms_Flow_Instruction = Generalization(general=Instruction, specific=mindstorms_Flow)
gen_mindstorms_Choregraphy_Flow = Generalization(general=Flow, specific=mindstorms_Choregraphy)
gen_mindstorms_Reuse_Instruction = Generalization(general=Instruction, specific=mindstorms_Reuse)
gen_mindstorms_Action_Instruction = Generalization(general=Instruction, specific=mindstorms_Action)
gen_mindstorms_While_ConditionalFlow = Generalization(general=ConditionalFlow, specific=mindstorms_While)
gen_mindstorms_GoForward_Action = Generalization(general=Action, specific=mindstorms_GoForward)
gen_mindstorms_GoBackward_Action = Generalization(general=Action, specific=mindstorms_GoBackward)
gen_mindstorms_Rotate_Action = Generalization(general=Action, specific=mindstorms_Rotate)
gen_mindstorms_GoTo_Action = Generalization(general=Action, specific=mindstorms_GoTo)
gen_mindstorms_ReturnToBase_Action = Generalization(general=Action, specific=mindstorms_ReturnToBase)
gen_mindstorms_Grab_Action = Generalization(general=Action, specific=mindstorms_Grab)
gen_mindstorms_Release_Action = Generalization(general=Action, specific=mindstorms_Release)
gen_mindstorms_Delay_Action = Generalization(general=Action, specific=mindstorms_Delay)
gen_mindstorms_TouchSensor_Sensor = Generalization(general=Sensor, specific=mindstorms_TouchSensor)
gen_mindstorms_UltrasonicSensor_Sensor = Generalization(general=Sensor, specific=mindstorms_UltrasonicSensor)
gen_mindstorms_ColorSensor_Sensor = Generalization(general=Sensor, specific=mindstorms_ColorSensor)
gen_mindstorms_ConditionalFlow_Flow = Generalization(general=Flow, specific=mindstorms_ConditionalFlow)
gen_mindstorms_Sensor_Condition = Generalization(general=Condition, specific=mindstorms_Sensor)
gen_mindstorms_If_ConditionalFlow = Generalization(general=ConditionalFlow, specific=mindstorms_If)

# Domain Model
domain_model = DomainModel(
    name="mindstorms",
    types={mindstorms_Instruction, mindstorms_Flow, Instruction, mindstorms_Choregraphy, Flow, mindstorms_Reuse, mindstorms_Action, mindstorms_While, mindstorms_GoForward, Action, mindstorms_GoBackward, mindstorms_Rotate, mindstorms_GoTo, mindstorms_ReturnToBase, mindstorms_Grab, mindstorms_Release, mindstorms_Delay, mindstorms_TouchSensor, Sensor, mindstorms_UltrasonicSensor, mindstorms_ColorSensor, mindstorms_ConditionalFlow, mindstorms_Condition, mindstorms_Sensor, Condition, mindstorms_If, ConditionalFlow, Color, OperatorKind},
    associations={next1, previous3, first5, instructions6, choregraphy9, condition10, elsif12},
    generalizations={gen_mindstorms_Flow_Instruction, gen_mindstorms_Choregraphy_Flow, gen_mindstorms_Reuse_Instruction, gen_mindstorms_Action_Instruction, gen_mindstorms_While_ConditionalFlow, gen_mindstorms_GoForward_Action, gen_mindstorms_GoBackward_Action, gen_mindstorms_Rotate_Action, gen_mindstorms_GoTo_Action, gen_mindstorms_ReturnToBase_Action, gen_mindstorms_Grab_Action, gen_mindstorms_Release_Action, gen_mindstorms_Delay_Action, gen_mindstorms_TouchSensor_Sensor, gen_mindstorms_UltrasonicSensor_Sensor, gen_mindstorms_ColorSensor_Sensor, gen_mindstorms_ConditionalFlow_Flow, gen_mindstorms_Sensor_Condition, gen_mindstorms_If_ConditionalFlow},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)