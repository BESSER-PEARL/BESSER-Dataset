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
DigitalValue: Enumeration = Enumeration(
    name="DigitalValue",
    literals={
            EnumerationLiteral(name="ON"),
			EnumerationLiteral(name="OFF")
    }
)

# Classes
arduinoml_Off = Class(name="arduinoml::Off")
Action = Class(name="Action")
arduinoml_On = Class(name="arduinoml::On")
arduinoml_Wait = Class(name="arduinoml::Wait")
arduinoml_Board = Class(name="arduinoml::Board")
arduinoml_State = Class(name="arduinoml::State")
arduinoml_Brick = Class(name="arduinoml::Brick", is_abstract=True)
NamedElement = Class(name="NamedElement")
arduinoml_Action = Class(name="arduinoml::Action", is_abstract=True)
arduinoml_Transition = Class(name="arduinoml::Transition")
arduinoml_Sensor = Class(name="arduinoml::Sensor")
Brick = Class(name="Brick")
arduinoml_Actuator = Class(name="arduinoml::Actuator")
arduinoml_Trigger = Class(name="arduinoml::Trigger")
arduinoml_NamedElement = Class(name="arduinoml::NamedElement", is_abstract=True)

# arduinoml_Off class attributes and methods

# Action class attributes and methods

# arduinoml_On class attributes and methods

# arduinoml_Wait class attributes and methods
arduinoml_Wait_waitingTime: Property = Property(name="waitingTime", type=IntegerType)
arduinoml_Wait.attributes={arduinoml_Wait_waitingTime}

# arduinoml_Board class attributes and methods

# arduinoml_State class attributes and methods

# arduinoml_Brick class attributes and methods
arduinoml_Brick_pin: Property = Property(name="pin", type=IntegerType)
arduinoml_Brick.attributes={arduinoml_Brick_pin}

# NamedElement class attributes and methods

# arduinoml_Action class attributes and methods

# arduinoml_Transition class attributes and methods

# arduinoml_Sensor class attributes and methods

# Brick class attributes and methods

# arduinoml_Actuator class attributes and methods

# arduinoml_Trigger class attributes and methods
arduinoml_Trigger_value: Property = Property(name="value", type=StringType)
arduinoml_Trigger.attributes={arduinoml_Trigger_value}

# arduinoml_NamedElement class attributes and methods
arduinoml_NamedElement_name: Property = Property(name="name", type=StringType)
arduinoml_NamedElement.attributes={arduinoml_NamedElement_name}

# Relationships
initial0: BinaryAssociation = BinaryAssociation(
    name="initial0",
    ends={
        Property(name="arduinoml_State", type=arduinoml_Board, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoml_Board", type=arduinoml_State, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
alternatives1: BinaryAssociation = BinaryAssociation(
    name="alternatives1",
    ends={
        Property(name="arduinoml_State3", type=arduinoml_Board, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoml_Board2", type=arduinoml_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bricks4: BinaryAssociation = BinaryAssociation(
    name="bricks4",
    ends={
        Property(name="arduinoml_Brick", type=arduinoml_Board, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoml_Board5", type=arduinoml_Brick, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
actions6: BinaryAssociation = BinaryAssociation(
    name="actions6",
    ends={
        Property(name="arduinoml_Action", type=arduinoml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoml_State7", type=arduinoml_Action, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
eventCode8: BinaryAssociation = BinaryAssociation(
    name="eventCode8",
    ends={
        Property(name="Transition", type=arduinoml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=arduinoml_Transition, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
target9: BinaryAssociation = BinaryAssociation(
    name="target9",
    ends={
        Property(name="arduinoml_State10", type=arduinoml_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoml_Transition", type=arduinoml_State, multiplicity=Multiplicity(1, 1))
    }
)
trigger11: BinaryAssociation = BinaryAssociation(
    name="trigger11",
    ends={
        Property(name="arduinoml_Trigger", type=arduinoml_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoml_Transition12", type=arduinoml_Trigger, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source13: BinaryAssociation = BinaryAssociation(
    name="source13",
    ends={
        Property(name="State", type=arduinoml_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="eventCode", type=arduinoml_State, multiplicity=Multiplicity(1, 1))
    }
)
actuators14: BinaryAssociation = BinaryAssociation(
    name="actuators14",
    ends={
        Property(name="arduinoml_Actuator", type=arduinoml_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoml_Action15", type=arduinoml_Actuator, multiplicity=Multiplicity(1, 9999))
    }
)
sensors16: BinaryAssociation = BinaryAssociation(
    name="sensors16",
    ends={
        Property(name="arduinoml_Sensor", type=arduinoml_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoml_Trigger17", type=arduinoml_Sensor, multiplicity=Multiplicity(1, 9999))
    }
)

# Generalizations
gen_arduinoml_Off_Action = Generalization(general=Action, specific=arduinoml_Off)
gen_arduinoml_On_Action = Generalization(general=Action, specific=arduinoml_On)
gen_arduinoml_State_NamedElement = Generalization(general=NamedElement, specific=arduinoml_State)
gen_arduinoml_Brick_NamedElement = Generalization(general=NamedElement, specific=arduinoml_Brick)
gen_arduinoml_Sensor_Brick = Generalization(general=Brick, specific=arduinoml_Sensor)
gen_arduinoml_Actuator_Brick = Generalization(general=Brick, specific=arduinoml_Actuator)
gen_arduinoml_Transition_NamedElement = Generalization(general=NamedElement, specific=arduinoml_Transition)
gen_arduinoml_Wait_Action = Generalization(general=Action, specific=arduinoml_Wait)

# Domain Model
domain_model = DomainModel(
    name="arduinoml",
    types={arduinoml_Off, Action, arduinoml_On, arduinoml_Wait, arduinoml_Board, arduinoml_State, arduinoml_Brick, NamedElement, arduinoml_Action, arduinoml_Transition, arduinoml_Sensor, Brick, arduinoml_Actuator, arduinoml_Trigger, arduinoml_NamedElement, DigitalValue},
    associations={initial0, alternatives1, bricks4, actions6, eventCode8, target9, trigger11, source13, actuators14, sensors16},
    generalizations={gen_arduinoml_Off_Action, gen_arduinoml_On_Action, gen_arduinoml_State_NamedElement, gen_arduinoml_Brick_NamedElement, gen_arduinoml_Sensor_Brick, gen_arduinoml_Actuator_Brick, gen_arduinoml_Transition_NamedElement, gen_arduinoml_Wait_Action},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)