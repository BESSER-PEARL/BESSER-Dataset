from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class ValueExp:

    pass
class SQLDML_IntegerValueExp(ValueExp):

    def __init__(self, aValue: str):
        self.aValue = aValue
        
        pass
    @property
    def aValue(self):
        return self.__aValue

    @aValue.setter
    def aValue(self, aValue: str):
        self.__aValue = aValue


class SQLDML_StringValueExp(ValueExp):

    def __init__(self, aValue: str):
        self.aValue = aValue
        
        pass
    @property
    def aValue(self):
        return self.__aValue

    @aValue.setter
    def aValue(self, aValue: str):
        self.__aValue = aValue


class DataType:

    pass
class StringValueExp:

    pass
class Predicate:

    pass
class SQLDML_FunctionExp(Predicate):

    def __init__(self, name: str, SQLDML_FunctionExp: set["Expression"] = None, Predicate: "SQLDML_InExp" = None):
        self.name = name
        self.SQLDML_FunctionExp = SQLDML_FunctionExp if SQLDML_FunctionExp is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def SQLDML_FunctionExp(self):
        return self.__SQLDML_FunctionExp

    @SQLDML_FunctionExp.setter
    def SQLDML_FunctionExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQLDML_FunctionExp__SQLDML_FunctionExp", None)
        self.__SQLDML_FunctionExp = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Expression32"):
                    opp_val = getattr(item, "Expression32", None)
                    
                    if opp_val == self:
                        setattr(item, "Expression32", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Expression32"):
                    opp_val = getattr(item, "Expression32", None)
                    
                    setattr(item, "Expression32", self)
                    

class SQLDML_ValueExp(Predicate):

    pass
class SQLDML_ListExp(Predicate):

    pass
class BinaryExp:

    pass
class SQLDML_OperationExp(BinaryExp):

    def __init__(self, optName: str):
        self.optName = optName
        
        pass
    @property
    def optName(self):
        return self.__optName

    @optName.setter
    def optName(self, optName: str):
        self.__optName = optName


class SQLDML_AndExp(BinaryExp):

    pass
class SQLDML_OrExp(BinaryExp):

    pass
class WhereClause:

    pass
class NamedElement:

    pass
class SQLDML_DataType(NamedElement):

    pass
class SQLDML_ColumnExp(NamedElement, Predicate):

    def __init__(self, alias: str, SQLDML_ColumnExp: "DataType" = None, Predicate: "SQLDML_InExp" = None):
        self.alias = alias
        self.SQLDML_ColumnExp = SQLDML_ColumnExp
        
        pass
    @property
    def alias(self):
        return self.__alias

    @alias.setter
    def alias(self, alias: str):
        self.__alias = alias


    @property
    def SQLDML_ColumnExp(self):
        return self.__SQLDML_ColumnExp

    @SQLDML_ColumnExp.setter
    def SQLDML_ColumnExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQLDML_ColumnExp__SQLDML_ColumnExp", None)
        self.__SQLDML_ColumnExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DataType"):
                opp_val = getattr(old_value, "DataType", None)
                if opp_val == self:
                    setattr(old_value, "DataType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DataType"):
                opp_val = getattr(value, "DataType", None)
                setattr(value, "DataType", self)

class SQLDML_Table(NamedElement):

    def __init__(self, alias: str):
        self.alias = alias
        
        pass
    @property
    def alias(self):
        return self.__alias

    @alias.setter
    def alias(self, alias: str):
        self.__alias = alias


class Expression:

    pass
class SQLDML_LikeExp(Expression):

    def __init__(self, columnName: str, SQLDML_LikeExp: "StringValueExp" = None, Expression32: "SQLDML_FunctionExp" = None, Expression30: "SQLDML_ListExp" = None, Expression16: "SQLDML_BinaryExp" = None, Expression11: "SQLDML_WhereClause" = None, Expression9: "SQLDML_QueryStmtCol" = None, Expression21: "SQLDML_NotExp" = None, Expression13: "SQLDML_BinaryExp" = None, Expression: "SQLDML_InsertStmt" = None, Expression18: "SQLDML_NotExp" = None):
        self.columnName = columnName
        self.SQLDML_LikeExp = SQLDML_LikeExp
        
        pass
    @property
    def columnName(self):
        return self.__columnName

    @columnName.setter
    def columnName(self, columnName: str):
        self.__columnName = columnName


    @property
    def SQLDML_LikeExp(self):
        return self.__SQLDML_LikeExp

    @SQLDML_LikeExp.setter
    def SQLDML_LikeExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQLDML_LikeExp__SQLDML_LikeExp", None)
        self.__SQLDML_LikeExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StringValueExp"):
                opp_val = getattr(old_value, "StringValueExp", None)
                if opp_val == self:
                    setattr(old_value, "StringValueExp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StringValueExp"):
                opp_val = getattr(value, "StringValueExp", None)
                setattr(value, "StringValueExp", self)

class SQLDML_Predicate(Expression):

    pass
class SQLDML_BinaryExp(Expression):

    def __init__(self, opName: str, SQLDML_BinaryExp: "Expression" = None, SQLDML_BinaryExp15: "Expression" = None, Expression32: "SQLDML_FunctionExp" = None, Expression30: "SQLDML_ListExp" = None, Expression16: "SQLDML_BinaryExp" = None, Expression11: "SQLDML_WhereClause" = None, Expression9: "SQLDML_QueryStmtCol" = None, Expression21: "SQLDML_NotExp" = None, Expression13: "SQLDML_BinaryExp" = None, Expression: "SQLDML_InsertStmt" = None, Expression18: "SQLDML_NotExp" = None):
        self.opName = opName
        self.SQLDML_BinaryExp = SQLDML_BinaryExp
        self.SQLDML_BinaryExp15 = SQLDML_BinaryExp15
        
        pass
    @property
    def opName(self):
        return self.__opName

    @opName.setter
    def opName(self, opName: str):
        self.__opName = opName


    @property
    def SQLDML_BinaryExp15(self):
        return self.__SQLDML_BinaryExp15

    @SQLDML_BinaryExp15.setter
    def SQLDML_BinaryExp15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQLDML_BinaryExp__SQLDML_BinaryExp15", None)
        self.__SQLDML_BinaryExp15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression16"):
                opp_val = getattr(old_value, "Expression16", None)
                if opp_val == self:
                    setattr(old_value, "Expression16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression16"):
                opp_val = getattr(value, "Expression16", None)
                setattr(value, "Expression16", self)

    @property
    def SQLDML_BinaryExp(self):
        return self.__SQLDML_BinaryExp

    @SQLDML_BinaryExp.setter
    def SQLDML_BinaryExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQLDML_BinaryExp__SQLDML_BinaryExp", None)
        self.__SQLDML_BinaryExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression13"):
                opp_val = getattr(old_value, "Expression13", None)
                if opp_val == self:
                    setattr(old_value, "Expression13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression13"):
                opp_val = getattr(value, "Expression13", None)
                setattr(value, "Expression13", self)

class SQLDML_InExp(Expression):

    def __init__(self, columnName: str, SQLDML_InExp: set["Predicate"] = None, Expression32: "SQLDML_FunctionExp" = None, Expression30: "SQLDML_ListExp" = None, Expression16: "SQLDML_BinaryExp" = None, Expression11: "SQLDML_WhereClause" = None, Expression9: "SQLDML_QueryStmtCol" = None, Expression21: "SQLDML_NotExp" = None, Expression13: "SQLDML_BinaryExp" = None, Expression: "SQLDML_InsertStmt" = None, Expression18: "SQLDML_NotExp" = None):
        self.columnName = columnName
        self.SQLDML_InExp = SQLDML_InExp if SQLDML_InExp is not None else set()
        
        pass
    @property
    def columnName(self):
        return self.__columnName

    @columnName.setter
    def columnName(self, columnName: str):
        self.__columnName = columnName


    @property
    def SQLDML_InExp(self):
        return self.__SQLDML_InExp

    @SQLDML_InExp.setter
    def SQLDML_InExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQLDML_InExp__SQLDML_InExp", None)
        self.__SQLDML_InExp = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Predicate"):
                    opp_val = getattr(item, "Predicate", None)
                    
                    if opp_val == self:
                        setattr(item, "Predicate", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Predicate"):
                    opp_val = getattr(item, "Predicate", None)
                    
                    setattr(item, "Predicate", self)
                    

class SQLDML_NotExp(Expression):

    def __init__(self, opName: str, SQLDML_NotExp: "Expression" = None, SQLDML_NotExp20: "Expression" = None, Expression32: "SQLDML_FunctionExp" = None, Expression30: "SQLDML_ListExp" = None, Expression16: "SQLDML_BinaryExp" = None, Expression11: "SQLDML_WhereClause" = None, Expression9: "SQLDML_QueryStmtCol" = None, Expression21: "SQLDML_NotExp" = None, Expression13: "SQLDML_BinaryExp" = None, Expression: "SQLDML_InsertStmt" = None, Expression18: "SQLDML_NotExp" = None):
        self.opName = opName
        self.SQLDML_NotExp = SQLDML_NotExp
        self.SQLDML_NotExp20 = SQLDML_NotExp20
        
        pass
    @property
    def opName(self):
        return self.__opName

    @opName.setter
    def opName(self, opName: str):
        self.__opName = opName


    @property
    def SQLDML_NotExp(self):
        return self.__SQLDML_NotExp

    @SQLDML_NotExp.setter
    def SQLDML_NotExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQLDML_NotExp__SQLDML_NotExp", None)
        self.__SQLDML_NotExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression18"):
                opp_val = getattr(old_value, "Expression18", None)
                if opp_val == self:
                    setattr(old_value, "Expression18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression18"):
                opp_val = getattr(value, "Expression18", None)
                setattr(value, "Expression18", self)

    @property
    def SQLDML_NotExp20(self):
        return self.__SQLDML_NotExp20

    @SQLDML_NotExp20.setter
    def SQLDML_NotExp20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQLDML_NotExp__SQLDML_NotExp20", None)
        self.__SQLDML_NotExp20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression21"):
                opp_val = getattr(old_value, "Expression21", None)
                if opp_val == self:
                    setattr(old_value, "Expression21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression21"):
                opp_val = getattr(value, "Expression21", None)
                setattr(value, "Expression21", self)

class SQLDML_QueryPredicate(Expression):

    pass
class QueryStmt:

    pass
class SQLDML_QueryStmtAllCol(QueryStmt):

    pass
class SQLDML_QueryStmtCol(QueryStmt):

    pass
class ColumnExp:

    pass
class Table:

    pass
class Statement:

    pass
class SQLDML_InsertStmt(Statement):

    def __init__(self, tableName: str, SQLDML_InsertStmt: set["Expression"] = None, Statement: "SQLDML_SQLRoot" = None):
        self.tableName = tableName
        self.SQLDML_InsertStmt = SQLDML_InsertStmt if SQLDML_InsertStmt is not None else set()
        
        pass
    @property
    def tableName(self):
        return self.__tableName

    @tableName.setter
    def tableName(self, tableName: str):
        self.__tableName = tableName


    @property
    def SQLDML_InsertStmt(self):
        return self.__SQLDML_InsertStmt

    @SQLDML_InsertStmt.setter
    def SQLDML_InsertStmt(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQLDML_InsertStmt__SQLDML_InsertStmt", None)
        self.__SQLDML_InsertStmt = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Expression"):
                    opp_val = getattr(item, "Expression", None)
                    
                    if opp_val == self:
                        setattr(item, "Expression", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Expression"):
                    opp_val = getattr(item, "Expression", None)
                    
                    setattr(item, "Expression", self)
                    

class SQLDML_QueryStmt(Statement):

    pass
class LocatedElement:

    pass
class SQLDML_NamedElement(LocatedElement):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class SQLDML_WhereClause(LocatedElement):

    pass
class SQLDML_Expression(LocatedElement):

    pass
class SQLDML_SQLRoot(LocatedElement):

    pass
class SQLDML_ViewStatement(Statement):

    def __init__(self, name: str, SQLDML_ViewStatement3: "QueryStmt" = None, SQLDML_ViewStatement: set["ColumnExp"] = None, Statement: "SQLDML_SQLRoot" = None):
        self.name = name
        self.SQLDML_ViewStatement3 = SQLDML_ViewStatement3
        self.SQLDML_ViewStatement = SQLDML_ViewStatement if SQLDML_ViewStatement is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def SQLDML_ViewStatement(self):
        return self.__SQLDML_ViewStatement

    @SQLDML_ViewStatement.setter
    def SQLDML_ViewStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQLDML_ViewStatement__SQLDML_ViewStatement", None)
        self.__SQLDML_ViewStatement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ColumnExp"):
                    opp_val = getattr(item, "ColumnExp", None)
                    
                    if opp_val == self:
                        setattr(item, "ColumnExp", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ColumnExp"):
                    opp_val = getattr(item, "ColumnExp", None)
                    
                    setattr(item, "ColumnExp", self)
                    

    @property
    def SQLDML_ViewStatement3(self):
        return self.__SQLDML_ViewStatement3

    @SQLDML_ViewStatement3.setter
    def SQLDML_ViewStatement3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQLDML_ViewStatement__SQLDML_ViewStatement3", None)
        self.__SQLDML_ViewStatement3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QueryStmt"):
                opp_val = getattr(old_value, "QueryStmt", None)
                if opp_val == self:
                    setattr(old_value, "QueryStmt", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QueryStmt"):
                opp_val = getattr(value, "QueryStmt", None)
                setattr(value, "QueryStmt", self)

class SQLDML_Statement(LocatedElement):

    pass
class SQLDML_LocatedElement(ABC):

    def __init__(self, location: str, commentsBefore: str, commentsAfter: str):
        self.location = location
        self.commentsBefore = commentsBefore
        self.commentsAfter = commentsAfter
        
        pass
    @property
    def commentsBefore(self):
        return self.__commentsBefore

    @commentsBefore.setter
    def commentsBefore(self, commentsBefore: str):
        self.__commentsBefore = commentsBefore


    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location


    @property
    def commentsAfter(self):
        return self.__commentsAfter

    @commentsAfter.setter
    def commentsAfter(self, commentsAfter: str):
        self.__commentsAfter = commentsAfter

