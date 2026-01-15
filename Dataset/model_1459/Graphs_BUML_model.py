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
graphs_Edge = Class(name="graphs::Edge")
graphs_CompositeNode = Class(name="graphs::CompositeNode")
Node = Class(name="Node")
graphs_Graph = Class(name="graphs::Graph")
graphs_Node = Class(name="graphs::Node")

# graphs_Edge class attributes and methods
graphs_Edge_weight: Property = Property(name="weight", type=IntegerType)
graphs_Edge.attributes={graphs_Edge_weight}

# graphs_CompositeNode class attributes and methods

# Node class attributes and methods

# graphs_Graph class attributes and methods

# graphs_Node class attributes and methods
graphs_Node_name: Property = Property(name="name", type=StringType)
graphs_Node_m_outputs: Method = Method(name="outputs", parameters={}, type=StringType)
graphs_Node_m_inputs: Method = Method(name="inputs", parameters={}, type=StringType)
graphs_Node.attributes={graphs_Node_name}
graphs_Node.methods={graphs_Node_m_outputs, graphs_Node_m_inputs}

# Relationships
edges1: BinaryAssociation = BinaryAssociation(
    name="edges1",
    ends={
        Property(name="graphs_Edge", type=graphs_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graphs_Graph2", type=graphs_Edge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subGraph3: BinaryAssociation = BinaryAssociation(
    name="subGraph3",
    ends={
        Property(name="graphs_Graph4", type=graphs_CompositeNode, multiplicity=Multiplicity(1, 1)),
        Property(name="graphs_CompositeNode", type=graphs_Graph, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nodes0: BinaryAssociation = BinaryAssociation(
    name="nodes0",
    ends={
        Property(name="graphs_Node", type=graphs_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graphs_Graph", type=graphs_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ends11: BinaryAssociation = BinaryAssociation(
    name="ends11",
    ends={
        Property(name="graphs_Edge12", type=graphs_Node, multiplicity=Multiplicity(2, 2)),
        Property(name="graphs_Node13", type=graphs_Edge, multiplicity=Multiplicity(1, 1))
    }
)
src5: BinaryAssociation = BinaryAssociation(
    name="src5",
    ends={
        Property(name="graphs_Node7", type=graphs_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="graphs_Edge6", type=graphs_Node, multiplicity=Multiplicity(1, 1))
    }
)
tar8: BinaryAssociation = BinaryAssociation(
    name="tar8",
    ends={
        Property(name="graphs_Node10", type=graphs_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="graphs_Edge9", type=graphs_Node, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_graphs_CompositeNode_Node = Generalization(general=Node, specific=graphs_CompositeNode)

# Domain Model
domain_model = DomainModel(
    name="graphs",
    types={graphs_Edge, graphs_CompositeNode, Node, graphs_Graph, graphs_Node},
    associations={edges1, subGraph3, nodes0, ends11, src5, tar8},
    generalizations={gen_graphs_CompositeNode_Node},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)