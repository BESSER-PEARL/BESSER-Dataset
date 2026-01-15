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
fsm_FSMException = Class(name="fsm::FSMException")
fsm_NonDeterminism = Class(name="fsm::NonDeterminism")
FSMException = Class(name="FSMException")
fsm_NoTransition = Class(name="fsm::NoTransition")
fsm_NoInitialStateException = Class(name="fsm::NoInitialStateException")

# fsm_FSM class attributes and methods
fsm_FSM_m_run: Method = Method(name="run", parameters={})
fsm_FSM_m_reset: Method = Method(name="reset", parameters={})
fsm_FSM.methods={fsm_FSM_m_reset, fsm_FSM_m_run}

# fsm_State class attributes and methods
fsm_State_name: Property = Property(name="name", type=StringType)
fsm_State_m_step: Method = Method(name="step", parameters={Parameter(name='c')})
fsm_State.attributes={fsm_State_name}
fsm_State.methods={fsm_State_m_step}

# fsm_Transition class attributes and methods
fsm_Transition_input: Property = Property(name="input", type=StringType)
fsm_Transition_output: Property = Property(name="output", type=StringType)
fsm_Transition_m_fire: Method = Method(name="fire", parameters={})
fsm_Transition.attributes={fsm_Transition_input, fsm_Transition_output}
fsm_Transition.methods={fsm_Transition_m_fire}

# fsm_FSMException class attributes and methods

# fsm_NonDeterminism class attributes and methods

# FSMException class attributes and methods

# fsm_NoTransition class attributes and methods

# fsm_NoInitialStateException class attributes and methods

# Relationships
ownedState0: BinaryAssociation = BinaryAssociation(
    name="ownedState0",
    ends={
        Property(name="State", type=fsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="owningFSM", type=fsm_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialState1: BinaryAssociation = BinaryAssociation(
    name="initialState1",
    ends={
        Property(name="fsm_State", type=fsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_FSM", type=fsm_State, multiplicity=Multiplicity(1, 1))
    }
)
currentState2: BinaryAssociation = BinaryAssociation(
    name="currentState2",
    ends={
        Property(name="fsm_State4", type=fsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_FSM3", type=fsm_State, multiplicity=Multiplicity(0, 1))
    }
)
finalState5: BinaryAssociation = BinaryAssociation(
    name="finalState5",
    ends={
        Property(name="fsm_State7", type=fsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_FSM6", type=fsm_State, multiplicity=Multiplicity(1, 9999))
    }
)
outgoingTransition13: BinaryAssociation = BinaryAssociation(
    name="outgoingTransition13",
    ends={
        Property(name="Transition", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=fsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
incomingTransition14: BinaryAssociation = BinaryAssociation(
    name="incomingTransition14",
    ends={
        Property(name="Transition15", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=fsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
source16: BinaryAssociation = BinaryAssociation(
    name="source16",
    ends={
        Property(name="State17", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingTransition", type=fsm_State, multiplicity=Multiplicity(1, 1))
    }
)
target18: BinaryAssociation = BinaryAssociation(
    name="target18",
    ends={
        Property(name="State19", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingTransition", type=fsm_State, multiplicity=Multiplicity(1, 1))
    }
)
transition8: BinaryAssociation = BinaryAssociation(
    name="transition8",
    ends={
        Property(name="fsm_Transition", type=fsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_FSM9", type=fsm_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fsmException10: BinaryAssociation = BinaryAssociation(
    name="fsmException10",
    ends={
        Property(name="fsm_FSMException", type=fsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_FSM11", type=fsm_FSMException, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
owningFSM12: BinaryAssociation = BinaryAssociation(
    name="owningFSM12",
    ends={
        Property(name="FSM", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedState", type=fsm_FSM, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_fsm_NonDeterminism_FSMException = Generalization(general=FSMException, specific=fsm_NonDeterminism)
gen_fsm_NoTransition_FSMException = Generalization(general=FSMException, specific=fsm_NoTransition)
gen_fsm_NoInitialStateException_FSMException = Generalization(general=FSMException, specific=fsm_NoInitialStateException)

# Domain Model
domain_model = DomainModel(
    name="fsm",
    types={fsm_FSM, fsm_State, fsm_Transition, fsm_FSMException, fsm_NonDeterminism, FSMException, fsm_NoTransition, fsm_NoInitialStateException},
    associations={ownedState0, initialState1, currentState2, finalState5, outgoingTransition13, incomingTransition14, source16, target18, transition8, fsmException10, owningFSM12},
    generalizations={gen_fsm_NonDeterminism_FSMException, gen_fsm_NoTransition_FSMException, gen_fsm_NoInitialStateException_FSMException},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)