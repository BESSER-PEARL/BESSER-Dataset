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
vml_Diagram = Class(name="vml::Diagram")
vml_Pie = Class(name="vml::Pie")
vml_Graph = Class(name="vml::Graph")
vml_Slice = Class(name="vml::Slice")
vml_Node = Class(name="vml::Node")
vml_Edge = Class(name="vml::Edge")
vml_Model = Class(name="vml::Model")

# vml_Diagram class attributes and methods
vml_Diagram_title: Property = Property(name="title", type=StringType)
vml_Diagram.attributes={vml_Diagram_title}

# vml_Pie class attributes and methods
vml_Pie_ID: Property = Property(name="ID", type=StringType)
vml_Pie_title: Property = Property(name="title", type=StringType)
vml_Pie.attributes={vml_Pie_ID, vml_Pie_title}

# vml_Graph class attributes and methods
vml_Graph_ID: Property = Property(name="ID", type=StringType)
vml_Graph_title: Property = Property(name="title", type=StringType)
vml_Graph.attributes={vml_Graph_ID, vml_Graph_title}

# vml_Slice class attributes and methods
vml_Slice_title: Property = Property(name="title", type=StringType)
vml_Slice_value: Property = Property(name="value", type=IntegerType)
vml_Slice.attributes={vml_Slice_title, vml_Slice_value}

# vml_Node class attributes and methods
vml_Node_title: Property = Property(name="title", type=StringType)
vml_Node.attributes={vml_Node_title}

# vml_Edge class attributes and methods
vml_Edge_relation: Property = Property(name="relation", type=StringType)
vml_Edge.attributes={vml_Edge_relation}

# vml_Model class attributes and methods

# Relationships
diagrams0: BinaryAssociation = BinaryAssociation(
    name="diagrams0",
    ends={
        Property(name="vml_Diagram", type=vml_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="vml_Model", type=vml_Diagram, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pies1: BinaryAssociation = BinaryAssociation(
    name="pies1",
    ends={
        Property(name="vml_Pie", type=vml_Diagram, multiplicity=Multiplicity(1, 1)),
        Property(name="vml_Diagram2", type=vml_Pie, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
graph3: BinaryAssociation = BinaryAssociation(
    name="graph3",
    ends={
        Property(name="vml_Graph", type=vml_Diagram, multiplicity=Multiplicity(1, 1)),
        Property(name="vml_Diagram4", type=vml_Graph, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
slices5: BinaryAssociation = BinaryAssociation(
    name="slices5",
    ends={
        Property(name="vml_Slice", type=vml_Pie, multiplicity=Multiplicity(1, 1)),
        Property(name="vml_Pie6", type=vml_Slice, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nodes7: BinaryAssociation = BinaryAssociation(
    name="nodes7",
    ends={
        Property(name="vml_Node", type=vml_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="vml_Graph8", type=vml_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edges9: BinaryAssociation = BinaryAssociation(
    name="edges9",
    ends={
        Property(name="vml_Edge", type=vml_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="vml_Graph10", type=vml_Edge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outgoing11: BinaryAssociation = BinaryAssociation(
    name="outgoing11",
    ends={
        Property(name="Edge", type=vml_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=vml_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
incoming12: BinaryAssociation = BinaryAssociation(
    name="incoming12",
    ends={
        Property(name="Edge13", type=vml_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=vml_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
source14: BinaryAssociation = BinaryAssociation(
    name="source14",
    ends={
        Property(name="Node", type=vml_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=vml_Node, multiplicity=Multiplicity(0, 1))
    }
)
target15: BinaryAssociation = BinaryAssociation(
    name="target15",
    ends={
        Property(name="Node16", type=vml_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=vml_Node, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="vml",
    types={vml_Diagram, vml_Pie, vml_Graph, vml_Slice, vml_Node, vml_Edge, vml_Model},
    associations={diagrams0, pies1, graph3, slices5, nodes7, edges9, outgoing11, incoming12, source14, target15},
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