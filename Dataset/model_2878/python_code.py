from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class SignalKind(Enum):
    REGISTER = "REGISTER"
    BUS = "BUS"
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
class LogicalOperator(Enum):
    AND = "AND"
    OR = "OR"
    NAND = "NAND"
    NOR = "NOR"
    XOR = "XOR"
    XNOR = "XNOR"
class RelationalOperator(Enum):
    EQ = "EQ"
    NEQ = "NEQ"
    LOWERTHAN = "LOWERTHAN"
    LE = "LE"
    GREATERTHAN = "GREATERTHAN"
    GE = "GE"
class Mode(Enum):
    IN = "IN"
    OUT = "OUT"
    INOUT = "INOUT"
    BUFFER = "BUFFER"
    LINKAGE = "LINKAGE"
class UnaryOperator(Enum):
    ABS = "ABS"
    NOT = "NOT"
class MultiplyingOperator(Enum):
    MUL = "MUL"
    DIV = "DIV"
    MOD = "MOD"
    REM = "REM"
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
class Purity(Enum):
    IMPURE = "IMPURE"
    PURE = "PURE"
class RangeDirection(Enum):
    TO = "TO"
    DOWNTO = "DOWNTO"
class Sign(Enum):
    PLUS = "PLUS"
    MINUS = "MINUS"


############################################
# Definition of Classes
############################################

class Configuration:

    pass
class vhdl_configuration_ConfigurationReference(ABC):

    pass
class configuration_vhdl_EntityReference:

    pass
class BlockConfiguration:

    pass
class configuration_vhdl_PortMaps:

    pass
class configuration_vhdl_GenericMaps:

    pass
class configuration_vhdl_MultiName:

    pass
class ConfigurationItem:

    pass
class vhdl_configuration_ComponentConfiguration(ConfigurationItem):

    pass
class configuration_vhdl_Name:

    pass
class configuration_ConfigurationItem:

    pass
class nature_vhdl_Name:

    pass
class vhdl_nature_Natured(ABC):

    pass
class vhdl_nature_NatureReference(ABC):

    pass
class vhdl_type_PhysicalTypeDefinitionSecondary:

    def __init__(self, number: str, name: str, vhdl_type_PhysicalTypeDefinitionSecondary: "type_vhdl_Name" = None):
        self.number = number
        self.name = name
        self.vhdl_type_PhysicalTypeDefinitionSecondary = vhdl_type_PhysicalTypeDefinitionSecondary
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def number(self) -> str:
        return self.__number

    @number.setter
    def number(self, number: str):
        self.__number = number

    @property
    def vhdl_type_PhysicalTypeDefinitionSecondary(self):
        return self.__vhdl_type_PhysicalTypeDefinitionSecondary

    @vhdl_type_PhysicalTypeDefinitionSecondary.setter
    def vhdl_type_PhysicalTypeDefinitionSecondary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_type_PhysicalTypeDefinitionSecondary__vhdl_type_PhysicalTypeDefinitionSecondary", None)
        self.__vhdl_type_PhysicalTypeDefinitionSecondary = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "type_vhdl_Name"):
                opp_val = getattr(old_value, "type_vhdl_Name", None)
                if opp_val == self:
                    setattr(old_value, "type_vhdl_Name", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "type_vhdl_Name"):
                opp_val = getattr(value, "type_vhdl_Name", None)
                setattr(value, "type_vhdl_Name", self)

class RecordNatureElement:

    pass
class CompositeNatureDefinition:

    pass
class vhdl_nature_RecordNatureDefinition(CompositeNatureDefinition):

    pass
class ArrayNatureDefinition:

    pass
class vhdl_nature_UnconstrainedArrayNatureDefinition(ArrayNatureDefinition):

    pass
class vhdl_nature_ConstrainedArrayNatureDefinition(ArrayNatureDefinition):

    pass
class nature_CompositeNatureDefinition:

    pass
class vhdl_type_TypeReference(ABC):

    pass
class vhdl_type_Typed(ABC):

    pass
class type_vhdl_Name:

    pass
class PhysicalTypeDefinitionSecondary:

    pass
class EnumerationLiteral:

    pass
class vhdl_type_EnumerationLiteral(ABC):

    pass
class ArrayTypeDefinition:

    pass
class vhdl_type_UnconstrainedArrayTypeDefinition(ArrayTypeDefinition):

    pass
class vhdl_type_ConstrainedArrayTypeDefinition(ArrayTypeDefinition):

    pass
class type_CompositeTypeDefinition:

    pass
class RecordTypeElement:

    pass
class CompositeTypeDefinition:

    pass
class vhdl_type_RecordTypeDefinition(CompositeTypeDefinition):

    pass
class type_TypeDefinition:

    pass
class NatureDefinition:

    pass
class vhdl_nature_CompositeNatureDefinition(NatureDefinition):

    pass
class vhdl_nature_ScalarNatureDefinition(NatureDefinition):

    pass
class ValueDeclaration:

    pass
class vhdl_declaration_SignalDeclaration(ValueDeclaration):

    def __init__(self, kind: str, mode: str):
        self.kind = kind
        self.mode = mode
        
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

class vhdl_declaration_VariableDeclaration(ValueDeclaration):

    def __init__(self, shared: bool, mode: str):
        self.shared = shared
        self.mode = mode
        
    @property
    def mode(self) -> str:
        return self.__mode

    @mode.setter
    def mode(self, mode: str):
        self.__mode = mode

    @property
    def shared(self) -> bool:
        return self.__shared

    @shared.setter
    def shared(self, shared: bool):
        self.__shared = shared

class vhdl_declaration_ConstantDeclaration(ValueDeclaration):

    pass
class TypeDefinition:

    pass
class vhdl_type_RangeTypeDefinition(TypeDefinition):

    def __init__(self, direction: str, vhdl_type_RangeTypeDefinition: "Expression" = None, vhdl_type_RangeTypeDefinition309: "Expression" = None, TypeDefinition: "vhdl_declaration_TypeDeclaration"):
        self.direction = direction
        self.vhdl_type_RangeTypeDefinition = vhdl_type_RangeTypeDefinition
        self.vhdl_type_RangeTypeDefinition309 = vhdl_type_RangeTypeDefinition309
        
    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

    @property
    def vhdl_type_RangeTypeDefinition(self):
        return self.__vhdl_type_RangeTypeDefinition

    @vhdl_type_RangeTypeDefinition.setter
    def vhdl_type_RangeTypeDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_type_RangeTypeDefinition__vhdl_type_RangeTypeDefinition", None)
        self.__vhdl_type_RangeTypeDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression307"):
                opp_val = getattr(old_value, "Expression307", None)
                if opp_val == self:
                    setattr(old_value, "Expression307", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression307"):
                opp_val = getattr(value, "Expression307", None)
                setattr(value, "Expression307", self)

    @property
    def vhdl_type_RangeTypeDefinition309(self):
        return self.__vhdl_type_RangeTypeDefinition309

    @vhdl_type_RangeTypeDefinition309.setter
    def vhdl_type_RangeTypeDefinition309(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_type_RangeTypeDefinition__vhdl_type_RangeTypeDefinition309", None)
        self.__vhdl_type_RangeTypeDefinition309 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression310"):
                opp_val = getattr(old_value, "Expression310", None)
                if opp_val == self:
                    setattr(old_value, "Expression310", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression310"):
                opp_val = getattr(value, "Expression310", None)
                setattr(value, "Expression310", self)

class vhdl_type_CompositeTypeDefinition(TypeDefinition):

    pass
class vhdl_type_EnumerationTypeDefinition(TypeDefinition):

    pass
class vhdl_type_PhysicalTypeDefinition(TypeDefinition):

    def __init__(self, primary: str, vhdl_type_PhysicalTypeDefinition: "Expression" = None, vhdl_type_PhysicalTypeDefinition304: set["PhysicalTypeDefinitionSecondary"] = None, TypeDefinition: "vhdl_declaration_TypeDeclaration"):
        self.primary = primary
        self.vhdl_type_PhysicalTypeDefinition = vhdl_type_PhysicalTypeDefinition
        self.vhdl_type_PhysicalTypeDefinition304 = vhdl_type_PhysicalTypeDefinition304 if vhdl_type_PhysicalTypeDefinition304 is not None else set()
        
    @property
    def primary(self) -> str:
        return self.__primary

    @primary.setter
    def primary(self, primary: str):
        self.__primary = primary

    @property
    def vhdl_type_PhysicalTypeDefinition304(self):
        return self.__vhdl_type_PhysicalTypeDefinition304

    @vhdl_type_PhysicalTypeDefinition304.setter
    def vhdl_type_PhysicalTypeDefinition304(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_type_PhysicalTypeDefinition__vhdl_type_PhysicalTypeDefinition304", None)
        self.__vhdl_type_PhysicalTypeDefinition304 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PhysicalTypeDefinitionSecondary"):
                    opp_val = getattr(item, "PhysicalTypeDefinitionSecondary", None)
                    
                    if opp_val == self:
                        setattr(item, "PhysicalTypeDefinitionSecondary", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PhysicalTypeDefinitionSecondary"):
                    opp_val = getattr(item, "PhysicalTypeDefinitionSecondary", None)
                    
                    setattr(item, "PhysicalTypeDefinitionSecondary", self)
                    

    @property
    def vhdl_type_PhysicalTypeDefinition(self):
        return self.__vhdl_type_PhysicalTypeDefinition

    @vhdl_type_PhysicalTypeDefinition.setter
    def vhdl_type_PhysicalTypeDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_type_PhysicalTypeDefinition__vhdl_type_PhysicalTypeDefinition", None)
        self.__vhdl_type_PhysicalTypeDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression302"):
                opp_val = getattr(old_value, "Expression302", None)
                if opp_val == self:
                    setattr(old_value, "Expression302", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression302"):
                opp_val = getattr(value, "Expression302", None)
                setattr(value, "Expression302", self)

class declaration_vhdl_PortMaps:

    pass
class declaration_vhdl_GenericMaps:

    pass
class declaration_vhdl_EntityReference:

    pass
class declaration_vhdl_ComponentReference:

    pass
class SourceAspect:

    pass
class vhdl_ams_Noise(SourceAspect):

    pass
class vhdl_ams_Spectrum(SourceAspect):

    pass
class declaration_SubprogramDeclaration:

    pass
class SubprogramBody:

    pass
class nature_Natured:

    pass
class vhdl_nature_ArrayNatureDefinition(nature_Natured, nature_CompositeNatureDefinition):

    pass
class QuantityAspect:

    pass
class MultiNamed:

    pass
class declaration_QuantityDeclaration:

    pass
class QuantityDeclaration:

    pass
class vhdl_declaration_BranchQuantityDeclaration(QuantityDeclaration):

    pass
class declaration_vhdl_MultiName:

    pass
class declaration_vhdl_Name:

    pass
class AssociationExpression:

    pass
class vhdl_expression_ConditionalWaveformExpression(AssociationExpression):

    pass
class type_EnumerationLiteral:

    pass
class expression_BinaryExpression:

    pass
class NatureReference:

    pass
class expression_vhdl_Name:

    pass
class ValueExpression:

    pass
class vhdl_expression_UnitValueExpression(ValueExpression):

    pass
class vhdl_expression_BitStringExpression(ValueExpression):

    pass
class expression_IndicationExpression:

    pass
class type_Typed:

    pass
class vhdl_declaration_SourceQuantityDeclaration(MultiNamed, type_Typed, declaration_QuantityDeclaration):

    pass
class vhdl_declaration_FunctionDeclaration(type_Typed, declaration_SubprogramDeclaration):

    def __init__(self, purity: str):
        self.purity = purity
        
    @property
    def purity(self) -> str:
        return self.__purity

    @purity.setter
    def purity(self, purity: str):
        self.__purity = purity

class vhdl_type_AccessTypeDefinition(type_Typed, type_TypeDefinition):

    pass
class vhdl_type_FileTypeDefinition(type_Typed, type_TypeDefinition):

    pass
class vhdl_type_ArrayTypeDefinition(type_Typed, type_CompositeTypeDefinition):

    pass
class vhdl_declaration_FreeQuantityDeclaration(MultiNamed, type_Typed, declaration_QuantityDeclaration):

    pass
class expression_Expression:

    pass
class vhdl_expression_AllocatorExpression(type_Typed, expression_Expression):

    pass
class expression_vhdl_Signature:

    pass
class expression_ValueExpression:

    pass
class Name:

    pass
class vhdl_expression_AttributeExpression(expression_ValueExpression, Name):

    pass
class vhdl_expression_OthersExpression(Name, expression_Expression):

    pass
class vhdl_expression_SignatureExpression(Name, expression_Expression):

    pass
class vhdl_expression_NameExpression(Name, expression_Expression):

    pass
class vhdl_expression_TypeQualificationExpression(Name, expression_Expression):

    pass
class vhdl_expression_IdentifierExpression(type_EnumerationLiteral, expression_ValueExpression, Name):

    pass
class vhdl_expression_CharacterExpression(type_EnumerationLiteral, expression_ValueExpression, Name):

    pass
class vhdl_expression_RangeExpression(expression_BinaryExpression, Name):

    def __init__(self, direction: str):
        self.direction = direction
        
    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

class vhdl_expression_StringExpression(expression_ValueExpression, Name):

    pass
class vhdl_expression_AllExpression(Name, expression_Expression):

    pass
class expression_MultiExpression:

    pass
class vhdl_expression_AggregateExpression(expression_MultiExpression, Name):

    pass
class BinaryExpression:

    pass
class vhdl_expression_ShiftExpression(BinaryExpression):

    def __init__(self, operator: str):
        self.operator = operator
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

class vhdl_expression_MultiplyingExpression(BinaryExpression):

    def __init__(self, operator: str):
        self.operator = operator
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

class vhdl_expression_PowerExpression(BinaryExpression):

    pass
class vhdl_expression_LogicalExpression(BinaryExpression):

    def __init__(self, operator: str):
        self.operator = operator
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

class vhdl_expression_RelationalExpression(BinaryExpression):

    def __init__(self, operator: str):
        self.operator = operator
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

class vhdl_expression_AddingExpression(BinaryExpression):

    def __init__(self, operator: str):
        self.operator = operator
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

class IterationScheme:

    pass
class vhdl_statement_ForIterationScheme(IterationScheme):

    def __init__(self, variable: str, vhdl_statement_ForIterationScheme: "Expression" = None, IterationScheme: "vhdl_statement_LoopStatement"):
        self.variable = variable
        self.vhdl_statement_ForIterationScheme = vhdl_statement_ForIterationScheme
        
    @property
    def variable(self) -> str:
        return self.__variable

    @variable.setter
    def variable(self, variable: str):
        self.__variable = variable

    @property
    def vhdl_statement_ForIterationScheme(self):
        return self.__vhdl_statement_ForIterationScheme

    @vhdl_statement_ForIterationScheme.setter
    def vhdl_statement_ForIterationScheme(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_statement_ForIterationScheme__vhdl_statement_ForIterationScheme", None)
        self.__vhdl_statement_ForIterationScheme = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression181"):
                opp_val = getattr(old_value, "Expression181", None)
                if opp_val == self:
                    setattr(old_value, "Expression181", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression181"):
                opp_val = getattr(value, "Expression181", None)
                setattr(value, "Expression181", self)

class vhdl_statement_WhileIterationScheme(IterationScheme):

    pass
class GenerationScheme:

    pass
class vhdl_statement_IfGenerationScheme(GenerationScheme):

    pass
class vhdl_statement_ForGenerationScheme(GenerationScheme):

    def __init__(self, variable: str, vhdl_statement_ForGenerationScheme: "Expression" = None, GenerationScheme: "vhdl_statement_GenerateStatement"):
        self.variable = variable
        self.vhdl_statement_ForGenerationScheme = vhdl_statement_ForGenerationScheme
        
    @property
    def variable(self) -> str:
        return self.__variable

    @variable.setter
    def variable(self, variable: str):
        self.__variable = variable

    @property
    def vhdl_statement_ForGenerationScheme(self):
        return self.__vhdl_statement_ForGenerationScheme

    @vhdl_statement_ForGenerationScheme.setter
    def vhdl_statement_ForGenerationScheme(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_statement_ForGenerationScheme__vhdl_statement_ForGenerationScheme", None)
        self.__vhdl_statement_ForGenerationScheme = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression179"):
                opp_val = getattr(old_value, "Expression179", None)
                if opp_val == self:
                    setattr(old_value, "Expression179", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression179"):
                opp_val = getattr(value, "Expression179", None)
                setattr(value, "Expression179", self)

class ConfigurationReference:

    pass
class statement_vhdl_EntityReference:

    pass
class statement_vhdl_ComponentReference:

    pass
class InstantiationStatement:

    pass
class vhdl_statement_ConfigurationInstantiationStatement(InstantiationStatement):

    pass
class vhdl_statement_EntityInstantiationStatement(InstantiationStatement):

    pass
class vhdl_statement_ComponentInstantiationStatement(InstantiationStatement):

    pass
class statement_vhdl_Name:

    pass
class BreakStatementItem:

    pass
class statement_vhdl_PortMaps:

    pass
class statement_vhdl_Ports:

    pass
class statement_vhdl_GenericMaps:

    pass
class statement_vhdl_Generics:

    pass
class statement_vhdl_CallReference:

    pass
class IfStatementTest:

    pass
class IfStatement:

    pass
class vhdl_statement_SimultaneousIfStatement(IfStatement):

    pass
class CaseAlternative:

    pass
class CaseStatement:

    pass
class vhdl_statement_SimultaneousCaseStatement(CaseStatement):

    pass
class vhdl_ComponentReference(ABC):

    pass
class statement_vhdl_MultiName:

    pass
class DelayMechanism:

    pass
class vhdl_statement_TransportMechanism(DelayMechanism):

    pass
class vhdl_statement_RejectMechanism(DelayMechanism):

    pass
class ConditionalSignalAssignmentStatement:

    pass
class vhdl_statement_SelectedSignalAssignmentStatement(ConditionalSignalAssignmentStatement):

    pass
class SignalAssignmentStatement:

    pass
class vhdl_statement_SequentialSignalAssignmentStatement(SignalAssignmentStatement):

    pass
class vhdl_statement_ConditionalSignalAssignmentStatement(SignalAssignmentStatement):

    pass
class ExpressionStatement:

    pass
class vhdl_statement_ReturnStatement(ExpressionStatement):

    pass
class SubprogramDeclaration:

    pass
class vhdl_declaration_ProcedureDeclaration(SubprogramDeclaration):

    pass
class vhdl_CallReference(ABC):

    pass
class CallReference:

    pass
class vhdl_CallResolvedReference(CallReference):

    pass
class configuration_ConfigurationReference:

    pass
class ComponentReference:

    pass
class PackageReference:

    pass
class EntityReference:

    pass
class nature_NatureReference:

    pass
class vhdl_expression_SubnatureIndicationExpression(nature_NatureReference, expression_IndicationExpression):

    pass
class type_TypeReference:

    pass
class MultiName:

    pass
class vhdl_VhdlObject(ABC):

    def __init__(self, id: str):
        self.id = id
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

class vhdl_MultiName(ABC):

    pass
class vhdl_MultiNamed:

    pass
class vhdl_Named(ABC):

    pass
class TypeReference:

    pass
class Expression:

    pass
class vhdl_expression_NullExpression(Expression):

    pass
class vhdl_expression_WaveformExpression(Expression):

    pass
class vhdl_expression_BinaryExpression(Expression):

    pass
class vhdl_expression_ValueExpression(Expression):

    def __init__(self, value: str, Expression181: "vhdl_statement_ForIterationScheme", Expression297: "vhdl_type_ConstrainedArrayTypeDefinition", Expression109: "vhdl_statement_AssertionStatement", Expression54: "vhdl_statement_SelectedSignalAssignmentStatement", Expression74: "vhdl_statement_CaseStatement", Expression215: "vhdl_expression_SignExpression", Expression78: "vhdl_statement_CaseAlternative", Expression187: "vhdl_expression_AssociationExpression", Expression152: "vhdl_statement_SimpleSimultaneousStatement", Expression30: "vhdl_PortMaps", Expression67: "vhdl_statement_WaitStatement", Expression183: "vhdl_statement_IfGenerationScheme", Expression69: "vhdl_statement_VariableAssignmentStatement", Expression87: "vhdl_statement_IfStatementTest", Expression185: "vhdl_statement_RejectMechanism", Expression328: "vhdl_ams_QuantityAspect", Expression177: "vhdl_statement_ExpressionStatement", Expression333: "vhdl_ams_Spectrum", Expression201: "vhdl_expression_IndicationExpression", Expression112: "vhdl_statement_AssertionStatement", Expression179: "vhdl_statement_ForGenerationScheme", Expression250: "vhdl_declaration_LimitDeclaration", Expression72: "vhdl_statement_VariableAssignmentStatement", Expression224: "vhdl_expression_WaveformExpression", Expression294: "vhdl_declaration_ValueDeclaration", Expression106: "vhdl_statement_AssertionStatement", Expression193: "vhdl_expression_BinaryExpression", Expression338: "vhdl_ams_Noise", Expression56: "vhdl_statement_SequentialSignalAssignmentStatement", Expression314: "vhdl_nature_ConstrainedArrayNatureDefinition", Expression50: "vhdl_statement_ReportStatement", Expression221: "vhdl_expression_WaveformExpression", Expression310: "vhdl_type_RangeTypeDefinition", Expression132: "vhdl_statement_BreakStatement", Expression283: "vhdl_declaration_FileDeclaration", Expression173: "vhdl_statement_NextStatement", Expression336: "vhdl_ams_Spectrum", Expression198: "vhdl_expression_IndicationExpression", Expression64: "vhdl_statement_WaitStatement", Expression217: "vhdl_expression_UnaryExpression", Expression278: "vhdl_declaration_DisconnectionSpecification", Expression47: "vhdl_statement_ReportStatement", Expression160: "vhdl_statement_ExitStatement", Expression226: "vhdl_expression_MultiExpression", Expression236: "vhdl_declaration_AttributeSpecification", Expression175: "vhdl_statement_WhileIterationScheme", Expression280: "vhdl_declaration_FileDeclaration", Expression228: "vhdl_expression_TypeQualificationExpression", Expression190: "vhdl_expression_AssociationExpression", Expression142: "vhdl_statement_BreakStatementItem", Expression248: "vhdl_declaration_FreeQuantityDeclaration", Expression307: "vhdl_type_RangeTypeDefinition", Expression158: "vhdl_statement_SimpleSimultaneousStatement", Expression331: "vhdl_ams_QuantityAspect", Expression302: "vhdl_type_PhysicalTypeDefinition", Expression52: "vhdl_statement_ConditionalSignalAssignmentStatement", Expression: "vhdl_GenericMaps", Expression58: "vhdl_statement_SignalAssignmentStatement", Expression196: "vhdl_expression_BinaryExpression", Expression204: "vhdl_expression_IndicationExpression", Expression155: "vhdl_statement_SimpleSimultaneousStatement", Expression114: "vhdl_statement_BlockStatement"):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class vhdl_expression_IndicationExpression(Expression):

    pass
class vhdl_expression_UnaffectedExpression(Expression):

    pass
class vhdl_expression_OpenExpression(Expression):

    pass
class vhdl_expression_SignExpression(Expression):

    def __init__(self, sign: str, vhdl_expression_SignExpression: "Expression" = None, Expression181: "vhdl_statement_ForIterationScheme", Expression297: "vhdl_type_ConstrainedArrayTypeDefinition", Expression109: "vhdl_statement_AssertionStatement", Expression54: "vhdl_statement_SelectedSignalAssignmentStatement", Expression74: "vhdl_statement_CaseStatement", Expression215: "vhdl_expression_SignExpression", Expression78: "vhdl_statement_CaseAlternative", Expression187: "vhdl_expression_AssociationExpression", Expression152: "vhdl_statement_SimpleSimultaneousStatement", Expression30: "vhdl_PortMaps", Expression67: "vhdl_statement_WaitStatement", Expression183: "vhdl_statement_IfGenerationScheme", Expression69: "vhdl_statement_VariableAssignmentStatement", Expression87: "vhdl_statement_IfStatementTest", Expression185: "vhdl_statement_RejectMechanism", Expression328: "vhdl_ams_QuantityAspect", Expression177: "vhdl_statement_ExpressionStatement", Expression333: "vhdl_ams_Spectrum", Expression201: "vhdl_expression_IndicationExpression", Expression112: "vhdl_statement_AssertionStatement", Expression179: "vhdl_statement_ForGenerationScheme", Expression250: "vhdl_declaration_LimitDeclaration", Expression72: "vhdl_statement_VariableAssignmentStatement", Expression224: "vhdl_expression_WaveformExpression", Expression294: "vhdl_declaration_ValueDeclaration", Expression106: "vhdl_statement_AssertionStatement", Expression193: "vhdl_expression_BinaryExpression", Expression338: "vhdl_ams_Noise", Expression56: "vhdl_statement_SequentialSignalAssignmentStatement", Expression314: "vhdl_nature_ConstrainedArrayNatureDefinition", Expression50: "vhdl_statement_ReportStatement", Expression221: "vhdl_expression_WaveformExpression", Expression310: "vhdl_type_RangeTypeDefinition", Expression132: "vhdl_statement_BreakStatement", Expression283: "vhdl_declaration_FileDeclaration", Expression173: "vhdl_statement_NextStatement", Expression336: "vhdl_ams_Spectrum", Expression198: "vhdl_expression_IndicationExpression", Expression64: "vhdl_statement_WaitStatement", Expression217: "vhdl_expression_UnaryExpression", Expression278: "vhdl_declaration_DisconnectionSpecification", Expression47: "vhdl_statement_ReportStatement", Expression160: "vhdl_statement_ExitStatement", Expression226: "vhdl_expression_MultiExpression", Expression236: "vhdl_declaration_AttributeSpecification", Expression175: "vhdl_statement_WhileIterationScheme", Expression280: "vhdl_declaration_FileDeclaration", Expression228: "vhdl_expression_TypeQualificationExpression", Expression190: "vhdl_expression_AssociationExpression", Expression142: "vhdl_statement_BreakStatementItem", Expression248: "vhdl_declaration_FreeQuantityDeclaration", Expression307: "vhdl_type_RangeTypeDefinition", Expression158: "vhdl_statement_SimpleSimultaneousStatement", Expression331: "vhdl_ams_QuantityAspect", Expression302: "vhdl_type_PhysicalTypeDefinition", Expression52: "vhdl_statement_ConditionalSignalAssignmentStatement", Expression: "vhdl_GenericMaps", Expression58: "vhdl_statement_SignalAssignmentStatement", Expression196: "vhdl_expression_BinaryExpression", Expression204: "vhdl_expression_IndicationExpression", Expression155: "vhdl_statement_SimpleSimultaneousStatement", Expression114: "vhdl_statement_BlockStatement"):
        self.sign = sign
        self.vhdl_expression_SignExpression = vhdl_expression_SignExpression
        
    @property
    def sign(self) -> str:
        return self.__sign

    @sign.setter
    def sign(self, sign: str):
        self.__sign = sign

    @property
    def vhdl_expression_SignExpression(self):
        return self.__vhdl_expression_SignExpression

    @vhdl_expression_SignExpression.setter
    def vhdl_expression_SignExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_expression_SignExpression__vhdl_expression_SignExpression", None)
        self.__vhdl_expression_SignExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression215"):
                opp_val = getattr(old_value, "Expression215", None)
                if opp_val == self:
                    setattr(old_value, "Expression215", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression215"):
                opp_val = getattr(value, "Expression215", None)
                setattr(value, "Expression215", self)

class vhdl_expression_UnaryExpression(Expression):

    def __init__(self, operator: str, vhdl_expression_UnaryExpression: "Expression" = None, Expression181: "vhdl_statement_ForIterationScheme", Expression297: "vhdl_type_ConstrainedArrayTypeDefinition", Expression109: "vhdl_statement_AssertionStatement", Expression54: "vhdl_statement_SelectedSignalAssignmentStatement", Expression74: "vhdl_statement_CaseStatement", Expression215: "vhdl_expression_SignExpression", Expression78: "vhdl_statement_CaseAlternative", Expression187: "vhdl_expression_AssociationExpression", Expression152: "vhdl_statement_SimpleSimultaneousStatement", Expression30: "vhdl_PortMaps", Expression67: "vhdl_statement_WaitStatement", Expression183: "vhdl_statement_IfGenerationScheme", Expression69: "vhdl_statement_VariableAssignmentStatement", Expression87: "vhdl_statement_IfStatementTest", Expression185: "vhdl_statement_RejectMechanism", Expression328: "vhdl_ams_QuantityAspect", Expression177: "vhdl_statement_ExpressionStatement", Expression333: "vhdl_ams_Spectrum", Expression201: "vhdl_expression_IndicationExpression", Expression112: "vhdl_statement_AssertionStatement", Expression179: "vhdl_statement_ForGenerationScheme", Expression250: "vhdl_declaration_LimitDeclaration", Expression72: "vhdl_statement_VariableAssignmentStatement", Expression224: "vhdl_expression_WaveformExpression", Expression294: "vhdl_declaration_ValueDeclaration", Expression106: "vhdl_statement_AssertionStatement", Expression193: "vhdl_expression_BinaryExpression", Expression338: "vhdl_ams_Noise", Expression56: "vhdl_statement_SequentialSignalAssignmentStatement", Expression314: "vhdl_nature_ConstrainedArrayNatureDefinition", Expression50: "vhdl_statement_ReportStatement", Expression221: "vhdl_expression_WaveformExpression", Expression310: "vhdl_type_RangeTypeDefinition", Expression132: "vhdl_statement_BreakStatement", Expression283: "vhdl_declaration_FileDeclaration", Expression173: "vhdl_statement_NextStatement", Expression336: "vhdl_ams_Spectrum", Expression198: "vhdl_expression_IndicationExpression", Expression64: "vhdl_statement_WaitStatement", Expression217: "vhdl_expression_UnaryExpression", Expression278: "vhdl_declaration_DisconnectionSpecification", Expression47: "vhdl_statement_ReportStatement", Expression160: "vhdl_statement_ExitStatement", Expression226: "vhdl_expression_MultiExpression", Expression236: "vhdl_declaration_AttributeSpecification", Expression175: "vhdl_statement_WhileIterationScheme", Expression280: "vhdl_declaration_FileDeclaration", Expression228: "vhdl_expression_TypeQualificationExpression", Expression190: "vhdl_expression_AssociationExpression", Expression142: "vhdl_statement_BreakStatementItem", Expression248: "vhdl_declaration_FreeQuantityDeclaration", Expression307: "vhdl_type_RangeTypeDefinition", Expression158: "vhdl_statement_SimpleSimultaneousStatement", Expression331: "vhdl_ams_QuantityAspect", Expression302: "vhdl_type_PhysicalTypeDefinition", Expression52: "vhdl_statement_ConditionalSignalAssignmentStatement", Expression: "vhdl_GenericMaps", Expression58: "vhdl_statement_SignalAssignmentStatement", Expression196: "vhdl_expression_BinaryExpression", Expression204: "vhdl_expression_IndicationExpression", Expression155: "vhdl_statement_SimpleSimultaneousStatement", Expression114: "vhdl_statement_BlockStatement"):
        self.operator = operator
        self.vhdl_expression_UnaryExpression = vhdl_expression_UnaryExpression
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def vhdl_expression_UnaryExpression(self):
        return self.__vhdl_expression_UnaryExpression

    @vhdl_expression_UnaryExpression.setter
    def vhdl_expression_UnaryExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_expression_UnaryExpression__vhdl_expression_UnaryExpression", None)
        self.__vhdl_expression_UnaryExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression217"):
                opp_val = getattr(old_value, "Expression217", None)
                if opp_val == self:
                    setattr(old_value, "Expression217", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression217"):
                opp_val = getattr(value, "Expression217", None)
                setattr(value, "Expression217", self)

class vhdl_expression_MultiExpression(Expression):

    pass
class vhdl_expression_AssociationExpression(Expression):

    pass
class vhdl_PackageReference(ABC):

    pass
class Declaration:

    pass
class vhdl_declaration_ConfigurationSpecification(Declaration):

    pass
class vhdl_declaration_UseClauseDeclaration(Declaration):

    pass
class vhdl_declaration_QuantityDeclaration(Declaration):

    pass
class vhdl_Name(EntityReference, CallReference, configuration_ConfigurationReference, type_TypeReference, nature_NatureReference, MultiName, PackageReference, ComponentReference):

    pass
class VhdlObject:

    pass
class vhdl_type_RecordTypeElement(type_Typed, MultiNamed, VhdlObject):

    pass
class vhdl_expression_Expression(VhdlObject):

    pass
class vhdl_PackageResolvedReference(VhdlObject, PackageReference):

    pass
class vhdl_statement_Statement(VhdlObject):

    def __init__(self, label: str):
        self.label = label
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

class vhdl_Signature(VhdlObject):

    pass
class vhdl_nature_NatureDefinition(VhdlObject):

    pass
class vhdl_statement_IfStatementTest(VhdlObject):

    pass
class vhdl_type_TypeDefinition(VhdlObject):

    pass
class vhdl_Module(VhdlObject):

    pass
class vhdl_nature_RecordNatureElement(MultiNamed, VhdlObject, nature_Natured):

    pass
class vhdl_PortMaps(VhdlObject):

    pass
class vhdl_configuration_ConfigurationResolvedReference(configuration_ConfigurationReference, VhdlObject):

    pass
class vhdl_declaration_Declaration(VhdlObject):

    pass
class vhdl_Model(VhdlObject):

    pass
class vhdl_declaration_SubprogramBody(VhdlObject):

    pass
class vhdl_configuration_ConfigurationItem(VhdlObject):

    pass
class vhdl_ams_QuantityAspect(MultiNamed, VhdlObject):

    pass
class vhdl_NameList(VhdlObject, MultiName):

    pass
class vhdl_statement_IterationScheme(VhdlObject):

    pass
class vhdl_GenericMaps(VhdlObject):

    pass
class vhdl_statement_BreakStatementItem(VhdlObject):

    pass
class vhdl_EntityResolvedReference(EntityReference, VhdlObject):

    pass
class vhdl_statement_DelayMechanism(VhdlObject):

    pass
class vhdl_ComponentResolvedReference(VhdlObject, ComponentReference):

    pass
class vhdl_statement_GenerationScheme(VhdlObject):

    pass
class vhdl_ams_SourceAspect(VhdlObject):

    pass
class vhdl_statement_CaseAlternative(VhdlObject):

    pass
class vhdl_DesignUnit(VhdlObject):

    def __init__(self, library: str, vhdl_DesignUnit: set["vhdl_Name"] = None, vhdl_DesignUnit8: "vhdl_Module" = None, vhdl_DesignUnit24: "vhdl_Model" = None):
        self.library = library
        self.vhdl_DesignUnit = vhdl_DesignUnit if vhdl_DesignUnit is not None else set()
        self.vhdl_DesignUnit8 = vhdl_DesignUnit8
        self.vhdl_DesignUnit24 = vhdl_DesignUnit24
        
    @property
    def library(self) -> str:
        return self.__library

    @library.setter
    def library(self, library: str):
        self.__library = library

    @property
    def vhdl_DesignUnit24(self):
        return self.__vhdl_DesignUnit24

    @vhdl_DesignUnit24.setter
    def vhdl_DesignUnit24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_DesignUnit__vhdl_DesignUnit24", None)
        self.__vhdl_DesignUnit24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_Model"):
                opp_val = getattr(old_value, "vhdl_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_Model"):
                opp_val = getattr(value, "vhdl_Model", None)
                if opp_val is None:
                    setattr(value, "vhdl_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def vhdl_DesignUnit(self):
        return self.__vhdl_DesignUnit

    @vhdl_DesignUnit.setter
    def vhdl_DesignUnit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_DesignUnit__vhdl_DesignUnit", None)
        self.__vhdl_DesignUnit = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "vhdl_Name"):
                    opp_val = getattr(item, "vhdl_Name", None)
                    
                    if opp_val == self:
                        setattr(item, "vhdl_Name", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "vhdl_Name"):
                    opp_val = getattr(item, "vhdl_Name", None)
                    
                    setattr(item, "vhdl_Name", self)
                    

    @property
    def vhdl_DesignUnit8(self):
        return self.__vhdl_DesignUnit8

    @vhdl_DesignUnit8.setter
    def vhdl_DesignUnit8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_DesignUnit__vhdl_DesignUnit8", None)
        self.__vhdl_DesignUnit8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vhdl_Module"):
                opp_val = getattr(old_value, "vhdl_Module", None)
                if opp_val == self:
                    setattr(old_value, "vhdl_Module", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vhdl_Module"):
                opp_val = getattr(value, "vhdl_Module", None)
                setattr(value, "vhdl_Module", self)

class vhdl_Ports(VhdlObject):

    pass
class vhdl_Generics(VhdlObject):

    pass
class declaration_Declaration:

    pass
class vhdl_declaration_ValueDeclaration(MultiNamed, type_Typed, declaration_Declaration):

    pass
class vhdl_declaration_LimitDeclaration(MultiNamed, type_Typed, declaration_Declaration):

    pass
class vhdl_declaration_DisconnectionSpecification(type_Typed, declaration_Declaration):

    pass
class vhdl_declaration_TerminalDeclaration(MultiNamed, nature_Natured, declaration_Declaration):

    pass
class vhdl_declaration_FileDeclaration(MultiNamed, type_Typed, declaration_Declaration):

    pass
class Statement:

    pass
class vhdl_statement_ProcessStatement(Statement):

    def __init__(self, postponed: bool, vhdl_statement_ProcessStatement103: "statement_vhdl_MultiName" = None, vhdl_statement_ProcessStatement: set["Declaration"] = None, vhdl_statement_ProcessStatement100: set["Statement"] = None, Statement128: "vhdl_statement_BlockStatement", Statement167: "vhdl_statement_GenerateStatement", Statement18: "vhdl_Entity", Statement81: "vhdl_statement_CaseAlternative", Statement90: "vhdl_statement_IfStatementTest", Statement96: "vhdl_statement_SimultaneousProceduralStatement", Statement: "vhdl_Architecture", Statement171: "vhdl_statement_LoopStatement", Statement85: "vhdl_statement_IfStatement", Statement260: "vhdl_declaration_SubprogramBody", Statement101: "vhdl_statement_ProcessStatement"):
        self.postponed = postponed
        self.vhdl_statement_ProcessStatement103 = vhdl_statement_ProcessStatement103
        self.vhdl_statement_ProcessStatement = vhdl_statement_ProcessStatement if vhdl_statement_ProcessStatement is not None else set()
        self.vhdl_statement_ProcessStatement100 = vhdl_statement_ProcessStatement100 if vhdl_statement_ProcessStatement100 is not None else set()
        
    @property
    def postponed(self) -> bool:
        return self.__postponed

    @postponed.setter
    def postponed(self, postponed: bool):
        self.__postponed = postponed

    @property
    def vhdl_statement_ProcessStatement103(self):
        return self.__vhdl_statement_ProcessStatement103

    @vhdl_statement_ProcessStatement103.setter
    def vhdl_statement_ProcessStatement103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_statement_ProcessStatement__vhdl_statement_ProcessStatement103", None)
        self.__vhdl_statement_ProcessStatement103 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statement_vhdl_MultiName104"):
                opp_val = getattr(old_value, "statement_vhdl_MultiName104", None)
                if opp_val == self:
                    setattr(old_value, "statement_vhdl_MultiName104", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statement_vhdl_MultiName104"):
                opp_val = getattr(value, "statement_vhdl_MultiName104", None)
                setattr(value, "statement_vhdl_MultiName104", self)

    @property
    def vhdl_statement_ProcessStatement(self):
        return self.__vhdl_statement_ProcessStatement

    @vhdl_statement_ProcessStatement.setter
    def vhdl_statement_ProcessStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_statement_ProcessStatement__vhdl_statement_ProcessStatement", None)
        self.__vhdl_statement_ProcessStatement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Declaration98"):
                    opp_val = getattr(item, "Declaration98", None)
                    
                    if opp_val == self:
                        setattr(item, "Declaration98", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Declaration98"):
                    opp_val = getattr(item, "Declaration98", None)
                    
                    setattr(item, "Declaration98", self)
                    

    @property
    def vhdl_statement_ProcessStatement100(self):
        return self.__vhdl_statement_ProcessStatement100

    @vhdl_statement_ProcessStatement100.setter
    def vhdl_statement_ProcessStatement100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_statement_ProcessStatement__vhdl_statement_ProcessStatement100", None)
        self.__vhdl_statement_ProcessStatement100 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Statement101"):
                    opp_val = getattr(item, "Statement101", None)
                    
                    if opp_val == self:
                        setattr(item, "Statement101", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Statement101"):
                    opp_val = getattr(item, "Statement101", None)
                    
                    setattr(item, "Statement101", self)
                    

class vhdl_statement_ExpressionStatement(Statement):

    pass
class vhdl_statement_LoopStatement(Statement):

    pass
class vhdl_statement_WaitStatement(Statement):

    pass
class vhdl_statement_AssertionStatement(Statement):

    def __init__(self, postponed: bool, vhdl_statement_AssertionStatement: "Expression" = None, vhdl_statement_AssertionStatement108: "Expression" = None, vhdl_statement_AssertionStatement111: "Expression" = None, Statement128: "vhdl_statement_BlockStatement", Statement167: "vhdl_statement_GenerateStatement", Statement18: "vhdl_Entity", Statement81: "vhdl_statement_CaseAlternative", Statement90: "vhdl_statement_IfStatementTest", Statement96: "vhdl_statement_SimultaneousProceduralStatement", Statement: "vhdl_Architecture", Statement171: "vhdl_statement_LoopStatement", Statement85: "vhdl_statement_IfStatement", Statement260: "vhdl_declaration_SubprogramBody", Statement101: "vhdl_statement_ProcessStatement"):
        self.postponed = postponed
        self.vhdl_statement_AssertionStatement = vhdl_statement_AssertionStatement
        self.vhdl_statement_AssertionStatement108 = vhdl_statement_AssertionStatement108
        self.vhdl_statement_AssertionStatement111 = vhdl_statement_AssertionStatement111
        
    @property
    def postponed(self) -> bool:
        return self.__postponed

    @postponed.setter
    def postponed(self, postponed: bool):
        self.__postponed = postponed

    @property
    def vhdl_statement_AssertionStatement(self):
        return self.__vhdl_statement_AssertionStatement

    @vhdl_statement_AssertionStatement.setter
    def vhdl_statement_AssertionStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_statement_AssertionStatement__vhdl_statement_AssertionStatement", None)
        self.__vhdl_statement_AssertionStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression106"):
                opp_val = getattr(old_value, "Expression106", None)
                if opp_val == self:
                    setattr(old_value, "Expression106", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression106"):
                opp_val = getattr(value, "Expression106", None)
                setattr(value, "Expression106", self)

    @property
    def vhdl_statement_AssertionStatement111(self):
        return self.__vhdl_statement_AssertionStatement111

    @vhdl_statement_AssertionStatement111.setter
    def vhdl_statement_AssertionStatement111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_statement_AssertionStatement__vhdl_statement_AssertionStatement111", None)
        self.__vhdl_statement_AssertionStatement111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression112"):
                opp_val = getattr(old_value, "Expression112", None)
                if opp_val == self:
                    setattr(old_value, "Expression112", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression112"):
                opp_val = getattr(value, "Expression112", None)
                setattr(value, "Expression112", self)

    @property
    def vhdl_statement_AssertionStatement108(self):
        return self.__vhdl_statement_AssertionStatement108

    @vhdl_statement_AssertionStatement108.setter
    def vhdl_statement_AssertionStatement108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_statement_AssertionStatement__vhdl_statement_AssertionStatement108", None)
        self.__vhdl_statement_AssertionStatement108 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression109"):
                opp_val = getattr(old_value, "Expression109", None)
                if opp_val == self:
                    setattr(old_value, "Expression109", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression109"):
                opp_val = getattr(value, "Expression109", None)
                setattr(value, "Expression109", self)

class vhdl_statement_SimpleSimultaneousStatement(Statement):

    pass
class vhdl_statement_NextStatement(Statement):

    def __init__(self, next: str, vhdl_statement_NextStatement: "Expression" = None, Statement128: "vhdl_statement_BlockStatement", Statement167: "vhdl_statement_GenerateStatement", Statement18: "vhdl_Entity", Statement81: "vhdl_statement_CaseAlternative", Statement90: "vhdl_statement_IfStatementTest", Statement96: "vhdl_statement_SimultaneousProceduralStatement", Statement: "vhdl_Architecture", Statement171: "vhdl_statement_LoopStatement", Statement85: "vhdl_statement_IfStatement", Statement260: "vhdl_declaration_SubprogramBody", Statement101: "vhdl_statement_ProcessStatement"):
        self.next = next
        self.vhdl_statement_NextStatement = vhdl_statement_NextStatement
        
    @property
    def next(self) -> str:
        return self.__next

    @next.setter
    def next(self, next: str):
        self.__next = next

    @property
    def vhdl_statement_NextStatement(self):
        return self.__vhdl_statement_NextStatement

    @vhdl_statement_NextStatement.setter
    def vhdl_statement_NextStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_statement_NextStatement__vhdl_statement_NextStatement", None)
        self.__vhdl_statement_NextStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression173"):
                opp_val = getattr(old_value, "Expression173", None)
                if opp_val == self:
                    setattr(old_value, "Expression173", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression173"):
                opp_val = getattr(value, "Expression173", None)
                setattr(value, "Expression173", self)

class vhdl_statement_IfStatement(Statement):

    pass
class vhdl_statement_BlockStatement(Statement):

    pass
class vhdl_statement_BreakStatement(Statement):

    pass
class vhdl_statement_SimultaneousProceduralStatement(Statement):

    pass
class vhdl_statement_ExitStatement(Statement):

    def __init__(self, exit: str, vhdl_statement_ExitStatement: "Expression" = None, Statement128: "vhdl_statement_BlockStatement", Statement167: "vhdl_statement_GenerateStatement", Statement18: "vhdl_Entity", Statement81: "vhdl_statement_CaseAlternative", Statement90: "vhdl_statement_IfStatementTest", Statement96: "vhdl_statement_SimultaneousProceduralStatement", Statement: "vhdl_Architecture", Statement171: "vhdl_statement_LoopStatement", Statement85: "vhdl_statement_IfStatement", Statement260: "vhdl_declaration_SubprogramBody", Statement101: "vhdl_statement_ProcessStatement"):
        self.exit = exit
        self.vhdl_statement_ExitStatement = vhdl_statement_ExitStatement
        
    @property
    def exit(self) -> str:
        return self.__exit

    @exit.setter
    def exit(self, exit: str):
        self.__exit = exit

    @property
    def vhdl_statement_ExitStatement(self):
        return self.__vhdl_statement_ExitStatement

    @vhdl_statement_ExitStatement.setter
    def vhdl_statement_ExitStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_statement_ExitStatement__vhdl_statement_ExitStatement", None)
        self.__vhdl_statement_ExitStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression160"):
                opp_val = getattr(old_value, "Expression160", None)
                if opp_val == self:
                    setattr(old_value, "Expression160", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression160"):
                opp_val = getattr(value, "Expression160", None)
                setattr(value, "Expression160", self)

class vhdl_statement_SignalAssignmentStatement(Statement):

    def __init__(self, postponed: bool, guarded: bool, vhdl_statement_SignalAssignmentStatement: "Expression" = None, vhdl_statement_SignalAssignmentStatement60: "DelayMechanism" = None, Statement128: "vhdl_statement_BlockStatement", Statement167: "vhdl_statement_GenerateStatement", Statement18: "vhdl_Entity", Statement81: "vhdl_statement_CaseAlternative", Statement90: "vhdl_statement_IfStatementTest", Statement96: "vhdl_statement_SimultaneousProceduralStatement", Statement: "vhdl_Architecture", Statement171: "vhdl_statement_LoopStatement", Statement85: "vhdl_statement_IfStatement", Statement260: "vhdl_declaration_SubprogramBody", Statement101: "vhdl_statement_ProcessStatement"):
        self.postponed = postponed
        self.guarded = guarded
        self.vhdl_statement_SignalAssignmentStatement = vhdl_statement_SignalAssignmentStatement
        self.vhdl_statement_SignalAssignmentStatement60 = vhdl_statement_SignalAssignmentStatement60
        
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
    def vhdl_statement_SignalAssignmentStatement(self):
        return self.__vhdl_statement_SignalAssignmentStatement

    @vhdl_statement_SignalAssignmentStatement.setter
    def vhdl_statement_SignalAssignmentStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_statement_SignalAssignmentStatement__vhdl_statement_SignalAssignmentStatement", None)
        self.__vhdl_statement_SignalAssignmentStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression58"):
                opp_val = getattr(old_value, "Expression58", None)
                if opp_val == self:
                    setattr(old_value, "Expression58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression58"):
                opp_val = getattr(value, "Expression58", None)
                setattr(value, "Expression58", self)

    @property
    def vhdl_statement_SignalAssignmentStatement60(self):
        return self.__vhdl_statement_SignalAssignmentStatement60

    @vhdl_statement_SignalAssignmentStatement60.setter
    def vhdl_statement_SignalAssignmentStatement60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_statement_SignalAssignmentStatement__vhdl_statement_SignalAssignmentStatement60", None)
        self.__vhdl_statement_SignalAssignmentStatement60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DelayMechanism"):
                opp_val = getattr(old_value, "DelayMechanism", None)
                if opp_val == self:
                    setattr(old_value, "DelayMechanism", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DelayMechanism"):
                opp_val = getattr(value, "DelayMechanism", None)
                setattr(value, "DelayMechanism", self)

class vhdl_statement_ProcedureCallStatement(Statement):

    def __init__(self, postponed: bool, vhdl_statement_ProcedureCallStatement: "statement_vhdl_CallReference" = None, Statement128: "vhdl_statement_BlockStatement", Statement167: "vhdl_statement_GenerateStatement", Statement18: "vhdl_Entity", Statement81: "vhdl_statement_CaseAlternative", Statement90: "vhdl_statement_IfStatementTest", Statement96: "vhdl_statement_SimultaneousProceduralStatement", Statement: "vhdl_Architecture", Statement171: "vhdl_statement_LoopStatement", Statement85: "vhdl_statement_IfStatement", Statement260: "vhdl_declaration_SubprogramBody", Statement101: "vhdl_statement_ProcessStatement"):
        self.postponed = postponed
        self.vhdl_statement_ProcedureCallStatement = vhdl_statement_ProcedureCallStatement
        
    @property
    def postponed(self) -> bool:
        return self.__postponed

    @postponed.setter
    def postponed(self, postponed: bool):
        self.__postponed = postponed

    @property
    def vhdl_statement_ProcedureCallStatement(self):
        return self.__vhdl_statement_ProcedureCallStatement

    @vhdl_statement_ProcedureCallStatement.setter
    def vhdl_statement_ProcedureCallStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_statement_ProcedureCallStatement__vhdl_statement_ProcedureCallStatement", None)
        self.__vhdl_statement_ProcedureCallStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statement_vhdl_CallReference"):
                opp_val = getattr(old_value, "statement_vhdl_CallReference", None)
                if opp_val == self:
                    setattr(old_value, "statement_vhdl_CallReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statement_vhdl_CallReference"):
                opp_val = getattr(value, "statement_vhdl_CallReference", None)
                setattr(value, "statement_vhdl_CallReference", self)

class vhdl_statement_ReportStatement(Statement):

    pass
class vhdl_statement_GenerateStatement(Statement):

    pass
class vhdl_statement_VariableAssignmentStatement(Statement):

    pass
class vhdl_statement_InstantiationStatement(Statement):

    pass
class vhdl_statement_CaseStatement(Statement):

    pass
class vhdl_EntityReference(ABC):

    pass
class Named:

    pass
class vhdl_declaration_NatureDeclaration(Named, declaration_Declaration):

    pass
class vhdl_declaration_SubprogramDeclaration(Named, declaration_Declaration):

    pass
class vhdl_declaration_AliasDeclaration(Named, declaration_Declaration):

    pass
class vhdl_declaration_AttributeDeclaration(Named, type_Typed, declaration_Declaration):

    pass
class vhdl_declaration_SubnatureDeclaration(nature_Natured, Named, declaration_Declaration):

    pass
class vhdl_declaration_TypeDeclaration(Named, declaration_Declaration):

    pass
class vhdl_declaration_GroupTemplateDeclaration(Named, declaration_Declaration):

    def __init__(self, entry: str):
        self.entry = entry
        
    @property
    def entry(self) -> str:
        return self.__entry

    @entry.setter
    def entry(self, entry: str):
        self.__entry = entry

class vhdl_Component(Named, declaration_Declaration):

    pass
class vhdl_declaration_GroupDeclaration(Named, declaration_Declaration):

    pass
class vhdl_declaration_AttributeSpecification(Named, declaration_Declaration):

    def __init__(self, class: str, vhdl_declaration_AttributeSpecification: "declaration_vhdl_MultiName" = None, vhdl_declaration_AttributeSpecification235: "Expression" = None):
        self.class = class
        self.vhdl_declaration_AttributeSpecification = vhdl_declaration_AttributeSpecification
        self.vhdl_declaration_AttributeSpecification235 = vhdl_declaration_AttributeSpecification235
        
    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def vhdl_declaration_AttributeSpecification(self):
        return self.__vhdl_declaration_AttributeSpecification

    @vhdl_declaration_AttributeSpecification.setter
    def vhdl_declaration_AttributeSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_declaration_AttributeSpecification__vhdl_declaration_AttributeSpecification", None)
        self.__vhdl_declaration_AttributeSpecification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "declaration_vhdl_MultiName"):
                opp_val = getattr(old_value, "declaration_vhdl_MultiName", None)
                if opp_val == self:
                    setattr(old_value, "declaration_vhdl_MultiName", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "declaration_vhdl_MultiName"):
                opp_val = getattr(value, "declaration_vhdl_MultiName", None)
                setattr(value, "declaration_vhdl_MultiName", self)

    @property
    def vhdl_declaration_AttributeSpecification235(self):
        return self.__vhdl_declaration_AttributeSpecification235

    @vhdl_declaration_AttributeSpecification235.setter
    def vhdl_declaration_AttributeSpecification235(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vhdl_declaration_AttributeSpecification__vhdl_declaration_AttributeSpecification235", None)
        self.__vhdl_declaration_AttributeSpecification235 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression236"):
                opp_val = getattr(old_value, "Expression236", None)
                if opp_val == self:
                    setattr(old_value, "Expression236", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression236"):
                opp_val = getattr(value, "Expression236", None)
                setattr(value, "Expression236", self)

class vhdl_configuration_BlockConfiguration(configuration_ConfigurationItem, Named):

    pass
class vhdl_expression_SubtypeIndicationExpression(Named, type_TypeReference, expression_IndicationExpression):

    pass
class vhdl_declaration_SubtypeDeclaration(Named, type_Typed, declaration_Declaration):

    pass
class Module:

    pass
class vhdl_configuration_Configuration(Named, Module):

    pass
class vhdl_Entity(Named, Module):

    pass
class vhdl_PackageBody(Module):

    pass
class vhdl_Package(Named, Module):

    pass
class vhdl_Architecture(Named, Module):

    pass