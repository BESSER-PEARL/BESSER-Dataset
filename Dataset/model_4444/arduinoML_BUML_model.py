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

Time_unit: Enumeration = Enumeration(
    name="Time_unit",
    literals={
            EnumerationLiteral(name="ms"),
			EnumerationLiteral(name="s"),
			EnumerationLiteral(name="min")
    }
)

Compare: Enumeration = Enumeration(
    name="Compare",
    literals={
            EnumerationLiteral(name="inf"),
			EnumerationLiteral(name="einf"),
			EnumerationLiteral(name="equal"),
			EnumerationLiteral(name="esup"),
			EnumerationLiteral(name="sup")
    }
)

# Classes
arduinoML_State = Class(name="arduinoML::State")
arduinoML_Action = Class(name="arduinoML::Action")
arduinoML_TransitionState = Class(name="arduinoML::TransitionState")
arduinoML_Transition = Class(name="arduinoML::Transition", is_abstract=True)
arduinoML_Brick = Class(name="arduinoML::Brick", is_abstract=True)
NamedElement = Class(name="NamedElement")
arduinoML_Actuator = Class(name="arduinoML::Actuator")
Brick = Class(name="Brick")
arduinoML_Digital = Class(name="arduinoML::Digital")
arduinoML_App = Class(name="arduinoML::App")
arduinoML_Mode = Class(name="arduinoML::Mode")
arduinoML_TransitionMode = Class(name="arduinoML::TransitionMode")
Transition = Class(name="Transition")
arduinoML_Analog = Class(name="arduinoML::Analog")
arduinoML_NamedElement = Class(name="arduinoML::NamedElement", is_abstract=True)

# arduinoML_State class attributes and methods

# arduinoML_Action class attributes and methods
arduinoML_Action_value: Property = Property(name="value", type=StringType)
arduinoML_Action.attributes={arduinoML_Action_value}

# arduinoML_TransitionState class attributes and methods

# arduinoML_Transition class attributes and methods
arduinoML_Transition_d_values: Property = Property(name="d_values", type=StringType)
arduinoML_Transition_time: Property = Property(name="time", type=IntegerType)
arduinoML_Transition_unit: Property = Property(name="unit", type=StringType)
arduinoML_Transition_a_values: Property = Property(name="a_values", type=IntegerType)
arduinoML_Transition_comp: Property = Property(name="comp", type=StringType)
arduinoML_Transition.attributes={arduinoML_Transition_a_values, arduinoML_Transition_d_values, arduinoML_Transition_comp, arduinoML_Transition_unit, arduinoML_Transition_time}

# arduinoML_Brick class attributes and methods
arduinoML_Brick_pin: Property = Property(name="pin", type=IntegerType)
arduinoML_Brick.attributes={arduinoML_Brick_pin}

# NamedElement class attributes and methods

# arduinoML_Actuator class attributes and methods

# Brick class attributes and methods

# arduinoML_Digital class attributes and methods

# arduinoML_App class attributes and methods
arduinoML_App_monitoring: Property = Property(name="monitoring", type=BooleanType)
arduinoML_App.attributes={arduinoML_App_monitoring}

# arduinoML_Mode class attributes and methods

# arduinoML_TransitionMode class attributes and methods

# Transition class attributes and methods

# arduinoML_Analog class attributes and methods
arduinoML_Analog_debug: Property = Property(name="debug", type=BooleanType)
arduinoML_Analog.attributes={arduinoML_Analog_debug}

# arduinoML_NamedElement class attributes and methods
arduinoML_NamedElement_name: Property = Property(name="name", type=StringType)
arduinoML_NamedElement.attributes={arduinoML_NamedElement_name}

# Relationships
modes1: BinaryAssociation = BinaryAssociation(
    name="modes1",
    ends={
        Property(name="arduinoML_Mode3", type=arduinoML_App, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoML_App2", type=arduinoML_Mode, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
bricks4: BinaryAssociation = BinaryAssociation(
    name="bricks4",
    ends={
        Property(name="arduinoML_Brick", type=arduinoML_App, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoML_App5", type=arduinoML_Brick, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
actions6: BinaryAssociation = BinaryAssociation(
    name="actions6",
    ends={
        Property(name="arduinoML_Action", type=arduinoML_State, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoML_State", type=arduinoML_Action, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
transitions_state7: BinaryAssociation = BinaryAssociation(
    name="transitions_state7",
    ends={
        Property(name="TransitionState", type=arduinoML_State, multiplicity=Multiplicity(1, 1)),
        Property(name="state", type=arduinoML_TransitionState, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
actuator8: BinaryAssociation = BinaryAssociation(
    name="actuator8",
    ends={
        Property(name="arduinoML_Actuator", type=arduinoML_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoML_Action9", type=arduinoML_Actuator, multiplicity=Multiplicity(1, 1))
    }
)
digitals10: BinaryAssociation = BinaryAssociation(
    name="digitals10",
    ends={
        Property(name="arduinoML_Digital", type=arduinoML_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoML_Transition", type=arduinoML_Digital, multiplicity=Multiplicity(0, 9999))
    }
)
initial_mode0: BinaryAssociation = BinaryAssociation(
    name="initial_mode0",
    ends={
        Property(name="arduinoML_Mode", type=arduinoML_App, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoML_App", type=arduinoML_Mode, multiplicity=Multiplicity(0, 1))
    }
)
bricks13: BinaryAssociation = BinaryAssociation(
    name="bricks13",
    ends={
        Property(name="arduinoML_Brick15", type=arduinoML_Mode, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoML_Mode14", type=arduinoML_Brick, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
states16: BinaryAssociation = BinaryAssociation(
    name="states16",
    ends={
        Property(name="arduinoML_State18", type=arduinoML_Mode, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoML_Mode17", type=arduinoML_State, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
initial19: BinaryAssociation = BinaryAssociation(
    name="initial19",
    ends={
        Property(name="arduinoML_State21", type=arduinoML_Mode, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoML_Mode20", type=arduinoML_State, multiplicity=Multiplicity(1, 1))
    }
)
transitions_mode22: BinaryAssociation = BinaryAssociation(
    name="transitions_mode22",
    ends={
        Property(name="TransitionMode", type=arduinoML_Mode, multiplicity=Multiplicity(1, 1)),
        Property(name="mode", type=arduinoML_TransitionMode, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
next_state23: BinaryAssociation = BinaryAssociation(
    name="next_state23",
    ends={
        Property(name="arduinoML_State24", type=arduinoML_TransitionState, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoML_TransitionState", type=arduinoML_State, multiplicity=Multiplicity(1, 1))
    }
)
state25: BinaryAssociation = BinaryAssociation(
    name="state25",
    ends={
        Property(name="State", type=arduinoML_TransitionState, multiplicity=Multiplicity(1, 1)),
        Property(name="transitions_state", type=arduinoML_State, multiplicity=Multiplicity(1, 1))
    }
)
mode26: BinaryAssociation = BinaryAssociation(
    name="mode26",
    ends={
        Property(name="Mode", type=arduinoML_TransitionMode, multiplicity=Multiplicity(1, 1)),
        Property(name="transitions_mode", type=arduinoML_Mode, multiplicity=Multiplicity(1, 1))
    }
)
next_mode27: BinaryAssociation = BinaryAssociation(
    name="next_mode27",
    ends={
        Property(name="arduinoML_Mode28", type=arduinoML_TransitionMode, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoML_TransitionMode", type=arduinoML_Mode, multiplicity=Multiplicity(1, 1))
    }
)
analogs11: BinaryAssociation = BinaryAssociation(
    name="analogs11",
    ends={
        Property(name="arduinoML_Analog", type=arduinoML_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoML_Transition12", type=arduinoML_Analog, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_arduinoML_State_NamedElement = Generalization(general=NamedElement, specific=arduinoML_State)
gen_arduinoML_Brick_NamedElement = Generalization(general=NamedElement, specific=arduinoML_Brick)
gen_arduinoML_Actuator_Brick = Generalization(general=Brick, specific=arduinoML_Actuator)
gen_arduinoML_Digital_Brick = Generalization(general=Brick, specific=arduinoML_Digital)
gen_arduinoML_App_NamedElement = Generalization(general=NamedElement, specific=arduinoML_App)
gen_arduinoML_Mode_NamedElement = Generalization(general=NamedElement, specific=arduinoML_Mode)
gen_arduinoML_TransitionState_Transition = Generalization(general=Transition, specific=arduinoML_TransitionState)
gen_arduinoML_TransitionMode_Transition = Generalization(general=Transition, specific=arduinoML_TransitionMode)
gen_arduinoML_Analog_Brick = Generalization(general=Brick, specific=arduinoML_Analog)

# Domain Model
domain_model = DomainModel(
    name="arduinoML",
    types={arduinoML_State, arduinoML_Action, arduinoML_TransitionState, arduinoML_Transition, arduinoML_Brick, NamedElement, arduinoML_Actuator, Brick, arduinoML_Digital, arduinoML_App, arduinoML_Mode, arduinoML_TransitionMode, Transition, arduinoML_Analog, arduinoML_NamedElement, Signal, Time_unit, Compare},
    associations={modes1, bricks4, actions6, transitions_state7, actuator8, digitals10, initial_mode0, bricks13, states16, initial19, transitions_mode22, next_state23, state25, mode26, next_mode27, analogs11},
    generalizations={gen_arduinoML_State_NamedElement, gen_arduinoML_Brick_NamedElement, gen_arduinoML_Actuator_Brick, gen_arduinoML_Digital_Brick, gen_arduinoML_App_NamedElement, gen_arduinoML_Mode_NamedElement, gen_arduinoML_TransitionState_Transition, gen_arduinoML_TransitionMode_Transition, gen_arduinoML_Analog_Brick},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)