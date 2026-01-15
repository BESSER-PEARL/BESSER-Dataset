from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class AssignmentStatement:

    pass
class dom_SpecialAssignmentStatement(AssignmentStatement):

    pass
class CollectionInitValue:

    pass
class dom_ExpRange(CollectionInitValue):

    pass
class dom_ExprList(CollectionInitValue):

    pass
class dom_ShortModelDeclarationExpression:

    pass
class NameExpression:

    pass
class dom_ModelExpression(NameExpression):

    pass
class dom_SpecialNameExpression(NameExpression):

    pass
class CollectionType:

    pass
class dom_SequenceType(CollectionType):

    pass
class dom_OrderedSetType(CollectionType):

    pass
class dom_BagType(CollectionType):

    pass
class dom_SetType(CollectionType):

    pass
class PrimitiveType:

    pass
class dom_StringType(PrimitiveType):

    pass
class dom_RealType(PrimitiveType):

    pass
class dom_IntegerType(PrimitiveType):

    pass
class dom_BooleanType(PrimitiveType):

    pass
class Type:

    pass
class dom_MapType(Type):

    pass
class dom_NativeType(Type):

    pass
class dom_PrimitiveType(Type):

    pass
class dom_ModelElementType(Type):

    pass
class dom_CollectionType(Type):

    pass
class dom_AnyType(Type):

    pass
class Annotation:

    pass
class dom_SimpleAnnotation(Annotation):

    pass
class dom_ExecutableAnnotation(Annotation):

    pass
class CollectionExpression:

    pass
class dom_BagExpression(CollectionExpression):

    pass
class dom_SetExpression(CollectionExpression):

    pass
class LiteralExpression:

    pass
class dom_CollectionExpression(LiteralExpression):

    pass
class dom_PrimitiveExpression(LiteralExpression):

    pass
class SwitchCaseStatement:

    pass
class dom_MapExpression(LiteralExpression):

    pass
class dom_OrderedSetExpression(CollectionExpression):

    pass
class dom_SequenceExpression(CollectionExpression):

    pass
class dom_SwitchCaseExpressionStatement(SwitchCaseStatement):

    pass
class dom_SwitchCaseDefaultStatement(SwitchCaseStatement):

    pass
class Statement:

    pass
class dom_ExpressionStatement(Statement):

    pass
class dom_ReturnStatement(Statement):

    pass
class dom_BreakStatement(Statement):

    pass
class dom_DeleteStatement(Statement):

    pass
class dom_WhileStatement(Statement):

    pass
class dom_SwitchStatement(Statement):

    pass
class dom_IfStatement(Statement):

    pass
class dom_TransactionStatement(Statement):

    pass
class dom_SwitchCaseStatement(Statement):

    pass
class dom_ThrowStatement(Statement):

    pass
class dom_BreakAllStatement(Statement):

    pass
class dom_AbortStatement(Statement):

    pass
class dom_ContinueStatement(Statement):

    pass
class dom_AssignmentStatement(Statement):

    pass
class dom_ForStatement(Statement):

    pass
class FeatureCallExpression:

    pass
class dom_FOLMethodCallExpression(FeatureCallExpression):

    pass
class dom_MethodCallExpression(FeatureCallExpression):

    pass
class dom_PropertyCallExpression(FeatureCallExpression):

    pass
class UnaryOperatorExpression:

    pass
class dom_NotOperatorExpression(UnaryOperatorExpression):

    pass
class dom_NegativeOperatorExpression(UnaryOperatorExpression):

    pass
class OperatorExpression:

    pass
class dom_UnaryOperatorExpression(OperatorExpression):

    pass
class dom_BinaryOperatorExpression(OperatorExpression):

    pass
class Expression:

    pass
class dom_NewExpression(Expression):

    pass
class dom_FeatureCallExpression(Expression):

    pass
class dom_ModelElementTypeExpression(Expression):

    pass
class dom_VariableDeclarationExpression(Expression):

    pass
class dom_FormalParameterExpression(Expression):

    pass
class dom_OperatorExpression(Expression):

    pass
class dom_ModelDeclarationStatement(Statement):

    pass
class dom_NameExpression(Expression):

    def __init__(self, name: str, dom_NameExpression22: "dom_EnumerationLiteralExpression" = None, dom_NameExpression: "dom_Program" = None, dom_NameExpression41: "dom_PropertyCallExpression" = None, dom_NameExpression25: "dom_EnumerationLiteralExpression" = None, dom_NameExpression28: "dom_EnumerationLiteralExpression" = None, dom_NameExpression37: "dom_MethodCallExpression" = None, dom_NameExpression66: "dom_OperationDefinition" = None, dom_NameExpression46: "dom_VariableDeclarationExpression" = None, dom_NameExpression125: "dom_FOLMethodCallExpression" = None, dom_NameExpression109: "dom_ModelDeclarationStatement" = None, dom_NameExpression112: "dom_ModelDeclarationStatement" = None, dom_NameExpression115: "dom_ModelDeclarationStatement" = None, dom_NameExpression137: "dom_Annotation" = None, dom_NameExpression159: "dom_ModelDeclarationParameter" = None, dom_NameExpression169: "dom_TransactionStatement" = None, dom_NameExpression172: "dom_FormalParameterExpression" = None, dom_NameExpression184: "dom_ModelElementTypeExpression" = None, dom_NameExpression187: "dom_ModelElementTypeExpression" = None):
        self.name = name
        self.dom_NameExpression22 = dom_NameExpression22
        self.dom_NameExpression = dom_NameExpression
        self.dom_NameExpression41 = dom_NameExpression41
        self.dom_NameExpression25 = dom_NameExpression25
        self.dom_NameExpression28 = dom_NameExpression28
        self.dom_NameExpression37 = dom_NameExpression37
        self.dom_NameExpression66 = dom_NameExpression66
        self.dom_NameExpression46 = dom_NameExpression46
        self.dom_NameExpression125 = dom_NameExpression125
        self.dom_NameExpression109 = dom_NameExpression109
        self.dom_NameExpression112 = dom_NameExpression112
        self.dom_NameExpression115 = dom_NameExpression115
        self.dom_NameExpression137 = dom_NameExpression137
        self.dom_NameExpression159 = dom_NameExpression159
        self.dom_NameExpression169 = dom_NameExpression169
        self.dom_NameExpression172 = dom_NameExpression172
        self.dom_NameExpression184 = dom_NameExpression184
        self.dom_NameExpression187 = dom_NameExpression187
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dom_NameExpression187(self):
        return self.__dom_NameExpression187

    @dom_NameExpression187.setter
    def dom_NameExpression187(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_NameExpression__dom_NameExpression187", None)
        self.__dom_NameExpression187 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_ModelElementTypeExpression186"):
                opp_val = getattr(old_value, "dom_ModelElementTypeExpression186", None)
                if opp_val == self:
                    setattr(old_value, "dom_ModelElementTypeExpression186", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_ModelElementTypeExpression186"):
                opp_val = getattr(value, "dom_ModelElementTypeExpression186", None)
                setattr(value, "dom_ModelElementTypeExpression186", self)

    @property
    def dom_NameExpression125(self):
        return self.__dom_NameExpression125

    @dom_NameExpression125.setter
    def dom_NameExpression125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_NameExpression__dom_NameExpression125", None)
        self.__dom_NameExpression125 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_FOLMethodCallExpression124"):
                opp_val = getattr(old_value, "dom_FOLMethodCallExpression124", None)
                if opp_val == self:
                    setattr(old_value, "dom_FOLMethodCallExpression124", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_FOLMethodCallExpression124"):
                opp_val = getattr(value, "dom_FOLMethodCallExpression124", None)
                setattr(value, "dom_FOLMethodCallExpression124", self)

    @property
    def dom_NameExpression28(self):
        return self.__dom_NameExpression28

    @dom_NameExpression28.setter
    def dom_NameExpression28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_NameExpression__dom_NameExpression28", None)
        self.__dom_NameExpression28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_EnumerationLiteralExpression27"):
                opp_val = getattr(old_value, "dom_EnumerationLiteralExpression27", None)
                if opp_val == self:
                    setattr(old_value, "dom_EnumerationLiteralExpression27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_EnumerationLiteralExpression27"):
                opp_val = getattr(value, "dom_EnumerationLiteralExpression27", None)
                setattr(value, "dom_EnumerationLiteralExpression27", self)

    @property
    def dom_NameExpression184(self):
        return self.__dom_NameExpression184

    @dom_NameExpression184.setter
    def dom_NameExpression184(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_NameExpression__dom_NameExpression184", None)
        self.__dom_NameExpression184 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_ModelElementTypeExpression183"):
                opp_val = getattr(old_value, "dom_ModelElementTypeExpression183", None)
                if opp_val == self:
                    setattr(old_value, "dom_ModelElementTypeExpression183", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_ModelElementTypeExpression183"):
                opp_val = getattr(value, "dom_ModelElementTypeExpression183", None)
                setattr(value, "dom_ModelElementTypeExpression183", self)

    @property
    def dom_NameExpression109(self):
        return self.__dom_NameExpression109

    @dom_NameExpression109.setter
    def dom_NameExpression109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_NameExpression__dom_NameExpression109", None)
        self.__dom_NameExpression109 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_ModelDeclarationStatement108"):
                opp_val = getattr(old_value, "dom_ModelDeclarationStatement108", None)
                if opp_val == self:
                    setattr(old_value, "dom_ModelDeclarationStatement108", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_ModelDeclarationStatement108"):
                opp_val = getattr(value, "dom_ModelDeclarationStatement108", None)
                setattr(value, "dom_ModelDeclarationStatement108", self)

    @property
    def dom_NameExpression169(self):
        return self.__dom_NameExpression169

    @dom_NameExpression169.setter
    def dom_NameExpression169(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_NameExpression__dom_NameExpression169", None)
        self.__dom_NameExpression169 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_TransactionStatement168"):
                opp_val = getattr(old_value, "dom_TransactionStatement168", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_TransactionStatement168"):
                opp_val = getattr(value, "dom_TransactionStatement168", None)
                if opp_val is None:
                    setattr(value, "dom_TransactionStatement168", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dom_NameExpression22(self):
        return self.__dom_NameExpression22

    @dom_NameExpression22.setter
    def dom_NameExpression22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_NameExpression__dom_NameExpression22", None)
        self.__dom_NameExpression22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_EnumerationLiteralExpression"):
                opp_val = getattr(old_value, "dom_EnumerationLiteralExpression", None)
                if opp_val == self:
                    setattr(old_value, "dom_EnumerationLiteralExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_EnumerationLiteralExpression"):
                opp_val = getattr(value, "dom_EnumerationLiteralExpression", None)
                setattr(value, "dom_EnumerationLiteralExpression", self)

    @property
    def dom_NameExpression46(self):
        return self.__dom_NameExpression46

    @dom_NameExpression46.setter
    def dom_NameExpression46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_NameExpression__dom_NameExpression46", None)
        self.__dom_NameExpression46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_VariableDeclarationExpression"):
                opp_val = getattr(old_value, "dom_VariableDeclarationExpression", None)
                if opp_val == self:
                    setattr(old_value, "dom_VariableDeclarationExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_VariableDeclarationExpression"):
                opp_val = getattr(value, "dom_VariableDeclarationExpression", None)
                setattr(value, "dom_VariableDeclarationExpression", self)

    @property
    def dom_NameExpression115(self):
        return self.__dom_NameExpression115

    @dom_NameExpression115.setter
    def dom_NameExpression115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_NameExpression__dom_NameExpression115", None)
        self.__dom_NameExpression115 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_ModelDeclarationStatement114"):
                opp_val = getattr(old_value, "dom_ModelDeclarationStatement114", None)
                if opp_val == self:
                    setattr(old_value, "dom_ModelDeclarationStatement114", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_ModelDeclarationStatement114"):
                opp_val = getattr(value, "dom_ModelDeclarationStatement114", None)
                setattr(value, "dom_ModelDeclarationStatement114", self)

    @property
    def dom_NameExpression159(self):
        return self.__dom_NameExpression159

    @dom_NameExpression159.setter
    def dom_NameExpression159(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_NameExpression__dom_NameExpression159", None)
        self.__dom_NameExpression159 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_ModelDeclarationParameter158"):
                opp_val = getattr(old_value, "dom_ModelDeclarationParameter158", None)
                if opp_val == self:
                    setattr(old_value, "dom_ModelDeclarationParameter158", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_ModelDeclarationParameter158"):
                opp_val = getattr(value, "dom_ModelDeclarationParameter158", None)
                setattr(value, "dom_ModelDeclarationParameter158", self)

    @property
    def dom_NameExpression172(self):
        return self.__dom_NameExpression172

    @dom_NameExpression172.setter
    def dom_NameExpression172(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_NameExpression__dom_NameExpression172", None)
        self.__dom_NameExpression172 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_FormalParameterExpression171"):
                opp_val = getattr(old_value, "dom_FormalParameterExpression171", None)
                if opp_val == self:
                    setattr(old_value, "dom_FormalParameterExpression171", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_FormalParameterExpression171"):
                opp_val = getattr(value, "dom_FormalParameterExpression171", None)
                setattr(value, "dom_FormalParameterExpression171", self)

    @property
    def dom_NameExpression25(self):
        return self.__dom_NameExpression25

    @dom_NameExpression25.setter
    def dom_NameExpression25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_NameExpression__dom_NameExpression25", None)
        self.__dom_NameExpression25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_EnumerationLiteralExpression24"):
                opp_val = getattr(old_value, "dom_EnumerationLiteralExpression24", None)
                if opp_val == self:
                    setattr(old_value, "dom_EnumerationLiteralExpression24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_EnumerationLiteralExpression24"):
                opp_val = getattr(value, "dom_EnumerationLiteralExpression24", None)
                setattr(value, "dom_EnumerationLiteralExpression24", self)

    @property
    def dom_NameExpression(self):
        return self.__dom_NameExpression

    @dom_NameExpression.setter
    def dom_NameExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_NameExpression__dom_NameExpression", None)
        self.__dom_NameExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Program8"):
                opp_val = getattr(old_value, "dom_Program8", None)
                if opp_val == self:
                    setattr(old_value, "dom_Program8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Program8"):
                opp_val = getattr(value, "dom_Program8", None)
                setattr(value, "dom_Program8", self)

    @property
    def dom_NameExpression112(self):
        return self.__dom_NameExpression112

    @dom_NameExpression112.setter
    def dom_NameExpression112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_NameExpression__dom_NameExpression112", None)
        self.__dom_NameExpression112 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_ModelDeclarationStatement111"):
                opp_val = getattr(old_value, "dom_ModelDeclarationStatement111", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_ModelDeclarationStatement111"):
                opp_val = getattr(value, "dom_ModelDeclarationStatement111", None)
                if opp_val is None:
                    setattr(value, "dom_ModelDeclarationStatement111", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dom_NameExpression137(self):
        return self.__dom_NameExpression137

    @dom_NameExpression137.setter
    def dom_NameExpression137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_NameExpression__dom_NameExpression137", None)
        self.__dom_NameExpression137 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Annotation"):
                opp_val = getattr(old_value, "dom_Annotation", None)
                if opp_val == self:
                    setattr(old_value, "dom_Annotation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Annotation"):
                opp_val = getattr(value, "dom_Annotation", None)
                setattr(value, "dom_Annotation", self)

    @property
    def dom_NameExpression66(self):
        return self.__dom_NameExpression66

    @dom_NameExpression66.setter
    def dom_NameExpression66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_NameExpression__dom_NameExpression66", None)
        self.__dom_NameExpression66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_OperationDefinition65"):
                opp_val = getattr(old_value, "dom_OperationDefinition65", None)
                if opp_val == self:
                    setattr(old_value, "dom_OperationDefinition65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_OperationDefinition65"):
                opp_val = getattr(value, "dom_OperationDefinition65", None)
                setattr(value, "dom_OperationDefinition65", self)

    @property
    def dom_NameExpression37(self):
        return self.__dom_NameExpression37

    @dom_NameExpression37.setter
    def dom_NameExpression37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_NameExpression__dom_NameExpression37", None)
        self.__dom_NameExpression37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_MethodCallExpression36"):
                opp_val = getattr(old_value, "dom_MethodCallExpression36", None)
                if opp_val == self:
                    setattr(old_value, "dom_MethodCallExpression36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_MethodCallExpression36"):
                opp_val = getattr(value, "dom_MethodCallExpression36", None)
                setattr(value, "dom_MethodCallExpression36", self)

    @property
    def dom_NameExpression41(self):
        return self.__dom_NameExpression41

    @dom_NameExpression41.setter
    def dom_NameExpression41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_NameExpression__dom_NameExpression41", None)
        self.__dom_NameExpression41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_PropertyCallExpression"):
                opp_val = getattr(old_value, "dom_PropertyCallExpression", None)
                if opp_val == self:
                    setattr(old_value, "dom_PropertyCallExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_PropertyCallExpression"):
                opp_val = getattr(value, "dom_PropertyCallExpression", None)
                setattr(value, "dom_PropertyCallExpression", self)

class dom_EnumerationLiteralExpression(Expression):

    pass
class PrimitiveExpression:

    pass
class dom_StringExpression(PrimitiveExpression):

    def __init__(self, val: str, dom_StringExpression: "dom_Import" = None, dom_StringExpression141: "dom_SimpleAnnotation" = None, dom_StringExpression162: "dom_ModelDeclarationParameter" = None, dom_StringExpression150: "dom_NativeType" = None):
        self.val = val
        self.dom_StringExpression = dom_StringExpression
        self.dom_StringExpression141 = dom_StringExpression141
        self.dom_StringExpression162 = dom_StringExpression162
        self.dom_StringExpression150 = dom_StringExpression150
        
    @property
    def val(self) -> str:
        return self.__val

    @val.setter
    def val(self, val: str):
        self.__val = val

    @property
    def dom_StringExpression162(self):
        return self.__dom_StringExpression162

    @dom_StringExpression162.setter
    def dom_StringExpression162(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_StringExpression__dom_StringExpression162", None)
        self.__dom_StringExpression162 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_ModelDeclarationParameter161"):
                opp_val = getattr(old_value, "dom_ModelDeclarationParameter161", None)
                if opp_val == self:
                    setattr(old_value, "dom_ModelDeclarationParameter161", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_ModelDeclarationParameter161"):
                opp_val = getattr(value, "dom_ModelDeclarationParameter161", None)
                setattr(value, "dom_ModelDeclarationParameter161", self)

    @property
    def dom_StringExpression(self):
        return self.__dom_StringExpression

    @dom_StringExpression.setter
    def dom_StringExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_StringExpression__dom_StringExpression", None)
        self.__dom_StringExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Import12"):
                opp_val = getattr(old_value, "dom_Import12", None)
                if opp_val == self:
                    setattr(old_value, "dom_Import12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Import12"):
                opp_val = getattr(value, "dom_Import12", None)
                setattr(value, "dom_Import12", self)

    @property
    def dom_StringExpression150(self):
        return self.__dom_StringExpression150

    @dom_StringExpression150.setter
    def dom_StringExpression150(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_StringExpression__dom_StringExpression150", None)
        self.__dom_StringExpression150 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_NativeType"):
                opp_val = getattr(old_value, "dom_NativeType", None)
                if opp_val == self:
                    setattr(old_value, "dom_NativeType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_NativeType"):
                opp_val = getattr(value, "dom_NativeType", None)
                setattr(value, "dom_NativeType", self)

    @property
    def dom_StringExpression141(self):
        return self.__dom_StringExpression141

    @dom_StringExpression141.setter
    def dom_StringExpression141(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_StringExpression__dom_StringExpression141", None)
        self.__dom_StringExpression141 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_SimpleAnnotation"):
                opp_val = getattr(old_value, "dom_SimpleAnnotation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_SimpleAnnotation"):
                opp_val = getattr(value, "dom_SimpleAnnotation", None)
                if opp_val is None:
                    setattr(value, "dom_SimpleAnnotation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dom_IntegerExpression(PrimitiveExpression):

    def __init__(self, val: int):
        self.val = val
        
    @property
    def val(self) -> int:
        return self.__val

    @val.setter
    def val(self, val: int):
        self.__val = val

class dom_RealExpression(PrimitiveExpression):

    def __init__(self, val: float):
        self.val = val
        
    @property
    def val(self) -> float:
        return self.__val

    @val.setter
    def val(self, val: float):
        self.__val = val

class dom_BooleanExpression(PrimitiveExpression):

    def __init__(self, val: bool, dom_BooleanExpression44: "dom_PropertyCallExpression" = None, dom_BooleanExpression: "dom_FeatureCallExpression" = None, dom_BooleanExpression49: "dom_VariableDeclarationExpression" = None):
        self.val = val
        self.dom_BooleanExpression44 = dom_BooleanExpression44
        self.dom_BooleanExpression = dom_BooleanExpression
        self.dom_BooleanExpression49 = dom_BooleanExpression49
        
    @property
    def val(self) -> bool:
        return self.__val

    @val.setter
    def val(self, val: bool):
        self.__val = val

    @property
    def dom_BooleanExpression(self):
        return self.__dom_BooleanExpression

    @dom_BooleanExpression.setter
    def dom_BooleanExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_BooleanExpression__dom_BooleanExpression", None)
        self.__dom_BooleanExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_FeatureCallExpression32"):
                opp_val = getattr(old_value, "dom_FeatureCallExpression32", None)
                if opp_val == self:
                    setattr(old_value, "dom_FeatureCallExpression32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_FeatureCallExpression32"):
                opp_val = getattr(value, "dom_FeatureCallExpression32", None)
                setattr(value, "dom_FeatureCallExpression32", self)

    @property
    def dom_BooleanExpression44(self):
        return self.__dom_BooleanExpression44

    @dom_BooleanExpression44.setter
    def dom_BooleanExpression44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_BooleanExpression__dom_BooleanExpression44", None)
        self.__dom_BooleanExpression44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_PropertyCallExpression43"):
                opp_val = getattr(old_value, "dom_PropertyCallExpression43", None)
                if opp_val == self:
                    setattr(old_value, "dom_PropertyCallExpression43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_PropertyCallExpression43"):
                opp_val = getattr(value, "dom_PropertyCallExpression43", None)
                setattr(value, "dom_PropertyCallExpression43", self)

    @property
    def dom_BooleanExpression49(self):
        return self.__dom_BooleanExpression49

    @dom_BooleanExpression49.setter
    def dom_BooleanExpression49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_BooleanExpression__dom_BooleanExpression49", None)
        self.__dom_BooleanExpression49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_VariableDeclarationExpression48"):
                opp_val = getattr(old_value, "dom_VariableDeclarationExpression48", None)
                if opp_val == self:
                    setattr(old_value, "dom_VariableDeclarationExpression48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_VariableDeclarationExpression48"):
                opp_val = getattr(value, "dom_VariableDeclarationExpression48", None)
                setattr(value, "dom_VariableDeclarationExpression48", self)

class dom_LiteralExpression(Expression):

    pass
class BinaryOperatorExpression:

    pass
class dom_NotEqualsOperatorExpression(BinaryOperatorExpression):

    pass
class dom_MinusOperatorExpression(BinaryOperatorExpression):

    pass
class dom_ImpliesOperatorExpression(BinaryOperatorExpression):

    pass
class dom_MultiplyOperatorExpression(BinaryOperatorExpression):

    pass
class dom_GreaterThanOrEqualToOperatorExpression(BinaryOperatorExpression):

    pass
class dom_PlusOperatorExpression(BinaryOperatorExpression):

    pass
class dom_GreaterThanOperatorExpression(BinaryOperatorExpression):

    pass
class dom_DivideOperatorExpression(BinaryOperatorExpression):

    pass
class dom_LessThanOperatorExpression(BinaryOperatorExpression):

    pass
class dom_LessThanOrEqualToOperatorExpression(BinaryOperatorExpression):

    pass
class dom_EqualsOperatorExpression(BinaryOperatorExpression):

    pass
class dom_OrOperatorExpression(BinaryOperatorExpression):

    pass
class dom_XorOperatorExpression(BinaryOperatorExpression):

    pass
class dom_AndOperatorExpression(BinaryOperatorExpression):

    pass
class dom_DomElement(ABC):

    def __init__(self, line: int, column: int, dom_DomElement: "dom_DomElement" = None, dom_DomElement0: "dom_DomElement" = None):
        self.line = line
        self.column = column
        self.dom_DomElement = dom_DomElement
        self.dom_DomElement0 = dom_DomElement0
        
    @property
    def column(self) -> int:
        return self.__column

    @column.setter
    def column(self, column: int):
        self.__column = column

    @property
    def line(self) -> int:
        return self.__line

    @line.setter
    def line(self, line: int):
        self.__line = line

    @property
    def dom_DomElement(self):
        return self.__dom_DomElement

    @dom_DomElement.setter
    def dom_DomElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_DomElement__dom_DomElement", None)
        self.__dom_DomElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_DomElement0"):
                opp_val = getattr(old_value, "dom_DomElement0", None)
                if opp_val == self:
                    setattr(old_value, "dom_DomElement0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_DomElement0"):
                opp_val = getattr(value, "dom_DomElement0", None)
                setattr(value, "dom_DomElement0", self)

    @property
    def dom_DomElement0(self):
        return self.__dom_DomElement0

    @dom_DomElement0.setter
    def dom_DomElement0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_DomElement__dom_DomElement0", None)
        self.__dom_DomElement0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_DomElement"):
                opp_val = getattr(old_value, "dom_DomElement", None)
                if opp_val == self:
                    setattr(old_value, "dom_DomElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_DomElement"):
                opp_val = getattr(value, "dom_DomElement", None)
                setattr(value, "dom_DomElement", self)

class DomElement:

    pass
class dom_Statement(DomElement):

    pass
class dom_Block(DomElement):

    pass
class dom_OperationDefinition(DomElement):

    pass
class dom_AnnotationBlock(DomElement):

    pass
class dom_KeyValue(DomElement):

    pass
class dom_ModelDeclarationParameter(DomElement):

    pass
class dom_Type(DomElement):

    pass
class dom_Expression(DomElement):

    pass
class dom_Import(DomElement):

    pass
class dom_Annotation(DomElement):

    pass
class dom_CollectionInitValue(DomElement):

    pass
class dom_Program(DomElement):

    pass