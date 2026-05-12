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

# Classes
SpreadsheetMLPrintingSetup_VersionType = Class(name="SpreadsheetMLPrintingSetup_VersionType")
SpreadsheetMLPrintingSetup_ValueType = Class(name="SpreadsheetMLPrintingSetup_ValueType", is_abstract=True)
SpreadsheetMLPrintingSetup_DateTimeType = Class(name="SpreadsheetMLPrintingSetup_DateTimeType")
SpreadsheetMLPrintingSetup_DateTimeTypeValue = Class(name="SpreadsheetMLPrintingSetup_DateTimeTypeValue")
DateTimeType = Class(name="DateTimeType")
SpreadsheetMLPrintingSetup_BooleanValue = Class(name="SpreadsheetMLPrintingSetup_BooleanValue")
SpreadsheetMLPrintingSetup_ErrorValue = Class(name="SpreadsheetMLPrintingSetup_ErrorValue")
SpreadsheetMLPrintingSetup_DocumentPropertiesCollection = Class(name="SpreadsheetMLPrintingSetup_DocumentPropertiesCollection")
Workbook = Class(name="Workbook")
Data = Class(name="Data")
SpreadsheetMLPrintingSetup_StringValue = Class(name="SpreadsheetMLPrintingSetup_StringValue")
ValueType = Class(name="ValueType")
SpreadsheetMLPrintingSetup_NumberValue = Class(name="SpreadsheetMLPrintingSetup_NumberValue")
VersionType = Class(name="VersionType")
SpreadsheetMLPrintingSetup_CustomDocumentPropertiesCollection = Class(name="SpreadsheetMLPrintingSetup_CustomDocumentPropertiesCollection")
SpreadsheetMLPrintingSetup_CustomDocumentProperty = Class(name="SpreadsheetMLPrintingSetup_CustomDocumentProperty")
CustomDocumentPropertiesCollection = Class(name="CustomDocumentPropertiesCollection")
SpreadsheetMLPrintingSetup_SmartTagType = Class(name="SpreadsheetMLPrintingSetup_SmartTagType")
SmartTagsCollection = Class(name="SmartTagsCollection")
SpreadsheetMLPrintingSetup_SmartTagsCollection = Class(name="SpreadsheetMLPrintingSetup_SmartTagsCollection")
Cell = Class(name="Cell")
SmartTagType = Class(name="SmartTagType")
SpreadsheetMLPrintingSetup_Workbook = Class(name="SpreadsheetMLPrintingSetup_Workbook")
DocumentPropertiesCollection = Class(name="DocumentPropertiesCollection")
CustomDocumentProperty = Class(name="CustomDocumentProperty")
Worksheet = Class(name="Worksheet")
SpreadsheetMLPrintingSetup_Worksheet = Class(name="SpreadsheetMLPrintingSetup_Worksheet")
Table = Class(name="Table")
WorksheetOptionsElt = Class(name="WorksheetOptionsElt")
SpreadsheetMLPrintingSetup_StyledElement = Class(name="SpreadsheetMLPrintingSetup_StyledElement", is_abstract=True)
SpreadsheetMLPrintingSetup_Table = Class(name="SpreadsheetMLPrintingSetup_Table")
StyledElement = Class(name="StyledElement")
Column = Class(name="Column")
Row = Class(name="Row")
ExcelWorkbook = Class(name="ExcelWorkbook")
SpreadsheetMLPrintingSetup_TableElement = Class(name="SpreadsheetMLPrintingSetup_TableElement", is_abstract=True)
SpreadsheetMLPrintingSetup_ColOrRowElement = Class(name="SpreadsheetMLPrintingSetup_ColOrRowElement", is_abstract=True)
TableElement = Class(name="TableElement")
SpreadsheetMLPrintingSetup_Column = Class(name="SpreadsheetMLPrintingSetup_Column")
ColOrRowElement = Class(name="ColOrRowElement")
SpreadsheetMLPrintingSetup_Row = Class(name="SpreadsheetMLPrintingSetup_Row")
SpreadsheetMLPrintingSetup_Cell = Class(name="SpreadsheetMLPrintingSetup_Cell")
Comment = Class(name="Comment")
SpreadsheetMLPrintingSetup_Comment = Class(name="SpreadsheetMLPrintingSetup_Comment")
SpreadsheetMLPrintingSetup_ExcelWorkbook = Class(name="SpreadsheetMLPrintingSetup_ExcelWorkbook")
SpreadsheetMLPrintingSetup_Data = Class(name="SpreadsheetMLPrintingSetup_Data")
SpreadsheetMLPrintingSetup_WorksheetOptionsElt = Class(name="SpreadsheetMLPrintingSetup_WorksheetOptionsElt")
Print = Class(name="Print")
PageSetup = Class(name="PageSetup")
Layout = Class(name="Layout")
Header = Class(name="Header")
Footer = Class(name="Footer")
SpreadsheetMLPrintingSetup_PageSetup = Class(name="SpreadsheetMLPrintingSetup_PageSetup")
PageMarginsInfo = Class(name="PageMarginsInfo")
SpreadsheetMLPrintingSetup_Layout = Class(name="SpreadsheetMLPrintingSetup_Layout")
SpreadsheetMLPrintingSetup_Footer = Class(name="SpreadsheetMLPrintingSetup_Footer")
SpreadsheetMLPrintingSetup_HeaderOrFooterElt = Class(name="SpreadsheetMLPrintingSetup_HeaderOrFooterElt", is_abstract=True)
SpreadsheetMLPrintingSetup_Header = Class(name="SpreadsheetMLPrintingSetup_Header")
HeaderOrFooterElt = Class(name="HeaderOrFooterElt")
SpreadsheetMLPrintingSetup_Print = Class(name="SpreadsheetMLPrintingSetup_Print")
SpreadsheetMLPrintingSetup_PageMarginsInfo = Class(name="SpreadsheetMLPrintingSetup_PageMarginsInfo")

# SpreadsheetMLPrintingSetup_VersionType class attributes and methods
SpreadsheetMLPrintingSetup_VersionType_n: Property = Property(name="n", type=StringType)
SpreadsheetMLPrintingSetup_VersionType_nn: Property = Property(name="nn", type=StringType)
SpreadsheetMLPrintingSetup_VersionType.attributes={SpreadsheetMLPrintingSetup_VersionType_nn, SpreadsheetMLPrintingSetup_VersionType_n}

# SpreadsheetMLPrintingSetup_ValueType class attributes and methods

# SpreadsheetMLPrintingSetup_DateTimeType class attributes and methods
SpreadsheetMLPrintingSetup_DateTimeType_day: Property = Property(name="day", type=StringType)
SpreadsheetMLPrintingSetup_DateTimeType_hour: Property = Property(name="hour", type=StringType)
SpreadsheetMLPrintingSetup_DateTimeType_minute: Property = Property(name="minute", type=StringType)
SpreadsheetMLPrintingSetup_DateTimeType_second: Property = Property(name="second", type=StringType)
SpreadsheetMLPrintingSetup_DateTimeType_year: Property = Property(name="year", type=StringType)
SpreadsheetMLPrintingSetup_DateTimeType_month: Property = Property(name="month", type=StringType)
SpreadsheetMLPrintingSetup_DateTimeType.attributes={SpreadsheetMLPrintingSetup_DateTimeType_year, SpreadsheetMLPrintingSetup_DateTimeType_month, SpreadsheetMLPrintingSetup_DateTimeType_second, SpreadsheetMLPrintingSetup_DateTimeType_day, SpreadsheetMLPrintingSetup_DateTimeType_hour, SpreadsheetMLPrintingSetup_DateTimeType_minute}

# SpreadsheetMLPrintingSetup_DateTimeTypeValue class attributes and methods

# DateTimeType class attributes and methods

# SpreadsheetMLPrintingSetup_BooleanValue class attributes and methods
SpreadsheetMLPrintingSetup_BooleanValue_value: Property = Property(name="value", type=StringType)
SpreadsheetMLPrintingSetup_BooleanValue.attributes={SpreadsheetMLPrintingSetup_BooleanValue_value}

# SpreadsheetMLPrintingSetup_ErrorValue class attributes and methods

# SpreadsheetMLPrintingSetup_DocumentPropertiesCollection class attributes and methods
SpreadsheetMLPrintingSetup_DocumentPropertiesCollection_revision: Property = Property(name="revision", type=StringType)
SpreadsheetMLPrintingSetup_DocumentPropertiesCollection_presentationFormat: Property = Property(name="presentationFormat", type=StringType)
SpreadsheetMLPrintingSetup_DocumentPropertiesCollection_guid: Property = Property(name="guid", type=StringType)
SpreadsheetMLPrintingSetup_DocumentPropertiesCollection_appName: Property = Property(name="appName", type=StringType)
SpreadsheetMLPrintingSetup_DocumentPropertiesCollection_totalTime: Property = Property(name="totalTime", type=StringType)
SpreadsheetMLPrintingSetup_DocumentPropertiesCollection_pages: Property = Property(name="pages", type=StringType)
SpreadsheetMLPrintingSetup_DocumentPropertiesCollection_words: Property = Property(name="words", type=StringType)
SpreadsheetMLPrintingSetup_DocumentPropertiesCollection_characters: Property = Property(name="characters", type=StringType)
SpreadsheetMLPrintingSetup_DocumentPropertiesCollection_charactersWithSpaces: Property = Property(name="charactersWithSpaces", type=StringType)
SpreadsheetMLPrintingSetup_DocumentPropertiesCollection_title: Property = Property(name="title", type=StringType)
SpreadsheetMLPrintingSetup_DocumentPropertiesCollection_bytes: Property = Property(name="bytes", type=StringType)
SpreadsheetMLPrintingSetup_DocumentPropertiesCollection_subject: Property = Property(name="subject", type=StringType)
SpreadsheetMLPrintingSetup_DocumentPropertiesCollection_lines: Property = Property(name="lines", type=StringType)
SpreadsheetMLPrintingSetup_DocumentPropertiesCollection_keywords: Property = Property(name="keywords", type=StringType)
SpreadsheetMLPrintingSetup_DocumentPropertiesCollection_paragraphs: Property = Property(name="paragraphs", type=StringType)
SpreadsheetMLPrintingSetup_DocumentPropertiesCollection_description: Property = Property(name="description", type=StringType)
SpreadsheetMLPrintingSetup_DocumentPropertiesCollection_category: Property = Property(name="category", type=StringType)
SpreadsheetMLPrintingSetup_DocumentPropertiesCollection_author: Property = Property(name="author", type=StringType)
SpreadsheetMLPrintingSetup_DocumentPropertiesCollection_lastAuthor: Property = Property(name="lastAuthor", type=StringType)
SpreadsheetMLPrintingSetup_DocumentPropertiesCollection_manager: Property = Property(name="manager", type=StringType)
SpreadsheetMLPrintingSetup_DocumentPropertiesCollection_company: Property = Property(name="company", type=StringType)
SpreadsheetMLPrintingSetup_DocumentPropertiesCollection_hyperlinkBase: Property = Property(name="hyperlinkBase", type=StringType)
SpreadsheetMLPrintingSetup_DocumentPropertiesCollection.attributes={SpreadsheetMLPrintingSetup_DocumentPropertiesCollection_author, SpreadsheetMLPrintingSetup_DocumentPropertiesCollection_bytes, SpreadsheetMLPrintingSetup_DocumentPropertiesCollection_keywords, SpreadsheetMLPrintingSetup_DocumentPropertiesCollection_charactersWithSpaces, SpreadsheetMLPrintingSetup_DocumentPropertiesCollection_presentationFormat, SpreadsheetMLPrintingSetup_DocumentPropertiesCollection_lastAuthor, SpreadsheetMLPrintingSetup_DocumentPropertiesCollection_paragraphs, SpreadsheetMLPrintingSetup_DocumentPropertiesCollection_hyperlinkBase, SpreadsheetMLPrintingSetup_DocumentPropertiesCollection_guid, SpreadsheetMLPrintingSetup_DocumentPropertiesCollection_description, SpreadsheetMLPrintingSetup_DocumentPropertiesCollection_manager, SpreadsheetMLPrintingSetup_DocumentPropertiesCollection_revision, SpreadsheetMLPrintingSetup_DocumentPropertiesCollection_company, SpreadsheetMLPrintingSetup_DocumentPropertiesCollection_category, SpreadsheetMLPrintingSetup_DocumentPropertiesCollection_totalTime, SpreadsheetMLPrintingSetup_DocumentPropertiesCollection_title, SpreadsheetMLPrintingSetup_DocumentPropertiesCollection_pages, SpreadsheetMLPrintingSetup_DocumentPropertiesCollection_subject, SpreadsheetMLPrintingSetup_DocumentPropertiesCollection_lines, SpreadsheetMLPrintingSetup_DocumentPropertiesCollection_words, SpreadsheetMLPrintingSetup_DocumentPropertiesCollection_appName, SpreadsheetMLPrintingSetup_DocumentPropertiesCollection_characters}

# Workbook class attributes and methods

# Data class attributes and methods

# SpreadsheetMLPrintingSetup_StringValue class attributes and methods
SpreadsheetMLPrintingSetup_StringValue_value: Property = Property(name="value", type=StringType)
SpreadsheetMLPrintingSetup_StringValue.attributes={SpreadsheetMLPrintingSetup_StringValue_value}

# ValueType class attributes and methods

# SpreadsheetMLPrintingSetup_NumberValue class attributes and methods
SpreadsheetMLPrintingSetup_NumberValue_value: Property = Property(name="value", type=StringType)
SpreadsheetMLPrintingSetup_NumberValue.attributes={SpreadsheetMLPrintingSetup_NumberValue_value}

# VersionType class attributes and methods

# SpreadsheetMLPrintingSetup_CustomDocumentPropertiesCollection class attributes and methods

# SpreadsheetMLPrintingSetup_CustomDocumentProperty class attributes and methods
SpreadsheetMLPrintingSetup_CustomDocumentProperty_name: Property = Property(name="name", type=StringType)
SpreadsheetMLPrintingSetup_CustomDocumentProperty.attributes={SpreadsheetMLPrintingSetup_CustomDocumentProperty_name}

# CustomDocumentPropertiesCollection class attributes and methods

# SpreadsheetMLPrintingSetup_SmartTagType class attributes and methods
SpreadsheetMLPrintingSetup_SmartTagType_namespaceuri: Property = Property(name="namespaceuri", type=StringType)
SpreadsheetMLPrintingSetup_SmartTagType_name: Property = Property(name="name", type=StringType)
SpreadsheetMLPrintingSetup_SmartTagType_url: Property = Property(name="url", type=StringType)
SpreadsheetMLPrintingSetup_SmartTagType.attributes={SpreadsheetMLPrintingSetup_SmartTagType_name, SpreadsheetMLPrintingSetup_SmartTagType_url, SpreadsheetMLPrintingSetup_SmartTagType_namespaceuri}

# SmartTagsCollection class attributes and methods

# SpreadsheetMLPrintingSetup_SmartTagsCollection class attributes and methods

# Cell class attributes and methods

# SmartTagType class attributes and methods

# SpreadsheetMLPrintingSetup_Workbook class attributes and methods

# DocumentPropertiesCollection class attributes and methods

# CustomDocumentProperty class attributes and methods

# Worksheet class attributes and methods

# SpreadsheetMLPrintingSetup_Worksheet class attributes and methods
SpreadsheetMLPrintingSetup_Worksheet_name: Property = Property(name="name", type=StringType)
SpreadsheetMLPrintingSetup_Worksheet_protected: Property = Property(name="protected", type=StringType)
SpreadsheetMLPrintingSetup_Worksheet_rightToLeft: Property = Property(name="rightToLeft", type=StringType)
SpreadsheetMLPrintingSetup_Worksheet.attributes={SpreadsheetMLPrintingSetup_Worksheet_rightToLeft, SpreadsheetMLPrintingSetup_Worksheet_name, SpreadsheetMLPrintingSetup_Worksheet_protected}

# Table class attributes and methods

# WorksheetOptionsElt class attributes and methods

# SpreadsheetMLPrintingSetup_StyledElement class attributes and methods

# SpreadsheetMLPrintingSetup_Table class attributes and methods
SpreadsheetMLPrintingSetup_Table_defaultColumnWidth: Property = Property(name="defaultColumnWidth", type=StringType)
SpreadsheetMLPrintingSetup_Table_defaultRowHeight: Property = Property(name="defaultRowHeight", type=StringType)
SpreadsheetMLPrintingSetup_Table_expandedColumnCount: Property = Property(name="expandedColumnCount", type=StringType)
SpreadsheetMLPrintingSetup_Table_expandedRowCount: Property = Property(name="expandedRowCount", type=StringType)
SpreadsheetMLPrintingSetup_Table_leftCell: Property = Property(name="leftCell", type=StringType)
SpreadsheetMLPrintingSetup_Table_topCell: Property = Property(name="topCell", type=StringType)
SpreadsheetMLPrintingSetup_Table_fullColumns: Property = Property(name="fullColumns", type=StringType)
SpreadsheetMLPrintingSetup_Table_fullRows: Property = Property(name="fullRows", type=StringType)
SpreadsheetMLPrintingSetup_Table.attributes={SpreadsheetMLPrintingSetup_Table_expandedRowCount, SpreadsheetMLPrintingSetup_Table_expandedColumnCount, SpreadsheetMLPrintingSetup_Table_topCell, SpreadsheetMLPrintingSetup_Table_defaultColumnWidth, SpreadsheetMLPrintingSetup_Table_fullRows, SpreadsheetMLPrintingSetup_Table_leftCell, SpreadsheetMLPrintingSetup_Table_fullColumns, SpreadsheetMLPrintingSetup_Table_defaultRowHeight}

# StyledElement class attributes and methods

# Column class attributes and methods

# Row class attributes and methods

# ExcelWorkbook class attributes and methods

# SpreadsheetMLPrintingSetup_TableElement class attributes and methods
SpreadsheetMLPrintingSetup_TableElement_index: Property = Property(name="index", type=StringType)
SpreadsheetMLPrintingSetup_TableElement.attributes={SpreadsheetMLPrintingSetup_TableElement_index}

# SpreadsheetMLPrintingSetup_ColOrRowElement class attributes and methods
SpreadsheetMLPrintingSetup_ColOrRowElement_hidden: Property = Property(name="hidden", type=StringType)
SpreadsheetMLPrintingSetup_ColOrRowElement_span: Property = Property(name="span", type=StringType)
SpreadsheetMLPrintingSetup_ColOrRowElement.attributes={SpreadsheetMLPrintingSetup_ColOrRowElement_hidden, SpreadsheetMLPrintingSetup_ColOrRowElement_span}

# TableElement class attributes and methods

# SpreadsheetMLPrintingSetup_Column class attributes and methods
SpreadsheetMLPrintingSetup_Column_autoFitWidth: Property = Property(name="autoFitWidth", type=StringType)
SpreadsheetMLPrintingSetup_Column_width: Property = Property(name="width", type=StringType)
SpreadsheetMLPrintingSetup_Column.attributes={SpreadsheetMLPrintingSetup_Column_width, SpreadsheetMLPrintingSetup_Column_autoFitWidth}

# ColOrRowElement class attributes and methods

# SpreadsheetMLPrintingSetup_Row class attributes and methods
SpreadsheetMLPrintingSetup_Row_autoFitHeight: Property = Property(name="autoFitHeight", type=StringType)
SpreadsheetMLPrintingSetup_Row_height: Property = Property(name="height", type=StringType)
SpreadsheetMLPrintingSetup_Row.attributes={SpreadsheetMLPrintingSetup_Row_height, SpreadsheetMLPrintingSetup_Row_autoFitHeight}

# SpreadsheetMLPrintingSetup_Cell class attributes and methods
SpreadsheetMLPrintingSetup_Cell_arrayRange: Property = Property(name="arrayRange", type=StringType)
SpreadsheetMLPrintingSetup_Cell_formula: Property = Property(name="formula", type=StringType)
SpreadsheetMLPrintingSetup_Cell_hRef: Property = Property(name="hRef", type=StringType)
SpreadsheetMLPrintingSetup_Cell_mergeAcross: Property = Property(name="mergeAcross", type=StringType)
SpreadsheetMLPrintingSetup_Cell_mergeDown: Property = Property(name="mergeDown", type=StringType)
SpreadsheetMLPrintingSetup_Cell.attributes={SpreadsheetMLPrintingSetup_Cell_formula, SpreadsheetMLPrintingSetup_Cell_hRef, SpreadsheetMLPrintingSetup_Cell_mergeAcross, SpreadsheetMLPrintingSetup_Cell_mergeDown, SpreadsheetMLPrintingSetup_Cell_arrayRange}

# Comment class attributes and methods

# SpreadsheetMLPrintingSetup_Comment class attributes and methods
SpreadsheetMLPrintingSetup_Comment_author: Property = Property(name="author", type=StringType)
SpreadsheetMLPrintingSetup_Comment_showAlways: Property = Property(name="showAlways", type=StringType)
SpreadsheetMLPrintingSetup_Comment.attributes={SpreadsheetMLPrintingSetup_Comment_showAlways, SpreadsheetMLPrintingSetup_Comment_author}

# SpreadsheetMLPrintingSetup_ExcelWorkbook class attributes and methods
SpreadsheetMLPrintingSetup_ExcelWorkbook_hideWorkbookTabs: Property = Property(name="hideWorkbookTabs", type=StringType)
SpreadsheetMLPrintingSetup_ExcelWorkbook_windowHeight: Property = Property(name="windowHeight", type=StringType)
SpreadsheetMLPrintingSetup_ExcelWorkbook_windowWidth: Property = Property(name="windowWidth", type=StringType)
SpreadsheetMLPrintingSetup_ExcelWorkbook_windowTopX: Property = Property(name="windowTopX", type=StringType)
SpreadsheetMLPrintingSetup_ExcelWorkbook_windowTopY: Property = Property(name="windowTopY", type=StringType)
SpreadsheetMLPrintingSetup_ExcelWorkbook_activeSheet: Property = Property(name="activeSheet", type=StringType)
SpreadsheetMLPrintingSetup_ExcelWorkbook_activeChart: Property = Property(name="activeChart", type=StringType)
SpreadsheetMLPrintingSetup_ExcelWorkbook_firstVisibleSheet: Property = Property(name="firstVisibleSheet", type=StringType)
SpreadsheetMLPrintingSetup_ExcelWorkbook_selectedSheets: Property = Property(name="selectedSheets", type=StringType)
SpreadsheetMLPrintingSetup_ExcelWorkbook_windowHidden: Property = Property(name="windowHidden", type=StringType)
SpreadsheetMLPrintingSetup_ExcelWorkbook_hideHorizontalScrollBar: Property = Property(name="hideHorizontalScrollBar", type=StringType)
SpreadsheetMLPrintingSetup_ExcelWorkbook_hideVerticalScrollBar: Property = Property(name="hideVerticalScrollBar", type=StringType)
SpreadsheetMLPrintingSetup_ExcelWorkbook_futureVer: Property = Property(name="futureVer", type=StringType)
SpreadsheetMLPrintingSetup_ExcelWorkbook_maxChange: Property = Property(name="maxChange", type=StringType)
SpreadsheetMLPrintingSetup_ExcelWorkbook_tabRatio: Property = Property(name="tabRatio", type=StringType)
SpreadsheetMLPrintingSetup_ExcelWorkbook_windowIconic: Property = Property(name="windowIconic", type=StringType)
SpreadsheetMLPrintingSetup_ExcelWorkbook_displayDrawingObjects: Property = Property(name="displayDrawingObjects", type=StringType)
SpreadsheetMLPrintingSetup_ExcelWorkbook_createBackup: Property = Property(name="createBackup", type=StringType)
SpreadsheetMLPrintingSetup_ExcelWorkbook_calculation: Property = Property(name="calculation", type=StringType)
SpreadsheetMLPrintingSetup_ExcelWorkbook_doNotCalculateBeforeSave: Property = Property(name="doNotCalculateBeforeSave", type=StringType)
SpreadsheetMLPrintingSetup_ExcelWorkbook_hidePivotTableFieldList: Property = Property(name="hidePivotTableFieldList", type=StringType)
SpreadsheetMLPrintingSetup_ExcelWorkbook_date1904: Property = Property(name="date1904", type=StringType)
SpreadsheetMLPrintingSetup_ExcelWorkbook_protectStructure: Property = Property(name="protectStructure", type=StringType)
SpreadsheetMLPrintingSetup_ExcelWorkbook_refModeR1C1: Property = Property(name="refModeR1C1", type=StringType)
SpreadsheetMLPrintingSetup_ExcelWorkbook_protectWindows: Property = Property(name="protectWindows", type=StringType)
SpreadsheetMLPrintingSetup_ExcelWorkbook_iteration: Property = Property(name="iteration", type=StringType)
SpreadsheetMLPrintingSetup_ExcelWorkbook_displayInkNotes: Property = Property(name="displayInkNotes", type=StringType)
SpreadsheetMLPrintingSetup_ExcelWorkbook_embedSaveSmartTags: Property = Property(name="embedSaveSmartTags", type=StringType)
SpreadsheetMLPrintingSetup_ExcelWorkbook_maxIterations: Property = Property(name="maxIterations", type=StringType)
SpreadsheetMLPrintingSetup_ExcelWorkbook_precisionAsDisplayed: Property = Property(name="precisionAsDisplayed", type=StringType)
SpreadsheetMLPrintingSetup_ExcelWorkbook_doNotSaveLinkValues: Property = Property(name="doNotSaveLinkValues", type=StringType)
SpreadsheetMLPrintingSetup_ExcelWorkbook_noAutoRecover: Property = Property(name="noAutoRecover", type=StringType)
SpreadsheetMLPrintingSetup_ExcelWorkbook_acceptLabelsInFormulas: Property = Property(name="acceptLabelsInFormulas", type=StringType)
SpreadsheetMLPrintingSetup_ExcelWorkbook_uncalced: Property = Property(name="uncalced", type=StringType)
SpreadsheetMLPrintingSetup_ExcelWorkbook.attributes={SpreadsheetMLPrintingSetup_ExcelWorkbook_activeSheet, SpreadsheetMLPrintingSetup_ExcelWorkbook_windowHeight, SpreadsheetMLPrintingSetup_ExcelWorkbook_activeChart, SpreadsheetMLPrintingSetup_ExcelWorkbook_displayDrawingObjects, SpreadsheetMLPrintingSetup_ExcelWorkbook_maxIterations, SpreadsheetMLPrintingSetup_ExcelWorkbook_hideHorizontalScrollBar, SpreadsheetMLPrintingSetup_ExcelWorkbook_protectWindows, SpreadsheetMLPrintingSetup_ExcelWorkbook_windowTopX, SpreadsheetMLPrintingSetup_ExcelWorkbook_hidePivotTableFieldList, SpreadsheetMLPrintingSetup_ExcelWorkbook_createBackup, SpreadsheetMLPrintingSetup_ExcelWorkbook_iteration, SpreadsheetMLPrintingSetup_ExcelWorkbook_protectStructure, SpreadsheetMLPrintingSetup_ExcelWorkbook_firstVisibleSheet, SpreadsheetMLPrintingSetup_ExcelWorkbook_date1904, SpreadsheetMLPrintingSetup_ExcelWorkbook_embedSaveSmartTags, SpreadsheetMLPrintingSetup_ExcelWorkbook_noAutoRecover, SpreadsheetMLPrintingSetup_ExcelWorkbook_acceptLabelsInFormulas, SpreadsheetMLPrintingSetup_ExcelWorkbook_uncalced, SpreadsheetMLPrintingSetup_ExcelWorkbook_precisionAsDisplayed, SpreadsheetMLPrintingSetup_ExcelWorkbook_maxChange, SpreadsheetMLPrintingSetup_ExcelWorkbook_windowHidden, SpreadsheetMLPrintingSetup_ExcelWorkbook_doNotSaveLinkValues, SpreadsheetMLPrintingSetup_ExcelWorkbook_refModeR1C1, SpreadsheetMLPrintingSetup_ExcelWorkbook_windowIconic, SpreadsheetMLPrintingSetup_ExcelWorkbook_calculation, SpreadsheetMLPrintingSetup_ExcelWorkbook_displayInkNotes, SpreadsheetMLPrintingSetup_ExcelWorkbook_futureVer, SpreadsheetMLPrintingSetup_ExcelWorkbook_tabRatio, SpreadsheetMLPrintingSetup_ExcelWorkbook_windowWidth, SpreadsheetMLPrintingSetup_ExcelWorkbook_hideVerticalScrollBar, SpreadsheetMLPrintingSetup_ExcelWorkbook_doNotCalculateBeforeSave, SpreadsheetMLPrintingSetup_ExcelWorkbook_windowTopY, SpreadsheetMLPrintingSetup_ExcelWorkbook_selectedSheets, SpreadsheetMLPrintingSetup_ExcelWorkbook_hideWorkbookTabs}

# SpreadsheetMLPrintingSetup_Data class attributes and methods

# SpreadsheetMLPrintingSetup_WorksheetOptionsElt class attributes and methods
SpreadsheetMLPrintingSetup_WorksheetOptionsElt_name: Property = Property(name="name", type=StringType)
SpreadsheetMLPrintingSetup_WorksheetOptionsElt_excelWorksheetType: Property = Property(name="excelWorksheetType", type=StringType)
SpreadsheetMLPrintingSetup_WorksheetOptionsElt_intlMacro: Property = Property(name="intlMacro", type=StringType)
SpreadsheetMLPrintingSetup_WorksheetOptionsElt_unsynced: Property = Property(name="unsynced", type=StringType)
SpreadsheetMLPrintingSetup_WorksheetOptionsElt_fitToPage: Property = Property(name="fitToPage", type=StringType)
SpreadsheetMLPrintingSetup_WorksheetOptionsElt_doNotDisplayColHeaders: Property = Property(name="doNotDisplayColHeaders", type=StringType)
SpreadsheetMLPrintingSetup_WorksheetOptionsElt_doNotDisplayRowHeaders: Property = Property(name="doNotDisplayRowHeaders", type=StringType)
SpreadsheetMLPrintingSetup_WorksheetOptionsElt_gridlineColor: Property = Property(name="gridlineColor", type=StringType)
SpreadsheetMLPrintingSetup_WorksheetOptionsElt_defaultRowHeight: Property = Property(name="defaultRowHeight", type=StringType)
SpreadsheetMLPrintingSetup_WorksheetOptionsElt_defaultColumnWidth: Property = Property(name="defaultColumnWidth", type=StringType)
SpreadsheetMLPrintingSetup_WorksheetOptionsElt_standardWidth: Property = Property(name="standardWidth", type=StringType)
SpreadsheetMLPrintingSetup_WorksheetOptionsElt_visible: Property = Property(name="visible", type=StringType)
SpreadsheetMLPrintingSetup_WorksheetOptionsElt_leftColumnVisible: Property = Property(name="leftColumnVisible", type=StringType)
SpreadsheetMLPrintingSetup_WorksheetOptionsElt_displayRightToLeft: Property = Property(name="displayRightToLeft", type=StringType)
SpreadsheetMLPrintingSetup_WorksheetOptionsElt_gridlineColorIndex: Property = Property(name="gridlineColorIndex", type=StringType)
SpreadsheetMLPrintingSetup_WorksheetOptionsElt_displayFormulas: Property = Property(name="displayFormulas", type=StringType)
SpreadsheetMLPrintingSetup_WorksheetOptionsElt_doNotDisplayGridlines: Property = Property(name="doNotDisplayGridlines", type=StringType)
SpreadsheetMLPrintingSetup_WorksheetOptionsElt_doNotDisplayHeadings: Property = Property(name="doNotDisplayHeadings", type=StringType)
SpreadsheetMLPrintingSetup_WorksheetOptionsElt_doNotDisplayOutline: Property = Property(name="doNotDisplayOutline", type=StringType)
SpreadsheetMLPrintingSetup_WorksheetOptionsElt_selected: Property = Property(name="selected", type=StringType)
SpreadsheetMLPrintingSetup_WorksheetOptionsElt_codeName: Property = Property(name="codeName", type=StringType)
SpreadsheetMLPrintingSetup_WorksheetOptionsElt_displayPageBreak: Property = Property(name="displayPageBreak", type=StringType)
SpreadsheetMLPrintingSetup_WorksheetOptionsElt_transitionExpressionEvaluation: Property = Property(name="transitionExpressionEvaluation", type=StringType)
SpreadsheetMLPrintingSetup_WorksheetOptionsElt_transitionFormulaEntry: Property = Property(name="transitionFormulaEntry", type=StringType)
SpreadsheetMLPrintingSetup_WorksheetOptionsElt_zoom: Property = Property(name="zoom", type=StringType)
SpreadsheetMLPrintingSetup_WorksheetOptionsElt_pageBreakZoom: Property = Property(name="pageBreakZoom", type=StringType)
SpreadsheetMLPrintingSetup_WorksheetOptionsElt_showPageBreakZoom: Property = Property(name="showPageBreakZoom", type=StringType)
SpreadsheetMLPrintingSetup_WorksheetOptionsElt_topRowVisible: Property = Property(name="topRowVisible", type=StringType)
SpreadsheetMLPrintingSetup_WorksheetOptionsElt_topRowBottomPane: Property = Property(name="topRowBottomPane", type=StringType)
SpreadsheetMLPrintingSetup_WorksheetOptionsElt_leftColumnRightPane: Property = Property(name="leftColumnRightPane", type=StringType)
SpreadsheetMLPrintingSetup_WorksheetOptionsElt_activePane: Property = Property(name="activePane", type=StringType)
SpreadsheetMLPrintingSetup_WorksheetOptionsElt_splitHorizontal: Property = Property(name="splitHorizontal", type=StringType)
SpreadsheetMLPrintingSetup_WorksheetOptionsElt_splitVertical: Property = Property(name="splitVertical", type=StringType)
SpreadsheetMLPrintingSetup_WorksheetOptionsElt_freezePanes: Property = Property(name="freezePanes", type=StringType)
SpreadsheetMLPrintingSetup_WorksheetOptionsElt_applyAutomaticOutlineStyles: Property = Property(name="applyAutomaticOutlineStyles", type=StringType)
SpreadsheetMLPrintingSetup_WorksheetOptionsElt_noSummaryRowsBelowDetail: Property = Property(name="noSummaryRowsBelowDetail", type=StringType)
SpreadsheetMLPrintingSetup_WorksheetOptionsElt_noSummaryColumnsRightDetail: Property = Property(name="noSummaryColumnsRightDetail", type=StringType)
SpreadsheetMLPrintingSetup_WorksheetOptionsElt_doNotDisplayZeros: Property = Property(name="doNotDisplayZeros", type=StringType)
SpreadsheetMLPrintingSetup_WorksheetOptionsElt_activeRow: Property = Property(name="activeRow", type=StringType)
SpreadsheetMLPrintingSetup_WorksheetOptionsElt_activeColumn: Property = Property(name="activeColumn", type=StringType)
SpreadsheetMLPrintingSetup_WorksheetOptionsElt_filterOn: Property = Property(name="filterOn", type=StringType)
SpreadsheetMLPrintingSetup_WorksheetOptionsElt_rangeSelection: Property = Property(name="rangeSelection", type=StringType)
SpreadsheetMLPrintingSetup_WorksheetOptionsElt_allowSizeCols: Property = Property(name="allowSizeCols", type=StringType)
SpreadsheetMLPrintingSetup_WorksheetOptionsElt_allowSizeRows: Property = Property(name="allowSizeRows", type=StringType)
SpreadsheetMLPrintingSetup_WorksheetOptionsElt_allowInsertCols: Property = Property(name="allowInsertCols", type=StringType)
SpreadsheetMLPrintingSetup_WorksheetOptionsElt_allowInsertRows: Property = Property(name="allowInsertRows", type=StringType)
SpreadsheetMLPrintingSetup_WorksheetOptionsElt_allowInsertHyperlinks: Property = Property(name="allowInsertHyperlinks", type=StringType)
SpreadsheetMLPrintingSetup_WorksheetOptionsElt_frozenNoSplit: Property = Property(name="frozenNoSplit", type=StringType)
SpreadsheetMLPrintingSetup_WorksheetOptionsElt_tabColorIndex: Property = Property(name="tabColorIndex", type=StringType)
SpreadsheetMLPrintingSetup_WorksheetOptionsElt_protectContentst: Property = Property(name="protectContentst", type=StringType)
SpreadsheetMLPrintingSetup_WorksheetOptionsElt_protectObjects: Property = Property(name="protectObjects", type=StringType)
SpreadsheetMLPrintingSetup_WorksheetOptionsElt_protectScenarios: Property = Property(name="protectScenarios", type=StringType)
SpreadsheetMLPrintingSetup_WorksheetOptionsElt_enableSelection: Property = Property(name="enableSelection", type=StringType)
SpreadsheetMLPrintingSetup_WorksheetOptionsElt_allowFormatCells: Property = Property(name="allowFormatCells", type=StringType)
SpreadsheetMLPrintingSetup_WorksheetOptionsElt_allowDeleteCols: Property = Property(name="allowDeleteCols", type=StringType)
SpreadsheetMLPrintingSetup_WorksheetOptionsElt_allowDeleteRows: Property = Property(name="allowDeleteRows", type=StringType)
SpreadsheetMLPrintingSetup_WorksheetOptionsElt_allowSort: Property = Property(name="allowSort", type=StringType)
SpreadsheetMLPrintingSetup_WorksheetOptionsElt_allowFilter: Property = Property(name="allowFilter", type=StringType)
SpreadsheetMLPrintingSetup_WorksheetOptionsElt_allowUsePivotTables: Property = Property(name="allowUsePivotTables", type=StringType)
SpreadsheetMLPrintingSetup_WorksheetOptionsElt.attributes={SpreadsheetMLPrintingSetup_WorksheetOptionsElt_allowSizeRows, SpreadsheetMLPrintingSetup_WorksheetOptionsElt_splitVertical, SpreadsheetMLPrintingSetup_WorksheetOptionsElt_allowFilter, SpreadsheetMLPrintingSetup_WorksheetOptionsElt_allowSizeCols, SpreadsheetMLPrintingSetup_WorksheetOptionsElt_excelWorksheetType, SpreadsheetMLPrintingSetup_WorksheetOptionsElt_name, SpreadsheetMLPrintingSetup_WorksheetOptionsElt_tabColorIndex, SpreadsheetMLPrintingSetup_WorksheetOptionsElt_allowFormatCells, SpreadsheetMLPrintingSetup_WorksheetOptionsElt_defaultColumnWidth, SpreadsheetMLPrintingSetup_WorksheetOptionsElt_topRowVisible, SpreadsheetMLPrintingSetup_WorksheetOptionsElt_topRowBottomPane, SpreadsheetMLPrintingSetup_WorksheetOptionsElt_allowInsertRows, SpreadsheetMLPrintingSetup_WorksheetOptionsElt_doNotDisplayOutline, SpreadsheetMLPrintingSetup_WorksheetOptionsElt_standardWidth, SpreadsheetMLPrintingSetup_WorksheetOptionsElt_rangeSelection, SpreadsheetMLPrintingSetup_WorksheetOptionsElt_allowInsertHyperlinks, SpreadsheetMLPrintingSetup_WorksheetOptionsElt_activeRow, SpreadsheetMLPrintingSetup_WorksheetOptionsElt_frozenNoSplit, SpreadsheetMLPrintingSetup_WorksheetOptionsElt_displayPageBreak, SpreadsheetMLPrintingSetup_WorksheetOptionsElt_intlMacro, SpreadsheetMLPrintingSetup_WorksheetOptionsElt_allowDeleteCols, SpreadsheetMLPrintingSetup_WorksheetOptionsElt_doNotDisplayZeros, SpreadsheetMLPrintingSetup_WorksheetOptionsElt_noSummaryRowsBelowDetail, SpreadsheetMLPrintingSetup_WorksheetOptionsElt_protectScenarios, SpreadsheetMLPrintingSetup_WorksheetOptionsElt_allowSort, SpreadsheetMLPrintingSetup_WorksheetOptionsElt_gridlineColor, SpreadsheetMLPrintingSetup_WorksheetOptionsElt_displayFormulas, SpreadsheetMLPrintingSetup_WorksheetOptionsElt_allowInsertCols, SpreadsheetMLPrintingSetup_WorksheetOptionsElt_transitionExpressionEvaluation, SpreadsheetMLPrintingSetup_WorksheetOptionsElt_enableSelection, SpreadsheetMLPrintingSetup_WorksheetOptionsElt_splitHorizontal, SpreadsheetMLPrintingSetup_WorksheetOptionsElt_showPageBreakZoom, SpreadsheetMLPrintingSetup_WorksheetOptionsElt_leftColumnVisible, SpreadsheetMLPrintingSetup_WorksheetOptionsElt_doNotDisplayGridlines, SpreadsheetMLPrintingSetup_WorksheetOptionsElt_unsynced, SpreadsheetMLPrintingSetup_WorksheetOptionsElt_protectContentst, SpreadsheetMLPrintingSetup_WorksheetOptionsElt_gridlineColorIndex, SpreadsheetMLPrintingSetup_WorksheetOptionsElt_doNotDisplayRowHeaders, SpreadsheetMLPrintingSetup_WorksheetOptionsElt_allowUsePivotTables, SpreadsheetMLPrintingSetup_WorksheetOptionsElt_filterOn, SpreadsheetMLPrintingSetup_WorksheetOptionsElt_selected, SpreadsheetMLPrintingSetup_WorksheetOptionsElt_displayRightToLeft, SpreadsheetMLPrintingSetup_WorksheetOptionsElt_leftColumnRightPane, SpreadsheetMLPrintingSetup_WorksheetOptionsElt_doNotDisplayColHeaders, SpreadsheetMLPrintingSetup_WorksheetOptionsElt_activePane, SpreadsheetMLPrintingSetup_WorksheetOptionsElt_freezePanes, SpreadsheetMLPrintingSetup_WorksheetOptionsElt_visible, SpreadsheetMLPrintingSetup_WorksheetOptionsElt_zoom, SpreadsheetMLPrintingSetup_WorksheetOptionsElt_fitToPage, SpreadsheetMLPrintingSetup_WorksheetOptionsElt_defaultRowHeight, SpreadsheetMLPrintingSetup_WorksheetOptionsElt_applyAutomaticOutlineStyles, SpreadsheetMLPrintingSetup_WorksheetOptionsElt_protectObjects, SpreadsheetMLPrintingSetup_WorksheetOptionsElt_doNotDisplayHeadings, SpreadsheetMLPrintingSetup_WorksheetOptionsElt_activeColumn, SpreadsheetMLPrintingSetup_WorksheetOptionsElt_allowDeleteRows, SpreadsheetMLPrintingSetup_WorksheetOptionsElt_codeName, SpreadsheetMLPrintingSetup_WorksheetOptionsElt_pageBreakZoom, SpreadsheetMLPrintingSetup_WorksheetOptionsElt_noSummaryColumnsRightDetail, SpreadsheetMLPrintingSetup_WorksheetOptionsElt_transitionFormulaEntry}

# Print class attributes and methods

# PageSetup class attributes and methods

# Layout class attributes and methods

# Header class attributes and methods

# Footer class attributes and methods

# SpreadsheetMLPrintingSetup_PageSetup class attributes and methods

# PageMarginsInfo class attributes and methods

# SpreadsheetMLPrintingSetup_Layout class attributes and methods
SpreadsheetMLPrintingSetup_Layout_centerVertical: Property = Property(name="centerVertical", type=StringType)
SpreadsheetMLPrintingSetup_Layout_startPageNumber: Property = Property(name="startPageNumber", type=StringType)
SpreadsheetMLPrintingSetup_Layout_orientation: Property = Property(name="orientation", type=StringType)
SpreadsheetMLPrintingSetup_Layout_centerHorizontal: Property = Property(name="centerHorizontal", type=StringType)
SpreadsheetMLPrintingSetup_Layout.attributes={SpreadsheetMLPrintingSetup_Layout_centerHorizontal, SpreadsheetMLPrintingSetup_Layout_centerVertical, SpreadsheetMLPrintingSetup_Layout_startPageNumber, SpreadsheetMLPrintingSetup_Layout_orientation}

# SpreadsheetMLPrintingSetup_Footer class attributes and methods

# SpreadsheetMLPrintingSetup_HeaderOrFooterElt class attributes and methods
SpreadsheetMLPrintingSetup_HeaderOrFooterElt_margin: Property = Property(name="margin", type=StringType)
SpreadsheetMLPrintingSetup_HeaderOrFooterElt_data: Property = Property(name="data", type=StringType)
SpreadsheetMLPrintingSetup_HeaderOrFooterElt.attributes={SpreadsheetMLPrintingSetup_HeaderOrFooterElt_margin, SpreadsheetMLPrintingSetup_HeaderOrFooterElt_data}

# SpreadsheetMLPrintingSetup_Header class attributes and methods

# HeaderOrFooterElt class attributes and methods

# SpreadsheetMLPrintingSetup_Print class attributes and methods
SpreadsheetMLPrintingSetup_Print_commentsLayout: Property = Property(name="commentsLayout", type=StringType)
SpreadsheetMLPrintingSetup_Print_scale: Property = Property(name="scale", type=StringType)
SpreadsheetMLPrintingSetup_Print_printErrors: Property = Property(name="printErrors", type=StringType)
SpreadsheetMLPrintingSetup_Print_validPrinterInfo: Property = Property(name="validPrinterInfo", type=StringType)
SpreadsheetMLPrintingSetup_Print_paperSizeIndex: Property = Property(name="paperSizeIndex", type=StringType)
SpreadsheetMLPrintingSetup_Print_horizontalResolution: Property = Property(name="horizontalResolution", type=StringType)
SpreadsheetMLPrintingSetup_Print_fitWidth: Property = Property(name="fitWidth", type=StringType)
SpreadsheetMLPrintingSetup_Print_fitHeight: Property = Property(name="fitHeight", type=StringType)
SpreadsheetMLPrintingSetup_Print_leftToRight: Property = Property(name="leftToRight", type=StringType)
SpreadsheetMLPrintingSetup_Print_blackAndWhite: Property = Property(name="blackAndWhite", type=StringType)
SpreadsheetMLPrintingSetup_Print_draftQuality: Property = Property(name="draftQuality", type=StringType)
SpreadsheetMLPrintingSetup_Print_verticalResolution: Property = Property(name="verticalResolution", type=StringType)
SpreadsheetMLPrintingSetup_Print_gridlines: Property = Property(name="gridlines", type=StringType)
SpreadsheetMLPrintingSetup_Print_numberOfCopies: Property = Property(name="numberOfCopies", type=StringType)
SpreadsheetMLPrintingSetup_Print_rowColHeadings: Property = Property(name="rowColHeadings", type=StringType)
SpreadsheetMLPrintingSetup_Print.attributes={SpreadsheetMLPrintingSetup_Print_paperSizeIndex, SpreadsheetMLPrintingSetup_Print_numberOfCopies, SpreadsheetMLPrintingSetup_Print_validPrinterInfo, SpreadsheetMLPrintingSetup_Print_rowColHeadings, SpreadsheetMLPrintingSetup_Print_draftQuality, SpreadsheetMLPrintingSetup_Print_leftToRight, SpreadsheetMLPrintingSetup_Print_verticalResolution, SpreadsheetMLPrintingSetup_Print_fitWidth, SpreadsheetMLPrintingSetup_Print_gridlines, SpreadsheetMLPrintingSetup_Print_horizontalResolution, SpreadsheetMLPrintingSetup_Print_printErrors, SpreadsheetMLPrintingSetup_Print_commentsLayout, SpreadsheetMLPrintingSetup_Print_blackAndWhite, SpreadsheetMLPrintingSetup_Print_scale, SpreadsheetMLPrintingSetup_Print_fitHeight}

# SpreadsheetMLPrintingSetup_PageMarginsInfo class attributes and methods
SpreadsheetMLPrintingSetup_PageMarginsInfo_left: Property = Property(name="left", type=StringType)
SpreadsheetMLPrintingSetup_PageMarginsInfo_right: Property = Property(name="right", type=StringType)
SpreadsheetMLPrintingSetup_PageMarginsInfo_top: Property = Property(name="top", type=StringType)
SpreadsheetMLPrintingSetup_PageMarginsInfo_bottom: Property = Property(name="bottom", type=StringType)
SpreadsheetMLPrintingSetup_PageMarginsInfo.attributes={SpreadsheetMLPrintingSetup_PageMarginsInfo_bottom, SpreadsheetMLPrintingSetup_PageMarginsInfo_left, SpreadsheetMLPrintingSetup_PageMarginsInfo_right, SpreadsheetMLPrintingSetup_PageMarginsInfo_top}

# Relationships
value1: BinaryAssociation = BinaryAssociation(
    name="value1",
    ends={
        Property(name="DateTimeType", type=SpreadsheetMLPrintingSetup_DateTimeTypeValue, multiplicity=Multiplicity(1, 1)),
        Property(name="SpreadsheetMLPrintingSetup_DateTimeTypeValue", type=DateTimeType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
vt_data0: BinaryAssociation = BinaryAssociation(
    name="vt_data0",
    ends={
        Property(name="Data", type=SpreadsheetMLPrintingSetup_ValueType, multiplicity=Multiplicity(1, 1)),
        Property(name="value", type=Data, multiplicity=Multiplicity(1, 1))
    }
)
version3: BinaryAssociation = BinaryAssociation(
    name="version3",
    ends={
        Property(name="VersionType", type=SpreadsheetMLPrintingSetup_DocumentPropertiesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="SpreadsheetMLPrintingSetup_DocumentPropertiesCollection", type=VersionType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lastPrinted4: BinaryAssociation = BinaryAssociation(
    name="lastPrinted4",
    ends={
        Property(name="DateTimeType6", type=SpreadsheetMLPrintingSetup_DocumentPropertiesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="SpreadsheetMLPrintingSetup_DocumentPropertiesCollection5", type=DateTimeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
created7: BinaryAssociation = BinaryAssociation(
    name="created7",
    ends={
        Property(name="DateTimeType9", type=SpreadsheetMLPrintingSetup_DocumentPropertiesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="SpreadsheetMLPrintingSetup_DocumentPropertiesCollection8", type=DateTimeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lastSaved10: BinaryAssociation = BinaryAssociation(
    name="lastSaved10",
    ends={
        Property(name="DateTimeType12", type=SpreadsheetMLPrintingSetup_DocumentPropertiesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="SpreadsheetMLPrintingSetup_DocumentPropertiesCollection11", type=DateTimeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dp_workbook2: BinaryAssociation = BinaryAssociation(
    name="dp_workbook2",
    ends={
        Property(name="Workbook", type=SpreadsheetMLPrintingSetup_DocumentPropertiesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="wb_docProperties", type=Workbook, multiplicity=Multiplicity(1, 1))
    }
)
cdp_workbook13: BinaryAssociation = BinaryAssociation(
    name="cdp_workbook13",
    ends={
        Property(name="Workbook14", type=SpreadsheetMLPrintingSetup_CustomDocumentPropertiesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="wb_customDocProperties", type=Workbook, multiplicity=Multiplicity(1, 1))
    }
)
customDocumentProperty_cdpe16: BinaryAssociation = BinaryAssociation(
    name="customDocumentProperty_cdpe16",
    ends={
        Property(name="CustomDocumentPropertiesCollection", type=SpreadsheetMLPrintingSetup_CustomDocumentProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="customDocumentProperties", type=CustomDocumentPropertiesCollection, multiplicity=Multiplicity(1, 1))
    }
)
value17: BinaryAssociation = BinaryAssociation(
    name="value17",
    ends={
        Property(name="ValueType", type=SpreadsheetMLPrintingSetup_CustomDocumentProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="SpreadsheetMLPrintingSetup_CustomDocumentProperty", type=ValueType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
smartTagType_ste18: BinaryAssociation = BinaryAssociation(
    name="smartTagType_ste18",
    ends={
        Property(name="SmartTagsCollection", type=SpreadsheetMLPrintingSetup_SmartTagType, multiplicity=Multiplicity(1, 1)),
        Property(name="smartTagTypes", type=SmartTagsCollection, multiplicity=Multiplicity(1, 1))
    }
)
st_workbook19: BinaryAssociation = BinaryAssociation(
    name="st_workbook19",
    ends={
        Property(name="Workbook20", type=SpreadsheetMLPrintingSetup_SmartTagsCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="wb_smartTags", type=Workbook, multiplicity=Multiplicity(1, 1))
    }
)
st_cell21: BinaryAssociation = BinaryAssociation(
    name="st_cell21",
    ends={
        Property(name="Cell", type=SpreadsheetMLPrintingSetup_SmartTagsCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="c_smartTags", type=Cell, multiplicity=Multiplicity(1, 1))
    }
)
smartTagTypes22: BinaryAssociation = BinaryAssociation(
    name="smartTagTypes22",
    ends={
        Property(name="SmartTagType", type=SpreadsheetMLPrintingSetup_SmartTagsCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="smartTagType_ste", type=SmartTagType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
wb_smartTags23: BinaryAssociation = BinaryAssociation(
    name="wb_smartTags23",
    ends={
        Property(name="SmartTagsCollection24", type=SpreadsheetMLPrintingSetup_Workbook, multiplicity=Multiplicity(1, 1)),
        Property(name="st_workbook", type=SmartTagsCollection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
wb_docProperties25: BinaryAssociation = BinaryAssociation(
    name="wb_docProperties25",
    ends={
        Property(name="DocumentPropertiesCollection", type=SpreadsheetMLPrintingSetup_Workbook, multiplicity=Multiplicity(1, 1)),
        Property(name="dp_workbook", type=DocumentPropertiesCollection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
wb_customDocProperties26: BinaryAssociation = BinaryAssociation(
    name="wb_customDocProperties26",
    ends={
        Property(name="CustomDocumentPropertiesCollection27", type=SpreadsheetMLPrintingSetup_Workbook, multiplicity=Multiplicity(1, 1)),
        Property(name="cdp_workbook", type=CustomDocumentPropertiesCollection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
customDocumentProperties15: BinaryAssociation = BinaryAssociation(
    name="customDocumentProperties15",
    ends={
        Property(name="CustomDocumentProperty", type=SpreadsheetMLPrintingSetup_CustomDocumentPropertiesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="customDocumentProperty_cdpe", type=CustomDocumentProperty, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
wb_excelWorkbook28: BinaryAssociation = BinaryAssociation(
    name="wb_excelWorkbook28",
    ends={
        Property(name="ew_workbook", type=ExcelWorkbook, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="ExcelWorkbook", type=SpreadsheetMLPrintingSetup_Workbook, multiplicity=Multiplicity(1, 1))
    }
)
wb_worksheets29: BinaryAssociation = BinaryAssociation(
    name="wb_worksheets29",
    ends={
        Property(name="Worksheet", type=SpreadsheetMLPrintingSetup_Workbook, multiplicity=Multiplicity(1, 1)),
        Property(name="ws_workbook", type=Worksheet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ws_workbook30: BinaryAssociation = BinaryAssociation(
    name="ws_workbook30",
    ends={
        Property(name="Workbook31", type=SpreadsheetMLPrintingSetup_Worksheet, multiplicity=Multiplicity(1, 1)),
        Property(name="wb_worksheets", type=Workbook, multiplicity=Multiplicity(1, 1))
    }
)
ws_table32: BinaryAssociation = BinaryAssociation(
    name="ws_table32",
    ends={
        Property(name="Table", type=SpreadsheetMLPrintingSetup_Worksheet, multiplicity=Multiplicity(1, 1)),
        Property(name="t_worksheet", type=Table, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
w_worksheetOptions33: BinaryAssociation = BinaryAssociation(
    name="w_worksheetOptions33",
    ends={
        Property(name="WorksheetOptionsElt", type=SpreadsheetMLPrintingSetup_Worksheet, multiplicity=Multiplicity(1, 1)),
        Property(name="wo_worksheet", type=WorksheetOptionsElt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
t_worksheet34: BinaryAssociation = BinaryAssociation(
    name="t_worksheet34",
    ends={
        Property(name="Worksheet35", type=SpreadsheetMLPrintingSetup_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="ws_table", type=Worksheet, multiplicity=Multiplicity(1, 1))
    }
)
t_cols36: BinaryAssociation = BinaryAssociation(
    name="t_cols36",
    ends={
        Property(name="Column", type=SpreadsheetMLPrintingSetup_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="c_table", type=Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
t_rows37: BinaryAssociation = BinaryAssociation(
    name="t_rows37",
    ends={
        Property(name="Row", type=SpreadsheetMLPrintingSetup_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="r_table", type=Row, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
c_table38: BinaryAssociation = BinaryAssociation(
    name="c_table38",
    ends={
        Property(name="Table39", type=SpreadsheetMLPrintingSetup_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="t_cols", type=Table, multiplicity=Multiplicity(1, 1))
    }
)
r_table40: BinaryAssociation = BinaryAssociation(
    name="r_table40",
    ends={
        Property(name="Table41", type=SpreadsheetMLPrintingSetup_Row, multiplicity=Multiplicity(1, 1)),
        Property(name="t_rows", type=Table, multiplicity=Multiplicity(1, 1))
    }
)
r_cells42: BinaryAssociation = BinaryAssociation(
    name="r_cells42",
    ends={
        Property(name="Cell43", type=SpreadsheetMLPrintingSetup_Row, multiplicity=Multiplicity(1, 1)),
        Property(name="c_row", type=Cell, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
c_smartTags44: BinaryAssociation = BinaryAssociation(
    name="c_smartTags44",
    ends={
        Property(name="SmartTagsCollection45", type=SpreadsheetMLPrintingSetup_Cell, multiplicity=Multiplicity(1, 1)),
        Property(name="st_cell", type=SmartTagsCollection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
c_row46: BinaryAssociation = BinaryAssociation(
    name="c_row46",
    ends={
        Property(name="Row47", type=SpreadsheetMLPrintingSetup_Cell, multiplicity=Multiplicity(1, 1)),
        Property(name="r_cells", type=Row, multiplicity=Multiplicity(1, 1))
    }
)
c_data48: BinaryAssociation = BinaryAssociation(
    name="c_data48",
    ends={
        Property(name="Data49", type=SpreadsheetMLPrintingSetup_Cell, multiplicity=Multiplicity(1, 1)),
        Property(name="d_cell", type=Data, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
c_comment50: BinaryAssociation = BinaryAssociation(
    name="c_comment50",
    ends={
        Property(name="Comment", type=SpreadsheetMLPrintingSetup_Cell, multiplicity=Multiplicity(1, 1)),
        Property(name="c_cell", type=Comment, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
c_cell51: BinaryAssociation = BinaryAssociation(
    name="c_cell51",
    ends={
        Property(name="Cell52", type=SpreadsheetMLPrintingSetup_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="c_comment", type=Cell, multiplicity=Multiplicity(1, 1))
    }
)
d_cell55: BinaryAssociation = BinaryAssociation(
    name="d_cell55",
    ends={
        Property(name="Cell56", type=SpreadsheetMLPrintingSetup_Data, multiplicity=Multiplicity(1, 1)),
        Property(name="c_data", type=Cell, multiplicity=Multiplicity(1, 1))
    }
)
d_comment57: BinaryAssociation = BinaryAssociation(
    name="d_comment57",
    ends={
        Property(name="Comment58", type=SpreadsheetMLPrintingSetup_Data, multiplicity=Multiplicity(1, 1)),
        Property(name="com_data", type=Comment, multiplicity=Multiplicity(1, 1))
    }
)
value59: BinaryAssociation = BinaryAssociation(
    name="value59",
    ends={
        Property(name="ValueType60", type=SpreadsheetMLPrintingSetup_Data, multiplicity=Multiplicity(1, 1)),
        Property(name="vt_data", type=ValueType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
com_data53: BinaryAssociation = BinaryAssociation(
    name="com_data53",
    ends={
        Property(name="Data54", type=SpreadsheetMLPrintingSetup_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="d_comment", type=Data, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ew_workbook61: BinaryAssociation = BinaryAssociation(
    name="ew_workbook61",
    ends={
        Property(name="Workbook62", type=SpreadsheetMLPrintingSetup_ExcelWorkbook, multiplicity=Multiplicity(1, 1)),
        Property(name="wb_excelWorkbook", type=Workbook, multiplicity=Multiplicity(1, 1))
    }
)
wo_worksheet63: BinaryAssociation = BinaryAssociation(
    name="wo_worksheet63",
    ends={
        Property(name="Worksheet64", type=SpreadsheetMLPrintingSetup_WorksheetOptionsElt, multiplicity=Multiplicity(1, 1)),
        Property(name="w_worksheetOptions", type=Worksheet, multiplicity=Multiplicity(1, 1))
    }
)
wo_print66: BinaryAssociation = BinaryAssociation(
    name="wo_print66",
    ends={
        Property(name="Print", type=SpreadsheetMLPrintingSetup_WorksheetOptionsElt, multiplicity=Multiplicity(1, 1)),
        Property(name="p_worksheetOptions", type=Print, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
wo_pageSetup65: BinaryAssociation = BinaryAssociation(
    name="wo_pageSetup65",
    ends={
        Property(name="PageSetup", type=SpreadsheetMLPrintingSetup_WorksheetOptionsElt, multiplicity=Multiplicity(1, 1)),
        Property(name="ps_worksheetOptions", type=PageSetup, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ps_layout69: BinaryAssociation = BinaryAssociation(
    name="ps_layout69",
    ends={
        Property(name="Layout", type=SpreadsheetMLPrintingSetup_PageSetup, multiplicity=Multiplicity(1, 1)),
        Property(name="l_pageSetup", type=Layout, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ps_header70: BinaryAssociation = BinaryAssociation(
    name="ps_header70",
    ends={
        Property(name="Header", type=SpreadsheetMLPrintingSetup_PageSetup, multiplicity=Multiplicity(1, 1)),
        Property(name="h_pageSetup", type=Header, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ps_footer71: BinaryAssociation = BinaryAssociation(
    name="ps_footer71",
    ends={
        Property(name="Footer", type=SpreadsheetMLPrintingSetup_PageSetup, multiplicity=Multiplicity(1, 1)),
        Property(name="f_pageSetup", type=Footer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ps_worksheetOptions67: BinaryAssociation = BinaryAssociation(
    name="ps_worksheetOptions67",
    ends={
        Property(name="WorksheetOptionsElt68", type=SpreadsheetMLPrintingSetup_PageSetup, multiplicity=Multiplicity(1, 1)),
        Property(name="wo_pageSetup", type=WorksheetOptionsElt, multiplicity=Multiplicity(1, 1))
    }
)
ps_pageMargins72: BinaryAssociation = BinaryAssociation(
    name="ps_pageMargins72",
    ends={
        Property(name="PageMarginsInfo", type=SpreadsheetMLPrintingSetup_PageSetup, multiplicity=Multiplicity(1, 1)),
        Property(name="pm_pageSetup", type=PageMarginsInfo, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
l_pageSetup73: BinaryAssociation = BinaryAssociation(
    name="l_pageSetup73",
    ends={
        Property(name="PageSetup74", type=SpreadsheetMLPrintingSetup_Layout, multiplicity=Multiplicity(1, 1)),
        Property(name="ps_layout", type=PageSetup, multiplicity=Multiplicity(1, 1))
    }
)
h_pageSetup75: BinaryAssociation = BinaryAssociation(
    name="h_pageSetup75",
    ends={
        Property(name="ps_header", type=PageSetup, multiplicity=Multiplicity(1, 1)),
        Property(name="PageSetup76", type=SpreadsheetMLPrintingSetup_Header, multiplicity=Multiplicity(1, 1))
    }
)
f_pageSetup77: BinaryAssociation = BinaryAssociation(
    name="f_pageSetup77",
    ends={
        Property(name="PageSetup78", type=SpreadsheetMLPrintingSetup_Footer, multiplicity=Multiplicity(1, 1)),
        Property(name="ps_footer", type=PageSetup, multiplicity=Multiplicity(1, 1))
    }
)
pm_pageSetup79: BinaryAssociation = BinaryAssociation(
    name="pm_pageSetup79",
    ends={
        Property(name="PageSetup80", type=SpreadsheetMLPrintingSetup_PageMarginsInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="ps_pageMargins", type=PageSetup, multiplicity=Multiplicity(1, 1))
    }
)
p_worksheetOptions81: BinaryAssociation = BinaryAssociation(
    name="p_worksheetOptions81",
    ends={
        Property(name="WorksheetOptionsElt82", type=SpreadsheetMLPrintingSetup_Print, multiplicity=Multiplicity(1, 1)),
        Property(name="wo_print", type=WorksheetOptionsElt, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_SpreadsheetMLPrintingSetup_DateTimeTypeValue_ValueType = Generalization(general=ValueType, specific=SpreadsheetMLPrintingSetup_DateTimeTypeValue)
gen_SpreadsheetMLPrintingSetup_BooleanValue_ValueType = Generalization(general=ValueType, specific=SpreadsheetMLPrintingSetup_BooleanValue)
gen_SpreadsheetMLPrintingSetup_ErrorValue_ValueType = Generalization(general=ValueType, specific=SpreadsheetMLPrintingSetup_ErrorValue)
gen_SpreadsheetMLPrintingSetup_StringValue_ValueType = Generalization(general=ValueType, specific=SpreadsheetMLPrintingSetup_StringValue)
gen_SpreadsheetMLPrintingSetup_NumberValue_ValueType = Generalization(general=ValueType, specific=SpreadsheetMLPrintingSetup_NumberValue)
gen_SpreadsheetMLPrintingSetup_Table_StyledElement = Generalization(general=StyledElement, specific=SpreadsheetMLPrintingSetup_Table)
gen_SpreadsheetMLPrintingSetup_TableElement_StyledElement = Generalization(general=StyledElement, specific=SpreadsheetMLPrintingSetup_TableElement)
gen_SpreadsheetMLPrintingSetup_ColOrRowElement_TableElement = Generalization(general=TableElement, specific=SpreadsheetMLPrintingSetup_ColOrRowElement)
gen_SpreadsheetMLPrintingSetup_Column_ColOrRowElement = Generalization(general=ColOrRowElement, specific=SpreadsheetMLPrintingSetup_Column)
gen_SpreadsheetMLPrintingSetup_Row_ColOrRowElement = Generalization(general=ColOrRowElement, specific=SpreadsheetMLPrintingSetup_Row)
gen_SpreadsheetMLPrintingSetup_Cell_TableElement = Generalization(general=TableElement, specific=SpreadsheetMLPrintingSetup_Cell)
gen_SpreadsheetMLPrintingSetup_Footer_HeaderOrFooterElt = Generalization(general=HeaderOrFooterElt, specific=SpreadsheetMLPrintingSetup_Footer)
gen_SpreadsheetMLPrintingSetup_Header_HeaderOrFooterElt = Generalization(general=HeaderOrFooterElt, specific=SpreadsheetMLPrintingSetup_Header)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={SpreadsheetMLPrintingSetup_VersionType, SpreadsheetMLPrintingSetup_ValueType, SpreadsheetMLPrintingSetup_DateTimeType, SpreadsheetMLPrintingSetup_DateTimeTypeValue, DateTimeType, SpreadsheetMLPrintingSetup_BooleanValue, SpreadsheetMLPrintingSetup_ErrorValue, SpreadsheetMLPrintingSetup_DocumentPropertiesCollection, Workbook, Data, SpreadsheetMLPrintingSetup_StringValue, ValueType, SpreadsheetMLPrintingSetup_NumberValue, VersionType, SpreadsheetMLPrintingSetup_CustomDocumentPropertiesCollection, SpreadsheetMLPrintingSetup_CustomDocumentProperty, CustomDocumentPropertiesCollection, SpreadsheetMLPrintingSetup_SmartTagType, SmartTagsCollection, SpreadsheetMLPrintingSetup_SmartTagsCollection, Cell, SmartTagType, SpreadsheetMLPrintingSetup_Workbook, DocumentPropertiesCollection, CustomDocumentProperty, Worksheet, SpreadsheetMLPrintingSetup_Worksheet, Table, WorksheetOptionsElt, SpreadsheetMLPrintingSetup_StyledElement, SpreadsheetMLPrintingSetup_Table, StyledElement, Column, Row, ExcelWorkbook, SpreadsheetMLPrintingSetup_TableElement, SpreadsheetMLPrintingSetup_ColOrRowElement, TableElement, SpreadsheetMLPrintingSetup_Column, ColOrRowElement, SpreadsheetMLPrintingSetup_Row, SpreadsheetMLPrintingSetup_Cell, Comment, SpreadsheetMLPrintingSetup_Comment, SpreadsheetMLPrintingSetup_ExcelWorkbook, SpreadsheetMLPrintingSetup_Data, SpreadsheetMLPrintingSetup_WorksheetOptionsElt, Print, PageSetup, Layout, Header, Footer, SpreadsheetMLPrintingSetup_PageSetup, PageMarginsInfo, SpreadsheetMLPrintingSetup_Layout, SpreadsheetMLPrintingSetup_Footer, SpreadsheetMLPrintingSetup_HeaderOrFooterElt, SpreadsheetMLPrintingSetup_Header, HeaderOrFooterElt, SpreadsheetMLPrintingSetup_Print, SpreadsheetMLPrintingSetup_PageMarginsInfo, DisplayDrawingObjectsType, CalculationWorkbookType, ExcelWorksheetTypeType, VisibleType, EnableSelectionType, OrientationType, CommentsLayoutType},
    associations={value1, vt_data0, version3, lastPrinted4, created7, lastSaved10, dp_workbook2, cdp_workbook13, customDocumentProperty_cdpe16, value17, smartTagType_ste18, st_workbook19, st_cell21, smartTagTypes22, wb_smartTags23, wb_docProperties25, wb_customDocProperties26, customDocumentProperties15, wb_excelWorkbook28, wb_worksheets29, ws_workbook30, ws_table32, w_worksheetOptions33, t_worksheet34, t_cols36, t_rows37, c_table38, r_table40, r_cells42, c_smartTags44, c_row46, c_data48, c_comment50, c_cell51, d_cell55, d_comment57, value59, com_data53, ew_workbook61, wo_worksheet63, wo_print66, wo_pageSetup65, ps_layout69, ps_header70, ps_footer71, ps_worksheetOptions67, ps_pageMargins72, l_pageSetup73, h_pageSetup75, f_pageSetup77, pm_pageSetup79, p_worksheetOptions81},
    generalizations={gen_SpreadsheetMLPrintingSetup_DateTimeTypeValue_ValueType, gen_SpreadsheetMLPrintingSetup_BooleanValue_ValueType, gen_SpreadsheetMLPrintingSetup_ErrorValue_ValueType, gen_SpreadsheetMLPrintingSetup_StringValue_ValueType, gen_SpreadsheetMLPrintingSetup_NumberValue_ValueType, gen_SpreadsheetMLPrintingSetup_Table_StyledElement, gen_SpreadsheetMLPrintingSetup_TableElement_StyledElement, gen_SpreadsheetMLPrintingSetup_ColOrRowElement_TableElement, gen_SpreadsheetMLPrintingSetup_Column_ColOrRowElement, gen_SpreadsheetMLPrintingSetup_Row_ColOrRowElement, gen_SpreadsheetMLPrintingSetup_Cell_TableElement, gen_SpreadsheetMLPrintingSetup_Footer_HeaderOrFooterElt, gen_SpreadsheetMLPrintingSetup_Header_HeaderOrFooterElt},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)