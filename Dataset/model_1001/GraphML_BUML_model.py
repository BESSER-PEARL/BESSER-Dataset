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
ElemType: Enumeration = Enumeration(
    name="ElemType",
    literals={
            EnumerationLiteral(name="edge"),
			EnumerationLiteral(name="node"),
			EnumerationLiteral(name="graph")
    }
)

AttrType: Enumeration = Enumeration(
    name="AttrType",
    literals={
            EnumerationLiteral(name="double"),
			EnumerationLiteral(name="string"),
			EnumerationLiteral(name="integer"),
			EnumerationLiteral(name="boolean")
    }
)

EdgeType: Enumeration = Enumeration(
    name="EdgeType",
    literals={
            EnumerationLiteral(name="directed"),
			EnumerationLiteral(name="undirected")
    }
)

# Classes
Data = Class(name="Data")
GraphML_LocatedElement = Class(name="GraphML::LocatedElement", is_abstract=True)
GraphML_Root = Class(name="GraphML::Root")
LocatedElement = Class(name="LocatedElement")
Key = Class(name="Key")
Graph = Class(name="Graph")
GraphML_Element = Class(name="GraphML::Element")
GraphML_Key = Class(name="GraphML::Key")
Element = Class(name="Element")
GraphML_Graph = Class(name="GraphML::Graph")
GraphML_Edge = Class(name="GraphML::Edge")
Node = Class(name="Node")
Port = Class(name="Port")
GraphML_HyperEdge = Class(name="GraphML::HyperEdge")
EndPoint = Class(name="EndPoint")
GraphML_Node = Class(name="GraphML::Node")
Edge = Class(name="Edge")
GraphML_Port = Class(name="GraphML::Port")
GraphML_EndPoint = Class(name="GraphML::EndPoint")
GraphML_Data = Class(name="GraphML::Data")

# Data class attributes and methods

# GraphML_LocatedElement class attributes and methods
GraphML_LocatedElement_location: Property = Property(name="location", type=StringType)
GraphML_LocatedElement_commentsBefore: Property = Property(name="commentsBefore", type=StringType)
GraphML_LocatedElement_commentsAfter: Property = Property(name="commentsAfter", type=StringType)
GraphML_LocatedElement.attributes={GraphML_LocatedElement_commentsBefore, GraphML_LocatedElement_location, GraphML_LocatedElement_commentsAfter}

# GraphML_Root class attributes and methods

# LocatedElement class attributes and methods

# Key class attributes and methods

# Graph class attributes and methods

# GraphML_Element class attributes and methods
GraphML_Element_id: Property = Property(name="id", type=StringType)
GraphML_Element.attributes={GraphML_Element_id}

# GraphML_Key class attributes and methods
GraphML_Key_for: Property = Property(name="for", type=StringType)
GraphML_Key_attrName: Property = Property(name="attrName", type=StringType)
GraphML_Key_type: Property = Property(name="type", type=StringType)
GraphML_Key_defValue: Property = Property(name="defValue", type=StringType)
GraphML_Key.attributes={GraphML_Key_attrName, GraphML_Key_type, GraphML_Key_for, GraphML_Key_defValue}

# Element class attributes and methods

# GraphML_Graph class attributes and methods
GraphML_Graph_edgeDefault: Property = Property(name="edgeDefault", type=StringType)
GraphML_Graph.attributes={GraphML_Graph_edgeDefault}

# GraphML_Edge class attributes and methods
GraphML_Edge_directed: Property = Property(name="directed", type=StringType)
GraphML_Edge.attributes={GraphML_Edge_directed}

# Node class attributes and methods

# Port class attributes and methods

# GraphML_HyperEdge class attributes and methods

# EndPoint class attributes and methods

# GraphML_Node class attributes and methods

# Edge class attributes and methods

# GraphML_Port class attributes and methods
GraphML_Port_name: Property = Property(name="name", type=StringType)
GraphML_Port.attributes={GraphML_Port_name}

# GraphML_EndPoint class attributes and methods

# GraphML_Data class attributes and methods
GraphML_Data_key: Property = Property(name="key", type=StringType)
GraphML_Data_value: Property = Property(name="value", type=StringType)
GraphML_Data.attributes={GraphML_Data_key, GraphML_Data_value}

# Relationships
datas3: BinaryAssociation = BinaryAssociation(
    name="datas3",
    ends={
        Property(name="Data", type=GraphML_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="GraphML_Element", type=Data, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
keys0: BinaryAssociation = BinaryAssociation(
    name="keys0",
    ends={
        Property(name="Key", type=GraphML_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="GraphML_Root", type=Key, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
graphs1: BinaryAssociation = BinaryAssociation(
    name="graphs1",
    ends={
        Property(name="Graph", type=GraphML_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="GraphML_Root2", type=Graph, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ports21: BinaryAssociation = BinaryAssociation(
    name="ports21",
    ends={
        Property(name="Port23", type=GraphML_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="GraphML_Node22", type=Port, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
graph4: BinaryAssociation = BinaryAssociation(
    name="graph4",
    ends={
        Property(name="#", type=GraphML_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="0", type=Graph, multiplicity=Multiplicity(0, 1))
    }
)
contents5: BinaryAssociation = BinaryAssociation(
    name="contents5",
    ends={
        Property(name="#7", type=GraphML_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="06", type=Element, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source8: BinaryAssociation = BinaryAssociation(
    name="source8",
    ends={
        Property(name="#10", type=GraphML_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="09", type=Node, multiplicity=Multiplicity(1, 1))
    }
)
target11: BinaryAssociation = BinaryAssociation(
    name="target11",
    ends={
        Property(name="#13", type=GraphML_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="012", type=Node, multiplicity=Multiplicity(1, 1))
    }
)
sourceport14: BinaryAssociation = BinaryAssociation(
    name="sourceport14",
    ends={
        Property(name="Port", type=GraphML_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="GraphML_Edge", type=Port, multiplicity=Multiplicity(1, 1))
    }
)
targetport15: BinaryAssociation = BinaryAssociation(
    name="targetport15",
    ends={
        Property(name="Port17", type=GraphML_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="GraphML_Edge16", type=Port, multiplicity=Multiplicity(1, 1))
    }
)
endpoints18: BinaryAssociation = BinaryAssociation(
    name="endpoints18",
    ends={
        Property(name="EndPoint", type=GraphML_HyperEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="GraphML_HyperEdge", type=EndPoint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subgraph19: BinaryAssociation = BinaryAssociation(
    name="subgraph19",
    ends={
        Property(name="Graph20", type=GraphML_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="GraphML_Node", type=Graph, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
sourceOf24: BinaryAssociation = BinaryAssociation(
    name="sourceOf24",
    ends={
        Property(name="#26", type=GraphML_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="025", type=Edge, multiplicity=Multiplicity(0, 9999))
    }
)
targetOf27: BinaryAssociation = BinaryAssociation(
    name="targetOf27",
    ends={
        Property(name="#29", type=GraphML_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="028", type=Edge, multiplicity=Multiplicity(0, 9999))
    }
)
node30: BinaryAssociation = BinaryAssociation(
    name="node30",
    ends={
        Property(name="Node", type=GraphML_EndPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="GraphML_EndPoint", type=Node, multiplicity=Multiplicity(1, 1))
    }
)
port31: BinaryAssociation = BinaryAssociation(
    name="port31",
    ends={
        Property(name="Port33", type=GraphML_EndPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="GraphML_EndPoint32", type=Port, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_GraphML_Root_LocatedElement = Generalization(general=LocatedElement, specific=GraphML_Root)
gen_GraphML_Element_LocatedElement = Generalization(general=LocatedElement, specific=GraphML_Element)
gen_GraphML_Key_Element = Generalization(general=Element, specific=GraphML_Key)
gen_GraphML_Graph_Element = Generalization(general=Element, specific=GraphML_Graph)
gen_GraphML_Edge_Element = Generalization(general=Element, specific=GraphML_Edge)
gen_GraphML_HyperEdge_Element = Generalization(general=Element, specific=GraphML_HyperEdge)
gen_GraphML_Node_Element = Generalization(general=Element, specific=GraphML_Node)
gen_GraphML_Port_LocatedElement = Generalization(general=LocatedElement, specific=GraphML_Port)
gen_GraphML_EndPoint_LocatedElement = Generalization(general=LocatedElement, specific=GraphML_EndPoint)
gen_GraphML_Data_LocatedElement = Generalization(general=LocatedElement, specific=GraphML_Data)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={Data, GraphML_LocatedElement, GraphML_Root, LocatedElement, Key, Graph, GraphML_Element, GraphML_Key, Element, GraphML_Graph, GraphML_Edge, Node, Port, GraphML_HyperEdge, EndPoint, GraphML_Node, Edge, GraphML_Port, GraphML_EndPoint, GraphML_Data, ElemType, AttrType, EdgeType},
    associations={datas3, keys0, graphs1, ports21, graph4, contents5, source8, target11, sourceport14, targetport15, endpoints18, subgraph19, sourceOf24, targetOf27, node30, port31},
    generalizations={gen_GraphML_Root_LocatedElement, gen_GraphML_Element_LocatedElement, gen_GraphML_Key_Element, gen_GraphML_Graph_Element, gen_GraphML_Edge_Element, gen_GraphML_HyperEdge_Element, gen_GraphML_Node_Element, gen_GraphML_Port_LocatedElement, gen_GraphML_EndPoint_LocatedElement, gen_GraphML_Data_LocatedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)