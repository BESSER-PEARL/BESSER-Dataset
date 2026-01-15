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
cellsheet_EStringToTokenEntry = Class(name="cellsheet::EStringToTokenEntry")
cellsheet_Token = Class(name="cellsheet::Token")
cellsheet_HasA1 = Class(name="cellsheet::HasA1", is_abstract=True)
cellsheet_HasId = Class(name="cellsheet::HasId", is_abstract=True)
cellsheet_Workspace = Class(name="cellsheet::Workspace")
cellsheet_Book = Class(name="cellsheet::Book")
HasId = Class(name="HasId")
HasA1 = Class(name="HasA1")
cellsheet_CellFormat = Class(name="cellsheet::CellFormat")
cellsheet_Sheet = Class(name="cellsheet::Sheet")
cellsheet_Row = Class(name="cellsheet::Row")
cellsheet_Cell = Class(name="cellsheet::Cell", is_abstract=True)
cellsheet_Ast = Class(name="cellsheet::Ast", is_abstract=True)
cellsheet_BlankCell = Class(name="cellsheet::BlankCell")
Cell = Class(name="Cell")
cellsheet_TextCell = Class(name="cellsheet::TextCell")
cellsheet_NumericCell = Class(name="cellsheet::NumericCell")
cellsheet_BooleanCell = Class(name="cellsheet::BooleanCell")
cellsheet_DateCell = Class(name="cellsheet::DateCell")
cellsheet_FormulaCell = Class(name="cellsheet::FormulaCell")
cellsheet_AstEval = Class(name="cellsheet::AstEval")
cellsheet_Range = Class(name="cellsheet::Range")
cellsheet_Operand = Class(name="cellsheet::Operand", is_abstract=True)
Ast = Class(name="Ast")
cellsheet_Operation = Class(name="cellsheet::Operation", is_abstract=True)
cellsheet_PrefixOperator = Class(name="cellsheet::PrefixOperator", is_abstract=True)
cellsheet_InfixOperator = Class(name="cellsheet::InfixOperator", is_abstract=True)
cellsheet_PostfixOperator = Class(name="cellsheet::PostfixOperator", is_abstract=True)
cellsheet_Unknown = Class(name="cellsheet::Unknown")
cellsheet_Noop = Class(name="cellsheet::Noop")
cellsheet_Text = Class(name="cellsheet::Text")
Operand = Class(name="Operand")
cellsheet_Number = Class(name="cellsheet::Number")
cellsheet_Logical = Class(name="cellsheet::Logical")
cellsheet_Error = Class(name="cellsheet::Error")
cellsheet_Ref = Class(name="cellsheet::Ref")
cellsheet_RelativeRef = Class(name="cellsheet::RelativeRef")
Ref = Class(name="Ref")
cellsheet_RelativeRange = Class(name="cellsheet::RelativeRange")
cellsheet_Function = Class(name="cellsheet::Function")
Operation = Class(name="Operation")
cellsheet_Plus = Class(name="cellsheet::Plus")
PrefixOperator = Class(name="PrefixOperator")
cellsheet_Negation = Class(name="cellsheet::Negation")
cellsheet_Percent = Class(name="cellsheet::Percent")
PostfixOperator = Class(name="PostfixOperator")
cellsheet_Exponentiation = Class(name="cellsheet::Exponentiation")
InfixOperator = Class(name="InfixOperator")
cellsheet_Multiplication = Class(name="cellsheet::Multiplication")
cellsheet_Division = Class(name="cellsheet::Division")
cellsheet_Addition = Class(name="cellsheet::Addition")
cellsheet_Subtraction = Class(name="cellsheet::Subtraction")
cellsheet_Concatenation = Class(name="cellsheet::Concatenation")
cellsheet_EQ = Class(name="cellsheet::EQ")
cellsheet_LT = Class(name="cellsheet::LT")
cellsheet_GT = Class(name="cellsheet::GT")
cellsheet_LTE = Class(name="cellsheet::LTE")
cellsheet_GTE = Class(name="cellsheet::GTE")
cellsheet_NEQ = Class(name="cellsheet::NEQ")
cellsheet_Intersection = Class(name="cellsheet::Intersection")
cellsheet_Union = Class(name="cellsheet::Union")

# cellsheet_EStringToTokenEntry class attributes and methods
cellsheet_EStringToTokenEntry_key: Property = Property(name="key", type=StringType)
cellsheet_EStringToTokenEntry.attributes={cellsheet_EStringToTokenEntry_key}

# cellsheet_Token class attributes and methods
cellsheet_Token_value: Property = Property(name="value", type=StringType)
cellsheet_Token.attributes={cellsheet_Token_value}

# cellsheet_HasA1 class attributes and methods
cellsheet_HasA1_a1: Property = Property(name="a1", type=StringType)
cellsheet_HasA1.attributes={cellsheet_HasA1_a1}

# cellsheet_HasId class attributes and methods
cellsheet_HasId_id: Property = Property(name="id", type=StringType)
cellsheet_HasId.attributes={cellsheet_HasId_id}

# cellsheet_Workspace class attributes and methods

# cellsheet_Book class attributes and methods
cellsheet_Book_bookname: Property = Property(name="bookname", type=StringType)
cellsheet_Book.attributes={cellsheet_Book_bookname}

# HasId class attributes and methods

# HasA1 class attributes and methods

# cellsheet_CellFormat class attributes and methods
cellsheet_CellFormat_value: Property = Property(name="value", type=StringType)
cellsheet_CellFormat.attributes={cellsheet_CellFormat_value}

# cellsheet_Sheet class attributes and methods
cellsheet_Sheet_sheetName: Property = Property(name="sheetName", type=StringType)
cellsheet_Sheet_sheetIndex: Property = Property(name="sheetIndex", type=IntegerType)
cellsheet_Sheet.attributes={cellsheet_Sheet_sheetName, cellsheet_Sheet_sheetIndex}

# cellsheet_Row class attributes and methods
cellsheet_Row_rowIndex: Property = Property(name="rowIndex", type=IntegerType)
cellsheet_Row_m_getBook: Method = Method(name="getBook", parameters={}, type=StringType)
cellsheet_Row_m_getA1RowIndex: Method = Method(name="getA1RowIndex", parameters={}, type=IntegerType)
cellsheet_Row.attributes={cellsheet_Row_rowIndex}
cellsheet_Row.methods={cellsheet_Row_m_getA1RowIndex, cellsheet_Row_m_getBook}

# cellsheet_Cell class attributes and methods
cellsheet_Cell_colIndex: Property = Property(name="colIndex", type=IntegerType)
cellsheet_Cell_m_getBook: Method = Method(name="getBook", parameters={}, type=StringType)
cellsheet_Cell_m_getSheet: Method = Method(name="getSheet", parameters={}, type=StringType)
cellsheet_Cell_m_getRowIndex: Method = Method(name="getRowIndex", parameters={}, type=IntegerType)
cellsheet_Cell_m_getA1RowIndex: Method = Method(name="getA1RowIndex", parameters={}, type=IntegerType)
cellsheet_Cell_m_getA1ColIndex: Method = Method(name="getA1ColIndex", parameters={}, type=StringType)
cellsheet_Cell.attributes={cellsheet_Cell_colIndex}
cellsheet_Cell.methods={cellsheet_Cell_m_getRowIndex, cellsheet_Cell_m_getA1ColIndex, cellsheet_Cell_m_getBook, cellsheet_Cell_m_getA1RowIndex, cellsheet_Cell_m_getSheet}

# cellsheet_Ast class attributes and methods

# cellsheet_BlankCell class attributes and methods
cellsheet_BlankCell_value: Property = Property(name="value", type=StringType)
cellsheet_BlankCell.attributes={cellsheet_BlankCell_value}

# Cell class attributes and methods

# cellsheet_TextCell class attributes and methods
cellsheet_TextCell_value: Property = Property(name="value", type=StringType)
cellsheet_TextCell.attributes={cellsheet_TextCell_value}

# cellsheet_NumericCell class attributes and methods
cellsheet_NumericCell_value: Property = Property(name="value", type=StringType)
cellsheet_NumericCell.attributes={cellsheet_NumericCell_value}

# cellsheet_BooleanCell class attributes and methods
cellsheet_BooleanCell_value: Property = Property(name="value", type=StringType)
cellsheet_BooleanCell.attributes={cellsheet_BooleanCell_value}

# cellsheet_DateCell class attributes and methods
cellsheet_DateCell_value: Property = Property(name="value", type=DateType)
cellsheet_DateCell.attributes={cellsheet_DateCell_value}

# cellsheet_FormulaCell class attributes and methods
cellsheet_FormulaCell_value: Property = Property(name="value", type=StringType)
cellsheet_FormulaCell.attributes={cellsheet_FormulaCell_value}

# cellsheet_AstEval class attributes and methods
cellsheet_AstEval_text: Property = Property(name="text", type=StringType)
cellsheet_AstEval_numberValue: Property = Property(name="numberValue", type=StringType)
cellsheet_AstEval_isError: Property = Property(name="isError", type=BooleanType)
cellsheet_AstEval.attributes={cellsheet_AstEval_numberValue, cellsheet_AstEval_text, cellsheet_AstEval_isError}

# cellsheet_Range class attributes and methods

# cellsheet_Operand class attributes and methods

# Ast class attributes and methods

# cellsheet_Operation class attributes and methods

# cellsheet_PrefixOperator class attributes and methods

# cellsheet_InfixOperator class attributes and methods

# cellsheet_PostfixOperator class attributes and methods

# cellsheet_Unknown class attributes and methods

# cellsheet_Noop class attributes and methods

# cellsheet_Text class attributes and methods

# Operand class attributes and methods

# cellsheet_Number class attributes and methods

# cellsheet_Logical class attributes and methods

# cellsheet_Error class attributes and methods

# cellsheet_Ref class attributes and methods

# cellsheet_RelativeRef class attributes and methods

# Ref class attributes and methods

# cellsheet_RelativeRange class attributes and methods

# cellsheet_Function class attributes and methods

# Operation class attributes and methods

# cellsheet_Plus class attributes and methods

# PrefixOperator class attributes and methods

# cellsheet_Negation class attributes and methods

# cellsheet_Percent class attributes and methods

# PostfixOperator class attributes and methods

# cellsheet_Exponentiation class attributes and methods

# InfixOperator class attributes and methods

# cellsheet_Multiplication class attributes and methods

# cellsheet_Division class attributes and methods

# cellsheet_Addition class attributes and methods

# cellsheet_Subtraction class attributes and methods

# cellsheet_Concatenation class attributes and methods

# cellsheet_EQ class attributes and methods

# cellsheet_LT class attributes and methods

# cellsheet_GT class attributes and methods

# cellsheet_LTE class attributes and methods

# cellsheet_GTE class attributes and methods

# cellsheet_NEQ class attributes and methods

# cellsheet_Intersection class attributes and methods

# cellsheet_Union class attributes and methods

# Relationships
value0: BinaryAssociation = BinaryAssociation(
    name="value0",
    ends={
        Property(name="cellsheet_Token", type=cellsheet_EStringToTokenEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="cellsheet_EStringToTokenEntry", type=cellsheet_Token, multiplicity=Multiplicity(0, 1))
    }
)
books1: BinaryAssociation = BinaryAssociation(
    name="books1",
    ends={
        Property(name="Book", type=cellsheet_Workspace, multiplicity=Multiplicity(1, 1)),
        Property(name="workspace", type=cellsheet_Book, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tokens2: BinaryAssociation = BinaryAssociation(
    name="tokens2",
    ends={
        Property(name="cellsheet_EStringToTokenEntry3", type=cellsheet_Workspace, multiplicity=Multiplicity(1, 1)),
        Property(name="cellsheet_Workspace", type=cellsheet_EStringToTokenEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
workspace4: BinaryAssociation = BinaryAssociation(
    name="workspace4",
    ends={
        Property(name="Workspace", type=cellsheet_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="books", type=cellsheet_Workspace, multiplicity=Multiplicity(0, 1))
    }
)
cellFormats5: BinaryAssociation = BinaryAssociation(
    name="cellFormats5",
    ends={
        Property(name="CellFormat", type=cellsheet_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="book", type=cellsheet_CellFormat, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sheets6: BinaryAssociation = BinaryAssociation(
    name="sheets6",
    ends={
        Property(name="Sheet", type=cellsheet_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="book7", type=cellsheet_Sheet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
book8: BinaryAssociation = BinaryAssociation(
    name="book8",
    ends={
        Property(name="Book9", type=cellsheet_Sheet, multiplicity=Multiplicity(1, 1)),
        Property(name="sheets", type=cellsheet_Book, multiplicity=Multiplicity(0, 1))
    }
)
rows10: BinaryAssociation = BinaryAssociation(
    name="rows10",
    ends={
        Property(name="Row", type=cellsheet_Sheet, multiplicity=Multiplicity(1, 1)),
        Property(name="sheet", type=cellsheet_Row, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sheet11: BinaryAssociation = BinaryAssociation(
    name="sheet11",
    ends={
        Property(name="Sheet12", type=cellsheet_Row, multiplicity=Multiplicity(1, 1)),
        Property(name="rows", type=cellsheet_Sheet, multiplicity=Multiplicity(0, 1))
    }
)
cells13: BinaryAssociation = BinaryAssociation(
    name="cells13",
    ends={
        Property(name="Cell", type=cellsheet_Row, multiplicity=Multiplicity(1, 1)),
        Property(name="row", type=cellsheet_Cell, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
row14: BinaryAssociation = BinaryAssociation(
    name="row14",
    ends={
        Property(name="Row15", type=cellsheet_Cell, multiplicity=Multiplicity(1, 1)),
        Property(name="cells", type=cellsheet_Row, multiplicity=Multiplicity(0, 1))
    }
)
asts16: BinaryAssociation = BinaryAssociation(
    name="asts16",
    ends={
        Property(name="Ast", type=cellsheet_Cell, multiplicity=Multiplicity(1, 1)),
        Property(name="cell", type=cellsheet_Ast, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
root17: BinaryAssociation = BinaryAssociation(
    name="root17",
    ends={
        Property(name="cellsheet_Ast", type=cellsheet_Cell, multiplicity=Multiplicity(1, 1)),
        Property(name="cellsheet_Cell", type=cellsheet_Ast, multiplicity=Multiplicity(0, 1))
    }
)
usedBy18: BinaryAssociation = BinaryAssociation(
    name="usedBy18",
    ends={
        Property(name="Ast19", type=cellsheet_Token, multiplicity=Multiplicity(1, 1)),
        Property(name="token", type=cellsheet_Ast, multiplicity=Multiplicity(0, 9999))
    }
)
children21: BinaryAssociation = BinaryAssociation(
    name="children21",
    ends={
        Property(name="cellsheet_Ast22", type=cellsheet_Ast, multiplicity=Multiplicity(1, 1)),
        Property(name="cellsheet_Ast20", type=cellsheet_Ast, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cell23: BinaryAssociation = BinaryAssociation(
    name="cell23",
    ends={
        Property(name="Cell24", type=cellsheet_Ast, multiplicity=Multiplicity(1, 1)),
        Property(name="asts", type=cellsheet_Cell, multiplicity=Multiplicity(0, 1))
    }
)
token25: BinaryAssociation = BinaryAssociation(
    name="token25",
    ends={
        Property(name="Token", type=cellsheet_Ast, multiplicity=Multiplicity(1, 1)),
        Property(name="usedBy", type=cellsheet_Token, multiplicity=Multiplicity(0, 1))
    }
)
result26: BinaryAssociation = BinaryAssociation(
    name="result26",
    ends={
        Property(name="cellsheet_AstEval", type=cellsheet_Ast, multiplicity=Multiplicity(1, 1)),
        Property(name="cellsheet_Ast27", type=cellsheet_AstEval, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
book28: BinaryAssociation = BinaryAssociation(
    name="book28",
    ends={
        Property(name="Book29", type=cellsheet_CellFormat, multiplicity=Multiplicity(1, 1)),
        Property(name="cellFormats", type=cellsheet_Book, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_cellsheet_Book_HasId = Generalization(general=HasId, specific=cellsheet_Book)
gen_cellsheet_Book_HasA1 = Generalization(general=HasA1, specific=cellsheet_Book)
gen_cellsheet_Sheet_HasId = Generalization(general=HasId, specific=cellsheet_Sheet)
gen_cellsheet_Sheet_HasA1 = Generalization(general=HasA1, specific=cellsheet_Sheet)
gen_cellsheet_Row_HasId = Generalization(general=HasId, specific=cellsheet_Row)
gen_cellsheet_Row_HasA1 = Generalization(general=HasA1, specific=cellsheet_Row)
gen_cellsheet_Cell_HasId = Generalization(general=HasId, specific=cellsheet_Cell)
gen_cellsheet_Cell_HasA1 = Generalization(general=HasA1, specific=cellsheet_Cell)
gen_cellsheet_BlankCell_Cell = Generalization(general=Cell, specific=cellsheet_BlankCell)
gen_cellsheet_TextCell_Cell = Generalization(general=Cell, specific=cellsheet_TextCell)
gen_cellsheet_NumericCell_Cell = Generalization(general=Cell, specific=cellsheet_NumericCell)
gen_cellsheet_BooleanCell_Cell = Generalization(general=Cell, specific=cellsheet_BooleanCell)
gen_cellsheet_DateCell_Cell = Generalization(general=Cell, specific=cellsheet_DateCell)
gen_cellsheet_FormulaCell_Cell = Generalization(general=Cell, specific=cellsheet_FormulaCell)
gen_cellsheet_Range_Operand = Generalization(general=Operand, specific=cellsheet_Range)
gen_cellsheet_Operand_Ast = Generalization(general=Ast, specific=cellsheet_Operand)
gen_cellsheet_Operation_Ast = Generalization(general=Ast, specific=cellsheet_Operation)
gen_cellsheet_PrefixOperator_Ast = Generalization(general=Ast, specific=cellsheet_PrefixOperator)
gen_cellsheet_InfixOperator_Ast = Generalization(general=Ast, specific=cellsheet_InfixOperator)
gen_cellsheet_PostfixOperator_Ast = Generalization(general=Ast, specific=cellsheet_PostfixOperator)
gen_cellsheet_Unknown_Ast = Generalization(general=Ast, specific=cellsheet_Unknown)
gen_cellsheet_Noop_Ast = Generalization(general=Ast, specific=cellsheet_Noop)
gen_cellsheet_Text_Operand = Generalization(general=Operand, specific=cellsheet_Text)
gen_cellsheet_Number_Operand = Generalization(general=Operand, specific=cellsheet_Number)
gen_cellsheet_Logical_Operand = Generalization(general=Operand, specific=cellsheet_Logical)
gen_cellsheet_Error_Operand = Generalization(general=Operand, specific=cellsheet_Error)
gen_cellsheet_Ref_Operand = Generalization(general=Operand, specific=cellsheet_Ref)
gen_cellsheet_GTE_InfixOperator = Generalization(general=InfixOperator, specific=cellsheet_GTE)
gen_cellsheet_RelativeRef_Ref = Generalization(general=Ref, specific=cellsheet_RelativeRef)
gen_cellsheet_RelativeRange_Ref = Generalization(general=Ref, specific=cellsheet_RelativeRange)
gen_cellsheet_Function_Operation = Generalization(general=Operation, specific=cellsheet_Function)
gen_cellsheet_Plus_PrefixOperator = Generalization(general=PrefixOperator, specific=cellsheet_Plus)
gen_cellsheet_Negation_PrefixOperator = Generalization(general=PrefixOperator, specific=cellsheet_Negation)
gen_cellsheet_Percent_PostfixOperator = Generalization(general=PostfixOperator, specific=cellsheet_Percent)
gen_cellsheet_Exponentiation_InfixOperator = Generalization(general=InfixOperator, specific=cellsheet_Exponentiation)
gen_cellsheet_Multiplication_InfixOperator = Generalization(general=InfixOperator, specific=cellsheet_Multiplication)
gen_cellsheet_Division_InfixOperator = Generalization(general=InfixOperator, specific=cellsheet_Division)
gen_cellsheet_Addition_InfixOperator = Generalization(general=InfixOperator, specific=cellsheet_Addition)
gen_cellsheet_Subtraction_InfixOperator = Generalization(general=InfixOperator, specific=cellsheet_Subtraction)
gen_cellsheet_Concatenation_InfixOperator = Generalization(general=InfixOperator, specific=cellsheet_Concatenation)
gen_cellsheet_EQ_InfixOperator = Generalization(general=InfixOperator, specific=cellsheet_EQ)
gen_cellsheet_LT_InfixOperator = Generalization(general=InfixOperator, specific=cellsheet_LT)
gen_cellsheet_GT_InfixOperator = Generalization(general=InfixOperator, specific=cellsheet_GT)
gen_cellsheet_LTE_InfixOperator = Generalization(general=InfixOperator, specific=cellsheet_LTE)
gen_cellsheet_NEQ_InfixOperator = Generalization(general=InfixOperator, specific=cellsheet_NEQ)
gen_cellsheet_Intersection_InfixOperator = Generalization(general=InfixOperator, specific=cellsheet_Intersection)
gen_cellsheet_Union_InfixOperator = Generalization(general=InfixOperator, specific=cellsheet_Union)
gen_cellsheet_CellFormat_HasId = Generalization(general=HasId, specific=cellsheet_CellFormat)

# Domain Model
domain_model = DomainModel(
    name="cellsheet",
    types={cellsheet_EStringToTokenEntry, cellsheet_Token, cellsheet_HasA1, cellsheet_HasId, cellsheet_Workspace, cellsheet_Book, HasId, HasA1, cellsheet_CellFormat, cellsheet_Sheet, cellsheet_Row, cellsheet_Cell, cellsheet_Ast, cellsheet_BlankCell, Cell, cellsheet_TextCell, cellsheet_NumericCell, cellsheet_BooleanCell, cellsheet_DateCell, cellsheet_FormulaCell, cellsheet_AstEval, cellsheet_Range, cellsheet_Operand, Ast, cellsheet_Operation, cellsheet_PrefixOperator, cellsheet_InfixOperator, cellsheet_PostfixOperator, cellsheet_Unknown, cellsheet_Noop, cellsheet_Text, Operand, cellsheet_Number, cellsheet_Logical, cellsheet_Error, cellsheet_Ref, cellsheet_RelativeRef, Ref, cellsheet_RelativeRange, cellsheet_Function, Operation, cellsheet_Plus, PrefixOperator, cellsheet_Negation, cellsheet_Percent, PostfixOperator, cellsheet_Exponentiation, InfixOperator, cellsheet_Multiplication, cellsheet_Division, cellsheet_Addition, cellsheet_Subtraction, cellsheet_Concatenation, cellsheet_EQ, cellsheet_LT, cellsheet_GT, cellsheet_LTE, cellsheet_GTE, cellsheet_NEQ, cellsheet_Intersection, cellsheet_Union},
    associations={value0, books1, tokens2, workspace4, cellFormats5, sheets6, book8, rows10, sheet11, cells13, row14, asts16, root17, usedBy18, children21, cell23, token25, result26, book28},
    generalizations={gen_cellsheet_Book_HasId, gen_cellsheet_Book_HasA1, gen_cellsheet_Sheet_HasId, gen_cellsheet_Sheet_HasA1, gen_cellsheet_Row_HasId, gen_cellsheet_Row_HasA1, gen_cellsheet_Cell_HasId, gen_cellsheet_Cell_HasA1, gen_cellsheet_BlankCell_Cell, gen_cellsheet_TextCell_Cell, gen_cellsheet_NumericCell_Cell, gen_cellsheet_BooleanCell_Cell, gen_cellsheet_DateCell_Cell, gen_cellsheet_FormulaCell_Cell, gen_cellsheet_Range_Operand, gen_cellsheet_Operand_Ast, gen_cellsheet_Operation_Ast, gen_cellsheet_PrefixOperator_Ast, gen_cellsheet_InfixOperator_Ast, gen_cellsheet_PostfixOperator_Ast, gen_cellsheet_Unknown_Ast, gen_cellsheet_Noop_Ast, gen_cellsheet_Text_Operand, gen_cellsheet_Number_Operand, gen_cellsheet_Logical_Operand, gen_cellsheet_Error_Operand, gen_cellsheet_Ref_Operand, gen_cellsheet_GTE_InfixOperator, gen_cellsheet_RelativeRef_Ref, gen_cellsheet_RelativeRange_Ref, gen_cellsheet_Function_Operation, gen_cellsheet_Plus_PrefixOperator, gen_cellsheet_Negation_PrefixOperator, gen_cellsheet_Percent_PostfixOperator, gen_cellsheet_Exponentiation_InfixOperator, gen_cellsheet_Multiplication_InfixOperator, gen_cellsheet_Division_InfixOperator, gen_cellsheet_Addition_InfixOperator, gen_cellsheet_Subtraction_InfixOperator, gen_cellsheet_Concatenation_InfixOperator, gen_cellsheet_EQ_InfixOperator, gen_cellsheet_LT_InfixOperator, gen_cellsheet_GT_InfixOperator, gen_cellsheet_LTE_InfixOperator, gen_cellsheet_NEQ_InfixOperator, gen_cellsheet_Intersection_InfixOperator, gen_cellsheet_Union_InfixOperator, gen_cellsheet_CellFormat_HasId},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)