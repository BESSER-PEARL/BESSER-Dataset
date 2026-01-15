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
graph_GraphModel = Class(name="graph::GraphModel")
graph_Node = Class(name="graph::Node")
graph_Edge = Class(name="graph::Edge")

# graph_GraphModel class attributes and methods

# graph_Node class attributes and methods
graph_Node_value: Property = Property(name="value", type=StringType)
graph_Node.attributes={graph_Node_value}

# graph_Edge class attributes and methods
graph_Edge_label: Property = Property(name="label", type=StringType)
graph_Edge.attributes={graph_Edge_label}

# Relationships
node0: BinaryAssociation = BinaryAssociation(
    name="node0",
    ends={
        Property(name="graph_Node", type=graph_GraphModel, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_GraphModel", type=graph_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edge1: BinaryAssociation = BinaryAssociation(
    name="edge1",
    ends={
        Property(name="graph_Edge", type=graph_GraphModel, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_GraphModel2", type=graph_Edge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
src3: BinaryAssociation = BinaryAssociation(
    name="src3",
    ends={
        Property(name="graph_Node5", type=graph_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_Edge4", type=graph_Node, multiplicity=Multiplicity(1, 1))
    }
)
tgt6: BinaryAssociation = BinaryAssociation(
    name="tgt6",
    ends={
        Property(name="graph_Node8", type=graph_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_Edge7", type=graph_Node, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="graph",
    types={graph_GraphModel, graph_Node, graph_Edge},
    associations={node0, edge1, src3, tgt6},
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