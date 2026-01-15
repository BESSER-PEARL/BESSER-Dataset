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
trace_Trace = Class(name="trace::Trace")
trace_GlobalState = Class(name="trace::GlobalState")
Events = Class(name="Events")
TracedObjects = Class(name="TracedObjects")
trace_StaticObjectsPools = Class(name="trace::StaticObjectsPools")
EventOccurrence = Class(name="EventOccurrence")
Net_runExitEventOccurrence = Class(name="Net::runExitEventOccurrence")
Place_tokens_State = Class(name="Place::tokens::State")
Place_addTokenEntryEventOccurrence = Class(name="Place::addTokenEntryEventOccurrence")
Place_addTokenExitEventOccurrence = Class(name="Place::addTokenExitEventOccurrence")
trace_Transition = Class(name="trace::Transition")
trace_Net = Class(name="trace::Net")
trace_Events_EventOccurrence = Class(name="trace::Events::EventOccurrence", is_abstract=True)
Events_trace_GlobalState = Class(name="Events::trace::GlobalState")
trace_Events_Events = Class(name="trace::Events::Events")
Net_mainEntryEventOccurrence = Class(name="Net::mainEntryEventOccurrence")
Net_mainExitEventOccurrence = Class(name="Net::mainExitEventOccurrence")
Net_runEntryEventOccurrence = Class(name="Net::runEntryEventOccurrence")
Transition_fireEntryEventOccurrence = Class(name="Transition::fireEntryEventOccurrence")
Transition_fireExitEventOccurrence = Class(name="Transition::fireExitEventOccurrence")
trace_Events_Net_mainEntryEventOccurrence = Class(name="trace::Events::Net::mainEntryEventOccurrence")
Events_trace_Net = Class(name="Events::trace::Net")
Place_removeTokenEntryEventOccurrence = Class(name="Place::removeTokenEntryEventOccurrence")
Place_removeTokenExitEventOccurrence = Class(name="Place::removeTokenExitEventOccurrence")
Transition_isEnabledEntryEventOccurrence = Class(name="Transition::isEnabledEntryEventOccurrence")
Transition_isEnabledExitEventOccurrence = Class(name="Transition::isEnabledExitEventOccurrence")
petrinet_TracedPlace = Class(name="petrinet::TracedPlace")
trace_Events_Place_addTokenExitEventOccurrence = Class(name="trace::Events::Place::addTokenExitEventOccurrence")
trace_Events_Place_removeTokenEntryEventOccurrence = Class(name="trace::Events::Place::removeTokenEntryEventOccurrence")
trace_Events_Net_mainExitEventOccurrence = Class(name="trace::Events::Net::mainExitEventOccurrence")
trace_Events_Net_runEntryEventOccurrence = Class(name="trace::Events::Net::runEntryEventOccurrence")
trace_Events_Net_runExitEventOccurrence = Class(name="trace::Events::Net::runExitEventOccurrence")
trace_Events_Place_addTokenEntryEventOccurrence = Class(name="trace::Events::Place::addTokenEntryEventOccurrence")
trace_Events_Transition_fireEntryEventOccurrence = Class(name="trace::Events::Transition::fireEntryEventOccurrence")
trace_Events_Transition_fireExitEventOccurrence = Class(name="trace::Events::Transition::fireExitEventOccurrence")
trace_States_Place_tokens_State = Class(name="trace::States::Place::tokens::State")
trace_Events_Place_removeTokenExitEventOccurrence = Class(name="trace::Events::Place::removeTokenExitEventOccurrence")
trace_Events_Transition_isEnabledEntryEventOccurrence = Class(name="trace::Events::Transition::isEnabledEntryEventOccurrence")
Events_trace_Transition = Class(name="Events::trace::Transition")
trace_Events_Transition_isEnabledExitEventOccurrence = Class(name="trace::Events::Transition::isEnabledExitEventOccurrence")
Events_trace_EObject = Class(name="Events::trace::EObject")
petrinet_trace_Place = Class(name="petrinet::trace::Place")
States_trace_GlobalState = Class(name="States::trace::GlobalState")
trace_Traced_TracedObjects = Class(name="trace::Traced::TracedObjects")
trace_petrinet_TracedPlace = Class(name="trace::petrinet::TracedPlace")

# trace_Trace class attributes and methods

# trace_GlobalState class attributes and methods

# Events class attributes and methods

# TracedObjects class attributes and methods

# trace_StaticObjectsPools class attributes and methods

# EventOccurrence class attributes and methods

# Net_runExitEventOccurrence class attributes and methods

# Place_tokens_State class attributes and methods

# Place_addTokenEntryEventOccurrence class attributes and methods

# Place_addTokenExitEventOccurrence class attributes and methods

# trace_Transition class attributes and methods

# trace_Net class attributes and methods

# trace_Events_EventOccurrence class attributes and methods

# Events_trace_GlobalState class attributes and methods

# trace_Events_Events class attributes and methods

# Net_mainEntryEventOccurrence class attributes and methods

# Net_mainExitEventOccurrence class attributes and methods

# Net_runEntryEventOccurrence class attributes and methods

# Transition_fireEntryEventOccurrence class attributes and methods

# Transition_fireExitEventOccurrence class attributes and methods

# trace_Events_Net_mainEntryEventOccurrence class attributes and methods

# Events_trace_Net class attributes and methods

# Place_removeTokenEntryEventOccurrence class attributes and methods

# Place_removeTokenExitEventOccurrence class attributes and methods

# Transition_isEnabledEntryEventOccurrence class attributes and methods

# Transition_isEnabledExitEventOccurrence class attributes and methods

# petrinet_TracedPlace class attributes and methods

# trace_Events_Place_addTokenExitEventOccurrence class attributes and methods

# trace_Events_Place_removeTokenEntryEventOccurrence class attributes and methods

# trace_Events_Net_mainExitEventOccurrence class attributes and methods

# trace_Events_Net_runEntryEventOccurrence class attributes and methods

# trace_Events_Net_runExitEventOccurrence class attributes and methods

# trace_Events_Place_addTokenEntryEventOccurrence class attributes and methods

# trace_Events_Transition_fireEntryEventOccurrence class attributes and methods

# trace_Events_Transition_fireExitEventOccurrence class attributes and methods

# trace_States_Place_tokens_State class attributes and methods
trace_States_Place_tokens_State_tokens: Property = Property(name="tokens", type=IntegerType)
trace_States_Place_tokens_State.attributes={trace_States_Place_tokens_State_tokens}

# trace_Events_Place_removeTokenExitEventOccurrence class attributes and methods

# trace_Events_Transition_isEnabledEntryEventOccurrence class attributes and methods

# Events_trace_Transition class attributes and methods

# trace_Events_Transition_isEnabledExitEventOccurrence class attributes and methods

# Events_trace_EObject class attributes and methods

# petrinet_trace_Place class attributes and methods

# States_trace_GlobalState class attributes and methods

# trace_Traced_TracedObjects class attributes and methods

# trace_petrinet_TracedPlace class attributes and methods
trace_petrinet_TracedPlace_initialTokens: Property = Property(name="initialTokens", type=IntegerType)
trace_petrinet_TracedPlace_name: Property = Property(name="name", type=StringType)
trace_petrinet_TracedPlace.attributes={trace_petrinet_TracedPlace_initialTokens, trace_petrinet_TracedPlace_name}

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
Net_runEntryEventOccurrence_Trace18: BinaryAssociation = BinaryAssociation(
    name="Net_runEntryEventOccurrence_Trace18",
    ends={
        Property(name="Net_runEntryEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events19", type=Net_runEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eventsTriggeredDuringState7: BinaryAssociation = BinaryAssociation(
    name="eventsTriggeredDuringState7",
    ends={
        Property(name="Events8", type=trace_GlobalState, multiplicity=Multiplicity(1, 1)),
        Property(name="EventOccurrence", type=EventOccurrence, multiplicity=Multiplicity(0, 9999))
    }
)
Net_runExitEventOccurrence_Trace20: BinaryAssociation = BinaryAssociation(
    name="Net_runExitEventOccurrence_Trace20",
    ends={
        Property(name="Net_runExitEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events21", type=Net_runExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
place_tokens_States9: BinaryAssociation = BinaryAssociation(
    name="place_tokens_States9",
    ends={
        Property(name="States", type=trace_GlobalState, multiplicity=Multiplicity(1, 1)),
        Property(name="Place_tokens_State", type=Place_tokens_State, multiplicity=Multiplicity(0, 9999))
    }
)
Place_addTokenEntryEventOccurrence_Trace22: BinaryAssociation = BinaryAssociation(
    name="Place_addTokenEntryEventOccurrence_Trace22",
    ends={
        Property(name="Place_addTokenEntryEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events23", type=Place_addTokenEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Place_addTokenExitEventOccurrence_Trace24: BinaryAssociation = BinaryAssociation(
    name="Place_addTokenExitEventOccurrence_Trace24",
    ends={
        Property(name="Place_addTokenExitEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events25", type=Place_addTokenExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pool_Transitions10: BinaryAssociation = BinaryAssociation(
    name="pool_Transitions10",
    ends={
        Property(name="trace_Transition", type=trace_StaticObjectsPools, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_StaticObjectsPools11", type=trace_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pool_Nets12: BinaryAssociation = BinaryAssociation(
    name="pool_Nets12",
    ends={
        Property(name="trace_Net", type=trace_StaticObjectsPools, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_StaticObjectsPools13", type=trace_Net, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stateDuringWhichTriggered14: BinaryAssociation = BinaryAssociation(
    name="stateDuringWhichTriggered14",
    ends={
        Property(name="GlobalState", type=trace_Events_EventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="eventsTriggeredDuringState", type=Events_trace_GlobalState, multiplicity=Multiplicity(1, 1))
    }
)
Net_mainEntryEventOccurrence_Trace15: BinaryAssociation = BinaryAssociation(
    name="Net_mainEntryEventOccurrence_Trace15",
    ends={
        Property(name="Net_mainEntryEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events", type=Net_mainEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Net_mainExitEventOccurrence_Trace16: BinaryAssociation = BinaryAssociation(
    name="Net_mainExitEventOccurrence_Trace16",
    ends={
        Property(name="Net_mainExitEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events17", type=Net_mainExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Transition_fireEntryEventOccurrence_Trace34: BinaryAssociation = BinaryAssociation(
    name="Transition_fireEntryEventOccurrence_Trace34",
    ends={
        Property(name="Transition_fireEntryEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events35", type=Transition_fireEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Transition_fireExitEventOccurrence_Trace36: BinaryAssociation = BinaryAssociation(
    name="Transition_fireExitEventOccurrence_Trace36",
    ends={
        Property(name="Transition_fireExitEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events37", type=Transition_fireExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
thisParam38: BinaryAssociation = BinaryAssociation(
    name="thisParam38",
    ends={
        Property(name="Events_trace_Net", type=trace_Events_Net_mainEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Net_mainEntryEventOccurrence", type=Events_trace_Net, multiplicity=Multiplicity(0, 1))
    }
)
Place_removeTokenEntryEventOccurrence_Trace26: BinaryAssociation = BinaryAssociation(
    name="Place_removeTokenEntryEventOccurrence_Trace26",
    ends={
        Property(name="Place_removeTokenEntryEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events27", type=Place_removeTokenEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Place_removeTokenExitEventOccurrence_Trace28: BinaryAssociation = BinaryAssociation(
    name="Place_removeTokenExitEventOccurrence_Trace28",
    ends={
        Property(name="Place_removeTokenExitEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events29", type=Place_removeTokenExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Transition_isEnabledEntryEventOccurrence_Trace30: BinaryAssociation = BinaryAssociation(
    name="Transition_isEnabledEntryEventOccurrence_Trace30",
    ends={
        Property(name="Transition_isEnabledEntryEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events31", type=Transition_isEnabledEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Transition_isEnabledExitEventOccurrence_Trace32: BinaryAssociation = BinaryAssociation(
    name="Transition_isEnabledExitEventOccurrence_Trace32",
    ends={
        Property(name="Transition_isEnabledExitEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events33", type=Transition_isEnabledExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
thisParam45: BinaryAssociation = BinaryAssociation(
    name="thisParam45",
    ends={
        Property(name="petrinet_TracedPlace", type=trace_Events_Place_addTokenEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Place_addTokenEntryEventOccurrence", type=petrinet_TracedPlace, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent46: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent46",
    ends={
        Property(name="Place_addTokenEntryEventOccurrence47", type=trace_Events_Place_addTokenExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Place_addTokenExitEventOccurrence", type=Place_addTokenEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
thisParam48: BinaryAssociation = BinaryAssociation(
    name="thisParam48",
    ends={
        Property(name="petrinet_TracedPlace49", type=trace_Events_Place_removeTokenEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Place_removeTokenEntryEventOccurrence", type=petrinet_TracedPlace, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent39: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent39",
    ends={
        Property(name="Net_mainEntryEventOccurrence40", type=trace_Events_Net_mainExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Net_mainExitEventOccurrence", type=Net_mainEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
thisParam41: BinaryAssociation = BinaryAssociation(
    name="thisParam41",
    ends={
        Property(name="Events_trace_Net42", type=trace_Events_Net_runEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Net_runEntryEventOccurrence", type=Events_trace_Net, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent43: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent43",
    ends={
        Property(name="Net_runEntryEventOccurrence44", type=trace_Events_Net_runExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Net_runExitEventOccurrence", type=Net_runEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
returnReturn55: BinaryAssociation = BinaryAssociation(
    name="returnReturn55",
    ends={
        Property(name="trace_Events_Transition_isEnabledExitEventOccurrence56", type=Events_trace_EObject, multiplicity=Multiplicity(0, 1)),
        Property(name="Events_trace_EObject", type=trace_Events_Transition_isEnabledExitEventOccurrence, multiplicity=Multiplicity(1, 1))
    }
)
thisParam57: BinaryAssociation = BinaryAssociation(
    name="thisParam57",
    ends={
        Property(name="Events_trace_Transition58", type=trace_Events_Transition_fireEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Transition_fireEntryEventOccurrence", type=Events_trace_Transition, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent59: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent59",
    ends={
        Property(name="Transition_fireEntryEventOccurrence60", type=trace_Events_Transition_fireExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Transition_fireExitEventOccurrence", type=Transition_fireEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent50: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent50",
    ends={
        Property(name="Place_removeTokenEntryEventOccurrence51", type=trace_Events_Place_removeTokenExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Place_removeTokenExitEventOccurrence", type=Place_removeTokenEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
thisParam52: BinaryAssociation = BinaryAssociation(
    name="thisParam52",
    ends={
        Property(name="Events_trace_Transition", type=trace_Events_Transition_isEnabledEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Transition_isEnabledEntryEventOccurrence", type=Events_trace_Transition, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent53: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent53",
    ends={
        Property(name="Transition_isEnabledEntryEventOccurrence54", type=trace_Events_Transition_isEnabledExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Transition_isEnabledExitEventOccurrence", type=Transition_isEnabledEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
originalObject66: BinaryAssociation = BinaryAssociation(
    name="originalObject66",
    ends={
        Property(name="petrinet_trace_Place", type=trace_petrinet_TracedPlace, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_petrinet_TracedPlace", type=petrinet_trace_Place, multiplicity=Multiplicity(0, 1))
    }
)
tokensTrace67: BinaryAssociation = BinaryAssociation(
    name="tokensTrace67",
    ends={
        Property(name="States69", type=trace_petrinet_TracedPlace, multiplicity=Multiplicity(1, 1)),
        Property(name="Place_tokens_State68", type=Place_tokens_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent61: BinaryAssociation = BinaryAssociation(
    name="parent61",
    ends={
        Property(name="Traced", type=trace_States_Place_tokens_State, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet", type=petrinet_TracedPlace, multiplicity=Multiplicity(1, 1))
    }
)
globalStates62: BinaryAssociation = BinaryAssociation(
    name="globalStates62",
    ends={
        Property(name="GlobalState63", type=trace_States_Place_tokens_State, multiplicity=Multiplicity(1, 1)),
        Property(name="place_tokens_States", type=States_trace_GlobalState, multiplicity=Multiplicity(1, 9999))
    }
)
petrinet_tracedPlaces64: BinaryAssociation = BinaryAssociation(
    name="petrinet_tracedPlaces64",
    ends={
        Property(name="petrinet_TracedPlace65", type=trace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Traced_TracedObjects", type=petrinet_TracedPlace, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_trace_Events_Net_mainEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_Net_mainEntryEventOccurrence)
gen_trace_Events_Place_addTokenExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_Place_addTokenExitEventOccurrence)
gen_trace_Events_Place_removeTokenEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_Place_removeTokenEntryEventOccurrence)
gen_trace_Events_Net_mainExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_Net_mainExitEventOccurrence)
gen_trace_Events_Net_runEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_Net_runEntryEventOccurrence)
gen_trace_Events_Net_runExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_Net_runExitEventOccurrence)
gen_trace_Events_Place_addTokenEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_Place_addTokenEntryEventOccurrence)
gen_trace_Events_Transition_fireEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_Transition_fireEntryEventOccurrence)
gen_trace_Events_Transition_fireExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_Transition_fireExitEventOccurrence)
gen_trace_Events_Place_removeTokenExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_Place_removeTokenExitEventOccurrence)
gen_trace_Events_Transition_isEnabledEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_Transition_isEnabledEntryEventOccurrence)
gen_trace_Events_Transition_isEnabledExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_Transition_isEnabledExitEventOccurrence)

# Domain Model
domain_model = DomainModel(
    name="trace",
    types={trace_Trace, trace_GlobalState, Events, TracedObjects, trace_StaticObjectsPools, EventOccurrence, Net_runExitEventOccurrence, Place_tokens_State, Place_addTokenEntryEventOccurrence, Place_addTokenExitEventOccurrence, trace_Transition, trace_Net, trace_Events_EventOccurrence, Events_trace_GlobalState, trace_Events_Events, Net_mainEntryEventOccurrence, Net_mainExitEventOccurrence, Net_runEntryEventOccurrence, Transition_fireEntryEventOccurrence, Transition_fireExitEventOccurrence, trace_Events_Net_mainEntryEventOccurrence, Events_trace_Net, Place_removeTokenEntryEventOccurrence, Place_removeTokenExitEventOccurrence, Transition_isEnabledEntryEventOccurrence, Transition_isEnabledExitEventOccurrence, petrinet_TracedPlace, trace_Events_Place_addTokenExitEventOccurrence, trace_Events_Place_removeTokenEntryEventOccurrence, trace_Events_Net_mainExitEventOccurrence, trace_Events_Net_runEntryEventOccurrence, trace_Events_Net_runExitEventOccurrence, trace_Events_Place_addTokenEntryEventOccurrence, trace_Events_Transition_fireEntryEventOccurrence, trace_Events_Transition_fireExitEventOccurrence, trace_States_Place_tokens_State, trace_Events_Place_removeTokenExitEventOccurrence, trace_Events_Transition_isEnabledEntryEventOccurrence, Events_trace_Transition, trace_Events_Transition_isEnabledExitEventOccurrence, Events_trace_EObject, petrinet_trace_Place, States_trace_GlobalState, trace_Traced_TracedObjects, trace_petrinet_TracedPlace},
    associations={globalTrace0, events1, tracedObjects3, staticObjectsPools5, Net_runEntryEventOccurrence_Trace18, eventsTriggeredDuringState7, Net_runExitEventOccurrence_Trace20, place_tokens_States9, Place_addTokenEntryEventOccurrence_Trace22, Place_addTokenExitEventOccurrence_Trace24, pool_Transitions10, pool_Nets12, stateDuringWhichTriggered14, Net_mainEntryEventOccurrence_Trace15, Net_mainExitEventOccurrence_Trace16, Transition_fireEntryEventOccurrence_Trace34, Transition_fireExitEventOccurrence_Trace36, thisParam38, Place_removeTokenEntryEventOccurrence_Trace26, Place_removeTokenExitEventOccurrence_Trace28, Transition_isEnabledEntryEventOccurrence_Trace30, Transition_isEnabledExitEventOccurrence_Trace32, thisParam45, correspondingEntryEvent46, thisParam48, correspondingEntryEvent39, thisParam41, correspondingEntryEvent43, returnReturn55, thisParam57, correspondingEntryEvent59, correspondingEntryEvent50, thisParam52, correspondingEntryEvent53, originalObject66, tokensTrace67, parent61, globalStates62, petrinet_tracedPlaces64},
    generalizations={gen_trace_Events_Net_mainEntryEventOccurrence_EventOccurrence, gen_trace_Events_Place_addTokenExitEventOccurrence_EventOccurrence, gen_trace_Events_Place_removeTokenEntryEventOccurrence_EventOccurrence, gen_trace_Events_Net_mainExitEventOccurrence_EventOccurrence, gen_trace_Events_Net_runEntryEventOccurrence_EventOccurrence, gen_trace_Events_Net_runExitEventOccurrence_EventOccurrence, gen_trace_Events_Place_addTokenEntryEventOccurrence_EventOccurrence, gen_trace_Events_Transition_fireEntryEventOccurrence_EventOccurrence, gen_trace_Events_Transition_fireExitEventOccurrence_EventOccurrence, gen_trace_Events_Place_removeTokenExitEventOccurrence_EventOccurrence, gen_trace_Events_Transition_isEnabledEntryEventOccurrence_EventOccurrence, gen_trace_Events_Transition_isEnabledExitEventOccurrence_EventOccurrence},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)