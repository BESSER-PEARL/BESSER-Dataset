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
arduinoml_Board = Class(name="arduinoml::Board")
arduinoml_State = Class(name="arduinoml::State")
arduinoml_Brick = Class(name="arduinoml::Brick", is_abstract=True)
arduinoml_Action = Class(name="arduinoml::Action", is_abstract=True)
arduinoml_Transition = Class(name="arduinoml::Transition")
arduinoml_Actuator = Class(name="arduinoml::Actuator")
Brick = Class(name="Brick")
arduinoml_ActuatorState = Class(name="arduinoml::ActuatorState")
arduinoml_Sensor = Class(name="arduinoml::Sensor")
arduinoml_Off = Class(name="arduinoml::Off")
Action = Class(name="Action")
arduinoml_On = Class(name="arduinoml::On")

# arduinoml_Board class attributes and methods

# arduinoml_State class attributes and methods
arduinoml_State_name: Property = Property(name="name", type=StringType)
arduinoml_State.attributes={arduinoml_State_name}

# arduinoml_Brick class attributes and methods
arduinoml_Brick_name: Property = Property(name="name", type=StringType)
arduinoml_Brick_pin: Property = Property(name="pin", type=IntegerType)
arduinoml_Brick.attributes={arduinoml_Brick_pin, arduinoml_Brick_name}

# arduinoml_Action class attributes and methods

# arduinoml_Transition class attributes and methods

# arduinoml_Actuator class attributes and methods

# Brick class attributes and methods

# arduinoml_ActuatorState class attributes and methods
arduinoml_ActuatorState_isOn: Property = Property(name="isOn", type=BooleanType)
arduinoml_ActuatorState.attributes={arduinoml_ActuatorState_isOn}

# arduinoml_Sensor class attributes and methods

# arduinoml_Off class attributes and methods
arduinoml_Off_m_turnOff: Method = Method(name="turnOff", parameters={})
arduinoml_Off.methods={arduinoml_Off_m_turnOff}

# Action class attributes and methods

# arduinoml_On class attributes and methods
arduinoml_On_m_turnOn: Method = Method(name="turnOn", parameters={})
arduinoml_On.methods={arduinoml_On_m_turnOn}

# Relationships
bricks4: BinaryAssociation = BinaryAssociation(
    name="bricks4",
    ends={
        Property(name="arduinoml_Brick", type=arduinoml_Board, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoml_Board5", type=arduinoml_Brick, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initial0: BinaryAssociation = BinaryAssociation(
    name="initial0",
    ends={
        Property(name="arduinoml_State", type=arduinoml_Board, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoml_Board", type=arduinoml_State, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
possibles1: BinaryAssociation = BinaryAssociation(
    name="possibles1",
    ends={
        Property(name="arduinoml_State3", type=arduinoml_Board, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoml_Board2", type=arduinoml_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actions6: BinaryAssociation = BinaryAssociation(
    name="actions6",
    ends={
        Property(name="arduinoml_Action", type=arduinoml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoml_State7", type=arduinoml_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eventCode8: BinaryAssociation = BinaryAssociation(
    name="eventCode8",
    ends={
        Property(name="arduinoml_Transition", type=arduinoml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoml_State9", type=arduinoml_Transition, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
state10: BinaryAssociation = BinaryAssociation(
    name="state10",
    ends={
        Property(name="arduinoml_ActuatorState", type=arduinoml_Actuator, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoml_Actuator", type=arduinoml_ActuatorState, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source11: BinaryAssociation = BinaryAssociation(
    name="source11",
    ends={
        Property(name="arduinoml_State13", type=arduinoml_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoml_Transition12", type=arduinoml_State, multiplicity=Multiplicity(1, 1))
    }
)
target14: BinaryAssociation = BinaryAssociation(
    name="target14",
    ends={
        Property(name="arduinoml_State16", type=arduinoml_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoml_Transition15", type=arduinoml_State, multiplicity=Multiplicity(1, 1))
    }
)
target17: BinaryAssociation = BinaryAssociation(
    name="target17",
    ends={
        Property(name="arduinoml_Sensor", type=arduinoml_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoml_Action18", type=arduinoml_Sensor, multiplicity=Multiplicity(1, 1))
    }
)
triggers19: BinaryAssociation = BinaryAssociation(
    name="triggers19",
    ends={
        Property(name="arduinoml_Transition21", type=arduinoml_ActuatorState, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoml_ActuatorState20", type=arduinoml_Transition, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_arduinoml_Actuator_Brick = Generalization(general=Brick, specific=arduinoml_Actuator)
gen_arduinoml_Sensor_Brick = Generalization(general=Brick, specific=arduinoml_Sensor)
gen_arduinoml_Off_Action = Generalization(general=Action, specific=arduinoml_Off)
gen_arduinoml_On_Action = Generalization(general=Action, specific=arduinoml_On)

# Domain Model
domain_model = DomainModel(
    name="arduinoml",
    types={arduinoml_Board, arduinoml_State, arduinoml_Brick, arduinoml_Action, arduinoml_Transition, arduinoml_Actuator, Brick, arduinoml_ActuatorState, arduinoml_Sensor, arduinoml_Off, Action, arduinoml_On},
    associations={bricks4, initial0, possibles1, actions6, eventCode8, state10, source11, target14, target17, triggers19},
    generalizations={gen_arduinoml_Actuator_Brick, gen_arduinoml_Sensor_Brick, gen_arduinoml_Off_Action, gen_arduinoml_On_Action},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)