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
ArduinoCard_State = Class(name="ArduinoCard::State")
ArduinoCard_Transition = Class(name="ArduinoCard::Transition")
ArduinoCard_Command = Class(name="ArduinoCard::Command")
ArduinoCard_Block = Class(name="ArduinoCard::Block", is_abstract=True)
ArduinoCard_Sensor = Class(name="ArduinoCard::Sensor")
Block = Class(name="Block")
ArduinoCard_Actuator = Class(name="ArduinoCard::Actuator")
ArduinoCard_Condition = Class(name="ArduinoCard::Condition")
BlockInteraction = Class(name="BlockInteraction")
ArduinoCard_Card = Class(name="ArduinoCard::Card")
ArduinoCard_BlockInteraction = Class(name="ArduinoCard::BlockInteraction", is_abstract=True)

# ArduinoCard_State class attributes and methods
ArduinoCard_State_name: Property = Property(name="name", type=StringType)
ArduinoCard_State_isInitial: Property = Property(name="isInitial", type=BooleanType)
ArduinoCard_State.attributes={ArduinoCard_State_isInitial, ArduinoCard_State_name}

# ArduinoCard_Transition class attributes and methods
ArduinoCard_Transition_name: Property = Property(name="name", type=StringType)
ArduinoCard_Transition.attributes={ArduinoCard_Transition_name}

# ArduinoCard_Command class attributes and methods

# ArduinoCard_Block class attributes and methods
ArduinoCard_Block_name: Property = Property(name="name", type=StringType)
ArduinoCard_Block_pinNumber: Property = Property(name="pinNumber", type=IntegerType)
ArduinoCard_Block_isAnalogic: Property = Property(name="isAnalogic", type=StringType)
ArduinoCard_Block.attributes={ArduinoCard_Block_pinNumber, ArduinoCard_Block_isAnalogic, ArduinoCard_Block_name}

# ArduinoCard_Sensor class attributes and methods

# Block class attributes and methods

# ArduinoCard_Actuator class attributes and methods

# ArduinoCard_Condition class attributes and methods

# BlockInteraction class attributes and methods

# ArduinoCard_Card class attributes and methods

# ArduinoCard_BlockInteraction class attributes and methods
ArduinoCard_BlockInteraction_isHigh: Property = Property(name="isHigh", type=BooleanType)
ArduinoCard_BlockInteraction_name: Property = Property(name="name", type=StringType)
ArduinoCard_BlockInteraction.attributes={ArduinoCard_BlockInteraction_isHigh, ArduinoCard_BlockInteraction_name}

# Relationships
Transitions0: BinaryAssociation = BinaryAssociation(
    name="Transitions0",
    ends={
        Property(name="ArduinoCard_Transition", type=ArduinoCard_State, multiplicity=Multiplicity(1, 1)),
        Property(name="ArduinoCard_State", type=ArduinoCard_Transition, multiplicity=Multiplicity(1, 9999))
    }
)
Command1: BinaryAssociation = BinaryAssociation(
    name="Command1",
    ends={
        Property(name="ArduinoCard_Command", type=ArduinoCard_State, multiplicity=Multiplicity(1, 1)),
        Property(name="ArduinoCard_State2", type=ArduinoCard_Command, multiplicity=Multiplicity(1, 9999))
    }
)
Sensor3: BinaryAssociation = BinaryAssociation(
    name="Sensor3",
    ends={
        Property(name="ArduinoCard_Sensor", type=ArduinoCard_Condition, multiplicity=Multiplicity(1, 1)),
        Property(name="ArduinoCard_Condition", type=ArduinoCard_Sensor, multiplicity=Multiplicity(1, 1))
    }
)
nextState4: BinaryAssociation = BinaryAssociation(
    name="nextState4",
    ends={
        Property(name="ArduinoCard_State6", type=ArduinoCard_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="ArduinoCard_Transition5", type=ArduinoCard_State, multiplicity=Multiplicity(1, 1))
    }
)
Condition7: BinaryAssociation = BinaryAssociation(
    name="Condition7",
    ends={
        Property(name="ArduinoCard_Condition9", type=ArduinoCard_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="ArduinoCard_Transition8", type=ArduinoCard_Condition, multiplicity=Multiplicity(1, 9999))
    }
)
Actuator10: BinaryAssociation = BinaryAssociation(
    name="Actuator10",
    ends={
        Property(name="ArduinoCard_Actuator", type=ArduinoCard_Command, multiplicity=Multiplicity(1, 1)),
        Property(name="ArduinoCard_Command11", type=ArduinoCard_Actuator, multiplicity=Multiplicity(1, 1))
    }
)
States12: BinaryAssociation = BinaryAssociation(
    name="States12",
    ends={
        Property(name="ArduinoCard_State13", type=ArduinoCard_Card, multiplicity=Multiplicity(1, 1)),
        Property(name="ArduinoCard_Card", type=ArduinoCard_State, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
Transitions14: BinaryAssociation = BinaryAssociation(
    name="Transitions14",
    ends={
        Property(name="ArduinoCard_Transition16", type=ArduinoCard_Card, multiplicity=Multiplicity(1, 1)),
        Property(name="ArduinoCard_Card15", type=ArduinoCard_Transition, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
BlockInteractions17: BinaryAssociation = BinaryAssociation(
    name="BlockInteractions17",
    ends={
        Property(name="ArduinoCard_BlockInteraction", type=ArduinoCard_Card, multiplicity=Multiplicity(1, 1)),
        Property(name="ArduinoCard_Card18", type=ArduinoCard_BlockInteraction, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
Blocks19: BinaryAssociation = BinaryAssociation(
    name="Blocks19",
    ends={
        Property(name="ArduinoCard_Block", type=ArduinoCard_Card, multiplicity=Multiplicity(1, 1)),
        Property(name="ArduinoCard_Card20", type=ArduinoCard_Block, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)

# Generalizations
gen_ArduinoCard_Sensor_Block = Generalization(general=Block, specific=ArduinoCard_Sensor)
gen_ArduinoCard_Actuator_Block = Generalization(general=Block, specific=ArduinoCard_Actuator)
gen_ArduinoCard_Condition_BlockInteraction = Generalization(general=BlockInteraction, specific=ArduinoCard_Condition)
gen_ArduinoCard_Command_BlockInteraction = Generalization(general=BlockInteraction, specific=ArduinoCard_Command)

# Domain Model
domain_model = DomainModel(
    name="ArduinoCard",
    types={ArduinoCard_State, ArduinoCard_Transition, ArduinoCard_Command, ArduinoCard_Block, ArduinoCard_Sensor, Block, ArduinoCard_Actuator, ArduinoCard_Condition, BlockInteraction, ArduinoCard_Card, ArduinoCard_BlockInteraction},
    associations={Transitions0, Command1, Sensor3, nextState4, Condition7, Actuator10, States12, Transitions14, BlockInteractions17, Blocks19},
    generalizations={gen_ArduinoCard_Sensor_Block, gen_ArduinoCard_Actuator_Block, gen_ArduinoCard_Condition_BlockInteraction, gen_ArduinoCard_Command_BlockInteraction},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)