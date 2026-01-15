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
graph_Edge = Class(name="graph::Edge")
Identifiable = Class(name="Identifiable")
graph_Node = Class(name="graph::Node")
graph_GraphAsset = Class(name="graph::GraphAsset")
graph_Identifiable = Class(name="graph::Identifiable", is_abstract=True)
graph_Graph = Class(name="graph::Graph")
graph_NodeResponsibility = Class(name="graph::NodeResponsibility")
graph_Subgraphs = Class(name="graph::Subgraphs")

# graph_Edge class attributes and methods
graph_Edge_EdgeLabel: Property = Property(name="EdgeLabel", type=IntegerType)
graph_Edge_visited: Property = Property(name="visited", type=BooleanType)
graph_Edge.attributes={graph_Edge_visited, graph_Edge_EdgeLabel}

# Identifiable class attributes and methods

# graph_Node class attributes and methods
graph_Node_name: Property = Property(name="name", type=StringType)
graph_Node_AttackerObservation: Property = Property(name="AttackerObservation", type=IntegerType)
graph_Node_visited: Property = Property(name="visited", type=BooleanType)
graph_Node_Attacker: Property = Property(name="Attacker", type=BooleanType)
graph_Node.attributes={graph_Node_name, graph_Node_Attacker, graph_Node_AttackerObservation, graph_Node_visited}

# graph_GraphAsset class attributes and methods
graph_GraphAsset_Encrypted: Property = Property(name="Encrypted", type=BooleanType)
graph_GraphAsset_Label: Property = Property(name="Label", type=IntegerType)
graph_GraphAsset.attributes={graph_GraphAsset_Encrypted, graph_GraphAsset_Label}

# graph_Identifiable class attributes and methods
graph_Identifiable_ID: Property = Property(name="ID", type=StringType)
graph_Identifiable_number: Property = Property(name="number", type=IntegerType)
graph_Identifiable.attributes={graph_Identifiable_ID, graph_Identifiable_number}

# graph_Graph class attributes and methods

# graph_NodeResponsibility class attributes and methods
graph_NodeResponsibility_operation: Property = Property(name="operation", type=StringType)
graph_NodeResponsibility_m_findMostRestrictiveLabel: Method = Method(name="findMostRestrictiveLabel", parameters={}, type=StringType)
graph_NodeResponsibility_m_findLeastRestrictiveLabel: Method = Method(name="findLeastRestrictiveLabel", parameters={}, type=StringType)
graph_NodeResponsibility.attributes={graph_NodeResponsibility_operation}
graph_NodeResponsibility.methods={graph_NodeResponsibility_m_findLeastRestrictiveLabel, graph_NodeResponsibility_m_findMostRestrictiveLabel}

# graph_Subgraphs class attributes and methods

# Relationships
source6: BinaryAssociation = BinaryAssociation(
    name="source6",
    ends={
        Property(name="graph_Node8", type=graph_GraphAsset, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_GraphAsset7", type=graph_Node, multiplicity=Multiplicity(1, 1))
    }
)
targets9: BinaryAssociation = BinaryAssociation(
    name="targets9",
    ends={
        Property(name="graph_Node11", type=graph_GraphAsset, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_GraphAsset10", type=graph_Node, multiplicity=Multiplicity(1, 9999))
    }
)
target0: BinaryAssociation = BinaryAssociation(
    name="target0",
    ends={
        Property(name="graph_Node", type=graph_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_Edge", type=graph_Node, multiplicity=Multiplicity(0, 9999))
    }
)
source1: BinaryAssociation = BinaryAssociation(
    name="source1",
    ends={
        Property(name="graph_Node3", type=graph_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_Edge2", type=graph_Node, multiplicity=Multiplicity(0, 1))
    }
)
graphassets4: BinaryAssociation = BinaryAssociation(
    name="graphassets4",
    ends={
        Property(name="graph_GraphAsset", type=graph_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_Edge5", type=graph_GraphAsset, multiplicity=Multiplicity(0, 9999))
    }
)
outgoingassets25: BinaryAssociation = BinaryAssociation(
    name="outgoingassets25",
    ends={
        Property(name="graph_GraphAsset27", type=graph_NodeResponsibility, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_NodeResponsibility26", type=graph_GraphAsset, multiplicity=Multiplicity(0, 9999))
    }
)
incomingassets28: BinaryAssociation = BinaryAssociation(
    name="incomingassets28",
    ends={
        Property(name="graph_GraphAsset30", type=graph_NodeResponsibility, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_NodeResponsibility29", type=graph_GraphAsset, multiplicity=Multiplicity(0, 9999))
    }
)
subgraphs31: BinaryAssociation = BinaryAssociation(
    name="subgraphs31",
    ends={
        Property(name="graph_Subgraphs32", type=graph_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_Graph", type=graph_Subgraphs, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outedges12: BinaryAssociation = BinaryAssociation(
    name="outedges12",
    ends={
        Property(name="graph_Edge14", type=graph_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_Node13", type=graph_Edge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
responsibility15: BinaryAssociation = BinaryAssociation(
    name="responsibility15",
    ends={
        Property(name="graph_NodeResponsibility", type=graph_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_Node16", type=graph_NodeResponsibility, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inedges17: BinaryAssociation = BinaryAssociation(
    name="inedges17",
    ends={
        Property(name="graph_Edge19", type=graph_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_Node18", type=graph_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
nodes20: BinaryAssociation = BinaryAssociation(
    name="nodes20",
    ends={
        Property(name="graph_Node21", type=graph_Subgraphs, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_Subgraphs", type=graph_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
assets22: BinaryAssociation = BinaryAssociation(
    name="assets22",
    ends={
        Property(name="graph_GraphAsset24", type=graph_Subgraphs, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_Subgraphs23", type=graph_GraphAsset, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_graph_Node_Identifiable = Generalization(general=Identifiable, specific=graph_Node)
gen_graph_Edge_Identifiable = Generalization(general=Identifiable, specific=graph_Edge)
gen_graph_GraphAsset_Identifiable = Generalization(general=Identifiable, specific=graph_GraphAsset)
gen_graph_Subgraphs_Identifiable = Generalization(general=Identifiable, specific=graph_Subgraphs)
gen_graph_NodeResponsibility_Identifiable = Generalization(general=Identifiable, specific=graph_NodeResponsibility)

# Domain Model
domain_model = DomainModel(
    name="graph",
    types={graph_Edge, Identifiable, graph_Node, graph_GraphAsset, graph_Identifiable, graph_Graph, graph_NodeResponsibility, graph_Subgraphs},
    associations={source6, targets9, target0, source1, graphassets4, outgoingassets25, incomingassets28, subgraphs31, outedges12, responsibility15, inedges17, nodes20, assets22},
    generalizations={gen_graph_Node_Identifiable, gen_graph_Edge_Identifiable, gen_graph_GraphAsset_Identifiable, gen_graph_Subgraphs_Identifiable, gen_graph_NodeResponsibility_Identifiable},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)