from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class RealType:

    pass
class eol_IntegerType(RealType):

    pass
class SummablePrimitiveType:

    pass
class ComparablePrimitiveType:

    pass
class eol_StringType(ComparablePrimitiveType, SummablePrimitiveType):

    pass
class eol_RealType(ComparablePrimitiveType, SummablePrimitiveType):

    pass
class PrimitiveType:

    pass
class eol_SummablePrimitiveType(PrimitiveType):

    pass
class eol_BooleanType(PrimitiveType):

    pass
class eol_ComparablePrimitiveType(PrimitiveType):

    pass
class OrderedCollectionType:

    pass
class eol_SequenceType(OrderedCollectionType):

    pass
class PseudoType:

    pass
class eol_SelfContentType(PseudoType):

    pass
class eol_SelfType(PseudoType):

    pass
class AnyType:

    pass
class eol_PrimitiveType(AnyType):

    pass
class eol_NativeType(AnyType):

    pass
class eol_ModelElementType(AnyType):

    def __init__(self, modelName: str, elementName: str, resolvedIMetamodel: str, resolvedIPackage: str, modelElementType: str, eol_ModelElementType: "eol_ModelDeclarationStatement" = None):
        self.modelName = modelName
        self.elementName = elementName
        self.resolvedIMetamodel = resolvedIMetamodel
        self.resolvedIPackage = resolvedIPackage
        self.modelElementType = modelElementType
        self.eol_ModelElementType = eol_ModelElementType
        
    @property
    def modelName(self) -> str:
        return self.__modelName

    @modelName.setter
    def modelName(self, modelName: str):
        self.__modelName = modelName

    @property
    def resolvedIPackage(self) -> str:
        return self.__resolvedIPackage

    @resolvedIPackage.setter
    def resolvedIPackage(self, resolvedIPackage: str):
        self.__resolvedIPackage = resolvedIPackage

    @property
    def elementName(self) -> str:
        return self.__elementName

    @elementName.setter
    def elementName(self, elementName: str):
        self.__elementName = elementName

    @property
    def resolvedIMetamodel(self) -> str:
        return self.__resolvedIMetamodel

    @resolvedIMetamodel.setter
    def resolvedIMetamodel(self, resolvedIMetamodel: str):
        self.__resolvedIMetamodel = resolvedIMetamodel

    @property
    def modelElementType(self) -> str:
        return self.__modelElementType

    @modelElementType.setter
    def modelElementType(self, modelElementType: str):
        self.__modelElementType = modelElementType

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
            if hasattr(old_value, "eol_ModelDeclarationStatement182"):
                opp_val = getattr(old_value, "eol_ModelDeclarationStatement182", None)
                if opp_val == self:
                    setattr(old_value, "eol_ModelDeclarationStatement182", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_ModelDeclarationStatement182"):
                opp_val = getattr(value, "eol_ModelDeclarationStatement182", None)
                setattr(value, "eol_ModelDeclarationStatement182", self)

class eol_MapType(AnyType):

    pass
class eol_PseudoType(AnyType):

    pass
class eol_ModelType(AnyType):

    def __init__(self, resolvedIMetamodel: str, modelName: str):
        self.resolvedIMetamodel = resolvedIMetamodel
        self.modelName = modelName
        
    @property
    def resolvedIMetamodel(self) -> str:
        return self.__resolvedIMetamodel

    @resolvedIMetamodel.setter
    def resolvedIMetamodel(self, resolvedIMetamodel: str):
        self.__resolvedIMetamodel = resolvedIMetamodel

    @property
    def modelName(self) -> str:
        return self.__modelName

    @modelName.setter
    def modelName(self, modelName: str):
        self.__modelName = modelName

class UniqueCollectionType:

    pass
class eol_OrderedSetType(OrderedCollectionType, UniqueCollectionType):

    pass
class eol_SetType(UniqueCollectionType):

    pass
class CollectionType:

    pass
class eol_UniqueCollectionType(CollectionType):

    pass
class eol_OrderedCollectionType(CollectionType):

    pass
class eol_BagType(CollectionType):

    pass
class eol_CollectionType(AnyType):

    pass
class eol_InvalidType(AnyType):

    pass
class eol_VoidType(AnyType):

    pass
class AnnotationStatement:

    pass
class eol_ExecutableAnnotationStatement(AnnotationStatement):

    pass
class eol_SimpleAnnotationStatement(AnnotationStatement):

    pass
class AssignmentStatement:

    pass
class eol_SpecialAssignmentStatement(AssignmentStatement):

    pass
class Type:

    pass
class eol_AnyType(Type):

    def __init__(self, declared: bool, eol_AnyType: set["eol_Type"] = None, eol_AnyType184: "eol_MapType" = None, eol_AnyType187: "eol_MapType" = None):
        self.declared = declared
        self.eol_AnyType = eol_AnyType if eol_AnyType is not None else set()
        self.eol_AnyType184 = eol_AnyType184
        self.eol_AnyType187 = eol_AnyType187
        
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
                if hasattr(item, "eol_Type180"):
                    opp_val = getattr(item, "eol_Type180", None)
                    
                    if opp_val == self:
                        setattr(item, "eol_Type180", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eol_Type180"):
                    opp_val = getattr(item, "eol_Type180", None)
                    
                    setattr(item, "eol_Type180", self)
                    

    @property
    def eol_AnyType184(self):
        return self.__eol_AnyType184

    @eol_AnyType184.setter
    def eol_AnyType184(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_AnyType__eol_AnyType184", None)
        self.__eol_AnyType184 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_MapType"):
                opp_val = getattr(old_value, "eol_MapType", None)
                if opp_val == self:
                    setattr(old_value, "eol_MapType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_MapType"):
                opp_val = getattr(value, "eol_MapType", None)
                setattr(value, "eol_MapType", self)

    @property
    def eol_AnyType187(self):
        return self.__eol_AnyType187

    @eol_AnyType187.setter
    def eol_AnyType187(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_AnyType__eol_AnyType187", None)
        self.__eol_AnyType187 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_MapType186"):
                opp_val = getattr(old_value, "eol_MapType186", None)
                if opp_val == self:
                    setattr(old_value, "eol_MapType186", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_MapType186"):
                opp_val = getattr(value, "eol_MapType186", None)
                setattr(value, "eol_MapType186", self)

class Statement:

    pass
class eol_AssignmentStatement(Statement):

    pass
class eol_SwitchStatement(Statement):

    pass
class eol_ContinueStatement(Statement):

    pass
class eol_BreakStatement(Statement):

    pass
class eol_WhileStatement(Statement):

    pass
class eol_ForStatement(Statement):

    pass
class eol_BreakAllStatement(Statement):

    pass
class eol_AbortStatement(Statement):

    pass
class eol_ThrowStatement(Statement):

    pass
class eol_ExpressionStatement(Statement):

    pass
class eol_AnnotationStatement(Statement):

    pass
class eol_DeleteStatement(Statement):

    pass
class eol_SwitchCaseStatement(Statement):

    pass
class eol_ReturnStatement(Statement):

    pass
class eol_TransactionStatement(Statement):

    pass
class eol_IfStatement(Statement):

    pass
class SwitchCaseStatement:

    pass
class eol_SwitchCaseDefaultStatement(SwitchCaseStatement):

    pass
class eol_SwitchCaseExpressionStatement(SwitchCaseStatement):

    pass
class CollectionInitialisationExpression:

    pass
class eol_ExpressionRange(CollectionInitialisationExpression):

    pass
class eol_ExpressionList(CollectionInitialisationExpression):

    pass
class OrderedCollection:

    pass
class eol_SequenceExpression(OrderedCollection):

    pass
class UniqueCollection:

    pass
class eol_OrderedSetExpression(UniqueCollection, OrderedCollection):

    pass
class eol_SetExpression(UniqueCollection):

    pass
class CollectionExpression:

    pass
class eol_UniqueCollection(CollectionExpression):

    pass
class eol_OrderedCollection(CollectionExpression):

    pass
class eol_BagExpression(CollectionExpression):

    pass
class SummableExpression:

    pass
class ComparableExpression:

    pass
class eol_RealExpression(ComparableExpression, SummableExpression):

    def __init__(self, value: float):
        self.value = value
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

class eol_IntegerExpression(ComparableExpression, SummableExpression):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class eol_StringExpression(ComparableExpression, SummableExpression):

    def __init__(self, value: str, eol_StringExpression: "eol_SimpleAnnotationStatement" = None, eol_StringExpression189: "eol_NativeType" = None):
        self.value = value
        self.eol_StringExpression = eol_StringExpression
        self.eol_StringExpression189 = eol_StringExpression189
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

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
            if hasattr(old_value, "eol_SimpleAnnotationStatement"):
                opp_val = getattr(old_value, "eol_SimpleAnnotationStatement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_SimpleAnnotationStatement"):
                opp_val = getattr(value, "eol_SimpleAnnotationStatement", None)
                if opp_val is None:
                    setattr(value, "eol_SimpleAnnotationStatement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eol_StringExpression189(self):
        return self.__eol_StringExpression189

    @eol_StringExpression189.setter
    def eol_StringExpression189(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_StringExpression__eol_StringExpression189", None)
        self.__eol_StringExpression189 = value
        
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

class PrimitiveExpression:

    pass
class eol_SummableExpression(PrimitiveExpression):

    pass
class eol_BooleanExpression(PrimitiveExpression):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class eol_ComparableExpression(PrimitiveExpression):

    pass
class KeyValueExpression:

    pass
class eol_ModelDeclarationParameter(KeyValueExpression):

    pass
class FeatureCallExpression:

    pass
class eol_FOLMethodCallExpression(FeatureCallExpression):

    pass
class eol_PropertyCallExpression(FeatureCallExpression):

    def __init__(self, extended: bool, eol_PropertyCallExpression: "eol_NameExpression" = None):
        self.extended = extended
        self.eol_PropertyCallExpression = eol_PropertyCallExpression
        
    @property
    def extended(self) -> bool:
        return self.__extended

    @extended.setter
    def extended(self, extended: bool):
        self.__extended = extended

    @property
    def eol_PropertyCallExpression(self):
        return self.__eol_PropertyCallExpression

    @eol_PropertyCallExpression.setter
    def eol_PropertyCallExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_PropertyCallExpression__eol_PropertyCallExpression", None)
        self.__eol_PropertyCallExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_NameExpression67"):
                opp_val = getattr(old_value, "eol_NameExpression67", None)
                if opp_val == self:
                    setattr(old_value, "eol_NameExpression67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_NameExpression67"):
                opp_val = getattr(value, "eol_NameExpression67", None)
                setattr(value, "eol_NameExpression67", self)

class eol_MethodCallExpression(FeatureCallExpression):

    pass
class VariableDeclarationExpression:

    pass
class ComparisonOperatorExpression:

    pass
class eol_LessThanOrEqualToOperatorExpression(ComparisonOperatorExpression):

    pass
class eol_NotEqualsOperatorExpression(ComparisonOperatorExpression):

    pass
class eol_LessThanOperatorExpression(ComparisonOperatorExpression):

    pass
class eol_GreaterThanOperatorExpression(ComparisonOperatorExpression):

    pass
class eol_EqualsOperatorExpression(ComparisonOperatorExpression):

    pass
class eol_GreaterThanOrEqualToOperatorExpression(ComparisonOperatorExpression):

    pass
class ArithmeticOperatorExpression:

    pass
class eol_MinusOperatorExpression(ArithmeticOperatorExpression):

    pass
class eol_PlusOperatorExpression(ArithmeticOperatorExpression):

    pass
class eol_MultiplyOperatorExpression(ArithmeticOperatorExpression):

    pass
class eol_DivideOperatorExpression(ArithmeticOperatorExpression):

    pass
class LogicalOperatorExpression:

    pass
class eol_ImpliesOperatorExpression(LogicalOperatorExpression):

    pass
class eol_XorOperatorExpression(LogicalOperatorExpression):

    pass
class eol_OrOperatorExpression(LogicalOperatorExpression):

    pass
class eol_AndOperatorExpression(LogicalOperatorExpression):

    pass
class BinaryOperatorExpression:

    pass
class eol_ArithmeticOperatorExpression(BinaryOperatorExpression):

    pass
class eol_ComparisonOperatorExpression(BinaryOperatorExpression):

    pass
class eol_LogicalOperatorExpression(BinaryOperatorExpression):

    pass
class UnaryOperatorExpression:

    pass
class eol_NegativeOperatorExpression(UnaryOperatorExpression):

    pass
class eol_NotOperatorExpression(UnaryOperatorExpression):

    pass
class OperatorExpression:

    pass
class eol_BinaryOperatorExpression(OperatorExpression):

    pass
class eol_UnaryOperatorExpression(OperatorExpression):

    pass
class Expression:

    pass
class eol_EnumerationLiteralExpression(Expression):

    pass
class eol_CollectionInitialisationExpression(Expression):

    pass
class eol_PrimitiveExpression(Expression):

    pass
class eol_NewExpression(Expression):

    pass
class eol_FeatureCallExpression(Expression):

    def __init__(self, arrow: bool, eol_FeatureCallExpression: "eol_Expression" = None):
        self.arrow = arrow
        self.eol_FeatureCallExpression = eol_FeatureCallExpression
        
    @property
    def arrow(self) -> bool:
        return self.__arrow

    @arrow.setter
    def arrow(self, arrow: bool):
        self.__arrow = arrow

    @property
    def eol_FeatureCallExpression(self):
        return self.__eol_FeatureCallExpression

    @eol_FeatureCallExpression.setter
    def eol_FeatureCallExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_FeatureCallExpression__eol_FeatureCallExpression", None)
        self.__eol_FeatureCallExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_Expression57"):
                opp_val = getattr(old_value, "eol_Expression57", None)
                if opp_val == self:
                    setattr(old_value, "eol_Expression57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_Expression57"):
                opp_val = getattr(value, "eol_Expression57", None)
                setattr(value, "eol_Expression57", self)

class eol_KeyValueExpression(Expression):

    pass
class eol_CollectionExpression(Expression):

    pass
class eol_MapExpression(Expression):

    pass
class eol_OperatorExpression(Expression):

    pass
class eol_Type:

    pass
class eol_VariableDeclarationExpression(Expression):

    def __init__(self, create: bool, eol_VariableDeclarationExpression: "eol_OperationDefinition" = None, eol_VariableDeclarationExpression36: "eol_OperationDefinition" = None, eol_VariableDeclarationExpression51: "eol_NameExpression" = None, eol_VariableDeclarationExpression54: set["eol_NameExpression"] = None, eol_VariableDeclarationExpression176: "eol_ModelDeclarationStatement" = None, eol_VariableDeclarationExpression170: "eol_ModelDeclarationStatement" = None):
        self.create = create
        self.eol_VariableDeclarationExpression = eol_VariableDeclarationExpression
        self.eol_VariableDeclarationExpression36 = eol_VariableDeclarationExpression36
        self.eol_VariableDeclarationExpression51 = eol_VariableDeclarationExpression51
        self.eol_VariableDeclarationExpression54 = eol_VariableDeclarationExpression54 if eol_VariableDeclarationExpression54 is not None else set()
        self.eol_VariableDeclarationExpression176 = eol_VariableDeclarationExpression176
        self.eol_VariableDeclarationExpression170 = eol_VariableDeclarationExpression170
        
    @property
    def create(self) -> bool:
        return self.__create

    @create.setter
    def create(self, create: bool):
        self.__create = create

    @property
    def eol_VariableDeclarationExpression176(self):
        return self.__eol_VariableDeclarationExpression176

    @eol_VariableDeclarationExpression176.setter
    def eol_VariableDeclarationExpression176(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_VariableDeclarationExpression__eol_VariableDeclarationExpression176", None)
        self.__eol_VariableDeclarationExpression176 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_ModelDeclarationStatement175"):
                opp_val = getattr(old_value, "eol_ModelDeclarationStatement175", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_ModelDeclarationStatement175"):
                opp_val = getattr(value, "eol_ModelDeclarationStatement175", None)
                if opp_val is None:
                    setattr(value, "eol_ModelDeclarationStatement175", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "eol_OperationDefinition33"):
                opp_val = getattr(old_value, "eol_OperationDefinition33", None)
                if opp_val == self:
                    setattr(old_value, "eol_OperationDefinition33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_OperationDefinition33"):
                opp_val = getattr(value, "eol_OperationDefinition33", None)
                setattr(value, "eol_OperationDefinition33", self)

    @property
    def eol_VariableDeclarationExpression54(self):
        return self.__eol_VariableDeclarationExpression54

    @eol_VariableDeclarationExpression54.setter
    def eol_VariableDeclarationExpression54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_VariableDeclarationExpression__eol_VariableDeclarationExpression54", None)
        self.__eol_VariableDeclarationExpression54 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eol_NameExpression55"):
                    opp_val = getattr(item, "eol_NameExpression55", None)
                    
                    if opp_val == self:
                        setattr(item, "eol_NameExpression55", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eol_NameExpression55"):
                    opp_val = getattr(item, "eol_NameExpression55", None)
                    
                    setattr(item, "eol_NameExpression55", self)
                    

    @property
    def eol_VariableDeclarationExpression170(self):
        return self.__eol_VariableDeclarationExpression170

    @eol_VariableDeclarationExpression170.setter
    def eol_VariableDeclarationExpression170(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_VariableDeclarationExpression__eol_VariableDeclarationExpression170", None)
        self.__eol_VariableDeclarationExpression170 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_ModelDeclarationStatement169"):
                opp_val = getattr(old_value, "eol_ModelDeclarationStatement169", None)
                if opp_val == self:
                    setattr(old_value, "eol_ModelDeclarationStatement169", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_ModelDeclarationStatement169"):
                opp_val = getattr(value, "eol_ModelDeclarationStatement169", None)
                setattr(value, "eol_ModelDeclarationStatement169", self)

    @property
    def eol_VariableDeclarationExpression51(self):
        return self.__eol_VariableDeclarationExpression51

    @eol_VariableDeclarationExpression51.setter
    def eol_VariableDeclarationExpression51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_VariableDeclarationExpression__eol_VariableDeclarationExpression51", None)
        self.__eol_VariableDeclarationExpression51 = value
        
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
    def eol_VariableDeclarationExpression36(self):
        return self.__eol_VariableDeclarationExpression36

    @eol_VariableDeclarationExpression36.setter
    def eol_VariableDeclarationExpression36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_VariableDeclarationExpression__eol_VariableDeclarationExpression36", None)
        self.__eol_VariableDeclarationExpression36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_OperationDefinition35"):
                opp_val = getattr(old_value, "eol_OperationDefinition35", None)
                if opp_val == self:
                    setattr(old_value, "eol_OperationDefinition35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_OperationDefinition35"):
                opp_val = getattr(value, "eol_OperationDefinition35", None)
                setattr(value, "eol_OperationDefinition35", self)

class eol_FormalParameterExpression(VariableDeclarationExpression):

    pass
class eol_NameExpression(Expression):

    def __init__(self, name: str, resolvedContent: str, isType: bool, eol_NameExpression: "eol_OperationDefinition" = None, eol_NameExpression52: "eol_VariableDeclarationExpression" = None, eol_NameExpression55: "eol_VariableDeclarationExpression" = None, eol_NameExpression62: "eol_MethodCallExpression" = None, eol_NameExpression67: "eol_PropertyCallExpression" = None, eol_NameExpression75: "eol_FOLMethodCallExpression" = None, eol_NameExpression85: "eol_NewExpression" = None, eol_NameExpression96: "eol_EnumerationLiteralExpression" = None, eol_NameExpression99: "eol_EnumerationLiteralExpression" = None, eol_NameExpression102: "eol_EnumerationLiteralExpression" = None, eol_NameExpression111: "eol_TransactionStatement" = None, eol_NameExpression173: "eol_ModelDeclarationStatement" = None, eol_NameExpression164: "eol_AnnotationStatement" = None):
        self.name = name
        self.resolvedContent = resolvedContent
        self.isType = isType
        self.eol_NameExpression = eol_NameExpression
        self.eol_NameExpression52 = eol_NameExpression52
        self.eol_NameExpression55 = eol_NameExpression55
        self.eol_NameExpression62 = eol_NameExpression62
        self.eol_NameExpression67 = eol_NameExpression67
        self.eol_NameExpression75 = eol_NameExpression75
        self.eol_NameExpression85 = eol_NameExpression85
        self.eol_NameExpression96 = eol_NameExpression96
        self.eol_NameExpression99 = eol_NameExpression99
        self.eol_NameExpression102 = eol_NameExpression102
        self.eol_NameExpression111 = eol_NameExpression111
        self.eol_NameExpression173 = eol_NameExpression173
        self.eol_NameExpression164 = eol_NameExpression164
        
    @property
    def isType(self) -> bool:
        return self.__isType

    @isType.setter
    def isType(self, isType: bool):
        self.__isType = isType

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
    def eol_NameExpression99(self):
        return self.__eol_NameExpression99

    @eol_NameExpression99.setter
    def eol_NameExpression99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_NameExpression__eol_NameExpression99", None)
        self.__eol_NameExpression99 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_EnumerationLiteralExpression98"):
                opp_val = getattr(old_value, "eol_EnumerationLiteralExpression98", None)
                if opp_val == self:
                    setattr(old_value, "eol_EnumerationLiteralExpression98", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_EnumerationLiteralExpression98"):
                opp_val = getattr(value, "eol_EnumerationLiteralExpression98", None)
                setattr(value, "eol_EnumerationLiteralExpression98", self)

    @property
    def eol_NameExpression85(self):
        return self.__eol_NameExpression85

    @eol_NameExpression85.setter
    def eol_NameExpression85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_NameExpression__eol_NameExpression85", None)
        self.__eol_NameExpression85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_NewExpression"):
                opp_val = getattr(old_value, "eol_NewExpression", None)
                if opp_val == self:
                    setattr(old_value, "eol_NewExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_NewExpression"):
                opp_val = getattr(value, "eol_NewExpression", None)
                setattr(value, "eol_NewExpression", self)

    @property
    def eol_NameExpression111(self):
        return self.__eol_NameExpression111

    @eol_NameExpression111.setter
    def eol_NameExpression111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_NameExpression__eol_NameExpression111", None)
        self.__eol_NameExpression111 = value
        
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
    def eol_NameExpression102(self):
        return self.__eol_NameExpression102

    @eol_NameExpression102.setter
    def eol_NameExpression102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_NameExpression__eol_NameExpression102", None)
        self.__eol_NameExpression102 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_EnumerationLiteralExpression101"):
                opp_val = getattr(old_value, "eol_EnumerationLiteralExpression101", None)
                if opp_val == self:
                    setattr(old_value, "eol_EnumerationLiteralExpression101", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_EnumerationLiteralExpression101"):
                opp_val = getattr(value, "eol_EnumerationLiteralExpression101", None)
                setattr(value, "eol_EnumerationLiteralExpression101", self)

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
            if hasattr(old_value, "eol_VariableDeclarationExpression51"):
                opp_val = getattr(old_value, "eol_VariableDeclarationExpression51", None)
                if opp_val == self:
                    setattr(old_value, "eol_VariableDeclarationExpression51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_VariableDeclarationExpression51"):
                opp_val = getattr(value, "eol_VariableDeclarationExpression51", None)
                setattr(value, "eol_VariableDeclarationExpression51", self)

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
            if hasattr(old_value, "eol_OperationDefinition29"):
                opp_val = getattr(old_value, "eol_OperationDefinition29", None)
                if opp_val == self:
                    setattr(old_value, "eol_OperationDefinition29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_OperationDefinition29"):
                opp_val = getattr(value, "eol_OperationDefinition29", None)
                setattr(value, "eol_OperationDefinition29", self)

    @property
    def eol_NameExpression67(self):
        return self.__eol_NameExpression67

    @eol_NameExpression67.setter
    def eol_NameExpression67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_NameExpression__eol_NameExpression67", None)
        self.__eol_NameExpression67 = value
        
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
    def eol_NameExpression62(self):
        return self.__eol_NameExpression62

    @eol_NameExpression62.setter
    def eol_NameExpression62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_NameExpression__eol_NameExpression62", None)
        self.__eol_NameExpression62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_MethodCallExpression61"):
                opp_val = getattr(old_value, "eol_MethodCallExpression61", None)
                if opp_val == self:
                    setattr(old_value, "eol_MethodCallExpression61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_MethodCallExpression61"):
                opp_val = getattr(value, "eol_MethodCallExpression61", None)
                setattr(value, "eol_MethodCallExpression61", self)

    @property
    def eol_NameExpression75(self):
        return self.__eol_NameExpression75

    @eol_NameExpression75.setter
    def eol_NameExpression75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_NameExpression__eol_NameExpression75", None)
        self.__eol_NameExpression75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_FOLMethodCallExpression74"):
                opp_val = getattr(old_value, "eol_FOLMethodCallExpression74", None)
                if opp_val == self:
                    setattr(old_value, "eol_FOLMethodCallExpression74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_FOLMethodCallExpression74"):
                opp_val = getattr(value, "eol_FOLMethodCallExpression74", None)
                setattr(value, "eol_FOLMethodCallExpression74", self)

    @property
    def eol_NameExpression173(self):
        return self.__eol_NameExpression173

    @eol_NameExpression173.setter
    def eol_NameExpression173(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_NameExpression__eol_NameExpression173", None)
        self.__eol_NameExpression173 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_ModelDeclarationStatement172"):
                opp_val = getattr(old_value, "eol_ModelDeclarationStatement172", None)
                if opp_val == self:
                    setattr(old_value, "eol_ModelDeclarationStatement172", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_ModelDeclarationStatement172"):
                opp_val = getattr(value, "eol_ModelDeclarationStatement172", None)
                setattr(value, "eol_ModelDeclarationStatement172", self)

    @property
    def eol_NameExpression164(self):
        return self.__eol_NameExpression164

    @eol_NameExpression164.setter
    def eol_NameExpression164(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_NameExpression__eol_NameExpression164", None)
        self.__eol_NameExpression164 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_AnnotationStatement"):
                opp_val = getattr(old_value, "eol_AnnotationStatement", None)
                if opp_val == self:
                    setattr(old_value, "eol_AnnotationStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_AnnotationStatement"):
                opp_val = getattr(value, "eol_AnnotationStatement", None)
                setattr(value, "eol_AnnotationStatement", self)

    @property
    def eol_NameExpression55(self):
        return self.__eol_NameExpression55

    @eol_NameExpression55.setter
    def eol_NameExpression55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_NameExpression__eol_NameExpression55", None)
        self.__eol_NameExpression55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_VariableDeclarationExpression54"):
                opp_val = getattr(old_value, "eol_VariableDeclarationExpression54", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_VariableDeclarationExpression54"):
                opp_val = getattr(value, "eol_VariableDeclarationExpression54", None)
                if opp_val is None:
                    setattr(value, "eol_VariableDeclarationExpression54", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eol_NameExpression96(self):
        return self.__eol_NameExpression96

    @eol_NameExpression96.setter
    def eol_NameExpression96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_NameExpression__eol_NameExpression96", None)
        self.__eol_NameExpression96 = value
        
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

class eol_EOLLibraryModule:

    def __init__(self, name: str, eol_EOLLibraryModule: set["eol_Import"] = None, eol_EOLLibraryModule2: set["eol_ModelDeclarationStatement"] = None, eol_EOLLibraryModule4: set["eol_OperationDefinition"] = None, eol_EOLLibraryModule8: "eol_Import" = None):
        self.name = name
        self.eol_EOLLibraryModule = eol_EOLLibraryModule if eol_EOLLibraryModule is not None else set()
        self.eol_EOLLibraryModule2 = eol_EOLLibraryModule2 if eol_EOLLibraryModule2 is not None else set()
        self.eol_EOLLibraryModule4 = eol_EOLLibraryModule4 if eol_EOLLibraryModule4 is not None else set()
        self.eol_EOLLibraryModule8 = eol_EOLLibraryModule8
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def eol_EOLLibraryModule2(self):
        return self.__eol_EOLLibraryModule2

    @eol_EOLLibraryModule2.setter
    def eol_EOLLibraryModule2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_EOLLibraryModule__eol_EOLLibraryModule2", None)
        self.__eol_EOLLibraryModule2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eol_ModelDeclarationStatement"):
                    opp_val = getattr(item, "eol_ModelDeclarationStatement", None)
                    
                    if opp_val == self:
                        setattr(item, "eol_ModelDeclarationStatement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eol_ModelDeclarationStatement"):
                    opp_val = getattr(item, "eol_ModelDeclarationStatement", None)
                    
                    setattr(item, "eol_ModelDeclarationStatement", self)
                    

    @property
    def eol_EOLLibraryModule4(self):
        return self.__eol_EOLLibraryModule4

    @eol_EOLLibraryModule4.setter
    def eol_EOLLibraryModule4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_EOLLibraryModule__eol_EOLLibraryModule4", None)
        self.__eol_EOLLibraryModule4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eol_OperationDefinition"):
                    opp_val = getattr(item, "eol_OperationDefinition", None)
                    
                    if opp_val == self:
                        setattr(item, "eol_OperationDefinition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eol_OperationDefinition"):
                    opp_val = getattr(item, "eol_OperationDefinition", None)
                    
                    setattr(item, "eol_OperationDefinition", self)
                    

    @property
    def eol_EOLLibraryModule8(self):
        return self.__eol_EOLLibraryModule8

    @eol_EOLLibraryModule8.setter
    def eol_EOLLibraryModule8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_EOLLibraryModule__eol_EOLLibraryModule8", None)
        self.__eol_EOLLibraryModule8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_Import7"):
                opp_val = getattr(old_value, "eol_Import7", None)
                if opp_val == self:
                    setattr(old_value, "eol_Import7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_Import7"):
                opp_val = getattr(value, "eol_Import7", None)
                setattr(value, "eol_Import7", self)

    @property
    def eol_EOLLibraryModule(self):
        return self.__eol_EOLLibraryModule

    @eol_EOLLibraryModule.setter
    def eol_EOLLibraryModule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_EOLLibraryModule__eol_EOLLibraryModule", None)
        self.__eol_EOLLibraryModule = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eol_Import"):
                    opp_val = getattr(item, "eol_Import", None)
                    
                    if opp_val == self:
                        setattr(item, "eol_Import", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eol_Import"):
                    opp_val = getattr(item, "eol_Import", None)
                    
                    setattr(item, "eol_Import", self)
                    

class eol_Expression(ABC):

    def __init__(self, inBrackets: bool, eol_Expression: "eol_ExpressionOrStatementBlock" = None, eol_Expression17: "eol_ExpressionOrStatementBlock" = None, eol_Expression41: "eol_Type" = None, eol_Expression44: "eol_UnaryOperatorExpression" = None, eol_Expression46: "eol_BinaryOperatorExpression" = None, eol_Expression49: "eol_BinaryOperatorExpression" = None, eol_Expression57: "eol_FeatureCallExpression" = None, eol_Expression59: "eol_MethodCallExpression" = None, eol_Expression72: "eol_FOLMethodCallExpression" = None, eol_Expression83: "eol_KeyValueExpression" = None, eol_Expression88: "eol_NewExpression" = None, eol_Expression92: "eol_CollectionExpression" = None, eol_Expression80: "eol_KeyValueExpression" = None, eol_Expression104: "eol_ExpressionRange" = None, eol_Expression107: "eol_ExpressionRange" = None, eol_Expression109: "eol_ExpressionList" = None, eol_Expression127: "eol_SwitchCaseExpressionStatement" = None, eol_Expression129: "eol_IfStatement" = None, eol_Expression116: "eol_ExpressionStatement" = None, eol_Expression118: "eol_SwitchStatement" = None, eol_Expression155: "eol_ThrowStatement" = None, eol_Expression157: "eol_DeleteStatement" = None, eol_Expression159: "eol_AssignmentStatement" = None, eol_Expression162: "eol_AssignmentStatement" = None, eol_Expression143: "eol_ForStatement" = None, eol_Expression148: "eol_WhileStatement" = None, eol_Expression153: "eol_ReturnStatement" = None, eol_Expression167: "eol_ExecutableAnnotationStatement" = None):
        self.inBrackets = inBrackets
        self.eol_Expression = eol_Expression
        self.eol_Expression17 = eol_Expression17
        self.eol_Expression41 = eol_Expression41
        self.eol_Expression44 = eol_Expression44
        self.eol_Expression46 = eol_Expression46
        self.eol_Expression49 = eol_Expression49
        self.eol_Expression57 = eol_Expression57
        self.eol_Expression59 = eol_Expression59
        self.eol_Expression72 = eol_Expression72
        self.eol_Expression83 = eol_Expression83
        self.eol_Expression88 = eol_Expression88
        self.eol_Expression92 = eol_Expression92
        self.eol_Expression80 = eol_Expression80
        self.eol_Expression104 = eol_Expression104
        self.eol_Expression107 = eol_Expression107
        self.eol_Expression109 = eol_Expression109
        self.eol_Expression127 = eol_Expression127
        self.eol_Expression129 = eol_Expression129
        self.eol_Expression116 = eol_Expression116
        self.eol_Expression118 = eol_Expression118
        self.eol_Expression155 = eol_Expression155
        self.eol_Expression157 = eol_Expression157
        self.eol_Expression159 = eol_Expression159
        self.eol_Expression162 = eol_Expression162
        self.eol_Expression143 = eol_Expression143
        self.eol_Expression148 = eol_Expression148
        self.eol_Expression153 = eol_Expression153
        self.eol_Expression167 = eol_Expression167
        
    @property
    def inBrackets(self) -> bool:
        return self.__inBrackets

    @inBrackets.setter
    def inBrackets(self, inBrackets: bool):
        self.__inBrackets = inBrackets

    @property
    def eol_Expression83(self):
        return self.__eol_Expression83

    @eol_Expression83.setter
    def eol_Expression83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_Expression__eol_Expression83", None)
        self.__eol_Expression83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_KeyValueExpression82"):
                opp_val = getattr(old_value, "eol_KeyValueExpression82", None)
                if opp_val == self:
                    setattr(old_value, "eol_KeyValueExpression82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_KeyValueExpression82"):
                opp_val = getattr(value, "eol_KeyValueExpression82", None)
                setattr(value, "eol_KeyValueExpression82", self)

    @property
    def eol_Expression57(self):
        return self.__eol_Expression57

    @eol_Expression57.setter
    def eol_Expression57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_Expression__eol_Expression57", None)
        self.__eol_Expression57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_FeatureCallExpression"):
                opp_val = getattr(old_value, "eol_FeatureCallExpression", None)
                if opp_val == self:
                    setattr(old_value, "eol_FeatureCallExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_FeatureCallExpression"):
                opp_val = getattr(value, "eol_FeatureCallExpression", None)
                setattr(value, "eol_FeatureCallExpression", self)

    @property
    def eol_Expression80(self):
        return self.__eol_Expression80

    @eol_Expression80.setter
    def eol_Expression80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_Expression__eol_Expression80", None)
        self.__eol_Expression80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_KeyValueExpression"):
                opp_val = getattr(old_value, "eol_KeyValueExpression", None)
                if opp_val == self:
                    setattr(old_value, "eol_KeyValueExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_KeyValueExpression"):
                opp_val = getattr(value, "eol_KeyValueExpression", None)
                setattr(value, "eol_KeyValueExpression", self)

    @property
    def eol_Expression167(self):
        return self.__eol_Expression167

    @eol_Expression167.setter
    def eol_Expression167(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_Expression__eol_Expression167", None)
        self.__eol_Expression167 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_ExecutableAnnotationStatement"):
                opp_val = getattr(old_value, "eol_ExecutableAnnotationStatement", None)
                if opp_val == self:
                    setattr(old_value, "eol_ExecutableAnnotationStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_ExecutableAnnotationStatement"):
                opp_val = getattr(value, "eol_ExecutableAnnotationStatement", None)
                setattr(value, "eol_ExecutableAnnotationStatement", self)

    @property
    def eol_Expression162(self):
        return self.__eol_Expression162

    @eol_Expression162.setter
    def eol_Expression162(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_Expression__eol_Expression162", None)
        self.__eol_Expression162 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_AssignmentStatement161"):
                opp_val = getattr(old_value, "eol_AssignmentStatement161", None)
                if opp_val == self:
                    setattr(old_value, "eol_AssignmentStatement161", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_AssignmentStatement161"):
                opp_val = getattr(value, "eol_AssignmentStatement161", None)
                setattr(value, "eol_AssignmentStatement161", self)

    @property
    def eol_Expression157(self):
        return self.__eol_Expression157

    @eol_Expression157.setter
    def eol_Expression157(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_Expression__eol_Expression157", None)
        self.__eol_Expression157 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_DeleteStatement"):
                opp_val = getattr(old_value, "eol_DeleteStatement", None)
                if opp_val == self:
                    setattr(old_value, "eol_DeleteStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_DeleteStatement"):
                opp_val = getattr(value, "eol_DeleteStatement", None)
                setattr(value, "eol_DeleteStatement", self)

    @property
    def eol_Expression116(self):
        return self.__eol_Expression116

    @eol_Expression116.setter
    def eol_Expression116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_Expression__eol_Expression116", None)
        self.__eol_Expression116 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_ExpressionStatement"):
                opp_val = getattr(old_value, "eol_ExpressionStatement", None)
                if opp_val == self:
                    setattr(old_value, "eol_ExpressionStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_ExpressionStatement"):
                opp_val = getattr(value, "eol_ExpressionStatement", None)
                setattr(value, "eol_ExpressionStatement", self)

    @property
    def eol_Expression109(self):
        return self.__eol_Expression109

    @eol_Expression109.setter
    def eol_Expression109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_Expression__eol_Expression109", None)
        self.__eol_Expression109 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_ExpressionList"):
                opp_val = getattr(old_value, "eol_ExpressionList", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_ExpressionList"):
                opp_val = getattr(value, "eol_ExpressionList", None)
                if opp_val is None:
                    setattr(value, "eol_ExpressionList", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eol_Expression153(self):
        return self.__eol_Expression153

    @eol_Expression153.setter
    def eol_Expression153(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_Expression__eol_Expression153", None)
        self.__eol_Expression153 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_ReturnStatement"):
                opp_val = getattr(old_value, "eol_ReturnStatement", None)
                if opp_val == self:
                    setattr(old_value, "eol_ReturnStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_ReturnStatement"):
                opp_val = getattr(value, "eol_ReturnStatement", None)
                setattr(value, "eol_ReturnStatement", self)

    @property
    def eol_Expression92(self):
        return self.__eol_Expression92

    @eol_Expression92.setter
    def eol_Expression92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_Expression__eol_Expression92", None)
        self.__eol_Expression92 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_CollectionExpression"):
                opp_val = getattr(old_value, "eol_CollectionExpression", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_CollectionExpression"):
                opp_val = getattr(value, "eol_CollectionExpression", None)
                if opp_val is None:
                    setattr(value, "eol_CollectionExpression", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eol_Expression107(self):
        return self.__eol_Expression107

    @eol_Expression107.setter
    def eol_Expression107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_Expression__eol_Expression107", None)
        self.__eol_Expression107 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_ExpressionRange106"):
                opp_val = getattr(old_value, "eol_ExpressionRange106", None)
                if opp_val == self:
                    setattr(old_value, "eol_ExpressionRange106", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_ExpressionRange106"):
                opp_val = getattr(value, "eol_ExpressionRange106", None)
                setattr(value, "eol_ExpressionRange106", self)

    @property
    def eol_Expression143(self):
        return self.__eol_Expression143

    @eol_Expression143.setter
    def eol_Expression143(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_Expression__eol_Expression143", None)
        self.__eol_Expression143 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_ForStatement142"):
                opp_val = getattr(old_value, "eol_ForStatement142", None)
                if opp_val == self:
                    setattr(old_value, "eol_ForStatement142", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_ForStatement142"):
                opp_val = getattr(value, "eol_ForStatement142", None)
                setattr(value, "eol_ForStatement142", self)

    @property
    def eol_Expression44(self):
        return self.__eol_Expression44

    @eol_Expression44.setter
    def eol_Expression44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_Expression__eol_Expression44", None)
        self.__eol_Expression44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_UnaryOperatorExpression"):
                opp_val = getattr(old_value, "eol_UnaryOperatorExpression", None)
                if opp_val == self:
                    setattr(old_value, "eol_UnaryOperatorExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_UnaryOperatorExpression"):
                opp_val = getattr(value, "eol_UnaryOperatorExpression", None)
                setattr(value, "eol_UnaryOperatorExpression", self)

    @property
    def eol_Expression17(self):
        return self.__eol_Expression17

    @eol_Expression17.setter
    def eol_Expression17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_Expression__eol_Expression17", None)
        self.__eol_Expression17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_ExpressionOrStatementBlock16"):
                opp_val = getattr(old_value, "eol_ExpressionOrStatementBlock16", None)
                if opp_val == self:
                    setattr(old_value, "eol_ExpressionOrStatementBlock16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_ExpressionOrStatementBlock16"):
                opp_val = getattr(value, "eol_ExpressionOrStatementBlock16", None)
                setattr(value, "eol_ExpressionOrStatementBlock16", self)

    @property
    def eol_Expression148(self):
        return self.__eol_Expression148

    @eol_Expression148.setter
    def eol_Expression148(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_Expression__eol_Expression148", None)
        self.__eol_Expression148 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_WhileStatement"):
                opp_val = getattr(old_value, "eol_WhileStatement", None)
                if opp_val == self:
                    setattr(old_value, "eol_WhileStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_WhileStatement"):
                opp_val = getattr(value, "eol_WhileStatement", None)
                setattr(value, "eol_WhileStatement", self)

    @property
    def eol_Expression104(self):
        return self.__eol_Expression104

    @eol_Expression104.setter
    def eol_Expression104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_Expression__eol_Expression104", None)
        self.__eol_Expression104 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_ExpressionRange"):
                opp_val = getattr(old_value, "eol_ExpressionRange", None)
                if opp_val == self:
                    setattr(old_value, "eol_ExpressionRange", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_ExpressionRange"):
                opp_val = getattr(value, "eol_ExpressionRange", None)
                setattr(value, "eol_ExpressionRange", self)

    @property
    def eol_Expression129(self):
        return self.__eol_Expression129

    @eol_Expression129.setter
    def eol_Expression129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_Expression__eol_Expression129", None)
        self.__eol_Expression129 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_IfStatement"):
                opp_val = getattr(old_value, "eol_IfStatement", None)
                if opp_val == self:
                    setattr(old_value, "eol_IfStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_IfStatement"):
                opp_val = getattr(value, "eol_IfStatement", None)
                setattr(value, "eol_IfStatement", self)

    @property
    def eol_Expression155(self):
        return self.__eol_Expression155

    @eol_Expression155.setter
    def eol_Expression155(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_Expression__eol_Expression155", None)
        self.__eol_Expression155 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_ThrowStatement"):
                opp_val = getattr(old_value, "eol_ThrowStatement", None)
                if opp_val == self:
                    setattr(old_value, "eol_ThrowStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_ThrowStatement"):
                opp_val = getattr(value, "eol_ThrowStatement", None)
                setattr(value, "eol_ThrowStatement", self)

    @property
    def eol_Expression88(self):
        return self.__eol_Expression88

    @eol_Expression88.setter
    def eol_Expression88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_Expression__eol_Expression88", None)
        self.__eol_Expression88 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_NewExpression87"):
                opp_val = getattr(old_value, "eol_NewExpression87", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_NewExpression87"):
                opp_val = getattr(value, "eol_NewExpression87", None)
                if opp_val is None:
                    setattr(value, "eol_NewExpression87", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eol_Expression118(self):
        return self.__eol_Expression118

    @eol_Expression118.setter
    def eol_Expression118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_Expression__eol_Expression118", None)
        self.__eol_Expression118 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_SwitchStatement"):
                opp_val = getattr(old_value, "eol_SwitchStatement", None)
                if opp_val == self:
                    setattr(old_value, "eol_SwitchStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_SwitchStatement"):
                opp_val = getattr(value, "eol_SwitchStatement", None)
                setattr(value, "eol_SwitchStatement", self)

    @property
    def eol_Expression46(self):
        return self.__eol_Expression46

    @eol_Expression46.setter
    def eol_Expression46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_Expression__eol_Expression46", None)
        self.__eol_Expression46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_BinaryOperatorExpression"):
                opp_val = getattr(old_value, "eol_BinaryOperatorExpression", None)
                if opp_val == self:
                    setattr(old_value, "eol_BinaryOperatorExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_BinaryOperatorExpression"):
                opp_val = getattr(value, "eol_BinaryOperatorExpression", None)
                setattr(value, "eol_BinaryOperatorExpression", self)

    @property
    def eol_Expression159(self):
        return self.__eol_Expression159

    @eol_Expression159.setter
    def eol_Expression159(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_Expression__eol_Expression159", None)
        self.__eol_Expression159 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_AssignmentStatement"):
                opp_val = getattr(old_value, "eol_AssignmentStatement", None)
                if opp_val == self:
                    setattr(old_value, "eol_AssignmentStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_AssignmentStatement"):
                opp_val = getattr(value, "eol_AssignmentStatement", None)
                setattr(value, "eol_AssignmentStatement", self)

    @property
    def eol_Expression41(self):
        return self.__eol_Expression41

    @eol_Expression41.setter
    def eol_Expression41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_Expression__eol_Expression41", None)
        self.__eol_Expression41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_Type42"):
                opp_val = getattr(old_value, "eol_Type42", None)
                if opp_val == self:
                    setattr(old_value, "eol_Type42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_Type42"):
                opp_val = getattr(value, "eol_Type42", None)
                setattr(value, "eol_Type42", self)

    @property
    def eol_Expression127(self):
        return self.__eol_Expression127

    @eol_Expression127.setter
    def eol_Expression127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_Expression__eol_Expression127", None)
        self.__eol_Expression127 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_SwitchCaseExpressionStatement126"):
                opp_val = getattr(old_value, "eol_SwitchCaseExpressionStatement126", None)
                if opp_val == self:
                    setattr(old_value, "eol_SwitchCaseExpressionStatement126", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_SwitchCaseExpressionStatement126"):
                opp_val = getattr(value, "eol_SwitchCaseExpressionStatement126", None)
                setattr(value, "eol_SwitchCaseExpressionStatement126", self)

    @property
    def eol_Expression72(self):
        return self.__eol_Expression72

    @eol_Expression72.setter
    def eol_Expression72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_Expression__eol_Expression72", None)
        self.__eol_Expression72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_FOLMethodCallExpression71"):
                opp_val = getattr(old_value, "eol_FOLMethodCallExpression71", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_FOLMethodCallExpression71"):
                opp_val = getattr(value, "eol_FOLMethodCallExpression71", None)
                if opp_val is None:
                    setattr(value, "eol_FOLMethodCallExpression71", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eol_Expression(self):
        return self.__eol_Expression

    @eol_Expression.setter
    def eol_Expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_Expression__eol_Expression", None)
        self.__eol_Expression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_ExpressionOrStatementBlock14"):
                opp_val = getattr(old_value, "eol_ExpressionOrStatementBlock14", None)
                if opp_val == self:
                    setattr(old_value, "eol_ExpressionOrStatementBlock14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_ExpressionOrStatementBlock14"):
                opp_val = getattr(value, "eol_ExpressionOrStatementBlock14", None)
                setattr(value, "eol_ExpressionOrStatementBlock14", self)

    @property
    def eol_Expression49(self):
        return self.__eol_Expression49

    @eol_Expression49.setter
    def eol_Expression49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_Expression__eol_Expression49", None)
        self.__eol_Expression49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_BinaryOperatorExpression48"):
                opp_val = getattr(old_value, "eol_BinaryOperatorExpression48", None)
                if opp_val == self:
                    setattr(old_value, "eol_BinaryOperatorExpression48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_BinaryOperatorExpression48"):
                opp_val = getattr(value, "eol_BinaryOperatorExpression48", None)
                setattr(value, "eol_BinaryOperatorExpression48", self)

    @property
    def eol_Expression59(self):
        return self.__eol_Expression59

    @eol_Expression59.setter
    def eol_Expression59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_Expression__eol_Expression59", None)
        self.__eol_Expression59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_MethodCallExpression"):
                opp_val = getattr(old_value, "eol_MethodCallExpression", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_MethodCallExpression"):
                opp_val = getattr(value, "eol_MethodCallExpression", None)
                if opp_val is None:
                    setattr(value, "eol_MethodCallExpression", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class eol_ExpressionOrStatementBlock:

    pass
class Block:

    pass
class eol_AnnotationBlock(Block):

    pass
class eol_Statement(ABC):

    pass
class eol_Block:

    pass
class EOLLibraryModule:

    pass
class eol_EOLModule(EOLLibraryModule):

    pass
class eol_OperationDefinition:

    pass
class eol_ModelDeclarationStatement(Statement):

    def __init__(self, resolvedIMetamodel: str, eol_ModelDeclarationStatement: "eol_EOLLibraryModule" = None, eol_ModelDeclarationStatement172: "eol_NameExpression" = None, eol_ModelDeclarationStatement175: set["eol_VariableDeclarationExpression"] = None, eol_ModelDeclarationStatement178: set["eol_ModelDeclarationParameter"] = None, eol_ModelDeclarationStatement169: "eol_VariableDeclarationExpression" = None, eol_ModelDeclarationStatement182: "eol_ModelElementType" = None):
        self.resolvedIMetamodel = resolvedIMetamodel
        self.eol_ModelDeclarationStatement = eol_ModelDeclarationStatement
        self.eol_ModelDeclarationStatement172 = eol_ModelDeclarationStatement172
        self.eol_ModelDeclarationStatement175 = eol_ModelDeclarationStatement175 if eol_ModelDeclarationStatement175 is not None else set()
        self.eol_ModelDeclarationStatement178 = eol_ModelDeclarationStatement178 if eol_ModelDeclarationStatement178 is not None else set()
        self.eol_ModelDeclarationStatement169 = eol_ModelDeclarationStatement169
        self.eol_ModelDeclarationStatement182 = eol_ModelDeclarationStatement182
        
    @property
    def resolvedIMetamodel(self) -> str:
        return self.__resolvedIMetamodel

    @resolvedIMetamodel.setter
    def resolvedIMetamodel(self, resolvedIMetamodel: str):
        self.__resolvedIMetamodel = resolvedIMetamodel

    @property
    def eol_ModelDeclarationStatement(self):
        return self.__eol_ModelDeclarationStatement

    @eol_ModelDeclarationStatement.setter
    def eol_ModelDeclarationStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_ModelDeclarationStatement__eol_ModelDeclarationStatement", None)
        self.__eol_ModelDeclarationStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_EOLLibraryModule2"):
                opp_val = getattr(old_value, "eol_EOLLibraryModule2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_EOLLibraryModule2"):
                opp_val = getattr(value, "eol_EOLLibraryModule2", None)
                if opp_val is None:
                    setattr(value, "eol_EOLLibraryModule2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eol_ModelDeclarationStatement172(self):
        return self.__eol_ModelDeclarationStatement172

    @eol_ModelDeclarationStatement172.setter
    def eol_ModelDeclarationStatement172(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_ModelDeclarationStatement__eol_ModelDeclarationStatement172", None)
        self.__eol_ModelDeclarationStatement172 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_NameExpression173"):
                opp_val = getattr(old_value, "eol_NameExpression173", None)
                if opp_val == self:
                    setattr(old_value, "eol_NameExpression173", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_NameExpression173"):
                opp_val = getattr(value, "eol_NameExpression173", None)
                setattr(value, "eol_NameExpression173", self)

    @property
    def eol_ModelDeclarationStatement169(self):
        return self.__eol_ModelDeclarationStatement169

    @eol_ModelDeclarationStatement169.setter
    def eol_ModelDeclarationStatement169(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_ModelDeclarationStatement__eol_ModelDeclarationStatement169", None)
        self.__eol_ModelDeclarationStatement169 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_VariableDeclarationExpression170"):
                opp_val = getattr(old_value, "eol_VariableDeclarationExpression170", None)
                if opp_val == self:
                    setattr(old_value, "eol_VariableDeclarationExpression170", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_VariableDeclarationExpression170"):
                opp_val = getattr(value, "eol_VariableDeclarationExpression170", None)
                setattr(value, "eol_VariableDeclarationExpression170", self)

    @property
    def eol_ModelDeclarationStatement178(self):
        return self.__eol_ModelDeclarationStatement178

    @eol_ModelDeclarationStatement178.setter
    def eol_ModelDeclarationStatement178(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_ModelDeclarationStatement__eol_ModelDeclarationStatement178", None)
        self.__eol_ModelDeclarationStatement178 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eol_ModelDeclarationParameter"):
                    opp_val = getattr(item, "eol_ModelDeclarationParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "eol_ModelDeclarationParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eol_ModelDeclarationParameter"):
                    opp_val = getattr(item, "eol_ModelDeclarationParameter", None)
                    
                    setattr(item, "eol_ModelDeclarationParameter", self)
                    

    @property
    def eol_ModelDeclarationStatement175(self):
        return self.__eol_ModelDeclarationStatement175

    @eol_ModelDeclarationStatement175.setter
    def eol_ModelDeclarationStatement175(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_ModelDeclarationStatement__eol_ModelDeclarationStatement175", None)
        self.__eol_ModelDeclarationStatement175 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eol_VariableDeclarationExpression176"):
                    opp_val = getattr(item, "eol_VariableDeclarationExpression176", None)
                    
                    if opp_val == self:
                        setattr(item, "eol_VariableDeclarationExpression176", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eol_VariableDeclarationExpression176"):
                    opp_val = getattr(item, "eol_VariableDeclarationExpression176", None)
                    
                    setattr(item, "eol_VariableDeclarationExpression176", self)
                    

    @property
    def eol_ModelDeclarationStatement182(self):
        return self.__eol_ModelDeclarationStatement182

    @eol_ModelDeclarationStatement182.setter
    def eol_ModelDeclarationStatement182(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_ModelDeclarationStatement__eol_ModelDeclarationStatement182", None)
        self.__eol_ModelDeclarationStatement182 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_ModelElementType"):
                opp_val = getattr(old_value, "eol_ModelElementType", None)
                if opp_val == self:
                    setattr(old_value, "eol_ModelElementType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_ModelElementType"):
                opp_val = getattr(value, "eol_ModelElementType", None)
                setattr(value, "eol_ModelElementType", self)

class eol_Import:

    def __init__(self, imported: str, eol_Import: "eol_EOLLibraryModule" = None, eol_Import7: "eol_EOLLibraryModule" = None):
        self.imported = imported
        self.eol_Import = eol_Import
        self.eol_Import7 = eol_Import7
        
    @property
    def imported(self) -> str:
        return self.__imported

    @imported.setter
    def imported(self, imported: str):
        self.__imported = imported

    @property
    def eol_Import7(self):
        return self.__eol_Import7

    @eol_Import7.setter
    def eol_Import7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_Import__eol_Import7", None)
        self.__eol_Import7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_EOLLibraryModule8"):
                opp_val = getattr(old_value, "eol_EOLLibraryModule8", None)
                if opp_val == self:
                    setattr(old_value, "eol_EOLLibraryModule8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_EOLLibraryModule8"):
                opp_val = getattr(value, "eol_EOLLibraryModule8", None)
                setattr(value, "eol_EOLLibraryModule8", self)

    @property
    def eol_Import(self):
        return self.__eol_Import

    @eol_Import.setter
    def eol_Import(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_Import__eol_Import", None)
        self.__eol_Import = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_EOLLibraryModule"):
                opp_val = getattr(old_value, "eol_EOLLibraryModule", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_EOLLibraryModule"):
                opp_val = getattr(value, "eol_EOLLibraryModule", None)
                if opp_val is None:
                    setattr(value, "eol_EOLLibraryModule", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
