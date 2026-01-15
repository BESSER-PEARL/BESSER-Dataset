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
statemachine_Statemachine = Class(name="statemachine::Statemachine")
statemachine_InputSignal = Class(name="statemachine::InputSignal")
Signal = Class(name="Signal")
statemachine_OutputSignal = Class(name="statemachine::OutputSignal")
statemachine_Command = Class(name="statemachine::Command")
statemachine_Transition = Class(name="statemachine::Transition")
statemachine_Signal = Class(name="statemachine::Signal")
statemachine_State = Class(name="statemachine::State")
statemachine_Event = Class(name="statemachine::Event")
statemachine_Condition = Class(name="statemachine::Condition")

# statemachine_Statemachine class attributes and methods

# statemachine_InputSignal class attributes and methods

# Signal class attributes and methods

# statemachine_OutputSignal class attributes and methods

# statemachine_Command class attributes and methods
statemachine_Command_newValue: Property = Property(name="newValue", type=BooleanType)
statemachine_Command.attributes={statemachine_Command_newValue}

# statemachine_Transition class attributes and methods

# statemachine_Signal class attributes and methods
statemachine_Signal_name: Property = Property(name="name", type=StringType)
statemachine_Signal.attributes={statemachine_Signal_name}

# statemachine_State class attributes and methods
statemachine_State_name: Property = Property(name="name", type=StringType)
statemachine_State.attributes={statemachine_State_name}

# statemachine_Event class attributes and methods
statemachine_Event_value: Property = Property(name="value", type=BooleanType)
statemachine_Event.attributes={statemachine_Event_value}

# statemachine_Condition class attributes and methods

# Relationships
states1: BinaryAssociation = BinaryAssociation(
    name="states1",
    ends={
        Property(name="statemachine_State", type=statemachine_Statemachine, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_Statemachine2", type=statemachine_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
commands3: BinaryAssociation = BinaryAssociation(
    name="commands3",
    ends={
        Property(name="statemachine_Command", type=statemachine_State, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_State4", type=statemachine_Command, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions5: BinaryAssociation = BinaryAssociation(
    name="transitions5",
    ends={
        Property(name="statemachine_Transition", type=statemachine_State, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_State6", type=statemachine_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nestedStates8: BinaryAssociation = BinaryAssociation(
    name="nestedStates8",
    ends={
        Property(name="statemachine_State9", type=statemachine_State, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_State7", type=statemachine_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
signals0: BinaryAssociation = BinaryAssociation(
    name="signals0",
    ends={
        Property(name="statemachine_Signal", type=statemachine_Statemachine, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_Statemachine", type=statemachine_Signal, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
state12: BinaryAssociation = BinaryAssociation(
    name="state12",
    ends={
        Property(name="statemachine_Transition13", type=statemachine_State, multiplicity=Multiplicity(0, 1)),
        Property(name="statemachine_State14", type=statemachine_Transition, multiplicity=Multiplicity(1, 1))
    }
)
events15: BinaryAssociation = BinaryAssociation(
    name="events15",
    ends={
        Property(name="statemachine_Event", type=statemachine_Condition, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_Condition16", type=statemachine_Event, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
signal17: BinaryAssociation = BinaryAssociation(
    name="signal17",
    ends={
        Property(name="statemachine_Signal19", type=statemachine_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_Event18", type=statemachine_Signal, multiplicity=Multiplicity(0, 1))
    }
)
signal20: BinaryAssociation = BinaryAssociation(
    name="signal20",
    ends={
        Property(name="statemachine_Signal22", type=statemachine_Command, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_Command21", type=statemachine_Signal, multiplicity=Multiplicity(0, 1))
    }
)
condition10: BinaryAssociation = BinaryAssociation(
    name="condition10",
    ends={
        Property(name="statemachine_Condition", type=statemachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_Transition11", type=statemachine_Condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_statemachine_InputSignal_Signal = Generalization(general=Signal, specific=statemachine_InputSignal)
gen_statemachine_OutputSignal_Signal = Generalization(general=Signal, specific=statemachine_OutputSignal)

# Domain Model
domain_model = DomainModel(
    name="statemachine",
    types={statemachine_Statemachine, statemachine_InputSignal, Signal, statemachine_OutputSignal, statemachine_Command, statemachine_Transition, statemachine_Signal, statemachine_State, statemachine_Event, statemachine_Condition},
    associations={states1, commands3, transitions5, nestedStates8, signals0, state12, events15, signal17, signal20, condition10},
    generalizations={gen_statemachine_InputSignal_Signal, gen_statemachine_OutputSignal_Signal},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)