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
Workbook = Class(name="Workbook")
Worksheet = Class(name="Worksheet")
Table = Class(name="Table")
Column = Class(name="Column")
Row = Class(name="Row")
ColOrRowElement = Class(name="ColOrRowElement")
Cell = Class(name="Cell")
TableElement = Class(name="TableElement")
ErrorValue = Class(name="ErrorValue")
Data = Class(name="Data")
ValueType = Class(name="ValueType")
NumberValue = Class(name="NumberValue")
StringValue = Class(name="StringValue")
BooleanValue = Class(name="BooleanValue")

# Workbook class attributes and methods

# Worksheet class attributes and methods
Worksheet_name: Property = Property(name="name", type=StringType)
Worksheet.attributes={Worksheet_name}

# Table class attributes and methods

# Column class attributes and methods

# Row class attributes and methods

# ColOrRowElement class attributes and methods
ColOrRowElement_span: Property = Property(name="span", type=IntegerType)
ColOrRowElement_hidden: Property = Property(name="hidden", type=BooleanType)
ColOrRowElement.attributes={ColOrRowElement_hidden, ColOrRowElement_span}

# Cell class attributes and methods
Cell_formula: Property = Property(name="formula", type=StringType)
Cell.attributes={Cell_formula}

# TableElement class attributes and methods
TableElement_index: Property = Property(name="index", type=IntegerType)
TableElement.attributes={TableElement_index}

# ErrorValue class attributes and methods

# Data class attributes and methods

# ValueType class attributes and methods

# NumberValue class attributes and methods
NumberValue_value: Property = Property(name="value", type=FloatType)
NumberValue.attributes={NumberValue_value}

# StringValue class attributes and methods
StringValue_value: Property = Property(name="value", type=StringType)
StringValue.attributes={StringValue_value}

# BooleanValue class attributes and methods
BooleanValue_value: Property = Property(name="value", type=BooleanType)
BooleanValue.attributes={BooleanValue_value}

# Relationships
worksheets0: BinaryAssociation = BinaryAssociation(
    name="worksheets0",
    ends={
        Property(name="Workbook", type=Worksheet, multiplicity=Multiplicity(1, 9999), is_composite=True),
        Property(name="Worksheet", type=Workbook, multiplicity=Multiplicity(1, 1))
    }
)
rows5: BinaryAssociation = BinaryAssociation(
    name="rows5",
    ends={
        Property(name="Row", type=Table, multiplicity=Multiplicity(1, 1)),
        Property(name="Table6", type=Row, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
table1: BinaryAssociation = BinaryAssociation(
    name="table1",
    ends={
        Property(name="Table", type=Worksheet, multiplicity=Multiplicity(1, 1)),
        Property(name="Worksheet2", type=Table, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
columns3: BinaryAssociation = BinaryAssociation(
    name="columns3",
    ends={
        Property(name="Column", type=Table, multiplicity=Multiplicity(1, 1)),
        Property(name="Table4", type=Column, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
cells7: BinaryAssociation = BinaryAssociation(
    name="cells7",
    ends={
        Property(name="Cell", type=Row, multiplicity=Multiplicity(1, 1)),
        Property(name="Row8", type=Cell, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
data9: BinaryAssociation = BinaryAssociation(
    name="data9",
    ends={
        Property(name="Data", type=Cell, multiplicity=Multiplicity(1, 1)),
        Property(name="Cell10", type=Data, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value11: BinaryAssociation = BinaryAssociation(
    name="value11",
    ends={
        Property(name="ValueType", type=Data, multiplicity=Multiplicity(1, 1)),
        Property(name="Data12", type=ValueType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_Cell_TableElement = Generalization(general=TableElement, specific=Cell)
gen_Column_ColOrRowElement = Generalization(general=ColOrRowElement, specific=Column)
gen_Row_ColOrRowElement = Generalization(general=ColOrRowElement, specific=Row)
gen_ColOrRowElement_TableElement = Generalization(general=TableElement, specific=ColOrRowElement)
gen_ErrorValue_ValueType = Generalization(general=ValueType, specific=ErrorValue)
gen_NumberValue_ValueType = Generalization(general=ValueType, specific=NumberValue)
gen_StringValue_ValueType = Generalization(general=ValueType, specific=StringValue)
gen_BooleanValue_ValueType = Generalization(general=ValueType, specific=BooleanValue)

# Domain Model
domain_model = DomainModel(
    name="",
    types={Workbook, Worksheet, Table, Column, Row, ColOrRowElement, Cell, TableElement, ErrorValue, Data, ValueType, NumberValue, StringValue, BooleanValue},
    associations={worksheets0, rows5, table1, columns3, cells7, data9, value11},
    generalizations={gen_Cell_TableElement, gen_Column_ColOrRowElement, gen_Row_ColOrRowElement, gen_ColOrRowElement_TableElement, gen_ErrorValue_ValueType, gen_NumberValue_ValueType, gen_StringValue_ValueType, gen_BooleanValue_ValueType},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)