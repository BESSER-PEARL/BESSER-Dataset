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
graph2_Graph = Class(name="graph2::Graph")
graph2_GraphComponent = Class(name="graph2::GraphComponent", is_abstract=True)
graph2_Node = Class(name="graph2::Node")
GraphComponent = Class(name="GraphComponent")
graph2_Edge = Class(name="graph2::Edge")

# graph2_Graph class attributes and methods

# graph2_GraphComponent class attributes and methods
graph2_GraphComponent_text: Property = Property(name="text", type=StringType)
graph2_GraphComponent.attributes={graph2_GraphComponent_text}

# graph2_Node class attributes and methods

# GraphComponent class attributes and methods

# graph2_Edge class attributes and methods

# Relationships
gcs0: BinaryAssociation = BinaryAssociation(
    name="gcs0",
    ends={
        Property(name="graph2_GraphComponent", type=graph2_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph2_Graph", type=graph2_GraphComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
src1: BinaryAssociation = BinaryAssociation(
    name="src1",
    ends={
        Property(name="graph2_Node", type=graph2_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="graph2_Edge", type=graph2_Node, multiplicity=Multiplicity(0, 1))
    }
)
trg2: BinaryAssociation = BinaryAssociation(
    name="trg2",
    ends={
        Property(name="graph2_Node4", type=graph2_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="graph2_Edge3", type=graph2_Node, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_graph2_Node_GraphComponent = Generalization(general=GraphComponent, specific=graph2_Node)
gen_graph2_Edge_GraphComponent = Generalization(general=GraphComponent, specific=graph2_Edge)

# Domain Model
domain_model = DomainModel(
    name="graph2",
    types={graph2_Graph, graph2_GraphComponent, graph2_Node, GraphComponent, graph2_Edge},
    associations={gcs0, src1, trg2},
    generalizations={gen_graph2_Node_GraphComponent, gen_graph2_Edge_GraphComponent},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)