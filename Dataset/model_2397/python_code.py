from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class sQL_ForeignKey:

    pass
class sQL_PrimaryKey:

    pass
class sQL_Column:

    def __init__(self, name: str, dataType: str, notNull: str, sQL_Column: "sQL_Table" = None, sQL_Column9: "sQL_PrimaryKey" = None, sQL_Column12: "sQL_ForeignKey" = None, sQL_Column18: "sQL_ForeignKey" = None):
        self.name = name
        self.dataType = dataType
        self.notNull = notNull
        self.sQL_Column = sQL_Column
        self.sQL_Column9 = sQL_Column9
        self.sQL_Column12 = sQL_Column12
        self.sQL_Column18 = sQL_Column18
        
    @property
    def dataType(self) -> str:
        return self.__dataType

    @dataType.setter
    def dataType(self, dataType: str):
        self.__dataType = dataType

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def notNull(self) -> str:
        return self.__notNull

    @notNull.setter
    def notNull(self, notNull: str):
        self.__notNull = notNull

    @property
    def sQL_Column12(self):
        return self.__sQL_Column12

    @sQL_Column12.setter
    def sQL_Column12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sQL_Column__sQL_Column12", None)
        self.__sQL_Column12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sQL_ForeignKey11"):
                opp_val = getattr(old_value, "sQL_ForeignKey11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sQL_ForeignKey11"):
                opp_val = getattr(value, "sQL_ForeignKey11", None)
                if opp_val is None:
                    setattr(value, "sQL_ForeignKey11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sQL_Column18(self):
        return self.__sQL_Column18

    @sQL_Column18.setter
    def sQL_Column18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sQL_Column__sQL_Column18", None)
        self.__sQL_Column18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sQL_ForeignKey17"):
                opp_val = getattr(old_value, "sQL_ForeignKey17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sQL_ForeignKey17"):
                opp_val = getattr(value, "sQL_ForeignKey17", None)
                if opp_val is None:
                    setattr(value, "sQL_ForeignKey17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sQL_Column9(self):
        return self.__sQL_Column9

    @sQL_Column9.setter
    def sQL_Column9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sQL_Column__sQL_Column9", None)
        self.__sQL_Column9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sQL_PrimaryKey8"):
                opp_val = getattr(old_value, "sQL_PrimaryKey8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sQL_PrimaryKey8"):
                opp_val = getattr(value, "sQL_PrimaryKey8", None)
                if opp_val is None:
                    setattr(value, "sQL_PrimaryKey8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sQL_Column(self):
        return self.__sQL_Column

    @sQL_Column.setter
    def sQL_Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sQL_Column__sQL_Column", None)
        self.__sQL_Column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sQL_Table2"):
                opp_val = getattr(old_value, "sQL_Table2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sQL_Table2"):
                opp_val = getattr(value, "sQL_Table2", None)
                if opp_val is None:
                    setattr(value, "sQL_Table2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sQL_Table:

    def __init__(self, name: str, sQL_Table: "sQL_Database" = None, sQL_Table2: set["sQL_Column"] = None, sQL_Table15: "sQL_ForeignKey" = None, sQL_Table4: "sQL_PrimaryKey" = None, sQL_Table6: set["sQL_ForeignKey"] = None):
        self.name = name
        self.sQL_Table = sQL_Table
        self.sQL_Table2 = sQL_Table2 if sQL_Table2 is not None else set()
        self.sQL_Table15 = sQL_Table15
        self.sQL_Table4 = sQL_Table4
        self.sQL_Table6 = sQL_Table6 if sQL_Table6 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def sQL_Table4(self):
        return self.__sQL_Table4

    @sQL_Table4.setter
    def sQL_Table4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sQL_Table__sQL_Table4", None)
        self.__sQL_Table4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sQL_PrimaryKey"):
                opp_val = getattr(old_value, "sQL_PrimaryKey", None)
                if opp_val == self:
                    setattr(old_value, "sQL_PrimaryKey", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sQL_PrimaryKey"):
                opp_val = getattr(value, "sQL_PrimaryKey", None)
                setattr(value, "sQL_PrimaryKey", self)

    @property
    def sQL_Table(self):
        return self.__sQL_Table

    @sQL_Table.setter
    def sQL_Table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sQL_Table__sQL_Table", None)
        self.__sQL_Table = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sQL_Database"):
                opp_val = getattr(old_value, "sQL_Database", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sQL_Database"):
                opp_val = getattr(value, "sQL_Database", None)
                if opp_val is None:
                    setattr(value, "sQL_Database", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sQL_Table2(self):
        return self.__sQL_Table2

    @sQL_Table2.setter
    def sQL_Table2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sQL_Table__sQL_Table2", None)
        self.__sQL_Table2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sQL_Column"):
                    opp_val = getattr(item, "sQL_Column", None)
                    
                    if opp_val == self:
                        setattr(item, "sQL_Column", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sQL_Column"):
                    opp_val = getattr(item, "sQL_Column", None)
                    
                    setattr(item, "sQL_Column", self)
                    

    @property
    def sQL_Table15(self):
        return self.__sQL_Table15

    @sQL_Table15.setter
    def sQL_Table15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sQL_Table__sQL_Table15", None)
        self.__sQL_Table15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sQL_ForeignKey14"):
                opp_val = getattr(old_value, "sQL_ForeignKey14", None)
                if opp_val == self:
                    setattr(old_value, "sQL_ForeignKey14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sQL_ForeignKey14"):
                opp_val = getattr(value, "sQL_ForeignKey14", None)
                setattr(value, "sQL_ForeignKey14", self)

    @property
    def sQL_Table6(self):
        return self.__sQL_Table6

    @sQL_Table6.setter
    def sQL_Table6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sQL_Table__sQL_Table6", None)
        self.__sQL_Table6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sQL_ForeignKey"):
                    opp_val = getattr(item, "sQL_ForeignKey", None)
                    
                    if opp_val == self:
                        setattr(item, "sQL_ForeignKey", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sQL_ForeignKey"):
                    opp_val = getattr(item, "sQL_ForeignKey", None)
                    
                    setattr(item, "sQL_ForeignKey", self)
                    

class sQL_Database:

    pass