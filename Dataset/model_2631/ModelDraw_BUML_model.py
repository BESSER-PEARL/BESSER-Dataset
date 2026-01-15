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
DrawType: Enumeration = Enumeration(
    name="DrawType",
    literals={
            EnumerationLiteral(name="diagram")
    }
)

NodeType: Enumeration = Enumeration(
    name="NodeType",
    literals={
            EnumerationLiteral(name="node"),
			EnumerationLiteral(name="markednode")
    }
)

NodeShape: Enumeration = Enumeration(
    name="NodeShape",
    literals={
            EnumerationLiteral(name="circle"),
			EnumerationLiteral(name="doublecircle"),
			EnumerationLiteral(name="record")
    }
)

NodeColor: Enumeration = Enumeration(
    name="NodeColor",
    literals={
            EnumerationLiteral(name="gray95")
    }
)

Decoration: Enumeration = Enumeration(
    name="Decoration",
    literals={
            EnumerationLiteral(name="none"),
			EnumerationLiteral(name="triangle"),
			EnumerationLiteral(name="diamond"),
			EnumerationLiteral(name="odiamond"),
			EnumerationLiteral(name="open"),
			EnumerationLiteral(name="empty")
    }
)

NodeStyle: Enumeration = Enumeration(
    name="NodeStyle",
    literals={
            EnumerationLiteral(name="none"),
			EnumerationLiteral(name="italic"),
			EnumerationLiteral(name="underline")
    }
)

# Classes
modeldraw_Content = Class(name="modeldraw::Content")
modeldraw_NamedItem = Class(name="modeldraw::NamedItem", is_abstract=True)
modeldraw_Item = Class(name="modeldraw::Item", is_abstract=True)
modeldraw_EClass = Class(name="modeldraw::EClass")
modeldraw_MutatorDraw = Class(name="modeldraw::MutatorDraw")
Item = Class(name="Item")
modeldraw_Node = Class(name="modeldraw::Node")
modeldraw_Relation = Class(name="modeldraw::Relation", is_abstract=True)
modeldraw_EEnumLiteral = Class(name="modeldraw::EEnumLiteral")
modeldraw_EAttribute = Class(name="modeldraw::EAttribute")
modeldraw_BooleanAttribute = Class(name="modeldraw::BooleanAttribute")
NamedItem = Class(name="NamedItem")
modeldraw_EReference = Class(name="modeldraw::EReference")
modeldraw_Edge = Class(name="modeldraw::Edge")
Relation = Class(name="Relation")
modeldraw_Level = Class(name="modeldraw::Level")
modeldraw_NodeEnumerator = Class(name="modeldraw::NodeEnumerator")
modeldraw_Enumerator = Class(name="modeldraw::Enumerator")
modeldraw_Information = Class(name="modeldraw::Information")

# modeldraw_Content class attributes and methods
modeldraw_Content_symbol: Property = Property(name="symbol", type=StringType)
modeldraw_Content.attributes={modeldraw_Content_symbol}

# modeldraw_NamedItem class attributes and methods

# modeldraw_Item class attributes and methods

# modeldraw_EClass class attributes and methods

# modeldraw_MutatorDraw class attributes and methods
modeldraw_MutatorDraw_metamodel: Property = Property(name="metamodel", type=StringType)
modeldraw_MutatorDraw_type: Property = Property(name="type", type=StringType)
modeldraw_MutatorDraw.attributes={modeldraw_MutatorDraw_type, modeldraw_MutatorDraw_metamodel}

# Item class attributes and methods

# modeldraw_Node class attributes and methods
modeldraw_Node_type: Property = Property(name="type", type=StringType)
modeldraw_Node_shape: Property = Property(name="shape", type=StringType)
modeldraw_Node_color: Property = Property(name="color", type=StringType)
modeldraw_Node_style: Property = Property(name="style", type=StringType)
modeldraw_Node.attributes={modeldraw_Node_shape, modeldraw_Node_style, modeldraw_Node_type, modeldraw_Node_color}

# modeldraw_Relation class attributes and methods
modeldraw_Relation_src_decoration: Property = Property(name="src_decoration", type=StringType)
modeldraw_Relation_tar_decoration: Property = Property(name="tar_decoration", type=StringType)
modeldraw_Relation.attributes={modeldraw_Relation_src_decoration, modeldraw_Relation_tar_decoration}

# modeldraw_EEnumLiteral class attributes and methods

# modeldraw_EAttribute class attributes and methods

# modeldraw_BooleanAttribute class attributes and methods
modeldraw_BooleanAttribute_negation: Property = Property(name="negation", type=BooleanType)
modeldraw_BooleanAttribute.attributes={modeldraw_BooleanAttribute_negation}

# NamedItem class attributes and methods

# modeldraw_EReference class attributes and methods

# modeldraw_Edge class attributes and methods

# Relation class attributes and methods

# modeldraw_Level class attributes and methods

# modeldraw_NodeEnumerator class attributes and methods

# modeldraw_Enumerator class attributes and methods
modeldraw_Enumerator_value: Property = Property(name="value", type=StringType)
modeldraw_Enumerator.attributes={modeldraw_Enumerator_value}

# modeldraw_Information class attributes and methods

# Relationships
contents4: BinaryAssociation = BinaryAssociation(
    name="contents4",
    ends={
        Property(name="modeldraw_Content", type=modeldraw_MutatorDraw, multiplicity=Multiplicity(1, 1)),
        Property(name="modeldraw_MutatorDraw5", type=modeldraw_Content, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name0: BinaryAssociation = BinaryAssociation(
    name="name0",
    ends={
        Property(name="modeldraw_EClass", type=modeldraw_Item, multiplicity=Multiplicity(1, 1)),
        Property(name="modeldraw_Item", type=modeldraw_EClass, multiplicity=Multiplicity(0, 1))
    }
)
nodes1: BinaryAssociation = BinaryAssociation(
    name="nodes1",
    ends={
        Property(name="modeldraw_Node", type=modeldraw_MutatorDraw, multiplicity=Multiplicity(1, 1)),
        Property(name="modeldraw_MutatorDraw", type=modeldraw_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relations2: BinaryAssociation = BinaryAssociation(
    name="relations2",
    ends={
        Property(name="modeldraw_Relation", type=modeldraw_MutatorDraw, multiplicity=Multiplicity(1, 1)),
        Property(name="modeldraw_MutatorDraw3", type=modeldraw_Relation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enumerator35: BinaryAssociation = BinaryAssociation(
    name="enumerator35",
    ends={
        Property(name="modeldraw_NodeEnumerator36", type=modeldraw_Enumerator, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="modeldraw_Enumerator", type=modeldraw_NodeEnumerator, multiplicity=Multiplicity(1, 1))
    }
)
literal37: BinaryAssociation = BinaryAssociation(
    name="literal37",
    ends={
        Property(name="modeldraw_EEnumLiteral", type=modeldraw_Enumerator, multiplicity=Multiplicity(1, 1)),
        Property(name="modeldraw_Enumerator38", type=modeldraw_EEnumLiteral, multiplicity=Multiplicity(1, 1))
    }
)
attName6: BinaryAssociation = BinaryAssociation(
    name="attName6",
    ends={
        Property(name="modeldraw_EAttribute", type=modeldraw_NamedItem, multiplicity=Multiplicity(1, 1)),
        Property(name="modeldraw_NamedItem", type=modeldraw_EAttribute, multiplicity=Multiplicity(0, 1))
    }
)
att7: BinaryAssociation = BinaryAssociation(
    name="att7",
    ends={
        Property(name="modeldraw_EAttribute8", type=modeldraw_BooleanAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="modeldraw_BooleanAttribute", type=modeldraw_EAttribute, multiplicity=Multiplicity(1, 1))
    }
)
attribute9: BinaryAssociation = BinaryAssociation(
    name="attribute9",
    ends={
        Property(name="modeldraw_BooleanAttribute11", type=modeldraw_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="modeldraw_Node10", type=modeldraw_BooleanAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reference12: BinaryAssociation = BinaryAssociation(
    name="reference12",
    ends={
        Property(name="modeldraw_EReference", type=modeldraw_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="modeldraw_Node13", type=modeldraw_EReference, multiplicity=Multiplicity(0, 9999))
    }
)
reference14: BinaryAssociation = BinaryAssociation(
    name="reference14",
    ends={
        Property(name="modeldraw_EReference16", type=modeldraw_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="modeldraw_Relation15", type=modeldraw_EReference, multiplicity=Multiplicity(0, 1))
    }
)
label17: BinaryAssociation = BinaryAssociation(
    name="label17",
    ends={
        Property(name="modeldraw_EAttribute19", type=modeldraw_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="modeldraw_Relation18", type=modeldraw_EAttribute, multiplicity=Multiplicity(0, 1))
    }
)
src_label20: BinaryAssociation = BinaryAssociation(
    name="src_label20",
    ends={
        Property(name="modeldraw_EAttribute22", type=modeldraw_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="modeldraw_Relation21", type=modeldraw_EAttribute, multiplicity=Multiplicity(0, 1))
    }
)
tar_label23: BinaryAssociation = BinaryAssociation(
    name="tar_label23",
    ends={
        Property(name="modeldraw_EAttribute25", type=modeldraw_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="modeldraw_Relation24", type=modeldraw_EAttribute, multiplicity=Multiplicity(0, 1))
    }
)
source26: BinaryAssociation = BinaryAssociation(
    name="source26",
    ends={
        Property(name="modeldraw_EReference27", type=modeldraw_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="modeldraw_Edge", type=modeldraw_EReference, multiplicity=Multiplicity(0, 1))
    }
)
target28: BinaryAssociation = BinaryAssociation(
    name="target28",
    ends={
        Property(name="modeldraw_EReference30", type=modeldraw_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="modeldraw_Edge29", type=modeldraw_EReference, multiplicity=Multiplicity(0, 1))
    }
)
upper31: BinaryAssociation = BinaryAssociation(
    name="upper31",
    ends={
        Property(name="modeldraw_EReference32", type=modeldraw_Level, multiplicity=Multiplicity(1, 1)),
        Property(name="modeldraw_Level", type=modeldraw_EReference, multiplicity=Multiplicity(0, 1))
    }
)
att33: BinaryAssociation = BinaryAssociation(
    name="att33",
    ends={
        Property(name="modeldraw_EAttribute34", type=modeldraw_NodeEnumerator, multiplicity=Multiplicity(1, 1)),
        Property(name="modeldraw_NodeEnumerator", type=modeldraw_EAttribute, multiplicity=Multiplicity(1, 1))
    }
)
type39: BinaryAssociation = BinaryAssociation(
    name="type39",
    ends={
        Property(name="modeldraw_EReference40", type=modeldraw_Information, multiplicity=Multiplicity(1, 1)),
        Property(name="modeldraw_Information", type=modeldraw_EReference, multiplicity=Multiplicity(1, 1))
    }
)
att41: BinaryAssociation = BinaryAssociation(
    name="att41",
    ends={
        Property(name="modeldraw_EAttribute43", type=modeldraw_Information, multiplicity=Multiplicity(1, 1)),
        Property(name="modeldraw_Information42", type=modeldraw_EAttribute, multiplicity=Multiplicity(0, 1))
    }
)
nodenum44: BinaryAssociation = BinaryAssociation(
    name="nodenum44",
    ends={
        Property(name="modeldraw_NodeEnumerator46", type=modeldraw_Content, multiplicity=Multiplicity(1, 1)),
        Property(name="modeldraw_Content45", type=modeldraw_NodeEnumerator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
info47: BinaryAssociation = BinaryAssociation(
    name="info47",
    ends={
        Property(name="modeldraw_Information49", type=modeldraw_Content, multiplicity=Multiplicity(1, 1)),
        Property(name="modeldraw_Content48", type=modeldraw_Information, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_modeldraw_NamedItem_Item = Generalization(general=Item, specific=modeldraw_NamedItem)
gen_modeldraw_MutatorDraw_Item = Generalization(general=Item, specific=modeldraw_MutatorDraw)
gen_modeldraw_BooleanAttribute_Item = Generalization(general=Item, specific=modeldraw_BooleanAttribute)
gen_modeldraw_Node_NamedItem = Generalization(general=NamedItem, specific=modeldraw_Node)
gen_modeldraw_Relation_NamedItem = Generalization(general=NamedItem, specific=modeldraw_Relation)
gen_modeldraw_Edge_Relation = Generalization(general=Relation, specific=modeldraw_Edge)
gen_modeldraw_Level_Relation = Generalization(general=Relation, specific=modeldraw_Level)
gen_modeldraw_NodeEnumerator_Item = Generalization(general=Item, specific=modeldraw_NodeEnumerator)
gen_modeldraw_Information_Item = Generalization(general=Item, specific=modeldraw_Information)
gen_modeldraw_Content_NamedItem = Generalization(general=NamedItem, specific=modeldraw_Content)

# Domain Model
domain_model = DomainModel(
    name="modeldraw",
    types={modeldraw_Content, modeldraw_NamedItem, modeldraw_Item, modeldraw_EClass, modeldraw_MutatorDraw, Item, modeldraw_Node, modeldraw_Relation, modeldraw_EEnumLiteral, modeldraw_EAttribute, modeldraw_BooleanAttribute, NamedItem, modeldraw_EReference, modeldraw_Edge, Relation, modeldraw_Level, modeldraw_NodeEnumerator, modeldraw_Enumerator, modeldraw_Information, DrawType, NodeType, NodeShape, NodeColor, Decoration, NodeStyle},
    associations={contents4, name0, nodes1, relations2, enumerator35, literal37, attName6, att7, attribute9, reference12, reference14, label17, src_label20, tar_label23, source26, target28, upper31, att33, type39, att41, nodenum44, info47},
    generalizations={gen_modeldraw_NamedItem_Item, gen_modeldraw_MutatorDraw_Item, gen_modeldraw_BooleanAttribute_Item, gen_modeldraw_Node_NamedItem, gen_modeldraw_Relation_NamedItem, gen_modeldraw_Edge_Relation, gen_modeldraw_Level_Relation, gen_modeldraw_NodeEnumerator_Item, gen_modeldraw_Information_Item, gen_modeldraw_Content_NamedItem},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)