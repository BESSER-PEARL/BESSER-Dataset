from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class rdbms_ForeignKey:

    pass
class rdbms_Table:

    def __init__(self, name: str, rdbms_Table: "rdbms_RDBMSModel" = None, rdbms_Table6: set["rdbms_ForeignKey"] = None, rdbms_Table9: set["rdbms_Column"] = None, rdbms_Table12: set["rdbms_Column"] = None, rdbms_Table16: "rdbms_ForeignKey" = None):
        self.name = name
        self.rdbms_Table = rdbms_Table
        self.rdbms_Table6 = rdbms_Table6 if rdbms_Table6 is not None else set()
        self.rdbms_Table9 = rdbms_Table9 if rdbms_Table9 is not None else set()
        self.rdbms_Table12 = rdbms_Table12 if rdbms_Table12 is not None else set()
        self.rdbms_Table16 = rdbms_Table16
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def rdbms_Table16(self):
        return self.__rdbms_Table16

    @rdbms_Table16.setter
    def rdbms_Table16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_Table__rdbms_Table16", None)
        self.__rdbms_Table16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_ForeignKey15"):
                opp_val = getattr(old_value, "rdbms_ForeignKey15", None)
                if opp_val == self:
                    setattr(old_value, "rdbms_ForeignKey15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_ForeignKey15"):
                opp_val = getattr(value, "rdbms_ForeignKey15", None)
                setattr(value, "rdbms_ForeignKey15", self)

    @property
    def rdbms_Table6(self):
        return self.__rdbms_Table6

    @rdbms_Table6.setter
    def rdbms_Table6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_Table__rdbms_Table6", None)
        self.__rdbms_Table6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rdbms_ForeignKey7"):
                    opp_val = getattr(item, "rdbms_ForeignKey7", None)
                    
                    if opp_val == self:
                        setattr(item, "rdbms_ForeignKey7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rdbms_ForeignKey7"):
                    opp_val = getattr(item, "rdbms_ForeignKey7", None)
                    
                    setattr(item, "rdbms_ForeignKey7", self)
                    

    @property
    def rdbms_Table12(self):
        return self.__rdbms_Table12

    @rdbms_Table12.setter
    def rdbms_Table12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_Table__rdbms_Table12", None)
        self.__rdbms_Table12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rdbms_Column13"):
                    opp_val = getattr(item, "rdbms_Column13", None)
                    
                    if opp_val == self:
                        setattr(item, "rdbms_Column13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rdbms_Column13"):
                    opp_val = getattr(item, "rdbms_Column13", None)
                    
                    setattr(item, "rdbms_Column13", self)
                    

    @property
    def rdbms_Table(self):
        return self.__rdbms_Table

    @rdbms_Table.setter
    def rdbms_Table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_Table__rdbms_Table", None)
        self.__rdbms_Table = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_RDBMSModel"):
                opp_val = getattr(old_value, "rdbms_RDBMSModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_RDBMSModel"):
                opp_val = getattr(value, "rdbms_RDBMSModel", None)
                if opp_val is None:
                    setattr(value, "rdbms_RDBMSModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rdbms_Table9(self):
        return self.__rdbms_Table9

    @rdbms_Table9.setter
    def rdbms_Table9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_Table__rdbms_Table9", None)
        self.__rdbms_Table9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rdbms_Column10"):
                    opp_val = getattr(item, "rdbms_Column10", None)
                    
                    if opp_val == self:
                        setattr(item, "rdbms_Column10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rdbms_Column10"):
                    opp_val = getattr(item, "rdbms_Column10", None)
                    
                    setattr(item, "rdbms_Column10", self)
                    

class rdbms_RDBMSModel:

    pass
class rdbms_Column:

    def __init__(self, name: str, type: str, rdbms_Column: "rdbms_RDBMSModel" = None, rdbms_Column10: "rdbms_Table" = None, rdbms_Column13: "rdbms_Table" = None, rdbms_Column19: "rdbms_ForeignKey" = None):
        self.name = name
        self.type = type
        self.rdbms_Column = rdbms_Column
        self.rdbms_Column10 = rdbms_Column10
        self.rdbms_Column13 = rdbms_Column13
        self.rdbms_Column19 = rdbms_Column19
        
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
    def rdbms_Column10(self):
        return self.__rdbms_Column10

    @rdbms_Column10.setter
    def rdbms_Column10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_Column__rdbms_Column10", None)
        self.__rdbms_Column10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_Table9"):
                opp_val = getattr(old_value, "rdbms_Table9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_Table9"):
                opp_val = getattr(value, "rdbms_Table9", None)
                if opp_val is None:
                    setattr(value, "rdbms_Table9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rdbms_Column19(self):
        return self.__rdbms_Column19

    @rdbms_Column19.setter
    def rdbms_Column19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_Column__rdbms_Column19", None)
        self.__rdbms_Column19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_ForeignKey18"):
                opp_val = getattr(old_value, "rdbms_ForeignKey18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_ForeignKey18"):
                opp_val = getattr(value, "rdbms_ForeignKey18", None)
                if opp_val is None:
                    setattr(value, "rdbms_ForeignKey18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rdbms_Column(self):
        return self.__rdbms_Column

    @rdbms_Column.setter
    def rdbms_Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_Column__rdbms_Column", None)
        self.__rdbms_Column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_RDBMSModel2"):
                opp_val = getattr(old_value, "rdbms_RDBMSModel2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_RDBMSModel2"):
                opp_val = getattr(value, "rdbms_RDBMSModel2", None)
                if opp_val is None:
                    setattr(value, "rdbms_RDBMSModel2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rdbms_Column13(self):
        return self.__rdbms_Column13

    @rdbms_Column13.setter
    def rdbms_Column13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_Column__rdbms_Column13", None)
        self.__rdbms_Column13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_Table12"):
                opp_val = getattr(old_value, "rdbms_Table12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_Table12"):
                opp_val = getattr(value, "rdbms_Table12", None)
                if opp_val is None:
                    setattr(value, "rdbms_Table12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
