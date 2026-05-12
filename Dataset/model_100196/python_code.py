from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class SQLDDL_LocatedElement(ABC):

    def __init__(self, location: str, commentsBefore: str, commentsAfter: str):
        self.location = location
        self.commentsBefore = commentsBefore
        self.commentsAfter = commentsAfter
        
        pass
    @property
    def commentsAfter(self):
        return self.__commentsAfter

    @commentsAfter.setter
    def commentsAfter(self, commentsAfter: str):
        self.__commentsAfter = commentsAfter


    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location


    @property
    def commentsBefore(self):
        return self.__commentsBefore

    @commentsBefore.setter
    def commentsBefore(self, commentsBefore: str):
        self.__commentsBefore = commentsBefore


class Database:

    pass
class Table:

    pass
class NamedElement:

    pass
class SQLDDL_Table(NamedElement):

    pass
class SQLDDL_Database(NamedElement):

    pass
class SQLDDL_Type(NamedElement):

    def __init__(self, length: str, isUnsigned: str):
        self.length = length
        self.isUnsigned = isUnsigned
        
        pass
    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length: str):
        self.__length = length


    @property
    def isUnsigned(self):
        return self.__isUnsigned

    @isUnsigned.setter
    def isUnsigned(self, isUnsigned: str):
        self.__isUnsigned = isUnsigned


class SQLDDL_Parameter(NamedElement):

    pass
class Key:

    pass
class Value:

    pass
class SQLDDL_NullVal(Value):

    pass
class SQLDDL_StringVal(Value):

    def __init__(self, value: str, Value: "SQLDDL_Column" = None, Value23: "SQLDDL_Parameter" = None):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class SQLDDL_IntegerVal(Value):

    def __init__(self, value: str, Value: "SQLDDL_Column" = None, Value23: "SQLDDL_Parameter" = None):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class SQLDDL_ForeignKey(Key):

    pass
class SQLDDL_PrimaryKey(Key):

    pass
class SQLDDL_SimpleKey(Key):

    pass
class Column:

    pass
class Parameter:

    pass
class TableElement:

    pass
class SQLDDL_Key(TableElement):

    def __init__(self, isUnique: str, name: str, keys: set["Column"] = None, TableElement: "SQLDDL_Table" = None):
        self.isUnique = isUnique
        self.name = name
        self.keys = keys if keys is not None else set()
        
        pass
    @property
    def isUnique(self):
        return self.__isUnique

    @isUnique.setter
    def isUnique(self, isUnique: str):
        self.__isUnique = isUnique


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def keys(self):
        return self.__keys

    @keys.setter
    def keys(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQLDDL_Key__keys", None)
        self.__keys = value if value is not None else set()
        
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
                    

class ForeignKey:

    pass
class Type:

    pass
class SQLDDL_Column(TableElement):

    def __init__(self, name: str, canBeNull: str, referencedColumns: set["ForeignKey"] = None, SQLDDL_Column: "Type" = None, SQLDDL_Column12: "Value" = None, columns: set["Key"] = None, TableElement: "SQLDDL_Table" = None):
        self.name = name
        self.canBeNull = canBeNull
        self.referencedColumns = referencedColumns if referencedColumns is not None else set()
        self.SQLDDL_Column = SQLDDL_Column
        self.SQLDDL_Column12 = SQLDDL_Column12
        self.columns = columns if columns is not None else set()
        
        pass
    @property
    def canBeNull(self):
        return self.__canBeNull

    @canBeNull.setter
    def canBeNull(self, canBeNull: str):
        self.__canBeNull = canBeNull


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def columns(self):
        return self.__columns

    @columns.setter
    def columns(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQLDDL_Column__columns", None)
        self.__columns = value if value is not None else set()
        
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
    def SQLDDL_Column(self):
        return self.__SQLDDL_Column

    @SQLDDL_Column.setter
    def SQLDDL_Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQLDDL_Column__SQLDDL_Column", None)
        self.__SQLDDL_Column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Type"):
                opp_val = getattr(old_value, "Type", None)
                if opp_val == self:
                    setattr(old_value, "Type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Type"):
                opp_val = getattr(value, "Type", None)
                setattr(value, "Type", self)

    @property
    def referencedColumns(self):
        return self.__referencedColumns

    @referencedColumns.setter
    def referencedColumns(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQLDDL_Column__referencedColumns", None)
        self.__referencedColumns = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ForeignKey9"):
                    opp_val = getattr(item, "ForeignKey9", None)
                    
                    if opp_val == self:
                        setattr(item, "ForeignKey9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ForeignKey9"):
                    opp_val = getattr(item, "ForeignKey9", None)
                    
                    setattr(item, "ForeignKey9", self)
                    

    @property
    def SQLDDL_Column12(self):
        return self.__SQLDDL_Column12

    @SQLDDL_Column12.setter
    def SQLDDL_Column12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQLDDL_Column__SQLDDL_Column12", None)
        self.__SQLDDL_Column12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Value"):
                opp_val = getattr(old_value, "Value", None)
                if opp_val == self:
                    setattr(old_value, "Value", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Value"):
                opp_val = getattr(value, "Value", None)
                setattr(value, "Value", self)

class LocatedElement:

    pass
class SQLDDL_Value(LocatedElement):

    pass
class SQLDDL_NamedElement(LocatedElement):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class SQLDDL_TableElement(LocatedElement):

    pass