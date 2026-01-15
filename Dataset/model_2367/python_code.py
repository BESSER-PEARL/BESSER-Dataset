from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Type(Enum):
    NUMERIC = "NUMERIC"
    VARCHAR = "VARCHAR"
    DATE = "DATE"
    TIME = "TIME"
    FLOAT = "FLOAT"
    CHAR = "CHAR"


############################################
# Definition of Classes
############################################

class relational_obeo_ModelElement(ABC):

    def __init__(self, comment: str):
        self.comment = comment
        
    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

class ModelElement:

    pass
class relational_obeo_ForeignKey(ModelElement):

    def __init__(self, name: str, ForeignKey: "relational_obeo_Table" = None, ownedForeignKeys: "relational_obeo_Table" = None, relational_obeo_ForeignKey: "relational_obeo_Table" = None):
        self.name = name
        self.ForeignKey = ForeignKey
        self.ownedForeignKeys = ownedForeignKeys
        self.relational_obeo_ForeignKey = relational_obeo_ForeignKey
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def relational_obeo_ForeignKey(self):
        return self.__relational_obeo_ForeignKey

    @relational_obeo_ForeignKey.setter
    def relational_obeo_ForeignKey(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_obeo_ForeignKey__relational_obeo_ForeignKey", None)
        self.__relational_obeo_ForeignKey = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "relational_obeo_Table"):
                opp_val = getattr(old_value, "relational_obeo_Table", None)
                if opp_val == self:
                    setattr(old_value, "relational_obeo_Table", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "relational_obeo_Table"):
                opp_val = getattr(value, "relational_obeo_Table", None)
                setattr(value, "relational_obeo_Table", self)

    @property
    def ownedForeignKeys(self):
        return self.__ownedForeignKeys

    @ownedForeignKeys.setter
    def ownedForeignKeys(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_obeo_ForeignKey__ownedForeignKeys", None)
        self.__ownedForeignKeys = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Table10"):
                opp_val = getattr(old_value, "Table10", None)
                if opp_val == self:
                    setattr(old_value, "Table10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Table10"):
                opp_val = getattr(value, "Table10", None)
                setattr(value, "Table10", self)

    @property
    def ForeignKey(self):
        return self.__ForeignKey

    @ForeignKey.setter
    def ForeignKey(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_obeo_ForeignKey__ForeignKey", None)
        self.__ForeignKey = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "foreignTable"):
                opp_val = getattr(old_value, "foreignTable", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "foreignTable"):
                opp_val = getattr(value, "foreignTable", None)
                if opp_val is None:
                    setattr(value, "foreignTable", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class relational_obeo_Column(ModelElement):

    def __init__(self, name: str, type: str, isPrimaryKey: bool, isUnique: bool, Column: "relational_obeo_Table" = None, ownedColumns: "relational_obeo_Table" = None):
        self.name = name
        self.type = type
        self.isPrimaryKey = isPrimaryKey
        self.isUnique = isUnique
        self.Column = Column
        self.ownedColumns = ownedColumns
        
    @property
    def isUnique(self) -> bool:
        return self.__isUnique

    @isUnique.setter
    def isUnique(self, isUnique: bool):
        self.__isUnique = isUnique

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def isPrimaryKey(self) -> bool:
        return self.__isPrimaryKey

    @isPrimaryKey.setter
    def isPrimaryKey(self, isPrimaryKey: bool):
        self.__isPrimaryKey = isPrimaryKey

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ownedColumns(self):
        return self.__ownedColumns

    @ownedColumns.setter
    def ownedColumns(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_obeo_Column__ownedColumns", None)
        self.__ownedColumns = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Table13"):
                opp_val = getattr(old_value, "Table13", None)
                if opp_val == self:
                    setattr(old_value, "Table13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Table13"):
                opp_val = getattr(value, "Table13", None)
                setattr(value, "Table13", self)

    @property
    def Column(self):
        return self.__Column

    @Column.setter
    def Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_obeo_Column__Column", None)
        self.__Column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owner5"):
                opp_val = getattr(old_value, "owner5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner5"):
                opp_val = getattr(value, "owner5", None)
                if opp_val is None:
                    setattr(value, "owner5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class relational_obeo_Table(ModelElement):

    def __init__(self, name: str, Table: "relational_obeo_Schema" = None, owner5: set["relational_obeo_Column"] = None, foreignTable: set["relational_obeo_ForeignKey"] = None, Table10: "relational_obeo_ForeignKey" = None, relational_obeo_Table: "relational_obeo_ForeignKey" = None, Table13: "relational_obeo_Column" = None, ownedTables: "relational_obeo_Schema" = None):
        self.name = name
        self.Table = Table
        self.owner5 = owner5 if owner5 is not None else set()
        self.foreignTable = foreignTable if foreignTable is not None else set()
        self.Table10 = Table10
        self.relational_obeo_Table = relational_obeo_Table
        self.Table13 = Table13
        self.ownedTables = ownedTables
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def relational_obeo_Table(self):
        return self.__relational_obeo_Table

    @relational_obeo_Table.setter
    def relational_obeo_Table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_obeo_Table__relational_obeo_Table", None)
        self.__relational_obeo_Table = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "relational_obeo_ForeignKey"):
                opp_val = getattr(old_value, "relational_obeo_ForeignKey", None)
                if opp_val == self:
                    setattr(old_value, "relational_obeo_ForeignKey", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "relational_obeo_ForeignKey"):
                opp_val = getattr(value, "relational_obeo_ForeignKey", None)
                setattr(value, "relational_obeo_ForeignKey", self)

    @property
    def owner5(self):
        return self.__owner5

    @owner5.setter
    def owner5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_obeo_Table__owner5", None)
        self.__owner5 = value if value is not None else set()
        
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
    def foreignTable(self):
        return self.__foreignTable

    @foreignTable.setter
    def foreignTable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_obeo_Table__foreignTable", None)
        self.__foreignTable = value if value is not None else set()
        
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
    def ownedTables(self):
        return self.__ownedTables

    @ownedTables.setter
    def ownedTables(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_obeo_Table__ownedTables", None)
        self.__ownedTables = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Schema8"):
                opp_val = getattr(old_value, "Schema8", None)
                if opp_val == self:
                    setattr(old_value, "Schema8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Schema8"):
                opp_val = getattr(value, "Schema8", None)
                setattr(value, "Schema8", self)

    @property
    def Table10(self):
        return self.__Table10

    @Table10.setter
    def Table10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_obeo_Table__Table10", None)
        self.__Table10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedForeignKeys"):
                opp_val = getattr(old_value, "ownedForeignKeys", None)
                if opp_val == self:
                    setattr(old_value, "ownedForeignKeys", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedForeignKeys"):
                opp_val = getattr(value, "ownedForeignKeys", None)
                setattr(value, "ownedForeignKeys", self)

    @property
    def Table(self):
        return self.__Table

    @Table.setter
    def Table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_obeo_Table__Table", None)
        self.__Table = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owner2"):
                opp_val = getattr(old_value, "owner2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner2"):
                opp_val = getattr(value, "owner2", None)
                if opp_val is None:
                    setattr(value, "owner2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Table13(self):
        return self.__Table13

    @Table13.setter
    def Table13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_obeo_Table__Table13", None)
        self.__Table13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedColumns"):
                opp_val = getattr(old_value, "ownedColumns", None)
                if opp_val == self:
                    setattr(old_value, "ownedColumns", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedColumns"):
                opp_val = getattr(value, "ownedColumns", None)
                setattr(value, "ownedColumns", self)

class relational_obeo_Schema(ModelElement):

    def __init__(self, name: str, Schema: "relational_obeo_Database" = None, owner2: set["relational_obeo_Table"] = None, ownedSchemas: "relational_obeo_Database" = None, Schema8: "relational_obeo_Table" = None):
        self.name = name
        self.Schema = Schema
        self.owner2 = owner2 if owner2 is not None else set()
        self.ownedSchemas = ownedSchemas
        self.Schema8 = Schema8
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Schema(self):
        return self.__Schema

    @Schema.setter
    def Schema(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_obeo_Schema__Schema", None)
        self.__Schema = value
        
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
    def Schema8(self):
        return self.__Schema8

    @Schema8.setter
    def Schema8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_obeo_Schema__Schema8", None)
        self.__Schema8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedTables"):
                opp_val = getattr(old_value, "ownedTables", None)
                if opp_val == self:
                    setattr(old_value, "ownedTables", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedTables"):
                opp_val = getattr(value, "ownedTables", None)
                setattr(value, "ownedTables", self)

    @property
    def owner2(self):
        return self.__owner2

    @owner2.setter
    def owner2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_obeo_Schema__owner2", None)
        self.__owner2 = value if value is not None else set()
        
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
    def ownedSchemas(self):
        return self.__ownedSchemas

    @ownedSchemas.setter
    def ownedSchemas(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_obeo_Schema__ownedSchemas", None)
        self.__ownedSchemas = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Database"):
                opp_val = getattr(old_value, "Database", None)
                if opp_val == self:
                    setattr(old_value, "Database", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Database"):
                opp_val = getattr(value, "Database", None)
                setattr(value, "Database", self)

class relational_obeo_Database(ModelElement):

    def __init__(self, url: str, name: str, owner: set["relational_obeo_Schema"] = None, Database: "relational_obeo_Schema" = None):
        self.url = url
        self.name = name
        self.owner = owner if owner is not None else set()
        self.Database = Database
        
    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Database(self):
        return self.__Database

    @Database.setter
    def Database(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_obeo_Database__Database", None)
        self.__Database = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedSchemas"):
                opp_val = getattr(old_value, "ownedSchemas", None)
                if opp_val == self:
                    setattr(old_value, "ownedSchemas", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedSchemas"):
                opp_val = getattr(value, "ownedSchemas", None)
                setattr(value, "ownedSchemas", self)

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_obeo_Database__owner", None)
        self.__owner = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Schema"):
                    opp_val = getattr(item, "Schema", None)
                    
                    if opp_val == self:
                        setattr(item, "Schema", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Schema"):
                    opp_val = getattr(item, "Schema", None)
                    
                    setattr(item, "Schema", self)
                    
