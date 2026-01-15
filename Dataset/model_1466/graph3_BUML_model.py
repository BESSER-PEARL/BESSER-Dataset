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
graph3_Graph = Class(name="graph3::Graph")
graph3_Node = Class(name="graph3::Node")

# graph3_Graph class attributes and methods

# graph3_Node class attributes and methods
graph3_Node_text: Property = Property(name="text", type=StringType)
graph3_Node.attributes={graph3_Node_text}

# Relationships
nodes0: BinaryAssociation = BinaryAssociation(
    name="nodes0",
    ends={
        Property(name="graph3_Node", type=graph3_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph3_Graph", type=graph3_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
linksTo2: BinaryAssociation = BinaryAssociation(
    name="linksTo2",
    ends={
        Property(name="graph3_Node3", type=graph3_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="graph3_Node1", type=graph3_Node, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="graph3",
    types={graph3_Graph, graph3_Node},
    associations={nodes0, linksTo2},
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