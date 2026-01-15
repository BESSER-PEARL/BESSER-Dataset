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
processModels_CompositeTask = Class(name="processModels::CompositeTask")
Task = Class(name="Task")
processModels_FlowEdge = Class(name="processModels::FlowEdge")
processModels_ProcessModel = Class(name="processModels::ProcessModel")
processModels_Node = Class(name="processModels::Node", is_abstract=True)
processModels_Task = Class(name="processModels::Task")
Node = Class(name="Node")

# processModels_CompositeTask class attributes and methods

# Task class attributes and methods

# processModels_FlowEdge class attributes and methods
processModels_FlowEdge_m_input: Method = Method(name="input", parameters={}, type=Node)
processModels_FlowEdge_m_output: Method = Method(name="output", parameters={}, type=Node)
processModels_FlowEdge.methods={processModels_FlowEdge_m_output, processModels_FlowEdge_m_input}

# processModels_ProcessModel class attributes and methods
processModels_ProcessModel_m_terminatingTasks: Method = Method(name="terminatingTasks", parameters={}, type=StringType)
processModels_ProcessModel_m_nodes: Method = Method(name="nodes", parameters={}, type=StringType)
processModels_ProcessModel_m_edges: Method = Method(name="edges", parameters={}, type=StringType)
processModels_ProcessModel.methods={processModels_ProcessModel_m_terminatingTasks, processModels_ProcessModel_m_edges, processModels_ProcessModel_m_nodes}

# processModels_Node class attributes and methods

# processModels_Task class attributes and methods
processModels_Task_m_name: Method = Method(name="name", parameters={}, type=StringType)
processModels_Task.methods={processModels_Task_m_name}

# Node class attributes and methods

# Generalizations
gen_processModels_CompositeTask_Task = Generalization(general=Task, specific=processModels_CompositeTask)
gen_processModels_Task_Node = Generalization(general=Node, specific=processModels_Task)

# Domain Model
domain_model = DomainModel(
    name="processModels",
    types={processModels_CompositeTask, Task, processModels_FlowEdge, processModels_ProcessModel, processModels_Node, processModels_Task, Node},
    associations={},
    generalizations={gen_processModels_CompositeTask_Task, gen_processModels_Task_Node},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)