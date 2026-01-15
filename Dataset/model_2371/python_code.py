from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class DataType(Enum):
    int = "int"
    varchar = "varchar"
    text = "text"
    unknown = "unknown"
    bool = "bool"
    decimal = "decimal"


############################################
# Definition of Classes
############################################

class DB_Column:

    def __init__(self, name: str, type: str, notNull: bool, DB_Column14: "DB_Key" = None, DB_Column17: set["DB_ForeignKey"] = None, DB_Column24: "DB_ForeignKey" = None, DB_Column: "DB_Table" = None, DB_Column11: "DB_Table" = None, DB_Column27: "DB_Key" = None):
        self.name = name
        self.type = type
        self.notNull = notNull
        self.DB_Column14 = DB_Column14
        self.DB_Column17 = DB_Column17 if DB_Column17 is not None else set()
        self.DB_Column24 = DB_Column24
        self.DB_Column = DB_Column
        self.DB_Column11 = DB_Column11
        self.DB_Column27 = DB_Column27
        
    @property
    def notNull(self) -> bool:
        return self.__notNull

    @notNull.setter
    def notNull(self, notNull: bool):
        self.__notNull = notNull

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def DB_Column27(self):
        return self.__DB_Column27

    @DB_Column27.setter
    def DB_Column27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DB_Column__DB_Column27", None)
        self.__DB_Column27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DB_Key26"):
                opp_val = getattr(old_value, "DB_Key26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DB_Key26"):
                opp_val = getattr(value, "DB_Key26", None)
                if opp_val is None:
                    setattr(value, "DB_Key26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def DB_Column24(self):
        return self.__DB_Column24

    @DB_Column24.setter
    def DB_Column24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DB_Column__DB_Column24", None)
        self.__DB_Column24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DB_ForeignKey23"):
                opp_val = getattr(old_value, "DB_ForeignKey23", None)
                if opp_val == self:
                    setattr(old_value, "DB_ForeignKey23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DB_ForeignKey23"):
                opp_val = getattr(value, "DB_ForeignKey23", None)
                setattr(value, "DB_ForeignKey23", self)

    @property
    def DB_Column11(self):
        return self.__DB_Column11

    @DB_Column11.setter
    def DB_Column11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DB_Column__DB_Column11", None)
        self.__DB_Column11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DB_Table12"):
                opp_val = getattr(old_value, "DB_Table12", None)
                if opp_val == self:
                    setattr(old_value, "DB_Table12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DB_Table12"):
                opp_val = getattr(value, "DB_Table12", None)
                setattr(value, "DB_Table12", self)

    @property
    def DB_Column(self):
        return self.__DB_Column

    @DB_Column.setter
    def DB_Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DB_Column__DB_Column", None)
        self.__DB_Column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DB_Table6"):
                opp_val = getattr(old_value, "DB_Table6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DB_Table6"):
                opp_val = getattr(value, "DB_Table6", None)
                if opp_val is None:
                    setattr(value, "DB_Table6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def DB_Column14(self):
        return self.__DB_Column14

    @DB_Column14.setter
    def DB_Column14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DB_Column__DB_Column14", None)
        self.__DB_Column14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DB_Key15"):
                opp_val = getattr(old_value, "DB_Key15", None)
                if opp_val == self:
                    setattr(old_value, "DB_Key15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DB_Key15"):
                opp_val = getattr(value, "DB_Key15", None)
                setattr(value, "DB_Key15", self)

    @property
    def DB_Column17(self):
        return self.__DB_Column17

    @DB_Column17.setter
    def DB_Column17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DB_Column__DB_Column17", None)
        self.__DB_Column17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DB_ForeignKey18"):
                    opp_val = getattr(item, "DB_ForeignKey18", None)
                    
                    if opp_val == self:
                        setattr(item, "DB_ForeignKey18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DB_ForeignKey18"):
                    opp_val = getattr(item, "DB_ForeignKey18", None)
                    
                    setattr(item, "DB_ForeignKey18", self)
                    

class DB_Key:

    def __init__(self, name: str, DB_Key: "DB_Table" = None, DB_Key15: "DB_Column" = None, DB_Key21: "DB_ForeignKey" = None, DB_Key26: set["DB_Column"] = None, DB_Key29: "DB_ForeignKey" = None):
        self.name = name
        self.DB_Key = DB_Key
        self.DB_Key15 = DB_Key15
        self.DB_Key21 = DB_Key21
        self.DB_Key26 = DB_Key26 if DB_Key26 is not None else set()
        self.DB_Key29 = DB_Key29
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def DB_Key21(self):
        return self.__DB_Key21

    @DB_Key21.setter
    def DB_Key21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DB_Key__DB_Key21", None)
        self.__DB_Key21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DB_ForeignKey20"):
                opp_val = getattr(old_value, "DB_ForeignKey20", None)
                if opp_val == self:
                    setattr(old_value, "DB_ForeignKey20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DB_ForeignKey20"):
                opp_val = getattr(value, "DB_ForeignKey20", None)
                setattr(value, "DB_ForeignKey20", self)

    @property
    def DB_Key(self):
        return self.__DB_Key

    @DB_Key.setter
    def DB_Key(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DB_Key__DB_Key", None)
        self.__DB_Key = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DB_Table4"):
                opp_val = getattr(old_value, "DB_Table4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DB_Table4"):
                opp_val = getattr(value, "DB_Table4", None)
                if opp_val is None:
                    setattr(value, "DB_Table4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def DB_Key29(self):
        return self.__DB_Key29

    @DB_Key29.setter
    def DB_Key29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DB_Key__DB_Key29", None)
        self.__DB_Key29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DB_ForeignKey30"):
                opp_val = getattr(old_value, "DB_ForeignKey30", None)
                if opp_val == self:
                    setattr(old_value, "DB_ForeignKey30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DB_ForeignKey30"):
                opp_val = getattr(value, "DB_ForeignKey30", None)
                setattr(value, "DB_ForeignKey30", self)

    @property
    def DB_Key15(self):
        return self.__DB_Key15

    @DB_Key15.setter
    def DB_Key15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DB_Key__DB_Key15", None)
        self.__DB_Key15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DB_Column14"):
                opp_val = getattr(old_value, "DB_Column14", None)
                if opp_val == self:
                    setattr(old_value, "DB_Column14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DB_Column14"):
                opp_val = getattr(value, "DB_Column14", None)
                setattr(value, "DB_Column14", self)

    @property
    def DB_Key26(self):
        return self.__DB_Key26

    @DB_Key26.setter
    def DB_Key26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DB_Key__DB_Key26", None)
        self.__DB_Key26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DB_Column27"):
                    opp_val = getattr(item, "DB_Column27", None)
                    
                    if opp_val == self:
                        setattr(item, "DB_Column27", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DB_Column27"):
                    opp_val = getattr(item, "DB_Column27", None)
                    
                    setattr(item, "DB_Column27", self)
                    

class DB_ForeignKey:

    def __init__(self, isMany: str, DB_ForeignKey: "DB_Table" = None, DB_ForeignKey18: "DB_Column" = None, DB_ForeignKey20: "DB_Key" = None, DB_ForeignKey23: "DB_Column" = None, DB_ForeignKey30: "DB_Key" = None):
        self.isMany = isMany
        self.DB_ForeignKey = DB_ForeignKey
        self.DB_ForeignKey18 = DB_ForeignKey18
        self.DB_ForeignKey20 = DB_ForeignKey20
        self.DB_ForeignKey23 = DB_ForeignKey23
        self.DB_ForeignKey30 = DB_ForeignKey30
        
    @property
    def isMany(self) -> str:
        return self.__isMany

    @isMany.setter
    def isMany(self, isMany: str):
        self.__isMany = isMany

    @property
    def DB_ForeignKey30(self):
        return self.__DB_ForeignKey30

    @DB_ForeignKey30.setter
    def DB_ForeignKey30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DB_ForeignKey__DB_ForeignKey30", None)
        self.__DB_ForeignKey30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DB_Key29"):
                opp_val = getattr(old_value, "DB_Key29", None)
                if opp_val == self:
                    setattr(old_value, "DB_Key29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DB_Key29"):
                opp_val = getattr(value, "DB_Key29", None)
                setattr(value, "DB_Key29", self)

    @property
    def DB_ForeignKey23(self):
        return self.__DB_ForeignKey23

    @DB_ForeignKey23.setter
    def DB_ForeignKey23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DB_ForeignKey__DB_ForeignKey23", None)
        self.__DB_ForeignKey23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DB_Column24"):
                opp_val = getattr(old_value, "DB_Column24", None)
                if opp_val == self:
                    setattr(old_value, "DB_Column24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DB_Column24"):
                opp_val = getattr(value, "DB_Column24", None)
                setattr(value, "DB_Column24", self)

    @property
    def DB_ForeignKey18(self):
        return self.__DB_ForeignKey18

    @DB_ForeignKey18.setter
    def DB_ForeignKey18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DB_ForeignKey__DB_ForeignKey18", None)
        self.__DB_ForeignKey18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DB_Column17"):
                opp_val = getattr(old_value, "DB_Column17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DB_Column17"):
                opp_val = getattr(value, "DB_Column17", None)
                if opp_val is None:
                    setattr(value, "DB_Column17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def DB_ForeignKey20(self):
        return self.__DB_ForeignKey20

    @DB_ForeignKey20.setter
    def DB_ForeignKey20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DB_ForeignKey__DB_ForeignKey20", None)
        self.__DB_ForeignKey20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DB_Key21"):
                opp_val = getattr(old_value, "DB_Key21", None)
                if opp_val == self:
                    setattr(old_value, "DB_Key21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DB_Key21"):
                opp_val = getattr(value, "DB_Key21", None)
                setattr(value, "DB_Key21", self)

    @property
    def DB_ForeignKey(self):
        return self.__DB_ForeignKey

    @DB_ForeignKey.setter
    def DB_ForeignKey(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DB_ForeignKey__DB_ForeignKey", None)
        self.__DB_ForeignKey = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DB_Table2"):
                opp_val = getattr(old_value, "DB_Table2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DB_Table2"):
                opp_val = getattr(value, "DB_Table2", None)
                if opp_val is None:
                    setattr(value, "DB_Table2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class DB_Table:

    def __init__(self, name: str, DB_Table: "DB_Database" = None, DB_Table2: set["DB_ForeignKey"] = None, DB_Table4: set["DB_Key"] = None, DB_Table6: set["DB_Column"] = None, DB_Table8: "DB_Database" = None, DB_Table12: "DB_Column" = None):
        self.name = name
        self.DB_Table = DB_Table
        self.DB_Table2 = DB_Table2 if DB_Table2 is not None else set()
        self.DB_Table4 = DB_Table4 if DB_Table4 is not None else set()
        self.DB_Table6 = DB_Table6 if DB_Table6 is not None else set()
        self.DB_Table8 = DB_Table8
        self.DB_Table12 = DB_Table12
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def DB_Table(self):
        return self.__DB_Table

    @DB_Table.setter
    def DB_Table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DB_Table__DB_Table", None)
        self.__DB_Table = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DB_Database"):
                opp_val = getattr(old_value, "DB_Database", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DB_Database"):
                opp_val = getattr(value, "DB_Database", None)
                if opp_val is None:
                    setattr(value, "DB_Database", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def DB_Table12(self):
        return self.__DB_Table12

    @DB_Table12.setter
    def DB_Table12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DB_Table__DB_Table12", None)
        self.__DB_Table12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DB_Column11"):
                opp_val = getattr(old_value, "DB_Column11", None)
                if opp_val == self:
                    setattr(old_value, "DB_Column11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DB_Column11"):
                opp_val = getattr(value, "DB_Column11", None)
                setattr(value, "DB_Column11", self)

    @property
    def DB_Table2(self):
        return self.__DB_Table2

    @DB_Table2.setter
    def DB_Table2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DB_Table__DB_Table2", None)
        self.__DB_Table2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DB_ForeignKey"):
                    opp_val = getattr(item, "DB_ForeignKey", None)
                    
                    if opp_val == self:
                        setattr(item, "DB_ForeignKey", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DB_ForeignKey"):
                    opp_val = getattr(item, "DB_ForeignKey", None)
                    
                    setattr(item, "DB_ForeignKey", self)
                    

    @property
    def DB_Table6(self):
        return self.__DB_Table6

    @DB_Table6.setter
    def DB_Table6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DB_Table__DB_Table6", None)
        self.__DB_Table6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DB_Column"):
                    opp_val = getattr(item, "DB_Column", None)
                    
                    if opp_val == self:
                        setattr(item, "DB_Column", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DB_Column"):
                    opp_val = getattr(item, "DB_Column", None)
                    
                    setattr(item, "DB_Column", self)
                    

    @property
    def DB_Table4(self):
        return self.__DB_Table4

    @DB_Table4.setter
    def DB_Table4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DB_Table__DB_Table4", None)
        self.__DB_Table4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DB_Key"):
                    opp_val = getattr(item, "DB_Key", None)
                    
                    if opp_val == self:
                        setattr(item, "DB_Key", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DB_Key"):
                    opp_val = getattr(item, "DB_Key", None)
                    
                    setattr(item, "DB_Key", self)
                    

    @property
    def DB_Table8(self):
        return self.__DB_Table8

    @DB_Table8.setter
    def DB_Table8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DB_Table__DB_Table8", None)
        self.__DB_Table8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DB_Database9"):
                opp_val = getattr(old_value, "DB_Database9", None)
                if opp_val == self:
                    setattr(old_value, "DB_Database9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DB_Database9"):
                opp_val = getattr(value, "DB_Database9", None)
                setattr(value, "DB_Database9", self)

class DB_Database:

    def __init__(self, name: str, DB_Database: set["DB_Table"] = None, DB_Database9: "DB_Table" = None):
        self.name = name
        self.DB_Database = DB_Database if DB_Database is not None else set()
        self.DB_Database9 = DB_Database9
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def DB_Database(self):
        return self.__DB_Database

    @DB_Database.setter
    def DB_Database(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DB_Database__DB_Database", None)
        self.__DB_Database = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DB_Table"):
                    opp_val = getattr(item, "DB_Table", None)
                    
                    if opp_val == self:
                        setattr(item, "DB_Table", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DB_Table"):
                    opp_val = getattr(item, "DB_Table", None)
                    
                    setattr(item, "DB_Table", self)
                    

    @property
    def DB_Database9(self):
        return self.__DB_Database9

    @DB_Database9.setter
    def DB_Database9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DB_Database__DB_Database9", None)
        self.__DB_Database9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DB_Table8"):
                opp_val = getattr(old_value, "DB_Table8", None)
                if opp_val == self:
                    setattr(old_value, "DB_Table8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DB_Table8"):
                opp_val = getattr(value, "DB_Table8", None)
                setattr(value, "DB_Table8", self)
