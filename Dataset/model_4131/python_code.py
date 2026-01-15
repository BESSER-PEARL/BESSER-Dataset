from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class cool_Expression:

    pass
class Feature_:

    pass
class cool_Method(Feature_):

    pass
class cool_Attr(Feature_):

    pass
class cool_Type:

    pass
class Literal:

    pass
class cool_StringLiteral(Literal):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class cool_BooleanLiteral(Literal):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class cool_NumberLiteral(Literal):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class cool_IdentifiableElement:

    def __init__(self, name: str, cool_IdentifiableElement: "cool_IdentifierRefExpression" = None):
        self.name = name
        self.cool_IdentifiableElement = cool_IdentifiableElement
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cool_IdentifiableElement(self):
        return self.__cool_IdentifiableElement

    @cool_IdentifiableElement.setter
    def cool_IdentifiableElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cool_IdentifiableElement__cool_IdentifiableElement", None)
        self.__cool_IdentifiableElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cool_IdentifierRefExpression"):
                opp_val = getattr(old_value, "cool_IdentifierRefExpression", None)
                if opp_val == self:
                    setattr(old_value, "cool_IdentifierRefExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cool_IdentifierRefExpression"):
                opp_val = getattr(value, "cool_IdentifierRefExpression", None)
                setattr(value, "cool_IdentifierRefExpression", self)

class PrimaryExpression:

    pass
class cool_LetExpression(PrimaryExpression):

    pass
class cool_AssignmentExpression(PrimaryExpression):

    def __init__(self, name: str, cool_AssignmentExpression: "cool_Expression" = None):
        self.name = name
        self.cool_AssignmentExpression = cool_AssignmentExpression
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cool_AssignmentExpression(self):
        return self.__cool_AssignmentExpression

    @cool_AssignmentExpression.setter
    def cool_AssignmentExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cool_AssignmentExpression__cool_AssignmentExpression", None)
        self.__cool_AssignmentExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cool_Expression23"):
                opp_val = getattr(old_value, "cool_Expression23", None)
                if opp_val == self:
                    setattr(old_value, "cool_Expression23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cool_Expression23"):
                opp_val = getattr(value, "cool_Expression23", None)
                setattr(value, "cool_Expression23", self)

class cool_IdentifierRefExpression(PrimaryExpression):

    pass
class cool_LoopExpression(PrimaryExpression):

    pass
class cool_ConditionalExpression(PrimaryExpression):

    pass
class cool_IsvoidExpression(PrimaryExpression):

    pass
class cool_BlockExpression(PrimaryExpression):

    pass
class cool_DispatchExpression(PrimaryExpression):

    pass
class cool_ParenExpression(PrimaryExpression):

    pass
class cool_IntegerCompositeExpression(PrimaryExpression):

    pass
class cool_NegationExpression(PrimaryExpression):

    pass
class cool_Literal(PrimaryExpression):

    pass
class cool_NewExpression(PrimaryExpression):

    pass
class cool_CaseExpression(PrimaryExpression):

    pass
class cool_SelfTypeLiteral(PrimaryExpression):

    pass
class Expression:

    pass
class cool_MultiplicationExpression(Expression):

    pass
class cool_CompareExpression(Expression):

    def __init__(self, op: str, cool_CompareExpression: "cool_Expression" = None, cool_CompareExpression83: "cool_Expression" = None):
        self.op = op
        self.cool_CompareExpression = cool_CompareExpression
        self.cool_CompareExpression83 = cool_CompareExpression83
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def cool_CompareExpression(self):
        return self.__cool_CompareExpression

    @cool_CompareExpression.setter
    def cool_CompareExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cool_CompareExpression__cool_CompareExpression", None)
        self.__cool_CompareExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cool_Expression81"):
                opp_val = getattr(old_value, "cool_Expression81", None)
                if opp_val == self:
                    setattr(old_value, "cool_Expression81", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cool_Expression81"):
                opp_val = getattr(value, "cool_Expression81", None)
                setattr(value, "cool_Expression81", self)

    @property
    def cool_CompareExpression83(self):
        return self.__cool_CompareExpression83

    @cool_CompareExpression83.setter
    def cool_CompareExpression83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cool_CompareExpression__cool_CompareExpression83", None)
        self.__cool_CompareExpression83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cool_Expression84"):
                opp_val = getattr(old_value, "cool_Expression84", None)
                if opp_val == self:
                    setattr(old_value, "cool_Expression84", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cool_Expression84"):
                opp_val = getattr(value, "cool_Expression84", None)
                setattr(value, "cool_Expression84", self)

class cool_Div(Expression):

    pass
class cool_AdditionExpression(Expression):

    pass
class cool_Minus(Expression):

    pass
class cool_PrimaryExpression(Expression):

    pass
class IdentifiableElement:

    pass
class cool_LetDeclaration(IdentifiableElement):

    pass
class cool_Formal(IdentifiableElement):

    pass
class cool_Case(IdentifiableElement):

    pass
class cool_Feature_(IdentifiableElement):

    pass
class Type:

    pass
class cool_Class_(Type, IdentifiableElement):

    pass
class cool_Program:

    pass