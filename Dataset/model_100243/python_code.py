from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class CellType(Enum):
    CellTypeNumeric = "CellTypeNumeric"
    CellTypeFormula = "CellTypeFormula"
    CellTypeString = "CellTypeString"
    CellTypeDate = "CellTypeDate"


############################################
# Definition of Classes
############################################

class spreadsheet_Cell:

    def __init__(self, ValueFormatted: str, CellType: str, DoubleValue: float, StringValue: str, Cell: "spreadsheet_Row" = None, Cell15: "spreadsheet_Column" = None, Cell20: "spreadsheet_Row" = None, Cell23: "spreadsheet_Column" = None):
        self.ValueFormatted = ValueFormatted
        self.CellType = CellType
        self.DoubleValue = DoubleValue
        self.StringValue = StringValue
        self.Cell = Cell
        self.Cell15 = Cell15
        self.Cell20 = Cell20
        self.Cell23 = Cell23
        
        pass
    @property
    def StringValue(self):
        return self.__StringValue

    @StringValue.setter
    def StringValue(self, StringValue: str):
        self.__StringValue = StringValue


    @property
    def CellType(self):
        return self.__CellType

    @CellType.setter
    def CellType(self, CellType: str):
        self.__CellType = CellType


    @property
    def DoubleValue(self):
        return self.__DoubleValue

    @DoubleValue.setter
    def DoubleValue(self, DoubleValue: float):
        self.__DoubleValue = DoubleValue


    @property
    def ValueFormatted(self):
        return self.__ValueFormatted

    @ValueFormatted.setter
    def ValueFormatted(self, ValueFormatted: str):
        self.__ValueFormatted = ValueFormatted


    @property
    def Cell23(self):
        return self.__Cell23

    @Cell23.setter
    def Cell23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spreadsheet_Cell__Cell23", None)
        self.__Cell23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Column24"):
                opp_val = getattr(old_value, "Column24", None)
                if opp_val == self:
                    setattr(old_value, "Column24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Column24"):
                opp_val = getattr(value, "Column24", None)
                setattr(value, "Column24", self)

    @property
    def Cell20(self):
        return self.__Cell20

    @Cell20.setter
    def Cell20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spreadsheet_Cell__Cell20", None)
        self.__Cell20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Row21"):
                opp_val = getattr(old_value, "Row21", None)
                if opp_val == self:
                    setattr(old_value, "Row21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Row21"):
                opp_val = getattr(value, "Row21", None)
                setattr(value, "Row21", self)

    @property
    def Cell15(self):
        return self.__Cell15

    @Cell15.setter
    def Cell15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spreadsheet_Cell__Cell15", None)
        self.__Cell15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Column14"):
                opp_val = getattr(old_value, "Column14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Column14"):
                opp_val = getattr(value, "Column14", None)
                if opp_val is None:
                    setattr(value, "Column14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Cell(self):
        return self.__Cell

    @Cell.setter
    def Cell(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spreadsheet_Cell__Cell", None)
        self.__Cell = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Row9"):
                opp_val = getattr(old_value, "Row9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Row9"):
                opp_val = getattr(value, "Row9", None)
                if opp_val is None:
                    setattr(value, "Row9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class spreadsheet_Column:

    def __init__(self, ColumnIndex: int, Column: "spreadsheet_Sheet" = None, Column14: set["spreadsheet_Cell"] = None, Column17: "spreadsheet_Sheet" = None, Column24: "spreadsheet_Cell" = None):
        self.ColumnIndex = ColumnIndex
        self.Column = Column
        self.Column14 = Column14 if Column14 is not None else set()
        self.Column17 = Column17
        self.Column24 = Column24
        
        pass
    @property
    def ColumnIndex(self):
        return self.__ColumnIndex

    @ColumnIndex.setter
    def ColumnIndex(self, ColumnIndex: int):
        self.__ColumnIndex = ColumnIndex


    @property
    def Column24(self):
        return self.__Column24

    @Column24.setter
    def Column24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spreadsheet_Column__Column24", None)
        self.__Column24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Cell23"):
                opp_val = getattr(old_value, "Cell23", None)
                if opp_val == self:
                    setattr(old_value, "Cell23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Cell23"):
                opp_val = getattr(value, "Cell23", None)
                setattr(value, "Cell23", self)

    @property
    def Column(self):
        return self.__Column

    @Column.setter
    def Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spreadsheet_Column__Column", None)
        self.__Column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Sheet4"):
                opp_val = getattr(old_value, "Sheet4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Sheet4"):
                opp_val = getattr(value, "Sheet4", None)
                if opp_val is None:
                    setattr(value, "Sheet4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Column17(self):
        return self.__Column17

    @Column17.setter
    def Column17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spreadsheet_Column__Column17", None)
        self.__Column17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Sheet18"):
                opp_val = getattr(old_value, "Sheet18", None)
                if opp_val == self:
                    setattr(old_value, "Sheet18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Sheet18"):
                opp_val = getattr(value, "Sheet18", None)
                setattr(value, "Sheet18", self)

    @property
    def Column14(self):
        return self.__Column14

    @Column14.setter
    def Column14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spreadsheet_Column__Column14", None)
        self.__Column14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Cell15"):
                    opp_val = getattr(item, "Cell15", None)
                    
                    if opp_val == self:
                        setattr(item, "Cell15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Cell15"):
                    opp_val = getattr(item, "Cell15", None)
                    
                    setattr(item, "Cell15", self)
                    

    def getCell(self, spreadsheet_rowindex) :
        # TODO: Implement getCell method
        pass

class spreadsheet_Row:

    def __init__(self, RowIndex: int, Row: "spreadsheet_Sheet" = None, Row9: set["spreadsheet_Cell"] = None, Row11: "spreadsheet_Sheet" = None, Row21: "spreadsheet_Cell" = None):
        self.RowIndex = RowIndex
        self.Row = Row
        self.Row9 = Row9 if Row9 is not None else set()
        self.Row11 = Row11
        self.Row21 = Row21
        
        pass
    @property
    def RowIndex(self):
        return self.__RowIndex

    @RowIndex.setter
    def RowIndex(self, RowIndex: int):
        self.__RowIndex = RowIndex


    @property
    def Row11(self):
        return self.__Row11

    @Row11.setter
    def Row11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spreadsheet_Row__Row11", None)
        self.__Row11 = value
        
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
    def Row9(self):
        return self.__Row9

    @Row9.setter
    def Row9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spreadsheet_Row__Row9", None)
        self.__Row9 = value if value is not None else set()
        
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
    def Row21(self):
        return self.__Row21

    @Row21.setter
    def Row21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spreadsheet_Row__Row21", None)
        self.__Row21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Cell20"):
                opp_val = getattr(old_value, "Cell20", None)
                if opp_val == self:
                    setattr(old_value, "Cell20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Cell20"):
                opp_val = getattr(value, "Cell20", None)
                setattr(value, "Cell20", self)

    @property
    def Row(self):
        return self.__Row

    @Row.setter
    def Row(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spreadsheet_Row__Row", None)
        self.__Row = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Sheet2"):
                opp_val = getattr(old_value, "Sheet2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Sheet2"):
                opp_val = getattr(value, "Sheet2", None)
                if opp_val is None:
                    setattr(value, "Sheet2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def getCell(self, spreadsheet_column) :
        # TODO: Implement getCell method
        pass

class spreadsheet_Sheet:

    def __init__(self, SheetName: str, SheetIndex: int, Sheet: "spreadsheet_Spreadsheet" = None, Sheet2: set["spreadsheet_Row"] = None, Sheet4: set["spreadsheet_Column"] = None, Sheet6: "spreadsheet_Spreadsheet" = None, Sheet12: "spreadsheet_Row" = None, Sheet18: "spreadsheet_Column" = None):
        self.SheetName = SheetName
        self.SheetIndex = SheetIndex
        self.Sheet = Sheet
        self.Sheet2 = Sheet2 if Sheet2 is not None else set()
        self.Sheet4 = Sheet4 if Sheet4 is not None else set()
        self.Sheet6 = Sheet6
        self.Sheet12 = Sheet12
        self.Sheet18 = Sheet18
        
        pass
    @property
    def SheetName(self):
        return self.__SheetName

    @SheetName.setter
    def SheetName(self, SheetName: str):
        self.__SheetName = SheetName


    @property
    def SheetIndex(self):
        return self.__SheetIndex

    @SheetIndex.setter
    def SheetIndex(self, SheetIndex: int):
        self.__SheetIndex = SheetIndex


    @property
    def Sheet6(self):
        return self.__Sheet6

    @Sheet6.setter
    def Sheet6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spreadsheet_Sheet__Sheet6", None)
        self.__Sheet6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Spreadsheet7"):
                opp_val = getattr(old_value, "Spreadsheet7", None)
                if opp_val == self:
                    setattr(old_value, "Spreadsheet7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Spreadsheet7"):
                opp_val = getattr(value, "Spreadsheet7", None)
                setattr(value, "Spreadsheet7", self)

    @property
    def Sheet2(self):
        return self.__Sheet2

    @Sheet2.setter
    def Sheet2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spreadsheet_Sheet__Sheet2", None)
        self.__Sheet2 = value if value is not None else set()
        
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
    def Sheet(self):
        return self.__Sheet

    @Sheet.setter
    def Sheet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spreadsheet_Sheet__Sheet", None)
        self.__Sheet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Spreadsheet"):
                opp_val = getattr(old_value, "Spreadsheet", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Spreadsheet"):
                opp_val = getattr(value, "Spreadsheet", None)
                if opp_val is None:
                    setattr(value, "Spreadsheet", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Sheet12(self):
        return self.__Sheet12

    @Sheet12.setter
    def Sheet12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spreadsheet_Sheet__Sheet12", None)
        self.__Sheet12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Row11"):
                opp_val = getattr(old_value, "Row11", None)
                if opp_val == self:
                    setattr(old_value, "Row11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Row11"):
                opp_val = getattr(value, "Row11", None)
                setattr(value, "Row11", self)

    @property
    def Sheet4(self):
        return self.__Sheet4

    @Sheet4.setter
    def Sheet4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spreadsheet_Sheet__Sheet4", None)
        self.__Sheet4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Column"):
                    opp_val = getattr(item, "Column", None)
                    
                    if opp_val == self:
                        setattr(item, "Column", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Column"):
                    opp_val = getattr(item, "Column", None)
                    
                    setattr(item, "Column", self)
                    

    @property
    def Sheet18(self):
        return self.__Sheet18

    @Sheet18.setter
    def Sheet18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spreadsheet_Sheet__Sheet18", None)
        self.__Sheet18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Column17"):
                opp_val = getattr(old_value, "Column17", None)
                if opp_val == self:
                    setattr(old_value, "Column17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Column17"):
                opp_val = getattr(value, "Column17", None)
                setattr(value, "Column17", self)

    def getColumn(self, spreadsheet_columnindex) :
        # TODO: Implement getColumn method
        pass

    def getRow(self, spreadsheet_rowindex) :
        # TODO: Implement getRow method
        pass

class spreadsheet_Spreadsheet(ABC):

    def __init__(self, FilePath: str, Label: str, Spreadsheet: set["spreadsheet_Sheet"] = None, Spreadsheet7: "spreadsheet_Sheet" = None):
        self.FilePath = FilePath
        self.Label = Label
        self.Spreadsheet = Spreadsheet if Spreadsheet is not None else set()
        self.Spreadsheet7 = Spreadsheet7
        
        pass
    @property
    def Label(self):
        return self.__Label

    @Label.setter
    def Label(self, Label: str):
        self.__Label = Label


    @property
    def FilePath(self):
        return self.__FilePath

    @FilePath.setter
    def FilePath(self, FilePath: str):
        self.__FilePath = FilePath


    @property
    def Spreadsheet(self):
        return self.__Spreadsheet

    @Spreadsheet.setter
    def Spreadsheet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spreadsheet_Spreadsheet__Spreadsheet", None)
        self.__Spreadsheet = value if value is not None else set()
        
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
                    

    @property
    def Spreadsheet7(self):
        return self.__Spreadsheet7

    @Spreadsheet7.setter
    def Spreadsheet7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spreadsheet_Spreadsheet__Spreadsheet7", None)
        self.__Spreadsheet7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Sheet6"):
                opp_val = getattr(old_value, "Sheet6", None)
                if opp_val == self:
                    setattr(old_value, "Sheet6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Sheet6"):
                opp_val = getattr(value, "Sheet6", None)
                setattr(value, "Sheet6", self)

    def readFile(self):
        # TODO: Implement readFile method
        pass

    def getSheet(self, spreadsheet_sheetindex) :
        # TODO: Implement getSheet method
        pass
