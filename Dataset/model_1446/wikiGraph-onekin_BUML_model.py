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
GraphWiki_Wiki = Class(name="GraphWiki::Wiki")
GraphWiki_IndexGraph = Class(name="GraphWiki::IndexGraph")
GraphWiki_CategoryGraph = Class(name="GraphWiki::CategoryGraph")
GraphWiki_ArticleGraph = Class(name="GraphWiki::ArticleGraph")
GraphWiki_ClassificationGraph = Class(name="GraphWiki::ClassificationGraph")
GraphWiki_Node = Class(name="GraphWiki::Node")
GraphWiki_Edge = Class(name="GraphWiki::Edge")
GraphWiki_Revision = Class(name="GraphWiki::Revision")
GraphWiki_Graph = Class(name="GraphWiki::Graph")
Graph = Class(name="Graph")

# GraphWiki_Wiki class attributes and methods
GraphWiki_Wiki_title: Property = Property(name="title", type=StringType)
GraphWiki_Wiki.attributes={GraphWiki_Wiki_title}

# GraphWiki_IndexGraph class attributes and methods

# GraphWiki_CategoryGraph class attributes and methods

# GraphWiki_ArticleGraph class attributes and methods

# GraphWiki_ClassificationGraph class attributes and methods

# GraphWiki_Node class attributes and methods
GraphWiki_Node_title: Property = Property(name="title", type=StringType)
GraphWiki_Node_editions: Property = Property(name="editions", type=IntegerType)
GraphWiki_Node_node_id: Property = Property(name="node_id", type=IntegerType)
GraphWiki_Node_visits: Property = Property(name="visits", type=IntegerType)
GraphWiki_Node_node_namespace: Property = Property(name="node_namespace", type=IntegerType)
GraphWiki_Node_type: Property = Property(name="type", type=StringType)
GraphWiki_Node.attributes={GraphWiki_Node_node_namespace, GraphWiki_Node_node_id, GraphWiki_Node_title, GraphWiki_Node_visits, GraphWiki_Node_type, GraphWiki_Node_editions}

# GraphWiki_Edge class attributes and methods
GraphWiki_Edge_type: Property = Property(name="type", type=StringType)
GraphWiki_Edge.attributes={GraphWiki_Edge_type}

# GraphWiki_Revision class attributes and methods
GraphWiki_Revision_user: Property = Property(name="user", type=StringType)
GraphWiki_Revision_date: Property = Property(name="date", type=StringType)
GraphWiki_Revision_text_id: Property = Property(name="text_id", type=IntegerType)
GraphWiki_Revision.attributes={GraphWiki_Revision_text_id, GraphWiki_Revision_date, GraphWiki_Revision_user}

# GraphWiki_Graph class attributes and methods
GraphWiki_Graph_name: Property = Property(name="name", type=StringType)
GraphWiki_Graph.attributes={GraphWiki_Graph_name}

# Graph class attributes and methods

# Relationships
graphIndex0: BinaryAssociation = BinaryAssociation(
    name="graphIndex0",
    ends={
        Property(name="GraphWiki_IndexGraph", type=GraphWiki_Wiki, multiplicity=Multiplicity(1, 1)),
        Property(name="GraphWiki_Wiki", type=GraphWiki_IndexGraph, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
graphCategories1: BinaryAssociation = BinaryAssociation(
    name="graphCategories1",
    ends={
        Property(name="GraphWiki_CategoryGraph", type=GraphWiki_Wiki, multiplicity=Multiplicity(1, 1)),
        Property(name="GraphWiki_Wiki2", type=GraphWiki_CategoryGraph, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
graphArticles3: BinaryAssociation = BinaryAssociation(
    name="graphArticles3",
    ends={
        Property(name="GraphWiki_ArticleGraph", type=GraphWiki_Wiki, multiplicity=Multiplicity(1, 1)),
        Property(name="GraphWiki_Wiki4", type=GraphWiki_ArticleGraph, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
graphClassification5: BinaryAssociation = BinaryAssociation(
    name="graphClassification5",
    ends={
        Property(name="GraphWiki_ClassificationGraph", type=GraphWiki_Wiki, multiplicity=Multiplicity(1, 1)),
        Property(name="GraphWiki_Wiki6", type=GraphWiki_ClassificationGraph, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nodes7: BinaryAssociation = BinaryAssociation(
    name="nodes7",
    ends={
        Property(name="GraphWiki_Node", type=GraphWiki_Wiki, multiplicity=Multiplicity(1, 1)),
        Property(name="GraphWiki_Wiki8", type=GraphWiki_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edges9: BinaryAssociation = BinaryAssociation(
    name="edges9",
    ends={
        Property(name="GraphWiki_Edge", type=GraphWiki_Wiki, multiplicity=Multiplicity(1, 1)),
        Property(name="GraphWiki_Wiki10", type=GraphWiki_Edge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
revisions11: BinaryAssociation = BinaryAssociation(
    name="revisions11",
    ends={
        Property(name="GraphWiki_Revision", type=GraphWiki_Wiki, multiplicity=Multiplicity(1, 1)),
        Property(name="GraphWiki_Wiki12", type=GraphWiki_Revision, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nodes13: BinaryAssociation = BinaryAssociation(
    name="nodes13",
    ends={
        Property(name="GraphWiki_Node14", type=GraphWiki_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="GraphWiki_Graph", type=GraphWiki_Node, multiplicity=Multiplicity(0, 9999))
    }
)
edges15: BinaryAssociation = BinaryAssociation(
    name="edges15",
    ends={
        Property(name="GraphWiki_Edge17", type=GraphWiki_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="GraphWiki_Graph16", type=GraphWiki_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
lastRevision18: BinaryAssociation = BinaryAssociation(
    name="lastRevision18",
    ends={
        Property(name="GraphWiki_Revision20", type=GraphWiki_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="GraphWiki_Node19", type=GraphWiki_Revision, multiplicity=Multiplicity(0, 1))
    }
)
revisions21: BinaryAssociation = BinaryAssociation(
    name="revisions21",
    ends={
        Property(name="Revision", type=GraphWiki_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="node", type=GraphWiki_Revision, multiplicity=Multiplicity(0, 9999))
    }
)
from22: BinaryAssociation = BinaryAssociation(
    name="from22",
    ends={
        Property(name="GraphWiki_Node24", type=GraphWiki_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="GraphWiki_Edge23", type=GraphWiki_Node, multiplicity=Multiplicity(1, 1))
    }
)
to25: BinaryAssociation = BinaryAssociation(
    name="to25",
    ends={
        Property(name="GraphWiki_Node27", type=GraphWiki_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="GraphWiki_Edge26", type=GraphWiki_Node, multiplicity=Multiplicity(1, 1))
    }
)
node28: BinaryAssociation = BinaryAssociation(
    name="node28",
    ends={
        Property(name="Node", type=GraphWiki_Revision, multiplicity=Multiplicity(1, 1)),
        Property(name="revisions", type=GraphWiki_Node, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_GraphWiki_IndexGraph_Graph = Generalization(general=Graph, specific=GraphWiki_IndexGraph)
gen_GraphWiki_CategoryGraph_Graph = Generalization(general=Graph, specific=GraphWiki_CategoryGraph)
gen_GraphWiki_ArticleGraph_Graph = Generalization(general=Graph, specific=GraphWiki_ArticleGraph)
gen_GraphWiki_ClassificationGraph_Graph = Generalization(general=Graph, specific=GraphWiki_ClassificationGraph)

# Domain Model
domain_model = DomainModel(
    name="GraphWiki",
    types={GraphWiki_Wiki, GraphWiki_IndexGraph, GraphWiki_CategoryGraph, GraphWiki_ArticleGraph, GraphWiki_ClassificationGraph, GraphWiki_Node, GraphWiki_Edge, GraphWiki_Revision, GraphWiki_Graph, Graph},
    associations={graphIndex0, graphCategories1, graphArticles3, graphClassification5, nodes7, edges9, revisions11, nodes13, edges15, lastRevision18, revisions21, from22, to25, node28},
    generalizations={gen_GraphWiki_IndexGraph_Graph, gen_GraphWiki_CategoryGraph_Graph, gen_GraphWiki_ArticleGraph_Graph, gen_GraphWiki_ClassificationGraph_Graph},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)