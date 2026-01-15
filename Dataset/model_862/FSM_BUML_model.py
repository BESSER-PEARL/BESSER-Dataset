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
fsm_InitialState = Class(name="fsm::InitialState")
State = Class(name="State")
fsm_FinalState = Class(name="fsm::FinalState")
fsm_Machine = Class(name="fsm::Machine")
fsm_State = Class(name="fsm::State")
fsm_Transition = Class(name="fsm::Transition")

# fsm_InitialState class attributes and methods

# State class attributes and methods

# fsm_FinalState class attributes and methods

# fsm_Machine class attributes and methods
fsm_Machine_name: Property = Property(name="name", type=StringType)
fsm_Machine.attributes={fsm_Machine_name}

# fsm_State class attributes and methods
fsm_State_name: Property = Property(name="name", type=StringType)
fsm_State.attributes={fsm_State_name}

# fsm_Transition class attributes and methods
fsm_Transition_event: Property = Property(name="event", type=StringType)
fsm_Transition.attributes={fsm_Transition_event}

# Relationships
owning3: BinaryAssociation = BinaryAssociation(
    name="owning3",
    ends={
        Property(name="Machine", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states", type=fsm_Machine, multiplicity=Multiplicity(1, 1))
    }
)
incoming4: BinaryAssociation = BinaryAssociation(
    name="incoming4",
    ends={
        Property(name="Transition5", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=fsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing6: BinaryAssociation = BinaryAssociation(
    name="outgoing6",
    ends={
        Property(name="Transition7", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=fsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
owning8: BinaryAssociation = BinaryAssociation(
    name="owning8",
    ends={
        Property(name="Machine9", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transitions", type=fsm_Machine, multiplicity=Multiplicity(1, 1))
    }
)
source10: BinaryAssociation = BinaryAssociation(
    name="source10",
    ends={
        Property(name="State11", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=fsm_State, multiplicity=Multiplicity(1, 1))
    }
)
target12: BinaryAssociation = BinaryAssociation(
    name="target12",
    ends={
        Property(name="State13", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=fsm_State, multiplicity=Multiplicity(1, 1))
    }
)
states0: BinaryAssociation = BinaryAssociation(
    name="states0",
    ends={
        Property(name="State", type=fsm_Machine, multiplicity=Multiplicity(1, 1)),
        Property(name="owning", type=fsm_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="Transition", type=fsm_Machine, multiplicity=Multiplicity(1, 1)),
        Property(name="owning2", type=fsm_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_fsm_InitialState_State = Generalization(general=State, specific=fsm_InitialState)
gen_fsm_FinalState_State = Generalization(general=State, specific=fsm_FinalState)

# Domain Model
domain_model = DomainModel(
    name="fsm",
    types={fsm_InitialState, State, fsm_FinalState, fsm_Machine, fsm_State, fsm_Transition},
    associations={owning3, incoming4, outgoing6, owning8, source10, target12, states0, transitions1},
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