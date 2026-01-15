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
DataType: Enumeration = Enumeration(
    name="DataType",
    literals={
            EnumerationLiteral(name="Integer"),
			EnumerationLiteral(name="Real"),
			EnumerationLiteral(name="Float"),
			EnumerationLiteral(name="Double"),
			EnumerationLiteral(name="Boolean")
    }
)

# Classes
sam_Automaton = Class(name="sam::Automaton")
sam_Transition = Class(name="sam::Transition")
sam_AbstractState = Class(name="sam::AbstractState", is_abstract=True)
NamedItem = Class(name="NamedItem")
sam_MacroState = Class(name="sam::MacroState")
ModelContent = Class(name="ModelContent")
sam_Port = Class(name="sam::Port", is_abstract=True)
sam_State = Class(name="sam::State")
TraceableElement = Class(name="TraceableElement")
sam_InitialState = Class(name="sam::InitialState")
State = Class(name="State")
AbstractState = Class(name="AbstractState")
sam_ControlPort = Class(name="sam::ControlPort", is_abstract=True)
Port = Class(name="Port")
sam_DataPort = Class(name="sam::DataPort", is_abstract=True)
sam_InControlPort = Class(name="sam::InControlPort")
ControlPort = Class(name="ControlPort")
InputPort = Class(name="InputPort")
sam_ControlMerge = Class(name="sam::ControlMerge")
sam_OutControlPort = Class(name="sam::OutControlPort")
OutputPort = Class(name="OutputPort")
sam_MessageSplit = Class(name="sam::MessageSplit")
sam_OutDataPort = Class(name="sam::OutDataPort")
sam_InDataPort = Class(name="sam::InDataPort")
DataPort = Class(name="DataPort")
sam_DataStore = Class(name="sam::DataStore")
sam_DataSynchronisation = Class(name="sam::DataSynchronisation", is_abstract=True)
sam_DataMerge = Class(name="sam::DataMerge")
sam_InputPort = Class(name="sam::InputPort", is_abstract=True)
sam_System = Class(name="sam::System")
sam_Flow = Class(name="sam::Flow", is_abstract=True)
sam_MultiPort = Class(name="sam::MultiPort")
sam_OutputPort = Class(name="sam::OutputPort", is_abstract=True)
sam_DataComposition = Class(name="sam::DataComposition")
DataSynchronisation = Class(name="DataSynchronisation")
sam_ControlFlow = Class(name="sam::ControlFlow")
Flow = Class(name="Flow")
sam_DataFlow = Class(name="sam::DataFlow")
sam_FlowGroup = Class(name="sam::FlowGroup")
sam_DataDecomposition = Class(name="sam::DataDecomposition")
sam_Model = Class(name="sam::Model")
sam_EObject = Class(name="sam::EObject")
sam_Gate = Class(name="sam::Gate", is_abstract=True)
sam_ModelContent = Class(name="sam::ModelContent", is_abstract=True)
sam_MessagePort = Class(name="sam::MessagePort", is_abstract=True)
sam_IdentifiedItem = Class(name="sam::IdentifiedItem", is_abstract=True)
EModelElement = Class(name="EModelElement")
sam_NamedItem = Class(name="sam::NamedItem", is_abstract=True)
IdentifiedItem = Class(name="IdentifiedItem")
sam_InMessagePort = Class(name="sam::InMessagePort")
ENamedElement = Class(name="ENamedElement")
sam_MessageFlow = Class(name="sam::MessageFlow")
sam_OutMessagePort = Class(name="sam::OutMessagePort")
MessagePort = Class(name="MessagePort")
sam_MessageMerge = Class(name="sam::MessageMerge")
sam_AsynchronousGate = Class(name="sam::AsynchronousGate", is_abstract=True)
Gate = Class(name="Gate")
sam_SynchronousGate = Class(name="sam::SynchronousGate", is_abstract=True)
SynchronousGate = Class(name="SynchronousGate")
MergeGate = Class(name="MergeGate")
sam_SplitGate = Class(name="sam::SplitGate", is_abstract=True)
AsynchronousGate = Class(name="AsynchronousGate")
sam_MergeGate = Class(name="sam::MergeGate", is_abstract=True)
SplitGate = Class(name="SplitGate")
sam_TraceableElement = Class(name="sam::TraceableElement")

# sam_Automaton class attributes and methods

# sam_Transition class attributes and methods
sam_Transition_condition: Property = Property(name="condition", type=StringType)
sam_Transition_emission: Property = Property(name="emission", type=StringType)
sam_Transition_priority: Property = Property(name="priority", type=StringType)
sam_Transition.attributes={sam_Transition_condition, sam_Transition_emission, sam_Transition_priority}

# sam_AbstractState class attributes and methods

# NamedItem class attributes and methods

# sam_MacroState class attributes and methods

# ModelContent class attributes and methods

# sam_Port class attributes and methods
sam_Port_m_isIn: Method = Method(name="isIn", parameters={}, type=BooleanType)
sam_Port_m_isOut: Method = Method(name="isOut", parameters={}, type=BooleanType)
sam_Port.methods={sam_Port_m_isIn, sam_Port_m_isOut}

# sam_State class attributes and methods

# TraceableElement class attributes and methods

# sam_InitialState class attributes and methods

# State class attributes and methods

# AbstractState class attributes and methods

# sam_ControlPort class attributes and methods

# Port class attributes and methods

# sam_DataPort class attributes and methods

# sam_InControlPort class attributes and methods

# ControlPort class attributes and methods

# InputPort class attributes and methods

# sam_ControlMerge class attributes and methods

# sam_OutControlPort class attributes and methods

# OutputPort class attributes and methods

# sam_MessageSplit class attributes and methods

# sam_OutDataPort class attributes and methods

# sam_InDataPort class attributes and methods

# DataPort class attributes and methods

# sam_DataStore class attributes and methods

# sam_DataSynchronisation class attributes and methods

# sam_DataMerge class attributes and methods

# sam_InputPort class attributes and methods

# sam_System class attributes and methods

# sam_Flow class attributes and methods

# sam_MultiPort class attributes and methods

# sam_OutputPort class attributes and methods

# sam_DataComposition class attributes and methods

# DataSynchronisation class attributes and methods

# sam_ControlFlow class attributes and methods

# Flow class attributes and methods

# sam_DataFlow class attributes and methods
sam_DataFlow_type: Property = Property(name="type", type=StringType)
sam_DataFlow.attributes={sam_DataFlow_type}

# sam_FlowGroup class attributes and methods
sam_FlowGroup_globalComment: Property = Property(name="globalComment", type=StringType)
sam_FlowGroup.attributes={sam_FlowGroup_globalComment}

# sam_DataDecomposition class attributes and methods

# sam_Model class attributes and methods

# sam_EObject class attributes and methods

# sam_Gate class attributes and methods

# sam_ModelContent class attributes and methods

# sam_MessagePort class attributes and methods

# sam_IdentifiedItem class attributes and methods
sam_IdentifiedItem_comment: Property = Property(name="comment", type=StringType)
sam_IdentifiedItem_requirements: Property = Property(name="requirements", type=StringType)
sam_IdentifiedItem.attributes={sam_IdentifiedItem_comment, sam_IdentifiedItem_requirements}

# EModelElement class attributes and methods

# sam_NamedItem class attributes and methods
sam_NamedItem_name: Property = Property(name="name", type=StringType)
sam_NamedItem.attributes={sam_NamedItem_name}

# IdentifiedItem class attributes and methods

# sam_InMessagePort class attributes and methods

# ENamedElement class attributes and methods

# sam_MessageFlow class attributes and methods

# sam_OutMessagePort class attributes and methods

# MessagePort class attributes and methods

# sam_MessageMerge class attributes and methods

# sam_AsynchronousGate class attributes and methods

# Gate class attributes and methods

# sam_SynchronousGate class attributes and methods

# SynchronousGate class attributes and methods

# MergeGate class attributes and methods

# sam_SplitGate class attributes and methods

# AsynchronousGate class attributes and methods

# sam_MergeGate class attributes and methods

# SplitGate class attributes and methods

# sam_TraceableElement class attributes and methods

# Relationships
parentState0: BinaryAssociation = BinaryAssociation(
    name="parentState0",
    ends={
        Property(name="MacroState", type=sam_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="composition", type=sam_MacroState, multiplicity=Multiplicity(0, 1))
    }
)
parentAutomaton1: BinaryAssociation = BinaryAssociation(
    name="parentAutomaton1",
    ends={
        Property(name="Automaton", type=sam_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="listStates", type=sam_Automaton, multiplicity=Multiplicity(0, 1))
    }
)
listPorts5: BinaryAssociation = BinaryAssociation(
    name="listPorts5",
    ends={
        Property(name="parentAutomaton6", type=sam_Port, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="Port", type=sam_Automaton, multiplicity=Multiplicity(1, 1))
    }
)
listStates7: BinaryAssociation = BinaryAssociation(
    name="listStates7",
    ends={
        Property(name="AbstractState", type=sam_Automaton, multiplicity=Multiplicity(1, 1)),
        Property(name="parentAutomaton8", type=sam_AbstractState, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
isInstanceOf10: BinaryAssociation = BinaryAssociation(
    name="isInstanceOf10",
    ends={
        Property(name="sam_Automaton", type=sam_Automaton, multiplicity=Multiplicity(1, 1)),
        Property(name="sam_Automaton9", type=sam_Automaton, multiplicity=Multiplicity(0, 1))
    }
)
outlink2: BinaryAssociation = BinaryAssociation(
    name="outlink2",
    ends={
        Property(name="Transition", type=sam_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=sam_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
listTransitions3: BinaryAssociation = BinaryAssociation(
    name="listTransitions3",
    ends={
        Property(name="Transition4", type=sam_Automaton, multiplicity=Multiplicity(1, 1)),
        Property(name="parentAutomaton", type=sam_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inlink13: BinaryAssociation = BinaryAssociation(
    name="inlink13",
    ends={
        Property(name="Transition14", type=sam_State, multiplicity=Multiplicity(1, 1)),
        Property(name="dest", type=sam_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
composition11: BinaryAssociation = BinaryAssociation(
    name="composition11",
    ends={
        Property(name="AbstractState12", type=sam_MacroState, multiplicity=Multiplicity(1, 1)),
        Property(name="parentState", type=sam_AbstractState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
merge20: BinaryAssociation = BinaryAssociation(
    name="merge20",
    ends={
        Property(name="ControlMerge", type=sam_InControlPort, multiplicity=Multiplicity(1, 1)),
        Property(name="in", type=sam_ControlMerge, multiplicity=Multiplicity(0, 1))
    }
)
dest15: BinaryAssociation = BinaryAssociation(
    name="dest15",
    ends={
        Property(name="State", type=sam_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="inlink", type=sam_State, multiplicity=Multiplicity(1, 1))
    }
)
parentAutomaton16: BinaryAssociation = BinaryAssociation(
    name="parentAutomaton16",
    ends={
        Property(name="Automaton17", type=sam_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="listTransitions", type=sam_Automaton, multiplicity=Multiplicity(1, 1))
    }
)
source18: BinaryAssociation = BinaryAssociation(
    name="source18",
    ends={
        Property(name="AbstractState19", type=sam_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outlink", type=sam_AbstractState, multiplicity=Multiplicity(1, 1))
    }
)
split27: BinaryAssociation = BinaryAssociation(
    name="split27",
    ends={
        Property(name="MessageSplit", type=sam_OutControlPort, multiplicity=Multiplicity(1, 1)),
        Property(name="outControl", type=sam_MessageSplit, multiplicity=Multiplicity(0, 1))
    }
)
merge28: BinaryAssociation = BinaryAssociation(
    name="merge28",
    ends={
        Property(name="ControlMerge29", type=sam_OutControlPort, multiplicity=Multiplicity(1, 1)),
        Property(name="out", type=sam_ControlMerge, multiplicity=Multiplicity(0, 1))
    }
)
parentDataStore30: BinaryAssociation = BinaryAssociation(
    name="parentDataStore30",
    ends={
        Property(name="DataStore32", type=sam_OutDataPort, multiplicity=Multiplicity(1, 1)),
        Property(name="out31", type=sam_DataStore, multiplicity=Multiplicity(0, 1))
    }
)
parentDataStore21: BinaryAssociation = BinaryAssociation(
    name="parentDataStore21",
    ends={
        Property(name="DataStore", type=sam_InDataPort, multiplicity=Multiplicity(1, 1)),
        Property(name="in22", type=sam_DataStore, multiplicity=Multiplicity(0, 1))
    }
)
parentSync23: BinaryAssociation = BinaryAssociation(
    name="parentSync23",
    ends={
        Property(name="DataSynchronisation", type=sam_InDataPort, multiplicity=Multiplicity(1, 1)),
        Property(name="in24", type=sam_DataSynchronisation, multiplicity=Multiplicity(0, 1))
    }
)
merge25: BinaryAssociation = BinaryAssociation(
    name="merge25",
    ends={
        Property(name="DataMerge", type=sam_InDataPort, multiplicity=Multiplicity(1, 1)),
        Property(name="in26", type=sam_DataMerge, multiplicity=Multiplicity(0, 1))
    }
)
parentSystem41: BinaryAssociation = BinaryAssociation(
    name="parentSystem41",
    ends={
        Property(name="System", type=sam_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="listPorts", type=sam_System, multiplicity=Multiplicity(0, 1))
    }
)
outlink42: BinaryAssociation = BinaryAssociation(
    name="outlink42",
    ends={
        Property(name="sam_Flow", type=sam_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="sam_Port", type=sam_Flow, multiplicity=Multiplicity(0, 1))
    }
)
inlink43: BinaryAssociation = BinaryAssociation(
    name="inlink43",
    ends={
        Property(name="sam_Flow45", type=sam_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="sam_Port44", type=sam_Flow, multiplicity=Multiplicity(0, 1))
    }
)
parentAutomaton46: BinaryAssociation = BinaryAssociation(
    name="parentAutomaton46",
    ends={
        Property(name="Automaton48", type=sam_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="listPorts47", type=sam_Automaton, multiplicity=Multiplicity(0, 1))
    }
)
parentMultiPort49: BinaryAssociation = BinaryAssociation(
    name="parentMultiPort49",
    ends={
        Property(name="sam_MultiPort", type=sam_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="sam_Port50", type=sam_MultiPort, multiplicity=Multiplicity(0, 1))
    }
)
parentSync33: BinaryAssociation = BinaryAssociation(
    name="parentSync33",
    ends={
        Property(name="DataSynchronisation35", type=sam_OutDataPort, multiplicity=Multiplicity(1, 1)),
        Property(name="out34", type=sam_DataSynchronisation, multiplicity=Multiplicity(0, 1))
    }
)
split36: BinaryAssociation = BinaryAssociation(
    name="split36",
    ends={
        Property(name="MessageSplit37", type=sam_OutDataPort, multiplicity=Multiplicity(1, 1)),
        Property(name="outData", type=sam_MessageSplit, multiplicity=Multiplicity(0, 1))
    }
)
merge38: BinaryAssociation = BinaryAssociation(
    name="merge38",
    ends={
        Property(name="DataMerge40", type=sam_OutDataPort, multiplicity=Multiplicity(1, 1)),
        Property(name="out39", type=sam_DataMerge, multiplicity=Multiplicity(0, 1))
    }
)
source58: BinaryAssociation = BinaryAssociation(
    name="source58",
    ends={
        Property(name="sam_DataPort", type=sam_DataFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="sam_DataFlow", type=sam_DataPort, multiplicity=Multiplicity(1, 1))
    }
)
dest59: BinaryAssociation = BinaryAssociation(
    name="dest59",
    ends={
        Property(name="sam_DataPort61", type=sam_DataFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="sam_DataFlow60", type=sam_DataPort, multiplicity=Multiplicity(1, 9999))
    }
)
parentSystem62: BinaryAssociation = BinaryAssociation(
    name="parentSystem62",
    ends={
        Property(name="System63", type=sam_DataStore, multiplicity=Multiplicity(1, 1)),
        Property(name="listStores", type=sam_System, multiplicity=Multiplicity(1, 1))
    }
)
isInstanceOf52: BinaryAssociation = BinaryAssociation(
    name="isInstanceOf52",
    ends={
        Property(name="sam_Port53", type=sam_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="sam_Port51", type=sam_Port, multiplicity=Multiplicity(0, 1))
    }
)
source54: BinaryAssociation = BinaryAssociation(
    name="source54",
    ends={
        Property(name="sam_ControlPort", type=sam_ControlFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="sam_ControlFlow", type=sam_ControlPort, multiplicity=Multiplicity(1, 1))
    }
)
dest55: BinaryAssociation = BinaryAssociation(
    name="dest55",
    ends={
        Property(name="sam_ControlPort57", type=sam_ControlFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="sam_ControlFlow56", type=sam_ControlPort, multiplicity=Multiplicity(1, 9999))
    }
)
parentSystem67: BinaryAssociation = BinaryAssociation(
    name="parentSystem67",
    ends={
        Property(name="System68", type=sam_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="listFlows", type=sam_System, multiplicity=Multiplicity(1, 1))
    }
)
group69: BinaryAssociation = BinaryAssociation(
    name="group69",
    ends={
        Property(name="FlowGroup", type=sam_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="flows", type=sam_FlowGroup, multiplicity=Multiplicity(1, 1))
    }
)
listPorts70: BinaryAssociation = BinaryAssociation(
    name="listPorts70",
    ends={
        Property(name="Port71", type=sam_System, multiplicity=Multiplicity(1, 1)),
        Property(name="parentSystem", type=sam_Port, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
in64: BinaryAssociation = BinaryAssociation(
    name="in64",
    ends={
        Property(name="InDataPort", type=sam_DataStore, multiplicity=Multiplicity(1, 1)),
        Property(name="parentDataStore", type=sam_InDataPort, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
out65: BinaryAssociation = BinaryAssociation(
    name="out65",
    ends={
        Property(name="OutDataPort", type=sam_DataStore, multiplicity=Multiplicity(1, 1)),
        Property(name="parentDataStore66", type=sam_OutDataPort, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
modelContent83: BinaryAssociation = BinaryAssociation(
    name="modelContent83",
    ends={
        Property(name="ModelContent84", type=sam_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="parentModel", type=sam_ModelContent, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
flowGroups85: BinaryAssociation = BinaryAssociation(
    name="flowGroups85",
    ends={
        Property(name="FlowGroup86", type=sam_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="model", type=sam_FlowGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requirementModel87: BinaryAssociation = BinaryAssociation(
    name="requirementModel87",
    ends={
        Property(name="sam_EObject", type=sam_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="sam_Model", type=sam_EObject, multiplicity=Multiplicity(0, 1))
    }
)
listStores72: BinaryAssociation = BinaryAssociation(
    name="listStores72",
    ends={
        Property(name="DataStore74", type=sam_System, multiplicity=Multiplicity(1, 1)),
        Property(name="parentSystem73", type=sam_DataStore, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
listSynchronisation75: BinaryAssociation = BinaryAssociation(
    name="listSynchronisation75",
    ends={
        Property(name="Gate", type=sam_System, multiplicity=Multiplicity(1, 1)),
        Property(name="parentSystem76", type=sam_Gate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
listFlows77: BinaryAssociation = BinaryAssociation(
    name="listFlows77",
    ends={
        Property(name="Flow", type=sam_System, multiplicity=Multiplicity(1, 1)),
        Property(name="parentSystem78", type=sam_Flow, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
listElements79: BinaryAssociation = BinaryAssociation(
    name="listElements79",
    ends={
        Property(name="ModelContent", type=sam_System, multiplicity=Multiplicity(1, 1)),
        Property(name="parentSystem80", type=sam_ModelContent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
isInstanceOf82: BinaryAssociation = BinaryAssociation(
    name="isInstanceOf82",
    ends={
        Property(name="sam_System", type=sam_System, multiplicity=Multiplicity(1, 1)),
        Property(name="sam_System81", type=sam_System, multiplicity=Multiplicity(0, 1))
    }
)
listPort92: BinaryAssociation = BinaryAssociation(
    name="listPort92",
    ends={
        Property(name="sam_Port94", type=sam_MultiPort, multiplicity=Multiplicity(1, 1)),
        Property(name="sam_MultiPort93", type=sam_Port, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
parent95: BinaryAssociation = BinaryAssociation(
    name="parent95",
    ends={
        Property(name="ModelContent96", type=sam_MultiPort, multiplicity=Multiplicity(1, 1)),
        Property(name="listMultiPort", type=sam_ModelContent, multiplicity=Multiplicity(1, 1))
    }
)
isInstanceOf98: BinaryAssociation = BinaryAssociation(
    name="isInstanceOf98",
    ends={
        Property(name="sam_MultiPort99", type=sam_MultiPort, multiplicity=Multiplicity(1, 1)),
        Property(name="sam_MultiPort97", type=sam_MultiPort, multiplicity=Multiplicity(0, 1))
    }
)
parentModel88: BinaryAssociation = BinaryAssociation(
    name="parentModel88",
    ends={
        Property(name="Model", type=sam_ModelContent, multiplicity=Multiplicity(1, 1)),
        Property(name="modelContent", type=sam_Model, multiplicity=Multiplicity(0, 1))
    }
)
parentSystem89: BinaryAssociation = BinaryAssociation(
    name="parentSystem89",
    ends={
        Property(name="System90", type=sam_ModelContent, multiplicity=Multiplicity(1, 1)),
        Property(name="listElements", type=sam_System, multiplicity=Multiplicity(0, 1))
    }
)
listMultiPort91: BinaryAssociation = BinaryAssociation(
    name="listMultiPort91",
    ends={
        Property(name="MultiPort", type=sam_ModelContent, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=sam_MultiPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
merge104: BinaryAssociation = BinaryAssociation(
    name="merge104",
    ends={
        Property(name="MessageMerge", type=sam_OutMessagePort, multiplicity=Multiplicity(1, 1)),
        Property(name="out105", type=sam_MessageMerge, multiplicity=Multiplicity(0, 1))
    }
)
split106: BinaryAssociation = BinaryAssociation(
    name="split106",
    ends={
        Property(name="MessageSplit108", type=sam_InMessagePort, multiplicity=Multiplicity(1, 1)),
        Property(name="in107", type=sam_MessageSplit, multiplicity=Multiplicity(0, 1))
    }
)
merge109: BinaryAssociation = BinaryAssociation(
    name="merge109",
    ends={
        Property(name="MessageMerge111", type=sam_InMessagePort, multiplicity=Multiplicity(1, 1)),
        Property(name="in110", type=sam_MessageMerge, multiplicity=Multiplicity(0, 1))
    }
)
source100: BinaryAssociation = BinaryAssociation(
    name="source100",
    ends={
        Property(name="sam_MessagePort", type=sam_MessageFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="sam_MessageFlow", type=sam_MessagePort, multiplicity=Multiplicity(1, 1))
    }
)
dest101: BinaryAssociation = BinaryAssociation(
    name="dest101",
    ends={
        Property(name="sam_MessagePort103", type=sam_MessageFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="sam_MessageFlow102", type=sam_MessagePort, multiplicity=Multiplicity(1, 9999))
    }
)
in118: BinaryAssociation = BinaryAssociation(
    name="in118",
    ends={
        Property(name="InDataPort119", type=sam_DataSynchronisation, multiplicity=Multiplicity(1, 1)),
        Property(name="parentSync", type=sam_InDataPort, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
flows112: BinaryAssociation = BinaryAssociation(
    name="flows112",
    ends={
        Property(name="Flow113", type=sam_FlowGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="group", type=sam_Flow, multiplicity=Multiplicity(0, 9999))
    }
)
model114: BinaryAssociation = BinaryAssociation(
    name="model114",
    ends={
        Property(name="Model115", type=sam_FlowGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="flowGroups", type=sam_Model, multiplicity=Multiplicity(1, 1))
    }
)
parentSystem116: BinaryAssociation = BinaryAssociation(
    name="parentSystem116",
    ends={
        Property(name="System117", type=sam_Gate, multiplicity=Multiplicity(1, 1)),
        Property(name="listSynchronisation", type=sam_System, multiplicity=Multiplicity(1, 1))
    }
)
in123: BinaryAssociation = BinaryAssociation(
    name="in123",
    ends={
        Property(name="InMessagePort", type=sam_MessageSplit, multiplicity=Multiplicity(1, 1)),
        Property(name="split", type=sam_InMessagePort, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
outData124: BinaryAssociation = BinaryAssociation(
    name="outData124",
    ends={
        Property(name="OutDataPort126", type=sam_MessageSplit, multiplicity=Multiplicity(1, 1)),
        Property(name="split125", type=sam_OutDataPort, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
outControl127: BinaryAssociation = BinaryAssociation(
    name="outControl127",
    ends={
        Property(name="OutControlPort", type=sam_MessageSplit, multiplicity=Multiplicity(1, 1)),
        Property(name="split128", type=sam_OutControlPort, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
in129: BinaryAssociation = BinaryAssociation(
    name="in129",
    ends={
        Property(name="InDataPort130", type=sam_DataMerge, multiplicity=Multiplicity(1, 1)),
        Property(name="merge", type=sam_InDataPort, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
out120: BinaryAssociation = BinaryAssociation(
    name="out120",
    ends={
        Property(name="OutDataPort122", type=sam_DataSynchronisation, multiplicity=Multiplicity(1, 1)),
        Property(name="parentSync121", type=sam_OutDataPort, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
in139: BinaryAssociation = BinaryAssociation(
    name="in139",
    ends={
        Property(name="InMessagePort141", type=sam_MessageMerge, multiplicity=Multiplicity(1, 1)),
        Property(name="merge140", type=sam_InMessagePort, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
out142: BinaryAssociation = BinaryAssociation(
    name="out142",
    ends={
        Property(name="OutMessagePort", type=sam_MessageMerge, multiplicity=Multiplicity(1, 1)),
        Property(name="merge143", type=sam_OutMessagePort, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
out131: BinaryAssociation = BinaryAssociation(
    name="out131",
    ends={
        Property(name="OutDataPort133", type=sam_DataMerge, multiplicity=Multiplicity(1, 1)),
        Property(name="merge132", type=sam_OutDataPort, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
in134: BinaryAssociation = BinaryAssociation(
    name="in134",
    ends={
        Property(name="InControlPort", type=sam_ControlMerge, multiplicity=Multiplicity(1, 1)),
        Property(name="merge135", type=sam_InControlPort, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
out136: BinaryAssociation = BinaryAssociation(
    name="out136",
    ends={
        Property(name="OutControlPort138", type=sam_ControlMerge, multiplicity=Multiplicity(1, 1)),
        Property(name="merge137", type=sam_OutControlPort, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)

# Generalizations
gen_sam_AbstractState_NamedItem = Generalization(general=NamedItem, specific=sam_AbstractState)
gen_sam_Automaton_ModelContent = Generalization(general=ModelContent, specific=sam_Automaton)
gen_sam_State_AbstractState = Generalization(general=AbstractState, specific=sam_State)
gen_sam_Transition_TraceableElement = Generalization(general=TraceableElement, specific=sam_Transition)
gen_sam_InitialState_State = Generalization(general=State, specific=sam_InitialState)
gen_sam_MacroState_AbstractState = Generalization(general=AbstractState, specific=sam_MacroState)
gen_sam_ControlPort_Port = Generalization(general=Port, specific=sam_ControlPort)
gen_sam_DataPort_Port = Generalization(general=Port, specific=sam_DataPort)
gen_sam_InControlPort_ControlPort = Generalization(general=ControlPort, specific=sam_InControlPort)
gen_sam_InControlPort_InputPort = Generalization(general=InputPort, specific=sam_InControlPort)
gen_sam_OutControlPort_ControlPort = Generalization(general=ControlPort, specific=sam_OutControlPort)
gen_sam_OutControlPort_OutputPort = Generalization(general=OutputPort, specific=sam_OutControlPort)
gen_sam_OutDataPort_DataPort = Generalization(general=DataPort, specific=sam_OutDataPort)
gen_sam_OutDataPort_OutputPort = Generalization(general=OutputPort, specific=sam_OutDataPort)
gen_sam_InDataPort_DataPort = Generalization(general=DataPort, specific=sam_InDataPort)
gen_sam_InDataPort_InputPort = Generalization(general=InputPort, specific=sam_InDataPort)
gen_sam_InputPort_Port = Generalization(general=Port, specific=sam_InputPort)
gen_sam_OutputPort_Port = Generalization(general=Port, specific=sam_OutputPort)
gen_sam_Port_NamedItem = Generalization(general=NamedItem, specific=sam_Port)
gen_sam_DataStore_NamedItem = Generalization(general=NamedItem, specific=sam_DataStore)
gen_sam_DataComposition_DataSynchronisation = Generalization(general=DataSynchronisation, specific=sam_DataComposition)
gen_sam_ControlFlow_Flow = Generalization(general=Flow, specific=sam_ControlFlow)
gen_sam_DataFlow_Flow = Generalization(general=Flow, specific=sam_DataFlow)
gen_sam_System_ModelContent = Generalization(general=ModelContent, specific=sam_System)
gen_sam_System_TraceableElement = Generalization(general=TraceableElement, specific=sam_System)
gen_sam_DataDecomposition_DataSynchronisation = Generalization(general=DataSynchronisation, specific=sam_DataDecomposition)
gen_sam_Flow_NamedItem = Generalization(general=NamedItem, specific=sam_Flow)
gen_sam_ModelContent_NamedItem = Generalization(general=NamedItem, specific=sam_ModelContent)
gen_sam_MultiPort_NamedItem = Generalization(general=NamedItem, specific=sam_MultiPort)
gen_sam_MessagePort_Port = Generalization(general=Port, specific=sam_MessagePort)
gen_sam_IdentifiedItem_EModelElement = Generalization(general=EModelElement, specific=sam_IdentifiedItem)
gen_sam_NamedItem_IdentifiedItem = Generalization(general=IdentifiedItem, specific=sam_NamedItem)
gen_sam_InMessagePort_MessagePort = Generalization(general=MessagePort, specific=sam_InMessagePort)
gen_sam_InMessagePort_InputPort = Generalization(general=InputPort, specific=sam_InMessagePort)
gen_sam_FlowGroup_ENamedElement = Generalization(general=ENamedElement, specific=sam_FlowGroup)
gen_sam_MessageFlow_Flow = Generalization(general=Flow, specific=sam_MessageFlow)
gen_sam_OutMessagePort_MessagePort = Generalization(general=MessagePort, specific=sam_OutMessagePort)
gen_sam_OutMessagePort_OutputPort = Generalization(general=OutputPort, specific=sam_OutMessagePort)
gen_sam_AsynchronousGate_Gate = Generalization(general=Gate, specific=sam_AsynchronousGate)
gen_sam_SynchronousGate_Gate = Generalization(general=Gate, specific=sam_SynchronousGate)
gen_sam_DataSynchronisation_SynchronousGate = Generalization(general=SynchronousGate, specific=sam_DataSynchronisation)
gen_sam_Gate_IdentifiedItem = Generalization(general=IdentifiedItem, specific=sam_Gate)
gen_sam_DataMerge_MergeGate = Generalization(general=MergeGate, specific=sam_DataMerge)
gen_sam_SplitGate_AsynchronousGate = Generalization(general=AsynchronousGate, specific=sam_SplitGate)
gen_sam_MergeGate_AsynchronousGate = Generalization(general=AsynchronousGate, specific=sam_MergeGate)
gen_sam_MessageSplit_SplitGate = Generalization(general=SplitGate, specific=sam_MessageSplit)
gen_sam_MessageMerge_MergeGate = Generalization(general=MergeGate, specific=sam_MessageMerge)
gen_sam_TraceableElement_NamedItem = Generalization(general=NamedItem, specific=sam_TraceableElement)
gen_sam_ControlMerge_MergeGate = Generalization(general=MergeGate, specific=sam_ControlMerge)

# Domain Model
domain_model = DomainModel(
    name="sam",
    types={sam_Automaton, sam_Transition, sam_AbstractState, NamedItem, sam_MacroState, ModelContent, sam_Port, sam_State, TraceableElement, sam_InitialState, State, AbstractState, sam_ControlPort, Port, sam_DataPort, sam_InControlPort, ControlPort, InputPort, sam_ControlMerge, sam_OutControlPort, OutputPort, sam_MessageSplit, sam_OutDataPort, sam_InDataPort, DataPort, sam_DataStore, sam_DataSynchronisation, sam_DataMerge, sam_InputPort, sam_System, sam_Flow, sam_MultiPort, sam_OutputPort, sam_DataComposition, DataSynchronisation, sam_ControlFlow, Flow, sam_DataFlow, sam_FlowGroup, sam_DataDecomposition, sam_Model, sam_EObject, sam_Gate, sam_ModelContent, sam_MessagePort, sam_IdentifiedItem, EModelElement, sam_NamedItem, IdentifiedItem, sam_InMessagePort, ENamedElement, sam_MessageFlow, sam_OutMessagePort, MessagePort, sam_MessageMerge, sam_AsynchronousGate, Gate, sam_SynchronousGate, SynchronousGate, MergeGate, sam_SplitGate, AsynchronousGate, sam_MergeGate, SplitGate, sam_TraceableElement, DataType},
    associations={parentState0, parentAutomaton1, listPorts5, listStates7, isInstanceOf10, outlink2, listTransitions3, inlink13, composition11, merge20, dest15, parentAutomaton16, source18, split27, merge28, parentDataStore30, parentDataStore21, parentSync23, merge25, parentSystem41, outlink42, inlink43, parentAutomaton46, parentMultiPort49, parentSync33, split36, merge38, source58, dest59, parentSystem62, isInstanceOf52, source54, dest55, parentSystem67, group69, listPorts70, in64, out65, modelContent83, flowGroups85, requirementModel87, listStores72, listSynchronisation75, listFlows77, listElements79, isInstanceOf82, listPort92, parent95, isInstanceOf98, parentModel88, parentSystem89, listMultiPort91, merge104, split106, merge109, source100, dest101, in118, flows112, model114, parentSystem116, in123, outData124, outControl127, in129, out120, in139, out142, out131, in134, out136},
    generalizations={gen_sam_AbstractState_NamedItem, gen_sam_Automaton_ModelContent, gen_sam_State_AbstractState, gen_sam_Transition_TraceableElement, gen_sam_InitialState_State, gen_sam_MacroState_AbstractState, gen_sam_ControlPort_Port, gen_sam_DataPort_Port, gen_sam_InControlPort_ControlPort, gen_sam_InControlPort_InputPort, gen_sam_OutControlPort_ControlPort, gen_sam_OutControlPort_OutputPort, gen_sam_OutDataPort_DataPort, gen_sam_OutDataPort_OutputPort, gen_sam_InDataPort_DataPort, gen_sam_InDataPort_InputPort, gen_sam_InputPort_Port, gen_sam_OutputPort_Port, gen_sam_Port_NamedItem, gen_sam_DataStore_NamedItem, gen_sam_DataComposition_DataSynchronisation, gen_sam_ControlFlow_Flow, gen_sam_DataFlow_Flow, gen_sam_System_ModelContent, gen_sam_System_TraceableElement, gen_sam_DataDecomposition_DataSynchronisation, gen_sam_Flow_NamedItem, gen_sam_ModelContent_NamedItem, gen_sam_MultiPort_NamedItem, gen_sam_MessagePort_Port, gen_sam_IdentifiedItem_EModelElement, gen_sam_NamedItem_IdentifiedItem, gen_sam_InMessagePort_MessagePort, gen_sam_InMessagePort_InputPort, gen_sam_FlowGroup_ENamedElement, gen_sam_MessageFlow_Flow, gen_sam_OutMessagePort_MessagePort, gen_sam_OutMessagePort_OutputPort, gen_sam_AsynchronousGate_Gate, gen_sam_SynchronousGate_Gate, gen_sam_DataSynchronisation_SynchronousGate, gen_sam_Gate_IdentifiedItem, gen_sam_DataMerge_MergeGate, gen_sam_SplitGate_AsynchronousGate, gen_sam_MergeGate_AsynchronousGate, gen_sam_MessageSplit_SplitGate, gen_sam_MessageMerge_MergeGate, gen_sam_TraceableElement_NamedItem, gen_sam_ControlMerge_MergeGate},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)