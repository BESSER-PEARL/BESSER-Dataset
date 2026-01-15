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
fsm_FSM = Class(name="fsm::FSM")
fsm_State = Class(name="fsm::State")
fsm_Transition = Class(name="fsm::Transition")

# fsm_FSM class attributes and methods

# fsm_State class attributes and methods
fsm_State_name: Property = Property(name="name", type=StringType)
fsm_State.attributes={fsm_State_name}

# fsm_Transition class attributes and methods
fsm_Transition_input: Property = Property(name="input", type=StringType)
fsm_Transition_output: Property = Property(name="output", type=StringType)
fsm_Transition_time: Property = Property(name="time", type=IntegerType)
fsm_Transition.attributes={fsm_Transition_output, fsm_Transition_input, fsm_Transition_time}

# Relationships
ownedState0: BinaryAssociation = BinaryAssociation(
    name="ownedState0",
    ends={
        Property(name="1", type=fsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="", type=fsm_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialState2: BinaryAssociation = BinaryAssociation(
    name="initialState2",
    ends={
        Property(name="fsm_State", type=fsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_FSM", type=fsm_State, multiplicity=Multiplicity(1, 1))
    }
)
finalState3: BinaryAssociation = BinaryAssociation(
    name="finalState3",
    ends={
        Property(name="fsm_State5", type=fsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_FSM4", type=fsm_State, multiplicity=Multiplicity(1, 9999))
    }
)
owningFSM6: BinaryAssociation = BinaryAssociation(
    name="owningFSM6",
    ends={
        Property(name="8", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="7", type=fsm_FSM, multiplicity=Multiplicity(1, 1))
    }
)
outgoingTransition9: BinaryAssociation = BinaryAssociation(
    name="outgoingTransition9",
    ends={
        Property(name="11", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="10", type=fsm_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source15: BinaryAssociation = BinaryAssociation(
    name="source15",
    ends={
        Property(name="17", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="16", type=fsm_State, multiplicity=Multiplicity(1, 1))
    }
)
target18: BinaryAssociation = BinaryAssociation(
    name="target18",
    ends={
        Property(name="20", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="19", type=fsm_State, multiplicity=Multiplicity(1, 1))
    }
)
incomingTransition12: BinaryAssociation = BinaryAssociation(
    name="incomingTransition12",
    ends={
        Property(name="14", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="13", type=fsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="fsm",
    types={fsm_FSM, fsm_State, fsm_Transition},
    associations={ownedState0, initialState2, finalState3, owningFSM6, outgoingTransition9, source15, target18, incomingTransition12},
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