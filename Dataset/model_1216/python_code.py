from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class PrimitiveType:

    pass
class eol_ComparablePrimitiveType(PrimitiveType):

    pass
class OrderedCollectionType:

    pass
class eol_SequenceType(OrderedCollectionType):

    pass
class UniqueCollectionType:

    pass
class eol_OrderedSetType(UniqueCollectionType, OrderedCollectionType):

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
class eol_BooleanType(PrimitiveType):

    pass
class eol_SummablePrimitiveType(PrimitiveType):

    pass
class AnyType:

    pass
class eol_PseudoType(AnyType):

    pass
class eol_PrimitiveType(AnyType):

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
    def resolvedIMetamodel(self) -> str:
        return self.__resolvedIMetamodel

    @resolvedIMetamodel.setter
    def resolvedIMetamodel(self, resolvedIMetamodel: str):
        self.__resolvedIMetamodel = resolvedIMetamodel

    @property
    def resolvedIPackage(self) -> str:
        return self.__resolvedIPackage

    @resolvedIPackage.setter
    def resolvedIPackage(self, resolvedIPackage: str):
        self.__resolvedIPackage = resolvedIPackage

    @property
    def modelElementType(self) -> str:
        return self.__modelElementType

    @modelElementType.setter
    def modelElementType(self, modelElementType: str):
        self.__modelElementType = modelElementType

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
            if hasattr(old_value, "eol_ModelDeclarationStatement191"):
                opp_val = getattr(old_value, "eol_ModelDeclarationStatement191", None)
                if opp_val == self:
                    setattr(old_value, "eol_ModelDeclarationStatement191", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_ModelDeclarationStatement191"):
                opp_val = getattr(value, "eol_ModelDeclarationStatement191", None)
                setattr(value, "eol_ModelDeclarationStatement191", self)

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

class eol_CollectionType(AnyType):

    pass
class eol_InvalidType(AnyType):

    pass
class eol_VoidType(AnyType):

    pass
class eol_NativeType(AnyType):

    pass
class eol_MapType(AnyType):

    pass
class PseudoType:

    pass
class eol_SelfContentType(PseudoType):

    pass
class eol_SelfType(PseudoType):

    pass
class AnnotationStatement:

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

    def __init__(self, declared: bool, eol_AnyType193: "eol_MapType" = None, eol_AnyType196: "eol_MapType" = None, eol_AnyType: set["eol_Type"] = None):
        self.declared = declared
        self.eol_AnyType193 = eol_AnyType193
        self.eol_AnyType196 = eol_AnyType196
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
                if hasattr(item, "eol_Type189"):
                    opp_val = getattr(item, "eol_Type189", None)
                    
                    if opp_val == self:
                        setattr(item, "eol_Type189", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eol_Type189"):
                    opp_val = getattr(item, "eol_Type189", None)
                    
                    setattr(item, "eol_Type189", self)
                    

    @property
    def eol_AnyType193(self):
        return self.__eol_AnyType193

    @eol_AnyType193.setter
    def eol_AnyType193(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_AnyType__eol_AnyType193", None)
        self.__eol_AnyType193 = value
        
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
    def eol_AnyType196(self):
        return self.__eol_AnyType196

    @eol_AnyType196.setter
    def eol_AnyType196(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_AnyType__eol_AnyType196", None)
        self.__eol_AnyType196 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_MapType195"):
                opp_val = getattr(old_value, "eol_MapType195", None)
                if opp_val == self:
                    setattr(old_value, "eol_MapType195", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_MapType195"):
                opp_val = getattr(value, "eol_MapType195", None)
                setattr(value, "eol_MapType195", self)

class eol_ExecutableAnnotationStatement(AnnotationStatement):

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
class Statement:

    pass
class eol_SwitchCaseStatement(Statement):

    pass
class eol_ContinueStatement(Statement):

    pass
class eol_ExpressionStatement(Statement):

    pass
class eol_WhileStatement(Statement):

    pass
class eol_ThrowStatement(Statement):

    pass
class eol_DeleteStatement(Statement):

    pass
class eol_ReturnStatement(Statement):

    pass
class eol_AbortStatement(Statement):

    pass
class eol_BreakAllStatement(Statement):

    pass
class eol_IfStatement(Statement):

    pass
class eol_SwitchStatement(Statement):

    pass
class eol_ForStatement(Statement):

    pass
class eol_BreakStatement(Statement):

    pass
class eol_AnnotationStatement(Statement):

    pass
class eol_AssignmentStatement(Statement):

    pass
class eol_TransactionStatement(Statement):

    pass
class eol_ExpressionList(CollectionInitialisationExpression):

    pass
class SummableExpression:

    pass
class ComparableExpression:

    pass
class eol_StringExpression(ComparableExpression, SummableExpression):

    def __init__(self, value: str, eol_StringExpression: "eol_SimpleAnnotationStatement" = None, eol_StringExpression198: "eol_NativeType" = None):
        self.value = value
        self.eol_StringExpression = eol_StringExpression
        self.eol_StringExpression198 = eol_StringExpression198
        
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
    def eol_StringExpression198(self):
        return self.__eol_StringExpression198

    @eol_StringExpression198.setter
    def eol_StringExpression198(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_StringExpression__eol_StringExpression198", None)
        self.__eol_StringExpression198 = value
        
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
class eol_BooleanExpression(PrimitiveExpression):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class eol_SummableExpression(PrimitiveExpression):

    pass
class eol_ComparableExpression(PrimitiveExpression):

    pass
class OrderedCollection:

    pass
class eol_SequenceExpression(OrderedCollection):

    pass
class UniqueCollection:

    pass
class eol_OrderedSetExpression(OrderedCollection, UniqueCollection):

    pass
class eol_SetExpression(UniqueCollection):

    pass
class CollectionExpression:

    pass
class eol_OrderedCollection(CollectionExpression):

    pass
class eol_UniqueCollection(CollectionExpression):

    pass
class eol_BagExpression(CollectionExpression):

    pass
class eol_IntegerExpression(ComparableExpression, SummableExpression):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class eol_RealExpression(ComparableExpression, SummableExpression):

    def __init__(self, value: float):
        self.value = value
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

class KeyValueExpression:

    pass
class eol_ModelDeclarationParameter(KeyValueExpression):

    pass
class VariableDeclarationExpression:

    pass
class ComparisonOperatorExpression:

    pass
class eol_LessThanOperatorExpression(ComparisonOperatorExpression):

    pass
class eol_GreaterThanOperatorExpression(ComparisonOperatorExpression):

    pass
class eol_NotEqualsOperatorExpression(ComparisonOperatorExpression):

    pass
class eol_LessThanOrEqualToOperatorExpression(ComparisonOperatorExpression):

    pass
class eol_EqualsOperatorExpression(ComparisonOperatorExpression):

    pass
class eol_GreaterThanOrEqualToOperatorExpression(ComparisonOperatorExpression):

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
class FeatureCallExpression:

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
            if hasattr(old_value, "eol_NameExpression76"):
                opp_val = getattr(old_value, "eol_NameExpression76", None)
                if opp_val == self:
                    setattr(old_value, "eol_NameExpression76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_NameExpression76"):
                opp_val = getattr(value, "eol_NameExpression76", None)
                setattr(value, "eol_NameExpression76", self)

class eol_FOLMethodCallExpression(FeatureCallExpression):

    pass
class eol_MethodCallExpression(FeatureCallExpression):

    pass
class UnaryOperatorExpression:

    pass
class eol_NegativeOperatorExpression(UnaryOperatorExpression):

    pass
class eol_NotOperatorExpression(UnaryOperatorExpression):

    pass
class OperatorExpression:

    pass
class eol_UnaryOperatorExpression(OperatorExpression):

    pass
class Expression:

    pass
class eol_KeyValueExpression(Expression):

    pass
class eol_EnumerationLiteralExpression(Expression):

    pass
class eol_CollectionExpression(Expression):

    pass
class eol_PrimitiveExpression(Expression):

    pass
class eol_CollectionInitialisationExpression(Expression):

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
            if hasattr(old_value, "eol_Expression66"):
                opp_val = getattr(old_value, "eol_Expression66", None)
                if opp_val == self:
                    setattr(old_value, "eol_Expression66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_Expression66"):
                opp_val = getattr(value, "eol_Expression66", None)
                setattr(value, "eol_Expression66", self)

class eol_MapExpression(Expression):

    pass
class eol_NewExpression(Expression):

    pass
class eol_OperatorExpression(Expression):

    pass
class LogicalOperatorExpression:

    pass
class eol_OrOperatorExpression(LogicalOperatorExpression):

    pass
class eol_ImpliesOperatorExpression(LogicalOperatorExpression):

    pass
class eol_XorOperatorExpression(LogicalOperatorExpression):

    pass
class eol_AndOperatorExpression(LogicalOperatorExpression):

    pass
class BinaryOperatorExpression:

    pass
class eol_ComparisonOperatorExpression(BinaryOperatorExpression):

    pass
class eol_ArithmeticOperatorExpression(BinaryOperatorExpression):

    pass
class eol_LogicalOperatorExpression(BinaryOperatorExpression):

    pass
class eol_BinaryOperatorExpression(OperatorExpression):

    pass
class eol_VariableDeclarationExpression(Expression):

    def __init__(self, create: bool, eol_VariableDeclarationExpression: "eol_OperationDefinition" = None, eol_VariableDeclarationExpression45: "eol_OperationDefinition" = None, eol_VariableDeclarationExpression60: "eol_NameExpression" = None, eol_VariableDeclarationExpression63: set["eol_NameExpression"] = None, eol_VariableDeclarationExpression179: "eol_ModelDeclarationStatement" = None, eol_VariableDeclarationExpression185: "eol_ModelDeclarationStatement" = None):
        self.create = create
        self.eol_VariableDeclarationExpression = eol_VariableDeclarationExpression
        self.eol_VariableDeclarationExpression45 = eol_VariableDeclarationExpression45
        self.eol_VariableDeclarationExpression60 = eol_VariableDeclarationExpression60
        self.eol_VariableDeclarationExpression63 = eol_VariableDeclarationExpression63 if eol_VariableDeclarationExpression63 is not None else set()
        self.eol_VariableDeclarationExpression179 = eol_VariableDeclarationExpression179
        self.eol_VariableDeclarationExpression185 = eol_VariableDeclarationExpression185
        
    @property
    def create(self) -> bool:
        return self.__create

    @create.setter
    def create(self, create: bool):
        self.__create = create

    @property
    def eol_VariableDeclarationExpression63(self):
        return self.__eol_VariableDeclarationExpression63

    @eol_VariableDeclarationExpression63.setter
    def eol_VariableDeclarationExpression63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_VariableDeclarationExpression__eol_VariableDeclarationExpression63", None)
        self.__eol_VariableDeclarationExpression63 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eol_NameExpression64"):
                    opp_val = getattr(item, "eol_NameExpression64", None)
                    
                    if opp_val == self:
                        setattr(item, "eol_NameExpression64", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eol_NameExpression64"):
                    opp_val = getattr(item, "eol_NameExpression64", None)
                    
                    setattr(item, "eol_NameExpression64", self)
                    

    @property
    def eol_VariableDeclarationExpression179(self):
        return self.__eol_VariableDeclarationExpression179

    @eol_VariableDeclarationExpression179.setter
    def eol_VariableDeclarationExpression179(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_VariableDeclarationExpression__eol_VariableDeclarationExpression179", None)
        self.__eol_VariableDeclarationExpression179 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_ModelDeclarationStatement178"):
                opp_val = getattr(old_value, "eol_ModelDeclarationStatement178", None)
                if opp_val == self:
                    setattr(old_value, "eol_ModelDeclarationStatement178", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_ModelDeclarationStatement178"):
                opp_val = getattr(value, "eol_ModelDeclarationStatement178", None)
                setattr(value, "eol_ModelDeclarationStatement178", self)

    @property
    def eol_VariableDeclarationExpression45(self):
        return self.__eol_VariableDeclarationExpression45

    @eol_VariableDeclarationExpression45.setter
    def eol_VariableDeclarationExpression45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_VariableDeclarationExpression__eol_VariableDeclarationExpression45", None)
        self.__eol_VariableDeclarationExpression45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_OperationDefinition44"):
                opp_val = getattr(old_value, "eol_OperationDefinition44", None)
                if opp_val == self:
                    setattr(old_value, "eol_OperationDefinition44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_OperationDefinition44"):
                opp_val = getattr(value, "eol_OperationDefinition44", None)
                setattr(value, "eol_OperationDefinition44", self)

    @property
    def eol_VariableDeclarationExpression185(self):
        return self.__eol_VariableDeclarationExpression185

    @eol_VariableDeclarationExpression185.setter
    def eol_VariableDeclarationExpression185(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_VariableDeclarationExpression__eol_VariableDeclarationExpression185", None)
        self.__eol_VariableDeclarationExpression185 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_ModelDeclarationStatement184"):
                opp_val = getattr(old_value, "eol_ModelDeclarationStatement184", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_ModelDeclarationStatement184"):
                opp_val = getattr(value, "eol_ModelDeclarationStatement184", None)
                if opp_val is None:
                    setattr(value, "eol_ModelDeclarationStatement184", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eol_VariableDeclarationExpression60(self):
        return self.__eol_VariableDeclarationExpression60

    @eol_VariableDeclarationExpression60.setter
    def eol_VariableDeclarationExpression60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_VariableDeclarationExpression__eol_VariableDeclarationExpression60", None)
        self.__eol_VariableDeclarationExpression60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_NameExpression61"):
                opp_val = getattr(old_value, "eol_NameExpression61", None)
                if opp_val == self:
                    setattr(old_value, "eol_NameExpression61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_NameExpression61"):
                opp_val = getattr(value, "eol_NameExpression61", None)
                setattr(value, "eol_NameExpression61", self)

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
            if hasattr(old_value, "eol_OperationDefinition42"):
                opp_val = getattr(old_value, "eol_OperationDefinition42", None)
                if opp_val == self:
                    setattr(old_value, "eol_OperationDefinition42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_OperationDefinition42"):
                opp_val = getattr(value, "eol_OperationDefinition42", None)
                setattr(value, "eol_OperationDefinition42", self)

class eol_FormalParameterExpression(VariableDeclarationExpression):

    pass
class eol_NameExpression(Expression):

    def __init__(self, name: str, resolvedContent: str, isType: bool, eol_NameExpression: "eol_OperationDefinition" = None, eol_NameExpression71: "eol_MethodCallExpression" = None, eol_NameExpression61: "eol_VariableDeclarationExpression" = None, eol_NameExpression64: "eol_VariableDeclarationExpression" = None, eol_NameExpression94: "eol_NewExpression" = None, eol_NameExpression76: "eol_PropertyCallExpression" = None, eol_NameExpression84: "eol_FOLMethodCallExpression" = None, eol_NameExpression120: "eol_TransactionStatement" = None, eol_NameExpression105: "eol_EnumerationLiteralExpression" = None, eol_NameExpression108: "eol_EnumerationLiteralExpression" = None, eol_NameExpression111: "eol_EnumerationLiteralExpression" = None, eol_NameExpression182: "eol_ModelDeclarationStatement" = None, eol_NameExpression173: "eol_AnnotationStatement" = None):
        self.name = name
        self.resolvedContent = resolvedContent
        self.isType = isType
        self.eol_NameExpression = eol_NameExpression
        self.eol_NameExpression71 = eol_NameExpression71
        self.eol_NameExpression61 = eol_NameExpression61
        self.eol_NameExpression64 = eol_NameExpression64
        self.eol_NameExpression94 = eol_NameExpression94
        self.eol_NameExpression76 = eol_NameExpression76
        self.eol_NameExpression84 = eol_NameExpression84
        self.eol_NameExpression120 = eol_NameExpression120
        self.eol_NameExpression105 = eol_NameExpression105
        self.eol_NameExpression108 = eol_NameExpression108
        self.eol_NameExpression111 = eol_NameExpression111
        self.eol_NameExpression182 = eol_NameExpression182
        self.eol_NameExpression173 = eol_NameExpression173
        
    @property
    def isType(self) -> bool:
        return self.__isType

    @isType.setter
    def isType(self, isType: bool):
        self.__isType = isType

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
    def eol_NameExpression120(self):
        return self.__eol_NameExpression120

    @eol_NameExpression120.setter
    def eol_NameExpression120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_NameExpression__eol_NameExpression120", None)
        self.__eol_NameExpression120 = value
        
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
    def eol_NameExpression64(self):
        return self.__eol_NameExpression64

    @eol_NameExpression64.setter
    def eol_NameExpression64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_NameExpression__eol_NameExpression64", None)
        self.__eol_NameExpression64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_VariableDeclarationExpression63"):
                opp_val = getattr(old_value, "eol_VariableDeclarationExpression63", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_VariableDeclarationExpression63"):
                opp_val = getattr(value, "eol_VariableDeclarationExpression63", None)
                if opp_val is None:
                    setattr(value, "eol_VariableDeclarationExpression63", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eol_NameExpression61(self):
        return self.__eol_NameExpression61

    @eol_NameExpression61.setter
    def eol_NameExpression61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_NameExpression__eol_NameExpression61", None)
        self.__eol_NameExpression61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_VariableDeclarationExpression60"):
                opp_val = getattr(old_value, "eol_VariableDeclarationExpression60", None)
                if opp_val == self:
                    setattr(old_value, "eol_VariableDeclarationExpression60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_VariableDeclarationExpression60"):
                opp_val = getattr(value, "eol_VariableDeclarationExpression60", None)
                setattr(value, "eol_VariableDeclarationExpression60", self)

    @property
    def eol_NameExpression182(self):
        return self.__eol_NameExpression182

    @eol_NameExpression182.setter
    def eol_NameExpression182(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_NameExpression__eol_NameExpression182", None)
        self.__eol_NameExpression182 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_ModelDeclarationStatement181"):
                opp_val = getattr(old_value, "eol_ModelDeclarationStatement181", None)
                if opp_val == self:
                    setattr(old_value, "eol_ModelDeclarationStatement181", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_ModelDeclarationStatement181"):
                opp_val = getattr(value, "eol_ModelDeclarationStatement181", None)
                setattr(value, "eol_ModelDeclarationStatement181", self)

    @property
    def eol_NameExpression84(self):
        return self.__eol_NameExpression84

    @eol_NameExpression84.setter
    def eol_NameExpression84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_NameExpression__eol_NameExpression84", None)
        self.__eol_NameExpression84 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_FOLMethodCallExpression83"):
                opp_val = getattr(old_value, "eol_FOLMethodCallExpression83", None)
                if opp_val == self:
                    setattr(old_value, "eol_FOLMethodCallExpression83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_FOLMethodCallExpression83"):
                opp_val = getattr(value, "eol_FOLMethodCallExpression83", None)
                setattr(value, "eol_FOLMethodCallExpression83", self)

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
            if hasattr(old_value, "eol_MethodCallExpression70"):
                opp_val = getattr(old_value, "eol_MethodCallExpression70", None)
                if opp_val == self:
                    setattr(old_value, "eol_MethodCallExpression70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_MethodCallExpression70"):
                opp_val = getattr(value, "eol_MethodCallExpression70", None)
                setattr(value, "eol_MethodCallExpression70", self)

    @property
    def eol_NameExpression105(self):
        return self.__eol_NameExpression105

    @eol_NameExpression105.setter
    def eol_NameExpression105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_NameExpression__eol_NameExpression105", None)
        self.__eol_NameExpression105 = value
        
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
    def eol_NameExpression173(self):
        return self.__eol_NameExpression173

    @eol_NameExpression173.setter
    def eol_NameExpression173(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_NameExpression__eol_NameExpression173", None)
        self.__eol_NameExpression173 = value
        
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
    def eol_NameExpression111(self):
        return self.__eol_NameExpression111

    @eol_NameExpression111.setter
    def eol_NameExpression111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_NameExpression__eol_NameExpression111", None)
        self.__eol_NameExpression111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_EnumerationLiteralExpression110"):
                opp_val = getattr(old_value, "eol_EnumerationLiteralExpression110", None)
                if opp_val == self:
                    setattr(old_value, "eol_EnumerationLiteralExpression110", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_EnumerationLiteralExpression110"):
                opp_val = getattr(value, "eol_EnumerationLiteralExpression110", None)
                setattr(value, "eol_EnumerationLiteralExpression110", self)

    @property
    def eol_NameExpression94(self):
        return self.__eol_NameExpression94

    @eol_NameExpression94.setter
    def eol_NameExpression94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_NameExpression__eol_NameExpression94", None)
        self.__eol_NameExpression94 = value
        
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
    def eol_NameExpression108(self):
        return self.__eol_NameExpression108

    @eol_NameExpression108.setter
    def eol_NameExpression108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_NameExpression__eol_NameExpression108", None)
        self.__eol_NameExpression108 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_EnumerationLiteralExpression107"):
                opp_val = getattr(old_value, "eol_EnumerationLiteralExpression107", None)
                if opp_val == self:
                    setattr(old_value, "eol_EnumerationLiteralExpression107", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_EnumerationLiteralExpression107"):
                opp_val = getattr(value, "eol_EnumerationLiteralExpression107", None)
                setattr(value, "eol_EnumerationLiteralExpression107", self)

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
            if hasattr(old_value, "eol_OperationDefinition38"):
                opp_val = getattr(old_value, "eol_OperationDefinition38", None)
                if opp_val == self:
                    setattr(old_value, "eol_OperationDefinition38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_OperationDefinition38"):
                opp_val = getattr(value, "eol_OperationDefinition38", None)
                setattr(value, "eol_OperationDefinition38", self)

    @property
    def eol_NameExpression76(self):
        return self.__eol_NameExpression76

    @eol_NameExpression76.setter
    def eol_NameExpression76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_NameExpression__eol_NameExpression76", None)
        self.__eol_NameExpression76 = value
        
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

class Block:

    pass
class eol_AnnotationBlock(Block):

    pass
class EOLLibraryModule:

    pass
class eol_EOLModule(EOLLibraryModule):

    pass
class eol_ModelDeclarationStatement(Statement):

    def __init__(self, resolvedIMetamodel: str, eol_ModelDeclarationStatement: "eol_EOLLibraryModule" = None, eol_ModelDeclarationStatement178: "eol_VariableDeclarationExpression" = None, eol_ModelDeclarationStatement181: "eol_NameExpression" = None, eol_ModelDeclarationStatement184: set["eol_VariableDeclarationExpression"] = None, eol_ModelDeclarationStatement187: set["eol_ModelDeclarationParameter"] = None, eol_ModelDeclarationStatement191: "eol_ModelElementType" = None):
        self.resolvedIMetamodel = resolvedIMetamodel
        self.eol_ModelDeclarationStatement = eol_ModelDeclarationStatement
        self.eol_ModelDeclarationStatement178 = eol_ModelDeclarationStatement178
        self.eol_ModelDeclarationStatement181 = eol_ModelDeclarationStatement181
        self.eol_ModelDeclarationStatement184 = eol_ModelDeclarationStatement184 if eol_ModelDeclarationStatement184 is not None else set()
        self.eol_ModelDeclarationStatement187 = eol_ModelDeclarationStatement187 if eol_ModelDeclarationStatement187 is not None else set()
        self.eol_ModelDeclarationStatement191 = eol_ModelDeclarationStatement191
        
    @property
    def resolvedIMetamodel(self) -> str:
        return self.__resolvedIMetamodel

    @resolvedIMetamodel.setter
    def resolvedIMetamodel(self, resolvedIMetamodel: str):
        self.__resolvedIMetamodel = resolvedIMetamodel

    @property
    def eol_ModelDeclarationStatement184(self):
        return self.__eol_ModelDeclarationStatement184

    @eol_ModelDeclarationStatement184.setter
    def eol_ModelDeclarationStatement184(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_ModelDeclarationStatement__eol_ModelDeclarationStatement184", None)
        self.__eol_ModelDeclarationStatement184 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eol_VariableDeclarationExpression185"):
                    opp_val = getattr(item, "eol_VariableDeclarationExpression185", None)
                    
                    if opp_val == self:
                        setattr(item, "eol_VariableDeclarationExpression185", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eol_VariableDeclarationExpression185"):
                    opp_val = getattr(item, "eol_VariableDeclarationExpression185", None)
                    
                    setattr(item, "eol_VariableDeclarationExpression185", self)
                    

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
            if hasattr(old_value, "eol_EOLLibraryModule11"):
                opp_val = getattr(old_value, "eol_EOLLibraryModule11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_EOLLibraryModule11"):
                opp_val = getattr(value, "eol_EOLLibraryModule11", None)
                if opp_val is None:
                    setattr(value, "eol_EOLLibraryModule11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eol_ModelDeclarationStatement187(self):
        return self.__eol_ModelDeclarationStatement187

    @eol_ModelDeclarationStatement187.setter
    def eol_ModelDeclarationStatement187(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_ModelDeclarationStatement__eol_ModelDeclarationStatement187", None)
        self.__eol_ModelDeclarationStatement187 = value if value is not None else set()
        
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
    def eol_ModelDeclarationStatement181(self):
        return self.__eol_ModelDeclarationStatement181

    @eol_ModelDeclarationStatement181.setter
    def eol_ModelDeclarationStatement181(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_ModelDeclarationStatement__eol_ModelDeclarationStatement181", None)
        self.__eol_ModelDeclarationStatement181 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_NameExpression182"):
                opp_val = getattr(old_value, "eol_NameExpression182", None)
                if opp_val == self:
                    setattr(old_value, "eol_NameExpression182", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_NameExpression182"):
                opp_val = getattr(value, "eol_NameExpression182", None)
                setattr(value, "eol_NameExpression182", self)

    @property
    def eol_ModelDeclarationStatement191(self):
        return self.__eol_ModelDeclarationStatement191

    @eol_ModelDeclarationStatement191.setter
    def eol_ModelDeclarationStatement191(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_ModelDeclarationStatement__eol_ModelDeclarationStatement191", None)
        self.__eol_ModelDeclarationStatement191 = value
        
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

    @property
    def eol_ModelDeclarationStatement178(self):
        return self.__eol_ModelDeclarationStatement178

    @eol_ModelDeclarationStatement178.setter
    def eol_ModelDeclarationStatement178(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_ModelDeclarationStatement__eol_ModelDeclarationStatement178", None)
        self.__eol_ModelDeclarationStatement178 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_VariableDeclarationExpression179"):
                opp_val = getattr(old_value, "eol_VariableDeclarationExpression179", None)
                if opp_val == self:
                    setattr(old_value, "eol_VariableDeclarationExpression179", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_VariableDeclarationExpression179"):
                opp_val = getattr(value, "eol_VariableDeclarationExpression179", None)
                setattr(value, "eol_VariableDeclarationExpression179", self)

class eol_TextPosition:

    def __init__(self, line: int, column: int, eol_TextPosition8: "eol_TextRegion" = None, eol_TextPosition: "eol_TextRegion" = None):
        self.line = line
        self.column = column
        self.eol_TextPosition8 = eol_TextPosition8
        self.eol_TextPosition = eol_TextPosition
        
    @property
    def line(self) -> int:
        return self.__line

    @line.setter
    def line(self, line: int):
        self.__line = line

    @property
    def column(self) -> int:
        return self.__column

    @column.setter
    def column(self, column: int):
        self.__column = column

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
class eol_EOLElement:

    def __init__(self, uri: str, eol_EOLElement: "eol_EOLElement" = None, eol_EOLElement0: "eol_EOLElement" = None, eol_EOLElement3: "eol_TextRegion" = None):
        self.uri = uri
        self.eol_EOLElement = eol_EOLElement
        self.eol_EOLElement0 = eol_EOLElement0
        self.eol_EOLElement3 = eol_EOLElement3
        
    @property
    def uri(self) -> str:
        return self.__uri

    @uri.setter
    def uri(self, uri: str):
        self.__uri = uri

    @property
    def eol_EOLElement(self):
        return self.__eol_EOLElement

    @eol_EOLElement.setter
    def eol_EOLElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_EOLElement__eol_EOLElement", None)
        self.__eol_EOLElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_EOLElement0"):
                opp_val = getattr(old_value, "eol_EOLElement0", None)
                if opp_val == self:
                    setattr(old_value, "eol_EOLElement0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_EOLElement0"):
                opp_val = getattr(value, "eol_EOLElement0", None)
                setattr(value, "eol_EOLElement0", self)

    @property
    def eol_EOLElement3(self):
        return self.__eol_EOLElement3

    @eol_EOLElement3.setter
    def eol_EOLElement3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_EOLElement__eol_EOLElement3", None)
        self.__eol_EOLElement3 = value
        
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
    def eol_EOLElement0(self):
        return self.__eol_EOLElement0

    @eol_EOLElement0.setter
    def eol_EOLElement0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_EOLElement__eol_EOLElement0", None)
        self.__eol_EOLElement0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_EOLElement"):
                opp_val = getattr(old_value, "eol_EOLElement", None)
                if opp_val == self:
                    setattr(old_value, "eol_EOLElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_EOLElement"):
                opp_val = getattr(value, "eol_EOLElement", None)
                setattr(value, "eol_EOLElement", self)

class EOLElement:

    pass
class eol_Import(EOLElement):

    def __init__(self, imported: str, eol_Import: "eol_EOLLibraryModule" = None, eol_Import16: "eol_EOLLibraryModule" = None):
        self.imported = imported
        self.eol_Import = eol_Import
        self.eol_Import16 = eol_Import16
        
    @property
    def imported(self) -> str:
        return self.__imported

    @imported.setter
    def imported(self, imported: str):
        self.__imported = imported

    @property
    def eol_Import16(self):
        return self.__eol_Import16

    @eol_Import16.setter
    def eol_Import16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_Import__eol_Import16", None)
        self.__eol_Import16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_EOLLibraryModule17"):
                opp_val = getattr(old_value, "eol_EOLLibraryModule17", None)
                if opp_val == self:
                    setattr(old_value, "eol_EOLLibraryModule17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_EOLLibraryModule17"):
                opp_val = getattr(value, "eol_EOLLibraryModule17", None)
                setattr(value, "eol_EOLLibraryModule17", self)

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

class eol_Expression(EOLElement):

    def __init__(self, inBrackets: bool, eol_Expression: "eol_ExpressionOrStatementBlock" = None, eol_Expression26: "eol_ExpressionOrStatementBlock" = None, eol_Expression55: "eol_BinaryOperatorExpression" = None, eol_Expression58: "eol_BinaryOperatorExpression" = None, eol_Expression50: "eol_Type" = None, eol_Expression53: "eol_UnaryOperatorExpression" = None, eol_Expression66: "eol_FeatureCallExpression" = None, eol_Expression68: "eol_MethodCallExpression" = None, eol_Expression97: "eol_NewExpression" = None, eol_Expression81: "eol_FOLMethodCallExpression" = None, eol_Expression89: "eol_KeyValueExpression" = None, eol_Expression92: "eol_KeyValueExpression" = None, eol_Expression101: "eol_CollectionExpression" = None, eol_Expression118: "eol_ExpressionList" = None, eol_Expression113: "eol_ExpressionRange" = None, eol_Expression116: "eol_ExpressionRange" = None, eol_Expression136: "eol_SwitchCaseExpressionStatement" = None, eol_Expression138: "eol_IfStatement" = None, eol_Expression125: "eol_ExpressionStatement" = None, eol_Expression127: "eol_SwitchStatement" = None, eol_Expression162: "eol_ReturnStatement" = None, eol_Expression164: "eol_ThrowStatement" = None, eol_Expression166: "eol_DeleteStatement" = None, eol_Expression168: "eol_AssignmentStatement" = None, eol_Expression152: "eol_ForStatement" = None, eol_Expression157: "eol_WhileStatement" = None, eol_Expression176: "eol_ExecutableAnnotationStatement" = None, eol_Expression171: "eol_AssignmentStatement" = None):
        self.inBrackets = inBrackets
        self.eol_Expression = eol_Expression
        self.eol_Expression26 = eol_Expression26
        self.eol_Expression55 = eol_Expression55
        self.eol_Expression58 = eol_Expression58
        self.eol_Expression50 = eol_Expression50
        self.eol_Expression53 = eol_Expression53
        self.eol_Expression66 = eol_Expression66
        self.eol_Expression68 = eol_Expression68
        self.eol_Expression97 = eol_Expression97
        self.eol_Expression81 = eol_Expression81
        self.eol_Expression89 = eol_Expression89
        self.eol_Expression92 = eol_Expression92
        self.eol_Expression101 = eol_Expression101
        self.eol_Expression118 = eol_Expression118
        self.eol_Expression113 = eol_Expression113
        self.eol_Expression116 = eol_Expression116
        self.eol_Expression136 = eol_Expression136
        self.eol_Expression138 = eol_Expression138
        self.eol_Expression125 = eol_Expression125
        self.eol_Expression127 = eol_Expression127
        self.eol_Expression162 = eol_Expression162
        self.eol_Expression164 = eol_Expression164
        self.eol_Expression166 = eol_Expression166
        self.eol_Expression168 = eol_Expression168
        self.eol_Expression152 = eol_Expression152
        self.eol_Expression157 = eol_Expression157
        self.eol_Expression176 = eol_Expression176
        self.eol_Expression171 = eol_Expression171
        
    @property
    def inBrackets(self) -> bool:
        return self.__inBrackets

    @inBrackets.setter
    def inBrackets(self, inBrackets: bool):
        self.__inBrackets = inBrackets

    @property
    def eol_Expression164(self):
        return self.__eol_Expression164

    @eol_Expression164.setter
    def eol_Expression164(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_Expression__eol_Expression164", None)
        self.__eol_Expression164 = value
        
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
    def eol_Expression66(self):
        return self.__eol_Expression66

    @eol_Expression66.setter
    def eol_Expression66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_Expression__eol_Expression66", None)
        self.__eol_Expression66 = value
        
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
    def eol_Expression157(self):
        return self.__eol_Expression157

    @eol_Expression157.setter
    def eol_Expression157(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_Expression__eol_Expression157", None)
        self.__eol_Expression157 = value
        
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
    def eol_Expression152(self):
        return self.__eol_Expression152

    @eol_Expression152.setter
    def eol_Expression152(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_Expression__eol_Expression152", None)
        self.__eol_Expression152 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_ForStatement151"):
                opp_val = getattr(old_value, "eol_ForStatement151", None)
                if opp_val == self:
                    setattr(old_value, "eol_ForStatement151", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_ForStatement151"):
                opp_val = getattr(value, "eol_ForStatement151", None)
                setattr(value, "eol_ForStatement151", self)

    @property
    def eol_Expression138(self):
        return self.__eol_Expression138

    @eol_Expression138.setter
    def eol_Expression138(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_Expression__eol_Expression138", None)
        self.__eol_Expression138 = value
        
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
    def eol_Expression101(self):
        return self.__eol_Expression101

    @eol_Expression101.setter
    def eol_Expression101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_Expression__eol_Expression101", None)
        self.__eol_Expression101 = value
        
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
    def eol_Expression55(self):
        return self.__eol_Expression55

    @eol_Expression55.setter
    def eol_Expression55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_Expression__eol_Expression55", None)
        self.__eol_Expression55 = value
        
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
    def eol_Expression162(self):
        return self.__eol_Expression162

    @eol_Expression162.setter
    def eol_Expression162(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_Expression__eol_Expression162", None)
        self.__eol_Expression162 = value
        
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
    def eol_Expression136(self):
        return self.__eol_Expression136

    @eol_Expression136.setter
    def eol_Expression136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_Expression__eol_Expression136", None)
        self.__eol_Expression136 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_SwitchCaseExpressionStatement135"):
                opp_val = getattr(old_value, "eol_SwitchCaseExpressionStatement135", None)
                if opp_val == self:
                    setattr(old_value, "eol_SwitchCaseExpressionStatement135", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_SwitchCaseExpressionStatement135"):
                opp_val = getattr(value, "eol_SwitchCaseExpressionStatement135", None)
                setattr(value, "eol_SwitchCaseExpressionStatement135", self)

    @property
    def eol_Expression97(self):
        return self.__eol_Expression97

    @eol_Expression97.setter
    def eol_Expression97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_Expression__eol_Expression97", None)
        self.__eol_Expression97 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_NewExpression96"):
                opp_val = getattr(old_value, "eol_NewExpression96", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_NewExpression96"):
                opp_val = getattr(value, "eol_NewExpression96", None)
                if opp_val is None:
                    setattr(value, "eol_NewExpression96", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eol_Expression68(self):
        return self.__eol_Expression68

    @eol_Expression68.setter
    def eol_Expression68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_Expression__eol_Expression68", None)
        self.__eol_Expression68 = value
        
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
            if hasattr(old_value, "eol_ExpressionRange115"):
                opp_val = getattr(old_value, "eol_ExpressionRange115", None)
                if opp_val == self:
                    setattr(old_value, "eol_ExpressionRange115", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_ExpressionRange115"):
                opp_val = getattr(value, "eol_ExpressionRange115", None)
                setattr(value, "eol_ExpressionRange115", self)

    @property
    def eol_Expression50(self):
        return self.__eol_Expression50

    @eol_Expression50.setter
    def eol_Expression50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_Expression__eol_Expression50", None)
        self.__eol_Expression50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_Type51"):
                opp_val = getattr(old_value, "eol_Type51", None)
                if opp_val == self:
                    setattr(old_value, "eol_Type51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_Type51"):
                opp_val = getattr(value, "eol_Type51", None)
                setattr(value, "eol_Type51", self)

    @property
    def eol_Expression53(self):
        return self.__eol_Expression53

    @eol_Expression53.setter
    def eol_Expression53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_Expression__eol_Expression53", None)
        self.__eol_Expression53 = value
        
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
    def eol_Expression58(self):
        return self.__eol_Expression58

    @eol_Expression58.setter
    def eol_Expression58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_Expression__eol_Expression58", None)
        self.__eol_Expression58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_BinaryOperatorExpression57"):
                opp_val = getattr(old_value, "eol_BinaryOperatorExpression57", None)
                if opp_val == self:
                    setattr(old_value, "eol_BinaryOperatorExpression57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_BinaryOperatorExpression57"):
                opp_val = getattr(value, "eol_BinaryOperatorExpression57", None)
                setattr(value, "eol_BinaryOperatorExpression57", self)

    @property
    def eol_Expression125(self):
        return self.__eol_Expression125

    @eol_Expression125.setter
    def eol_Expression125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_Expression__eol_Expression125", None)
        self.__eol_Expression125 = value
        
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
    def eol_Expression89(self):
        return self.__eol_Expression89

    @eol_Expression89.setter
    def eol_Expression89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_Expression__eol_Expression89", None)
        self.__eol_Expression89 = value
        
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
    def eol_Expression176(self):
        return self.__eol_Expression176

    @eol_Expression176.setter
    def eol_Expression176(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_Expression__eol_Expression176", None)
        self.__eol_Expression176 = value
        
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
    def eol_Expression(self):
        return self.__eol_Expression

    @eol_Expression.setter
    def eol_Expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_Expression__eol_Expression", None)
        self.__eol_Expression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_ExpressionOrStatementBlock23"):
                opp_val = getattr(old_value, "eol_ExpressionOrStatementBlock23", None)
                if opp_val == self:
                    setattr(old_value, "eol_ExpressionOrStatementBlock23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_ExpressionOrStatementBlock23"):
                opp_val = getattr(value, "eol_ExpressionOrStatementBlock23", None)
                setattr(value, "eol_ExpressionOrStatementBlock23", self)

    @property
    def eol_Expression166(self):
        return self.__eol_Expression166

    @eol_Expression166.setter
    def eol_Expression166(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_Expression__eol_Expression166", None)
        self.__eol_Expression166 = value
        
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
    def eol_Expression92(self):
        return self.__eol_Expression92

    @eol_Expression92.setter
    def eol_Expression92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_Expression__eol_Expression92", None)
        self.__eol_Expression92 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_KeyValueExpression91"):
                opp_val = getattr(old_value, "eol_KeyValueExpression91", None)
                if opp_val == self:
                    setattr(old_value, "eol_KeyValueExpression91", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_KeyValueExpression91"):
                opp_val = getattr(value, "eol_KeyValueExpression91", None)
                setattr(value, "eol_KeyValueExpression91", self)

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
    def eol_Expression113(self):
        return self.__eol_Expression113

    @eol_Expression113.setter
    def eol_Expression113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_Expression__eol_Expression113", None)
        self.__eol_Expression113 = value
        
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
    def eol_Expression171(self):
        return self.__eol_Expression171

    @eol_Expression171.setter
    def eol_Expression171(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_Expression__eol_Expression171", None)
        self.__eol_Expression171 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_AssignmentStatement170"):
                opp_val = getattr(old_value, "eol_AssignmentStatement170", None)
                if opp_val == self:
                    setattr(old_value, "eol_AssignmentStatement170", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_AssignmentStatement170"):
                opp_val = getattr(value, "eol_AssignmentStatement170", None)
                setattr(value, "eol_AssignmentStatement170", self)

    @property
    def eol_Expression81(self):
        return self.__eol_Expression81

    @eol_Expression81.setter
    def eol_Expression81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_Expression__eol_Expression81", None)
        self.__eol_Expression81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_FOLMethodCallExpression80"):
                opp_val = getattr(old_value, "eol_FOLMethodCallExpression80", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_FOLMethodCallExpression80"):
                opp_val = getattr(value, "eol_FOLMethodCallExpression80", None)
                if opp_val is None:
                    setattr(value, "eol_FOLMethodCallExpression80", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eol_Expression26(self):
        return self.__eol_Expression26

    @eol_Expression26.setter
    def eol_Expression26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_Expression__eol_Expression26", None)
        self.__eol_Expression26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_ExpressionOrStatementBlock25"):
                opp_val = getattr(old_value, "eol_ExpressionOrStatementBlock25", None)
                if opp_val == self:
                    setattr(old_value, "eol_ExpressionOrStatementBlock25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_ExpressionOrStatementBlock25"):
                opp_val = getattr(value, "eol_ExpressionOrStatementBlock25", None)
                setattr(value, "eol_ExpressionOrStatementBlock25", self)

    @property
    def eol_Expression168(self):
        return self.__eol_Expression168

    @eol_Expression168.setter
    def eol_Expression168(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_Expression__eol_Expression168", None)
        self.__eol_Expression168 = value
        
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
    def eol_Expression118(self):
        return self.__eol_Expression118

    @eol_Expression118.setter
    def eol_Expression118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_Expression__eol_Expression118", None)
        self.__eol_Expression118 = value
        
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

class eol_ExpressionOrStatementBlock(EOLElement):

    pass
class eol_Type(EOLElement):

    pass
class eol_Statement(EOLElement):

    pass
class eol_OperationDefinition(EOLElement):

    pass
class eol_Block(EOLElement):

    pass
class eol_EOLLibraryModule(EOLElement):

    def __init__(self, name: str, eol_EOLLibraryModule: set["eol_Import"] = None, eol_EOLLibraryModule11: set["eol_ModelDeclarationStatement"] = None, eol_EOLLibraryModule13: set["eol_OperationDefinition"] = None, eol_EOLLibraryModule17: "eol_Import" = None):
        self.name = name
        self.eol_EOLLibraryModule = eol_EOLLibraryModule if eol_EOLLibraryModule is not None else set()
        self.eol_EOLLibraryModule11 = eol_EOLLibraryModule11 if eol_EOLLibraryModule11 is not None else set()
        self.eol_EOLLibraryModule13 = eol_EOLLibraryModule13 if eol_EOLLibraryModule13 is not None else set()
        self.eol_EOLLibraryModule17 = eol_EOLLibraryModule17
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def eol_EOLLibraryModule13(self):
        return self.__eol_EOLLibraryModule13

    @eol_EOLLibraryModule13.setter
    def eol_EOLLibraryModule13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_EOLLibraryModule__eol_EOLLibraryModule13", None)
        self.__eol_EOLLibraryModule13 = value if value is not None else set()
        
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
                    

    @property
    def eol_EOLLibraryModule17(self):
        return self.__eol_EOLLibraryModule17

    @eol_EOLLibraryModule17.setter
    def eol_EOLLibraryModule17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_EOLLibraryModule__eol_EOLLibraryModule17", None)
        self.__eol_EOLLibraryModule17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_Import16"):
                opp_val = getattr(old_value, "eol_Import16", None)
                if opp_val == self:
                    setattr(old_value, "eol_Import16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_Import16"):
                opp_val = getattr(value, "eol_Import16", None)
                setattr(value, "eol_Import16", self)

    @property
    def eol_EOLLibraryModule11(self):
        return self.__eol_EOLLibraryModule11

    @eol_EOLLibraryModule11.setter
    def eol_EOLLibraryModule11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_EOLLibraryModule__eol_EOLLibraryModule11", None)
        self.__eol_EOLLibraryModule11 = value if value is not None else set()
        
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
                    
