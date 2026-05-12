from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class ColOrRowElement:

    pass
class SpreadsheetMLSimplified_Table:

    pass
class TableElement:

    pass
class SpreadsheetMLSimplified_Cell(TableElement):

    def __init__(self, arrayRange: str, formula: str, hRef: str, mergeAcross: float, mergeDown: float, Cell: "SpreadsheetMLSimplified_Row" = None, r_cells: "SpreadsheetMLSimplified_Row" = None, d_cell: "SpreadsheetMLSimplified_Data" = None, Cell19: "SpreadsheetMLSimplified_Data" = None):
        self.arrayRange = arrayRange
        self.formula = formula
        self.hRef = hRef
        self.mergeAcross = mergeAcross
        self.mergeDown = mergeDown
        self.Cell = Cell
        self.r_cells = r_cells
        self.d_cell = d_cell
        self.Cell19 = Cell19
        
        pass
    @property
    def mergeDown(self):
        return self.__mergeDown

    @mergeDown.setter
    def mergeDown(self, mergeDown: float):
        self.__mergeDown = mergeDown


    @property
    def mergeAcross(self):
        return self.__mergeAcross

    @mergeAcross.setter
    def mergeAcross(self, mergeAcross: float):
        self.__mergeAcross = mergeAcross


    @property
    def arrayRange(self):
        return self.__arrayRange

    @arrayRange.setter
    def arrayRange(self, arrayRange: str):
        self.__arrayRange = arrayRange


    @property
    def formula(self):
        return self.__formula

    @formula.setter
    def formula(self, formula: str):
        self.__formula = formula


    @property
    def hRef(self):
        return self.__hRef

    @hRef.setter
    def hRef(self, hRef: str):
        self.__hRef = hRef


    @property
    def d_cell(self):
        return self.__d_cell

    @d_cell.setter
    def d_cell(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLSimplified_Cell__d_cell", None)
        self.__d_cell = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Data17"):
                opp_val = getattr(old_value, "Data17", None)
                if opp_val == self:
                    setattr(old_value, "Data17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Data17"):
                opp_val = getattr(value, "Data17", None)
                setattr(value, "Data17", self)

    @property
    def Cell(self):
        return self.__Cell

    @Cell.setter
    def Cell(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLSimplified_Cell__Cell", None)
        self.__Cell = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "c_row"):
                opp_val = getattr(old_value, "c_row", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "c_row"):
                opp_val = getattr(value, "c_row", None)
                if opp_val is None:
                    setattr(value, "c_row", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Cell19(self):
        return self.__Cell19

    @Cell19.setter
    def Cell19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLSimplified_Cell__Cell19", None)
        self.__Cell19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "c_data"):
                opp_val = getattr(old_value, "c_data", None)
                if opp_val == self:
                    setattr(old_value, "c_data", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "c_data"):
                opp_val = getattr(value, "c_data", None)
                setattr(value, "c_data", self)

    @property
    def r_cells(self):
        return self.__r_cells

    @r_cells.setter
    def r_cells(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLSimplified_Cell__r_cells", None)
        self.__r_cells = value
        
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

class SpreadsheetMLSimplified_ColOrRowElement(TableElement):

    def __init__(self, hidden: bool, span: int):
        self.hidden = hidden
        self.span = span
        
        pass
    @property
    def hidden(self):
        return self.__hidden

    @hidden.setter
    def hidden(self, hidden: bool):
        self.__hidden = hidden


    @property
    def span(self):
        return self.__span

    @span.setter
    def span(self, span: int):
        self.__span = span


class SpreadsheetMLSimplified_TableElement(ABC):

    def __init__(self, index: int):
        self.index = index
        
        pass
    @property
    def index(self):
        return self.__index

    @index.setter
    def index(self, index: int):
        self.__index = index


class SpreadsheetMLSimplified_Row(ColOrRowElement):

    def __init__(self, autoFitHeight: bool, height: float, Row: "SpreadsheetMLSimplified_Table" = None, t_rows: "SpreadsheetMLSimplified_Table" = None, c_row: set["SpreadsheetMLSimplified_Cell"] = None, Row15: "SpreadsheetMLSimplified_Cell" = None):
        self.autoFitHeight = autoFitHeight
        self.height = height
        self.Row = Row
        self.t_rows = t_rows
        self.c_row = c_row if c_row is not None else set()
        self.Row15 = Row15
        
        pass
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height: float):
        self.__height = height


    @property
    def autoFitHeight(self):
        return self.__autoFitHeight

    @autoFitHeight.setter
    def autoFitHeight(self, autoFitHeight: bool):
        self.__autoFitHeight = autoFitHeight


    @property
    def Row15(self):
        return self.__Row15

    @Row15.setter
    def Row15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLSimplified_Row__Row15", None)
        self.__Row15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r_cells"):
                opp_val = getattr(old_value, "r_cells", None)
                if opp_val == self:
                    setattr(old_value, "r_cells", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r_cells"):
                opp_val = getattr(value, "r_cells", None)
                setattr(value, "r_cells", self)

    @property
    def c_row(self):
        return self.__c_row

    @c_row.setter
    def c_row(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLSimplified_Row__c_row", None)
        self.__c_row = value if value is not None else set()
        
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
    def Row(self):
        return self.__Row

    @Row.setter
    def Row(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLSimplified_Row__Row", None)
        self.__Row = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r_table"):
                opp_val = getattr(old_value, "r_table", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r_table"):
                opp_val = getattr(value, "r_table", None)
                if opp_val is None:
                    setattr(value, "r_table", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def t_rows(self):
        return self.__t_rows

    @t_rows.setter
    def t_rows(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLSimplified_Row__t_rows", None)
        self.__t_rows = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Table12"):
                opp_val = getattr(old_value, "Table12", None)
                if opp_val == self:
                    setattr(old_value, "Table12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Table12"):
                opp_val = getattr(value, "Table12", None)
                setattr(value, "Table12", self)

class SpreadsheetMLSimplified_Column(ColOrRowElement):

    def __init__(self, autoFitWidth: bool, width: float, Column: "SpreadsheetMLSimplified_Table" = None, t_cols: "SpreadsheetMLSimplified_Table" = None):
        self.autoFitWidth = autoFitWidth
        self.width = width
        self.Column = Column
        self.t_cols = t_cols
        
        pass
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width: float):
        self.__width = width


    @property
    def autoFitWidth(self):
        return self.__autoFitWidth

    @autoFitWidth.setter
    def autoFitWidth(self, autoFitWidth: bool):
        self.__autoFitWidth = autoFitWidth


    @property
    def Column(self):
        return self.__Column

    @Column.setter
    def Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLSimplified_Column__Column", None)
        self.__Column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "c_table"):
                opp_val = getattr(old_value, "c_table", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "c_table"):
                opp_val = getattr(value, "c_table", None)
                if opp_val is None:
                    setattr(value, "c_table", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def t_cols(self):
        return self.__t_cols

    @t_cols.setter
    def t_cols(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLSimplified_Column__t_cols", None)
        self.__t_cols = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Table10"):
                opp_val = getattr(old_value, "Table10", None)
                if opp_val == self:
                    setattr(old_value, "Table10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Table10"):
                opp_val = getattr(value, "Table10", None)
                setattr(value, "Table10", self)

class ValueType:

    pass
class SpreadsheetMLSimplified_NumberValue(ValueType):

    def __init__(self, value: float):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value


class SpreadsheetMLSimplified_StringValue(ValueType):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class SpreadsheetMLSimplified_Data:

    pass
class SpreadsheetMLSimplified_Worksheet:

    def __init__(self, name: str, Worksheet: "SpreadsheetMLSimplified_Workbook" = None, Worksheet6: "SpreadsheetMLSimplified_Table" = None, wb_worksheets: "SpreadsheetMLSimplified_Workbook" = None, t_worksheet: "SpreadsheetMLSimplified_Table" = None):
        self.name = name
        self.Worksheet = Worksheet
        self.Worksheet6 = Worksheet6
        self.wb_worksheets = wb_worksheets
        self.t_worksheet = t_worksheet
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def Worksheet6(self):
        return self.__Worksheet6

    @Worksheet6.setter
    def Worksheet6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLSimplified_Worksheet__Worksheet6", None)
        self.__Worksheet6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ws_table"):
                opp_val = getattr(old_value, "ws_table", None)
                if opp_val == self:
                    setattr(old_value, "ws_table", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ws_table"):
                opp_val = getattr(value, "ws_table", None)
                setattr(value, "ws_table", self)

    @property
    def Worksheet(self):
        return self.__Worksheet

    @Worksheet.setter
    def Worksheet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLSimplified_Worksheet__Worksheet", None)
        self.__Worksheet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ws_workbook"):
                opp_val = getattr(old_value, "ws_workbook", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ws_workbook"):
                opp_val = getattr(value, "ws_workbook", None)
                if opp_val is None:
                    setattr(value, "ws_workbook", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def wb_worksheets(self):
        return self.__wb_worksheets

    @wb_worksheets.setter
    def wb_worksheets(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLSimplified_Worksheet__wb_worksheets", None)
        self.__wb_worksheets = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Workbook"):
                opp_val = getattr(old_value, "Workbook", None)
                if opp_val == self:
                    setattr(old_value, "Workbook", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Workbook"):
                opp_val = getattr(value, "Workbook", None)
                setattr(value, "Workbook", self)

    @property
    def t_worksheet(self):
        return self.__t_worksheet

    @t_worksheet.setter
    def t_worksheet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLSimplified_Worksheet__t_worksheet", None)
        self.__t_worksheet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Table"):
                opp_val = getattr(old_value, "Table", None)
                if opp_val == self:
                    setattr(old_value, "Table", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Table"):
                opp_val = getattr(value, "Table", None)
                setattr(value, "Table", self)

class SpreadsheetMLSimplified_Workbook:

    pass
class SpreadsheetMLSimplified_ErrorValue(ValueType):

    pass
class SpreadsheetMLSimplified_BooleanValue(ValueType):

    def __init__(self, value: bool):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value


class SpreadsheetMLSimplified_DateTimeTypeValue(ValueType):

    pass
class SpreadsheetMLSimplified_ValueType(ABC):

    pass
class SpreadsheetMLSimplified_DateTimeType:

    def __init__(self, year: int, month: int, day: int, hour: int, minute: int, second: int, SpreadsheetMLSimplified_DateTimeType: "SpreadsheetMLSimplified_DateTimeTypeValue" = None):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second
        self.SpreadsheetMLSimplified_DateTimeType = SpreadsheetMLSimplified_DateTimeType
        
        pass
    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, day: int):
        self.__day = day


    @property
    def minute(self):
        return self.__minute

    @minute.setter
    def minute(self, minute: int):
        self.__minute = minute


    @property
    def second(self):
        return self.__second

    @second.setter
    def second(self, second: int):
        self.__second = second


    @property
    def hour(self):
        return self.__hour

    @hour.setter
    def hour(self, hour: int):
        self.__hour = hour


    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year: int):
        self.__year = year


    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, month: int):
        self.__month = month


    @property
    def SpreadsheetMLSimplified_DateTimeType(self):
        return self.__SpreadsheetMLSimplified_DateTimeType

    @SpreadsheetMLSimplified_DateTimeType.setter
    def SpreadsheetMLSimplified_DateTimeType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLSimplified_DateTimeType__SpreadsheetMLSimplified_DateTimeType", None)
        self.__SpreadsheetMLSimplified_DateTimeType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SpreadsheetMLSimplified_DateTimeTypeValue"):
                opp_val = getattr(old_value, "SpreadsheetMLSimplified_DateTimeTypeValue", None)
                if opp_val == self:
                    setattr(old_value, "SpreadsheetMLSimplified_DateTimeTypeValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SpreadsheetMLSimplified_DateTimeTypeValue"):
                opp_val = getattr(value, "SpreadsheetMLSimplified_DateTimeTypeValue", None)
                setattr(value, "SpreadsheetMLSimplified_DateTimeTypeValue", self)
