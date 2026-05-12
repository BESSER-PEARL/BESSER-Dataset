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
xdoc_Document = Class(name="xdoc_Document")
AbstractSection = Class(name="AbstractSection")
xdoc_TextOrMarkup = Class(name="xdoc_TextOrMarkup")
xdoc_Chapter = Class(name="xdoc_Chapter")
xdoc_LangDef = Class(name="xdoc_LangDef")
xdoc_Glossary = Class(name="xdoc_Glossary")
xdoc_Part = Class(name="xdoc_Part")
xdoc_XdocFile = Class(name="xdoc_XdocFile")
xdoc_AbstractSection = Class(name="xdoc_AbstractSection")
xdoc_Section2 = Class(name="xdoc_Section2")
xdoc_SectionRef = Class(name="xdoc_SectionRef")
Section = Class(name="Section")
xdoc_Section3 = Class(name="xdoc_Section3")
xdoc_Section2Ref = Class(name="xdoc_Section2Ref")
Section2 = Class(name="Section2")
xdoc_Section4 = Class(name="xdoc_Section4")
xdoc_Section = Class(name="xdoc_Section")
xdoc_ChapterRef = Class(name="xdoc_ChapterRef")
Chapter = Class(name="Chapter")
xdoc_Identifiable = Class(name="xdoc_Identifiable")
xdoc_EObject = Class(name="xdoc_EObject")
xdoc_TextPart = Class(name="xdoc_TextPart")
xdoc_MarkUp = Class(name="xdoc_MarkUp")
xdoc_Table = Class(name="xdoc_Table")
MarkUp = Class(name="MarkUp")
xdoc_TableRow = Class(name="xdoc_TableRow")
xdoc_TableData = Class(name="xdoc_TableData")
Identifiable = Class(name="Identifiable")
xdoc_Ref = Class(name="xdoc_Ref")
xdoc_OrderedList = Class(name="xdoc_OrderedList")
xdoc_Item = Class(name="xdoc_Item")
xdoc_UnorderedList = Class(name="xdoc_UnorderedList")
xdoc_Emphasize = Class(name="xdoc_Emphasize")
MarkupInCode = Class(name="MarkupInCode")
xdoc_Anchor = Class(name="xdoc_Anchor")
xdoc_ImageRef = Class(name="xdoc_ImageRef")
xdoc_ImageProxy = Class(name="xdoc_ImageProxy")
xdoc_CodeBlock = Class(name="xdoc_CodeBlock")
xdoc_CodeRef = Class(name="xdoc_CodeRef")
xdoc_JvmDeclaredType = Class(name="xdoc_JvmDeclaredType")
xdoc_Link = Class(name="xdoc_Link")
xdoc_PartRef = Class(name="xdoc_PartRef")
Part = Class(name="Part")
xdoc_Code = Class(name="xdoc_Code")
xdoc_MarkupInCode = Class(name="xdoc_MarkupInCode")
xdoc_Todo = Class(name="xdoc_Todo")
xdoc_GlossaryEntry = Class(name="xdoc_GlossaryEntry")

# xdoc_Document class attributes and methods

# AbstractSection class attributes and methods

# xdoc_TextOrMarkup class attributes and methods

# xdoc_Chapter class attributes and methods

# xdoc_LangDef class attributes and methods
xdoc_LangDef_keywords: Property = Property(name="keywords", type=StringType)
xdoc_LangDef_name: Property = Property(name="name", type=StringType)
xdoc_LangDef.attributes={xdoc_LangDef_name, xdoc_LangDef_keywords}

# xdoc_Glossary class attributes and methods

# xdoc_Part class attributes and methods

# xdoc_XdocFile class attributes and methods

# xdoc_AbstractSection class attributes and methods

# xdoc_Section2 class attributes and methods

# xdoc_SectionRef class attributes and methods

# Section class attributes and methods

# xdoc_Section3 class attributes and methods

# xdoc_Section2Ref class attributes and methods

# Section2 class attributes and methods

# xdoc_Section4 class attributes and methods

# xdoc_Section class attributes and methods

# xdoc_ChapterRef class attributes and methods

# Chapter class attributes and methods

# xdoc_Identifiable class attributes and methods
xdoc_Identifiable_name: Property = Property(name="name", type=StringType)
xdoc_Identifiable.attributes={xdoc_Identifiable_name}

# xdoc_EObject class attributes and methods

# xdoc_TextPart class attributes and methods
xdoc_TextPart_text: Property = Property(name="text", type=StringType)
xdoc_TextPart.attributes={xdoc_TextPart_text}

# xdoc_MarkUp class attributes and methods

# xdoc_Table class attributes and methods

# MarkUp class attributes and methods

# xdoc_TableRow class attributes and methods

# xdoc_TableData class attributes and methods

# Identifiable class attributes and methods

# xdoc_Ref class attributes and methods

# xdoc_OrderedList class attributes and methods

# xdoc_Item class attributes and methods

# xdoc_UnorderedList class attributes and methods

# xdoc_Emphasize class attributes and methods

# MarkupInCode class attributes and methods

# xdoc_Anchor class attributes and methods

# xdoc_ImageRef class attributes and methods
xdoc_ImageRef_name: Property = Property(name="name", type=StringType)
xdoc_ImageRef_path: Property = Property(name="path", type=StringType)
xdoc_ImageRef_clazz: Property = Property(name="clazz", type=StringType)
xdoc_ImageRef_style: Property = Property(name="style", type=StringType)
xdoc_ImageRef_caption: Property = Property(name="caption", type=StringType)
xdoc_ImageRef.attributes={xdoc_ImageRef_style, xdoc_ImageRef_caption, xdoc_ImageRef_name, xdoc_ImageRef_path, xdoc_ImageRef_clazz}

# xdoc_ImageProxy class attributes and methods

# xdoc_CodeBlock class attributes and methods

# xdoc_CodeRef class attributes and methods

# xdoc_JvmDeclaredType class attributes and methods

# xdoc_Link class attributes and methods
xdoc_Link_url: Property = Property(name="url", type=StringType)
xdoc_Link_text: Property = Property(name="text", type=StringType)
xdoc_Link.attributes={xdoc_Link_url, xdoc_Link_text}

# xdoc_PartRef class attributes and methods

# Part class attributes and methods

# xdoc_Code class attributes and methods
xdoc_Code_contents: Property = Property(name="contents", type=StringType)
xdoc_Code.attributes={xdoc_Code_contents}

# xdoc_MarkupInCode class attributes and methods

# xdoc_Todo class attributes and methods
xdoc_Todo_text: Property = Property(name="text", type=StringType)
xdoc_Todo.attributes={xdoc_Todo_text}

# xdoc_GlossaryEntry class attributes and methods
xdoc_GlossaryEntry_name: Property = Property(name="name", type=StringType)
xdoc_GlossaryEntry_alias: Property = Property(name="alias", type=StringType)
xdoc_GlossaryEntry.attributes={xdoc_GlossaryEntry_alias, xdoc_GlossaryEntry_name}

# Relationships
subtitle1: BinaryAssociation = BinaryAssociation(
    name="subtitle1",
    ends={
        Property(name="xdoc_TextOrMarkup", type=xdoc_Document, multiplicity=Multiplicity(1, 1)),
        Property(name="xdoc_Document", type=xdoc_TextOrMarkup, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
authors2: BinaryAssociation = BinaryAssociation(
    name="authors2",
    ends={
        Property(name="xdoc_TextOrMarkup4", type=xdoc_Document, multiplicity=Multiplicity(1, 1)),
        Property(name="xdoc_Document3", type=xdoc_TextOrMarkup, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
chapters5: BinaryAssociation = BinaryAssociation(
    name="chapters5",
    ends={
        Property(name="xdoc_Chapter", type=xdoc_Document, multiplicity=Multiplicity(1, 1)),
        Property(name="xdoc_Document6", type=xdoc_Chapter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
langDefs7: BinaryAssociation = BinaryAssociation(
    name="langDefs7",
    ends={
        Property(name="xdoc_LangDef", type=xdoc_Document, multiplicity=Multiplicity(1, 1)),
        Property(name="xdoc_Document8", type=xdoc_LangDef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
glossary9: BinaryAssociation = BinaryAssociation(
    name="glossary9",
    ends={
        Property(name="xdoc_Glossary", type=xdoc_Document, multiplicity=Multiplicity(1, 1)),
        Property(name="xdoc_Document10", type=xdoc_Glossary, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parts11: BinaryAssociation = BinaryAssociation(
    name="parts11",
    ends={
        Property(name="xdoc_Part", type=xdoc_Document, multiplicity=Multiplicity(1, 1)),
        Property(name="xdoc_Document12", type=xdoc_Part, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mainSection0: BinaryAssociation = BinaryAssociation(
    name="mainSection0",
    ends={
        Property(name="xdoc_AbstractSection", type=xdoc_XdocFile, multiplicity=Multiplicity(1, 1)),
        Property(name="xdoc_XdocFile", type=xdoc_AbstractSection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subSections17: BinaryAssociation = BinaryAssociation(
    name="subSections17",
    ends={
        Property(name="xdoc_Section2", type=xdoc_Section, multiplicity=Multiplicity(1, 1)),
        Property(name="xdoc_Section18", type=xdoc_Section2, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
section19: BinaryAssociation = BinaryAssociation(
    name="section19",
    ends={
        Property(name="xdoc_Section20", type=xdoc_SectionRef, multiplicity=Multiplicity(1, 1)),
        Property(name="xdoc_SectionRef", type=xdoc_Section, multiplicity=Multiplicity(0, 1))
    }
)
subSections21: BinaryAssociation = BinaryAssociation(
    name="subSections21",
    ends={
        Property(name="xdoc_Section3", type=xdoc_Section2, multiplicity=Multiplicity(1, 1)),
        Property(name="xdoc_Section222", type=xdoc_Section3, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
section223: BinaryAssociation = BinaryAssociation(
    name="section223",
    ends={
        Property(name="xdoc_Section224", type=xdoc_Section2Ref, multiplicity=Multiplicity(1, 1)),
        Property(name="xdoc_Section2Ref", type=xdoc_Section2, multiplicity=Multiplicity(0, 1))
    }
)
subSections25: BinaryAssociation = BinaryAssociation(
    name="subSections25",
    ends={
        Property(name="xdoc_Section4", type=xdoc_Section3, multiplicity=Multiplicity(1, 1)),
        Property(name="xdoc_Section326", type=xdoc_Section4, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subSections13: BinaryAssociation = BinaryAssociation(
    name="subSections13",
    ends={
        Property(name="xdoc_Section", type=xdoc_Chapter, multiplicity=Multiplicity(1, 1)),
        Property(name="xdoc_Chapter14", type=xdoc_Section, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
chapter15: BinaryAssociation = BinaryAssociation(
    name="chapter15",
    ends={
        Property(name="xdoc_Chapter16", type=xdoc_ChapterRef, multiplicity=Multiplicity(1, 1)),
        Property(name="xdoc_ChapterRef", type=xdoc_Chapter, multiplicity=Multiplicity(0, 1))
    }
)
contents33: BinaryAssociation = BinaryAssociation(
    name="contents33",
    ends={
        Property(name="xdoc_EObject", type=xdoc_TextOrMarkup, multiplicity=Multiplicity(1, 1)),
        Property(name="xdoc_TextOrMarkup34", type=xdoc_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rows35: BinaryAssociation = BinaryAssociation(
    name="rows35",
    ends={
        Property(name="xdoc_TableRow", type=xdoc_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="xdoc_Table", type=xdoc_TableRow, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
data36: BinaryAssociation = BinaryAssociation(
    name="data36",
    ends={
        Property(name="xdoc_TableData", type=xdoc_TableRow, multiplicity=Multiplicity(1, 1)),
        Property(name="xdoc_TableRow37", type=xdoc_TableData, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contents38: BinaryAssociation = BinaryAssociation(
    name="contents38",
    ends={
        Property(name="xdoc_TextOrMarkup40", type=xdoc_TableData, multiplicity=Multiplicity(1, 1)),
        Property(name="xdoc_TableData39", type=xdoc_TextOrMarkup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
title27: BinaryAssociation = BinaryAssociation(
    name="title27",
    ends={
        Property(name="xdoc_TextOrMarkup29", type=xdoc_AbstractSection, multiplicity=Multiplicity(1, 1)),
        Property(name="xdoc_AbstractSection28", type=xdoc_TextOrMarkup, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
contents30: BinaryAssociation = BinaryAssociation(
    name="contents30",
    ends={
        Property(name="xdoc_TextOrMarkup32", type=xdoc_AbstractSection, multiplicity=Multiplicity(1, 1)),
        Property(name="xdoc_AbstractSection31", type=xdoc_TextOrMarkup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ref43: BinaryAssociation = BinaryAssociation(
    name="ref43",
    ends={
        Property(name="xdoc_Identifiable", type=xdoc_Ref, multiplicity=Multiplicity(1, 1)),
        Property(name="xdoc_Ref", type=xdoc_Identifiable, multiplicity=Multiplicity(0, 1))
    }
)
contents44: BinaryAssociation = BinaryAssociation(
    name="contents44",
    ends={
        Property(name="xdoc_TextOrMarkup46", type=xdoc_Ref, multiplicity=Multiplicity(1, 1)),
        Property(name="xdoc_Ref45", type=xdoc_TextOrMarkup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
items47: BinaryAssociation = BinaryAssociation(
    name="items47",
    ends={
        Property(name="xdoc_Item", type=xdoc_OrderedList, multiplicity=Multiplicity(1, 1)),
        Property(name="xdoc_OrderedList", type=xdoc_Item, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
items48: BinaryAssociation = BinaryAssociation(
    name="items48",
    ends={
        Property(name="xdoc_Item49", type=xdoc_UnorderedList, multiplicity=Multiplicity(1, 1)),
        Property(name="xdoc_UnorderedList", type=xdoc_Item, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contents41: BinaryAssociation = BinaryAssociation(
    name="contents41",
    ends={
        Property(name="xdoc_TextOrMarkup42", type=xdoc_Emphasize, multiplicity=Multiplicity(1, 1)),
        Property(name="xdoc_Emphasize", type=xdoc_TextOrMarkup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
image57: BinaryAssociation = BinaryAssociation(
    name="image57",
    ends={
        Property(name="xdoc_ImageProxy", type=xdoc_ImageRef, multiplicity=Multiplicity(1, 1)),
        Property(name="xdoc_ImageRef", type=xdoc_ImageProxy, multiplicity=Multiplicity(0, 1))
    }
)
contents58: BinaryAssociation = BinaryAssociation(
    name="contents58",
    ends={
        Property(name="xdoc_EObject59", type=xdoc_CodeBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="xdoc_CodeBlock", type=xdoc_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
language60: BinaryAssociation = BinaryAssociation(
    name="language60",
    ends={
        Property(name="xdoc_LangDef62", type=xdoc_CodeBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="xdoc_CodeBlock61", type=xdoc_LangDef, multiplicity=Multiplicity(0, 1))
    }
)
contents50: BinaryAssociation = BinaryAssociation(
    name="contents50",
    ends={
        Property(name="xdoc_TextOrMarkup52", type=xdoc_Item, multiplicity=Multiplicity(1, 1)),
        Property(name="xdoc_Item51", type=xdoc_TextOrMarkup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
element53: BinaryAssociation = BinaryAssociation(
    name="element53",
    ends={
        Property(name="xdoc_JvmDeclaredType", type=xdoc_CodeRef, multiplicity=Multiplicity(1, 1)),
        Property(name="xdoc_CodeRef", type=xdoc_JvmDeclaredType, multiplicity=Multiplicity(0, 1))
    }
)
altText54: BinaryAssociation = BinaryAssociation(
    name="altText54",
    ends={
        Property(name="xdoc_TextOrMarkup56", type=xdoc_CodeRef, multiplicity=Multiplicity(1, 1)),
        Property(name="xdoc_CodeRef55", type=xdoc_TextOrMarkup, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
description63: BinaryAssociation = BinaryAssociation(
    name="description63",
    ends={
        Property(name="xdoc_TextOrMarkup64", type=xdoc_GlossaryEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="xdoc_GlossaryEntry", type=xdoc_TextOrMarkup, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
glossaryEntry65: BinaryAssociation = BinaryAssociation(
    name="glossaryEntry65",
    ends={
        Property(name="xdoc_GlossaryEntry67", type=xdoc_Glossary, multiplicity=Multiplicity(1, 1)),
        Property(name="xdoc_Glossary66", type=xdoc_GlossaryEntry, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
chapters68: BinaryAssociation = BinaryAssociation(
    name="chapters68",
    ends={
        Property(name="xdoc_Chapter70", type=xdoc_Part, multiplicity=Multiplicity(1, 1)),
        Property(name="xdoc_Part69", type=xdoc_Chapter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
part71: BinaryAssociation = BinaryAssociation(
    name="part71",
    ends={
        Property(name="xdoc_Part72", type=xdoc_PartRef, multiplicity=Multiplicity(1, 1)),
        Property(name="xdoc_PartRef", type=xdoc_Part, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_xdoc_Document_AbstractSection = Generalization(general=AbstractSection, specific=xdoc_Document)
gen_xdoc_Chapter_AbstractSection = Generalization(general=AbstractSection, specific=xdoc_Chapter)
gen_xdoc_SectionRef_Section = Generalization(general=Section, specific=xdoc_SectionRef)
gen_xdoc_Section2_AbstractSection = Generalization(general=AbstractSection, specific=xdoc_Section2)
gen_xdoc_Section2Ref_Section2 = Generalization(general=Section2, specific=xdoc_Section2Ref)
gen_xdoc_Section3_AbstractSection = Generalization(general=AbstractSection, specific=xdoc_Section3)
gen_xdoc_ChapterRef_Chapter = Generalization(general=Chapter, specific=xdoc_ChapterRef)
gen_xdoc_Section_AbstractSection = Generalization(general=AbstractSection, specific=xdoc_Section)
gen_xdoc_Table_MarkUp = Generalization(general=MarkUp, specific=xdoc_Table)
gen_xdoc_Section4_AbstractSection = Generalization(general=AbstractSection, specific=xdoc_Section4)
gen_xdoc_AbstractSection_Identifiable = Generalization(general=Identifiable, specific=xdoc_AbstractSection)
gen_xdoc_Ref_MarkUp = Generalization(general=MarkUp, specific=xdoc_Ref)
gen_xdoc_Ref_MarkupInCode = Generalization(general=MarkupInCode, specific=xdoc_Ref)
gen_xdoc_OrderedList_MarkUp = Generalization(general=MarkUp, specific=xdoc_OrderedList)
gen_xdoc_UnorderedList_MarkUp = Generalization(general=MarkUp, specific=xdoc_UnorderedList)
gen_xdoc_Emphasize_MarkUp = Generalization(general=MarkUp, specific=xdoc_Emphasize)
gen_xdoc_Emphasize_MarkupInCode = Generalization(general=MarkupInCode, specific=xdoc_Emphasize)
gen_xdoc_Anchor_Identifiable = Generalization(general=Identifiable, specific=xdoc_Anchor)
gen_xdoc_Anchor_MarkUp = Generalization(general=MarkUp, specific=xdoc_Anchor)
gen_xdoc_Anchor_MarkupInCode = Generalization(general=MarkupInCode, specific=xdoc_Anchor)
gen_xdoc_ImageRef_MarkUp = Generalization(general=MarkUp, specific=xdoc_ImageRef)
gen_xdoc_CodeBlock_MarkUp = Generalization(general=MarkUp, specific=xdoc_CodeBlock)
gen_xdoc_CodeRef_MarkUp = Generalization(general=MarkUp, specific=xdoc_CodeRef)
gen_xdoc_Link_MarkUp = Generalization(general=MarkUp, specific=xdoc_Link)
gen_xdoc_Part_AbstractSection = Generalization(general=AbstractSection, specific=xdoc_Part)
gen_xdoc_PartRef_Part = Generalization(general=Part, specific=xdoc_PartRef)
gen_xdoc_Todo_MarkUp = Generalization(general=MarkUp, specific=xdoc_Todo)
gen_xdoc_Todo_MarkupInCode = Generalization(general=MarkupInCode, specific=xdoc_Todo)

# Domain Model
domain_model = DomainModel(
    name="xdoc",
    types={xdoc_Document, AbstractSection, xdoc_TextOrMarkup, xdoc_Chapter, xdoc_LangDef, xdoc_Glossary, xdoc_Part, xdoc_XdocFile, xdoc_AbstractSection, xdoc_Section2, xdoc_SectionRef, Section, xdoc_Section3, xdoc_Section2Ref, Section2, xdoc_Section4, xdoc_Section, xdoc_ChapterRef, Chapter, xdoc_Identifiable, xdoc_EObject, xdoc_TextPart, xdoc_MarkUp, xdoc_Table, MarkUp, xdoc_TableRow, xdoc_TableData, Identifiable, xdoc_Ref, xdoc_OrderedList, xdoc_Item, xdoc_UnorderedList, xdoc_Emphasize, MarkupInCode, xdoc_Anchor, xdoc_ImageRef, xdoc_ImageProxy, xdoc_CodeBlock, xdoc_CodeRef, xdoc_JvmDeclaredType, xdoc_Link, xdoc_PartRef, Part, xdoc_Code, xdoc_MarkupInCode, xdoc_Todo, xdoc_GlossaryEntry},
    associations={subtitle1, authors2, chapters5, langDefs7, glossary9, parts11, mainSection0, subSections17, section19, subSections21, section223, subSections25, subSections13, chapter15, contents33, rows35, data36, contents38, title27, contents30, ref43, contents44, items47, items48, contents41, image57, contents58, language60, contents50, element53, altText54, description63, glossaryEntry65, chapters68, part71},
    generalizations={gen_xdoc_Document_AbstractSection, gen_xdoc_Chapter_AbstractSection, gen_xdoc_SectionRef_Section, gen_xdoc_Section2_AbstractSection, gen_xdoc_Section2Ref_Section2, gen_xdoc_Section3_AbstractSection, gen_xdoc_ChapterRef_Chapter, gen_xdoc_Section_AbstractSection, gen_xdoc_Table_MarkUp, gen_xdoc_Section4_AbstractSection, gen_xdoc_AbstractSection_Identifiable, gen_xdoc_Ref_MarkUp, gen_xdoc_Ref_MarkupInCode, gen_xdoc_OrderedList_MarkUp, gen_xdoc_UnorderedList_MarkUp, gen_xdoc_Emphasize_MarkUp, gen_xdoc_Emphasize_MarkupInCode, gen_xdoc_Anchor_Identifiable, gen_xdoc_Anchor_MarkUp, gen_xdoc_Anchor_MarkupInCode, gen_xdoc_ImageRef_MarkUp, gen_xdoc_CodeBlock_MarkUp, gen_xdoc_CodeRef_MarkUp, gen_xdoc_Link_MarkUp, gen_xdoc_Part_AbstractSection, gen_xdoc_PartRef_Part, gen_xdoc_Todo_MarkUp, gen_xdoc_Todo_MarkupInCode},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)