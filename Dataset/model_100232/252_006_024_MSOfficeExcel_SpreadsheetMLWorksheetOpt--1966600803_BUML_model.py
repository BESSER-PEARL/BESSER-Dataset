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
CalculationWorkbookType: Enumeration = Enumeration(
    name="CalculationWorkbookType",
    literals={
            EnumerationLiteral(name="cwt_automaticCalculation"),
			EnumerationLiteral(name="cwt_manualCalculation"),
			EnumerationLiteral(name="cwt_semiAutomaticCalculation")
    }
)

DisplayDrawingObjectsType: Enumeration = Enumeration(
    name="DisplayDrawingObjectsType",
    literals={
            EnumerationLiteral(name="ddot_displayShapes"),
			EnumerationLiteral(name="ddot_placeHolders"),
			EnumerationLiteral(name="ddot_hideAll")
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

ExcelWorksheetTypeType: Enumeration = Enumeration(
    name="ExcelWorksheetTypeType",
    literals={
            EnumerationLiteral(name="ewt_Worksheet"),
			EnumerationLiteral(name="ewt_Chart"),
			EnumerationLiteral(name="ewt_Macro"),
			EnumerationLiteral(name="ewt_Dialog")
    }
)

# Classes
SpreadsheetMLWorksheetOpt_DateTimeType = Class(name="SpreadsheetMLWorksheetOpt_DateTimeType")
SpreadsheetMLWorksheetOpt_StringValue = Class(name="SpreadsheetMLWorksheetOpt_StringValue")
ValueType = Class(name="ValueType")
SpreadsheetMLWorksheetOpt_NumberValue = Class(name="SpreadsheetMLWorksheetOpt_NumberValue")
SpreadsheetMLWorksheetOpt_DateTimeTypeValue = Class(name="SpreadsheetMLWorksheetOpt_DateTimeTypeValue")
DateTimeType = Class(name="DateTimeType")
SpreadsheetMLWorksheetOpt_VersionType = Class(name="SpreadsheetMLWorksheetOpt_VersionType")
SpreadsheetMLWorksheetOpt_BooleanValue = Class(name="SpreadsheetMLWorksheetOpt_BooleanValue")
SpreadsheetMLWorksheetOpt_ValueType = Class(name="SpreadsheetMLWorksheetOpt_ValueType", is_abstract=True)
Data = Class(name="Data")
Workbook = Class(name="Workbook")
SpreadsheetMLWorksheetOpt_ErrorValue = Class(name="SpreadsheetMLWorksheetOpt_ErrorValue")
SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection = Class(name="SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection")
VersionType = Class(name="VersionType")
SpreadsheetMLWorksheetOpt_CustomDocumentPropertiesCollection = Class(name="SpreadsheetMLWorksheetOpt_CustomDocumentPropertiesCollection")
SmartTagsCollection = Class(name="SmartTagsCollection")
CustomDocumentProperty = Class(name="CustomDocumentProperty")
SpreadsheetMLWorksheetOpt_CustomDocumentProperty = Class(name="SpreadsheetMLWorksheetOpt_CustomDocumentProperty")
CustomDocumentPropertiesCollection = Class(name="CustomDocumentPropertiesCollection")
SpreadsheetMLWorksheetOpt_SmartTagType = Class(name="SpreadsheetMLWorksheetOpt_SmartTagType")
DocumentPropertiesCollection = Class(name="DocumentPropertiesCollection")
SpreadsheetMLWorksheetOpt_SmartTagsCollection = Class(name="SpreadsheetMLWorksheetOpt_SmartTagsCollection")
ExcelWorkbook = Class(name="ExcelWorkbook")
Cell = Class(name="Cell")
SmartTagType = Class(name="SmartTagType")
SpreadsheetMLWorksheetOpt_Workbook = Class(name="SpreadsheetMLWorksheetOpt_Workbook")
Table = Class(name="Table")
WorksheetOptionsElt = Class(name="WorksheetOptionsElt")
Worksheet = Class(name="Worksheet")
SpreadsheetMLWorksheetOpt_Worksheet = Class(name="SpreadsheetMLWorksheetOpt_Worksheet")
Row = Class(name="Row")
SpreadsheetMLWorksheetOpt_StyledElement = Class(name="SpreadsheetMLWorksheetOpt_StyledElement", is_abstract=True)
SpreadsheetMLWorksheetOpt_Table = Class(name="SpreadsheetMLWorksheetOpt_Table")
StyledElement = Class(name="StyledElement")
Column = Class(name="Column")
SpreadsheetMLWorksheetOpt_ColOrRowElement = Class(name="SpreadsheetMLWorksheetOpt_ColOrRowElement", is_abstract=True)
TableElement = Class(name="TableElement")
SpreadsheetMLWorksheetOpt_Column = Class(name="SpreadsheetMLWorksheetOpt_Column")
ColOrRowElement = Class(name="ColOrRowElement")
SpreadsheetMLWorksheetOpt_TableElement = Class(name="SpreadsheetMLWorksheetOpt_TableElement", is_abstract=True)
SpreadsheetMLWorksheetOpt_Cell = Class(name="SpreadsheetMLWorksheetOpt_Cell")
SpreadsheetMLWorksheetOpt_Row = Class(name="SpreadsheetMLWorksheetOpt_Row")
Comment = Class(name="Comment")
SpreadsheetMLWorksheetOpt_Comment = Class(name="SpreadsheetMLWorksheetOpt_Comment")
SpreadsheetMLWorksheetOpt_ExcelWorkbook = Class(name="SpreadsheetMLWorksheetOpt_ExcelWorkbook")
SpreadsheetMLWorksheetOpt_Data = Class(name="SpreadsheetMLWorksheetOpt_Data")
SpreadsheetMLWorksheetOpt_WorksheetOptionsElt = Class(name="SpreadsheetMLWorksheetOpt_WorksheetOptionsElt")

# SpreadsheetMLWorksheetOpt_DateTimeType class attributes and methods
SpreadsheetMLWorksheetOpt_DateTimeType_year: Property = Property(name="year", type=StringType)
SpreadsheetMLWorksheetOpt_DateTimeType_month: Property = Property(name="month", type=StringType)
SpreadsheetMLWorksheetOpt_DateTimeType_day: Property = Property(name="day", type=StringType)
SpreadsheetMLWorksheetOpt_DateTimeType_hour: Property = Property(name="hour", type=StringType)
SpreadsheetMLWorksheetOpt_DateTimeType_minute: Property = Property(name="minute", type=StringType)
SpreadsheetMLWorksheetOpt_DateTimeType_second: Property = Property(name="second", type=StringType)
SpreadsheetMLWorksheetOpt_DateTimeType.attributes={SpreadsheetMLWorksheetOpt_DateTimeType_minute, SpreadsheetMLWorksheetOpt_DateTimeType_month, SpreadsheetMLWorksheetOpt_DateTimeType_hour, SpreadsheetMLWorksheetOpt_DateTimeType_day, SpreadsheetMLWorksheetOpt_DateTimeType_year, SpreadsheetMLWorksheetOpt_DateTimeType_second}

# SpreadsheetMLWorksheetOpt_StringValue class attributes and methods
SpreadsheetMLWorksheetOpt_StringValue_value: Property = Property(name="value", type=StringType)
SpreadsheetMLWorksheetOpt_StringValue.attributes={SpreadsheetMLWorksheetOpt_StringValue_value}

# ValueType class attributes and methods

# SpreadsheetMLWorksheetOpt_NumberValue class attributes and methods
SpreadsheetMLWorksheetOpt_NumberValue_value: Property = Property(name="value", type=StringType)
SpreadsheetMLWorksheetOpt_NumberValue.attributes={SpreadsheetMLWorksheetOpt_NumberValue_value}

# SpreadsheetMLWorksheetOpt_DateTimeTypeValue class attributes and methods

# DateTimeType class attributes and methods

# SpreadsheetMLWorksheetOpt_VersionType class attributes and methods
SpreadsheetMLWorksheetOpt_VersionType_n: Property = Property(name="n", type=StringType)
SpreadsheetMLWorksheetOpt_VersionType_nn: Property = Property(name="nn", type=StringType)
SpreadsheetMLWorksheetOpt_VersionType.attributes={SpreadsheetMLWorksheetOpt_VersionType_nn, SpreadsheetMLWorksheetOpt_VersionType_n}

# SpreadsheetMLWorksheetOpt_BooleanValue class attributes and methods
SpreadsheetMLWorksheetOpt_BooleanValue_value: Property = Property(name="value", type=StringType)
SpreadsheetMLWorksheetOpt_BooleanValue.attributes={SpreadsheetMLWorksheetOpt_BooleanValue_value}

# SpreadsheetMLWorksheetOpt_ValueType class attributes and methods

# Data class attributes and methods

# Workbook class attributes and methods

# SpreadsheetMLWorksheetOpt_ErrorValue class attributes and methods

# SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection class attributes and methods
SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection_title: Property = Property(name="title", type=StringType)
SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection_subject: Property = Property(name="subject", type=StringType)
SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection_keywords: Property = Property(name="keywords", type=StringType)
SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection_description: Property = Property(name="description", type=StringType)
SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection_category: Property = Property(name="category", type=StringType)
SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection_author: Property = Property(name="author", type=StringType)
SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection_lastAuthor: Property = Property(name="lastAuthor", type=StringType)
SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection_manager: Property = Property(name="manager", type=StringType)
SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection_company: Property = Property(name="company", type=StringType)
SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection_hyperlinkBase: Property = Property(name="hyperlinkBase", type=StringType)
SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection_appName: Property = Property(name="appName", type=StringType)
SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection_lines: Property = Property(name="lines", type=StringType)
SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection_paragraphs: Property = Property(name="paragraphs", type=StringType)
SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection_totalTime: Property = Property(name="totalTime", type=StringType)
SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection_pages: Property = Property(name="pages", type=StringType)
SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection_words: Property = Property(name="words", type=StringType)
SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection_revision: Property = Property(name="revision", type=StringType)
SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection_characters: Property = Property(name="characters", type=StringType)
SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection_presentationFormat: Property = Property(name="presentationFormat", type=StringType)
SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection_charactersWithSpaces: Property = Property(name="charactersWithSpaces", type=StringType)
SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection_guid: Property = Property(name="guid", type=StringType)
SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection_bytes: Property = Property(name="bytes", type=StringType)
SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection.attributes={SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection_category, SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection_lines, SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection_presentationFormat, SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection_lastAuthor, SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection_description, SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection_paragraphs, SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection_subject, SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection_appName, SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection_title, SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection_charactersWithSpaces, SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection_keywords, SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection_pages, SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection_revision, SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection_totalTime, SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection_words, SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection_author, SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection_characters, SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection_manager, SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection_hyperlinkBase, SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection_bytes, SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection_company, SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection_guid}

# VersionType class attributes and methods

# SpreadsheetMLWorksheetOpt_CustomDocumentPropertiesCollection class attributes and methods

# SmartTagsCollection class attributes and methods

# CustomDocumentProperty class attributes and methods

# SpreadsheetMLWorksheetOpt_CustomDocumentProperty class attributes and methods
SpreadsheetMLWorksheetOpt_CustomDocumentProperty_name: Property = Property(name="name", type=StringType)
SpreadsheetMLWorksheetOpt_CustomDocumentProperty.attributes={SpreadsheetMLWorksheetOpt_CustomDocumentProperty_name}

# CustomDocumentPropertiesCollection class attributes and methods

# SpreadsheetMLWorksheetOpt_SmartTagType class attributes and methods
SpreadsheetMLWorksheetOpt_SmartTagType_namespaceuri: Property = Property(name="namespaceuri", type=StringType)
SpreadsheetMLWorksheetOpt_SmartTagType_name: Property = Property(name="name", type=StringType)
SpreadsheetMLWorksheetOpt_SmartTagType_url: Property = Property(name="url", type=StringType)
SpreadsheetMLWorksheetOpt_SmartTagType.attributes={SpreadsheetMLWorksheetOpt_SmartTagType_namespaceuri, SpreadsheetMLWorksheetOpt_SmartTagType_name, SpreadsheetMLWorksheetOpt_SmartTagType_url}

# DocumentPropertiesCollection class attributes and methods

# SpreadsheetMLWorksheetOpt_SmartTagsCollection class attributes and methods

# ExcelWorkbook class attributes and methods

# Cell class attributes and methods

# SmartTagType class attributes and methods

# SpreadsheetMLWorksheetOpt_Workbook class attributes and methods

# Table class attributes and methods

# WorksheetOptionsElt class attributes and methods

# Worksheet class attributes and methods

# SpreadsheetMLWorksheetOpt_Worksheet class attributes and methods
SpreadsheetMLWorksheetOpt_Worksheet_name: Property = Property(name="name", type=StringType)
SpreadsheetMLWorksheetOpt_Worksheet_protected: Property = Property(name="protected", type=StringType)
SpreadsheetMLWorksheetOpt_Worksheet_rightToLeft: Property = Property(name="rightToLeft", type=StringType)
SpreadsheetMLWorksheetOpt_Worksheet.attributes={SpreadsheetMLWorksheetOpt_Worksheet_protected, SpreadsheetMLWorksheetOpt_Worksheet_rightToLeft, SpreadsheetMLWorksheetOpt_Worksheet_name}

# Row class attributes and methods

# SpreadsheetMLWorksheetOpt_StyledElement class attributes and methods

# SpreadsheetMLWorksheetOpt_Table class attributes and methods
SpreadsheetMLWorksheetOpt_Table_defaultColumnWidth: Property = Property(name="defaultColumnWidth", type=StringType)
SpreadsheetMLWorksheetOpt_Table_defaultRowHeight: Property = Property(name="defaultRowHeight", type=StringType)
SpreadsheetMLWorksheetOpt_Table_expandedColumnCount: Property = Property(name="expandedColumnCount", type=StringType)
SpreadsheetMLWorksheetOpt_Table_expandedRowCount: Property = Property(name="expandedRowCount", type=StringType)
SpreadsheetMLWorksheetOpt_Table_leftCell: Property = Property(name="leftCell", type=StringType)
SpreadsheetMLWorksheetOpt_Table_topCell: Property = Property(name="topCell", type=StringType)
SpreadsheetMLWorksheetOpt_Table_fullColumns: Property = Property(name="fullColumns", type=StringType)
SpreadsheetMLWorksheetOpt_Table_fullRows: Property = Property(name="fullRows", type=StringType)
SpreadsheetMLWorksheetOpt_Table.attributes={SpreadsheetMLWorksheetOpt_Table_fullColumns, SpreadsheetMLWorksheetOpt_Table_topCell, SpreadsheetMLWorksheetOpt_Table_defaultColumnWidth, SpreadsheetMLWorksheetOpt_Table_fullRows, SpreadsheetMLWorksheetOpt_Table_leftCell, SpreadsheetMLWorksheetOpt_Table_defaultRowHeight, SpreadsheetMLWorksheetOpt_Table_expandedRowCount, SpreadsheetMLWorksheetOpt_Table_expandedColumnCount}

# StyledElement class attributes and methods

# Column class attributes and methods

# SpreadsheetMLWorksheetOpt_ColOrRowElement class attributes and methods
SpreadsheetMLWorksheetOpt_ColOrRowElement_hidden: Property = Property(name="hidden", type=StringType)
SpreadsheetMLWorksheetOpt_ColOrRowElement_span: Property = Property(name="span", type=StringType)
SpreadsheetMLWorksheetOpt_ColOrRowElement.attributes={SpreadsheetMLWorksheetOpt_ColOrRowElement_span, SpreadsheetMLWorksheetOpt_ColOrRowElement_hidden}

# TableElement class attributes and methods

# SpreadsheetMLWorksheetOpt_Column class attributes and methods
SpreadsheetMLWorksheetOpt_Column_autoFitWidth: Property = Property(name="autoFitWidth", type=StringType)
SpreadsheetMLWorksheetOpt_Column_width: Property = Property(name="width", type=StringType)
SpreadsheetMLWorksheetOpt_Column.attributes={SpreadsheetMLWorksheetOpt_Column_autoFitWidth, SpreadsheetMLWorksheetOpt_Column_width}

# ColOrRowElement class attributes and methods

# SpreadsheetMLWorksheetOpt_TableElement class attributes and methods
SpreadsheetMLWorksheetOpt_TableElement_index: Property = Property(name="index", type=StringType)
SpreadsheetMLWorksheetOpt_TableElement.attributes={SpreadsheetMLWorksheetOpt_TableElement_index}

# SpreadsheetMLWorksheetOpt_Cell class attributes and methods
SpreadsheetMLWorksheetOpt_Cell_arrayRange: Property = Property(name="arrayRange", type=StringType)
SpreadsheetMLWorksheetOpt_Cell_formula: Property = Property(name="formula", type=StringType)
SpreadsheetMLWorksheetOpt_Cell_hRef: Property = Property(name="hRef", type=StringType)
SpreadsheetMLWorksheetOpt_Cell_mergeAcross: Property = Property(name="mergeAcross", type=StringType)
SpreadsheetMLWorksheetOpt_Cell_mergeDown: Property = Property(name="mergeDown", type=StringType)
SpreadsheetMLWorksheetOpt_Cell.attributes={SpreadsheetMLWorksheetOpt_Cell_mergeAcross, SpreadsheetMLWorksheetOpt_Cell_arrayRange, SpreadsheetMLWorksheetOpt_Cell_hRef, SpreadsheetMLWorksheetOpt_Cell_formula, SpreadsheetMLWorksheetOpt_Cell_mergeDown}

# SpreadsheetMLWorksheetOpt_Row class attributes and methods
SpreadsheetMLWorksheetOpt_Row_autoFitHeight: Property = Property(name="autoFitHeight", type=StringType)
SpreadsheetMLWorksheetOpt_Row_height: Property = Property(name="height", type=StringType)
SpreadsheetMLWorksheetOpt_Row.attributes={SpreadsheetMLWorksheetOpt_Row_autoFitHeight, SpreadsheetMLWorksheetOpt_Row_height}

# Comment class attributes and methods

# SpreadsheetMLWorksheetOpt_Comment class attributes and methods
SpreadsheetMLWorksheetOpt_Comment_author: Property = Property(name="author", type=StringType)
SpreadsheetMLWorksheetOpt_Comment_showAlways: Property = Property(name="showAlways", type=StringType)
SpreadsheetMLWorksheetOpt_Comment.attributes={SpreadsheetMLWorksheetOpt_Comment_showAlways, SpreadsheetMLWorksheetOpt_Comment_author}

# SpreadsheetMLWorksheetOpt_ExcelWorkbook class attributes and methods
SpreadsheetMLWorksheetOpt_ExcelWorkbook_windowHidden: Property = Property(name="windowHidden", type=StringType)
SpreadsheetMLWorksheetOpt_ExcelWorkbook_hideHorizontalScrollBar: Property = Property(name="hideHorizontalScrollBar", type=StringType)
SpreadsheetMLWorksheetOpt_ExcelWorkbook_hideVerticalScrollBar: Property = Property(name="hideVerticalScrollBar", type=StringType)
SpreadsheetMLWorksheetOpt_ExcelWorkbook_hideWorkbookTabs: Property = Property(name="hideWorkbookTabs", type=StringType)
SpreadsheetMLWorksheetOpt_ExcelWorkbook_windowHeight: Property = Property(name="windowHeight", type=StringType)
SpreadsheetMLWorksheetOpt_ExcelWorkbook_windowWidth: Property = Property(name="windowWidth", type=StringType)
SpreadsheetMLWorksheetOpt_ExcelWorkbook_windowTopX: Property = Property(name="windowTopX", type=StringType)
SpreadsheetMLWorksheetOpt_ExcelWorkbook_windowTopY: Property = Property(name="windowTopY", type=StringType)
SpreadsheetMLWorksheetOpt_ExcelWorkbook_activeSheet: Property = Property(name="activeSheet", type=StringType)
SpreadsheetMLWorksheetOpt_ExcelWorkbook_selectedSheets: Property = Property(name="selectedSheets", type=StringType)
SpreadsheetMLWorksheetOpt_ExcelWorkbook_displayInkNotes: Property = Property(name="displayInkNotes", type=StringType)
SpreadsheetMLWorksheetOpt_ExcelWorkbook_embedSaveSmartTags: Property = Property(name="embedSaveSmartTags", type=StringType)
SpreadsheetMLWorksheetOpt_ExcelWorkbook_futureVer: Property = Property(name="futureVer", type=StringType)
SpreadsheetMLWorksheetOpt_ExcelWorkbook_tabRatio: Property = Property(name="tabRatio", type=StringType)
SpreadsheetMLWorksheetOpt_ExcelWorkbook_windowIconic: Property = Property(name="windowIconic", type=StringType)
SpreadsheetMLWorksheetOpt_ExcelWorkbook_displayDrawingObjects: Property = Property(name="displayDrawingObjects", type=StringType)
SpreadsheetMLWorksheetOpt_ExcelWorkbook_activeChart: Property = Property(name="activeChart", type=StringType)
SpreadsheetMLWorksheetOpt_ExcelWorkbook_firstVisibleSheet: Property = Property(name="firstVisibleSheet", type=StringType)
SpreadsheetMLWorksheetOpt_ExcelWorkbook_hidePivotTableFieldList: Property = Property(name="hidePivotTableFieldList", type=StringType)
SpreadsheetMLWorksheetOpt_ExcelWorkbook_protectStructure: Property = Property(name="protectStructure", type=StringType)
SpreadsheetMLWorksheetOpt_ExcelWorkbook_protectWindows: Property = Property(name="protectWindows", type=StringType)
SpreadsheetMLWorksheetOpt_ExcelWorkbook_iteration: Property = Property(name="iteration", type=StringType)
SpreadsheetMLWorksheetOpt_ExcelWorkbook_maxIterations: Property = Property(name="maxIterations", type=StringType)
SpreadsheetMLWorksheetOpt_ExcelWorkbook_maxChange: Property = Property(name="maxChange", type=StringType)
SpreadsheetMLWorksheetOpt_ExcelWorkbook_precisionAsDisplayed: Property = Property(name="precisionAsDisplayed", type=StringType)
SpreadsheetMLWorksheetOpt_ExcelWorkbook_doNotSaveLinkValues: Property = Property(name="doNotSaveLinkValues", type=StringType)
SpreadsheetMLWorksheetOpt_ExcelWorkbook_noAutoRecover: Property = Property(name="noAutoRecover", type=StringType)
SpreadsheetMLWorksheetOpt_ExcelWorkbook_createBackup: Property = Property(name="createBackup", type=StringType)
SpreadsheetMLWorksheetOpt_ExcelWorkbook_calculation: Property = Property(name="calculation", type=StringType)
SpreadsheetMLWorksheetOpt_ExcelWorkbook_doNotCalculateBeforeSave: Property = Property(name="doNotCalculateBeforeSave", type=StringType)
SpreadsheetMLWorksheetOpt_ExcelWorkbook_date1904: Property = Property(name="date1904", type=StringType)
SpreadsheetMLWorksheetOpt_ExcelWorkbook_refModeR1C1: Property = Property(name="refModeR1C1", type=StringType)
SpreadsheetMLWorksheetOpt_ExcelWorkbook_acceptLabelsInFormulas: Property = Property(name="acceptLabelsInFormulas", type=StringType)
SpreadsheetMLWorksheetOpt_ExcelWorkbook_uncalced: Property = Property(name="uncalced", type=StringType)
SpreadsheetMLWorksheetOpt_ExcelWorkbook.attributes={SpreadsheetMLWorksheetOpt_ExcelWorkbook_hidePivotTableFieldList, SpreadsheetMLWorksheetOpt_ExcelWorkbook_windowHeight, SpreadsheetMLWorksheetOpt_ExcelWorkbook_protectStructure, SpreadsheetMLWorksheetOpt_ExcelWorkbook_windowIconic, SpreadsheetMLWorksheetOpt_ExcelWorkbook_activeSheet, SpreadsheetMLWorksheetOpt_ExcelWorkbook_selectedSheets, SpreadsheetMLWorksheetOpt_ExcelWorkbook_maxIterations, SpreadsheetMLWorksheetOpt_ExcelWorkbook_windowTopY, SpreadsheetMLWorksheetOpt_ExcelWorkbook_displayDrawingObjects, SpreadsheetMLWorksheetOpt_ExcelWorkbook_tabRatio, SpreadsheetMLWorksheetOpt_ExcelWorkbook_refModeR1C1, SpreadsheetMLWorksheetOpt_ExcelWorkbook_displayInkNotes, SpreadsheetMLWorksheetOpt_ExcelWorkbook_date1904, SpreadsheetMLWorksheetOpt_ExcelWorkbook_windowWidth, SpreadsheetMLWorksheetOpt_ExcelWorkbook_activeChart, SpreadsheetMLWorksheetOpt_ExcelWorkbook_embedSaveSmartTags, SpreadsheetMLWorksheetOpt_ExcelWorkbook_calculation, SpreadsheetMLWorksheetOpt_ExcelWorkbook_futureVer, SpreadsheetMLWorksheetOpt_ExcelWorkbook_createBackup, SpreadsheetMLWorksheetOpt_ExcelWorkbook_firstVisibleSheet, SpreadsheetMLWorksheetOpt_ExcelWorkbook_noAutoRecover, SpreadsheetMLWorksheetOpt_ExcelWorkbook_hideHorizontalScrollBar, SpreadsheetMLWorksheetOpt_ExcelWorkbook_precisionAsDisplayed, SpreadsheetMLWorksheetOpt_ExcelWorkbook_doNotCalculateBeforeSave, SpreadsheetMLWorksheetOpt_ExcelWorkbook_maxChange, SpreadsheetMLWorksheetOpt_ExcelWorkbook_hideWorkbookTabs, SpreadsheetMLWorksheetOpt_ExcelWorkbook_hideVerticalScrollBar, SpreadsheetMLWorksheetOpt_ExcelWorkbook_iteration, SpreadsheetMLWorksheetOpt_ExcelWorkbook_windowTopX, SpreadsheetMLWorksheetOpt_ExcelWorkbook_doNotSaveLinkValues, SpreadsheetMLWorksheetOpt_ExcelWorkbook_uncalced, SpreadsheetMLWorksheetOpt_ExcelWorkbook_windowHidden, SpreadsheetMLWorksheetOpt_ExcelWorkbook_protectWindows, SpreadsheetMLWorksheetOpt_ExcelWorkbook_acceptLabelsInFormulas}

# SpreadsheetMLWorksheetOpt_Data class attributes and methods

# SpreadsheetMLWorksheetOpt_WorksheetOptionsElt class attributes and methods
SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_fitToPage: Property = Property(name="fitToPage", type=StringType)
SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_doNotDisplayColHeaders: Property = Property(name="doNotDisplayColHeaders", type=StringType)
SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_unsynced: Property = Property(name="unsynced", type=StringType)
SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_selected: Property = Property(name="selected", type=StringType)
SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_codeName: Property = Property(name="codeName", type=StringType)
SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_displayPageBreak: Property = Property(name="displayPageBreak", type=StringType)
SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_transitionExpressionEvaluation: Property = Property(name="transitionExpressionEvaluation", type=StringType)
SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_transitionFormulaEntry: Property = Property(name="transitionFormulaEntry", type=StringType)
SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_zoom: Property = Property(name="zoom", type=StringType)
SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_pageBreakZoom: Property = Property(name="pageBreakZoom", type=StringType)
SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_doNotDisplayRowHeaders: Property = Property(name="doNotDisplayRowHeaders", type=StringType)
SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_gridlineColor: Property = Property(name="gridlineColor", type=StringType)
SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_name: Property = Property(name="name", type=StringType)
SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_excelWorksheetType: Property = Property(name="excelWorksheetType", type=StringType)
SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_intlMacro: Property = Property(name="intlMacro", type=StringType)
SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_standardWidth: Property = Property(name="standardWidth", type=StringType)
SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_visible: Property = Property(name="visible", type=StringType)
SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_leftColumnVisible: Property = Property(name="leftColumnVisible", type=StringType)
SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_displayRightToLeft: Property = Property(name="displayRightToLeft", type=StringType)
SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_gridlineColorIndex: Property = Property(name="gridlineColorIndex", type=StringType)
SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_displayFormulas: Property = Property(name="displayFormulas", type=StringType)
SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_doNotDisplayGridlines: Property = Property(name="doNotDisplayGridlines", type=StringType)
SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_doNotDisplayHeadings: Property = Property(name="doNotDisplayHeadings", type=StringType)
SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_showPageBreakZoom: Property = Property(name="showPageBreakZoom", type=StringType)
SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_defaultRowHeight: Property = Property(name="defaultRowHeight", type=StringType)
SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_defaultColumnWidth: Property = Property(name="defaultColumnWidth", type=StringType)
SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_noSummaryColumnsRightDetail: Property = Property(name="noSummaryColumnsRightDetail", type=StringType)
SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_doNotDisplayZeros: Property = Property(name="doNotDisplayZeros", type=StringType)
SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_activeRow: Property = Property(name="activeRow", type=StringType)
SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_activeColumn: Property = Property(name="activeColumn", type=StringType)
SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_filterOn: Property = Property(name="filterOn", type=StringType)
SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_rangeSelection: Property = Property(name="rangeSelection", type=StringType)
SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_doNotDisplayOutline: Property = Property(name="doNotDisplayOutline", type=StringType)
SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_applyAutomaticOutlineStyles: Property = Property(name="applyAutomaticOutlineStyles", type=StringType)
SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_noSummaryRowsBelowDetail: Property = Property(name="noSummaryRowsBelowDetail", type=StringType)
SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_splitHorizontal: Property = Property(name="splitHorizontal", type=StringType)
SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_splitVertical: Property = Property(name="splitVertical", type=StringType)
SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_freezePanes: Property = Property(name="freezePanes", type=StringType)
SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_frozenNoSplit: Property = Property(name="frozenNoSplit", type=StringType)
SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_tabColorIndex: Property = Property(name="tabColorIndex", type=StringType)
SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_protectContentst: Property = Property(name="protectContentst", type=StringType)
SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_topRowVisible: Property = Property(name="topRowVisible", type=StringType)
SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_topRowBottomPane: Property = Property(name="topRowBottomPane", type=StringType)
SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_leftColumnRightPane: Property = Property(name="leftColumnRightPane", type=StringType)
SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_activePane: Property = Property(name="activePane", type=StringType)
SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_allowSizeRows: Property = Property(name="allowSizeRows", type=StringType)
SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_allowInsertCols: Property = Property(name="allowInsertCols", type=StringType)
SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_allowInsertRows: Property = Property(name="allowInsertRows", type=StringType)
SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_allowInsertHyperlinks: Property = Property(name="allowInsertHyperlinks", type=StringType)
SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_allowDeleteCols: Property = Property(name="allowDeleteCols", type=StringType)
SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_allowDeleteRows: Property = Property(name="allowDeleteRows", type=StringType)
SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_allowSort: Property = Property(name="allowSort", type=StringType)
SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_allowFilter: Property = Property(name="allowFilter", type=StringType)
SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_protectObjects: Property = Property(name="protectObjects", type=StringType)
SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_protectScenarios: Property = Property(name="protectScenarios", type=StringType)
SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_enableSelection: Property = Property(name="enableSelection", type=StringType)
SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_allowFormatCells: Property = Property(name="allowFormatCells", type=StringType)
SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_allowSizeCols: Property = Property(name="allowSizeCols", type=StringType)
SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_allowUsePivotTables: Property = Property(name="allowUsePivotTables", type=StringType)
SpreadsheetMLWorksheetOpt_WorksheetOptionsElt.attributes={SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_standardWidth, SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_allowInsertCols, SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_doNotDisplayZeros, SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_visible, SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_displayPageBreak, SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_filterOn, SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_protectScenarios, SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_gridlineColor, SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_name, SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_activeRow, SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_topRowVisible, SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_gridlineColorIndex, SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_defaultColumnWidth, SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_applyAutomaticOutlineStyles, SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_defaultRowHeight, SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_splitHorizontal, SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_codeName, SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_displayFormulas, SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_noSummaryColumnsRightDetail, SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_freezePanes, SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_leftColumnRightPane, SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_tabColorIndex, SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_frozenNoSplit, SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_allowDeleteCols, SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_zoom, SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_protectObjects, SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_allowInsertRows, SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_leftColumnVisible, SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_displayRightToLeft, SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_allowSizeCols, SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_splitVertical, SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_topRowBottomPane, SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_allowUsePivotTables, SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_noSummaryRowsBelowDetail, SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_allowFilter, SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_fitToPage, SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_pageBreakZoom, SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_doNotDisplayRowHeaders, SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_allowDeleteRows, SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_allowInsertHyperlinks, SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_allowSort, SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_activePane, SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_doNotDisplayGridlines, SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_allowFormatCells, SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_selected, SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_excelWorksheetType, SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_showPageBreakZoom, SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_rangeSelection, SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_activeColumn, SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_intlMacro, SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_doNotDisplayOutline, SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_transitionFormulaEntry, SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_enableSelection, SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_transitionExpressionEvaluation, SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_allowSizeRows, SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_unsynced, SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_protectContentst, SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_doNotDisplayHeadings, SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_doNotDisplayColHeaders}

# Relationships
value1: BinaryAssociation = BinaryAssociation(
    name="value1",
    ends={
        Property(name="DateTimeType", type=SpreadsheetMLWorksheetOpt_DateTimeTypeValue, multiplicity=Multiplicity(1, 1)),
        Property(name="SpreadsheetMLWorksheetOpt_DateTimeTypeValue", type=DateTimeType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
vt_data0: BinaryAssociation = BinaryAssociation(
    name="vt_data0",
    ends={
        Property(name="Data", type=SpreadsheetMLWorksheetOpt_ValueType, multiplicity=Multiplicity(1, 1)),
        Property(name="value", type=Data, multiplicity=Multiplicity(1, 1))
    }
)
dp_workbook2: BinaryAssociation = BinaryAssociation(
    name="dp_workbook2",
    ends={
        Property(name="Workbook", type=SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="wb_docProperties", type=Workbook, multiplicity=Multiplicity(1, 1))
    }
)
version3: BinaryAssociation = BinaryAssociation(
    name="version3",
    ends={
        Property(name="VersionType", type=SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection", type=VersionType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lastPrinted4: BinaryAssociation = BinaryAssociation(
    name="lastPrinted4",
    ends={
        Property(name="DateTimeType6", type=SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection5", type=DateTimeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
created7: BinaryAssociation = BinaryAssociation(
    name="created7",
    ends={
        Property(name="DateTimeType9", type=SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection8", type=DateTimeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lastSaved10: BinaryAssociation = BinaryAssociation(
    name="lastSaved10",
    ends={
        Property(name="DateTimeType12", type=SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection11", type=DateTimeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
smartTagType_ste18: BinaryAssociation = BinaryAssociation(
    name="smartTagType_ste18",
    ends={
        Property(name="SmartTagsCollection", type=SpreadsheetMLWorksheetOpt_SmartTagType, multiplicity=Multiplicity(1, 1)),
        Property(name="smartTagTypes", type=SmartTagsCollection, multiplicity=Multiplicity(1, 1))
    }
)
cdp_workbook13: BinaryAssociation = BinaryAssociation(
    name="cdp_workbook13",
    ends={
        Property(name="Workbook14", type=SpreadsheetMLWorksheetOpt_CustomDocumentPropertiesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="wb_customDocProperties", type=Workbook, multiplicity=Multiplicity(1, 1))
    }
)
customDocumentProperties15: BinaryAssociation = BinaryAssociation(
    name="customDocumentProperties15",
    ends={
        Property(name="CustomDocumentProperty", type=SpreadsheetMLWorksheetOpt_CustomDocumentPropertiesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="customDocumentProperty_cdpe", type=CustomDocumentProperty, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
customDocumentProperty_cdpe16: BinaryAssociation = BinaryAssociation(
    name="customDocumentProperty_cdpe16",
    ends={
        Property(name="CustomDocumentPropertiesCollection", type=SpreadsheetMLWorksheetOpt_CustomDocumentProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="customDocumentProperties", type=CustomDocumentPropertiesCollection, multiplicity=Multiplicity(1, 1))
    }
)
value17: BinaryAssociation = BinaryAssociation(
    name="value17",
    ends={
        Property(name="ValueType", type=SpreadsheetMLWorksheetOpt_CustomDocumentProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="SpreadsheetMLWorksheetOpt_CustomDocumentProperty", type=ValueType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
wb_smartTags23: BinaryAssociation = BinaryAssociation(
    name="wb_smartTags23",
    ends={
        Property(name="SmartTagsCollection24", type=SpreadsheetMLWorksheetOpt_Workbook, multiplicity=Multiplicity(1, 1)),
        Property(name="st_workbook", type=SmartTagsCollection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
wb_docProperties25: BinaryAssociation = BinaryAssociation(
    name="wb_docProperties25",
    ends={
        Property(name="DocumentPropertiesCollection", type=SpreadsheetMLWorksheetOpt_Workbook, multiplicity=Multiplicity(1, 1)),
        Property(name="dp_workbook", type=DocumentPropertiesCollection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
wb_customDocProperties26: BinaryAssociation = BinaryAssociation(
    name="wb_customDocProperties26",
    ends={
        Property(name="CustomDocumentPropertiesCollection27", type=SpreadsheetMLWorksheetOpt_Workbook, multiplicity=Multiplicity(1, 1)),
        Property(name="cdp_workbook", type=CustomDocumentPropertiesCollection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
st_workbook19: BinaryAssociation = BinaryAssociation(
    name="st_workbook19",
    ends={
        Property(name="Workbook20", type=SpreadsheetMLWorksheetOpt_SmartTagsCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="wb_smartTags", type=Workbook, multiplicity=Multiplicity(1, 1))
    }
)
st_cell21: BinaryAssociation = BinaryAssociation(
    name="st_cell21",
    ends={
        Property(name="Cell", type=SpreadsheetMLWorksheetOpt_SmartTagsCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="c_smartTags", type=Cell, multiplicity=Multiplicity(1, 1))
    }
)
smartTagTypes22: BinaryAssociation = BinaryAssociation(
    name="smartTagTypes22",
    ends={
        Property(name="SmartTagType", type=SpreadsheetMLWorksheetOpt_SmartTagsCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="smartTagType_ste", type=SmartTagType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ws_table32: BinaryAssociation = BinaryAssociation(
    name="ws_table32",
    ends={
        Property(name="Table", type=SpreadsheetMLWorksheetOpt_Worksheet, multiplicity=Multiplicity(1, 1)),
        Property(name="t_worksheet", type=Table, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
w_worksheetOptions33: BinaryAssociation = BinaryAssociation(
    name="w_worksheetOptions33",
    ends={
        Property(name="WorksheetOptionsElt", type=SpreadsheetMLWorksheetOpt_Worksheet, multiplicity=Multiplicity(1, 1)),
        Property(name="wo_worksheet", type=WorksheetOptionsElt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
wb_excelWorkbook28: BinaryAssociation = BinaryAssociation(
    name="wb_excelWorkbook28",
    ends={
        Property(name="ExcelWorkbook", type=SpreadsheetMLWorksheetOpt_Workbook, multiplicity=Multiplicity(1, 1)),
        Property(name="ew_workbook", type=ExcelWorkbook, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
wb_worksheets29: BinaryAssociation = BinaryAssociation(
    name="wb_worksheets29",
    ends={
        Property(name="Worksheet", type=SpreadsheetMLWorksheetOpt_Workbook, multiplicity=Multiplicity(1, 1)),
        Property(name="ws_workbook", type=Worksheet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ws_workbook30: BinaryAssociation = BinaryAssociation(
    name="ws_workbook30",
    ends={
        Property(name="Workbook31", type=SpreadsheetMLWorksheetOpt_Worksheet, multiplicity=Multiplicity(1, 1)),
        Property(name="wb_worksheets", type=Workbook, multiplicity=Multiplicity(1, 1))
    }
)
t_rows37: BinaryAssociation = BinaryAssociation(
    name="t_rows37",
    ends={
        Property(name="Row", type=SpreadsheetMLWorksheetOpt_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="r_table", type=Row, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
t_worksheet34: BinaryAssociation = BinaryAssociation(
    name="t_worksheet34",
    ends={
        Property(name="Worksheet35", type=SpreadsheetMLWorksheetOpt_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="ws_table", type=Worksheet, multiplicity=Multiplicity(1, 1))
    }
)
t_cols36: BinaryAssociation = BinaryAssociation(
    name="t_cols36",
    ends={
        Property(name="Column", type=SpreadsheetMLWorksheetOpt_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="c_table", type=Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
c_table38: BinaryAssociation = BinaryAssociation(
    name="c_table38",
    ends={
        Property(name="Table39", type=SpreadsheetMLWorksheetOpt_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="t_cols", type=Table, multiplicity=Multiplicity(1, 1))
    }
)
c_smartTags44: BinaryAssociation = BinaryAssociation(
    name="c_smartTags44",
    ends={
        Property(name="SmartTagsCollection45", type=SpreadsheetMLWorksheetOpt_Cell, multiplicity=Multiplicity(1, 1)),
        Property(name="st_cell", type=SmartTagsCollection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
c_row46: BinaryAssociation = BinaryAssociation(
    name="c_row46",
    ends={
        Property(name="Row47", type=SpreadsheetMLWorksheetOpt_Cell, multiplicity=Multiplicity(1, 1)),
        Property(name="r_cells", type=Row, multiplicity=Multiplicity(1, 1))
    }
)
r_table40: BinaryAssociation = BinaryAssociation(
    name="r_table40",
    ends={
        Property(name="Table41", type=SpreadsheetMLWorksheetOpt_Row, multiplicity=Multiplicity(1, 1)),
        Property(name="t_rows", type=Table, multiplicity=Multiplicity(1, 1))
    }
)
r_cells42: BinaryAssociation = BinaryAssociation(
    name="r_cells42",
    ends={
        Property(name="Cell43", type=SpreadsheetMLWorksheetOpt_Row, multiplicity=Multiplicity(1, 1)),
        Property(name="c_row", type=Cell, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
c_data48: BinaryAssociation = BinaryAssociation(
    name="c_data48",
    ends={
        Property(name="d_cell", type=Data, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="Data49", type=SpreadsheetMLWorksheetOpt_Cell, multiplicity=Multiplicity(1, 1))
    }
)
c_comment50: BinaryAssociation = BinaryAssociation(
    name="c_comment50",
    ends={
        Property(name="Comment", type=SpreadsheetMLWorksheetOpt_Cell, multiplicity=Multiplicity(1, 1)),
        Property(name="c_cell", type=Comment, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
c_cell51: BinaryAssociation = BinaryAssociation(
    name="c_cell51",
    ends={
        Property(name="Cell52", type=SpreadsheetMLWorksheetOpt_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="c_comment", type=Cell, multiplicity=Multiplicity(1, 1))
    }
)
d_cell55: BinaryAssociation = BinaryAssociation(
    name="d_cell55",
    ends={
        Property(name="Cell56", type=SpreadsheetMLWorksheetOpt_Data, multiplicity=Multiplicity(1, 1)),
        Property(name="c_data", type=Cell, multiplicity=Multiplicity(1, 1))
    }
)
d_comment57: BinaryAssociation = BinaryAssociation(
    name="d_comment57",
    ends={
        Property(name="Comment58", type=SpreadsheetMLWorksheetOpt_Data, multiplicity=Multiplicity(1, 1)),
        Property(name="com_data", type=Comment, multiplicity=Multiplicity(1, 1))
    }
)
value59: BinaryAssociation = BinaryAssociation(
    name="value59",
    ends={
        Property(name="ValueType60", type=SpreadsheetMLWorksheetOpt_Data, multiplicity=Multiplicity(1, 1)),
        Property(name="vt_data", type=ValueType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
com_data53: BinaryAssociation = BinaryAssociation(
    name="com_data53",
    ends={
        Property(name="Data54", type=SpreadsheetMLWorksheetOpt_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="d_comment", type=Data, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ew_workbook61: BinaryAssociation = BinaryAssociation(
    name="ew_workbook61",
    ends={
        Property(name="Workbook62", type=SpreadsheetMLWorksheetOpt_ExcelWorkbook, multiplicity=Multiplicity(1, 1)),
        Property(name="wb_excelWorkbook", type=Workbook, multiplicity=Multiplicity(1, 1))
    }
)
wo_worksheet63: BinaryAssociation = BinaryAssociation(
    name="wo_worksheet63",
    ends={
        Property(name="Worksheet64", type=SpreadsheetMLWorksheetOpt_WorksheetOptionsElt, multiplicity=Multiplicity(1, 1)),
        Property(name="w_worksheetOptions", type=Worksheet, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_SpreadsheetMLWorksheetOpt_StringValue_ValueType = Generalization(general=ValueType, specific=SpreadsheetMLWorksheetOpt_StringValue)
gen_SpreadsheetMLWorksheetOpt_NumberValue_ValueType = Generalization(general=ValueType, specific=SpreadsheetMLWorksheetOpt_NumberValue)
gen_SpreadsheetMLWorksheetOpt_DateTimeTypeValue_ValueType = Generalization(general=ValueType, specific=SpreadsheetMLWorksheetOpt_DateTimeTypeValue)
gen_SpreadsheetMLWorksheetOpt_BooleanValue_ValueType = Generalization(general=ValueType, specific=SpreadsheetMLWorksheetOpt_BooleanValue)
gen_SpreadsheetMLWorksheetOpt_ErrorValue_ValueType = Generalization(general=ValueType, specific=SpreadsheetMLWorksheetOpt_ErrorValue)
gen_SpreadsheetMLWorksheetOpt_Table_StyledElement = Generalization(general=StyledElement, specific=SpreadsheetMLWorksheetOpt_Table)
gen_SpreadsheetMLWorksheetOpt_ColOrRowElement_TableElement = Generalization(general=TableElement, specific=SpreadsheetMLWorksheetOpt_ColOrRowElement)
gen_SpreadsheetMLWorksheetOpt_Column_ColOrRowElement = Generalization(general=ColOrRowElement, specific=SpreadsheetMLWorksheetOpt_Column)
gen_SpreadsheetMLWorksheetOpt_TableElement_StyledElement = Generalization(general=StyledElement, specific=SpreadsheetMLWorksheetOpt_TableElement)
gen_SpreadsheetMLWorksheetOpt_Cell_TableElement = Generalization(general=TableElement, specific=SpreadsheetMLWorksheetOpt_Cell)
gen_SpreadsheetMLWorksheetOpt_Row_ColOrRowElement = Generalization(general=ColOrRowElement, specific=SpreadsheetMLWorksheetOpt_Row)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={SpreadsheetMLWorksheetOpt_DateTimeType, SpreadsheetMLWorksheetOpt_StringValue, ValueType, SpreadsheetMLWorksheetOpt_NumberValue, SpreadsheetMLWorksheetOpt_DateTimeTypeValue, DateTimeType, SpreadsheetMLWorksheetOpt_VersionType, SpreadsheetMLWorksheetOpt_BooleanValue, SpreadsheetMLWorksheetOpt_ValueType, Data, Workbook, SpreadsheetMLWorksheetOpt_ErrorValue, SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection, VersionType, SpreadsheetMLWorksheetOpt_CustomDocumentPropertiesCollection, SmartTagsCollection, CustomDocumentProperty, SpreadsheetMLWorksheetOpt_CustomDocumentProperty, CustomDocumentPropertiesCollection, SpreadsheetMLWorksheetOpt_SmartTagType, DocumentPropertiesCollection, SpreadsheetMLWorksheetOpt_SmartTagsCollection, ExcelWorkbook, Cell, SmartTagType, SpreadsheetMLWorksheetOpt_Workbook, Table, WorksheetOptionsElt, Worksheet, SpreadsheetMLWorksheetOpt_Worksheet, Row, SpreadsheetMLWorksheetOpt_StyledElement, SpreadsheetMLWorksheetOpt_Table, StyledElement, Column, SpreadsheetMLWorksheetOpt_ColOrRowElement, TableElement, SpreadsheetMLWorksheetOpt_Column, ColOrRowElement, SpreadsheetMLWorksheetOpt_TableElement, SpreadsheetMLWorksheetOpt_Cell, SpreadsheetMLWorksheetOpt_Row, Comment, SpreadsheetMLWorksheetOpt_Comment, SpreadsheetMLWorksheetOpt_ExcelWorkbook, SpreadsheetMLWorksheetOpt_Data, SpreadsheetMLWorksheetOpt_WorksheetOptionsElt, CalculationWorkbookType, DisplayDrawingObjectsType, VisibleType, EnableSelectionType, ExcelWorksheetTypeType},
    associations={value1, vt_data0, dp_workbook2, version3, lastPrinted4, created7, lastSaved10, smartTagType_ste18, cdp_workbook13, customDocumentProperties15, customDocumentProperty_cdpe16, value17, wb_smartTags23, wb_docProperties25, wb_customDocProperties26, st_workbook19, st_cell21, smartTagTypes22, ws_table32, w_worksheetOptions33, wb_excelWorkbook28, wb_worksheets29, ws_workbook30, t_rows37, t_worksheet34, t_cols36, c_table38, c_smartTags44, c_row46, r_table40, r_cells42, c_data48, c_comment50, c_cell51, d_cell55, d_comment57, value59, com_data53, ew_workbook61, wo_worksheet63},
    generalizations={gen_SpreadsheetMLWorksheetOpt_StringValue_ValueType, gen_SpreadsheetMLWorksheetOpt_NumberValue_ValueType, gen_SpreadsheetMLWorksheetOpt_DateTimeTypeValue_ValueType, gen_SpreadsheetMLWorksheetOpt_BooleanValue_ValueType, gen_SpreadsheetMLWorksheetOpt_ErrorValue_ValueType, gen_SpreadsheetMLWorksheetOpt_Table_StyledElement, gen_SpreadsheetMLWorksheetOpt_ColOrRowElement_TableElement, gen_SpreadsheetMLWorksheetOpt_Column_ColOrRowElement, gen_SpreadsheetMLWorksheetOpt_TableElement_StyledElement, gen_SpreadsheetMLWorksheetOpt_Cell_TableElement, gen_SpreadsheetMLWorksheetOpt_Row_ColOrRowElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)