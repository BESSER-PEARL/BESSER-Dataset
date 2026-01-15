from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class edu_visitor_IASTNodeVisitor(ABC):

    def __init__(self):
        
    def visit(self, node: ASTNode):
        # TODO: Implement visit method
        pass

    def visit(self, node: str):
        # TODO: Implement visit method
        pass

    def visit(self, node: QuantifiedExpression):
        # TODO: Implement visit method
        pass

    def visit(self, node: str):
        # TODO: Implement visit method
        pass

    def visit(self, node: Assertion):
        # TODO: Implement visit method
        pass

    def visit(self, node: UnaryExpression):
        # TODO: Implement visit method
        pass

    def visit(self, node: str):
        # TODO: Implement visit method
        pass

    def visit(self, node: str):
        # TODO: Implement visit method
        pass

    def visit(self, node: Literal):
        # TODO: Implement visit method
        pass

    def visit(self, node: str):
        # TODO: Implement visit method
        pass

    def visit(self, node: str):
        # TODO: Implement visit method
        pass

    def visit(self, node: Sign):
        # TODO: Implement visit method
        pass

    def visit(self, node: str):
        # TODO: Implement visit method
        pass

    def visit(self, node: str):
        # TODO: Implement visit method
        pass

    def visit(self, node: str):
        # TODO: Implement visit method
        pass

    def visit(self, node: str):
        # TODO: Implement visit method
        pass

    def visit(self, node: str):
        # TODO: Implement visit method
        pass

    def visit(self, node: str):
        # TODO: Implement visit method
        pass

    def visit(self, node: str):
        # TODO: Implement visit method
        pass

    def visit(self, node: str):
        # TODO: Implement visit method
        pass

    def visit(self, node: str):
        # TODO: Implement visit method
        pass

    def visit(self, node: str):
        # TODO: Implement visit method
        pass

    def visit(self, node: str):
        # TODO: Implement visit method
        pass

    def visit(self, node: Type):
        # TODO: Implement visit method
        pass

    def visit(self, node: str):
        # TODO: Implement visit method
        pass

    def visit(self, node: str):
        # TODO: Implement visit method
        pass

    def visit(self, node: str):
        # TODO: Implement visit method
        pass

    def visit(self, node: PrimitiveType):
        # TODO: Implement visit method
        pass

    def visit(self, node: str):
        # TODO: Implement visit method
        pass

    def visit(self, node: str):
        # TODO: Implement visit method
        pass

    def visit(self, node: BinaryExpression):
        # TODO: Implement visit method
        pass

    def visit(self, node: str):
        # TODO: Implement visit method
        pass

    def visit(self, node: str):
        # TODO: Implement visit method
        pass

    def visit(self, node: str):
        # TODO: Implement visit method
        pass

    def visit(self, node: str):
        # TODO: Implement visit method
        pass

    def visit(self, node: str):
        # TODO: Implement visit method
        pass

    def visit(self, node: Expression):
        # TODO: Implement visit method
        pass

    def visit(self, node: str):
        # TODO: Implement visit method
        pass

    def visit(self, node: str):
        # TODO: Implement visit method
        pass

    def visit(self, node: Annotation):
        # TODO: Implement visit method
        pass

    def visit(self, node: str):
        # TODO: Implement visit method
        pass

    def visit(self, node: str):
        # TODO: Implement visit method
        pass

    def visit(self, node: str):
        # TODO: Implement visit method
        pass

    def visit(self, node: str):
        # TODO: Implement visit method
        pass

    def visit(self, node: str):
        # TODO: Implement visit method
        pass

    def visit(self, node: str):
        # TODO: Implement visit method
        pass

    def visit(self, node: str):
        # TODO: Implement visit method
        pass

    def visit(self, node: str):
        # TODO: Implement visit method
        pass

    def visit(self, node: str):
        # TODO: Implement visit method
        pass

    def visit(self, node: str):
        # TODO: Implement visit method
        pass

    def visit(self, node: str):
        # TODO: Implement visit method
        pass

    def visit(self, node: str):
        # TODO: Implement visit method
        pass

    def visit(self, node: SymbolReference):
        # TODO: Implement visit method
        pass

    def visit(self, node: str):
        # TODO: Implement visit method
        pass

    def visit(self, node: str):
        # TODO: Implement visit method
        pass

    def visit(self, node: Statement):
        # TODO: Implement visit method
        pass

class edu_ExpressionToExpressionMap:

    pass
class SymbolReference:

    pass
class edu_ReturnValueReference(SymbolReference):

    def __init__(self, edu_ReturnValueReference: "edu_FunctionDeclaration" = None):
        self.edu_ReturnValueReference = edu_ReturnValueReference
        
    @property
    def edu_ReturnValueReference(self):
        return self.__edu_ReturnValueReference

    @edu_ReturnValueReference.setter
    def edu_ReturnValueReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_ReturnValueReference__edu_ReturnValueReference", None)
        self.__edu_ReturnValueReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_FunctionDeclaration80"):
                opp_val = getattr(old_value, "edu_FunctionDeclaration80", None)
                if opp_val == self:
                    setattr(old_value, "edu_FunctionDeclaration80", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_FunctionDeclaration80"):
                opp_val = getattr(value, "edu_FunctionDeclaration80", None)
                setattr(value, "edu_FunctionDeclaration80", self)

    def accept(self, visitor: str):
        # TODO: Implement accept method
        pass

class UnaryExpression:

    pass
class edu_Negation(UnaryExpression):

    def __init__(self):
        
    def accept(self, visitor: str):
        # TODO: Implement accept method
        pass

class edu_Sign(UnaryExpression):

    def __init__(self):
        
    def accept(self, visitor: str):
        # TODO: Implement accept method
        pass

class Sign:

    pass
class edu_Plus(Sign):

    def __init__(self):
        
    def accept(self, visitor: str):
        # TODO: Implement accept method
        pass

class edu_Minus(Sign):

    def __init__(self):
        
    def accept(self, visitor: str):
        # TODO: Implement accept method
        pass

class FunctionAnnotation:

    pass
class edu_Postcondition(FunctionAnnotation):

    def __init__(self, edu_Postcondition: "edu_FunctionDeclaration" = None):
        self.edu_Postcondition = edu_Postcondition
        
    @property
    def edu_Postcondition(self):
        return self.__edu_Postcondition

    @edu_Postcondition.setter
    def edu_Postcondition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_Postcondition__edu_Postcondition", None)
        self.__edu_Postcondition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_FunctionDeclaration54"):
                opp_val = getattr(old_value, "edu_FunctionDeclaration54", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_FunctionDeclaration54"):
                opp_val = getattr(value, "edu_FunctionDeclaration54", None)
                if opp_val is None:
                    setattr(value, "edu_FunctionDeclaration54", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def accept(self, visitor: str):
        # TODO: Implement accept method
        pass

class edu_Precondition(FunctionAnnotation):

    def __init__(self, edu_Precondition: "edu_FunctionDeclaration" = None):
        self.edu_Precondition = edu_Precondition
        
    @property
    def edu_Precondition(self):
        return self.__edu_Precondition

    @edu_Precondition.setter
    def edu_Precondition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_Precondition__edu_Precondition", None)
        self.__edu_Precondition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_FunctionDeclaration52"):
                opp_val = getattr(old_value, "edu_FunctionDeclaration52", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_FunctionDeclaration52"):
                opp_val = getattr(value, "edu_FunctionDeclaration52", None)
                if opp_val is None:
                    setattr(value, "edu_FunctionDeclaration52", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def accept(self, visitor: str):
        # TODO: Implement accept method
        pass

class PrimitiveType:

    pass
class edu_IntegerType(PrimitiveType):

    def __init__(self):
        
    def accept(self, visitor: str):
        # TODO: Implement accept method
        pass

class edu_BooleanType(PrimitiveType):

    def __init__(self):
        
    def accept(self, visitor: str):
        # TODO: Implement accept method
        pass

class QuantifiedExpression:

    pass
class edu_ForAllQuantifier(QuantifiedExpression):

    def __init__(self):
        
    def accept(self, visitor: str):
        # TODO: Implement accept method
        pass

class edu_ExistsQuantifier(QuantifiedExpression):

    def __init__(self):
        
    def accept(self, visitor: str):
        # TODO: Implement accept method
        pass

class edu_VariableReference(SymbolReference):

    def __init__(self, edu_VariableReference: "edu_Assignment" = None, edu_VariableReference77: "edu_VariableDeclaration" = None):
        self.edu_VariableReference = edu_VariableReference
        self.edu_VariableReference77 = edu_VariableReference77
        
    @property
    def edu_VariableReference(self):
        return self.__edu_VariableReference

    @edu_VariableReference.setter
    def edu_VariableReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_VariableReference__edu_VariableReference", None)
        self.__edu_VariableReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_Assignment22"):
                opp_val = getattr(old_value, "edu_Assignment22", None)
                if opp_val == self:
                    setattr(old_value, "edu_Assignment22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_Assignment22"):
                opp_val = getattr(value, "edu_Assignment22", None)
                setattr(value, "edu_Assignment22", self)

    @property
    def edu_VariableReference77(self):
        return self.__edu_VariableReference77

    @edu_VariableReference77.setter
    def edu_VariableReference77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_VariableReference__edu_VariableReference77", None)
        self.__edu_VariableReference77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_VariableDeclaration78"):
                opp_val = getattr(old_value, "edu_VariableDeclaration78", None)
                if opp_val == self:
                    setattr(old_value, "edu_VariableDeclaration78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_VariableDeclaration78"):
                opp_val = getattr(value, "edu_VariableDeclaration78", None)
                setattr(value, "edu_VariableDeclaration78", self)

    def accept(self, visitor: str):
        # TODO: Implement accept method
        pass

class Assertion:

    pass
class edu_GuardAssertion(Assertion):

    def __init__(self):
        
    def accept(self, visitor: str):
        # TODO: Implement accept method
        pass

class Annotation:

    pass
class edu_FunctionAnnotation(Annotation):

    def __init__(self):
        
    def accept(self, visitor: str):
        # TODO: Implement accept method
        pass

class edu_Invariant(Annotation):

    def __init__(self, edu_Invariant: "edu_Loop" = None):
        self.edu_Invariant = edu_Invariant
        
    @property
    def edu_Invariant(self):
        return self.__edu_Invariant

    @edu_Invariant.setter
    def edu_Invariant(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_Invariant__edu_Invariant", None)
        self.__edu_Invariant = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_Loop70"):
                opp_val = getattr(old_value, "edu_Loop70", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_Loop70"):
                opp_val = getattr(value, "edu_Loop70", None)
                if opp_val is None:
                    setattr(value, "edu_Loop70", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def accept(self, visitor: str):
        # TODO: Implement accept method
        pass

class edu_Assumption(Annotation):

    def __init__(self):
        
    def accept(self, visitor: str):
        # TODO: Implement accept method
        pass

class edu_Assertion(Annotation):

    def __init__(self):
        
    def accept(self, visitor: str):
        # TODO: Implement accept method
        pass

class Statement:

    pass
class edu_VariableDeclaration(Statement):

    def __init__(self, name: str, edu_VariableDeclaration: "edu_Type" = None, edu_VariableDeclaration25: "edu_Expression" = None, edu_VariableDeclaration57: "edu_FunctionDeclaration" = None, edu_VariableDeclaration38: "edu_QuantifiedExpression" = None, edu_VariableDeclaration78: "edu_VariableReference" = None, edu_VariableDeclaration112: "edu_LetExpression" = None):
        self.name = name
        self.edu_VariableDeclaration = edu_VariableDeclaration
        self.edu_VariableDeclaration25 = edu_VariableDeclaration25
        self.edu_VariableDeclaration57 = edu_VariableDeclaration57
        self.edu_VariableDeclaration38 = edu_VariableDeclaration38
        self.edu_VariableDeclaration78 = edu_VariableDeclaration78
        self.edu_VariableDeclaration112 = edu_VariableDeclaration112
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def edu_VariableDeclaration78(self):
        return self.__edu_VariableDeclaration78

    @edu_VariableDeclaration78.setter
    def edu_VariableDeclaration78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_VariableDeclaration__edu_VariableDeclaration78", None)
        self.__edu_VariableDeclaration78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_VariableReference77"):
                opp_val = getattr(old_value, "edu_VariableReference77", None)
                if opp_val == self:
                    setattr(old_value, "edu_VariableReference77", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_VariableReference77"):
                opp_val = getattr(value, "edu_VariableReference77", None)
                setattr(value, "edu_VariableReference77", self)

    @property
    def edu_VariableDeclaration(self):
        return self.__edu_VariableDeclaration

    @edu_VariableDeclaration.setter
    def edu_VariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_VariableDeclaration__edu_VariableDeclaration", None)
        self.__edu_VariableDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_Type"):
                opp_val = getattr(old_value, "edu_Type", None)
                if opp_val == self:
                    setattr(old_value, "edu_Type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_Type"):
                opp_val = getattr(value, "edu_Type", None)
                setattr(value, "edu_Type", self)

    @property
    def edu_VariableDeclaration57(self):
        return self.__edu_VariableDeclaration57

    @edu_VariableDeclaration57.setter
    def edu_VariableDeclaration57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_VariableDeclaration__edu_VariableDeclaration57", None)
        self.__edu_VariableDeclaration57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_FunctionDeclaration56"):
                opp_val = getattr(old_value, "edu_FunctionDeclaration56", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_FunctionDeclaration56"):
                opp_val = getattr(value, "edu_FunctionDeclaration56", None)
                if opp_val is None:
                    setattr(value, "edu_FunctionDeclaration56", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def edu_VariableDeclaration38(self):
        return self.__edu_VariableDeclaration38

    @edu_VariableDeclaration38.setter
    def edu_VariableDeclaration38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_VariableDeclaration__edu_VariableDeclaration38", None)
        self.__edu_VariableDeclaration38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_QuantifiedExpression"):
                opp_val = getattr(old_value, "edu_QuantifiedExpression", None)
                if opp_val == self:
                    setattr(old_value, "edu_QuantifiedExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_QuantifiedExpression"):
                opp_val = getattr(value, "edu_QuantifiedExpression", None)
                setattr(value, "edu_QuantifiedExpression", self)

    @property
    def edu_VariableDeclaration25(self):
        return self.__edu_VariableDeclaration25

    @edu_VariableDeclaration25.setter
    def edu_VariableDeclaration25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_VariableDeclaration__edu_VariableDeclaration25", None)
        self.__edu_VariableDeclaration25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_Expression26"):
                opp_val = getattr(old_value, "edu_Expression26", None)
                if opp_val == self:
                    setattr(old_value, "edu_Expression26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_Expression26"):
                opp_val = getattr(value, "edu_Expression26", None)
                setattr(value, "edu_Expression26", self)

    @property
    def edu_VariableDeclaration112(self):
        return self.__edu_VariableDeclaration112

    @edu_VariableDeclaration112.setter
    def edu_VariableDeclaration112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_VariableDeclaration__edu_VariableDeclaration112", None)
        self.__edu_VariableDeclaration112 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_LetExpression"):
                opp_val = getattr(old_value, "edu_LetExpression", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_LetExpression"):
                opp_val = getattr(value, "edu_LetExpression", None)
                if opp_val is None:
                    setattr(value, "edu_LetExpression", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def accept(self, visitor: str):
        # TODO: Implement accept method
        pass

class edu_Loop(Statement):

    def __init__(self, edu_Loop: "edu_Expression" = None, edu_Loop67: "edu_Block" = None, edu_Loop70: set["edu_Invariant"] = None):
        self.edu_Loop = edu_Loop
        self.edu_Loop67 = edu_Loop67
        self.edu_Loop70 = edu_Loop70 if edu_Loop70 is not None else set()
        
    @property
    def edu_Loop(self):
        return self.__edu_Loop

    @edu_Loop.setter
    def edu_Loop(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_Loop__edu_Loop", None)
        self.__edu_Loop = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_Expression65"):
                opp_val = getattr(old_value, "edu_Expression65", None)
                if opp_val == self:
                    setattr(old_value, "edu_Expression65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_Expression65"):
                opp_val = getattr(value, "edu_Expression65", None)
                setattr(value, "edu_Expression65", self)

    @property
    def edu_Loop67(self):
        return self.__edu_Loop67

    @edu_Loop67.setter
    def edu_Loop67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_Loop__edu_Loop67", None)
        self.__edu_Loop67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_Block68"):
                opp_val = getattr(old_value, "edu_Block68", None)
                if opp_val == self:
                    setattr(old_value, "edu_Block68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_Block68"):
                opp_val = getattr(value, "edu_Block68", None)
                setattr(value, "edu_Block68", self)

    @property
    def edu_Loop70(self):
        return self.__edu_Loop70

    @edu_Loop70.setter
    def edu_Loop70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_Loop__edu_Loop70", None)
        self.__edu_Loop70 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "edu_Invariant"):
                    opp_val = getattr(item, "edu_Invariant", None)
                    
                    if opp_val == self:
                        setattr(item, "edu_Invariant", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "edu_Invariant"):
                    opp_val = getattr(item, "edu_Invariant", None)
                    
                    setattr(item, "edu_Invariant", self)
                    

    def accept(self, visitor: str):
        # TODO: Implement accept method
        pass

class edu_Assignment(Statement):

    def __init__(self, edu_Assignment: "edu_Expression" = None, edu_Assignment22: "edu_VariableReference" = None):
        self.edu_Assignment = edu_Assignment
        self.edu_Assignment22 = edu_Assignment22
        
    @property
    def edu_Assignment22(self):
        return self.__edu_Assignment22

    @edu_Assignment22.setter
    def edu_Assignment22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_Assignment__edu_Assignment22", None)
        self.__edu_Assignment22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_VariableReference"):
                opp_val = getattr(old_value, "edu_VariableReference", None)
                if opp_val == self:
                    setattr(old_value, "edu_VariableReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_VariableReference"):
                opp_val = getattr(value, "edu_VariableReference", None)
                setattr(value, "edu_VariableReference", self)

    @property
    def edu_Assignment(self):
        return self.__edu_Assignment

    @edu_Assignment.setter
    def edu_Assignment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_Assignment__edu_Assignment", None)
        self.__edu_Assignment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_Expression20"):
                opp_val = getattr(old_value, "edu_Expression20", None)
                if opp_val == self:
                    setattr(old_value, "edu_Expression20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_Expression20"):
                opp_val = getattr(value, "edu_Expression20", None)
                setattr(value, "edu_Expression20", self)

    def accept(self, visitor: str):
        # TODO: Implement accept method
        pass

class edu_Conditional(Statement):

    def __init__(self, edu_Conditional35: "edu_Block" = None, edu_Conditional: "edu_Expression" = None, edu_Conditional32: "edu_Block" = None):
        self.edu_Conditional35 = edu_Conditional35
        self.edu_Conditional = edu_Conditional
        self.edu_Conditional32 = edu_Conditional32
        
    @property
    def edu_Conditional35(self):
        return self.__edu_Conditional35

    @edu_Conditional35.setter
    def edu_Conditional35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_Conditional__edu_Conditional35", None)
        self.__edu_Conditional35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_Block36"):
                opp_val = getattr(old_value, "edu_Block36", None)
                if opp_val == self:
                    setattr(old_value, "edu_Block36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_Block36"):
                opp_val = getattr(value, "edu_Block36", None)
                setattr(value, "edu_Block36", self)

    @property
    def edu_Conditional32(self):
        return self.__edu_Conditional32

    @edu_Conditional32.setter
    def edu_Conditional32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_Conditional__edu_Conditional32", None)
        self.__edu_Conditional32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_Block33"):
                opp_val = getattr(old_value, "edu_Block33", None)
                if opp_val == self:
                    setattr(old_value, "edu_Block33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_Block33"):
                opp_val = getattr(value, "edu_Block33", None)
                setattr(value, "edu_Block33", self)

    @property
    def edu_Conditional(self):
        return self.__edu_Conditional

    @edu_Conditional.setter
    def edu_Conditional(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_Conditional__edu_Conditional", None)
        self.__edu_Conditional = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_Expression30"):
                opp_val = getattr(old_value, "edu_Expression30", None)
                if opp_val == self:
                    setattr(old_value, "edu_Expression30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_Expression30"):
                opp_val = getattr(value, "edu_Expression30", None)
                setattr(value, "edu_Expression30", self)

    def accept(self, visitor: str):
        # TODO: Implement accept method
        pass

class edu_ReturnStatement(Statement):

    def __init__(self, edu_ReturnStatement: "edu_Expression" = None, edu_ReturnStatement74: "edu_FunctionDeclaration" = None):
        self.edu_ReturnStatement = edu_ReturnStatement
        self.edu_ReturnStatement74 = edu_ReturnStatement74
        
    @property
    def edu_ReturnStatement74(self):
        return self.__edu_ReturnStatement74

    @edu_ReturnStatement74.setter
    def edu_ReturnStatement74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_ReturnStatement__edu_ReturnStatement74", None)
        self.__edu_ReturnStatement74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_FunctionDeclaration75"):
                opp_val = getattr(old_value, "edu_FunctionDeclaration75", None)
                if opp_val == self:
                    setattr(old_value, "edu_FunctionDeclaration75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_FunctionDeclaration75"):
                opp_val = getattr(value, "edu_FunctionDeclaration75", None)
                setattr(value, "edu_FunctionDeclaration75", self)

    @property
    def edu_ReturnStatement(self):
        return self.__edu_ReturnStatement

    @edu_ReturnStatement.setter
    def edu_ReturnStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_ReturnStatement__edu_ReturnStatement", None)
        self.__edu_ReturnStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_Expression72"):
                opp_val = getattr(old_value, "edu_Expression72", None)
                if opp_val == self:
                    setattr(old_value, "edu_Expression72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_Expression72"):
                opp_val = getattr(value, "edu_Expression72", None)
                setattr(value, "edu_Expression72", self)

    def accept(self, visitor: str):
        # TODO: Implement accept method
        pass

class edu_Annotation(Statement):

    def __init__(self, edu_Annotation: "edu_Expression" = None):
        self.edu_Annotation = edu_Annotation
        
    @property
    def edu_Annotation(self):
        return self.__edu_Annotation

    @edu_Annotation.setter
    def edu_Annotation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_Annotation__edu_Annotation", None)
        self.__edu_Annotation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_Expression18"):
                opp_val = getattr(old_value, "edu_Expression18", None)
                if opp_val == self:
                    setattr(old_value, "edu_Expression18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_Expression18"):
                opp_val = getattr(value, "edu_Expression18", None)
                setattr(value, "edu_Expression18", self)

    def accept(self, visitor: str):
        # TODO: Implement accept method
        pass

class GuardAssertion:

    pass
class edu_DivisorNotZeroAssertion(GuardAssertion):

    def __init__(self, edu_DivisorNotZeroAssertion: "edu_Expression" = None):
        self.edu_DivisorNotZeroAssertion = edu_DivisorNotZeroAssertion
        
    @property
    def edu_DivisorNotZeroAssertion(self):
        return self.__edu_DivisorNotZeroAssertion

    @edu_DivisorNotZeroAssertion.setter
    def edu_DivisorNotZeroAssertion(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_DivisorNotZeroAssertion__edu_DivisorNotZeroAssertion", None)
        self.__edu_DivisorNotZeroAssertion = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_Expression16"):
                opp_val = getattr(old_value, "edu_Expression16", None)
                if opp_val == self:
                    setattr(old_value, "edu_Expression16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_Expression16"):
                opp_val = getattr(value, "edu_Expression16", None)
                setattr(value, "edu_Expression16", self)

    def accept(self, visitor: str):
        # TODO: Implement accept method
        pass

class edu_FunctionCallPreconditionAssertion(GuardAssertion):

    def __init__(self, edu_FunctionCallPreconditionAssertion: "edu_FunctionCall" = None):
        self.edu_FunctionCallPreconditionAssertion = edu_FunctionCallPreconditionAssertion
        
    @property
    def edu_FunctionCallPreconditionAssertion(self):
        return self.__edu_FunctionCallPreconditionAssertion

    @edu_FunctionCallPreconditionAssertion.setter
    def edu_FunctionCallPreconditionAssertion(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_FunctionCallPreconditionAssertion__edu_FunctionCallPreconditionAssertion", None)
        self.__edu_FunctionCallPreconditionAssertion = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_FunctionCall"):
                opp_val = getattr(old_value, "edu_FunctionCall", None)
                if opp_val == self:
                    setattr(old_value, "edu_FunctionCall", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_FunctionCall"):
                opp_val = getattr(value, "edu_FunctionCall", None)
                setattr(value, "edu_FunctionCall", self)

    def accept(self, visitor: str):
        # TODO: Implement accept method
        pass

class Expression:

    pass
class edu_SymbolReference(Expression):

    def __init__(self, edu_SymbolReference: "edu_Expression" = None):
        self.edu_SymbolReference = edu_SymbolReference
        
    @property
    def edu_SymbolReference(self):
        return self.__edu_SymbolReference

    @edu_SymbolReference.setter
    def edu_SymbolReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_SymbolReference__edu_SymbolReference", None)
        self.__edu_SymbolReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_Expression82"):
                opp_val = getattr(old_value, "edu_Expression82", None)
                if opp_val == self:
                    setattr(old_value, "edu_Expression82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_Expression82"):
                opp_val = getattr(value, "edu_Expression82", None)
                setattr(value, "edu_Expression82", self)

    def accept(self, visitor: str):
        # TODO: Implement accept method
        pass

class edu_TernaryExpression(Expression):

    def __init__(self, edu_TernaryExpression: "edu_Expression" = None, edu_TernaryExpression106: "edu_Expression" = None, edu_TernaryExpression109: "edu_Expression" = None):
        self.edu_TernaryExpression = edu_TernaryExpression
        self.edu_TernaryExpression106 = edu_TernaryExpression106
        self.edu_TernaryExpression109 = edu_TernaryExpression109
        
    @property
    def edu_TernaryExpression109(self):
        return self.__edu_TernaryExpression109

    @edu_TernaryExpression109.setter
    def edu_TernaryExpression109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_TernaryExpression__edu_TernaryExpression109", None)
        self.__edu_TernaryExpression109 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_Expression110"):
                opp_val = getattr(old_value, "edu_Expression110", None)
                if opp_val == self:
                    setattr(old_value, "edu_Expression110", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_Expression110"):
                opp_val = getattr(value, "edu_Expression110", None)
                setattr(value, "edu_Expression110", self)

    @property
    def edu_TernaryExpression(self):
        return self.__edu_TernaryExpression

    @edu_TernaryExpression.setter
    def edu_TernaryExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_TernaryExpression__edu_TernaryExpression", None)
        self.__edu_TernaryExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_Expression104"):
                opp_val = getattr(old_value, "edu_Expression104", None)
                if opp_val == self:
                    setattr(old_value, "edu_Expression104", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_Expression104"):
                opp_val = getattr(value, "edu_Expression104", None)
                setattr(value, "edu_Expression104", self)

    @property
    def edu_TernaryExpression106(self):
        return self.__edu_TernaryExpression106

    @edu_TernaryExpression106.setter
    def edu_TernaryExpression106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_TernaryExpression__edu_TernaryExpression106", None)
        self.__edu_TernaryExpression106 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_Expression107"):
                opp_val = getattr(old_value, "edu_Expression107", None)
                if opp_val == self:
                    setattr(old_value, "edu_Expression107", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_Expression107"):
                opp_val = getattr(value, "edu_Expression107", None)
                setattr(value, "edu_Expression107", self)

    def accept(self, visitor: str):
        # TODO: Implement accept method
        pass

class edu_LetExpression(Expression):

    pass
class edu_ArrayAccess(Expression):

    def __init__(self, edu_ArrayAccess: "edu_Expression" = None, edu_ArrayAccess96: "edu_Expression" = None):
        self.edu_ArrayAccess = edu_ArrayAccess
        self.edu_ArrayAccess96 = edu_ArrayAccess96
        
    @property
    def edu_ArrayAccess(self):
        return self.__edu_ArrayAccess

    @edu_ArrayAccess.setter
    def edu_ArrayAccess(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_ArrayAccess__edu_ArrayAccess", None)
        self.__edu_ArrayAccess = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_Expression94"):
                opp_val = getattr(old_value, "edu_Expression94", None)
                if opp_val == self:
                    setattr(old_value, "edu_Expression94", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_Expression94"):
                opp_val = getattr(value, "edu_Expression94", None)
                setattr(value, "edu_Expression94", self)

    @property
    def edu_ArrayAccess96(self):
        return self.__edu_ArrayAccess96

    @edu_ArrayAccess96.setter
    def edu_ArrayAccess96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_ArrayAccess__edu_ArrayAccess96", None)
        self.__edu_ArrayAccess96 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_Expression97"):
                opp_val = getattr(old_value, "edu_Expression97", None)
                if opp_val == self:
                    setattr(old_value, "edu_Expression97", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_Expression97"):
                opp_val = getattr(value, "edu_Expression97", None)
                setattr(value, "edu_Expression97", self)

    def accept(self, visitor: str):
        # TODO: Implement accept method
        pass

class edu_QuantifiedExpression(Expression):

    def __init__(self, edu_QuantifiedExpression: "edu_VariableDeclaration" = None, edu_QuantifiedExpression40: "edu_Expression" = None, edu_QuantifiedExpression43: "edu_Expression" = None):
        self.edu_QuantifiedExpression = edu_QuantifiedExpression
        self.edu_QuantifiedExpression40 = edu_QuantifiedExpression40
        self.edu_QuantifiedExpression43 = edu_QuantifiedExpression43
        
    @property
    def edu_QuantifiedExpression(self):
        return self.__edu_QuantifiedExpression

    @edu_QuantifiedExpression.setter
    def edu_QuantifiedExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_QuantifiedExpression__edu_QuantifiedExpression", None)
        self.__edu_QuantifiedExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_VariableDeclaration38"):
                opp_val = getattr(old_value, "edu_VariableDeclaration38", None)
                if opp_val == self:
                    setattr(old_value, "edu_VariableDeclaration38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_VariableDeclaration38"):
                opp_val = getattr(value, "edu_VariableDeclaration38", None)
                setattr(value, "edu_VariableDeclaration38", self)

    @property
    def edu_QuantifiedExpression40(self):
        return self.__edu_QuantifiedExpression40

    @edu_QuantifiedExpression40.setter
    def edu_QuantifiedExpression40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_QuantifiedExpression__edu_QuantifiedExpression40", None)
        self.__edu_QuantifiedExpression40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_Expression41"):
                opp_val = getattr(old_value, "edu_Expression41", None)
                if opp_val == self:
                    setattr(old_value, "edu_Expression41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_Expression41"):
                opp_val = getattr(value, "edu_Expression41", None)
                setattr(value, "edu_Expression41", self)

    @property
    def edu_QuantifiedExpression43(self):
        return self.__edu_QuantifiedExpression43

    @edu_QuantifiedExpression43.setter
    def edu_QuantifiedExpression43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_QuantifiedExpression__edu_QuantifiedExpression43", None)
        self.__edu_QuantifiedExpression43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_Expression44"):
                opp_val = getattr(old_value, "edu_Expression44", None)
                if opp_val == self:
                    setattr(old_value, "edu_Expression44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_Expression44"):
                opp_val = getattr(value, "edu_Expression44", None)
                setattr(value, "edu_Expression44", self)

    def accept(self, visitor: str):
        # TODO: Implement accept method
        pass

class edu_FunctionCall(Expression):

    def __init__(self, edu_FunctionCall: "edu_FunctionCallPreconditionAssertion" = None, edu_FunctionCall46: set["edu_Expression"] = None, edu_FunctionCall49: "edu_FunctionDeclaration" = None):
        self.edu_FunctionCall = edu_FunctionCall
        self.edu_FunctionCall46 = edu_FunctionCall46 if edu_FunctionCall46 is not None else set()
        self.edu_FunctionCall49 = edu_FunctionCall49
        
    @property
    def edu_FunctionCall49(self):
        return self.__edu_FunctionCall49

    @edu_FunctionCall49.setter
    def edu_FunctionCall49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_FunctionCall__edu_FunctionCall49", None)
        self.__edu_FunctionCall49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_FunctionDeclaration50"):
                opp_val = getattr(old_value, "edu_FunctionDeclaration50", None)
                if opp_val == self:
                    setattr(old_value, "edu_FunctionDeclaration50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_FunctionDeclaration50"):
                opp_val = getattr(value, "edu_FunctionDeclaration50", None)
                setattr(value, "edu_FunctionDeclaration50", self)

    @property
    def edu_FunctionCall(self):
        return self.__edu_FunctionCall

    @edu_FunctionCall.setter
    def edu_FunctionCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_FunctionCall__edu_FunctionCall", None)
        self.__edu_FunctionCall = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_FunctionCallPreconditionAssertion"):
                opp_val = getattr(old_value, "edu_FunctionCallPreconditionAssertion", None)
                if opp_val == self:
                    setattr(old_value, "edu_FunctionCallPreconditionAssertion", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_FunctionCallPreconditionAssertion"):
                opp_val = getattr(value, "edu_FunctionCallPreconditionAssertion", None)
                setattr(value, "edu_FunctionCallPreconditionAssertion", self)

    @property
    def edu_FunctionCall46(self):
        return self.__edu_FunctionCall46

    @edu_FunctionCall46.setter
    def edu_FunctionCall46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_FunctionCall__edu_FunctionCall46", None)
        self.__edu_FunctionCall46 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "edu_Expression47"):
                    opp_val = getattr(item, "edu_Expression47", None)
                    
                    if opp_val == self:
                        setattr(item, "edu_Expression47", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "edu_Expression47"):
                    opp_val = getattr(item, "edu_Expression47", None)
                    
                    setattr(item, "edu_Expression47", self)
                    

    def accept(self, visitor: str):
        # TODO: Implement accept method
        pass

class edu_BinaryExpression(Expression):

    def __init__(self, edu_BinaryExpression: "edu_Expression" = None, edu_BinaryExpression7: "edu_Expression" = None):
        self.edu_BinaryExpression = edu_BinaryExpression
        self.edu_BinaryExpression7 = edu_BinaryExpression7
        
    @property
    def edu_BinaryExpression7(self):
        return self.__edu_BinaryExpression7

    @edu_BinaryExpression7.setter
    def edu_BinaryExpression7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_BinaryExpression__edu_BinaryExpression7", None)
        self.__edu_BinaryExpression7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_Expression8"):
                opp_val = getattr(old_value, "edu_Expression8", None)
                if opp_val == self:
                    setattr(old_value, "edu_Expression8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_Expression8"):
                opp_val = getattr(value, "edu_Expression8", None)
                setattr(value, "edu_Expression8", self)

    @property
    def edu_BinaryExpression(self):
        return self.__edu_BinaryExpression

    @edu_BinaryExpression.setter
    def edu_BinaryExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_BinaryExpression__edu_BinaryExpression", None)
        self.__edu_BinaryExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_Expression"):
                opp_val = getattr(old_value, "edu_Expression", None)
                if opp_val == self:
                    setattr(old_value, "edu_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_Expression"):
                opp_val = getattr(value, "edu_Expression", None)
                setattr(value, "edu_Expression", self)

    def accept(self, visitor: str):
        # TODO: Implement accept method
        pass

class Type:

    pass
class edu_PrimitiveType(Type):

    def __init__(self, edu_PrimitiveType: "edu_ArrayType" = None):
        self.edu_PrimitiveType = edu_PrimitiveType
        
    @property
    def edu_PrimitiveType(self):
        return self.__edu_PrimitiveType

    @edu_PrimitiveType.setter
    def edu_PrimitiveType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_PrimitiveType__edu_PrimitiveType", None)
        self.__edu_PrimitiveType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_ArrayType"):
                opp_val = getattr(old_value, "edu_ArrayType", None)
                if opp_val == self:
                    setattr(old_value, "edu_ArrayType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_ArrayType"):
                opp_val = getattr(value, "edu_ArrayType", None)
                setattr(value, "edu_ArrayType", self)

    def accept(self, visitor: str):
        # TODO: Implement accept method
        pass

class edu_ArrayType(Type):

    def __init__(self, edu_ArrayType: "edu_PrimitiveType" = None):
        self.edu_ArrayType = edu_ArrayType
        
    @property
    def edu_ArrayType(self):
        return self.__edu_ArrayType

    @edu_ArrayType.setter
    def edu_ArrayType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_ArrayType__edu_ArrayType", None)
        self.__edu_ArrayType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_PrimitiveType"):
                opp_val = getattr(old_value, "edu_PrimitiveType", None)
                if opp_val == self:
                    setattr(old_value, "edu_PrimitiveType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_PrimitiveType"):
                opp_val = getattr(value, "edu_PrimitiveType", None)
                setattr(value, "edu_PrimitiveType", self)

    def accept(self, visitor: str):
        # TODO: Implement accept method
        pass

class edu_Literal(Expression):

    def __init__(self):
        
    def accept(self, visitor: str):
        # TODO: Implement accept method
        pass

class Literal:

    pass
class edu_ArrayFunction(Literal):

    def __init__(self, edu_ArrayFunction: "edu_Expression" = None, edu_ArrayFunction88: "edu_Expression" = None, edu_ArrayFunction91: "edu_Expression" = None):
        self.edu_ArrayFunction = edu_ArrayFunction
        self.edu_ArrayFunction88 = edu_ArrayFunction88
        self.edu_ArrayFunction91 = edu_ArrayFunction91
        
    @property
    def edu_ArrayFunction(self):
        return self.__edu_ArrayFunction

    @edu_ArrayFunction.setter
    def edu_ArrayFunction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_ArrayFunction__edu_ArrayFunction", None)
        self.__edu_ArrayFunction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_Expression86"):
                opp_val = getattr(old_value, "edu_Expression86", None)
                if opp_val == self:
                    setattr(old_value, "edu_Expression86", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_Expression86"):
                opp_val = getattr(value, "edu_Expression86", None)
                setattr(value, "edu_Expression86", self)

    @property
    def edu_ArrayFunction88(self):
        return self.__edu_ArrayFunction88

    @edu_ArrayFunction88.setter
    def edu_ArrayFunction88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_ArrayFunction__edu_ArrayFunction88", None)
        self.__edu_ArrayFunction88 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_Expression89"):
                opp_val = getattr(old_value, "edu_Expression89", None)
                if opp_val == self:
                    setattr(old_value, "edu_Expression89", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_Expression89"):
                opp_val = getattr(value, "edu_Expression89", None)
                setattr(value, "edu_Expression89", self)

    @property
    def edu_ArrayFunction91(self):
        return self.__edu_ArrayFunction91

    @edu_ArrayFunction91.setter
    def edu_ArrayFunction91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_ArrayFunction__edu_ArrayFunction91", None)
        self.__edu_ArrayFunction91 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_Expression92"):
                opp_val = getattr(old_value, "edu_Expression92", None)
                if opp_val == self:
                    setattr(old_value, "edu_Expression92", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_Expression92"):
                opp_val = getattr(value, "edu_Expression92", None)
                setattr(value, "edu_Expression92", self)

    def accept(self, visitor: str):
        # TODO: Implement accept method
        pass

class edu_BooleanLiteral(Literal):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

    def getValue(self) -> bool:
        # TODO: Implement getValue method
        pass

    def accept(self, visitor: str):
        # TODO: Implement accept method
        pass

class edu_IntegerLiteral(Literal):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    def accept(self, visitor: str):
        # TODO: Implement accept method
        pass

class edu_ArrayLiteral(Literal):

    def __init__(self, edu_ArrayLiteral: set["edu_Expression"] = None):
        self.edu_ArrayLiteral = edu_ArrayLiteral if edu_ArrayLiteral is not None else set()
        
    @property
    def edu_ArrayLiteral(self):
        return self.__edu_ArrayLiteral

    @edu_ArrayLiteral.setter
    def edu_ArrayLiteral(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_ArrayLiteral__edu_ArrayLiteral", None)
        self.__edu_ArrayLiteral = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "edu_Expression12"):
                    opp_val = getattr(item, "edu_Expression12", None)
                    
                    if opp_val == self:
                        setattr(item, "edu_Expression12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "edu_Expression12"):
                    opp_val = getattr(item, "edu_Expression12", None)
                    
                    setattr(item, "edu_Expression12", self)
                    

    def accept(self, visitor: str):
        # TODO: Implement accept method
        pass

class edu_UnaryExpression(Expression):

    def __init__(self, edu_UnaryExpression: "edu_Expression" = None):
        self.edu_UnaryExpression = edu_UnaryExpression
        
    @property
    def edu_UnaryExpression(self):
        return self.__edu_UnaryExpression

    @edu_UnaryExpression.setter
    def edu_UnaryExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_UnaryExpression__edu_UnaryExpression", None)
        self.__edu_UnaryExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_Expression10"):
                opp_val = getattr(old_value, "edu_Expression10", None)
                if opp_val == self:
                    setattr(old_value, "edu_Expression10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_Expression10"):
                opp_val = getattr(value, "edu_Expression10", None)
                setattr(value, "edu_Expression10", self)

    def accept(self, visitor: str):
        # TODO: Implement accept method
        pass

class BinaryExpression:

    pass
class edu_Unequal(BinaryExpression):

    def __init__(self):
        
    def accept(self, visitor: str):
        # TODO: Implement accept method
        pass

class edu_Subtraction(BinaryExpression):

    def __init__(self):
        
    def accept(self, visitor: str):
        # TODO: Implement accept method
        pass

class edu_Conjunction(BinaryExpression):

    def __init__(self):
        
    def accept(self, visitor: str):
        # TODO: Implement accept method
        pass

class edu_Implication(BinaryExpression):

    def __init__(self):
        
    def accept(self, visitor: str):
        # TODO: Implement accept method
        pass

class edu_Equal(BinaryExpression):

    def __init__(self):
        
    def accept(self, visitor: str):
        # TODO: Implement accept method
        pass

class edu_Multiplication(BinaryExpression):

    def __init__(self):
        
    def accept(self, visitor: str):
        # TODO: Implement accept method
        pass

class edu_Less(BinaryExpression):

    def __init__(self):
        
    def accept(self, visitor: str):
        # TODO: Implement accept method
        pass

class edu_Disjunction(BinaryExpression):

    def __init__(self):
        
    def accept(self, visitor: str):
        # TODO: Implement accept method
        pass

class edu_LessOrEqual(BinaryExpression):

    def __init__(self):
        
    def accept(self, visitor: str):
        # TODO: Implement accept method
        pass

class edu_Equivalence(BinaryExpression):

    def __init__(self):
        
    def accept(self, visitor: str):
        # TODO: Implement accept method
        pass

class edu_Division(BinaryExpression):

    def __init__(self):
        
    def accept(self, visitor: str):
        # TODO: Implement accept method
        pass

class edu_Modulus(BinaryExpression):

    def __init__(self):
        
    def accept(self, visitor: str):
        # TODO: Implement accept method
        pass

class edu_GreaterOrEqual(BinaryExpression):

    def __init__(self):
        
    def accept(self, visitor: str):
        # TODO: Implement accept method
        pass

class edu_Greater(BinaryExpression):

    def __init__(self):
        
    def accept(self, visitor: str):
        # TODO: Implement accept method
        pass

class edu_Addition(BinaryExpression):

    def __init__(self):
        
    def accept(self, visitor: str):
        # TODO: Implement accept method
        pass

class edu_ASTNode(ABC):

    def __init__(self):
        
    def accept(self, visitor: str):
        # TODO: Implement accept method
        pass

class edu_Axiom(Annotation):

    def __init__(self, edu_Axiom: "edu_Program" = None):
        self.edu_Axiom = edu_Axiom
        
    @property
    def edu_Axiom(self):
        return self.__edu_Axiom

    @edu_Axiom.setter
    def edu_Axiom(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_Axiom__edu_Axiom", None)
        self.__edu_Axiom = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_Program4"):
                opp_val = getattr(old_value, "edu_Program4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_Program4"):
                opp_val = getattr(value, "edu_Program4", None)
                if opp_val is None:
                    setattr(value, "edu_Program4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def accept(self, visitor: str):
        # TODO: Implement accept method
        pass

class edu_Block(Statement):

    def __init__(self, edu_Block: "edu_Program" = None, edu_Block28: set["edu_Statement"] = None, edu_Block36: "edu_Conditional" = None, edu_Block33: "edu_Conditional" = None, edu_Block60: "edu_FunctionDeclaration" = None, edu_Block68: "edu_Loop" = None):
        self.edu_Block = edu_Block
        self.edu_Block28 = edu_Block28 if edu_Block28 is not None else set()
        self.edu_Block36 = edu_Block36
        self.edu_Block33 = edu_Block33
        self.edu_Block60 = edu_Block60
        self.edu_Block68 = edu_Block68
        
    @property
    def edu_Block(self):
        return self.__edu_Block

    @edu_Block.setter
    def edu_Block(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_Block__edu_Block", None)
        self.__edu_Block = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_Program2"):
                opp_val = getattr(old_value, "edu_Program2", None)
                if opp_val == self:
                    setattr(old_value, "edu_Program2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_Program2"):
                opp_val = getattr(value, "edu_Program2", None)
                setattr(value, "edu_Program2", self)

    @property
    def edu_Block33(self):
        return self.__edu_Block33

    @edu_Block33.setter
    def edu_Block33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_Block__edu_Block33", None)
        self.__edu_Block33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_Conditional32"):
                opp_val = getattr(old_value, "edu_Conditional32", None)
                if opp_val == self:
                    setattr(old_value, "edu_Conditional32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_Conditional32"):
                opp_val = getattr(value, "edu_Conditional32", None)
                setattr(value, "edu_Conditional32", self)

    @property
    def edu_Block68(self):
        return self.__edu_Block68

    @edu_Block68.setter
    def edu_Block68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_Block__edu_Block68", None)
        self.__edu_Block68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_Loop67"):
                opp_val = getattr(old_value, "edu_Loop67", None)
                if opp_val == self:
                    setattr(old_value, "edu_Loop67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_Loop67"):
                opp_val = getattr(value, "edu_Loop67", None)
                setattr(value, "edu_Loop67", self)

    @property
    def edu_Block28(self):
        return self.__edu_Block28

    @edu_Block28.setter
    def edu_Block28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_Block__edu_Block28", None)
        self.__edu_Block28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "edu_Statement"):
                    opp_val = getattr(item, "edu_Statement", None)
                    
                    if opp_val == self:
                        setattr(item, "edu_Statement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "edu_Statement"):
                    opp_val = getattr(item, "edu_Statement", None)
                    
                    setattr(item, "edu_Statement", self)
                    

    @property
    def edu_Block36(self):
        return self.__edu_Block36

    @edu_Block36.setter
    def edu_Block36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_Block__edu_Block36", None)
        self.__edu_Block36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_Conditional35"):
                opp_val = getattr(old_value, "edu_Conditional35", None)
                if opp_val == self:
                    setattr(old_value, "edu_Conditional35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_Conditional35"):
                opp_val = getattr(value, "edu_Conditional35", None)
                setattr(value, "edu_Conditional35", self)

    @property
    def edu_Block60(self):
        return self.__edu_Block60

    @edu_Block60.setter
    def edu_Block60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_Block__edu_Block60", None)
        self.__edu_Block60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_FunctionDeclaration59"):
                opp_val = getattr(old_value, "edu_FunctionDeclaration59", None)
                if opp_val == self:
                    setattr(old_value, "edu_FunctionDeclaration59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_FunctionDeclaration59"):
                opp_val = getattr(value, "edu_FunctionDeclaration59", None)
                setattr(value, "edu_FunctionDeclaration59", self)

    def accept(self, visitor: str):
        # TODO: Implement accept method
        pass

class ASTNode:

    pass
class edu_Expression(ASTNode):

    def __init__(self, edu_Expression10: "edu_UnaryExpression" = None, edu_Expression12: "edu_ArrayLiteral" = None, edu_Expression: "edu_BinaryExpression" = None, edu_Expression8: "edu_BinaryExpression" = None, edu_Expression16: "edu_DivisorNotZeroAssertion" = None, edu_Expression18: "edu_Annotation" = None, edu_Expression26: "edu_VariableDeclaration" = None, edu_Expression20: "edu_Assignment" = None, edu_Expression30: "edu_Conditional" = None, edu_Expression47: "edu_FunctionCall" = None, edu_Expression41: "edu_QuantifiedExpression" = None, edu_Expression44: "edu_QuantifiedExpression" = None, edu_Expression65: "edu_Loop" = None, edu_Expression82: "edu_SymbolReference" = None, edu_Expression72: "edu_ReturnStatement" = None, edu_Expression94: "edu_ArrayAccess" = None, edu_Expression97: "edu_ArrayAccess" = None, edu_Expression99: "edu_ExpressionToExpressionMap" = None, edu_Expression102: "edu_ExpressionToExpressionMap" = None, edu_Expression84: "edu_ExpressionEvaluation" = None, edu_Expression86: "edu_ArrayFunction" = None, edu_Expression89: "edu_ArrayFunction" = None, edu_Expression92: "edu_ArrayFunction" = None, edu_Expression104: "edu_TernaryExpression" = None, edu_Expression107: "edu_TernaryExpression" = None, edu_Expression110: "edu_TernaryExpression" = None, edu_Expression115: "edu_LetExpression" = None):
        self.edu_Expression10 = edu_Expression10
        self.edu_Expression12 = edu_Expression12
        self.edu_Expression = edu_Expression
        self.edu_Expression8 = edu_Expression8
        self.edu_Expression16 = edu_Expression16
        self.edu_Expression18 = edu_Expression18
        self.edu_Expression26 = edu_Expression26
        self.edu_Expression20 = edu_Expression20
        self.edu_Expression30 = edu_Expression30
        self.edu_Expression47 = edu_Expression47
        self.edu_Expression41 = edu_Expression41
        self.edu_Expression44 = edu_Expression44
        self.edu_Expression65 = edu_Expression65
        self.edu_Expression82 = edu_Expression82
        self.edu_Expression72 = edu_Expression72
        self.edu_Expression94 = edu_Expression94
        self.edu_Expression97 = edu_Expression97
        self.edu_Expression99 = edu_Expression99
        self.edu_Expression102 = edu_Expression102
        self.edu_Expression84 = edu_Expression84
        self.edu_Expression86 = edu_Expression86
        self.edu_Expression89 = edu_Expression89
        self.edu_Expression92 = edu_Expression92
        self.edu_Expression104 = edu_Expression104
        self.edu_Expression107 = edu_Expression107
        self.edu_Expression110 = edu_Expression110
        self.edu_Expression115 = edu_Expression115
        
    @property
    def edu_Expression41(self):
        return self.__edu_Expression41

    @edu_Expression41.setter
    def edu_Expression41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_Expression__edu_Expression41", None)
        self.__edu_Expression41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_QuantifiedExpression40"):
                opp_val = getattr(old_value, "edu_QuantifiedExpression40", None)
                if opp_val == self:
                    setattr(old_value, "edu_QuantifiedExpression40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_QuantifiedExpression40"):
                opp_val = getattr(value, "edu_QuantifiedExpression40", None)
                setattr(value, "edu_QuantifiedExpression40", self)

    @property
    def edu_Expression12(self):
        return self.__edu_Expression12

    @edu_Expression12.setter
    def edu_Expression12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_Expression__edu_Expression12", None)
        self.__edu_Expression12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_ArrayLiteral"):
                opp_val = getattr(old_value, "edu_ArrayLiteral", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_ArrayLiteral"):
                opp_val = getattr(value, "edu_ArrayLiteral", None)
                if opp_val is None:
                    setattr(value, "edu_ArrayLiteral", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def edu_Expression102(self):
        return self.__edu_Expression102

    @edu_Expression102.setter
    def edu_Expression102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_Expression__edu_Expression102", None)
        self.__edu_Expression102 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_ExpressionToExpressionMap101"):
                opp_val = getattr(old_value, "edu_ExpressionToExpressionMap101", None)
                if opp_val == self:
                    setattr(old_value, "edu_ExpressionToExpressionMap101", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_ExpressionToExpressionMap101"):
                opp_val = getattr(value, "edu_ExpressionToExpressionMap101", None)
                setattr(value, "edu_ExpressionToExpressionMap101", self)

    @property
    def edu_Expression8(self):
        return self.__edu_Expression8

    @edu_Expression8.setter
    def edu_Expression8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_Expression__edu_Expression8", None)
        self.__edu_Expression8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_BinaryExpression7"):
                opp_val = getattr(old_value, "edu_BinaryExpression7", None)
                if opp_val == self:
                    setattr(old_value, "edu_BinaryExpression7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_BinaryExpression7"):
                opp_val = getattr(value, "edu_BinaryExpression7", None)
                setattr(value, "edu_BinaryExpression7", self)

    @property
    def edu_Expression104(self):
        return self.__edu_Expression104

    @edu_Expression104.setter
    def edu_Expression104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_Expression__edu_Expression104", None)
        self.__edu_Expression104 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_TernaryExpression"):
                opp_val = getattr(old_value, "edu_TernaryExpression", None)
                if opp_val == self:
                    setattr(old_value, "edu_TernaryExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_TernaryExpression"):
                opp_val = getattr(value, "edu_TernaryExpression", None)
                setattr(value, "edu_TernaryExpression", self)

    @property
    def edu_Expression10(self):
        return self.__edu_Expression10

    @edu_Expression10.setter
    def edu_Expression10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_Expression__edu_Expression10", None)
        self.__edu_Expression10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_UnaryExpression"):
                opp_val = getattr(old_value, "edu_UnaryExpression", None)
                if opp_val == self:
                    setattr(old_value, "edu_UnaryExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_UnaryExpression"):
                opp_val = getattr(value, "edu_UnaryExpression", None)
                setattr(value, "edu_UnaryExpression", self)

    @property
    def edu_Expression107(self):
        return self.__edu_Expression107

    @edu_Expression107.setter
    def edu_Expression107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_Expression__edu_Expression107", None)
        self.__edu_Expression107 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_TernaryExpression106"):
                opp_val = getattr(old_value, "edu_TernaryExpression106", None)
                if opp_val == self:
                    setattr(old_value, "edu_TernaryExpression106", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_TernaryExpression106"):
                opp_val = getattr(value, "edu_TernaryExpression106", None)
                setattr(value, "edu_TernaryExpression106", self)

    @property
    def edu_Expression44(self):
        return self.__edu_Expression44

    @edu_Expression44.setter
    def edu_Expression44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_Expression__edu_Expression44", None)
        self.__edu_Expression44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_QuantifiedExpression43"):
                opp_val = getattr(old_value, "edu_QuantifiedExpression43", None)
                if opp_val == self:
                    setattr(old_value, "edu_QuantifiedExpression43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_QuantifiedExpression43"):
                opp_val = getattr(value, "edu_QuantifiedExpression43", None)
                setattr(value, "edu_QuantifiedExpression43", self)

    @property
    def edu_Expression47(self):
        return self.__edu_Expression47

    @edu_Expression47.setter
    def edu_Expression47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_Expression__edu_Expression47", None)
        self.__edu_Expression47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_FunctionCall46"):
                opp_val = getattr(old_value, "edu_FunctionCall46", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_FunctionCall46"):
                opp_val = getattr(value, "edu_FunctionCall46", None)
                if opp_val is None:
                    setattr(value, "edu_FunctionCall46", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def edu_Expression65(self):
        return self.__edu_Expression65

    @edu_Expression65.setter
    def edu_Expression65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_Expression__edu_Expression65", None)
        self.__edu_Expression65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_Loop"):
                opp_val = getattr(old_value, "edu_Loop", None)
                if opp_val == self:
                    setattr(old_value, "edu_Loop", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_Loop"):
                opp_val = getattr(value, "edu_Loop", None)
                setattr(value, "edu_Loop", self)

    @property
    def edu_Expression94(self):
        return self.__edu_Expression94

    @edu_Expression94.setter
    def edu_Expression94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_Expression__edu_Expression94", None)
        self.__edu_Expression94 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_ArrayAccess"):
                opp_val = getattr(old_value, "edu_ArrayAccess", None)
                if opp_val == self:
                    setattr(old_value, "edu_ArrayAccess", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_ArrayAccess"):
                opp_val = getattr(value, "edu_ArrayAccess", None)
                setattr(value, "edu_ArrayAccess", self)

    @property
    def edu_Expression82(self):
        return self.__edu_Expression82

    @edu_Expression82.setter
    def edu_Expression82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_Expression__edu_Expression82", None)
        self.__edu_Expression82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_SymbolReference"):
                opp_val = getattr(old_value, "edu_SymbolReference", None)
                if opp_val == self:
                    setattr(old_value, "edu_SymbolReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_SymbolReference"):
                opp_val = getattr(value, "edu_SymbolReference", None)
                setattr(value, "edu_SymbolReference", self)

    @property
    def edu_Expression16(self):
        return self.__edu_Expression16

    @edu_Expression16.setter
    def edu_Expression16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_Expression__edu_Expression16", None)
        self.__edu_Expression16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_DivisorNotZeroAssertion"):
                opp_val = getattr(old_value, "edu_DivisorNotZeroAssertion", None)
                if opp_val == self:
                    setattr(old_value, "edu_DivisorNotZeroAssertion", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_DivisorNotZeroAssertion"):
                opp_val = getattr(value, "edu_DivisorNotZeroAssertion", None)
                setattr(value, "edu_DivisorNotZeroAssertion", self)

    @property
    def edu_Expression18(self):
        return self.__edu_Expression18

    @edu_Expression18.setter
    def edu_Expression18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_Expression__edu_Expression18", None)
        self.__edu_Expression18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_Annotation"):
                opp_val = getattr(old_value, "edu_Annotation", None)
                if opp_val == self:
                    setattr(old_value, "edu_Annotation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_Annotation"):
                opp_val = getattr(value, "edu_Annotation", None)
                setattr(value, "edu_Annotation", self)

    @property
    def edu_Expression(self):
        return self.__edu_Expression

    @edu_Expression.setter
    def edu_Expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_Expression__edu_Expression", None)
        self.__edu_Expression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_BinaryExpression"):
                opp_val = getattr(old_value, "edu_BinaryExpression", None)
                if opp_val == self:
                    setattr(old_value, "edu_BinaryExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_BinaryExpression"):
                opp_val = getattr(value, "edu_BinaryExpression", None)
                setattr(value, "edu_BinaryExpression", self)

    @property
    def edu_Expression99(self):
        return self.__edu_Expression99

    @edu_Expression99.setter
    def edu_Expression99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_Expression__edu_Expression99", None)
        self.__edu_Expression99 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_ExpressionToExpressionMap"):
                opp_val = getattr(old_value, "edu_ExpressionToExpressionMap", None)
                if opp_val == self:
                    setattr(old_value, "edu_ExpressionToExpressionMap", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_ExpressionToExpressionMap"):
                opp_val = getattr(value, "edu_ExpressionToExpressionMap", None)
                setattr(value, "edu_ExpressionToExpressionMap", self)

    @property
    def edu_Expression110(self):
        return self.__edu_Expression110

    @edu_Expression110.setter
    def edu_Expression110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_Expression__edu_Expression110", None)
        self.__edu_Expression110 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_TernaryExpression109"):
                opp_val = getattr(old_value, "edu_TernaryExpression109", None)
                if opp_val == self:
                    setattr(old_value, "edu_TernaryExpression109", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_TernaryExpression109"):
                opp_val = getattr(value, "edu_TernaryExpression109", None)
                setattr(value, "edu_TernaryExpression109", self)

    @property
    def edu_Expression97(self):
        return self.__edu_Expression97

    @edu_Expression97.setter
    def edu_Expression97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_Expression__edu_Expression97", None)
        self.__edu_Expression97 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_ArrayAccess96"):
                opp_val = getattr(old_value, "edu_ArrayAccess96", None)
                if opp_val == self:
                    setattr(old_value, "edu_ArrayAccess96", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_ArrayAccess96"):
                opp_val = getattr(value, "edu_ArrayAccess96", None)
                setattr(value, "edu_ArrayAccess96", self)

    @property
    def edu_Expression92(self):
        return self.__edu_Expression92

    @edu_Expression92.setter
    def edu_Expression92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_Expression__edu_Expression92", None)
        self.__edu_Expression92 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_ArrayFunction91"):
                opp_val = getattr(old_value, "edu_ArrayFunction91", None)
                if opp_val == self:
                    setattr(old_value, "edu_ArrayFunction91", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_ArrayFunction91"):
                opp_val = getattr(value, "edu_ArrayFunction91", None)
                setattr(value, "edu_ArrayFunction91", self)

    @property
    def edu_Expression84(self):
        return self.__edu_Expression84

    @edu_Expression84.setter
    def edu_Expression84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_Expression__edu_Expression84", None)
        self.__edu_Expression84 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_ExpressionEvaluation"):
                opp_val = getattr(old_value, "edu_ExpressionEvaluation", None)
                if opp_val == self:
                    setattr(old_value, "edu_ExpressionEvaluation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_ExpressionEvaluation"):
                opp_val = getattr(value, "edu_ExpressionEvaluation", None)
                setattr(value, "edu_ExpressionEvaluation", self)

    @property
    def edu_Expression20(self):
        return self.__edu_Expression20

    @edu_Expression20.setter
    def edu_Expression20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_Expression__edu_Expression20", None)
        self.__edu_Expression20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_Assignment"):
                opp_val = getattr(old_value, "edu_Assignment", None)
                if opp_val == self:
                    setattr(old_value, "edu_Assignment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_Assignment"):
                opp_val = getattr(value, "edu_Assignment", None)
                setattr(value, "edu_Assignment", self)

    @property
    def edu_Expression26(self):
        return self.__edu_Expression26

    @edu_Expression26.setter
    def edu_Expression26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_Expression__edu_Expression26", None)
        self.__edu_Expression26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_VariableDeclaration25"):
                opp_val = getattr(old_value, "edu_VariableDeclaration25", None)
                if opp_val == self:
                    setattr(old_value, "edu_VariableDeclaration25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_VariableDeclaration25"):
                opp_val = getattr(value, "edu_VariableDeclaration25", None)
                setattr(value, "edu_VariableDeclaration25", self)

    @property
    def edu_Expression115(self):
        return self.__edu_Expression115

    @edu_Expression115.setter
    def edu_Expression115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_Expression__edu_Expression115", None)
        self.__edu_Expression115 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_LetExpression114"):
                opp_val = getattr(old_value, "edu_LetExpression114", None)
                if opp_val == self:
                    setattr(old_value, "edu_LetExpression114", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_LetExpression114"):
                opp_val = getattr(value, "edu_LetExpression114", None)
                setattr(value, "edu_LetExpression114", self)

    @property
    def edu_Expression86(self):
        return self.__edu_Expression86

    @edu_Expression86.setter
    def edu_Expression86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_Expression__edu_Expression86", None)
        self.__edu_Expression86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_ArrayFunction"):
                opp_val = getattr(old_value, "edu_ArrayFunction", None)
                if opp_val == self:
                    setattr(old_value, "edu_ArrayFunction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_ArrayFunction"):
                opp_val = getattr(value, "edu_ArrayFunction", None)
                setattr(value, "edu_ArrayFunction", self)

    @property
    def edu_Expression30(self):
        return self.__edu_Expression30

    @edu_Expression30.setter
    def edu_Expression30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_Expression__edu_Expression30", None)
        self.__edu_Expression30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_Conditional"):
                opp_val = getattr(old_value, "edu_Conditional", None)
                if opp_val == self:
                    setattr(old_value, "edu_Conditional", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_Conditional"):
                opp_val = getattr(value, "edu_Conditional", None)
                setattr(value, "edu_Conditional", self)

    @property
    def edu_Expression89(self):
        return self.__edu_Expression89

    @edu_Expression89.setter
    def edu_Expression89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_Expression__edu_Expression89", None)
        self.__edu_Expression89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_ArrayFunction88"):
                opp_val = getattr(old_value, "edu_ArrayFunction88", None)
                if opp_val == self:
                    setattr(old_value, "edu_ArrayFunction88", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_ArrayFunction88"):
                opp_val = getattr(value, "edu_ArrayFunction88", None)
                setattr(value, "edu_ArrayFunction88", self)

    @property
    def edu_Expression72(self):
        return self.__edu_Expression72

    @edu_Expression72.setter
    def edu_Expression72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_Expression__edu_Expression72", None)
        self.__edu_Expression72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_ReturnStatement"):
                opp_val = getattr(old_value, "edu_ReturnStatement", None)
                if opp_val == self:
                    setattr(old_value, "edu_ReturnStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_ReturnStatement"):
                opp_val = getattr(value, "edu_ReturnStatement", None)
                setattr(value, "edu_ReturnStatement", self)

    def accept(self, visitor: str):
        # TODO: Implement accept method
        pass

class edu_Statement(ASTNode):

    def __init__(self, edu_Statement: "edu_Block" = None):
        self.edu_Statement = edu_Statement
        
    @property
    def edu_Statement(self):
        return self.__edu_Statement

    @edu_Statement.setter
    def edu_Statement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_Statement__edu_Statement", None)
        self.__edu_Statement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_Block28"):
                opp_val = getattr(old_value, "edu_Block28", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_Block28"):
                opp_val = getattr(value, "edu_Block28", None)
                if opp_val is None:
                    setattr(value, "edu_Block28", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def accept(self, visitor: str):
        # TODO: Implement accept method
        pass

class edu_Type(ASTNode):

    def __init__(self, edu_Type: "edu_VariableDeclaration" = None, edu_Type63: "edu_FunctionDeclaration" = None):
        self.edu_Type = edu_Type
        self.edu_Type63 = edu_Type63
        
    @property
    def edu_Type63(self):
        return self.__edu_Type63

    @edu_Type63.setter
    def edu_Type63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_Type__edu_Type63", None)
        self.__edu_Type63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_FunctionDeclaration62"):
                opp_val = getattr(old_value, "edu_FunctionDeclaration62", None)
                if opp_val == self:
                    setattr(old_value, "edu_FunctionDeclaration62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_FunctionDeclaration62"):
                opp_val = getattr(value, "edu_FunctionDeclaration62", None)
                setattr(value, "edu_FunctionDeclaration62", self)

    @property
    def edu_Type(self):
        return self.__edu_Type

    @edu_Type.setter
    def edu_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_Type__edu_Type", None)
        self.__edu_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_VariableDeclaration"):
                opp_val = getattr(old_value, "edu_VariableDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "edu_VariableDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_VariableDeclaration"):
                opp_val = getattr(value, "edu_VariableDeclaration", None)
                setattr(value, "edu_VariableDeclaration", self)

    def accept(self, visitor: str):
        # TODO: Implement accept method
        pass

class edu_ExpressionEvaluation(ASTNode):

    pass
class edu_FunctionDeclaration(ASTNode):

    def __init__(self, name: str, edu_FunctionDeclaration: "edu_Program" = None, edu_FunctionDeclaration50: "edu_FunctionCall" = None, edu_FunctionDeclaration52: set["edu_Precondition"] = None, edu_FunctionDeclaration54: set["edu_Postcondition"] = None, edu_FunctionDeclaration56: set["edu_VariableDeclaration"] = None, edu_FunctionDeclaration59: "edu_Block" = None, edu_FunctionDeclaration62: "edu_Type" = None, edu_FunctionDeclaration80: "edu_ReturnValueReference" = None, edu_FunctionDeclaration75: "edu_ReturnStatement" = None):
        self.name = name
        self.edu_FunctionDeclaration = edu_FunctionDeclaration
        self.edu_FunctionDeclaration50 = edu_FunctionDeclaration50
        self.edu_FunctionDeclaration52 = edu_FunctionDeclaration52 if edu_FunctionDeclaration52 is not None else set()
        self.edu_FunctionDeclaration54 = edu_FunctionDeclaration54 if edu_FunctionDeclaration54 is not None else set()
        self.edu_FunctionDeclaration56 = edu_FunctionDeclaration56 if edu_FunctionDeclaration56 is not None else set()
        self.edu_FunctionDeclaration59 = edu_FunctionDeclaration59
        self.edu_FunctionDeclaration62 = edu_FunctionDeclaration62
        self.edu_FunctionDeclaration80 = edu_FunctionDeclaration80
        self.edu_FunctionDeclaration75 = edu_FunctionDeclaration75
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def edu_FunctionDeclaration59(self):
        return self.__edu_FunctionDeclaration59

    @edu_FunctionDeclaration59.setter
    def edu_FunctionDeclaration59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_FunctionDeclaration__edu_FunctionDeclaration59", None)
        self.__edu_FunctionDeclaration59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_Block60"):
                opp_val = getattr(old_value, "edu_Block60", None)
                if opp_val == self:
                    setattr(old_value, "edu_Block60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_Block60"):
                opp_val = getattr(value, "edu_Block60", None)
                setattr(value, "edu_Block60", self)

    @property
    def edu_FunctionDeclaration50(self):
        return self.__edu_FunctionDeclaration50

    @edu_FunctionDeclaration50.setter
    def edu_FunctionDeclaration50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_FunctionDeclaration__edu_FunctionDeclaration50", None)
        self.__edu_FunctionDeclaration50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_FunctionCall49"):
                opp_val = getattr(old_value, "edu_FunctionCall49", None)
                if opp_val == self:
                    setattr(old_value, "edu_FunctionCall49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_FunctionCall49"):
                opp_val = getattr(value, "edu_FunctionCall49", None)
                setattr(value, "edu_FunctionCall49", self)

    @property
    def edu_FunctionDeclaration(self):
        return self.__edu_FunctionDeclaration

    @edu_FunctionDeclaration.setter
    def edu_FunctionDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_FunctionDeclaration__edu_FunctionDeclaration", None)
        self.__edu_FunctionDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_Program"):
                opp_val = getattr(old_value, "edu_Program", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_Program"):
                opp_val = getattr(value, "edu_Program", None)
                if opp_val is None:
                    setattr(value, "edu_Program", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def edu_FunctionDeclaration56(self):
        return self.__edu_FunctionDeclaration56

    @edu_FunctionDeclaration56.setter
    def edu_FunctionDeclaration56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_FunctionDeclaration__edu_FunctionDeclaration56", None)
        self.__edu_FunctionDeclaration56 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "edu_VariableDeclaration57"):
                    opp_val = getattr(item, "edu_VariableDeclaration57", None)
                    
                    if opp_val == self:
                        setattr(item, "edu_VariableDeclaration57", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "edu_VariableDeclaration57"):
                    opp_val = getattr(item, "edu_VariableDeclaration57", None)
                    
                    setattr(item, "edu_VariableDeclaration57", self)
                    

    @property
    def edu_FunctionDeclaration62(self):
        return self.__edu_FunctionDeclaration62

    @edu_FunctionDeclaration62.setter
    def edu_FunctionDeclaration62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_FunctionDeclaration__edu_FunctionDeclaration62", None)
        self.__edu_FunctionDeclaration62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_Type63"):
                opp_val = getattr(old_value, "edu_Type63", None)
                if opp_val == self:
                    setattr(old_value, "edu_Type63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_Type63"):
                opp_val = getattr(value, "edu_Type63", None)
                setattr(value, "edu_Type63", self)

    @property
    def edu_FunctionDeclaration52(self):
        return self.__edu_FunctionDeclaration52

    @edu_FunctionDeclaration52.setter
    def edu_FunctionDeclaration52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_FunctionDeclaration__edu_FunctionDeclaration52", None)
        self.__edu_FunctionDeclaration52 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "edu_Precondition"):
                    opp_val = getattr(item, "edu_Precondition", None)
                    
                    if opp_val == self:
                        setattr(item, "edu_Precondition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "edu_Precondition"):
                    opp_val = getattr(item, "edu_Precondition", None)
                    
                    setattr(item, "edu_Precondition", self)
                    

    @property
    def edu_FunctionDeclaration54(self):
        return self.__edu_FunctionDeclaration54

    @edu_FunctionDeclaration54.setter
    def edu_FunctionDeclaration54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_FunctionDeclaration__edu_FunctionDeclaration54", None)
        self.__edu_FunctionDeclaration54 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "edu_Postcondition"):
                    opp_val = getattr(item, "edu_Postcondition", None)
                    
                    if opp_val == self:
                        setattr(item, "edu_Postcondition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "edu_Postcondition"):
                    opp_val = getattr(item, "edu_Postcondition", None)
                    
                    setattr(item, "edu_Postcondition", self)
                    

    @property
    def edu_FunctionDeclaration80(self):
        return self.__edu_FunctionDeclaration80

    @edu_FunctionDeclaration80.setter
    def edu_FunctionDeclaration80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_FunctionDeclaration__edu_FunctionDeclaration80", None)
        self.__edu_FunctionDeclaration80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_ReturnValueReference"):
                opp_val = getattr(old_value, "edu_ReturnValueReference", None)
                if opp_val == self:
                    setattr(old_value, "edu_ReturnValueReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_ReturnValueReference"):
                opp_val = getattr(value, "edu_ReturnValueReference", None)
                setattr(value, "edu_ReturnValueReference", self)

    @property
    def edu_FunctionDeclaration75(self):
        return self.__edu_FunctionDeclaration75

    @edu_FunctionDeclaration75.setter
    def edu_FunctionDeclaration75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_FunctionDeclaration__edu_FunctionDeclaration75", None)
        self.__edu_FunctionDeclaration75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_ReturnStatement74"):
                opp_val = getattr(old_value, "edu_ReturnStatement74", None)
                if opp_val == self:
                    setattr(old_value, "edu_ReturnStatement74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_ReturnStatement74"):
                opp_val = getattr(value, "edu_ReturnStatement74", None)
                setattr(value, "edu_ReturnStatement74", self)

    def accept(self, visitor: str):
        # TODO: Implement accept method
        pass

class edu_Program(ASTNode):

    def __init__(self, edu_Program: set["edu_FunctionDeclaration"] = None, edu_Program2: "edu_Block" = None, edu_Program4: set["edu_Axiom"] = None):
        self.edu_Program = edu_Program if edu_Program is not None else set()
        self.edu_Program2 = edu_Program2
        self.edu_Program4 = edu_Program4 if edu_Program4 is not None else set()
        
    @property
    def edu_Program4(self):
        return self.__edu_Program4

    @edu_Program4.setter
    def edu_Program4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_Program__edu_Program4", None)
        self.__edu_Program4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "edu_Axiom"):
                    opp_val = getattr(item, "edu_Axiom", None)
                    
                    if opp_val == self:
                        setattr(item, "edu_Axiom", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "edu_Axiom"):
                    opp_val = getattr(item, "edu_Axiom", None)
                    
                    setattr(item, "edu_Axiom", self)
                    

    @property
    def edu_Program(self):
        return self.__edu_Program

    @edu_Program.setter
    def edu_Program(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_Program__edu_Program", None)
        self.__edu_Program = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "edu_FunctionDeclaration"):
                    opp_val = getattr(item, "edu_FunctionDeclaration", None)
                    
                    if opp_val == self:
                        setattr(item, "edu_FunctionDeclaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "edu_FunctionDeclaration"):
                    opp_val = getattr(item, "edu_FunctionDeclaration", None)
                    
                    setattr(item, "edu_FunctionDeclaration", self)
                    

    @property
    def edu_Program2(self):
        return self.__edu_Program2

    @edu_Program2.setter
    def edu_Program2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_Program__edu_Program2", None)
        self.__edu_Program2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_Block"):
                opp_val = getattr(old_value, "edu_Block", None)
                if opp_val == self:
                    setattr(old_value, "edu_Block", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_Block"):
                opp_val = getattr(value, "edu_Block", None)
                setattr(value, "edu_Block", self)

    def accept(self, visitor: str):
        # TODO: Implement accept method
        pass
