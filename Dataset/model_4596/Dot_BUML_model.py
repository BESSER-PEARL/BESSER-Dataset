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
attributetype: Enumeration = Enumeration(
    name="attributetype",
    literals={
            EnumerationLiteral(name="graph"),
			EnumerationLiteral(name="node"),
			EnumerationLiteral(name="edge")
    }
)

edgeop: Enumeration = Enumeration(
    name="edgeop",
    literals={
            EnumerationLiteral(name="directed"),
			EnumerationLiteral(name="undirected")
    }
)

graphtype: Enumeration = Enumeration(
    name="graphtype",
    literals={
            EnumerationLiteral(name="graph"),
			EnumerationLiteral(name="digraph")
    }
)

# Classes
dot_stmt = Class(name="dot::stmt")
dot_edge_stmt_node = Class(name="dot::edge::stmt::node")
stmt = Class(name="stmt")
dot_node_id = Class(name="dot::node::id")
dot_graphvizmodel = Class(name="dot::graphvizmodel")
dot_graph = Class(name="dot::graph")
dot_attr_stmt = Class(name="dot::attr::stmt")
dot_a_list = Class(name="dot::a::list")
dot_edgeRHS = Class(name="dot::edgeRHS")
dot_attr_list = Class(name="dot::attr::list")
dot_edge_stmt_subgraph = Class(name="dot::edge::stmt::subgraph")
dot_subgraph = Class(name="dot::subgraph")
dot_node_stmt = Class(name="dot::node::stmt")
dot_attribute = Class(name="dot::attribute")
dot_edgeRHS_node = Class(name="dot::edgeRHS::node")
edgeRHS = Class(name="edgeRHS")
dot_edgeRHS_subgraph = Class(name="dot::edgeRHS::subgraph")

# dot_stmt class attributes and methods

# dot_edge_stmt_node class attributes and methods

# stmt class attributes and methods

# dot_node_id class attributes and methods
dot_node_id_name: Property = Property(name="name", type=StringType)
dot_node_id.attributes={dot_node_id_name}

# dot_graphvizmodel class attributes and methods

# dot_graph class attributes and methods
dot_graph_strict: Property = Property(name="strict", type=BooleanType)
dot_graph_type: Property = Property(name="type", type=StringType)
dot_graph_name: Property = Property(name="name", type=StringType)
dot_graph.attributes={dot_graph_type, dot_graph_strict, dot_graph_name}

# dot_attr_stmt class attributes and methods
dot_attr_stmt_type: Property = Property(name="type", type=StringType)
dot_attr_stmt.attributes={dot_attr_stmt_type}

# dot_a_list class attributes and methods
dot_a_list_name: Property = Property(name="name", type=StringType)
dot_a_list_value: Property = Property(name="value", type=StringType)
dot_a_list.attributes={dot_a_list_value, dot_a_list_name}

# dot_edgeRHS class attributes and methods
dot_edgeRHS_op: Property = Property(name="op", type=StringType)
dot_edgeRHS.attributes={dot_edgeRHS_op}

# dot_attr_list class attributes and methods

# dot_edge_stmt_subgraph class attributes and methods

# dot_subgraph class attributes and methods
dot_subgraph_name: Property = Property(name="name", type=StringType)
dot_subgraph.attributes={dot_subgraph_name}

# dot_node_stmt class attributes and methods
dot_node_stmt_name: Property = Property(name="name", type=StringType)
dot_node_stmt.attributes={dot_node_stmt_name}

# dot_attribute class attributes and methods
dot_attribute_name: Property = Property(name="name", type=StringType)
dot_attribute_value: Property = Property(name="value", type=StringType)
dot_attribute.attributes={dot_attribute_name, dot_attribute_value}

# dot_edgeRHS_node class attributes and methods

# edgeRHS class attributes and methods

# dot_edgeRHS_subgraph class attributes and methods

# Relationships
graphs0: BinaryAssociation = BinaryAssociation(
    name="graphs0",
    ends={
        Property(name="dot_graph", type=dot_graphvizmodel, multiplicity=Multiplicity(1, 1)),
        Property(name="dot_graphvizmodel", type=dot_graph, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stmts1: BinaryAssociation = BinaryAssociation(
    name="stmts1",
    ends={
        Property(name="dot_stmt", type=dot_graph, multiplicity=Multiplicity(1, 1)),
        Property(name="dot_graph2", type=dot_stmt, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
node_id3: BinaryAssociation = BinaryAssociation(
    name="node_id3",
    ends={
        Property(name="dot_node_id", type=dot_edge_stmt_node, multiplicity=Multiplicity(1, 1)),
        Property(name="dot_edge_stmt_node", type=dot_node_id, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attributes17: BinaryAssociation = BinaryAssociation(
    name="attributes17",
    ends={
        Property(name="dot_attr_list18", type=dot_attr_stmt, multiplicity=Multiplicity(1, 1)),
        Property(name="dot_attr_stmt", type=dot_attr_list, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
a_list19: BinaryAssociation = BinaryAssociation(
    name="a_list19",
    ends={
        Property(name="dot_a_list", type=dot_attr_list, multiplicity=Multiplicity(1, 1)),
        Property(name="dot_attr_list20", type=dot_a_list, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edgeRHS4: BinaryAssociation = BinaryAssociation(
    name="edgeRHS4",
    ends={
        Property(name="dot_edgeRHS", type=dot_edge_stmt_node, multiplicity=Multiplicity(1, 1)),
        Property(name="dot_edge_stmt_node5", type=dot_edgeRHS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes6: BinaryAssociation = BinaryAssociation(
    name="attributes6",
    ends={
        Property(name="dot_attr_list", type=dot_edge_stmt_node, multiplicity=Multiplicity(1, 1)),
        Property(name="dot_edge_stmt_node7", type=dot_attr_list, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subgraph8: BinaryAssociation = BinaryAssociation(
    name="subgraph8",
    ends={
        Property(name="dot_subgraph", type=dot_edge_stmt_subgraph, multiplicity=Multiplicity(1, 1)),
        Property(name="dot_edge_stmt_subgraph", type=dot_subgraph, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
edgeRHS9: BinaryAssociation = BinaryAssociation(
    name="edgeRHS9",
    ends={
        Property(name="dot_edgeRHS11", type=dot_edge_stmt_subgraph, multiplicity=Multiplicity(1, 1)),
        Property(name="dot_edge_stmt_subgraph10", type=dot_edgeRHS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attributes12: BinaryAssociation = BinaryAssociation(
    name="attributes12",
    ends={
        Property(name="dot_attr_list14", type=dot_edge_stmt_subgraph, multiplicity=Multiplicity(1, 1)),
        Property(name="dot_edge_stmt_subgraph13", type=dot_attr_list, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes15: BinaryAssociation = BinaryAssociation(
    name="attributes15",
    ends={
        Property(name="dot_attr_list16", type=dot_node_stmt, multiplicity=Multiplicity(1, 1)),
        Property(name="dot_node_stmt", type=dot_attr_list, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stmts21: BinaryAssociation = BinaryAssociation(
    name="stmts21",
    ends={
        Property(name="dot_stmt23", type=dot_subgraph, multiplicity=Multiplicity(1, 1)),
        Property(name="dot_subgraph22", type=dot_stmt, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
node24: BinaryAssociation = BinaryAssociation(
    name="node24",
    ends={
        Property(name="dot_node_id25", type=dot_edgeRHS_node, multiplicity=Multiplicity(1, 1)),
        Property(name="dot_edgeRHS_node", type=dot_node_id, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subgraph26: BinaryAssociation = BinaryAssociation(
    name="subgraph26",
    ends={
        Property(name="dot_subgraph27", type=dot_edgeRHS_subgraph, multiplicity=Multiplicity(1, 1)),
        Property(name="dot_edgeRHS_subgraph", type=dot_subgraph, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_dot_edge_stmt_node_stmt = Generalization(general=stmt, specific=dot_edge_stmt_node)
gen_dot_attr_stmt_stmt = Generalization(general=stmt, specific=dot_attr_stmt)
gen_dot_edge_stmt_subgraph_stmt = Generalization(general=stmt, specific=dot_edge_stmt_subgraph)
gen_dot_node_stmt_stmt = Generalization(general=stmt, specific=dot_node_stmt)
gen_dot_attribute_stmt = Generalization(general=stmt, specific=dot_attribute)
gen_dot_subgraph_stmt = Generalization(general=stmt, specific=dot_subgraph)
gen_dot_edgeRHS_node_edgeRHS = Generalization(general=edgeRHS, specific=dot_edgeRHS_node)
gen_dot_edgeRHS_subgraph_edgeRHS = Generalization(general=edgeRHS, specific=dot_edgeRHS_subgraph)

# Domain Model
domain_model = DomainModel(
    name="dot",
    types={dot_stmt, dot_edge_stmt_node, stmt, dot_node_id, dot_graphvizmodel, dot_graph, dot_attr_stmt, dot_a_list, dot_edgeRHS, dot_attr_list, dot_edge_stmt_subgraph, dot_subgraph, dot_node_stmt, dot_attribute, dot_edgeRHS_node, edgeRHS, dot_edgeRHS_subgraph, attributetype, edgeop, graphtype},
    associations={graphs0, stmts1, node_id3, attributes17, a_list19, edgeRHS4, attributes6, subgraph8, edgeRHS9, attributes12, attributes15, stmts21, node24, subgraph26},
    generalizations={gen_dot_edge_stmt_node_stmt, gen_dot_attr_stmt_stmt, gen_dot_edge_stmt_subgraph_stmt, gen_dot_node_stmt_stmt, gen_dot_attribute_stmt, gen_dot_subgraph_stmt, gen_dot_edgeRHS_node_edgeRHS, gen_dot_edgeRHS_subgraph_edgeRHS},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)