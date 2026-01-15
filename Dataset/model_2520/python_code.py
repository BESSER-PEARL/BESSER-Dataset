from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Statement:

    pass
class codemodel_statements_CompStmt(Statement):

    pass
class codemodel_statements_AsgnStmt(Statement):

    pass
class CMElement:

    pass
class codemodel_statements_Statement(CMElement):

    pass
class codemodel_D(CMElement):

    pass
class codemodel_Variable(CMElement):

    pass
class codemodel_CodeModel(CMElement):

    pass
class expressions_codemodel_Variable:

    pass
class Expression:

    pass
class codemodel_expressions_BinExp(Expression):

    def __init__(self, operator: str, codemodel_expressions_BinExp: "Expression" = None, codemodel_expressions_BinExp7: "Expression" = None, Expression: "codemodel_expressions_BinExp", Expression8: "codemodel_expressions_BinExp", Expression10: "codemodel_statements_AsgnStmt", Expression13: "codemodel_statements_AsgnStmt"):
        self.operator = operator
        self.codemodel_expressions_BinExp = codemodel_expressions_BinExp
        self.codemodel_expressions_BinExp7 = codemodel_expressions_BinExp7
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def codemodel_expressions_BinExp(self):
        return self.__codemodel_expressions_BinExp

    @codemodel_expressions_BinExp.setter
    def codemodel_expressions_BinExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_codemodel_expressions_BinExp__codemodel_expressions_BinExp", None)
        self.__codemodel_expressions_BinExp = value
        
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

    @property
    def codemodel_expressions_BinExp7(self):
        return self.__codemodel_expressions_BinExp7

    @codemodel_expressions_BinExp7.setter
    def codemodel_expressions_BinExp7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_codemodel_expressions_BinExp__codemodel_expressions_BinExp7", None)
        self.__codemodel_expressions_BinExp7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression8"):
                opp_val = getattr(old_value, "Expression8", None)
                if opp_val == self:
                    setattr(old_value, "Expression8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression8"):
                opp_val = getattr(value, "Expression8", None)
                setattr(value, "Expression8", self)

class codemodel_expressions_VarExp(Expression):

    pass
class codemodel_expressions_Expression(CMElement):

    pass
class codemodel_E(CMElement):

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
