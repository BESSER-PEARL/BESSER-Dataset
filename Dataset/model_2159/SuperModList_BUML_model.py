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
list_VersionedListVertex = Class(name="list::VersionedListVertex")
list_VersionedListEdge = Class(name="list::VersionedListEdge")
list_VersionedListStartReference = Class(name="list::VersionedListStartReference")
UUIDElement = Class(name="UUIDElement")
list_ProductSpaceElement = Class(name="list::ProductSpaceElement")
list_VersionedList = Class(name="list::VersionedList")
ProductSpaceElement = Class(name="ProductSpaceElement")

# list_VersionedListVertex class attributes and methods

# list_VersionedListEdge class attributes and methods

# list_VersionedListStartReference class attributes and methods

# UUIDElement class attributes and methods

# list_ProductSpaceElement class attributes and methods

# list_VersionedList class attributes and methods
list_VersionedList_m_linearize: Method = Method(name="linearize", parameters={}, type=ProductSpaceElement)
list_VersionedList_m_getEdge: Method = Method(name="getEdge", parameters={Parameter(name='from'), Parameter(name='to')}, type=StringType)
list_VersionedList_m_getAllOccurrencesOf: Method = Method(name="getAllOccurrencesOf", parameters={Parameter(name='element')}, type=StringType)
list_VersionedList.methods={list_VersionedList_m_getEdge, list_VersionedList_m_getAllOccurrencesOf, list_VersionedList_m_linearize}

# ProductSpaceElement class attributes and methods

# Relationships
vertices0: BinaryAssociation = BinaryAssociation(
    name="vertices0",
    ends={
        Property(name="VersionedListVertex", type=list_VersionedList, multiplicity=Multiplicity(1, 1)),
        Property(name="list", type=list_VersionedListVertex, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edges1: BinaryAssociation = BinaryAssociation(
    name="edges1",
    ends={
        Property(name="VersionedListEdge", type=list_VersionedList, multiplicity=Multiplicity(1, 1)),
        Property(name="list2", type=list_VersionedListEdge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
startVertices3: BinaryAssociation = BinaryAssociation(
    name="startVertices3",
    ends={
        Property(name="VersionedListStartReference", type=list_VersionedList, multiplicity=Multiplicity(1, 1)),
        Property(name="list4", type=list_VersionedListStartReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
element5: BinaryAssociation = BinaryAssociation(
    name="element5",
    ends={
        Property(name="list_ProductSpaceElement", type=list_VersionedListVertex, multiplicity=Multiplicity(1, 1)),
        Property(name="list_VersionedListVertex", type=list_ProductSpaceElement, multiplicity=Multiplicity(0, 1))
    }
)
incomingEdges6: BinaryAssociation = BinaryAssociation(
    name="incomingEdges6",
    ends={
        Property(name="VersionedListEdge7", type=list_VersionedListVertex, multiplicity=Multiplicity(1, 1)),
        Property(name="sink", type=list_VersionedListEdge, multiplicity=Multiplicity(0, 9999))
    }
)
outgoingEdges8: BinaryAssociation = BinaryAssociation(
    name="outgoingEdges8",
    ends={
        Property(name="VersionedListEdge9", type=list_VersionedListVertex, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=list_VersionedListEdge, multiplicity=Multiplicity(0, 9999))
    }
)
list10: BinaryAssociation = BinaryAssociation(
    name="list10",
    ends={
        Property(name="VersionedList", type=list_VersionedListVertex, multiplicity=Multiplicity(1, 1)),
        Property(name="vertices", type=list_VersionedList, multiplicity=Multiplicity(0, 1))
    }
)
startRef11: BinaryAssociation = BinaryAssociation(
    name="startRef11",
    ends={
        Property(name="VersionedListStartReference12", type=list_VersionedListVertex, multiplicity=Multiplicity(1, 1)),
        Property(name="vertex", type=list_VersionedListStartReference, multiplicity=Multiplicity(0, 1))
    }
)
source13: BinaryAssociation = BinaryAssociation(
    name="source13",
    ends={
        Property(name="VersionedListVertex14", type=list_VersionedListEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingEdges", type=list_VersionedListVertex, multiplicity=Multiplicity(0, 1))
    }
)
sink15: BinaryAssociation = BinaryAssociation(
    name="sink15",
    ends={
        Property(name="VersionedListVertex16", type=list_VersionedListEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingEdges", type=list_VersionedListVertex, multiplicity=Multiplicity(0, 1))
    }
)
list17: BinaryAssociation = BinaryAssociation(
    name="list17",
    ends={
        Property(name="VersionedList18", type=list_VersionedListEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="edges", type=list_VersionedList, multiplicity=Multiplicity(0, 1))
    }
)
vertex19: BinaryAssociation = BinaryAssociation(
    name="vertex19",
    ends={
        Property(name="VersionedListVertex20", type=list_VersionedListStartReference, multiplicity=Multiplicity(1, 1)),
        Property(name="startRef", type=list_VersionedListVertex, multiplicity=Multiplicity(0, 1))
    }
)
list21: BinaryAssociation = BinaryAssociation(
    name="list21",
    ends={
        Property(name="VersionedList22", type=list_VersionedListStartReference, multiplicity=Multiplicity(1, 1)),
        Property(name="startVertices", type=list_VersionedList, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_list_VersionedListVertex_ProductSpaceElement = Generalization(general=ProductSpaceElement, specific=list_VersionedListVertex)
gen_list_VersionedListVertex_UUIDElement = Generalization(general=UUIDElement, specific=list_VersionedListVertex)
gen_list_VersionedListEdge_ProductSpaceElement = Generalization(general=ProductSpaceElement, specific=list_VersionedListEdge)
gen_list_VersionedList_ProductSpaceElement = Generalization(general=ProductSpaceElement, specific=list_VersionedList)
gen_list_VersionedListStartReference_ProductSpaceElement = Generalization(general=ProductSpaceElement, specific=list_VersionedListStartReference)

# Domain Model
domain_model = DomainModel(
    name="list",
    types={list_VersionedListVertex, list_VersionedListEdge, list_VersionedListStartReference, UUIDElement, list_ProductSpaceElement, list_VersionedList, ProductSpaceElement},
    associations={vertices0, edges1, startVertices3, element5, incomingEdges6, outgoingEdges8, list10, startRef11, source13, sink15, list17, vertex19, list21},
    generalizations={gen_list_VersionedListVertex_ProductSpaceElement, gen_list_VersionedListVertex_UUIDElement, gen_list_VersionedListEdge_ProductSpaceElement, gen_list_VersionedList_ProductSpaceElement, gen_list_VersionedListStartReference_ProductSpaceElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)