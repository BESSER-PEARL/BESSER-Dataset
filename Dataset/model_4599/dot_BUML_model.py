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
SettingsType: Enumeration = Enumeration(
    name="SettingsType",
    literals={
            EnumerationLiteral(name="GRAPH"),
			EnumerationLiteral(name="NODE"),
			EnumerationLiteral(name="EDGE")
    }
)

# Classes
dot_Graph = Class(name="dot::Graph")
Identifiable = Class(name="Identifiable")
Statement = Class(name="Statement")
dot_Statement = Class(name="dot::Statement", is_abstract=True)
dot_Node = Class(name="dot::Node")
AttributedItem = Class(name="AttributedItem")
dot_RecordNode = Class(name="dot::RecordNode")
Node = Class(name="Node")
dot_InnerNode = Class(name="dot::InnerNode")
dot_Edge = Class(name="dot::Edge")
dot_Identifiable = Class(name="dot::Identifiable", is_abstract=True)
dot_Settings = Class(name="dot::Settings")
dot_Assignment = Class(name="dot::Assignment")
dot_StringToStringMapEntry = Class(name="dot::StringToStringMapEntry")
dot_AttributedItem = Class(name="dot::AttributedItem", is_abstract=True)

# dot_Graph class attributes and methods

# Identifiable class attributes and methods

# Statement class attributes and methods

# dot_Statement class attributes and methods

# dot_Node class attributes and methods

# AttributedItem class attributes and methods

# dot_RecordNode class attributes and methods

# Node class attributes and methods

# dot_InnerNode class attributes and methods

# dot_Edge class attributes and methods

# dot_Identifiable class attributes and methods
dot_Identifiable_id: Property = Property(name="id", type=StringType)
dot_Identifiable.attributes={dot_Identifiable_id}

# dot_Settings class attributes and methods
dot_Settings_type: Property = Property(name="type", type=StringType)
dot_Settings.attributes={dot_Settings_type}

# dot_Assignment class attributes and methods
dot_Assignment_key: Property = Property(name="key", type=StringType)
dot_Assignment_value: Property = Property(name="value", type=StringType)
dot_Assignment.attributes={dot_Assignment_key, dot_Assignment_value}

# dot_StringToStringMapEntry class attributes and methods
dot_StringToStringMapEntry_key: Property = Property(name="key", type=StringType)
dot_StringToStringMapEntry_value: Property = Property(name="value", type=StringType)
dot_StringToStringMapEntry.attributes={dot_StringToStringMapEntry_value, dot_StringToStringMapEntry_key}

# dot_AttributedItem class attributes and methods

# Relationships
statements0: BinaryAssociation = BinaryAssociation(
    name="statements0",
    ends={
        Property(name="dot_Statement", type=dot_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="dot_Graph", type=dot_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
innerNodes1: BinaryAssociation = BinaryAssociation(
    name="innerNodes1",
    ends={
        Property(name="InnerNode", type=dot_RecordNode, multiplicity=Multiplicity(1, 1)),
        Property(name="recordNode", type=dot_InnerNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source2: BinaryAssociation = BinaryAssociation(
    name="source2",
    ends={
        Property(name="dot_Node", type=dot_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="dot_Edge", type=dot_Node, multiplicity=Multiplicity(1, 1))
    }
)
target3: BinaryAssociation = BinaryAssociation(
    name="target3",
    ends={
        Property(name="dot_Node5", type=dot_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="dot_Edge4", type=dot_Node, multiplicity=Multiplicity(1, 1))
    }
)
recordNode7: BinaryAssociation = BinaryAssociation(
    name="recordNode7",
    ends={
        Property(name="RecordNode", type=dot_InnerNode, multiplicity=Multiplicity(1, 1)),
        Property(name="innerNodes", type=dot_RecordNode, multiplicity=Multiplicity(1, 1))
    }
)
attributes6: BinaryAssociation = BinaryAssociation(
    name="attributes6",
    ends={
        Property(name="dot_StringToStringMapEntry", type=dot_AttributedItem, multiplicity=Multiplicity(1, 1)),
        Property(name="dot_AttributedItem", type=dot_StringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_dot_Graph_Identifiable = Generalization(general=Identifiable, specific=dot_Graph)
gen_dot_Graph_Statement = Generalization(general=Statement, specific=dot_Graph)
gen_dot_Node_Identifiable = Generalization(general=Identifiable, specific=dot_Node)
gen_dot_Node_Statement = Generalization(general=Statement, specific=dot_Node)
gen_dot_Node_AttributedItem = Generalization(general=AttributedItem, specific=dot_Node)
gen_dot_RecordNode_Node = Generalization(general=Node, specific=dot_RecordNode)
gen_dot_Edge_Statement = Generalization(general=Statement, specific=dot_Edge)
gen_dot_Edge_AttributedItem = Generalization(general=AttributedItem, specific=dot_Edge)
gen_dot_Settings_Statement = Generalization(general=Statement, specific=dot_Settings)
gen_dot_Settings_AttributedItem = Generalization(general=AttributedItem, specific=dot_Settings)
gen_dot_InnerNode_Node = Generalization(general=Node, specific=dot_InnerNode)
gen_dot_Assignment_Statement = Generalization(general=Statement, specific=dot_Assignment)

# Domain Model
domain_model = DomainModel(
    name="dot",
    types={dot_Graph, Identifiable, Statement, dot_Statement, dot_Node, AttributedItem, dot_RecordNode, Node, dot_InnerNode, dot_Edge, dot_Identifiable, dot_Settings, dot_Assignment, dot_StringToStringMapEntry, dot_AttributedItem, SettingsType},
    associations={statements0, innerNodes1, source2, target3, recordNode7, attributes6},
    generalizations={gen_dot_Graph_Identifiable, gen_dot_Graph_Statement, gen_dot_Node_Identifiable, gen_dot_Node_Statement, gen_dot_Node_AttributedItem, gen_dot_RecordNode_Node, gen_dot_Edge_Statement, gen_dot_Edge_AttributedItem, gen_dot_Settings_Statement, gen_dot_Settings_AttributedItem, gen_dot_InnerNode_Node, gen_dot_Assignment_Statement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)