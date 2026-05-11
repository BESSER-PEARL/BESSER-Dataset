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
Dot_Graph = Class(name="Dot_Graph")
NamedElement = Class(name="NamedElement")
Dot_GraphElement = Class(name="Dot_GraphElement")
Dot_NamedElement = Class(name="Dot_NamedElement")
Dot_Node = Class(name="Dot_Node")
GraphElement = Class(name="GraphElement")
Dot_DirectedArc = Class(name="Dot_DirectedArc")

# Dot_Graph class attributes and methods

# NamedElement class attributes and methods

# Dot_GraphElement class attributes and methods
Dot_GraphElement_label: Property = Property(name="label", type=StringType)
Dot_GraphElement_color: Property = Property(name="color", type=StringType)
Dot_GraphElement.attributes={Dot_GraphElement_color, Dot_GraphElement_label}

# Dot_NamedElement class attributes and methods
Dot_NamedElement_name: Property = Property(name="name", type=StringType)
Dot_NamedElement.attributes={Dot_NamedElement_name}

# Dot_Node class attributes and methods
Dot_Node_shape: Property = Property(name="shape", type=StringType)
Dot_Node_style: Property = Property(name="style", type=StringType)
Dot_Node.attributes={Dot_Node_shape, Dot_Node_style}

# GraphElement class attributes and methods

# Dot_DirectedArc class attributes and methods

# Relationships
contents0: BinaryAssociation = BinaryAssociation(
    name="contents0",
    ends={
        Property(name="GraphElement", type=Dot_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph", type=Dot_GraphElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
graph1: BinaryAssociation = BinaryAssociation(
    name="graph1",
    ends={
        Property(name="Graph", type=Dot_GraphElement, multiplicity=Multiplicity(1, 1)),
        Property(name="contents", type=Dot_Graph, multiplicity=Multiplicity(0, 1))
    }
)
sourceNode2: BinaryAssociation = BinaryAssociation(
    name="sourceNode2",
    ends={
        Property(name="Dot_Node", type=Dot_DirectedArc, multiplicity=Multiplicity(1, 1)),
        Property(name="Dot_DirectedArc", type=Dot_Node, multiplicity=Multiplicity(0, 1))
    }
)
targetNode3: BinaryAssociation = BinaryAssociation(
    name="targetNode3",
    ends={
        Property(name="Dot_Node5", type=Dot_DirectedArc, multiplicity=Multiplicity(1, 1)),
        Property(name="Dot_DirectedArc4", type=Dot_Node, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_Dot_Graph_NamedElement = Generalization(general=NamedElement, specific=Dot_Graph)
gen_Dot_GraphElement_NamedElement = Generalization(general=NamedElement, specific=Dot_GraphElement)
gen_Dot_Node_GraphElement = Generalization(general=GraphElement, specific=Dot_Node)
gen_Dot_DirectedArc_GraphElement = Generalization(general=GraphElement, specific=Dot_DirectedArc)

# Domain Model
domain_model = DomainModel(
    name="Dot",
    types={Dot_Graph, NamedElement, Dot_GraphElement, Dot_NamedElement, Dot_Node, GraphElement, Dot_DirectedArc},
    associations={contents0, graph1, sourceNode2, targetNode3},
    generalizations={gen_Dot_Graph_NamedElement, gen_Dot_GraphElement_NamedElement, gen_Dot_Node_GraphElement, gen_Dot_DirectedArc_GraphElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)