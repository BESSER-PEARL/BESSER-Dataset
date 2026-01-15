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
fsm_Transition = Class(name="fsm::Transition")
fsm_InitialState = Class(name="fsm::InitialState")
State = Class(name="State")
fsm_FinalState = Class(name="fsm::FinalState")
fsm_FSM = Class(name="fsm::FSM")
fsm_State = Class(name="fsm::State")

# fsm_Transition class attributes and methods
fsm_Transition_name: Property = Property(name="name", type=StringType)
fsm_Transition.attributes={fsm_Transition_name}

# fsm_InitialState class attributes and methods

# State class attributes and methods

# fsm_FinalState class attributes and methods

# fsm_FSM class attributes and methods
fsm_FSM_name: Property = Property(name="name", type=StringType)
fsm_FSM.attributes={fsm_FSM_name}

# fsm_State class attributes and methods
fsm_State_name: Property = Property(name="name", type=StringType)
fsm_State.attributes={fsm_State_name}

# Relationships
transition1: BinaryAssociation = BinaryAssociation(
    name="transition1",
    ends={
        Property(name="fsm_Transition", type=fsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_FSM2", type=fsm_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source3: BinaryAssociation = BinaryAssociation(
    name="source3",
    ends={
        Property(name="fsm_State5", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Transition4", type=fsm_State, multiplicity=Multiplicity(1, 1))
    }
)
target6: BinaryAssociation = BinaryAssociation(
    name="target6",
    ends={
        Property(name="fsm_State8", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Transition7", type=fsm_State, multiplicity=Multiplicity(1, 1))
    }
)
state0: BinaryAssociation = BinaryAssociation(
    name="state0",
    ends={
        Property(name="fsm_State", type=fsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_FSM", type=fsm_State, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)

# Generalizations
gen_fsm_InitialState_State = Generalization(general=State, specific=fsm_InitialState)
gen_fsm_FinalState_State = Generalization(general=State, specific=fsm_FinalState)

# Domain Model
domain_model = DomainModel(
    name="fsm",
    types={fsm_Transition, fsm_InitialState, State, fsm_FinalState, fsm_FSM, fsm_State},
    associations={transition1, source3, target6, state0},
    generalizations={gen_fsm_InitialState_State, gen_fsm_FinalState_State},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)