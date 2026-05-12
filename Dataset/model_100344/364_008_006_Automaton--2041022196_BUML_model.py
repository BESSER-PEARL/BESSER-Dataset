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
            EnumerationLiteral(name="UNRESTRICTED"),
			EnumerationLiteral(name="IMMEDIATE"),
			EnumerationLiteral(name="STRICT_IMMEDIATE"),
			EnumerationLiteral(name="NOT_SET"),
			EnumerationLiteral(name="CHRONICLE"),
			EnumerationLiteral(name="RECENT")
    }
)

# Classes
automaton_InternalModel = Class(name="automaton_InternalModel")
automaton_Automaton = Class(name="automaton_Automaton")
automaton_Event = Class(name="automaton_Event")
automaton_State = Class(name="automaton_State")
automaton_TimedZone = Class(name="automaton_TimedZone", is_abstract=True)
automaton_InitState = Class(name="automaton_InitState")
automaton_EventToken = Class(name="automaton_EventToken")
automaton_ParameterTable = Class(name="automaton_ParameterTable")
automaton_FinalState = Class(name="automaton_FinalState")
automaton_TrapState = Class(name="automaton_TrapState")
State = Class(name="State")
automaton_Transition = Class(name="automaton_Transition", is_abstract=True)
automaton_TypedTransition = Class(name="automaton_TypedTransition")
Transition = Class(name="Transition")
automaton_Guard = Class(name="automaton_Guard")
automaton_Parameter = Class(name="automaton_Parameter")
automaton_NegativeTransition = Class(name="automaton_NegativeTransition")
TypedTransition = Class(name="TypedTransition")
automaton_EpsilonTransition = Class(name="automaton_EpsilonTransition")
automaton_EventPattern = Class(name="automaton_EventPattern")
automaton_Within = Class(name="automaton_Within")
TimedZone = Class(name="TimedZone")
automaton_HoldsFor = Class(name="automaton_HoldsFor")
automaton_ParameterBinding = Class(name="automaton_ParameterBinding")

# automaton_InternalModel class attributes and methods

# automaton_Automaton class attributes and methods
automaton_Automaton_eventPatternId: Property = Property(name="eventPatternId", type=StringType)
automaton_Automaton.attributes={automaton_Automaton_eventPatternId}

# automaton_Event class attributes and methods

# automaton_State class attributes and methods
automaton_State_label: Property = Property(name="label", type=StringType)
automaton_State.attributes={automaton_State_label}

# automaton_TimedZone class attributes and methods
automaton_TimedZone_time: Property = Property(name="time", type=StringType)
automaton_TimedZone.attributes={automaton_TimedZone_time}

# automaton_InitState class attributes and methods

# automaton_EventToken class attributes and methods

# automaton_ParameterTable class attributes and methods

# automaton_FinalState class attributes and methods

# automaton_TrapState class attributes and methods

# State class attributes and methods

# automaton_Transition class attributes and methods

# automaton_TypedTransition class attributes and methods

# Transition class attributes and methods

# automaton_Guard class attributes and methods

# automaton_Parameter class attributes and methods
automaton_Parameter_position: Property = Property(name="position", type=IntegerType)
automaton_Parameter_symbolicName: Property = Property(name="symbolicName", type=StringType)
automaton_Parameter.attributes={automaton_Parameter_position, automaton_Parameter_symbolicName}

# automaton_NegativeTransition class attributes and methods

# TypedTransition class attributes and methods

# automaton_EpsilonTransition class attributes and methods

# automaton_EventPattern class attributes and methods

# automaton_Within class attributes and methods

# TimedZone class attributes and methods

# automaton_HoldsFor class attributes and methods

# automaton_ParameterBinding class attributes and methods
automaton_ParameterBinding_symbolicName: Property = Property(name="symbolicName", type=StringType)
automaton_ParameterBinding_value: Property = Property(name="value", type=StringType)
automaton_ParameterBinding.attributes={automaton_ParameterBinding_value, automaton_ParameterBinding_symbolicName}

# Relationships
automata0: BinaryAssociation = BinaryAssociation(
    name="automata0",
    ends={
        Property(name="automaton_Automaton", type=automaton_InternalModel, multiplicity=Multiplicity(1, 1)),
        Property(name="automaton_InternalModel", type=automaton_Automaton, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
latestEvent1: BinaryAssociation = BinaryAssociation(
    name="latestEvent1",
    ends={
        Property(name="automaton_Event", type=automaton_InternalModel, multiplicity=Multiplicity(1, 1)),
        Property(name="automaton_InternalModel2", type=automaton_Event, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
enabledForTheLatestEvent3: BinaryAssociation = BinaryAssociation(
    name="enabledForTheLatestEvent3",
    ends={
        Property(name="automaton_Automaton5", type=automaton_InternalModel, multiplicity=Multiplicity(1, 1)),
        Property(name="automaton_InternalModel4", type=automaton_Automaton, multiplicity=Multiplicity(0, 9999))
    }
)
states8: BinaryAssociation = BinaryAssociation(
    name="states8",
    ends={
        Property(name="automaton_State", type=automaton_Automaton, multiplicity=Multiplicity(1, 1)),
        Property(name="automaton_Automaton9", type=automaton_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eventTokens10: BinaryAssociation = BinaryAssociation(
    name="eventTokens10",
    ends={
        Property(name="automaton_EventToken12", type=automaton_Automaton, multiplicity=Multiplicity(1, 1)),
        Property(name="automaton_Automaton11", type=automaton_EventToken, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
timedZones13: BinaryAssociation = BinaryAssociation(
    name="timedZones13",
    ends={
        Property(name="automaton_TimedZone", type=automaton_Automaton, multiplicity=Multiplicity(1, 1)),
        Property(name="automaton_Automaton14", type=automaton_TimedZone, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialState15: BinaryAssociation = BinaryAssociation(
    name="initialState15",
    ends={
        Property(name="automaton_InitState", type=automaton_Automaton, multiplicity=Multiplicity(1, 1)),
        Property(name="automaton_Automaton16", type=automaton_InitState, multiplicity=Multiplicity(1, 1))
    }
)
eventTokensInModel6: BinaryAssociation = BinaryAssociation(
    name="eventTokensInModel6",
    ends={
        Property(name="automaton_EventToken", type=automaton_InternalModel, multiplicity=Multiplicity(1, 1)),
        Property(name="automaton_InternalModel7", type=automaton_EventToken, multiplicity=Multiplicity(0, 9999))
    }
)
trapState19: BinaryAssociation = BinaryAssociation(
    name="trapState19",
    ends={
        Property(name="automaton_Automaton20", type=automaton_TrapState, multiplicity=Multiplicity(1, 1)),
        Property(name="automaton_TrapState", type=automaton_Automaton, multiplicity=Multiplicity(1, 1))
    }
)
currentState21: BinaryAssociation = BinaryAssociation(
    name="currentState21",
    ends={
        Property(name="State", type=automaton_EventToken, multiplicity=Multiplicity(1, 1)),
        Property(name="eventTokens", type=automaton_State, multiplicity=Multiplicity(0, 1))
    }
)
recordedEvents22: BinaryAssociation = BinaryAssociation(
    name="recordedEvents22",
    ends={
        Property(name="automaton_Event24", type=automaton_EventToken, multiplicity=Multiplicity(1, 1)),
        Property(name="automaton_EventToken23", type=automaton_Event, multiplicity=Multiplicity(0, 9999))
    }
)
lastProcessed25: BinaryAssociation = BinaryAssociation(
    name="lastProcessed25",
    ends={
        Property(name="automaton_Event27", type=automaton_EventToken, multiplicity=Multiplicity(1, 1)),
        Property(name="automaton_EventToken26", type=automaton_Event, multiplicity=Multiplicity(0, 1))
    }
)
timedZones28: BinaryAssociation = BinaryAssociation(
    name="timedZones28",
    ends={
        Property(name="automaton_TimedZone30", type=automaton_EventToken, multiplicity=Multiplicity(1, 1)),
        Property(name="automaton_EventToken29", type=automaton_TimedZone, multiplicity=Multiplicity(0, 9999))
    }
)
parameterTable31: BinaryAssociation = BinaryAssociation(
    name="parameterTable31",
    ends={
        Property(name="ParameterTable", type=automaton_EventToken, multiplicity=Multiplicity(1, 1)),
        Property(name="eventToken", type=automaton_ParameterTable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
finalStates17: BinaryAssociation = BinaryAssociation(
    name="finalStates17",
    ends={
        Property(name="automaton_FinalState", type=automaton_Automaton, multiplicity=Multiplicity(1, 1)),
        Property(name="automaton_Automaton18", type=automaton_FinalState, multiplicity=Multiplicity(1, 9999))
    }
)
eventTokens35: BinaryAssociation = BinaryAssociation(
    name="eventTokens35",
    ends={
        Property(name="EventToken", type=automaton_State, multiplicity=Multiplicity(1, 1)),
        Property(name="currentState", type=automaton_EventToken, multiplicity=Multiplicity(0, 9999))
    }
)
lastProcessedEvent36: BinaryAssociation = BinaryAssociation(
    name="lastProcessedEvent36",
    ends={
        Property(name="automaton_Event38", type=automaton_State, multiplicity=Multiplicity(1, 1)),
        Property(name="automaton_State37", type=automaton_Event, multiplicity=Multiplicity(0, 1))
    }
)
inStateOf39: BinaryAssociation = BinaryAssociation(
    name="inStateOf39",
    ends={
        Property(name="TimedZone", type=automaton_State, multiplicity=Multiplicity(1, 1)),
        Property(name="inState", type=automaton_TimedZone, multiplicity=Multiplicity(0, 9999))
    }
)
outStateOf40: BinaryAssociation = BinaryAssociation(
    name="outStateOf40",
    ends={
        Property(name="TimedZone41", type=automaton_State, multiplicity=Multiplicity(1, 1)),
        Property(name="outState", type=automaton_TimedZone, multiplicity=Multiplicity(0, 9999))
    }
)
inTransitions32: BinaryAssociation = BinaryAssociation(
    name="inTransitions32",
    ends={
        Property(name="Transition", type=automaton_State, multiplicity=Multiplicity(1, 1)),
        Property(name="postState", type=automaton_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
outTransitions33: BinaryAssociation = BinaryAssociation(
    name="outTransitions33",
    ends={
        Property(name="Transition34", type=automaton_State, multiplicity=Multiplicity(1, 1)),
        Property(name="preState", type=automaton_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
guards46: BinaryAssociation = BinaryAssociation(
    name="guards46",
    ends={
        Property(name="Guard", type=automaton_TypedTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="transition", type=automaton_Guard, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
parameters47: BinaryAssociation = BinaryAssociation(
    name="parameters47",
    ends={
        Property(name="Parameter", type=automaton_TypedTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="transition48", type=automaton_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eventType49: BinaryAssociation = BinaryAssociation(
    name="eventType49",
    ends={
        Property(name="automaton_EventPattern", type=automaton_Guard, multiplicity=Multiplicity(1, 1)),
        Property(name="automaton_Guard", type=automaton_EventPattern, multiplicity=Multiplicity(1, 1))
    }
)
preState42: BinaryAssociation = BinaryAssociation(
    name="preState42",
    ends={
        Property(name="State43", type=automaton_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outTransitions", type=automaton_State, multiplicity=Multiplicity(0, 1))
    }
)
postState44: BinaryAssociation = BinaryAssociation(
    name="postState44",
    ends={
        Property(name="State45", type=automaton_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="inTransitions", type=automaton_State, multiplicity=Multiplicity(0, 1))
    }
)
inState51: BinaryAssociation = BinaryAssociation(
    name="inState51",
    ends={
        Property(name="State52", type=automaton_TimedZone, multiplicity=Multiplicity(1, 1)),
        Property(name="inStateOf", type=automaton_State, multiplicity=Multiplicity(1, 1))
    }
)
outState53: BinaryAssociation = BinaryAssociation(
    name="outState53",
    ends={
        Property(name="State54", type=automaton_TimedZone, multiplicity=Multiplicity(1, 1)),
        Property(name="outStateOf", type=automaton_State, multiplicity=Multiplicity(1, 1))
    }
)
transition50: BinaryAssociation = BinaryAssociation(
    name="transition50",
    ends={
        Property(name="TypedTransition", type=automaton_Guard, multiplicity=Multiplicity(1, 1)),
        Property(name="guards", type=automaton_TypedTransition, multiplicity=Multiplicity(1, 1))
    }
)
parameterBindings57: BinaryAssociation = BinaryAssociation(
    name="parameterBindings57",
    ends={
        Property(name="parameterTable", type=automaton_ParameterBinding, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="ParameterBinding", type=automaton_ParameterTable, multiplicity=Multiplicity(1, 1))
    }
)
eventToken58: BinaryAssociation = BinaryAssociation(
    name="eventToken58",
    ends={
        Property(name="EventToken60", type=automaton_ParameterTable, multiplicity=Multiplicity(1, 1)),
        Property(name="parameterTable59", type=automaton_EventToken, multiplicity=Multiplicity(1, 1))
    }
)
parameterTable61: BinaryAssociation = BinaryAssociation(
    name="parameterTable61",
    ends={
        Property(name="ParameterTable62", type=automaton_ParameterBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="parameterBindings", type=automaton_ParameterTable, multiplicity=Multiplicity(1, 1))
    }
)
transition55: BinaryAssociation = BinaryAssociation(
    name="transition55",
    ends={
        Property(name="TypedTransition56", type=automaton_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameters", type=automaton_TypedTransition, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_automaton_InitState_State = Generalization(general=State, specific=automaton_InitState)
gen_automaton_FinalState_State = Generalization(general=State, specific=automaton_FinalState)
gen_automaton_TypedTransition_Transition = Generalization(general=Transition, specific=automaton_TypedTransition)
gen_automaton_NegativeTransition_TypedTransition = Generalization(general=TypedTransition, specific=automaton_NegativeTransition)
gen_automaton_EpsilonTransition_Transition = Generalization(general=Transition, specific=automaton_EpsilonTransition)
gen_automaton_TrapState_State = Generalization(general=State, specific=automaton_TrapState)
gen_automaton_Within_TimedZone = Generalization(general=TimedZone, specific=automaton_Within)
gen_automaton_HoldsFor_TimedZone = Generalization(general=TimedZone, specific=automaton_HoldsFor)

# Domain Model
domain_model = DomainModel(
    name="automaton",
    types={automaton_InternalModel, automaton_Automaton, automaton_Event, automaton_State, automaton_TimedZone, automaton_InitState, automaton_EventToken, automaton_ParameterTable, automaton_FinalState, automaton_TrapState, State, automaton_Transition, automaton_TypedTransition, Transition, automaton_Guard, automaton_Parameter, automaton_NegativeTransition, TypedTransition, automaton_EpsilonTransition, automaton_EventPattern, automaton_Within, TimedZone, automaton_HoldsFor, automaton_ParameterBinding, EventContext},
    associations={automata0, latestEvent1, enabledForTheLatestEvent3, states8, eventTokens10, timedZones13, initialState15, eventTokensInModel6, trapState19, currentState21, recordedEvents22, lastProcessed25, timedZones28, parameterTable31, finalStates17, eventTokens35, lastProcessedEvent36, inStateOf39, outStateOf40, inTransitions32, outTransitions33, guards46, parameters47, eventType49, preState42, postState44, inState51, outState53, transition50, parameterBindings57, eventToken58, parameterTable61, transition55},
    generalizations={gen_automaton_InitState_State, gen_automaton_FinalState_State, gen_automaton_TypedTransition_Transition, gen_automaton_NegativeTransition_TypedTransition, gen_automaton_EpsilonTransition_Transition, gen_automaton_TrapState_State, gen_automaton_Within_TimedZone, gen_automaton_HoldsFor_TimedZone},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)