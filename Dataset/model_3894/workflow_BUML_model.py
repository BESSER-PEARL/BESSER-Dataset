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
workflow_IPort = Class(name="workflow::IPort", is_abstract=True)
IWorkflowElement = Class(name="IWorkflowElement")
workflow_ILink = Class(name="workflow::ILink")
workflow_IWorkflow = Class(name="workflow::IWorkflow")
workflow_IInputPort = Class(name="workflow::IInputPort")
workflow_IWorkflowJob = Class(name="workflow::IWorkflowJob")
IWorkflowNode = Class(name="IWorkflowNode")
workflow_IWorkflowElement = Class(name="workflow::IWorkflowElement", is_abstract=True)
workflow_IOutputPort = Class(name="workflow::IOutputPort")
IPort = Class(name="IPort")
workflow_IWorkflowNode = Class(name="workflow::IWorkflowNode", is_abstract=True)

# workflow_IPort class attributes and methods
workflow_IPort_fileName: Property = Property(name="fileName", type=StringType)
workflow_IPort.attributes={workflow_IPort_fileName}

# IWorkflowElement class attributes and methods

# workflow_ILink class attributes and methods

# workflow_IWorkflow class attributes and methods

# workflow_IInputPort class attributes and methods

# workflow_IWorkflowJob class attributes and methods
workflow_IWorkflowJob_jobDescription: Property = Property(name="jobDescription", type=StringType)
workflow_IWorkflowJob_jobDescriptionFileName: Property = Property(name="jobDescriptionFileName", type=StringType)
workflow_IWorkflowJob.attributes={workflow_IWorkflowJob_jobDescriptionFileName, workflow_IWorkflowJob_jobDescription}

# IWorkflowNode class attributes and methods

# workflow_IWorkflowElement class attributes and methods
workflow_IWorkflowElement_name: Property = Property(name="name", type=StringType)
workflow_IWorkflowElement_id: Property = Property(name="id", type=StringType)
workflow_IWorkflowElement.attributes={workflow_IWorkflowElement_name, workflow_IWorkflowElement_id}

# workflow_IOutputPort class attributes and methods

# IPort class attributes and methods

# workflow_IWorkflowNode class attributes and methods
workflow_IWorkflowNode_isStart: Property = Property(name="isStart", type=BooleanType)
workflow_IWorkflowNode_isFinish: Property = Property(name="isFinish", type=BooleanType)
workflow_IWorkflowNode.attributes={workflow_IWorkflowNode_isStart, workflow_IWorkflowNode_isFinish}

# Relationships
workflow0: BinaryAssociation = BinaryAssociation(
    name="workflow0",
    ends={
        Property(name="IWorkflow", type=workflow_ILink, multiplicity=Multiplicity(1, 1)),
        Property(name="links", type=workflow_IWorkflow, multiplicity=Multiplicity(1, 1))
    }
)
links9: BinaryAssociation = BinaryAssociation(
    name="links9",
    ends={
        Property(name="ILink10", type=workflow_IOutputPort, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=workflow_ILink, multiplicity=Multiplicity(0, 9999))
    }
)
nodes11: BinaryAssociation = BinaryAssociation(
    name="nodes11",
    ends={
        Property(name="IWorkflowNode12", type=workflow_IWorkflow, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow", type=workflow_IWorkflowNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
links13: BinaryAssociation = BinaryAssociation(
    name="links13",
    ends={
        Property(name="ILink15", type=workflow_IWorkflow, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow14", type=workflow_ILink, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
workflow16: BinaryAssociation = BinaryAssociation(
    name="workflow16",
    ends={
        Property(name="IWorkflow17", type=workflow_IWorkflowNode, multiplicity=Multiplicity(1, 1)),
        Property(name="nodes", type=workflow_IWorkflow, multiplicity=Multiplicity(1, 1))
    }
)
outputs18: BinaryAssociation = BinaryAssociation(
    name="outputs18",
    ends={
        Property(name="IOutputPort19", type=workflow_IWorkflowNode, multiplicity=Multiplicity(1, 1)),
        Property(name="node", type=workflow_IOutputPort, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
inputs20: BinaryAssociation = BinaryAssociation(
    name="inputs20",
    ends={
        Property(name="IInputPort22", type=workflow_IWorkflowNode, multiplicity=Multiplicity(1, 1)),
        Property(name="node21", type=workflow_IInputPort, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
target1: BinaryAssociation = BinaryAssociation(
    name="target1",
    ends={
        Property(name="IInputPort", type=workflow_ILink, multiplicity=Multiplicity(1, 1)),
        Property(name="links2", type=workflow_IInputPort, multiplicity=Multiplicity(1, 1))
    }
)
source3: BinaryAssociation = BinaryAssociation(
    name="source3",
    ends={
        Property(name="IOutputPort", type=workflow_ILink, multiplicity=Multiplicity(1, 1)),
        Property(name="links4", type=workflow_IOutputPort, multiplicity=Multiplicity(1, 1))
    }
)
node5: BinaryAssociation = BinaryAssociation(
    name="node5",
    ends={
        Property(name="IWorkflowNode", type=workflow_IInputPort, multiplicity=Multiplicity(1, 1)),
        Property(name="inputs", type=workflow_IWorkflowNode, multiplicity=Multiplicity(1, 1))
    }
)
links6: BinaryAssociation = BinaryAssociation(
    name="links6",
    ends={
        Property(name="ILink", type=workflow_IInputPort, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=workflow_ILink, multiplicity=Multiplicity(0, 9999))
    }
)
node7: BinaryAssociation = BinaryAssociation(
    name="node7",
    ends={
        Property(name="IWorkflowNode8", type=workflow_IOutputPort, multiplicity=Multiplicity(1, 1)),
        Property(name="outputs", type=workflow_IWorkflowNode, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_workflow_IPort_IWorkflowElement = Generalization(general=IWorkflowElement, specific=workflow_IPort)
gen_workflow_ILink_IWorkflowElement = Generalization(general=IWorkflowElement, specific=workflow_ILink)
gen_workflow_IWorkflow_IWorkflowElement = Generalization(general=IWorkflowElement, specific=workflow_IWorkflow)
gen_workflow_IWorkflowJob_IWorkflowNode = Generalization(general=IWorkflowNode, specific=workflow_IWorkflowJob)
gen_workflow_IWorkflowNode_IWorkflowElement = Generalization(general=IWorkflowElement, specific=workflow_IWorkflowNode)
gen_workflow_IInputPort_IPort = Generalization(general=IPort, specific=workflow_IInputPort)
gen_workflow_IOutputPort_IPort = Generalization(general=IPort, specific=workflow_IOutputPort)

# Domain Model
domain_model = DomainModel(
    name="workflow",
    types={workflow_IPort, IWorkflowElement, workflow_ILink, workflow_IWorkflow, workflow_IInputPort, workflow_IWorkflowJob, IWorkflowNode, workflow_IWorkflowElement, workflow_IOutputPort, IPort, workflow_IWorkflowNode},
    associations={workflow0, links9, nodes11, links13, workflow16, outputs18, inputs20, target1, source3, node5, links6, node7},
    generalizations={gen_workflow_IPort_IWorkflowElement, gen_workflow_ILink_IWorkflowElement, gen_workflow_IWorkflow_IWorkflowElement, gen_workflow_IWorkflowJob_IWorkflowNode, gen_workflow_IWorkflowNode_IWorkflowElement, gen_workflow_IInputPort_IPort, gen_workflow_IOutputPort_IPort},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)