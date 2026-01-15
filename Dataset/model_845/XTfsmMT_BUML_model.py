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
tfsm_plaink3_State = Class(name="tfsm::plaink3::State")
tfsm_plaink3_TFSM = Class(name="tfsm::plaink3::TFSM")
NamedElement = Class(name="NamedElement")
tfsm_plaink3_FSMEvent = Class(name="tfsm::plaink3::FSMEvent")
tfsm_plaink3_FSMClock = Class(name="tfsm::plaink3::FSMClock")
tfsm_plaink3_Transition = Class(name="tfsm::plaink3::Transition")
tfsm_plaink3_Guard = Class(name="tfsm::plaink3::Guard", is_abstract=True)
tfsm_plaink3_NamedElement = Class(name="tfsm::plaink3::NamedElement", is_abstract=True)
tfsm_plaink3_TemporalGuard = Class(name="tfsm::plaink3::TemporalGuard")
Guard = Class(name="Guard")
tfsm_plaink3_EventGuard = Class(name="tfsm::plaink3::EventGuard")
tfsm_plaink3_EvaluateGuard = Class(name="tfsm::plaink3::EvaluateGuard")
tfsm_plaink3_TimedSystem = Class(name="tfsm::plaink3::TimedSystem")

# tfsm_plaink3_State class attributes and methods
tfsm_plaink3_State_m_onEnter: Method = Method(name="onEnter", parameters={})
tfsm_plaink3_State_m_onLeave: Method = Method(name="onLeave", parameters={})
tfsm_plaink3_State_m_visit: Method = Method(name="visit", parameters={})
tfsm_plaink3_State.methods={tfsm_plaink3_State_m_visit, tfsm_plaink3_State_m_onEnter, tfsm_plaink3_State_m_onLeave}

# tfsm_plaink3_TFSM class attributes and methods
tfsm_plaink3_TFSM_stepNumber: Property = Property(name="stepNumber", type=IntegerType)
tfsm_plaink3_TFSM_lastStateChangeStepNumber: Property = Property(name="lastStateChangeStepNumber", type=IntegerType)
tfsm_plaink3_TFSM_m_visit: Method = Method(name="visit", parameters={})
tfsm_plaink3_TFSM_m_init: Method = Method(name="init", parameters={})
tfsm_plaink3_TFSM.attributes={tfsm_plaink3_TFSM_lastStateChangeStepNumber, tfsm_plaink3_TFSM_stepNumber}
tfsm_plaink3_TFSM.methods={tfsm_plaink3_TFSM_m_visit, tfsm_plaink3_TFSM_m_init}

# NamedElement class attributes and methods

# tfsm_plaink3_FSMEvent class attributes and methods
tfsm_plaink3_FSMEvent_isTriggered: Property = Property(name="isTriggered", type=StringType)
tfsm_plaink3_FSMEvent_m_trigger: Method = Method(name="trigger", parameters={})
tfsm_plaink3_FSMEvent_m_unTrigger: Method = Method(name="unTrigger", parameters={})
tfsm_plaink3_FSMEvent.attributes={tfsm_plaink3_FSMEvent_isTriggered}
tfsm_plaink3_FSMEvent.methods={tfsm_plaink3_FSMEvent_m_trigger, tfsm_plaink3_FSMEvent_m_unTrigger}

# tfsm_plaink3_FSMClock class attributes and methods
tfsm_plaink3_FSMClock_numberOfTicks: Property = Property(name="numberOfTicks", type=StringType)
tfsm_plaink3_FSMClock_m_ticks: Method = Method(name="ticks", parameters={})
tfsm_plaink3_FSMClock_m_visit: Method = Method(name="visit", parameters={})
tfsm_plaink3_FSMClock.attributes={tfsm_plaink3_FSMClock_numberOfTicks}
tfsm_plaink3_FSMClock.methods={tfsm_plaink3_FSMClock_m_visit, tfsm_plaink3_FSMClock_m_ticks}

# tfsm_plaink3_Transition class attributes and methods
tfsm_plaink3_Transition_action: Property = Property(name="action", type=StringType)
tfsm_plaink3_Transition_m_fire: Method = Method(name="fire", parameters={})
tfsm_plaink3_Transition_m_visit: Method = Method(name="visit", parameters={})
tfsm_plaink3_Transition.attributes={tfsm_plaink3_Transition_action}
tfsm_plaink3_Transition.methods={tfsm_plaink3_Transition_m_visit, tfsm_plaink3_Transition_m_fire}

# tfsm_plaink3_Guard class attributes and methods
tfsm_plaink3_Guard_m_visit: Method = Method(name="visit", parameters={})
tfsm_plaink3_Guard.methods={tfsm_plaink3_Guard_m_visit}

# tfsm_plaink3_NamedElement class attributes and methods
tfsm_plaink3_NamedElement_name: Property = Property(name="name", type=StringType)
tfsm_plaink3_NamedElement.attributes={tfsm_plaink3_NamedElement_name}

# tfsm_plaink3_TemporalGuard class attributes and methods
tfsm_plaink3_TemporalGuard_afterDuration: Property = Property(name="afterDuration", type=IntegerType)
tfsm_plaink3_TemporalGuard_m_visit: Method = Method(name="visit", parameters={})
tfsm_plaink3_TemporalGuard.attributes={tfsm_plaink3_TemporalGuard_afterDuration}
tfsm_plaink3_TemporalGuard.methods={tfsm_plaink3_TemporalGuard_m_visit}

# Guard class attributes and methods

# tfsm_plaink3_EventGuard class attributes and methods
tfsm_plaink3_EventGuard_m_visit: Method = Method(name="visit", parameters={})
tfsm_plaink3_EventGuard.methods={tfsm_plaink3_EventGuard_m_visit}

# tfsm_plaink3_EvaluateGuard class attributes and methods
tfsm_plaink3_EvaluateGuard_condition: Property = Property(name="condition", type=StringType)
tfsm_plaink3_EvaluateGuard.attributes={tfsm_plaink3_EvaluateGuard_condition}

# tfsm_plaink3_TimedSystem class attributes and methods
tfsm_plaink3_TimedSystem_m_initializeModel: Method = Method(name="initializeModel", parameters={Parameter(name='args')})
tfsm_plaink3_TimedSystem_m_visit: Method = Method(name="visit", parameters={})
tfsm_plaink3_TimedSystem_m_main: Method = Method(name="main", parameters={})
tfsm_plaink3_TimedSystem.methods={tfsm_plaink3_TimedSystem_m_main, tfsm_plaink3_TimedSystem_m_initializeModel, tfsm_plaink3_TimedSystem_m_visit}

# Relationships
ownedStates0: BinaryAssociation = BinaryAssociation(
    name="ownedStates0",
    ends={
        Property(name="1", type=tfsm_plaink3_TFSM, multiplicity=Multiplicity(1, 1)),
        Property(name="", type=tfsm_plaink3_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialState2: BinaryAssociation = BinaryAssociation(
    name="initialState2",
    ends={
        Property(name="tfsm_plaink3_State", type=tfsm_plaink3_TFSM, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_plaink3_TFSM", type=tfsm_plaink3_State, multiplicity=Multiplicity(1, 1))
    }
)
localEvents3: BinaryAssociation = BinaryAssociation(
    name="localEvents3",
    ends={
        Property(name="tfsm_plaink3_FSMEvent", type=tfsm_plaink3_TFSM, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_plaink3_TFSM4", type=tfsm_plaink3_FSMEvent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
localClock5: BinaryAssociation = BinaryAssociation(
    name="localClock5",
    ends={
        Property(name="tfsm_plaink3_FSMClock", type=tfsm_plaink3_TFSM, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_plaink3_TFSM6", type=tfsm_plaink3_FSMClock, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ownedTransitions7: BinaryAssociation = BinaryAssociation(
    name="ownedTransitions7",
    ends={
        Property(name="tfsm_plaink3_Transition", type=tfsm_plaink3_TFSM, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_plaink3_TFSM8", type=tfsm_plaink3_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
currentState9: BinaryAssociation = BinaryAssociation(
    name="currentState9",
    ends={
        Property(name="tfsm_plaink3_State11", type=tfsm_plaink3_TFSM, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_plaink3_TFSM10", type=tfsm_plaink3_State, multiplicity=Multiplicity(0, 1))
    }
)
owningFSM12: BinaryAssociation = BinaryAssociation(
    name="owningFSM12",
    ends={
        Property(name="14", type=tfsm_plaink3_State, multiplicity=Multiplicity(1, 1)),
        Property(name="13", type=tfsm_plaink3_TFSM, multiplicity=Multiplicity(1, 1))
    }
)
outgoingTransitions15: BinaryAssociation = BinaryAssociation(
    name="outgoingTransitions15",
    ends={
        Property(name="17", type=tfsm_plaink3_State, multiplicity=Multiplicity(1, 1)),
        Property(name="16", type=tfsm_plaink3_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
target24: BinaryAssociation = BinaryAssociation(
    name="target24",
    ends={
        Property(name="26", type=tfsm_plaink3_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="25", type=tfsm_plaink3_State, multiplicity=Multiplicity(1, 1))
    }
)
ownedGuard27: BinaryAssociation = BinaryAssociation(
    name="ownedGuard27",
    ends={
        Property(name="tfsm_plaink3_Guard", type=tfsm_plaink3_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_plaink3_Transition28", type=tfsm_plaink3_Guard, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
generatedEvents29: BinaryAssociation = BinaryAssociation(
    name="generatedEvents29",
    ends={
        Property(name="tfsm_plaink3_FSMEvent31", type=tfsm_plaink3_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_plaink3_Transition30", type=tfsm_plaink3_FSMEvent, multiplicity=Multiplicity(0, 9999))
    }
)
onClock32: BinaryAssociation = BinaryAssociation(
    name="onClock32",
    ends={
        Property(name="tfsm_plaink3_FSMClock33", type=tfsm_plaink3_TemporalGuard, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_plaink3_TemporalGuard", type=tfsm_plaink3_FSMClock, multiplicity=Multiplicity(1, 1))
    }
)
triggeringEvent34: BinaryAssociation = BinaryAssociation(
    name="triggeringEvent34",
    ends={
        Property(name="tfsm_plaink3_FSMEvent35", type=tfsm_plaink3_EventGuard, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_plaink3_EventGuard", type=tfsm_plaink3_FSMEvent, multiplicity=Multiplicity(1, 1))
    }
)
sollicitingTransitions36: BinaryAssociation = BinaryAssociation(
    name="sollicitingTransitions36",
    ends={
        Property(name="tfsm_plaink3_Transition38", type=tfsm_plaink3_FSMEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_plaink3_FSMEvent37", type=tfsm_plaink3_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
incomingTransitions18: BinaryAssociation = BinaryAssociation(
    name="incomingTransitions18",
    ends={
        Property(name="20", type=tfsm_plaink3_State, multiplicity=Multiplicity(1, 1)),
        Property(name="19", type=tfsm_plaink3_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
source21: BinaryAssociation = BinaryAssociation(
    name="source21",
    ends={
        Property(name="23", type=tfsm_plaink3_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="22", type=tfsm_plaink3_State, multiplicity=Multiplicity(1, 1))
    }
)
tfsms39: BinaryAssociation = BinaryAssociation(
    name="tfsms39",
    ends={
        Property(name="tfsm_plaink3_TFSM40", type=tfsm_plaink3_TimedSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_plaink3_TimedSystem", type=tfsm_plaink3_TFSM, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
globalClocks41: BinaryAssociation = BinaryAssociation(
    name="globalClocks41",
    ends={
        Property(name="tfsm_plaink3_FSMClock43", type=tfsm_plaink3_TimedSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_plaink3_TimedSystem42", type=tfsm_plaink3_FSMClock, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
globalEvents44: BinaryAssociation = BinaryAssociation(
    name="globalEvents44",
    ends={
        Property(name="tfsm_plaink3_FSMEvent46", type=tfsm_plaink3_TimedSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_plaink3_TimedSystem45", type=tfsm_plaink3_FSMEvent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_tfsm_plaink3_TFSM_NamedElement = Generalization(general=NamedElement, specific=tfsm_plaink3_TFSM)
gen_tfsm_plaink3_State_NamedElement = Generalization(general=NamedElement, specific=tfsm_plaink3_State)
gen_tfsm_plaink3_Guard_NamedElement = Generalization(general=NamedElement, specific=tfsm_plaink3_Guard)
gen_tfsm_plaink3_TemporalGuard_Guard = Generalization(general=Guard, specific=tfsm_plaink3_TemporalGuard)
gen_tfsm_plaink3_EventGuard_Guard = Generalization(general=Guard, specific=tfsm_plaink3_EventGuard)
gen_tfsm_plaink3_FSMEvent_NamedElement = Generalization(general=NamedElement, specific=tfsm_plaink3_FSMEvent)
gen_tfsm_plaink3_Transition_NamedElement = Generalization(general=NamedElement, specific=tfsm_plaink3_Transition)
gen_tfsm_plaink3_EvaluateGuard_Guard = Generalization(general=Guard, specific=tfsm_plaink3_EvaluateGuard)
gen_tfsm_plaink3_FSMClock_NamedElement = Generalization(general=NamedElement, specific=tfsm_plaink3_FSMClock)
gen_tfsm_plaink3_TimedSystem_NamedElement = Generalization(general=NamedElement, specific=tfsm_plaink3_TimedSystem)

# Domain Model
domain_model = DomainModel(
    name="tfsm_plaink3",
    types={tfsm_plaink3_State, tfsm_plaink3_TFSM, NamedElement, tfsm_plaink3_FSMEvent, tfsm_plaink3_FSMClock, tfsm_plaink3_Transition, tfsm_plaink3_Guard, tfsm_plaink3_NamedElement, tfsm_plaink3_TemporalGuard, Guard, tfsm_plaink3_EventGuard, tfsm_plaink3_EvaluateGuard, tfsm_plaink3_TimedSystem},
    associations={ownedStates0, initialState2, localEvents3, localClock5, ownedTransitions7, currentState9, owningFSM12, outgoingTransitions15, target24, ownedGuard27, generatedEvents29, onClock32, triggeringEvent34, sollicitingTransitions36, incomingTransitions18, source21, tfsms39, globalClocks41, globalEvents44},
    generalizations={gen_tfsm_plaink3_TFSM_NamedElement, gen_tfsm_plaink3_State_NamedElement, gen_tfsm_plaink3_Guard_NamedElement, gen_tfsm_plaink3_TemporalGuard_Guard, gen_tfsm_plaink3_EventGuard_Guard, gen_tfsm_plaink3_FSMEvent_NamedElement, gen_tfsm_plaink3_Transition_NamedElement, gen_tfsm_plaink3_EvaluateGuard_Guard, gen_tfsm_plaink3_FSMClock_NamedElement, gen_tfsm_plaink3_TimedSystem_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)