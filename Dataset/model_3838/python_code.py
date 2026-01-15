from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class BinaryCondition:

    pass
class sql4csv_OrCondition(BinaryCondition):

    pass
class sql4csv_AndCondition(BinaryCondition):

    pass
class sql4csv_ValueEquality:

    def __init__(self, right: str):
        self.right = right
        
    @property
    def right(self) -> str:
        return self.__right

    @right.setter
    def right(self, right: str):
        self.__right = right

class sql4csv_ColumnEquality:

    pass
class sql4csv_Table:

    def __init__(self, name: str, sql4csv_Table12: "sql4csv_Query" = None, sql4csv_Table17: "sql4csv_Column" = None, sql4csv_Table: "sql4csv_Query" = None):
        self.name = name
        self.sql4csv_Table12 = sql4csv_Table12
        self.sql4csv_Table17 = sql4csv_Table17
        self.sql4csv_Table = sql4csv_Table
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def sql4csv_Table12(self):
        return self.__sql4csv_Table12

    @sql4csv_Table12.setter
    def sql4csv_Table12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql4csv_Table__sql4csv_Table12", None)
        self.__sql4csv_Table12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql4csv_Query11"):
                opp_val = getattr(old_value, "sql4csv_Query11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql4csv_Query11"):
                opp_val = getattr(value, "sql4csv_Query11", None)
                if opp_val is None:
                    setattr(value, "sql4csv_Query11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sql4csv_Table(self):
        return self.__sql4csv_Table

    @sql4csv_Table.setter
    def sql4csv_Table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql4csv_Table__sql4csv_Table", None)
        self.__sql4csv_Table = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql4csv_Query9"):
                opp_val = getattr(old_value, "sql4csv_Query9", None)
                if opp_val == self:
                    setattr(old_value, "sql4csv_Query9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql4csv_Query9"):
                opp_val = getattr(value, "sql4csv_Query9", None)
                setattr(value, "sql4csv_Query9", self)

    @property
    def sql4csv_Table17(self):
        return self.__sql4csv_Table17

    @sql4csv_Table17.setter
    def sql4csv_Table17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql4csv_Table__sql4csv_Table17", None)
        self.__sql4csv_Table17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql4csv_Column16"):
                opp_val = getattr(old_value, "sql4csv_Column16", None)
                if opp_val == self:
                    setattr(old_value, "sql4csv_Column16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql4csv_Column16"):
                opp_val = getattr(value, "sql4csv_Column16", None)
                setattr(value, "sql4csv_Column16", self)

class sql4csv_EObject:

    pass
class Condition:

    pass
class sql4csv_BinaryCondition(Condition):

    pass
class sql4csv_Equality(Condition):

    pass
class sql4csv_Condition:

    pass
class sql4csv_Column:

    def __init__(self, name: str, sql4csv_Column: "sql4csv_Query" = None, sql4csv_Column16: "sql4csv_Table" = None, sql4csv_Column19: "sql4csv_Equality" = None, sql4csv_Column7: "sql4csv_Query" = None, sql4csv_Column28: "sql4csv_ColumnEquality" = None):
        self.name = name
        self.sql4csv_Column = sql4csv_Column
        self.sql4csv_Column16 = sql4csv_Column16
        self.sql4csv_Column19 = sql4csv_Column19
        self.sql4csv_Column7 = sql4csv_Column7
        self.sql4csv_Column28 = sql4csv_Column28
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def sql4csv_Column7(self):
        return self.__sql4csv_Column7

    @sql4csv_Column7.setter
    def sql4csv_Column7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql4csv_Column__sql4csv_Column7", None)
        self.__sql4csv_Column7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql4csv_Query6"):
                opp_val = getattr(old_value, "sql4csv_Query6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql4csv_Query6"):
                opp_val = getattr(value, "sql4csv_Query6", None)
                if opp_val is None:
                    setattr(value, "sql4csv_Query6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sql4csv_Column28(self):
        return self.__sql4csv_Column28

    @sql4csv_Column28.setter
    def sql4csv_Column28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql4csv_Column__sql4csv_Column28", None)
        self.__sql4csv_Column28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql4csv_ColumnEquality"):
                opp_val = getattr(old_value, "sql4csv_ColumnEquality", None)
                if opp_val == self:
                    setattr(old_value, "sql4csv_ColumnEquality", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql4csv_ColumnEquality"):
                opp_val = getattr(value, "sql4csv_ColumnEquality", None)
                setattr(value, "sql4csv_ColumnEquality", self)

    @property
    def sql4csv_Column16(self):
        return self.__sql4csv_Column16

    @sql4csv_Column16.setter
    def sql4csv_Column16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql4csv_Column__sql4csv_Column16", None)
        self.__sql4csv_Column16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql4csv_Table17"):
                opp_val = getattr(old_value, "sql4csv_Table17", None)
                if opp_val == self:
                    setattr(old_value, "sql4csv_Table17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql4csv_Table17"):
                opp_val = getattr(value, "sql4csv_Table17", None)
                setattr(value, "sql4csv_Table17", self)

    @property
    def sql4csv_Column(self):
        return self.__sql4csv_Column

    @sql4csv_Column.setter
    def sql4csv_Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql4csv_Column__sql4csv_Column", None)
        self.__sql4csv_Column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql4csv_Query4"):
                opp_val = getattr(old_value, "sql4csv_Query4", None)
                if opp_val == self:
                    setattr(old_value, "sql4csv_Query4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql4csv_Query4"):
                opp_val = getattr(value, "sql4csv_Query4", None)
                setattr(value, "sql4csv_Query4", self)

    @property
    def sql4csv_Column19(self):
        return self.__sql4csv_Column19

    @sql4csv_Column19.setter
    def sql4csv_Column19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql4csv_Column__sql4csv_Column19", None)
        self.__sql4csv_Column19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql4csv_Equality"):
                opp_val = getattr(old_value, "sql4csv_Equality", None)
                if opp_val == self:
                    setattr(old_value, "sql4csv_Equality", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql4csv_Equality"):
                opp_val = getattr(value, "sql4csv_Equality", None)
                setattr(value, "sql4csv_Equality", self)

class sql4csv_Query:

    pass
class sql4csv_Program:

    pass
class sql4csv_SQL4CSV:

    pass