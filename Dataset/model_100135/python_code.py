from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class DataType(Enum):
    Integer = "Integer"
    Real = "Real"
    Char = "Char"
    String = "String"
    Date = "Date"
    DateTime = "DateTime"
    Time = "Time"
    Blob = "Blob"
    GUID = "GUID"
    Bool = "Bool"
class RelationshipType(Enum):
    OneToOne = "OneToOne"
    OneToMany = "OneToMany"
    ManyToOne = "ManyToOne"
    ManyToMany = "ManyToMany"
class EntityFormType(Enum):
    Select = "Select"
    Insert = "Insert"
    Update = "Update"
    Delete = "Delete"


############################################
# Definition of Classes
############################################

class Attribute:

    pass
class Form:

    pass
class dbca_CustomForm(Form):

    pass
class dbca_EntityContainmentForm(Form):

    pass
class dbca_EntityForm(Form):

    def __init__(self, type: str, dbca_EntityForm: "dbca_Entity" = None):
        self.type = type
        self.dbca_EntityForm = dbca_EntityForm
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def dbca_EntityForm(self):
        return self.__dbca_EntityForm

    @dbca_EntityForm.setter
    def dbca_EntityForm(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbca_EntityForm__dbca_EntityForm", None)
        self.__dbca_EntityForm = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbca_Entity35"):
                opp_val = getattr(old_value, "dbca_Entity35", None)
                if opp_val == self:
                    setattr(old_value, "dbca_Entity35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbca_Entity35"):
                opp_val = getattr(value, "dbca_Entity35", None)
                setattr(value, "dbca_Entity35", self)

class ClientElement:

    pass
class dbca_Form(ClientElement):

    pass
class Service:

    pass
class dbca_QueryService(Service):

    pass
class dbca_CustomService(Service):

    pass
class dbca_OperationService(Service):

    pass
class dbca_EntityService(Service):

    pass
class Parameter:

    pass
class dbca_EntityParameter(Parameter):

    pass
class dbca_DataParameter(Parameter):

    def __init__(self, type: str, dbca_DataParameter: "dbca_Function" = None):
        self.type = type
        self.dbca_DataParameter = dbca_DataParameter
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def dbca_DataParameter(self):
        return self.__dbca_DataParameter

    @dbca_DataParameter.setter
    def dbca_DataParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbca_DataParameter__dbca_DataParameter", None)
        self.__dbca_DataParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbca_Function"):
                opp_val = getattr(old_value, "dbca_Function", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbca_Function"):
                opp_val = getattr(value, "dbca_Function", None)
                if opp_val is None:
                    setattr(value, "dbca_Function", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Entity:

    pass
class dbca_ComputedEntity(Entity):

    pass
class dbca_PersistentEntity(Entity):

    pass
class dbca_AbstractEntity(Entity):

    pass
class ServerElement:

    pass
class dbca_Service(ServerElement):

    pass
class NamedElement:

    pass
class dbca_Database(NamedElement):

    pass
class dbca_Server(NamedElement):

    pass
class dbca_ClientElement(NamedElement):

    pass
class dbca_Client(NamedElement):

    pass
class dbca_Attribute(NamedElement):

    def __init__(self, type: str, maxLength: int):
        self.type = type
        self.maxLength = maxLength
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def maxLength(self):
        return self.__maxLength

    @maxLength.setter
    def maxLength(self, maxLength: int):
        self.__maxLength = maxLength


class dbca_ServerElement(NamedElement):

    pass
class dbca_Parameter(NamedElement):

    pass
class dbca_Relationship(NamedElement):

    def __init__(self, type: str, isNullable: bool, isContainment: str, dbca_Relationship: "dbca_Entity" = None, dbca_Relationship16: "dbca_Entity" = None, dbca_Relationship19: set["dbca_Property"] = None):
        self.type = type
        self.isNullable = isNullable
        self.isContainment = isContainment
        self.dbca_Relationship = dbca_Relationship
        self.dbca_Relationship16 = dbca_Relationship16
        self.dbca_Relationship19 = dbca_Relationship19 if dbca_Relationship19 is not None else set()
        
        pass
    @property
    def isNullable(self):
        return self.__isNullable

    @isNullable.setter
    def isNullable(self, isNullable: bool):
        self.__isNullable = isNullable


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def isContainment(self):
        return self.__isContainment

    @isContainment.setter
    def isContainment(self, isContainment: str):
        self.__isContainment = isContainment


    @property
    def dbca_Relationship16(self):
        return self.__dbca_Relationship16

    @dbca_Relationship16.setter
    def dbca_Relationship16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbca_Relationship__dbca_Relationship16", None)
        self.__dbca_Relationship16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbca_Entity17"):
                opp_val = getattr(old_value, "dbca_Entity17", None)
                if opp_val == self:
                    setattr(old_value, "dbca_Entity17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbca_Entity17"):
                opp_val = getattr(value, "dbca_Entity17", None)
                setattr(value, "dbca_Entity17", self)

    @property
    def dbca_Relationship(self):
        return self.__dbca_Relationship

    @dbca_Relationship.setter
    def dbca_Relationship(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbca_Relationship__dbca_Relationship", None)
        self.__dbca_Relationship = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbca_Entity11"):
                opp_val = getattr(old_value, "dbca_Entity11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbca_Entity11"):
                opp_val = getattr(value, "dbca_Entity11", None)
                if opp_val is None:
                    setattr(value, "dbca_Entity11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dbca_Relationship19(self):
        return self.__dbca_Relationship19

    @dbca_Relationship19.setter
    def dbca_Relationship19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbca_Relationship__dbca_Relationship19", None)
        self.__dbca_Relationship19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dbca_Property20"):
                    opp_val = getattr(item, "dbca_Property20", None)
                    
                    if opp_val == self:
                        setattr(item, "dbca_Property20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dbca_Property20"):
                    opp_val = getattr(item, "dbca_Property20", None)
                    
                    setattr(item, "dbca_Property20", self)
                    

class dbca_DatabaseElement(NamedElement):

    pass
class dbca_Application(NamedElement):

    pass
class CommentedElement:

    pass
class dbca_NamedElement(CommentedElement):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class Element:

    pass
class dbca_CommentedElement(Element):

    def __init__(self, comment: str):
        self.comment = comment
        
        pass
    @property
    def comment(self):
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment


class dbca_Element(ABC):

    pass
class dbca_Property(Attribute):

    def __init__(self, isNullable: bool, defaultValue: str, dbca_Property: "dbca_Entity" = None, dbca_Property20: "dbca_Relationship" = None):
        self.isNullable = isNullable
        self.defaultValue = defaultValue
        self.dbca_Property = dbca_Property
        self.dbca_Property20 = dbca_Property20
        
        pass
    @property
    def isNullable(self):
        return self.__isNullable

    @isNullable.setter
    def isNullable(self, isNullable: bool):
        self.__isNullable = isNullable


    @property
    def defaultValue(self):
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: str):
        self.__defaultValue = defaultValue


    @property
    def dbca_Property(self):
        return self.__dbca_Property

    @dbca_Property.setter
    def dbca_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbca_Property__dbca_Property", None)
        self.__dbca_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbca_Entity9"):
                opp_val = getattr(old_value, "dbca_Entity9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbca_Entity9"):
                opp_val = getattr(value, "dbca_Entity9", None)
                if opp_val is None:
                    setattr(value, "dbca_Entity9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dbca_Property20(self):
        return self.__dbca_Property20

    @dbca_Property20.setter
    def dbca_Property20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbca_Property__dbca_Property20", None)
        self.__dbca_Property20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbca_Relationship19"):
                opp_val = getattr(old_value, "dbca_Relationship19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbca_Relationship19"):
                opp_val = getattr(value, "dbca_Relationship19", None)
                if opp_val is None:
                    setattr(value, "dbca_Relationship19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dbca_PrimaryProperty(Attribute):

    pass
class DatabaseElement:

    pass
class dbca_Query(DatabaseElement):

    pass
class dbca_Operation(DatabaseElement):

    pass
class dbca_Event(DatabaseElement):

    pass
class dbca_Function(DatabaseElement):

    def __init__(self, returnType: str, dbca_Function: set["dbca_DataParameter"] = None):
        self.returnType = returnType
        self.dbca_Function = dbca_Function if dbca_Function is not None else set()
        
        pass
    @property
    def returnType(self):
        return self.__returnType

    @returnType.setter
    def returnType(self, returnType: str):
        self.__returnType = returnType


    @property
    def dbca_Function(self):
        return self.__dbca_Function

    @dbca_Function.setter
    def dbca_Function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbca_Function__dbca_Function", None)
        self.__dbca_Function = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dbca_DataParameter"):
                    opp_val = getattr(item, "dbca_DataParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "dbca_DataParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dbca_DataParameter"):
                    opp_val = getattr(item, "dbca_DataParameter", None)
                    
                    setattr(item, "dbca_DataParameter", self)
                    

class dbca_Entity(DatabaseElement):

    pass