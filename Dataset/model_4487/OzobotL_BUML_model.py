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
            EnumerationLiteral(name="none"),
			EnumerationLiteral(name="red"),
			EnumerationLiteral(name="green"),
			EnumerationLiteral(name="blue"),
			EnumerationLiteral(name="yellow")
    }
)

Direction: Enumeration = Enumeration(
    name="Direction",
    literals={
            EnumerationLiteral(name="left"),
			EnumerationLiteral(name="right")
    }
)

Velocity: Enumeration = Enumeration(
    name="Velocity",
    literals={
            EnumerationLiteral(name="very_slow"),
			EnumerationLiteral(name="slow"),
			EnumerationLiteral(name="medium"),
			EnumerationLiteral(name="fast"),
			EnumerationLiteral(name="very_fast")
    }
)

# Classes
model_NamedElement = Class(name="model::NamedElement", is_abstract=True)
model_OzobotProgram = Class(name="model::OzobotProgram")
NamedElement = Class(name="NamedElement")
model_Block = Class(name="model::Block")
model_Command = Class(name="model::Command", is_abstract=True)
model_Transition = Class(name="model::Transition")
model_Move = Class(name="model::Move")
Command = Class(name="Command")
model_Light = Class(name="model::Light")
model_Rotate = Class(name="model::Rotate")
model_Wait = Class(name="model::Wait")
model_Repeat = Class(name="model::Repeat")
model_Ozobot = Class(name="model::Ozobot")

# model_NamedElement class attributes and methods
model_NamedElement_name: Property = Property(name="name", type=StringType)
model_NamedElement.attributes={model_NamedElement_name}

# model_OzobotProgram class attributes and methods

# NamedElement class attributes and methods

# model_Block class attributes and methods

# model_Command class attributes and methods
model_Command_message: Property = Property(name="message", type=StringType)
model_Command.attributes={model_Command_message}

# model_Transition class attributes and methods

# model_Move class attributes and methods
model_Move_distance: Property = Property(name="distance", type=IntegerType)
model_Move_velocity: Property = Property(name="velocity", type=StringType)
model_Move.attributes={model_Move_distance, model_Move_velocity}

# Command class attributes and methods

# model_Light class attributes and methods
model_Light_color: Property = Property(name="color", type=StringType)
model_Light.attributes={model_Light_color}

# model_Rotate class attributes and methods
model_Rotate_direction: Property = Property(name="direction", type=StringType)
model_Rotate_velocity: Property = Property(name="velocity", type=StringType)
model_Rotate_angle: Property = Property(name="angle", type=FloatType)
model_Rotate.attributes={model_Rotate_direction, model_Rotate_velocity, model_Rotate_angle}

# model_Wait class attributes and methods
model_Wait_time: Property = Property(name="time", type=IntegerType)
model_Wait.attributes={model_Wait_time}

# model_Repeat class attributes and methods
model_Repeat_count: Property = Property(name="count", type=IntegerType)
model_Repeat.attributes={model_Repeat_count}

# model_Ozobot class attributes and methods
model_Ozobot_xposition: Property = Property(name="xposition", type=FloatType)
model_Ozobot_yposition: Property = Property(name="yposition", type=FloatType)
model_Ozobot_orientation: Property = Property(name="orientation", type=FloatType)
model_Ozobot.attributes={model_Ozobot_yposition, model_Ozobot_orientation, model_Ozobot_xposition}

# Relationships
block0: BinaryAssociation = BinaryAssociation(
    name="block0",
    ends={
        Property(name="model_Block", type=model_OzobotProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="model_OzobotProgram", type=model_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
current1: BinaryAssociation = BinaryAssociation(
    name="current1",
    ends={
        Property(name="model_Command", type=model_OzobotProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="model_OzobotProgram2", type=model_Command, multiplicity=Multiplicity(1, 1))
    }
)
currentCommand3: BinaryAssociation = BinaryAssociation(
    name="currentCommand3",
    ends={
        Property(name="model_Command5", type=model_OzobotProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="model_OzobotProgram4", type=model_Command, multiplicity=Multiplicity(0, 1))
    }
)
outgoing6: BinaryAssociation = BinaryAssociation(
    name="outgoing6",
    ends={
        Property(name="7", type=model_Command, multiplicity=Multiplicity(1, 1)),
        Property(name="", type=model_Transition, multiplicity=Multiplicity(0, 1))
    }
)
incoming8: BinaryAssociation = BinaryAssociation(
    name="incoming8",
    ends={
        Property(name="10", type=model_Command, multiplicity=Multiplicity(1, 1)),
        Property(name="9", type=model_Transition, multiplicity=Multiplicity(0, 1))
    }
)
block11: BinaryAssociation = BinaryAssociation(
    name="block11",
    ends={
        Property(name="model_Block12", type=model_Repeat, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Repeat", type=model_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
programs13: BinaryAssociation = BinaryAssociation(
    name="programs13",
    ends={
        Property(name="model_OzobotProgram14", type=model_Ozobot, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Ozobot", type=model_OzobotProgram, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
commands15: BinaryAssociation = BinaryAssociation(
    name="commands15",
    ends={
        Property(name="model_Command17", type=model_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Block16", type=model_Command, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions18: BinaryAssociation = BinaryAssociation(
    name="transitions18",
    ends={
        Property(name="model_Transition", type=model_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Block19", type=model_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source20: BinaryAssociation = BinaryAssociation(
    name="source20",
    ends={
        Property(name="22", type=model_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="21", type=model_Command, multiplicity=Multiplicity(1, 1))
    }
)
target23: BinaryAssociation = BinaryAssociation(
    name="target23",
    ends={
        Property(name="25", type=model_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="24", type=model_Command, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_model_OzobotProgram_NamedElement = Generalization(general=NamedElement, specific=model_OzobotProgram)
gen_model_Command_NamedElement = Generalization(general=NamedElement, specific=model_Command)
gen_model_Move_Command = Generalization(general=Command, specific=model_Move)
gen_model_Light_Command = Generalization(general=Command, specific=model_Light)
gen_model_Rotate_Command = Generalization(general=Command, specific=model_Rotate)
gen_model_Wait_Command = Generalization(general=Command, specific=model_Wait)
gen_model_Repeat_Command = Generalization(general=Command, specific=model_Repeat)
gen_model_Ozobot_NamedElement = Generalization(general=NamedElement, specific=model_Ozobot)
gen_model_Block_NamedElement = Generalization(general=NamedElement, specific=model_Block)
gen_model_Transition_NamedElement = Generalization(general=NamedElement, specific=model_Transition)

# Domain Model
domain_model = DomainModel(
    name="model",
    types={model_NamedElement, model_OzobotProgram, NamedElement, model_Block, model_Command, model_Transition, model_Move, Command, model_Light, model_Rotate, model_Wait, model_Repeat, model_Ozobot, Color, Direction, Velocity},
    associations={block0, current1, currentCommand3, outgoing6, incoming8, block11, programs13, commands15, transitions18, source20, target23},
    generalizations={gen_model_OzobotProgram_NamedElement, gen_model_Command_NamedElement, gen_model_Move_Command, gen_model_Light_Command, gen_model_Rotate_Command, gen_model_Wait_Command, gen_model_Repeat_Command, gen_model_Ozobot_NamedElement, gen_model_Block_NamedElement, gen_model_Transition_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)