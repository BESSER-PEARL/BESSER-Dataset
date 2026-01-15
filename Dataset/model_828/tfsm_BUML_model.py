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
tfsm_TFSM = Class(name="tfsm::TFSM")
NamedElement = Class(name="NamedElement")
tfsm_State = Class(name="tfsm::State")
tfsm_FSMClock = Class(name="tfsm::FSMClock")
tfsm_Transition = Class(name="tfsm::Transition")
tfsm_Guard = Class(name="tfsm::Guard", is_abstract=True)
tfsm_NamedElement = Class(name="tfsm::NamedElement")
tfsm_TemporalGuard = Class(name="tfsm::TemporalGuard")
Guard = Class(name="Guard")
tfsm_FSMEvent = Class(name="tfsm::FSMEvent")
tfsm_System = Class(name="tfsm::System")
tfsm_EventGuard = Class(name="tfsm::EventGuard")

# tfsm_TFSM class attributes and methods

# NamedElement class attributes and methods

# tfsm_State class attributes and methods
tfsm_State_m_onEnter: Method = Method(name="onEnter", parameters={}, type=StringType)
tfsm_State_m_onLeave: Method = Method(name="onLeave", parameters={}, type=StringType)
tfsm_State.methods={tfsm_State_m_onLeave, tfsm_State_m_onEnter}

# tfsm_FSMClock class attributes and methods

# tfsm_Transition class attributes and methods
tfsm_Transition_action: Property = Property(name="action", type=StringType)
tfsm_Transition_m_fire: Method = Method(name="fire", parameters={}, type=StringType)
tfsm_Transition.attributes={tfsm_Transition_action}
tfsm_Transition.methods={tfsm_Transition_m_fire}

# tfsm_Guard class attributes and methods

# tfsm_NamedElement class attributes and methods
tfsm_NamedElement_name: Property = Property(name="name", type=StringType)
tfsm_NamedElement.attributes={tfsm_NamedElement_name}

# tfsm_TemporalGuard class attributes and methods
tfsm_TemporalGuard_afterDuration: Property = Property(name="afterDuration", type=IntegerType)
tfsm_TemporalGuard.attributes={tfsm_TemporalGuard_afterDuration}

# Guard class attributes and methods

# tfsm_FSMEvent class attributes and methods

# tfsm_System class attributes and methods

# tfsm_EventGuard class attributes and methods

# Relationships
ownedClock4: BinaryAssociation = BinaryAssociation(
    name="ownedClock4",
    ends={
        Property(name="tfsm_FSMClock", type=tfsm_TFSM, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_TFSM5", type=tfsm_FSMClock, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
owningFSM6: BinaryAssociation = BinaryAssociation(
    name="owningFSM6",
    ends={
        Property(name="TFSM", type=tfsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedState", type=tfsm_TFSM, multiplicity=Multiplicity(1, 1))
    }
)
outgoingTransition7: BinaryAssociation = BinaryAssociation(
    name="outgoingTransition7",
    ends={
        Property(name="Transition", type=tfsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=tfsm_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
incomingTransition8: BinaryAssociation = BinaryAssociation(
    name="incomingTransition8",
    ends={
        Property(name="Transition9", type=tfsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=tfsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
source10: BinaryAssociation = BinaryAssociation(
    name="source10",
    ends={
        Property(name="State11", type=tfsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingTransition", type=tfsm_State, multiplicity=Multiplicity(1, 1))
    }
)
target12: BinaryAssociation = BinaryAssociation(
    name="target12",
    ends={
        Property(name="State13", type=tfsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingTransition", type=tfsm_State, multiplicity=Multiplicity(1, 1))
    }
)
ownedGuard14: BinaryAssociation = BinaryAssociation(
    name="ownedGuard14",
    ends={
        Property(name="tfsm_Guard", type=tfsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_Transition", type=tfsm_Guard, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
generatedEvents15: BinaryAssociation = BinaryAssociation(
    name="generatedEvents15",
    ends={
        Property(name="FSMEvent", type=tfsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="sollicitingTransitions", type=tfsm_FSMEvent, multiplicity=Multiplicity(0, 9999))
    }
)
onClock16: BinaryAssociation = BinaryAssociation(
    name="onClock16",
    ends={
        Property(name="tfsm_FSMClock17", type=tfsm_TemporalGuard, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_TemporalGuard", type=tfsm_FSMClock, multiplicity=Multiplicity(1, 1))
    }
)
ownedState0: BinaryAssociation = BinaryAssociation(
    name="ownedState0",
    ends={
        Property(name="State", type=tfsm_TFSM, multiplicity=Multiplicity(1, 1)),
        Property(name="owningFSM", type=tfsm_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialState1: BinaryAssociation = BinaryAssociation(
    name="initialState1",
    ends={
        Property(name="tfsm_State", type=tfsm_TFSM, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_TFSM", type=tfsm_State, multiplicity=Multiplicity(1, 1))
    }
)
ownedEvents2: BinaryAssociation = BinaryAssociation(
    name="ownedEvents2",
    ends={
        Property(name="tfsm_FSMEvent", type=tfsm_TFSM, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_TFSM3", type=tfsm_FSMEvent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tfsms22: BinaryAssociation = BinaryAssociation(
    name="tfsms22",
    ends={
        Property(name="tfsm_TFSM23", type=tfsm_System, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_System", type=tfsm_TFSM, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
globalClocks24: BinaryAssociation = BinaryAssociation(
    name="globalClocks24",
    ends={
        Property(name="tfsm_FSMClock26", type=tfsm_System, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_System25", type=tfsm_FSMClock, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
globalEvent27: BinaryAssociation = BinaryAssociation(
    name="globalEvent27",
    ends={
        Property(name="tfsm_FSMEvent29", type=tfsm_System, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_System28", type=tfsm_FSMEvent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triggeringEvent18: BinaryAssociation = BinaryAssociation(
    name="triggeringEvent18",
    ends={
        Property(name="tfsm_FSMEvent19", type=tfsm_EventGuard, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_EventGuard", type=tfsm_FSMEvent, multiplicity=Multiplicity(1, 1))
    }
)
sollicitingTransitions20: BinaryAssociation = BinaryAssociation(
    name="sollicitingTransitions20",
    ends={
        Property(name="Transition21", type=tfsm_FSMEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="generatedEvents", type=tfsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_tfsm_TFSM_NamedElement = Generalization(general=NamedElement, specific=tfsm_TFSM)
gen_tfsm_State_NamedElement = Generalization(general=NamedElement, specific=tfsm_State)
gen_tfsm_Transition_NamedElement = Generalization(general=NamedElement, specific=tfsm_Transition)
gen_tfsm_Guard_NamedElement = Generalization(general=NamedElement, specific=tfsm_Guard)
gen_tfsm_TemporalGuard_Guard = Generalization(general=Guard, specific=tfsm_TemporalGuard)
gen_tfsm_FSMClock_NamedElement = Generalization(general=NamedElement, specific=tfsm_FSMClock)
gen_tfsm_EventGuard_Guard = Generalization(general=Guard, specific=tfsm_EventGuard)
gen_tfsm_FSMEvent_NamedElement = Generalization(general=NamedElement, specific=tfsm_FSMEvent)

# Domain Model
domain_model = DomainModel(
    name="tfsm",
    types={tfsm_TFSM, NamedElement, tfsm_State, tfsm_FSMClock, tfsm_Transition, tfsm_Guard, tfsm_NamedElement, tfsm_TemporalGuard, Guard, tfsm_FSMEvent, tfsm_System, tfsm_EventGuard},
    associations={ownedClock4, owningFSM6, outgoingTransition7, incomingTransition8, source10, target12, ownedGuard14, generatedEvents15, onClock16, ownedState0, initialState1, ownedEvents2, tfsms22, globalClocks24, globalEvent27, triggeringEvent18, sollicitingTransitions20},
    generalizations={gen_tfsm_TFSM_NamedElement, gen_tfsm_State_NamedElement, gen_tfsm_Transition_NamedElement, gen_tfsm_Guard_NamedElement, gen_tfsm_TemporalGuard_Guard, gen_tfsm_FSMClock_NamedElement, gen_tfsm_EventGuard_Guard, gen_tfsm_FSMEvent_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)