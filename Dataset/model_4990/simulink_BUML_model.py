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
EnableStates: Enumeration = Enumeration(
    name="EnableStates",
    literals={
            EnumerationLiteral(name="Held"),
			EnumerationLiteral(name="Reset"),
			EnumerationLiteral(name="Inherit")
    }
)

TriggerType: Enumeration = Enumeration(
    name="TriggerType",
    literals={
            EnumerationLiteral(name="Rising"),
			EnumerationLiteral(name="Falling"),
			EnumerationLiteral(name="Either"),
			EnumerationLiteral(name="FunctionCall")
    }
)

TagVisibility: Enumeration = Enumeration(
    name="TagVisibility",
    literals={
            EnumerationLiteral(name="Local"),
			EnumerationLiteral(name="Scoped"),
			EnumerationLiteral(name="Global")
    }
)

# Classes
simulink_SimulinkElement = Class(name="simulink::SimulinkElement", is_abstract=True)
simulink_InPort = Class(name="simulink::InPort")
simulink_OutPort = Class(name="simulink::OutPort")
simulink_SubSystem = Class(name="simulink::SubSystem")
simulink_IdentifierReference = Class(name="simulink::IdentifierReference")
simulink_Block = Class(name="simulink::Block")
SimulinkElement = Class(name="SimulinkElement")
simulink_Parameter = Class(name="simulink::Parameter")
simulink_Port = Class(name="simulink::Port", is_abstract=True)
simulink_Trigger = Class(name="simulink::Trigger")
simulink_Enable = Class(name="simulink::Enable")
InPort = Class(name="InPort")
simulink_BusSelector = Class(name="simulink::BusSelector")
BusSpecification = Class(name="BusSpecification")
simulink_LibraryLinkReference = Class(name="simulink::LibraryLinkReference")
simulink_PortBlock = Class(name="simulink::PortBlock", is_abstract=True)
Port = Class(name="Port")
simulink_SingleConnection = Class(name="simulink::SingleConnection")
simulink_Connection = Class(name="simulink::Connection", is_abstract=True)
simulink_OutPortBlock = Class(name="simulink::OutPortBlock")
simulink_BusSignalMapping = Class(name="simulink::BusSignalMapping")
simulink_BusSpecification = Class(name="simulink::BusSpecification", is_abstract=True)
simulink_BusCreator = Class(name="simulink::BusCreator")
simulink_Goto = Class(name="simulink::Goto")
VirtualBlock = Class(name="VirtualBlock")
simulink_From = Class(name="simulink::From")
simulink_VirtualBlock = Class(name="simulink::VirtualBlock", is_abstract=True)
Block = Class(name="Block")
simulink_SimulinkModel = Class(name="simulink::SimulinkModel")
simulink_MultiConnection = Class(name="simulink::MultiConnection")
Connection = Class(name="Connection")
simulink_ModelReference = Class(name="simulink::ModelReference")
PortBlock = Class(name="PortBlock")
simulink_InPortBlock = Class(name="simulink::InPortBlock")
simulink_TriggerBlock = Class(name="simulink::TriggerBlock")
InPortBlock = Class(name="InPortBlock")
simulink_EnableBlock = Class(name="simulink::EnableBlock")
simulink_SimulinkReference = Class(name="simulink::SimulinkReference", is_abstract=True)
simulink_GotoTagVisibility = Class(name="simulink::GotoTagVisibility")
SimulinkReference = Class(name="SimulinkReference")
simulink_State = Class(name="simulink::State")
OutPort = Class(name="OutPort")

# simulink_SimulinkElement class attributes and methods
simulink_SimulinkElement_name: Property = Property(name="name", type=StringType)
simulink_SimulinkElement.attributes={simulink_SimulinkElement_name}

# simulink_InPort class attributes and methods

# simulink_OutPort class attributes and methods

# simulink_SubSystem class attributes and methods
simulink_SubSystem_tag: Property = Property(name="tag", type=StringType)
simulink_SubSystem.attributes={simulink_SubSystem_tag}

# simulink_IdentifierReference class attributes and methods

# simulink_Block class attributes and methods

# SimulinkElement class attributes and methods

# simulink_Parameter class attributes and methods
simulink_Parameter_name: Property = Property(name="name", type=StringType)
simulink_Parameter_type: Property = Property(name="type", type=StringType)
simulink_Parameter_value: Property = Property(name="value", type=StringType)
simulink_Parameter_readOnly: Property = Property(name="readOnly", type=BooleanType)
simulink_Parameter.attributes={simulink_Parameter_value, simulink_Parameter_name, simulink_Parameter_type, simulink_Parameter_readOnly}

# simulink_Port class attributes and methods

# simulink_Trigger class attributes and methods
simulink_Trigger_triggerType: Property = Property(name="triggerType", type=StringType)
simulink_Trigger_statesWhenEnabling: Property = Property(name="statesWhenEnabling", type=StringType)
simulink_Trigger.attributes={simulink_Trigger_statesWhenEnabling, simulink_Trigger_triggerType}

# simulink_Enable class attributes and methods
simulink_Enable_statesWhenEnabling: Property = Property(name="statesWhenEnabling", type=StringType)
simulink_Enable.attributes={simulink_Enable_statesWhenEnabling}

# InPort class attributes and methods

# simulink_BusSelector class attributes and methods
simulink_BusSelector_outputAsBus: Property = Property(name="outputAsBus", type=BooleanType)
simulink_BusSelector.attributes={simulink_BusSelector_outputAsBus}

# BusSpecification class attributes and methods

# simulink_LibraryLinkReference class attributes and methods
simulink_LibraryLinkReference_disabled: Property = Property(name="disabled", type=BooleanType)
simulink_LibraryLinkReference.attributes={simulink_LibraryLinkReference_disabled}

# simulink_PortBlock class attributes and methods

# Port class attributes and methods

# simulink_SingleConnection class attributes and methods

# simulink_Connection class attributes and methods
simulink_Connection_lineName: Property = Property(name="lineName", type=StringType)
simulink_Connection.attributes={simulink_Connection_lineName}

# simulink_OutPortBlock class attributes and methods

# simulink_BusSignalMapping class attributes and methods
simulink_BusSignalMapping_mappingPath: Property = Property(name="mappingPath", type=StringType)
simulink_BusSignalMapping_incomplete: Property = Property(name="incomplete", type=BooleanType)
simulink_BusSignalMapping.attributes={simulink_BusSignalMapping_mappingPath, simulink_BusSignalMapping_incomplete}

# simulink_BusSpecification class attributes and methods

# simulink_BusCreator class attributes and methods

# simulink_Goto class attributes and methods
simulink_Goto_tagVisibility: Property = Property(name="tagVisibility", type=StringType)
simulink_Goto_gotoTag: Property = Property(name="gotoTag", type=StringType)
simulink_Goto.attributes={simulink_Goto_gotoTag, simulink_Goto_tagVisibility}

# VirtualBlock class attributes and methods

# simulink_From class attributes and methods

# simulink_VirtualBlock class attributes and methods

# Block class attributes and methods

# simulink_SimulinkModel class attributes and methods
simulink_SimulinkModel_version: Property = Property(name="version", type=StringType)
simulink_SimulinkModel_file: Property = Property(name="file", type=StringType)
simulink_SimulinkModel_library: Property = Property(name="library", type=BooleanType)
simulink_SimulinkModel.attributes={simulink_SimulinkModel_library, simulink_SimulinkModel_file, simulink_SimulinkModel_version}

# simulink_MultiConnection class attributes and methods

# Connection class attributes and methods

# simulink_ModelReference class attributes and methods

# PortBlock class attributes and methods

# simulink_InPortBlock class attributes and methods

# simulink_TriggerBlock class attributes and methods

# InPortBlock class attributes and methods

# simulink_EnableBlock class attributes and methods

# simulink_SimulinkReference class attributes and methods
simulink_SimulinkReference_name: Property = Property(name="name", type=StringType)
simulink_SimulinkReference_qualifier: Property = Property(name="qualifier", type=StringType)
simulink_SimulinkReference_m_getFQN: Method = Method(name="getFQN", parameters={}, type=StringType)
simulink_SimulinkReference.attributes={simulink_SimulinkReference_qualifier, simulink_SimulinkReference_name}
simulink_SimulinkReference.methods={simulink_SimulinkReference_m_getFQN}

# simulink_GotoTagVisibility class attributes and methods

# SimulinkReference class attributes and methods

# simulink_State class attributes and methods

# OutPort class attributes and methods

# Relationships
inports7: BinaryAssociation = BinaryAssociation(
    name="inports7",
    ends={
        Property(name="simulink_InPort", type=simulink_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="simulink_Block8", type=simulink_InPort, multiplicity=Multiplicity(0, 9999))
    }
)
outports9: BinaryAssociation = BinaryAssociation(
    name="outports9",
    ends={
        Property(name="simulink_OutPort", type=simulink_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="simulink_Block10", type=simulink_OutPort, multiplicity=Multiplicity(0, 9999))
    }
)
parent11: BinaryAssociation = BinaryAssociation(
    name="parent11",
    ends={
        Property(name="SubSystem", type=simulink_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="subBlocks", type=simulink_SubSystem, multiplicity=Multiplicity(0, 1))
    }
)
simulinkRef0: BinaryAssociation = BinaryAssociation(
    name="simulinkRef0",
    ends={
        Property(name="simulink_IdentifierReference", type=simulink_SimulinkElement, multiplicity=Multiplicity(1, 1)),
        Property(name="simulink_SimulinkElement", type=simulink_IdentifierReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters1: BinaryAssociation = BinaryAssociation(
    name="parameters1",
    ends={
        Property(name="simulink_Parameter", type=simulink_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="simulink_Block", type=simulink_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ports2: BinaryAssociation = BinaryAssociation(
    name="ports2",
    ends={
        Property(name="Port", type=simulink_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="container", type=simulink_Port, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
trigger3: BinaryAssociation = BinaryAssociation(
    name="trigger3",
    ends={
        Property(name="simulink_Trigger", type=simulink_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="simulink_Block4", type=simulink_Trigger, multiplicity=Multiplicity(0, 1))
    }
)
enabler5: BinaryAssociation = BinaryAssociation(
    name="enabler5",
    ends={
        Property(name="simulink_Enable", type=simulink_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="simulink_Block6", type=simulink_Enable, multiplicity=Multiplicity(0, 1))
    }
)
from23: BinaryAssociation = BinaryAssociation(
    name="from23",
    ends={
        Property(name="OutPort", type=simulink_Connection, multiplicity=Multiplicity(1, 1)),
        Property(name="connection", type=simulink_OutPort, multiplicity=Multiplicity(0, 1))
    }
)
sourceBlock13: BinaryAssociation = BinaryAssociation(
    name="sourceBlock13",
    ends={
        Property(name="simulink_Block14", type=simulink_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="simulink_Block12", type=simulink_Block, multiplicity=Multiplicity(0, 1))
    }
)
sourceBlockRef15: BinaryAssociation = BinaryAssociation(
    name="sourceBlockRef15",
    ends={
        Property(name="simulink_LibraryLinkReference", type=simulink_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="simulink_Block16", type=simulink_LibraryLinkReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
container17: BinaryAssociation = BinaryAssociation(
    name="container17",
    ends={
        Property(name="Block", type=simulink_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="ports", type=simulink_Block, multiplicity=Multiplicity(0, 1))
    }
)
portBlock18: BinaryAssociation = BinaryAssociation(
    name="portBlock18",
    ends={
        Property(name="PortBlock", type=simulink_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="port", type=simulink_PortBlock, multiplicity=Multiplicity(0, 1))
    }
)
parameters19: BinaryAssociation = BinaryAssociation(
    name="parameters19",
    ends={
        Property(name="simulink_Parameter20", type=simulink_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="simulink_Port", type=simulink_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connection21: BinaryAssociation = BinaryAssociation(
    name="connection21",
    ends={
        Property(name="SingleConnection", type=simulink_InPort, multiplicity=Multiplicity(1, 1)),
        Property(name="to", type=simulink_SingleConnection, multiplicity=Multiplicity(0, 1))
    }
)
connection22: BinaryAssociation = BinaryAssociation(
    name="connection22",
    ends={
        Property(name="Connection", type=simulink_OutPort, multiplicity=Multiplicity(1, 1)),
        Property(name="from", type=simulink_Connection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parent32: BinaryAssociation = BinaryAssociation(
    name="parent32",
    ends={
        Property(name="MultiConnection", type=simulink_SingleConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="connections", type=simulink_MultiConnection, multiplicity=Multiplicity(0, 1))
    }
)
to33: BinaryAssociation = BinaryAssociation(
    name="to33",
    ends={
        Property(name="InPort", type=simulink_SingleConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="connection34", type=simulink_InPort, multiplicity=Multiplicity(0, 1))
    }
)
port35: BinaryAssociation = BinaryAssociation(
    name="port35",
    ends={
        Property(name="Port36", type=simulink_PortBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="portBlock", type=simulink_Port, multiplicity=Multiplicity(0, 1))
    }
)
mappings24: BinaryAssociation = BinaryAssociation(
    name="mappings24",
    ends={
        Property(name="BusSignalMapping", type=simulink_BusSelector, multiplicity=Multiplicity(1, 1)),
        Property(name="selector", type=simulink_BusSignalMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
busCreator25: BinaryAssociation = BinaryAssociation(
    name="busCreator25",
    ends={
        Property(name="simulink_BusSpecification", type=simulink_BusSelector, multiplicity=Multiplicity(1, 1)),
        Property(name="simulink_BusSelector", type=simulink_BusSpecification, multiplicity=Multiplicity(0, 1))
    }
)
fromBlocks26: BinaryAssociation = BinaryAssociation(
    name="fromBlocks26",
    ends={
        Property(name="From", type=simulink_Goto, multiplicity=Multiplicity(1, 1)),
        Property(name="gotoBlock", type=simulink_From, multiplicity=Multiplicity(0, 9999))
    }
)
gotoBlock27: BinaryAssociation = BinaryAssociation(
    name="gotoBlock27",
    ends={
        Property(name="Goto", type=simulink_From, multiplicity=Multiplicity(1, 1)),
        Property(name="fromBlocks", type=simulink_Goto, multiplicity=Multiplicity(0, 1))
    }
)
contains28: BinaryAssociation = BinaryAssociation(
    name="contains28",
    ends={
        Property(name="simulink_Block29", type=simulink_SimulinkModel, multiplicity=Multiplicity(1, 1)),
        Property(name="simulink_SimulinkModel", type=simulink_Block, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connections30: BinaryAssociation = BinaryAssociation(
    name="connections30",
    ends={
        Property(name="SingleConnection31", type=simulink_MultiConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=simulink_SingleConnection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referencedModel43: BinaryAssociation = BinaryAssociation(
    name="referencedModel43",
    ends={
        Property(name="simulink_SimulinkModel44", type=simulink_ModelReference, multiplicity=Multiplicity(1, 1)),
        Property(name="simulink_ModelReference", type=simulink_SimulinkModel, multiplicity=Multiplicity(0, 1))
    }
)
modelRef45: BinaryAssociation = BinaryAssociation(
    name="modelRef45",
    ends={
        Property(name="simulink_IdentifierReference47", type=simulink_ModelReference, multiplicity=Multiplicity(1, 1)),
        Property(name="simulink_ModelReference46", type=simulink_IdentifierReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
element37: BinaryAssociation = BinaryAssociation(
    name="element37",
    ends={
        Property(name="simulink_SimulinkElement38", type=simulink_SimulinkReference, multiplicity=Multiplicity(1, 1)),
        Property(name="simulink_SimulinkReference", type=simulink_SimulinkElement, multiplicity=Multiplicity(0, 1))
    }
)
gotoBlock39: BinaryAssociation = BinaryAssociation(
    name="gotoBlock39",
    ends={
        Property(name="simulink_Goto", type=simulink_GotoTagVisibility, multiplicity=Multiplicity(1, 1)),
        Property(name="simulink_GotoTagVisibility", type=simulink_Goto, multiplicity=Multiplicity(0, 1))
    }
)
subBlocks40: BinaryAssociation = BinaryAssociation(
    name="subBlocks40",
    ends={
        Property(name="Block42", type=simulink_SubSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="parent41", type=simulink_Block, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
selector48: BinaryAssociation = BinaryAssociation(
    name="selector48",
    ends={
        Property(name="BusSelector", type=simulink_BusSignalMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="mappings", type=simulink_BusSelector, multiplicity=Multiplicity(0, 1))
    }
)
mappingFrom49: BinaryAssociation = BinaryAssociation(
    name="mappingFrom49",
    ends={
        Property(name="simulink_OutPort50", type=simulink_BusSignalMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="simulink_BusSignalMapping", type=simulink_OutPort, multiplicity=Multiplicity(0, 1))
    }
)
mappingTo51: BinaryAssociation = BinaryAssociation(
    name="mappingTo51",
    ends={
        Property(name="simulink_OutPort53", type=simulink_BusSignalMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="simulink_BusSignalMapping52", type=simulink_OutPort, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_simulink_Block_SimulinkElement = Generalization(general=SimulinkElement, specific=simulink_Block)
gen_simulink_Trigger_InPort = Generalization(general=InPort, specific=simulink_Trigger)
gen_simulink_Enable_InPort = Generalization(general=InPort, specific=simulink_Enable)
gen_simulink_BusSelector_BusSpecification = Generalization(general=BusSpecification, specific=simulink_BusSelector)
gen_simulink_Port_SimulinkElement = Generalization(general=SimulinkElement, specific=simulink_Port)
gen_simulink_InPort_Port = Generalization(general=Port, specific=simulink_InPort)
gen_simulink_OutPort_Port = Generalization(general=Port, specific=simulink_OutPort)
gen_simulink_Connection_SimulinkElement = Generalization(general=SimulinkElement, specific=simulink_Connection)
gen_simulink_SingleConnection_Connection = Generalization(general=Connection, specific=simulink_SingleConnection)
gen_simulink_PortBlock_VirtualBlock = Generalization(general=VirtualBlock, specific=simulink_PortBlock)
gen_simulink_BusCreator_BusSpecification = Generalization(general=BusSpecification, specific=simulink_BusCreator)
gen_simulink_Goto_VirtualBlock = Generalization(general=VirtualBlock, specific=simulink_Goto)
gen_simulink_VirtualBlock_Block = Generalization(general=Block, specific=simulink_VirtualBlock)
gen_simulink_From_VirtualBlock = Generalization(general=VirtualBlock, specific=simulink_From)
gen_simulink_SimulinkModel_SimulinkElement = Generalization(general=SimulinkElement, specific=simulink_SimulinkModel)
gen_simulink_MultiConnection_Connection = Generalization(general=Connection, specific=simulink_MultiConnection)
gen_simulink_ModelReference_Block = Generalization(general=Block, specific=simulink_ModelReference)
gen_simulink_OutPortBlock_PortBlock = Generalization(general=PortBlock, specific=simulink_OutPortBlock)
gen_simulink_InPortBlock_PortBlock = Generalization(general=PortBlock, specific=simulink_InPortBlock)
gen_simulink_TriggerBlock_InPortBlock = Generalization(general=InPortBlock, specific=simulink_TriggerBlock)
gen_simulink_EnableBlock_InPortBlock = Generalization(general=InPortBlock, specific=simulink_EnableBlock)
gen_simulink_GotoTagVisibility_VirtualBlock = Generalization(general=VirtualBlock, specific=simulink_GotoTagVisibility)
gen_simulink_SubSystem_Block = Generalization(general=Block, specific=simulink_SubSystem)
gen_simulink_BusSpecification_Block = Generalization(general=Block, specific=simulink_BusSpecification)
gen_simulink_LibraryLinkReference_SimulinkReference = Generalization(general=SimulinkReference, specific=simulink_LibraryLinkReference)
gen_simulink_IdentifierReference_SimulinkReference = Generalization(general=SimulinkReference, specific=simulink_IdentifierReference)
gen_simulink_State_OutPort = Generalization(general=OutPort, specific=simulink_State)

# Domain Model
domain_model = DomainModel(
    name="simulink",
    types={simulink_SimulinkElement, simulink_InPort, simulink_OutPort, simulink_SubSystem, simulink_IdentifierReference, simulink_Block, SimulinkElement, simulink_Parameter, simulink_Port, simulink_Trigger, simulink_Enable, InPort, simulink_BusSelector, BusSpecification, simulink_LibraryLinkReference, simulink_PortBlock, Port, simulink_SingleConnection, simulink_Connection, simulink_OutPortBlock, simulink_BusSignalMapping, simulink_BusSpecification, simulink_BusCreator, simulink_Goto, VirtualBlock, simulink_From, simulink_VirtualBlock, Block, simulink_SimulinkModel, simulink_MultiConnection, Connection, simulink_ModelReference, PortBlock, simulink_InPortBlock, simulink_TriggerBlock, InPortBlock, simulink_EnableBlock, simulink_SimulinkReference, simulink_GotoTagVisibility, SimulinkReference, simulink_State, OutPort, EnableStates, TriggerType, TagVisibility},
    associations={inports7, outports9, parent11, simulinkRef0, parameters1, ports2, trigger3, enabler5, from23, sourceBlock13, sourceBlockRef15, container17, portBlock18, parameters19, connection21, connection22, parent32, to33, port35, mappings24, busCreator25, fromBlocks26, gotoBlock27, contains28, connections30, referencedModel43, modelRef45, element37, gotoBlock39, subBlocks40, selector48, mappingFrom49, mappingTo51},
    generalizations={gen_simulink_Block_SimulinkElement, gen_simulink_Trigger_InPort, gen_simulink_Enable_InPort, gen_simulink_BusSelector_BusSpecification, gen_simulink_Port_SimulinkElement, gen_simulink_InPort_Port, gen_simulink_OutPort_Port, gen_simulink_Connection_SimulinkElement, gen_simulink_SingleConnection_Connection, gen_simulink_PortBlock_VirtualBlock, gen_simulink_BusCreator_BusSpecification, gen_simulink_Goto_VirtualBlock, gen_simulink_VirtualBlock_Block, gen_simulink_From_VirtualBlock, gen_simulink_SimulinkModel_SimulinkElement, gen_simulink_MultiConnection_Connection, gen_simulink_ModelReference_Block, gen_simulink_OutPortBlock_PortBlock, gen_simulink_InPortBlock_PortBlock, gen_simulink_TriggerBlock_InPortBlock, gen_simulink_EnableBlock_InPortBlock, gen_simulink_GotoTagVisibility_VirtualBlock, gen_simulink_SubSystem_Block, gen_simulink_BusSpecification_Block, gen_simulink_LibraryLinkReference_SimulinkReference, gen_simulink_IdentifierReference_SimulinkReference, gen_simulink_State_OutPort},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)