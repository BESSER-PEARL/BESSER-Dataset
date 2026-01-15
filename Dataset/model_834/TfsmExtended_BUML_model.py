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
tfsmextended_TFSM = Class(name="tfsmextended::TFSM")
NamedElement = Class(name="NamedElement")
tfsmextended_State = Class(name="tfsmextended::State")
tfsmextended_FSMEvent = Class(name="tfsmextended::FSMEvent")
tfsmextended_FSMClock = Class(name="tfsmextended::FSMClock")
tfsmextended_Transition = Class(name="tfsmextended::Transition")
tfsmextended_Guard = Class(name="tfsmextended::Guard", is_abstract=True)
tfsmextended_NamedElement = Class(name="tfsmextended::NamedElement")
tfsmextended_TemporalGuard = Class(name="tfsmextended::TemporalGuard")
Guard = Class(name="Guard")
tfsmextended_EventGuard = Class(name="tfsmextended::EventGuard")
tfsmextended_TimedSystem = Class(name="tfsmextended::TimedSystem")
tfsmextended_EvaluateGuard = Class(name="tfsmextended::EvaluateGuard")

# tfsmextended_TFSM class attributes and methods
tfsmextended_TFSM_m_init: Method = Method(name="init", parameters={})
tfsmextended_TFSM.methods={tfsmextended_TFSM_m_init}

# NamedElement class attributes and methods

# tfsmextended_State class attributes and methods
tfsmextended_State_m_onEnter: Method = Method(name="onEnter", parameters={})
tfsmextended_State_m_onLeave: Method = Method(name="onLeave", parameters={})
tfsmextended_State.methods={tfsmextended_State_m_onLeave, tfsmextended_State_m_onEnter}

# tfsmextended_FSMEvent class attributes and methods
tfsmextended_FSMEvent_isTriggered: Property = Property(name="isTriggered", type=BooleanType)
tfsmextended_FSMEvent_m_trigger: Method = Method(name="trigger", parameters={})
tfsmextended_FSMEvent_m_unTrigger: Method = Method(name="unTrigger", parameters={})
tfsmextended_FSMEvent.attributes={tfsmextended_FSMEvent_isTriggered}
tfsmextended_FSMEvent.methods={tfsmextended_FSMEvent_m_trigger, tfsmextended_FSMEvent_m_unTrigger}

# tfsmextended_FSMClock class attributes and methods
tfsmextended_FSMClock_numberOfTicks: Property = Property(name="numberOfTicks", type=StringType)
tfsmextended_FSMClock_m_ticks: Method = Method(name="ticks", parameters={}, type=StringType)
tfsmextended_FSMClock.attributes={tfsmextended_FSMClock_numberOfTicks}
tfsmextended_FSMClock.methods={tfsmextended_FSMClock_m_ticks}

# tfsmextended_Transition class attributes and methods
tfsmextended_Transition_action: Property = Property(name="action", type=StringType)
tfsmextended_Transition_m_fire: Method = Method(name="fire", parameters={})
tfsmextended_Transition.attributes={tfsmextended_Transition_action}
tfsmextended_Transition.methods={tfsmextended_Transition_m_fire}

# tfsmextended_Guard class attributes and methods

# tfsmextended_NamedElement class attributes and methods
tfsmextended_NamedElement_name: Property = Property(name="name", type=StringType)
tfsmextended_NamedElement.attributes={tfsmextended_NamedElement_name}

# tfsmextended_TemporalGuard class attributes and methods
tfsmextended_TemporalGuard_afterDuration: Property = Property(name="afterDuration", type=IntegerType)
tfsmextended_TemporalGuard.attributes={tfsmextended_TemporalGuard_afterDuration}

# Guard class attributes and methods

# tfsmextended_EventGuard class attributes and methods

# tfsmextended_TimedSystem class attributes and methods

# tfsmextended_EvaluateGuard class attributes and methods
tfsmextended_EvaluateGuard_condition: Property = Property(name="condition", type=StringType)
tfsmextended_EvaluateGuard.attributes={tfsmextended_EvaluateGuard_condition}

# Relationships
ownedStates0: BinaryAssociation = BinaryAssociation(
    name="ownedStates0",
    ends={
        Property(name="State", type=tfsmextended_TFSM, multiplicity=Multiplicity(1, 1)),
        Property(name="owningFSM", type=tfsmextended_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialState1: BinaryAssociation = BinaryAssociation(
    name="initialState1",
    ends={
        Property(name="tfsmextended_State", type=tfsmextended_TFSM, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsmextended_TFSM", type=tfsmextended_State, multiplicity=Multiplicity(1, 1))
    }
)
localEvents2: BinaryAssociation = BinaryAssociation(
    name="localEvents2",
    ends={
        Property(name="tfsmextended_FSMEvent", type=tfsmextended_TFSM, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsmextended_TFSM3", type=tfsmextended_FSMEvent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
localClock4: BinaryAssociation = BinaryAssociation(
    name="localClock4",
    ends={
        Property(name="tfsmextended_FSMClock", type=tfsmextended_TFSM, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsmextended_TFSM5", type=tfsmextended_FSMClock, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ownedTransitions6: BinaryAssociation = BinaryAssociation(
    name="ownedTransitions6",
    ends={
        Property(name="tfsmextended_Transition", type=tfsmextended_TFSM, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsmextended_TFSM7", type=tfsmextended_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
currentState8: BinaryAssociation = BinaryAssociation(
    name="currentState8",
    ends={
        Property(name="tfsmextended_State10", type=tfsmextended_TFSM, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsmextended_TFSM9", type=tfsmextended_State, multiplicity=Multiplicity(0, 1))
    }
)
owningFSM11: BinaryAssociation = BinaryAssociation(
    name="owningFSM11",
    ends={
        Property(name="TFSM", type=tfsmextended_State, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedStates", type=tfsmextended_TFSM, multiplicity=Multiplicity(1, 1))
    }
)
outgoingTransitions12: BinaryAssociation = BinaryAssociation(
    name="outgoingTransitions12",
    ends={
        Property(name="Transition", type=tfsmextended_State, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=tfsmextended_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
incomingTransitions13: BinaryAssociation = BinaryAssociation(
    name="incomingTransitions13",
    ends={
        Property(name="Transition14", type=tfsmextended_State, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=tfsmextended_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
source15: BinaryAssociation = BinaryAssociation(
    name="source15",
    ends={
        Property(name="State16", type=tfsmextended_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingTransitions", type=tfsmextended_State, multiplicity=Multiplicity(1, 1))
    }
)
target17: BinaryAssociation = BinaryAssociation(
    name="target17",
    ends={
        Property(name="State18", type=tfsmextended_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingTransitions", type=tfsmextended_State, multiplicity=Multiplicity(1, 1))
    }
)
ownedGuard19: BinaryAssociation = BinaryAssociation(
    name="ownedGuard19",
    ends={
        Property(name="tfsmextended_Guard", type=tfsmextended_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsmextended_Transition20", type=tfsmextended_Guard, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
generatedEvents21: BinaryAssociation = BinaryAssociation(
    name="generatedEvents21",
    ends={
        Property(name="tfsmextended_FSMEvent23", type=tfsmextended_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsmextended_Transition22", type=tfsmextended_FSMEvent, multiplicity=Multiplicity(0, 9999))
    }
)
onClock24: BinaryAssociation = BinaryAssociation(
    name="onClock24",
    ends={
        Property(name="tfsmextended_FSMClock25", type=tfsmextended_TemporalGuard, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsmextended_TemporalGuard", type=tfsmextended_FSMClock, multiplicity=Multiplicity(1, 1))
    }
)
triggeringEvent26: BinaryAssociation = BinaryAssociation(
    name="triggeringEvent26",
    ends={
        Property(name="tfsmextended_FSMEvent27", type=tfsmextended_EventGuard, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsmextended_EventGuard", type=tfsmextended_FSMEvent, multiplicity=Multiplicity(1, 1))
    }
)
sollicitingTransitions28: BinaryAssociation = BinaryAssociation(
    name="sollicitingTransitions28",
    ends={
        Property(name="tfsmextended_Transition30", type=tfsmextended_FSMEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsmextended_FSMEvent29", type=tfsmextended_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
tfsms31: BinaryAssociation = BinaryAssociation(
    name="tfsms31",
    ends={
        Property(name="tfsmextended_TFSM32", type=tfsmextended_TimedSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsmextended_TimedSystem", type=tfsmextended_TFSM, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
globalClocks33: BinaryAssociation = BinaryAssociation(
    name="globalClocks33",
    ends={
        Property(name="tfsmextended_FSMClock35", type=tfsmextended_TimedSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsmextended_TimedSystem34", type=tfsmextended_FSMClock, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
globalEvents36: BinaryAssociation = BinaryAssociation(
    name="globalEvents36",
    ends={
        Property(name="tfsmextended_FSMEvent38", type=tfsmextended_TimedSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsmextended_TimedSystem37", type=tfsmextended_FSMEvent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_tfsmextended_TFSM_NamedElement = Generalization(general=NamedElement, specific=tfsmextended_TFSM)
gen_tfsmextended_State_NamedElement = Generalization(general=NamedElement, specific=tfsmextended_State)
gen_tfsmextended_Transition_NamedElement = Generalization(general=NamedElement, specific=tfsmextended_Transition)
gen_tfsmextended_Guard_NamedElement = Generalization(general=NamedElement, specific=tfsmextended_Guard)
gen_tfsmextended_TemporalGuard_Guard = Generalization(general=Guard, specific=tfsmextended_TemporalGuard)
gen_tfsmextended_EventGuard_Guard = Generalization(general=Guard, specific=tfsmextended_EventGuard)
gen_tfsmextended_FSMEvent_NamedElement = Generalization(general=NamedElement, specific=tfsmextended_FSMEvent)
gen_tfsmextended_FSMClock_NamedElement = Generalization(general=NamedElement, specific=tfsmextended_FSMClock)
gen_tfsmextended_TimedSystem_NamedElement = Generalization(general=NamedElement, specific=tfsmextended_TimedSystem)
gen_tfsmextended_EvaluateGuard_Guard = Generalization(general=Guard, specific=tfsmextended_EvaluateGuard)

# Domain Model
domain_model = DomainModel(
    name="tfsmextended",
    types={tfsmextended_TFSM, NamedElement, tfsmextended_State, tfsmextended_FSMEvent, tfsmextended_FSMClock, tfsmextended_Transition, tfsmextended_Guard, tfsmextended_NamedElement, tfsmextended_TemporalGuard, Guard, tfsmextended_EventGuard, tfsmextended_TimedSystem, tfsmextended_EvaluateGuard},
    associations={ownedStates0, initialState1, localEvents2, localClock4, ownedTransitions6, currentState8, owningFSM11, outgoingTransitions12, incomingTransitions13, source15, target17, ownedGuard19, generatedEvents21, onClock24, triggeringEvent26, sollicitingTransitions28, tfsms31, globalClocks33, globalEvents36},
    generalizations={gen_tfsmextended_TFSM_NamedElement, gen_tfsmextended_State_NamedElement, gen_tfsmextended_Transition_NamedElement, gen_tfsmextended_Guard_NamedElement, gen_tfsmextended_TemporalGuard_Guard, gen_tfsmextended_EventGuard_Guard, gen_tfsmextended_FSMEvent_NamedElement, gen_tfsmextended_FSMClock_NamedElement, gen_tfsmextended_TimedSystem_NamedElement, gen_tfsmextended_EvaluateGuard_Guard},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)