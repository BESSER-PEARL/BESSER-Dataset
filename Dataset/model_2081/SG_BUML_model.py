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
sgf_tree_Tree = Class(name="sgf_tree_Tree")
Root = Class(name="Root")
sgf_tree_Node = Class(name="sgf_tree_Node", is_abstract=True)
sgf_skeleton_Skeleton = Class(name="sgf_skeleton_Skeleton")
Tree = Class(name="Tree")
sgf_bundle_Bundle = Class(name="sgf_bundle_Bundle")
Coordinator = Class(name="Coordinator")
Simulator = Class(name="Simulator")
sgf_tree_Root = Class(name="sgf_tree_Root")
Node = Class(name="Node")
BasicNode = Class(name="BasicNode")
sgf_tree_Coordinator = Class(name="sgf_tree_Coordinator")
sgf_tree_Simulator = Class(name="sgf_tree_Simulator")
sgf_tree_BasicNode = Class(name="sgf_tree_BasicNode", is_abstract=True)
Processor = Class(name="Processor")
sgf_vm_Processor = Class(name="sgf_vm_Processor")
sgf_graph_Graph = Class(name="sgf_graph_Graph")
Skeleton = Class(name="Skeleton")
Process = Class(name="Process")
sgf_bundle_Process = Class(name="sgf_bundle_Process")
sgf_vm_VM = Class(name="sgf_vm_VM")
Bundle = Class(name="Bundle")
VM = Class(name="VM")
Mapping = Class(name="Mapping")
sgf_graph_Mapping = Class(name="sgf_graph_Mapping")

# sgf_tree_Tree class attributes and methods
sgf_tree_Tree_ID: Property = Property(name="ID", type=StringType)
sgf_tree_Tree.attributes={sgf_tree_Tree_ID}

# Root class attributes and methods

# sgf_tree_Node class attributes and methods
sgf_tree_Node_ID: Property = Property(name="ID", type=StringType)
sgf_tree_Node.attributes={sgf_tree_Node_ID}

# sgf_skeleton_Skeleton class attributes and methods
sgf_skeleton_Skeleton_ID: Property = Property(name="ID", type=StringType)
sgf_skeleton_Skeleton.attributes={sgf_skeleton_Skeleton_ID}

# Tree class attributes and methods

# sgf_bundle_Bundle class attributes and methods
sgf_bundle_Bundle_ID: Property = Property(name="ID", type=StringType)
sgf_bundle_Bundle.attributes={sgf_bundle_Bundle_ID}

# Coordinator class attributes and methods

# Simulator class attributes and methods

# sgf_tree_Root class attributes and methods

# Node class attributes and methods

# BasicNode class attributes and methods

# sgf_tree_Coordinator class attributes and methods

# sgf_tree_Simulator class attributes and methods

# sgf_tree_BasicNode class attributes and methods
sgf_tree_BasicNode_modelName: Property = Property(name="modelName", type=StringType)
sgf_tree_BasicNode.attributes={sgf_tree_BasicNode_modelName}

# Processor class attributes and methods

# sgf_vm_Processor class attributes and methods
sgf_vm_Processor_ID: Property = Property(name="ID", type=StringType)
sgf_vm_Processor_IP: Property = Property(name="IP", type=StringType)
sgf_vm_Processor.attributes={sgf_vm_Processor_ID, sgf_vm_Processor_IP}

# sgf_graph_Graph class attributes and methods
sgf_graph_Graph_ID: Property = Property(name="ID", type=StringType)
sgf_graph_Graph.attributes={sgf_graph_Graph_ID}

# Skeleton class attributes and methods

# Process class attributes and methods

# sgf_bundle_Process class attributes and methods
sgf_bundle_Process_ID: Property = Property(name="ID", type=StringType)
sgf_bundle_Process.attributes={sgf_bundle_Process_ID}

# sgf_vm_VM class attributes and methods
sgf_vm_VM_ID: Property = Property(name="ID", type=StringType)
sgf_vm_VM_protocol: Property = Property(name="protocol", type=StringType)
sgf_vm_VM.attributes={sgf_vm_VM_ID, sgf_vm_VM_protocol}

# Bundle class attributes and methods

# VM class attributes and methods

# Mapping class attributes and methods

# sgf_graph_Mapping class attributes and methods
sgf_graph_Mapping_ID: Property = Property(name="ID", type=StringType)
sgf_graph_Mapping.attributes={sgf_graph_Mapping_ID}

# Relationships
Root0: BinaryAssociation = BinaryAssociation(
    name="Root0",
    ends={
        Property(name="Root", type=sgf_tree_Tree, multiplicity=Multiplicity(1, 1)),
        Property(name="sgf_tree_Tree", type=Root, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tree8: BinaryAssociation = BinaryAssociation(
    name="tree8",
    ends={
        Property(name="Tree", type=sgf_skeleton_Skeleton, multiplicity=Multiplicity(1, 1)),
        Property(name="sgf_skeleton_Skeleton", type=Tree, multiplicity=Multiplicity(0, 1))
    }
)
rootskel9: BinaryAssociation = BinaryAssociation(
    name="rootskel9",
    ends={
        Property(name="Root11", type=sgf_skeleton_Skeleton, multiplicity=Multiplicity(1, 1)),
        Property(name="sgf_skeleton_Skeleton10", type=Root, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
Coordinator1: BinaryAssociation = BinaryAssociation(
    name="Coordinator1",
    ends={
        Property(name="Coordinator", type=sgf_tree_Tree, multiplicity=Multiplicity(1, 1)),
        Property(name="sgf_tree_Tree2", type=Coordinator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Simulator3: BinaryAssociation = BinaryAssociation(
    name="Simulator3",
    ends={
        Property(name="Simulator", type=sgf_tree_Tree, multiplicity=Multiplicity(1, 1)),
        Property(name="sgf_tree_Tree4", type=Simulator, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
child5: BinaryAssociation = BinaryAssociation(
    name="child5",
    ends={
        Property(name="BasicNode", type=sgf_tree_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="sgf_tree_Root", type=BasicNode, multiplicity=Multiplicity(1, 1))
    }
)
children6: BinaryAssociation = BinaryAssociation(
    name="children6",
    ends={
        Property(name="BasicNode7", type=sgf_tree_Coordinator, multiplicity=Multiplicity(1, 1)),
        Property(name="sgf_tree_Coordinator", type=BasicNode, multiplicity=Multiplicity(1, 9999))
    }
)
processors16: BinaryAssociation = BinaryAssociation(
    name="processors16",
    ends={
        Property(name="Processor", type=sgf_vm_VM, multiplicity=Multiplicity(1, 1)),
        Property(name="sgf_vm_VM", type=Processor, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
skeleton12: BinaryAssociation = BinaryAssociation(
    name="skeleton12",
    ends={
        Property(name="Skeleton", type=sgf_bundle_Bundle, multiplicity=Multiplicity(1, 1)),
        Property(name="sgf_bundle_Bundle", type=Skeleton, multiplicity=Multiplicity(1, 1))
    }
)
Process13: BinaryAssociation = BinaryAssociation(
    name="Process13",
    ends={
        Property(name="Process", type=sgf_bundle_Bundle, multiplicity=Multiplicity(1, 1)),
        Property(name="sgf_bundle_Bundle14", type=Process, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
nodes15: BinaryAssociation = BinaryAssociation(
    name="nodes15",
    ends={
        Property(name="Node", type=sgf_bundle_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="sgf_bundle_Process", type=Node, multiplicity=Multiplicity(1, 9999))
    }
)
processor24: BinaryAssociation = BinaryAssociation(
    name="processor24",
    ends={
        Property(name="Processor26", type=sgf_graph_Mapping, multiplicity=Multiplicity(1, 1)),
        Property(name="sgf_graph_Mapping25", type=Processor, multiplicity=Multiplicity(1, 1))
    }
)
bundle17: BinaryAssociation = BinaryAssociation(
    name="bundle17",
    ends={
        Property(name="Bundle", type=sgf_graph_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="sgf_graph_Graph", type=Bundle, multiplicity=Multiplicity(1, 1))
    }
)
vm18: BinaryAssociation = BinaryAssociation(
    name="vm18",
    ends={
        Property(name="VM", type=sgf_graph_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="sgf_graph_Graph19", type=VM, multiplicity=Multiplicity(1, 1))
    }
)
mappings20: BinaryAssociation = BinaryAssociation(
    name="mappings20",
    ends={
        Property(name="Mapping", type=sgf_graph_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="sgf_graph_Graph21", type=Mapping, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
processes22: BinaryAssociation = BinaryAssociation(
    name="processes22",
    ends={
        Property(name="Process23", type=sgf_graph_Mapping, multiplicity=Multiplicity(1, 1)),
        Property(name="sgf_graph_Mapping", type=Process, multiplicity=Multiplicity(1, 9999))
    }
)

# Generalizations
gen_sgf_tree_Root_Node = Generalization(general=Node, specific=sgf_tree_Root)
gen_sgf_tree_Coordinator_BasicNode = Generalization(general=BasicNode, specific=sgf_tree_Coordinator)
gen_sgf_tree_Simulator_BasicNode = Generalization(general=BasicNode, specific=sgf_tree_Simulator)
gen_sgf_tree_BasicNode_Node = Generalization(general=Node, specific=sgf_tree_BasicNode)

# Domain Model
domain_model = DomainModel(
    name="sgf",
    types={sgf_tree_Tree, Root, sgf_tree_Node, sgf_skeleton_Skeleton, Tree, sgf_bundle_Bundle, Coordinator, Simulator, sgf_tree_Root, Node, BasicNode, sgf_tree_Coordinator, sgf_tree_Simulator, sgf_tree_BasicNode, Processor, sgf_vm_Processor, sgf_graph_Graph, Skeleton, Process, sgf_bundle_Process, sgf_vm_VM, Bundle, VM, Mapping, sgf_graph_Mapping},
    associations={Root0, tree8, rootskel9, Coordinator1, Simulator3, child5, children6, processors16, skeleton12, Process13, nodes15, processor24, bundle17, vm18, mappings20, processes22},
    generalizations={gen_sgf_tree_Root_Node, gen_sgf_tree_Coordinator_BasicNode, gen_sgf_tree_Simulator_BasicNode, gen_sgf_tree_BasicNode_Node},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)