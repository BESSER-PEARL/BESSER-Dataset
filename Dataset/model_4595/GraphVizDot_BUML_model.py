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
EdgeOperator: Enumeration = Enumeration(
    name="EdgeOperator",
    literals={
            EnumerationLiteral(name="directed"),
			EnumerationLiteral(name="undirected")
    }
)

GraphType: Enumeration = Enumeration(
    name="GraphType",
    literals={
            EnumerationLiteral(name="graph"),
			EnumerationLiteral(name="digraph")
    }
)

AttributeType: Enumeration = Enumeration(
    name="AttributeType",
    literals={
            EnumerationLiteral(name="graph"),
			EnumerationLiteral(name="node"),
			EnumerationLiteral(name="edge")
    }
)

# Classes
dot_GraphvizModel = Class(name="dot::GraphvizModel")
dot_Graph = Class(name="dot::Graph")
dot_Statement = Class(name="dot::Statement")
dot_Attribute = Class(name="dot::Attribute")
Statement = Class(name="Statement")
dot_NodeStatement = Class(name="dot::NodeStatement")
dot_Node = Class(name="dot::Node")
dot_Port = Class(name="dot::Port")
dot_EdgeStatement = Class(name="dot::EdgeStatement")
dot_Subgraph = Class(name="dot::Subgraph")
dot_AttributeStatement = Class(name="dot::AttributeStatement")
dot_EdgeTarget = Class(name="dot::EdgeTarget")

# dot_GraphvizModel class attributes and methods

# dot_Graph class attributes and methods
dot_Graph_strict: Property = Property(name="strict", type=BooleanType)
dot_Graph_type: Property = Property(name="type", type=StringType)
dot_Graph_name: Property = Property(name="name", type=StringType)
dot_Graph.attributes={dot_Graph_strict, dot_Graph_type, dot_Graph_name}

# dot_Statement class attributes and methods

# dot_Attribute class attributes and methods
dot_Attribute_name: Property = Property(name="name", type=StringType)
dot_Attribute_value: Property = Property(name="value", type=StringType)
dot_Attribute.attributes={dot_Attribute_name, dot_Attribute_value}

# Statement class attributes and methods

# dot_NodeStatement class attributes and methods

# dot_Node class attributes and methods
dot_Node_name: Property = Property(name="name", type=StringType)
dot_Node.attributes={dot_Node_name}

# dot_Port class attributes and methods
dot_Port_name: Property = Property(name="name", type=StringType)
dot_Port_compass_pt: Property = Property(name="compass_pt", type=StringType)
dot_Port.attributes={dot_Port_compass_pt, dot_Port_name}

# dot_EdgeStatement class attributes and methods

# dot_Subgraph class attributes and methods
dot_Subgraph_name: Property = Property(name="name", type=StringType)
dot_Subgraph.attributes={dot_Subgraph_name}

# dot_AttributeStatement class attributes and methods
dot_AttributeStatement_type: Property = Property(name="type", type=StringType)
dot_AttributeStatement.attributes={dot_AttributeStatement_type}

# dot_EdgeTarget class attributes and methods
dot_EdgeTarget_operator: Property = Property(name="operator", type=StringType)
dot_EdgeTarget.attributes={dot_EdgeTarget_operator}

# Relationships
graphs0: BinaryAssociation = BinaryAssociation(
    name="graphs0",
    ends={
        Property(name="dot_Graph", type=dot_GraphvizModel, multiplicity=Multiplicity(1, 1)),
        Property(name="dot_GraphvizModel", type=dot_Graph, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statements1: BinaryAssociation = BinaryAssociation(
    name="statements1",
    ends={
        Property(name="dot_Statement", type=dot_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="dot_Graph2", type=dot_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
node3: BinaryAssociation = BinaryAssociation(
    name="node3",
    ends={
        Property(name="dot_Node", type=dot_NodeStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dot_NodeStatement", type=dot_Node, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attributes4: BinaryAssociation = BinaryAssociation(
    name="attributes4",
    ends={
        Property(name="dot_Attribute", type=dot_NodeStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dot_NodeStatement5", type=dot_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
port6: BinaryAssociation = BinaryAssociation(
    name="port6",
    ends={
        Property(name="dot_Port", type=dot_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="dot_Node7", type=dot_Port, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attributes12: BinaryAssociation = BinaryAssociation(
    name="attributes12",
    ends={
        Property(name="dot_Attribute14", type=dot_EdgeStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dot_EdgeStatement13", type=dot_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
targetSubgraph15: BinaryAssociation = BinaryAssociation(
    name="targetSubgraph15",
    ends={
        Property(name="dot_Subgraph", type=dot_EdgeTarget, multiplicity=Multiplicity(1, 1)),
        Property(name="dot_EdgeTarget16", type=dot_Subgraph, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
targetnode17: BinaryAssociation = BinaryAssociation(
    name="targetnode17",
    ends={
        Property(name="dot_Node19", type=dot_EdgeTarget, multiplicity=Multiplicity(1, 1)),
        Property(name="dot_EdgeTarget18", type=dot_Node, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attributes20: BinaryAssociation = BinaryAssociation(
    name="attributes20",
    ends={
        Property(name="dot_Attribute21", type=dot_AttributeStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dot_AttributeStatement", type=dot_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statements22: BinaryAssociation = BinaryAssociation(
    name="statements22",
    ends={
        Property(name="dot_Statement24", type=dot_Subgraph, multiplicity=Multiplicity(1, 1)),
        Property(name="dot_Subgraph23", type=dot_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sourceNode8: BinaryAssociation = BinaryAssociation(
    name="sourceNode8",
    ends={
        Property(name="dot_Node9", type=dot_EdgeStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dot_EdgeStatement", type=dot_Node, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
edgeTargets10: BinaryAssociation = BinaryAssociation(
    name="edgeTargets10",
    ends={
        Property(name="dot_EdgeTarget", type=dot_EdgeStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dot_EdgeStatement11", type=dot_EdgeTarget, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_dot_Attribute_Statement = Generalization(general=Statement, specific=dot_Attribute)
gen_dot_NodeStatement_Statement = Generalization(general=Statement, specific=dot_NodeStatement)
gen_dot_EdgeStatement_Statement = Generalization(general=Statement, specific=dot_EdgeStatement)
gen_dot_AttributeStatement_Statement = Generalization(general=Statement, specific=dot_AttributeStatement)
gen_dot_Subgraph_Statement = Generalization(general=Statement, specific=dot_Subgraph)

# Domain Model
domain_model = DomainModel(
    name="dot",
    types={dot_GraphvizModel, dot_Graph, dot_Statement, dot_Attribute, Statement, dot_NodeStatement, dot_Node, dot_Port, dot_EdgeStatement, dot_Subgraph, dot_AttributeStatement, dot_EdgeTarget, EdgeOperator, GraphType, AttributeType},
    associations={graphs0, statements1, node3, attributes4, port6, attributes12, targetSubgraph15, targetnode17, attributes20, statements22, sourceNode8, edgeTargets10},
    generalizations={gen_dot_Attribute_Statement, gen_dot_NodeStatement_Statement, gen_dot_EdgeStatement_Statement, gen_dot_AttributeStatement_Statement, gen_dot_Subgraph_Statement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)