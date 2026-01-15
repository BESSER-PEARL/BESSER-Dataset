from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class BinaryOperatorExpression:

    pass
class eol_ComparisonOperatorExpression(BinaryOperatorExpression):

    pass
class eol_ArithmeticOperatorExpression(BinaryOperatorExpression):

    pass
class eol_LogicalOperatorExpression(BinaryOperatorExpression):

    pass
class PseudoType:

    pass
class eol_SelfContentType(PseudoType):

    pass
class eol_SelfType(PseudoType):

    pass
class eol_OperationArgType(PseudoType):

    pass
class AssignmentStatement:

    pass
class eol_SelfInnermostType(PseudoType):

    pass
class CollectionInitValue:

    pass
class eol_ExpRange(CollectionInitValue):

    pass
class eol_ExprList(CollectionInitValue):

    pass
class VariableDeclarationExpression:

    pass
class eol_SpecialAssignmentStatement(AssignmentStatement):

    pass
class eol_EClassifier:

    pass
class NameExpression:

    pass
class eol_SpecialNameExpression(NameExpression):

    pass
class Annotation:

    pass
class eol_ExecutableAnnotation(Annotation):

    pass
class eol_SimpleAnnotation(Annotation):

    pass
class Type:

    pass
class eol_EType(Type):

    pass
class eol_CollectionType(Type):

    pass
class eol_VoidType(Type):

    pass
class eol_ModelElementType(Type):

    def __init__(self, modelName: str, elementName: str, eol_ModelElementType: "eol_EClassifier" = None, eol_ModelElementType178: set["eol_ModelDeclarationStatement"] = None):
        self.modelName = modelName
        self.elementName = elementName
        self.eol_ModelElementType = eol_ModelElementType
        self.eol_ModelElementType178 = eol_ModelElementType178 if eol_ModelElementType178 is not None else set()
        
    @property
    def modelName(self) -> str:
        return self.__modelName

    @modelName.setter
    def modelName(self, modelName: str):
        self.__modelName = modelName

    @property
    def elementName(self) -> str:
        return self.__elementName

    @elementName.setter
    def elementName(self, elementName: str):
        self.__elementName = elementName

    @property
    def eol_ModelElementType178(self):
        return self.__eol_ModelElementType178

    @eol_ModelElementType178.setter
    def eol_ModelElementType178(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_ModelElementType__eol_ModelElementType178", None)
        self.__eol_ModelElementType178 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eol_ModelDeclarationStatement179"):
                    opp_val = getattr(item, "eol_ModelDeclarationStatement179", None)
                    
                    if opp_val == self:
                        setattr(item, "eol_ModelDeclarationStatement179", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eol_ModelDeclarationStatement179"):
                    opp_val = getattr(item, "eol_ModelDeclarationStatement179", None)
                    
                    setattr(item, "eol_ModelDeclarationStatement179", self)
                    

    @property
    def eol_ModelElementType(self):
        return self.__eol_ModelElementType

    @eol_ModelElementType.setter
    def eol_ModelElementType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_ModelElementType__eol_ModelElementType", None)
        self.__eol_ModelElementType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_EClassifier"):
                opp_val = getattr(old_value, "eol_EClassifier", None)
                if opp_val == self:
                    setattr(old_value, "eol_EClassifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_EClassifier"):
                opp_val = getattr(value, "eol_EClassifier", None)
                setattr(value, "eol_EClassifier", self)

class eol_ModelType(Type):

    pass
class eol_PseudoType(Type):

    pass
class eol_NativeType(Type):

    pass
class eol_AnyType(Type):

    def __init__(self, declared: bool, eol_AnyType: set["eol_Type"] = None):
        self.declared = declared
        self.eol_AnyType = eol_AnyType if eol_AnyType is not None else set()
        
    @property
    def declared(self) -> bool:
        return self.__declared

    @declared.setter
    def declared(self, declared: bool):
        self.__declared = declared

    @property
    def eol_AnyType(self):
        return self.__eol_AnyType

    @eol_AnyType.setter
    def eol_AnyType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_AnyType__eol_AnyType", None)
        self.__eol_AnyType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eol_Type156"):
                    opp_val = getattr(item, "eol_Type156", None)
                    
                    if opp_val == self:
                        setattr(item, "eol_Type156", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eol_Type156"):
                    opp_val = getattr(item, "eol_Type156", None)
                    
                    setattr(item, "eol_Type156", self)
                    

class eol_MapType(Type):

    pass
class OrderedCollectionType:

    pass
class eol_SequenceType(OrderedCollectionType):

    pass
class CollectionType:

    pass
class eol_UniqueCollectionType(CollectionType):

    pass
class eol_OrderedCollectionType(CollectionType):

    pass
class eol_BagType(CollectionType):

    pass
class UniqueCollectionType:

    pass
class eol_OrderedSetType(OrderedCollectionType, UniqueCollectionType):

    pass
class eol_SetType(UniqueCollectionType):

    pass
class PrimitiveType:

    pass
class eol_StringType(PrimitiveType):

    pass
class eol_IntegerType(PrimitiveType):

    pass
class eol_RealType(PrimitiveType):

    pass
class eol_BooleanType(PrimitiveType):

    pass
class eol_PrimitiveType(Type):

    pass
class LiteralExpression:

    pass
class eol_CollectionExpression(LiteralExpression):

    pass
class eol_NativeExpression(LiteralExpression):

    pass
class eol_PrimitiveExpression(LiteralExpression):

    pass
class eol_MapExpression(LiteralExpression):

    pass
class CollectionExpression:

    pass
class eol_OrderedSetExpression(CollectionExpression):

    pass
class eol_BagExpression(CollectionExpression):

    pass
class eol_SequenceExpression(CollectionExpression):

    pass
class eol_SetExpression(CollectionExpression):

    pass
class SwitchCaseStatement:

    pass
class eol_SwitchCaseDefaultStatement(SwitchCaseStatement):

    pass
class eol_SwitchCaseExpressionStatement(SwitchCaseStatement):

    pass
class eol_EPackage:

    pass
class Statement:

    pass
class eol_SwitchStatement(Statement):

    pass
class eol_ThrowStatement(Statement):

    pass
class eol_ExpressionStatement(Statement):

    pass
class eol_ReturnStatement(Statement):

    pass
class eol_IfStatement(Statement):

    pass
class eol_SwitchCaseStatement(Statement):

    pass
class eol_ModelDeclarationStatement(Statement):

    pass
class eol_WhileStatement(Statement):

    pass
class eol_AbortStatement(Statement):

    pass
class eol_TransactionStatement(Statement):

    pass
class eol_AssignmentStatement(Statement):

    pass
class eol_ForStatement(Statement):

    pass
class eol_DeleteStatement(Statement):

    pass
class eol_ContinueStatement(Statement):

    pass
class eol_BreakAllStatement(Statement):

    pass
class eol_BreakStatement(Statement):

    pass
class eol_FormalParameterExpression(VariableDeclarationExpression):

    pass
class UnaryOperatorExpression:

    pass
class eol_NotOperatorExpression(UnaryOperatorExpression):

    pass
class eol_NegativeOperatorExpression(UnaryOperatorExpression):

    pass
class FeatureCallExpression:

    pass
class eol_PropertyCallExpression(FeatureCallExpression):

    pass
class eol_FOLMethodCallExpression(FeatureCallExpression):

    pass
class eol_MethodCallExpression(FeatureCallExpression):

    pass
class eol_EObject:

    pass
class ArithmeticOperatorExpression:

    pass
class eol_PlusOperatorExpression(ArithmeticOperatorExpression):

    pass
class eol_MultiplyOperatorExpression(ArithmeticOperatorExpression):

    pass
class eol_MinusOperatorExpression(ArithmeticOperatorExpression):

    pass
class eol_DivideOperatorExpression(ArithmeticOperatorExpression):

    pass
class ComparisonOperatorExpression:

    pass
class eol_GreaterThanOrEqualToOperatorExpression(ComparisonOperatorExpression):

    pass
class eol_LessThanOrEqualToOperatorExpression(ComparisonOperatorExpression):

    pass
class eol_LessThanOperatorExpression(ComparisonOperatorExpression):

    pass
class eol_GreaterThanOperatorExpression(ComparisonOperatorExpression):

    pass
class eol_NotEqualsOperatorExpression(ComparisonOperatorExpression):

    pass
class eol_EqualsOperatorExpression(ComparisonOperatorExpression):

    pass
class eol_ModelExpression(NameExpression):

    pass
class PrimitiveExpression:

    pass
class eol_RealExpression(PrimitiveExpression):

    def __init__(self, val: float):
        self.val = val
        
    @property
    def val(self) -> float:
        return self.__val

    @val.setter
    def val(self, val: float):
        self.__val = val

class eol_IntegerExpression(PrimitiveExpression):

    def __init__(self, val: int):
        self.val = val
        
    @property
    def val(self) -> int:
        return self.__val

    @val.setter
    def val(self, val: int):
        self.__val = val

class eol_BooleanExpression(PrimitiveExpression):

    def __init__(self, val: bool, eol_BooleanExpression: "eol_FeatureCallExpression" = None, eol_BooleanExpression43: "eol_NameExpression" = None, eol_BooleanExpression50: "eol_PropertyCallExpression" = None, eol_BooleanExpression55: "eol_VariableDeclarationExpression" = None, eol_BooleanExpression219: "eol_NativeExpression" = None):
        self.val = val
        self.eol_BooleanExpression = eol_BooleanExpression
        self.eol_BooleanExpression43 = eol_BooleanExpression43
        self.eol_BooleanExpression50 = eol_BooleanExpression50
        self.eol_BooleanExpression55 = eol_BooleanExpression55
        self.eol_BooleanExpression219 = eol_BooleanExpression219
        
    @property
    def val(self) -> bool:
        return self.__val

    @val.setter
    def val(self, val: bool):
        self.__val = val

    @property
    def eol_BooleanExpression219(self):
        return self.__eol_BooleanExpression219

    @eol_BooleanExpression219.setter
    def eol_BooleanExpression219(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_BooleanExpression__eol_BooleanExpression219", None)
        self.__eol_BooleanExpression219 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_NativeExpression218"):
                opp_val = getattr(old_value, "eol_NativeExpression218", None)
                if opp_val == self:
                    setattr(old_value, "eol_NativeExpression218", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_NativeExpression218"):
                opp_val = getattr(value, "eol_NativeExpression218", None)
                setattr(value, "eol_NativeExpression218", self)

    @property
    def eol_BooleanExpression43(self):
        return self.__eol_BooleanExpression43

    @eol_BooleanExpression43.setter
    def eol_BooleanExpression43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_BooleanExpression__eol_BooleanExpression43", None)
        self.__eol_BooleanExpression43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_NameExpression42"):
                opp_val = getattr(old_value, "eol_NameExpression42", None)
                if opp_val == self:
                    setattr(old_value, "eol_NameExpression42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_NameExpression42"):
                opp_val = getattr(value, "eol_NameExpression42", None)
                setattr(value, "eol_NameExpression42", self)

    @property
    def eol_BooleanExpression(self):
        return self.__eol_BooleanExpression

    @eol_BooleanExpression.setter
    def eol_BooleanExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_BooleanExpression__eol_BooleanExpression", None)
        self.__eol_BooleanExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_FeatureCallExpression33"):
                opp_val = getattr(old_value, "eol_FeatureCallExpression33", None)
                if opp_val == self:
                    setattr(old_value, "eol_FeatureCallExpression33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_FeatureCallExpression33"):
                opp_val = getattr(value, "eol_FeatureCallExpression33", None)
                setattr(value, "eol_FeatureCallExpression33", self)

    @property
    def eol_BooleanExpression50(self):
        return self.__eol_BooleanExpression50

    @eol_BooleanExpression50.setter
    def eol_BooleanExpression50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_BooleanExpression__eol_BooleanExpression50", None)
        self.__eol_BooleanExpression50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_PropertyCallExpression49"):
                opp_val = getattr(old_value, "eol_PropertyCallExpression49", None)
                if opp_val == self:
                    setattr(old_value, "eol_PropertyCallExpression49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_PropertyCallExpression49"):
                opp_val = getattr(value, "eol_PropertyCallExpression49", None)
                setattr(value, "eol_PropertyCallExpression49", self)

    @property
    def eol_BooleanExpression55(self):
        return self.__eol_BooleanExpression55

    @eol_BooleanExpression55.setter
    def eol_BooleanExpression55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_BooleanExpression__eol_BooleanExpression55", None)
        self.__eol_BooleanExpression55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_VariableDeclarationExpression54"):
                opp_val = getattr(old_value, "eol_VariableDeclarationExpression54", None)
                if opp_val == self:
                    setattr(old_value, "eol_VariableDeclarationExpression54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_VariableDeclarationExpression54"):
                opp_val = getattr(value, "eol_VariableDeclarationExpression54", None)
                setattr(value, "eol_VariableDeclarationExpression54", self)

class LogicalOperatorExpression:

    pass
class eol_ImpliesOperatorExpression(LogicalOperatorExpression):

    pass
class eol_OrOperatorExpression(LogicalOperatorExpression):

    pass
class eol_XorOperatorExpression(LogicalOperatorExpression):

    pass
class eol_AndOperatorExpression(LogicalOperatorExpression):

    pass
class OperatorExpression:

    pass
class eol_UnaryOperatorExpression(OperatorExpression):

    pass
class eol_BinaryOperatorExpression(OperatorExpression):

    pass
class Expression:

    pass
class eol_FeatureCallExpression(Expression):

    pass
class eol_NameExpression(Expression):

    def __init__(self, name: str, resolvedContent: str, eol_NameExpression: "eol_EnumerationLiteralExpression" = None, eol_NameExpression27: "eol_EnumerationLiteralExpression" = None, eol_NameExpression38: "eol_MethodCallExpression" = None, eol_NameExpression42: "eol_BooleanExpression" = None, eol_NameExpression47: "eol_PropertyCallExpression" = None, eol_NameExpression71: "eol_OperationDefinition" = None, eol_NameExpression52: "eol_VariableDeclarationExpression" = None, eol_NameExpression142: "eol_FOLMethodCallExpression" = None, eol_NameExpression165: "eol_Annotation" = None, eol_NameExpression190: "eol_ModelDeclarationParameter" = None, eol_NameExpression197: "eol_TransactionStatement" = None, eol_NameExpression239: "eol_EolLibraryModule" = None):
        self.name = name
        self.resolvedContent = resolvedContent
        self.eol_NameExpression = eol_NameExpression
        self.eol_NameExpression27 = eol_NameExpression27
        self.eol_NameExpression38 = eol_NameExpression38
        self.eol_NameExpression42 = eol_NameExpression42
        self.eol_NameExpression47 = eol_NameExpression47
        self.eol_NameExpression71 = eol_NameExpression71
        self.eol_NameExpression52 = eol_NameExpression52
        self.eol_NameExpression142 = eol_NameExpression142
        self.eol_NameExpression165 = eol_NameExpression165
        self.eol_NameExpression190 = eol_NameExpression190
        self.eol_NameExpression197 = eol_NameExpression197
        self.eol_NameExpression239 = eol_NameExpression239
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def resolvedContent(self) -> str:
        return self.__resolvedContent

    @resolvedContent.setter
    def resolvedContent(self, resolvedContent: str):
        self.__resolvedContent = resolvedContent

    @property
    def eol_NameExpression38(self):
        return self.__eol_NameExpression38

    @eol_NameExpression38.setter
    def eol_NameExpression38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_NameExpression__eol_NameExpression38", None)
        self.__eol_NameExpression38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_MethodCallExpression37"):
                opp_val = getattr(old_value, "eol_MethodCallExpression37", None)
                if opp_val == self:
                    setattr(old_value, "eol_MethodCallExpression37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_MethodCallExpression37"):
                opp_val = getattr(value, "eol_MethodCallExpression37", None)
                setattr(value, "eol_MethodCallExpression37", self)

    @property
    def eol_NameExpression239(self):
        return self.__eol_NameExpression239

    @eol_NameExpression239.setter
    def eol_NameExpression239(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_NameExpression__eol_NameExpression239", None)
        self.__eol_NameExpression239 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_EolLibraryModule238"):
                opp_val = getattr(old_value, "eol_EolLibraryModule238", None)
                if opp_val == self:
                    setattr(old_value, "eol_EolLibraryModule238", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_EolLibraryModule238"):
                opp_val = getattr(value, "eol_EolLibraryModule238", None)
                setattr(value, "eol_EolLibraryModule238", self)

    @property
    def eol_NameExpression42(self):
        return self.__eol_NameExpression42

    @eol_NameExpression42.setter
    def eol_NameExpression42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_NameExpression__eol_NameExpression42", None)
        self.__eol_NameExpression42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_BooleanExpression43"):
                opp_val = getattr(old_value, "eol_BooleanExpression43", None)
                if opp_val == self:
                    setattr(old_value, "eol_BooleanExpression43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_BooleanExpression43"):
                opp_val = getattr(value, "eol_BooleanExpression43", None)
                setattr(value, "eol_BooleanExpression43", self)

    @property
    def eol_NameExpression197(self):
        return self.__eol_NameExpression197

    @eol_NameExpression197.setter
    def eol_NameExpression197(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_NameExpression__eol_NameExpression197", None)
        self.__eol_NameExpression197 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_TransactionStatement"):
                opp_val = getattr(old_value, "eol_TransactionStatement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_TransactionStatement"):
                opp_val = getattr(value, "eol_TransactionStatement", None)
                if opp_val is None:
                    setattr(value, "eol_TransactionStatement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eol_NameExpression47(self):
        return self.__eol_NameExpression47

    @eol_NameExpression47.setter
    def eol_NameExpression47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_NameExpression__eol_NameExpression47", None)
        self.__eol_NameExpression47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_PropertyCallExpression"):
                opp_val = getattr(old_value, "eol_PropertyCallExpression", None)
                if opp_val == self:
                    setattr(old_value, "eol_PropertyCallExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_PropertyCallExpression"):
                opp_val = getattr(value, "eol_PropertyCallExpression", None)
                setattr(value, "eol_PropertyCallExpression", self)

    @property
    def eol_NameExpression27(self):
        return self.__eol_NameExpression27

    @eol_NameExpression27.setter
    def eol_NameExpression27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_NameExpression__eol_NameExpression27", None)
        self.__eol_NameExpression27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_EnumerationLiteralExpression26"):
                opp_val = getattr(old_value, "eol_EnumerationLiteralExpression26", None)
                if opp_val == self:
                    setattr(old_value, "eol_EnumerationLiteralExpression26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_EnumerationLiteralExpression26"):
                opp_val = getattr(value, "eol_EnumerationLiteralExpression26", None)
                setattr(value, "eol_EnumerationLiteralExpression26", self)

    @property
    def eol_NameExpression142(self):
        return self.__eol_NameExpression142

    @eol_NameExpression142.setter
    def eol_NameExpression142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_NameExpression__eol_NameExpression142", None)
        self.__eol_NameExpression142 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_FOLMethodCallExpression141"):
                opp_val = getattr(old_value, "eol_FOLMethodCallExpression141", None)
                if opp_val == self:
                    setattr(old_value, "eol_FOLMethodCallExpression141", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_FOLMethodCallExpression141"):
                opp_val = getattr(value, "eol_FOLMethodCallExpression141", None)
                setattr(value, "eol_FOLMethodCallExpression141", self)

    @property
    def eol_NameExpression190(self):
        return self.__eol_NameExpression190

    @eol_NameExpression190.setter
    def eol_NameExpression190(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_NameExpression__eol_NameExpression190", None)
        self.__eol_NameExpression190 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_ModelDeclarationParameter189"):
                opp_val = getattr(old_value, "eol_ModelDeclarationParameter189", None)
                if opp_val == self:
                    setattr(old_value, "eol_ModelDeclarationParameter189", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_ModelDeclarationParameter189"):
                opp_val = getattr(value, "eol_ModelDeclarationParameter189", None)
                setattr(value, "eol_ModelDeclarationParameter189", self)

    @property
    def eol_NameExpression52(self):
        return self.__eol_NameExpression52

    @eol_NameExpression52.setter
    def eol_NameExpression52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_NameExpression__eol_NameExpression52", None)
        self.__eol_NameExpression52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_VariableDeclarationExpression"):
                opp_val = getattr(old_value, "eol_VariableDeclarationExpression", None)
                if opp_val == self:
                    setattr(old_value, "eol_VariableDeclarationExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_VariableDeclarationExpression"):
                opp_val = getattr(value, "eol_VariableDeclarationExpression", None)
                setattr(value, "eol_VariableDeclarationExpression", self)

    @property
    def eol_NameExpression165(self):
        return self.__eol_NameExpression165

    @eol_NameExpression165.setter
    def eol_NameExpression165(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_NameExpression__eol_NameExpression165", None)
        self.__eol_NameExpression165 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_Annotation"):
                opp_val = getattr(old_value, "eol_Annotation", None)
                if opp_val == self:
                    setattr(old_value, "eol_Annotation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_Annotation"):
                opp_val = getattr(value, "eol_Annotation", None)
                setattr(value, "eol_Annotation", self)

    @property
    def eol_NameExpression(self):
        return self.__eol_NameExpression

    @eol_NameExpression.setter
    def eol_NameExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_NameExpression__eol_NameExpression", None)
        self.__eol_NameExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_EnumerationLiteralExpression"):
                opp_val = getattr(old_value, "eol_EnumerationLiteralExpression", None)
                if opp_val == self:
                    setattr(old_value, "eol_EnumerationLiteralExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_EnumerationLiteralExpression"):
                opp_val = getattr(value, "eol_EnumerationLiteralExpression", None)
                setattr(value, "eol_EnumerationLiteralExpression", self)

    @property
    def eol_NameExpression71(self):
        return self.__eol_NameExpression71

    @eol_NameExpression71.setter
    def eol_NameExpression71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_NameExpression__eol_NameExpression71", None)
        self.__eol_NameExpression71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_OperationDefinition70"):
                opp_val = getattr(old_value, "eol_OperationDefinition70", None)
                if opp_val == self:
                    setattr(old_value, "eol_OperationDefinition70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_OperationDefinition70"):
                opp_val = getattr(value, "eol_OperationDefinition70", None)
                setattr(value, "eol_OperationDefinition70", self)

class eol_ModelDeclarationParameter(Expression):

    pass
class eol_CollectionInitValue(Expression):

    pass
class eol_KeyValue(Expression):

    pass
class eol_LiteralExpression(Expression):

    pass
class eol_VariableDeclarationExpression(Expression):

    def __init__(self, definitionPoints: str, eol_VariableDeclarationExpression: "eol_NameExpression" = None, eol_VariableDeclarationExpression54: "eol_BooleanExpression" = None, eol_VariableDeclarationExpression57: set["eol_Expression"] = None, eol_VariableDeclarationExpression76: "eol_OperationDefinition" = None, eol_VariableDeclarationExpression79: "eol_OperationDefinition" = None, eol_VariableDeclarationExpression123: "eol_ModelDeclarationStatement" = None, eol_VariableDeclarationExpression126: "eol_ModelDeclarationStatement" = None, eol_VariableDeclarationExpression129: "eol_ModelDeclarationStatement" = None):
        self.definitionPoints = definitionPoints
        self.eol_VariableDeclarationExpression = eol_VariableDeclarationExpression
        self.eol_VariableDeclarationExpression54 = eol_VariableDeclarationExpression54
        self.eol_VariableDeclarationExpression57 = eol_VariableDeclarationExpression57 if eol_VariableDeclarationExpression57 is not None else set()
        self.eol_VariableDeclarationExpression76 = eol_VariableDeclarationExpression76
        self.eol_VariableDeclarationExpression79 = eol_VariableDeclarationExpression79
        self.eol_VariableDeclarationExpression123 = eol_VariableDeclarationExpression123
        self.eol_VariableDeclarationExpression126 = eol_VariableDeclarationExpression126
        self.eol_VariableDeclarationExpression129 = eol_VariableDeclarationExpression129
        
    @property
    def definitionPoints(self) -> str:
        return self.__definitionPoints

    @definitionPoints.setter
    def definitionPoints(self, definitionPoints: str):
        self.__definitionPoints = definitionPoints

    @property
    def eol_VariableDeclarationExpression(self):
        return self.__eol_VariableDeclarationExpression

    @eol_VariableDeclarationExpression.setter
    def eol_VariableDeclarationExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_VariableDeclarationExpression__eol_VariableDeclarationExpression", None)
        self.__eol_VariableDeclarationExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_NameExpression52"):
                opp_val = getattr(old_value, "eol_NameExpression52", None)
                if opp_val == self:
                    setattr(old_value, "eol_NameExpression52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_NameExpression52"):
                opp_val = getattr(value, "eol_NameExpression52", None)
                setattr(value, "eol_NameExpression52", self)

    @property
    def eol_VariableDeclarationExpression129(self):
        return self.__eol_VariableDeclarationExpression129

    @eol_VariableDeclarationExpression129.setter
    def eol_VariableDeclarationExpression129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_VariableDeclarationExpression__eol_VariableDeclarationExpression129", None)
        self.__eol_VariableDeclarationExpression129 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_ModelDeclarationStatement128"):
                opp_val = getattr(old_value, "eol_ModelDeclarationStatement128", None)
                if opp_val == self:
                    setattr(old_value, "eol_ModelDeclarationStatement128", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_ModelDeclarationStatement128"):
                opp_val = getattr(value, "eol_ModelDeclarationStatement128", None)
                setattr(value, "eol_ModelDeclarationStatement128", self)

    @property
    def eol_VariableDeclarationExpression57(self):
        return self.__eol_VariableDeclarationExpression57

    @eol_VariableDeclarationExpression57.setter
    def eol_VariableDeclarationExpression57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_VariableDeclarationExpression__eol_VariableDeclarationExpression57", None)
        self.__eol_VariableDeclarationExpression57 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eol_Expression58"):
                    opp_val = getattr(item, "eol_Expression58", None)
                    
                    if opp_val == self:
                        setattr(item, "eol_Expression58", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eol_Expression58"):
                    opp_val = getattr(item, "eol_Expression58", None)
                    
                    setattr(item, "eol_Expression58", self)
                    

    @property
    def eol_VariableDeclarationExpression79(self):
        return self.__eol_VariableDeclarationExpression79

    @eol_VariableDeclarationExpression79.setter
    def eol_VariableDeclarationExpression79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_VariableDeclarationExpression__eol_VariableDeclarationExpression79", None)
        self.__eol_VariableDeclarationExpression79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_OperationDefinition78"):
                opp_val = getattr(old_value, "eol_OperationDefinition78", None)
                if opp_val == self:
                    setattr(old_value, "eol_OperationDefinition78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_OperationDefinition78"):
                opp_val = getattr(value, "eol_OperationDefinition78", None)
                setattr(value, "eol_OperationDefinition78", self)

    @property
    def eol_VariableDeclarationExpression76(self):
        return self.__eol_VariableDeclarationExpression76

    @eol_VariableDeclarationExpression76.setter
    def eol_VariableDeclarationExpression76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_VariableDeclarationExpression__eol_VariableDeclarationExpression76", None)
        self.__eol_VariableDeclarationExpression76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_OperationDefinition75"):
                opp_val = getattr(old_value, "eol_OperationDefinition75", None)
                if opp_val == self:
                    setattr(old_value, "eol_OperationDefinition75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_OperationDefinition75"):
                opp_val = getattr(value, "eol_OperationDefinition75", None)
                setattr(value, "eol_OperationDefinition75", self)

    @property
    def eol_VariableDeclarationExpression123(self):
        return self.__eol_VariableDeclarationExpression123

    @eol_VariableDeclarationExpression123.setter
    def eol_VariableDeclarationExpression123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_VariableDeclarationExpression__eol_VariableDeclarationExpression123", None)
        self.__eol_VariableDeclarationExpression123 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_ModelDeclarationStatement122"):
                opp_val = getattr(old_value, "eol_ModelDeclarationStatement122", None)
                if opp_val == self:
                    setattr(old_value, "eol_ModelDeclarationStatement122", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_ModelDeclarationStatement122"):
                opp_val = getattr(value, "eol_ModelDeclarationStatement122", None)
                setattr(value, "eol_ModelDeclarationStatement122", self)

    @property
    def eol_VariableDeclarationExpression54(self):
        return self.__eol_VariableDeclarationExpression54

    @eol_VariableDeclarationExpression54.setter
    def eol_VariableDeclarationExpression54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_VariableDeclarationExpression__eol_VariableDeclarationExpression54", None)
        self.__eol_VariableDeclarationExpression54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_BooleanExpression55"):
                opp_val = getattr(old_value, "eol_BooleanExpression55", None)
                if opp_val == self:
                    setattr(old_value, "eol_BooleanExpression55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_BooleanExpression55"):
                opp_val = getattr(value, "eol_BooleanExpression55", None)
                setattr(value, "eol_BooleanExpression55", self)

    @property
    def eol_VariableDeclarationExpression126(self):
        return self.__eol_VariableDeclarationExpression126

    @eol_VariableDeclarationExpression126.setter
    def eol_VariableDeclarationExpression126(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_VariableDeclarationExpression__eol_VariableDeclarationExpression126", None)
        self.__eol_VariableDeclarationExpression126 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_ModelDeclarationStatement125"):
                opp_val = getattr(old_value, "eol_ModelDeclarationStatement125", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_ModelDeclarationStatement125"):
                opp_val = getattr(value, "eol_ModelDeclarationStatement125", None)
                if opp_val is None:
                    setattr(value, "eol_ModelDeclarationStatement125", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class eol_NewExpression(Expression):

    pass
class eol_EnumerationLiteralExpression(Expression):

    pass
class eol_OperatorExpression(Expression):

    pass
class eol_TextPosition:

    def __init__(self, line: int, column: int, eol_TextPosition: "eol_TextRegion" = None, eol_TextPosition8: "eol_TextRegion" = None):
        self.line = line
        self.column = column
        self.eol_TextPosition = eol_TextPosition
        self.eol_TextPosition8 = eol_TextPosition8
        
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
    def eol_TextPosition(self):
        return self.__eol_TextPosition

    @eol_TextPosition.setter
    def eol_TextPosition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_TextPosition__eol_TextPosition", None)
        self.__eol_TextPosition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_TextRegion5"):
                opp_val = getattr(old_value, "eol_TextRegion5", None)
                if opp_val == self:
                    setattr(old_value, "eol_TextRegion5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_TextRegion5"):
                opp_val = getattr(value, "eol_TextRegion5", None)
                setattr(value, "eol_TextRegion5", self)

    @property
    def eol_TextPosition8(self):
        return self.__eol_TextPosition8

    @eol_TextPosition8.setter
    def eol_TextPosition8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_TextPosition__eol_TextPosition8", None)
        self.__eol_TextPosition8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_TextRegion7"):
                opp_val = getattr(old_value, "eol_TextRegion7", None)
                if opp_val == self:
                    setattr(old_value, "eol_TextRegion7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_TextRegion7"):
                opp_val = getattr(value, "eol_TextRegion7", None)
                setattr(value, "eol_TextRegion7", self)

class eol_TextRegion:

    pass
class eol_EolElement(ABC):

    def __init__(self, line: int, column: int, uri: str, eol_EolElement: "eol_EolElement" = None, eol_EolElement0: "eol_EolElement" = None, eol_EolElement3: "eol_TextRegion" = None):
        self.line = line
        self.column = column
        self.uri = uri
        self.eol_EolElement = eol_EolElement
        self.eol_EolElement0 = eol_EolElement0
        self.eol_EolElement3 = eol_EolElement3
        
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
    def uri(self) -> str:
        return self.__uri

    @uri.setter
    def uri(self, uri: str):
        self.__uri = uri

    @property
    def eol_EolElement(self):
        return self.__eol_EolElement

    @eol_EolElement.setter
    def eol_EolElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_EolElement__eol_EolElement", None)
        self.__eol_EolElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_EolElement0"):
                opp_val = getattr(old_value, "eol_EolElement0", None)
                if opp_val == self:
                    setattr(old_value, "eol_EolElement0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_EolElement0"):
                opp_val = getattr(value, "eol_EolElement0", None)
                setattr(value, "eol_EolElement0", self)

    @property
    def eol_EolElement0(self):
        return self.__eol_EolElement0

    @eol_EolElement0.setter
    def eol_EolElement0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_EolElement__eol_EolElement0", None)
        self.__eol_EolElement0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_EolElement"):
                opp_val = getattr(old_value, "eol_EolElement", None)
                if opp_val == self:
                    setattr(old_value, "eol_EolElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_EolElement"):
                opp_val = getattr(value, "eol_EolElement", None)
                setattr(value, "eol_EolElement", self)

    @property
    def eol_EolElement3(self):
        return self.__eol_EolElement3

    @eol_EolElement3.setter
    def eol_EolElement3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_EolElement__eol_EolElement3", None)
        self.__eol_EolElement3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_TextRegion"):
                opp_val = getattr(old_value, "eol_TextRegion", None)
                if opp_val == self:
                    setattr(old_value, "eol_TextRegion", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_TextRegion"):
                opp_val = getattr(value, "eol_TextRegion", None)
                setattr(value, "eol_TextRegion", self)

class eol_StringExpression(PrimitiveExpression):

    def __init__(self, val: str, eol_StringExpression: "eol_Import" = None, eol_StringExpression169: "eol_SimpleAnnotation" = None, eol_StringExpression181: "eol_NativeType" = None, eol_StringExpression193: "eol_ModelDeclarationParameter" = None, eol_StringExpression216: "eol_NativeExpression" = None):
        self.val = val
        self.eol_StringExpression = eol_StringExpression
        self.eol_StringExpression169 = eol_StringExpression169
        self.eol_StringExpression181 = eol_StringExpression181
        self.eol_StringExpression193 = eol_StringExpression193
        self.eol_StringExpression216 = eol_StringExpression216
        
    @property
    def val(self) -> str:
        return self.__val

    @val.setter
    def val(self, val: str):
        self.__val = val

    @property
    def eol_StringExpression193(self):
        return self.__eol_StringExpression193

    @eol_StringExpression193.setter
    def eol_StringExpression193(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_StringExpression__eol_StringExpression193", None)
        self.__eol_StringExpression193 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_ModelDeclarationParameter192"):
                opp_val = getattr(old_value, "eol_ModelDeclarationParameter192", None)
                if opp_val == self:
                    setattr(old_value, "eol_ModelDeclarationParameter192", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_ModelDeclarationParameter192"):
                opp_val = getattr(value, "eol_ModelDeclarationParameter192", None)
                setattr(value, "eol_ModelDeclarationParameter192", self)

    @property
    def eol_StringExpression181(self):
        return self.__eol_StringExpression181

    @eol_StringExpression181.setter
    def eol_StringExpression181(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_StringExpression__eol_StringExpression181", None)
        self.__eol_StringExpression181 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_NativeType"):
                opp_val = getattr(old_value, "eol_NativeType", None)
                if opp_val == self:
                    setattr(old_value, "eol_NativeType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_NativeType"):
                opp_val = getattr(value, "eol_NativeType", None)
                setattr(value, "eol_NativeType", self)

    @property
    def eol_StringExpression216(self):
        return self.__eol_StringExpression216

    @eol_StringExpression216.setter
    def eol_StringExpression216(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_StringExpression__eol_StringExpression216", None)
        self.__eol_StringExpression216 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_NativeExpression"):
                opp_val = getattr(old_value, "eol_NativeExpression", None)
                if opp_val == self:
                    setattr(old_value, "eol_NativeExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_NativeExpression"):
                opp_val = getattr(value, "eol_NativeExpression", None)
                setattr(value, "eol_NativeExpression", self)

    @property
    def eol_StringExpression(self):
        return self.__eol_StringExpression

    @eol_StringExpression.setter
    def eol_StringExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_StringExpression__eol_StringExpression", None)
        self.__eol_StringExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_Import"):
                opp_val = getattr(old_value, "eol_Import", None)
                if opp_val == self:
                    setattr(old_value, "eol_Import", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_Import"):
                opp_val = getattr(value, "eol_Import", None)
                setattr(value, "eol_Import", self)

    @property
    def eol_StringExpression169(self):
        return self.__eol_StringExpression169

    @eol_StringExpression169.setter
    def eol_StringExpression169(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_StringExpression__eol_StringExpression169", None)
        self.__eol_StringExpression169 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_SimpleAnnotation"):
                opp_val = getattr(old_value, "eol_SimpleAnnotation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_SimpleAnnotation"):
                opp_val = getattr(value, "eol_SimpleAnnotation", None)
                if opp_val is None:
                    setattr(value, "eol_SimpleAnnotation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class EolElement:

    pass
class eol_Type(EolElement):

    pass
class eol_Annotation(EolElement):

    pass
class eol_Statement(EolElement):

    pass
class eol_ExpressionOrStatementBlock(EolElement):

    pass
class eol_OperationDefinition(EolElement):

    pass
class eol_Expression(EolElement):

    pass
class eol_AnnotationBlock(EolElement):

    pass
class eol_EolLibraryModule(EolElement):

    pass
class eol_Import(EolElement):

    pass
class eol_Block(EolElement):

    pass
class EolLibraryModule:

    pass
class eol_EolProgram(EolLibraryModule):

    pass