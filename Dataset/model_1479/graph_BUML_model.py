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
graphmodelling_ModellingType = Class(name="graphmodelling_ModellingType")
graphmodelling_Entity = Class(name="graphmodelling_Entity")
graphmodelling_Graph = Class(name="graphmodelling_Graph")
Entity = Class(name="Entity")
graphmodelling_Node = Class(name="graphmodelling_Node")
graphmodelling_Edge = Class(name="graphmodelling_Edge")
graphmodelling_Property = Class(name="graphmodelling_Property")
graphmodelling_Operation = Class(name="graphmodelling_Operation")

# graphmodelling_ModellingType class attributes and methods
graphmodelling_ModellingType_name: Property = Property(name="name", type=StringType)
graphmodelling_ModellingType.attributes={graphmodelling_ModellingType_name}

# graphmodelling_Entity class attributes and methods
graphmodelling_Entity_ID: Property = Property(name="ID", type=StringType)
graphmodelling_Entity_name: Property = Property(name="name", type=StringType)
graphmodelling_Entity_text: Property = Property(name="text", type=StringType)
graphmodelling_Entity_description: Property = Property(name="description", type=StringType)
graphmodelling_Entity_value: Property = Property(name="value", type=StringType)
graphmodelling_Entity_type: Property = Property(name="type", type=StringType)
graphmodelling_Entity_className: Property = Property(name="className", type=StringType)
graphmodelling_Entity_group: Property = Property(name="group", type=StringType)
graphmodelling_Entity_category: Property = Property(name="category", type=StringType)
graphmodelling_Entity_accessModifier: Property = Property(name="accessModifier", type=StringType)
graphmodelling_Entity_x: Property = Property(name="x", type=StringType)
graphmodelling_Entity_y: Property = Property(name="y", type=StringType)
graphmodelling_Entity_width: Property = Property(name="width", type=StringType)
graphmodelling_Entity_height: Property = Property(name="height", type=StringType)
graphmodelling_Entity.attributes={graphmodelling_Entity_text, graphmodelling_Entity_className, graphmodelling_Entity_x, graphmodelling_Entity_type, graphmodelling_Entity_description, graphmodelling_Entity_y, graphmodelling_Entity_category, graphmodelling_Entity_width, graphmodelling_Entity_group, graphmodelling_Entity_height, graphmodelling_Entity_accessModifier, graphmodelling_Entity_ID, graphmodelling_Entity_name, graphmodelling_Entity_value}

# graphmodelling_Graph class attributes and methods

# Entity class attributes and methods

# graphmodelling_Node class attributes and methods

# graphmodelling_Edge class attributes and methods

# graphmodelling_Property class attributes and methods

# graphmodelling_Operation class attributes and methods

# Relationships
source13: BinaryAssociation = BinaryAssociation(
    name="source13",
    ends={
        Property(name="graphmodelling_Node15", type=graphmodelling_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="graphmodelling_Edge14", type=graphmodelling_Node, multiplicity=Multiplicity(0, 1))
    }
)
target16: BinaryAssociation = BinaryAssociation(
    name="target16",
    ends={
        Property(name="graphmodelling_Node18", type=graphmodelling_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="graphmodelling_Edge17", type=graphmodelling_Node, multiplicity=Multiplicity(0, 1))
    }
)
nodes0: BinaryAssociation = BinaryAssociation(
    name="nodes0",
    ends={
        Property(name="graphmodelling_Node", type=graphmodelling_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graphmodelling_Graph", type=graphmodelling_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edges1: BinaryAssociation = BinaryAssociation(
    name="edges1",
    ends={
        Property(name="graphmodelling_Edge", type=graphmodelling_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graphmodelling_Graph2", type=graphmodelling_Edge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentNode4: BinaryAssociation = BinaryAssociation(
    name="parentNode4",
    ends={
        Property(name="graphmodelling_Node5", type=graphmodelling_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="graphmodelling_Node3", type=graphmodelling_Node, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subNodes7: BinaryAssociation = BinaryAssociation(
    name="subNodes7",
    ends={
        Property(name="graphmodelling_Node8", type=graphmodelling_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="graphmodelling_Node6", type=graphmodelling_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
properties9: BinaryAssociation = BinaryAssociation(
    name="properties9",
    ends={
        Property(name="graphmodelling_Property", type=graphmodelling_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="graphmodelling_Node10", type=graphmodelling_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operations11: BinaryAssociation = BinaryAssociation(
    name="operations11",
    ends={
        Property(name="graphmodelling_Operation", type=graphmodelling_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="graphmodelling_Node12", type=graphmodelling_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_graphmodelling_Edge_Entity = Generalization(general=Entity, specific=graphmodelling_Edge)
gen_graphmodelling_Graph_Entity = Generalization(general=Entity, specific=graphmodelling_Graph)
gen_graphmodelling_Node_Entity = Generalization(general=Entity, specific=graphmodelling_Node)
gen_graphmodelling_Property_Entity = Generalization(general=Entity, specific=graphmodelling_Property)
gen_graphmodelling_Operation_Entity = Generalization(general=Entity, specific=graphmodelling_Operation)

# Domain Model
domain_model = DomainModel(
    name="graphmodelling",
    types={graphmodelling_ModellingType, graphmodelling_Entity, graphmodelling_Graph, Entity, graphmodelling_Node, graphmodelling_Edge, graphmodelling_Property, graphmodelling_Operation},
    associations={source13, target16, nodes0, edges1, parentNode4, subNodes7, properties9, operations11},
    generalizations={gen_graphmodelling_Edge_Entity, gen_graphmodelling_Graph_Entity, gen_graphmodelling_Node_Entity, gen_graphmodelling_Property_Entity, gen_graphmodelling_Operation_Entity},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)