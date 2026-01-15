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
fsm_State = Class(name="fsm::State")
fsm_Transition = Class(name="fsm::Transition")
fsm_FSM = Class(name="fsm::FSM")
fsm_Initial = Class(name="fsm::Initial")
State = Class(name="State")
fsm_Final = Class(name="fsm::Final")

# fsm_State class attributes and methods
fsm_State_name: Property = Property(name="name", type=StringType)
fsm_State_m_execute: Method = Method(name="execute", parameters={})
fsm_State.attributes={fsm_State_name}
fsm_State.methods={fsm_State_m_execute}

# fsm_Transition class attributes and methods
fsm_Transition_event: Property = Property(name="event", type=StringType)
fsm_Transition_m_isActivated: Method = Method(name="isActivated", parameters={}, type=BooleanType)
fsm_Transition.attributes={fsm_Transition_event}
fsm_Transition.methods={fsm_Transition_m_isActivated}

# fsm_FSM class attributes and methods
fsm_FSM_m_execute: Method = Method(name="execute", parameters={Parameter(name='events')})
fsm_FSM.methods={fsm_FSM_m_execute}

# fsm_Initial class attributes and methods

# State class attributes and methods

# fsm_Final class attributes and methods

# Relationships
states0: BinaryAssociation = BinaryAssociation(
    name="states0",
    ends={
        Property(name="fsm_State", type=fsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_FSM", type=fsm_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="Transition", type=fsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm", type=fsm_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
incoming2: BinaryAssociation = BinaryAssociation(
    name="incoming2",
    ends={
        Property(name="fsm_State3", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Transition", type=fsm_State, multiplicity=Multiplicity(1, 1))
    }
)
outgoing4: BinaryAssociation = BinaryAssociation(
    name="outgoing4",
    ends={
        Property(name="fsm_State6", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Transition5", type=fsm_State, multiplicity=Multiplicity(1, 1))
    }
)
fsm7: BinaryAssociation = BinaryAssociation(
    name="fsm7",
    ends={
        Property(name="FSM", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transitions", type=fsm_FSM, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_fsm_Initial_State = Generalization(general=State, specific=fsm_Initial)
gen_fsm_Final_State = Generalization(general=State, specific=fsm_Final)

# Domain Model
domain_model = DomainModel(
    name="fsm",
    types={fsm_State, fsm_Transition, fsm_FSM, fsm_Initial, State, fsm_Final},
    associations={states0, transitions1, incoming2, outgoing4, fsm7},
    generalizations={gen_fsm_Initial_State, gen_fsm_Final_State},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)