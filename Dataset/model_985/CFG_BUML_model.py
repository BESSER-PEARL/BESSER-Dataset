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
cfg_cfg = Class(name="cfg::cfg")
cfg_node = Class(name="cfg::node")
cfg_edge = Class(name="cfg::edge")
cfg_startnode = Class(name="cfg::startnode")
node = Class(name="node")
cfg_endnode = Class(name="cfg::endnode")

# cfg_cfg class attributes and methods

# cfg_node class attributes and methods
cfg_node_name: Property = Property(name="name", type=StringType)
cfg_node.attributes={cfg_node_name}

# cfg_edge class attributes and methods

# cfg_startnode class attributes and methods

# node class attributes and methods

# cfg_endnode class attributes and methods

# Relationships
EReference13: BinaryAssociation = BinaryAssociation(
    name="EReference13",
    ends={
        Property(name="cfg_edge5", type=cfg_node, multiplicity=Multiplicity(1, 1)),
        Property(name="cfg_node4", type=cfg_edge, multiplicity=Multiplicity(0, 1))
    }
)
nodes0: BinaryAssociation = BinaryAssociation(
    name="nodes0",
    ends={
        Property(name="cfg_node", type=cfg_cfg, multiplicity=Multiplicity(1, 1)),
        Property(name="cfg_cfg", type=cfg_node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edges1: BinaryAssociation = BinaryAssociation(
    name="edges1",
    ends={
        Property(name="cfg_edge", type=cfg_cfg, multiplicity=Multiplicity(1, 1)),
        Property(name="cfg_cfg2", type=cfg_edge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
incoming6: BinaryAssociation = BinaryAssociation(
    name="incoming6",
    ends={
        Property(name="edge", type=cfg_node, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=cfg_edge, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing7: BinaryAssociation = BinaryAssociation(
    name="outgoing7",
    ends={
        Property(name="edge8", type=cfg_node, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=cfg_edge, multiplicity=Multiplicity(0, 9999))
    }
)
target9: BinaryAssociation = BinaryAssociation(
    name="target9",
    ends={
        Property(name="node", type=cfg_edge, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=cfg_node, multiplicity=Multiplicity(1, 1))
    }
)
EReference010: BinaryAssociation = BinaryAssociation(
    name="EReference010",
    ends={
        Property(name="cfg_node12", type=cfg_edge, multiplicity=Multiplicity(1, 1)),
        Property(name="cfg_edge11", type=cfg_node, multiplicity=Multiplicity(0, 1))
    }
)
source13: BinaryAssociation = BinaryAssociation(
    name="source13",
    ends={
        Property(name="node14", type=cfg_edge, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=cfg_node, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_cfg_startnode_node = Generalization(general=node, specific=cfg_startnode)
gen_cfg_endnode_node = Generalization(general=node, specific=cfg_endnode)

# Domain Model
domain_model = DomainModel(
    name="cfg",
    types={cfg_cfg, cfg_node, cfg_edge, cfg_startnode, node, cfg_endnode},
    associations={EReference13, nodes0, edges1, incoming6, outgoing7, target9, EReference010, source13},
    generalizations={gen_cfg_startnode_node, gen_cfg_endnode_node},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)