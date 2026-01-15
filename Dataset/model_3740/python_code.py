from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Type(Enum):
    int = "int"
    bigInt = "bigInt"
    boolean = "boolean"
    byteArray = "byteArray"
    date = "date"
    double = "double"
    varchar = "varchar"
    undefined = "undefined"


############################################
# Definition of Classes
############################################

class Constraint:

    pass
class genericsql_Unique(Constraint):

    pass
class genericsql_Check(Constraint):

    def __init__(self, expression: str):
        self.expression = expression
        
    @property
    def expression(self) -> str:
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression

class genericsql_Constraint(ABC):

    pass
class genericsql_NamedElement(ABC):

    def __init__(self, name: str, comment: str):
        self.name = name
        self.comment = comment
        
    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class NamedElement:

    pass
class genericsql_Field(NamedElement):

    def __init__(self, size: int, defaultValue: str, specificType: str, notNull: bool, unique: bool, type: str, autoIcrement: bool, genericsql_Field: "genericsql_PrimaryKey" = None, genericsql_Field12: "genericsql_ForeignKey" = None, Field: "genericsql_Table" = None, fields: "genericsql_Table" = None, genericsql_Field22: "genericsql_Constraint" = None):
        self.size = size
        self.defaultValue = defaultValue
        self.specificType = specificType
        self.notNull = notNull
        self.unique = unique
        self.type = type
        self.autoIcrement = autoIcrement
        self.genericsql_Field = genericsql_Field
        self.genericsql_Field12 = genericsql_Field12
        self.Field = Field
        self.fields = fields
        self.genericsql_Field22 = genericsql_Field22
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def unique(self) -> bool:
        return self.__unique

    @unique.setter
    def unique(self, unique: bool):
        self.__unique = unique

    @property
    def notNull(self) -> bool:
        return self.__notNull

    @notNull.setter
    def notNull(self, notNull: bool):
        self.__notNull = notNull

    @property
    def specificType(self) -> str:
        return self.__specificType

    @specificType.setter
    def specificType(self, specificType: str):
        self.__specificType = specificType

    @property
    def defaultValue(self) -> str:
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: str):
        self.__defaultValue = defaultValue

    @property
    def autoIcrement(self) -> bool:
        return self.__autoIcrement

    @autoIcrement.setter
    def autoIcrement(self, autoIcrement: bool):
        self.__autoIcrement = autoIcrement

    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, size: int):
        self.__size = size

    @property
    def Field(self):
        return self.__Field

    @Field.setter
    def Field(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_genericsql_Field__Field", None)
        self.__Field = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "table5"):
                opp_val = getattr(old_value, "table5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "table5"):
                opp_val = getattr(value, "table5", None)
                if opp_val is None:
                    setattr(value, "table5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def genericsql_Field(self):
        return self.__genericsql_Field

    @genericsql_Field.setter
    def genericsql_Field(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_genericsql_Field__genericsql_Field", None)
        self.__genericsql_Field = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "genericsql_PrimaryKey"):
                opp_val = getattr(old_value, "genericsql_PrimaryKey", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "genericsql_PrimaryKey"):
                opp_val = getattr(value, "genericsql_PrimaryKey", None)
                if opp_val is None:
                    setattr(value, "genericsql_PrimaryKey", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def genericsql_Field12(self):
        return self.__genericsql_Field12

    @genericsql_Field12.setter
    def genericsql_Field12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_genericsql_Field__genericsql_Field12", None)
        self.__genericsql_Field12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "genericsql_ForeignKey"):
                opp_val = getattr(old_value, "genericsql_ForeignKey", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "genericsql_ForeignKey"):
                opp_val = getattr(value, "genericsql_ForeignKey", None)
                if opp_val is None:
                    setattr(value, "genericsql_ForeignKey", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def genericsql_Field22(self):
        return self.__genericsql_Field22

    @genericsql_Field22.setter
    def genericsql_Field22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_genericsql_Field__genericsql_Field22", None)
        self.__genericsql_Field22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "genericsql_Constraint21"):
                opp_val = getattr(old_value, "genericsql_Constraint21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "genericsql_Constraint21"):
                opp_val = getattr(value, "genericsql_Constraint21", None)
                if opp_val is None:
                    setattr(value, "genericsql_Constraint21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fields(self):
        return self.__fields

    @fields.setter
    def fields(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_genericsql_Field__fields", None)
        self.__fields = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Table19"):
                opp_val = getattr(old_value, "Table19", None)
                if opp_val == self:
                    setattr(old_value, "Table19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Table19"):
                opp_val = getattr(value, "Table19", None)
                setattr(value, "Table19", self)

class genericsql_PrimaryKey(NamedElement):

    pass
class genericsql_Table(NamedElement):

    pass
class genericsql_ForeignKey(NamedElement):

    pass
class genericsql_DataBase(NamedElement):

    pass