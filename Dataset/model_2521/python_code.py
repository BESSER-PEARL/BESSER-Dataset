from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class expressions_codemodel_Variable:

    pass
class Expression:

    pass
class codemodel_expressions_BinExp(Expression):

    def __init__(self, operator: str, codemodel_expressions_BinExp8: "Expression" = None, codemodel_expressions_BinExp: "Expression" = None, Expression: "codemodel_expressions_BinExp", Expression9: "codemodel_expressions_BinExp", Expression11: "codemodel_statements_AsgnStmt", Expression14: "codemodel_statements_AsgnStmt"):
        self.operator = operator
        self.codemodel_expressions_BinExp8 = codemodel_expressions_BinExp8
        self.codemodel_expressions_BinExp = codemodel_expressions_BinExp
        
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
    def codemodel_expressions_BinExp8(self):
        return self.__codemodel_expressions_BinExp8

    @codemodel_expressions_BinExp8.setter
    def codemodel_expressions_BinExp8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_codemodel_expressions_BinExp__codemodel_expressions_BinExp8", None)
        self.__codemodel_expressions_BinExp8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression9"):
                opp_val = getattr(old_value, "Expression9", None)
                if opp_val == self:
                    setattr(old_value, "Expression9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression9"):
                opp_val = getattr(value, "Expression9", None)
                setattr(value, "Expression9", self)

class codemodel_expressions_VarExp(Expression):

    pass
class Statement:

    pass
class codemodel_statements_AsgnStmt(Statement):

    pass
class codemodel_statements_CompStmt(Statement):

    pass
class CMElement:

    pass
class codemodel_expressions_Expression(CMElement):

    pass
class codemodel_statements_Statement(CMElement):

    pass
class codemodel_Root(CMElement):

    pass
class codemodel_E(CMElement):

    pass
class codemodel_D(CMElement):

    pass
class codemodel_Variable(CMElement):

    pass
class codemodel_CodeModel(CMElement):

    pass
class codemodel_CMElement(ABC):

    def __init__(self, name: str, codemodel_CMElement: "codemodel_Root" = None):
        self.name = name
        self.codemodel_CMElement = codemodel_CMElement
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def codemodel_CMElement(self):
        return self.__codemodel_CMElement

    @codemodel_CMElement.setter
    def codemodel_CMElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_codemodel_CMElement__codemodel_CMElement", None)
        self.__codemodel_CMElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "codemodel_Root"):
                opp_val = getattr(old_value, "codemodel_Root", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "codemodel_Root"):
                opp_val = getattr(value, "codemodel_Root", None)
                if opp_val is None:
                    setattr(value, "codemodel_Root", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
