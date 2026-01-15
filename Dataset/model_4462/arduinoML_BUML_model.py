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
DigitalSignalEnum: Enumeration = Enumeration(
    name="DigitalSignalEnum",
    literals={
            EnumerationLiteral(name="HIGH"),
			EnumerationLiteral(name="LOW")
    }
)

Operator: Enumeration = Enumeration(
    name="Operator",
    literals={
            EnumerationLiteral(name="AND"),
			EnumerationLiteral(name="OR"),
			EnumerationLiteral(name="NONE")
    }
)

# Classes
arduinoML_Brick = Class(name="arduinoML::Brick", is_abstract=True)
NamedElement = Class(name="NamedElement")
arduinoML_Actuator = Class(name="arduinoML::Actuator")
Brick = Class(name="Brick")
arduinoML_Sensor = Class(name="arduinoML::Sensor")
arduinoML_App = Class(name="arduinoML::App")
arduinoML_State = Class(name="arduinoML::State")
arduinoML_NamedElement = Class(name="arduinoML::NamedElement", is_abstract=True)
arduinoML_Action = Class(name="arduinoML::Action")
arduinoML_Transition = Class(name="arduinoML::Transition")
arduinoML_Signal = Class(name="arduinoML::Signal", is_abstract=True)
arduinoML_LCDScreenActuator = Class(name="arduinoML::LCDScreenActuator")
Actuator = Class(name="Actuator")
arduinoML_DigitalSignal = Class(name="arduinoML::DigitalSignal")
Signal = Class(name="Signal")
arduinoML_StringSignal = Class(name="arduinoML::StringSignal")
arduinoML_KeyboardSensor = Class(name="arduinoML::KeyboardSensor")
Sensor = Class(name="Sensor")
arduinoML_Condition = Class(name="arduinoML::Condition")

# arduinoML_Brick class attributes and methods
arduinoML_Brick_pins: Property = Property(name="pins", type=IntegerType)
arduinoML_Brick.attributes={arduinoML_Brick_pins}

# NamedElement class attributes and methods

# arduinoML_Actuator class attributes and methods

# Brick class attributes and methods

# arduinoML_Sensor class attributes and methods

# arduinoML_App class attributes and methods
arduinoML_App_name: Property = Property(name="name", type=StringType)
arduinoML_App.attributes={arduinoML_App_name}

# arduinoML_State class attributes and methods

# arduinoML_NamedElement class attributes and methods
arduinoML_NamedElement_name: Property = Property(name="name", type=StringType)
arduinoML_NamedElement.attributes={arduinoML_NamedElement_name}

# arduinoML_Action class attributes and methods

# arduinoML_Transition class attributes and methods

# arduinoML_Signal class attributes and methods

# arduinoML_LCDScreenActuator class attributes and methods

# Actuator class attributes and methods

# arduinoML_DigitalSignal class attributes and methods
arduinoML_DigitalSignal_value: Property = Property(name="value", type=StringType)
arduinoML_DigitalSignal.attributes={arduinoML_DigitalSignal_value}

# Signal class attributes and methods

# arduinoML_StringSignal class attributes and methods
arduinoML_StringSignal_value: Property = Property(name="value", type=StringType)
arduinoML_StringSignal.attributes={arduinoML_StringSignal_value}

# arduinoML_KeyboardSensor class attributes and methods

# Sensor class attributes and methods

# arduinoML_Condition class attributes and methods
arduinoML_Condition_operator: Property = Property(name="operator", type=StringType)
arduinoML_Condition.attributes={arduinoML_Condition_operator}

# Relationships
bricks0: BinaryAssociation = BinaryAssociation(
    name="bricks0",
    ends={
        Property(name="arduinoML_Brick", type=arduinoML_App, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoML_App", type=arduinoML_Brick, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
states1: BinaryAssociation = BinaryAssociation(
    name="states1",
    ends={
        Property(name="arduinoML_State", type=arduinoML_App, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoML_App2", type=arduinoML_State, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
initial3: BinaryAssociation = BinaryAssociation(
    name="initial3",
    ends={
        Property(name="arduinoML_State5", type=arduinoML_App, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoML_App4", type=arduinoML_State, multiplicity=Multiplicity(1, 1))
    }
)
actions6: BinaryAssociation = BinaryAssociation(
    name="actions6",
    ends={
        Property(name="arduinoML_Action", type=arduinoML_State, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoML_State7", type=arduinoML_Action, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
transition8: BinaryAssociation = BinaryAssociation(
    name="transition8",
    ends={
        Property(name="arduinoML_Transition", type=arduinoML_State, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoML_State9", type=arduinoML_Transition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
actuator10: BinaryAssociation = BinaryAssociation(
    name="actuator10",
    ends={
        Property(name="arduinoML_Actuator", type=arduinoML_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoML_Action11", type=arduinoML_Actuator, multiplicity=Multiplicity(1, 1))
    }
)
value12: BinaryAssociation = BinaryAssociation(
    name="value12",
    ends={
        Property(name="arduinoML_Signal", type=arduinoML_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoML_Action13", type=arduinoML_Signal, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
next14: BinaryAssociation = BinaryAssociation(
    name="next14",
    ends={
        Property(name="arduinoML_State16", type=arduinoML_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoML_Transition15", type=arduinoML_State, multiplicity=Multiplicity(1, 1))
    }
)
signal21: BinaryAssociation = BinaryAssociation(
    name="signal21",
    ends={
        Property(name="arduinoML_Signal23", type=arduinoML_Condition, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoML_Condition22", type=arduinoML_Signal, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
conditions17: BinaryAssociation = BinaryAssociation(
    name="conditions17",
    ends={
        Property(name="arduinoML_Condition", type=arduinoML_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoML_Transition18", type=arduinoML_Condition, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
sensor19: BinaryAssociation = BinaryAssociation(
    name="sensor19",
    ends={
        Property(name="arduinoML_Sensor", type=arduinoML_Condition, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoML_Condition20", type=arduinoML_Sensor, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_arduinoML_Brick_NamedElement = Generalization(general=NamedElement, specific=arduinoML_Brick)
gen_arduinoML_Actuator_Brick = Generalization(general=Brick, specific=arduinoML_Actuator)
gen_arduinoML_Sensor_Brick = Generalization(general=Brick, specific=arduinoML_Sensor)
gen_arduinoML_State_NamedElement = Generalization(general=NamedElement, specific=arduinoML_State)
gen_arduinoML_LCDScreenActuator_Actuator = Generalization(general=Actuator, specific=arduinoML_LCDScreenActuator)
gen_arduinoML_DigitalSignal_Signal = Generalization(general=Signal, specific=arduinoML_DigitalSignal)
gen_arduinoML_StringSignal_Signal = Generalization(general=Signal, specific=arduinoML_StringSignal)
gen_arduinoML_KeyboardSensor_Sensor = Generalization(general=Sensor, specific=arduinoML_KeyboardSensor)
gen_arduinoML_Condition_NamedElement = Generalization(general=NamedElement, specific=arduinoML_Condition)

# Domain Model
domain_model = DomainModel(
    name="arduinoML",
    types={arduinoML_Brick, NamedElement, arduinoML_Actuator, Brick, arduinoML_Sensor, arduinoML_App, arduinoML_State, arduinoML_NamedElement, arduinoML_Action, arduinoML_Transition, arduinoML_Signal, arduinoML_LCDScreenActuator, Actuator, arduinoML_DigitalSignal, Signal, arduinoML_StringSignal, arduinoML_KeyboardSensor, Sensor, arduinoML_Condition, DigitalSignalEnum, Operator},
    associations={bricks0, states1, initial3, actions6, transition8, actuator10, value12, next14, signal21, conditions17, sensor19},
    generalizations={gen_arduinoML_Brick_NamedElement, gen_arduinoML_Actuator_Brick, gen_arduinoML_Sensor_Brick, gen_arduinoML_State_NamedElement, gen_arduinoML_LCDScreenActuator_Actuator, gen_arduinoML_DigitalSignal_Signal, gen_arduinoML_StringSignal_Signal, gen_arduinoML_KeyboardSensor_Sensor, gen_arduinoML_Condition_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)