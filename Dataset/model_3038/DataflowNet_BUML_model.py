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
Comparation: Enumeration = Enumeration(
    name="Comparation",
    literals={
            EnumerationLiteral(name="Equal"),
			EnumerationLiteral(name="NotEqual"),
			EnumerationLiteral(name="Less"),
			EnumerationLiteral(name="Greater")
    }
)

Protocol: Enumeration = Enumeration(
    name="Protocol",
    literals={
            EnumerationLiteral(name="Paho"),
			EnumerationLiteral(name="Akka")
    }
)

# Classes
dataflownet_StateMachine = Class(name="dataflownet::StateMachine")
Node = Class(name="Node")
dataflownet_StateMachineState = Class(name="dataflownet::StateMachineState")
dataflownet_FiringRule = Class(name="dataflownet::FiringRule")
dataflownet_Channel = Class(name="dataflownet::Channel")
dataflownet_NamedElement = Class(name="dataflownet::NamedElement", is_abstract=True)
dataflownet_Node = Class(name="dataflownet::Node", is_abstract=True)
NamedElement = Class(name="NamedElement")
dataflownet_DataflowNet = Class(name="dataflownet::DataflowNet")
dataflownet_Process = Class(name="dataflownet::Process")
dataflownet_StateMachineTransition = Class(name="dataflownet::StateMachineTransition")
dataflownet_Type = Class(name="dataflownet::Type")
dataflownet_Token = Class(name="dataflownet::Token")
dataflownet_DataflowSystem = Class(name="dataflownet::DataflowSystem")

# dataflownet_StateMachine class attributes and methods

# Node class attributes and methods

# dataflownet_StateMachineState class attributes and methods

# dataflownet_FiringRule class attributes and methods
dataflownet_FiringRule_compType: Property = Property(name="compType", type=StringType)
dataflownet_FiringRule.attributes={dataflownet_FiringRule_compType}

# dataflownet_Channel class attributes and methods

# dataflownet_NamedElement class attributes and methods
dataflownet_NamedElement_name: Property = Property(name="name", type=StringType)
dataflownet_NamedElement.attributes={dataflownet_NamedElement_name}

# dataflownet_Node class attributes and methods

# NamedElement class attributes and methods

# dataflownet_DataflowNet class attributes and methods

# dataflownet_Process class attributes and methods
dataflownet_Process_host: Property = Property(name="host", type=StringType)
dataflownet_Process.attributes={dataflownet_Process_host}

# dataflownet_StateMachineTransition class attributes and methods
dataflownet_StateMachineTransition_priority: Property = Property(name="priority", type=IntegerType)
dataflownet_StateMachineTransition.attributes={dataflownet_StateMachineTransition_priority}

# dataflownet_Type class attributes and methods

# dataflownet_Token class attributes and methods
dataflownet_Token_value: Property = Property(name="value", type=StringType)
dataflownet_Token.attributes={dataflownet_Token_value}

# dataflownet_DataflowSystem class attributes and methods
dataflownet_DataflowSystem_protocol: Property = Property(name="protocol", type=StringType)
dataflownet_DataflowSystem.attributes={dataflownet_DataflowSystem_protocol}

# Relationships
parent0: BinaryAssociation = BinaryAssociation(
    name="parent0",
    ends={
        Property(name="nodes", type=dataflownet_DataflowNet, multiplicity=Multiplicity(0, 1)),
        Property(name="DataflowNet", type=dataflownet_Node, multiplicity=Multiplicity(1, 1))
    }
)
nodes1: BinaryAssociation = BinaryAssociation(
    name="nodes1",
    ends={
        Property(name="StateMachineState", type=dataflownet_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=dataflownet_StateMachineState, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
initialState2: BinaryAssociation = BinaryAssociation(
    name="initialState2",
    ends={
        Property(name="dataflownet_StateMachineState", type=dataflownet_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="dataflownet_StateMachine", type=dataflownet_StateMachineState, multiplicity=Multiplicity(1, 1))
    }
)
firingRules3: BinaryAssociation = BinaryAssociation(
    name="firingRules3",
    ends={
        Property(name="dataflownet_FiringRule", type=dataflownet_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="dataflownet_StateMachine4", type=dataflownet_FiringRule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputChannels5: BinaryAssociation = BinaryAssociation(
    name="outputChannels5",
    ends={
        Property(name="dataflownet_Channel", type=dataflownet_DataflowNet, multiplicity=Multiplicity(1, 1)),
        Property(name="dataflownet_DataflowNet", type=dataflownet_Channel, multiplicity=Multiplicity(0, 9999))
    }
)
process14: BinaryAssociation = BinaryAssociation(
    name="process14",
    ends={
        Property(name="dataflownet_Process", type=dataflownet_DataflowNet, multiplicity=Multiplicity(1, 1)),
        Property(name="dataflownet_DataflowNet15", type=dataflownet_Process, multiplicity=Multiplicity(0, 1))
    }
)
outputTransitions16: BinaryAssociation = BinaryAssociation(
    name="outputTransitions16",
    ends={
        Property(name="StateMachineTransition", type=dataflownet_StateMachineState, multiplicity=Multiplicity(1, 1)),
        Property(name="fromState", type=dataflownet_StateMachineTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputTransitions17: BinaryAssociation = BinaryAssociation(
    name="inputTransitions17",
    ends={
        Property(name="StateMachineTransition18", type=dataflownet_StateMachineState, multiplicity=Multiplicity(1, 1)),
        Property(name="toState", type=dataflownet_StateMachineTransition, multiplicity=Multiplicity(0, 9999))
    }
)
parent19: BinaryAssociation = BinaryAssociation(
    name="parent19",
    ends={
        Property(name="StateMachine", type=dataflownet_StateMachineState, multiplicity=Multiplicity(1, 1)),
        Property(name="nodes20", type=dataflownet_StateMachine, multiplicity=Multiplicity(1, 1))
    }
)
inputChannels6: BinaryAssociation = BinaryAssociation(
    name="inputChannels6",
    ends={
        Property(name="dataflownet_Channel8", type=dataflownet_DataflowNet, multiplicity=Multiplicity(1, 1)),
        Property(name="dataflownet_DataflowNet7", type=dataflownet_Channel, multiplicity=Multiplicity(0, 9999))
    }
)
nodes9: BinaryAssociation = BinaryAssociation(
    name="nodes9",
    ends={
        Property(name="Node", type=dataflownet_DataflowNet, multiplicity=Multiplicity(1, 1)),
        Property(name="parent10", type=dataflownet_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownChannels11: BinaryAssociation = BinaryAssociation(
    name="ownChannels11",
    ends={
        Property(name="dataflownet_Channel13", type=dataflownet_DataflowNet, multiplicity=Multiplicity(1, 1)),
        Property(name="dataflownet_DataflowNet12", type=dataflownet_Channel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputs27: BinaryAssociation = BinaryAssociation(
    name="outputs27",
    ends={
        Property(name="dataflownet_FiringRule29", type=dataflownet_StateMachineTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="dataflownet_StateMachineTransition28", type=dataflownet_FiringRule, multiplicity=Multiplicity(0, 9999))
    }
)
type30: BinaryAssociation = BinaryAssociation(
    name="type30",
    ends={
        Property(name="dataflownet_Type", type=dataflownet_Channel, multiplicity=Multiplicity(1, 1)),
        Property(name="dataflownet_Channel31", type=dataflownet_Type, multiplicity=Multiplicity(1, 1))
    }
)
channel32: BinaryAssociation = BinaryAssociation(
    name="channel32",
    ends={
        Property(name="dataflownet_Channel34", type=dataflownet_FiringRule, multiplicity=Multiplicity(1, 1)),
        Property(name="dataflownet_FiringRule33", type=dataflownet_Channel, multiplicity=Multiplicity(1, 1))
    }
)
tokens35: BinaryAssociation = BinaryAssociation(
    name="tokens35",
    ends={
        Property(name="dataflownet_Token", type=dataflownet_FiringRule, multiplicity=Multiplicity(1, 1)),
        Property(name="dataflownet_FiringRule36", type=dataflownet_Token, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type37: BinaryAssociation = BinaryAssociation(
    name="type37",
    ends={
        Property(name="dataflownet_Type39", type=dataflownet_Token, multiplicity=Multiplicity(1, 1)),
        Property(name="dataflownet_Token38", type=dataflownet_Type, multiplicity=Multiplicity(1, 1))
    }
)
fromState21: BinaryAssociation = BinaryAssociation(
    name="fromState21",
    ends={
        Property(name="StateMachineState22", type=dataflownet_StateMachineTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="outputTransitions", type=dataflownet_StateMachineState, multiplicity=Multiplicity(1, 1))
    }
)
toState23: BinaryAssociation = BinaryAssociation(
    name="toState23",
    ends={
        Property(name="StateMachineState24", type=dataflownet_StateMachineTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="inputTransitions", type=dataflownet_StateMachineState, multiplicity=Multiplicity(1, 1))
    }
)
inputs25: BinaryAssociation = BinaryAssociation(
    name="inputs25",
    ends={
        Property(name="dataflownet_FiringRule26", type=dataflownet_StateMachineTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="dataflownet_StateMachineTransition", type=dataflownet_FiringRule, multiplicity=Multiplicity(0, 9999))
    }
)
nets42: BinaryAssociation = BinaryAssociation(
    name="nets42",
    ends={
        Property(name="dataflownet_DataflowSystem43", type=dataflownet_DataflowNet, multiplicity=Multiplicity(1, 9999), is_composite=True),
        Property(name="dataflownet_DataflowNet44", type=dataflownet_DataflowSystem, multiplicity=Multiplicity(1, 1))
    }
)
channels45: BinaryAssociation = BinaryAssociation(
    name="channels45",
    ends={
        Property(name="dataflownet_Channel47", type=dataflownet_DataflowSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="dataflownet_DataflowSystem46", type=dataflownet_Channel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
processes48: BinaryAssociation = BinaryAssociation(
    name="processes48",
    ends={
        Property(name="dataflownet_Process50", type=dataflownet_DataflowSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="dataflownet_DataflowSystem49", type=dataflownet_Process, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
types40: BinaryAssociation = BinaryAssociation(
    name="types40",
    ends={
        Property(name="dataflownet_Type41", type=dataflownet_DataflowSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="dataflownet_DataflowSystem", type=dataflownet_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_dataflownet_StateMachine_Node = Generalization(general=Node, specific=dataflownet_StateMachine)
gen_dataflownet_DataflowNet_Node = Generalization(general=Node, specific=dataflownet_DataflowNet)
gen_dataflownet_Node_NamedElement = Generalization(general=NamedElement, specific=dataflownet_Node)
gen_dataflownet_StateMachineState_NamedElement = Generalization(general=NamedElement, specific=dataflownet_StateMachineState)
gen_dataflownet_StateMachineTransition_NamedElement = Generalization(general=NamedElement, specific=dataflownet_StateMachineTransition)
gen_dataflownet_Channel_NamedElement = Generalization(general=NamedElement, specific=dataflownet_Channel)
gen_dataflownet_FiringRule_NamedElement = Generalization(general=NamedElement, specific=dataflownet_FiringRule)
gen_dataflownet_Process_NamedElement = Generalization(general=NamedElement, specific=dataflownet_Process)
gen_dataflownet_DataflowSystem_NamedElement = Generalization(general=NamedElement, specific=dataflownet_DataflowSystem)

# Domain Model
domain_model = DomainModel(
    name="dataflownet",
    types={dataflownet_StateMachine, Node, dataflownet_StateMachineState, dataflownet_FiringRule, dataflownet_Channel, dataflownet_NamedElement, dataflownet_Node, NamedElement, dataflownet_DataflowNet, dataflownet_Process, dataflownet_StateMachineTransition, dataflownet_Type, dataflownet_Token, dataflownet_DataflowSystem, Comparation, Protocol},
    associations={parent0, nodes1, initialState2, firingRules3, outputChannels5, process14, outputTransitions16, inputTransitions17, parent19, inputChannels6, nodes9, ownChannels11, outputs27, type30, channel32, tokens35, type37, fromState21, toState23, inputs25, nets42, channels45, processes48, types40},
    generalizations={gen_dataflownet_StateMachine_Node, gen_dataflownet_DataflowNet_Node, gen_dataflownet_Node_NamedElement, gen_dataflownet_StateMachineState_NamedElement, gen_dataflownet_StateMachineTransition_NamedElement, gen_dataflownet_Channel_NamedElement, gen_dataflownet_FiringRule_NamedElement, gen_dataflownet_Process_NamedElement, gen_dataflownet_DataflowSystem_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)