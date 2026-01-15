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


############################################
# Definition of Classes
############################################

class UniqueConstraint:

    pass
class relational_PrimaryKey(UniqueConstraint):

    pass
class ReferenceConstraint:

    pass
class relational_UniqueConstraint(ReferenceConstraint):

    pass
class TableConstraint:

    pass
class Constraint:

    pass
class relational_TableConstraint(Constraint):

    pass
class TypedElement:

    pass
class relational_Column(TypedElement):

    def __init__(self, length: int, nullable: bool, defaultValue: str, columns: "relational_Table" = None, members: set["relational_ReferenceConstraint"] = None, referencedMembers: set["relational_ForeignKey"] = None, Column: "relational_Table" = None, Column30: "relational_ReferenceConstraint" = None, Column36: "relational_ForeignKey" = None):
        self.length = length
        self.nullable = nullable
        self.defaultValue = defaultValue
        self.columns = columns
        self.members = members if members is not None else set()
        self.referencedMembers = referencedMembers if referencedMembers is not None else set()
        self.Column = Column
        self.Column30 = Column30
        self.Column36 = Column36
        
    @property
    def length(self) -> int:
        return self.__length

    @length.setter
    def length(self, length: int):
        self.__length = length

    @property
    def nullable(self) -> bool:
        return self.__nullable

    @nullable.setter
    def nullable(self, nullable: bool):
        self.__nullable = nullable

    @property
    def defaultValue(self) -> str:
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: str):
        self.__defaultValue = defaultValue

    @property
    def Column36(self):
        return self.__Column36

    @Column36.setter
    def Column36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_Column__Column36", None)
        self.__Column36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "foreignKey35"):
                opp_val = getattr(old_value, "foreignKey35", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "foreignKey35"):
                opp_val = getattr(value, "foreignKey35", None)
                if opp_val is None:
                    setattr(value, "foreignKey35", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Column30(self):
        return self.__Column30

    @Column30.setter
    def Column30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_Column__Column30", None)
        self.__Column30 = value
        
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
    def columns(self):
        return self.__columns

    @columns.setter
    def columns(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_Column__columns", None)
        self.__columns = value
        
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
            if hasattr(old_value, "table20"):
                opp_val = getattr(old_value, "table20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "table20"):
                opp_val = getattr(value, "table20", None)
                if opp_val is None:
                    setattr(value, "table20", set([self]))
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
                    

class Table:

    pass
class relational_BaseTable(Table):

    pass
class relational_ForeignKey(ReferenceConstraint):

    pass
class relational_ReferenceConstraint(TableConstraint):

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

class SQLObject:

    pass
class relational_Schema(SQLObject):

    pass
class relational_TypedElement(SQLObject):

    pass
class relational_Constraint(SQLObject):

    pass
class relational_Table(SQLObject):

    pass
class relational_Trigger(SQLObject):

    def __init__(self, updateType: bool, insertType: bool, deleteType: bool, actionTime: str, Trigger: "relational_Schema" = None, triggers9: "relational_Table" = None, triggersConstrainted: set["relational_Table"] = None, Trigger16: "relational_Table" = None, Trigger18: "relational_Table" = None, triggers: "relational_Schema" = None):
        self.updateType = updateType
        self.insertType = insertType
        self.deleteType = deleteType
        self.actionTime = actionTime
        self.Trigger = Trigger
        self.triggers9 = triggers9
        self.triggersConstrainted = triggersConstrainted if triggersConstrainted is not None else set()
        self.Trigger16 = Trigger16
        self.Trigger18 = Trigger18
        self.triggers = triggers
        
    @property
    def deleteType(self) -> bool:
        return self.__deleteType

    @deleteType.setter
    def deleteType(self, deleteType: bool):
        self.__deleteType = deleteType

    @property
    def actionTime(self) -> str:
        return self.__actionTime

    @actionTime.setter
    def actionTime(self, actionTime: str):
        self.__actionTime = actionTime

    @property
    def updateType(self) -> bool:
        return self.__updateType

    @updateType.setter
    def updateType(self, updateType: bool):
        self.__updateType = updateType

    @property
    def insertType(self) -> bool:
        return self.__insertType

    @insertType.setter
    def insertType(self, insertType: bool):
        self.__insertType = insertType

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

    @property
    def Trigger18(self):
        return self.__Trigger18

    @Trigger18.setter
    def Trigger18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_Trigger__Trigger18", None)
        self.__Trigger18 = value
        
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
    def triggers9(self):
        return self.__triggers9

    @triggers9.setter
    def triggers9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_Trigger__triggers9", None)
        self.__triggers9 = value
        
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
    def Trigger16(self):
        return self.__Trigger16

    @Trigger16.setter
    def Trigger16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_Trigger__Trigger16", None)
        self.__Trigger16 = value
        
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
                if hasattr(item, "Table12"):
                    opp_val = getattr(item, "Table12", None)
                    
                    if opp_val == self:
                        setattr(item, "Table12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Table12"):
                    opp_val = getattr(item, "Table12", None)
                    
                    setattr(item, "Table12", self)
                    

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

class relational_DataType(SQLObject):

    pass
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
                    

class relational_ENamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name
