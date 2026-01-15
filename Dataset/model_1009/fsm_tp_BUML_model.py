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
fsm_tp_FSM = Class(name="fsm::tp::FSM")
fsm_tp_State = Class(name="fsm::tp::State")
fsm_tp_Transition = Class(name="fsm::tp::Transition")
fsm_tp_InitialState = Class(name="fsm::tp::InitialState")
State = Class(name="State")

# fsm_tp_FSM class attributes and methods
fsm_tp_FSM_name: Property = Property(name="name", type=StringType)
fsm_tp_FSM.attributes={fsm_tp_FSM_name}

# fsm_tp_State class attributes and methods
fsm_tp_State_name: Property = Property(name="name", type=StringType)
fsm_tp_State_isFinal: Property = Property(name="isFinal", type=BooleanType)
fsm_tp_State.attributes={fsm_tp_State_isFinal, fsm_tp_State_name}

# fsm_tp_Transition class attributes and methods
fsm_tp_Transition_name: Property = Property(name="name", type=StringType)
fsm_tp_Transition_trigger: Property = Property(name="trigger", type=StringType)
fsm_tp_Transition.attributes={fsm_tp_Transition_trigger, fsm_tp_Transition_name}

# fsm_tp_InitialState class attributes and methods

# State class attributes and methods

# Relationships
state0: BinaryAssociation = BinaryAssociation(
    name="state0",
    ends={
        Property(name="fsm_tp_State", type=fsm_tp_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_tp_FSM", type=fsm_tp_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition1: BinaryAssociation = BinaryAssociation(
    name="transition1",
    ends={
        Property(name="fsm_tp_Transition", type=fsm_tp_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_tp_FSM2", type=fsm_tp_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialstate3: BinaryAssociation = BinaryAssociation(
    name="initialstate3",
    ends={
        Property(name="fsm_tp_InitialState", type=fsm_tp_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_tp_FSM4", type=fsm_tp_InitialState, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source5: BinaryAssociation = BinaryAssociation(
    name="source5",
    ends={
        Property(name="fsm_tp_State7", type=fsm_tp_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_tp_Transition6", type=fsm_tp_State, multiplicity=Multiplicity(1, 1))
    }
)
target8: BinaryAssociation = BinaryAssociation(
    name="target8",
    ends={
        Property(name="fsm_tp_State10", type=fsm_tp_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_tp_Transition9", type=fsm_tp_State, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_fsm_tp_InitialState_State = Generalization(general=State, specific=fsm_tp_InitialState)

# Domain Model
domain_model = DomainModel(
    name="fsm_tp",
    types={fsm_tp_FSM, fsm_tp_State, fsm_tp_Transition, fsm_tp_InitialState, State},
    associations={state0, transition1, initialstate3, source5, target8},
    generalizations={gen_fsm_tp_InitialState_State},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)