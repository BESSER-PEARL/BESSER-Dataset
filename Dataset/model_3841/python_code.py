from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class target_Database:

    pass
class target_Column:

    def __init__(self, type: str, name: str, target_Column: "target_Table" = None, target_Column5: "target_Table" = None, target_Column8: "target_FKey" = None):
        self.type = type
        self.name = name
        self.target_Column = target_Column
        self.target_Column5 = target_Column5
        self.target_Column8 = target_Column8
        
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
    def target_Column(self):
        return self.__target_Column

    @target_Column.setter
    def target_Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_target_Column__target_Column", None)
        self.__target_Column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "target_Table2"):
                opp_val = getattr(old_value, "target_Table2", None)
                if opp_val == self:
                    setattr(old_value, "target_Table2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "target_Table2"):
                opp_val = getattr(value, "target_Table2", None)
                setattr(value, "target_Table2", self)

    @property
    def target_Column8(self):
        return self.__target_Column8

    @target_Column8.setter
    def target_Column8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_target_Column__target_Column8", None)
        self.__target_Column8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "target_FKey7"):
                opp_val = getattr(old_value, "target_FKey7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "target_FKey7"):
                opp_val = getattr(value, "target_FKey7", None)
                if opp_val is None:
                    setattr(value, "target_FKey7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def target_Column5(self):
        return self.__target_Column5

    @target_Column5.setter
    def target_Column5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_target_Column__target_Column5", None)
        self.__target_Column5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "target_Table4"):
                opp_val = getattr(old_value, "target_Table4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "target_Table4"):
                opp_val = getattr(value, "target_Table4", None)
                if opp_val is None:
                    setattr(value, "target_Table4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class target_FKey:

    pass
class target_Table:

    def __init__(self, name: str, target_Table: set["target_FKey"] = None, target_Table2: "target_Column" = None, target_Table4: set["target_Column"] = None, target_Table11: "target_FKey" = None, target_Table13: "target_Database" = None):
        self.name = name
        self.target_Table = target_Table if target_Table is not None else set()
        self.target_Table2 = target_Table2
        self.target_Table4 = target_Table4 if target_Table4 is not None else set()
        self.target_Table11 = target_Table11
        self.target_Table13 = target_Table13
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def target_Table11(self):
        return self.__target_Table11

    @target_Table11.setter
    def target_Table11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_target_Table__target_Table11", None)
        self.__target_Table11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "target_FKey10"):
                opp_val = getattr(old_value, "target_FKey10", None)
                if opp_val == self:
                    setattr(old_value, "target_FKey10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "target_FKey10"):
                opp_val = getattr(value, "target_FKey10", None)
                setattr(value, "target_FKey10", self)

    @property
    def target_Table4(self):
        return self.__target_Table4

    @target_Table4.setter
    def target_Table4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_target_Table__target_Table4", None)
        self.__target_Table4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "target_Column5"):
                    opp_val = getattr(item, "target_Column5", None)
                    
                    if opp_val == self:
                        setattr(item, "target_Column5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "target_Column5"):
                    opp_val = getattr(item, "target_Column5", None)
                    
                    setattr(item, "target_Column5", self)
                    

    @property
    def target_Table13(self):
        return self.__target_Table13

    @target_Table13.setter
    def target_Table13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_target_Table__target_Table13", None)
        self.__target_Table13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "target_Database"):
                opp_val = getattr(old_value, "target_Database", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "target_Database"):
                opp_val = getattr(value, "target_Database", None)
                if opp_val is None:
                    setattr(value, "target_Database", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def target_Table2(self):
        return self.__target_Table2

    @target_Table2.setter
    def target_Table2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_target_Table__target_Table2", None)
        self.__target_Table2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "target_Column"):
                opp_val = getattr(old_value, "target_Column", None)
                if opp_val == self:
                    setattr(old_value, "target_Column", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "target_Column"):
                opp_val = getattr(value, "target_Column", None)
                setattr(value, "target_Column", self)

    @property
    def target_Table(self):
        return self.__target_Table

    @target_Table.setter
    def target_Table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_target_Table__target_Table", None)
        self.__target_Table = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "target_FKey"):
                    opp_val = getattr(item, "target_FKey", None)
                    
                    if opp_val == self:
                        setattr(item, "target_FKey", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "target_FKey"):
                    opp_val = getattr(item, "target_FKey", None)
                    
                    setattr(item, "target_FKey", self)
                    
