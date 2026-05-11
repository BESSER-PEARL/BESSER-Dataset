from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class view_rdb_NamedColumnSet:

    pass
class ViewAlias:

    pass
class view_rdb_Column:

    pass
class constraints_rdb_TableColumn:

    pass
class Constraint:

    pass
class rdb_constraints_ColumnRefConstraint(Constraint):

    pass
class rdb_constraints_CheckConstraint(Constraint):

    def __init__(self, expression: str):
        self.expression = expression
        
        pass
    @property
    def expression(self):
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression


class PrimitiveDataType:

    pass
class ViewColumn:

    pass
class rdb_view_ReferencedViewColumn(ViewColumn):

    pass
class rdb_view_ViewExpressionColumn(ViewColumn):

    def __init__(self, expression: str, ViewColumn: "rdb_view_View" = None):
        self.expression = expression
        
        pass
    @property
    def expression(self):
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression


class DataType:

    pass
class rdb_datatypes_PrimitiveDataType(DataType):

    def __init__(self, type: str):
        self.type = type
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


class datatypes_PrimitiveDataType:

    pass
class IndexedColumn:

    pass
class rdb_constraints_Index(Constraint):

    pass
class ColumnRefConstraint:

    pass
class rdb_constraints_ForeignKey(ColumnRefConstraint):

    pass
class rdb_constraints_UniqueConstraint(ColumnRefConstraint):

    pass
class Element:

    pass
class rdb_NamedElement(Element):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class SchemaElement:

    pass
class rdb_datatypes_Domain(SchemaElement, datatypes_PrimitiveDataType):

    pass
class rdb_NamedColumnSet(SchemaElement):

    pass
class rdb_Element:

    pass
class Domain:

    pass
class Column:

    pass
class rdb_view_ViewColumn(Column):

    pass
class CheckConstraint:

    pass
class Index:

    pass
class ForeignKey:

    pass
class UniqueConstraint:

    pass
class rdb_constraints_PrimaryKey(UniqueConstraint):

    pass
class PrimaryKey:

    pass
class rdb_TableColumn(Column):

    def __init__(self, isPrimaryKey: str, isForeignKey: str, rdb_TableColumn: "rdb_Table" = None, rdb_TableColumn17: "Domain" = None, rdb_TableColumn19: "PrimitiveDataType" = None):
        self.isPrimaryKey = isPrimaryKey
        self.isForeignKey = isForeignKey
        self.rdb_TableColumn = rdb_TableColumn
        self.rdb_TableColumn17 = rdb_TableColumn17
        self.rdb_TableColumn19 = rdb_TableColumn19
        
        pass
    @property
    def isPrimaryKey(self):
        return self.__isPrimaryKey

    @isPrimaryKey.setter
    def isPrimaryKey(self, isPrimaryKey: str):
        self.__isPrimaryKey = isPrimaryKey


    @property
    def isForeignKey(self):
        return self.__isForeignKey

    @isForeignKey.setter
    def isForeignKey(self, isForeignKey: str):
        self.__isForeignKey = isForeignKey


    @property
    def rdb_TableColumn19(self):
        return self.__rdb_TableColumn19

    @rdb_TableColumn19.setter
    def rdb_TableColumn19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdb_TableColumn__rdb_TableColumn19", None)
        self.__rdb_TableColumn19 = value
        
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
    def rdb_TableColumn17(self):
        return self.__rdb_TableColumn17

    @rdb_TableColumn17.setter
    def rdb_TableColumn17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdb_TableColumn__rdb_TableColumn17", None)
        self.__rdb_TableColumn17 = value
        
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
    def rdb_TableColumn(self):
        return self.__rdb_TableColumn

    @rdb_TableColumn.setter
    def rdb_TableColumn(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdb_TableColumn__rdb_TableColumn", None)
        self.__rdb_TableColumn = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdb_Table"):
                opp_val = getattr(old_value, "rdb_Table", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdb_Table"):
                opp_val = getattr(value, "rdb_Table", None)
                if opp_val is None:
                    setattr(value, "rdb_Table", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class NamedColumnSet:

    pass
class rdb_view_View(NamedColumnSet):

    def __init__(self, ddl: str, rdb_view_View: set["ViewColumn"] = None, rdb_view_View30: set["ViewAlias"] = None):
        self.ddl = ddl
        self.rdb_view_View = rdb_view_View if rdb_view_View is not None else set()
        self.rdb_view_View30 = rdb_view_View30 if rdb_view_View30 is not None else set()
        
        pass
    @property
    def ddl(self):
        return self.__ddl

    @ddl.setter
    def ddl(self, ddl: str):
        self.__ddl = ddl


    @property
    def rdb_view_View(self):
        return self.__rdb_view_View

    @rdb_view_View.setter
    def rdb_view_View(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdb_view_View__rdb_view_View", None)
        self.__rdb_view_View = value if value is not None else set()
        
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
    def rdb_view_View30(self):
        return self.__rdb_view_View30

    @rdb_view_View30.setter
    def rdb_view_View30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdb_view_View__rdb_view_View30", None)
        self.__rdb_view_View30 = value if value is not None else set()
        
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
                    

class rdb_Table(NamedColumnSet):

    pass
class NamedElement:

    pass
class rdb_Schema(NamedElement):

    pass
class rdb_Column(NamedElement):

    pass
class rdb_view_ViewAlias(NamedElement):

    pass
class rdb_constraints_Constraint(NamedElement):

    pass
class rdb_datatypes_DataType(NamedElement):

    def __init__(self, size: int, decimalDigits: int, nullable: bool, default: str, check: str, var: str):
        self.size = size
        self.decimalDigits = decimalDigits
        self.nullable = nullable
        self.default = default
        self.check = check
        self.var = var
        
        pass
    @property
    def default(self):
        return self.__default

    @default.setter
    def default(self, default: str):
        self.__default = default


    @property
    def var(self):
        return self.__var

    @var.setter
    def var(self, var: str):
        self.__var = var


    @property
    def nullable(self):
        return self.__nullable

    @nullable.setter
    def nullable(self, nullable: bool):
        self.__nullable = nullable


    @property
    def decimalDigits(self):
        return self.__decimalDigits

    @decimalDigits.setter
    def decimalDigits(self, decimalDigits: int):
        self.__decimalDigits = decimalDigits


    @property
    def check(self):
        return self.__check

    @check.setter
    def check(self, check: str):
        self.__check = check


    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size: int):
        self.__size = size


class rdb_constraints_IndexedColumn(NamedElement):

    def __init__(self, ascending: bool, rdb_constraints_IndexedColumn: "constraints_rdb_TableColumn" = None):
        self.ascending = ascending
        self.rdb_constraints_IndexedColumn = rdb_constraints_IndexedColumn
        
        pass
    @property
    def ascending(self):
        return self.__ascending

    @ascending.setter
    def ascending(self, ascending: bool):
        self.__ascending = ascending


    @property
    def rdb_constraints_IndexedColumn(self):
        return self.__rdb_constraints_IndexedColumn

    @rdb_constraints_IndexedColumn.setter
    def rdb_constraints_IndexedColumn(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdb_constraints_IndexedColumn__rdb_constraints_IndexedColumn", None)
        self.__rdb_constraints_IndexedColumn = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "constraints_rdb_TableColumn25"):
                opp_val = getattr(old_value, "constraints_rdb_TableColumn25", None)
                if opp_val == self:
                    setattr(old_value, "constraints_rdb_TableColumn25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "constraints_rdb_TableColumn25"):
                opp_val = getattr(value, "constraints_rdb_TableColumn25", None)
                setattr(value, "constraints_rdb_TableColumn25", self)

class rdb_SchemaElement(NamedElement):

    def __init__(self, owner: str, rdb_SchemaElement: "rdb_Schema" = None):
        self.owner = owner
        self.rdb_SchemaElement = rdb_SchemaElement
        
        pass
    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, owner: str):
        self.__owner = owner


    @property
    def rdb_SchemaElement(self):
        return self.__rdb_SchemaElement

    @rdb_SchemaElement.setter
    def rdb_SchemaElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdb_SchemaElement__rdb_SchemaElement", None)
        self.__rdb_SchemaElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdb_Schema4"):
                opp_val = getattr(old_value, "rdb_Schema4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdb_Schema4"):
                opp_val = getattr(value, "rdb_Schema4", None)
                if opp_val is None:
                    setattr(value, "rdb_Schema4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class rdb_Model(NamedElement):

    def __init__(self, server_id: str, rdb_Model: set["rdb_Schema"] = None):
        self.server_id = server_id
        self.rdb_Model = rdb_Model if rdb_Model is not None else set()
        
        pass
    @property
    def server_id(self):
        return self.__server_id

    @server_id.setter
    def server_id(self, server_id: str):
        self.__server_id = server_id


    @property
    def rdb_Model(self):
        return self.__rdb_Model

    @rdb_Model.setter
    def rdb_Model(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdb_Model__rdb_Model", None)
        self.__rdb_Model = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rdb_Schema"):
                    opp_val = getattr(item, "rdb_Schema", None)
                    
                    if opp_val == self:
                        setattr(item, "rdb_Schema", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rdb_Schema"):
                    opp_val = getattr(item, "rdb_Schema", None)
                    
                    setattr(item, "rdb_Schema", self)
                    
