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
fsmkerm_FSM = Class(name="fsmkerm::FSM")
fsmkerm_State = Class(name="fsmkerm::State")
fsmkerm_Transition = Class(name="fsmkerm::Transition")
fsmkerm_FSMException = Class(name="fsmkerm::FSMException")
fsmkerm_NonDeterminism = Class(name="fsmkerm::NonDeterminism")
FSMException = Class(name="FSMException")
fsmkerm_NoTransition = Class(name="fsmkerm::NoTransition")
fsmkerm_NoInitialStateException = Class(name="fsmkerm::NoInitialStateException")

# fsmkerm_FSM class attributes and methods
fsmkerm_FSM_m_run: Method = Method(name="run", parameters={})
fsmkerm_FSM_m_reset: Method = Method(name="reset", parameters={})
fsmkerm_FSM.methods={fsmkerm_FSM_m_run, fsmkerm_FSM_m_reset}

# fsmkerm_State class attributes and methods
fsmkerm_State_name: Property = Property(name="name", type=StringType)
fsmkerm_State_m_step: Method = Method(name="step", parameters={Parameter(name='c')})
fsmkerm_State.attributes={fsmkerm_State_name}
fsmkerm_State.methods={fsmkerm_State_m_step}

# fsmkerm_Transition class attributes and methods
fsmkerm_Transition_input: Property = Property(name="input", type=StringType)
fsmkerm_Transition_output: Property = Property(name="output", type=StringType)
fsmkerm_Transition_m_fire: Method = Method(name="fire", parameters={})
fsmkerm_Transition.attributes={fsmkerm_Transition_input, fsmkerm_Transition_output}
fsmkerm_Transition.methods={fsmkerm_Transition_m_fire}

# fsmkerm_FSMException class attributes and methods

# fsmkerm_NonDeterminism class attributes and methods

# FSMException class attributes and methods

# fsmkerm_NoTransition class attributes and methods

# fsmkerm_NoInitialStateException class attributes and methods

# Relationships
ownedState0: BinaryAssociation = BinaryAssociation(
    name="ownedState0",
    ends={
        Property(name="State", type=fsmkerm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="owningFSM", type=fsmkerm_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialState1: BinaryAssociation = BinaryAssociation(
    name="initialState1",
    ends={
        Property(name="fsmkerm_State", type=fsmkerm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="fsmkerm_FSM", type=fsmkerm_State, multiplicity=Multiplicity(1, 1))
    }
)
currentState2: BinaryAssociation = BinaryAssociation(
    name="currentState2",
    ends={
        Property(name="fsmkerm_State4", type=fsmkerm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="fsmkerm_FSM3", type=fsmkerm_State, multiplicity=Multiplicity(0, 1))
    }
)
finalState5: BinaryAssociation = BinaryAssociation(
    name="finalState5",
    ends={
        Property(name="fsmkerm_State7", type=fsmkerm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="fsmkerm_FSM6", type=fsmkerm_State, multiplicity=Multiplicity(1, 9999))
    }
)
transition8: BinaryAssociation = BinaryAssociation(
    name="transition8",
    ends={
        Property(name="fsmkerm_Transition", type=fsmkerm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="fsmkerm_FSM9", type=fsmkerm_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fsmException10: BinaryAssociation = BinaryAssociation(
    name="fsmException10",
    ends={
        Property(name="fsmkerm_FSMException", type=fsmkerm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="fsmkerm_FSM11", type=fsmkerm_FSMException, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
outgoingTransition13: BinaryAssociation = BinaryAssociation(
    name="outgoingTransition13",
    ends={
        Property(name="Transition", type=fsmkerm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=fsmkerm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
incomingTransition14: BinaryAssociation = BinaryAssociation(
    name="incomingTransition14",
    ends={
        Property(name="Transition15", type=fsmkerm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=fsmkerm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
source16: BinaryAssociation = BinaryAssociation(
    name="source16",
    ends={
        Property(name="State17", type=fsmkerm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingTransition", type=fsmkerm_State, multiplicity=Multiplicity(1, 1))
    }
)
target18: BinaryAssociation = BinaryAssociation(
    name="target18",
    ends={
        Property(name="State19", type=fsmkerm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingTransition", type=fsmkerm_State, multiplicity=Multiplicity(1, 1))
    }
)
owningFSM12: BinaryAssociation = BinaryAssociation(
    name="owningFSM12",
    ends={
        Property(name="FSM", type=fsmkerm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedState", type=fsmkerm_FSM, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_fsmkerm_NonDeterminism_FSMException = Generalization(general=FSMException, specific=fsmkerm_NonDeterminism)
gen_fsmkerm_NoTransition_FSMException = Generalization(general=FSMException, specific=fsmkerm_NoTransition)
gen_fsmkerm_NoInitialStateException_FSMException = Generalization(general=FSMException, specific=fsmkerm_NoInitialStateException)

# Domain Model
domain_model = DomainModel(
    name="fsmkerm",
    types={fsmkerm_FSM, fsmkerm_State, fsmkerm_Transition, fsmkerm_FSMException, fsmkerm_NonDeterminism, FSMException, fsmkerm_NoTransition, fsmkerm_NoInitialStateException},
    associations={ownedState0, initialState1, currentState2, finalState5, transition8, fsmException10, outgoingTransition13, incomingTransition14, source16, target18, owningFSM12},
    generalizations={gen_fsmkerm_NonDeterminism_FSMException, gen_fsmkerm_NoTransition_FSMException, gen_fsmkerm_NoInitialStateException_FSMException},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)