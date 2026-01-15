from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class transformation_EEnumLiteral:

    pass
class transformation_EClassifier:

    pass
class ArithmeticExpression:

    pass
class transformation_Multiplication(ArithmeticExpression):

    pass
class transformation_Division(ArithmeticExpression):

    pass
class transformation_Subtraction(ArithmeticExpression):

    pass
class transformation_Addition(ArithmeticExpression):

    pass
class transformation_ETypedElement:

    pass
class UnaryExpression:

    pass
class transformation_Minus(UnaryExpression):

    pass
class transformation_Negation(UnaryExpression):

    pass
class BinaryExpression:

    pass
class transformation_LogicalExpression(BinaryExpression):

    pass
class transformation_CoalescingExpression(BinaryExpression):

    pass
class transformation_ArithmeticExpression(BinaryExpression):

    pass
class RelationalExpression:

    pass
class transformation_GreaterOrEqual(RelationalExpression):

    pass
class transformation_Greater(RelationalExpression):

    pass
class transformation_LessOrEqual(RelationalExpression):

    pass
class transformation_Less(RelationalExpression):

    pass
class transformation_RelationalExpression(BinaryExpression):

    pass
class EqualityExpression:

    pass
class transformation_Different(EqualityExpression):

    pass
class transformation_Equal(EqualityExpression):

    pass
class transformation_EqualityExpression(BinaryExpression):

    pass
class LogicalExpression:

    pass
class transformation_And(LogicalExpression):

    pass
class transformation_Or(LogicalExpression):

    pass
class Expression:

    pass
class transformation_BooleanLiteral(Expression):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class transformation_TypeOfExpression(Expression):

    pass
class transformation_RealLiteral(Expression):

    def __init__(self, value: float):
        self.value = value
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

class transformation_Invocation(Expression):

    pass
class transformation_ClassLiteral(Expression):

    pass
class transformation_EnumLiteral(Expression):

    pass
class transformation_Map(Expression):

    pass
class transformation_IntegerLiteral(Expression):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class transformation_Lambda(Expression):

    pass
class transformation_VariableUse(Expression):

    pass
class transformation_ExtentExpression(Expression):

    pass
class transformation_Let(Expression):

    pass
class transformation_Source(Expression):

    pass
class transformation_FeatureAccess(Expression):

    def __init__(self, nullable: bool, spreading: bool, transformation_FeatureAccess: "transformation_Expression" = None, transformation_FeatureAccess67: "transformation_ETypedElement" = None):
        self.nullable = nullable
        self.spreading = spreading
        self.transformation_FeatureAccess = transformation_FeatureAccess
        self.transformation_FeatureAccess67 = transformation_FeatureAccess67
        
    @property
    def nullable(self) -> bool:
        return self.__nullable

    @nullable.setter
    def nullable(self, nullable: bool):
        self.__nullable = nullable

    @property
    def spreading(self) -> bool:
        return self.__spreading

    @spreading.setter
    def spreading(self, spreading: bool):
        self.__spreading = spreading

    @property
    def transformation_FeatureAccess67(self):
        return self.__transformation_FeatureAccess67

    @transformation_FeatureAccess67.setter
    def transformation_FeatureAccess67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_transformation_FeatureAccess__transformation_FeatureAccess67", None)
        self.__transformation_FeatureAccess67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transformation_ETypedElement"):
                opp_val = getattr(old_value, "transformation_ETypedElement", None)
                if opp_val == self:
                    setattr(old_value, "transformation_ETypedElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transformation_ETypedElement"):
                opp_val = getattr(value, "transformation_ETypedElement", None)
                setattr(value, "transformation_ETypedElement", self)

    @property
    def transformation_FeatureAccess(self):
        return self.__transformation_FeatureAccess

    @transformation_FeatureAccess.setter
    def transformation_FeatureAccess(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_transformation_FeatureAccess__transformation_FeatureAccess", None)
        self.__transformation_FeatureAccess = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transformation_Expression65"):
                opp_val = getattr(old_value, "transformation_Expression65", None)
                if opp_val == self:
                    setattr(old_value, "transformation_Expression65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transformation_Expression65"):
                opp_val = getattr(value, "transformation_Expression65", None)
                setattr(value, "transformation_Expression65", self)

class transformation_StringLiteral(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class transformation_UnaryExpression(Expression):

    pass
class transformation_BinaryExpression(Expression):

    pass
class transformation_If(Expression):

    pass
class transformation_ConditionalExpression(Expression):

    pass
class transformation_Expression(ABC):

    pass
class transformation_VariableInitialization:

    pass
class transformation_VariableDefinition:

    def __init__(self, name: str, transformation_VariableDefinition: "transformation_VariableInitialization" = None, transformation_VariableDefinition78: "transformation_Lambda" = None, transformation_VariableDefinition87: "transformation_VariableUse" = None):
        self.name = name
        self.transformation_VariableDefinition = transformation_VariableDefinition
        self.transformation_VariableDefinition78 = transformation_VariableDefinition78
        self.transformation_VariableDefinition87 = transformation_VariableDefinition87
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def transformation_VariableDefinition87(self):
        return self.__transformation_VariableDefinition87

    @transformation_VariableDefinition87.setter
    def transformation_VariableDefinition87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_transformation_VariableDefinition__transformation_VariableDefinition87", None)
        self.__transformation_VariableDefinition87 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transformation_VariableUse"):
                opp_val = getattr(old_value, "transformation_VariableUse", None)
                if opp_val == self:
                    setattr(old_value, "transformation_VariableUse", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transformation_VariableUse"):
                opp_val = getattr(value, "transformation_VariableUse", None)
                setattr(value, "transformation_VariableUse", self)

    @property
    def transformation_VariableDefinition78(self):
        return self.__transformation_VariableDefinition78

    @transformation_VariableDefinition78.setter
    def transformation_VariableDefinition78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_transformation_VariableDefinition__transformation_VariableDefinition78", None)
        self.__transformation_VariableDefinition78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transformation_Lambda"):
                opp_val = getattr(old_value, "transformation_Lambda", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transformation_Lambda"):
                opp_val = getattr(value, "transformation_Lambda", None)
                if opp_val is None:
                    setattr(value, "transformation_Lambda", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def transformation_VariableDefinition(self):
        return self.__transformation_VariableDefinition

    @transformation_VariableDefinition.setter
    def transformation_VariableDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_transformation_VariableDefinition__transformation_VariableDefinition", None)
        self.__transformation_VariableDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transformation_VariableInitialization"):
                opp_val = getattr(old_value, "transformation_VariableInitialization", None)
                if opp_val == self:
                    setattr(old_value, "transformation_VariableInitialization", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transformation_VariableInitialization"):
                opp_val = getattr(value, "transformation_VariableInitialization", None)
                setattr(value, "transformation_VariableInitialization", self)

class transformation_EStructuralFeature:

    pass
class transformation_EClass:

    pass
class transformation_ContentMapping(ABC):

    pass
class CompositeMapping:

    pass
class transformation_OtherwiseClause(CompositeMapping):

    pass
class transformation_WhenClause(CompositeMapping):

    pass
class ContentMapping:

    pass
class transformation_ConditionalMapping(ContentMapping):

    pass
class transformation_ResultMapping(ContentMapping):

    pass
class transformation_FeatureMapping(ContentMapping):

    pass
class transformation_CompositeMapping(ContentMapping):

    pass
class transformation_EPackage:

    pass
class transformation_AbstractMapping(ABC):

    pass
class transformation_MetamodelDeclaration(ABC):

    pass
class transformation_EDataType:

    pass
class AbstractMapping:

    pass
class transformation_ClassMapping(AbstractMapping):

    def __init__(self, default: bool, transformation_ClassMapping17: "transformation_ContentMapping" = None, transformation_ClassMapping: "transformation_EClass" = None, transformation_ClassMapping14: "transformation_EClass" = None):
        self.default = default
        self.transformation_ClassMapping17 = transformation_ClassMapping17
        self.transformation_ClassMapping = transformation_ClassMapping
        self.transformation_ClassMapping14 = transformation_ClassMapping14
        
    @property
    def default(self) -> bool:
        return self.__default

    @default.setter
    def default(self, default: bool):
        self.__default = default

    @property
    def transformation_ClassMapping(self):
        return self.__transformation_ClassMapping

    @transformation_ClassMapping.setter
    def transformation_ClassMapping(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_transformation_ClassMapping__transformation_ClassMapping", None)
        self.__transformation_ClassMapping = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transformation_EClass"):
                opp_val = getattr(old_value, "transformation_EClass", None)
                if opp_val == self:
                    setattr(old_value, "transformation_EClass", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transformation_EClass"):
                opp_val = getattr(value, "transformation_EClass", None)
                setattr(value, "transformation_EClass", self)

    @property
    def transformation_ClassMapping17(self):
        return self.__transformation_ClassMapping17

    @transformation_ClassMapping17.setter
    def transformation_ClassMapping17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_transformation_ClassMapping__transformation_ClassMapping17", None)
        self.__transformation_ClassMapping17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transformation_ContentMapping18"):
                opp_val = getattr(old_value, "transformation_ContentMapping18", None)
                if opp_val == self:
                    setattr(old_value, "transformation_ContentMapping18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transformation_ContentMapping18"):
                opp_val = getattr(value, "transformation_ContentMapping18", None)
                setattr(value, "transformation_ContentMapping18", self)

    @property
    def transformation_ClassMapping14(self):
        return self.__transformation_ClassMapping14

    @transformation_ClassMapping14.setter
    def transformation_ClassMapping14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_transformation_ClassMapping__transformation_ClassMapping14", None)
        self.__transformation_ClassMapping14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transformation_EClass15"):
                opp_val = getattr(old_value, "transformation_EClass15", None)
                if opp_val == self:
                    setattr(old_value, "transformation_EClass15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transformation_EClass15"):
                opp_val = getattr(value, "transformation_EClass15", None)
                setattr(value, "transformation_EClass15", self)

class transformation_DataTypeMapping(AbstractMapping):

    pass
class ExplicitMetamodel:

    pass
class transformation_TargetMetamodel(ExplicitMetamodel):

    pass
class transformation_SourceMetamodel(ExplicitMetamodel):

    pass
class MetamodelDeclaration:

    pass
class transformation_ExtentMetamodel(MetamodelDeclaration):

    def __init__(self, generated: bool, transformation_ExtentMetamodel: "transformation_SourceMetamodel" = None):
        self.generated = generated
        self.transformation_ExtentMetamodel = transformation_ExtentMetamodel
        
    @property
    def generated(self) -> bool:
        return self.__generated

    @generated.setter
    def generated(self, generated: bool):
        self.__generated = generated

    @property
    def transformation_ExtentMetamodel(self):
        return self.__transformation_ExtentMetamodel

    @transformation_ExtentMetamodel.setter
    def transformation_ExtentMetamodel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_transformation_ExtentMetamodel__transformation_ExtentMetamodel", None)
        self.__transformation_ExtentMetamodel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transformation_SourceMetamodel"):
                opp_val = getattr(old_value, "transformation_SourceMetamodel", None)
                if opp_val == self:
                    setattr(old_value, "transformation_SourceMetamodel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transformation_SourceMetamodel"):
                opp_val = getattr(value, "transformation_SourceMetamodel", None)
                setattr(value, "transformation_SourceMetamodel", self)

class transformation_ExplicitMetamodel(MetamodelDeclaration):

    def __init__(self, alias: str):
        self.alias = alias
        
    @property
    def alias(self) -> str:
        return self.__alias

    @alias.setter
    def alias(self, alias: str):
        self.__alias = alias

class transformation_Transformation:

    def __init__(self, name: str, transformation_Transformation: set["transformation_MetamodelDeclaration"] = None, transformation_Transformation2: set["transformation_AbstractMapping"] = None):
        self.name = name
        self.transformation_Transformation = transformation_Transformation if transformation_Transformation is not None else set()
        self.transformation_Transformation2 = transformation_Transformation2 if transformation_Transformation2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def transformation_Transformation2(self):
        return self.__transformation_Transformation2

    @transformation_Transformation2.setter
    def transformation_Transformation2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_transformation_Transformation__transformation_Transformation2", None)
        self.__transformation_Transformation2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "transformation_AbstractMapping"):
                    opp_val = getattr(item, "transformation_AbstractMapping", None)
                    
                    if opp_val == self:
                        setattr(item, "transformation_AbstractMapping", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "transformation_AbstractMapping"):
                    opp_val = getattr(item, "transformation_AbstractMapping", None)
                    
                    setattr(item, "transformation_AbstractMapping", self)
                    

    @property
    def transformation_Transformation(self):
        return self.__transformation_Transformation

    @transformation_Transformation.setter
    def transformation_Transformation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_transformation_Transformation__transformation_Transformation", None)
        self.__transformation_Transformation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "transformation_MetamodelDeclaration"):
                    opp_val = getattr(item, "transformation_MetamodelDeclaration", None)
                    
                    if opp_val == self:
                        setattr(item, "transformation_MetamodelDeclaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "transformation_MetamodelDeclaration"):
                    opp_val = getattr(item, "transformation_MetamodelDeclaration", None)
                    
                    setattr(item, "transformation_MetamodelDeclaration", self)
                    
