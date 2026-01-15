from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class TableM_FKey:

    pass
class TableM_Column:

    def __init__(self, name: str, type: str, Column: "TableM_Table" = None, cols: "TableM_Table" = None, TableM_Column: "TableM_Table" = None, TableM_Column14: "TableM_FKey" = None):
        self.name = name
        self.type = type
        self.Column = Column
        self.cols = cols
        self.TableM_Column = TableM_Column
        self.TableM_Column14 = TableM_Column14
        
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
    def Column(self):
        return self.__Column

    @Column.setter
    def Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TableM_Column__Column", None)
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
    def TableM_Column14(self):
        return self.__TableM_Column14

    @TableM_Column14.setter
    def TableM_Column14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TableM_Column__TableM_Column14", None)
        self.__TableM_Column14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TableM_FKey13"):
                opp_val = getattr(old_value, "TableM_FKey13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TableM_FKey13"):
                opp_val = getattr(value, "TableM_FKey13", None)
                if opp_val is None:
                    setattr(value, "TableM_FKey13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cols(self):
        return self.__cols

    @cols.setter
    def cols(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TableM_Column__cols", None)
        self.__cols = value
        
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
    def TableM_Column(self):
        return self.__TableM_Column

    @TableM_Column.setter
    def TableM_Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TableM_Column__TableM_Column", None)
        self.__TableM_Column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TableM_Table"):
                opp_val = getattr(old_value, "TableM_Table", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TableM_Table"):
                opp_val = getattr(value, "TableM_Table", None)
                if opp_val is None:
                    setattr(value, "TableM_Table", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class TableM_Table:

    def __init__(self, name: str, owner: set["TableM_Column"] = None, TableM_Table5: set["TableM_FKey"] = None, Table: "TableM_Column" = None, TableM_Table: set["TableM_Column"] = None, owner3: set["TableM_FKey"] = None, TableM_Table9: "TableM_FKey" = None, Table11: "TableM_FKey" = None):
        self.name = name
        self.owner = owner if owner is not None else set()
        self.TableM_Table5 = TableM_Table5 if TableM_Table5 is not None else set()
        self.Table = Table
        self.TableM_Table = TableM_Table if TableM_Table is not None else set()
        self.owner3 = owner3 if owner3 is not None else set()
        self.TableM_Table9 = TableM_Table9
        self.Table11 = Table11
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def owner3(self):
        return self.__owner3

    @owner3.setter
    def owner3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TableM_Table__owner3", None)
        self.__owner3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FKey"):
                    opp_val = getattr(item, "FKey", None)
                    
                    if opp_val == self:
                        setattr(item, "FKey", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FKey"):
                    opp_val = getattr(item, "FKey", None)
                    
                    setattr(item, "FKey", self)
                    

    @property
    def TableM_Table5(self):
        return self.__TableM_Table5

    @TableM_Table5.setter
    def TableM_Table5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TableM_Table__TableM_Table5", None)
        self.__TableM_Table5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TableM_FKey"):
                    opp_val = getattr(item, "TableM_FKey", None)
                    
                    if opp_val == self:
                        setattr(item, "TableM_FKey", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TableM_FKey"):
                    opp_val = getattr(item, "TableM_FKey", None)
                    
                    setattr(item, "TableM_FKey", self)
                    

    @property
    def Table11(self):
        return self.__Table11

    @Table11.setter
    def Table11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TableM_Table__Table11", None)
        self.__Table11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fkeys"):
                opp_val = getattr(old_value, "fkeys", None)
                if opp_val == self:
                    setattr(old_value, "fkeys", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fkeys"):
                opp_val = getattr(value, "fkeys", None)
                setattr(value, "fkeys", self)

    @property
    def Table(self):
        return self.__Table

    @Table.setter
    def Table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TableM_Table__Table", None)
        self.__Table = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cols"):
                opp_val = getattr(old_value, "cols", None)
                if opp_val == self:
                    setattr(old_value, "cols", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cols"):
                opp_val = getattr(value, "cols", None)
                setattr(value, "cols", self)

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TableM_Table__owner", None)
        self.__owner = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Column"):
                    opp_val = getattr(item, "Column", None)
                    
                    if opp_val == self:
                        setattr(item, "Column", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Column"):
                    opp_val = getattr(item, "Column", None)
                    
                    setattr(item, "Column", self)
                    

    @property
    def TableM_Table9(self):
        return self.__TableM_Table9

    @TableM_Table9.setter
    def TableM_Table9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TableM_Table__TableM_Table9", None)
        self.__TableM_Table9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TableM_FKey8"):
                opp_val = getattr(old_value, "TableM_FKey8", None)
                if opp_val == self:
                    setattr(old_value, "TableM_FKey8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TableM_FKey8"):
                opp_val = getattr(value, "TableM_FKey8", None)
                setattr(value, "TableM_FKey8", self)

    @property
    def TableM_Table(self):
        return self.__TableM_Table

    @TableM_Table.setter
    def TableM_Table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TableM_Table__TableM_Table", None)
        self.__TableM_Table = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TableM_Column"):
                    opp_val = getattr(item, "TableM_Column", None)
                    
                    if opp_val == self:
                        setattr(item, "TableM_Column", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TableM_Column"):
                    opp_val = getattr(item, "TableM_Column", None)
                    
                    setattr(item, "TableM_Column", self)
                    
