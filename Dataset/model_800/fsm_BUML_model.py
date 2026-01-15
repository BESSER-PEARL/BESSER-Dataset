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
fsmSample_FSM = Class(name="fsmSample::FSM")
fsmSample_Action = Class(name="fsmSample::Action")
fsmSample_State = Class(name="fsmSample::State")
fsmSample_Transition = Class(name="fsmSample::Transition")

# fsmSample_FSM class attributes and methods
fsmSample_FSM_name: Property = Property(name="name", type=StringType)
fsmSample_FSM.attributes={fsmSample_FSM_name}

# fsmSample_Action class attributes and methods
fsmSample_Action_name: Property = Property(name="name", type=StringType)
fsmSample_Action_m_run: Method = Method(name="run", parameters={Parameter(name='sync')}, type=StringType)
fsmSample_Action.attributes={fsmSample_Action_name}
fsmSample_Action.methods={fsmSample_Action_m_run}

# fsmSample_State class attributes and methods
fsmSample_State_name: Property = Property(name="name", type=StringType)
fsmSample_State.attributes={fsmSample_State_name}

# fsmSample_Transition class attributes and methods
fsmSample_Transition_input: Property = Property(name="input", type=StringType)
fsmSample_Transition_output: Property = Property(name="output", type=StringType)
fsmSample_Transition.attributes={fsmSample_Transition_output, fsmSample_Transition_input}

# Relationships
target14: BinaryAssociation = BinaryAssociation(
    name="target14",
    ends={
        Property(name="State15", type=fsmSample_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingTransition", type=fsmSample_State, multiplicity=Multiplicity(1, 1))
    }
)
action16: BinaryAssociation = BinaryAssociation(
    name="action16",
    ends={
        Property(name="fsmSample_Action", type=fsmSample_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fsmSample_Transition", type=fsmSample_Action, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedState0: BinaryAssociation = BinaryAssociation(
    name="ownedState0",
    ends={
        Property(name="State", type=fsmSample_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="owningFSM", type=fsmSample_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialState1: BinaryAssociation = BinaryAssociation(
    name="initialState1",
    ends={
        Property(name="fsmSample_State", type=fsmSample_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="fsmSample_FSM", type=fsmSample_State, multiplicity=Multiplicity(1, 1))
    }
)
finalState2: BinaryAssociation = BinaryAssociation(
    name="finalState2",
    ends={
        Property(name="fsmSample_State4", type=fsmSample_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="fsmSample_FSM3", type=fsmSample_State, multiplicity=Multiplicity(1, 9999))
    }
)
currentState5: BinaryAssociation = BinaryAssociation(
    name="currentState5",
    ends={
        Property(name="fsmSample_State7", type=fsmSample_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="fsmSample_FSM6", type=fsmSample_State, multiplicity=Multiplicity(1, 1))
    }
)
owningFSM8: BinaryAssociation = BinaryAssociation(
    name="owningFSM8",
    ends={
        Property(name="FSM", type=fsmSample_State, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedState", type=fsmSample_FSM, multiplicity=Multiplicity(1, 1))
    }
)
outgoingTransition9: BinaryAssociation = BinaryAssociation(
    name="outgoingTransition9",
    ends={
        Property(name="Transition", type=fsmSample_State, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=fsmSample_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
incomingTransition10: BinaryAssociation = BinaryAssociation(
    name="incomingTransition10",
    ends={
        Property(name="Transition11", type=fsmSample_State, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=fsmSample_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
source12: BinaryAssociation = BinaryAssociation(
    name="source12",
    ends={
        Property(name="State13", type=fsmSample_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingTransition", type=fsmSample_State, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="fsmSample",
    types={fsmSample_FSM, fsmSample_Action, fsmSample_State, fsmSample_Transition},
    associations={target14, action16, ownedState0, initialState1, finalState2, currentState5, owningFSM8, outgoingTransition9, incomingTransition10, source12},
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