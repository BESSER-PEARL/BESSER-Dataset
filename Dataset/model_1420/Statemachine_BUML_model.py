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
statemachine_Event = Class(name="statemachine::Event")
statemachine_Command = Class(name="statemachine::Command")
statemachine_State = Class(name="statemachine::State")
statemachine_Transition = Class(name="statemachine::Transition")

# statemachine_Statemachine class attributes and methods

# statemachine_Event class attributes and methods
statemachine_Event_name: Property = Property(name="name", type=StringType)
statemachine_Event_code: Property = Property(name="code", type=StringType)
statemachine_Event.attributes={statemachine_Event_name, statemachine_Event_code}

# statemachine_Command class attributes and methods
statemachine_Command_name: Property = Property(name="name", type=StringType)
statemachine_Command_code: Property = Property(name="code", type=StringType)
statemachine_Command.attributes={statemachine_Command_name, statemachine_Command_code}

# statemachine_State class attributes and methods
statemachine_State_name: Property = Property(name="name", type=StringType)
statemachine_State.attributes={statemachine_State_name}

# statemachine_Transition class attributes and methods

# Relationships
events0: BinaryAssociation = BinaryAssociation(
    name="events0",
    ends={
        Property(name="statemachine_Event", type=statemachine_Statemachine, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_Statemachine", type=statemachine_Event, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resetEvents1: BinaryAssociation = BinaryAssociation(
    name="resetEvents1",
    ends={
        Property(name="statemachine_Event3", type=statemachine_Statemachine, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_Statemachine2", type=statemachine_Event, multiplicity=Multiplicity(0, 9999))
    }
)
commands4: BinaryAssociation = BinaryAssociation(
    name="commands4",
    ends={
        Property(name="statemachine_Command", type=statemachine_Statemachine, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_Statemachine5", type=statemachine_Command, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
states6: BinaryAssociation = BinaryAssociation(
    name="states6",
    ends={
        Property(name="statemachine_State", type=statemachine_Statemachine, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_Statemachine7", type=statemachine_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actions8: BinaryAssociation = BinaryAssociation(
    name="actions8",
    ends={
        Property(name="statemachine_Command10", type=statemachine_State, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_State9", type=statemachine_Command, multiplicity=Multiplicity(0, 9999))
    }
)
transitions11: BinaryAssociation = BinaryAssociation(
    name="transitions11",
    ends={
        Property(name="statemachine_Transition", type=statemachine_State, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_State12", type=statemachine_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
event13: BinaryAssociation = BinaryAssociation(
    name="event13",
    ends={
        Property(name="statemachine_Event15", type=statemachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_Transition14", type=statemachine_Event, multiplicity=Multiplicity(0, 1))
    }
)
state16: BinaryAssociation = BinaryAssociation(
    name="state16",
    ends={
        Property(name="statemachine_State18", type=statemachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_Transition17", type=statemachine_State, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="statemachine",
    types={statemachine_Statemachine, statemachine_Event, statemachine_Command, statemachine_State, statemachine_Transition},
    associations={events0, resetEvents1, commands4, states6, actions8, transitions11, event13, state16},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)