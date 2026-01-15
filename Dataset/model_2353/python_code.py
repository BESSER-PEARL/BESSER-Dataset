from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class simpleRdbms_RModelElement:

    def __init__(self, kind: str, name: str):
        self.kind = kind
        self.name = name
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class RModelElement:

    pass
class simpleRdbms_Table(RModelElement):

    pass
class simpleRdbms_Schema(RModelElement):

    pass
class simpleRdbms_ForeignKey(RModelElement):

    pass
class simpleRdbms_Key(RModelElement):

    pass
class simpleRdbms_Column(RModelElement):

    def __init__(self, type: str, Column: "simpleRdbms_Table" = None, Column16: "simpleRdbms_Key" = None, Column21: "simpleRdbms_ForeignKey" = None, column: "simpleRdbms_Table" = None, column10: set["simpleRdbms_Key"] = None, column13: set["simpleRdbms_ForeignKey"] = None):
        self.type = type
        self.Column = Column
        self.Column16 = Column16
        self.Column21 = Column21
        self.column = column
        self.column10 = column10 if column10 is not None else set()
        self.column13 = column13 if column13 is not None else set()
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def column(self):
        return self.__column

    @column.setter
    def column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleRdbms_Column__column", None)
        self.__column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Table8"):
                opp_val = getattr(old_value, "Table8", None)
                if opp_val == self:
                    setattr(old_value, "Table8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Table8"):
                opp_val = getattr(value, "Table8", None)
                setattr(value, "Table8", self)

    @property
    def Column16(self):
        return self.__Column16

    @Column16.setter
    def Column16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleRdbms_Column__Column16", None)
        self.__Column16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "key"):
                opp_val = getattr(old_value, "key", None)
                if opp_val == self:
                    setattr(old_value, "key", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "key"):
                opp_val = getattr(value, "key", None)
                setattr(value, "key", self)

    @property
    def Column21(self):
        return self.__Column21

    @Column21.setter
    def Column21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleRdbms_Column__Column21", None)
        self.__Column21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "foreignKey"):
                opp_val = getattr(old_value, "foreignKey", None)
                if opp_val == self:
                    setattr(old_value, "foreignKey", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "foreignKey"):
                opp_val = getattr(value, "foreignKey", None)
                setattr(value, "foreignKey", self)

    @property
    def column13(self):
        return self.__column13

    @column13.setter
    def column13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleRdbms_Column__column13", None)
        self.__column13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ForeignKey14"):
                    opp_val = getattr(item, "ForeignKey14", None)
                    
                    if opp_val == self:
                        setattr(item, "ForeignKey14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ForeignKey14"):
                    opp_val = getattr(item, "ForeignKey14", None)
                    
                    setattr(item, "ForeignKey14", self)
                    

    @property
    def Column(self):
        return self.__Column

    @Column.setter
    def Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleRdbms_Column__Column", None)
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
    def column10(self):
        return self.__column10

    @column10.setter
    def column10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleRdbms_Column__column10", None)
        self.__column10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Key11"):
                    opp_val = getattr(item, "Key11", None)
                    
                    if opp_val == self:
                        setattr(item, "Key11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Key11"):
                    opp_val = getattr(item, "Key11", None)
                    
                    setattr(item, "Key11", self)
                    
