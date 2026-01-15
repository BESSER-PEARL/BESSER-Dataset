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
Color: Enumeration = Enumeration(
    name="Color",
    literals={
            EnumerationLiteral(name="BLACK"),
			EnumerationLiteral(name="RED"),
			EnumerationLiteral(name="GREEN"),
			EnumerationLiteral(name="BLUE")
    }
)

# Classes
notation_IdElement = Class(name="notation::IdElement", is_abstract=True)
notation_NotationElement = Class(name="notation::NotationElement", is_abstract=True)
IdElement = Class(name="IdElement")
notation_GraphicalElement = Class(name="notation::GraphicalElement", is_abstract=True)
NotationElement = Class(name="NotationElement")
notation_Figure = Class(name="notation::Figure", is_abstract=True)
GraphicalElement = Class(name="GraphicalElement")
notation_Rectangle = Class(name="notation::Rectangle")
Figure = Class(name="Figure")
notation_Token = Class(name="notation::Token")
TextualElement = Class(name="TextualElement")
notation_Keyword = Class(name="notation::Keyword")
notation_Value = Class(name="notation::Value", is_abstract=True)
notation_EAttribute = Class(name="notation::EAttribute")
notation_AttributeValue = Class(name="notation::AttributeValue")
Value = Class(name="Value")
notation_ReferenceValue = Class(name="notation::ReferenceValue")
notation_EReference = Class(name="notation::EReference")
notation_SyntaxOf = Class(name="notation::SyntaxOf")
notation_Composite = Class(name="notation::Composite")
notation_Definition = Class(name="notation::Definition")
notation_Line = Class(name="notation::Line")
notation_Label = Class(name="notation::Label")
notation_TextualElement = Class(name="notation::TextualElement")

# notation_IdElement class attributes and methods
notation_IdElement_id: Property = Property(name="id", type=StringType)
notation_IdElement.attributes={notation_IdElement_id}

# notation_NotationElement class attributes and methods

# IdElement class attributes and methods

# notation_GraphicalElement class attributes and methods
notation_GraphicalElement_x: Property = Property(name="x", type=IntegerType)
notation_GraphicalElement_y: Property = Property(name="y", type=IntegerType)
notation_GraphicalElement_height: Property = Property(name="height", type=IntegerType)
notation_GraphicalElement_width: Property = Property(name="width", type=IntegerType)
notation_GraphicalElement_fill: Property = Property(name="fill", type=StringType)
notation_GraphicalElement_stroke: Property = Property(name="stroke", type=StringType)
notation_GraphicalElement.attributes={notation_GraphicalElement_width, notation_GraphicalElement_y, notation_GraphicalElement_stroke, notation_GraphicalElement_fill, notation_GraphicalElement_x, notation_GraphicalElement_height}

# NotationElement class attributes and methods

# notation_Figure class attributes and methods

# GraphicalElement class attributes and methods

# notation_Rectangle class attributes and methods

# Figure class attributes and methods

# notation_Token class attributes and methods

# TextualElement class attributes and methods

# notation_Keyword class attributes and methods

# notation_Value class attributes and methods
notation_Value_separator: Property = Property(name="separator", type=StringType)
notation_Value.attributes={notation_Value_separator}

# notation_EAttribute class attributes and methods

# notation_AttributeValue class attributes and methods

# Value class attributes and methods

# notation_ReferenceValue class attributes and methods

# notation_EReference class attributes and methods

# notation_SyntaxOf class attributes and methods

# notation_Composite class attributes and methods

# notation_Definition class attributes and methods

# notation_Line class attributes and methods

# notation_Label class attributes and methods

# notation_TextualElement class attributes and methods
notation_TextualElement_fill: Property = Property(name="fill", type=StringType)
notation_TextualElement.attributes={notation_TextualElement_fill}

# Relationships
attribute1: BinaryAssociation = BinaryAssociation(
    name="attribute1",
    ends={
        Property(name="notation_EAttribute", type=notation_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="notation_Value", type=notation_EAttribute, multiplicity=Multiplicity(1, 1))
    }
)
reference2: BinaryAssociation = BinaryAssociation(
    name="reference2",
    ends={
        Property(name="notation_EReference", type=notation_ReferenceValue, multiplicity=Multiplicity(1, 1)),
        Property(name="notation_ReferenceValue", type=notation_EReference, multiplicity=Multiplicity(1, 1))
    }
)
reference3: BinaryAssociation = BinaryAssociation(
    name="reference3",
    ends={
        Property(name="notation_EReference4", type=notation_SyntaxOf, multiplicity=Multiplicity(1, 1)),
        Property(name="notation_SyntaxOf", type=notation_EReference, multiplicity=Multiplicity(1, 1))
    }
)
separator5: BinaryAssociation = BinaryAssociation(
    name="separator5",
    ends={
        Property(name="notation_NotationElement", type=notation_SyntaxOf, multiplicity=Multiplicity(1, 1)),
        Property(name="notation_SyntaxOf6", type=notation_NotationElement, multiplicity=Multiplicity(0, 1))
    }
)
subElements7: BinaryAssociation = BinaryAssociation(
    name="subElements7",
    ends={
        Property(name="notation_NotationElement8", type=notation_Composite, multiplicity=Multiplicity(1, 1)),
        Property(name="notation_Composite", type=notation_NotationElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements9: BinaryAssociation = BinaryAssociation(
    name="elements9",
    ends={
        Property(name="notation_NotationElement10", type=notation_Definition, multiplicity=Multiplicity(1, 1)),
        Property(name="notation_Definition", type=notation_NotationElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
text0: BinaryAssociation = BinaryAssociation(
    name="text0",
    ends={
        Property(name="notation_TextualElement", type=notation_Label, multiplicity=Multiplicity(1, 1)),
        Property(name="notation_Label", type=notation_TextualElement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_notation_NotationElement_IdElement = Generalization(general=IdElement, specific=notation_NotationElement)
gen_notation_GraphicalElement_NotationElement = Generalization(general=NotationElement, specific=notation_GraphicalElement)
gen_notation_Figure_GraphicalElement = Generalization(general=GraphicalElement, specific=notation_Figure)
gen_notation_Rectangle_Figure = Generalization(general=Figure, specific=notation_Rectangle)
gen_notation_Token_TextualElement = Generalization(general=TextualElement, specific=notation_Token)
gen_notation_Keyword_TextualElement = Generalization(general=TextualElement, specific=notation_Keyword)
gen_notation_Value_TextualElement = Generalization(general=TextualElement, specific=notation_Value)
gen_notation_AttributeValue_Value = Generalization(general=Value, specific=notation_AttributeValue)
gen_notation_ReferenceValue_Value = Generalization(general=Value, specific=notation_ReferenceValue)
gen_notation_SyntaxOf_NotationElement = Generalization(general=NotationElement, specific=notation_SyntaxOf)
gen_notation_Composite_NotationElement = Generalization(general=NotationElement, specific=notation_Composite)
gen_notation_Line_GraphicalElement = Generalization(general=GraphicalElement, specific=notation_Line)
gen_notation_Label_GraphicalElement = Generalization(general=GraphicalElement, specific=notation_Label)
gen_notation_TextualElement_NotationElement = Generalization(general=NotationElement, specific=notation_TextualElement)

# Domain Model
domain_model = DomainModel(
    name="notation",
    types={notation_IdElement, notation_NotationElement, IdElement, notation_GraphicalElement, NotationElement, notation_Figure, GraphicalElement, notation_Rectangle, Figure, notation_Token, TextualElement, notation_Keyword, notation_Value, notation_EAttribute, notation_AttributeValue, Value, notation_ReferenceValue, notation_EReference, notation_SyntaxOf, notation_Composite, notation_Definition, notation_Line, notation_Label, notation_TextualElement, Color},
    associations={attribute1, reference2, reference3, separator5, subElements7, elements9, text0},
    generalizations={gen_notation_NotationElement_IdElement, gen_notation_GraphicalElement_NotationElement, gen_notation_Figure_GraphicalElement, gen_notation_Rectangle_Figure, gen_notation_Token_TextualElement, gen_notation_Keyword_TextualElement, gen_notation_Value_TextualElement, gen_notation_AttributeValue_Value, gen_notation_ReferenceValue_Value, gen_notation_SyntaxOf_NotationElement, gen_notation_Composite_NotationElement, gen_notation_Line_GraphicalElement, gen_notation_Label_GraphicalElement, gen_notation_TextualElement_NotationElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)