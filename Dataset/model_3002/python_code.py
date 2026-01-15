from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class RangeLiteral:

    pass
class amethyst_CharRangeLiteral(RangeLiteral):

    pass
class amethyst_NumberRangeLiteral(RangeLiteral):

    pass
class Symbol:

    pass
class amethyst_DefinitionDeclaration(Symbol):

    def __init__(self, static: bool, amethyst_DefinitionDeclaration36: set["amethyst_Statement"] = None, amethyst_DefinitionDeclaration: set["amethyst_Symbol"] = None, amethyst_DefinitionDeclaration33: "amethyst_AbstractType" = None):
        self.static = static
        self.amethyst_DefinitionDeclaration36 = amethyst_DefinitionDeclaration36 if amethyst_DefinitionDeclaration36 is not None else set()
        self.amethyst_DefinitionDeclaration = amethyst_DefinitionDeclaration if amethyst_DefinitionDeclaration is not None else set()
        self.amethyst_DefinitionDeclaration33 = amethyst_DefinitionDeclaration33
        
    @property
    def static(self) -> bool:
        return self.__static

    @static.setter
    def static(self, static: bool):
        self.__static = static

    @property
    def amethyst_DefinitionDeclaration33(self):
        return self.__amethyst_DefinitionDeclaration33

    @amethyst_DefinitionDeclaration33.setter
    def amethyst_DefinitionDeclaration33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_amethyst_DefinitionDeclaration__amethyst_DefinitionDeclaration33", None)
        self.__amethyst_DefinitionDeclaration33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "amethyst_AbstractType34"):
                opp_val = getattr(old_value, "amethyst_AbstractType34", None)
                if opp_val == self:
                    setattr(old_value, "amethyst_AbstractType34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "amethyst_AbstractType34"):
                opp_val = getattr(value, "amethyst_AbstractType34", None)
                setattr(value, "amethyst_AbstractType34", self)

    @property
    def amethyst_DefinitionDeclaration(self):
        return self.__amethyst_DefinitionDeclaration

    @amethyst_DefinitionDeclaration.setter
    def amethyst_DefinitionDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_amethyst_DefinitionDeclaration__amethyst_DefinitionDeclaration", None)
        self.__amethyst_DefinitionDeclaration = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "amethyst_Symbol31"):
                    opp_val = getattr(item, "amethyst_Symbol31", None)
                    
                    if opp_val == self:
                        setattr(item, "amethyst_Symbol31", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "amethyst_Symbol31"):
                    opp_val = getattr(item, "amethyst_Symbol31", None)
                    
                    setattr(item, "amethyst_Symbol31", self)
                    

    @property
    def amethyst_DefinitionDeclaration36(self):
        return self.__amethyst_DefinitionDeclaration36

    @amethyst_DefinitionDeclaration36.setter
    def amethyst_DefinitionDeclaration36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_amethyst_DefinitionDeclaration__amethyst_DefinitionDeclaration36", None)
        self.__amethyst_DefinitionDeclaration36 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "amethyst_Statement37"):
                    opp_val = getattr(item, "amethyst_Statement37", None)
                    
                    if opp_val == self:
                        setattr(item, "amethyst_Statement37", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "amethyst_Statement37"):
                    opp_val = getattr(item, "amethyst_Statement37", None)
                    
                    setattr(item, "amethyst_Statement37", self)
                    

class amethyst_TagLoopInitializerDeclaration(Symbol):

    pass
class amethyst_ForInitializerDeclaration(Symbol):

    pass
class amethyst_ParameterDeclaration(Symbol):

    pass
class amethyst_VariableDeclaration(Symbol):

    pass
class amethyst_ClassDeclaration(Symbol):

    pass
class PrimitiveType:

    pass
class amethyst_DefinitionType(PrimitiveType):

    pass
class amethyst_IntType(PrimitiveType):

    pass
class amethyst_AnyType(PrimitiveType):

    pass
class amethyst_StringType(PrimitiveType):

    pass
class amethyst_BooleanType(PrimitiveType):

    pass
class amethyst_FloatType(PrimitiveType):

    pass
class amethyst_CharType(PrimitiveType):

    pass
class Type:

    pass
class amethyst_PrimitiveType(Type):

    pass
class amethyst_AbstractType:

    pass
class Literal:

    pass
class amethyst_NullLiteral(Literal):

    pass
class amethyst_IntLiteral(Literal):

    def __init__(self, value: int, amethyst_IntLiteral: "amethyst_NumberRangeLiteral" = None, amethyst_IntLiteral190: "amethyst_NumberRangeLiteral" = None):
        self.value = value
        self.amethyst_IntLiteral = amethyst_IntLiteral
        self.amethyst_IntLiteral190 = amethyst_IntLiteral190
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def amethyst_IntLiteral190(self):
        return self.__amethyst_IntLiteral190

    @amethyst_IntLiteral190.setter
    def amethyst_IntLiteral190(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_amethyst_IntLiteral__amethyst_IntLiteral190", None)
        self.__amethyst_IntLiteral190 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "amethyst_NumberRangeLiteral189"):
                opp_val = getattr(old_value, "amethyst_NumberRangeLiteral189", None)
                if opp_val == self:
                    setattr(old_value, "amethyst_NumberRangeLiteral189", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "amethyst_NumberRangeLiteral189"):
                opp_val = getattr(value, "amethyst_NumberRangeLiteral189", None)
                setattr(value, "amethyst_NumberRangeLiteral189", self)

    @property
    def amethyst_IntLiteral(self):
        return self.__amethyst_IntLiteral

    @amethyst_IntLiteral.setter
    def amethyst_IntLiteral(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_amethyst_IntLiteral__amethyst_IntLiteral", None)
        self.__amethyst_IntLiteral = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "amethyst_NumberRangeLiteral"):
                opp_val = getattr(old_value, "amethyst_NumberRangeLiteral", None)
                if opp_val == self:
                    setattr(old_value, "amethyst_NumberRangeLiteral", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "amethyst_NumberRangeLiteral"):
                opp_val = getattr(value, "amethyst_NumberRangeLiteral", None)
                setattr(value, "amethyst_NumberRangeLiteral", self)

class amethyst_RangeLiteral(Literal):

    pass
class amethyst_StringLiteral(Literal):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class amethyst_BooleanLiteral(Literal):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class amethyst_FloatLiteral(Literal):

    def __init__(self, value: float):
        self.value = value
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

class amethyst_CharLiteral(Literal):

    def __init__(self, value: str, amethyst_CharLiteral: "amethyst_CharRangeLiteral" = None, amethyst_CharLiteral194: "amethyst_CharRangeLiteral" = None):
        self.value = value
        self.amethyst_CharLiteral = amethyst_CharLiteral
        self.amethyst_CharLiteral194 = amethyst_CharLiteral194
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def amethyst_CharLiteral(self):
        return self.__amethyst_CharLiteral

    @amethyst_CharLiteral.setter
    def amethyst_CharLiteral(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_amethyst_CharLiteral__amethyst_CharLiteral", None)
        self.__amethyst_CharLiteral = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "amethyst_CharRangeLiteral"):
                opp_val = getattr(old_value, "amethyst_CharRangeLiteral", None)
                if opp_val == self:
                    setattr(old_value, "amethyst_CharRangeLiteral", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "amethyst_CharRangeLiteral"):
                opp_val = getattr(value, "amethyst_CharRangeLiteral", None)
                setattr(value, "amethyst_CharRangeLiteral", self)

    @property
    def amethyst_CharLiteral194(self):
        return self.__amethyst_CharLiteral194

    @amethyst_CharLiteral194.setter
    def amethyst_CharLiteral194(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_amethyst_CharLiteral__amethyst_CharLiteral194", None)
        self.__amethyst_CharLiteral194 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "amethyst_CharRangeLiteral193"):
                opp_val = getattr(old_value, "amethyst_CharRangeLiteral193", None)
                if opp_val == self:
                    setattr(old_value, "amethyst_CharRangeLiteral193", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "amethyst_CharRangeLiteral193"):
                opp_val = getattr(value, "amethyst_CharRangeLiteral193", None)
                setattr(value, "amethyst_CharRangeLiteral193", self)

class Expression:

    pass
class amethyst_TypeCastExpression(Expression):

    pass
class amethyst_InExpression(Expression):

    pass
class amethyst_CallExpression(Expression):

    pass
class amethyst_MatchingExpression(Expression):

    def __init__(self, operator: str, amethyst_MatchingExpression: "amethyst_Expression" = None, amethyst_MatchingExpression164: "amethyst_Expression" = None):
        self.operator = operator
        self.amethyst_MatchingExpression = amethyst_MatchingExpression
        self.amethyst_MatchingExpression164 = amethyst_MatchingExpression164
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def amethyst_MatchingExpression(self):
        return self.__amethyst_MatchingExpression

    @amethyst_MatchingExpression.setter
    def amethyst_MatchingExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_amethyst_MatchingExpression__amethyst_MatchingExpression", None)
        self.__amethyst_MatchingExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "amethyst_Expression162"):
                opp_val = getattr(old_value, "amethyst_Expression162", None)
                if opp_val == self:
                    setattr(old_value, "amethyst_Expression162", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "amethyst_Expression162"):
                opp_val = getattr(value, "amethyst_Expression162", None)
                setattr(value, "amethyst_Expression162", self)

    @property
    def amethyst_MatchingExpression164(self):
        return self.__amethyst_MatchingExpression164

    @amethyst_MatchingExpression164.setter
    def amethyst_MatchingExpression164(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_amethyst_MatchingExpression__amethyst_MatchingExpression164", None)
        self.__amethyst_MatchingExpression164 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "amethyst_Expression165"):
                opp_val = getattr(old_value, "amethyst_Expression165", None)
                if opp_val == self:
                    setattr(old_value, "amethyst_Expression165", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "amethyst_Expression165"):
                opp_val = getattr(value, "amethyst_Expression165", None)
                setattr(value, "amethyst_Expression165", self)

class amethyst_ShiftExpression(Expression):

    def __init__(self, operator: str, amethyst_ShiftExpression: "amethyst_Expression" = None, amethyst_ShiftExpression149: "amethyst_Expression" = None):
        self.operator = operator
        self.amethyst_ShiftExpression = amethyst_ShiftExpression
        self.amethyst_ShiftExpression149 = amethyst_ShiftExpression149
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def amethyst_ShiftExpression(self):
        return self.__amethyst_ShiftExpression

    @amethyst_ShiftExpression.setter
    def amethyst_ShiftExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_amethyst_ShiftExpression__amethyst_ShiftExpression", None)
        self.__amethyst_ShiftExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "amethyst_Expression147"):
                opp_val = getattr(old_value, "amethyst_Expression147", None)
                if opp_val == self:
                    setattr(old_value, "amethyst_Expression147", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "amethyst_Expression147"):
                opp_val = getattr(value, "amethyst_Expression147", None)
                setattr(value, "amethyst_Expression147", self)

    @property
    def amethyst_ShiftExpression149(self):
        return self.__amethyst_ShiftExpression149

    @amethyst_ShiftExpression149.setter
    def amethyst_ShiftExpression149(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_amethyst_ShiftExpression__amethyst_ShiftExpression149", None)
        self.__amethyst_ShiftExpression149 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "amethyst_Expression150"):
                opp_val = getattr(old_value, "amethyst_Expression150", None)
                if opp_val == self:
                    setattr(old_value, "amethyst_Expression150", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "amethyst_Expression150"):
                opp_val = getattr(value, "amethyst_Expression150", None)
                setattr(value, "amethyst_Expression150", self)

class amethyst_SelfExpression(Expression):

    pass
class amethyst_NewExpression(Expression):

    pass
class amethyst_IndexAccessExpression(Expression):

    pass
class amethyst_NotExpression(Expression):

    pass
class amethyst_AssignmentExpression(Expression):

    pass
class amethyst_Literal(Expression):

    pass
class amethyst_AndExpression(Expression):

    pass
class amethyst_SuperExpression(Expression):

    pass
class amethyst_UnaryMinusExpression(Expression):

    pass
class amethyst_OrExpression(Expression):

    pass
class amethyst_EqualityExpression(Expression):

    def __init__(self, operator: str, amethyst_EqualityExpression144: "amethyst_Expression" = None, amethyst_EqualityExpression: "amethyst_Expression" = None):
        self.operator = operator
        self.amethyst_EqualityExpression144 = amethyst_EqualityExpression144
        self.amethyst_EqualityExpression = amethyst_EqualityExpression
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def amethyst_EqualityExpression(self):
        return self.__amethyst_EqualityExpression

    @amethyst_EqualityExpression.setter
    def amethyst_EqualityExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_amethyst_EqualityExpression__amethyst_EqualityExpression", None)
        self.__amethyst_EqualityExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "amethyst_Expression142"):
                opp_val = getattr(old_value, "amethyst_Expression142", None)
                if opp_val == self:
                    setattr(old_value, "amethyst_Expression142", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "amethyst_Expression142"):
                opp_val = getattr(value, "amethyst_Expression142", None)
                setattr(value, "amethyst_Expression142", self)

    @property
    def amethyst_EqualityExpression144(self):
        return self.__amethyst_EqualityExpression144

    @amethyst_EqualityExpression144.setter
    def amethyst_EqualityExpression144(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_amethyst_EqualityExpression__amethyst_EqualityExpression144", None)
        self.__amethyst_EqualityExpression144 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "amethyst_Expression145"):
                opp_val = getattr(old_value, "amethyst_Expression145", None)
                if opp_val == self:
                    setattr(old_value, "amethyst_Expression145", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "amethyst_Expression145"):
                opp_val = getattr(value, "amethyst_Expression145", None)
                setattr(value, "amethyst_Expression145", self)

class amethyst_AdditiveExpression(Expression):

    def __init__(self, operator: str, amethyst_AdditiveExpression: "amethyst_Expression" = None, amethyst_AdditiveExpression154: "amethyst_Expression" = None):
        self.operator = operator
        self.amethyst_AdditiveExpression = amethyst_AdditiveExpression
        self.amethyst_AdditiveExpression154 = amethyst_AdditiveExpression154
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def amethyst_AdditiveExpression154(self):
        return self.__amethyst_AdditiveExpression154

    @amethyst_AdditiveExpression154.setter
    def amethyst_AdditiveExpression154(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_amethyst_AdditiveExpression__amethyst_AdditiveExpression154", None)
        self.__amethyst_AdditiveExpression154 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "amethyst_Expression155"):
                opp_val = getattr(old_value, "amethyst_Expression155", None)
                if opp_val == self:
                    setattr(old_value, "amethyst_Expression155", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "amethyst_Expression155"):
                opp_val = getattr(value, "amethyst_Expression155", None)
                setattr(value, "amethyst_Expression155", self)

    @property
    def amethyst_AdditiveExpression(self):
        return self.__amethyst_AdditiveExpression

    @amethyst_AdditiveExpression.setter
    def amethyst_AdditiveExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_amethyst_AdditiveExpression__amethyst_AdditiveExpression", None)
        self.__amethyst_AdditiveExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "amethyst_Expression152"):
                opp_val = getattr(old_value, "amethyst_Expression152", None)
                if opp_val == self:
                    setattr(old_value, "amethyst_Expression152", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "amethyst_Expression152"):
                opp_val = getattr(value, "amethyst_Expression152", None)
                setattr(value, "amethyst_Expression152", self)

class amethyst_MemberAccessExpression(Expression):

    pass
class amethyst_RelationalExpression(Expression):

    def __init__(self, operator: str, amethyst_RelationalExpression: "amethyst_Expression" = None, amethyst_RelationalExpression139: "amethyst_Expression" = None):
        self.operator = operator
        self.amethyst_RelationalExpression = amethyst_RelationalExpression
        self.amethyst_RelationalExpression139 = amethyst_RelationalExpression139
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def amethyst_RelationalExpression139(self):
        return self.__amethyst_RelationalExpression139

    @amethyst_RelationalExpression139.setter
    def amethyst_RelationalExpression139(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_amethyst_RelationalExpression__amethyst_RelationalExpression139", None)
        self.__amethyst_RelationalExpression139 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "amethyst_Expression140"):
                opp_val = getattr(old_value, "amethyst_Expression140", None)
                if opp_val == self:
                    setattr(old_value, "amethyst_Expression140", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "amethyst_Expression140"):
                opp_val = getattr(value, "amethyst_Expression140", None)
                setattr(value, "amethyst_Expression140", self)

    @property
    def amethyst_RelationalExpression(self):
        return self.__amethyst_RelationalExpression

    @amethyst_RelationalExpression.setter
    def amethyst_RelationalExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_amethyst_RelationalExpression__amethyst_RelationalExpression", None)
        self.__amethyst_RelationalExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "amethyst_Expression137"):
                opp_val = getattr(old_value, "amethyst_Expression137", None)
                if opp_val == self:
                    setattr(old_value, "amethyst_Expression137", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "amethyst_Expression137"):
                opp_val = getattr(value, "amethyst_Expression137", None)
                setattr(value, "amethyst_Expression137", self)

class amethyst_ParenthisedExpression(Expression):

    pass
class amethyst_MultiplicativeExpression(Expression):

    def __init__(self, operator: str, amethyst_MultiplicativeExpression: "amethyst_Expression" = None, amethyst_MultiplicativeExpression159: "amethyst_Expression" = None):
        self.operator = operator
        self.amethyst_MultiplicativeExpression = amethyst_MultiplicativeExpression
        self.amethyst_MultiplicativeExpression159 = amethyst_MultiplicativeExpression159
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def amethyst_MultiplicativeExpression159(self):
        return self.__amethyst_MultiplicativeExpression159

    @amethyst_MultiplicativeExpression159.setter
    def amethyst_MultiplicativeExpression159(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_amethyst_MultiplicativeExpression__amethyst_MultiplicativeExpression159", None)
        self.__amethyst_MultiplicativeExpression159 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "amethyst_Expression160"):
                opp_val = getattr(old_value, "amethyst_Expression160", None)
                if opp_val == self:
                    setattr(old_value, "amethyst_Expression160", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "amethyst_Expression160"):
                opp_val = getattr(value, "amethyst_Expression160", None)
                setattr(value, "amethyst_Expression160", self)

    @property
    def amethyst_MultiplicativeExpression(self):
        return self.__amethyst_MultiplicativeExpression

    @amethyst_MultiplicativeExpression.setter
    def amethyst_MultiplicativeExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_amethyst_MultiplicativeExpression__amethyst_MultiplicativeExpression", None)
        self.__amethyst_MultiplicativeExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "amethyst_Expression157"):
                opp_val = getattr(old_value, "amethyst_Expression157", None)
                if opp_val == self:
                    setattr(old_value, "amethyst_Expression157", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "amethyst_Expression157"):
                opp_val = getattr(value, "amethyst_Expression157", None)
                setattr(value, "amethyst_Expression157", self)

class amethyst_SymbolReference(Expression):

    pass
class amethyst_PropertyDeclaration(Symbol):

    pass
class AbstractType:

    pass
class amethyst_Type(AbstractType):

    pass
class amethyst_ArrayType(AbstractType):

    pass
class amethyst_TagExpression:

    pass
class amethyst_EObject:

    pass
class amethyst_TagAttribute:

    pass
class amethyst_TagLoopExpression:

    pass
class amethyst_ClassType(Type):

    pass
class amethyst_TagDeclaration:

    pass
class Statement:

    pass
class amethyst_CaseStatement(Statement):

    pass
class amethyst_Expression(Statement):

    pass
class amethyst_WhenStatement(Statement):

    pass
class amethyst_WhileStatement(Statement):

    pass
class amethyst_ElseStatement(Statement):

    pass
class amethyst_JsCodeStatement(Statement):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class amethyst_ElseIfStatement(Statement):

    pass
class amethyst_ReturnStatement(Statement):

    pass
class amethyst_IfStatement(Statement):

    pass
class amethyst_NextStatement(Statement):

    pass
class amethyst_ForStatement(Statement):

    pass
class amethyst_CaseElseStatement(Statement):

    pass
class amethyst_BreakStatement(Statement):

    pass
class amethyst_Symbol(Statement):

    def __init__(self, name: str, amethyst_Symbol: "amethyst_TagLoopExpression" = None, amethyst_Symbol22: "amethyst_SymbolReference" = None, amethyst_Symbol31: "amethyst_DefinitionDeclaration" = None, amethyst_Symbol45: "amethyst_ClassDeclaration" = None, amethyst_Symbol48: "amethyst_ClassDeclaration" = None, amethyst_Symbol97: "amethyst_ForStatement" = None, amethyst_Symbol125: "amethyst_MemberAccessExpression" = None):
        self.name = name
        self.amethyst_Symbol = amethyst_Symbol
        self.amethyst_Symbol22 = amethyst_Symbol22
        self.amethyst_Symbol31 = amethyst_Symbol31
        self.amethyst_Symbol45 = amethyst_Symbol45
        self.amethyst_Symbol48 = amethyst_Symbol48
        self.amethyst_Symbol97 = amethyst_Symbol97
        self.amethyst_Symbol125 = amethyst_Symbol125
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def amethyst_Symbol(self):
        return self.__amethyst_Symbol

    @amethyst_Symbol.setter
    def amethyst_Symbol(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_amethyst_Symbol__amethyst_Symbol", None)
        self.__amethyst_Symbol = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "amethyst_TagLoopExpression11"):
                opp_val = getattr(old_value, "amethyst_TagLoopExpression11", None)
                if opp_val == self:
                    setattr(old_value, "amethyst_TagLoopExpression11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "amethyst_TagLoopExpression11"):
                opp_val = getattr(value, "amethyst_TagLoopExpression11", None)
                setattr(value, "amethyst_TagLoopExpression11", self)

    @property
    def amethyst_Symbol48(self):
        return self.__amethyst_Symbol48

    @amethyst_Symbol48.setter
    def amethyst_Symbol48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_amethyst_Symbol__amethyst_Symbol48", None)
        self.__amethyst_Symbol48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "amethyst_ClassDeclaration47"):
                opp_val = getattr(old_value, "amethyst_ClassDeclaration47", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "amethyst_ClassDeclaration47"):
                opp_val = getattr(value, "amethyst_ClassDeclaration47", None)
                if opp_val is None:
                    setattr(value, "amethyst_ClassDeclaration47", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def amethyst_Symbol31(self):
        return self.__amethyst_Symbol31

    @amethyst_Symbol31.setter
    def amethyst_Symbol31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_amethyst_Symbol__amethyst_Symbol31", None)
        self.__amethyst_Symbol31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "amethyst_DefinitionDeclaration"):
                opp_val = getattr(old_value, "amethyst_DefinitionDeclaration", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "amethyst_DefinitionDeclaration"):
                opp_val = getattr(value, "amethyst_DefinitionDeclaration", None)
                if opp_val is None:
                    setattr(value, "amethyst_DefinitionDeclaration", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def amethyst_Symbol22(self):
        return self.__amethyst_Symbol22

    @amethyst_Symbol22.setter
    def amethyst_Symbol22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_amethyst_Symbol__amethyst_Symbol22", None)
        self.__amethyst_Symbol22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "amethyst_SymbolReference"):
                opp_val = getattr(old_value, "amethyst_SymbolReference", None)
                if opp_val == self:
                    setattr(old_value, "amethyst_SymbolReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "amethyst_SymbolReference"):
                opp_val = getattr(value, "amethyst_SymbolReference", None)
                setattr(value, "amethyst_SymbolReference", self)

    @property
    def amethyst_Symbol45(self):
        return self.__amethyst_Symbol45

    @amethyst_Symbol45.setter
    def amethyst_Symbol45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_amethyst_Symbol__amethyst_Symbol45", None)
        self.__amethyst_Symbol45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "amethyst_ClassDeclaration44"):
                opp_val = getattr(old_value, "amethyst_ClassDeclaration44", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "amethyst_ClassDeclaration44"):
                opp_val = getattr(value, "amethyst_ClassDeclaration44", None)
                if opp_val is None:
                    setattr(value, "amethyst_ClassDeclaration44", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def amethyst_Symbol97(self):
        return self.__amethyst_Symbol97

    @amethyst_Symbol97.setter
    def amethyst_Symbol97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_amethyst_Symbol__amethyst_Symbol97", None)
        self.__amethyst_Symbol97 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "amethyst_ForStatement"):
                opp_val = getattr(old_value, "amethyst_ForStatement", None)
                if opp_val == self:
                    setattr(old_value, "amethyst_ForStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "amethyst_ForStatement"):
                opp_val = getattr(value, "amethyst_ForStatement", None)
                setattr(value, "amethyst_ForStatement", self)

    @property
    def amethyst_Symbol125(self):
        return self.__amethyst_Symbol125

    @amethyst_Symbol125.setter
    def amethyst_Symbol125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_amethyst_Symbol__amethyst_Symbol125", None)
        self.__amethyst_Symbol125 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "amethyst_MemberAccessExpression124"):
                opp_val = getattr(old_value, "amethyst_MemberAccessExpression124", None)
                if opp_val == self:
                    setattr(old_value, "amethyst_MemberAccessExpression124", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "amethyst_MemberAccessExpression124"):
                opp_val = getattr(value, "amethyst_MemberAccessExpression124", None)
                setattr(value, "amethyst_MemberAccessExpression124", self)

class amethyst_Statement:

    pass
class amethyst_Import:

    def __init__(self, importedNamespace: str, amethyst_Import: "amethyst_Module" = None):
        self.importedNamespace = importedNamespace
        self.amethyst_Import = amethyst_Import
        
    @property
    def importedNamespace(self) -> str:
        return self.__importedNamespace

    @importedNamespace.setter
    def importedNamespace(self, importedNamespace: str):
        self.__importedNamespace = importedNamespace

    @property
    def amethyst_Import(self):
        return self.__amethyst_Import

    @amethyst_Import.setter
    def amethyst_Import(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_amethyst_Import__amethyst_Import", None)
        self.__amethyst_Import = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "amethyst_Module"):
                opp_val = getattr(old_value, "amethyst_Module", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "amethyst_Module"):
                opp_val = getattr(value, "amethyst_Module", None)
                if opp_val is None:
                    setattr(value, "amethyst_Module", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class amethyst_Module:

    def __init__(self, name: str, amethyst_Module: set["amethyst_Import"] = None, amethyst_Module2: set["amethyst_Statement"] = None):
        self.name = name
        self.amethyst_Module = amethyst_Module if amethyst_Module is not None else set()
        self.amethyst_Module2 = amethyst_Module2 if amethyst_Module2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def amethyst_Module(self):
        return self.__amethyst_Module

    @amethyst_Module.setter
    def amethyst_Module(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_amethyst_Module__amethyst_Module", None)
        self.__amethyst_Module = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "amethyst_Import"):
                    opp_val = getattr(item, "amethyst_Import", None)
                    
                    if opp_val == self:
                        setattr(item, "amethyst_Import", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "amethyst_Import"):
                    opp_val = getattr(item, "amethyst_Import", None)
                    
                    setattr(item, "amethyst_Import", self)
                    

    @property
    def amethyst_Module2(self):
        return self.__amethyst_Module2

    @amethyst_Module2.setter
    def amethyst_Module2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_amethyst_Module__amethyst_Module2", None)
        self.__amethyst_Module2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "amethyst_Statement"):
                    opp_val = getattr(item, "amethyst_Statement", None)
                    
                    if opp_val == self:
                        setattr(item, "amethyst_Statement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "amethyst_Statement"):
                    opp_val = getattr(item, "amethyst_Statement", None)
                    
                    setattr(item, "amethyst_Statement", self)
                    
