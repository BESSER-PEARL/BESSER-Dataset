from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class SortDirectionEnum(Enum):
    ASC = "ASC"
    DESC = "DESC"


############################################
# Definition of Classes
############################################

class SqlDateTime:

    pass
class ddlDsl_SqlDate(SqlDateTime):

    pass
class LongRaw:

    pass
class ddlDsl_Raw(LongRaw):

    def __init__(self, size: int):
        self.size = size
        
    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, size: int):
        self.__size = size

class ddlDsl_Long(LongRaw):

    def __init__(self, raw: bool):
        self.raw = raw
        
    @property
    def raw(self) -> bool:
        return self.__raw

    @raw.setter
    def raw(self, raw: bool):
        self.__raw = raw

class ddlDsl_SqlInterval(SqlDateTime):

    def __init__(self, year: bool, day: bool, precision: int, secondsPrecision: int):
        self.year = year
        self.day = day
        self.precision = precision
        self.secondsPrecision = secondsPrecision
        
    @property
    def precision(self) -> int:
        return self.__precision

    @precision.setter
    def precision(self, precision: int):
        self.__precision = precision

    @property
    def secondsPrecision(self) -> int:
        return self.__secondsPrecision

    @secondsPrecision.setter
    def secondsPrecision(self, secondsPrecision: int):
        self.__secondsPrecision = secondsPrecision

    @property
    def year(self) -> bool:
        return self.__year

    @year.setter
    def year(self, year: bool):
        self.__year = year

    @property
    def day(self) -> bool:
        return self.__day

    @day.setter
    def day(self, day: bool):
        self.__day = day

class ddlDsl_SqlTimeStamp(SqlDateTime):

    def __init__(self, precision: int):
        self.precision = precision
        
    @property
    def precision(self) -> int:
        return self.__precision

    @precision.setter
    def precision(self, precision: int):
        self.__precision = precision

class SqlDataType:

    pass
class ddlDsl_SqlBoolean(SqlDataType):

    pass
class ddlDsl_LargeObjectType(SqlDataType):

    def __init__(self, size: int):
        self.size = size
        
    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, size: int):
        self.__size = size

class ddlDsl_RowIdType(SqlDataType):

    def __init__(self, size: int):
        self.size = size
        
    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, size: int):
        self.__size = size

class ddlDsl_SqlDateTime(SqlDataType):

    pass
class ddlDsl_SqlNumber(SqlDataType):

    def __init__(self, hasPrecision: bool, precision: int, scale: int):
        self.hasPrecision = hasPrecision
        self.precision = precision
        self.scale = scale
        
    @property
    def hasPrecision(self) -> bool:
        return self.__hasPrecision

    @hasPrecision.setter
    def hasPrecision(self, hasPrecision: bool):
        self.__hasPrecision = hasPrecision

    @property
    def scale(self) -> int:
        return self.__scale

    @scale.setter
    def scale(self, scale: int):
        self.__scale = scale

    @property
    def precision(self) -> int:
        return self.__precision

    @precision.setter
    def precision(self, precision: int):
        self.__precision = precision

class ddlDsl_LongRaw(SqlDataType):

    pass
class ddlDsl_SqlCharacter(SqlDataType):

    def __init__(self, national: bool, size: int):
        self.national = national
        self.size = size
        
    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, size: int):
        self.__size = size

    @property
    def national(self) -> bool:
        return self.__national

    @national.setter
    def national(self, national: bool):
        self.__national = national

class ddlDsl_SqlDataType:

    def __init__(self, name: str, ddlDsl_SqlDataType: "ddlDsl_Column" = None):
        self.name = name
        self.ddlDsl_SqlDataType = ddlDsl_SqlDataType
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ddlDsl_SqlDataType(self):
        return self.__ddlDsl_SqlDataType

    @ddlDsl_SqlDataType.setter
    def ddlDsl_SqlDataType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddlDsl_SqlDataType__ddlDsl_SqlDataType", None)
        self.__ddlDsl_SqlDataType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddlDsl_Column19"):
                opp_val = getattr(old_value, "ddlDsl_Column19", None)
                if opp_val == self:
                    setattr(old_value, "ddlDsl_Column19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddlDsl_Column19"):
                opp_val = getattr(value, "ddlDsl_Column19", None)
                setattr(value, "ddlDsl_Column19", self)

class TableProperty:

    pass
class Constraint:

    pass
class ddlDsl_ForeignKeyConstraint(Constraint):

    pass
class ddlDsl_PrimaryKeyConstraint(Constraint):

    pass
class ddlDsl_UniqueKeyConstraint(Constraint):

    pass
class ddlDsl_NullableConstraint(Constraint):

    def __init__(self, not: bool):
        self.not = not
        
    @property
    def not(self) -> bool:
        return self.__not

    @not.setter
    def not(self, not: bool):
        self.__not = not

class ddlDsl_ReferenceClause:

    pass
class ddlDsl_Column(TableProperty):

    def __init__(self, sorted: bool, default: str, ddlDsl_Column17: "ddlDsl_CreateIndex" = None, ddlDsl_Column: "ddlDsl_ColumnComment" = None, ddlDsl_Column24: "ddlDsl_ReferenceClause" = None, ddlDsl_Column26: "ddlDsl_UniqueKeyConstraint" = None, ddlDsl_Column19: "ddlDsl_SqlDataType" = None, ddlDsl_Column21: "ddlDsl_Constraint" = None, ddlDsl_Column39: "ddlDsl_ReferenceClause" = None, ddlDsl_Column28: "ddlDsl_PrimaryKeyConstraint" = None, ddlDsl_Column30: "ddlDsl_ForeignKeyConstraint" = None):
        self.sorted = sorted
        self.default = default
        self.ddlDsl_Column17 = ddlDsl_Column17
        self.ddlDsl_Column = ddlDsl_Column
        self.ddlDsl_Column24 = ddlDsl_Column24
        self.ddlDsl_Column26 = ddlDsl_Column26
        self.ddlDsl_Column19 = ddlDsl_Column19
        self.ddlDsl_Column21 = ddlDsl_Column21
        self.ddlDsl_Column39 = ddlDsl_Column39
        self.ddlDsl_Column28 = ddlDsl_Column28
        self.ddlDsl_Column30 = ddlDsl_Column30
        
    @property
    def default(self) -> str:
        return self.__default

    @default.setter
    def default(self, default: str):
        self.__default = default

    @property
    def sorted(self) -> bool:
        return self.__sorted

    @sorted.setter
    def sorted(self, sorted: bool):
        self.__sorted = sorted

    @property
    def ddlDsl_Column(self):
        return self.__ddlDsl_Column

    @ddlDsl_Column.setter
    def ddlDsl_Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddlDsl_Column__ddlDsl_Column", None)
        self.__ddlDsl_Column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddlDsl_ColumnComment"):
                opp_val = getattr(old_value, "ddlDsl_ColumnComment", None)
                if opp_val == self:
                    setattr(old_value, "ddlDsl_ColumnComment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddlDsl_ColumnComment"):
                opp_val = getattr(value, "ddlDsl_ColumnComment", None)
                setattr(value, "ddlDsl_ColumnComment", self)

    @property
    def ddlDsl_Column26(self):
        return self.__ddlDsl_Column26

    @ddlDsl_Column26.setter
    def ddlDsl_Column26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddlDsl_Column__ddlDsl_Column26", None)
        self.__ddlDsl_Column26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddlDsl_UniqueKeyConstraint"):
                opp_val = getattr(old_value, "ddlDsl_UniqueKeyConstraint", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddlDsl_UniqueKeyConstraint"):
                opp_val = getattr(value, "ddlDsl_UniqueKeyConstraint", None)
                if opp_val is None:
                    setattr(value, "ddlDsl_UniqueKeyConstraint", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ddlDsl_Column24(self):
        return self.__ddlDsl_Column24

    @ddlDsl_Column24.setter
    def ddlDsl_Column24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddlDsl_Column__ddlDsl_Column24", None)
        self.__ddlDsl_Column24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddlDsl_ReferenceClause"):
                opp_val = getattr(old_value, "ddlDsl_ReferenceClause", None)
                if opp_val == self:
                    setattr(old_value, "ddlDsl_ReferenceClause", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddlDsl_ReferenceClause"):
                opp_val = getattr(value, "ddlDsl_ReferenceClause", None)
                setattr(value, "ddlDsl_ReferenceClause", self)

    @property
    def ddlDsl_Column30(self):
        return self.__ddlDsl_Column30

    @ddlDsl_Column30.setter
    def ddlDsl_Column30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddlDsl_Column__ddlDsl_Column30", None)
        self.__ddlDsl_Column30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddlDsl_ForeignKeyConstraint"):
                opp_val = getattr(old_value, "ddlDsl_ForeignKeyConstraint", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddlDsl_ForeignKeyConstraint"):
                opp_val = getattr(value, "ddlDsl_ForeignKeyConstraint", None)
                if opp_val is None:
                    setattr(value, "ddlDsl_ForeignKeyConstraint", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ddlDsl_Column19(self):
        return self.__ddlDsl_Column19

    @ddlDsl_Column19.setter
    def ddlDsl_Column19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddlDsl_Column__ddlDsl_Column19", None)
        self.__ddlDsl_Column19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddlDsl_SqlDataType"):
                opp_val = getattr(old_value, "ddlDsl_SqlDataType", None)
                if opp_val == self:
                    setattr(old_value, "ddlDsl_SqlDataType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddlDsl_SqlDataType"):
                opp_val = getattr(value, "ddlDsl_SqlDataType", None)
                setattr(value, "ddlDsl_SqlDataType", self)

    @property
    def ddlDsl_Column21(self):
        return self.__ddlDsl_Column21

    @ddlDsl_Column21.setter
    def ddlDsl_Column21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddlDsl_Column__ddlDsl_Column21", None)
        self.__ddlDsl_Column21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddlDsl_Constraint22"):
                opp_val = getattr(old_value, "ddlDsl_Constraint22", None)
                if opp_val == self:
                    setattr(old_value, "ddlDsl_Constraint22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddlDsl_Constraint22"):
                opp_val = getattr(value, "ddlDsl_Constraint22", None)
                setattr(value, "ddlDsl_Constraint22", self)

    @property
    def ddlDsl_Column28(self):
        return self.__ddlDsl_Column28

    @ddlDsl_Column28.setter
    def ddlDsl_Column28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddlDsl_Column__ddlDsl_Column28", None)
        self.__ddlDsl_Column28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddlDsl_PrimaryKeyConstraint"):
                opp_val = getattr(old_value, "ddlDsl_PrimaryKeyConstraint", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddlDsl_PrimaryKeyConstraint"):
                opp_val = getattr(value, "ddlDsl_PrimaryKeyConstraint", None)
                if opp_val is None:
                    setattr(value, "ddlDsl_PrimaryKeyConstraint", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ddlDsl_Column17(self):
        return self.__ddlDsl_Column17

    @ddlDsl_Column17.setter
    def ddlDsl_Column17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddlDsl_Column__ddlDsl_Column17", None)
        self.__ddlDsl_Column17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddlDsl_CreateIndex16"):
                opp_val = getattr(old_value, "ddlDsl_CreateIndex16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddlDsl_CreateIndex16"):
                opp_val = getattr(value, "ddlDsl_CreateIndex16", None)
                if opp_val is None:
                    setattr(value, "ddlDsl_CreateIndex16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ddlDsl_Column39(self):
        return self.__ddlDsl_Column39

    @ddlDsl_Column39.setter
    def ddlDsl_Column39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddlDsl_Column__ddlDsl_Column39", None)
        self.__ddlDsl_Column39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddlDsl_ReferenceClause38"):
                opp_val = getattr(old_value, "ddlDsl_ReferenceClause38", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddlDsl_ReferenceClause38"):
                opp_val = getattr(value, "ddlDsl_ReferenceClause38", None)
                if opp_val is None:
                    setattr(value, "ddlDsl_ReferenceClause38", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ddlDsl_TableProperty:

    def __init__(self, name: str, ddlDsl_TableProperty: "ddlDsl_CreateTable" = None):
        self.name = name
        self.ddlDsl_TableProperty = ddlDsl_TableProperty
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ddlDsl_TableProperty(self):
        return self.__ddlDsl_TableProperty

    @ddlDsl_TableProperty.setter
    def ddlDsl_TableProperty(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddlDsl_TableProperty__ddlDsl_TableProperty", None)
        self.__ddlDsl_TableProperty = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddlDsl_CreateTable12"):
                opp_val = getattr(old_value, "ddlDsl_CreateTable12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddlDsl_CreateTable12"):
                opp_val = getattr(value, "ddlDsl_CreateTable12", None)
                if opp_val is None:
                    setattr(value, "ddlDsl_CreateTable12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Create:

    pass
class ddlDsl_CreateIndex(Create):

    def __init__(self, unique: bool, sortOrders: str, ddlDsl_CreateIndex: "ddlDsl_CreateTable" = None, ddlDsl_CreateIndex16: set["ddlDsl_Column"] = None):
        self.unique = unique
        self.sortOrders = sortOrders
        self.ddlDsl_CreateIndex = ddlDsl_CreateIndex
        self.ddlDsl_CreateIndex16 = ddlDsl_CreateIndex16 if ddlDsl_CreateIndex16 is not None else set()
        
    @property
    def unique(self) -> bool:
        return self.__unique

    @unique.setter
    def unique(self, unique: bool):
        self.__unique = unique

    @property
    def sortOrders(self) -> str:
        return self.__sortOrders

    @sortOrders.setter
    def sortOrders(self, sortOrders: str):
        self.__sortOrders = sortOrders

    @property
    def ddlDsl_CreateIndex(self):
        return self.__ddlDsl_CreateIndex

    @ddlDsl_CreateIndex.setter
    def ddlDsl_CreateIndex(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddlDsl_CreateIndex__ddlDsl_CreateIndex", None)
        self.__ddlDsl_CreateIndex = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddlDsl_CreateTable14"):
                opp_val = getattr(old_value, "ddlDsl_CreateTable14", None)
                if opp_val == self:
                    setattr(old_value, "ddlDsl_CreateTable14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddlDsl_CreateTable14"):
                opp_val = getattr(value, "ddlDsl_CreateTable14", None)
                setattr(value, "ddlDsl_CreateTable14", self)

    @property
    def ddlDsl_CreateIndex16(self):
        return self.__ddlDsl_CreateIndex16

    @ddlDsl_CreateIndex16.setter
    def ddlDsl_CreateIndex16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddlDsl_CreateIndex__ddlDsl_CreateIndex16", None)
        self.__ddlDsl_CreateIndex16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ddlDsl_Column17"):
                    opp_val = getattr(item, "ddlDsl_Column17", None)
                    
                    if opp_val == self:
                        setattr(item, "ddlDsl_Column17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ddlDsl_Column17"):
                    opp_val = getattr(item, "ddlDsl_Column17", None)
                    
                    setattr(item, "ddlDsl_Column17", self)
                    

class ddlDsl_CreateTable(Create):

    pass
class DdlStatement:

    pass
class ddlDsl_Drop(DdlStatement):

    def __init__(self, object: str):
        self.object = object
        
    @property
    def object(self) -> str:
        return self.__object

    @object.setter
    def object(self, object: str):
        self.__object = object

class ddlDsl_Create(DdlStatement):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class ddlDsl_Alter(DdlStatement):

    pass
class ddlDsl_DdlStatement:

    pass
class Comment:

    pass
class ddlDsl_ColumnComment(Comment):

    pass
class ddlDsl_TableComment(Comment):

    pass
class ddlDsl_Comment(DdlStatement):

    def __init__(self, comment: str):
        self.comment = comment
        
    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

class AlterTableAction:

    pass
class ddlDsl_AddTableConstraint(AlterTableAction):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class ddlDsl_DropTableConstraint(AlterTableAction):

    pass
class ddlDsl_Constraint(TableProperty):

    pass
class ddlDsl_AlterTableAction:

    pass
class ddlDsl_Ddl:

    pass