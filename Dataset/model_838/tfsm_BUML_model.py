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
tfsm_FSMEvent = Class(name="tfsm::FSMEvent")
tfsm_FSMClock = Class(name="tfsm::FSMClock")
tfsm_Guard = Class(name="tfsm::Guard", is_abstract=True)
tfsm_NamedElement = Class(name="tfsm::NamedElement", is_abstract=True)
tfsm_TemporalGuard = Class(name="tfsm::TemporalGuard")
Guard = Class(name="Guard")
tfsm_Transition = Class(name="tfsm::Transition")
tfsm_TimedSystem = Class(name="tfsm::TimedSystem")
tfsm_EvaluateGuard = Class(name="tfsm::EvaluateGuard")
tfsm_EventGuard = Class(name="tfsm::EventGuard")

# tfsm_TFSM class attributes and methods

# NamedElement class attributes and methods

# tfsm_State class attributes and methods

# tfsm_FSMEvent class attributes and methods

# tfsm_FSMClock class attributes and methods

# tfsm_Guard class attributes and methods

# tfsm_NamedElement class attributes and methods
tfsm_NamedElement_name: Property = Property(name="name", type=StringType)
tfsm_NamedElement.attributes={tfsm_NamedElement_name}

# tfsm_TemporalGuard class attributes and methods
tfsm_TemporalGuard_afterDuration: Property = Property(name="afterDuration", type=IntegerType)
tfsm_TemporalGuard.attributes={tfsm_TemporalGuard_afterDuration}

# Guard class attributes and methods

# tfsm_Transition class attributes and methods
tfsm_Transition_action: Property = Property(name="action", type=StringType)
tfsm_Transition.attributes={tfsm_Transition_action}

# tfsm_TimedSystem class attributes and methods

# tfsm_EvaluateGuard class attributes and methods
tfsm_EvaluateGuard_condition: Property = Property(name="condition", type=StringType)
tfsm_EvaluateGuard.attributes={tfsm_EvaluateGuard_condition}

# tfsm_EventGuard class attributes and methods

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
owningFSM9: BinaryAssociation = BinaryAssociation(
    name="owningFSM9",
    ends={
        Property(name="11", type=tfsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="10", type=tfsm_TFSM, multiplicity=Multiplicity(1, 1))
    }
)
outgoingTransitions12: BinaryAssociation = BinaryAssociation(
    name="outgoingTransitions12",
    ends={
        Property(name="14", type=tfsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="13", type=tfsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
incomingTransitions15: BinaryAssociation = BinaryAssociation(
    name="incomingTransitions15",
    ends={
        Property(name="17", type=tfsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="16", type=tfsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
source18: BinaryAssociation = BinaryAssociation(
    name="source18",
    ends={
        Property(name="20", type=tfsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="19", type=tfsm_State, multiplicity=Multiplicity(1, 1))
    }
)
target21: BinaryAssociation = BinaryAssociation(
    name="target21",
    ends={
        Property(name="23", type=tfsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="22", type=tfsm_State, multiplicity=Multiplicity(1, 1))
    }
)
ownedGuard24: BinaryAssociation = BinaryAssociation(
    name="ownedGuard24",
    ends={
        Property(name="tfsm_Guard", type=tfsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_Transition25", type=tfsm_Guard, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
generatedEvents26: BinaryAssociation = BinaryAssociation(
    name="generatedEvents26",
    ends={
        Property(name="tfsm_FSMEvent28", type=tfsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_Transition27", type=tfsm_FSMEvent, multiplicity=Multiplicity(0, 9999))
    }
)
onClock29: BinaryAssociation = BinaryAssociation(
    name="onClock29",
    ends={
        Property(name="tfsm_FSMClock30", type=tfsm_TemporalGuard, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_TemporalGuard", type=tfsm_FSMClock, multiplicity=Multiplicity(1, 1))
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
tfsms36: BinaryAssociation = BinaryAssociation(
    name="tfsms36",
    ends={
        Property(name="tfsm_TFSM37", type=tfsm_TimedSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_TimedSystem", type=tfsm_TFSM, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
globalClocks38: BinaryAssociation = BinaryAssociation(
    name="globalClocks38",
    ends={
        Property(name="tfsm_FSMClock40", type=tfsm_TimedSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_TimedSystem39", type=tfsm_FSMClock, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
globalEvents41: BinaryAssociation = BinaryAssociation(
    name="globalEvents41",
    ends={
        Property(name="tfsm_FSMEvent43", type=tfsm_TimedSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_TimedSystem42", type=tfsm_FSMEvent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triggeringEvent31: BinaryAssociation = BinaryAssociation(
    name="triggeringEvent31",
    ends={
        Property(name="tfsm_FSMEvent32", type=tfsm_EventGuard, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_EventGuard", type=tfsm_FSMEvent, multiplicity=Multiplicity(1, 1))
    }
)
sollicitingTransitions33: BinaryAssociation = BinaryAssociation(
    name="sollicitingTransitions33",
    ends={
        Property(name="tfsm_Transition35", type=tfsm_FSMEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_FSMEvent34", type=tfsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_tfsm_TFSM_NamedElement = Generalization(general=NamedElement, specific=tfsm_TFSM)
gen_tfsm_State_NamedElement = Generalization(general=NamedElement, specific=tfsm_State)
gen_tfsm_Transition_NamedElement = Generalization(general=NamedElement, specific=tfsm_Transition)
gen_tfsm_Guard_NamedElement = Generalization(general=NamedElement, specific=tfsm_Guard)
gen_tfsm_TemporalGuard_Guard = Generalization(general=Guard, specific=tfsm_TemporalGuard)
gen_tfsm_FSMClock_NamedElement = Generalization(general=NamedElement, specific=tfsm_FSMClock)
gen_tfsm_TimedSystem_NamedElement = Generalization(general=NamedElement, specific=tfsm_TimedSystem)
gen_tfsm_EvaluateGuard_Guard = Generalization(general=Guard, specific=tfsm_EvaluateGuard)
gen_tfsm_EventGuard_Guard = Generalization(general=Guard, specific=tfsm_EventGuard)
gen_tfsm_FSMEvent_NamedElement = Generalization(general=NamedElement, specific=tfsm_FSMEvent)

# Domain Model
domain_model = DomainModel(
    name="tfsm",
    types={tfsm_TFSM, NamedElement, tfsm_State, tfsm_FSMEvent, tfsm_FSMClock, tfsm_Guard, tfsm_NamedElement, tfsm_TemporalGuard, Guard, tfsm_Transition, tfsm_TimedSystem, tfsm_EvaluateGuard, tfsm_EventGuard},
    associations={ownedStates0, initialState2, localEvents3, owningFSM9, outgoingTransitions12, incomingTransitions15, source18, target21, ownedGuard24, generatedEvents26, onClock29, localClock5, ownedTransitions7, tfsms36, globalClocks38, globalEvents41, triggeringEvent31, sollicitingTransitions33},
    generalizations={gen_tfsm_TFSM_NamedElement, gen_tfsm_State_NamedElement, gen_tfsm_Transition_NamedElement, gen_tfsm_Guard_NamedElement, gen_tfsm_TemporalGuard_Guard, gen_tfsm_FSMClock_NamedElement, gen_tfsm_TimedSystem_NamedElement, gen_tfsm_EvaluateGuard_Guard, gen_tfsm_EventGuard_Guard, gen_tfsm_FSMEvent_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)