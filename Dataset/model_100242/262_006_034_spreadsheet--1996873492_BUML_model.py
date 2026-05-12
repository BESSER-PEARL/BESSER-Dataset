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
CellType: Enumeration = Enumeration(
    name="CellType",
    literals={
            EnumerationLiteral(name="CellTypeFormula"),
			EnumerationLiteral(name="CellTypeString"),
			EnumerationLiteral(name="CellTypeDate"),
			EnumerationLiteral(name="CellTypeNumeric")
    }
)

# Classes
spreadsheet_Sheet = Class(name="spreadsheet_Sheet")
spreadsheet_Spreadsheet = Class(name="spreadsheet_Spreadsheet", is_abstract=True)
spreadsheet_Cell = Class(name="spreadsheet_Cell")
spreadsheet_Row = Class(name="spreadsheet_Row")
spreadsheet_Column = Class(name="spreadsheet_Column")

# spreadsheet_Sheet class attributes and methods
spreadsheet_Sheet_SheetName: Property = Property(name="SheetName", type=StringType)
spreadsheet_Sheet_SheetIndex: Property = Property(name="SheetIndex", type=IntegerType)
spreadsheet_Sheet_m_getColumn: Method = Method(name="getColumn", parameters={Parameter(name='spreadsheet_columnindex', type=StringType)}, type=StringType)
spreadsheet_Sheet_m_getRow: Method = Method(name="getRow", parameters={Parameter(name='spreadsheet_rowindex', type=StringType)}, type=StringType)
spreadsheet_Sheet.attributes={spreadsheet_Sheet_SheetIndex, spreadsheet_Sheet_SheetName}
spreadsheet_Sheet.methods={spreadsheet_Sheet_m_getColumn, spreadsheet_Sheet_m_getRow}

# spreadsheet_Spreadsheet class attributes and methods
spreadsheet_Spreadsheet_FilePath: Property = Property(name="FilePath", type=StringType)
spreadsheet_Spreadsheet_Label: Property = Property(name="Label", type=StringType)
spreadsheet_Spreadsheet_m_getSheet: Method = Method(name="getSheet", parameters={Parameter(name='spreadsheet_sheetindex', type=StringType)}, type=StringType)
spreadsheet_Spreadsheet_m_readFile: Method = Method(name="readFile", parameters={})
spreadsheet_Spreadsheet_m_writeFile: Method = Method(name="writeFile", parameters={})
spreadsheet_Spreadsheet_m_getSheet: Method = Method(name="getSheet", parameters={Parameter(name='spreadsheet_sheetname', type=StringType)}, type=StringType)
spreadsheet_Spreadsheet.attributes={spreadsheet_Spreadsheet_Label, spreadsheet_Spreadsheet_FilePath}
spreadsheet_Spreadsheet.methods={spreadsheet_Spreadsheet_m_getSheet, spreadsheet_Spreadsheet_m_getSheet, spreadsheet_Spreadsheet_m_writeFile, spreadsheet_Spreadsheet_m_readFile}

# spreadsheet_Cell class attributes and methods
spreadsheet_Cell_ValueFormatted: Property = Property(name="ValueFormatted", type=StringType)
spreadsheet_Cell_CellType: Property = Property(name="CellType", type=StringType)
spreadsheet_Cell_DoubleValue: Property = Property(name="DoubleValue", type=FloatType)
spreadsheet_Cell_StringValue: Property = Property(name="StringValue", type=StringType)
spreadsheet_Cell.attributes={spreadsheet_Cell_CellType, spreadsheet_Cell_ValueFormatted, spreadsheet_Cell_StringValue, spreadsheet_Cell_DoubleValue}

# spreadsheet_Row class attributes and methods
spreadsheet_Row_RowIndex: Property = Property(name="RowIndex", type=IntegerType)
spreadsheet_Row_m_getCell: Method = Method(name="getCell", parameters={Parameter(name='spreadsheet_column', type=StringType)}, type=StringType)
spreadsheet_Row_m_getCell: Method = Method(name="getCell", parameters={Parameter(name='spreadsheet_columnindex', type=StringType)}, type=StringType)
spreadsheet_Row.attributes={spreadsheet_Row_RowIndex}
spreadsheet_Row.methods={spreadsheet_Row_m_getCell, spreadsheet_Row_m_getCell}

# spreadsheet_Column class attributes and methods
spreadsheet_Column_ColumnIndex: Property = Property(name="ColumnIndex", type=IntegerType)
spreadsheet_Column_m_getCell: Method = Method(name="getCell", parameters={Parameter(name='spreadsheet_rowindex', type=StringType)}, type=StringType)
spreadsheet_Column_m_getCell: Method = Method(name="getCell", parameters={Parameter(name='spreadsheet_row', type=StringType)}, type=StringType)
spreadsheet_Column.attributes={spreadsheet_Column_ColumnIndex}
spreadsheet_Column.methods={spreadsheet_Column_m_getCell, spreadsheet_Column_m_getCell}

# Relationships
Sheet0: BinaryAssociation = BinaryAssociation(
    name="Sheet0",
    ends={
        Property(name="Sheet", type=spreadsheet_Spreadsheet, multiplicity=Multiplicity(1, 1)),
        Property(name="Spreadsheet", type=spreadsheet_Sheet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Cell8: BinaryAssociation = BinaryAssociation(
    name="Cell8",
    ends={
        Property(name="Cell", type=spreadsheet_Row, multiplicity=Multiplicity(1, 1)),
        Property(name="Row9", type=spreadsheet_Cell, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Sheet10: BinaryAssociation = BinaryAssociation(
    name="Sheet10",
    ends={
        Property(name="Sheet12", type=spreadsheet_Row, multiplicity=Multiplicity(1, 1)),
        Property(name="Row11", type=spreadsheet_Sheet, multiplicity=Multiplicity(1, 1))
    }
)
Row1: BinaryAssociation = BinaryAssociation(
    name="Row1",
    ends={
        Property(name="Row", type=spreadsheet_Sheet, multiplicity=Multiplicity(1, 1)),
        Property(name="Sheet2", type=spreadsheet_Row, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Column3: BinaryAssociation = BinaryAssociation(
    name="Column3",
    ends={
        Property(name="Column", type=spreadsheet_Sheet, multiplicity=Multiplicity(1, 1)),
        Property(name="Sheet4", type=spreadsheet_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Spreadsheet5: BinaryAssociation = BinaryAssociation(
    name="Spreadsheet5",
    ends={
        Property(name="Spreadsheet7", type=spreadsheet_Sheet, multiplicity=Multiplicity(1, 1)),
        Property(name="Sheet6", type=spreadsheet_Spreadsheet, multiplicity=Multiplicity(0, 1))
    }
)
Row19: BinaryAssociation = BinaryAssociation(
    name="Row19",
    ends={
        Property(name="Row21", type=spreadsheet_Cell, multiplicity=Multiplicity(1, 1)),
        Property(name="Cell20", type=spreadsheet_Row, multiplicity=Multiplicity(1, 1))
    }
)
Cell13: BinaryAssociation = BinaryAssociation(
    name="Cell13",
    ends={
        Property(name="Cell15", type=spreadsheet_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="Column14", type=spreadsheet_Cell, multiplicity=Multiplicity(0, 9999))
    }
)
Sheet16: BinaryAssociation = BinaryAssociation(
    name="Sheet16",
    ends={
        Property(name="Sheet18", type=spreadsheet_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="Column17", type=spreadsheet_Sheet, multiplicity=Multiplicity(1, 1))
    }
)
Column22: BinaryAssociation = BinaryAssociation(
    name="Column22",
    ends={
        Property(name="Column24", type=spreadsheet_Cell, multiplicity=Multiplicity(1, 1)),
        Property(name="Cell23", type=spreadsheet_Column, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="spreadsheet",
    types={spreadsheet_Sheet, spreadsheet_Spreadsheet, spreadsheet_Cell, spreadsheet_Row, spreadsheet_Column, CellType},
    associations={Sheet0, Cell8, Sheet10, Row1, Column3, Spreadsheet5, Row19, Cell13, Sheet16, Column22},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)