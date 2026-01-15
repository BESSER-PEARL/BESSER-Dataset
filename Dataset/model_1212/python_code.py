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
class eol_CollectionType(AnyType):

    pass
class eol_NativeType(AnyType):

    pass
class eol_VoidType(AnyType):

    pass
class eol_InvalidType(AnyType):

    pass
class eol_PrimitiveType(AnyType):

    pass
class eol_ModelElementType(AnyType):

    def __init__(self, modelType: str, modelName: str, elementName: str, eol_ModelElementType220: "eol_IPackage" = None, eol_ModelElementType: "eol_IModel" = None, eol_ModelElementType217: "eol_ModelDeclarationStatement" = None):
        self.modelType = modelType
        self.modelName = modelName
        self.elementName = elementName
        self.eol_ModelElementType220 = eol_ModelElementType220
        self.eol_ModelElementType = eol_ModelElementType
        self.eol_ModelElementType217 = eol_ModelElementType217
        
    @property
    def modelType(self) -> str:
        return self.__modelType

    @modelType.setter
    def modelType(self, modelType: str):
        self.__modelType = modelType

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
    def eol_ModelElementType220(self):
        return self.__eol_ModelElementType220

    @eol_ModelElementType220.setter
    def eol_ModelElementType220(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_ModelElementType__eol_ModelElementType220", None)
        self.__eol_ModelElementType220 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_IPackage221"):
                opp_val = getattr(old_value, "eol_IPackage221", None)
                if opp_val == self:
                    setattr(old_value, "eol_IPackage221", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_IPackage221"):
                opp_val = getattr(value, "eol_IPackage221", None)
                setattr(value, "eol_IPackage221", self)

    @property
    def eol_ModelElementType217(self):
        return self.__eol_ModelElementType217

    @eol_ModelElementType217.setter
    def eol_ModelElementType217(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_ModelElementType__eol_ModelElementType217", None)
        self.__eol_ModelElementType217 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_ModelDeclarationStatement218"):
                opp_val = getattr(old_value, "eol_ModelDeclarationStatement218", None)
                if opp_val == self:
                    setattr(old_value, "eol_ModelDeclarationStatement218", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_ModelDeclarationStatement218"):
                opp_val = getattr(value, "eol_ModelDeclarationStatement218", None)
                setattr(value, "eol_ModelDeclarationStatement218", self)

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
            if hasattr(old_value, "eol_IModel215"):
                opp_val = getattr(old_value, "eol_IModel215", None)
                if opp_val == self:
                    setattr(old_value, "eol_IModel215", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_IModel215"):
                opp_val = getattr(value, "eol_IModel215", None)
                setattr(value, "eol_IModel215", self)

class eol_ModelType(AnyType):

    pass
class Type:

    pass
class eol_AnyType(Type):

    def __init__(self, declared: bool, eol_AnyType223: "eol_MapType" = None, eol_AnyType: set["eol_Type"] = None, eol_AnyType226: "eol_MapType" = None):
        self.declared = declared
        self.eol_AnyType223 = eol_AnyType223
        self.eol_AnyType = eol_AnyType if eol_AnyType is not None else set()
        self.eol_AnyType226 = eol_AnyType226
        
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
                if hasattr(item, "eol_Type211"):
                    opp_val = getattr(item, "eol_Type211", None)
                    
                    if opp_val == self:
                        setattr(item, "eol_Type211", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eol_Type211"):
                    opp_val = getattr(item, "eol_Type211", None)
                    
                    setattr(item, "eol_Type211", self)
                    

    @property
    def eol_AnyType223(self):
        return self.__eol_AnyType223

    @eol_AnyType223.setter
    def eol_AnyType223(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_AnyType__eol_AnyType223", None)
        self.__eol_AnyType223 = value
        
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
    def eol_AnyType226(self):
        return self.__eol_AnyType226

    @eol_AnyType226.setter
    def eol_AnyType226(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_AnyType__eol_AnyType226", None)
        self.__eol_AnyType226 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_MapType225"):
                opp_val = getattr(old_value, "eol_MapType225", None)
                if opp_val == self:
                    setattr(old_value, "eol_MapType225", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_MapType225"):
                opp_val = getattr(value, "eol_MapType225", None)
                setattr(value, "eol_MapType225", self)

class eol_MapType(AnyType):

    pass
class PseudoType:

    pass
class eol_SelfContentType(PseudoType):

    pass
class eol_SelfInnermostContentType(PseudoType):

    pass
class eol_SelfType(PseudoType):

    pass
class eol_PseudoType(AnyType):

    pass
class AnnotationStatement:

    pass
class eol_SimpleAnnotationStatement(AnnotationStatement):

    pass
class AssignmentStatement:

    pass
class eol_SpecialAssignmentStatement(AssignmentStatement):

    pass
class eol_ExecutableAnnotationStatement(AnnotationStatement):

    pass
class Statement:

    pass
class eol_AbortStatement(Statement):

    pass
class eol_ExpressionStatement(Statement):

    pass
class eol_WhileStatement(Statement):

    pass
class eol_BreakAllStatement(Statement):

    pass
class eol_ReturnStatement(Statement):

    pass
class eol_AnnotationStatement(Statement):

    pass
class eol_ThrowStatement(Statement):

    pass
class eol_SwitchStatement(Statement):

    pass
class eol_ContinueStatement(Statement):

    pass
class eol_BreakStatement(Statement):

    pass
class eol_DeleteStatement(Statement):

    pass
class eol_ForStatement(Statement):

    pass
class eol_IfStatement(Statement):

    pass
class eol_AssignmentStatement(Statement):

    pass
class eol_TransactionStatement(Statement):

    pass
class SwitchCaseStatement:

    pass
class eol_SwitchCaseExpressionStatement(SwitchCaseStatement):

    pass
class eol_SwitchCaseStatement(Statement):

    pass
class eol_SwitchCaseDefaultStatement(SwitchCaseStatement):

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
class CollectionInitialisationExpression:

    pass
class eol_ExpressionList(CollectionInitialisationExpression):

    pass
class eol_ExpressionRange(CollectionInitialisationExpression):

    pass
class KeyValueExpression:

    pass
class eol_ModelDeclarationParameter(KeyValueExpression):

    pass
class SummableExpression:

    pass
class ComparableExpression:

    pass
class eol_RealExpression(SummableExpression, ComparableExpression):

    def __init__(self, value: float):
        self.value = value
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

class eol_IntegerExpression(SummableExpression, ComparableExpression):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

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
            if hasattr(old_value, "eol_NameExpression94"):
                opp_val = getattr(old_value, "eol_NameExpression94", None)
                if opp_val == self:
                    setattr(old_value, "eol_NameExpression94", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_NameExpression94"):
                opp_val = getattr(value, "eol_NameExpression94", None)
                setattr(value, "eol_NameExpression94", self)

class eol_MethodCallExpression(FeatureCallExpression):

    pass
class VariableDeclarationExpression:

    pass
class eol_FOLMethodCallExpression(FeatureCallExpression):

    pass
class ComparisonOperatorExpression:

    pass
class eol_GreaterThanOperatorExpression(ComparisonOperatorExpression):

    pass
class eol_GreaterThanOrEqualToOperatorExpression(ComparisonOperatorExpression):

    pass
class ArithmeticOperatorExpression:

    pass
class eol_MultiplyOperatorExpression(ArithmeticOperatorExpression):

    pass
class eol_MinusOperatorExpression(ArithmeticOperatorExpression):

    pass
class eol_PlusOperatorExpression(ArithmeticOperatorExpression):

    pass
class eol_DivideOperatorExpression(ArithmeticOperatorExpression):

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
class eol_EqualsOperatorExpression(ComparisonOperatorExpression):

    pass
class eol_NotEqualsOperatorExpression(ComparisonOperatorExpression):

    pass
class eol_LessThanOperatorExpression(ComparisonOperatorExpression):

    pass
class eol_LessThanOrEqualToOperatorExpression(ComparisonOperatorExpression):

    pass
class eol_FormalParameterExpression(VariableDeclarationExpression):

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
class eol_FeatureCallExpression(Expression):

    def __init__(self, isArrow: bool, eol_FeatureCallExpression: "eol_Expression" = None):
        self.isArrow = isArrow
        self.eol_FeatureCallExpression = eol_FeatureCallExpression
        
    @property
    def isArrow(self) -> bool:
        return self.__isArrow

    @isArrow.setter
    def isArrow(self, isArrow: bool):
        self.__isArrow = isArrow

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
            if hasattr(old_value, "eol_Expression84"):
                opp_val = getattr(old_value, "eol_Expression84", None)
                if opp_val == self:
                    setattr(old_value, "eol_Expression84", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_Expression84"):
                opp_val = getattr(value, "eol_Expression84", None)
                setattr(value, "eol_Expression84", self)

class eol_KeyValueExpression(Expression):

    pass
class eol_CollectionExpression(Expression):

    pass
class eol_NewExpression(Expression):

    pass
class eol_CollectionInitialisationExpression(Expression):

    pass
class eol_PrimitiveExpression(Expression):

    pass
class eol_MapExpression(Expression):

    pass
class eol_VariableDeclarationExpression(Expression):

    def __init__(self, create: bool, eol_VariableDeclarationExpression: "eol_OperationDefinition" = None, eol_VariableDeclarationExpression60: "eol_OperationDefinition" = None, eol_VariableDeclarationExpression75: "eol_NameExpression" = None, eol_VariableDeclarationExpression78: set["eol_Expression"] = None, eol_VariableDeclarationExpression81: set["eol_NameExpression"] = None, eol_VariableDeclarationExpression198: "eol_ModelDeclarationStatement" = None, eol_VariableDeclarationExpression204: "eol_ModelDeclarationStatement" = None):
        self.create = create
        self.eol_VariableDeclarationExpression = eol_VariableDeclarationExpression
        self.eol_VariableDeclarationExpression60 = eol_VariableDeclarationExpression60
        self.eol_VariableDeclarationExpression75 = eol_VariableDeclarationExpression75
        self.eol_VariableDeclarationExpression78 = eol_VariableDeclarationExpression78 if eol_VariableDeclarationExpression78 is not None else set()
        self.eol_VariableDeclarationExpression81 = eol_VariableDeclarationExpression81 if eol_VariableDeclarationExpression81 is not None else set()
        self.eol_VariableDeclarationExpression198 = eol_VariableDeclarationExpression198
        self.eol_VariableDeclarationExpression204 = eol_VariableDeclarationExpression204
        
    @property
    def create(self) -> bool:
        return self.__create

    @create.setter
    def create(self, create: bool):
        self.__create = create

    @property
    def eol_VariableDeclarationExpression75(self):
        return self.__eol_VariableDeclarationExpression75

    @eol_VariableDeclarationExpression75.setter
    def eol_VariableDeclarationExpression75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_VariableDeclarationExpression__eol_VariableDeclarationExpression75", None)
        self.__eol_VariableDeclarationExpression75 = value
        
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

    @property
    def eol_VariableDeclarationExpression204(self):
        return self.__eol_VariableDeclarationExpression204

    @eol_VariableDeclarationExpression204.setter
    def eol_VariableDeclarationExpression204(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_VariableDeclarationExpression__eol_VariableDeclarationExpression204", None)
        self.__eol_VariableDeclarationExpression204 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_ModelDeclarationStatement203"):
                opp_val = getattr(old_value, "eol_ModelDeclarationStatement203", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_ModelDeclarationStatement203"):
                opp_val = getattr(value, "eol_ModelDeclarationStatement203", None)
                if opp_val is None:
                    setattr(value, "eol_ModelDeclarationStatement203", set([self]))
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
            if hasattr(old_value, "eol_OperationDefinition59"):
                opp_val = getattr(old_value, "eol_OperationDefinition59", None)
                if opp_val == self:
                    setattr(old_value, "eol_OperationDefinition59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_OperationDefinition59"):
                opp_val = getattr(value, "eol_OperationDefinition59", None)
                setattr(value, "eol_OperationDefinition59", self)

    @property
    def eol_VariableDeclarationExpression78(self):
        return self.__eol_VariableDeclarationExpression78

    @eol_VariableDeclarationExpression78.setter
    def eol_VariableDeclarationExpression78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_VariableDeclarationExpression__eol_VariableDeclarationExpression78", None)
        self.__eol_VariableDeclarationExpression78 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eol_Expression79"):
                    opp_val = getattr(item, "eol_Expression79", None)
                    
                    if opp_val == self:
                        setattr(item, "eol_Expression79", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eol_Expression79"):
                    opp_val = getattr(item, "eol_Expression79", None)
                    
                    setattr(item, "eol_Expression79", self)
                    

    @property
    def eol_VariableDeclarationExpression198(self):
        return self.__eol_VariableDeclarationExpression198

    @eol_VariableDeclarationExpression198.setter
    def eol_VariableDeclarationExpression198(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_VariableDeclarationExpression__eol_VariableDeclarationExpression198", None)
        self.__eol_VariableDeclarationExpression198 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_ModelDeclarationStatement197"):
                opp_val = getattr(old_value, "eol_ModelDeclarationStatement197", None)
                if opp_val == self:
                    setattr(old_value, "eol_ModelDeclarationStatement197", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_ModelDeclarationStatement197"):
                opp_val = getattr(value, "eol_ModelDeclarationStatement197", None)
                setattr(value, "eol_ModelDeclarationStatement197", self)

    @property
    def eol_VariableDeclarationExpression81(self):
        return self.__eol_VariableDeclarationExpression81

    @eol_VariableDeclarationExpression81.setter
    def eol_VariableDeclarationExpression81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_VariableDeclarationExpression__eol_VariableDeclarationExpression81", None)
        self.__eol_VariableDeclarationExpression81 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eol_NameExpression82"):
                    opp_val = getattr(item, "eol_NameExpression82", None)
                    
                    if opp_val == self:
                        setattr(item, "eol_NameExpression82", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eol_NameExpression82"):
                    opp_val = getattr(item, "eol_NameExpression82", None)
                    
                    setattr(item, "eol_NameExpression82", self)
                    

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
            if hasattr(old_value, "eol_OperationDefinition57"):
                opp_val = getattr(old_value, "eol_OperationDefinition57", None)
                if opp_val == self:
                    setattr(old_value, "eol_OperationDefinition57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_OperationDefinition57"):
                opp_val = getattr(value, "eol_OperationDefinition57", None)
                setattr(value, "eol_OperationDefinition57", self)

class eol_EnumerationLiteralExpression(Expression):

    pass
class eol_OperatorExpression(Expression):

    pass
class EOLLibraryModule:

    pass
class eol_EOLProgram(EOLLibraryModule):

    pass
class eol_ModelDeclarationStatement(Statement):

    pass
class Block:

    pass
class eol_AnnotationBlock(Block):

    pass
class eol_StringExpression(SummableExpression, ComparableExpression):

    def __init__(self, value: str, eol_StringExpression: "eol_IPackage" = None, eol_StringExpression193: "eol_SimpleAnnotationStatement" = None, eol_StringExpression228: "eol_NativeType" = None):
        self.value = value
        self.eol_StringExpression = eol_StringExpression
        self.eol_StringExpression193 = eol_StringExpression193
        self.eol_StringExpression228 = eol_StringExpression228
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

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
    def eol_StringExpression228(self):
        return self.__eol_StringExpression228

    @eol_StringExpression228.setter
    def eol_StringExpression228(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_StringExpression__eol_StringExpression228", None)
        self.__eol_StringExpression228 = value
        
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
    def eol_StringExpression(self):
        return self.__eol_StringExpression

    @eol_StringExpression.setter
    def eol_StringExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_StringExpression__eol_StringExpression", None)
        self.__eol_StringExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_IPackage14"):
                opp_val = getattr(old_value, "eol_IPackage14", None)
                if opp_val == self:
                    setattr(old_value, "eol_IPackage14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_IPackage14"):
                opp_val = getattr(value, "eol_IPackage14", None)
                setattr(value, "eol_IPackage14", self)

class eol_NameExpression(Expression):

    def __init__(self, name: str, resolvedContent: str, isType: bool, eol_NameExpression: "eol_IModel" = None, eol_NameExpression7: "eol_IModel" = None, eol_NameExpression10: "eol_IModel" = None, eol_NameExpression53: "eol_OperationDefinition" = None, eol_NameExpression76: "eol_VariableDeclarationExpression" = None, eol_NameExpression94: "eol_PropertyCallExpression" = None, eol_NameExpression102: "eol_FOLMethodCallExpression" = None, eol_NameExpression82: "eol_VariableDeclarationExpression" = None, eol_NameExpression89: "eol_MethodCallExpression" = None, eol_NameExpression112: "eol_NewExpression" = None, eol_NameExpression132: "eol_EnumerationLiteralExpression" = None, eol_NameExpression123: "eol_EnumerationLiteralExpression" = None, eol_NameExpression126: "eol_EnumerationLiteralExpression" = None, eol_NameExpression141: "eol_TransactionStatement" = None, eol_NameExpression201: "eol_ModelDeclarationStatement" = None, eol_NameExpression191: "eol_AnnotationStatement" = None):
        self.name = name
        self.resolvedContent = resolvedContent
        self.isType = isType
        self.eol_NameExpression = eol_NameExpression
        self.eol_NameExpression7 = eol_NameExpression7
        self.eol_NameExpression10 = eol_NameExpression10
        self.eol_NameExpression53 = eol_NameExpression53
        self.eol_NameExpression76 = eol_NameExpression76
        self.eol_NameExpression94 = eol_NameExpression94
        self.eol_NameExpression102 = eol_NameExpression102
        self.eol_NameExpression82 = eol_NameExpression82
        self.eol_NameExpression89 = eol_NameExpression89
        self.eol_NameExpression112 = eol_NameExpression112
        self.eol_NameExpression132 = eol_NameExpression132
        self.eol_NameExpression123 = eol_NameExpression123
        self.eol_NameExpression126 = eol_NameExpression126
        self.eol_NameExpression141 = eol_NameExpression141
        self.eol_NameExpression201 = eol_NameExpression201
        self.eol_NameExpression191 = eol_NameExpression191
        
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
    def isType(self) -> bool:
        return self.__isType

    @isType.setter
    def isType(self, isType: bool):
        self.__isType = isType

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
            if hasattr(old_value, "eol_OperationDefinition52"):
                opp_val = getattr(old_value, "eol_OperationDefinition52", None)
                if opp_val == self:
                    setattr(old_value, "eol_OperationDefinition52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_OperationDefinition52"):
                opp_val = getattr(value, "eol_OperationDefinition52", None)
                setattr(value, "eol_OperationDefinition52", self)

    @property
    def eol_NameExpression7(self):
        return self.__eol_NameExpression7

    @eol_NameExpression7.setter
    def eol_NameExpression7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_NameExpression__eol_NameExpression7", None)
        self.__eol_NameExpression7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_IModel6"):
                opp_val = getattr(old_value, "eol_IModel6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_IModel6"):
                opp_val = getattr(value, "eol_IModel6", None)
                if opp_val is None:
                    setattr(value, "eol_IModel6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eol_NameExpression10(self):
        return self.__eol_NameExpression10

    @eol_NameExpression10.setter
    def eol_NameExpression10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_NameExpression__eol_NameExpression10", None)
        self.__eol_NameExpression10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_IModel9"):
                opp_val = getattr(old_value, "eol_IModel9", None)
                if opp_val == self:
                    setattr(old_value, "eol_IModel9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_IModel9"):
                opp_val = getattr(value, "eol_IModel9", None)
                setattr(value, "eol_IModel9", self)

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
            if hasattr(old_value, "eol_IModel"):
                opp_val = getattr(old_value, "eol_IModel", None)
                if opp_val == self:
                    setattr(old_value, "eol_IModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_IModel"):
                opp_val = getattr(value, "eol_IModel", None)
                setattr(value, "eol_IModel", self)

    @property
    def eol_NameExpression82(self):
        return self.__eol_NameExpression82

    @eol_NameExpression82.setter
    def eol_NameExpression82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_NameExpression__eol_NameExpression82", None)
        self.__eol_NameExpression82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_VariableDeclarationExpression81"):
                opp_val = getattr(old_value, "eol_VariableDeclarationExpression81", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_VariableDeclarationExpression81"):
                opp_val = getattr(value, "eol_VariableDeclarationExpression81", None)
                if opp_val is None:
                    setattr(value, "eol_VariableDeclarationExpression81", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eol_NameExpression112(self):
        return self.__eol_NameExpression112

    @eol_NameExpression112.setter
    def eol_NameExpression112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_NameExpression__eol_NameExpression112", None)
        self.__eol_NameExpression112 = value
        
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
    def eol_NameExpression76(self):
        return self.__eol_NameExpression76

    @eol_NameExpression76.setter
    def eol_NameExpression76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_NameExpression__eol_NameExpression76", None)
        self.__eol_NameExpression76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_VariableDeclarationExpression75"):
                opp_val = getattr(old_value, "eol_VariableDeclarationExpression75", None)
                if opp_val == self:
                    setattr(old_value, "eol_VariableDeclarationExpression75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_VariableDeclarationExpression75"):
                opp_val = getattr(value, "eol_VariableDeclarationExpression75", None)
                setattr(value, "eol_VariableDeclarationExpression75", self)

    @property
    def eol_NameExpression132(self):
        return self.__eol_NameExpression132

    @eol_NameExpression132.setter
    def eol_NameExpression132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_NameExpression__eol_NameExpression132", None)
        self.__eol_NameExpression132 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_EnumerationLiteralExpression131"):
                opp_val = getattr(old_value, "eol_EnumerationLiteralExpression131", None)
                if opp_val == self:
                    setattr(old_value, "eol_EnumerationLiteralExpression131", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_EnumerationLiteralExpression131"):
                opp_val = getattr(value, "eol_EnumerationLiteralExpression131", None)
                setattr(value, "eol_EnumerationLiteralExpression131", self)

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
            if hasattr(old_value, "eol_FOLMethodCallExpression101"):
                opp_val = getattr(old_value, "eol_FOLMethodCallExpression101", None)
                if opp_val == self:
                    setattr(old_value, "eol_FOLMethodCallExpression101", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_FOLMethodCallExpression101"):
                opp_val = getattr(value, "eol_FOLMethodCallExpression101", None)
                setattr(value, "eol_FOLMethodCallExpression101", self)

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
    def eol_NameExpression191(self):
        return self.__eol_NameExpression191

    @eol_NameExpression191.setter
    def eol_NameExpression191(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_NameExpression__eol_NameExpression191", None)
        self.__eol_NameExpression191 = value
        
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
    def eol_NameExpression141(self):
        return self.__eol_NameExpression141

    @eol_NameExpression141.setter
    def eol_NameExpression141(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_NameExpression__eol_NameExpression141", None)
        self.__eol_NameExpression141 = value
        
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
    def eol_NameExpression126(self):
        return self.__eol_NameExpression126

    @eol_NameExpression126.setter
    def eol_NameExpression126(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_NameExpression__eol_NameExpression126", None)
        self.__eol_NameExpression126 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_EnumerationLiteralExpression125"):
                opp_val = getattr(old_value, "eol_EnumerationLiteralExpression125", None)
                if opp_val == self:
                    setattr(old_value, "eol_EnumerationLiteralExpression125", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_EnumerationLiteralExpression125"):
                opp_val = getattr(value, "eol_EnumerationLiteralExpression125", None)
                setattr(value, "eol_EnumerationLiteralExpression125", self)

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
            if hasattr(old_value, "eol_ModelDeclarationStatement200"):
                opp_val = getattr(old_value, "eol_ModelDeclarationStatement200", None)
                if opp_val == self:
                    setattr(old_value, "eol_ModelDeclarationStatement200", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_ModelDeclarationStatement200"):
                opp_val = getattr(value, "eol_ModelDeclarationStatement200", None)
                setattr(value, "eol_ModelDeclarationStatement200", self)

    @property
    def eol_NameExpression89(self):
        return self.__eol_NameExpression89

    @eol_NameExpression89.setter
    def eol_NameExpression89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_NameExpression__eol_NameExpression89", None)
        self.__eol_NameExpression89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_MethodCallExpression88"):
                opp_val = getattr(old_value, "eol_MethodCallExpression88", None)
                if opp_val == self:
                    setattr(old_value, "eol_MethodCallExpression88", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_MethodCallExpression88"):
                opp_val = getattr(value, "eol_MethodCallExpression88", None)
                setattr(value, "eol_MethodCallExpression88", self)

    @property
    def eol_NameExpression123(self):
        return self.__eol_NameExpression123

    @eol_NameExpression123.setter
    def eol_NameExpression123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_NameExpression__eol_NameExpression123", None)
        self.__eol_NameExpression123 = value
        
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

class EOLElement:

    pass
class eol_Statement(EOLElement):

    pass
class eol_IPackage(EOLElement):

    def __init__(self, nsPrefix: str, iPackageDriver: str, name: str, eol_IPackage17: "eol_IPackage" = None, eol_IPackage15: set["eol_IPackage"] = None, eol_IPackage: "eol_IModel" = None, eol_IPackage14: "eol_StringExpression" = None, eol_IPackage221: "eol_ModelElementType" = None):
        self.nsPrefix = nsPrefix
        self.iPackageDriver = iPackageDriver
        self.name = name
        self.eol_IPackage17 = eol_IPackage17
        self.eol_IPackage15 = eol_IPackage15 if eol_IPackage15 is not None else set()
        self.eol_IPackage = eol_IPackage
        self.eol_IPackage14 = eol_IPackage14
        self.eol_IPackage221 = eol_IPackage221
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def nsPrefix(self) -> str:
        return self.__nsPrefix

    @nsPrefix.setter
    def nsPrefix(self, nsPrefix: str):
        self.__nsPrefix = nsPrefix

    @property
    def iPackageDriver(self) -> str:
        return self.__iPackageDriver

    @iPackageDriver.setter
    def iPackageDriver(self, iPackageDriver: str):
        self.__iPackageDriver = iPackageDriver

    @property
    def eol_IPackage14(self):
        return self.__eol_IPackage14

    @eol_IPackage14.setter
    def eol_IPackage14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_IPackage__eol_IPackage14", None)
        self.__eol_IPackage14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_StringExpression"):
                opp_val = getattr(old_value, "eol_StringExpression", None)
                if opp_val == self:
                    setattr(old_value, "eol_StringExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_StringExpression"):
                opp_val = getattr(value, "eol_StringExpression", None)
                setattr(value, "eol_StringExpression", self)

    @property
    def eol_IPackage15(self):
        return self.__eol_IPackage15

    @eol_IPackage15.setter
    def eol_IPackage15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_IPackage__eol_IPackage15", None)
        self.__eol_IPackage15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eol_IPackage17"):
                    opp_val = getattr(item, "eol_IPackage17", None)
                    
                    if opp_val == self:
                        setattr(item, "eol_IPackage17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eol_IPackage17"):
                    opp_val = getattr(item, "eol_IPackage17", None)
                    
                    setattr(item, "eol_IPackage17", self)
                    

    @property
    def eol_IPackage221(self):
        return self.__eol_IPackage221

    @eol_IPackage221.setter
    def eol_IPackage221(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_IPackage__eol_IPackage221", None)
        self.__eol_IPackage221 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_ModelElementType220"):
                opp_val = getattr(old_value, "eol_ModelElementType220", None)
                if opp_val == self:
                    setattr(old_value, "eol_ModelElementType220", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_ModelElementType220"):
                opp_val = getattr(value, "eol_ModelElementType220", None)
                setattr(value, "eol_ModelElementType220", self)

    @property
    def eol_IPackage17(self):
        return self.__eol_IPackage17

    @eol_IPackage17.setter
    def eol_IPackage17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_IPackage__eol_IPackage17", None)
        self.__eol_IPackage17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_IPackage15"):
                opp_val = getattr(old_value, "eol_IPackage15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_IPackage15"):
                opp_val = getattr(value, "eol_IPackage15", None)
                if opp_val is None:
                    setattr(value, "eol_IPackage15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eol_IPackage(self):
        return self.__eol_IPackage

    @eol_IPackage.setter
    def eol_IPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_IPackage__eol_IPackage", None)
        self.__eol_IPackage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_IModel12"):
                opp_val = getattr(old_value, "eol_IModel12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_IModel12"):
                opp_val = getattr(value, "eol_IModel12", None)
                if opp_val is None:
                    setattr(value, "eol_IModel12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class eol_Import(EOLElement):

    def __init__(self, imported: str, eol_Import33: "eol_EOLLibraryModule" = None, eol_Import: "eol_EOLLibraryModule" = None):
        self.imported = imported
        self.eol_Import33 = eol_Import33
        self.eol_Import = eol_Import
        
    @property
    def imported(self) -> str:
        return self.__imported

    @imported.setter
    def imported(self, imported: str):
        self.__imported = imported

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

    @property
    def eol_Import33(self):
        return self.__eol_Import33

    @eol_Import33.setter
    def eol_Import33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_Import__eol_Import33", None)
        self.__eol_Import33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_EOLLibraryModule34"):
                opp_val = getattr(old_value, "eol_EOLLibraryModule34", None)
                if opp_val == self:
                    setattr(old_value, "eol_EOLLibraryModule34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_EOLLibraryModule34"):
                opp_val = getattr(value, "eol_EOLLibraryModule34", None)
                setattr(value, "eol_EOLLibraryModule34", self)

class eol_Expression(EOLElement):

    pass
class eol_OperationDefinition(EOLElement):

    pass
class eol_Block(EOLElement):

    pass
class eol_Type(EOLElement):

    pass
class eol_EOLLibraryModule(EOLElement):

    def __init__(self, name: str, eol_EOLLibraryModule: set["eol_Import"] = None, eol_EOLLibraryModule25: set["eol_IModel"] = None, eol_EOLLibraryModule28: set["eol_ModelDeclarationStatement"] = None, eol_EOLLibraryModule30: set["eol_OperationDefinition"] = None, eol_EOLLibraryModule34: "eol_Import" = None):
        self.name = name
        self.eol_EOLLibraryModule = eol_EOLLibraryModule if eol_EOLLibraryModule is not None else set()
        self.eol_EOLLibraryModule25 = eol_EOLLibraryModule25 if eol_EOLLibraryModule25 is not None else set()
        self.eol_EOLLibraryModule28 = eol_EOLLibraryModule28 if eol_EOLLibraryModule28 is not None else set()
        self.eol_EOLLibraryModule30 = eol_EOLLibraryModule30 if eol_EOLLibraryModule30 is not None else set()
        self.eol_EOLLibraryModule34 = eol_EOLLibraryModule34
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def eol_EOLLibraryModule25(self):
        return self.__eol_EOLLibraryModule25

    @eol_EOLLibraryModule25.setter
    def eol_EOLLibraryModule25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_EOLLibraryModule__eol_EOLLibraryModule25", None)
        self.__eol_EOLLibraryModule25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eol_IModel26"):
                    opp_val = getattr(item, "eol_IModel26", None)
                    
                    if opp_val == self:
                        setattr(item, "eol_IModel26", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eol_IModel26"):
                    opp_val = getattr(item, "eol_IModel26", None)
                    
                    setattr(item, "eol_IModel26", self)
                    

    @property
    def eol_EOLLibraryModule34(self):
        return self.__eol_EOLLibraryModule34

    @eol_EOLLibraryModule34.setter
    def eol_EOLLibraryModule34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_EOLLibraryModule__eol_EOLLibraryModule34", None)
        self.__eol_EOLLibraryModule34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_Import33"):
                opp_val = getattr(old_value, "eol_Import33", None)
                if opp_val == self:
                    setattr(old_value, "eol_Import33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_Import33"):
                opp_val = getattr(value, "eol_Import33", None)
                setattr(value, "eol_Import33", self)

    @property
    def eol_EOLLibraryModule28(self):
        return self.__eol_EOLLibraryModule28

    @eol_EOLLibraryModule28.setter
    def eol_EOLLibraryModule28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_EOLLibraryModule__eol_EOLLibraryModule28", None)
        self.__eol_EOLLibraryModule28 = value if value is not None else set()
        
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
    def eol_EOLLibraryModule30(self):
        return self.__eol_EOLLibraryModule30

    @eol_EOLLibraryModule30.setter
    def eol_EOLLibraryModule30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_EOLLibraryModule__eol_EOLLibraryModule30", None)
        self.__eol_EOLLibraryModule30 = value if value is not None else set()
        
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
                    

class eol_ExpressionOrStatementBlock(EOLElement):

    pass
class eol_IModel(EOLElement):

    def __init__(self, iMetamodelDriver: str, eol_IModel: "eol_NameExpression" = None, eol_IModel6: set["eol_NameExpression"] = None, eol_IModel9: "eol_NameExpression" = None, eol_IModel12: set["eol_IPackage"] = None, eol_IModel26: "eol_EOLLibraryModule" = None, eol_IModel129: "eol_EnumerationLiteralExpression" = None, eol_IModel207: "eol_ModelDeclarationStatement" = None, eol_IModel213: "eol_ModelType" = None, eol_IModel215: "eol_ModelElementType" = None):
        self.iMetamodelDriver = iMetamodelDriver
        self.eol_IModel = eol_IModel
        self.eol_IModel6 = eol_IModel6 if eol_IModel6 is not None else set()
        self.eol_IModel9 = eol_IModel9
        self.eol_IModel12 = eol_IModel12 if eol_IModel12 is not None else set()
        self.eol_IModel26 = eol_IModel26
        self.eol_IModel129 = eol_IModel129
        self.eol_IModel207 = eol_IModel207
        self.eol_IModel213 = eol_IModel213
        self.eol_IModel215 = eol_IModel215
        
    @property
    def iMetamodelDriver(self) -> str:
        return self.__iMetamodelDriver

    @iMetamodelDriver.setter
    def iMetamodelDriver(self, iMetamodelDriver: str):
        self.__iMetamodelDriver = iMetamodelDriver

    @property
    def eol_IModel213(self):
        return self.__eol_IModel213

    @eol_IModel213.setter
    def eol_IModel213(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_IModel__eol_IModel213", None)
        self.__eol_IModel213 = value
        
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
    def eol_IModel6(self):
        return self.__eol_IModel6

    @eol_IModel6.setter
    def eol_IModel6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_IModel__eol_IModel6", None)
        self.__eol_IModel6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eol_NameExpression7"):
                    opp_val = getattr(item, "eol_NameExpression7", None)
                    
                    if opp_val == self:
                        setattr(item, "eol_NameExpression7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eol_NameExpression7"):
                    opp_val = getattr(item, "eol_NameExpression7", None)
                    
                    setattr(item, "eol_NameExpression7", self)
                    

    @property
    def eol_IModel215(self):
        return self.__eol_IModel215

    @eol_IModel215.setter
    def eol_IModel215(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_IModel__eol_IModel215", None)
        self.__eol_IModel215 = value
        
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
    def eol_IModel129(self):
        return self.__eol_IModel129

    @eol_IModel129.setter
    def eol_IModel129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_IModel__eol_IModel129", None)
        self.__eol_IModel129 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_EnumerationLiteralExpression128"):
                opp_val = getattr(old_value, "eol_EnumerationLiteralExpression128", None)
                if opp_val == self:
                    setattr(old_value, "eol_EnumerationLiteralExpression128", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_EnumerationLiteralExpression128"):
                opp_val = getattr(value, "eol_EnumerationLiteralExpression128", None)
                setattr(value, "eol_EnumerationLiteralExpression128", self)

    @property
    def eol_IModel12(self):
        return self.__eol_IModel12

    @eol_IModel12.setter
    def eol_IModel12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_IModel__eol_IModel12", None)
        self.__eol_IModel12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eol_IPackage"):
                    opp_val = getattr(item, "eol_IPackage", None)
                    
                    if opp_val == self:
                        setattr(item, "eol_IPackage", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eol_IPackage"):
                    opp_val = getattr(item, "eol_IPackage", None)
                    
                    setattr(item, "eol_IPackage", self)
                    

    @property
    def eol_IModel9(self):
        return self.__eol_IModel9

    @eol_IModel9.setter
    def eol_IModel9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_IModel__eol_IModel9", None)
        self.__eol_IModel9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_NameExpression10"):
                opp_val = getattr(old_value, "eol_NameExpression10", None)
                if opp_val == self:
                    setattr(old_value, "eol_NameExpression10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_NameExpression10"):
                opp_val = getattr(value, "eol_NameExpression10", None)
                setattr(value, "eol_NameExpression10", self)

    @property
    def eol_IModel207(self):
        return self.__eol_IModel207

    @eol_IModel207.setter
    def eol_IModel207(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_IModel__eol_IModel207", None)
        self.__eol_IModel207 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_ModelDeclarationStatement206"):
                opp_val = getattr(old_value, "eol_ModelDeclarationStatement206", None)
                if opp_val == self:
                    setattr(old_value, "eol_ModelDeclarationStatement206", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_ModelDeclarationStatement206"):
                opp_val = getattr(value, "eol_ModelDeclarationStatement206", None)
                setattr(value, "eol_ModelDeclarationStatement206", self)

    @property
    def eol_IModel26(self):
        return self.__eol_IModel26

    @eol_IModel26.setter
    def eol_IModel26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_IModel__eol_IModel26", None)
        self.__eol_IModel26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_EOLLibraryModule25"):
                opp_val = getattr(old_value, "eol_EOLLibraryModule25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_EOLLibraryModule25"):
                opp_val = getattr(value, "eol_EOLLibraryModule25", None)
                if opp_val is None:
                    setattr(value, "eol_EOLLibraryModule25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eol_IModel(self):
        return self.__eol_IModel

    @eol_IModel.setter
    def eol_IModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_IModel__eol_IModel", None)
        self.__eol_IModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_NameExpression"):
                opp_val = getattr(old_value, "eol_NameExpression", None)
                if opp_val == self:
                    setattr(old_value, "eol_NameExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_NameExpression"):
                opp_val = getattr(value, "eol_NameExpression", None)
                setattr(value, "eol_NameExpression", self)

class eol_TextRegion(EOLElement):

    pass
class eol_TextPosition(EOLElement):

    def __init__(self, line: int, column: int, eol_TextPosition: "eol_TextRegion" = None, eol_TextPosition22: "eol_TextRegion" = None):
        self.line = line
        self.column = column
        self.eol_TextPosition = eol_TextPosition
        self.eol_TextPosition22 = eol_TextPosition22
        
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
            if hasattr(old_value, "eol_TextRegion19"):
                opp_val = getattr(old_value, "eol_TextRegion19", None)
                if opp_val == self:
                    setattr(old_value, "eol_TextRegion19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_TextRegion19"):
                opp_val = getattr(value, "eol_TextRegion19", None)
                setattr(value, "eol_TextRegion19", self)

    @property
    def eol_TextPosition22(self):
        return self.__eol_TextPosition22

    @eol_TextPosition22.setter
    def eol_TextPosition22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_TextPosition__eol_TextPosition22", None)
        self.__eol_TextPosition22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_TextRegion21"):
                opp_val = getattr(old_value, "eol_TextRegion21", None)
                if opp_val == self:
                    setattr(old_value, "eol_TextRegion21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_TextRegion21"):
                opp_val = getattr(value, "eol_TextRegion21", None)
                setattr(value, "eol_TextRegion21", self)

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
