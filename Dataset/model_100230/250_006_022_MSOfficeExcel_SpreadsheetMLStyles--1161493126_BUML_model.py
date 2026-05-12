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
DisplayDrawingObjectsType: Enumeration = Enumeration(
    name="DisplayDrawingObjectsType",
    literals={
            EnumerationLiteral(name="ddot_displayShapes"),
			EnumerationLiteral(name="ddot_placeHolders"),
			EnumerationLiteral(name="ddot_hideAll")
    }
)

CalculationWorkbookType: Enumeration = Enumeration(
    name="CalculationWorkbookType",
    literals={
            EnumerationLiteral(name="cwt_automaticCalculation"),
			EnumerationLiteral(name="cwt_manualCalculation"),
			EnumerationLiteral(name="cwt_semiAutomaticCalculation")
    }
)

ExcelWorksheetTypeType: Enumeration = Enumeration(
    name="ExcelWorksheetTypeType",
    literals={
            EnumerationLiteral(name="ewt_Worksheet"),
			EnumerationLiteral(name="ewt_Chart"),
			EnumerationLiteral(name="ewt_Macro"),
			EnumerationLiteral(name="ewt_Dialog")
    }
)

VisibleType: Enumeration = Enumeration(
    name="VisibleType",
    literals={
            EnumerationLiteral(name="vt_SheetVisible"),
			EnumerationLiteral(name="vt_SheetHidden"),
			EnumerationLiteral(name="vt_SheetVeryHidden")
    }
)

EnableSelectionType: Enumeration = Enumeration(
    name="EnableSelectionType",
    literals={
            EnumerationLiteral(name="est_UnlockedCells"),
			EnumerationLiteral(name="est_NoSelection")
    }
)

OrientationType: Enumeration = Enumeration(
    name="OrientationType",
    literals={
            EnumerationLiteral(name="ot_Landscape"),
			EnumerationLiteral(name="ot_Portrait")
    }
)

CommentsLayoutType: Enumeration = Enumeration(
    name="CommentsLayoutType",
    literals={
            EnumerationLiteral(name="clt_InPlace"),
			EnumerationLiteral(name="clt_PrintNone"),
			EnumerationLiteral(name="clt_SheetEnd")
    }
)

HorizontalAlignementType: Enumeration = Enumeration(
    name="HorizontalAlignementType",
    literals={
            EnumerationLiteral(name="hat_CenterAcrossSelection"),
			EnumerationLiteral(name="hat_Fill"),
			EnumerationLiteral(name="hat_Left"),
			EnumerationLiteral(name="hat_Right"),
			EnumerationLiteral(name="hat_Justify"),
			EnumerationLiteral(name="hat_Distributed"),
			EnumerationLiteral(name="hat_Center"),
			EnumerationLiteral(name="hat_Automatic"),
			EnumerationLiteral(name="hat_JustifyDistributed")
    }
)

ReadingOrderType: Enumeration = Enumeration(
    name="ReadingOrderType",
    literals={
            EnumerationLiteral(name="rot_RightToLeft"),
			EnumerationLiteral(name="rot_LeftToRight"),
			EnumerationLiteral(name="rot_Context")
    }
)

VerticalAlignementType: Enumeration = Enumeration(
    name="VerticalAlignementType",
    literals={
            EnumerationLiteral(name="vat_Top"),
			EnumerationLiteral(name="vat_Bottom"),
			EnumerationLiteral(name="vat_Justify"),
			EnumerationLiteral(name="vat_Distributed"),
			EnumerationLiteral(name="vat_Center"),
			EnumerationLiteral(name="vat_Automatic"),
			EnumerationLiteral(name="vat_JustifyDistributed")
    }
)

LineStyleType: Enumeration = Enumeration(
    name="LineStyleType",
    literals={
            EnumerationLiteral(name="lst_None"),
			EnumerationLiteral(name="lst_Continuous"),
			EnumerationLiteral(name="lst_Dash"),
			EnumerationLiteral(name="lst_Dot"),
			EnumerationLiteral(name="lst_DashDot"),
			EnumerationLiteral(name="lst_DashDotDot"),
			EnumerationLiteral(name="lst_SlantDashDot"),
			EnumerationLiteral(name="lst_Double")
    }
)

PositionType: Enumeration = Enumeration(
    name="PositionType",
    literals={
            EnumerationLiteral(name="pt_DiagonalRight"),
			EnumerationLiteral(name="pt_Left"),
			EnumerationLiteral(name="pt_Top"),
			EnumerationLiteral(name="pt_Right"),
			EnumerationLiteral(name="pt_Bottom"),
			EnumerationLiteral(name="pt_DiagonalLeft")
    }
)

UnderlineType: Enumeration = Enumeration(
    name="UnderlineType",
    literals={
            EnumerationLiteral(name="ut_None"),
			EnumerationLiteral(name="ut_Single"),
			EnumerationLiteral(name="ut_Double"),
			EnumerationLiteral(name="ut_SingleAccounting"),
			EnumerationLiteral(name="ut_DoubleAccounting")
    }
)

VerticalAlignType: Enumeration = Enumeration(
    name="VerticalAlignType",
    literals={
            EnumerationLiteral(name="vat_Superscript"),
			EnumerationLiteral(name="vat_None"),
			EnumerationLiteral(name="vat_Subscript")
    }
)

PatternType: Enumeration = Enumeration(
    name="PatternType",
    literals={
            EnumerationLiteral(name="pt_HorzStripe"),
			EnumerationLiteral(name="pt_VertStripe"),
			EnumerationLiteral(name="pt_ReverseDiagStripe"),
			EnumerationLiteral(name="pt_None"),
			EnumerationLiteral(name="pt_Solid"),
			EnumerationLiteral(name="pt_Gray75"),
			EnumerationLiteral(name="pt_Gray50"),
			EnumerationLiteral(name="pt_Gray25"),
			EnumerationLiteral(name="pt_Gray125"),
			EnumerationLiteral(name="pt_Gray0625"),
			EnumerationLiteral(name="pt_DiagStripe"),
			EnumerationLiteral(name="pt_DiagCross"),
			EnumerationLiteral(name="pt_ThickDiagCross"),
			EnumerationLiteral(name="pt_ThinHorzStripe"),
			EnumerationLiteral(name="pt_ThinVertStripe"),
			EnumerationLiteral(name="pt_ThinReverseDiagStripe"),
			EnumerationLiteral(name="pt_ThinDiagStripe"),
			EnumerationLiteral(name="pt_ThinHorzCross"),
			EnumerationLiteral(name="pt_ThinDiagCross")
    }
)

ExcelNumberFormatType: Enumeration = Enumeration(
    name="ExcelNumberFormatType",
    literals={
            EnumerationLiteral(name="enft_General_Date"),
			EnumerationLiteral(name="enft_Long_Date"),
			EnumerationLiteral(name="enft_Medium_Date"),
			EnumerationLiteral(name="enft_General"),
			EnumerationLiteral(name="enft_General_Number"),
			EnumerationLiteral(name="enft_Short_Date"),
			EnumerationLiteral(name="enft_Long_Time"),
			EnumerationLiteral(name="enft_Medium_Time"),
			EnumerationLiteral(name="enft_Short_Time"),
			EnumerationLiteral(name="enft_Currency"),
			EnumerationLiteral(name="enft_Euro_Currency"),
			EnumerationLiteral(name="enft_Fixed"),
			EnumerationLiteral(name="enft_Standard"),
			EnumerationLiteral(name="enft_Percent"),
			EnumerationLiteral(name="enft_Scientific"),
			EnumerationLiteral(name="enft_Yes_No"),
			EnumerationLiteral(name="enft_True_False"),
			EnumerationLiteral(name="enft_On_Off")
    }
)

# Classes
SpreadsheetMLStyles_DateTimeType = Class(name="SpreadsheetMLStyles_DateTimeType")
SpreadsheetMLStyles_VersionType = Class(name="SpreadsheetMLStyles_VersionType")
SpreadsheetMLStyles_ValueType = Class(name="SpreadsheetMLStyles_ValueType", is_abstract=True)
Data = Class(name="Data")
SpreadsheetMLStyles_StringValue = Class(name="SpreadsheetMLStyles_StringValue")
ValueType = Class(name="ValueType")
SpreadsheetMLStyles_NumberValue = Class(name="SpreadsheetMLStyles_NumberValue")
SpreadsheetMLStyles_DateTimeTypeValue = Class(name="SpreadsheetMLStyles_DateTimeTypeValue")
DateTimeType = Class(name="DateTimeType")
SpreadsheetMLStyles_BooleanValue = Class(name="SpreadsheetMLStyles_BooleanValue")
SpreadsheetMLStyles_ErrorValue = Class(name="SpreadsheetMLStyles_ErrorValue")
SpreadsheetMLStyles_DocumentPropertiesCollection = Class(name="SpreadsheetMLStyles_DocumentPropertiesCollection")
Workbook = Class(name="Workbook")
VersionType = Class(name="VersionType")
SpreadsheetMLStyles_CustomDocumentPropertiesCollection = Class(name="SpreadsheetMLStyles_CustomDocumentPropertiesCollection")
CustomDocumentProperty = Class(name="CustomDocumentProperty")
SpreadsheetMLStyles_CustomDocumentProperty = Class(name="SpreadsheetMLStyles_CustomDocumentProperty")
CustomDocumentPropertiesCollection = Class(name="CustomDocumentPropertiesCollection")
SpreadsheetMLStyles_Workbook = Class(name="SpreadsheetMLStyles_Workbook")
SpreadsheetMLStyles_SmartTagType = Class(name="SpreadsheetMLStyles_SmartTagType")
SmartTagsCollection = Class(name="SmartTagsCollection")
SpreadsheetMLStyles_SmartTagsCollection = Class(name="SpreadsheetMLStyles_SmartTagsCollection")
Cell = Class(name="Cell")
SmartTagType = Class(name="SmartTagType")
Worksheet = Class(name="Worksheet")
DocumentPropertiesCollection = Class(name="DocumentPropertiesCollection")
ExcelWorkbook = Class(name="ExcelWorkbook")
StylesCollection = Class(name="StylesCollection")
NamesType = Class(name="NamesType")
SpreadsheetMLStyles_Table = Class(name="SpreadsheetMLStyles_Table")
SpreadsheetMLStyles_Worksheet = Class(name="SpreadsheetMLStyles_Worksheet")
Table = Class(name="Table")
WorksheetOptionsElt = Class(name="WorksheetOptionsElt")
SpreadsheetMLStyles_StyledElement = Class(name="SpreadsheetMLStyles_StyledElement", is_abstract=True)
StyleType = Class(name="StyleType")
StyledElement = Class(name="StyledElement")
Column = Class(name="Column")
Row = Class(name="Row")
SpreadsheetMLStyles_Row = Class(name="SpreadsheetMLStyles_Row")
SpreadsheetMLStyles_TableElement = Class(name="SpreadsheetMLStyles_TableElement", is_abstract=True)
SpreadsheetMLStyles_ColOrRowElement = Class(name="SpreadsheetMLStyles_ColOrRowElement", is_abstract=True)
TableElement = Class(name="TableElement")
SpreadsheetMLStyles_Column = Class(name="SpreadsheetMLStyles_Column")
ColOrRowElement = Class(name="ColOrRowElement")
SpreadsheetMLStyles_Cell = Class(name="SpreadsheetMLStyles_Cell")
SpreadsheetMLStyles_Comment = Class(name="SpreadsheetMLStyles_Comment")
Comment = Class(name="Comment")
SpreadsheetMLStyles_Data = Class(name="SpreadsheetMLStyles_Data")
SpreadsheetMLStyles_ExcelWorkbook = Class(name="SpreadsheetMLStyles_ExcelWorkbook")
SpreadsheetMLStyles_WorksheetOptionsElt = Class(name="SpreadsheetMLStyles_WorksheetOptionsElt")
PageSetup = Class(name="PageSetup")
Print = Class(name="Print")
Header = Class(name="Header")
Footer = Class(name="Footer")
PageMarginsInfo = Class(name="PageMarginsInfo")
SpreadsheetMLStyles_Layout = Class(name="SpreadsheetMLStyles_Layout")
SpreadsheetMLStyles_PageSetup = Class(name="SpreadsheetMLStyles_PageSetup")
Layout = Class(name="Layout")
SpreadsheetMLStyles_HeaderOrFooterElt = Class(name="SpreadsheetMLStyles_HeaderOrFooterElt", is_abstract=True)
SpreadsheetMLStyles_Header = Class(name="SpreadsheetMLStyles_Header")
HeaderOrFooterElt = Class(name="HeaderOrFooterElt")
SpreadsheetMLStyles_PageMarginsInfo = Class(name="SpreadsheetMLStyles_PageMarginsInfo")
SpreadsheetMLStyles_Print = Class(name="SpreadsheetMLStyles_Print")
SpreadsheetMLStyles_Footer = Class(name="SpreadsheetMLStyles_Footer")
SpreadsheetMLStyles_StylesCollection = Class(name="SpreadsheetMLStyles_StylesCollection")
SpreadsheetMLStyles_StyleType = Class(name="SpreadsheetMLStyles_StyleType")
AlignmentType = Class(name="AlignmentType")
BordersType = Class(name="BordersType")
InteriorType = Class(name="InteriorType")
NumberFormatType = Class(name="NumberFormatType")
ProtectionType = Class(name="ProtectionType")
SpreadsheetMLStyles_ProtectionType = Class(name="SpreadsheetMLStyles_ProtectionType")
FontType = Class(name="FontType")
SpreadsheetMLStyles_AlignmentType = Class(name="SpreadsheetMLStyles_AlignmentType")
SpreadsheetMLStyles_BorderType = Class(name="SpreadsheetMLStyles_BorderType")
SpreadsheetMLStyles_BordersType = Class(name="SpreadsheetMLStyles_BordersType")
BorderType = Class(name="BorderType")
SpreadsheetMLStyles_FontType = Class(name="SpreadsheetMLStyles_FontType")
SpreadsheetMLStyles_InteriorType = Class(name="SpreadsheetMLStyles_InteriorType")
SpreadsheetMLStyles_NumberFormatType = Class(name="SpreadsheetMLStyles_NumberFormatType")
NamedRange = Class(name="NamedRange")
SpreadsheetMLStyles_NamesType = Class(name="SpreadsheetMLStyles_NamesType")
SpreadsheetMLStyles_NamedRange = Class(name="SpreadsheetMLStyles_NamedRange")

# SpreadsheetMLStyles_DateTimeType class attributes and methods
SpreadsheetMLStyles_DateTimeType_year: Property = Property(name="year", type=StringType)
SpreadsheetMLStyles_DateTimeType_month: Property = Property(name="month", type=StringType)
SpreadsheetMLStyles_DateTimeType_day: Property = Property(name="day", type=StringType)
SpreadsheetMLStyles_DateTimeType_hour: Property = Property(name="hour", type=StringType)
SpreadsheetMLStyles_DateTimeType_minute: Property = Property(name="minute", type=StringType)
SpreadsheetMLStyles_DateTimeType_second: Property = Property(name="second", type=StringType)
SpreadsheetMLStyles_DateTimeType.attributes={SpreadsheetMLStyles_DateTimeType_month, SpreadsheetMLStyles_DateTimeType_day, SpreadsheetMLStyles_DateTimeType_second, SpreadsheetMLStyles_DateTimeType_hour, SpreadsheetMLStyles_DateTimeType_minute, SpreadsheetMLStyles_DateTimeType_year}

# SpreadsheetMLStyles_VersionType class attributes and methods
SpreadsheetMLStyles_VersionType_n: Property = Property(name="n", type=StringType)
SpreadsheetMLStyles_VersionType_nn: Property = Property(name="nn", type=StringType)
SpreadsheetMLStyles_VersionType.attributes={SpreadsheetMLStyles_VersionType_n, SpreadsheetMLStyles_VersionType_nn}

# SpreadsheetMLStyles_ValueType class attributes and methods

# Data class attributes and methods

# SpreadsheetMLStyles_StringValue class attributes and methods
SpreadsheetMLStyles_StringValue_value: Property = Property(name="value", type=StringType)
SpreadsheetMLStyles_StringValue.attributes={SpreadsheetMLStyles_StringValue_value}

# ValueType class attributes and methods

# SpreadsheetMLStyles_NumberValue class attributes and methods
SpreadsheetMLStyles_NumberValue_value: Property = Property(name="value", type=StringType)
SpreadsheetMLStyles_NumberValue.attributes={SpreadsheetMLStyles_NumberValue_value}

# SpreadsheetMLStyles_DateTimeTypeValue class attributes and methods

# DateTimeType class attributes and methods

# SpreadsheetMLStyles_BooleanValue class attributes and methods
SpreadsheetMLStyles_BooleanValue_value: Property = Property(name="value", type=StringType)
SpreadsheetMLStyles_BooleanValue.attributes={SpreadsheetMLStyles_BooleanValue_value}

# SpreadsheetMLStyles_ErrorValue class attributes and methods

# SpreadsheetMLStyles_DocumentPropertiesCollection class attributes and methods
SpreadsheetMLStyles_DocumentPropertiesCollection_title: Property = Property(name="title", type=StringType)
SpreadsheetMLStyles_DocumentPropertiesCollection_subject: Property = Property(name="subject", type=StringType)
SpreadsheetMLStyles_DocumentPropertiesCollection_keywords: Property = Property(name="keywords", type=StringType)
SpreadsheetMLStyles_DocumentPropertiesCollection_description: Property = Property(name="description", type=StringType)
SpreadsheetMLStyles_DocumentPropertiesCollection_category: Property = Property(name="category", type=StringType)
SpreadsheetMLStyles_DocumentPropertiesCollection_author: Property = Property(name="author", type=StringType)
SpreadsheetMLStyles_DocumentPropertiesCollection_lastAuthor: Property = Property(name="lastAuthor", type=StringType)
SpreadsheetMLStyles_DocumentPropertiesCollection_manager: Property = Property(name="manager", type=StringType)
SpreadsheetMLStyles_DocumentPropertiesCollection_company: Property = Property(name="company", type=StringType)
SpreadsheetMLStyles_DocumentPropertiesCollection_hyperlinkBase: Property = Property(name="hyperlinkBase", type=StringType)
SpreadsheetMLStyles_DocumentPropertiesCollection_revision: Property = Property(name="revision", type=StringType)
SpreadsheetMLStyles_DocumentPropertiesCollection_presentationFormat: Property = Property(name="presentationFormat", type=StringType)
SpreadsheetMLStyles_DocumentPropertiesCollection_guid: Property = Property(name="guid", type=StringType)
SpreadsheetMLStyles_DocumentPropertiesCollection_appName: Property = Property(name="appName", type=StringType)
SpreadsheetMLStyles_DocumentPropertiesCollection_paragraphs: Property = Property(name="paragraphs", type=StringType)
SpreadsheetMLStyles_DocumentPropertiesCollection_totalTime: Property = Property(name="totalTime", type=StringType)
SpreadsheetMLStyles_DocumentPropertiesCollection_pages: Property = Property(name="pages", type=StringType)
SpreadsheetMLStyles_DocumentPropertiesCollection_words: Property = Property(name="words", type=StringType)
SpreadsheetMLStyles_DocumentPropertiesCollection_characters: Property = Property(name="characters", type=StringType)
SpreadsheetMLStyles_DocumentPropertiesCollection_charactersWithSpaces: Property = Property(name="charactersWithSpaces", type=StringType)
SpreadsheetMLStyles_DocumentPropertiesCollection_bytes: Property = Property(name="bytes", type=StringType)
SpreadsheetMLStyles_DocumentPropertiesCollection_lines: Property = Property(name="lines", type=StringType)
SpreadsheetMLStyles_DocumentPropertiesCollection.attributes={SpreadsheetMLStyles_DocumentPropertiesCollection_author, SpreadsheetMLStyles_DocumentPropertiesCollection_description, SpreadsheetMLStyles_DocumentPropertiesCollection_presentationFormat, SpreadsheetMLStyles_DocumentPropertiesCollection_lines, SpreadsheetMLStyles_DocumentPropertiesCollection_characters, SpreadsheetMLStyles_DocumentPropertiesCollection_totalTime, SpreadsheetMLStyles_DocumentPropertiesCollection_title, SpreadsheetMLStyles_DocumentPropertiesCollection_guid, SpreadsheetMLStyles_DocumentPropertiesCollection_charactersWithSpaces, SpreadsheetMLStyles_DocumentPropertiesCollection_category, SpreadsheetMLStyles_DocumentPropertiesCollection_bytes, SpreadsheetMLStyles_DocumentPropertiesCollection_company, SpreadsheetMLStyles_DocumentPropertiesCollection_subject, SpreadsheetMLStyles_DocumentPropertiesCollection_lastAuthor, SpreadsheetMLStyles_DocumentPropertiesCollection_hyperlinkBase, SpreadsheetMLStyles_DocumentPropertiesCollection_pages, SpreadsheetMLStyles_DocumentPropertiesCollection_revision, SpreadsheetMLStyles_DocumentPropertiesCollection_words, SpreadsheetMLStyles_DocumentPropertiesCollection_paragraphs, SpreadsheetMLStyles_DocumentPropertiesCollection_manager, SpreadsheetMLStyles_DocumentPropertiesCollection_appName, SpreadsheetMLStyles_DocumentPropertiesCollection_keywords}

# Workbook class attributes and methods

# VersionType class attributes and methods

# SpreadsheetMLStyles_CustomDocumentPropertiesCollection class attributes and methods

# CustomDocumentProperty class attributes and methods

# SpreadsheetMLStyles_CustomDocumentProperty class attributes and methods
SpreadsheetMLStyles_CustomDocumentProperty_name: Property = Property(name="name", type=StringType)
SpreadsheetMLStyles_CustomDocumentProperty.attributes={SpreadsheetMLStyles_CustomDocumentProperty_name}

# CustomDocumentPropertiesCollection class attributes and methods

# SpreadsheetMLStyles_Workbook class attributes and methods

# SpreadsheetMLStyles_SmartTagType class attributes and methods
SpreadsheetMLStyles_SmartTagType_namespaceuri: Property = Property(name="namespaceuri", type=StringType)
SpreadsheetMLStyles_SmartTagType_name: Property = Property(name="name", type=StringType)
SpreadsheetMLStyles_SmartTagType_url: Property = Property(name="url", type=StringType)
SpreadsheetMLStyles_SmartTagType.attributes={SpreadsheetMLStyles_SmartTagType_url, SpreadsheetMLStyles_SmartTagType_name, SpreadsheetMLStyles_SmartTagType_namespaceuri}

# SmartTagsCollection class attributes and methods

# SpreadsheetMLStyles_SmartTagsCollection class attributes and methods

# Cell class attributes and methods

# SmartTagType class attributes and methods

# Worksheet class attributes and methods

# DocumentPropertiesCollection class attributes and methods

# ExcelWorkbook class attributes and methods

# StylesCollection class attributes and methods

# NamesType class attributes and methods

# SpreadsheetMLStyles_Table class attributes and methods
SpreadsheetMLStyles_Table_topCell: Property = Property(name="topCell", type=StringType)
SpreadsheetMLStyles_Table_defaultColumnWidth: Property = Property(name="defaultColumnWidth", type=StringType)
SpreadsheetMLStyles_Table_defaultRowHeight: Property = Property(name="defaultRowHeight", type=StringType)
SpreadsheetMLStyles_Table_expandedColumnCount: Property = Property(name="expandedColumnCount", type=StringType)
SpreadsheetMLStyles_Table_expandedRowCount: Property = Property(name="expandedRowCount", type=StringType)
SpreadsheetMLStyles_Table_leftCell: Property = Property(name="leftCell", type=StringType)
SpreadsheetMLStyles_Table_fullColumns: Property = Property(name="fullColumns", type=StringType)
SpreadsheetMLStyles_Table_fullRows: Property = Property(name="fullRows", type=StringType)
SpreadsheetMLStyles_Table.attributes={SpreadsheetMLStyles_Table_expandedRowCount, SpreadsheetMLStyles_Table_fullRows, SpreadsheetMLStyles_Table_expandedColumnCount, SpreadsheetMLStyles_Table_topCell, SpreadsheetMLStyles_Table_leftCell, SpreadsheetMLStyles_Table_defaultColumnWidth, SpreadsheetMLStyles_Table_fullColumns, SpreadsheetMLStyles_Table_defaultRowHeight}

# SpreadsheetMLStyles_Worksheet class attributes and methods
SpreadsheetMLStyles_Worksheet_name: Property = Property(name="name", type=StringType)
SpreadsheetMLStyles_Worksheet_protected: Property = Property(name="protected", type=StringType)
SpreadsheetMLStyles_Worksheet_rightToLeft: Property = Property(name="rightToLeft", type=StringType)
SpreadsheetMLStyles_Worksheet.attributes={SpreadsheetMLStyles_Worksheet_rightToLeft, SpreadsheetMLStyles_Worksheet_protected, SpreadsheetMLStyles_Worksheet_name}

# Table class attributes and methods

# WorksheetOptionsElt class attributes and methods

# SpreadsheetMLStyles_StyledElement class attributes and methods

# StyleType class attributes and methods

# StyledElement class attributes and methods

# Column class attributes and methods

# Row class attributes and methods

# SpreadsheetMLStyles_Row class attributes and methods
SpreadsheetMLStyles_Row_autoFitHeight: Property = Property(name="autoFitHeight", type=StringType)
SpreadsheetMLStyles_Row_height: Property = Property(name="height", type=StringType)
SpreadsheetMLStyles_Row.attributes={SpreadsheetMLStyles_Row_height, SpreadsheetMLStyles_Row_autoFitHeight}

# SpreadsheetMLStyles_TableElement class attributes and methods
SpreadsheetMLStyles_TableElement_index: Property = Property(name="index", type=StringType)
SpreadsheetMLStyles_TableElement.attributes={SpreadsheetMLStyles_TableElement_index}

# SpreadsheetMLStyles_ColOrRowElement class attributes and methods
SpreadsheetMLStyles_ColOrRowElement_hidden: Property = Property(name="hidden", type=StringType)
SpreadsheetMLStyles_ColOrRowElement_span: Property = Property(name="span", type=StringType)
SpreadsheetMLStyles_ColOrRowElement.attributes={SpreadsheetMLStyles_ColOrRowElement_hidden, SpreadsheetMLStyles_ColOrRowElement_span}

# TableElement class attributes and methods

# SpreadsheetMLStyles_Column class attributes and methods
SpreadsheetMLStyles_Column_width: Property = Property(name="width", type=StringType)
SpreadsheetMLStyles_Column_autoFitWidth: Property = Property(name="autoFitWidth", type=StringType)
SpreadsheetMLStyles_Column.attributes={SpreadsheetMLStyles_Column_autoFitWidth, SpreadsheetMLStyles_Column_width}

# ColOrRowElement class attributes and methods

# SpreadsheetMLStyles_Cell class attributes and methods
SpreadsheetMLStyles_Cell_arrayRange: Property = Property(name="arrayRange", type=StringType)
SpreadsheetMLStyles_Cell_formula: Property = Property(name="formula", type=StringType)
SpreadsheetMLStyles_Cell_hRef: Property = Property(name="hRef", type=StringType)
SpreadsheetMLStyles_Cell_mergeAcross: Property = Property(name="mergeAcross", type=StringType)
SpreadsheetMLStyles_Cell_mergeDown: Property = Property(name="mergeDown", type=StringType)
SpreadsheetMLStyles_Cell.attributes={SpreadsheetMLStyles_Cell_mergeDown, SpreadsheetMLStyles_Cell_arrayRange, SpreadsheetMLStyles_Cell_hRef, SpreadsheetMLStyles_Cell_formula, SpreadsheetMLStyles_Cell_mergeAcross}

# SpreadsheetMLStyles_Comment class attributes and methods
SpreadsheetMLStyles_Comment_author: Property = Property(name="author", type=StringType)
SpreadsheetMLStyles_Comment_showAlways: Property = Property(name="showAlways", type=StringType)
SpreadsheetMLStyles_Comment.attributes={SpreadsheetMLStyles_Comment_author, SpreadsheetMLStyles_Comment_showAlways}

# Comment class attributes and methods

# SpreadsheetMLStyles_Data class attributes and methods

# SpreadsheetMLStyles_ExcelWorkbook class attributes and methods
SpreadsheetMLStyles_ExcelWorkbook_hideVerticalScrollBar: Property = Property(name="hideVerticalScrollBar", type=StringType)
SpreadsheetMLStyles_ExcelWorkbook_hideWorkbookTabs: Property = Property(name="hideWorkbookTabs", type=StringType)
SpreadsheetMLStyles_ExcelWorkbook_windowHeight: Property = Property(name="windowHeight", type=StringType)
SpreadsheetMLStyles_ExcelWorkbook_windowWidth: Property = Property(name="windowWidth", type=StringType)
SpreadsheetMLStyles_ExcelWorkbook_windowTopX: Property = Property(name="windowTopX", type=StringType)
SpreadsheetMLStyles_ExcelWorkbook_windowTopY: Property = Property(name="windowTopY", type=StringType)
SpreadsheetMLStyles_ExcelWorkbook_activeSheet: Property = Property(name="activeSheet", type=StringType)
SpreadsheetMLStyles_ExcelWorkbook_selectedSheets: Property = Property(name="selectedSheets", type=StringType)
SpreadsheetMLStyles_ExcelWorkbook_windowHidden: Property = Property(name="windowHidden", type=StringType)
SpreadsheetMLStyles_ExcelWorkbook_hideHorizontalScrollBar: Property = Property(name="hideHorizontalScrollBar", type=StringType)
SpreadsheetMLStyles_ExcelWorkbook_protectWindows: Property = Property(name="protectWindows", type=StringType)
SpreadsheetMLStyles_ExcelWorkbook_displayInkNotes: Property = Property(name="displayInkNotes", type=StringType)
SpreadsheetMLStyles_ExcelWorkbook_embedSaveSmartTags: Property = Property(name="embedSaveSmartTags", type=StringType)
SpreadsheetMLStyles_ExcelWorkbook_futureVer: Property = Property(name="futureVer", type=StringType)
SpreadsheetMLStyles_ExcelWorkbook_tabRatio: Property = Property(name="tabRatio", type=StringType)
SpreadsheetMLStyles_ExcelWorkbook_windowIconic: Property = Property(name="windowIconic", type=StringType)
SpreadsheetMLStyles_ExcelWorkbook_displayDrawingObjects: Property = Property(name="displayDrawingObjects", type=StringType)
SpreadsheetMLStyles_ExcelWorkbook_activeChart: Property = Property(name="activeChart", type=StringType)
SpreadsheetMLStyles_ExcelWorkbook_firstVisibleSheet: Property = Property(name="firstVisibleSheet", type=StringType)
SpreadsheetMLStyles_ExcelWorkbook_hidePivotTableFieldList: Property = Property(name="hidePivotTableFieldList", type=StringType)
SpreadsheetMLStyles_ExcelWorkbook_protectStructure: Property = Property(name="protectStructure", type=StringType)
SpreadsheetMLStyles_ExcelWorkbook_date1904: Property = Property(name="date1904", type=StringType)
SpreadsheetMLStyles_ExcelWorkbook_refModeR1C1: Property = Property(name="refModeR1C1", type=StringType)
SpreadsheetMLStyles_ExcelWorkbook_iteration: Property = Property(name="iteration", type=StringType)
SpreadsheetMLStyles_ExcelWorkbook_maxIterations: Property = Property(name="maxIterations", type=StringType)
SpreadsheetMLStyles_ExcelWorkbook_createBackup: Property = Property(name="createBackup", type=StringType)
SpreadsheetMLStyles_ExcelWorkbook_calculation: Property = Property(name="calculation", type=StringType)
SpreadsheetMLStyles_ExcelWorkbook_doNotCalculateBeforeSave: Property = Property(name="doNotCalculateBeforeSave", type=StringType)
SpreadsheetMLStyles_ExcelWorkbook_noAutoRecover: Property = Property(name="noAutoRecover", type=StringType)
SpreadsheetMLStyles_ExcelWorkbook_acceptLabelsInFormulas: Property = Property(name="acceptLabelsInFormulas", type=StringType)
SpreadsheetMLStyles_ExcelWorkbook_uncalced: Property = Property(name="uncalced", type=StringType)
SpreadsheetMLStyles_ExcelWorkbook_maxChange: Property = Property(name="maxChange", type=StringType)
SpreadsheetMLStyles_ExcelWorkbook_precisionAsDisplayed: Property = Property(name="precisionAsDisplayed", type=StringType)
SpreadsheetMLStyles_ExcelWorkbook_doNotSaveLinkValues: Property = Property(name="doNotSaveLinkValues", type=StringType)
SpreadsheetMLStyles_ExcelWorkbook.attributes={SpreadsheetMLStyles_ExcelWorkbook_windowIconic, SpreadsheetMLStyles_ExcelWorkbook_precisionAsDisplayed, SpreadsheetMLStyles_ExcelWorkbook_hidePivotTableFieldList, SpreadsheetMLStyles_ExcelWorkbook_windowWidth, SpreadsheetMLStyles_ExcelWorkbook_doNotSaveLinkValues, SpreadsheetMLStyles_ExcelWorkbook_selectedSheets, SpreadsheetMLStyles_ExcelWorkbook_displayInkNotes, SpreadsheetMLStyles_ExcelWorkbook_noAutoRecover, SpreadsheetMLStyles_ExcelWorkbook_iteration, SpreadsheetMLStyles_ExcelWorkbook_windowHidden, SpreadsheetMLStyles_ExcelWorkbook_date1904, SpreadsheetMLStyles_ExcelWorkbook_hideVerticalScrollBar, SpreadsheetMLStyles_ExcelWorkbook_embedSaveSmartTags, SpreadsheetMLStyles_ExcelWorkbook_calculation, SpreadsheetMLStyles_ExcelWorkbook_tabRatio, SpreadsheetMLStyles_ExcelWorkbook_firstVisibleSheet, SpreadsheetMLStyles_ExcelWorkbook_windowHeight, SpreadsheetMLStyles_ExcelWorkbook_windowTopX, SpreadsheetMLStyles_ExcelWorkbook_uncalced, SpreadsheetMLStyles_ExcelWorkbook_maxIterations, SpreadsheetMLStyles_ExcelWorkbook_createBackup, SpreadsheetMLStyles_ExcelWorkbook_protectWindows, SpreadsheetMLStyles_ExcelWorkbook_hideHorizontalScrollBar, SpreadsheetMLStyles_ExcelWorkbook_refModeR1C1, SpreadsheetMLStyles_ExcelWorkbook_activeSheet, SpreadsheetMLStyles_ExcelWorkbook_displayDrawingObjects, SpreadsheetMLStyles_ExcelWorkbook_windowTopY, SpreadsheetMLStyles_ExcelWorkbook_acceptLabelsInFormulas, SpreadsheetMLStyles_ExcelWorkbook_doNotCalculateBeforeSave, SpreadsheetMLStyles_ExcelWorkbook_maxChange, SpreadsheetMLStyles_ExcelWorkbook_hideWorkbookTabs, SpreadsheetMLStyles_ExcelWorkbook_futureVer, SpreadsheetMLStyles_ExcelWorkbook_protectStructure, SpreadsheetMLStyles_ExcelWorkbook_activeChart}

# SpreadsheetMLStyles_WorksheetOptionsElt class attributes and methods
SpreadsheetMLStyles_WorksheetOptionsElt_fitToPage: Property = Property(name="fitToPage", type=StringType)
SpreadsheetMLStyles_WorksheetOptionsElt_doNotDisplayColHeaders: Property = Property(name="doNotDisplayColHeaders", type=StringType)
SpreadsheetMLStyles_WorksheetOptionsElt_doNotDisplayRowHeaders: Property = Property(name="doNotDisplayRowHeaders", type=StringType)
SpreadsheetMLStyles_WorksheetOptionsElt_gridlineColor: Property = Property(name="gridlineColor", type=StringType)
SpreadsheetMLStyles_WorksheetOptionsElt_name: Property = Property(name="name", type=StringType)
SpreadsheetMLStyles_WorksheetOptionsElt_excelWorksheetType: Property = Property(name="excelWorksheetType", type=StringType)
SpreadsheetMLStyles_WorksheetOptionsElt_intlMacro: Property = Property(name="intlMacro", type=StringType)
SpreadsheetMLStyles_WorksheetOptionsElt_unsynced: Property = Property(name="unsynced", type=StringType)
SpreadsheetMLStyles_WorksheetOptionsElt_transitionFormulaEntry: Property = Property(name="transitionFormulaEntry", type=StringType)
SpreadsheetMLStyles_WorksheetOptionsElt_zoom: Property = Property(name="zoom", type=StringType)
SpreadsheetMLStyles_WorksheetOptionsElt_pageBreakZoom: Property = Property(name="pageBreakZoom", type=StringType)
SpreadsheetMLStyles_WorksheetOptionsElt_showPageBreakZoom: Property = Property(name="showPageBreakZoom", type=StringType)
SpreadsheetMLStyles_WorksheetOptionsElt_defaultRowHeight: Property = Property(name="defaultRowHeight", type=StringType)
SpreadsheetMLStyles_WorksheetOptionsElt_defaultColumnWidth: Property = Property(name="defaultColumnWidth", type=StringType)
SpreadsheetMLStyles_WorksheetOptionsElt_standardWidth: Property = Property(name="standardWidth", type=StringType)
SpreadsheetMLStyles_WorksheetOptionsElt_visible: Property = Property(name="visible", type=StringType)
SpreadsheetMLStyles_WorksheetOptionsElt_leftColumnVisible: Property = Property(name="leftColumnVisible", type=StringType)
SpreadsheetMLStyles_WorksheetOptionsElt_selected: Property = Property(name="selected", type=StringType)
SpreadsheetMLStyles_WorksheetOptionsElt_codeName: Property = Property(name="codeName", type=StringType)
SpreadsheetMLStyles_WorksheetOptionsElt_displayPageBreak: Property = Property(name="displayPageBreak", type=StringType)
SpreadsheetMLStyles_WorksheetOptionsElt_transitionExpressionEvaluation: Property = Property(name="transitionExpressionEvaluation", type=StringType)
SpreadsheetMLStyles_WorksheetOptionsElt_doNotDisplayHeadings: Property = Property(name="doNotDisplayHeadings", type=StringType)
SpreadsheetMLStyles_WorksheetOptionsElt_doNotDisplayOutline: Property = Property(name="doNotDisplayOutline", type=StringType)
SpreadsheetMLStyles_WorksheetOptionsElt_applyAutomaticOutlineStyles: Property = Property(name="applyAutomaticOutlineStyles", type=StringType)
SpreadsheetMLStyles_WorksheetOptionsElt_noSummaryRowsBelowDetail: Property = Property(name="noSummaryRowsBelowDetail", type=StringType)
SpreadsheetMLStyles_WorksheetOptionsElt_noSummaryColumnsRightDetail: Property = Property(name="noSummaryColumnsRightDetail", type=StringType)
SpreadsheetMLStyles_WorksheetOptionsElt_doNotDisplayZeros: Property = Property(name="doNotDisplayZeros", type=StringType)
SpreadsheetMLStyles_WorksheetOptionsElt_activeRow: Property = Property(name="activeRow", type=StringType)
SpreadsheetMLStyles_WorksheetOptionsElt_activeColumn: Property = Property(name="activeColumn", type=StringType)
SpreadsheetMLStyles_WorksheetOptionsElt_filterOn: Property = Property(name="filterOn", type=StringType)
SpreadsheetMLStyles_WorksheetOptionsElt_displayRightToLeft: Property = Property(name="displayRightToLeft", type=StringType)
SpreadsheetMLStyles_WorksheetOptionsElt_gridlineColorIndex: Property = Property(name="gridlineColorIndex", type=StringType)
SpreadsheetMLStyles_WorksheetOptionsElt_displayFormulas: Property = Property(name="displayFormulas", type=StringType)
SpreadsheetMLStyles_WorksheetOptionsElt_doNotDisplayGridlines: Property = Property(name="doNotDisplayGridlines", type=StringType)
SpreadsheetMLStyles_WorksheetOptionsElt_leftColumnRightPane: Property = Property(name="leftColumnRightPane", type=StringType)
SpreadsheetMLStyles_WorksheetOptionsElt_activePane: Property = Property(name="activePane", type=StringType)
SpreadsheetMLStyles_WorksheetOptionsElt_splitHorizontal: Property = Property(name="splitHorizontal", type=StringType)
SpreadsheetMLStyles_WorksheetOptionsElt_splitVertical: Property = Property(name="splitVertical", type=StringType)
SpreadsheetMLStyles_WorksheetOptionsElt_freezePanes: Property = Property(name="freezePanes", type=StringType)
SpreadsheetMLStyles_WorksheetOptionsElt_frozenNoSplit: Property = Property(name="frozenNoSplit", type=StringType)
SpreadsheetMLStyles_WorksheetOptionsElt_tabColorIndex: Property = Property(name="tabColorIndex", type=StringType)
SpreadsheetMLStyles_WorksheetOptionsElt_protectContentst: Property = Property(name="protectContentst", type=StringType)
SpreadsheetMLStyles_WorksheetOptionsElt_protectObjects: Property = Property(name="protectObjects", type=StringType)
SpreadsheetMLStyles_WorksheetOptionsElt_rangeSelection: Property = Property(name="rangeSelection", type=StringType)
SpreadsheetMLStyles_WorksheetOptionsElt_topRowVisible: Property = Property(name="topRowVisible", type=StringType)
SpreadsheetMLStyles_WorksheetOptionsElt_topRowBottomPane: Property = Property(name="topRowBottomPane", type=StringType)
SpreadsheetMLStyles_WorksheetOptionsElt_allowSizeRows: Property = Property(name="allowSizeRows", type=StringType)
SpreadsheetMLStyles_WorksheetOptionsElt_allowInsertCols: Property = Property(name="allowInsertCols", type=StringType)
SpreadsheetMLStyles_WorksheetOptionsElt_allowInsertRows: Property = Property(name="allowInsertRows", type=StringType)
SpreadsheetMLStyles_WorksheetOptionsElt_allowInsertHyperlinks: Property = Property(name="allowInsertHyperlinks", type=StringType)
SpreadsheetMLStyles_WorksheetOptionsElt_allowDeleteCols: Property = Property(name="allowDeleteCols", type=StringType)
SpreadsheetMLStyles_WorksheetOptionsElt_allowDeleteRows: Property = Property(name="allowDeleteRows", type=StringType)
SpreadsheetMLStyles_WorksheetOptionsElt_allowSort: Property = Property(name="allowSort", type=StringType)
SpreadsheetMLStyles_WorksheetOptionsElt_allowFilter: Property = Property(name="allowFilter", type=StringType)
SpreadsheetMLStyles_WorksheetOptionsElt_allowUsePivotTables: Property = Property(name="allowUsePivotTables", type=StringType)
SpreadsheetMLStyles_WorksheetOptionsElt_protectScenarios: Property = Property(name="protectScenarios", type=StringType)
SpreadsheetMLStyles_WorksheetOptionsElt_enableSelection: Property = Property(name="enableSelection", type=StringType)
SpreadsheetMLStyles_WorksheetOptionsElt_allowFormatCells: Property = Property(name="allowFormatCells", type=StringType)
SpreadsheetMLStyles_WorksheetOptionsElt_allowSizeCols: Property = Property(name="allowSizeCols", type=StringType)
SpreadsheetMLStyles_WorksheetOptionsElt.attributes={SpreadsheetMLStyles_WorksheetOptionsElt_doNotDisplayZeros, SpreadsheetMLStyles_WorksheetOptionsElt_selected, SpreadsheetMLStyles_WorksheetOptionsElt_doNotDisplayColHeaders, SpreadsheetMLStyles_WorksheetOptionsElt_doNotDisplayGridlines, SpreadsheetMLStyles_WorksheetOptionsElt_displayPageBreak, SpreadsheetMLStyles_WorksheetOptionsElt_transitionFormulaEntry, SpreadsheetMLStyles_WorksheetOptionsElt_gridlineColor, SpreadsheetMLStyles_WorksheetOptionsElt_intlMacro, SpreadsheetMLStyles_WorksheetOptionsElt_allowFilter, SpreadsheetMLStyles_WorksheetOptionsElt_allowInsertRows, SpreadsheetMLStyles_WorksheetOptionsElt_allowSizeRows, SpreadsheetMLStyles_WorksheetOptionsElt_rangeSelection, SpreadsheetMLStyles_WorksheetOptionsElt_topRowBottomPane, SpreadsheetMLStyles_WorksheetOptionsElt_protectObjects, SpreadsheetMLStyles_WorksheetOptionsElt_doNotDisplayHeadings, SpreadsheetMLStyles_WorksheetOptionsElt_doNotDisplayRowHeaders, SpreadsheetMLStyles_WorksheetOptionsElt_allowFormatCells, SpreadsheetMLStyles_WorksheetOptionsElt_tabColorIndex, SpreadsheetMLStyles_WorksheetOptionsElt_allowUsePivotTables, SpreadsheetMLStyles_WorksheetOptionsElt_protectContentst, SpreadsheetMLStyles_WorksheetOptionsElt_activeRow, SpreadsheetMLStyles_WorksheetOptionsElt_splitHorizontal, SpreadsheetMLStyles_WorksheetOptionsElt_doNotDisplayOutline, SpreadsheetMLStyles_WorksheetOptionsElt_visible, SpreadsheetMLStyles_WorksheetOptionsElt_allowDeleteCols, SpreadsheetMLStyles_WorksheetOptionsElt_displayRightToLeft, SpreadsheetMLStyles_WorksheetOptionsElt_codeName, SpreadsheetMLStyles_WorksheetOptionsElt_activeColumn, SpreadsheetMLStyles_WorksheetOptionsElt_activePane, SpreadsheetMLStyles_WorksheetOptionsElt_splitVertical, SpreadsheetMLStyles_WorksheetOptionsElt_filterOn, SpreadsheetMLStyles_WorksheetOptionsElt_freezePanes, SpreadsheetMLStyles_WorksheetOptionsElt_allowSizeCols, SpreadsheetMLStyles_WorksheetOptionsElt_leftColumnRightPane, SpreadsheetMLStyles_WorksheetOptionsElt_standardWidth, SpreadsheetMLStyles_WorksheetOptionsElt_showPageBreakZoom, SpreadsheetMLStyles_WorksheetOptionsElt_pageBreakZoom, SpreadsheetMLStyles_WorksheetOptionsElt_unsynced, SpreadsheetMLStyles_WorksheetOptionsElt_noSummaryRowsBelowDetail, SpreadsheetMLStyles_WorksheetOptionsElt_transitionExpressionEvaluation, SpreadsheetMLStyles_WorksheetOptionsElt_excelWorksheetType, SpreadsheetMLStyles_WorksheetOptionsElt_allowInsertHyperlinks, SpreadsheetMLStyles_WorksheetOptionsElt_allowSort, SpreadsheetMLStyles_WorksheetOptionsElt_leftColumnVisible, SpreadsheetMLStyles_WorksheetOptionsElt_topRowVisible, SpreadsheetMLStyles_WorksheetOptionsElt_displayFormulas, SpreadsheetMLStyles_WorksheetOptionsElt_name, SpreadsheetMLStyles_WorksheetOptionsElt_noSummaryColumnsRightDetail, SpreadsheetMLStyles_WorksheetOptionsElt_zoom, SpreadsheetMLStyles_WorksheetOptionsElt_fitToPage, SpreadsheetMLStyles_WorksheetOptionsElt_enableSelection, SpreadsheetMLStyles_WorksheetOptionsElt_frozenNoSplit, SpreadsheetMLStyles_WorksheetOptionsElt_defaultColumnWidth, SpreadsheetMLStyles_WorksheetOptionsElt_protectScenarios, SpreadsheetMLStyles_WorksheetOptionsElt_allowDeleteRows, SpreadsheetMLStyles_WorksheetOptionsElt_defaultRowHeight, SpreadsheetMLStyles_WorksheetOptionsElt_applyAutomaticOutlineStyles, SpreadsheetMLStyles_WorksheetOptionsElt_allowInsertCols, SpreadsheetMLStyles_WorksheetOptionsElt_gridlineColorIndex}

# PageSetup class attributes and methods

# Print class attributes and methods

# Header class attributes and methods

# Footer class attributes and methods

# PageMarginsInfo class attributes and methods

# SpreadsheetMLStyles_Layout class attributes and methods
SpreadsheetMLStyles_Layout_orientation: Property = Property(name="orientation", type=StringType)
SpreadsheetMLStyles_Layout_centerHorizontal: Property = Property(name="centerHorizontal", type=StringType)
SpreadsheetMLStyles_Layout_centerVertical: Property = Property(name="centerVertical", type=StringType)
SpreadsheetMLStyles_Layout_startPageNumber: Property = Property(name="startPageNumber", type=StringType)
SpreadsheetMLStyles_Layout.attributes={SpreadsheetMLStyles_Layout_orientation, SpreadsheetMLStyles_Layout_centerHorizontal, SpreadsheetMLStyles_Layout_centerVertical, SpreadsheetMLStyles_Layout_startPageNumber}

# SpreadsheetMLStyles_PageSetup class attributes and methods

# Layout class attributes and methods

# SpreadsheetMLStyles_HeaderOrFooterElt class attributes and methods
SpreadsheetMLStyles_HeaderOrFooterElt_margin: Property = Property(name="margin", type=StringType)
SpreadsheetMLStyles_HeaderOrFooterElt_data: Property = Property(name="data", type=StringType)
SpreadsheetMLStyles_HeaderOrFooterElt.attributes={SpreadsheetMLStyles_HeaderOrFooterElt_data, SpreadsheetMLStyles_HeaderOrFooterElt_margin}

# SpreadsheetMLStyles_Header class attributes and methods

# HeaderOrFooterElt class attributes and methods

# SpreadsheetMLStyles_PageMarginsInfo class attributes and methods
SpreadsheetMLStyles_PageMarginsInfo_left: Property = Property(name="left", type=StringType)
SpreadsheetMLStyles_PageMarginsInfo_right: Property = Property(name="right", type=StringType)
SpreadsheetMLStyles_PageMarginsInfo_top: Property = Property(name="top", type=StringType)
SpreadsheetMLStyles_PageMarginsInfo_bottom: Property = Property(name="bottom", type=StringType)
SpreadsheetMLStyles_PageMarginsInfo.attributes={SpreadsheetMLStyles_PageMarginsInfo_bottom, SpreadsheetMLStyles_PageMarginsInfo_top, SpreadsheetMLStyles_PageMarginsInfo_left, SpreadsheetMLStyles_PageMarginsInfo_right}

# SpreadsheetMLStyles_Print class attributes and methods
SpreadsheetMLStyles_Print_blackAndWhite: Property = Property(name="blackAndWhite", type=StringType)
SpreadsheetMLStyles_Print_draftQuality: Property = Property(name="draftQuality", type=StringType)
SpreadsheetMLStyles_Print_commentsLayout: Property = Property(name="commentsLayout", type=StringType)
SpreadsheetMLStyles_Print_scale: Property = Property(name="scale", type=StringType)
SpreadsheetMLStyles_Print_printErrors: Property = Property(name="printErrors", type=StringType)
SpreadsheetMLStyles_Print_validPrinterInfo: Property = Property(name="validPrinterInfo", type=StringType)
SpreadsheetMLStyles_Print_paperSizeIndex: Property = Property(name="paperSizeIndex", type=StringType)
SpreadsheetMLStyles_Print_horizontalResolution: Property = Property(name="horizontalResolution", type=StringType)
SpreadsheetMLStyles_Print_fitWidth: Property = Property(name="fitWidth", type=StringType)
SpreadsheetMLStyles_Print_fitHeight: Property = Property(name="fitHeight", type=StringType)
SpreadsheetMLStyles_Print_leftToRight: Property = Property(name="leftToRight", type=StringType)
SpreadsheetMLStyles_Print_verticalResolution: Property = Property(name="verticalResolution", type=StringType)
SpreadsheetMLStyles_Print_gridlines: Property = Property(name="gridlines", type=StringType)
SpreadsheetMLStyles_Print_numberOfCopies: Property = Property(name="numberOfCopies", type=StringType)
SpreadsheetMLStyles_Print_rowColHeadings: Property = Property(name="rowColHeadings", type=StringType)
SpreadsheetMLStyles_Print.attributes={SpreadsheetMLStyles_Print_fitWidth, SpreadsheetMLStyles_Print_verticalResolution, SpreadsheetMLStyles_Print_printErrors, SpreadsheetMLStyles_Print_horizontalResolution, SpreadsheetMLStyles_Print_blackAndWhite, SpreadsheetMLStyles_Print_scale, SpreadsheetMLStyles_Print_paperSizeIndex, SpreadsheetMLStyles_Print_numberOfCopies, SpreadsheetMLStyles_Print_draftQuality, SpreadsheetMLStyles_Print_gridlines, SpreadsheetMLStyles_Print_rowColHeadings, SpreadsheetMLStyles_Print_fitHeight, SpreadsheetMLStyles_Print_validPrinterInfo, SpreadsheetMLStyles_Print_commentsLayout, SpreadsheetMLStyles_Print_leftToRight}

# SpreadsheetMLStyles_Footer class attributes and methods

# SpreadsheetMLStyles_StylesCollection class attributes and methods

# SpreadsheetMLStyles_StyleType class attributes and methods
SpreadsheetMLStyles_StyleType_id: Property = Property(name="id", type=StringType)
SpreadsheetMLStyles_StyleType_name: Property = Property(name="name", type=StringType)
SpreadsheetMLStyles_StyleType.attributes={SpreadsheetMLStyles_StyleType_name, SpreadsheetMLStyles_StyleType_id}

# AlignmentType class attributes and methods

# BordersType class attributes and methods

# InteriorType class attributes and methods

# NumberFormatType class attributes and methods

# ProtectionType class attributes and methods

# SpreadsheetMLStyles_ProtectionType class attributes and methods
SpreadsheetMLStyles_ProtectionType_protected: Property = Property(name="protected", type=StringType)
SpreadsheetMLStyles_ProtectionType.attributes={SpreadsheetMLStyles_ProtectionType_protected}

# FontType class attributes and methods

# SpreadsheetMLStyles_AlignmentType class attributes and methods
SpreadsheetMLStyles_AlignmentType_horizontal: Property = Property(name="horizontal", type=StringType)
SpreadsheetMLStyles_AlignmentType_shrinkToFit: Property = Property(name="shrinkToFit", type=StringType)
SpreadsheetMLStyles_AlignmentType_vertical: Property = Property(name="vertical", type=StringType)
SpreadsheetMLStyles_AlignmentType_verticalText: Property = Property(name="verticalText", type=StringType)
SpreadsheetMLStyles_AlignmentType_wrapText: Property = Property(name="wrapText", type=StringType)
SpreadsheetMLStyles_AlignmentType_readingOrder: Property = Property(name="readingOrder", type=StringType)
SpreadsheetMLStyles_AlignmentType_indent: Property = Property(name="indent", type=StringType)
SpreadsheetMLStyles_AlignmentType_rotate: Property = Property(name="rotate", type=StringType)
SpreadsheetMLStyles_AlignmentType.attributes={SpreadsheetMLStyles_AlignmentType_readingOrder, SpreadsheetMLStyles_AlignmentType_shrinkToFit, SpreadsheetMLStyles_AlignmentType_vertical, SpreadsheetMLStyles_AlignmentType_verticalText, SpreadsheetMLStyles_AlignmentType_indent, SpreadsheetMLStyles_AlignmentType_rotate, SpreadsheetMLStyles_AlignmentType_horizontal, SpreadsheetMLStyles_AlignmentType_wrapText}

# SpreadsheetMLStyles_BorderType class attributes and methods
SpreadsheetMLStyles_BorderType_position: Property = Property(name="position", type=StringType)
SpreadsheetMLStyles_BorderType_color: Property = Property(name="color", type=StringType)
SpreadsheetMLStyles_BorderType_lineStyle: Property = Property(name="lineStyle", type=StringType)
SpreadsheetMLStyles_BorderType_weight: Property = Property(name="weight", type=StringType)
SpreadsheetMLStyles_BorderType.attributes={SpreadsheetMLStyles_BorderType_lineStyle, SpreadsheetMLStyles_BorderType_position, SpreadsheetMLStyles_BorderType_weight, SpreadsheetMLStyles_BorderType_color}

# SpreadsheetMLStyles_BordersType class attributes and methods

# BorderType class attributes and methods

# SpreadsheetMLStyles_FontType class attributes and methods
SpreadsheetMLStyles_FontType_italic: Property = Property(name="italic", type=StringType)
SpreadsheetMLStyles_FontType_outline: Property = Property(name="outline", type=StringType)
SpreadsheetMLStyles_FontType_bold: Property = Property(name="bold", type=StringType)
SpreadsheetMLStyles_FontType_color: Property = Property(name="color", type=StringType)
SpreadsheetMLStyles_FontType_fontName: Property = Property(name="fontName", type=StringType)
SpreadsheetMLStyles_FontType_shadow: Property = Property(name="shadow", type=StringType)
SpreadsheetMLStyles_FontType_size: Property = Property(name="size", type=StringType)
SpreadsheetMLStyles_FontType_strikeThrough: Property = Property(name="strikeThrough", type=StringType)
SpreadsheetMLStyles_FontType_underline: Property = Property(name="underline", type=StringType)
SpreadsheetMLStyles_FontType_verticalAlign: Property = Property(name="verticalAlign", type=StringType)
SpreadsheetMLStyles_FontType.attributes={SpreadsheetMLStyles_FontType_italic, SpreadsheetMLStyles_FontType_underline, SpreadsheetMLStyles_FontType_outline, SpreadsheetMLStyles_FontType_verticalAlign, SpreadsheetMLStyles_FontType_bold, SpreadsheetMLStyles_FontType_color, SpreadsheetMLStyles_FontType_strikeThrough, SpreadsheetMLStyles_FontType_size, SpreadsheetMLStyles_FontType_shadow, SpreadsheetMLStyles_FontType_fontName}

# SpreadsheetMLStyles_InteriorType class attributes and methods
SpreadsheetMLStyles_InteriorType_color: Property = Property(name="color", type=StringType)
SpreadsheetMLStyles_InteriorType_pattern: Property = Property(name="pattern", type=StringType)
SpreadsheetMLStyles_InteriorType_patternColor: Property = Property(name="patternColor", type=StringType)
SpreadsheetMLStyles_InteriorType.attributes={SpreadsheetMLStyles_InteriorType_patternColor, SpreadsheetMLStyles_InteriorType_pattern, SpreadsheetMLStyles_InteriorType_color}

# SpreadsheetMLStyles_NumberFormatType class attributes and methods
SpreadsheetMLStyles_NumberFormatType_format: Property = Property(name="format", type=StringType)
SpreadsheetMLStyles_NumberFormatType.attributes={SpreadsheetMLStyles_NumberFormatType_format}

# NamedRange class attributes and methods

# SpreadsheetMLStyles_NamesType class attributes and methods

# SpreadsheetMLStyles_NamedRange class attributes and methods
SpreadsheetMLStyles_NamedRange_name: Property = Property(name="name", type=StringType)
SpreadsheetMLStyles_NamedRange_refersTo: Property = Property(name="refersTo", type=StringType)
SpreadsheetMLStyles_NamedRange_hidden: Property = Property(name="hidden", type=StringType)
SpreadsheetMLStyles_NamedRange.attributes={SpreadsheetMLStyles_NamedRange_refersTo, SpreadsheetMLStyles_NamedRange_name, SpreadsheetMLStyles_NamedRange_hidden}

# Relationships
vt_data0: BinaryAssociation = BinaryAssociation(
    name="vt_data0",
    ends={
        Property(name="Data", type=SpreadsheetMLStyles_ValueType, multiplicity=Multiplicity(1, 1)),
        Property(name="value", type=Data, multiplicity=Multiplicity(1, 1))
    }
)
value1: BinaryAssociation = BinaryAssociation(
    name="value1",
    ends={
        Property(name="DateTimeType", type=SpreadsheetMLStyles_DateTimeTypeValue, multiplicity=Multiplicity(1, 1)),
        Property(name="SpreadsheetMLStyles_DateTimeTypeValue", type=DateTimeType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
dp_workbook2: BinaryAssociation = BinaryAssociation(
    name="dp_workbook2",
    ends={
        Property(name="Workbook", type=SpreadsheetMLStyles_DocumentPropertiesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="wb_docProperties", type=Workbook, multiplicity=Multiplicity(1, 1))
    }
)
version3: BinaryAssociation = BinaryAssociation(
    name="version3",
    ends={
        Property(name="VersionType", type=SpreadsheetMLStyles_DocumentPropertiesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="SpreadsheetMLStyles_DocumentPropertiesCollection", type=VersionType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lastPrinted4: BinaryAssociation = BinaryAssociation(
    name="lastPrinted4",
    ends={
        Property(name="DateTimeType6", type=SpreadsheetMLStyles_DocumentPropertiesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="SpreadsheetMLStyles_DocumentPropertiesCollection5", type=DateTimeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
created7: BinaryAssociation = BinaryAssociation(
    name="created7",
    ends={
        Property(name="DateTimeType9", type=SpreadsheetMLStyles_DocumentPropertiesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="SpreadsheetMLStyles_DocumentPropertiesCollection8", type=DateTimeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lastSaved10: BinaryAssociation = BinaryAssociation(
    name="lastSaved10",
    ends={
        Property(name="DateTimeType12", type=SpreadsheetMLStyles_DocumentPropertiesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="SpreadsheetMLStyles_DocumentPropertiesCollection11", type=DateTimeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cdp_workbook13: BinaryAssociation = BinaryAssociation(
    name="cdp_workbook13",
    ends={
        Property(name="Workbook14", type=SpreadsheetMLStyles_CustomDocumentPropertiesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="wb_customDocProperties", type=Workbook, multiplicity=Multiplicity(1, 1))
    }
)
customDocumentProperties15: BinaryAssociation = BinaryAssociation(
    name="customDocumentProperties15",
    ends={
        Property(name="CustomDocumentProperty", type=SpreadsheetMLStyles_CustomDocumentPropertiesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="customDocumentProperty_cdpe", type=CustomDocumentProperty, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
customDocumentProperty_cdpe16: BinaryAssociation = BinaryAssociation(
    name="customDocumentProperty_cdpe16",
    ends={
        Property(name="CustomDocumentPropertiesCollection", type=SpreadsheetMLStyles_CustomDocumentProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="customDocumentProperties", type=CustomDocumentPropertiesCollection, multiplicity=Multiplicity(1, 1))
    }
)
value17: BinaryAssociation = BinaryAssociation(
    name="value17",
    ends={
        Property(name="ValueType", type=SpreadsheetMLStyles_CustomDocumentProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="SpreadsheetMLStyles_CustomDocumentProperty", type=ValueType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
smartTagType_ste18: BinaryAssociation = BinaryAssociation(
    name="smartTagType_ste18",
    ends={
        Property(name="SmartTagsCollection", type=SpreadsheetMLStyles_SmartTagType, multiplicity=Multiplicity(1, 1)),
        Property(name="smartTagTypes", type=SmartTagsCollection, multiplicity=Multiplicity(1, 1))
    }
)
st_workbook19: BinaryAssociation = BinaryAssociation(
    name="st_workbook19",
    ends={
        Property(name="Workbook20", type=SpreadsheetMLStyles_SmartTagsCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="wb_smartTags", type=Workbook, multiplicity=Multiplicity(1, 1))
    }
)
st_cell21: BinaryAssociation = BinaryAssociation(
    name="st_cell21",
    ends={
        Property(name="Cell", type=SpreadsheetMLStyles_SmartTagsCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="c_smartTags", type=Cell, multiplicity=Multiplicity(1, 1))
    }
)
smartTagTypes22: BinaryAssociation = BinaryAssociation(
    name="smartTagTypes22",
    ends={
        Property(name="SmartTagType", type=SpreadsheetMLStyles_SmartTagsCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="smartTagType_ste", type=SmartTagType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
wb_worksheets31: BinaryAssociation = BinaryAssociation(
    name="wb_worksheets31",
    ends={
        Property(name="Worksheet", type=SpreadsheetMLStyles_Workbook, multiplicity=Multiplicity(1, 1)),
        Property(name="ws_workbook", type=Worksheet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
wb_smartTags23: BinaryAssociation = BinaryAssociation(
    name="wb_smartTags23",
    ends={
        Property(name="SmartTagsCollection24", type=SpreadsheetMLStyles_Workbook, multiplicity=Multiplicity(1, 1)),
        Property(name="st_workbook", type=SmartTagsCollection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
wb_docProperties25: BinaryAssociation = BinaryAssociation(
    name="wb_docProperties25",
    ends={
        Property(name="DocumentPropertiesCollection", type=SpreadsheetMLStyles_Workbook, multiplicity=Multiplicity(1, 1)),
        Property(name="dp_workbook", type=DocumentPropertiesCollection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
wb_customDocProperties26: BinaryAssociation = BinaryAssociation(
    name="wb_customDocProperties26",
    ends={
        Property(name="CustomDocumentPropertiesCollection27", type=SpreadsheetMLStyles_Workbook, multiplicity=Multiplicity(1, 1)),
        Property(name="cdp_workbook", type=CustomDocumentPropertiesCollection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
wb_excelWorkbook28: BinaryAssociation = BinaryAssociation(
    name="wb_excelWorkbook28",
    ends={
        Property(name="ExcelWorkbook", type=SpreadsheetMLStyles_Workbook, multiplicity=Multiplicity(1, 1)),
        Property(name="ew_workbook", type=ExcelWorkbook, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
wb_styles29: BinaryAssociation = BinaryAssociation(
    name="wb_styles29",
    ends={
        Property(name="StylesCollection", type=SpreadsheetMLStyles_Workbook, multiplicity=Multiplicity(1, 1)),
        Property(name="s_workbook", type=StylesCollection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
wb_names30: BinaryAssociation = BinaryAssociation(
    name="wb_names30",
    ends={
        Property(name="NamesType", type=SpreadsheetMLStyles_Workbook, multiplicity=Multiplicity(1, 1)),
        Property(name="nt_workbook", type=NamesType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
styleID36: BinaryAssociation = BinaryAssociation(
    name="styleID36",
    ends={
        Property(name="st_styledElement", type=StyleType, multiplicity=Multiplicity(0, 1)),
        Property(name="StyleType", type=SpreadsheetMLStyles_StyledElement, multiplicity=Multiplicity(1, 1))
    }
)
ws_workbook32: BinaryAssociation = BinaryAssociation(
    name="ws_workbook32",
    ends={
        Property(name="Workbook33", type=SpreadsheetMLStyles_Worksheet, multiplicity=Multiplicity(1, 1)),
        Property(name="wb_worksheets", type=Workbook, multiplicity=Multiplicity(1, 1))
    }
)
ws_table34: BinaryAssociation = BinaryAssociation(
    name="ws_table34",
    ends={
        Property(name="Table", type=SpreadsheetMLStyles_Worksheet, multiplicity=Multiplicity(1, 1)),
        Property(name="t_worksheet", type=Table, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
w_worksheetOptions35: BinaryAssociation = BinaryAssociation(
    name="w_worksheetOptions35",
    ends={
        Property(name="WorksheetOptionsElt", type=SpreadsheetMLStyles_Worksheet, multiplicity=Multiplicity(1, 1)),
        Property(name="wo_worksheet", type=WorksheetOptionsElt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
t_worksheet37: BinaryAssociation = BinaryAssociation(
    name="t_worksheet37",
    ends={
        Property(name="Worksheet38", type=SpreadsheetMLStyles_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="ws_table", type=Worksheet, multiplicity=Multiplicity(1, 1))
    }
)
t_cols39: BinaryAssociation = BinaryAssociation(
    name="t_cols39",
    ends={
        Property(name="Column", type=SpreadsheetMLStyles_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="c_table", type=Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
t_rows40: BinaryAssociation = BinaryAssociation(
    name="t_rows40",
    ends={
        Property(name="Row", type=SpreadsheetMLStyles_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="r_table", type=Row, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
r_table43: BinaryAssociation = BinaryAssociation(
    name="r_table43",
    ends={
        Property(name="Table44", type=SpreadsheetMLStyles_Row, multiplicity=Multiplicity(1, 1)),
        Property(name="t_rows", type=Table, multiplicity=Multiplicity(1, 1))
    }
)
c_table41: BinaryAssociation = BinaryAssociation(
    name="c_table41",
    ends={
        Property(name="Table42", type=SpreadsheetMLStyles_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="t_cols", type=Table, multiplicity=Multiplicity(1, 1))
    }
)
c_smartTags47: BinaryAssociation = BinaryAssociation(
    name="c_smartTags47",
    ends={
        Property(name="SmartTagsCollection48", type=SpreadsheetMLStyles_Cell, multiplicity=Multiplicity(1, 1)),
        Property(name="st_cell", type=SmartTagsCollection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
c_row49: BinaryAssociation = BinaryAssociation(
    name="c_row49",
    ends={
        Property(name="Row50", type=SpreadsheetMLStyles_Cell, multiplicity=Multiplicity(1, 1)),
        Property(name="r_cells", type=Row, multiplicity=Multiplicity(1, 1))
    }
)
r_cells45: BinaryAssociation = BinaryAssociation(
    name="r_cells45",
    ends={
        Property(name="Cell46", type=SpreadsheetMLStyles_Row, multiplicity=Multiplicity(1, 1)),
        Property(name="c_row", type=Cell, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
c_cell54: BinaryAssociation = BinaryAssociation(
    name="c_cell54",
    ends={
        Property(name="Cell55", type=SpreadsheetMLStyles_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="c_comment", type=Cell, multiplicity=Multiplicity(1, 1))
    }
)
c_data51: BinaryAssociation = BinaryAssociation(
    name="c_data51",
    ends={
        Property(name="Data52", type=SpreadsheetMLStyles_Cell, multiplicity=Multiplicity(1, 1)),
        Property(name="d_cell", type=Data, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
c_comment53: BinaryAssociation = BinaryAssociation(
    name="c_comment53",
    ends={
        Property(name="Comment", type=SpreadsheetMLStyles_Cell, multiplicity=Multiplicity(1, 1)),
        Property(name="c_cell", type=Comment, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
d_comment60: BinaryAssociation = BinaryAssociation(
    name="d_comment60",
    ends={
        Property(name="Comment61", type=SpreadsheetMLStyles_Data, multiplicity=Multiplicity(1, 1)),
        Property(name="com_data", type=Comment, multiplicity=Multiplicity(1, 1))
    }
)
com_data56: BinaryAssociation = BinaryAssociation(
    name="com_data56",
    ends={
        Property(name="Data57", type=SpreadsheetMLStyles_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="d_comment", type=Data, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value62: BinaryAssociation = BinaryAssociation(
    name="value62",
    ends={
        Property(name="ValueType63", type=SpreadsheetMLStyles_Data, multiplicity=Multiplicity(1, 1)),
        Property(name="vt_data", type=ValueType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
d_cell58: BinaryAssociation = BinaryAssociation(
    name="d_cell58",
    ends={
        Property(name="Cell59", type=SpreadsheetMLStyles_Data, multiplicity=Multiplicity(1, 1)),
        Property(name="c_data", type=Cell, multiplicity=Multiplicity(1, 1))
    }
)
ew_workbook64: BinaryAssociation = BinaryAssociation(
    name="ew_workbook64",
    ends={
        Property(name="Workbook65", type=SpreadsheetMLStyles_ExcelWorkbook, multiplicity=Multiplicity(1, 1)),
        Property(name="wb_excelWorkbook", type=Workbook, multiplicity=Multiplicity(1, 1))
    }
)
wo_worksheet66: BinaryAssociation = BinaryAssociation(
    name="wo_worksheet66",
    ends={
        Property(name="Worksheet67", type=SpreadsheetMLStyles_WorksheetOptionsElt, multiplicity=Multiplicity(1, 1)),
        Property(name="w_worksheetOptions", type=Worksheet, multiplicity=Multiplicity(1, 1))
    }
)
wo_print69: BinaryAssociation = BinaryAssociation(
    name="wo_print69",
    ends={
        Property(name="p_worksheetOptions", type=Print, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="Print", type=SpreadsheetMLStyles_WorksheetOptionsElt, multiplicity=Multiplicity(1, 1))
    }
)
wo_pageSetup68: BinaryAssociation = BinaryAssociation(
    name="wo_pageSetup68",
    ends={
        Property(name="PageSetup", type=SpreadsheetMLStyles_WorksheetOptionsElt, multiplicity=Multiplicity(1, 1)),
        Property(name="ps_worksheetOptions", type=PageSetup, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ps_header73: BinaryAssociation = BinaryAssociation(
    name="ps_header73",
    ends={
        Property(name="Header", type=SpreadsheetMLStyles_PageSetup, multiplicity=Multiplicity(1, 1)),
        Property(name="h_pageSetup", type=Header, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ps_footer74: BinaryAssociation = BinaryAssociation(
    name="ps_footer74",
    ends={
        Property(name="Footer", type=SpreadsheetMLStyles_PageSetup, multiplicity=Multiplicity(1, 1)),
        Property(name="f_pageSetup", type=Footer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ps_pageMargins75: BinaryAssociation = BinaryAssociation(
    name="ps_pageMargins75",
    ends={
        Property(name="PageMarginsInfo", type=SpreadsheetMLStyles_PageSetup, multiplicity=Multiplicity(1, 1)),
        Property(name="pm_pageSetup", type=PageMarginsInfo, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
l_pageSetup76: BinaryAssociation = BinaryAssociation(
    name="l_pageSetup76",
    ends={
        Property(name="PageSetup77", type=SpreadsheetMLStyles_Layout, multiplicity=Multiplicity(1, 1)),
        Property(name="ps_layout", type=PageSetup, multiplicity=Multiplicity(1, 1))
    }
)
ps_worksheetOptions70: BinaryAssociation = BinaryAssociation(
    name="ps_worksheetOptions70",
    ends={
        Property(name="WorksheetOptionsElt71", type=SpreadsheetMLStyles_PageSetup, multiplicity=Multiplicity(1, 1)),
        Property(name="wo_pageSetup", type=WorksheetOptionsElt, multiplicity=Multiplicity(1, 1))
    }
)
ps_layout72: BinaryAssociation = BinaryAssociation(
    name="ps_layout72",
    ends={
        Property(name="Layout", type=SpreadsheetMLStyles_PageSetup, multiplicity=Multiplicity(1, 1)),
        Property(name="l_pageSetup", type=Layout, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
h_pageSetup78: BinaryAssociation = BinaryAssociation(
    name="h_pageSetup78",
    ends={
        Property(name="PageSetup79", type=SpreadsheetMLStyles_Header, multiplicity=Multiplicity(1, 1)),
        Property(name="ps_header", type=PageSetup, multiplicity=Multiplicity(1, 1))
    }
)
pm_pageSetup82: BinaryAssociation = BinaryAssociation(
    name="pm_pageSetup82",
    ends={
        Property(name="PageSetup83", type=SpreadsheetMLStyles_PageMarginsInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="ps_pageMargins", type=PageSetup, multiplicity=Multiplicity(1, 1))
    }
)
f_pageSetup80: BinaryAssociation = BinaryAssociation(
    name="f_pageSetup80",
    ends={
        Property(name="PageSetup81", type=SpreadsheetMLStyles_Footer, multiplicity=Multiplicity(1, 1)),
        Property(name="ps_footer", type=PageSetup, multiplicity=Multiplicity(1, 1))
    }
)
p_worksheetOptions84: BinaryAssociation = BinaryAssociation(
    name="p_worksheetOptions84",
    ends={
        Property(name="WorksheetOptionsElt85", type=SpreadsheetMLStyles_Print, multiplicity=Multiplicity(1, 1)),
        Property(name="wo_print", type=WorksheetOptionsElt, multiplicity=Multiplicity(1, 1))
    }
)
s_workbook86: BinaryAssociation = BinaryAssociation(
    name="s_workbook86",
    ends={
        Property(name="Workbook87", type=SpreadsheetMLStyles_StylesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="wb_styles", type=Workbook, multiplicity=Multiplicity(1, 1))
    }
)
style88: BinaryAssociation = BinaryAssociation(
    name="style88",
    ends={
        Property(name="StyleType89", type=SpreadsheetMLStyles_StylesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="st_styles", type=StyleType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent93: BinaryAssociation = BinaryAssociation(
    name="parent93",
    ends={
        Property(name="StyleType94", type=SpreadsheetMLStyles_StyleType, multiplicity=Multiplicity(1, 1)),
        Property(name="st_parent", type=StyleType, multiplicity=Multiplicity(0, 1))
    }
)
st_parent95: BinaryAssociation = BinaryAssociation(
    name="st_parent95",
    ends={
        Property(name="StyleType96", type=SpreadsheetMLStyles_StyleType, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=StyleType, multiplicity=Multiplicity(1, 1))
    }
)
alignment97: BinaryAssociation = BinaryAssociation(
    name="alignment97",
    ends={
        Property(name="AlignmentType", type=SpreadsheetMLStyles_StyleType, multiplicity=Multiplicity(1, 1)),
        Property(name="at_styleType", type=AlignmentType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
st_styles90: BinaryAssociation = BinaryAssociation(
    name="st_styles90",
    ends={
        Property(name="StylesCollection91", type=SpreadsheetMLStyles_StyleType, multiplicity=Multiplicity(1, 1)),
        Property(name="style", type=StylesCollection, multiplicity=Multiplicity(1, 1))
    }
)
st_styledElement92: BinaryAssociation = BinaryAssociation(
    name="st_styledElement92",
    ends={
        Property(name="StyledElement", type=SpreadsheetMLStyles_StyleType, multiplicity=Multiplicity(1, 1)),
        Property(name="styleID", type=StyledElement, multiplicity=Multiplicity(1, 1))
    }
)
interior100: BinaryAssociation = BinaryAssociation(
    name="interior100",
    ends={
        Property(name="InteriorType", type=SpreadsheetMLStyles_StyleType, multiplicity=Multiplicity(1, 1)),
        Property(name="it_styleType", type=InteriorType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
numberFormat101: BinaryAssociation = BinaryAssociation(
    name="numberFormat101",
    ends={
        Property(name="NumberFormatType", type=SpreadsheetMLStyles_StyleType, multiplicity=Multiplicity(1, 1)),
        Property(name="nft_styleType", type=NumberFormatType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
protection102: BinaryAssociation = BinaryAssociation(
    name="protection102",
    ends={
        Property(name="ProtectionType", type=SpreadsheetMLStyles_StyleType, multiplicity=Multiplicity(1, 1)),
        Property(name="pt_styleType", type=ProtectionType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pt_styleType103: BinaryAssociation = BinaryAssociation(
    name="pt_styleType103",
    ends={
        Property(name="StyleType104", type=SpreadsheetMLStyles_ProtectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="protection", type=StyleType, multiplicity=Multiplicity(1, 1))
    }
)
borders98: BinaryAssociation = BinaryAssociation(
    name="borders98",
    ends={
        Property(name="BordersType", type=SpreadsheetMLStyles_StyleType, multiplicity=Multiplicity(1, 1)),
        Property(name="bt_styleType", type=BordersType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
font99: BinaryAssociation = BinaryAssociation(
    name="font99",
    ends={
        Property(name="FontType", type=SpreadsheetMLStyles_StyleType, multiplicity=Multiplicity(1, 1)),
        Property(name="ft_styleType", type=FontType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
at_styleType105: BinaryAssociation = BinaryAssociation(
    name="at_styleType105",
    ends={
        Property(name="StyleType106", type=SpreadsheetMLStyles_AlignmentType, multiplicity=Multiplicity(1, 1)),
        Property(name="alignment", type=StyleType, multiplicity=Multiplicity(1, 1))
    }
)
bt_styleType107: BinaryAssociation = BinaryAssociation(
    name="bt_styleType107",
    ends={
        Property(name="StyleType108", type=SpreadsheetMLStyles_BordersType, multiplicity=Multiplicity(1, 1)),
        Property(name="borders", type=StyleType, multiplicity=Multiplicity(1, 1))
    }
)
border109: BinaryAssociation = BinaryAssociation(
    name="border109",
    ends={
        Property(name="BorderType", type=SpreadsheetMLStyles_BordersType, multiplicity=Multiplicity(1, 1)),
        Property(name="bt_bordersType", type=BorderType, multiplicity=Multiplicity(0, 6), is_composite=True)
    }
)
bt_bordersType110: BinaryAssociation = BinaryAssociation(
    name="bt_bordersType110",
    ends={
        Property(name="BordersType111", type=SpreadsheetMLStyles_BorderType, multiplicity=Multiplicity(1, 1)),
        Property(name="border", type=BordersType, multiplicity=Multiplicity(1, 1))
    }
)
ft_styleType112: BinaryAssociation = BinaryAssociation(
    name="ft_styleType112",
    ends={
        Property(name="StyleType113", type=SpreadsheetMLStyles_FontType, multiplicity=Multiplicity(1, 1)),
        Property(name="font", type=StyleType, multiplicity=Multiplicity(1, 1))
    }
)
it_styleType114: BinaryAssociation = BinaryAssociation(
    name="it_styleType114",
    ends={
        Property(name="StyleType115", type=SpreadsheetMLStyles_InteriorType, multiplicity=Multiplicity(1, 1)),
        Property(name="interior", type=StyleType, multiplicity=Multiplicity(1, 1))
    }
)
nft_styleType116: BinaryAssociation = BinaryAssociation(
    name="nft_styleType116",
    ends={
        Property(name="StyleType117", type=SpreadsheetMLStyles_NumberFormatType, multiplicity=Multiplicity(1, 1)),
        Property(name="numberFormat", type=StyleType, multiplicity=Multiplicity(1, 1))
    }
)
namedRanges120: BinaryAssociation = BinaryAssociation(
    name="namedRanges120",
    ends={
        Property(name="NamedRange", type=SpreadsheetMLStyles_NamesType, multiplicity=Multiplicity(1, 1)),
        Property(name="nr_namesType", type=NamedRange, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nt_workbook118: BinaryAssociation = BinaryAssociation(
    name="nt_workbook118",
    ends={
        Property(name="Workbook119", type=SpreadsheetMLStyles_NamesType, multiplicity=Multiplicity(1, 1)),
        Property(name="wb_names", type=Workbook, multiplicity=Multiplicity(1, 1))
    }
)
nr_namesType121: BinaryAssociation = BinaryAssociation(
    name="nr_namesType121",
    ends={
        Property(name="NamesType122", type=SpreadsheetMLStyles_NamedRange, multiplicity=Multiplicity(1, 1)),
        Property(name="namedRanges", type=NamesType, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_SpreadsheetMLStyles_StringValue_ValueType = Generalization(general=ValueType, specific=SpreadsheetMLStyles_StringValue)
gen_SpreadsheetMLStyles_DateTimeTypeValue_ValueType = Generalization(general=ValueType, specific=SpreadsheetMLStyles_DateTimeTypeValue)
gen_SpreadsheetMLStyles_BooleanValue_ValueType = Generalization(general=ValueType, specific=SpreadsheetMLStyles_BooleanValue)
gen_SpreadsheetMLStyles_ErrorValue_ValueType = Generalization(general=ValueType, specific=SpreadsheetMLStyles_ErrorValue)
gen_SpreadsheetMLStyles_NumberValue_ValueType = Generalization(general=ValueType, specific=SpreadsheetMLStyles_NumberValue)
gen_SpreadsheetMLStyles_Table_StyledElement = Generalization(general=StyledElement, specific=SpreadsheetMLStyles_Table)
gen_SpreadsheetMLStyles_Row_ColOrRowElement = Generalization(general=ColOrRowElement, specific=SpreadsheetMLStyles_Row)
gen_SpreadsheetMLStyles_TableElement_StyledElement = Generalization(general=StyledElement, specific=SpreadsheetMLStyles_TableElement)
gen_SpreadsheetMLStyles_ColOrRowElement_TableElement = Generalization(general=TableElement, specific=SpreadsheetMLStyles_ColOrRowElement)
gen_SpreadsheetMLStyles_Column_ColOrRowElement = Generalization(general=ColOrRowElement, specific=SpreadsheetMLStyles_Column)
gen_SpreadsheetMLStyles_Cell_TableElement = Generalization(general=TableElement, specific=SpreadsheetMLStyles_Cell)
gen_SpreadsheetMLStyles_Header_HeaderOrFooterElt = Generalization(general=HeaderOrFooterElt, specific=SpreadsheetMLStyles_Header)
gen_SpreadsheetMLStyles_Footer_HeaderOrFooterElt = Generalization(general=HeaderOrFooterElt, specific=SpreadsheetMLStyles_Footer)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={SpreadsheetMLStyles_DateTimeType, SpreadsheetMLStyles_VersionType, SpreadsheetMLStyles_ValueType, Data, SpreadsheetMLStyles_StringValue, ValueType, SpreadsheetMLStyles_NumberValue, SpreadsheetMLStyles_DateTimeTypeValue, DateTimeType, SpreadsheetMLStyles_BooleanValue, SpreadsheetMLStyles_ErrorValue, SpreadsheetMLStyles_DocumentPropertiesCollection, Workbook, VersionType, SpreadsheetMLStyles_CustomDocumentPropertiesCollection, CustomDocumentProperty, SpreadsheetMLStyles_CustomDocumentProperty, CustomDocumentPropertiesCollection, SpreadsheetMLStyles_Workbook, SpreadsheetMLStyles_SmartTagType, SmartTagsCollection, SpreadsheetMLStyles_SmartTagsCollection, Cell, SmartTagType, Worksheet, DocumentPropertiesCollection, ExcelWorkbook, StylesCollection, NamesType, SpreadsheetMLStyles_Table, SpreadsheetMLStyles_Worksheet, Table, WorksheetOptionsElt, SpreadsheetMLStyles_StyledElement, StyleType, StyledElement, Column, Row, SpreadsheetMLStyles_Row, SpreadsheetMLStyles_TableElement, SpreadsheetMLStyles_ColOrRowElement, TableElement, SpreadsheetMLStyles_Column, ColOrRowElement, SpreadsheetMLStyles_Cell, SpreadsheetMLStyles_Comment, Comment, SpreadsheetMLStyles_Data, SpreadsheetMLStyles_ExcelWorkbook, SpreadsheetMLStyles_WorksheetOptionsElt, PageSetup, Print, Header, Footer, PageMarginsInfo, SpreadsheetMLStyles_Layout, SpreadsheetMLStyles_PageSetup, Layout, SpreadsheetMLStyles_HeaderOrFooterElt, SpreadsheetMLStyles_Header, HeaderOrFooterElt, SpreadsheetMLStyles_PageMarginsInfo, SpreadsheetMLStyles_Print, SpreadsheetMLStyles_Footer, SpreadsheetMLStyles_StylesCollection, SpreadsheetMLStyles_StyleType, AlignmentType, BordersType, InteriorType, NumberFormatType, ProtectionType, SpreadsheetMLStyles_ProtectionType, FontType, SpreadsheetMLStyles_AlignmentType, SpreadsheetMLStyles_BorderType, SpreadsheetMLStyles_BordersType, BorderType, SpreadsheetMLStyles_FontType, SpreadsheetMLStyles_InteriorType, SpreadsheetMLStyles_NumberFormatType, NamedRange, SpreadsheetMLStyles_NamesType, SpreadsheetMLStyles_NamedRange, DisplayDrawingObjectsType, CalculationWorkbookType, ExcelWorksheetTypeType, VisibleType, EnableSelectionType, OrientationType, CommentsLayoutType, HorizontalAlignementType, ReadingOrderType, VerticalAlignementType, LineStyleType, PositionType, UnderlineType, VerticalAlignType, PatternType, ExcelNumberFormatType},
    associations={vt_data0, value1, dp_workbook2, version3, lastPrinted4, created7, lastSaved10, cdp_workbook13, customDocumentProperties15, customDocumentProperty_cdpe16, value17, smartTagType_ste18, st_workbook19, st_cell21, smartTagTypes22, wb_worksheets31, wb_smartTags23, wb_docProperties25, wb_customDocProperties26, wb_excelWorkbook28, wb_styles29, wb_names30, styleID36, ws_workbook32, ws_table34, w_worksheetOptions35, t_worksheet37, t_cols39, t_rows40, r_table43, c_table41, c_smartTags47, c_row49, r_cells45, c_cell54, c_data51, c_comment53, d_comment60, com_data56, value62, d_cell58, ew_workbook64, wo_worksheet66, wo_print69, wo_pageSetup68, ps_header73, ps_footer74, ps_pageMargins75, l_pageSetup76, ps_worksheetOptions70, ps_layout72, h_pageSetup78, pm_pageSetup82, f_pageSetup80, p_worksheetOptions84, s_workbook86, style88, parent93, st_parent95, alignment97, st_styles90, st_styledElement92, interior100, numberFormat101, protection102, pt_styleType103, borders98, font99, at_styleType105, bt_styleType107, border109, bt_bordersType110, ft_styleType112, it_styleType114, nft_styleType116, namedRanges120, nt_workbook118, nr_namesType121},
    generalizations={gen_SpreadsheetMLStyles_StringValue_ValueType, gen_SpreadsheetMLStyles_DateTimeTypeValue_ValueType, gen_SpreadsheetMLStyles_BooleanValue_ValueType, gen_SpreadsheetMLStyles_ErrorValue_ValueType, gen_SpreadsheetMLStyles_NumberValue_ValueType, gen_SpreadsheetMLStyles_Table_StyledElement, gen_SpreadsheetMLStyles_Row_ColOrRowElement, gen_SpreadsheetMLStyles_TableElement_StyledElement, gen_SpreadsheetMLStyles_ColOrRowElement_TableElement, gen_SpreadsheetMLStyles_Column_ColOrRowElement, gen_SpreadsheetMLStyles_Cell_TableElement, gen_SpreadsheetMLStyles_Header_HeaderOrFooterElt, gen_SpreadsheetMLStyles_Footer_HeaderOrFooterElt},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)