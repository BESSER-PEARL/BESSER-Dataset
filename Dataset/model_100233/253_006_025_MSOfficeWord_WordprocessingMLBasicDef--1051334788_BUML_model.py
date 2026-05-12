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
BreakType: Enumeration = Enumeration(
    name="BreakType",
    literals={
            EnumerationLiteral(name="bt_page"),
			EnumerationLiteral(name="bt_column"),
			EnumerationLiteral(name="bt_text_wrapping")
    }
)

NoteValue: Enumeration = Enumeration(
    name="NoteValue",
    literals={
            EnumerationLiteral(name="ftn_normal"),
			EnumerationLiteral(name="ftn_separator"),
			EnumerationLiteral(name="ftn_continuation_separator"),
			EnumerationLiteral(name="ftn_continuation_notice")
    }
)

OnOffType: Enumeration = Enumeration(
    name="OnOffType",
    literals={
            EnumerationLiteral(name="oot_on"),
			EnumerationLiteral(name="oot_off")
    }
)

FldCharTypeProperty: Enumeration = Enumeration(
    name="FldCharTypeProperty",
    literals={
            EnumerationLiteral(name="fctp_end"),
			EnumerationLiteral(name="fctp_begin"),
			EnumerationLiteral(name="fctp_separate")
    }
)

# Classes
WordprocessingMLBasicDef_VersionType = Class(name="WordprocessingMLBasicDef_VersionType")
WordprocessingMLBasicDef_DateTimeType = Class(name="WordprocessingMLBasicDef_DateTimeType")
WordprocessingMLBasicDef_DocumentPropertiesCollection = Class(name="WordprocessingMLBasicDef_DocumentPropertiesCollection")
WordDocument = Class(name="WordDocument")
WordprocessingMLBasicDef_ValueType = Class(name="WordprocessingMLBasicDef_ValueType", is_abstract=True)
WordprocessingMLBasicDef_StringValue = Class(name="WordprocessingMLBasicDef_StringValue")
ValueType = Class(name="ValueType")
WordprocessingMLBasicDef_FloatValue = Class(name="WordprocessingMLBasicDef_FloatValue")
WordprocessingMLBasicDef_DateTimeTypeValue = Class(name="WordprocessingMLBasicDef_DateTimeTypeValue")
DateTimeType = Class(name="DateTimeType")
WordprocessingMLBasicDef_BooleanValue = Class(name="WordprocessingMLBasicDef_BooleanValue")
VersionType = Class(name="VersionType")
CustomDocumentProperty = Class(name="CustomDocumentProperty")
WordprocessingMLBasicDef_CustomDocumentProperty = Class(name="WordprocessingMLBasicDef_CustomDocumentProperty")
WordprocessingMLBasicDef_CustomDocumentPropertiesCollection = Class(name="WordprocessingMLBasicDef_CustomDocumentPropertiesCollection")
WordprocessingMLBasicDef_SmartTagsCollection = Class(name="WordprocessingMLBasicDef_SmartTagsCollection")
CustomDocumentPropertiesCollection = Class(name="CustomDocumentPropertiesCollection")
WordprocessingMLBasicDef_SmartTagType = Class(name="WordprocessingMLBasicDef_SmartTagType")
SmartTagsCollection = Class(name="SmartTagsCollection")
WordprocessingMLBasicDef_StringProperty = Class(name="WordprocessingMLBasicDef_StringProperty")
StringType = Class(name="StringType")
WordprocessingMLBasicDef_StringType = Class(name="WordprocessingMLBasicDef_StringType")
SmartTagType = Class(name="SmartTagType")
WordprocessingMLBasicDef_WordDocument = Class(name="WordprocessingMLBasicDef_WordDocument")
DocumentPropertiesCollection = Class(name="DocumentPropertiesCollection")
ListsElt = Class(name="ListsElt")
StylesElt = Class(name="StylesElt")
DocPrElt = Class(name="DocPrElt")
BodyElt = Class(name="BodyElt")
StringProperty = Class(name="StringProperty")
WordprocessingMLBasicDef_DocPrElt = Class(name="WordprocessingMLBasicDef_DocPrElt")
FontsListElt = Class(name="FontsListElt")
BlockLevelElt = Class(name="BlockLevelElt")
SectPrElt = Class(name="SectPrElt")
WordprocessingMLBasicDef_BlockLevelElt = Class(name="WordprocessingMLBasicDef_BlockLevelElt", is_abstract=True)
NoteElt = Class(name="NoteElt")
WordprocessingMLBasicDef_BlockLevelChunkElt = Class(name="WordprocessingMLBasicDef_BlockLevelChunkElt", is_abstract=True)
WordprocessingMLBasicDef_BodyElt = Class(name="WordprocessingMLBasicDef_BodyElt")
ParaContentElt = Class(name="ParaContentElt")
WordprocessingMLBasicDef_ParaPrElt = Class(name="WordprocessingMLBasicDef_ParaPrElt")
ParaElt = Class(name="ParaElt")
WordprocessingMLBasicDef_ParaContentElt = Class(name="WordprocessingMLBasicDef_ParaContentElt", is_abstract=True)
WordprocessingMLBasicDef_RunElt = Class(name="WordprocessingMLBasicDef_RunElt")
RunPrElt = Class(name="RunPrElt")
WordprocessingMLBasicDef_ParaElt = Class(name="WordprocessingMLBasicDef_ParaElt")
BlockLevelChunkElt = Class(name="BlockLevelChunkElt")
ParaPrElt = Class(name="ParaPrElt")
WordprocessingMLBasicDef_RunPrElt = Class(name="WordprocessingMLBasicDef_RunPrElt")
RunElt = Class(name="RunElt")
WordprocessingMLBasicDef_RunContentElt = Class(name="WordprocessingMLBasicDef_RunContentElt", is_abstract=True)
WordprocessingMLBasicDef_BreakElt = Class(name="WordprocessingMLBasicDef_BreakElt")
WordprocessingMLBasicDef_Text = Class(name="WordprocessingMLBasicDef_Text")
WordprocessingMLBasicDef_DelText = Class(name="WordprocessingMLBasicDef_DelText")
RunContentElt = Class(name="RunContentElt")
WordprocessingMLBasicDef_NoBreakHyphen = Class(name="WordprocessingMLBasicDef_NoBreakHyphen")
WordprocessingMLBasicDef_SoftHyphen = Class(name="WordprocessingMLBasicDef_SoftHyphen")
WordprocessingMLBasicDef_AnnotationRef = Class(name="WordprocessingMLBasicDef_AnnotationRef")
WordprocessingMLBasicDef_FootnoteRef = Class(name="WordprocessingMLBasicDef_FootnoteRef")
WordprocessingMLBasicDef_EndnoteRef = Class(name="WordprocessingMLBasicDef_EndnoteRef")
WordprocessingMLBasicDef_Separator = Class(name="WordprocessingMLBasicDef_Separator")
WordprocessingMLBasicDef_ContinuationSeparator = Class(name="WordprocessingMLBasicDef_ContinuationSeparator")
WordprocessingMLBasicDef_PgNum = Class(name="WordprocessingMLBasicDef_PgNum")
WordprocessingMLBasicDef_Cr = Class(name="WordprocessingMLBasicDef_Cr")
WordprocessingMLBasicDef_Footnote = Class(name="WordprocessingMLBasicDef_Footnote")
WordprocessingMLBasicDef_InstrText = Class(name="WordprocessingMLBasicDef_InstrText")
WordprocessingMLBasicDef_DelInstrText = Class(name="WordprocessingMLBasicDef_DelInstrText")
WordprocessingMLBasicDef_Picture = Class(name="WordprocessingMLBasicDef_Picture")
PictureType = Class(name="PictureType")
WordprocessingMLBasicDef_Symbol = Class(name="WordprocessingMLBasicDef_Symbol")
SymElt = Class(name="SymElt")
WordprocessingMLBasicDef_SymElt = Class(name="WordprocessingMLBasicDef_SymElt")
WordprocessingMLBasicDef_Endnote = Class(name="WordprocessingMLBasicDef_Endnote")
WordprocessingMLBasicDef_NoteElt = Class(name="WordprocessingMLBasicDef_NoteElt", is_abstract=True)
WordprocessingMLBasicDef_FldChar = Class(name="WordprocessingMLBasicDef_FldChar")
WordprocessingMLBasicDef_SectPrElt = Class(name="WordprocessingMLBasicDef_SectPrElt")
FldCharElt = Class(name="FldCharElt")
WordprocessingMLBasicDef_FldCharElt = Class(name="WordprocessingMLBasicDef_FldCharElt")
WordprocessingMLBasicDef_FontsListElt = Class(name="WordprocessingMLBasicDef_FontsListElt")
WordprocessingMLBasicDef_ListsElt = Class(name="WordprocessingMLBasicDef_ListsElt")
WordprocessingMLBasicDef_StylesElt = Class(name="WordprocessingMLBasicDef_StylesElt")
WordprocessingMLBasicDef_Tab = Class(name="WordprocessingMLBasicDef_Tab")
TabElt = Class(name="TabElt")
WordprocessingMLBasicDef_RunLevelElt = Class(name="WordprocessingMLBasicDef_RunLevelElt")
WordprocessingMLBasicDef_CfChunk = Class(name="WordprocessingMLBasicDef_CfChunk")
WordprocessingMLBasicDef_SimpleFieldElt = Class(name="WordprocessingMLBasicDef_SimpleFieldElt")
WordprocessingMLBasicDef_HLinkElt = Class(name="WordprocessingMLBasicDef_HLinkElt")
WordprocessingMLBasicDef_SubDocElt = Class(name="WordprocessingMLBasicDef_SubDocElt")
WordprocessingMLBasicDef_PictureType = Class(name="WordprocessingMLBasicDef_PictureType")
WordprocessingMLBasicDef_TabElt = Class(name="WordprocessingMLBasicDef_TabElt")

# WordprocessingMLBasicDef_VersionType class attributes and methods
WordprocessingMLBasicDef_VersionType_n: Property = Property(name="n", type=StringType)
WordprocessingMLBasicDef_VersionType_nn: Property = Property(name="nn", type=StringType)
WordprocessingMLBasicDef_VersionType.attributes={WordprocessingMLBasicDef_VersionType_nn, WordprocessingMLBasicDef_VersionType_n}

# WordprocessingMLBasicDef_DateTimeType class attributes and methods
WordprocessingMLBasicDef_DateTimeType_year: Property = Property(name="year", type=StringType)
WordprocessingMLBasicDef_DateTimeType_month: Property = Property(name="month", type=StringType)
WordprocessingMLBasicDef_DateTimeType_day: Property = Property(name="day", type=StringType)
WordprocessingMLBasicDef_DateTimeType_hour: Property = Property(name="hour", type=StringType)
WordprocessingMLBasicDef_DateTimeType_minute: Property = Property(name="minute", type=StringType)
WordprocessingMLBasicDef_DateTimeType_second: Property = Property(name="second", type=StringType)
WordprocessingMLBasicDef_DateTimeType.attributes={WordprocessingMLBasicDef_DateTimeType_hour, WordprocessingMLBasicDef_DateTimeType_day, WordprocessingMLBasicDef_DateTimeType_second, WordprocessingMLBasicDef_DateTimeType_minute, WordprocessingMLBasicDef_DateTimeType_year, WordprocessingMLBasicDef_DateTimeType_month}

# WordprocessingMLBasicDef_DocumentPropertiesCollection class attributes and methods
WordprocessingMLBasicDef_DocumentPropertiesCollection_title: Property = Property(name="title", type=StringType)
WordprocessingMLBasicDef_DocumentPropertiesCollection_subject: Property = Property(name="subject", type=StringType)
WordprocessingMLBasicDef_DocumentPropertiesCollection_keywords: Property = Property(name="keywords", type=StringType)
WordprocessingMLBasicDef_DocumentPropertiesCollection_description: Property = Property(name="description", type=StringType)
WordprocessingMLBasicDef_DocumentPropertiesCollection_category: Property = Property(name="category", type=StringType)
WordprocessingMLBasicDef_DocumentPropertiesCollection_presentationFormat: Property = Property(name="presentationFormat", type=StringType)
WordprocessingMLBasicDef_DocumentPropertiesCollection_guid: Property = Property(name="guid", type=StringType)
WordprocessingMLBasicDef_DocumentPropertiesCollection_appName: Property = Property(name="appName", type=StringType)
WordprocessingMLBasicDef_DocumentPropertiesCollection_totalTime: Property = Property(name="totalTime", type=StringType)
WordprocessingMLBasicDef_DocumentPropertiesCollection_author: Property = Property(name="author", type=StringType)
WordprocessingMLBasicDef_DocumentPropertiesCollection_lastAuthor: Property = Property(name="lastAuthor", type=StringType)
WordprocessingMLBasicDef_DocumentPropertiesCollection_manager: Property = Property(name="manager", type=StringType)
WordprocessingMLBasicDef_DocumentPropertiesCollection_company: Property = Property(name="company", type=StringType)
WordprocessingMLBasicDef_DocumentPropertiesCollection_hyperlinkBase: Property = Property(name="hyperlinkBase", type=StringType)
WordprocessingMLBasicDef_DocumentPropertiesCollection_revision: Property = Property(name="revision", type=StringType)
WordprocessingMLBasicDef_DocumentPropertiesCollection_pages: Property = Property(name="pages", type=StringType)
WordprocessingMLBasicDef_DocumentPropertiesCollection_words: Property = Property(name="words", type=StringType)
WordprocessingMLBasicDef_DocumentPropertiesCollection_characters: Property = Property(name="characters", type=StringType)
WordprocessingMLBasicDef_DocumentPropertiesCollection_charactersWithSpaces: Property = Property(name="charactersWithSpaces", type=StringType)
WordprocessingMLBasicDef_DocumentPropertiesCollection_bytes: Property = Property(name="bytes", type=StringType)
WordprocessingMLBasicDef_DocumentPropertiesCollection_lines: Property = Property(name="lines", type=StringType)
WordprocessingMLBasicDef_DocumentPropertiesCollection_paragraphs: Property = Property(name="paragraphs", type=StringType)
WordprocessingMLBasicDef_DocumentPropertiesCollection.attributes={WordprocessingMLBasicDef_DocumentPropertiesCollection_hyperlinkBase, WordprocessingMLBasicDef_DocumentPropertiesCollection_totalTime, WordprocessingMLBasicDef_DocumentPropertiesCollection_revision, WordprocessingMLBasicDef_DocumentPropertiesCollection_lines, WordprocessingMLBasicDef_DocumentPropertiesCollection_manager, WordprocessingMLBasicDef_DocumentPropertiesCollection_words, WordprocessingMLBasicDef_DocumentPropertiesCollection_characters, WordprocessingMLBasicDef_DocumentPropertiesCollection_subject, WordprocessingMLBasicDef_DocumentPropertiesCollection_appName, WordprocessingMLBasicDef_DocumentPropertiesCollection_title, WordprocessingMLBasicDef_DocumentPropertiesCollection_charactersWithSpaces, WordprocessingMLBasicDef_DocumentPropertiesCollection_keywords, WordprocessingMLBasicDef_DocumentPropertiesCollection_presentationFormat, WordprocessingMLBasicDef_DocumentPropertiesCollection_guid, WordprocessingMLBasicDef_DocumentPropertiesCollection_lastAuthor, WordprocessingMLBasicDef_DocumentPropertiesCollection_description, WordprocessingMLBasicDef_DocumentPropertiesCollection_company, WordprocessingMLBasicDef_DocumentPropertiesCollection_bytes, WordprocessingMLBasicDef_DocumentPropertiesCollection_pages, WordprocessingMLBasicDef_DocumentPropertiesCollection_category, WordprocessingMLBasicDef_DocumentPropertiesCollection_paragraphs, WordprocessingMLBasicDef_DocumentPropertiesCollection_author}

# WordDocument class attributes and methods

# WordprocessingMLBasicDef_ValueType class attributes and methods

# WordprocessingMLBasicDef_StringValue class attributes and methods
WordprocessingMLBasicDef_StringValue_value: Property = Property(name="value", type=StringType)
WordprocessingMLBasicDef_StringValue.attributes={WordprocessingMLBasicDef_StringValue_value}

# ValueType class attributes and methods

# WordprocessingMLBasicDef_FloatValue class attributes and methods
WordprocessingMLBasicDef_FloatValue_value: Property = Property(name="value", type=StringType)
WordprocessingMLBasicDef_FloatValue.attributes={WordprocessingMLBasicDef_FloatValue_value}

# WordprocessingMLBasicDef_DateTimeTypeValue class attributes and methods

# DateTimeType class attributes and methods

# WordprocessingMLBasicDef_BooleanValue class attributes and methods
WordprocessingMLBasicDef_BooleanValue_value: Property = Property(name="value", type=StringType)
WordprocessingMLBasicDef_BooleanValue.attributes={WordprocessingMLBasicDef_BooleanValue_value}

# VersionType class attributes and methods

# CustomDocumentProperty class attributes and methods

# WordprocessingMLBasicDef_CustomDocumentProperty class attributes and methods
WordprocessingMLBasicDef_CustomDocumentProperty_name: Property = Property(name="name", type=StringType)
WordprocessingMLBasicDef_CustomDocumentProperty.attributes={WordprocessingMLBasicDef_CustomDocumentProperty_name}

# WordprocessingMLBasicDef_CustomDocumentPropertiesCollection class attributes and methods

# WordprocessingMLBasicDef_SmartTagsCollection class attributes and methods

# CustomDocumentPropertiesCollection class attributes and methods

# WordprocessingMLBasicDef_SmartTagType class attributes and methods
WordprocessingMLBasicDef_SmartTagType_name: Property = Property(name="name", type=StringType)
WordprocessingMLBasicDef_SmartTagType_url: Property = Property(name="url", type=StringType)
WordprocessingMLBasicDef_SmartTagType_namespaceuri: Property = Property(name="namespaceuri", type=StringType)
WordprocessingMLBasicDef_SmartTagType.attributes={WordprocessingMLBasicDef_SmartTagType_namespaceuri, WordprocessingMLBasicDef_SmartTagType_url, WordprocessingMLBasicDef_SmartTagType_name}

# SmartTagsCollection class attributes and methods

# WordprocessingMLBasicDef_StringProperty class attributes and methods

# StringType class attributes and methods

# WordprocessingMLBasicDef_StringType class attributes and methods
WordprocessingMLBasicDef_StringType_val: Property = Property(name="val", type=StringType)
WordprocessingMLBasicDef_StringType.attributes={WordprocessingMLBasicDef_StringType_val}

# SmartTagType class attributes and methods

# WordprocessingMLBasicDef_WordDocument class attributes and methods

# DocumentPropertiesCollection class attributes and methods

# ListsElt class attributes and methods

# StylesElt class attributes and methods

# DocPrElt class attributes and methods

# BodyElt class attributes and methods

# StringProperty class attributes and methods

# WordprocessingMLBasicDef_DocPrElt class attributes and methods

# FontsListElt class attributes and methods

# BlockLevelElt class attributes and methods

# SectPrElt class attributes and methods

# WordprocessingMLBasicDef_BlockLevelElt class attributes and methods

# NoteElt class attributes and methods

# WordprocessingMLBasicDef_BlockLevelChunkElt class attributes and methods

# WordprocessingMLBasicDef_BodyElt class attributes and methods

# ParaContentElt class attributes and methods

# WordprocessingMLBasicDef_ParaPrElt class attributes and methods

# ParaElt class attributes and methods

# WordprocessingMLBasicDef_ParaContentElt class attributes and methods

# WordprocessingMLBasicDef_RunElt class attributes and methods

# RunPrElt class attributes and methods

# WordprocessingMLBasicDef_ParaElt class attributes and methods

# BlockLevelChunkElt class attributes and methods

# ParaPrElt class attributes and methods

# WordprocessingMLBasicDef_RunPrElt class attributes and methods

# RunElt class attributes and methods

# WordprocessingMLBasicDef_RunContentElt class attributes and methods

# WordprocessingMLBasicDef_BreakElt class attributes and methods
WordprocessingMLBasicDef_BreakElt_type: Property = Property(name="type", type=StringType)
WordprocessingMLBasicDef_BreakElt.attributes={WordprocessingMLBasicDef_BreakElt_type}

# WordprocessingMLBasicDef_Text class attributes and methods

# WordprocessingMLBasicDef_DelText class attributes and methods

# RunContentElt class attributes and methods

# WordprocessingMLBasicDef_NoBreakHyphen class attributes and methods

# WordprocessingMLBasicDef_SoftHyphen class attributes and methods

# WordprocessingMLBasicDef_AnnotationRef class attributes and methods

# WordprocessingMLBasicDef_FootnoteRef class attributes and methods

# WordprocessingMLBasicDef_EndnoteRef class attributes and methods

# WordprocessingMLBasicDef_Separator class attributes and methods

# WordprocessingMLBasicDef_ContinuationSeparator class attributes and methods

# WordprocessingMLBasicDef_PgNum class attributes and methods

# WordprocessingMLBasicDef_Cr class attributes and methods

# WordprocessingMLBasicDef_Footnote class attributes and methods

# WordprocessingMLBasicDef_InstrText class attributes and methods

# WordprocessingMLBasicDef_DelInstrText class attributes and methods

# WordprocessingMLBasicDef_Picture class attributes and methods

# PictureType class attributes and methods

# WordprocessingMLBasicDef_Symbol class attributes and methods

# SymElt class attributes and methods

# WordprocessingMLBasicDef_SymElt class attributes and methods

# WordprocessingMLBasicDef_Endnote class attributes and methods

# WordprocessingMLBasicDef_NoteElt class attributes and methods
WordprocessingMLBasicDef_NoteElt_type: Property = Property(name="type", type=StringType)
WordprocessingMLBasicDef_NoteElt_suppressRef: Property = Property(name="suppressRef", type=StringType)
WordprocessingMLBasicDef_NoteElt.attributes={WordprocessingMLBasicDef_NoteElt_suppressRef, WordprocessingMLBasicDef_NoteElt_type}

# WordprocessingMLBasicDef_FldChar class attributes and methods

# WordprocessingMLBasicDef_SectPrElt class attributes and methods

# FldCharElt class attributes and methods

# WordprocessingMLBasicDef_FldCharElt class attributes and methods
WordprocessingMLBasicDef_FldCharElt_fldCharType: Property = Property(name="fldCharType", type=StringType)
WordprocessingMLBasicDef_FldCharElt_fldLock: Property = Property(name="fldLock", type=StringType)
WordprocessingMLBasicDef_FldCharElt.attributes={WordprocessingMLBasicDef_FldCharElt_fldCharType, WordprocessingMLBasicDef_FldCharElt_fldLock}

# WordprocessingMLBasicDef_FontsListElt class attributes and methods

# WordprocessingMLBasicDef_ListsElt class attributes and methods

# WordprocessingMLBasicDef_StylesElt class attributes and methods

# WordprocessingMLBasicDef_Tab class attributes and methods

# TabElt class attributes and methods

# WordprocessingMLBasicDef_RunLevelElt class attributes and methods

# WordprocessingMLBasicDef_CfChunk class attributes and methods

# WordprocessingMLBasicDef_SimpleFieldElt class attributes and methods

# WordprocessingMLBasicDef_HLinkElt class attributes and methods

# WordprocessingMLBasicDef_SubDocElt class attributes and methods

# WordprocessingMLBasicDef_PictureType class attributes and methods

# WordprocessingMLBasicDef_TabElt class attributes and methods

# Relationships
dp_wordDocument1: BinaryAssociation = BinaryAssociation(
    name="dp_wordDocument1",
    ends={
        Property(name="WordDocument", type=WordprocessingMLBasicDef_DocumentPropertiesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="wd_docProperties", type=WordDocument, multiplicity=Multiplicity(1, 1))
    }
)
value0: BinaryAssociation = BinaryAssociation(
    name="value0",
    ends={
        Property(name="DateTimeType", type=WordprocessingMLBasicDef_DateTimeTypeValue, multiplicity=Multiplicity(1, 1)),
        Property(name="WordprocessingMLBasicDef_DateTimeTypeValue", type=DateTimeType, multiplicity=Multiplicity(1, 1))
    }
)
version2: BinaryAssociation = BinaryAssociation(
    name="version2",
    ends={
        Property(name="VersionType", type=WordprocessingMLBasicDef_DocumentPropertiesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="WordprocessingMLBasicDef_DocumentPropertiesCollection", type=VersionType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lastPrinted3: BinaryAssociation = BinaryAssociation(
    name="lastPrinted3",
    ends={
        Property(name="DateTimeType5", type=WordprocessingMLBasicDef_DocumentPropertiesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="WordprocessingMLBasicDef_DocumentPropertiesCollection4", type=DateTimeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
created6: BinaryAssociation = BinaryAssociation(
    name="created6",
    ends={
        Property(name="DateTimeType8", type=WordprocessingMLBasicDef_DocumentPropertiesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="WordprocessingMLBasicDef_DocumentPropertiesCollection7", type=DateTimeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lastSaved9: BinaryAssociation = BinaryAssociation(
    name="lastSaved9",
    ends={
        Property(name="DateTimeType11", type=WordprocessingMLBasicDef_DocumentPropertiesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="WordprocessingMLBasicDef_DocumentPropertiesCollection10", type=DateTimeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cdp_wordDocument12: BinaryAssociation = BinaryAssociation(
    name="cdp_wordDocument12",
    ends={
        Property(name="WordDocument13", type=WordprocessingMLBasicDef_CustomDocumentPropertiesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="wd_customDocProperties", type=WordDocument, multiplicity=Multiplicity(1, 1))
    }
)
customDocumentProperties14: BinaryAssociation = BinaryAssociation(
    name="customDocumentProperties14",
    ends={
        Property(name="CustomDocumentProperty", type=WordprocessingMLBasicDef_CustomDocumentPropertiesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="customDocumentProperty_cdpe", type=CustomDocumentProperty, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
customDocumentProperty_cdpe15: BinaryAssociation = BinaryAssociation(
    name="customDocumentProperty_cdpe15",
    ends={
        Property(name="CustomDocumentPropertiesCollection", type=WordprocessingMLBasicDef_CustomDocumentProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="customDocumentProperties", type=CustomDocumentPropertiesCollection, multiplicity=Multiplicity(1, 1))
    }
)
value16: BinaryAssociation = BinaryAssociation(
    name="value16",
    ends={
        Property(name="ValueType", type=WordprocessingMLBasicDef_CustomDocumentProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="WordprocessingMLBasicDef_CustomDocumentProperty", type=ValueType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
smartTagType_ste17: BinaryAssociation = BinaryAssociation(
    name="smartTagType_ste17",
    ends={
        Property(name="SmartTagsCollection", type=WordprocessingMLBasicDef_SmartTagType, multiplicity=Multiplicity(1, 1)),
        Property(name="smartTagTypes", type=SmartTagsCollection, multiplicity=Multiplicity(1, 1))
    }
)
st_wordDocument18: BinaryAssociation = BinaryAssociation(
    name="st_wordDocument18",
    ends={
        Property(name="WordDocument19", type=WordprocessingMLBasicDef_SmartTagsCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="wd_smartTags", type=WordDocument, multiplicity=Multiplicity(1, 1))
    }
)
smartTagTypes20: BinaryAssociation = BinaryAssociation(
    name="smartTagTypes20",
    ends={
        Property(name="SmartTagType", type=WordprocessingMLBasicDef_SmartTagsCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="smartTagType_ste", type=SmartTagType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
wd_smartTags21: BinaryAssociation = BinaryAssociation(
    name="wd_smartTags21",
    ends={
        Property(name="SmartTagsCollection22", type=WordprocessingMLBasicDef_WordDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="st_wordDocument", type=SmartTagsCollection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
wd_docProperties23: BinaryAssociation = BinaryAssociation(
    name="wd_docProperties23",
    ends={
        Property(name="DocumentPropertiesCollection", type=WordprocessingMLBasicDef_WordDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="dp_wordDocument", type=DocumentPropertiesCollection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
wd_customDocProperties24: BinaryAssociation = BinaryAssociation(
    name="wd_customDocProperties24",
    ends={
        Property(name="CustomDocumentPropertiesCollection25", type=WordprocessingMLBasicDef_WordDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="cdp_wordDocument", type=CustomDocumentPropertiesCollection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lists31: BinaryAssociation = BinaryAssociation(
    name="lists31",
    ends={
        Property(name="ListsElt", type=WordprocessingMLBasicDef_WordDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="le_wordDocument", type=ListsElt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
styles32: BinaryAssociation = BinaryAssociation(
    name="styles32",
    ends={
        Property(name="StylesElt", type=WordprocessingMLBasicDef_WordDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="se_wordDocument", type=StylesElt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
docPr33: BinaryAssociation = BinaryAssociation(
    name="docPr33",
    ends={
        Property(name="DocPrElt", type=WordprocessingMLBasicDef_WordDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="dpe_wordDocument", type=DocPrElt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body34: BinaryAssociation = BinaryAssociation(
    name="body34",
    ends={
        Property(name="BodyElt", type=WordprocessingMLBasicDef_WordDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="be_wordDocument", type=BodyElt, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ignoreSubtree26: BinaryAssociation = BinaryAssociation(
    name="ignoreSubtree26",
    ends={
        Property(name="StringProperty", type=WordprocessingMLBasicDef_WordDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="WordprocessingMLBasicDef_WordDocument", type=StringProperty, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ignoreElements27: BinaryAssociation = BinaryAssociation(
    name="ignoreElements27",
    ends={
        Property(name="StringProperty29", type=WordprocessingMLBasicDef_WordDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="WordprocessingMLBasicDef_WordDocument28", type=StringProperty, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fonts30: BinaryAssociation = BinaryAssociation(
    name="fonts30",
    ends={
        Property(name="FontsListElt", type=WordprocessingMLBasicDef_WordDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="fle_wordDocument", type=FontsListElt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
be_wordDocument37: BinaryAssociation = BinaryAssociation(
    name="be_wordDocument37",
    ends={
        Property(name="WordDocument38", type=WordprocessingMLBasicDef_BodyElt, multiplicity=Multiplicity(1, 1)),
        Property(name="body", type=WordDocument, multiplicity=Multiplicity(1, 1))
    }
)
blockLevelElts39: BinaryAssociation = BinaryAssociation(
    name="blockLevelElts39",
    ends={
        Property(name="BlockLevelElt", type=WordprocessingMLBasicDef_BodyElt, multiplicity=Multiplicity(1, 1)),
        Property(name="ble_bodyElt", type=BlockLevelElt, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sectPr40: BinaryAssociation = BinaryAssociation(
    name="sectPr40",
    ends={
        Property(name="SectPrElt", type=WordprocessingMLBasicDef_BodyElt, multiplicity=Multiplicity(1, 1)),
        Property(name="spe_bodyElt", type=SectPrElt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ble_bodyElt41: BinaryAssociation = BinaryAssociation(
    name="ble_bodyElt41",
    ends={
        Property(name="BodyElt42", type=WordprocessingMLBasicDef_BlockLevelElt, multiplicity=Multiplicity(1, 1)),
        Property(name="blockLevelElts", type=BodyElt, multiplicity=Multiplicity(1, 1))
    }
)
ble_note43: BinaryAssociation = BinaryAssociation(
    name="ble_note43",
    ends={
        Property(name="NoteElt", type=WordprocessingMLBasicDef_BlockLevelElt, multiplicity=Multiplicity(1, 1)),
        Property(name="n_blockLevelElts", type=NoteElt, multiplicity=Multiplicity(1, 1))
    }
)
dpe_wordDocument35: BinaryAssociation = BinaryAssociation(
    name="dpe_wordDocument35",
    ends={
        Property(name="WordDocument36", type=WordprocessingMLBasicDef_DocPrElt, multiplicity=Multiplicity(1, 1)),
        Property(name="docPr", type=WordDocument, multiplicity=Multiplicity(1, 1))
    }
)
pContentElts45: BinaryAssociation = BinaryAssociation(
    name="pContentElts45",
    ends={
        Property(name="ParaContentElt", type=WordprocessingMLBasicDef_ParaElt, multiplicity=Multiplicity(1, 1)),
        Property(name="pce_pElt", type=ParaContentElt, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ppe_pElt46: BinaryAssociation = BinaryAssociation(
    name="ppe_pElt46",
    ends={
        Property(name="ParaElt", type=WordprocessingMLBasicDef_ParaPrElt, multiplicity=Multiplicity(1, 1)),
        Property(name="pPr", type=ParaElt, multiplicity=Multiplicity(1, 1))
    }
)
pce_pElt47: BinaryAssociation = BinaryAssociation(
    name="pce_pElt47",
    ends={
        Property(name="ParaElt48", type=WordprocessingMLBasicDef_ParaContentElt, multiplicity=Multiplicity(1, 1)),
        Property(name="pContentElts", type=ParaElt, multiplicity=Multiplicity(1, 1))
    }
)
rPr49: BinaryAssociation = BinaryAssociation(
    name="rPr49",
    ends={
        Property(name="RunPrElt", type=WordprocessingMLBasicDef_RunElt, multiplicity=Multiplicity(1, 1)),
        Property(name="rpe_rElt", type=RunPrElt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pPr44: BinaryAssociation = BinaryAssociation(
    name="pPr44",
    ends={
        Property(name="ParaPrElt", type=WordprocessingMLBasicDef_ParaElt, multiplicity=Multiplicity(1, 1)),
        Property(name="ppe_pElt", type=ParaPrElt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rpe_rElt51: BinaryAssociation = BinaryAssociation(
    name="rpe_rElt51",
    ends={
        Property(name="RunElt", type=WordprocessingMLBasicDef_RunPrElt, multiplicity=Multiplicity(1, 1)),
        Property(name="rPr", type=RunElt, multiplicity=Multiplicity(1, 1))
    }
)
rce_rElt52: BinaryAssociation = BinaryAssociation(
    name="rce_rElt52",
    ends={
        Property(name="RunElt53", type=WordprocessingMLBasicDef_RunContentElt, multiplicity=Multiplicity(1, 1)),
        Property(name="rContentElts", type=RunElt, multiplicity=Multiplicity(1, 1))
    }
)
rContentElts50: BinaryAssociation = BinaryAssociation(
    name="rContentElts50",
    ends={
        Property(name="RunContentElt", type=WordprocessingMLBasicDef_RunElt, multiplicity=Multiplicity(1, 1)),
        Property(name="rce_rElt", type=RunContentElt, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
n_blockLevelElts54: BinaryAssociation = BinaryAssociation(
    name="n_blockLevelElts54",
    ends={
        Property(name="BlockLevelElt55", type=WordprocessingMLBasicDef_NoteElt, multiplicity=Multiplicity(1, 1)),
        Property(name="ble_note", type=BlockLevelElt, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
font56: BinaryAssociation = BinaryAssociation(
    name="font56",
    ends={
        Property(name="StringType", type=WordprocessingMLBasicDef_SymElt, multiplicity=Multiplicity(1, 1)),
        Property(name="WordprocessingMLBasicDef_SymElt", type=StringType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
char57: BinaryAssociation = BinaryAssociation(
    name="char57",
    ends={
        Property(name="StringType59", type=WordprocessingMLBasicDef_SymElt, multiplicity=Multiplicity(1, 1)),
        Property(name="WordprocessingMLBasicDef_SymElt58", type=StringType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
fldData60: BinaryAssociation = BinaryAssociation(
    name="fldData60",
    ends={
        Property(name="StringType61", type=WordprocessingMLBasicDef_FldCharElt, multiplicity=Multiplicity(1, 1)),
        Property(name="WordprocessingMLBasicDef_FldCharElt", type=StringType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fle_wordDocument62: BinaryAssociation = BinaryAssociation(
    name="fle_wordDocument62",
    ends={
        Property(name="WordDocument63", type=WordprocessingMLBasicDef_FontsListElt, multiplicity=Multiplicity(1, 1)),
        Property(name="fonts", type=WordDocument, multiplicity=Multiplicity(1, 1))
    }
)
le_wordDocument64: BinaryAssociation = BinaryAssociation(
    name="le_wordDocument64",
    ends={
        Property(name="WordDocument65", type=WordprocessingMLBasicDef_ListsElt, multiplicity=Multiplicity(1, 1)),
        Property(name="lists", type=WordDocument, multiplicity=Multiplicity(1, 1))
    }
)
se_wordDocument66: BinaryAssociation = BinaryAssociation(
    name="se_wordDocument66",
    ends={
        Property(name="WordDocument67", type=WordprocessingMLBasicDef_StylesElt, multiplicity=Multiplicity(1, 1)),
        Property(name="styles", type=WordDocument, multiplicity=Multiplicity(1, 1))
    }
)
spe_bodyElt68: BinaryAssociation = BinaryAssociation(
    name="spe_bodyElt68",
    ends={
        Property(name="BodyElt69", type=WordprocessingMLBasicDef_SectPrElt, multiplicity=Multiplicity(1, 1)),
        Property(name="sectPr", type=BodyElt, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_WordprocessingMLBasicDef_StringValue_ValueType = Generalization(general=ValueType, specific=WordprocessingMLBasicDef_StringValue)
gen_WordprocessingMLBasicDef_FloatValue_ValueType = Generalization(general=ValueType, specific=WordprocessingMLBasicDef_FloatValue)
gen_WordprocessingMLBasicDef_DateTimeTypeValue_ValueType = Generalization(general=ValueType, specific=WordprocessingMLBasicDef_DateTimeTypeValue)
gen_WordprocessingMLBasicDef_BooleanValue_ValueType = Generalization(general=ValueType, specific=WordprocessingMLBasicDef_BooleanValue)
gen_WordprocessingMLBasicDef_StringProperty_StringType = Generalization(general=StringType, specific=WordprocessingMLBasicDef_StringProperty)
gen_WordprocessingMLBasicDef_BlockLevelChunkElt_BlockLevelElt = Generalization(general=BlockLevelElt, specific=WordprocessingMLBasicDef_BlockLevelChunkElt)
gen_WordprocessingMLBasicDef_RunElt_ParaContentElt = Generalization(general=ParaContentElt, specific=WordprocessingMLBasicDef_RunElt)
gen_WordprocessingMLBasicDef_ParaElt_BlockLevelChunkElt = Generalization(general=BlockLevelChunkElt, specific=WordprocessingMLBasicDef_ParaElt)
gen_WordprocessingMLBasicDef_BreakElt_RunContentElt = Generalization(general=RunContentElt, specific=WordprocessingMLBasicDef_BreakElt)
gen_WordprocessingMLBasicDef_Text_RunContentElt = Generalization(general=RunContentElt, specific=WordprocessingMLBasicDef_Text)
gen_WordprocessingMLBasicDef_Text_StringType = Generalization(general=StringType, specific=WordprocessingMLBasicDef_Text)
gen_WordprocessingMLBasicDef_DelText_RunContentElt = Generalization(general=RunContentElt, specific=WordprocessingMLBasicDef_DelText)
gen_WordprocessingMLBasicDef_DelText_StringType = Generalization(general=StringType, specific=WordprocessingMLBasicDef_DelText)
gen_WordprocessingMLBasicDef_NoBreakHyphen_RunContentElt = Generalization(general=RunContentElt, specific=WordprocessingMLBasicDef_NoBreakHyphen)
gen_WordprocessingMLBasicDef_SoftHyphen_RunContentElt = Generalization(general=RunContentElt, specific=WordprocessingMLBasicDef_SoftHyphen)
gen_WordprocessingMLBasicDef_AnnotationRef_RunContentElt = Generalization(general=RunContentElt, specific=WordprocessingMLBasicDef_AnnotationRef)
gen_WordprocessingMLBasicDef_FootnoteRef_RunContentElt = Generalization(general=RunContentElt, specific=WordprocessingMLBasicDef_FootnoteRef)
gen_WordprocessingMLBasicDef_EndnoteRef_RunContentElt = Generalization(general=RunContentElt, specific=WordprocessingMLBasicDef_EndnoteRef)
gen_WordprocessingMLBasicDef_Separator_RunContentElt = Generalization(general=RunContentElt, specific=WordprocessingMLBasicDef_Separator)
gen_WordprocessingMLBasicDef_ContinuationSeparator_RunContentElt = Generalization(general=RunContentElt, specific=WordprocessingMLBasicDef_ContinuationSeparator)
gen_WordprocessingMLBasicDef_PgNum_RunContentElt = Generalization(general=RunContentElt, specific=WordprocessingMLBasicDef_PgNum)
gen_WordprocessingMLBasicDef_Cr_RunContentElt = Generalization(general=RunContentElt, specific=WordprocessingMLBasicDef_Cr)
gen_WordprocessingMLBasicDef_Footnote_RunContentElt = Generalization(general=RunContentElt, specific=WordprocessingMLBasicDef_Footnote)
gen_WordprocessingMLBasicDef_Footnote_NoteElt = Generalization(general=NoteElt, specific=WordprocessingMLBasicDef_Footnote)
gen_WordprocessingMLBasicDef_InstrText_RunContentElt = Generalization(general=RunContentElt, specific=WordprocessingMLBasicDef_InstrText)
gen_WordprocessingMLBasicDef_InstrText_StringType = Generalization(general=StringType, specific=WordprocessingMLBasicDef_InstrText)
gen_WordprocessingMLBasicDef_DelInstrText_RunContentElt = Generalization(general=RunContentElt, specific=WordprocessingMLBasicDef_DelInstrText)
gen_WordprocessingMLBasicDef_DelInstrText_StringType = Generalization(general=StringType, specific=WordprocessingMLBasicDef_DelInstrText)
gen_WordprocessingMLBasicDef_Picture_RunContentElt = Generalization(general=RunContentElt, specific=WordprocessingMLBasicDef_Picture)
gen_WordprocessingMLBasicDef_Picture_PictureType = Generalization(general=PictureType, specific=WordprocessingMLBasicDef_Picture)
gen_WordprocessingMLBasicDef_Symbol_RunContentElt = Generalization(general=RunContentElt, specific=WordprocessingMLBasicDef_Symbol)
gen_WordprocessingMLBasicDef_Symbol_SymElt = Generalization(general=SymElt, specific=WordprocessingMLBasicDef_Symbol)
gen_WordprocessingMLBasicDef_Endnote_RunContentElt = Generalization(general=RunContentElt, specific=WordprocessingMLBasicDef_Endnote)
gen_WordprocessingMLBasicDef_Endnote_NoteElt = Generalization(general=NoteElt, specific=WordprocessingMLBasicDef_Endnote)
gen_WordprocessingMLBasicDef_FldChar_RunContentElt = Generalization(general=RunContentElt, specific=WordprocessingMLBasicDef_FldChar)
gen_WordprocessingMLBasicDef_FldChar_FldCharElt = Generalization(general=FldCharElt, specific=WordprocessingMLBasicDef_FldChar)
gen_WordprocessingMLBasicDef_Tab_RunContentElt = Generalization(general=RunContentElt, specific=WordprocessingMLBasicDef_Tab)
gen_WordprocessingMLBasicDef_Tab_TabElt = Generalization(general=TabElt, specific=WordprocessingMLBasicDef_Tab)
gen_WordprocessingMLBasicDef_RunLevelElt_BlockLevelChunkElt = Generalization(general=BlockLevelChunkElt, specific=WordprocessingMLBasicDef_RunLevelElt)
gen_WordprocessingMLBasicDef_CfChunk_BlockLevelElt = Generalization(general=BlockLevelElt, specific=WordprocessingMLBasicDef_CfChunk)
gen_WordprocessingMLBasicDef_SimpleFieldElt_ParaContentElt = Generalization(general=ParaContentElt, specific=WordprocessingMLBasicDef_SimpleFieldElt)
gen_WordprocessingMLBasicDef_HLinkElt_ParaContentElt = Generalization(general=ParaContentElt, specific=WordprocessingMLBasicDef_HLinkElt)
gen_WordprocessingMLBasicDef_SubDocElt_ParaContentElt = Generalization(general=ParaContentElt, specific=WordprocessingMLBasicDef_SubDocElt)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={WordprocessingMLBasicDef_VersionType, WordprocessingMLBasicDef_DateTimeType, WordprocessingMLBasicDef_DocumentPropertiesCollection, WordDocument, WordprocessingMLBasicDef_ValueType, WordprocessingMLBasicDef_StringValue, ValueType, WordprocessingMLBasicDef_FloatValue, WordprocessingMLBasicDef_DateTimeTypeValue, DateTimeType, WordprocessingMLBasicDef_BooleanValue, VersionType, CustomDocumentProperty, WordprocessingMLBasicDef_CustomDocumentProperty, WordprocessingMLBasicDef_CustomDocumentPropertiesCollection, WordprocessingMLBasicDef_SmartTagsCollection, CustomDocumentPropertiesCollection, WordprocessingMLBasicDef_SmartTagType, SmartTagsCollection, WordprocessingMLBasicDef_StringProperty, StringType, WordprocessingMLBasicDef_StringType, SmartTagType, WordprocessingMLBasicDef_WordDocument, DocumentPropertiesCollection, ListsElt, StylesElt, DocPrElt, BodyElt, StringProperty, WordprocessingMLBasicDef_DocPrElt, FontsListElt, BlockLevelElt, SectPrElt, WordprocessingMLBasicDef_BlockLevelElt, NoteElt, WordprocessingMLBasicDef_BlockLevelChunkElt, WordprocessingMLBasicDef_BodyElt, ParaContentElt, WordprocessingMLBasicDef_ParaPrElt, ParaElt, WordprocessingMLBasicDef_ParaContentElt, WordprocessingMLBasicDef_RunElt, RunPrElt, WordprocessingMLBasicDef_ParaElt, BlockLevelChunkElt, ParaPrElt, WordprocessingMLBasicDef_RunPrElt, RunElt, WordprocessingMLBasicDef_RunContentElt, WordprocessingMLBasicDef_BreakElt, WordprocessingMLBasicDef_Text, WordprocessingMLBasicDef_DelText, RunContentElt, WordprocessingMLBasicDef_NoBreakHyphen, WordprocessingMLBasicDef_SoftHyphen, WordprocessingMLBasicDef_AnnotationRef, WordprocessingMLBasicDef_FootnoteRef, WordprocessingMLBasicDef_EndnoteRef, WordprocessingMLBasicDef_Separator, WordprocessingMLBasicDef_ContinuationSeparator, WordprocessingMLBasicDef_PgNum, WordprocessingMLBasicDef_Cr, WordprocessingMLBasicDef_Footnote, WordprocessingMLBasicDef_InstrText, WordprocessingMLBasicDef_DelInstrText, WordprocessingMLBasicDef_Picture, PictureType, WordprocessingMLBasicDef_Symbol, SymElt, WordprocessingMLBasicDef_SymElt, WordprocessingMLBasicDef_Endnote, WordprocessingMLBasicDef_NoteElt, WordprocessingMLBasicDef_FldChar, WordprocessingMLBasicDef_SectPrElt, FldCharElt, WordprocessingMLBasicDef_FldCharElt, WordprocessingMLBasicDef_FontsListElt, WordprocessingMLBasicDef_ListsElt, WordprocessingMLBasicDef_StylesElt, WordprocessingMLBasicDef_Tab, TabElt, WordprocessingMLBasicDef_RunLevelElt, WordprocessingMLBasicDef_CfChunk, WordprocessingMLBasicDef_SimpleFieldElt, WordprocessingMLBasicDef_HLinkElt, WordprocessingMLBasicDef_SubDocElt, WordprocessingMLBasicDef_PictureType, WordprocessingMLBasicDef_TabElt, BreakType, NoteValue, OnOffType, FldCharTypeProperty},
    associations={dp_wordDocument1, value0, version2, lastPrinted3, created6, lastSaved9, cdp_wordDocument12, customDocumentProperties14, customDocumentProperty_cdpe15, value16, smartTagType_ste17, st_wordDocument18, smartTagTypes20, wd_smartTags21, wd_docProperties23, wd_customDocProperties24, lists31, styles32, docPr33, body34, ignoreSubtree26, ignoreElements27, fonts30, be_wordDocument37, blockLevelElts39, sectPr40, ble_bodyElt41, ble_note43, dpe_wordDocument35, pContentElts45, ppe_pElt46, pce_pElt47, rPr49, pPr44, rpe_rElt51, rce_rElt52, rContentElts50, n_blockLevelElts54, font56, char57, fldData60, fle_wordDocument62, le_wordDocument64, se_wordDocument66, spe_bodyElt68},
    generalizations={gen_WordprocessingMLBasicDef_StringValue_ValueType, gen_WordprocessingMLBasicDef_FloatValue_ValueType, gen_WordprocessingMLBasicDef_DateTimeTypeValue_ValueType, gen_WordprocessingMLBasicDef_BooleanValue_ValueType, gen_WordprocessingMLBasicDef_StringProperty_StringType, gen_WordprocessingMLBasicDef_BlockLevelChunkElt_BlockLevelElt, gen_WordprocessingMLBasicDef_RunElt_ParaContentElt, gen_WordprocessingMLBasicDef_ParaElt_BlockLevelChunkElt, gen_WordprocessingMLBasicDef_BreakElt_RunContentElt, gen_WordprocessingMLBasicDef_Text_RunContentElt, gen_WordprocessingMLBasicDef_Text_StringType, gen_WordprocessingMLBasicDef_DelText_RunContentElt, gen_WordprocessingMLBasicDef_DelText_StringType, gen_WordprocessingMLBasicDef_NoBreakHyphen_RunContentElt, gen_WordprocessingMLBasicDef_SoftHyphen_RunContentElt, gen_WordprocessingMLBasicDef_AnnotationRef_RunContentElt, gen_WordprocessingMLBasicDef_FootnoteRef_RunContentElt, gen_WordprocessingMLBasicDef_EndnoteRef_RunContentElt, gen_WordprocessingMLBasicDef_Separator_RunContentElt, gen_WordprocessingMLBasicDef_ContinuationSeparator_RunContentElt, gen_WordprocessingMLBasicDef_PgNum_RunContentElt, gen_WordprocessingMLBasicDef_Cr_RunContentElt, gen_WordprocessingMLBasicDef_Footnote_RunContentElt, gen_WordprocessingMLBasicDef_Footnote_NoteElt, gen_WordprocessingMLBasicDef_InstrText_RunContentElt, gen_WordprocessingMLBasicDef_InstrText_StringType, gen_WordprocessingMLBasicDef_DelInstrText_RunContentElt, gen_WordprocessingMLBasicDef_DelInstrText_StringType, gen_WordprocessingMLBasicDef_Picture_RunContentElt, gen_WordprocessingMLBasicDef_Picture_PictureType, gen_WordprocessingMLBasicDef_Symbol_RunContentElt, gen_WordprocessingMLBasicDef_Symbol_SymElt, gen_WordprocessingMLBasicDef_Endnote_RunContentElt, gen_WordprocessingMLBasicDef_Endnote_NoteElt, gen_WordprocessingMLBasicDef_FldChar_RunContentElt, gen_WordprocessingMLBasicDef_FldChar_FldCharElt, gen_WordprocessingMLBasicDef_Tab_RunContentElt, gen_WordprocessingMLBasicDef_Tab_TabElt, gen_WordprocessingMLBasicDef_RunLevelElt_BlockLevelChunkElt, gen_WordprocessingMLBasicDef_CfChunk_BlockLevelElt, gen_WordprocessingMLBasicDef_SimpleFieldElt_ParaContentElt, gen_WordprocessingMLBasicDef_HLinkElt_ParaContentElt, gen_WordprocessingMLBasicDef_SubDocElt_ParaContentElt},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)