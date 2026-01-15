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
statemachine_mk2_StateMachine = Class(name="statemachine::mk2::StateMachine")
statemachine_mk2_SimpleState = Class(name="statemachine::mk2::SimpleState")
statemachine_mk2_State = Class(name="statemachine::mk2::State", is_abstract=True)
State = Class(name="State")
statemachine_mk2_Transition = Class(name="statemachine::mk2::Transition")
statemachine_mk2_Event = Class(name="statemachine::mk2::Event")
statemachine_mk2_Final_state = Class(name="statemachine::mk2::Final::state")
statemachine_mk2_Composite_state = Class(name="statemachine::mk2::Composite::state")

# statemachine_mk2_StateMachine class attributes and methods

# statemachine_mk2_SimpleState class attributes and methods

# statemachine_mk2_State class attributes and methods
statemachine_mk2_State_name: Property = Property(name="name", type=StringType)
statemachine_mk2_State.attributes={statemachine_mk2_State_name}

# State class attributes and methods

# statemachine_mk2_Transition class attributes and methods
statemachine_mk2_Transition_name: Property = Property(name="name", type=StringType)
statemachine_mk2_Transition.attributes={statemachine_mk2_Transition_name}

# statemachine_mk2_Event class attributes and methods
statemachine_mk2_Event_description: Property = Property(name="description", type=StringType)
statemachine_mk2_Event.attributes={statemachine_mk2_Event_description}

# statemachine_mk2_Final_state class attributes and methods

# statemachine_mk2_Composite_state class attributes and methods

# Relationships
simple_states0: BinaryAssociation = BinaryAssociation(
    name="simple_states0",
    ends={
        Property(name="statemachine_mk2_SimpleState", type=statemachine_mk2_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_mk2_StateMachine", type=statemachine_mk2_SimpleState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initial_state1: BinaryAssociation = BinaryAssociation(
    name="initial_state1",
    ends={
        Property(name="statemachine_mk2_State", type=statemachine_mk2_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_mk2_StateMachine2", type=statemachine_mk2_State, multiplicity=Multiplicity(1, 1))
    }
)
source14: BinaryAssociation = BinaryAssociation(
    name="source14",
    ends={
        Property(name="State", type=statemachine_mk2_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=statemachine_mk2_State, multiplicity=Multiplicity(1, 1))
    }
)
target15: BinaryAssociation = BinaryAssociation(
    name="target15",
    ends={
        Property(name="State16", type=statemachine_mk2_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=statemachine_mk2_State, multiplicity=Multiplicity(1, 1))
    }
)
triggers17: BinaryAssociation = BinaryAssociation(
    name="triggers17",
    ends={
        Property(name="statemachine_mk2_Event19", type=statemachine_mk2_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_mk2_Transition18", type=statemachine_mk2_Event, multiplicity=Multiplicity(0, 9999))
    }
)
possible_states20: BinaryAssociation = BinaryAssociation(
    name="possible_states20",
    ends={
        Property(name="statemachine_mk2_State22", type=statemachine_mk2_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_mk2_Event21", type=statemachine_mk2_State, multiplicity=Multiplicity(0, 9999))
    }
)
causes23: BinaryAssociation = BinaryAssociation(
    name="causes23",
    ends={
        Property(name="statemachine_mk2_Transition25", type=statemachine_mk2_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_mk2_Event24", type=statemachine_mk2_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
substates26: BinaryAssociation = BinaryAssociation(
    name="substates26",
    ends={
        Property(name="statemachine_mk2_State28", type=statemachine_mk2_Composite_state, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_mk2_Composite_state27", type=statemachine_mk2_State, multiplicity=Multiplicity(0, 9999))
    }
)
transitions3: BinaryAssociation = BinaryAssociation(
    name="transitions3",
    ends={
        Property(name="statemachine_mk2_Transition", type=statemachine_mk2_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_mk2_StateMachine4", type=statemachine_mk2_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
events5: BinaryAssociation = BinaryAssociation(
    name="events5",
    ends={
        Property(name="statemachine_mk2_Event", type=statemachine_mk2_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_mk2_StateMachine6", type=statemachine_mk2_Event, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
final_states7: BinaryAssociation = BinaryAssociation(
    name="final_states7",
    ends={
        Property(name="statemachine_mk2_Final_state", type=statemachine_mk2_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_mk2_StateMachine8", type=statemachine_mk2_Final_state, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
composite_states9: BinaryAssociation = BinaryAssociation(
    name="composite_states9",
    ends={
        Property(name="statemachine_mk2_Composite_state", type=statemachine_mk2_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_mk2_StateMachine10", type=statemachine_mk2_Composite_state, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
outgoing11: BinaryAssociation = BinaryAssociation(
    name="outgoing11",
    ends={
        Property(name="Transition", type=statemachine_mk2_State, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=statemachine_mk2_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
incoming12: BinaryAssociation = BinaryAssociation(
    name="incoming12",
    ends={
        Property(name="Transition13", type=statemachine_mk2_State, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=statemachine_mk2_Transition, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_statemachine_mk2_Final_state_State = Generalization(general=State, specific=statemachine_mk2_Final_state)
gen_statemachine_mk2_Composite_state_State = Generalization(general=State, specific=statemachine_mk2_Composite_state)
gen_statemachine_mk2_SimpleState_State = Generalization(general=State, specific=statemachine_mk2_SimpleState)

# Domain Model
domain_model = DomainModel(
    name="statemachine_mk2",
    types={statemachine_mk2_StateMachine, statemachine_mk2_SimpleState, statemachine_mk2_State, State, statemachine_mk2_Transition, statemachine_mk2_Event, statemachine_mk2_Final_state, statemachine_mk2_Composite_state},
    associations={simple_states0, initial_state1, source14, target15, triggers17, possible_states20, causes23, substates26, transitions3, events5, final_states7, composite_states9, outgoing11, incoming12},
    generalizations={gen_statemachine_mk2_Final_state_State, gen_statemachine_mk2_Composite_state_State, gen_statemachine_mk2_SimpleState_State},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)