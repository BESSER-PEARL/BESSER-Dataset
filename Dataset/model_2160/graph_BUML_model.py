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
Colors: Enumeration = Enumeration(
    name="Colors",
    literals={
            EnumerationLiteral(name="clean"),
			EnumerationLiteral(name="touched"),
			EnumerationLiteral(name="performed")
    }
)

# Classes
egt_Vertex = Class(name="egt::Vertex")
egt_Edge = Class(name="egt::Edge")
egt_ColorRegistry = Class(name="egt::ColorRegistry")
egt_DiEdge = Class(name="egt::DiEdge")
Edge = Class(name="Edge")
egt_GraphModel = Class(name="egt::GraphModel")
egt_SingleEdge = Class(name="egt::SingleEdge")

# egt_Vertex class attributes and methods
egt_Vertex_index: Property = Property(name="index", type=IntegerType)
egt_Vertex_name: Property = Property(name="name", type=StringType)
egt_Vertex_color: Property = Property(name="color", type=StringType)
egt_Vertex.attributes={egt_Vertex_color, egt_Vertex_name, egt_Vertex_index}

# egt_Edge class attributes and methods
egt_Edge_weight: Property = Property(name="weight", type=FloatType)
egt_Edge_color: Property = Property(name="color", type=StringType)
egt_Edge.attributes={egt_Edge_color, egt_Edge_weight}

# egt_ColorRegistry class attributes and methods
egt_ColorRegistry_images: Property = Property(name="images", type=StringType)
egt_ColorRegistry_m_init: Method = Method(name="init", parameters={})
egt_ColorRegistry_m_dispose: Method = Method(name="dispose", parameters={})
egt_ColorRegistry.attributes={egt_ColorRegistry_images}
egt_ColorRegistry.methods={egt_ColorRegistry_m_dispose, egt_ColorRegistry_m_init}

# egt_DiEdge class attributes and methods

# Edge class attributes and methods

# egt_GraphModel class attributes and methods

# egt_SingleEdge class attributes and methods

# Relationships
edges0: BinaryAssociation = BinaryAssociation(
    name="edges0",
    ends={
        Property(name="egt_Edge", type=egt_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="egt_Vertex", type=egt_Edge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentVertex1: BinaryAssociation = BinaryAssociation(
    name="parentVertex1",
    ends={
        Property(name="egt_Vertex3", type=egt_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="egt_Edge2", type=egt_Vertex, multiplicity=Multiplicity(0, 1))
    }
)
vertexes4: BinaryAssociation = BinaryAssociation(
    name="vertexes4",
    ends={
        Property(name="egt_Vertex5", type=egt_GraphModel, multiplicity=Multiplicity(1, 1)),
        Property(name="egt_GraphModel", type=egt_Vertex, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
colorRegistry6: BinaryAssociation = BinaryAssociation(
    name="colorRegistry6",
    ends={
        Property(name="egt_ColorRegistry", type=egt_GraphModel, multiplicity=Multiplicity(1, 1)),
        Property(name="egt_GraphModel7", type=egt_ColorRegistry, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
child9: BinaryAssociation = BinaryAssociation(
    name="child9",
    ends={
        Property(name="egt_SingleEdge", type=egt_SingleEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="egt_SingleEdge8", type=egt_SingleEdge, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_egt_DiEdge_Edge = Generalization(general=Edge, specific=egt_DiEdge)
gen_egt_SingleEdge_Edge = Generalization(general=Edge, specific=egt_SingleEdge)

# Domain Model
domain_model = DomainModel(
    name="egt",
    types={egt_Vertex, egt_Edge, egt_ColorRegistry, egt_DiEdge, Edge, egt_GraphModel, egt_SingleEdge, Colors},
    associations={edges0, parentVertex1, vertexes4, colorRegistry6, child9},
    generalizations={gen_egt_DiEdge_Edge, gen_egt_SingleEdge_Edge},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)