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
Excel_DateTimeType = Class(name="Excel_DateTimeType")
Excel_ValueType = Class(name="Excel_ValueType", is_abstract=True)
Data = Class(name="Data")
Excel_StringValue = Class(name="Excel_StringValue")
ValueType = Class(name="ValueType")
Excel_Worksheet = Class(name="Excel_Worksheet")
Workbook = Class(name="Workbook")
Excel_NumberValue = Class(name="Excel_NumberValue")
Excel_DateTimeTypeValue = Class(name="Excel_DateTimeTypeValue")
DateTimeType = Class(name="DateTimeType")
Excel_BooleanValue = Class(name="Excel_BooleanValue")
Excel_ErrorValue = Class(name="Excel_ErrorValue")
Excel_Workbook = Class(name="Excel_Workbook")
Worksheet = Class(name="Worksheet")
Excel_TableElement = Class(name="Excel_TableElement", is_abstract=True)
Table = Class(name="Table")
Excel_Table = Class(name="Excel_Table")
Column = Class(name="Column")
Row = Class(name="Row")
Excel_ColOrRowElement = Class(name="Excel_ColOrRowElement", is_abstract=True)
TableElement = Class(name="TableElement")
Excel_Column = Class(name="Excel_Column")
ColOrRowElement = Class(name="ColOrRowElement")
Excel_Row = Class(name="Excel_Row")
Cell = Class(name="Cell")
Excel_Cell = Class(name="Excel_Cell")
Excel_Data = Class(name="Excel_Data")

# Excel_DateTimeType class attributes and methods
Excel_DateTimeType_year: Property = Property(name="year", type=StringType)
Excel_DateTimeType_month: Property = Property(name="month", type=StringType)
Excel_DateTimeType_day: Property = Property(name="day", type=StringType)
Excel_DateTimeType_hour: Property = Property(name="hour", type=StringType)
Excel_DateTimeType_minute: Property = Property(name="minute", type=StringType)
Excel_DateTimeType_second: Property = Property(name="second", type=StringType)
Excel_DateTimeType.attributes={Excel_DateTimeType_month, Excel_DateTimeType_hour, Excel_DateTimeType_day, Excel_DateTimeType_minute, Excel_DateTimeType_year, Excel_DateTimeType_second}

# Excel_ValueType class attributes and methods

# Data class attributes and methods

# Excel_StringValue class attributes and methods
Excel_StringValue_value: Property = Property(name="value", type=StringType)
Excel_StringValue.attributes={Excel_StringValue_value}

# ValueType class attributes and methods

# Excel_Worksheet class attributes and methods
Excel_Worksheet_name: Property = Property(name="name", type=StringType)
Excel_Worksheet.attributes={Excel_Worksheet_name}

# Workbook class attributes and methods

# Excel_NumberValue class attributes and methods
Excel_NumberValue_value: Property = Property(name="value", type=StringType)
Excel_NumberValue.attributes={Excel_NumberValue_value}

# Excel_DateTimeTypeValue class attributes and methods

# DateTimeType class attributes and methods

# Excel_BooleanValue class attributes and methods
Excel_BooleanValue_value: Property = Property(name="value", type=StringType)
Excel_BooleanValue.attributes={Excel_BooleanValue_value}

# Excel_ErrorValue class attributes and methods

# Excel_Workbook class attributes and methods

# Worksheet class attributes and methods

# Excel_TableElement class attributes and methods
Excel_TableElement_index: Property = Property(name="index", type=StringType)
Excel_TableElement.attributes={Excel_TableElement_index}

# Table class attributes and methods

# Excel_Table class attributes and methods

# Column class attributes and methods

# Row class attributes and methods

# Excel_ColOrRowElement class attributes and methods
Excel_ColOrRowElement_hidden: Property = Property(name="hidden", type=StringType)
Excel_ColOrRowElement_span: Property = Property(name="span", type=StringType)
Excel_ColOrRowElement.attributes={Excel_ColOrRowElement_span, Excel_ColOrRowElement_hidden}

# TableElement class attributes and methods

# Excel_Column class attributes and methods
Excel_Column_autoFitWidth: Property = Property(name="autoFitWidth", type=StringType)
Excel_Column_width: Property = Property(name="width", type=StringType)
Excel_Column.attributes={Excel_Column_autoFitWidth, Excel_Column_width}

# ColOrRowElement class attributes and methods

# Excel_Row class attributes and methods
Excel_Row_autoFitHeight: Property = Property(name="autoFitHeight", type=StringType)
Excel_Row_height: Property = Property(name="height", type=StringType)
Excel_Row.attributes={Excel_Row_height, Excel_Row_autoFitHeight}

# Cell class attributes and methods

# Excel_Cell class attributes and methods
Excel_Cell_arrayRange: Property = Property(name="arrayRange", type=StringType)
Excel_Cell_formula: Property = Property(name="formula", type=StringType)
Excel_Cell_hRef: Property = Property(name="hRef", type=StringType)
Excel_Cell_mergeAcross: Property = Property(name="mergeAcross", type=StringType)
Excel_Cell_mergeDown: Property = Property(name="mergeDown", type=StringType)
Excel_Cell.attributes={Excel_Cell_hRef, Excel_Cell_formula, Excel_Cell_arrayRange, Excel_Cell_mergeAcross, Excel_Cell_mergeDown}

# Excel_Data class attributes and methods

# Relationships
vt_data0: BinaryAssociation = BinaryAssociation(
    name="vt_data0",
    ends={
        Property(name="Data", type=Excel_ValueType, multiplicity=Multiplicity(1, 1)),
        Property(name="value", type=Data, multiplicity=Multiplicity(1, 1))
    }
)
value1: BinaryAssociation = BinaryAssociation(
    name="value1",
    ends={
        Property(name="DateTimeType", type=Excel_DateTimeTypeValue, multiplicity=Multiplicity(1, 1)),
        Property(name="Excel_DateTimeTypeValue", type=DateTimeType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
wb_worksheets2: BinaryAssociation = BinaryAssociation(
    name="wb_worksheets2",
    ends={
        Property(name="Worksheet", type=Excel_Workbook, multiplicity=Multiplicity(1, 1)),
        Property(name="ws_workbook", type=Worksheet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ws_workbook3: BinaryAssociation = BinaryAssociation(
    name="ws_workbook3",
    ends={
        Property(name="Workbook", type=Excel_Worksheet, multiplicity=Multiplicity(1, 1)),
        Property(name="wb_worksheets", type=Workbook, multiplicity=Multiplicity(1, 1))
    }
)
ws_table4: BinaryAssociation = BinaryAssociation(
    name="ws_table4",
    ends={
        Property(name="Table", type=Excel_Worksheet, multiplicity=Multiplicity(1, 1)),
        Property(name="t_worksheet", type=Table, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
t_worksheet5: BinaryAssociation = BinaryAssociation(
    name="t_worksheet5",
    ends={
        Property(name="Worksheet6", type=Excel_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="ws_table", type=Worksheet, multiplicity=Multiplicity(1, 1))
    }
)
t_cols7: BinaryAssociation = BinaryAssociation(
    name="t_cols7",
    ends={
        Property(name="Column", type=Excel_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="c_table", type=Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
t_rows8: BinaryAssociation = BinaryAssociation(
    name="t_rows8",
    ends={
        Property(name="Row", type=Excel_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="r_table", type=Row, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
r_table11: BinaryAssociation = BinaryAssociation(
    name="r_table11",
    ends={
        Property(name="t_rows", type=Table, multiplicity=Multiplicity(1, 1)),
        Property(name="Table12", type=Excel_Row, multiplicity=Multiplicity(1, 1))
    }
)
c_table9: BinaryAssociation = BinaryAssociation(
    name="c_table9",
    ends={
        Property(name="Table10", type=Excel_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="t_cols", type=Table, multiplicity=Multiplicity(1, 1))
    }
)
c_data16: BinaryAssociation = BinaryAssociation(
    name="c_data16",
    ends={
        Property(name="Data17", type=Excel_Cell, multiplicity=Multiplicity(1, 1)),
        Property(name="d_cell", type=Data, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
r_cells13: BinaryAssociation = BinaryAssociation(
    name="r_cells13",
    ends={
        Property(name="Cell", type=Excel_Row, multiplicity=Multiplicity(1, 1)),
        Property(name="c_row", type=Cell, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
c_row14: BinaryAssociation = BinaryAssociation(
    name="c_row14",
    ends={
        Property(name="Row15", type=Excel_Cell, multiplicity=Multiplicity(1, 1)),
        Property(name="r_cells", type=Row, multiplicity=Multiplicity(1, 1))
    }
)
d_cell18: BinaryAssociation = BinaryAssociation(
    name="d_cell18",
    ends={
        Property(name="Cell19", type=Excel_Data, multiplicity=Multiplicity(1, 1)),
        Property(name="c_data", type=Cell, multiplicity=Multiplicity(1, 1))
    }
)
value20: BinaryAssociation = BinaryAssociation(
    name="value20",
    ends={
        Property(name="ValueType", type=Excel_Data, multiplicity=Multiplicity(1, 1)),
        Property(name="vt_data", type=ValueType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_Excel_StringValue_ValueType = Generalization(general=ValueType, specific=Excel_StringValue)
gen_Excel_NumberValue_ValueType = Generalization(general=ValueType, specific=Excel_NumberValue)
gen_Excel_DateTimeTypeValue_ValueType = Generalization(general=ValueType, specific=Excel_DateTimeTypeValue)
gen_Excel_BooleanValue_ValueType = Generalization(general=ValueType, specific=Excel_BooleanValue)
gen_Excel_ErrorValue_ValueType = Generalization(general=ValueType, specific=Excel_ErrorValue)
gen_Excel_ColOrRowElement_TableElement = Generalization(general=TableElement, specific=Excel_ColOrRowElement)
gen_Excel_Column_ColOrRowElement = Generalization(general=ColOrRowElement, specific=Excel_Column)
gen_Excel_Row_ColOrRowElement = Generalization(general=ColOrRowElement, specific=Excel_Row)
gen_Excel_Cell_TableElement = Generalization(general=TableElement, specific=Excel_Cell)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={Excel_DateTimeType, Excel_ValueType, Data, Excel_StringValue, ValueType, Excel_Worksheet, Workbook, Excel_NumberValue, Excel_DateTimeTypeValue, DateTimeType, Excel_BooleanValue, Excel_ErrorValue, Excel_Workbook, Worksheet, Excel_TableElement, Table, Excel_Table, Column, Row, Excel_ColOrRowElement, TableElement, Excel_Column, ColOrRowElement, Excel_Row, Cell, Excel_Cell, Excel_Data},
    associations={vt_data0, value1, wb_worksheets2, ws_workbook3, ws_table4, t_worksheet5, t_cols7, t_rows8, r_table11, c_table9, c_data16, r_cells13, c_row14, d_cell18, value20},
    generalizations={gen_Excel_StringValue_ValueType, gen_Excel_NumberValue_ValueType, gen_Excel_DateTimeTypeValue_ValueType, gen_Excel_BooleanValue_ValueType, gen_Excel_ErrorValue_ValueType, gen_Excel_ColOrRowElement_TableElement, gen_Excel_Column_ColOrRowElement, gen_Excel_Row_ColOrRowElement, gen_Excel_Cell_TableElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)