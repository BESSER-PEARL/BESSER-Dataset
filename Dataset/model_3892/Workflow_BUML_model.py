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
workflow_Workflow = Class(name="workflow::Workflow")
WorkflowElement = Class(name="WorkflowElement")
workflow_WorkflowNode = Class(name="workflow::WorkflowNode", is_abstract=True)
workflow_Edge = Class(name="workflow::Edge")
workflow_Comment = Class(name="workflow::Comment")
Port = Class(name="Port")
workflow_Fault = Class(name="workflow::Fault")
OutputPort = Class(name="OutputPort")
workflow_CompoundTask = Class(name="workflow::CompoundTask")
WorkflowNode = Class(name="WorkflowNode")
workflow_Port = Class(name="workflow::Port", is_abstract=True)
workflow_TransformationTask = Class(name="workflow::TransformationTask")
workflow_OutputPort = Class(name="workflow::OutputPort")
workflow_InputPort = Class(name="workflow::InputPort")
workflow_ConditionalOutputPort = Class(name="workflow::ConditionalOutputPort")
workflow_Task = Class(name="workflow::Task")
workflow_ConditionalTask = Class(name="workflow::ConditionalTask")
workflow_LoopTask = Class(name="workflow::LoopTask")
CompoundTask = Class(name="CompoundTask")
workflow_WorkflowElement = Class(name="workflow::WorkflowElement", is_abstract=True)

# workflow_Workflow class attributes and methods

# WorkflowElement class attributes and methods

# workflow_WorkflowNode class attributes and methods
workflow_WorkflowNode_isStart: Property = Property(name="isStart", type=BooleanType)
workflow_WorkflowNode_isFinish: Property = Property(name="isFinish", type=BooleanType)
workflow_WorkflowNode.attributes={workflow_WorkflowNode_isStart, workflow_WorkflowNode_isFinish}

# workflow_Edge class attributes and methods

# workflow_Comment class attributes and methods

# Port class attributes and methods

# workflow_Fault class attributes and methods

# OutputPort class attributes and methods

# workflow_CompoundTask class attributes and methods

# WorkflowNode class attributes and methods

# workflow_Port class attributes and methods

# workflow_TransformationTask class attributes and methods
workflow_TransformationTask_transformExpression: Property = Property(name="transformExpression", type=StringType)
workflow_TransformationTask.attributes={workflow_TransformationTask_transformExpression}

# workflow_OutputPort class attributes and methods

# workflow_InputPort class attributes and methods

# workflow_ConditionalOutputPort class attributes and methods
workflow_ConditionalOutputPort_condition: Property = Property(name="condition", type=StringType)
workflow_ConditionalOutputPort.attributes={workflow_ConditionalOutputPort_condition}

# workflow_Task class attributes and methods

# workflow_ConditionalTask class attributes and methods

# workflow_LoopTask class attributes and methods
workflow_LoopTask_whileCondition: Property = Property(name="whileCondition", type=StringType)
workflow_LoopTask.attributes={workflow_LoopTask_whileCondition}

# CompoundTask class attributes and methods

# workflow_WorkflowElement class attributes and methods
workflow_WorkflowElement_workFlowElementId: Property = Property(name="workFlowElementId", type=StringType)
workflow_WorkflowElement_name: Property = Property(name="name", type=StringType)
workflow_WorkflowElement_comment: Property = Property(name="comment", type=StringType)
workflow_WorkflowElement_x: Property = Property(name="x", type=IntegerType)
workflow_WorkflowElement_y: Property = Property(name="y", type=IntegerType)
workflow_WorkflowElement_width: Property = Property(name="width", type=IntegerType)
workflow_WorkflowElement_height: Property = Property(name="height", type=IntegerType)
workflow_WorkflowElement.attributes={workflow_WorkflowElement_height, workflow_WorkflowElement_workFlowElementId, workflow_WorkflowElement_x, workflow_WorkflowElement_comment, workflow_WorkflowElement_y, workflow_WorkflowElement_name, workflow_WorkflowElement_width}

# Relationships
nodes0: BinaryAssociation = BinaryAssociation(
    name="nodes0",
    ends={
        Property(name="WorkflowNode", type=workflow_Workflow, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow", type=workflow_WorkflowNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edges1: BinaryAssociation = BinaryAssociation(
    name="edges1",
    ends={
        Property(name="Edge", type=workflow_Workflow, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow2", type=workflow_Edge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
comments3: BinaryAssociation = BinaryAssociation(
    name="comments3",
    ends={
        Property(name="Comment", type=workflow_Workflow, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow4", type=workflow_Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
workflow9: BinaryAssociation = BinaryAssociation(
    name="workflow9",
    ends={
        Property(name="Workflow10", type=workflow_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="edges", type=workflow_Workflow, multiplicity=Multiplicity(1, 1))
    }
)
target11: BinaryAssociation = BinaryAssociation(
    name="target11",
    ends={
        Property(name="InputPort13", type=workflow_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="edges12", type=workflow_InputPort, multiplicity=Multiplicity(1, 1))
    }
)
source14: BinaryAssociation = BinaryAssociation(
    name="source14",
    ends={
        Property(name="OutputPort16", type=workflow_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="edges15", type=workflow_OutputPort, multiplicity=Multiplicity(1, 1))
    }
)
node17: BinaryAssociation = BinaryAssociation(
    name="node17",
    ends={
        Property(name="WorkflowNode18", type=workflow_InputPort, multiplicity=Multiplicity(1, 1)),
        Property(name="inputs", type=workflow_WorkflowNode, multiplicity=Multiplicity(1, 1))
    }
)
edges19: BinaryAssociation = BinaryAssociation(
    name="edges19",
    ends={
        Property(name="Edge20", type=workflow_InputPort, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=workflow_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
node21: BinaryAssociation = BinaryAssociation(
    name="node21",
    ends={
        Property(name="WorkflowNode22", type=workflow_OutputPort, multiplicity=Multiplicity(1, 1)),
        Property(name="outputs", type=workflow_WorkflowNode, multiplicity=Multiplicity(1, 1))
    }
)
edges23: BinaryAssociation = BinaryAssociation(
    name="edges23",
    ends={
        Property(name="Edge24", type=workflow_OutputPort, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=workflow_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
subworkflow25: BinaryAssociation = BinaryAssociation(
    name="subworkflow25",
    ends={
        Property(name="workflow_Workflow", type=workflow_CompoundTask, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_CompoundTask", type=workflow_Workflow, multiplicity=Multiplicity(1, 1))
    }
)
workflow5: BinaryAssociation = BinaryAssociation(
    name="workflow5",
    ends={
        Property(name="Workflow", type=workflow_WorkflowNode, multiplicity=Multiplicity(1, 1)),
        Property(name="nodes", type=workflow_Workflow, multiplicity=Multiplicity(1, 1))
    }
)
outputs6: BinaryAssociation = BinaryAssociation(
    name="outputs6",
    ends={
        Property(name="OutputPort", type=workflow_WorkflowNode, multiplicity=Multiplicity(1, 1)),
        Property(name="node", type=workflow_OutputPort, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
inputs7: BinaryAssociation = BinaryAssociation(
    name="inputs7",
    ends={
        Property(name="InputPort", type=workflow_WorkflowNode, multiplicity=Multiplicity(1, 1)),
        Property(name="node8", type=workflow_InputPort, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
workflow26: BinaryAssociation = BinaryAssociation(
    name="workflow26",
    ends={
        Property(name="Workflow27", type=workflow_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="comments", type=workflow_Workflow, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_workflow_Workflow_WorkflowElement = Generalization(general=WorkflowElement, specific=workflow_Workflow)
gen_workflow_Edge_WorkflowElement = Generalization(general=WorkflowElement, specific=workflow_Edge)
gen_workflow_InputPort_Port = Generalization(general=Port, specific=workflow_InputPort)
gen_workflow_OutputPort_Port = Generalization(general=Port, specific=workflow_OutputPort)
gen_workflow_Fault_OutputPort = Generalization(general=OutputPort, specific=workflow_Fault)
gen_workflow_CompoundTask_WorkflowNode = Generalization(general=WorkflowNode, specific=workflow_CompoundTask)
gen_workflow_Port_WorkflowElement = Generalization(general=WorkflowElement, specific=workflow_Port)
gen_workflow_TransformationTask_WorkflowNode = Generalization(general=WorkflowNode, specific=workflow_TransformationTask)
gen_workflow_WorkflowNode_WorkflowElement = Generalization(general=WorkflowElement, specific=workflow_WorkflowNode)
gen_workflow_ConditionalOutputPort_OutputPort = Generalization(general=OutputPort, specific=workflow_ConditionalOutputPort)
gen_workflow_Comment_WorkflowElement = Generalization(general=WorkflowElement, specific=workflow_Comment)
gen_workflow_Task_WorkflowNode = Generalization(general=WorkflowNode, specific=workflow_Task)
gen_workflow_ConditionalTask_WorkflowNode = Generalization(general=WorkflowNode, specific=workflow_ConditionalTask)
gen_workflow_LoopTask_CompoundTask = Generalization(general=CompoundTask, specific=workflow_LoopTask)

# Domain Model
domain_model = DomainModel(
    name="workflow",
    types={workflow_Workflow, WorkflowElement, workflow_WorkflowNode, workflow_Edge, workflow_Comment, Port, workflow_Fault, OutputPort, workflow_CompoundTask, WorkflowNode, workflow_Port, workflow_TransformationTask, workflow_OutputPort, workflow_InputPort, workflow_ConditionalOutputPort, workflow_Task, workflow_ConditionalTask, workflow_LoopTask, CompoundTask, workflow_WorkflowElement},
    associations={nodes0, edges1, comments3, workflow9, target11, source14, node17, edges19, node21, edges23, subworkflow25, workflow5, outputs6, inputs7, workflow26},
    generalizations={gen_workflow_Workflow_WorkflowElement, gen_workflow_Edge_WorkflowElement, gen_workflow_InputPort_Port, gen_workflow_OutputPort_Port, gen_workflow_Fault_OutputPort, gen_workflow_CompoundTask_WorkflowNode, gen_workflow_Port_WorkflowElement, gen_workflow_TransformationTask_WorkflowNode, gen_workflow_WorkflowNode_WorkflowElement, gen_workflow_ConditionalOutputPort_OutputPort, gen_workflow_Comment_WorkflowElement, gen_workflow_Task_WorkflowNode, gen_workflow_ConditionalTask_WorkflowNode, gen_workflow_LoopTask_CompoundTask},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)