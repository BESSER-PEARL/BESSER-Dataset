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
scxml_NamedElement = Class(name="scxml::NamedElement")
scxml_DataModel = Class(name="scxml::DataModel")
scxml_Transition = Class(name="scxml::Transition")
scxml_State = Class(name="scxml::State")
NamedElement = Class(name="NamedElement")
scxml_OnEntry = Class(name="scxml::OnEntry")
scxml_OnExit = Class(name="scxml::OnExit")
scxml_InitialState = Class(name="scxml::InitialState")
scxml_FinalState = Class(name="scxml::FinalState")
scxml_Parallel = Class(name="scxml::Parallel")
scxml_Anchor = Class(name="scxml::Anchor")
scxml_Invoke = Class(name="scxml::Invoke")
scxml_HistoryState = Class(name="scxml::HistoryState")
scxml_Assign = Class(name="scxml::Assign")
scxml_ServiceTemplate = Class(name="scxml::ServiceTemplate")
scxml_Script = Class(name="scxml::Script")
scxml_Cancel = Class(name="scxml::Cancel")
scxml_If = Class(name="scxml::If")
scxml_Log = Class(name="scxml::Log")
scxml_Param = Class(name="scxml::Param")
scxml_Raise = Class(name="scxml::Raise")
scxml_Send = Class(name="scxml::Send")
scxml_Validate = Class(name="scxml::Validate")
scxml_Donedata = Class(name="scxml::Donedata")
scxml_ElseIf = Class(name="scxml::ElseIf")
scxml_Else = Class(name="scxml::Else")
scxml_Data = Class(name="scxml::Data")
scxml_Content = Class(name="scxml::Content")
scxml_Finalize = Class(name="scxml::Finalize")

# scxml_NamedElement class attributes and methods

# scxml_DataModel class attributes and methods
scxml_DataModel_schema: Property = Property(name="schema", type=StringType)
scxml_DataModel.attributes={scxml_DataModel_schema}

# scxml_Transition class attributes and methods
scxml_Transition_event: Property = Property(name="event", type=StringType)
scxml_Transition_cond: Property = Property(name="cond", type=StringType)
scxml_Transition_anchor: Property = Property(name="anchor", type=StringType)
scxml_Transition.attributes={scxml_Transition_cond, scxml_Transition_anchor, scxml_Transition_event}

# scxml_State class attributes and methods
scxml_State_id: Property = Property(name="id", type=StringType)
scxml_State.attributes={scxml_State_id}

# NamedElement class attributes and methods

# scxml_OnEntry class attributes and methods

# scxml_OnExit class attributes and methods

# scxml_InitialState class attributes and methods

# scxml_FinalState class attributes and methods
scxml_FinalState_id: Property = Property(name="id", type=StringType)
scxml_FinalState.attributes={scxml_FinalState_id}

# scxml_Parallel class attributes and methods
scxml_Parallel_id: Property = Property(name="id", type=StringType)
scxml_Parallel.attributes={scxml_Parallel_id}

# scxml_Anchor class attributes and methods
scxml_Anchor_type: Property = Property(name="type", type=StringType)
scxml_Anchor_snapshot: Property = Property(name="snapshot", type=StringType)
scxml_Anchor.attributes={scxml_Anchor_type, scxml_Anchor_snapshot}

# scxml_Invoke class attributes and methods
scxml_Invoke_type: Property = Property(name="type", type=StringType)
scxml_Invoke_typeexpr: Property = Property(name="typeexpr", type=StringType)
scxml_Invoke_src: Property = Property(name="src", type=StringType)
scxml_Invoke_srcexpr: Property = Property(name="srcexpr", type=StringType)
scxml_Invoke_id: Property = Property(name="id", type=StringType)
scxml_Invoke_idlocation: Property = Property(name="idlocation", type=StringType)
scxml_Invoke_namelist: Property = Property(name="namelist", type=StringType)
scxml_Invoke_autoforward: Property = Property(name="autoforward", type=StringType)
scxml_Invoke.attributes={scxml_Invoke_idlocation, scxml_Invoke_srcexpr, scxml_Invoke_typeexpr, scxml_Invoke_type, scxml_Invoke_namelist, scxml_Invoke_autoforward, scxml_Invoke_id, scxml_Invoke_src}

# scxml_HistoryState class attributes and methods
scxml_HistoryState_id: Property = Property(name="id", type=StringType)
scxml_HistoryState_type: Property = Property(name="type", type=StringType)
scxml_HistoryState.attributes={scxml_HistoryState_id, scxml_HistoryState_type}

# scxml_Assign class attributes and methods
scxml_Assign_location: Property = Property(name="location", type=StringType)
scxml_Assign_dataid: Property = Property(name="dataid", type=StringType)
scxml_Assign_expr: Property = Property(name="expr", type=StringType)
scxml_Assign.attributes={scxml_Assign_expr, scxml_Assign_location, scxml_Assign_dataid}

# scxml_ServiceTemplate class attributes and methods
scxml_ServiceTemplate_name: Property = Property(name="name", type=StringType)
scxml_ServiceTemplate_xmlns: Property = Property(name="xmlns", type=StringType)
scxml_ServiceTemplate_version: Property = Property(name="version", type=StringType)
scxml_ServiceTemplate_profile: Property = Property(name="profile", type=StringType)
scxml_ServiceTemplate_exmode: Property = Property(name="exmode", type=StringType)
scxml_ServiceTemplate.attributes={scxml_ServiceTemplate_exmode, scxml_ServiceTemplate_name, scxml_ServiceTemplate_xmlns, scxml_ServiceTemplate_profile, scxml_ServiceTemplate_version}

# scxml_Script class attributes and methods

# scxml_Cancel class attributes and methods
scxml_Cancel_sendid: Property = Property(name="sendid", type=StringType)
scxml_Cancel_sendidexpr: Property = Property(name="sendidexpr", type=StringType)
scxml_Cancel.attributes={scxml_Cancel_sendid, scxml_Cancel_sendidexpr}

# scxml_If class attributes and methods
scxml_If_cond: Property = Property(name="cond", type=StringType)
scxml_If.attributes={scxml_If_cond}

# scxml_Log class attributes and methods
scxml_Log_label: Property = Property(name="label", type=StringType)
scxml_Log_expr: Property = Property(name="expr", type=StringType)
scxml_Log_level: Property = Property(name="level", type=StringType)
scxml_Log.attributes={scxml_Log_expr, scxml_Log_level, scxml_Log_label}

# scxml_Param class attributes and methods
scxml_Param_name: Property = Property(name="name", type=StringType)
scxml_Param_expr: Property = Property(name="expr", type=StringType)
scxml_Param.attributes={scxml_Param_name, scxml_Param_expr}

# scxml_Raise class attributes and methods
scxml_Raise_event: Property = Property(name="event", type=StringType)
scxml_Raise.attributes={scxml_Raise_event}

# scxml_Send class attributes and methods
scxml_Send_event: Property = Property(name="event", type=StringType)
scxml_Send_eventexpr: Property = Property(name="eventexpr", type=StringType)
scxml_Send_target: Property = Property(name="target", type=StringType)
scxml_Send_targetexpr: Property = Property(name="targetexpr", type=StringType)
scxml_Send_type: Property = Property(name="type", type=StringType)
scxml_Send_typeexpr: Property = Property(name="typeexpr", type=StringType)
scxml_Send_id: Property = Property(name="id", type=StringType)
scxml_Send_idlocation: Property = Property(name="idlocation", type=StringType)
scxml_Send_delay: Property = Property(name="delay", type=StringType)
scxml_Send_delayexpr: Property = Property(name="delayexpr", type=StringType)
scxml_Send_namelist: Property = Property(name="namelist", type=StringType)
scxml_Send_hints: Property = Property(name="hints", type=StringType)
scxml_Send_hintsexpr: Property = Property(name="hintsexpr", type=StringType)
scxml_Send.attributes={scxml_Send_target, scxml_Send_type, scxml_Send_id, scxml_Send_eventexpr, scxml_Send_event, scxml_Send_typeexpr, scxml_Send_delay, scxml_Send_namelist, scxml_Send_idlocation, scxml_Send_hints, scxml_Send_hintsexpr, scxml_Send_targetexpr, scxml_Send_delayexpr}

# scxml_Validate class attributes and methods
scxml_Validate_location: Property = Property(name="location", type=StringType)
scxml_Validate_schema: Property = Property(name="schema", type=StringType)
scxml_Validate.attributes={scxml_Validate_schema, scxml_Validate_location}

# scxml_Donedata class attributes and methods

# scxml_ElseIf class attributes and methods
scxml_ElseIf_cond: Property = Property(name="cond", type=StringType)
scxml_ElseIf.attributes={scxml_ElseIf_cond}

# scxml_Else class attributes and methods

# scxml_Data class attributes and methods
scxml_Data_id: Property = Property(name="id", type=StringType)
scxml_Data_src: Property = Property(name="src", type=StringType)
scxml_Data_expr: Property = Property(name="expr", type=StringType)
scxml_Data.attributes={scxml_Data_id, scxml_Data_expr, scxml_Data_src}

# scxml_Content class attributes and methods

# scxml_Finalize class attributes and methods

# Relationships
datamodel0: BinaryAssociation = BinaryAssociation(
    name="datamodel0",
    ends={
        Property(name="scxml_DataModel", type=scxml_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_NamedElement", type=scxml_DataModel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition1: BinaryAssociation = BinaryAssociation(
    name="transition1",
    ends={
        Property(name="scxml_Transition", type=scxml_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_NamedElement2", type=scxml_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
onentry3: BinaryAssociation = BinaryAssociation(
    name="onentry3",
    ends={
        Property(name="scxml_OnEntry", type=scxml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_State", type=scxml_OnEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
onexit4: BinaryAssociation = BinaryAssociation(
    name="onexit4",
    ends={
        Property(name="scxml_OnExit", type=scxml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_State5", type=scxml_OnExit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initial6: BinaryAssociation = BinaryAssociation(
    name="initial6",
    ends={
        Property(name="scxml_InitialState", type=scxml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_State7", type=scxml_InitialState, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
state9: BinaryAssociation = BinaryAssociation(
    name="state9",
    ends={
        Property(name="scxml_State10", type=scxml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_State8", type=scxml_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
final11: BinaryAssociation = BinaryAssociation(
    name="final11",
    ends={
        Property(name="scxml_FinalState", type=scxml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_State12", type=scxml_FinalState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parallel13: BinaryAssociation = BinaryAssociation(
    name="parallel13",
    ends={
        Property(name="scxml_Parallel", type=scxml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_State14", type=scxml_Parallel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
history15: BinaryAssociation = BinaryAssociation(
    name="history15",
    ends={
        Property(name="scxml_HistoryState", type=scxml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_State16", type=scxml_HistoryState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
anchor17: BinaryAssociation = BinaryAssociation(
    name="anchor17",
    ends={
        Property(name="scxml_Anchor", type=scxml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_State18", type=scxml_Anchor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
invoke19: BinaryAssociation = BinaryAssociation(
    name="invoke19",
    ends={
        Property(name="scxml_Invoke", type=scxml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_State20", type=scxml_Invoke, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target21: BinaryAssociation = BinaryAssociation(
    name="target21",
    ends={
        Property(name="scxml_NamedElement23", type=scxml_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_Transition22", type=scxml_NamedElement, multiplicity=Multiplicity(0, 1))
    }
)
transition27: BinaryAssociation = BinaryAssociation(
    name="transition27",
    ends={
        Property(name="scxml_Transition28", type=scxml_ServiceTemplate, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ServiceTemplate", type=scxml_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
state29: BinaryAssociation = BinaryAssociation(
    name="state29",
    ends={
        Property(name="scxml_State31", type=scxml_ServiceTemplate, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ServiceTemplate30", type=scxml_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source24: BinaryAssociation = BinaryAssociation(
    name="source24",
    ends={
        Property(name="scxml_NamedElement26", type=scxml_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_Transition25", type=scxml_NamedElement, multiplicity=Multiplicity(0, 1))
    }
)
final35: BinaryAssociation = BinaryAssociation(
    name="final35",
    ends={
        Property(name="scxml_ServiceTemplate36", type=scxml_FinalState, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="scxml_FinalState37", type=scxml_ServiceTemplate, multiplicity=Multiplicity(1, 1))
    }
)
parallel38: BinaryAssociation = BinaryAssociation(
    name="parallel38",
    ends={
        Property(name="scxml_Parallel40", type=scxml_ServiceTemplate, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ServiceTemplate39", type=scxml_Parallel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
datamodel41: BinaryAssociation = BinaryAssociation(
    name="datamodel41",
    ends={
        Property(name="scxml_DataModel43", type=scxml_ServiceTemplate, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ServiceTemplate42", type=scxml_DataModel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
script44: BinaryAssociation = BinaryAssociation(
    name="script44",
    ends={
        Property(name="scxml_Script", type=scxml_ServiceTemplate, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ServiceTemplate45", type=scxml_Script, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
script46: BinaryAssociation = BinaryAssociation(
    name="script46",
    ends={
        Property(name="scxml_Script48", type=scxml_OnEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_OnEntry47", type=scxml_Script, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assign49: BinaryAssociation = BinaryAssociation(
    name="assign49",
    ends={
        Property(name="scxml_Assign", type=scxml_OnEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_OnEntry50", type=scxml_Assign, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cancel51: BinaryAssociation = BinaryAssociation(
    name="cancel51",
    ends={
        Property(name="scxml_Cancel", type=scxml_OnEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_OnEntry52", type=scxml_Cancel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
if53: BinaryAssociation = BinaryAssociation(
    name="if53",
    ends={
        Property(name="scxml_If", type=scxml_OnEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_OnEntry54", type=scxml_If, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
log55: BinaryAssociation = BinaryAssociation(
    name="log55",
    ends={
        Property(name="scxml_Log", type=scxml_OnEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_OnEntry56", type=scxml_Log, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
param57: BinaryAssociation = BinaryAssociation(
    name="param57",
    ends={
        Property(name="scxml_Param", type=scxml_OnEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_OnEntry58", type=scxml_Param, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
raise59: BinaryAssociation = BinaryAssociation(
    name="raise59",
    ends={
        Property(name="scxml_Raise", type=scxml_OnEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_OnEntry60", type=scxml_Raise, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
send61: BinaryAssociation = BinaryAssociation(
    name="send61",
    ends={
        Property(name="scxml_Send", type=scxml_OnEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_OnEntry62", type=scxml_Send, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
validate63: BinaryAssociation = BinaryAssociation(
    name="validate63",
    ends={
        Property(name="scxml_Validate", type=scxml_OnEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_OnEntry64", type=scxml_Validate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
script65: BinaryAssociation = BinaryAssociation(
    name="script65",
    ends={
        Property(name="scxml_Script67", type=scxml_OnExit, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_OnExit66", type=scxml_Script, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assign68: BinaryAssociation = BinaryAssociation(
    name="assign68",
    ends={
        Property(name="scxml_Assign70", type=scxml_OnExit, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_OnExit69", type=scxml_Assign, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cancel71: BinaryAssociation = BinaryAssociation(
    name="cancel71",
    ends={
        Property(name="scxml_Cancel73", type=scxml_OnExit, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_OnExit72", type=scxml_Cancel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
if74: BinaryAssociation = BinaryAssociation(
    name="if74",
    ends={
        Property(name="scxml_If76", type=scxml_OnExit, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_OnExit75", type=scxml_If, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
log77: BinaryAssociation = BinaryAssociation(
    name="log77",
    ends={
        Property(name="scxml_Log79", type=scxml_OnExit, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_OnExit78", type=scxml_Log, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
param80: BinaryAssociation = BinaryAssociation(
    name="param80",
    ends={
        Property(name="scxml_Param82", type=scxml_OnExit, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_OnExit81", type=scxml_Param, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initial32: BinaryAssociation = BinaryAssociation(
    name="initial32",
    ends={
        Property(name="scxml_InitialState34", type=scxml_ServiceTemplate, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ServiceTemplate33", type=scxml_InitialState, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
validate89: BinaryAssociation = BinaryAssociation(
    name="validate89",
    ends={
        Property(name="scxml_Validate91", type=scxml_OnExit, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_OnExit90", type=scxml_Validate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
onentry92: BinaryAssociation = BinaryAssociation(
    name="onentry92",
    ends={
        Property(name="scxml_OnEntry94", type=scxml_FinalState, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_FinalState93", type=scxml_OnEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
onexit95: BinaryAssociation = BinaryAssociation(
    name="onexit95",
    ends={
        Property(name="scxml_OnExit97", type=scxml_FinalState, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_FinalState96", type=scxml_OnExit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
donedata98: BinaryAssociation = BinaryAssociation(
    name="donedata98",
    ends={
        Property(name="scxml_Donedata", type=scxml_FinalState, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_FinalState99", type=scxml_Donedata, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
onentry100: BinaryAssociation = BinaryAssociation(
    name="onentry100",
    ends={
        Property(name="scxml_OnEntry102", type=scxml_Parallel, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_Parallel101", type=scxml_OnEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
onexit103: BinaryAssociation = BinaryAssociation(
    name="onexit103",
    ends={
        Property(name="scxml_OnExit105", type=scxml_Parallel, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_Parallel104", type=scxml_OnExit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parallel107: BinaryAssociation = BinaryAssociation(
    name="parallel107",
    ends={
        Property(name="scxml_Parallel108", type=scxml_Parallel, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_Parallel106", type=scxml_Parallel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
state109: BinaryAssociation = BinaryAssociation(
    name="state109",
    ends={
        Property(name="scxml_State111", type=scxml_Parallel, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_Parallel110", type=scxml_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
history112: BinaryAssociation = BinaryAssociation(
    name="history112",
    ends={
        Property(name="scxml_HistoryState114", type=scxml_Parallel, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_Parallel113", type=scxml_HistoryState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
anchor115: BinaryAssociation = BinaryAssociation(
    name="anchor115",
    ends={
        Property(name="scxml_Anchor117", type=scxml_Parallel, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_Parallel116", type=scxml_Anchor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elseif118: BinaryAssociation = BinaryAssociation(
    name="elseif118",
    ends={
        Property(name="scxml_ElseIf", type=scxml_If, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_If119", type=scxml_ElseIf, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
raise83: BinaryAssociation = BinaryAssociation(
    name="raise83",
    ends={
        Property(name="scxml_Raise85", type=scxml_OnExit, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_OnExit84", type=scxml_Raise, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
send86: BinaryAssociation = BinaryAssociation(
    name="send86",
    ends={
        Property(name="scxml_Send88", type=scxml_OnExit, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_OnExit87", type=scxml_Send, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
else120: BinaryAssociation = BinaryAssociation(
    name="else120",
    ends={
        Property(name="scxml_Else", type=scxml_If, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_If121", type=scxml_Else, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assign122: BinaryAssociation = BinaryAssociation(
    name="assign122",
    ends={
        Property(name="scxml_Assign124", type=scxml_If, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_If123", type=scxml_Assign, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cancel125: BinaryAssociation = BinaryAssociation(
    name="cancel125",
    ends={
        Property(name="scxml_Cancel127", type=scxml_If, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_If126", type=scxml_Cancel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
if129: BinaryAssociation = BinaryAssociation(
    name="if129",
    ends={
        Property(name="scxml_If130", type=scxml_If, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_If128", type=scxml_If, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
log131: BinaryAssociation = BinaryAssociation(
    name="log131",
    ends={
        Property(name="scxml_Log133", type=scxml_If, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_If132", type=scxml_Log, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
param134: BinaryAssociation = BinaryAssociation(
    name="param134",
    ends={
        Property(name="scxml_Param136", type=scxml_If, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_If135", type=scxml_Param, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
raise137: BinaryAssociation = BinaryAssociation(
    name="raise137",
    ends={
        Property(name="scxml_Raise139", type=scxml_If, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_If138", type=scxml_Raise, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
send140: BinaryAssociation = BinaryAssociation(
    name="send140",
    ends={
        Property(name="scxml_Send142", type=scxml_If, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_If141", type=scxml_Send, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
data146: BinaryAssociation = BinaryAssociation(
    name="data146",
    ends={
        Property(name="scxml_Data", type=scxml_DataModel, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_DataModel147", type=scxml_Data, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
content148: BinaryAssociation = BinaryAssociation(
    name="content148",
    ends={
        Property(name="scxml_Content", type=scxml_Data, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_Data149", type=scxml_Content, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
validate143: BinaryAssociation = BinaryAssociation(
    name="validate143",
    ends={
        Property(name="scxml_Validate145", type=scxml_If, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_If144", type=scxml_Validate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
param150: BinaryAssociation = BinaryAssociation(
    name="param150",
    ends={
        Property(name="scxml_Param152", type=scxml_Send, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_Send151", type=scxml_Param, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
content153: BinaryAssociation = BinaryAssociation(
    name="content153",
    ends={
        Property(name="scxml_Content155", type=scxml_Send, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_Send154", type=scxml_Content, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
content157: BinaryAssociation = BinaryAssociation(
    name="content157",
    ends={
        Property(name="scxml_Content158", type=scxml_Content, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_Content156", type=scxml_Content, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
content159: BinaryAssociation = BinaryAssociation(
    name="content159",
    ends={
        Property(name="scxml_Content161", type=scxml_Donedata, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_Donedata160", type=scxml_Content, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
param162: BinaryAssociation = BinaryAssociation(
    name="param162",
    ends={
        Property(name="scxml_Param164", type=scxml_Donedata, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_Donedata163", type=scxml_Param, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
content165: BinaryAssociation = BinaryAssociation(
    name="content165",
    ends={
        Property(name="scxml_Content167", type=scxml_Invoke, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_Invoke166", type=scxml_Content, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
param168: BinaryAssociation = BinaryAssociation(
    name="param168",
    ends={
        Property(name="scxml_Invoke169", type=scxml_Param, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="scxml_Param170", type=scxml_Invoke, multiplicity=Multiplicity(1, 1))
    }
)
finalize171: BinaryAssociation = BinaryAssociation(
    name="finalize171",
    ends={
        Property(name="scxml_Finalize", type=scxml_Invoke, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_Invoke172", type=scxml_Finalize, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assign173: BinaryAssociation = BinaryAssociation(
    name="assign173",
    ends={
        Property(name="scxml_Assign175", type=scxml_Finalize, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_Finalize174", type=scxml_Assign, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cancel176: BinaryAssociation = BinaryAssociation(
    name="cancel176",
    ends={
        Property(name="scxml_Cancel178", type=scxml_Finalize, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_Finalize177", type=scxml_Cancel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
if179: BinaryAssociation = BinaryAssociation(
    name="if179",
    ends={
        Property(name="scxml_If181", type=scxml_Finalize, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_Finalize180", type=scxml_If, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
raise188: BinaryAssociation = BinaryAssociation(
    name="raise188",
    ends={
        Property(name="scxml_Raise190", type=scxml_Finalize, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_Finalize189", type=scxml_Raise, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
send191: BinaryAssociation = BinaryAssociation(
    name="send191",
    ends={
        Property(name="scxml_Send193", type=scxml_Finalize, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_Finalize192", type=scxml_Send, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
validate194: BinaryAssociation = BinaryAssociation(
    name="validate194",
    ends={
        Property(name="scxml_Validate196", type=scxml_Finalize, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_Finalize195", type=scxml_Validate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
log182: BinaryAssociation = BinaryAssociation(
    name="log182",
    ends={
        Property(name="scxml_Log184", type=scxml_Finalize, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_Finalize183", type=scxml_Log, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
param185: BinaryAssociation = BinaryAssociation(
    name="param185",
    ends={
        Property(name="scxml_Param187", type=scxml_Finalize, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_Finalize186", type=scxml_Param, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_scxml_State_NamedElement = Generalization(general=NamedElement, specific=scxml_State)
gen_scxml_InitialState_NamedElement = Generalization(general=NamedElement, specific=scxml_InitialState)
gen_scxml_FinalState_NamedElement = Generalization(general=NamedElement, specific=scxml_FinalState)
gen_scxml_Parallel_NamedElement = Generalization(general=NamedElement, specific=scxml_Parallel)
gen_scxml_HistoryState_NamedElement = Generalization(general=NamedElement, specific=scxml_HistoryState)

# Domain Model
domain_model = DomainModel(
    name="scxml",
    types={scxml_NamedElement, scxml_DataModel, scxml_Transition, scxml_State, NamedElement, scxml_OnEntry, scxml_OnExit, scxml_InitialState, scxml_FinalState, scxml_Parallel, scxml_Anchor, scxml_Invoke, scxml_HistoryState, scxml_Assign, scxml_ServiceTemplate, scxml_Script, scxml_Cancel, scxml_If, scxml_Log, scxml_Param, scxml_Raise, scxml_Send, scxml_Validate, scxml_Donedata, scxml_ElseIf, scxml_Else, scxml_Data, scxml_Content, scxml_Finalize},
    associations={datamodel0, transition1, onentry3, onexit4, initial6, state9, final11, parallel13, history15, anchor17, invoke19, target21, transition27, state29, source24, final35, parallel38, datamodel41, script44, script46, assign49, cancel51, if53, log55, param57, raise59, send61, validate63, script65, assign68, cancel71, if74, log77, param80, initial32, validate89, onentry92, onexit95, donedata98, onentry100, onexit103, parallel107, state109, history112, anchor115, elseif118, raise83, send86, else120, assign122, cancel125, if129, log131, param134, raise137, send140, data146, content148, validate143, param150, content153, content157, content159, param162, content165, param168, finalize171, assign173, cancel176, if179, raise188, send191, validate194, log182, param185},
    generalizations={gen_scxml_State_NamedElement, gen_scxml_InitialState_NamedElement, gen_scxml_FinalState_NamedElement, gen_scxml_Parallel_NamedElement, gen_scxml_HistoryState_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)