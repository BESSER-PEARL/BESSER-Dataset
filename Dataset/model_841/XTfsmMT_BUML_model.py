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
tfsm_TFSM = Class(name="tfsm_TFSM")
NamedElement = Class(name="NamedElement")
tfsm_State = Class(name="tfsm_State")
tfsm_FSMEvent = Class(name="tfsm_FSMEvent")
tfsm_FSMClock = Class(name="tfsm_FSMClock")
tfsm_Transition = Class(name="tfsm_Transition")
tfsm_Guard = Class(name="tfsm_Guard", is_abstract=True)
tfsm_NamedElement = Class(name="tfsm_NamedElement", is_abstract=True)
tfsm_TemporalGuard = Class(name="tfsm_TemporalGuard")
Guard = Class(name="Guard")
tfsm_EventGuard = Class(name="tfsm_EventGuard")
tfsm_TimedSystem = Class(name="tfsm_TimedSystem")
tfsm_EvaluateGuard = Class(name="tfsm_EvaluateGuard")

# tfsm_TFSM class attributes and methods
tfsm_TFSM_stepNumber: Property = Property(name="stepNumber", type=IntegerType)
tfsm_TFSM_lastStateChangeStepNumber: Property = Property(name="lastStateChangeStepNumber", type=IntegerType)
tfsm_TFSM_m_init: Method = Method(name="init", parameters={})
tfsm_TFSM_m_visit: Method = Method(name="visit", parameters={})
tfsm_TFSM.attributes={tfsm_TFSM_stepNumber, tfsm_TFSM_lastStateChangeStepNumber}
tfsm_TFSM.methods={tfsm_TFSM_m_visit, tfsm_TFSM_m_init}

# NamedElement class attributes and methods

# tfsm_State class attributes and methods
tfsm_State_m_onEnter: Method = Method(name="onEnter", parameters={})
tfsm_State_m_onLeave: Method = Method(name="onLeave", parameters={})
tfsm_State_m_visit: Method = Method(name="visit", parameters={})
tfsm_State.methods={tfsm_State_m_visit, tfsm_State_m_onLeave, tfsm_State_m_onEnter}

# tfsm_FSMEvent class attributes and methods
tfsm_FSMEvent_isTriggered: Property = Property(name="isTriggered", type=StringType)
tfsm_FSMEvent_m_trigger: Method = Method(name="trigger", parameters={})
tfsm_FSMEvent_m_unTrigger: Method = Method(name="unTrigger", parameters={})
tfsm_FSMEvent.attributes={tfsm_FSMEvent_isTriggered}
tfsm_FSMEvent.methods={tfsm_FSMEvent_m_trigger, tfsm_FSMEvent_m_unTrigger}

# tfsm_FSMClock class attributes and methods
tfsm_FSMClock_numberOfTicks: Property = Property(name="numberOfTicks", type=StringType)
tfsm_FSMClock_m_ticks: Method = Method(name="ticks", parameters={})
tfsm_FSMClock_m_visit: Method = Method(name="visit", parameters={})
tfsm_FSMClock.attributes={tfsm_FSMClock_numberOfTicks}
tfsm_FSMClock.methods={tfsm_FSMClock_m_ticks, tfsm_FSMClock_m_visit}

# tfsm_Transition class attributes and methods
tfsm_Transition_action: Property = Property(name="action", type=StringType)
tfsm_Transition_m_fire: Method = Method(name="fire", parameters={})
tfsm_Transition_m_visit: Method = Method(name="visit", parameters={})
tfsm_Transition.attributes={tfsm_Transition_action}
tfsm_Transition.methods={tfsm_Transition_m_visit, tfsm_Transition_m_fire}

# tfsm_Guard class attributes and methods
tfsm_Guard_m_visit: Method = Method(name="visit", parameters={})
tfsm_Guard.methods={tfsm_Guard_m_visit}

# tfsm_NamedElement class attributes and methods
tfsm_NamedElement_name: Property = Property(name="name", type=StringType)
tfsm_NamedElement.attributes={tfsm_NamedElement_name}

# tfsm_TemporalGuard class attributes and methods
tfsm_TemporalGuard_afterDuration: Property = Property(name="afterDuration", type=IntegerType)
tfsm_TemporalGuard_m_visit: Method = Method(name="visit", parameters={})
tfsm_TemporalGuard.attributes={tfsm_TemporalGuard_afterDuration}
tfsm_TemporalGuard.methods={tfsm_TemporalGuard_m_visit}

# Guard class attributes and methods

# tfsm_EventGuard class attributes and methods
tfsm_EventGuard_m_visit: Method = Method(name="visit", parameters={})
tfsm_EventGuard.methods={tfsm_EventGuard_m_visit}

# tfsm_TimedSystem class attributes and methods
tfsm_TimedSystem_m_main: Method = Method(name="main", parameters={})
tfsm_TimedSystem_m_initializeModel: Method = Method(name="initializeModel", parameters={Parameter(name='tfsm_args', type=StringType)})
tfsm_TimedSystem_m_visit: Method = Method(name="visit", parameters={})
tfsm_TimedSystem.methods={tfsm_TimedSystem_m_initializeModel, tfsm_TimedSystem_m_main, tfsm_TimedSystem_m_visit}

# tfsm_EvaluateGuard class attributes and methods
tfsm_EvaluateGuard_condition: Property = Property(name="condition", type=StringType)
tfsm_EvaluateGuard.attributes={tfsm_EvaluateGuard_condition}

# Relationships
ownedStates0: BinaryAssociation = BinaryAssociation(
    name="ownedStates0",
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
currentState8: BinaryAssociation = BinaryAssociation(
    name="currentState8",
    ends={
        Property(name="tfsm_State10", type=tfsm_TFSM, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_TFSM9", type=tfsm_State, multiplicity=Multiplicity(0, 1))
    }
)
owningFSM11: BinaryAssociation = BinaryAssociation(
    name="owningFSM11",
    ends={
        Property(name="TFSM", type=tfsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedStates", type=tfsm_TFSM, multiplicity=Multiplicity(1, 1))
    }
)
outgoingTransitions12: BinaryAssociation = BinaryAssociation(
    name="outgoingTransitions12",
    ends={
        Property(name="Transition", type=tfsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=tfsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
incomingTransitions13: BinaryAssociation = BinaryAssociation(
    name="incomingTransitions13",
    ends={
        Property(name="Transition14", type=tfsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=tfsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
source15: BinaryAssociation = BinaryAssociation(
    name="source15",
    ends={
        Property(name="State16", type=tfsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingTransitions", type=tfsm_State, multiplicity=Multiplicity(1, 1))
    }
)
target17: BinaryAssociation = BinaryAssociation(
    name="target17",
    ends={
        Property(name="State18", type=tfsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingTransitions", type=tfsm_State, multiplicity=Multiplicity(1, 1))
    }
)
ownedGuard19: BinaryAssociation = BinaryAssociation(
    name="ownedGuard19",
    ends={
        Property(name="tfsm_Guard", type=tfsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_Transition20", type=tfsm_Guard, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
generatedEvents21: BinaryAssociation = BinaryAssociation(
    name="generatedEvents21",
    ends={
        Property(name="tfsm_FSMEvent23", type=tfsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_Transition22", type=tfsm_FSMEvent, multiplicity=Multiplicity(0, 9999))
    }
)
globalEvents36: BinaryAssociation = BinaryAssociation(
    name="globalEvents36",
    ends={
        Property(name="tfsm_FSMEvent38", type=tfsm_TimedSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_TimedSystem37", type=tfsm_FSMEvent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
onClock24: BinaryAssociation = BinaryAssociation(
    name="onClock24",
    ends={
        Property(name="tfsm_FSMClock25", type=tfsm_TemporalGuard, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_TemporalGuard", type=tfsm_FSMClock, multiplicity=Multiplicity(1, 1))
    }
)
triggeringEvent26: BinaryAssociation = BinaryAssociation(
    name="triggeringEvent26",
    ends={
        Property(name="tfsm_FSMEvent27", type=tfsm_EventGuard, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_EventGuard", type=tfsm_FSMEvent, multiplicity=Multiplicity(1, 1))
    }
)
sollicitingTransitions28: BinaryAssociation = BinaryAssociation(
    name="sollicitingTransitions28",
    ends={
        Property(name="tfsm_Transition30", type=tfsm_FSMEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_FSMEvent29", type=tfsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
tfsms31: BinaryAssociation = BinaryAssociation(
    name="tfsms31",
    ends={
        Property(name="tfsm_TFSM32", type=tfsm_TimedSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_TimedSystem", type=tfsm_TFSM, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
globalClocks33: BinaryAssociation = BinaryAssociation(
    name="globalClocks33",
    ends={
        Property(name="tfsm_FSMClock35", type=tfsm_TimedSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_TimedSystem34", type=tfsm_FSMClock, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_tfsm_TFSM_NamedElement = Generalization(general=NamedElement, specific=tfsm_TFSM)
gen_tfsm_State_NamedElement = Generalization(general=NamedElement, specific=tfsm_State)
gen_tfsm_Transition_NamedElement = Generalization(general=NamedElement, specific=tfsm_Transition)
gen_tfsm_Guard_NamedElement = Generalization(general=NamedElement, specific=tfsm_Guard)
gen_tfsm_TemporalGuard_Guard = Generalization(general=Guard, specific=tfsm_TemporalGuard)
gen_tfsm_EventGuard_Guard = Generalization(general=Guard, specific=tfsm_EventGuard)
gen_tfsm_FSMEvent_NamedElement = Generalization(general=NamedElement, specific=tfsm_FSMEvent)
gen_tfsm_FSMClock_NamedElement = Generalization(general=NamedElement, specific=tfsm_FSMClock)
gen_tfsm_TimedSystem_NamedElement = Generalization(general=NamedElement, specific=tfsm_TimedSystem)
gen_tfsm_EvaluateGuard_Guard = Generalization(general=Guard, specific=tfsm_EvaluateGuard)

# Domain Model
domain_model = DomainModel(
    name="tfsm",
    types={tfsm_TFSM, NamedElement, tfsm_State, tfsm_FSMEvent, tfsm_FSMClock, tfsm_Transition, tfsm_Guard, tfsm_NamedElement, tfsm_TemporalGuard, Guard, tfsm_EventGuard, tfsm_TimedSystem, tfsm_EvaluateGuard},
    associations={ownedStates0, initialState1, localEvents2, localClock4, ownedTransitions6, currentState8, owningFSM11, outgoingTransitions12, incomingTransitions13, source15, target17, ownedGuard19, generatedEvents21, globalEvents36, onClock24, triggeringEvent26, sollicitingTransitions28, tfsms31, globalClocks33},
    generalizations={gen_tfsm_TFSM_NamedElement, gen_tfsm_State_NamedElement, gen_tfsm_Transition_NamedElement, gen_tfsm_Guard_NamedElement, gen_tfsm_TemporalGuard_Guard, gen_tfsm_EventGuard_Guard, gen_tfsm_FSMEvent_NamedElement, gen_tfsm_FSMClock_NamedElement, gen_tfsm_TimedSystem_NamedElement, gen_tfsm_EvaluateGuard_Guard},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)