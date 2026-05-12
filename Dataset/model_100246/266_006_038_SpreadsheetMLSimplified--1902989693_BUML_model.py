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
SpreadsheetMLSimplified_DateTimeType = Class(name="SpreadsheetMLSimplified_DateTimeType")
SpreadsheetMLSimplified_ValueType = Class(name="SpreadsheetMLSimplified_ValueType", is_abstract=True)
SpreadsheetMLSimplified_DateTimeTypeValue = Class(name="SpreadsheetMLSimplified_DateTimeTypeValue")
SpreadsheetMLSimplified_BooleanValue = Class(name="SpreadsheetMLSimplified_BooleanValue")
SpreadsheetMLSimplified_ErrorValue = Class(name="SpreadsheetMLSimplified_ErrorValue")
SpreadsheetMLSimplified_Workbook = Class(name="SpreadsheetMLSimplified_Workbook")
SpreadsheetMLSimplified_Worksheet = Class(name="SpreadsheetMLSimplified_Worksheet")
SpreadsheetMLSimplified_Data = Class(name="SpreadsheetMLSimplified_Data")
SpreadsheetMLSimplified_StringValue = Class(name="SpreadsheetMLSimplified_StringValue")
ValueType = Class(name="ValueType")
SpreadsheetMLSimplified_NumberValue = Class(name="SpreadsheetMLSimplified_NumberValue")
SpreadsheetMLSimplified_Column = Class(name="SpreadsheetMLSimplified_Column")
SpreadsheetMLSimplified_Row = Class(name="SpreadsheetMLSimplified_Row")
SpreadsheetMLSimplified_TableElement = Class(name="SpreadsheetMLSimplified_TableElement", is_abstract=True)
SpreadsheetMLSimplified_ColOrRowElement = Class(name="SpreadsheetMLSimplified_ColOrRowElement", is_abstract=True)
TableElement = Class(name="TableElement")
SpreadsheetMLSimplified_Table = Class(name="SpreadsheetMLSimplified_Table")
SpreadsheetMLSimplified_Cell = Class(name="SpreadsheetMLSimplified_Cell")
ColOrRowElement = Class(name="ColOrRowElement")

# SpreadsheetMLSimplified_DateTimeType class attributes and methods
SpreadsheetMLSimplified_DateTimeType_year: Property = Property(name="year", type=IntegerType)
SpreadsheetMLSimplified_DateTimeType_month: Property = Property(name="month", type=IntegerType)
SpreadsheetMLSimplified_DateTimeType_day: Property = Property(name="day", type=IntegerType)
SpreadsheetMLSimplified_DateTimeType_hour: Property = Property(name="hour", type=IntegerType)
SpreadsheetMLSimplified_DateTimeType_minute: Property = Property(name="minute", type=IntegerType)
SpreadsheetMLSimplified_DateTimeType_second: Property = Property(name="second", type=IntegerType)
SpreadsheetMLSimplified_DateTimeType.attributes={SpreadsheetMLSimplified_DateTimeType_hour, SpreadsheetMLSimplified_DateTimeType_second, SpreadsheetMLSimplified_DateTimeType_month, SpreadsheetMLSimplified_DateTimeType_day, SpreadsheetMLSimplified_DateTimeType_year, SpreadsheetMLSimplified_DateTimeType_minute}

# SpreadsheetMLSimplified_ValueType class attributes and methods

# SpreadsheetMLSimplified_DateTimeTypeValue class attributes and methods

# SpreadsheetMLSimplified_BooleanValue class attributes and methods
SpreadsheetMLSimplified_BooleanValue_value: Property = Property(name="value", type=BooleanType)
SpreadsheetMLSimplified_BooleanValue.attributes={SpreadsheetMLSimplified_BooleanValue_value}

# SpreadsheetMLSimplified_ErrorValue class attributes and methods

# SpreadsheetMLSimplified_Workbook class attributes and methods

# SpreadsheetMLSimplified_Worksheet class attributes and methods
SpreadsheetMLSimplified_Worksheet_name: Property = Property(name="name", type=StringType)
SpreadsheetMLSimplified_Worksheet.attributes={SpreadsheetMLSimplified_Worksheet_name}

# SpreadsheetMLSimplified_Data class attributes and methods

# SpreadsheetMLSimplified_StringValue class attributes and methods
SpreadsheetMLSimplified_StringValue_value: Property = Property(name="value", type=StringType)
SpreadsheetMLSimplified_StringValue.attributes={SpreadsheetMLSimplified_StringValue_value}

# ValueType class attributes and methods

# SpreadsheetMLSimplified_NumberValue class attributes and methods
SpreadsheetMLSimplified_NumberValue_value: Property = Property(name="value", type=FloatType)
SpreadsheetMLSimplified_NumberValue.attributes={SpreadsheetMLSimplified_NumberValue_value}

# SpreadsheetMLSimplified_Column class attributes and methods
SpreadsheetMLSimplified_Column_autoFitWidth: Property = Property(name="autoFitWidth", type=BooleanType)
SpreadsheetMLSimplified_Column_width: Property = Property(name="width", type=FloatType)
SpreadsheetMLSimplified_Column.attributes={SpreadsheetMLSimplified_Column_autoFitWidth, SpreadsheetMLSimplified_Column_width}

# SpreadsheetMLSimplified_Row class attributes and methods
SpreadsheetMLSimplified_Row_autoFitHeight: Property = Property(name="autoFitHeight", type=BooleanType)
SpreadsheetMLSimplified_Row_height: Property = Property(name="height", type=FloatType)
SpreadsheetMLSimplified_Row.attributes={SpreadsheetMLSimplified_Row_height, SpreadsheetMLSimplified_Row_autoFitHeight}

# SpreadsheetMLSimplified_TableElement class attributes and methods
SpreadsheetMLSimplified_TableElement_index: Property = Property(name="index", type=IntegerType)
SpreadsheetMLSimplified_TableElement.attributes={SpreadsheetMLSimplified_TableElement_index}

# SpreadsheetMLSimplified_ColOrRowElement class attributes and methods
SpreadsheetMLSimplified_ColOrRowElement_hidden: Property = Property(name="hidden", type=BooleanType)
SpreadsheetMLSimplified_ColOrRowElement_span: Property = Property(name="span", type=IntegerType)
SpreadsheetMLSimplified_ColOrRowElement.attributes={SpreadsheetMLSimplified_ColOrRowElement_hidden, SpreadsheetMLSimplified_ColOrRowElement_span}

# TableElement class attributes and methods

# SpreadsheetMLSimplified_Table class attributes and methods

# SpreadsheetMLSimplified_Cell class attributes and methods
SpreadsheetMLSimplified_Cell_arrayRange: Property = Property(name="arrayRange", type=StringType)
SpreadsheetMLSimplified_Cell_formula: Property = Property(name="formula", type=StringType)
SpreadsheetMLSimplified_Cell_hRef: Property = Property(name="hRef", type=StringType)
SpreadsheetMLSimplified_Cell_mergeAcross: Property = Property(name="mergeAcross", type=FloatType)
SpreadsheetMLSimplified_Cell_mergeDown: Property = Property(name="mergeDown", type=FloatType)
SpreadsheetMLSimplified_Cell.attributes={SpreadsheetMLSimplified_Cell_arrayRange, SpreadsheetMLSimplified_Cell_mergeAcross, SpreadsheetMLSimplified_Cell_formula, SpreadsheetMLSimplified_Cell_mergeDown, SpreadsheetMLSimplified_Cell_hRef}

# ColOrRowElement class attributes and methods

# Relationships
value1: BinaryAssociation = BinaryAssociation(
    name="value1",
    ends={
        Property(name="SpreadsheetMLSimplified_DateTimeType", type=SpreadsheetMLSimplified_DateTimeTypeValue, multiplicity=Multiplicity(1, 1)),
        Property(name="SpreadsheetMLSimplified_DateTimeTypeValue", type=SpreadsheetMLSimplified_DateTimeType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
wb_worksheets2: BinaryAssociation = BinaryAssociation(
    name="wb_worksheets2",
    ends={
        Property(name="Worksheet", type=SpreadsheetMLSimplified_Workbook, multiplicity=Multiplicity(1, 1)),
        Property(name="ws_workbook", type=SpreadsheetMLSimplified_Worksheet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
vt_data0: BinaryAssociation = BinaryAssociation(
    name="vt_data0",
    ends={
        Property(name="Data", type=SpreadsheetMLSimplified_ValueType, multiplicity=Multiplicity(1, 1)),
        Property(name="value", type=SpreadsheetMLSimplified_Data, multiplicity=Multiplicity(1, 1))
    }
)
t_worksheet5: BinaryAssociation = BinaryAssociation(
    name="t_worksheet5",
    ends={
        Property(name="Worksheet6", type=SpreadsheetMLSimplified_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="ws_table", type=SpreadsheetMLSimplified_Worksheet, multiplicity=Multiplicity(1, 1))
    }
)
t_cols7: BinaryAssociation = BinaryAssociation(
    name="t_cols7",
    ends={
        Property(name="Column", type=SpreadsheetMLSimplified_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="c_table", type=SpreadsheetMLSimplified_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
t_rows8: BinaryAssociation = BinaryAssociation(
    name="t_rows8",
    ends={
        Property(name="Row", type=SpreadsheetMLSimplified_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="r_table", type=SpreadsheetMLSimplified_Row, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ws_workbook3: BinaryAssociation = BinaryAssociation(
    name="ws_workbook3",
    ends={
        Property(name="Workbook", type=SpreadsheetMLSimplified_Worksheet, multiplicity=Multiplicity(1, 1)),
        Property(name="wb_worksheets", type=SpreadsheetMLSimplified_Workbook, multiplicity=Multiplicity(1, 1))
    }
)
ws_table4: BinaryAssociation = BinaryAssociation(
    name="ws_table4",
    ends={
        Property(name="Table", type=SpreadsheetMLSimplified_Worksheet, multiplicity=Multiplicity(1, 1)),
        Property(name="t_worksheet", type=SpreadsheetMLSimplified_Table, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
r_table11: BinaryAssociation = BinaryAssociation(
    name="r_table11",
    ends={
        Property(name="Table12", type=SpreadsheetMLSimplified_Row, multiplicity=Multiplicity(1, 1)),
        Property(name="t_rows", type=SpreadsheetMLSimplified_Table, multiplicity=Multiplicity(1, 1))
    }
)
r_cells13: BinaryAssociation = BinaryAssociation(
    name="r_cells13",
    ends={
        Property(name="Cell", type=SpreadsheetMLSimplified_Row, multiplicity=Multiplicity(1, 1)),
        Property(name="c_row", type=SpreadsheetMLSimplified_Cell, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
c_row14: BinaryAssociation = BinaryAssociation(
    name="c_row14",
    ends={
        Property(name="Row15", type=SpreadsheetMLSimplified_Cell, multiplicity=Multiplicity(1, 1)),
        Property(name="r_cells", type=SpreadsheetMLSimplified_Row, multiplicity=Multiplicity(1, 1))
    }
)
c_table9: BinaryAssociation = BinaryAssociation(
    name="c_table9",
    ends={
        Property(name="Table10", type=SpreadsheetMLSimplified_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="t_cols", type=SpreadsheetMLSimplified_Table, multiplicity=Multiplicity(1, 1))
    }
)
value20: BinaryAssociation = BinaryAssociation(
    name="value20",
    ends={
        Property(name="ValueType", type=SpreadsheetMLSimplified_Data, multiplicity=Multiplicity(1, 1)),
        Property(name="vt_data", type=SpreadsheetMLSimplified_ValueType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
c_data16: BinaryAssociation = BinaryAssociation(
    name="c_data16",
    ends={
        Property(name="Data17", type=SpreadsheetMLSimplified_Cell, multiplicity=Multiplicity(1, 1)),
        Property(name="d_cell", type=SpreadsheetMLSimplified_Data, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
d_cell18: BinaryAssociation = BinaryAssociation(
    name="d_cell18",
    ends={
        Property(name="Cell19", type=SpreadsheetMLSimplified_Data, multiplicity=Multiplicity(1, 1)),
        Property(name="c_data", type=SpreadsheetMLSimplified_Cell, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_SpreadsheetMLSimplified_DateTimeTypeValue_ValueType = Generalization(general=ValueType, specific=SpreadsheetMLSimplified_DateTimeTypeValue)
gen_SpreadsheetMLSimplified_BooleanValue_ValueType = Generalization(general=ValueType, specific=SpreadsheetMLSimplified_BooleanValue)
gen_SpreadsheetMLSimplified_ErrorValue_ValueType = Generalization(general=ValueType, specific=SpreadsheetMLSimplified_ErrorValue)
gen_SpreadsheetMLSimplified_StringValue_ValueType = Generalization(general=ValueType, specific=SpreadsheetMLSimplified_StringValue)
gen_SpreadsheetMLSimplified_NumberValue_ValueType = Generalization(general=ValueType, specific=SpreadsheetMLSimplified_NumberValue)
gen_SpreadsheetMLSimplified_ColOrRowElement_TableElement = Generalization(general=TableElement, specific=SpreadsheetMLSimplified_ColOrRowElement)
gen_SpreadsheetMLSimplified_Cell_TableElement = Generalization(general=TableElement, specific=SpreadsheetMLSimplified_Cell)
gen_SpreadsheetMLSimplified_Column_ColOrRowElement = Generalization(general=ColOrRowElement, specific=SpreadsheetMLSimplified_Column)
gen_SpreadsheetMLSimplified_Row_ColOrRowElement = Generalization(general=ColOrRowElement, specific=SpreadsheetMLSimplified_Row)

# Domain Model
domain_model = DomainModel(
    name="SpreadsheetMLSimplified",
    types={SpreadsheetMLSimplified_DateTimeType, SpreadsheetMLSimplified_ValueType, SpreadsheetMLSimplified_DateTimeTypeValue, SpreadsheetMLSimplified_BooleanValue, SpreadsheetMLSimplified_ErrorValue, SpreadsheetMLSimplified_Workbook, SpreadsheetMLSimplified_Worksheet, SpreadsheetMLSimplified_Data, SpreadsheetMLSimplified_StringValue, ValueType, SpreadsheetMLSimplified_NumberValue, SpreadsheetMLSimplified_Column, SpreadsheetMLSimplified_Row, SpreadsheetMLSimplified_TableElement, SpreadsheetMLSimplified_ColOrRowElement, TableElement, SpreadsheetMLSimplified_Table, SpreadsheetMLSimplified_Cell, ColOrRowElement},
    associations={value1, wb_worksheets2, vt_data0, t_worksheet5, t_cols7, t_rows8, ws_workbook3, ws_table4, r_table11, r_cells13, c_row14, c_table9, value20, c_data16, d_cell18},
    generalizations={gen_SpreadsheetMLSimplified_DateTimeTypeValue_ValueType, gen_SpreadsheetMLSimplified_BooleanValue_ValueType, gen_SpreadsheetMLSimplified_ErrorValue_ValueType, gen_SpreadsheetMLSimplified_StringValue_ValueType, gen_SpreadsheetMLSimplified_NumberValue_ValueType, gen_SpreadsheetMLSimplified_ColOrRowElement_TableElement, gen_SpreadsheetMLSimplified_Cell_TableElement, gen_SpreadsheetMLSimplified_Column_ColOrRowElement, gen_SpreadsheetMLSimplified_Row_ColOrRowElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)