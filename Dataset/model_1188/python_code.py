from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class OperatorKind(Enum):
    OR = "OR"
    XOR = "XOR"
    IMPLIES = "IMPLIES"
    NOT = "NOT"
    MUL = "MUL"
    DIV = "DIV"
    MINUS = "MINUS"
    PLUS = "PLUS"
    LESS = "LESS"
    GREATER = "GREATER"
    LESS_OR_EQUAL = "LESS_OR_EQUAL"
    GREATER_OR_EQUAL = "GREATER_OR_EQUAL"
    EQUAL = "EQUAL"
    DISTINCT = "DISTINCT"
    AND = "AND"


############################################
# Definition of Classes
############################################

class ir_ocl_OclAnyLibElement:

    pass
class CollectionLiteralExp:

    pass
class ir_ocl_BagLiteralExp(CollectionLiteralExp):

    pass
class ir_ocl_OrderedSetLiteralExp(CollectionLiteralExp):

    pass
class ir_ocl_SequenceLiteralExp(CollectionLiteralExp):

    pass
class ir_ocl_SetLiteralExp(CollectionLiteralExp):

    pass
class ocl_ir_EFTupleType:

    pass
class LiteralExp:

    pass
class ir_ocl_RealLiteralExp(LiteralExp):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class ir_ocl_IntegerLiteralExp(LiteralExp):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class ir_ocl_CollectionLiteralExp(LiteralExp):

    pass
class ir_ocl_OclUndefined(LiteralExp):

    pass
class ir_ocl_TupleLiteralExp(LiteralExp):

    pass
class ir_ocl_OclInvalid(LiteralExp):

    pass
class ir_ocl_StringLiteralExp(LiteralExp):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class ir_ocl_BooleanLiteralExp(LiteralExp):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class ocl_ir_EFEnumLiteral:

    pass
class ocl_ir_MetaTypeRef:

    pass
class ir_ocl_EnumLiteralExp(LiteralExp):

    pass
class ir_ocl_TuplePart:

    def __init__(self, name: str, ir_ocl_TuplePart: "OclExpression" = None):
        self.name = name
        self.ir_ocl_TuplePart = ir_ocl_TuplePart
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ir_ocl_TuplePart(self):
        return self.__ir_ocl_TuplePart

    @ir_ocl_TuplePart.setter
    def ir_ocl_TuplePart(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_ocl_TuplePart__ir_ocl_TuplePart", None)
        self.__ir_ocl_TuplePart = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression98"):
                opp_val = getattr(old_value, "OclExpression98", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression98", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression98"):
                opp_val = getattr(value, "OclExpression98", None)
                setattr(value, "OclExpression98", self)

class TuplePart:

    pass
class LoopExp:

    pass
class ir_ocl_IterateExp(LoopExp):

    pass
class ir_ocl_IteratorExp(LoopExp):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class Iterator:

    pass
class ocl_ir_PropertyFeatureRef:

    pass
class ocl_ir_TypeRef:

    pass
class ir_ocl_OclExpression(ABC):

    pass
class Operation:

    pass
class DerivedProperty:

    pass
class OclExpression:

    pass
class ir_ocl_UnsupportedExp(OclExpression):

    def __init__(self, reason: str, description: str, OclExpression78: "ir_ocl_IfExp", OclExpression91: "ir_ocl_OperatorCallExp", OclExpression60: "ir_ocl_CallExp", OclExpression86: "ir_ocl_LetExp", OclExpression89: "ir_ocl_LetExp", OclExpression73: "ir_ocl_IterateExp", OclExpression68: "ir_ocl_LoopExp", OclExpression: "ir_ocl_OclInvariant", OclExpression55: "ir_ocl_OclDerivedProperty", OclExpression98: "ir_ocl_TuplePart", OclExpression81: "ir_ocl_IfExp", OclExpression75: "ir_ocl_IfExp", OclExpression57: "ir_ocl_OclOperation", OclExpression103: "ir_ocl_CollectionLiteralExp", OclExpression62: "ir_ocl_AbstractOperationCallExp"):
        self.reason = reason
        self.description = description
        
    @property
    def reason(self) -> str:
        return self.__reason

    @reason.setter
    def reason(self, reason: str):
        self.__reason = reason

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

class ir_ocl_VarExp(OclExpression):

    pass
class ir_ocl_LiteralExp(OclExpression):

    pass
class ir_ocl_LetExp(OclExpression):

    pass
class ir_ocl_IfExp(OclExpression):

    pass
class ocl_ir_EFClass:

    pass
class ocl_WithContextVariable:

    pass
class ir_ocl_OclDerivedProperty(DerivedProperty, ocl_WithContextVariable):

    pass
class ir_ocl_OclOperation(Operation, ocl_WithContextVariable):

    pass
class Constraint:

    pass
class ir_ocl_OclInvariant(Constraint, ocl_WithContextVariable):

    pass
class ocl_ir_VariableDeclaration:

    pass
class ir_ocl_WithContextVariable(ABC):

    pass
class ocl_ir_OperationFeatureRef:

    pass
class AbstractOperationCallExp:

    pass
class ir_ocl_CollectionCallExp(AbstractOperationCallExp):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class ir_ocl_OperationCallExp(AbstractOperationCallExp):

    def __init__(self, name: str, ir_ocl_OperationCallExp: "ocl_ir_OperationFeatureRef" = None):
        self.name = name
        self.ir_ocl_OperationCallExp = ir_ocl_OperationCallExp
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ir_ocl_OperationCallExp(self):
        return self.__ir_ocl_OperationCallExp

    @ir_ocl_OperationCallExp.setter
    def ir_ocl_OperationCallExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_ocl_OperationCallExp__ir_ocl_OperationCallExp", None)
        self.__ir_ocl_OperationCallExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ocl_ir_OperationFeatureRef"):
                opp_val = getattr(old_value, "ocl_ir_OperationFeatureRef", None)
                if opp_val == self:
                    setattr(old_value, "ocl_ir_OperationFeatureRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ocl_ir_OperationFeatureRef"):
                opp_val = getattr(value, "ocl_ir_OperationFeatureRef", None)
                setattr(value, "ocl_ir_OperationFeatureRef", self)

class CallExp:

    pass
class ir_ocl_OperatorCallExp(CallExp):

    def __init__(self, operator: str, ir_ocl_OperatorCallExp: "OclExpression" = None):
        self.operator = operator
        self.ir_ocl_OperatorCallExp = ir_ocl_OperatorCallExp
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def ir_ocl_OperatorCallExp(self):
        return self.__ir_ocl_OperatorCallExp

    @ir_ocl_OperatorCallExp.setter
    def ir_ocl_OperatorCallExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_ocl_OperatorCallExp__ir_ocl_OperatorCallExp", None)
        self.__ir_ocl_OperatorCallExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression91"):
                opp_val = getattr(old_value, "OclExpression91", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression91", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression91"):
                opp_val = getattr(value, "OclExpression91", None)
                setattr(value, "OclExpression91", self)

class ir_ocl_LoopExp(CallExp):

    pass
class ir_ocl_PropertyCallExp(CallExp):

    def __init__(self, name: str, ir_ocl_PropertyCallExp: "ocl_ir_PropertyFeatureRef" = None):
        self.name = name
        self.ir_ocl_PropertyCallExp = ir_ocl_PropertyCallExp
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ir_ocl_PropertyCallExp(self):
        return self.__ir_ocl_PropertyCallExp

    @ir_ocl_PropertyCallExp.setter
    def ir_ocl_PropertyCallExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_ocl_PropertyCallExp__ir_ocl_PropertyCallExp", None)
        self.__ir_ocl_PropertyCallExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ocl_ir_PropertyFeatureRef"):
                opp_val = getattr(old_value, "ocl_ir_PropertyFeatureRef", None)
                if opp_val == self:
                    setattr(old_value, "ocl_ir_PropertyFeatureRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ocl_ir_PropertyFeatureRef"):
                opp_val = getattr(value, "ocl_ir_PropertyFeatureRef", None)
                setattr(value, "ocl_ir_PropertyFeatureRef", self)

class ir_ocl_AbstractOperationCallExp(CallExp):

    pass
class ir_ocl_CallExp(OclExpression):

    pass
class ir_ocl_ModelElement(OclExpression):

    pass
class TypeRef:

    pass
class ir_MetaTypeRef(TypeRef):

    pass
class ir_TupleTypeElement:

    def __init__(self, name: str, ir_TupleTypeElement: "ir_EFTupleType" = None, ir_TupleTypeElement44: "ir_TypeRef" = None):
        self.name = name
        self.ir_TupleTypeElement = ir_TupleTypeElement
        self.ir_TupleTypeElement44 = ir_TupleTypeElement44
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ir_TupleTypeElement(self):
        return self.__ir_TupleTypeElement

    @ir_TupleTypeElement.setter
    def ir_TupleTypeElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_TupleTypeElement__ir_TupleTypeElement", None)
        self.__ir_TupleTypeElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_EFTupleType42"):
                opp_val = getattr(old_value, "ir_EFTupleType42", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_EFTupleType42"):
                opp_val = getattr(value, "ir_EFTupleType42", None)
                if opp_val is None:
                    setattr(value, "ir_EFTupleType42", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ir_TupleTypeElement44(self):
        return self.__ir_TupleTypeElement44

    @ir_TupleTypeElement44.setter
    def ir_TupleTypeElement44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_TupleTypeElement__ir_TupleTypeElement44", None)
        self.__ir_TupleTypeElement44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_TypeRef45"):
                opp_val = getattr(old_value, "ir_TypeRef45", None)
                if opp_val == self:
                    setattr(old_value, "ir_TypeRef45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_TypeRef45"):
                opp_val = getattr(value, "ir_TypeRef45", None)
                setattr(value, "ir_TypeRef45", self)

class ir_EFEnumLiteral:

    def __init__(self, name: str, ir_EFEnumLiteral: "ir_EFEnum" = None):
        self.name = name
        self.ir_EFEnumLiteral = ir_EFEnumLiteral
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ir_EFEnumLiteral(self):
        return self.__ir_EFEnumLiteral

    @ir_EFEnumLiteral.setter
    def ir_EFEnumLiteral(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_EFEnumLiteral__ir_EFEnumLiteral", None)
        self.__ir_EFEnumLiteral = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_EFEnum40"):
                opp_val = getattr(old_value, "ir_EFEnum40", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_EFEnum40"):
                opp_val = getattr(value, "ir_EFEnum40", None)
                if opp_val is None:
                    setattr(value, "ir_EFEnum40", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class CollectionTypeRef:

    pass
class ir_OrderedSetTypeRef(CollectionTypeRef):

    pass
class ir_BagTypeRef(CollectionTypeRef):

    pass
class ir_SequenceTypeRef(CollectionTypeRef):

    pass
class ir_SetTypeRef(CollectionTypeRef):

    pass
class ir_CollectionTypeRef(TypeRef):

    pass
class ir_InvalidTypeRef(TypeRef):

    pass
class ir_EPackage:

    pass
class ir_EFPackage:

    pass
class VariableDeclaration:

    pass
class ir_ocl_Iterator(VariableDeclaration):

    pass
class ir_VariableDeclaration:

    def __init__(self, name: str, ir_VariableDeclaration: "ir_TypeRef" = None):
        self.name = name
        self.ir_VariableDeclaration = ir_VariableDeclaration
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ir_VariableDeclaration(self):
        return self.__ir_VariableDeclaration

    @ir_VariableDeclaration.setter
    def ir_VariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_VariableDeclaration__ir_VariableDeclaration", None)
        self.__ir_VariableDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_TypeRef25"):
                opp_val = getattr(old_value, "ir_TypeRef25", None)
                if opp_val == self:
                    setattr(old_value, "ir_TypeRef25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_TypeRef25"):
                opp_val = getattr(value, "ir_TypeRef25", None)
                setattr(value, "ir_TypeRef25", self)

class ir_EStructuralFeature:

    pass
class ir_EEnum:

    pass
class ir_EClass:

    pass
class EFType:

    pass
class ir_EFEnum(EFType):

    pass
class ir_Parameter(VariableDeclaration):

    pass
class AbstractFunction:

    pass
class ir_EFType(ABC):

    pass
class TypedElement:

    pass
class ir_AbstractFunction(TypedElement):

    def __init__(self, name: str, ir_AbstractFunction: "ir_EFType" = None):
        self.name = name
        self.ir_AbstractFunction = ir_AbstractFunction
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ir_AbstractFunction(self):
        return self.__ir_AbstractFunction

    @ir_AbstractFunction.setter
    def ir_AbstractFunction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_AbstractFunction__ir_AbstractFunction", None)
        self.__ir_AbstractFunction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_EFType"):
                opp_val = getattr(old_value, "ir_EFType", None)
                if opp_val == self:
                    setattr(old_value, "ir_EFType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_EFType"):
                opp_val = getattr(value, "ir_EFType", None)
                setattr(value, "ir_EFType", self)

class ir_TypeRef(ABC):

    pass
class ir_TypedElement(ABC):

    pass
class ir_EFTupleType(EFType):

    def __init__(self, id: str, ir_EFTupleType20: "ir_TupleFieldRef" = None, ir_EFTupleType: "ir_Specification" = None, ir_EFTupleType42: set["ir_TupleTypeElement"] = None):
        self.id = id
        self.ir_EFTupleType20 = ir_EFTupleType20
        self.ir_EFTupleType = ir_EFTupleType
        self.ir_EFTupleType42 = ir_EFTupleType42 if ir_EFTupleType42 is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def ir_EFTupleType42(self):
        return self.__ir_EFTupleType42

    @ir_EFTupleType42.setter
    def ir_EFTupleType42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_EFTupleType__ir_EFTupleType42", None)
        self.__ir_EFTupleType42 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ir_TupleTypeElement"):
                    opp_val = getattr(item, "ir_TupleTypeElement", None)
                    
                    if opp_val == self:
                        setattr(item, "ir_TupleTypeElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ir_TupleTypeElement"):
                    opp_val = getattr(item, "ir_TupleTypeElement", None)
                    
                    setattr(item, "ir_TupleTypeElement", self)
                    

    @property
    def ir_EFTupleType20(self):
        return self.__ir_EFTupleType20

    @ir_EFTupleType20.setter
    def ir_EFTupleType20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_EFTupleType__ir_EFTupleType20", None)
        self.__ir_EFTupleType20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_TupleFieldRef"):
                opp_val = getattr(old_value, "ir_TupleFieldRef", None)
                if opp_val == self:
                    setattr(old_value, "ir_TupleFieldRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_TupleFieldRef"):
                opp_val = getattr(value, "ir_TupleFieldRef", None)
                setattr(value, "ir_TupleFieldRef", self)

    @property
    def ir_EFTupleType(self):
        return self.__ir_EFTupleType

    @ir_EFTupleType.setter
    def ir_EFTupleType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_EFTupleType__ir_EFTupleType", None)
        self.__ir_EFTupleType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_Specification12"):
                opp_val = getattr(old_value, "ir_Specification12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_Specification12"):
                opp_val = getattr(value, "ir_Specification12", None)
                if opp_val is None:
                    setattr(value, "ir_Specification12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ir_EFPrimitiveType(EFType):

    def __init__(self, name: str, ir_EFPrimitiveType: "ir_Specification" = None):
        self.name = name
        self.ir_EFPrimitiveType = ir_EFPrimitiveType
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ir_EFPrimitiveType(self):
        return self.__ir_EFPrimitiveType

    @ir_EFPrimitiveType.setter
    def ir_EFPrimitiveType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_EFPrimitiveType__ir_EFPrimitiveType", None)
        self.__ir_EFPrimitiveType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_Specification10"):
                opp_val = getattr(old_value, "ir_Specification10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_Specification10"):
                opp_val = getattr(value, "ir_Specification10", None)
                if opp_val is None:
                    setattr(value, "ir_Specification10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class PropertyFeatureRef:

    pass
class ir_MetamodelFeatureRef(PropertyFeatureRef):

    pass
class ir_BuiltinPropertyRef(PropertyFeatureRef):

    pass
class ir_DerivedPropertyRef(PropertyFeatureRef):

    pass
class ir_TupleFieldRef(PropertyFeatureRef):

    def __init__(self, name: str, ir_TupleFieldRef: "ir_EFTupleType" = None):
        self.name = name
        self.ir_TupleFieldRef = ir_TupleFieldRef
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ir_TupleFieldRef(self):
        return self.__ir_TupleFieldRef

    @ir_TupleFieldRef.setter
    def ir_TupleFieldRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_TupleFieldRef__ir_TupleFieldRef", None)
        self.__ir_TupleFieldRef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_EFTupleType20"):
                opp_val = getattr(old_value, "ir_EFTupleType20", None)
                if opp_val == self:
                    setattr(old_value, "ir_EFTupleType20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_EFTupleType20"):
                opp_val = getattr(value, "ir_EFTupleType20", None)
                setattr(value, "ir_EFTupleType20", self)

class OperationFeatureRef:

    pass
class ir_DefinedOperationRef(OperationFeatureRef):

    pass
class ir_BuiltinOperationRef(OperationFeatureRef):

    pass
class FeatureRef:

    pass
class ir_PropertyFeatureRef(FeatureRef):

    pass
class ir_OperationFeatureRef(FeatureRef):

    pass
class ir_FeatureRef(ABC):

    pass
class ir_Specification:

    pass
class ir_Operation(AbstractFunction):

    pass
class ir_DerivedProperty(AbstractFunction):

    pass
class ir_EFClass(EFType):

    pass
class ir_Constraint(ABC):

    def __init__(self, name: str, ir_Constraint: "ir_Specification" = None):
        self.name = name
        self.ir_Constraint = ir_Constraint
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ir_Constraint(self):
        return self.__ir_Constraint

    @ir_Constraint.setter
    def ir_Constraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_Constraint__ir_Constraint", None)
        self.__ir_Constraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_Specification2"):
                opp_val = getattr(old_value, "ir_Specification2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_Specification2"):
                opp_val = getattr(value, "ir_Specification2", None)
                if opp_val is None:
                    setattr(value, "ir_Specification2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ir_EFMetamodel:

    pass