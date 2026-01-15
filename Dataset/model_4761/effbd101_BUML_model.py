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

# Classes
effbd101_Function = Class(name="effbd101::Function")
SequenceNode = Class(name="SequenceNode")
ProcessNode = Class(name="ProcessNode")
effbd101_Sequence = Class(name="effbd101::Sequence", is_abstract=True)
effbd101_Flow = Class(name="effbd101::Flow")
effbd101_OutputPort = Class(name="effbd101::OutputPort")
effbd101_InputPort = Class(name="effbd101::InputPort")
effbd101_Description = Class(name="effbd101::Description")
effbd101_SequenceNode = Class(name="effbd101::SequenceNode", is_abstract=True)
effbd101_And = Class(name="effbd101::And")
Sequence = Class(name="Sequence")
effbd101_Or = Class(name="effbd101::Or")
effbd101_Start = Class(name="effbd101::Start")
effbd101_Final = Class(name="effbd101::Final")
effbd101_Loop = Class(name="effbd101::Loop")
effbd101_Port = Class(name="effbd101::Port", is_abstract=True)
effbd101_Item = Class(name="effbd101::Item")
effbd101_ProcessNode = Class(name="effbd101::ProcessNode", is_abstract=True)
Port = Class(name="Port")

# effbd101_Function class attributes and methods

# SequenceNode class attributes and methods

# ProcessNode class attributes and methods

# effbd101_Sequence class attributes and methods

# effbd101_Flow class attributes and methods

# effbd101_OutputPort class attributes and methods

# effbd101_InputPort class attributes and methods

# effbd101_Description class attributes and methods
effbd101_Description_content: Property = Property(name="content", type=StringType)
effbd101_Description.attributes={effbd101_Description_content}

# effbd101_SequenceNode class attributes and methods
effbd101_SequenceNode_name: Property = Property(name="name", type=StringType)
effbd101_SequenceNode.attributes={effbd101_SequenceNode_name}

# effbd101_And class attributes and methods

# Sequence class attributes and methods

# effbd101_Or class attributes and methods

# effbd101_Start class attributes and methods

# effbd101_Final class attributes and methods

# effbd101_Loop class attributes and methods

# effbd101_Port class attributes and methods
effbd101_Port_id: Property = Property(name="id", type=StringType)
effbd101_Port.attributes={effbd101_Port_id}

# effbd101_Item class attributes and methods
effbd101_Item_name: Property = Property(name="name", type=StringType)
effbd101_Item.attributes={effbd101_Item_name}

# effbd101_ProcessNode class attributes and methods
effbd101_ProcessNode_label: Property = Property(name="label", type=StringType)
effbd101_ProcessNode.attributes={effbd101_ProcessNode_label}

# Port class attributes and methods

# Relationships
decompositions1: BinaryAssociation = BinaryAssociation(
    name="decompositions1",
    ends={
        Property(name="effbd101_Function", type=effbd101_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd101_Function0", type=effbd101_Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sequenceNodes2: BinaryAssociation = BinaryAssociation(
    name="sequenceNodes2",
    ends={
        Property(name="effbd101_Sequence", type=effbd101_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd101_Function3", type=effbd101_Sequence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
flows4: BinaryAssociation = BinaryAssociation(
    name="flows4",
    ends={
        Property(name="effbd101_Flow", type=effbd101_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd101_Function5", type=effbd101_Flow, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputPorts6: BinaryAssociation = BinaryAssociation(
    name="outputPorts6",
    ends={
        Property(name="effbd101_OutputPort", type=effbd101_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd101_Function7", type=effbd101_OutputPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputPorts8: BinaryAssociation = BinaryAssociation(
    name="inputPorts8",
    ends={
        Property(name="effbd101_InputPort", type=effbd101_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd101_Function9", type=effbd101_InputPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
descriptions10: BinaryAssociation = BinaryAssociation(
    name="descriptions10",
    ends={
        Property(name="effbd101_Description", type=effbd101_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd101_Function11", type=effbd101_Description, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
controlFlowEdge13: BinaryAssociation = BinaryAssociation(
    name="controlFlowEdge13",
    ends={
        Property(name="effbd101_SequenceNode", type=effbd101_SequenceNode, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd101_SequenceNode12", type=effbd101_SequenceNode, multiplicity=Multiplicity(0, 9999))
    }
)
inputflowEdge14: BinaryAssociation = BinaryAssociation(
    name="inputflowEdge14",
    ends={
        Property(name="effbd101_InputPort16", type=effbd101_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd101_Flow15", type=effbd101_InputPort, multiplicity=Multiplicity(0, 9999))
    }
)
items17: BinaryAssociation = BinaryAssociation(
    name="items17",
    ends={
        Property(name="effbd101_Item", type=effbd101_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd101_Flow18", type=effbd101_Item, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputflowEdge19: BinaryAssociation = BinaryAssociation(
    name="outputflowEdge19",
    ends={
        Property(name="effbd101_Flow21", type=effbd101_OutputPort, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd101_OutputPort20", type=effbd101_Flow, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_effbd101_Function_SequenceNode = Generalization(general=SequenceNode, specific=effbd101_Function)
gen_effbd101_Function_ProcessNode = Generalization(general=ProcessNode, specific=effbd101_Function)
gen_effbd101_Sequence_SequenceNode = Generalization(general=SequenceNode, specific=effbd101_Sequence)
gen_effbd101_And_Sequence = Generalization(general=Sequence, specific=effbd101_And)
gen_effbd101_Or_Sequence = Generalization(general=Sequence, specific=effbd101_Or)
gen_effbd101_Start_Sequence = Generalization(general=Sequence, specific=effbd101_Start)
gen_effbd101_Final_Sequence = Generalization(general=Sequence, specific=effbd101_Final)
gen_effbd101_Loop_Sequence = Generalization(general=Sequence, specific=effbd101_Loop)
gen_effbd101_Flow_ProcessNode = Generalization(general=ProcessNode, specific=effbd101_Flow)
gen_effbd101_OutputPort_Port = Generalization(general=Port, specific=effbd101_OutputPort)
gen_effbd101_InputPort_Port = Generalization(general=Port, specific=effbd101_InputPort)

# Domain Model
domain_model = DomainModel(
    name="effbd101",
    types={effbd101_Function, SequenceNode, ProcessNode, effbd101_Sequence, effbd101_Flow, effbd101_OutputPort, effbd101_InputPort, effbd101_Description, effbd101_SequenceNode, effbd101_And, Sequence, effbd101_Or, effbd101_Start, effbd101_Final, effbd101_Loop, effbd101_Port, effbd101_Item, effbd101_ProcessNode, Port},
    associations={decompositions1, sequenceNodes2, flows4, outputPorts6, inputPorts8, descriptions10, controlFlowEdge13, inputflowEdge14, items17, outputflowEdge19},
    generalizations={gen_effbd101_Function_SequenceNode, gen_effbd101_Function_ProcessNode, gen_effbd101_Sequence_SequenceNode, gen_effbd101_And_Sequence, gen_effbd101_Or_Sequence, gen_effbd101_Start_Sequence, gen_effbd101_Final_Sequence, gen_effbd101_Loop_Sequence, gen_effbd101_Flow_ProcessNode, gen_effbd101_OutputPort_Port, gen_effbd101_InputPort_Port},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)