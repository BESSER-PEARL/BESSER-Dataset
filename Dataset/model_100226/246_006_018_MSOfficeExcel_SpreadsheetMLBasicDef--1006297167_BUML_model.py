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
SpreadsheetMLBasicDef_DateTimeType = Class(name="SpreadsheetMLBasicDef_DateTimeType")
SpreadsheetMLBasicDef_ValueType = Class(name="SpreadsheetMLBasicDef_ValueType", is_abstract=True)
Data = Class(name="Data")
SpreadsheetMLBasicDef_StringValue = Class(name="SpreadsheetMLBasicDef_StringValue")
ValueType = Class(name="ValueType")
SpreadsheetMLBasicDef_VersionType = Class(name="SpreadsheetMLBasicDef_VersionType")
DateTimeType = Class(name="DateTimeType")
SpreadsheetMLBasicDef_BooleanValue = Class(name="SpreadsheetMLBasicDef_BooleanValue")
SpreadsheetMLBasicDef_ErrorValue = Class(name="SpreadsheetMLBasicDef_ErrorValue")
SpreadsheetMLBasicDef_DocumentPropertiesCollection = Class(name="SpreadsheetMLBasicDef_DocumentPropertiesCollection")
Workbook = Class(name="Workbook")
SpreadsheetMLBasicDef_NumberValue = Class(name="SpreadsheetMLBasicDef_NumberValue")
SpreadsheetMLBasicDef_DateTimeTypeValue = Class(name="SpreadsheetMLBasicDef_DateTimeTypeValue")
VersionType = Class(name="VersionType")
CustomDocumentProperty = Class(name="CustomDocumentProperty")
SpreadsheetMLBasicDef_CustomDocumentProperty = Class(name="SpreadsheetMLBasicDef_CustomDocumentProperty")
CustomDocumentPropertiesCollection = Class(name="CustomDocumentPropertiesCollection")
SpreadsheetMLBasicDef_CustomDocumentPropertiesCollection = Class(name="SpreadsheetMLBasicDef_CustomDocumentPropertiesCollection")
SpreadsheetMLBasicDef_SmartTagsCollection = Class(name="SpreadsheetMLBasicDef_SmartTagsCollection")
SpreadsheetMLBasicDef_SmartTagType = Class(name="SpreadsheetMLBasicDef_SmartTagType")
SmartTagsCollection = Class(name="SmartTagsCollection")
DocumentPropertiesCollection = Class(name="DocumentPropertiesCollection")
Worksheet = Class(name="Worksheet")
Cell = Class(name="Cell")
SmartTagType = Class(name="SmartTagType")
SpreadsheetMLBasicDef_Workbook = Class(name="SpreadsheetMLBasicDef_Workbook")
SpreadsheetMLBasicDef_StyledElement = Class(name="SpreadsheetMLBasicDef_StyledElement", is_abstract=True)
SpreadsheetMLBasicDef_Table = Class(name="SpreadsheetMLBasicDef_Table")
StyledElement = Class(name="StyledElement")
Column = Class(name="Column")
SpreadsheetMLBasicDef_Worksheet = Class(name="SpreadsheetMLBasicDef_Worksheet")
Table = Class(name="Table")
SpreadsheetMLBasicDef_TableElement = Class(name="SpreadsheetMLBasicDef_TableElement", is_abstract=True)
SpreadsheetMLBasicDef_ColOrRowElement = Class(name="SpreadsheetMLBasicDef_ColOrRowElement", is_abstract=True)
Row = Class(name="Row")
SpreadsheetMLBasicDef_Row = Class(name="SpreadsheetMLBasicDef_Row")
TableElement = Class(name="TableElement")
SpreadsheetMLBasicDef_Column = Class(name="SpreadsheetMLBasicDef_Column")
ColOrRowElement = Class(name="ColOrRowElement")
Comment = Class(name="Comment")
SpreadsheetMLBasicDef_Cell = Class(name="SpreadsheetMLBasicDef_Cell")
SpreadsheetMLBasicDef_Data = Class(name="SpreadsheetMLBasicDef_Data")
SpreadsheetMLBasicDef_Comment = Class(name="SpreadsheetMLBasicDef_Comment")

# SpreadsheetMLBasicDef_DateTimeType class attributes and methods
SpreadsheetMLBasicDef_DateTimeType_year: Property = Property(name="year", type=StringType)
SpreadsheetMLBasicDef_DateTimeType_month: Property = Property(name="month", type=StringType)
SpreadsheetMLBasicDef_DateTimeType_day: Property = Property(name="day", type=StringType)
SpreadsheetMLBasicDef_DateTimeType_hour: Property = Property(name="hour", type=StringType)
SpreadsheetMLBasicDef_DateTimeType_minute: Property = Property(name="minute", type=StringType)
SpreadsheetMLBasicDef_DateTimeType_second: Property = Property(name="second", type=StringType)
SpreadsheetMLBasicDef_DateTimeType.attributes={SpreadsheetMLBasicDef_DateTimeType_second, SpreadsheetMLBasicDef_DateTimeType_year, SpreadsheetMLBasicDef_DateTimeType_minute, SpreadsheetMLBasicDef_DateTimeType_month, SpreadsheetMLBasicDef_DateTimeType_hour, SpreadsheetMLBasicDef_DateTimeType_day}

# SpreadsheetMLBasicDef_ValueType class attributes and methods

# Data class attributes and methods

# SpreadsheetMLBasicDef_StringValue class attributes and methods
SpreadsheetMLBasicDef_StringValue_value: Property = Property(name="value", type=StringType)
SpreadsheetMLBasicDef_StringValue.attributes={SpreadsheetMLBasicDef_StringValue_value}

# ValueType class attributes and methods

# SpreadsheetMLBasicDef_VersionType class attributes and methods
SpreadsheetMLBasicDef_VersionType_n: Property = Property(name="n", type=StringType)
SpreadsheetMLBasicDef_VersionType_nn: Property = Property(name="nn", type=StringType)
SpreadsheetMLBasicDef_VersionType.attributes={SpreadsheetMLBasicDef_VersionType_n, SpreadsheetMLBasicDef_VersionType_nn}

# DateTimeType class attributes and methods

# SpreadsheetMLBasicDef_BooleanValue class attributes and methods
SpreadsheetMLBasicDef_BooleanValue_value: Property = Property(name="value", type=StringType)
SpreadsheetMLBasicDef_BooleanValue.attributes={SpreadsheetMLBasicDef_BooleanValue_value}

# SpreadsheetMLBasicDef_ErrorValue class attributes and methods

# SpreadsheetMLBasicDef_DocumentPropertiesCollection class attributes and methods
SpreadsheetMLBasicDef_DocumentPropertiesCollection_author: Property = Property(name="author", type=StringType)
SpreadsheetMLBasicDef_DocumentPropertiesCollection_lastAuthor: Property = Property(name="lastAuthor", type=StringType)
SpreadsheetMLBasicDef_DocumentPropertiesCollection_manager: Property = Property(name="manager", type=StringType)
SpreadsheetMLBasicDef_DocumentPropertiesCollection_company: Property = Property(name="company", type=StringType)
SpreadsheetMLBasicDef_DocumentPropertiesCollection_hyperlinkBase: Property = Property(name="hyperlinkBase", type=StringType)
SpreadsheetMLBasicDef_DocumentPropertiesCollection_revision: Property = Property(name="revision", type=StringType)
SpreadsheetMLBasicDef_DocumentPropertiesCollection_presentationFormat: Property = Property(name="presentationFormat", type=StringType)
SpreadsheetMLBasicDef_DocumentPropertiesCollection_guid: Property = Property(name="guid", type=StringType)
SpreadsheetMLBasicDef_DocumentPropertiesCollection_title: Property = Property(name="title", type=StringType)
SpreadsheetMLBasicDef_DocumentPropertiesCollection_subject: Property = Property(name="subject", type=StringType)
SpreadsheetMLBasicDef_DocumentPropertiesCollection_keywords: Property = Property(name="keywords", type=StringType)
SpreadsheetMLBasicDef_DocumentPropertiesCollection_description: Property = Property(name="description", type=StringType)
SpreadsheetMLBasicDef_DocumentPropertiesCollection_category: Property = Property(name="category", type=StringType)
SpreadsheetMLBasicDef_DocumentPropertiesCollection_pages: Property = Property(name="pages", type=StringType)
SpreadsheetMLBasicDef_DocumentPropertiesCollection_words: Property = Property(name="words", type=StringType)
SpreadsheetMLBasicDef_DocumentPropertiesCollection_characters: Property = Property(name="characters", type=StringType)
SpreadsheetMLBasicDef_DocumentPropertiesCollection_appName: Property = Property(name="appName", type=StringType)
SpreadsheetMLBasicDef_DocumentPropertiesCollection_totalTime: Property = Property(name="totalTime", type=StringType)
SpreadsheetMLBasicDef_DocumentPropertiesCollection_charactersWithSpaces: Property = Property(name="charactersWithSpaces", type=StringType)
SpreadsheetMLBasicDef_DocumentPropertiesCollection_bytes: Property = Property(name="bytes", type=StringType)
SpreadsheetMLBasicDef_DocumentPropertiesCollection_lines: Property = Property(name="lines", type=StringType)
SpreadsheetMLBasicDef_DocumentPropertiesCollection_paragraphs: Property = Property(name="paragraphs", type=StringType)
SpreadsheetMLBasicDef_DocumentPropertiesCollection.attributes={SpreadsheetMLBasicDef_DocumentPropertiesCollection_presentationFormat, SpreadsheetMLBasicDef_DocumentPropertiesCollection_company, SpreadsheetMLBasicDef_DocumentPropertiesCollection_lastAuthor, SpreadsheetMLBasicDef_DocumentPropertiesCollection_manager, SpreadsheetMLBasicDef_DocumentPropertiesCollection_description, SpreadsheetMLBasicDef_DocumentPropertiesCollection_author, SpreadsheetMLBasicDef_DocumentPropertiesCollection_keywords, SpreadsheetMLBasicDef_DocumentPropertiesCollection_appName, SpreadsheetMLBasicDef_DocumentPropertiesCollection_characters, SpreadsheetMLBasicDef_DocumentPropertiesCollection_paragraphs, SpreadsheetMLBasicDef_DocumentPropertiesCollection_subject, SpreadsheetMLBasicDef_DocumentPropertiesCollection_category, SpreadsheetMLBasicDef_DocumentPropertiesCollection_pages, SpreadsheetMLBasicDef_DocumentPropertiesCollection_lines, SpreadsheetMLBasicDef_DocumentPropertiesCollection_totalTime, SpreadsheetMLBasicDef_DocumentPropertiesCollection_bytes, SpreadsheetMLBasicDef_DocumentPropertiesCollection_hyperlinkBase, SpreadsheetMLBasicDef_DocumentPropertiesCollection_words, SpreadsheetMLBasicDef_DocumentPropertiesCollection_charactersWithSpaces, SpreadsheetMLBasicDef_DocumentPropertiesCollection_title, SpreadsheetMLBasicDef_DocumentPropertiesCollection_guid, SpreadsheetMLBasicDef_DocumentPropertiesCollection_revision}

# Workbook class attributes and methods

# SpreadsheetMLBasicDef_NumberValue class attributes and methods
SpreadsheetMLBasicDef_NumberValue_value: Property = Property(name="value", type=StringType)
SpreadsheetMLBasicDef_NumberValue.attributes={SpreadsheetMLBasicDef_NumberValue_value}

# SpreadsheetMLBasicDef_DateTimeTypeValue class attributes and methods

# VersionType class attributes and methods

# CustomDocumentProperty class attributes and methods

# SpreadsheetMLBasicDef_CustomDocumentProperty class attributes and methods
SpreadsheetMLBasicDef_CustomDocumentProperty_name: Property = Property(name="name", type=StringType)
SpreadsheetMLBasicDef_CustomDocumentProperty.attributes={SpreadsheetMLBasicDef_CustomDocumentProperty_name}

# CustomDocumentPropertiesCollection class attributes and methods

# SpreadsheetMLBasicDef_CustomDocumentPropertiesCollection class attributes and methods

# SpreadsheetMLBasicDef_SmartTagsCollection class attributes and methods

# SpreadsheetMLBasicDef_SmartTagType class attributes and methods
SpreadsheetMLBasicDef_SmartTagType_namespaceuri: Property = Property(name="namespaceuri", type=StringType)
SpreadsheetMLBasicDef_SmartTagType_name: Property = Property(name="name", type=StringType)
SpreadsheetMLBasicDef_SmartTagType_url: Property = Property(name="url", type=StringType)
SpreadsheetMLBasicDef_SmartTagType.attributes={SpreadsheetMLBasicDef_SmartTagType_url, SpreadsheetMLBasicDef_SmartTagType_namespaceuri, SpreadsheetMLBasicDef_SmartTagType_name}

# SmartTagsCollection class attributes and methods

# DocumentPropertiesCollection class attributes and methods

# Worksheet class attributes and methods

# Cell class attributes and methods

# SmartTagType class attributes and methods

# SpreadsheetMLBasicDef_Workbook class attributes and methods

# SpreadsheetMLBasicDef_StyledElement class attributes and methods

# SpreadsheetMLBasicDef_Table class attributes and methods
SpreadsheetMLBasicDef_Table_expandedRowCount: Property = Property(name="expandedRowCount", type=StringType)
SpreadsheetMLBasicDef_Table_leftCell: Property = Property(name="leftCell", type=StringType)
SpreadsheetMLBasicDef_Table_topCell: Property = Property(name="topCell", type=StringType)
SpreadsheetMLBasicDef_Table_fullColumns: Property = Property(name="fullColumns", type=StringType)
SpreadsheetMLBasicDef_Table_fullRows: Property = Property(name="fullRows", type=StringType)
SpreadsheetMLBasicDef_Table_defaultColumnWidth: Property = Property(name="defaultColumnWidth", type=StringType)
SpreadsheetMLBasicDef_Table_defaultRowHeight: Property = Property(name="defaultRowHeight", type=StringType)
SpreadsheetMLBasicDef_Table_expandedColumnCount: Property = Property(name="expandedColumnCount", type=StringType)
SpreadsheetMLBasicDef_Table.attributes={SpreadsheetMLBasicDef_Table_expandedColumnCount, SpreadsheetMLBasicDef_Table_expandedRowCount, SpreadsheetMLBasicDef_Table_defaultColumnWidth, SpreadsheetMLBasicDef_Table_leftCell, SpreadsheetMLBasicDef_Table_topCell, SpreadsheetMLBasicDef_Table_defaultRowHeight, SpreadsheetMLBasicDef_Table_fullRows, SpreadsheetMLBasicDef_Table_fullColumns}

# StyledElement class attributes and methods

# Column class attributes and methods

# SpreadsheetMLBasicDef_Worksheet class attributes and methods
SpreadsheetMLBasicDef_Worksheet_name: Property = Property(name="name", type=StringType)
SpreadsheetMLBasicDef_Worksheet.attributes={SpreadsheetMLBasicDef_Worksheet_name}

# Table class attributes and methods

# SpreadsheetMLBasicDef_TableElement class attributes and methods
SpreadsheetMLBasicDef_TableElement_index: Property = Property(name="index", type=StringType)
SpreadsheetMLBasicDef_TableElement.attributes={SpreadsheetMLBasicDef_TableElement_index}

# SpreadsheetMLBasicDef_ColOrRowElement class attributes and methods
SpreadsheetMLBasicDef_ColOrRowElement_hidden: Property = Property(name="hidden", type=StringType)
SpreadsheetMLBasicDef_ColOrRowElement_span: Property = Property(name="span", type=StringType)
SpreadsheetMLBasicDef_ColOrRowElement.attributes={SpreadsheetMLBasicDef_ColOrRowElement_span, SpreadsheetMLBasicDef_ColOrRowElement_hidden}

# Row class attributes and methods

# SpreadsheetMLBasicDef_Row class attributes and methods
SpreadsheetMLBasicDef_Row_autoFitHeight: Property = Property(name="autoFitHeight", type=StringType)
SpreadsheetMLBasicDef_Row_height: Property = Property(name="height", type=StringType)
SpreadsheetMLBasicDef_Row.attributes={SpreadsheetMLBasicDef_Row_height, SpreadsheetMLBasicDef_Row_autoFitHeight}

# TableElement class attributes and methods

# SpreadsheetMLBasicDef_Column class attributes and methods
SpreadsheetMLBasicDef_Column_autoFitWidth: Property = Property(name="autoFitWidth", type=StringType)
SpreadsheetMLBasicDef_Column_width: Property = Property(name="width", type=StringType)
SpreadsheetMLBasicDef_Column.attributes={SpreadsheetMLBasicDef_Column_autoFitWidth, SpreadsheetMLBasicDef_Column_width}

# ColOrRowElement class attributes and methods

# Comment class attributes and methods

# SpreadsheetMLBasicDef_Cell class attributes and methods
SpreadsheetMLBasicDef_Cell_arrayRange: Property = Property(name="arrayRange", type=StringType)
SpreadsheetMLBasicDef_Cell_formula: Property = Property(name="formula", type=StringType)
SpreadsheetMLBasicDef_Cell_hRef: Property = Property(name="hRef", type=StringType)
SpreadsheetMLBasicDef_Cell_mergeAcross: Property = Property(name="mergeAcross", type=StringType)
SpreadsheetMLBasicDef_Cell_mergeDown: Property = Property(name="mergeDown", type=StringType)
SpreadsheetMLBasicDef_Cell.attributes={SpreadsheetMLBasicDef_Cell_formula, SpreadsheetMLBasicDef_Cell_mergeAcross, SpreadsheetMLBasicDef_Cell_hRef, SpreadsheetMLBasicDef_Cell_arrayRange, SpreadsheetMLBasicDef_Cell_mergeDown}

# SpreadsheetMLBasicDef_Data class attributes and methods

# SpreadsheetMLBasicDef_Comment class attributes and methods
SpreadsheetMLBasicDef_Comment_author: Property = Property(name="author", type=StringType)
SpreadsheetMLBasicDef_Comment_showAlways: Property = Property(name="showAlways", type=StringType)
SpreadsheetMLBasicDef_Comment.attributes={SpreadsheetMLBasicDef_Comment_showAlways, SpreadsheetMLBasicDef_Comment_author}

# Relationships
vt_data0: BinaryAssociation = BinaryAssociation(
    name="vt_data0",
    ends={
        Property(name="Data", type=SpreadsheetMLBasicDef_ValueType, multiplicity=Multiplicity(1, 1)),
        Property(name="value", type=Data, multiplicity=Multiplicity(1, 1))
    }
)
value1: BinaryAssociation = BinaryAssociation(
    name="value1",
    ends={
        Property(name="DateTimeType", type=SpreadsheetMLBasicDef_DateTimeTypeValue, multiplicity=Multiplicity(1, 1)),
        Property(name="SpreadsheetMLBasicDef_DateTimeTypeValue", type=DateTimeType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
dp_workbook2: BinaryAssociation = BinaryAssociation(
    name="dp_workbook2",
    ends={
        Property(name="Workbook", type=SpreadsheetMLBasicDef_DocumentPropertiesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="wb_docProperties", type=Workbook, multiplicity=Multiplicity(1, 1))
    }
)
lastPrinted4: BinaryAssociation = BinaryAssociation(
    name="lastPrinted4",
    ends={
        Property(name="SpreadsheetMLBasicDef_DocumentPropertiesCollection5", type=DateTimeType, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="DateTimeType6", type=SpreadsheetMLBasicDef_DocumentPropertiesCollection, multiplicity=Multiplicity(1, 1))
    }
)
created7: BinaryAssociation = BinaryAssociation(
    name="created7",
    ends={
        Property(name="DateTimeType9", type=SpreadsheetMLBasicDef_DocumentPropertiesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="SpreadsheetMLBasicDef_DocumentPropertiesCollection8", type=DateTimeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lastSaved10: BinaryAssociation = BinaryAssociation(
    name="lastSaved10",
    ends={
        Property(name="DateTimeType12", type=SpreadsheetMLBasicDef_DocumentPropertiesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="SpreadsheetMLBasicDef_DocumentPropertiesCollection11", type=DateTimeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
version3: BinaryAssociation = BinaryAssociation(
    name="version3",
    ends={
        Property(name="VersionType", type=SpreadsheetMLBasicDef_DocumentPropertiesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="SpreadsheetMLBasicDef_DocumentPropertiesCollection", type=VersionType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cdp_workbook13: BinaryAssociation = BinaryAssociation(
    name="cdp_workbook13",
    ends={
        Property(name="Workbook14", type=SpreadsheetMLBasicDef_CustomDocumentPropertiesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="wb_customDocProperties", type=Workbook, multiplicity=Multiplicity(1, 1))
    }
)
customDocumentProperties15: BinaryAssociation = BinaryAssociation(
    name="customDocumentProperties15",
    ends={
        Property(name="CustomDocumentProperty", type=SpreadsheetMLBasicDef_CustomDocumentPropertiesCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="customDocumentProperty_cdpe", type=CustomDocumentProperty, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
customDocumentProperty_cdpe16: BinaryAssociation = BinaryAssociation(
    name="customDocumentProperty_cdpe16",
    ends={
        Property(name="CustomDocumentPropertiesCollection", type=SpreadsheetMLBasicDef_CustomDocumentProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="customDocumentProperties", type=CustomDocumentPropertiesCollection, multiplicity=Multiplicity(1, 1))
    }
)
st_workbook19: BinaryAssociation = BinaryAssociation(
    name="st_workbook19",
    ends={
        Property(name="Workbook20", type=SpreadsheetMLBasicDef_SmartTagsCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="wb_smartTags", type=Workbook, multiplicity=Multiplicity(1, 1))
    }
)
value17: BinaryAssociation = BinaryAssociation(
    name="value17",
    ends={
        Property(name="ValueType", type=SpreadsheetMLBasicDef_CustomDocumentProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="SpreadsheetMLBasicDef_CustomDocumentProperty", type=ValueType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
smartTagType_ste18: BinaryAssociation = BinaryAssociation(
    name="smartTagType_ste18",
    ends={
        Property(name="SmartTagsCollection", type=SpreadsheetMLBasicDef_SmartTagType, multiplicity=Multiplicity(1, 1)),
        Property(name="smartTagTypes", type=SmartTagsCollection, multiplicity=Multiplicity(1, 1))
    }
)
wb_smartTags23: BinaryAssociation = BinaryAssociation(
    name="wb_smartTags23",
    ends={
        Property(name="SmartTagsCollection24", type=SpreadsheetMLBasicDef_Workbook, multiplicity=Multiplicity(1, 1)),
        Property(name="st_workbook", type=SmartTagsCollection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
wb_docProperties25: BinaryAssociation = BinaryAssociation(
    name="wb_docProperties25",
    ends={
        Property(name="DocumentPropertiesCollection", type=SpreadsheetMLBasicDef_Workbook, multiplicity=Multiplicity(1, 1)),
        Property(name="dp_workbook", type=DocumentPropertiesCollection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
wb_customDocProperties26: BinaryAssociation = BinaryAssociation(
    name="wb_customDocProperties26",
    ends={
        Property(name="CustomDocumentPropertiesCollection27", type=SpreadsheetMLBasicDef_Workbook, multiplicity=Multiplicity(1, 1)),
        Property(name="cdp_workbook", type=CustomDocumentPropertiesCollection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
wb_worksheets28: BinaryAssociation = BinaryAssociation(
    name="wb_worksheets28",
    ends={
        Property(name="Worksheet", type=SpreadsheetMLBasicDef_Workbook, multiplicity=Multiplicity(1, 1)),
        Property(name="ws_workbook", type=Worksheet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
st_cell21: BinaryAssociation = BinaryAssociation(
    name="st_cell21",
    ends={
        Property(name="Cell", type=SpreadsheetMLBasicDef_SmartTagsCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="c_smartTags", type=Cell, multiplicity=Multiplicity(1, 1))
    }
)
smartTagTypes22: BinaryAssociation = BinaryAssociation(
    name="smartTagTypes22",
    ends={
        Property(name="SmartTagType", type=SpreadsheetMLBasicDef_SmartTagsCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="smartTagType_ste", type=SmartTagType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
t_worksheet32: BinaryAssociation = BinaryAssociation(
    name="t_worksheet32",
    ends={
        Property(name="Worksheet33", type=SpreadsheetMLBasicDef_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="ws_table", type=Worksheet, multiplicity=Multiplicity(1, 1))
    }
)
t_cols34: BinaryAssociation = BinaryAssociation(
    name="t_cols34",
    ends={
        Property(name="Column", type=SpreadsheetMLBasicDef_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="c_table", type=Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ws_workbook29: BinaryAssociation = BinaryAssociation(
    name="ws_workbook29",
    ends={
        Property(name="Workbook30", type=SpreadsheetMLBasicDef_Worksheet, multiplicity=Multiplicity(1, 1)),
        Property(name="wb_worksheets", type=Workbook, multiplicity=Multiplicity(1, 1))
    }
)
ws_table31: BinaryAssociation = BinaryAssociation(
    name="ws_table31",
    ends={
        Property(name="Table", type=SpreadsheetMLBasicDef_Worksheet, multiplicity=Multiplicity(1, 1)),
        Property(name="t_worksheet", type=Table, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
t_rows35: BinaryAssociation = BinaryAssociation(
    name="t_rows35",
    ends={
        Property(name="Row", type=SpreadsheetMLBasicDef_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="r_table", type=Row, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
c_table36: BinaryAssociation = BinaryAssociation(
    name="c_table36",
    ends={
        Property(name="Table37", type=SpreadsheetMLBasicDef_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="t_cols", type=Table, multiplicity=Multiplicity(1, 1))
    }
)
r_table38: BinaryAssociation = BinaryAssociation(
    name="r_table38",
    ends={
        Property(name="Table39", type=SpreadsheetMLBasicDef_Row, multiplicity=Multiplicity(1, 1)),
        Property(name="t_rows", type=Table, multiplicity=Multiplicity(1, 1))
    }
)
r_cells40: BinaryAssociation = BinaryAssociation(
    name="r_cells40",
    ends={
        Property(name="Cell41", type=SpreadsheetMLBasicDef_Row, multiplicity=Multiplicity(1, 1)),
        Property(name="c_row", type=Cell, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
c_smartTags44: BinaryAssociation = BinaryAssociation(
    name="c_smartTags44",
    ends={
        Property(name="SmartTagsCollection45", type=SpreadsheetMLBasicDef_Cell, multiplicity=Multiplicity(1, 1)),
        Property(name="st_cell", type=SmartTagsCollection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
c_data46: BinaryAssociation = BinaryAssociation(
    name="c_data46",
    ends={
        Property(name="Data47", type=SpreadsheetMLBasicDef_Cell, multiplicity=Multiplicity(1, 1)),
        Property(name="d_cell", type=Data, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
c_comment48: BinaryAssociation = BinaryAssociation(
    name="c_comment48",
    ends={
        Property(name="Comment", type=SpreadsheetMLBasicDef_Cell, multiplicity=Multiplicity(1, 1)),
        Property(name="c_cell", type=Comment, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
c_row42: BinaryAssociation = BinaryAssociation(
    name="c_row42",
    ends={
        Property(name="Row43", type=SpreadsheetMLBasicDef_Cell, multiplicity=Multiplicity(1, 1)),
        Property(name="r_cells", type=Row, multiplicity=Multiplicity(1, 1))
    }
)
c_cell49: BinaryAssociation = BinaryAssociation(
    name="c_cell49",
    ends={
        Property(name="Cell50", type=SpreadsheetMLBasicDef_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="c_comment", type=Cell, multiplicity=Multiplicity(1, 1))
    }
)
com_data51: BinaryAssociation = BinaryAssociation(
    name="com_data51",
    ends={
        Property(name="Data52", type=SpreadsheetMLBasicDef_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="d_comment", type=Data, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
d_cell53: BinaryAssociation = BinaryAssociation(
    name="d_cell53",
    ends={
        Property(name="Cell54", type=SpreadsheetMLBasicDef_Data, multiplicity=Multiplicity(1, 1)),
        Property(name="c_data", type=Cell, multiplicity=Multiplicity(1, 1))
    }
)
d_comment55: BinaryAssociation = BinaryAssociation(
    name="d_comment55",
    ends={
        Property(name="Comment56", type=SpreadsheetMLBasicDef_Data, multiplicity=Multiplicity(1, 1)),
        Property(name="com_data", type=Comment, multiplicity=Multiplicity(1, 1))
    }
)
value57: BinaryAssociation = BinaryAssociation(
    name="value57",
    ends={
        Property(name="ValueType58", type=SpreadsheetMLBasicDef_Data, multiplicity=Multiplicity(1, 1)),
        Property(name="vt_data", type=ValueType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_SpreadsheetMLBasicDef_StringValue_ValueType = Generalization(general=ValueType, specific=SpreadsheetMLBasicDef_StringValue)
gen_SpreadsheetMLBasicDef_BooleanValue_ValueType = Generalization(general=ValueType, specific=SpreadsheetMLBasicDef_BooleanValue)
gen_SpreadsheetMLBasicDef_ErrorValue_ValueType = Generalization(general=ValueType, specific=SpreadsheetMLBasicDef_ErrorValue)
gen_SpreadsheetMLBasicDef_NumberValue_ValueType = Generalization(general=ValueType, specific=SpreadsheetMLBasicDef_NumberValue)
gen_SpreadsheetMLBasicDef_DateTimeTypeValue_ValueType = Generalization(general=ValueType, specific=SpreadsheetMLBasicDef_DateTimeTypeValue)
gen_SpreadsheetMLBasicDef_Table_StyledElement = Generalization(general=StyledElement, specific=SpreadsheetMLBasicDef_Table)
gen_SpreadsheetMLBasicDef_TableElement_StyledElement = Generalization(general=StyledElement, specific=SpreadsheetMLBasicDef_TableElement)
gen_SpreadsheetMLBasicDef_Row_ColOrRowElement = Generalization(general=ColOrRowElement, specific=SpreadsheetMLBasicDef_Row)
gen_SpreadsheetMLBasicDef_ColOrRowElement_TableElement = Generalization(general=TableElement, specific=SpreadsheetMLBasicDef_ColOrRowElement)
gen_SpreadsheetMLBasicDef_Column_ColOrRowElement = Generalization(general=ColOrRowElement, specific=SpreadsheetMLBasicDef_Column)
gen_SpreadsheetMLBasicDef_Cell_TableElement = Generalization(general=TableElement, specific=SpreadsheetMLBasicDef_Cell)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={SpreadsheetMLBasicDef_DateTimeType, SpreadsheetMLBasicDef_ValueType, Data, SpreadsheetMLBasicDef_StringValue, ValueType, SpreadsheetMLBasicDef_VersionType, DateTimeType, SpreadsheetMLBasicDef_BooleanValue, SpreadsheetMLBasicDef_ErrorValue, SpreadsheetMLBasicDef_DocumentPropertiesCollection, Workbook, SpreadsheetMLBasicDef_NumberValue, SpreadsheetMLBasicDef_DateTimeTypeValue, VersionType, CustomDocumentProperty, SpreadsheetMLBasicDef_CustomDocumentProperty, CustomDocumentPropertiesCollection, SpreadsheetMLBasicDef_CustomDocumentPropertiesCollection, SpreadsheetMLBasicDef_SmartTagsCollection, SpreadsheetMLBasicDef_SmartTagType, SmartTagsCollection, DocumentPropertiesCollection, Worksheet, Cell, SmartTagType, SpreadsheetMLBasicDef_Workbook, SpreadsheetMLBasicDef_StyledElement, SpreadsheetMLBasicDef_Table, StyledElement, Column, SpreadsheetMLBasicDef_Worksheet, Table, SpreadsheetMLBasicDef_TableElement, SpreadsheetMLBasicDef_ColOrRowElement, Row, SpreadsheetMLBasicDef_Row, TableElement, SpreadsheetMLBasicDef_Column, ColOrRowElement, Comment, SpreadsheetMLBasicDef_Cell, SpreadsheetMLBasicDef_Data, SpreadsheetMLBasicDef_Comment},
    associations={vt_data0, value1, dp_workbook2, lastPrinted4, created7, lastSaved10, version3, cdp_workbook13, customDocumentProperties15, customDocumentProperty_cdpe16, st_workbook19, value17, smartTagType_ste18, wb_smartTags23, wb_docProperties25, wb_customDocProperties26, wb_worksheets28, st_cell21, smartTagTypes22, t_worksheet32, t_cols34, ws_workbook29, ws_table31, t_rows35, c_table36, r_table38, r_cells40, c_smartTags44, c_data46, c_comment48, c_row42, c_cell49, com_data51, d_cell53, d_comment55, value57},
    generalizations={gen_SpreadsheetMLBasicDef_StringValue_ValueType, gen_SpreadsheetMLBasicDef_BooleanValue_ValueType, gen_SpreadsheetMLBasicDef_ErrorValue_ValueType, gen_SpreadsheetMLBasicDef_NumberValue_ValueType, gen_SpreadsheetMLBasicDef_DateTimeTypeValue_ValueType, gen_SpreadsheetMLBasicDef_Table_StyledElement, gen_SpreadsheetMLBasicDef_TableElement_StyledElement, gen_SpreadsheetMLBasicDef_Row_ColOrRowElement, gen_SpreadsheetMLBasicDef_ColOrRowElement_TableElement, gen_SpreadsheetMLBasicDef_Column_ColOrRowElement, gen_SpreadsheetMLBasicDef_Cell_TableElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)