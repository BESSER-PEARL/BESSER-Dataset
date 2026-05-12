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

StyleKindValue: Enumeration = Enumeration(
    name="StyleKindValue",
    literals={
            EnumerationLiteral(name="skv_paragraph"),
			EnumerationLiteral(name="skv_character"),
			EnumerationLiteral(name="skv_table"),
			EnumerationLiteral(name="skv_list")
    }
)

UnderlineValues: Enumeration = Enumeration(
    name="UnderlineValues",
    literals={
            EnumerationLiteral(name="uv_single"),
			EnumerationLiteral(name="uv_words"),
			EnumerationLiteral(name="uv_double"),
			EnumerationLiteral(name="uv_thick"),
			EnumerationLiteral(name="uv_dotted"),
			EnumerationLiteral(name="uv_dotted_heavy"),
			EnumerationLiteral(name="uv_dash"),
			EnumerationLiteral(name="uv_dashed_heavy"),
			EnumerationLiteral(name="uv_dash_long"),
			EnumerationLiteral(name="uv_dash_long_heavy"),
			EnumerationLiteral(name="uv_none"),
			EnumerationLiteral(name="uv_dot_dash"),
			EnumerationLiteral(name="uv_dash_dot_heavy"),
			EnumerationLiteral(name="uv_dot_dot_dash"),
			EnumerationLiteral(name="uv_dash_dot_dot_heavy"),
			EnumerationLiteral(name="uv_wave"),
			EnumerationLiteral(name="uv_wavy_heavy"),
			EnumerationLiteral(name="uv_wavy_double")
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
            EnumerationLiteral(name="fctp_begin"),
			EnumerationLiteral(name="fctp_separate"),
			EnumerationLiteral(name="fctp_end")
    }
)

HintType: Enumeration = Enumeration(
    name="HintType",
    literals={
            EnumerationLiteral(name="ht_fareast"),
			EnumerationLiteral(name="ht_cs"),
			EnumerationLiteral(name="ht_default")
    }
)

HighlightColorValues: Enumeration = Enumeration(
    name="HighlightColorValues",
    literals={
            EnumerationLiteral(name="hcv_black"),
			EnumerationLiteral(name="hcv_blue"),
			EnumerationLiteral(name="hcv_cyan"),
			EnumerationLiteral(name="hcv_green"),
			EnumerationLiteral(name="hcv_magenta"),
			EnumerationLiteral(name="hcv_red"),
			EnumerationLiteral(name="hcv_yellow"),
			EnumerationLiteral(name="hcv_white"),
			EnumerationLiteral(name="hcv_dark_blue"),
			EnumerationLiteral(name="hcv_dark_cyan"),
			EnumerationLiteral(name="hcv_dark_green"),
			EnumerationLiteral(name="hcv_dark_magenta"),
			EnumerationLiteral(name="hcv_dark_red"),
			EnumerationLiteral(name="hcv_dark_yellow"),
			EnumerationLiteral(name="hcv_dark_gray"),
			EnumerationLiteral(name="hcv_light_gray"),
			EnumerationLiteral(name="hcv_none")
    }
)

VerticalAlignRunType: Enumeration = Enumeration(
    name="VerticalAlignRunType",
    literals={
            EnumerationLiteral(name="vart_baseline"),
			EnumerationLiteral(name="vart_superscript"),
			EnumerationLiteral(name="vart_subscript")
    }
)

JustificationValue: Enumeration = Enumeration(
    name="JustificationValue",
    literals={
            EnumerationLiteral(name="jv_left"),
			EnumerationLiteral(name="jv_center"),
			EnumerationLiteral(name="jv_right"),
			EnumerationLiteral(name="jv_both")
    }
)

# Classes
WordprocessingMLStyles_DateTimeType = Class(name="WordprocessingMLStyles_DateTimeType")
WordprocessingMLStyles_VersionType = Class(name="WordprocessingMLStyles_VersionType")
WordprocessingMLStyles_BooleanValue = Class(name="WordprocessingMLStyles_BooleanValue")
WordprocessingMLStyles_DocumentPropertiesCollection = Class(name="WordprocessingMLStyles_DocumentPropertiesCollection")
WordDocument = Class(name="WordDocument")
WordprocessingMLStyles_ValueType = Class(name="WordprocessingMLStyles_ValueType", is_abstract=True)
WordprocessingMLStyles_StringValue = Class(name="WordprocessingMLStyles_StringValue")
ValueType = Class(name="ValueType")
WordprocessingMLStyles_FloatValue = Class(name="WordprocessingMLStyles_FloatValue")
WordprocessingMLStyles_DateTimeTypeValue = Class(name="WordprocessingMLStyles_DateTimeTypeValue")
DateTimeType = Class(name="DateTimeType")
WordprocessingMLStyles_CustomDocumentPropertiesCollection = Class(name="WordprocessingMLStyles_CustomDocumentPropertiesCollection")
CustomDocumentProperty = Class(name="CustomDocumentProperty")
WordprocessingMLStyles_CustomDocumentProperty = Class(name="WordprocessingMLStyles_CustomDocumentProperty")
CustomDocumentPropertiesCollection = Class(name="CustomDocumentPropertiesCollection")
VersionType = Class(name="VersionType")
WordprocessingMLStyles_SmartTagType = Class(name="WordprocessingMLStyles_SmartTagType")
SmartTagsCollection = Class(name="SmartTagsCollection")
WordprocessingMLStyles_SmartTagsCollection = Class(name="WordprocessingMLStyles_SmartTagsCollection")
SmartTagType = Class(name="SmartTagType")
WordprocessingMLStyles_StringProperty = Class(name="WordprocessingMLStyles_StringProperty")
StringType = Class(name="StringType")
WordprocessingMLStyles_StringType = Class(name="WordprocessingMLStyles_StringType")
WordprocessingMLStyles_UnderlineProperty = Class(name="WordprocessingMLStyles_UnderlineProperty")
DocumentPropertiesCollection = Class(name="DocumentPropertiesCollection")
StringProperty = Class(name="StringProperty")
FontsListElt = Class(name="FontsListElt")
ListsElt = Class(name="ListsElt")
WordprocessingMLStyles_WordDocument = Class(name="WordprocessingMLStyles_WordDocument")
BodyElt = Class(name="BodyElt")
WordprocessingMLStyles_DocPrElt = Class(name="WordprocessingMLStyles_DocPrElt")
WordprocessingMLStyles_BodyElt = Class(name="WordprocessingMLStyles_BodyElt")
BlockLevelElt = Class(name="BlockLevelElt")
SectPrElt = Class(name="SectPrElt")
WordprocessingMLStyles_BlockLevelElt = Class(name="WordprocessingMLStyles_BlockLevelElt", is_abstract=True)
NoteElt = Class(name="NoteElt")
TableCellElt = Class(name="TableCellElt")
StylesElt = Class(name="StylesElt")
WordprocessingMLStyles_BlockLevelChunkElt = Class(name="WordprocessingMLStyles_BlockLevelChunkElt", is_abstract=True)
DocPrElt = Class(name="DocPrElt")
WordprocessingMLStyles_ParaElt = Class(name="WordprocessingMLStyles_ParaElt")
BlockLevelChunkElt = Class(name="BlockLevelChunkElt")
ParaPrElt = Class(name="ParaPrElt")
ParaContentElt = Class(name="ParaContentElt")
WordprocessingMLStyles_ParaPrElt = Class(name="WordprocessingMLStyles_ParaPrElt")
ParaElt = Class(name="ParaElt")
StyleElt = Class(name="StyleElt")
WordprocessingMLStyles_ParaContentElt = Class(name="WordprocessingMLStyles_ParaContentElt", is_abstract=True)
WordprocessingMLStyles_RunElt = Class(name="WordprocessingMLStyles_RunElt")
RunPrElt = Class(name="RunPrElt")
RunContentElt = Class(name="RunContentElt")
WordprocessingMLStyles_RunPrElt = Class(name="WordprocessingMLStyles_RunPrElt")
RunElt = Class(name="RunElt")
FontsElt = Class(name="FontsElt")
UnderlineProperty = Class(name="UnderlineProperty")
LangElt = Class(name="LangElt")
WordprocessingMLStyles_LangElt = Class(name="WordprocessingMLStyles_LangElt")
WordprocessingMLStyles_RunContentElt = Class(name="WordprocessingMLStyles_RunContentElt", is_abstract=True)
WordprocessingMLStyles_BreakElt = Class(name="WordprocessingMLStyles_BreakElt")
WordprocessingMLStyles_Text = Class(name="WordprocessingMLStyles_Text")
WordprocessingMLStyles_DelText = Class(name="WordprocessingMLStyles_DelText")
WordprocessingMLStyles_InstrText = Class(name="WordprocessingMLStyles_InstrText")
WordprocessingMLStyles_DelInstrText = Class(name="WordprocessingMLStyles_DelInstrText")
WordprocessingMLStyles_NoBreakHyphen = Class(name="WordprocessingMLStyles_NoBreakHyphen")
WordprocessingMLStyles_SoftHyphen = Class(name="WordprocessingMLStyles_SoftHyphen")
WordprocessingMLStyles_AnnotationRef = Class(name="WordprocessingMLStyles_AnnotationRef")
WordprocessingMLStyles_FootnoteRef = Class(name="WordprocessingMLStyles_FootnoteRef")
WordprocessingMLStyles_EndnoteRef = Class(name="WordprocessingMLStyles_EndnoteRef")
WordprocessingMLStyles_Separator = Class(name="WordprocessingMLStyles_Separator")
WordprocessingMLStyles_ContinuationSeparator = Class(name="WordprocessingMLStyles_ContinuationSeparator")
WordprocessingMLStyles_PgNum = Class(name="WordprocessingMLStyles_PgNum")
WordprocessingMLStyles_Cr = Class(name="WordprocessingMLStyles_Cr")
WordprocessingMLStyles_Footnote = Class(name="WordprocessingMLStyles_Footnote")
FldCharElt = Class(name="FldCharElt")
WordprocessingMLStyles_Endnote = Class(name="WordprocessingMLStyles_Endnote")
WordprocessingMLStyles_NoteElt = Class(name="WordprocessingMLStyles_NoteElt", is_abstract=True)
WordprocessingMLStyles_Picture = Class(name="WordprocessingMLStyles_Picture")
PictureType = Class(name="PictureType")
WordprocessingMLStyles_Symbol = Class(name="WordprocessingMLStyles_Symbol")
SymElt = Class(name="SymElt")
WordprocessingMLStyles_SymElt = Class(name="WordprocessingMLStyles_SymElt")
WordprocessingMLStyles_Tab = Class(name="WordprocessingMLStyles_Tab")
TabElt = Class(name="TabElt")
WordprocessingMLStyles_FldChar = Class(name="WordprocessingMLStyles_FldChar")
WordprocessingMLStyles_TableGridElt = Class(name="WordprocessingMLStyles_TableGridElt")
WordprocessingMLStyles_FldCharElt = Class(name="WordprocessingMLStyles_FldCharElt")
WordprocessingMLStyles_TableElt = Class(name="WordprocessingMLStyles_TableElt")
TablePrElt = Class(name="TablePrElt")
TableGridElt = Class(name="TableGridElt")
TableContentElt = Class(name="TableContentElt")
WordprocessingMLStyles_TablePrElt = Class(name="WordprocessingMLStyles_TablePrElt")
TableElt = Class(name="TableElt")
WordprocessingMLStyles_TablePrExElt = Class(name="WordprocessingMLStyles_TablePrExElt")
WordprocessingMLStyles_TableContentElt = Class(name="WordprocessingMLStyles_TableContentElt")
RowElt = Class(name="RowElt")
RunLevelElt = Class(name="RunLevelElt")
WordprocessingMLStyles_RowElt = Class(name="WordprocessingMLStyles_RowElt")
TablePrExElt = Class(name="TablePrExElt")
TableRowPrElt = Class(name="TableRowPrElt")
RowContentElt = Class(name="RowContentElt")
WordprocessingMLStyles_TableRowPrElt = Class(name="WordprocessingMLStyles_TableRowPrElt")
WordprocessingMLStyles_RowContentElt = Class(name="WordprocessingMLStyles_RowContentElt")
WordprocessingMLStyles_TableCellElt = Class(name="WordprocessingMLStyles_TableCellElt")
TableCellPrElt = Class(name="TableCellPrElt")
WordprocessingMLStyles_TableCellPrElt = Class(name="WordprocessingMLStyles_TableCellPrElt")
WordprocessingMLStyles_FontsListElt = Class(name="WordprocessingMLStyles_FontsListElt")
FontElt = Class(name="FontElt")
WordprocessingMLStyles_FontsElt = Class(name="WordprocessingMLStyles_FontsElt")
WordprocessingMLStyles_FontElt = Class(name="WordprocessingMLStyles_FontElt")
WordprocessingMLStyles_StylesElt = Class(name="WordprocessingMLStyles_StylesElt")
WordprocessingMLStyles_StyleElt = Class(name="WordprocessingMLStyles_StyleElt")
WordprocessingMLStyles_ListsElt = Class(name="WordprocessingMLStyles_ListsElt")
WordprocessingMLStyles_SectPrElt = Class(name="WordprocessingMLStyles_SectPrElt")
WordprocessingMLStyles_RunLevelElt = Class(name="WordprocessingMLStyles_RunLevelElt")
WordprocessingMLStyles_CfChunk = Class(name="WordprocessingMLStyles_CfChunk")
WordprocessingMLStyles_SimpleFieldElt = Class(name="WordprocessingMLStyles_SimpleFieldElt")
WordprocessingMLStyles_HLinkElt = Class(name="WordprocessingMLStyles_HLinkElt")
WordprocessingMLStyles_SubDocElt = Class(name="WordprocessingMLStyles_SubDocElt")
WordprocessingMLStyles_PictureType = Class(name="WordprocessingMLStyles_PictureType")
WordprocessingMLStyles_TabElt = Class(name="WordprocessingMLStyles_TabElt")

# WordprocessingMLStyles_DateTimeType class attributes and methods
WordprocessingMLStyles_DateTimeType_year: Property = Property(name="year", type=StringType)
WordprocessingMLStyles_DateTimeType_month: Property = Property(name="month", type=StringType)
WordprocessingMLStyles_DateTimeType_day: Property = Property(name="day", type=StringType)
WordprocessingMLStyles_DateTimeType_hour: Property = Property(name="hour", type=StringType)
WordprocessingMLStyles_DateTimeType_minute: Property = Property(name="minute", type=StringType)
WordprocessingMLStyles_DateTimeType_second: Property = Property(name="second", type=StringType)
WordprocessingMLStyles_DateTimeType.attributes={WordprocessingMLStyles_DateTimeType_second, WordprocessingMLStyles_DateTimeType_minute, WordprocessingMLStyles_DateTimeType_day, WordprocessingMLStyles_DateTimeType_hour, WordprocessingMLStyles_DateTimeType_year, WordprocessingMLStyles_DateTimeType_month}

# WordprocessingMLStyles_VersionType class attributes and methods
WordprocessingMLStyles_VersionType_n: Property = Property(name="n", type=StringType)
WordprocessingMLStyles_VersionType_nn: Property = Property(name="nn", type=StringType)
WordprocessingMLStyles_VersionType.attributes={WordprocessingMLStyles_VersionType_nn, WordprocessingMLStyles_VersionType_n}

# WordprocessingMLStyles_BooleanValue class attributes and methods
WordprocessingMLStyles_BooleanValue_value: Property = Property(name="value", type=StringType)
WordprocessingMLStyles_BooleanValue.attributes={WordprocessingMLStyles_BooleanValue_value}

# WordprocessingMLStyles_DocumentPropertiesCollection class attributes and methods
WordprocessingMLStyles_DocumentPropertiesCollection_title: Property = Property(name="title", type=StringType)
WordprocessingMLStyles_DocumentPropertiesCollection_subject: Property = Property(name="subject", type=StringType)
WordprocessingMLStyles_DocumentPropertiesCollection_keywords: Property = Property(name="keywords", type=StringType)
WordprocessingMLStyles_DocumentPropertiesCollection_description: Property = Property(name="description", type=StringType)
WordprocessingMLStyles_DocumentPropertiesCollection_category: Property = Property(name="category", type=StringType)
WordprocessingMLStyles_DocumentPropertiesCollection_author: Property = Property(name="author", type=StringType)
WordprocessingMLStyles_DocumentPropertiesCollection_lastAuthor: Property = Property(name="lastAuthor", type=StringType)
WordprocessingMLStyles_DocumentPropertiesCollection_manager: Property = Property(name="manager", type=StringType)
WordprocessingMLStyles_DocumentPropertiesCollection_company: Property = Property(name="company", type=StringType)
WordprocessingMLStyles_DocumentPropertiesCollection_hyperlinkBase: Property = Property(name="hyperlinkBase", type=StringType)
WordprocessingMLStyles_DocumentPropertiesCollection_revision: Property = Property(name="revision", type=StringType)
WordprocessingMLStyles_DocumentPropertiesCollection_totalTime: Property = Property(name="totalTime", type=StringType)
WordprocessingMLStyles_DocumentPropertiesCollection_pages: Property = Property(name="pages", type=StringType)
WordprocessingMLStyles_DocumentPropertiesCollection_words: Property = Property(name="words", type=StringType)
WordprocessingMLStyles_DocumentPropertiesCollection_characters: Property = Property(name="characters", type=StringType)
WordprocessingMLStyles_DocumentPropertiesCollection_charactersWithSpaces: Property = Property(name="charactersWithSpaces", type=StringType)
WordprocessingMLStyles_DocumentPropertiesCollection_bytes: Property = Property(name="bytes", type=StringType)
WordprocessingMLStyles_DocumentPropertiesCollection_lines: Property = Property(name="lines", type=StringType)
WordprocessingMLStyles_DocumentPropertiesCollection_paragraphs: Property = Property(name="paragraphs", type=StringType)
WordprocessingMLStyles_DocumentPropertiesCollection_presentationFormat: Property = Property(name="presentationFormat", type=StringType)
WordprocessingMLStyles_DocumentPropertiesCollection_guid: Property = Property(name="guid", type=StringType)
WordprocessingMLStyles_DocumentPropertiesCollection_appName: Property = Property(name="appName", type=StringType)
WordprocessingMLStyles_DocumentPropertiesCollection.attributes={WordprocessingMLStyles_DocumentPropertiesCollection_revision, WordprocessingMLStyles_DocumentPropertiesCollection_company, WordprocessingMLStyles_DocumentPropertiesCollection_subject, WordprocessingMLStyles_DocumentPropertiesCollection_presentationFormat, WordprocessingMLStyles_DocumentPropertiesCollection_keywords, WordprocessingMLStyles_DocumentPropertiesCollection_manager, WordprocessingMLStyles_DocumentPropertiesCollection_category, WordprocessingMLStyles_DocumentPropertiesCollection_pages, WordprocessingMLStyles_DocumentPropertiesCollection_hyperlinkBase, WordprocessingMLStyles_DocumentPropertiesCollection_lines, WordprocessingMLStyles_DocumentPropertiesCollection_charactersWithSpaces, WordprocessingMLStyles_DocumentPropertiesCollection_description, WordprocessingMLStyles_DocumentPropertiesCollection_lastAuthor, WordprocessingMLStyles_DocumentPropertiesCollection_characters, WordprocessingMLStyles_DocumentPropertiesCollection_author, WordprocessingMLStyles_DocumentPropertiesCollection_guid, WordprocessingMLStyles_DocumentPropertiesCollection_title, WordprocessingMLStyles_DocumentPropertiesCollection_words, WordprocessingMLStyles_DocumentPropertiesCollection_bytes, WordprocessingMLStyles_DocumentPropertiesCollection_totalTime, WordprocessingMLStyles_DocumentPropertiesCollection_appName, WordprocessingMLStyles_DocumentPropertiesCollection_paragraphs}

# WordDocument class attributes and methods

# WordprocessingMLStyles_ValueType class attributes and methods

# WordprocessingMLStyles_StringValue class attributes and methods
WordprocessingMLStyles_StringValue_value: Property = Property(name="value", type=StringType)
WordprocessingMLStyles_StringValue.attributes={WordprocessingMLStyles_StringValue_value}

# ValueType class attributes and methods

# WordprocessingMLStyles_FloatValue class attributes and methods
WordprocessingMLStyles_FloatValue_value: Property = Property(name="value", type=StringType)
WordprocessingMLStyles_FloatValue.attributes={WordprocessingMLStyles_FloatValue_value}

# WordprocessingMLStyles_DateTimeTypeValue class attributes and methods

# DateTimeType class attributes and methods

# WordprocessingMLStyles_CustomDocumentPropertiesCollection class attributes and methods

# CustomDocumentProperty class attributes and methods

# WordprocessingMLStyles_CustomDocumentProperty class attributes and methods
WordprocessingMLStyles_CustomDocumentProperty_name: Property = Property(name="name", type=StringType)
WordprocessingMLStyles_CustomDocumentProperty.attributes={WordprocessingMLStyles_CustomDocumentProperty_name}

# CustomDocumentPropertiesCollection class attributes and methods

# VersionType class attributes and methods

# WordprocessingMLStyles_SmartTagType class attributes and methods
WordprocessingMLStyles_SmartTagType_namespaceuri: Property = Property(name="namespaceuri", type=StringType)
WordprocessingMLStyles_SmartTagType_name: Property = Property(name="name", type=StringType)
WordprocessingMLStyles_SmartTagType_url: Property = Property(name="url", type=StringType)
WordprocessingMLStyles_SmartTagType.attributes={WordprocessingMLStyles_SmartTagType_url, WordprocessingMLStyles_SmartTagType_name, WordprocessingMLStyles_SmartTagType_namespaceuri}

# SmartTagsCollection class attributes and methods

# WordprocessingMLStyles_SmartTagsCollection class attributes and methods

# SmartTagType class attributes and methods

# WordprocessingMLStyles_StringProperty class attributes and methods

# StringType class attributes and methods

# WordprocessingMLStyles_StringType class attributes and methods
WordprocessingMLStyles_StringType_val: Property = Property(name="val", type=StringType)
WordprocessingMLStyles_StringType.attributes={WordprocessingMLStyles_StringType_val}

# WordprocessingMLStyles_UnderlineProperty class attributes and methods
WordprocessingMLStyles_UnderlineProperty_val: Property = Property(name="val", type=StringType)
WordprocessingMLStyles_UnderlineProperty_color: Property = Property(name="color", type=StringType)
WordprocessingMLStyles_UnderlineProperty.attributes={WordprocessingMLStyles_UnderlineProperty_val, WordprocessingMLStyles_UnderlineProperty_color}

# DocumentPropertiesCollection class attributes and methods

# StringProperty class attributes and methods

# FontsListElt class attributes and methods

# ListsElt class attributes and methods

# WordprocessingMLStyles_WordDocument class attributes and methods

# BodyElt class attributes and methods

# WordprocessingMLStyles_DocPrElt class attributes and methods

# WordprocessingMLStyles_BodyElt class attributes and methods

# BlockLevelElt class attributes and methods

# SectPrElt class attributes and methods

# WordprocessingMLStyles_BlockLevelElt class attributes and methods

# NoteElt class attributes and methods

# TableCellElt class attributes and methods

# StylesElt class attributes and methods

# WordprocessingMLStyles_BlockLevelChunkElt class attributes and methods

# DocPrElt class attributes and methods

# WordprocessingMLStyles_ParaElt class attributes and methods

# BlockLevelChunkElt class attributes and methods

# ParaPrElt class attributes and methods

# ParaContentElt class attributes and methods

# WordprocessingMLStyles_ParaPrElt class attributes and methods
WordprocessingMLStyles_ParaPrElt_keepNext: Property = Property(name="keepNext", type=StringType)
WordprocessingMLStyles_ParaPrElt_keepLines: Property = Property(name="keepLines", type=StringType)
WordprocessingMLStyles_ParaPrElt_pageBreakBefore: Property = Property(name="pageBreakBefore", type=StringType)
WordprocessingMLStyles_ParaPrElt_supressLineNumbers: Property = Property(name="supressLineNumbers", type=StringType)
WordprocessingMLStyles_ParaPrElt_suppressAutoHyphens: Property = Property(name="suppressAutoHyphens", type=StringType)
WordprocessingMLStyles_ParaPrElt_contextualSpacing: Property = Property(name="contextualSpacing", type=StringType)
WordprocessingMLStyles_ParaPrElt_bidi: Property = Property(name="bidi", type=StringType)
WordprocessingMLStyles_ParaPrElt_justification: Property = Property(name="justification", type=StringType)
WordprocessingMLStyles_ParaPrElt.attributes={WordprocessingMLStyles_ParaPrElt_pageBreakBefore, WordprocessingMLStyles_ParaPrElt_justification, WordprocessingMLStyles_ParaPrElt_supressLineNumbers, WordprocessingMLStyles_ParaPrElt_contextualSpacing, WordprocessingMLStyles_ParaPrElt_suppressAutoHyphens, WordprocessingMLStyles_ParaPrElt_keepNext, WordprocessingMLStyles_ParaPrElt_keepLines, WordprocessingMLStyles_ParaPrElt_bidi}

# ParaElt class attributes and methods

# StyleElt class attributes and methods

# WordprocessingMLStyles_ParaContentElt class attributes and methods

# WordprocessingMLStyles_RunElt class attributes and methods

# RunPrElt class attributes and methods

# RunContentElt class attributes and methods

# WordprocessingMLStyles_RunPrElt class attributes and methods
WordprocessingMLStyles_RunPrElt_capitals: Property = Property(name="capitals", type=StringType)
WordprocessingMLStyles_RunPrElt_bold: Property = Property(name="bold", type=StringType)
WordprocessingMLStyles_RunPrElt_bold_cs: Property = Property(name="bold_cs", type=StringType)
WordprocessingMLStyles_RunPrElt_italic: Property = Property(name="italic", type=StringType)
WordprocessingMLStyles_RunPrElt_italic_cs: Property = Property(name="italic_cs", type=StringType)
WordprocessingMLStyles_RunPrElt_cs: Property = Property(name="cs", type=StringType)
WordprocessingMLStyles_RunPrElt_smallCapitals: Property = Property(name="smallCapitals", type=StringType)
WordprocessingMLStyles_RunPrElt_strike: Property = Property(name="strike", type=StringType)
WordprocessingMLStyles_RunPrElt_doubleStrike: Property = Property(name="doubleStrike", type=StringType)
WordprocessingMLStyles_RunPrElt_outline: Property = Property(name="outline", type=StringType)
WordprocessingMLStyles_RunPrElt_shadow: Property = Property(name="shadow", type=StringType)
WordprocessingMLStyles_RunPrElt_emboss: Property = Property(name="emboss", type=StringType)
WordprocessingMLStyles_RunPrElt_imprint: Property = Property(name="imprint", type=StringType)
WordprocessingMLStyles_RunPrElt_noProof: Property = Property(name="noProof", type=StringType)
WordprocessingMLStyles_RunPrElt_vanish: Property = Property(name="vanish", type=StringType)
WordprocessingMLStyles_RunPrElt_specVanish: Property = Property(name="specVanish", type=StringType)
WordprocessingMLStyles_RunPrElt_rtl: Property = Property(name="rtl", type=StringType)
WordprocessingMLStyles_RunPrElt_color: Property = Property(name="color", type=StringType)
WordprocessingMLStyles_RunPrElt_highlight: Property = Property(name="highlight", type=StringType)
WordprocessingMLStyles_RunPrElt_verticalAlign: Property = Property(name="verticalAlign", type=StringType)
WordprocessingMLStyles_RunPrElt.attributes={WordprocessingMLStyles_RunPrElt_vanish, WordprocessingMLStyles_RunPrElt_italic_cs, WordprocessingMLStyles_RunPrElt_rtl, WordprocessingMLStyles_RunPrElt_color, WordprocessingMLStyles_RunPrElt_outline, WordprocessingMLStyles_RunPrElt_emboss, WordprocessingMLStyles_RunPrElt_specVanish, WordprocessingMLStyles_RunPrElt_bold_cs, WordprocessingMLStyles_RunPrElt_imprint, WordprocessingMLStyles_RunPrElt_italic, WordprocessingMLStyles_RunPrElt_shadow, WordprocessingMLStyles_RunPrElt_strike, WordprocessingMLStyles_RunPrElt_noProof, WordprocessingMLStyles_RunPrElt_capitals, WordprocessingMLStyles_RunPrElt_doubleStrike, WordprocessingMLStyles_RunPrElt_smallCapitals, WordprocessingMLStyles_RunPrElt_bold, WordprocessingMLStyles_RunPrElt_verticalAlign, WordprocessingMLStyles_RunPrElt_highlight, WordprocessingMLStyles_RunPrElt_cs}

# RunElt class attributes and methods

# FontsElt class attributes and methods

# UnderlineProperty class attributes and methods

# LangElt class attributes and methods

# WordprocessingMLStyles_LangElt class attributes and methods
WordprocessingMLStyles_LangElt_val: Property = Property(name="val", type=StringType)
WordprocessingMLStyles_LangElt_bidi: Property = Property(name="bidi", type=StringType)
WordprocessingMLStyles_LangElt.attributes={WordprocessingMLStyles_LangElt_bidi, WordprocessingMLStyles_LangElt_val}

# WordprocessingMLStyles_RunContentElt class attributes and methods

# WordprocessingMLStyles_BreakElt class attributes and methods
WordprocessingMLStyles_BreakElt_type: Property = Property(name="type", type=StringType)
WordprocessingMLStyles_BreakElt.attributes={WordprocessingMLStyles_BreakElt_type}

# WordprocessingMLStyles_Text class attributes and methods

# WordprocessingMLStyles_DelText class attributes and methods

# WordprocessingMLStyles_InstrText class attributes and methods

# WordprocessingMLStyles_DelInstrText class attributes and methods

# WordprocessingMLStyles_NoBreakHyphen class attributes and methods

# WordprocessingMLStyles_SoftHyphen class attributes and methods

# WordprocessingMLStyles_AnnotationRef class attributes and methods

# WordprocessingMLStyles_FootnoteRef class attributes and methods

# WordprocessingMLStyles_EndnoteRef class attributes and methods

# WordprocessingMLStyles_Separator class attributes and methods

# WordprocessingMLStyles_ContinuationSeparator class attributes and methods

# WordprocessingMLStyles_PgNum class attributes and methods

# WordprocessingMLStyles_Cr class attributes and methods

# WordprocessingMLStyles_Footnote class attributes and methods

# FldCharElt class attributes and methods

# WordprocessingMLStyles_Endnote class attributes and methods

# WordprocessingMLStyles_NoteElt class attributes and methods
WordprocessingMLStyles_NoteElt_type: Property = Property(name="type", type=StringType)
WordprocessingMLStyles_NoteElt_suppressRef: Property = Property(name="suppressRef", type=StringType)
WordprocessingMLStyles_NoteElt.attributes={WordprocessingMLStyles_NoteElt_type, WordprocessingMLStyles_NoteElt_suppressRef}

# WordprocessingMLStyles_Picture class attributes and methods

# PictureType class attributes and methods

# WordprocessingMLStyles_Symbol class attributes and methods

# SymElt class attributes and methods

# WordprocessingMLStyles_SymElt class attributes and methods

# WordprocessingMLStyles_Tab class attributes and methods

# TabElt class attributes and methods

# WordprocessingMLStyles_FldChar class attributes and methods

# WordprocessingMLStyles_TableGridElt class attributes and methods

# WordprocessingMLStyles_FldCharElt class attributes and methods
WordprocessingMLStyles_FldCharElt_fldCharType: Property = Property(name="fldCharType", type=StringType)
WordprocessingMLStyles_FldCharElt_fldLock: Property = Property(name="fldLock", type=StringType)
WordprocessingMLStyles_FldCharElt.attributes={WordprocessingMLStyles_FldCharElt_fldLock, WordprocessingMLStyles_FldCharElt_fldCharType}

# WordprocessingMLStyles_TableElt class attributes and methods

# TablePrElt class attributes and methods

# TableGridElt class attributes and methods

# TableContentElt class attributes and methods

# WordprocessingMLStyles_TablePrElt class attributes and methods

# TableElt class attributes and methods

# WordprocessingMLStyles_TablePrExElt class attributes and methods

# WordprocessingMLStyles_TableContentElt class attributes and methods

# RowElt class attributes and methods

# RunLevelElt class attributes and methods

# WordprocessingMLStyles_RowElt class attributes and methods

# TablePrExElt class attributes and methods

# TableRowPrElt class attributes and methods

# RowContentElt class attributes and methods

# WordprocessingMLStyles_TableRowPrElt class attributes and methods

# WordprocessingMLStyles_RowContentElt class attributes and methods

# WordprocessingMLStyles_TableCellElt class attributes and methods

# TableCellPrElt class attributes and methods

# WordprocessingMLStyles_TableCellPrElt class attributes and methods

# WordprocessingMLStyles_FontsListElt class attributes and methods

# FontElt class attributes and methods

# WordprocessingMLStyles_FontsElt class attributes and methods
WordprocessingMLStyles_FontsElt_hint: Property = Property(name="hint", type=StringType)
WordprocessingMLStyles_FontsElt.attributes={WordprocessingMLStyles_FontsElt_hint}

# WordprocessingMLStyles_FontElt class attributes and methods

# WordprocessingMLStyles_StylesElt class attributes and methods
WordprocessingMLStyles_StylesElt_versionOfBuiltInStylenames: Property = Property(name="versionOfBuiltInStylenames", type=StringType)
WordprocessingMLStyles_StylesElt.attributes={WordprocessingMLStyles_StylesElt_versionOfBuiltInStylenames}

# WordprocessingMLStyles_StyleElt class attributes and methods
WordprocessingMLStyles_StyleElt_type: Property = Property(name="type", type=StringType)
WordprocessingMLStyles_StyleElt_default: Property = Property(name="default", type=StringType)
WordprocessingMLStyles_StyleElt_sti: Property = Property(name="sti", type=StringType)
WordprocessingMLStyles_StyleElt_autoRedefine: Property = Property(name="autoRedefine", type=StringType)
WordprocessingMLStyles_StyleElt_hidden: Property = Property(name="hidden", type=StringType)
WordprocessingMLStyles_StyleElt_semiHidden: Property = Property(name="semiHidden", type=StringType)
WordprocessingMLStyles_StyleElt_locked: Property = Property(name="locked", type=StringType)
WordprocessingMLStyles_StyleElt_personal: Property = Property(name="personal", type=StringType)
WordprocessingMLStyles_StyleElt_personalCompose: Property = Property(name="personalCompose", type=StringType)
WordprocessingMLStyles_StyleElt_personalReply: Property = Property(name="personalReply", type=StringType)
WordprocessingMLStyles_StyleElt.attributes={WordprocessingMLStyles_StyleElt_personal, WordprocessingMLStyles_StyleElt_default, WordprocessingMLStyles_StyleElt_personalCompose, WordprocessingMLStyles_StyleElt_semiHidden, WordprocessingMLStyles_StyleElt_sti, WordprocessingMLStyles_StyleElt_type, WordprocessingMLStyles_StyleElt_hidden, WordprocessingMLStyles_StyleElt_autoRedefine, WordprocessingMLStyles_StyleElt_personalReply, WordprocessingMLStyles_StyleElt_locked}

# WordprocessingMLStyles_ListsElt class attributes and methods

# WordprocessingMLStyles_SectPrElt class attributes and methods

# WordprocessingMLStyles_RunLevelElt class attributes and methods

# WordprocessingMLStyles_CfChunk class attributes and methods

# WordprocessingMLStyles_SimpleFieldElt class attributes and methods

# WordprocessingMLStyles_HLinkElt class attributes and methods

# WordprocessingMLStyles_SubDocElt class attributes and methods

# WordprocessingMLStyles_PictureType class attributes and methods

# WordprocessingMLStyles_TabElt class attributes and methods

# Relationships
value0: BinaryAssociation = BinaryAssociation(
    name="value0",
    ends={
        Property(name="WordprocessingMLStyles_DateTimeTypeValue", type=DateTimeType, multiplicity=Multiplicity(1, 1)),
        Property(name="DateTimeType", type=WordprocessingMLStyles_DateTimeTypeValue, multiplicity=Multiplicity(1, 1))
    }
)
dp_wordDocument1: BinaryAssociation = BinaryAssociation(
    name="dp_wordDocument1",
    ends={
        Property(name="WordDocument", type=WordprocessingMLStyles_DocumentPropertiesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="wd_docProperties", type=WordDocument, multiplicity=Multiplicity(1, 1))
    }
)
lastPrinted3: BinaryAssociation = BinaryAssociation(
    name="lastPrinted3",
    ends={
        Property(name="DateTimeType5", type=WordprocessingMLStyles_DocumentPropertiesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="WordprocessingMLStyles_DocumentPropertiesCollection4", type=DateTimeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
created6: BinaryAssociation = BinaryAssociation(
    name="created6",
    ends={
        Property(name="DateTimeType8", type=WordprocessingMLStyles_DocumentPropertiesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="WordprocessingMLStyles_DocumentPropertiesCollection7", type=DateTimeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lastSaved9: BinaryAssociation = BinaryAssociation(
    name="lastSaved9",
    ends={
        Property(name="DateTimeType11", type=WordprocessingMLStyles_DocumentPropertiesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="WordprocessingMLStyles_DocumentPropertiesCollection10", type=DateTimeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cdp_wordDocument12: BinaryAssociation = BinaryAssociation(
    name="cdp_wordDocument12",
    ends={
        Property(name="WordDocument13", type=WordprocessingMLStyles_CustomDocumentPropertiesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="wd_customDocProperties", type=WordDocument, multiplicity=Multiplicity(1, 1))
    }
)
customDocumentProperties14: BinaryAssociation = BinaryAssociation(
    name="customDocumentProperties14",
    ends={
        Property(name="CustomDocumentProperty", type=WordprocessingMLStyles_CustomDocumentPropertiesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="customDocumentProperty_cdpe", type=CustomDocumentProperty, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
customDocumentProperty_cdpe15: BinaryAssociation = BinaryAssociation(
    name="customDocumentProperty_cdpe15",
    ends={
        Property(name="CustomDocumentPropertiesCollection", type=WordprocessingMLStyles_CustomDocumentProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="customDocumentProperties", type=CustomDocumentPropertiesCollection, multiplicity=Multiplicity(1, 1))
    }
)
version2: BinaryAssociation = BinaryAssociation(
    name="version2",
    ends={
        Property(name="VersionType", type=WordprocessingMLStyles_DocumentPropertiesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="WordprocessingMLStyles_DocumentPropertiesCollection", type=VersionType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
smartTagType_ste17: BinaryAssociation = BinaryAssociation(
    name="smartTagType_ste17",
    ends={
        Property(name="SmartTagsCollection", type=WordprocessingMLStyles_SmartTagType, multiplicity=Multiplicity(1, 1)),
        Property(name="smartTagTypes", type=SmartTagsCollection, multiplicity=Multiplicity(1, 1))
    }
)
st_wordDocument18: BinaryAssociation = BinaryAssociation(
    name="st_wordDocument18",
    ends={
        Property(name="WordDocument19", type=WordprocessingMLStyles_SmartTagsCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="wd_smartTags", type=WordDocument, multiplicity=Multiplicity(1, 1))
    }
)
smartTagTypes20: BinaryAssociation = BinaryAssociation(
    name="smartTagTypes20",
    ends={
        Property(name="SmartTagType", type=WordprocessingMLStyles_SmartTagsCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="smartTagType_ste", type=SmartTagType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value16: BinaryAssociation = BinaryAssociation(
    name="value16",
    ends={
        Property(name="ValueType", type=WordprocessingMLStyles_CustomDocumentProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="WordprocessingMLStyles_CustomDocumentProperty", type=ValueType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
wd_smartTags21: BinaryAssociation = BinaryAssociation(
    name="wd_smartTags21",
    ends={
        Property(name="SmartTagsCollection22", type=WordprocessingMLStyles_WordDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="st_wordDocument", type=SmartTagsCollection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
wd_docProperties23: BinaryAssociation = BinaryAssociation(
    name="wd_docProperties23",
    ends={
        Property(name="DocumentPropertiesCollection", type=WordprocessingMLStyles_WordDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="dp_wordDocument", type=DocumentPropertiesCollection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
wd_customDocProperties24: BinaryAssociation = BinaryAssociation(
    name="wd_customDocProperties24",
    ends={
        Property(name="CustomDocumentPropertiesCollection25", type=WordprocessingMLStyles_WordDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="cdp_wordDocument", type=CustomDocumentPropertiesCollection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ignoreSubtree26: BinaryAssociation = BinaryAssociation(
    name="ignoreSubtree26",
    ends={
        Property(name="StringProperty", type=WordprocessingMLStyles_WordDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="WordprocessingMLStyles_WordDocument", type=StringProperty, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ignoreElements27: BinaryAssociation = BinaryAssociation(
    name="ignoreElements27",
    ends={
        Property(name="StringProperty29", type=WordprocessingMLStyles_WordDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="WordprocessingMLStyles_WordDocument28", type=StringProperty, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fonts30: BinaryAssociation = BinaryAssociation(
    name="fonts30",
    ends={
        Property(name="FontsListElt", type=WordprocessingMLStyles_WordDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="fle_wordDocument", type=FontsListElt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lists31: BinaryAssociation = BinaryAssociation(
    name="lists31",
    ends={
        Property(name="ListsElt", type=WordprocessingMLStyles_WordDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="le_wordDocument", type=ListsElt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pContentElts46: BinaryAssociation = BinaryAssociation(
    name="pContentElts46",
    ends={
        Property(name="ParaContentElt", type=WordprocessingMLStyles_ParaElt, multiplicity=Multiplicity(1, 1)),
        Property(name="pce_pElt", type=ParaContentElt, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body34: BinaryAssociation = BinaryAssociation(
    name="body34",
    ends={
        Property(name="BodyElt", type=WordprocessingMLStyles_WordDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="be_wordDocument", type=BodyElt, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
dpe_wordDocument35: BinaryAssociation = BinaryAssociation(
    name="dpe_wordDocument35",
    ends={
        Property(name="WordDocument36", type=WordprocessingMLStyles_DocPrElt, multiplicity=Multiplicity(1, 1)),
        Property(name="docPr", type=WordDocument, multiplicity=Multiplicity(1, 1))
    }
)
be_wordDocument37: BinaryAssociation = BinaryAssociation(
    name="be_wordDocument37",
    ends={
        Property(name="WordDocument38", type=WordprocessingMLStyles_BodyElt, multiplicity=Multiplicity(1, 1)),
        Property(name="body", type=WordDocument, multiplicity=Multiplicity(1, 1))
    }
)
blockLevelElts39: BinaryAssociation = BinaryAssociation(
    name="blockLevelElts39",
    ends={
        Property(name="BlockLevelElt", type=WordprocessingMLStyles_BodyElt, multiplicity=Multiplicity(1, 1)),
        Property(name="ble_bodyElt", type=BlockLevelElt, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sectPr40: BinaryAssociation = BinaryAssociation(
    name="sectPr40",
    ends={
        Property(name="SectPrElt", type=WordprocessingMLStyles_BodyElt, multiplicity=Multiplicity(1, 1)),
        Property(name="spe_bodyElt", type=SectPrElt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ble_bodyElt41: BinaryAssociation = BinaryAssociation(
    name="ble_bodyElt41",
    ends={
        Property(name="BodyElt42", type=WordprocessingMLStyles_BlockLevelElt, multiplicity=Multiplicity(1, 1)),
        Property(name="blockLevelElts", type=BodyElt, multiplicity=Multiplicity(1, 1))
    }
)
ble_note43: BinaryAssociation = BinaryAssociation(
    name="ble_note43",
    ends={
        Property(name="NoteElt", type=WordprocessingMLStyles_BlockLevelElt, multiplicity=Multiplicity(1, 1)),
        Property(name="n_blockLevelElts", type=NoteElt, multiplicity=Multiplicity(1, 1))
    }
)
ble_tableCellElt44: BinaryAssociation = BinaryAssociation(
    name="ble_tableCellElt44",
    ends={
        Property(name="TableCellElt", type=WordprocessingMLStyles_BlockLevelElt, multiplicity=Multiplicity(1, 1)),
        Property(name="tce_content", type=TableCellElt, multiplicity=Multiplicity(1, 1))
    }
)
styles32: BinaryAssociation = BinaryAssociation(
    name="styles32",
    ends={
        Property(name="StylesElt", type=WordprocessingMLStyles_WordDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="se_wordDocument", type=StylesElt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
docPr33: BinaryAssociation = BinaryAssociation(
    name="docPr33",
    ends={
        Property(name="DocPrElt", type=WordprocessingMLStyles_WordDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="dpe_wordDocument", type=DocPrElt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pPr45: BinaryAssociation = BinaryAssociation(
    name="pPr45",
    ends={
        Property(name="ParaPrElt", type=WordprocessingMLStyles_ParaElt, multiplicity=Multiplicity(1, 1)),
        Property(name="ppe_pElt", type=ParaPrElt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ppe_pElt47: BinaryAssociation = BinaryAssociation(
    name="ppe_pElt47",
    ends={
        Property(name="ParaElt", type=WordprocessingMLStyles_ParaPrElt, multiplicity=Multiplicity(1, 1)),
        Property(name="pPr", type=ParaElt, multiplicity=Multiplicity(1, 1))
    }
)
ppe_styleElt48: BinaryAssociation = BinaryAssociation(
    name="ppe_styleElt48",
    ends={
        Property(name="StyleElt", type=WordprocessingMLStyles_ParaPrElt, multiplicity=Multiplicity(1, 1)),
        Property(name="se_pPr", type=StyleElt, multiplicity=Multiplicity(1, 1))
    }
)
pStyle49: BinaryAssociation = BinaryAssociation(
    name="pStyle49",
    ends={
        Property(name="StringProperty50", type=WordprocessingMLStyles_ParaPrElt, multiplicity=Multiplicity(1, 1)),
        Property(name="WordprocessingMLStyles_ParaPrElt", type=StringProperty, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pce_pElt51: BinaryAssociation = BinaryAssociation(
    name="pce_pElt51",
    ends={
        Property(name="ParaElt52", type=WordprocessingMLStyles_ParaContentElt, multiplicity=Multiplicity(1, 1)),
        Property(name="pContentElts", type=ParaElt, multiplicity=Multiplicity(1, 1))
    }
)
rPr53: BinaryAssociation = BinaryAssociation(
    name="rPr53",
    ends={
        Property(name="RunPrElt", type=WordprocessingMLStyles_RunElt, multiplicity=Multiplicity(1, 1)),
        Property(name="rpe_rElt", type=RunPrElt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rContentElts54: BinaryAssociation = BinaryAssociation(
    name="rContentElts54",
    ends={
        Property(name="RunContentElt", type=WordprocessingMLStyles_RunElt, multiplicity=Multiplicity(1, 1)),
        Property(name="rce_rElt", type=RunContentElt, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rpe_rElt55: BinaryAssociation = BinaryAssociation(
    name="rpe_rElt55",
    ends={
        Property(name="RunElt", type=WordprocessingMLStyles_RunPrElt, multiplicity=Multiplicity(1, 1)),
        Property(name="rPr", type=RunElt, multiplicity=Multiplicity(1, 1))
    }
)
rpe_styleElt56: BinaryAssociation = BinaryAssociation(
    name="rpe_styleElt56",
    ends={
        Property(name="StyleElt57", type=WordprocessingMLStyles_RunPrElt, multiplicity=Multiplicity(1, 1)),
        Property(name="se_rPr", type=StyleElt, multiplicity=Multiplicity(1, 1))
    }
)
rStyle58: BinaryAssociation = BinaryAssociation(
    name="rStyle58",
    ends={
        Property(name="StringProperty59", type=WordprocessingMLStyles_RunPrElt, multiplicity=Multiplicity(1, 1)),
        Property(name="WordprocessingMLStyles_RunPrElt", type=StringProperty, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rFonts60: BinaryAssociation = BinaryAssociation(
    name="rFonts60",
    ends={
        Property(name="FontsElt", type=WordprocessingMLStyles_RunPrElt, multiplicity=Multiplicity(1, 1)),
        Property(name="fse_runPrElt", type=FontsElt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
underline61: BinaryAssociation = BinaryAssociation(
    name="underline61",
    ends={
        Property(name="UnderlineProperty", type=WordprocessingMLStyles_RunPrElt, multiplicity=Multiplicity(1, 1)),
        Property(name="WordprocessingMLStyles_RunPrElt62", type=UnderlineProperty, multiplicity=Multiplicity(0, 1))
    }
)
language63: BinaryAssociation = BinaryAssociation(
    name="language63",
    ends={
        Property(name="LangElt", type=WordprocessingMLStyles_RunPrElt, multiplicity=Multiplicity(1, 1)),
        Property(name="le_runPrElt", type=LangElt, multiplicity=Multiplicity(0, 1))
    }
)
le_runPrElt64: BinaryAssociation = BinaryAssociation(
    name="le_runPrElt64",
    ends={
        Property(name="RunPrElt65", type=WordprocessingMLStyles_LangElt, multiplicity=Multiplicity(1, 1)),
        Property(name="language", type=RunPrElt, multiplicity=Multiplicity(1, 1))
    }
)
rce_rElt66: BinaryAssociation = BinaryAssociation(
    name="rce_rElt66",
    ends={
        Property(name="RunElt67", type=WordprocessingMLStyles_RunContentElt, multiplicity=Multiplicity(1, 1)),
        Property(name="rContentElts", type=RunElt, multiplicity=Multiplicity(1, 1))
    }
)
n_blockLevelElts68: BinaryAssociation = BinaryAssociation(
    name="n_blockLevelElts68",
    ends={
        Property(name="BlockLevelElt69", type=WordprocessingMLStyles_NoteElt, multiplicity=Multiplicity(1, 1)),
        Property(name="ble_note", type=BlockLevelElt, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
font70: BinaryAssociation = BinaryAssociation(
    name="font70",
    ends={
        Property(name="StringType", type=WordprocessingMLStyles_SymElt, multiplicity=Multiplicity(1, 1)),
        Property(name="WordprocessingMLStyles_SymElt", type=StringType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
char71: BinaryAssociation = BinaryAssociation(
    name="char71",
    ends={
        Property(name="StringType73", type=WordprocessingMLStyles_SymElt, multiplicity=Multiplicity(1, 1)),
        Property(name="WordprocessingMLStyles_SymElt72", type=StringType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
fldData74: BinaryAssociation = BinaryAssociation(
    name="fldData74",
    ends={
        Property(name="StringType75", type=WordprocessingMLStyles_FldCharElt, multiplicity=Multiplicity(1, 1)),
        Property(name="WordprocessingMLStyles_FldCharElt", type=StringType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tblPr76: BinaryAssociation = BinaryAssociation(
    name="tblPr76",
    ends={
        Property(name="TablePrElt", type=WordprocessingMLStyles_TableElt, multiplicity=Multiplicity(1, 1)),
        Property(name="tpe_tblElt", type=TablePrElt, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tblGrid77: BinaryAssociation = BinaryAssociation(
    name="tblGrid77",
    ends={
        Property(name="TableGridElt", type=WordprocessingMLStyles_TableElt, multiplicity=Multiplicity(1, 1)),
        Property(name="tge_tblElt", type=TableGridElt, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tblContent78: BinaryAssociation = BinaryAssociation(
    name="tblContent78",
    ends={
        Property(name="TableContentElt", type=WordprocessingMLStyles_TableElt, multiplicity=Multiplicity(1, 1)),
        Property(name="tce_tblElt", type=TableContentElt, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
tpe_tblElt79: BinaryAssociation = BinaryAssociation(
    name="tpe_tblElt79",
    ends={
        Property(name="TableElt", type=WordprocessingMLStyles_TablePrElt, multiplicity=Multiplicity(1, 1)),
        Property(name="tblPr", type=TableElt, multiplicity=Multiplicity(1, 1))
    }
)
tpe_styleElt80: BinaryAssociation = BinaryAssociation(
    name="tpe_styleElt80",
    ends={
        Property(name="StyleElt81", type=WordprocessingMLStyles_TablePrElt, multiplicity=Multiplicity(1, 1)),
        Property(name="se_tblPr", type=StyleElt, multiplicity=Multiplicity(1, 1))
    }
)
tge_tblElt82: BinaryAssociation = BinaryAssociation(
    name="tge_tblElt82",
    ends={
        Property(name="TableElt83", type=WordprocessingMLStyles_TableGridElt, multiplicity=Multiplicity(1, 1)),
        Property(name="tblGrid", type=TableElt, multiplicity=Multiplicity(1, 1))
    }
)
tce_tblElt84: BinaryAssociation = BinaryAssociation(
    name="tce_tblElt84",
    ends={
        Property(name="TableElt85", type=WordprocessingMLStyles_TableContentElt, multiplicity=Multiplicity(1, 1)),
        Property(name="tblContent", type=TableElt, multiplicity=Multiplicity(1, 1))
    }
)
tr86: BinaryAssociation = BinaryAssociation(
    name="tr86",
    ends={
        Property(name="RowElt", type=WordprocessingMLStyles_TableContentElt, multiplicity=Multiplicity(1, 1)),
        Property(name="re_tblContentElt", type=RowElt, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tce_runLevelElts87: BinaryAssociation = BinaryAssociation(
    name="tce_runLevelElts87",
    ends={
        Property(name="RunLevelElt", type=WordprocessingMLStyles_TableContentElt, multiplicity=Multiplicity(1, 1)),
        Property(name="rle_tblContentElt", type=RunLevelElt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
re_tblContentElt88: BinaryAssociation = BinaryAssociation(
    name="re_tblContentElt88",
    ends={
        Property(name="TableContentElt89", type=WordprocessingMLStyles_RowElt, multiplicity=Multiplicity(1, 1)),
        Property(name="tr", type=TableContentElt, multiplicity=Multiplicity(1, 1))
    }
)
tblPrEx90: BinaryAssociation = BinaryAssociation(
    name="tblPrEx90",
    ends={
        Property(name="TablePrExElt", type=WordprocessingMLStyles_RowElt, multiplicity=Multiplicity(1, 1)),
        Property(name="tpee_rowElt", type=TablePrExElt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
trPr91: BinaryAssociation = BinaryAssociation(
    name="trPr91",
    ends={
        Property(name="TableRowPrElt", type=WordprocessingMLStyles_RowElt, multiplicity=Multiplicity(1, 1)),
        Property(name="tpe_rowElt", type=TableRowPrElt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rowContent92: BinaryAssociation = BinaryAssociation(
    name="rowContent92",
    ends={
        Property(name="RowContentElt", type=WordprocessingMLStyles_RowElt, multiplicity=Multiplicity(1, 1)),
        Property(name="rce_rowElt", type=RowContentElt, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
tcPr107: BinaryAssociation = BinaryAssociation(
    name="tcPr107",
    ends={
        Property(name="TableCellPrElt", type=WordprocessingMLStyles_TableCellElt, multiplicity=Multiplicity(1, 1)),
        Property(name="tcpe_tableCellElt", type=TableCellPrElt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tpee_rowElt93: BinaryAssociation = BinaryAssociation(
    name="tpee_rowElt93",
    ends={
        Property(name="RowElt94", type=WordprocessingMLStyles_TablePrExElt, multiplicity=Multiplicity(1, 1)),
        Property(name="tblPrEx", type=RowElt, multiplicity=Multiplicity(1, 1))
    }
)
tpe_rowElt95: BinaryAssociation = BinaryAssociation(
    name="tpe_rowElt95",
    ends={
        Property(name="RowElt96", type=WordprocessingMLStyles_TableRowPrElt, multiplicity=Multiplicity(1, 1)),
        Property(name="trPr", type=RowElt, multiplicity=Multiplicity(1, 1))
    }
)
trpe_styleElt97: BinaryAssociation = BinaryAssociation(
    name="trpe_styleElt97",
    ends={
        Property(name="StyleElt98", type=WordprocessingMLStyles_TableRowPrElt, multiplicity=Multiplicity(1, 1)),
        Property(name="se_trPr", type=StyleElt, multiplicity=Multiplicity(1, 1))
    }
)
rce_rowElt99: BinaryAssociation = BinaryAssociation(
    name="rce_rowElt99",
    ends={
        Property(name="RowElt100", type=WordprocessingMLStyles_RowContentElt, multiplicity=Multiplicity(1, 1)),
        Property(name="rowContent", type=RowElt, multiplicity=Multiplicity(1, 1))
    }
)
tc101: BinaryAssociation = BinaryAssociation(
    name="tc101",
    ends={
        Property(name="TableCellElt102", type=WordprocessingMLStyles_RowContentElt, multiplicity=Multiplicity(1, 1)),
        Property(name="tce_rowContentElt", type=TableCellElt, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rce_runLevelElts103: BinaryAssociation = BinaryAssociation(
    name="rce_runLevelElts103",
    ends={
        Property(name="RunLevelElt104", type=WordprocessingMLStyles_RowContentElt, multiplicity=Multiplicity(1, 1)),
        Property(name="rle_rowContentElt", type=RunLevelElt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tce_rowContentElt105: BinaryAssociation = BinaryAssociation(
    name="tce_rowContentElt105",
    ends={
        Property(name="RowContentElt106", type=WordprocessingMLStyles_TableCellElt, multiplicity=Multiplicity(1, 1)),
        Property(name="tc", type=RowContentElt, multiplicity=Multiplicity(1, 1))
    }
)
tce_content108: BinaryAssociation = BinaryAssociation(
    name="tce_content108",
    ends={
        Property(name="BlockLevelElt109", type=WordprocessingMLStyles_TableCellElt, multiplicity=Multiplicity(1, 1)),
        Property(name="ble_tableCellElt", type=BlockLevelElt, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
tcpe_tableCellElt110: BinaryAssociation = BinaryAssociation(
    name="tcpe_tableCellElt110",
    ends={
        Property(name="TableCellElt111", type=WordprocessingMLStyles_TableCellPrElt, multiplicity=Multiplicity(1, 1)),
        Property(name="tcPr", type=TableCellElt, multiplicity=Multiplicity(1, 1))
    }
)
tcpe_styleElt112: BinaryAssociation = BinaryAssociation(
    name="tcpe_styleElt112",
    ends={
        Property(name="StyleElt113", type=WordprocessingMLStyles_TableCellPrElt, multiplicity=Multiplicity(1, 1)),
        Property(name="se_tcPr", type=StyleElt, multiplicity=Multiplicity(1, 1))
    }
)
fle_wordDocument114: BinaryAssociation = BinaryAssociation(
    name="fle_wordDocument114",
    ends={
        Property(name="WordDocument115", type=WordprocessingMLStyles_FontsListElt, multiplicity=Multiplicity(1, 1)),
        Property(name="fonts", type=WordDocument, multiplicity=Multiplicity(1, 1))
    }
)
defaultFonts116: BinaryAssociation = BinaryAssociation(
    name="defaultFonts116",
    ends={
        Property(name="FontsElt117", type=WordprocessingMLStyles_FontsListElt, multiplicity=Multiplicity(1, 1)),
        Property(name="fse_fontsListElt", type=FontsElt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fonts118: BinaryAssociation = BinaryAssociation(
    name="fonts118",
    ends={
        Property(name="FontElt", type=WordprocessingMLStyles_FontsListElt, multiplicity=Multiplicity(1, 1)),
        Property(name="fe_fontsListElt", type=FontElt, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fse_fontsListElt119: BinaryAssociation = BinaryAssociation(
    name="fse_fontsListElt119",
    ends={
        Property(name="FontsListElt120", type=WordprocessingMLStyles_FontsElt, multiplicity=Multiplicity(1, 1)),
        Property(name="defaultFonts", type=FontsListElt, multiplicity=Multiplicity(1, 1))
    }
)
fse_runPrElt121: BinaryAssociation = BinaryAssociation(
    name="fse_runPrElt121",
    ends={
        Property(name="RunPrElt122", type=WordprocessingMLStyles_FontsElt, multiplicity=Multiplicity(1, 1)),
        Property(name="rFonts", type=RunPrElt, multiplicity=Multiplicity(1, 1))
    }
)
ascii123: BinaryAssociation = BinaryAssociation(
    name="ascii123",
    ends={
        Property(name="StringType124", type=WordprocessingMLStyles_FontsElt, multiplicity=Multiplicity(1, 1)),
        Property(name="WordprocessingMLStyles_FontsElt", type=StringType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
h_ansi125: BinaryAssociation = BinaryAssociation(
    name="h_ansi125",
    ends={
        Property(name="StringType127", type=WordprocessingMLStyles_FontsElt, multiplicity=Multiplicity(1, 1)),
        Property(name="WordprocessingMLStyles_FontsElt126", type=StringType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
fareast128: BinaryAssociation = BinaryAssociation(
    name="fareast128",
    ends={
        Property(name="StringType130", type=WordprocessingMLStyles_FontsElt, multiplicity=Multiplicity(1, 1)),
        Property(name="WordprocessingMLStyles_FontsElt129", type=StringType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
cs131: BinaryAssociation = BinaryAssociation(
    name="cs131",
    ends={
        Property(name="StringType133", type=WordprocessingMLStyles_FontsElt, multiplicity=Multiplicity(1, 1)),
        Property(name="WordprocessingMLStyles_FontsElt132", type=StringType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
fe_fontsListElt134: BinaryAssociation = BinaryAssociation(
    name="fe_fontsListElt134",
    ends={
        Property(name="FontsListElt136", type=WordprocessingMLStyles_FontElt, multiplicity=Multiplicity(1, 1)),
        Property(name="fonts135", type=FontsListElt, multiplicity=Multiplicity(1, 1))
    }
)
name137: BinaryAssociation = BinaryAssociation(
    name="name137",
    ends={
        Property(name="StringType138", type=WordprocessingMLStyles_FontElt, multiplicity=Multiplicity(1, 1)),
        Property(name="WordprocessingMLStyles_FontElt", type=StringType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
altName139: BinaryAssociation = BinaryAssociation(
    name="altName139",
    ends={
        Property(name="StringProperty141", type=WordprocessingMLStyles_FontElt, multiplicity=Multiplicity(1, 1)),
        Property(name="WordprocessingMLStyles_FontElt140", type=StringProperty, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
se_wordDocument142: BinaryAssociation = BinaryAssociation(
    name="se_wordDocument142",
    ends={
        Property(name="WordDocument143", type=WordprocessingMLStyles_StylesElt, multiplicity=Multiplicity(1, 1)),
        Property(name="styles", type=WordDocument, multiplicity=Multiplicity(1, 1))
    }
)
styles144: BinaryAssociation = BinaryAssociation(
    name="styles144",
    ends={
        Property(name="StyleElt145", type=WordprocessingMLStyles_StylesElt, multiplicity=Multiplicity(1, 1)),
        Property(name="se_stylesElt", type=StyleElt, multiplicity=Multiplicity(0, 9999))
    }
)
se_stylesElt146: BinaryAssociation = BinaryAssociation(
    name="se_stylesElt146",
    ends={
        Property(name="StylesElt148", type=WordprocessingMLStyles_StyleElt, multiplicity=Multiplicity(1, 1)),
        Property(name="styles147", type=StylesElt, multiplicity=Multiplicity(1, 1))
    }
)
styleId149: BinaryAssociation = BinaryAssociation(
    name="styleId149",
    ends={
        Property(name="StringType150", type=WordprocessingMLStyles_StyleElt, multiplicity=Multiplicity(1, 1)),
        Property(name="WordprocessingMLStyles_StyleElt", type=StringType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name151: BinaryAssociation = BinaryAssociation(
    name="name151",
    ends={
        Property(name="StringProperty153", type=WordprocessingMLStyles_StyleElt, multiplicity=Multiplicity(1, 1)),
        Property(name="WordprocessingMLStyles_StyleElt152", type=StringProperty, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
aliases154: BinaryAssociation = BinaryAssociation(
    name="aliases154",
    ends={
        Property(name="StringProperty156", type=WordprocessingMLStyles_StyleElt, multiplicity=Multiplicity(1, 1)),
        Property(name="WordprocessingMLStyles_StyleElt155", type=StringProperty, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
basedOn157: BinaryAssociation = BinaryAssociation(
    name="basedOn157",
    ends={
        Property(name="StringProperty159", type=WordprocessingMLStyles_StyleElt, multiplicity=Multiplicity(1, 1)),
        Property(name="WordprocessingMLStyles_StyleElt158", type=StringProperty, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
se_rPr171: BinaryAssociation = BinaryAssociation(
    name="se_rPr171",
    ends={
        Property(name="RunPrElt172", type=WordprocessingMLStyles_StyleElt, multiplicity=Multiplicity(1, 1)),
        Property(name="rpe_styleElt", type=RunPrElt, multiplicity=Multiplicity(0, 1))
    }
)
next160: BinaryAssociation = BinaryAssociation(
    name="next160",
    ends={
        Property(name="StringProperty162", type=WordprocessingMLStyles_StyleElt, multiplicity=Multiplicity(1, 1)),
        Property(name="WordprocessingMLStyles_StyleElt161", type=StringProperty, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
link163: BinaryAssociation = BinaryAssociation(
    name="link163",
    ends={
        Property(name="StringProperty165", type=WordprocessingMLStyles_StyleElt, multiplicity=Multiplicity(1, 1)),
        Property(name="WordprocessingMLStyles_StyleElt164", type=StringProperty, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rsid166: BinaryAssociation = BinaryAssociation(
    name="rsid166",
    ends={
        Property(name="StringType168", type=WordprocessingMLStyles_StyleElt, multiplicity=Multiplicity(1, 1)),
        Property(name="WordprocessingMLStyles_StyleElt167", type=StringType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
se_pPr169: BinaryAssociation = BinaryAssociation(
    name="se_pPr169",
    ends={
        Property(name="ParaPrElt170", type=WordprocessingMLStyles_StyleElt, multiplicity=Multiplicity(1, 1)),
        Property(name="ppe_styleElt", type=ParaPrElt, multiplicity=Multiplicity(0, 1))
    }
)
se_tblPr173: BinaryAssociation = BinaryAssociation(
    name="se_tblPr173",
    ends={
        Property(name="TablePrElt174", type=WordprocessingMLStyles_StyleElt, multiplicity=Multiplicity(1, 1)),
        Property(name="tpe_styleElt", type=TablePrElt, multiplicity=Multiplicity(0, 1))
    }
)
se_trPr175: BinaryAssociation = BinaryAssociation(
    name="se_trPr175",
    ends={
        Property(name="TableRowPrElt176", type=WordprocessingMLStyles_StyleElt, multiplicity=Multiplicity(1, 1)),
        Property(name="trpe_styleElt", type=TableRowPrElt, multiplicity=Multiplicity(0, 1))
    }
)
se_tcPr177: BinaryAssociation = BinaryAssociation(
    name="se_tcPr177",
    ends={
        Property(name="TableCellPrElt178", type=WordprocessingMLStyles_StyleElt, multiplicity=Multiplicity(1, 1)),
        Property(name="tcpe_styleElt", type=TableCellPrElt, multiplicity=Multiplicity(0, 1))
    }
)
le_wordDocument179: BinaryAssociation = BinaryAssociation(
    name="le_wordDocument179",
    ends={
        Property(name="WordDocument180", type=WordprocessingMLStyles_ListsElt, multiplicity=Multiplicity(1, 1)),
        Property(name="lists", type=WordDocument, multiplicity=Multiplicity(1, 1))
    }
)
spe_bodyElt181: BinaryAssociation = BinaryAssociation(
    name="spe_bodyElt181",
    ends={
        Property(name="BodyElt182", type=WordprocessingMLStyles_SectPrElt, multiplicity=Multiplicity(1, 1)),
        Property(name="sectPr", type=BodyElt, multiplicity=Multiplicity(1, 1))
    }
)
rle_tblContentElt183: BinaryAssociation = BinaryAssociation(
    name="rle_tblContentElt183",
    ends={
        Property(name="TableContentElt184", type=WordprocessingMLStyles_RunLevelElt, multiplicity=Multiplicity(1, 1)),
        Property(name="tce_runLevelElts", type=TableContentElt, multiplicity=Multiplicity(1, 1))
    }
)
rle_rowContentElt185: BinaryAssociation = BinaryAssociation(
    name="rle_rowContentElt185",
    ends={
        Property(name="RowContentElt186", type=WordprocessingMLStyles_RunLevelElt, multiplicity=Multiplicity(1, 1)),
        Property(name="rce_runLevelElts", type=RowContentElt, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_WordprocessingMLStyles_BooleanValue_ValueType = Generalization(general=ValueType, specific=WordprocessingMLStyles_BooleanValue)
gen_WordprocessingMLStyles_StringValue_ValueType = Generalization(general=ValueType, specific=WordprocessingMLStyles_StringValue)
gen_WordprocessingMLStyles_FloatValue_ValueType = Generalization(general=ValueType, specific=WordprocessingMLStyles_FloatValue)
gen_WordprocessingMLStyles_DateTimeTypeValue_ValueType = Generalization(general=ValueType, specific=WordprocessingMLStyles_DateTimeTypeValue)
gen_WordprocessingMLStyles_StringProperty_StringType = Generalization(general=StringType, specific=WordprocessingMLStyles_StringProperty)
gen_WordprocessingMLStyles_BlockLevelChunkElt_BlockLevelElt = Generalization(general=BlockLevelElt, specific=WordprocessingMLStyles_BlockLevelChunkElt)
gen_WordprocessingMLStyles_ParaElt_BlockLevelChunkElt = Generalization(general=BlockLevelChunkElt, specific=WordprocessingMLStyles_ParaElt)
gen_WordprocessingMLStyles_RunElt_ParaContentElt = Generalization(general=ParaContentElt, specific=WordprocessingMLStyles_RunElt)
gen_WordprocessingMLStyles_BreakElt_RunContentElt = Generalization(general=RunContentElt, specific=WordprocessingMLStyles_BreakElt)
gen_WordprocessingMLStyles_Text_RunContentElt = Generalization(general=RunContentElt, specific=WordprocessingMLStyles_Text)
gen_WordprocessingMLStyles_Text_StringType = Generalization(general=StringType, specific=WordprocessingMLStyles_Text)
gen_WordprocessingMLStyles_DelText_RunContentElt = Generalization(general=RunContentElt, specific=WordprocessingMLStyles_DelText)
gen_WordprocessingMLStyles_DelText_StringType = Generalization(general=StringType, specific=WordprocessingMLStyles_DelText)
gen_WordprocessingMLStyles_InstrText_RunContentElt = Generalization(general=RunContentElt, specific=WordprocessingMLStyles_InstrText)
gen_WordprocessingMLStyles_InstrText_StringType = Generalization(general=StringType, specific=WordprocessingMLStyles_InstrText)
gen_WordprocessingMLStyles_DelInstrText_RunContentElt = Generalization(general=RunContentElt, specific=WordprocessingMLStyles_DelInstrText)
gen_WordprocessingMLStyles_DelInstrText_StringType = Generalization(general=StringType, specific=WordprocessingMLStyles_DelInstrText)
gen_WordprocessingMLStyles_NoBreakHyphen_RunContentElt = Generalization(general=RunContentElt, specific=WordprocessingMLStyles_NoBreakHyphen)
gen_WordprocessingMLStyles_SoftHyphen_RunContentElt = Generalization(general=RunContentElt, specific=WordprocessingMLStyles_SoftHyphen)
gen_WordprocessingMLStyles_AnnotationRef_RunContentElt = Generalization(general=RunContentElt, specific=WordprocessingMLStyles_AnnotationRef)
gen_WordprocessingMLStyles_FootnoteRef_RunContentElt = Generalization(general=RunContentElt, specific=WordprocessingMLStyles_FootnoteRef)
gen_WordprocessingMLStyles_EndnoteRef_RunContentElt = Generalization(general=RunContentElt, specific=WordprocessingMLStyles_EndnoteRef)
gen_WordprocessingMLStyles_Separator_RunContentElt = Generalization(general=RunContentElt, specific=WordprocessingMLStyles_Separator)
gen_WordprocessingMLStyles_ContinuationSeparator_RunContentElt = Generalization(general=RunContentElt, specific=WordprocessingMLStyles_ContinuationSeparator)
gen_WordprocessingMLStyles_PgNum_RunContentElt = Generalization(general=RunContentElt, specific=WordprocessingMLStyles_PgNum)
gen_WordprocessingMLStyles_Cr_RunContentElt = Generalization(general=RunContentElt, specific=WordprocessingMLStyles_Cr)
gen_WordprocessingMLStyles_Footnote_RunContentElt = Generalization(general=RunContentElt, specific=WordprocessingMLStyles_Footnote)
gen_WordprocessingMLStyles_Footnote_NoteElt = Generalization(general=NoteElt, specific=WordprocessingMLStyles_Footnote)
gen_WordprocessingMLStyles_FldChar_FldCharElt = Generalization(general=FldCharElt, specific=WordprocessingMLStyles_FldChar)
gen_WordprocessingMLStyles_Endnote_RunContentElt = Generalization(general=RunContentElt, specific=WordprocessingMLStyles_Endnote)
gen_WordprocessingMLStyles_Endnote_NoteElt = Generalization(general=NoteElt, specific=WordprocessingMLStyles_Endnote)
gen_WordprocessingMLStyles_Picture_RunContentElt = Generalization(general=RunContentElt, specific=WordprocessingMLStyles_Picture)
gen_WordprocessingMLStyles_Picture_PictureType = Generalization(general=PictureType, specific=WordprocessingMLStyles_Picture)
gen_WordprocessingMLStyles_Symbol_RunContentElt = Generalization(general=RunContentElt, specific=WordprocessingMLStyles_Symbol)
gen_WordprocessingMLStyles_Symbol_SymElt = Generalization(general=SymElt, specific=WordprocessingMLStyles_Symbol)
gen_WordprocessingMLStyles_Tab_RunContentElt = Generalization(general=RunContentElt, specific=WordprocessingMLStyles_Tab)
gen_WordprocessingMLStyles_Tab_TabElt = Generalization(general=TabElt, specific=WordprocessingMLStyles_Tab)
gen_WordprocessingMLStyles_FldChar_RunContentElt = Generalization(general=RunContentElt, specific=WordprocessingMLStyles_FldChar)
gen_WordprocessingMLStyles_TableElt_BlockLevelChunkElt = Generalization(general=BlockLevelChunkElt, specific=WordprocessingMLStyles_TableElt)
gen_WordprocessingMLStyles_CfChunk_BlockLevelElt = Generalization(general=BlockLevelElt, specific=WordprocessingMLStyles_CfChunk)
gen_WordprocessingMLStyles_RunLevelElt_BlockLevelChunkElt = Generalization(general=BlockLevelChunkElt, specific=WordprocessingMLStyles_RunLevelElt)
gen_WordprocessingMLStyles_SimpleFieldElt_ParaContentElt = Generalization(general=ParaContentElt, specific=WordprocessingMLStyles_SimpleFieldElt)
gen_WordprocessingMLStyles_HLinkElt_ParaContentElt = Generalization(general=ParaContentElt, specific=WordprocessingMLStyles_HLinkElt)
gen_WordprocessingMLStyles_SubDocElt_ParaContentElt = Generalization(general=ParaContentElt, specific=WordprocessingMLStyles_SubDocElt)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={WordprocessingMLStyles_DateTimeType, WordprocessingMLStyles_VersionType, WordprocessingMLStyles_BooleanValue, WordprocessingMLStyles_DocumentPropertiesCollection, WordDocument, WordprocessingMLStyles_ValueType, WordprocessingMLStyles_StringValue, ValueType, WordprocessingMLStyles_FloatValue, WordprocessingMLStyles_DateTimeTypeValue, DateTimeType, WordprocessingMLStyles_CustomDocumentPropertiesCollection, CustomDocumentProperty, WordprocessingMLStyles_CustomDocumentProperty, CustomDocumentPropertiesCollection, VersionType, WordprocessingMLStyles_SmartTagType, SmartTagsCollection, WordprocessingMLStyles_SmartTagsCollection, SmartTagType, WordprocessingMLStyles_StringProperty, StringType, WordprocessingMLStyles_StringType, WordprocessingMLStyles_UnderlineProperty, DocumentPropertiesCollection, StringProperty, FontsListElt, ListsElt, WordprocessingMLStyles_WordDocument, BodyElt, WordprocessingMLStyles_DocPrElt, WordprocessingMLStyles_BodyElt, BlockLevelElt, SectPrElt, WordprocessingMLStyles_BlockLevelElt, NoteElt, TableCellElt, StylesElt, WordprocessingMLStyles_BlockLevelChunkElt, DocPrElt, WordprocessingMLStyles_ParaElt, BlockLevelChunkElt, ParaPrElt, ParaContentElt, WordprocessingMLStyles_ParaPrElt, ParaElt, StyleElt, WordprocessingMLStyles_ParaContentElt, WordprocessingMLStyles_RunElt, RunPrElt, RunContentElt, WordprocessingMLStyles_RunPrElt, RunElt, FontsElt, UnderlineProperty, LangElt, WordprocessingMLStyles_LangElt, WordprocessingMLStyles_RunContentElt, WordprocessingMLStyles_BreakElt, WordprocessingMLStyles_Text, WordprocessingMLStyles_DelText, WordprocessingMLStyles_InstrText, WordprocessingMLStyles_DelInstrText, WordprocessingMLStyles_NoBreakHyphen, WordprocessingMLStyles_SoftHyphen, WordprocessingMLStyles_AnnotationRef, WordprocessingMLStyles_FootnoteRef, WordprocessingMLStyles_EndnoteRef, WordprocessingMLStyles_Separator, WordprocessingMLStyles_ContinuationSeparator, WordprocessingMLStyles_PgNum, WordprocessingMLStyles_Cr, WordprocessingMLStyles_Footnote, FldCharElt, WordprocessingMLStyles_Endnote, WordprocessingMLStyles_NoteElt, WordprocessingMLStyles_Picture, PictureType, WordprocessingMLStyles_Symbol, SymElt, WordprocessingMLStyles_SymElt, WordprocessingMLStyles_Tab, TabElt, WordprocessingMLStyles_FldChar, WordprocessingMLStyles_TableGridElt, WordprocessingMLStyles_FldCharElt, WordprocessingMLStyles_TableElt, TablePrElt, TableGridElt, TableContentElt, WordprocessingMLStyles_TablePrElt, TableElt, WordprocessingMLStyles_TablePrExElt, WordprocessingMLStyles_TableContentElt, RowElt, RunLevelElt, WordprocessingMLStyles_RowElt, TablePrExElt, TableRowPrElt, RowContentElt, WordprocessingMLStyles_TableRowPrElt, WordprocessingMLStyles_RowContentElt, WordprocessingMLStyles_TableCellElt, TableCellPrElt, WordprocessingMLStyles_TableCellPrElt, WordprocessingMLStyles_FontsListElt, FontElt, WordprocessingMLStyles_FontsElt, WordprocessingMLStyles_FontElt, WordprocessingMLStyles_StylesElt, WordprocessingMLStyles_StyleElt, WordprocessingMLStyles_ListsElt, WordprocessingMLStyles_SectPrElt, WordprocessingMLStyles_RunLevelElt, WordprocessingMLStyles_CfChunk, WordprocessingMLStyles_SimpleFieldElt, WordprocessingMLStyles_HLinkElt, WordprocessingMLStyles_SubDocElt, WordprocessingMLStyles_PictureType, WordprocessingMLStyles_TabElt, BreakType, StyleKindValue, UnderlineValues, NoteValue, OnOffType, FldCharTypeProperty, HintType, HighlightColorValues, VerticalAlignRunType, JustificationValue},
    associations={value0, dp_wordDocument1, lastPrinted3, created6, lastSaved9, cdp_wordDocument12, customDocumentProperties14, customDocumentProperty_cdpe15, version2, smartTagType_ste17, st_wordDocument18, smartTagTypes20, value16, wd_smartTags21, wd_docProperties23, wd_customDocProperties24, ignoreSubtree26, ignoreElements27, fonts30, lists31, pContentElts46, body34, dpe_wordDocument35, be_wordDocument37, blockLevelElts39, sectPr40, ble_bodyElt41, ble_note43, ble_tableCellElt44, styles32, docPr33, pPr45, ppe_pElt47, ppe_styleElt48, pStyle49, pce_pElt51, rPr53, rContentElts54, rpe_rElt55, rpe_styleElt56, rStyle58, rFonts60, underline61, language63, le_runPrElt64, rce_rElt66, n_blockLevelElts68, font70, char71, fldData74, tblPr76, tblGrid77, tblContent78, tpe_tblElt79, tpe_styleElt80, tge_tblElt82, tce_tblElt84, tr86, tce_runLevelElts87, re_tblContentElt88, tblPrEx90, trPr91, rowContent92, tcPr107, tpee_rowElt93, tpe_rowElt95, trpe_styleElt97, rce_rowElt99, tc101, rce_runLevelElts103, tce_rowContentElt105, tce_content108, tcpe_tableCellElt110, tcpe_styleElt112, fle_wordDocument114, defaultFonts116, fonts118, fse_fontsListElt119, fse_runPrElt121, ascii123, h_ansi125, fareast128, cs131, fe_fontsListElt134, name137, altName139, se_wordDocument142, styles144, se_stylesElt146, styleId149, name151, aliases154, basedOn157, se_rPr171, next160, link163, rsid166, se_pPr169, se_tblPr173, se_trPr175, se_tcPr177, le_wordDocument179, spe_bodyElt181, rle_tblContentElt183, rle_rowContentElt185},
    generalizations={gen_WordprocessingMLStyles_BooleanValue_ValueType, gen_WordprocessingMLStyles_StringValue_ValueType, gen_WordprocessingMLStyles_FloatValue_ValueType, gen_WordprocessingMLStyles_DateTimeTypeValue_ValueType, gen_WordprocessingMLStyles_StringProperty_StringType, gen_WordprocessingMLStyles_BlockLevelChunkElt_BlockLevelElt, gen_WordprocessingMLStyles_ParaElt_BlockLevelChunkElt, gen_WordprocessingMLStyles_RunElt_ParaContentElt, gen_WordprocessingMLStyles_BreakElt_RunContentElt, gen_WordprocessingMLStyles_Text_RunContentElt, gen_WordprocessingMLStyles_Text_StringType, gen_WordprocessingMLStyles_DelText_RunContentElt, gen_WordprocessingMLStyles_DelText_StringType, gen_WordprocessingMLStyles_InstrText_RunContentElt, gen_WordprocessingMLStyles_InstrText_StringType, gen_WordprocessingMLStyles_DelInstrText_RunContentElt, gen_WordprocessingMLStyles_DelInstrText_StringType, gen_WordprocessingMLStyles_NoBreakHyphen_RunContentElt, gen_WordprocessingMLStyles_SoftHyphen_RunContentElt, gen_WordprocessingMLStyles_AnnotationRef_RunContentElt, gen_WordprocessingMLStyles_FootnoteRef_RunContentElt, gen_WordprocessingMLStyles_EndnoteRef_RunContentElt, gen_WordprocessingMLStyles_Separator_RunContentElt, gen_WordprocessingMLStyles_ContinuationSeparator_RunContentElt, gen_WordprocessingMLStyles_PgNum_RunContentElt, gen_WordprocessingMLStyles_Cr_RunContentElt, gen_WordprocessingMLStyles_Footnote_RunContentElt, gen_WordprocessingMLStyles_Footnote_NoteElt, gen_WordprocessingMLStyles_FldChar_FldCharElt, gen_WordprocessingMLStyles_Endnote_RunContentElt, gen_WordprocessingMLStyles_Endnote_NoteElt, gen_WordprocessingMLStyles_Picture_RunContentElt, gen_WordprocessingMLStyles_Picture_PictureType, gen_WordprocessingMLStyles_Symbol_RunContentElt, gen_WordprocessingMLStyles_Symbol_SymElt, gen_WordprocessingMLStyles_Tab_RunContentElt, gen_WordprocessingMLStyles_Tab_TabElt, gen_WordprocessingMLStyles_FldChar_RunContentElt, gen_WordprocessingMLStyles_TableElt_BlockLevelChunkElt, gen_WordprocessingMLStyles_CfChunk_BlockLevelElt, gen_WordprocessingMLStyles_RunLevelElt_BlockLevelChunkElt, gen_WordprocessingMLStyles_SimpleFieldElt_ParaContentElt, gen_WordprocessingMLStyles_HLinkElt_ParaContentElt, gen_WordprocessingMLStyles_SubDocElt_ParaContentElt},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)