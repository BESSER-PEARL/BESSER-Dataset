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

# Enumerations
FunctionType: Enumeration = Enumeration(
    name="FunctionType",
    literals={
            EnumerationLiteral(name="Boolean"),
			EnumerationLiteral(name="Gausian")
    }
)

VariableType: Enumeration = Enumeration(
    name="VariableType",
    literals={
            EnumerationLiteral(name="Boolean"),
			EnumerationLiteral(name="Real"),
			EnumerationLiteral(name="Categorial")
    }
)

MessageType: Enumeration = Enumeration(
    name="MessageType",
    literals={
            EnumerationLiteral(name="MarginalEdge"),
			EnumerationLiteral(name="VariableToFactor")
    }
)

# Classes
graphEditor_Node = Class(name="graphEditor::Node", is_abstract=True)
graphEditor_Edge = Class(name="graphEditor::Edge")
graphEditor_Message = Class(name="graphEditor::Message")
graphEditor_GraphElement = Class(name="graphEditor::GraphElement", is_abstract=True)
GraphElement = Class(name="GraphElement")
graphEditor_Factornode = Class(name="graphEditor::Factornode")
Node = Class(name="Node")
graphEditor_Variablenode = Class(name="graphEditor::Variablenode")
graphEditor_Graph = Class(name="graphEditor::Graph")

# graphEditor_Node class attributes and methods
graphEditor_Node_name: Property = Property(name="name", type=StringType)
graphEditor_Node.attributes={graphEditor_Node_name}

# graphEditor_Edge class attributes and methods

# graphEditor_Message class attributes and methods
graphEditor_Message_count: Property = Property(name="count", type=IntegerType)
graphEditor_Message_type: Property = Property(name="type", type=StringType)
graphEditor_Message.attributes={graphEditor_Message_count, graphEditor_Message_type}

# graphEditor_GraphElement class attributes and methods
graphEditor_GraphElement_id: Property = Property(name="id", type=StringType)
graphEditor_GraphElement.attributes={graphEditor_GraphElement_id}

# GraphElement class attributes and methods

# graphEditor_Factornode class attributes and methods
graphEditor_Factornode_type: Property = Property(name="type", type=StringType)
graphEditor_Factornode_values: Property = Property(name="values", type=StringType)
graphEditor_Factornode.attributes={graphEditor_Factornode_values, graphEditor_Factornode_type}

# Node class attributes and methods

# graphEditor_Variablenode class attributes and methods
graphEditor_Variablenode_type: Property = Property(name="type", type=StringType)
graphEditor_Variablenode_values: Property = Property(name="values", type=FloatType)
graphEditor_Variablenode_isKnown: Property = Property(name="isKnown", type=BooleanType)
graphEditor_Variablenode.attributes={graphEditor_Variablenode_isKnown, graphEditor_Variablenode_type, graphEditor_Variablenode_values}

# graphEditor_Graph class attributes and methods
graphEditor_Graph_name: Property = Property(name="name", type=StringType)
graphEditor_Graph_result: Property = Property(name="result", type=StringType)
graphEditor_Graph_m_getGraphElement: Method = Method(name="getGraphElement", parameters={Parameter(name='id')}, type=StringType)
graphEditor_Graph_m_getConnectingVariablenodes: Method = Method(name="getConnectingVariablenodes", parameters={Parameter(name='node')}, type=StringType)
graphEditor_Graph.attributes={graphEditor_Graph_name, graphEditor_Graph_result}
graphEditor_Graph.methods={graphEditor_Graph_m_getConnectingVariablenodes, graphEditor_Graph_m_getGraphElement}

# Relationships
nodes0: BinaryAssociation = BinaryAssociation(
    name="nodes0",
    ends={
        Property(name="graphEditor_Node", type=graphEditor_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graphEditor_Graph", type=graphEditor_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edges1: BinaryAssociation = BinaryAssociation(
    name="edges1",
    ends={
        Property(name="graphEditor_Edge", type=graphEditor_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graphEditor_Graph2", type=graphEditor_Edge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
messages3: BinaryAssociation = BinaryAssociation(
    name="messages3",
    ends={
        Property(name="graphEditor_Message", type=graphEditor_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graphEditor_Graph4", type=graphEditor_Message, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
from5: BinaryAssociation = BinaryAssociation(
    name="from5",
    ends={
        Property(name="graphEditor_Node7", type=graphEditor_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="graphEditor_Message6", type=graphEditor_Node, multiplicity=Multiplicity(1, 1))
    }
)
to8: BinaryAssociation = BinaryAssociation(
    name="to8",
    ends={
        Property(name="graphEditor_Node10", type=graphEditor_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="graphEditor_Message9", type=graphEditor_Node, multiplicity=Multiplicity(1, 1))
    }
)
from11: BinaryAssociation = BinaryAssociation(
    name="from11",
    ends={
        Property(name="graphEditor_Node13", type=graphEditor_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="graphEditor_Edge12", type=graphEditor_Node, multiplicity=Multiplicity(1, 1))
    }
)
to14: BinaryAssociation = BinaryAssociation(
    name="to14",
    ends={
        Property(name="graphEditor_Node16", type=graphEditor_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="graphEditor_Edge15", type=graphEditor_Node, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_graphEditor_Node_GraphElement = Generalization(general=GraphElement, specific=graphEditor_Node)
gen_graphEditor_Factornode_Node = Generalization(general=Node, specific=graphEditor_Factornode)
gen_graphEditor_Variablenode_Node = Generalization(general=Node, specific=graphEditor_Variablenode)
gen_graphEditor_Message_GraphElement = Generalization(general=GraphElement, specific=graphEditor_Message)
gen_graphEditor_Edge_GraphElement = Generalization(general=GraphElement, specific=graphEditor_Edge)

# Domain Model
domain_model = DomainModel(
    name="graphEditor",
    types={graphEditor_Node, graphEditor_Edge, graphEditor_Message, graphEditor_GraphElement, GraphElement, graphEditor_Factornode, Node, graphEditor_Variablenode, graphEditor_Graph, FunctionType, VariableType, MessageType},
    associations={nodes0, edges1, messages3, from5, to8, from11, to14},
    generalizations={gen_graphEditor_Node_GraphElement, gen_graphEditor_Factornode_Node, gen_graphEditor_Variablenode_Node, gen_graphEditor_Message_GraphElement, gen_graphEditor_Edge_GraphElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)