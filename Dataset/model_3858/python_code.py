from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class grammarSql_ForeignKey:

    pass
class grammarSql_PrimaryKey:

    pass
class grammarSql_Column:

    def __init__(self, name: str, type: str, isNotNull: bool, grammarSql_Column13: "grammarSql_Reference" = None, grammarSql_Column: "grammarSql_PrimaryKey" = None, grammarSql_Column5: "grammarSql_ForeignKey" = None):
        self.name = name
        self.type = type
        self.isNotNull = isNotNull
        self.grammarSql_Column13 = grammarSql_Column13
        self.grammarSql_Column = grammarSql_Column
        self.grammarSql_Column5 = grammarSql_Column5
        
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
    def isNotNull(self) -> bool:
        return self.__isNotNull

    @isNotNull.setter
    def isNotNull(self, isNotNull: bool):
        self.__isNotNull = isNotNull

    @property
    def grammarSql_Column13(self):
        return self.__grammarSql_Column13

    @grammarSql_Column13.setter
    def grammarSql_Column13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_grammarSql_Column__grammarSql_Column13", None)
        self.__grammarSql_Column13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "grammarSql_Reference12"):
                opp_val = getattr(old_value, "grammarSql_Reference12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "grammarSql_Reference12"):
                opp_val = getattr(value, "grammarSql_Reference12", None)
                if opp_val is None:
                    setattr(value, "grammarSql_Reference12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def grammarSql_Column5(self):
        return self.__grammarSql_Column5

    @grammarSql_Column5.setter
    def grammarSql_Column5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_grammarSql_Column__grammarSql_Column5", None)
        self.__grammarSql_Column5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "grammarSql_ForeignKey"):
                opp_val = getattr(old_value, "grammarSql_ForeignKey", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "grammarSql_ForeignKey"):
                opp_val = getattr(value, "grammarSql_ForeignKey", None)
                if opp_val is None:
                    setattr(value, "grammarSql_ForeignKey", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def grammarSql_Column(self):
        return self.__grammarSql_Column

    @grammarSql_Column.setter
    def grammarSql_Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_grammarSql_Column__grammarSql_Column", None)
        self.__grammarSql_Column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "grammarSql_PrimaryKey"):
                opp_val = getattr(old_value, "grammarSql_PrimaryKey", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "grammarSql_PrimaryKey"):
                opp_val = getattr(value, "grammarSql_PrimaryKey", None)
                if opp_val is None:
                    setattr(value, "grammarSql_PrimaryKey", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class grammarSql_EObject:

    pass
class grammarSql_Table:

    def __init__(self, name: str, grammarSql_Table10: "grammarSql_Reference" = None, grammarSql_Table: "grammarSql_Model" = None, grammarSql_Table2: set["grammarSql_EObject"] = None):
        self.name = name
        self.grammarSql_Table10 = grammarSql_Table10
        self.grammarSql_Table = grammarSql_Table
        self.grammarSql_Table2 = grammarSql_Table2 if grammarSql_Table2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def grammarSql_Table2(self):
        return self.__grammarSql_Table2

    @grammarSql_Table2.setter
    def grammarSql_Table2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_grammarSql_Table__grammarSql_Table2", None)
        self.__grammarSql_Table2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "grammarSql_EObject"):
                    opp_val = getattr(item, "grammarSql_EObject", None)
                    
                    if opp_val == self:
                        setattr(item, "grammarSql_EObject", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "grammarSql_EObject"):
                    opp_val = getattr(item, "grammarSql_EObject", None)
                    
                    setattr(item, "grammarSql_EObject", self)
                    

    @property
    def grammarSql_Table10(self):
        return self.__grammarSql_Table10

    @grammarSql_Table10.setter
    def grammarSql_Table10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_grammarSql_Table__grammarSql_Table10", None)
        self.__grammarSql_Table10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "grammarSql_Reference9"):
                opp_val = getattr(old_value, "grammarSql_Reference9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "grammarSql_Reference9"):
                opp_val = getattr(value, "grammarSql_Reference9", None)
                if opp_val is None:
                    setattr(value, "grammarSql_Reference9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def grammarSql_Table(self):
        return self.__grammarSql_Table

    @grammarSql_Table.setter
    def grammarSql_Table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_grammarSql_Table__grammarSql_Table", None)
        self.__grammarSql_Table = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "grammarSql_Model"):
                opp_val = getattr(old_value, "grammarSql_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "grammarSql_Model"):
                opp_val = getattr(value, "grammarSql_Model", None)
                if opp_val is None:
                    setattr(value, "grammarSql_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class grammarSql_Model:

    pass
class grammarSql_Reference:

    pass