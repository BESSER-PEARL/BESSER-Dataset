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
fsm_InitialState = Class(name="fsm::InitialState")
fsm_FinalState = Class(name="fsm::FinalState")
State = Class(name="State")

# fsm_FSM class attributes and methods
fsm_FSM_name: Property = Property(name="name", type=StringType)
fsm_FSM.attributes={fsm_FSM_name}

# fsm_State class attributes and methods
fsm_State_name: Property = Property(name="name", type=StringType)
fsm_State.attributes={fsm_State_name}

# fsm_Transition class attributes and methods
fsm_Transition_event: Property = Property(name="event", type=StringType)
fsm_Transition.attributes={fsm_Transition_event}

# fsm_InitialState class attributes and methods

# fsm_FinalState class attributes and methods

# State class attributes and methods

# Relationships
states0: BinaryAssociation = BinaryAssociation(
    name="states0",
    ends={
        Property(name="State", type=fsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm", type=fsm_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="Transition", type=fsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm2", type=fsm_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialstate3: BinaryAssociation = BinaryAssociation(
    name="initialstate3",
    ends={
        Property(name="fsm_InitialState", type=fsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_FSM", type=fsm_InitialState, multiplicity=Multiplicity(1, 1))
    }
)
incommingtransitions7: BinaryAssociation = BinaryAssociation(
    name="incommingtransitions7",
    ends={
        Property(name="Transition8", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="to", type=fsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
fsm9: BinaryAssociation = BinaryAssociation(
    name="fsm9",
    ends={
        Property(name="FSM10", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transitions", type=fsm_FSM, multiplicity=Multiplicity(1, 1))
    }
)
from11: BinaryAssociation = BinaryAssociation(
    name="from11",
    ends={
        Property(name="State12", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingtransitions", type=fsm_State, multiplicity=Multiplicity(1, 1))
    }
)
to13: BinaryAssociation = BinaryAssociation(
    name="to13",
    ends={
        Property(name="State14", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incommingtransitions", type=fsm_State, multiplicity=Multiplicity(1, 1))
    }
)
fsm4: BinaryAssociation = BinaryAssociation(
    name="fsm4",
    ends={
        Property(name="FSM", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states", type=fsm_FSM, multiplicity=Multiplicity(1, 1))
    }
)
outgoingtransitions5: BinaryAssociation = BinaryAssociation(
    name="outgoingtransitions5",
    ends={
        Property(name="Transition6", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="from", type=fsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_fsm_FinalState_State = Generalization(general=State, specific=fsm_FinalState)
gen_fsm_InitialState_State = Generalization(general=State, specific=fsm_InitialState)

# Domain Model
domain_model = DomainModel(
    name="fsm",
    types={fsm_FSM, fsm_State, fsm_Transition, fsm_InitialState, fsm_FinalState, State},
    associations={states0, transitions1, initialstate3, incommingtransitions7, fsm9, from11, to13, fsm4, outgoingtransitions5},
    generalizations={gen_fsm_FinalState_State, gen_fsm_InitialState_State},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)