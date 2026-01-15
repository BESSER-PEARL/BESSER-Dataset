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
minifsm_FSM = Class(name="minifsm::FSM")
minifsm_State = Class(name="minifsm::State")
minifsm_Initial = Class(name="minifsm::Initial")
State = Class(name="State")
minifsm_Terminal = Class(name="minifsm::Terminal")
minifsm_Transition = Class(name="minifsm::Transition")

# minifsm_FSM class attributes and methods
minifsm_FSM_m_handle: Method = Method(name="handle", parameters={Parameter(name='event')})
minifsm_FSM.methods={minifsm_FSM_m_handle}

# minifsm_State class attributes and methods
minifsm_State_name: Property = Property(name="name", type=StringType)
minifsm_State_m_execute: Method = Method(name="execute", parameters={})
minifsm_State.attributes={minifsm_State_name}
minifsm_State.methods={minifsm_State_m_execute}

# minifsm_Initial class attributes and methods

# State class attributes and methods

# minifsm_Terminal class attributes and methods

# minifsm_Transition class attributes and methods
minifsm_Transition_event: Property = Property(name="event", type=StringType)
minifsm_Transition_m_isActivated: Method = Method(name="isActivated", parameters={}, type=BooleanType)
minifsm_Transition.attributes={minifsm_Transition_event}
minifsm_Transition.methods={minifsm_Transition_m_isActivated}

# Relationships
states0: BinaryAssociation = BinaryAssociation(
    name="states0",
    ends={
        Property(name="minifsm_State", type=minifsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="minifsm_FSM", type=minifsm_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fsm7: BinaryAssociation = BinaryAssociation(
    name="fsm7",
    ends={
        Property(name="FSM", type=minifsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transitions", type=minifsm_FSM, multiplicity=Multiplicity(0, 1))
    }
)
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="Transition", type=minifsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm", type=minifsm_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
incoming2: BinaryAssociation = BinaryAssociation(
    name="incoming2",
    ends={
        Property(name="minifsm_State3", type=minifsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="minifsm_Transition", type=minifsm_State, multiplicity=Multiplicity(0, 1))
    }
)
outgoing4: BinaryAssociation = BinaryAssociation(
    name="outgoing4",
    ends={
        Property(name="minifsm_State6", type=minifsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="minifsm_Transition5", type=minifsm_State, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_minifsm_Initial_State = Generalization(general=State, specific=minifsm_Initial)
gen_minifsm_Terminal_State = Generalization(general=State, specific=minifsm_Terminal)

# Domain Model
domain_model = DomainModel(
    name="minifsm",
    types={minifsm_FSM, minifsm_State, minifsm_Initial, State, minifsm_Terminal, minifsm_Transition},
    associations={states0, fsm7, transitions1, incoming2, outgoing4},
    generalizations={gen_minifsm_Initial_State, gen_minifsm_Terminal_State},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)