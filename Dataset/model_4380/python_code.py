from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Prefix:

    pass
class AffectationPrefixStatement:

    pass
class leek_PrefixIncrement(AffectationPrefixStatement, Prefix):

    pass
class leek_PrefixDecrement(AffectationPrefixStatement, Prefix):

    pass
class ForInVariableReference:

    pass
class Expression:

    pass
class leek_Or(Expression):

    pass
class leek_StringLiteral(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class leek_Different(Expression):

    pass
class leek_UnitaryMinus(Expression):

    pass
class leek_TernaryIf(Expression):

    pass
class leek_TrueLiteral(Expression):

    pass
class leek_TypedDifferent(Expression):

    pass
class leek_More(Expression):

    pass
class leek_RealLiteral(Expression):

    def __init__(self, value: float):
        self.value = value
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

class leek_Not(Expression):

    pass
class leek_Plus(Expression):

    pass
class leek_IntLiteral(Expression):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class leek_And(Expression):

    pass
class leek_Multi(Expression):

    pass
class leek_Less(Expression):

    pass
class leek_NullLiteral(Expression):

    pass
class leek_Equals(Expression):

    pass
class leek_Div(Expression):

    pass
class leek_MoreOrEquals(Expression):

    pass
class leek_Minus(Expression):

    pass
class leek_LessOrEquals(Expression):

    pass
class leek_Comparison(Expression):

    pass
class leek_FalseLiteral(Expression):

    pass
class leek_ForInVariableReference:

    pass
class Postfix:

    pass
class AffectationPostfixStatement:

    pass
class leek_PostfixIncrement(AffectationPostfixStatement, Postfix):

    pass
class leek_PostfixDecrement(AffectationPostfixStatement, Postfix):

    pass
class leek_Prefix(Expression):

    pass
class leek_Postfix(Expression):

    pass
class leek_ArrayLiteral(Expression):

    pass
class leek_IfCondition:

    pass
class leek_ForAffectation:

    pass
class leek_ForInitializer:

    pass
class Iteration:

    pass
class leek_ForIn(Iteration):

    pass
class leek_For(Iteration):

    pass
class leek_While(Iteration):

    pass
class leek_Statement:

    pass
class leek_Script:

    pass
class leek_VariableReference(ForInVariableReference, AffectationPostfixStatement, Postfix):

    pass
class ForAffectation:

    pass
class ForInitializer:

    pass
class leek_VariableDeclaration(ForInitializer, ForInVariableReference):

    def __init__(self, byAdress: bool, name: str, leek_VariableDeclaration47: "leek_GlobalDeclaration" = None, leek_VariableDeclaration: "leek_FunctionDeclaration" = None, leek_VariableDeclaration45: "leek_LocalDeclaration" = None, leek_VariableDeclaration52: "leek_VariableReference" = None):
        self.byAdress = byAdress
        self.name = name
        self.leek_VariableDeclaration47 = leek_VariableDeclaration47
        self.leek_VariableDeclaration = leek_VariableDeclaration
        self.leek_VariableDeclaration45 = leek_VariableDeclaration45
        self.leek_VariableDeclaration52 = leek_VariableDeclaration52
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def byAdress(self) -> bool:
        return self.__byAdress

    @byAdress.setter
    def byAdress(self, byAdress: bool):
        self.__byAdress = byAdress

    @property
    def leek_VariableDeclaration(self):
        return self.__leek_VariableDeclaration

    @leek_VariableDeclaration.setter
    def leek_VariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_leek_VariableDeclaration__leek_VariableDeclaration", None)
        self.__leek_VariableDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "leek_FunctionDeclaration"):
                opp_val = getattr(old_value, "leek_FunctionDeclaration", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "leek_FunctionDeclaration"):
                opp_val = getattr(value, "leek_FunctionDeclaration", None)
                if opp_val is None:
                    setattr(value, "leek_FunctionDeclaration", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def leek_VariableDeclaration52(self):
        return self.__leek_VariableDeclaration52

    @leek_VariableDeclaration52.setter
    def leek_VariableDeclaration52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_leek_VariableDeclaration__leek_VariableDeclaration52", None)
        self.__leek_VariableDeclaration52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "leek_VariableReference51"):
                opp_val = getattr(old_value, "leek_VariableReference51", None)
                if opp_val == self:
                    setattr(old_value, "leek_VariableReference51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "leek_VariableReference51"):
                opp_val = getattr(value, "leek_VariableReference51", None)
                setattr(value, "leek_VariableReference51", self)

    @property
    def leek_VariableDeclaration47(self):
        return self.__leek_VariableDeclaration47

    @leek_VariableDeclaration47.setter
    def leek_VariableDeclaration47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_leek_VariableDeclaration__leek_VariableDeclaration47", None)
        self.__leek_VariableDeclaration47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "leek_GlobalDeclaration"):
                opp_val = getattr(old_value, "leek_GlobalDeclaration", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "leek_GlobalDeclaration"):
                opp_val = getattr(value, "leek_GlobalDeclaration", None)
                if opp_val is None:
                    setattr(value, "leek_GlobalDeclaration", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def leek_VariableDeclaration45(self):
        return self.__leek_VariableDeclaration45

    @leek_VariableDeclaration45.setter
    def leek_VariableDeclaration45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_leek_VariableDeclaration__leek_VariableDeclaration45", None)
        self.__leek_VariableDeclaration45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "leek_LocalDeclaration"):
                opp_val = getattr(old_value, "leek_LocalDeclaration", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "leek_LocalDeclaration"):
                opp_val = getattr(value, "leek_LocalDeclaration", None)
                if opp_val is None:
                    setattr(value, "leek_LocalDeclaration", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class IfCondition:

    pass
class leek_Expression(ForAffectation, IfCondition):

    pass
class AffectationStatement:

    pass
class leek_AffectationIncrement(AffectationStatement):

    pass
class leek_AffectationPrefixStatement(AffectationStatement):

    pass
class leek_AffectationDecrement(AffectationStatement):

    pass
class leek_AffectationPostfixStatement(AffectationStatement):

    pass
class leek_Affectation(AffectationStatement, ForInitializer, ForAffectation, IfCondition):

    pass
class Statement:

    pass
class leek_If(Statement):

    pass
class leek_StatementBlock(Statement):

    pass
class leek_ContinueStatement(Statement):

    pass
class leek_GlobalDeclaration(Statement):

    pass
class leek_FunctionCall(Statement, Expression):

    pass
class leek_AffectationStatement(Statement):

    pass
class leek_ReturnStatement(Statement):

    pass
class leek_LocalDeclaration(Statement):

    pass
class leek_Include(Statement):

    def __init__(self, importURI: str):
        self.importURI = importURI
        
    @property
    def importURI(self) -> str:
        return self.__importURI

    @importURI.setter
    def importURI(self, importURI: str):
        self.__importURI = importURI

class leek_Iteration(Statement):

    pass
class leek_FunctionDeclaration(Statement, Expression):

    def __init__(self, name: str, leek_FunctionDeclaration: set["leek_VariableDeclaration"] = None, leek_FunctionDeclaration42: "leek_StatementBlock" = None, leek_FunctionDeclaration57: "leek_FunctionCall" = None):
        self.name = name
        self.leek_FunctionDeclaration = leek_FunctionDeclaration if leek_FunctionDeclaration is not None else set()
        self.leek_FunctionDeclaration42 = leek_FunctionDeclaration42
        self.leek_FunctionDeclaration57 = leek_FunctionDeclaration57
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def leek_FunctionDeclaration42(self):
        return self.__leek_FunctionDeclaration42

    @leek_FunctionDeclaration42.setter
    def leek_FunctionDeclaration42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_leek_FunctionDeclaration__leek_FunctionDeclaration42", None)
        self.__leek_FunctionDeclaration42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "leek_StatementBlock43"):
                opp_val = getattr(old_value, "leek_StatementBlock43", None)
                if opp_val == self:
                    setattr(old_value, "leek_StatementBlock43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "leek_StatementBlock43"):
                opp_val = getattr(value, "leek_StatementBlock43", None)
                setattr(value, "leek_StatementBlock43", self)

    @property
    def leek_FunctionDeclaration(self):
        return self.__leek_FunctionDeclaration

    @leek_FunctionDeclaration.setter
    def leek_FunctionDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_leek_FunctionDeclaration__leek_FunctionDeclaration", None)
        self.__leek_FunctionDeclaration = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "leek_VariableDeclaration"):
                    opp_val = getattr(item, "leek_VariableDeclaration", None)
                    
                    if opp_val == self:
                        setattr(item, "leek_VariableDeclaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "leek_VariableDeclaration"):
                    opp_val = getattr(item, "leek_VariableDeclaration", None)
                    
                    setattr(item, "leek_VariableDeclaration", self)
                    

    @property
    def leek_FunctionDeclaration57(self):
        return self.__leek_FunctionDeclaration57

    @leek_FunctionDeclaration57.setter
    def leek_FunctionDeclaration57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_leek_FunctionDeclaration__leek_FunctionDeclaration57", None)
        self.__leek_FunctionDeclaration57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "leek_FunctionCall"):
                opp_val = getattr(old_value, "leek_FunctionCall", None)
                if opp_val == self:
                    setattr(old_value, "leek_FunctionCall", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "leek_FunctionCall"):
                opp_val = getattr(value, "leek_FunctionCall", None)
                setattr(value, "leek_FunctionCall", self)

class leek_EmptyStatement(Statement):

    pass
class leek_BreakStatement(Statement):

    pass