from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class ER_Column:

    def __init__(self, name: str, type: str, column: "ER_Table" = None, Column: "ER_Table" = None, ER_Column: "ER_Key" = None, ER_Column18: set["ER_Key"] = None, column21: set["ER_ForeignKey"] = None, Column29: "ER_ForeignKey" = None):
        self.name = name
        self.type = type
        self.column = column
        self.Column = Column
        self.ER_Column = ER_Column
        self.ER_Column18 = ER_Column18 if ER_Column18 is not None else set()
        self.column21 = column21 if column21 is not None else set()
        self.Column29 = Column29
        
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
    def Column29(self):
        return self.__Column29

    @Column29.setter
    def Column29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ER_Column__Column29", None)
        self.__Column29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hasForeignKey28"):
                opp_val = getattr(old_value, "hasForeignKey28", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hasForeignKey28"):
                opp_val = getattr(value, "hasForeignKey28", None)
                if opp_val is None:
                    setattr(value, "hasForeignKey28", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Column(self):
        return self.__Column

    @Column.setter
    def Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ER_Column__Column", None)
        self.__Column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owner6"):
                opp_val = getattr(old_value, "owner6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner6"):
                opp_val = getattr(value, "owner6", None)
                if opp_val is None:
                    setattr(value, "owner6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def column21(self):
        return self.__column21

    @column21.setter
    def column21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ER_Column__column21", None)
        self.__column21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ForeignKey22"):
                    opp_val = getattr(item, "ForeignKey22", None)
                    
                    if opp_val == self:
                        setattr(item, "ForeignKey22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ForeignKey22"):
                    opp_val = getattr(item, "ForeignKey22", None)
                    
                    setattr(item, "ForeignKey22", self)
                    

    @property
    def ER_Column18(self):
        return self.__ER_Column18

    @ER_Column18.setter
    def ER_Column18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ER_Column__ER_Column18", None)
        self.__ER_Column18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ER_Key19"):
                    opp_val = getattr(item, "ER_Key19", None)
                    
                    if opp_val == self:
                        setattr(item, "ER_Key19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ER_Key19"):
                    opp_val = getattr(item, "ER_Key19", None)
                    
                    setattr(item, "ER_Key19", self)
                    

    @property
    def column(self):
        return self.__column

    @column.setter
    def column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ER_Column__column", None)
        self.__column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Table16"):
                opp_val = getattr(old_value, "Table16", None)
                if opp_val == self:
                    setattr(old_value, "Table16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Table16"):
                opp_val = getattr(value, "Table16", None)
                setattr(value, "Table16", self)

    @property
    def ER_Column(self):
        return self.__ER_Column

    @ER_Column.setter
    def ER_Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ER_Column__ER_Column", None)
        self.__ER_Column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ER_Key"):
                opp_val = getattr(old_value, "ER_Key", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ER_Key"):
                opp_val = getattr(value, "ER_Key", None)
                if opp_val is None:
                    setattr(value, "ER_Key", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ER_Key:

    def __init__(self, name: str, ER_Key14: set["ER_ForeignKey"] = None, Key: "ER_Table" = None, hasKey: "ER_Table" = None, ER_Key: set["ER_Column"] = None, ER_Key19: "ER_Column" = None, ER_Key32: "ER_ForeignKey" = None):
        self.name = name
        self.ER_Key14 = ER_Key14 if ER_Key14 is not None else set()
        self.Key = Key
        self.hasKey = hasKey
        self.ER_Key = ER_Key if ER_Key is not None else set()
        self.ER_Key19 = ER_Key19
        self.ER_Key32 = ER_Key32
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Key(self):
        return self.__Key

    @Key.setter
    def Key(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ER_Key__Key", None)
        self.__Key = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owner"):
                opp_val = getattr(old_value, "owner", None)
                if opp_val == self:
                    setattr(old_value, "owner", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner"):
                opp_val = getattr(value, "owner", None)
                setattr(value, "owner", self)

    @property
    def ER_Key19(self):
        return self.__ER_Key19

    @ER_Key19.setter
    def ER_Key19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ER_Key__ER_Key19", None)
        self.__ER_Key19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ER_Column18"):
                opp_val = getattr(old_value, "ER_Column18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ER_Column18"):
                opp_val = getattr(value, "ER_Column18", None)
                if opp_val is None:
                    setattr(value, "ER_Column18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ER_Key14(self):
        return self.__ER_Key14

    @ER_Key14.setter
    def ER_Key14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ER_Key__ER_Key14", None)
        self.__ER_Key14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ER_ForeignKey"):
                    opp_val = getattr(item, "ER_ForeignKey", None)
                    
                    if opp_val == self:
                        setattr(item, "ER_ForeignKey", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ER_ForeignKey"):
                    opp_val = getattr(item, "ER_ForeignKey", None)
                    
                    setattr(item, "ER_ForeignKey", self)
                    

    @property
    def ER_Key(self):
        return self.__ER_Key

    @ER_Key.setter
    def ER_Key(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ER_Key__ER_Key", None)
        self.__ER_Key = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ER_Column"):
                    opp_val = getattr(item, "ER_Column", None)
                    
                    if opp_val == self:
                        setattr(item, "ER_Column", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ER_Column"):
                    opp_val = getattr(item, "ER_Column", None)
                    
                    setattr(item, "ER_Column", self)
                    

    @property
    def ER_Key32(self):
        return self.__ER_Key32

    @ER_Key32.setter
    def ER_Key32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ER_Key__ER_Key32", None)
        self.__ER_Key32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ER_ForeignKey31"):
                opp_val = getattr(old_value, "ER_ForeignKey31", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ER_ForeignKey31"):
                opp_val = getattr(value, "ER_ForeignKey31", None)
                if opp_val is None:
                    setattr(value, "ER_ForeignKey31", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def hasKey(self):
        return self.__hasKey

    @hasKey.setter
    def hasKey(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ER_Key__hasKey", None)
        self.__hasKey = value
        
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

class ER_Table:

    def __init__(self, name: str, table: "ER_Schema" = None, Table: "ER_Schema" = None, Table16: "ER_Column" = None, owner: "ER_Key" = None, owner6: set["ER_Column"] = None, owner8: set["ER_ForeignKey"] = None, Table11: "ER_Key" = None, Table26: "ER_ForeignKey" = None):
        self.name = name
        self.table = table
        self.Table = Table
        self.Table16 = Table16
        self.owner = owner
        self.owner6 = owner6 if owner6 is not None else set()
        self.owner8 = owner8 if owner8 is not None else set()
        self.Table11 = Table11
        self.Table26 = Table26
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Table(self):
        return self.__Table

    @Table.setter
    def Table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ER_Table__Table", None)
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
    def owner6(self):
        return self.__owner6

    @owner6.setter
    def owner6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ER_Table__owner6", None)
        self.__owner6 = value if value is not None else set()
        
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
    def owner8(self):
        return self.__owner8

    @owner8.setter
    def owner8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ER_Table__owner8", None)
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
    def Table16(self):
        return self.__Table16

    @Table16.setter
    def Table16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ER_Table__Table16", None)
        self.__Table16 = value
        
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
    def Table26(self):
        return self.__Table26

    @Table26.setter
    def Table26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ER_Table__Table26", None)
        self.__Table26 = value
        
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
    def table(self):
        return self.__table

    @table.setter
    def table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ER_Table__table", None)
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
    def Table11(self):
        return self.__Table11

    @Table11.setter
    def Table11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ER_Table__Table11", None)
        self.__Table11 = value
        
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

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ER_Table__owner", None)
        self.__owner = value
        
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

class ER_Schema:

    def __init__(self, name: str, schema2: set["ER_ForeignKey"] = None, Schema: "ER_Table" = None, schema: set["ER_Table"] = None, Schema24: "ER_ForeignKey" = None):
        self.name = name
        self.schema2 = schema2 if schema2 is not None else set()
        self.Schema = Schema
        self.schema = schema if schema is not None else set()
        self.Schema24 = Schema24
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Schema24(self):
        return self.__Schema24

    @Schema24.setter
    def Schema24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ER_Schema__Schema24", None)
        self.__Schema24 = value
        
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
    def schema(self):
        return self.__schema

    @schema.setter
    def schema(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ER_Schema__schema", None)
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
    def schema2(self):
        return self.__schema2

    @schema2.setter
    def schema2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ER_Schema__schema2", None)
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
    def Schema(self):
        return self.__Schema

    @Schema.setter
    def Schema(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ER_Schema__Schema", None)
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

class ER_ForeignKey:

    def __init__(self, name: str, ForeignKey: "ER_Schema" = None, ER_ForeignKey: "ER_Key" = None, ForeignKey9: "ER_Table" = None, ForeignKey22: "ER_Column" = None, foreignKey: "ER_Schema" = None, hasForeignKey: "ER_Table" = None, hasForeignKey28: set["ER_Column"] = None, ER_ForeignKey31: set["ER_Key"] = None):
        self.name = name
        self.ForeignKey = ForeignKey
        self.ER_ForeignKey = ER_ForeignKey
        self.ForeignKey9 = ForeignKey9
        self.ForeignKey22 = ForeignKey22
        self.foreignKey = foreignKey
        self.hasForeignKey = hasForeignKey
        self.hasForeignKey28 = hasForeignKey28 if hasForeignKey28 is not None else set()
        self.ER_ForeignKey31 = ER_ForeignKey31 if ER_ForeignKey31 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ForeignKey22(self):
        return self.__ForeignKey22

    @ForeignKey22.setter
    def ForeignKey22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ER_ForeignKey__ForeignKey22", None)
        self.__ForeignKey22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "column21"):
                opp_val = getattr(old_value, "column21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "column21"):
                opp_val = getattr(value, "column21", None)
                if opp_val is None:
                    setattr(value, "column21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ER_ForeignKey(self):
        return self.__ER_ForeignKey

    @ER_ForeignKey.setter
    def ER_ForeignKey(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ER_ForeignKey__ER_ForeignKey", None)
        self.__ER_ForeignKey = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ER_Key14"):
                opp_val = getattr(old_value, "ER_Key14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ER_Key14"):
                opp_val = getattr(value, "ER_Key14", None)
                if opp_val is None:
                    setattr(value, "ER_Key14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ER_ForeignKey31(self):
        return self.__ER_ForeignKey31

    @ER_ForeignKey31.setter
    def ER_ForeignKey31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ER_ForeignKey__ER_ForeignKey31", None)
        self.__ER_ForeignKey31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ER_Key32"):
                    opp_val = getattr(item, "ER_Key32", None)
                    
                    if opp_val == self:
                        setattr(item, "ER_Key32", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ER_Key32"):
                    opp_val = getattr(item, "ER_Key32", None)
                    
                    setattr(item, "ER_Key32", self)
                    

    @property
    def ForeignKey9(self):
        return self.__ForeignKey9

    @ForeignKey9.setter
    def ForeignKey9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ER_ForeignKey__ForeignKey9", None)
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
    def hasForeignKey28(self):
        return self.__hasForeignKey28

    @hasForeignKey28.setter
    def hasForeignKey28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ER_ForeignKey__hasForeignKey28", None)
        self.__hasForeignKey28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Column29"):
                    opp_val = getattr(item, "Column29", None)
                    
                    if opp_val == self:
                        setattr(item, "Column29", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Column29"):
                    opp_val = getattr(item, "Column29", None)
                    
                    setattr(item, "Column29", self)
                    

    @property
    def ForeignKey(self):
        return self.__ForeignKey

    @ForeignKey.setter
    def ForeignKey(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ER_ForeignKey__ForeignKey", None)
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
    def hasForeignKey(self):
        return self.__hasForeignKey

    @hasForeignKey.setter
    def hasForeignKey(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ER_ForeignKey__hasForeignKey", None)
        self.__hasForeignKey = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Table26"):
                opp_val = getattr(old_value, "Table26", None)
                if opp_val == self:
                    setattr(old_value, "Table26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Table26"):
                opp_val = getattr(value, "Table26", None)
                setattr(value, "Table26", self)

    @property
    def foreignKey(self):
        return self.__foreignKey

    @foreignKey.setter
    def foreignKey(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ER_ForeignKey__foreignKey", None)
        self.__foreignKey = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Schema24"):
                opp_val = getattr(old_value, "Schema24", None)
                if opp_val == self:
                    setattr(old_value, "Schema24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Schema24"):
                opp_val = getattr(value, "Schema24", None)
                setattr(value, "Schema24", self)
