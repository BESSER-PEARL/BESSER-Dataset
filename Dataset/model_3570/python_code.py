from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Literal:

    pass
class expression_NullLiteral(Literal):

    def __init__(self, val: str):
        self.val = val
        
    @property
    def val(self) -> str:
        return self.__val

    @val.setter
    def val(self, val: str):
        self.__val = val

class expression_IntegerLiteral(Literal):

    def __init__(self, val: int):
        self.val = val
        
    @property
    def val(self) -> int:
        return self.__val

    @val.setter
    def val(self, val: int):
        self.__val = val

class expression_StringLiteral(Literal):

    def __init__(self, val: str):
        self.val = val
        
    @property
    def val(self) -> str:
        return self.__val

    @val.setter
    def val(self, val: str):
        self.__val = val

class expression_RealLiteral(Literal):

    def __init__(self, val: str):
        self.val = val
        
    @property
    def val(self) -> str:
        return self.__val

    @val.setter
    def val(self, val: str):
        self.__val = val

class expression_BooleanLiteral(Literal):

    def __init__(self, val: str):
        self.val = val
        
    @property
    def val(self) -> str:
        return self.__val

    @val.setter
    def val(self, val: str):
        self.__val = val

class FeatureCall:

    pass
class Expression:

    pass
class expression_ListLiteral(Expression):

    pass
class expression_OperationCall(Expression, FeatureCall):

    pass
class expression_TypeSelectExpression(Expression, FeatureCall):

    pass
class expression_CollectionExpression(Expression, FeatureCall):

    def __init__(self, var: str, expression_CollectionExpression: "expression_Expression" = None):
        self.var = var
        self.expression_CollectionExpression = expression_CollectionExpression
        
    @property
    def var(self) -> str:
        return self.__var

    @var.setter
    def var(self, var: str):
        self.__var = var

    @property
    def expression_CollectionExpression(self):
        return self.__expression_CollectionExpression

    @expression_CollectionExpression.setter
    def expression_CollectionExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expression_CollectionExpression__expression_CollectionExpression", None)
        self.__expression_CollectionExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expression_Expression41"):
                opp_val = getattr(old_value, "expression_Expression41", None)
                if opp_val == self:
                    setattr(old_value, "expression_Expression41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expression_Expression41"):
                opp_val = getattr(value, "expression_Expression41", None)
                setattr(value, "expression_Expression41", self)

class expression_CastedExpression(Expression):

    pass
class expression_FeatureCall(Expression):

    def __init__(self, name: str, expression_FeatureCall: "expression_Expression" = None, expression_FeatureCall34: "expression_Identifier" = None):
        self.name = name
        self.expression_FeatureCall = expression_FeatureCall
        self.expression_FeatureCall34 = expression_FeatureCall34
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def expression_FeatureCall(self):
        return self.__expression_FeatureCall

    @expression_FeatureCall.setter
    def expression_FeatureCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expression_FeatureCall__expression_FeatureCall", None)
        self.__expression_FeatureCall = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expression_Expression32"):
                opp_val = getattr(old_value, "expression_Expression32", None)
                if opp_val == self:
                    setattr(old_value, "expression_Expression32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expression_Expression32"):
                opp_val = getattr(value, "expression_Expression32", None)
                setattr(value, "expression_Expression32", self)

    @property
    def expression_FeatureCall34(self):
        return self.__expression_FeatureCall34

    @expression_FeatureCall34.setter
    def expression_FeatureCall34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expression_FeatureCall__expression_FeatureCall34", None)
        self.__expression_FeatureCall34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expression_Identifier35"):
                opp_val = getattr(old_value, "expression_Identifier35", None)
                if opp_val == self:
                    setattr(old_value, "expression_Identifier35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expression_Identifier35"):
                opp_val = getattr(value, "expression_Identifier35", None)
                setattr(value, "expression_Identifier35", self)

class expression_BooleanOperation(Expression):

    def __init__(self, operator: str, expression_BooleanOperation: "expression_Expression" = None, expression_BooleanOperation53: "expression_Expression" = None):
        self.operator = operator
        self.expression_BooleanOperation = expression_BooleanOperation
        self.expression_BooleanOperation53 = expression_BooleanOperation53
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def expression_BooleanOperation53(self):
        return self.__expression_BooleanOperation53

    @expression_BooleanOperation53.setter
    def expression_BooleanOperation53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expression_BooleanOperation__expression_BooleanOperation53", None)
        self.__expression_BooleanOperation53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expression_Expression54"):
                opp_val = getattr(old_value, "expression_Expression54", None)
                if opp_val == self:
                    setattr(old_value, "expression_Expression54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expression_Expression54"):
                opp_val = getattr(value, "expression_Expression54", None)
                setattr(value, "expression_Expression54", self)

    @property
    def expression_BooleanOperation(self):
        return self.__expression_BooleanOperation

    @expression_BooleanOperation.setter
    def expression_BooleanOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expression_BooleanOperation__expression_BooleanOperation", None)
        self.__expression_BooleanOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expression_Expression51"):
                opp_val = getattr(old_value, "expression_Expression51", None)
                if opp_val == self:
                    setattr(old_value, "expression_Expression51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expression_Expression51"):
                opp_val = getattr(value, "expression_Expression51", None)
                setattr(value, "expression_Expression51", self)

class expression_ConstructorCallExpression(Expression):

    pass
class expression_Literal(Expression):

    pass
class expression_ChainExpression(Expression):

    pass
class expression_GlobalVarExpression(Expression):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class expression_LetExpression(Expression):

    def __init__(self, identifier: str, expression_LetExpression: "expression_Expression" = None, expression_LetExpression2: "expression_Expression" = None):
        self.identifier = identifier
        self.expression_LetExpression = expression_LetExpression
        self.expression_LetExpression2 = expression_LetExpression2
        
    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def expression_LetExpression(self):
        return self.__expression_LetExpression

    @expression_LetExpression.setter
    def expression_LetExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expression_LetExpression__expression_LetExpression", None)
        self.__expression_LetExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expression_Expression"):
                opp_val = getattr(old_value, "expression_Expression", None)
                if opp_val == self:
                    setattr(old_value, "expression_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expression_Expression"):
                opp_val = getattr(value, "expression_Expression", None)
                setattr(value, "expression_Expression", self)

    @property
    def expression_LetExpression2(self):
        return self.__expression_LetExpression2

    @expression_LetExpression2.setter
    def expression_LetExpression2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expression_LetExpression__expression_LetExpression2", None)
        self.__expression_LetExpression2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expression_Expression3"):
                opp_val = getattr(old_value, "expression_Expression3", None)
                if opp_val == self:
                    setattr(old_value, "expression_Expression3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expression_Expression3"):
                opp_val = getattr(value, "expression_Expression3", None)
                setattr(value, "expression_Expression3", self)

class expression_SwitchExpression(Expression):

    pass
class expression_IfExpression(Expression):

    pass
class expression_SyntaxElement:

    pass
class SyntaxElement:

    pass
class expression_Identifier(SyntaxElement):

    def __init__(self, cl: str, id: str, expression_Identifier: "expression_CastedExpression" = None, expression_Identifier35: "expression_FeatureCall" = None, expression_Identifier44: "expression_Identifier" = None, expression_Identifier42: "expression_Identifier" = None, expression_Identifier39: "expression_ConstructorCallExpression" = None):
        self.cl = cl
        self.id = id
        self.expression_Identifier = expression_Identifier
        self.expression_Identifier35 = expression_Identifier35
        self.expression_Identifier44 = expression_Identifier44
        self.expression_Identifier42 = expression_Identifier42
        self.expression_Identifier39 = expression_Identifier39
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def cl(self) -> str:
        return self.__cl

    @cl.setter
    def cl(self, cl: str):
        self.__cl = cl

    @property
    def expression_Identifier42(self):
        return self.__expression_Identifier42

    @expression_Identifier42.setter
    def expression_Identifier42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expression_Identifier__expression_Identifier42", None)
        self.__expression_Identifier42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expression_Identifier44"):
                opp_val = getattr(old_value, "expression_Identifier44", None)
                if opp_val == self:
                    setattr(old_value, "expression_Identifier44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expression_Identifier44"):
                opp_val = getattr(value, "expression_Identifier44", None)
                setattr(value, "expression_Identifier44", self)

    @property
    def expression_Identifier(self):
        return self.__expression_Identifier

    @expression_Identifier.setter
    def expression_Identifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expression_Identifier__expression_Identifier", None)
        self.__expression_Identifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expression_CastedExpression"):
                opp_val = getattr(old_value, "expression_CastedExpression", None)
                if opp_val == self:
                    setattr(old_value, "expression_CastedExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expression_CastedExpression"):
                opp_val = getattr(value, "expression_CastedExpression", None)
                setattr(value, "expression_CastedExpression", self)

    @property
    def expression_Identifier44(self):
        return self.__expression_Identifier44

    @expression_Identifier44.setter
    def expression_Identifier44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expression_Identifier__expression_Identifier44", None)
        self.__expression_Identifier44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expression_Identifier42"):
                opp_val = getattr(old_value, "expression_Identifier42", None)
                if opp_val == self:
                    setattr(old_value, "expression_Identifier42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expression_Identifier42"):
                opp_val = getattr(value, "expression_Identifier42", None)
                setattr(value, "expression_Identifier42", self)

    @property
    def expression_Identifier35(self):
        return self.__expression_Identifier35

    @expression_Identifier35.setter
    def expression_Identifier35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expression_Identifier__expression_Identifier35", None)
        self.__expression_Identifier35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expression_FeatureCall34"):
                opp_val = getattr(old_value, "expression_FeatureCall34", None)
                if opp_val == self:
                    setattr(old_value, "expression_FeatureCall34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expression_FeatureCall34"):
                opp_val = getattr(value, "expression_FeatureCall34", None)
                setattr(value, "expression_FeatureCall34", self)

    @property
    def expression_Identifier39(self):
        return self.__expression_Identifier39

    @expression_Identifier39.setter
    def expression_Identifier39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expression_Identifier__expression_Identifier39", None)
        self.__expression_Identifier39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expression_ConstructorCallExpression"):
                opp_val = getattr(old_value, "expression_ConstructorCallExpression", None)
                if opp_val == self:
                    setattr(old_value, "expression_ConstructorCallExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expression_ConstructorCallExpression"):
                opp_val = getattr(value, "expression_ConstructorCallExpression", None)
                setattr(value, "expression_ConstructorCallExpression", self)

class expression_Case(SyntaxElement):

    pass
class expression_Expression(SyntaxElement):

    pass