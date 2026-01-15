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
tfsmextended_FSMEvent = Class(name="tfsmextended::FSMEvent")
tfsmextended_FSMClock = Class(name="tfsmextended::FSMClock")
tfsmextended_Transition = Class(name="tfsmextended::Transition")
tfsmextended_TFSM = Class(name="tfsmextended::TFSM")
NamedElement = Class(name="NamedElement")
tfsmextended_State = Class(name="tfsmextended::State")
tfsmextended_Guard = Class(name="tfsmextended::Guard", is_abstract=True)
tfsmextended_NamedElement = Class(name="tfsmextended::NamedElement")
tfsmextended_TemporalGuard = Class(name="tfsmextended::TemporalGuard")
Guard = Class(name="Guard")
tfsmextended_EvaluateGuard = Class(name="tfsmextended::EvaluateGuard")
tfsmextended_EventGuard = Class(name="tfsmextended::EventGuard")
tfsmextended_TimedSystem = Class(name="tfsmextended::TimedSystem")

# tfsmextended_FSMEvent class attributes and methods
tfsmextended_FSMEvent_isTriggered: Property = Property(name="isTriggered", type=StringType)
tfsmextended_FSMEvent_m_trigger: Method = Method(name="trigger", parameters={})
tfsmextended_FSMEvent_m_unTrigger: Method = Method(name="unTrigger", parameters={})
tfsmextended_FSMEvent.attributes={tfsmextended_FSMEvent_isTriggered}
tfsmextended_FSMEvent.methods={tfsmextended_FSMEvent_m_unTrigger, tfsmextended_FSMEvent_m_trigger}

# tfsmextended_FSMClock class attributes and methods
tfsmextended_FSMClock_numberOfTicks: Property = Property(name="numberOfTicks", type=StringType)
tfsmextended_FSMClock_m_ticks: Method = Method(name="ticks", parameters={})
tfsmextended_FSMClock.attributes={tfsmextended_FSMClock_numberOfTicks}
tfsmextended_FSMClock.methods={tfsmextended_FSMClock_m_ticks}

# tfsmextended_Transition class attributes and methods
tfsmextended_Transition_action: Property = Property(name="action", type=StringType)
tfsmextended_Transition_m_fire: Method = Method(name="fire", parameters={})
tfsmextended_Transition.attributes={tfsmextended_Transition_action}
tfsmextended_Transition.methods={tfsmextended_Transition_m_fire}

# tfsmextended_TFSM class attributes and methods
tfsmextended_TFSM_m_init: Method = Method(name="init", parameters={})
tfsmextended_TFSM.methods={tfsmextended_TFSM_m_init}

# NamedElement class attributes and methods

# tfsmextended_State class attributes and methods
tfsmextended_State_m_onEnter: Method = Method(name="onEnter", parameters={})
tfsmextended_State_m_onLeave: Method = Method(name="onLeave", parameters={})
tfsmextended_State.methods={tfsmextended_State_m_onEnter, tfsmextended_State_m_onLeave}

# tfsmextended_Guard class attributes and methods

# tfsmextended_NamedElement class attributes and methods
tfsmextended_NamedElement_name: Property = Property(name="name", type=StringType)
tfsmextended_NamedElement.attributes={tfsmextended_NamedElement_name}

# tfsmextended_TemporalGuard class attributes and methods
tfsmextended_TemporalGuard_afterDuration: Property = Property(name="afterDuration", type=IntegerType)
tfsmextended_TemporalGuard.attributes={tfsmextended_TemporalGuard_afterDuration}

# Guard class attributes and methods

# tfsmextended_EvaluateGuard class attributes and methods
tfsmextended_EvaluateGuard_condition: Property = Property(name="condition", type=StringType)
tfsmextended_EvaluateGuard.attributes={tfsmextended_EvaluateGuard_condition}

# tfsmextended_EventGuard class attributes and methods

# tfsmextended_TimedSystem class attributes and methods

# Relationships
ownedStates0: BinaryAssociation = BinaryAssociation(
    name="ownedStates0",
    ends={
        Property(name="", type=tfsmextended_State, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="1", type=tfsmextended_TFSM, multiplicity=Multiplicity(1, 1))
    }
)
initialState2: BinaryAssociation = BinaryAssociation(
    name="initialState2",
    ends={
        Property(name="tfsmextended_State", type=tfsmextended_TFSM, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsmextended_TFSM", type=tfsmextended_State, multiplicity=Multiplicity(1, 1))
    }
)
localEvents3: BinaryAssociation = BinaryAssociation(
    name="localEvents3",
    ends={
        Property(name="tfsmextended_FSMEvent", type=tfsmextended_TFSM, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsmextended_TFSM4", type=tfsmextended_FSMEvent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
localClock5: BinaryAssociation = BinaryAssociation(
    name="localClock5",
    ends={
        Property(name="tfsmextended_FSMClock", type=tfsmextended_TFSM, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsmextended_TFSM6", type=tfsmextended_FSMClock, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ownedTransitions7: BinaryAssociation = BinaryAssociation(
    name="ownedTransitions7",
    ends={
        Property(name="tfsmextended_Transition", type=tfsmextended_TFSM, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsmextended_TFSM8", type=tfsmextended_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
currentState9: BinaryAssociation = BinaryAssociation(
    name="currentState9",
    ends={
        Property(name="tfsmextended_State11", type=tfsmextended_TFSM, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsmextended_TFSM10", type=tfsmextended_State, multiplicity=Multiplicity(0, 1))
    }
)
ownedGuard27: BinaryAssociation = BinaryAssociation(
    name="ownedGuard27",
    ends={
        Property(name="tfsmextended_Guard", type=tfsmextended_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsmextended_Transition28", type=tfsmextended_Guard, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
generatedEvents29: BinaryAssociation = BinaryAssociation(
    name="generatedEvents29",
    ends={
        Property(name="tfsmextended_FSMEvent31", type=tfsmextended_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsmextended_Transition30", type=tfsmextended_FSMEvent, multiplicity=Multiplicity(0, 9999))
    }
)
owningFSM12: BinaryAssociation = BinaryAssociation(
    name="owningFSM12",
    ends={
        Property(name="14", type=tfsmextended_State, multiplicity=Multiplicity(1, 1)),
        Property(name="13", type=tfsmextended_TFSM, multiplicity=Multiplicity(1, 1))
    }
)
outgoingTransitions15: BinaryAssociation = BinaryAssociation(
    name="outgoingTransitions15",
    ends={
        Property(name="17", type=tfsmextended_State, multiplicity=Multiplicity(1, 1)),
        Property(name="16", type=tfsmextended_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
incomingTransitions18: BinaryAssociation = BinaryAssociation(
    name="incomingTransitions18",
    ends={
        Property(name="20", type=tfsmextended_State, multiplicity=Multiplicity(1, 1)),
        Property(name="19", type=tfsmextended_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
source21: BinaryAssociation = BinaryAssociation(
    name="source21",
    ends={
        Property(name="23", type=tfsmextended_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="22", type=tfsmextended_State, multiplicity=Multiplicity(1, 1))
    }
)
target24: BinaryAssociation = BinaryAssociation(
    name="target24",
    ends={
        Property(name="26", type=tfsmextended_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="25", type=tfsmextended_State, multiplicity=Multiplicity(1, 1))
    }
)
tfsms39: BinaryAssociation = BinaryAssociation(
    name="tfsms39",
    ends={
        Property(name="tfsmextended_TFSM40", type=tfsmextended_TimedSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsmextended_TimedSystem", type=tfsmextended_TFSM, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
globalClocks41: BinaryAssociation = BinaryAssociation(
    name="globalClocks41",
    ends={
        Property(name="tfsmextended_FSMClock43", type=tfsmextended_TimedSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsmextended_TimedSystem42", type=tfsmextended_FSMClock, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
globalEvents44: BinaryAssociation = BinaryAssociation(
    name="globalEvents44",
    ends={
        Property(name="tfsmextended_FSMEvent46", type=tfsmextended_TimedSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsmextended_TimedSystem45", type=tfsmextended_FSMEvent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
onClock32: BinaryAssociation = BinaryAssociation(
    name="onClock32",
    ends={
        Property(name="tfsmextended_FSMClock33", type=tfsmextended_TemporalGuard, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsmextended_TemporalGuard", type=tfsmextended_FSMClock, multiplicity=Multiplicity(1, 1))
    }
)
triggeringEvent34: BinaryAssociation = BinaryAssociation(
    name="triggeringEvent34",
    ends={
        Property(name="tfsmextended_FSMEvent35", type=tfsmextended_EventGuard, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsmextended_EventGuard", type=tfsmextended_FSMEvent, multiplicity=Multiplicity(1, 1))
    }
)
sollicitingTransitions36: BinaryAssociation = BinaryAssociation(
    name="sollicitingTransitions36",
    ends={
        Property(name="tfsmextended_Transition38", type=tfsmextended_FSMEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsmextended_FSMEvent37", type=tfsmextended_Transition, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_tfsmextended_TFSM_NamedElement = Generalization(general=NamedElement, specific=tfsmextended_TFSM)
gen_tfsmextended_Guard_NamedElement = Generalization(general=NamedElement, specific=tfsmextended_Guard)
gen_tfsmextended_TemporalGuard_Guard = Generalization(general=Guard, specific=tfsmextended_TemporalGuard)
gen_tfsmextended_State_NamedElement = Generalization(general=NamedElement, specific=tfsmextended_State)
gen_tfsmextended_Transition_NamedElement = Generalization(general=NamedElement, specific=tfsmextended_Transition)
gen_tfsmextended_EvaluateGuard_Guard = Generalization(general=Guard, specific=tfsmextended_EvaluateGuard)
gen_tfsmextended_EventGuard_Guard = Generalization(general=Guard, specific=tfsmextended_EventGuard)
gen_tfsmextended_FSMEvent_NamedElement = Generalization(general=NamedElement, specific=tfsmextended_FSMEvent)
gen_tfsmextended_FSMClock_NamedElement = Generalization(general=NamedElement, specific=tfsmextended_FSMClock)
gen_tfsmextended_TimedSystem_NamedElement = Generalization(general=NamedElement, specific=tfsmextended_TimedSystem)

# Domain Model
domain_model = DomainModel(
    name="tfsmextended",
    types={tfsmextended_FSMEvent, tfsmextended_FSMClock, tfsmextended_Transition, tfsmextended_TFSM, NamedElement, tfsmextended_State, tfsmextended_Guard, tfsmextended_NamedElement, tfsmextended_TemporalGuard, Guard, tfsmextended_EvaluateGuard, tfsmextended_EventGuard, tfsmextended_TimedSystem},
    associations={ownedStates0, initialState2, localEvents3, localClock5, ownedTransitions7, currentState9, ownedGuard27, generatedEvents29, owningFSM12, outgoingTransitions15, incomingTransitions18, source21, target24, tfsms39, globalClocks41, globalEvents44, onClock32, triggeringEvent34, sollicitingTransitions36},
    generalizations={gen_tfsmextended_TFSM_NamedElement, gen_tfsmextended_Guard_NamedElement, gen_tfsmextended_TemporalGuard_Guard, gen_tfsmextended_State_NamedElement, gen_tfsmextended_Transition_NamedElement, gen_tfsmextended_EvaluateGuard_Guard, gen_tfsmextended_EventGuard_Guard, gen_tfsmextended_FSMEvent_NamedElement, gen_tfsmextended_FSMClock_NamedElement, gen_tfsmextended_TimedSystem_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)