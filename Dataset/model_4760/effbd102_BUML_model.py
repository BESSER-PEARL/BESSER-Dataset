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
effbd102_Function = Class(name="effbd102::Function")
SequenceNode = Class(name="SequenceNode")
ProcessNode = Class(name="ProcessNode")
effbd102_Sequence = Class(name="effbd102::Sequence", is_abstract=True)
effbd102_Flow = Class(name="effbd102::Flow")
effbd102_OutputPort = Class(name="effbd102::OutputPort")
effbd102_InputPort = Class(name="effbd102::InputPort")
effbd102_Description = Class(name="effbd102::Description")
effbd102_SequenceNode = Class(name="effbd102::SequenceNode", is_abstract=True)
effbd102_And = Class(name="effbd102::And")
Sequence = Class(name="Sequence")
effbd102_Start = Class(name="effbd102::Start")
effbd102_Final = Class(name="effbd102::Final")
effbd102_Loop = Class(name="effbd102::Loop")
Port = Class(name="Port")
effbd102_Port = Class(name="effbd102::Port", is_abstract=True)
effbd102_Item = Class(name="effbd102::Item")
effbd102_ProcessNode = Class(name="effbd102::ProcessNode", is_abstract=True)
effbd102_LoopExit = Class(name="effbd102::LoopExit")
effbd102_Or = Class(name="effbd102::Or")
effbd102_Iteration = Class(name="effbd102::Iteration")

# effbd102_Function class attributes and methods
effbd102_Function_domain: Property = Property(name="domain", type=StringType)
effbd102_Function_minDuration: Property = Property(name="minDuration", type=FloatType)
effbd102_Function_maxDuration: Property = Property(name="maxDuration", type=FloatType)
effbd102_Function.attributes={effbd102_Function_minDuration, effbd102_Function_domain, effbd102_Function_maxDuration}

# SequenceNode class attributes and methods

# ProcessNode class attributes and methods

# effbd102_Sequence class attributes and methods

# effbd102_Flow class attributes and methods

# effbd102_OutputPort class attributes and methods

# effbd102_InputPort class attributes and methods

# effbd102_Description class attributes and methods
effbd102_Description_content: Property = Property(name="content", type=StringType)
effbd102_Description.attributes={effbd102_Description_content}

# effbd102_SequenceNode class attributes and methods
effbd102_SequenceNode_name: Property = Property(name="name", type=StringType)
effbd102_SequenceNode.attributes={effbd102_SequenceNode_name}

# effbd102_And class attributes and methods

# Sequence class attributes and methods

# effbd102_Start class attributes and methods

# effbd102_Final class attributes and methods

# effbd102_Loop class attributes and methods

# Port class attributes and methods

# effbd102_Port class attributes and methods
effbd102_Port_id: Property = Property(name="id", type=StringType)
effbd102_Port.attributes={effbd102_Port_id}

# effbd102_Item class attributes and methods
effbd102_Item_name: Property = Property(name="name", type=StringType)
effbd102_Item.attributes={effbd102_Item_name}

# effbd102_ProcessNode class attributes and methods
effbd102_ProcessNode_label: Property = Property(name="label", type=StringType)
effbd102_ProcessNode.attributes={effbd102_ProcessNode_label}

# effbd102_LoopExit class attributes and methods

# effbd102_Or class attributes and methods

# effbd102_Iteration class attributes and methods

# Relationships
decompositions1: BinaryAssociation = BinaryAssociation(
    name="decompositions1",
    ends={
        Property(name="effbd102_Function", type=effbd102_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd102_Function0", type=effbd102_Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sequenceNodes2: BinaryAssociation = BinaryAssociation(
    name="sequenceNodes2",
    ends={
        Property(name="effbd102_Sequence", type=effbd102_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd102_Function3", type=effbd102_Sequence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
flows4: BinaryAssociation = BinaryAssociation(
    name="flows4",
    ends={
        Property(name="effbd102_Flow", type=effbd102_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd102_Function5", type=effbd102_Flow, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputPorts6: BinaryAssociation = BinaryAssociation(
    name="outputPorts6",
    ends={
        Property(name="effbd102_OutputPort", type=effbd102_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd102_Function7", type=effbd102_OutputPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputPorts8: BinaryAssociation = BinaryAssociation(
    name="inputPorts8",
    ends={
        Property(name="effbd102_InputPort", type=effbd102_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd102_Function9", type=effbd102_InputPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
descriptions10: BinaryAssociation = BinaryAssociation(
    name="descriptions10",
    ends={
        Property(name="effbd102_Description", type=effbd102_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd102_Function11", type=effbd102_Description, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
controlFlowEdge13: BinaryAssociation = BinaryAssociation(
    name="controlFlowEdge13",
    ends={
        Property(name="effbd102_SequenceNode", type=effbd102_SequenceNode, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd102_SequenceNode12", type=effbd102_SequenceNode, multiplicity=Multiplicity(0, 9999))
    }
)
inputflowEdge14: BinaryAssociation = BinaryAssociation(
    name="inputflowEdge14",
    ends={
        Property(name="effbd102_InputPort16", type=effbd102_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd102_Flow15", type=effbd102_InputPort, multiplicity=Multiplicity(0, 9999))
    }
)
items17: BinaryAssociation = BinaryAssociation(
    name="items17",
    ends={
        Property(name="effbd102_Item", type=effbd102_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd102_Flow18", type=effbd102_Item, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputflowEdge19: BinaryAssociation = BinaryAssociation(
    name="outputflowEdge19",
    ends={
        Property(name="effbd102_Flow21", type=effbd102_OutputPort, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd102_OutputPort20", type=effbd102_Flow, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_effbd102_Function_SequenceNode = Generalization(general=SequenceNode, specific=effbd102_Function)
gen_effbd102_Function_ProcessNode = Generalization(general=ProcessNode, specific=effbd102_Function)
gen_effbd102_Sequence_SequenceNode = Generalization(general=SequenceNode, specific=effbd102_Sequence)
gen_effbd102_And_Sequence = Generalization(general=Sequence, specific=effbd102_And)
gen_effbd102_Start_Sequence = Generalization(general=Sequence, specific=effbd102_Start)
gen_effbd102_Final_Sequence = Generalization(general=Sequence, specific=effbd102_Final)
gen_effbd102_Loop_Sequence = Generalization(general=Sequence, specific=effbd102_Loop)
gen_effbd102_InputPort_Port = Generalization(general=Port, specific=effbd102_InputPort)
gen_effbd102_Flow_ProcessNode = Generalization(general=ProcessNode, specific=effbd102_Flow)
gen_effbd102_OutputPort_Port = Generalization(general=Port, specific=effbd102_OutputPort)
gen_effbd102_LoopExit_Sequence = Generalization(general=Sequence, specific=effbd102_LoopExit)
gen_effbd102_Or_Sequence = Generalization(general=Sequence, specific=effbd102_Or)
gen_effbd102_Iteration_Sequence = Generalization(general=Sequence, specific=effbd102_Iteration)

# Domain Model
domain_model = DomainModel(
    name="effbd102",
    types={effbd102_Function, SequenceNode, ProcessNode, effbd102_Sequence, effbd102_Flow, effbd102_OutputPort, effbd102_InputPort, effbd102_Description, effbd102_SequenceNode, effbd102_And, Sequence, effbd102_Start, effbd102_Final, effbd102_Loop, Port, effbd102_Port, effbd102_Item, effbd102_ProcessNode, effbd102_LoopExit, effbd102_Or, effbd102_Iteration, FunctionDomain},
    associations={decompositions1, sequenceNodes2, flows4, outputPorts6, inputPorts8, descriptions10, controlFlowEdge13, inputflowEdge14, items17, outputflowEdge19},
    generalizations={gen_effbd102_Function_SequenceNode, gen_effbd102_Function_ProcessNode, gen_effbd102_Sequence_SequenceNode, gen_effbd102_And_Sequence, gen_effbd102_Start_Sequence, gen_effbd102_Final_Sequence, gen_effbd102_Loop_Sequence, gen_effbd102_InputPort_Port, gen_effbd102_Flow_ProcessNode, gen_effbd102_OutputPort_Port, gen_effbd102_LoopExit_Sequence, gen_effbd102_Or_Sequence, gen_effbd102_Iteration_Sequence},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)