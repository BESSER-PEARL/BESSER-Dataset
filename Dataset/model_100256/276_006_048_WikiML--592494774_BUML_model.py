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
ViewType: Enumeration = Enumeration(
    name="ViewType",
    literals={
            EnumerationLiteral(name="thumb")
    }
)

HorizontalAlign: Enumeration = Enumeration(
    name="HorizontalAlign",
    literals={
            EnumerationLiteral(name="right")
    }
)

# Classes
wikiML_ParagraphTypes = Class(name="wikiML_ParagraphTypes")
wikiML_BlockQuote = Class(name="wikiML_BlockQuote")
ParagraphTypes = Class(name="ParagraphTypes")
wikiML_AnyTextSequence = Class(name="wikiML_AnyTextSequence")
wikiML_Template = Class(name="wikiML_Template")
wikiML_AboutTemplate = Class(name="wikiML_AboutTemplate")
Template = Class(name="Template")
wikiML_MainTemplate = Class(name="wikiML_MainTemplate")
wikiML_WikiPage = Class(name="wikiML_WikiPage")
wikiML_Image = Class(name="wikiML_Image")
wikiML_AbstractUnformattedInlineContent = Class(name="wikiML_AbstractUnformattedInlineContent")
wikiML_Category = Class(name="wikiML_Category")
wikiML_Text = Class(name="wikiML_Text")
wikiML_QuoteTemplate = Class(name="wikiML_QuoteTemplate")
wikiML_OrderedList = Class(name="wikiML_OrderedList")
wikiML_OrderListItem = Class(name="wikiML_OrderListItem")
wikiML_Paragraph = Class(name="wikiML_Paragraph")
wikiML_UnorderedList = Class(name="wikiML_UnorderedList")
wikiML_UnorderListItem = Class(name="wikiML_UnorderListItem")
wikiML_Bold = Class(name="wikiML_Bold")
AbstractFormattedInlineContent = Class(name="AbstractFormattedInlineContent")
wikiML_Italic = Class(name="wikiML_Italic")
wikiML_ItalicBold = Class(name="wikiML_ItalicBold")
AbstractUnformattedInlineContent = Class(name="AbstractUnformattedInlineContent")
wikiML_HyperLink = Class(name="wikiML_HyperLink")
wikiML_AnyText = Class(name="wikiML_AnyText")
wikiML_Internal = Class(name="wikiML_Internal")
HyperLink = Class(name="HyperLink")
wikiML_External = Class(name="wikiML_External")
wikiML_Heading2 = Class(name="wikiML_Heading2")
wikiML_Heading3 = Class(name="wikiML_Heading3")
wikiML_Heading4 = Class(name="wikiML_Heading4")
wikiML_Heading5 = Class(name="wikiML_Heading5")
wikiML_AbstractFormattedInlineContent = Class(name="wikiML_AbstractFormattedInlineContent")
AnyText = Class(name="AnyText")

# wikiML_ParagraphTypes class attributes and methods

# wikiML_BlockQuote class attributes and methods

# ParagraphTypes class attributes and methods

# wikiML_AnyTextSequence class attributes and methods

# wikiML_Template class attributes and methods
wikiML_Template_type: Property = Property(name="type", type=StringType)
wikiML_Template.attributes={wikiML_Template_type}

# wikiML_AboutTemplate class attributes and methods

# Template class attributes and methods

# wikiML_MainTemplate class attributes and methods

# wikiML_WikiPage class attributes and methods
wikiML_WikiPage_name: Property = Property(name="name", type=StringType)
wikiML_WikiPage.attributes={wikiML_WikiPage_name}

# wikiML_Image class attributes and methods
wikiML_Image_name: Property = Property(name="name", type=StringType)
wikiML_Image_type: Property = Property(name="type", type=StringType)
wikiML_Image_hAlign: Property = Property(name="hAlign", type=StringType)
wikiML_Image.attributes={wikiML_Image_type, wikiML_Image_hAlign, wikiML_Image_name}

# wikiML_AbstractUnformattedInlineContent class attributes and methods

# wikiML_Category class attributes and methods
wikiML_Category_value: Property = Property(name="value", type=StringType)
wikiML_Category.attributes={wikiML_Category_value}

# wikiML_Text class attributes and methods
wikiML_Text_name: Property = Property(name="name", type=StringType)
wikiML_Text.attributes={wikiML_Text_name}

# wikiML_QuoteTemplate class attributes and methods

# wikiML_OrderedList class attributes and methods

# wikiML_OrderListItem class attributes and methods

# wikiML_Paragraph class attributes and methods
wikiML_Paragraph_paragraph: Property = Property(name="paragraph", type=StringType)
wikiML_Paragraph.attributes={wikiML_Paragraph_paragraph}

# wikiML_UnorderedList class attributes and methods

# wikiML_UnorderListItem class attributes and methods
wikiML_UnorderListItem_level: Property = Property(name="level", type=StringType)
wikiML_UnorderListItem.attributes={wikiML_UnorderListItem_level}

# wikiML_Bold class attributes and methods

# AbstractFormattedInlineContent class attributes and methods

# wikiML_Italic class attributes and methods

# wikiML_ItalicBold class attributes and methods

# AbstractUnformattedInlineContent class attributes and methods

# wikiML_HyperLink class attributes and methods

# wikiML_AnyText class attributes and methods

# wikiML_Internal class attributes and methods

# HyperLink class attributes and methods

# wikiML_External class attributes and methods
wikiML_External_name: Property = Property(name="name", type=StringType)
wikiML_External.attributes={wikiML_External_name}

# wikiML_Heading2 class attributes and methods

# wikiML_Heading3 class attributes and methods

# wikiML_Heading4 class attributes and methods

# wikiML_Heading5 class attributes and methods

# wikiML_AbstractFormattedInlineContent class attributes and methods

# AnyText class attributes and methods

# Relationships
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="wikiML_ParagraphTypes", type=wikiML_WikiPage, multiplicity=Multiplicity(1, 1)),
        Property(name="wikiML_WikiPage", type=wikiML_ParagraphTypes, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
content1: BinaryAssociation = BinaryAssociation(
    name="content1",
    ends={
        Property(name="wikiML_AnyTextSequence", type=wikiML_BlockQuote, multiplicity=Multiplicity(1, 1)),
        Property(name="wikiML_BlockQuote", type=wikiML_AnyTextSequence, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
content2: BinaryAssociation = BinaryAssociation(
    name="content2",
    ends={
        Property(name="wikiML_AnyTextSequence3", type=wikiML_AboutTemplate, multiplicity=Multiplicity(1, 1)),
        Property(name="wikiML_AboutTemplate", type=wikiML_AnyTextSequence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
content4: BinaryAssociation = BinaryAssociation(
    name="content4",
    ends={
        Property(name="wikiML_AnyTextSequence5", type=wikiML_MainTemplate, multiplicity=Multiplicity(1, 1)),
        Property(name="wikiML_MainTemplate", type=wikiML_AnyTextSequence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
itemtext16: BinaryAssociation = BinaryAssociation(
    name="itemtext16",
    ends={
        Property(name="wikiML_AnyTextSequence18", type=wikiML_OrderListItem, multiplicity=Multiplicity(1, 1)),
        Property(name="wikiML_OrderListItem17", type=wikiML_AnyTextSequence, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
altText19: BinaryAssociation = BinaryAssociation(
    name="altText19",
    ends={
        Property(name="wikiML_AbstractUnformattedInlineContent", type=wikiML_Image, multiplicity=Multiplicity(1, 1)),
        Property(name="wikiML_Image", type=wikiML_AbstractUnformattedInlineContent, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
caption20: BinaryAssociation = BinaryAssociation(
    name="caption20",
    ends={
        Property(name="wikiML_AnyTextSequence22", type=wikiML_Image, multiplicity=Multiplicity(1, 1)),
        Property(name="wikiML_Image21", type=wikiML_AnyTextSequence, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name23: BinaryAssociation = BinaryAssociation(
    name="name23",
    ends={
        Property(name="wikiML_Text", type=wikiML_Category, multiplicity=Multiplicity(1, 1)),
        Property(name="wikiML_Category", type=wikiML_Text, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
items6: BinaryAssociation = BinaryAssociation(
    name="items6",
    ends={
        Property(name="wikiML_OrderListItem", type=wikiML_OrderedList, multiplicity=Multiplicity(1, 1)),
        Property(name="wikiML_OrderedList", type=wikiML_OrderListItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
end7: BinaryAssociation = BinaryAssociation(
    name="end7",
    ends={
        Property(name="wikiML_Paragraph", type=wikiML_OrderedList, multiplicity=Multiplicity(1, 1)),
        Property(name="wikiML_OrderedList8", type=wikiML_Paragraph, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
items9: BinaryAssociation = BinaryAssociation(
    name="items9",
    ends={
        Property(name="wikiML_UnorderListItem", type=wikiML_UnorderedList, multiplicity=Multiplicity(1, 1)),
        Property(name="wikiML_UnorderedList", type=wikiML_UnorderListItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
end10: BinaryAssociation = BinaryAssociation(
    name="end10",
    ends={
        Property(name="wikiML_Paragraph12", type=wikiML_UnorderedList, multiplicity=Multiplicity(1, 1)),
        Property(name="wikiML_UnorderedList11", type=wikiML_Paragraph, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
itemtext13: BinaryAssociation = BinaryAssociation(
    name="itemtext13",
    ends={
        Property(name="wikiML_AnyTextSequence15", type=wikiML_UnorderListItem, multiplicity=Multiplicity(1, 1)),
        Property(name="wikiML_UnorderListItem14", type=wikiML_AnyTextSequence, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
altText34: BinaryAssociation = BinaryAssociation(
    name="altText34",
    ends={
        Property(name="wikiML_AnyText", type=wikiML_HyperLink, multiplicity=Multiplicity(1, 1)),
        Property(name="wikiML_HyperLink", type=wikiML_AnyText, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
link35: BinaryAssociation = BinaryAssociation(
    name="link35",
    ends={
        Property(name="wikiML_WikiPage36", type=wikiML_Internal, multiplicity=Multiplicity(1, 1)),
        Property(name="wikiML_Internal", type=wikiML_WikiPage, multiplicity=Multiplicity(0, 1))
    }
)
anchor37: BinaryAssociation = BinaryAssociation(
    name="anchor37",
    ends={
        Property(name="wikiML_Text39", type=wikiML_Internal, multiplicity=Multiplicity(1, 1)),
        Property(name="wikiML_Internal38", type=wikiML_Text, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
headingValue224: BinaryAssociation = BinaryAssociation(
    name="headingValue224",
    ends={
        Property(name="wikiML_AbstractUnformattedInlineContent25", type=wikiML_Heading2, multiplicity=Multiplicity(1, 1)),
        Property(name="wikiML_Heading2", type=wikiML_AbstractUnformattedInlineContent, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
headingValue326: BinaryAssociation = BinaryAssociation(
    name="headingValue326",
    ends={
        Property(name="wikiML_AbstractUnformattedInlineContent27", type=wikiML_Heading3, multiplicity=Multiplicity(1, 1)),
        Property(name="wikiML_Heading3", type=wikiML_AbstractUnformattedInlineContent, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
headingValue428: BinaryAssociation = BinaryAssociation(
    name="headingValue428",
    ends={
        Property(name="wikiML_AbstractUnformattedInlineContent29", type=wikiML_Heading4, multiplicity=Multiplicity(1, 1)),
        Property(name="wikiML_Heading4", type=wikiML_AbstractUnformattedInlineContent, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
headingValue530: BinaryAssociation = BinaryAssociation(
    name="headingValue530",
    ends={
        Property(name="wikiML_AbstractUnformattedInlineContent31", type=wikiML_Heading5, multiplicity=Multiplicity(1, 1)),
        Property(name="wikiML_Heading5", type=wikiML_AbstractUnformattedInlineContent, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name32: BinaryAssociation = BinaryAssociation(
    name="name32",
    ends={
        Property(name="wikiML_AbstractUnformattedInlineContent33", type=wikiML_AbstractFormattedInlineContent, multiplicity=Multiplicity(1, 1)),
        Property(name="wikiML_AbstractFormattedInlineContent", type=wikiML_AbstractUnformattedInlineContent, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
content40: BinaryAssociation = BinaryAssociation(
    name="content40",
    ends={
        Property(name="wikiML_AnyText42", type=wikiML_AnyTextSequence, multiplicity=Multiplicity(1, 1)),
        Property(name="wikiML_AnyTextSequence41", type=wikiML_AnyText, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_wikiML_BlockQuote_ParagraphTypes = Generalization(general=ParagraphTypes, specific=wikiML_BlockQuote)
gen_wikiML_Template_ParagraphTypes = Generalization(general=ParagraphTypes, specific=wikiML_Template)
gen_wikiML_AboutTemplate_Template = Generalization(general=Template, specific=wikiML_AboutTemplate)
gen_wikiML_MainTemplate_Template = Generalization(general=Template, specific=wikiML_MainTemplate)
gen_wikiML_Image_ParagraphTypes = Generalization(general=ParagraphTypes, specific=wikiML_Image)
gen_wikiML_Category_ParagraphTypes = Generalization(general=ParagraphTypes, specific=wikiML_Category)
gen_wikiML_QuoteTemplate_Template = Generalization(general=Template, specific=wikiML_QuoteTemplate)
gen_wikiML_OrderedList_ParagraphTypes = Generalization(general=ParagraphTypes, specific=wikiML_OrderedList)
gen_wikiML_UnorderedList_ParagraphTypes = Generalization(general=ParagraphTypes, specific=wikiML_UnorderedList)
gen_wikiML_Bold_AbstractFormattedInlineContent = Generalization(general=AbstractFormattedInlineContent, specific=wikiML_Bold)
gen_wikiML_Italic_AbstractFormattedInlineContent = Generalization(general=AbstractFormattedInlineContent, specific=wikiML_Italic)
gen_wikiML_ItalicBold_AbstractFormattedInlineContent = Generalization(general=AbstractFormattedInlineContent, specific=wikiML_ItalicBold)
gen_wikiML_AbstractUnformattedInlineContent_AnyText = Generalization(general=AnyText, specific=wikiML_AbstractUnformattedInlineContent)
gen_wikiML_Text_AbstractUnformattedInlineContent = Generalization(general=AbstractUnformattedInlineContent, specific=wikiML_Text)
gen_wikiML_HyperLink_AbstractUnformattedInlineContent = Generalization(general=AbstractUnformattedInlineContent, specific=wikiML_HyperLink)
gen_wikiML_Internal_HyperLink = Generalization(general=HyperLink, specific=wikiML_Internal)
gen_wikiML_External_HyperLink = Generalization(general=HyperLink, specific=wikiML_External)
gen_wikiML_Heading2_ParagraphTypes = Generalization(general=ParagraphTypes, specific=wikiML_Heading2)
gen_wikiML_Heading3_ParagraphTypes = Generalization(general=ParagraphTypes, specific=wikiML_Heading3)
gen_wikiML_Heading4_ParagraphTypes = Generalization(general=ParagraphTypes, specific=wikiML_Heading4)
gen_wikiML_Heading5_ParagraphTypes = Generalization(general=ParagraphTypes, specific=wikiML_Heading5)
gen_wikiML_AbstractFormattedInlineContent_AnyText = Generalization(general=AnyText, specific=wikiML_AbstractFormattedInlineContent)
gen_wikiML_AnyText_ParagraphTypes = Generalization(general=ParagraphTypes, specific=wikiML_AnyText)
gen_wikiML_Paragraph_ParagraphTypes = Generalization(general=ParagraphTypes, specific=wikiML_Paragraph)

# Domain Model
domain_model = DomainModel(
    name="wikiML",
    types={wikiML_ParagraphTypes, wikiML_BlockQuote, ParagraphTypes, wikiML_AnyTextSequence, wikiML_Template, wikiML_AboutTemplate, Template, wikiML_MainTemplate, wikiML_WikiPage, wikiML_Image, wikiML_AbstractUnformattedInlineContent, wikiML_Category, wikiML_Text, wikiML_QuoteTemplate, wikiML_OrderedList, wikiML_OrderListItem, wikiML_Paragraph, wikiML_UnorderedList, wikiML_UnorderListItem, wikiML_Bold, AbstractFormattedInlineContent, wikiML_Italic, wikiML_ItalicBold, AbstractUnformattedInlineContent, wikiML_HyperLink, wikiML_AnyText, wikiML_Internal, HyperLink, wikiML_External, wikiML_Heading2, wikiML_Heading3, wikiML_Heading4, wikiML_Heading5, wikiML_AbstractFormattedInlineContent, AnyText, ViewType, HorizontalAlign},
    associations={elements0, content1, content2, content4, itemtext16, altText19, caption20, name23, items6, end7, items9, end10, itemtext13, altText34, link35, anchor37, headingValue224, headingValue326, headingValue428, headingValue530, name32, content40},
    generalizations={gen_wikiML_BlockQuote_ParagraphTypes, gen_wikiML_Template_ParagraphTypes, gen_wikiML_AboutTemplate_Template, gen_wikiML_MainTemplate_Template, gen_wikiML_Image_ParagraphTypes, gen_wikiML_Category_ParagraphTypes, gen_wikiML_QuoteTemplate_Template, gen_wikiML_OrderedList_ParagraphTypes, gen_wikiML_UnorderedList_ParagraphTypes, gen_wikiML_Bold_AbstractFormattedInlineContent, gen_wikiML_Italic_AbstractFormattedInlineContent, gen_wikiML_ItalicBold_AbstractFormattedInlineContent, gen_wikiML_AbstractUnformattedInlineContent_AnyText, gen_wikiML_Text_AbstractUnformattedInlineContent, gen_wikiML_HyperLink_AbstractUnformattedInlineContent, gen_wikiML_Internal_HyperLink, gen_wikiML_External_HyperLink, gen_wikiML_Heading2_ParagraphTypes, gen_wikiML_Heading3_ParagraphTypes, gen_wikiML_Heading4_ParagraphTypes, gen_wikiML_Heading5_ParagraphTypes, gen_wikiML_AbstractFormattedInlineContent_AnyText, gen_wikiML_AnyText_ParagraphTypes, gen_wikiML_Paragraph_ParagraphTypes},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)