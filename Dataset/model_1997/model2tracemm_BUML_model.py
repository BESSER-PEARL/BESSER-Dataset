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
A_a_State = Class(name="A::a::State")
trace_Trace = Class(name="trace::Trace")
trace_GlobalState = Class(name="trace::GlobalState")
Events = Class(name="Events")
TracedObjects = Class(name="TracedObjects")
trace_StaticObjectsPools = Class(name="trace::StaticObjectsPools")
EventOccurrence = Class(name="EventOccurrence")
B_b_State = Class(name="B::b::State")
C_c_State = Class(name="C::c::State")
trace_F = Class(name="trace::F")
trace_Events_EventOccurrence = Class(name="trace::Events::EventOccurrence", is_abstract=True)
Events_trace_GlobalState = Class(name="Events::trace::GlobalState")
trace_Events_Events = Class(name="trace::Events::Events")
A_doAEntryEventOccurrence = Class(name="A::doAEntryEventOccurrence")
A_doAExitEventOccurrence = Class(name="A::doAExitEventOccurrence")
C_doCEntryEventOccurrence = Class(name="C::doCEntryEventOccurrence")
C_doCExitEventOccurrence = Class(name="C::doCExitEventOccurrence")
trace_Events_A_doAEntryEventOccurrence = Class(name="trace::Events::A::doAEntryEventOccurrence")
model2_TracedA = Class(name="model2::TracedA")
model2Configuration_TracedC = Class(name="model2Configuration::TracedC")
trace_Events_A_doAExitEventOccurrence = Class(name="trace::Events::A::doAExitEventOccurrence")
trace_Events_C_doCEntryEventOccurrence = Class(name="trace::Events::C::doCEntryEventOccurrence")
model2Configuration_TracedB = Class(name="model2Configuration::TracedB")
trace_Events_C_doCExitEventOccurrence = Class(name="trace::Events::C::doCExitEventOccurrence")
trace_States_B_b_State = Class(name="trace::States::B::b::State")
States_trace_GlobalState = Class(name="States::trace::GlobalState")
trace_States_C_c_State = Class(name="trace::States::C::c::State")
States_trace_F = Class(name="States::trace::F")
trace_States_A_a_State = Class(name="trace::States::A::a::State")
trace_Traced_TracedObjects = Class(name="trace::Traced::TracedObjects")
trace_model2Configuration_TracedB = Class(name="trace::model2Configuration::TracedB")
trace_model2Configuration_TracedC = Class(name="trace::model2Configuration::TracedC")
trace_model2_TracedA = Class(name="trace::model2::TracedA")
model2_trace_A = Class(name="model2::trace::A")

# A_a_State class attributes and methods

# trace_Trace class attributes and methods

# trace_GlobalState class attributes and methods

# Events class attributes and methods

# TracedObjects class attributes and methods

# trace_StaticObjectsPools class attributes and methods

# EventOccurrence class attributes and methods

# B_b_State class attributes and methods

# C_c_State class attributes and methods

# trace_F class attributes and methods

# trace_Events_EventOccurrence class attributes and methods

# Events_trace_GlobalState class attributes and methods

# trace_Events_Events class attributes and methods

# A_doAEntryEventOccurrence class attributes and methods

# A_doAExitEventOccurrence class attributes and methods

# C_doCEntryEventOccurrence class attributes and methods

# C_doCExitEventOccurrence class attributes and methods

# trace_Events_A_doAEntryEventOccurrence class attributes and methods

# model2_TracedA class attributes and methods

# model2Configuration_TracedC class attributes and methods

# trace_Events_A_doAExitEventOccurrence class attributes and methods

# trace_Events_C_doCEntryEventOccurrence class attributes and methods

# model2Configuration_TracedB class attributes and methods

# trace_Events_C_doCExitEventOccurrence class attributes and methods

# trace_States_B_b_State class attributes and methods
trace_States_B_b_State_b: Property = Property(name="b", type=IntegerType)
trace_States_B_b_State.attributes={trace_States_B_b_State_b}

# States_trace_GlobalState class attributes and methods

# trace_States_C_c_State class attributes and methods

# States_trace_F class attributes and methods

# trace_States_A_a_State class attributes and methods
trace_States_A_a_State_a: Property = Property(name="a", type=IntegerType)
trace_States_A_a_State.attributes={trace_States_A_a_State_a}

# trace_Traced_TracedObjects class attributes and methods

# trace_model2Configuration_TracedB class attributes and methods

# trace_model2Configuration_TracedC class attributes and methods

# trace_model2_TracedA class attributes and methods

# model2_trace_A class attributes and methods

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
        Property(name="Events8", type=trace_GlobalState, multiplicity=Multiplicity(1, 1)),
        Property(name="EventOccurrence", type=EventOccurrence, multiplicity=Multiplicity(0, 9999))
    }
)
b_b_States9: BinaryAssociation = BinaryAssociation(
    name="b_b_States9",
    ends={
        Property(name="States", type=trace_GlobalState, multiplicity=Multiplicity(1, 1)),
        Property(name="B_b_State", type=B_b_State, multiplicity=Multiplicity(0, 9999))
    }
)
c_c_States10: BinaryAssociation = BinaryAssociation(
    name="c_c_States10",
    ends={
        Property(name="States11", type=trace_GlobalState, multiplicity=Multiplicity(1, 1)),
        Property(name="C_c_State", type=C_c_State, multiplicity=Multiplicity(0, 9999))
    }
)
parent35: BinaryAssociation = BinaryAssociation(
    name="parent35",
    ends={
        Property(name="Traced", type=trace_States_B_b_State, multiplicity=Multiplicity(1, 1)),
        Property(name="model2Configuration", type=model2Configuration_TracedB, multiplicity=Multiplicity(1, 1))
    }
)
a_a_States12: BinaryAssociation = BinaryAssociation(
    name="a_a_States12",
    ends={
        Property(name="States13", type=trace_GlobalState, multiplicity=Multiplicity(1, 1)),
        Property(name="A_a_State", type=A_a_State, multiplicity=Multiplicity(0, 9999))
    }
)
pool_Fs14: BinaryAssociation = BinaryAssociation(
    name="pool_Fs14",
    ends={
        Property(name="trace_F", type=trace_StaticObjectsPools, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_StaticObjectsPools15", type=trace_F, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stateDuringWhichTriggered16: BinaryAssociation = BinaryAssociation(
    name="stateDuringWhichTriggered16",
    ends={
        Property(name="GlobalState", type=trace_Events_EventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="eventsTriggeredDuringState", type=Events_trace_GlobalState, multiplicity=Multiplicity(1, 1))
    }
)
A_doAEntryEventOccurrence_Trace17: BinaryAssociation = BinaryAssociation(
    name="A_doAEntryEventOccurrence_Trace17",
    ends={
        Property(name="A_doAEntryEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events", type=A_doAEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
A_doAExitEventOccurrence_Trace18: BinaryAssociation = BinaryAssociation(
    name="A_doAExitEventOccurrence_Trace18",
    ends={
        Property(name="A_doAExitEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events19", type=A_doAExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
C_doCEntryEventOccurrence_Trace20: BinaryAssociation = BinaryAssociation(
    name="C_doCEntryEventOccurrence_Trace20",
    ends={
        Property(name="C_doCEntryEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events21", type=C_doCEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
C_doCExitEventOccurrence_Trace22: BinaryAssociation = BinaryAssociation(
    name="C_doCExitEventOccurrence_Trace22",
    ends={
        Property(name="C_doCExitEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events23", type=C_doCExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
thisParam24: BinaryAssociation = BinaryAssociation(
    name="thisParam24",
    ends={
        Property(name="model2_TracedA", type=trace_Events_A_doAEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_A_doAEntryEventOccurrence", type=model2_TracedA, multiplicity=Multiplicity(0, 1))
    }
)
paramAParam25: BinaryAssociation = BinaryAssociation(
    name="paramAParam25",
    ends={
        Property(name="model2Configuration_TracedC", type=trace_Events_A_doAEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_A_doAEntryEventOccurrence26", type=model2Configuration_TracedC, multiplicity=Multiplicity(1, 1))
    }
)
correspondingEntryEvent27: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent27",
    ends={
        Property(name="A_doAEntryEventOccurrence28", type=trace_Events_A_doAExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_A_doAExitEventOccurrence", type=A_doAEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
thisParam29: BinaryAssociation = BinaryAssociation(
    name="thisParam29",
    ends={
        Property(name="model2Configuration_TracedC30", type=trace_Events_C_doCEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_C_doCEntryEventOccurrence", type=model2Configuration_TracedC, multiplicity=Multiplicity(0, 1))
    }
)
paramCParam31: BinaryAssociation = BinaryAssociation(
    name="paramCParam31",
    ends={
        Property(name="model2Configuration_TracedB", type=trace_Events_C_doCEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_C_doCEntryEventOccurrence32", type=model2Configuration_TracedB, multiplicity=Multiplicity(1, 1))
    }
)
correspondingEntryEvent33: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent33",
    ends={
        Property(name="C_doCEntryEventOccurrence34", type=trace_Events_C_doCExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_C_doCExitEventOccurrence", type=C_doCEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
globalStates36: BinaryAssociation = BinaryAssociation(
    name="globalStates36",
    ends={
        Property(name="GlobalState37", type=trace_States_B_b_State, multiplicity=Multiplicity(1, 1)),
        Property(name="b_b_States", type=States_trace_GlobalState, multiplicity=Multiplicity(1, 9999))
    }
)
c38: BinaryAssociation = BinaryAssociation(
    name="c38",
    ends={
        Property(name="States_trace_F", type=trace_States_C_c_State, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_States_C_c_State", type=States_trace_F, multiplicity=Multiplicity(0, 1))
    }
)
parent39: BinaryAssociation = BinaryAssociation(
    name="parent39",
    ends={
        Property(name="Traced41", type=trace_States_C_c_State, multiplicity=Multiplicity(1, 1)),
        Property(name="model2Configuration40", type=model2Configuration_TracedC, multiplicity=Multiplicity(1, 1))
    }
)
globalStates42: BinaryAssociation = BinaryAssociation(
    name="globalStates42",
    ends={
        Property(name="GlobalState43", type=trace_States_C_c_State, multiplicity=Multiplicity(1, 1)),
        Property(name="c_c_States", type=States_trace_GlobalState, multiplicity=Multiplicity(1, 9999))
    }
)
parent44: BinaryAssociation = BinaryAssociation(
    name="parent44",
    ends={
        Property(name="Traced45", type=trace_States_A_a_State, multiplicity=Multiplicity(1, 1)),
        Property(name="model2", type=model2_TracedA, multiplicity=Multiplicity(1, 1))
    }
)
globalStates46: BinaryAssociation = BinaryAssociation(
    name="globalStates46",
    ends={
        Property(name="GlobalState47", type=trace_States_A_a_State, multiplicity=Multiplicity(1, 1)),
        Property(name="a_a_States", type=States_trace_GlobalState, multiplicity=Multiplicity(1, 9999))
    }
)
model2Configuration_tracedBs48: BinaryAssociation = BinaryAssociation(
    name="model2Configuration_tracedBs48",
    ends={
        Property(name="model2Configuration_TracedB49", type=trace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Traced_TracedObjects", type=model2Configuration_TracedB, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
model2Configuration_tracedCs50: BinaryAssociation = BinaryAssociation(
    name="model2Configuration_tracedCs50",
    ends={
        Property(name="model2Configuration_TracedC52", type=trace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Traced_TracedObjects51", type=model2Configuration_TracedC, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
model2_tracedAs53: BinaryAssociation = BinaryAssociation(
    name="model2_tracedAs53",
    ends={
        Property(name="model2_TracedA55", type=trace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Traced_TracedObjects54", type=model2_TracedA, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bTrace56: BinaryAssociation = BinaryAssociation(
    name="bTrace56",
    ends={
        Property(name="States58", type=trace_model2Configuration_TracedB, multiplicity=Multiplicity(1, 1)),
        Property(name="B_b_State57", type=B_b_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cTrace59: BinaryAssociation = BinaryAssociation(
    name="cTrace59",
    ends={
        Property(name="States61", type=trace_model2Configuration_TracedC, multiplicity=Multiplicity(1, 1)),
        Property(name="C_c_State60", type=C_c_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
originalObject62: BinaryAssociation = BinaryAssociation(
    name="originalObject62",
    ends={
        Property(name="model2_trace_A", type=trace_model2_TracedA, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_model2_TracedA", type=model2_trace_A, multiplicity=Multiplicity(0, 1))
    }
)
aTrace63: BinaryAssociation = BinaryAssociation(
    name="aTrace63",
    ends={
        Property(name="States65", type=trace_model2_TracedA, multiplicity=Multiplicity(1, 1)),
        Property(name="A_a_State64", type=A_a_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_trace_Events_A_doAEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_A_doAEntryEventOccurrence)
gen_trace_Events_A_doAExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_A_doAExitEventOccurrence)
gen_trace_Events_C_doCEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_C_doCEntryEventOccurrence)
gen_trace_Events_C_doCExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_C_doCExitEventOccurrence)

# Domain Model
domain_model = DomainModel(
    name="trace",
    types={A_a_State, trace_Trace, trace_GlobalState, Events, TracedObjects, trace_StaticObjectsPools, EventOccurrence, B_b_State, C_c_State, trace_F, trace_Events_EventOccurrence, Events_trace_GlobalState, trace_Events_Events, A_doAEntryEventOccurrence, A_doAExitEventOccurrence, C_doCEntryEventOccurrence, C_doCExitEventOccurrence, trace_Events_A_doAEntryEventOccurrence, model2_TracedA, model2Configuration_TracedC, trace_Events_A_doAExitEventOccurrence, trace_Events_C_doCEntryEventOccurrence, model2Configuration_TracedB, trace_Events_C_doCExitEventOccurrence, trace_States_B_b_State, States_trace_GlobalState, trace_States_C_c_State, States_trace_F, trace_States_A_a_State, trace_Traced_TracedObjects, trace_model2Configuration_TracedB, trace_model2Configuration_TracedC, trace_model2_TracedA, model2_trace_A},
    associations={globalTrace0, events1, tracedObjects3, staticObjectsPools5, eventsTriggeredDuringState7, b_b_States9, c_c_States10, parent35, a_a_States12, pool_Fs14, stateDuringWhichTriggered16, A_doAEntryEventOccurrence_Trace17, A_doAExitEventOccurrence_Trace18, C_doCEntryEventOccurrence_Trace20, C_doCExitEventOccurrence_Trace22, thisParam24, paramAParam25, correspondingEntryEvent27, thisParam29, paramCParam31, correspondingEntryEvent33, globalStates36, c38, parent39, globalStates42, parent44, globalStates46, model2Configuration_tracedBs48, model2Configuration_tracedCs50, model2_tracedAs53, bTrace56, cTrace59, originalObject62, aTrace63},
    generalizations={gen_trace_Events_A_doAEntryEventOccurrence_EventOccurrence, gen_trace_Events_A_doAExitEventOccurrence_EventOccurrence, gen_trace_Events_C_doCEntryEventOccurrence_EventOccurrence, gen_trace_Events_C_doCExitEventOccurrence_EventOccurrence},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)