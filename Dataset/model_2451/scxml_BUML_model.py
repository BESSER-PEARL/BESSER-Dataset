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
ExmodeDatatype: Enumeration = Enumeration(
    name="ExmodeDatatype",
    literals={
            EnumerationLiteral(name="lax"),
			EnumerationLiteral(name="strict")
    }
)

HistoryTypeDatatype: Enumeration = Enumeration(
    name="HistoryTypeDatatype",
    literals={
            EnumerationLiteral(name="shallow"),
			EnumerationLiteral(name="deep")
    }
)

AdapterToken: Enumeration = Enumeration(
    name="AdapterToken",
    literals={
            EnumerationLiteral(name="DESCRIPTION"),
			EnumerationLiteral(name="DATAMODEL")
    }
)

# Classes
scxml_StateChart = Class(name="scxml::StateChart")
AbstractState = Class(name="AbstractState")
AbstractSimpleState = Class(name="AbstractSimpleState")
DatamodelContainer = Class(name="DatamodelContainer")
DescriptionContainer = Class(name="DescriptionContainer")
scxml_Script = Class(name="scxml::Script")
scxml_Node = Class(name="scxml::Node")
scxml_OnEntry = Class(name="scxml::OnEntry")
scxml_OnExit = Class(name="scxml::OnExit")
scxml_TransitionSource = Class(name="scxml::TransitionSource", is_abstract=True)
Node = Class(name="Node")
scxml_CondEventTransition = Class(name="scxml::CondEventTransition")
scxml_TransitionTarget = Class(name="scxml::TransitionTarget", is_abstract=True)
scxml_AbstractState = Class(name="scxml::AbstractState", is_abstract=True)
scxml_SimpleState = Class(name="scxml::SimpleState")
scxml_ParallelState = Class(name="scxml::ParallelState")
scxml_State = Class(name="scxml::State")
TransitionSource = Class(name="TransitionSource")
scxml_HistoryState = Class(name="scxml::HistoryState")
scxml_Transition = Class(name="scxml::Transition")
ExecutableContent = Class(name="ExecutableContent")
Transition = Class(name="Transition")
scxml_InitialState = Class(name="scxml::InitialState")
TransitionTarget = Class(name="TransitionTarget")
scxml_Param = Class(name="scxml::Param")
scxml_Donedata = Class(name="scxml::Donedata")
scxml_EObject = Class(name="scxml::EObject")
scxml_Content = Class(name="scxml::Content")
scxml_FinalState = Class(name="scxml::FinalState")
State = Class(name="State")
scxml_AbstractSimpleState = Class(name="scxml::AbstractSimpleState", is_abstract=True)
scxml_Invoke = Class(name="scxml::Invoke")
scxml_ExecutableContent = Class(name="scxml::ExecutableContent")
scxml_If = Class(name="scxml::If")
scxml_Log = Class(name="scxml::Log")
InitialState = Class(name="InitialState")
scxml_Raise = Class(name="scxml::Raise")
scxml_Send = Class(name="scxml::Send")
scxml_Cancel = Class(name="scxml::Cancel")
scxml_Assign = Class(name="scxml::Assign")
scxml_Validate = Class(name="scxml::Validate")
Donedata = Class(name="Donedata")
scxml_Conditional = Class(name="scxml::Conditional")
Conditional = Class(name="Conditional")
scxml_ElseIf = Class(name="scxml::ElseIf")
scxml_Else = Class(name="scxml::Else")
scxml_Data = Class(name="scxml::Data")
scxml_XData = Class(name="scxml::XData")
Data = Class(name="Data")
scxml_XObject = Class(name="scxml::XObject")
scxml_EClass = Class(name="scxml::EClass")
scxml_Datamodel = Class(name="scxml::Datamodel")
scxml_DatamodelContainer = Class(name="scxml::DatamodelContainer", is_abstract=True)
IAdaptable = Class(name="IAdaptable")
scxml_DescriptionContainer = Class(name="scxml::DescriptionContainer", is_abstract=True)
scxml_Description = Class(name="scxml::Description")
scxml_IAdaptable = Class(name="scxml::IAdaptable", is_abstract=True)

# scxml_StateChart class attributes and methods
scxml_StateChart_xmlns: Property = Property(name="xmlns", type=StringType)
scxml_StateChart_version: Property = Property(name="version", type=StringType)
scxml_StateChart_profile: Property = Property(name="profile", type=StringType)
scxml_StateChart_exmode: Property = Property(name="exmode", type=StringType)
scxml_StateChart_id: Property = Property(name="id", type=StringType)
scxml_StateChart.attributes={scxml_StateChart_id, scxml_StateChart_version, scxml_StateChart_exmode, scxml_StateChart_xmlns, scxml_StateChart_profile}

# AbstractState class attributes and methods

# AbstractSimpleState class attributes and methods

# DatamodelContainer class attributes and methods

# DescriptionContainer class attributes and methods

# scxml_Script class attributes and methods
scxml_Script_value: Property = Property(name="value", type=StringType)
scxml_Script.attributes={scxml_Script_value}

# scxml_Node class attributes and methods

# scxml_OnEntry class attributes and methods

# scxml_OnExit class attributes and methods

# scxml_TransitionSource class attributes and methods

# Node class attributes and methods

# scxml_CondEventTransition class attributes and methods
scxml_CondEventTransition_cond: Property = Property(name="cond", type=StringType)
scxml_CondEventTransition_event: Property = Property(name="event", type=StringType)
scxml_CondEventTransition.attributes={scxml_CondEventTransition_cond, scxml_CondEventTransition_event}

# scxml_TransitionTarget class attributes and methods
scxml_TransitionTarget_id: Property = Property(name="id", type=StringType)
scxml_TransitionTarget.attributes={scxml_TransitionTarget_id}

# scxml_AbstractState class attributes and methods

# scxml_SimpleState class attributes and methods

# scxml_ParallelState class attributes and methods

# scxml_State class attributes and methods

# TransitionSource class attributes and methods

# scxml_HistoryState class attributes and methods
scxml_HistoryState_type: Property = Property(name="type", type=StringType)
scxml_HistoryState.attributes={scxml_HistoryState_type}

# scxml_Transition class attributes and methods

# ExecutableContent class attributes and methods

# Transition class attributes and methods

# scxml_InitialState class attributes and methods

# TransitionTarget class attributes and methods

# scxml_Param class attributes and methods
scxml_Param_name: Property = Property(name="name", type=StringType)
scxml_Param_expr: Property = Property(name="expr", type=StringType)
scxml_Param.attributes={scxml_Param_expr, scxml_Param_name}

# scxml_Donedata class attributes and methods

# scxml_EObject class attributes and methods

# scxml_Content class attributes and methods
scxml_Content_value: Property = Property(name="value", type=StringType)
scxml_Content.attributes={scxml_Content_value}

# scxml_FinalState class attributes and methods

# State class attributes and methods

# scxml_AbstractSimpleState class attributes and methods

# scxml_Invoke class attributes and methods
scxml_Invoke_type: Property = Property(name="type", type=StringType)
scxml_Invoke_typeexpr: Property = Property(name="typeexpr", type=StringType)
scxml_Invoke_src: Property = Property(name="src", type=StringType)
scxml_Invoke_srcexpr: Property = Property(name="srcexpr", type=StringType)
scxml_Invoke_id: Property = Property(name="id", type=StringType)
scxml_Invoke_idlocation: Property = Property(name="idlocation", type=StringType)
scxml_Invoke_namelist: Property = Property(name="namelist", type=StringType)
scxml_Invoke_autoforward: Property = Property(name="autoforward", type=StringType)
scxml_Invoke.attributes={scxml_Invoke_type, scxml_Invoke_id, scxml_Invoke_idlocation, scxml_Invoke_typeexpr, scxml_Invoke_autoforward, scxml_Invoke_namelist, scxml_Invoke_srcexpr, scxml_Invoke_src}

# scxml_ExecutableContent class attributes and methods
scxml_ExecutableContent_group: Property = Property(name="group", type=StringType)
scxml_ExecutableContent.attributes={scxml_ExecutableContent_group}

# scxml_If class attributes and methods

# scxml_Log class attributes and methods
scxml_Log_label: Property = Property(name="label", type=StringType)
scxml_Log_expr: Property = Property(name="expr", type=StringType)
scxml_Log_level: Property = Property(name="level", type=StringType)
scxml_Log.attributes={scxml_Log_label, scxml_Log_expr, scxml_Log_level}

# InitialState class attributes and methods

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
scxml_Send.attributes={scxml_Send_namelist, scxml_Send_targetexpr, scxml_Send_typeexpr, scxml_Send_delayexpr, scxml_Send_hints, scxml_Send_idlocation, scxml_Send_type, scxml_Send_eventexpr, scxml_Send_target, scxml_Send_event, scxml_Send_id, scxml_Send_delay, scxml_Send_hintsexpr}

# scxml_Cancel class attributes and methods
scxml_Cancel_sendid: Property = Property(name="sendid", type=StringType)
scxml_Cancel_sendidexpr: Property = Property(name="sendidexpr", type=StringType)
scxml_Cancel.attributes={scxml_Cancel_sendidexpr, scxml_Cancel_sendid}

# scxml_Assign class attributes and methods
scxml_Assign_location: Property = Property(name="location", type=StringType)
scxml_Assign_expr: Property = Property(name="expr", type=StringType)
scxml_Assign_name: Property = Property(name="name", type=StringType)
scxml_Assign.attributes={scxml_Assign_name, scxml_Assign_location, scxml_Assign_expr}

# scxml_Validate class attributes and methods
scxml_Validate_location: Property = Property(name="location", type=StringType)
scxml_Validate_schema: Property = Property(name="schema", type=StringType)
scxml_Validate.attributes={scxml_Validate_location, scxml_Validate_schema}

# Donedata class attributes and methods

# scxml_Conditional class attributes and methods
scxml_Conditional_cond: Property = Property(name="cond", type=StringType)
scxml_Conditional.attributes={scxml_Conditional_cond}

# Conditional class attributes and methods

# scxml_ElseIf class attributes and methods

# scxml_Else class attributes and methods

# scxml_Data class attributes and methods
scxml_Data_id: Property = Property(name="id", type=StringType)
scxml_Data_src: Property = Property(name="src", type=StringType)
scxml_Data_expr: Property = Property(name="expr", type=StringType)
scxml_Data.attributes={scxml_Data_src, scxml_Data_expr, scxml_Data_id}

# scxml_XData class attributes and methods

# Data class attributes and methods

# scxml_XObject class attributes and methods
scxml_XObject_nsUri: Property = Property(name="nsUri", type=StringType)
scxml_XObject_classifierName: Property = Property(name="classifierName", type=StringType)
scxml_XObject_exchange: Property = Property(name="exchange", type=BooleanType)
scxml_XObject_m_registerAdapter: Method = Method(name="registerAdapter", parameters={})
scxml_XObject.attributes={scxml_XObject_nsUri, scxml_XObject_classifierName, scxml_XObject_exchange}
scxml_XObject.methods={scxml_XObject_m_registerAdapter}

# scxml_EClass class attributes and methods

# scxml_Datamodel class attributes and methods
scxml_Datamodel_schema: Property = Property(name="schema", type=StringType)
scxml_Datamodel.attributes={scxml_Datamodel_schema}

# scxml_DatamodelContainer class attributes and methods
scxml_DatamodelContainer_m_getAdapter: Method = Method(name="getAdapter", parameters={Parameter(name='adapter')}, type=StringType)
scxml_DatamodelContainer.methods={scxml_DatamodelContainer_m_getAdapter}

# IAdaptable class attributes and methods

# scxml_DescriptionContainer class attributes and methods
scxml_DescriptionContainer_m_getAdapter: Method = Method(name="getAdapter", parameters={Parameter(name='adapter')}, type=StringType)
scxml_DescriptionContainer.methods={scxml_DescriptionContainer_m_getAdapter}

# scxml_Description class attributes and methods
scxml_Description_value: Property = Property(name="value", type=StringType)
scxml_Description.attributes={scxml_Description_value}

# scxml_IAdaptable class attributes and methods

# Relationships
script0: BinaryAssociation = BinaryAssociation(
    name="script0",
    ends={
        Property(name="scxml_Script", type=scxml_StateChart, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_StateChart", type=scxml_Script, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
onentry1: BinaryAssociation = BinaryAssociation(
    name="onentry1",
    ends={
        Property(name="scxml_OnEntry", type=scxml_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_Node", type=scxml_OnEntry, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
onexit2: BinaryAssociation = BinaryAssociation(
    name="onexit2",
    ends={
        Property(name="scxml_OnExit", type=scxml_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_Node3", type=scxml_OnExit, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
transition4: BinaryAssociation = BinaryAssociation(
    name="transition4",
    ends={
        Property(name="scxml_CondEventTransition", type=scxml_TransitionSource, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_TransitionSource", type=scxml_CondEventTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
state5: BinaryAssociation = BinaryAssociation(
    name="state5",
    ends={
        Property(name="scxml_SimpleState", type=scxml_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_AbstractState", type=scxml_SimpleState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parallel6: BinaryAssociation = BinaryAssociation(
    name="parallel6",
    ends={
        Property(name="scxml_ParallelState", type=scxml_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_AbstractState7", type=scxml_ParallelState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
history8: BinaryAssociation = BinaryAssociation(
    name="history8",
    ends={
        Property(name="scxml_HistoryState", type=scxml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_State", type=scxml_HistoryState, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target9: BinaryAssociation = BinaryAssociation(
    name="target9",
    ends={
        Property(name="scxml_TransitionTarget", type=scxml_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_Transition", type=scxml_TransitionTarget, multiplicity=Multiplicity(0, 9999))
    }
)
transition10: BinaryAssociation = BinaryAssociation(
    name="transition10",
    ends={
        Property(name="scxml_Transition11", type=scxml_InitialState, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_InitialState", type=scxml_Transition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
param12: BinaryAssociation = BinaryAssociation(
    name="param12",
    ends={
        Property(name="scxml_Param", type=scxml_Donedata, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_Donedata", type=scxml_Param, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
content13: BinaryAssociation = BinaryAssociation(
    name="content13",
    ends={
        Property(name="scxml_EObject", type=scxml_Donedata, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_Donedata14", type=scxml_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
donedata15: BinaryAssociation = BinaryAssociation(
    name="donedata15",
    ends={
        Property(name="scxml_Donedata16", type=scxml_FinalState, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_FinalState", type=scxml_Donedata, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initial117: BinaryAssociation = BinaryAssociation(
    name="initial117",
    ends={
        Property(name="scxml_TransitionTarget18", type=scxml_AbstractSimpleState, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_AbstractSimpleState", type=scxml_TransitionTarget, multiplicity=Multiplicity(0, 1))
    }
)
initial19: BinaryAssociation = BinaryAssociation(
    name="initial19",
    ends={
        Property(name="scxml_InitialState21", type=scxml_AbstractSimpleState, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_AbstractSimpleState20", type=scxml_InitialState, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
final22: BinaryAssociation = BinaryAssociation(
    name="final22",
    ends={
        Property(name="scxml_FinalState24", type=scxml_AbstractSimpleState, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_AbstractSimpleState23", type=scxml_FinalState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
invoke25: BinaryAssociation = BinaryAssociation(
    name="invoke25",
    ends={
        Property(name="scxml_Invoke", type=scxml_SimpleState, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_SimpleState26", type=scxml_Invoke, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
if27: BinaryAssociation = BinaryAssociation(
    name="if27",
    ends={
        Property(name="scxml_If", type=scxml_ExecutableContent, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ExecutableContent", type=scxml_If, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
log28: BinaryAssociation = BinaryAssociation(
    name="log28",
    ends={
        Property(name="scxml_Log", type=scxml_ExecutableContent, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ExecutableContent29", type=scxml_Log, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
raise30: BinaryAssociation = BinaryAssociation(
    name="raise30",
    ends={
        Property(name="scxml_Raise", type=scxml_ExecutableContent, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ExecutableContent31", type=scxml_Raise, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
send32: BinaryAssociation = BinaryAssociation(
    name="send32",
    ends={
        Property(name="scxml_Send", type=scxml_ExecutableContent, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ExecutableContent33", type=scxml_Send, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cancel34: BinaryAssociation = BinaryAssociation(
    name="cancel34",
    ends={
        Property(name="scxml_Cancel", type=scxml_ExecutableContent, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ExecutableContent35", type=scxml_Cancel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
assign36: BinaryAssociation = BinaryAssociation(
    name="assign36",
    ends={
        Property(name="scxml_Assign", type=scxml_ExecutableContent, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ExecutableContent37", type=scxml_Assign, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
validate38: BinaryAssociation = BinaryAssociation(
    name="validate38",
    ends={
        Property(name="scxml_Validate", type=scxml_ExecutableContent, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ExecutableContent39", type=scxml_Validate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
script40: BinaryAssociation = BinaryAssociation(
    name="script40",
    ends={
        Property(name="scxml_Script42", type=scxml_ExecutableContent, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ExecutableContent41", type=scxml_Script, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elseif43: BinaryAssociation = BinaryAssociation(
    name="elseif43",
    ends={
        Property(name="scxml_ElseIf", type=scxml_If, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_If44", type=scxml_ElseIf, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
else45: BinaryAssociation = BinaryAssociation(
    name="else45",
    ends={
        Property(name="scxml_Else", type=scxml_If, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_If46", type=scxml_Else, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
finalize47: BinaryAssociation = BinaryAssociation(
    name="finalize47",
    ends={
        Property(name="scxml_ExecutableContent49", type=scxml_Invoke, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_Invoke48", type=scxml_ExecutableContent, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
object50: BinaryAssociation = BinaryAssociation(
    name="object50",
    ends={
        Property(name="scxml_EObject51", type=scxml_XData, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_XData", type=scxml_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type52: BinaryAssociation = BinaryAssociation(
    name="type52",
    ends={
        Property(name="scxml_EClass", type=scxml_XObject, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_XObject", type=scxml_EClass, multiplicity=Multiplicity(0, 1))
    }
)
data53: BinaryAssociation = BinaryAssociation(
    name="data53",
    ends={
        Property(name="scxml_Data", type=scxml_Datamodel, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_Datamodel", type=scxml_Data, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
datamodel54: BinaryAssociation = BinaryAssociation(
    name="datamodel54",
    ends={
        Property(name="scxml_Datamodel55", type=scxml_DatamodelContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_DatamodelContainer", type=scxml_Datamodel, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
description56: BinaryAssociation = BinaryAssociation(
    name="description56",
    ends={
        Property(name="scxml_Description", type=scxml_DescriptionContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_DescriptionContainer", type=scxml_Description, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_scxml_StateChart_AbstractState = Generalization(general=AbstractState, specific=scxml_StateChart)
gen_scxml_StateChart_AbstractSimpleState = Generalization(general=AbstractSimpleState, specific=scxml_StateChart)
gen_scxml_StateChart_DatamodelContainer = Generalization(general=DatamodelContainer, specific=scxml_StateChart)
gen_scxml_StateChart_DescriptionContainer = Generalization(general=DescriptionContainer, specific=scxml_StateChart)
gen_scxml_Node_DescriptionContainer = Generalization(general=DescriptionContainer, specific=scxml_Node)
gen_scxml_TransitionSource_Node = Generalization(general=Node, specific=scxml_TransitionSource)
gen_scxml_TransitionTarget_Node = Generalization(general=Node, specific=scxml_TransitionTarget)
gen_scxml_State_TransitionTarget = Generalization(general=TransitionTarget, specific=scxml_State)
gen_scxml_State_AbstractState = Generalization(general=AbstractState, specific=scxml_State)
gen_scxml_State_TransitionSource = Generalization(general=TransitionSource, specific=scxml_State)
gen_scxml_State_DatamodelContainer = Generalization(general=DatamodelContainer, specific=scxml_State)
gen_scxml_Transition_ExecutableContent = Generalization(general=ExecutableContent, specific=scxml_Transition)
gen_scxml_Transition_DescriptionContainer = Generalization(general=DescriptionContainer, specific=scxml_Transition)
gen_scxml_CondEventTransition_Transition = Generalization(general=Transition, specific=scxml_CondEventTransition)
gen_scxml_InitialState_DescriptionContainer = Generalization(general=DescriptionContainer, specific=scxml_InitialState)
gen_scxml_FinalState_TransitionTarget = Generalization(general=TransitionTarget, specific=scxml_FinalState)
gen_scxml_ParallelState_State = Generalization(general=State, specific=scxml_ParallelState)
gen_scxml_SimpleState_State = Generalization(general=State, specific=scxml_SimpleState)
gen_scxml_SimpleState_AbstractSimpleState = Generalization(general=AbstractSimpleState, specific=scxml_SimpleState)
gen_scxml_HistoryState_TransitionTarget = Generalization(general=TransitionTarget, specific=scxml_HistoryState)
gen_scxml_HistoryState_InitialState = Generalization(general=InitialState, specific=scxml_HistoryState)
gen_scxml_OnEntry_ExecutableContent = Generalization(general=ExecutableContent, specific=scxml_OnEntry)
gen_scxml_OnExit_ExecutableContent = Generalization(general=ExecutableContent, specific=scxml_OnExit)
gen_scxml_Raise_Donedata = Generalization(general=Donedata, specific=scxml_Raise)
gen_scxml_If_Conditional = Generalization(general=Conditional, specific=scxml_If)
gen_scxml_If_ExecutableContent = Generalization(general=ExecutableContent, specific=scxml_If)
gen_scxml_ElseIf_Conditional = Generalization(general=Conditional, specific=scxml_ElseIf)
gen_scxml_Send_Donedata = Generalization(general=Donedata, specific=scxml_Send)
gen_scxml_Invoke_Donedata = Generalization(general=Donedata, specific=scxml_Invoke)
gen_scxml_Data_DescriptionContainer = Generalization(general=DescriptionContainer, specific=scxml_Data)
gen_scxml_XData_Data = Generalization(general=Data, specific=scxml_XData)
gen_scxml_Datamodel_DescriptionContainer = Generalization(general=DescriptionContainer, specific=scxml_Datamodel)
gen_scxml_DatamodelContainer_IAdaptable = Generalization(general=IAdaptable, specific=scxml_DatamodelContainer)
gen_scxml_DescriptionContainer_IAdaptable = Generalization(general=IAdaptable, specific=scxml_DescriptionContainer)

# Domain Model
domain_model = DomainModel(
    name="scxml",
    types={scxml_StateChart, AbstractState, AbstractSimpleState, DatamodelContainer, DescriptionContainer, scxml_Script, scxml_Node, scxml_OnEntry, scxml_OnExit, scxml_TransitionSource, Node, scxml_CondEventTransition, scxml_TransitionTarget, scxml_AbstractState, scxml_SimpleState, scxml_ParallelState, scxml_State, TransitionSource, scxml_HistoryState, scxml_Transition, ExecutableContent, Transition, scxml_InitialState, TransitionTarget, scxml_Param, scxml_Donedata, scxml_EObject, scxml_Content, scxml_FinalState, State, scxml_AbstractSimpleState, scxml_Invoke, scxml_ExecutableContent, scxml_If, scxml_Log, InitialState, scxml_Raise, scxml_Send, scxml_Cancel, scxml_Assign, scxml_Validate, Donedata, scxml_Conditional, Conditional, scxml_ElseIf, scxml_Else, scxml_Data, scxml_XData, Data, scxml_XObject, scxml_EClass, scxml_Datamodel, scxml_DatamodelContainer, IAdaptable, scxml_DescriptionContainer, scxml_Description, scxml_IAdaptable, ExmodeDatatype, HistoryTypeDatatype, AdapterToken},
    associations={script0, onentry1, onexit2, transition4, state5, parallel6, history8, target9, transition10, param12, content13, donedata15, initial117, initial19, final22, invoke25, if27, log28, raise30, send32, cancel34, assign36, validate38, script40, elseif43, else45, finalize47, object50, type52, data53, datamodel54, description56},
    generalizations={gen_scxml_StateChart_AbstractState, gen_scxml_StateChart_AbstractSimpleState, gen_scxml_StateChart_DatamodelContainer, gen_scxml_StateChart_DescriptionContainer, gen_scxml_Node_DescriptionContainer, gen_scxml_TransitionSource_Node, gen_scxml_TransitionTarget_Node, gen_scxml_State_TransitionTarget, gen_scxml_State_AbstractState, gen_scxml_State_TransitionSource, gen_scxml_State_DatamodelContainer, gen_scxml_Transition_ExecutableContent, gen_scxml_Transition_DescriptionContainer, gen_scxml_CondEventTransition_Transition, gen_scxml_InitialState_DescriptionContainer, gen_scxml_FinalState_TransitionTarget, gen_scxml_ParallelState_State, gen_scxml_SimpleState_State, gen_scxml_SimpleState_AbstractSimpleState, gen_scxml_HistoryState_TransitionTarget, gen_scxml_HistoryState_InitialState, gen_scxml_OnEntry_ExecutableContent, gen_scxml_OnExit_ExecutableContent, gen_scxml_Raise_Donedata, gen_scxml_If_Conditional, gen_scxml_If_ExecutableContent, gen_scxml_ElseIf_Conditional, gen_scxml_Send_Donedata, gen_scxml_Invoke_Donedata, gen_scxml_Data_DescriptionContainer, gen_scxml_XData_Data, gen_scxml_Datamodel_DescriptionContainer, gen_scxml_DatamodelContainer_IAdaptable, gen_scxml_DescriptionContainer_IAdaptable},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)