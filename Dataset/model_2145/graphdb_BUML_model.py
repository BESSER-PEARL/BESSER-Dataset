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

# Enumerations
PrimitiveType: Enumeration = Enumeration(
    name="PrimitiveType",
    literals={
            EnumerationLiteral(name="Object"),
			EnumerationLiteral(name="String"),
			EnumerationLiteral(name="Integer"),
			EnumerationLiteral(name="Boolean")
    }
)

# Classes
graphdb_Graph = Class(name="graphdb::Graph")
graphdb_Vertex = Class(name="graphdb::Vertex")
graphdb_Edge = Class(name="graphdb::Edge")
graphdb_Element = Class(name="graphdb::Element", is_abstract=True)
graphdb_GraphElement = Class(name="graphdb::GraphElement", is_abstract=True)
Element = Class(name="Element")
graphdb_Property = Class(name="graphdb::Property")
GraphElement = Class(name="GraphElement")

# graphdb_Graph class attributes and methods

# graphdb_Vertex class attributes and methods
graphdb_Vertex_labels: Property = Property(name="labels", type=StringType)
graphdb_Vertex_name: Property = Property(name="name", type=StringType)
graphdb_Vertex.attributes={graphdb_Vertex_labels, graphdb_Vertex_name}

# graphdb_Edge class attributes and methods
graphdb_Edge_type: Property = Property(name="type", type=StringType)
graphdb_Edge_name: Property = Property(name="name", type=StringType)
graphdb_Edge.attributes={graphdb_Edge_name, graphdb_Edge_type}

# graphdb_Element class attributes and methods

# graphdb_GraphElement class attributes and methods

# Element class attributes and methods

# graphdb_Property class attributes and methods
graphdb_Property_key: Property = Property(name="key", type=StringType)
graphdb_Property_type: Property = Property(name="type", type=StringType)
graphdb_Property.attributes={graphdb_Property_type, graphdb_Property_key}

# GraphElement class attributes and methods

# Relationships
inEdges4: BinaryAssociation = BinaryAssociation(
    name="inEdges4",
    ends={
        Property(name="Edge5", type=graphdb_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="head", type=graphdb_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
vertices0: BinaryAssociation = BinaryAssociation(
    name="vertices0",
    ends={
        Property(name="Vertex", type=graphdb_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph", type=graphdb_Vertex, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edges1: BinaryAssociation = BinaryAssociation(
    name="edges1",
    ends={
        Property(name="Edge", type=graphdb_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph2", type=graphdb_Edge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
properties3: BinaryAssociation = BinaryAssociation(
    name="properties3",
    ends={
        Property(name="Property", type=graphdb_GraphElement, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=graphdb_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outEdges6: BinaryAssociation = BinaryAssociation(
    name="outEdges6",
    ends={
        Property(name="Edge7", type=graphdb_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="tail", type=graphdb_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
graph8: BinaryAssociation = BinaryAssociation(
    name="graph8",
    ends={
        Property(name="Graph", type=graphdb_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="vertices", type=graphdb_Graph, multiplicity=Multiplicity(0, 1))
    }
)
tail9: BinaryAssociation = BinaryAssociation(
    name="tail9",
    ends={
        Property(name="Vertex10", type=graphdb_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="outEdges", type=graphdb_Vertex, multiplicity=Multiplicity(0, 1))
    }
)
head11: BinaryAssociation = BinaryAssociation(
    name="head11",
    ends={
        Property(name="Vertex12", type=graphdb_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="inEdges", type=graphdb_Vertex, multiplicity=Multiplicity(0, 1))
    }
)
graph13: BinaryAssociation = BinaryAssociation(
    name="graph13",
    ends={
        Property(name="Graph14", type=graphdb_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="edges", type=graphdb_Graph, multiplicity=Multiplicity(0, 1))
    }
)
owner15: BinaryAssociation = BinaryAssociation(
    name="owner15",
    ends={
        Property(name="GraphElement", type=graphdb_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="properties", type=graphdb_GraphElement, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_graphdb_GraphElement_Element = Generalization(general=Element, specific=graphdb_GraphElement)
gen_graphdb_Vertex_GraphElement = Generalization(general=GraphElement, specific=graphdb_Vertex)
gen_graphdb_Edge_GraphElement = Generalization(general=GraphElement, specific=graphdb_Edge)
gen_graphdb_Property_Element = Generalization(general=Element, specific=graphdb_Property)

# Domain Model
domain_model = DomainModel(
    name="graphdb",
    types={graphdb_Graph, graphdb_Vertex, graphdb_Edge, graphdb_Element, graphdb_GraphElement, Element, graphdb_Property, GraphElement, PrimitiveType},
    associations={inEdges4, vertices0, edges1, properties3, outEdges6, graph8, tail9, head11, graph13, owner15},
    generalizations={gen_graphdb_GraphElement_Element, gen_graphdb_Vertex_GraphElement, gen_graphdb_Edge_GraphElement, gen_graphdb_Property_Element},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)