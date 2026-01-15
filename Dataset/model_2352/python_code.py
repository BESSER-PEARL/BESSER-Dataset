from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class SimpleRDBMS_RModelElement:

    def __init__(self, kind: str, name: str):
        self.kind = kind
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

class RModelElement:

    pass
class SimpleRDBMS_Schema(RModelElement):

    pass
class SimpleRDBMS_Column(RModelElement):

    def __init__(self, type: str, Column: "SimpleRDBMS_Table" = None, column11: set["SimpleRDBMS_ForeignKey"] = None, Column14: "SimpleRDBMS_Key" = None, Column19: "SimpleRDBMS_ForeignKey" = None, column: "SimpleRDBMS_Table" = None, column8: set["SimpleRDBMS_Key"] = None):
        self.type = type
        self.Column = Column
        self.column11 = column11 if column11 is not None else set()
        self.Column14 = Column14
        self.Column19 = Column19
        self.column = column
        self.column8 = column8 if column8 is not None else set()
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def Column(self):
        return self.__Column

    @Column.setter
    def Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimpleRDBMS_Column__Column", None)
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
    def column11(self):
        return self.__column11

    @column11.setter
    def column11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimpleRDBMS_Column__column11", None)
        self.__column11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ForeignKey12"):
                    opp_val = getattr(item, "ForeignKey12", None)
                    
                    if opp_val == self:
                        setattr(item, "ForeignKey12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ForeignKey12"):
                    opp_val = getattr(item, "ForeignKey12", None)
                    
                    setattr(item, "ForeignKey12", self)
                    

    @property
    def Column19(self):
        return self.__Column19

    @Column19.setter
    def Column19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimpleRDBMS_Column__Column19", None)
        self.__Column19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "foreignKey"):
                opp_val = getattr(old_value, "foreignKey", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "foreignKey"):
                opp_val = getattr(value, "foreignKey", None)
                if opp_val is None:
                    setattr(value, "foreignKey", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def column(self):
        return self.__column

    @column.setter
    def column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimpleRDBMS_Column__column", None)
        self.__column = value
        
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
    def Column14(self):
        return self.__Column14

    @Column14.setter
    def Column14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimpleRDBMS_Column__Column14", None)
        self.__Column14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "_key"):
                opp_val = getattr(old_value, "_key", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "_key"):
                opp_val = getattr(value, "_key", None)
                if opp_val is None:
                    setattr(value, "_key", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def column8(self):
        return self.__column8

    @column8.setter
    def column8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimpleRDBMS_Column__column8", None)
        self.__column8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Key9"):
                    opp_val = getattr(item, "Key9", None)
                    
                    if opp_val == self:
                        setattr(item, "Key9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Key9"):
                    opp_val = getattr(item, "Key9", None)
                    
                    setattr(item, "Key9", self)
                    

class SimpleRDBMS_Key(RModelElement):

    pass
class SimpleRDBMS_ForeignKey(RModelElement):

    pass
class SimpleRDBMS_Table(RModelElement):

    pass