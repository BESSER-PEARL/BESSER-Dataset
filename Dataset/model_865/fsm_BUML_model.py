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
fsm_FSM = Class(name="fsm_FSM")
fsm_InitialState = Class(name="fsm_InitialState")
SuperState = Class(name="SuperState")
fsm_Action = Class(name="fsm_Action")
fsm_eAction = Class(name="fsm_eAction")
fsm_SteadyState = Class(name="fsm_SteadyState")
State = Class(name="State")
fsm_TransientState = Class(name="fsm_TransientState")
fsm_Transition = Class(name="fsm_Transition")
fsm_SuperState = Class(name="fsm_SuperState")
fsm_State = Class(name="fsm_State")

# fsm_FSM class attributes and methods

# fsm_InitialState class attributes and methods

# SuperState class attributes and methods

# fsm_Action class attributes and methods
fsm_Action_entryLabel: Property = Property(name="entryLabel", type=StringType)
fsm_Action.attributes={fsm_Action_entryLabel}

# fsm_eAction class attributes and methods
fsm_eAction_exitLabel: Property = Property(name="exitLabel", type=StringType)
fsm_eAction.attributes={fsm_eAction_exitLabel}

# fsm_SteadyState class attributes and methods

# State class attributes and methods

# fsm_TransientState class attributes and methods

# fsm_Transition class attributes and methods
fsm_Transition_guard: Property = Property(name="guard", type=StringType)
fsm_Transition_action: Property = Property(name="action", type=StringType)
fsm_Transition.attributes={fsm_Transition_guard, fsm_Transition_action}

# fsm_SuperState class attributes and methods

# fsm_State class attributes and methods
fsm_State_name: Property = Property(name="name", type=StringType)
fsm_State.attributes={fsm_State_name}

# Relationships
state0: BinaryAssociation = BinaryAssociation(
    name="state0",
    ends={
        Property(name="fsm_State", type=fsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_FSM", type=fsm_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intialState1: BinaryAssociation = BinaryAssociation(
    name="intialState1",
    ends={
        Property(name="fsm_InitialState", type=fsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_FSM2", type=fsm_InitialState, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
entry3: BinaryAssociation = BinaryAssociation(
    name="entry3",
    ends={
        Property(name="fsm_Action", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_State4", type=fsm_Action, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exit5: BinaryAssociation = BinaryAssociation(
    name="exit5",
    ends={
        Property(name="fsm_eAction", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_State6", type=fsm_eAction, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target7: BinaryAssociation = BinaryAssociation(
    name="target7",
    ends={
        Property(name="fsm_State8", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Transition", type=fsm_State, multiplicity=Multiplicity(1, 1))
    }
)
source9: BinaryAssociation = BinaryAssociation(
    name="source9",
    ends={
        Property(name="fsm_SuperState", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Transition10", type=fsm_SuperState, multiplicity=Multiplicity(1, 1))
    }
)
src11: BinaryAssociation = BinaryAssociation(
    name="src11",
    ends={
        Property(name="SuperState", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outTrans", type=fsm_SuperState, multiplicity=Multiplicity(0, 1))
    }
)
outTrans12: BinaryAssociation = BinaryAssociation(
    name="outTrans12",
    ends={
        Property(name="Transition", type=fsm_SuperState, multiplicity=Multiplicity(1, 1)),
        Property(name="src", type=fsm_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_fsm_State_SuperState = Generalization(general=SuperState, specific=fsm_State)
gen_fsm_SteadyState_State = Generalization(general=State, specific=fsm_SteadyState)
gen_fsm_TransientState_State = Generalization(general=State, specific=fsm_TransientState)
gen_fsm_InitialState_SuperState = Generalization(general=SuperState, specific=fsm_InitialState)

# Domain Model
domain_model = DomainModel(
    name="fsm",
    types={fsm_FSM, fsm_InitialState, SuperState, fsm_Action, fsm_eAction, fsm_SteadyState, State, fsm_TransientState, fsm_Transition, fsm_SuperState, fsm_State},
    associations={state0, intialState1, entry3, exit5, target7, source9, src11, outTrans12},
    generalizations={gen_fsm_State_SuperState, gen_fsm_SteadyState_State, gen_fsm_TransientState_State, gen_fsm_InitialState_SuperState},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)