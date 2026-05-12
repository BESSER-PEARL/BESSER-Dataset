from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class RDBMS_Column:

    def __init__(self, name: str, RDBMS_ecoreColumn: "RDBMS_Table" = None, columns: "RDBMS_Table" = None, RDBMS_Column: "RDBMS_FKey" = None, RDBMS_Column16: "RDBMS_PKey" = None):
        self.name = name
        self.RDBMS_ecoreColumn = RDBMS_ecoreColumn
        self.columns = columns
        self.RDBMS_Column = RDBMS_Column
        self.RDBMS_Column16 = RDBMS_Column16
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def RDBMS_Column(self):
        return self.__RDBMS_Column

    @RDBMS_Column.setter
    def RDBMS_Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RDBMS_Column__RDBMS_Column", None)
        self.__RDBMS_Column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RDBMS_FKey11"):
                opp_val = getattr(old_value, "RDBMS_FKey11", None)
                if opp_val == self:
                    setattr(old_value, "RDBMS_FKey11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RDBMS_FKey11"):
                opp_val = getattr(value, "RDBMS_FKey11", None)
                setattr(value, "RDBMS_FKey11", self)

    @property
    def columns(self):
        return self.__columns

    @columns.setter
    def columns(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RDBMS_Column__columns", None)
        self.__columns = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RDBMS_ecoreTable7"):
                opp_val = getattr(old_value, "RDBMS_ecoreTable7", None)
                if opp_val == self:
                    setattr(old_value, "RDBMS_ecoreTable7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RDBMS_ecoreTable7"):
                opp_val = getattr(value, "RDBMS_ecoreTable7", None)
                setattr(value, "RDBMS_ecoreTable7", self)

    @property
    def RDBMS_Column16(self):
        return self.__RDBMS_Column16

    @RDBMS_Column16.setter
    def RDBMS_Column16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RDBMS_Column__RDBMS_Column16", None)
        self.__RDBMS_Column16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RDBMS_PKey15"):
                opp_val = getattr(old_value, "RDBMS_PKey15", None)
                if opp_val == self:
                    setattr(old_value, "RDBMS_PKey15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RDBMS_PKey15"):
                opp_val = getattr(value, "RDBMS_PKey15", None)
                setattr(value, "RDBMS_PKey15", self)

    @property
    def RDBMS_ecoreColumn(self):
        return self.__RDBMS_ecoreColumn

    @RDBMS_ecoreColumn.setter
    def RDBMS_ecoreColumn(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RDBMS_Column__RDBMS_ecoreColumn", None)
        self.__RDBMS_ecoreColumn = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "table"):
                opp_val = getattr(old_value, "table", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "table"):
                opp_val = getattr(value, "table", None)
                if opp_val is None:
                    setattr(value, "table", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def setTable(self, RDBMS_n):
        # TODO: Implement setTable method
        pass

    def setName(self, RDBMS_n):
        # TODO: Implement setName method
        pass

class RDBMS_FKey:

    pass
class RDBMS_Table:

    def __init__(self, name: str, RDBMS_ecoreTable: "RDBMS_Scheme" = None, table: set["RDBMS_Column"] = None, tables: "RDBMS_Scheme" = None, RDBMS_Table: "RDBMS_PKey" = None, RDBMS_ecoreTable7: "RDBMS_Column" = None):
        self.name = name
        self.RDBMS_ecoreTable = RDBMS_ecoreTable
        self.table = table if table is not None else set()
        self.tables = tables
        self.RDBMS_Table = RDBMS_Table
        self.RDBMS_ecoreTable7 = RDBMS_ecoreTable7
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def RDBMS_Table(self):
        return self.__RDBMS_Table

    @RDBMS_Table.setter
    def RDBMS_Table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RDBMS_Table__RDBMS_Table", None)
        self.__RDBMS_Table = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RDBMS_PKey"):
                opp_val = getattr(old_value, "RDBMS_PKey", None)
                if opp_val == self:
                    setattr(old_value, "RDBMS_PKey", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RDBMS_PKey"):
                opp_val = getattr(value, "RDBMS_PKey", None)
                setattr(value, "RDBMS_PKey", self)

    @property
    def table(self):
        return self.__table

    @table.setter
    def table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RDBMS_Table__table", None)
        self.__table = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RDBMS_ecoreColumn"):
                    opp_val = getattr(item, "RDBMS_ecoreColumn", None)
                    
                    if opp_val == self:
                        setattr(item, "RDBMS_ecoreColumn", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RDBMS_ecoreColumn"):
                    opp_val = getattr(item, "RDBMS_ecoreColumn", None)
                    
                    setattr(item, "RDBMS_ecoreColumn", self)
                    

    @property
    def tables(self):
        return self.__tables

    @tables.setter
    def tables(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RDBMS_Table__tables", None)
        self.__tables = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RDBMS_ecoreScheme"):
                opp_val = getattr(old_value, "RDBMS_ecoreScheme", None)
                if opp_val == self:
                    setattr(old_value, "RDBMS_ecoreScheme", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RDBMS_ecoreScheme"):
                opp_val = getattr(value, "RDBMS_ecoreScheme", None)
                setattr(value, "RDBMS_ecoreScheme", self)

    @property
    def RDBMS_ecoreTable(self):
        return self.__RDBMS_ecoreTable

    @RDBMS_ecoreTable.setter
    def RDBMS_ecoreTable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RDBMS_Table__RDBMS_ecoreTable", None)
        self.__RDBMS_ecoreTable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scheme"):
                opp_val = getattr(old_value, "scheme", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scheme"):
                opp_val = getattr(value, "scheme", None)
                if opp_val is None:
                    setattr(value, "scheme", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def RDBMS_ecoreTable7(self):
        return self.__RDBMS_ecoreTable7

    @RDBMS_ecoreTable7.setter
    def RDBMS_ecoreTable7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RDBMS_Table__RDBMS_ecoreTable7", None)
        self.__RDBMS_ecoreTable7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "columns"):
                opp_val = getattr(old_value, "columns", None)
                if opp_val == self:
                    setattr(old_value, "columns", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "columns"):
                opp_val = getattr(value, "columns", None)
                setattr(value, "columns", self)

    def setName(self, RDBMS_n):
        # TODO: Implement setName method
        pass

    def remColumn(self, RDBMS_n):
        # TODO: Implement remColumn method
        pass

    def addColumn(self, RDBMS_n):
        # TODO: Implement addColumn method
        pass

class RDBMS_Scheme:

    def __init__(self, name: str, scheme: set["RDBMS_Table"] = None, scheme2: set["RDBMS_FKey"] = None, RDBMS_ecoreScheme: "RDBMS_Table" = None, RDBMS_ecoreScheme13: "RDBMS_FKey" = None):
        self.name = name
        self.scheme = scheme if scheme is not None else set()
        self.scheme2 = scheme2 if scheme2 is not None else set()
        self.RDBMS_ecoreScheme = RDBMS_ecoreScheme
        self.RDBMS_ecoreScheme13 = RDBMS_ecoreScheme13
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def RDBMS_ecoreScheme13(self):
        return self.__RDBMS_ecoreScheme13

    @RDBMS_ecoreScheme13.setter
    def RDBMS_ecoreScheme13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RDBMS_Scheme__RDBMS_ecoreScheme13", None)
        self.__RDBMS_ecoreScheme13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "keys"):
                opp_val = getattr(old_value, "keys", None)
                if opp_val == self:
                    setattr(old_value, "keys", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "keys"):
                opp_val = getattr(value, "keys", None)
                setattr(value, "keys", self)

    @property
    def RDBMS_ecoreScheme(self):
        return self.__RDBMS_ecoreScheme

    @RDBMS_ecoreScheme.setter
    def RDBMS_ecoreScheme(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RDBMS_Scheme__RDBMS_ecoreScheme", None)
        self.__RDBMS_ecoreScheme = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tables"):
                opp_val = getattr(old_value, "tables", None)
                if opp_val == self:
                    setattr(old_value, "tables", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tables"):
                opp_val = getattr(value, "tables", None)
                setattr(value, "tables", self)

    @property
    def scheme2(self):
        return self.__scheme2

    @scheme2.setter
    def scheme2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RDBMS_Scheme__scheme2", None)
        self.__scheme2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RDBMS_ecoreFKey"):
                    opp_val = getattr(item, "RDBMS_ecoreFKey", None)
                    
                    if opp_val == self:
                        setattr(item, "RDBMS_ecoreFKey", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RDBMS_ecoreFKey"):
                    opp_val = getattr(item, "RDBMS_ecoreFKey", None)
                    
                    setattr(item, "RDBMS_ecoreFKey", self)
                    

    @property
    def scheme(self):
        return self.__scheme

    @scheme.setter
    def scheme(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RDBMS_Scheme__scheme", None)
        self.__scheme = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RDBMS_ecoreTable"):
                    opp_val = getattr(item, "RDBMS_ecoreTable", None)
                    
                    if opp_val == self:
                        setattr(item, "RDBMS_ecoreTable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RDBMS_ecoreTable"):
                    opp_val = getattr(item, "RDBMS_ecoreTable", None)
                    
                    setattr(item, "RDBMS_ecoreTable", self)
                    

    def remTable(self, RDBMS_n):
        # TODO: Implement remTable method
        pass

    def addTable(self, RDBMS_n):
        # TODO: Implement addTable method
        pass

    def setName(self, RDBMS_n):
        # TODO: Implement setName method
        pass

class RDBMS_PKey:

    pass