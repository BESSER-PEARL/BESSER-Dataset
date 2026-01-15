from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class AssignmentStmt:

    pass
class expressions_codemodel_Variable:

    pass
class Expression:

    pass
class codemodel_expressions_BinaryExp(Expression):

    def __init__(self, operator: str, codemodel_expressions_BinaryExp: "Expression" = None, codemodel_expressions_BinaryExp16: "Expression" = None, Expression36: "codemodel_statements_ForStmt", Expression39: "codemodel_statements_ForStmt", Expression17: "codemodel_expressions_BinaryExp", Expression26: "codemodel_statements_IfStmt", Expression: "codemodel_expressions_BinaryExp", Expression22: "codemodel_statements_AssignmentStmt", Expression19: "codemodel_statements_AssignmentStmt"):
        self.operator = operator
        self.codemodel_expressions_BinaryExp = codemodel_expressions_BinaryExp
        self.codemodel_expressions_BinaryExp16 = codemodel_expressions_BinaryExp16
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def codemodel_expressions_BinaryExp16(self):
        return self.__codemodel_expressions_BinaryExp16

    @codemodel_expressions_BinaryExp16.setter
    def codemodel_expressions_BinaryExp16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_codemodel_expressions_BinaryExp__codemodel_expressions_BinaryExp16", None)
        self.__codemodel_expressions_BinaryExp16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression17"):
                opp_val = getattr(old_value, "Expression17", None)
                if opp_val == self:
                    setattr(old_value, "Expression17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression17"):
                opp_val = getattr(value, "Expression17", None)
                setattr(value, "Expression17", self)

    @property
    def codemodel_expressions_BinaryExp(self):
        return self.__codemodel_expressions_BinaryExp

    @codemodel_expressions_BinaryExp.setter
    def codemodel_expressions_BinaryExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_codemodel_expressions_BinaryExp__codemodel_expressions_BinaryExp", None)
        self.__codemodel_expressions_BinaryExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression"):
                opp_val = getattr(old_value, "Expression", None)
                if opp_val == self:
                    setattr(old_value, "Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression"):
                opp_val = getattr(value, "Expression", None)
                setattr(value, "Expression", self)

class codemodel_expressions_LiteralExp(Expression):

    def __init__(self, value: str, Expression36: "codemodel_statements_ForStmt", Expression39: "codemodel_statements_ForStmt", Expression17: "codemodel_expressions_BinaryExp", Expression26: "codemodel_statements_IfStmt", Expression: "codemodel_expressions_BinaryExp", Expression22: "codemodel_statements_AssignmentStmt", Expression19: "codemodel_statements_AssignmentStmt"):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class codemodel_expressions_VariableExp(Expression):

    pass
class DataType:

    pass
class codemodel_VectorType(DataType):

    def __init__(self, size: str):
        self.size = size
        
    @property
    def size(self) -> str:
        return self.__size

    @size.setter
    def size(self, size: str):
        self.__size = size

class codemodel_ScalarType(DataType):

    pass
class codemodel_MatrixType(DataType):

    def __init__(self, rows: str, columns: str):
        self.rows = rows
        self.columns = columns
        
    @property
    def columns(self) -> str:
        return self.__columns

    @columns.setter
    def columns(self, columns: str):
        self.__columns = columns

    @property
    def rows(self) -> str:
        return self.__rows

    @rows.setter
    def rows(self, rows: str):
        self.__rows = rows

class Variable:

    pass
class Statement:

    pass
class codemodel_statements_ForStmt(Statement):

    pass
class codemodel_statements_IfStmt(Statement):

    pass
class codemodel_statements_CompositeStmt(Statement):

    pass
class codemodel_statements_AssignmentStmt(Statement):

    pass
class codemodel_LocalVariable(Variable):

    pass
class codemodel_FunctionArgument(Variable):

    pass
class codemodel_GlobalVariable(Variable):

    pass
class CMElement:

    pass
class codemodel_Variable(CMElement):

    def __init__(self, constant: bool, identifier: str, codemodel_Variable: "codemodel_DataType" = None):
        self.constant = constant
        self.identifier = identifier
        self.codemodel_Variable = codemodel_Variable
        
    @property
    def constant(self) -> bool:
        return self.__constant

    @constant.setter
    def constant(self, constant: bool):
        self.__constant = constant

    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def codemodel_Variable(self):
        return self.__codemodel_Variable

    @codemodel_Variable.setter
    def codemodel_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_codemodel_Variable__codemodel_Variable", None)
        self.__codemodel_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "codemodel_DataType6"):
                opp_val = getattr(old_value, "codemodel_DataType6", None)
                if opp_val == self:
                    setattr(old_value, "codemodel_DataType6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "codemodel_DataType6"):
                opp_val = getattr(value, "codemodel_DataType6", None)
                setattr(value, "codemodel_DataType6", self)

class codemodel_statements_Statement(CMElement):

    pass
class codemodel_Function(CMElement):

    def __init__(self, identifier: str, codemodel_Function: "codemodel_CodeModule" = None, codemodel_Function8: set["codemodel_FunctionArgument"] = None, codemodel_Function10: set["codemodel_LocalVariable"] = None, codemodel_Function12: set["Statement"] = None):
        self.identifier = identifier
        self.codemodel_Function = codemodel_Function
        self.codemodel_Function8 = codemodel_Function8 if codemodel_Function8 is not None else set()
        self.codemodel_Function10 = codemodel_Function10 if codemodel_Function10 is not None else set()
        self.codemodel_Function12 = codemodel_Function12 if codemodel_Function12 is not None else set()
        
    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def codemodel_Function10(self):
        return self.__codemodel_Function10

    @codemodel_Function10.setter
    def codemodel_Function10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_codemodel_Function__codemodel_Function10", None)
        self.__codemodel_Function10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "codemodel_LocalVariable"):
                    opp_val = getattr(item, "codemodel_LocalVariable", None)
                    
                    if opp_val == self:
                        setattr(item, "codemodel_LocalVariable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "codemodel_LocalVariable"):
                    opp_val = getattr(item, "codemodel_LocalVariable", None)
                    
                    setattr(item, "codemodel_LocalVariable", self)
                    

    @property
    def codemodel_Function12(self):
        return self.__codemodel_Function12

    @codemodel_Function12.setter
    def codemodel_Function12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_codemodel_Function__codemodel_Function12", None)
        self.__codemodel_Function12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Statement"):
                    opp_val = getattr(item, "Statement", None)
                    
                    if opp_val == self:
                        setattr(item, "Statement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Statement"):
                    opp_val = getattr(item, "Statement", None)
                    
                    setattr(item, "Statement", self)
                    

    @property
    def codemodel_Function(self):
        return self.__codemodel_Function

    @codemodel_Function.setter
    def codemodel_Function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_codemodel_Function__codemodel_Function", None)
        self.__codemodel_Function = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "codemodel_CodeModule2"):
                opp_val = getattr(old_value, "codemodel_CodeModule2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "codemodel_CodeModule2"):
                opp_val = getattr(value, "codemodel_CodeModule2", None)
                if opp_val is None:
                    setattr(value, "codemodel_CodeModule2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def codemodel_Function8(self):
        return self.__codemodel_Function8

    @codemodel_Function8.setter
    def codemodel_Function8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_codemodel_Function__codemodel_Function8", None)
        self.__codemodel_Function8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "codemodel_FunctionArgument"):
                    opp_val = getattr(item, "codemodel_FunctionArgument", None)
                    
                    if opp_val == self:
                        setattr(item, "codemodel_FunctionArgument", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "codemodel_FunctionArgument"):
                    opp_val = getattr(item, "codemodel_FunctionArgument", None)
                    
                    setattr(item, "codemodel_FunctionArgument", self)
                    

class codemodel_expressions_Expression(CMElement):

    pass
class codemodel_DataType(CMElement):

    def __init__(self, basetype: str, codemodel_DataType: "codemodel_CodeModule" = None, codemodel_DataType6: "codemodel_Variable" = None):
        self.basetype = basetype
        self.codemodel_DataType = codemodel_DataType
        self.codemodel_DataType6 = codemodel_DataType6
        
    @property
    def basetype(self) -> str:
        return self.__basetype

    @basetype.setter
    def basetype(self, basetype: str):
        self.__basetype = basetype

    @property
    def codemodel_DataType6(self):
        return self.__codemodel_DataType6

    @codemodel_DataType6.setter
    def codemodel_DataType6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_codemodel_DataType__codemodel_DataType6", None)
        self.__codemodel_DataType6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "codemodel_Variable"):
                opp_val = getattr(old_value, "codemodel_Variable", None)
                if opp_val == self:
                    setattr(old_value, "codemodel_Variable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "codemodel_Variable"):
                opp_val = getattr(value, "codemodel_Variable", None)
                setattr(value, "codemodel_Variable", self)

    @property
    def codemodel_DataType(self):
        return self.__codemodel_DataType

    @codemodel_DataType.setter
    def codemodel_DataType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_codemodel_DataType__codemodel_DataType", None)
        self.__codemodel_DataType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "codemodel_CodeModule4"):
                opp_val = getattr(old_value, "codemodel_CodeModule4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "codemodel_CodeModule4"):
                opp_val = getattr(value, "codemodel_CodeModule4", None)
                if opp_val is None:
                    setattr(value, "codemodel_CodeModule4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class codemodel_CodeModule(CMElement):

    pass
class codemodel_CMElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name
