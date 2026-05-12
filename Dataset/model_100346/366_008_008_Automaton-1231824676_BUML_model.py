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

# Enumerations
EventContext: Enumeration = Enumeration(
    name="EventContext",
    literals={
            EnumerationLiteral(name="CHRONICLE"),
			EnumerationLiteral(name="RECENT"),
			EnumerationLiteral(name="UNRESTRICTED"),
			EnumerationLiteral(name="IMMEDIATE"),
			EnumerationLiteral(name="STRICT_IMMEDIATE")
    }
)

# Classes
automaton_InternalModel = Class(name="automaton_InternalModel")
automaton_Automaton = Class(name="automaton_Automaton")
automaton_Event = Class(name="automaton_Event")
automaton_Transition = Class(name="automaton_Transition", is_abstract=True)
automaton_State = Class(name="automaton_State")
automaton_EventPattern = Class(name="automaton_EventPattern")
automaton_EventToken = Class(name="automaton_EventToken")
automaton_TimedZone = Class(name="automaton_TimedZone", is_abstract=True)
automaton_InitState = Class(name="automaton_InitState")
State = Class(name="State")
automaton_FinalState = Class(name="automaton_FinalState")
automaton_TrapState = Class(name="automaton_TrapState")
automaton_Within = Class(name="automaton_Within")
TimedZone = Class(name="TimedZone")
automaton_TypedTransition = Class(name="automaton_TypedTransition")
Transition = Class(name="Transition")
automaton_Guard = Class(name="automaton_Guard")
automaton_EpsilonTransition = Class(name="automaton_EpsilonTransition")
automaton_AtomicEventPattern = Class(name="automaton_AtomicEventPattern")
automaton_HoldsFor = Class(name="automaton_HoldsFor")

# automaton_InternalModel class attributes and methods
automaton_InternalModel_context: Property = Property(name="context", type=StringType)
automaton_InternalModel.attributes={automaton_InternalModel_context}

# automaton_Automaton class attributes and methods

# automaton_Event class attributes and methods

# automaton_Transition class attributes and methods

# automaton_State class attributes and methods
automaton_State_label: Property = Property(name="label", type=StringType)
automaton_State.attributes={automaton_State_label}

# automaton_EventPattern class attributes and methods

# automaton_EventToken class attributes and methods

# automaton_TimedZone class attributes and methods
automaton_TimedZone_time: Property = Property(name="time", type=StringType)
automaton_TimedZone.attributes={automaton_TimedZone_time}

# automaton_InitState class attributes and methods

# State class attributes and methods

# automaton_FinalState class attributes and methods

# automaton_TrapState class attributes and methods

# automaton_Within class attributes and methods

# TimedZone class attributes and methods

# automaton_TypedTransition class attributes and methods

# Transition class attributes and methods

# automaton_Guard class attributes and methods

# automaton_EpsilonTransition class attributes and methods

# automaton_AtomicEventPattern class attributes and methods

# automaton_HoldsFor class attributes and methods

# Relationships
automata0: BinaryAssociation = BinaryAssociation(
    name="automata0",
    ends={
        Property(name="automaton_Automaton", type=automaton_InternalModel, multiplicity=Multiplicity(1, 1)),
        Property(name="automaton_InternalModel", type=automaton_Automaton, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
currentState10: BinaryAssociation = BinaryAssociation(
    name="currentState10",
    ends={
        Property(name="State", type=automaton_EventToken, multiplicity=Multiplicity(1, 1)),
        Property(name="eventTokens", type=automaton_State, multiplicity=Multiplicity(0, 1))
    }
)
recordedEvents11: BinaryAssociation = BinaryAssociation(
    name="recordedEvents11",
    ends={
        Property(name="automaton_Event13", type=automaton_EventToken, multiplicity=Multiplicity(1, 1)),
        Property(name="automaton_EventToken12", type=automaton_Event, multiplicity=Multiplicity(0, 9999))
    }
)
lastProcessed14: BinaryAssociation = BinaryAssociation(
    name="lastProcessed14",
    ends={
        Property(name="automaton_Event16", type=automaton_EventToken, multiplicity=Multiplicity(1, 1)),
        Property(name="automaton_EventToken15", type=automaton_Event, multiplicity=Multiplicity(0, 1))
    }
)
timedZones17: BinaryAssociation = BinaryAssociation(
    name="timedZones17",
    ends={
        Property(name="automaton_TimedZone19", type=automaton_EventToken, multiplicity=Multiplicity(1, 1)),
        Property(name="automaton_EventToken18", type=automaton_TimedZone, multiplicity=Multiplicity(0, 9999))
    }
)
inTransitions20: BinaryAssociation = BinaryAssociation(
    name="inTransitions20",
    ends={
        Property(name="Transition", type=automaton_State, multiplicity=Multiplicity(1, 1)),
        Property(name="postState", type=automaton_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
outTransitions21: BinaryAssociation = BinaryAssociation(
    name="outTransitions21",
    ends={
        Property(name="Transition22", type=automaton_State, multiplicity=Multiplicity(1, 1)),
        Property(name="preState", type=automaton_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
latestEvent1: BinaryAssociation = BinaryAssociation(
    name="latestEvent1",
    ends={
        Property(name="automaton_Event", type=automaton_InternalModel, multiplicity=Multiplicity(1, 1)),
        Property(name="automaton_InternalModel2", type=automaton_Event, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
states3: BinaryAssociation = BinaryAssociation(
    name="states3",
    ends={
        Property(name="automaton_State", type=automaton_Automaton, multiplicity=Multiplicity(1, 1)),
        Property(name="automaton_Automaton4", type=automaton_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eventPattern5: BinaryAssociation = BinaryAssociation(
    name="eventPattern5",
    ends={
        Property(name="Cep.ecoreEventPattern", type=automaton_Automaton, multiplicity=Multiplicity(1, 1)),
        Property(name="automaton", type=automaton_EventPattern, multiplicity=Multiplicity(1, 1))
    }
)
eventTokens6: BinaryAssociation = BinaryAssociation(
    name="eventTokens6",
    ends={
        Property(name="automaton_EventToken", type=automaton_Automaton, multiplicity=Multiplicity(1, 1)),
        Property(name="automaton_Automaton7", type=automaton_EventToken, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
timedZones8: BinaryAssociation = BinaryAssociation(
    name="timedZones8",
    ends={
        Property(name="automaton_TimedZone", type=automaton_Automaton, multiplicity=Multiplicity(1, 1)),
        Property(name="automaton_Automaton9", type=automaton_TimedZone, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inStateOf27: BinaryAssociation = BinaryAssociation(
    name="inStateOf27",
    ends={
        Property(name="TimedZone", type=automaton_State, multiplicity=Multiplicity(1, 1)),
        Property(name="inState", type=automaton_TimedZone, multiplicity=Multiplicity(0, 9999))
    }
)
outStateOf28: BinaryAssociation = BinaryAssociation(
    name="outStateOf28",
    ends={
        Property(name="TimedZone29", type=automaton_State, multiplicity=Multiplicity(1, 1)),
        Property(name="outState", type=automaton_TimedZone, multiplicity=Multiplicity(0, 9999))
    }
)
preState30: BinaryAssociation = BinaryAssociation(
    name="preState30",
    ends={
        Property(name="State31", type=automaton_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outTransitions", type=automaton_State, multiplicity=Multiplicity(0, 1))
    }
)
postState32: BinaryAssociation = BinaryAssociation(
    name="postState32",
    ends={
        Property(name="State33", type=automaton_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="inTransitions", type=automaton_State, multiplicity=Multiplicity(0, 1))
    }
)
eventTokens23: BinaryAssociation = BinaryAssociation(
    name="eventTokens23",
    ends={
        Property(name="EventToken", type=automaton_State, multiplicity=Multiplicity(1, 1)),
        Property(name="currentState", type=automaton_EventToken, multiplicity=Multiplicity(0, 9999))
    }
)
lastProcessedEvent24: BinaryAssociation = BinaryAssociation(
    name="lastProcessedEvent24",
    ends={
        Property(name="automaton_Event26", type=automaton_State, multiplicity=Multiplicity(1, 1)),
        Property(name="automaton_State25", type=automaton_Event, multiplicity=Multiplicity(0, 1))
    }
)
inState37: BinaryAssociation = BinaryAssociation(
    name="inState37",
    ends={
        Property(name="State38", type=automaton_TimedZone, multiplicity=Multiplicity(1, 1)),
        Property(name="inStateOf", type=automaton_State, multiplicity=Multiplicity(1, 1))
    }
)
outState39: BinaryAssociation = BinaryAssociation(
    name="outState39",
    ends={
        Property(name="State40", type=automaton_TimedZone, multiplicity=Multiplicity(1, 1)),
        Property(name="outStateOf", type=automaton_State, multiplicity=Multiplicity(1, 1))
    }
)
guard34: BinaryAssociation = BinaryAssociation(
    name="guard34",
    ends={
        Property(name="Guard", type=automaton_TypedTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="transition", type=automaton_Guard, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
eventType35: BinaryAssociation = BinaryAssociation(
    name="eventType35",
    ends={
        Property(name="automaton_AtomicEventPattern", type=automaton_Guard, multiplicity=Multiplicity(1, 1)),
        Property(name="automaton_Guard", type=automaton_AtomicEventPattern, multiplicity=Multiplicity(1, 1))
    }
)
transition36: BinaryAssociation = BinaryAssociation(
    name="transition36",
    ends={
        Property(name="TypedTransition", type=automaton_Guard, multiplicity=Multiplicity(1, 1)),
        Property(name="guard", type=automaton_TypedTransition, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_automaton_InitState_State = Generalization(general=State, specific=automaton_InitState)
gen_automaton_FinalState_State = Generalization(general=State, specific=automaton_FinalState)
gen_automaton_TrapState_State = Generalization(general=State, specific=automaton_TrapState)
gen_automaton_Within_TimedZone = Generalization(general=TimedZone, specific=automaton_Within)
gen_automaton_TypedTransition_Transition = Generalization(general=Transition, specific=automaton_TypedTransition)
gen_automaton_EpsilonTransition_Transition = Generalization(general=Transition, specific=automaton_EpsilonTransition)
gen_automaton_HoldsFor_TimedZone = Generalization(general=TimedZone, specific=automaton_HoldsFor)

# Domain Model
domain_model = DomainModel(
    name="automaton",
    types={automaton_InternalModel, automaton_Automaton, automaton_Event, automaton_Transition, automaton_State, automaton_EventPattern, automaton_EventToken, automaton_TimedZone, automaton_InitState, State, automaton_FinalState, automaton_TrapState, automaton_Within, TimedZone, automaton_TypedTransition, Transition, automaton_Guard, automaton_EpsilonTransition, automaton_AtomicEventPattern, automaton_HoldsFor, EventContext},
    associations={automata0, currentState10, recordedEvents11, lastProcessed14, timedZones17, inTransitions20, outTransitions21, latestEvent1, states3, eventPattern5, eventTokens6, timedZones8, inStateOf27, outStateOf28, preState30, postState32, eventTokens23, lastProcessedEvent24, inState37, outState39, guard34, eventType35, transition36},
    generalizations={gen_automaton_InitState_State, gen_automaton_FinalState_State, gen_automaton_TrapState_State, gen_automaton_Within_TimedZone, gen_automaton_TypedTransition_Transition, gen_automaton_EpsilonTransition_Transition, gen_automaton_HoldsFor_TimedZone},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)