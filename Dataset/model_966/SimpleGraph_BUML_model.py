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
simplegraph_Element = Class(name="simplegraph::Element", is_abstract=True)
simplegraph_Graph = Class(name="simplegraph::Graph")
simplegraph_Node = Class(name="simplegraph::Node")
Element = Class(name="Element")
simplegraph_Edge = Class(name="simplegraph::Edge")

# simplegraph_Element class attributes and methods

# simplegraph_Graph class attributes and methods
simplegraph_Graph_name: Property = Property(name="name", type=StringType)
simplegraph_Graph.attributes={simplegraph_Graph_name}

# simplegraph_Node class attributes and methods
simplegraph_Node_label: Property = Property(name="label", type=StringType)
simplegraph_Node.attributes={simplegraph_Node_label}

# Element class attributes and methods

# simplegraph_Edge class attributes and methods

# Relationships
source4: BinaryAssociation = BinaryAssociation(
    name="source4",
    ends={
        Property(name="Node5", type=simplegraph_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=simplegraph_Node, multiplicity=Multiplicity(0, 1))
    }
)
graph6: BinaryAssociation = BinaryAssociation(
    name="graph6",
    ends={
        Property(name="Graph", type=simplegraph_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="element", type=simplegraph_Graph, multiplicity=Multiplicity(1, 1))
    }
)
element7: BinaryAssociation = BinaryAssociation(
    name="element7",
    ends={
        Property(name="Element", type=simplegraph_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph", type=simplegraph_Element, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
incoming0: BinaryAssociation = BinaryAssociation(
    name="incoming0",
    ends={
        Property(name="Edge", type=simplegraph_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=simplegraph_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing1: BinaryAssociation = BinaryAssociation(
    name="outgoing1",
    ends={
        Property(name="Edge2", type=simplegraph_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=simplegraph_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
target3: BinaryAssociation = BinaryAssociation(
    name="target3",
    ends={
        Property(name="Node", type=simplegraph_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=simplegraph_Node, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_simplegraph_Node_Element = Generalization(general=Element, specific=simplegraph_Node)
gen_simplegraph_Edge_Element = Generalization(general=Element, specific=simplegraph_Edge)

# Domain Model
domain_model = DomainModel(
    name="simplegraph",
    types={simplegraph_Element, simplegraph_Graph, simplegraph_Node, Element, simplegraph_Edge},
    associations={source4, graph6, element7, incoming0, outgoing1, target3},
    generalizations={gen_simplegraph_Node_Element, gen_simplegraph_Edge_Element},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)