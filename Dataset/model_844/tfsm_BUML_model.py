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
tfsm_Guard = Class(name="tfsm::Guard", is_abstract=True)
tfsm_NamedElement = Class(name="tfsm::NamedElement", is_abstract=True)
tfsm_TemporalGuard = Class(name="tfsm::TemporalGuard")
Guard = Class(name="Guard")
tfsm_EventGuard = Class(name="tfsm::EventGuard")
tfsm_FSMEvent = Class(name="tfsm::FSMEvent")
tfsm_FSMClock = Class(name="tfsm::FSMClock")
tfsm_Transition = Class(name="tfsm::Transition")
tfsm_TimedSystem = Class(name="tfsm::TimedSystem")
tfsm_EvaluateGuard = Class(name="tfsm::EvaluateGuard")

# tfsm_TFSM class attributes and methods
tfsm_TFSM_m_initialize: Method = Method(name="initialize", parameters={})
tfsm_TFSM.methods={tfsm_TFSM_m_initialize}

# NamedElement class attributes and methods

# tfsm_State class attributes and methods
tfsm_State_m_onEnter: Method = Method(name="onEnter", parameters={})
tfsm_State_m_onLeave: Method = Method(name="onLeave", parameters={})
tfsm_State.methods={tfsm_State_m_onLeave, tfsm_State_m_onEnter}

# tfsm_Guard class attributes and methods

# tfsm_NamedElement class attributes and methods
tfsm_NamedElement_name: Property = Property(name="name", type=StringType)
tfsm_NamedElement.attributes={tfsm_NamedElement_name}

# tfsm_TemporalGuard class attributes and methods
tfsm_TemporalGuard_afterDuration: Property = Property(name="afterDuration", type=IntegerType)
tfsm_TemporalGuard.attributes={tfsm_TemporalGuard_afterDuration}

# Guard class attributes and methods

# tfsm_EventGuard class attributes and methods

# tfsm_FSMEvent class attributes and methods
tfsm_FSMEvent_m_occurs: Method = Method(name="occurs", parameters={})
tfsm_FSMEvent.methods={tfsm_FSMEvent_m_occurs}

# tfsm_FSMClock class attributes and methods
tfsm_FSMClock_m_ticks: Method = Method(name="ticks", parameters={})
tfsm_FSMClock.methods={tfsm_FSMClock_m_ticks}

# tfsm_Transition class attributes and methods
tfsm_Transition_action: Property = Property(name="action", type=StringType)
tfsm_Transition_m_fire: Method = Method(name="fire", parameters={})
tfsm_Transition.attributes={tfsm_Transition_action}
tfsm_Transition.methods={tfsm_Transition_m_fire}

# tfsm_TimedSystem class attributes and methods
tfsm_TimedSystem_m_initialize: Method = Method(name="initialize", parameters={})
tfsm_TimedSystem.methods={tfsm_TimedSystem_m_initialize}

# tfsm_EvaluateGuard class attributes and methods
tfsm_EvaluateGuard_condition: Property = Property(name="condition", type=StringType)
tfsm_EvaluateGuard_m_evaluate: Method = Method(name="evaluate", parameters={}, type=BooleanType)
tfsm_EvaluateGuard.attributes={tfsm_EvaluateGuard_condition}
tfsm_EvaluateGuard.methods={tfsm_EvaluateGuard_m_evaluate}

# Relationships
ownedStates0: BinaryAssociation = BinaryAssociation(
    name="ownedStates0",
    ends={
        Property(name="State", type=tfsm_TFSM, multiplicity=Multiplicity(1, 1)),
        Property(name="owningFSM", type=tfsm_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source12: BinaryAssociation = BinaryAssociation(
    name="source12",
    ends={
        Property(name="State13", type=tfsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingTransitions", type=tfsm_State, multiplicity=Multiplicity(1, 1))
    }
)
target14: BinaryAssociation = BinaryAssociation(
    name="target14",
    ends={
        Property(name="State15", type=tfsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingTransitions", type=tfsm_State, multiplicity=Multiplicity(1, 1))
    }
)
ownedGuard16: BinaryAssociation = BinaryAssociation(
    name="ownedGuard16",
    ends={
        Property(name="tfsm_Guard", type=tfsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_Transition17", type=tfsm_Guard, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
generatedEvents18: BinaryAssociation = BinaryAssociation(
    name="generatedEvents18",
    ends={
        Property(name="tfsm_FSMEvent20", type=tfsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_Transition19", type=tfsm_FSMEvent, multiplicity=Multiplicity(0, 9999))
    }
)
onClock21: BinaryAssociation = BinaryAssociation(
    name="onClock21",
    ends={
        Property(name="tfsm_FSMClock22", type=tfsm_TemporalGuard, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_TemporalGuard", type=tfsm_FSMClock, multiplicity=Multiplicity(1, 1))
    }
)
initialState1: BinaryAssociation = BinaryAssociation(
    name="initialState1",
    ends={
        Property(name="tfsm_State", type=tfsm_TFSM, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_TFSM", type=tfsm_State, multiplicity=Multiplicity(1, 1))
    }
)
localEvents2: BinaryAssociation = BinaryAssociation(
    name="localEvents2",
    ends={
        Property(name="tfsm_FSMEvent", type=tfsm_TFSM, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_TFSM3", type=tfsm_FSMEvent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
localClock4: BinaryAssociation = BinaryAssociation(
    name="localClock4",
    ends={
        Property(name="tfsm_FSMClock", type=tfsm_TFSM, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_TFSM5", type=tfsm_FSMClock, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ownedTransitions6: BinaryAssociation = BinaryAssociation(
    name="ownedTransitions6",
    ends={
        Property(name="tfsm_Transition", type=tfsm_TFSM, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_TFSM7", type=tfsm_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningFSM8: BinaryAssociation = BinaryAssociation(
    name="owningFSM8",
    ends={
        Property(name="TFSM", type=tfsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedStates", type=tfsm_TFSM, multiplicity=Multiplicity(1, 1))
    }
)
outgoingTransitions9: BinaryAssociation = BinaryAssociation(
    name="outgoingTransitions9",
    ends={
        Property(name="Transition", type=tfsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=tfsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
incomingTransitions10: BinaryAssociation = BinaryAssociation(
    name="incomingTransitions10",
    ends={
        Property(name="Transition11", type=tfsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=tfsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
triggeringEvent23: BinaryAssociation = BinaryAssociation(
    name="triggeringEvent23",
    ends={
        Property(name="tfsm_FSMEvent24", type=tfsm_EventGuard, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_EventGuard", type=tfsm_FSMEvent, multiplicity=Multiplicity(1, 1))
    }
)
sollicitingTransitions25: BinaryAssociation = BinaryAssociation(
    name="sollicitingTransitions25",
    ends={
        Property(name="tfsm_Transition27", type=tfsm_FSMEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_FSMEvent26", type=tfsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
tfsms28: BinaryAssociation = BinaryAssociation(
    name="tfsms28",
    ends={
        Property(name="tfsm_TFSM29", type=tfsm_TimedSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_TimedSystem", type=tfsm_TFSM, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
globalClocks30: BinaryAssociation = BinaryAssociation(
    name="globalClocks30",
    ends={
        Property(name="tfsm_FSMClock32", type=tfsm_TimedSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_TimedSystem31", type=tfsm_FSMClock, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
globalEvents33: BinaryAssociation = BinaryAssociation(
    name="globalEvents33",
    ends={
        Property(name="tfsm_FSMEvent35", type=tfsm_TimedSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_TimedSystem34", type=tfsm_FSMEvent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_tfsm_TFSM_NamedElement = Generalization(general=NamedElement, specific=tfsm_TFSM)
gen_tfsm_Guard_NamedElement = Generalization(general=NamedElement, specific=tfsm_Guard)
gen_tfsm_TemporalGuard_Guard = Generalization(general=Guard, specific=tfsm_TemporalGuard)
gen_tfsm_EventGuard_Guard = Generalization(general=Guard, specific=tfsm_EventGuard)
gen_tfsm_State_NamedElement = Generalization(general=NamedElement, specific=tfsm_State)
gen_tfsm_Transition_NamedElement = Generalization(general=NamedElement, specific=tfsm_Transition)
gen_tfsm_FSMEvent_NamedElement = Generalization(general=NamedElement, specific=tfsm_FSMEvent)
gen_tfsm_FSMClock_NamedElement = Generalization(general=NamedElement, specific=tfsm_FSMClock)
gen_tfsm_TimedSystem_NamedElement = Generalization(general=NamedElement, specific=tfsm_TimedSystem)
gen_tfsm_EvaluateGuard_Guard = Generalization(general=Guard, specific=tfsm_EvaluateGuard)

# Domain Model
domain_model = DomainModel(
    name="tfsm",
    types={tfsm_TFSM, NamedElement, tfsm_State, tfsm_Guard, tfsm_NamedElement, tfsm_TemporalGuard, Guard, tfsm_EventGuard, tfsm_FSMEvent, tfsm_FSMClock, tfsm_Transition, tfsm_TimedSystem, tfsm_EvaluateGuard},
    associations={ownedStates0, source12, target14, ownedGuard16, generatedEvents18, onClock21, initialState1, localEvents2, localClock4, ownedTransitions6, owningFSM8, outgoingTransitions9, incomingTransitions10, triggeringEvent23, sollicitingTransitions25, tfsms28, globalClocks30, globalEvents33},
    generalizations={gen_tfsm_TFSM_NamedElement, gen_tfsm_Guard_NamedElement, gen_tfsm_TemporalGuard_Guard, gen_tfsm_EventGuard_Guard, gen_tfsm_State_NamedElement, gen_tfsm_Transition_NamedElement, gen_tfsm_FSMEvent_NamedElement, gen_tfsm_FSMClock_NamedElement, gen_tfsm_TimedSystem_NamedElement, gen_tfsm_EvaluateGuard_Guard},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)