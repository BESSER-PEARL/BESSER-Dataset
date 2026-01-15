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
effbd2_Function = Class(name="effbd2::Function")
FunctionSpecification = Class(name="FunctionSpecification")
effbd2_DataFlowEdge = Class(name="effbd2::DataFlowEdge")
effbd2_EffbdNode = Class(name="effbd2::EffbdNode", is_abstract=True)
effbd2_ControlFlowEdge = Class(name="effbd2::ControlFlowEdge")
EffbdElement = Class(name="EffbdElement")
effbd2_SequenceNode = Class(name="effbd2::SequenceNode", is_abstract=True)
Transformer = Class(name="Transformer")
effbd2_EffbdElement = Class(name="effbd2::EffbdElement", is_abstract=True)
effbd2_Fork = Class(name="effbd2::Fork")
SequenceNode = Class(name="SequenceNode")
effbd2_Decision = Class(name="effbd2::Decision")
effbd2_Transformed = Class(name="effbd2::Transformed", is_abstract=True)
EffbdNode = Class(name="EffbdNode")
effbd2_ItemContent = Class(name="effbd2::ItemContent")
effbd2_ContinuousFlowItem = Class(name="effbd2::ContinuousFlowItem")
Transformed = Class(name="Transformed")
effbd2_TriggerItem = Class(name="effbd2::TriggerItem")
effbd2_In = Class(name="effbd2::In", is_abstract=True)
DataPort = Class(name="DataPort")
effbd2_DataPort = Class(name="effbd2::DataPort", is_abstract=True)
effbd2_FunctionSpecification = Class(name="effbd2::FunctionSpecification", is_abstract=True)
effbd2_Input = Class(name="effbd2::Input")
effbd2_Control = Class(name="effbd2::Control")
effbd2_Resource = Class(name="effbd2::Resource")
effbd2_Out = Class(name="effbd2::Out")
effbd2_FunctionDefinition = Class(name="effbd2::FunctionDefinition")
DataFlowEdge = Class(name="DataFlowEdge")
effbd2_DataFlowOutputEdge = Class(name="effbd2::DataFlowOutputEdge")
effbd2_IterationStart = Class(name="effbd2::IterationStart")
In = Class(name="In")
effbd2_Transformer = Class(name="effbd2::Transformer", is_abstract=True)
effbd2_DataFlowInputEdge = Class(name="effbd2::DataFlowInputEdge")
effbd2_LoopExit = Class(name="effbd2::LoopExit")
effbd2_Join = Class(name="effbd2::Join")
effbd2_Merge = Class(name="effbd2::Merge")
effbd2_Start = Class(name="effbd2::Start")
effbd2_Final = Class(name="effbd2::Final")
effbd2_LoopStart = Class(name="effbd2::LoopStart")
effbd2_LoopEnd = Class(name="effbd2::LoopEnd")
effbd2_IterationEnd = Class(name="effbd2::IterationEnd")

# effbd2_Function class attributes and methods

# FunctionSpecification class attributes and methods

# effbd2_DataFlowEdge class attributes and methods

# effbd2_EffbdNode class attributes and methods

# effbd2_ControlFlowEdge class attributes and methods

# EffbdElement class attributes and methods

# effbd2_SequenceNode class attributes and methods

# Transformer class attributes and methods

# effbd2_EffbdElement class attributes and methods
effbd2_EffbdElement_name: Property = Property(name="name", type=StringType)
effbd2_EffbdElement.attributes={effbd2_EffbdElement_name}

# effbd2_Fork class attributes and methods

# SequenceNode class attributes and methods

# effbd2_Decision class attributes and methods

# effbd2_Transformed class attributes and methods

# EffbdNode class attributes and methods

# effbd2_ItemContent class attributes and methods
effbd2_ItemContent_id: Property = Property(name="id", type=StringType)
effbd2_ItemContent.attributes={effbd2_ItemContent_id}

# effbd2_ContinuousFlowItem class attributes and methods

# Transformed class attributes and methods

# effbd2_TriggerItem class attributes and methods

# effbd2_In class attributes and methods

# DataPort class attributes and methods

# effbd2_DataPort class attributes and methods
effbd2_DataPort_id: Property = Property(name="id", type=StringType)
effbd2_DataPort.attributes={effbd2_DataPort_id}

# effbd2_FunctionSpecification class attributes and methods
effbd2_FunctionSpecification_domain: Property = Property(name="domain", type=StringType)
effbd2_FunctionSpecification_minDuration: Property = Property(name="minDuration", type=IntegerType)
effbd2_FunctionSpecification_maxDuration: Property = Property(name="maxDuration", type=IntegerType)
effbd2_FunctionSpecification.attributes={effbd2_FunctionSpecification_minDuration, effbd2_FunctionSpecification_domain, effbd2_FunctionSpecification_maxDuration}

# effbd2_Input class attributes and methods

# effbd2_Control class attributes and methods

# effbd2_Resource class attributes and methods

# effbd2_Out class attributes and methods

# effbd2_FunctionDefinition class attributes and methods
effbd2_FunctionDefinition_transformationDefinition: Property = Property(name="transformationDefinition", type=StringType)
effbd2_FunctionDefinition.attributes={effbd2_FunctionDefinition_transformationDefinition}

# DataFlowEdge class attributes and methods

# effbd2_DataFlowOutputEdge class attributes and methods

# effbd2_IterationStart class attributes and methods

# In class attributes and methods

# effbd2_Transformer class attributes and methods

# effbd2_DataFlowInputEdge class attributes and methods

# effbd2_LoopExit class attributes and methods

# effbd2_Join class attributes and methods

# effbd2_Merge class attributes and methods

# effbd2_Start class attributes and methods

# effbd2_Final class attributes and methods

# effbd2_LoopStart class attributes and methods

# effbd2_LoopEnd class attributes and methods

# effbd2_IterationEnd class attributes and methods

# Relationships
dataEdges0: BinaryAssociation = BinaryAssociation(
    name="dataEdges0",
    ends={
        Property(name="effbd2_DataFlowEdge", type=effbd2_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd2_Function", type=effbd2_DataFlowEdge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
effbdNodes1: BinaryAssociation = BinaryAssociation(
    name="effbdNodes1",
    ends={
        Property(name="effbd2_EffbdNode", type=effbd2_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd2_Function2", type=effbd2_EffbdNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
controlEdges3: BinaryAssociation = BinaryAssociation(
    name="controlEdges3",
    ends={
        Property(name="effbd2_ControlFlowEdge", type=effbd2_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd2_Function4", type=effbd2_ControlFlowEdge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
decompositions6: BinaryAssociation = BinaryAssociation(
    name="decompositions6",
    ends={
        Property(name="effbd2_Function7", type=effbd2_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd2_Function5", type=effbd2_Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
content17: BinaryAssociation = BinaryAssociation(
    name="content17",
    ends={
        Property(name="effbd2_ItemContent", type=effbd2_Transformed, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd2_Transformed", type=effbd2_ItemContent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputPorts8: BinaryAssociation = BinaryAssociation(
    name="inputPorts8",
    ends={
        Property(name="effbd2_Input", type=effbd2_FunctionSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd2_FunctionSpecification", type=effbd2_Input, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
controlPorts9: BinaryAssociation = BinaryAssociation(
    name="controlPorts9",
    ends={
        Property(name="effbd2_Control", type=effbd2_FunctionSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd2_FunctionSpecification10", type=effbd2_Control, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourcePorts11: BinaryAssociation = BinaryAssociation(
    name="resourcePorts11",
    ends={
        Property(name="effbd2_Resource", type=effbd2_FunctionSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd2_FunctionSpecification12", type=effbd2_Resource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputPort13: BinaryAssociation = BinaryAssociation(
    name="outputPort13",
    ends={
        Property(name="effbd2_Out", type=effbd2_FunctionSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd2_FunctionSpecification14", type=effbd2_Out, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
definitions15: BinaryAssociation = BinaryAssociation(
    name="definitions15",
    ends={
        Property(name="effbd2_FunctionDefinition", type=effbd2_FunctionSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd2_FunctionSpecification16", type=effbd2_FunctionDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputFrom23: BinaryAssociation = BinaryAssociation(
    name="inputFrom23",
    ends={
        Property(name="effbd2_Transformed24", type=effbd2_DataFlowInputEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd2_DataFlowInputEdge", type=effbd2_Transformed, multiplicity=Multiplicity(0, 1))
    }
)
inputTo25: BinaryAssociation = BinaryAssociation(
    name="inputTo25",
    ends={
        Property(name="effbd2_In", type=effbd2_DataFlowInputEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd2_DataFlowInputEdge26", type=effbd2_In, multiplicity=Multiplicity(0, 1))
    }
)
outputFrom27: BinaryAssociation = BinaryAssociation(
    name="outputFrom27",
    ends={
        Property(name="effbd2_Out28", type=effbd2_DataFlowOutputEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd2_DataFlowOutputEdge", type=effbd2_Out, multiplicity=Multiplicity(0, 1))
    }
)
ouputTo29: BinaryAssociation = BinaryAssociation(
    name="ouputTo29",
    ends={
        Property(name="effbd2_Transformed31", type=effbd2_DataFlowOutputEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd2_DataFlowOutputEdge30", type=effbd2_Transformed, multiplicity=Multiplicity(0, 1))
    }
)
from18: BinaryAssociation = BinaryAssociation(
    name="from18",
    ends={
        Property(name="effbd2_Transformer", type=effbd2_ControlFlowEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd2_ControlFlowEdge19", type=effbd2_Transformer, multiplicity=Multiplicity(0, 1))
    }
)
to20: BinaryAssociation = BinaryAssociation(
    name="to20",
    ends={
        Property(name="effbd2_Transformer22", type=effbd2_ControlFlowEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="effbd2_ControlFlowEdge21", type=effbd2_Transformer, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_effbd2_Function_FunctionSpecification = Generalization(general=FunctionSpecification, specific=effbd2_Function)
gen_effbd2_DataFlowEdge_EffbdElement = Generalization(general=EffbdElement, specific=effbd2_DataFlowEdge)
gen_effbd2_EffbdNode_EffbdElement = Generalization(general=EffbdElement, specific=effbd2_EffbdNode)
gen_effbd2_SequenceNode_Transformer = Generalization(general=Transformer, specific=effbd2_SequenceNode)
gen_effbd2_Fork_SequenceNode = Generalization(general=SequenceNode, specific=effbd2_Fork)
gen_effbd2_Decision_SequenceNode = Generalization(general=SequenceNode, specific=effbd2_Decision)
gen_effbd2_Transformed_EffbdNode = Generalization(general=EffbdNode, specific=effbd2_Transformed)
gen_effbd2_ContinuousFlowItem_Transformed = Generalization(general=Transformed, specific=effbd2_ContinuousFlowItem)
gen_effbd2_TriggerItem_Transformed = Generalization(general=Transformed, specific=effbd2_TriggerItem)
gen_effbd2_In_DataPort = Generalization(general=DataPort, specific=effbd2_In)
gen_effbd2_Out_DataPort = Generalization(general=DataPort, specific=effbd2_Out)
gen_effbd2_FunctionSpecification_Transformer = Generalization(general=Transformer, specific=effbd2_FunctionSpecification)
gen_effbd2_DataFlowInputEdge_DataFlowEdge = Generalization(general=DataFlowEdge, specific=effbd2_DataFlowInputEdge)
gen_effbd2_DataFlowOutputEdge_DataFlowEdge = Generalization(general=DataFlowEdge, specific=effbd2_DataFlowOutputEdge)
gen_effbd2_IterationStart_SequenceNode = Generalization(general=SequenceNode, specific=effbd2_IterationStart)
gen_effbd2_Resource_In = Generalization(general=In, specific=effbd2_Resource)
gen_effbd2_Control_In = Generalization(general=In, specific=effbd2_Control)
gen_effbd2_Input_In = Generalization(general=In, specific=effbd2_Input)
gen_effbd2_ControlFlowEdge_EffbdElement = Generalization(general=EffbdElement, specific=effbd2_ControlFlowEdge)
gen_effbd2_Transformer_EffbdNode = Generalization(general=EffbdNode, specific=effbd2_Transformer)
gen_effbd2_LoopExit_SequenceNode = Generalization(general=SequenceNode, specific=effbd2_LoopExit)
gen_effbd2_Join_SequenceNode = Generalization(general=SequenceNode, specific=effbd2_Join)
gen_effbd2_Merge_SequenceNode = Generalization(general=SequenceNode, specific=effbd2_Merge)
gen_effbd2_Start_SequenceNode = Generalization(general=SequenceNode, specific=effbd2_Start)
gen_effbd2_Final_SequenceNode = Generalization(general=SequenceNode, specific=effbd2_Final)
gen_effbd2_LoopStart_SequenceNode = Generalization(general=SequenceNode, specific=effbd2_LoopStart)
gen_effbd2_LoopEnd_SequenceNode = Generalization(general=SequenceNode, specific=effbd2_LoopEnd)
gen_effbd2_IterationEnd_SequenceNode = Generalization(general=SequenceNode, specific=effbd2_IterationEnd)

# Domain Model
domain_model = DomainModel(
    name="effbd2",
    types={effbd2_Function, FunctionSpecification, effbd2_DataFlowEdge, effbd2_EffbdNode, effbd2_ControlFlowEdge, EffbdElement, effbd2_SequenceNode, Transformer, effbd2_EffbdElement, effbd2_Fork, SequenceNode, effbd2_Decision, effbd2_Transformed, EffbdNode, effbd2_ItemContent, effbd2_ContinuousFlowItem, Transformed, effbd2_TriggerItem, effbd2_In, DataPort, effbd2_DataPort, effbd2_FunctionSpecification, effbd2_Input, effbd2_Control, effbd2_Resource, effbd2_Out, effbd2_FunctionDefinition, DataFlowEdge, effbd2_DataFlowOutputEdge, effbd2_IterationStart, In, effbd2_Transformer, effbd2_DataFlowInputEdge, effbd2_LoopExit, effbd2_Join, effbd2_Merge, effbd2_Start, effbd2_Final, effbd2_LoopStart, effbd2_LoopEnd, effbd2_IterationEnd, FunctionDomain},
    associations={dataEdges0, effbdNodes1, controlEdges3, decompositions6, content17, inputPorts8, controlPorts9, resourcePorts11, outputPort13, definitions15, inputFrom23, inputTo25, outputFrom27, ouputTo29, from18, to20},
    generalizations={gen_effbd2_Function_FunctionSpecification, gen_effbd2_DataFlowEdge_EffbdElement, gen_effbd2_EffbdNode_EffbdElement, gen_effbd2_SequenceNode_Transformer, gen_effbd2_Fork_SequenceNode, gen_effbd2_Decision_SequenceNode, gen_effbd2_Transformed_EffbdNode, gen_effbd2_ContinuousFlowItem_Transformed, gen_effbd2_TriggerItem_Transformed, gen_effbd2_In_DataPort, gen_effbd2_Out_DataPort, gen_effbd2_FunctionSpecification_Transformer, gen_effbd2_DataFlowInputEdge_DataFlowEdge, gen_effbd2_DataFlowOutputEdge_DataFlowEdge, gen_effbd2_IterationStart_SequenceNode, gen_effbd2_Resource_In, gen_effbd2_Control_In, gen_effbd2_Input_In, gen_effbd2_ControlFlowEdge_EffbdElement, gen_effbd2_Transformer_EffbdNode, gen_effbd2_LoopExit_SequenceNode, gen_effbd2_Join_SequenceNode, gen_effbd2_Merge_SequenceNode, gen_effbd2_Start_SequenceNode, gen_effbd2_Final_SequenceNode, gen_effbd2_LoopStart_SequenceNode, gen_effbd2_LoopEnd_SequenceNode, gen_effbd2_IterationEnd_SequenceNode},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)