from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class PrimitiveType(Enum):
    boolean = "boolean"
    char = "char"
    int = "int"
    float = "float"


############################################
# Definition of Classes
############################################

class mm_rdb_Column:

    def __init__(self, isNillable: str, name: str, type: str, defaultValue: str, Table27: "Table" = None):
        self.isNillable = isNillable
        self.name = name
        self.type = type
        self.defaultValue = defaultValue
        self.Table27 = Table27
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def defaultValue(self) -> str:
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: str):
        self.__defaultValue = defaultValue

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def isNillable(self) -> str:
        return self.__isNillable

    @isNillable.setter
    def isNillable(self, isNillable: str):
        self.__isNillable = isNillable

    @property
    def Table27(self):
        return self.__Table27

    @Table27.setter
    def Table27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_rdb_Column__Table27", None)
        self.__Table27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdb28"):
                opp_val = getattr(old_value, "rdb28", None)
                if opp_val == self:
                    setattr(old_value, "rdb28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdb28"):
                opp_val = getattr(value, "rdb28", None)
                setattr(value, "rdb28", self)

class TableConstraint:

    pass
class mm_rdb_Table:

    def __init__(self, name: str, Schema19: "Schema" = None, Column22: set["Column"] = None, TableConstraint: set["TableConstraint"] = None):
        self.name = name
        self.Schema19 = Schema19
        self.Column22 = Column22 if Column22 is not None else set()
        self.TableConstraint = TableConstraint if TableConstraint is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Column22(self):
        return self.__Column22

    @Column22.setter
    def Column22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_rdb_Table__Column22", None)
        self.__Column22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rdb23"):
                    opp_val = getattr(item, "rdb23", None)
                    
                    if opp_val == self:
                        setattr(item, "rdb23", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rdb23"):
                    opp_val = getattr(item, "rdb23", None)
                    
                    setattr(item, "rdb23", self)
                    

    @property
    def Schema19(self):
        return self.__Schema19

    @Schema19.setter
    def Schema19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_rdb_Table__Schema19", None)
        self.__Schema19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdb20"):
                opp_val = getattr(old_value, "rdb20", None)
                if opp_val == self:
                    setattr(old_value, "rdb20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdb20"):
                opp_val = getattr(value, "rdb20", None)
                setattr(value, "rdb20", self)

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
                if hasattr(item, "rdb25"):
                    opp_val = getattr(item, "rdb25", None)
                    
                    if opp_val == self:
                        setattr(item, "rdb25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rdb25"):
                    opp_val = getattr(item, "rdb25", None)
                    
                    setattr(item, "rdb25", self)
                    

class Column:

    pass
class ModelOperation:

    pass
class mm_ops_AddNotNull(ModelOperation):

    def __init__(self, owningSchemaName: str, owningTableName: str, constrainedColumnName: str):
        self.owningSchemaName = owningSchemaName
        self.owningTableName = owningTableName
        self.constrainedColumnName = constrainedColumnName
        
    @property
    def owningTableName(self) -> str:
        return self.__owningTableName

    @owningTableName.setter
    def owningTableName(self, owningTableName: str):
        self.__owningTableName = owningTableName

    @property
    def owningSchemaName(self) -> str:
        return self.__owningSchemaName

    @owningSchemaName.setter
    def owningSchemaName(self, owningSchemaName: str):
        self.__owningSchemaName = owningSchemaName

    @property
    def constrainedColumnName(self) -> str:
        return self.__constrainedColumnName

    @constrainedColumnName.setter
    def constrainedColumnName(self, constrainedColumnName: str):
        self.__constrainedColumnName = constrainedColumnName

class mm_ops_HasNoInstances(ModelOperation):

    def __init__(self, owningSchemaName: str, tableName: str):
        self.owningSchemaName = owningSchemaName
        self.tableName = tableName
        
    @property
    def tableName(self) -> str:
        return self.__tableName

    @tableName.setter
    def tableName(self, tableName: str):
        self.__tableName = tableName

    @property
    def owningSchemaName(self) -> str:
        return self.__owningSchemaName

    @owningSchemaName.setter
    def owningSchemaName(self, owningSchemaName: str):
        self.__owningSchemaName = owningSchemaName

class mm_ops_SetColumnType(ModelOperation):

    def __init__(self, owningSchemaName: str, owningTableName: str, owningColumnName: str, newType: str, oldType: str):
        self.owningSchemaName = owningSchemaName
        self.owningTableName = owningTableName
        self.owningColumnName = owningColumnName
        self.newType = newType
        self.oldType = oldType
        
    @property
    def owningSchemaName(self) -> str:
        return self.__owningSchemaName

    @owningSchemaName.setter
    def owningSchemaName(self, owningSchemaName: str):
        self.__owningSchemaName = owningSchemaName

    @property
    def oldType(self) -> str:
        return self.__oldType

    @oldType.setter
    def oldType(self, oldType: str):
        self.__oldType = oldType

    @property
    def owningTableName(self) -> str:
        return self.__owningTableName

    @owningTableName.setter
    def owningTableName(self, owningTableName: str):
        self.__owningTableName = owningTableName

    @property
    def newType(self) -> str:
        return self.__newType

    @newType.setter
    def newType(self, newType: str):
        self.__newType = newType

    @property
    def owningColumnName(self) -> str:
        return self.__owningColumnName

    @owningColumnName.setter
    def owningColumnName(self, owningColumnName: str):
        self.__owningColumnName = owningColumnName

class mm_ops_RenameTable(ModelOperation):

    def __init__(self, owningSchemaName: str, name: str, newName: str):
        self.owningSchemaName = owningSchemaName
        self.name = name
        self.newName = newName
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def owningSchemaName(self) -> str:
        return self.__owningSchemaName

    @owningSchemaName.setter
    def owningSchemaName(self, owningSchemaName: str):
        self.__owningSchemaName = owningSchemaName

    @property
    def newName(self) -> str:
        return self.__newName

    @newName.setter
    def newName(self, newName: str):
        self.__newName = newName

class mm_ops_AddUnique(ModelOperation):

    def __init__(self, owningSchemaName: str, owningTableName: str, constrainedColumnNames: str, name: str):
        self.owningSchemaName = owningSchemaName
        self.owningTableName = owningTableName
        self.constrainedColumnNames = constrainedColumnNames
        self.name = name
        
    @property
    def owningSchemaName(self) -> str:
        return self.__owningSchemaName

    @owningSchemaName.setter
    def owningSchemaName(self, owningSchemaName: str):
        self.__owningSchemaName = owningSchemaName

    @property
    def owningTableName(self) -> str:
        return self.__owningTableName

    @owningTableName.setter
    def owningTableName(self, owningTableName: str):
        self.__owningTableName = owningTableName

    @property
    def constrainedColumnNames(self) -> str:
        return self.__constrainedColumnNames

    @constrainedColumnNames.setter
    def constrainedColumnNames(self, constrainedColumnNames: str):
        self.__constrainedColumnNames = constrainedColumnNames

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class mm_ops_RemoveColumn(ModelOperation):

    def __init__(self, owningSchemaName: str, owningTableName: str, name: str):
        self.owningSchemaName = owningSchemaName
        self.owningTableName = owningTableName
        self.name = name
        
    @property
    def owningTableName(self) -> str:
        return self.__owningTableName

    @owningTableName.setter
    def owningTableName(self, owningTableName: str):
        self.__owningTableName = owningTableName

    @property
    def owningSchemaName(self) -> str:
        return self.__owningSchemaName

    @owningSchemaName.setter
    def owningSchemaName(self, owningSchemaName: str):
        self.__owningSchemaName = owningSchemaName

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class mm_ops_RemoveNotNull(ModelOperation):

    def __init__(self, owningSchemaName: str, owningTableName: str, constrainedColumnName: str):
        self.owningSchemaName = owningSchemaName
        self.owningTableName = owningTableName
        self.constrainedColumnName = constrainedColumnName
        
    @property
    def owningSchemaName(self) -> str:
        return self.__owningSchemaName

    @owningSchemaName.setter
    def owningSchemaName(self, owningSchemaName: str):
        self.__owningSchemaName = owningSchemaName

    @property
    def owningTableName(self) -> str:
        return self.__owningTableName

    @owningTableName.setter
    def owningTableName(self, owningTableName: str):
        self.__owningTableName = owningTableName

    @property
    def constrainedColumnName(self) -> str:
        return self.__constrainedColumnName

    @constrainedColumnName.setter
    def constrainedColumnName(self, constrainedColumnName: str):
        self.__constrainedColumnName = constrainedColumnName

class mm_ops_RemoveTable(ModelOperation):

    def __init__(self, owningSchemaName: str, name: str):
        self.owningSchemaName = owningSchemaName
        self.name = name
        
    @property
    def owningSchemaName(self) -> str:
        return self.__owningSchemaName

    @owningSchemaName.setter
    def owningSchemaName(self, owningSchemaName: str):
        self.__owningSchemaName = owningSchemaName

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class mm_ops_AddSequence(ModelOperation):

    def __init__(self, owningSchemaName: str, name: str, startValue: int):
        self.owningSchemaName = owningSchemaName
        self.name = name
        self.startValue = startValue
        
    @property
    def startValue(self) -> int:
        return self.__startValue

    @startValue.setter
    def startValue(self, startValue: int):
        self.__startValue = startValue

    @property
    def owningSchemaName(self) -> str:
        return self.__owningSchemaName

    @owningSchemaName.setter
    def owningSchemaName(self, owningSchemaName: str):
        self.__owningSchemaName = owningSchemaName

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class mm_ops_DeleteRows(ModelOperation):

    def __init__(self, owningSchemaName: str, tableName: str, whereCondition: str):
        self.owningSchemaName = owningSchemaName
        self.tableName = tableName
        self.whereCondition = whereCondition
        
    @property
    def owningSchemaName(self) -> str:
        return self.__owningSchemaName

    @owningSchemaName.setter
    def owningSchemaName(self, owningSchemaName: str):
        self.__owningSchemaName = owningSchemaName

    @property
    def whereCondition(self) -> str:
        return self.__whereCondition

    @whereCondition.setter
    def whereCondition(self, whereCondition: str):
        self.__whereCondition = whereCondition

    @property
    def tableName(self) -> str:
        return self.__tableName

    @tableName.setter
    def tableName(self, tableName: str):
        self.__tableName = tableName

class mm_ops_RemoveDefaultValue(ModelOperation):

    def __init__(self, owningSchemaName: str, owningTableName: str, owningColumnName: str):
        self.owningSchemaName = owningSchemaName
        self.owningTableName = owningTableName
        self.owningColumnName = owningColumnName
        
    @property
    def owningSchemaName(self) -> str:
        return self.__owningSchemaName

    @owningSchemaName.setter
    def owningSchemaName(self, owningSchemaName: str):
        self.__owningSchemaName = owningSchemaName

    @property
    def owningColumnName(self) -> str:
        return self.__owningColumnName

    @owningColumnName.setter
    def owningColumnName(self, owningColumnName: str):
        self.__owningColumnName = owningColumnName

    @property
    def owningTableName(self) -> str:
        return self.__owningTableName

    @owningTableName.setter
    def owningTableName(self, owningTableName: str):
        self.__owningTableName = owningTableName

class mm_ops_GenerateSequenceNumbers(ModelOperation):

    def __init__(self, owningSchemaName: str, tableName: str, columnName: str, sequenceName: str):
        self.owningSchemaName = owningSchemaName
        self.tableName = tableName
        self.columnName = columnName
        self.sequenceName = sequenceName
        
    @property
    def sequenceName(self) -> str:
        return self.__sequenceName

    @sequenceName.setter
    def sequenceName(self, sequenceName: str):
        self.__sequenceName = sequenceName

    @property
    def owningSchemaName(self) -> str:
        return self.__owningSchemaName

    @owningSchemaName.setter
    def owningSchemaName(self, owningSchemaName: str):
        self.__owningSchemaName = owningSchemaName

    @property
    def columnName(self) -> str:
        return self.__columnName

    @columnName.setter
    def columnName(self, columnName: str):
        self.__columnName = columnName

    @property
    def tableName(self) -> str:
        return self.__tableName

    @tableName.setter
    def tableName(self, tableName: str):
        self.__tableName = tableName

class mm_ops_InsertRows(ModelOperation):

    def __init__(self, owningSchemaName: str, sourceTableName: str, sourceColumnsNames: str, whereCondition: str, targetTableName: str, targetColumnNames: str):
        self.owningSchemaName = owningSchemaName
        self.sourceTableName = sourceTableName
        self.sourceColumnsNames = sourceColumnsNames
        self.whereCondition = whereCondition
        self.targetTableName = targetTableName
        self.targetColumnNames = targetColumnNames
        
    @property
    def targetColumnNames(self) -> str:
        return self.__targetColumnNames

    @targetColumnNames.setter
    def targetColumnNames(self, targetColumnNames: str):
        self.__targetColumnNames = targetColumnNames

    @property
    def sourceTableName(self) -> str:
        return self.__sourceTableName

    @sourceTableName.setter
    def sourceTableName(self, sourceTableName: str):
        self.__sourceTableName = sourceTableName

    @property
    def owningSchemaName(self) -> str:
        return self.__owningSchemaName

    @owningSchemaName.setter
    def owningSchemaName(self, owningSchemaName: str):
        self.__owningSchemaName = owningSchemaName

    @property
    def targetTableName(self) -> str:
        return self.__targetTableName

    @targetTableName.setter
    def targetTableName(self, targetTableName: str):
        self.__targetTableName = targetTableName

    @property
    def whereCondition(self) -> str:
        return self.__whereCondition

    @whereCondition.setter
    def whereCondition(self, whereCondition: str):
        self.__whereCondition = whereCondition

    @property
    def sourceColumnsNames(self) -> str:
        return self.__sourceColumnsNames

    @sourceColumnsNames.setter
    def sourceColumnsNames(self, sourceColumnsNames: str):
        self.__sourceColumnsNames = sourceColumnsNames

class mm_ops_NillRows(ModelOperation):

    def __init__(self, owningSchemaName: str, tableName: str, columnName: str, whereCondition: str):
        self.owningSchemaName = owningSchemaName
        self.tableName = tableName
        self.columnName = columnName
        self.whereCondition = whereCondition
        
    @property
    def whereCondition(self) -> str:
        return self.__whereCondition

    @whereCondition.setter
    def whereCondition(self, whereCondition: str):
        self.__whereCondition = whereCondition

    @property
    def tableName(self) -> str:
        return self.__tableName

    @tableName.setter
    def tableName(self, tableName: str):
        self.__tableName = tableName

    @property
    def columnName(self) -> str:
        return self.__columnName

    @columnName.setter
    def columnName(self, columnName: str):
        self.__columnName = columnName

    @property
    def owningSchemaName(self) -> str:
        return self.__owningSchemaName

    @owningSchemaName.setter
    def owningSchemaName(self, owningSchemaName: str):
        self.__owningSchemaName = owningSchemaName

class mm_ops_RemoveConstraint(ModelOperation):

    def __init__(self, owningSchemaName: str, owningTableName: str, name: str):
        self.owningSchemaName = owningSchemaName
        self.owningTableName = owningTableName
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def owningSchemaName(self) -> str:
        return self.__owningSchemaName

    @owningSchemaName.setter
    def owningSchemaName(self, owningSchemaName: str):
        self.__owningSchemaName = owningSchemaName

    @property
    def owningTableName(self) -> str:
        return self.__owningTableName

    @owningTableName.setter
    def owningTableName(self, owningTableName: str):
        self.__owningTableName = owningTableName

class mm_ops_AddPrimaryKey(ModelOperation):

    def __init__(self, owningSchemaName: str, owningTableName: str, constrainedColumnName: str, name: str):
        self.owningSchemaName = owningSchemaName
        self.owningTableName = owningTableName
        self.constrainedColumnName = constrainedColumnName
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def owningSchemaName(self) -> str:
        return self.__owningSchemaName

    @owningSchemaName.setter
    def owningSchemaName(self, owningSchemaName: str):
        self.__owningSchemaName = owningSchemaName

    @property
    def owningTableName(self) -> str:
        return self.__owningTableName

    @owningTableName.setter
    def owningTableName(self, owningTableName: str):
        self.__owningTableName = owningTableName

    @property
    def constrainedColumnName(self) -> str:
        return self.__constrainedColumnName

    @constrainedColumnName.setter
    def constrainedColumnName(self, constrainedColumnName: str):
        self.__constrainedColumnName = constrainedColumnName

class mm_ops_AddColumn(ModelOperation):

    def __init__(self, owningSchemaName: str, owningTableName: str, name: str, type: str, defaultValue: str):
        self.owningSchemaName = owningSchemaName
        self.owningTableName = owningTableName
        self.name = name
        self.type = type
        self.defaultValue = defaultValue
        
    @property
    def owningTableName(self) -> str:
        return self.__owningTableName

    @owningTableName.setter
    def owningTableName(self, owningTableName: str):
        self.__owningTableName = owningTableName

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def defaultValue(self) -> str:
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: str):
        self.__defaultValue = defaultValue

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def owningSchemaName(self) -> str:
        return self.__owningSchemaName

    @owningSchemaName.setter
    def owningSchemaName(self, owningSchemaName: str):
        self.__owningSchemaName = owningSchemaName

class mm_ops_SetDefaultValue(ModelOperation):

    def __init__(self, owningSchemaName: str, owningTableName: str, owningColumnName: str, newDefaultValue: str):
        self.owningSchemaName = owningSchemaName
        self.owningTableName = owningTableName
        self.owningColumnName = owningColumnName
        self.newDefaultValue = newDefaultValue
        
    @property
    def owningTableName(self) -> str:
        return self.__owningTableName

    @owningTableName.setter
    def owningTableName(self, owningTableName: str):
        self.__owningTableName = owningTableName

    @property
    def owningSchemaName(self) -> str:
        return self.__owningSchemaName

    @owningSchemaName.setter
    def owningSchemaName(self, owningSchemaName: str):
        self.__owningSchemaName = owningSchemaName

    @property
    def owningColumnName(self) -> str:
        return self.__owningColumnName

    @owningColumnName.setter
    def owningColumnName(self, owningColumnName: str):
        self.__owningColumnName = owningColumnName

    @property
    def newDefaultValue(self) -> str:
        return self.__newDefaultValue

    @newDefaultValue.setter
    def newDefaultValue(self, newDefaultValue: str):
        self.__newDefaultValue = newDefaultValue

class mm_ops_RenameColumn(ModelOperation):

    def __init__(self, owningSchemaName: str, owningTableName: str, name: str, newName: str):
        self.owningSchemaName = owningSchemaName
        self.owningTableName = owningTableName
        self.name = name
        self.newName = newName
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def owningSchemaName(self) -> str:
        return self.__owningSchemaName

    @owningSchemaName.setter
    def owningSchemaName(self, owningSchemaName: str):
        self.__owningSchemaName = owningSchemaName

    @property
    def newName(self) -> str:
        return self.__newName

    @newName.setter
    def newName(self, newName: str):
        self.__newName = newName

    @property
    def owningTableName(self) -> str:
        return self.__owningTableName

    @owningTableName.setter
    def owningTableName(self, owningTableName: str):
        self.__owningTableName = owningTableName

class mm_ops_AddForeignKey(ModelOperation):

    def __init__(self, owningSchemaName: str, owningTableName: str, constrainedColumnName: str, name: str, targetTableName: str):
        self.owningSchemaName = owningSchemaName
        self.owningTableName = owningTableName
        self.constrainedColumnName = constrainedColumnName
        self.name = name
        self.targetTableName = targetTableName
        
    @property
    def targetTableName(self) -> str:
        return self.__targetTableName

    @targetTableName.setter
    def targetTableName(self, targetTableName: str):
        self.__targetTableName = targetTableName

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def owningSchemaName(self) -> str:
        return self.__owningSchemaName

    @owningSchemaName.setter
    def owningSchemaName(self, owningSchemaName: str):
        self.__owningSchemaName = owningSchemaName

    @property
    def owningTableName(self) -> str:
        return self.__owningTableName

    @owningTableName.setter
    def owningTableName(self, owningTableName: str):
        self.__owningTableName = owningTableName

    @property
    def constrainedColumnName(self) -> str:
        return self.__constrainedColumnName

    @constrainedColumnName.setter
    def constrainedColumnName(self, constrainedColumnName: str):
        self.__constrainedColumnName = constrainedColumnName

class mm_ops_AddIndex(ModelOperation):

    def __init__(self, owningSchemaName: str, owningTableName: str, name: str, columnsNames: str):
        self.owningSchemaName = owningSchemaName
        self.owningTableName = owningTableName
        self.name = name
        self.columnsNames = columnsNames
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def owningSchemaName(self) -> str:
        return self.__owningSchemaName

    @owningSchemaName.setter
    def owningSchemaName(self, owningSchemaName: str):
        self.__owningSchemaName = owningSchemaName

    @property
    def columnsNames(self) -> str:
        return self.__columnsNames

    @columnsNames.setter
    def columnsNames(self, columnsNames: str):
        self.__columnsNames = columnsNames

    @property
    def owningTableName(self) -> str:
        return self.__owningTableName

    @owningTableName.setter
    def owningTableName(self, owningTableName: str):
        self.__owningTableName = owningTableName

class mm_ops_HasNoOwnInstances(ModelOperation):

    def __init__(self, whereCondition: str, owningSchemaName: str, tableName: str):
        self.whereCondition = whereCondition
        self.owningSchemaName = owningSchemaName
        self.tableName = tableName
        
    @property
    def tableName(self) -> str:
        return self.__tableName

    @tableName.setter
    def tableName(self, tableName: str):
        self.__tableName = tableName

    @property
    def whereCondition(self) -> str:
        return self.__whereCondition

    @whereCondition.setter
    def whereCondition(self, whereCondition: str):
        self.__whereCondition = whereCondition

    @property
    def owningSchemaName(self) -> str:
        return self.__owningSchemaName

    @owningSchemaName.setter
    def owningSchemaName(self, owningSchemaName: str):
        self.__owningSchemaName = owningSchemaName

class mm_ops_RemoveSequence(ModelOperation):

    def __init__(self, owningSchemaName: str, name: str):
        self.owningSchemaName = owningSchemaName
        self.name = name
        
    @property
    def owningSchemaName(self) -> str:
        return self.__owningSchemaName

    @owningSchemaName.setter
    def owningSchemaName(self, owningSchemaName: str):
        self.__owningSchemaName = owningSchemaName

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class mm_ops_UpdateRows(ModelOperation):

    def __init__(self, sourceTableName: str, sourceColumnName: str, targetTableName: str, targetColumnName: str, whereCondition: str, owningSchemaName: str):
        self.sourceTableName = sourceTableName
        self.sourceColumnName = sourceColumnName
        self.targetTableName = targetTableName
        self.targetColumnName = targetColumnName
        self.whereCondition = whereCondition
        self.owningSchemaName = owningSchemaName
        
    @property
    def owningSchemaName(self) -> str:
        return self.__owningSchemaName

    @owningSchemaName.setter
    def owningSchemaName(self, owningSchemaName: str):
        self.__owningSchemaName = owningSchemaName

    @property
    def sourceColumnName(self) -> str:
        return self.__sourceColumnName

    @sourceColumnName.setter
    def sourceColumnName(self, sourceColumnName: str):
        self.__sourceColumnName = sourceColumnName

    @property
    def whereCondition(self) -> str:
        return self.__whereCondition

    @whereCondition.setter
    def whereCondition(self, whereCondition: str):
        self.__whereCondition = whereCondition

    @property
    def targetColumnName(self) -> str:
        return self.__targetColumnName

    @targetColumnName.setter
    def targetColumnName(self, targetColumnName: str):
        self.__targetColumnName = targetColumnName

    @property
    def targetTableName(self) -> str:
        return self.__targetTableName

    @targetTableName.setter
    def targetTableName(self, targetTableName: str):
        self.__targetTableName = targetTableName

    @property
    def sourceTableName(self) -> str:
        return self.__sourceTableName

    @sourceTableName.setter
    def sourceTableName(self, sourceTableName: str):
        self.__sourceTableName = sourceTableName

class mm_ops_RemoveIndex(ModelOperation):

    def __init__(self, owningSchemaName: str, name: str):
        self.owningSchemaName = owningSchemaName
        self.name = name
        
    @property
    def owningSchemaName(self) -> str:
        return self.__owningSchemaName

    @owningSchemaName.setter
    def owningSchemaName(self, owningSchemaName: str):
        self.__owningSchemaName = owningSchemaName

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class mm_ops_AddTable(ModelOperation):

    def __init__(self, owningSchemaName: str, name: str):
        self.owningSchemaName = owningSchemaName
        self.name = name
        
    @property
    def owningSchemaName(self) -> str:
        return self.__owningSchemaName

    @owningSchemaName.setter
    def owningSchemaName(self, owningSchemaName: str):
        self.__owningSchemaName = owningSchemaName

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class mm_ops_AddSchema(ModelOperation):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class Operations:

    pass
class mm_ops_ModelOperation(ABC):

    pass
class mm_rdb_ForeignKey(TableConstraint):

    pass
class mm_rdb_PrimaryKey(TableConstraint):

    pass
class mm_rdb_Unique(TableConstraint):

    pass
class mm_rdb_TableConstraint(ABC):

    def __init__(self, name: str, Table30: "Table" = None):
        self.name = name
        self.Table30 = Table30
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Table30(self):
        return self.__Table30

    @Table30.setter
    def Table30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_rdb_TableConstraint__Table30", None)
        self.__Table30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdb31"):
                opp_val = getattr(old_value, "rdb31", None)
                if opp_val == self:
                    setattr(old_value, "rdb31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdb31"):
                opp_val = getattr(value, "rdb31", None)
                setattr(value, "rdb31", self)

class ops_ModelOperation:

    pass
class ModelRoot:

    pass
class mm_rdb_Operations(ModelRoot):

    pass
class mm_rdb_ModelRoot(ABC):

    pass
class mm_rdb_Index:

    def __init__(self, name: str, Schema15: "Schema" = None, mm_rdb_Index: set["Column"] = None):
        self.name = name
        self.Schema15 = Schema15
        self.mm_rdb_Index = mm_rdb_Index if mm_rdb_Index is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Schema15(self):
        return self.__Schema15

    @Schema15.setter
    def Schema15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_rdb_Index__Schema15", None)
        self.__Schema15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdb16"):
                opp_val = getattr(old_value, "rdb16", None)
                if opp_val == self:
                    setattr(old_value, "rdb16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdb16"):
                opp_val = getattr(value, "rdb16", None)
                setattr(value, "rdb16", self)

    @property
    def mm_rdb_Index(self):
        return self.__mm_rdb_Index

    @mm_rdb_Index.setter
    def mm_rdb_Index(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_rdb_Index__mm_rdb_Index", None)
        self.__mm_rdb_Index = value if value is not None else set()
        
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
                    

class mm_rdb_Sequence:

    def __init__(self, name: str, startValue: int, Schema12: "Schema" = None):
        self.name = name
        self.startValue = startValue
        self.Schema12 = Schema12
        
    @property
    def startValue(self) -> int:
        return self.__startValue

    @startValue.setter
    def startValue(self, startValue: int):
        self.__startValue = startValue

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Schema12(self):
        return self.__Schema12

    @Schema12.setter
    def Schema12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_rdb_Sequence__Schema12", None)
        self.__Schema12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdb13"):
                opp_val = getattr(old_value, "rdb13", None)
                if opp_val == self:
                    setattr(old_value, "rdb13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdb13"):
                opp_val = getattr(value, "rdb13", None)
                setattr(value, "rdb13", self)

class Index:

    pass
class Sequence:

    pass
class Table:

    pass
class Structure:

    pass
class mm_rdb_Schema:

    def __init__(self, name: str, Structure: "Structure" = None, Table: set["Table"] = None, Sequence: "Sequence" = None, Index: set["Index"] = None):
        self.name = name
        self.Structure = Structure
        self.Table = Table if Table is not None else set()
        self.Sequence = Sequence
        self.Index = Index if Index is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Index(self):
        return self.__Index

    @Index.setter
    def Index(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_rdb_Schema__Index", None)
        self.__Index = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rdb10"):
                    opp_val = getattr(item, "rdb10", None)
                    
                    if opp_val == self:
                        setattr(item, "rdb10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rdb10"):
                    opp_val = getattr(item, "rdb10", None)
                    
                    setattr(item, "rdb10", self)
                    

    @property
    def Structure(self):
        return self.__Structure

    @Structure.setter
    def Structure(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_rdb_Schema__Structure", None)
        self.__Structure = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdb4"):
                opp_val = getattr(old_value, "rdb4", None)
                if opp_val == self:
                    setattr(old_value, "rdb4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdb4"):
                opp_val = getattr(value, "rdb4", None)
                setattr(value, "rdb4", self)

    @property
    def Table(self):
        return self.__Table

    @Table.setter
    def Table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_rdb_Schema__Table", None)
        self.__Table = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rdb6"):
                    opp_val = getattr(item, "rdb6", None)
                    
                    if opp_val == self:
                        setattr(item, "rdb6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rdb6"):
                    opp_val = getattr(item, "rdb6", None)
                    
                    setattr(item, "rdb6", self)
                    

    @property
    def Sequence(self):
        return self.__Sequence

    @Sequence.setter
    def Sequence(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_rdb_Schema__Sequence", None)
        self.__Sequence = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdb8"):
                opp_val = getattr(old_value, "rdb8", None)
                if opp_val == self:
                    setattr(old_value, "rdb8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdb8"):
                opp_val = getattr(value, "rdb8", None)
                setattr(value, "rdb8", self)

class Schema:

    pass
class mm_rdb_Structure(ModelRoot):

    pass