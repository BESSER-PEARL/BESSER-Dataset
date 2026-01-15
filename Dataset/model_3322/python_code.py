from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Expr:

    pass
class miniJava_Multiplication(Expr):

    pass
class miniJava_Point(Expr):

    pass
class miniJava_SquareBrackets(Expr):

    pass
class miniJava_Addition(Expr):

    pass
class miniJava_Expression(Expr):

    pass
class miniJava_MethodCall:

    pass
class miniJava_NumberValue:

    def __init__(self, value: int, miniJava_NumberValue: "miniJava_Expr" = None):
        self.value = value
        self.miniJava_NumberValue = miniJava_NumberValue
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def miniJava_NumberValue(self):
        return self.__miniJava_NumberValue

    @miniJava_NumberValue.setter
    def miniJava_NumberValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_NumberValue__miniJava_NumberValue", None)
        self.__miniJava_NumberValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Expr58"):
                opp_val = getattr(old_value, "miniJava_Expr58", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Expr58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Expr58"):
                opp_val = getattr(value, "miniJava_Expr58", None)
                setattr(value, "miniJava_Expr58", self)

class miniJava_Expr:

    def __init__(self, expressionType: str, miniJava_Expr: "miniJava_Method" = None, miniJava_Expr38: "miniJava_Statement" = None, miniJava_Expr44: "miniJava_Statement" = None, miniJava_Expr47: "miniJava_Expr" = None, miniJava_Expr45: "miniJava_Expr" = None, miniJava_Expr50: "miniJava_Expr" = None, miniJava_Expr48: "miniJava_Expr" = None, miniJava_Expr52: "miniJava_Type" = None, miniJava_Expr55: "miniJava_Variable" = None, miniJava_Expr58: "miniJava_NumberValue" = None, miniJava_Expr60: "miniJava_MethodCall" = None, miniJava_Expr63: "miniJava_Expr" = None, miniJava_Expr61: "miniJava_Expr" = None, miniJava_Expr69: "miniJava_MethodCall" = None):
        self.expressionType = expressionType
        self.miniJava_Expr = miniJava_Expr
        self.miniJava_Expr38 = miniJava_Expr38
        self.miniJava_Expr44 = miniJava_Expr44
        self.miniJava_Expr47 = miniJava_Expr47
        self.miniJava_Expr45 = miniJava_Expr45
        self.miniJava_Expr50 = miniJava_Expr50
        self.miniJava_Expr48 = miniJava_Expr48
        self.miniJava_Expr52 = miniJava_Expr52
        self.miniJava_Expr55 = miniJava_Expr55
        self.miniJava_Expr58 = miniJava_Expr58
        self.miniJava_Expr60 = miniJava_Expr60
        self.miniJava_Expr63 = miniJava_Expr63
        self.miniJava_Expr61 = miniJava_Expr61
        self.miniJava_Expr69 = miniJava_Expr69
        
    @property
    def expressionType(self) -> str:
        return self.__expressionType

    @expressionType.setter
    def expressionType(self, expressionType: str):
        self.__expressionType = expressionType

    @property
    def miniJava_Expr47(self):
        return self.__miniJava_Expr47

    @miniJava_Expr47.setter
    def miniJava_Expr47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Expr__miniJava_Expr47", None)
        self.__miniJava_Expr47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Expr45"):
                opp_val = getattr(old_value, "miniJava_Expr45", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Expr45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Expr45"):
                opp_val = getattr(value, "miniJava_Expr45", None)
                setattr(value, "miniJava_Expr45", self)

    @property
    def miniJava_Expr55(self):
        return self.__miniJava_Expr55

    @miniJava_Expr55.setter
    def miniJava_Expr55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Expr__miniJava_Expr55", None)
        self.__miniJava_Expr55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Variable56"):
                opp_val = getattr(old_value, "miniJava_Variable56", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Variable56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Variable56"):
                opp_val = getattr(value, "miniJava_Variable56", None)
                setattr(value, "miniJava_Variable56", self)

    @property
    def miniJava_Expr48(self):
        return self.__miniJava_Expr48

    @miniJava_Expr48.setter
    def miniJava_Expr48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Expr__miniJava_Expr48", None)
        self.__miniJava_Expr48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Expr50"):
                opp_val = getattr(old_value, "miniJava_Expr50", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Expr50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Expr50"):
                opp_val = getattr(value, "miniJava_Expr50", None)
                setattr(value, "miniJava_Expr50", self)

    @property
    def miniJava_Expr45(self):
        return self.__miniJava_Expr45

    @miniJava_Expr45.setter
    def miniJava_Expr45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Expr__miniJava_Expr45", None)
        self.__miniJava_Expr45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Expr47"):
                opp_val = getattr(old_value, "miniJava_Expr47", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Expr47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Expr47"):
                opp_val = getattr(value, "miniJava_Expr47", None)
                setattr(value, "miniJava_Expr47", self)

    @property
    def miniJava_Expr60(self):
        return self.__miniJava_Expr60

    @miniJava_Expr60.setter
    def miniJava_Expr60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Expr__miniJava_Expr60", None)
        self.__miniJava_Expr60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_MethodCall"):
                opp_val = getattr(old_value, "miniJava_MethodCall", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_MethodCall", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_MethodCall"):
                opp_val = getattr(value, "miniJava_MethodCall", None)
                setattr(value, "miniJava_MethodCall", self)

    @property
    def miniJava_Expr61(self):
        return self.__miniJava_Expr61

    @miniJava_Expr61.setter
    def miniJava_Expr61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Expr__miniJava_Expr61", None)
        self.__miniJava_Expr61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Expr63"):
                opp_val = getattr(old_value, "miniJava_Expr63", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Expr63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Expr63"):
                opp_val = getattr(value, "miniJava_Expr63", None)
                setattr(value, "miniJava_Expr63", self)

    @property
    def miniJava_Expr58(self):
        return self.__miniJava_Expr58

    @miniJava_Expr58.setter
    def miniJava_Expr58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Expr__miniJava_Expr58", None)
        self.__miniJava_Expr58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_NumberValue"):
                opp_val = getattr(old_value, "miniJava_NumberValue", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_NumberValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_NumberValue"):
                opp_val = getattr(value, "miniJava_NumberValue", None)
                setattr(value, "miniJava_NumberValue", self)

    @property
    def miniJava_Expr(self):
        return self.__miniJava_Expr

    @miniJava_Expr.setter
    def miniJava_Expr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Expr__miniJava_Expr", None)
        self.__miniJava_Expr = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Method32"):
                opp_val = getattr(old_value, "miniJava_Method32", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Method32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Method32"):
                opp_val = getattr(value, "miniJava_Method32", None)
                setattr(value, "miniJava_Method32", self)

    @property
    def miniJava_Expr63(self):
        return self.__miniJava_Expr63

    @miniJava_Expr63.setter
    def miniJava_Expr63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Expr__miniJava_Expr63", None)
        self.__miniJava_Expr63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Expr61"):
                opp_val = getattr(old_value, "miniJava_Expr61", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Expr61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Expr61"):
                opp_val = getattr(value, "miniJava_Expr61", None)
                setattr(value, "miniJava_Expr61", self)

    @property
    def miniJava_Expr50(self):
        return self.__miniJava_Expr50

    @miniJava_Expr50.setter
    def miniJava_Expr50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Expr__miniJava_Expr50", None)
        self.__miniJava_Expr50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Expr48"):
                opp_val = getattr(old_value, "miniJava_Expr48", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Expr48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Expr48"):
                opp_val = getattr(value, "miniJava_Expr48", None)
                setattr(value, "miniJava_Expr48", self)

    @property
    def miniJava_Expr38(self):
        return self.__miniJava_Expr38

    @miniJava_Expr38.setter
    def miniJava_Expr38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Expr__miniJava_Expr38", None)
        self.__miniJava_Expr38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Statement37"):
                opp_val = getattr(old_value, "miniJava_Statement37", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Statement37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Statement37"):
                opp_val = getattr(value, "miniJava_Statement37", None)
                setattr(value, "miniJava_Statement37", self)

    @property
    def miniJava_Expr44(self):
        return self.__miniJava_Expr44

    @miniJava_Expr44.setter
    def miniJava_Expr44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Expr__miniJava_Expr44", None)
        self.__miniJava_Expr44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Statement43"):
                opp_val = getattr(old_value, "miniJava_Statement43", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Statement43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Statement43"):
                opp_val = getattr(value, "miniJava_Statement43", None)
                setattr(value, "miniJava_Statement43", self)

    @property
    def miniJava_Expr52(self):
        return self.__miniJava_Expr52

    @miniJava_Expr52.setter
    def miniJava_Expr52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Expr__miniJava_Expr52", None)
        self.__miniJava_Expr52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Type53"):
                opp_val = getattr(old_value, "miniJava_Type53", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Type53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Type53"):
                opp_val = getattr(value, "miniJava_Type53", None)
                setattr(value, "miniJava_Type53", self)

    @property
    def miniJava_Expr69(self):
        return self.__miniJava_Expr69

    @miniJava_Expr69.setter
    def miniJava_Expr69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Expr__miniJava_Expr69", None)
        self.__miniJava_Expr69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_MethodCall68"):
                opp_val = getattr(old_value, "miniJava_MethodCall68", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_MethodCall68"):
                opp_val = getattr(value, "miniJava_MethodCall68", None)
                if opp_val is None:
                    setattr(value, "miniJava_MethodCall68", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class miniJava_Variable:

    def __init__(self, name: str, miniJava_Variable: "miniJava_VarDeclaration" = None, miniJava_Variable17: "miniJava_Type" = None, miniJava_Variable24: "miniJava_Method" = None, miniJava_Variable41: "miniJava_Statement" = None, miniJava_Variable56: "miniJava_Expr" = None):
        self.name = name
        self.miniJava_Variable = miniJava_Variable
        self.miniJava_Variable17 = miniJava_Variable17
        self.miniJava_Variable24 = miniJava_Variable24
        self.miniJava_Variable41 = miniJava_Variable41
        self.miniJava_Variable56 = miniJava_Variable56
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def miniJava_Variable(self):
        return self.__miniJava_Variable

    @miniJava_Variable.setter
    def miniJava_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Variable__miniJava_Variable", None)
        self.__miniJava_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_VarDeclaration15"):
                opp_val = getattr(old_value, "miniJava_VarDeclaration15", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_VarDeclaration15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_VarDeclaration15"):
                opp_val = getattr(value, "miniJava_VarDeclaration15", None)
                setattr(value, "miniJava_VarDeclaration15", self)

    @property
    def miniJava_Variable41(self):
        return self.__miniJava_Variable41

    @miniJava_Variable41.setter
    def miniJava_Variable41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Variable__miniJava_Variable41", None)
        self.__miniJava_Variable41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Statement40"):
                opp_val = getattr(old_value, "miniJava_Statement40", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Statement40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Statement40"):
                opp_val = getattr(value, "miniJava_Statement40", None)
                setattr(value, "miniJava_Statement40", self)

    @property
    def miniJava_Variable24(self):
        return self.__miniJava_Variable24

    @miniJava_Variable24.setter
    def miniJava_Variable24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Variable__miniJava_Variable24", None)
        self.__miniJava_Variable24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Method23"):
                opp_val = getattr(old_value, "miniJava_Method23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Method23"):
                opp_val = getattr(value, "miniJava_Method23", None)
                if opp_val is None:
                    setattr(value, "miniJava_Method23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def miniJava_Variable56(self):
        return self.__miniJava_Variable56

    @miniJava_Variable56.setter
    def miniJava_Variable56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Variable__miniJava_Variable56", None)
        self.__miniJava_Variable56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Expr55"):
                opp_val = getattr(old_value, "miniJava_Expr55", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Expr55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Expr55"):
                opp_val = getattr(value, "miniJava_Expr55", None)
                setattr(value, "miniJava_Expr55", self)

    @property
    def miniJava_Variable17(self):
        return self.__miniJava_Variable17

    @miniJava_Variable17.setter
    def miniJava_Variable17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Variable__miniJava_Variable17", None)
        self.__miniJava_Variable17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Type18"):
                opp_val = getattr(old_value, "miniJava_Type18", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Type18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Type18"):
                opp_val = getattr(value, "miniJava_Type18", None)
                setattr(value, "miniJava_Type18", self)

class miniJava_Type:

    def __init__(self, typeName: str, miniJava_Type: "miniJava_ClassDecl" = None, miniJava_Type18: "miniJava_Variable" = None, miniJava_Type21: "miniJava_Method" = None, miniJava_Type53: "miniJava_Expr" = None):
        self.typeName = typeName
        self.miniJava_Type = miniJava_Type
        self.miniJava_Type18 = miniJava_Type18
        self.miniJava_Type21 = miniJava_Type21
        self.miniJava_Type53 = miniJava_Type53
        
    @property
    def typeName(self) -> str:
        return self.__typeName

    @typeName.setter
    def typeName(self, typeName: str):
        self.__typeName = typeName

    @property
    def miniJava_Type53(self):
        return self.__miniJava_Type53

    @miniJava_Type53.setter
    def miniJava_Type53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Type__miniJava_Type53", None)
        self.__miniJava_Type53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Expr52"):
                opp_val = getattr(old_value, "miniJava_Expr52", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Expr52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Expr52"):
                opp_val = getattr(value, "miniJava_Expr52", None)
                setattr(value, "miniJava_Expr52", self)

    @property
    def miniJava_Type(self):
        return self.__miniJava_Type

    @miniJava_Type.setter
    def miniJava_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Type__miniJava_Type", None)
        self.__miniJava_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_ClassDecl13"):
                opp_val = getattr(old_value, "miniJava_ClassDecl13", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_ClassDecl13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_ClassDecl13"):
                opp_val = getattr(value, "miniJava_ClassDecl13", None)
                setattr(value, "miniJava_ClassDecl13", self)

    @property
    def miniJava_Type21(self):
        return self.__miniJava_Type21

    @miniJava_Type21.setter
    def miniJava_Type21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Type__miniJava_Type21", None)
        self.__miniJava_Type21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Method20"):
                opp_val = getattr(old_value, "miniJava_Method20", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Method20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Method20"):
                opp_val = getattr(value, "miniJava_Method20", None)
                setattr(value, "miniJava_Method20", self)

    @property
    def miniJava_Type18(self):
        return self.__miniJava_Type18

    @miniJava_Type18.setter
    def miniJava_Type18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Type__miniJava_Type18", None)
        self.__miniJava_Type18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Variable17"):
                opp_val = getattr(old_value, "miniJava_Variable17", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Variable17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Variable17"):
                opp_val = getattr(value, "miniJava_Variable17", None)
                setattr(value, "miniJava_Variable17", self)

class miniJava_Statement:

    def __init__(self, statementType: str, isArrayElementAssignment: bool, miniJava_Statement: "miniJava_MainMethod" = None, miniJava_Statement30: "miniJava_Method" = None, miniJava_Statement35: "miniJava_Statement" = None, miniJava_Statement33: set["miniJava_Statement"] = None, miniJava_Statement37: "miniJava_Expr" = None, miniJava_Statement40: "miniJava_Variable" = None, miniJava_Statement43: "miniJava_Expr" = None):
        self.statementType = statementType
        self.isArrayElementAssignment = isArrayElementAssignment
        self.miniJava_Statement = miniJava_Statement
        self.miniJava_Statement30 = miniJava_Statement30
        self.miniJava_Statement35 = miniJava_Statement35
        self.miniJava_Statement33 = miniJava_Statement33 if miniJava_Statement33 is not None else set()
        self.miniJava_Statement37 = miniJava_Statement37
        self.miniJava_Statement40 = miniJava_Statement40
        self.miniJava_Statement43 = miniJava_Statement43
        
    @property
    def isArrayElementAssignment(self) -> bool:
        return self.__isArrayElementAssignment

    @isArrayElementAssignment.setter
    def isArrayElementAssignment(self, isArrayElementAssignment: bool):
        self.__isArrayElementAssignment = isArrayElementAssignment

    @property
    def statementType(self) -> str:
        return self.__statementType

    @statementType.setter
    def statementType(self, statementType: str):
        self.__statementType = statementType

    @property
    def miniJava_Statement33(self):
        return self.__miniJava_Statement33

    @miniJava_Statement33.setter
    def miniJava_Statement33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Statement__miniJava_Statement33", None)
        self.__miniJava_Statement33 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "miniJava_Statement35"):
                    opp_val = getattr(item, "miniJava_Statement35", None)
                    
                    if opp_val == self:
                        setattr(item, "miniJava_Statement35", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "miniJava_Statement35"):
                    opp_val = getattr(item, "miniJava_Statement35", None)
                    
                    setattr(item, "miniJava_Statement35", self)
                    

    @property
    def miniJava_Statement35(self):
        return self.__miniJava_Statement35

    @miniJava_Statement35.setter
    def miniJava_Statement35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Statement__miniJava_Statement35", None)
        self.__miniJava_Statement35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Statement33"):
                opp_val = getattr(old_value, "miniJava_Statement33", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Statement33"):
                opp_val = getattr(value, "miniJava_Statement33", None)
                if opp_val is None:
                    setattr(value, "miniJava_Statement33", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def miniJava_Statement(self):
        return self.__miniJava_Statement

    @miniJava_Statement.setter
    def miniJava_Statement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Statement__miniJava_Statement", None)
        self.__miniJava_Statement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_MainMethod11"):
                opp_val = getattr(old_value, "miniJava_MainMethod11", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_MainMethod11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_MainMethod11"):
                opp_val = getattr(value, "miniJava_MainMethod11", None)
                setattr(value, "miniJava_MainMethod11", self)

    @property
    def miniJava_Statement43(self):
        return self.__miniJava_Statement43

    @miniJava_Statement43.setter
    def miniJava_Statement43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Statement__miniJava_Statement43", None)
        self.__miniJava_Statement43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Expr44"):
                opp_val = getattr(old_value, "miniJava_Expr44", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Expr44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Expr44"):
                opp_val = getattr(value, "miniJava_Expr44", None)
                setattr(value, "miniJava_Expr44", self)

    @property
    def miniJava_Statement40(self):
        return self.__miniJava_Statement40

    @miniJava_Statement40.setter
    def miniJava_Statement40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Statement__miniJava_Statement40", None)
        self.__miniJava_Statement40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Variable41"):
                opp_val = getattr(old_value, "miniJava_Variable41", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Variable41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Variable41"):
                opp_val = getattr(value, "miniJava_Variable41", None)
                setattr(value, "miniJava_Variable41", self)

    @property
    def miniJava_Statement30(self):
        return self.__miniJava_Statement30

    @miniJava_Statement30.setter
    def miniJava_Statement30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Statement__miniJava_Statement30", None)
        self.__miniJava_Statement30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Method29"):
                opp_val = getattr(old_value, "miniJava_Method29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Method29"):
                opp_val = getattr(value, "miniJava_Method29", None)
                if opp_val is None:
                    setattr(value, "miniJava_Method29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def miniJava_Statement37(self):
        return self.__miniJava_Statement37

    @miniJava_Statement37.setter
    def miniJava_Statement37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Statement__miniJava_Statement37", None)
        self.__miniJava_Statement37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Expr38"):
                opp_val = getattr(old_value, "miniJava_Expr38", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Expr38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Expr38"):
                opp_val = getattr(value, "miniJava_Expr38", None)
                setattr(value, "miniJava_Expr38", self)

class miniJava_Method:

    def __init__(self, name: str, miniJava_Method: "miniJava_ClassDecl" = None, miniJava_Method20: "miniJava_Type" = None, miniJava_Method23: set["miniJava_Variable"] = None, miniJava_Method26: set["miniJava_VarDeclaration"] = None, miniJava_Method29: set["miniJava_Statement"] = None, miniJava_Method32: "miniJava_Expr" = None, miniJava_Method66: "miniJava_MethodCall" = None):
        self.name = name
        self.miniJava_Method = miniJava_Method
        self.miniJava_Method20 = miniJava_Method20
        self.miniJava_Method23 = miniJava_Method23 if miniJava_Method23 is not None else set()
        self.miniJava_Method26 = miniJava_Method26 if miniJava_Method26 is not None else set()
        self.miniJava_Method29 = miniJava_Method29 if miniJava_Method29 is not None else set()
        self.miniJava_Method32 = miniJava_Method32
        self.miniJava_Method66 = miniJava_Method66
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def miniJava_Method32(self):
        return self.__miniJava_Method32

    @miniJava_Method32.setter
    def miniJava_Method32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Method__miniJava_Method32", None)
        self.__miniJava_Method32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Expr"):
                opp_val = getattr(old_value, "miniJava_Expr", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Expr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Expr"):
                opp_val = getattr(value, "miniJava_Expr", None)
                setattr(value, "miniJava_Expr", self)

    @property
    def miniJava_Method29(self):
        return self.__miniJava_Method29

    @miniJava_Method29.setter
    def miniJava_Method29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Method__miniJava_Method29", None)
        self.__miniJava_Method29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "miniJava_Statement30"):
                    opp_val = getattr(item, "miniJava_Statement30", None)
                    
                    if opp_val == self:
                        setattr(item, "miniJava_Statement30", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "miniJava_Statement30"):
                    opp_val = getattr(item, "miniJava_Statement30", None)
                    
                    setattr(item, "miniJava_Statement30", self)
                    

    @property
    def miniJava_Method26(self):
        return self.__miniJava_Method26

    @miniJava_Method26.setter
    def miniJava_Method26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Method__miniJava_Method26", None)
        self.__miniJava_Method26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "miniJava_VarDeclaration27"):
                    opp_val = getattr(item, "miniJava_VarDeclaration27", None)
                    
                    if opp_val == self:
                        setattr(item, "miniJava_VarDeclaration27", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "miniJava_VarDeclaration27"):
                    opp_val = getattr(item, "miniJava_VarDeclaration27", None)
                    
                    setattr(item, "miniJava_VarDeclaration27", self)
                    

    @property
    def miniJava_Method20(self):
        return self.__miniJava_Method20

    @miniJava_Method20.setter
    def miniJava_Method20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Method__miniJava_Method20", None)
        self.__miniJava_Method20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Type21"):
                opp_val = getattr(old_value, "miniJava_Type21", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Type21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Type21"):
                opp_val = getattr(value, "miniJava_Type21", None)
                setattr(value, "miniJava_Type21", self)

    @property
    def miniJava_Method66(self):
        return self.__miniJava_Method66

    @miniJava_Method66.setter
    def miniJava_Method66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Method__miniJava_Method66", None)
        self.__miniJava_Method66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_MethodCall65"):
                opp_val = getattr(old_value, "miniJava_MethodCall65", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_MethodCall65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_MethodCall65"):
                opp_val = getattr(value, "miniJava_MethodCall65", None)
                setattr(value, "miniJava_MethodCall65", self)

    @property
    def miniJava_Method23(self):
        return self.__miniJava_Method23

    @miniJava_Method23.setter
    def miniJava_Method23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Method__miniJava_Method23", None)
        self.__miniJava_Method23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "miniJava_Variable24"):
                    opp_val = getattr(item, "miniJava_Variable24", None)
                    
                    if opp_val == self:
                        setattr(item, "miniJava_Variable24", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "miniJava_Variable24"):
                    opp_val = getattr(item, "miniJava_Variable24", None)
                    
                    setattr(item, "miniJava_Variable24", self)
                    

    @property
    def miniJava_Method(self):
        return self.__miniJava_Method

    @miniJava_Method.setter
    def miniJava_Method(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_Method__miniJava_Method", None)
        self.__miniJava_Method = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_ClassDecl9"):
                opp_val = getattr(old_value, "miniJava_ClassDecl9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_ClassDecl9"):
                opp_val = getattr(value, "miniJava_ClassDecl9", None)
                if opp_val is None:
                    setattr(value, "miniJava_ClassDecl9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class miniJava_VarDeclaration:

    pass
class miniJava_MainMethod:

    pass
class miniJava_ClassDecl:

    def __init__(self, name: str, miniJava_ClassDecl: "miniJava_Program" = None, miniJava_ClassDecl2: "miniJava_MainMethod" = None, miniJava_ClassDecl5: "miniJava_ClassDecl" = None, miniJava_ClassDecl3: "miniJava_ClassDecl" = None, miniJava_ClassDecl7: set["miniJava_VarDeclaration"] = None, miniJava_ClassDecl9: set["miniJava_Method"] = None, miniJava_ClassDecl13: "miniJava_Type" = None):
        self.name = name
        self.miniJava_ClassDecl = miniJava_ClassDecl
        self.miniJava_ClassDecl2 = miniJava_ClassDecl2
        self.miniJava_ClassDecl5 = miniJava_ClassDecl5
        self.miniJava_ClassDecl3 = miniJava_ClassDecl3
        self.miniJava_ClassDecl7 = miniJava_ClassDecl7 if miniJava_ClassDecl7 is not None else set()
        self.miniJava_ClassDecl9 = miniJava_ClassDecl9 if miniJava_ClassDecl9 is not None else set()
        self.miniJava_ClassDecl13 = miniJava_ClassDecl13
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def miniJava_ClassDecl(self):
        return self.__miniJava_ClassDecl

    @miniJava_ClassDecl.setter
    def miniJava_ClassDecl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_ClassDecl__miniJava_ClassDecl", None)
        self.__miniJava_ClassDecl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Program"):
                opp_val = getattr(old_value, "miniJava_Program", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Program"):
                opp_val = getattr(value, "miniJava_Program", None)
                if opp_val is None:
                    setattr(value, "miniJava_Program", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def miniJava_ClassDecl9(self):
        return self.__miniJava_ClassDecl9

    @miniJava_ClassDecl9.setter
    def miniJava_ClassDecl9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_ClassDecl__miniJava_ClassDecl9", None)
        self.__miniJava_ClassDecl9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "miniJava_Method"):
                    opp_val = getattr(item, "miniJava_Method", None)
                    
                    if opp_val == self:
                        setattr(item, "miniJava_Method", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "miniJava_Method"):
                    opp_val = getattr(item, "miniJava_Method", None)
                    
                    setattr(item, "miniJava_Method", self)
                    

    @property
    def miniJava_ClassDecl3(self):
        return self.__miniJava_ClassDecl3

    @miniJava_ClassDecl3.setter
    def miniJava_ClassDecl3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_ClassDecl__miniJava_ClassDecl3", None)
        self.__miniJava_ClassDecl3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_ClassDecl5"):
                opp_val = getattr(old_value, "miniJava_ClassDecl5", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_ClassDecl5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_ClassDecl5"):
                opp_val = getattr(value, "miniJava_ClassDecl5", None)
                setattr(value, "miniJava_ClassDecl5", self)

    @property
    def miniJava_ClassDecl13(self):
        return self.__miniJava_ClassDecl13

    @miniJava_ClassDecl13.setter
    def miniJava_ClassDecl13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_ClassDecl__miniJava_ClassDecl13", None)
        self.__miniJava_ClassDecl13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_Type"):
                opp_val = getattr(old_value, "miniJava_Type", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_Type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_Type"):
                opp_val = getattr(value, "miniJava_Type", None)
                setattr(value, "miniJava_Type", self)

    @property
    def miniJava_ClassDecl7(self):
        return self.__miniJava_ClassDecl7

    @miniJava_ClassDecl7.setter
    def miniJava_ClassDecl7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_ClassDecl__miniJava_ClassDecl7", None)
        self.__miniJava_ClassDecl7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "miniJava_VarDeclaration"):
                    opp_val = getattr(item, "miniJava_VarDeclaration", None)
                    
                    if opp_val == self:
                        setattr(item, "miniJava_VarDeclaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "miniJava_VarDeclaration"):
                    opp_val = getattr(item, "miniJava_VarDeclaration", None)
                    
                    setattr(item, "miniJava_VarDeclaration", self)
                    

    @property
    def miniJava_ClassDecl5(self):
        return self.__miniJava_ClassDecl5

    @miniJava_ClassDecl5.setter
    def miniJava_ClassDecl5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_ClassDecl__miniJava_ClassDecl5", None)
        self.__miniJava_ClassDecl5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_ClassDecl3"):
                opp_val = getattr(old_value, "miniJava_ClassDecl3", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_ClassDecl3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_ClassDecl3"):
                opp_val = getattr(value, "miniJava_ClassDecl3", None)
                setattr(value, "miniJava_ClassDecl3", self)

    @property
    def miniJava_ClassDecl2(self):
        return self.__miniJava_ClassDecl2

    @miniJava_ClassDecl2.setter
    def miniJava_ClassDecl2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_miniJava_ClassDecl__miniJava_ClassDecl2", None)
        self.__miniJava_ClassDecl2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "miniJava_MainMethod"):
                opp_val = getattr(old_value, "miniJava_MainMethod", None)
                if opp_val == self:
                    setattr(old_value, "miniJava_MainMethod", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "miniJava_MainMethod"):
                opp_val = getattr(value, "miniJava_MainMethod", None)
                setattr(value, "miniJava_MainMethod", self)

class miniJava_Program:

    pass