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
sam_Port = Class(name="sam::Port", is_abstract=True)
sam_AbstractState = Class(name="sam::AbstractState", is_abstract=True)
NamedItem = Class(name="NamedItem")
sam_InitialState = Class(name="sam::InitialState")
State = Class(name="State")
sam_MacroState = Class(name="sam::MacroState")
sam_Automaton = Class(name="sam::Automaton")
sam_Transition = Class(name="sam::Transition")
ModelContent = Class(name="ModelContent")
sam_ControlPort = Class(name="sam::ControlPort", is_abstract=True)
Port = Class(name="Port")
AbstractState = Class(name="AbstractState")
sam_State = Class(name="sam::State")
IdentifiedItem = Class(name="IdentifiedItem")
sam_OutControlPort = Class(name="sam::OutControlPort")
OutputPort = Class(name="OutputPort")
sam_OutDataPort = Class(name="sam::OutDataPort")
sam_DataPort = Class(name="sam::DataPort", is_abstract=True)
sam_InControlPort = Class(name="sam::InControlPort")
ControlPort = Class(name="ControlPort")
InputPort = Class(name="InputPort")
sam_InDataPort = Class(name="sam::InDataPort")
DataPort = Class(name="DataPort")
sam_SynchronisationGate = Class(name="sam::SynchronisationGate", is_abstract=True)
sam_DataStore = Class(name="sam::DataStore")
sam_InputPort = Class(name="sam::InputPort", is_abstract=True)
sam_MultiPort = Class(name="sam::MultiPort")
sam_Composition = Class(name="sam::Composition")
SynchronisationGate = Class(name="SynchronisationGate")
sam_ControlFlow = Class(name="sam::ControlFlow")
Flow = Class(name="Flow")
sam_OutputPort = Class(name="sam::OutputPort", is_abstract=True)
sam_System = Class(name="sam::System")
sam_Flow = Class(name="sam::Flow", is_abstract=True)
sam_DataFlow = Class(name="sam::DataFlow")
sam_Decomposition = Class(name="sam::Decomposition")
sam_ModelContent = Class(name="sam::ModelContent", is_abstract=True)
sam_IdentifiedItem = Class(name="sam::IdentifiedItem", is_abstract=True)
EModelElement = Class(name="EModelElement")
sam_Model = Class(name="sam::Model")
sam_NamedItem = Class(name="sam::NamedItem", is_abstract=True)

# sam_Port class attributes and methods

# sam_AbstractState class attributes and methods

# NamedItem class attributes and methods

# sam_InitialState class attributes and methods

# State class attributes and methods

# sam_MacroState class attributes and methods

# sam_Automaton class attributes and methods

# sam_Transition class attributes and methods
sam_Transition_condition: Property = Property(name="condition", type=StringType)
sam_Transition_emission: Property = Property(name="emission", type=StringType)
sam_Transition_priority: Property = Property(name="priority", type=StringType)
sam_Transition.attributes={sam_Transition_priority, sam_Transition_condition, sam_Transition_emission}

# ModelContent class attributes and methods

# sam_ControlPort class attributes and methods

# Port class attributes and methods

# AbstractState class attributes and methods

# sam_State class attributes and methods

# IdentifiedItem class attributes and methods

# sam_OutControlPort class attributes and methods

# OutputPort class attributes and methods

# sam_OutDataPort class attributes and methods

# sam_DataPort class attributes and methods

# sam_InControlPort class attributes and methods

# ControlPort class attributes and methods

# InputPort class attributes and methods

# sam_InDataPort class attributes and methods

# DataPort class attributes and methods

# sam_SynchronisationGate class attributes and methods

# sam_DataStore class attributes and methods

# sam_InputPort class attributes and methods

# sam_MultiPort class attributes and methods

# sam_Composition class attributes and methods

# SynchronisationGate class attributes and methods

# sam_ControlFlow class attributes and methods

# Flow class attributes and methods

# sam_OutputPort class attributes and methods

# sam_System class attributes and methods

# sam_Flow class attributes and methods

# sam_DataFlow class attributes and methods
sam_DataFlow_type: Property = Property(name="type", type=StringType)
sam_DataFlow.attributes={sam_DataFlow_type}

# sam_Decomposition class attributes and methods

# sam_ModelContent class attributes and methods

# sam_IdentifiedItem class attributes and methods
sam_IdentifiedItem_comment: Property = Property(name="comment", type=StringType)
sam_IdentifiedItem_requirements: Property = Property(name="requirements", type=StringType)
sam_IdentifiedItem.attributes={sam_IdentifiedItem_comment, sam_IdentifiedItem_requirements}

# EModelElement class attributes and methods

# sam_Model class attributes and methods

# sam_NamedItem class attributes and methods
sam_NamedItem_name: Property = Property(name="name", type=StringType)
sam_NamedItem.attributes={sam_NamedItem_name}

# Relationships
listPorts5: BinaryAssociation = BinaryAssociation(
    name="listPorts5",
    ends={
        Property(name="Port", type=sam_Automaton, multiplicity=Multiplicity(1, 1)),
        Property(name="parentAutomaton6", type=sam_Port, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
dest15: BinaryAssociation = BinaryAssociation(
    name="dest15",
    ends={
        Property(name="inlink", type=sam_State, multiplicity=Multiplicity(1, 1)),
        Property(name="State", type=sam_Transition, multiplicity=Multiplicity(1, 1))
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
composition11: BinaryAssociation = BinaryAssociation(
    name="composition11",
    ends={
        Property(name="AbstractState12", type=sam_MacroState, multiplicity=Multiplicity(1, 1)),
        Property(name="parentState", type=sam_AbstractState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inlink13: BinaryAssociation = BinaryAssociation(
    name="inlink13",
    ends={
        Property(name="Transition14", type=sam_State, multiplicity=Multiplicity(1, 1)),
        Property(name="dest", type=sam_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
parentSync23: BinaryAssociation = BinaryAssociation(
    name="parentSync23",
    ends={
        Property(name="SynchronisationGate24", type=sam_OutDataPort, multiplicity=Multiplicity(1, 1)),
        Property(name="out", type=sam_SynchronisationGate, multiplicity=Multiplicity(0, 1))
    }
)
parentSync20: BinaryAssociation = BinaryAssociation(
    name="parentSync20",
    ends={
        Property(name="SynchronisationGate", type=sam_InDataPort, multiplicity=Multiplicity(1, 1)),
        Property(name="in", type=sam_SynchronisationGate, multiplicity=Multiplicity(0, 1))
    }
)
parentDataStore21: BinaryAssociation = BinaryAssociation(
    name="parentDataStore21",
    ends={
        Property(name="DataStore", type=sam_InDataPort, multiplicity=Multiplicity(1, 1)),
        Property(name="in22", type=sam_DataStore, multiplicity=Multiplicity(0, 1))
    }
)
parentMultiPort36: BinaryAssociation = BinaryAssociation(
    name="parentMultiPort36",
    ends={
        Property(name="sam_MultiPort", type=sam_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="sam_Port37", type=sam_MultiPort, multiplicity=Multiplicity(0, 1))
    }
)
isInstanceOf39: BinaryAssociation = BinaryAssociation(
    name="isInstanceOf39",
    ends={
        Property(name="sam_Port40", type=sam_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="sam_Port38", type=sam_Port, multiplicity=Multiplicity(0, 1))
    }
)
parentDataStore25: BinaryAssociation = BinaryAssociation(
    name="parentDataStore25",
    ends={
        Property(name="DataStore27", type=sam_OutDataPort, multiplicity=Multiplicity(1, 1)),
        Property(name="out26", type=sam_DataStore, multiplicity=Multiplicity(0, 1))
    }
)
parentSystem28: BinaryAssociation = BinaryAssociation(
    name="parentSystem28",
    ends={
        Property(name="System", type=sam_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="listPorts", type=sam_System, multiplicity=Multiplicity(0, 1))
    }
)
outlink29: BinaryAssociation = BinaryAssociation(
    name="outlink29",
    ends={
        Property(name="sam_Flow", type=sam_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="sam_Port", type=sam_Flow, multiplicity=Multiplicity(0, 1))
    }
)
inlink30: BinaryAssociation = BinaryAssociation(
    name="inlink30",
    ends={
        Property(name="sam_Flow32", type=sam_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="sam_Port31", type=sam_Flow, multiplicity=Multiplicity(0, 1))
    }
)
parentAutomaton33: BinaryAssociation = BinaryAssociation(
    name="parentAutomaton33",
    ends={
        Property(name="Automaton35", type=sam_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="listPorts34", type=sam_Automaton, multiplicity=Multiplicity(0, 1))
    }
)
parentSystem49: BinaryAssociation = BinaryAssociation(
    name="parentSystem49",
    ends={
        Property(name="System50", type=sam_DataStore, multiplicity=Multiplicity(1, 1)),
        Property(name="listStores", type=sam_System, multiplicity=Multiplicity(1, 1))
    }
)
in51: BinaryAssociation = BinaryAssociation(
    name="in51",
    ends={
        Property(name="InDataPort", type=sam_DataStore, multiplicity=Multiplicity(1, 1)),
        Property(name="parentDataStore", type=sam_InDataPort, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
out52: BinaryAssociation = BinaryAssociation(
    name="out52",
    ends={
        Property(name="OutDataPort", type=sam_DataStore, multiplicity=Multiplicity(1, 1)),
        Property(name="parentDataStore53", type=sam_OutDataPort, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source41: BinaryAssociation = BinaryAssociation(
    name="source41",
    ends={
        Property(name="sam_ControlPort", type=sam_ControlFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="sam_ControlFlow", type=sam_ControlPort, multiplicity=Multiplicity(1, 1))
    }
)
dest42: BinaryAssociation = BinaryAssociation(
    name="dest42",
    ends={
        Property(name="sam_ControlPort44", type=sam_ControlFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="sam_ControlFlow43", type=sam_ControlPort, multiplicity=Multiplicity(1, 9999))
    }
)
source45: BinaryAssociation = BinaryAssociation(
    name="source45",
    ends={
        Property(name="sam_DataPort", type=sam_DataFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="sam_DataFlow", type=sam_DataPort, multiplicity=Multiplicity(1, 1))
    }
)
dest46: BinaryAssociation = BinaryAssociation(
    name="dest46",
    ends={
        Property(name="sam_DataPort48", type=sam_DataFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="sam_DataFlow47", type=sam_DataPort, multiplicity=Multiplicity(1, 9999))
    }
)
out58: BinaryAssociation = BinaryAssociation(
    name="out58",
    ends={
        Property(name="OutDataPort59", type=sam_SynchronisationGate, multiplicity=Multiplicity(1, 1)),
        Property(name="parentSync", type=sam_OutDataPort, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
in60: BinaryAssociation = BinaryAssociation(
    name="in60",
    ends={
        Property(name="InDataPort62", type=sam_SynchronisationGate, multiplicity=Multiplicity(1, 1)),
        Property(name="parentSync61", type=sam_InDataPort, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
parentSystem54: BinaryAssociation = BinaryAssociation(
    name="parentSystem54",
    ends={
        Property(name="System55", type=sam_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="listFlows", type=sam_System, multiplicity=Multiplicity(1, 1))
    }
)
parentSystem56: BinaryAssociation = BinaryAssociation(
    name="parentSystem56",
    ends={
        Property(name="System57", type=sam_SynchronisationGate, multiplicity=Multiplicity(1, 1)),
        Property(name="listSynchronisation", type=sam_System, multiplicity=Multiplicity(1, 1))
    }
)
listElements73: BinaryAssociation = BinaryAssociation(
    name="listElements73",
    ends={
        Property(name="ModelContent", type=sam_System, multiplicity=Multiplicity(1, 1)),
        Property(name="parentSystem74", type=sam_ModelContent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
listPorts63: BinaryAssociation = BinaryAssociation(
    name="listPorts63",
    ends={
        Property(name="Port64", type=sam_System, multiplicity=Multiplicity(1, 1)),
        Property(name="parentSystem", type=sam_Port, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
listStores65: BinaryAssociation = BinaryAssociation(
    name="listStores65",
    ends={
        Property(name="DataStore67", type=sam_System, multiplicity=Multiplicity(1, 1)),
        Property(name="parentSystem66", type=sam_DataStore, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
listSynchronisation68: BinaryAssociation = BinaryAssociation(
    name="listSynchronisation68",
    ends={
        Property(name="SynchronisationGate70", type=sam_System, multiplicity=Multiplicity(1, 1)),
        Property(name="parentSystem69", type=sam_SynchronisationGate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
listFlows71: BinaryAssociation = BinaryAssociation(
    name="listFlows71",
    ends={
        Property(name="Flow", type=sam_System, multiplicity=Multiplicity(1, 1)),
        Property(name="parentSystem72", type=sam_Flow, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
listMultiPort82: BinaryAssociation = BinaryAssociation(
    name="listMultiPort82",
    ends={
        Property(name="MultiPort", type=sam_ModelContent, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=sam_MultiPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
isInstanceOf76: BinaryAssociation = BinaryAssociation(
    name="isInstanceOf76",
    ends={
        Property(name="sam_System", type=sam_System, multiplicity=Multiplicity(1, 1)),
        Property(name="sam_System75", type=sam_System, multiplicity=Multiplicity(0, 1))
    }
)
modelContent77: BinaryAssociation = BinaryAssociation(
    name="modelContent77",
    ends={
        Property(name="ModelContent78", type=sam_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="parentModel", type=sam_ModelContent, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parentModel79: BinaryAssociation = BinaryAssociation(
    name="parentModel79",
    ends={
        Property(name="Model", type=sam_ModelContent, multiplicity=Multiplicity(1, 1)),
        Property(name="modelContent", type=sam_Model, multiplicity=Multiplicity(0, 1))
    }
)
parentSystem80: BinaryAssociation = BinaryAssociation(
    name="parentSystem80",
    ends={
        Property(name="System81", type=sam_ModelContent, multiplicity=Multiplicity(1, 1)),
        Property(name="listElements", type=sam_System, multiplicity=Multiplicity(0, 1))
    }
)
listPort83: BinaryAssociation = BinaryAssociation(
    name="listPort83",
    ends={
        Property(name="sam_Port85", type=sam_MultiPort, multiplicity=Multiplicity(1, 1)),
        Property(name="sam_MultiPort84", type=sam_Port, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
parent86: BinaryAssociation = BinaryAssociation(
    name="parent86",
    ends={
        Property(name="ModelContent87", type=sam_MultiPort, multiplicity=Multiplicity(1, 1)),
        Property(name="listMultiPort", type=sam_ModelContent, multiplicity=Multiplicity(1, 1))
    }
)
isInstanceOf89: BinaryAssociation = BinaryAssociation(
    name="isInstanceOf89",
    ends={
        Property(name="sam_MultiPort90", type=sam_MultiPort, multiplicity=Multiplicity(1, 1)),
        Property(name="sam_MultiPort88", type=sam_MultiPort, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_sam_AbstractState_NamedItem = Generalization(general=NamedItem, specific=sam_AbstractState)
gen_sam_InitialState_State = Generalization(general=State, specific=sam_InitialState)
gen_sam_Automaton_ModelContent = Generalization(general=ModelContent, specific=sam_Automaton)
gen_sam_ControlPort_Port = Generalization(general=Port, specific=sam_ControlPort)
gen_sam_MacroState_AbstractState = Generalization(general=AbstractState, specific=sam_MacroState)
gen_sam_State_AbstractState = Generalization(general=AbstractState, specific=sam_State)
gen_sam_Transition_IdentifiedItem = Generalization(general=IdentifiedItem, specific=sam_Transition)
gen_sam_OutControlPort_ControlPort = Generalization(general=ControlPort, specific=sam_OutControlPort)
gen_sam_OutControlPort_OutputPort = Generalization(general=OutputPort, specific=sam_OutControlPort)
gen_sam_OutDataPort_DataPort = Generalization(general=DataPort, specific=sam_OutDataPort)
gen_sam_OutDataPort_OutputPort = Generalization(general=OutputPort, specific=sam_OutDataPort)
gen_sam_DataPort_Port = Generalization(general=Port, specific=sam_DataPort)
gen_sam_InControlPort_ControlPort = Generalization(general=ControlPort, specific=sam_InControlPort)
gen_sam_InControlPort_InputPort = Generalization(general=InputPort, specific=sam_InControlPort)
gen_sam_InDataPort_DataPort = Generalization(general=DataPort, specific=sam_InDataPort)
gen_sam_InDataPort_InputPort = Generalization(general=InputPort, specific=sam_InDataPort)
gen_sam_InputPort_Port = Generalization(general=Port, specific=sam_InputPort)
gen_sam_Composition_SynchronisationGate = Generalization(general=SynchronisationGate, specific=sam_Composition)
gen_sam_ControlFlow_Flow = Generalization(general=Flow, specific=sam_ControlFlow)
gen_sam_OutputPort_Port = Generalization(general=Port, specific=sam_OutputPort)
gen_sam_Port_NamedItem = Generalization(general=NamedItem, specific=sam_Port)
gen_sam_DataFlow_Flow = Generalization(general=Flow, specific=sam_DataFlow)
gen_sam_DataStore_NamedItem = Generalization(general=NamedItem, specific=sam_DataStore)
gen_sam_System_ModelContent = Generalization(general=ModelContent, specific=sam_System)
gen_sam_Decomposition_SynchronisationGate = Generalization(general=SynchronisationGate, specific=sam_Decomposition)
gen_sam_Flow_NamedItem = Generalization(general=NamedItem, specific=sam_Flow)
gen_sam_SynchronisationGate_IdentifiedItem = Generalization(general=IdentifiedItem, specific=sam_SynchronisationGate)
gen_sam_IdentifiedItem_EModelElement = Generalization(general=EModelElement, specific=sam_IdentifiedItem)
gen_sam_ModelContent_NamedItem = Generalization(general=NamedItem, specific=sam_ModelContent)
gen_sam_NamedItem_IdentifiedItem = Generalization(general=IdentifiedItem, specific=sam_NamedItem)
gen_sam_MultiPort_NamedItem = Generalization(general=NamedItem, specific=sam_MultiPort)

# Domain Model
domain_model = DomainModel(
    name="sam",
    types={sam_Port, sam_AbstractState, NamedItem, sam_InitialState, State, sam_MacroState, sam_Automaton, sam_Transition, ModelContent, sam_ControlPort, Port, AbstractState, sam_State, IdentifiedItem, sam_OutControlPort, OutputPort, sam_OutDataPort, sam_DataPort, sam_InControlPort, ControlPort, InputPort, sam_InDataPort, DataPort, sam_SynchronisationGate, sam_DataStore, sam_InputPort, sam_MultiPort, sam_Composition, SynchronisationGate, sam_ControlFlow, Flow, sam_OutputPort, sam_System, sam_Flow, sam_DataFlow, sam_Decomposition, sam_ModelContent, sam_IdentifiedItem, EModelElement, sam_Model, sam_NamedItem, DataType},
    associations={listPorts5, listStates7, isInstanceOf10, parentState0, parentAutomaton1, outlink2, listTransitions3, dest15, parentAutomaton16, source18, composition11, inlink13, parentSync23, parentSync20, parentDataStore21, parentMultiPort36, isInstanceOf39, parentDataStore25, parentSystem28, outlink29, inlink30, parentAutomaton33, parentSystem49, in51, out52, source41, dest42, source45, dest46, out58, in60, parentSystem54, parentSystem56, listElements73, listPorts63, listStores65, listSynchronisation68, listFlows71, listMultiPort82, isInstanceOf76, modelContent77, parentModel79, parentSystem80, listPort83, parent86, isInstanceOf89},
    generalizations={gen_sam_AbstractState_NamedItem, gen_sam_InitialState_State, gen_sam_Automaton_ModelContent, gen_sam_ControlPort_Port, gen_sam_MacroState_AbstractState, gen_sam_State_AbstractState, gen_sam_Transition_IdentifiedItem, gen_sam_OutControlPort_ControlPort, gen_sam_OutControlPort_OutputPort, gen_sam_OutDataPort_DataPort, gen_sam_OutDataPort_OutputPort, gen_sam_DataPort_Port, gen_sam_InControlPort_ControlPort, gen_sam_InControlPort_InputPort, gen_sam_InDataPort_DataPort, gen_sam_InDataPort_InputPort, gen_sam_InputPort_Port, gen_sam_Composition_SynchronisationGate, gen_sam_ControlFlow_Flow, gen_sam_OutputPort_Port, gen_sam_Port_NamedItem, gen_sam_DataFlow_Flow, gen_sam_DataStore_NamedItem, gen_sam_System_ModelContent, gen_sam_Decomposition_SynchronisationGate, gen_sam_Flow_NamedItem, gen_sam_SynchronisationGate_IdentifiedItem, gen_sam_IdentifiedItem_EModelElement, gen_sam_ModelContent_NamedItem, gen_sam_NamedItem_IdentifiedItem, gen_sam_MultiPort_NamedItem},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)