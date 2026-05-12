from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class ValueType:

    pass
class NumberValue(ValueType):

    def __init__(self, value: float, ValueType: "Data" = None):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value


class StringValue(ValueType):

    def __init__(self, value: str, ValueType: "Data" = None):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class BooleanValue(ValueType):

    def __init__(self, value: bool, ValueType: "Data" = None):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value


class Data:

    pass
class ErrorValue(ValueType):

    pass
class TableElement:

    def __init__(self, index: int):
        self.index = index
        
        pass
    @property
    def index(self):
        return self.__index

    @index.setter
    def index(self, index: int):
        self.__index = index


class Cell(TableElement):

    def __init__(self, formula: str, index: int, Cell: "Row" = None, Cell10: set["Data"] = None):
        super().__init__(index)
        self.formula = formula
        self.Cell = Cell
        self.Cell10 = Cell10 if Cell10 is not None else set()
        
        pass
    @property
    def formula(self):
        return self.__formula

    @formula.setter
    def formula(self, formula: str):
        self.__formula = formula


    @property
    def Cell(self):
        return self.__Cell

    @Cell.setter
    def Cell(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cell__Cell", None)
        self.__Cell = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Row8"):
                opp_val = getattr(old_value, "Row8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Row8"):
                opp_val = getattr(value, "Row8", None)
                if opp_val is None:
                    setattr(value, "Row8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Cell10(self):
        return self.__Cell10

    @Cell10.setter
    def Cell10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cell__Cell10", None)
        self.__Cell10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Data"):
                    opp_val = getattr(item, "Data", None)
                    
                    if opp_val == self:
                        setattr(item, "Data", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Data"):
                    opp_val = getattr(item, "Data", None)
                    
                    setattr(item, "Data", self)
                    

class ColOrRowElement(TableElement):

    def __init__(self, span: int, hidden: bool, index: int):
        super().__init__(index)
        self.span = span
        self.hidden = hidden
        
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


class Row(ColOrRowElement):

    def __init__(self, span: int, hidden: bool, index: int, Row: "Table" = None, Row8: set["Cell"] = None):
        super().__init__(span, hidden, index)
        self.Row = Row
        self.Row8 = Row8 if Row8 is not None else set()
        
        pass
    @property
    def Row(self):
        return self.__Row

    @Row.setter
    def Row(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Row__Row", None)
        self.__Row = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Table6"):
                opp_val = getattr(old_value, "Table6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Table6"):
                opp_val = getattr(value, "Table6", None)
                if opp_val is None:
                    setattr(value, "Table6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Row8(self):
        return self.__Row8

    @Row8.setter
    def Row8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Row__Row8", None)
        self.__Row8 = value if value is not None else set()
        
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
                    

class Column(ColOrRowElement):

    def __init__(self, span: int, hidden: bool, index: int, Column: "Table" = None):
        super().__init__(span, hidden, index)
        self.Column = Column
        
        pass
    @property
    def Column(self):
        return self.__Column

    @Column.setter
    def Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Column__Column", None)
        self.__Column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Table4"):
                opp_val = getattr(old_value, "Table4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Table4"):
                opp_val = getattr(value, "Table4", None)
                if opp_val is None:
                    setattr(value, "Table4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Table:

    pass
class Worksheet:

    def __init__(self, name: str, Worksheet: "Workbook" = None, Worksheet2: "Table" = None):
        self.name = name
        self.Worksheet = Worksheet
        self.Worksheet2 = Worksheet2
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def Worksheet2(self):
        return self.__Worksheet2

    @Worksheet2.setter
    def Worksheet2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Worksheet__Worksheet2", None)
        self.__Worksheet2 = value
        
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

    @property
    def Worksheet(self):
        return self.__Worksheet

    @Worksheet.setter
    def Worksheet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Worksheet__Worksheet", None)
        self.__Worksheet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Workbook"):
                opp_val = getattr(old_value, "Workbook", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Workbook"):
                opp_val = getattr(value, "Workbook", None)
                if opp_val is None:
                    setattr(value, "Workbook", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Workbook:

    pass