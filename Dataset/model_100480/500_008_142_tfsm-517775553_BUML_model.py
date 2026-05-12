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
tfsm_plaink3_TFSM = Class(name="tfsm_plaink3_TFSM")
NamedElement = Class(name="NamedElement")
tfsm_plaink3_State = Class(name="tfsm_plaink3_State")
tfsm_plaink3_FSMEvent = Class(name="tfsm_plaink3_FSMEvent")
tfsm_plaink3_FSMClock = Class(name="tfsm_plaink3_FSMClock")
tfsm_plaink3_Transition = Class(name="tfsm_plaink3_Transition")
tfsm_plaink3_Guard = Class(name="tfsm_plaink3_Guard", is_abstract=True)
tfsm_plaink3_TemporalGuard = Class(name="tfsm_plaink3_TemporalGuard")
Guard = Class(name="Guard")
tfsm_plaink3_EventGuard = Class(name="tfsm_plaink3_EventGuard")
tfsm_plaink3_TimedSystem = Class(name="tfsm_plaink3_TimedSystem")
tfsm_plaink3_NamedElement = Class(name="tfsm_plaink3_NamedElement", is_abstract=True)
tfsm_plaink3_EvaluateGuard = Class(name="tfsm_plaink3_EvaluateGuard")

# tfsm_plaink3_TFSM class attributes and methods

# NamedElement class attributes and methods

# tfsm_plaink3_State class attributes and methods

# tfsm_plaink3_FSMEvent class attributes and methods
tfsm_plaink3_FSMEvent_isTriggered: Property = Property(name="isTriggered", type=BooleanType)
tfsm_plaink3_FSMEvent.attributes={tfsm_plaink3_FSMEvent_isTriggered}

# tfsm_plaink3_FSMClock class attributes and methods
tfsm_plaink3_FSMClock_numberOfTicks: Property = Property(name="numberOfTicks", type=StringType)
tfsm_plaink3_FSMClock.attributes={tfsm_plaink3_FSMClock_numberOfTicks}

# tfsm_plaink3_Transition class attributes and methods
tfsm_plaink3_Transition_action: Property = Property(name="action", type=StringType)
tfsm_plaink3_Transition.attributes={tfsm_plaink3_Transition_action}

# tfsm_plaink3_Guard class attributes and methods

# tfsm_plaink3_TemporalGuard class attributes and methods
tfsm_plaink3_TemporalGuard_afterDuration: Property = Property(name="afterDuration", type=IntegerType)
tfsm_plaink3_TemporalGuard.attributes={tfsm_plaink3_TemporalGuard_afterDuration}

# Guard class attributes and methods

# tfsm_plaink3_EventGuard class attributes and methods

# tfsm_plaink3_TimedSystem class attributes and methods

# tfsm_plaink3_NamedElement class attributes and methods
tfsm_plaink3_NamedElement_name: Property = Property(name="name", type=StringType)
tfsm_plaink3_NamedElement.attributes={tfsm_plaink3_NamedElement_name}

# tfsm_plaink3_EvaluateGuard class attributes and methods
tfsm_plaink3_EvaluateGuard_condition: Property = Property(name="condition", type=StringType)
tfsm_plaink3_EvaluateGuard.attributes={tfsm_plaink3_EvaluateGuard_condition}

# Relationships
ownedStates0: BinaryAssociation = BinaryAssociation(
    name="ownedStates0",
    ends={
        Property(name="State", type=tfsm_plaink3_TFSM, multiplicity=Multiplicity(1, 1)),
        Property(name="owningFSM", type=tfsm_plaink3_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialState1: BinaryAssociation = BinaryAssociation(
    name="initialState1",
    ends={
        Property(name="tfsm_plaink3_State", type=tfsm_plaink3_TFSM, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_plaink3_TFSM", type=tfsm_plaink3_State, multiplicity=Multiplicity(1, 1))
    }
)
localEvents2: BinaryAssociation = BinaryAssociation(
    name="localEvents2",
    ends={
        Property(name="tfsm_plaink3_FSMEvent", type=tfsm_plaink3_TFSM, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_plaink3_TFSM3", type=tfsm_plaink3_FSMEvent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
localClock4: BinaryAssociation = BinaryAssociation(
    name="localClock4",
    ends={
        Property(name="tfsm_plaink3_FSMClock", type=tfsm_plaink3_TFSM, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_plaink3_TFSM5", type=tfsm_plaink3_FSMClock, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ownedTransitions6: BinaryAssociation = BinaryAssociation(
    name="ownedTransitions6",
    ends={
        Property(name="tfsm_plaink3_Transition", type=tfsm_plaink3_TFSM, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_plaink3_TFSM7", type=tfsm_plaink3_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
currentState8: BinaryAssociation = BinaryAssociation(
    name="currentState8",
    ends={
        Property(name="tfsm_plaink3_State10", type=tfsm_plaink3_TFSM, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_plaink3_TFSM9", type=tfsm_plaink3_State, multiplicity=Multiplicity(0, 1))
    }
)
owningFSM11: BinaryAssociation = BinaryAssociation(
    name="owningFSM11",
    ends={
        Property(name="TFSM", type=tfsm_plaink3_State, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedStates", type=tfsm_plaink3_TFSM, multiplicity=Multiplicity(1, 1))
    }
)
outgoingTransitions12: BinaryAssociation = BinaryAssociation(
    name="outgoingTransitions12",
    ends={
        Property(name="Transition", type=tfsm_plaink3_State, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=tfsm_plaink3_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
incomingTransitions13: BinaryAssociation = BinaryAssociation(
    name="incomingTransitions13",
    ends={
        Property(name="Transition14", type=tfsm_plaink3_State, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=tfsm_plaink3_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
source15: BinaryAssociation = BinaryAssociation(
    name="source15",
    ends={
        Property(name="State16", type=tfsm_plaink3_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingTransitions", type=tfsm_plaink3_State, multiplicity=Multiplicity(1, 1))
    }
)
target17: BinaryAssociation = BinaryAssociation(
    name="target17",
    ends={
        Property(name="State18", type=tfsm_plaink3_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingTransitions", type=tfsm_plaink3_State, multiplicity=Multiplicity(1, 1))
    }
)
ownedGuard19: BinaryAssociation = BinaryAssociation(
    name="ownedGuard19",
    ends={
        Property(name="tfsm_plaink3_Guard", type=tfsm_plaink3_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_plaink3_Transition20", type=tfsm_plaink3_Guard, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
generatedEvents21: BinaryAssociation = BinaryAssociation(
    name="generatedEvents21",
    ends={
        Property(name="tfsm_plaink3_FSMEvent23", type=tfsm_plaink3_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_plaink3_Transition22", type=tfsm_plaink3_FSMEvent, multiplicity=Multiplicity(0, 9999))
    }
)
onClock24: BinaryAssociation = BinaryAssociation(
    name="onClock24",
    ends={
        Property(name="tfsm_plaink3_FSMClock25", type=tfsm_plaink3_TemporalGuard, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_plaink3_TemporalGuard", type=tfsm_plaink3_FSMClock, multiplicity=Multiplicity(1, 1))
    }
)
triggeringEvent26: BinaryAssociation = BinaryAssociation(
    name="triggeringEvent26",
    ends={
        Property(name="tfsm_plaink3_FSMEvent27", type=tfsm_plaink3_EventGuard, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_plaink3_EventGuard", type=tfsm_plaink3_FSMEvent, multiplicity=Multiplicity(1, 1))
    }
)
sollicitingTransitions28: BinaryAssociation = BinaryAssociation(
    name="sollicitingTransitions28",
    ends={
        Property(name="tfsm_plaink3_Transition30", type=tfsm_plaink3_FSMEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_plaink3_FSMEvent29", type=tfsm_plaink3_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
globalClocks33: BinaryAssociation = BinaryAssociation(
    name="globalClocks33",
    ends={
        Property(name="tfsm_plaink3_FSMClock35", type=tfsm_plaink3_TimedSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_plaink3_TimedSystem34", type=tfsm_plaink3_FSMClock, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
globalEvents36: BinaryAssociation = BinaryAssociation(
    name="globalEvents36",
    ends={
        Property(name="tfsm_plaink3_FSMEvent38", type=tfsm_plaink3_TimedSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_plaink3_TimedSystem37", type=tfsm_plaink3_FSMEvent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tfsms31: BinaryAssociation = BinaryAssociation(
    name="tfsms31",
    ends={
        Property(name="tfsm_plaink3_TFSM32", type=tfsm_plaink3_TimedSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_plaink3_TimedSystem", type=tfsm_plaink3_TFSM, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_tfsm_plaink3_TFSM_NamedElement = Generalization(general=NamedElement, specific=tfsm_plaink3_TFSM)
gen_tfsm_plaink3_Transition_NamedElement = Generalization(general=NamedElement, specific=tfsm_plaink3_Transition)
gen_tfsm_plaink3_State_NamedElement = Generalization(general=NamedElement, specific=tfsm_plaink3_State)
gen_tfsm_plaink3_Guard_NamedElement = Generalization(general=NamedElement, specific=tfsm_plaink3_Guard)
gen_tfsm_plaink3_TemporalGuard_Guard = Generalization(general=Guard, specific=tfsm_plaink3_TemporalGuard)
gen_tfsm_plaink3_EventGuard_Guard = Generalization(general=Guard, specific=tfsm_plaink3_EventGuard)
gen_tfsm_plaink3_FSMEvent_NamedElement = Generalization(general=NamedElement, specific=tfsm_plaink3_FSMEvent)
gen_tfsm_plaink3_FSMClock_NamedElement = Generalization(general=NamedElement, specific=tfsm_plaink3_FSMClock)
gen_tfsm_plaink3_TimedSystem_NamedElement = Generalization(general=NamedElement, specific=tfsm_plaink3_TimedSystem)
gen_tfsm_plaink3_EvaluateGuard_Guard = Generalization(general=Guard, specific=tfsm_plaink3_EvaluateGuard)

# Domain Model
domain_model = DomainModel(
    name="tfsm_plaink3",
    types={tfsm_plaink3_TFSM, NamedElement, tfsm_plaink3_State, tfsm_plaink3_FSMEvent, tfsm_plaink3_FSMClock, tfsm_plaink3_Transition, tfsm_plaink3_Guard, tfsm_plaink3_TemporalGuard, Guard, tfsm_plaink3_EventGuard, tfsm_plaink3_TimedSystem, tfsm_plaink3_NamedElement, tfsm_plaink3_EvaluateGuard},
    associations={ownedStates0, initialState1, localEvents2, localClock4, ownedTransitions6, currentState8, owningFSM11, outgoingTransitions12, incomingTransitions13, source15, target17, ownedGuard19, generatedEvents21, onClock24, triggeringEvent26, sollicitingTransitions28, globalClocks33, globalEvents36, tfsms31},
    generalizations={gen_tfsm_plaink3_TFSM_NamedElement, gen_tfsm_plaink3_Transition_NamedElement, gen_tfsm_plaink3_State_NamedElement, gen_tfsm_plaink3_Guard_NamedElement, gen_tfsm_plaink3_TemporalGuard_Guard, gen_tfsm_plaink3_EventGuard_Guard, gen_tfsm_plaink3_FSMEvent_NamedElement, gen_tfsm_plaink3_FSMClock_NamedElement, gen_tfsm_plaink3_TimedSystem_NamedElement, gen_tfsm_plaink3_EvaluateGuard_Guard},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)