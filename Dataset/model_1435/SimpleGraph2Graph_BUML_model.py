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
simplegraph2graph_Graph2Graph = Class(name="simplegraph2graph::Graph2Graph")
simplegraph2graph_Graph = Class(name="simplegraph2graph::Graph")
simplegraph2graph_Element2Element = Class(name="simplegraph2graph::Element2Element", is_abstract=True)
simplegraph2graph_Edge2Edge = Class(name="simplegraph2graph::Edge2Edge")
simplegraph2graph_Edge = Class(name="simplegraph2graph::Edge")
simplegraph2graph_Node2Node = Class(name="simplegraph2graph::Node2Node")
Element2Element = Class(name="Element2Element")
simplegraph2graph_Node = Class(name="simplegraph2graph::Node")

# simplegraph2graph_Graph2Graph class attributes and methods
simplegraph2graph_Graph2Graph_name: Property = Property(name="name", type=StringType)
simplegraph2graph_Graph2Graph.attributes={simplegraph2graph_Graph2Graph_name}

# simplegraph2graph_Graph class attributes and methods

# simplegraph2graph_Element2Element class attributes and methods

# simplegraph2graph_Edge2Edge class attributes and methods

# simplegraph2graph_Edge class attributes and methods

# simplegraph2graph_Node2Node class attributes and methods
simplegraph2graph_Node2Node_label: Property = Property(name="label", type=StringType)
simplegraph2graph_Node2Node.attributes={simplegraph2graph_Node2Node_label}

# Element2Element class attributes and methods

# simplegraph2graph_Node class attributes and methods

# Relationships
graph10: BinaryAssociation = BinaryAssociation(
    name="graph10",
    ends={
        Property(name="simplegraph2graph_Graph", type=simplegraph2graph_Graph2Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="simplegraph2graph_Graph2Graph", type=simplegraph2graph_Graph, multiplicity=Multiplicity(0, 1))
    }
)
graph21: BinaryAssociation = BinaryAssociation(
    name="graph21",
    ends={
        Property(name="simplegraph2graph_Graph3", type=simplegraph2graph_Graph2Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="simplegraph2graph_Graph2Graph2", type=simplegraph2graph_Graph, multiplicity=Multiplicity(0, 1))
    }
)
element2Element4: BinaryAssociation = BinaryAssociation(
    name="element2Element4",
    ends={
        Property(name="Element2Element", type=simplegraph2graph_Graph2Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=simplegraph2graph_Element2Element, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owner5: BinaryAssociation = BinaryAssociation(
    name="owner5",
    ends={
        Property(name="Graph2Graph", type=simplegraph2graph_Element2Element, multiplicity=Multiplicity(1, 1)),
        Property(name="element2Element", type=simplegraph2graph_Graph2Graph, multiplicity=Multiplicity(0, 1))
    }
)
edge16: BinaryAssociation = BinaryAssociation(
    name="edge16",
    ends={
        Property(name="simplegraph2graph_Edge", type=simplegraph2graph_Edge2Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="simplegraph2graph_Edge2Edge", type=simplegraph2graph_Edge, multiplicity=Multiplicity(0, 1))
    }
)
edge27: BinaryAssociation = BinaryAssociation(
    name="edge27",
    ends={
        Property(name="simplegraph2graph_Edge9", type=simplegraph2graph_Edge2Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="simplegraph2graph_Edge2Edge8", type=simplegraph2graph_Edge, multiplicity=Multiplicity(0, 1))
    }
)
target10: BinaryAssociation = BinaryAssociation(
    name="target10",
    ends={
        Property(name="simplegraph2graph_Node2Node", type=simplegraph2graph_Edge2Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="simplegraph2graph_Edge2Edge11", type=simplegraph2graph_Node2Node, multiplicity=Multiplicity(0, 1))
    }
)
source12: BinaryAssociation = BinaryAssociation(
    name="source12",
    ends={
        Property(name="simplegraph2graph_Node2Node14", type=simplegraph2graph_Edge2Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="simplegraph2graph_Edge2Edge13", type=simplegraph2graph_Node2Node, multiplicity=Multiplicity(0, 1))
    }
)
node115: BinaryAssociation = BinaryAssociation(
    name="node115",
    ends={
        Property(name="simplegraph2graph_Node", type=simplegraph2graph_Node2Node, multiplicity=Multiplicity(1, 1)),
        Property(name="simplegraph2graph_Node2Node16", type=simplegraph2graph_Node, multiplicity=Multiplicity(0, 1))
    }
)
node217: BinaryAssociation = BinaryAssociation(
    name="node217",
    ends={
        Property(name="simplegraph2graph_Node19", type=simplegraph2graph_Node2Node, multiplicity=Multiplicity(1, 1)),
        Property(name="simplegraph2graph_Node2Node18", type=simplegraph2graph_Node, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_simplegraph2graph_Node2Node_Element2Element = Generalization(general=Element2Element, specific=simplegraph2graph_Node2Node)

# Domain Model
domain_model = DomainModel(
    name="simplegraph2graph",
    types={simplegraph2graph_Graph2Graph, simplegraph2graph_Graph, simplegraph2graph_Element2Element, simplegraph2graph_Edge2Edge, simplegraph2graph_Edge, simplegraph2graph_Node2Node, Element2Element, simplegraph2graph_Node},
    associations={graph10, graph21, element2Element4, owner5, edge16, edge27, target10, source12, node115, node217},
    generalizations={gen_simplegraph2graph_Node2Node_Element2Element},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)