from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class AbstractDataType:

    pass
class dbDsl_NumberType(AbstractDataType):

    pass
class dbDsl_CharType(AbstractDataType):

    pass
class dbDsl_Column:

    def __init__(self, name: str, dbDsl_Column4: "dbDsl_AbstractDataType" = None, dbDsl_Column6: "dbDsl_AbstractColumnMapper" = None, dbDsl_Column: "dbDsl_Table" = None):
        self.name = name
        self.dbDsl_Column4 = dbDsl_Column4
        self.dbDsl_Column6 = dbDsl_Column6
        self.dbDsl_Column = dbDsl_Column
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dbDsl_Column(self):
        return self.__dbDsl_Column

    @dbDsl_Column.setter
    def dbDsl_Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbDsl_Column__dbDsl_Column", None)
        self.__dbDsl_Column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbDsl_Table2"):
                opp_val = getattr(old_value, "dbDsl_Table2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbDsl_Table2"):
                opp_val = getattr(value, "dbDsl_Table2", None)
                if opp_val is None:
                    setattr(value, "dbDsl_Table2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dbDsl_Column4(self):
        return self.__dbDsl_Column4

    @dbDsl_Column4.setter
    def dbDsl_Column4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbDsl_Column__dbDsl_Column4", None)
        self.__dbDsl_Column4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbDsl_AbstractDataType"):
                opp_val = getattr(old_value, "dbDsl_AbstractDataType", None)
                if opp_val == self:
                    setattr(old_value, "dbDsl_AbstractDataType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbDsl_AbstractDataType"):
                opp_val = getattr(value, "dbDsl_AbstractDataType", None)
                setattr(value, "dbDsl_AbstractDataType", self)

    @property
    def dbDsl_Column6(self):
        return self.__dbDsl_Column6

    @dbDsl_Column6.setter
    def dbDsl_Column6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbDsl_Column__dbDsl_Column6", None)
        self.__dbDsl_Column6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbDsl_AbstractColumnMapper"):
                opp_val = getattr(old_value, "dbDsl_AbstractColumnMapper", None)
                if opp_val == self:
                    setattr(old_value, "dbDsl_AbstractColumnMapper", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbDsl_AbstractColumnMapper"):
                opp_val = getattr(value, "dbDsl_AbstractColumnMapper", None)
                setattr(value, "dbDsl_AbstractColumnMapper", self)

class dbDsl_Table:

    def __init__(self, name: str, dbDsl_Table: "dbDsl_Database" = None, dbDsl_Table2: set["dbDsl_Column"] = None):
        self.name = name
        self.dbDsl_Table = dbDsl_Table
        self.dbDsl_Table2 = dbDsl_Table2 if dbDsl_Table2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dbDsl_Table2(self):
        return self.__dbDsl_Table2

    @dbDsl_Table2.setter
    def dbDsl_Table2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbDsl_Table__dbDsl_Table2", None)
        self.__dbDsl_Table2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dbDsl_Column"):
                    opp_val = getattr(item, "dbDsl_Column", None)
                    
                    if opp_val == self:
                        setattr(item, "dbDsl_Column", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dbDsl_Column"):
                    opp_val = getattr(item, "dbDsl_Column", None)
                    
                    setattr(item, "dbDsl_Column", self)
                    

    @property
    def dbDsl_Table(self):
        return self.__dbDsl_Table

    @dbDsl_Table.setter
    def dbDsl_Table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbDsl_Table__dbDsl_Table", None)
        self.__dbDsl_Table = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbDsl_Database"):
                opp_val = getattr(old_value, "dbDsl_Database", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbDsl_Database"):
                opp_val = getattr(value, "dbDsl_Database", None)
                if opp_val is None:
                    setattr(value, "dbDsl_Database", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Root:

    pass
class dbDsl_Database(Root):

    def __init__(self, name: str, dbDsl_Database: set["dbDsl_Table"] = None):
        self.name = name
        self.dbDsl_Database = dbDsl_Database if dbDsl_Database is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dbDsl_Database(self):
        return self.__dbDsl_Database

    @dbDsl_Database.setter
    def dbDsl_Database(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbDsl_Database__dbDsl_Database", None)
        self.__dbDsl_Database = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dbDsl_Table"):
                    opp_val = getattr(item, "dbDsl_Table", None)
                    
                    if opp_val == self:
                        setattr(item, "dbDsl_Table", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dbDsl_Table"):
                    opp_val = getattr(item, "dbDsl_Table", None)
                    
                    setattr(item, "dbDsl_Table", self)
                    

class dbDsl_Root:

    pass
class dbDsl_AbstractColumnMapper:

    pass
class dbDsl_AbstractDataType:

    pass