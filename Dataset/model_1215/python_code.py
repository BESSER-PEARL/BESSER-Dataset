from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class PseudoType:

    pass
class eol_SelfContentType(PseudoType):

    pass
class eol_OperationArgType(PseudoType):

    pass
class eol_SelfInnermostType(PseudoType):

    pass
class eol_SelfType(PseudoType):

    pass
class AssignmentStatement:

    pass
class eol_SpecialAssignmentStatement(AssignmentStatement):

    pass
class CollectionInitValue:

    pass
class eol_ExpRange(CollectionInitValue):

    pass
class eol_ExprList(CollectionInitValue):

    pass
class VariableDeclarationExpression:

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
class eol_EClassifier:

    pass
class NameExpression:

    pass
class eol_SpecialNameExpression(NameExpression):

    pass
class Annotation:

    pass
class eol_SimpleAnnotation(Annotation):

    pass
class eol_ExecutableAnnotation(Annotation):

    pass
class LiteralExpression:

    pass
class eol_CollectionExpression(LiteralExpression):

    pass
class eol_NativeExpression(LiteralExpression):

    pass
class eol_PrimitiveExpression(LiteralExpression):

    pass
class eol_BagType(CollectionType):

    pass
class UniqueCollectionType:

    pass
class eol_OrderedSetType(UniqueCollectionType, OrderedCollectionType):

    pass
class eol_SetType(UniqueCollectionType):

    pass
class PrimitiveType:

    pass
class eol_IntegerType(PrimitiveType):

    pass
class eol_RealType(PrimitiveType):

    pass
class eol_StringType(PrimitiveType):

    pass
class eol_BooleanType(PrimitiveType):

    pass
class Type:

    pass
class eol_ModelType(Type):

    pass
class eol_MapType(Type):

    pass
class eol_CollectionType(Type):

    pass
class eol_VoidType(Type):

    pass
class eol_EType(Type):

    pass
class eol_ModelElementType(Type):

    def __init__(self, modelName: str, elementName: str, eol_ModelElementType: "eol_EClassifier" = None, eol_ModelElementType189: "eol_ModelDeclarationStatement" = None):
        self.modelName = modelName
        self.elementName = elementName
        self.eol_ModelElementType = eol_ModelElementType
        self.eol_ModelElementType189 = eol_ModelElementType189
        
    @property
    def elementName(self) -> str:
        return self.__elementName

    @elementName.setter
    def elementName(self, elementName: str):
        self.__elementName = elementName

    @property
    def modelName(self) -> str:
        return self.__modelName

    @modelName.setter
    def modelName(self, modelName: str):
        self.__modelName = modelName

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

    @property
    def eol_ModelElementType189(self):
        return self.__eol_ModelElementType189

    @eol_ModelElementType189.setter
    def eol_ModelElementType189(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_ModelElementType__eol_ModelElementType189", None)
        self.__eol_ModelElementType189 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_ModelDeclarationStatement190"):
                opp_val = getattr(old_value, "eol_ModelDeclarationStatement190", None)
                if opp_val == self:
                    setattr(old_value, "eol_ModelDeclarationStatement190", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_ModelDeclarationStatement190"):
                opp_val = getattr(value, "eol_ModelDeclarationStatement190", None)
                setattr(value, "eol_ModelDeclarationStatement190", self)

class eol_PseudoType(Type):

    pass
class eol_NativeType(Type):

    pass
class eol_PrimitiveType(Type):

    pass
class eol_AnyType(Type):

    pass
class eol_MapExpression(LiteralExpression):

    pass
class CollectionExpression:

    pass
class eol_SequenceExpression(CollectionExpression):

    pass
class eol_OrderedSetExpression(CollectionExpression):

    pass
class eol_BagExpression(CollectionExpression):

    pass
class eol_SetExpression(CollectionExpression):

    pass
class SwitchCaseStatement:

    pass
class eol_EPackage:

    pass
class eol_SwitchCaseDefaultStatement(SwitchCaseStatement):

    pass
class eol_SwitchCaseExpressionStatement(SwitchCaseStatement):

    pass
class eol_FormalParameterExpression(VariableDeclarationExpression):

    pass
class Statement:

    pass
class eol_BreakAllStatement(Statement):

    pass
class eol_ThrowStatement(Statement):

    pass
class eol_ForStatement(Statement):

    pass
class eol_SwitchCaseStatement(Statement):

    pass
class eol_IfStatement(Statement):

    pass
class eol_AbortStatement(Statement):

    pass
class eol_BreakStatement(Statement):

    pass
class eol_ExpressionStatement(Statement):

    pass
class eol_WhileStatement(Statement):

    pass
class eol_DeleteStatement(Statement):

    pass
class eol_ContinueStatement(Statement):

    pass
class eol_SwitchStatement(Statement):

    pass
class eol_ReturnStatement(Statement):

    pass
class eol_TransactionStatement(Statement):

    pass
class eol_AssignmentStatement(Statement):

    pass
class UnaryOperatorExpression:

    pass
class eol_NotOperatorExpression(UnaryOperatorExpression):

    pass
class eol_NegativeOperatorExpression(UnaryOperatorExpression):

    pass
class eol_ModelExpression(NameExpression):

    pass
class eol_EObject:

    pass
class FeatureCallExpression:

    pass
class eol_FOLMethodCallExpression(FeatureCallExpression):

    pass
class eol_PropertyCallExpression(FeatureCallExpression):

    pass
class eol_MethodCallExpression(FeatureCallExpression):

    pass
class eol_ModelDeclarationStatement(Statement):

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

    def __init__(self, val: bool, eol_BooleanExpression: "eol_FeatureCallExpression" = None, eol_BooleanExpression54: "eol_NameExpression" = None, eol_BooleanExpression61: "eol_PropertyCallExpression" = None, eol_BooleanExpression66: "eol_VariableDeclarationExpression" = None, eol_BooleanExpression230: "eol_NativeExpression" = None):
        self.val = val
        self.eol_BooleanExpression = eol_BooleanExpression
        self.eol_BooleanExpression54 = eol_BooleanExpression54
        self.eol_BooleanExpression61 = eol_BooleanExpression61
        self.eol_BooleanExpression66 = eol_BooleanExpression66
        self.eol_BooleanExpression230 = eol_BooleanExpression230
        
    @property
    def val(self) -> bool:
        return self.__val

    @val.setter
    def val(self, val: bool):
        self.__val = val

    @property
    def eol_BooleanExpression54(self):
        return self.__eol_BooleanExpression54

    @eol_BooleanExpression54.setter
    def eol_BooleanExpression54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_BooleanExpression__eol_BooleanExpression54", None)
        self.__eol_BooleanExpression54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_NameExpression53"):
                opp_val = getattr(old_value, "eol_NameExpression53", None)
                if opp_val == self:
                    setattr(old_value, "eol_NameExpression53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_NameExpression53"):
                opp_val = getattr(value, "eol_NameExpression53", None)
                setattr(value, "eol_NameExpression53", self)

    @property
    def eol_BooleanExpression66(self):
        return self.__eol_BooleanExpression66

    @eol_BooleanExpression66.setter
    def eol_BooleanExpression66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_BooleanExpression__eol_BooleanExpression66", None)
        self.__eol_BooleanExpression66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_VariableDeclarationExpression65"):
                opp_val = getattr(old_value, "eol_VariableDeclarationExpression65", None)
                if opp_val == self:
                    setattr(old_value, "eol_VariableDeclarationExpression65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_VariableDeclarationExpression65"):
                opp_val = getattr(value, "eol_VariableDeclarationExpression65", None)
                setattr(value, "eol_VariableDeclarationExpression65", self)

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
            if hasattr(old_value, "eol_FeatureCallExpression44"):
                opp_val = getattr(old_value, "eol_FeatureCallExpression44", None)
                if opp_val == self:
                    setattr(old_value, "eol_FeatureCallExpression44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_FeatureCallExpression44"):
                opp_val = getattr(value, "eol_FeatureCallExpression44", None)
                setattr(value, "eol_FeatureCallExpression44", self)

    @property
    def eol_BooleanExpression230(self):
        return self.__eol_BooleanExpression230

    @eol_BooleanExpression230.setter
    def eol_BooleanExpression230(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_BooleanExpression__eol_BooleanExpression230", None)
        self.__eol_BooleanExpression230 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_NativeExpression229"):
                opp_val = getattr(old_value, "eol_NativeExpression229", None)
                if opp_val == self:
                    setattr(old_value, "eol_NativeExpression229", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_NativeExpression229"):
                opp_val = getattr(value, "eol_NativeExpression229", None)
                setattr(value, "eol_NativeExpression229", self)

    @property
    def eol_BooleanExpression61(self):
        return self.__eol_BooleanExpression61

    @eol_BooleanExpression61.setter
    def eol_BooleanExpression61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_BooleanExpression__eol_BooleanExpression61", None)
        self.__eol_BooleanExpression61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_PropertyCallExpression60"):
                opp_val = getattr(old_value, "eol_PropertyCallExpression60", None)
                if opp_val == self:
                    setattr(old_value, "eol_PropertyCallExpression60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_PropertyCallExpression60"):
                opp_val = getattr(value, "eol_PropertyCallExpression60", None)
                setattr(value, "eol_PropertyCallExpression60", self)

class BinaryOperatorExpression:

    pass
class eol_GreaterThanOrEqualToOperatorExpression(BinaryOperatorExpression):

    pass
class eol_LessThanOrEqualToOperatorExpression(BinaryOperatorExpression):

    pass
class eol_GreaterThanOperatorExpression(BinaryOperatorExpression):

    pass
class eol_OrOperatorExpression(BinaryOperatorExpression):

    pass
class eol_NotEqualsOperatorExpression(BinaryOperatorExpression):

    pass
class eol_DivideOperatorExpression(BinaryOperatorExpression):

    pass
class eol_XorOperatorExpression(BinaryOperatorExpression):

    pass
class eol_PlusOperatorExpression(BinaryOperatorExpression):

    pass
class eol_EqualsOperatorExpression(BinaryOperatorExpression):

    pass
class eol_LessThanOperatorExpression(BinaryOperatorExpression):

    pass
class eol_MinusOperatorExpression(BinaryOperatorExpression):

    pass
class eol_MultiplyOperatorExpression(BinaryOperatorExpression):

    pass
class eol_ImpliesOperatorExpression(BinaryOperatorExpression):

    pass
class eol_AndOperatorExpression(BinaryOperatorExpression):

    pass
class OperatorExpression:

    pass
class eol_UnaryOperatorExpression(OperatorExpression):

    pass
class eol_BinaryOperatorExpression(OperatorExpression):

    pass
class Expression:

    pass
class eol_LiteralExpression(Expression):

    pass
class eol_VariableDeclarationExpression(Expression):

    def __init__(self, lastDefinitionPoint: str, eol_VariableDeclarationExpression: "eol_NameExpression" = None, eol_VariableDeclarationExpression65: "eol_BooleanExpression" = None, eol_VariableDeclarationExpression68: set["eol_Expression"] = None, eol_VariableDeclarationExpression88: "eol_OperationDefinition" = None, eol_VariableDeclarationExpression91: "eol_OperationDefinition" = None):
        self.lastDefinitionPoint = lastDefinitionPoint
        self.eol_VariableDeclarationExpression = eol_VariableDeclarationExpression
        self.eol_VariableDeclarationExpression65 = eol_VariableDeclarationExpression65
        self.eol_VariableDeclarationExpression68 = eol_VariableDeclarationExpression68 if eol_VariableDeclarationExpression68 is not None else set()
        self.eol_VariableDeclarationExpression88 = eol_VariableDeclarationExpression88
        self.eol_VariableDeclarationExpression91 = eol_VariableDeclarationExpression91
        
    @property
    def lastDefinitionPoint(self) -> str:
        return self.__lastDefinitionPoint

    @lastDefinitionPoint.setter
    def lastDefinitionPoint(self, lastDefinitionPoint: str):
        self.__lastDefinitionPoint = lastDefinitionPoint

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
            if hasattr(old_value, "eol_NameExpression63"):
                opp_val = getattr(old_value, "eol_NameExpression63", None)
                if opp_val == self:
                    setattr(old_value, "eol_NameExpression63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_NameExpression63"):
                opp_val = getattr(value, "eol_NameExpression63", None)
                setattr(value, "eol_NameExpression63", self)

    @property
    def eol_VariableDeclarationExpression68(self):
        return self.__eol_VariableDeclarationExpression68

    @eol_VariableDeclarationExpression68.setter
    def eol_VariableDeclarationExpression68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_VariableDeclarationExpression__eol_VariableDeclarationExpression68", None)
        self.__eol_VariableDeclarationExpression68 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eol_Expression69"):
                    opp_val = getattr(item, "eol_Expression69", None)
                    
                    if opp_val == self:
                        setattr(item, "eol_Expression69", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eol_Expression69"):
                    opp_val = getattr(item, "eol_Expression69", None)
                    
                    setattr(item, "eol_Expression69", self)
                    

    @property
    def eol_VariableDeclarationExpression65(self):
        return self.__eol_VariableDeclarationExpression65

    @eol_VariableDeclarationExpression65.setter
    def eol_VariableDeclarationExpression65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_VariableDeclarationExpression__eol_VariableDeclarationExpression65", None)
        self.__eol_VariableDeclarationExpression65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_BooleanExpression66"):
                opp_val = getattr(old_value, "eol_BooleanExpression66", None)
                if opp_val == self:
                    setattr(old_value, "eol_BooleanExpression66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_BooleanExpression66"):
                opp_val = getattr(value, "eol_BooleanExpression66", None)
                setattr(value, "eol_BooleanExpression66", self)

    @property
    def eol_VariableDeclarationExpression88(self):
        return self.__eol_VariableDeclarationExpression88

    @eol_VariableDeclarationExpression88.setter
    def eol_VariableDeclarationExpression88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_VariableDeclarationExpression__eol_VariableDeclarationExpression88", None)
        self.__eol_VariableDeclarationExpression88 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_OperationDefinition87"):
                opp_val = getattr(old_value, "eol_OperationDefinition87", None)
                if opp_val == self:
                    setattr(old_value, "eol_OperationDefinition87", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_OperationDefinition87"):
                opp_val = getattr(value, "eol_OperationDefinition87", None)
                setattr(value, "eol_OperationDefinition87", self)

    @property
    def eol_VariableDeclarationExpression91(self):
        return self.__eol_VariableDeclarationExpression91

    @eol_VariableDeclarationExpression91.setter
    def eol_VariableDeclarationExpression91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_VariableDeclarationExpression__eol_VariableDeclarationExpression91", None)
        self.__eol_VariableDeclarationExpression91 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_OperationDefinition90"):
                opp_val = getattr(old_value, "eol_OperationDefinition90", None)
                if opp_val == self:
                    setattr(old_value, "eol_OperationDefinition90", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_OperationDefinition90"):
                opp_val = getattr(value, "eol_OperationDefinition90", None)
                setattr(value, "eol_OperationDefinition90", self)

class eol_FeatureCallExpression(Expression):

    pass
class eol_EnumerationLiteralExpression(Expression):

    pass
class eol_NewExpression(Expression):

    pass
class eol_NameExpression(Expression):

    def __init__(self, name: str, resolvedContent: str, eol_NameExpression: "eol_Program" = None, eol_NameExpression49: "eol_MethodCallExpression" = None, eol_NameExpression53: "eol_BooleanExpression" = None, eol_NameExpression35: "eol_EnumerationLiteralExpression" = None, eol_NameExpression38: "eol_EnumerationLiteralExpression" = None, eol_NameExpression58: "eol_PropertyCallExpression" = None, eol_NameExpression63: "eol_VariableDeclarationExpression" = None, eol_NameExpression83: "eol_OperationDefinition" = None, eol_NameExpression134: "eol_ModelDeclarationStatement" = None, eol_NameExpression140: "eol_ModelDeclarationStatement" = None, eol_NameExpression153: "eol_FOLMethodCallExpression" = None, eol_NameExpression137: "eol_ModelDeclarationStatement" = None, eol_NameExpression176: "eol_Annotation" = None, eol_NameExpression201: "eol_ModelDeclarationParameter" = None, eol_NameExpression211: "eol_TransactionStatement" = None, eol_NameExpression222: "eol_ModelType" = None):
        self.name = name
        self.resolvedContent = resolvedContent
        self.eol_NameExpression = eol_NameExpression
        self.eol_NameExpression49 = eol_NameExpression49
        self.eol_NameExpression53 = eol_NameExpression53
        self.eol_NameExpression35 = eol_NameExpression35
        self.eol_NameExpression38 = eol_NameExpression38
        self.eol_NameExpression58 = eol_NameExpression58
        self.eol_NameExpression63 = eol_NameExpression63
        self.eol_NameExpression83 = eol_NameExpression83
        self.eol_NameExpression134 = eol_NameExpression134
        self.eol_NameExpression140 = eol_NameExpression140
        self.eol_NameExpression153 = eol_NameExpression153
        self.eol_NameExpression137 = eol_NameExpression137
        self.eol_NameExpression176 = eol_NameExpression176
        self.eol_NameExpression201 = eol_NameExpression201
        self.eol_NameExpression211 = eol_NameExpression211
        self.eol_NameExpression222 = eol_NameExpression222
        
    @property
    def resolvedContent(self) -> str:
        return self.__resolvedContent

    @resolvedContent.setter
    def resolvedContent(self, resolvedContent: str):
        self.__resolvedContent = resolvedContent

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def eol_NameExpression211(self):
        return self.__eol_NameExpression211

    @eol_NameExpression211.setter
    def eol_NameExpression211(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_NameExpression__eol_NameExpression211", None)
        self.__eol_NameExpression211 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_TransactionStatement210"):
                opp_val = getattr(old_value, "eol_TransactionStatement210", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_TransactionStatement210"):
                opp_val = getattr(value, "eol_TransactionStatement210", None)
                if opp_val is None:
                    setattr(value, "eol_TransactionStatement210", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eol_NameExpression153(self):
        return self.__eol_NameExpression153

    @eol_NameExpression153.setter
    def eol_NameExpression153(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_NameExpression__eol_NameExpression153", None)
        self.__eol_NameExpression153 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_FOLMethodCallExpression152"):
                opp_val = getattr(old_value, "eol_FOLMethodCallExpression152", None)
                if opp_val == self:
                    setattr(old_value, "eol_FOLMethodCallExpression152", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_FOLMethodCallExpression152"):
                opp_val = getattr(value, "eol_FOLMethodCallExpression152", None)
                setattr(value, "eol_FOLMethodCallExpression152", self)

    @property
    def eol_NameExpression176(self):
        return self.__eol_NameExpression176

    @eol_NameExpression176.setter
    def eol_NameExpression176(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_NameExpression__eol_NameExpression176", None)
        self.__eol_NameExpression176 = value
        
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
            if hasattr(old_value, "eol_Program18"):
                opp_val = getattr(old_value, "eol_Program18", None)
                if opp_val == self:
                    setattr(old_value, "eol_Program18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_Program18"):
                opp_val = getattr(value, "eol_Program18", None)
                setattr(value, "eol_Program18", self)

    @property
    def eol_NameExpression134(self):
        return self.__eol_NameExpression134

    @eol_NameExpression134.setter
    def eol_NameExpression134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_NameExpression__eol_NameExpression134", None)
        self.__eol_NameExpression134 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_ModelDeclarationStatement133"):
                opp_val = getattr(old_value, "eol_ModelDeclarationStatement133", None)
                if opp_val == self:
                    setattr(old_value, "eol_ModelDeclarationStatement133", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_ModelDeclarationStatement133"):
                opp_val = getattr(value, "eol_ModelDeclarationStatement133", None)
                setattr(value, "eol_ModelDeclarationStatement133", self)

    @property
    def eol_NameExpression137(self):
        return self.__eol_NameExpression137

    @eol_NameExpression137.setter
    def eol_NameExpression137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_NameExpression__eol_NameExpression137", None)
        self.__eol_NameExpression137 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_ModelDeclarationStatement136"):
                opp_val = getattr(old_value, "eol_ModelDeclarationStatement136", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_ModelDeclarationStatement136"):
                opp_val = getattr(value, "eol_ModelDeclarationStatement136", None)
                if opp_val is None:
                    setattr(value, "eol_ModelDeclarationStatement136", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eol_NameExpression201(self):
        return self.__eol_NameExpression201

    @eol_NameExpression201.setter
    def eol_NameExpression201(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_NameExpression__eol_NameExpression201", None)
        self.__eol_NameExpression201 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_ModelDeclarationParameter200"):
                opp_val = getattr(old_value, "eol_ModelDeclarationParameter200", None)
                if opp_val == self:
                    setattr(old_value, "eol_ModelDeclarationParameter200", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_ModelDeclarationParameter200"):
                opp_val = getattr(value, "eol_ModelDeclarationParameter200", None)
                setattr(value, "eol_ModelDeclarationParameter200", self)

    @property
    def eol_NameExpression35(self):
        return self.__eol_NameExpression35

    @eol_NameExpression35.setter
    def eol_NameExpression35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_NameExpression__eol_NameExpression35", None)
        self.__eol_NameExpression35 = value
        
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
    def eol_NameExpression63(self):
        return self.__eol_NameExpression63

    @eol_NameExpression63.setter
    def eol_NameExpression63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_NameExpression__eol_NameExpression63", None)
        self.__eol_NameExpression63 = value
        
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
    def eol_NameExpression49(self):
        return self.__eol_NameExpression49

    @eol_NameExpression49.setter
    def eol_NameExpression49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_NameExpression__eol_NameExpression49", None)
        self.__eol_NameExpression49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_MethodCallExpression48"):
                opp_val = getattr(old_value, "eol_MethodCallExpression48", None)
                if opp_val == self:
                    setattr(old_value, "eol_MethodCallExpression48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_MethodCallExpression48"):
                opp_val = getattr(value, "eol_MethodCallExpression48", None)
                setattr(value, "eol_MethodCallExpression48", self)

    @property
    def eol_NameExpression53(self):
        return self.__eol_NameExpression53

    @eol_NameExpression53.setter
    def eol_NameExpression53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_NameExpression__eol_NameExpression53", None)
        self.__eol_NameExpression53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_BooleanExpression54"):
                opp_val = getattr(old_value, "eol_BooleanExpression54", None)
                if opp_val == self:
                    setattr(old_value, "eol_BooleanExpression54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_BooleanExpression54"):
                opp_val = getattr(value, "eol_BooleanExpression54", None)
                setattr(value, "eol_BooleanExpression54", self)

    @property
    def eol_NameExpression58(self):
        return self.__eol_NameExpression58

    @eol_NameExpression58.setter
    def eol_NameExpression58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_NameExpression__eol_NameExpression58", None)
        self.__eol_NameExpression58 = value
        
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
    def eol_NameExpression140(self):
        return self.__eol_NameExpression140

    @eol_NameExpression140.setter
    def eol_NameExpression140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_NameExpression__eol_NameExpression140", None)
        self.__eol_NameExpression140 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_ModelDeclarationStatement139"):
                opp_val = getattr(old_value, "eol_ModelDeclarationStatement139", None)
                if opp_val == self:
                    setattr(old_value, "eol_ModelDeclarationStatement139", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_ModelDeclarationStatement139"):
                opp_val = getattr(value, "eol_ModelDeclarationStatement139", None)
                setattr(value, "eol_ModelDeclarationStatement139", self)

    @property
    def eol_NameExpression222(self):
        return self.__eol_NameExpression222

    @eol_NameExpression222.setter
    def eol_NameExpression222(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_NameExpression__eol_NameExpression222", None)
        self.__eol_NameExpression222 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_ModelType"):
                opp_val = getattr(old_value, "eol_ModelType", None)
                if opp_val == self:
                    setattr(old_value, "eol_ModelType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_ModelType"):
                opp_val = getattr(value, "eol_ModelType", None)
                setattr(value, "eol_ModelType", self)

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
            if hasattr(old_value, "eol_EnumerationLiteralExpression37"):
                opp_val = getattr(old_value, "eol_EnumerationLiteralExpression37", None)
                if opp_val == self:
                    setattr(old_value, "eol_EnumerationLiteralExpression37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_EnumerationLiteralExpression37"):
                opp_val = getattr(value, "eol_EnumerationLiteralExpression37", None)
                setattr(value, "eol_EnumerationLiteralExpression37", self)

    @property
    def eol_NameExpression83(self):
        return self.__eol_NameExpression83

    @eol_NameExpression83.setter
    def eol_NameExpression83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_NameExpression__eol_NameExpression83", None)
        self.__eol_NameExpression83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_OperationDefinition82"):
                opp_val = getattr(old_value, "eol_OperationDefinition82", None)
                if opp_val == self:
                    setattr(old_value, "eol_OperationDefinition82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_OperationDefinition82"):
                opp_val = getattr(value, "eol_OperationDefinition82", None)
                setattr(value, "eol_OperationDefinition82", self)

class eol_OperatorExpression(Expression):

    pass
class eol_StringExpression(PrimitiveExpression):

    def __init__(self, val: str, eol_StringExpression: "eol_Import" = None, eol_StringExpression180: "eol_SimpleAnnotation" = None, eol_StringExpression204: "eol_ModelDeclarationParameter" = None, eol_StringExpression192: "eol_NativeType" = None, eol_StringExpression227: "eol_NativeExpression" = None):
        self.val = val
        self.eol_StringExpression = eol_StringExpression
        self.eol_StringExpression180 = eol_StringExpression180
        self.eol_StringExpression204 = eol_StringExpression204
        self.eol_StringExpression192 = eol_StringExpression192
        self.eol_StringExpression227 = eol_StringExpression227
        
    @property
    def val(self) -> str:
        return self.__val

    @val.setter
    def val(self, val: str):
        self.__val = val

    @property
    def eol_StringExpression180(self):
        return self.__eol_StringExpression180

    @eol_StringExpression180.setter
    def eol_StringExpression180(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_StringExpression__eol_StringExpression180", None)
        self.__eol_StringExpression180 = value
        
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

    @property
    def eol_StringExpression204(self):
        return self.__eol_StringExpression204

    @eol_StringExpression204.setter
    def eol_StringExpression204(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_StringExpression__eol_StringExpression204", None)
        self.__eol_StringExpression204 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_ModelDeclarationParameter203"):
                opp_val = getattr(old_value, "eol_ModelDeclarationParameter203", None)
                if opp_val == self:
                    setattr(old_value, "eol_ModelDeclarationParameter203", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_ModelDeclarationParameter203"):
                opp_val = getattr(value, "eol_ModelDeclarationParameter203", None)
                setattr(value, "eol_ModelDeclarationParameter203", self)

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
            if hasattr(old_value, "eol_Import22"):
                opp_val = getattr(old_value, "eol_Import22", None)
                if opp_val == self:
                    setattr(old_value, "eol_Import22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_Import22"):
                opp_val = getattr(value, "eol_Import22", None)
                setattr(value, "eol_Import22", self)

    @property
    def eol_StringExpression192(self):
        return self.__eol_StringExpression192

    @eol_StringExpression192.setter
    def eol_StringExpression192(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_StringExpression__eol_StringExpression192", None)
        self.__eol_StringExpression192 = value
        
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
    def eol_StringExpression227(self):
        return self.__eol_StringExpression227

    @eol_StringExpression227.setter
    def eol_StringExpression227(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_StringExpression__eol_StringExpression227", None)
        self.__eol_StringExpression227 = value
        
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

class EolElement:

    pass
class eol_CollectionInitValue(EolElement):

    pass
class eol_OperationDefinition(EolElement):

    pass
class eol_Expression(EolElement):

    pass
class eol_Annotation(EolElement):

    pass
class eol_KeyValue(EolElement):

    pass
class eol_Type(EolElement):

    pass
class eol_Statement(EolElement):

    pass
class eol_AnnotationBlock(EolElement):

    pass
class eol_ModelDeclarationParameter(EolElement):

    pass
class eol_Block(EolElement):

    pass
class eol_Import(EolElement):

    pass
class eol_Program(EolElement):

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
    def uri(self) -> str:
        return self.__uri

    @uri.setter
    def uri(self, uri: str):
        self.__uri = uri

    @property
    def line(self) -> int:
        return self.__line

    @line.setter
    def line(self, line: int):
        self.__line = line

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
