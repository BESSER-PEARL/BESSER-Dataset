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
tfsm_State = Class(name="tfsm::State")
tfsm_FSMEvent = Class(name="tfsm::FSMEvent")
tfsm_FSMClock = Class(name="tfsm::FSMClock")
tfsm_Transition = Class(name="tfsm::Transition")
tfsm_TFSM = Class(name="tfsm::TFSM")
NamedElement = Class(name="NamedElement")
tfsm_Guard = Class(name="tfsm::Guard", is_abstract=True)
tfsm_NamedElement = Class(name="tfsm::NamedElement", is_abstract=True)
tfsm_TemporalGuard = Class(name="tfsm::TemporalGuard")
Guard = Class(name="Guard")
tfsm_EvaluateGuard = Class(name="tfsm::EvaluateGuard")
tfsm_EventGuard = Class(name="tfsm::EventGuard")
tfsm_TimedSystem = Class(name="tfsm::TimedSystem")

# tfsm_State class attributes and methods
tfsm_State_m_onEnter: Method = Method(name="onEnter", parameters={})
tfsm_State_m_onLeave: Method = Method(name="onLeave", parameters={})
tfsm_State.methods={tfsm_State_m_onLeave, tfsm_State_m_onEnter}

# tfsm_FSMEvent class attributes and methods
tfsm_FSMEvent_m_occurs: Method = Method(name="occurs", parameters={})
tfsm_FSMEvent.methods={tfsm_FSMEvent_m_occurs}

# tfsm_FSMClock class attributes and methods
tfsm_FSMClock_numberOfTicks: Property = Property(name="numberOfTicks", type=BooleanType)
tfsm_FSMClock_m_ticks: Method = Method(name="ticks", parameters={})
tfsm_FSMClock.attributes={tfsm_FSMClock_numberOfTicks}
tfsm_FSMClock.methods={tfsm_FSMClock_m_ticks}

# tfsm_Transition class attributes and methods
tfsm_Transition_action: Property = Property(name="action", type=StringType)
tfsm_Transition_m_fire: Method = Method(name="fire", parameters={})
tfsm_Transition.attributes={tfsm_Transition_action}
tfsm_Transition.methods={tfsm_Transition_m_fire}

# tfsm_TFSM class attributes and methods
tfsm_TFSM_m_initialize: Method = Method(name="initialize", parameters={})
tfsm_TFSM_m_changeCurrentState: Method = Method(name="changeCurrentState", parameters={Parameter(name='newState')})
tfsm_TFSM.methods={tfsm_TFSM_m_changeCurrentState, tfsm_TFSM_m_initialize}

# NamedElement class attributes and methods

# tfsm_Guard class attributes and methods

# tfsm_NamedElement class attributes and methods
tfsm_NamedElement_name: Property = Property(name="name", type=StringType)
tfsm_NamedElement.attributes={tfsm_NamedElement_name}

# tfsm_TemporalGuard class attributes and methods
tfsm_TemporalGuard_afterDuration: Property = Property(name="afterDuration", type=StringType)
tfsm_TemporalGuard.attributes={tfsm_TemporalGuard_afterDuration}

# Guard class attributes and methods

# tfsm_EvaluateGuard class attributes and methods
tfsm_EvaluateGuard_condition: Property = Property(name="condition", type=StringType)
tfsm_EvaluateGuard_m_evaluate: Method = Method(name="evaluate", parameters={})
tfsm_EvaluateGuard.attributes={tfsm_EvaluateGuard_condition}
tfsm_EvaluateGuard.methods={tfsm_EvaluateGuard_m_evaluate}

# tfsm_EventGuard class attributes and methods

# tfsm_TimedSystem class attributes and methods
tfsm_TimedSystem_m_initialize: Method = Method(name="initialize", parameters={})
tfsm_TimedSystem.methods={tfsm_TimedSystem_m_initialize}

# Relationships
ownedStates0: BinaryAssociation = BinaryAssociation(
    name="ownedStates0",
    ends={
        Property(name="1", type=tfsm_TFSM, multiplicity=Multiplicity(1, 1)),
        Property(name="", type=tfsm_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialState2: BinaryAssociation = BinaryAssociation(
    name="initialState2",
    ends={
        Property(name="tfsm_State", type=tfsm_TFSM, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_TFSM", type=tfsm_State, multiplicity=Multiplicity(1, 1))
    }
)
localEvents3: BinaryAssociation = BinaryAssociation(
    name="localEvents3",
    ends={
        Property(name="tfsm_FSMEvent", type=tfsm_TFSM, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_TFSM4", type=tfsm_FSMEvent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
localClock5: BinaryAssociation = BinaryAssociation(
    name="localClock5",
    ends={
        Property(name="tfsm_FSMClock", type=tfsm_TFSM, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_TFSM6", type=tfsm_FSMClock, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ownedTransitions7: BinaryAssociation = BinaryAssociation(
    name="ownedTransitions7",
    ends={
        Property(name="tfsm_Transition", type=tfsm_TFSM, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_TFSM8", type=tfsm_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
currentState9: BinaryAssociation = BinaryAssociation(
    name="currentState9",
    ends={
        Property(name="tfsm_State11", type=tfsm_TFSM, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_TFSM10", type=tfsm_State, multiplicity=Multiplicity(0, 1))
    }
)
source21: BinaryAssociation = BinaryAssociation(
    name="source21",
    ends={
        Property(name="23", type=tfsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="22", type=tfsm_State, multiplicity=Multiplicity(1, 1))
    }
)
target24: BinaryAssociation = BinaryAssociation(
    name="target24",
    ends={
        Property(name="26", type=tfsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="25", type=tfsm_State, multiplicity=Multiplicity(1, 1))
    }
)
ownedGuard27: BinaryAssociation = BinaryAssociation(
    name="ownedGuard27",
    ends={
        Property(name="tfsm_Guard", type=tfsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_Transition28", type=tfsm_Guard, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
generatedEvents29: BinaryAssociation = BinaryAssociation(
    name="generatedEvents29",
    ends={
        Property(name="tfsm_FSMEvent31", type=tfsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_Transition30", type=tfsm_FSMEvent, multiplicity=Multiplicity(0, 9999))
    }
)
onClock32: BinaryAssociation = BinaryAssociation(
    name="onClock32",
    ends={
        Property(name="tfsm_FSMClock33", type=tfsm_TemporalGuard, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_TemporalGuard", type=tfsm_FSMClock, multiplicity=Multiplicity(1, 1))
    }
)
owningFSM12: BinaryAssociation = BinaryAssociation(
    name="owningFSM12",
    ends={
        Property(name="14", type=tfsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="13", type=tfsm_TFSM, multiplicity=Multiplicity(1, 1))
    }
)
outgoingTransitions15: BinaryAssociation = BinaryAssociation(
    name="outgoingTransitions15",
    ends={
        Property(name="17", type=tfsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="16", type=tfsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
incomingTransitions18: BinaryAssociation = BinaryAssociation(
    name="incomingTransitions18",
    ends={
        Property(name="20", type=tfsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="19", type=tfsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
tfsms39: BinaryAssociation = BinaryAssociation(
    name="tfsms39",
    ends={
        Property(name="tfsm_TFSM40", type=tfsm_TimedSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_TimedSystem", type=tfsm_TFSM, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
globalClocks41: BinaryAssociation = BinaryAssociation(
    name="globalClocks41",
    ends={
        Property(name="tfsm_FSMClock43", type=tfsm_TimedSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_TimedSystem42", type=tfsm_FSMClock, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
globalEvents44: BinaryAssociation = BinaryAssociation(
    name="globalEvents44",
    ends={
        Property(name="tfsm_FSMEvent46", type=tfsm_TimedSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_TimedSystem45", type=tfsm_FSMEvent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triggeringEvent34: BinaryAssociation = BinaryAssociation(
    name="triggeringEvent34",
    ends={
        Property(name="tfsm_FSMEvent35", type=tfsm_EventGuard, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_EventGuard", type=tfsm_FSMEvent, multiplicity=Multiplicity(1, 1))
    }
)
sollicitingTransitions36: BinaryAssociation = BinaryAssociation(
    name="sollicitingTransitions36",
    ends={
        Property(name="tfsm_Transition38", type=tfsm_FSMEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_FSMEvent37", type=tfsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_tfsm_TFSM_NamedElement = Generalization(general=NamedElement, specific=tfsm_TFSM)
gen_tfsm_Guard_NamedElement = Generalization(general=NamedElement, specific=tfsm_Guard)
gen_tfsm_TemporalGuard_Guard = Generalization(general=Guard, specific=tfsm_TemporalGuard)
gen_tfsm_State_NamedElement = Generalization(general=NamedElement, specific=tfsm_State)
gen_tfsm_Transition_NamedElement = Generalization(general=NamedElement, specific=tfsm_Transition)
gen_tfsm_EvaluateGuard_Guard = Generalization(general=Guard, specific=tfsm_EvaluateGuard)
gen_tfsm_EventGuard_Guard = Generalization(general=Guard, specific=tfsm_EventGuard)
gen_tfsm_FSMEvent_NamedElement = Generalization(general=NamedElement, specific=tfsm_FSMEvent)
gen_tfsm_FSMClock_NamedElement = Generalization(general=NamedElement, specific=tfsm_FSMClock)
gen_tfsm_TimedSystem_NamedElement = Generalization(general=NamedElement, specific=tfsm_TimedSystem)

# Domain Model
domain_model = DomainModel(
    name="tfsm",
    types={tfsm_State, tfsm_FSMEvent, tfsm_FSMClock, tfsm_Transition, tfsm_TFSM, NamedElement, tfsm_Guard, tfsm_NamedElement, tfsm_TemporalGuard, Guard, tfsm_EvaluateGuard, tfsm_EventGuard, tfsm_TimedSystem},
    associations={ownedStates0, initialState2, localEvents3, localClock5, ownedTransitions7, currentState9, source21, target24, ownedGuard27, generatedEvents29, onClock32, owningFSM12, outgoingTransitions15, incomingTransitions18, tfsms39, globalClocks41, globalEvents44, triggeringEvent34, sollicitingTransitions36},
    generalizations={gen_tfsm_TFSM_NamedElement, gen_tfsm_Guard_NamedElement, gen_tfsm_TemporalGuard_Guard, gen_tfsm_State_NamedElement, gen_tfsm_Transition_NamedElement, gen_tfsm_EvaluateGuard_Guard, gen_tfsm_EventGuard_Guard, gen_tfsm_FSMEvent_NamedElement, gen_tfsm_FSMClock_NamedElement, gen_tfsm_TimedSystem_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)