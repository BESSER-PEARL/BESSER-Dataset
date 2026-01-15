from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class RDBMSMM_RDBMSModel:

    pass
class RDBMSMM_Table:

    def __init__(self, name: str, RDBMSMM_Table: set["RDBMSMM_Column"] = None, RDBMSMM_Table2: set["RDBMSMM_Column"] = None, RDBMSMM_Table5: set["RDBMSMM_FKey"] = None, RDBMSMM_Table8: "RDBMSMM_FKey" = None, RDBMSMM_Table13: "RDBMSMM_RDBMSModel" = None):
        self.name = name
        self.RDBMSMM_Table = RDBMSMM_Table if RDBMSMM_Table is not None else set()
        self.RDBMSMM_Table2 = RDBMSMM_Table2 if RDBMSMM_Table2 is not None else set()
        self.RDBMSMM_Table5 = RDBMSMM_Table5 if RDBMSMM_Table5 is not None else set()
        self.RDBMSMM_Table8 = RDBMSMM_Table8
        self.RDBMSMM_Table13 = RDBMSMM_Table13
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def RDBMSMM_Table2(self):
        return self.__RDBMSMM_Table2

    @RDBMSMM_Table2.setter
    def RDBMSMM_Table2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RDBMSMM_Table__RDBMSMM_Table2", None)
        self.__RDBMSMM_Table2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RDBMSMM_Column3"):
                    opp_val = getattr(item, "RDBMSMM_Column3", None)
                    
                    if opp_val == self:
                        setattr(item, "RDBMSMM_Column3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RDBMSMM_Column3"):
                    opp_val = getattr(item, "RDBMSMM_Column3", None)
                    
                    setattr(item, "RDBMSMM_Column3", self)
                    

    @property
    def RDBMSMM_Table(self):
        return self.__RDBMSMM_Table

    @RDBMSMM_Table.setter
    def RDBMSMM_Table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RDBMSMM_Table__RDBMSMM_Table", None)
        self.__RDBMSMM_Table = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RDBMSMM_Column"):
                    opp_val = getattr(item, "RDBMSMM_Column", None)
                    
                    if opp_val == self:
                        setattr(item, "RDBMSMM_Column", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RDBMSMM_Column"):
                    opp_val = getattr(item, "RDBMSMM_Column", None)
                    
                    setattr(item, "RDBMSMM_Column", self)
                    

    @property
    def RDBMSMM_Table5(self):
        return self.__RDBMSMM_Table5

    @RDBMSMM_Table5.setter
    def RDBMSMM_Table5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RDBMSMM_Table__RDBMSMM_Table5", None)
        self.__RDBMSMM_Table5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RDBMSMM_FKey"):
                    opp_val = getattr(item, "RDBMSMM_FKey", None)
                    
                    if opp_val == self:
                        setattr(item, "RDBMSMM_FKey", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RDBMSMM_FKey"):
                    opp_val = getattr(item, "RDBMSMM_FKey", None)
                    
                    setattr(item, "RDBMSMM_FKey", self)
                    

    @property
    def RDBMSMM_Table8(self):
        return self.__RDBMSMM_Table8

    @RDBMSMM_Table8.setter
    def RDBMSMM_Table8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RDBMSMM_Table__RDBMSMM_Table8", None)
        self.__RDBMSMM_Table8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RDBMSMM_FKey7"):
                opp_val = getattr(old_value, "RDBMSMM_FKey7", None)
                if opp_val == self:
                    setattr(old_value, "RDBMSMM_FKey7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RDBMSMM_FKey7"):
                opp_val = getattr(value, "RDBMSMM_FKey7", None)
                setattr(value, "RDBMSMM_FKey7", self)

    @property
    def RDBMSMM_Table13(self):
        return self.__RDBMSMM_Table13

    @RDBMSMM_Table13.setter
    def RDBMSMM_Table13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RDBMSMM_Table__RDBMSMM_Table13", None)
        self.__RDBMSMM_Table13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RDBMSMM_RDBMSModel"):
                opp_val = getattr(old_value, "RDBMSMM_RDBMSModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RDBMSMM_RDBMSModel"):
                opp_val = getattr(value, "RDBMSMM_RDBMSModel", None)
                if opp_val is None:
                    setattr(value, "RDBMSMM_RDBMSModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class RDBMSMM_FKey:

    pass
class RDBMSMM_Column:

    def __init__(self, type: str, name: str, RDBMSMM_Column: "RDBMSMM_Table" = None, RDBMSMM_Column3: "RDBMSMM_Table" = None, RDBMSMM_Column11: "RDBMSMM_FKey" = None):
        self.type = type
        self.name = name
        self.RDBMSMM_Column = RDBMSMM_Column
        self.RDBMSMM_Column3 = RDBMSMM_Column3
        self.RDBMSMM_Column11 = RDBMSMM_Column11
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def RDBMSMM_Column3(self):
        return self.__RDBMSMM_Column3

    @RDBMSMM_Column3.setter
    def RDBMSMM_Column3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RDBMSMM_Column__RDBMSMM_Column3", None)
        self.__RDBMSMM_Column3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RDBMSMM_Table2"):
                opp_val = getattr(old_value, "RDBMSMM_Table2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RDBMSMM_Table2"):
                opp_val = getattr(value, "RDBMSMM_Table2", None)
                if opp_val is None:
                    setattr(value, "RDBMSMM_Table2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def RDBMSMM_Column(self):
        return self.__RDBMSMM_Column

    @RDBMSMM_Column.setter
    def RDBMSMM_Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RDBMSMM_Column__RDBMSMM_Column", None)
        self.__RDBMSMM_Column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RDBMSMM_Table"):
                opp_val = getattr(old_value, "RDBMSMM_Table", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RDBMSMM_Table"):
                opp_val = getattr(value, "RDBMSMM_Table", None)
                if opp_val is None:
                    setattr(value, "RDBMSMM_Table", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def RDBMSMM_Column11(self):
        return self.__RDBMSMM_Column11

    @RDBMSMM_Column11.setter
    def RDBMSMM_Column11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RDBMSMM_Column__RDBMSMM_Column11", None)
        self.__RDBMSMM_Column11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RDBMSMM_FKey10"):
                opp_val = getattr(old_value, "RDBMSMM_FKey10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RDBMSMM_FKey10"):
                opp_val = getattr(value, "RDBMSMM_FKey10", None)
                if opp_val is None:
                    setattr(value, "RDBMSMM_FKey10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
