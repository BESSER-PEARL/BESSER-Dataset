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
graphmodel_ModellingType = Class(name="graphmodel::ModellingType")
graphmodel_Entity = Class(name="graphmodel::Entity")
graphmodel_Property = Class(name="graphmodel::Property")
graphmodel_Operation = Class(name="graphmodel::Operation")
graphmodel_Graph = Class(name="graphmodel::Graph")
Entity = Class(name="Entity")
graphmodel_Node = Class(name="graphmodel::Node")
graphmodel_Edge = Class(name="graphmodel::Edge")

# graphmodel_ModellingType class attributes and methods
graphmodel_ModellingType_name: Property = Property(name="name", type=StringType)
graphmodel_ModellingType.attributes={graphmodel_ModellingType_name}

# graphmodel_Entity class attributes and methods
graphmodel_Entity_value: Property = Property(name="value", type=StringType)
graphmodel_Entity_type: Property = Property(name="type", type=StringType)
graphmodel_Entity_className: Property = Property(name="className", type=StringType)
graphmodel_Entity_group: Property = Property(name="group", type=StringType)
graphmodel_Entity_category: Property = Property(name="category", type=StringType)
graphmodel_Entity_accessModifier: Property = Property(name="accessModifier", type=StringType)
graphmodel_Entity_x: Property = Property(name="x", type=StringType)
graphmodel_Entity_y: Property = Property(name="y", type=StringType)
graphmodel_Entity_width: Property = Property(name="width", type=StringType)
graphmodel_Entity_height: Property = Property(name="height", type=StringType)
graphmodel_Entity_ID: Property = Property(name="ID", type=StringType)
graphmodel_Entity_name: Property = Property(name="name", type=StringType)
graphmodel_Entity_text: Property = Property(name="text", type=StringType)
graphmodel_Entity_description: Property = Property(name="description", type=StringType)
graphmodel_Entity.attributes={graphmodel_Entity_value, graphmodel_Entity_y, graphmodel_Entity_ID, graphmodel_Entity_accessModifier, graphmodel_Entity_x, graphmodel_Entity_width, graphmodel_Entity_className, graphmodel_Entity_name, graphmodel_Entity_height, graphmodel_Entity_group, graphmodel_Entity_category, graphmodel_Entity_type, graphmodel_Entity_text, graphmodel_Entity_description}

# graphmodel_Property class attributes and methods

# graphmodel_Operation class attributes and methods

# graphmodel_Graph class attributes and methods

# Entity class attributes and methods

# graphmodel_Node class attributes and methods

# graphmodel_Edge class attributes and methods

# Relationships
subNodes7: BinaryAssociation = BinaryAssociation(
    name="subNodes7",
    ends={
        Property(name="graphmodel_Node8", type=graphmodel_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="graphmodel_Node6", type=graphmodel_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
properties9: BinaryAssociation = BinaryAssociation(
    name="properties9",
    ends={
        Property(name="graphmodel_Property", type=graphmodel_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="graphmodel_Node10", type=graphmodel_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operations11: BinaryAssociation = BinaryAssociation(
    name="operations11",
    ends={
        Property(name="graphmodel_Operation", type=graphmodel_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="graphmodel_Node12", type=graphmodel_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nodes0: BinaryAssociation = BinaryAssociation(
    name="nodes0",
    ends={
        Property(name="graphmodel_Node", type=graphmodel_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graphmodel_Graph", type=graphmodel_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edges1: BinaryAssociation = BinaryAssociation(
    name="edges1",
    ends={
        Property(name="graphmodel_Edge", type=graphmodel_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graphmodel_Graph2", type=graphmodel_Edge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentNode4: BinaryAssociation = BinaryAssociation(
    name="parentNode4",
    ends={
        Property(name="graphmodel_Node5", type=graphmodel_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="graphmodel_Node3", type=graphmodel_Node, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source13: BinaryAssociation = BinaryAssociation(
    name="source13",
    ends={
        Property(name="graphmodel_Node15", type=graphmodel_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="graphmodel_Edge14", type=graphmodel_Node, multiplicity=Multiplicity(0, 1))
    }
)
target16: BinaryAssociation = BinaryAssociation(
    name="target16",
    ends={
        Property(name="graphmodel_Node18", type=graphmodel_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="graphmodel_Edge17", type=graphmodel_Node, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_graphmodel_Property_Entity = Generalization(general=Entity, specific=graphmodel_Property)
gen_graphmodel_Operation_Entity = Generalization(general=Entity, specific=graphmodel_Operation)
gen_graphmodel_Graph_Entity = Generalization(general=Entity, specific=graphmodel_Graph)
gen_graphmodel_Node_Entity = Generalization(general=Entity, specific=graphmodel_Node)
gen_graphmodel_Edge_Entity = Generalization(general=Entity, specific=graphmodel_Edge)

# Domain Model
domain_model = DomainModel(
    name="graphmodel",
    types={graphmodel_ModellingType, graphmodel_Entity, graphmodel_Property, graphmodel_Operation, graphmodel_Graph, Entity, graphmodel_Node, graphmodel_Edge},
    associations={subNodes7, properties9, operations11, nodes0, edges1, parentNode4, source13, target16},
    generalizations={gen_graphmodel_Property_Entity, gen_graphmodel_Operation_Entity, gen_graphmodel_Graph_Entity, gen_graphmodel_Node_Entity, gen_graphmodel_Edge_Entity},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)