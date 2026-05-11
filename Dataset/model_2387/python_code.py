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

class ModelOperation:

    pass
class mm_ops_SetDefaultValue(ModelOperation):

    def __init__(self, owningColumnName: str, newDefaultValue: str, owningSchemaName: str, owningTableName: str):
        self.owningColumnName = owningColumnName
        self.newDefaultValue = newDefaultValue
        self.owningSchemaName = owningSchemaName
        self.owningTableName = owningTableName
        
        pass
    @property
    def owningSchemaName(self):
        return self.__owningSchemaName

    @owningSchemaName.setter
    def owningSchemaName(self, owningSchemaName: str):
        self.__owningSchemaName = owningSchemaName


    @property
    def owningTableName(self):
        return self.__owningTableName

    @owningTableName.setter
    def owningTableName(self, owningTableName: str):
        self.__owningTableName = owningTableName


    @property
    def newDefaultValue(self):
        return self.__newDefaultValue

    @newDefaultValue.setter
    def newDefaultValue(self, newDefaultValue: str):
        self.__newDefaultValue = newDefaultValue


    @property
    def owningColumnName(self):
        return self.__owningColumnName

    @owningColumnName.setter
    def owningColumnName(self, owningColumnName: str):
        self.__owningColumnName = owningColumnName


class mm_ops_RenameColumn(ModelOperation):

    def __init__(self, owningSchemaName: str, owningTableName: str, name: str, newName: str):
        self.owningSchemaName = owningSchemaName
        self.owningTableName = owningTableName
        self.name = name
        self.newName = newName
        
        pass
    @property
    def owningTableName(self):
        return self.__owningTableName

    @owningTableName.setter
    def owningTableName(self, owningTableName: str):
        self.__owningTableName = owningTableName


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def owningSchemaName(self):
        return self.__owningSchemaName

    @owningSchemaName.setter
    def owningSchemaName(self, owningSchemaName: str):
        self.__owningSchemaName = owningSchemaName


    @property
    def newName(self):
        return self.__newName

    @newName.setter
    def newName(self, newName: str):
        self.__newName = newName


class mm_ops_HasNoInstances(ModelOperation):

    def __init__(self, owningSchemaName: str, tableName: str):
        self.owningSchemaName = owningSchemaName
        self.tableName = tableName
        
        pass
    @property
    def tableName(self):
        return self.__tableName

    @tableName.setter
    def tableName(self, tableName: str):
        self.__tableName = tableName


    @property
    def owningSchemaName(self):
        return self.__owningSchemaName

    @owningSchemaName.setter
    def owningSchemaName(self, owningSchemaName: str):
        self.__owningSchemaName = owningSchemaName


class mm_ops_AddTable(ModelOperation):

    def __init__(self, owningSchemaName: str, name: str):
        self.owningSchemaName = owningSchemaName
        self.name = name
        
        pass
    @property
    def owningSchemaName(self):
        return self.__owningSchemaName

    @owningSchemaName.setter
    def owningSchemaName(self, owningSchemaName: str):
        self.__owningSchemaName = owningSchemaName


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class mm_ops_AddIndex(ModelOperation):

    def __init__(self, owningSchemaName: str, owningTableName: str, name: str, columnsNames: str):
        self.owningSchemaName = owningSchemaName
        self.owningTableName = owningTableName
        self.name = name
        self.columnsNames = columnsNames
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def columnsNames(self):
        return self.__columnsNames

    @columnsNames.setter
    def columnsNames(self, columnsNames: str):
        self.__columnsNames = columnsNames


    @property
    def owningTableName(self):
        return self.__owningTableName

    @owningTableName.setter
    def owningTableName(self, owningTableName: str):
        self.__owningTableName = owningTableName


    @property
    def owningSchemaName(self):
        return self.__owningSchemaName

    @owningSchemaName.setter
    def owningSchemaName(self, owningSchemaName: str):
        self.__owningSchemaName = owningSchemaName


class mm_ops_RemoveIndex(ModelOperation):

    def __init__(self, owningSchemaName: str, name: str):
        self.owningSchemaName = owningSchemaName
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def owningSchemaName(self):
        return self.__owningSchemaName

    @owningSchemaName.setter
    def owningSchemaName(self, owningSchemaName: str):
        self.__owningSchemaName = owningSchemaName


class mm_ops_GenerateSequenceNumbers(ModelOperation):

    def __init__(self, owningSchemaName: str, tableName: str, columnName: str, sequenceName: str):
        self.owningSchemaName = owningSchemaName
        self.tableName = tableName
        self.columnName = columnName
        self.sequenceName = sequenceName
        
        pass
    @property
    def tableName(self):
        return self.__tableName

    @tableName.setter
    def tableName(self, tableName: str):
        self.__tableName = tableName


    @property
    def owningSchemaName(self):
        return self.__owningSchemaName

    @owningSchemaName.setter
    def owningSchemaName(self, owningSchemaName: str):
        self.__owningSchemaName = owningSchemaName


    @property
    def columnName(self):
        return self.__columnName

    @columnName.setter
    def columnName(self, columnName: str):
        self.__columnName = columnName


    @property
    def sequenceName(self):
        return self.__sequenceName

    @sequenceName.setter
    def sequenceName(self, sequenceName: str):
        self.__sequenceName = sequenceName


class mm_ops_RemoveColumn(ModelOperation):

    def __init__(self, owningSchemaName: str, owningTableName: str, name: str):
        self.owningSchemaName = owningSchemaName
        self.owningTableName = owningTableName
        self.name = name
        
        pass
    @property
    def owningTableName(self):
        return self.__owningTableName

    @owningTableName.setter
    def owningTableName(self, owningTableName: str):
        self.__owningTableName = owningTableName


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def owningSchemaName(self):
        return self.__owningSchemaName

    @owningSchemaName.setter
    def owningSchemaName(self, owningSchemaName: str):
        self.__owningSchemaName = owningSchemaName


class mm_ops_UpdateRows(ModelOperation):

    def __init__(self, owningSchemaName: str, sourceTableName: str, sourceColumnName: str, targetTableName: str, targetColumnName: str, whereCondition: str):
        self.owningSchemaName = owningSchemaName
        self.sourceTableName = sourceTableName
        self.sourceColumnName = sourceColumnName
        self.targetTableName = targetTableName
        self.targetColumnName = targetColumnName
        self.whereCondition = whereCondition
        
        pass
    @property
    def sourceTableName(self):
        return self.__sourceTableName

    @sourceTableName.setter
    def sourceTableName(self, sourceTableName: str):
        self.__sourceTableName = sourceTableName


    @property
    def sourceColumnName(self):
        return self.__sourceColumnName

    @sourceColumnName.setter
    def sourceColumnName(self, sourceColumnName: str):
        self.__sourceColumnName = sourceColumnName


    @property
    def whereCondition(self):
        return self.__whereCondition

    @whereCondition.setter
    def whereCondition(self, whereCondition: str):
        self.__whereCondition = whereCondition


    @property
    def owningSchemaName(self):
        return self.__owningSchemaName

    @owningSchemaName.setter
    def owningSchemaName(self, owningSchemaName: str):
        self.__owningSchemaName = owningSchemaName


    @property
    def targetTableName(self):
        return self.__targetTableName

    @targetTableName.setter
    def targetTableName(self, targetTableName: str):
        self.__targetTableName = targetTableName


    @property
    def targetColumnName(self):
        return self.__targetColumnName

    @targetColumnName.setter
    def targetColumnName(self, targetColumnName: str):
        self.__targetColumnName = targetColumnName


class mm_ops_NillRows(ModelOperation):

    def __init__(self, owningSchemaName: str, tableName: str, columnName: str, whereCondition: str):
        self.owningSchemaName = owningSchemaName
        self.tableName = tableName
        self.columnName = columnName
        self.whereCondition = whereCondition
        
        pass
    @property
    def owningSchemaName(self):
        return self.__owningSchemaName

    @owningSchemaName.setter
    def owningSchemaName(self, owningSchemaName: str):
        self.__owningSchemaName = owningSchemaName


    @property
    def columnName(self):
        return self.__columnName

    @columnName.setter
    def columnName(self, columnName: str):
        self.__columnName = columnName


    @property
    def tableName(self):
        return self.__tableName

    @tableName.setter
    def tableName(self, tableName: str):
        self.__tableName = tableName


    @property
    def whereCondition(self):
        return self.__whereCondition

    @whereCondition.setter
    def whereCondition(self, whereCondition: str):
        self.__whereCondition = whereCondition


class mm_ops_RemoveNotNull(ModelOperation):

    def __init__(self, owningSchemaName: str, owningTableName: str, constrainedColumnName: str):
        self.owningSchemaName = owningSchemaName
        self.owningTableName = owningTableName
        self.constrainedColumnName = constrainedColumnName
        
        pass
    @property
    def owningSchemaName(self):
        return self.__owningSchemaName

    @owningSchemaName.setter
    def owningSchemaName(self, owningSchemaName: str):
        self.__owningSchemaName = owningSchemaName


    @property
    def constrainedColumnName(self):
        return self.__constrainedColumnName

    @constrainedColumnName.setter
    def constrainedColumnName(self, constrainedColumnName: str):
        self.__constrainedColumnName = constrainedColumnName


    @property
    def owningTableName(self):
        return self.__owningTableName

    @owningTableName.setter
    def owningTableName(self, owningTableName: str):
        self.__owningTableName = owningTableName


class mm_ops_RemoveTable(ModelOperation):

    def __init__(self, owningSchemaName: str, name: str):
        self.owningSchemaName = owningSchemaName
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def owningSchemaName(self):
        return self.__owningSchemaName

    @owningSchemaName.setter
    def owningSchemaName(self, owningSchemaName: str):
        self.__owningSchemaName = owningSchemaName


class mm_ops_RemoveDefaultValue(ModelOperation):

    def __init__(self, owningSchemaName: str, owningTableName: str, owningColumnName: str):
        self.owningSchemaName = owningSchemaName
        self.owningTableName = owningTableName
        self.owningColumnName = owningColumnName
        
        pass
    @property
    def owningSchemaName(self):
        return self.__owningSchemaName

    @owningSchemaName.setter
    def owningSchemaName(self, owningSchemaName: str):
        self.__owningSchemaName = owningSchemaName


    @property
    def owningTableName(self):
        return self.__owningTableName

    @owningTableName.setter
    def owningTableName(self, owningTableName: str):
        self.__owningTableName = owningTableName


    @property
    def owningColumnName(self):
        return self.__owningColumnName

    @owningColumnName.setter
    def owningColumnName(self, owningColumnName: str):
        self.__owningColumnName = owningColumnName


class mm_ops_RemoveSequence(ModelOperation):

    def __init__(self, owningSchemaName: str, name: str):
        self.owningSchemaName = owningSchemaName
        self.name = name
        
        pass
    @property
    def owningSchemaName(self):
        return self.__owningSchemaName

    @owningSchemaName.setter
    def owningSchemaName(self, owningSchemaName: str):
        self.__owningSchemaName = owningSchemaName


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class mm_ops_AddPrimaryKey(ModelOperation):

    def __init__(self, owningSchemaName: str, owningTableName: str, constrainedColumnName: str, name: str):
        self.owningSchemaName = owningSchemaName
        self.owningTableName = owningTableName
        self.constrainedColumnName = constrainedColumnName
        self.name = name
        
        pass
    @property
    def owningSchemaName(self):
        return self.__owningSchemaName

    @owningSchemaName.setter
    def owningSchemaName(self, owningSchemaName: str):
        self.__owningSchemaName = owningSchemaName


    @property
    def constrainedColumnName(self):
        return self.__constrainedColumnName

    @constrainedColumnName.setter
    def constrainedColumnName(self, constrainedColumnName: str):
        self.__constrainedColumnName = constrainedColumnName


    @property
    def owningTableName(self):
        return self.__owningTableName

    @owningTableName.setter
    def owningTableName(self, owningTableName: str):
        self.__owningTableName = owningTableName


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class mm_ops_RemoveConstraint(ModelOperation):

    def __init__(self, owningSchemaName: str, owningTableName: str, name: str):
        self.owningSchemaName = owningSchemaName
        self.owningTableName = owningTableName
        self.name = name
        
        pass
    @property
    def owningTableName(self):
        return self.__owningTableName

    @owningTableName.setter
    def owningTableName(self, owningTableName: str):
        self.__owningTableName = owningTableName


    @property
    def owningSchemaName(self):
        return self.__owningSchemaName

    @owningSchemaName.setter
    def owningSchemaName(self, owningSchemaName: str):
        self.__owningSchemaName = owningSchemaName


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class mm_ops_RenameTable(ModelOperation):

    def __init__(self, owningSchemaName: str, name: str, newName: str):
        self.owningSchemaName = owningSchemaName
        self.name = name
        self.newName = newName
        
        pass
    @property
    def newName(self):
        return self.__newName

    @newName.setter
    def newName(self, newName: str):
        self.__newName = newName


    @property
    def owningSchemaName(self):
        return self.__owningSchemaName

    @owningSchemaName.setter
    def owningSchemaName(self, owningSchemaName: str):
        self.__owningSchemaName = owningSchemaName


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class mm_ops_AddSequence(ModelOperation):

    def __init__(self, owningSchemaName: str, name: str, startValue: int):
        self.owningSchemaName = owningSchemaName
        self.name = name
        self.startValue = startValue
        
        pass
    @property
    def startValue(self):
        return self.__startValue

    @startValue.setter
    def startValue(self, startValue: int):
        self.__startValue = startValue


    @property
    def owningSchemaName(self):
        return self.__owningSchemaName

    @owningSchemaName.setter
    def owningSchemaName(self, owningSchemaName: str):
        self.__owningSchemaName = owningSchemaName


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class mm_ops_HasNoOwnInstances(ModelOperation):

    def __init__(self, owningSchemaName: str, tableName: str, whereCondition: str):
        self.owningSchemaName = owningSchemaName
        self.tableName = tableName
        self.whereCondition = whereCondition
        
        pass
    @property
    def tableName(self):
        return self.__tableName

    @tableName.setter
    def tableName(self, tableName: str):
        self.__tableName = tableName


    @property
    def owningSchemaName(self):
        return self.__owningSchemaName

    @owningSchemaName.setter
    def owningSchemaName(self, owningSchemaName: str):
        self.__owningSchemaName = owningSchemaName


    @property
    def whereCondition(self):
        return self.__whereCondition

    @whereCondition.setter
    def whereCondition(self, whereCondition: str):
        self.__whereCondition = whereCondition


class mm_ops_InsertRows(ModelOperation):

    def __init__(self, owningSchemaName: str, sourceTableName: str, sourceColumnsNames: str, whereCondition: str, targetTableName: str, targetColumnNames: str):
        self.owningSchemaName = owningSchemaName
        self.sourceTableName = sourceTableName
        self.sourceColumnsNames = sourceColumnsNames
        self.whereCondition = whereCondition
        self.targetTableName = targetTableName
        self.targetColumnNames = targetColumnNames
        
        pass
    @property
    def sourceTableName(self):
        return self.__sourceTableName

    @sourceTableName.setter
    def sourceTableName(self, sourceTableName: str):
        self.__sourceTableName = sourceTableName


    @property
    def targetTableName(self):
        return self.__targetTableName

    @targetTableName.setter
    def targetTableName(self, targetTableName: str):
        self.__targetTableName = targetTableName


    @property
    def targetColumnNames(self):
        return self.__targetColumnNames

    @targetColumnNames.setter
    def targetColumnNames(self, targetColumnNames: str):
        self.__targetColumnNames = targetColumnNames


    @property
    def whereCondition(self):
        return self.__whereCondition

    @whereCondition.setter
    def whereCondition(self, whereCondition: str):
        self.__whereCondition = whereCondition


    @property
    def owningSchemaName(self):
        return self.__owningSchemaName

    @owningSchemaName.setter
    def owningSchemaName(self, owningSchemaName: str):
        self.__owningSchemaName = owningSchemaName


    @property
    def sourceColumnsNames(self):
        return self.__sourceColumnsNames

    @sourceColumnsNames.setter
    def sourceColumnsNames(self, sourceColumnsNames: str):
        self.__sourceColumnsNames = sourceColumnsNames


class mm_ops_DeleteRows(ModelOperation):

    def __init__(self, owningSchemaName: str, tableName: str, whereCondition: str):
        self.owningSchemaName = owningSchemaName
        self.tableName = tableName
        self.whereCondition = whereCondition
        
        pass
    @property
    def owningSchemaName(self):
        return self.__owningSchemaName

    @owningSchemaName.setter
    def owningSchemaName(self, owningSchemaName: str):
        self.__owningSchemaName = owningSchemaName


    @property
    def tableName(self):
        return self.__tableName

    @tableName.setter
    def tableName(self, tableName: str):
        self.__tableName = tableName


    @property
    def whereCondition(self):
        return self.__whereCondition

    @whereCondition.setter
    def whereCondition(self, whereCondition: str):
        self.__whereCondition = whereCondition


class mm_ops_SetColumnType(ModelOperation):

    def __init__(self, owningSchemaName: str, owningTableName: str, owningColumnName: str, newType: str, oldType: str):
        self.owningSchemaName = owningSchemaName
        self.owningTableName = owningTableName
        self.owningColumnName = owningColumnName
        self.newType = newType
        self.oldType = oldType
        
        pass
    @property
    def oldType(self):
        return self.__oldType

    @oldType.setter
    def oldType(self, oldType: str):
        self.__oldType = oldType


    @property
    def owningTableName(self):
        return self.__owningTableName

    @owningTableName.setter
    def owningTableName(self, owningTableName: str):
        self.__owningTableName = owningTableName


    @property
    def owningSchemaName(self):
        return self.__owningSchemaName

    @owningSchemaName.setter
    def owningSchemaName(self, owningSchemaName: str):
        self.__owningSchemaName = owningSchemaName


    @property
    def newType(self):
        return self.__newType

    @newType.setter
    def newType(self, newType: str):
        self.__newType = newType


    @property
    def owningColumnName(self):
        return self.__owningColumnName

    @owningColumnName.setter
    def owningColumnName(self, owningColumnName: str):
        self.__owningColumnName = owningColumnName


class mm_ops_AddColumn(ModelOperation):

    def __init__(self, owningSchemaName: str, owningTableName: str, name: str, type: str, defaultValue: str):
        self.owningSchemaName = owningSchemaName
        self.owningTableName = owningTableName
        self.name = name
        self.type = type
        self.defaultValue = defaultValue
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def owningTableName(self):
        return self.__owningTableName

    @owningTableName.setter
    def owningTableName(self, owningTableName: str):
        self.__owningTableName = owningTableName


    @property
    def owningSchemaName(self):
        return self.__owningSchemaName

    @owningSchemaName.setter
    def owningSchemaName(self, owningSchemaName: str):
        self.__owningSchemaName = owningSchemaName


    @property
    def defaultValue(self):
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: str):
        self.__defaultValue = defaultValue


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


class mm_ops_AddSchema(ModelOperation):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class Operations:

    pass
class mm_ops_AddNotNull(ModelOperation):

    def __init__(self, owningSchemaName: str, owningTableName: str, constrainedColumnName: str):
        self.owningSchemaName = owningSchemaName
        self.owningTableName = owningTableName
        self.constrainedColumnName = constrainedColumnName
        
        pass
    @property
    def owningSchemaName(self):
        return self.__owningSchemaName

    @owningSchemaName.setter
    def owningSchemaName(self, owningSchemaName: str):
        self.__owningSchemaName = owningSchemaName


    @property
    def constrainedColumnName(self):
        return self.__constrainedColumnName

    @constrainedColumnName.setter
    def constrainedColumnName(self, constrainedColumnName: str):
        self.__constrainedColumnName = constrainedColumnName


    @property
    def owningTableName(self):
        return self.__owningTableName

    @owningTableName.setter
    def owningTableName(self, owningTableName: str):
        self.__owningTableName = owningTableName


class mm_ops_AddUnique(ModelOperation):

    def __init__(self, owningSchemaName: str, owningTableName: str, constrainedColumnNames: str, name: str):
        self.owningSchemaName = owningSchemaName
        self.owningTableName = owningTableName
        self.constrainedColumnNames = constrainedColumnNames
        self.name = name
        
        pass
    @property
    def constrainedColumnNames(self):
        return self.__constrainedColumnNames

    @constrainedColumnNames.setter
    def constrainedColumnNames(self, constrainedColumnNames: str):
        self.__constrainedColumnNames = constrainedColumnNames


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def owningTableName(self):
        return self.__owningTableName

    @owningTableName.setter
    def owningTableName(self, owningTableName: str):
        self.__owningTableName = owningTableName


    @property
    def owningSchemaName(self):
        return self.__owningSchemaName

    @owningSchemaName.setter
    def owningSchemaName(self, owningSchemaName: str):
        self.__owningSchemaName = owningSchemaName


class mm_ops_AddForeignKey(ModelOperation):

    def __init__(self, owningSchemaName: str, owningTableName: str, constrainedColumnName: str, name: str, targetTableName: str):
        self.owningSchemaName = owningSchemaName
        self.owningTableName = owningTableName
        self.constrainedColumnName = constrainedColumnName
        self.name = name
        self.targetTableName = targetTableName
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def owningSchemaName(self):
        return self.__owningSchemaName

    @owningSchemaName.setter
    def owningSchemaName(self, owningSchemaName: str):
        self.__owningSchemaName = owningSchemaName


    @property
    def targetTableName(self):
        return self.__targetTableName

    @targetTableName.setter
    def targetTableName(self, targetTableName: str):
        self.__targetTableName = targetTableName


    @property
    def constrainedColumnName(self):
        return self.__constrainedColumnName

    @constrainedColumnName.setter
    def constrainedColumnName(self, constrainedColumnName: str):
        self.__constrainedColumnName = constrainedColumnName


    @property
    def owningTableName(self):
        return self.__owningTableName

    @owningTableName.setter
    def owningTableName(self, owningTableName: str):
        self.__owningTableName = owningTableName


class mm_rdb_TableConstraint(ABC):

    def __init__(self, name: str, constraints: "Table" = None):
        self.name = name
        self.constraints = constraints
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def constraints(self):
        return self.__constraints

    @constraints.setter
    def constraints(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_rdb_TableConstraint__constraints", None)
        self.__constraints = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Table22"):
                opp_val = getattr(old_value, "Table22", None)
                if opp_val == self:
                    setattr(old_value, "Table22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Table22"):
                opp_val = getattr(value, "Table22", None)
                setattr(value, "Table22", self)

class mm_rdb_Column:

    def __init__(self, name: str, type: str, defaultValue: str, isNillable: str, columns: "Table" = None):
        self.name = name
        self.type = type
        self.defaultValue = defaultValue
        self.isNillable = isNillable
        self.columns = columns
        
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
    def isNillable(self):
        return self.__isNillable

    @isNillable.setter
    def isNillable(self, isNillable: str):
        self.__isNillable = isNillable


    @property
    def defaultValue(self):
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: str):
        self.__defaultValue = defaultValue


    @property
    def columns(self):
        return self.__columns

    @columns.setter
    def columns(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_rdb_Column__columns", None)
        self.__columns = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Table20"):
                opp_val = getattr(old_value, "Table20", None)
                if opp_val == self:
                    setattr(old_value, "Table20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Table20"):
                opp_val = getattr(value, "Table20", None)
                setattr(value, "Table20", self)

class TableConstraint:

    pass
class mm_rdb_Unique(TableConstraint):

    pass
class mm_rdb_Table:

    def __init__(self, name: str, tables: "Schema" = None, owningTable: set["Column"] = None, owningTable18: set["TableConstraint"] = None):
        self.name = name
        self.tables = tables
        self.owningTable = owningTable if owningTable is not None else set()
        self.owningTable18 = owningTable18 if owningTable18 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


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
                if hasattr(item, "Column16"):
                    opp_val = getattr(item, "Column16", None)
                    
                    if opp_val == self:
                        setattr(item, "Column16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Column16"):
                    opp_val = getattr(item, "Column16", None)
                    
                    setattr(item, "Column16", self)
                    

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
            if hasattr(old_value, "Schema14"):
                opp_val = getattr(old_value, "Schema14", None)
                if opp_val == self:
                    setattr(old_value, "Schema14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Schema14"):
                opp_val = getattr(value, "Schema14", None)
                setattr(value, "Schema14", self)

    @property
    def owningTable18(self):
        return self.__owningTable18

    @owningTable18.setter
    def owningTable18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_rdb_Table__owningTable18", None)
        self.__owningTable18 = value if value is not None else set()
        
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
                    

class Column:

    pass
class mm_ops_ModelOperation(ABC):

    pass
class mm_rdb_ForeignKey(TableConstraint):

    pass
class Sequence:

    pass
class mm_rdb_PrimaryKey(TableConstraint):

    pass
class Table:

    pass
class Structure:

    pass
class mm_rdb_Schema:

    def __init__(self, name: str, owningSchema5: "Sequence" = None, owningSchema7: set["Index"] = None, schemas: "Structure" = None, owningSchema: set["Table"] = None):
        self.name = name
        self.owningSchema5 = owningSchema5
        self.owningSchema7 = owningSchema7 if owningSchema7 is not None else set()
        self.schemas = schemas
        self.owningSchema = owningSchema if owningSchema is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def owningSchema7(self):
        return self.__owningSchema7

    @owningSchema7.setter
    def owningSchema7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_rdb_Schema__owningSchema7", None)
        self.__owningSchema7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Index"):
                    opp_val = getattr(item, "Index", None)
                    
                    if opp_val == self:
                        setattr(item, "Index", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Index"):
                    opp_val = getattr(item, "Index", None)
                    
                    setattr(item, "Index", self)
                    

    @property
    def owningSchema(self):
        return self.__owningSchema

    @owningSchema.setter
    def owningSchema(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_rdb_Schema__owningSchema", None)
        self.__owningSchema = value if value is not None else set()
        
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
    def owningSchema5(self):
        return self.__owningSchema5

    @owningSchema5.setter
    def owningSchema5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_rdb_Schema__owningSchema5", None)
        self.__owningSchema5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Sequence"):
                opp_val = getattr(old_value, "Sequence", None)
                if opp_val == self:
                    setattr(old_value, "Sequence", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Sequence"):
                opp_val = getattr(value, "Sequence", None)
                setattr(value, "Sequence", self)

    @property
    def schemas(self):
        return self.__schemas

    @schemas.setter
    def schemas(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_rdb_Schema__schemas", None)
        self.__schemas = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Structure"):
                opp_val = getattr(old_value, "Structure", None)
                if opp_val == self:
                    setattr(old_value, "Structure", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Structure"):
                opp_val = getattr(value, "Structure", None)
                setattr(value, "Structure", self)

class Schema:

    pass
class ops_ModelOperation:

    pass
class ModelRoot:

    pass
class mm_rdb_Structure(ModelRoot):

    pass
class mm_rdb_Operations(ModelRoot):

    pass
class mm_rdb_Index:

    def __init__(self, name: str, indexes: "Schema" = None, mm_rdb_Index: set["Column"] = None):
        self.name = name
        self.indexes = indexes
        self.mm_rdb_Index = mm_rdb_Index if mm_rdb_Index is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def indexes(self):
        return self.__indexes

    @indexes.setter
    def indexes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_rdb_Index__indexes", None)
        self.__indexes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Schema11"):
                opp_val = getattr(old_value, "Schema11", None)
                if opp_val == self:
                    setattr(old_value, "Schema11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Schema11"):
                opp_val = getattr(value, "Schema11", None)
                setattr(value, "Schema11", self)

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

    def __init__(self, name: str, startValue: int, sequence: "Schema" = None):
        self.name = name
        self.startValue = startValue
        self.sequence = sequence
        
        pass
    @property
    def startValue(self):
        return self.__startValue

    @startValue.setter
    def startValue(self, startValue: int):
        self.__startValue = startValue


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def sequence(self):
        return self.__sequence

    @sequence.setter
    def sequence(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_rdb_Sequence__sequence", None)
        self.__sequence = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Schema9"):
                opp_val = getattr(old_value, "Schema9", None)
                if opp_val == self:
                    setattr(old_value, "Schema9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Schema9"):
                opp_val = getattr(value, "Schema9", None)
                setattr(value, "Schema9", self)

class Index:

    pass
class mm_rdb_ModelRoot(ABC):

    pass