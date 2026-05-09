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
EdgeType: Enumeration = Enumeration(
    name="EdgeType",
    literals={
            EnumerationLiteral(name="directed"),
			EnumerationLiteral(name="undirected")
    }
)

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

# Classes
GraphML_LocatedElement = Class(name="GraphML_LocatedElement", is_abstract=True)
GraphML_Root = Class(name="GraphML_Root")
LocatedElement = Class(name="LocatedElement")
Key = Class(name="Key")
Graph = Class(name="Graph")
GraphML_Element = Class(name="GraphML_Element")
GraphML_Edge = Class(name="GraphML_Edge")
Node = Class(name="Node")
Port = Class(name="Port")
GraphML_HyperEdge = Class(name="GraphML_HyperEdge")
EndPoint = Class(name="EndPoint")
GraphML_Node = Class(name="GraphML_Node")
Edge = Class(name="Edge")
GraphML_Port = Class(name="GraphML_Port")
Data = Class(name="Data")
GraphML_Key = Class(name="GraphML_Key")
Element = Class(name="Element")
GraphML_Graph = Class(name="GraphML_Graph")
GraphML_EndPoint = Class(name="GraphML_EndPoint")
GraphML_Data = Class(name="GraphML_Data")

# GraphML_LocatedElement class attributes and methods
GraphML_LocatedElement_location: Property = Property(name="location", type=StringType)
GraphML_LocatedElement_commentsBefore: Property = Property(name="commentsBefore", type=StringType)
GraphML_LocatedElement_commentsAfter: Property = Property(name="commentsAfter", type=StringType)
GraphML_LocatedElement.attributes={GraphML_LocatedElement_commentsBefore, GraphML_LocatedElement_commentsAfter, GraphML_LocatedElement_location}

# GraphML_Root class attributes and methods

# LocatedElement class attributes and methods

# Key class attributes and methods

# Graph class attributes and methods

# GraphML_Element class attributes and methods
GraphML_Element_id: Property = Property(name="id", type=StringType)
GraphML_Element.attributes={GraphML_Element_id}

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

# Data class attributes and methods

# GraphML_Key class attributes and methods
GraphML_Key_for_: Property = Property(name="for_", type=StringType)
GraphML_Key_attrName: Property = Property(name="attrName", type=StringType)
GraphML_Key_type: Property = Property(name="type", type=StringType)
GraphML_Key_defValue: Property = Property(name="defValue", type=StringType)
GraphML_Key.attributes={GraphML_Key_attrName, GraphML_Key_for_, GraphML_Key_type, GraphML_Key_defValue}

# Element class attributes and methods

# GraphML_Graph class attributes and methods
GraphML_Graph_edgeDefault: Property = Property(name="edgeDefault", type=StringType)
GraphML_Graph.attributes={GraphML_Graph_edgeDefault}

# GraphML_EndPoint class attributes and methods

# GraphML_Data class attributes and methods
GraphML_Data_key: Property = Property(name="key", type=StringType)
GraphML_Data_value: Property = Property(name="value", type=StringType)
GraphML_Data.attributes={GraphML_Data_key, GraphML_Data_value}

# Relationships
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
source7: BinaryAssociation = BinaryAssociation(
    name="source7",
    ends={
        Property(name="Node", type=GraphML_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="sourceOf", type=Node, multiplicity=Multiplicity(1, 1))
    }
)
target8: BinaryAssociation = BinaryAssociation(
    name="target8",
    ends={
        Property(name="Node9", type=GraphML_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="targetOf", type=Node, multiplicity=Multiplicity(1, 1))
    }
)
sourceport10: BinaryAssociation = BinaryAssociation(
    name="sourceport10",
    ends={
        Property(name="Port", type=GraphML_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="GraphML_Edge", type=Port, multiplicity=Multiplicity(1, 1))
    }
)
targetport11: BinaryAssociation = BinaryAssociation(
    name="targetport11",
    ends={
        Property(name="Port13", type=GraphML_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="GraphML_Edge12", type=Port, multiplicity=Multiplicity(1, 1))
    }
)
endpoints14: BinaryAssociation = BinaryAssociation(
    name="endpoints14",
    ends={
        Property(name="EndPoint", type=GraphML_HyperEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="GraphML_HyperEdge", type=EndPoint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subgraph15: BinaryAssociation = BinaryAssociation(
    name="subgraph15",
    ends={
        Property(name="Graph16", type=GraphML_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="GraphML_Node", type=Graph, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ports17: BinaryAssociation = BinaryAssociation(
    name="ports17",
    ends={
        Property(name="Port19", type=GraphML_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="GraphML_Node18", type=Port, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sourceOf20: BinaryAssociation = BinaryAssociation(
    name="sourceOf20",
    ends={
        Property(name="Edge", type=GraphML_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=Edge, multiplicity=Multiplicity(0, 9999))
    }
)
targetOf21: BinaryAssociation = BinaryAssociation(
    name="targetOf21",
    ends={
        Property(name="Edge22", type=GraphML_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=Edge, multiplicity=Multiplicity(0, 9999))
    }
)
datas3: BinaryAssociation = BinaryAssociation(
    name="datas3",
    ends={
        Property(name="Data", type=GraphML_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="GraphML_Element", type=Data, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
graph4: BinaryAssociation = BinaryAssociation(
    name="graph4",
    ends={
        Property(name="Graph5", type=GraphML_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="contents", type=Graph, multiplicity=Multiplicity(0, 1))
    }
)
contents6: BinaryAssociation = BinaryAssociation(
    name="contents6",
    ends={
        Property(name="Element", type=GraphML_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph", type=Element, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
node23: BinaryAssociation = BinaryAssociation(
    name="node23",
    ends={
        Property(name="Node24", type=GraphML_EndPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="GraphML_EndPoint", type=Node, multiplicity=Multiplicity(1, 1))
    }
)
port25: BinaryAssociation = BinaryAssociation(
    name="port25",
    ends={
        Property(name="Port27", type=GraphML_EndPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="GraphML_EndPoint26", type=Port, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_GraphML_Root_LocatedElement = Generalization(general=LocatedElement, specific=GraphML_Root)
gen_GraphML_Element_LocatedElement = Generalization(general=LocatedElement, specific=GraphML_Element)
gen_GraphML_Edge_Element = Generalization(general=Element, specific=GraphML_Edge)
gen_GraphML_HyperEdge_Element = Generalization(general=Element, specific=GraphML_HyperEdge)
gen_GraphML_Node_Element = Generalization(general=Element, specific=GraphML_Node)
gen_GraphML_Port_LocatedElement = Generalization(general=LocatedElement, specific=GraphML_Port)
gen_GraphML_Key_Element = Generalization(general=Element, specific=GraphML_Key)
gen_GraphML_Graph_Element = Generalization(general=Element, specific=GraphML_Graph)
gen_GraphML_EndPoint_LocatedElement = Generalization(general=LocatedElement, specific=GraphML_EndPoint)
gen_GraphML_Data_LocatedElement = Generalization(general=LocatedElement, specific=GraphML_Data)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={GraphML_LocatedElement, GraphML_Root, LocatedElement, Key, Graph, GraphML_Element, GraphML_Edge, Node, Port, GraphML_HyperEdge, EndPoint, GraphML_Node, Edge, GraphML_Port, Data, GraphML_Key, Element, GraphML_Graph, GraphML_EndPoint, GraphML_Data, EdgeType, ElemType, AttrType},
    associations={keys0, graphs1, source7, target8, sourceport10, targetport11, endpoints14, subgraph15, ports17, sourceOf20, targetOf21, datas3, graph4, contents6, node23, port25},
    generalizations={gen_GraphML_Root_LocatedElement, gen_GraphML_Element_LocatedElement, gen_GraphML_Edge_Element, gen_GraphML_HyperEdge_Element, gen_GraphML_Node_Element, gen_GraphML_Port_LocatedElement, gen_GraphML_Key_Element, gen_GraphML_Graph_Element, gen_GraphML_EndPoint_LocatedElement, gen_GraphML_Data_LocatedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)