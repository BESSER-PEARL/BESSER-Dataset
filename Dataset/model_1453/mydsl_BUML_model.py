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
mydsl_Graph = Class(name="mydsl::Graph")
mydsl_Edge = Class(name="mydsl::Edge")
mydsl_Node = Class(name="mydsl::Node")

# mydsl_Graph class attributes and methods
mydsl_Graph_name: Property = Property(name="name", type=StringType)
mydsl_Graph.attributes={mydsl_Graph_name}

# mydsl_Edge class attributes and methods
mydsl_Edge_label: Property = Property(name="label", type=StringType)
mydsl_Edge_parsed_target: Property = Property(name="parsed_target", type=StringType)
mydsl_Edge_parsed_source: Property = Property(name="parsed_source", type=StringType)
mydsl_Edge.attributes={mydsl_Edge_parsed_source, mydsl_Edge_label, mydsl_Edge_parsed_target}

# mydsl_Node class attributes and methods
mydsl_Node_content: Property = Property(name="content", type=StringType)
mydsl_Node_name: Property = Property(name="name", type=StringType)
mydsl_Node_isInvisible: Property = Property(name="isInvisible", type=BooleanType)
mydsl_Node.attributes={mydsl_Node_content, mydsl_Node_name, mydsl_Node_isInvisible}

# Relationships
edges0: BinaryAssociation = BinaryAssociation(
    name="edges0",
    ends={
        Property(name="mydsl_Edge", type=mydsl_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="mydsl_Graph", type=mydsl_Edge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nodes1: BinaryAssociation = BinaryAssociation(
    name="nodes1",
    ends={
        Property(name="mydsl_Node", type=mydsl_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="mydsl_Graph2", type=mydsl_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subgraphs4: BinaryAssociation = BinaryAssociation(
    name="subgraphs4",
    ends={
        Property(name="mydsl_Graph5", type=mydsl_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="mydsl_Graph3", type=mydsl_Graph, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target6: BinaryAssociation = BinaryAssociation(
    name="target6",
    ends={
        Property(name="mydsl_Node8", type=mydsl_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="mydsl_Edge7", type=mydsl_Node, multiplicity=Multiplicity(0, 1))
    }
)
source9: BinaryAssociation = BinaryAssociation(
    name="source9",
    ends={
        Property(name="mydsl_Node11", type=mydsl_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="mydsl_Edge10", type=mydsl_Node, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="mydsl",
    types={mydsl_Graph, mydsl_Edge, mydsl_Node},
    associations={edges0, nodes1, subgraphs4, target6, source9},
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