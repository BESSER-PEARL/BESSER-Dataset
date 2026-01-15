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
graphs_Graph = Class(name="graphs::Graph")
graphs_Node = Class(name="graphs::Node")
graphs_Edge = Class(name="graphs::Edge")

# graphs_Graph class attributes and methods
graphs_Graph_m_nodes: Method = Method(name="nodes", parameters={}, type=StringType)
graphs_Graph_m_edges: Method = Method(name="edges", parameters={}, type=StringType)
graphs_Graph.methods={graphs_Graph_m_edges, graphs_Graph_m_nodes}

# graphs_Node class attributes and methods
graphs_Node_m_outputs: Method = Method(name="outputs", parameters={}, type=StringType)
graphs_Node_m_inputs: Method = Method(name="inputs", parameters={}, type=StringType)
graphs_Node.methods={graphs_Node_m_outputs, graphs_Node_m_inputs}

# graphs_Edge class attributes and methods

# Domain Model
domain_model = DomainModel(
    name="graphs",
    types={graphs_Graph, graphs_Node, graphs_Edge},
    associations={},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)