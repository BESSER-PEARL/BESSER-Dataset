from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class InfixOperator:

    pass
class cellsheet_Subtraction(InfixOperator):

    pass
class cellsheet_NEQ(InfixOperator):

    pass
class cellsheet_EQ(InfixOperator):

    pass
class cellsheet_Concatenation(InfixOperator):

    pass
class cellsheet_Intersection(InfixOperator):

    pass
class cellsheet_Union(InfixOperator):

    pass
class cellsheet_Division(InfixOperator):

    pass
class cellsheet_LTE(InfixOperator):

    pass
class cellsheet_Multiplication(InfixOperator):

    pass
class cellsheet_LT(InfixOperator):

    pass
class cellsheet_Addition(InfixOperator):

    pass
class cellsheet_GT(InfixOperator):

    pass
class cellsheet_GTE(InfixOperator):

    pass
class cellsheet_Exponentiation(InfixOperator):

    pass
class PostfixOperator:

    pass
class cellsheet_Percent(PostfixOperator):

    pass
class PrefixOperator:

    pass
class cellsheet_Negation(PrefixOperator):

    pass
class cellsheet_Plus(PrefixOperator):

    pass
class Operation:

    pass
class cellsheet_Function(Operation):

    pass
class Ref:

    pass
class cellsheet_RelativeRange(Ref):

    pass
class cellsheet_RelativeRef(Ref):

    pass
class Operand:

    pass
class cellsheet_Logical(Operand):

    pass
class cellsheet_Ref(Operand):

    pass
class cellsheet_Error(Operand):

    pass
class cellsheet_Number(Operand):

    pass
class cellsheet_Text(Operand):

    pass
class Ast:

    pass
class cellsheet_InfixOperator(Ast):

    pass
class cellsheet_PrefixOperator(Ast):

    pass
class cellsheet_PostfixOperator(Ast):

    pass
class cellsheet_Unknown(Ast):

    pass
class cellsheet_Noop(Ast):

    pass
class cellsheet_Operation(Ast):

    pass
class cellsheet_Operand(Ast):

    pass
class cellsheet_Range(Operand):

    pass
class cellsheet_AstEval:

    def __init__(self, text: str, numberValue: str, isError: bool, cellsheet_AstEval: "cellsheet_Ast" = None):
        self.text = text
        self.numberValue = numberValue
        self.isError = isError
        self.cellsheet_AstEval = cellsheet_AstEval
        
    @property
    def numberValue(self) -> str:
        return self.__numberValue

    @numberValue.setter
    def numberValue(self, numberValue: str):
        self.__numberValue = numberValue

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def isError(self) -> bool:
        return self.__isError

    @isError.setter
    def isError(self, isError: bool):
        self.__isError = isError

    @property
    def cellsheet_AstEval(self):
        return self.__cellsheet_AstEval

    @cellsheet_AstEval.setter
    def cellsheet_AstEval(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cellsheet_AstEval__cellsheet_AstEval", None)
        self.__cellsheet_AstEval = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cellsheet_Ast27"):
                opp_val = getattr(old_value, "cellsheet_Ast27", None)
                if opp_val == self:
                    setattr(old_value, "cellsheet_Ast27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cellsheet_Ast27"):
                opp_val = getattr(value, "cellsheet_Ast27", None)
                setattr(value, "cellsheet_Ast27", self)

class Cell:

    pass
class cellsheet_DateCell(Cell):

    def __init__(self, value: date):
        self.value = value
        
    @property
    def value(self) -> date:
        return self.__value

    @value.setter
    def value(self, value: date):
        self.__value = value

class cellsheet_FormulaCell(Cell):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class cellsheet_TextCell(Cell):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class cellsheet_BooleanCell(Cell):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class cellsheet_NumericCell(Cell):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class cellsheet_BlankCell(Cell):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class cellsheet_Ast(ABC):

    pass
class HasA1:

    pass
class HasId:

    pass
class cellsheet_Sheet(HasA1, HasId):

    def __init__(self, sheetName: str, sheetIndex: int, Sheet: "cellsheet_Book" = None, sheets: "cellsheet_Book" = None, sheet: set["cellsheet_Row"] = None, Sheet12: "cellsheet_Row" = None):
        self.sheetName = sheetName
        self.sheetIndex = sheetIndex
        self.Sheet = Sheet
        self.sheets = sheets
        self.sheet = sheet if sheet is not None else set()
        self.Sheet12 = Sheet12
        
    @property
    def sheetName(self) -> str:
        return self.__sheetName

    @sheetName.setter
    def sheetName(self, sheetName: str):
        self.__sheetName = sheetName

    @property
    def sheetIndex(self) -> int:
        return self.__sheetIndex

    @sheetIndex.setter
    def sheetIndex(self, sheetIndex: int):
        self.__sheetIndex = sheetIndex

    @property
    def sheets(self):
        return self.__sheets

    @sheets.setter
    def sheets(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cellsheet_Sheet__sheets", None)
        self.__sheets = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Book9"):
                opp_val = getattr(old_value, "Book9", None)
                if opp_val == self:
                    setattr(old_value, "Book9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Book9"):
                opp_val = getattr(value, "Book9", None)
                setattr(value, "Book9", self)

    @property
    def sheet(self):
        return self.__sheet

    @sheet.setter
    def sheet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cellsheet_Sheet__sheet", None)
        self.__sheet = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Row"):
                    opp_val = getattr(item, "Row", None)
                    
                    if opp_val == self:
                        setattr(item, "Row", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Row"):
                    opp_val = getattr(item, "Row", None)
                    
                    setattr(item, "Row", self)
                    

    @property
    def Sheet12(self):
        return self.__Sheet12

    @Sheet12.setter
    def Sheet12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cellsheet_Sheet__Sheet12", None)
        self.__Sheet12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rows"):
                opp_val = getattr(old_value, "rows", None)
                if opp_val == self:
                    setattr(old_value, "rows", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rows"):
                opp_val = getattr(value, "rows", None)
                setattr(value, "rows", self)

    @property
    def Sheet(self):
        return self.__Sheet

    @Sheet.setter
    def Sheet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cellsheet_Sheet__Sheet", None)
        self.__Sheet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "book7"):
                opp_val = getattr(old_value, "book7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "book7"):
                opp_val = getattr(value, "book7", None)
                if opp_val is None:
                    setattr(value, "book7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class cellsheet_Row(HasA1, HasId):

    def __init__(self, rowIndex: int, Row: "cellsheet_Sheet" = None, rows: "cellsheet_Sheet" = None, row: set["cellsheet_Cell"] = None, Row15: "cellsheet_Cell" = None):
        self.rowIndex = rowIndex
        self.Row = Row
        self.rows = rows
        self.row = row if row is not None else set()
        self.Row15 = Row15
        
    @property
    def rowIndex(self) -> int:
        return self.__rowIndex

    @rowIndex.setter
    def rowIndex(self, rowIndex: int):
        self.__rowIndex = rowIndex

    @property
    def Row(self):
        return self.__Row

    @Row.setter
    def Row(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cellsheet_Row__Row", None)
        self.__Row = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sheet"):
                opp_val = getattr(old_value, "sheet", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sheet"):
                opp_val = getattr(value, "sheet", None)
                if opp_val is None:
                    setattr(value, "sheet", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def row(self):
        return self.__row

    @row.setter
    def row(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cellsheet_Row__row", None)
        self.__row = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Cell"):
                    opp_val = getattr(item, "Cell", None)
                    
                    if opp_val == self:
                        setattr(item, "Cell", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Cell"):
                    opp_val = getattr(item, "Cell", None)
                    
                    setattr(item, "Cell", self)
                    

    @property
    def rows(self):
        return self.__rows

    @rows.setter
    def rows(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cellsheet_Row__rows", None)
        self.__rows = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Sheet12"):
                opp_val = getattr(old_value, "Sheet12", None)
                if opp_val == self:
                    setattr(old_value, "Sheet12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Sheet12"):
                opp_val = getattr(value, "Sheet12", None)
                setattr(value, "Sheet12", self)

    @property
    def Row15(self):
        return self.__Row15

    @Row15.setter
    def Row15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cellsheet_Row__Row15", None)
        self.__Row15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cells"):
                opp_val = getattr(old_value, "cells", None)
                if opp_val == self:
                    setattr(old_value, "cells", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cells"):
                opp_val = getattr(value, "cells", None)
                setattr(value, "cells", self)

    def getA1RowIndex(self) -> int:
        # TODO: Implement getA1RowIndex method
        pass

    def getBook(self) -> str:
        # TODO: Implement getBook method
        pass

class cellsheet_Cell(HasA1, HasId):

    def __init__(self, colIndex: int, Cell: "cellsheet_Row" = None, cells: "cellsheet_Row" = None, cell: set["cellsheet_Ast"] = None, cellsheet_Cell: "cellsheet_Ast" = None, Cell24: "cellsheet_Ast" = None):
        self.colIndex = colIndex
        self.Cell = Cell
        self.cells = cells
        self.cell = cell if cell is not None else set()
        self.cellsheet_Cell = cellsheet_Cell
        self.Cell24 = Cell24
        
    @property
    def colIndex(self) -> int:
        return self.__colIndex

    @colIndex.setter
    def colIndex(self, colIndex: int):
        self.__colIndex = colIndex

    @property
    def cellsheet_Cell(self):
        return self.__cellsheet_Cell

    @cellsheet_Cell.setter
    def cellsheet_Cell(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cellsheet_Cell__cellsheet_Cell", None)
        self.__cellsheet_Cell = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cellsheet_Ast"):
                opp_val = getattr(old_value, "cellsheet_Ast", None)
                if opp_val == self:
                    setattr(old_value, "cellsheet_Ast", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cellsheet_Ast"):
                opp_val = getattr(value, "cellsheet_Ast", None)
                setattr(value, "cellsheet_Ast", self)

    @property
    def cells(self):
        return self.__cells

    @cells.setter
    def cells(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cellsheet_Cell__cells", None)
        self.__cells = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Row15"):
                opp_val = getattr(old_value, "Row15", None)
                if opp_val == self:
                    setattr(old_value, "Row15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Row15"):
                opp_val = getattr(value, "Row15", None)
                setattr(value, "Row15", self)

    @property
    def cell(self):
        return self.__cell

    @cell.setter
    def cell(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cellsheet_Cell__cell", None)
        self.__cell = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Ast"):
                    opp_val = getattr(item, "Ast", None)
                    
                    if opp_val == self:
                        setattr(item, "Ast", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Ast"):
                    opp_val = getattr(item, "Ast", None)
                    
                    setattr(item, "Ast", self)
                    

    @property
    def Cell24(self):
        return self.__Cell24

    @Cell24.setter
    def Cell24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cellsheet_Cell__Cell24", None)
        self.__Cell24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "asts"):
                opp_val = getattr(old_value, "asts", None)
                if opp_val == self:
                    setattr(old_value, "asts", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "asts"):
                opp_val = getattr(value, "asts", None)
                setattr(value, "asts", self)

    @property
    def Cell(self):
        return self.__Cell

    @Cell.setter
    def Cell(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cellsheet_Cell__Cell", None)
        self.__Cell = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "row"):
                opp_val = getattr(old_value, "row", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "row"):
                opp_val = getattr(value, "row", None)
                if opp_val is None:
                    setattr(value, "row", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def getRowIndex(self) -> int:
        # TODO: Implement getRowIndex method
        pass

    def getA1ColIndex(self) -> str:
        # TODO: Implement getA1ColIndex method
        pass

    def getBook(self) -> str:
        # TODO: Implement getBook method
        pass

    def getA1RowIndex(self) -> int:
        # TODO: Implement getA1RowIndex method
        pass

    def getSheet(self) -> str:
        # TODO: Implement getSheet method
        pass

class cellsheet_CellFormat(HasId):

    def __init__(self, value: str, CellFormat: "cellsheet_Book" = None, cellFormats: "cellsheet_Book" = None):
        self.value = value
        self.CellFormat = CellFormat
        self.cellFormats = cellFormats
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def cellFormats(self):
        return self.__cellFormats

    @cellFormats.setter
    def cellFormats(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cellsheet_CellFormat__cellFormats", None)
        self.__cellFormats = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Book29"):
                opp_val = getattr(old_value, "Book29", None)
                if opp_val == self:
                    setattr(old_value, "Book29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Book29"):
                opp_val = getattr(value, "Book29", None)
                setattr(value, "Book29", self)

    @property
    def CellFormat(self):
        return self.__CellFormat

    @CellFormat.setter
    def CellFormat(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cellsheet_CellFormat__CellFormat", None)
        self.__CellFormat = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "book"):
                opp_val = getattr(old_value, "book", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "book"):
                opp_val = getattr(value, "book", None)
                if opp_val is None:
                    setattr(value, "book", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class cellsheet_Book(HasA1, HasId):

    def __init__(self, bookname: str, Book: "cellsheet_Workspace" = None, books: "cellsheet_Workspace" = None, book: set["cellsheet_CellFormat"] = None, book7: set["cellsheet_Sheet"] = None, Book9: "cellsheet_Sheet" = None, Book29: "cellsheet_CellFormat" = None):
        self.bookname = bookname
        self.Book = Book
        self.books = books
        self.book = book if book is not None else set()
        self.book7 = book7 if book7 is not None else set()
        self.Book9 = Book9
        self.Book29 = Book29
        
    @property
    def bookname(self) -> str:
        return self.__bookname

    @bookname.setter
    def bookname(self, bookname: str):
        self.__bookname = bookname

    @property
    def Book29(self):
        return self.__Book29

    @Book29.setter
    def Book29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cellsheet_Book__Book29", None)
        self.__Book29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cellFormats"):
                opp_val = getattr(old_value, "cellFormats", None)
                if opp_val == self:
                    setattr(old_value, "cellFormats", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cellFormats"):
                opp_val = getattr(value, "cellFormats", None)
                setattr(value, "cellFormats", self)

    @property
    def Book9(self):
        return self.__Book9

    @Book9.setter
    def Book9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cellsheet_Book__Book9", None)
        self.__Book9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sheets"):
                opp_val = getattr(old_value, "sheets", None)
                if opp_val == self:
                    setattr(old_value, "sheets", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sheets"):
                opp_val = getattr(value, "sheets", None)
                setattr(value, "sheets", self)

    @property
    def books(self):
        return self.__books

    @books.setter
    def books(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cellsheet_Book__books", None)
        self.__books = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Workspace"):
                opp_val = getattr(old_value, "Workspace", None)
                if opp_val == self:
                    setattr(old_value, "Workspace", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Workspace"):
                opp_val = getattr(value, "Workspace", None)
                setattr(value, "Workspace", self)

    @property
    def book(self):
        return self.__book

    @book.setter
    def book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cellsheet_Book__book", None)
        self.__book = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CellFormat"):
                    opp_val = getattr(item, "CellFormat", None)
                    
                    if opp_val == self:
                        setattr(item, "CellFormat", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CellFormat"):
                    opp_val = getattr(item, "CellFormat", None)
                    
                    setattr(item, "CellFormat", self)
                    

    @property
    def Book(self):
        return self.__Book

    @Book.setter
    def Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cellsheet_Book__Book", None)
        self.__Book = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workspace"):
                opp_val = getattr(old_value, "workspace", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workspace"):
                opp_val = getattr(value, "workspace", None)
                if opp_val is None:
                    setattr(value, "workspace", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def book7(self):
        return self.__book7

    @book7.setter
    def book7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cellsheet_Book__book7", None)
        self.__book7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Sheet"):
                    opp_val = getattr(item, "Sheet", None)
                    
                    if opp_val == self:
                        setattr(item, "Sheet", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Sheet"):
                    opp_val = getattr(item, "Sheet", None)
                    
                    setattr(item, "Sheet", self)
                    

class cellsheet_Workspace:

    pass
class cellsheet_HasId(ABC):

    def __init__(self, id: str):
        self.id = id
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

class cellsheet_HasA1(ABC):

    def __init__(self, a1: str):
        self.a1 = a1
        
    @property
    def a1(self) -> str:
        return self.__a1

    @a1.setter
    def a1(self, a1: str):
        self.__a1 = a1

class cellsheet_Token:

    def __init__(self, value: str, cellsheet_Token: "cellsheet_EStringToTokenEntry" = None, token: set["cellsheet_Ast"] = None, Token: "cellsheet_Ast" = None):
        self.value = value
        self.cellsheet_Token = cellsheet_Token
        self.token = token if token is not None else set()
        self.Token = Token
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def cellsheet_Token(self):
        return self.__cellsheet_Token

    @cellsheet_Token.setter
    def cellsheet_Token(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cellsheet_Token__cellsheet_Token", None)
        self.__cellsheet_Token = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cellsheet_EStringToTokenEntry"):
                opp_val = getattr(old_value, "cellsheet_EStringToTokenEntry", None)
                if opp_val == self:
                    setattr(old_value, "cellsheet_EStringToTokenEntry", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cellsheet_EStringToTokenEntry"):
                opp_val = getattr(value, "cellsheet_EStringToTokenEntry", None)
                setattr(value, "cellsheet_EStringToTokenEntry", self)

    @property
    def Token(self):
        return self.__Token

    @Token.setter
    def Token(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cellsheet_Token__Token", None)
        self.__Token = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "usedBy"):
                opp_val = getattr(old_value, "usedBy", None)
                if opp_val == self:
                    setattr(old_value, "usedBy", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "usedBy"):
                opp_val = getattr(value, "usedBy", None)
                setattr(value, "usedBy", self)

    @property
    def token(self):
        return self.__token

    @token.setter
    def token(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cellsheet_Token__token", None)
        self.__token = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Ast19"):
                    opp_val = getattr(item, "Ast19", None)
                    
                    if opp_val == self:
                        setattr(item, "Ast19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Ast19"):
                    opp_val = getattr(item, "Ast19", None)
                    
                    setattr(item, "Ast19", self)
                    

class cellsheet_EStringToTokenEntry:

    def __init__(self, key: str, cellsheet_EStringToTokenEntry: "cellsheet_Token" = None, cellsheet_EStringToTokenEntry3: "cellsheet_Workspace" = None):
        self.key = key
        self.cellsheet_EStringToTokenEntry = cellsheet_EStringToTokenEntry
        self.cellsheet_EStringToTokenEntry3 = cellsheet_EStringToTokenEntry3
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def cellsheet_EStringToTokenEntry3(self):
        return self.__cellsheet_EStringToTokenEntry3

    @cellsheet_EStringToTokenEntry3.setter
    def cellsheet_EStringToTokenEntry3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cellsheet_EStringToTokenEntry__cellsheet_EStringToTokenEntry3", None)
        self.__cellsheet_EStringToTokenEntry3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cellsheet_Workspace"):
                opp_val = getattr(old_value, "cellsheet_Workspace", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cellsheet_Workspace"):
                opp_val = getattr(value, "cellsheet_Workspace", None)
                if opp_val is None:
                    setattr(value, "cellsheet_Workspace", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cellsheet_EStringToTokenEntry(self):
        return self.__cellsheet_EStringToTokenEntry

    @cellsheet_EStringToTokenEntry.setter
    def cellsheet_EStringToTokenEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cellsheet_EStringToTokenEntry__cellsheet_EStringToTokenEntry", None)
        self.__cellsheet_EStringToTokenEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cellsheet_Token"):
                opp_val = getattr(old_value, "cellsheet_Token", None)
                if opp_val == self:
                    setattr(old_value, "cellsheet_Token", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cellsheet_Token"):
                opp_val = getattr(value, "cellsheet_Token", None)
                setattr(value, "cellsheet_Token", self)
