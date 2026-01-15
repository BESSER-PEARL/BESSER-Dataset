from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class LiteralExpressionType(Enum):
    STRING = "STRING"
    INTEGER = "INTEGER"
    BOOLEAN = "BOOLEAN"
    NULL = "NULL"
class BasicTypes(Enum):
    BINARY_INTEGER = "BINARY_INTEGER"
    BINARY_FLOAT = "BINARY_FLOAT"
    BINARY_DOUBLE = "BINARY_DOUBLE"
    NATURAL = "NATURAL"
    POSITIVE = "POSITIVE"
    NUMBER = "NUMBER"
    NUMERIC = "NUMERIC"
    DECIMAL = "DECIMAL"
    DEC = "DEC"
    LONG = "LONG"
    BOOLEAN = "BOOLEAN"
    DATE = "DATE"
    INTEGER = "INTEGER"
    INT = "INT"
    FLOAT = "FLOAT"
    REAL = "REAL"
    DOUBLE = "DOUBLE"
    CHAR = "CHAR"
    VARCHAR = "VARCHAR"
    VARCHAR2 = "VARCHAR2"
    CHARACTER = "CHARACTER"
    NCHAR = "NCHAR"
    NVARCHAR = "NVARCHAR"
    NVARCHAR2 = "NVARCHAR2"
    BLOB = "BLOB"
    CLOB = "CLOB"
    ROWID = "ROWID"
class ArithmeticOperatorType(Enum):
    PLUS = "PLUS"
    MINUS = "MINUS"
    DOUBLEVERTICALBAR = "DOUBLEVERTICALBAR"
    MULTIPLICATION = "MULTIPLICATION"
    DIVISION = "DIVISION"
    EXPONENT = "EXPONENT"
    POSITIVE = "POSITIVE"
    NEGATIVE = "NEGATIVE"
class BooleanOperatorType(Enum):
    OR = "OR"
    AND = "AND"
    NOT = "NOT"
    EQUALS = "EQUALS"
    LESSTHAN = "LESSTHAN"
    GREATERTHAN = "GREATERTHAN"
    NOTEQUALS = "NOTEQUALS"
    LESSEQUALS = "LESSEQUALS"
    GREATEREQUALS = "GREATEREQUALS"


############################################
# Definition of Classes
############################################

class plsql_declaration_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class TriggerBlock:

    pass
class plsql_declaration_PLSQLDefinition:

    pass
class statement_BlockStatement:

    pass
class plsql_condition_SQLCondition(ABC):

    pass
class SelectStatement:

    pass
class Argument:

    pass
class type_TypedElement:

    pass
class declaration_Declaration:

    pass
class plsql_declaration_FunctionDeclaration(declaration_Declaration, type_TypedElement):

    pass
class plsql_declaration_VariableDeclaration(declaration_Declaration, type_TypedElement):

    def __init__(self, constant: bool, notnull: bool, default: bool, plsql_declaration_VariableDeclaration: "Expression" = None):
        self.constant = constant
        self.notnull = notnull
        self.default = default
        self.plsql_declaration_VariableDeclaration = plsql_declaration_VariableDeclaration
        
    @property
    def constant(self) -> bool:
        return self.__constant

    @constant.setter
    def constant(self, constant: bool):
        self.__constant = constant

    @property
    def default(self) -> bool:
        return self.__default

    @default.setter
    def default(self, default: bool):
        self.__default = default

    @property
    def notnull(self) -> bool:
        return self.__notnull

    @notnull.setter
    def notnull(self, notnull: bool):
        self.__notnull = notnull

    @property
    def plsql_declaration_VariableDeclaration(self):
        return self.__plsql_declaration_VariableDeclaration

    @plsql_declaration_VariableDeclaration.setter
    def plsql_declaration_VariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_plsql_declaration_VariableDeclaration__plsql_declaration_VariableDeclaration", None)
        self.__plsql_declaration_VariableDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression108"):
                opp_val = getattr(old_value, "Expression108", None)
                if opp_val == self:
                    setattr(old_value, "Expression108", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression108"):
                opp_val = getattr(value, "Expression108", None)
                setattr(value, "Expression108", self)

class plsql_type_TypedElement(ABC):

    pass
class Type:

    pass
class plsql_type_GenericType(Type):

    pass
class plsql_type_IndirectType(Type):

    def __init__(self, identifier: str, rowtype: bool, type: bool, range: int, Type: "plsql_type_TypedElement"):
        self.identifier = identifier
        self.rowtype = rowtype
        self.type = type
        self.range = range
        
    @property
    def rowtype(self) -> bool:
        return self.__rowtype

    @rowtype.setter
    def rowtype(self, rowtype: bool):
        self.__rowtype = rowtype

    @property
    def range(self) -> int:
        return self.__range

    @range.setter
    def range(self, range: int):
        self.__range = range

    @property
    def type(self) -> bool:
        return self.__type

    @type.setter
    def type(self, type: bool):
        self.__type = type

    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

class plsql_type_Datatype(Type):

    def __init__(self, name: str, range: int, Type: "plsql_type_TypedElement"):
        self.name = name
        self.range = range
        
    @property
    def range(self) -> int:
        return self.__range

    @range.setter
    def range(self, range: int):
        self.__range = range

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class plsql_type_Type:

    pass
class StringOperation:

    pass
class plsql_expression_ConcatString(StringOperation):

    pass
class NamedElement:

    pass
class plsql_declaration_Declaration(NamedElement):

    pass
class plsql_declaration_Package(NamedElement):

    pass
class plsql_expression_FunctionCallParameter(NamedElement):

    pass
class condition_SQLCondition:

    pass
class plsql_expression_Expression(ABC):

    pass
class plsql_statement_ExceptionSection:

    def __init__(self, exceptionNames: str, plsql_statement_ExceptionSection: set["Statement"] = None):
        self.exceptionNames = exceptionNames
        self.plsql_statement_ExceptionSection = plsql_statement_ExceptionSection if plsql_statement_ExceptionSection is not None else set()
        
    @property
    def exceptionNames(self) -> str:
        return self.__exceptionNames

    @exceptionNames.setter
    def exceptionNames(self, exceptionNames: str):
        self.__exceptionNames = exceptionNames

    @property
    def plsql_statement_ExceptionSection(self):
        return self.__plsql_statement_ExceptionSection

    @plsql_statement_ExceptionSection.setter
    def plsql_statement_ExceptionSection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_plsql_statement_ExceptionSection__plsql_statement_ExceptionSection", None)
        self.__plsql_statement_ExceptionSection = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Statement54"):
                    opp_val = getattr(item, "Statement54", None)
                    
                    if opp_val == self:
                        setattr(item, "Statement54", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Statement54"):
                    opp_val = getattr(item, "Statement54", None)
                    
                    setattr(item, "Statement54", self)
                    

class plsql_statement_UpdatePair:

    def __init__(self, column: str, plsql_statement_UpdatePair: "Expression" = None):
        self.column = column
        self.plsql_statement_UpdatePair = plsql_statement_UpdatePair
        
    @property
    def column(self) -> str:
        return self.__column

    @column.setter
    def column(self, column: str):
        self.__column = column

    @property
    def plsql_statement_UpdatePair(self):
        return self.__plsql_statement_UpdatePair

    @plsql_statement_UpdatePair.setter
    def plsql_statement_UpdatePair(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_plsql_statement_UpdatePair__plsql_statement_UpdatePair", None)
        self.__plsql_statement_UpdatePair = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression52"):
                opp_val = getattr(old_value, "Expression52", None)
                if opp_val == self:
                    setattr(old_value, "Expression52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression52"):
                opp_val = getattr(value, "Expression52", None)
                setattr(value, "Expression52", self)

class UpdatePair:

    pass
class SQLCondition:

    pass
class plsql_condition_ConditionComparison(SQLCondition):

    def __init__(self, type: str, plsql_condition_ConditionComparison: "Expression" = None, plsql_condition_ConditionComparison105: "Expression" = None, SQLCondition101: "plsql_condition_NotCondition", SQLCondition99: "plsql_condition_BooleanCondition", SQLCondition: "plsql_statement_SelectStatement", SQLCondition50: "plsql_statement_UpdateStatement", SQLCondition96: "plsql_condition_BooleanCondition"):
        self.type = type
        self.plsql_condition_ConditionComparison = plsql_condition_ConditionComparison
        self.plsql_condition_ConditionComparison105 = plsql_condition_ConditionComparison105
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def plsql_condition_ConditionComparison105(self):
        return self.__plsql_condition_ConditionComparison105

    @plsql_condition_ConditionComparison105.setter
    def plsql_condition_ConditionComparison105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_plsql_condition_ConditionComparison__plsql_condition_ConditionComparison105", None)
        self.__plsql_condition_ConditionComparison105 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression106"):
                opp_val = getattr(old_value, "Expression106", None)
                if opp_val == self:
                    setattr(old_value, "Expression106", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression106"):
                opp_val = getattr(value, "Expression106", None)
                setattr(value, "Expression106", self)

    @property
    def plsql_condition_ConditionComparison(self):
        return self.__plsql_condition_ConditionComparison

    @plsql_condition_ConditionComparison.setter
    def plsql_condition_ConditionComparison(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_plsql_condition_ConditionComparison__plsql_condition_ConditionComparison", None)
        self.__plsql_condition_ConditionComparison = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression103"):
                opp_val = getattr(old_value, "Expression103", None)
                if opp_val == self:
                    setattr(old_value, "Expression103", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression103"):
                opp_val = getattr(value, "Expression103", None)
                setattr(value, "Expression103", self)

class plsql_condition_BooleanCondition(SQLCondition):

    def __init__(self, type: str, plsql_condition_BooleanCondition: "SQLCondition" = None, plsql_condition_BooleanCondition98: "SQLCondition" = None, SQLCondition101: "plsql_condition_NotCondition", SQLCondition99: "plsql_condition_BooleanCondition", SQLCondition: "plsql_statement_SelectStatement", SQLCondition50: "plsql_statement_UpdateStatement", SQLCondition96: "plsql_condition_BooleanCondition"):
        self.type = type
        self.plsql_condition_BooleanCondition = plsql_condition_BooleanCondition
        self.plsql_condition_BooleanCondition98 = plsql_condition_BooleanCondition98
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def plsql_condition_BooleanCondition98(self):
        return self.__plsql_condition_BooleanCondition98

    @plsql_condition_BooleanCondition98.setter
    def plsql_condition_BooleanCondition98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_plsql_condition_BooleanCondition__plsql_condition_BooleanCondition98", None)
        self.__plsql_condition_BooleanCondition98 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SQLCondition99"):
                opp_val = getattr(old_value, "SQLCondition99", None)
                if opp_val == self:
                    setattr(old_value, "SQLCondition99", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SQLCondition99"):
                opp_val = getattr(value, "SQLCondition99", None)
                setattr(value, "SQLCondition99", self)

    @property
    def plsql_condition_BooleanCondition(self):
        return self.__plsql_condition_BooleanCondition

    @plsql_condition_BooleanCondition.setter
    def plsql_condition_BooleanCondition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_plsql_condition_BooleanCondition__plsql_condition_BooleanCondition", None)
        self.__plsql_condition_BooleanCondition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SQLCondition96"):
                opp_val = getattr(old_value, "SQLCondition96", None)
                if opp_val == self:
                    setattr(old_value, "SQLCondition96", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SQLCondition96"):
                opp_val = getattr(value, "SQLCondition96", None)
                setattr(value, "SQLCondition96", self)

class plsql_condition_NotCondition(SQLCondition):

    pass
class ModifySQLStatement:

    pass
class plsql_statement_InsertStatement(ModifySQLStatement):

    def __init__(self, into: str, columns: str, plsql_statement_InsertStatement: set["Expression"] = None):
        self.into = into
        self.columns = columns
        self.plsql_statement_InsertStatement = plsql_statement_InsertStatement if plsql_statement_InsertStatement is not None else set()
        
    @property
    def columns(self) -> str:
        return self.__columns

    @columns.setter
    def columns(self, columns: str):
        self.__columns = columns

    @property
    def into(self) -> str:
        return self.__into

    @into.setter
    def into(self, into: str):
        self.__into = into

    @property
    def plsql_statement_InsertStatement(self):
        return self.__plsql_statement_InsertStatement

    @plsql_statement_InsertStatement.setter
    def plsql_statement_InsertStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_plsql_statement_InsertStatement__plsql_statement_InsertStatement", None)
        self.__plsql_statement_InsertStatement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Expression46"):
                    opp_val = getattr(item, "Expression46", None)
                    
                    if opp_val == self:
                        setattr(item, "Expression46", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Expression46"):
                    opp_val = getattr(item, "Expression46", None)
                    
                    setattr(item, "Expression46", self)
                    

class plsql_statement_SetTransactionStatement(ModifySQLStatement):

    pass
class plsql_statement_UpdateStatement(ModifySQLStatement):

    def __init__(self, table: str, plsql_statement_UpdateStatement: set["UpdatePair"] = None, plsql_statement_UpdateStatement49: "SQLCondition" = None):
        self.table = table
        self.plsql_statement_UpdateStatement = plsql_statement_UpdateStatement if plsql_statement_UpdateStatement is not None else set()
        self.plsql_statement_UpdateStatement49 = plsql_statement_UpdateStatement49
        
    @property
    def table(self) -> str:
        return self.__table

    @table.setter
    def table(self, table: str):
        self.__table = table

    @property
    def plsql_statement_UpdateStatement49(self):
        return self.__plsql_statement_UpdateStatement49

    @plsql_statement_UpdateStatement49.setter
    def plsql_statement_UpdateStatement49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_plsql_statement_UpdateStatement__plsql_statement_UpdateStatement49", None)
        self.__plsql_statement_UpdateStatement49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SQLCondition50"):
                opp_val = getattr(old_value, "SQLCondition50", None)
                if opp_val == self:
                    setattr(old_value, "SQLCondition50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SQLCondition50"):
                opp_val = getattr(value, "SQLCondition50", None)
                setattr(value, "SQLCondition50", self)

    @property
    def plsql_statement_UpdateStatement(self):
        return self.__plsql_statement_UpdateStatement

    @plsql_statement_UpdateStatement.setter
    def plsql_statement_UpdateStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_plsql_statement_UpdateStatement__plsql_statement_UpdateStatement", None)
        self.__plsql_statement_UpdateStatement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UpdatePair"):
                    opp_val = getattr(item, "UpdatePair", None)
                    
                    if opp_val == self:
                        setattr(item, "UpdatePair", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UpdatePair"):
                    opp_val = getattr(item, "UpdatePair", None)
                    
                    setattr(item, "UpdatePair", self)
                    

class plsql_statement_DeleteStatement(ModifySQLStatement):

    pass
class plsql_statement_SelectStatement(ModifySQLStatement):

    def __init__(self, distinct: bool, unique: bool, all: bool, selectList: str, bulk: bool, collect: bool, from: str, isCount: bool, plsql_statement_SelectStatement: set["VarRefExpression"] = None, plsql_statement_SelectStatement41: "SQLCondition" = None, plsql_statement_SelectStatement43: set["Expression"] = None):
        self.distinct = distinct
        self.unique = unique
        self.all = all
        self.selectList = selectList
        self.bulk = bulk
        self.collect = collect
        self.from = from
        self.isCount = isCount
        self.plsql_statement_SelectStatement = plsql_statement_SelectStatement if plsql_statement_SelectStatement is not None else set()
        self.plsql_statement_SelectStatement41 = plsql_statement_SelectStatement41
        self.plsql_statement_SelectStatement43 = plsql_statement_SelectStatement43 if plsql_statement_SelectStatement43 is not None else set()
        
    @property
    def unique(self) -> bool:
        return self.__unique

    @unique.setter
    def unique(self, unique: bool):
        self.__unique = unique

    @property
    def distinct(self) -> bool:
        return self.__distinct

    @distinct.setter
    def distinct(self, distinct: bool):
        self.__distinct = distinct

    @property
    def collect(self) -> bool:
        return self.__collect

    @collect.setter
    def collect(self, collect: bool):
        self.__collect = collect

    @property
    def bulk(self) -> bool:
        return self.__bulk

    @bulk.setter
    def bulk(self, bulk: bool):
        self.__bulk = bulk

    @property
    def isCount(self) -> bool:
        return self.__isCount

    @isCount.setter
    def isCount(self, isCount: bool):
        self.__isCount = isCount

    @property
    def all(self) -> bool:
        return self.__all

    @all.setter
    def all(self, all: bool):
        self.__all = all

    @property
    def selectList(self) -> str:
        return self.__selectList

    @selectList.setter
    def selectList(self, selectList: str):
        self.__selectList = selectList

    @property
    def from(self) -> str:
        return self.__from

    @from.setter
    def from(self, from: str):
        self.__from = from

    @property
    def plsql_statement_SelectStatement43(self):
        return self.__plsql_statement_SelectStatement43

    @plsql_statement_SelectStatement43.setter
    def plsql_statement_SelectStatement43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_plsql_statement_SelectStatement__plsql_statement_SelectStatement43", None)
        self.__plsql_statement_SelectStatement43 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Expression44"):
                    opp_val = getattr(item, "Expression44", None)
                    
                    if opp_val == self:
                        setattr(item, "Expression44", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Expression44"):
                    opp_val = getattr(item, "Expression44", None)
                    
                    setattr(item, "Expression44", self)
                    

    @property
    def plsql_statement_SelectStatement(self):
        return self.__plsql_statement_SelectStatement

    @plsql_statement_SelectStatement.setter
    def plsql_statement_SelectStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_plsql_statement_SelectStatement__plsql_statement_SelectStatement", None)
        self.__plsql_statement_SelectStatement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "VarRefExpression39"):
                    opp_val = getattr(item, "VarRefExpression39", None)
                    
                    if opp_val == self:
                        setattr(item, "VarRefExpression39", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "VarRefExpression39"):
                    opp_val = getattr(item, "VarRefExpression39", None)
                    
                    setattr(item, "VarRefExpression39", self)
                    

    @property
    def plsql_statement_SelectStatement41(self):
        return self.__plsql_statement_SelectStatement41

    @plsql_statement_SelectStatement41.setter
    def plsql_statement_SelectStatement41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_plsql_statement_SelectStatement__plsql_statement_SelectStatement41", None)
        self.__plsql_statement_SelectStatement41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SQLCondition"):
                opp_val = getattr(old_value, "SQLCondition", None)
                if opp_val == self:
                    setattr(old_value, "SQLCondition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SQLCondition"):
                opp_val = getattr(value, "SQLCondition", None)
                setattr(value, "SQLCondition", self)

class VarRefExpression:

    pass
class plsql_expression_FormsVarRef(VarRefExpression):

    def __init__(self, reference: str, VarRefExpression: "plsql_statement_FetchStatement", VarRefExpression39: "plsql_statement_SelectStatement"):
        self.reference = reference
        
    @property
    def reference(self) -> str:
        return self.__reference

    @reference.setter
    def reference(self, reference: str):
        self.__reference = reference

class plsql_expression_SQLVariable(VarRefExpression):

    pass
class plsql_expression_SQLCursor(VarRefExpression):

    pass
class CursorDeclaration:

    pass
class ControlSQLStatement:

    pass
class plsql_statement_CommitStatement(ControlSQLStatement):

    pass
class plsql_statement_LockTableStatement(ControlSQLStatement):

    pass
class plsql_statement_FetchStatement(ControlSQLStatement):

    pass
class plsql_statement_SavepointStatement(ControlSQLStatement):

    pass
class plsql_statement_RollbackStatement(ControlSQLStatement):

    pass
class plsql_statement_OpenStatement(ControlSQLStatement):

    pass
class plsql_statement_CloseStatement(ControlSQLStatement):

    pass
class SQLStatement:

    pass
class plsql_statement_ModifySQLStatement(SQLStatement):

    pass
class plsql_statement_ControlSQLStatement(SQLStatement):

    pass
class FunctionCallParameter:

    pass
class expression_Expression:

    pass
class plsql_expression_BooleanExpression(condition_SQLCondition, expression_Expression):

    def __init__(self, type: str, plsql_expression_BooleanExpression: "Expression" = None, plsql_expression_BooleanExpression58: "Expression" = None):
        self.type = type
        self.plsql_expression_BooleanExpression = plsql_expression_BooleanExpression
        self.plsql_expression_BooleanExpression58 = plsql_expression_BooleanExpression58
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def plsql_expression_BooleanExpression58(self):
        return self.__plsql_expression_BooleanExpression58

    @plsql_expression_BooleanExpression58.setter
    def plsql_expression_BooleanExpression58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_plsql_expression_BooleanExpression__plsql_expression_BooleanExpression58", None)
        self.__plsql_expression_BooleanExpression58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression59"):
                opp_val = getattr(old_value, "Expression59", None)
                if opp_val == self:
                    setattr(old_value, "Expression59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression59"):
                opp_val = getattr(value, "Expression59", None)
                setattr(value, "Expression59", self)

    @property
    def plsql_expression_BooleanExpression(self):
        return self.__plsql_expression_BooleanExpression

    @plsql_expression_BooleanExpression.setter
    def plsql_expression_BooleanExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_plsql_expression_BooleanExpression__plsql_expression_BooleanExpression", None)
        self.__plsql_expression_BooleanExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression56"):
                opp_val = getattr(old_value, "Expression56", None)
                if opp_val == self:
                    setattr(old_value, "Expression56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression56"):
                opp_val = getattr(value, "Expression56", None)
                setattr(value, "Expression56", self)

class ExceptionSection:

    pass
class Declaration:

    pass
class plsql_declaration_ProcedureDeclaration(Declaration):

    pass
class plsql_declaration_CursorDeclaration(Declaration):

    pass
class VariableDeclaration:

    pass
class LoopStatement:

    pass
class plsql_statement_ForStatement(LoopStatement):

    pass
class IfStatement:

    pass
class declaration_NamedElement:

    pass
class plsql_declaration_TriggerBlock(statement_BlockStatement, declaration_NamedElement):

    pass
class plsql_declaration_Argument(type_TypedElement, declaration_NamedElement):

    def __init__(self, in: bool, out: bool, default: bool, plsql_declaration_Argument: "Expression" = None):
        self.in = in
        self.out = out
        self.default = default
        self.plsql_declaration_Argument = plsql_declaration_Argument
        
    @property
    def default(self) -> bool:
        return self.__default

    @default.setter
    def default(self, default: bool):
        self.__default = default

    @property
    def in(self) -> bool:
        return self.__in

    @in.setter
    def in(self, in: bool):
        self.__in = in

    @property
    def out(self) -> bool:
        return self.__out

    @out.setter
    def out(self, out: bool):
        self.__out = out

    @property
    def plsql_declaration_Argument(self):
        return self.__plsql_declaration_Argument

    @plsql_declaration_Argument.setter
    def plsql_declaration_Argument(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_plsql_declaration_Argument__plsql_declaration_Argument", None)
        self.__plsql_declaration_Argument = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression132"):
                opp_val = getattr(old_value, "Expression132", None)
                if opp_val == self:
                    setattr(old_value, "Expression132", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression132"):
                opp_val = getattr(value, "Expression132", None)
                setattr(value, "Expression132", self)

class statement_Statement:

    pass
class plsql_statement_FunctionCallStatement(statement_Statement, expression_Expression, declaration_NamedElement):

    pass
class plsql_statement_GotoStatement(statement_Statement, declaration_NamedElement):

    pass
class Expression:

    pass
class plsql_expression_ArithmeticExpression(Expression):

    def __init__(self, type: str, plsql_expression_ArithmeticExpression: "Expression" = None, plsql_expression_ArithmeticExpression90: "Expression" = None, Expression37: "plsql_statement_OpenStatement", Expression46: "plsql_statement_InsertStatement", Expression76: "plsql_expression_LikeExpression", Expression91: "plsql_expression_ArithmeticExpression", Expression: "plsql_statement_AssignmentStatement", Expression108: "plsql_declaration_VariableDeclaration", Expression84: "plsql_expression_PropertyAccess", Expression56: "plsql_expression_BooleanExpression", Expression86: "plsql_expression_FunctionCallParameter", Expression3: "plsql_statement_AssignmentStatement", Expression132: "plsql_declaration_Argument", Expression52: "plsql_statement_UpdatePair", Expression63: "plsql_expression_IsNullExpression", Expression18: "plsql_statement_ForStatement", Expression20: "plsql_statement_ReturnStatement", Expression61: "plsql_expression_NotExpression", Expression59: "plsql_expression_BooleanExpression", Expression73: "plsql_expression_LikeExpression", Expression93: "plsql_expression_ConcatString", Expression65: "plsql_expression_InRangeExpression", Expression68: "plsql_expression_InRangeExpression", Expression44: "plsql_statement_SelectStatement", Expression88: "plsql_expression_ArithmeticExpression", Expression103: "plsql_condition_ConditionComparison", Expression5: "plsql_statement_IfStatement", Expression106: "plsql_condition_ConditionComparison", Expression71: "plsql_expression_InRangeExpression"):
        self.type = type
        self.plsql_expression_ArithmeticExpression = plsql_expression_ArithmeticExpression
        self.plsql_expression_ArithmeticExpression90 = plsql_expression_ArithmeticExpression90
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def plsql_expression_ArithmeticExpression90(self):
        return self.__plsql_expression_ArithmeticExpression90

    @plsql_expression_ArithmeticExpression90.setter
    def plsql_expression_ArithmeticExpression90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_plsql_expression_ArithmeticExpression__plsql_expression_ArithmeticExpression90", None)
        self.__plsql_expression_ArithmeticExpression90 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression91"):
                opp_val = getattr(old_value, "Expression91", None)
                if opp_val == self:
                    setattr(old_value, "Expression91", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression91"):
                opp_val = getattr(value, "Expression91", None)
                setattr(value, "Expression91", self)

    @property
    def plsql_expression_ArithmeticExpression(self):
        return self.__plsql_expression_ArithmeticExpression

    @plsql_expression_ArithmeticExpression.setter
    def plsql_expression_ArithmeticExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_plsql_expression_ArithmeticExpression__plsql_expression_ArithmeticExpression", None)
        self.__plsql_expression_ArithmeticExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression88"):
                opp_val = getattr(old_value, "Expression88", None)
                if opp_val == self:
                    setattr(old_value, "Expression88", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression88"):
                opp_val = getattr(value, "Expression88", None)
                setattr(value, "Expression88", self)

class plsql_expression_FoundExpression(Expression):

    pass
class plsql_expression_StringOperation(Expression):

    pass
class plsql_expression_PropertyAccess(Expression):

    def __init__(self, propertyName: str, plsql_expression_PropertyAccess: "Expression" = None, Expression37: "plsql_statement_OpenStatement", Expression46: "plsql_statement_InsertStatement", Expression76: "plsql_expression_LikeExpression", Expression91: "plsql_expression_ArithmeticExpression", Expression: "plsql_statement_AssignmentStatement", Expression108: "plsql_declaration_VariableDeclaration", Expression84: "plsql_expression_PropertyAccess", Expression56: "plsql_expression_BooleanExpression", Expression86: "plsql_expression_FunctionCallParameter", Expression3: "plsql_statement_AssignmentStatement", Expression132: "plsql_declaration_Argument", Expression52: "plsql_statement_UpdatePair", Expression63: "plsql_expression_IsNullExpression", Expression18: "plsql_statement_ForStatement", Expression20: "plsql_statement_ReturnStatement", Expression61: "plsql_expression_NotExpression", Expression59: "plsql_expression_BooleanExpression", Expression73: "plsql_expression_LikeExpression", Expression93: "plsql_expression_ConcatString", Expression65: "plsql_expression_InRangeExpression", Expression68: "plsql_expression_InRangeExpression", Expression44: "plsql_statement_SelectStatement", Expression88: "plsql_expression_ArithmeticExpression", Expression103: "plsql_condition_ConditionComparison", Expression5: "plsql_statement_IfStatement", Expression106: "plsql_condition_ConditionComparison", Expression71: "plsql_expression_InRangeExpression"):
        self.propertyName = propertyName
        self.plsql_expression_PropertyAccess = plsql_expression_PropertyAccess
        
    @property
    def propertyName(self) -> str:
        return self.__propertyName

    @propertyName.setter
    def propertyName(self, propertyName: str):
        self.__propertyName = propertyName

    @property
    def plsql_expression_PropertyAccess(self):
        return self.__plsql_expression_PropertyAccess

    @plsql_expression_PropertyAccess.setter
    def plsql_expression_PropertyAccess(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_plsql_expression_PropertyAccess__plsql_expression_PropertyAccess", None)
        self.__plsql_expression_PropertyAccess = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression84"):
                opp_val = getattr(old_value, "Expression84", None)
                if opp_val == self:
                    setattr(old_value, "Expression84", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression84"):
                opp_val = getattr(value, "Expression84", None)
                setattr(value, "Expression84", self)

class plsql_expression_VarRefExpression(Expression):

    pass
class plsql_expression_IsNullExpression(Expression):

    pass
class plsql_expression_LiteralExpression(Expression):

    def __init__(self, type: str, value: str, Expression37: "plsql_statement_OpenStatement", Expression46: "plsql_statement_InsertStatement", Expression76: "plsql_expression_LikeExpression", Expression91: "plsql_expression_ArithmeticExpression", Expression: "plsql_statement_AssignmentStatement", Expression108: "plsql_declaration_VariableDeclaration", Expression84: "plsql_expression_PropertyAccess", Expression56: "plsql_expression_BooleanExpression", Expression86: "plsql_expression_FunctionCallParameter", Expression3: "plsql_statement_AssignmentStatement", Expression132: "plsql_declaration_Argument", Expression52: "plsql_statement_UpdatePair", Expression63: "plsql_expression_IsNullExpression", Expression18: "plsql_statement_ForStatement", Expression20: "plsql_statement_ReturnStatement", Expression61: "plsql_expression_NotExpression", Expression59: "plsql_expression_BooleanExpression", Expression73: "plsql_expression_LikeExpression", Expression93: "plsql_expression_ConcatString", Expression65: "plsql_expression_InRangeExpression", Expression68: "plsql_expression_InRangeExpression", Expression44: "plsql_statement_SelectStatement", Expression88: "plsql_expression_ArithmeticExpression", Expression103: "plsql_condition_ConditionComparison", Expression5: "plsql_statement_IfStatement", Expression106: "plsql_condition_ConditionComparison", Expression71: "plsql_expression_InRangeExpression"):
        self.type = type
        self.value = value
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class plsql_expression_InRangeExpression(Expression):

    pass
class plsql_expression_NotExpression(Expression):

    pass
class plsql_expression_LikeExpression(Expression):

    pass
class Statement:

    pass
class plsql_statement_IfStatement(Statement):

    pass
class plsql_statement_BlockStatement(Statement):

    pass
class plsql_statement_NullStatement(Statement):

    pass
class plsql_statement_CaseStatement(Statement):

    pass
class plsql_statement_ReturnStatement(Statement):

    pass
class plsql_statement_LoopStatement(Statement):

    pass
class plsql_statement_ExitStatement(Statement):

    pass
class plsql_statement_RaiseStatement(Statement):

    def __init__(self, exception: str, Statement54: "plsql_statement_ExceptionSection", Statement119: "plsql_declaration_ProcedureDeclaration", Statement: "plsql_statement_IfStatement", Statement12: "plsql_statement_IfStatement", Statement24: "plsql_statement_BlockStatement", Statement137: "plsql_declaration_Package", Statement127: "plsql_declaration_FunctionDeclaration", Statement14: "plsql_statement_LoopStatement"):
        self.exception = exception
        
    @property
    def exception(self) -> str:
        return self.__exception

    @exception.setter
    def exception(self, exception: str):
        self.__exception = exception

class plsql_statement_SQLStatement(Statement):

    pass
class plsql_statement_AssignmentStatement(Statement):

    pass
class plsql_statement_Statement(ABC):

    pass