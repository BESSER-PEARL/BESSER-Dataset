from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Property(Enum):
    NotNull = "NotNull"
    AutoIncrement = "AutoIncrement"
    Unique = "Unique"
class Action(Enum):
    Cascade = "Cascade"
    SetNull = "SetNull"
class Condition(Enum):
    Delete = "Delete"
    Update = "Update"


############################################
# Definition of Classes
############################################

class sql_Annotation:

    def __init__(self, annotation: str, Annotation: "sql_ModelElement" = None, ownedAnnotations: "sql_ModelElement" = None):
        self.annotation = annotation
        self.Annotation = Annotation
        self.ownedAnnotations = ownedAnnotations
        
        pass
    @property
    def annotation(self):
        return self.__annotation

    @annotation.setter
    def annotation(self, annotation: str):
        self.__annotation = annotation


    @property
    def ownedAnnotations(self):
        return self.__ownedAnnotations

    @ownedAnnotations.setter
    def ownedAnnotations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_Annotation__ownedAnnotations", None)
        self.__ownedAnnotations = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ModelElement"):
                opp_val = getattr(old_value, "ModelElement", None)
                if opp_val == self:
                    setattr(old_value, "ModelElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ModelElement"):
                opp_val = getattr(value, "ModelElement", None)
                setattr(value, "ModelElement", self)

    @property
    def Annotation(self):
        return self.__Annotation

    @Annotation.setter
    def Annotation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_Annotation__Annotation", None)
        self.__Annotation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owningModelElement"):
                opp_val = getattr(old_value, "owningModelElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owningModelElement"):
                opp_val = getattr(value, "owningModelElement", None)
                if opp_val is None:
                    setattr(value, "owningModelElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sql_ModelElement(ABC):

    pass
class NamedElement:

    pass
class sql_Table(NamedElement):

    pass
class Key:

    pass
class sql_Schema(NamedElement):

    pass
class sql_ForeignKey(Key):

    pass
class sql_PrimaryKey(Key):

    pass
class ModelElement:

    pass
class sql_Key(ModelElement):

    pass
class sql_Event(ModelElement):

    def __init__(self, condition: str, action: str, ownedEvents: "sql_ForeignKey" = None, Event: "sql_ForeignKey" = None):
        self.condition = condition
        self.action = action
        self.ownedEvents = ownedEvents
        self.Event = Event
        
        pass
    @property
    def condition(self):
        return self.__condition

    @condition.setter
    def condition(self, condition: str):
        self.__condition = condition


    @property
    def action(self):
        return self.__action

    @action.setter
    def action(self, action: str):
        self.__action = action


    @property
    def Event(self):
        return self.__Event

    @Event.setter
    def Event(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_Event__Event", None)
        self.__Event = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owningForeignKey"):
                opp_val = getattr(old_value, "owningForeignKey", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owningForeignKey"):
                opp_val = getattr(value, "owningForeignKey", None)
                if opp_val is None:
                    setattr(value, "owningForeignKey", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ownedEvents(self):
        return self.__ownedEvents

    @ownedEvents.setter
    def ownedEvents(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_Event__ownedEvents", None)
        self.__ownedEvents = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ForeignKey20"):
                opp_val = getattr(old_value, "ForeignKey20", None)
                if opp_val == self:
                    setattr(old_value, "ForeignKey20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ForeignKey20"):
                opp_val = getattr(value, "ForeignKey20", None)
                setattr(value, "ForeignKey20", self)

class sql_Column(ModelElement, NamedElement):

    def __init__(self, type: str, properties: str, ownedColumns: "sql_Table" = None, column: set["sql_Key"] = None, Column11: "sql_Key" = None, Column: "sql_Table" = None):
        self.type = type
        self.properties = properties
        self.ownedColumns = ownedColumns
        self.column = column if column is not None else set()
        self.Column11 = Column11
        self.Column = Column
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def properties(self):
        return self.__properties

    @properties.setter
    def properties(self, properties: str):
        self.__properties = properties


    @property
    def ownedColumns(self):
        return self.__ownedColumns

    @ownedColumns.setter
    def ownedColumns(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_Column__ownedColumns", None)
        self.__ownedColumns = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Table"):
                opp_val = getattr(old_value, "Table", None)
                if opp_val == self:
                    setattr(old_value, "Table", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Table"):
                opp_val = getattr(value, "Table", None)
                setattr(value, "Table", self)

    @property
    def column(self):
        return self.__column

    @column.setter
    def column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_Column__column", None)
        self.__column = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Key"):
                    opp_val = getattr(item, "Key", None)
                    
                    if opp_val == self:
                        setattr(item, "Key", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Key"):
                    opp_val = getattr(item, "Key", None)
                    
                    setattr(item, "Key", self)
                    

    @property
    def Column(self):
        return self.__Column

    @Column.setter
    def Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_Column__Column", None)
        self.__Column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owningTable"):
                opp_val = getattr(old_value, "owningTable", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owningTable"):
                opp_val = getattr(value, "owningTable", None)
                if opp_val is None:
                    setattr(value, "owningTable", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Column11(self):
        return self.__Column11

    @Column11.setter
    def Column11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_Column__Column11", None)
        self.__Column11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "keys"):
                opp_val = getattr(old_value, "keys", None)
                if opp_val == self:
                    setattr(old_value, "keys", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "keys"):
                opp_val = getattr(value, "keys", None)
                setattr(value, "keys", self)

class sql_NamedElement(ModelElement):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

