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
graph1_Node = Class(name="graph1::Node")
graph1_Edge = Class(name="graph1::Edge")
graph1_Graph = Class(name="graph1::Graph")

# graph1_Node class attributes and methods
graph1_Node_name: Property = Property(name="name", type=StringType)
graph1_Node.attributes={graph1_Node_name}

# graph1_Edge class attributes and methods

# graph1_Graph class attributes and methods

# Relationships
src0: BinaryAssociation = BinaryAssociation(
    name="src0",
    ends={
        Property(name="graph1_Node", type=graph1_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="graph1_Edge", type=graph1_Node, multiplicity=Multiplicity(0, 1))
    }
)
trg1: BinaryAssociation = BinaryAssociation(
    name="trg1",
    ends={
        Property(name="graph1_Node3", type=graph1_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="graph1_Edge2", type=graph1_Node, multiplicity=Multiplicity(0, 1))
    }
)
nodes4: BinaryAssociation = BinaryAssociation(
    name="nodes4",
    ends={
        Property(name="graph1_Node5", type=graph1_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph1_Graph", type=graph1_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edges6: BinaryAssociation = BinaryAssociation(
    name="edges6",
    ends={
        Property(name="graph1_Edge8", type=graph1_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph1_Graph7", type=graph1_Edge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="graph1",
    types={graph1_Node, graph1_Edge, graph1_Graph},
    associations={src0, trg1, nodes4, edges6},
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