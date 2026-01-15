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
effbd106_Sequence = Class(name="effbd106::Sequence", is_abstract=True)
effbd106_Flow = Class(name="effbd106::Flow")
effbd106_Function = Class(name="effbd106::Function")
SequenceNode = Class(name="SequenceNode")
ProcessNode = Class(name="ProcessNode")
effbd106_Or = Class(name="effbd106::Or")
effbd106_Start = Class(name="effbd106::Start")
effbd106_Final = Class(name="effbd106::Final")
effbd106_Loop = Class(name="effbd106::Loop")
Port = Class(name="Port")
effbd106_Port = Class(name="effbd106::Port", is_abstract=True)
effbd106_OutputPort = Class(name="effbd106::OutputPort")
effbd106_InputPort = Class(name="effbd106::InputPort")
effbd106_Description = Class(name="effbd106::Description")
effbd106_Token = Class(name="effbd106::Token")
effbd106_SequenceNode = Class(name="effbd106::SequenceNode", is_abstract=True)
effbd106_And = Class(name="effbd106::And")
Sequence = Class(name="Sequence")
effbd106_LoopExit = Class(name="effbd106::LoopExit")
effbd106_Iteration = Class(name="effbd106::Iteration")
effbd106_Item = Class(name="effbd106::Item")
effbd106_ProcessNode = Class(name="effbd106::ProcessNode", is_abstract=True)

# effbd106_Sequence class attributes and methods

# effbd106_Flow class attributes and methods

# effbd106_Function class attributes and methods
effbd106_Function_domain: Property = Property(name="domain", type=StringType)
effbd106_Function.attributes={effbd106_Function_domain}

# SequenceNode class attributes and methods

# ProcessNode class attributes and methods

# effbd106_Or class attributes and methods

# effbd106_Start class attributes and methods

# effbd106_Final class attributes and methods

# effbd106_Loop class attributes and methods

# Port class attributes and methods

# effbd106_Port class attributes and methods
effbd106_Port_id: Property = Property(name="id", type=StringType)
effbd106_Port.attributes={effbd106_Port_id}

# effbd106_OutputPort class attributes and methods

# effbd106_InputPort class attributes and methods

# effbd106_Description class attributes and methods
effbd106_Description_content: Property = Property(name="content", type=StringType)
effbd106_Description.attributes={effbd106_Description_content}

# effbd106_Token class attributes and methods

# effbd106_SequenceNode class attributes and methods
effbd106_SequenceNode_name: Property = Property(name="name", type=StringType)
effbd106_SequenceNode_tMin: Property = Property(name="tMin", type=IntegerType)
effbd106_SequenceNode_tMax: Property = Property(name="tMax", type=IntegerType)
effbd106_SequenceNode.attributes={effbd106_SequenceNode_tMax, effbd106_SequenceNode_name, effbd106_SequenceNode_tMin}

# effbd106_And class attributes and methods

# Sequence class attributes and methods

# effbd106_LoopExit class attributes and methods

# effbd106_Iteration class attributes and methods

# effbd106_Item class attributes and methods
effbd106_Item_name: Property = Property(name="name", type=StringType)
effbd106_Item.attributes={effbd106_Item_name}

# effbd106_ProcessNode class attributes and methods
effbd106_ProcessNode_label: Property = Property(name="label", type=StringType)
effbd106_ProcessNode.attributes={effbd106_ProcessNode_label}

# Relationships
decompositions1: BinaryAssociation = BinaryAssociation(
    name="decompositions1",
    ends={
        Property(name="effbd106_Function", type=effbd106_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd106_Function0", type=effbd106_Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sequenceNodes2: BinaryAssociation = BinaryAssociation(
    name="sequenceNodes2",
    ends={
        Property(name="effbd106_Sequence", type=effbd106_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd106_Function3", type=effbd106_Sequence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
flows4: BinaryAssociation = BinaryAssociation(
    name="flows4",
    ends={
        Property(name="effbd106_Flow", type=effbd106_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd106_Function5", type=effbd106_Flow, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputPorts6: BinaryAssociation = BinaryAssociation(
    name="outputPorts6",
    ends={
        Property(name="effbd106_OutputPort", type=effbd106_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd106_Function7", type=effbd106_OutputPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputPorts8: BinaryAssociation = BinaryAssociation(
    name="inputPorts8",
    ends={
        Property(name="effbd106_InputPort", type=effbd106_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd106_Function9", type=effbd106_InputPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
descriptions10: BinaryAssociation = BinaryAssociation(
    name="descriptions10",
    ends={
        Property(name="effbd106_Description", type=effbd106_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd106_Function11", type=effbd106_Description, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tokens12: BinaryAssociation = BinaryAssociation(
    name="tokens12",
    ends={
        Property(name="effbd106_Token", type=effbd106_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd106_Function13", type=effbd106_Token, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
controlFlowEdge15: BinaryAssociation = BinaryAssociation(
    name="controlFlowEdge15",
    ends={
        Property(name="effbd106_SequenceNode", type=effbd106_SequenceNode, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd106_SequenceNode14", type=effbd106_SequenceNode, multiplicity=Multiplicity(0, 9999))
    }
)
inputflowEdge16: BinaryAssociation = BinaryAssociation(
    name="inputflowEdge16",
    ends={
        Property(name="effbd106_InputPort18", type=effbd106_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd106_Flow17", type=effbd106_InputPort, multiplicity=Multiplicity(0, 9999))
    }
)
items19: BinaryAssociation = BinaryAssociation(
    name="items19",
    ends={
        Property(name="effbd106_Item", type=effbd106_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd106_Flow20", type=effbd106_Item, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputflowEdge21: BinaryAssociation = BinaryAssociation(
    name="outputflowEdge21",
    ends={
        Property(name="effbd106_Flow23", type=effbd106_OutputPort, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd106_OutputPort22", type=effbd106_Flow, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_effbd106_Function_SequenceNode = Generalization(general=SequenceNode, specific=effbd106_Function)
gen_effbd106_Function_ProcessNode = Generalization(general=ProcessNode, specific=effbd106_Function)
gen_effbd106_Or_Sequence = Generalization(general=Sequence, specific=effbd106_Or)
gen_effbd106_Start_Sequence = Generalization(general=Sequence, specific=effbd106_Start)
gen_effbd106_Final_Sequence = Generalization(general=Sequence, specific=effbd106_Final)
gen_effbd106_Loop_Sequence = Generalization(general=Sequence, specific=effbd106_Loop)
gen_effbd106_InputPort_Port = Generalization(general=Port, specific=effbd106_InputPort)
gen_effbd106_Sequence_SequenceNode = Generalization(general=SequenceNode, specific=effbd106_Sequence)
gen_effbd106_And_Sequence = Generalization(general=Sequence, specific=effbd106_And)
gen_effbd106_LoopExit_Sequence = Generalization(general=Sequence, specific=effbd106_LoopExit)
gen_effbd106_Iteration_Sequence = Generalization(general=Sequence, specific=effbd106_Iteration)
gen_effbd106_Flow_ProcessNode = Generalization(general=ProcessNode, specific=effbd106_Flow)
gen_effbd106_OutputPort_Port = Generalization(general=Port, specific=effbd106_OutputPort)

# Domain Model
domain_model = DomainModel(
    name="effbd106",
    types={effbd106_Sequence, effbd106_Flow, effbd106_Function, SequenceNode, ProcessNode, effbd106_Or, effbd106_Start, effbd106_Final, effbd106_Loop, Port, effbd106_Port, effbd106_OutputPort, effbd106_InputPort, effbd106_Description, effbd106_Token, effbd106_SequenceNode, effbd106_And, Sequence, effbd106_LoopExit, effbd106_Iteration, effbd106_Item, effbd106_ProcessNode, FunctionDomain},
    associations={decompositions1, sequenceNodes2, flows4, outputPorts6, inputPorts8, descriptions10, tokens12, controlFlowEdge15, inputflowEdge16, items19, outputflowEdge21},
    generalizations={gen_effbd106_Function_SequenceNode, gen_effbd106_Function_ProcessNode, gen_effbd106_Or_Sequence, gen_effbd106_Start_Sequence, gen_effbd106_Final_Sequence, gen_effbd106_Loop_Sequence, gen_effbd106_InputPort_Port, gen_effbd106_Sequence_SequenceNode, gen_effbd106_And_Sequence, gen_effbd106_LoopExit_Sequence, gen_effbd106_Iteration_Sequence, gen_effbd106_Flow_ProcessNode, gen_effbd106_OutputPort_Port},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)