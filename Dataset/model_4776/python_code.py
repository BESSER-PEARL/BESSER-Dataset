from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class OperatorKind(Enum):
    Add = "Add"
    Subtract = "Subtract"
    Multiply = "Multiply"
    Divide = "Divide"
    ElementWiseMultiply = "ElementWiseMultiply"
    ElementWiseDivide = "ElementWiseDivide"
    ElementWisePower = "ElementWisePower"
    Negate = "Negate"
    Power = "Power"
    Root = "Root"
    Transpose = "Transpose"
    LogicalAnd = "LogicalAnd"
    LogicalOr = "LogicalOr"
    LogicalNot = "LogicalNot"
    Implies = "Implies"
    LessThan = "LessThan"
    LessThanOrEqualTo = "LessThanOrEqualTo"
    GreaterThan = "GreaterThan"
    GreaterThanOrEqualTo = "GreaterThanOrEqualTo"
    EqualTo = "EqualTo"
    NotEqualTo = "NotEqualTo"


############################################
# Definition of Classes
############################################

class typesystem_Expression:

    pass
class ArrayType:

    pass
class NumericLiteral:

    pass
class typesystem_IntegerLiteral(NumericLiteral):

    def __init__(self, data: str, value: str):
        self.data = data
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def data(self) -> str:
        return self.__data

    @data.setter
    def data(self, data: str):
        self.__data = data

class typesystem_TensorType(ArrayType):

    def __init__(self, vector: bool, matrix: bool):
        self.vector = vector
        self.matrix = matrix
        
    @property
    def vector(self) -> bool:
        return self.__vector

    @vector.setter
    def vector(self, vector: bool):
        self.__vector = vector

    @property
    def matrix(self) -> bool:
        return self.__matrix

    @matrix.setter
    def matrix(self, matrix: bool):
        self.__matrix = matrix

class typesystem_RealLiteral(NumericLiteral):

    def __init__(self, data: str, value: float):
        self.data = data
        self.value = value
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def data(self) -> str:
        return self.__data

    @data.setter
    def data(self, data: str):
        self.__data = data

class Literal:

    pass
class typesystem_BooleanLiteral(Literal):

    def __init__(self, true: bool):
        self.true = true
        
    @property
    def true(self) -> bool:
        return self.__true

    @true.setter
    def true(self, true: bool):
        self.__true = true

class typesystem_StringLiteral(Literal):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class typesystem_NumericLiteral(Literal):

    def __init__(self, typesystem_NumericLiteral: "typesystem_Unit" = None):
        self.typesystem_NumericLiteral = typesystem_NumericLiteral
        
    @property
    def typesystem_NumericLiteral(self):
        return self.__typesystem_NumericLiteral

    @typesystem_NumericLiteral.setter
    def typesystem_NumericLiteral(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_typesystem_NumericLiteral__typesystem_NumericLiteral", None)
        self.__typesystem_NumericLiteral = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "typesystem_Unit15"):
                opp_val = getattr(old_value, "typesystem_Unit15", None)
                if opp_val == self:
                    setattr(old_value, "typesystem_Unit15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "typesystem_Unit15"):
                opp_val = getattr(value, "typesystem_Unit15", None)
                setattr(value, "typesystem_Unit15", self)

    def isComplex(self) -> bool:
        # TODO: Implement isComplex method
        pass

class Expression:

    pass
class typesystem_Literal(Expression):

    pass
class UnitProduct:

    pass
class typesystem_UnitNumerator(UnitProduct):

    pass
class typesystem_UnitDenominator(UnitProduct):

    pass
class typesystem_UnitFactor:

    def __init__(self, symbol: str, exponent: int, typesystem_UnitFactor: "typesystem_UnitProduct" = None):
        self.symbol = symbol
        self.exponent = exponent
        self.typesystem_UnitFactor = typesystem_UnitFactor
        
    @property
    def exponent(self) -> int:
        return self.__exponent

    @exponent.setter
    def exponent(self, exponent: int):
        self.__exponent = exponent

    @property
    def symbol(self) -> str:
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol: str):
        self.__symbol = symbol

    @property
    def typesystem_UnitFactor(self):
        return self.__typesystem_UnitFactor

    @typesystem_UnitFactor.setter
    def typesystem_UnitFactor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_typesystem_UnitFactor__typesystem_UnitFactor", None)
        self.__typesystem_UnitFactor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "typesystem_UnitProduct"):
                opp_val = getattr(old_value, "typesystem_UnitProduct", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "typesystem_UnitProduct"):
                opp_val = getattr(value, "typesystem_UnitProduct", None)
                if opp_val is None:
                    setattr(value, "typesystem_UnitProduct", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class typesystem_UnitProduct(ABC):

    def __init__(self, typesystem_UnitProduct: set["typesystem_UnitFactor"] = None):
        self.typesystem_UnitProduct = typesystem_UnitProduct if typesystem_UnitProduct is not None else set()
        
    @property
    def typesystem_UnitProduct(self):
        return self.__typesystem_UnitProduct

    @typesystem_UnitProduct.setter
    def typesystem_UnitProduct(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_typesystem_UnitProduct__typesystem_UnitProduct", None)
        self.__typesystem_UnitProduct = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "typesystem_UnitFactor"):
                    opp_val = getattr(item, "typesystem_UnitFactor", None)
                    
                    if opp_val == self:
                        setattr(item, "typesystem_UnitFactor", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "typesystem_UnitFactor"):
                    opp_val = getattr(item, "typesystem_UnitFactor", None)
                    
                    setattr(item, "typesystem_UnitFactor", self)
                    

    def getFactor(self, symbol: str) -> str:
        # TODO: Implement getFactor method
        pass

class typesystem_Unit:

    def __init__(self, scale: int, wildcard: bool, typesystem_Unit: "typesystem_NumericType" = None, typesystem_Unit15: "typesystem_NumericLiteral" = None, typesystem_Unit10: "typesystem_UnitNumerator" = None, typesystem_Unit12: "typesystem_UnitDenominator" = None):
        self.scale = scale
        self.wildcard = wildcard
        self.typesystem_Unit = typesystem_Unit
        self.typesystem_Unit15 = typesystem_Unit15
        self.typesystem_Unit10 = typesystem_Unit10
        self.typesystem_Unit12 = typesystem_Unit12
        
    @property
    def scale(self) -> int:
        return self.__scale

    @scale.setter
    def scale(self, scale: int):
        self.__scale = scale

    @property
    def wildcard(self) -> bool:
        return self.__wildcard

    @wildcard.setter
    def wildcard(self, wildcard: bool):
        self.__wildcard = wildcard

    @property
    def typesystem_Unit15(self):
        return self.__typesystem_Unit15

    @typesystem_Unit15.setter
    def typesystem_Unit15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_typesystem_Unit__typesystem_Unit15", None)
        self.__typesystem_Unit15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "typesystem_NumericLiteral"):
                opp_val = getattr(old_value, "typesystem_NumericLiteral", None)
                if opp_val == self:
                    setattr(old_value, "typesystem_NumericLiteral", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "typesystem_NumericLiteral"):
                opp_val = getattr(value, "typesystem_NumericLiteral", None)
                setattr(value, "typesystem_NumericLiteral", self)

    @property
    def typesystem_Unit10(self):
        return self.__typesystem_Unit10

    @typesystem_Unit10.setter
    def typesystem_Unit10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_typesystem_Unit__typesystem_Unit10", None)
        self.__typesystem_Unit10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "typesystem_UnitNumerator"):
                opp_val = getattr(old_value, "typesystem_UnitNumerator", None)
                if opp_val == self:
                    setattr(old_value, "typesystem_UnitNumerator", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "typesystem_UnitNumerator"):
                opp_val = getattr(value, "typesystem_UnitNumerator", None)
                setattr(value, "typesystem_UnitNumerator", self)

    @property
    def typesystem_Unit12(self):
        return self.__typesystem_Unit12

    @typesystem_Unit12.setter
    def typesystem_Unit12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_typesystem_Unit__typesystem_Unit12", None)
        self.__typesystem_Unit12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "typesystem_UnitDenominator"):
                opp_val = getattr(old_value, "typesystem_UnitDenominator", None)
                if opp_val == self:
                    setattr(old_value, "typesystem_UnitDenominator", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "typesystem_UnitDenominator"):
                opp_val = getattr(value, "typesystem_UnitDenominator", None)
                setattr(value, "typesystem_UnitDenominator", self)

    @property
    def typesystem_Unit(self):
        return self.__typesystem_Unit

    @typesystem_Unit.setter
    def typesystem_Unit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_typesystem_Unit__typesystem_Unit", None)
        self.__typesystem_Unit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "typesystem_NumericType"):
                opp_val = getattr(old_value, "typesystem_NumericType", None)
                if opp_val == self:
                    setattr(old_value, "typesystem_NumericType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "typesystem_NumericType"):
                opp_val = getattr(value, "typesystem_NumericType", None)
                setattr(value, "typesystem_NumericType", self)

    def isEquivalentTo(self, other: str, ignoreScale: bool) -> bool:
        # TODO: Implement isEquivalentTo method
        pass

    def evaluate(self, other: str, operator: str) -> str:
        # TODO: Implement evaluate method
        pass

    def getNormalized(self) -> str:
        # TODO: Implement getNormalized method
        pass

    def evaluate(self, n: int, operator: str) -> str:
        # TODO: Implement evaluate method
        pass

class PrimitiveType:

    pass
class typesystem_NumericType(PrimitiveType):

    pass
class DataType:

    pass
class typesystem_PrimitiveType(DataType):

    pass
class typesystem_UnitType(DataType):

    pass
class typesystem_AnyDataType(DataType):

    pass
class typesystem_InvalidDataType(DataType):

    pass
class typesystem_ArrayDimension:

    pass
class typesystem_ArrayType(DataType):

    def __init__(self, dimensionality: int, dimensional: bool, multidimensional: bool, typesystem_ArrayType: "typesystem_DataType" = None, typesystem_ArrayType3: "typesystem_DataType" = None, typesystem_ArrayType6: set["typesystem_ArrayDimension"] = None):
        self.dimensionality = dimensionality
        self.dimensional = dimensional
        self.multidimensional = multidimensional
        self.typesystem_ArrayType = typesystem_ArrayType
        self.typesystem_ArrayType3 = typesystem_ArrayType3
        self.typesystem_ArrayType6 = typesystem_ArrayType6 if typesystem_ArrayType6 is not None else set()
        
    @property
    def multidimensional(self) -> bool:
        return self.__multidimensional

    @multidimensional.setter
    def multidimensional(self, multidimensional: bool):
        self.__multidimensional = multidimensional

    @property
    def dimensionality(self) -> int:
        return self.__dimensionality

    @dimensionality.setter
    def dimensionality(self, dimensionality: int):
        self.__dimensionality = dimensionality

    @property
    def dimensional(self) -> bool:
        return self.__dimensional

    @dimensional.setter
    def dimensional(self, dimensional: bool):
        self.__dimensional = dimensional

    @property
    def typesystem_ArrayType3(self):
        return self.__typesystem_ArrayType3

    @typesystem_ArrayType3.setter
    def typesystem_ArrayType3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_typesystem_ArrayType__typesystem_ArrayType3", None)
        self.__typesystem_ArrayType3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "typesystem_DataType4"):
                opp_val = getattr(old_value, "typesystem_DataType4", None)
                if opp_val == self:
                    setattr(old_value, "typesystem_DataType4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "typesystem_DataType4"):
                opp_val = getattr(value, "typesystem_DataType4", None)
                setattr(value, "typesystem_DataType4", self)

    @property
    def typesystem_ArrayType6(self):
        return self.__typesystem_ArrayType6

    @typesystem_ArrayType6.setter
    def typesystem_ArrayType6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_typesystem_ArrayType__typesystem_ArrayType6", None)
        self.__typesystem_ArrayType6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "typesystem_ArrayDimension"):
                    opp_val = getattr(item, "typesystem_ArrayDimension", None)
                    
                    if opp_val == self:
                        setattr(item, "typesystem_ArrayDimension", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "typesystem_ArrayDimension"):
                    opp_val = getattr(item, "typesystem_ArrayDimension", None)
                    
                    setattr(item, "typesystem_ArrayDimension", self)
                    

    @property
    def typesystem_ArrayType(self):
        return self.__typesystem_ArrayType

    @typesystem_ArrayType.setter
    def typesystem_ArrayType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_typesystem_ArrayType__typesystem_ArrayType", None)
        self.__typesystem_ArrayType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "typesystem_DataType"):
                opp_val = getattr(old_value, "typesystem_DataType", None)
                if opp_val == self:
                    setattr(old_value, "typesystem_DataType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "typesystem_DataType"):
                opp_val = getattr(value, "typesystem_DataType", None)
                setattr(value, "typesystem_DataType", self)

class typesystem_StringType(PrimitiveType):

    pass
class typesystem_BooleanType(PrimitiveType):

    pass
class typesystem_DataType(ABC):

    def __init__(self, typesystem_DataType: "typesystem_ArrayType" = None, typesystem_DataType4: "typesystem_ArrayType" = None):
        self.typesystem_DataType = typesystem_DataType
        self.typesystem_DataType4 = typesystem_DataType4
        
    @property
    def typesystem_DataType(self):
        return self.__typesystem_DataType

    @typesystem_DataType.setter
    def typesystem_DataType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_typesystem_DataType__typesystem_DataType", None)
        self.__typesystem_DataType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "typesystem_ArrayType"):
                opp_val = getattr(old_value, "typesystem_ArrayType", None)
                if opp_val == self:
                    setattr(old_value, "typesystem_ArrayType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "typesystem_ArrayType"):
                opp_val = getattr(value, "typesystem_ArrayType", None)
                setattr(value, "typesystem_ArrayType", self)

    @property
    def typesystem_DataType4(self):
        return self.__typesystem_DataType4

    @typesystem_DataType4.setter
    def typesystem_DataType4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_typesystem_DataType__typesystem_DataType4", None)
        self.__typesystem_DataType4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "typesystem_ArrayType3"):
                opp_val = getattr(old_value, "typesystem_ArrayType3", None)
                if opp_val == self:
                    setattr(old_value, "typesystem_ArrayType3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "typesystem_ArrayType3"):
                opp_val = getattr(value, "typesystem_ArrayType3", None)
                setattr(value, "typesystem_ArrayType3", self)

    def evaluate(self, other: str, operator: str) -> str:
        # TODO: Implement evaluate method
        pass

    def evaluate(self, n: int, operator: str) -> str:
        # TODO: Implement evaluate method
        pass

    def isAssignableFrom(self, other: str) -> bool:
        # TODO: Implement isAssignableFrom method
        pass

    def isEquivalentTo(self, other: str) -> bool:
        # TODO: Implement isEquivalentTo method
        pass

class NumericType:

    pass
class typesystem_ComplexType(NumericType):

    pass
class typesystem_GaussianType(NumericType):

    pass
class typesystem_IntegerType(NumericType):

    pass
class typesystem_RealType(NumericType):

    pass