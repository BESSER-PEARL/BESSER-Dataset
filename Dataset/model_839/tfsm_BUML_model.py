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
tfsm_plaink3_FSMClock = Class(name="tfsm::plaink3::FSMClock")
tfsm_plaink3_Transition = Class(name="tfsm::plaink3::Transition")
tfsm_plaink3_TFSM = Class(name="tfsm::plaink3::TFSM")
NamedElement = Class(name="NamedElement")
tfsm_plaink3_State = Class(name="tfsm::plaink3::State")
tfsm_plaink3_FSMEvent = Class(name="tfsm::plaink3::FSMEvent")
tfsm_plaink3_TimedSystem = Class(name="tfsm::plaink3::TimedSystem")
tfsm_plaink3_EvaluateGuard = Class(name="tfsm::plaink3::EvaluateGuard")
tfsm_plaink3_Guard = Class(name="tfsm::plaink3::Guard", is_abstract=True)
tfsm_plaink3_NamedElement = Class(name="tfsm::plaink3::NamedElement", is_abstract=True)
tfsm_plaink3_TemporalGuard = Class(name="tfsm::plaink3::TemporalGuard")
Guard = Class(name="Guard")
tfsm_plaink3_EventGuard = Class(name="tfsm::plaink3::EventGuard")

# tfsm_plaink3_FSMClock class attributes and methods

# tfsm_plaink3_Transition class attributes and methods
tfsm_plaink3_Transition_action: Property = Property(name="action", type=StringType)
tfsm_plaink3_Transition.attributes={tfsm_plaink3_Transition_action}

# tfsm_plaink3_TFSM class attributes and methods

# NamedElement class attributes and methods

# tfsm_plaink3_State class attributes and methods

# tfsm_plaink3_FSMEvent class attributes and methods

# tfsm_plaink3_TimedSystem class attributes and methods

# tfsm_plaink3_EvaluateGuard class attributes and methods
tfsm_plaink3_EvaluateGuard_condition: Property = Property(name="condition", type=StringType)
tfsm_plaink3_EvaluateGuard.attributes={tfsm_plaink3_EvaluateGuard_condition}

# tfsm_plaink3_Guard class attributes and methods

# tfsm_plaink3_NamedElement class attributes and methods
tfsm_plaink3_NamedElement_name: Property = Property(name="name", type=StringType)
tfsm_plaink3_NamedElement.attributes={tfsm_plaink3_NamedElement_name}

# tfsm_plaink3_TemporalGuard class attributes and methods
tfsm_plaink3_TemporalGuard_afterDuration: Property = Property(name="afterDuration", type=IntegerType)
tfsm_plaink3_TemporalGuard.attributes={tfsm_plaink3_TemporalGuard_afterDuration}

# Guard class attributes and methods

# tfsm_plaink3_EventGuard class attributes and methods

# Relationships
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
owningFSM8: BinaryAssociation = BinaryAssociation(
    name="owningFSM8",
    ends={
        Property(name="TFSM", type=tfsm_plaink3_State, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedStates", type=tfsm_plaink3_TFSM, multiplicity=Multiplicity(1, 1))
    }
)
outgoingTransitions9: BinaryAssociation = BinaryAssociation(
    name="outgoingTransitions9",
    ends={
        Property(name="Transition", type=tfsm_plaink3_State, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=tfsm_plaink3_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
incomingTransitions10: BinaryAssociation = BinaryAssociation(
    name="incomingTransitions10",
    ends={
        Property(name="Transition11", type=tfsm_plaink3_State, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=tfsm_plaink3_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
source12: BinaryAssociation = BinaryAssociation(
    name="source12",
    ends={
        Property(name="State13", type=tfsm_plaink3_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingTransitions", type=tfsm_plaink3_State, multiplicity=Multiplicity(1, 1))
    }
)
target14: BinaryAssociation = BinaryAssociation(
    name="target14",
    ends={
        Property(name="State15", type=tfsm_plaink3_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingTransitions", type=tfsm_plaink3_State, multiplicity=Multiplicity(1, 1))
    }
)
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
tfsms28: BinaryAssociation = BinaryAssociation(
    name="tfsms28",
    ends={
        Property(name="tfsm_plaink3_TFSM29", type=tfsm_plaink3_TimedSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_plaink3_TimedSystem", type=tfsm_plaink3_TFSM, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
globalClocks30: BinaryAssociation = BinaryAssociation(
    name="globalClocks30",
    ends={
        Property(name="tfsm_plaink3_FSMClock32", type=tfsm_plaink3_TimedSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_plaink3_TimedSystem31", type=tfsm_plaink3_FSMClock, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
globalEvents33: BinaryAssociation = BinaryAssociation(
    name="globalEvents33",
    ends={
        Property(name="tfsm_plaink3_FSMEvent35", type=tfsm_plaink3_TimedSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_plaink3_TimedSystem34", type=tfsm_plaink3_FSMEvent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedGuard16: BinaryAssociation = BinaryAssociation(
    name="ownedGuard16",
    ends={
        Property(name="tfsm_plaink3_Guard", type=tfsm_plaink3_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_plaink3_Transition17", type=tfsm_plaink3_Guard, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
generatedEvents18: BinaryAssociation = BinaryAssociation(
    name="generatedEvents18",
    ends={
        Property(name="tfsm_plaink3_FSMEvent20", type=tfsm_plaink3_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_plaink3_Transition19", type=tfsm_plaink3_FSMEvent, multiplicity=Multiplicity(0, 9999))
    }
)
onClock21: BinaryAssociation = BinaryAssociation(
    name="onClock21",
    ends={
        Property(name="tfsm_plaink3_FSMClock22", type=tfsm_plaink3_TemporalGuard, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_plaink3_TemporalGuard", type=tfsm_plaink3_FSMClock, multiplicity=Multiplicity(1, 1))
    }
)
triggeringEvent23: BinaryAssociation = BinaryAssociation(
    name="triggeringEvent23",
    ends={
        Property(name="tfsm_plaink3_FSMEvent24", type=tfsm_plaink3_EventGuard, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_plaink3_EventGuard", type=tfsm_plaink3_FSMEvent, multiplicity=Multiplicity(1, 1))
    }
)
sollicitingTransitions25: BinaryAssociation = BinaryAssociation(
    name="sollicitingTransitions25",
    ends={
        Property(name="tfsm_plaink3_Transition27", type=tfsm_plaink3_FSMEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_plaink3_FSMEvent26", type=tfsm_plaink3_Transition, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_tfsm_plaink3_State_NamedElement = Generalization(general=NamedElement, specific=tfsm_plaink3_State)
gen_tfsm_plaink3_Transition_NamedElement = Generalization(general=NamedElement, specific=tfsm_plaink3_Transition)
gen_tfsm_plaink3_TFSM_NamedElement = Generalization(general=NamedElement, specific=tfsm_plaink3_TFSM)
gen_tfsm_plaink3_FSMClock_NamedElement = Generalization(general=NamedElement, specific=tfsm_plaink3_FSMClock)
gen_tfsm_plaink3_TimedSystem_NamedElement = Generalization(general=NamedElement, specific=tfsm_plaink3_TimedSystem)
gen_tfsm_plaink3_EvaluateGuard_Guard = Generalization(general=Guard, specific=tfsm_plaink3_EvaluateGuard)
gen_tfsm_plaink3_Guard_NamedElement = Generalization(general=NamedElement, specific=tfsm_plaink3_Guard)
gen_tfsm_plaink3_TemporalGuard_Guard = Generalization(general=Guard, specific=tfsm_plaink3_TemporalGuard)
gen_tfsm_plaink3_EventGuard_Guard = Generalization(general=Guard, specific=tfsm_plaink3_EventGuard)
gen_tfsm_plaink3_FSMEvent_NamedElement = Generalization(general=NamedElement, specific=tfsm_plaink3_FSMEvent)

# Domain Model
domain_model = DomainModel(
    name="tfsm_plaink3",
    types={tfsm_plaink3_FSMClock, tfsm_plaink3_Transition, tfsm_plaink3_TFSM, NamedElement, tfsm_plaink3_State, tfsm_plaink3_FSMEvent, tfsm_plaink3_TimedSystem, tfsm_plaink3_EvaluateGuard, tfsm_plaink3_Guard, tfsm_plaink3_NamedElement, tfsm_plaink3_TemporalGuard, Guard, tfsm_plaink3_EventGuard},
    associations={localClock4, ownedTransitions6, owningFSM8, outgoingTransitions9, incomingTransitions10, source12, target14, ownedStates0, initialState1, localEvents2, tfsms28, globalClocks30, globalEvents33, ownedGuard16, generatedEvents18, onClock21, triggeringEvent23, sollicitingTransitions25},
    generalizations={gen_tfsm_plaink3_State_NamedElement, gen_tfsm_plaink3_Transition_NamedElement, gen_tfsm_plaink3_TFSM_NamedElement, gen_tfsm_plaink3_FSMClock_NamedElement, gen_tfsm_plaink3_TimedSystem_NamedElement, gen_tfsm_plaink3_EvaluateGuard_Guard, gen_tfsm_plaink3_Guard_NamedElement, gen_tfsm_plaink3_TemporalGuard_Guard, gen_tfsm_plaink3_EventGuard_Guard, gen_tfsm_plaink3_FSMEvent_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)