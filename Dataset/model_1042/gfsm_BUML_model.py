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
gfsm_Guard = Class(name="gfsm::Guard", is_abstract=True)
gfsm_Machine = Class(name="gfsm::Machine")
gfsm_Transition = Class(name="gfsm::Transition")
gfsm_State = Class(name="gfsm::State")
gfsm_InitialState = Class(name="gfsm::InitialState")
State = Class(name="State")
gfsm_FinalState = Class(name="gfsm::FinalState")

# gfsm_Guard class attributes and methods

# gfsm_Machine class attributes and methods
gfsm_Machine_name: Property = Property(name="name", type=StringType)
gfsm_Machine.attributes={gfsm_Machine_name}

# gfsm_Transition class attributes and methods
gfsm_Transition_event: Property = Property(name="event", type=StringType)
gfsm_Transition.attributes={gfsm_Transition_event}

# gfsm_State class attributes and methods
gfsm_State_name: Property = Property(name="name", type=StringType)
gfsm_State.attributes={gfsm_State_name}

# gfsm_InitialState class attributes and methods

# State class attributes and methods

# gfsm_FinalState class attributes and methods

# Relationships
owning3: BinaryAssociation = BinaryAssociation(
    name="owning3",
    ends={
        Property(name="Machine", type=gfsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states", type=gfsm_Machine, multiplicity=Multiplicity(1, 1))
    }
)
incoming4: BinaryAssociation = BinaryAssociation(
    name="incoming4",
    ends={
        Property(name="Transition5", type=gfsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=gfsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing6: BinaryAssociation = BinaryAssociation(
    name="outgoing6",
    ends={
        Property(name="Transition7", type=gfsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=gfsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
owning8: BinaryAssociation = BinaryAssociation(
    name="owning8",
    ends={
        Property(name="Machine9", type=gfsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transitions", type=gfsm_Machine, multiplicity=Multiplicity(1, 1))
    }
)
target10: BinaryAssociation = BinaryAssociation(
    name="target10",
    ends={
        Property(name="State11", type=gfsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=gfsm_State, multiplicity=Multiplicity(1, 1))
    }
)
source12: BinaryAssociation = BinaryAssociation(
    name="source12",
    ends={
        Property(name="State13", type=gfsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=gfsm_State, multiplicity=Multiplicity(1, 1))
    }
)
guard14: BinaryAssociation = BinaryAssociation(
    name="guard14",
    ends={
        Property(name="gfsm_Guard", type=gfsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="gfsm_Transition", type=gfsm_Guard, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
transitions0: BinaryAssociation = BinaryAssociation(
    name="transitions0",
    ends={
        Property(name="Transition", type=gfsm_Machine, multiplicity=Multiplicity(1, 1)),
        Property(name="owning", type=gfsm_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
states1: BinaryAssociation = BinaryAssociation(
    name="states1",
    ends={
        Property(name="State", type=gfsm_Machine, multiplicity=Multiplicity(1, 1)),
        Property(name="owning2", type=gfsm_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_gfsm_InitialState_State = Generalization(general=State, specific=gfsm_InitialState)
gen_gfsm_FinalState_State = Generalization(general=State, specific=gfsm_FinalState)

# Domain Model
domain_model = DomainModel(
    name="gfsm",
    types={gfsm_Guard, gfsm_Machine, gfsm_Transition, gfsm_State, gfsm_InitialState, State, gfsm_FinalState},
    associations={owning3, incoming4, outgoing6, owning8, target10, source12, guard14, transitions0, states1},
    generalizations={gen_gfsm_InitialState_State, gen_gfsm_FinalState_State},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)