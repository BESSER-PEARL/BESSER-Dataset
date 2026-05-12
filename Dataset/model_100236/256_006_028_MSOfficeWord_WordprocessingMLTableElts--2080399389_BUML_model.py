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
NoteValue: Enumeration = Enumeration(
    name="NoteValue",
    literals={
            EnumerationLiteral(name="ftn_normal"),
			EnumerationLiteral(name="ftn_separator"),
			EnumerationLiteral(name="ftn_continuation_separator"),
			EnumerationLiteral(name="ftn_continuation_notice")
    }
)

BreakType: Enumeration = Enumeration(
    name="BreakType",
    literals={
            EnumerationLiteral(name="bt_page"),
			EnumerationLiteral(name="bt_column"),
			EnumerationLiteral(name="bt_text_wrapping")
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
            EnumerationLiteral(name="fctp_begin"),
			EnumerationLiteral(name="fctp_separate"),
			EnumerationLiteral(name="fctp_end")
    }
)

# Classes
WordprocessingMLTableElts_DateTimeType = Class(name="WordprocessingMLTableElts_DateTimeType")
WordprocessingMLTableElts_DateTimeTypeValue = Class(name="WordprocessingMLTableElts_DateTimeTypeValue")
DateTimeType = Class(name="DateTimeType")
WordprocessingMLTableElts_VersionType = Class(name="WordprocessingMLTableElts_VersionType")
WordprocessingMLTableElts_ValueType = Class(name="WordprocessingMLTableElts_ValueType", is_abstract=True)
WordprocessingMLTableElts_StringValue = Class(name="WordprocessingMLTableElts_StringValue")
ValueType = Class(name="ValueType")
WordprocessingMLTableElts_FloatValue = Class(name="WordprocessingMLTableElts_FloatValue")
WordprocessingMLTableElts_BooleanValue = Class(name="WordprocessingMLTableElts_BooleanValue")
WordprocessingMLTableElts_DocumentPropertiesCollection = Class(name="WordprocessingMLTableElts_DocumentPropertiesCollection")
WordDocument = Class(name="WordDocument")
VersionType = Class(name="VersionType")
WordprocessingMLTableElts_CustomDocumentPropertiesCollection = Class(name="WordprocessingMLTableElts_CustomDocumentPropertiesCollection")
WordprocessingMLTableElts_SmartTagType = Class(name="WordprocessingMLTableElts_SmartTagType")
SmartTagsCollection = Class(name="SmartTagsCollection")
CustomDocumentProperty = Class(name="CustomDocumentProperty")
WordprocessingMLTableElts_CustomDocumentProperty = Class(name="WordprocessingMLTableElts_CustomDocumentProperty")
CustomDocumentPropertiesCollection = Class(name="CustomDocumentPropertiesCollection")
WordprocessingMLTableElts_SmartTagsCollection = Class(name="WordprocessingMLTableElts_SmartTagsCollection")
SmartTagType = Class(name="SmartTagType")
WordprocessingMLTableElts_StringProperty = Class(name="WordprocessingMLTableElts_StringProperty")
StringType = Class(name="StringType")
WordprocessingMLTableElts_StringType = Class(name="WordprocessingMLTableElts_StringType")
StringProperty = Class(name="StringProperty")
WordprocessingMLTableElts_WordDocument = Class(name="WordprocessingMLTableElts_WordDocument")
DocumentPropertiesCollection = Class(name="DocumentPropertiesCollection")
DocPrElt = Class(name="DocPrElt")
FontsListElt = Class(name="FontsListElt")
ListsElt = Class(name="ListsElt")
StylesElt = Class(name="StylesElt")
SectPrElt = Class(name="SectPrElt")
WordprocessingMLTableElts_BlockLevelElt = Class(name="WordprocessingMLTableElts_BlockLevelElt", is_abstract=True)
BodyElt = Class(name="BodyElt")
WordprocessingMLTableElts_DocPrElt = Class(name="WordprocessingMLTableElts_DocPrElt")
WordprocessingMLTableElts_BodyElt = Class(name="WordprocessingMLTableElts_BodyElt")
BlockLevelElt = Class(name="BlockLevelElt")
WordprocessingMLTableElts_ParaPrElt = Class(name="WordprocessingMLTableElts_ParaPrElt")
ParaElt = Class(name="ParaElt")
NoteElt = Class(name="NoteElt")
TableCellElt = Class(name="TableCellElt")
WordprocessingMLTableElts_BlockLevelChunkElt = Class(name="WordprocessingMLTableElts_BlockLevelChunkElt", is_abstract=True)
WordprocessingMLTableElts_ParaElt = Class(name="WordprocessingMLTableElts_ParaElt")
BlockLevelChunkElt = Class(name="BlockLevelChunkElt")
ParaPrElt = Class(name="ParaPrElt")
ParaContentElt = Class(name="ParaContentElt")
WordprocessingMLTableElts_RunContentElt = Class(name="WordprocessingMLTableElts_RunContentElt", is_abstract=True)
WordprocessingMLTableElts_ParaContentElt = Class(name="WordprocessingMLTableElts_ParaContentElt", is_abstract=True)
WordprocessingMLTableElts_RunElt = Class(name="WordprocessingMLTableElts_RunElt")
RunPrElt = Class(name="RunPrElt")
RunContentElt = Class(name="RunContentElt")
WordprocessingMLTableElts_RunPrElt = Class(name="WordprocessingMLTableElts_RunPrElt")
RunElt = Class(name="RunElt")
WordprocessingMLTableElts_DelInstrText = Class(name="WordprocessingMLTableElts_DelInstrText")
WordprocessingMLTableElts_NoBreakHyphen = Class(name="WordprocessingMLTableElts_NoBreakHyphen")
WordprocessingMLTableElts_SoftHyphen = Class(name="WordprocessingMLTableElts_SoftHyphen")
WordprocessingMLTableElts_AnnotationRef = Class(name="WordprocessingMLTableElts_AnnotationRef")
WordprocessingMLTableElts_FootnoteRef = Class(name="WordprocessingMLTableElts_FootnoteRef")
WordprocessingMLTableElts_BreakElt = Class(name="WordprocessingMLTableElts_BreakElt")
WordprocessingMLTableElts_Text = Class(name="WordprocessingMLTableElts_Text")
WordprocessingMLTableElts_DelText = Class(name="WordprocessingMLTableElts_DelText")
WordprocessingMLTableElts_InstrText = Class(name="WordprocessingMLTableElts_InstrText")
WordprocessingMLTableElts_Picture = Class(name="WordprocessingMLTableElts_Picture")
PictureType = Class(name="PictureType")
WordprocessingMLTableElts_Symbol = Class(name="WordprocessingMLTableElts_Symbol")
SymElt = Class(name="SymElt")
WordprocessingMLTableElts_EndnoteRef = Class(name="WordprocessingMLTableElts_EndnoteRef")
WordprocessingMLTableElts_Separator = Class(name="WordprocessingMLTableElts_Separator")
WordprocessingMLTableElts_ContinuationSeparator = Class(name="WordprocessingMLTableElts_ContinuationSeparator")
WordprocessingMLTableElts_PgNum = Class(name="WordprocessingMLTableElts_PgNum")
WordprocessingMLTableElts_Cr = Class(name="WordprocessingMLTableElts_Cr")
WordprocessingMLTableElts_Footnote = Class(name="WordprocessingMLTableElts_Footnote")
WordprocessingMLTableElts_Endnote = Class(name="WordprocessingMLTableElts_Endnote")
WordprocessingMLTableElts_NoteElt = Class(name="WordprocessingMLTableElts_NoteElt", is_abstract=True)
WordprocessingMLTableElts_SymElt = Class(name="WordprocessingMLTableElts_SymElt")
WordprocessingMLTableElts_Tab = Class(name="WordprocessingMLTableElts_Tab")
TabElt = Class(name="TabElt")
WordprocessingMLTableElts_FldChar = Class(name="WordprocessingMLTableElts_FldChar")
FldCharElt = Class(name="FldCharElt")
WordprocessingMLTableElts_FldCharElt = Class(name="WordprocessingMLTableElts_FldCharElt")
TableContentElt = Class(name="TableContentElt")
WordprocessingMLTableElts_TablePrElt = Class(name="WordprocessingMLTableElts_TablePrElt")
WordprocessingMLTableElts_TableElt = Class(name="WordprocessingMLTableElts_TableElt")
TablePrElt = Class(name="TablePrElt")
TableGridElt = Class(name="TableGridElt")
RunLevelElt = Class(name="RunLevelElt")
TableElt = Class(name="TableElt")
WordprocessingMLTableElts_TableGridElt = Class(name="WordprocessingMLTableElts_TableGridElt")
WordprocessingMLTableElts_TableContentElt = Class(name="WordprocessingMLTableElts_TableContentElt")
RowElt = Class(name="RowElt")
WordprocessingMLTableElts_TablePrExElt = Class(name="WordprocessingMLTableElts_TablePrExElt")
WordprocessingMLTableElts_TableRowPrElt = Class(name="WordprocessingMLTableElts_TableRowPrElt")
WordprocessingMLTableElts_RowElt = Class(name="WordprocessingMLTableElts_RowElt")
TablePrExElt = Class(name="TablePrExElt")
TableRowPrElt = Class(name="TableRowPrElt")
RowContentElt = Class(name="RowContentElt")
TableCellPrElt = Class(name="TableCellPrElt")
WordprocessingMLTableElts_RowContentElt = Class(name="WordprocessingMLTableElts_RowContentElt")
WordprocessingMLTableElts_TableCellElt = Class(name="WordprocessingMLTableElts_TableCellElt")
WordprocessingMLTableElts_StylesElt = Class(name="WordprocessingMLTableElts_StylesElt")
WordprocessingMLTableElts_TableCellPrElt = Class(name="WordprocessingMLTableElts_TableCellPrElt")
WordprocessingMLTableElts_FontsListElt = Class(name="WordprocessingMLTableElts_FontsListElt")
WordprocessingMLTableElts_ListsElt = Class(name="WordprocessingMLTableElts_ListsElt")
WordprocessingMLTableElts_CfChunk = Class(name="WordprocessingMLTableElts_CfChunk")
WordprocessingMLTableElts_SimpleFieldElt = Class(name="WordprocessingMLTableElts_SimpleFieldElt")
WordprocessingMLTableElts_HLinkElt = Class(name="WordprocessingMLTableElts_HLinkElt")
WordprocessingMLTableElts_SectPrElt = Class(name="WordprocessingMLTableElts_SectPrElt")
WordprocessingMLTableElts_RunLevelElt = Class(name="WordprocessingMLTableElts_RunLevelElt")
WordprocessingMLTableElts_SubDocElt = Class(name="WordprocessingMLTableElts_SubDocElt")
WordprocessingMLTableElts_PictureType = Class(name="WordprocessingMLTableElts_PictureType")
WordprocessingMLTableElts_TabElt = Class(name="WordprocessingMLTableElts_TabElt")

# WordprocessingMLTableElts_DateTimeType class attributes and methods
WordprocessingMLTableElts_DateTimeType_hour: Property = Property(name="hour", type=StringType)
WordprocessingMLTableElts_DateTimeType_minute: Property = Property(name="minute", type=StringType)
WordprocessingMLTableElts_DateTimeType_second: Property = Property(name="second", type=StringType)
WordprocessingMLTableElts_DateTimeType_year: Property = Property(name="year", type=StringType)
WordprocessingMLTableElts_DateTimeType_month: Property = Property(name="month", type=StringType)
WordprocessingMLTableElts_DateTimeType_day: Property = Property(name="day", type=StringType)
WordprocessingMLTableElts_DateTimeType.attributes={WordprocessingMLTableElts_DateTimeType_year, WordprocessingMLTableElts_DateTimeType_day, WordprocessingMLTableElts_DateTimeType_second, WordprocessingMLTableElts_DateTimeType_minute, WordprocessingMLTableElts_DateTimeType_month, WordprocessingMLTableElts_DateTimeType_hour}

# WordprocessingMLTableElts_DateTimeTypeValue class attributes and methods

# DateTimeType class attributes and methods

# WordprocessingMLTableElts_VersionType class attributes and methods
WordprocessingMLTableElts_VersionType_n: Property = Property(name="n", type=StringType)
WordprocessingMLTableElts_VersionType_nn: Property = Property(name="nn", type=StringType)
WordprocessingMLTableElts_VersionType.attributes={WordprocessingMLTableElts_VersionType_nn, WordprocessingMLTableElts_VersionType_n}

# WordprocessingMLTableElts_ValueType class attributes and methods

# WordprocessingMLTableElts_StringValue class attributes and methods
WordprocessingMLTableElts_StringValue_value: Property = Property(name="value", type=StringType)
WordprocessingMLTableElts_StringValue.attributes={WordprocessingMLTableElts_StringValue_value}

# ValueType class attributes and methods

# WordprocessingMLTableElts_FloatValue class attributes and methods
WordprocessingMLTableElts_FloatValue_value: Property = Property(name="value", type=StringType)
WordprocessingMLTableElts_FloatValue.attributes={WordprocessingMLTableElts_FloatValue_value}

# WordprocessingMLTableElts_BooleanValue class attributes and methods
WordprocessingMLTableElts_BooleanValue_value: Property = Property(name="value", type=StringType)
WordprocessingMLTableElts_BooleanValue.attributes={WordprocessingMLTableElts_BooleanValue_value}

# WordprocessingMLTableElts_DocumentPropertiesCollection class attributes and methods
WordprocessingMLTableElts_DocumentPropertiesCollection_keywords: Property = Property(name="keywords", type=StringType)
WordprocessingMLTableElts_DocumentPropertiesCollection_description: Property = Property(name="description", type=StringType)
WordprocessingMLTableElts_DocumentPropertiesCollection_category: Property = Property(name="category", type=StringType)
WordprocessingMLTableElts_DocumentPropertiesCollection_title: Property = Property(name="title", type=StringType)
WordprocessingMLTableElts_DocumentPropertiesCollection_subject: Property = Property(name="subject", type=StringType)
WordprocessingMLTableElts_DocumentPropertiesCollection_totalTime: Property = Property(name="totalTime", type=StringType)
WordprocessingMLTableElts_DocumentPropertiesCollection_author: Property = Property(name="author", type=StringType)
WordprocessingMLTableElts_DocumentPropertiesCollection_lastAuthor: Property = Property(name="lastAuthor", type=StringType)
WordprocessingMLTableElts_DocumentPropertiesCollection_manager: Property = Property(name="manager", type=StringType)
WordprocessingMLTableElts_DocumentPropertiesCollection_company: Property = Property(name="company", type=StringType)
WordprocessingMLTableElts_DocumentPropertiesCollection_hyperlinkBase: Property = Property(name="hyperlinkBase", type=StringType)
WordprocessingMLTableElts_DocumentPropertiesCollection_revision: Property = Property(name="revision", type=StringType)
WordprocessingMLTableElts_DocumentPropertiesCollection_presentationFormat: Property = Property(name="presentationFormat", type=StringType)
WordprocessingMLTableElts_DocumentPropertiesCollection_guid: Property = Property(name="guid", type=StringType)
WordprocessingMLTableElts_DocumentPropertiesCollection_appName: Property = Property(name="appName", type=StringType)
WordprocessingMLTableElts_DocumentPropertiesCollection_lines: Property = Property(name="lines", type=StringType)
WordprocessingMLTableElts_DocumentPropertiesCollection_paragraphs: Property = Property(name="paragraphs", type=StringType)
WordprocessingMLTableElts_DocumentPropertiesCollection_pages: Property = Property(name="pages", type=StringType)
WordprocessingMLTableElts_DocumentPropertiesCollection_words: Property = Property(name="words", type=StringType)
WordprocessingMLTableElts_DocumentPropertiesCollection_characters: Property = Property(name="characters", type=StringType)
WordprocessingMLTableElts_DocumentPropertiesCollection_charactersWithSpaces: Property = Property(name="charactersWithSpaces", type=StringType)
WordprocessingMLTableElts_DocumentPropertiesCollection_bytes: Property = Property(name="bytes", type=StringType)
WordprocessingMLTableElts_DocumentPropertiesCollection.attributes={WordprocessingMLTableElts_DocumentPropertiesCollection_manager, WordprocessingMLTableElts_DocumentPropertiesCollection_hyperlinkBase, WordprocessingMLTableElts_DocumentPropertiesCollection_paragraphs, WordprocessingMLTableElts_DocumentPropertiesCollection_words, WordprocessingMLTableElts_DocumentPropertiesCollection_guid, WordprocessingMLTableElts_DocumentPropertiesCollection_author, WordprocessingMLTableElts_DocumentPropertiesCollection_charactersWithSpaces, WordprocessingMLTableElts_DocumentPropertiesCollection_company, WordprocessingMLTableElts_DocumentPropertiesCollection_pages, WordprocessingMLTableElts_DocumentPropertiesCollection_appName, WordprocessingMLTableElts_DocumentPropertiesCollection_description, WordprocessingMLTableElts_DocumentPropertiesCollection_title, WordprocessingMLTableElts_DocumentPropertiesCollection_presentationFormat, WordprocessingMLTableElts_DocumentPropertiesCollection_lastAuthor, WordprocessingMLTableElts_DocumentPropertiesCollection_totalTime, WordprocessingMLTableElts_DocumentPropertiesCollection_revision, WordprocessingMLTableElts_DocumentPropertiesCollection_characters, WordprocessingMLTableElts_DocumentPropertiesCollection_bytes, WordprocessingMLTableElts_DocumentPropertiesCollection_lines, WordprocessingMLTableElts_DocumentPropertiesCollection_category, WordprocessingMLTableElts_DocumentPropertiesCollection_subject, WordprocessingMLTableElts_DocumentPropertiesCollection_keywords}

# WordDocument class attributes and methods

# VersionType class attributes and methods

# WordprocessingMLTableElts_CustomDocumentPropertiesCollection class attributes and methods

# WordprocessingMLTableElts_SmartTagType class attributes and methods
WordprocessingMLTableElts_SmartTagType_namespaceuri: Property = Property(name="namespaceuri", type=StringType)
WordprocessingMLTableElts_SmartTagType_name: Property = Property(name="name", type=StringType)
WordprocessingMLTableElts_SmartTagType_url: Property = Property(name="url", type=StringType)
WordprocessingMLTableElts_SmartTagType.attributes={WordprocessingMLTableElts_SmartTagType_name, WordprocessingMLTableElts_SmartTagType_url, WordprocessingMLTableElts_SmartTagType_namespaceuri}

# SmartTagsCollection class attributes and methods

# CustomDocumentProperty class attributes and methods

# WordprocessingMLTableElts_CustomDocumentProperty class attributes and methods
WordprocessingMLTableElts_CustomDocumentProperty_name: Property = Property(name="name", type=StringType)
WordprocessingMLTableElts_CustomDocumentProperty.attributes={WordprocessingMLTableElts_CustomDocumentProperty_name}

# CustomDocumentPropertiesCollection class attributes and methods

# WordprocessingMLTableElts_SmartTagsCollection class attributes and methods

# SmartTagType class attributes and methods

# WordprocessingMLTableElts_StringProperty class attributes and methods

# StringType class attributes and methods

# WordprocessingMLTableElts_StringType class attributes and methods
WordprocessingMLTableElts_StringType_val: Property = Property(name="val", type=StringType)
WordprocessingMLTableElts_StringType.attributes={WordprocessingMLTableElts_StringType_val}

# StringProperty class attributes and methods

# WordprocessingMLTableElts_WordDocument class attributes and methods

# DocumentPropertiesCollection class attributes and methods

# DocPrElt class attributes and methods

# FontsListElt class attributes and methods

# ListsElt class attributes and methods

# StylesElt class attributes and methods

# SectPrElt class attributes and methods

# WordprocessingMLTableElts_BlockLevelElt class attributes and methods

# BodyElt class attributes and methods

# WordprocessingMLTableElts_DocPrElt class attributes and methods

# WordprocessingMLTableElts_BodyElt class attributes and methods

# BlockLevelElt class attributes and methods

# WordprocessingMLTableElts_ParaPrElt class attributes and methods

# ParaElt class attributes and methods

# NoteElt class attributes and methods

# TableCellElt class attributes and methods

# WordprocessingMLTableElts_BlockLevelChunkElt class attributes and methods

# WordprocessingMLTableElts_ParaElt class attributes and methods

# BlockLevelChunkElt class attributes and methods

# ParaPrElt class attributes and methods

# ParaContentElt class attributes and methods

# WordprocessingMLTableElts_RunContentElt class attributes and methods

# WordprocessingMLTableElts_ParaContentElt class attributes and methods

# WordprocessingMLTableElts_RunElt class attributes and methods

# RunPrElt class attributes and methods

# RunContentElt class attributes and methods

# WordprocessingMLTableElts_RunPrElt class attributes and methods

# RunElt class attributes and methods

# WordprocessingMLTableElts_DelInstrText class attributes and methods

# WordprocessingMLTableElts_NoBreakHyphen class attributes and methods

# WordprocessingMLTableElts_SoftHyphen class attributes and methods

# WordprocessingMLTableElts_AnnotationRef class attributes and methods

# WordprocessingMLTableElts_FootnoteRef class attributes and methods

# WordprocessingMLTableElts_BreakElt class attributes and methods
WordprocessingMLTableElts_BreakElt_type: Property = Property(name="type", type=StringType)
WordprocessingMLTableElts_BreakElt.attributes={WordprocessingMLTableElts_BreakElt_type}

# WordprocessingMLTableElts_Text class attributes and methods

# WordprocessingMLTableElts_DelText class attributes and methods

# WordprocessingMLTableElts_InstrText class attributes and methods

# WordprocessingMLTableElts_Picture class attributes and methods

# PictureType class attributes and methods

# WordprocessingMLTableElts_Symbol class attributes and methods

# SymElt class attributes and methods

# WordprocessingMLTableElts_EndnoteRef class attributes and methods

# WordprocessingMLTableElts_Separator class attributes and methods

# WordprocessingMLTableElts_ContinuationSeparator class attributes and methods

# WordprocessingMLTableElts_PgNum class attributes and methods

# WordprocessingMLTableElts_Cr class attributes and methods

# WordprocessingMLTableElts_Footnote class attributes and methods

# WordprocessingMLTableElts_Endnote class attributes and methods

# WordprocessingMLTableElts_NoteElt class attributes and methods
WordprocessingMLTableElts_NoteElt_type: Property = Property(name="type", type=StringType)
WordprocessingMLTableElts_NoteElt_suppressRef: Property = Property(name="suppressRef", type=StringType)
WordprocessingMLTableElts_NoteElt.attributes={WordprocessingMLTableElts_NoteElt_suppressRef, WordprocessingMLTableElts_NoteElt_type}

# WordprocessingMLTableElts_SymElt class attributes and methods

# WordprocessingMLTableElts_Tab class attributes and methods

# TabElt class attributes and methods

# WordprocessingMLTableElts_FldChar class attributes and methods

# FldCharElt class attributes and methods

# WordprocessingMLTableElts_FldCharElt class attributes and methods
WordprocessingMLTableElts_FldCharElt_fldCharType: Property = Property(name="fldCharType", type=StringType)
WordprocessingMLTableElts_FldCharElt_fldLock: Property = Property(name="fldLock", type=StringType)
WordprocessingMLTableElts_FldCharElt.attributes={WordprocessingMLTableElts_FldCharElt_fldLock, WordprocessingMLTableElts_FldCharElt_fldCharType}

# TableContentElt class attributes and methods

# WordprocessingMLTableElts_TablePrElt class attributes and methods

# WordprocessingMLTableElts_TableElt class attributes and methods

# TablePrElt class attributes and methods

# TableGridElt class attributes and methods

# RunLevelElt class attributes and methods

# TableElt class attributes and methods

# WordprocessingMLTableElts_TableGridElt class attributes and methods

# WordprocessingMLTableElts_TableContentElt class attributes and methods

# RowElt class attributes and methods

# WordprocessingMLTableElts_TablePrExElt class attributes and methods

# WordprocessingMLTableElts_TableRowPrElt class attributes and methods

# WordprocessingMLTableElts_RowElt class attributes and methods

# TablePrExElt class attributes and methods

# TableRowPrElt class attributes and methods

# RowContentElt class attributes and methods

# TableCellPrElt class attributes and methods

# WordprocessingMLTableElts_RowContentElt class attributes and methods

# WordprocessingMLTableElts_TableCellElt class attributes and methods

# WordprocessingMLTableElts_StylesElt class attributes and methods

# WordprocessingMLTableElts_TableCellPrElt class attributes and methods

# WordprocessingMLTableElts_FontsListElt class attributes and methods

# WordprocessingMLTableElts_ListsElt class attributes and methods

# WordprocessingMLTableElts_CfChunk class attributes and methods

# WordprocessingMLTableElts_SimpleFieldElt class attributes and methods

# WordprocessingMLTableElts_HLinkElt class attributes and methods

# WordprocessingMLTableElts_SectPrElt class attributes and methods

# WordprocessingMLTableElts_RunLevelElt class attributes and methods

# WordprocessingMLTableElts_SubDocElt class attributes and methods

# WordprocessingMLTableElts_PictureType class attributes and methods

# WordprocessingMLTableElts_TabElt class attributes and methods

# Relationships
value0: BinaryAssociation = BinaryAssociation(
    name="value0",
    ends={
        Property(name="DateTimeType", type=WordprocessingMLTableElts_DateTimeTypeValue, multiplicity=Multiplicity(1, 1)),
        Property(name="WordprocessingMLTableElts_DateTimeTypeValue", type=DateTimeType, multiplicity=Multiplicity(1, 1))
    }
)
dp_wordDocument1: BinaryAssociation = BinaryAssociation(
    name="dp_wordDocument1",
    ends={
        Property(name="WordDocument", type=WordprocessingMLTableElts_DocumentPropertiesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="wd_docProperties", type=WordDocument, multiplicity=Multiplicity(1, 1))
    }
)
version2: BinaryAssociation = BinaryAssociation(
    name="version2",
    ends={
        Property(name="WordprocessingMLTableElts_DocumentPropertiesCollection", type=VersionType, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="VersionType", type=WordprocessingMLTableElts_DocumentPropertiesCollection, multiplicity=Multiplicity(1, 1))
    }
)
lastPrinted3: BinaryAssociation = BinaryAssociation(
    name="lastPrinted3",
    ends={
        Property(name="DateTimeType5", type=WordprocessingMLTableElts_DocumentPropertiesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="WordprocessingMLTableElts_DocumentPropertiesCollection4", type=DateTimeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
created6: BinaryAssociation = BinaryAssociation(
    name="created6",
    ends={
        Property(name="DateTimeType8", type=WordprocessingMLTableElts_DocumentPropertiesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="WordprocessingMLTableElts_DocumentPropertiesCollection7", type=DateTimeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lastSaved9: BinaryAssociation = BinaryAssociation(
    name="lastSaved9",
    ends={
        Property(name="DateTimeType11", type=WordprocessingMLTableElts_DocumentPropertiesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="WordprocessingMLTableElts_DocumentPropertiesCollection10", type=DateTimeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
smartTagType_ste17: BinaryAssociation = BinaryAssociation(
    name="smartTagType_ste17",
    ends={
        Property(name="SmartTagsCollection", type=WordprocessingMLTableElts_SmartTagType, multiplicity=Multiplicity(1, 1)),
        Property(name="smartTagTypes", type=SmartTagsCollection, multiplicity=Multiplicity(1, 1))
    }
)
cdp_wordDocument12: BinaryAssociation = BinaryAssociation(
    name="cdp_wordDocument12",
    ends={
        Property(name="WordDocument13", type=WordprocessingMLTableElts_CustomDocumentPropertiesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="wd_customDocProperties", type=WordDocument, multiplicity=Multiplicity(1, 1))
    }
)
customDocumentProperties14: BinaryAssociation = BinaryAssociation(
    name="customDocumentProperties14",
    ends={
        Property(name="CustomDocumentProperty", type=WordprocessingMLTableElts_CustomDocumentPropertiesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="customDocumentProperty_cdpe", type=CustomDocumentProperty, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
customDocumentProperty_cdpe15: BinaryAssociation = BinaryAssociation(
    name="customDocumentProperty_cdpe15",
    ends={
        Property(name="CustomDocumentPropertiesCollection", type=WordprocessingMLTableElts_CustomDocumentProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="customDocumentProperties", type=CustomDocumentPropertiesCollection, multiplicity=Multiplicity(1, 1))
    }
)
value16: BinaryAssociation = BinaryAssociation(
    name="value16",
    ends={
        Property(name="ValueType", type=WordprocessingMLTableElts_CustomDocumentProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="WordprocessingMLTableElts_CustomDocumentProperty", type=ValueType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
st_wordDocument18: BinaryAssociation = BinaryAssociation(
    name="st_wordDocument18",
    ends={
        Property(name="WordDocument19", type=WordprocessingMLTableElts_SmartTagsCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="wd_smartTags", type=WordDocument, multiplicity=Multiplicity(1, 1))
    }
)
smartTagTypes20: BinaryAssociation = BinaryAssociation(
    name="smartTagTypes20",
    ends={
        Property(name="SmartTagType", type=WordprocessingMLTableElts_SmartTagsCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="smartTagType_ste", type=SmartTagType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
wd_customDocProperties24: BinaryAssociation = BinaryAssociation(
    name="wd_customDocProperties24",
    ends={
        Property(name="CustomDocumentPropertiesCollection25", type=WordprocessingMLTableElts_WordDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="cdp_wordDocument", type=CustomDocumentPropertiesCollection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ignoreSubtree26: BinaryAssociation = BinaryAssociation(
    name="ignoreSubtree26",
    ends={
        Property(name="StringProperty", type=WordprocessingMLTableElts_WordDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="WordprocessingMLTableElts_WordDocument", type=StringProperty, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
wd_smartTags21: BinaryAssociation = BinaryAssociation(
    name="wd_smartTags21",
    ends={
        Property(name="SmartTagsCollection22", type=WordprocessingMLTableElts_WordDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="st_wordDocument", type=SmartTagsCollection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
wd_docProperties23: BinaryAssociation = BinaryAssociation(
    name="wd_docProperties23",
    ends={
        Property(name="DocumentPropertiesCollection", type=WordprocessingMLTableElts_WordDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="dp_wordDocument", type=DocumentPropertiesCollection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
styles32: BinaryAssociation = BinaryAssociation(
    name="styles32",
    ends={
        Property(name="se_wordDocument", type=StylesElt, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="StylesElt", type=WordprocessingMLTableElts_WordDocument, multiplicity=Multiplicity(1, 1))
    }
)
docPr33: BinaryAssociation = BinaryAssociation(
    name="docPr33",
    ends={
        Property(name="DocPrElt", type=WordprocessingMLTableElts_WordDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="dpe_wordDocument", type=DocPrElt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ignoreElements27: BinaryAssociation = BinaryAssociation(
    name="ignoreElements27",
    ends={
        Property(name="StringProperty29", type=WordprocessingMLTableElts_WordDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="WordprocessingMLTableElts_WordDocument28", type=StringProperty, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fonts30: BinaryAssociation = BinaryAssociation(
    name="fonts30",
    ends={
        Property(name="FontsListElt", type=WordprocessingMLTableElts_WordDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="fle_wordDocument", type=FontsListElt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lists31: BinaryAssociation = BinaryAssociation(
    name="lists31",
    ends={
        Property(name="ListsElt", type=WordprocessingMLTableElts_WordDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="le_wordDocument", type=ListsElt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sectPr40: BinaryAssociation = BinaryAssociation(
    name="sectPr40",
    ends={
        Property(name="SectPrElt", type=WordprocessingMLTableElts_BodyElt, multiplicity=Multiplicity(1, 1)),
        Property(name="spe_bodyElt", type=SectPrElt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ble_bodyElt41: BinaryAssociation = BinaryAssociation(
    name="ble_bodyElt41",
    ends={
        Property(name="BodyElt42", type=WordprocessingMLTableElts_BlockLevelElt, multiplicity=Multiplicity(1, 1)),
        Property(name="blockLevelElts", type=BodyElt, multiplicity=Multiplicity(1, 1))
    }
)
body34: BinaryAssociation = BinaryAssociation(
    name="body34",
    ends={
        Property(name="BodyElt", type=WordprocessingMLTableElts_WordDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="be_wordDocument", type=BodyElt, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
dpe_wordDocument35: BinaryAssociation = BinaryAssociation(
    name="dpe_wordDocument35",
    ends={
        Property(name="WordDocument36", type=WordprocessingMLTableElts_DocPrElt, multiplicity=Multiplicity(1, 1)),
        Property(name="docPr", type=WordDocument, multiplicity=Multiplicity(1, 1))
    }
)
be_wordDocument37: BinaryAssociation = BinaryAssociation(
    name="be_wordDocument37",
    ends={
        Property(name="WordDocument38", type=WordprocessingMLTableElts_BodyElt, multiplicity=Multiplicity(1, 1)),
        Property(name="body", type=WordDocument, multiplicity=Multiplicity(1, 1))
    }
)
blockLevelElts39: BinaryAssociation = BinaryAssociation(
    name="blockLevelElts39",
    ends={
        Property(name="BlockLevelElt", type=WordprocessingMLTableElts_BodyElt, multiplicity=Multiplicity(1, 1)),
        Property(name="ble_bodyElt", type=BlockLevelElt, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pContentElts46: BinaryAssociation = BinaryAssociation(
    name="pContentElts46",
    ends={
        Property(name="pce_pElt", type=ParaContentElt, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="ParaContentElt", type=WordprocessingMLTableElts_ParaElt, multiplicity=Multiplicity(1, 1))
    }
)
ppe_pElt47: BinaryAssociation = BinaryAssociation(
    name="ppe_pElt47",
    ends={
        Property(name="ParaElt", type=WordprocessingMLTableElts_ParaPrElt, multiplicity=Multiplicity(1, 1)),
        Property(name="pPr", type=ParaElt, multiplicity=Multiplicity(1, 1))
    }
)
ble_note43: BinaryAssociation = BinaryAssociation(
    name="ble_note43",
    ends={
        Property(name="NoteElt", type=WordprocessingMLTableElts_BlockLevelElt, multiplicity=Multiplicity(1, 1)),
        Property(name="n_blockLevelElts", type=NoteElt, multiplicity=Multiplicity(1, 1))
    }
)
ble_tableCellElt44: BinaryAssociation = BinaryAssociation(
    name="ble_tableCellElt44",
    ends={
        Property(name="TableCellElt", type=WordprocessingMLTableElts_BlockLevelElt, multiplicity=Multiplicity(1, 1)),
        Property(name="tce_content", type=TableCellElt, multiplicity=Multiplicity(1, 1))
    }
)
pPr45: BinaryAssociation = BinaryAssociation(
    name="pPr45",
    ends={
        Property(name="ParaPrElt", type=WordprocessingMLTableElts_ParaElt, multiplicity=Multiplicity(1, 1)),
        Property(name="ppe_pElt", type=ParaPrElt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rpe_rElt52: BinaryAssociation = BinaryAssociation(
    name="rpe_rElt52",
    ends={
        Property(name="RunElt", type=WordprocessingMLTableElts_RunPrElt, multiplicity=Multiplicity(1, 1)),
        Property(name="rPr", type=RunElt, multiplicity=Multiplicity(1, 1))
    }
)
rce_rElt53: BinaryAssociation = BinaryAssociation(
    name="rce_rElt53",
    ends={
        Property(name="RunElt54", type=WordprocessingMLTableElts_RunContentElt, multiplicity=Multiplicity(1, 1)),
        Property(name="rContentElts", type=RunElt, multiplicity=Multiplicity(1, 1))
    }
)
pce_pElt48: BinaryAssociation = BinaryAssociation(
    name="pce_pElt48",
    ends={
        Property(name="ParaElt49", type=WordprocessingMLTableElts_ParaContentElt, multiplicity=Multiplicity(1, 1)),
        Property(name="pContentElts", type=ParaElt, multiplicity=Multiplicity(1, 1))
    }
)
rPr50: BinaryAssociation = BinaryAssociation(
    name="rPr50",
    ends={
        Property(name="RunPrElt", type=WordprocessingMLTableElts_RunElt, multiplicity=Multiplicity(1, 1)),
        Property(name="rpe_rElt", type=RunPrElt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rContentElts51: BinaryAssociation = BinaryAssociation(
    name="rContentElts51",
    ends={
        Property(name="RunContentElt", type=WordprocessingMLTableElts_RunElt, multiplicity=Multiplicity(1, 1)),
        Property(name="rce_rElt", type=RunContentElt, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
n_blockLevelElts55: BinaryAssociation = BinaryAssociation(
    name="n_blockLevelElts55",
    ends={
        Property(name="BlockLevelElt56", type=WordprocessingMLTableElts_NoteElt, multiplicity=Multiplicity(1, 1)),
        Property(name="ble_note", type=BlockLevelElt, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
fldData61: BinaryAssociation = BinaryAssociation(
    name="fldData61",
    ends={
        Property(name="StringType62", type=WordprocessingMLTableElts_FldCharElt, multiplicity=Multiplicity(1, 1)),
        Property(name="WordprocessingMLTableElts_FldCharElt", type=StringType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
font57: BinaryAssociation = BinaryAssociation(
    name="font57",
    ends={
        Property(name="StringType", type=WordprocessingMLTableElts_SymElt, multiplicity=Multiplicity(1, 1)),
        Property(name="WordprocessingMLTableElts_SymElt", type=StringType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
char58: BinaryAssociation = BinaryAssociation(
    name="char58",
    ends={
        Property(name="StringType60", type=WordprocessingMLTableElts_SymElt, multiplicity=Multiplicity(1, 1)),
        Property(name="WordprocessingMLTableElts_SymElt59", type=StringType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tblContent65: BinaryAssociation = BinaryAssociation(
    name="tblContent65",
    ends={
        Property(name="TableContentElt", type=WordprocessingMLTableElts_TableElt, multiplicity=Multiplicity(1, 1)),
        Property(name="tce_tblElt", type=TableContentElt, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
tblPr63: BinaryAssociation = BinaryAssociation(
    name="tblPr63",
    ends={
        Property(name="TablePrElt", type=WordprocessingMLTableElts_TableElt, multiplicity=Multiplicity(1, 1)),
        Property(name="tpe_tblElt", type=TablePrElt, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tblGrid64: BinaryAssociation = BinaryAssociation(
    name="tblGrid64",
    ends={
        Property(name="TableGridElt", type=WordprocessingMLTableElts_TableElt, multiplicity=Multiplicity(1, 1)),
        Property(name="tge_tblElt", type=TableGridElt, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tr71: BinaryAssociation = BinaryAssociation(
    name="tr71",
    ends={
        Property(name="re_tblContentElt", type=RowElt, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="RowElt", type=WordprocessingMLTableElts_TableContentElt, multiplicity=Multiplicity(1, 1))
    }
)
tce_runLevelElts72: BinaryAssociation = BinaryAssociation(
    name="tce_runLevelElts72",
    ends={
        Property(name="RunLevelElt", type=WordprocessingMLTableElts_TableContentElt, multiplicity=Multiplicity(1, 1)),
        Property(name="rle_tblContentElt", type=RunLevelElt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tpe_tblElt66: BinaryAssociation = BinaryAssociation(
    name="tpe_tblElt66",
    ends={
        Property(name="TableElt", type=WordprocessingMLTableElts_TablePrElt, multiplicity=Multiplicity(1, 1)),
        Property(name="tblPr", type=TableElt, multiplicity=Multiplicity(1, 1))
    }
)
tge_tblElt67: BinaryAssociation = BinaryAssociation(
    name="tge_tblElt67",
    ends={
        Property(name="TableElt68", type=WordprocessingMLTableElts_TableGridElt, multiplicity=Multiplicity(1, 1)),
        Property(name="tblGrid", type=TableElt, multiplicity=Multiplicity(1, 1))
    }
)
tce_tblElt69: BinaryAssociation = BinaryAssociation(
    name="tce_tblElt69",
    ends={
        Property(name="TableElt70", type=WordprocessingMLTableElts_TableContentElt, multiplicity=Multiplicity(1, 1)),
        Property(name="tblContent", type=TableElt, multiplicity=Multiplicity(1, 1))
    }
)
tpee_rowElt78: BinaryAssociation = BinaryAssociation(
    name="tpee_rowElt78",
    ends={
        Property(name="RowElt79", type=WordprocessingMLTableElts_TablePrExElt, multiplicity=Multiplicity(1, 1)),
        Property(name="tblPrEx", type=RowElt, multiplicity=Multiplicity(1, 1))
    }
)
re_tblContentElt73: BinaryAssociation = BinaryAssociation(
    name="re_tblContentElt73",
    ends={
        Property(name="TableContentElt74", type=WordprocessingMLTableElts_RowElt, multiplicity=Multiplicity(1, 1)),
        Property(name="tr", type=TableContentElt, multiplicity=Multiplicity(1, 1))
    }
)
tblPrEx75: BinaryAssociation = BinaryAssociation(
    name="tblPrEx75",
    ends={
        Property(name="TablePrExElt", type=WordprocessingMLTableElts_RowElt, multiplicity=Multiplicity(1, 1)),
        Property(name="tpee_rowElt", type=TablePrExElt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
trPr76: BinaryAssociation = BinaryAssociation(
    name="trPr76",
    ends={
        Property(name="TableRowPrElt", type=WordprocessingMLTableElts_RowElt, multiplicity=Multiplicity(1, 1)),
        Property(name="tpe_rowElt", type=TableRowPrElt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rowContent77: BinaryAssociation = BinaryAssociation(
    name="rowContent77",
    ends={
        Property(name="RowContentElt", type=WordprocessingMLTableElts_RowElt, multiplicity=Multiplicity(1, 1)),
        Property(name="rce_rowElt", type=RowContentElt, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
tce_rowContentElt88: BinaryAssociation = BinaryAssociation(
    name="tce_rowContentElt88",
    ends={
        Property(name="RowContentElt89", type=WordprocessingMLTableElts_TableCellElt, multiplicity=Multiplicity(1, 1)),
        Property(name="tc", type=RowContentElt, multiplicity=Multiplicity(1, 1))
    }
)
tcPr90: BinaryAssociation = BinaryAssociation(
    name="tcPr90",
    ends={
        Property(name="TableCellPrElt", type=WordprocessingMLTableElts_TableCellElt, multiplicity=Multiplicity(1, 1)),
        Property(name="tcpe_tableCellElt", type=TableCellPrElt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tpe_rowElt80: BinaryAssociation = BinaryAssociation(
    name="tpe_rowElt80",
    ends={
        Property(name="RowElt81", type=WordprocessingMLTableElts_TableRowPrElt, multiplicity=Multiplicity(1, 1)),
        Property(name="trPr", type=RowElt, multiplicity=Multiplicity(1, 1))
    }
)
rce_rowElt82: BinaryAssociation = BinaryAssociation(
    name="rce_rowElt82",
    ends={
        Property(name="RowElt83", type=WordprocessingMLTableElts_RowContentElt, multiplicity=Multiplicity(1, 1)),
        Property(name="rowContent", type=RowElt, multiplicity=Multiplicity(1, 1))
    }
)
tc84: BinaryAssociation = BinaryAssociation(
    name="tc84",
    ends={
        Property(name="TableCellElt85", type=WordprocessingMLTableElts_RowContentElt, multiplicity=Multiplicity(1, 1)),
        Property(name="tce_rowContentElt", type=TableCellElt, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rce_runLevelElts86: BinaryAssociation = BinaryAssociation(
    name="rce_runLevelElts86",
    ends={
        Property(name="RunLevelElt87", type=WordprocessingMLTableElts_RowContentElt, multiplicity=Multiplicity(1, 1)),
        Property(name="rle_rowContentElt", type=RunLevelElt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
le_wordDocument97: BinaryAssociation = BinaryAssociation(
    name="le_wordDocument97",
    ends={
        Property(name="WordDocument98", type=WordprocessingMLTableElts_ListsElt, multiplicity=Multiplicity(1, 1)),
        Property(name="lists", type=WordDocument, multiplicity=Multiplicity(1, 1))
    }
)
tce_content91: BinaryAssociation = BinaryAssociation(
    name="tce_content91",
    ends={
        Property(name="BlockLevelElt92", type=WordprocessingMLTableElts_TableCellElt, multiplicity=Multiplicity(1, 1)),
        Property(name="ble_tableCellElt", type=BlockLevelElt, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
tcpe_tableCellElt93: BinaryAssociation = BinaryAssociation(
    name="tcpe_tableCellElt93",
    ends={
        Property(name="TableCellElt94", type=WordprocessingMLTableElts_TableCellPrElt, multiplicity=Multiplicity(1, 1)),
        Property(name="tcPr", type=TableCellElt, multiplicity=Multiplicity(1, 1))
    }
)
fle_wordDocument95: BinaryAssociation = BinaryAssociation(
    name="fle_wordDocument95",
    ends={
        Property(name="WordDocument96", type=WordprocessingMLTableElts_FontsListElt, multiplicity=Multiplicity(1, 1)),
        Property(name="fonts", type=WordDocument, multiplicity=Multiplicity(1, 1))
    }
)
se_wordDocument99: BinaryAssociation = BinaryAssociation(
    name="se_wordDocument99",
    ends={
        Property(name="WordDocument100", type=WordprocessingMLTableElts_StylesElt, multiplicity=Multiplicity(1, 1)),
        Property(name="styles", type=WordDocument, multiplicity=Multiplicity(1, 1))
    }
)
spe_bodyElt101: BinaryAssociation = BinaryAssociation(
    name="spe_bodyElt101",
    ends={
        Property(name="BodyElt102", type=WordprocessingMLTableElts_SectPrElt, multiplicity=Multiplicity(1, 1)),
        Property(name="sectPr", type=BodyElt, multiplicity=Multiplicity(1, 1))
    }
)
rle_tblContentElt103: BinaryAssociation = BinaryAssociation(
    name="rle_tblContentElt103",
    ends={
        Property(name="TableContentElt104", type=WordprocessingMLTableElts_RunLevelElt, multiplicity=Multiplicity(1, 1)),
        Property(name="tce_runLevelElts", type=TableContentElt, multiplicity=Multiplicity(1, 1))
    }
)
rle_rowContentElt105: BinaryAssociation = BinaryAssociation(
    name="rle_rowContentElt105",
    ends={
        Property(name="RowContentElt106", type=WordprocessingMLTableElts_RunLevelElt, multiplicity=Multiplicity(1, 1)),
        Property(name="rce_runLevelElts", type=RowContentElt, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_WordprocessingMLTableElts_DateTimeTypeValue_ValueType = Generalization(general=ValueType, specific=WordprocessingMLTableElts_DateTimeTypeValue)
gen_WordprocessingMLTableElts_StringValue_ValueType = Generalization(general=ValueType, specific=WordprocessingMLTableElts_StringValue)
gen_WordprocessingMLTableElts_FloatValue_ValueType = Generalization(general=ValueType, specific=WordprocessingMLTableElts_FloatValue)
gen_WordprocessingMLTableElts_BooleanValue_ValueType = Generalization(general=ValueType, specific=WordprocessingMLTableElts_BooleanValue)
gen_WordprocessingMLTableElts_StringProperty_StringType = Generalization(general=StringType, specific=WordprocessingMLTableElts_StringProperty)
gen_WordprocessingMLTableElts_BlockLevelChunkElt_BlockLevelElt = Generalization(general=BlockLevelElt, specific=WordprocessingMLTableElts_BlockLevelChunkElt)
gen_WordprocessingMLTableElts_ParaElt_BlockLevelChunkElt = Generalization(general=BlockLevelChunkElt, specific=WordprocessingMLTableElts_ParaElt)
gen_WordprocessingMLTableElts_RunElt_ParaContentElt = Generalization(general=ParaContentElt, specific=WordprocessingMLTableElts_RunElt)
gen_WordprocessingMLTableElts_DelInstrText_RunContentElt = Generalization(general=RunContentElt, specific=WordprocessingMLTableElts_DelInstrText)
gen_WordprocessingMLTableElts_DelInstrText_StringType = Generalization(general=StringType, specific=WordprocessingMLTableElts_DelInstrText)
gen_WordprocessingMLTableElts_NoBreakHyphen_RunContentElt = Generalization(general=RunContentElt, specific=WordprocessingMLTableElts_NoBreakHyphen)
gen_WordprocessingMLTableElts_SoftHyphen_RunContentElt = Generalization(general=RunContentElt, specific=WordprocessingMLTableElts_SoftHyphen)
gen_WordprocessingMLTableElts_AnnotationRef_RunContentElt = Generalization(general=RunContentElt, specific=WordprocessingMLTableElts_AnnotationRef)
gen_WordprocessingMLTableElts_FootnoteRef_RunContentElt = Generalization(general=RunContentElt, specific=WordprocessingMLTableElts_FootnoteRef)
gen_WordprocessingMLTableElts_BreakElt_RunContentElt = Generalization(general=RunContentElt, specific=WordprocessingMLTableElts_BreakElt)
gen_WordprocessingMLTableElts_Text_RunContentElt = Generalization(general=RunContentElt, specific=WordprocessingMLTableElts_Text)
gen_WordprocessingMLTableElts_Text_StringType = Generalization(general=StringType, specific=WordprocessingMLTableElts_Text)
gen_WordprocessingMLTableElts_DelText_RunContentElt = Generalization(general=RunContentElt, specific=WordprocessingMLTableElts_DelText)
gen_WordprocessingMLTableElts_DelText_StringType = Generalization(general=StringType, specific=WordprocessingMLTableElts_DelText)
gen_WordprocessingMLTableElts_InstrText_RunContentElt = Generalization(general=RunContentElt, specific=WordprocessingMLTableElts_InstrText)
gen_WordprocessingMLTableElts_InstrText_StringType = Generalization(general=StringType, specific=WordprocessingMLTableElts_InstrText)
gen_WordprocessingMLTableElts_Picture_RunContentElt = Generalization(general=RunContentElt, specific=WordprocessingMLTableElts_Picture)
gen_WordprocessingMLTableElts_Picture_PictureType = Generalization(general=PictureType, specific=WordprocessingMLTableElts_Picture)
gen_WordprocessingMLTableElts_Symbol_RunContentElt = Generalization(general=RunContentElt, specific=WordprocessingMLTableElts_Symbol)
gen_WordprocessingMLTableElts_Symbol_SymElt = Generalization(general=SymElt, specific=WordprocessingMLTableElts_Symbol)
gen_WordprocessingMLTableElts_EndnoteRef_RunContentElt = Generalization(general=RunContentElt, specific=WordprocessingMLTableElts_EndnoteRef)
gen_WordprocessingMLTableElts_Separator_RunContentElt = Generalization(general=RunContentElt, specific=WordprocessingMLTableElts_Separator)
gen_WordprocessingMLTableElts_ContinuationSeparator_RunContentElt = Generalization(general=RunContentElt, specific=WordprocessingMLTableElts_ContinuationSeparator)
gen_WordprocessingMLTableElts_PgNum_RunContentElt = Generalization(general=RunContentElt, specific=WordprocessingMLTableElts_PgNum)
gen_WordprocessingMLTableElts_Cr_RunContentElt = Generalization(general=RunContentElt, specific=WordprocessingMLTableElts_Cr)
gen_WordprocessingMLTableElts_Footnote_RunContentElt = Generalization(general=RunContentElt, specific=WordprocessingMLTableElts_Footnote)
gen_WordprocessingMLTableElts_Footnote_NoteElt = Generalization(general=NoteElt, specific=WordprocessingMLTableElts_Footnote)
gen_WordprocessingMLTableElts_Endnote_RunContentElt = Generalization(general=RunContentElt, specific=WordprocessingMLTableElts_Endnote)
gen_WordprocessingMLTableElts_Endnote_NoteElt = Generalization(general=NoteElt, specific=WordprocessingMLTableElts_Endnote)
gen_WordprocessingMLTableElts_Tab_RunContentElt = Generalization(general=RunContentElt, specific=WordprocessingMLTableElts_Tab)
gen_WordprocessingMLTableElts_Tab_TabElt = Generalization(general=TabElt, specific=WordprocessingMLTableElts_Tab)
gen_WordprocessingMLTableElts_FldChar_RunContentElt = Generalization(general=RunContentElt, specific=WordprocessingMLTableElts_FldChar)
gen_WordprocessingMLTableElts_FldChar_FldCharElt = Generalization(general=FldCharElt, specific=WordprocessingMLTableElts_FldChar)
gen_WordprocessingMLTableElts_TableElt_BlockLevelChunkElt = Generalization(general=BlockLevelChunkElt, specific=WordprocessingMLTableElts_TableElt)
gen_WordprocessingMLTableElts_CfChunk_BlockLevelElt = Generalization(general=BlockLevelElt, specific=WordprocessingMLTableElts_CfChunk)
gen_WordprocessingMLTableElts_SimpleFieldElt_ParaContentElt = Generalization(general=ParaContentElt, specific=WordprocessingMLTableElts_SimpleFieldElt)
gen_WordprocessingMLTableElts_HLinkElt_ParaContentElt = Generalization(general=ParaContentElt, specific=WordprocessingMLTableElts_HLinkElt)
gen_WordprocessingMLTableElts_RunLevelElt_BlockLevelChunkElt = Generalization(general=BlockLevelChunkElt, specific=WordprocessingMLTableElts_RunLevelElt)
gen_WordprocessingMLTableElts_SubDocElt_ParaContentElt = Generalization(general=ParaContentElt, specific=WordprocessingMLTableElts_SubDocElt)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={WordprocessingMLTableElts_DateTimeType, WordprocessingMLTableElts_DateTimeTypeValue, DateTimeType, WordprocessingMLTableElts_VersionType, WordprocessingMLTableElts_ValueType, WordprocessingMLTableElts_StringValue, ValueType, WordprocessingMLTableElts_FloatValue, WordprocessingMLTableElts_BooleanValue, WordprocessingMLTableElts_DocumentPropertiesCollection, WordDocument, VersionType, WordprocessingMLTableElts_CustomDocumentPropertiesCollection, WordprocessingMLTableElts_SmartTagType, SmartTagsCollection, CustomDocumentProperty, WordprocessingMLTableElts_CustomDocumentProperty, CustomDocumentPropertiesCollection, WordprocessingMLTableElts_SmartTagsCollection, SmartTagType, WordprocessingMLTableElts_StringProperty, StringType, WordprocessingMLTableElts_StringType, StringProperty, WordprocessingMLTableElts_WordDocument, DocumentPropertiesCollection, DocPrElt, FontsListElt, ListsElt, StylesElt, SectPrElt, WordprocessingMLTableElts_BlockLevelElt, BodyElt, WordprocessingMLTableElts_DocPrElt, WordprocessingMLTableElts_BodyElt, BlockLevelElt, WordprocessingMLTableElts_ParaPrElt, ParaElt, NoteElt, TableCellElt, WordprocessingMLTableElts_BlockLevelChunkElt, WordprocessingMLTableElts_ParaElt, BlockLevelChunkElt, ParaPrElt, ParaContentElt, WordprocessingMLTableElts_RunContentElt, WordprocessingMLTableElts_ParaContentElt, WordprocessingMLTableElts_RunElt, RunPrElt, RunContentElt, WordprocessingMLTableElts_RunPrElt, RunElt, WordprocessingMLTableElts_DelInstrText, WordprocessingMLTableElts_NoBreakHyphen, WordprocessingMLTableElts_SoftHyphen, WordprocessingMLTableElts_AnnotationRef, WordprocessingMLTableElts_FootnoteRef, WordprocessingMLTableElts_BreakElt, WordprocessingMLTableElts_Text, WordprocessingMLTableElts_DelText, WordprocessingMLTableElts_InstrText, WordprocessingMLTableElts_Picture, PictureType, WordprocessingMLTableElts_Symbol, SymElt, WordprocessingMLTableElts_EndnoteRef, WordprocessingMLTableElts_Separator, WordprocessingMLTableElts_ContinuationSeparator, WordprocessingMLTableElts_PgNum, WordprocessingMLTableElts_Cr, WordprocessingMLTableElts_Footnote, WordprocessingMLTableElts_Endnote, WordprocessingMLTableElts_NoteElt, WordprocessingMLTableElts_SymElt, WordprocessingMLTableElts_Tab, TabElt, WordprocessingMLTableElts_FldChar, FldCharElt, WordprocessingMLTableElts_FldCharElt, TableContentElt, WordprocessingMLTableElts_TablePrElt, WordprocessingMLTableElts_TableElt, TablePrElt, TableGridElt, RunLevelElt, TableElt, WordprocessingMLTableElts_TableGridElt, WordprocessingMLTableElts_TableContentElt, RowElt, WordprocessingMLTableElts_TablePrExElt, WordprocessingMLTableElts_TableRowPrElt, WordprocessingMLTableElts_RowElt, TablePrExElt, TableRowPrElt, RowContentElt, TableCellPrElt, WordprocessingMLTableElts_RowContentElt, WordprocessingMLTableElts_TableCellElt, WordprocessingMLTableElts_StylesElt, WordprocessingMLTableElts_TableCellPrElt, WordprocessingMLTableElts_FontsListElt, WordprocessingMLTableElts_ListsElt, WordprocessingMLTableElts_CfChunk, WordprocessingMLTableElts_SimpleFieldElt, WordprocessingMLTableElts_HLinkElt, WordprocessingMLTableElts_SectPrElt, WordprocessingMLTableElts_RunLevelElt, WordprocessingMLTableElts_SubDocElt, WordprocessingMLTableElts_PictureType, WordprocessingMLTableElts_TabElt, NoteValue, BreakType, OnOffType, FldCharTypeProperty},
    associations={value0, dp_wordDocument1, version2, lastPrinted3, created6, lastSaved9, smartTagType_ste17, cdp_wordDocument12, customDocumentProperties14, customDocumentProperty_cdpe15, value16, st_wordDocument18, smartTagTypes20, wd_customDocProperties24, ignoreSubtree26, wd_smartTags21, wd_docProperties23, styles32, docPr33, ignoreElements27, fonts30, lists31, sectPr40, ble_bodyElt41, body34, dpe_wordDocument35, be_wordDocument37, blockLevelElts39, pContentElts46, ppe_pElt47, ble_note43, ble_tableCellElt44, pPr45, rpe_rElt52, rce_rElt53, pce_pElt48, rPr50, rContentElts51, n_blockLevelElts55, fldData61, font57, char58, tblContent65, tblPr63, tblGrid64, tr71, tce_runLevelElts72, tpe_tblElt66, tge_tblElt67, tce_tblElt69, tpee_rowElt78, re_tblContentElt73, tblPrEx75, trPr76, rowContent77, tce_rowContentElt88, tcPr90, tpe_rowElt80, rce_rowElt82, tc84, rce_runLevelElts86, le_wordDocument97, tce_content91, tcpe_tableCellElt93, fle_wordDocument95, se_wordDocument99, spe_bodyElt101, rle_tblContentElt103, rle_rowContentElt105},
    generalizations={gen_WordprocessingMLTableElts_DateTimeTypeValue_ValueType, gen_WordprocessingMLTableElts_StringValue_ValueType, gen_WordprocessingMLTableElts_FloatValue_ValueType, gen_WordprocessingMLTableElts_BooleanValue_ValueType, gen_WordprocessingMLTableElts_StringProperty_StringType, gen_WordprocessingMLTableElts_BlockLevelChunkElt_BlockLevelElt, gen_WordprocessingMLTableElts_ParaElt_BlockLevelChunkElt, gen_WordprocessingMLTableElts_RunElt_ParaContentElt, gen_WordprocessingMLTableElts_DelInstrText_RunContentElt, gen_WordprocessingMLTableElts_DelInstrText_StringType, gen_WordprocessingMLTableElts_NoBreakHyphen_RunContentElt, gen_WordprocessingMLTableElts_SoftHyphen_RunContentElt, gen_WordprocessingMLTableElts_AnnotationRef_RunContentElt, gen_WordprocessingMLTableElts_FootnoteRef_RunContentElt, gen_WordprocessingMLTableElts_BreakElt_RunContentElt, gen_WordprocessingMLTableElts_Text_RunContentElt, gen_WordprocessingMLTableElts_Text_StringType, gen_WordprocessingMLTableElts_DelText_RunContentElt, gen_WordprocessingMLTableElts_DelText_StringType, gen_WordprocessingMLTableElts_InstrText_RunContentElt, gen_WordprocessingMLTableElts_InstrText_StringType, gen_WordprocessingMLTableElts_Picture_RunContentElt, gen_WordprocessingMLTableElts_Picture_PictureType, gen_WordprocessingMLTableElts_Symbol_RunContentElt, gen_WordprocessingMLTableElts_Symbol_SymElt, gen_WordprocessingMLTableElts_EndnoteRef_RunContentElt, gen_WordprocessingMLTableElts_Separator_RunContentElt, gen_WordprocessingMLTableElts_ContinuationSeparator_RunContentElt, gen_WordprocessingMLTableElts_PgNum_RunContentElt, gen_WordprocessingMLTableElts_Cr_RunContentElt, gen_WordprocessingMLTableElts_Footnote_RunContentElt, gen_WordprocessingMLTableElts_Footnote_NoteElt, gen_WordprocessingMLTableElts_Endnote_RunContentElt, gen_WordprocessingMLTableElts_Endnote_NoteElt, gen_WordprocessingMLTableElts_Tab_RunContentElt, gen_WordprocessingMLTableElts_Tab_TabElt, gen_WordprocessingMLTableElts_FldChar_RunContentElt, gen_WordprocessingMLTableElts_FldChar_FldCharElt, gen_WordprocessingMLTableElts_TableElt_BlockLevelChunkElt, gen_WordprocessingMLTableElts_CfChunk_BlockLevelElt, gen_WordprocessingMLTableElts_SimpleFieldElt_ParaContentElt, gen_WordprocessingMLTableElts_HLinkElt_ParaContentElt, gen_WordprocessingMLTableElts_RunLevelElt_BlockLevelChunkElt, gen_WordprocessingMLTableElts_SubDocElt_ParaContentElt},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)