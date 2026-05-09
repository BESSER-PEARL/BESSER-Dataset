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
B_b_State = Class(name="B_b_State")
C_c_State = Class(name="C_c_State")
A_a_State = Class(name="A_a_State")
A_doAExitEventOccurrence = Class(name="A_doAExitEventOccurrence")
C_doCEntryEventOccurrence = Class(name="C_doCEntryEventOccurrence")
C_doCExitEventOccurrence = Class(name="C_doCExitEventOccurrence")
trace_Events_A_doAEntryEventOccurrence = Class(name="trace_Events_A_doAEntryEventOccurrence")
model2_TracedA = Class(name="model2_TracedA")
model2Configuration_TracedC = Class(name="model2Configuration_TracedC")
trace_Events_A_doAExitEventOccurrence = Class(name="trace_Events_A_doAExitEventOccurrence")
trace_Events_C_doCEntryEventOccurrence = Class(name="trace_Events_C_doCEntryEventOccurrence")
model2Configuration_TracedB = Class(name="model2Configuration_TracedB")
trace_Events_C_doCExitEventOccurrence = Class(name="trace_Events_C_doCExitEventOccurrence")
trace_States_B_b_State = Class(name="trace_States_B_b_State")
States_trace_GlobalState = Class(name="States_trace_GlobalState")
trace_States_C_c_State = Class(name="trace_States_C_c_State")
States_trace_F = Class(name="States_trace_F")
trace_F = Class(name="trace_F")
trace_Events_EventOccurrence = Class(name="trace_Events_EventOccurrence", is_abstract=True)
Events_trace_GlobalState = Class(name="Events_trace_GlobalState")
trace_Events_Events = Class(name="trace_Events_Events")
A_doAEntryEventOccurrence = Class(name="A_doAEntryEventOccurrence")
trace_model2Configuration_TracedB = Class(name="trace_model2Configuration_TracedB")
trace_model2Configuration_TracedC = Class(name="trace_model2Configuration_TracedC")
trace_model2_TracedA = Class(name="trace_model2_TracedA")
model2_trace_A = Class(name="model2_trace_A")
trace_States_A_a_State = Class(name="trace_States_A_a_State")
trace_Traced_TracedObjects = Class(name="trace_Traced_TracedObjects")

# trace_Trace class attributes and methods

# trace_GlobalState class attributes and methods

# Events class attributes and methods

# TracedObjects class attributes and methods

# trace_StaticObjectsPools class attributes and methods

# EventOccurrence class attributes and methods

# B_b_State class attributes and methods

# C_c_State class attributes and methods

# A_a_State class attributes and methods

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

# trace_F class attributes and methods

# trace_Events_EventOccurrence class attributes and methods

# Events_trace_GlobalState class attributes and methods

# trace_Events_Events class attributes and methods

# A_doAEntryEventOccurrence class attributes and methods

# trace_model2Configuration_TracedB class attributes and methods

# trace_model2Configuration_TracedC class attributes and methods

# trace_model2_TracedA class attributes and methods

# model2_trace_A class attributes and methods

# trace_States_A_a_State class attributes and methods
trace_States_A_a_State_a: Property = Property(name="a", type=IntegerType)
trace_States_A_a_State.attributes={trace_States_A_a_State_a}

# trace_Traced_TracedObjects class attributes and methods

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
b_b_States8: BinaryAssociation = BinaryAssociation(
    name="b_b_States8",
    ends={
        Property(name="B_b_State", type=trace_GlobalState, multiplicity=Multiplicity(1, 1)),
        Property(name="globalStates", type=B_b_State, multiplicity=Multiplicity(0, 9999))
    }
)
c_c_States9: BinaryAssociation = BinaryAssociation(
    name="c_c_States9",
    ends={
        Property(name="C_c_State", type=trace_GlobalState, multiplicity=Multiplicity(1, 1)),
        Property(name="globalStates10", type=C_c_State, multiplicity=Multiplicity(0, 9999))
    }
)
A_doAExitEventOccurrence_Trace17: BinaryAssociation = BinaryAssociation(
    name="A_doAExitEventOccurrence_Trace17",
    ends={
        Property(name="A_doAExitEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events18", type=A_doAExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
C_doCEntryEventOccurrence_Trace19: BinaryAssociation = BinaryAssociation(
    name="C_doCEntryEventOccurrence_Trace19",
    ends={
        Property(name="C_doCEntryEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events20", type=C_doCEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
C_doCExitEventOccurrence_Trace21: BinaryAssociation = BinaryAssociation(
    name="C_doCExitEventOccurrence_Trace21",
    ends={
        Property(name="C_doCExitEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events22", type=C_doCExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
thisParam23: BinaryAssociation = BinaryAssociation(
    name="thisParam23",
    ends={
        Property(name="model2_TracedA", type=trace_Events_A_doAEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_A_doAEntryEventOccurrence", type=model2_TracedA, multiplicity=Multiplicity(0, 1))
    }
)
paramAParam24: BinaryAssociation = BinaryAssociation(
    name="paramAParam24",
    ends={
        Property(name="model2Configuration_TracedC", type=trace_Events_A_doAEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_A_doAEntryEventOccurrence25", type=model2Configuration_TracedC, multiplicity=Multiplicity(1, 1))
    }
)
correspondingEntryEvent26: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent26",
    ends={
        Property(name="A_doAEntryEventOccurrence27", type=trace_Events_A_doAExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_A_doAExitEventOccurrence", type=A_doAEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
thisParam28: BinaryAssociation = BinaryAssociation(
    name="thisParam28",
    ends={
        Property(name="model2Configuration_TracedC29", type=trace_Events_C_doCEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_C_doCEntryEventOccurrence", type=model2Configuration_TracedC, multiplicity=Multiplicity(0, 1))
    }
)
paramCParam30: BinaryAssociation = BinaryAssociation(
    name="paramCParam30",
    ends={
        Property(name="model2Configuration_TracedB", type=trace_Events_C_doCEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_C_doCEntryEventOccurrence31", type=model2Configuration_TracedB, multiplicity=Multiplicity(1, 1))
    }
)
correspondingEntryEvent32: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent32",
    ends={
        Property(name="C_doCEntryEventOccurrence33", type=trace_Events_C_doCExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_C_doCExitEventOccurrence", type=C_doCEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
parent34: BinaryAssociation = BinaryAssociation(
    name="parent34",
    ends={
        Property(name="TracedB", type=trace_States_B_b_State, multiplicity=Multiplicity(1, 1)),
        Property(name="bTrace", type=model2Configuration_TracedB, multiplicity=Multiplicity(1, 1))
    }
)
globalStates35: BinaryAssociation = BinaryAssociation(
    name="globalStates35",
    ends={
        Property(name="GlobalState36", type=trace_States_B_b_State, multiplicity=Multiplicity(1, 1)),
        Property(name="b_b_States", type=States_trace_GlobalState, multiplicity=Multiplicity(1, 9999))
    }
)
c37: BinaryAssociation = BinaryAssociation(
    name="c37",
    ends={
        Property(name="States_trace_F", type=trace_States_C_c_State, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_States_C_c_State", type=States_trace_F, multiplicity=Multiplicity(0, 1))
    }
)
parent38: BinaryAssociation = BinaryAssociation(
    name="parent38",
    ends={
        Property(name="TracedC", type=trace_States_C_c_State, multiplicity=Multiplicity(1, 1)),
        Property(name="cTrace", type=model2Configuration_TracedC, multiplicity=Multiplicity(1, 1))
    }
)
globalStates39: BinaryAssociation = BinaryAssociation(
    name="globalStates39",
    ends={
        Property(name="GlobalState40", type=trace_States_C_c_State, multiplicity=Multiplicity(1, 1)),
        Property(name="c_c_States", type=States_trace_GlobalState, multiplicity=Multiplicity(1, 9999))
    }
)
a_a_States11: BinaryAssociation = BinaryAssociation(
    name="a_a_States11",
    ends={
        Property(name="A_a_State", type=trace_GlobalState, multiplicity=Multiplicity(1, 1)),
        Property(name="globalStates12", type=A_a_State, multiplicity=Multiplicity(0, 9999))
    }
)
pool_Fs13: BinaryAssociation = BinaryAssociation(
    name="pool_Fs13",
    ends={
        Property(name="trace_F", type=trace_StaticObjectsPools, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_StaticObjectsPools14", type=trace_F, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stateDuringWhichTriggered15: BinaryAssociation = BinaryAssociation(
    name="stateDuringWhichTriggered15",
    ends={
        Property(name="GlobalState", type=trace_Events_EventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="eventsTriggeredDuringState", type=Events_trace_GlobalState, multiplicity=Multiplicity(1, 1))
    }
)
A_doAEntryEventOccurrence_Trace16: BinaryAssociation = BinaryAssociation(
    name="A_doAEntryEventOccurrence_Trace16",
    ends={
        Property(name="A_doAEntryEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events", type=A_doAEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
model2Configuration_tracedCs46: BinaryAssociation = BinaryAssociation(
    name="model2Configuration_tracedCs46",
    ends={
        Property(name="model2Configuration_TracedC48", type=trace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Traced_TracedObjects47", type=model2Configuration_TracedC, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
model2_tracedAs49: BinaryAssociation = BinaryAssociation(
    name="model2_tracedAs49",
    ends={
        Property(name="model2_TracedA51", type=trace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Traced_TracedObjects50", type=model2_TracedA, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bTrace52: BinaryAssociation = BinaryAssociation(
    name="bTrace52",
    ends={
        Property(name="B_b_State53", type=trace_model2Configuration_TracedB, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=B_b_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cTrace54: BinaryAssociation = BinaryAssociation(
    name="cTrace54",
    ends={
        Property(name="C_c_State56", type=trace_model2Configuration_TracedC, multiplicity=Multiplicity(1, 1)),
        Property(name="parent55", type=C_c_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
originalObject57: BinaryAssociation = BinaryAssociation(
    name="originalObject57",
    ends={
        Property(name="model2_trace_A", type=trace_model2_TracedA, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_model2_TracedA", type=model2_trace_A, multiplicity=Multiplicity(0, 1))
    }
)
aTrace58: BinaryAssociation = BinaryAssociation(
    name="aTrace58",
    ends={
        Property(name="A_a_State60", type=trace_model2_TracedA, multiplicity=Multiplicity(1, 1)),
        Property(name="parent59", type=A_a_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent41: BinaryAssociation = BinaryAssociation(
    name="parent41",
    ends={
        Property(name="TracedA", type=trace_States_A_a_State, multiplicity=Multiplicity(1, 1)),
        Property(name="aTrace", type=model2_TracedA, multiplicity=Multiplicity(1, 1))
    }
)
globalStates42: BinaryAssociation = BinaryAssociation(
    name="globalStates42",
    ends={
        Property(name="GlobalState43", type=trace_States_A_a_State, multiplicity=Multiplicity(1, 1)),
        Property(name="a_a_States", type=States_trace_GlobalState, multiplicity=Multiplicity(1, 9999))
    }
)
model2Configuration_tracedBs44: BinaryAssociation = BinaryAssociation(
    name="model2Configuration_tracedBs44",
    ends={
        Property(name="model2Configuration_TracedB45", type=trace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Traced_TracedObjects", type=model2Configuration_TracedB, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
    types={trace_Trace, trace_GlobalState, Events, TracedObjects, trace_StaticObjectsPools, EventOccurrence, B_b_State, C_c_State, A_a_State, A_doAExitEventOccurrence, C_doCEntryEventOccurrence, C_doCExitEventOccurrence, trace_Events_A_doAEntryEventOccurrence, model2_TracedA, model2Configuration_TracedC, trace_Events_A_doAExitEventOccurrence, trace_Events_C_doCEntryEventOccurrence, model2Configuration_TracedB, trace_Events_C_doCExitEventOccurrence, trace_States_B_b_State, States_trace_GlobalState, trace_States_C_c_State, States_trace_F, trace_F, trace_Events_EventOccurrence, Events_trace_GlobalState, trace_Events_Events, A_doAEntryEventOccurrence, trace_model2Configuration_TracedB, trace_model2Configuration_TracedC, trace_model2_TracedA, model2_trace_A, trace_States_A_a_State, trace_Traced_TracedObjects},
    associations={globalTrace0, events1, tracedObjects3, staticObjectsPools5, eventsTriggeredDuringState7, b_b_States8, c_c_States9, A_doAExitEventOccurrence_Trace17, C_doCEntryEventOccurrence_Trace19, C_doCExitEventOccurrence_Trace21, thisParam23, paramAParam24, correspondingEntryEvent26, thisParam28, paramCParam30, correspondingEntryEvent32, parent34, globalStates35, c37, parent38, globalStates39, a_a_States11, pool_Fs13, stateDuringWhichTriggered15, A_doAEntryEventOccurrence_Trace16, model2Configuration_tracedCs46, model2_tracedAs49, bTrace52, cTrace54, originalObject57, aTrace58, parent41, globalStates42, model2Configuration_tracedBs44},
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