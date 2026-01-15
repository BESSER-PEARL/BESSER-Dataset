from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Expression:

    pass
class fIDL_StringLiteral(Expression):

    pass
class fIDL_NumberLiteral(Expression):

    pass
class fIDL_BooleanLiteral(Expression):

    def __init__(self, isTrue: bool):
        self.isTrue = isTrue
        
    @property
    def isTrue(self) -> bool:
        return self.__isTrue

    @isTrue.setter
    def isTrue(self, isTrue: bool):
        self.__isTrue = isTrue

class IntegerType:

    pass
class fIDL_Uint16Type(IntegerType):

    pass
class fIDL_Uint8Type(IntegerType):

    pass
class fIDL_Int64Type(IntegerType):

    pass
class fIDL_Uint32Type(IntegerType):

    pass
class fIDL_Int16Type(IntegerType):

    pass
class fIDL_Uint64Type(IntegerType):

    pass
class fIDL_Int32Type(IntegerType):

    pass
class fIDL_Int8Type(IntegerType):

    pass
class Literal:

    pass
class EnumMemberValue:

    pass
class Constant:

    pass
class fIDL_Literal(Constant):

    pass
class PrimitiveType:

    pass
class fIDL_Float32Type(PrimitiveType):

    pass
class fIDL_StatusType(PrimitiveType):

    pass
class fIDL_BooleanType(PrimitiveType):

    pass
class fIDL_Float64Type(PrimitiveType):

    pass
class Type:

    pass
class fIDL_HandleType(Type):

    def __init__(self, type: str, nullable: bool):
        self.type = type
        self.nullable = nullable
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def nullable(self) -> bool:
        return self.__nullable

    @nullable.setter
    def nullable(self, nullable: bool):
        self.__nullable = nullable

class fIDL_PrimitiveType(Type):

    pass
class fIDL_ArrayType(Type):

    pass
class fIDL_RequestType(Type):

    def __init__(self, nullable: bool, fIDL_RequestType: "fIDL_Declaration" = None):
        self.nullable = nullable
        self.fIDL_RequestType = fIDL_RequestType
        
    @property
    def nullable(self) -> bool:
        return self.__nullable

    @nullable.setter
    def nullable(self, nullable: bool):
        self.__nullable = nullable

    @property
    def fIDL_RequestType(self):
        return self.__fIDL_RequestType

    @fIDL_RequestType.setter
    def fIDL_RequestType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fIDL_RequestType__fIDL_RequestType", None)
        self.__fIDL_RequestType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fIDL_Declaration65"):
                opp_val = getattr(old_value, "fIDL_Declaration65", None)
                if opp_val == self:
                    setattr(old_value, "fIDL_Declaration65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fIDL_Declaration65"):
                opp_val = getattr(value, "fIDL_Declaration65", None)
                setattr(value, "fIDL_Declaration65", self)

class fIDL_StringType(Type):

    def __init__(self, nullable: bool, fIDL_StringType: "fIDL_Constant" = None):
        self.nullable = nullable
        self.fIDL_StringType = fIDL_StringType
        
    @property
    def nullable(self) -> bool:
        return self.__nullable

    @nullable.setter
    def nullable(self, nullable: bool):
        self.__nullable = nullable

    @property
    def fIDL_StringType(self):
        return self.__fIDL_StringType

    @fIDL_StringType.setter
    def fIDL_StringType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fIDL_StringType__fIDL_StringType", None)
        self.__fIDL_StringType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fIDL_Constant63"):
                opp_val = getattr(old_value, "fIDL_Constant63", None)
                if opp_val == self:
                    setattr(old_value, "fIDL_Constant63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fIDL_Constant63"):
                opp_val = getattr(value, "fIDL_Constant63", None)
                setattr(value, "fIDL_Constant63", self)

class fIDL_VectorType(Type):

    def __init__(self, nullable: bool, fIDL_VectorType60: "fIDL_Constant" = None, fIDL_VectorType: "fIDL_Type" = None):
        self.nullable = nullable
        self.fIDL_VectorType60 = fIDL_VectorType60
        self.fIDL_VectorType = fIDL_VectorType
        
    @property
    def nullable(self) -> bool:
        return self.__nullable

    @nullable.setter
    def nullable(self, nullable: bool):
        self.__nullable = nullable

    @property
    def fIDL_VectorType(self):
        return self.__fIDL_VectorType

    @fIDL_VectorType.setter
    def fIDL_VectorType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fIDL_VectorType__fIDL_VectorType", None)
        self.__fIDL_VectorType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fIDL_Type58"):
                opp_val = getattr(old_value, "fIDL_Type58", None)
                if opp_val == self:
                    setattr(old_value, "fIDL_Type58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fIDL_Type58"):
                opp_val = getattr(value, "fIDL_Type58", None)
                setattr(value, "fIDL_Type58", self)

    @property
    def fIDL_VectorType60(self):
        return self.__fIDL_VectorType60

    @fIDL_VectorType60.setter
    def fIDL_VectorType60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fIDL_VectorType__fIDL_VectorType60", None)
        self.__fIDL_VectorType60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fIDL_Constant61"):
                opp_val = getattr(old_value, "fIDL_Constant61", None)
                if opp_val == self:
                    setattr(old_value, "fIDL_Constant61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fIDL_Constant61"):
                opp_val = getattr(value, "fIDL_Constant61", None)
                setattr(value, "fIDL_Constant61", self)

class fIDL_IdentifierType(Type):

    def __init__(self, nullable: bool, fIDL_IdentifierType: "fIDL_Declaration" = None):
        self.nullable = nullable
        self.fIDL_IdentifierType = fIDL_IdentifierType
        
    @property
    def nullable(self) -> bool:
        return self.__nullable

    @nullable.setter
    def nullable(self, nullable: bool):
        self.__nullable = nullable

    @property
    def fIDL_IdentifierType(self):
        return self.__fIDL_IdentifierType

    @fIDL_IdentifierType.setter
    def fIDL_IdentifierType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fIDL_IdentifierType__fIDL_IdentifierType", None)
        self.__fIDL_IdentifierType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fIDL_Declaration51"):
                opp_val = getattr(old_value, "fIDL_Declaration51", None)
                if opp_val == self:
                    setattr(old_value, "fIDL_Declaration51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fIDL_Declaration51"):
                opp_val = getattr(value, "fIDL_Declaration51", None)
                setattr(value, "fIDL_Declaration51", self)

class fIDL_StructField:

    def __init__(self, name: str, fIDL_StructField: "fIDL_StructMember" = None, fIDL_StructField39: "fIDL_Type" = None, fIDL_StructField42: "fIDL_Constant" = None):
        self.name = name
        self.fIDL_StructField = fIDL_StructField
        self.fIDL_StructField39 = fIDL_StructField39
        self.fIDL_StructField42 = fIDL_StructField42
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fIDL_StructField(self):
        return self.__fIDL_StructField

    @fIDL_StructField.setter
    def fIDL_StructField(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fIDL_StructField__fIDL_StructField", None)
        self.__fIDL_StructField = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fIDL_StructMember34"):
                opp_val = getattr(old_value, "fIDL_StructMember34", None)
                if opp_val == self:
                    setattr(old_value, "fIDL_StructMember34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fIDL_StructMember34"):
                opp_val = getattr(value, "fIDL_StructMember34", None)
                setattr(value, "fIDL_StructMember34", self)

    @property
    def fIDL_StructField39(self):
        return self.__fIDL_StructField39

    @fIDL_StructField39.setter
    def fIDL_StructField39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fIDL_StructField__fIDL_StructField39", None)
        self.__fIDL_StructField39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fIDL_Type40"):
                opp_val = getattr(old_value, "fIDL_Type40", None)
                if opp_val == self:
                    setattr(old_value, "fIDL_Type40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fIDL_Type40"):
                opp_val = getattr(value, "fIDL_Type40", None)
                setattr(value, "fIDL_Type40", self)

    @property
    def fIDL_StructField42(self):
        return self.__fIDL_StructField42

    @fIDL_StructField42.setter
    def fIDL_StructField42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fIDL_StructField__fIDL_StructField42", None)
        self.__fIDL_StructField42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fIDL_Constant43"):
                opp_val = getattr(old_value, "fIDL_Constant43", None)
                if opp_val == self:
                    setattr(old_value, "fIDL_Constant43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fIDL_Constant43"):
                opp_val = getattr(value, "fIDL_Constant43", None)
                setattr(value, "fIDL_Constant43", self)

class UnionMember:

    pass
class fIDL_UnionField(UnionMember):

    def __init__(self, name: str, fIDL_UnionField: "fIDL_Type" = None):
        self.name = name
        self.fIDL_UnionField = fIDL_UnionField
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fIDL_UnionField(self):
        return self.__fIDL_UnionField

    @fIDL_UnionField.setter
    def fIDL_UnionField(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fIDL_UnionField__fIDL_UnionField", None)
        self.__fIDL_UnionField = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fIDL_Type49"):
                opp_val = getattr(old_value, "fIDL_Type49", None)
                if opp_val == self:
                    setattr(old_value, "fIDL_Type49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fIDL_Type49"):
                opp_val = getattr(value, "fIDL_Type49", None)
                setattr(value, "fIDL_Type49", self)

class fIDL_UnionMember:

    pass
class fIDL_Parameter:

    def __init__(self, name: str, fIDL_Parameter30: "fIDL_Type" = None, fIDL_Parameter: "fIDL_ParameterList" = None):
        self.name = name
        self.fIDL_Parameter30 = fIDL_Parameter30
        self.fIDL_Parameter = fIDL_Parameter
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fIDL_Parameter30(self):
        return self.__fIDL_Parameter30

    @fIDL_Parameter30.setter
    def fIDL_Parameter30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fIDL_Parameter__fIDL_Parameter30", None)
        self.__fIDL_Parameter30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fIDL_Type31"):
                opp_val = getattr(old_value, "fIDL_Type31", None)
                if opp_val == self:
                    setattr(old_value, "fIDL_Type31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fIDL_Type31"):
                opp_val = getattr(value, "fIDL_Type31", None)
                setattr(value, "fIDL_Type31", self)

    @property
    def fIDL_Parameter(self):
        return self.__fIDL_Parameter

    @fIDL_Parameter.setter
    def fIDL_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fIDL_Parameter__fIDL_Parameter", None)
        self.__fIDL_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fIDL_ParameterList28"):
                opp_val = getattr(old_value, "fIDL_ParameterList28", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fIDL_ParameterList28"):
                opp_val = getattr(value, "fIDL_ParameterList28", None)
                if opp_val is None:
                    setattr(value, "fIDL_ParameterList28", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class fIDL_ParameterList:

    pass
class fIDL_InterfaceParameters:

    def __init__(self, name: str, resultName: str, fIDL_InterfaceParameters: "fIDL_InterfaceMethod" = None, fIDL_InterfaceParameters23: "fIDL_ParameterList" = None, fIDL_InterfaceParameters25: "fIDL_ParameterList" = None):
        self.name = name
        self.resultName = resultName
        self.fIDL_InterfaceParameters = fIDL_InterfaceParameters
        self.fIDL_InterfaceParameters23 = fIDL_InterfaceParameters23
        self.fIDL_InterfaceParameters25 = fIDL_InterfaceParameters25
        
    @property
    def resultName(self) -> str:
        return self.__resultName

    @resultName.setter
    def resultName(self, resultName: str):
        self.__resultName = resultName

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fIDL_InterfaceParameters23(self):
        return self.__fIDL_InterfaceParameters23

    @fIDL_InterfaceParameters23.setter
    def fIDL_InterfaceParameters23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fIDL_InterfaceParameters__fIDL_InterfaceParameters23", None)
        self.__fIDL_InterfaceParameters23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fIDL_ParameterList"):
                opp_val = getattr(old_value, "fIDL_ParameterList", None)
                if opp_val == self:
                    setattr(old_value, "fIDL_ParameterList", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fIDL_ParameterList"):
                opp_val = getattr(value, "fIDL_ParameterList", None)
                setattr(value, "fIDL_ParameterList", self)

    @property
    def fIDL_InterfaceParameters25(self):
        return self.__fIDL_InterfaceParameters25

    @fIDL_InterfaceParameters25.setter
    def fIDL_InterfaceParameters25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fIDL_InterfaceParameters__fIDL_InterfaceParameters25", None)
        self.__fIDL_InterfaceParameters25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fIDL_ParameterList26"):
                opp_val = getattr(old_value, "fIDL_ParameterList26", None)
                if opp_val == self:
                    setattr(old_value, "fIDL_ParameterList26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fIDL_ParameterList26"):
                opp_val = getattr(value, "fIDL_ParameterList26", None)
                setattr(value, "fIDL_ParameterList26", self)

    @property
    def fIDL_InterfaceParameters(self):
        return self.__fIDL_InterfaceParameters

    @fIDL_InterfaceParameters.setter
    def fIDL_InterfaceParameters(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fIDL_InterfaceParameters__fIDL_InterfaceParameters", None)
        self.__fIDL_InterfaceParameters = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fIDL_InterfaceMethod21"):
                opp_val = getattr(old_value, "fIDL_InterfaceMethod21", None)
                if opp_val == self:
                    setattr(old_value, "fIDL_InterfaceMethod21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fIDL_InterfaceMethod21"):
                opp_val = getattr(value, "fIDL_InterfaceMethod21", None)
                setattr(value, "fIDL_InterfaceMethod21", self)

class fIDL_Expression(EnumMemberValue, Literal):

    pass
class fIDL_StructMember:

    pass
class fIDL_EnumMemberValue:

    def __init__(self, value: str, fIDL_EnumMemberValue: "fIDL_EnumMember" = None):
        self.value = value
        self.fIDL_EnumMemberValue = fIDL_EnumMemberValue
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def fIDL_EnumMemberValue(self):
        return self.__fIDL_EnumMemberValue

    @fIDL_EnumMemberValue.setter
    def fIDL_EnumMemberValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fIDL_EnumMemberValue__fIDL_EnumMemberValue", None)
        self.__fIDL_EnumMemberValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fIDL_EnumMember14"):
                opp_val = getattr(old_value, "fIDL_EnumMember14", None)
                if opp_val == self:
                    setattr(old_value, "fIDL_EnumMember14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fIDL_EnumMember14"):
                opp_val = getattr(value, "fIDL_EnumMember14", None)
                setattr(value, "fIDL_EnumMember14", self)

class fIDL_EnumMember:

    def __init__(self, name: str, fIDL_EnumMember: "fIDL_EnumDeclaration" = None, fIDL_EnumMember14: "fIDL_EnumMemberValue" = None):
        self.name = name
        self.fIDL_EnumMember = fIDL_EnumMember
        self.fIDL_EnumMember14 = fIDL_EnumMember14
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fIDL_EnumMember(self):
        return self.__fIDL_EnumMember

    @fIDL_EnumMember.setter
    def fIDL_EnumMember(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fIDL_EnumMember__fIDL_EnumMember", None)
        self.__fIDL_EnumMember = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fIDL_EnumDeclaration12"):
                opp_val = getattr(old_value, "fIDL_EnumDeclaration12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fIDL_EnumDeclaration12"):
                opp_val = getattr(value, "fIDL_EnumDeclaration12", None)
                if opp_val is None:
                    setattr(value, "fIDL_EnumDeclaration12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fIDL_EnumMember14(self):
        return self.__fIDL_EnumMember14

    @fIDL_EnumMember14.setter
    def fIDL_EnumMember14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fIDL_EnumMember__fIDL_EnumMember14", None)
        self.__fIDL_EnumMember14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fIDL_EnumMemberValue"):
                opp_val = getattr(old_value, "fIDL_EnumMemberValue", None)
                if opp_val == self:
                    setattr(old_value, "fIDL_EnumMemberValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fIDL_EnumMemberValue"):
                opp_val = getattr(value, "fIDL_EnumMemberValue", None)
                setattr(value, "fIDL_EnumMemberValue", self)

class fIDL_IntegerType(PrimitiveType):

    pass
class fIDL_Constant:

    def __init__(self, ci: str, fIDL_Constant: "fIDL_ConstDeclaration" = None, fIDL_Constant43: "fIDL_StructField" = None, fIDL_Constant56: "fIDL_ArrayType" = None, fIDL_Constant61: "fIDL_VectorType" = None, fIDL_Constant63: "fIDL_StringType" = None):
        self.ci = ci
        self.fIDL_Constant = fIDL_Constant
        self.fIDL_Constant43 = fIDL_Constant43
        self.fIDL_Constant56 = fIDL_Constant56
        self.fIDL_Constant61 = fIDL_Constant61
        self.fIDL_Constant63 = fIDL_Constant63
        
    @property
    def ci(self) -> str:
        return self.__ci

    @ci.setter
    def ci(self, ci: str):
        self.__ci = ci

    @property
    def fIDL_Constant61(self):
        return self.__fIDL_Constant61

    @fIDL_Constant61.setter
    def fIDL_Constant61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fIDL_Constant__fIDL_Constant61", None)
        self.__fIDL_Constant61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fIDL_VectorType60"):
                opp_val = getattr(old_value, "fIDL_VectorType60", None)
                if opp_val == self:
                    setattr(old_value, "fIDL_VectorType60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fIDL_VectorType60"):
                opp_val = getattr(value, "fIDL_VectorType60", None)
                setattr(value, "fIDL_VectorType60", self)

    @property
    def fIDL_Constant43(self):
        return self.__fIDL_Constant43

    @fIDL_Constant43.setter
    def fIDL_Constant43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fIDL_Constant__fIDL_Constant43", None)
        self.__fIDL_Constant43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fIDL_StructField42"):
                opp_val = getattr(old_value, "fIDL_StructField42", None)
                if opp_val == self:
                    setattr(old_value, "fIDL_StructField42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fIDL_StructField42"):
                opp_val = getattr(value, "fIDL_StructField42", None)
                setattr(value, "fIDL_StructField42", self)

    @property
    def fIDL_Constant56(self):
        return self.__fIDL_Constant56

    @fIDL_Constant56.setter
    def fIDL_Constant56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fIDL_Constant__fIDL_Constant56", None)
        self.__fIDL_Constant56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fIDL_ArrayType55"):
                opp_val = getattr(old_value, "fIDL_ArrayType55", None)
                if opp_val == self:
                    setattr(old_value, "fIDL_ArrayType55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fIDL_ArrayType55"):
                opp_val = getattr(value, "fIDL_ArrayType55", None)
                setattr(value, "fIDL_ArrayType55", self)

    @property
    def fIDL_Constant63(self):
        return self.__fIDL_Constant63

    @fIDL_Constant63.setter
    def fIDL_Constant63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fIDL_Constant__fIDL_Constant63", None)
        self.__fIDL_Constant63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fIDL_StringType"):
                opp_val = getattr(old_value, "fIDL_StringType", None)
                if opp_val == self:
                    setattr(old_value, "fIDL_StringType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fIDL_StringType"):
                opp_val = getattr(value, "fIDL_StringType", None)
                setattr(value, "fIDL_StringType", self)

    @property
    def fIDL_Constant(self):
        return self.__fIDL_Constant

    @fIDL_Constant.setter
    def fIDL_Constant(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fIDL_Constant__fIDL_Constant", None)
        self.__fIDL_Constant = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fIDL_ConstDeclaration9"):
                opp_val = getattr(old_value, "fIDL_ConstDeclaration9", None)
                if opp_val == self:
                    setattr(old_value, "fIDL_ConstDeclaration9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fIDL_ConstDeclaration9"):
                opp_val = getattr(value, "fIDL_ConstDeclaration9", None)
                setattr(value, "fIDL_ConstDeclaration9", self)

class fIDL_Type:

    pass
class InterfaceMember:

    pass
class fIDL_InterfaceMethod(InterfaceMember):

    pass
class fIDL_InterfaceMember:

    pass
class fIDL_Attribute:

    def __init__(self, name: str, value: str, fIDL_Attribute: "fIDL_AttributedDeclaration" = None):
        self.name = name
        self.value = value
        self.fIDL_Attribute = fIDL_Attribute
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fIDL_Attribute(self):
        return self.__fIDL_Attribute

    @fIDL_Attribute.setter
    def fIDL_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fIDL_Attribute__fIDL_Attribute", None)
        self.__fIDL_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fIDL_AttributedDeclaration4"):
                opp_val = getattr(old_value, "fIDL_AttributedDeclaration4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fIDL_AttributedDeclaration4"):
                opp_val = getattr(value, "fIDL_AttributedDeclaration4", None)
                if opp_val is None:
                    setattr(value, "fIDL_AttributedDeclaration4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class fIDL_AttributedDeclaration:

    pass
class fIDL_Using:

    def __init__(self, importedNamespace: str, name: str, fIDL_Using: "fIDL_LibraryHeader" = None):
        self.importedNamespace = importedNamespace
        self.name = name
        self.fIDL_Using = fIDL_Using
        
    @property
    def importedNamespace(self) -> str:
        return self.__importedNamespace

    @importedNamespace.setter
    def importedNamespace(self, importedNamespace: str):
        self.__importedNamespace = importedNamespace

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fIDL_Using(self):
        return self.__fIDL_Using

    @fIDL_Using.setter
    def fIDL_Using(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fIDL_Using__fIDL_Using", None)
        self.__fIDL_Using = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fIDL_LibraryHeader"):
                opp_val = getattr(old_value, "fIDL_LibraryHeader", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fIDL_LibraryHeader"):
                opp_val = getattr(value, "fIDL_LibraryHeader", None)
                if opp_val is None:
                    setattr(value, "fIDL_LibraryHeader", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class File:

    pass
class fIDL_LibraryHeader(File):

    def __init__(self, name: str, fIDL_LibraryHeader: set["fIDL_Using"] = None, fIDL_LibraryHeader2: set["fIDL_AttributedDeclaration"] = None):
        self.name = name
        self.fIDL_LibraryHeader = fIDL_LibraryHeader if fIDL_LibraryHeader is not None else set()
        self.fIDL_LibraryHeader2 = fIDL_LibraryHeader2 if fIDL_LibraryHeader2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fIDL_LibraryHeader(self):
        return self.__fIDL_LibraryHeader

    @fIDL_LibraryHeader.setter
    def fIDL_LibraryHeader(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fIDL_LibraryHeader__fIDL_LibraryHeader", None)
        self.__fIDL_LibraryHeader = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fIDL_Using"):
                    opp_val = getattr(item, "fIDL_Using", None)
                    
                    if opp_val == self:
                        setattr(item, "fIDL_Using", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fIDL_Using"):
                    opp_val = getattr(item, "fIDL_Using", None)
                    
                    setattr(item, "fIDL_Using", self)
                    

    @property
    def fIDL_LibraryHeader2(self):
        return self.__fIDL_LibraryHeader2

    @fIDL_LibraryHeader2.setter
    def fIDL_LibraryHeader2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fIDL_LibraryHeader__fIDL_LibraryHeader2", None)
        self.__fIDL_LibraryHeader2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fIDL_AttributedDeclaration"):
                    opp_val = getattr(item, "fIDL_AttributedDeclaration", None)
                    
                    if opp_val == self:
                        setattr(item, "fIDL_AttributedDeclaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fIDL_AttributedDeclaration"):
                    opp_val = getattr(item, "fIDL_AttributedDeclaration", None)
                    
                    setattr(item, "fIDL_AttributedDeclaration", self)
                    

class fIDL_File:

    pass
class Declaration:

    pass
class fIDL_UnionDeclaration(Declaration):

    pass
class fIDL_EnumDeclaration(Declaration):

    pass
class fIDL_InterfaceDeclaration(Declaration):

    pass
class fIDL_StructDeclaration(Declaration):

    pass
class fIDL_ConstDeclaration(InterfaceMember, Declaration):

    pass
class fIDL_Declaration:

    def __init__(self, name: str, fIDL_Declaration: "fIDL_AttributedDeclaration" = None, fIDL_Declaration51: "fIDL_IdentifierType" = None, fIDL_Declaration65: "fIDL_RequestType" = None):
        self.name = name
        self.fIDL_Declaration = fIDL_Declaration
        self.fIDL_Declaration51 = fIDL_Declaration51
        self.fIDL_Declaration65 = fIDL_Declaration65
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fIDL_Declaration(self):
        return self.__fIDL_Declaration

    @fIDL_Declaration.setter
    def fIDL_Declaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fIDL_Declaration__fIDL_Declaration", None)
        self.__fIDL_Declaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fIDL_AttributedDeclaration6"):
                opp_val = getattr(old_value, "fIDL_AttributedDeclaration6", None)
                if opp_val == self:
                    setattr(old_value, "fIDL_AttributedDeclaration6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fIDL_AttributedDeclaration6"):
                opp_val = getattr(value, "fIDL_AttributedDeclaration6", None)
                setattr(value, "fIDL_AttributedDeclaration6", self)

    @property
    def fIDL_Declaration51(self):
        return self.__fIDL_Declaration51

    @fIDL_Declaration51.setter
    def fIDL_Declaration51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fIDL_Declaration__fIDL_Declaration51", None)
        self.__fIDL_Declaration51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fIDL_IdentifierType"):
                opp_val = getattr(old_value, "fIDL_IdentifierType", None)
                if opp_val == self:
                    setattr(old_value, "fIDL_IdentifierType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fIDL_IdentifierType"):
                opp_val = getattr(value, "fIDL_IdentifierType", None)
                setattr(value, "fIDL_IdentifierType", self)

    @property
    def fIDL_Declaration65(self):
        return self.__fIDL_Declaration65

    @fIDL_Declaration65.setter
    def fIDL_Declaration65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fIDL_Declaration__fIDL_Declaration65", None)
        self.__fIDL_Declaration65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fIDL_RequestType"):
                opp_val = getattr(old_value, "fIDL_RequestType", None)
                if opp_val == self:
                    setattr(old_value, "fIDL_RequestType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fIDL_RequestType"):
                opp_val = getattr(value, "fIDL_RequestType", None)
                setattr(value, "fIDL_RequestType", self)
