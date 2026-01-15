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
FunctionDomain: Enumeration = Enumeration(
    name="FunctionDomain",
    literals={
            EnumerationLiteral(name="time"),
			EnumerationLiteral(name="space"),
			EnumerationLiteral(name="form")
    }
)

# Classes
effbd103_Function = Class(name="effbd103::Function")
SequenceNode = Class(name="SequenceNode")
ProcessNode = Class(name="ProcessNode")
effbd103_And = Class(name="effbd103::And")
Sequence = Class(name="Sequence")
effbd103_Or = Class(name="effbd103::Or")
effbd103_Start = Class(name="effbd103::Start")
effbd103_Final = Class(name="effbd103::Final")
effbd103_Loop = Class(name="effbd103::Loop")
Port = Class(name="Port")
effbd103_Sequence = Class(name="effbd103::Sequence", is_abstract=True)
effbd103_Flow = Class(name="effbd103::Flow")
effbd103_OutputPort = Class(name="effbd103::OutputPort")
effbd103_InputPort = Class(name="effbd103::InputPort")
effbd103_Description = Class(name="effbd103::Description")
effbd103_Token = Class(name="effbd103::Token")
effbd103_SequenceNode = Class(name="effbd103::SequenceNode", is_abstract=True)
effbd103_LoopExit = Class(name="effbd103::LoopExit")
effbd103_Iteration = Class(name="effbd103::Iteration")
effbd103_Port = Class(name="effbd103::Port", is_abstract=True)
effbd103_Item = Class(name="effbd103::Item")
effbd103_ProcessNode = Class(name="effbd103::ProcessNode", is_abstract=True)

# effbd103_Function class attributes and methods
effbd103_Function_domain: Property = Property(name="domain", type=StringType)
effbd103_Function.attributes={effbd103_Function_domain}

# SequenceNode class attributes and methods

# ProcessNode class attributes and methods

# effbd103_And class attributes and methods

# Sequence class attributes and methods

# effbd103_Or class attributes and methods

# effbd103_Start class attributes and methods

# effbd103_Final class attributes and methods

# effbd103_Loop class attributes and methods

# Port class attributes and methods

# effbd103_Sequence class attributes and methods

# effbd103_Flow class attributes and methods

# effbd103_OutputPort class attributes and methods

# effbd103_InputPort class attributes and methods

# effbd103_Description class attributes and methods
effbd103_Description_content: Property = Property(name="content", type=StringType)
effbd103_Description.attributes={effbd103_Description_content}

# effbd103_Token class attributes and methods

# effbd103_SequenceNode class attributes and methods
effbd103_SequenceNode_tMin: Property = Property(name="tMin", type=IntegerType)
effbd103_SequenceNode_tMax: Property = Property(name="tMax", type=IntegerType)
effbd103_SequenceNode_name: Property = Property(name="name", type=StringType)
effbd103_SequenceNode.attributes={effbd103_SequenceNode_tMin, effbd103_SequenceNode_tMax, effbd103_SequenceNode_name}

# effbd103_LoopExit class attributes and methods

# effbd103_Iteration class attributes and methods

# effbd103_Port class attributes and methods
effbd103_Port_id: Property = Property(name="id", type=StringType)
effbd103_Port.attributes={effbd103_Port_id}

# effbd103_Item class attributes and methods
effbd103_Item_name: Property = Property(name="name", type=StringType)
effbd103_Item.attributes={effbd103_Item_name}

# effbd103_ProcessNode class attributes and methods
effbd103_ProcessNode_label: Property = Property(name="label", type=StringType)
effbd103_ProcessNode.attributes={effbd103_ProcessNode_label}

# Relationships
decompositions1: BinaryAssociation = BinaryAssociation(
    name="decompositions1",
    ends={
        Property(name="effbd103_Function", type=effbd103_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd103_Function0", type=effbd103_Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sequenceNodes2: BinaryAssociation = BinaryAssociation(
    name="sequenceNodes2",
    ends={
        Property(name="effbd103_Sequence", type=effbd103_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd103_Function3", type=effbd103_Sequence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
flows4: BinaryAssociation = BinaryAssociation(
    name="flows4",
    ends={
        Property(name="effbd103_Flow", type=effbd103_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd103_Function5", type=effbd103_Flow, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputPorts6: BinaryAssociation = BinaryAssociation(
    name="outputPorts6",
    ends={
        Property(name="effbd103_OutputPort", type=effbd103_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd103_Function7", type=effbd103_OutputPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputPorts8: BinaryAssociation = BinaryAssociation(
    name="inputPorts8",
    ends={
        Property(name="effbd103_InputPort", type=effbd103_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd103_Function9", type=effbd103_InputPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
descriptions10: BinaryAssociation = BinaryAssociation(
    name="descriptions10",
    ends={
        Property(name="effbd103_Description", type=effbd103_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd103_Function11", type=effbd103_Description, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tokens12: BinaryAssociation = BinaryAssociation(
    name="tokens12",
    ends={
        Property(name="effbd103_Token", type=effbd103_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd103_Function13", type=effbd103_Token, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
controlFlowEdge15: BinaryAssociation = BinaryAssociation(
    name="controlFlowEdge15",
    ends={
        Property(name="effbd103_SequenceNode", type=effbd103_SequenceNode, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd103_SequenceNode14", type=effbd103_SequenceNode, multiplicity=Multiplicity(0, 9999))
    }
)
inputflowEdge16: BinaryAssociation = BinaryAssociation(
    name="inputflowEdge16",
    ends={
        Property(name="effbd103_InputPort18", type=effbd103_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd103_Flow17", type=effbd103_InputPort, multiplicity=Multiplicity(0, 9999))
    }
)
items19: BinaryAssociation = BinaryAssociation(
    name="items19",
    ends={
        Property(name="effbd103_Item", type=effbd103_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd103_Flow20", type=effbd103_Item, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputflowEdge21: BinaryAssociation = BinaryAssociation(
    name="outputflowEdge21",
    ends={
        Property(name="effbd103_Flow23", type=effbd103_OutputPort, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd103_OutputPort22", type=effbd103_Flow, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_effbd103_Function_SequenceNode = Generalization(general=SequenceNode, specific=effbd103_Function)
gen_effbd103_Function_ProcessNode = Generalization(general=ProcessNode, specific=effbd103_Function)
gen_effbd103_Sequence_SequenceNode = Generalization(general=SequenceNode, specific=effbd103_Sequence)
gen_effbd103_And_Sequence = Generalization(general=Sequence, specific=effbd103_And)
gen_effbd103_Or_Sequence = Generalization(general=Sequence, specific=effbd103_Or)
gen_effbd103_Start_Sequence = Generalization(general=Sequence, specific=effbd103_Start)
gen_effbd103_Final_Sequence = Generalization(general=Sequence, specific=effbd103_Final)
gen_effbd103_Loop_Sequence = Generalization(general=Sequence, specific=effbd103_Loop)
gen_effbd103_InputPort_Port = Generalization(general=Port, specific=effbd103_InputPort)
gen_effbd103_LoopExit_Sequence = Generalization(general=Sequence, specific=effbd103_LoopExit)
gen_effbd103_Iteration_Sequence = Generalization(general=Sequence, specific=effbd103_Iteration)
gen_effbd103_Flow_ProcessNode = Generalization(general=ProcessNode, specific=effbd103_Flow)
gen_effbd103_OutputPort_Port = Generalization(general=Port, specific=effbd103_OutputPort)

# Domain Model
domain_model = DomainModel(
    name="effbd103",
    types={effbd103_Function, SequenceNode, ProcessNode, effbd103_And, Sequence, effbd103_Or, effbd103_Start, effbd103_Final, effbd103_Loop, Port, effbd103_Sequence, effbd103_Flow, effbd103_OutputPort, effbd103_InputPort, effbd103_Description, effbd103_Token, effbd103_SequenceNode, effbd103_LoopExit, effbd103_Iteration, effbd103_Port, effbd103_Item, effbd103_ProcessNode, FunctionDomain},
    associations={decompositions1, sequenceNodes2, flows4, outputPorts6, inputPorts8, descriptions10, tokens12, controlFlowEdge15, inputflowEdge16, items19, outputflowEdge21},
    generalizations={gen_effbd103_Function_SequenceNode, gen_effbd103_Function_ProcessNode, gen_effbd103_Sequence_SequenceNode, gen_effbd103_And_Sequence, gen_effbd103_Or_Sequence, gen_effbd103_Start_Sequence, gen_effbd103_Final_Sequence, gen_effbd103_Loop_Sequence, gen_effbd103_InputPort_Port, gen_effbd103_LoopExit_Sequence, gen_effbd103_Iteration_Sequence, gen_effbd103_Flow_ProcessNode, gen_effbd103_OutputPort_Port},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)