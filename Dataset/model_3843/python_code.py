from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class RDBMS_ForeignKey:

    pass
class RDBMS_Column:

    def __init__(self, name: str, type: str, RDBMS_Column10: "RDBMS_ForeignKey" = None, RDBMS_Column: "RDBMS_Table" = None, RDBMS_Column7: "RDBMS_Table" = None):
        self.name = name
        self.type = type
        self.RDBMS_Column10 = RDBMS_Column10
        self.RDBMS_Column = RDBMS_Column
        self.RDBMS_Column7 = RDBMS_Column7
        
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
    def RDBMS_Column(self):
        return self.__RDBMS_Column

    @RDBMS_Column.setter
    def RDBMS_Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RDBMS_Column__RDBMS_Column", None)
        self.__RDBMS_Column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RDBMS_Table2"):
                opp_val = getattr(old_value, "RDBMS_Table2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RDBMS_Table2"):
                opp_val = getattr(value, "RDBMS_Table2", None)
                if opp_val is None:
                    setattr(value, "RDBMS_Table2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def RDBMS_Column10(self):
        return self.__RDBMS_Column10

    @RDBMS_Column10.setter
    def RDBMS_Column10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RDBMS_Column__RDBMS_Column10", None)
        self.__RDBMS_Column10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RDBMS_ForeignKey9"):
                opp_val = getattr(old_value, "RDBMS_ForeignKey9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RDBMS_ForeignKey9"):
                opp_val = getattr(value, "RDBMS_ForeignKey9", None)
                if opp_val is None:
                    setattr(value, "RDBMS_ForeignKey9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def RDBMS_Column7(self):
        return self.__RDBMS_Column7

    @RDBMS_Column7.setter
    def RDBMS_Column7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RDBMS_Column__RDBMS_Column7", None)
        self.__RDBMS_Column7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RDBMS_Table6"):
                opp_val = getattr(old_value, "RDBMS_Table6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RDBMS_Table6"):
                opp_val = getattr(value, "RDBMS_Table6", None)
                if opp_val is None:
                    setattr(value, "RDBMS_Table6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class RDBMS_Table:

    def __init__(self, name: str, is_local: bool, RDBMS_Table: "RDBMS_Schema" = None, RDBMS_Table13: "RDBMS_ForeignKey" = None, RDBMS_Table2: set["RDBMS_Column"] = None, RDBMS_Table4: set["RDBMS_ForeignKey"] = None, RDBMS_Table6: set["RDBMS_Column"] = None):
        self.name = name
        self.is_local = is_local
        self.RDBMS_Table = RDBMS_Table
        self.RDBMS_Table13 = RDBMS_Table13
        self.RDBMS_Table2 = RDBMS_Table2 if RDBMS_Table2 is not None else set()
        self.RDBMS_Table4 = RDBMS_Table4 if RDBMS_Table4 is not None else set()
        self.RDBMS_Table6 = RDBMS_Table6 if RDBMS_Table6 is not None else set()
        
    @property
    def is_local(self) -> bool:
        return self.__is_local

    @is_local.setter
    def is_local(self, is_local: bool):
        self.__is_local = is_local

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def RDBMS_Table6(self):
        return self.__RDBMS_Table6

    @RDBMS_Table6.setter
    def RDBMS_Table6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RDBMS_Table__RDBMS_Table6", None)
        self.__RDBMS_Table6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RDBMS_Column7"):
                    opp_val = getattr(item, "RDBMS_Column7", None)
                    
                    if opp_val == self:
                        setattr(item, "RDBMS_Column7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RDBMS_Column7"):
                    opp_val = getattr(item, "RDBMS_Column7", None)
                    
                    setattr(item, "RDBMS_Column7", self)
                    

    @property
    def RDBMS_Table4(self):
        return self.__RDBMS_Table4

    @RDBMS_Table4.setter
    def RDBMS_Table4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RDBMS_Table__RDBMS_Table4", None)
        self.__RDBMS_Table4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RDBMS_ForeignKey"):
                    opp_val = getattr(item, "RDBMS_ForeignKey", None)
                    
                    if opp_val == self:
                        setattr(item, "RDBMS_ForeignKey", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RDBMS_ForeignKey"):
                    opp_val = getattr(item, "RDBMS_ForeignKey", None)
                    
                    setattr(item, "RDBMS_ForeignKey", self)
                    

    @property
    def RDBMS_Table2(self):
        return self.__RDBMS_Table2

    @RDBMS_Table2.setter
    def RDBMS_Table2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RDBMS_Table__RDBMS_Table2", None)
        self.__RDBMS_Table2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RDBMS_Column"):
                    opp_val = getattr(item, "RDBMS_Column", None)
                    
                    if opp_val == self:
                        setattr(item, "RDBMS_Column", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RDBMS_Column"):
                    opp_val = getattr(item, "RDBMS_Column", None)
                    
                    setattr(item, "RDBMS_Column", self)
                    

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
            if hasattr(old_value, "RDBMS_Schema"):
                opp_val = getattr(old_value, "RDBMS_Schema", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RDBMS_Schema"):
                opp_val = getattr(value, "RDBMS_Schema", None)
                if opp_val is None:
                    setattr(value, "RDBMS_Schema", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def RDBMS_Table13(self):
        return self.__RDBMS_Table13

    @RDBMS_Table13.setter
    def RDBMS_Table13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RDBMS_Table__RDBMS_Table13", None)
        self.__RDBMS_Table13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RDBMS_ForeignKey12"):
                opp_val = getattr(old_value, "RDBMS_ForeignKey12", None)
                if opp_val == self:
                    setattr(old_value, "RDBMS_ForeignKey12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RDBMS_ForeignKey12"):
                opp_val = getattr(value, "RDBMS_ForeignKey12", None)
                setattr(value, "RDBMS_ForeignKey12", self)

class RDBMS_Schema:

    def __init__(self, name: str, RDBMS_Schema: set["RDBMS_Table"] = None):
        self.name = name
        self.RDBMS_Schema = RDBMS_Schema if RDBMS_Schema is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def RDBMS_Schema(self):
        return self.__RDBMS_Schema

    @RDBMS_Schema.setter
    def RDBMS_Schema(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RDBMS_Schema__RDBMS_Schema", None)
        self.__RDBMS_Schema = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RDBMS_Table"):
                    opp_val = getattr(item, "RDBMS_Table", None)
                    
                    if opp_val == self:
                        setattr(item, "RDBMS_Table", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RDBMS_Table"):
                    opp_val = getattr(item, "RDBMS_Table", None)
                    
                    setattr(item, "RDBMS_Table", self)
                    
