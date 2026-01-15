from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class AbstractExpression:

    pass
class miniJava_ClassConstruction(AbstractExpression):

    pass
class miniJava_Negation(AbstractExpression):

    pass
class miniJava_IntegerArrayConstruction(AbstractExpression):

    pass
class miniJava_ArrayAccess(AbstractExpression):

    pass
class miniJava_Multiply(AbstractExpression):

    pass
class miniJava_FunctionCall(AbstractExpression):

    pass
class miniJava_LengthOf(AbstractExpression):

    pass
class miniJava_Plus(AbstractExpression):

    pass
class miniJava_ClassifierReference(AbstractExpression):

    pass
class miniJava_LessThen(AbstractExpression):

    pass
class miniJava_ThisReference(AbstractExpression):

    pass
class miniJava_IntLiteral(AbstractExpression):

    def __init__(self, resultInt: int):
        self.resultInt = resultInt
        
    @property
    def resultInt(self) -> int:
        return self.__resultInt

    @resultInt.setter
    def resultInt(self, resultInt: int):
        self.__resultInt = resultInt

class miniJava_Minus(AbstractExpression):

    pass
class miniJava_Boolean(AbstractExpression):

    def __init__(self, result: bool):
        self.result = result
        
    @property
    def result(self) -> bool:
        return self.__result

    @result.setter
    def result(self, result: bool):
        self.__result = result

class miniJava_BlockExpression(AbstractExpression):

    pass
class miniJava_And(AbstractExpression):

    pass
class miniJava_AbstactType:

    pass
class miniJava_MethodDeclaration:

    pass
class Statement:

    pass
class miniJava_IfStatement(Statement):

    pass
class miniJava_WhileLoop(Statement):

    pass
class miniJava_Assignment(Statement):

    pass
class miniJava_PrintLine(Statement):

    pass
class miniJava_ArrayAssignment(Statement):

    pass
class miniJava_BlockStatement(Statement):

    pass
class AbstactType:

    pass
class miniJava_IntegerType(AbstactType):

    pass
class miniJava_ClassifierType(AbstactType):

    pass
class miniJava_BooleanType(AbstactType):

    pass
class miniJava_IntegerArrayType(AbstactType):

    pass
class miniJava_AbstractExpression:

    pass
class miniJava_VariableDeclaration:

    pass
class miniJava_Statement:

    pass
class miniJava_Identifier:

    def __init__(self, value: str, miniJava_Identifier: "miniJava_MainClass" = None, miniJava_Identifier7: "miniJava_MainClass" = None, miniJava_Identifier12: "miniJava_Class" = None, miniJava_Identifier15: "miniJava_Class" = None, miniJava_Identifier24: "miniJava_VariableDeclaration" = None, miniJava_Identifier30: "miniJava_MethodDeclaration" = None, miniJava_Identifier43: "miniJava_ClassifierType" = None, miniJava_Identifier62: "miniJava_Assignment" = None, miniJava_Identifier67: "miniJava_ArrayAssignment" = None, miniJava_Identifier110: "miniJava_FunctionCall" = None, miniJava_Identifier115: "miniJava_ClassifierReference" = None, miniJava_Identifier119: "miniJava_ClassConstruction" = None):
        self.value = value
        self.miniJava_Identifier = miniJava_Identifier
        self.miniJava_Identifier7 = miniJava_Identifier7
        self.miniJava_Identifier12 = miniJava_Identifier12
        self.miniJava_Identifier15 = miniJava_Identifier15
        self.miniJava_Identifier24 = miniJava_Identifier24
        self.miniJava_Identifier30 = miniJava_Identifier30
        self.miniJava_Identifier43 = miniJava_Identifier43
        self.miniJava_Identifier62 = miniJava_Identifier62
        self.miniJava_Identifier67 = miniJava_Identifier67
        self.miniJava_Identifier110 = miniJava_Identifier110
        self.miniJava_Identifier115 = miniJava_Identifier115
        self.miniJava_Identifier119 = miniJava_Identifier119
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def miniJava_Identifier(self):
        return self.__miniJava_Identifier

    @miniJava_Identifier.setter
    def miniJava_Identifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Identifier__miniJava_Identifier", None)
        self.__miniJava_Identifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_MainClass4"):
                opp_val = getattr(old_value, "miniJava_MainClass4", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_MainClass4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_MainClass4"):
                opp_val = getattr(value, "miniJava_MainClass4", None)
                setattr(value, "miniJava_MainClass4", self)

    @property
    def miniJava_Identifier62(self):
        return self.__miniJava_Identifier62

    @miniJava_Identifier62.setter
    def miniJava_Identifier62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Identifier__miniJava_Identifier62", None)
        self.__miniJava_Identifier62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Assignment"):
                opp_val = getattr(old_value, "miniJava_Assignment", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Assignment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Assignment"):
                opp_val = getattr(value, "miniJava_Assignment", None)
                setattr(value, "miniJava_Assignment", self)

    @property
    def miniJava_Identifier110(self):
        return self.__miniJava_Identifier110

    @miniJava_Identifier110.setter
    def miniJava_Identifier110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Identifier__miniJava_Identifier110", None)
        self.__miniJava_Identifier110 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_FunctionCall109"):
                opp_val = getattr(old_value, "miniJava_FunctionCall109", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_FunctionCall109", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_FunctionCall109"):
                opp_val = getattr(value, "miniJava_FunctionCall109", None)
                setattr(value, "miniJava_FunctionCall109", self)

    @property
    def miniJava_Identifier7(self):
        return self.__miniJava_Identifier7

    @miniJava_Identifier7.setter
    def miniJava_Identifier7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Identifier__miniJava_Identifier7", None)
        self.__miniJava_Identifier7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_MainClass6"):
                opp_val = getattr(old_value, "miniJava_MainClass6", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_MainClass6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_MainClass6"):
                opp_val = getattr(value, "miniJava_MainClass6", None)
                setattr(value, "miniJava_MainClass6", self)

    @property
    def miniJava_Identifier67(self):
        return self.__miniJava_Identifier67

    @miniJava_Identifier67.setter
    def miniJava_Identifier67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Identifier__miniJava_Identifier67", None)
        self.__miniJava_Identifier67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_ArrayAssignment"):
                opp_val = getattr(old_value, "miniJava_ArrayAssignment", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_ArrayAssignment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_ArrayAssignment"):
                opp_val = getattr(value, "miniJava_ArrayAssignment", None)
                setattr(value, "miniJava_ArrayAssignment", self)

    @property
    def miniJava_Identifier43(self):
        return self.__miniJava_Identifier43

    @miniJava_Identifier43.setter
    def miniJava_Identifier43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Identifier__miniJava_Identifier43", None)
        self.__miniJava_Identifier43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_ClassifierType"):
                opp_val = getattr(old_value, "miniJava_ClassifierType", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_ClassifierType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_ClassifierType"):
                opp_val = getattr(value, "miniJava_ClassifierType", None)
                setattr(value, "miniJava_ClassifierType", self)

    @property
    def miniJava_Identifier119(self):
        return self.__miniJava_Identifier119

    @miniJava_Identifier119.setter
    def miniJava_Identifier119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Identifier__miniJava_Identifier119", None)
        self.__miniJava_Identifier119 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_ClassConstruction"):
                opp_val = getattr(old_value, "miniJava_ClassConstruction", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_ClassConstruction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_ClassConstruction"):
                opp_val = getattr(value, "miniJava_ClassConstruction", None)
                setattr(value, "miniJava_ClassConstruction", self)

    @property
    def miniJava_Identifier15(self):
        return self.__miniJava_Identifier15

    @miniJava_Identifier15.setter
    def miniJava_Identifier15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Identifier__miniJava_Identifier15", None)
        self.__miniJava_Identifier15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Class14"):
                opp_val = getattr(old_value, "miniJava_Class14", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Class14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Class14"):
                opp_val = getattr(value, "miniJava_Class14", None)
                setattr(value, "miniJava_Class14", self)

    @property
    def miniJava_Identifier30(self):
        return self.__miniJava_Identifier30

    @miniJava_Identifier30.setter
    def miniJava_Identifier30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Identifier__miniJava_Identifier30", None)
        self.__miniJava_Identifier30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_MethodDeclaration29"):
                opp_val = getattr(old_value, "miniJava_MethodDeclaration29", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_MethodDeclaration29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_MethodDeclaration29"):
                opp_val = getattr(value, "miniJava_MethodDeclaration29", None)
                setattr(value, "miniJava_MethodDeclaration29", self)

    @property
    def miniJava_Identifier12(self):
        return self.__miniJava_Identifier12

    @miniJava_Identifier12.setter
    def miniJava_Identifier12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Identifier__miniJava_Identifier12", None)
        self.__miniJava_Identifier12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Class11"):
                opp_val = getattr(old_value, "miniJava_Class11", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Class11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Class11"):
                opp_val = getattr(value, "miniJava_Class11", None)
                setattr(value, "miniJava_Class11", self)

    @property
    def miniJava_Identifier24(self):
        return self.__miniJava_Identifier24

    @miniJava_Identifier24.setter
    def miniJava_Identifier24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Identifier__miniJava_Identifier24", None)
        self.__miniJava_Identifier24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_VariableDeclaration23"):
                opp_val = getattr(old_value, "miniJava_VariableDeclaration23", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_VariableDeclaration23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_VariableDeclaration23"):
                opp_val = getattr(value, "miniJava_VariableDeclaration23", None)
                setattr(value, "miniJava_VariableDeclaration23", self)

    @property
    def miniJava_Identifier115(self):
        return self.__miniJava_Identifier115

    @miniJava_Identifier115.setter
    def miniJava_Identifier115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Identifier__miniJava_Identifier115", None)
        self.__miniJava_Identifier115 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_ClassifierReference"):
                opp_val = getattr(old_value, "miniJava_ClassifierReference", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_ClassifierReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_ClassifierReference"):
                opp_val = getattr(value, "miniJava_ClassifierReference", None)
                setattr(value, "miniJava_ClassifierReference", self)

class miniJava_Class:

    pass
class miniJava_MainClass:

    pass
class miniJava_Program:

    pass