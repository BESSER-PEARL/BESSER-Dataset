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
Elements_IdentifiedElement = Class(name="Elements::IdentifiedElement", is_abstract=True)
Elements_Element = Class(name="Elements::Element")
NamedElement = Class(name="NamedElement")
Elements_NamedElement = Class(name="Elements::NamedElement", is_abstract=True)
IdentifiedElement = Class(name="IdentifiedElement")
Elements_Root = Class(name="Elements::Root")
Elements_Node = Class(name="Elements::Node")
Elements_Edge = Class(name="Elements::Edge")
Elements_StrictElement = Class(name="Elements::StrictElement")
Element = Class(name="Element")
Elements_ReferencingNode = Class(name="Elements::ReferencingNode")
Node = Class(name="Node")

# Elements_IdentifiedElement class attributes and methods
Elements_IdentifiedElement_id: Property = Property(name="id", type=StringType)
Elements_IdentifiedElement.attributes={Elements_IdentifiedElement_id}

# Elements_Element class attributes and methods
Elements_Element_value: Property = Property(name="value", type=IntegerType)
Elements_Element_values: Property = Property(name="values", type=IntegerType)
Elements_Element.attributes={Elements_Element_values, Elements_Element_value}

# NamedElement class attributes and methods

# Elements_NamedElement class attributes and methods
Elements_NamedElement_name: Property = Property(name="name", type=StringType)
Elements_NamedElement.attributes={Elements_NamedElement_name}

# IdentifiedElement class attributes and methods

# Elements_Root class attributes and methods
Elements_Root_name: Property = Property(name="name", type=StringType)
Elements_Root.attributes={Elements_Root_name}

# Elements_Node class attributes and methods

# Elements_Edge class attributes and methods

# Elements_StrictElement class attributes and methods
Elements_StrictElement_sValue: Property = Property(name="sValue", type=IntegerType)
Elements_StrictElement_sValues: Property = Property(name="sValues", type=IntegerType)
Elements_StrictElement.attributes={Elements_StrictElement_sValues, Elements_StrictElement_sValue}

# Element class attributes and methods

# Elements_ReferencingNode class attributes and methods

# Node class attributes and methods

# Relationships
content0: BinaryAssociation = BinaryAssociation(
    name="content0",
    ends={
        Property(name="Elements_NamedElement", type=Elements_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="Elements_Root", type=Elements_NamedElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
manyContent2: BinaryAssociation = BinaryAssociation(
    name="manyContent2",
    ends={
        Property(name="Elements_Element", type=Elements_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="Elements_Element1", type=Elements_Element, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
singleContent4: BinaryAssociation = BinaryAssociation(
    name="singleContent4",
    ends={
        Property(name="Elements_Element5", type=Elements_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="Elements_Element3", type=Elements_Element, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
manyContentWithUp7: BinaryAssociation = BinaryAssociation(
    name="manyContentWithUp7",
    ends={
        Property(name="Element", type=Elements_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="upFromManyContent", type=Elements_Element, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
upFromManyContent9: BinaryAssociation = BinaryAssociation(
    name="upFromManyContent9",
    ends={
        Property(name="Element10", type=Elements_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="manyContentWithUp", type=Elements_Element, multiplicity=Multiplicity(0, 1))
    }
)
singleContentWithUp12: BinaryAssociation = BinaryAssociation(
    name="singleContentWithUp12",
    ends={
        Property(name="Element13", type=Elements_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="upFromSingleContent", type=Elements_Element, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
upFromSingleContent15: BinaryAssociation = BinaryAssociation(
    name="upFromSingleContent15",
    ends={
        Property(name="Element16", type=Elements_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="singleContentWithUp", type=Elements_Element, multiplicity=Multiplicity(0, 1))
    }
)
manyRef18: BinaryAssociation = BinaryAssociation(
    name="manyRef18",
    ends={
        Property(name="Elements_Element19", type=Elements_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="Elements_Element17", type=Elements_Element, multiplicity=Multiplicity(0, 9999))
    }
)
singleRef21: BinaryAssociation = BinaryAssociation(
    name="singleRef21",
    ends={
        Property(name="Elements_Element22", type=Elements_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="Elements_Element20", type=Elements_Element, multiplicity=Multiplicity(0, 1))
    }
)
singleFromSingleRef124: BinaryAssociation = BinaryAssociation(
    name="singleFromSingleRef124",
    ends={
        Property(name="Element25", type=Elements_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="singleFromSingleRef2", type=Elements_Element, multiplicity=Multiplicity(0, 1))
    }
)
singleFromSingleRef227: BinaryAssociation = BinaryAssociation(
    name="singleFromSingleRef227",
    ends={
        Property(name="Element28", type=Elements_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="singleFromSingleRef1", type=Elements_Element, multiplicity=Multiplicity(0, 1))
    }
)
manyFromSingleRef30: BinaryAssociation = BinaryAssociation(
    name="manyFromSingleRef30",
    ends={
        Property(name="Element31", type=Elements_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="singleFromManyRef", type=Elements_Element, multiplicity=Multiplicity(0, 9999))
    }
)
singleFromManyRef33: BinaryAssociation = BinaryAssociation(
    name="singleFromManyRef33",
    ends={
        Property(name="Element34", type=Elements_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="manyFromSingleRef", type=Elements_Element, multiplicity=Multiplicity(0, 1))
    }
)
manyFromManyRef136: BinaryAssociation = BinaryAssociation(
    name="manyFromManyRef136",
    ends={
        Property(name="Element37", type=Elements_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="manyFromManyRef2", type=Elements_Element, multiplicity=Multiplicity(0, 9999))
    }
)
manyFromManyRef239: BinaryAssociation = BinaryAssociation(
    name="manyFromManyRef239",
    ends={
        Property(name="Element40", type=Elements_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="manyFromManyRef1", type=Elements_Element, multiplicity=Multiplicity(0, 9999))
    }
)
sSingleContent43: BinaryAssociation = BinaryAssociation(
    name="sSingleContent43",
    ends={
        Property(name="Elements_StrictElement44", type=Elements_Element, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Elements_Element45", type=Elements_StrictElement, multiplicity=Multiplicity(1, 1))
    }
)
sManyRef46: BinaryAssociation = BinaryAssociation(
    name="sManyRef46",
    ends={
        Property(name="Elements_Element48", type=Elements_StrictElement, multiplicity=Multiplicity(1, 1)),
        Property(name="Elements_StrictElement47", type=Elements_Element, multiplicity=Multiplicity(1, 9999))
    }
)
sSingleRef49: BinaryAssociation = BinaryAssociation(
    name="sSingleRef49",
    ends={
        Property(name="Elements_Element51", type=Elements_StrictElement, multiplicity=Multiplicity(1, 1)),
        Property(name="Elements_StrictElement50", type=Elements_Element, multiplicity=Multiplicity(1, 1))
    }
)
sManyFromSingleRef53: BinaryAssociation = BinaryAssociation(
    name="sManyFromSingleRef53",
    ends={
        Property(name="StrictElement", type=Elements_StrictElement, multiplicity=Multiplicity(1, 1)),
        Property(name="sSingleFromManyRef", type=Elements_StrictElement, multiplicity=Multiplicity(1, 9999))
    }
)
sSingleFromManyRef55: BinaryAssociation = BinaryAssociation(
    name="sSingleFromManyRef55",
    ends={
        Property(name="StrictElement56", type=Elements_StrictElement, multiplicity=Multiplicity(1, 1)),
        Property(name="sManyFromSingleRef", type=Elements_StrictElement, multiplicity=Multiplicity(1, 1))
    }
)
sManyFromManyRef158: BinaryAssociation = BinaryAssociation(
    name="sManyFromManyRef158",
    ends={
        Property(name="StrictElement59", type=Elements_StrictElement, multiplicity=Multiplicity(1, 1)),
        Property(name="sManyFromManyRef2", type=Elements_StrictElement, multiplicity=Multiplicity(1, 9999))
    }
)
sManyFromManyRef261: BinaryAssociation = BinaryAssociation(
    name="sManyFromManyRef261",
    ends={
        Property(name="StrictElement62", type=Elements_StrictElement, multiplicity=Multiplicity(1, 1)),
        Property(name="sManyFromManyRef1", type=Elements_StrictElement, multiplicity=Multiplicity(1, 9999))
    }
)
incoming63: BinaryAssociation = BinaryAssociation(
    name="incoming63",
    ends={
        Property(name="Edge", type=Elements_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=Elements_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing64: BinaryAssociation = BinaryAssociation(
    name="outgoing64",
    ends={
        Property(name="Edge65", type=Elements_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=Elements_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
subNodes66: BinaryAssociation = BinaryAssociation(
    name="subNodes66",
    ends={
        Property(name="Elements_NamedElement67", type=Elements_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="Elements_Node", type=Elements_NamedElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target68: BinaryAssociation = BinaryAssociation(
    name="target68",
    ends={
        Property(name="Node", type=Elements_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=Elements_Node, multiplicity=Multiplicity(1, 1))
    }
)
sManyContent41: BinaryAssociation = BinaryAssociation(
    name="sManyContent41",
    ends={
        Property(name="Elements_Element42", type=Elements_StrictElement, multiplicity=Multiplicity(1, 1)),
        Property(name="Elements_StrictElement", type=Elements_Element, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
source69: BinaryAssociation = BinaryAssociation(
    name="source69",
    ends={
        Property(name="Node70", type=Elements_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=Elements_Node, multiplicity=Multiplicity(1, 1))
    }
)
referenced71: BinaryAssociation = BinaryAssociation(
    name="referenced71",
    ends={
        Property(name="Elements_Node72", type=Elements_ReferencingNode, multiplicity=Multiplicity(1, 1)),
        Property(name="Elements_ReferencingNode", type=Elements_Node, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_Elements_Element_NamedElement = Generalization(general=NamedElement, specific=Elements_Element)
gen_Elements_NamedElement_IdentifiedElement = Generalization(general=IdentifiedElement, specific=Elements_NamedElement)
gen_Elements_Root_IdentifiedElement = Generalization(general=IdentifiedElement, specific=Elements_Root)
gen_Elements_Node_NamedElement = Generalization(general=NamedElement, specific=Elements_Node)
gen_Elements_Edge_NamedElement = Generalization(general=NamedElement, specific=Elements_Edge)
gen_Elements_StrictElement_Element = Generalization(general=Element, specific=Elements_StrictElement)
gen_Elements_ReferencingNode_Node = Generalization(general=Node, specific=Elements_ReferencingNode)

# Domain Model
domain_model = DomainModel(
    name="Elements",
    types={Elements_IdentifiedElement, Elements_Element, NamedElement, Elements_NamedElement, IdentifiedElement, Elements_Root, Elements_Node, Elements_Edge, Elements_StrictElement, Element, Elements_ReferencingNode, Node},
    associations={content0, manyContent2, singleContent4, manyContentWithUp7, upFromManyContent9, singleContentWithUp12, upFromSingleContent15, manyRef18, singleRef21, singleFromSingleRef124, singleFromSingleRef227, manyFromSingleRef30, singleFromManyRef33, manyFromManyRef136, manyFromManyRef239, sSingleContent43, sManyRef46, sSingleRef49, sManyFromSingleRef53, sSingleFromManyRef55, sManyFromManyRef158, sManyFromManyRef261, incoming63, outgoing64, subNodes66, target68, sManyContent41, source69, referenced71},
    generalizations={gen_Elements_Element_NamedElement, gen_Elements_NamedElement_IdentifiedElement, gen_Elements_Root_IdentifiedElement, gen_Elements_Node_NamedElement, gen_Elements_Edge_NamedElement, gen_Elements_StrictElement_Element, gen_Elements_ReferencingNode_Node},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)