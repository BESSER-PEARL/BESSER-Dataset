from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Element:

    pass
class sql_Column(Element):

    def __init__(self, type: str, Column: "sql_Table" = None, column: "sql_Table" = None, sql_Column: "sql_Table" = None, sql_Column4: "sql_Table" = None):
        self.type = type
        self.Column = Column
        self.column = column
        self.sql_Column = sql_Column
        self.sql_Column4 = sql_Column4
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def column(self):
        return self.__column

    @column.setter
    def column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_Column__column", None)
        self.__column = value
        
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
    def sql_Column(self):
        return self.__sql_Column

    @sql_Column.setter
    def sql_Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_Column__sql_Column", None)
        self.__sql_Column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_Table"):
                opp_val = getattr(old_value, "sql_Table", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Table"):
                opp_val = getattr(value, "sql_Table", None)
                if opp_val is None:
                    setattr(value, "sql_Table", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Column(self):
        return self.__Column

    @Column.setter
    def Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_Column__Column", None)
        self.__Column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owner"):
                opp_val = getattr(old_value, "owner", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner"):
                opp_val = getattr(value, "owner", None)
                if opp_val is None:
                    setattr(value, "owner", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sql_Column4(self):
        return self.__sql_Column4

    @sql_Column4.setter
    def sql_Column4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_Column__sql_Column4", None)
        self.__sql_Column4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_Table3"):
                opp_val = getattr(old_value, "sql_Table3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Table3"):
                opp_val = getattr(value, "sql_Table3", None)
                if opp_val is None:
                    setattr(value, "sql_Table3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sql_Table(Element):

    pass
class sql_Element:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name
