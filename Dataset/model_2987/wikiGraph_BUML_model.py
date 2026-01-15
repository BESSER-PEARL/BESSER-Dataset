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
wiki_Wiki = Class(name="wiki::Wiki")
wiki_IndexGraph = Class(name="wiki::IndexGraph")
wiki_ArticleGraph = Class(name="wiki::ArticleGraph")
wiki_ClassificationGraph = Class(name="wiki::ClassificationGraph")
wiki_Node = Class(name="wiki::Node")
wiki_Edge = Class(name="wiki::Edge")
wiki_Revision = Class(name="wiki::Revision")
wiki_Graph = Class(name="wiki::Graph")
wiki_CategoryGraph = Class(name="wiki::CategoryGraph")
Graph = Class(name="Graph")

# wiki_Wiki class attributes and methods
wiki_Wiki_title: Property = Property(name="title", type=StringType)
wiki_Wiki.attributes={wiki_Wiki_title}

# wiki_IndexGraph class attributes and methods

# wiki_ArticleGraph class attributes and methods

# wiki_ClassificationGraph class attributes and methods

# wiki_Node class attributes and methods
wiki_Node_title: Property = Property(name="title", type=StringType)
wiki_Node_editions: Property = Property(name="editions", type=IntegerType)
wiki_Node_node_id: Property = Property(name="node_id", type=IntegerType)
wiki_Node_visits: Property = Property(name="visits", type=IntegerType)
wiki_Node_type: Property = Property(name="type", type=StringType)
wiki_Node_node_namespace: Property = Property(name="node_namespace", type=IntegerType)
wiki_Node.attributes={wiki_Node_node_namespace, wiki_Node_type, wiki_Node_editions, wiki_Node_title, wiki_Node_node_id, wiki_Node_visits}

# wiki_Edge class attributes and methods
wiki_Edge_type: Property = Property(name="type", type=StringType)
wiki_Edge.attributes={wiki_Edge_type}

# wiki_Revision class attributes and methods
wiki_Revision_user: Property = Property(name="user", type=StringType)
wiki_Revision_date: Property = Property(name="date", type=StringType)
wiki_Revision_text_id: Property = Property(name="text_id", type=IntegerType)
wiki_Revision.attributes={wiki_Revision_user, wiki_Revision_date, wiki_Revision_text_id}

# wiki_Graph class attributes and methods
wiki_Graph_name: Property = Property(name="name", type=StringType)
wiki_Graph.attributes={wiki_Graph_name}

# wiki_CategoryGraph class attributes and methods

# Graph class attributes and methods

# Relationships
graphIndex0: BinaryAssociation = BinaryAssociation(
    name="graphIndex0",
    ends={
        Property(name="wiki_IndexGraph", type=wiki_Wiki, multiplicity=Multiplicity(1, 1)),
        Property(name="wiki_Wiki", type=wiki_IndexGraph, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
graphArticles3: BinaryAssociation = BinaryAssociation(
    name="graphArticles3",
    ends={
        Property(name="wiki_ArticleGraph", type=wiki_Wiki, multiplicity=Multiplicity(1, 1)),
        Property(name="wiki_Wiki4", type=wiki_ArticleGraph, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
graphClassification5: BinaryAssociation = BinaryAssociation(
    name="graphClassification5",
    ends={
        Property(name="wiki_ClassificationGraph", type=wiki_Wiki, multiplicity=Multiplicity(1, 1)),
        Property(name="wiki_Wiki6", type=wiki_ClassificationGraph, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nodes7: BinaryAssociation = BinaryAssociation(
    name="nodes7",
    ends={
        Property(name="wiki_Node", type=wiki_Wiki, multiplicity=Multiplicity(1, 1)),
        Property(name="wiki_Wiki8", type=wiki_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edges9: BinaryAssociation = BinaryAssociation(
    name="edges9",
    ends={
        Property(name="wiki_Edge", type=wiki_Wiki, multiplicity=Multiplicity(1, 1)),
        Property(name="wiki_Wiki10", type=wiki_Edge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
revisions11: BinaryAssociation = BinaryAssociation(
    name="revisions11",
    ends={
        Property(name="wiki_Revision", type=wiki_Wiki, multiplicity=Multiplicity(1, 1)),
        Property(name="wiki_Wiki12", type=wiki_Revision, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
noderefs13: BinaryAssociation = BinaryAssociation(
    name="noderefs13",
    ends={
        Property(name="wiki_Node14", type=wiki_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="wiki_Graph", type=wiki_Node, multiplicity=Multiplicity(0, 9999))
    }
)
edgerefs15: BinaryAssociation = BinaryAssociation(
    name="edgerefs15",
    ends={
        Property(name="wiki_Edge17", type=wiki_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="wiki_Graph16", type=wiki_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
graphCategories1: BinaryAssociation = BinaryAssociation(
    name="graphCategories1",
    ends={
        Property(name="wiki_CategoryGraph", type=wiki_Wiki, multiplicity=Multiplicity(1, 1)),
        Property(name="wiki_Wiki2", type=wiki_CategoryGraph, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lastRevision18: BinaryAssociation = BinaryAssociation(
    name="lastRevision18",
    ends={
        Property(name="wiki_Revision20", type=wiki_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="wiki_Node19", type=wiki_Revision, multiplicity=Multiplicity(0, 1))
    }
)
revisions21: BinaryAssociation = BinaryAssociation(
    name="revisions21",
    ends={
        Property(name="Revision", type=wiki_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="node", type=wiki_Revision, multiplicity=Multiplicity(0, 9999))
    }
)
node22: BinaryAssociation = BinaryAssociation(
    name="node22",
    ends={
        Property(name="Node", type=wiki_Revision, multiplicity=Multiplicity(1, 1)),
        Property(name="revisions", type=wiki_Node, multiplicity=Multiplicity(0, 1))
    }
)
to23: BinaryAssociation = BinaryAssociation(
    name="to23",
    ends={
        Property(name="wiki_Node25", type=wiki_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="wiki_Edge24", type=wiki_Node, multiplicity=Multiplicity(1, 1))
    }
)
from26: BinaryAssociation = BinaryAssociation(
    name="from26",
    ends={
        Property(name="wiki_Node28", type=wiki_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="wiki_Edge27", type=wiki_Node, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_wiki_IndexGraph_Graph = Generalization(general=Graph, specific=wiki_IndexGraph)
gen_wiki_CategoryGraph_Graph = Generalization(general=Graph, specific=wiki_CategoryGraph)
gen_wiki_ArticleGraph_Graph = Generalization(general=Graph, specific=wiki_ArticleGraph)
gen_wiki_ClassificationGraph_Graph = Generalization(general=Graph, specific=wiki_ClassificationGraph)

# Domain Model
domain_model = DomainModel(
    name="wiki",
    types={wiki_Wiki, wiki_IndexGraph, wiki_ArticleGraph, wiki_ClassificationGraph, wiki_Node, wiki_Edge, wiki_Revision, wiki_Graph, wiki_CategoryGraph, Graph},
    associations={graphIndex0, graphArticles3, graphClassification5, nodes7, edges9, revisions11, noderefs13, edgerefs15, graphCategories1, lastRevision18, revisions21, node22, to23, from26},
    generalizations={gen_wiki_IndexGraph_Graph, gen_wiki_CategoryGraph_Graph, gen_wiki_ArticleGraph_Graph, gen_wiki_ClassificationGraph_Graph},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)