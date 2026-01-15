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
effbd201_Function = Class(name="effbd201::Function")
SequenceNode = Class(name="SequenceNode")
ProcessNode = Class(name="ProcessNode")
effbd201_And = Class(name="effbd201::And")
Sequence = Class(name="Sequence")
effbd201_Or = Class(name="effbd201::Or")
effbd201_Start = Class(name="effbd201::Start")
effbd201_Final = Class(name="effbd201::Final")
effbd201_Loop = Class(name="effbd201::Loop")
effbd201_Sequence = Class(name="effbd201::Sequence", is_abstract=True)
effbd201_Flow = Class(name="effbd201::Flow")
effbd201_OutputPort = Class(name="effbd201::OutputPort")
effbd201_InputPort = Class(name="effbd201::InputPort")
effbd201_Description = Class(name="effbd201::Description")
effbd201_Token = Class(name="effbd201::Token")
effbd201_SequenceNode = Class(name="effbd201::SequenceNode", is_abstract=True)
effbd201_LoopExit = Class(name="effbd201::LoopExit")
effbd201_Iteration = Class(name="effbd201::Iteration")
Port = Class(name="Port")
effbd201_Port = Class(name="effbd201::Port", is_abstract=True)
effbd201_Item = Class(name="effbd201::Item")
effbd201_ProcessNode = Class(name="effbd201::ProcessNode", is_abstract=True)

# effbd201_Function class attributes and methods
effbd201_Function_domain: Property = Property(name="domain", type=StringType)
effbd201_Function.attributes={effbd201_Function_domain}

# SequenceNode class attributes and methods

# ProcessNode class attributes and methods

# effbd201_And class attributes and methods

# Sequence class attributes and methods

# effbd201_Or class attributes and methods

# effbd201_Start class attributes and methods

# effbd201_Final class attributes and methods

# effbd201_Loop class attributes and methods

# effbd201_Sequence class attributes and methods

# effbd201_Flow class attributes and methods

# effbd201_OutputPort class attributes and methods

# effbd201_InputPort class attributes and methods

# effbd201_Description class attributes and methods
effbd201_Description_content: Property = Property(name="content", type=StringType)
effbd201_Description.attributes={effbd201_Description_content}

# effbd201_Token class attributes and methods

# effbd201_SequenceNode class attributes and methods
effbd201_SequenceNode_tMax: Property = Property(name="tMax", type=IntegerType)
effbd201_SequenceNode_name: Property = Property(name="name", type=StringType)
effbd201_SequenceNode_tMin: Property = Property(name="tMin", type=IntegerType)
effbd201_SequenceNode.attributes={effbd201_SequenceNode_tMin, effbd201_SequenceNode_tMax, effbd201_SequenceNode_name}

# effbd201_LoopExit class attributes and methods

# effbd201_Iteration class attributes and methods

# Port class attributes and methods

# effbd201_Port class attributes and methods
effbd201_Port_id: Property = Property(name="id", type=StringType)
effbd201_Port.attributes={effbd201_Port_id}

# effbd201_Item class attributes and methods
effbd201_Item_name: Property = Property(name="name", type=StringType)
effbd201_Item.attributes={effbd201_Item_name}

# effbd201_ProcessNode class attributes and methods
effbd201_ProcessNode_label: Property = Property(name="label", type=StringType)
effbd201_ProcessNode.attributes={effbd201_ProcessNode_label}

# Relationships
decompositions1: BinaryAssociation = BinaryAssociation(
    name="decompositions1",
    ends={
        Property(name="effbd201_Function", type=effbd201_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd201_Function0", type=effbd201_Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sequenceNodes2: BinaryAssociation = BinaryAssociation(
    name="sequenceNodes2",
    ends={
        Property(name="effbd201_Sequence", type=effbd201_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd201_Function3", type=effbd201_Sequence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
flows4: BinaryAssociation = BinaryAssociation(
    name="flows4",
    ends={
        Property(name="effbd201_Flow", type=effbd201_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd201_Function5", type=effbd201_Flow, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputPorts6: BinaryAssociation = BinaryAssociation(
    name="outputPorts6",
    ends={
        Property(name="effbd201_OutputPort", type=effbd201_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd201_Function7", type=effbd201_OutputPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputPorts8: BinaryAssociation = BinaryAssociation(
    name="inputPorts8",
    ends={
        Property(name="effbd201_InputPort", type=effbd201_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd201_Function9", type=effbd201_InputPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
descriptions10: BinaryAssociation = BinaryAssociation(
    name="descriptions10",
    ends={
        Property(name="effbd201_Description", type=effbd201_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd201_Function11", type=effbd201_Description, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tokens12: BinaryAssociation = BinaryAssociation(
    name="tokens12",
    ends={
        Property(name="effbd201_Token", type=effbd201_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd201_Function13", type=effbd201_Token, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
controlFlowEdge15: BinaryAssociation = BinaryAssociation(
    name="controlFlowEdge15",
    ends={
        Property(name="effbd201_SequenceNode", type=effbd201_SequenceNode, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd201_SequenceNode14", type=effbd201_SequenceNode, multiplicity=Multiplicity(0, 9999))
    }
)
outputflowEdge16: BinaryAssociation = BinaryAssociation(
    name="outputflowEdge16",
    ends={
        Property(name="effbd201_Flow17", type=effbd201_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd201_Port", type=effbd201_Flow, multiplicity=Multiplicity(0, 9999))
    }
)
inputflowEdge18: BinaryAssociation = BinaryAssociation(
    name="inputflowEdge18",
    ends={
        Property(name="effbd201_Port20", type=effbd201_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd201_Flow19", type=effbd201_Port, multiplicity=Multiplicity(0, 9999))
    }
)
items21: BinaryAssociation = BinaryAssociation(
    name="items21",
    ends={
        Property(name="effbd201_Item", type=effbd201_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd201_Flow22", type=effbd201_Item, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_effbd201_Function_SequenceNode = Generalization(general=SequenceNode, specific=effbd201_Function)
gen_effbd201_Function_ProcessNode = Generalization(general=ProcessNode, specific=effbd201_Function)
gen_effbd201_Sequence_SequenceNode = Generalization(general=SequenceNode, specific=effbd201_Sequence)
gen_effbd201_And_Sequence = Generalization(general=Sequence, specific=effbd201_And)
gen_effbd201_Or_Sequence = Generalization(general=Sequence, specific=effbd201_Or)
gen_effbd201_Start_Sequence = Generalization(general=Sequence, specific=effbd201_Start)
gen_effbd201_Final_Sequence = Generalization(general=Sequence, specific=effbd201_Final)
gen_effbd201_Loop_Sequence = Generalization(general=Sequence, specific=effbd201_Loop)
gen_effbd201_LoopExit_Sequence = Generalization(general=Sequence, specific=effbd201_LoopExit)
gen_effbd201_Iteration_Sequence = Generalization(general=Sequence, specific=effbd201_Iteration)
gen_effbd201_InputPort_Port = Generalization(general=Port, specific=effbd201_InputPort)
gen_effbd201_Flow_ProcessNode = Generalization(general=ProcessNode, specific=effbd201_Flow)
gen_effbd201_OutputPort_Port = Generalization(general=Port, specific=effbd201_OutputPort)

# Domain Model
domain_model = DomainModel(
    name="effbd201",
    types={effbd201_Function, SequenceNode, ProcessNode, effbd201_And, Sequence, effbd201_Or, effbd201_Start, effbd201_Final, effbd201_Loop, effbd201_Sequence, effbd201_Flow, effbd201_OutputPort, effbd201_InputPort, effbd201_Description, effbd201_Token, effbd201_SequenceNode, effbd201_LoopExit, effbd201_Iteration, Port, effbd201_Port, effbd201_Item, effbd201_ProcessNode, FunctionDomain},
    associations={decompositions1, sequenceNodes2, flows4, outputPorts6, inputPorts8, descriptions10, tokens12, controlFlowEdge15, outputflowEdge16, inputflowEdge18, items21},
    generalizations={gen_effbd201_Function_SequenceNode, gen_effbd201_Function_ProcessNode, gen_effbd201_Sequence_SequenceNode, gen_effbd201_And_Sequence, gen_effbd201_Or_Sequence, gen_effbd201_Start_Sequence, gen_effbd201_Final_Sequence, gen_effbd201_Loop_Sequence, gen_effbd201_LoopExit_Sequence, gen_effbd201_Iteration_Sequence, gen_effbd201_InputPort_Port, gen_effbd201_Flow_ProcessNode, gen_effbd201_OutputPort_Port},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)