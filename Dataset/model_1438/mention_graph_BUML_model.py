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
mention_graph_MentionGraph = Class(name="mention::graph::MentionGraph")
mention_graph_Node = Class(name="mention::graph::Node", is_abstract=True)
mention_graph_Edge = Class(name="mention::graph::Edge")
mention_graph_User = Class(name="mention::graph::User")
Node = Class(name="Node")
mention_graph_HashTag = Class(name="mention::graph::HashTag")

# mention_graph_MentionGraph class attributes and methods

# mention_graph_Node class attributes and methods
mention_graph_Node_value: Property = Property(name="value", type=StringType)
mention_graph_Node.attributes={mention_graph_Node_value}

# mention_graph_Edge class attributes and methods

# mention_graph_User class attributes and methods

# Node class attributes and methods

# mention_graph_HashTag class attributes and methods
mention_graph_HashTag_count: Property = Property(name="count", type=IntegerType)
mention_graph_HashTag.attributes={mention_graph_HashTag_count}

# Relationships
nodes0: BinaryAssociation = BinaryAssociation(
    name="nodes0",
    ends={
        Property(name="mention_graph_Node", type=mention_graph_MentionGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="mention_graph_MentionGraph", type=mention_graph_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source4: BinaryAssociation = BinaryAssociation(
    name="source4",
    ends={
        Property(name="mention_graph_Node6", type=mention_graph_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="mention_graph_Edge5", type=mention_graph_Node, multiplicity=Multiplicity(1, 1))
    }
)
target7: BinaryAssociation = BinaryAssociation(
    name="target7",
    ends={
        Property(name="mention_graph_Node9", type=mention_graph_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="mention_graph_Edge8", type=mention_graph_Node, multiplicity=Multiplicity(1, 1))
    }
)
edges1: BinaryAssociation = BinaryAssociation(
    name="edges1",
    ends={
        Property(name="mention_graph_Edge", type=mention_graph_MentionGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="mention_graph_MentionGraph2", type=mention_graph_Edge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relatedHashtags3: BinaryAssociation = BinaryAssociation(
    name="relatedHashtags3",
    ends={
        Property(name="mention_graph_HashTag", type=mention_graph_User, multiplicity=Multiplicity(1, 1)),
        Property(name="mention_graph_User", type=mention_graph_HashTag, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_mention_graph_User_Node = Generalization(general=Node, specific=mention_graph_User)
gen_mention_graph_HashTag_Node = Generalization(general=Node, specific=mention_graph_HashTag)

# Domain Model
domain_model = DomainModel(
    name="mention_graph",
    types={mention_graph_MentionGraph, mention_graph_Node, mention_graph_Edge, mention_graph_User, Node, mention_graph_HashTag},
    associations={nodes0, source4, target7, edges1, relatedHashtags3},
    generalizations={gen_mention_graph_User_Node, gen_mention_graph_HashTag_Node},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)