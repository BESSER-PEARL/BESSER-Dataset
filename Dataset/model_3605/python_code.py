from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class UnaryExpression:

    pass
class gremlin_NotExpression(UnaryExpression):

    def __init__(self):
        
    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class Expression:

    pass
class gremlin_StringLiteral(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class gremlin_BinaryExpression(Expression):

    pass
class gremlin_NullLiteral(Expression):

    def __init__(self):
        
    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class gremlin_BooleanLiteral(Expression):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class gremlin_DoubleLiteral(Expression):

    def __init__(self, value: float):
        self.value = value
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class gremlin_TernaryOperator(Expression):

    def __init__(self, gremlin_TernaryOperator: "gremlin_Instruction" = None, gremlin_TernaryOperator70: "gremlin_Instruction" = None, gremlin_TernaryOperator73: "gremlin_Instruction" = None):
        self.gremlin_TernaryOperator = gremlin_TernaryOperator
        self.gremlin_TernaryOperator70 = gremlin_TernaryOperator70
        self.gremlin_TernaryOperator73 = gremlin_TernaryOperator73
        
    @property
    def gremlin_TernaryOperator73(self):
        return self.__gremlin_TernaryOperator73

    @gremlin_TernaryOperator73.setter
    def gremlin_TernaryOperator73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gremlin_TernaryOperator__gremlin_TernaryOperator73", None)
        self.__gremlin_TernaryOperator73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gremlin_Instruction74"):
                opp_val = getattr(old_value, "gremlin_Instruction74", None)
                if opp_val == self:
                    setattr(old_value, "gremlin_Instruction74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gremlin_Instruction74"):
                opp_val = getattr(value, "gremlin_Instruction74", None)
                setattr(value, "gremlin_Instruction74", self)

    @property
    def gremlin_TernaryOperator(self):
        return self.__gremlin_TernaryOperator

    @gremlin_TernaryOperator.setter
    def gremlin_TernaryOperator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gremlin_TernaryOperator__gremlin_TernaryOperator", None)
        self.__gremlin_TernaryOperator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gremlin_Instruction68"):
                opp_val = getattr(old_value, "gremlin_Instruction68", None)
                if opp_val == self:
                    setattr(old_value, "gremlin_Instruction68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gremlin_Instruction68"):
                opp_val = getattr(value, "gremlin_Instruction68", None)
                setattr(value, "gremlin_Instruction68", self)

    @property
    def gremlin_TernaryOperator70(self):
        return self.__gremlin_TernaryOperator70

    @gremlin_TernaryOperator70.setter
    def gremlin_TernaryOperator70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gremlin_TernaryOperator__gremlin_TernaryOperator70", None)
        self.__gremlin_TernaryOperator70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gremlin_Instruction71"):
                opp_val = getattr(old_value, "gremlin_Instruction71", None)
                if opp_val == self:
                    setattr(old_value, "gremlin_Instruction71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gremlin_Instruction71"):
                opp_val = getattr(value, "gremlin_Instruction71", None)
                setattr(value, "gremlin_Instruction71", self)

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class gremlin_IntegerLiteral(Expression):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class gremlin_UnaryExpression(Expression):

    pass
class BinaryExpression:

    pass
class gremlin_InExpression(BinaryExpression):

    def __init__(self):
        
    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class gremlin_AndExpression(BinaryExpression):

    def __init__(self):
        
    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class gremlin_AffectationExpression(BinaryExpression):

    def __init__(self):
        
    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class gremlin_OrExpression(BinaryExpression):

    def __init__(self):
        
    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class gremlin_GreaterExpression(BinaryExpression):

    def __init__(self):
        
    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class gremlin_LeftShiftExpression(BinaryExpression):

    def __init__(self):
        
    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class gremlin_DifferenceExpression(BinaryExpression):

    def __init__(self):
        
    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class gremlin_LessOrEqualExpression(BinaryExpression):

    def __init__(self):
        
    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class gremlin_LessExpression(BinaryExpression):

    def __init__(self):
        
    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class gremlin_PlusExpression(BinaryExpression):

    def __init__(self):
        
    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class gremlin_GreaterOrEqualExpression(BinaryExpression):

    def __init__(self):
        
    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class gremlin_EqualityExpression(BinaryExpression):

    def __init__(self):
        
    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class gremlin_EObject:

    pass
class MethodCall:

    pass
class gremlin_NextCall(MethodCall):

    def __init__(self):
        
    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class gremlin_CountCall(MethodCall):

    def __init__(self):
        
    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class gremlin_SizeCall(MethodCall):

    def __init__(self):
        
    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class gremlin_ToIntegerCall(MethodCall):

    def __init__(self):
        
    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class gremlin_AddAllCall(MethodCall):

    def __init__(self, gremlin_AddAllCall: "gremlin_Instruction" = None):
        self.gremlin_AddAllCall = gremlin_AddAllCall
        
    @property
    def gremlin_AddAllCall(self):
        return self.__gremlin_AddAllCall

    @gremlin_AddAllCall.setter
    def gremlin_AddAllCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gremlin_AddAllCall__gremlin_AddAllCall", None)
        self.__gremlin_AddAllCall = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gremlin_Instruction41"):
                opp_val = getattr(old_value, "gremlin_Instruction41", None)
                if opp_val == self:
                    setattr(old_value, "gremlin_Instruction41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gremlin_Instruction41"):
                opp_val = getattr(value, "gremlin_Instruction41", None)
                setattr(value, "gremlin_Instruction41", self)

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class gremlin_UnionCall(MethodCall):

    def __init__(self, gremlin_UnionCall: "gremlin_Instruction" = None, gremlin_UnionCall47: "gremlin_Instruction" = None, gremlin_UnionCall50: "gremlin_TypeDeclaration" = None):
        self.gremlin_UnionCall = gremlin_UnionCall
        self.gremlin_UnionCall47 = gremlin_UnionCall47
        self.gremlin_UnionCall50 = gremlin_UnionCall50
        
    @property
    def gremlin_UnionCall47(self):
        return self.__gremlin_UnionCall47

    @gremlin_UnionCall47.setter
    def gremlin_UnionCall47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gremlin_UnionCall__gremlin_UnionCall47", None)
        self.__gremlin_UnionCall47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gremlin_Instruction48"):
                opp_val = getattr(old_value, "gremlin_Instruction48", None)
                if opp_val == self:
                    setattr(old_value, "gremlin_Instruction48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gremlin_Instruction48"):
                opp_val = getattr(value, "gremlin_Instruction48", None)
                setattr(value, "gremlin_Instruction48", self)

    @property
    def gremlin_UnionCall50(self):
        return self.__gremlin_UnionCall50

    @gremlin_UnionCall50.setter
    def gremlin_UnionCall50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gremlin_UnionCall__gremlin_UnionCall50", None)
        self.__gremlin_UnionCall50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gremlin_TypeDeclaration51"):
                opp_val = getattr(old_value, "gremlin_TypeDeclaration51", None)
                if opp_val == self:
                    setattr(old_value, "gremlin_TypeDeclaration51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gremlin_TypeDeclaration51"):
                opp_val = getattr(value, "gremlin_TypeDeclaration51", None)
                setattr(value, "gremlin_TypeDeclaration51", self)

    @property
    def gremlin_UnionCall(self):
        return self.__gremlin_UnionCall

    @gremlin_UnionCall.setter
    def gremlin_UnionCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gremlin_UnionCall__gremlin_UnionCall", None)
        self.__gremlin_UnionCall = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gremlin_Instruction45"):
                opp_val = getattr(old_value, "gremlin_Instruction45", None)
                if opp_val == self:
                    setattr(old_value, "gremlin_Instruction45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gremlin_Instruction45"):
                opp_val = getattr(value, "gremlin_Instruction45", None)
                setattr(value, "gremlin_Instruction45", self)

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class gremlin_ToListCall(MethodCall):

    def __init__(self):
        
    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class gremlin_FirstCall(MethodCall):

    def __init__(self):
        
    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class gremlin_HasNextCall(MethodCall):

    def __init__(self):
        
    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class gremlin_IndexCall(MethodCall):

    def __init__(self, indexName: str, indexProperty: str, indexQuery: str):
        self.indexName = indexName
        self.indexProperty = indexProperty
        self.indexQuery = indexQuery
        
    @property
    def indexQuery(self) -> str:
        return self.__indexQuery

    @indexQuery.setter
    def indexQuery(self, indexQuery: str):
        self.__indexQuery = indexQuery

    @property
    def indexName(self) -> str:
        return self.__indexName

    @indexName.setter
    def indexName(self, indexName: str):
        self.__indexName = indexName

    @property
    def indexProperty(self) -> str:
        return self.__indexProperty

    @indexProperty.setter
    def indexProperty(self, indexProperty: str):
        self.__indexProperty = indexProperty

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class gremlin_IntersectionCall(MethodCall):

    def __init__(self, gremlin_IntersectionCall: "gremlin_Instruction" = None, gremlin_IntersectionCall55: "gremlin_Instruction" = None, gremlin_IntersectionCall58: "gremlin_TypeDeclaration" = None):
        self.gremlin_IntersectionCall = gremlin_IntersectionCall
        self.gremlin_IntersectionCall55 = gremlin_IntersectionCall55
        self.gremlin_IntersectionCall58 = gremlin_IntersectionCall58
        
    @property
    def gremlin_IntersectionCall55(self):
        return self.__gremlin_IntersectionCall55

    @gremlin_IntersectionCall55.setter
    def gremlin_IntersectionCall55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gremlin_IntersectionCall__gremlin_IntersectionCall55", None)
        self.__gremlin_IntersectionCall55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gremlin_Instruction56"):
                opp_val = getattr(old_value, "gremlin_Instruction56", None)
                if opp_val == self:
                    setattr(old_value, "gremlin_Instruction56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gremlin_Instruction56"):
                opp_val = getattr(value, "gremlin_Instruction56", None)
                setattr(value, "gremlin_Instruction56", self)

    @property
    def gremlin_IntersectionCall(self):
        return self.__gremlin_IntersectionCall

    @gremlin_IntersectionCall.setter
    def gremlin_IntersectionCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gremlin_IntersectionCall__gremlin_IntersectionCall", None)
        self.__gremlin_IntersectionCall = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gremlin_Instruction53"):
                opp_val = getattr(old_value, "gremlin_Instruction53", None)
                if opp_val == self:
                    setattr(old_value, "gremlin_Instruction53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gremlin_Instruction53"):
                opp_val = getattr(value, "gremlin_Instruction53", None)
                setattr(value, "gremlin_Instruction53", self)

    @property
    def gremlin_IntersectionCall58(self):
        return self.__gremlin_IntersectionCall58

    @gremlin_IntersectionCall58.setter
    def gremlin_IntersectionCall58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gremlin_IntersectionCall__gremlin_IntersectionCall58", None)
        self.__gremlin_IntersectionCall58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gremlin_TypeDeclaration59"):
                opp_val = getattr(old_value, "gremlin_TypeDeclaration59", None)
                if opp_val == self:
                    setattr(old_value, "gremlin_TypeDeclaration59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gremlin_TypeDeclaration59"):
                opp_val = getattr(value, "gremlin_TypeDeclaration59", None)
                setattr(value, "gremlin_TypeDeclaration59", self)

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class gremlin_ContainsAllCall(MethodCall):

    def __init__(self, gremlin_ContainsAllCall: "gremlin_Instruction" = None):
        self.gremlin_ContainsAllCall = gremlin_ContainsAllCall
        
    @property
    def gremlin_ContainsAllCall(self):
        return self.__gremlin_ContainsAllCall

    @gremlin_ContainsAllCall.setter
    def gremlin_ContainsAllCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gremlin_ContainsAllCall__gremlin_ContainsAllCall", None)
        self.__gremlin_ContainsAllCall = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gremlin_Instruction39"):
                opp_val = getattr(old_value, "gremlin_Instruction39", None)
                if opp_val == self:
                    setattr(old_value, "gremlin_Instruction39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gremlin_Instruction39"):
                opp_val = getattr(value, "gremlin_Instruction39", None)
                setattr(value, "gremlin_Instruction39", self)

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class gremlin_RetainAllCall(MethodCall):

    def __init__(self, gremlin_RetainAllCall: "gremlin_Instruction" = None):
        self.gremlin_RetainAllCall = gremlin_RetainAllCall
        
    @property
    def gremlin_RetainAllCall(self):
        return self.__gremlin_RetainAllCall

    @gremlin_RetainAllCall.setter
    def gremlin_RetainAllCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gremlin_RetainAllCall__gremlin_RetainAllCall", None)
        self.__gremlin_RetainAllCall = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gremlin_Instruction43"):
                opp_val = getattr(old_value, "gremlin_Instruction43", None)
                if opp_val == self:
                    setattr(old_value, "gremlin_Instruction43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gremlin_Instruction43"):
                opp_val = getattr(value, "gremlin_Instruction43", None)
                setattr(value, "gremlin_Instruction43", self)

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class gremlin_IsEmptyCall(MethodCall):

    def __init__(self):
        
    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class gremlin_ContainsCall(MethodCall):

    def __init__(self, gremlin_ContainsCall: "gremlin_Instruction" = None):
        self.gremlin_ContainsCall = gremlin_ContainsCall
        
    @property
    def gremlin_ContainsCall(self):
        return self.__gremlin_ContainsCall

    @gremlin_ContainsCall.setter
    def gremlin_ContainsCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gremlin_ContainsCall__gremlin_ContainsCall", None)
        self.__gremlin_ContainsCall = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gremlin_Instruction37"):
                opp_val = getattr(old_value, "gremlin_Instruction37", None)
                if opp_val == self:
                    setattr(old_value, "gremlin_Instruction37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gremlin_Instruction37"):
                opp_val = getattr(value, "gremlin_Instruction37", None)
                setattr(value, "gremlin_Instruction37", self)

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class gremlin_CustomMethodCall(MethodCall):

    def __init__(self, name: str, gremlin_CustomMethodCall: set["gremlin_EObject"] = None):
        self.name = name
        self.gremlin_CustomMethodCall = gremlin_CustomMethodCall if gremlin_CustomMethodCall is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def gremlin_CustomMethodCall(self):
        return self.__gremlin_CustomMethodCall

    @gremlin_CustomMethodCall.setter
    def gremlin_CustomMethodCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gremlin_CustomMethodCall__gremlin_CustomMethodCall", None)
        self.__gremlin_CustomMethodCall = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gremlin_EObject"):
                    opp_val = getattr(item, "gremlin_EObject", None)
                    
                    if opp_val == self:
                        setattr(item, "gremlin_EObject", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gremlin_EObject"):
                    opp_val = getattr(item, "gremlin_EObject", None)
                    
                    setattr(item, "gremlin_EObject", self)
                    

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class Step:

    pass
class gremlin_RetainStep(Step):

    def __init__(self, gremlin_RetainStep: "gremlin_CollectionDefinition" = None):
        self.gremlin_RetainStep = gremlin_RetainStep
        
    @property
    def gremlin_RetainStep(self):
        return self.__gremlin_RetainStep

    @gremlin_RetainStep.setter
    def gremlin_RetainStep(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gremlin_RetainStep__gremlin_RetainStep", None)
        self.__gremlin_RetainStep = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gremlin_CollectionDefinition28"):
                opp_val = getattr(old_value, "gremlin_CollectionDefinition28", None)
                if opp_val == self:
                    setattr(old_value, "gremlin_CollectionDefinition28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gremlin_CollectionDefinition28"):
                opp_val = getattr(value, "gremlin_CollectionDefinition28", None)
                setattr(value, "gremlin_CollectionDefinition28", self)

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class gremlin_OutVStep(Step):

    def __init__(self):
        
    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class gremlin_InEStep(Step):

    def __init__(self, relationshipName: str):
        self.relationshipName = relationshipName
        
    @property
    def relationshipName(self) -> str:
        return self.__relationshipName

    @relationshipName.setter
    def relationshipName(self, relationshipName: str):
        self.__relationshipName = relationshipName

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class gremlin_ScatterStep(Step):

    def __init__(self):
        
    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class gremlin_GatherStep(Step):

    def __init__(self, gremlin_GatherStep: "gremlin_Closure" = None):
        self.gremlin_GatherStep = gremlin_GatherStep
        
    @property
    def gremlin_GatherStep(self):
        return self.__gremlin_GatherStep

    @gremlin_GatherStep.setter
    def gremlin_GatherStep(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gremlin_GatherStep__gremlin_GatherStep", None)
        self.__gremlin_GatherStep = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gremlin_Closure34"):
                opp_val = getattr(old_value, "gremlin_Closure34", None)
                if opp_val == self:
                    setattr(old_value, "gremlin_Closure34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gremlin_Closure34"):
                opp_val = getattr(value, "gremlin_Closure34", None)
                setattr(value, "gremlin_Closure34", self)

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class gremlin_TransformStep(Step):

    def __init__(self, gremlin_TransformStep: "gremlin_Closure" = None):
        self.gremlin_TransformStep = gremlin_TransformStep
        
    @property
    def gremlin_TransformStep(self):
        return self.__gremlin_TransformStep

    @gremlin_TransformStep.setter
    def gremlin_TransformStep(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gremlin_TransformStep__gremlin_TransformStep", None)
        self.__gremlin_TransformStep = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gremlin_Closure32"):
                opp_val = getattr(old_value, "gremlin_Closure32", None)
                if opp_val == self:
                    setattr(old_value, "gremlin_Closure32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gremlin_Closure32"):
                opp_val = getattr(value, "gremlin_Closure32", None)
                setattr(value, "gremlin_Closure32", self)

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class gremlin_StartStep(Step):

    def __init__(self):
        
    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class gremlin_FilterStep(Step):

    def __init__(self, gremlin_FilterStep: "gremlin_Closure" = None):
        self.gremlin_FilterStep = gremlin_FilterStep
        
    @property
    def gremlin_FilterStep(self):
        return self.__gremlin_FilterStep

    @gremlin_FilterStep.setter
    def gremlin_FilterStep(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gremlin_FilterStep__gremlin_FilterStep", None)
        self.__gremlin_FilterStep = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gremlin_Closure26"):
                opp_val = getattr(old_value, "gremlin_Closure26", None)
                if opp_val == self:
                    setattr(old_value, "gremlin_Closure26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gremlin_Closure26"):
                opp_val = getattr(value, "gremlin_Closure26", None)
                setattr(value, "gremlin_Closure26", self)

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class gremlin_OutEStep(Step):

    def __init__(self, relationshipName: str):
        self.relationshipName = relationshipName
        
    @property
    def relationshipName(self) -> str:
        return self.__relationshipName

    @relationshipName.setter
    def relationshipName(self, relationshipName: str):
        self.__relationshipName = relationshipName

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class gremlin_FillStep(Step):

    def __init__(self, gremlin_FillStep: "gremlin_Instruction" = None):
        self.gremlin_FillStep = gremlin_FillStep
        
    @property
    def gremlin_FillStep(self):
        return self.__gremlin_FillStep

    @gremlin_FillStep.setter
    def gremlin_FillStep(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gremlin_FillStep__gremlin_FillStep", None)
        self.__gremlin_FillStep = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gremlin_Instruction22"):
                opp_val = getattr(old_value, "gremlin_Instruction22", None)
                if opp_val == self:
                    setattr(old_value, "gremlin_Instruction22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gremlin_Instruction22"):
                opp_val = getattr(value, "gremlin_Instruction22", None)
                setattr(value, "gremlin_Instruction22", self)

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class gremlin_InVStep(Step):

    def __init__(self):
        
    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class gremlin_CustomStep(Step):

    def __init__(self, name: str, gremlin_CustomStep: set["gremlin_EObject"] = None):
        self.name = name
        self.gremlin_CustomStep = gremlin_CustomStep if gremlin_CustomStep is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def gremlin_CustomStep(self):
        return self.__gremlin_CustomStep

    @gremlin_CustomStep.setter
    def gremlin_CustomStep(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gremlin_CustomStep__gremlin_CustomStep", None)
        self.__gremlin_CustomStep = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gremlin_EObject76"):
                    opp_val = getattr(item, "gremlin_EObject76", None)
                    
                    if opp_val == self:
                        setattr(item, "gremlin_EObject76", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gremlin_EObject76"):
                    opp_val = getattr(item, "gremlin_EObject76", None)
                    
                    setattr(item, "gremlin_EObject76", self)
                    

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class gremlin_ExceptStep(Step):

    def __init__(self, gremlin_ExceptStep: "gremlin_CollectionDefinition" = None):
        self.gremlin_ExceptStep = gremlin_ExceptStep
        
    @property
    def gremlin_ExceptStep(self):
        return self.__gremlin_ExceptStep

    @gremlin_ExceptStep.setter
    def gremlin_ExceptStep(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gremlin_ExceptStep__gremlin_ExceptStep", None)
        self.__gremlin_ExceptStep = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gremlin_CollectionDefinition30"):
                opp_val = getattr(old_value, "gremlin_CollectionDefinition30", None)
                if opp_val == self:
                    setattr(old_value, "gremlin_CollectionDefinition30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gremlin_CollectionDefinition30"):
                opp_val = getattr(value, "gremlin_CollectionDefinition30", None)
                setattr(value, "gremlin_CollectionDefinition30", self)

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class gremlin_EdgesStep(Step):

    def __init__(self, relationshipName: str):
        self.relationshipName = relationshipName
        
    @property
    def relationshipName(self) -> str:
        return self.__relationshipName

    @relationshipName.setter
    def relationshipName(self, relationshipName: str):
        self.__relationshipName = relationshipName

class gremlin_PropertyStep(Step):

    def __init__(self, name: str, gremlin_PropertyStep: "gremlin_Instruction" = None):
        self.name = name
        self.gremlin_PropertyStep = gremlin_PropertyStep
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def gremlin_PropertyStep(self):
        return self.__gremlin_PropertyStep

    @gremlin_PropertyStep.setter
    def gremlin_PropertyStep(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gremlin_PropertyStep__gremlin_PropertyStep", None)
        self.__gremlin_PropertyStep = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gremlin_Instruction24"):
                opp_val = getattr(old_value, "gremlin_Instruction24", None)
                if opp_val == self:
                    setattr(old_value, "gremlin_Instruction24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gremlin_Instruction24"):
                opp_val = getattr(value, "gremlin_Instruction24", None)
                setattr(value, "gremlin_Instruction24", self)

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class gremlin_IdentityStep(Step):

    def __init__(self, needed: bool):
        self.needed = needed
        
    @property
    def needed(self) -> bool:
        return self.__needed

    @needed.setter
    def needed(self, needed: bool):
        self.__needed = needed

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class gremlin_VerticesStep(Step):

    def __init__(self, vertexId: str):
        self.vertexId = vertexId
        
    @property
    def vertexId(self) -> str:
        return self.__vertexId

    @vertexId.setter
    def vertexId(self, vertexId: str):
        self.__vertexId = vertexId

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class VariableAccess:

    pass
class gremlin_ClosureIt(VariableAccess):

    def __init__(self):
        
    def getName(self) -> str:
        # TODO: Implement getName method
        pass

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class TraversalElement:

    pass
class gremlin_VariableAccess(TraversalElement):

    def __init__(self, name: str, gremlin_VariableAccess: "gremlin_TypeDeclaration" = None):
        self.name = name
        self.gremlin_VariableAccess = gremlin_VariableAccess
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def gremlin_VariableAccess(self):
        return self.__gremlin_VariableAccess

    @gremlin_VariableAccess.setter
    def gremlin_VariableAccess(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gremlin_VariableAccess__gremlin_VariableAccess", None)
        self.__gremlin_VariableAccess = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gremlin_TypeDeclaration20"):
                opp_val = getattr(old_value, "gremlin_TypeDeclaration20", None)
                if opp_val == self:
                    setattr(old_value, "gremlin_TypeDeclaration20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gremlin_TypeDeclaration20"):
                opp_val = getattr(value, "gremlin_TypeDeclaration20", None)
                setattr(value, "gremlin_TypeDeclaration20", self)

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class gremlin_MethodCall(TraversalElement):

    pass
class gremlin_Step(TraversalElement):

    pass
class gremlin_CollectionDefinition(TraversalElement):

    def __init__(self, gremlin_CollectionDefinition: set["gremlin_Instruction"] = None, gremlin_CollectionDefinition15: "gremlin_TypeDeclaration" = None, gremlin_CollectionDefinition28: "gremlin_RetainStep" = None, gremlin_CollectionDefinition30: "gremlin_ExceptStep" = None):
        self.gremlin_CollectionDefinition = gremlin_CollectionDefinition if gremlin_CollectionDefinition is not None else set()
        self.gremlin_CollectionDefinition15 = gremlin_CollectionDefinition15
        self.gremlin_CollectionDefinition28 = gremlin_CollectionDefinition28
        self.gremlin_CollectionDefinition30 = gremlin_CollectionDefinition30
        
    @property
    def gremlin_CollectionDefinition15(self):
        return self.__gremlin_CollectionDefinition15

    @gremlin_CollectionDefinition15.setter
    def gremlin_CollectionDefinition15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gremlin_CollectionDefinition__gremlin_CollectionDefinition15", None)
        self.__gremlin_CollectionDefinition15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gremlin_TypeDeclaration16"):
                opp_val = getattr(old_value, "gremlin_TypeDeclaration16", None)
                if opp_val == self:
                    setattr(old_value, "gremlin_TypeDeclaration16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gremlin_TypeDeclaration16"):
                opp_val = getattr(value, "gremlin_TypeDeclaration16", None)
                setattr(value, "gremlin_TypeDeclaration16", self)

    @property
    def gremlin_CollectionDefinition28(self):
        return self.__gremlin_CollectionDefinition28

    @gremlin_CollectionDefinition28.setter
    def gremlin_CollectionDefinition28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gremlin_CollectionDefinition__gremlin_CollectionDefinition28", None)
        self.__gremlin_CollectionDefinition28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gremlin_RetainStep"):
                opp_val = getattr(old_value, "gremlin_RetainStep", None)
                if opp_val == self:
                    setattr(old_value, "gremlin_RetainStep", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gremlin_RetainStep"):
                opp_val = getattr(value, "gremlin_RetainStep", None)
                setattr(value, "gremlin_RetainStep", self)

    @property
    def gremlin_CollectionDefinition30(self):
        return self.__gremlin_CollectionDefinition30

    @gremlin_CollectionDefinition30.setter
    def gremlin_CollectionDefinition30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gremlin_CollectionDefinition__gremlin_CollectionDefinition30", None)
        self.__gremlin_CollectionDefinition30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gremlin_ExceptStep"):
                opp_val = getattr(old_value, "gremlin_ExceptStep", None)
                if opp_val == self:
                    setattr(old_value, "gremlin_ExceptStep", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gremlin_ExceptStep"):
                opp_val = getattr(value, "gremlin_ExceptStep", None)
                setattr(value, "gremlin_ExceptStep", self)

    @property
    def gremlin_CollectionDefinition(self):
        return self.__gremlin_CollectionDefinition

    @gremlin_CollectionDefinition.setter
    def gremlin_CollectionDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gremlin_CollectionDefinition__gremlin_CollectionDefinition", None)
        self.__gremlin_CollectionDefinition = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gremlin_Instruction13"):
                    opp_val = getattr(item, "gremlin_Instruction13", None)
                    
                    if opp_val == self:
                        setattr(item, "gremlin_Instruction13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gremlin_Instruction13"):
                    opp_val = getattr(item, "gremlin_Instruction13", None)
                    
                    setattr(item, "gremlin_Instruction13", self)
                    

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class TypeDeclaration:

    pass
class gremlin_SortedSetDeclaration(TypeDeclaration):

    def __init__(self):
        
    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class gremlin_SetDeclaration(TypeDeclaration):

    def __init__(self):
        
    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class gremlin_ListDeclaration(TypeDeclaration):

    def __init__(self):
        
    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class Instruction:

    pass
class gremlin_TraversalElement(Instruction):

    pass
class gremlin_Expression(Instruction):

    pass
class gremlin_VariableDeclaration(Instruction):

    def __init__(self, name: str, final: bool, gremlin_VariableDeclaration: "gremlin_Instruction" = None, gremlin_VariableDeclaration6: "gremlin_TypeDeclaration" = None):
        self.name = name
        self.final = final
        self.gremlin_VariableDeclaration = gremlin_VariableDeclaration
        self.gremlin_VariableDeclaration6 = gremlin_VariableDeclaration6
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def final(self) -> bool:
        return self.__final

    @final.setter
    def final(self, final: bool):
        self.__final = final

    @property
    def gremlin_VariableDeclaration6(self):
        return self.__gremlin_VariableDeclaration6

    @gremlin_VariableDeclaration6.setter
    def gremlin_VariableDeclaration6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gremlin_VariableDeclaration__gremlin_VariableDeclaration6", None)
        self.__gremlin_VariableDeclaration6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gremlin_TypeDeclaration"):
                opp_val = getattr(old_value, "gremlin_TypeDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "gremlin_TypeDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gremlin_TypeDeclaration"):
                opp_val = getattr(value, "gremlin_TypeDeclaration", None)
                setattr(value, "gremlin_TypeDeclaration", self)

    @property
    def gremlin_VariableDeclaration(self):
        return self.__gremlin_VariableDeclaration

    @gremlin_VariableDeclaration.setter
    def gremlin_VariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gremlin_VariableDeclaration__gremlin_VariableDeclaration", None)
        self.__gremlin_VariableDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gremlin_Instruction4"):
                opp_val = getattr(old_value, "gremlin_Instruction4", None)
                if opp_val == self:
                    setattr(old_value, "gremlin_Instruction4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gremlin_Instruction4"):
                opp_val = getattr(value, "gremlin_Instruction4", None)
                setattr(value, "gremlin_Instruction4", self)

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class gremlin_TypeDeclaration(Instruction):

    pass
class gremlin_MethodDeclaration(Instruction):

    def __init__(self, name: str, parameters: str, gremlin_MethodDeclaration: set["gremlin_Instruction"] = None):
        self.name = name
        self.parameters = parameters
        self.gremlin_MethodDeclaration = gremlin_MethodDeclaration if gremlin_MethodDeclaration is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def parameters(self) -> str:
        return self.__parameters

    @parameters.setter
    def parameters(self, parameters: str):
        self.__parameters = parameters

    @property
    def gremlin_MethodDeclaration(self):
        return self.__gremlin_MethodDeclaration

    @gremlin_MethodDeclaration.setter
    def gremlin_MethodDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gremlin_MethodDeclaration__gremlin_MethodDeclaration", None)
        self.__gremlin_MethodDeclaration = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gremlin_Instruction2"):
                    opp_val = getattr(item, "gremlin_Instruction2", None)
                    
                    if opp_val == self:
                        setattr(item, "gremlin_Instruction2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gremlin_Instruction2"):
                    opp_val = getattr(item, "gremlin_Instruction2", None)
                    
                    setattr(item, "gremlin_Instruction2", self)
                    

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class gremlin_Closure(Instruction):

    def __init__(self, gremlin_Closure: set["gremlin_Instruction"] = None, gremlin_Closure26: "gremlin_FilterStep" = None, gremlin_Closure32: "gremlin_TransformStep" = None, gremlin_Closure34: "gremlin_GatherStep" = None):
        self.gremlin_Closure = gremlin_Closure if gremlin_Closure is not None else set()
        self.gremlin_Closure26 = gremlin_Closure26
        self.gremlin_Closure32 = gremlin_Closure32
        self.gremlin_Closure34 = gremlin_Closure34
        
    @property
    def gremlin_Closure26(self):
        return self.__gremlin_Closure26

    @gremlin_Closure26.setter
    def gremlin_Closure26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gremlin_Closure__gremlin_Closure26", None)
        self.__gremlin_Closure26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gremlin_FilterStep"):
                opp_val = getattr(old_value, "gremlin_FilterStep", None)
                if opp_val == self:
                    setattr(old_value, "gremlin_FilterStep", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gremlin_FilterStep"):
                opp_val = getattr(value, "gremlin_FilterStep", None)
                setattr(value, "gremlin_FilterStep", self)

    @property
    def gremlin_Closure32(self):
        return self.__gremlin_Closure32

    @gremlin_Closure32.setter
    def gremlin_Closure32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gremlin_Closure__gremlin_Closure32", None)
        self.__gremlin_Closure32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gremlin_TransformStep"):
                opp_val = getattr(old_value, "gremlin_TransformStep", None)
                if opp_val == self:
                    setattr(old_value, "gremlin_TransformStep", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gremlin_TransformStep"):
                opp_val = getattr(value, "gremlin_TransformStep", None)
                setattr(value, "gremlin_TransformStep", self)

    @property
    def gremlin_Closure(self):
        return self.__gremlin_Closure

    @gremlin_Closure.setter
    def gremlin_Closure(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gremlin_Closure__gremlin_Closure", None)
        self.__gremlin_Closure = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gremlin_Instruction18"):
                    opp_val = getattr(item, "gremlin_Instruction18", None)
                    
                    if opp_val == self:
                        setattr(item, "gremlin_Instruction18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gremlin_Instruction18"):
                    opp_val = getattr(item, "gremlin_Instruction18", None)
                    
                    setattr(item, "gremlin_Instruction18", self)
                    

    @property
    def gremlin_Closure34(self):
        return self.__gremlin_Closure34

    @gremlin_Closure34.setter
    def gremlin_Closure34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gremlin_Closure__gremlin_Closure34", None)
        self.__gremlin_Closure34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gremlin_GatherStep"):
                opp_val = getattr(old_value, "gremlin_GatherStep", None)
                if opp_val == self:
                    setattr(old_value, "gremlin_GatherStep", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gremlin_GatherStep"):
                opp_val = getattr(value, "gremlin_GatherStep", None)
                setattr(value, "gremlin_GatherStep", self)

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class gremlin_ReturnStatement(Instruction):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class gremlin_Instruction(ABC):

    pass
class gremlin_GremlinScript:

    def __init__(self, name: str, gremlin_GremlinScript: set["gremlin_Instruction"] = None):
        self.name = name
        self.gremlin_GremlinScript = gremlin_GremlinScript if gremlin_GremlinScript is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def gremlin_GremlinScript(self):
        return self.__gremlin_GremlinScript

    @gremlin_GremlinScript.setter
    def gremlin_GremlinScript(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gremlin_GremlinScript__gremlin_GremlinScript", None)
        self.__gremlin_GremlinScript = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gremlin_Instruction"):
                    opp_val = getattr(item, "gremlin_Instruction", None)
                    
                    if opp_val == self:
                        setattr(item, "gremlin_Instruction", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gremlin_Instruction"):
                    opp_val = getattr(item, "gremlin_Instruction", None)
                    
                    setattr(item, "gremlin_Instruction", self)
                    

    def toString(self) -> str:
        # TODO: Implement toString method
        pass
