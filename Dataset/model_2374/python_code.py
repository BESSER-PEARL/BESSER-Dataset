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
class rdb_NamedElement:

    pass
class rdb_Constraint:

    pass
class mm_rdb_TableConstraint(rdb_Constraint, rdb_NamedElement):

    pass
class ColumnConstraint:

    pass
class Column:

    pass
class mm_dml_ColumnReference(Column):

    pass
class mm_rdb_TableColumn(Column):

    def __init__(self, type: str, ownedColumns: "Table" = None, owningColumn: set["ColumnConstraint"] = None, Column: "mm_dml_ColumnReference" = None):
        self.type = type
        self.ownedColumns = ownedColumns
        self.owningColumn = owningColumn if owningColumn is not None else set()
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def owningColumn(self):
        return self.__owningColumn

    @owningColumn.setter
    def owningColumn(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_rdb_TableColumn__owningColumn", None)
        self.__owningColumn = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ColumnConstraint"):
                    opp_val = getattr(item, "ColumnConstraint", None)
                    
                    if opp_val == self:
                        setattr(item, "ColumnConstraint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ColumnConstraint"):
                    opp_val = getattr(item, "ColumnConstraint", None)
                    
                    setattr(item, "ColumnConstraint", self)
                    

    @property
    def ownedColumns(self):
        return self.__ownedColumns

    @ownedColumns.setter
    def ownedColumns(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_rdb_TableColumn__ownedColumns", None)
        self.__ownedColumns = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Table29"):
                opp_val = getattr(old_value, "Table29", None)
                if opp_val == self:
                    setattr(old_value, "Table29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Table29"):
                opp_val = getattr(value, "Table29", None)
                setattr(value, "Table29", self)

    def getOwningTable(self) :
        # TODO: Implement getOwningTable method
        pass

class Constraint:

    pass
class mm_rdb_ColumnConstraint(Constraint):

    pass
class Database:

    pass
class mm_rdb_ModelRoot:

    pass
class TableConstraint:

    pass
class mm_rdb_ForeignKey(TableConstraint):

    pass
class mm_rdb_UniqueIndex(TableConstraint):

    pass
class TableColumn:

    pass
class PrimaryKey:

    pass
class rdb_Relation:

    pass
class rdb_DbObject:

    pass
class mm_rdb_Table(rdb_DbObject, rdb_Relation):

    def __init__(self, tables: "Schema" = None, mm_rdb_Table: "PrimaryKey" = None, _owningTable: set["TableColumn"] = None, owningTable: set["TableConstraint"] = None):
        self.tables = tables
        self.mm_rdb_Table = mm_rdb_Table
        self._owningTable = _owningTable if _owningTable is not None else set()
        self.owningTable = owningTable if owningTable is not None else set()
        
        pass
    @property
    def owningTable(self):
        return self.__owningTable

    @owningTable.setter
    def owningTable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_rdb_Table__owningTable", None)
        self.__owningTable = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TableConstraint"):
                    opp_val = getattr(item, "TableConstraint", None)
                    
                    if opp_val == self:
                        setattr(item, "TableConstraint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TableConstraint"):
                    opp_val = getattr(item, "TableConstraint", None)
                    
                    setattr(item, "TableConstraint", self)
                    

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
    def _owningTable(self):
        return self.___owningTable

    @_owningTable.setter
    def _owningTable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_rdb_Table___owningTable", None)
        self.___owningTable = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TableColumn"):
                    opp_val = getattr(item, "TableColumn", None)
                    
                    if opp_val == self:
                        setattr(item, "TableColumn", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TableColumn"):
                    opp_val = getattr(item, "TableColumn", None)
                    
                    setattr(item, "TableColumn", self)
                    

    @property
    def tables(self):
        return self.__tables

    @tables.setter
    def tables(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_rdb_Table__tables", None)
        self.__tables = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Schema12"):
                opp_val = getattr(old_value, "Schema12", None)
                if opp_val == self:
                    setattr(old_value, "Schema12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Schema12"):
                opp_val = getattr(value, "Schema12", None)
                setattr(value, "Schema12", self)

    def getPrimaryColumn(self) :
        # TODO: Implement getPrimaryColumn method
        pass

    def getColumns(self) :
        # TODO: Implement getColumns method
        pass

class mm_rdb_Relation(ABC):

    def __init__(self):
        
        pass
    def getColumns(self) :
        # TODO: Implement getColumns method
        pass

class Index:

    pass
class Sequence:

    pass
class Table:

    pass
class DbObject:

    pass
class mm_rdb_Constraint(DbObject):

    pass
class mm_rdb_Sequence(DbObject):

    def __init__(self, cacheSize: int, sequences: "Schema" = None):
        self.cacheSize = cacheSize
        self.sequences = sequences
        
        pass
    @property
    def cacheSize(self):
        return self.__cacheSize

    @cacheSize.setter
    def cacheSize(self, cacheSize: int):
        self.__cacheSize = cacheSize


    @property
    def sequences(self):
        return self.__sequences

    @sequences.setter
    def sequences(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_rdb_Sequence__sequences", None)
        self.__sequences = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Schema17"):
                opp_val = getattr(old_value, "Schema17", None)
                if opp_val == self:
                    setattr(old_value, "Schema17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Schema17"):
                opp_val = getattr(value, "Schema17", None)
                setattr(value, "Schema17", self)

class mm_rdb_Index(DbObject):

    pass
class mm_rdb_Schema(DbObject):

    pass
class Schema:

    pass
class NamedElement:

    pass
class mm_rdb_DbObject(NamedElement):

    pass
class mm_rdb_Column(NamedElement):

    def __init__(self):
        
        pass
    def getOwningTable(self) :
        # TODO: Implement getOwningTable method
        pass

class mm_rdb_Database(NamedElement):

    pass
class mm_rdb_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class Operation:

    pass
class mm_rdb_RenameTable(Operation):

    def __init__(self, newName: str, mm_rdb_RenameTable: "Table" = None, Operation: "mm_rdb_ModelRoot" = None):
        self.newName = newName
        self.mm_rdb_RenameTable = mm_rdb_RenameTable
        
        pass
    @property
    def newName(self):
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
            if hasattr(old_value, "Table53"):
                opp_val = getattr(old_value, "Table53", None)
                if opp_val == self:
                    setattr(old_value, "Table53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Table53"):
                opp_val = getattr(value, "Table53", None)
                setattr(value, "Table53", self)

    def renameTable(self, mm_renamedTable, mm_newName) :
        # TODO: Implement renameTable method
        pass

class mm_rdb_CreateTable(Operation):

    def __init__(self, tableName: str, mm_rdb_CreateTable: set["TableColumn"] = None, mm_rdb_CreateTable44: set["TableConstraint"] = None, mm_rdb_CreateTable47: "PrimaryKey" = None, mm_rdb_CreateTable50: "Sequence" = None, Operation: "mm_rdb_ModelRoot" = None):
        self.tableName = tableName
        self.mm_rdb_CreateTable = mm_rdb_CreateTable if mm_rdb_CreateTable is not None else set()
        self.mm_rdb_CreateTable44 = mm_rdb_CreateTable44 if mm_rdb_CreateTable44 is not None else set()
        self.mm_rdb_CreateTable47 = mm_rdb_CreateTable47
        self.mm_rdb_CreateTable50 = mm_rdb_CreateTable50
        
        pass
    @property
    def tableName(self):
        return self.__tableName

    @tableName.setter
    def tableName(self, tableName: str):
        self.__tableName = tableName


    @property
    def mm_rdb_CreateTable47(self):
        return self.__mm_rdb_CreateTable47

    @mm_rdb_CreateTable47.setter
    def mm_rdb_CreateTable47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_rdb_CreateTable__mm_rdb_CreateTable47", None)
        self.__mm_rdb_CreateTable47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PrimaryKey48"):
                opp_val = getattr(old_value, "PrimaryKey48", None)
                if opp_val == self:
                    setattr(old_value, "PrimaryKey48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PrimaryKey48"):
                opp_val = getattr(value, "PrimaryKey48", None)
                setattr(value, "PrimaryKey48", self)

    @property
    def mm_rdb_CreateTable50(self):
        return self.__mm_rdb_CreateTable50

    @mm_rdb_CreateTable50.setter
    def mm_rdb_CreateTable50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_rdb_CreateTable__mm_rdb_CreateTable50", None)
        self.__mm_rdb_CreateTable50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Sequence51"):
                opp_val = getattr(old_value, "Sequence51", None)
                if opp_val == self:
                    setattr(old_value, "Sequence51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Sequence51"):
                opp_val = getattr(value, "Sequence51", None)
                setattr(value, "Sequence51", self)

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
                if hasattr(item, "TableColumn42"):
                    opp_val = getattr(item, "TableColumn42", None)
                    
                    if opp_val == self:
                        setattr(item, "TableColumn42", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TableColumn42"):
                    opp_val = getattr(item, "TableColumn42", None)
                    
                    setattr(item, "TableColumn42", self)
                    

    @property
    def mm_rdb_CreateTable44(self):
        return self.__mm_rdb_CreateTable44

    @mm_rdb_CreateTable44.setter
    def mm_rdb_CreateTable44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_rdb_CreateTable__mm_rdb_CreateTable44", None)
        self.__mm_rdb_CreateTable44 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TableConstraint45"):
                    opp_val = getattr(item, "TableConstraint45", None)
                    
                    if opp_val == self:
                        setattr(item, "TableConstraint45", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TableConstraint45"):
                    opp_val = getattr(item, "TableConstraint45", None)
                    
                    setattr(item, "TableConstraint45", self)
                    

    def createTable(self, mm_tableName, mm_generateID, mm_tableColumns, mm_primaryKey, mm_tableConstraints) :
        # TODO: Implement createTable method
        pass

class mm_rdb_AddColumn(Operation):

    def __init__(self, newColumnName: str, mm_rdb_AddColumn: "Table" = None, mm_rdb_AddColumn59: set["ColumnConstraint"] = None, Operation: "mm_rdb_ModelRoot" = None):
        self.newColumnName = newColumnName
        self.mm_rdb_AddColumn = mm_rdb_AddColumn
        self.mm_rdb_AddColumn59 = mm_rdb_AddColumn59 if mm_rdb_AddColumn59 is not None else set()
        
        pass
    @property
    def newColumnName(self):
        return self.__newColumnName

    @newColumnName.setter
    def newColumnName(self, newColumnName: str):
        self.__newColumnName = newColumnName


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
            if hasattr(old_value, "Table57"):
                opp_val = getattr(old_value, "Table57", None)
                if opp_val == self:
                    setattr(old_value, "Table57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Table57"):
                opp_val = getattr(value, "Table57", None)
                setattr(value, "Table57", self)

    @property
    def mm_rdb_AddColumn59(self):
        return self.__mm_rdb_AddColumn59

    @mm_rdb_AddColumn59.setter
    def mm_rdb_AddColumn59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_rdb_AddColumn__mm_rdb_AddColumn59", None)
        self.__mm_rdb_AddColumn59 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ColumnConstraint60"):
                    opp_val = getattr(item, "ColumnConstraint60", None)
                    
                    if opp_val == self:
                        setattr(item, "ColumnConstraint60", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ColumnConstraint60"):
                    opp_val = getattr(item, "ColumnConstraint60", None)
                    
                    setattr(item, "ColumnConstraint60", self)
                    

    def addColumn(self, mm_columnConstrains, mm_newColumnName, mm_changedTable) :
        # TODO: Implement addColumn method
        pass

class mm_rdb_TypeChangeToColumn(Operation):

    def __init__(self, newType: str, mm_rdb_TypeChangeToColumn: "Table" = None, mm_rdb_TypeChangeToColumn69: "TableColumn" = None, Operation: "mm_rdb_ModelRoot" = None):
        self.newType = newType
        self.mm_rdb_TypeChangeToColumn = mm_rdb_TypeChangeToColumn
        self.mm_rdb_TypeChangeToColumn69 = mm_rdb_TypeChangeToColumn69
        
        pass
    @property
    def newType(self):
        return self.__newType

    @newType.setter
    def newType(self, newType: str):
        self.__newType = newType


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
            if hasattr(old_value, "Table67"):
                opp_val = getattr(old_value, "Table67", None)
                if opp_val == self:
                    setattr(old_value, "Table67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Table67"):
                opp_val = getattr(value, "Table67", None)
                setattr(value, "Table67", self)

    @property
    def mm_rdb_TypeChangeToColumn69(self):
        return self.__mm_rdb_TypeChangeToColumn69

    @mm_rdb_TypeChangeToColumn69.setter
    def mm_rdb_TypeChangeToColumn69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_rdb_TypeChangeToColumn__mm_rdb_TypeChangeToColumn69", None)
        self.__mm_rdb_TypeChangeToColumn69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TableColumn70"):
                opp_val = getattr(old_value, "TableColumn70", None)
                if opp_val == self:
                    setattr(old_value, "TableColumn70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TableColumn70"):
                opp_val = getattr(value, "TableColumn70", None)
                setattr(value, "TableColumn70", self)

    def typeChangeToColumn(self, mm_changedTypeColumn, mm_newType, mm_changedTable) :
        # TODO: Implement typeChangeToColumn method
        pass

class mm_rdb_DeleteColumn(Operation):

    def __init__(self, mm_rdb_DeleteColumn: "Table" = None, mm_rdb_DeleteColumn74: "TableColumn" = None, Operation: "mm_rdb_ModelRoot" = None):
        self.mm_rdb_DeleteColumn = mm_rdb_DeleteColumn
        self.mm_rdb_DeleteColumn74 = mm_rdb_DeleteColumn74
        
        pass
    @property
    def mm_rdb_DeleteColumn74(self):
        return self.__mm_rdb_DeleteColumn74

    @mm_rdb_DeleteColumn74.setter
    def mm_rdb_DeleteColumn74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_rdb_DeleteColumn__mm_rdb_DeleteColumn74", None)
        self.__mm_rdb_DeleteColumn74 = value
        
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
    def mm_rdb_DeleteColumn(self):
        return self.__mm_rdb_DeleteColumn

    @mm_rdb_DeleteColumn.setter
    def mm_rdb_DeleteColumn(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_rdb_DeleteColumn__mm_rdb_DeleteColumn", None)
        self.__mm_rdb_DeleteColumn = value
        
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

    def deleteColumn(self, mm_deleteColumn, mm_changedTable) :
        # TODO: Implement deleteColumn method
        pass

class mm_rdb_RenameColumn(Operation):

    def __init__(self, newColumnName: str, mm_rdb_RenameColumn: "Table" = None, mm_rdb_RenameColumn64: "TableColumn" = None, Operation: "mm_rdb_ModelRoot" = None):
        self.newColumnName = newColumnName
        self.mm_rdb_RenameColumn = mm_rdb_RenameColumn
        self.mm_rdb_RenameColumn64 = mm_rdb_RenameColumn64
        
        pass
    @property
    def newColumnName(self):
        return self.__newColumnName

    @newColumnName.setter
    def newColumnName(self, newColumnName: str):
        self.__newColumnName = newColumnName


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
            if hasattr(old_value, "Table62"):
                opp_val = getattr(old_value, "Table62", None)
                if opp_val == self:
                    setattr(old_value, "Table62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Table62"):
                opp_val = getattr(value, "Table62", None)
                setattr(value, "Table62", self)

    @property
    def mm_rdb_RenameColumn64(self):
        return self.__mm_rdb_RenameColumn64

    @mm_rdb_RenameColumn64.setter
    def mm_rdb_RenameColumn64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_rdb_RenameColumn__mm_rdb_RenameColumn64", None)
        self.__mm_rdb_RenameColumn64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TableColumn65"):
                opp_val = getattr(old_value, "TableColumn65", None)
                if opp_val == self:
                    setattr(old_value, "TableColumn65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TableColumn65"):
                opp_val = getattr(value, "TableColumn65", None)
                setattr(value, "TableColumn65", self)

    def renameColumn(self, mm_newColumnName, mm_renamedColumn, mm_changedTable) :
        # TODO: Implement renameColumn method
        pass

class mm_rdb_DeleteTable(Operation):

    def __init__(self, mm_rdb_DeleteTable: "Table" = None, Operation: "mm_rdb_ModelRoot" = None):
        self.mm_rdb_DeleteTable = mm_rdb_DeleteTable
        
        pass
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
            if hasattr(old_value, "Table55"):
                opp_val = getattr(old_value, "Table55", None)
                if opp_val == self:
                    setattr(old_value, "Table55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Table55"):
                opp_val = getattr(value, "Table55", None)
                setattr(value, "Table55", self)

    def deleteTable(self, mm_deletedTable) :
        # TODO: Implement deleteTable method
        pass
