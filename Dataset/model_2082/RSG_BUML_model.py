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
rsgf_tree_Tree = Class(name="rsgf_tree_Tree")
rsgf_tree_Root = Class(name="rsgf_tree_Root")
Node = Class(name="Node")
BasicNode = Class(name="BasicNode")
rsgf_tree_BasicNode = Class(name="rsgf_tree_BasicNode", is_abstract=True)
rsgf_tree_Coordinator = Class(name="rsgf_tree_Coordinator", is_abstract=True)
rsgf_tree_CDEVSCoordinator = Class(name="rsgf_tree_CDEVSCoordinator")
rsgf_tree_PDEVSCoordinator = Class(name="rsgf_tree_PDEVSCoordinator")
rsgf_tree_FlatCoordinator = Class(name="rsgf_tree_FlatCoordinator")
rsgf_tree_NodeCoordinator = Class(name="rsgf_tree_NodeCoordinator")
rsgf_tree_P_Coordinator = Class(name="rsgf_tree_P_Coordinator")
rsgf_tree_Simulator = Class(name="rsgf_tree_Simulator", is_abstract=True)
rsgf_tree_CDEVSSimulator = Class(name="rsgf_tree_CDEVSSimulator")
rsgf_tree_PDEVSSimulator = Class(name="rsgf_tree_PDEVSSimulator")
rsgf_tree_P_Simulator = Class(name="rsgf_tree_P_Simulator")
Root = Class(name="Root")
Coordinator = Class(name="Coordinator")
Simulator = Class(name="Simulator")
rsgf_tree_Node = Class(name="rsgf_tree_Node", is_abstract=True)
rsgf_bundle_Bundle = Class(name="rsgf_bundle_Bundle")
Skeleton = Class(name="Skeleton")
Process = Class(name="Process")
rsgf_bundle_Process = Class(name="rsgf_bundle_Process")
Middleware = Class(name="Middleware")
rsgf_skeleton_Skeleton = Class(name="rsgf_skeleton_Skeleton")
Tree = Class(name="Tree")
VM = Class(name="VM")
rsgf_vm_VM = Class(name="rsgf_vm_VM")
rsgf_mw_Middleware = Class(name="rsgf_mw_Middleware")

# rsgf_tree_Tree class attributes and methods
rsgf_tree_Tree_ID: Property = Property(name="ID", type=StringType)
rsgf_tree_Tree.attributes={rsgf_tree_Tree_ID}

# rsgf_tree_Root class attributes and methods

# Node class attributes and methods

# BasicNode class attributes and methods

# rsgf_tree_BasicNode class attributes and methods
rsgf_tree_BasicNode_modelName: Property = Property(name="modelName", type=StringType)
rsgf_tree_BasicNode.attributes={rsgf_tree_BasicNode_modelName}

# rsgf_tree_Coordinator class attributes and methods

# rsgf_tree_CDEVSCoordinator class attributes and methods

# rsgf_tree_PDEVSCoordinator class attributes and methods

# rsgf_tree_FlatCoordinator class attributes and methods

# rsgf_tree_NodeCoordinator class attributes and methods

# rsgf_tree_P_Coordinator class attributes and methods

# rsgf_tree_Simulator class attributes and methods

# rsgf_tree_CDEVSSimulator class attributes and methods

# rsgf_tree_PDEVSSimulator class attributes and methods

# rsgf_tree_P_Simulator class attributes and methods

# Root class attributes and methods

# Coordinator class attributes and methods

# Simulator class attributes and methods

# rsgf_tree_Node class attributes and methods
rsgf_tree_Node_ID: Property = Property(name="ID", type=StringType)
rsgf_tree_Node.attributes={rsgf_tree_Node_ID}

# rsgf_bundle_Bundle class attributes and methods
rsgf_bundle_Bundle_ID: Property = Property(name="ID", type=StringType)
rsgf_bundle_Bundle.attributes={rsgf_bundle_Bundle_ID}

# Skeleton class attributes and methods

# Process class attributes and methods

# rsgf_bundle_Process class attributes and methods
rsgf_bundle_Process_ID: Property = Property(name="ID", type=StringType)
rsgf_bundle_Process.attributes={rsgf_bundle_Process_ID}

# Middleware class attributes and methods

# rsgf_skeleton_Skeleton class attributes and methods
rsgf_skeleton_Skeleton_ID: Property = Property(name="ID", type=StringType)
rsgf_skeleton_Skeleton.attributes={rsgf_skeleton_Skeleton_ID}

# Tree class attributes and methods

# VM class attributes and methods

# rsgf_vm_VM class attributes and methods
rsgf_vm_VM_ID: Property = Property(name="ID", type=StringType)
rsgf_vm_VM_protocol: Property = Property(name="protocol", type=StringType)
rsgf_vm_VM.attributes={rsgf_vm_VM_ID, rsgf_vm_VM_protocol}

# rsgf_mw_Middleware class attributes and methods
rsgf_mw_Middleware_m_bind: Method = Method(name="bind", parameters={})
rsgf_mw_Middleware_m_establish: Method = Method(name="establish", parameters={})
rsgf_mw_Middleware_m_send: Method = Method(name="send", parameters={})
rsgf_mw_Middleware.methods={rsgf_mw_Middleware_m_bind, rsgf_mw_Middleware_m_establish, rsgf_mw_Middleware_m_send}

# Relationships
child5: BinaryAssociation = BinaryAssociation(
    name="child5",
    ends={
        Property(name="BasicNode", type=rsgf_tree_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="rsgf_tree_Root", type=BasicNode, multiplicity=Multiplicity(1, 1))
    }
)
children6: BinaryAssociation = BinaryAssociation(
    name="children6",
    ends={
        Property(name="BasicNode7", type=rsgf_tree_Coordinator, multiplicity=Multiplicity(1, 1)),
        Property(name="rsgf_tree_Coordinator", type=BasicNode, multiplicity=Multiplicity(1, 9999))
    }
)
Root0: BinaryAssociation = BinaryAssociation(
    name="Root0",
    ends={
        Property(name="Root", type=rsgf_tree_Tree, multiplicity=Multiplicity(1, 1)),
        Property(name="rsgf_tree_Tree", type=Root, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
Coordinator1: BinaryAssociation = BinaryAssociation(
    name="Coordinator1",
    ends={
        Property(name="Coordinator", type=rsgf_tree_Tree, multiplicity=Multiplicity(1, 1)),
        Property(name="rsgf_tree_Tree2", type=Coordinator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Simulator3: BinaryAssociation = BinaryAssociation(
    name="Simulator3",
    ends={
        Property(name="Simulator", type=rsgf_tree_Tree, multiplicity=Multiplicity(1, 1)),
        Property(name="rsgf_tree_Tree4", type=Simulator, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
rootskel9: BinaryAssociation = BinaryAssociation(
    name="rootskel9",
    ends={
        Property(name="Root11", type=rsgf_skeleton_Skeleton, multiplicity=Multiplicity(1, 1)),
        Property(name="rsgf_skeleton_Skeleton10", type=Root, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
skeleton12: BinaryAssociation = BinaryAssociation(
    name="skeleton12",
    ends={
        Property(name="Skeleton", type=rsgf_bundle_Bundle, multiplicity=Multiplicity(1, 1)),
        Property(name="rsgf_bundle_Bundle", type=Skeleton, multiplicity=Multiplicity(1, 1))
    }
)
Process13: BinaryAssociation = BinaryAssociation(
    name="Process13",
    ends={
        Property(name="Process", type=rsgf_bundle_Bundle, multiplicity=Multiplicity(1, 1)),
        Property(name="rsgf_bundle_Bundle14", type=Process, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
nodes15: BinaryAssociation = BinaryAssociation(
    name="nodes15",
    ends={
        Property(name="Node", type=rsgf_bundle_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="rsgf_bundle_Process", type=Node, multiplicity=Multiplicity(1, 9999))
    }
)
middleware16: BinaryAssociation = BinaryAssociation(
    name="middleware16",
    ends={
        Property(name="Middleware", type=rsgf_bundle_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="rsgf_bundle_Process17", type=Middleware, multiplicity=Multiplicity(1, 1))
    }
)
tree8: BinaryAssociation = BinaryAssociation(
    name="tree8",
    ends={
        Property(name="Tree", type=rsgf_skeleton_Skeleton, multiplicity=Multiplicity(1, 1)),
        Property(name="rsgf_skeleton_Skeleton", type=Tree, multiplicity=Multiplicity(0, 1))
    }
)
uses20: BinaryAssociation = BinaryAssociation(
    name="uses20",
    ends={
        Property(name="VM", type=rsgf_mw_Middleware, multiplicity=Multiplicity(1, 1)),
        Property(name="rsgf_mw_Middleware21", type=VM, multiplicity=Multiplicity(0, 1))
    }
)
process18: BinaryAssociation = BinaryAssociation(
    name="process18",
    ends={
        Property(name="Process19", type=rsgf_mw_Middleware, multiplicity=Multiplicity(1, 1)),
        Property(name="rsgf_mw_Middleware", type=Process, multiplicity=Multiplicity(1, 9999))
    }
)

# Generalizations
gen_rsgf_tree_Root_Node = Generalization(general=Node, specific=rsgf_tree_Root)
gen_rsgf_tree_BasicNode_Node = Generalization(general=Node, specific=rsgf_tree_BasicNode)
gen_rsgf_tree_Coordinator_BasicNode = Generalization(general=BasicNode, specific=rsgf_tree_Coordinator)
gen_rsgf_tree_CDEVSCoordinator_Coordinator = Generalization(general=Coordinator, specific=rsgf_tree_CDEVSCoordinator)
gen_rsgf_tree_PDEVSCoordinator_Coordinator = Generalization(general=Coordinator, specific=rsgf_tree_PDEVSCoordinator)
gen_rsgf_tree_FlatCoordinator_Coordinator = Generalization(general=Coordinator, specific=rsgf_tree_FlatCoordinator)
gen_rsgf_tree_NodeCoordinator_Coordinator = Generalization(general=Coordinator, specific=rsgf_tree_NodeCoordinator)
gen_rsgf_tree_P_Coordinator_Coordinator = Generalization(general=Coordinator, specific=rsgf_tree_P_Coordinator)
gen_rsgf_tree_Simulator_BasicNode = Generalization(general=BasicNode, specific=rsgf_tree_Simulator)
gen_rsgf_tree_CDEVSSimulator_Simulator = Generalization(general=Simulator, specific=rsgf_tree_CDEVSSimulator)
gen_rsgf_tree_PDEVSSimulator_Simulator = Generalization(general=Simulator, specific=rsgf_tree_PDEVSSimulator)
gen_rsgf_tree_P_Simulator_Simulator = Generalization(general=Simulator, specific=rsgf_tree_P_Simulator)

# Domain Model
domain_model = DomainModel(
    name="rsgf",
    types={rsgf_tree_Tree, rsgf_tree_Root, Node, BasicNode, rsgf_tree_BasicNode, rsgf_tree_Coordinator, rsgf_tree_CDEVSCoordinator, rsgf_tree_PDEVSCoordinator, rsgf_tree_FlatCoordinator, rsgf_tree_NodeCoordinator, rsgf_tree_P_Coordinator, rsgf_tree_Simulator, rsgf_tree_CDEVSSimulator, rsgf_tree_PDEVSSimulator, rsgf_tree_P_Simulator, Root, Coordinator, Simulator, rsgf_tree_Node, rsgf_bundle_Bundle, Skeleton, Process, rsgf_bundle_Process, Middleware, rsgf_skeleton_Skeleton, Tree, VM, rsgf_vm_VM, rsgf_mw_Middleware},
    associations={child5, children6, Root0, Coordinator1, Simulator3, rootskel9, skeleton12, Process13, nodes15, middleware16, tree8, uses20, process18},
    generalizations={gen_rsgf_tree_Root_Node, gen_rsgf_tree_BasicNode_Node, gen_rsgf_tree_Coordinator_BasicNode, gen_rsgf_tree_CDEVSCoordinator_Coordinator, gen_rsgf_tree_PDEVSCoordinator_Coordinator, gen_rsgf_tree_FlatCoordinator_Coordinator, gen_rsgf_tree_NodeCoordinator_Coordinator, gen_rsgf_tree_P_Coordinator_Coordinator, gen_rsgf_tree_Simulator_BasicNode, gen_rsgf_tree_CDEVSSimulator_Simulator, gen_rsgf_tree_PDEVSSimulator_Simulator, gen_rsgf_tree_P_Simulator_Simulator},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)