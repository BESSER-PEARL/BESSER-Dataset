from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class rdbmsMM_dummy:

    pass
class rdbmsMM_Table:

    def __init__(self, name: str, table: "rdbmsMM_Schema" = None, owner: set["rdbmsMM_Column"] = None, owner6: "rdbmsMM_Key" = None, Table: "rdbmsMM_Schema" = None, Table19: "rdbmsMM_Key" = None, owner8: set["rdbmsMM_ForeignKey"] = None, Table11: "rdbmsMM_Column" = None, Table30: "rdbmsMM_ForeignKey" = None):
        self.name = name
        self.table = table
        self.owner = owner if owner is not None else set()
        self.owner6 = owner6
        self.Table = Table
        self.Table19 = Table19
        self.owner8 = owner8 if owner8 is not None else set()
        self.Table11 = Table11
        self.Table30 = Table30
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbmsMM_Table__owner", None)
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
    def Table11(self):
        return self.__Table11

    @Table11.setter
    def Table11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbmsMM_Table__Table11", None)
        self.__Table11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "column"):
                opp_val = getattr(old_value, "column", None)
                if opp_val == self:
                    setattr(old_value, "column", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "column"):
                opp_val = getattr(value, "column", None)
                setattr(value, "column", self)

    @property
    def table(self):
        return self.__table

    @table.setter
    def table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbmsMM_Table__table", None)
        self.__table = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Schema"):
                opp_val = getattr(old_value, "Schema", None)
                if opp_val == self:
                    setattr(old_value, "Schema", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Schema"):
                opp_val = getattr(value, "Schema", None)
                setattr(value, "Schema", self)

    @property
    def Table(self):
        return self.__Table

    @Table.setter
    def Table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbmsMM_Table__Table", None)
        self.__Table = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "schema"):
                opp_val = getattr(old_value, "schema", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "schema"):
                opp_val = getattr(value, "schema", None)
                if opp_val is None:
                    setattr(value, "schema", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def owner8(self):
        return self.__owner8

    @owner8.setter
    def owner8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbmsMM_Table__owner8", None)
        self.__owner8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ForeignKey9"):
                    opp_val = getattr(item, "ForeignKey9", None)
                    
                    if opp_val == self:
                        setattr(item, "ForeignKey9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ForeignKey9"):
                    opp_val = getattr(item, "ForeignKey9", None)
                    
                    setattr(item, "ForeignKey9", self)
                    

    @property
    def owner6(self):
        return self.__owner6

    @owner6.setter
    def owner6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbmsMM_Table__owner6", None)
        self.__owner6 = value
        
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

    @property
    def Table30(self):
        return self.__Table30

    @Table30.setter
    def Table30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbmsMM_Table__Table30", None)
        self.__Table30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hasForeignKey"):
                opp_val = getattr(old_value, "hasForeignKey", None)
                if opp_val == self:
                    setattr(old_value, "hasForeignKey", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hasForeignKey"):
                opp_val = getattr(value, "hasForeignKey", None)
                setattr(value, "hasForeignKey", self)

    @property
    def Table19(self):
        return self.__Table19

    @Table19.setter
    def Table19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbmsMM_Table__Table19", None)
        self.__Table19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hasKey"):
                opp_val = getattr(old_value, "hasKey", None)
                if opp_val == self:
                    setattr(old_value, "hasKey", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hasKey"):
                opp_val = getattr(value, "hasKey", None)
                setattr(value, "hasKey", self)

class rdbmsMM_Schema:

    def __init__(self, name: str, schema2: set["rdbmsMM_ForeignKey"] = None, Schema: "rdbmsMM_Table" = None, schema: set["rdbmsMM_Table"] = None, Schema26: "rdbmsMM_ForeignKey" = None, rdbmsMM_Schema: "rdbmsMM_dummy" = None):
        self.name = name
        self.schema2 = schema2 if schema2 is not None else set()
        self.Schema = Schema
        self.schema = schema if schema is not None else set()
        self.Schema26 = Schema26
        self.rdbmsMM_Schema = rdbmsMM_Schema
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Schema26(self):
        return self.__Schema26

    @Schema26.setter
    def Schema26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbmsMM_Schema__Schema26", None)
        self.__Schema26 = value
        
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
    def Schema(self):
        return self.__Schema

    @Schema.setter
    def Schema(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbmsMM_Schema__Schema", None)
        self.__Schema = value
        
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

    @property
    def schema2(self):
        return self.__schema2

    @schema2.setter
    def schema2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbmsMM_Schema__schema2", None)
        self.__schema2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ForeignKey"):
                    opp_val = getattr(item, "ForeignKey", None)
                    
                    if opp_val == self:
                        setattr(item, "ForeignKey", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ForeignKey"):
                    opp_val = getattr(item, "ForeignKey", None)
                    
                    setattr(item, "ForeignKey", self)
                    

    @property
    def schema(self):
        return self.__schema

    @schema.setter
    def schema(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbmsMM_Schema__schema", None)
        self.__schema = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Table"):
                    opp_val = getattr(item, "Table", None)
                    
                    if opp_val == self:
                        setattr(item, "Table", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Table"):
                    opp_val = getattr(item, "Table", None)
                    
                    setattr(item, "Table", self)
                    

    @property
    def rdbmsMM_Schema(self):
        return self.__rdbmsMM_Schema

    @rdbmsMM_Schema.setter
    def rdbmsMM_Schema(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbmsMM_Schema__rdbmsMM_Schema", None)
        self.__rdbmsMM_Schema = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbmsMM_dummy"):
                opp_val = getattr(old_value, "rdbmsMM_dummy", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbmsMM_dummy"):
                opp_val = getattr(value, "rdbmsMM_dummy", None)
                if opp_val is None:
                    setattr(value, "rdbmsMM_dummy", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class rdbmsMM_Key:

    def __init__(self, name: str, Key: "rdbmsMM_Table" = None, hasKey: "rdbmsMM_Table" = None, hasKey21: set["rdbmsMM_Column"] = None, refersTo: set["rdbmsMM_ForeignKey"] = None, Key14: "rdbmsMM_Column" = None, Key28: "rdbmsMM_ForeignKey" = None):
        self.name = name
        self.Key = Key
        self.hasKey = hasKey
        self.hasKey21 = hasKey21 if hasKey21 is not None else set()
        self.refersTo = refersTo if refersTo is not None else set()
        self.Key14 = Key14
        self.Key28 = Key28
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Key28(self):
        return self.__Key28

    @Key28.setter
    def Key28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbmsMM_Key__Key28", None)
        self.__Key28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "referredBy"):
                opp_val = getattr(old_value, "referredBy", None)
                if opp_val == self:
                    setattr(old_value, "referredBy", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "referredBy"):
                opp_val = getattr(value, "referredBy", None)
                setattr(value, "referredBy", self)

    @property
    def Key14(self):
        return self.__Key14

    @Key14.setter
    def Key14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbmsMM_Key__Key14", None)
        self.__Key14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "column13"):
                opp_val = getattr(old_value, "column13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "column13"):
                opp_val = getattr(value, "column13", None)
                if opp_val is None:
                    setattr(value, "column13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def hasKey21(self):
        return self.__hasKey21

    @hasKey21.setter
    def hasKey21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbmsMM_Key__hasKey21", None)
        self.__hasKey21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Column22"):
                    opp_val = getattr(item, "Column22", None)
                    
                    if opp_val == self:
                        setattr(item, "Column22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Column22"):
                    opp_val = getattr(item, "Column22", None)
                    
                    setattr(item, "Column22", self)
                    

    @property
    def refersTo(self):
        return self.__refersTo

    @refersTo.setter
    def refersTo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbmsMM_Key__refersTo", None)
        self.__refersTo = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ForeignKey24"):
                    opp_val = getattr(item, "ForeignKey24", None)
                    
                    if opp_val == self:
                        setattr(item, "ForeignKey24", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ForeignKey24"):
                    opp_val = getattr(item, "ForeignKey24", None)
                    
                    setattr(item, "ForeignKey24", self)
                    

    @property
    def Key(self):
        return self.__Key

    @Key.setter
    def Key(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbmsMM_Key__Key", None)
        self.__Key = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owner6"):
                opp_val = getattr(old_value, "owner6", None)
                if opp_val == self:
                    setattr(old_value, "owner6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner6"):
                opp_val = getattr(value, "owner6", None)
                setattr(value, "owner6", self)

    @property
    def hasKey(self):
        return self.__hasKey

    @hasKey.setter
    def hasKey(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbmsMM_Key__hasKey", None)
        self.__hasKey = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Table19"):
                opp_val = getattr(old_value, "Table19", None)
                if opp_val == self:
                    setattr(old_value, "Table19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Table19"):
                opp_val = getattr(value, "Table19", None)
                setattr(value, "Table19", self)

class rdbmsMM_Column:

    def __init__(self, name: str, type: str, Column: "rdbmsMM_Table" = None, Column22: "rdbmsMM_Key" = None, column: "rdbmsMM_Table" = None, column13: set["rdbmsMM_Key"] = None, column16: set["rdbmsMM_ForeignKey"] = None, Column33: "rdbmsMM_ForeignKey" = None):
        self.name = name
        self.type = type
        self.Column = Column
        self.Column22 = Column22
        self.column = column
        self.column13 = column13 if column13 is not None else set()
        self.column16 = column16 if column16 is not None else set()
        self.Column33 = Column33
        
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
    def column16(self):
        return self.__column16

    @column16.setter
    def column16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbmsMM_Column__column16", None)
        self.__column16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ForeignKey17"):
                    opp_val = getattr(item, "ForeignKey17", None)
                    
                    if opp_val == self:
                        setattr(item, "ForeignKey17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ForeignKey17"):
                    opp_val = getattr(item, "ForeignKey17", None)
                    
                    setattr(item, "ForeignKey17", self)
                    

    @property
    def Column22(self):
        return self.__Column22

    @Column22.setter
    def Column22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbmsMM_Column__Column22", None)
        self.__Column22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hasKey21"):
                opp_val = getattr(old_value, "hasKey21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hasKey21"):
                opp_val = getattr(value, "hasKey21", None)
                if opp_val is None:
                    setattr(value, "hasKey21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def column(self):
        return self.__column

    @column.setter
    def column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbmsMM_Column__column", None)
        self.__column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Table11"):
                opp_val = getattr(old_value, "Table11", None)
                if opp_val == self:
                    setattr(old_value, "Table11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Table11"):
                opp_val = getattr(value, "Table11", None)
                setattr(value, "Table11", self)

    @property
    def Column(self):
        return self.__Column

    @Column.setter
    def Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbmsMM_Column__Column", None)
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
    def column13(self):
        return self.__column13

    @column13.setter
    def column13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbmsMM_Column__column13", None)
        self.__column13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Key14"):
                    opp_val = getattr(item, "Key14", None)
                    
                    if opp_val == self:
                        setattr(item, "Key14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Key14"):
                    opp_val = getattr(item, "Key14", None)
                    
                    setattr(item, "Key14", self)
                    

    @property
    def Column33(self):
        return self.__Column33

    @Column33.setter
    def Column33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbmsMM_Column__Column33", None)
        self.__Column33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hasForeignKey32"):
                opp_val = getattr(old_value, "hasForeignKey32", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hasForeignKey32"):
                opp_val = getattr(value, "hasForeignKey32", None)
                if opp_val is None:
                    setattr(value, "hasForeignKey32", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class rdbmsMM_ForeignKey:

    def __init__(self, name: str, ForeignKey: "rdbmsMM_Schema" = None, ForeignKey9: "rdbmsMM_Table" = None, ForeignKey24: "rdbmsMM_Key" = None, foreignKey: "rdbmsMM_Schema" = None, ForeignKey17: "rdbmsMM_Column" = None, referredBy: "rdbmsMM_Key" = None, hasForeignKey: "rdbmsMM_Table" = None, hasForeignKey32: set["rdbmsMM_Column"] = None):
        self.name = name
        self.ForeignKey = ForeignKey
        self.ForeignKey9 = ForeignKey9
        self.ForeignKey24 = ForeignKey24
        self.foreignKey = foreignKey
        self.ForeignKey17 = ForeignKey17
        self.referredBy = referredBy
        self.hasForeignKey = hasForeignKey
        self.hasForeignKey32 = hasForeignKey32 if hasForeignKey32 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ForeignKey(self):
        return self.__ForeignKey

    @ForeignKey.setter
    def ForeignKey(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbmsMM_ForeignKey__ForeignKey", None)
        self.__ForeignKey = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "schema2"):
                opp_val = getattr(old_value, "schema2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "schema2"):
                opp_val = getattr(value, "schema2", None)
                if opp_val is None:
                    setattr(value, "schema2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def foreignKey(self):
        return self.__foreignKey

    @foreignKey.setter
    def foreignKey(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbmsMM_ForeignKey__foreignKey", None)
        self.__foreignKey = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Schema26"):
                opp_val = getattr(old_value, "Schema26", None)
                if opp_val == self:
                    setattr(old_value, "Schema26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Schema26"):
                opp_val = getattr(value, "Schema26", None)
                setattr(value, "Schema26", self)

    @property
    def ForeignKey17(self):
        return self.__ForeignKey17

    @ForeignKey17.setter
    def ForeignKey17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbmsMM_ForeignKey__ForeignKey17", None)
        self.__ForeignKey17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "column16"):
                opp_val = getattr(old_value, "column16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "column16"):
                opp_val = getattr(value, "column16", None)
                if opp_val is None:
                    setattr(value, "column16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ForeignKey24(self):
        return self.__ForeignKey24

    @ForeignKey24.setter
    def ForeignKey24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbmsMM_ForeignKey__ForeignKey24", None)
        self.__ForeignKey24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "refersTo"):
                opp_val = getattr(old_value, "refersTo", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "refersTo"):
                opp_val = getattr(value, "refersTo", None)
                if opp_val is None:
                    setattr(value, "refersTo", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def hasForeignKey32(self):
        return self.__hasForeignKey32

    @hasForeignKey32.setter
    def hasForeignKey32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbmsMM_ForeignKey__hasForeignKey32", None)
        self.__hasForeignKey32 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Column33"):
                    opp_val = getattr(item, "Column33", None)
                    
                    if opp_val == self:
                        setattr(item, "Column33", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Column33"):
                    opp_val = getattr(item, "Column33", None)
                    
                    setattr(item, "Column33", self)
                    

    @property
    def referredBy(self):
        return self.__referredBy

    @referredBy.setter
    def referredBy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbmsMM_ForeignKey__referredBy", None)
        self.__referredBy = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Key28"):
                opp_val = getattr(old_value, "Key28", None)
                if opp_val == self:
                    setattr(old_value, "Key28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Key28"):
                opp_val = getattr(value, "Key28", None)
                setattr(value, "Key28", self)

    @property
    def ForeignKey9(self):
        return self.__ForeignKey9

    @ForeignKey9.setter
    def ForeignKey9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbmsMM_ForeignKey__ForeignKey9", None)
        self.__ForeignKey9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owner8"):
                opp_val = getattr(old_value, "owner8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner8"):
                opp_val = getattr(value, "owner8", None)
                if opp_val is None:
                    setattr(value, "owner8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def hasForeignKey(self):
        return self.__hasForeignKey

    @hasForeignKey.setter
    def hasForeignKey(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbmsMM_ForeignKey__hasForeignKey", None)
        self.__hasForeignKey = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Table30"):
                opp_val = getattr(old_value, "Table30", None)
                if opp_val == self:
                    setattr(old_value, "Table30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Table30"):
                opp_val = getattr(value, "Table30", None)
                setattr(value, "Table30", self)
