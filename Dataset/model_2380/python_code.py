from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ActionTimeType(Enum):
    AFTER = "AFTER"
    BEFORE = "BEFORE"
    INSTEADOF = "INSTEADOF"
class ActionGranularityType(Enum):
    STATEMENT = "STATEMENT"
    ROW = "ROW"
class ReferentialActionType(Enum):
    CASCADE = "CASCADE"
    SET_NULL = "SET_NULL"
    SET_DEFAULT = "SET_DEFAULT"
    NO_ACTION = "NO_ACTION"
    RESTRICT = "RESTRICT"


############################################
# Definition of Classes
############################################

class UserDefinedType:

    pass
class relational_DistinctUserDefinedType(UserDefinedType):

    pass
class DistinctUserDefinedType:

    pass
class relational_Domain(DistinctUserDefinedType):

    def __init__(self, defaultValue: str, nullable: bool, relational_Domain: "relational_CheckConstraint" = None, relational_Domain49: "relational_DataType" = None):
        self.defaultValue = defaultValue
        self.nullable = nullable
        self.relational_Domain = relational_Domain
        self.relational_Domain49 = relational_Domain49
        
    @property
    def defaultValue(self) -> str:
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: str):
        self.__defaultValue = defaultValue

    @property
    def nullable(self) -> bool:
        return self.__nullable

    @nullable.setter
    def nullable(self, nullable: bool):
        self.__nullable = nullable

    @property
    def relational_Domain49(self):
        return self.__relational_Domain49

    @relational_Domain49.setter
    def relational_Domain49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_Domain__relational_Domain49", None)
        self.__relational_Domain49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "relational_DataType"):
                opp_val = getattr(old_value, "relational_DataType", None)
                if opp_val == self:
                    setattr(old_value, "relational_DataType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "relational_DataType"):
                opp_val = getattr(value, "relational_DataType", None)
                setattr(value, "relational_DataType", self)

    @property
    def relational_Domain(self):
        return self.__relational_Domain

    @relational_Domain.setter
    def relational_Domain(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_Domain__relational_Domain", None)
        self.__relational_Domain = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "relational_CheckConstraint"):
                opp_val = getattr(old_value, "relational_CheckConstraint", None)
                if opp_val == self:
                    setattr(old_value, "relational_CheckConstraint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "relational_CheckConstraint"):
                opp_val = getattr(value, "relational_CheckConstraint", None)
                setattr(value, "relational_CheckConstraint", self)

class DataType:

    pass
class UniqueConstraint:

    pass
class relational_PrimaryKey(UniqueConstraint):

    pass
class TableConstraint:

    pass
class relational_CheckConstraint(TableConstraint):

    def __init__(self, searchCondition: str, relational_CheckConstraint: "relational_Domain" = None):
        self.searchCondition = searchCondition
        self.relational_CheckConstraint = relational_CheckConstraint
        
    @property
    def searchCondition(self) -> str:
        return self.__searchCondition

    @searchCondition.setter
    def searchCondition(self, searchCondition: str):
        self.__searchCondition = searchCondition

    @property
    def relational_CheckConstraint(self):
        return self.__relational_CheckConstraint

    @relational_CheckConstraint.setter
    def relational_CheckConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_CheckConstraint__relational_CheckConstraint", None)
        self.__relational_CheckConstraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "relational_Domain"):
                opp_val = getattr(old_value, "relational_Domain", None)
                if opp_val == self:
                    setattr(old_value, "relational_Domain", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "relational_Domain"):
                opp_val = getattr(value, "relational_Domain", None)
                setattr(value, "relational_Domain", self)

class Constraint:

    pass
class ReferenceConstraint:

    pass
class relational_UniqueConstraint(ReferenceConstraint):

    pass
class Table:

    pass
class relational_BaseTable(Table):

    pass
class relational_ForeignKey(ReferenceConstraint):

    def __init__(self, onUpdate: str, onDelete: str, ForeignKey: "relational_Column" = None, ForeignKey30: "relational_BaseTable" = None, referencingForeignKeys: "relational_BaseTable" = None, foreignKey: "relational_UniqueConstraint" = None, foreignKey39: set["relational_Column"] = None, ForeignKey42: "relational_UniqueConstraint" = None):
        self.onUpdate = onUpdate
        self.onDelete = onDelete
        self.ForeignKey = ForeignKey
        self.ForeignKey30 = ForeignKey30
        self.referencingForeignKeys = referencingForeignKeys
        self.foreignKey = foreignKey
        self.foreignKey39 = foreignKey39 if foreignKey39 is not None else set()
        self.ForeignKey42 = ForeignKey42
        
    @property
    def onUpdate(self) -> str:
        return self.__onUpdate

    @onUpdate.setter
    def onUpdate(self, onUpdate: str):
        self.__onUpdate = onUpdate

    @property
    def onDelete(self) -> str:
        return self.__onDelete

    @onDelete.setter
    def onDelete(self, onDelete: str):
        self.__onDelete = onDelete

    @property
    def foreignKey(self):
        return self.__foreignKey

    @foreignKey.setter
    def foreignKey(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_ForeignKey__foreignKey", None)
        self.__foreignKey = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UniqueConstraint"):
                opp_val = getattr(old_value, "UniqueConstraint", None)
                if opp_val == self:
                    setattr(old_value, "UniqueConstraint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UniqueConstraint"):
                opp_val = getattr(value, "UniqueConstraint", None)
                setattr(value, "UniqueConstraint", self)

    @property
    def ForeignKey42(self):
        return self.__ForeignKey42

    @ForeignKey42.setter
    def ForeignKey42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_ForeignKey__ForeignKey42", None)
        self.__ForeignKey42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uniqueConstraint"):
                opp_val = getattr(old_value, "uniqueConstraint", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uniqueConstraint"):
                opp_val = getattr(value, "uniqueConstraint", None)
                if opp_val is None:
                    setattr(value, "uniqueConstraint", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ForeignKey30(self):
        return self.__ForeignKey30

    @ForeignKey30.setter
    def ForeignKey30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_ForeignKey__ForeignKey30", None)
        self.__ForeignKey30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "referencedTable"):
                opp_val = getattr(old_value, "referencedTable", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "referencedTable"):
                opp_val = getattr(value, "referencedTable", None)
                if opp_val is None:
                    setattr(value, "referencedTable", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def foreignKey39(self):
        return self.__foreignKey39

    @foreignKey39.setter
    def foreignKey39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_ForeignKey__foreignKey39", None)
        self.__foreignKey39 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Column40"):
                    opp_val = getattr(item, "Column40", None)
                    
                    if opp_val == self:
                        setattr(item, "Column40", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Column40"):
                    opp_val = getattr(item, "Column40", None)
                    
                    setattr(item, "Column40", self)
                    

    @property
    def referencingForeignKeys(self):
        return self.__referencingForeignKeys

    @referencingForeignKeys.setter
    def referencingForeignKeys(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_ForeignKey__referencingForeignKeys", None)
        self.__referencingForeignKeys = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BaseTable36"):
                opp_val = getattr(old_value, "BaseTable36", None)
                if opp_val == self:
                    setattr(old_value, "BaseTable36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BaseTable36"):
                opp_val = getattr(value, "BaseTable36", None)
                setattr(value, "BaseTable36", self)

    @property
    def ForeignKey(self):
        return self.__ForeignKey

    @ForeignKey.setter
    def ForeignKey(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_ForeignKey__ForeignKey", None)
        self.__ForeignKey = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "referencedMembers"):
                opp_val = getattr(old_value, "referencedMembers", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "referencedMembers"):
                opp_val = getattr(value, "referencedMembers", None)
                if opp_val is None:
                    setattr(value, "referencedMembers", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class relational_ReferenceConstraint(TableConstraint):

    pass
class relational_TableConstraint(Constraint):

    pass
class TypedElement:

    pass
class relational_Column(TypedElement):

    def __init__(self, nullable: bool, defaultValue: str, length: int, srid: str, columns: "relational_Table" = None, Column: "relational_Table" = None, members: set["relational_ReferenceConstraint"] = None, referencedMembers: set["relational_ForeignKey"] = None, Column34: "relational_ReferenceConstraint" = None, Column40: "relational_ForeignKey" = None):
        self.nullable = nullable
        self.defaultValue = defaultValue
        self.length = length
        self.srid = srid
        self.columns = columns
        self.Column = Column
        self.members = members if members is not None else set()
        self.referencedMembers = referencedMembers if referencedMembers is not None else set()
        self.Column34 = Column34
        self.Column40 = Column40
        
    @property
    def srid(self) -> str:
        return self.__srid

    @srid.setter
    def srid(self, srid: str):
        self.__srid = srid

    @property
    def nullable(self) -> bool:
        return self.__nullable

    @nullable.setter
    def nullable(self, nullable: bool):
        self.__nullable = nullable

    @property
    def length(self) -> int:
        return self.__length

    @length.setter
    def length(self, length: int):
        self.__length = length

    @property
    def defaultValue(self) -> str:
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
        old_value = getattr(self, f"_relational_Column__columns", None)
        self.__columns = value
        
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
    def Column40(self):
        return self.__Column40

    @Column40.setter
    def Column40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_Column__Column40", None)
        self.__Column40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "foreignKey39"):
                opp_val = getattr(old_value, "foreignKey39", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "foreignKey39"):
                opp_val = getattr(value, "foreignKey39", None)
                if opp_val is None:
                    setattr(value, "foreignKey39", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Column(self):
        return self.__Column

    @Column.setter
    def Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_Column__Column", None)
        self.__Column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "table24"):
                opp_val = getattr(old_value, "table24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "table24"):
                opp_val = getattr(value, "table24", None)
                if opp_val is None:
                    setattr(value, "table24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Column34(self):
        return self.__Column34

    @Column34.setter
    def Column34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_Column__Column34", None)
        self.__Column34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "referenceConstraint"):
                opp_val = getattr(old_value, "referenceConstraint", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "referenceConstraint"):
                opp_val = getattr(value, "referenceConstraint", None)
                if opp_val is None:
                    setattr(value, "referenceConstraint", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def referencedMembers(self):
        return self.__referencedMembers

    @referencedMembers.setter
    def referencedMembers(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_Column__referencedMembers", None)
        self.__referencedMembers = value if value is not None else set()
        
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
    def members(self):
        return self.__members

    @members.setter
    def members(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_Column__members", None)
        self.__members = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ReferenceConstraint"):
                    opp_val = getattr(item, "ReferenceConstraint", None)
                    
                    if opp_val == self:
                        setattr(item, "ReferenceConstraint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ReferenceConstraint"):
                    opp_val = getattr(item, "ReferenceConstraint", None)
                    
                    setattr(item, "ReferenceConstraint", self)
                    

class relational_Assertion(Constraint):

    def __init__(self, searchCondition: str, Assertion: "relational_Schema" = None, assertions: "relational_Schema" = None):
        self.searchCondition = searchCondition
        self.Assertion = Assertion
        self.assertions = assertions
        
    @property
    def searchCondition(self) -> str:
        return self.__searchCondition

    @searchCondition.setter
    def searchCondition(self, searchCondition: str):
        self.__searchCondition = searchCondition

    @property
    def assertions(self):
        return self.__assertions

    @assertions.setter
    def assertions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_Assertion__assertions", None)
        self.__assertions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Schema44"):
                opp_val = getattr(old_value, "Schema44", None)
                if opp_val == self:
                    setattr(old_value, "Schema44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Schema44"):
                opp_val = getattr(value, "Schema44", None)
                setattr(value, "Schema44", self)

    @property
    def Assertion(self):
        return self.__Assertion

    @Assertion.setter
    def Assertion(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_Assertion__Assertion", None)
        self.__Assertion = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "schema8"):
                opp_val = getattr(old_value, "schema8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "schema8"):
                opp_val = getattr(value, "schema8", None)
                if opp_val is None:
                    setattr(value, "schema8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class SQLObject:

    pass
class relational_TypedElement(SQLObject):

    pass
class relational_Table(SQLObject):

    pass
class relational_Trigger(SQLObject):

    def __init__(self, updateType: bool, insertType: bool, deleteType: bool, actionTime: str, condition: str, statementSQL: str, oldRow: str, newRow: str, oldTable: str, newTable: str, actionGranularity: str, Trigger: "relational_Schema" = None, triggersConstrainted: set["relational_Table"] = None, triggers: "relational_Schema" = None, triggers13: "relational_Table" = None, Trigger20: "relational_Table" = None, Trigger22: "relational_Table" = None):
        self.updateType = updateType
        self.insertType = insertType
        self.deleteType = deleteType
        self.actionTime = actionTime
        self.condition = condition
        self.statementSQL = statementSQL
        self.oldRow = oldRow
        self.newRow = newRow
        self.oldTable = oldTable
        self.newTable = newTable
        self.actionGranularity = actionGranularity
        self.Trigger = Trigger
        self.triggersConstrainted = triggersConstrainted if triggersConstrainted is not None else set()
        self.triggers = triggers
        self.triggers13 = triggers13
        self.Trigger20 = Trigger20
        self.Trigger22 = Trigger22
        
    @property
    def newRow(self) -> str:
        return self.__newRow

    @newRow.setter
    def newRow(self, newRow: str):
        self.__newRow = newRow

    @property
    def insertType(self) -> bool:
        return self.__insertType

    @insertType.setter
    def insertType(self, insertType: bool):
        self.__insertType = insertType

    @property
    def updateType(self) -> bool:
        return self.__updateType

    @updateType.setter
    def updateType(self, updateType: bool):
        self.__updateType = updateType

    @property
    def oldTable(self) -> str:
        return self.__oldTable

    @oldTable.setter
    def oldTable(self, oldTable: str):
        self.__oldTable = oldTable

    @property
    def condition(self) -> str:
        return self.__condition

    @condition.setter
    def condition(self, condition: str):
        self.__condition = condition

    @property
    def statementSQL(self) -> str:
        return self.__statementSQL

    @statementSQL.setter
    def statementSQL(self, statementSQL: str):
        self.__statementSQL = statementSQL

    @property
    def oldRow(self) -> str:
        return self.__oldRow

    @oldRow.setter
    def oldRow(self, oldRow: str):
        self.__oldRow = oldRow

    @property
    def actionGranularity(self) -> str:
        return self.__actionGranularity

    @actionGranularity.setter
    def actionGranularity(self, actionGranularity: str):
        self.__actionGranularity = actionGranularity

    @property
    def actionTime(self) -> str:
        return self.__actionTime

    @actionTime.setter
    def actionTime(self, actionTime: str):
        self.__actionTime = actionTime

    @property
    def newTable(self) -> str:
        return self.__newTable

    @newTable.setter
    def newTable(self, newTable: str):
        self.__newTable = newTable

    @property
    def deleteType(self) -> bool:
        return self.__deleteType

    @deleteType.setter
    def deleteType(self, deleteType: bool):
        self.__deleteType = deleteType

    @property
    def triggers13(self):
        return self.__triggers13

    @triggers13.setter
    def triggers13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_Trigger__triggers13", None)
        self.__triggers13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Table14"):
                opp_val = getattr(old_value, "Table14", None)
                if opp_val == self:
                    setattr(old_value, "Table14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Table14"):
                opp_val = getattr(value, "Table14", None)
                setattr(value, "Table14", self)

    @property
    def Trigger22(self):
        return self.__Trigger22

    @Trigger22.setter
    def Trigger22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_Trigger__Trigger22", None)
        self.__Trigger22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "triggerTables"):
                opp_val = getattr(old_value, "triggerTables", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "triggerTables"):
                opp_val = getattr(value, "triggerTables", None)
                if opp_val is None:
                    setattr(value, "triggerTables", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Trigger20(self):
        return self.__Trigger20

    @Trigger20.setter
    def Trigger20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_Trigger__Trigger20", None)
        self.__Trigger20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "table"):
                opp_val = getattr(old_value, "table", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "table"):
                opp_val = getattr(value, "table", None)
                if opp_val is None:
                    setattr(value, "table", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def triggersConstrainted(self):
        return self.__triggersConstrainted

    @triggersConstrainted.setter
    def triggersConstrainted(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_Trigger__triggersConstrainted", None)
        self.__triggersConstrainted = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Table16"):
                    opp_val = getattr(item, "Table16", None)
                    
                    if opp_val == self:
                        setattr(item, "Table16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Table16"):
                    opp_val = getattr(item, "Table16", None)
                    
                    setattr(item, "Table16", self)
                    

    @property
    def Trigger(self):
        return self.__Trigger

    @Trigger.setter
    def Trigger(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_Trigger__Trigger", None)
        self.__Trigger = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "schema6"):
                opp_val = getattr(old_value, "schema6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "schema6"):
                opp_val = getattr(value, "schema6", None)
                if opp_val is None:
                    setattr(value, "schema6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def triggers(self):
        return self.__triggers

    @triggers.setter
    def triggers(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_Trigger__triggers", None)
        self.__triggers = value
        
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

class relational_Schema(SQLObject):

    pass
class relational_Constraint(SQLObject):

    pass
class relational_DataType(SQLObject):

    pass
class relational_UserDefinedType(DataType):

    pass
class relational_Comment(ABC):

    def __init__(self, description: str, Comment: "relational_SQLObject" = None, comments: "relational_SQLObject" = None):
        self.description = description
        self.Comment = Comment
        self.comments = comments
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def comments(self):
        return self.__comments

    @comments.setter
    def comments(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_Comment__comments", None)
        self.__comments = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SQLObject"):
                opp_val = getattr(old_value, "SQLObject", None)
                if opp_val == self:
                    setattr(old_value, "SQLObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SQLObject"):
                opp_val = getattr(value, "SQLObject", None)
                setattr(value, "SQLObject", self)

    @property
    def Comment(self):
        return self.__Comment

    @Comment.setter
    def Comment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_Comment__Comment", None)
        self.__Comment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqlobject"):
                opp_val = getattr(old_value, "sqlobject", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqlobject"):
                opp_val = getattr(value, "sqlobject", None)
                if opp_val is None:
                    setattr(value, "sqlobject", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ENamedElement:

    pass
class relational_SQLObject(ENamedElement):

    def __init__(self, description: str, label: str, sqlobject: set["relational_Comment"] = None, SQLObject: "relational_Comment" = None):
        self.description = description
        self.label = label
        self.sqlobject = sqlobject if sqlobject is not None else set()
        self.SQLObject = SQLObject
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def sqlobject(self):
        return self.__sqlobject

    @sqlobject.setter
    def sqlobject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_SQLObject__sqlobject", None)
        self.__sqlobject = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Comment"):
                    opp_val = getattr(item, "Comment", None)
                    
                    if opp_val == self:
                        setattr(item, "Comment", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Comment"):
                    opp_val = getattr(item, "Comment", None)
                    
                    setattr(item, "Comment", self)
                    

    @property
    def SQLObject(self):
        return self.__SQLObject

    @SQLObject.setter
    def SQLObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_SQLObject__SQLObject", None)
        self.__SQLObject = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "comments"):
                opp_val = getattr(old_value, "comments", None)
                if opp_val == self:
                    setattr(old_value, "comments", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "comments"):
                opp_val = getattr(value, "comments", None)
                setattr(value, "comments", self)

class relational_ENamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name
