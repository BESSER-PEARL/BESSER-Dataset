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
effbd104_And = Class(name="effbd104::And")
Sequence = Class(name="Sequence")
effbd104_Function = Class(name="effbd104::Function")
SequenceNode = Class(name="SequenceNode")
ProcessNode = Class(name="ProcessNode")
effbd104_Sequence = Class(name="effbd104::Sequence", is_abstract=True)
effbd104_Flow = Class(name="effbd104::Flow")
effbd104_OutputPort = Class(name="effbd104::OutputPort")
effbd104_InputPort = Class(name="effbd104::InputPort")
effbd104_Description = Class(name="effbd104::Description")
effbd104_Token = Class(name="effbd104::Token")
effbd104_SequenceNode = Class(name="effbd104::SequenceNode", is_abstract=True)
effbd104_LoopExit = Class(name="effbd104::LoopExit")
effbd104_Iteration = Class(name="effbd104::Iteration")
effbd104_Or = Class(name="effbd104::Or")
effbd104_Start = Class(name="effbd104::Start")
effbd104_Final = Class(name="effbd104::Final")
effbd104_Loop = Class(name="effbd104::Loop")
Port = Class(name="Port")
effbd104_Port = Class(name="effbd104::Port", is_abstract=True)
effbd104_Item = Class(name="effbd104::Item")
effbd104_ProcessNode = Class(name="effbd104::ProcessNode", is_abstract=True)

# effbd104_And class attributes and methods

# Sequence class attributes and methods

# effbd104_Function class attributes and methods
effbd104_Function_domain: Property = Property(name="domain", type=StringType)
effbd104_Function.attributes={effbd104_Function_domain}

# SequenceNode class attributes and methods

# ProcessNode class attributes and methods

# effbd104_Sequence class attributes and methods

# effbd104_Flow class attributes and methods

# effbd104_OutputPort class attributes and methods

# effbd104_InputPort class attributes and methods

# effbd104_Description class attributes and methods
effbd104_Description_content: Property = Property(name="content", type=StringType)
effbd104_Description.attributes={effbd104_Description_content}

# effbd104_Token class attributes and methods

# effbd104_SequenceNode class attributes and methods
effbd104_SequenceNode_name: Property = Property(name="name", type=StringType)
effbd104_SequenceNode_tMin: Property = Property(name="tMin", type=IntegerType)
effbd104_SequenceNode_tMax: Property = Property(name="tMax", type=IntegerType)
effbd104_SequenceNode.attributes={effbd104_SequenceNode_tMin, effbd104_SequenceNode_name, effbd104_SequenceNode_tMax}

# effbd104_LoopExit class attributes and methods

# effbd104_Iteration class attributes and methods

# effbd104_Or class attributes and methods

# effbd104_Start class attributes and methods

# effbd104_Final class attributes and methods

# effbd104_Loop class attributes and methods

# Port class attributes and methods

# effbd104_Port class attributes and methods
effbd104_Port_id: Property = Property(name="id", type=StringType)
effbd104_Port.attributes={effbd104_Port_id}

# effbd104_Item class attributes and methods
effbd104_Item_name: Property = Property(name="name", type=StringType)
effbd104_Item.attributes={effbd104_Item_name}

# effbd104_ProcessNode class attributes and methods
effbd104_ProcessNode_label: Property = Property(name="label", type=StringType)
effbd104_ProcessNode.attributes={effbd104_ProcessNode_label}

# Relationships
controlFlowEdge15: BinaryAssociation = BinaryAssociation(
    name="controlFlowEdge15",
    ends={
        Property(name="effbd104_SequenceNode", type=effbd104_SequenceNode, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd104_SequenceNode14", type=effbd104_SequenceNode, multiplicity=Multiplicity(0, 9999))
    }
)
decompositions1: BinaryAssociation = BinaryAssociation(
    name="decompositions1",
    ends={
        Property(name="effbd104_Function", type=effbd104_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd104_Function0", type=effbd104_Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sequenceNodes2: BinaryAssociation = BinaryAssociation(
    name="sequenceNodes2",
    ends={
        Property(name="effbd104_Sequence", type=effbd104_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd104_Function3", type=effbd104_Sequence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
flows4: BinaryAssociation = BinaryAssociation(
    name="flows4",
    ends={
        Property(name="effbd104_Flow", type=effbd104_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd104_Function5", type=effbd104_Flow, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputPorts6: BinaryAssociation = BinaryAssociation(
    name="outputPorts6",
    ends={
        Property(name="effbd104_OutputPort", type=effbd104_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd104_Function7", type=effbd104_OutputPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputPorts8: BinaryAssociation = BinaryAssociation(
    name="inputPorts8",
    ends={
        Property(name="effbd104_InputPort", type=effbd104_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd104_Function9", type=effbd104_InputPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
descriptions10: BinaryAssociation = BinaryAssociation(
    name="descriptions10",
    ends={
        Property(name="effbd104_Description", type=effbd104_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd104_Function11", type=effbd104_Description, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tokens12: BinaryAssociation = BinaryAssociation(
    name="tokens12",
    ends={
        Property(name="effbd104_Token", type=effbd104_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd104_Function13", type=effbd104_Token, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputflowEdge16: BinaryAssociation = BinaryAssociation(
    name="inputflowEdge16",
    ends={
        Property(name="effbd104_InputPort18", type=effbd104_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd104_Flow17", type=effbd104_InputPort, multiplicity=Multiplicity(0, 9999))
    }
)
items19: BinaryAssociation = BinaryAssociation(
    name="items19",
    ends={
        Property(name="effbd104_Item", type=effbd104_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd104_Flow20", type=effbd104_Item, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputflowEdge21: BinaryAssociation = BinaryAssociation(
    name="outputflowEdge21",
    ends={
        Property(name="effbd104_Flow23", type=effbd104_OutputPort, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd104_OutputPort22", type=effbd104_Flow, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_effbd104_Sequence_SequenceNode = Generalization(general=SequenceNode, specific=effbd104_Sequence)
gen_effbd104_And_Sequence = Generalization(general=Sequence, specific=effbd104_And)
gen_effbd104_Function_SequenceNode = Generalization(general=SequenceNode, specific=effbd104_Function)
gen_effbd104_Function_ProcessNode = Generalization(general=ProcessNode, specific=effbd104_Function)
gen_effbd104_LoopExit_Sequence = Generalization(general=Sequence, specific=effbd104_LoopExit)
gen_effbd104_Or_Sequence = Generalization(general=Sequence, specific=effbd104_Or)
gen_effbd104_Start_Sequence = Generalization(general=Sequence, specific=effbd104_Start)
gen_effbd104_Final_Sequence = Generalization(general=Sequence, specific=effbd104_Final)
gen_effbd104_Loop_Sequence = Generalization(general=Sequence, specific=effbd104_Loop)
gen_effbd104_InputPort_Port = Generalization(general=Port, specific=effbd104_InputPort)
gen_effbd104_Flow_ProcessNode = Generalization(general=ProcessNode, specific=effbd104_Flow)
gen_effbd104_OutputPort_Port = Generalization(general=Port, specific=effbd104_OutputPort)
gen_effbd104_Iteration_Sequence = Generalization(general=Sequence, specific=effbd104_Iteration)

# Domain Model
domain_model = DomainModel(
    name="effbd104",
    types={effbd104_And, Sequence, effbd104_Function, SequenceNode, ProcessNode, effbd104_Sequence, effbd104_Flow, effbd104_OutputPort, effbd104_InputPort, effbd104_Description, effbd104_Token, effbd104_SequenceNode, effbd104_LoopExit, effbd104_Iteration, effbd104_Or, effbd104_Start, effbd104_Final, effbd104_Loop, Port, effbd104_Port, effbd104_Item, effbd104_ProcessNode, FunctionDomain},
    associations={controlFlowEdge15, decompositions1, sequenceNodes2, flows4, outputPorts6, inputPorts8, descriptions10, tokens12, inputflowEdge16, items19, outputflowEdge21},
    generalizations={gen_effbd104_Sequence_SequenceNode, gen_effbd104_And_Sequence, gen_effbd104_Function_SequenceNode, gen_effbd104_Function_ProcessNode, gen_effbd104_LoopExit_Sequence, gen_effbd104_Or_Sequence, gen_effbd104_Start_Sequence, gen_effbd104_Final_Sequence, gen_effbd104_Loop_Sequence, gen_effbd104_InputPort_Port, gen_effbd104_Flow_ProcessNode, gen_effbd104_OutputPort_Port, gen_effbd104_Iteration_Sequence},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)