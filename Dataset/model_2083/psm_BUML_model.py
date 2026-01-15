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
Processor = Class(name="Processor")
ws_middleware_Middleware = Class(name="ws::middleware::Middleware", is_abstract=True)
VM = Class(name="VM")
Process = Class(name="Process")
ws_middleware_WebService = Class(name="ws::middleware::WebService")
Middleware = Class(name="Middleware")
Stub = Class(name="Stub")
Repository = Class(name="Repository")
ws_middleware_VM = Class(name="ws::middleware::VM")
Coordinator = Class(name="Coordinator")
ws_middleware_Processor = Class(name="ws::middleware::Processor")
ws_middleware_ServiceImpl = Class(name="ws::middleware::ServiceImpl")
ServiceDescription = Class(name="ServiceDescription")
ws_middleware_Stub = Class(name="ws::middleware::Stub")
ServiceImpl = Class(name="ServiceImpl")
ws_middleware_Repository = Class(name="ws::middleware::Repository")
ws_middleware_ServiceDescription = Class(name="ws::middleware::ServiceDescription", is_abstract=True)
ws_tree_Tree = Class(name="ws::tree::Tree")
Root = Class(name="Root")
ws_tree_P_Coordinator = Class(name="ws::tree::P::Coordinator")
ws_tree_Simulator = Class(name="ws::tree::Simulator", is_abstract=True)
ws_tree_CDEVSSimulator = Class(name="ws::tree::CDEVSSimulator")
Simulator = Class(name="Simulator")
ws_tree_Root = Class(name="ws::tree::Root")
Node = Class(name="Node")
BasicNode = Class(name="BasicNode")
ws_tree_Coordinator = Class(name="ws::tree::Coordinator")
ws_tree_CDEVSCoordinator = Class(name="ws::tree::CDEVSCoordinator")
ws_tree_PDEVSCoordinator = Class(name="ws::tree::PDEVSCoordinator")
ws_tree_FlatCoordinator = Class(name="ws::tree::FlatCoordinator")
ws_tree_NodeCoordinator = Class(name="ws::tree::NodeCoordinator")
ws_tree_PDEVSSimulator = Class(name="ws::tree::PDEVSSimulator")
ws_tree_P_Simulator = Class(name="ws::tree::P::Simulator")
ws_tree_BasicNode = Class(name="ws::tree::BasicNode", is_abstract=True)
ws_tree_Node = Class(name="ws::tree::Node", is_abstract=True)
ws_skeleton_Skeleton = Class(name="ws::skeleton::Skeleton")
Tree = Class(name="Tree")
ws_bundle_Bundle = Class(name="ws::bundle::Bundle")
Skeleton = Class(name="Skeleton")
ws_bundle_Process = Class(name="ws::bundle::Process")

# Processor class attributes and methods

# ws_middleware_Middleware class attributes and methods
ws_middleware_Middleware_m_bind: Method = Method(name="bind", parameters={})
ws_middleware_Middleware_m_establish: Method = Method(name="establish", parameters={})
ws_middleware_Middleware_m_send: Method = Method(name="send", parameters={})
ws_middleware_Middleware.methods={ws_middleware_Middleware_m_establish, ws_middleware_Middleware_m_bind, ws_middleware_Middleware_m_send}

# VM class attributes and methods

# Process class attributes and methods

# ws_middleware_WebService class attributes and methods

# Middleware class attributes and methods

# Stub class attributes and methods

# Repository class attributes and methods

# ws_middleware_VM class attributes and methods
ws_middleware_VM_ID: Property = Property(name="ID", type=StringType)
ws_middleware_VM_protocol: Property = Property(name="protocol", type=StringType)
ws_middleware_VM.attributes={ws_middleware_VM_ID, ws_middleware_VM_protocol}

# Coordinator class attributes and methods

# ws_middleware_Processor class attributes and methods
ws_middleware_Processor_ID: Property = Property(name="ID", type=StringType)
ws_middleware_Processor_IP: Property = Property(name="IP", type=StringType)
ws_middleware_Processor_m_receive: Method = Method(name="receive", parameters={})
ws_middleware_Processor.attributes={ws_middleware_Processor_ID, ws_middleware_Processor_IP}
ws_middleware_Processor.methods={ws_middleware_Processor_m_receive}

# ws_middleware_ServiceImpl class attributes and methods
ws_middleware_ServiceImpl_m_receive: Method = Method(name="receive", parameters={})
ws_middleware_ServiceImpl.methods={ws_middleware_ServiceImpl_m_receive}

# ServiceDescription class attributes and methods

# ws_middleware_Stub class attributes and methods
ws_middleware_Stub_m_receive: Method = Method(name="receive", parameters={})
ws_middleware_Stub.methods={ws_middleware_Stub_m_receive}

# ServiceImpl class attributes and methods

# ws_middleware_Repository class attributes and methods
ws_middleware_Repository_m_lookup: Method = Method(name="lookup", parameters={})
ws_middleware_Repository_m_rebind: Method = Method(name="rebind", parameters={})
ws_middleware_Repository.methods={ws_middleware_Repository_m_lookup, ws_middleware_Repository_m_rebind}

# ws_middleware_ServiceDescription class attributes and methods

# ws_tree_Tree class attributes and methods
ws_tree_Tree_ID: Property = Property(name="ID", type=StringType)
ws_tree_Tree.attributes={ws_tree_Tree_ID}

# Root class attributes and methods

# ws_tree_P_Coordinator class attributes and methods

# ws_tree_Simulator class attributes and methods

# ws_tree_CDEVSSimulator class attributes and methods

# Simulator class attributes and methods

# ws_tree_Root class attributes and methods

# Node class attributes and methods

# BasicNode class attributes and methods

# ws_tree_Coordinator class attributes and methods

# ws_tree_CDEVSCoordinator class attributes and methods

# ws_tree_PDEVSCoordinator class attributes and methods

# ws_tree_FlatCoordinator class attributes and methods

# ws_tree_NodeCoordinator class attributes and methods

# ws_tree_PDEVSSimulator class attributes and methods

# ws_tree_P_Simulator class attributes and methods

# ws_tree_BasicNode class attributes and methods
ws_tree_BasicNode_modelName: Property = Property(name="modelName", type=StringType)
ws_tree_BasicNode.attributes={ws_tree_BasicNode_modelName}

# ws_tree_Node class attributes and methods
ws_tree_Node_ID: Property = Property(name="ID", type=StringType)
ws_tree_Node.attributes={ws_tree_Node_ID}

# ws_skeleton_Skeleton class attributes and methods
ws_skeleton_Skeleton_ID: Property = Property(name="ID", type=StringType)
ws_skeleton_Skeleton.attributes={ws_skeleton_Skeleton_ID}

# Tree class attributes and methods

# ws_bundle_Bundle class attributes and methods
ws_bundle_Bundle_ID: Property = Property(name="ID", type=StringType)
ws_bundle_Bundle.attributes={ws_bundle_Bundle_ID}

# Skeleton class attributes and methods

# ws_bundle_Process class attributes and methods
ws_bundle_Process_ID: Property = Property(name="ID", type=StringType)
ws_bundle_Process_m_receive: Method = Method(name="receive", parameters={})
ws_bundle_Process.attributes={ws_bundle_Process_ID}
ws_bundle_Process.methods={ws_bundle_Process_m_receive}

# Relationships
uses0: BinaryAssociation = BinaryAssociation(
    name="uses0",
    ends={
        Property(name="VM", type=ws_middleware_Middleware, multiplicity=Multiplicity(1, 1)),
        Property(name="ws_middleware_Middleware", type=VM, multiplicity=Multiplicity(0, 1))
    }
)
process1: BinaryAssociation = BinaryAssociation(
    name="process1",
    ends={
        Property(name="Process", type=ws_middleware_Middleware, multiplicity=Multiplicity(1, 1)),
        Property(name="ws_middleware_Middleware2", type=Process, multiplicity=Multiplicity(1, 9999))
    }
)
stubs3: BinaryAssociation = BinaryAssociation(
    name="stubs3",
    ends={
        Property(name="Stub", type=ws_middleware_WebService, multiplicity=Multiplicity(1, 1)),
        Property(name="ws_middleware_WebService", type=Stub, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
registry4: BinaryAssociation = BinaryAssociation(
    name="registry4",
    ends={
        Property(name="Repository", type=ws_middleware_WebService, multiplicity=Multiplicity(1, 1)),
        Property(name="ws_middleware_WebService5", type=Repository, multiplicity=Multiplicity(1, 1))
    }
)
Root9: BinaryAssociation = BinaryAssociation(
    name="Root9",
    ends={
        Property(name="Root", type=ws_tree_Tree, multiplicity=Multiplicity(1, 1)),
        Property(name="ws_tree_Tree", type=Root, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
processors6: BinaryAssociation = BinaryAssociation(
    name="processors6",
    ends={
        Property(name="Processor", type=ws_middleware_VM, multiplicity=Multiplicity(1, 1)),
        Property(name="ws_middleware_VM", type=Processor, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
impl7: BinaryAssociation = BinaryAssociation(
    name="impl7",
    ends={
        Property(name="ServiceImpl", type=ws_middleware_Stub, multiplicity=Multiplicity(1, 1)),
        Property(name="ws_middleware_Stub", type=ServiceImpl, multiplicity=Multiplicity(1, 1))
    }
)
services8: BinaryAssociation = BinaryAssociation(
    name="services8",
    ends={
        Property(name="ServiceDescription", type=ws_middleware_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="ws_middleware_Repository", type=ServiceDescription, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
Coordinator10: BinaryAssociation = BinaryAssociation(
    name="Coordinator10",
    ends={
        Property(name="Coordinator", type=ws_tree_Tree, multiplicity=Multiplicity(1, 1)),
        Property(name="ws_tree_Tree11", type=Coordinator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Simulator12: BinaryAssociation = BinaryAssociation(
    name="Simulator12",
    ends={
        Property(name="Simulator", type=ws_tree_Tree, multiplicity=Multiplicity(1, 1)),
        Property(name="ws_tree_Tree13", type=Simulator, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
child14: BinaryAssociation = BinaryAssociation(
    name="child14",
    ends={
        Property(name="BasicNode", type=ws_tree_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="ws_tree_Root", type=BasicNode, multiplicity=Multiplicity(1, 1))
    }
)
children15: BinaryAssociation = BinaryAssociation(
    name="children15",
    ends={
        Property(name="BasicNode16", type=ws_tree_Coordinator, multiplicity=Multiplicity(1, 1)),
        Property(name="ws_tree_Coordinator", type=BasicNode, multiplicity=Multiplicity(1, 9999))
    }
)
skeleton21: BinaryAssociation = BinaryAssociation(
    name="skeleton21",
    ends={
        Property(name="ws_bundle_Bundle", type=Skeleton, multiplicity=Multiplicity(1, 1)),
        Property(name="Skeleton", type=ws_bundle_Bundle, multiplicity=Multiplicity(1, 1))
    }
)
Process22: BinaryAssociation = BinaryAssociation(
    name="Process22",
    ends={
        Property(name="Process24", type=ws_bundle_Bundle, multiplicity=Multiplicity(1, 1)),
        Property(name="ws_bundle_Bundle23", type=Process, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
tree17: BinaryAssociation = BinaryAssociation(
    name="tree17",
    ends={
        Property(name="Tree", type=ws_skeleton_Skeleton, multiplicity=Multiplicity(1, 1)),
        Property(name="ws_skeleton_Skeleton", type=Tree, multiplicity=Multiplicity(0, 1))
    }
)
rootskel18: BinaryAssociation = BinaryAssociation(
    name="rootskel18",
    ends={
        Property(name="Root20", type=ws_skeleton_Skeleton, multiplicity=Multiplicity(1, 1)),
        Property(name="ws_skeleton_Skeleton19", type=Root, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
nodes25: BinaryAssociation = BinaryAssociation(
    name="nodes25",
    ends={
        Property(name="Node", type=ws_bundle_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="ws_bundle_Process", type=Node, multiplicity=Multiplicity(1, 9999))
    }
)
middleware26: BinaryAssociation = BinaryAssociation(
    name="middleware26",
    ends={
        Property(name="Middleware", type=ws_bundle_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="ws_bundle_Process27", type=Middleware, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_ws_middleware_WebService_Middleware = Generalization(general=Middleware, specific=ws_middleware_WebService)
gen_ws_middleware_ServiceImpl_ServiceDescription = Generalization(general=ServiceDescription, specific=ws_middleware_ServiceImpl)
gen_ws_tree_P_Coordinator_Coordinator = Generalization(general=Coordinator, specific=ws_tree_P_Coordinator)
gen_ws_tree_Simulator_BasicNode = Generalization(general=BasicNode, specific=ws_tree_Simulator)
gen_ws_tree_Root_Node = Generalization(general=Node, specific=ws_tree_Root)
gen_ws_tree_Coordinator_BasicNode = Generalization(general=BasicNode, specific=ws_tree_Coordinator)
gen_ws_tree_CDEVSCoordinator_Coordinator = Generalization(general=Coordinator, specific=ws_tree_CDEVSCoordinator)
gen_ws_tree_PDEVSCoordinator_Coordinator = Generalization(general=Coordinator, specific=ws_tree_PDEVSCoordinator)
gen_ws_tree_FlatCoordinator_Coordinator = Generalization(general=Coordinator, specific=ws_tree_FlatCoordinator)
gen_ws_tree_NodeCoordinator_Coordinator = Generalization(general=Coordinator, specific=ws_tree_NodeCoordinator)
gen_ws_tree_CDEVSSimulator_Simulator = Generalization(general=Simulator, specific=ws_tree_CDEVSSimulator)
gen_ws_tree_PDEVSSimulator_Simulator = Generalization(general=Simulator, specific=ws_tree_PDEVSSimulator)
gen_ws_tree_P_Simulator_Simulator = Generalization(general=Simulator, specific=ws_tree_P_Simulator)
gen_ws_tree_BasicNode_Node = Generalization(general=Node, specific=ws_tree_BasicNode)

# Domain Model
domain_model = DomainModel(
    name="ws",
    types={Processor, ws_middleware_Middleware, VM, Process, ws_middleware_WebService, Middleware, Stub, Repository, ws_middleware_VM, Coordinator, ws_middleware_Processor, ws_middleware_ServiceImpl, ServiceDescription, ws_middleware_Stub, ServiceImpl, ws_middleware_Repository, ws_middleware_ServiceDescription, ws_tree_Tree, Root, ws_tree_P_Coordinator, ws_tree_Simulator, ws_tree_CDEVSSimulator, Simulator, ws_tree_Root, Node, BasicNode, ws_tree_Coordinator, ws_tree_CDEVSCoordinator, ws_tree_PDEVSCoordinator, ws_tree_FlatCoordinator, ws_tree_NodeCoordinator, ws_tree_PDEVSSimulator, ws_tree_P_Simulator, ws_tree_BasicNode, ws_tree_Node, ws_skeleton_Skeleton, Tree, ws_bundle_Bundle, Skeleton, ws_bundle_Process},
    associations={uses0, process1, stubs3, registry4, Root9, processors6, impl7, services8, Coordinator10, Simulator12, child14, children15, skeleton21, Process22, tree17, rootskel18, nodes25, middleware26},
    generalizations={gen_ws_middleware_WebService_Middleware, gen_ws_middleware_ServiceImpl_ServiceDescription, gen_ws_tree_P_Coordinator_Coordinator, gen_ws_tree_Simulator_BasicNode, gen_ws_tree_Root_Node, gen_ws_tree_Coordinator_BasicNode, gen_ws_tree_CDEVSCoordinator_Coordinator, gen_ws_tree_PDEVSCoordinator_Coordinator, gen_ws_tree_FlatCoordinator_Coordinator, gen_ws_tree_NodeCoordinator_Coordinator, gen_ws_tree_CDEVSSimulator_Simulator, gen_ws_tree_PDEVSSimulator_Simulator, gen_ws_tree_P_Simulator_Simulator, gen_ws_tree_BasicNode_Node},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)