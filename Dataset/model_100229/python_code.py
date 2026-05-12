from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class SpreadsheetMLSimplified_Data:

    pass
class ColOrRowElement:

    pass
class SpreadsheetMLSimplified_Row(ColOrRowElement):

    def __init__(self, autoFitHeight: str, height: str, c_row: set["Cell"] = None, t_rows: "Table" = None):
        self.autoFitHeight = autoFitHeight
        self.height = height
        self.c_row = c_row if c_row is not None else set()
        self.t_rows = t_rows
        
        pass
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height: str):
        self.__height = height


    @property
    def autoFitHeight(self):
        return self.__autoFitHeight

    @autoFitHeight.setter
    def autoFitHeight(self, autoFitHeight: str):
        self.__autoFitHeight = autoFitHeight


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
                    

class SpreadsheetMLSimplified_Column(ColOrRowElement):

    def __init__(self, autoFitWidth: str, width: str, t_cols: "Table" = None):
        self.autoFitWidth = autoFitWidth
        self.width = width
        self.t_cols = t_cols
        
        pass
    @property
    def autoFitWidth(self):
        return self.__autoFitWidth

    @autoFitWidth.setter
    def autoFitWidth(self, autoFitWidth: str):
        self.__autoFitWidth = autoFitWidth


    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width


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

class Cell:

    pass
class SpreadsheetMLSimplified_TableElement(ABC):

    def __init__(self, index: str):
        self.index = index
        
        pass
    @property
    def index(self):
        return self.__index

    @index.setter
    def index(self, index: str):
        self.__index = index


class SpreadsheetMLSimplified_Worksheet:

    def __init__(self, name: str, wb_worksheets: "Workbook" = None, t_worksheet: "Table" = None):
        self.name = name
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

class Row:

    pass
class Column:

    pass
class SpreadsheetMLSimplified_Table:

    pass
class Table:

    pass
class TableElement:

    pass
class SpreadsheetMLSimplified_Cell(TableElement):

    def __init__(self, arrayRange: str, formula: str, hRef: str, mergeAcross: str, mergeDown: str, d_cell: "Data" = None, r_cells: "Row" = None):
        self.arrayRange = arrayRange
        self.formula = formula
        self.hRef = hRef
        self.mergeAcross = mergeAcross
        self.mergeDown = mergeDown
        self.d_cell = d_cell
        self.r_cells = r_cells
        
        pass
    @property
    def arrayRange(self):
        return self.__arrayRange

    @arrayRange.setter
    def arrayRange(self, arrayRange: str):
        self.__arrayRange = arrayRange


    @property
    def mergeAcross(self):
        return self.__mergeAcross

    @mergeAcross.setter
    def mergeAcross(self, mergeAcross: str):
        self.__mergeAcross = mergeAcross


    @property
    def hRef(self):
        return self.__hRef

    @hRef.setter
    def hRef(self, hRef: str):
        self.__hRef = hRef


    @property
    def formula(self):
        return self.__formula

    @formula.setter
    def formula(self, formula: str):
        self.__formula = formula


    @property
    def mergeDown(self):
        return self.__mergeDown

    @mergeDown.setter
    def mergeDown(self, mergeDown: str):
        self.__mergeDown = mergeDown


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

    def __init__(self, hidden: str, span: str):
        self.hidden = hidden
        self.span = span
        
        pass
    @property
    def hidden(self):
        return self.__hidden

    @hidden.setter
    def hidden(self, hidden: str):
        self.__hidden = hidden


    @property
    def span(self):
        return self.__span

    @span.setter
    def span(self, span: str):
        self.__span = span


class Workbook:

    pass
class Worksheet:

    pass
class SpreadsheetMLSimplified_Workbook:

    pass
class DateTimeType:

    pass
class ValueType:

    pass
class SpreadsheetMLSimplified_BooleanValue(ValueType):

    def __init__(self, value: str, ValueType: "SpreadsheetMLSimplified_Data" = None):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class SpreadsheetMLSimplified_NumberValue(ValueType):

    def __init__(self, value: str, ValueType: "SpreadsheetMLSimplified_Data" = None):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class SpreadsheetMLSimplified_ErrorValue(ValueType):

    pass
class SpreadsheetMLSimplified_DateTimeTypeValue(ValueType):

    pass
class SpreadsheetMLSimplified_StringValue(ValueType):

    def __init__(self, value: str, ValueType: "SpreadsheetMLSimplified_Data" = None):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class Data:

    pass
class SpreadsheetMLSimplified_ValueType(ABC):

    pass
class SpreadsheetMLSimplified_DateTimeType:

    def __init__(self, month: str, day: str, hour: str, minute: str, second: str, year: str):
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second
        self.year = year
        
        pass
    @property
    def second(self):
        return self.__second

    @second.setter
    def second(self, second: str):
        self.__second = second


    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year: str):
        self.__year = year


    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, month: str):
        self.__month = month


    @property
    def minute(self):
        return self.__minute

    @minute.setter
    def minute(self, minute: str):
        self.__minute = minute


    @property
    def hour(self):
        return self.__hour

    @hour.setter
    def hour(self, hour: str):
        self.__hour = hour


    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, day: str):
        self.__day = day

