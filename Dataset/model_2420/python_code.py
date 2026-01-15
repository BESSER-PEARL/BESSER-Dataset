from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class PrimitiveTypeCodes(Enum):
    ARRAY = "ARRAY"
    BIGINT = "BIGINT"
    BINARY = "BINARY"
    BIT = "BIT"
    BLOB = "BLOB"
    BOOLEAN = "BOOLEAN"
    DISTINCT = "DISTINCT"
    DOUBLE = "DOUBLE"
    FLOAT = "FLOAT"
    INTEGER = "INTEGER"
    JAVA_OBJECT = "JAVA_OBJECT"
    LONGNVARCHAR = "LONGNVARCHAR"
    LONGVARBINARY = "LONGVARBINARY"
    LONGVARCHAR = "LONGVARCHAR"
    NCHAR = "NCHAR"
    CHAR = "CHAR"
    CLOB = "CLOB"
    DATALINK = "DATALINK"
    DATE = "DATE"
    DECIMAL = "DECIMAL"
    REAL = "REAL"
    REF = "REF"
    ROWID = "ROWID"
    SMALLINT = "SMALLINT"
    SQLXML = "SQLXML"
    STRUCT = "STRUCT"
    TIME = "TIME"
    TIMESTAMP = "TIMESTAMP"
    TINYINT = "TINYINT"
    NCLOB = "NCLOB"
    NULL = "NULL"
    NUMERIC = "NUMERIC"
    NVARCHAR = "NVARCHAR"
    OTHER = "OTHER"
    VARBINARY = "VARBINARY"
    VARCHAR = "VARCHAR"


############################################
# Definition of Classes
############################################

class view_rdbmdl_NamedColumnSet:

    pass
class view_rdbmdl_Column:

    pass
class ViewAlias:

    pass
class ViewColumn:

    pass
class rdbmdl_view_ReferencedViewColumn(ViewColumn):

    pass
class rdbmdl_view_ViewExpressionColumn(ViewColumn):

    def __init__(self, expression: str, ViewColumn: "rdbmdl_view_View"):
        self.expression = expression
        
    @property
    def expression(self) -> str:
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression

class DataType:

    pass
class rdbmdl_datatypes_PrimitiveDataType(DataType):

    def __init__(self, type: str):
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class datatypes_PrimitiveDataType:

    pass
class constraints_rdbmdl_TableColumn:

    pass
class Constraint:

    pass
class rdbmdl_constraints_ColumnRefConstraint(Constraint):

    pass
class rdbmdl_constraints_CheckConstraint(Constraint):

    def __init__(self, expression: str):
        self.expression = expression
        
    @property
    def expression(self) -> str:
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression

class IndexedColumn:

    pass
class rdbmdl_constraints_Index(Constraint):

    pass
class ColumnRefConstraint:

    pass
class rdbmdl_constraints_ForeignKey(ColumnRefConstraint):

    pass
class rdbmdl_constraints_UniqueConstraint(ColumnRefConstraint):

    pass
class ForeignKey:

    pass
class UniqueConstraint:

    pass
class rdbmdl_constraints_PrimaryKey(UniqueConstraint):

    pass
class PrimitiveDataType:

    pass
class Domain:

    pass
class Column:

    pass
class rdbmdl_view_ViewColumn(Column):

    pass
class CheckConstraint:

    pass
class Index:

    pass
class NamedElement:

    pass
class rdbmdl_Column(NamedElement):

    pass
class rdbmdl_Schema(NamedElement):

    pass
class rdbmdl_constraints_Constraint(NamedElement):

    pass
class rdbmdl_view_ViewAlias(NamedElement):

    pass
class rdbmdl_datatypes_DataType(NamedElement):

    def __init__(self, size: int, decimalDigits: int, nullable: bool, default: str, check: str, var: str):
        self.size = size
        self.decimalDigits = decimalDigits
        self.nullable = nullable
        self.default = default
        self.check = check
        self.var = var
        
    @property
    def decimalDigits(self) -> int:
        return self.__decimalDigits

    @decimalDigits.setter
    def decimalDigits(self, decimalDigits: int):
        self.__decimalDigits = decimalDigits

    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, size: int):
        self.__size = size

    @property
    def default(self) -> str:
        return self.__default

    @default.setter
    def default(self, default: str):
        self.__default = default

    @property
    def check(self) -> str:
        return self.__check

    @check.setter
    def check(self, check: str):
        self.__check = check

    @property
    def nullable(self) -> bool:
        return self.__nullable

    @nullable.setter
    def nullable(self, nullable: bool):
        self.__nullable = nullable

    @property
    def var(self) -> str:
        return self.__var

    @var.setter
    def var(self, var: str):
        self.__var = var

class rdbmdl_constraints_IndexedColumn(NamedElement):

    def __init__(self, ascending: bool, rdbmdl_constraints_IndexedColumn: "constraints_rdbmdl_TableColumn" = None):
        self.ascending = ascending
        self.rdbmdl_constraints_IndexedColumn = rdbmdl_constraints_IndexedColumn
        
    @property
    def ascending(self) -> bool:
        return self.__ascending

    @ascending.setter
    def ascending(self, ascending: bool):
        self.__ascending = ascending

    @property
    def rdbmdl_constraints_IndexedColumn(self):
        return self.__rdbmdl_constraints_IndexedColumn

    @rdbmdl_constraints_IndexedColumn.setter
    def rdbmdl_constraints_IndexedColumn(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbmdl_constraints_IndexedColumn__rdbmdl_constraints_IndexedColumn", None)
        self.__rdbmdl_constraints_IndexedColumn = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "constraints_rdbmdl_TableColumn25"):
                opp_val = getattr(old_value, "constraints_rdbmdl_TableColumn25", None)
                if opp_val == self:
                    setattr(old_value, "constraints_rdbmdl_TableColumn25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "constraints_rdbmdl_TableColumn25"):
                opp_val = getattr(value, "constraints_rdbmdl_TableColumn25", None)
                setattr(value, "constraints_rdbmdl_TableColumn25", self)

class rdbmdl_Model(NamedElement):

    def __init__(self, server_id: str, rdbmdl_Model: set["rdbmdl_Schema"] = None):
        self.server_id = server_id
        self.rdbmdl_Model = rdbmdl_Model if rdbmdl_Model is not None else set()
        
    @property
    def server_id(self) -> str:
        return self.__server_id

    @server_id.setter
    def server_id(self, server_id: str):
        self.__server_id = server_id

    @property
    def rdbmdl_Model(self):
        return self.__rdbmdl_Model

    @rdbmdl_Model.setter
    def rdbmdl_Model(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbmdl_Model__rdbmdl_Model", None)
        self.__rdbmdl_Model = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rdbmdl_Schema"):
                    opp_val = getattr(item, "rdbmdl_Schema", None)
                    
                    if opp_val == self:
                        setattr(item, "rdbmdl_Schema", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rdbmdl_Schema"):
                    opp_val = getattr(item, "rdbmdl_Schema", None)
                    
                    setattr(item, "rdbmdl_Schema", self)
                    

class PrimaryKey:

    pass
class rdbmdl_TableColumn(Column):

    def __init__(self, isPrimaryKey: str, isForeignKey: str, rdbmdl_TableColumn: "rdbmdl_Table" = None, rdbmdl_TableColumn17: "Domain" = None, rdbmdl_TableColumn19: "PrimitiveDataType" = None):
        self.isPrimaryKey = isPrimaryKey
        self.isForeignKey = isForeignKey
        self.rdbmdl_TableColumn = rdbmdl_TableColumn
        self.rdbmdl_TableColumn17 = rdbmdl_TableColumn17
        self.rdbmdl_TableColumn19 = rdbmdl_TableColumn19
        
    @property
    def isPrimaryKey(self) -> str:
        return self.__isPrimaryKey

    @isPrimaryKey.setter
    def isPrimaryKey(self, isPrimaryKey: str):
        self.__isPrimaryKey = isPrimaryKey

    @property
    def isForeignKey(self) -> str:
        return self.__isForeignKey

    @isForeignKey.setter
    def isForeignKey(self, isForeignKey: str):
        self.__isForeignKey = isForeignKey

    @property
    def rdbmdl_TableColumn17(self):
        return self.__rdbmdl_TableColumn17

    @rdbmdl_TableColumn17.setter
    def rdbmdl_TableColumn17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbmdl_TableColumn__rdbmdl_TableColumn17", None)
        self.__rdbmdl_TableColumn17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Domain"):
                opp_val = getattr(old_value, "Domain", None)
                if opp_val == self:
                    setattr(old_value, "Domain", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Domain"):
                opp_val = getattr(value, "Domain", None)
                setattr(value, "Domain", self)

    @property
    def rdbmdl_TableColumn19(self):
        return self.__rdbmdl_TableColumn19

    @rdbmdl_TableColumn19.setter
    def rdbmdl_TableColumn19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbmdl_TableColumn__rdbmdl_TableColumn19", None)
        self.__rdbmdl_TableColumn19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PrimitiveDataType"):
                opp_val = getattr(old_value, "PrimitiveDataType", None)
                if opp_val == self:
                    setattr(old_value, "PrimitiveDataType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PrimitiveDataType"):
                opp_val = getattr(value, "PrimitiveDataType", None)
                setattr(value, "PrimitiveDataType", self)

    @property
    def rdbmdl_TableColumn(self):
        return self.__rdbmdl_TableColumn

    @rdbmdl_TableColumn.setter
    def rdbmdl_TableColumn(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbmdl_TableColumn__rdbmdl_TableColumn", None)
        self.__rdbmdl_TableColumn = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbmdl_Table"):
                opp_val = getattr(old_value, "rdbmdl_Table", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbmdl_Table"):
                opp_val = getattr(value, "rdbmdl_Table", None)
                if opp_val is None:
                    setattr(value, "rdbmdl_Table", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class NamedColumnSet:

    pass
class rdbmdl_view_View(NamedColumnSet):

    def __init__(self, ddl: str, rdbmdl_view_View: set["ViewColumn"] = None, rdbmdl_view_View30: set["ViewAlias"] = None):
        self.ddl = ddl
        self.rdbmdl_view_View = rdbmdl_view_View if rdbmdl_view_View is not None else set()
        self.rdbmdl_view_View30 = rdbmdl_view_View30 if rdbmdl_view_View30 is not None else set()
        
    @property
    def ddl(self) -> str:
        return self.__ddl

    @ddl.setter
    def ddl(self, ddl: str):
        self.__ddl = ddl

    @property
    def rdbmdl_view_View(self):
        return self.__rdbmdl_view_View

    @rdbmdl_view_View.setter
    def rdbmdl_view_View(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbmdl_view_View__rdbmdl_view_View", None)
        self.__rdbmdl_view_View = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ViewColumn"):
                    opp_val = getattr(item, "ViewColumn", None)
                    
                    if opp_val == self:
                        setattr(item, "ViewColumn", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ViewColumn"):
                    opp_val = getattr(item, "ViewColumn", None)
                    
                    setattr(item, "ViewColumn", self)
                    

    @property
    def rdbmdl_view_View30(self):
        return self.__rdbmdl_view_View30

    @rdbmdl_view_View30.setter
    def rdbmdl_view_View30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbmdl_view_View__rdbmdl_view_View30", None)
        self.__rdbmdl_view_View30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ViewAlias"):
                    opp_val = getattr(item, "ViewAlias", None)
                    
                    if opp_val == self:
                        setattr(item, "ViewAlias", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ViewAlias"):
                    opp_val = getattr(item, "ViewAlias", None)
                    
                    setattr(item, "ViewAlias", self)
                    

class rdbmdl_Table(NamedColumnSet):

    pass
class rdbmdl_SchemaElement(NamedElement):

    def __init__(self, owner: str, rdbmdl_SchemaElement: "rdbmdl_Schema" = None):
        self.owner = owner
        self.rdbmdl_SchemaElement = rdbmdl_SchemaElement
        
    @property
    def owner(self) -> str:
        return self.__owner

    @owner.setter
    def owner(self, owner: str):
        self.__owner = owner

    @property
    def rdbmdl_SchemaElement(self):
        return self.__rdbmdl_SchemaElement

    @rdbmdl_SchemaElement.setter
    def rdbmdl_SchemaElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbmdl_SchemaElement__rdbmdl_SchemaElement", None)
        self.__rdbmdl_SchemaElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbmdl_Schema4"):
                opp_val = getattr(old_value, "rdbmdl_Schema4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbmdl_Schema4"):
                opp_val = getattr(value, "rdbmdl_Schema4", None)
                if opp_val is None:
                    setattr(value, "rdbmdl_Schema4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Element:

    pass
class rdbmdl_NamedElement(Element):

    def __init__(self, uid: str, name: str):
        self.uid = uid
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

class SchemaElement:

    pass
class rdbmdl_datatypes_Domain(SchemaElement, datatypes_PrimitiveDataType):

    pass
class rdbmdl_NamedColumnSet(SchemaElement):

    pass
class rdbmdl_Element:

    pass