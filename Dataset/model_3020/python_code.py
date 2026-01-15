from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Expression:

    pass
class javali_Null(Expression):

    pass
class javali_NewObject(Expression):

    pass
class javali_And(Expression):

    pass
class javali_Relation(Expression):

    def __init__(self, operator: str, javali_Relation: "javali_Expression" = None, javali_Relation120: "javali_Expression" = None):
        self.operator = operator
        self.javali_Relation = javali_Relation
        self.javali_Relation120 = javali_Relation120
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def javali_Relation120(self):
        return self.__javali_Relation120

    @javali_Relation120.setter
    def javali_Relation120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javali_Relation__javali_Relation120", None)
        self.__javali_Relation120 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javali_Expression121"):
                opp_val = getattr(old_value, "javali_Expression121", None)
                if opp_val == self:
                    setattr(old_value, "javali_Expression121", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javali_Expression121"):
                opp_val = getattr(value, "javali_Expression121", None)
                setattr(value, "javali_Expression121", self)

    @property
    def javali_Relation(self):
        return self.__javali_Relation

    @javali_Relation.setter
    def javali_Relation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javali_Relation__javali_Relation", None)
        self.__javali_Relation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javali_Expression118"):
                opp_val = getattr(old_value, "javali_Expression118", None)
                if opp_val == self:
                    setattr(old_value, "javali_Expression118", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javali_Expression118"):
                opp_val = getattr(value, "javali_Expression118", None)
                setattr(value, "javali_Expression118", self)

class javali_Multiplication(Expression):

    def __init__(self, operator: str, javali_Multiplication: "javali_Expression" = None, javali_Multiplication130: "javali_Expression" = None):
        self.operator = operator
        self.javali_Multiplication = javali_Multiplication
        self.javali_Multiplication130 = javali_Multiplication130
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def javali_Multiplication130(self):
        return self.__javali_Multiplication130

    @javali_Multiplication130.setter
    def javali_Multiplication130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javali_Multiplication__javali_Multiplication130", None)
        self.__javali_Multiplication130 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javali_Expression131"):
                opp_val = getattr(old_value, "javali_Expression131", None)
                if opp_val == self:
                    setattr(old_value, "javali_Expression131", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javali_Expression131"):
                opp_val = getattr(value, "javali_Expression131", None)
                setattr(value, "javali_Expression131", self)

    @property
    def javali_Multiplication(self):
        return self.__javali_Multiplication

    @javali_Multiplication.setter
    def javali_Multiplication(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javali_Multiplication__javali_Multiplication", None)
        self.__javali_Multiplication = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javali_Expression128"):
                opp_val = getattr(old_value, "javali_Expression128", None)
                if opp_val == self:
                    setattr(old_value, "javali_Expression128", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javali_Expression128"):
                opp_val = getattr(value, "javali_Expression128", None)
                setattr(value, "javali_Expression128", self)

class javali_Addition(Expression):

    def __init__(self, operator: str, javali_Addition: "javali_Expression" = None, javali_Addition125: "javali_Expression" = None):
        self.operator = operator
        self.javali_Addition = javali_Addition
        self.javali_Addition125 = javali_Addition125
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def javali_Addition125(self):
        return self.__javali_Addition125

    @javali_Addition125.setter
    def javali_Addition125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javali_Addition__javali_Addition125", None)
        self.__javali_Addition125 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javali_Expression126"):
                opp_val = getattr(old_value, "javali_Expression126", None)
                if opp_val == self:
                    setattr(old_value, "javali_Expression126", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javali_Expression126"):
                opp_val = getattr(value, "javali_Expression126", None)
                setattr(value, "javali_Expression126", self)

    @property
    def javali_Addition(self):
        return self.__javali_Addition

    @javali_Addition.setter
    def javali_Addition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javali_Addition__javali_Addition", None)
        self.__javali_Addition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javali_Expression123"):
                opp_val = getattr(old_value, "javali_Expression123", None)
                if opp_val == self:
                    setattr(old_value, "javali_Expression123", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javali_Expression123"):
                opp_val = getattr(value, "javali_Expression123", None)
                setattr(value, "javali_Expression123", self)

class javali_Equality(Expression):

    def __init__(self, operator: str, javali_Equality: "javali_Expression" = None, javali_Equality115: "javali_Expression" = None):
        self.operator = operator
        self.javali_Equality = javali_Equality
        self.javali_Equality115 = javali_Equality115
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def javali_Equality(self):
        return self.__javali_Equality

    @javali_Equality.setter
    def javali_Equality(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javali_Equality__javali_Equality", None)
        self.__javali_Equality = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javali_Expression113"):
                opp_val = getattr(old_value, "javali_Expression113", None)
                if opp_val == self:
                    setattr(old_value, "javali_Expression113", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javali_Expression113"):
                opp_val = getattr(value, "javali_Expression113", None)
                setattr(value, "javali_Expression113", self)

    @property
    def javali_Equality115(self):
        return self.__javali_Equality115

    @javali_Equality115.setter
    def javali_Equality115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javali_Equality__javali_Equality115", None)
        self.__javali_Equality115 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javali_Expression116"):
                opp_val = getattr(old_value, "javali_Expression116", None)
                if opp_val == self:
                    setattr(old_value, "javali_Expression116", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javali_Expression116"):
                opp_val = getattr(value, "javali_Expression116", None)
                setattr(value, "javali_Expression116", self)

class javali_Or(Expression):

    pass
class javali_Xor(Expression):

    pass
class javali_NewArray(Expression):

    pass
class javali_VarExpression(Expression):

    pass
class javali_Expression:

    pass
class Statement:

    pass
class javali_IfElse(Statement):

    pass
class javali_While(Statement):

    pass
class javali_For(Statement):

    pass
class javali_DoWhile(Statement):

    pass
class javali_Continue(Statement):

    pass
class javali_VarDeclaration(Statement):

    pass
class javali_ProcCall(Statement, Expression):

    pass
class javali_Decrement(Statement):

    pass
class javali_VarAssign(Statement):

    pass
class javali_Break(Statement):

    pass
class javali_Increment(Statement):

    pass
class javali_Return(Statement):

    pass
class javali_Statement:

    pass
class javali_Block:

    pass
class javali_Constant:

    def __init__(self, static: bool, javali_Constant6: "javali_Type" = None, javali_Constant8: "javali_Identifier" = None, javali_Constant10: "javali_Literal" = None, javali_Constant: "javali_Module" = None):
        self.static = static
        self.javali_Constant6 = javali_Constant6
        self.javali_Constant8 = javali_Constant8
        self.javali_Constant10 = javali_Constant10
        self.javali_Constant = javali_Constant
        
    @property
    def static(self) -> bool:
        return self.__static

    @static.setter
    def static(self, static: bool):
        self.__static = static

    @property
    def javali_Constant10(self):
        return self.__javali_Constant10

    @javali_Constant10.setter
    def javali_Constant10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javali_Constant__javali_Constant10", None)
        self.__javali_Constant10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javali_Literal"):
                opp_val = getattr(old_value, "javali_Literal", None)
                if opp_val == self:
                    setattr(old_value, "javali_Literal", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javali_Literal"):
                opp_val = getattr(value, "javali_Literal", None)
                setattr(value, "javali_Literal", self)

    @property
    def javali_Constant6(self):
        return self.__javali_Constant6

    @javali_Constant6.setter
    def javali_Constant6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javali_Constant__javali_Constant6", None)
        self.__javali_Constant6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javali_Type"):
                opp_val = getattr(old_value, "javali_Type", None)
                if opp_val == self:
                    setattr(old_value, "javali_Type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javali_Type"):
                opp_val = getattr(value, "javali_Type", None)
                setattr(value, "javali_Type", self)

    @property
    def javali_Constant(self):
        return self.__javali_Constant

    @javali_Constant.setter
    def javali_Constant(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javali_Constant__javali_Constant", None)
        self.__javali_Constant = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javali_Module"):
                opp_val = getattr(old_value, "javali_Module", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javali_Module"):
                opp_val = getattr(value, "javali_Module", None)
                if opp_val is None:
                    setattr(value, "javali_Module", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def javali_Constant8(self):
        return self.__javali_Constant8

    @javali_Constant8.setter
    def javali_Constant8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javali_Constant__javali_Constant8", None)
        self.__javali_Constant8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javali_Identifier"):
                opp_val = getattr(old_value, "javali_Identifier", None)
                if opp_val == self:
                    setattr(old_value, "javali_Identifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javali_Identifier"):
                opp_val = getattr(value, "javali_Identifier", None)
                setattr(value, "javali_Identifier", self)

class javali_Module:

    pass
class javali_Literal(Expression):

    def __init__(self, value: str, javali_Literal: "javali_Constant" = None):
        self.value = value
        self.javali_Literal = javali_Literal
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def javali_Literal(self):
        return self.__javali_Literal

    @javali_Literal.setter
    def javali_Literal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javali_Literal__javali_Literal", None)
        self.__javali_Literal = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javali_Constant10"):
                opp_val = getattr(old_value, "javali_Constant10", None)
                if opp_val == self:
                    setattr(old_value, "javali_Constant10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javali_Constant10"):
                opp_val = getattr(value, "javali_Constant10", None)
                setattr(value, "javali_Constant10", self)

class javali_Identifier:

    def __init__(self, id: str, javali_Identifier: "javali_Constant" = None, javali_Identifier21: "javali_Procedure" = None, javali_Identifier13: "javali_Record" = None, javali_Identifier35: "javali_VarDeclaration" = None, javali_Identifier73: "javali_Increment" = None, javali_Identifier83: "javali_ProcCall" = None, javali_Identifier89: "javali_Type" = None, javali_Identifier91: "javali_NewArray" = None, javali_Identifier75: "javali_Decrement" = None, javali_Identifier78: "javali_VarExpression" = None, javali_Identifier96: "javali_NewObject" = None):
        self.id = id
        self.javali_Identifier = javali_Identifier
        self.javali_Identifier21 = javali_Identifier21
        self.javali_Identifier13 = javali_Identifier13
        self.javali_Identifier35 = javali_Identifier35
        self.javali_Identifier73 = javali_Identifier73
        self.javali_Identifier83 = javali_Identifier83
        self.javali_Identifier89 = javali_Identifier89
        self.javali_Identifier91 = javali_Identifier91
        self.javali_Identifier75 = javali_Identifier75
        self.javali_Identifier78 = javali_Identifier78
        self.javali_Identifier96 = javali_Identifier96
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def javali_Identifier78(self):
        return self.__javali_Identifier78

    @javali_Identifier78.setter
    def javali_Identifier78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javali_Identifier__javali_Identifier78", None)
        self.__javali_Identifier78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javali_VarExpression77"):
                opp_val = getattr(old_value, "javali_VarExpression77", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javali_VarExpression77"):
                opp_val = getattr(value, "javali_VarExpression77", None)
                if opp_val is None:
                    setattr(value, "javali_VarExpression77", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def javali_Identifier35(self):
        return self.__javali_Identifier35

    @javali_Identifier35.setter
    def javali_Identifier35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javali_Identifier__javali_Identifier35", None)
        self.__javali_Identifier35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javali_VarDeclaration34"):
                opp_val = getattr(old_value, "javali_VarDeclaration34", None)
                if opp_val == self:
                    setattr(old_value, "javali_VarDeclaration34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javali_VarDeclaration34"):
                opp_val = getattr(value, "javali_VarDeclaration34", None)
                setattr(value, "javali_VarDeclaration34", self)

    @property
    def javali_Identifier83(self):
        return self.__javali_Identifier83

    @javali_Identifier83.setter
    def javali_Identifier83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javali_Identifier__javali_Identifier83", None)
        self.__javali_Identifier83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javali_ProcCall"):
                opp_val = getattr(old_value, "javali_ProcCall", None)
                if opp_val == self:
                    setattr(old_value, "javali_ProcCall", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javali_ProcCall"):
                opp_val = getattr(value, "javali_ProcCall", None)
                setattr(value, "javali_ProcCall", self)

    @property
    def javali_Identifier73(self):
        return self.__javali_Identifier73

    @javali_Identifier73.setter
    def javali_Identifier73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javali_Identifier__javali_Identifier73", None)
        self.__javali_Identifier73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javali_Increment"):
                opp_val = getattr(old_value, "javali_Increment", None)
                if opp_val == self:
                    setattr(old_value, "javali_Increment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javali_Increment"):
                opp_val = getattr(value, "javali_Increment", None)
                setattr(value, "javali_Increment", self)

    @property
    def javali_Identifier21(self):
        return self.__javali_Identifier21

    @javali_Identifier21.setter
    def javali_Identifier21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javali_Identifier__javali_Identifier21", None)
        self.__javali_Identifier21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javali_Procedure20"):
                opp_val = getattr(old_value, "javali_Procedure20", None)
                if opp_val == self:
                    setattr(old_value, "javali_Procedure20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javali_Procedure20"):
                opp_val = getattr(value, "javali_Procedure20", None)
                setattr(value, "javali_Procedure20", self)

    @property
    def javali_Identifier89(self):
        return self.__javali_Identifier89

    @javali_Identifier89.setter
    def javali_Identifier89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javali_Identifier__javali_Identifier89", None)
        self.__javali_Identifier89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javali_Type88"):
                opp_val = getattr(old_value, "javali_Type88", None)
                if opp_val == self:
                    setattr(old_value, "javali_Type88", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javali_Type88"):
                opp_val = getattr(value, "javali_Type88", None)
                setattr(value, "javali_Type88", self)

    @property
    def javali_Identifier91(self):
        return self.__javali_Identifier91

    @javali_Identifier91.setter
    def javali_Identifier91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javali_Identifier__javali_Identifier91", None)
        self.__javali_Identifier91 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javali_NewArray"):
                opp_val = getattr(old_value, "javali_NewArray", None)
                if opp_val == self:
                    setattr(old_value, "javali_NewArray", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javali_NewArray"):
                opp_val = getattr(value, "javali_NewArray", None)
                setattr(value, "javali_NewArray", self)

    @property
    def javali_Identifier75(self):
        return self.__javali_Identifier75

    @javali_Identifier75.setter
    def javali_Identifier75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javali_Identifier__javali_Identifier75", None)
        self.__javali_Identifier75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javali_Decrement"):
                opp_val = getattr(old_value, "javali_Decrement", None)
                if opp_val == self:
                    setattr(old_value, "javali_Decrement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javali_Decrement"):
                opp_val = getattr(value, "javali_Decrement", None)
                setattr(value, "javali_Decrement", self)

    @property
    def javali_Identifier13(self):
        return self.__javali_Identifier13

    @javali_Identifier13.setter
    def javali_Identifier13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javali_Identifier__javali_Identifier13", None)
        self.__javali_Identifier13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javali_Record12"):
                opp_val = getattr(old_value, "javali_Record12", None)
                if opp_val == self:
                    setattr(old_value, "javali_Record12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javali_Record12"):
                opp_val = getattr(value, "javali_Record12", None)
                setattr(value, "javali_Record12", self)

    @property
    def javali_Identifier(self):
        return self.__javali_Identifier

    @javali_Identifier.setter
    def javali_Identifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javali_Identifier__javali_Identifier", None)
        self.__javali_Identifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javali_Constant8"):
                opp_val = getattr(old_value, "javali_Constant8", None)
                if opp_val == self:
                    setattr(old_value, "javali_Constant8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javali_Constant8"):
                opp_val = getattr(value, "javali_Constant8", None)
                setattr(value, "javali_Constant8", self)

    @property
    def javali_Identifier96(self):
        return self.__javali_Identifier96

    @javali_Identifier96.setter
    def javali_Identifier96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javali_Identifier__javali_Identifier96", None)
        self.__javali_Identifier96 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javali_NewObject"):
                opp_val = getattr(old_value, "javali_NewObject", None)
                if opp_val == self:
                    setattr(old_value, "javali_NewObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javali_NewObject"):
                opp_val = getattr(value, "javali_NewObject", None)
                setattr(value, "javali_NewObject", self)

class javali_Type:

    def __init__(self, arrayDims: str, javali_Type: "javali_Constant" = None, javali_Type18: "javali_Procedure" = None, javali_Type32: "javali_VarDeclaration" = None, javali_Type88: "javali_Identifier" = None):
        self.arrayDims = arrayDims
        self.javali_Type = javali_Type
        self.javali_Type18 = javali_Type18
        self.javali_Type32 = javali_Type32
        self.javali_Type88 = javali_Type88
        
    @property
    def arrayDims(self) -> str:
        return self.__arrayDims

    @arrayDims.setter
    def arrayDims(self, arrayDims: str):
        self.__arrayDims = arrayDims

    @property
    def javali_Type(self):
        return self.__javali_Type

    @javali_Type.setter
    def javali_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javali_Type__javali_Type", None)
        self.__javali_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javali_Constant6"):
                opp_val = getattr(old_value, "javali_Constant6", None)
                if opp_val == self:
                    setattr(old_value, "javali_Constant6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javali_Constant6"):
                opp_val = getattr(value, "javali_Constant6", None)
                setattr(value, "javali_Constant6", self)

    @property
    def javali_Type88(self):
        return self.__javali_Type88

    @javali_Type88.setter
    def javali_Type88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javali_Type__javali_Type88", None)
        self.__javali_Type88 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javali_Identifier89"):
                opp_val = getattr(old_value, "javali_Identifier89", None)
                if opp_val == self:
                    setattr(old_value, "javali_Identifier89", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javali_Identifier89"):
                opp_val = getattr(value, "javali_Identifier89", None)
                setattr(value, "javali_Identifier89", self)

    @property
    def javali_Type32(self):
        return self.__javali_Type32

    @javali_Type32.setter
    def javali_Type32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javali_Type__javali_Type32", None)
        self.__javali_Type32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javali_VarDeclaration31"):
                opp_val = getattr(old_value, "javali_VarDeclaration31", None)
                if opp_val == self:
                    setattr(old_value, "javali_VarDeclaration31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javali_VarDeclaration31"):
                opp_val = getattr(value, "javali_VarDeclaration31", None)
                setattr(value, "javali_VarDeclaration31", self)

    @property
    def javali_Type18(self):
        return self.__javali_Type18

    @javali_Type18.setter
    def javali_Type18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javali_Type__javali_Type18", None)
        self.__javali_Type18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javali_Procedure17"):
                opp_val = getattr(old_value, "javali_Procedure17", None)
                if opp_val == self:
                    setattr(old_value, "javali_Procedure17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javali_Procedure17"):
                opp_val = getattr(value, "javali_Procedure17", None)
                setattr(value, "javali_Procedure17", self)

class javali_Procedure:

    def __init__(self, void: bool, comment: str, static: bool, javali_Procedure: "javali_Module" = None, javali_Procedure20: "javali_Identifier" = None, javali_Procedure23: set["javali_VarDeclaration"] = None, javali_Procedure26: "javali_Block" = None, javali_Procedure17: "javali_Type" = None):
        self.void = void
        self.comment = comment
        self.static = static
        self.javali_Procedure = javali_Procedure
        self.javali_Procedure20 = javali_Procedure20
        self.javali_Procedure23 = javali_Procedure23 if javali_Procedure23 is not None else set()
        self.javali_Procedure26 = javali_Procedure26
        self.javali_Procedure17 = javali_Procedure17
        
    @property
    def static(self) -> bool:
        return self.__static

    @static.setter
    def static(self, static: bool):
        self.__static = static

    @property
    def void(self) -> bool:
        return self.__void

    @void.setter
    def void(self, void: bool):
        self.__void = void

    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def javali_Procedure(self):
        return self.__javali_Procedure

    @javali_Procedure.setter
    def javali_Procedure(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javali_Procedure__javali_Procedure", None)
        self.__javali_Procedure = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javali_Module4"):
                opp_val = getattr(old_value, "javali_Module4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javali_Module4"):
                opp_val = getattr(value, "javali_Module4", None)
                if opp_val is None:
                    setattr(value, "javali_Module4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def javali_Procedure23(self):
        return self.__javali_Procedure23

    @javali_Procedure23.setter
    def javali_Procedure23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javali_Procedure__javali_Procedure23", None)
        self.__javali_Procedure23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "javali_VarDeclaration24"):
                    opp_val = getattr(item, "javali_VarDeclaration24", None)
                    
                    if opp_val == self:
                        setattr(item, "javali_VarDeclaration24", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "javali_VarDeclaration24"):
                    opp_val = getattr(item, "javali_VarDeclaration24", None)
                    
                    setattr(item, "javali_VarDeclaration24", self)
                    

    @property
    def javali_Procedure20(self):
        return self.__javali_Procedure20

    @javali_Procedure20.setter
    def javali_Procedure20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javali_Procedure__javali_Procedure20", None)
        self.__javali_Procedure20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javali_Identifier21"):
                opp_val = getattr(old_value, "javali_Identifier21", None)
                if opp_val == self:
                    setattr(old_value, "javali_Identifier21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javali_Identifier21"):
                opp_val = getattr(value, "javali_Identifier21", None)
                setattr(value, "javali_Identifier21", self)

    @property
    def javali_Procedure26(self):
        return self.__javali_Procedure26

    @javali_Procedure26.setter
    def javali_Procedure26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javali_Procedure__javali_Procedure26", None)
        self.__javali_Procedure26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javali_Block"):
                opp_val = getattr(old_value, "javali_Block", None)
                if opp_val == self:
                    setattr(old_value, "javali_Block", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javali_Block"):
                opp_val = getattr(value, "javali_Block", None)
                setattr(value, "javali_Block", self)

    @property
    def javali_Procedure17(self):
        return self.__javali_Procedure17

    @javali_Procedure17.setter
    def javali_Procedure17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javali_Procedure__javali_Procedure17", None)
        self.__javali_Procedure17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javali_Type18"):
                opp_val = getattr(old_value, "javali_Type18", None)
                if opp_val == self:
                    setattr(old_value, "javali_Type18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javali_Type18"):
                opp_val = getattr(value, "javali_Type18", None)
                setattr(value, "javali_Type18", self)

class javali_Record:

    pass