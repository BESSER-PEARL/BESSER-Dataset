from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class relational_ForeignKey:

    pass
class relational_Key:

    def __init__(self, name: str, Key: "relational_Table" = None, relational_Key: set["relational_Column"] = None, refersTo: "relational_ForeignKey" = None, key: "relational_Table" = None, relational_Key13: "relational_ForeignKey" = None):
        self.name = name
        self.Key = Key
        self.relational_Key = relational_Key if relational_Key is not None else set()
        self.refersTo = refersTo
        self.key = key
        self.relational_Key13 = relational_Key13
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def refersTo(self):
        return self.__refersTo

    @refersTo.setter
    def refersTo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_Key__refersTo", None)
        self.__refersTo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ForeignKey7"):
                opp_val = getattr(old_value, "ForeignKey7", None)
                if opp_val == self:
                    setattr(old_value, "ForeignKey7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ForeignKey7"):
                opp_val = getattr(value, "ForeignKey7", None)
                setattr(value, "ForeignKey7", self)

    @property
    def relational_Key13(self):
        return self.__relational_Key13

    @relational_Key13.setter
    def relational_Key13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_Key__relational_Key13", None)
        self.__relational_Key13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "relational_ForeignKey12"):
                opp_val = getattr(old_value, "relational_ForeignKey12", None)
                if opp_val == self:
                    setattr(old_value, "relational_ForeignKey12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "relational_ForeignKey12"):
                opp_val = getattr(value, "relational_ForeignKey12", None)
                setattr(value, "relational_ForeignKey12", self)

    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_Key__key", None)
        self.__key = value
        
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
    def relational_Key(self):
        return self.__relational_Key

    @relational_Key.setter
    def relational_Key(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_Key__relational_Key", None)
        self.__relational_Key = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "relational_Column5"):
                    opp_val = getattr(item, "relational_Column5", None)
                    
                    if opp_val == self:
                        setattr(item, "relational_Column5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "relational_Column5"):
                    opp_val = getattr(item, "relational_Column5", None)
                    
                    setattr(item, "relational_Column5", self)
                    

    @property
    def Key(self):
        return self.__Key

    @Key.setter
    def Key(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_Key__Key", None)
        self.__Key = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "table"):
                opp_val = getattr(old_value, "table", None)
                if opp_val == self:
                    setattr(old_value, "table", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "table"):
                opp_val = getattr(value, "table", None)
                setattr(value, "table", self)

class relational_Table:

    def __init__(self, name: str, relational_Table: set["relational_Column"] = None, table: "relational_Key" = None, table3: "relational_ForeignKey" = None, Table: "relational_Key" = None, relational_Table16: "relational_ForeignKey" = None):
        self.name = name
        self.relational_Table = relational_Table if relational_Table is not None else set()
        self.table = table
        self.table3 = table3
        self.Table = Table
        self.relational_Table16 = relational_Table16
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def relational_Table(self):
        return self.__relational_Table

    @relational_Table.setter
    def relational_Table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_Table__relational_Table", None)
        self.__relational_Table = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "relational_Column"):
                    opp_val = getattr(item, "relational_Column", None)
                    
                    if opp_val == self:
                        setattr(item, "relational_Column", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "relational_Column"):
                    opp_val = getattr(item, "relational_Column", None)
                    
                    setattr(item, "relational_Column", self)
                    

    @property
    def table3(self):
        return self.__table3

    @table3.setter
    def table3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_Table__table3", None)
        self.__table3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ForeignKey"):
                opp_val = getattr(old_value, "ForeignKey", None)
                if opp_val == self:
                    setattr(old_value, "ForeignKey", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ForeignKey"):
                opp_val = getattr(value, "ForeignKey", None)
                setattr(value, "ForeignKey", self)

    @property
    def Table(self):
        return self.__Table

    @Table.setter
    def Table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_Table__Table", None)
        self.__Table = value
        
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
    def relational_Table16(self):
        return self.__relational_Table16

    @relational_Table16.setter
    def relational_Table16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_Table__relational_Table16", None)
        self.__relational_Table16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "relational_ForeignKey15"):
                opp_val = getattr(old_value, "relational_ForeignKey15", None)
                if opp_val == self:
                    setattr(old_value, "relational_ForeignKey15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "relational_ForeignKey15"):
                opp_val = getattr(value, "relational_ForeignKey15", None)
                setattr(value, "relational_ForeignKey15", self)

    @property
    def table(self):
        return self.__table

    @table.setter
    def table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_Table__table", None)
        self.__table = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Key"):
                opp_val = getattr(old_value, "Key", None)
                if opp_val == self:
                    setattr(old_value, "Key", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Key"):
                opp_val = getattr(value, "Key", None)
                setattr(value, "Key", self)

class relational_Column:

    def __init__(self, name: str, type: str, relational_Column: "relational_Table" = None, relational_Column5: "relational_Key" = None, relational_Column10: "relational_ForeignKey" = None):
        self.name = name
        self.type = type
        self.relational_Column = relational_Column
        self.relational_Column5 = relational_Column5
        self.relational_Column10 = relational_Column10
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def relational_Column(self):
        return self.__relational_Column

    @relational_Column.setter
    def relational_Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_Column__relational_Column", None)
        self.__relational_Column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "relational_Table"):
                opp_val = getattr(old_value, "relational_Table", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "relational_Table"):
                opp_val = getattr(value, "relational_Table", None)
                if opp_val is None:
                    setattr(value, "relational_Table", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def relational_Column10(self):
        return self.__relational_Column10

    @relational_Column10.setter
    def relational_Column10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_Column__relational_Column10", None)
        self.__relational_Column10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "relational_ForeignKey"):
                opp_val = getattr(old_value, "relational_ForeignKey", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "relational_ForeignKey"):
                opp_val = getattr(value, "relational_ForeignKey", None)
                if opp_val is None:
                    setattr(value, "relational_ForeignKey", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def relational_Column5(self):
        return self.__relational_Column5

    @relational_Column5.setter
    def relational_Column5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_Column__relational_Column5", None)
        self.__relational_Column5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "relational_Key"):
                opp_val = getattr(old_value, "relational_Key", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "relational_Key"):
                opp_val = getattr(value, "relational_Key", None)
                if opp_val is None:
                    setattr(value, "relational_Key", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
