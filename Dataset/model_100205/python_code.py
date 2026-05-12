from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class TriggerTime(Enum):
    BEFORE = "BEFORE"
    AFTER = "AFTER"


############################################
# Definition of Classes
############################################

class TriggerAction:

    pass
class sqls_TriggerUpdate(TriggerAction):

    pass
class sqls_TriggerDelete(TriggerAction):

    pass
class sqls_TriggerInsert(TriggerAction):

    pass
class Type:

    pass
class sqls_TypeDef(Type):

    pass
class sqls_Enum(Type):

    pass
class sqls_TriggerAction:

    pass
class sqls_UpdateColumnExpression:

    pass
class sqls_TableRef:

    def __init__(self, alias: str, sqls_TableRef: "sqls_Select" = None, sqls_TableRef64: "sqls_Table" = None, sqls_TableRef126: "sqls_ColumnRef" = None):
        self.alias = alias
        self.sqls_TableRef = sqls_TableRef
        self.sqls_TableRef64 = sqls_TableRef64
        self.sqls_TableRef126 = sqls_TableRef126
        
        pass
    @property
    def alias(self):
        return self.__alias

    @alias.setter
    def alias(self, alias: str):
        self.__alias = alias


    @property
    def sqls_TableRef(self):
        return self.__sqls_TableRef

    @sqls_TableRef.setter
    def sqls_TableRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqls_TableRef__sqls_TableRef", None)
        self.__sqls_TableRef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqls_Select50"):
                opp_val = getattr(old_value, "sqls_Select50", None)
                if opp_val == self:
                    setattr(old_value, "sqls_Select50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqls_Select50"):
                opp_val = getattr(value, "sqls_Select50", None)
                setattr(value, "sqls_Select50", self)

    @property
    def sqls_TableRef126(self):
        return self.__sqls_TableRef126

    @sqls_TableRef126.setter
    def sqls_TableRef126(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqls_TableRef__sqls_TableRef126", None)
        self.__sqls_TableRef126 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqls_ColumnRef"):
                opp_val = getattr(old_value, "sqls_ColumnRef", None)
                if opp_val == self:
                    setattr(old_value, "sqls_ColumnRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqls_ColumnRef"):
                opp_val = getattr(value, "sqls_ColumnRef", None)
                setattr(value, "sqls_ColumnRef", self)

    @property
    def sqls_TableRef64(self):
        return self.__sqls_TableRef64

    @sqls_TableRef64.setter
    def sqls_TableRef64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqls_TableRef__sqls_TableRef64", None)
        self.__sqls_TableRef64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqls_Table65"):
                opp_val = getattr(old_value, "sqls_Table65", None)
                if opp_val == self:
                    setattr(old_value, "sqls_Table65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqls_Table65"):
                opp_val = getattr(value, "sqls_Table65", None)
                setattr(value, "sqls_Table65", self)

class sqls_Function:

    pass
class SqlExpr:

    pass
class sqls_SqlBinaryExpr(SqlExpr):

    def __init__(self, op: str, sqls_SqlBinaryExpr: "sqls_SqlExpr" = None, sqls_SqlBinaryExpr117: "sqls_SqlExpr" = None):
        self.op = op
        self.sqls_SqlBinaryExpr = sqls_SqlBinaryExpr
        self.sqls_SqlBinaryExpr117 = sqls_SqlBinaryExpr117
        
        pass
    @property
    def op(self):
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op


    @property
    def sqls_SqlBinaryExpr117(self):
        return self.__sqls_SqlBinaryExpr117

    @sqls_SqlBinaryExpr117.setter
    def sqls_SqlBinaryExpr117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqls_SqlBinaryExpr__sqls_SqlBinaryExpr117", None)
        self.__sqls_SqlBinaryExpr117 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqls_SqlExpr118"):
                opp_val = getattr(old_value, "sqls_SqlExpr118", None)
                if opp_val == self:
                    setattr(old_value, "sqls_SqlExpr118", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqls_SqlExpr118"):
                opp_val = getattr(value, "sqls_SqlExpr118", None)
                setattr(value, "sqls_SqlExpr118", self)

    @property
    def sqls_SqlBinaryExpr(self):
        return self.__sqls_SqlBinaryExpr

    @sqls_SqlBinaryExpr.setter
    def sqls_SqlBinaryExpr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqls_SqlBinaryExpr__sqls_SqlBinaryExpr", None)
        self.__sqls_SqlBinaryExpr = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqls_SqlExpr115"):
                opp_val = getattr(old_value, "sqls_SqlExpr115", None)
                if opp_val == self:
                    setattr(old_value, "sqls_SqlExpr115", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqls_SqlExpr115"):
                opp_val = getattr(value, "sqls_SqlExpr115", None)
                setattr(value, "sqls_SqlExpr115", self)

class sqls_SqlPlaceholder(SqlExpr):

    pass
class sqls_SqlParam(SqlExpr):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class sqls_OldColumn(SqlExpr):

    pass
class sqls_ColumnRef(SqlExpr):

    pass
class sqls_SqlNumberLiteral(SqlExpr):

    def __init__(self, value: int):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value


class sqls_NewColumn(SqlExpr):

    pass
class sqls_SqlStringLiteral(SqlExpr):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class sqls_SqlNested(SqlExpr):

    pass
class sqls_SqlFunction(SqlExpr):

    pass
class sqls_SelectList:

    pass
class sqls_ResultColumn:

    def __init__(self, name: str, sqls_ResultColumn46: "sqls_SelectList" = None, sqls_ResultColumn: "sqls_SqlExpr" = None):
        self.name = name
        self.sqls_ResultColumn46 = sqls_ResultColumn46
        self.sqls_ResultColumn = sqls_ResultColumn
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def sqls_ResultColumn(self):
        return self.__sqls_ResultColumn

    @sqls_ResultColumn.setter
    def sqls_ResultColumn(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqls_ResultColumn__sqls_ResultColumn", None)
        self.__sqls_ResultColumn = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqls_SqlExpr44"):
                opp_val = getattr(old_value, "sqls_SqlExpr44", None)
                if opp_val == self:
                    setattr(old_value, "sqls_SqlExpr44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqls_SqlExpr44"):
                opp_val = getattr(value, "sqls_SqlExpr44", None)
                setattr(value, "sqls_SqlExpr44", self)

    @property
    def sqls_ResultColumn46(self):
        return self.__sqls_ResultColumn46

    @sqls_ResultColumn46.setter
    def sqls_ResultColumn46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqls_ResultColumn__sqls_ResultColumn46", None)
        self.__sqls_ResultColumn46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqls_SelectList"):
                opp_val = getattr(old_value, "sqls_SelectList", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqls_SelectList"):
                opp_val = getattr(value, "sqls_SelectList", None)
                if opp_val is None:
                    setattr(value, "sqls_SelectList", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sqls_OrderingTerm:

    def __init__(self, asc: bool, desc: bool, sqls_OrderingTerm: "sqls_SqlExpr" = None, sqls_OrderingTerm56: "sqls_Select" = None):
        self.asc = asc
        self.desc = desc
        self.sqls_OrderingTerm = sqls_OrderingTerm
        self.sqls_OrderingTerm56 = sqls_OrderingTerm56
        
        pass
    @property
    def desc(self):
        return self.__desc

    @desc.setter
    def desc(self, desc: bool):
        self.__desc = desc


    @property
    def asc(self):
        return self.__asc

    @asc.setter
    def asc(self, asc: bool):
        self.__asc = asc


    @property
    def sqls_OrderingTerm(self):
        return self.__sqls_OrderingTerm

    @sqls_OrderingTerm.setter
    def sqls_OrderingTerm(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqls_OrderingTerm__sqls_OrderingTerm", None)
        self.__sqls_OrderingTerm = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqls_SqlExpr42"):
                opp_val = getattr(old_value, "sqls_SqlExpr42", None)
                if opp_val == self:
                    setattr(old_value, "sqls_SqlExpr42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqls_SqlExpr42"):
                opp_val = getattr(value, "sqls_SqlExpr42", None)
                setattr(value, "sqls_SqlExpr42", self)

    @property
    def sqls_OrderingTerm56(self):
        return self.__sqls_OrderingTerm56

    @sqls_OrderingTerm56.setter
    def sqls_OrderingTerm56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqls_OrderingTerm__sqls_OrderingTerm56", None)
        self.__sqls_OrderingTerm56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqls_Select55"):
                opp_val = getattr(old_value, "sqls_Select55", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqls_Select55"):
                opp_val = getattr(value, "sqls_Select55", None)
                if opp_val is None:
                    setattr(value, "sqls_Select55", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sqls_SqlSentence:

    pass
class SqlSentence:

    pass
class sqls_InsertStatement(SqlSentence):

    pass
class sqls_Delete(SqlSentence):

    pass
class sqls_Insert(SqlSentence):

    pass
class sqls_DeleteTable(SqlSentence):

    pass
class sqls_Get(SqlSentence):

    pass
class sqls_Update(SqlSentence):

    pass
class sqls_SqlMethodRef(SqlSentence):

    pass
class sqls_Select(SqlSentence):

    def __init__(self, all: bool, sqls_Select: "sqls_SelectList" = None, sqls_Select50: "sqls_TableRef" = None, sqls_Select52: "sqls_SqlExpr" = None, sqls_Select55: set["sqls_OrderingTerm"] = None, sqls_Select58: "sqls_SqlExpr" = None, sqls_Select61: "sqls_SqlExpr" = None):
        self.all = all
        self.sqls_Select = sqls_Select
        self.sqls_Select50 = sqls_Select50
        self.sqls_Select52 = sqls_Select52
        self.sqls_Select55 = sqls_Select55 if sqls_Select55 is not None else set()
        self.sqls_Select58 = sqls_Select58
        self.sqls_Select61 = sqls_Select61
        
        pass
    @property
    def all(self):
        return self.__all

    @all.setter
    def all(self, all: bool):
        self.__all = all


    @property
    def sqls_Select58(self):
        return self.__sqls_Select58

    @sqls_Select58.setter
    def sqls_Select58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqls_Select__sqls_Select58", None)
        self.__sqls_Select58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqls_SqlExpr59"):
                opp_val = getattr(old_value, "sqls_SqlExpr59", None)
                if opp_val == self:
                    setattr(old_value, "sqls_SqlExpr59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqls_SqlExpr59"):
                opp_val = getattr(value, "sqls_SqlExpr59", None)
                setattr(value, "sqls_SqlExpr59", self)

    @property
    def sqls_Select(self):
        return self.__sqls_Select

    @sqls_Select.setter
    def sqls_Select(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqls_Select__sqls_Select", None)
        self.__sqls_Select = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqls_SelectList48"):
                opp_val = getattr(old_value, "sqls_SelectList48", None)
                if opp_val == self:
                    setattr(old_value, "sqls_SelectList48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqls_SelectList48"):
                opp_val = getattr(value, "sqls_SelectList48", None)
                setattr(value, "sqls_SelectList48", self)

    @property
    def sqls_Select61(self):
        return self.__sqls_Select61

    @sqls_Select61.setter
    def sqls_Select61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqls_Select__sqls_Select61", None)
        self.__sqls_Select61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqls_SqlExpr62"):
                opp_val = getattr(old_value, "sqls_SqlExpr62", None)
                if opp_val == self:
                    setattr(old_value, "sqls_SqlExpr62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqls_SqlExpr62"):
                opp_val = getattr(value, "sqls_SqlExpr62", None)
                setattr(value, "sqls_SqlExpr62", self)

    @property
    def sqls_Select55(self):
        return self.__sqls_Select55

    @sqls_Select55.setter
    def sqls_Select55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqls_Select__sqls_Select55", None)
        self.__sqls_Select55 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sqls_OrderingTerm56"):
                    opp_val = getattr(item, "sqls_OrderingTerm56", None)
                    
                    if opp_val == self:
                        setattr(item, "sqls_OrderingTerm56", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sqls_OrderingTerm56"):
                    opp_val = getattr(item, "sqls_OrderingTerm56", None)
                    
                    setattr(item, "sqls_OrderingTerm56", self)
                    

    @property
    def sqls_Select50(self):
        return self.__sqls_Select50

    @sqls_Select50.setter
    def sqls_Select50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqls_Select__sqls_Select50", None)
        self.__sqls_Select50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqls_TableRef"):
                opp_val = getattr(old_value, "sqls_TableRef", None)
                if opp_val == self:
                    setattr(old_value, "sqls_TableRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqls_TableRef"):
                opp_val = getattr(value, "sqls_TableRef", None)
                setattr(value, "sqls_TableRef", self)

    @property
    def sqls_Select52(self):
        return self.__sqls_Select52

    @sqls_Select52.setter
    def sqls_Select52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqls_Select__sqls_Select52", None)
        self.__sqls_Select52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqls_SqlExpr53"):
                opp_val = getattr(old_value, "sqls_SqlExpr53", None)
                if opp_val == self:
                    setattr(old_value, "sqls_SqlExpr53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqls_SqlExpr53"):
                opp_val = getattr(value, "sqls_SqlExpr53", None)
                setattr(value, "sqls_SqlExpr53", self)

class TableConstraint:

    pass
class sqls_UniqueTableConstraint(TableConstraint):

    def __init__(self, name: str, sqls_UniqueTableConstraint: set["sqls_Column"] = None):
        self.name = name
        self.sqls_UniqueTableConstraint = sqls_UniqueTableConstraint if sqls_UniqueTableConstraint is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def sqls_UniqueTableConstraint(self):
        return self.__sqls_UniqueTableConstraint

    @sqls_UniqueTableConstraint.setter
    def sqls_UniqueTableConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqls_UniqueTableConstraint__sqls_UniqueTableConstraint", None)
        self.__sqls_UniqueTableConstraint = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sqls_Column32"):
                    opp_val = getattr(item, "sqls_Column32", None)
                    
                    if opp_val == self:
                        setattr(item, "sqls_Column32", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sqls_Column32"):
                    opp_val = getattr(item, "sqls_Column32", None)
                    
                    setattr(item, "sqls_Column32", self)
                    

class sqls_TableConstraint:

    pass
class sqls_SqlExpr:

    pass
class sqls_SqlType:

    pass
class sqls_EnumElement:

    def __init__(self, name: str, text: str, sqls_EnumElement: "sqls_Enum" = None):
        self.name = name
        self.text = text
        self.sqls_EnumElement = sqls_EnumElement
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


    @property
    def sqls_EnumElement(self):
        return self.__sqls_EnumElement

    @sqls_EnumElement.setter
    def sqls_EnumElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqls_EnumElement__sqls_EnumElement", None)
        self.__sqls_EnumElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqls_Enum"):
                opp_val = getattr(old_value, "sqls_Enum", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqls_Enum"):
                opp_val = getattr(value, "sqls_Enum", None)
                if opp_val is None:
                    setattr(value, "sqls_Enum", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sqls_SqlMethod:

    def __init__(self, array: bool, name: str, sqls_SqlMethod34: set["sqls_Tag"] = None, sqls_SqlMethod37: "sqls_Table" = None, sqls_SqlMethod40: set["sqls_SqlSentence"] = None, sqls_SqlMethod: "sqls_SqlLibrary" = None, sqls_SqlMethod131: "sqls_SqlMethodRef" = None):
        self.array = array
        self.name = name
        self.sqls_SqlMethod34 = sqls_SqlMethod34 if sqls_SqlMethod34 is not None else set()
        self.sqls_SqlMethod37 = sqls_SqlMethod37
        self.sqls_SqlMethod40 = sqls_SqlMethod40 if sqls_SqlMethod40 is not None else set()
        self.sqls_SqlMethod = sqls_SqlMethod
        self.sqls_SqlMethod131 = sqls_SqlMethod131
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def array(self):
        return self.__array

    @array.setter
    def array(self, array: bool):
        self.__array = array


    @property
    def sqls_SqlMethod34(self):
        return self.__sqls_SqlMethod34

    @sqls_SqlMethod34.setter
    def sqls_SqlMethod34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqls_SqlMethod__sqls_SqlMethod34", None)
        self.__sqls_SqlMethod34 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sqls_Tag35"):
                    opp_val = getattr(item, "sqls_Tag35", None)
                    
                    if opp_val == self:
                        setattr(item, "sqls_Tag35", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sqls_Tag35"):
                    opp_val = getattr(item, "sqls_Tag35", None)
                    
                    setattr(item, "sqls_Tag35", self)
                    

    @property
    def sqls_SqlMethod131(self):
        return self.__sqls_SqlMethod131

    @sqls_SqlMethod131.setter
    def sqls_SqlMethod131(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqls_SqlMethod__sqls_SqlMethod131", None)
        self.__sqls_SqlMethod131 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqls_SqlMethodRef"):
                opp_val = getattr(old_value, "sqls_SqlMethodRef", None)
                if opp_val == self:
                    setattr(old_value, "sqls_SqlMethodRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqls_SqlMethodRef"):
                opp_val = getattr(value, "sqls_SqlMethodRef", None)
                setattr(value, "sqls_SqlMethodRef", self)

    @property
    def sqls_SqlMethod(self):
        return self.__sqls_SqlMethod

    @sqls_SqlMethod.setter
    def sqls_SqlMethod(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqls_SqlMethod__sqls_SqlMethod", None)
        self.__sqls_SqlMethod = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqls_SqlLibrary13"):
                opp_val = getattr(old_value, "sqls_SqlLibrary13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqls_SqlLibrary13"):
                opp_val = getattr(value, "sqls_SqlLibrary13", None)
                if opp_val is None:
                    setattr(value, "sqls_SqlLibrary13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sqls_SqlMethod37(self):
        return self.__sqls_SqlMethod37

    @sqls_SqlMethod37.setter
    def sqls_SqlMethod37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqls_SqlMethod__sqls_SqlMethod37", None)
        self.__sqls_SqlMethod37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqls_Table38"):
                opp_val = getattr(old_value, "sqls_Table38", None)
                if opp_val == self:
                    setattr(old_value, "sqls_Table38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqls_Table38"):
                opp_val = getattr(value, "sqls_Table38", None)
                setattr(value, "sqls_Table38", self)

    @property
    def sqls_SqlMethod40(self):
        return self.__sqls_SqlMethod40

    @sqls_SqlMethod40.setter
    def sqls_SqlMethod40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqls_SqlMethod__sqls_SqlMethod40", None)
        self.__sqls_SqlMethod40 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sqls_SqlSentence"):
                    opp_val = getattr(item, "sqls_SqlSentence", None)
                    
                    if opp_val == self:
                        setattr(item, "sqls_SqlSentence", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sqls_SqlSentence"):
                    opp_val = getattr(item, "sqls_SqlSentence", None)
                    
                    setattr(item, "sqls_SqlSentence", self)
                    

class sqls_Trigger:

    def __init__(self, name: str, time: str, sqls_Trigger101: set["sqls_Tag"] = None, sqls_Trigger104: "sqls_TriggerAction" = None, sqls_Trigger106: "sqls_Table" = None, sqls_Trigger109: set["sqls_SqlSentence"] = None, sqls_Trigger: "sqls_SqlLibrary" = None):
        self.name = name
        self.time = time
        self.sqls_Trigger101 = sqls_Trigger101 if sqls_Trigger101 is not None else set()
        self.sqls_Trigger104 = sqls_Trigger104
        self.sqls_Trigger106 = sqls_Trigger106
        self.sqls_Trigger109 = sqls_Trigger109 if sqls_Trigger109 is not None else set()
        self.sqls_Trigger = sqls_Trigger
        
        pass
    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self, time: str):
        self.__time = time


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def sqls_Trigger(self):
        return self.__sqls_Trigger

    @sqls_Trigger.setter
    def sqls_Trigger(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqls_Trigger__sqls_Trigger", None)
        self.__sqls_Trigger = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqls_SqlLibrary11"):
                opp_val = getattr(old_value, "sqls_SqlLibrary11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqls_SqlLibrary11"):
                opp_val = getattr(value, "sqls_SqlLibrary11", None)
                if opp_val is None:
                    setattr(value, "sqls_SqlLibrary11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sqls_Trigger106(self):
        return self.__sqls_Trigger106

    @sqls_Trigger106.setter
    def sqls_Trigger106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqls_Trigger__sqls_Trigger106", None)
        self.__sqls_Trigger106 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqls_Table107"):
                opp_val = getattr(old_value, "sqls_Table107", None)
                if opp_val == self:
                    setattr(old_value, "sqls_Table107", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqls_Table107"):
                opp_val = getattr(value, "sqls_Table107", None)
                setattr(value, "sqls_Table107", self)

    @property
    def sqls_Trigger104(self):
        return self.__sqls_Trigger104

    @sqls_Trigger104.setter
    def sqls_Trigger104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqls_Trigger__sqls_Trigger104", None)
        self.__sqls_Trigger104 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqls_TriggerAction"):
                opp_val = getattr(old_value, "sqls_TriggerAction", None)
                if opp_val == self:
                    setattr(old_value, "sqls_TriggerAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqls_TriggerAction"):
                opp_val = getattr(value, "sqls_TriggerAction", None)
                setattr(value, "sqls_TriggerAction", self)

    @property
    def sqls_Trigger109(self):
        return self.__sqls_Trigger109

    @sqls_Trigger109.setter
    def sqls_Trigger109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqls_Trigger__sqls_Trigger109", None)
        self.__sqls_Trigger109 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sqls_SqlSentence110"):
                    opp_val = getattr(item, "sqls_SqlSentence110", None)
                    
                    if opp_val == self:
                        setattr(item, "sqls_SqlSentence110", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sqls_SqlSentence110"):
                    opp_val = getattr(item, "sqls_SqlSentence110", None)
                    
                    setattr(item, "sqls_SqlSentence110", self)
                    

    @property
    def sqls_Trigger101(self):
        return self.__sqls_Trigger101

    @sqls_Trigger101.setter
    def sqls_Trigger101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqls_Trigger__sqls_Trigger101", None)
        self.__sqls_Trigger101 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sqls_Tag102"):
                    opp_val = getattr(item, "sqls_Tag102", None)
                    
                    if opp_val == self:
                        setattr(item, "sqls_Tag102", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sqls_Tag102"):
                    opp_val = getattr(item, "sqls_Tag102", None)
                    
                    setattr(item, "sqls_Tag102", self)
                    

class sqls_Column:

    def __init__(self, name: str, null: bool, primaryKey: bool, sqls_Column29: "sqls_SqlExpr" = None, sqls_Column76: "sqls_InsertStatement" = None, sqls_Column94: "sqls_UpdateColumnExpression" = None, sqls_Column120: "sqls_NewColumn" = None, sqls_Column122: "sqls_OldColumn" = None, sqls_Column32: "sqls_UniqueTableConstraint" = None, sqls_Column: "sqls_Table" = None, sqls_Column26: "sqls_SqlType" = None, sqls_Column129: "sqls_ColumnRef" = None, sqls_Column135: "sqls_TriggerUpdate" = None):
        self.name = name
        self.null = null
        self.primaryKey = primaryKey
        self.sqls_Column29 = sqls_Column29
        self.sqls_Column76 = sqls_Column76
        self.sqls_Column94 = sqls_Column94
        self.sqls_Column120 = sqls_Column120
        self.sqls_Column122 = sqls_Column122
        self.sqls_Column32 = sqls_Column32
        self.sqls_Column = sqls_Column
        self.sqls_Column26 = sqls_Column26
        self.sqls_Column129 = sqls_Column129
        self.sqls_Column135 = sqls_Column135
        
        pass
    @property
    def primaryKey(self):
        return self.__primaryKey

    @primaryKey.setter
    def primaryKey(self, primaryKey: bool):
        self.__primaryKey = primaryKey


    @property
    def null(self):
        return self.__null

    @null.setter
    def null(self, null: bool):
        self.__null = null


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def sqls_Column(self):
        return self.__sqls_Column

    @sqls_Column.setter
    def sqls_Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqls_Column__sqls_Column", None)
        self.__sqls_Column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqls_Table22"):
                opp_val = getattr(old_value, "sqls_Table22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqls_Table22"):
                opp_val = getattr(value, "sqls_Table22", None)
                if opp_val is None:
                    setattr(value, "sqls_Table22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sqls_Column29(self):
        return self.__sqls_Column29

    @sqls_Column29.setter
    def sqls_Column29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqls_Column__sqls_Column29", None)
        self.__sqls_Column29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqls_SqlExpr30"):
                opp_val = getattr(old_value, "sqls_SqlExpr30", None)
                if opp_val == self:
                    setattr(old_value, "sqls_SqlExpr30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqls_SqlExpr30"):
                opp_val = getattr(value, "sqls_SqlExpr30", None)
                setattr(value, "sqls_SqlExpr30", self)

    @property
    def sqls_Column76(self):
        return self.__sqls_Column76

    @sqls_Column76.setter
    def sqls_Column76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqls_Column__sqls_Column76", None)
        self.__sqls_Column76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqls_InsertStatement75"):
                opp_val = getattr(old_value, "sqls_InsertStatement75", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqls_InsertStatement75"):
                opp_val = getattr(value, "sqls_InsertStatement75", None)
                if opp_val is None:
                    setattr(value, "sqls_InsertStatement75", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sqls_Column122(self):
        return self.__sqls_Column122

    @sqls_Column122.setter
    def sqls_Column122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqls_Column__sqls_Column122", None)
        self.__sqls_Column122 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqls_OldColumn"):
                opp_val = getattr(old_value, "sqls_OldColumn", None)
                if opp_val == self:
                    setattr(old_value, "sqls_OldColumn", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqls_OldColumn"):
                opp_val = getattr(value, "sqls_OldColumn", None)
                setattr(value, "sqls_OldColumn", self)

    @property
    def sqls_Column135(self):
        return self.__sqls_Column135

    @sqls_Column135.setter
    def sqls_Column135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqls_Column__sqls_Column135", None)
        self.__sqls_Column135 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqls_TriggerUpdate"):
                opp_val = getattr(old_value, "sqls_TriggerUpdate", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqls_TriggerUpdate"):
                opp_val = getattr(value, "sqls_TriggerUpdate", None)
                if opp_val is None:
                    setattr(value, "sqls_TriggerUpdate", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sqls_Column120(self):
        return self.__sqls_Column120

    @sqls_Column120.setter
    def sqls_Column120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqls_Column__sqls_Column120", None)
        self.__sqls_Column120 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqls_NewColumn"):
                opp_val = getattr(old_value, "sqls_NewColumn", None)
                if opp_val == self:
                    setattr(old_value, "sqls_NewColumn", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqls_NewColumn"):
                opp_val = getattr(value, "sqls_NewColumn", None)
                setattr(value, "sqls_NewColumn", self)

    @property
    def sqls_Column94(self):
        return self.__sqls_Column94

    @sqls_Column94.setter
    def sqls_Column94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqls_Column__sqls_Column94", None)
        self.__sqls_Column94 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqls_UpdateColumnExpression93"):
                opp_val = getattr(old_value, "sqls_UpdateColumnExpression93", None)
                if opp_val == self:
                    setattr(old_value, "sqls_UpdateColumnExpression93", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqls_UpdateColumnExpression93"):
                opp_val = getattr(value, "sqls_UpdateColumnExpression93", None)
                setattr(value, "sqls_UpdateColumnExpression93", self)

    @property
    def sqls_Column129(self):
        return self.__sqls_Column129

    @sqls_Column129.setter
    def sqls_Column129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqls_Column__sqls_Column129", None)
        self.__sqls_Column129 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqls_ColumnRef128"):
                opp_val = getattr(old_value, "sqls_ColumnRef128", None)
                if opp_val == self:
                    setattr(old_value, "sqls_ColumnRef128", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqls_ColumnRef128"):
                opp_val = getattr(value, "sqls_ColumnRef128", None)
                setattr(value, "sqls_ColumnRef128", self)

    @property
    def sqls_Column32(self):
        return self.__sqls_Column32

    @sqls_Column32.setter
    def sqls_Column32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqls_Column__sqls_Column32", None)
        self.__sqls_Column32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqls_UniqueTableConstraint"):
                opp_val = getattr(old_value, "sqls_UniqueTableConstraint", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqls_UniqueTableConstraint"):
                opp_val = getattr(value, "sqls_UniqueTableConstraint", None)
                if opp_val is None:
                    setattr(value, "sqls_UniqueTableConstraint", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sqls_Column26(self):
        return self.__sqls_Column26

    @sqls_Column26.setter
    def sqls_Column26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqls_Column__sqls_Column26", None)
        self.__sqls_Column26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqls_SqlType27"):
                opp_val = getattr(old_value, "sqls_SqlType27", None)
                if opp_val == self:
                    setattr(old_value, "sqls_SqlType27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqls_SqlType27"):
                opp_val = getattr(value, "sqls_SqlType27", None)
                setattr(value, "sqls_SqlType27", self)

class sqls_Table:

    def __init__(self, name: str, sqls_Table: "sqls_SqlLibrary" = None, sqls_Table38: "sqls_SqlMethod" = None, sqls_Table65: "sqls_TableRef" = None, sqls_Table81: "sqls_Delete" = None, sqls_Table71: "sqls_Insert" = None, sqls_Table73: "sqls_InsertStatement" = None, sqls_Table86: "sqls_Update" = None, sqls_Table99: "sqls_Get" = None, sqls_Table107: "sqls_Trigger" = None, sqls_Table133: "sqls_DeleteTable" = None, sqls_Table19: set["sqls_Tag"] = None, sqls_Table22: set["sqls_Column"] = None, sqls_Table24: set["sqls_TableConstraint"] = None):
        self.name = name
        self.sqls_Table = sqls_Table
        self.sqls_Table38 = sqls_Table38
        self.sqls_Table65 = sqls_Table65
        self.sqls_Table81 = sqls_Table81
        self.sqls_Table71 = sqls_Table71
        self.sqls_Table73 = sqls_Table73
        self.sqls_Table86 = sqls_Table86
        self.sqls_Table99 = sqls_Table99
        self.sqls_Table107 = sqls_Table107
        self.sqls_Table133 = sqls_Table133
        self.sqls_Table19 = sqls_Table19 if sqls_Table19 is not None else set()
        self.sqls_Table22 = sqls_Table22 if sqls_Table22 is not None else set()
        self.sqls_Table24 = sqls_Table24 if sqls_Table24 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def sqls_Table107(self):
        return self.__sqls_Table107

    @sqls_Table107.setter
    def sqls_Table107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqls_Table__sqls_Table107", None)
        self.__sqls_Table107 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqls_Trigger106"):
                opp_val = getattr(old_value, "sqls_Trigger106", None)
                if opp_val == self:
                    setattr(old_value, "sqls_Trigger106", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqls_Trigger106"):
                opp_val = getattr(value, "sqls_Trigger106", None)
                setattr(value, "sqls_Trigger106", self)

    @property
    def sqls_Table99(self):
        return self.__sqls_Table99

    @sqls_Table99.setter
    def sqls_Table99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqls_Table__sqls_Table99", None)
        self.__sqls_Table99 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqls_Get"):
                opp_val = getattr(old_value, "sqls_Get", None)
                if opp_val == self:
                    setattr(old_value, "sqls_Get", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqls_Get"):
                opp_val = getattr(value, "sqls_Get", None)
                setattr(value, "sqls_Get", self)

    @property
    def sqls_Table24(self):
        return self.__sqls_Table24

    @sqls_Table24.setter
    def sqls_Table24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqls_Table__sqls_Table24", None)
        self.__sqls_Table24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sqls_TableConstraint"):
                    opp_val = getattr(item, "sqls_TableConstraint", None)
                    
                    if opp_val == self:
                        setattr(item, "sqls_TableConstraint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sqls_TableConstraint"):
                    opp_val = getattr(item, "sqls_TableConstraint", None)
                    
                    setattr(item, "sqls_TableConstraint", self)
                    

    @property
    def sqls_Table38(self):
        return self.__sqls_Table38

    @sqls_Table38.setter
    def sqls_Table38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqls_Table__sqls_Table38", None)
        self.__sqls_Table38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqls_SqlMethod37"):
                opp_val = getattr(old_value, "sqls_SqlMethod37", None)
                if opp_val == self:
                    setattr(old_value, "sqls_SqlMethod37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqls_SqlMethod37"):
                opp_val = getattr(value, "sqls_SqlMethod37", None)
                setattr(value, "sqls_SqlMethod37", self)

    @property
    def sqls_Table133(self):
        return self.__sqls_Table133

    @sqls_Table133.setter
    def sqls_Table133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqls_Table__sqls_Table133", None)
        self.__sqls_Table133 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqls_DeleteTable"):
                opp_val = getattr(old_value, "sqls_DeleteTable", None)
                if opp_val == self:
                    setattr(old_value, "sqls_DeleteTable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqls_DeleteTable"):
                opp_val = getattr(value, "sqls_DeleteTable", None)
                setattr(value, "sqls_DeleteTable", self)

    @property
    def sqls_Table86(self):
        return self.__sqls_Table86

    @sqls_Table86.setter
    def sqls_Table86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqls_Table__sqls_Table86", None)
        self.__sqls_Table86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqls_Update"):
                opp_val = getattr(old_value, "sqls_Update", None)
                if opp_val == self:
                    setattr(old_value, "sqls_Update", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqls_Update"):
                opp_val = getattr(value, "sqls_Update", None)
                setattr(value, "sqls_Update", self)

    @property
    def sqls_Table(self):
        return self.__sqls_Table

    @sqls_Table.setter
    def sqls_Table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqls_Table__sqls_Table", None)
        self.__sqls_Table = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqls_SqlLibrary9"):
                opp_val = getattr(old_value, "sqls_SqlLibrary9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqls_SqlLibrary9"):
                opp_val = getattr(value, "sqls_SqlLibrary9", None)
                if opp_val is None:
                    setattr(value, "sqls_SqlLibrary9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sqls_Table81(self):
        return self.__sqls_Table81

    @sqls_Table81.setter
    def sqls_Table81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqls_Table__sqls_Table81", None)
        self.__sqls_Table81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqls_Delete"):
                opp_val = getattr(old_value, "sqls_Delete", None)
                if opp_val == self:
                    setattr(old_value, "sqls_Delete", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqls_Delete"):
                opp_val = getattr(value, "sqls_Delete", None)
                setattr(value, "sqls_Delete", self)

    @property
    def sqls_Table65(self):
        return self.__sqls_Table65

    @sqls_Table65.setter
    def sqls_Table65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqls_Table__sqls_Table65", None)
        self.__sqls_Table65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqls_TableRef64"):
                opp_val = getattr(old_value, "sqls_TableRef64", None)
                if opp_val == self:
                    setattr(old_value, "sqls_TableRef64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqls_TableRef64"):
                opp_val = getattr(value, "sqls_TableRef64", None)
                setattr(value, "sqls_TableRef64", self)

    @property
    def sqls_Table22(self):
        return self.__sqls_Table22

    @sqls_Table22.setter
    def sqls_Table22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqls_Table__sqls_Table22", None)
        self.__sqls_Table22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sqls_Column"):
                    opp_val = getattr(item, "sqls_Column", None)
                    
                    if opp_val == self:
                        setattr(item, "sqls_Column", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sqls_Column"):
                    opp_val = getattr(item, "sqls_Column", None)
                    
                    setattr(item, "sqls_Column", self)
                    

    @property
    def sqls_Table71(self):
        return self.__sqls_Table71

    @sqls_Table71.setter
    def sqls_Table71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqls_Table__sqls_Table71", None)
        self.__sqls_Table71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqls_Insert"):
                opp_val = getattr(old_value, "sqls_Insert", None)
                if opp_val == self:
                    setattr(old_value, "sqls_Insert", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqls_Insert"):
                opp_val = getattr(value, "sqls_Insert", None)
                setattr(value, "sqls_Insert", self)

    @property
    def sqls_Table19(self):
        return self.__sqls_Table19

    @sqls_Table19.setter
    def sqls_Table19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqls_Table__sqls_Table19", None)
        self.__sqls_Table19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sqls_Tag20"):
                    opp_val = getattr(item, "sqls_Tag20", None)
                    
                    if opp_val == self:
                        setattr(item, "sqls_Tag20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sqls_Tag20"):
                    opp_val = getattr(item, "sqls_Tag20", None)
                    
                    setattr(item, "sqls_Tag20", self)
                    

    @property
    def sqls_Table73(self):
        return self.__sqls_Table73

    @sqls_Table73.setter
    def sqls_Table73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqls_Table__sqls_Table73", None)
        self.__sqls_Table73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqls_InsertStatement"):
                opp_val = getattr(old_value, "sqls_InsertStatement", None)
                if opp_val == self:
                    setattr(old_value, "sqls_InsertStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqls_InsertStatement"):
                opp_val = getattr(value, "sqls_InsertStatement", None)
                setattr(value, "sqls_InsertStatement", self)

class sqls_Type:

    pass
class sqls_Tag:

    def __init__(self, name: str, sqls_Tag35: "sqls_SqlMethod" = None, sqls_Tag102: "sqls_Trigger" = None, sqls_Tag: "sqls_SqlLibrary" = None, sqls_Tag20: "sqls_Table" = None):
        self.name = name
        self.sqls_Tag35 = sqls_Tag35
        self.sqls_Tag102 = sqls_Tag102
        self.sqls_Tag = sqls_Tag
        self.sqls_Tag20 = sqls_Tag20
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def sqls_Tag20(self):
        return self.__sqls_Tag20

    @sqls_Tag20.setter
    def sqls_Tag20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqls_Tag__sqls_Tag20", None)
        self.__sqls_Tag20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqls_Table19"):
                opp_val = getattr(old_value, "sqls_Table19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqls_Table19"):
                opp_val = getattr(value, "sqls_Table19", None)
                if opp_val is None:
                    setattr(value, "sqls_Table19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sqls_Tag35(self):
        return self.__sqls_Tag35

    @sqls_Tag35.setter
    def sqls_Tag35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqls_Tag__sqls_Tag35", None)
        self.__sqls_Tag35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqls_SqlMethod34"):
                opp_val = getattr(old_value, "sqls_SqlMethod34", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqls_SqlMethod34"):
                opp_val = getattr(value, "sqls_SqlMethod34", None)
                if opp_val is None:
                    setattr(value, "sqls_SqlMethod34", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sqls_Tag(self):
        return self.__sqls_Tag

    @sqls_Tag.setter
    def sqls_Tag(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqls_Tag__sqls_Tag", None)
        self.__sqls_Tag = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqls_SqlLibrary2"):
                opp_val = getattr(old_value, "sqls_SqlLibrary2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqls_SqlLibrary2"):
                opp_val = getattr(value, "sqls_SqlLibrary2", None)
                if opp_val is None:
                    setattr(value, "sqls_SqlLibrary2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sqls_Tag102(self):
        return self.__sqls_Tag102

    @sqls_Tag102.setter
    def sqls_Tag102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqls_Tag__sqls_Tag102", None)
        self.__sqls_Tag102 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqls_Trigger101"):
                opp_val = getattr(old_value, "sqls_Trigger101", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqls_Trigger101"):
                opp_val = getattr(value, "sqls_Trigger101", None)
                if opp_val is None:
                    setattr(value, "sqls_Trigger101", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sqls_Import:

    pass
class sqls_SqlLibrary:

    def __init__(self, database: str, version: int, sqls_SqlLibrary9: set["sqls_Table"] = None, sqls_SqlLibrary: set["sqls_Import"] = None, sqls_SqlLibrary2: set["sqls_Tag"] = None, sqls_SqlLibrary4: set["sqls_Type"] = None, sqls_SqlLibrary6: set["sqls_Type"] = None, sqls_SqlLibrary11: set["sqls_Trigger"] = None, sqls_SqlLibrary13: set["sqls_SqlMethod"] = None):
        self.database = database
        self.version = version
        self.sqls_SqlLibrary9 = sqls_SqlLibrary9 if sqls_SqlLibrary9 is not None else set()
        self.sqls_SqlLibrary = sqls_SqlLibrary if sqls_SqlLibrary is not None else set()
        self.sqls_SqlLibrary2 = sqls_SqlLibrary2 if sqls_SqlLibrary2 is not None else set()
        self.sqls_SqlLibrary4 = sqls_SqlLibrary4 if sqls_SqlLibrary4 is not None else set()
        self.sqls_SqlLibrary6 = sqls_SqlLibrary6 if sqls_SqlLibrary6 is not None else set()
        self.sqls_SqlLibrary11 = sqls_SqlLibrary11 if sqls_SqlLibrary11 is not None else set()
        self.sqls_SqlLibrary13 = sqls_SqlLibrary13 if sqls_SqlLibrary13 is not None else set()
        
        pass
    @property
    def database(self):
        return self.__database

    @database.setter
    def database(self, database: str):
        self.__database = database


    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, version: int):
        self.__version = version


    @property
    def sqls_SqlLibrary2(self):
        return self.__sqls_SqlLibrary2

    @sqls_SqlLibrary2.setter
    def sqls_SqlLibrary2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqls_SqlLibrary__sqls_SqlLibrary2", None)
        self.__sqls_SqlLibrary2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sqls_Tag"):
                    opp_val = getattr(item, "sqls_Tag", None)
                    
                    if opp_val == self:
                        setattr(item, "sqls_Tag", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sqls_Tag"):
                    opp_val = getattr(item, "sqls_Tag", None)
                    
                    setattr(item, "sqls_Tag", self)
                    

    @property
    def sqls_SqlLibrary11(self):
        return self.__sqls_SqlLibrary11

    @sqls_SqlLibrary11.setter
    def sqls_SqlLibrary11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqls_SqlLibrary__sqls_SqlLibrary11", None)
        self.__sqls_SqlLibrary11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sqls_Trigger"):
                    opp_val = getattr(item, "sqls_Trigger", None)
                    
                    if opp_val == self:
                        setattr(item, "sqls_Trigger", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sqls_Trigger"):
                    opp_val = getattr(item, "sqls_Trigger", None)
                    
                    setattr(item, "sqls_Trigger", self)
                    

    @property
    def sqls_SqlLibrary13(self):
        return self.__sqls_SqlLibrary13

    @sqls_SqlLibrary13.setter
    def sqls_SqlLibrary13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqls_SqlLibrary__sqls_SqlLibrary13", None)
        self.__sqls_SqlLibrary13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sqls_SqlMethod"):
                    opp_val = getattr(item, "sqls_SqlMethod", None)
                    
                    if opp_val == self:
                        setattr(item, "sqls_SqlMethod", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sqls_SqlMethod"):
                    opp_val = getattr(item, "sqls_SqlMethod", None)
                    
                    setattr(item, "sqls_SqlMethod", self)
                    

    @property
    def sqls_SqlLibrary6(self):
        return self.__sqls_SqlLibrary6

    @sqls_SqlLibrary6.setter
    def sqls_SqlLibrary6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqls_SqlLibrary__sqls_SqlLibrary6", None)
        self.__sqls_SqlLibrary6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sqls_Type7"):
                    opp_val = getattr(item, "sqls_Type7", None)
                    
                    if opp_val == self:
                        setattr(item, "sqls_Type7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sqls_Type7"):
                    opp_val = getattr(item, "sqls_Type7", None)
                    
                    setattr(item, "sqls_Type7", self)
                    

    @property
    def sqls_SqlLibrary(self):
        return self.__sqls_SqlLibrary

    @sqls_SqlLibrary.setter
    def sqls_SqlLibrary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqls_SqlLibrary__sqls_SqlLibrary", None)
        self.__sqls_SqlLibrary = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sqls_Import"):
                    opp_val = getattr(item, "sqls_Import", None)
                    
                    if opp_val == self:
                        setattr(item, "sqls_Import", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sqls_Import"):
                    opp_val = getattr(item, "sqls_Import", None)
                    
                    setattr(item, "sqls_Import", self)
                    

    @property
    def sqls_SqlLibrary9(self):
        return self.__sqls_SqlLibrary9

    @sqls_SqlLibrary9.setter
    def sqls_SqlLibrary9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqls_SqlLibrary__sqls_SqlLibrary9", None)
        self.__sqls_SqlLibrary9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sqls_Table"):
                    opp_val = getattr(item, "sqls_Table", None)
                    
                    if opp_val == self:
                        setattr(item, "sqls_Table", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sqls_Table"):
                    opp_val = getattr(item, "sqls_Table", None)
                    
                    setattr(item, "sqls_Table", self)
                    

    @property
    def sqls_SqlLibrary4(self):
        return self.__sqls_SqlLibrary4

    @sqls_SqlLibrary4.setter
    def sqls_SqlLibrary4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqls_SqlLibrary__sqls_SqlLibrary4", None)
        self.__sqls_SqlLibrary4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sqls_Type"):
                    opp_val = getattr(item, "sqls_Type", None)
                    
                    if opp_val == self:
                        setattr(item, "sqls_Type", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sqls_Type"):
                    opp_val = getattr(item, "sqls_Type", None)
                    
                    setattr(item, "sqls_Type", self)
                    
