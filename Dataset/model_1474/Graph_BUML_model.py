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
Graph_Graph = Class(name="Graph::Graph")
NamedElement = Class(name="NamedElement")
Graph_GraphElement = Class(name="Graph::GraphElement")
Graph_NamedElement = Class(name="Graph::NamedElement")
Graph_Node = Class(name="Graph::Node")
GraphElement = Class(name="GraphElement")
Graph_DirectedArc = Class(name="Graph::DirectedArc")

# Graph_Graph class attributes and methods

# NamedElement class attributes and methods

# Graph_GraphElement class attributes and methods
Graph_GraphElement_label: Property = Property(name="label", type=StringType)
Graph_GraphElement_color: Property = Property(name="color", type=StringType)
Graph_GraphElement.attributes={Graph_GraphElement_label, Graph_GraphElement_color}

# Graph_NamedElement class attributes and methods
Graph_NamedElement_name: Property = Property(name="name", type=StringType)
Graph_NamedElement.attributes={Graph_NamedElement_name}

# Graph_Node class attributes and methods
Graph_Node_shape: Property = Property(name="shape", type=StringType)
Graph_Node_style: Property = Property(name="style", type=StringType)
Graph_Node.attributes={Graph_Node_shape, Graph_Node_style}

# GraphElement class attributes and methods

# Graph_DirectedArc class attributes and methods
Graph_DirectedArc_weight: Property = Property(name="weight", type=IntegerType)
Graph_DirectedArc.attributes={Graph_DirectedArc_weight}

# Relationships
contents0: BinaryAssociation = BinaryAssociation(
    name="contents0",
    ends={
        Property(name="GraphElement", type=Graph_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph", type=Graph_GraphElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
graph1: BinaryAssociation = BinaryAssociation(
    name="graph1",
    ends={
        Property(name="Graph", type=Graph_GraphElement, multiplicity=Multiplicity(1, 1)),
        Property(name="contents", type=Graph_Graph, multiplicity=Multiplicity(0, 1))
    }
)
sourceNode2: BinaryAssociation = BinaryAssociation(
    name="sourceNode2",
    ends={
        Property(name="Graph_Node", type=Graph_DirectedArc, multiplicity=Multiplicity(1, 1)),
        Property(name="Graph_DirectedArc", type=Graph_Node, multiplicity=Multiplicity(0, 1))
    }
)
targetNode3: BinaryAssociation = BinaryAssociation(
    name="targetNode3",
    ends={
        Property(name="Graph_Node5", type=Graph_DirectedArc, multiplicity=Multiplicity(1, 1)),
        Property(name="Graph_DirectedArc4", type=Graph_Node, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_Graph_Graph_NamedElement = Generalization(general=NamedElement, specific=Graph_Graph)
gen_Graph_GraphElement_NamedElement = Generalization(general=NamedElement, specific=Graph_GraphElement)
gen_Graph_Node_GraphElement = Generalization(general=GraphElement, specific=Graph_Node)
gen_Graph_DirectedArc_GraphElement = Generalization(general=GraphElement, specific=Graph_DirectedArc)

# Domain Model
domain_model = DomainModel(
    name="Graph",
    types={Graph_Graph, NamedElement, Graph_GraphElement, Graph_NamedElement, Graph_Node, GraphElement, Graph_DirectedArc},
    associations={contents0, graph1, sourceNode2, targetNode3},
    generalizations={gen_Graph_Graph_NamedElement, gen_Graph_GraphElement_NamedElement, gen_Graph_Node_GraphElement, gen_Graph_DirectedArc_GraphElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)