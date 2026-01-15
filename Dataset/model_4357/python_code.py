from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class mini_lang_Expression(ABC):

    pass
class ComparisonExpression:

    pass
class mini_lang_EqualsExpression(ComparisonExpression):

    pass
class mini_lang_NotEqualsExpression(ComparisonExpression):

    pass
class Expression:

    pass
class mini_lang_NameExpression(Expression):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class mini_lang_FOLCallExpression(Expression):

    def __init__(self, iterator: str, method: str, mini_lang_FOLCallExpression: "mini_lang_Expression" = None, mini_lang_FOLCallExpression24: "mini_lang_Expression" = None):
        self.iterator = iterator
        self.method = method
        self.mini_lang_FOLCallExpression = mini_lang_FOLCallExpression
        self.mini_lang_FOLCallExpression24 = mini_lang_FOLCallExpression24
        
    @property
    def iterator(self) -> str:
        return self.__iterator

    @iterator.setter
    def iterator(self, iterator: str):
        self.__iterator = iterator

    @property
    def method(self) -> str:
        return self.__method

    @method.setter
    def method(self, method: str):
        self.__method = method

    @property
    def mini_lang_FOLCallExpression(self):
        return self.__mini_lang_FOLCallExpression

    @mini_lang_FOLCallExpression.setter
    def mini_lang_FOLCallExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mini_lang_FOLCallExpression__mini_lang_FOLCallExpression", None)
        self.__mini_lang_FOLCallExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mini_lang_Expression22"):
                opp_val = getattr(old_value, "mini_lang_Expression22", None)
                if opp_val == self:
                    setattr(old_value, "mini_lang_Expression22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mini_lang_Expression22"):
                opp_val = getattr(value, "mini_lang_Expression22", None)
                setattr(value, "mini_lang_Expression22", self)

    @property
    def mini_lang_FOLCallExpression24(self):
        return self.__mini_lang_FOLCallExpression24

    @mini_lang_FOLCallExpression24.setter
    def mini_lang_FOLCallExpression24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mini_lang_FOLCallExpression__mini_lang_FOLCallExpression24", None)
        self.__mini_lang_FOLCallExpression24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mini_lang_Expression25"):
                opp_val = getattr(old_value, "mini_lang_Expression25", None)
                if opp_val == self:
                    setattr(old_value, "mini_lang_Expression25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mini_lang_Expression25"):
                opp_val = getattr(value, "mini_lang_Expression25", None)
                setattr(value, "mini_lang_Expression25", self)

class mini_lang_ComparisonExpression(Expression):

    pass
class Statement:

    pass
class mini_lang_ReturnStatement(Statement):

    pass
class mini_lang_ExpressionStatement(Statement):

    pass
class mini_lang_AssignmentStatement(Statement):

    pass
class mini_lang_IfStatement(Statement):

    pass
class mini_lang_Statement(ABC):

    pass
class mini_lang_Block:

    pass
class mini_lang_MiniLang:

    pass