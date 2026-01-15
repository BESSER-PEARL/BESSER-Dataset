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
simpleGraph_Graph = Class(name="simpleGraph::Graph")
GraphElement = Class(name="GraphElement")
simpleGraph_Node = Class(name="simpleGraph::Node")
simpleGraph_Position = Class(name="simpleGraph::Position")
simpleGraph_Label = Class(name="simpleGraph::Label")
simpleGraph_Nail = Class(name="simpleGraph::Nail")
Position = Class(name="Position")
simpleGraph_Edge = Class(name="simpleGraph::Edge")
simpleGraph_GraphElement = Class(name="simpleGraph::GraphElement", is_abstract=True)
simpleGraph_Parameter = Class(name="simpleGraph::Parameter")

# simpleGraph_Graph class attributes and methods

# GraphElement class attributes and methods

# simpleGraph_Node class attributes and methods

# simpleGraph_Position class attributes and methods
simpleGraph_Position_X: Property = Property(name="X", type=IntegerType)
simpleGraph_Position_Y: Property = Property(name="Y", type=IntegerType)
simpleGraph_Position.attributes={simpleGraph_Position_X, simpleGraph_Position_Y}

# simpleGraph_Label class attributes and methods
simpleGraph_Label_value: Property = Property(name="value", type=StringType)
simpleGraph_Label.attributes={simpleGraph_Label_value}

# simpleGraph_Nail class attributes and methods

# Position class attributes and methods

# simpleGraph_Edge class attributes and methods

# simpleGraph_GraphElement class attributes and methods
simpleGraph_GraphElement_id: Property = Property(name="id", type=IntegerType)
simpleGraph_GraphElement_generated: Property = Property(name="generated", type=BooleanType)
simpleGraph_GraphElement.attributes={simpleGraph_GraphElement_generated, simpleGraph_GraphElement_id}

# simpleGraph_Parameter class attributes and methods
simpleGraph_Parameter_key: Property = Property(name="key", type=StringType)
simpleGraph_Parameter_value: Property = Property(name="value", type=StringType)
simpleGraph_Parameter.attributes={simpleGraph_Parameter_value, simpleGraph_Parameter_key}

# Relationships
nodes0: BinaryAssociation = BinaryAssociation(
    name="nodes0",
    ends={
        Property(name="simpleGraph_Node", type=simpleGraph_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleGraph_Graph", type=simpleGraph_Node, multiplicity=Multiplicity(0, 9999))
    }
)
source4: BinaryAssociation = BinaryAssociation(
    name="source4",
    ends={
        Property(name="simpleGraph_Node6", type=simpleGraph_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleGraph_Edge5", type=simpleGraph_Node, multiplicity=Multiplicity(0, 1))
    }
)
target7: BinaryAssociation = BinaryAssociation(
    name="target7",
    ends={
        Property(name="simpleGraph_Node9", type=simpleGraph_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleGraph_Edge8", type=simpleGraph_Node, multiplicity=Multiplicity(0, 1))
    }
)
labels10: BinaryAssociation = BinaryAssociation(
    name="labels10",
    ends={
        Property(name="simpleGraph_Label", type=simpleGraph_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleGraph_Edge11", type=simpleGraph_Label, multiplicity=Multiplicity(0, 9999))
    }
)
nails12: BinaryAssociation = BinaryAssociation(
    name="nails12",
    ends={
        Property(name="simpleGraph_Nail", type=simpleGraph_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleGraph_Edge13", type=simpleGraph_Nail, multiplicity=Multiplicity(0, 9999))
    }
)
edges1: BinaryAssociation = BinaryAssociation(
    name="edges1",
    ends={
        Property(name="simpleGraph_Edge", type=simpleGraph_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleGraph_Graph2", type=simpleGraph_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
parameters3: BinaryAssociation = BinaryAssociation(
    name="parameters3",
    ends={
        Property(name="simpleGraph_Parameter", type=simpleGraph_GraphElement, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleGraph_GraphElement", type=simpleGraph_Parameter, multiplicity=Multiplicity(0, 9999))
    }
)
label14: BinaryAssociation = BinaryAssociation(
    name="label14",
    ends={
        Property(name="simpleGraph_Label16", type=simpleGraph_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleGraph_Node15", type=simpleGraph_Label, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_simpleGraph_Graph_GraphElement = Generalization(general=GraphElement, specific=simpleGraph_Graph)
gen_simpleGraph_Position_GraphElement = Generalization(general=GraphElement, specific=simpleGraph_Position)
gen_simpleGraph_Edge_GraphElement = Generalization(general=GraphElement, specific=simpleGraph_Edge)
gen_simpleGraph_Node_Position = Generalization(general=Position, specific=simpleGraph_Node)
gen_simpleGraph_Label_Position = Generalization(general=Position, specific=simpleGraph_Label)
gen_simpleGraph_Nail_Position = Generalization(general=Position, specific=simpleGraph_Nail)

# Domain Model
domain_model = DomainModel(
    name="simpleGraph",
    types={simpleGraph_Graph, GraphElement, simpleGraph_Node, simpleGraph_Position, simpleGraph_Label, simpleGraph_Nail, Position, simpleGraph_Edge, simpleGraph_GraphElement, simpleGraph_Parameter},
    associations={nodes0, source4, target7, labels10, nails12, edges1, parameters3, label14},
    generalizations={gen_simpleGraph_Graph_GraphElement, gen_simpleGraph_Position_GraphElement, gen_simpleGraph_Edge_GraphElement, gen_simpleGraph_Node_Position, gen_simpleGraph_Label_Position, gen_simpleGraph_Nail_Position},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)