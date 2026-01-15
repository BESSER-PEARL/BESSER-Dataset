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
DecompositionType: Enumeration = Enumeration(
    name="DecompositionType",
    literals={
            EnumerationLiteral(name="EXCLUSIVE_OR"),
			EnumerationLiteral(name="PARALLEL_AND")
    }
)

# Classes
simulink_SimulinkModel = Class(name="simulink::SimulinkModel")
SubSystem = Class(name="SubSystem")
simulink_SimulinkElement = Class(name="simulink::SimulinkElement", is_abstract=True)
simulink_Block = Class(name="simulink::Block")
SimulinkElement = Class(name="SimulinkElement")
simulink_Port = Class(name="simulink::Port", is_abstract=True)
simulink_SubSystem = Class(name="simulink::SubSystem")
simulink_PortBlock = Class(name="simulink::PortBlock", is_abstract=True)
simulink_InPort = Class(name="simulink::InPort")
Port = Class(name="Port")
simulink_Connection = Class(name="simulink::Connection")
simulink_OutPort = Class(name="simulink::OutPort")
Block = Class(name="Block")
simulink_InPortBlock = Class(name="simulink::InPortBlock")
PortBlock = Class(name="PortBlock")
simulink_OutPortBlock = Class(name="simulink::OutPortBlock")
simulink_Chart = Class(name="simulink::Chart")
CompositeStateflowElement = Class(name="CompositeStateflowElement")
simulink_Vertex = Class(name="simulink::Vertex", is_abstract=True)
ContainableStateflowElement = Class(name="ContainableStateflowElement")
simulink_Transition = Class(name="simulink::Transition")
simulink_State = Class(name="simulink::State")
Vertex = Class(name="Vertex")
simulink_Action = Class(name="simulink::Action")
simulink_Junction = Class(name="simulink::Junction")
simulink_SFWGuard = Class(name="simulink::SFWGuard")
simulink_SFWTrigger = Class(name="simulink::SFWTrigger")
simulink_StateflowElement = Class(name="simulink::StateflowElement", is_abstract=True)
simulink_Function = Class(name="simulink::Function")
simulink_CompositeStateflowElement = Class(name="simulink::CompositeStateflowElement", is_abstract=True)
StateflowElement = Class(name="StateflowElement")
simulink_ContainableStateflowElement = Class(name="simulink::ContainableStateflowElement", is_abstract=True)
simulink_TruthTable = Class(name="simulink::TruthTable", is_abstract=True)
simulink_ConditionTable = Class(name="simulink::ConditionTable")
simulink_ActionTable = Class(name="simulink::ActionTable")
simulink_Data = Class(name="simulink::Data", is_abstract=True)
simulink_Decision = Class(name="simulink::Decision")
simulink_Condition = Class(name="simulink::Condition")
simulink_ActionEntry = Class(name="simulink::ActionEntry")
simulink_DecisionEntry = Class(name="simulink::DecisionEntry")
simulink_ContainableTruthTable = Class(name="simulink::ContainableTruthTable")
TruthTable = Class(name="TruthTable")
simulink_TruthTableChart = Class(name="simulink::TruthTableChart")
simulink_InputData = Class(name="simulink::InputData")
Data = Class(name="Data")
InPort = Class(name="InPort")
simulink_OutputData = Class(name="simulink::OutputData")
OutPort = Class(name="OutPort")
simulink_LocalData = Class(name="simulink::LocalData")
simulink_BlockReference = Class(name="simulink::BlockReference")
Reference = Class(name="Reference")
simulink_Reference = Class(name="simulink::Reference", is_abstract=True)
simulink_ModelReference = Class(name="simulink::ModelReference")

# simulink_SimulinkModel class attributes and methods
simulink_SimulinkModel_file: Property = Property(name="file", type=StringType)
simulink_SimulinkModel_isLibrary: Property = Property(name="isLibrary", type=BooleanType)
simulink_SimulinkModel.attributes={simulink_SimulinkModel_file, simulink_SimulinkModel_isLibrary}

# SubSystem class attributes and methods

# simulink_SimulinkElement class attributes and methods
simulink_SimulinkElement_name: Property = Property(name="name", type=StringType)
simulink_SimulinkElement_handle: Property = Property(name="handle", type=StringType)
simulink_SimulinkElement.attributes={simulink_SimulinkElement_handle, simulink_SimulinkElement_name}

# simulink_Block class attributes and methods

# SimulinkElement class attributes and methods

# simulink_Port class attributes and methods
simulink_Port_dataType: Property = Property(name="dataType", type=StringType)
simulink_Port_portNumber: Property = Property(name="portNumber", type=IntegerType)
simulink_Port.attributes={simulink_Port_portNumber, simulink_Port_dataType}

# simulink_SubSystem class attributes and methods

# simulink_PortBlock class attributes and methods
simulink_PortBlock_portNumber: Property = Property(name="portNumber", type=IntegerType)
simulink_PortBlock.attributes={simulink_PortBlock_portNumber}

# simulink_InPort class attributes and methods

# Port class attributes and methods

# simulink_Connection class attributes and methods

# simulink_OutPort class attributes and methods

# Block class attributes and methods

# simulink_InPortBlock class attributes and methods

# PortBlock class attributes and methods

# simulink_OutPortBlock class attributes and methods

# simulink_Chart class attributes and methods
simulink_Chart_decomposition: Property = Property(name="decomposition", type=StringType)
simulink_Chart.attributes={simulink_Chart_decomposition}

# CompositeStateflowElement class attributes and methods

# simulink_Vertex class attributes and methods

# ContainableStateflowElement class attributes and methods

# simulink_Transition class attributes and methods
simulink_Transition_isDefaultTransition: Property = Property(name="isDefaultTransition", type=BooleanType)
simulink_Transition_executionOrder: Property = Property(name="executionOrder", type=IntegerType)
simulink_Transition.attributes={simulink_Transition_isDefaultTransition, simulink_Transition_executionOrder}

# simulink_State class attributes and methods
simulink_State_decomposition: Property = Property(name="decomposition", type=StringType)
simulink_State_executionOrder: Property = Property(name="executionOrder", type=IntegerType)
simulink_State.attributes={simulink_State_executionOrder, simulink_State_decomposition}

# Vertex class attributes and methods

# simulink_Action class attributes and methods
simulink_Action_statement: Property = Property(name="statement", type=StringType)
simulink_Action.attributes={simulink_Action_statement}

# simulink_Junction class attributes and methods

# simulink_SFWGuard class attributes and methods
simulink_SFWGuard_statement: Property = Property(name="statement", type=StringType)
simulink_SFWGuard.attributes={simulink_SFWGuard_statement}

# simulink_SFWTrigger class attributes and methods
simulink_SFWTrigger_statement: Property = Property(name="statement", type=StringType)
simulink_SFWTrigger.attributes={simulink_SFWTrigger_statement}

# simulink_StateflowElement class attributes and methods
simulink_StateflowElement_path: Property = Property(name="path", type=StringType)
simulink_StateflowElement_id: Property = Property(name="id", type=IntegerType)
simulink_StateflowElement.attributes={simulink_StateflowElement_path, simulink_StateflowElement_id}

# simulink_Function class attributes and methods
simulink_Function_signature: Property = Property(name="signature", type=StringType)
simulink_Function.attributes={simulink_Function_signature}

# simulink_CompositeStateflowElement class attributes and methods

# StateflowElement class attributes and methods

# simulink_ContainableStateflowElement class attributes and methods

# simulink_TruthTable class attributes and methods

# simulink_ConditionTable class attributes and methods

# simulink_ActionTable class attributes and methods

# simulink_Data class attributes and methods

# simulink_Decision class attributes and methods
simulink_Decision_actionReference: Property = Property(name="actionReference", type=StringType)
simulink_Decision_id: Property = Property(name="id", type=IntegerType)
simulink_Decision.attributes={simulink_Decision_id, simulink_Decision_actionReference}

# simulink_Condition class attributes and methods
simulink_Condition_description: Property = Property(name="description", type=StringType)
simulink_Condition_statement: Property = Property(name="statement", type=StringType)
simulink_Condition.attributes={simulink_Condition_description, simulink_Condition_statement}

# simulink_ActionEntry class attributes and methods
simulink_ActionEntry_actionReference: Property = Property(name="actionReference", type=StringType)
simulink_ActionEntry_description: Property = Property(name="description", type=StringType)
simulink_ActionEntry_actionStatement: Property = Property(name="actionStatement", type=StringType)
simulink_ActionEntry.attributes={simulink_ActionEntry_description, simulink_ActionEntry_actionReference, simulink_ActionEntry_actionStatement}

# simulink_DecisionEntry class attributes and methods
simulink_DecisionEntry_conditionOutcome: Property = Property(name="conditionOutcome", type=StringType)
simulink_DecisionEntry.attributes={simulink_DecisionEntry_conditionOutcome}

# simulink_ContainableTruthTable class attributes and methods

# TruthTable class attributes and methods

# simulink_TruthTableChart class attributes and methods

# simulink_InputData class attributes and methods

# Data class attributes and methods

# InPort class attributes and methods

# simulink_OutputData class attributes and methods

# OutPort class attributes and methods

# simulink_LocalData class attributes and methods
simulink_LocalData_dataType: Property = Property(name="dataType", type=StringType)
simulink_LocalData.attributes={simulink_LocalData_dataType}

# simulink_BlockReference class attributes and methods

# Reference class attributes and methods

# simulink_Reference class attributes and methods

# simulink_ModelReference class attributes and methods
simulink_ModelReference_modelName: Property = Property(name="modelName", type=StringType)
simulink_ModelReference.attributes={simulink_ModelReference_modelName}

# Relationships
ownedPorts0: BinaryAssociation = BinaryAssociation(
    name="ownedPorts0",
    ends={
        Property(name="Port", type=simulink_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="block", type=simulink_Port, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent1: BinaryAssociation = BinaryAssociation(
    name="parent1",
    ends={
        Property(name="SubSystem", type=simulink_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="subBlocks", type=simulink_SubSystem, multiplicity=Multiplicity(0, 1))
    }
)
block2: BinaryAssociation = BinaryAssociation(
    name="block2",
    ends={
        Property(name="Block", type=simulink_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedPorts", type=simulink_Block, multiplicity=Multiplicity(0, 1))
    }
)
portBlock3: BinaryAssociation = BinaryAssociation(
    name="portBlock3",
    ends={
        Property(name="PortBlock", type=simulink_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="port", type=simulink_PortBlock, multiplicity=Multiplicity(0, 1))
    }
)
connection4: BinaryAssociation = BinaryAssociation(
    name="connection4",
    ends={
        Property(name="Connection", type=simulink_InPort, multiplicity=Multiplicity(1, 1)),
        Property(name="to", type=simulink_Connection, multiplicity=Multiplicity(0, 1))
    }
)
connection5: BinaryAssociation = BinaryAssociation(
    name="connection5",
    ends={
        Property(name="Connection6", type=simulink_OutPort, multiplicity=Multiplicity(1, 1)),
        Property(name="from", type=simulink_Connection, multiplicity=Multiplicity(0, 1))
    }
)
subBlocks7: BinaryAssociation = BinaryAssociation(
    name="subBlocks7",
    ends={
        Property(name="Block8", type=simulink_SubSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=simulink_Block, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connections9: BinaryAssociation = BinaryAssociation(
    name="connections9",
    ends={
        Property(name="simulink_Connection", type=simulink_SubSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="simulink_SubSystem", type=simulink_Connection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
port10: BinaryAssociation = BinaryAssociation(
    name="port10",
    ends={
        Property(name="Port11", type=simulink_PortBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="portBlock", type=simulink_Port, multiplicity=Multiplicity(0, 1))
    }
)
from12: BinaryAssociation = BinaryAssociation(
    name="from12",
    ends={
        Property(name="OutPort", type=simulink_Connection, multiplicity=Multiplicity(1, 1)),
        Property(name="connection", type=simulink_OutPort, multiplicity=Multiplicity(0, 1))
    }
)
to13: BinaryAssociation = BinaryAssociation(
    name="to13",
    ends={
        Property(name="InPort", type=simulink_Connection, multiplicity=Multiplicity(1, 1)),
        Property(name="connection14", type=simulink_InPort, multiplicity=Multiplicity(0, 1))
    }
)
incomingTransitions15: BinaryAssociation = BinaryAssociation(
    name="incomingTransitions15",
    ends={
        Property(name="Transition", type=simulink_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="destination", type=simulink_Transition, multiplicity=Multiplicity(1, 9999))
    }
)
outgoingTransitions16: BinaryAssociation = BinaryAssociation(
    name="outgoingTransitions16",
    ends={
        Property(name="Transition17", type=simulink_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=simulink_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
entryActions18: BinaryAssociation = BinaryAssociation(
    name="entryActions18",
    ends={
        Property(name="Action", type=simulink_State, multiplicity=Multiplicity(1, 1)),
        Property(name="stateEntry", type=simulink_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
duringActions19: BinaryAssociation = BinaryAssociation(
    name="duringActions19",
    ends={
        Property(name="Action20", type=simulink_State, multiplicity=Multiplicity(1, 1)),
        Property(name="stateDuring", type=simulink_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exitActions21: BinaryAssociation = BinaryAssociation(
    name="exitActions21",
    ends={
        Property(name="Action22", type=simulink_State, multiplicity=Multiplicity(1, 1)),
        Property(name="stateExit", type=simulink_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source23: BinaryAssociation = BinaryAssociation(
    name="source23",
    ends={
        Property(name="Vertex", type=simulink_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingTransitions", type=simulink_Vertex, multiplicity=Multiplicity(0, 1))
    }
)
destination24: BinaryAssociation = BinaryAssociation(
    name="destination24",
    ends={
        Property(name="Vertex25", type=simulink_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingTransitions", type=simulink_Vertex, multiplicity=Multiplicity(1, 1))
    }
)
guard26: BinaryAssociation = BinaryAssociation(
    name="guard26",
    ends={
        Property(name="SFWGuard", type=simulink_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transition", type=simulink_SFWGuard, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
triggeredActions27: BinaryAssociation = BinaryAssociation(
    name="triggeredActions27",
    ends={
        Property(name="Action29", type=simulink_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transition28", type=simulink_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
trigger30: BinaryAssociation = BinaryAssociation(
    name="trigger30",
    ends={
        Property(name="SFWTrigger", type=simulink_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transition31", type=simulink_SFWTrigger, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
transition32: BinaryAssociation = BinaryAssociation(
    name="transition32",
    ends={
        Property(name="Transition33", type=simulink_SFWGuard, multiplicity=Multiplicity(1, 1)),
        Property(name="guard", type=simulink_Transition, multiplicity=Multiplicity(0, 1))
    }
)
transition34: BinaryAssociation = BinaryAssociation(
    name="transition34",
    ends={
        Property(name="Transition35", type=simulink_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="triggeredActions", type=simulink_Transition, multiplicity=Multiplicity(0, 1))
    }
)
stateEntry36: BinaryAssociation = BinaryAssociation(
    name="stateEntry36",
    ends={
        Property(name="State", type=simulink_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="entryActions", type=simulink_State, multiplicity=Multiplicity(0, 1))
    }
)
stateDuring37: BinaryAssociation = BinaryAssociation(
    name="stateDuring37",
    ends={
        Property(name="State38", type=simulink_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="duringActions", type=simulink_State, multiplicity=Multiplicity(0, 1))
    }
)
stateExit39: BinaryAssociation = BinaryAssociation(
    name="stateExit39",
    ends={
        Property(name="State40", type=simulink_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="exitActions", type=simulink_State, multiplicity=Multiplicity(0, 1))
    }
)
children41: BinaryAssociation = BinaryAssociation(
    name="children41",
    ends={
        Property(name="ContainableStateflowElement", type=simulink_CompositeStateflowElement, multiplicity=Multiplicity(1, 1)),
        Property(name="parent42", type=simulink_ContainableStateflowElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent43: BinaryAssociation = BinaryAssociation(
    name="parent43",
    ends={
        Property(name="CompositeStateflowElement", type=simulink_ContainableStateflowElement, multiplicity=Multiplicity(1, 1)),
        Property(name="children", type=simulink_CompositeStateflowElement, multiplicity=Multiplicity(0, 1))
    }
)
conditionTable44: BinaryAssociation = BinaryAssociation(
    name="conditionTable44",
    ends={
        Property(name="simulink_ConditionTable", type=simulink_TruthTable, multiplicity=Multiplicity(1, 1)),
        Property(name="simulink_TruthTable", type=simulink_ConditionTable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
actionTable45: BinaryAssociation = BinaryAssociation(
    name="actionTable45",
    ends={
        Property(name="simulink_ActionTable", type=simulink_TruthTable, multiplicity=Multiplicity(1, 1)),
        Property(name="simulink_TruthTable46", type=simulink_ActionTable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
data47: BinaryAssociation = BinaryAssociation(
    name="data47",
    ends={
        Property(name="simulink_Data", type=simulink_TruthTable, multiplicity=Multiplicity(1, 1)),
        Property(name="simulink_TruthTable48", type=simulink_Data, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
decisions49: BinaryAssociation = BinaryAssociation(
    name="decisions49",
    ends={
        Property(name="simulink_Decision", type=simulink_ConditionTable, multiplicity=Multiplicity(1, 1)),
        Property(name="simulink_ConditionTable50", type=simulink_Decision, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
conditions51: BinaryAssociation = BinaryAssociation(
    name="conditions51",
    ends={
        Property(name="simulink_Condition", type=simulink_ConditionTable, multiplicity=Multiplicity(1, 1)),
        Property(name="simulink_ConditionTable52", type=simulink_Condition, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
actionEntries53: BinaryAssociation = BinaryAssociation(
    name="actionEntries53",
    ends={
        Property(name="simulink_ActionEntry", type=simulink_ActionTable, multiplicity=Multiplicity(1, 1)),
        Property(name="simulink_ActionTable54", type=simulink_ActionEntry, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
decisionEntries55: BinaryAssociation = BinaryAssociation(
    name="decisionEntries55",
    ends={
        Property(name="simulink_DecisionEntry", type=simulink_Decision, multiplicity=Multiplicity(1, 1)),
        Property(name="simulink_Decision56", type=simulink_DecisionEntry, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
condition57: BinaryAssociation = BinaryAssociation(
    name="condition57",
    ends={
        Property(name="simulink_Condition59", type=simulink_DecisionEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="simulink_DecisionEntry58", type=simulink_Condition, multiplicity=Multiplicity(1, 1))
    }
)
transition60: BinaryAssociation = BinaryAssociation(
    name="transition60",
    ends={
        Property(name="Transition61", type=simulink_SFWTrigger, multiplicity=Multiplicity(1, 1)),
        Property(name="trigger", type=simulink_Transition, multiplicity=Multiplicity(0, 1))
    }
)
sourceBlock62: BinaryAssociation = BinaryAssociation(
    name="sourceBlock62",
    ends={
        Property(name="simulink_Block", type=simulink_Reference, multiplicity=Multiplicity(1, 1)),
        Property(name="simulink_Reference", type=simulink_Block, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_simulink_OutPort_Port = Generalization(general=Port, specific=simulink_OutPort)
gen_simulink_SimulinkModel_SubSystem = Generalization(general=SubSystem, specific=simulink_SimulinkModel)
gen_simulink_Block_SimulinkElement = Generalization(general=SimulinkElement, specific=simulink_Block)
gen_simulink_Port_SimulinkElement = Generalization(general=SimulinkElement, specific=simulink_Port)
gen_simulink_InPort_Port = Generalization(general=Port, specific=simulink_InPort)
gen_simulink_SubSystem_Block = Generalization(general=Block, specific=simulink_SubSystem)
gen_simulink_PortBlock_Block = Generalization(general=Block, specific=simulink_PortBlock)
gen_simulink_InPortBlock_PortBlock = Generalization(general=PortBlock, specific=simulink_InPortBlock)
gen_simulink_OutPortBlock_PortBlock = Generalization(general=PortBlock, specific=simulink_OutPortBlock)
gen_simulink_Connection_SimulinkElement = Generalization(general=SimulinkElement, specific=simulink_Connection)
gen_simulink_Chart_CompositeStateflowElement = Generalization(general=CompositeStateflowElement, specific=simulink_Chart)
gen_simulink_Chart_Block = Generalization(general=Block, specific=simulink_Chart)
gen_simulink_Vertex_ContainableStateflowElement = Generalization(general=ContainableStateflowElement, specific=simulink_Vertex)
gen_simulink_State_Vertex = Generalization(general=Vertex, specific=simulink_State)
gen_simulink_State_CompositeStateflowElement = Generalization(general=CompositeStateflowElement, specific=simulink_State)
gen_simulink_Junction_Vertex = Generalization(general=Vertex, specific=simulink_Junction)
gen_simulink_Transition_ContainableStateflowElement = Generalization(general=ContainableStateflowElement, specific=simulink_Transition)
gen_simulink_StateflowElement_SimulinkElement = Generalization(general=SimulinkElement, specific=simulink_StateflowElement)
gen_simulink_Function_CompositeStateflowElement = Generalization(general=CompositeStateflowElement, specific=simulink_Function)
gen_simulink_Function_ContainableStateflowElement = Generalization(general=ContainableStateflowElement, specific=simulink_Function)
gen_simulink_CompositeStateflowElement_StateflowElement = Generalization(general=StateflowElement, specific=simulink_CompositeStateflowElement)
gen_simulink_ContainableStateflowElement_StateflowElement = Generalization(general=StateflowElement, specific=simulink_ContainableStateflowElement)
gen_simulink_TruthTable_StateflowElement = Generalization(general=StateflowElement, specific=simulink_TruthTable)
gen_simulink_ContainableTruthTable_TruthTable = Generalization(general=TruthTable, specific=simulink_ContainableTruthTable)
gen_simulink_ContainableTruthTable_ContainableStateflowElement = Generalization(general=ContainableStateflowElement, specific=simulink_ContainableTruthTable)
gen_simulink_TruthTableChart_TruthTable = Generalization(general=TruthTable, specific=simulink_TruthTableChart)
gen_simulink_TruthTableChart_Block = Generalization(general=Block, specific=simulink_TruthTableChart)
gen_simulink_Data_ContainableStateflowElement = Generalization(general=ContainableStateflowElement, specific=simulink_Data)
gen_simulink_InputData_Data = Generalization(general=Data, specific=simulink_InputData)
gen_simulink_InputData_InPort = Generalization(general=InPort, specific=simulink_InputData)
gen_simulink_OutputData_Data = Generalization(general=Data, specific=simulink_OutputData)
gen_simulink_OutputData_OutPort = Generalization(general=OutPort, specific=simulink_OutputData)
gen_simulink_LocalData_Data = Generalization(general=Data, specific=simulink_LocalData)
gen_simulink_BlockReference_Reference = Generalization(general=Reference, specific=simulink_BlockReference)
gen_simulink_Reference_SubSystem = Generalization(general=SubSystem, specific=simulink_Reference)
gen_simulink_ModelReference_Reference = Generalization(general=Reference, specific=simulink_ModelReference)

# Domain Model
domain_model = DomainModel(
    name="simulink",
    types={simulink_SimulinkModel, SubSystem, simulink_SimulinkElement, simulink_Block, SimulinkElement, simulink_Port, simulink_SubSystem, simulink_PortBlock, simulink_InPort, Port, simulink_Connection, simulink_OutPort, Block, simulink_InPortBlock, PortBlock, simulink_OutPortBlock, simulink_Chart, CompositeStateflowElement, simulink_Vertex, ContainableStateflowElement, simulink_Transition, simulink_State, Vertex, simulink_Action, simulink_Junction, simulink_SFWGuard, simulink_SFWTrigger, simulink_StateflowElement, simulink_Function, simulink_CompositeStateflowElement, StateflowElement, simulink_ContainableStateflowElement, simulink_TruthTable, simulink_ConditionTable, simulink_ActionTable, simulink_Data, simulink_Decision, simulink_Condition, simulink_ActionEntry, simulink_DecisionEntry, simulink_ContainableTruthTable, TruthTable, simulink_TruthTableChart, simulink_InputData, Data, InPort, simulink_OutputData, OutPort, simulink_LocalData, simulink_BlockReference, Reference, simulink_Reference, simulink_ModelReference, DecompositionType},
    associations={ownedPorts0, parent1, block2, portBlock3, connection4, connection5, subBlocks7, connections9, port10, from12, to13, incomingTransitions15, outgoingTransitions16, entryActions18, duringActions19, exitActions21, source23, destination24, guard26, triggeredActions27, trigger30, transition32, transition34, stateEntry36, stateDuring37, stateExit39, children41, parent43, conditionTable44, actionTable45, data47, decisions49, conditions51, actionEntries53, decisionEntries55, condition57, transition60, sourceBlock62},
    generalizations={gen_simulink_OutPort_Port, gen_simulink_SimulinkModel_SubSystem, gen_simulink_Block_SimulinkElement, gen_simulink_Port_SimulinkElement, gen_simulink_InPort_Port, gen_simulink_SubSystem_Block, gen_simulink_PortBlock_Block, gen_simulink_InPortBlock_PortBlock, gen_simulink_OutPortBlock_PortBlock, gen_simulink_Connection_SimulinkElement, gen_simulink_Chart_CompositeStateflowElement, gen_simulink_Chart_Block, gen_simulink_Vertex_ContainableStateflowElement, gen_simulink_State_Vertex, gen_simulink_State_CompositeStateflowElement, gen_simulink_Junction_Vertex, gen_simulink_Transition_ContainableStateflowElement, gen_simulink_StateflowElement_SimulinkElement, gen_simulink_Function_CompositeStateflowElement, gen_simulink_Function_ContainableStateflowElement, gen_simulink_CompositeStateflowElement_StateflowElement, gen_simulink_ContainableStateflowElement_StateflowElement, gen_simulink_TruthTable_StateflowElement, gen_simulink_ContainableTruthTable_TruthTable, gen_simulink_ContainableTruthTable_ContainableStateflowElement, gen_simulink_TruthTableChart_TruthTable, gen_simulink_TruthTableChart_Block, gen_simulink_Data_ContainableStateflowElement, gen_simulink_InputData_Data, gen_simulink_InputData_InPort, gen_simulink_OutputData_Data, gen_simulink_OutputData_OutPort, gen_simulink_LocalData_Data, gen_simulink_BlockReference_Reference, gen_simulink_Reference_SubSystem, gen_simulink_ModelReference_Reference},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)