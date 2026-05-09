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
trace_Trace = Class(name="trace_Trace")
trace_GlobalState = Class(name="trace_GlobalState")
Events = Class(name="Events")
TracedObjects = Class(name="TracedObjects")
trace_StaticObjectsPools = Class(name="trace_StaticObjectsPools")
EventOccurrence = Class(name="EventOccurrence")
Place_tokens_State = Class(name="Place_tokens_State")
trace_Transition = Class(name="trace_Transition")
trace_Net = Class(name="trace_Net")
trace_Events_EventOccurrence = Class(name="trace_Events_EventOccurrence", is_abstract=True)
Events_trace_GlobalState = Class(name="Events_trace_GlobalState")
trace_Events_Events = Class(name="trace_Events_Events")
Net_mainEntryEventOccurrence = Class(name="Net_mainEntryEventOccurrence")
Net_mainExitEventOccurrence = Class(name="Net_mainExitEventOccurrence")
Net_runEntryEventOccurrence = Class(name="Net_runEntryEventOccurrence")
Net_runExitEventOccurrence = Class(name="Net_runExitEventOccurrence")
Place_addTokenEntryEventOccurrence = Class(name="Place_addTokenEntryEventOccurrence")
Place_addTokenExitEventOccurrence = Class(name="Place_addTokenExitEventOccurrence")
Place_removeTokenEntryEventOccurrence = Class(name="Place_removeTokenEntryEventOccurrence")
Place_removeTokenExitEventOccurrence = Class(name="Place_removeTokenExitEventOccurrence")
Transition_isEnabledEntryEventOccurrence = Class(name="Transition_isEnabledEntryEventOccurrence")
Transition_isEnabledExitEventOccurrence = Class(name="Transition_isEnabledExitEventOccurrence")
Transition_fireEntryEventOccurrence = Class(name="Transition_fireEntryEventOccurrence")
Transition_fireExitEventOccurrence = Class(name="Transition_fireExitEventOccurrence")
trace_Events_Net_mainEntryEventOccurrence = Class(name="trace_Events_Net_mainEntryEventOccurrence")
Events_trace_Net = Class(name="Events_trace_Net")
trace_Events_Net_mainExitEventOccurrence = Class(name="trace_Events_Net_mainExitEventOccurrence")
trace_Events_Net_runEntryEventOccurrence = Class(name="trace_Events_Net_runEntryEventOccurrence")
trace_Events_Net_runExitEventOccurrence = Class(name="trace_Events_Net_runExitEventOccurrence")
trace_Events_Place_addTokenEntryEventOccurrence = Class(name="trace_Events_Place_addTokenEntryEventOccurrence")
petrinet_TracedPlace = Class(name="petrinet_TracedPlace")
trace_Events_Place_addTokenExitEventOccurrence = Class(name="trace_Events_Place_addTokenExitEventOccurrence")
trace_Events_Place_removeTokenEntryEventOccurrence = Class(name="trace_Events_Place_removeTokenEntryEventOccurrence")
trace_Events_Place_removeTokenExitEventOccurrence = Class(name="trace_Events_Place_removeTokenExitEventOccurrence")
trace_Events_Transition_isEnabledEntryEventOccurrence = Class(name="trace_Events_Transition_isEnabledEntryEventOccurrence")
Events_trace_Transition = Class(name="Events_trace_Transition")
trace_Events_Transition_isEnabledExitEventOccurrence = Class(name="trace_Events_Transition_isEnabledExitEventOccurrence")
Events_trace_EObject = Class(name="Events_trace_EObject")
trace_Events_Transition_fireEntryEventOccurrence = Class(name="trace_Events_Transition_fireEntryEventOccurrence")
trace_Events_Transition_fireExitEventOccurrence = Class(name="trace_Events_Transition_fireExitEventOccurrence")
trace_States_Place_tokens_State = Class(name="trace_States_Place_tokens_State")
States_trace_GlobalState = Class(name="States_trace_GlobalState")
trace_Traced_TracedObjects = Class(name="trace_Traced_TracedObjects")
trace_petrinet_TracedPlace = Class(name="trace_petrinet_TracedPlace")
petrinet_trace_Place = Class(name="petrinet_trace_Place")

# trace_Trace class attributes and methods

# trace_GlobalState class attributes and methods

# Events class attributes and methods

# TracedObjects class attributes and methods

# trace_StaticObjectsPools class attributes and methods

# EventOccurrence class attributes and methods

# Place_tokens_State class attributes and methods

# trace_Transition class attributes and methods

# trace_Net class attributes and methods

# trace_Events_EventOccurrence class attributes and methods

# Events_trace_GlobalState class attributes and methods

# trace_Events_Events class attributes and methods

# Net_mainEntryEventOccurrence class attributes and methods

# Net_mainExitEventOccurrence class attributes and methods

# Net_runEntryEventOccurrence class attributes and methods

# Net_runExitEventOccurrence class attributes and methods

# Place_addTokenEntryEventOccurrence class attributes and methods

# Place_addTokenExitEventOccurrence class attributes and methods

# Place_removeTokenEntryEventOccurrence class attributes and methods

# Place_removeTokenExitEventOccurrence class attributes and methods

# Transition_isEnabledEntryEventOccurrence class attributes and methods

# Transition_isEnabledExitEventOccurrence class attributes and methods

# Transition_fireEntryEventOccurrence class attributes and methods

# Transition_fireExitEventOccurrence class attributes and methods

# trace_Events_Net_mainEntryEventOccurrence class attributes and methods

# Events_trace_Net class attributes and methods

# trace_Events_Net_mainExitEventOccurrence class attributes and methods

# trace_Events_Net_runEntryEventOccurrence class attributes and methods

# trace_Events_Net_runExitEventOccurrence class attributes and methods

# trace_Events_Place_addTokenEntryEventOccurrence class attributes and methods

# petrinet_TracedPlace class attributes and methods

# trace_Events_Place_addTokenExitEventOccurrence class attributes and methods

# trace_Events_Place_removeTokenEntryEventOccurrence class attributes and methods

# trace_Events_Place_removeTokenExitEventOccurrence class attributes and methods

# trace_Events_Transition_isEnabledEntryEventOccurrence class attributes and methods

# Events_trace_Transition class attributes and methods

# trace_Events_Transition_isEnabledExitEventOccurrence class attributes and methods

# Events_trace_EObject class attributes and methods

# trace_Events_Transition_fireEntryEventOccurrence class attributes and methods

# trace_Events_Transition_fireExitEventOccurrence class attributes and methods

# trace_States_Place_tokens_State class attributes and methods
trace_States_Place_tokens_State_tokens: Property = Property(name="tokens", type=IntegerType)
trace_States_Place_tokens_State.attributes={trace_States_Place_tokens_State_tokens}

# States_trace_GlobalState class attributes and methods

# trace_Traced_TracedObjects class attributes and methods

# trace_petrinet_TracedPlace class attributes and methods
trace_petrinet_TracedPlace_initialTokens: Property = Property(name="initialTokens", type=IntegerType)
trace_petrinet_TracedPlace_name: Property = Property(name="name", type=StringType)
trace_petrinet_TracedPlace.attributes={trace_petrinet_TracedPlace_name, trace_petrinet_TracedPlace_initialTokens}

# petrinet_trace_Place class attributes and methods

# Relationships
globalTrace0: BinaryAssociation = BinaryAssociation(
    name="globalTrace0",
    ends={
        Property(name="trace_GlobalState", type=trace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Trace", type=trace_GlobalState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
events1: BinaryAssociation = BinaryAssociation(
    name="events1",
    ends={
        Property(name="Events", type=trace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Trace2", type=Events, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tracedObjects3: BinaryAssociation = BinaryAssociation(
    name="tracedObjects3",
    ends={
        Property(name="TracedObjects", type=trace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Trace4", type=TracedObjects, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
staticObjectsPools5: BinaryAssociation = BinaryAssociation(
    name="staticObjectsPools5",
    ends={
        Property(name="trace_StaticObjectsPools", type=trace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Trace6", type=trace_StaticObjectsPools, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
eventsTriggeredDuringState7: BinaryAssociation = BinaryAssociation(
    name="eventsTriggeredDuringState7",
    ends={
        Property(name="EventOccurrence", type=trace_GlobalState, multiplicity=Multiplicity(1, 1)),
        Property(name="stateDuringWhichTriggered", type=EventOccurrence, multiplicity=Multiplicity(0, 9999))
    }
)
place_tokens_States8: BinaryAssociation = BinaryAssociation(
    name="place_tokens_States8",
    ends={
        Property(name="Place_tokens_State", type=trace_GlobalState, multiplicity=Multiplicity(1, 1)),
        Property(name="globalStates", type=Place_tokens_State, multiplicity=Multiplicity(0, 9999))
    }
)
pool_Transitions9: BinaryAssociation = BinaryAssociation(
    name="pool_Transitions9",
    ends={
        Property(name="trace_Transition", type=trace_StaticObjectsPools, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_StaticObjectsPools10", type=trace_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pool_Nets11: BinaryAssociation = BinaryAssociation(
    name="pool_Nets11",
    ends={
        Property(name="trace_Net", type=trace_StaticObjectsPools, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_StaticObjectsPools12", type=trace_Net, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stateDuringWhichTriggered13: BinaryAssociation = BinaryAssociation(
    name="stateDuringWhichTriggered13",
    ends={
        Property(name="GlobalState", type=trace_Events_EventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="eventsTriggeredDuringState", type=Events_trace_GlobalState, multiplicity=Multiplicity(1, 1))
    }
)
Net_mainEntryEventOccurrence_Trace14: BinaryAssociation = BinaryAssociation(
    name="Net_mainEntryEventOccurrence_Trace14",
    ends={
        Property(name="Net_mainEntryEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events", type=Net_mainEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Net_mainExitEventOccurrence_Trace15: BinaryAssociation = BinaryAssociation(
    name="Net_mainExitEventOccurrence_Trace15",
    ends={
        Property(name="Net_mainExitEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events16", type=Net_mainExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Net_runEntryEventOccurrence_Trace17: BinaryAssociation = BinaryAssociation(
    name="Net_runEntryEventOccurrence_Trace17",
    ends={
        Property(name="Net_runEntryEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events18", type=Net_runEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Net_runExitEventOccurrence_Trace19: BinaryAssociation = BinaryAssociation(
    name="Net_runExitEventOccurrence_Trace19",
    ends={
        Property(name="Net_runExitEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events20", type=Net_runExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Place_addTokenEntryEventOccurrence_Trace21: BinaryAssociation = BinaryAssociation(
    name="Place_addTokenEntryEventOccurrence_Trace21",
    ends={
        Property(name="Place_addTokenEntryEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events22", type=Place_addTokenEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Place_addTokenExitEventOccurrence_Trace23: BinaryAssociation = BinaryAssociation(
    name="Place_addTokenExitEventOccurrence_Trace23",
    ends={
        Property(name="Place_addTokenExitEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events24", type=Place_addTokenExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Place_removeTokenEntryEventOccurrence_Trace25: BinaryAssociation = BinaryAssociation(
    name="Place_removeTokenEntryEventOccurrence_Trace25",
    ends={
        Property(name="Place_removeTokenEntryEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events26", type=Place_removeTokenEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Place_removeTokenExitEventOccurrence_Trace27: BinaryAssociation = BinaryAssociation(
    name="Place_removeTokenExitEventOccurrence_Trace27",
    ends={
        Property(name="Place_removeTokenExitEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events28", type=Place_removeTokenExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Transition_isEnabledEntryEventOccurrence_Trace29: BinaryAssociation = BinaryAssociation(
    name="Transition_isEnabledEntryEventOccurrence_Trace29",
    ends={
        Property(name="Transition_isEnabledEntryEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events30", type=Transition_isEnabledEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Transition_isEnabledExitEventOccurrence_Trace31: BinaryAssociation = BinaryAssociation(
    name="Transition_isEnabledExitEventOccurrence_Trace31",
    ends={
        Property(name="Transition_isEnabledExitEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events32", type=Transition_isEnabledExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Transition_fireEntryEventOccurrence_Trace33: BinaryAssociation = BinaryAssociation(
    name="Transition_fireEntryEventOccurrence_Trace33",
    ends={
        Property(name="Transition_fireEntryEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events34", type=Transition_fireEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Transition_fireExitEventOccurrence_Trace35: BinaryAssociation = BinaryAssociation(
    name="Transition_fireExitEventOccurrence_Trace35",
    ends={
        Property(name="Transition_fireExitEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events36", type=Transition_fireExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
thisParam37: BinaryAssociation = BinaryAssociation(
    name="thisParam37",
    ends={
        Property(name="Events_trace_Net", type=trace_Events_Net_mainEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Net_mainEntryEventOccurrence", type=Events_trace_Net, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent38: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent38",
    ends={
        Property(name="Net_mainEntryEventOccurrence39", type=trace_Events_Net_mainExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Net_mainExitEventOccurrence", type=Net_mainEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
thisParam40: BinaryAssociation = BinaryAssociation(
    name="thisParam40",
    ends={
        Property(name="Events_trace_Net41", type=trace_Events_Net_runEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Net_runEntryEventOccurrence", type=Events_trace_Net, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent42: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent42",
    ends={
        Property(name="Net_runEntryEventOccurrence43", type=trace_Events_Net_runExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Net_runExitEventOccurrence", type=Net_runEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
thisParam44: BinaryAssociation = BinaryAssociation(
    name="thisParam44",
    ends={
        Property(name="petrinet_TracedPlace", type=trace_Events_Place_addTokenEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Place_addTokenEntryEventOccurrence", type=petrinet_TracedPlace, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent45: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent45",
    ends={
        Property(name="Place_addTokenEntryEventOccurrence46", type=trace_Events_Place_addTokenExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Place_addTokenExitEventOccurrence", type=Place_addTokenEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
thisParam47: BinaryAssociation = BinaryAssociation(
    name="thisParam47",
    ends={
        Property(name="petrinet_TracedPlace48", type=trace_Events_Place_removeTokenEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Place_removeTokenEntryEventOccurrence", type=petrinet_TracedPlace, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent49: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent49",
    ends={
        Property(name="Place_removeTokenEntryEventOccurrence50", type=trace_Events_Place_removeTokenExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Place_removeTokenExitEventOccurrence", type=Place_removeTokenEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
thisParam51: BinaryAssociation = BinaryAssociation(
    name="thisParam51",
    ends={
        Property(name="Events_trace_Transition", type=trace_Events_Transition_isEnabledEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Transition_isEnabledEntryEventOccurrence", type=Events_trace_Transition, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent52: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent52",
    ends={
        Property(name="Transition_isEnabledEntryEventOccurrence53", type=trace_Events_Transition_isEnabledExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Transition_isEnabledExitEventOccurrence", type=Transition_isEnabledEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
returnReturn54: BinaryAssociation = BinaryAssociation(
    name="returnReturn54",
    ends={
        Property(name="Events_trace_EObject", type=trace_Events_Transition_isEnabledExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Transition_isEnabledExitEventOccurrence55", type=Events_trace_EObject, multiplicity=Multiplicity(0, 1))
    }
)
thisParam56: BinaryAssociation = BinaryAssociation(
    name="thisParam56",
    ends={
        Property(name="Events_trace_Transition57", type=trace_Events_Transition_fireEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Transition_fireEntryEventOccurrence", type=Events_trace_Transition, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent58: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent58",
    ends={
        Property(name="Transition_fireEntryEventOccurrence59", type=trace_Events_Transition_fireExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Transition_fireExitEventOccurrence", type=Transition_fireEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
globalStates61: BinaryAssociation = BinaryAssociation(
    name="globalStates61",
    ends={
        Property(name="GlobalState62", type=trace_States_Place_tokens_State, multiplicity=Multiplicity(1, 1)),
        Property(name="place_tokens_States", type=States_trace_GlobalState, multiplicity=Multiplicity(1, 9999))
    }
)
petrinet_tracedPlaces63: BinaryAssociation = BinaryAssociation(
    name="petrinet_tracedPlaces63",
    ends={
        Property(name="petrinet_TracedPlace64", type=trace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Traced_TracedObjects", type=petrinet_TracedPlace, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
originalObject65: BinaryAssociation = BinaryAssociation(
    name="originalObject65",
    ends={
        Property(name="petrinet_trace_Place", type=trace_petrinet_TracedPlace, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_petrinet_TracedPlace", type=petrinet_trace_Place, multiplicity=Multiplicity(0, 1))
    }
)
tokensTrace66: BinaryAssociation = BinaryAssociation(
    name="tokensTrace66",
    ends={
        Property(name="Place_tokens_State67", type=trace_petrinet_TracedPlace, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=Place_tokens_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent60: BinaryAssociation = BinaryAssociation(
    name="parent60",
    ends={
        Property(name="TracedPlace", type=trace_States_Place_tokens_State, multiplicity=Multiplicity(1, 1)),
        Property(name="tokensTrace", type=petrinet_TracedPlace, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_trace_Events_Net_mainEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_Net_mainEntryEventOccurrence)
gen_trace_Events_Net_mainExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_Net_mainExitEventOccurrence)
gen_trace_Events_Net_runEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_Net_runEntryEventOccurrence)
gen_trace_Events_Net_runExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_Net_runExitEventOccurrence)
gen_trace_Events_Place_addTokenEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_Place_addTokenEntryEventOccurrence)
gen_trace_Events_Place_addTokenExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_Place_addTokenExitEventOccurrence)
gen_trace_Events_Place_removeTokenEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_Place_removeTokenEntryEventOccurrence)
gen_trace_Events_Place_removeTokenExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_Place_removeTokenExitEventOccurrence)
gen_trace_Events_Transition_isEnabledEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_Transition_isEnabledEntryEventOccurrence)
gen_trace_Events_Transition_isEnabledExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_Transition_isEnabledExitEventOccurrence)
gen_trace_Events_Transition_fireEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_Transition_fireEntryEventOccurrence)
gen_trace_Events_Transition_fireExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_Transition_fireExitEventOccurrence)

# Domain Model
domain_model = DomainModel(
    name="trace",
    types={trace_Trace, trace_GlobalState, Events, TracedObjects, trace_StaticObjectsPools, EventOccurrence, Place_tokens_State, trace_Transition, trace_Net, trace_Events_EventOccurrence, Events_trace_GlobalState, trace_Events_Events, Net_mainEntryEventOccurrence, Net_mainExitEventOccurrence, Net_runEntryEventOccurrence, Net_runExitEventOccurrence, Place_addTokenEntryEventOccurrence, Place_addTokenExitEventOccurrence, Place_removeTokenEntryEventOccurrence, Place_removeTokenExitEventOccurrence, Transition_isEnabledEntryEventOccurrence, Transition_isEnabledExitEventOccurrence, Transition_fireEntryEventOccurrence, Transition_fireExitEventOccurrence, trace_Events_Net_mainEntryEventOccurrence, Events_trace_Net, trace_Events_Net_mainExitEventOccurrence, trace_Events_Net_runEntryEventOccurrence, trace_Events_Net_runExitEventOccurrence, trace_Events_Place_addTokenEntryEventOccurrence, petrinet_TracedPlace, trace_Events_Place_addTokenExitEventOccurrence, trace_Events_Place_removeTokenEntryEventOccurrence, trace_Events_Place_removeTokenExitEventOccurrence, trace_Events_Transition_isEnabledEntryEventOccurrence, Events_trace_Transition, trace_Events_Transition_isEnabledExitEventOccurrence, Events_trace_EObject, trace_Events_Transition_fireEntryEventOccurrence, trace_Events_Transition_fireExitEventOccurrence, trace_States_Place_tokens_State, States_trace_GlobalState, trace_Traced_TracedObjects, trace_petrinet_TracedPlace, petrinet_trace_Place},
    associations={globalTrace0, events1, tracedObjects3, staticObjectsPools5, eventsTriggeredDuringState7, place_tokens_States8, pool_Transitions9, pool_Nets11, stateDuringWhichTriggered13, Net_mainEntryEventOccurrence_Trace14, Net_mainExitEventOccurrence_Trace15, Net_runEntryEventOccurrence_Trace17, Net_runExitEventOccurrence_Trace19, Place_addTokenEntryEventOccurrence_Trace21, Place_addTokenExitEventOccurrence_Trace23, Place_removeTokenEntryEventOccurrence_Trace25, Place_removeTokenExitEventOccurrence_Trace27, Transition_isEnabledEntryEventOccurrence_Trace29, Transition_isEnabledExitEventOccurrence_Trace31, Transition_fireEntryEventOccurrence_Trace33, Transition_fireExitEventOccurrence_Trace35, thisParam37, correspondingEntryEvent38, thisParam40, correspondingEntryEvent42, thisParam44, correspondingEntryEvent45, thisParam47, correspondingEntryEvent49, thisParam51, correspondingEntryEvent52, returnReturn54, thisParam56, correspondingEntryEvent58, globalStates61, petrinet_tracedPlaces63, originalObject65, tokensTrace66, parent60},
    generalizations={gen_trace_Events_Net_mainEntryEventOccurrence_EventOccurrence, gen_trace_Events_Net_mainExitEventOccurrence_EventOccurrence, gen_trace_Events_Net_runEntryEventOccurrence_EventOccurrence, gen_trace_Events_Net_runExitEventOccurrence_EventOccurrence, gen_trace_Events_Place_addTokenEntryEventOccurrence_EventOccurrence, gen_trace_Events_Place_addTokenExitEventOccurrence_EventOccurrence, gen_trace_Events_Place_removeTokenEntryEventOccurrence_EventOccurrence, gen_trace_Events_Place_removeTokenExitEventOccurrence_EventOccurrence, gen_trace_Events_Transition_isEnabledEntryEventOccurrence_EventOccurrence, gen_trace_Events_Transition_isEnabledExitEventOccurrence_EventOccurrence, gen_trace_Events_Transition_fireEntryEventOccurrence_EventOccurrence, gen_trace_Events_Transition_fireExitEventOccurrence_EventOccurrence},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)