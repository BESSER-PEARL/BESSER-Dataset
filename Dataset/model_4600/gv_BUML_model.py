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
gv_AttributeStatement = Class(name="gv::AttributeStatement")
gv_AbstractGraph = Class(name="gv::AbstractGraph", is_abstract=True)
Identifiable = Class(name="Identifiable")
gv_StatementList = Class(name="gv::StatementList")
gv_AList = Class(name="gv::AList")
Commentable = Class(name="Commentable")
gv_Attribute = Class(name="gv::Attribute")
gv_AssignmentStatement = Class(name="gv::AssignmentStatement")
Statement = Class(name="Statement")
gv_Attributable = Class(name="gv::Attributable", is_abstract=True)
gv_AttributeList = Class(name="gv::AttributeList")
gv_Identifiable = Class(name="gv::Identifiable", is_abstract=True)
gv_NodeStatement = Class(name="gv::NodeStatement")
Attribute = Class(name="Attribute")
gv_NodeID = Class(name="gv::NodeID")
Connectable = Class(name="Connectable")
StrictIdentifiable = Class(name="StrictIdentifiable")
gv_Port = Class(name="gv::Port")
gv_Commentable = Class(name="gv::Commentable", is_abstract=True)
gv_Connectable = Class(name="gv::Connectable", is_abstract=True)
gv_EdgeStatement = Class(name="gv::EdgeStatement")
Attributable = Class(name="Attributable")
gv_Target = Class(name="gv::Target")
gv_Graph = Class(name="gv::Graph")
AbstractGraph = Class(name="AbstractGraph")
gv_Statement = Class(name="gv::Statement", is_abstract=True)
gv_StrictIdentifiable = Class(name="gv::StrictIdentifiable", is_abstract=True)
gv_Subgraph = Class(name="gv::Subgraph")

# gv_AttributeStatement class attributes and methods
gv_AttributeStatement_context: Property = Property(name="context", type=StringType)
gv_AttributeStatement.attributes={gv_AttributeStatement_context}

# gv_AbstractGraph class attributes and methods

# Identifiable class attributes and methods

# gv_StatementList class attributes and methods

# gv_AList class attributes and methods

# Commentable class attributes and methods

# gv_Attribute class attributes and methods
gv_Attribute_key: Property = Property(name="key", type=StringType)
gv_Attribute_value: Property = Property(name="value", type=StringType)
gv_Attribute.attributes={gv_Attribute_key, gv_Attribute_value}

# gv_AssignmentStatement class attributes and methods
gv_AssignmentStatement_left: Property = Property(name="left", type=StringType)
gv_AssignmentStatement_right: Property = Property(name="right", type=StringType)
gv_AssignmentStatement.attributes={gv_AssignmentStatement_right, gv_AssignmentStatement_left}

# Statement class attributes and methods

# gv_Attributable class attributes and methods

# gv_AttributeList class attributes and methods

# gv_Identifiable class attributes and methods
gv_Identifiable_id: Property = Property(name="id", type=StringType)
gv_Identifiable.attributes={gv_Identifiable_id}

# gv_NodeStatement class attributes and methods

# Attribute class attributes and methods

# gv_NodeID class attributes and methods

# Connectable class attributes and methods

# StrictIdentifiable class attributes and methods

# gv_Port class attributes and methods
gv_Port_compass: Property = Property(name="compass", type=StringType)
gv_Port.attributes={gv_Port_compass}

# gv_Commentable class attributes and methods
gv_Commentable_comments: Property = Property(name="comments", type=StringType)
gv_Commentable.attributes={gv_Commentable_comments}

# gv_Connectable class attributes and methods

# gv_EdgeStatement class attributes and methods

# Attributable class attributes and methods

# gv_Target class attributes and methods
gv_Target_operation: Property = Property(name="operation", type=StringType)
gv_Target.attributes={gv_Target_operation}

# gv_Graph class attributes and methods
gv_Graph_strict: Property = Property(name="strict", type=StringType)
gv_Graph_type: Property = Property(name="type", type=StringType)
gv_Graph.attributes={gv_Graph_type, gv_Graph_strict}

# AbstractGraph class attributes and methods

# gv_Statement class attributes and methods

# gv_StrictIdentifiable class attributes and methods
gv_StrictIdentifiable_id: Property = Property(name="id", type=StringType)
gv_StrictIdentifiable.attributes={gv_StrictIdentifiable_id}

# gv_Subgraph class attributes and methods
gv_Subgraph_type: Property = Property(name="type", type=StringType)
gv_Subgraph.attributes={gv_Subgraph_type}

# Relationships
list6: BinaryAssociation = BinaryAssociation(
    name="list6",
    ends={
        Property(name="gv_AList8", type=gv_AttributeList, multiplicity=Multiplicity(1, 1)),
        Property(name="gv_AttributeList7", type=gv_AList, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
next10: BinaryAssociation = BinaryAssociation(
    name="next10",
    ends={
        Property(name="gv_AttributeList11", type=gv_AttributeList, multiplicity=Multiplicity(1, 1)),
        Property(name="gv_AttributeList9", type=gv_AttributeList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements0: BinaryAssociation = BinaryAssociation(
    name="statements0",
    ends={
        Property(name="gv_StatementList", type=gv_AbstractGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="gv_AbstractGraph", type=gv_StatementList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attribute1: BinaryAssociation = BinaryAssociation(
    name="attribute1",
    ends={
        Property(name="gv_Attribute", type=gv_AList, multiplicity=Multiplicity(1, 1)),
        Property(name="gv_AList", type=gv_Attribute, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tail3: BinaryAssociation = BinaryAssociation(
    name="tail3",
    ends={
        Property(name="gv_AList4", type=gv_AList, multiplicity=Multiplicity(1, 1)),
        Property(name="gv_AList2", type=gv_AList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attributes5: BinaryAssociation = BinaryAssociation(
    name="attributes5",
    ends={
        Property(name="gv_AttributeList", type=gv_Attributable, multiplicity=Multiplicity(1, 1)),
        Property(name="gv_Attributable", type=gv_AttributeList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
node_id17: BinaryAssociation = BinaryAssociation(
    name="node_id17",
    ends={
        Property(name="gv_NodeID", type=gv_NodeStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="gv_NodeStatement", type=gv_NodeID, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
port18: BinaryAssociation = BinaryAssociation(
    name="port18",
    ends={
        Property(name="gv_Port", type=gv_NodeID, multiplicity=Multiplicity(1, 1)),
        Property(name="gv_NodeID19", type=gv_Port, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attributes12: BinaryAssociation = BinaryAssociation(
    name="attributes12",
    ends={
        Property(name="gv_AttributeList13", type=gv_AttributeStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="gv_AttributeStatement", type=gv_AttributeList, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source14: BinaryAssociation = BinaryAssociation(
    name="source14",
    ends={
        Property(name="gv_Connectable", type=gv_EdgeStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="gv_EdgeStatement", type=gv_Connectable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
target15: BinaryAssociation = BinaryAssociation(
    name="target15",
    ends={
        Property(name="gv_Target", type=gv_EdgeStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="gv_EdgeStatement16", type=gv_Target, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statement20: BinaryAssociation = BinaryAssociation(
    name="statement20",
    ends={
        Property(name="gv_Statement", type=gv_StatementList, multiplicity=Multiplicity(1, 1)),
        Property(name="gv_StatementList21", type=gv_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tail23: BinaryAssociation = BinaryAssociation(
    name="tail23",
    ends={
        Property(name="gv_StatementList24", type=gv_StatementList, multiplicity=Multiplicity(1, 1)),
        Property(name="gv_StatementList22", type=gv_StatementList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
next_target26: BinaryAssociation = BinaryAssociation(
    name="next_target26",
    ends={
        Property(name="gv_Target27", type=gv_Target, multiplicity=Multiplicity(1, 1)),
        Property(name="gv_Target25", type=gv_Target, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target28: BinaryAssociation = BinaryAssociation(
    name="target28",
    ends={
        Property(name="gv_Connectable30", type=gv_Target, multiplicity=Multiplicity(1, 1)),
        Property(name="gv_Target29", type=gv_Connectable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_gv_Attribute_Commentable = Generalization(general=Commentable, specific=gv_Attribute)
gen_gv_AttributeList_Commentable = Generalization(general=Commentable, specific=gv_AttributeList)
gen_gv_AttributeStatement_Statement = Generalization(general=Statement, specific=gv_AttributeStatement)
gen_gv_AttributeStatement_Commentable = Generalization(general=Commentable, specific=gv_AttributeStatement)
gen_gv_AbstractGraph_Identifiable = Generalization(general=Identifiable, specific=gv_AbstractGraph)
gen_gv_AList_Commentable = Generalization(general=Commentable, specific=gv_AList)
gen_gv_AssignmentStatement_Statement = Generalization(general=Statement, specific=gv_AssignmentStatement)
gen_gv_AssignmentStatement_Commentable = Generalization(general=Commentable, specific=gv_AssignmentStatement)
gen_gv_NodeStatement_Statement = Generalization(general=Statement, specific=gv_NodeStatement)
gen_gv_NodeStatement_Attributable = Generalization(general=Attributable, specific=gv_NodeStatement)
gen_gv_NodeStatement_Attribute = Generalization(general=Attribute, specific=gv_NodeStatement)
gen_gv_NodeID_Connectable = Generalization(general=Connectable, specific=gv_NodeID)
gen_gv_NodeID_StrictIdentifiable = Generalization(general=StrictIdentifiable, specific=gv_NodeID)
gen_gv_NodeID_Commentable = Generalization(general=Commentable, specific=gv_NodeID)
gen_gv_EdgeStatement_Statement = Generalization(general=Statement, specific=gv_EdgeStatement)
gen_gv_EdgeStatement_Attributable = Generalization(general=Attributable, specific=gv_EdgeStatement)
gen_gv_EdgeStatement_Commentable = Generalization(general=Commentable, specific=gv_EdgeStatement)
gen_gv_Graph_AbstractGraph = Generalization(general=AbstractGraph, specific=gv_Graph)
gen_gv_Graph_Commentable = Generalization(general=Commentable, specific=gv_Graph)
gen_gv_Port_Identifiable = Generalization(general=Identifiable, specific=gv_Port)
gen_gv_Port_Commentable = Generalization(general=Commentable, specific=gv_Port)
gen_gv_StatementList_Commentable = Generalization(general=Commentable, specific=gv_StatementList)
gen_gv_Subgraph_AbstractGraph = Generalization(general=AbstractGraph, specific=gv_Subgraph)
gen_gv_Subgraph_Connectable = Generalization(general=Connectable, specific=gv_Subgraph)
gen_gv_Subgraph_Commentable = Generalization(general=Commentable, specific=gv_Subgraph)
gen_gv_Target_Commentable = Generalization(general=Commentable, specific=gv_Target)

# Domain Model
domain_model = DomainModel(
    name="gv",
    types={gv_AttributeStatement, gv_AbstractGraph, Identifiable, gv_StatementList, gv_AList, Commentable, gv_Attribute, gv_AssignmentStatement, Statement, gv_Attributable, gv_AttributeList, gv_Identifiable, gv_NodeStatement, Attribute, gv_NodeID, Connectable, StrictIdentifiable, gv_Port, gv_Commentable, gv_Connectable, gv_EdgeStatement, Attributable, gv_Target, gv_Graph, AbstractGraph, gv_Statement, gv_StrictIdentifiable, gv_Subgraph, Compass},
    associations={list6, next10, statements0, attribute1, tail3, attributes5, node_id17, port18, attributes12, source14, target15, statement20, tail23, next_target26, target28},
    generalizations={gen_gv_Attribute_Commentable, gen_gv_AttributeList_Commentable, gen_gv_AttributeStatement_Statement, gen_gv_AttributeStatement_Commentable, gen_gv_AbstractGraph_Identifiable, gen_gv_AList_Commentable, gen_gv_AssignmentStatement_Statement, gen_gv_AssignmentStatement_Commentable, gen_gv_NodeStatement_Statement, gen_gv_NodeStatement_Attributable, gen_gv_NodeStatement_Attribute, gen_gv_NodeID_Connectable, gen_gv_NodeID_StrictIdentifiable, gen_gv_NodeID_Commentable, gen_gv_EdgeStatement_Statement, gen_gv_EdgeStatement_Attributable, gen_gv_EdgeStatement_Commentable, gen_gv_Graph_AbstractGraph, gen_gv_Graph_Commentable, gen_gv_Port_Identifiable, gen_gv_Port_Commentable, gen_gv_StatementList_Commentable, gen_gv_Subgraph_AbstractGraph, gen_gv_Subgraph_Connectable, gen_gv_Subgraph_Commentable, gen_gv_Target_Commentable},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)