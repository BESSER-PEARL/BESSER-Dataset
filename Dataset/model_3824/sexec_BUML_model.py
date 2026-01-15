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
ExecutionNode = Class(name="ExecutionNode")
sexec_ExecutionState = Class(name="sexec::ExecutionState")
sexec_MappedElement = Class(name="sexec::MappedElement")
sexec_EObject = Class(name="sexec::EObject")
sexec_ExecutionFlow = Class(name="sexec::ExecutionFlow")
ScopedElement = Class(name="ScopedElement")
ExecutionScope = Class(name="ExecutionScope")
sexec_ExecutionNode = Class(name="sexec::ExecutionNode")
sexec_ExecutionRegion = Class(name="sexec::ExecutionRegion")
sexec_StateVector = Class(name="sexec::StateVector")
sexec_Step = Class(name="sexec::Step", is_abstract=True)
MappedElement = Class(name="MappedElement")
NamedElement = Class(name="NamedElement")
sexec_ExecutionExit = Class(name="sexec::ExecutionExit")
sexec_ExecutionChoice = Class(name="sexec::ExecutionChoice")
sexec_ExecutionScope = Class(name="sexec::ExecutionScope")
sexec_ExecutionEntry = Class(name="sexec::ExecutionEntry")
sexec_Execution = Class(name="sexec::Execution")
sexec_ExecutionSynchronization = Class(name="sexec::ExecutionSynchronization")
sexec_TimeEvent = Class(name="sexec::TimeEvent")
Event = Class(name="Event")
sexec_Check = Class(name="sexec::Check")
Step = Class(name="Step")
sexec_Expression = Class(name="sexec::Expression")
sexec_CheckRef = Class(name="sexec::CheckRef")
Check = Class(name="Check")
sexec_StateCase = Class(name="sexec::StateCase")
sexec_EnterState = Class(name="sexec::EnterState")
sexec_ExitState = Class(name="sexec::ExitState")
sexec_Call = Class(name="sexec::Call")
sexec_ScheduleTimeEvent = Class(name="sexec::ScheduleTimeEvent")
sexec_UnscheduleTimeEvent = Class(name="sexec::UnscheduleTimeEvent")
sexec_StateSwitch = Class(name="sexec::StateSwitch")
sexec_SaveHistory = Class(name="sexec::SaveHistory")
sexec_HistoryEntry = Class(name="sexec::HistoryEntry")
sexec_TraceBeginRunCycle = Class(name="sexec::TraceBeginRunCycle")
sexec_TraceEndRunCycle = Class(name="sexec::TraceEndRunCycle")
sexec_Trace = Class(name="sexec::Trace", is_abstract=True)
sexec_TraceNodeExecuted = Class(name="sexec::TraceNodeExecuted")
Trace = Class(name="Trace")
sexec_ReactionFired = Class(name="sexec::ReactionFired")
sexec_TraceReactionWillFire = Class(name="sexec::TraceReactionWillFire")
sexec_TraceStateEntered = Class(name="sexec::TraceStateEntered")
sexec_TraceStateExited = Class(name="sexec::TraceStateExited")

# ExecutionNode class attributes and methods

# sexec_ExecutionState class attributes and methods
sexec_ExecutionState_leaf: Property = Property(name="leaf", type=BooleanType)
sexec_ExecutionState.attributes={sexec_ExecutionState_leaf}

# sexec_MappedElement class attributes and methods

# sexec_EObject class attributes and methods

# sexec_ExecutionFlow class attributes and methods

# ScopedElement class attributes and methods

# ExecutionScope class attributes and methods

# sexec_ExecutionNode class attributes and methods
sexec_ExecutionNode_simpleName: Property = Property(name="simpleName", type=StringType)
sexec_ExecutionNode.attributes={sexec_ExecutionNode_simpleName}

# sexec_ExecutionRegion class attributes and methods

# sexec_StateVector class attributes and methods
sexec_StateVector_size: Property = Property(name="size", type=IntegerType)
sexec_StateVector_offset: Property = Property(name="offset", type=IntegerType)
sexec_StateVector.attributes={sexec_StateVector_offset, sexec_StateVector_size}

# sexec_Step class attributes and methods
sexec_Step_comment: Property = Property(name="comment", type=StringType)
sexec_Step.attributes={sexec_Step_comment}

# MappedElement class attributes and methods

# NamedElement class attributes and methods

# sexec_ExecutionExit class attributes and methods

# sexec_ExecutionChoice class attributes and methods

# sexec_ExecutionScope class attributes and methods

# sexec_ExecutionEntry class attributes and methods

# sexec_Execution class attributes and methods

# sexec_ExecutionSynchronization class attributes and methods

# sexec_TimeEvent class attributes and methods
sexec_TimeEvent_periodic: Property = Property(name="periodic", type=BooleanType)
sexec_TimeEvent.attributes={sexec_TimeEvent_periodic}

# Event class attributes and methods

# sexec_Check class attributes and methods

# Step class attributes and methods

# sexec_Expression class attributes and methods

# sexec_CheckRef class attributes and methods

# Check class attributes and methods

# sexec_StateCase class attributes and methods

# sexec_EnterState class attributes and methods

# sexec_ExitState class attributes and methods

# sexec_Call class attributes and methods

# sexec_ScheduleTimeEvent class attributes and methods

# sexec_UnscheduleTimeEvent class attributes and methods

# sexec_StateSwitch class attributes and methods
sexec_StateSwitch_stateConfigurationIdx: Property = Property(name="stateConfigurationIdx", type=IntegerType)
sexec_StateSwitch.attributes={sexec_StateSwitch_stateConfigurationIdx}

# sexec_SaveHistory class attributes and methods
sexec_SaveHistory_deep: Property = Property(name="deep", type=BooleanType)
sexec_SaveHistory.attributes={sexec_SaveHistory_deep}

# sexec_HistoryEntry class attributes and methods
sexec_HistoryEntry_deep: Property = Property(name="deep", type=BooleanType)
sexec_HistoryEntry.attributes={sexec_HistoryEntry_deep}

# sexec_TraceBeginRunCycle class attributes and methods

# sexec_TraceEndRunCycle class attributes and methods

# sexec_Trace class attributes and methods

# sexec_TraceNodeExecuted class attributes and methods

# Trace class attributes and methods

# sexec_ReactionFired class attributes and methods

# sexec_TraceReactionWillFire class attributes and methods

# sexec_TraceStateEntered class attributes and methods

# sexec_TraceStateExited class attributes and methods

# Relationships
sourceElement0: BinaryAssociation = BinaryAssociation(
    name="sourceElement0",
    ends={
        Property(name="sexec_EObject", type=sexec_MappedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="sexec_MappedElement", type=sexec_EObject, multiplicity=Multiplicity(0, 1))
    }
)
states1: BinaryAssociation = BinaryAssociation(
    name="states1",
    ends={
        Property(name="sexec_ExecutionState", type=sexec_ExecutionFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="sexec_ExecutionFlow", type=sexec_ExecutionState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nodes2: BinaryAssociation = BinaryAssociation(
    name="nodes2",
    ends={
        Property(name="sexec_ExecutionNode", type=sexec_ExecutionFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="sexec_ExecutionFlow3", type=sexec_ExecutionNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
regions4: BinaryAssociation = BinaryAssociation(
    name="regions4",
    ends={
        Property(name="sexec_ExecutionRegion", type=sexec_ExecutionFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="sexec_ExecutionFlow5", type=sexec_ExecutionRegion, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
historyVector6: BinaryAssociation = BinaryAssociation(
    name="historyVector6",
    ends={
        Property(name="sexec_StateVector", type=sexec_ExecutionFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="sexec_ExecutionFlow7", type=sexec_StateVector, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entryAction8: BinaryAssociation = BinaryAssociation(
    name="entryAction8",
    ends={
        Property(name="sexec_Step", type=sexec_ExecutionFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="sexec_ExecutionFlow9", type=sexec_Step, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exitAction10: BinaryAssociation = BinaryAssociation(
    name="exitAction10",
    ends={
        Property(name="sexec_Step12", type=sexec_ExecutionFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="sexec_ExecutionFlow11", type=sexec_Step, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entryAction13: BinaryAssociation = BinaryAssociation(
    name="entryAction13",
    ends={
        Property(name="sexec_Step15", type=sexec_ExecutionState, multiplicity=Multiplicity(1, 1)),
        Property(name="sexec_ExecutionState14", type=sexec_Step, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exitAction16: BinaryAssociation = BinaryAssociation(
    name="exitAction16",
    ends={
        Property(name="sexec_Step18", type=sexec_ExecutionState, multiplicity=Multiplicity(1, 1)),
        Property(name="sexec_ExecutionState17", type=sexec_Step, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
stateVector19: BinaryAssociation = BinaryAssociation(
    name="stateVector19",
    ends={
        Property(name="sexec_StateVector20", type=sexec_ExecutionScope, multiplicity=Multiplicity(1, 1)),
        Property(name="sexec_ExecutionScope", type=sexec_StateVector, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subScopes22: BinaryAssociation = BinaryAssociation(
    name="subScopes22",
    ends={
        Property(name="ExecutionScope", type=sexec_ExecutionScope, multiplicity=Multiplicity(1, 1)),
        Property(name="superScope", type=sexec_ExecutionScope, multiplicity=Multiplicity(0, 9999))
    }
)
superScope24: BinaryAssociation = BinaryAssociation(
    name="superScope24",
    ends={
        Property(name="ExecutionScope25", type=sexec_ExecutionScope, multiplicity=Multiplicity(1, 1)),
        Property(name="subScopes", type=sexec_ExecutionScope, multiplicity=Multiplicity(0, 1))
    }
)
historyVector26: BinaryAssociation = BinaryAssociation(
    name="historyVector26",
    ends={
        Property(name="sexec_StateVector28", type=sexec_ExecutionRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="sexec_ExecutionRegion27", type=sexec_StateVector, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nodes29: BinaryAssociation = BinaryAssociation(
    name="nodes29",
    ends={
        Property(name="sexec_ExecutionNode31", type=sexec_ExecutionRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="sexec_ExecutionRegion30", type=sexec_ExecutionNode, multiplicity=Multiplicity(0, 9999))
    }
)
condition32: BinaryAssociation = BinaryAssociation(
    name="condition32",
    ends={
        Property(name="sexec_Expression", type=sexec_Check, multiplicity=Multiplicity(1, 1)),
        Property(name="sexec_Check", type=sexec_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
refs33: BinaryAssociation = BinaryAssociation(
    name="refs33",
    ends={
        Property(name="CheckRef", type=sexec_Check, multiplicity=Multiplicity(1, 1)),
        Property(name="check", type=sexec_CheckRef, multiplicity=Multiplicity(0, 9999))
    }
)
check34: BinaryAssociation = BinaryAssociation(
    name="check34",
    ends={
        Property(name="Check", type=sexec_CheckRef, multiplicity=Multiplicity(1, 1)),
        Property(name="refs", type=sexec_Check, multiplicity=Multiplicity(0, 1))
    }
)
cases47: BinaryAssociation = BinaryAssociation(
    name="cases47",
    ends={
        Property(name="sexec_StateCase", type=sexec_StateSwitch, multiplicity=Multiplicity(1, 1)),
        Property(name="sexec_StateSwitch", type=sexec_StateCase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statement35: BinaryAssociation = BinaryAssociation(
    name="statement35",
    ends={
        Property(name="sexec_Expression36", type=sexec_Execution, multiplicity=Multiplicity(1, 1)),
        Property(name="sexec_Execution", type=sexec_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
state37: BinaryAssociation = BinaryAssociation(
    name="state37",
    ends={
        Property(name="sexec_ExecutionState38", type=sexec_EnterState, multiplicity=Multiplicity(1, 1)),
        Property(name="sexec_EnterState", type=sexec_ExecutionState, multiplicity=Multiplicity(0, 1))
    }
)
state39: BinaryAssociation = BinaryAssociation(
    name="state39",
    ends={
        Property(name="sexec_ExecutionState40", type=sexec_ExitState, multiplicity=Multiplicity(1, 1)),
        Property(name="sexec_ExitState", type=sexec_ExecutionState, multiplicity=Multiplicity(0, 1))
    }
)
timeEvent41: BinaryAssociation = BinaryAssociation(
    name="timeEvent41",
    ends={
        Property(name="sexec_TimeEvent", type=sexec_ScheduleTimeEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="sexec_ScheduleTimeEvent", type=sexec_TimeEvent, multiplicity=Multiplicity(0, 1))
    }
)
timeValue42: BinaryAssociation = BinaryAssociation(
    name="timeValue42",
    ends={
        Property(name="sexec_Expression44", type=sexec_ScheduleTimeEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="sexec_ScheduleTimeEvent43", type=sexec_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
timeEvent45: BinaryAssociation = BinaryAssociation(
    name="timeEvent45",
    ends={
        Property(name="sexec_TimeEvent46", type=sexec_UnscheduleTimeEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="sexec_UnscheduleTimeEvent", type=sexec_TimeEvent, multiplicity=Multiplicity(0, 1))
    }
)
historyStep64: BinaryAssociation = BinaryAssociation(
    name="historyStep64",
    ends={
        Property(name="sexec_Step66", type=sexec_HistoryEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="sexec_HistoryEntry65", type=sexec_Step, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
historyRegion48: BinaryAssociation = BinaryAssociation(
    name="historyRegion48",
    ends={
        Property(name="sexec_ExecutionRegion50", type=sexec_StateSwitch, multiplicity=Multiplicity(1, 1)),
        Property(name="sexec_StateSwitch49", type=sexec_ExecutionRegion, multiplicity=Multiplicity(0, 1))
    }
)
state51: BinaryAssociation = BinaryAssociation(
    name="state51",
    ends={
        Property(name="sexec_ExecutionState53", type=sexec_StateCase, multiplicity=Multiplicity(1, 1)),
        Property(name="sexec_StateCase52", type=sexec_ExecutionState, multiplicity=Multiplicity(0, 1))
    }
)
step54: BinaryAssociation = BinaryAssociation(
    name="step54",
    ends={
        Property(name="sexec_Step56", type=sexec_StateCase, multiplicity=Multiplicity(1, 1)),
        Property(name="sexec_StateCase55", type=sexec_Step, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
region57: BinaryAssociation = BinaryAssociation(
    name="region57",
    ends={
        Property(name="sexec_ExecutionRegion58", type=sexec_SaveHistory, multiplicity=Multiplicity(1, 1)),
        Property(name="sexec_SaveHistory", type=sexec_ExecutionRegion, multiplicity=Multiplicity(0, 1))
    }
)
initialStep59: BinaryAssociation = BinaryAssociation(
    name="initialStep59",
    ends={
        Property(name="sexec_Step60", type=sexec_HistoryEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="sexec_HistoryEntry", type=sexec_Step, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
region61: BinaryAssociation = BinaryAssociation(
    name="region61",
    ends={
        Property(name="sexec_ExecutionRegion63", type=sexec_HistoryEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="sexec_HistoryEntry62", type=sexec_ExecutionRegion, multiplicity=Multiplicity(0, 1))
    }
)
node67: BinaryAssociation = BinaryAssociation(
    name="node67",
    ends={
        Property(name="sexec_ExecutionNode68", type=sexec_TraceNodeExecuted, multiplicity=Multiplicity(1, 1)),
        Property(name="sexec_TraceNodeExecuted", type=sexec_ExecutionNode, multiplicity=Multiplicity(0, 1))
    }
)
state69: BinaryAssociation = BinaryAssociation(
    name="state69",
    ends={
        Property(name="sexec_ExecutionState70", type=sexec_TraceStateEntered, multiplicity=Multiplicity(1, 1)),
        Property(name="sexec_TraceStateEntered", type=sexec_ExecutionState, multiplicity=Multiplicity(0, 1))
    }
)
state71: BinaryAssociation = BinaryAssociation(
    name="state71",
    ends={
        Property(name="sexec_ExecutionState72", type=sexec_TraceStateExited, multiplicity=Multiplicity(1, 1)),
        Property(name="sexec_TraceStateExited", type=sexec_ExecutionState, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_sexec_ExecutionFlow_ExecutionScope = Generalization(general=ExecutionScope, specific=sexec_ExecutionFlow)
gen_sexec_ExecutionFlow_ExecutionNode = Generalization(general=ExecutionNode, specific=sexec_ExecutionFlow)
gen_sexec_ExecutionFlow_ScopedElement = Generalization(general=ScopedElement, specific=sexec_ExecutionFlow)
gen_sexec_ExecutionNode_MappedElement = Generalization(general=MappedElement, specific=sexec_ExecutionNode)
gen_sexec_ExecutionNode_NamedElement = Generalization(general=NamedElement, specific=sexec_ExecutionNode)
gen_sexec_ExecutionState_ExecutionNode = Generalization(general=ExecutionNode, specific=sexec_ExecutionState)
gen_sexec_ExecutionState_ExecutionScope = Generalization(general=ExecutionScope, specific=sexec_ExecutionState)
gen_sexec_ExecutionExit_ExecutionNode = Generalization(general=ExecutionNode, specific=sexec_ExecutionExit)
gen_sexec_ExecutionScope_MappedElement = Generalization(general=MappedElement, specific=sexec_ExecutionScope)
gen_sexec_ExecutionScope_NamedElement = Generalization(general=NamedElement, specific=sexec_ExecutionScope)
gen_sexec_ExecutionRegion_ExecutionScope = Generalization(general=ExecutionScope, specific=sexec_ExecutionRegion)
gen_sexec_ExecutionEntry_ExecutionNode = Generalization(general=ExecutionNode, specific=sexec_ExecutionEntry)
gen_sexec_Execution_Step = Generalization(general=Step, specific=sexec_Execution)
gen_sexec_ExecutionChoice_ExecutionNode = Generalization(general=ExecutionNode, specific=sexec_ExecutionChoice)
gen_sexec_ExecutionSynchronization_ExecutionNode = Generalization(general=ExecutionNode, specific=sexec_ExecutionSynchronization)
gen_sexec_TimeEvent_Event = Generalization(general=Event, specific=sexec_TimeEvent)
gen_sexec_Step_NamedElement = Generalization(general=NamedElement, specific=sexec_Step)
gen_sexec_Check_Step = Generalization(general=Step, specific=sexec_Check)
gen_sexec_CheckRef_Check = Generalization(general=Check, specific=sexec_CheckRef)
gen_sexec_StateSwitch_Step = Generalization(general=Step, specific=sexec_StateSwitch)
gen_sexec_EnterState_Step = Generalization(general=Step, specific=sexec_EnterState)
gen_sexec_ExitState_Step = Generalization(general=Step, specific=sexec_ExitState)
gen_sexec_Call_Step = Generalization(general=Step, specific=sexec_Call)
gen_sexec_ScheduleTimeEvent_Step = Generalization(general=Step, specific=sexec_ScheduleTimeEvent)
gen_sexec_UnscheduleTimeEvent_Step = Generalization(general=Step, specific=sexec_UnscheduleTimeEvent)
gen_sexec_SaveHistory_Step = Generalization(general=Step, specific=sexec_SaveHistory)
gen_sexec_HistoryEntry_Step = Generalization(general=Step, specific=sexec_HistoryEntry)
gen_sexec_TraceBeginRunCycle_Trace = Generalization(general=Trace, specific=sexec_TraceBeginRunCycle)
gen_sexec_TraceEndRunCycle_Trace = Generalization(general=Trace, specific=sexec_TraceEndRunCycle)
gen_sexec_Trace_Step = Generalization(general=Step, specific=sexec_Trace)
gen_sexec_TraceNodeExecuted_Trace = Generalization(general=Trace, specific=sexec_TraceNodeExecuted)
gen_sexec_ReactionFired_Trace = Generalization(general=Trace, specific=sexec_ReactionFired)
gen_sexec_TraceReactionWillFire_Trace = Generalization(general=Trace, specific=sexec_TraceReactionWillFire)
gen_sexec_TraceStateEntered_Trace = Generalization(general=Trace, specific=sexec_TraceStateEntered)
gen_sexec_TraceStateExited_Trace = Generalization(general=Trace, specific=sexec_TraceStateExited)

# Domain Model
domain_model = DomainModel(
    name="sexec",
    types={ExecutionNode, sexec_ExecutionState, sexec_MappedElement, sexec_EObject, sexec_ExecutionFlow, ScopedElement, ExecutionScope, sexec_ExecutionNode, sexec_ExecutionRegion, sexec_StateVector, sexec_Step, MappedElement, NamedElement, sexec_ExecutionExit, sexec_ExecutionChoice, sexec_ExecutionScope, sexec_ExecutionEntry, sexec_Execution, sexec_ExecutionSynchronization, sexec_TimeEvent, Event, sexec_Check, Step, sexec_Expression, sexec_CheckRef, Check, sexec_StateCase, sexec_EnterState, sexec_ExitState, sexec_Call, sexec_ScheduleTimeEvent, sexec_UnscheduleTimeEvent, sexec_StateSwitch, sexec_SaveHistory, sexec_HistoryEntry, sexec_TraceBeginRunCycle, sexec_TraceEndRunCycle, sexec_Trace, sexec_TraceNodeExecuted, Trace, sexec_ReactionFired, sexec_TraceReactionWillFire, sexec_TraceStateEntered, sexec_TraceStateExited},
    associations={sourceElement0, states1, nodes2, regions4, historyVector6, entryAction8, exitAction10, entryAction13, exitAction16, stateVector19, subScopes22, superScope24, historyVector26, nodes29, condition32, refs33, check34, cases47, statement35, state37, state39, timeEvent41, timeValue42, timeEvent45, historyStep64, historyRegion48, state51, step54, region57, initialStep59, region61, node67, state69, state71},
    generalizations={gen_sexec_ExecutionFlow_ExecutionScope, gen_sexec_ExecutionFlow_ExecutionNode, gen_sexec_ExecutionFlow_ScopedElement, gen_sexec_ExecutionNode_MappedElement, gen_sexec_ExecutionNode_NamedElement, gen_sexec_ExecutionState_ExecutionNode, gen_sexec_ExecutionState_ExecutionScope, gen_sexec_ExecutionExit_ExecutionNode, gen_sexec_ExecutionScope_MappedElement, gen_sexec_ExecutionScope_NamedElement, gen_sexec_ExecutionRegion_ExecutionScope, gen_sexec_ExecutionEntry_ExecutionNode, gen_sexec_Execution_Step, gen_sexec_ExecutionChoice_ExecutionNode, gen_sexec_ExecutionSynchronization_ExecutionNode, gen_sexec_TimeEvent_Event, gen_sexec_Step_NamedElement, gen_sexec_Check_Step, gen_sexec_CheckRef_Check, gen_sexec_StateSwitch_Step, gen_sexec_EnterState_Step, gen_sexec_ExitState_Step, gen_sexec_Call_Step, gen_sexec_ScheduleTimeEvent_Step, gen_sexec_UnscheduleTimeEvent_Step, gen_sexec_SaveHistory_Step, gen_sexec_HistoryEntry_Step, gen_sexec_TraceBeginRunCycle_Trace, gen_sexec_TraceEndRunCycle_Trace, gen_sexec_Trace_Step, gen_sexec_TraceNodeExecuted_Trace, gen_sexec_ReactionFired_Trace, gen_sexec_TraceReactionWillFire_Trace, gen_sexec_TraceStateEntered_Trace, gen_sexec_TraceStateExited_Trace},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)