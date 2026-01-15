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
effbd902_Function = Class(name="effbd902::Function")
SequenceNode = Class(name="SequenceNode")
ProcessNode = Class(name="ProcessNode")
AbstractFunction = Class(name="AbstractFunction")
effbd902_AbstractFunction = Class(name="effbd902::AbstractFunction", is_abstract=True)
effbd902_Sequence = Class(name="effbd902::Sequence", is_abstract=True)
effbd902_Flow = Class(name="effbd902::Flow")
effbd902_OutputPort = Class(name="effbd902::OutputPort")
effbd902_InputPort = Class(name="effbd902::InputPort")
effbd902_Or = Class(name="effbd902::Or")
effbd902_Start = Class(name="effbd902::Start")
effbd902_Final = Class(name="effbd902::Final")
effbd902_Loop = Class(name="effbd902::Loop")
Port = Class(name="Port")
effbd902_Port = Class(name="effbd902::Port", is_abstract=True)
effbd902_Item = Class(name="effbd902::Item")
effbd902_Description = Class(name="effbd902::Description")
effbd902_Token = Class(name="effbd902::Token")
effbd902_SequenceNode = Class(name="effbd902::SequenceNode", is_abstract=True)
effbd902_And = Class(name="effbd902::And")
Sequence = Class(name="Sequence")
effbd902_ProcessNode = Class(name="effbd902::ProcessNode", is_abstract=True)
effbd902_LoopExit = Class(name="effbd902::LoopExit")
effbd902_Iteration = Class(name="effbd902::Iteration")

# effbd902_Function class attributes and methods
effbd902_Function_domain: Property = Property(name="domain", type=StringType)
effbd902_Function.attributes={effbd902_Function_domain}

# SequenceNode class attributes and methods

# ProcessNode class attributes and methods

# AbstractFunction class attributes and methods

# effbd902_AbstractFunction class attributes and methods
effbd902_AbstractFunction_id: Property = Property(name="id", type=StringType)
effbd902_AbstractFunction.attributes={effbd902_AbstractFunction_id}

# effbd902_Sequence class attributes and methods

# effbd902_Flow class attributes and methods

# effbd902_OutputPort class attributes and methods

# effbd902_InputPort class attributes and methods

# effbd902_Or class attributes and methods

# effbd902_Start class attributes and methods

# effbd902_Final class attributes and methods

# effbd902_Loop class attributes and methods

# Port class attributes and methods

# effbd902_Port class attributes and methods
effbd902_Port_id: Property = Property(name="id", type=StringType)
effbd902_Port.attributes={effbd902_Port_id}

# effbd902_Item class attributes and methods
effbd902_Item_name: Property = Property(name="name", type=StringType)
effbd902_Item.attributes={effbd902_Item_name}

# effbd902_Description class attributes and methods
effbd902_Description_content: Property = Property(name="content", type=StringType)
effbd902_Description.attributes={effbd902_Description_content}

# effbd902_Token class attributes and methods

# effbd902_SequenceNode class attributes and methods
effbd902_SequenceNode_name: Property = Property(name="name", type=StringType)
effbd902_SequenceNode_tMin: Property = Property(name="tMin", type=IntegerType)
effbd902_SequenceNode_tMax: Property = Property(name="tMax", type=IntegerType)
effbd902_SequenceNode.attributes={effbd902_SequenceNode_tMin, effbd902_SequenceNode_tMax, effbd902_SequenceNode_name}

# effbd902_And class attributes and methods

# Sequence class attributes and methods

# effbd902_ProcessNode class attributes and methods
effbd902_ProcessNode_label: Property = Property(name="label", type=StringType)
effbd902_ProcessNode.attributes={effbd902_ProcessNode_label}

# effbd902_LoopExit class attributes and methods

# effbd902_Iteration class attributes and methods

# Relationships
decompositions0: BinaryAssociation = BinaryAssociation(
    name="decompositions0",
    ends={
        Property(name="effbd902_AbstractFunction", type=effbd902_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd902_Function", type=effbd902_AbstractFunction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sequenceNodes1: BinaryAssociation = BinaryAssociation(
    name="sequenceNodes1",
    ends={
        Property(name="effbd902_Sequence", type=effbd902_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd902_Function2", type=effbd902_Sequence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
flows3: BinaryAssociation = BinaryAssociation(
    name="flows3",
    ends={
        Property(name="effbd902_Flow", type=effbd902_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd902_Function4", type=effbd902_Flow, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputPorts5: BinaryAssociation = BinaryAssociation(
    name="outputPorts5",
    ends={
        Property(name="effbd902_OutputPort", type=effbd902_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd902_Function6", type=effbd902_OutputPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputflowEdge15: BinaryAssociation = BinaryAssociation(
    name="inputflowEdge15",
    ends={
        Property(name="effbd902_InputPort17", type=effbd902_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd902_Flow16", type=effbd902_InputPort, multiplicity=Multiplicity(0, 9999))
    }
)
inputPorts7: BinaryAssociation = BinaryAssociation(
    name="inputPorts7",
    ends={
        Property(name="effbd902_InputPort", type=effbd902_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd902_Function8", type=effbd902_InputPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
descriptions9: BinaryAssociation = BinaryAssociation(
    name="descriptions9",
    ends={
        Property(name="effbd902_Description", type=effbd902_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd902_Function10", type=effbd902_Description, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tokens11: BinaryAssociation = BinaryAssociation(
    name="tokens11",
    ends={
        Property(name="effbd902_Token", type=effbd902_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd902_Function12", type=effbd902_Token, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
controlFlowEdge14: BinaryAssociation = BinaryAssociation(
    name="controlFlowEdge14",
    ends={
        Property(name="effbd902_SequenceNode", type=effbd902_SequenceNode, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd902_SequenceNode13", type=effbd902_SequenceNode, multiplicity=Multiplicity(0, 9999))
    }
)
items18: BinaryAssociation = BinaryAssociation(
    name="items18",
    ends={
        Property(name="effbd902_Item", type=effbd902_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd902_Flow19", type=effbd902_Item, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputflowEdge20: BinaryAssociation = BinaryAssociation(
    name="outputflowEdge20",
    ends={
        Property(name="effbd902_Flow22", type=effbd902_OutputPort, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd902_OutputPort21", type=effbd902_Flow, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_effbd902_Function_SequenceNode = Generalization(general=SequenceNode, specific=effbd902_Function)
gen_effbd902_Function_ProcessNode = Generalization(general=ProcessNode, specific=effbd902_Function)
gen_effbd902_Function_AbstractFunction = Generalization(general=AbstractFunction, specific=effbd902_Function)
gen_effbd902_Or_Sequence = Generalization(general=Sequence, specific=effbd902_Or)
gen_effbd902_Start_Sequence = Generalization(general=Sequence, specific=effbd902_Start)
gen_effbd902_Final_Sequence = Generalization(general=Sequence, specific=effbd902_Final)
gen_effbd902_Loop_Sequence = Generalization(general=Sequence, specific=effbd902_Loop)
gen_effbd902_InputPort_Port = Generalization(general=Port, specific=effbd902_InputPort)
gen_effbd902_Flow_ProcessNode = Generalization(general=ProcessNode, specific=effbd902_Flow)
gen_effbd902_Sequence_SequenceNode = Generalization(general=SequenceNode, specific=effbd902_Sequence)
gen_effbd902_And_Sequence = Generalization(general=Sequence, specific=effbd902_And)
gen_effbd902_OutputPort_Port = Generalization(general=Port, specific=effbd902_OutputPort)
gen_effbd902_LoopExit_Sequence = Generalization(general=Sequence, specific=effbd902_LoopExit)
gen_effbd902_Iteration_Sequence = Generalization(general=Sequence, specific=effbd902_Iteration)

# Domain Model
domain_model = DomainModel(
    name="effbd902",
    types={effbd902_Function, SequenceNode, ProcessNode, AbstractFunction, effbd902_AbstractFunction, effbd902_Sequence, effbd902_Flow, effbd902_OutputPort, effbd902_InputPort, effbd902_Or, effbd902_Start, effbd902_Final, effbd902_Loop, Port, effbd902_Port, effbd902_Item, effbd902_Description, effbd902_Token, effbd902_SequenceNode, effbd902_And, Sequence, effbd902_ProcessNode, effbd902_LoopExit, effbd902_Iteration, FunctionDomain},
    associations={decompositions0, sequenceNodes1, flows3, outputPorts5, inputflowEdge15, inputPorts7, descriptions9, tokens11, controlFlowEdge14, items18, outputflowEdge20},
    generalizations={gen_effbd902_Function_SequenceNode, gen_effbd902_Function_ProcessNode, gen_effbd902_Function_AbstractFunction, gen_effbd902_Or_Sequence, gen_effbd902_Start_Sequence, gen_effbd902_Final_Sequence, gen_effbd902_Loop_Sequence, gen_effbd902_InputPort_Port, gen_effbd902_Flow_ProcessNode, gen_effbd902_Sequence_SequenceNode, gen_effbd902_And_Sequence, gen_effbd902_OutputPort_Port, gen_effbd902_LoopExit_Sequence, gen_effbd902_Iteration_Sequence},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)