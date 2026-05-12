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

# Classes
SpreadsheetMLWorkbookProp_DateTimeType = Class(name="SpreadsheetMLWorkbookProp_DateTimeType")
SpreadsheetMLWorkbookProp_VersionType = Class(name="SpreadsheetMLWorkbookProp_VersionType")
SpreadsheetMLWorkbookProp_ValueType = Class(name="SpreadsheetMLWorkbookProp_ValueType", is_abstract=True)
Data = Class(name="Data")
SpreadsheetMLWorkbookProp_StringValue = Class(name="SpreadsheetMLWorkbookProp_StringValue")
ValueType = Class(name="ValueType")
SpreadsheetMLWorkbookProp_NumberValue = Class(name="SpreadsheetMLWorkbookProp_NumberValue")
SpreadsheetMLWorkbookProp_DateTimeTypeValue = Class(name="SpreadsheetMLWorkbookProp_DateTimeTypeValue")
DateTimeType = Class(name="DateTimeType")
SpreadsheetMLWorkbookProp_BooleanValue = Class(name="SpreadsheetMLWorkbookProp_BooleanValue")
SpreadsheetMLWorkbookProp_ErrorValue = Class(name="SpreadsheetMLWorkbookProp_ErrorValue")
SpreadsheetMLWorkbookProp_DocumentPropertiesCollection = Class(name="SpreadsheetMLWorkbookProp_DocumentPropertiesCollection")
Workbook = Class(name="Workbook")
VersionType = Class(name="VersionType")
CustomDocumentProperty = Class(name="CustomDocumentProperty")
SpreadsheetMLWorkbookProp_CustomDocumentProperty = Class(name="SpreadsheetMLWorkbookProp_CustomDocumentProperty")
SpreadsheetMLWorkbookProp_CustomDocumentPropertiesCollection = Class(name="SpreadsheetMLWorkbookProp_CustomDocumentPropertiesCollection")
Cell = Class(name="Cell")
CustomDocumentPropertiesCollection = Class(name="CustomDocumentPropertiesCollection")
SpreadsheetMLWorkbookProp_SmartTagType = Class(name="SpreadsheetMLWorkbookProp_SmartTagType")
SmartTagsCollection = Class(name="SmartTagsCollection")
SpreadsheetMLWorkbookProp_SmartTagsCollection = Class(name="SpreadsheetMLWorkbookProp_SmartTagsCollection")
Worksheet = Class(name="Worksheet")
SpreadsheetMLWorkbookProp_Worksheet = Class(name="SpreadsheetMLWorkbookProp_Worksheet")
SmartTagType = Class(name="SmartTagType")
SpreadsheetMLWorkbookProp_Workbook = Class(name="SpreadsheetMLWorkbookProp_Workbook")
DocumentPropertiesCollection = Class(name="DocumentPropertiesCollection")
ExcelWorkbook = Class(name="ExcelWorkbook")
Row = Class(name="Row")
Table = Class(name="Table")
SpreadsheetMLWorkbookProp_StyledElement = Class(name="SpreadsheetMLWorkbookProp_StyledElement", is_abstract=True)
SpreadsheetMLWorkbookProp_Table = Class(name="SpreadsheetMLWorkbookProp_Table")
StyledElement = Class(name="StyledElement")
Column = Class(name="Column")
SpreadsheetMLWorkbookProp_Column = Class(name="SpreadsheetMLWorkbookProp_Column")
ColOrRowElement = Class(name="ColOrRowElement")
SpreadsheetMLWorkbookProp_TableElement = Class(name="SpreadsheetMLWorkbookProp_TableElement", is_abstract=True)
SpreadsheetMLWorkbookProp_ColOrRowElement = Class(name="SpreadsheetMLWorkbookProp_ColOrRowElement", is_abstract=True)
TableElement = Class(name="TableElement")
SpreadsheetMLWorkbookProp_Row = Class(name="SpreadsheetMLWorkbookProp_Row")
SpreadsheetMLWorkbookProp_Cell = Class(name="SpreadsheetMLWorkbookProp_Cell")
SpreadsheetMLWorkbookProp_Data = Class(name="SpreadsheetMLWorkbookProp_Data")
Comment = Class(name="Comment")
SpreadsheetMLWorkbookProp_Comment = Class(name="SpreadsheetMLWorkbookProp_Comment")
SpreadsheetMLWorkbookProp_ExcelWorkbook = Class(name="SpreadsheetMLWorkbookProp_ExcelWorkbook")

# SpreadsheetMLWorkbookProp_DateTimeType class attributes and methods
SpreadsheetMLWorkbookProp_DateTimeType_hour: Property = Property(name="hour", type=StringType)
SpreadsheetMLWorkbookProp_DateTimeType_minute: Property = Property(name="minute", type=StringType)
SpreadsheetMLWorkbookProp_DateTimeType_year: Property = Property(name="year", type=StringType)
SpreadsheetMLWorkbookProp_DateTimeType_month: Property = Property(name="month", type=StringType)
SpreadsheetMLWorkbookProp_DateTimeType_day: Property = Property(name="day", type=StringType)
SpreadsheetMLWorkbookProp_DateTimeType_second: Property = Property(name="second", type=StringType)
SpreadsheetMLWorkbookProp_DateTimeType.attributes={SpreadsheetMLWorkbookProp_DateTimeType_hour, SpreadsheetMLWorkbookProp_DateTimeType_second, SpreadsheetMLWorkbookProp_DateTimeType_day, SpreadsheetMLWorkbookProp_DateTimeType_minute, SpreadsheetMLWorkbookProp_DateTimeType_month, SpreadsheetMLWorkbookProp_DateTimeType_year}

# SpreadsheetMLWorkbookProp_VersionType class attributes and methods
SpreadsheetMLWorkbookProp_VersionType_n: Property = Property(name="n", type=StringType)
SpreadsheetMLWorkbookProp_VersionType_nn: Property = Property(name="nn", type=StringType)
SpreadsheetMLWorkbookProp_VersionType.attributes={SpreadsheetMLWorkbookProp_VersionType_n, SpreadsheetMLWorkbookProp_VersionType_nn}

# SpreadsheetMLWorkbookProp_ValueType class attributes and methods

# Data class attributes and methods

# SpreadsheetMLWorkbookProp_StringValue class attributes and methods
SpreadsheetMLWorkbookProp_StringValue_value: Property = Property(name="value", type=StringType)
SpreadsheetMLWorkbookProp_StringValue.attributes={SpreadsheetMLWorkbookProp_StringValue_value}

# ValueType class attributes and methods

# SpreadsheetMLWorkbookProp_NumberValue class attributes and methods
SpreadsheetMLWorkbookProp_NumberValue_value: Property = Property(name="value", type=StringType)
SpreadsheetMLWorkbookProp_NumberValue.attributes={SpreadsheetMLWorkbookProp_NumberValue_value}

# SpreadsheetMLWorkbookProp_DateTimeTypeValue class attributes and methods

# DateTimeType class attributes and methods

# SpreadsheetMLWorkbookProp_BooleanValue class attributes and methods
SpreadsheetMLWorkbookProp_BooleanValue_value: Property = Property(name="value", type=StringType)
SpreadsheetMLWorkbookProp_BooleanValue.attributes={SpreadsheetMLWorkbookProp_BooleanValue_value}

# SpreadsheetMLWorkbookProp_ErrorValue class attributes and methods

# SpreadsheetMLWorkbookProp_DocumentPropertiesCollection class attributes and methods
SpreadsheetMLWorkbookProp_DocumentPropertiesCollection_keywords: Property = Property(name="keywords", type=StringType)
SpreadsheetMLWorkbookProp_DocumentPropertiesCollection_title: Property = Property(name="title", type=StringType)
SpreadsheetMLWorkbookProp_DocumentPropertiesCollection_subject: Property = Property(name="subject", type=StringType)
SpreadsheetMLWorkbookProp_DocumentPropertiesCollection_totalTime: Property = Property(name="totalTime", type=StringType)
SpreadsheetMLWorkbookProp_DocumentPropertiesCollection_description: Property = Property(name="description", type=StringType)
SpreadsheetMLWorkbookProp_DocumentPropertiesCollection_category: Property = Property(name="category", type=StringType)
SpreadsheetMLWorkbookProp_DocumentPropertiesCollection_author: Property = Property(name="author", type=StringType)
SpreadsheetMLWorkbookProp_DocumentPropertiesCollection_lastAuthor: Property = Property(name="lastAuthor", type=StringType)
SpreadsheetMLWorkbookProp_DocumentPropertiesCollection_manager: Property = Property(name="manager", type=StringType)
SpreadsheetMLWorkbookProp_DocumentPropertiesCollection_company: Property = Property(name="company", type=StringType)
SpreadsheetMLWorkbookProp_DocumentPropertiesCollection_hyperlinkBase: Property = Property(name="hyperlinkBase", type=StringType)
SpreadsheetMLWorkbookProp_DocumentPropertiesCollection_revision: Property = Property(name="revision", type=StringType)
SpreadsheetMLWorkbookProp_DocumentPropertiesCollection_presentationFormat: Property = Property(name="presentationFormat", type=StringType)
SpreadsheetMLWorkbookProp_DocumentPropertiesCollection_guid: Property = Property(name="guid", type=StringType)
SpreadsheetMLWorkbookProp_DocumentPropertiesCollection_appName: Property = Property(name="appName", type=StringType)
SpreadsheetMLWorkbookProp_DocumentPropertiesCollection_pages: Property = Property(name="pages", type=StringType)
SpreadsheetMLWorkbookProp_DocumentPropertiesCollection_words: Property = Property(name="words", type=StringType)
SpreadsheetMLWorkbookProp_DocumentPropertiesCollection_characters: Property = Property(name="characters", type=StringType)
SpreadsheetMLWorkbookProp_DocumentPropertiesCollection_charactersWithSpaces: Property = Property(name="charactersWithSpaces", type=StringType)
SpreadsheetMLWorkbookProp_DocumentPropertiesCollection_bytes: Property = Property(name="bytes", type=StringType)
SpreadsheetMLWorkbookProp_DocumentPropertiesCollection_lines: Property = Property(name="lines", type=StringType)
SpreadsheetMLWorkbookProp_DocumentPropertiesCollection_paragraphs: Property = Property(name="paragraphs", type=StringType)
SpreadsheetMLWorkbookProp_DocumentPropertiesCollection.attributes={SpreadsheetMLWorkbookProp_DocumentPropertiesCollection_totalTime, SpreadsheetMLWorkbookProp_DocumentPropertiesCollection_keywords, SpreadsheetMLWorkbookProp_DocumentPropertiesCollection_title, SpreadsheetMLWorkbookProp_DocumentPropertiesCollection_pages, SpreadsheetMLWorkbookProp_DocumentPropertiesCollection_lastAuthor, SpreadsheetMLWorkbookProp_DocumentPropertiesCollection_author, SpreadsheetMLWorkbookProp_DocumentPropertiesCollection_guid, SpreadsheetMLWorkbookProp_DocumentPropertiesCollection_hyperlinkBase, SpreadsheetMLWorkbookProp_DocumentPropertiesCollection_description, SpreadsheetMLWorkbookProp_DocumentPropertiesCollection_lines, SpreadsheetMLWorkbookProp_DocumentPropertiesCollection_paragraphs, SpreadsheetMLWorkbookProp_DocumentPropertiesCollection_charactersWithSpaces, SpreadsheetMLWorkbookProp_DocumentPropertiesCollection_words, SpreadsheetMLWorkbookProp_DocumentPropertiesCollection_appName, SpreadsheetMLWorkbookProp_DocumentPropertiesCollection_presentationFormat, SpreadsheetMLWorkbookProp_DocumentPropertiesCollection_manager, SpreadsheetMLWorkbookProp_DocumentPropertiesCollection_characters, SpreadsheetMLWorkbookProp_DocumentPropertiesCollection_bytes, SpreadsheetMLWorkbookProp_DocumentPropertiesCollection_company, SpreadsheetMLWorkbookProp_DocumentPropertiesCollection_revision, SpreadsheetMLWorkbookProp_DocumentPropertiesCollection_category, SpreadsheetMLWorkbookProp_DocumentPropertiesCollection_subject}

# Workbook class attributes and methods

# VersionType class attributes and methods

# CustomDocumentProperty class attributes and methods

# SpreadsheetMLWorkbookProp_CustomDocumentProperty class attributes and methods
SpreadsheetMLWorkbookProp_CustomDocumentProperty_name: Property = Property(name="name", type=StringType)
SpreadsheetMLWorkbookProp_CustomDocumentProperty.attributes={SpreadsheetMLWorkbookProp_CustomDocumentProperty_name}

# SpreadsheetMLWorkbookProp_CustomDocumentPropertiesCollection class attributes and methods

# Cell class attributes and methods

# CustomDocumentPropertiesCollection class attributes and methods

# SpreadsheetMLWorkbookProp_SmartTagType class attributes and methods
SpreadsheetMLWorkbookProp_SmartTagType_namespaceuri: Property = Property(name="namespaceuri", type=StringType)
SpreadsheetMLWorkbookProp_SmartTagType_name: Property = Property(name="name", type=StringType)
SpreadsheetMLWorkbookProp_SmartTagType_url: Property = Property(name="url", type=StringType)
SpreadsheetMLWorkbookProp_SmartTagType.attributes={SpreadsheetMLWorkbookProp_SmartTagType_url, SpreadsheetMLWorkbookProp_SmartTagType_namespaceuri, SpreadsheetMLWorkbookProp_SmartTagType_name}

# SmartTagsCollection class attributes and methods

# SpreadsheetMLWorkbookProp_SmartTagsCollection class attributes and methods

# Worksheet class attributes and methods

# SpreadsheetMLWorkbookProp_Worksheet class attributes and methods
SpreadsheetMLWorkbookProp_Worksheet_name: Property = Property(name="name", type=StringType)
SpreadsheetMLWorkbookProp_Worksheet.attributes={SpreadsheetMLWorkbookProp_Worksheet_name}

# SmartTagType class attributes and methods

# SpreadsheetMLWorkbookProp_Workbook class attributes and methods

# DocumentPropertiesCollection class attributes and methods

# ExcelWorkbook class attributes and methods

# Row class attributes and methods

# Table class attributes and methods

# SpreadsheetMLWorkbookProp_StyledElement class attributes and methods

# SpreadsheetMLWorkbookProp_Table class attributes and methods
SpreadsheetMLWorkbookProp_Table_defaultColumnWidth: Property = Property(name="defaultColumnWidth", type=StringType)
SpreadsheetMLWorkbookProp_Table_defaultRowHeight: Property = Property(name="defaultRowHeight", type=StringType)
SpreadsheetMLWorkbookProp_Table_expandedColumnCount: Property = Property(name="expandedColumnCount", type=StringType)
SpreadsheetMLWorkbookProp_Table_expandedRowCount: Property = Property(name="expandedRowCount", type=StringType)
SpreadsheetMLWorkbookProp_Table_leftCell: Property = Property(name="leftCell", type=StringType)
SpreadsheetMLWorkbookProp_Table_topCell: Property = Property(name="topCell", type=StringType)
SpreadsheetMLWorkbookProp_Table_fullColumns: Property = Property(name="fullColumns", type=StringType)
SpreadsheetMLWorkbookProp_Table_fullRows: Property = Property(name="fullRows", type=StringType)
SpreadsheetMLWorkbookProp_Table.attributes={SpreadsheetMLWorkbookProp_Table_fullColumns, SpreadsheetMLWorkbookProp_Table_fullRows, SpreadsheetMLWorkbookProp_Table_topCell, SpreadsheetMLWorkbookProp_Table_leftCell, SpreadsheetMLWorkbookProp_Table_defaultColumnWidth, SpreadsheetMLWorkbookProp_Table_expandedRowCount, SpreadsheetMLWorkbookProp_Table_defaultRowHeight, SpreadsheetMLWorkbookProp_Table_expandedColumnCount}

# StyledElement class attributes and methods

# Column class attributes and methods

# SpreadsheetMLWorkbookProp_Column class attributes and methods
SpreadsheetMLWorkbookProp_Column_autoFitWidth: Property = Property(name="autoFitWidth", type=StringType)
SpreadsheetMLWorkbookProp_Column_width: Property = Property(name="width", type=StringType)
SpreadsheetMLWorkbookProp_Column.attributes={SpreadsheetMLWorkbookProp_Column_autoFitWidth, SpreadsheetMLWorkbookProp_Column_width}

# ColOrRowElement class attributes and methods

# SpreadsheetMLWorkbookProp_TableElement class attributes and methods
SpreadsheetMLWorkbookProp_TableElement_index: Property = Property(name="index", type=StringType)
SpreadsheetMLWorkbookProp_TableElement.attributes={SpreadsheetMLWorkbookProp_TableElement_index}

# SpreadsheetMLWorkbookProp_ColOrRowElement class attributes and methods
SpreadsheetMLWorkbookProp_ColOrRowElement_span: Property = Property(name="span", type=StringType)
SpreadsheetMLWorkbookProp_ColOrRowElement_hidden: Property = Property(name="hidden", type=StringType)
SpreadsheetMLWorkbookProp_ColOrRowElement.attributes={SpreadsheetMLWorkbookProp_ColOrRowElement_span, SpreadsheetMLWorkbookProp_ColOrRowElement_hidden}

# TableElement class attributes and methods

# SpreadsheetMLWorkbookProp_Row class attributes and methods
SpreadsheetMLWorkbookProp_Row_autoFitHeight: Property = Property(name="autoFitHeight", type=StringType)
SpreadsheetMLWorkbookProp_Row_height: Property = Property(name="height", type=StringType)
SpreadsheetMLWorkbookProp_Row.attributes={SpreadsheetMLWorkbookProp_Row_autoFitHeight, SpreadsheetMLWorkbookProp_Row_height}

# SpreadsheetMLWorkbookProp_Cell class attributes and methods
SpreadsheetMLWorkbookProp_Cell_arrayRange: Property = Property(name="arrayRange", type=StringType)
SpreadsheetMLWorkbookProp_Cell_formula: Property = Property(name="formula", type=StringType)
SpreadsheetMLWorkbookProp_Cell_hRef: Property = Property(name="hRef", type=StringType)
SpreadsheetMLWorkbookProp_Cell_mergeAcross: Property = Property(name="mergeAcross", type=StringType)
SpreadsheetMLWorkbookProp_Cell_mergeDown: Property = Property(name="mergeDown", type=StringType)
SpreadsheetMLWorkbookProp_Cell.attributes={SpreadsheetMLWorkbookProp_Cell_hRef, SpreadsheetMLWorkbookProp_Cell_formula, SpreadsheetMLWorkbookProp_Cell_mergeDown, SpreadsheetMLWorkbookProp_Cell_arrayRange, SpreadsheetMLWorkbookProp_Cell_mergeAcross}

# SpreadsheetMLWorkbookProp_Data class attributes and methods

# Comment class attributes and methods

# SpreadsheetMLWorkbookProp_Comment class attributes and methods
SpreadsheetMLWorkbookProp_Comment_author: Property = Property(name="author", type=StringType)
SpreadsheetMLWorkbookProp_Comment_showAlways: Property = Property(name="showAlways", type=StringType)
SpreadsheetMLWorkbookProp_Comment.attributes={SpreadsheetMLWorkbookProp_Comment_showAlways, SpreadsheetMLWorkbookProp_Comment_author}

# SpreadsheetMLWorkbookProp_ExcelWorkbook class attributes and methods
SpreadsheetMLWorkbookProp_ExcelWorkbook_selectedSheets: Property = Property(name="selectedSheets", type=StringType)
SpreadsheetMLWorkbookProp_ExcelWorkbook_windowHidden: Property = Property(name="windowHidden", type=StringType)
SpreadsheetMLWorkbookProp_ExcelWorkbook_hideHorizontalScrollBar: Property = Property(name="hideHorizontalScrollBar", type=StringType)
SpreadsheetMLWorkbookProp_ExcelWorkbook_hideVerticalScrollBar: Property = Property(name="hideVerticalScrollBar", type=StringType)
SpreadsheetMLWorkbookProp_ExcelWorkbook_hideWorkbookTabs: Property = Property(name="hideWorkbookTabs", type=StringType)
SpreadsheetMLWorkbookProp_ExcelWorkbook_windowHeight: Property = Property(name="windowHeight", type=StringType)
SpreadsheetMLWorkbookProp_ExcelWorkbook_protectStructure: Property = Property(name="protectStructure", type=StringType)
SpreadsheetMLWorkbookProp_ExcelWorkbook_protectWindows: Property = Property(name="protectWindows", type=StringType)
SpreadsheetMLWorkbookProp_ExcelWorkbook_displayInkNotes: Property = Property(name="displayInkNotes", type=StringType)
SpreadsheetMLWorkbookProp_ExcelWorkbook_embedSaveSmartTags: Property = Property(name="embedSaveSmartTags", type=StringType)
SpreadsheetMLWorkbookProp_ExcelWorkbook_futureVer: Property = Property(name="futureVer", type=StringType)
SpreadsheetMLWorkbookProp_ExcelWorkbook_windowWidth: Property = Property(name="windowWidth", type=StringType)
SpreadsheetMLWorkbookProp_ExcelWorkbook_windowTopX: Property = Property(name="windowTopX", type=StringType)
SpreadsheetMLWorkbookProp_ExcelWorkbook_windowTopY: Property = Property(name="windowTopY", type=StringType)
SpreadsheetMLWorkbookProp_ExcelWorkbook_activeSheet: Property = Property(name="activeSheet", type=StringType)
SpreadsheetMLWorkbookProp_ExcelWorkbook_activeChart: Property = Property(name="activeChart", type=StringType)
SpreadsheetMLWorkbookProp_ExcelWorkbook_firstVisibleSheet: Property = Property(name="firstVisibleSheet", type=StringType)
SpreadsheetMLWorkbookProp_ExcelWorkbook_hidePivotTableFieldList: Property = Property(name="hidePivotTableFieldList", type=StringType)
SpreadsheetMLWorkbookProp_ExcelWorkbook_iteration: Property = Property(name="iteration", type=StringType)
SpreadsheetMLWorkbookProp_ExcelWorkbook_maxIterations: Property = Property(name="maxIterations", type=StringType)
SpreadsheetMLWorkbookProp_ExcelWorkbook_maxChange: Property = Property(name="maxChange", type=StringType)
SpreadsheetMLWorkbookProp_ExcelWorkbook_precisionAsDisplayed: Property = Property(name="precisionAsDisplayed", type=StringType)
SpreadsheetMLWorkbookProp_ExcelWorkbook_doNotSaveLinkValues: Property = Property(name="doNotSaveLinkValues", type=StringType)
SpreadsheetMLWorkbookProp_ExcelWorkbook_noAutoRecover: Property = Property(name="noAutoRecover", type=StringType)
SpreadsheetMLWorkbookProp_ExcelWorkbook_tabRatio: Property = Property(name="tabRatio", type=StringType)
SpreadsheetMLWorkbookProp_ExcelWorkbook_acceptLabelsInFormulas: Property = Property(name="acceptLabelsInFormulas", type=StringType)
SpreadsheetMLWorkbookProp_ExcelWorkbook_windowIconic: Property = Property(name="windowIconic", type=StringType)
SpreadsheetMLWorkbookProp_ExcelWorkbook_displayDrawingObjects: Property = Property(name="displayDrawingObjects", type=StringType)
SpreadsheetMLWorkbookProp_ExcelWorkbook_createBackup: Property = Property(name="createBackup", type=StringType)
SpreadsheetMLWorkbookProp_ExcelWorkbook_calculation: Property = Property(name="calculation", type=StringType)
SpreadsheetMLWorkbookProp_ExcelWorkbook_doNotCalculateBeforeSave: Property = Property(name="doNotCalculateBeforeSave", type=StringType)
SpreadsheetMLWorkbookProp_ExcelWorkbook_date1904: Property = Property(name="date1904", type=StringType)
SpreadsheetMLWorkbookProp_ExcelWorkbook_refModeR1C1: Property = Property(name="refModeR1C1", type=StringType)
SpreadsheetMLWorkbookProp_ExcelWorkbook_uncalced: Property = Property(name="uncalced", type=StringType)
SpreadsheetMLWorkbookProp_ExcelWorkbook.attributes={SpreadsheetMLWorkbookProp_ExcelWorkbook_hidePivotTableFieldList, SpreadsheetMLWorkbookProp_ExcelWorkbook_protectStructure, SpreadsheetMLWorkbookProp_ExcelWorkbook_calculation, SpreadsheetMLWorkbookProp_ExcelWorkbook_doNotSaveLinkValues, SpreadsheetMLWorkbookProp_ExcelWorkbook_refModeR1C1, SpreadsheetMLWorkbookProp_ExcelWorkbook_maxIterations, SpreadsheetMLWorkbookProp_ExcelWorkbook_windowHidden, SpreadsheetMLWorkbookProp_ExcelWorkbook_noAutoRecover, SpreadsheetMLWorkbookProp_ExcelWorkbook_date1904, SpreadsheetMLWorkbookProp_ExcelWorkbook_embedSaveSmartTags, SpreadsheetMLWorkbookProp_ExcelWorkbook_maxChange, SpreadsheetMLWorkbookProp_ExcelWorkbook_windowHeight, SpreadsheetMLWorkbookProp_ExcelWorkbook_windowIconic, SpreadsheetMLWorkbookProp_ExcelWorkbook_hideWorkbookTabs, SpreadsheetMLWorkbookProp_ExcelWorkbook_futureVer, SpreadsheetMLWorkbookProp_ExcelWorkbook_iteration, SpreadsheetMLWorkbookProp_ExcelWorkbook_selectedSheets, SpreadsheetMLWorkbookProp_ExcelWorkbook_acceptLabelsInFormulas, SpreadsheetMLWorkbookProp_ExcelWorkbook_firstVisibleSheet, SpreadsheetMLWorkbookProp_ExcelWorkbook_protectWindows, SpreadsheetMLWorkbookProp_ExcelWorkbook_precisionAsDisplayed, SpreadsheetMLWorkbookProp_ExcelWorkbook_createBackup, SpreadsheetMLWorkbookProp_ExcelWorkbook_hideVerticalScrollBar, SpreadsheetMLWorkbookProp_ExcelWorkbook_activeChart, SpreadsheetMLWorkbookProp_ExcelWorkbook_windowTopY, SpreadsheetMLWorkbookProp_ExcelWorkbook_doNotCalculateBeforeSave, SpreadsheetMLWorkbookProp_ExcelWorkbook_tabRatio, SpreadsheetMLWorkbookProp_ExcelWorkbook_hideHorizontalScrollBar, SpreadsheetMLWorkbookProp_ExcelWorkbook_activeSheet, SpreadsheetMLWorkbookProp_ExcelWorkbook_displayDrawingObjects, SpreadsheetMLWorkbookProp_ExcelWorkbook_uncalced, SpreadsheetMLWorkbookProp_ExcelWorkbook_windowWidth, SpreadsheetMLWorkbookProp_ExcelWorkbook_displayInkNotes, SpreadsheetMLWorkbookProp_ExcelWorkbook_windowTopX}

# Relationships
vt_data0: BinaryAssociation = BinaryAssociation(
    name="vt_data0",
    ends={
        Property(name="Data", type=SpreadsheetMLWorkbookProp_ValueType, multiplicity=Multiplicity(1, 1)),
        Property(name="value", type=Data, multiplicity=Multiplicity(1, 1))
    }
)
value1: BinaryAssociation = BinaryAssociation(
    name="value1",
    ends={
        Property(name="DateTimeType", type=SpreadsheetMLWorkbookProp_DateTimeTypeValue, multiplicity=Multiplicity(1, 1)),
        Property(name="SpreadsheetMLWorkbookProp_DateTimeTypeValue", type=DateTimeType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
dp_workbook2: BinaryAssociation = BinaryAssociation(
    name="dp_workbook2",
    ends={
        Property(name="Workbook", type=SpreadsheetMLWorkbookProp_DocumentPropertiesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="wb_docProperties", type=Workbook, multiplicity=Multiplicity(1, 1))
    }
)
lastPrinted4: BinaryAssociation = BinaryAssociation(
    name="lastPrinted4",
    ends={
        Property(name="DateTimeType6", type=SpreadsheetMLWorkbookProp_DocumentPropertiesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="SpreadsheetMLWorkbookProp_DocumentPropertiesCollection5", type=DateTimeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
version3: BinaryAssociation = BinaryAssociation(
    name="version3",
    ends={
        Property(name="VersionType", type=SpreadsheetMLWorkbookProp_DocumentPropertiesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="SpreadsheetMLWorkbookProp_DocumentPropertiesCollection", type=VersionType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lastSaved10: BinaryAssociation = BinaryAssociation(
    name="lastSaved10",
    ends={
        Property(name="DateTimeType12", type=SpreadsheetMLWorkbookProp_DocumentPropertiesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="SpreadsheetMLWorkbookProp_DocumentPropertiesCollection11", type=DateTimeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
created7: BinaryAssociation = BinaryAssociation(
    name="created7",
    ends={
        Property(name="DateTimeType9", type=SpreadsheetMLWorkbookProp_DocumentPropertiesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="SpreadsheetMLWorkbookProp_DocumentPropertiesCollection8", type=DateTimeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
customDocumentProperties15: BinaryAssociation = BinaryAssociation(
    name="customDocumentProperties15",
    ends={
        Property(name="CustomDocumentProperty", type=SpreadsheetMLWorkbookProp_CustomDocumentPropertiesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="customDocumentProperty_cdpe", type=CustomDocumentProperty, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
cdp_workbook13: BinaryAssociation = BinaryAssociation(
    name="cdp_workbook13",
    ends={
        Property(name="Workbook14", type=SpreadsheetMLWorkbookProp_CustomDocumentPropertiesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="wb_customDocProperties", type=Workbook, multiplicity=Multiplicity(1, 1))
    }
)
st_workbook19: BinaryAssociation = BinaryAssociation(
    name="st_workbook19",
    ends={
        Property(name="Workbook20", type=SpreadsheetMLWorkbookProp_SmartTagsCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="wb_smartTags", type=Workbook, multiplicity=Multiplicity(1, 1))
    }
)
customDocumentProperty_cdpe16: BinaryAssociation = BinaryAssociation(
    name="customDocumentProperty_cdpe16",
    ends={
        Property(name="CustomDocumentPropertiesCollection", type=SpreadsheetMLWorkbookProp_CustomDocumentProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="customDocumentProperties", type=CustomDocumentPropertiesCollection, multiplicity=Multiplicity(1, 1))
    }
)
value17: BinaryAssociation = BinaryAssociation(
    name="value17",
    ends={
        Property(name="ValueType", type=SpreadsheetMLWorkbookProp_CustomDocumentProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="SpreadsheetMLWorkbookProp_CustomDocumentProperty", type=ValueType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
smartTagType_ste18: BinaryAssociation = BinaryAssociation(
    name="smartTagType_ste18",
    ends={
        Property(name="SmartTagsCollection", type=SpreadsheetMLWorkbookProp_SmartTagType, multiplicity=Multiplicity(1, 1)),
        Property(name="smartTagTypes", type=SmartTagsCollection, multiplicity=Multiplicity(1, 1))
    }
)
wb_worksheets29: BinaryAssociation = BinaryAssociation(
    name="wb_worksheets29",
    ends={
        Property(name="Worksheet", type=SpreadsheetMLWorkbookProp_Workbook, multiplicity=Multiplicity(1, 1)),
        Property(name="ws_workbook", type=Worksheet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
st_cell21: BinaryAssociation = BinaryAssociation(
    name="st_cell21",
    ends={
        Property(name="Cell", type=SpreadsheetMLWorkbookProp_SmartTagsCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="c_smartTags", type=Cell, multiplicity=Multiplicity(1, 1))
    }
)
smartTagTypes22: BinaryAssociation = BinaryAssociation(
    name="smartTagTypes22",
    ends={
        Property(name="SmartTagType", type=SpreadsheetMLWorkbookProp_SmartTagsCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="smartTagType_ste", type=SmartTagType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
wb_smartTags23: BinaryAssociation = BinaryAssociation(
    name="wb_smartTags23",
    ends={
        Property(name="SmartTagsCollection24", type=SpreadsheetMLWorkbookProp_Workbook, multiplicity=Multiplicity(1, 1)),
        Property(name="st_workbook", type=SmartTagsCollection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
wb_docProperties25: BinaryAssociation = BinaryAssociation(
    name="wb_docProperties25",
    ends={
        Property(name="DocumentPropertiesCollection", type=SpreadsheetMLWorkbookProp_Workbook, multiplicity=Multiplicity(1, 1)),
        Property(name="dp_workbook", type=DocumentPropertiesCollection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
wb_customDocProperties26: BinaryAssociation = BinaryAssociation(
    name="wb_customDocProperties26",
    ends={
        Property(name="CustomDocumentPropertiesCollection27", type=SpreadsheetMLWorkbookProp_Workbook, multiplicity=Multiplicity(1, 1)),
        Property(name="cdp_workbook", type=CustomDocumentPropertiesCollection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
wb_excelWorkbook28: BinaryAssociation = BinaryAssociation(
    name="wb_excelWorkbook28",
    ends={
        Property(name="ExcelWorkbook", type=SpreadsheetMLWorkbookProp_Workbook, multiplicity=Multiplicity(1, 1)),
        Property(name="ew_workbook", type=ExcelWorkbook, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
t_rows36: BinaryAssociation = BinaryAssociation(
    name="t_rows36",
    ends={
        Property(name="Row", type=SpreadsheetMLWorkbookProp_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="r_table", type=Row, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ws_workbook30: BinaryAssociation = BinaryAssociation(
    name="ws_workbook30",
    ends={
        Property(name="Workbook31", type=SpreadsheetMLWorkbookProp_Worksheet, multiplicity=Multiplicity(1, 1)),
        Property(name="wb_worksheets", type=Workbook, multiplicity=Multiplicity(1, 1))
    }
)
ws_table32: BinaryAssociation = BinaryAssociation(
    name="ws_table32",
    ends={
        Property(name="Table", type=SpreadsheetMLWorkbookProp_Worksheet, multiplicity=Multiplicity(1, 1)),
        Property(name="t_worksheet", type=Table, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
t_worksheet33: BinaryAssociation = BinaryAssociation(
    name="t_worksheet33",
    ends={
        Property(name="Worksheet34", type=SpreadsheetMLWorkbookProp_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="ws_table", type=Worksheet, multiplicity=Multiplicity(1, 1))
    }
)
t_cols35: BinaryAssociation = BinaryAssociation(
    name="t_cols35",
    ends={
        Property(name="Column", type=SpreadsheetMLWorkbookProp_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="c_table", type=Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
c_table37: BinaryAssociation = BinaryAssociation(
    name="c_table37",
    ends={
        Property(name="Table38", type=SpreadsheetMLWorkbookProp_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="t_cols", type=Table, multiplicity=Multiplicity(1, 1))
    }
)
r_table39: BinaryAssociation = BinaryAssociation(
    name="r_table39",
    ends={
        Property(name="Table40", type=SpreadsheetMLWorkbookProp_Row, multiplicity=Multiplicity(1, 1)),
        Property(name="t_rows", type=Table, multiplicity=Multiplicity(1, 1))
    }
)
r_cells41: BinaryAssociation = BinaryAssociation(
    name="r_cells41",
    ends={
        Property(name="Cell42", type=SpreadsheetMLWorkbookProp_Row, multiplicity=Multiplicity(1, 1)),
        Property(name="c_row", type=Cell, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
c_row45: BinaryAssociation = BinaryAssociation(
    name="c_row45",
    ends={
        Property(name="Row46", type=SpreadsheetMLWorkbookProp_Cell, multiplicity=Multiplicity(1, 1)),
        Property(name="r_cells", type=Row, multiplicity=Multiplicity(1, 1))
    }
)
c_smartTags43: BinaryAssociation = BinaryAssociation(
    name="c_smartTags43",
    ends={
        Property(name="SmartTagsCollection44", type=SpreadsheetMLWorkbookProp_Cell, multiplicity=Multiplicity(1, 1)),
        Property(name="st_cell", type=SmartTagsCollection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
com_data52: BinaryAssociation = BinaryAssociation(
    name="com_data52",
    ends={
        Property(name="Data53", type=SpreadsheetMLWorkbookProp_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="d_comment", type=Data, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
d_cell54: BinaryAssociation = BinaryAssociation(
    name="d_cell54",
    ends={
        Property(name="Cell55", type=SpreadsheetMLWorkbookProp_Data, multiplicity=Multiplicity(1, 1)),
        Property(name="c_data", type=Cell, multiplicity=Multiplicity(1, 1))
    }
)
c_data47: BinaryAssociation = BinaryAssociation(
    name="c_data47",
    ends={
        Property(name="Data48", type=SpreadsheetMLWorkbookProp_Cell, multiplicity=Multiplicity(1, 1)),
        Property(name="d_cell", type=Data, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
c_comment49: BinaryAssociation = BinaryAssociation(
    name="c_comment49",
    ends={
        Property(name="Comment", type=SpreadsheetMLWorkbookProp_Cell, multiplicity=Multiplicity(1, 1)),
        Property(name="c_cell", type=Comment, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
c_cell50: BinaryAssociation = BinaryAssociation(
    name="c_cell50",
    ends={
        Property(name="Cell51", type=SpreadsheetMLWorkbookProp_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="c_comment", type=Cell, multiplicity=Multiplicity(1, 1))
    }
)
d_comment56: BinaryAssociation = BinaryAssociation(
    name="d_comment56",
    ends={
        Property(name="Comment57", type=SpreadsheetMLWorkbookProp_Data, multiplicity=Multiplicity(1, 1)),
        Property(name="com_data", type=Comment, multiplicity=Multiplicity(1, 1))
    }
)
value58: BinaryAssociation = BinaryAssociation(
    name="value58",
    ends={
        Property(name="ValueType59", type=SpreadsheetMLWorkbookProp_Data, multiplicity=Multiplicity(1, 1)),
        Property(name="vt_data", type=ValueType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ew_workbook60: BinaryAssociation = BinaryAssociation(
    name="ew_workbook60",
    ends={
        Property(name="Workbook61", type=SpreadsheetMLWorkbookProp_ExcelWorkbook, multiplicity=Multiplicity(1, 1)),
        Property(name="wb_excelWorkbook", type=Workbook, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_SpreadsheetMLWorkbookProp_NumberValue_ValueType = Generalization(general=ValueType, specific=SpreadsheetMLWorkbookProp_NumberValue)
gen_SpreadsheetMLWorkbookProp_StringValue_ValueType = Generalization(general=ValueType, specific=SpreadsheetMLWorkbookProp_StringValue)
gen_SpreadsheetMLWorkbookProp_DateTimeTypeValue_ValueType = Generalization(general=ValueType, specific=SpreadsheetMLWorkbookProp_DateTimeTypeValue)
gen_SpreadsheetMLWorkbookProp_BooleanValue_ValueType = Generalization(general=ValueType, specific=SpreadsheetMLWorkbookProp_BooleanValue)
gen_SpreadsheetMLWorkbookProp_ErrorValue_ValueType = Generalization(general=ValueType, specific=SpreadsheetMLWorkbookProp_ErrorValue)
gen_SpreadsheetMLWorkbookProp_Table_StyledElement = Generalization(general=StyledElement, specific=SpreadsheetMLWorkbookProp_Table)
gen_SpreadsheetMLWorkbookProp_Column_ColOrRowElement = Generalization(general=ColOrRowElement, specific=SpreadsheetMLWorkbookProp_Column)
gen_SpreadsheetMLWorkbookProp_TableElement_StyledElement = Generalization(general=StyledElement, specific=SpreadsheetMLWorkbookProp_TableElement)
gen_SpreadsheetMLWorkbookProp_ColOrRowElement_TableElement = Generalization(general=TableElement, specific=SpreadsheetMLWorkbookProp_ColOrRowElement)
gen_SpreadsheetMLWorkbookProp_Row_ColOrRowElement = Generalization(general=ColOrRowElement, specific=SpreadsheetMLWorkbookProp_Row)
gen_SpreadsheetMLWorkbookProp_Cell_TableElement = Generalization(general=TableElement, specific=SpreadsheetMLWorkbookProp_Cell)

# Domain Model
domain_model = DomainModel(
    name="SpreadsheetMLWorkbookProp",
    types={SpreadsheetMLWorkbookProp_DateTimeType, SpreadsheetMLWorkbookProp_VersionType, SpreadsheetMLWorkbookProp_ValueType, Data, SpreadsheetMLWorkbookProp_StringValue, ValueType, SpreadsheetMLWorkbookProp_NumberValue, SpreadsheetMLWorkbookProp_DateTimeTypeValue, DateTimeType, SpreadsheetMLWorkbookProp_BooleanValue, SpreadsheetMLWorkbookProp_ErrorValue, SpreadsheetMLWorkbookProp_DocumentPropertiesCollection, Workbook, VersionType, CustomDocumentProperty, SpreadsheetMLWorkbookProp_CustomDocumentProperty, SpreadsheetMLWorkbookProp_CustomDocumentPropertiesCollection, Cell, CustomDocumentPropertiesCollection, SpreadsheetMLWorkbookProp_SmartTagType, SmartTagsCollection, SpreadsheetMLWorkbookProp_SmartTagsCollection, Worksheet, SpreadsheetMLWorkbookProp_Worksheet, SmartTagType, SpreadsheetMLWorkbookProp_Workbook, DocumentPropertiesCollection, ExcelWorkbook, Row, Table, SpreadsheetMLWorkbookProp_StyledElement, SpreadsheetMLWorkbookProp_Table, StyledElement, Column, SpreadsheetMLWorkbookProp_Column, ColOrRowElement, SpreadsheetMLWorkbookProp_TableElement, SpreadsheetMLWorkbookProp_ColOrRowElement, TableElement, SpreadsheetMLWorkbookProp_Row, SpreadsheetMLWorkbookProp_Cell, SpreadsheetMLWorkbookProp_Data, Comment, SpreadsheetMLWorkbookProp_Comment, SpreadsheetMLWorkbookProp_ExcelWorkbook, DisplayDrawingObjectsType, CalculationWorkbookType},
    associations={vt_data0, value1, dp_workbook2, lastPrinted4, version3, lastSaved10, created7, customDocumentProperties15, cdp_workbook13, st_workbook19, customDocumentProperty_cdpe16, value17, smartTagType_ste18, wb_worksheets29, st_cell21, smartTagTypes22, wb_smartTags23, wb_docProperties25, wb_customDocProperties26, wb_excelWorkbook28, t_rows36, ws_workbook30, ws_table32, t_worksheet33, t_cols35, c_table37, r_table39, r_cells41, c_row45, c_smartTags43, com_data52, d_cell54, c_data47, c_comment49, c_cell50, d_comment56, value58, ew_workbook60},
    generalizations={gen_SpreadsheetMLWorkbookProp_NumberValue_ValueType, gen_SpreadsheetMLWorkbookProp_StringValue_ValueType, gen_SpreadsheetMLWorkbookProp_DateTimeTypeValue_ValueType, gen_SpreadsheetMLWorkbookProp_BooleanValue_ValueType, gen_SpreadsheetMLWorkbookProp_ErrorValue_ValueType, gen_SpreadsheetMLWorkbookProp_Table_StyledElement, gen_SpreadsheetMLWorkbookProp_Column_ColOrRowElement, gen_SpreadsheetMLWorkbookProp_TableElement_StyledElement, gen_SpreadsheetMLWorkbookProp_ColOrRowElement_TableElement, gen_SpreadsheetMLWorkbookProp_Row_ColOrRowElement, gen_SpreadsheetMLWorkbookProp_Cell_TableElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)