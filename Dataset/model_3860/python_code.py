from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class NamedElement:

    pass
class table_Column(NamedElement):

    def __init__(self, type: str, table_Column: "table_Table" = None, table_Column3: "table_Table" = None):
        self.type = type
        self.table_Column = table_Column
        self.table_Column3 = table_Column3
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def table_Column(self):
        return self.__table_Column

    @table_Column.setter
    def table_Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_Column__table_Column", None)
        self.__table_Column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "table_Table"):
                opp_val = getattr(old_value, "table_Table", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "table_Table"):
                opp_val = getattr(value, "table_Table", None)
                if opp_val is None:
                    setattr(value, "table_Table", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def table_Column3(self):
        return self.__table_Column3

    @table_Column3.setter
    def table_Column3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_table_Column__table_Column3", None)
        self.__table_Column3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "table_Table2"):
                opp_val = getattr(old_value, "table_Table2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "table_Table2"):
                opp_val = getattr(value, "table_Table2", None)
                if opp_val is None:
                    setattr(value, "table_Table2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class table_Table(NamedElement):

    pass
class table_NamedElement:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name
