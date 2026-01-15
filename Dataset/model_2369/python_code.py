from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class rdbms_tables:

    def __init__(self, group: str, rdbms_tables: "rdbms_DocumentRoot" = None, rdbms_tables69: "rdbms_schema" = None, rdbms_tables83: set["rdbms_table"] = None):
        self.group = group
        self.rdbms_tables = rdbms_tables
        self.rdbms_tables69 = rdbms_tables69
        self.rdbms_tables83 = rdbms_tables83 if rdbms_tables83 is not None else set()
        
    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def rdbms_tables(self):
        return self.__rdbms_tables

    @rdbms_tables.setter
    def rdbms_tables(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_tables__rdbms_tables", None)
        self.__rdbms_tables = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_DocumentRoot42"):
                opp_val = getattr(old_value, "rdbms_DocumentRoot42", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_DocumentRoot42"):
                opp_val = getattr(value, "rdbms_DocumentRoot42", None)
                if opp_val is None:
                    setattr(value, "rdbms_DocumentRoot42", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rdbms_tables83(self):
        return self.__rdbms_tables83

    @rdbms_tables83.setter
    def rdbms_tables83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_tables__rdbms_tables83", None)
        self.__rdbms_tables83 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rdbms_table84"):
                    opp_val = getattr(item, "rdbms_table84", None)
                    
                    if opp_val == self:
                        setattr(item, "rdbms_table84", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rdbms_table84"):
                    opp_val = getattr(item, "rdbms_table84", None)
                    
                    setattr(item, "rdbms_table84", self)
                    

    @property
    def rdbms_tables69(self):
        return self.__rdbms_tables69

    @rdbms_tables69.setter
    def rdbms_tables69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_tables__rdbms_tables69", None)
        self.__rdbms_tables69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_schema68"):
                opp_val = getattr(old_value, "rdbms_schema68", None)
                if opp_val == self:
                    setattr(old_value, "rdbms_schema68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_schema68"):
                opp_val = getattr(value, "rdbms_schema68", None)
                setattr(value, "rdbms_schema68", self)

class rdbms_referencedColumns:

    def __init__(self, group: str, rdbms_referencedColumns: "rdbms_DocumentRoot" = None, rdbms_referencedColumns45: "rdbms_foreignKey" = None, rdbms_referencedColumns54: "rdbms_key" = None, rdbms_referencedColumns62: set["rdbms_oID"] = None):
        self.group = group
        self.rdbms_referencedColumns = rdbms_referencedColumns
        self.rdbms_referencedColumns45 = rdbms_referencedColumns45
        self.rdbms_referencedColumns54 = rdbms_referencedColumns54
        self.rdbms_referencedColumns62 = rdbms_referencedColumns62 if rdbms_referencedColumns62 is not None else set()
        
    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def rdbms_referencedColumns54(self):
        return self.__rdbms_referencedColumns54

    @rdbms_referencedColumns54.setter
    def rdbms_referencedColumns54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_referencedColumns__rdbms_referencedColumns54", None)
        self.__rdbms_referencedColumns54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_key53"):
                opp_val = getattr(old_value, "rdbms_key53", None)
                if opp_val == self:
                    setattr(old_value, "rdbms_key53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_key53"):
                opp_val = getattr(value, "rdbms_key53", None)
                setattr(value, "rdbms_key53", self)

    @property
    def rdbms_referencedColumns(self):
        return self.__rdbms_referencedColumns

    @rdbms_referencedColumns.setter
    def rdbms_referencedColumns(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_referencedColumns__rdbms_referencedColumns", None)
        self.__rdbms_referencedColumns = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_DocumentRoot31"):
                opp_val = getattr(old_value, "rdbms_DocumentRoot31", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_DocumentRoot31"):
                opp_val = getattr(value, "rdbms_DocumentRoot31", None)
                if opp_val is None:
                    setattr(value, "rdbms_DocumentRoot31", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rdbms_referencedColumns45(self):
        return self.__rdbms_referencedColumns45

    @rdbms_referencedColumns45.setter
    def rdbms_referencedColumns45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_referencedColumns__rdbms_referencedColumns45", None)
        self.__rdbms_referencedColumns45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_foreignKey44"):
                opp_val = getattr(old_value, "rdbms_foreignKey44", None)
                if opp_val == self:
                    setattr(old_value, "rdbms_foreignKey44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_foreignKey44"):
                opp_val = getattr(value, "rdbms_foreignKey44", None)
                setattr(value, "rdbms_foreignKey44", self)

    @property
    def rdbms_referencedColumns62(self):
        return self.__rdbms_referencedColumns62

    @rdbms_referencedColumns62.setter
    def rdbms_referencedColumns62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_referencedColumns__rdbms_referencedColumns62", None)
        self.__rdbms_referencedColumns62 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rdbms_oID63"):
                    opp_val = getattr(item, "rdbms_oID63", None)
                    
                    if opp_val == self:
                        setattr(item, "rdbms_oID63", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rdbms_oID63"):
                    opp_val = getattr(item, "rdbms_oID63", None)
                    
                    setattr(item, "rdbms_oID63", self)
                    

class rdbms_table:

    def __init__(self, kind: str, name: str, oID: str, rdbms_table: "rdbms_DocumentRoot" = None, rdbms_table77: "rdbms_columns" = None, rdbms_table80: "rdbms_key2" = None, rdbms_table84: "rdbms_tables" = None):
        self.kind = kind
        self.name = name
        self.oID = oID
        self.rdbms_table = rdbms_table
        self.rdbms_table77 = rdbms_table77
        self.rdbms_table80 = rdbms_table80
        self.rdbms_table84 = rdbms_table84
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def oID(self) -> str:
        return self.__oID

    @oID.setter
    def oID(self, oID: str):
        self.__oID = oID

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def rdbms_table84(self):
        return self.__rdbms_table84

    @rdbms_table84.setter
    def rdbms_table84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_table__rdbms_table84", None)
        self.__rdbms_table84 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_tables83"):
                opp_val = getattr(old_value, "rdbms_tables83", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_tables83"):
                opp_val = getattr(value, "rdbms_tables83", None)
                if opp_val is None:
                    setattr(value, "rdbms_tables83", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rdbms_table80(self):
        return self.__rdbms_table80

    @rdbms_table80.setter
    def rdbms_table80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_table__rdbms_table80", None)
        self.__rdbms_table80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_key281"):
                opp_val = getattr(old_value, "rdbms_key281", None)
                if opp_val == self:
                    setattr(old_value, "rdbms_key281", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_key281"):
                opp_val = getattr(value, "rdbms_key281", None)
                setattr(value, "rdbms_key281", self)

    @property
    def rdbms_table(self):
        return self.__rdbms_table

    @rdbms_table.setter
    def rdbms_table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_table__rdbms_table", None)
        self.__rdbms_table = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_DocumentRoot40"):
                opp_val = getattr(old_value, "rdbms_DocumentRoot40", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_DocumentRoot40"):
                opp_val = getattr(value, "rdbms_DocumentRoot40", None)
                if opp_val is None:
                    setattr(value, "rdbms_DocumentRoot40", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rdbms_table77(self):
        return self.__rdbms_table77

    @rdbms_table77.setter
    def rdbms_table77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_table__rdbms_table77", None)
        self.__rdbms_table77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_columns78"):
                opp_val = getattr(old_value, "rdbms_columns78", None)
                if opp_val == self:
                    setattr(old_value, "rdbms_columns78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_columns78"):
                opp_val = getattr(value, "rdbms_columns78", None)
                setattr(value, "rdbms_columns78", self)

class rdbms_schemas:

    def __init__(self, group: str, rdbms_schemas: "rdbms_DocumentRoot" = None, rdbms_schemas60: "rdbms_RDBMS" = None, rdbms_schemas74: set["rdbms_schema"] = None):
        self.group = group
        self.rdbms_schemas = rdbms_schemas
        self.rdbms_schemas60 = rdbms_schemas60
        self.rdbms_schemas74 = rdbms_schemas74 if rdbms_schemas74 is not None else set()
        
    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def rdbms_schemas74(self):
        return self.__rdbms_schemas74

    @rdbms_schemas74.setter
    def rdbms_schemas74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_schemas__rdbms_schemas74", None)
        self.__rdbms_schemas74 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rdbms_schema75"):
                    opp_val = getattr(item, "rdbms_schema75", None)
                    
                    if opp_val == self:
                        setattr(item, "rdbms_schema75", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rdbms_schema75"):
                    opp_val = getattr(item, "rdbms_schema75", None)
                    
                    setattr(item, "rdbms_schema75", self)
                    

    @property
    def rdbms_schemas60(self):
        return self.__rdbms_schemas60

    @rdbms_schemas60.setter
    def rdbms_schemas60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_schemas__rdbms_schemas60", None)
        self.__rdbms_schemas60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_RDBMS59"):
                opp_val = getattr(old_value, "rdbms_RDBMS59", None)
                if opp_val == self:
                    setattr(old_value, "rdbms_RDBMS59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_RDBMS59"):
                opp_val = getattr(value, "rdbms_RDBMS59", None)
                setattr(value, "rdbms_RDBMS59", self)

    @property
    def rdbms_schemas(self):
        return self.__rdbms_schemas

    @rdbms_schemas.setter
    def rdbms_schemas(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_schemas__rdbms_schemas", None)
        self.__rdbms_schemas = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_DocumentRoot38"):
                opp_val = getattr(old_value, "rdbms_DocumentRoot38", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_DocumentRoot38"):
                opp_val = getattr(value, "rdbms_DocumentRoot38", None)
                if opp_val is None:
                    setattr(value, "rdbms_DocumentRoot38", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class rdbms_schema:

    def __init__(self, kind: str, name: str, oID: str, rdbms_schema: "rdbms_DocumentRoot" = None, rdbms_schema71: "rdbms_foreignKeys" = None, rdbms_schema68: "rdbms_tables" = None, rdbms_schema75: "rdbms_schemas" = None):
        self.kind = kind
        self.name = name
        self.oID = oID
        self.rdbms_schema = rdbms_schema
        self.rdbms_schema71 = rdbms_schema71
        self.rdbms_schema68 = rdbms_schema68
        self.rdbms_schema75 = rdbms_schema75
        
    @property
    def oID(self) -> str:
        return self.__oID

    @oID.setter
    def oID(self, oID: str):
        self.__oID = oID

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

    @property
    def rdbms_schema71(self):
        return self.__rdbms_schema71

    @rdbms_schema71.setter
    def rdbms_schema71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_schema__rdbms_schema71", None)
        self.__rdbms_schema71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_foreignKeys72"):
                opp_val = getattr(old_value, "rdbms_foreignKeys72", None)
                if opp_val == self:
                    setattr(old_value, "rdbms_foreignKeys72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_foreignKeys72"):
                opp_val = getattr(value, "rdbms_foreignKeys72", None)
                setattr(value, "rdbms_foreignKeys72", self)

    @property
    def rdbms_schema75(self):
        return self.__rdbms_schema75

    @rdbms_schema75.setter
    def rdbms_schema75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_schema__rdbms_schema75", None)
        self.__rdbms_schema75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_schemas74"):
                opp_val = getattr(old_value, "rdbms_schemas74", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_schemas74"):
                opp_val = getattr(value, "rdbms_schemas74", None)
                if opp_val is None:
                    setattr(value, "rdbms_schemas74", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rdbms_schema68(self):
        return self.__rdbms_schema68

    @rdbms_schema68.setter
    def rdbms_schema68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_schema__rdbms_schema68", None)
        self.__rdbms_schema68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_tables69"):
                opp_val = getattr(old_value, "rdbms_tables69", None)
                if opp_val == self:
                    setattr(old_value, "rdbms_tables69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_tables69"):
                opp_val = getattr(value, "rdbms_tables69", None)
                setattr(value, "rdbms_tables69", self)

    @property
    def rdbms_schema(self):
        return self.__rdbms_schema

    @rdbms_schema.setter
    def rdbms_schema(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_schema__rdbms_schema", None)
        self.__rdbms_schema = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_DocumentRoot36"):
                opp_val = getattr(old_value, "rdbms_DocumentRoot36", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_DocumentRoot36"):
                opp_val = getattr(value, "rdbms_DocumentRoot36", None)
                if opp_val is None:
                    setattr(value, "rdbms_DocumentRoot36", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class rdbms_RDBMS:

    pass
class rdbms_oID:

    def __init__(self, oID: str, rdbms_oID: "rdbms_DocumentRoot" = None, rdbms_oID51: "rdbms_hasForeignKeys" = None, rdbms_oID63: "rdbms_referencedColumns" = None, rdbms_oID66: "rdbms_referencedKeys" = None):
        self.oID = oID
        self.rdbms_oID = rdbms_oID
        self.rdbms_oID51 = rdbms_oID51
        self.rdbms_oID63 = rdbms_oID63
        self.rdbms_oID66 = rdbms_oID66
        
    @property
    def oID(self) -> str:
        return self.__oID

    @oID.setter
    def oID(self, oID: str):
        self.__oID = oID

    @property
    def rdbms_oID63(self):
        return self.__rdbms_oID63

    @rdbms_oID63.setter
    def rdbms_oID63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_oID__rdbms_oID63", None)
        self.__rdbms_oID63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_referencedColumns62"):
                opp_val = getattr(old_value, "rdbms_referencedColumns62", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_referencedColumns62"):
                opp_val = getattr(value, "rdbms_referencedColumns62", None)
                if opp_val is None:
                    setattr(value, "rdbms_referencedColumns62", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rdbms_oID(self):
        return self.__rdbms_oID

    @rdbms_oID.setter
    def rdbms_oID(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_oID__rdbms_oID", None)
        self.__rdbms_oID = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_DocumentRoot27"):
                opp_val = getattr(old_value, "rdbms_DocumentRoot27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_DocumentRoot27"):
                opp_val = getattr(value, "rdbms_DocumentRoot27", None)
                if opp_val is None:
                    setattr(value, "rdbms_DocumentRoot27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rdbms_oID51(self):
        return self.__rdbms_oID51

    @rdbms_oID51.setter
    def rdbms_oID51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_oID__rdbms_oID51", None)
        self.__rdbms_oID51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_hasForeignKeys50"):
                opp_val = getattr(old_value, "rdbms_hasForeignKeys50", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_hasForeignKeys50"):
                opp_val = getattr(value, "rdbms_hasForeignKeys50", None)
                if opp_val is None:
                    setattr(value, "rdbms_hasForeignKeys50", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rdbms_oID66(self):
        return self.__rdbms_oID66

    @rdbms_oID66.setter
    def rdbms_oID66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_oID__rdbms_oID66", None)
        self.__rdbms_oID66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_referencedKeys65"):
                opp_val = getattr(old_value, "rdbms_referencedKeys65", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_referencedKeys65"):
                opp_val = getattr(value, "rdbms_referencedKeys65", None)
                if opp_val is None:
                    setattr(value, "rdbms_referencedKeys65", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class rdbms_key2:

    pass
class rdbms_key:

    def __init__(self, kind: str, name: str, oID: str, rdbms_key: "rdbms_DocumentRoot" = None, rdbms_key57: "rdbms_key2" = None, rdbms_key53: "rdbms_referencedColumns" = None):
        self.kind = kind
        self.name = name
        self.oID = oID
        self.rdbms_key = rdbms_key
        self.rdbms_key57 = rdbms_key57
        self.rdbms_key53 = rdbms_key53
        
    @property
    def oID(self) -> str:
        return self.__oID

    @oID.setter
    def oID(self, oID: str):
        self.__oID = oID

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

    @property
    def rdbms_key57(self):
        return self.__rdbms_key57

    @rdbms_key57.setter
    def rdbms_key57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_key__rdbms_key57", None)
        self.__rdbms_key57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_key256"):
                opp_val = getattr(old_value, "rdbms_key256", None)
                if opp_val == self:
                    setattr(old_value, "rdbms_key256", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_key256"):
                opp_val = getattr(value, "rdbms_key256", None)
                setattr(value, "rdbms_key256", self)

    @property
    def rdbms_key(self):
        return self.__rdbms_key

    @rdbms_key.setter
    def rdbms_key(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_key__rdbms_key", None)
        self.__rdbms_key = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_DocumentRoot23"):
                opp_val = getattr(old_value, "rdbms_DocumentRoot23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_DocumentRoot23"):
                opp_val = getattr(value, "rdbms_DocumentRoot23", None)
                if opp_val is None:
                    setattr(value, "rdbms_DocumentRoot23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rdbms_key53(self):
        return self.__rdbms_key53

    @rdbms_key53.setter
    def rdbms_key53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_key__rdbms_key53", None)
        self.__rdbms_key53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_referencedColumns54"):
                opp_val = getattr(old_value, "rdbms_referencedColumns54", None)
                if opp_val == self:
                    setattr(old_value, "rdbms_referencedColumns54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_referencedColumns54"):
                opp_val = getattr(value, "rdbms_referencedColumns54", None)
                setattr(value, "rdbms_referencedColumns54", self)

class rdbms_foreignKeys:

    def __init__(self, group: str, rdbms_foreignKeys: "rdbms_DocumentRoot" = None, rdbms_foreignKeys47: set["rdbms_foreignKey"] = None, rdbms_foreignKeys72: "rdbms_schema" = None):
        self.group = group
        self.rdbms_foreignKeys = rdbms_foreignKeys
        self.rdbms_foreignKeys47 = rdbms_foreignKeys47 if rdbms_foreignKeys47 is not None else set()
        self.rdbms_foreignKeys72 = rdbms_foreignKeys72
        
    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def rdbms_foreignKeys47(self):
        return self.__rdbms_foreignKeys47

    @rdbms_foreignKeys47.setter
    def rdbms_foreignKeys47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_foreignKeys__rdbms_foreignKeys47", None)
        self.__rdbms_foreignKeys47 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rdbms_foreignKey48"):
                    opp_val = getattr(item, "rdbms_foreignKey48", None)
                    
                    if opp_val == self:
                        setattr(item, "rdbms_foreignKey48", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rdbms_foreignKey48"):
                    opp_val = getattr(item, "rdbms_foreignKey48", None)
                    
                    setattr(item, "rdbms_foreignKey48", self)
                    

    @property
    def rdbms_foreignKeys(self):
        return self.__rdbms_foreignKeys

    @rdbms_foreignKeys.setter
    def rdbms_foreignKeys(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_foreignKeys__rdbms_foreignKeys", None)
        self.__rdbms_foreignKeys = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_DocumentRoot18"):
                opp_val = getattr(old_value, "rdbms_DocumentRoot18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_DocumentRoot18"):
                opp_val = getattr(value, "rdbms_DocumentRoot18", None)
                if opp_val is None:
                    setattr(value, "rdbms_DocumentRoot18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rdbms_foreignKeys72(self):
        return self.__rdbms_foreignKeys72

    @rdbms_foreignKeys72.setter
    def rdbms_foreignKeys72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_foreignKeys__rdbms_foreignKeys72", None)
        self.__rdbms_foreignKeys72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_schema71"):
                opp_val = getattr(old_value, "rdbms_schema71", None)
                if opp_val == self:
                    setattr(old_value, "rdbms_schema71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_schema71"):
                opp_val = getattr(value, "rdbms_schema71", None)
                setattr(value, "rdbms_schema71", self)

class rdbms_foreignKey:

    def __init__(self, kind: str, name: str, oID: str, owner: str, refersTo: str, rdbms_foreignKey: "rdbms_DocumentRoot" = None, rdbms_foreignKey44: "rdbms_referencedColumns" = None, rdbms_foreignKey48: "rdbms_foreignKeys" = None):
        self.kind = kind
        self.name = name
        self.oID = oID
        self.owner = owner
        self.refersTo = refersTo
        self.rdbms_foreignKey = rdbms_foreignKey
        self.rdbms_foreignKey44 = rdbms_foreignKey44
        self.rdbms_foreignKey48 = rdbms_foreignKey48
        
    @property
    def owner(self) -> str:
        return self.__owner

    @owner.setter
    def owner(self, owner: str):
        self.__owner = owner

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

    @property
    def refersTo(self) -> str:
        return self.__refersTo

    @refersTo.setter
    def refersTo(self, refersTo: str):
        self.__refersTo = refersTo

    @property
    def oID(self) -> str:
        return self.__oID

    @oID.setter
    def oID(self, oID: str):
        self.__oID = oID

    @property
    def rdbms_foreignKey44(self):
        return self.__rdbms_foreignKey44

    @rdbms_foreignKey44.setter
    def rdbms_foreignKey44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_foreignKey__rdbms_foreignKey44", None)
        self.__rdbms_foreignKey44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_referencedColumns45"):
                opp_val = getattr(old_value, "rdbms_referencedColumns45", None)
                if opp_val == self:
                    setattr(old_value, "rdbms_referencedColumns45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_referencedColumns45"):
                opp_val = getattr(value, "rdbms_referencedColumns45", None)
                setattr(value, "rdbms_referencedColumns45", self)

    @property
    def rdbms_foreignKey48(self):
        return self.__rdbms_foreignKey48

    @rdbms_foreignKey48.setter
    def rdbms_foreignKey48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_foreignKey__rdbms_foreignKey48", None)
        self.__rdbms_foreignKey48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_foreignKeys47"):
                opp_val = getattr(old_value, "rdbms_foreignKeys47", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_foreignKeys47"):
                opp_val = getattr(value, "rdbms_foreignKeys47", None)
                if opp_val is None:
                    setattr(value, "rdbms_foreignKeys47", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rdbms_foreignKey(self):
        return self.__rdbms_foreignKey

    @rdbms_foreignKey.setter
    def rdbms_foreignKey(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_foreignKey__rdbms_foreignKey", None)
        self.__rdbms_foreignKey = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_DocumentRoot16"):
                opp_val = getattr(old_value, "rdbms_DocumentRoot16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_DocumentRoot16"):
                opp_val = getattr(value, "rdbms_DocumentRoot16", None)
                if opp_val is None:
                    setattr(value, "rdbms_DocumentRoot16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class rdbms_columns:

    def __init__(self, group: str, rdbms_columns: set["rdbms_column"] = None, rdbms_columns14: "rdbms_DocumentRoot" = None, rdbms_columns78: "rdbms_table" = None):
        self.group = group
        self.rdbms_columns = rdbms_columns if rdbms_columns is not None else set()
        self.rdbms_columns14 = rdbms_columns14
        self.rdbms_columns78 = rdbms_columns78
        
    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def rdbms_columns78(self):
        return self.__rdbms_columns78

    @rdbms_columns78.setter
    def rdbms_columns78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_columns__rdbms_columns78", None)
        self.__rdbms_columns78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_table77"):
                opp_val = getattr(old_value, "rdbms_table77", None)
                if opp_val == self:
                    setattr(old_value, "rdbms_table77", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_table77"):
                opp_val = getattr(value, "rdbms_table77", None)
                setattr(value, "rdbms_table77", self)

    @property
    def rdbms_columns(self):
        return self.__rdbms_columns

    @rdbms_columns.setter
    def rdbms_columns(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_columns__rdbms_columns", None)
        self.__rdbms_columns = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rdbms_column4"):
                    opp_val = getattr(item, "rdbms_column4", None)
                    
                    if opp_val == self:
                        setattr(item, "rdbms_column4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rdbms_column4"):
                    opp_val = getattr(item, "rdbms_column4", None)
                    
                    setattr(item, "rdbms_column4", self)
                    

    @property
    def rdbms_columns14(self):
        return self.__rdbms_columns14

    @rdbms_columns14.setter
    def rdbms_columns14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_columns__rdbms_columns14", None)
        self.__rdbms_columns14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_DocumentRoot13"):
                opp_val = getattr(old_value, "rdbms_DocumentRoot13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_DocumentRoot13"):
                opp_val = getattr(value, "rdbms_DocumentRoot13", None)
                if opp_val is None:
                    setattr(value, "rdbms_DocumentRoot13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class rdbms_EStringToStringMapEntry:

    pass
class rdbms_DocumentRoot:

    def __init__(self, mixed: str, rdbms_DocumentRoot: set["rdbms_EStringToStringMapEntry"] = None, rdbms_DocumentRoot10: set["rdbms_column"] = None, rdbms_DocumentRoot13: set["rdbms_columns"] = None, rdbms_DocumentRoot16: set["rdbms_foreignKey"] = None, rdbms_DocumentRoot18: set["rdbms_foreignKeys"] = None, rdbms_DocumentRoot7: set["rdbms_EStringToStringMapEntry"] = None, rdbms_DocumentRoot23: set["rdbms_key"] = None, rdbms_DocumentRoot25: set["rdbms_key2"] = None, rdbms_DocumentRoot27: set["rdbms_oID"] = None, rdbms_DocumentRoot29: set["rdbms_RDBMS"] = None, rdbms_DocumentRoot20: set["rdbms_hasForeignKeys"] = None, rdbms_DocumentRoot33: set["rdbms_referencedKeys"] = None, rdbms_DocumentRoot36: set["rdbms_schema"] = None, rdbms_DocumentRoot38: set["rdbms_schemas"] = None, rdbms_DocumentRoot40: set["rdbms_table"] = None, rdbms_DocumentRoot31: set["rdbms_referencedColumns"] = None, rdbms_DocumentRoot42: set["rdbms_tables"] = None):
        self.mixed = mixed
        self.rdbms_DocumentRoot = rdbms_DocumentRoot if rdbms_DocumentRoot is not None else set()
        self.rdbms_DocumentRoot10 = rdbms_DocumentRoot10 if rdbms_DocumentRoot10 is not None else set()
        self.rdbms_DocumentRoot13 = rdbms_DocumentRoot13 if rdbms_DocumentRoot13 is not None else set()
        self.rdbms_DocumentRoot16 = rdbms_DocumentRoot16 if rdbms_DocumentRoot16 is not None else set()
        self.rdbms_DocumentRoot18 = rdbms_DocumentRoot18 if rdbms_DocumentRoot18 is not None else set()
        self.rdbms_DocumentRoot7 = rdbms_DocumentRoot7 if rdbms_DocumentRoot7 is not None else set()
        self.rdbms_DocumentRoot23 = rdbms_DocumentRoot23 if rdbms_DocumentRoot23 is not None else set()
        self.rdbms_DocumentRoot25 = rdbms_DocumentRoot25 if rdbms_DocumentRoot25 is not None else set()
        self.rdbms_DocumentRoot27 = rdbms_DocumentRoot27 if rdbms_DocumentRoot27 is not None else set()
        self.rdbms_DocumentRoot29 = rdbms_DocumentRoot29 if rdbms_DocumentRoot29 is not None else set()
        self.rdbms_DocumentRoot20 = rdbms_DocumentRoot20 if rdbms_DocumentRoot20 is not None else set()
        self.rdbms_DocumentRoot33 = rdbms_DocumentRoot33 if rdbms_DocumentRoot33 is not None else set()
        self.rdbms_DocumentRoot36 = rdbms_DocumentRoot36 if rdbms_DocumentRoot36 is not None else set()
        self.rdbms_DocumentRoot38 = rdbms_DocumentRoot38 if rdbms_DocumentRoot38 is not None else set()
        self.rdbms_DocumentRoot40 = rdbms_DocumentRoot40 if rdbms_DocumentRoot40 is not None else set()
        self.rdbms_DocumentRoot31 = rdbms_DocumentRoot31 if rdbms_DocumentRoot31 is not None else set()
        self.rdbms_DocumentRoot42 = rdbms_DocumentRoot42 if rdbms_DocumentRoot42 is not None else set()
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def rdbms_DocumentRoot23(self):
        return self.__rdbms_DocumentRoot23

    @rdbms_DocumentRoot23.setter
    def rdbms_DocumentRoot23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_DocumentRoot__rdbms_DocumentRoot23", None)
        self.__rdbms_DocumentRoot23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rdbms_key"):
                    opp_val = getattr(item, "rdbms_key", None)
                    
                    if opp_val == self:
                        setattr(item, "rdbms_key", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rdbms_key"):
                    opp_val = getattr(item, "rdbms_key", None)
                    
                    setattr(item, "rdbms_key", self)
                    

    @property
    def rdbms_DocumentRoot18(self):
        return self.__rdbms_DocumentRoot18

    @rdbms_DocumentRoot18.setter
    def rdbms_DocumentRoot18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_DocumentRoot__rdbms_DocumentRoot18", None)
        self.__rdbms_DocumentRoot18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rdbms_foreignKeys"):
                    opp_val = getattr(item, "rdbms_foreignKeys", None)
                    
                    if opp_val == self:
                        setattr(item, "rdbms_foreignKeys", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rdbms_foreignKeys"):
                    opp_val = getattr(item, "rdbms_foreignKeys", None)
                    
                    setattr(item, "rdbms_foreignKeys", self)
                    

    @property
    def rdbms_DocumentRoot16(self):
        return self.__rdbms_DocumentRoot16

    @rdbms_DocumentRoot16.setter
    def rdbms_DocumentRoot16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_DocumentRoot__rdbms_DocumentRoot16", None)
        self.__rdbms_DocumentRoot16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rdbms_foreignKey"):
                    opp_val = getattr(item, "rdbms_foreignKey", None)
                    
                    if opp_val == self:
                        setattr(item, "rdbms_foreignKey", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rdbms_foreignKey"):
                    opp_val = getattr(item, "rdbms_foreignKey", None)
                    
                    setattr(item, "rdbms_foreignKey", self)
                    

    @property
    def rdbms_DocumentRoot29(self):
        return self.__rdbms_DocumentRoot29

    @rdbms_DocumentRoot29.setter
    def rdbms_DocumentRoot29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_DocumentRoot__rdbms_DocumentRoot29", None)
        self.__rdbms_DocumentRoot29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rdbms_RDBMS"):
                    opp_val = getattr(item, "rdbms_RDBMS", None)
                    
                    if opp_val == self:
                        setattr(item, "rdbms_RDBMS", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rdbms_RDBMS"):
                    opp_val = getattr(item, "rdbms_RDBMS", None)
                    
                    setattr(item, "rdbms_RDBMS", self)
                    

    @property
    def rdbms_DocumentRoot25(self):
        return self.__rdbms_DocumentRoot25

    @rdbms_DocumentRoot25.setter
    def rdbms_DocumentRoot25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_DocumentRoot__rdbms_DocumentRoot25", None)
        self.__rdbms_DocumentRoot25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rdbms_key2"):
                    opp_val = getattr(item, "rdbms_key2", None)
                    
                    if opp_val == self:
                        setattr(item, "rdbms_key2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rdbms_key2"):
                    opp_val = getattr(item, "rdbms_key2", None)
                    
                    setattr(item, "rdbms_key2", self)
                    

    @property
    def rdbms_DocumentRoot10(self):
        return self.__rdbms_DocumentRoot10

    @rdbms_DocumentRoot10.setter
    def rdbms_DocumentRoot10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_DocumentRoot__rdbms_DocumentRoot10", None)
        self.__rdbms_DocumentRoot10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rdbms_column11"):
                    opp_val = getattr(item, "rdbms_column11", None)
                    
                    if opp_val == self:
                        setattr(item, "rdbms_column11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rdbms_column11"):
                    opp_val = getattr(item, "rdbms_column11", None)
                    
                    setattr(item, "rdbms_column11", self)
                    

    @property
    def rdbms_DocumentRoot(self):
        return self.__rdbms_DocumentRoot

    @rdbms_DocumentRoot.setter
    def rdbms_DocumentRoot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_DocumentRoot__rdbms_DocumentRoot", None)
        self.__rdbms_DocumentRoot = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rdbms_EStringToStringMapEntry"):
                    opp_val = getattr(item, "rdbms_EStringToStringMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "rdbms_EStringToStringMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rdbms_EStringToStringMapEntry"):
                    opp_val = getattr(item, "rdbms_EStringToStringMapEntry", None)
                    
                    setattr(item, "rdbms_EStringToStringMapEntry", self)
                    

    @property
    def rdbms_DocumentRoot40(self):
        return self.__rdbms_DocumentRoot40

    @rdbms_DocumentRoot40.setter
    def rdbms_DocumentRoot40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_DocumentRoot__rdbms_DocumentRoot40", None)
        self.__rdbms_DocumentRoot40 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rdbms_table"):
                    opp_val = getattr(item, "rdbms_table", None)
                    
                    if opp_val == self:
                        setattr(item, "rdbms_table", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rdbms_table"):
                    opp_val = getattr(item, "rdbms_table", None)
                    
                    setattr(item, "rdbms_table", self)
                    

    @property
    def rdbms_DocumentRoot42(self):
        return self.__rdbms_DocumentRoot42

    @rdbms_DocumentRoot42.setter
    def rdbms_DocumentRoot42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_DocumentRoot__rdbms_DocumentRoot42", None)
        self.__rdbms_DocumentRoot42 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rdbms_tables"):
                    opp_val = getattr(item, "rdbms_tables", None)
                    
                    if opp_val == self:
                        setattr(item, "rdbms_tables", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rdbms_tables"):
                    opp_val = getattr(item, "rdbms_tables", None)
                    
                    setattr(item, "rdbms_tables", self)
                    

    @property
    def rdbms_DocumentRoot7(self):
        return self.__rdbms_DocumentRoot7

    @rdbms_DocumentRoot7.setter
    def rdbms_DocumentRoot7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_DocumentRoot__rdbms_DocumentRoot7", None)
        self.__rdbms_DocumentRoot7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rdbms_EStringToStringMapEntry8"):
                    opp_val = getattr(item, "rdbms_EStringToStringMapEntry8", None)
                    
                    if opp_val == self:
                        setattr(item, "rdbms_EStringToStringMapEntry8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rdbms_EStringToStringMapEntry8"):
                    opp_val = getattr(item, "rdbms_EStringToStringMapEntry8", None)
                    
                    setattr(item, "rdbms_EStringToStringMapEntry8", self)
                    

    @property
    def rdbms_DocumentRoot38(self):
        return self.__rdbms_DocumentRoot38

    @rdbms_DocumentRoot38.setter
    def rdbms_DocumentRoot38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_DocumentRoot__rdbms_DocumentRoot38", None)
        self.__rdbms_DocumentRoot38 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rdbms_schemas"):
                    opp_val = getattr(item, "rdbms_schemas", None)
                    
                    if opp_val == self:
                        setattr(item, "rdbms_schemas", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rdbms_schemas"):
                    opp_val = getattr(item, "rdbms_schemas", None)
                    
                    setattr(item, "rdbms_schemas", self)
                    

    @property
    def rdbms_DocumentRoot20(self):
        return self.__rdbms_DocumentRoot20

    @rdbms_DocumentRoot20.setter
    def rdbms_DocumentRoot20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_DocumentRoot__rdbms_DocumentRoot20", None)
        self.__rdbms_DocumentRoot20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rdbms_hasForeignKeys21"):
                    opp_val = getattr(item, "rdbms_hasForeignKeys21", None)
                    
                    if opp_val == self:
                        setattr(item, "rdbms_hasForeignKeys21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rdbms_hasForeignKeys21"):
                    opp_val = getattr(item, "rdbms_hasForeignKeys21", None)
                    
                    setattr(item, "rdbms_hasForeignKeys21", self)
                    

    @property
    def rdbms_DocumentRoot36(self):
        return self.__rdbms_DocumentRoot36

    @rdbms_DocumentRoot36.setter
    def rdbms_DocumentRoot36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_DocumentRoot__rdbms_DocumentRoot36", None)
        self.__rdbms_DocumentRoot36 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rdbms_schema"):
                    opp_val = getattr(item, "rdbms_schema", None)
                    
                    if opp_val == self:
                        setattr(item, "rdbms_schema", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rdbms_schema"):
                    opp_val = getattr(item, "rdbms_schema", None)
                    
                    setattr(item, "rdbms_schema", self)
                    

    @property
    def rdbms_DocumentRoot31(self):
        return self.__rdbms_DocumentRoot31

    @rdbms_DocumentRoot31.setter
    def rdbms_DocumentRoot31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_DocumentRoot__rdbms_DocumentRoot31", None)
        self.__rdbms_DocumentRoot31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rdbms_referencedColumns"):
                    opp_val = getattr(item, "rdbms_referencedColumns", None)
                    
                    if opp_val == self:
                        setattr(item, "rdbms_referencedColumns", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rdbms_referencedColumns"):
                    opp_val = getattr(item, "rdbms_referencedColumns", None)
                    
                    setattr(item, "rdbms_referencedColumns", self)
                    

    @property
    def rdbms_DocumentRoot33(self):
        return self.__rdbms_DocumentRoot33

    @rdbms_DocumentRoot33.setter
    def rdbms_DocumentRoot33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_DocumentRoot__rdbms_DocumentRoot33", None)
        self.__rdbms_DocumentRoot33 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rdbms_referencedKeys34"):
                    opp_val = getattr(item, "rdbms_referencedKeys34", None)
                    
                    if opp_val == self:
                        setattr(item, "rdbms_referencedKeys34", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rdbms_referencedKeys34"):
                    opp_val = getattr(item, "rdbms_referencedKeys34", None)
                    
                    setattr(item, "rdbms_referencedKeys34", self)
                    

    @property
    def rdbms_DocumentRoot27(self):
        return self.__rdbms_DocumentRoot27

    @rdbms_DocumentRoot27.setter
    def rdbms_DocumentRoot27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_DocumentRoot__rdbms_DocumentRoot27", None)
        self.__rdbms_DocumentRoot27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rdbms_oID"):
                    opp_val = getattr(item, "rdbms_oID", None)
                    
                    if opp_val == self:
                        setattr(item, "rdbms_oID", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rdbms_oID"):
                    opp_val = getattr(item, "rdbms_oID", None)
                    
                    setattr(item, "rdbms_oID", self)
                    

    @property
    def rdbms_DocumentRoot13(self):
        return self.__rdbms_DocumentRoot13

    @rdbms_DocumentRoot13.setter
    def rdbms_DocumentRoot13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_DocumentRoot__rdbms_DocumentRoot13", None)
        self.__rdbms_DocumentRoot13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rdbms_columns14"):
                    opp_val = getattr(item, "rdbms_columns14", None)
                    
                    if opp_val == self:
                        setattr(item, "rdbms_columns14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rdbms_columns14"):
                    opp_val = getattr(item, "rdbms_columns14", None)
                    
                    setattr(item, "rdbms_columns14", self)
                    

class rdbms_hasForeignKeys:

    def __init__(self, group: str, rdbms_hasForeignKeys: "rdbms_column" = None, rdbms_hasForeignKeys21: "rdbms_DocumentRoot" = None, rdbms_hasForeignKeys50: set["rdbms_oID"] = None):
        self.group = group
        self.rdbms_hasForeignKeys = rdbms_hasForeignKeys
        self.rdbms_hasForeignKeys21 = rdbms_hasForeignKeys21
        self.rdbms_hasForeignKeys50 = rdbms_hasForeignKeys50 if rdbms_hasForeignKeys50 is not None else set()
        
    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def rdbms_hasForeignKeys21(self):
        return self.__rdbms_hasForeignKeys21

    @rdbms_hasForeignKeys21.setter
    def rdbms_hasForeignKeys21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_hasForeignKeys__rdbms_hasForeignKeys21", None)
        self.__rdbms_hasForeignKeys21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_DocumentRoot20"):
                opp_val = getattr(old_value, "rdbms_DocumentRoot20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_DocumentRoot20"):
                opp_val = getattr(value, "rdbms_DocumentRoot20", None)
                if opp_val is None:
                    setattr(value, "rdbms_DocumentRoot20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rdbms_hasForeignKeys(self):
        return self.__rdbms_hasForeignKeys

    @rdbms_hasForeignKeys.setter
    def rdbms_hasForeignKeys(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_hasForeignKeys__rdbms_hasForeignKeys", None)
        self.__rdbms_hasForeignKeys = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_column2"):
                opp_val = getattr(old_value, "rdbms_column2", None)
                if opp_val == self:
                    setattr(old_value, "rdbms_column2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_column2"):
                opp_val = getattr(value, "rdbms_column2", None)
                setattr(value, "rdbms_column2", self)

    @property
    def rdbms_hasForeignKeys50(self):
        return self.__rdbms_hasForeignKeys50

    @rdbms_hasForeignKeys50.setter
    def rdbms_hasForeignKeys50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_hasForeignKeys__rdbms_hasForeignKeys50", None)
        self.__rdbms_hasForeignKeys50 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rdbms_oID51"):
                    opp_val = getattr(item, "rdbms_oID51", None)
                    
                    if opp_val == self:
                        setattr(item, "rdbms_oID51", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rdbms_oID51"):
                    opp_val = getattr(item, "rdbms_oID51", None)
                    
                    setattr(item, "rdbms_oID51", self)
                    

class rdbms_referencedKeys:

    def __init__(self, group: str, rdbms_referencedKeys: "rdbms_column" = None, rdbms_referencedKeys34: "rdbms_DocumentRoot" = None, rdbms_referencedKeys65: set["rdbms_oID"] = None):
        self.group = group
        self.rdbms_referencedKeys = rdbms_referencedKeys
        self.rdbms_referencedKeys34 = rdbms_referencedKeys34
        self.rdbms_referencedKeys65 = rdbms_referencedKeys65 if rdbms_referencedKeys65 is not None else set()
        
    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def rdbms_referencedKeys34(self):
        return self.__rdbms_referencedKeys34

    @rdbms_referencedKeys34.setter
    def rdbms_referencedKeys34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_referencedKeys__rdbms_referencedKeys34", None)
        self.__rdbms_referencedKeys34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_DocumentRoot33"):
                opp_val = getattr(old_value, "rdbms_DocumentRoot33", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_DocumentRoot33"):
                opp_val = getattr(value, "rdbms_DocumentRoot33", None)
                if opp_val is None:
                    setattr(value, "rdbms_DocumentRoot33", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rdbms_referencedKeys(self):
        return self.__rdbms_referencedKeys

    @rdbms_referencedKeys.setter
    def rdbms_referencedKeys(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_referencedKeys__rdbms_referencedKeys", None)
        self.__rdbms_referencedKeys = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_column"):
                opp_val = getattr(old_value, "rdbms_column", None)
                if opp_val == self:
                    setattr(old_value, "rdbms_column", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_column"):
                opp_val = getattr(value, "rdbms_column", None)
                setattr(value, "rdbms_column", self)

    @property
    def rdbms_referencedKeys65(self):
        return self.__rdbms_referencedKeys65

    @rdbms_referencedKeys65.setter
    def rdbms_referencedKeys65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_referencedKeys__rdbms_referencedKeys65", None)
        self.__rdbms_referencedKeys65 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rdbms_oID66"):
                    opp_val = getattr(item, "rdbms_oID66", None)
                    
                    if opp_val == self:
                        setattr(item, "rdbms_oID66", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rdbms_oID66"):
                    opp_val = getattr(item, "rdbms_oID66", None)
                    
                    setattr(item, "rdbms_oID66", self)
                    

class rdbms_column:

    def __init__(self, kind: str, name: str, oID: str, type: str, rdbms_column2: "rdbms_hasForeignKeys" = None, rdbms_column: "rdbms_referencedKeys" = None, rdbms_column4: "rdbms_columns" = None, rdbms_column11: "rdbms_DocumentRoot" = None):
        self.kind = kind
        self.name = name
        self.oID = oID
        self.type = type
        self.rdbms_column2 = rdbms_column2
        self.rdbms_column = rdbms_column
        self.rdbms_column4 = rdbms_column4
        self.rdbms_column11 = rdbms_column11
        
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
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def oID(self) -> str:
        return self.__oID

    @oID.setter
    def oID(self, oID: str):
        self.__oID = oID

    @property
    def rdbms_column4(self):
        return self.__rdbms_column4

    @rdbms_column4.setter
    def rdbms_column4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_column__rdbms_column4", None)
        self.__rdbms_column4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_columns"):
                opp_val = getattr(old_value, "rdbms_columns", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_columns"):
                opp_val = getattr(value, "rdbms_columns", None)
                if opp_val is None:
                    setattr(value, "rdbms_columns", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rdbms_column11(self):
        return self.__rdbms_column11

    @rdbms_column11.setter
    def rdbms_column11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_column__rdbms_column11", None)
        self.__rdbms_column11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_DocumentRoot10"):
                opp_val = getattr(old_value, "rdbms_DocumentRoot10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_DocumentRoot10"):
                opp_val = getattr(value, "rdbms_DocumentRoot10", None)
                if opp_val is None:
                    setattr(value, "rdbms_DocumentRoot10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rdbms_column2(self):
        return self.__rdbms_column2

    @rdbms_column2.setter
    def rdbms_column2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_column__rdbms_column2", None)
        self.__rdbms_column2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_hasForeignKeys"):
                opp_val = getattr(old_value, "rdbms_hasForeignKeys", None)
                if opp_val == self:
                    setattr(old_value, "rdbms_hasForeignKeys", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_hasForeignKeys"):
                opp_val = getattr(value, "rdbms_hasForeignKeys", None)
                setattr(value, "rdbms_hasForeignKeys", self)

    @property
    def rdbms_column(self):
        return self.__rdbms_column

    @rdbms_column.setter
    def rdbms_column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_column__rdbms_column", None)
        self.__rdbms_column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_referencedKeys"):
                opp_val = getattr(old_value, "rdbms_referencedKeys", None)
                if opp_val == self:
                    setattr(old_value, "rdbms_referencedKeys", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_referencedKeys"):
                opp_val = getattr(value, "rdbms_referencedKeys", None)
                setattr(value, "rdbms_referencedKeys", self)
