from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class EString(Enum):
    TO_UNSIGNED = "TO_UNSIGNED"
    RISING_EDGE = "RISING_EDGE"
    STD_LOGIC = "STD_LOGIC"
    STD_LOGIC_VECTOR = "STD_LOGIC_VECTOR"
    INTEGER = "INTEGER"
    NATURAL = "NATURAL"
    UNSIGNED = "UNSIGNED"
    STRING = "STRING"
    FALLING_EDGE = "FALLING_EDGE"
class RangeDirection(Enum):
    TO = "TO"
    DOWNTO = "DOWNTO"
class LogicalOperator(Enum):
    AND = "AND"
    OR = "OR"
    NAND = "NAND"
    NOR = "NOR"
    XOR = "XOR"
    XNOR = "XNOR"
class SignalKind(Enum):
    REGISTER = "REGISTER"
    BUS = "BUS"
class UnaryOperator(Enum):
    ABS = "ABS"
    NOT = "NOT"
class EntityClass(Enum):
    ENTITY = "ENTITY"
    ARCHITECTURE = "ARCHITECTURE"
    CONFIGURATION = "CONFIGURATION"
    PROCEDURE = "PROCEDURE"
    FUNCTION = "FUNCTION"
    PACKAGE = "PACKAGE"
    TYPE = "TYPE"
    SUBTYPE = "SUBTYPE"
    CONSTANT = "CONSTANT"
    SIGNAL = "SIGNAL"
    VARIABLE = "VARIABLE"
    COMPONENT = "COMPONENT"
    LABEL = "LABEL"
    LITERAL = "LITERAL"
    UNITS = "UNITS"
    GROUP = "GROUP"
    FILE = "FILE"
    NATURE = "NATURE"
    SUBNATURE = "SUBNATURE"
    QUANTITY = "QUANTITY"
    TERMINAL = "TERMINAL"
class RelationalOperator(Enum):
    EQ = "EQ"
    NEQ = "NEQ"
    LOWERTHAN = "LOWERTHAN"
    LE = "LE"
    GREATERTHAN = "GREATERTHAN"
    GE = "GE"
    ASSOCIATE = "ASSOCIATE"
class Mode(Enum):
    IN = "IN"
    OUT = "OUT"
    INOUT = "INOUT"
    BUFFER = "BUFFER"
    LINKAGE = "LINKAGE"
class Purity(Enum):
    PURE = "PURE"
    IMPURE = "IMPURE"
class Sign(Enum):
    PLUS = "PLUS"
    MINUS = "MINUS"
class ShiftOperator(Enum):
    SLL = "SLL"
    SRL = "SRL"
    SLA = "SLA"
    SRA = "SRA"
    ROL = "ROL"
    ROR = "ROR"
class AddingOperator(Enum):
    PLUS = "PLUS"
    MINUS = "MINUS"
    AMPERSAND = "AMPERSAND"
class MultiplyingOperator(Enum):
    MOD = "MOD"
    REM = "REM"
    MUL = "MUL"
    DIV = "DIV"
class BuiltinLibs(Enum):
    WORK = "WORK"


############################################
# Definition of Classes
############################################

class ValueExpression:

    pass
class vhdl_UnitValueExpression(ValueExpression):

    def __init__(self, unit: str):
        self.unit = unit
        
    @property
    def unit(self) -> str:
        return self.__unit

    @unit.setter
    def unit(self, unit: str):
        self.__unit = unit

class vhdl_ValueExpression:

    def __init__(self, value: str, vhdl_ValueExpression: "vhdl_Value" = None):
        self.value = value
        self.vhdl_ValueExpression = vhdl_ValueExpression
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def vhdl_ValueExpression(self):
        return self.__vhdl_ValueExpression

    @vhdl_ValueExpression.setter
    def vhdl_ValueExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_ValueExpression__vhdl_ValueExpression", None)
        self.__vhdl_ValueExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_Value"):
                opp_val = getattr(old_value, "vhdl_Value", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_Value", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_Value"):
                opp_val = getattr(value, "vhdl_Value", None)
                setattr(value, "vhdl_Value", self)

class vhdl_RecordField:

    def __init__(self, name: str, vhdl_RecordField: "vhdl_RecordTypeDefinition" = None, vhdl_RecordField240: "vhdl_Member" = None):
        self.name = name
        self.vhdl_RecordField = vhdl_RecordField
        self.vhdl_RecordField240 = vhdl_RecordField240
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def vhdl_RecordField(self):
        return self.__vhdl_RecordField

    @vhdl_RecordField.setter
    def vhdl_RecordField(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_RecordField__vhdl_RecordField", None)
        self.__vhdl_RecordField = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_RecordTypeDefinition"):
                opp_val = getattr(old_value, "vhdl_RecordTypeDefinition", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_RecordTypeDefinition"):
                opp_val = getattr(value, "vhdl_RecordTypeDefinition", None)
                if opp_val is None:
                    setattr(value, "vhdl_RecordTypeDefinition", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def vhdl_RecordField240(self):
        return self.__vhdl_RecordField240

    @vhdl_RecordField240.setter
    def vhdl_RecordField240(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_RecordField__vhdl_RecordField240", None)
        self.__vhdl_RecordField240 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_Member"):
                opp_val = getattr(old_value, "vhdl_Member", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_Member", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_Member"):
                opp_val = getattr(value, "vhdl_Member", None)
                setattr(value, "vhdl_Member", self)

class ArrayTypeDefinition:

    pass
class vhdl_ConstrainedArrayTypeDefinition(ArrayTypeDefinition):

    pass
class vhdl_UnconstrainedArrayTypeDefinition(ArrayTypeDefinition):

    def __init__(self, index: str):
        self.index = index
        
    @property
    def index(self) -> str:
        return self.__index

    @index.setter
    def index(self, index: str):
        self.__index = index

class CompositeTypeDefinition:

    pass
class vhdl_RecordTypeDefinition(CompositeTypeDefinition):

    pass
class vhdl_ArrayTypeDefinition(CompositeTypeDefinition):

    pass
class TypeDefinition:

    pass
class vhdl_FileTypeDefinition(TypeDefinition):

    def __init__(self, type: str):
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class vhdl_CompositeTypeDefinition(TypeDefinition):

    pass
class vhdl_EnumerationTypeDefinition(TypeDefinition):

    def __init__(self, literal: str):
        self.literal = literal
        
    @property
    def literal(self) -> str:
        return self.__literal

    @literal.setter
    def literal(self, literal: str):
        self.__literal = literal

class vhdl_AccessTypeDefinition(TypeDefinition):

    pass
class vhdl_TypeDefinition:

    pass
class Type:

    pass
class vhdl_TypeDeclaration(Type):

    pass
class vhdl_SubtypeDeclaration(Type):

    pass
class Expression:

    pass
class vhdl_LogicalExpression(Expression):

    def __init__(self, operator: str, vhdl_LogicalExpression: "vhdl_Expression" = None, vhdl_LogicalExpression202: "vhdl_Expression" = None):
        self.operator = operator
        self.vhdl_LogicalExpression = vhdl_LogicalExpression
        self.vhdl_LogicalExpression202 = vhdl_LogicalExpression202
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def vhdl_LogicalExpression(self):
        return self.__vhdl_LogicalExpression

    @vhdl_LogicalExpression.setter
    def vhdl_LogicalExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_LogicalExpression__vhdl_LogicalExpression", None)
        self.__vhdl_LogicalExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_Expression200"):
                opp_val = getattr(old_value, "vhdl_Expression200", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_Expression200", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_Expression200"):
                opp_val = getattr(value, "vhdl_Expression200", None)
                setattr(value, "vhdl_Expression200", self)

    @property
    def vhdl_LogicalExpression202(self):
        return self.__vhdl_LogicalExpression202

    @vhdl_LogicalExpression202.setter
    def vhdl_LogicalExpression202(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_LogicalExpression__vhdl_LogicalExpression202", None)
        self.__vhdl_LogicalExpression202 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_Expression203"):
                opp_val = getattr(old_value, "vhdl_Expression203", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_Expression203", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_Expression203"):
                opp_val = getattr(value, "vhdl_Expression203", None)
                setattr(value, "vhdl_Expression203", self)

class vhdl_Boolean(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class vhdl_Factor(Expression):

    pass
class vhdl_String(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class vhdl_Open(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class vhdl_RelationalExpression(Expression):

    def __init__(self, operator: str, vhdl_RelationalExpression: "vhdl_Expression" = None, vhdl_RelationalExpression207: "vhdl_Expression" = None):
        self.operator = operator
        self.vhdl_RelationalExpression = vhdl_RelationalExpression
        self.vhdl_RelationalExpression207 = vhdl_RelationalExpression207
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def vhdl_RelationalExpression(self):
        return self.__vhdl_RelationalExpression

    @vhdl_RelationalExpression.setter
    def vhdl_RelationalExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_RelationalExpression__vhdl_RelationalExpression", None)
        self.__vhdl_RelationalExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_Expression205"):
                opp_val = getattr(old_value, "vhdl_Expression205", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_Expression205", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_Expression205"):
                opp_val = getattr(value, "vhdl_Expression205", None)
                setattr(value, "vhdl_Expression205", self)

    @property
    def vhdl_RelationalExpression207(self):
        return self.__vhdl_RelationalExpression207

    @vhdl_RelationalExpression207.setter
    def vhdl_RelationalExpression207(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_RelationalExpression__vhdl_RelationalExpression207", None)
        self.__vhdl_RelationalExpression207 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_Expression208"):
                opp_val = getattr(old_value, "vhdl_Expression208", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_Expression208", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_Expression208"):
                opp_val = getattr(value, "vhdl_Expression208", None)
                setattr(value, "vhdl_Expression208", self)

class vhdl_MemberExpression(Expression):

    pass
class vhdl_BitString(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class vhdl_ShiftExpression(Expression):

    def __init__(self, operator: str, vhdl_ShiftExpression: "vhdl_Expression" = None, vhdl_ShiftExpression217: "vhdl_Expression" = None):
        self.operator = operator
        self.vhdl_ShiftExpression = vhdl_ShiftExpression
        self.vhdl_ShiftExpression217 = vhdl_ShiftExpression217
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def vhdl_ShiftExpression217(self):
        return self.__vhdl_ShiftExpression217

    @vhdl_ShiftExpression217.setter
    def vhdl_ShiftExpression217(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_ShiftExpression__vhdl_ShiftExpression217", None)
        self.__vhdl_ShiftExpression217 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_Expression218"):
                opp_val = getattr(old_value, "vhdl_Expression218", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_Expression218", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_Expression218"):
                opp_val = getattr(value, "vhdl_Expression218", None)
                setattr(value, "vhdl_Expression218", self)

    @property
    def vhdl_ShiftExpression(self):
        return self.__vhdl_ShiftExpression

    @vhdl_ShiftExpression.setter
    def vhdl_ShiftExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_ShiftExpression__vhdl_ShiftExpression", None)
        self.__vhdl_ShiftExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_Expression215"):
                opp_val = getattr(old_value, "vhdl_Expression215", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_Expression215", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_Expression215"):
                opp_val = getattr(value, "vhdl_Expression215", None)
                setattr(value, "vhdl_Expression215", self)

class vhdl_Others(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class vhdl_Variable(Expression):

    def __init__(self, name: str, vhdl_Variable: "vhdl_Variable" = None, vhdl_Variable187: "vhdl_Variable" = None):
        self.name = name
        self.vhdl_Variable = vhdl_Variable
        self.vhdl_Variable187 = vhdl_Variable187
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def vhdl_Variable(self):
        return self.__vhdl_Variable

    @vhdl_Variable.setter
    def vhdl_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_Variable__vhdl_Variable", None)
        self.__vhdl_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_Variable187"):
                opp_val = getattr(old_value, "vhdl_Variable187", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_Variable187", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_Variable187"):
                opp_val = getattr(value, "vhdl_Variable187", None)
                setattr(value, "vhdl_Variable187", self)

    @property
    def vhdl_Variable187(self):
        return self.__vhdl_Variable187

    @vhdl_Variable187.setter
    def vhdl_Variable187(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_Variable__vhdl_Variable187", None)
        self.__vhdl_Variable187 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_Variable"):
                opp_val = getattr(old_value, "vhdl_Variable", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_Variable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_Variable"):
                opp_val = getattr(value, "vhdl_Variable", None)
                setattr(value, "vhdl_Variable", self)

class vhdl_Member(Expression):

    pass
class vhdl_Value(Expression):

    pass
class vhdl_MultiExpression(Expression):

    pass
class vhdl_AddingExpression(Expression):

    def __init__(self, operator: str, vhdl_AddingExpression222: "vhdl_Expression" = None, vhdl_AddingExpression: "vhdl_Expression" = None):
        self.operator = operator
        self.vhdl_AddingExpression222 = vhdl_AddingExpression222
        self.vhdl_AddingExpression = vhdl_AddingExpression
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def vhdl_AddingExpression(self):
        return self.__vhdl_AddingExpression

    @vhdl_AddingExpression.setter
    def vhdl_AddingExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_AddingExpression__vhdl_AddingExpression", None)
        self.__vhdl_AddingExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_Expression220"):
                opp_val = getattr(old_value, "vhdl_Expression220", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_Expression220", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_Expression220"):
                opp_val = getattr(value, "vhdl_Expression220", None)
                setattr(value, "vhdl_Expression220", self)

    @property
    def vhdl_AddingExpression222(self):
        return self.__vhdl_AddingExpression222

    @vhdl_AddingExpression222.setter
    def vhdl_AddingExpression222(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_AddingExpression__vhdl_AddingExpression222", None)
        self.__vhdl_AddingExpression222 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_Expression223"):
                opp_val = getattr(old_value, "vhdl_Expression223", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_Expression223", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_Expression223"):
                opp_val = getattr(value, "vhdl_Expression223", None)
                setattr(value, "vhdl_Expression223", self)

class vhdl_MultiplyingExpression(Expression):

    def __init__(self, operator: str, vhdl_MultiplyingExpression: "vhdl_Expression" = None, vhdl_MultiplyingExpression227: "vhdl_Expression" = None):
        self.operator = operator
        self.vhdl_MultiplyingExpression = vhdl_MultiplyingExpression
        self.vhdl_MultiplyingExpression227 = vhdl_MultiplyingExpression227
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def vhdl_MultiplyingExpression227(self):
        return self.__vhdl_MultiplyingExpression227

    @vhdl_MultiplyingExpression227.setter
    def vhdl_MultiplyingExpression227(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_MultiplyingExpression__vhdl_MultiplyingExpression227", None)
        self.__vhdl_MultiplyingExpression227 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_Expression228"):
                opp_val = getattr(old_value, "vhdl_Expression228", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_Expression228", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_Expression228"):
                opp_val = getattr(value, "vhdl_Expression228", None)
                setattr(value, "vhdl_Expression228", self)

    @property
    def vhdl_MultiplyingExpression(self):
        return self.__vhdl_MultiplyingExpression

    @vhdl_MultiplyingExpression.setter
    def vhdl_MultiplyingExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_MultiplyingExpression__vhdl_MultiplyingExpression", None)
        self.__vhdl_MultiplyingExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_Expression225"):
                opp_val = getattr(old_value, "vhdl_Expression225", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_Expression225", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_Expression225"):
                opp_val = getattr(value, "vhdl_Expression225", None)
                setattr(value, "vhdl_Expression225", self)

class vhdl_SliceExpression(Expression):

    pass
class vhdl_Char(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class vhdl_ConditionalWaveformExpression(Expression):

    pass
class vhdl_BuiltinFuncs(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class vhdl_ChoiceExpression(Expression):

    pass
class vhdl_RangeExpression(Expression):

    def __init__(self, direction: str, operator: str, vhdl_RangeExpression: "vhdl_Expression" = None, vhdl_RangeExpression197: "vhdl_Expression" = None):
        self.direction = direction
        self.operator = operator
        self.vhdl_RangeExpression = vhdl_RangeExpression
        self.vhdl_RangeExpression197 = vhdl_RangeExpression197
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

    @property
    def vhdl_RangeExpression197(self):
        return self.__vhdl_RangeExpression197

    @vhdl_RangeExpression197.setter
    def vhdl_RangeExpression197(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_RangeExpression__vhdl_RangeExpression197", None)
        self.__vhdl_RangeExpression197 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_Expression198"):
                opp_val = getattr(old_value, "vhdl_Expression198", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_Expression198", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_Expression198"):
                opp_val = getattr(value, "vhdl_Expression198", None)
                setattr(value, "vhdl_Expression198", self)

    @property
    def vhdl_RangeExpression(self):
        return self.__vhdl_RangeExpression

    @vhdl_RangeExpression.setter
    def vhdl_RangeExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_RangeExpression__vhdl_RangeExpression", None)
        self.__vhdl_RangeExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_Expression195"):
                opp_val = getattr(old_value, "vhdl_Expression195", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_Expression195", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_Expression195"):
                opp_val = getattr(value, "vhdl_Expression195", None)
                setattr(value, "vhdl_Expression195", self)

class IterationScheme:

    pass
class vhdl_ForIterationScheme(IterationScheme):

    def __init__(self, variable: str, vhdl_ForIterationScheme: "vhdl_Expression" = None):
        self.variable = variable
        self.vhdl_ForIterationScheme = vhdl_ForIterationScheme
        
    @property
    def variable(self) -> str:
        return self.__variable

    @variable.setter
    def variable(self, variable: str):
        self.__variable = variable

    @property
    def vhdl_ForIterationScheme(self):
        return self.__vhdl_ForIterationScheme

    @vhdl_ForIterationScheme.setter
    def vhdl_ForIterationScheme(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_ForIterationScheme__vhdl_ForIterationScheme", None)
        self.__vhdl_ForIterationScheme = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_Expression168"):
                opp_val = getattr(old_value, "vhdl_Expression168", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_Expression168", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_Expression168"):
                opp_val = getattr(value, "vhdl_Expression168", None)
                setattr(value, "vhdl_Expression168", self)

class vhdl_WhileIterationScheme(IterationScheme):

    pass
class vhdl_IterationScheme:

    pass
class vhdl_CaseAlternative:

    pass
class vhdl_IfStatementTest:

    pass
class SequentialStatement:

    pass
class vhdl_LoopStatement(SequentialStatement):

    pass
class vhdl_IfStatement(SequentialStatement):

    def __init__(self, label: str, vhdl_IfStatement: set["vhdl_IfStatementTest"] = None, vhdl_IfStatement134: set["vhdl_SequentialStatement"] = None):
        self.label = label
        self.vhdl_IfStatement = vhdl_IfStatement if vhdl_IfStatement is not None else set()
        self.vhdl_IfStatement134 = vhdl_IfStatement134 if vhdl_IfStatement134 is not None else set()
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def vhdl_IfStatement134(self):
        return self.__vhdl_IfStatement134

    @vhdl_IfStatement134.setter
    def vhdl_IfStatement134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_IfStatement__vhdl_IfStatement134", None)
        self.__vhdl_IfStatement134 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "vhdl_SequentialStatement135"):
                    opp_val = getattr(item, "vhdl_SequentialStatement135", None)
                    
                    if opp_val == self:
                        setattr(item, "vhdl_SequentialStatement135", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "vhdl_SequentialStatement135"):
                    opp_val = getattr(item, "vhdl_SequentialStatement135", None)
                    
                    setattr(item, "vhdl_SequentialStatement135", self)
                    

    @property
    def vhdl_IfStatement(self):
        return self.__vhdl_IfStatement

    @vhdl_IfStatement.setter
    def vhdl_IfStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_IfStatement__vhdl_IfStatement", None)
        self.__vhdl_IfStatement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "vhdl_IfStatementTest"):
                    opp_val = getattr(item, "vhdl_IfStatementTest", None)
                    
                    if opp_val == self:
                        setattr(item, "vhdl_IfStatementTest", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "vhdl_IfStatementTest"):
                    opp_val = getattr(item, "vhdl_IfStatementTest", None)
                    
                    setattr(item, "vhdl_IfStatementTest", self)
                    

class vhdl_CaseStatement(SequentialStatement):

    def __init__(self, label: str, vhdl_CaseStatement: "vhdl_Expression" = None, vhdl_CaseStatement145: set["vhdl_CaseAlternative"] = None):
        self.label = label
        self.vhdl_CaseStatement = vhdl_CaseStatement
        self.vhdl_CaseStatement145 = vhdl_CaseStatement145 if vhdl_CaseStatement145 is not None else set()
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def vhdl_CaseStatement145(self):
        return self.__vhdl_CaseStatement145

    @vhdl_CaseStatement145.setter
    def vhdl_CaseStatement145(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_CaseStatement__vhdl_CaseStatement145", None)
        self.__vhdl_CaseStatement145 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "vhdl_CaseAlternative"):
                    opp_val = getattr(item, "vhdl_CaseAlternative", None)
                    
                    if opp_val == self:
                        setattr(item, "vhdl_CaseAlternative", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "vhdl_CaseAlternative"):
                    opp_val = getattr(item, "vhdl_CaseAlternative", None)
                    
                    setattr(item, "vhdl_CaseAlternative", self)
                    

    @property
    def vhdl_CaseStatement(self):
        return self.__vhdl_CaseStatement

    @vhdl_CaseStatement.setter
    def vhdl_CaseStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_CaseStatement__vhdl_CaseStatement", None)
        self.__vhdl_CaseStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_Expression143"):
                opp_val = getattr(old_value, "vhdl_Expression143", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_Expression143", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_Expression143"):
                opp_val = getattr(value, "vhdl_Expression143", None)
                setattr(value, "vhdl_Expression143", self)

class vhdl_SequentialSignalAssignmentStatement(SequentialStatement):

    def __init__(self, label: str, postponed: bool, guarded: bool, vhdl_SequentialSignalAssignmentStatement: "vhdl_Expression" = None, vhdl_SequentialSignalAssignmentStatement163: "vhdl_Expression" = None):
        self.label = label
        self.postponed = postponed
        self.guarded = guarded
        self.vhdl_SequentialSignalAssignmentStatement = vhdl_SequentialSignalAssignmentStatement
        self.vhdl_SequentialSignalAssignmentStatement163 = vhdl_SequentialSignalAssignmentStatement163
        
    @property
    def guarded(self) -> bool:
        return self.__guarded

    @guarded.setter
    def guarded(self, guarded: bool):
        self.__guarded = guarded

    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def postponed(self) -> bool:
        return self.__postponed

    @postponed.setter
    def postponed(self, postponed: bool):
        self.__postponed = postponed

    @property
    def vhdl_SequentialSignalAssignmentStatement(self):
        return self.__vhdl_SequentialSignalAssignmentStatement

    @vhdl_SequentialSignalAssignmentStatement.setter
    def vhdl_SequentialSignalAssignmentStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_SequentialSignalAssignmentStatement__vhdl_SequentialSignalAssignmentStatement", None)
        self.__vhdl_SequentialSignalAssignmentStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_Expression161"):
                opp_val = getattr(old_value, "vhdl_Expression161", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_Expression161", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_Expression161"):
                opp_val = getattr(value, "vhdl_Expression161", None)
                setattr(value, "vhdl_Expression161", self)

    @property
    def vhdl_SequentialSignalAssignmentStatement163(self):
        return self.__vhdl_SequentialSignalAssignmentStatement163

    @vhdl_SequentialSignalAssignmentStatement163.setter
    def vhdl_SequentialSignalAssignmentStatement163(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_SequentialSignalAssignmentStatement__vhdl_SequentialSignalAssignmentStatement163", None)
        self.__vhdl_SequentialSignalAssignmentStatement163 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_Expression164"):
                opp_val = getattr(old_value, "vhdl_Expression164", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_Expression164", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_Expression164"):
                opp_val = getattr(value, "vhdl_Expression164", None)
                setattr(value, "vhdl_Expression164", self)

class vhdl_WaitStatement(SequentialStatement):

    def __init__(self, label: str, vhdl_WaitStatement: "vhdl_IdList" = None, vhdl_WaitStatement127: "vhdl_Expression" = None, vhdl_WaitStatement130: "vhdl_Expression" = None):
        self.label = label
        self.vhdl_WaitStatement = vhdl_WaitStatement
        self.vhdl_WaitStatement127 = vhdl_WaitStatement127
        self.vhdl_WaitStatement130 = vhdl_WaitStatement130
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def vhdl_WaitStatement130(self):
        return self.__vhdl_WaitStatement130

    @vhdl_WaitStatement130.setter
    def vhdl_WaitStatement130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_WaitStatement__vhdl_WaitStatement130", None)
        self.__vhdl_WaitStatement130 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_Expression131"):
                opp_val = getattr(old_value, "vhdl_Expression131", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_Expression131", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_Expression131"):
                opp_val = getattr(value, "vhdl_Expression131", None)
                setattr(value, "vhdl_Expression131", self)

    @property
    def vhdl_WaitStatement127(self):
        return self.__vhdl_WaitStatement127

    @vhdl_WaitStatement127.setter
    def vhdl_WaitStatement127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_WaitStatement__vhdl_WaitStatement127", None)
        self.__vhdl_WaitStatement127 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_Expression128"):
                opp_val = getattr(old_value, "vhdl_Expression128", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_Expression128", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_Expression128"):
                opp_val = getattr(value, "vhdl_Expression128", None)
                setattr(value, "vhdl_Expression128", self)

    @property
    def vhdl_WaitStatement(self):
        return self.__vhdl_WaitStatement

    @vhdl_WaitStatement.setter
    def vhdl_WaitStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_WaitStatement__vhdl_WaitStatement", None)
        self.__vhdl_WaitStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_IdList125"):
                opp_val = getattr(old_value, "vhdl_IdList125", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_IdList125", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_IdList125"):
                opp_val = getattr(value, "vhdl_IdList125", None)
                setattr(value, "vhdl_IdList125", self)

class vhdl_GenericMapAssociation:

    def __init__(self, formal: str, vhdl_GenericMapAssociation: "vhdl_GenericMap" = None, vhdl_GenericMapAssociation87: "vhdl_Expression" = None):
        self.formal = formal
        self.vhdl_GenericMapAssociation = vhdl_GenericMapAssociation
        self.vhdl_GenericMapAssociation87 = vhdl_GenericMapAssociation87
        
    @property
    def formal(self) -> str:
        return self.__formal

    @formal.setter
    def formal(self, formal: str):
        self.__formal = formal

    @property
    def vhdl_GenericMapAssociation(self):
        return self.__vhdl_GenericMapAssociation

    @vhdl_GenericMapAssociation.setter
    def vhdl_GenericMapAssociation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_GenericMapAssociation__vhdl_GenericMapAssociation", None)
        self.__vhdl_GenericMapAssociation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_GenericMap85"):
                opp_val = getattr(old_value, "vhdl_GenericMap85", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_GenericMap85"):
                opp_val = getattr(value, "vhdl_GenericMap85", None)
                if opp_val is None:
                    setattr(value, "vhdl_GenericMap85", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def vhdl_GenericMapAssociation87(self):
        return self.__vhdl_GenericMapAssociation87

    @vhdl_GenericMapAssociation87.setter
    def vhdl_GenericMapAssociation87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_GenericMapAssociation__vhdl_GenericMapAssociation87", None)
        self.__vhdl_GenericMapAssociation87 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_Expression88"):
                opp_val = getattr(old_value, "vhdl_Expression88", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_Expression88", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_Expression88"):
                opp_val = getattr(value, "vhdl_Expression88", None)
                setattr(value, "vhdl_Expression88", self)

class vhdl_PortMapAssociation:

    def __init__(self, formal: str, vhdl_PortMapAssociation: "vhdl_PortMap" = None, vhdl_PortMapAssociation82: "vhdl_Expression" = None):
        self.formal = formal
        self.vhdl_PortMapAssociation = vhdl_PortMapAssociation
        self.vhdl_PortMapAssociation82 = vhdl_PortMapAssociation82
        
    @property
    def formal(self) -> str:
        return self.__formal

    @formal.setter
    def formal(self, formal: str):
        self.__formal = formal

    @property
    def vhdl_PortMapAssociation82(self):
        return self.__vhdl_PortMapAssociation82

    @vhdl_PortMapAssociation82.setter
    def vhdl_PortMapAssociation82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_PortMapAssociation__vhdl_PortMapAssociation82", None)
        self.__vhdl_PortMapAssociation82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_Expression83"):
                opp_val = getattr(old_value, "vhdl_Expression83", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_Expression83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_Expression83"):
                opp_val = getattr(value, "vhdl_Expression83", None)
                setattr(value, "vhdl_Expression83", self)

    @property
    def vhdl_PortMapAssociation(self):
        return self.__vhdl_PortMapAssociation

    @vhdl_PortMapAssociation.setter
    def vhdl_PortMapAssociation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_PortMapAssociation__vhdl_PortMapAssociation", None)
        self.__vhdl_PortMapAssociation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_PortMap80"):
                opp_val = getattr(old_value, "vhdl_PortMap80", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_PortMap80"):
                opp_val = getattr(value, "vhdl_PortMap80", None)
                if opp_val is None:
                    setattr(value, "vhdl_PortMap80", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class vhdl_PortMap:

    pass
class vhdl_GenericMap:

    pass
class vhdl_SequentialStatement:

    pass
class vhdl_IdList:

    pass
class ArchitectureStatement:

    pass
class vhdl_IfGenerateStatement(ArchitectureStatement):

    pass
class vhdl_ComponentInstantiationStatement(ArchitectureStatement):

    def __init__(self, name: str, vhdl_ComponentInstantiationStatement: "vhdl_GenericMap" = None, vhdl_ComponentInstantiationStatement70: "vhdl_PortMap" = None):
        self.name = name
        self.vhdl_ComponentInstantiationStatement = vhdl_ComponentInstantiationStatement
        self.vhdl_ComponentInstantiationStatement70 = vhdl_ComponentInstantiationStatement70
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def vhdl_ComponentInstantiationStatement(self):
        return self.__vhdl_ComponentInstantiationStatement

    @vhdl_ComponentInstantiationStatement.setter
    def vhdl_ComponentInstantiationStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_ComponentInstantiationStatement__vhdl_ComponentInstantiationStatement", None)
        self.__vhdl_ComponentInstantiationStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_GenericMap"):
                opp_val = getattr(old_value, "vhdl_GenericMap", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_GenericMap", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_GenericMap"):
                opp_val = getattr(value, "vhdl_GenericMap", None)
                setattr(value, "vhdl_GenericMap", self)

    @property
    def vhdl_ComponentInstantiationStatement70(self):
        return self.__vhdl_ComponentInstantiationStatement70

    @vhdl_ComponentInstantiationStatement70.setter
    def vhdl_ComponentInstantiationStatement70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_ComponentInstantiationStatement__vhdl_ComponentInstantiationStatement70", None)
        self.__vhdl_ComponentInstantiationStatement70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_PortMap"):
                opp_val = getattr(old_value, "vhdl_PortMap", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_PortMap", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_PortMap"):
                opp_val = getattr(value, "vhdl_PortMap", None)
                setattr(value, "vhdl_PortMap", self)

class vhdl_ForGenerateStatement(ArchitectureStatement):

    pass
class vhdl_ConditionalSignalAssignmentStatement(ArchitectureStatement):

    def __init__(self, postponed: bool, guarded: bool, vhdl_ConditionalSignalAssignmentStatement: "vhdl_Expression" = None, vhdl_ConditionalSignalAssignmentStatement92: set["vhdl_Expression"] = None):
        self.postponed = postponed
        self.guarded = guarded
        self.vhdl_ConditionalSignalAssignmentStatement = vhdl_ConditionalSignalAssignmentStatement
        self.vhdl_ConditionalSignalAssignmentStatement92 = vhdl_ConditionalSignalAssignmentStatement92 if vhdl_ConditionalSignalAssignmentStatement92 is not None else set()
        
    @property
    def postponed(self) -> bool:
        return self.__postponed

    @postponed.setter
    def postponed(self, postponed: bool):
        self.__postponed = postponed

    @property
    def guarded(self) -> bool:
        return self.__guarded

    @guarded.setter
    def guarded(self, guarded: bool):
        self.__guarded = guarded

    @property
    def vhdl_ConditionalSignalAssignmentStatement(self):
        return self.__vhdl_ConditionalSignalAssignmentStatement

    @vhdl_ConditionalSignalAssignmentStatement.setter
    def vhdl_ConditionalSignalAssignmentStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_ConditionalSignalAssignmentStatement__vhdl_ConditionalSignalAssignmentStatement", None)
        self.__vhdl_ConditionalSignalAssignmentStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_Expression90"):
                opp_val = getattr(old_value, "vhdl_Expression90", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_Expression90", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_Expression90"):
                opp_val = getattr(value, "vhdl_Expression90", None)
                setattr(value, "vhdl_Expression90", self)

    @property
    def vhdl_ConditionalSignalAssignmentStatement92(self):
        return self.__vhdl_ConditionalSignalAssignmentStatement92

    @vhdl_ConditionalSignalAssignmentStatement92.setter
    def vhdl_ConditionalSignalAssignmentStatement92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_ConditionalSignalAssignmentStatement__vhdl_ConditionalSignalAssignmentStatement92", None)
        self.__vhdl_ConditionalSignalAssignmentStatement92 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "vhdl_Expression93"):
                    opp_val = getattr(item, "vhdl_Expression93", None)
                    
                    if opp_val == self:
                        setattr(item, "vhdl_Expression93", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "vhdl_Expression93"):
                    opp_val = getattr(item, "vhdl_Expression93", None)
                    
                    setattr(item, "vhdl_Expression93", self)
                    

class vhdl_EntityInstantiationStatement(ArchitectureStatement):

    def __init__(self, name: str, vhdl_EntityInstantiationStatement: "vhdl_Library" = None, vhdl_EntityInstantiationStatement74: "vhdl_GenericMap" = None, vhdl_EntityInstantiationStatement77: "vhdl_PortMap" = None):
        self.name = name
        self.vhdl_EntityInstantiationStatement = vhdl_EntityInstantiationStatement
        self.vhdl_EntityInstantiationStatement74 = vhdl_EntityInstantiationStatement74
        self.vhdl_EntityInstantiationStatement77 = vhdl_EntityInstantiationStatement77
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def vhdl_EntityInstantiationStatement(self):
        return self.__vhdl_EntityInstantiationStatement

    @vhdl_EntityInstantiationStatement.setter
    def vhdl_EntityInstantiationStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_EntityInstantiationStatement__vhdl_EntityInstantiationStatement", None)
        self.__vhdl_EntityInstantiationStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_Library72"):
                opp_val = getattr(old_value, "vhdl_Library72", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_Library72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_Library72"):
                opp_val = getattr(value, "vhdl_Library72", None)
                setattr(value, "vhdl_Library72", self)

    @property
    def vhdl_EntityInstantiationStatement77(self):
        return self.__vhdl_EntityInstantiationStatement77

    @vhdl_EntityInstantiationStatement77.setter
    def vhdl_EntityInstantiationStatement77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_EntityInstantiationStatement__vhdl_EntityInstantiationStatement77", None)
        self.__vhdl_EntityInstantiationStatement77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_PortMap78"):
                opp_val = getattr(old_value, "vhdl_PortMap78", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_PortMap78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_PortMap78"):
                opp_val = getattr(value, "vhdl_PortMap78", None)
                setattr(value, "vhdl_PortMap78", self)

    @property
    def vhdl_EntityInstantiationStatement74(self):
        return self.__vhdl_EntityInstantiationStatement74

    @vhdl_EntityInstantiationStatement74.setter
    def vhdl_EntityInstantiationStatement74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_EntityInstantiationStatement__vhdl_EntityInstantiationStatement74", None)
        self.__vhdl_EntityInstantiationStatement74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_GenericMap75"):
                opp_val = getattr(old_value, "vhdl_GenericMap75", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_GenericMap75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_GenericMap75"):
                opp_val = getattr(value, "vhdl_GenericMap75", None)
                setattr(value, "vhdl_GenericMap75", self)

class vhdl_ProcessStatement(ArchitectureStatement):

    def __init__(self, postponed: bool, vhdl_ProcessStatement: "vhdl_IdList" = None, vhdl_ProcessStatement67: set["vhdl_SequentialStatement"] = None):
        self.postponed = postponed
        self.vhdl_ProcessStatement = vhdl_ProcessStatement
        self.vhdl_ProcessStatement67 = vhdl_ProcessStatement67 if vhdl_ProcessStatement67 is not None else set()
        
    @property
    def postponed(self) -> bool:
        return self.__postponed

    @postponed.setter
    def postponed(self, postponed: bool):
        self.__postponed = postponed

    @property
    def vhdl_ProcessStatement(self):
        return self.__vhdl_ProcessStatement

    @vhdl_ProcessStatement.setter
    def vhdl_ProcessStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_ProcessStatement__vhdl_ProcessStatement", None)
        self.__vhdl_ProcessStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_IdList"):
                opp_val = getattr(old_value, "vhdl_IdList", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_IdList", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_IdList"):
                opp_val = getattr(value, "vhdl_IdList", None)
                setattr(value, "vhdl_IdList", self)

    @property
    def vhdl_ProcessStatement67(self):
        return self.__vhdl_ProcessStatement67

    @vhdl_ProcessStatement67.setter
    def vhdl_ProcessStatement67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_ProcessStatement__vhdl_ProcessStatement67", None)
        self.__vhdl_ProcessStatement67 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "vhdl_SequentialStatement"):
                    opp_val = getattr(item, "vhdl_SequentialStatement", None)
                    
                    if opp_val == self:
                        setattr(item, "vhdl_SequentialStatement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "vhdl_SequentialStatement"):
                    opp_val = getattr(item, "vhdl_SequentialStatement", None)
                    
                    setattr(item, "vhdl_SequentialStatement", self)
                    

class package_declarative_item:

    pass
class BlockDeclarativeItem:

    pass
class vhdl_AttributeSpecification(BlockDeclarativeItem):

    def __init__(self, name: str, entity: str, class: str, vhdl_AttributeSpecification: "vhdl_Expression" = None):
        self.name = name
        self.entity = entity
        self.class = class
        self.vhdl_AttributeSpecification = vhdl_AttributeSpecification
        
    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def entity(self) -> str:
        return self.__entity

    @entity.setter
    def entity(self, entity: str):
        self.__entity = entity

    @property
    def vhdl_AttributeSpecification(self):
        return self.__vhdl_AttributeSpecification

    @vhdl_AttributeSpecification.setter
    def vhdl_AttributeSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_AttributeSpecification__vhdl_AttributeSpecification", None)
        self.__vhdl_AttributeSpecification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_Expression59"):
                opp_val = getattr(old_value, "vhdl_Expression59", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_Expression59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_Expression59"):
                opp_val = getattr(value, "vhdl_Expression59", None)
                setattr(value, "vhdl_Expression59", self)

class vhdl_Component(BlockDeclarativeItem, package_declarative_item):

    def __init__(self, name: str, vhdl_Component: "vhdl_Generics" = None, vhdl_Component63: "vhdl_Ports" = None):
        self.name = name
        self.vhdl_Component = vhdl_Component
        self.vhdl_Component63 = vhdl_Component63
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def vhdl_Component(self):
        return self.__vhdl_Component

    @vhdl_Component.setter
    def vhdl_Component(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_Component__vhdl_Component", None)
        self.__vhdl_Component = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_Generics61"):
                opp_val = getattr(old_value, "vhdl_Generics61", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_Generics61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_Generics61"):
                opp_val = getattr(value, "vhdl_Generics61", None)
                setattr(value, "vhdl_Generics61", self)

    @property
    def vhdl_Component63(self):
        return self.__vhdl_Component63

    @vhdl_Component63.setter
    def vhdl_Component63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_Component__vhdl_Component63", None)
        self.__vhdl_Component63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_Ports64"):
                opp_val = getattr(old_value, "vhdl_Ports64", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_Ports64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_Ports64"):
                opp_val = getattr(value, "vhdl_Ports64", None)
                setattr(value, "vhdl_Ports64", self)

class vhdl_AttributeDeclaration(BlockDeclarativeItem):

    def __init__(self, name: str, type_id: str, type_keyword: str):
        self.name = name
        self.type_id = type_id
        self.type_keyword = type_keyword
        
    @property
    def type_keyword(self) -> str:
        return self.__type_keyword

    @type_keyword.setter
    def type_keyword(self, type_keyword: str):
        self.__type_keyword = type_keyword

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def type_id(self) -> str:
        return self.__type_id

    @type_id.setter
    def type_id(self, type_id: str):
        self.__type_id = type_id

class vhdl_SignalDeclaration(BlockDeclarativeItem, package_declarative_item):

    def __init__(self, kind: str, vhdl_SignalDeclaration: set["vhdl_Signal"] = None, vhdl_SignalDeclaration39: "vhdl_SubtypeIndication" = None, vhdl_SignalDeclaration42: "vhdl_Expression" = None):
        self.kind = kind
        self.vhdl_SignalDeclaration = vhdl_SignalDeclaration if vhdl_SignalDeclaration is not None else set()
        self.vhdl_SignalDeclaration39 = vhdl_SignalDeclaration39
        self.vhdl_SignalDeclaration42 = vhdl_SignalDeclaration42
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def vhdl_SignalDeclaration42(self):
        return self.__vhdl_SignalDeclaration42

    @vhdl_SignalDeclaration42.setter
    def vhdl_SignalDeclaration42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_SignalDeclaration__vhdl_SignalDeclaration42", None)
        self.__vhdl_SignalDeclaration42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_Expression43"):
                opp_val = getattr(old_value, "vhdl_Expression43", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_Expression43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_Expression43"):
                opp_val = getattr(value, "vhdl_Expression43", None)
                setattr(value, "vhdl_Expression43", self)

    @property
    def vhdl_SignalDeclaration(self):
        return self.__vhdl_SignalDeclaration

    @vhdl_SignalDeclaration.setter
    def vhdl_SignalDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_SignalDeclaration__vhdl_SignalDeclaration", None)
        self.__vhdl_SignalDeclaration = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "vhdl_Signal"):
                    opp_val = getattr(item, "vhdl_Signal", None)
                    
                    if opp_val == self:
                        setattr(item, "vhdl_Signal", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "vhdl_Signal"):
                    opp_val = getattr(item, "vhdl_Signal", None)
                    
                    setattr(item, "vhdl_Signal", self)
                    

    @property
    def vhdl_SignalDeclaration39(self):
        return self.__vhdl_SignalDeclaration39

    @vhdl_SignalDeclaration39.setter
    def vhdl_SignalDeclaration39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_SignalDeclaration__vhdl_SignalDeclaration39", None)
        self.__vhdl_SignalDeclaration39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_SubtypeIndication40"):
                opp_val = getattr(old_value, "vhdl_SubtypeIndication40", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_SubtypeIndication40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_SubtypeIndication40"):
                opp_val = getattr(value, "vhdl_SubtypeIndication40", None)
                setattr(value, "vhdl_SubtypeIndication40", self)

class vhdl_ConstantDeclaration(BlockDeclarativeItem, package_declarative_item):

    pass
class vhdl_VariableDeclaration(BlockDeclarativeItem, package_declarative_item):

    def __init__(self, shared: bool, vhdl_VariableDeclaration: set["vhdl_Var"] = None, vhdl_VariableDeclaration46: "vhdl_SubtypeIndication" = None, vhdl_VariableDeclaration49: "vhdl_Expression" = None):
        self.shared = shared
        self.vhdl_VariableDeclaration = vhdl_VariableDeclaration if vhdl_VariableDeclaration is not None else set()
        self.vhdl_VariableDeclaration46 = vhdl_VariableDeclaration46
        self.vhdl_VariableDeclaration49 = vhdl_VariableDeclaration49
        
    @property
    def shared(self) -> bool:
        return self.__shared

    @shared.setter
    def shared(self, shared: bool):
        self.__shared = shared

    @property
    def vhdl_VariableDeclaration46(self):
        return self.__vhdl_VariableDeclaration46

    @vhdl_VariableDeclaration46.setter
    def vhdl_VariableDeclaration46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_VariableDeclaration__vhdl_VariableDeclaration46", None)
        self.__vhdl_VariableDeclaration46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_SubtypeIndication47"):
                opp_val = getattr(old_value, "vhdl_SubtypeIndication47", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_SubtypeIndication47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_SubtypeIndication47"):
                opp_val = getattr(value, "vhdl_SubtypeIndication47", None)
                setattr(value, "vhdl_SubtypeIndication47", self)

    @property
    def vhdl_VariableDeclaration(self):
        return self.__vhdl_VariableDeclaration

    @vhdl_VariableDeclaration.setter
    def vhdl_VariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_VariableDeclaration__vhdl_VariableDeclaration", None)
        self.__vhdl_VariableDeclaration = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "vhdl_Var"):
                    opp_val = getattr(item, "vhdl_Var", None)
                    
                    if opp_val == self:
                        setattr(item, "vhdl_Var", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "vhdl_Var"):
                    opp_val = getattr(item, "vhdl_Var", None)
                    
                    setattr(item, "vhdl_Var", self)
                    

    @property
    def vhdl_VariableDeclaration49(self):
        return self.__vhdl_VariableDeclaration49

    @vhdl_VariableDeclaration49.setter
    def vhdl_VariableDeclaration49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_VariableDeclaration__vhdl_VariableDeclaration49", None)
        self.__vhdl_VariableDeclaration49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_Expression50"):
                opp_val = getattr(old_value, "vhdl_Expression50", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_Expression50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_Expression50"):
                opp_val = getattr(value, "vhdl_Expression50", None)
                setattr(value, "vhdl_Expression50", self)

class vhdl_Type(Expression, BlockDeclarativeItem, package_declarative_item):

    def __init__(self, value: str, name: str, vhdl_Type: "vhdl_SubtypeIndication" = None):
        self.value = value
        self.name = name
        self.vhdl_Type = vhdl_Type
        
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
    def vhdl_Type(self):
        return self.__vhdl_Type

    @vhdl_Type.setter
    def vhdl_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_Type__vhdl_Type", None)
        self.__vhdl_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_SubtypeIndication170"):
                opp_val = getattr(old_value, "vhdl_SubtypeIndication170", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_SubtypeIndication170", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_SubtypeIndication170"):
                opp_val = getattr(value, "vhdl_SubtypeIndication170", None)
                setattr(value, "vhdl_SubtypeIndication170", self)

class vhdl_Expression:

    def __init__(self, unary_operator: str, attribute: str, vhdl_Expression: "vhdl_Port" = None, vhdl_Expression31: "vhdl_Generic" = None, vhdl_Expression36: "vhdl_Alias" = None, vhdl_Expression43: "vhdl_SignalDeclaration" = None, vhdl_Expression50: "vhdl_VariableDeclaration" = None, vhdl_Expression57: "vhdl_ConstantDeclaration" = None, vhdl_Expression59: "vhdl_AttributeSpecification" = None, vhdl_Expression83: "vhdl_PortMapAssociation" = None, vhdl_Expression88: "vhdl_GenericMapAssociation" = None, vhdl_Expression90: "vhdl_ConditionalSignalAssignmentStatement" = None, vhdl_Expression93: "vhdl_ConditionalSignalAssignmentStatement" = None, vhdl_Expression96: "vhdl_Expression" = None, vhdl_Expression99: "vhdl_Expression" = None, vhdl_Expression97: "vhdl_Expression" = None, vhdl_Expression102: "vhdl_Expression" = None, vhdl_Expression100: "vhdl_Expression" = None, vhdl_Expression105: "vhdl_Expression" = None, vhdl_Expression103: "vhdl_Expression" = None, vhdl_Expression109: "vhdl_ForGenerateStatement" = None, vhdl_Expression117: "vhdl_IfGenerateStatement" = None, vhdl_Expression94: set["vhdl_Expression"] = None, vhdl_Expression128: "vhdl_WaitStatement" = None, vhdl_Expression131: "vhdl_WaitStatement" = None, vhdl_Expression138: "vhdl_IfStatementTest" = None, vhdl_Expression143: "vhdl_CaseStatement" = None, vhdl_Expression148: "vhdl_CaseAlternative" = None, vhdl_Expression156: "vhdl_LoopStatement" = None, vhdl_Expression161: "vhdl_SequentialSignalAssignmentStatement" = None, vhdl_Expression164: "vhdl_SequentialSignalAssignmentStatement" = None, vhdl_Expression166: "vhdl_WhileIterationScheme" = None, vhdl_Expression168: "vhdl_ForIterationScheme" = None, vhdl_Expression173: "vhdl_SubtypeIndication" = None, vhdl_Expression182: "vhdl_ConstrainedArrayTypeDefinition" = None, vhdl_Expression191: "vhdl_IdList" = None, vhdl_Expression193: "vhdl_ConditionalWaveformExpression" = None, vhdl_Expression195: "vhdl_RangeExpression" = None, vhdl_Expression198: "vhdl_RangeExpression" = None, vhdl_Expression200: "vhdl_LogicalExpression" = None, vhdl_Expression203: "vhdl_LogicalExpression" = None, vhdl_Expression205: "vhdl_RelationalExpression" = None, vhdl_Expression208: "vhdl_RelationalExpression" = None, vhdl_Expression210: "vhdl_ChoiceExpression" = None, vhdl_Expression213: "vhdl_ChoiceExpression" = None, vhdl_Expression215: "vhdl_ShiftExpression" = None, vhdl_Expression218: "vhdl_ShiftExpression" = None, vhdl_Expression223: "vhdl_AddingExpression" = None, vhdl_Expression225: "vhdl_MultiplyingExpression" = None, vhdl_Expression228: "vhdl_MultiplyingExpression" = None, vhdl_Expression230: "vhdl_Factor" = None, vhdl_Expression233: "vhdl_Factor" = None, vhdl_Expression235: "vhdl_MemberExpression" = None, vhdl_Expression238: "vhdl_MemberExpression" = None, vhdl_Expression220: "vhdl_AddingExpression" = None, vhdl_Expression243: "vhdl_Member" = None, vhdl_Expression245: "vhdl_SliceExpression" = None, vhdl_Expression248: "vhdl_SliceExpression" = None):
        self.unary_operator = unary_operator
        self.attribute = attribute
        self.vhdl_Expression = vhdl_Expression
        self.vhdl_Expression31 = vhdl_Expression31
        self.vhdl_Expression36 = vhdl_Expression36
        self.vhdl_Expression43 = vhdl_Expression43
        self.vhdl_Expression50 = vhdl_Expression50
        self.vhdl_Expression57 = vhdl_Expression57
        self.vhdl_Expression59 = vhdl_Expression59
        self.vhdl_Expression83 = vhdl_Expression83
        self.vhdl_Expression88 = vhdl_Expression88
        self.vhdl_Expression90 = vhdl_Expression90
        self.vhdl_Expression93 = vhdl_Expression93
        self.vhdl_Expression96 = vhdl_Expression96
        self.vhdl_Expression99 = vhdl_Expression99
        self.vhdl_Expression97 = vhdl_Expression97
        self.vhdl_Expression102 = vhdl_Expression102
        self.vhdl_Expression100 = vhdl_Expression100
        self.vhdl_Expression105 = vhdl_Expression105
        self.vhdl_Expression103 = vhdl_Expression103
        self.vhdl_Expression109 = vhdl_Expression109
        self.vhdl_Expression117 = vhdl_Expression117
        self.vhdl_Expression94 = vhdl_Expression94 if vhdl_Expression94 is not None else set()
        self.vhdl_Expression128 = vhdl_Expression128
        self.vhdl_Expression131 = vhdl_Expression131
        self.vhdl_Expression138 = vhdl_Expression138
        self.vhdl_Expression143 = vhdl_Expression143
        self.vhdl_Expression148 = vhdl_Expression148
        self.vhdl_Expression156 = vhdl_Expression156
        self.vhdl_Expression161 = vhdl_Expression161
        self.vhdl_Expression164 = vhdl_Expression164
        self.vhdl_Expression166 = vhdl_Expression166
        self.vhdl_Expression168 = vhdl_Expression168
        self.vhdl_Expression173 = vhdl_Expression173
        self.vhdl_Expression182 = vhdl_Expression182
        self.vhdl_Expression191 = vhdl_Expression191
        self.vhdl_Expression193 = vhdl_Expression193
        self.vhdl_Expression195 = vhdl_Expression195
        self.vhdl_Expression198 = vhdl_Expression198
        self.vhdl_Expression200 = vhdl_Expression200
        self.vhdl_Expression203 = vhdl_Expression203
        self.vhdl_Expression205 = vhdl_Expression205
        self.vhdl_Expression208 = vhdl_Expression208
        self.vhdl_Expression210 = vhdl_Expression210
        self.vhdl_Expression213 = vhdl_Expression213
        self.vhdl_Expression215 = vhdl_Expression215
        self.vhdl_Expression218 = vhdl_Expression218
        self.vhdl_Expression223 = vhdl_Expression223
        self.vhdl_Expression225 = vhdl_Expression225
        self.vhdl_Expression228 = vhdl_Expression228
        self.vhdl_Expression230 = vhdl_Expression230
        self.vhdl_Expression233 = vhdl_Expression233
        self.vhdl_Expression235 = vhdl_Expression235
        self.vhdl_Expression238 = vhdl_Expression238
        self.vhdl_Expression220 = vhdl_Expression220
        self.vhdl_Expression243 = vhdl_Expression243
        self.vhdl_Expression245 = vhdl_Expression245
        self.vhdl_Expression248 = vhdl_Expression248
        
    @property
    def attribute(self) -> str:
        return self.__attribute

    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def unary_operator(self) -> str:
        return self.__unary_operator

    @unary_operator.setter
    def unary_operator(self, unary_operator: str):
        self.__unary_operator = unary_operator

    @property
    def vhdl_Expression156(self):
        return self.__vhdl_Expression156

    @vhdl_Expression156.setter
    def vhdl_Expression156(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_Expression__vhdl_Expression156", None)
        self.__vhdl_Expression156 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_LoopStatement155"):
                opp_val = getattr(old_value, "vhdl_LoopStatement155", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_LoopStatement155", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_LoopStatement155"):
                opp_val = getattr(value, "vhdl_LoopStatement155", None)
                setattr(value, "vhdl_LoopStatement155", self)

    @property
    def vhdl_Expression161(self):
        return self.__vhdl_Expression161

    @vhdl_Expression161.setter
    def vhdl_Expression161(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_Expression__vhdl_Expression161", None)
        self.__vhdl_Expression161 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_SequentialSignalAssignmentStatement"):
                opp_val = getattr(old_value, "vhdl_SequentialSignalAssignmentStatement", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_SequentialSignalAssignmentStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_SequentialSignalAssignmentStatement"):
                opp_val = getattr(value, "vhdl_SequentialSignalAssignmentStatement", None)
                setattr(value, "vhdl_SequentialSignalAssignmentStatement", self)

    @property
    def vhdl_Expression191(self):
        return self.__vhdl_Expression191

    @vhdl_Expression191.setter
    def vhdl_Expression191(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_Expression__vhdl_Expression191", None)
        self.__vhdl_Expression191 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_IdList190"):
                opp_val = getattr(old_value, "vhdl_IdList190", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_IdList190"):
                opp_val = getattr(value, "vhdl_IdList190", None)
                if opp_val is None:
                    setattr(value, "vhdl_IdList190", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def vhdl_Expression168(self):
        return self.__vhdl_Expression168

    @vhdl_Expression168.setter
    def vhdl_Expression168(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_Expression__vhdl_Expression168", None)
        self.__vhdl_Expression168 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_ForIterationScheme"):
                opp_val = getattr(old_value, "vhdl_ForIterationScheme", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_ForIterationScheme", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_ForIterationScheme"):
                opp_val = getattr(value, "vhdl_ForIterationScheme", None)
                setattr(value, "vhdl_ForIterationScheme", self)

    @property
    def vhdl_Expression50(self):
        return self.__vhdl_Expression50

    @vhdl_Expression50.setter
    def vhdl_Expression50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_Expression__vhdl_Expression50", None)
        self.__vhdl_Expression50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_VariableDeclaration49"):
                opp_val = getattr(old_value, "vhdl_VariableDeclaration49", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_VariableDeclaration49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_VariableDeclaration49"):
                opp_val = getattr(value, "vhdl_VariableDeclaration49", None)
                setattr(value, "vhdl_VariableDeclaration49", self)

    @property
    def vhdl_Expression233(self):
        return self.__vhdl_Expression233

    @vhdl_Expression233.setter
    def vhdl_Expression233(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_Expression__vhdl_Expression233", None)
        self.__vhdl_Expression233 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_Factor232"):
                opp_val = getattr(old_value, "vhdl_Factor232", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_Factor232", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_Factor232"):
                opp_val = getattr(value, "vhdl_Factor232", None)
                setattr(value, "vhdl_Factor232", self)

    @property
    def vhdl_Expression(self):
        return self.__vhdl_Expression

    @vhdl_Expression.setter
    def vhdl_Expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_Expression__vhdl_Expression", None)
        self.__vhdl_Expression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_Port23"):
                opp_val = getattr(old_value, "vhdl_Port23", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_Port23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_Port23"):
                opp_val = getattr(value, "vhdl_Port23", None)
                setattr(value, "vhdl_Port23", self)

    @property
    def vhdl_Expression210(self):
        return self.__vhdl_Expression210

    @vhdl_Expression210.setter
    def vhdl_Expression210(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_Expression__vhdl_Expression210", None)
        self.__vhdl_Expression210 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_ChoiceExpression"):
                opp_val = getattr(old_value, "vhdl_ChoiceExpression", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_ChoiceExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_ChoiceExpression"):
                opp_val = getattr(value, "vhdl_ChoiceExpression", None)
                setattr(value, "vhdl_ChoiceExpression", self)

    @property
    def vhdl_Expression102(self):
        return self.__vhdl_Expression102

    @vhdl_Expression102.setter
    def vhdl_Expression102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_Expression__vhdl_Expression102", None)
        self.__vhdl_Expression102 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_Expression100"):
                opp_val = getattr(old_value, "vhdl_Expression100", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_Expression100", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_Expression100"):
                opp_val = getattr(value, "vhdl_Expression100", None)
                setattr(value, "vhdl_Expression100", self)

    @property
    def vhdl_Expression105(self):
        return self.__vhdl_Expression105

    @vhdl_Expression105.setter
    def vhdl_Expression105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_Expression__vhdl_Expression105", None)
        self.__vhdl_Expression105 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_Expression103"):
                opp_val = getattr(old_value, "vhdl_Expression103", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_Expression103", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_Expression103"):
                opp_val = getattr(value, "vhdl_Expression103", None)
                setattr(value, "vhdl_Expression103", self)

    @property
    def vhdl_Expression230(self):
        return self.__vhdl_Expression230

    @vhdl_Expression230.setter
    def vhdl_Expression230(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_Expression__vhdl_Expression230", None)
        self.__vhdl_Expression230 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_Factor"):
                opp_val = getattr(old_value, "vhdl_Factor", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_Factor", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_Factor"):
                opp_val = getattr(value, "vhdl_Factor", None)
                setattr(value, "vhdl_Factor", self)

    @property
    def vhdl_Expression103(self):
        return self.__vhdl_Expression103

    @vhdl_Expression103.setter
    def vhdl_Expression103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_Expression__vhdl_Expression103", None)
        self.__vhdl_Expression103 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_Expression105"):
                opp_val = getattr(old_value, "vhdl_Expression105", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_Expression105", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_Expression105"):
                opp_val = getattr(value, "vhdl_Expression105", None)
                setattr(value, "vhdl_Expression105", self)

    @property
    def vhdl_Expression83(self):
        return self.__vhdl_Expression83

    @vhdl_Expression83.setter
    def vhdl_Expression83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_Expression__vhdl_Expression83", None)
        self.__vhdl_Expression83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_PortMapAssociation82"):
                opp_val = getattr(old_value, "vhdl_PortMapAssociation82", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_PortMapAssociation82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_PortMapAssociation82"):
                opp_val = getattr(value, "vhdl_PortMapAssociation82", None)
                setattr(value, "vhdl_PortMapAssociation82", self)

    @property
    def vhdl_Expression59(self):
        return self.__vhdl_Expression59

    @vhdl_Expression59.setter
    def vhdl_Expression59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_Expression__vhdl_Expression59", None)
        self.__vhdl_Expression59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_AttributeSpecification"):
                opp_val = getattr(old_value, "vhdl_AttributeSpecification", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_AttributeSpecification", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_AttributeSpecification"):
                opp_val = getattr(value, "vhdl_AttributeSpecification", None)
                setattr(value, "vhdl_AttributeSpecification", self)

    @property
    def vhdl_Expression93(self):
        return self.__vhdl_Expression93

    @vhdl_Expression93.setter
    def vhdl_Expression93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_Expression__vhdl_Expression93", None)
        self.__vhdl_Expression93 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_ConditionalSignalAssignmentStatement92"):
                opp_val = getattr(old_value, "vhdl_ConditionalSignalAssignmentStatement92", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_ConditionalSignalAssignmentStatement92"):
                opp_val = getattr(value, "vhdl_ConditionalSignalAssignmentStatement92", None)
                if opp_val is None:
                    setattr(value, "vhdl_ConditionalSignalAssignmentStatement92", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def vhdl_Expression138(self):
        return self.__vhdl_Expression138

    @vhdl_Expression138.setter
    def vhdl_Expression138(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_Expression__vhdl_Expression138", None)
        self.__vhdl_Expression138 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_IfStatementTest137"):
                opp_val = getattr(old_value, "vhdl_IfStatementTest137", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_IfStatementTest137", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_IfStatementTest137"):
                opp_val = getattr(value, "vhdl_IfStatementTest137", None)
                setattr(value, "vhdl_IfStatementTest137", self)

    @property
    def vhdl_Expression223(self):
        return self.__vhdl_Expression223

    @vhdl_Expression223.setter
    def vhdl_Expression223(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_Expression__vhdl_Expression223", None)
        self.__vhdl_Expression223 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_AddingExpression222"):
                opp_val = getattr(old_value, "vhdl_AddingExpression222", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_AddingExpression222", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_AddingExpression222"):
                opp_val = getattr(value, "vhdl_AddingExpression222", None)
                setattr(value, "vhdl_AddingExpression222", self)

    @property
    def vhdl_Expression205(self):
        return self.__vhdl_Expression205

    @vhdl_Expression205.setter
    def vhdl_Expression205(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_Expression__vhdl_Expression205", None)
        self.__vhdl_Expression205 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_RelationalExpression"):
                opp_val = getattr(old_value, "vhdl_RelationalExpression", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_RelationalExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_RelationalExpression"):
                opp_val = getattr(value, "vhdl_RelationalExpression", None)
                setattr(value, "vhdl_RelationalExpression", self)

    @property
    def vhdl_Expression109(self):
        return self.__vhdl_Expression109

    @vhdl_Expression109.setter
    def vhdl_Expression109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_Expression__vhdl_Expression109", None)
        self.__vhdl_Expression109 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_ForGenerateStatement108"):
                opp_val = getattr(old_value, "vhdl_ForGenerateStatement108", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_ForGenerateStatement108", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_ForGenerateStatement108"):
                opp_val = getattr(value, "vhdl_ForGenerateStatement108", None)
                setattr(value, "vhdl_ForGenerateStatement108", self)

    @property
    def vhdl_Expression228(self):
        return self.__vhdl_Expression228

    @vhdl_Expression228.setter
    def vhdl_Expression228(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_Expression__vhdl_Expression228", None)
        self.__vhdl_Expression228 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_MultiplyingExpression227"):
                opp_val = getattr(old_value, "vhdl_MultiplyingExpression227", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_MultiplyingExpression227", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_MultiplyingExpression227"):
                opp_val = getattr(value, "vhdl_MultiplyingExpression227", None)
                setattr(value, "vhdl_MultiplyingExpression227", self)

    @property
    def vhdl_Expression166(self):
        return self.__vhdl_Expression166

    @vhdl_Expression166.setter
    def vhdl_Expression166(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_Expression__vhdl_Expression166", None)
        self.__vhdl_Expression166 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_WhileIterationScheme"):
                opp_val = getattr(old_value, "vhdl_WhileIterationScheme", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_WhileIterationScheme", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_WhileIterationScheme"):
                opp_val = getattr(value, "vhdl_WhileIterationScheme", None)
                setattr(value, "vhdl_WhileIterationScheme", self)

    @property
    def vhdl_Expression31(self):
        return self.__vhdl_Expression31

    @vhdl_Expression31.setter
    def vhdl_Expression31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_Expression__vhdl_Expression31", None)
        self.__vhdl_Expression31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_Generic30"):
                opp_val = getattr(old_value, "vhdl_Generic30", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_Generic30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_Generic30"):
                opp_val = getattr(value, "vhdl_Generic30", None)
                setattr(value, "vhdl_Generic30", self)

    @property
    def vhdl_Expression198(self):
        return self.__vhdl_Expression198

    @vhdl_Expression198.setter
    def vhdl_Expression198(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_Expression__vhdl_Expression198", None)
        self.__vhdl_Expression198 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_RangeExpression197"):
                opp_val = getattr(old_value, "vhdl_RangeExpression197", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_RangeExpression197", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_RangeExpression197"):
                opp_val = getattr(value, "vhdl_RangeExpression197", None)
                setattr(value, "vhdl_RangeExpression197", self)

    @property
    def vhdl_Expression193(self):
        return self.__vhdl_Expression193

    @vhdl_Expression193.setter
    def vhdl_Expression193(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_Expression__vhdl_Expression193", None)
        self.__vhdl_Expression193 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_ConditionalWaveformExpression"):
                opp_val = getattr(old_value, "vhdl_ConditionalWaveformExpression", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_ConditionalWaveformExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_ConditionalWaveformExpression"):
                opp_val = getattr(value, "vhdl_ConditionalWaveformExpression", None)
                setattr(value, "vhdl_ConditionalWaveformExpression", self)

    @property
    def vhdl_Expression43(self):
        return self.__vhdl_Expression43

    @vhdl_Expression43.setter
    def vhdl_Expression43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_Expression__vhdl_Expression43", None)
        self.__vhdl_Expression43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_SignalDeclaration42"):
                opp_val = getattr(old_value, "vhdl_SignalDeclaration42", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_SignalDeclaration42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_SignalDeclaration42"):
                opp_val = getattr(value, "vhdl_SignalDeclaration42", None)
                setattr(value, "vhdl_SignalDeclaration42", self)

    @property
    def vhdl_Expression243(self):
        return self.__vhdl_Expression243

    @vhdl_Expression243.setter
    def vhdl_Expression243(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_Expression__vhdl_Expression243", None)
        self.__vhdl_Expression243 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_Member242"):
                opp_val = getattr(old_value, "vhdl_Member242", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_Member242"):
                opp_val = getattr(value, "vhdl_Member242", None)
                if opp_val is None:
                    setattr(value, "vhdl_Member242", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def vhdl_Expression57(self):
        return self.__vhdl_Expression57

    @vhdl_Expression57.setter
    def vhdl_Expression57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_Expression__vhdl_Expression57", None)
        self.__vhdl_Expression57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_ConstantDeclaration56"):
                opp_val = getattr(old_value, "vhdl_ConstantDeclaration56", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_ConstantDeclaration56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_ConstantDeclaration56"):
                opp_val = getattr(value, "vhdl_ConstantDeclaration56", None)
                setattr(value, "vhdl_ConstantDeclaration56", self)

    @property
    def vhdl_Expression235(self):
        return self.__vhdl_Expression235

    @vhdl_Expression235.setter
    def vhdl_Expression235(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_Expression__vhdl_Expression235", None)
        self.__vhdl_Expression235 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_MemberExpression"):
                opp_val = getattr(old_value, "vhdl_MemberExpression", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_MemberExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_MemberExpression"):
                opp_val = getattr(value, "vhdl_MemberExpression", None)
                setattr(value, "vhdl_MemberExpression", self)

    @property
    def vhdl_Expression99(self):
        return self.__vhdl_Expression99

    @vhdl_Expression99.setter
    def vhdl_Expression99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_Expression__vhdl_Expression99", None)
        self.__vhdl_Expression99 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_Expression97"):
                opp_val = getattr(old_value, "vhdl_Expression97", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_Expression97", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_Expression97"):
                opp_val = getattr(value, "vhdl_Expression97", None)
                setattr(value, "vhdl_Expression97", self)

    @property
    def vhdl_Expression164(self):
        return self.__vhdl_Expression164

    @vhdl_Expression164.setter
    def vhdl_Expression164(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_Expression__vhdl_Expression164", None)
        self.__vhdl_Expression164 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_SequentialSignalAssignmentStatement163"):
                opp_val = getattr(old_value, "vhdl_SequentialSignalAssignmentStatement163", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_SequentialSignalAssignmentStatement163", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_SequentialSignalAssignmentStatement163"):
                opp_val = getattr(value, "vhdl_SequentialSignalAssignmentStatement163", None)
                setattr(value, "vhdl_SequentialSignalAssignmentStatement163", self)

    @property
    def vhdl_Expression36(self):
        return self.__vhdl_Expression36

    @vhdl_Expression36.setter
    def vhdl_Expression36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_Expression__vhdl_Expression36", None)
        self.__vhdl_Expression36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_Alias35"):
                opp_val = getattr(old_value, "vhdl_Alias35", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_Alias35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_Alias35"):
                opp_val = getattr(value, "vhdl_Alias35", None)
                setattr(value, "vhdl_Alias35", self)

    @property
    def vhdl_Expression203(self):
        return self.__vhdl_Expression203

    @vhdl_Expression203.setter
    def vhdl_Expression203(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_Expression__vhdl_Expression203", None)
        self.__vhdl_Expression203 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_LogicalExpression202"):
                opp_val = getattr(old_value, "vhdl_LogicalExpression202", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_LogicalExpression202", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_LogicalExpression202"):
                opp_val = getattr(value, "vhdl_LogicalExpression202", None)
                setattr(value, "vhdl_LogicalExpression202", self)

    @property
    def vhdl_Expression88(self):
        return self.__vhdl_Expression88

    @vhdl_Expression88.setter
    def vhdl_Expression88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_Expression__vhdl_Expression88", None)
        self.__vhdl_Expression88 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_GenericMapAssociation87"):
                opp_val = getattr(old_value, "vhdl_GenericMapAssociation87", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_GenericMapAssociation87", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_GenericMapAssociation87"):
                opp_val = getattr(value, "vhdl_GenericMapAssociation87", None)
                setattr(value, "vhdl_GenericMapAssociation87", self)

    @property
    def vhdl_Expression143(self):
        return self.__vhdl_Expression143

    @vhdl_Expression143.setter
    def vhdl_Expression143(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_Expression__vhdl_Expression143", None)
        self.__vhdl_Expression143 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_CaseStatement"):
                opp_val = getattr(old_value, "vhdl_CaseStatement", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_CaseStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_CaseStatement"):
                opp_val = getattr(value, "vhdl_CaseStatement", None)
                setattr(value, "vhdl_CaseStatement", self)

    @property
    def vhdl_Expression90(self):
        return self.__vhdl_Expression90

    @vhdl_Expression90.setter
    def vhdl_Expression90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_Expression__vhdl_Expression90", None)
        self.__vhdl_Expression90 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_ConditionalSignalAssignmentStatement"):
                opp_val = getattr(old_value, "vhdl_ConditionalSignalAssignmentStatement", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_ConditionalSignalAssignmentStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_ConditionalSignalAssignmentStatement"):
                opp_val = getattr(value, "vhdl_ConditionalSignalAssignmentStatement", None)
                setattr(value, "vhdl_ConditionalSignalAssignmentStatement", self)

    @property
    def vhdl_Expression128(self):
        return self.__vhdl_Expression128

    @vhdl_Expression128.setter
    def vhdl_Expression128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_Expression__vhdl_Expression128", None)
        self.__vhdl_Expression128 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_WaitStatement127"):
                opp_val = getattr(old_value, "vhdl_WaitStatement127", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_WaitStatement127", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_WaitStatement127"):
                opp_val = getattr(value, "vhdl_WaitStatement127", None)
                setattr(value, "vhdl_WaitStatement127", self)

    @property
    def vhdl_Expression248(self):
        return self.__vhdl_Expression248

    @vhdl_Expression248.setter
    def vhdl_Expression248(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_Expression__vhdl_Expression248", None)
        self.__vhdl_Expression248 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_SliceExpression247"):
                opp_val = getattr(old_value, "vhdl_SliceExpression247", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_SliceExpression247"):
                opp_val = getattr(value, "vhdl_SliceExpression247", None)
                if opp_val is None:
                    setattr(value, "vhdl_SliceExpression247", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def vhdl_Expression117(self):
        return self.__vhdl_Expression117

    @vhdl_Expression117.setter
    def vhdl_Expression117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_Expression__vhdl_Expression117", None)
        self.__vhdl_Expression117 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_IfGenerateStatement"):
                opp_val = getattr(old_value, "vhdl_IfGenerateStatement", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_IfGenerateStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_IfGenerateStatement"):
                opp_val = getattr(value, "vhdl_IfGenerateStatement", None)
                setattr(value, "vhdl_IfGenerateStatement", self)

    @property
    def vhdl_Expression238(self):
        return self.__vhdl_Expression238

    @vhdl_Expression238.setter
    def vhdl_Expression238(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_Expression__vhdl_Expression238", None)
        self.__vhdl_Expression238 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_MemberExpression237"):
                opp_val = getattr(old_value, "vhdl_MemberExpression237", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_MemberExpression237", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_MemberExpression237"):
                opp_val = getattr(value, "vhdl_MemberExpression237", None)
                setattr(value, "vhdl_MemberExpression237", self)

    @property
    def vhdl_Expression208(self):
        return self.__vhdl_Expression208

    @vhdl_Expression208.setter
    def vhdl_Expression208(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_Expression__vhdl_Expression208", None)
        self.__vhdl_Expression208 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_RelationalExpression207"):
                opp_val = getattr(old_value, "vhdl_RelationalExpression207", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_RelationalExpression207", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_RelationalExpression207"):
                opp_val = getattr(value, "vhdl_RelationalExpression207", None)
                setattr(value, "vhdl_RelationalExpression207", self)

    @property
    def vhdl_Expression220(self):
        return self.__vhdl_Expression220

    @vhdl_Expression220.setter
    def vhdl_Expression220(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_Expression__vhdl_Expression220", None)
        self.__vhdl_Expression220 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_AddingExpression"):
                opp_val = getattr(old_value, "vhdl_AddingExpression", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_AddingExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_AddingExpression"):
                opp_val = getattr(value, "vhdl_AddingExpression", None)
                setattr(value, "vhdl_AddingExpression", self)

    @property
    def vhdl_Expression173(self):
        return self.__vhdl_Expression173

    @vhdl_Expression173.setter
    def vhdl_Expression173(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_Expression__vhdl_Expression173", None)
        self.__vhdl_Expression173 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_SubtypeIndication172"):
                opp_val = getattr(old_value, "vhdl_SubtypeIndication172", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_SubtypeIndication172", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_SubtypeIndication172"):
                opp_val = getattr(value, "vhdl_SubtypeIndication172", None)
                setattr(value, "vhdl_SubtypeIndication172", self)

    @property
    def vhdl_Expression215(self):
        return self.__vhdl_Expression215

    @vhdl_Expression215.setter
    def vhdl_Expression215(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_Expression__vhdl_Expression215", None)
        self.__vhdl_Expression215 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_ShiftExpression"):
                opp_val = getattr(old_value, "vhdl_ShiftExpression", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_ShiftExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_ShiftExpression"):
                opp_val = getattr(value, "vhdl_ShiftExpression", None)
                setattr(value, "vhdl_ShiftExpression", self)

    @property
    def vhdl_Expression96(self):
        return self.__vhdl_Expression96

    @vhdl_Expression96.setter
    def vhdl_Expression96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_Expression__vhdl_Expression96", None)
        self.__vhdl_Expression96 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_Expression94"):
                opp_val = getattr(old_value, "vhdl_Expression94", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_Expression94"):
                opp_val = getattr(value, "vhdl_Expression94", None)
                if opp_val is None:
                    setattr(value, "vhdl_Expression94", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def vhdl_Expression100(self):
        return self.__vhdl_Expression100

    @vhdl_Expression100.setter
    def vhdl_Expression100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_Expression__vhdl_Expression100", None)
        self.__vhdl_Expression100 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_Expression102"):
                opp_val = getattr(old_value, "vhdl_Expression102", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_Expression102", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_Expression102"):
                opp_val = getattr(value, "vhdl_Expression102", None)
                setattr(value, "vhdl_Expression102", self)

    @property
    def vhdl_Expression218(self):
        return self.__vhdl_Expression218

    @vhdl_Expression218.setter
    def vhdl_Expression218(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_Expression__vhdl_Expression218", None)
        self.__vhdl_Expression218 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_ShiftExpression217"):
                opp_val = getattr(old_value, "vhdl_ShiftExpression217", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_ShiftExpression217", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_ShiftExpression217"):
                opp_val = getattr(value, "vhdl_ShiftExpression217", None)
                setattr(value, "vhdl_ShiftExpression217", self)

    @property
    def vhdl_Expression195(self):
        return self.__vhdl_Expression195

    @vhdl_Expression195.setter
    def vhdl_Expression195(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_Expression__vhdl_Expression195", None)
        self.__vhdl_Expression195 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_RangeExpression"):
                opp_val = getattr(old_value, "vhdl_RangeExpression", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_RangeExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_RangeExpression"):
                opp_val = getattr(value, "vhdl_RangeExpression", None)
                setattr(value, "vhdl_RangeExpression", self)

    @property
    def vhdl_Expression131(self):
        return self.__vhdl_Expression131

    @vhdl_Expression131.setter
    def vhdl_Expression131(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_Expression__vhdl_Expression131", None)
        self.__vhdl_Expression131 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_WaitStatement130"):
                opp_val = getattr(old_value, "vhdl_WaitStatement130", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_WaitStatement130", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_WaitStatement130"):
                opp_val = getattr(value, "vhdl_WaitStatement130", None)
                setattr(value, "vhdl_WaitStatement130", self)

    @property
    def vhdl_Expression245(self):
        return self.__vhdl_Expression245

    @vhdl_Expression245.setter
    def vhdl_Expression245(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_Expression__vhdl_Expression245", None)
        self.__vhdl_Expression245 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_SliceExpression"):
                opp_val = getattr(old_value, "vhdl_SliceExpression", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_SliceExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_SliceExpression"):
                opp_val = getattr(value, "vhdl_SliceExpression", None)
                setattr(value, "vhdl_SliceExpression", self)

    @property
    def vhdl_Expression225(self):
        return self.__vhdl_Expression225

    @vhdl_Expression225.setter
    def vhdl_Expression225(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_Expression__vhdl_Expression225", None)
        self.__vhdl_Expression225 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_MultiplyingExpression"):
                opp_val = getattr(old_value, "vhdl_MultiplyingExpression", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_MultiplyingExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_MultiplyingExpression"):
                opp_val = getattr(value, "vhdl_MultiplyingExpression", None)
                setattr(value, "vhdl_MultiplyingExpression", self)

    @property
    def vhdl_Expression97(self):
        return self.__vhdl_Expression97

    @vhdl_Expression97.setter
    def vhdl_Expression97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_Expression__vhdl_Expression97", None)
        self.__vhdl_Expression97 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_Expression99"):
                opp_val = getattr(old_value, "vhdl_Expression99", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_Expression99", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_Expression99"):
                opp_val = getattr(value, "vhdl_Expression99", None)
                setattr(value, "vhdl_Expression99", self)

    @property
    def vhdl_Expression213(self):
        return self.__vhdl_Expression213

    @vhdl_Expression213.setter
    def vhdl_Expression213(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_Expression__vhdl_Expression213", None)
        self.__vhdl_Expression213 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_ChoiceExpression212"):
                opp_val = getattr(old_value, "vhdl_ChoiceExpression212", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_ChoiceExpression212", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_ChoiceExpression212"):
                opp_val = getattr(value, "vhdl_ChoiceExpression212", None)
                setattr(value, "vhdl_ChoiceExpression212", self)

    @property
    def vhdl_Expression94(self):
        return self.__vhdl_Expression94

    @vhdl_Expression94.setter
    def vhdl_Expression94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_Expression__vhdl_Expression94", None)
        self.__vhdl_Expression94 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "vhdl_Expression96"):
                    opp_val = getattr(item, "vhdl_Expression96", None)
                    
                    if opp_val == self:
                        setattr(item, "vhdl_Expression96", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "vhdl_Expression96"):
                    opp_val = getattr(item, "vhdl_Expression96", None)
                    
                    setattr(item, "vhdl_Expression96", self)
                    

    @property
    def vhdl_Expression200(self):
        return self.__vhdl_Expression200

    @vhdl_Expression200.setter
    def vhdl_Expression200(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_Expression__vhdl_Expression200", None)
        self.__vhdl_Expression200 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_LogicalExpression"):
                opp_val = getattr(old_value, "vhdl_LogicalExpression", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_LogicalExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_LogicalExpression"):
                opp_val = getattr(value, "vhdl_LogicalExpression", None)
                setattr(value, "vhdl_LogicalExpression", self)

    @property
    def vhdl_Expression148(self):
        return self.__vhdl_Expression148

    @vhdl_Expression148.setter
    def vhdl_Expression148(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_Expression__vhdl_Expression148", None)
        self.__vhdl_Expression148 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_CaseAlternative147"):
                opp_val = getattr(old_value, "vhdl_CaseAlternative147", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_CaseAlternative147", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_CaseAlternative147"):
                opp_val = getattr(value, "vhdl_CaseAlternative147", None)
                setattr(value, "vhdl_CaseAlternative147", self)

    @property
    def vhdl_Expression182(self):
        return self.__vhdl_Expression182

    @vhdl_Expression182.setter
    def vhdl_Expression182(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_Expression__vhdl_Expression182", None)
        self.__vhdl_Expression182 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_ConstrainedArrayTypeDefinition"):
                opp_val = getattr(old_value, "vhdl_ConstrainedArrayTypeDefinition", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_ConstrainedArrayTypeDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_ConstrainedArrayTypeDefinition"):
                opp_val = getattr(value, "vhdl_ConstrainedArrayTypeDefinition", None)
                setattr(value, "vhdl_ConstrainedArrayTypeDefinition", self)

class vhdl_SubtypeIndication:

    def __init__(self, builtin_type: str, vhdl_SubtypeIndication: "vhdl_Port" = None, vhdl_SubtypeIndication28: "vhdl_Generic" = None, vhdl_SubtypeIndication33: "vhdl_Alias" = None, vhdl_SubtypeIndication40: "vhdl_SignalDeclaration" = None, vhdl_SubtypeIndication47: "vhdl_VariableDeclaration" = None, vhdl_SubtypeIndication54: "vhdl_ConstantDeclaration" = None, vhdl_SubtypeIndication170: "vhdl_Type" = None, vhdl_SubtypeIndication175: "vhdl_SubtypeDeclaration" = None, vhdl_SubtypeIndication178: "vhdl_AccessTypeDefinition" = None, vhdl_SubtypeIndication180: "vhdl_ArrayTypeDefinition" = None, vhdl_SubtypeIndication172: "vhdl_Expression" = None, vhdl_SubtypeIndication186: "vhdl_RecordTypeDefinition" = None):
        self.builtin_type = builtin_type
        self.vhdl_SubtypeIndication = vhdl_SubtypeIndication
        self.vhdl_SubtypeIndication28 = vhdl_SubtypeIndication28
        self.vhdl_SubtypeIndication33 = vhdl_SubtypeIndication33
        self.vhdl_SubtypeIndication40 = vhdl_SubtypeIndication40
        self.vhdl_SubtypeIndication47 = vhdl_SubtypeIndication47
        self.vhdl_SubtypeIndication54 = vhdl_SubtypeIndication54
        self.vhdl_SubtypeIndication170 = vhdl_SubtypeIndication170
        self.vhdl_SubtypeIndication175 = vhdl_SubtypeIndication175
        self.vhdl_SubtypeIndication178 = vhdl_SubtypeIndication178
        self.vhdl_SubtypeIndication180 = vhdl_SubtypeIndication180
        self.vhdl_SubtypeIndication172 = vhdl_SubtypeIndication172
        self.vhdl_SubtypeIndication186 = vhdl_SubtypeIndication186
        
    @property
    def builtin_type(self) -> str:
        return self.__builtin_type

    @builtin_type.setter
    def builtin_type(self, builtin_type: str):
        self.__builtin_type = builtin_type

    @property
    def vhdl_SubtypeIndication186(self):
        return self.__vhdl_SubtypeIndication186

    @vhdl_SubtypeIndication186.setter
    def vhdl_SubtypeIndication186(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_SubtypeIndication__vhdl_SubtypeIndication186", None)
        self.__vhdl_SubtypeIndication186 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_RecordTypeDefinition185"):
                opp_val = getattr(old_value, "vhdl_RecordTypeDefinition185", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_RecordTypeDefinition185"):
                opp_val = getattr(value, "vhdl_RecordTypeDefinition185", None)
                if opp_val is None:
                    setattr(value, "vhdl_RecordTypeDefinition185", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def vhdl_SubtypeIndication178(self):
        return self.__vhdl_SubtypeIndication178

    @vhdl_SubtypeIndication178.setter
    def vhdl_SubtypeIndication178(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_SubtypeIndication__vhdl_SubtypeIndication178", None)
        self.__vhdl_SubtypeIndication178 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_AccessTypeDefinition"):
                opp_val = getattr(old_value, "vhdl_AccessTypeDefinition", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_AccessTypeDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_AccessTypeDefinition"):
                opp_val = getattr(value, "vhdl_AccessTypeDefinition", None)
                setattr(value, "vhdl_AccessTypeDefinition", self)

    @property
    def vhdl_SubtypeIndication170(self):
        return self.__vhdl_SubtypeIndication170

    @vhdl_SubtypeIndication170.setter
    def vhdl_SubtypeIndication170(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_SubtypeIndication__vhdl_SubtypeIndication170", None)
        self.__vhdl_SubtypeIndication170 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_Type"):
                opp_val = getattr(old_value, "vhdl_Type", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_Type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_Type"):
                opp_val = getattr(value, "vhdl_Type", None)
                setattr(value, "vhdl_Type", self)

    @property
    def vhdl_SubtypeIndication33(self):
        return self.__vhdl_SubtypeIndication33

    @vhdl_SubtypeIndication33.setter
    def vhdl_SubtypeIndication33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_SubtypeIndication__vhdl_SubtypeIndication33", None)
        self.__vhdl_SubtypeIndication33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_Alias"):
                opp_val = getattr(old_value, "vhdl_Alias", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_Alias", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_Alias"):
                opp_val = getattr(value, "vhdl_Alias", None)
                setattr(value, "vhdl_Alias", self)

    @property
    def vhdl_SubtypeIndication180(self):
        return self.__vhdl_SubtypeIndication180

    @vhdl_SubtypeIndication180.setter
    def vhdl_SubtypeIndication180(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_SubtypeIndication__vhdl_SubtypeIndication180", None)
        self.__vhdl_SubtypeIndication180 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_ArrayTypeDefinition"):
                opp_val = getattr(old_value, "vhdl_ArrayTypeDefinition", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_ArrayTypeDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_ArrayTypeDefinition"):
                opp_val = getattr(value, "vhdl_ArrayTypeDefinition", None)
                setattr(value, "vhdl_ArrayTypeDefinition", self)

    @property
    def vhdl_SubtypeIndication40(self):
        return self.__vhdl_SubtypeIndication40

    @vhdl_SubtypeIndication40.setter
    def vhdl_SubtypeIndication40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_SubtypeIndication__vhdl_SubtypeIndication40", None)
        self.__vhdl_SubtypeIndication40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_SignalDeclaration39"):
                opp_val = getattr(old_value, "vhdl_SignalDeclaration39", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_SignalDeclaration39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_SignalDeclaration39"):
                opp_val = getattr(value, "vhdl_SignalDeclaration39", None)
                setattr(value, "vhdl_SignalDeclaration39", self)

    @property
    def vhdl_SubtypeIndication(self):
        return self.__vhdl_SubtypeIndication

    @vhdl_SubtypeIndication.setter
    def vhdl_SubtypeIndication(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_SubtypeIndication__vhdl_SubtypeIndication", None)
        self.__vhdl_SubtypeIndication = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_Port21"):
                opp_val = getattr(old_value, "vhdl_Port21", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_Port21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_Port21"):
                opp_val = getattr(value, "vhdl_Port21", None)
                setattr(value, "vhdl_Port21", self)

    @property
    def vhdl_SubtypeIndication47(self):
        return self.__vhdl_SubtypeIndication47

    @vhdl_SubtypeIndication47.setter
    def vhdl_SubtypeIndication47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_SubtypeIndication__vhdl_SubtypeIndication47", None)
        self.__vhdl_SubtypeIndication47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_VariableDeclaration46"):
                opp_val = getattr(old_value, "vhdl_VariableDeclaration46", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_VariableDeclaration46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_VariableDeclaration46"):
                opp_val = getattr(value, "vhdl_VariableDeclaration46", None)
                setattr(value, "vhdl_VariableDeclaration46", self)

    @property
    def vhdl_SubtypeIndication54(self):
        return self.__vhdl_SubtypeIndication54

    @vhdl_SubtypeIndication54.setter
    def vhdl_SubtypeIndication54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_SubtypeIndication__vhdl_SubtypeIndication54", None)
        self.__vhdl_SubtypeIndication54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_ConstantDeclaration53"):
                opp_val = getattr(old_value, "vhdl_ConstantDeclaration53", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_ConstantDeclaration53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_ConstantDeclaration53"):
                opp_val = getattr(value, "vhdl_ConstantDeclaration53", None)
                setattr(value, "vhdl_ConstantDeclaration53", self)

    @property
    def vhdl_SubtypeIndication172(self):
        return self.__vhdl_SubtypeIndication172

    @vhdl_SubtypeIndication172.setter
    def vhdl_SubtypeIndication172(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_SubtypeIndication__vhdl_SubtypeIndication172", None)
        self.__vhdl_SubtypeIndication172 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_Expression173"):
                opp_val = getattr(old_value, "vhdl_Expression173", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_Expression173", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_Expression173"):
                opp_val = getattr(value, "vhdl_Expression173", None)
                setattr(value, "vhdl_Expression173", self)

    @property
    def vhdl_SubtypeIndication28(self):
        return self.__vhdl_SubtypeIndication28

    @vhdl_SubtypeIndication28.setter
    def vhdl_SubtypeIndication28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_SubtypeIndication__vhdl_SubtypeIndication28", None)
        self.__vhdl_SubtypeIndication28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_Generic27"):
                opp_val = getattr(old_value, "vhdl_Generic27", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_Generic27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_Generic27"):
                opp_val = getattr(value, "vhdl_Generic27", None)
                setattr(value, "vhdl_Generic27", self)

    @property
    def vhdl_SubtypeIndication175(self):
        return self.__vhdl_SubtypeIndication175

    @vhdl_SubtypeIndication175.setter
    def vhdl_SubtypeIndication175(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_SubtypeIndication__vhdl_SubtypeIndication175", None)
        self.__vhdl_SubtypeIndication175 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_SubtypeDeclaration"):
                opp_val = getattr(old_value, "vhdl_SubtypeDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_SubtypeDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_SubtypeDeclaration"):
                opp_val = getattr(value, "vhdl_SubtypeDeclaration", None)
                setattr(value, "vhdl_SubtypeDeclaration", self)

class Variable:

    pass
class vhdl_LoopVariable(Variable):

    pass
class vhdl_Alias(Variable, BlockDeclarativeItem):

    pass
class vhdl_Constant(Variable):

    pass
class vhdl_Var(Variable):

    pass
class vhdl_Signal(Variable):

    pass
class vhdl_Generic(Variable):

    pass
class vhdl_Port(Variable):

    def __init__(self, mode: str, kind: str, vhdl_Port: "vhdl_Ports" = None, vhdl_Port21: "vhdl_SubtypeIndication" = None, vhdl_Port23: "vhdl_Expression" = None):
        self.mode = mode
        self.kind = kind
        self.vhdl_Port = vhdl_Port
        self.vhdl_Port21 = vhdl_Port21
        self.vhdl_Port23 = vhdl_Port23
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def mode(self) -> str:
        return self.__mode

    @mode.setter
    def mode(self, mode: str):
        self.__mode = mode

    @property
    def vhdl_Port21(self):
        return self.__vhdl_Port21

    @vhdl_Port21.setter
    def vhdl_Port21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_Port__vhdl_Port21", None)
        self.__vhdl_Port21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_SubtypeIndication"):
                opp_val = getattr(old_value, "vhdl_SubtypeIndication", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_SubtypeIndication", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_SubtypeIndication"):
                opp_val = getattr(value, "vhdl_SubtypeIndication", None)
                setattr(value, "vhdl_SubtypeIndication", self)

    @property
    def vhdl_Port23(self):
        return self.__vhdl_Port23

    @vhdl_Port23.setter
    def vhdl_Port23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_Port__vhdl_Port23", None)
        self.__vhdl_Port23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_Expression"):
                opp_val = getattr(old_value, "vhdl_Expression", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_Expression"):
                opp_val = getattr(value, "vhdl_Expression", None)
                setattr(value, "vhdl_Expression", self)

    @property
    def vhdl_Port(self):
        return self.__vhdl_Port

    @vhdl_Port.setter
    def vhdl_Port(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_Port__vhdl_Port", None)
        self.__vhdl_Port = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_Ports19"):
                opp_val = getattr(old_value, "vhdl_Ports19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_Ports19"):
                opp_val = getattr(value, "vhdl_Ports19", None)
                if opp_val is None:
                    setattr(value, "vhdl_Ports19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class vhdl_Ports:

    pass
class vhdl_Generics:

    pass
class vhdl_ArchitectureStatement:

    def __init__(self, label: str, vhdl_ArchitectureStatement: "vhdl_Architecture" = None, vhdl_ArchitectureStatement115: "vhdl_ForGenerateStatement" = None, vhdl_ArchitectureStatement123: "vhdl_IfGenerateStatement" = None):
        self.label = label
        self.vhdl_ArchitectureStatement = vhdl_ArchitectureStatement
        self.vhdl_ArchitectureStatement115 = vhdl_ArchitectureStatement115
        self.vhdl_ArchitectureStatement123 = vhdl_ArchitectureStatement123
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def vhdl_ArchitectureStatement115(self):
        return self.__vhdl_ArchitectureStatement115

    @vhdl_ArchitectureStatement115.setter
    def vhdl_ArchitectureStatement115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_ArchitectureStatement__vhdl_ArchitectureStatement115", None)
        self.__vhdl_ArchitectureStatement115 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_ForGenerateStatement114"):
                opp_val = getattr(old_value, "vhdl_ForGenerateStatement114", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_ForGenerateStatement114"):
                opp_val = getattr(value, "vhdl_ForGenerateStatement114", None)
                if opp_val is None:
                    setattr(value, "vhdl_ForGenerateStatement114", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def vhdl_ArchitectureStatement123(self):
        return self.__vhdl_ArchitectureStatement123

    @vhdl_ArchitectureStatement123.setter
    def vhdl_ArchitectureStatement123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_ArchitectureStatement__vhdl_ArchitectureStatement123", None)
        self.__vhdl_ArchitectureStatement123 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_IfGenerateStatement122"):
                opp_val = getattr(old_value, "vhdl_IfGenerateStatement122", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_IfGenerateStatement122"):
                opp_val = getattr(value, "vhdl_IfGenerateStatement122", None)
                if opp_val is None:
                    setattr(value, "vhdl_IfGenerateStatement122", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def vhdl_ArchitectureStatement(self):
        return self.__vhdl_ArchitectureStatement

    @vhdl_ArchitectureStatement.setter
    def vhdl_ArchitectureStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_ArchitectureStatement__vhdl_ArchitectureStatement", None)
        self.__vhdl_ArchitectureStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_Architecture13"):
                opp_val = getattr(old_value, "vhdl_Architecture13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_Architecture13"):
                opp_val = getattr(value, "vhdl_Architecture13", None)
                if opp_val is None:
                    setattr(value, "vhdl_Architecture13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class vhdl_BlockDeclarativeItem:

    pass
class vhdl_package_declarative_part:

    pass
class vhdl_package_declarative_item:

    pass
class LibraryUnit:

    pass
class vhdl_Entity(LibraryUnit):

    pass
class vhdl_Architecture(LibraryUnit):

    pass
class vhdl_Package(LibraryUnit):

    pass
class vhdl_Library:

    def __init__(self, builtin_lib: str, vhdl_Library: "vhdl_UseClause" = None, vhdl_Library5: "vhdl_LibraryClause" = None, vhdl_Library72: "vhdl_EntityInstantiationStatement" = None):
        self.builtin_lib = builtin_lib
        self.vhdl_Library = vhdl_Library
        self.vhdl_Library5 = vhdl_Library5
        self.vhdl_Library72 = vhdl_Library72
        
    @property
    def builtin_lib(self) -> str:
        return self.__builtin_lib

    @builtin_lib.setter
    def builtin_lib(self, builtin_lib: str):
        self.__builtin_lib = builtin_lib

    @property
    def vhdl_Library72(self):
        return self.__vhdl_Library72

    @vhdl_Library72.setter
    def vhdl_Library72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_Library__vhdl_Library72", None)
        self.__vhdl_Library72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_EntityInstantiationStatement"):
                opp_val = getattr(old_value, "vhdl_EntityInstantiationStatement", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_EntityInstantiationStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_EntityInstantiationStatement"):
                opp_val = getattr(value, "vhdl_EntityInstantiationStatement", None)
                setattr(value, "vhdl_EntityInstantiationStatement", self)

    @property
    def vhdl_Library(self):
        return self.__vhdl_Library

    @vhdl_Library.setter
    def vhdl_Library(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_Library__vhdl_Library", None)
        self.__vhdl_Library = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_UseClause"):
                opp_val = getattr(old_value, "vhdl_UseClause", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_UseClause", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_UseClause"):
                opp_val = getattr(value, "vhdl_UseClause", None)
                setattr(value, "vhdl_UseClause", self)

    @property
    def vhdl_Library5(self):
        return self.__vhdl_Library5

    @vhdl_Library5.setter
    def vhdl_Library5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_Library__vhdl_Library5", None)
        self.__vhdl_Library5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_LibraryClause"):
                opp_val = getattr(old_value, "vhdl_LibraryClause", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_LibraryClause", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_LibraryClause"):
                opp_val = getattr(value, "vhdl_LibraryClause", None)
                setattr(value, "vhdl_LibraryClause", self)

class ContextItem:

    pass
class vhdl_LibraryClause(ContextItem):

    def __init__(self, name: str, vhdl_LibraryClause: "vhdl_Library" = None):
        self.name = name
        self.vhdl_LibraryClause = vhdl_LibraryClause
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def vhdl_LibraryClause(self):
        return self.__vhdl_LibraryClause

    @vhdl_LibraryClause.setter
    def vhdl_LibraryClause(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_LibraryClause__vhdl_LibraryClause", None)
        self.__vhdl_LibraryClause = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_Library5"):
                opp_val = getattr(old_value, "vhdl_Library5", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_Library5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_Library5"):
                opp_val = getattr(value, "vhdl_Library5", None)
                setattr(value, "vhdl_Library5", self)

class vhdl_UseClause(ContextItem):

    def __init__(self, importedNamespace: str, vhdl_UseClause: "vhdl_Library" = None):
        self.importedNamespace = importedNamespace
        self.vhdl_UseClause = vhdl_UseClause
        
    @property
    def importedNamespace(self) -> str:
        return self.__importedNamespace

    @importedNamespace.setter
    def importedNamespace(self, importedNamespace: str):
        self.__importedNamespace = importedNamespace

    @property
    def vhdl_UseClause(self):
        return self.__vhdl_UseClause

    @vhdl_UseClause.setter
    def vhdl_UseClause(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_UseClause__vhdl_UseClause", None)
        self.__vhdl_UseClause = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_Library"):
                opp_val = getattr(old_value, "vhdl_Library", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_Library", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_Library"):
                opp_val = getattr(value, "vhdl_Library", None)
                setattr(value, "vhdl_Library", self)

class vhdl_LibraryUnit:

    def __init__(self, name: str, vhdl_LibraryUnit: "vhdl_DesignFile" = None):
        self.name = name
        self.vhdl_LibraryUnit = vhdl_LibraryUnit
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def vhdl_LibraryUnit(self):
        return self.__vhdl_LibraryUnit

    @vhdl_LibraryUnit.setter
    def vhdl_LibraryUnit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_LibraryUnit__vhdl_LibraryUnit", None)
        self.__vhdl_LibraryUnit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_DesignFile2"):
                opp_val = getattr(old_value, "vhdl_DesignFile2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_DesignFile2"):
                opp_val = getattr(value, "vhdl_DesignFile2", None)
                if opp_val is None:
                    setattr(value, "vhdl_DesignFile2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class vhdl_ContextItem:

    pass
class vhdl_DesignFile:

    pass