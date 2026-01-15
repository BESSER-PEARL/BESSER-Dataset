from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class dml_ColumnReference:

    pass
class Relation:

    pass
class mm_dml_Query(Relation):

    pass
class ModelRoot:

    pass
class mm_rdb_Operation(ABC):

    pass
class UniqueIndex:

    pass
class mm_rdb_PrimaryKey(UniqueIndex):

    pass
class ColumnConstraint:

    pass
class Column:

    pass
class mm_dml_ColumnReference(Column):

    pass
class mm_rdb_TableColumn(Column):

    def __init__(self, type: str, Table35: "Table" = None, ColumnConstraint: set["ColumnConstraint"] = None, Column: "mm_dml_ColumnReference"):
        self.type = type
        self.Table35 = Table35
        self.ColumnConstraint = ColumnConstraint if ColumnConstraint is not None else set()
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def Table35(self):
        return self.__Table35

    @Table35.setter
    def Table35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_rdb_TableColumn__Table35", None)
        self.__Table35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdb36"):
                opp_val = getattr(old_value, "rdb36", None)
                if opp_val == self:
                    setattr(old_value, "rdb36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdb36"):
                opp_val = getattr(value, "rdb36", None)
                setattr(value, "rdb36", self)

    @property
    def ColumnConstraint(self):
        return self.__ColumnConstraint

    @ColumnConstraint.setter
    def ColumnConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_rdb_TableColumn__ColumnConstraint", None)
        self.__ColumnConstraint = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rdb38"):
                    opp_val = getattr(item, "rdb38", None)
                    
                    if opp_val == self:
                        setattr(item, "rdb38", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rdb38"):
                    opp_val = getattr(item, "rdb38", None)
                    
                    setattr(item, "rdb38", self)
                    

    def getOwningTable(self) -> str:
        # TODO: Implement getOwningTable method
        pass

class Constraint:

    pass
class mm_rdb_ColumnConstraint(Constraint):

    pass
class TableConstraint:

    pass
class mm_rdb_ForeignKey(TableConstraint):

    pass
class mm_rdb_UniqueIndex(TableConstraint):

    pass
class TableColumn:

    pass
class rdb_NamedElement:

    pass
class rdb_Constraint:

    pass
class mm_rdb_TableConstraint(rdb_Constraint, rdb_NamedElement):

    pass
class rdb_Relation:

    pass
class rdb_DbObject:

    pass
class mm_rdb_Table(rdb_DbObject, rdb_Relation):

    def __init__(self, Schema13: "Schema" = None, mm_rdb_Table: "PrimaryKey" = None, TableColumn: set["TableColumn"] = None, TableConstraint: set["TableConstraint"] = None):
        self.Schema13 = Schema13
        self.mm_rdb_Table = mm_rdb_Table
        self.TableColumn = TableColumn if TableColumn is not None else set()
        self.TableConstraint = TableConstraint if TableConstraint is not None else set()
        
    @property
    def mm_rdb_Table(self):
        return self.__mm_rdb_Table

    @mm_rdb_Table.setter
    def mm_rdb_Table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_rdb_Table__mm_rdb_Table", None)
        self.__mm_rdb_Table = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PrimaryKey"):
                opp_val = getattr(old_value, "PrimaryKey", None)
                if opp_val == self:
                    setattr(old_value, "PrimaryKey", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PrimaryKey"):
                opp_val = getattr(value, "PrimaryKey", None)
                setattr(value, "PrimaryKey", self)

    @property
    def Schema13(self):
        return self.__Schema13

    @Schema13.setter
    def Schema13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_rdb_Table__Schema13", None)
        self.__Schema13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdb14"):
                opp_val = getattr(old_value, "rdb14", None)
                if opp_val == self:
                    setattr(old_value, "rdb14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdb14"):
                opp_val = getattr(value, "rdb14", None)
                setattr(value, "rdb14", self)

    @property
    def TableColumn(self):
        return self.__TableColumn

    @TableColumn.setter
    def TableColumn(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_rdb_Table__TableColumn", None)
        self.__TableColumn = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rdb17"):
                    opp_val = getattr(item, "rdb17", None)
                    
                    if opp_val == self:
                        setattr(item, "rdb17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rdb17"):
                    opp_val = getattr(item, "rdb17", None)
                    
                    setattr(item, "rdb17", self)
                    

    @property
    def TableConstraint(self):
        return self.__TableConstraint

    @TableConstraint.setter
    def TableConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_rdb_Table__TableConstraint", None)
        self.__TableConstraint = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rdb19"):
                    opp_val = getattr(item, "rdb19", None)
                    
                    if opp_val == self:
                        setattr(item, "rdb19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rdb19"):
                    opp_val = getattr(item, "rdb19", None)
                    
                    setattr(item, "rdb19", self)
                    

    def getPrimaryColumn(self) -> str:
        # TODO: Implement getPrimaryColumn method
        pass

    def getColumns(self) -> str:
        # TODO: Implement getColumns method
        pass

class mm_rdb_Relation(ABC):

    def __init__(self):
        
    def getColumns(self) -> str:
        # TODO: Implement getColumns method
        pass

class PrimaryKey:

    pass
class Table:

    pass
class DbObject:

    pass
class mm_rdb_Constraint(DbObject):

    pass
class mm_rdb_Sequence(DbObject):

    def __init__(self, cacheSize: int, Schema21: "Schema" = None):
        self.cacheSize = cacheSize
        self.Schema21 = Schema21
        
    @property
    def cacheSize(self) -> int:
        return self.__cacheSize

    @cacheSize.setter
    def cacheSize(self, cacheSize: int):
        self.__cacheSize = cacheSize

    @property
    def Schema21(self):
        return self.__Schema21

    @Schema21.setter
    def Schema21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_rdb_Sequence__Schema21", None)
        self.__Schema21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdb22"):
                opp_val = getattr(old_value, "rdb22", None)
                if opp_val == self:
                    setattr(old_value, "rdb22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdb22"):
                opp_val = getattr(value, "rdb22", None)
                setattr(value, "rdb22", self)

class mm_rdb_Index(DbObject):

    pass
class mm_rdb_Schema(DbObject):

    pass
class Schema:

    pass
class Index:

    pass
class Sequence:

    pass
class NamedElement:

    pass
class mm_rdb_Column(NamedElement):

    def __init__(self):
        
    def getOwningTable(self) -> str:
        # TODO: Implement getOwningTable method
        pass

class mm_rdb_DbObject(NamedElement):

    pass
class mm_rdb_Database(NamedElement):

    pass
class mm_rdb_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class Operation:

    pass
class mm_rdb_RenameTable(Operation):

    def __init__(self, newName: str, mm_rdb_RenameTable: "Table" = None, rdb: "mm_rdb_ModelRoot"):
        self.newName = newName
        self.mm_rdb_RenameTable = mm_rdb_RenameTable
        
    @property
    def newName(self) -> str:
        return self.__newName

    @newName.setter
    def newName(self, newName: str):
        self.__newName = newName

    @property
    def mm_rdb_RenameTable(self):
        return self.__mm_rdb_RenameTable

    @mm_rdb_RenameTable.setter
    def mm_rdb_RenameTable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_rdb_RenameTable__mm_rdb_RenameTable", None)
        self.__mm_rdb_RenameTable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Table63"):
                opp_val = getattr(old_value, "Table63", None)
                if opp_val == self:
                    setattr(old_value, "Table63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Table63"):
                opp_val = getattr(value, "Table63", None)
                setattr(value, "Table63", self)

    def renameTable(self, renamedTable: str, newName: str) -> bool:
        # TODO: Implement renameTable method
        pass

class mm_rdb_RenameColumn(Operation):

    def __init__(self, newColumnName: str, mm_rdb_RenameColumn: "Table" = None, mm_rdb_RenameColumn74: "TableColumn" = None, rdb: "mm_rdb_ModelRoot"):
        self.newColumnName = newColumnName
        self.mm_rdb_RenameColumn = mm_rdb_RenameColumn
        self.mm_rdb_RenameColumn74 = mm_rdb_RenameColumn74
        
    @property
    def newColumnName(self) -> str:
        return self.__newColumnName

    @newColumnName.setter
    def newColumnName(self, newColumnName: str):
        self.__newColumnName = newColumnName

    @property
    def mm_rdb_RenameColumn74(self):
        return self.__mm_rdb_RenameColumn74

    @mm_rdb_RenameColumn74.setter
    def mm_rdb_RenameColumn74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_rdb_RenameColumn__mm_rdb_RenameColumn74", None)
        self.__mm_rdb_RenameColumn74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TableColumn75"):
                opp_val = getattr(old_value, "TableColumn75", None)
                if opp_val == self:
                    setattr(old_value, "TableColumn75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TableColumn75"):
                opp_val = getattr(value, "TableColumn75", None)
                setattr(value, "TableColumn75", self)

    @property
    def mm_rdb_RenameColumn(self):
        return self.__mm_rdb_RenameColumn

    @mm_rdb_RenameColumn.setter
    def mm_rdb_RenameColumn(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_rdb_RenameColumn__mm_rdb_RenameColumn", None)
        self.__mm_rdb_RenameColumn = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Table72"):
                opp_val = getattr(old_value, "Table72", None)
                if opp_val == self:
                    setattr(old_value, "Table72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Table72"):
                opp_val = getattr(value, "Table72", None)
                setattr(value, "Table72", self)

    def renameColumn(self, changedTable: str, renamedColumn: str, newColumnName: str) -> bool:
        # TODO: Implement renameColumn method
        pass

class mm_rdb_DeleteTable(Operation):

    def __init__(self, mm_rdb_DeleteTable: "Table" = None, rdb: "mm_rdb_ModelRoot"):
        self.mm_rdb_DeleteTable = mm_rdb_DeleteTable
        
    @property
    def mm_rdb_DeleteTable(self):
        return self.__mm_rdb_DeleteTable

    @mm_rdb_DeleteTable.setter
    def mm_rdb_DeleteTable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_rdb_DeleteTable__mm_rdb_DeleteTable", None)
        self.__mm_rdb_DeleteTable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Table65"):
                opp_val = getattr(old_value, "Table65", None)
                if opp_val == self:
                    setattr(old_value, "Table65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Table65"):
                opp_val = getattr(value, "Table65", None)
                setattr(value, "Table65", self)

    def deleteTable(self, deletedTable: str) -> bool:
        # TODO: Implement deleteTable method
        pass

class mm_rdb_DeleteColumn(Operation):

    def __init__(self, mm_rdb_DeleteColumn: "Table" = None, mm_rdb_DeleteColumn84: "TableColumn" = None, rdb: "mm_rdb_ModelRoot"):
        self.mm_rdb_DeleteColumn = mm_rdb_DeleteColumn
        self.mm_rdb_DeleteColumn84 = mm_rdb_DeleteColumn84
        
    @property
    def mm_rdb_DeleteColumn(self):
        return self.__mm_rdb_DeleteColumn

    @mm_rdb_DeleteColumn.setter
    def mm_rdb_DeleteColumn(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_rdb_DeleteColumn__mm_rdb_DeleteColumn", None)
        self.__mm_rdb_DeleteColumn = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Table82"):
                opp_val = getattr(old_value, "Table82", None)
                if opp_val == self:
                    setattr(old_value, "Table82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Table82"):
                opp_val = getattr(value, "Table82", None)
                setattr(value, "Table82", self)

    @property
    def mm_rdb_DeleteColumn84(self):
        return self.__mm_rdb_DeleteColumn84

    @mm_rdb_DeleteColumn84.setter
    def mm_rdb_DeleteColumn84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_rdb_DeleteColumn__mm_rdb_DeleteColumn84", None)
        self.__mm_rdb_DeleteColumn84 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TableColumn85"):
                opp_val = getattr(old_value, "TableColumn85", None)
                if opp_val == self:
                    setattr(old_value, "TableColumn85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TableColumn85"):
                opp_val = getattr(value, "TableColumn85", None)
                setattr(value, "TableColumn85", self)

    def deleteColumn(self, deleteColumn: str, changedTable: str) -> bool:
        # TODO: Implement deleteColumn method
        pass

class mm_rdb_AddColumn(Operation):

    def __init__(self, newColumnName: str, mm_rdb_AddColumn69: set["ColumnConstraint"] = None, mm_rdb_AddColumn: "Table" = None, rdb: "mm_rdb_ModelRoot"):
        self.newColumnName = newColumnName
        self.mm_rdb_AddColumn69 = mm_rdb_AddColumn69 if mm_rdb_AddColumn69 is not None else set()
        self.mm_rdb_AddColumn = mm_rdb_AddColumn
        
    @property
    def newColumnName(self) -> str:
        return self.__newColumnName

    @newColumnName.setter
    def newColumnName(self, newColumnName: str):
        self.__newColumnName = newColumnName

    @property
    def mm_rdb_AddColumn69(self):
        return self.__mm_rdb_AddColumn69

    @mm_rdb_AddColumn69.setter
    def mm_rdb_AddColumn69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_rdb_AddColumn__mm_rdb_AddColumn69", None)
        self.__mm_rdb_AddColumn69 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ColumnConstraint70"):
                    opp_val = getattr(item, "ColumnConstraint70", None)
                    
                    if opp_val == self:
                        setattr(item, "ColumnConstraint70", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ColumnConstraint70"):
                    opp_val = getattr(item, "ColumnConstraint70", None)
                    
                    setattr(item, "ColumnConstraint70", self)
                    

    @property
    def mm_rdb_AddColumn(self):
        return self.__mm_rdb_AddColumn

    @mm_rdb_AddColumn.setter
    def mm_rdb_AddColumn(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_rdb_AddColumn__mm_rdb_AddColumn", None)
        self.__mm_rdb_AddColumn = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Table67"):
                opp_val = getattr(old_value, "Table67", None)
                if opp_val == self:
                    setattr(old_value, "Table67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Table67"):
                opp_val = getattr(value, "Table67", None)
                setattr(value, "Table67", self)

    def addColumn(self, newColumnName: str, columnConstrains: str, changedTable: str) -> bool:
        # TODO: Implement addColumn method
        pass

class mm_rdb_CreateTable(Operation):

    def __init__(self, tableName: str, mm_rdb_CreateTable: set["TableColumn"] = None, mm_rdb_CreateTable54: set["TableConstraint"] = None, mm_rdb_CreateTable57: "PrimaryKey" = None, mm_rdb_CreateTable60: "Sequence" = None, rdb: "mm_rdb_ModelRoot"):
        self.tableName = tableName
        self.mm_rdb_CreateTable = mm_rdb_CreateTable if mm_rdb_CreateTable is not None else set()
        self.mm_rdb_CreateTable54 = mm_rdb_CreateTable54 if mm_rdb_CreateTable54 is not None else set()
        self.mm_rdb_CreateTable57 = mm_rdb_CreateTable57
        self.mm_rdb_CreateTable60 = mm_rdb_CreateTable60
        
    @property
    def tableName(self) -> str:
        return self.__tableName

    @tableName.setter
    def tableName(self, tableName: str):
        self.__tableName = tableName

    @property
    def mm_rdb_CreateTable(self):
        return self.__mm_rdb_CreateTable

    @mm_rdb_CreateTable.setter
    def mm_rdb_CreateTable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_rdb_CreateTable__mm_rdb_CreateTable", None)
        self.__mm_rdb_CreateTable = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TableColumn52"):
                    opp_val = getattr(item, "TableColumn52", None)
                    
                    if opp_val == self:
                        setattr(item, "TableColumn52", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TableColumn52"):
                    opp_val = getattr(item, "TableColumn52", None)
                    
                    setattr(item, "TableColumn52", self)
                    

    @property
    def mm_rdb_CreateTable54(self):
        return self.__mm_rdb_CreateTable54

    @mm_rdb_CreateTable54.setter
    def mm_rdb_CreateTable54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_rdb_CreateTable__mm_rdb_CreateTable54", None)
        self.__mm_rdb_CreateTable54 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TableConstraint55"):
                    opp_val = getattr(item, "TableConstraint55", None)
                    
                    if opp_val == self:
                        setattr(item, "TableConstraint55", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TableConstraint55"):
                    opp_val = getattr(item, "TableConstraint55", None)
                    
                    setattr(item, "TableConstraint55", self)
                    

    @property
    def mm_rdb_CreateTable60(self):
        return self.__mm_rdb_CreateTable60

    @mm_rdb_CreateTable60.setter
    def mm_rdb_CreateTable60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_rdb_CreateTable__mm_rdb_CreateTable60", None)
        self.__mm_rdb_CreateTable60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Sequence61"):
                opp_val = getattr(old_value, "Sequence61", None)
                if opp_val == self:
                    setattr(old_value, "Sequence61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Sequence61"):
                opp_val = getattr(value, "Sequence61", None)
                setattr(value, "Sequence61", self)

    @property
    def mm_rdb_CreateTable57(self):
        return self.__mm_rdb_CreateTable57

    @mm_rdb_CreateTable57.setter
    def mm_rdb_CreateTable57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_rdb_CreateTable__mm_rdb_CreateTable57", None)
        self.__mm_rdb_CreateTable57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PrimaryKey58"):
                opp_val = getattr(old_value, "PrimaryKey58", None)
                if opp_val == self:
                    setattr(old_value, "PrimaryKey58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PrimaryKey58"):
                opp_val = getattr(value, "PrimaryKey58", None)
                setattr(value, "PrimaryKey58", self)

    def createTable(self, tableName: str, generateID: str, tableConstraints: str, tableColumns: str, primaryKey: str) -> bool:
        # TODO: Implement createTable method
        pass

class mm_rdb_TypeChangeToColumn(Operation):

    def __init__(self, newType: str, mm_rdb_TypeChangeToColumn: "Table" = None, mm_rdb_TypeChangeToColumn79: "TableColumn" = None, rdb: "mm_rdb_ModelRoot"):
        self.newType = newType
        self.mm_rdb_TypeChangeToColumn = mm_rdb_TypeChangeToColumn
        self.mm_rdb_TypeChangeToColumn79 = mm_rdb_TypeChangeToColumn79
        
    @property
    def newType(self) -> str:
        return self.__newType

    @newType.setter
    def newType(self, newType: str):
        self.__newType = newType

    @property
    def mm_rdb_TypeChangeToColumn79(self):
        return self.__mm_rdb_TypeChangeToColumn79

    @mm_rdb_TypeChangeToColumn79.setter
    def mm_rdb_TypeChangeToColumn79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_rdb_TypeChangeToColumn__mm_rdb_TypeChangeToColumn79", None)
        self.__mm_rdb_TypeChangeToColumn79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TableColumn80"):
                opp_val = getattr(old_value, "TableColumn80", None)
                if opp_val == self:
                    setattr(old_value, "TableColumn80", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TableColumn80"):
                opp_val = getattr(value, "TableColumn80", None)
                setattr(value, "TableColumn80", self)

    @property
    def mm_rdb_TypeChangeToColumn(self):
        return self.__mm_rdb_TypeChangeToColumn

    @mm_rdb_TypeChangeToColumn.setter
    def mm_rdb_TypeChangeToColumn(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_rdb_TypeChangeToColumn__mm_rdb_TypeChangeToColumn", None)
        self.__mm_rdb_TypeChangeToColumn = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Table77"):
                opp_val = getattr(old_value, "Table77", None)
                if opp_val == self:
                    setattr(old_value, "Table77", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Table77"):
                opp_val = getattr(value, "Table77", None)
                setattr(value, "Table77", self)

    def typeChangeToColumn(self, changedTable: str, newType: str, changedTypeColumn: str) -> bool:
        # TODO: Implement typeChangeToColumn method
        pass

class Database:

    pass
class mm_rdb_ModelRoot:

    pass