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
Compass: Enumeration = Enumeration(
    name="Compass",
    literals={
            EnumerationLiteral(name="NORTH"),
			EnumerationLiteral(name="NORTH_EAST"),
			EnumerationLiteral(name="EAST"),
			EnumerationLiteral(name="SOUTH_EAST"),
			EnumerationLiteral(name="SOUTH"),
			EnumerationLiteral(name="SOUTH_WEST"),
			EnumerationLiteral(name="WEST"),
			EnumerationLiteral(name="NORTH_WEST"),
			EnumerationLiteral(name="CENTER"),
			EnumerationLiteral(name="APPROPRIATE")
    }
)

# Classes
dot_AbstractGraph = Class(name="dot::AbstractGraph", is_abstract=True)
Identifiable = Class(name="Identifiable")
dot_StatementList = Class(name="dot::StatementList")
dot_AList = Class(name="dot::AList")
Commentable = Class(name="Commentable")
dot_AttributeStatement = Class(name="dot::AttributeStatement")
Attributable = Class(name="Attributable")
dot_Commentable = Class(name="dot::Commentable", is_abstract=True)
dot_Attribute = Class(name="dot::Attribute")
dot_AssignmentStatement = Class(name="dot::AssignmentStatement")
Statement = Class(name="Statement")
dot_Attributable = Class(name="dot::Attributable", is_abstract=True)
dot_AttributeList = Class(name="dot::AttributeList")
dot_NodeID = Class(name="dot::NodeID")
Connectable = Class(name="Connectable")
StrictIdentifiable = Class(name="StrictIdentifiable")
dot_Port = Class(name="dot::Port")
dot_Statement = Class(name="dot::Statement", is_abstract=True)
dot_StrictIdentifiable = Class(name="dot::StrictIdentifiable", is_abstract=True)
dot_Connectable = Class(name="dot::Connectable", is_abstract=True)
dot_EdgeStatement = Class(name="dot::EdgeStatement")
dot_Target = Class(name="dot::Target")
dot_Graph = Class(name="dot::Graph")
AbstractGraph = Class(name="AbstractGraph")
dot_Identifiable = Class(name="dot::Identifiable", is_abstract=True)
dot_NodeStatement = Class(name="dot::NodeStatement")
Attribute = Class(name="Attribute")
dot_Subgraph = Class(name="dot::Subgraph")

# dot_AbstractGraph class attributes and methods

# Identifiable class attributes and methods

# dot_StatementList class attributes and methods

# dot_AList class attributes and methods
dot_AList_m_getAllAttributes: Method = Method(name="getAllAttributes", parameters={}, type=StringType)
dot_AList.methods={dot_AList_m_getAllAttributes}

# Commentable class attributes and methods

# dot_AttributeStatement class attributes and methods
dot_AttributeStatement_context: Property = Property(name="context", type=StringType)
dot_AttributeStatement.attributes={dot_AttributeStatement_context}

# Attributable class attributes and methods

# dot_Commentable class attributes and methods
dot_Commentable_comments: Property = Property(name="comments", type=StringType)
dot_Commentable.attributes={dot_Commentable_comments}

# dot_Attribute class attributes and methods
dot_Attribute_value: Property = Property(name="value", type=StringType)
dot_Attribute_key: Property = Property(name="key", type=StringType)
dot_Attribute.attributes={dot_Attribute_value, dot_Attribute_key}

# dot_AssignmentStatement class attributes and methods
dot_AssignmentStatement_left: Property = Property(name="left", type=StringType)
dot_AssignmentStatement_right: Property = Property(name="right", type=StringType)
dot_AssignmentStatement.attributes={dot_AssignmentStatement_left, dot_AssignmentStatement_right}

# Statement class attributes and methods

# dot_Attributable class attributes and methods
dot_Attributable_m_getAllALists: Method = Method(name="getAllALists", parameters={}, type=StringType)
dot_Attributable.methods={dot_Attributable_m_getAllALists}

# dot_AttributeList class attributes and methods

# dot_NodeID class attributes and methods

# Connectable class attributes and methods

# StrictIdentifiable class attributes and methods

# dot_Port class attributes and methods
dot_Port_compass: Property = Property(name="compass", type=StringType)
dot_Port.attributes={dot_Port_compass}

# dot_Statement class attributes and methods

# dot_StrictIdentifiable class attributes and methods
dot_StrictIdentifiable_id: Property = Property(name="id", type=StringType)
dot_StrictIdentifiable.attributes={dot_StrictIdentifiable_id}

# dot_Connectable class attributes and methods

# dot_EdgeStatement class attributes and methods

# dot_Target class attributes and methods
dot_Target_operation: Property = Property(name="operation", type=StringType)
dot_Target.attributes={dot_Target_operation}

# dot_Graph class attributes and methods
dot_Graph_type: Property = Property(name="type", type=StringType)
dot_Graph_strict: Property = Property(name="strict", type=StringType)
dot_Graph_m_getAllStatements: Method = Method(name="getAllStatements", parameters={}, type=Statement)
dot_Graph.attributes={dot_Graph_strict, dot_Graph_type}
dot_Graph.methods={dot_Graph_m_getAllStatements}

# AbstractGraph class attributes and methods

# dot_Identifiable class attributes and methods
dot_Identifiable_id: Property = Property(name="id", type=StringType)
dot_Identifiable.attributes={dot_Identifiable_id}

# dot_NodeStatement class attributes and methods

# Attribute class attributes and methods

# dot_Subgraph class attributes and methods
dot_Subgraph_type: Property = Property(name="type", type=StringType)
dot_Subgraph.attributes={dot_Subgraph_type}

# Relationships
statements0: BinaryAssociation = BinaryAssociation(
    name="statements0",
    ends={
        Property(name="dot_StatementList", type=dot_AbstractGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="dot_AbstractGraph", type=dot_StatementList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
list6: BinaryAssociation = BinaryAssociation(
    name="list6",
    ends={
        Property(name="dot_AList8", type=dot_AttributeList, multiplicity=Multiplicity(1, 1)),
        Property(name="dot_AttributeList7", type=dot_AList, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
next10: BinaryAssociation = BinaryAssociation(
    name="next10",
    ends={
        Property(name="dot_AttributeList11", type=dot_AttributeList, multiplicity=Multiplicity(1, 1)),
        Property(name="dot_AttributeList9", type=dot_AttributeList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attribute1: BinaryAssociation = BinaryAssociation(
    name="attribute1",
    ends={
        Property(name="dot_Attribute", type=dot_AList, multiplicity=Multiplicity(1, 1)),
        Property(name="dot_AList", type=dot_Attribute, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tail3: BinaryAssociation = BinaryAssociation(
    name="tail3",
    ends={
        Property(name="dot_AList4", type=dot_AList, multiplicity=Multiplicity(1, 1)),
        Property(name="dot_AList2", type=dot_AList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attributes5: BinaryAssociation = BinaryAssociation(
    name="attributes5",
    ends={
        Property(name="dot_AttributeList", type=dot_Attributable, multiplicity=Multiplicity(1, 1)),
        Property(name="dot_Attributable", type=dot_AttributeList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
node_id15: BinaryAssociation = BinaryAssociation(
    name="node_id15",
    ends={
        Property(name="dot_NodeID", type=dot_NodeStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dot_NodeStatement", type=dot_NodeID, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
port16: BinaryAssociation = BinaryAssociation(
    name="port16",
    ends={
        Property(name="dot_Port", type=dot_NodeID, multiplicity=Multiplicity(1, 1)),
        Property(name="dot_NodeID17", type=dot_Port, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement18: BinaryAssociation = BinaryAssociation(
    name="statement18",
    ends={
        Property(name="dot_Statement", type=dot_StatementList, multiplicity=Multiplicity(1, 1)),
        Property(name="dot_StatementList19", type=dot_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tail21: BinaryAssociation = BinaryAssociation(
    name="tail21",
    ends={
        Property(name="dot_StatementList22", type=dot_StatementList, multiplicity=Multiplicity(1, 1)),
        Property(name="dot_StatementList20", type=dot_StatementList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source12: BinaryAssociation = BinaryAssociation(
    name="source12",
    ends={
        Property(name="dot_Connectable", type=dot_EdgeStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dot_EdgeStatement", type=dot_Connectable, multiplicity=Multiplicity(1, 1))
    }
)
target13: BinaryAssociation = BinaryAssociation(
    name="target13",
    ends={
        Property(name="dot_Target", type=dot_EdgeStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dot_EdgeStatement14", type=dot_Target, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
next_target24: BinaryAssociation = BinaryAssociation(
    name="next_target24",
    ends={
        Property(name="dot_Target25", type=dot_Target, multiplicity=Multiplicity(1, 1)),
        Property(name="dot_Target23", type=dot_Target, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target26: BinaryAssociation = BinaryAssociation(
    name="target26",
    ends={
        Property(name="dot_Connectable28", type=dot_Target, multiplicity=Multiplicity(1, 1)),
        Property(name="dot_Target27", type=dot_Connectable, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_dot_AbstractGraph_Identifiable = Generalization(general=Identifiable, specific=dot_AbstractGraph)
gen_dot_AList_Commentable = Generalization(general=Commentable, specific=dot_AList)
gen_dot_AttributeList_Commentable = Generalization(general=Commentable, specific=dot_AttributeList)
gen_dot_AttributeStatement_Statement = Generalization(general=Statement, specific=dot_AttributeStatement)
gen_dot_AttributeStatement_Commentable = Generalization(general=Commentable, specific=dot_AttributeStatement)
gen_dot_AttributeStatement_Attributable = Generalization(general=Attributable, specific=dot_AttributeStatement)
gen_dot_AssignmentStatement_Statement = Generalization(general=Statement, specific=dot_AssignmentStatement)
gen_dot_AssignmentStatement_Commentable = Generalization(general=Commentable, specific=dot_AssignmentStatement)
gen_dot_Attribute_Commentable = Generalization(general=Commentable, specific=dot_Attribute)
gen_dot_NodeID_Connectable = Generalization(general=Connectable, specific=dot_NodeID)
gen_dot_NodeID_StrictIdentifiable = Generalization(general=StrictIdentifiable, specific=dot_NodeID)
gen_dot_NodeID_Commentable = Generalization(general=Commentable, specific=dot_NodeID)
gen_dot_Port_Identifiable = Generalization(general=Identifiable, specific=dot_Port)
gen_dot_Port_Commentable = Generalization(general=Commentable, specific=dot_Port)
gen_dot_StatementList_Commentable = Generalization(general=Commentable, specific=dot_StatementList)
gen_dot_EdgeStatement_Statement = Generalization(general=Statement, specific=dot_EdgeStatement)
gen_dot_EdgeStatement_Attributable = Generalization(general=Attributable, specific=dot_EdgeStatement)
gen_dot_EdgeStatement_Commentable = Generalization(general=Commentable, specific=dot_EdgeStatement)
gen_dot_Graph_AbstractGraph = Generalization(general=AbstractGraph, specific=dot_Graph)
gen_dot_Graph_Commentable = Generalization(general=Commentable, specific=dot_Graph)
gen_dot_NodeStatement_Statement = Generalization(general=Statement, specific=dot_NodeStatement)
gen_dot_NodeStatement_Attributable = Generalization(general=Attributable, specific=dot_NodeStatement)
gen_dot_NodeStatement_Attribute = Generalization(general=Attribute, specific=dot_NodeStatement)
gen_dot_Subgraph_AbstractGraph = Generalization(general=AbstractGraph, specific=dot_Subgraph)
gen_dot_Subgraph_Connectable = Generalization(general=Connectable, specific=dot_Subgraph)
gen_dot_Subgraph_Commentable = Generalization(general=Commentable, specific=dot_Subgraph)
gen_dot_Target_Commentable = Generalization(general=Commentable, specific=dot_Target)

# Domain Model
domain_model = DomainModel(
    name="dot",
    types={dot_AbstractGraph, Identifiable, dot_StatementList, dot_AList, Commentable, dot_AttributeStatement, Attributable, dot_Commentable, dot_Attribute, dot_AssignmentStatement, Statement, dot_Attributable, dot_AttributeList, dot_NodeID, Connectable, StrictIdentifiable, dot_Port, dot_Statement, dot_StrictIdentifiable, dot_Connectable, dot_EdgeStatement, dot_Target, dot_Graph, AbstractGraph, dot_Identifiable, dot_NodeStatement, Attribute, dot_Subgraph, Compass},
    associations={statements0, list6, next10, attribute1, tail3, attributes5, node_id15, port16, statement18, tail21, source12, target13, next_target24, target26},
    generalizations={gen_dot_AbstractGraph_Identifiable, gen_dot_AList_Commentable, gen_dot_AttributeList_Commentable, gen_dot_AttributeStatement_Statement, gen_dot_AttributeStatement_Commentable, gen_dot_AttributeStatement_Attributable, gen_dot_AssignmentStatement_Statement, gen_dot_AssignmentStatement_Commentable, gen_dot_Attribute_Commentable, gen_dot_NodeID_Connectable, gen_dot_NodeID_StrictIdentifiable, gen_dot_NodeID_Commentable, gen_dot_Port_Identifiable, gen_dot_Port_Commentable, gen_dot_StatementList_Commentable, gen_dot_EdgeStatement_Statement, gen_dot_EdgeStatement_Attributable, gen_dot_EdgeStatement_Commentable, gen_dot_Graph_AbstractGraph, gen_dot_Graph_Commentable, gen_dot_NodeStatement_Statement, gen_dot_NodeStatement_Attributable, gen_dot_NodeStatement_Attribute, gen_dot_Subgraph_AbstractGraph, gen_dot_Subgraph_Connectable, gen_dot_Subgraph_Commentable, gen_dot_Target_Commentable},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)