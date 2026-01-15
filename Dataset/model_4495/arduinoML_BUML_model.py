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
Signal: Enumeration = Enumeration(
    name="Signal",
    literals={
            EnumerationLiteral(name="HIGH"),
			EnumerationLiteral(name="LOW")
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
arduinoML_Transition = Class(name="arduinoML::Transition")
arduinoML_NamedElement = Class(name="arduinoML::NamedElement", is_abstract=True)
arduinoML_Action = Class(name="arduinoML::Action")

# arduinoML_Brick class attributes and methods
arduinoML_Brick_pin: Property = Property(name="pin", type=IntegerType)
arduinoML_Brick.attributes={arduinoML_Brick_pin}

# NamedElement class attributes and methods

# arduinoML_Actuator class attributes and methods

# Brick class attributes and methods

# arduinoML_Sensor class attributes and methods

# arduinoML_App class attributes and methods

# arduinoML_State class attributes and methods

# arduinoML_Transition class attributes and methods
arduinoML_Transition_value: Property = Property(name="value", type=StringType)
arduinoML_Transition.attributes={arduinoML_Transition_value}

# arduinoML_NamedElement class attributes and methods
arduinoML_NamedElement_name: Property = Property(name="name", type=StringType)
arduinoML_NamedElement.attributes={arduinoML_NamedElement_name}

# arduinoML_Action class attributes and methods
arduinoML_Action_value: Property = Property(name="value", type=StringType)
arduinoML_Action.attributes={arduinoML_Action_value}

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
transition8: BinaryAssociation = BinaryAssociation(
    name="transition8",
    ends={
        Property(name="Transition", type=arduinoML_State, multiplicity=Multiplicity(1, 1)),
        Property(name="state", type=arduinoML_Transition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
actuator9: BinaryAssociation = BinaryAssociation(
    name="actuator9",
    ends={
        Property(name="arduinoML_Actuator", type=arduinoML_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoML_Action10", type=arduinoML_Actuator, multiplicity=Multiplicity(1, 1))
    }
)
next11: BinaryAssociation = BinaryAssociation(
    name="next11",
    ends={
        Property(name="arduinoML_State12", type=arduinoML_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoML_Transition", type=arduinoML_State, multiplicity=Multiplicity(1, 1))
    }
)
sensor13: BinaryAssociation = BinaryAssociation(
    name="sensor13",
    ends={
        Property(name="arduinoML_Sensor", type=arduinoML_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoML_Transition14", type=arduinoML_Sensor, multiplicity=Multiplicity(1, 1))
    }
)
state15: BinaryAssociation = BinaryAssociation(
    name="state15",
    ends={
        Property(name="State", type=arduinoML_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transition", type=arduinoML_State, multiplicity=Multiplicity(1, 1))
    }
)
actions6: BinaryAssociation = BinaryAssociation(
    name="actions6",
    ends={
        Property(name="arduinoML_Action", type=arduinoML_State, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoML_State7", type=arduinoML_Action, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)

# Generalizations
gen_arduinoML_Brick_NamedElement = Generalization(general=NamedElement, specific=arduinoML_Brick)
gen_arduinoML_Actuator_Brick = Generalization(general=Brick, specific=arduinoML_Actuator)
gen_arduinoML_Sensor_Brick = Generalization(general=Brick, specific=arduinoML_Sensor)
gen_arduinoML_App_NamedElement = Generalization(general=NamedElement, specific=arduinoML_App)
gen_arduinoML_State_NamedElement = Generalization(general=NamedElement, specific=arduinoML_State)

# Domain Model
domain_model = DomainModel(
    name="arduinoML",
    types={arduinoML_Brick, NamedElement, arduinoML_Actuator, Brick, arduinoML_Sensor, arduinoML_App, arduinoML_State, arduinoML_Transition, arduinoML_NamedElement, arduinoML_Action, Signal},
    associations={bricks0, states1, initial3, transition8, actuator9, next11, sensor13, state15, actions6},
    generalizations={gen_arduinoML_Brick_NamedElement, gen_arduinoML_Actuator_Brick, gen_arduinoML_Sensor_Brick, gen_arduinoML_App_NamedElement, gen_arduinoML_State_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)