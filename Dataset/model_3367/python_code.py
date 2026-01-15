from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class SqliteDataType(Enum):
    text = "text"
    integer = "integer"
    real = "real"
    blob = "blob"
    none = "none"
    numeric = "numeric"
class CompoundOperator(Enum):
    union = "union"
    intersect = "intersect"
    except = "except"
    unionall = "unionall"
class ConflictResolution(Enum):
    rollback = "rollback"
    abort = "abort"
    fail = "fail"
    ignore = "ignore"
    replace = "replace"
class ColumnType(Enum):
    text = "text"
    integer = "integer"
    real = "real"
    blob = "blob"
    boolean = "boolean"


############################################
# Definition of Classes
############################################

class ColumnConstraint:

    pass
class sqliteModel_UniqueConstraint(ColumnConstraint):

    pass
class sqliteModel_DefaultConstraint(ColumnConstraint):

    pass
class sqliteModel_NotNullConstraint(ColumnConstraint):

    pass
class sqliteModel_PrimaryKeyColumnConstraint(ColumnConstraint):

    def __init__(self, asc: bool, desc: bool, autoincrement: bool):
        self.asc = asc
        self.desc = desc
        self.autoincrement = autoincrement
        
    @property
    def desc(self) -> bool:
        return self.__desc

    @desc.setter
    def desc(self, desc: bool):
        self.__desc = desc

    @property
    def autoincrement(self) -> bool:
        return self.__autoincrement

    @autoincrement.setter
    def autoincrement(self, autoincrement: bool):
        self.__autoincrement = autoincrement

    @property
    def asc(self) -> bool:
        return self.__asc

    @asc.setter
    def asc(self, asc: bool):
        self.__asc = asc

class DefaultValue:

    pass
class sqliteModel_ExpressionDefaultValue(DefaultValue):

    pass
class sqliteModel_LiteralDefaultValue(DefaultValue):

    pass
class TableDefinition:

    pass
class sqliteModel_CreateTableStatement(TableDefinition):

    def __init__(self, temporary: bool, sqliteModel_CreateTableStatement: set["sqliteModel_ColumnSource"] = None, sqliteModel_CreateTableStatement222: set["sqliteModel_TableConstraint"] = None):
        self.temporary = temporary
        self.sqliteModel_CreateTableStatement = sqliteModel_CreateTableStatement if sqliteModel_CreateTableStatement is not None else set()
        self.sqliteModel_CreateTableStatement222 = sqliteModel_CreateTableStatement222 if sqliteModel_CreateTableStatement222 is not None else set()
        
    @property
    def temporary(self) -> bool:
        return self.__temporary

    @temporary.setter
    def temporary(self, temporary: bool):
        self.__temporary = temporary

    @property
    def sqliteModel_CreateTableStatement(self):
        return self.__sqliteModel_CreateTableStatement

    @sqliteModel_CreateTableStatement.setter
    def sqliteModel_CreateTableStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_CreateTableStatement__sqliteModel_CreateTableStatement", None)
        self.__sqliteModel_CreateTableStatement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sqliteModel_ColumnSource220"):
                    opp_val = getattr(item, "sqliteModel_ColumnSource220", None)
                    
                    if opp_val == self:
                        setattr(item, "sqliteModel_ColumnSource220", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sqliteModel_ColumnSource220"):
                    opp_val = getattr(item, "sqliteModel_ColumnSource220", None)
                    
                    setattr(item, "sqliteModel_ColumnSource220", self)
                    

    @property
    def sqliteModel_CreateTableStatement222(self):
        return self.__sqliteModel_CreateTableStatement222

    @sqliteModel_CreateTableStatement222.setter
    def sqliteModel_CreateTableStatement222(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_CreateTableStatement__sqliteModel_CreateTableStatement222", None)
        self.__sqliteModel_CreateTableStatement222 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sqliteModel_TableConstraint"):
                    opp_val = getattr(item, "sqliteModel_TableConstraint", None)
                    
                    if opp_val == self:
                        setattr(item, "sqliteModel_TableConstraint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sqliteModel_TableConstraint"):
                    opp_val = getattr(item, "sqliteModel_TableConstraint", None)
                    
                    setattr(item, "sqliteModel_TableConstraint", self)
                    

class sqliteModel_AlterTableRenameStatement(TableDefinition):

    pass
class ColumnSource:

    pass
class sqliteModel_ResultColumn(ColumnSource):

    pass
class SelectSource:

    pass
class sqliteModel_SingleSourceSelectStatement(SelectSource):

    pass
class sqliteModel_SingleSourceTable(SelectSource):

    pass
class LiteralValue:

    pass
class sqliteModel_CurrentTimeStampLiteral(LiteralValue):

    def __init__(self, literal: str):
        self.literal = literal
        
    @property
    def literal(self) -> str:
        return self.__literal

    @literal.setter
    def literal(self, literal: str):
        self.__literal = literal

class sqliteModel_CurrentTimeLiteral(LiteralValue):

    def __init__(self, literal: str):
        self.literal = literal
        
    @property
    def literal(self) -> str:
        return self.__literal

    @literal.setter
    def literal(self, literal: str):
        self.__literal = literal

class sqliteModel_CurrentDateLiteral(LiteralValue):

    def __init__(self, literal: str):
        self.literal = literal
        
    @property
    def literal(self) -> str:
        return self.__literal

    @literal.setter
    def literal(self, literal: str):
        self.__literal = literal

class sqliteModel_StringLiteral(LiteralValue):

    def __init__(self, literal: str):
        self.literal = literal
        
    @property
    def literal(self) -> str:
        return self.__literal

    @literal.setter
    def literal(self, literal: str):
        self.__literal = literal

class sqliteModel_NullLiteral(LiteralValue):

    def __init__(self, literal: str):
        self.literal = literal
        
    @property
    def literal(self) -> str:
        return self.__literal

    @literal.setter
    def literal(self, literal: str):
        self.__literal = literal

class sqliteModel_NumericLiteral(LiteralValue):

    def __init__(self, number: str):
        self.number = number
        
    @property
    def number(self) -> str:
        return self.__number

    @number.setter
    def number(self, number: str):
        self.__number = number

class SelectCoreExpression:

    pass
class sqliteModel_SelectExpression(SelectCoreExpression):

    def __init__(self, all: bool, allColumns: bool, distinct: bool, sqliteModel_SelectExpression: "sqliteModel_SelectList" = None, sqliteModel_SelectExpression202: "sqliteModel_JoinSource" = None, sqliteModel_SelectExpression205: "sqliteModel_WhereExpressions" = None, sqliteModel_SelectExpression208: "sqliteModel_GroupByExpressions" = None, sqliteModel_SelectExpression211: "sqliteModel_HavingExpressions" = None):
        self.all = all
        self.allColumns = allColumns
        self.distinct = distinct
        self.sqliteModel_SelectExpression = sqliteModel_SelectExpression
        self.sqliteModel_SelectExpression202 = sqliteModel_SelectExpression202
        self.sqliteModel_SelectExpression205 = sqliteModel_SelectExpression205
        self.sqliteModel_SelectExpression208 = sqliteModel_SelectExpression208
        self.sqliteModel_SelectExpression211 = sqliteModel_SelectExpression211
        
    @property
    def all(self) -> bool:
        return self.__all

    @all.setter
    def all(self, all: bool):
        self.__all = all

    @property
    def allColumns(self) -> bool:
        return self.__allColumns

    @allColumns.setter
    def allColumns(self, allColumns: bool):
        self.__allColumns = allColumns

    @property
    def distinct(self) -> bool:
        return self.__distinct

    @distinct.setter
    def distinct(self, distinct: bool):
        self.__distinct = distinct

    @property
    def sqliteModel_SelectExpression205(self):
        return self.__sqliteModel_SelectExpression205

    @sqliteModel_SelectExpression205.setter
    def sqliteModel_SelectExpression205(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_SelectExpression__sqliteModel_SelectExpression205", None)
        self.__sqliteModel_SelectExpression205 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_WhereExpressions206"):
                opp_val = getattr(old_value, "sqliteModel_WhereExpressions206", None)
                if opp_val == self:
                    setattr(old_value, "sqliteModel_WhereExpressions206", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_WhereExpressions206"):
                opp_val = getattr(value, "sqliteModel_WhereExpressions206", None)
                setattr(value, "sqliteModel_WhereExpressions206", self)

    @property
    def sqliteModel_SelectExpression211(self):
        return self.__sqliteModel_SelectExpression211

    @sqliteModel_SelectExpression211.setter
    def sqliteModel_SelectExpression211(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_SelectExpression__sqliteModel_SelectExpression211", None)
        self.__sqliteModel_SelectExpression211 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_HavingExpressions212"):
                opp_val = getattr(old_value, "sqliteModel_HavingExpressions212", None)
                if opp_val == self:
                    setattr(old_value, "sqliteModel_HavingExpressions212", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_HavingExpressions212"):
                opp_val = getattr(value, "sqliteModel_HavingExpressions212", None)
                setattr(value, "sqliteModel_HavingExpressions212", self)

    @property
    def sqliteModel_SelectExpression(self):
        return self.__sqliteModel_SelectExpression

    @sqliteModel_SelectExpression.setter
    def sqliteModel_SelectExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_SelectExpression__sqliteModel_SelectExpression", None)
        self.__sqliteModel_SelectExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_SelectList200"):
                opp_val = getattr(old_value, "sqliteModel_SelectList200", None)
                if opp_val == self:
                    setattr(old_value, "sqliteModel_SelectList200", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_SelectList200"):
                opp_val = getattr(value, "sqliteModel_SelectList200", None)
                setattr(value, "sqliteModel_SelectList200", self)

    @property
    def sqliteModel_SelectExpression208(self):
        return self.__sqliteModel_SelectExpression208

    @sqliteModel_SelectExpression208.setter
    def sqliteModel_SelectExpression208(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_SelectExpression__sqliteModel_SelectExpression208", None)
        self.__sqliteModel_SelectExpression208 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_GroupByExpressions209"):
                opp_val = getattr(old_value, "sqliteModel_GroupByExpressions209", None)
                if opp_val == self:
                    setattr(old_value, "sqliteModel_GroupByExpressions209", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_GroupByExpressions209"):
                opp_val = getattr(value, "sqliteModel_GroupByExpressions209", None)
                setattr(value, "sqliteModel_GroupByExpressions209", self)

    @property
    def sqliteModel_SelectExpression202(self):
        return self.__sqliteModel_SelectExpression202

    @sqliteModel_SelectExpression202.setter
    def sqliteModel_SelectExpression202(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_SelectExpression__sqliteModel_SelectExpression202", None)
        self.__sqliteModel_SelectExpression202 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_JoinSource203"):
                opp_val = getattr(old_value, "sqliteModel_JoinSource203", None)
                if opp_val == self:
                    setattr(old_value, "sqliteModel_JoinSource203", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_JoinSource203"):
                opp_val = getattr(value, "sqliteModel_JoinSource203", None)
                setattr(value, "sqliteModel_JoinSource203", self)

class sqliteModel_SelectCore(SelectCoreExpression):

    def __init__(self, op: str, sqliteModel_SelectCore: "sqliteModel_SelectCoreExpression" = None, sqliteModel_SelectCore197: "sqliteModel_SelectCoreExpression" = None):
        self.op = op
        self.sqliteModel_SelectCore = sqliteModel_SelectCore
        self.sqliteModel_SelectCore197 = sqliteModel_SelectCore197
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def sqliteModel_SelectCore(self):
        return self.__sqliteModel_SelectCore

    @sqliteModel_SelectCore.setter
    def sqliteModel_SelectCore(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_SelectCore__sqliteModel_SelectCore", None)
        self.__sqliteModel_SelectCore = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_SelectCoreExpression195"):
                opp_val = getattr(old_value, "sqliteModel_SelectCoreExpression195", None)
                if opp_val == self:
                    setattr(old_value, "sqliteModel_SelectCoreExpression195", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_SelectCoreExpression195"):
                opp_val = getattr(value, "sqliteModel_SelectCoreExpression195", None)
                setattr(value, "sqliteModel_SelectCoreExpression195", self)

    @property
    def sqliteModel_SelectCore197(self):
        return self.__sqliteModel_SelectCore197

    @sqliteModel_SelectCore197.setter
    def sqliteModel_SelectCore197(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_SelectCore__sqliteModel_SelectCore197", None)
        self.__sqliteModel_SelectCore197 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_SelectCoreExpression198"):
                opp_val = getattr(old_value, "sqliteModel_SelectCoreExpression198", None)
                if opp_val == self:
                    setattr(old_value, "sqliteModel_SelectCoreExpression198", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_SelectCoreExpression198"):
                opp_val = getattr(value, "sqliteModel_SelectCoreExpression198", None)
                setattr(value, "sqliteModel_SelectCoreExpression198", self)

class ContentUriSegment:

    pass
class sqliteModel_ContentUriParamSegment(ContentUriSegment):

    def __init__(self, num: bool, text: bool):
        self.num = num
        self.text = text
        
    @property
    def text(self) -> bool:
        return self.__text

    @text.setter
    def text(self, text: bool):
        self.__text = text

    @property
    def num(self) -> bool:
        return self.__num

    @num.setter
    def num(self, num: bool):
        self.__num = num

class sqliteModel_UpdateColumnExpression:

    pass
class Expression:

    pass
class sqliteModel_ExprBit(Expression):

    def __init__(self, op: str, sqliteModel_ExprBit: "sqliteModel_Expression" = None, sqliteModel_ExprBit142: "sqliteModel_Expression" = None):
        self.op = op
        self.sqliteModel_ExprBit = sqliteModel_ExprBit
        self.sqliteModel_ExprBit142 = sqliteModel_ExprBit142
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def sqliteModel_ExprBit142(self):
        return self.__sqliteModel_ExprBit142

    @sqliteModel_ExprBit142.setter
    def sqliteModel_ExprBit142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_ExprBit__sqliteModel_ExprBit142", None)
        self.__sqliteModel_ExprBit142 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_Expression143"):
                opp_val = getattr(old_value, "sqliteModel_Expression143", None)
                if opp_val == self:
                    setattr(old_value, "sqliteModel_Expression143", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_Expression143"):
                opp_val = getattr(value, "sqliteModel_Expression143", None)
                setattr(value, "sqliteModel_Expression143", self)

    @property
    def sqliteModel_ExprBit(self):
        return self.__sqliteModel_ExprBit

    @sqliteModel_ExprBit.setter
    def sqliteModel_ExprBit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_ExprBit__sqliteModel_ExprBit", None)
        self.__sqliteModel_ExprBit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_Expression140"):
                opp_val = getattr(old_value, "sqliteModel_Expression140", None)
                if opp_val == self:
                    setattr(old_value, "sqliteModel_Expression140", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_Expression140"):
                opp_val = getattr(value, "sqliteModel_Expression140", None)
                setattr(value, "sqliteModel_Expression140", self)

class sqliteModel_NotNull(Expression):

    pass
class sqliteModel_NullCheckExpression(Expression):

    pass
class sqliteModel_FunctionArgument(Expression):

    pass
class sqliteModel_ExprOr(Expression):

    def __init__(self, op: str, sqliteModel_ExprOr162: "sqliteModel_Expression" = None, sqliteModel_ExprOr: "sqliteModel_Expression" = None):
        self.op = op
        self.sqliteModel_ExprOr162 = sqliteModel_ExprOr162
        self.sqliteModel_ExprOr = sqliteModel_ExprOr
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def sqliteModel_ExprOr162(self):
        return self.__sqliteModel_ExprOr162

    @sqliteModel_ExprOr162.setter
    def sqliteModel_ExprOr162(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_ExprOr__sqliteModel_ExprOr162", None)
        self.__sqliteModel_ExprOr162 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_Expression163"):
                opp_val = getattr(old_value, "sqliteModel_Expression163", None)
                if opp_val == self:
                    setattr(old_value, "sqliteModel_Expression163", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_Expression163"):
                opp_val = getattr(value, "sqliteModel_Expression163", None)
                setattr(value, "sqliteModel_Expression163", self)

    @property
    def sqliteModel_ExprOr(self):
        return self.__sqliteModel_ExprOr

    @sqliteModel_ExprOr.setter
    def sqliteModel_ExprOr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_ExprOr__sqliteModel_ExprOr", None)
        self.__sqliteModel_ExprOr = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_Expression160"):
                opp_val = getattr(old_value, "sqliteModel_Expression160", None)
                if opp_val == self:
                    setattr(old_value, "sqliteModel_Expression160", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_Expression160"):
                opp_val = getattr(value, "sqliteModel_Expression160", None)
                setattr(value, "sqliteModel_Expression160", self)

class sqliteModel_ExprConcat(Expression):

    def __init__(self, op: str, sqliteModel_ExprConcat: "sqliteModel_Expression" = None, sqliteModel_ExprConcat127: "sqliteModel_Expression" = None):
        self.op = op
        self.sqliteModel_ExprConcat = sqliteModel_ExprConcat
        self.sqliteModel_ExprConcat127 = sqliteModel_ExprConcat127
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def sqliteModel_ExprConcat(self):
        return self.__sqliteModel_ExprConcat

    @sqliteModel_ExprConcat.setter
    def sqliteModel_ExprConcat(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_ExprConcat__sqliteModel_ExprConcat", None)
        self.__sqliteModel_ExprConcat = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_Expression125"):
                opp_val = getattr(old_value, "sqliteModel_Expression125", None)
                if opp_val == self:
                    setattr(old_value, "sqliteModel_Expression125", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_Expression125"):
                opp_val = getattr(value, "sqliteModel_Expression125", None)
                setattr(value, "sqliteModel_Expression125", self)

    @property
    def sqliteModel_ExprConcat127(self):
        return self.__sqliteModel_ExprConcat127

    @sqliteModel_ExprConcat127.setter
    def sqliteModel_ExprConcat127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_ExprConcat__sqliteModel_ExprConcat127", None)
        self.__sqliteModel_ExprConcat127 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_Expression128"):
                opp_val = getattr(old_value, "sqliteModel_Expression128", None)
                if opp_val == self:
                    setattr(old_value, "sqliteModel_Expression128", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_Expression128"):
                opp_val = getattr(value, "sqliteModel_Expression128", None)
                setattr(value, "sqliteModel_Expression128", self)

class sqliteModel_IsNull(Expression):

    pass
class sqliteModel_OldColumn(Expression):

    pass
class sqliteModel_NewColumn(Expression):

    pass
class sqliteModel_ExprRelate(Expression):

    def __init__(self, op: str, sqliteModel_ExprRelate: "sqliteModel_Expression" = None, sqliteModel_ExprRelate147: "sqliteModel_Expression" = None):
        self.op = op
        self.sqliteModel_ExprRelate = sqliteModel_ExprRelate
        self.sqliteModel_ExprRelate147 = sqliteModel_ExprRelate147
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def sqliteModel_ExprRelate(self):
        return self.__sqliteModel_ExprRelate

    @sqliteModel_ExprRelate.setter
    def sqliteModel_ExprRelate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_ExprRelate__sqliteModel_ExprRelate", None)
        self.__sqliteModel_ExprRelate = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_Expression145"):
                opp_val = getattr(old_value, "sqliteModel_Expression145", None)
                if opp_val == self:
                    setattr(old_value, "sqliteModel_Expression145", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_Expression145"):
                opp_val = getattr(value, "sqliteModel_Expression145", None)
                setattr(value, "sqliteModel_Expression145", self)

    @property
    def sqliteModel_ExprRelate147(self):
        return self.__sqliteModel_ExprRelate147

    @sqliteModel_ExprRelate147.setter
    def sqliteModel_ExprRelate147(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_ExprRelate__sqliteModel_ExprRelate147", None)
        self.__sqliteModel_ExprRelate147 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_Expression148"):
                opp_val = getattr(old_value, "sqliteModel_Expression148", None)
                if opp_val == self:
                    setattr(old_value, "sqliteModel_Expression148", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_Expression148"):
                opp_val = getattr(value, "sqliteModel_Expression148", None)
                setattr(value, "sqliteModel_Expression148", self)

class sqliteModel_SelectStatementExpression(Expression):

    def __init__(self, not: bool, exists: bool, sqliteModel_SelectStatementExpression: "sqliteModel_SelectStatement" = None):
        self.not = not
        self.exists = exists
        self.sqliteModel_SelectStatementExpression = sqliteModel_SelectStatementExpression
        
    @property
    def exists(self) -> bool:
        return self.__exists

    @exists.setter
    def exists(self, exists: bool):
        self.__exists = exists

    @property
    def not(self) -> bool:
        return self.__not

    @not.setter
    def not(self, not: bool):
        self.__not = not

    @property
    def sqliteModel_SelectStatementExpression(self):
        return self.__sqliteModel_SelectStatementExpression

    @sqliteModel_SelectStatementExpression.setter
    def sqliteModel_SelectStatementExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_SelectStatementExpression__sqliteModel_SelectStatementExpression", None)
        self.__sqliteModel_SelectStatementExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_SelectStatement181"):
                opp_val = getattr(old_value, "sqliteModel_SelectStatement181", None)
                if opp_val == self:
                    setattr(old_value, "sqliteModel_SelectStatement181", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_SelectStatement181"):
                opp_val = getattr(value, "sqliteModel_SelectStatement181", None)
                setattr(value, "sqliteModel_SelectStatement181", self)

class sqliteModel_ExprAnd(Expression):

    def __init__(self, op: str, sqliteModel_ExprAnd: "sqliteModel_Expression" = None, sqliteModel_ExprAnd157: "sqliteModel_Expression" = None):
        self.op = op
        self.sqliteModel_ExprAnd = sqliteModel_ExprAnd
        self.sqliteModel_ExprAnd157 = sqliteModel_ExprAnd157
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def sqliteModel_ExprAnd157(self):
        return self.__sqliteModel_ExprAnd157

    @sqliteModel_ExprAnd157.setter
    def sqliteModel_ExprAnd157(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_ExprAnd__sqliteModel_ExprAnd157", None)
        self.__sqliteModel_ExprAnd157 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_Expression158"):
                opp_val = getattr(old_value, "sqliteModel_Expression158", None)
                if opp_val == self:
                    setattr(old_value, "sqliteModel_Expression158", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_Expression158"):
                opp_val = getattr(value, "sqliteModel_Expression158", None)
                setattr(value, "sqliteModel_Expression158", self)

    @property
    def sqliteModel_ExprAnd(self):
        return self.__sqliteModel_ExprAnd

    @sqliteModel_ExprAnd.setter
    def sqliteModel_ExprAnd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_ExprAnd__sqliteModel_ExprAnd", None)
        self.__sqliteModel_ExprAnd = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_Expression155"):
                opp_val = getattr(old_value, "sqliteModel_Expression155", None)
                if opp_val == self:
                    setattr(old_value, "sqliteModel_Expression155", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_Expression155"):
                opp_val = getattr(value, "sqliteModel_Expression155", None)
                setattr(value, "sqliteModel_Expression155", self)

class sqliteModel_ColumnSourceRef(Expression):

    def __init__(self, all: bool, sqliteModel_ColumnSourceRef: "sqliteModel_SelectSource" = None, sqliteModel_ColumnSourceRef175: "sqliteModel_ColumnSource" = None):
        self.all = all
        self.sqliteModel_ColumnSourceRef = sqliteModel_ColumnSourceRef
        self.sqliteModel_ColumnSourceRef175 = sqliteModel_ColumnSourceRef175
        
    @property
    def all(self) -> bool:
        return self.__all

    @all.setter
    def all(self, all: bool):
        self.__all = all

    @property
    def sqliteModel_ColumnSourceRef175(self):
        return self.__sqliteModel_ColumnSourceRef175

    @sqliteModel_ColumnSourceRef175.setter
    def sqliteModel_ColumnSourceRef175(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_ColumnSourceRef__sqliteModel_ColumnSourceRef175", None)
        self.__sqliteModel_ColumnSourceRef175 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_ColumnSource176"):
                opp_val = getattr(old_value, "sqliteModel_ColumnSource176", None)
                if opp_val == self:
                    setattr(old_value, "sqliteModel_ColumnSource176", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_ColumnSource176"):
                opp_val = getattr(value, "sqliteModel_ColumnSource176", None)
                setattr(value, "sqliteModel_ColumnSource176", self)

    @property
    def sqliteModel_ColumnSourceRef(self):
        return self.__sqliteModel_ColumnSourceRef

    @sqliteModel_ColumnSourceRef.setter
    def sqliteModel_ColumnSourceRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_ColumnSourceRef__sqliteModel_ColumnSourceRef", None)
        self.__sqliteModel_ColumnSourceRef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_SelectSource"):
                opp_val = getattr(old_value, "sqliteModel_SelectSource", None)
                if opp_val == self:
                    setattr(old_value, "sqliteModel_SelectSource", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_SelectSource"):
                opp_val = getattr(value, "sqliteModel_SelectSource", None)
                setattr(value, "sqliteModel_SelectSource", self)

class sqliteModel_CaseExpression(Expression):

    pass
class sqliteModel_ExprEqual(Expression):

    def __init__(self, op: str, sqliteModel_ExprEqual: "sqliteModel_Expression" = None, sqliteModel_ExprEqual152: "sqliteModel_Expression" = None):
        self.op = op
        self.sqliteModel_ExprEqual = sqliteModel_ExprEqual
        self.sqliteModel_ExprEqual152 = sqliteModel_ExprEqual152
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def sqliteModel_ExprEqual(self):
        return self.__sqliteModel_ExprEqual

    @sqliteModel_ExprEqual.setter
    def sqliteModel_ExprEqual(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_ExprEqual__sqliteModel_ExprEqual", None)
        self.__sqliteModel_ExprEqual = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_Expression150"):
                opp_val = getattr(old_value, "sqliteModel_Expression150", None)
                if opp_val == self:
                    setattr(old_value, "sqliteModel_Expression150", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_Expression150"):
                opp_val = getattr(value, "sqliteModel_Expression150", None)
                setattr(value, "sqliteModel_Expression150", self)

    @property
    def sqliteModel_ExprEqual152(self):
        return self.__sqliteModel_ExprEqual152

    @sqliteModel_ExprEqual152.setter
    def sqliteModel_ExprEqual152(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_ExprEqual__sqliteModel_ExprEqual152", None)
        self.__sqliteModel_ExprEqual152 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_Expression153"):
                opp_val = getattr(old_value, "sqliteModel_Expression153", None)
                if opp_val == self:
                    setattr(old_value, "sqliteModel_Expression153", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_Expression153"):
                opp_val = getattr(value, "sqliteModel_Expression153", None)
                setattr(value, "sqliteModel_Expression153", self)

class sqliteModel_ExprAdd(Expression):

    def __init__(self, op: str, sqliteModel_ExprAdd137: "sqliteModel_Expression" = None, sqliteModel_ExprAdd: "sqliteModel_Expression" = None):
        self.op = op
        self.sqliteModel_ExprAdd137 = sqliteModel_ExprAdd137
        self.sqliteModel_ExprAdd = sqliteModel_ExprAdd
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def sqliteModel_ExprAdd137(self):
        return self.__sqliteModel_ExprAdd137

    @sqliteModel_ExprAdd137.setter
    def sqliteModel_ExprAdd137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_ExprAdd__sqliteModel_ExprAdd137", None)
        self.__sqliteModel_ExprAdd137 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_Expression138"):
                opp_val = getattr(old_value, "sqliteModel_Expression138", None)
                if opp_val == self:
                    setattr(old_value, "sqliteModel_Expression138", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_Expression138"):
                opp_val = getattr(value, "sqliteModel_Expression138", None)
                setattr(value, "sqliteModel_Expression138", self)

    @property
    def sqliteModel_ExprAdd(self):
        return self.__sqliteModel_ExprAdd

    @sqliteModel_ExprAdd.setter
    def sqliteModel_ExprAdd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_ExprAdd__sqliteModel_ExprAdd", None)
        self.__sqliteModel_ExprAdd = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_Expression135"):
                opp_val = getattr(old_value, "sqliteModel_Expression135", None)
                if opp_val == self:
                    setattr(old_value, "sqliteModel_Expression135", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_Expression135"):
                opp_val = getattr(value, "sqliteModel_Expression135", None)
                setattr(value, "sqliteModel_Expression135", self)

class sqliteModel_CastExpression(Expression):

    def __init__(self, type: str, sqliteModel_CastExpression: "sqliteModel_Expression" = None):
        self.type = type
        self.sqliteModel_CastExpression = sqliteModel_CastExpression
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def sqliteModel_CastExpression(self):
        return self.__sqliteModel_CastExpression

    @sqliteModel_CastExpression.setter
    def sqliteModel_CastExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_CastExpression__sqliteModel_CastExpression", None)
        self.__sqliteModel_CastExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_Expression191"):
                opp_val = getattr(old_value, "sqliteModel_Expression191", None)
                if opp_val == self:
                    setattr(old_value, "sqliteModel_Expression191", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_Expression191"):
                opp_val = getattr(value, "sqliteModel_Expression191", None)
                setattr(value, "sqliteModel_Expression191", self)

class sqliteModel_Literal(Expression):

    pass
class sqliteModel_NestedExpression(Expression):

    pass
class sqliteModel_ExprMult(Expression):

    def __init__(self, op: str, sqliteModel_ExprMult: "sqliteModel_Expression" = None, sqliteModel_ExprMult132: "sqliteModel_Expression" = None):
        self.op = op
        self.sqliteModel_ExprMult = sqliteModel_ExprMult
        self.sqliteModel_ExprMult132 = sqliteModel_ExprMult132
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def sqliteModel_ExprMult(self):
        return self.__sqliteModel_ExprMult

    @sqliteModel_ExprMult.setter
    def sqliteModel_ExprMult(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_ExprMult__sqliteModel_ExprMult", None)
        self.__sqliteModel_ExprMult = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_Expression130"):
                opp_val = getattr(old_value, "sqliteModel_Expression130", None)
                if opp_val == self:
                    setattr(old_value, "sqliteModel_Expression130", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_Expression130"):
                opp_val = getattr(value, "sqliteModel_Expression130", None)
                setattr(value, "sqliteModel_Expression130", self)

    @property
    def sqliteModel_ExprMult132(self):
        return self.__sqliteModel_ExprMult132

    @sqliteModel_ExprMult132.setter
    def sqliteModel_ExprMult132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_ExprMult__sqliteModel_ExprMult132", None)
        self.__sqliteModel_ExprMult132 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_Expression133"):
                opp_val = getattr(old_value, "sqliteModel_Expression133", None)
                if opp_val == self:
                    setattr(old_value, "sqliteModel_Expression133", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_Expression133"):
                opp_val = getattr(value, "sqliteModel_Expression133", None)
                setattr(value, "sqliteModel_Expression133", self)

class ConfigurationStatement:

    pass
class sqliteModel_Function(ConfigurationStatement, Expression):

    def __init__(self, all: bool, sqliteModel_Function: set["sqliteModel_FunctionArg"] = None, sqliteModel_Function119: "sqliteModel_SelectStatement" = None, sqliteModel_Function122: set["sqliteModel_Expression"] = None):
        self.all = all
        self.sqliteModel_Function = sqliteModel_Function if sqliteModel_Function is not None else set()
        self.sqliteModel_Function119 = sqliteModel_Function119
        self.sqliteModel_Function122 = sqliteModel_Function122 if sqliteModel_Function122 is not None else set()
        
    @property
    def all(self) -> bool:
        return self.__all

    @all.setter
    def all(self, all: bool):
        self.__all = all

    @property
    def sqliteModel_Function122(self):
        return self.__sqliteModel_Function122

    @sqliteModel_Function122.setter
    def sqliteModel_Function122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_Function__sqliteModel_Function122", None)
        self.__sqliteModel_Function122 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sqliteModel_Expression123"):
                    opp_val = getattr(item, "sqliteModel_Expression123", None)
                    
                    if opp_val == self:
                        setattr(item, "sqliteModel_Expression123", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sqliteModel_Expression123"):
                    opp_val = getattr(item, "sqliteModel_Expression123", None)
                    
                    setattr(item, "sqliteModel_Expression123", self)
                    

    @property
    def sqliteModel_Function119(self):
        return self.__sqliteModel_Function119

    @sqliteModel_Function119.setter
    def sqliteModel_Function119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_Function__sqliteModel_Function119", None)
        self.__sqliteModel_Function119 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_SelectStatement120"):
                opp_val = getattr(old_value, "sqliteModel_SelectStatement120", None)
                if opp_val == self:
                    setattr(old_value, "sqliteModel_SelectStatement120", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_SelectStatement120"):
                opp_val = getattr(value, "sqliteModel_SelectStatement120", None)
                setattr(value, "sqliteModel_SelectStatement120", self)

    @property
    def sqliteModel_Function(self):
        return self.__sqliteModel_Function

    @sqliteModel_Function.setter
    def sqliteModel_Function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_Function__sqliteModel_Function", None)
        self.__sqliteModel_Function = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sqliteModel_FunctionArg"):
                    opp_val = getattr(item, "sqliteModel_FunctionArg", None)
                    
                    if opp_val == self:
                        setattr(item, "sqliteModel_FunctionArg", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sqliteModel_FunctionArg"):
                    opp_val = getattr(item, "sqliteModel_FunctionArg", None)
                    
                    setattr(item, "sqliteModel_FunctionArg", self)
                    

class sqliteModel_ActionStatement(ConfigurationStatement):

    pass
class sqliteModel_DefaultValue:

    pass
class sqliteModel_ColumnDef(ColumnSource):

    def __init__(self, type: str, sqliteModel_ColumnDef: "sqliteModel_IndexedColumn" = None, sqliteModel_ColumnDef95: "sqliteModel_InsertStatement" = None, sqliteModel_ColumnDef111: "sqliteModel_UpdateColumnExpression" = None, sqliteModel_ColumnDef229: set["sqliteModel_ColumnConstraint"] = None):
        self.type = type
        self.sqliteModel_ColumnDef = sqliteModel_ColumnDef
        self.sqliteModel_ColumnDef95 = sqliteModel_ColumnDef95
        self.sqliteModel_ColumnDef111 = sqliteModel_ColumnDef111
        self.sqliteModel_ColumnDef229 = sqliteModel_ColumnDef229 if sqliteModel_ColumnDef229 is not None else set()
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def sqliteModel_ColumnDef(self):
        return self.__sqliteModel_ColumnDef

    @sqliteModel_ColumnDef.setter
    def sqliteModel_ColumnDef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_ColumnDef__sqliteModel_ColumnDef", None)
        self.__sqliteModel_ColumnDef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_IndexedColumn85"):
                opp_val = getattr(old_value, "sqliteModel_IndexedColumn85", None)
                if opp_val == self:
                    setattr(old_value, "sqliteModel_IndexedColumn85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_IndexedColumn85"):
                opp_val = getattr(value, "sqliteModel_IndexedColumn85", None)
                setattr(value, "sqliteModel_IndexedColumn85", self)

    @property
    def sqliteModel_ColumnDef95(self):
        return self.__sqliteModel_ColumnDef95

    @sqliteModel_ColumnDef95.setter
    def sqliteModel_ColumnDef95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_ColumnDef__sqliteModel_ColumnDef95", None)
        self.__sqliteModel_ColumnDef95 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_InsertStatement94"):
                opp_val = getattr(old_value, "sqliteModel_InsertStatement94", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_InsertStatement94"):
                opp_val = getattr(value, "sqliteModel_InsertStatement94", None)
                if opp_val is None:
                    setattr(value, "sqliteModel_InsertStatement94", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sqliteModel_ColumnDef111(self):
        return self.__sqliteModel_ColumnDef111

    @sqliteModel_ColumnDef111.setter
    def sqliteModel_ColumnDef111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_ColumnDef__sqliteModel_ColumnDef111", None)
        self.__sqliteModel_ColumnDef111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_UpdateColumnExpression110"):
                opp_val = getattr(old_value, "sqliteModel_UpdateColumnExpression110", None)
                if opp_val == self:
                    setattr(old_value, "sqliteModel_UpdateColumnExpression110", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_UpdateColumnExpression110"):
                opp_val = getattr(value, "sqliteModel_UpdateColumnExpression110", None)
                setattr(value, "sqliteModel_UpdateColumnExpression110", self)

    @property
    def sqliteModel_ColumnDef229(self):
        return self.__sqliteModel_ColumnDef229

    @sqliteModel_ColumnDef229.setter
    def sqliteModel_ColumnDef229(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_ColumnDef__sqliteModel_ColumnDef229", None)
        self.__sqliteModel_ColumnDef229 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sqliteModel_ColumnConstraint"):
                    opp_val = getattr(item, "sqliteModel_ColumnConstraint", None)
                    
                    if opp_val == self:
                        setattr(item, "sqliteModel_ColumnConstraint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sqliteModel_ColumnConstraint"):
                    opp_val = getattr(item, "sqliteModel_ColumnConstraint", None)
                    
                    setattr(item, "sqliteModel_ColumnConstraint", self)
                    

class sqliteModel_ConflictClause:

    def __init__(self, resolution: str, sqliteModel_ConflictClause: "sqliteModel_UniqueTableConstraint" = None, sqliteModel_ConflictClause81: "sqliteModel_PrimaryConstraint" = None, sqliteModel_ConflictClause231: "sqliteModel_NotNullConstraint" = None, sqliteModel_ConflictClause233: "sqliteModel_UniqueConstraint" = None):
        self.resolution = resolution
        self.sqliteModel_ConflictClause = sqliteModel_ConflictClause
        self.sqliteModel_ConflictClause81 = sqliteModel_ConflictClause81
        self.sqliteModel_ConflictClause231 = sqliteModel_ConflictClause231
        self.sqliteModel_ConflictClause233 = sqliteModel_ConflictClause233
        
    @property
    def resolution(self) -> str:
        return self.__resolution

    @resolution.setter
    def resolution(self, resolution: str):
        self.__resolution = resolution

    @property
    def sqliteModel_ConflictClause231(self):
        return self.__sqliteModel_ConflictClause231

    @sqliteModel_ConflictClause231.setter
    def sqliteModel_ConflictClause231(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_ConflictClause__sqliteModel_ConflictClause231", None)
        self.__sqliteModel_ConflictClause231 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_NotNullConstraint"):
                opp_val = getattr(old_value, "sqliteModel_NotNullConstraint", None)
                if opp_val == self:
                    setattr(old_value, "sqliteModel_NotNullConstraint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_NotNullConstraint"):
                opp_val = getattr(value, "sqliteModel_NotNullConstraint", None)
                setattr(value, "sqliteModel_NotNullConstraint", self)

    @property
    def sqliteModel_ConflictClause233(self):
        return self.__sqliteModel_ConflictClause233

    @sqliteModel_ConflictClause233.setter
    def sqliteModel_ConflictClause233(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_ConflictClause__sqliteModel_ConflictClause233", None)
        self.__sqliteModel_ConflictClause233 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_UniqueConstraint"):
                opp_val = getattr(old_value, "sqliteModel_UniqueConstraint", None)
                if opp_val == self:
                    setattr(old_value, "sqliteModel_UniqueConstraint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_UniqueConstraint"):
                opp_val = getattr(value, "sqliteModel_UniqueConstraint", None)
                setattr(value, "sqliteModel_UniqueConstraint", self)

    @property
    def sqliteModel_ConflictClause81(self):
        return self.__sqliteModel_ConflictClause81

    @sqliteModel_ConflictClause81.setter
    def sqliteModel_ConflictClause81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_ConflictClause__sqliteModel_ConflictClause81", None)
        self.__sqliteModel_ConflictClause81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_PrimaryConstraint80"):
                opp_val = getattr(old_value, "sqliteModel_PrimaryConstraint80", None)
                if opp_val == self:
                    setattr(old_value, "sqliteModel_PrimaryConstraint80", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_PrimaryConstraint80"):
                opp_val = getattr(value, "sqliteModel_PrimaryConstraint80", None)
                setattr(value, "sqliteModel_PrimaryConstraint80", self)

    @property
    def sqliteModel_ConflictClause(self):
        return self.__sqliteModel_ConflictClause

    @sqliteModel_ConflictClause.setter
    def sqliteModel_ConflictClause(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_ConflictClause__sqliteModel_ConflictClause", None)
        self.__sqliteModel_ConflictClause = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_UniqueTableConstraint76"):
                opp_val = getattr(old_value, "sqliteModel_UniqueTableConstraint76", None)
                if opp_val == self:
                    setattr(old_value, "sqliteModel_UniqueTableConstraint76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_UniqueTableConstraint76"):
                opp_val = getattr(value, "sqliteModel_UniqueTableConstraint76", None)
                setattr(value, "sqliteModel_UniqueTableConstraint76", self)

class TableConstraint:

    pass
class sqliteModel_CheckTableConstraint(TableConstraint):

    pass
class sqliteModel_PrimaryConstraint(TableConstraint):

    pass
class sqliteModel_UniqueTableConstraint(TableConstraint):

    pass
class sqliteModel_DMLStatement:

    pass
class sqliteModel_TableConstraint:

    def __init__(self, name: str, sqliteModel_TableConstraint: "sqliteModel_CreateTableStatement" = None):
        self.name = name
        self.sqliteModel_TableConstraint = sqliteModel_TableConstraint
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def sqliteModel_TableConstraint(self):
        return self.__sqliteModel_TableConstraint

    @sqliteModel_TableConstraint.setter
    def sqliteModel_TableConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_TableConstraint__sqliteModel_TableConstraint", None)
        self.__sqliteModel_TableConstraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_CreateTableStatement222"):
                opp_val = getattr(old_value, "sqliteModel_CreateTableStatement222", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_CreateTableStatement222"):
                opp_val = getattr(value, "sqliteModel_CreateTableStatement222", None)
                if opp_val is None:
                    setattr(value, "sqliteModel_CreateTableStatement222", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sqliteModel_ColumnConstraint:

    pass
class sqliteModel_IndexedColumn:

    def __init__(self, collationName: str, asc: bool, desc: bool, sqliteModel_IndexedColumn: "sqliteModel_CreateIndexStatement" = None, sqliteModel_IndexedColumn74: "sqliteModel_UniqueTableConstraint" = None, sqliteModel_IndexedColumn78: "sqliteModel_PrimaryConstraint" = None, sqliteModel_IndexedColumn85: "sqliteModel_ColumnDef" = None):
        self.collationName = collationName
        self.asc = asc
        self.desc = desc
        self.sqliteModel_IndexedColumn = sqliteModel_IndexedColumn
        self.sqliteModel_IndexedColumn74 = sqliteModel_IndexedColumn74
        self.sqliteModel_IndexedColumn78 = sqliteModel_IndexedColumn78
        self.sqliteModel_IndexedColumn85 = sqliteModel_IndexedColumn85
        
    @property
    def collationName(self) -> str:
        return self.__collationName

    @collationName.setter
    def collationName(self, collationName: str):
        self.__collationName = collationName

    @property
    def asc(self) -> bool:
        return self.__asc

    @asc.setter
    def asc(self, asc: bool):
        self.__asc = asc

    @property
    def desc(self) -> bool:
        return self.__desc

    @desc.setter
    def desc(self, desc: bool):
        self.__desc = desc

    @property
    def sqliteModel_IndexedColumn85(self):
        return self.__sqliteModel_IndexedColumn85

    @sqliteModel_IndexedColumn85.setter
    def sqliteModel_IndexedColumn85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_IndexedColumn__sqliteModel_IndexedColumn85", None)
        self.__sqliteModel_IndexedColumn85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_ColumnDef"):
                opp_val = getattr(old_value, "sqliteModel_ColumnDef", None)
                if opp_val == self:
                    setattr(old_value, "sqliteModel_ColumnDef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_ColumnDef"):
                opp_val = getattr(value, "sqliteModel_ColumnDef", None)
                setattr(value, "sqliteModel_ColumnDef", self)

    @property
    def sqliteModel_IndexedColumn74(self):
        return self.__sqliteModel_IndexedColumn74

    @sqliteModel_IndexedColumn74.setter
    def sqliteModel_IndexedColumn74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_IndexedColumn__sqliteModel_IndexedColumn74", None)
        self.__sqliteModel_IndexedColumn74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_UniqueTableConstraint"):
                opp_val = getattr(old_value, "sqliteModel_UniqueTableConstraint", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_UniqueTableConstraint"):
                opp_val = getattr(value, "sqliteModel_UniqueTableConstraint", None)
                if opp_val is None:
                    setattr(value, "sqliteModel_UniqueTableConstraint", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sqliteModel_IndexedColumn(self):
        return self.__sqliteModel_IndexedColumn

    @sqliteModel_IndexedColumn.setter
    def sqliteModel_IndexedColumn(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_IndexedColumn__sqliteModel_IndexedColumn", None)
        self.__sqliteModel_IndexedColumn = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_CreateIndexStatement70"):
                opp_val = getattr(old_value, "sqliteModel_CreateIndexStatement70", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_CreateIndexStatement70"):
                opp_val = getattr(value, "sqliteModel_CreateIndexStatement70", None)
                if opp_val is None:
                    setattr(value, "sqliteModel_CreateIndexStatement70", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sqliteModel_IndexedColumn78(self):
        return self.__sqliteModel_IndexedColumn78

    @sqliteModel_IndexedColumn78.setter
    def sqliteModel_IndexedColumn78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_IndexedColumn__sqliteModel_IndexedColumn78", None)
        self.__sqliteModel_IndexedColumn78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_PrimaryConstraint"):
                opp_val = getattr(old_value, "sqliteModel_PrimaryConstraint", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_PrimaryConstraint"):
                opp_val = getattr(value, "sqliteModel_PrimaryConstraint", None)
                if opp_val is None:
                    setattr(value, "sqliteModel_PrimaryConstraint", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sqliteModel_CreateViewStatement(TableDefinition):

    def __init__(self, temporary: bool, sqliteModel_CreateViewStatement: "sqliteModel_DropViewStatement" = None, sqliteModel_CreateViewStatement224: "sqliteModel_SelectStatement" = None):
        self.temporary = temporary
        self.sqliteModel_CreateViewStatement = sqliteModel_CreateViewStatement
        self.sqliteModel_CreateViewStatement224 = sqliteModel_CreateViewStatement224
        
    @property
    def temporary(self) -> bool:
        return self.__temporary

    @temporary.setter
    def temporary(self, temporary: bool):
        self.__temporary = temporary

    @property
    def sqliteModel_CreateViewStatement(self):
        return self.__sqliteModel_CreateViewStatement

    @sqliteModel_CreateViewStatement.setter
    def sqliteModel_CreateViewStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_CreateViewStatement__sqliteModel_CreateViewStatement", None)
        self.__sqliteModel_CreateViewStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_DropViewStatement"):
                opp_val = getattr(old_value, "sqliteModel_DropViewStatement", None)
                if opp_val == self:
                    setattr(old_value, "sqliteModel_DropViewStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_DropViewStatement"):
                opp_val = getattr(value, "sqliteModel_DropViewStatement", None)
                setattr(value, "sqliteModel_DropViewStatement", self)

    @property
    def sqliteModel_CreateViewStatement224(self):
        return self.__sqliteModel_CreateViewStatement224

    @sqliteModel_CreateViewStatement224.setter
    def sqliteModel_CreateViewStatement224(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_CreateViewStatement__sqliteModel_CreateViewStatement224", None)
        self.__sqliteModel_CreateViewStatement224 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_SelectStatement225"):
                opp_val = getattr(old_value, "sqliteModel_SelectStatement225", None)
                if opp_val == self:
                    setattr(old_value, "sqliteModel_SelectStatement225", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_SelectStatement225"):
                opp_val = getattr(value, "sqliteModel_SelectStatement225", None)
                setattr(value, "sqliteModel_SelectStatement225", self)

class DDLStatement:

    pass
class sqliteModel_CreateIndexStatement(DDLStatement):

    def __init__(self, unique: bool, name: str, sqliteModel_CreateIndexStatement: "sqliteModel_TableDefinition" = None, sqliteModel_CreateIndexStatement70: set["sqliteModel_IndexedColumn"] = None, sqliteModel_CreateIndexStatement72: "sqliteModel_DropIndexStatement" = None):
        self.unique = unique
        self.name = name
        self.sqliteModel_CreateIndexStatement = sqliteModel_CreateIndexStatement
        self.sqliteModel_CreateIndexStatement70 = sqliteModel_CreateIndexStatement70 if sqliteModel_CreateIndexStatement70 is not None else set()
        self.sqliteModel_CreateIndexStatement72 = sqliteModel_CreateIndexStatement72
        
    @property
    def unique(self) -> bool:
        return self.__unique

    @unique.setter
    def unique(self, unique: bool):
        self.__unique = unique

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def sqliteModel_CreateIndexStatement70(self):
        return self.__sqliteModel_CreateIndexStatement70

    @sqliteModel_CreateIndexStatement70.setter
    def sqliteModel_CreateIndexStatement70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_CreateIndexStatement__sqliteModel_CreateIndexStatement70", None)
        self.__sqliteModel_CreateIndexStatement70 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sqliteModel_IndexedColumn"):
                    opp_val = getattr(item, "sqliteModel_IndexedColumn", None)
                    
                    if opp_val == self:
                        setattr(item, "sqliteModel_IndexedColumn", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sqliteModel_IndexedColumn"):
                    opp_val = getattr(item, "sqliteModel_IndexedColumn", None)
                    
                    setattr(item, "sqliteModel_IndexedColumn", self)
                    

    @property
    def sqliteModel_CreateIndexStatement(self):
        return self.__sqliteModel_CreateIndexStatement

    @sqliteModel_CreateIndexStatement.setter
    def sqliteModel_CreateIndexStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_CreateIndexStatement__sqliteModel_CreateIndexStatement", None)
        self.__sqliteModel_CreateIndexStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_TableDefinition68"):
                opp_val = getattr(old_value, "sqliteModel_TableDefinition68", None)
                if opp_val == self:
                    setattr(old_value, "sqliteModel_TableDefinition68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_TableDefinition68"):
                opp_val = getattr(value, "sqliteModel_TableDefinition68", None)
                setattr(value, "sqliteModel_TableDefinition68", self)

    @property
    def sqliteModel_CreateIndexStatement72(self):
        return self.__sqliteModel_CreateIndexStatement72

    @sqliteModel_CreateIndexStatement72.setter
    def sqliteModel_CreateIndexStatement72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_CreateIndexStatement__sqliteModel_CreateIndexStatement72", None)
        self.__sqliteModel_CreateIndexStatement72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_DropIndexStatement"):
                opp_val = getattr(old_value, "sqliteModel_DropIndexStatement", None)
                if opp_val == self:
                    setattr(old_value, "sqliteModel_DropIndexStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_DropIndexStatement"):
                opp_val = getattr(value, "sqliteModel_DropIndexStatement", None)
                setattr(value, "sqliteModel_DropIndexStatement", self)

class sqliteModel_CreateTriggerStatement(DDLStatement):

    def __init__(self, temporary: bool, name: str, when: str, eventType: str, updateColumnNames: str, forEachRow: str, sqliteModel_CreateTriggerStatement65: "sqliteModel_DropTriggerStatement" = None, sqliteModel_CreateTriggerStatement: "sqliteModel_TableDefinition" = None, sqliteModel_CreateTriggerStatement53: "sqliteModel_Expression" = None, sqliteModel_CreateTriggerStatement56: set["sqliteModel_DMLStatement"] = None):
        self.temporary = temporary
        self.name = name
        self.when = when
        self.eventType = eventType
        self.updateColumnNames = updateColumnNames
        self.forEachRow = forEachRow
        self.sqliteModel_CreateTriggerStatement65 = sqliteModel_CreateTriggerStatement65
        self.sqliteModel_CreateTriggerStatement = sqliteModel_CreateTriggerStatement
        self.sqliteModel_CreateTriggerStatement53 = sqliteModel_CreateTriggerStatement53
        self.sqliteModel_CreateTriggerStatement56 = sqliteModel_CreateTriggerStatement56 if sqliteModel_CreateTriggerStatement56 is not None else set()
        
    @property
    def when(self) -> str:
        return self.__when

    @when.setter
    def when(self, when: str):
        self.__when = when

    @property
    def eventType(self) -> str:
        return self.__eventType

    @eventType.setter
    def eventType(self, eventType: str):
        self.__eventType = eventType

    @property
    def updateColumnNames(self) -> str:
        return self.__updateColumnNames

    @updateColumnNames.setter
    def updateColumnNames(self, updateColumnNames: str):
        self.__updateColumnNames = updateColumnNames

    @property
    def forEachRow(self) -> str:
        return self.__forEachRow

    @forEachRow.setter
    def forEachRow(self, forEachRow: str):
        self.__forEachRow = forEachRow

    @property
    def temporary(self) -> bool:
        return self.__temporary

    @temporary.setter
    def temporary(self, temporary: bool):
        self.__temporary = temporary

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def sqliteModel_CreateTriggerStatement56(self):
        return self.__sqliteModel_CreateTriggerStatement56

    @sqliteModel_CreateTriggerStatement56.setter
    def sqliteModel_CreateTriggerStatement56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_CreateTriggerStatement__sqliteModel_CreateTriggerStatement56", None)
        self.__sqliteModel_CreateTriggerStatement56 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sqliteModel_DMLStatement"):
                    opp_val = getattr(item, "sqliteModel_DMLStatement", None)
                    
                    if opp_val == self:
                        setattr(item, "sqliteModel_DMLStatement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sqliteModel_DMLStatement"):
                    opp_val = getattr(item, "sqliteModel_DMLStatement", None)
                    
                    setattr(item, "sqliteModel_DMLStatement", self)
                    

    @property
    def sqliteModel_CreateTriggerStatement53(self):
        return self.__sqliteModel_CreateTriggerStatement53

    @sqliteModel_CreateTriggerStatement53.setter
    def sqliteModel_CreateTriggerStatement53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_CreateTriggerStatement__sqliteModel_CreateTriggerStatement53", None)
        self.__sqliteModel_CreateTriggerStatement53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_Expression54"):
                opp_val = getattr(old_value, "sqliteModel_Expression54", None)
                if opp_val == self:
                    setattr(old_value, "sqliteModel_Expression54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_Expression54"):
                opp_val = getattr(value, "sqliteModel_Expression54", None)
                setattr(value, "sqliteModel_Expression54", self)

    @property
    def sqliteModel_CreateTriggerStatement(self):
        return self.__sqliteModel_CreateTriggerStatement

    @sqliteModel_CreateTriggerStatement.setter
    def sqliteModel_CreateTriggerStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_CreateTriggerStatement__sqliteModel_CreateTriggerStatement", None)
        self.__sqliteModel_CreateTriggerStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_TableDefinition"):
                opp_val = getattr(old_value, "sqliteModel_TableDefinition", None)
                if opp_val == self:
                    setattr(old_value, "sqliteModel_TableDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_TableDefinition"):
                opp_val = getattr(value, "sqliteModel_TableDefinition", None)
                setattr(value, "sqliteModel_TableDefinition", self)

    @property
    def sqliteModel_CreateTriggerStatement65(self):
        return self.__sqliteModel_CreateTriggerStatement65

    @sqliteModel_CreateTriggerStatement65.setter
    def sqliteModel_CreateTriggerStatement65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_CreateTriggerStatement__sqliteModel_CreateTriggerStatement65", None)
        self.__sqliteModel_CreateTriggerStatement65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_DropTriggerStatement"):
                opp_val = getattr(old_value, "sqliteModel_DropTriggerStatement", None)
                if opp_val == self:
                    setattr(old_value, "sqliteModel_DropTriggerStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_DropTriggerStatement"):
                opp_val = getattr(value, "sqliteModel_DropTriggerStatement", None)
                setattr(value, "sqliteModel_DropTriggerStatement", self)

class sqliteModel_DropIndexStatement(DDLStatement):

    def __init__(self, ifExists: bool, sqliteModel_DropIndexStatement: "sqliteModel_CreateIndexStatement" = None):
        self.ifExists = ifExists
        self.sqliteModel_DropIndexStatement = sqliteModel_DropIndexStatement
        
    @property
    def ifExists(self) -> bool:
        return self.__ifExists

    @ifExists.setter
    def ifExists(self, ifExists: bool):
        self.__ifExists = ifExists

    @property
    def sqliteModel_DropIndexStatement(self):
        return self.__sqliteModel_DropIndexStatement

    @sqliteModel_DropIndexStatement.setter
    def sqliteModel_DropIndexStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_DropIndexStatement__sqliteModel_DropIndexStatement", None)
        self.__sqliteModel_DropIndexStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_CreateIndexStatement72"):
                opp_val = getattr(old_value, "sqliteModel_CreateIndexStatement72", None)
                if opp_val == self:
                    setattr(old_value, "sqliteModel_CreateIndexStatement72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_CreateIndexStatement72"):
                opp_val = getattr(value, "sqliteModel_CreateIndexStatement72", None)
                setattr(value, "sqliteModel_CreateIndexStatement72", self)

class sqliteModel_DropViewStatement(DDLStatement):

    def __init__(self, ifExists: bool, sqliteModel_DropViewStatement: "sqliteModel_CreateViewStatement" = None):
        self.ifExists = ifExists
        self.sqliteModel_DropViewStatement = sqliteModel_DropViewStatement
        
    @property
    def ifExists(self) -> bool:
        return self.__ifExists

    @ifExists.setter
    def ifExists(self, ifExists: bool):
        self.__ifExists = ifExists

    @property
    def sqliteModel_DropViewStatement(self):
        return self.__sqliteModel_DropViewStatement

    @sqliteModel_DropViewStatement.setter
    def sqliteModel_DropViewStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_DropViewStatement__sqliteModel_DropViewStatement", None)
        self.__sqliteModel_DropViewStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_CreateViewStatement"):
                opp_val = getattr(old_value, "sqliteModel_CreateViewStatement", None)
                if opp_val == self:
                    setattr(old_value, "sqliteModel_CreateViewStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_CreateViewStatement"):
                opp_val = getattr(value, "sqliteModel_CreateViewStatement", None)
                setattr(value, "sqliteModel_CreateViewStatement", self)

class sqliteModel_AlterTableAddColumnStatement(DDLStatement):

    pass
class sqliteModel_DropTriggerStatement(DDLStatement):

    def __init__(self, ifExists: bool, sqliteModel_DropTriggerStatement: "sqliteModel_CreateTriggerStatement" = None):
        self.ifExists = ifExists
        self.sqliteModel_DropTriggerStatement = sqliteModel_DropTriggerStatement
        
    @property
    def ifExists(self) -> bool:
        return self.__ifExists

    @ifExists.setter
    def ifExists(self, ifExists: bool):
        self.__ifExists = ifExists

    @property
    def sqliteModel_DropTriggerStatement(self):
        return self.__sqliteModel_DropTriggerStatement

    @sqliteModel_DropTriggerStatement.setter
    def sqliteModel_DropTriggerStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_DropTriggerStatement__sqliteModel_DropTriggerStatement", None)
        self.__sqliteModel_DropTriggerStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_CreateTriggerStatement65"):
                opp_val = getattr(old_value, "sqliteModel_CreateTriggerStatement65", None)
                if opp_val == self:
                    setattr(old_value, "sqliteModel_CreateTriggerStatement65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_CreateTriggerStatement65"):
                opp_val = getattr(value, "sqliteModel_CreateTriggerStatement65", None)
                setattr(value, "sqliteModel_CreateTriggerStatement65", self)

class sqliteModel_DropTableStatement(DDLStatement):

    def __init__(self, ifExists: bool, sqliteModel_DropTableStatement: "sqliteModel_TableDefinition" = None):
        self.ifExists = ifExists
        self.sqliteModel_DropTableStatement = sqliteModel_DropTableStatement
        
    @property
    def ifExists(self) -> bool:
        return self.__ifExists

    @ifExists.setter
    def ifExists(self, ifExists: bool):
        self.__ifExists = ifExists

    @property
    def sqliteModel_DropTableStatement(self):
        return self.__sqliteModel_DropTableStatement

    @sqliteModel_DropTableStatement.setter
    def sqliteModel_DropTableStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_DropTableStatement__sqliteModel_DropTableStatement", None)
        self.__sqliteModel_DropTableStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_TableDefinition63"):
                opp_val = getattr(old_value, "sqliteModel_TableDefinition63", None)
                if opp_val == self:
                    setattr(old_value, "sqliteModel_TableDefinition63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_TableDefinition63"):
                opp_val = getattr(value, "sqliteModel_TableDefinition63", None)
                setattr(value, "sqliteModel_TableDefinition63", self)

class sqliteModel_TableDefinition(DDLStatement):

    def __init__(self, name: str, sqliteModel_TableDefinition68: "sqliteModel_CreateIndexStatement" = None, sqliteModel_TableDefinition: "sqliteModel_CreateTriggerStatement" = None, sqliteModel_TableDefinition58: "sqliteModel_AlterTableAddColumnStatement" = None, sqliteModel_TableDefinition63: "sqliteModel_DropTableStatement" = None, sqliteModel_TableDefinition87: "sqliteModel_DeleteStatement" = None, sqliteModel_TableDefinition92: "sqliteModel_InsertStatement" = None, sqliteModel_TableDefinition103: "sqliteModel_UpdateStatement" = None, sqliteModel_TableDefinition214: "sqliteModel_SingleSourceTable" = None, sqliteModel_TableDefinition227: "sqliteModel_AlterTableRenameStatement" = None):
        self.name = name
        self.sqliteModel_TableDefinition68 = sqliteModel_TableDefinition68
        self.sqliteModel_TableDefinition = sqliteModel_TableDefinition
        self.sqliteModel_TableDefinition58 = sqliteModel_TableDefinition58
        self.sqliteModel_TableDefinition63 = sqliteModel_TableDefinition63
        self.sqliteModel_TableDefinition87 = sqliteModel_TableDefinition87
        self.sqliteModel_TableDefinition92 = sqliteModel_TableDefinition92
        self.sqliteModel_TableDefinition103 = sqliteModel_TableDefinition103
        self.sqliteModel_TableDefinition214 = sqliteModel_TableDefinition214
        self.sqliteModel_TableDefinition227 = sqliteModel_TableDefinition227
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def sqliteModel_TableDefinition103(self):
        return self.__sqliteModel_TableDefinition103

    @sqliteModel_TableDefinition103.setter
    def sqliteModel_TableDefinition103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_TableDefinition__sqliteModel_TableDefinition103", None)
        self.__sqliteModel_TableDefinition103 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_UpdateStatement"):
                opp_val = getattr(old_value, "sqliteModel_UpdateStatement", None)
                if opp_val == self:
                    setattr(old_value, "sqliteModel_UpdateStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_UpdateStatement"):
                opp_val = getattr(value, "sqliteModel_UpdateStatement", None)
                setattr(value, "sqliteModel_UpdateStatement", self)

    @property
    def sqliteModel_TableDefinition68(self):
        return self.__sqliteModel_TableDefinition68

    @sqliteModel_TableDefinition68.setter
    def sqliteModel_TableDefinition68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_TableDefinition__sqliteModel_TableDefinition68", None)
        self.__sqliteModel_TableDefinition68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_CreateIndexStatement"):
                opp_val = getattr(old_value, "sqliteModel_CreateIndexStatement", None)
                if opp_val == self:
                    setattr(old_value, "sqliteModel_CreateIndexStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_CreateIndexStatement"):
                opp_val = getattr(value, "sqliteModel_CreateIndexStatement", None)
                setattr(value, "sqliteModel_CreateIndexStatement", self)

    @property
    def sqliteModel_TableDefinition58(self):
        return self.__sqliteModel_TableDefinition58

    @sqliteModel_TableDefinition58.setter
    def sqliteModel_TableDefinition58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_TableDefinition__sqliteModel_TableDefinition58", None)
        self.__sqliteModel_TableDefinition58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_AlterTableAddColumnStatement"):
                opp_val = getattr(old_value, "sqliteModel_AlterTableAddColumnStatement", None)
                if opp_val == self:
                    setattr(old_value, "sqliteModel_AlterTableAddColumnStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_AlterTableAddColumnStatement"):
                opp_val = getattr(value, "sqliteModel_AlterTableAddColumnStatement", None)
                setattr(value, "sqliteModel_AlterTableAddColumnStatement", self)

    @property
    def sqliteModel_TableDefinition(self):
        return self.__sqliteModel_TableDefinition

    @sqliteModel_TableDefinition.setter
    def sqliteModel_TableDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_TableDefinition__sqliteModel_TableDefinition", None)
        self.__sqliteModel_TableDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_CreateTriggerStatement"):
                opp_val = getattr(old_value, "sqliteModel_CreateTriggerStatement", None)
                if opp_val == self:
                    setattr(old_value, "sqliteModel_CreateTriggerStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_CreateTriggerStatement"):
                opp_val = getattr(value, "sqliteModel_CreateTriggerStatement", None)
                setattr(value, "sqliteModel_CreateTriggerStatement", self)

    @property
    def sqliteModel_TableDefinition92(self):
        return self.__sqliteModel_TableDefinition92

    @sqliteModel_TableDefinition92.setter
    def sqliteModel_TableDefinition92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_TableDefinition__sqliteModel_TableDefinition92", None)
        self.__sqliteModel_TableDefinition92 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_InsertStatement"):
                opp_val = getattr(old_value, "sqliteModel_InsertStatement", None)
                if opp_val == self:
                    setattr(old_value, "sqliteModel_InsertStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_InsertStatement"):
                opp_val = getattr(value, "sqliteModel_InsertStatement", None)
                setattr(value, "sqliteModel_InsertStatement", self)

    @property
    def sqliteModel_TableDefinition214(self):
        return self.__sqliteModel_TableDefinition214

    @sqliteModel_TableDefinition214.setter
    def sqliteModel_TableDefinition214(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_TableDefinition__sqliteModel_TableDefinition214", None)
        self.__sqliteModel_TableDefinition214 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_SingleSourceTable"):
                opp_val = getattr(old_value, "sqliteModel_SingleSourceTable", None)
                if opp_val == self:
                    setattr(old_value, "sqliteModel_SingleSourceTable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_SingleSourceTable"):
                opp_val = getattr(value, "sqliteModel_SingleSourceTable", None)
                setattr(value, "sqliteModel_SingleSourceTable", self)

    @property
    def sqliteModel_TableDefinition87(self):
        return self.__sqliteModel_TableDefinition87

    @sqliteModel_TableDefinition87.setter
    def sqliteModel_TableDefinition87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_TableDefinition__sqliteModel_TableDefinition87", None)
        self.__sqliteModel_TableDefinition87 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_DeleteStatement"):
                opp_val = getattr(old_value, "sqliteModel_DeleteStatement", None)
                if opp_val == self:
                    setattr(old_value, "sqliteModel_DeleteStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_DeleteStatement"):
                opp_val = getattr(value, "sqliteModel_DeleteStatement", None)
                setattr(value, "sqliteModel_DeleteStatement", self)

    @property
    def sqliteModel_TableDefinition63(self):
        return self.__sqliteModel_TableDefinition63

    @sqliteModel_TableDefinition63.setter
    def sqliteModel_TableDefinition63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_TableDefinition__sqliteModel_TableDefinition63", None)
        self.__sqliteModel_TableDefinition63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_DropTableStatement"):
                opp_val = getattr(old_value, "sqliteModel_DropTableStatement", None)
                if opp_val == self:
                    setattr(old_value, "sqliteModel_DropTableStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_DropTableStatement"):
                opp_val = getattr(value, "sqliteModel_DropTableStatement", None)
                setattr(value, "sqliteModel_DropTableStatement", self)

    @property
    def sqliteModel_TableDefinition227(self):
        return self.__sqliteModel_TableDefinition227

    @sqliteModel_TableDefinition227.setter
    def sqliteModel_TableDefinition227(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_TableDefinition__sqliteModel_TableDefinition227", None)
        self.__sqliteModel_TableDefinition227 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_AlterTableRenameStatement"):
                opp_val = getattr(old_value, "sqliteModel_AlterTableRenameStatement", None)
                if opp_val == self:
                    setattr(old_value, "sqliteModel_AlterTableRenameStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_AlterTableRenameStatement"):
                opp_val = getattr(value, "sqliteModel_AlterTableRenameStatement", None)
                setattr(value, "sqliteModel_AlterTableRenameStatement", self)

class sqliteModel_LiteralValue:

    pass
class SingleSource:

    pass
class sqliteModel_SingleSourceJoin(SingleSource):

    pass
class sqliteModel_SelectSource(SingleSource):

    def __init__(self, name: str, sqliteModel_SelectSource: "sqliteModel_ColumnSourceRef" = None):
        self.name = name
        self.sqliteModel_SelectSource = sqliteModel_SelectSource
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def sqliteModel_SelectSource(self):
        return self.__sqliteModel_SelectSource

    @sqliteModel_SelectSource.setter
    def sqliteModel_SelectSource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_SelectSource__sqliteModel_SelectSource", None)
        self.__sqliteModel_SelectSource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_ColumnSourceRef"):
                opp_val = getattr(old_value, "sqliteModel_ColumnSourceRef", None)
                if opp_val == self:
                    setattr(old_value, "sqliteModel_ColumnSourceRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_ColumnSourceRef"):
                opp_val = getattr(value, "sqliteModel_ColumnSourceRef", None)
                setattr(value, "sqliteModel_ColumnSourceRef", self)

class sqliteModel_JoinStatement:

    def __init__(self, natural: bool, left: bool, outer: bool, inner: bool, cross: bool, sqliteModel_JoinStatement: "sqliteModel_JoinSource" = None, sqliteModel_JoinStatement46: "sqliteModel_SingleSource" = None, sqliteModel_JoinStatement49: "sqliteModel_Expression" = None):
        self.natural = natural
        self.left = left
        self.outer = outer
        self.inner = inner
        self.cross = cross
        self.sqliteModel_JoinStatement = sqliteModel_JoinStatement
        self.sqliteModel_JoinStatement46 = sqliteModel_JoinStatement46
        self.sqliteModel_JoinStatement49 = sqliteModel_JoinStatement49
        
    @property
    def outer(self) -> bool:
        return self.__outer

    @outer.setter
    def outer(self, outer: bool):
        self.__outer = outer

    @property
    def left(self) -> bool:
        return self.__left

    @left.setter
    def left(self, left: bool):
        self.__left = left

    @property
    def cross(self) -> bool:
        return self.__cross

    @cross.setter
    def cross(self, cross: bool):
        self.__cross = cross

    @property
    def natural(self) -> bool:
        return self.__natural

    @natural.setter
    def natural(self, natural: bool):
        self.__natural = natural

    @property
    def inner(self) -> bool:
        return self.__inner

    @inner.setter
    def inner(self, inner: bool):
        self.__inner = inner

    @property
    def sqliteModel_JoinStatement49(self):
        return self.__sqliteModel_JoinStatement49

    @sqliteModel_JoinStatement49.setter
    def sqliteModel_JoinStatement49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_JoinStatement__sqliteModel_JoinStatement49", None)
        self.__sqliteModel_JoinStatement49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_Expression50"):
                opp_val = getattr(old_value, "sqliteModel_Expression50", None)
                if opp_val == self:
                    setattr(old_value, "sqliteModel_Expression50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_Expression50"):
                opp_val = getattr(value, "sqliteModel_Expression50", None)
                setattr(value, "sqliteModel_Expression50", self)

    @property
    def sqliteModel_JoinStatement(self):
        return self.__sqliteModel_JoinStatement

    @sqliteModel_JoinStatement.setter
    def sqliteModel_JoinStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_JoinStatement__sqliteModel_JoinStatement", None)
        self.__sqliteModel_JoinStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_JoinSource42"):
                opp_val = getattr(old_value, "sqliteModel_JoinSource42", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_JoinSource42"):
                opp_val = getattr(value, "sqliteModel_JoinSource42", None)
                if opp_val is None:
                    setattr(value, "sqliteModel_JoinSource42", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sqliteModel_JoinStatement46(self):
        return self.__sqliteModel_JoinStatement46

    @sqliteModel_JoinStatement46.setter
    def sqliteModel_JoinStatement46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_JoinStatement__sqliteModel_JoinStatement46", None)
        self.__sqliteModel_JoinStatement46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_SingleSource47"):
                opp_val = getattr(old_value, "sqliteModel_SingleSource47", None)
                if opp_val == self:
                    setattr(old_value, "sqliteModel_SingleSource47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_SingleSource47"):
                opp_val = getattr(value, "sqliteModel_SingleSource47", None)
                setattr(value, "sqliteModel_SingleSource47", self)

class sqliteModel_HavingExpressions:

    pass
class sqliteModel_GroupByExpressions:

    pass
class sqliteModel_WhereExpressions:

    pass
class sqliteModel_ColumnSource:

    def __init__(self, name: str, sqliteModel_ColumnSource: "sqliteModel_SelectList" = None, sqliteModel_ColumnSource61: "sqliteModel_AlterTableAddColumnStatement" = None, sqliteModel_ColumnSource170: "sqliteModel_NewColumn" = None, sqliteModel_ColumnSource172: "sqliteModel_OldColumn" = None, sqliteModel_ColumnSource176: "sqliteModel_ColumnSourceRef" = None, sqliteModel_ColumnSource220: "sqliteModel_CreateTableStatement" = None):
        self.name = name
        self.sqliteModel_ColumnSource = sqliteModel_ColumnSource
        self.sqliteModel_ColumnSource61 = sqliteModel_ColumnSource61
        self.sqliteModel_ColumnSource170 = sqliteModel_ColumnSource170
        self.sqliteModel_ColumnSource172 = sqliteModel_ColumnSource172
        self.sqliteModel_ColumnSource176 = sqliteModel_ColumnSource176
        self.sqliteModel_ColumnSource220 = sqliteModel_ColumnSource220
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def sqliteModel_ColumnSource170(self):
        return self.__sqliteModel_ColumnSource170

    @sqliteModel_ColumnSource170.setter
    def sqliteModel_ColumnSource170(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_ColumnSource__sqliteModel_ColumnSource170", None)
        self.__sqliteModel_ColumnSource170 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_NewColumn"):
                opp_val = getattr(old_value, "sqliteModel_NewColumn", None)
                if opp_val == self:
                    setattr(old_value, "sqliteModel_NewColumn", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_NewColumn"):
                opp_val = getattr(value, "sqliteModel_NewColumn", None)
                setattr(value, "sqliteModel_NewColumn", self)

    @property
    def sqliteModel_ColumnSource220(self):
        return self.__sqliteModel_ColumnSource220

    @sqliteModel_ColumnSource220.setter
    def sqliteModel_ColumnSource220(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_ColumnSource__sqliteModel_ColumnSource220", None)
        self.__sqliteModel_ColumnSource220 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_CreateTableStatement"):
                opp_val = getattr(old_value, "sqliteModel_CreateTableStatement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_CreateTableStatement"):
                opp_val = getattr(value, "sqliteModel_CreateTableStatement", None)
                if opp_val is None:
                    setattr(value, "sqliteModel_CreateTableStatement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sqliteModel_ColumnSource(self):
        return self.__sqliteModel_ColumnSource

    @sqliteModel_ColumnSource.setter
    def sqliteModel_ColumnSource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_ColumnSource__sqliteModel_ColumnSource", None)
        self.__sqliteModel_ColumnSource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_SelectList"):
                opp_val = getattr(old_value, "sqliteModel_SelectList", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_SelectList"):
                opp_val = getattr(value, "sqliteModel_SelectList", None)
                if opp_val is None:
                    setattr(value, "sqliteModel_SelectList", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sqliteModel_ColumnSource176(self):
        return self.__sqliteModel_ColumnSource176

    @sqliteModel_ColumnSource176.setter
    def sqliteModel_ColumnSource176(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_ColumnSource__sqliteModel_ColumnSource176", None)
        self.__sqliteModel_ColumnSource176 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_ColumnSourceRef175"):
                opp_val = getattr(old_value, "sqliteModel_ColumnSourceRef175", None)
                if opp_val == self:
                    setattr(old_value, "sqliteModel_ColumnSourceRef175", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_ColumnSourceRef175"):
                opp_val = getattr(value, "sqliteModel_ColumnSourceRef175", None)
                setattr(value, "sqliteModel_ColumnSourceRef175", self)

    @property
    def sqliteModel_ColumnSource172(self):
        return self.__sqliteModel_ColumnSource172

    @sqliteModel_ColumnSource172.setter
    def sqliteModel_ColumnSource172(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_ColumnSource__sqliteModel_ColumnSource172", None)
        self.__sqliteModel_ColumnSource172 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_OldColumn"):
                opp_val = getattr(old_value, "sqliteModel_OldColumn", None)
                if opp_val == self:
                    setattr(old_value, "sqliteModel_OldColumn", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_OldColumn"):
                opp_val = getattr(value, "sqliteModel_OldColumn", None)
                setattr(value, "sqliteModel_OldColumn", self)

    @property
    def sqliteModel_ColumnSource61(self):
        return self.__sqliteModel_ColumnSource61

    @sqliteModel_ColumnSource61.setter
    def sqliteModel_ColumnSource61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_ColumnSource__sqliteModel_ColumnSource61", None)
        self.__sqliteModel_ColumnSource61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_AlterTableAddColumnStatement60"):
                opp_val = getattr(old_value, "sqliteModel_AlterTableAddColumnStatement60", None)
                if opp_val == self:
                    setattr(old_value, "sqliteModel_AlterTableAddColumnStatement60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_AlterTableAddColumnStatement60"):
                opp_val = getattr(value, "sqliteModel_AlterTableAddColumnStatement60", None)
                setattr(value, "sqliteModel_AlterTableAddColumnStatement60", self)

class sqliteModel_SelectList:

    pass
class sqliteModel_SingleSource:

    pass
class sqliteModel_JoinSource:

    pass
class sqliteModel_Case:

    pass
class sqliteModel_Expression:

    pass
class sqliteModel_ContentUriSegment:

    def __init__(self, name: str, sqliteModel_ContentUriSegment: "sqliteModel_ContentUri" = None):
        self.name = name
        self.sqliteModel_ContentUriSegment = sqliteModel_ContentUriSegment
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def sqliteModel_ContentUriSegment(self):
        return self.__sqliteModel_ContentUriSegment

    @sqliteModel_ContentUriSegment.setter
    def sqliteModel_ContentUriSegment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_ContentUriSegment__sqliteModel_ContentUriSegment", None)
        self.__sqliteModel_ContentUriSegment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_ContentUri"):
                opp_val = getattr(old_value, "sqliteModel_ContentUri", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_ContentUri"):
                opp_val = getattr(value, "sqliteModel_ContentUri", None)
                if opp_val is None:
                    setattr(value, "sqliteModel_ContentUri", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sqliteModel_ContentUri:

    def __init__(self, type: str, sqliteModel_ContentUri: set["sqliteModel_ContentUriSegment"] = None, sqliteModel_ContentUri116: "sqliteModel_ActionStatement" = None):
        self.type = type
        self.sqliteModel_ContentUri = sqliteModel_ContentUri if sqliteModel_ContentUri is not None else set()
        self.sqliteModel_ContentUri116 = sqliteModel_ContentUri116
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def sqliteModel_ContentUri116(self):
        return self.__sqliteModel_ContentUri116

    @sqliteModel_ContentUri116.setter
    def sqliteModel_ContentUri116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_ContentUri__sqliteModel_ContentUri116", None)
        self.__sqliteModel_ContentUri116 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_ActionStatement"):
                opp_val = getattr(old_value, "sqliteModel_ActionStatement", None)
                if opp_val == self:
                    setattr(old_value, "sqliteModel_ActionStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_ActionStatement"):
                opp_val = getattr(value, "sqliteModel_ActionStatement", None)
                setattr(value, "sqliteModel_ActionStatement", self)

    @property
    def sqliteModel_ContentUri(self):
        return self.__sqliteModel_ContentUri

    @sqliteModel_ContentUri.setter
    def sqliteModel_ContentUri(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_ContentUri__sqliteModel_ContentUri", None)
        self.__sqliteModel_ContentUri = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sqliteModel_ContentUriSegment"):
                    opp_val = getattr(item, "sqliteModel_ContentUriSegment", None)
                    
                    if opp_val == self:
                        setattr(item, "sqliteModel_ContentUriSegment", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sqliteModel_ContentUriSegment"):
                    opp_val = getattr(item, "sqliteModel_ContentUriSegment", None)
                    
                    setattr(item, "sqliteModel_ContentUriSegment", self)
                    

class sqliteModel_OrderingTerm:

    def __init__(self, asc: bool, desc: bool, sqliteModel_OrderingTerm: "sqliteModel_OrderingTermList" = None, sqliteModel_OrderingTerm38: "sqliteModel_Expression" = None):
        self.asc = asc
        self.desc = desc
        self.sqliteModel_OrderingTerm = sqliteModel_OrderingTerm
        self.sqliteModel_OrderingTerm38 = sqliteModel_OrderingTerm38
        
    @property
    def asc(self) -> bool:
        return self.__asc

    @asc.setter
    def asc(self, asc: bool):
        self.__asc = asc

    @property
    def desc(self) -> bool:
        return self.__desc

    @desc.setter
    def desc(self, desc: bool):
        self.__desc = desc

    @property
    def sqliteModel_OrderingTerm(self):
        return self.__sqliteModel_OrderingTerm

    @sqliteModel_OrderingTerm.setter
    def sqliteModel_OrderingTerm(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_OrderingTerm__sqliteModel_OrderingTerm", None)
        self.__sqliteModel_OrderingTerm = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_OrderingTermList29"):
                opp_val = getattr(old_value, "sqliteModel_OrderingTermList29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_OrderingTermList29"):
                opp_val = getattr(value, "sqliteModel_OrderingTermList29", None)
                if opp_val is None:
                    setattr(value, "sqliteModel_OrderingTermList29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sqliteModel_OrderingTerm38(self):
        return self.__sqliteModel_OrderingTerm38

    @sqliteModel_OrderingTerm38.setter
    def sqliteModel_OrderingTerm38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_OrderingTerm__sqliteModel_OrderingTerm38", None)
        self.__sqliteModel_OrderingTerm38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_Expression39"):
                opp_val = getattr(old_value, "sqliteModel_Expression39", None)
                if opp_val == self:
                    setattr(old_value, "sqliteModel_Expression39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_Expression39"):
                opp_val = getattr(value, "sqliteModel_Expression39", None)
                setattr(value, "sqliteModel_Expression39", self)

class sqliteModel_OrderingTermList:

    pass
class sqliteModel_SelectCoreExpression:

    pass
class DMLStatement:

    pass
class sqliteModel_UpdateStatement(DMLStatement):

    def __init__(self, conflictResolution: str, sqliteModel_UpdateStatement: "sqliteModel_TableDefinition" = None, sqliteModel_UpdateStatement105: set["sqliteModel_UpdateColumnExpression"] = None, sqliteModel_UpdateStatement107: "sqliteModel_Expression" = None):
        self.conflictResolution = conflictResolution
        self.sqliteModel_UpdateStatement = sqliteModel_UpdateStatement
        self.sqliteModel_UpdateStatement105 = sqliteModel_UpdateStatement105 if sqliteModel_UpdateStatement105 is not None else set()
        self.sqliteModel_UpdateStatement107 = sqliteModel_UpdateStatement107
        
    @property
    def conflictResolution(self) -> str:
        return self.__conflictResolution

    @conflictResolution.setter
    def conflictResolution(self, conflictResolution: str):
        self.__conflictResolution = conflictResolution

    @property
    def sqliteModel_UpdateStatement107(self):
        return self.__sqliteModel_UpdateStatement107

    @sqliteModel_UpdateStatement107.setter
    def sqliteModel_UpdateStatement107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_UpdateStatement__sqliteModel_UpdateStatement107", None)
        self.__sqliteModel_UpdateStatement107 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_Expression108"):
                opp_val = getattr(old_value, "sqliteModel_Expression108", None)
                if opp_val == self:
                    setattr(old_value, "sqliteModel_Expression108", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_Expression108"):
                opp_val = getattr(value, "sqliteModel_Expression108", None)
                setattr(value, "sqliteModel_Expression108", self)

    @property
    def sqliteModel_UpdateStatement105(self):
        return self.__sqliteModel_UpdateStatement105

    @sqliteModel_UpdateStatement105.setter
    def sqliteModel_UpdateStatement105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_UpdateStatement__sqliteModel_UpdateStatement105", None)
        self.__sqliteModel_UpdateStatement105 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sqliteModel_UpdateColumnExpression"):
                    opp_val = getattr(item, "sqliteModel_UpdateColumnExpression", None)
                    
                    if opp_val == self:
                        setattr(item, "sqliteModel_UpdateColumnExpression", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sqliteModel_UpdateColumnExpression"):
                    opp_val = getattr(item, "sqliteModel_UpdateColumnExpression", None)
                    
                    setattr(item, "sqliteModel_UpdateColumnExpression", self)
                    

    @property
    def sqliteModel_UpdateStatement(self):
        return self.__sqliteModel_UpdateStatement

    @sqliteModel_UpdateStatement.setter
    def sqliteModel_UpdateStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_UpdateStatement__sqliteModel_UpdateStatement", None)
        self.__sqliteModel_UpdateStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_TableDefinition103"):
                opp_val = getattr(old_value, "sqliteModel_TableDefinition103", None)
                if opp_val == self:
                    setattr(old_value, "sqliteModel_TableDefinition103", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_TableDefinition103"):
                opp_val = getattr(value, "sqliteModel_TableDefinition103", None)
                setattr(value, "sqliteModel_TableDefinition103", self)

class sqliteModel_DeleteStatement(DMLStatement):

    pass
class sqliteModel_InsertStatement(DMLStatement):

    def __init__(self, conflictResolution: str, sqliteModel_InsertStatement: "sqliteModel_TableDefinition" = None, sqliteModel_InsertStatement94: set["sqliteModel_ColumnDef"] = None, sqliteModel_InsertStatement97: set["sqliteModel_Expression"] = None, sqliteModel_InsertStatement100: "sqliteModel_SelectStatement" = None):
        self.conflictResolution = conflictResolution
        self.sqliteModel_InsertStatement = sqliteModel_InsertStatement
        self.sqliteModel_InsertStatement94 = sqliteModel_InsertStatement94 if sqliteModel_InsertStatement94 is not None else set()
        self.sqliteModel_InsertStatement97 = sqliteModel_InsertStatement97 if sqliteModel_InsertStatement97 is not None else set()
        self.sqliteModel_InsertStatement100 = sqliteModel_InsertStatement100
        
    @property
    def conflictResolution(self) -> str:
        return self.__conflictResolution

    @conflictResolution.setter
    def conflictResolution(self, conflictResolution: str):
        self.__conflictResolution = conflictResolution

    @property
    def sqliteModel_InsertStatement97(self):
        return self.__sqliteModel_InsertStatement97

    @sqliteModel_InsertStatement97.setter
    def sqliteModel_InsertStatement97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_InsertStatement__sqliteModel_InsertStatement97", None)
        self.__sqliteModel_InsertStatement97 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sqliteModel_Expression98"):
                    opp_val = getattr(item, "sqliteModel_Expression98", None)
                    
                    if opp_val == self:
                        setattr(item, "sqliteModel_Expression98", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sqliteModel_Expression98"):
                    opp_val = getattr(item, "sqliteModel_Expression98", None)
                    
                    setattr(item, "sqliteModel_Expression98", self)
                    

    @property
    def sqliteModel_InsertStatement(self):
        return self.__sqliteModel_InsertStatement

    @sqliteModel_InsertStatement.setter
    def sqliteModel_InsertStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_InsertStatement__sqliteModel_InsertStatement", None)
        self.__sqliteModel_InsertStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_TableDefinition92"):
                opp_val = getattr(old_value, "sqliteModel_TableDefinition92", None)
                if opp_val == self:
                    setattr(old_value, "sqliteModel_TableDefinition92", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_TableDefinition92"):
                opp_val = getattr(value, "sqliteModel_TableDefinition92", None)
                setattr(value, "sqliteModel_TableDefinition92", self)

    @property
    def sqliteModel_InsertStatement94(self):
        return self.__sqliteModel_InsertStatement94

    @sqliteModel_InsertStatement94.setter
    def sqliteModel_InsertStatement94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_InsertStatement__sqliteModel_InsertStatement94", None)
        self.__sqliteModel_InsertStatement94 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sqliteModel_ColumnDef95"):
                    opp_val = getattr(item, "sqliteModel_ColumnDef95", None)
                    
                    if opp_val == self:
                        setattr(item, "sqliteModel_ColumnDef95", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sqliteModel_ColumnDef95"):
                    opp_val = getattr(item, "sqliteModel_ColumnDef95", None)
                    
                    setattr(item, "sqliteModel_ColumnDef95", self)
                    

    @property
    def sqliteModel_InsertStatement100(self):
        return self.__sqliteModel_InsertStatement100

    @sqliteModel_InsertStatement100.setter
    def sqliteModel_InsertStatement100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_InsertStatement__sqliteModel_InsertStatement100", None)
        self.__sqliteModel_InsertStatement100 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_SelectStatement101"):
                opp_val = getattr(old_value, "sqliteModel_SelectStatement101", None)
                if opp_val == self:
                    setattr(old_value, "sqliteModel_SelectStatement101", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_SelectStatement101"):
                opp_val = getattr(value, "sqliteModel_SelectStatement101", None)
                setattr(value, "sqliteModel_SelectStatement101", self)

class sqliteModel_SelectStatement(DMLStatement):

    pass
class sqliteModel_InitBlock:

    pass
class sqliteModel_ConfigBlock:

    pass
class sqliteModel_DatabaseBlock:

    def __init__(self, name: str, sqliteModel_DatabaseBlock6: set["sqliteModel_MigrationBlock"] = None, sqliteModel_DatabaseBlock: "sqliteModel_Model" = None, sqliteModel_DatabaseBlock2: "sqliteModel_ConfigBlock" = None, sqliteModel_DatabaseBlock4: "sqliteModel_InitBlock" = None):
        self.name = name
        self.sqliteModel_DatabaseBlock6 = sqliteModel_DatabaseBlock6 if sqliteModel_DatabaseBlock6 is not None else set()
        self.sqliteModel_DatabaseBlock = sqliteModel_DatabaseBlock
        self.sqliteModel_DatabaseBlock2 = sqliteModel_DatabaseBlock2
        self.sqliteModel_DatabaseBlock4 = sqliteModel_DatabaseBlock4
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def sqliteModel_DatabaseBlock6(self):
        return self.__sqliteModel_DatabaseBlock6

    @sqliteModel_DatabaseBlock6.setter
    def sqliteModel_DatabaseBlock6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_DatabaseBlock__sqliteModel_DatabaseBlock6", None)
        self.__sqliteModel_DatabaseBlock6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sqliteModel_MigrationBlock"):
                    opp_val = getattr(item, "sqliteModel_MigrationBlock", None)
                    
                    if opp_val == self:
                        setattr(item, "sqliteModel_MigrationBlock", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sqliteModel_MigrationBlock"):
                    opp_val = getattr(item, "sqliteModel_MigrationBlock", None)
                    
                    setattr(item, "sqliteModel_MigrationBlock", self)
                    

    @property
    def sqliteModel_DatabaseBlock4(self):
        return self.__sqliteModel_DatabaseBlock4

    @sqliteModel_DatabaseBlock4.setter
    def sqliteModel_DatabaseBlock4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_DatabaseBlock__sqliteModel_DatabaseBlock4", None)
        self.__sqliteModel_DatabaseBlock4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_InitBlock"):
                opp_val = getattr(old_value, "sqliteModel_InitBlock", None)
                if opp_val == self:
                    setattr(old_value, "sqliteModel_InitBlock", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_InitBlock"):
                opp_val = getattr(value, "sqliteModel_InitBlock", None)
                setattr(value, "sqliteModel_InitBlock", self)

    @property
    def sqliteModel_DatabaseBlock(self):
        return self.__sqliteModel_DatabaseBlock

    @sqliteModel_DatabaseBlock.setter
    def sqliteModel_DatabaseBlock(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_DatabaseBlock__sqliteModel_DatabaseBlock", None)
        self.__sqliteModel_DatabaseBlock = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_Model"):
                opp_val = getattr(old_value, "sqliteModel_Model", None)
                if opp_val == self:
                    setattr(old_value, "sqliteModel_Model", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_Model"):
                opp_val = getattr(value, "sqliteModel_Model", None)
                setattr(value, "sqliteModel_Model", self)

    @property
    def sqliteModel_DatabaseBlock2(self):
        return self.__sqliteModel_DatabaseBlock2

    @sqliteModel_DatabaseBlock2.setter
    def sqliteModel_DatabaseBlock2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_DatabaseBlock__sqliteModel_DatabaseBlock2", None)
        self.__sqliteModel_DatabaseBlock2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_ConfigBlock"):
                opp_val = getattr(old_value, "sqliteModel_ConfigBlock", None)
                if opp_val == self:
                    setattr(old_value, "sqliteModel_ConfigBlock", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_ConfigBlock"):
                opp_val = getattr(value, "sqliteModel_ConfigBlock", None)
                setattr(value, "sqliteModel_ConfigBlock", self)

class sqliteModel_Model:

    def __init__(self, packageName: str, sqliteModel_Model: "sqliteModel_DatabaseBlock" = None):
        self.packageName = packageName
        self.sqliteModel_Model = sqliteModel_Model
        
    @property
    def packageName(self) -> str:
        return self.__packageName

    @packageName.setter
    def packageName(self, packageName: str):
        self.__packageName = packageName

    @property
    def sqliteModel_Model(self):
        return self.__sqliteModel_Model

    @sqliteModel_Model.setter
    def sqliteModel_Model(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_Model__sqliteModel_Model", None)
        self.__sqliteModel_Model = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_DatabaseBlock"):
                opp_val = getattr(old_value, "sqliteModel_DatabaseBlock", None)
                if opp_val == self:
                    setattr(old_value, "sqliteModel_DatabaseBlock", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_DatabaseBlock"):
                opp_val = getattr(value, "sqliteModel_DatabaseBlock", None)
                setattr(value, "sqliteModel_DatabaseBlock", self)

class sqliteModel_FunctionArg:

    def __init__(self, type: str, name: str, sqliteModel_FunctionArg: "sqliteModel_Function" = None, sqliteModel_FunctionArg193: "sqliteModel_FunctionArgument" = None):
        self.type = type
        self.name = name
        self.sqliteModel_FunctionArg = sqliteModel_FunctionArg
        self.sqliteModel_FunctionArg193 = sqliteModel_FunctionArg193
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def sqliteModel_FunctionArg193(self):
        return self.__sqliteModel_FunctionArg193

    @sqliteModel_FunctionArg193.setter
    def sqliteModel_FunctionArg193(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_FunctionArg__sqliteModel_FunctionArg193", None)
        self.__sqliteModel_FunctionArg193 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_FunctionArgument"):
                opp_val = getattr(old_value, "sqliteModel_FunctionArgument", None)
                if opp_val == self:
                    setattr(old_value, "sqliteModel_FunctionArgument", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_FunctionArgument"):
                opp_val = getattr(value, "sqliteModel_FunctionArgument", None)
                setattr(value, "sqliteModel_FunctionArgument", self)

    @property
    def sqliteModel_FunctionArg(self):
        return self.__sqliteModel_FunctionArg

    @sqliteModel_FunctionArg.setter
    def sqliteModel_FunctionArg(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_FunctionArg__sqliteModel_FunctionArg", None)
        self.__sqliteModel_FunctionArg = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_Function"):
                opp_val = getattr(old_value, "sqliteModel_Function", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_Function"):
                opp_val = getattr(value, "sqliteModel_Function", None)
                if opp_val is None:
                    setattr(value, "sqliteModel_Function", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sqliteModel_DDLStatement:

    pass
class sqliteModel_ConfigurationStatement:

    def __init__(self, name: str, sqliteModel_ConfigurationStatement: "sqliteModel_ConfigBlock" = None):
        self.name = name
        self.sqliteModel_ConfigurationStatement = sqliteModel_ConfigurationStatement
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def sqliteModel_ConfigurationStatement(self):
        return self.__sqliteModel_ConfigurationStatement

    @sqliteModel_ConfigurationStatement.setter
    def sqliteModel_ConfigurationStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqliteModel_ConfigurationStatement__sqliteModel_ConfigurationStatement", None)
        self.__sqliteModel_ConfigurationStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqliteModel_ConfigBlock8"):
                opp_val = getattr(old_value, "sqliteModel_ConfigBlock8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqliteModel_ConfigBlock8"):
                opp_val = getattr(value, "sqliteModel_ConfigBlock8", None)
                if opp_val is None:
                    setattr(value, "sqliteModel_ConfigBlock8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sqliteModel_MigrationBlock:

    pass