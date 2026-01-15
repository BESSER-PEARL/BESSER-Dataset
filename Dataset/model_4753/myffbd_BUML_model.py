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
myffbd_Function = Class(name="myffbd::Function")
SequenceNode = Class(name="SequenceNode")
myffbd_SequenceNode = Class(name="myffbd::SequenceNode", is_abstract=True)
myffbd_OutputPort = Class(name="myffbd::OutputPort")
myffbd_InputPort = Class(name="myffbd::InputPort")
myffbd_Description = Class(name="myffbd::Description")
myffbd_Token = Class(name="myffbd::Token")
myffbd_PortType = Class(name="myffbd::PortType")
myffbd_And = Class(name="myffbd::And")
myffbd_Or = Class(name="myffbd::Or")
myffbd_Start = Class(name="myffbd::Start")
myffbd_Final = Class(name="myffbd::Final")
myffbd_Loop = Class(name="myffbd::Loop")
Port = Class(name="Port")
myffbd_Port = Class(name="myffbd::Port", is_abstract=True)
myffbd_Flow = Class(name="myffbd::Flow")
myffbd_Item = Class(name="myffbd::Item")
myffbd_LoopExit = Class(name="myffbd::LoopExit")
myffbd_Iteration = Class(name="myffbd::Iteration")

# myffbd_Function class attributes and methods
myffbd_Function_domain: Property = Property(name="domain", type=StringType)
myffbd_Function_tMin: Property = Property(name="tMin", type=IntegerType)
myffbd_Function_tMax: Property = Property(name="tMax", type=IntegerType)
myffbd_Function.attributes={myffbd_Function_tMax, myffbd_Function_tMin, myffbd_Function_domain}

# SequenceNode class attributes and methods

# myffbd_SequenceNode class attributes and methods
myffbd_SequenceNode_name: Property = Property(name="name", type=StringType)
myffbd_SequenceNode.attributes={myffbd_SequenceNode_name}

# myffbd_OutputPort class attributes and methods

# myffbd_InputPort class attributes and methods

# myffbd_Description class attributes and methods
myffbd_Description_content: Property = Property(name="content", type=StringType)
myffbd_Description.attributes={myffbd_Description_content}

# myffbd_Token class attributes and methods

# myffbd_PortType class attributes and methods
myffbd_PortType_type: Property = Property(name="type", type=StringType)
myffbd_PortType.attributes={myffbd_PortType_type}

# myffbd_And class attributes and methods

# myffbd_Or class attributes and methods

# myffbd_Start class attributes and methods

# myffbd_Final class attributes and methods

# myffbd_Loop class attributes and methods

# Port class attributes and methods

# myffbd_Port class attributes and methods
myffbd_Port_id: Property = Property(name="id", type=StringType)
myffbd_Port.attributes={myffbd_Port_id}

# myffbd_Flow class attributes and methods

# myffbd_Item class attributes and methods
myffbd_Item_name: Property = Property(name="name", type=StringType)
myffbd_Item.attributes={myffbd_Item_name}

# myffbd_LoopExit class attributes and methods

# myffbd_Iteration class attributes and methods

# Relationships
decompositions1: BinaryAssociation = BinaryAssociation(
    name="decompositions1",
    ends={
        Property(name="myffbd_Function", type=myffbd_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="myffbd_Function0", type=myffbd_Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sequenceNodes2: BinaryAssociation = BinaryAssociation(
    name="sequenceNodes2",
    ends={
        Property(name="myffbd_SequenceNode", type=myffbd_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="myffbd_Function3", type=myffbd_SequenceNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputPorts4: BinaryAssociation = BinaryAssociation(
    name="outputPorts4",
    ends={
        Property(name="myffbd_OutputPort", type=myffbd_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="myffbd_Function5", type=myffbd_OutputPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputPorts6: BinaryAssociation = BinaryAssociation(
    name="inputPorts6",
    ends={
        Property(name="myffbd_InputPort", type=myffbd_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="myffbd_Function7", type=myffbd_InputPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
descriptions8: BinaryAssociation = BinaryAssociation(
    name="descriptions8",
    ends={
        Property(name="myffbd_Description", type=myffbd_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="myffbd_Function9", type=myffbd_Description, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tokens10: BinaryAssociation = BinaryAssociation(
    name="tokens10",
    ends={
        Property(name="myffbd_Token", type=myffbd_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="myffbd_Function11", type=myffbd_Token, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
portTypes12: BinaryAssociation = BinaryAssociation(
    name="portTypes12",
    ends={
        Property(name="myffbd_PortType", type=myffbd_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="myffbd_Function13", type=myffbd_PortType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
trg26: BinaryAssociation = BinaryAssociation(
    name="trg26",
    ends={
        Property(name="myffbd_Flow27", type=myffbd_Port, multiplicity=Multiplicity(0, 1)),
        Property(name="myffbd_Port28", type=myffbd_Flow, multiplicity=Multiplicity(1, 1))
    }
)
controlFlowEdge15: BinaryAssociation = BinaryAssociation(
    name="controlFlowEdge15",
    ends={
        Property(name="myffbd_SequenceNode16", type=myffbd_SequenceNode, multiplicity=Multiplicity(1, 1)),
        Property(name="myffbd_SequenceNode14", type=myffbd_SequenceNode, multiplicity=Multiplicity(0, 9999))
    }
)
flows17: BinaryAssociation = BinaryAssociation(
    name="flows17",
    ends={
        Property(name="myffbd_Flow", type=myffbd_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="myffbd_Port", type=myffbd_Flow, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type18: BinaryAssociation = BinaryAssociation(
    name="type18",
    ends={
        Property(name="myffbd_PortType20", type=myffbd_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="myffbd_Port19", type=myffbd_PortType, multiplicity=Multiplicity(0, 1))
    }
)
src21: BinaryAssociation = BinaryAssociation(
    name="src21",
    ends={
        Property(name="myffbd_Port23", type=myffbd_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="myffbd_Flow22", type=myffbd_Port, multiplicity=Multiplicity(0, 1))
    }
)
items24: BinaryAssociation = BinaryAssociation(
    name="items24",
    ends={
        Property(name="myffbd_Item", type=myffbd_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="myffbd_Flow25", type=myffbd_Item, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_myffbd_Function_SequenceNode = Generalization(general=SequenceNode, specific=myffbd_Function)
gen_myffbd_And_SequenceNode = Generalization(general=SequenceNode, specific=myffbd_And)
gen_myffbd_Or_SequenceNode = Generalization(general=SequenceNode, specific=myffbd_Or)
gen_myffbd_Start_SequenceNode = Generalization(general=SequenceNode, specific=myffbd_Start)
gen_myffbd_Final_SequenceNode = Generalization(general=SequenceNode, specific=myffbd_Final)
gen_myffbd_Loop_SequenceNode = Generalization(general=SequenceNode, specific=myffbd_Loop)
gen_myffbd_InputPort_Port = Generalization(general=Port, specific=myffbd_InputPort)
gen_myffbd_OutputPort_Port = Generalization(general=Port, specific=myffbd_OutputPort)
gen_myffbd_LoopExit_SequenceNode = Generalization(general=SequenceNode, specific=myffbd_LoopExit)
gen_myffbd_Iteration_SequenceNode = Generalization(general=SequenceNode, specific=myffbd_Iteration)

# Domain Model
domain_model = DomainModel(
    name="myffbd",
    types={myffbd_Function, SequenceNode, myffbd_SequenceNode, myffbd_OutputPort, myffbd_InputPort, myffbd_Description, myffbd_Token, myffbd_PortType, myffbd_And, myffbd_Or, myffbd_Start, myffbd_Final, myffbd_Loop, Port, myffbd_Port, myffbd_Flow, myffbd_Item, myffbd_LoopExit, myffbd_Iteration, FunctionDomain},
    associations={decompositions1, sequenceNodes2, outputPorts4, inputPorts6, descriptions8, tokens10, portTypes12, trg26, controlFlowEdge15, flows17, type18, src21, items24},
    generalizations={gen_myffbd_Function_SequenceNode, gen_myffbd_And_SequenceNode, gen_myffbd_Or_SequenceNode, gen_myffbd_Start_SequenceNode, gen_myffbd_Final_SequenceNode, gen_myffbd_Loop_SequenceNode, gen_myffbd_InputPort_Port, gen_myffbd_OutputPort_Port, gen_myffbd_LoopExit_SequenceNode, gen_myffbd_Iteration_SequenceNode},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)