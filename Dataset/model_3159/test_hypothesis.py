import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Commands_LabelCommand,
    Sequencer,
    C_Sequencers_Break,
    C_Sequencers_Goto,
    Literal,
    C_Expressions_FloatLiteral,
    C_Expressions_DoubleLiteral,
    C_Expressions_ShortLiteral,
    C_Expressions_StringLiteral,
    C_Expressions_IntLiteral,
    C_Expressions_CharLiteral,
    LogicExpression,
    C_Expressions_SimpleLogicExpression,
    C_Expressions_DisplacementLogicExpression,
    ConditionalExpression,
    C_Expressions_ComposedConditionalExpression,
    ArithmeticExpression,
    C_Expressions_BinaryArithmeticExpression,
    C_Expressions_UnaryArithmeticExpression,
    Declarations_PrototypeFunctionDeclaration,
    VariableAccess,
    C_Expressions_PointerVariableAccess,
    Declarations_ArrayDeclaration,
    Declarations_ConstantDeclaration,
    Access,
    C_Expressions_ArrayAccess,
    C_Expressions_VariableAccess,
    C_Expressions_PrototypeAccess,
    C_Expressions_ConstantAccess,
    IterativeCommand,
    C_Commands_ForCommand,
    C_Commands_DefaultOption,
    C_Commands_CaseOption,
    Commands_DefaultOption,
    Commands_CaseOption,
    Expressions_VariableAccess,
    Expressions_ConditionalExpression,
    DecisionCommand,
    C_Commands_SwitchCommand,
    C_Commands_IfCommand,
    Expression,
    C_Expressions_LogicExpression,
    C_Expressions_ArithmeticExpression,
    C_Expressions_Literal,
    C_Expressions_ConditionalExpression,
    C_Expressions_ConstantExpression,
    C_Expressions_CastExpression,
    C_Expressions_Construction,
    C_Expressions_Expression,
    C_Commands_WhileCommand,
    BlockedElement,
    C_Sequencers_Sequencer,
    C_Commands_Command,
    C_CompilationDirectiveDeclarations_Endif,
    IfDirective,
    C_CompilationDirectiveDeclarations_Elif,
    Expressions_ConstantExpression,
    ComplexDirectiveDeclaration,
    C_CompilationDirectiveDeclarations_IfDirective,
    C_CompilationDirectiveDeclarations_ElseDirective,
    C_CompilationDirectiveDeclarations_Ifndef,
    CompilationDirectiveDeclarations_Endif,
    CompilationDirectiveDeclarations_ComplexDirectiveDeclaration,
    SimpleDirectiveDeclaration,
    C_CompilationDirectiveDeclarations_Include,
    C_CompilationDirectiveDeclarations_Define,
    CompilationDirectiveDeclaration,
    C_CompilationDirectiveDeclarations_ComplexDirectiveDeclaration,
    C_CompilationDirectiveDeclarations_CompilationDirectiveDeclaration,
    Declarations_SimpleVariableDeclaration,
    FlowControlCommand,
    C_Commands_ReturnCommand,
    C_Commands_DecisionCommand,
    Expressions_Access,
    Command,
    C_Commands_FlowControlCommand,
    C_Commands_IterativeCommand,
    C_Commands_ExpressionCommand,
    C_Commands_Assignment,
    Commands_Command,
    Declarations_FragmentVariableDeclaration,
    Declarations_VariableDeclaration,
    Expressions_Expression,
    Declaration,
    C_Declarations_PrototypeFunctionDeclaration,
    C_Declarations_VariableDeclaration,
    C_Declarations_ConstantDeclaration,
    Main_Function,
    CompilationDirectiveDeclarations_CompilationDirectiveDeclaration,
    Expressions_Construction,
    Declarations_CompositeVariableDeclaration,
    Expressions_Literal,
    CompositeVariableDeclaration,
    C_Declarations_StructDeclaration,
    C_Declarations_TypeDefDeclaration,
    C_Declarations_EnumDeclaration,
    VariableDeclaration,
    C_Declarations_CompositeVariableDeclaration,
    Main_Element,
    Unit,
    C_Main_C_Unit,
    Main_Comment,
    NamedElement,
    C_Declarations_Declaration,
    C_Main_Comment,
    C_Main_Element,
    C_Main_Unit,
    Main_Unit,
    C_Main_Program,
    Main_Block,
    C_Abstractions_BlockedElement,
    C_Abstractions_NamedElement,
    Abstractions_NamedElement,
    C_Expressions_AtomicConditionalExpression,
    C_Expressions_FunctionCall,
    C_CompilationDirectiveDeclarations_Ifdef,
    C_Declarations_FragmentVariableDeclaration,
    C_Commands_LabelCommand,
    C_Expressions_Access,
    C_CompilationDirectiveDeclarations_SimpleDirectiveDeclaration,
    Types_Type,
    C_Types_FromHeader,
    CompositeType,
    C_Types_Enum,
    C_Types_Struct,
    C_Types_Array,
    C_Types_Typedef,
    Types_Array,
    Types_PrimitiveType,
    C_Types_Int,
    PrimitiveType,
    C_Types_Float,
    C_Types_Void,
    C_Types_Double,
    C_Types_Short,
    C_Types_Char,
    Abstractions_BlockedElement,
    C_Declarations_ArrayDeclaration,
    C_Declarations_SimpleVariableDeclaration,
    C_Main_Block,
    Declarations_Declaration,
    Element,
    C_Main_DeclarationsBlock,
    C_Main_FunctionsBlock,
    C_Main_Function,
    Main_DeclarationsBlock,
    C_Main_H_Unit,
    Type,
    C_Types_CompositeType,
    C_Types_PrimitiveType,
    C_Types_Type,
    ModifierKind,
    DisplacementLogicOperatorKind,
    RelationalOperatorKind,
    UnaryOperatorKind,
    RelationalConectorKind,
    BinaryOperatorKind,
    FunctionModifierKind,
    SimpleLogicOperatorKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_commands_labelcommand_is_not_abstract():
    assert not inspect.isabstract(Commands_LabelCommand)


def test_commands_labelcommand_constructor_exists():
    assert callable(Commands_LabelCommand.__init__)


def test_commands_labelcommand_constructor_args():
    sig = inspect.signature(Commands_LabelCommand.__init__)
    params = list(sig.parameters.keys())



def test_sequencer_is_not_abstract():
    assert not inspect.isabstract(Sequencer)


def test_sequencer_constructor_exists():
    assert callable(Sequencer.__init__)


def test_sequencer_constructor_args():
    sig = inspect.signature(Sequencer.__init__)
    params = list(sig.parameters.keys())



def test_c_sequencers_break_is_not_abstract():
    assert not inspect.isabstract(C_Sequencers_Break)


def test_c_sequencers_break_constructor_exists():
    assert callable(C_Sequencers_Break.__init__)


def test_c_sequencers_break_constructor_args():
    sig = inspect.signature(C_Sequencers_Break.__init__)
    params = list(sig.parameters.keys())



def test_c_sequencers_goto_is_not_abstract():
    assert not inspect.isabstract(C_Sequencers_Goto)


def test_c_sequencers_goto_constructor_exists():
    assert callable(C_Sequencers_Goto.__init__)


def test_c_sequencers_goto_constructor_args():
    sig = inspect.signature(C_Sequencers_Goto.__init__)
    params = list(sig.parameters.keys())



def test_literal_is_not_abstract():
    assert not inspect.isabstract(Literal)


def test_literal_constructor_exists():
    assert callable(Literal.__init__)


def test_literal_constructor_args():
    sig = inspect.signature(Literal.__init__)
    params = list(sig.parameters.keys())



def test_c_expressions_floatliteral_is_not_abstract():
    assert not inspect.isabstract(C_Expressions_FloatLiteral)


def test_c_expressions_floatliteral_constructor_exists():
    assert callable(C_Expressions_FloatLiteral.__init__)


def test_c_expressions_floatliteral_constructor_args():
    sig = inspect.signature(C_Expressions_FloatLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_c_expressions_floatliteral_has_value():
    assert hasattr(C_Expressions_FloatLiteral, "value")
    descriptor = None
    for klass in C_Expressions_FloatLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_c_expressions_doubleliteral_is_not_abstract():
    assert not inspect.isabstract(C_Expressions_DoubleLiteral)


def test_c_expressions_doubleliteral_constructor_exists():
    assert callable(C_Expressions_DoubleLiteral.__init__)


def test_c_expressions_doubleliteral_constructor_args():
    sig = inspect.signature(C_Expressions_DoubleLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_c_expressions_doubleliteral_has_value():
    assert hasattr(C_Expressions_DoubleLiteral, "value")
    descriptor = None
    for klass in C_Expressions_DoubleLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_c_expressions_shortliteral_is_not_abstract():
    assert not inspect.isabstract(C_Expressions_ShortLiteral)


def test_c_expressions_shortliteral_constructor_exists():
    assert callable(C_Expressions_ShortLiteral.__init__)


def test_c_expressions_shortliteral_constructor_args():
    sig = inspect.signature(C_Expressions_ShortLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_c_expressions_shortliteral_has_value():
    assert hasattr(C_Expressions_ShortLiteral, "value")
    descriptor = None
    for klass in C_Expressions_ShortLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_c_expressions_stringliteral_is_not_abstract():
    assert not inspect.isabstract(C_Expressions_StringLiteral)


def test_c_expressions_stringliteral_constructor_exists():
    assert callable(C_Expressions_StringLiteral.__init__)


def test_c_expressions_stringliteral_constructor_args():
    sig = inspect.signature(C_Expressions_StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_c_expressions_stringliteral_has_value():
    assert hasattr(C_Expressions_StringLiteral, "value")
    descriptor = None
    for klass in C_Expressions_StringLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_c_expressions_intliteral_is_not_abstract():
    assert not inspect.isabstract(C_Expressions_IntLiteral)


def test_c_expressions_intliteral_constructor_exists():
    assert callable(C_Expressions_IntLiteral.__init__)


def test_c_expressions_intliteral_constructor_args():
    sig = inspect.signature(C_Expressions_IntLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_c_expressions_intliteral_has_value():
    assert hasattr(C_Expressions_IntLiteral, "value")
    descriptor = None
    for klass in C_Expressions_IntLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_c_expressions_charliteral_is_not_abstract():
    assert not inspect.isabstract(C_Expressions_CharLiteral)


def test_c_expressions_charliteral_constructor_exists():
    assert callable(C_Expressions_CharLiteral.__init__)


def test_c_expressions_charliteral_constructor_args():
    sig = inspect.signature(C_Expressions_CharLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_c_expressions_charliteral_has_value():
    assert hasattr(C_Expressions_CharLiteral, "value")
    descriptor = None
    for klass in C_Expressions_CharLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_logicexpression_is_not_abstract():
    assert not inspect.isabstract(LogicExpression)


def test_logicexpression_constructor_exists():
    assert callable(LogicExpression.__init__)


def test_logicexpression_constructor_args():
    sig = inspect.signature(LogicExpression.__init__)
    params = list(sig.parameters.keys())



def test_c_expressions_simplelogicexpression_is_not_abstract():
    assert not inspect.isabstract(C_Expressions_SimpleLogicExpression)


def test_c_expressions_simplelogicexpression_constructor_exists():
    assert callable(C_Expressions_SimpleLogicExpression.__init__)


def test_c_expressions_simplelogicexpression_constructor_args():
    sig = inspect.signature(C_Expressions_SimpleLogicExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_c_expressions_simplelogicexpression_has_operator():
    assert hasattr(C_Expressions_SimpleLogicExpression, "operator")
    descriptor = None
    for klass in C_Expressions_SimpleLogicExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_c_expressions_displacementlogicexpression_is_not_abstract():
    assert not inspect.isabstract(C_Expressions_DisplacementLogicExpression)


def test_c_expressions_displacementlogicexpression_constructor_exists():
    assert callable(C_Expressions_DisplacementLogicExpression.__init__)


def test_c_expressions_displacementlogicexpression_constructor_args():
    sig = inspect.signature(C_Expressions_DisplacementLogicExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_c_expressions_displacementlogicexpression_has_operator():
    assert hasattr(C_Expressions_DisplacementLogicExpression, "operator")
    descriptor = None
    for klass in C_Expressions_DisplacementLogicExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_conditionalexpression_is_not_abstract():
    assert not inspect.isabstract(ConditionalExpression)


def test_conditionalexpression_constructor_exists():
    assert callable(ConditionalExpression.__init__)


def test_conditionalexpression_constructor_args():
    sig = inspect.signature(ConditionalExpression.__init__)
    params = list(sig.parameters.keys())



def test_c_expressions_composedconditionalexpression_is_not_abstract():
    assert not inspect.isabstract(C_Expressions_ComposedConditionalExpression)


def test_c_expressions_composedconditionalexpression_constructor_exists():
    assert callable(C_Expressions_ComposedConditionalExpression.__init__)


def test_c_expressions_composedconditionalexpression_constructor_args():
    sig = inspect.signature(C_Expressions_ComposedConditionalExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_c_expressions_composedconditionalexpression_has_operator():
    assert hasattr(C_Expressions_ComposedConditionalExpression, "operator")
    descriptor = None
    for klass in C_Expressions_ComposedConditionalExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_arithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(ArithmeticExpression)


def test_arithmeticexpression_constructor_exists():
    assert callable(ArithmeticExpression.__init__)


def test_arithmeticexpression_constructor_args():
    sig = inspect.signature(ArithmeticExpression.__init__)
    params = list(sig.parameters.keys())



def test_c_expressions_binaryarithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(C_Expressions_BinaryArithmeticExpression)


def test_c_expressions_binaryarithmeticexpression_constructor_exists():
    assert callable(C_Expressions_BinaryArithmeticExpression.__init__)


def test_c_expressions_binaryarithmeticexpression_constructor_args():
    sig = inspect.signature(C_Expressions_BinaryArithmeticExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_c_expressions_binaryarithmeticexpression_has_operator():
    assert hasattr(C_Expressions_BinaryArithmeticExpression, "operator")
    descriptor = None
    for klass in C_Expressions_BinaryArithmeticExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_c_expressions_unaryarithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(C_Expressions_UnaryArithmeticExpression)


def test_c_expressions_unaryarithmeticexpression_constructor_exists():
    assert callable(C_Expressions_UnaryArithmeticExpression.__init__)


def test_c_expressions_unaryarithmeticexpression_constructor_args():
    sig = inspect.signature(C_Expressions_UnaryArithmeticExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_c_expressions_unaryarithmeticexpression_has_operator():
    assert hasattr(C_Expressions_UnaryArithmeticExpression, "operator")
    descriptor = None
    for klass in C_Expressions_UnaryArithmeticExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_declarations_prototypefunctiondeclaration_is_not_abstract():
    assert not inspect.isabstract(Declarations_PrototypeFunctionDeclaration)


def test_declarations_prototypefunctiondeclaration_constructor_exists():
    assert callable(Declarations_PrototypeFunctionDeclaration.__init__)


def test_declarations_prototypefunctiondeclaration_constructor_args():
    sig = inspect.signature(Declarations_PrototypeFunctionDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_variableaccess_is_not_abstract():
    assert not inspect.isabstract(VariableAccess)


def test_variableaccess_constructor_exists():
    assert callable(VariableAccess.__init__)


def test_variableaccess_constructor_args():
    sig = inspect.signature(VariableAccess.__init__)
    params = list(sig.parameters.keys())



def test_c_expressions_pointervariableaccess_is_not_abstract():
    assert not inspect.isabstract(C_Expressions_PointerVariableAccess)


def test_c_expressions_pointervariableaccess_constructor_exists():
    assert callable(C_Expressions_PointerVariableAccess.__init__)


def test_c_expressions_pointervariableaccess_constructor_args():
    sig = inspect.signature(C_Expressions_PointerVariableAccess.__init__)
    params = list(sig.parameters.keys())



def test_declarations_arraydeclaration_is_not_abstract():
    assert not inspect.isabstract(Declarations_ArrayDeclaration)


def test_declarations_arraydeclaration_constructor_exists():
    assert callable(Declarations_ArrayDeclaration.__init__)


def test_declarations_arraydeclaration_constructor_args():
    sig = inspect.signature(Declarations_ArrayDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_declarations_constantdeclaration_is_not_abstract():
    assert not inspect.isabstract(Declarations_ConstantDeclaration)


def test_declarations_constantdeclaration_constructor_exists():
    assert callable(Declarations_ConstantDeclaration.__init__)


def test_declarations_constantdeclaration_constructor_args():
    sig = inspect.signature(Declarations_ConstantDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_access_is_not_abstract():
    assert not inspect.isabstract(Access)


def test_access_constructor_exists():
    assert callable(Access.__init__)


def test_access_constructor_args():
    sig = inspect.signature(Access.__init__)
    params = list(sig.parameters.keys())



def test_c_expressions_arrayaccess_is_not_abstract():
    assert not inspect.isabstract(C_Expressions_ArrayAccess)


def test_c_expressions_arrayaccess_constructor_exists():
    assert callable(C_Expressions_ArrayAccess.__init__)


def test_c_expressions_arrayaccess_constructor_args():
    sig = inspect.signature(C_Expressions_ArrayAccess.__init__)
    params = list(sig.parameters.keys())



def test_c_expressions_variableaccess_is_not_abstract():
    assert not inspect.isabstract(C_Expressions_VariableAccess)


def test_c_expressions_variableaccess_constructor_exists():
    assert callable(C_Expressions_VariableAccess.__init__)


def test_c_expressions_variableaccess_constructor_args():
    sig = inspect.signature(C_Expressions_VariableAccess.__init__)
    params = list(sig.parameters.keys())



def test_c_expressions_prototypeaccess_is_not_abstract():
    assert not inspect.isabstract(C_Expressions_PrototypeAccess)


def test_c_expressions_prototypeaccess_constructor_exists():
    assert callable(C_Expressions_PrototypeAccess.__init__)


def test_c_expressions_prototypeaccess_constructor_args():
    sig = inspect.signature(C_Expressions_PrototypeAccess.__init__)
    params = list(sig.parameters.keys())



def test_c_expressions_constantaccess_is_not_abstract():
    assert not inspect.isabstract(C_Expressions_ConstantAccess)


def test_c_expressions_constantaccess_constructor_exists():
    assert callable(C_Expressions_ConstantAccess.__init__)


def test_c_expressions_constantaccess_constructor_args():
    sig = inspect.signature(C_Expressions_ConstantAccess.__init__)
    params = list(sig.parameters.keys())



def test_iterativecommand_is_not_abstract():
    assert not inspect.isabstract(IterativeCommand)


def test_iterativecommand_constructor_exists():
    assert callable(IterativeCommand.__init__)


def test_iterativecommand_constructor_args():
    sig = inspect.signature(IterativeCommand.__init__)
    params = list(sig.parameters.keys())



def test_c_commands_forcommand_is_not_abstract():
    assert not inspect.isabstract(C_Commands_ForCommand)


def test_c_commands_forcommand_constructor_exists():
    assert callable(C_Commands_ForCommand.__init__)


def test_c_commands_forcommand_constructor_args():
    sig = inspect.signature(C_Commands_ForCommand.__init__)
    params = list(sig.parameters.keys())



def test_c_commands_defaultoption_is_not_abstract():
    assert not inspect.isabstract(C_Commands_DefaultOption)


def test_c_commands_defaultoption_constructor_exists():
    assert callable(C_Commands_DefaultOption.__init__)


def test_c_commands_defaultoption_constructor_args():
    sig = inspect.signature(C_Commands_DefaultOption.__init__)
    params = list(sig.parameters.keys())



def test_c_commands_caseoption_is_not_abstract():
    assert not inspect.isabstract(C_Commands_CaseOption)


def test_c_commands_caseoption_constructor_exists():
    assert callable(C_Commands_CaseOption.__init__)


def test_c_commands_caseoption_constructor_args():
    sig = inspect.signature(C_Commands_CaseOption.__init__)
    params = list(sig.parameters.keys())



def test_commands_defaultoption_is_not_abstract():
    assert not inspect.isabstract(Commands_DefaultOption)


def test_commands_defaultoption_constructor_exists():
    assert callable(Commands_DefaultOption.__init__)


def test_commands_defaultoption_constructor_args():
    sig = inspect.signature(Commands_DefaultOption.__init__)
    params = list(sig.parameters.keys())



def test_commands_caseoption_is_not_abstract():
    assert not inspect.isabstract(Commands_CaseOption)


def test_commands_caseoption_constructor_exists():
    assert callable(Commands_CaseOption.__init__)


def test_commands_caseoption_constructor_args():
    sig = inspect.signature(Commands_CaseOption.__init__)
    params = list(sig.parameters.keys())



def test_expressions_variableaccess_is_not_abstract():
    assert not inspect.isabstract(Expressions_VariableAccess)


def test_expressions_variableaccess_constructor_exists():
    assert callable(Expressions_VariableAccess.__init__)


def test_expressions_variableaccess_constructor_args():
    sig = inspect.signature(Expressions_VariableAccess.__init__)
    params = list(sig.parameters.keys())



def test_expressions_conditionalexpression_is_not_abstract():
    assert not inspect.isabstract(Expressions_ConditionalExpression)


def test_expressions_conditionalexpression_constructor_exists():
    assert callable(Expressions_ConditionalExpression.__init__)


def test_expressions_conditionalexpression_constructor_args():
    sig = inspect.signature(Expressions_ConditionalExpression.__init__)
    params = list(sig.parameters.keys())



def test_decisioncommand_is_not_abstract():
    assert not inspect.isabstract(DecisionCommand)


def test_decisioncommand_constructor_exists():
    assert callable(DecisionCommand.__init__)


def test_decisioncommand_constructor_args():
    sig = inspect.signature(DecisionCommand.__init__)
    params = list(sig.parameters.keys())



def test_c_commands_switchcommand_is_not_abstract():
    assert not inspect.isabstract(C_Commands_SwitchCommand)


def test_c_commands_switchcommand_constructor_exists():
    assert callable(C_Commands_SwitchCommand.__init__)


def test_c_commands_switchcommand_constructor_args():
    sig = inspect.signature(C_Commands_SwitchCommand.__init__)
    params = list(sig.parameters.keys())



def test_c_commands_ifcommand_is_not_abstract():
    assert not inspect.isabstract(C_Commands_IfCommand)


def test_c_commands_ifcommand_constructor_exists():
    assert callable(C_Commands_IfCommand.__init__)


def test_c_commands_ifcommand_constructor_args():
    sig = inspect.signature(C_Commands_IfCommand.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_c_expressions_logicexpression_is_not_abstract():
    assert not inspect.isabstract(C_Expressions_LogicExpression)


def test_c_expressions_logicexpression_constructor_exists():
    assert callable(C_Expressions_LogicExpression.__init__)


def test_c_expressions_logicexpression_constructor_args():
    sig = inspect.signature(C_Expressions_LogicExpression.__init__)
    params = list(sig.parameters.keys())



def test_c_expressions_arithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(C_Expressions_ArithmeticExpression)


def test_c_expressions_arithmeticexpression_constructor_exists():
    assert callable(C_Expressions_ArithmeticExpression.__init__)


def test_c_expressions_arithmeticexpression_constructor_args():
    sig = inspect.signature(C_Expressions_ArithmeticExpression.__init__)
    params = list(sig.parameters.keys())



def test_c_expressions_literal_is_not_abstract():
    assert not inspect.isabstract(C_Expressions_Literal)


def test_c_expressions_literal_constructor_exists():
    assert callable(C_Expressions_Literal.__init__)


def test_c_expressions_literal_constructor_args():
    sig = inspect.signature(C_Expressions_Literal.__init__)
    params = list(sig.parameters.keys())



def test_c_expressions_conditionalexpression_is_not_abstract():
    assert not inspect.isabstract(C_Expressions_ConditionalExpression)


def test_c_expressions_conditionalexpression_constructor_exists():
    assert callable(C_Expressions_ConditionalExpression.__init__)


def test_c_expressions_conditionalexpression_constructor_args():
    sig = inspect.signature(C_Expressions_ConditionalExpression.__init__)
    params = list(sig.parameters.keys())
    assert "conector" in params, "Missing parameter 'conector'"

def test_c_expressions_conditionalexpression_has_conector():
    assert hasattr(C_Expressions_ConditionalExpression, "conector")
    descriptor = None
    for klass in C_Expressions_ConditionalExpression.__mro__:
        if "conector" in klass.__dict__:
            descriptor = klass.__dict__["conector"]
            break
    assert isinstance(descriptor, property)



def test_c_expressions_constantexpression_is_not_abstract():
    assert not inspect.isabstract(C_Expressions_ConstantExpression)


def test_c_expressions_constantexpression_constructor_exists():
    assert callable(C_Expressions_ConstantExpression.__init__)


def test_c_expressions_constantexpression_constructor_args():
    sig = inspect.signature(C_Expressions_ConstantExpression.__init__)
    params = list(sig.parameters.keys())



def test_c_expressions_castexpression_is_not_abstract():
    assert not inspect.isabstract(C_Expressions_CastExpression)


def test_c_expressions_castexpression_constructor_exists():
    assert callable(C_Expressions_CastExpression.__init__)


def test_c_expressions_castexpression_constructor_args():
    sig = inspect.signature(C_Expressions_CastExpression.__init__)
    params = list(sig.parameters.keys())



def test_c_expressions_construction_is_not_abstract():
    assert not inspect.isabstract(C_Expressions_Construction)


def test_c_expressions_construction_constructor_exists():
    assert callable(C_Expressions_Construction.__init__)


def test_c_expressions_construction_constructor_args():
    sig = inspect.signature(C_Expressions_Construction.__init__)
    params = list(sig.parameters.keys())



def test_c_expressions_expression_is_not_abstract():
    assert not inspect.isabstract(C_Expressions_Expression)


def test_c_expressions_expression_constructor_exists():
    assert callable(C_Expressions_Expression.__init__)


def test_c_expressions_expression_constructor_args():
    sig = inspect.signature(C_Expressions_Expression.__init__)
    params = list(sig.parameters.keys())



def test_c_commands_whilecommand_is_not_abstract():
    assert not inspect.isabstract(C_Commands_WhileCommand)


def test_c_commands_whilecommand_constructor_exists():
    assert callable(C_Commands_WhileCommand.__init__)


def test_c_commands_whilecommand_constructor_args():
    sig = inspect.signature(C_Commands_WhileCommand.__init__)
    params = list(sig.parameters.keys())



def test_blockedelement_is_not_abstract():
    assert not inspect.isabstract(BlockedElement)


def test_blockedelement_constructor_exists():
    assert callable(BlockedElement.__init__)


def test_blockedelement_constructor_args():
    sig = inspect.signature(BlockedElement.__init__)
    params = list(sig.parameters.keys())



def test_c_sequencers_sequencer_is_not_abstract():
    assert not inspect.isabstract(C_Sequencers_Sequencer)


def test_c_sequencers_sequencer_constructor_exists():
    assert callable(C_Sequencers_Sequencer.__init__)


def test_c_sequencers_sequencer_constructor_args():
    sig = inspect.signature(C_Sequencers_Sequencer.__init__)
    params = list(sig.parameters.keys())



def test_c_commands_command_is_not_abstract():
    assert not inspect.isabstract(C_Commands_Command)


def test_c_commands_command_constructor_exists():
    assert callable(C_Commands_Command.__init__)


def test_c_commands_command_constructor_args():
    sig = inspect.signature(C_Commands_Command.__init__)
    params = list(sig.parameters.keys())



def test_c_compilationdirectivedeclarations_endif_is_not_abstract():
    assert not inspect.isabstract(C_CompilationDirectiveDeclarations_Endif)


def test_c_compilationdirectivedeclarations_endif_constructor_exists():
    assert callable(C_CompilationDirectiveDeclarations_Endif.__init__)


def test_c_compilationdirectivedeclarations_endif_constructor_args():
    sig = inspect.signature(C_CompilationDirectiveDeclarations_Endif.__init__)
    params = list(sig.parameters.keys())



def test_ifdirective_is_not_abstract():
    assert not inspect.isabstract(IfDirective)


def test_ifdirective_constructor_exists():
    assert callable(IfDirective.__init__)


def test_ifdirective_constructor_args():
    sig = inspect.signature(IfDirective.__init__)
    params = list(sig.parameters.keys())



def test_c_compilationdirectivedeclarations_elif_is_not_abstract():
    assert not inspect.isabstract(C_CompilationDirectiveDeclarations_Elif)


def test_c_compilationdirectivedeclarations_elif_constructor_exists():
    assert callable(C_CompilationDirectiveDeclarations_Elif.__init__)


def test_c_compilationdirectivedeclarations_elif_constructor_args():
    sig = inspect.signature(C_CompilationDirectiveDeclarations_Elif.__init__)
    params = list(sig.parameters.keys())



def test_expressions_constantexpression_is_not_abstract():
    assert not inspect.isabstract(Expressions_ConstantExpression)


def test_expressions_constantexpression_constructor_exists():
    assert callable(Expressions_ConstantExpression.__init__)


def test_expressions_constantexpression_constructor_args():
    sig = inspect.signature(Expressions_ConstantExpression.__init__)
    params = list(sig.parameters.keys())



def test_complexdirectivedeclaration_is_not_abstract():
    assert not inspect.isabstract(ComplexDirectiveDeclaration)


def test_complexdirectivedeclaration_constructor_exists():
    assert callable(ComplexDirectiveDeclaration.__init__)


def test_complexdirectivedeclaration_constructor_args():
    sig = inspect.signature(ComplexDirectiveDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_c_compilationdirectivedeclarations_ifdirective_is_not_abstract():
    assert not inspect.isabstract(C_CompilationDirectiveDeclarations_IfDirective)


def test_c_compilationdirectivedeclarations_ifdirective_constructor_exists():
    assert callable(C_CompilationDirectiveDeclarations_IfDirective.__init__)


def test_c_compilationdirectivedeclarations_ifdirective_constructor_args():
    sig = inspect.signature(C_CompilationDirectiveDeclarations_IfDirective.__init__)
    params = list(sig.parameters.keys())



def test_c_compilationdirectivedeclarations_elsedirective_is_not_abstract():
    assert not inspect.isabstract(C_CompilationDirectiveDeclarations_ElseDirective)


def test_c_compilationdirectivedeclarations_elsedirective_constructor_exists():
    assert callable(C_CompilationDirectiveDeclarations_ElseDirective.__init__)


def test_c_compilationdirectivedeclarations_elsedirective_constructor_args():
    sig = inspect.signature(C_CompilationDirectiveDeclarations_ElseDirective.__init__)
    params = list(sig.parameters.keys())



def test_c_compilationdirectivedeclarations_ifndef_is_not_abstract():
    assert not inspect.isabstract(C_CompilationDirectiveDeclarations_Ifndef)


def test_c_compilationdirectivedeclarations_ifndef_constructor_exists():
    assert callable(C_CompilationDirectiveDeclarations_Ifndef.__init__)


def test_c_compilationdirectivedeclarations_ifndef_constructor_args():
    sig = inspect.signature(C_CompilationDirectiveDeclarations_Ifndef.__init__)
    params = list(sig.parameters.keys())



def test_compilationdirectivedeclarations_endif_is_not_abstract():
    assert not inspect.isabstract(CompilationDirectiveDeclarations_Endif)


def test_compilationdirectivedeclarations_endif_constructor_exists():
    assert callable(CompilationDirectiveDeclarations_Endif.__init__)


def test_compilationdirectivedeclarations_endif_constructor_args():
    sig = inspect.signature(CompilationDirectiveDeclarations_Endif.__init__)
    params = list(sig.parameters.keys())



def test_compilationdirectivedeclarations_complexdirectivedeclaration_is_not_abstract():
    assert not inspect.isabstract(CompilationDirectiveDeclarations_ComplexDirectiveDeclaration)


def test_compilationdirectivedeclarations_complexdirectivedeclaration_constructor_exists():
    assert callable(CompilationDirectiveDeclarations_ComplexDirectiveDeclaration.__init__)


def test_compilationdirectivedeclarations_complexdirectivedeclaration_constructor_args():
    sig = inspect.signature(CompilationDirectiveDeclarations_ComplexDirectiveDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_simpledirectivedeclaration_is_not_abstract():
    assert not inspect.isabstract(SimpleDirectiveDeclaration)


def test_simpledirectivedeclaration_constructor_exists():
    assert callable(SimpleDirectiveDeclaration.__init__)


def test_simpledirectivedeclaration_constructor_args():
    sig = inspect.signature(SimpleDirectiveDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_c_compilationdirectivedeclarations_include_is_not_abstract():
    assert not inspect.isabstract(C_CompilationDirectiveDeclarations_Include)


def test_c_compilationdirectivedeclarations_include_constructor_exists():
    assert callable(C_CompilationDirectiveDeclarations_Include.__init__)


def test_c_compilationdirectivedeclarations_include_constructor_args():
    sig = inspect.signature(C_CompilationDirectiveDeclarations_Include.__init__)
    params = list(sig.parameters.keys())



def test_c_compilationdirectivedeclarations_define_is_not_abstract():
    assert not inspect.isabstract(C_CompilationDirectiveDeclarations_Define)


def test_c_compilationdirectivedeclarations_define_constructor_exists():
    assert callable(C_CompilationDirectiveDeclarations_Define.__init__)


def test_c_compilationdirectivedeclarations_define_constructor_args():
    sig = inspect.signature(C_CompilationDirectiveDeclarations_Define.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_c_compilationdirectivedeclarations_define_has_value():
    assert hasattr(C_CompilationDirectiveDeclarations_Define, "value")
    descriptor = None
    for klass in C_CompilationDirectiveDeclarations_Define.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_compilationdirectivedeclaration_is_not_abstract():
    assert not inspect.isabstract(CompilationDirectiveDeclaration)


def test_compilationdirectivedeclaration_constructor_exists():
    assert callable(CompilationDirectiveDeclaration.__init__)


def test_compilationdirectivedeclaration_constructor_args():
    sig = inspect.signature(CompilationDirectiveDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_c_compilationdirectivedeclarations_complexdirectivedeclaration_is_not_abstract():
    assert not inspect.isabstract(C_CompilationDirectiveDeclarations_ComplexDirectiveDeclaration)


def test_c_compilationdirectivedeclarations_complexdirectivedeclaration_constructor_exists():
    assert callable(C_CompilationDirectiveDeclarations_ComplexDirectiveDeclaration.__init__)


def test_c_compilationdirectivedeclarations_complexdirectivedeclaration_constructor_args():
    sig = inspect.signature(C_CompilationDirectiveDeclarations_ComplexDirectiveDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_c_compilationdirectivedeclarations_compilationdirectivedeclaration_is_not_abstract():
    assert not inspect.isabstract(C_CompilationDirectiveDeclarations_CompilationDirectiveDeclaration)


def test_c_compilationdirectivedeclarations_compilationdirectivedeclaration_constructor_exists():
    assert callable(C_CompilationDirectiveDeclarations_CompilationDirectiveDeclaration.__init__)


def test_c_compilationdirectivedeclarations_compilationdirectivedeclaration_constructor_args():
    sig = inspect.signature(C_CompilationDirectiveDeclarations_CompilationDirectiveDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_declarations_simplevariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(Declarations_SimpleVariableDeclaration)


def test_declarations_simplevariabledeclaration_constructor_exists():
    assert callable(Declarations_SimpleVariableDeclaration.__init__)


def test_declarations_simplevariabledeclaration_constructor_args():
    sig = inspect.signature(Declarations_SimpleVariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_flowcontrolcommand_is_not_abstract():
    assert not inspect.isabstract(FlowControlCommand)


def test_flowcontrolcommand_constructor_exists():
    assert callable(FlowControlCommand.__init__)


def test_flowcontrolcommand_constructor_args():
    sig = inspect.signature(FlowControlCommand.__init__)
    params = list(sig.parameters.keys())



def test_c_commands_returncommand_is_not_abstract():
    assert not inspect.isabstract(C_Commands_ReturnCommand)


def test_c_commands_returncommand_constructor_exists():
    assert callable(C_Commands_ReturnCommand.__init__)


def test_c_commands_returncommand_constructor_args():
    sig = inspect.signature(C_Commands_ReturnCommand.__init__)
    params = list(sig.parameters.keys())



def test_c_commands_decisioncommand_is_not_abstract():
    assert not inspect.isabstract(C_Commands_DecisionCommand)


def test_c_commands_decisioncommand_constructor_exists():
    assert callable(C_Commands_DecisionCommand.__init__)


def test_c_commands_decisioncommand_constructor_args():
    sig = inspect.signature(C_Commands_DecisionCommand.__init__)
    params = list(sig.parameters.keys())



def test_expressions_access_is_not_abstract():
    assert not inspect.isabstract(Expressions_Access)


def test_expressions_access_constructor_exists():
    assert callable(Expressions_Access.__init__)


def test_expressions_access_constructor_args():
    sig = inspect.signature(Expressions_Access.__init__)
    params = list(sig.parameters.keys())



def test_command_is_not_abstract():
    assert not inspect.isabstract(Command)


def test_command_constructor_exists():
    assert callable(Command.__init__)


def test_command_constructor_args():
    sig = inspect.signature(Command.__init__)
    params = list(sig.parameters.keys())



def test_c_commands_flowcontrolcommand_is_not_abstract():
    assert not inspect.isabstract(C_Commands_FlowControlCommand)


def test_c_commands_flowcontrolcommand_constructor_exists():
    assert callable(C_Commands_FlowControlCommand.__init__)


def test_c_commands_flowcontrolcommand_constructor_args():
    sig = inspect.signature(C_Commands_FlowControlCommand.__init__)
    params = list(sig.parameters.keys())



def test_c_commands_iterativecommand_is_not_abstract():
    assert not inspect.isabstract(C_Commands_IterativeCommand)


def test_c_commands_iterativecommand_constructor_exists():
    assert callable(C_Commands_IterativeCommand.__init__)


def test_c_commands_iterativecommand_constructor_args():
    sig = inspect.signature(C_Commands_IterativeCommand.__init__)
    params = list(sig.parameters.keys())



def test_c_commands_expressioncommand_is_not_abstract():
    assert not inspect.isabstract(C_Commands_ExpressionCommand)


def test_c_commands_expressioncommand_constructor_exists():
    assert callable(C_Commands_ExpressionCommand.__init__)


def test_c_commands_expressioncommand_constructor_args():
    sig = inspect.signature(C_Commands_ExpressionCommand.__init__)
    params = list(sig.parameters.keys())



def test_c_commands_assignment_is_not_abstract():
    assert not inspect.isabstract(C_Commands_Assignment)


def test_c_commands_assignment_constructor_exists():
    assert callable(C_Commands_Assignment.__init__)


def test_c_commands_assignment_constructor_args():
    sig = inspect.signature(C_Commands_Assignment.__init__)
    params = list(sig.parameters.keys())



def test_commands_command_is_not_abstract():
    assert not inspect.isabstract(Commands_Command)


def test_commands_command_constructor_exists():
    assert callable(Commands_Command.__init__)


def test_commands_command_constructor_args():
    sig = inspect.signature(Commands_Command.__init__)
    params = list(sig.parameters.keys())



def test_declarations_fragmentvariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(Declarations_FragmentVariableDeclaration)


def test_declarations_fragmentvariabledeclaration_constructor_exists():
    assert callable(Declarations_FragmentVariableDeclaration.__init__)


def test_declarations_fragmentvariabledeclaration_constructor_args():
    sig = inspect.signature(Declarations_FragmentVariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_declarations_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(Declarations_VariableDeclaration)


def test_declarations_variabledeclaration_constructor_exists():
    assert callable(Declarations_VariableDeclaration.__init__)


def test_declarations_variabledeclaration_constructor_args():
    sig = inspect.signature(Declarations_VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_expressions_expression_is_not_abstract():
    assert not inspect.isabstract(Expressions_Expression)


def test_expressions_expression_constructor_exists():
    assert callable(Expressions_Expression.__init__)


def test_expressions_expression_constructor_args():
    sig = inspect.signature(Expressions_Expression.__init__)
    params = list(sig.parameters.keys())



def test_declaration_is_not_abstract():
    assert not inspect.isabstract(Declaration)


def test_declaration_constructor_exists():
    assert callable(Declaration.__init__)


def test_declaration_constructor_args():
    sig = inspect.signature(Declaration.__init__)
    params = list(sig.parameters.keys())



def test_c_declarations_prototypefunctiondeclaration_is_not_abstract():
    assert not inspect.isabstract(C_Declarations_PrototypeFunctionDeclaration)


def test_c_declarations_prototypefunctiondeclaration_constructor_exists():
    assert callable(C_Declarations_PrototypeFunctionDeclaration.__init__)


def test_c_declarations_prototypefunctiondeclaration_constructor_args():
    sig = inspect.signature(C_Declarations_PrototypeFunctionDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "isAPointer" in params, "Missing parameter 'isAPointer'"
    assert "functionModifier" in params, "Missing parameter 'functionModifier'"

def test_c_declarations_prototypefunctiondeclaration_has_isAPointer():
    assert hasattr(C_Declarations_PrototypeFunctionDeclaration, "isAPointer")
    descriptor = None
    for klass in C_Declarations_PrototypeFunctionDeclaration.__mro__:
        if "isAPointer" in klass.__dict__:
            descriptor = klass.__dict__["isAPointer"]
            break
    assert isinstance(descriptor, property)

def test_c_declarations_prototypefunctiondeclaration_has_functionModifier():
    assert hasattr(C_Declarations_PrototypeFunctionDeclaration, "functionModifier")
    descriptor = None
    for klass in C_Declarations_PrototypeFunctionDeclaration.__mro__:
        if "functionModifier" in klass.__dict__:
            descriptor = klass.__dict__["functionModifier"]
            break
    assert isinstance(descriptor, property)



def test_c_declarations_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(C_Declarations_VariableDeclaration)


def test_c_declarations_variabledeclaration_constructor_exists():
    assert callable(C_Declarations_VariableDeclaration.__init__)


def test_c_declarations_variabledeclaration_constructor_args():
    sig = inspect.signature(C_Declarations_VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "numberOfPointers" in params, "Missing parameter 'numberOfPointers'"
    assert "isAPointer" in params, "Missing parameter 'isAPointer'"

def test_c_declarations_variabledeclaration_has_numberOfPointers():
    assert hasattr(C_Declarations_VariableDeclaration, "numberOfPointers")
    descriptor = None
    for klass in C_Declarations_VariableDeclaration.__mro__:
        if "numberOfPointers" in klass.__dict__:
            descriptor = klass.__dict__["numberOfPointers"]
            break
    assert isinstance(descriptor, property)

def test_c_declarations_variabledeclaration_has_isAPointer():
    assert hasattr(C_Declarations_VariableDeclaration, "isAPointer")
    descriptor = None
    for klass in C_Declarations_VariableDeclaration.__mro__:
        if "isAPointer" in klass.__dict__:
            descriptor = klass.__dict__["isAPointer"]
            break
    assert isinstance(descriptor, property)



def test_c_declarations_constantdeclaration_is_not_abstract():
    assert not inspect.isabstract(C_Declarations_ConstantDeclaration)


def test_c_declarations_constantdeclaration_constructor_exists():
    assert callable(C_Declarations_ConstantDeclaration.__init__)


def test_c_declarations_constantdeclaration_constructor_args():
    sig = inspect.signature(C_Declarations_ConstantDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_main_function_is_not_abstract():
    assert not inspect.isabstract(Main_Function)


def test_main_function_constructor_exists():
    assert callable(Main_Function.__init__)


def test_main_function_constructor_args():
    sig = inspect.signature(Main_Function.__init__)
    params = list(sig.parameters.keys())



def test_compilationdirectivedeclarations_compilationdirectivedeclaration_is_not_abstract():
    assert not inspect.isabstract(CompilationDirectiveDeclarations_CompilationDirectiveDeclaration)


def test_compilationdirectivedeclarations_compilationdirectivedeclaration_constructor_exists():
    assert callable(CompilationDirectiveDeclarations_CompilationDirectiveDeclaration.__init__)


def test_compilationdirectivedeclarations_compilationdirectivedeclaration_constructor_args():
    sig = inspect.signature(CompilationDirectiveDeclarations_CompilationDirectiveDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_expressions_construction_is_not_abstract():
    assert not inspect.isabstract(Expressions_Construction)


def test_expressions_construction_constructor_exists():
    assert callable(Expressions_Construction.__init__)


def test_expressions_construction_constructor_args():
    sig = inspect.signature(Expressions_Construction.__init__)
    params = list(sig.parameters.keys())



def test_declarations_compositevariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(Declarations_CompositeVariableDeclaration)


def test_declarations_compositevariabledeclaration_constructor_exists():
    assert callable(Declarations_CompositeVariableDeclaration.__init__)


def test_declarations_compositevariabledeclaration_constructor_args():
    sig = inspect.signature(Declarations_CompositeVariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_expressions_literal_is_not_abstract():
    assert not inspect.isabstract(Expressions_Literal)


def test_expressions_literal_constructor_exists():
    assert callable(Expressions_Literal.__init__)


def test_expressions_literal_constructor_args():
    sig = inspect.signature(Expressions_Literal.__init__)
    params = list(sig.parameters.keys())



def test_compositevariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(CompositeVariableDeclaration)


def test_compositevariabledeclaration_constructor_exists():
    assert callable(CompositeVariableDeclaration.__init__)


def test_compositevariabledeclaration_constructor_args():
    sig = inspect.signature(CompositeVariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_c_declarations_structdeclaration_is_not_abstract():
    assert not inspect.isabstract(C_Declarations_StructDeclaration)


def test_c_declarations_structdeclaration_constructor_exists():
    assert callable(C_Declarations_StructDeclaration.__init__)


def test_c_declarations_structdeclaration_constructor_args():
    sig = inspect.signature(C_Declarations_StructDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_c_declarations_typedefdeclaration_is_not_abstract():
    assert not inspect.isabstract(C_Declarations_TypeDefDeclaration)


def test_c_declarations_typedefdeclaration_constructor_exists():
    assert callable(C_Declarations_TypeDefDeclaration.__init__)


def test_c_declarations_typedefdeclaration_constructor_args():
    sig = inspect.signature(C_Declarations_TypeDefDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_c_declarations_enumdeclaration_is_not_abstract():
    assert not inspect.isabstract(C_Declarations_EnumDeclaration)


def test_c_declarations_enumdeclaration_constructor_exists():
    assert callable(C_Declarations_EnumDeclaration.__init__)


def test_c_declarations_enumdeclaration_constructor_args():
    sig = inspect.signature(C_Declarations_EnumDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(VariableDeclaration)


def test_variabledeclaration_constructor_exists():
    assert callable(VariableDeclaration.__init__)


def test_variabledeclaration_constructor_args():
    sig = inspect.signature(VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_c_declarations_compositevariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(C_Declarations_CompositeVariableDeclaration)


def test_c_declarations_compositevariabledeclaration_constructor_exists():
    assert callable(C_Declarations_CompositeVariableDeclaration.__init__)


def test_c_declarations_compositevariabledeclaration_constructor_args():
    sig = inspect.signature(C_Declarations_CompositeVariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_main_element_is_not_abstract():
    assert not inspect.isabstract(Main_Element)


def test_main_element_constructor_exists():
    assert callable(Main_Element.__init__)


def test_main_element_constructor_args():
    sig = inspect.signature(Main_Element.__init__)
    params = list(sig.parameters.keys())



def test_unit_is_not_abstract():
    assert not inspect.isabstract(Unit)


def test_unit_constructor_exists():
    assert callable(Unit.__init__)


def test_unit_constructor_args():
    sig = inspect.signature(Unit.__init__)
    params = list(sig.parameters.keys())



def test_c_main_c_unit_is_not_abstract():
    assert not inspect.isabstract(C_Main_C_Unit)


def test_c_main_c_unit_constructor_exists():
    assert callable(C_Main_C_Unit.__init__)


def test_c_main_c_unit_constructor_args():
    sig = inspect.signature(C_Main_C_Unit.__init__)
    params = list(sig.parameters.keys())



def test_main_comment_is_not_abstract():
    assert not inspect.isabstract(Main_Comment)


def test_main_comment_constructor_exists():
    assert callable(Main_Comment.__init__)


def test_main_comment_constructor_args():
    sig = inspect.signature(Main_Comment.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_c_declarations_declaration_is_not_abstract():
    assert not inspect.isabstract(C_Declarations_Declaration)


def test_c_declarations_declaration_constructor_exists():
    assert callable(C_Declarations_Declaration.__init__)


def test_c_declarations_declaration_constructor_args():
    sig = inspect.signature(C_Declarations_Declaration.__init__)
    params = list(sig.parameters.keys())
    assert "modifier" in params, "Missing parameter 'modifier'"

def test_c_declarations_declaration_has_modifier():
    assert hasattr(C_Declarations_Declaration, "modifier")
    descriptor = None
    for klass in C_Declarations_Declaration.__mro__:
        if "modifier" in klass.__dict__:
            descriptor = klass.__dict__["modifier"]
            break
    assert isinstance(descriptor, property)



def test_c_main_comment_is_not_abstract():
    assert not inspect.isabstract(C_Main_Comment)


def test_c_main_comment_constructor_exists():
    assert callable(C_Main_Comment.__init__)


def test_c_main_comment_constructor_args():
    sig = inspect.signature(C_Main_Comment.__init__)
    params = list(sig.parameters.keys())



def test_c_main_element_is_not_abstract():
    assert not inspect.isabstract(C_Main_Element)


def test_c_main_element_constructor_exists():
    assert callable(C_Main_Element.__init__)


def test_c_main_element_constructor_args():
    sig = inspect.signature(C_Main_Element.__init__)
    params = list(sig.parameters.keys())



def test_c_main_unit_is_not_abstract():
    assert not inspect.isabstract(C_Main_Unit)


def test_c_main_unit_constructor_exists():
    assert callable(C_Main_Unit.__init__)


def test_c_main_unit_constructor_args():
    sig = inspect.signature(C_Main_Unit.__init__)
    params = list(sig.parameters.keys())



def test_main_unit_is_not_abstract():
    assert not inspect.isabstract(Main_Unit)


def test_main_unit_constructor_exists():
    assert callable(Main_Unit.__init__)


def test_main_unit_constructor_args():
    sig = inspect.signature(Main_Unit.__init__)
    params = list(sig.parameters.keys())



def test_c_main_program_is_not_abstract():
    assert not inspect.isabstract(C_Main_Program)


def test_c_main_program_constructor_exists():
    assert callable(C_Main_Program.__init__)


def test_c_main_program_constructor_args():
    sig = inspect.signature(C_Main_Program.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_c_main_program_has_description():
    assert hasattr(C_Main_Program, "description")
    descriptor = None
    for klass in C_Main_Program.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_main_block_is_not_abstract():
    assert not inspect.isabstract(Main_Block)


def test_main_block_constructor_exists():
    assert callable(Main_Block.__init__)


def test_main_block_constructor_args():
    sig = inspect.signature(Main_Block.__init__)
    params = list(sig.parameters.keys())



def test_c_abstractions_blockedelement_is_not_abstract():
    assert not inspect.isabstract(C_Abstractions_BlockedElement)


def test_c_abstractions_blockedelement_constructor_exists():
    assert callable(C_Abstractions_BlockedElement.__init__)


def test_c_abstractions_blockedelement_constructor_args():
    sig = inspect.signature(C_Abstractions_BlockedElement.__init__)
    params = list(sig.parameters.keys())



def test_c_abstractions_namedelement_is_not_abstract():
    assert not inspect.isabstract(C_Abstractions_NamedElement)


def test_c_abstractions_namedelement_constructor_exists():
    assert callable(C_Abstractions_NamedElement.__init__)


def test_c_abstractions_namedelement_constructor_args():
    sig = inspect.signature(C_Abstractions_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_c_abstractions_namedelement_has_name():
    assert hasattr(C_Abstractions_NamedElement, "name")
    descriptor = None
    for klass in C_Abstractions_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_abstractions_namedelement_is_not_abstract():
    assert not inspect.isabstract(Abstractions_NamedElement)


def test_abstractions_namedelement_constructor_exists():
    assert callable(Abstractions_NamedElement.__init__)


def test_abstractions_namedelement_constructor_args():
    sig = inspect.signature(Abstractions_NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_c_expressions_atomicconditionalexpression_is_not_abstract():
    assert not inspect.isabstract(C_Expressions_AtomicConditionalExpression)


def test_c_expressions_atomicconditionalexpression_constructor_exists():
    assert callable(C_Expressions_AtomicConditionalExpression.__init__)


def test_c_expressions_atomicconditionalexpression_constructor_args():
    sig = inspect.signature(C_Expressions_AtomicConditionalExpression.__init__)
    params = list(sig.parameters.keys())



def test_c_expressions_functioncall_is_not_abstract():
    assert not inspect.isabstract(C_Expressions_FunctionCall)


def test_c_expressions_functioncall_constructor_exists():
    assert callable(C_Expressions_FunctionCall.__init__)


def test_c_expressions_functioncall_constructor_args():
    sig = inspect.signature(C_Expressions_FunctionCall.__init__)
    params = list(sig.parameters.keys())



def test_c_compilationdirectivedeclarations_ifdef_is_not_abstract():
    assert not inspect.isabstract(C_CompilationDirectiveDeclarations_Ifdef)


def test_c_compilationdirectivedeclarations_ifdef_constructor_exists():
    assert callable(C_CompilationDirectiveDeclarations_Ifdef.__init__)


def test_c_compilationdirectivedeclarations_ifdef_constructor_args():
    sig = inspect.signature(C_CompilationDirectiveDeclarations_Ifdef.__init__)
    params = list(sig.parameters.keys())



def test_c_declarations_fragmentvariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(C_Declarations_FragmentVariableDeclaration)


def test_c_declarations_fragmentvariabledeclaration_constructor_exists():
    assert callable(C_Declarations_FragmentVariableDeclaration.__init__)


def test_c_declarations_fragmentvariabledeclaration_constructor_args():
    sig = inspect.signature(C_Declarations_FragmentVariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_c_commands_labelcommand_is_not_abstract():
    assert not inspect.isabstract(C_Commands_LabelCommand)


def test_c_commands_labelcommand_constructor_exists():
    assert callable(C_Commands_LabelCommand.__init__)


def test_c_commands_labelcommand_constructor_args():
    sig = inspect.signature(C_Commands_LabelCommand.__init__)
    params = list(sig.parameters.keys())



def test_c_expressions_access_is_not_abstract():
    assert not inspect.isabstract(C_Expressions_Access)


def test_c_expressions_access_constructor_exists():
    assert callable(C_Expressions_Access.__init__)


def test_c_expressions_access_constructor_args():
    sig = inspect.signature(C_Expressions_Access.__init__)
    params = list(sig.parameters.keys())



def test_c_compilationdirectivedeclarations_simpledirectivedeclaration_is_not_abstract():
    assert not inspect.isabstract(C_CompilationDirectiveDeclarations_SimpleDirectiveDeclaration)


def test_c_compilationdirectivedeclarations_simpledirectivedeclaration_constructor_exists():
    assert callable(C_CompilationDirectiveDeclarations_SimpleDirectiveDeclaration.__init__)


def test_c_compilationdirectivedeclarations_simpledirectivedeclaration_constructor_args():
    sig = inspect.signature(C_CompilationDirectiveDeclarations_SimpleDirectiveDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_types_type_is_not_abstract():
    assert not inspect.isabstract(Types_Type)


def test_types_type_constructor_exists():
    assert callable(Types_Type.__init__)


def test_types_type_constructor_args():
    sig = inspect.signature(Types_Type.__init__)
    params = list(sig.parameters.keys())



def test_c_types_fromheader_is_not_abstract():
    assert not inspect.isabstract(C_Types_FromHeader)


def test_c_types_fromheader_constructor_exists():
    assert callable(C_Types_FromHeader.__init__)


def test_c_types_fromheader_constructor_args():
    sig = inspect.signature(C_Types_FromHeader.__init__)
    params = list(sig.parameters.keys())



def test_compositetype_is_not_abstract():
    assert not inspect.isabstract(CompositeType)


def test_compositetype_constructor_exists():
    assert callable(CompositeType.__init__)


def test_compositetype_constructor_args():
    sig = inspect.signature(CompositeType.__init__)
    params = list(sig.parameters.keys())



def test_c_types_enum_is_not_abstract():
    assert not inspect.isabstract(C_Types_Enum)


def test_c_types_enum_constructor_exists():
    assert callable(C_Types_Enum.__init__)


def test_c_types_enum_constructor_args():
    sig = inspect.signature(C_Types_Enum.__init__)
    params = list(sig.parameters.keys())



def test_c_types_struct_is_not_abstract():
    assert not inspect.isabstract(C_Types_Struct)


def test_c_types_struct_constructor_exists():
    assert callable(C_Types_Struct.__init__)


def test_c_types_struct_constructor_args():
    sig = inspect.signature(C_Types_Struct.__init__)
    params = list(sig.parameters.keys())



def test_c_types_array_is_not_abstract():
    assert not inspect.isabstract(C_Types_Array)


def test_c_types_array_constructor_exists():
    assert callable(C_Types_Array.__init__)


def test_c_types_array_constructor_args():
    sig = inspect.signature(C_Types_Array.__init__)
    params = list(sig.parameters.keys())



def test_c_types_typedef_is_not_abstract():
    assert not inspect.isabstract(C_Types_Typedef)


def test_c_types_typedef_constructor_exists():
    assert callable(C_Types_Typedef.__init__)


def test_c_types_typedef_constructor_args():
    sig = inspect.signature(C_Types_Typedef.__init__)
    params = list(sig.parameters.keys())



def test_types_array_is_not_abstract():
    assert not inspect.isabstract(Types_Array)


def test_types_array_constructor_exists():
    assert callable(Types_Array.__init__)


def test_types_array_constructor_args():
    sig = inspect.signature(Types_Array.__init__)
    params = list(sig.parameters.keys())



def test_types_primitivetype_is_not_abstract():
    assert not inspect.isabstract(Types_PrimitiveType)


def test_types_primitivetype_constructor_exists():
    assert callable(Types_PrimitiveType.__init__)


def test_types_primitivetype_constructor_args():
    sig = inspect.signature(Types_PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_c_types_int_is_not_abstract():
    assert not inspect.isabstract(C_Types_Int)


def test_c_types_int_constructor_exists():
    assert callable(C_Types_Int.__init__)


def test_c_types_int_constructor_args():
    sig = inspect.signature(C_Types_Int.__init__)
    params = list(sig.parameters.keys())



def test_primitivetype_is_not_abstract():
    assert not inspect.isabstract(PrimitiveType)


def test_primitivetype_constructor_exists():
    assert callable(PrimitiveType.__init__)


def test_primitivetype_constructor_args():
    sig = inspect.signature(PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_c_types_float_is_not_abstract():
    assert not inspect.isabstract(C_Types_Float)


def test_c_types_float_constructor_exists():
    assert callable(C_Types_Float.__init__)


def test_c_types_float_constructor_args():
    sig = inspect.signature(C_Types_Float.__init__)
    params = list(sig.parameters.keys())



def test_c_types_void_is_not_abstract():
    assert not inspect.isabstract(C_Types_Void)


def test_c_types_void_constructor_exists():
    assert callable(C_Types_Void.__init__)


def test_c_types_void_constructor_args():
    sig = inspect.signature(C_Types_Void.__init__)
    params = list(sig.parameters.keys())



def test_c_types_double_is_not_abstract():
    assert not inspect.isabstract(C_Types_Double)


def test_c_types_double_constructor_exists():
    assert callable(C_Types_Double.__init__)


def test_c_types_double_constructor_args():
    sig = inspect.signature(C_Types_Double.__init__)
    params = list(sig.parameters.keys())



def test_c_types_short_is_not_abstract():
    assert not inspect.isabstract(C_Types_Short)


def test_c_types_short_constructor_exists():
    assert callable(C_Types_Short.__init__)


def test_c_types_short_constructor_args():
    sig = inspect.signature(C_Types_Short.__init__)
    params = list(sig.parameters.keys())



def test_c_types_char_is_not_abstract():
    assert not inspect.isabstract(C_Types_Char)


def test_c_types_char_constructor_exists():
    assert callable(C_Types_Char.__init__)


def test_c_types_char_constructor_args():
    sig = inspect.signature(C_Types_Char.__init__)
    params = list(sig.parameters.keys())



def test_abstractions_blockedelement_is_not_abstract():
    assert not inspect.isabstract(Abstractions_BlockedElement)


def test_abstractions_blockedelement_constructor_exists():
    assert callable(Abstractions_BlockedElement.__init__)


def test_abstractions_blockedelement_constructor_args():
    sig = inspect.signature(Abstractions_BlockedElement.__init__)
    params = list(sig.parameters.keys())



def test_c_declarations_arraydeclaration_is_not_abstract():
    assert not inspect.isabstract(C_Declarations_ArrayDeclaration)


def test_c_declarations_arraydeclaration_constructor_exists():
    assert callable(C_Declarations_ArrayDeclaration.__init__)


def test_c_declarations_arraydeclaration_constructor_args():
    sig = inspect.signature(C_Declarations_ArrayDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "dimensions" in params, "Missing parameter 'dimensions'"

def test_c_declarations_arraydeclaration_has_dimensions():
    assert hasattr(C_Declarations_ArrayDeclaration, "dimensions")
    descriptor = None
    for klass in C_Declarations_ArrayDeclaration.__mro__:
        if "dimensions" in klass.__dict__:
            descriptor = klass.__dict__["dimensions"]
            break
    assert isinstance(descriptor, property)



def test_c_declarations_simplevariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(C_Declarations_SimpleVariableDeclaration)


def test_c_declarations_simplevariabledeclaration_constructor_exists():
    assert callable(C_Declarations_SimpleVariableDeclaration.__init__)


def test_c_declarations_simplevariabledeclaration_constructor_args():
    sig = inspect.signature(C_Declarations_SimpleVariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_c_main_block_is_not_abstract():
    assert not inspect.isabstract(C_Main_Block)


def test_c_main_block_constructor_exists():
    assert callable(C_Main_Block.__init__)


def test_c_main_block_constructor_args():
    sig = inspect.signature(C_Main_Block.__init__)
    params = list(sig.parameters.keys())



def test_declarations_declaration_is_not_abstract():
    assert not inspect.isabstract(Declarations_Declaration)


def test_declarations_declaration_constructor_exists():
    assert callable(Declarations_Declaration.__init__)


def test_declarations_declaration_constructor_args():
    sig = inspect.signature(Declarations_Declaration.__init__)
    params = list(sig.parameters.keys())



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_c_main_declarationsblock_is_not_abstract():
    assert not inspect.isabstract(C_Main_DeclarationsBlock)


def test_c_main_declarationsblock_constructor_exists():
    assert callable(C_Main_DeclarationsBlock.__init__)


def test_c_main_declarationsblock_constructor_args():
    sig = inspect.signature(C_Main_DeclarationsBlock.__init__)
    params = list(sig.parameters.keys())



def test_c_main_functionsblock_is_not_abstract():
    assert not inspect.isabstract(C_Main_FunctionsBlock)


def test_c_main_functionsblock_constructor_exists():
    assert callable(C_Main_FunctionsBlock.__init__)


def test_c_main_functionsblock_constructor_args():
    sig = inspect.signature(C_Main_FunctionsBlock.__init__)
    params = list(sig.parameters.keys())



def test_c_main_function_is_not_abstract():
    assert not inspect.isabstract(C_Main_Function)


def test_c_main_function_constructor_exists():
    assert callable(C_Main_Function.__init__)


def test_c_main_function_constructor_args():
    sig = inspect.signature(C_Main_Function.__init__)
    params = list(sig.parameters.keys())
    assert "functionModifier" in params, "Missing parameter 'functionModifier'"
    assert "modifier" in params, "Missing parameter 'modifier'"

def test_c_main_function_has_functionModifier():
    assert hasattr(C_Main_Function, "functionModifier")
    descriptor = None
    for klass in C_Main_Function.__mro__:
        if "functionModifier" in klass.__dict__:
            descriptor = klass.__dict__["functionModifier"]
            break
    assert isinstance(descriptor, property)

def test_c_main_function_has_modifier():
    assert hasattr(C_Main_Function, "modifier")
    descriptor = None
    for klass in C_Main_Function.__mro__:
        if "modifier" in klass.__dict__:
            descriptor = klass.__dict__["modifier"]
            break
    assert isinstance(descriptor, property)



def test_main_declarationsblock_is_not_abstract():
    assert not inspect.isabstract(Main_DeclarationsBlock)


def test_main_declarationsblock_constructor_exists():
    assert callable(Main_DeclarationsBlock.__init__)


def test_main_declarationsblock_constructor_args():
    sig = inspect.signature(Main_DeclarationsBlock.__init__)
    params = list(sig.parameters.keys())



def test_c_main_h_unit_is_not_abstract():
    assert not inspect.isabstract(C_Main_H_Unit)


def test_c_main_h_unit_constructor_exists():
    assert callable(C_Main_H_Unit.__init__)


def test_c_main_h_unit_constructor_args():
    sig = inspect.signature(C_Main_H_Unit.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_c_types_compositetype_is_not_abstract():
    assert not inspect.isabstract(C_Types_CompositeType)


def test_c_types_compositetype_constructor_exists():
    assert callable(C_Types_CompositeType.__init__)


def test_c_types_compositetype_constructor_args():
    sig = inspect.signature(C_Types_CompositeType.__init__)
    params = list(sig.parameters.keys())



def test_c_types_primitivetype_is_not_abstract():
    assert not inspect.isabstract(C_Types_PrimitiveType)


def test_c_types_primitivetype_constructor_exists():
    assert callable(C_Types_PrimitiveType.__init__)


def test_c_types_primitivetype_constructor_args():
    sig = inspect.signature(C_Types_PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_c_types_type_is_not_abstract():
    assert not inspect.isabstract(C_Types_Type)


def test_c_types_type_constructor_exists():
    assert callable(C_Types_Type.__init__)


def test_c_types_type_constructor_args():
    sig = inspect.signature(C_Types_Type.__init__)
    params = list(sig.parameters.keys())

def test_modifierkind_exists():
    # Check that the Enumeration exists
    assert ModifierKind is not None

def test_modifierkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ModifierKind]
    expected_literals = [
        "static",
        "volatile",
        "none",
        "register",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ModifierKind"

def test_displacementlogicoperatorkind_exists():
    # Check that the Enumeration exists
    assert DisplacementLogicOperatorKind is not None

def test_displacementlogicoperatorkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DisplacementLogicOperatorKind]
    expected_literals = [
        "LEFT_DISPLACEMENT",
        "RIGHT_DISPLACEMENT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DisplacementLogicOperatorKind"

def test_relationaloperatorkind_exists():
    # Check that the Enumeration exists
    assert RelationalOperatorKind is not None

def test_relationaloperatorkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RelationalOperatorKind]
    expected_literals = [
        "NOT_EQUALS",
        "LESS_EQUALS",
        "EQUALS",
        "GREATER_EQUALS",
        "none",
        "GREATER",
        "LESS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RelationalOperatorKind"

def test_unaryoperatorkind_exists():
    # Check that the Enumeration exists
    assert UnaryOperatorKind is not None

def test_unaryoperatorkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in UnaryOperatorKind]
    expected_literals = [
        "DIVIDED_BY_EQUALS",
        "TIMES_EQUALS",
        "PLUS_PLUS",
        "MINUS_MINUS",
        "MINUS",
        "MINUS_EQUALS",
        "PLUS_EQUALS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in UnaryOperatorKind"

def test_relationalconectorkind_exists():
    # Check that the Enumeration exists
    assert RelationalConectorKind is not None

def test_relationalconectorkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RelationalConectorKind]
    expected_literals = [
        "AND",
        "NOT",
        "OR",
        "none",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RelationalConectorKind"

def test_binaryoperatorkind_exists():
    # Check that the Enumeration exists
    assert BinaryOperatorKind is not None

def test_binaryoperatorkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BinaryOperatorKind]
    expected_literals = [
        "PLUS",
        "MODULE",
        "TIMES",
        "MINUS",
        "DIVIDED_BY",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BinaryOperatorKind"

def test_functionmodifierkind_exists():
    # Check that the Enumeration exists
    assert FunctionModifierKind is not None

def test_functionmodifierkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FunctionModifierKind]
    expected_literals = [
        "interrupt",
        "cdecl",
        "none",
        "pascal",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FunctionModifierKind"

def test_simplelogicoperatorkind_exists():
    # Check that the Enumeration exists
    assert SimpleLogicOperatorKind is not None

def test_simplelogicoperatorkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SimpleLogicOperatorKind]
    expected_literals = [
        "AND",
        "NOT",
        "XOR",
        "OR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SimpleLogicOperatorKind"


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
Commands_LabelCommand_strategy = st.builds(
    Commands_LabelCommand,
)
Sequencer_strategy = st.builds(
    Sequencer,
)
C_Sequencers_Break_strategy = st.builds(
    C_Sequencers_Break,
)
C_Sequencers_Goto_strategy = st.builds(
    C_Sequencers_Goto,
)
Literal_strategy = st.builds(
    Literal,
)
C_Expressions_FloatLiteral_strategy = st.builds(
    C_Expressions_FloatLiteral,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
C_Expressions_DoubleLiteral_strategy = st.builds(
    C_Expressions_DoubleLiteral,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
C_Expressions_ShortLiteral_strategy = st.builds(
    C_Expressions_ShortLiteral,
    value=
        st.integers()
)
C_Expressions_StringLiteral_strategy = st.builds(
    C_Expressions_StringLiteral,
    value=
        safe_text
)
C_Expressions_IntLiteral_strategy = st.builds(
    C_Expressions_IntLiteral,
    value=
        safe_text
)
C_Expressions_CharLiteral_strategy = st.builds(
    C_Expressions_CharLiteral,
    value=
        safe_text
)
LogicExpression_strategy = st.builds(
    LogicExpression,
)
C_Expressions_SimpleLogicExpression_strategy = st.builds(
    C_Expressions_SimpleLogicExpression,
    operator=
        safe_text
)
C_Expressions_DisplacementLogicExpression_strategy = st.builds(
    C_Expressions_DisplacementLogicExpression,
    operator=
        safe_text
)
ConditionalExpression_strategy = st.builds(
    ConditionalExpression,
)
C_Expressions_ComposedConditionalExpression_strategy = st.builds(
    C_Expressions_ComposedConditionalExpression,
    operator=
        safe_text
)
ArithmeticExpression_strategy = st.builds(
    ArithmeticExpression,
)
C_Expressions_BinaryArithmeticExpression_strategy = st.builds(
    C_Expressions_BinaryArithmeticExpression,
    operator=
        safe_text
)
C_Expressions_UnaryArithmeticExpression_strategy = st.builds(
    C_Expressions_UnaryArithmeticExpression,
    operator=
        safe_text
)
Declarations_PrototypeFunctionDeclaration_strategy = st.builds(
    Declarations_PrototypeFunctionDeclaration,
)
VariableAccess_strategy = st.builds(
    VariableAccess,
)
C_Expressions_PointerVariableAccess_strategy = st.builds(
    C_Expressions_PointerVariableAccess,
)
Declarations_ArrayDeclaration_strategy = st.builds(
    Declarations_ArrayDeclaration,
)
Declarations_ConstantDeclaration_strategy = st.builds(
    Declarations_ConstantDeclaration,
)
Access_strategy = st.builds(
    Access,
)
C_Expressions_ArrayAccess_strategy = st.builds(
    C_Expressions_ArrayAccess,
)
C_Expressions_VariableAccess_strategy = st.builds(
    C_Expressions_VariableAccess,
)
C_Expressions_PrototypeAccess_strategy = st.builds(
    C_Expressions_PrototypeAccess,
)
C_Expressions_ConstantAccess_strategy = st.builds(
    C_Expressions_ConstantAccess,
)
IterativeCommand_strategy = st.builds(
    IterativeCommand,
)
C_Commands_ForCommand_strategy = st.builds(
    C_Commands_ForCommand,
)
C_Commands_DefaultOption_strategy = st.builds(
    C_Commands_DefaultOption,
)
C_Commands_CaseOption_strategy = st.builds(
    C_Commands_CaseOption,
)
Commands_DefaultOption_strategy = st.builds(
    Commands_DefaultOption,
)
Commands_CaseOption_strategy = st.builds(
    Commands_CaseOption,
)
Expressions_VariableAccess_strategy = st.builds(
    Expressions_VariableAccess,
)
Expressions_ConditionalExpression_strategy = st.builds(
    Expressions_ConditionalExpression,
)
DecisionCommand_strategy = st.builds(
    DecisionCommand,
)
C_Commands_SwitchCommand_strategy = st.builds(
    C_Commands_SwitchCommand,
)
C_Commands_IfCommand_strategy = st.builds(
    C_Commands_IfCommand,
)
Expression_strategy = st.builds(
    Expression,
)
C_Expressions_LogicExpression_strategy = st.builds(
    C_Expressions_LogicExpression,
)
C_Expressions_ArithmeticExpression_strategy = st.builds(
    C_Expressions_ArithmeticExpression,
)
C_Expressions_Literal_strategy = st.builds(
    C_Expressions_Literal,
)
C_Expressions_ConditionalExpression_strategy = st.builds(
    C_Expressions_ConditionalExpression,
    conector=
        safe_text
)
C_Expressions_ConstantExpression_strategy = st.builds(
    C_Expressions_ConstantExpression,
)
C_Expressions_CastExpression_strategy = st.builds(
    C_Expressions_CastExpression,
)
C_Expressions_Construction_strategy = st.builds(
    C_Expressions_Construction,
)
C_Expressions_Expression_strategy = st.builds(
    C_Expressions_Expression,
)
C_Commands_WhileCommand_strategy = st.builds(
    C_Commands_WhileCommand,
)
BlockedElement_strategy = st.builds(
    BlockedElement,
)
C_Sequencers_Sequencer_strategy = st.builds(
    C_Sequencers_Sequencer,
)
C_Commands_Command_strategy = st.builds(
    C_Commands_Command,
)
C_CompilationDirectiveDeclarations_Endif_strategy = st.builds(
    C_CompilationDirectiveDeclarations_Endif,
)
IfDirective_strategy = st.builds(
    IfDirective,
)
C_CompilationDirectiveDeclarations_Elif_strategy = st.builds(
    C_CompilationDirectiveDeclarations_Elif,
)
Expressions_ConstantExpression_strategy = st.builds(
    Expressions_ConstantExpression,
)
ComplexDirectiveDeclaration_strategy = st.builds(
    ComplexDirectiveDeclaration,
)
C_CompilationDirectiveDeclarations_IfDirective_strategy = st.builds(
    C_CompilationDirectiveDeclarations_IfDirective,
)
C_CompilationDirectiveDeclarations_ElseDirective_strategy = st.builds(
    C_CompilationDirectiveDeclarations_ElseDirective,
)
C_CompilationDirectiveDeclarations_Ifndef_strategy = st.builds(
    C_CompilationDirectiveDeclarations_Ifndef,
)
CompilationDirectiveDeclarations_Endif_strategy = st.builds(
    CompilationDirectiveDeclarations_Endif,
)
CompilationDirectiveDeclarations_ComplexDirectiveDeclaration_strategy = st.builds(
    CompilationDirectiveDeclarations_ComplexDirectiveDeclaration,
)
SimpleDirectiveDeclaration_strategy = st.builds(
    SimpleDirectiveDeclaration,
)
C_CompilationDirectiveDeclarations_Include_strategy = st.builds(
    C_CompilationDirectiveDeclarations_Include,
)
C_CompilationDirectiveDeclarations_Define_strategy = st.builds(
    C_CompilationDirectiveDeclarations_Define,
    value=
        safe_text
)
CompilationDirectiveDeclaration_strategy = st.builds(
    CompilationDirectiveDeclaration,
)
C_CompilationDirectiveDeclarations_ComplexDirectiveDeclaration_strategy = st.builds(
    C_CompilationDirectiveDeclarations_ComplexDirectiveDeclaration,
)
C_CompilationDirectiveDeclarations_CompilationDirectiveDeclaration_strategy = st.builds(
    C_CompilationDirectiveDeclarations_CompilationDirectiveDeclaration,
)
Declarations_SimpleVariableDeclaration_strategy = st.builds(
    Declarations_SimpleVariableDeclaration,
)
FlowControlCommand_strategy = st.builds(
    FlowControlCommand,
)
C_Commands_ReturnCommand_strategy = st.builds(
    C_Commands_ReturnCommand,
)
C_Commands_DecisionCommand_strategy = st.builds(
    C_Commands_DecisionCommand,
)
Expressions_Access_strategy = st.builds(
    Expressions_Access,
)
Command_strategy = st.builds(
    Command,
)
C_Commands_FlowControlCommand_strategy = st.builds(
    C_Commands_FlowControlCommand,
)
C_Commands_IterativeCommand_strategy = st.builds(
    C_Commands_IterativeCommand,
)
C_Commands_ExpressionCommand_strategy = st.builds(
    C_Commands_ExpressionCommand,
)
C_Commands_Assignment_strategy = st.builds(
    C_Commands_Assignment,
)
Commands_Command_strategy = st.builds(
    Commands_Command,
)
Declarations_FragmentVariableDeclaration_strategy = st.builds(
    Declarations_FragmentVariableDeclaration,
)
Declarations_VariableDeclaration_strategy = st.builds(
    Declarations_VariableDeclaration,
)
Expressions_Expression_strategy = st.builds(
    Expressions_Expression,
)
Declaration_strategy = st.builds(
    Declaration,
)
C_Declarations_PrototypeFunctionDeclaration_strategy = st.builds(
    C_Declarations_PrototypeFunctionDeclaration,
    isAPointer=
        safe_text,
    functionModifier=
        safe_text
)
C_Declarations_VariableDeclaration_strategy = st.builds(
    C_Declarations_VariableDeclaration,
    numberOfPointers=
        safe_text,
    isAPointer=
        safe_text
)
C_Declarations_ConstantDeclaration_strategy = st.builds(
    C_Declarations_ConstantDeclaration,
)
Main_Function_strategy = st.builds(
    Main_Function,
)
CompilationDirectiveDeclarations_CompilationDirectiveDeclaration_strategy = st.builds(
    CompilationDirectiveDeclarations_CompilationDirectiveDeclaration,
)
Expressions_Construction_strategy = st.builds(
    Expressions_Construction,
)
Declarations_CompositeVariableDeclaration_strategy = st.builds(
    Declarations_CompositeVariableDeclaration,
)
Expressions_Literal_strategy = st.builds(
    Expressions_Literal,
)
CompositeVariableDeclaration_strategy = st.builds(
    CompositeVariableDeclaration,
)
C_Declarations_StructDeclaration_strategy = st.builds(
    C_Declarations_StructDeclaration,
)
C_Declarations_TypeDefDeclaration_strategy = st.builds(
    C_Declarations_TypeDefDeclaration,
)
C_Declarations_EnumDeclaration_strategy = st.builds(
    C_Declarations_EnumDeclaration,
)
VariableDeclaration_strategy = st.builds(
    VariableDeclaration,
)
C_Declarations_CompositeVariableDeclaration_strategy = st.builds(
    C_Declarations_CompositeVariableDeclaration,
)
Main_Element_strategy = st.builds(
    Main_Element,
)
Unit_strategy = st.builds(
    Unit,
)
C_Main_C_Unit_strategy = st.builds(
    C_Main_C_Unit,
)
Main_Comment_strategy = st.builds(
    Main_Comment,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
C_Declarations_Declaration_strategy = st.builds(
    C_Declarations_Declaration,
    modifier=
        safe_text
)
C_Main_Comment_strategy = st.builds(
    C_Main_Comment,
)
C_Main_Element_strategy = st.builds(
    C_Main_Element,
)
C_Main_Unit_strategy = st.builds(
    C_Main_Unit,
)
Main_Unit_strategy = st.builds(
    Main_Unit,
)
C_Main_Program_strategy = st.builds(
    C_Main_Program,
    description=
        safe_text
)
Main_Block_strategy = st.builds(
    Main_Block,
)
C_Abstractions_BlockedElement_strategy = st.builds(
    C_Abstractions_BlockedElement,
)
C_Abstractions_NamedElement_strategy = st.builds(
    C_Abstractions_NamedElement,
    name=
        safe_text
)
Abstractions_NamedElement_strategy = st.builds(
    Abstractions_NamedElement,
)
C_Expressions_AtomicConditionalExpression_strategy = st.builds(
    C_Expressions_AtomicConditionalExpression,
)
C_Expressions_FunctionCall_strategy = st.builds(
    C_Expressions_FunctionCall,
)
C_CompilationDirectiveDeclarations_Ifdef_strategy = st.builds(
    C_CompilationDirectiveDeclarations_Ifdef,
)
C_Declarations_FragmentVariableDeclaration_strategy = st.builds(
    C_Declarations_FragmentVariableDeclaration,
)
C_Commands_LabelCommand_strategy = st.builds(
    C_Commands_LabelCommand,
)
C_Expressions_Access_strategy = st.builds(
    C_Expressions_Access,
)
C_CompilationDirectiveDeclarations_SimpleDirectiveDeclaration_strategy = st.builds(
    C_CompilationDirectiveDeclarations_SimpleDirectiveDeclaration,
)
Types_Type_strategy = st.builds(
    Types_Type,
)
C_Types_FromHeader_strategy = st.builds(
    C_Types_FromHeader,
)
CompositeType_strategy = st.builds(
    CompositeType,
)
C_Types_Enum_strategy = st.builds(
    C_Types_Enum,
)
C_Types_Struct_strategy = st.builds(
    C_Types_Struct,
)
C_Types_Array_strategy = st.builds(
    C_Types_Array,
)
C_Types_Typedef_strategy = st.builds(
    C_Types_Typedef,
)
Types_Array_strategy = st.builds(
    Types_Array,
)
Types_PrimitiveType_strategy = st.builds(
    Types_PrimitiveType,
)
C_Types_Int_strategy = st.builds(
    C_Types_Int,
)
PrimitiveType_strategy = st.builds(
    PrimitiveType,
)
C_Types_Float_strategy = st.builds(
    C_Types_Float,
)
C_Types_Void_strategy = st.builds(
    C_Types_Void,
)
C_Types_Double_strategy = st.builds(
    C_Types_Double,
)
C_Types_Short_strategy = st.builds(
    C_Types_Short,
)
C_Types_Char_strategy = st.builds(
    C_Types_Char,
)
Abstractions_BlockedElement_strategy = st.builds(
    Abstractions_BlockedElement,
)
C_Declarations_ArrayDeclaration_strategy = st.builds(
    C_Declarations_ArrayDeclaration,
    dimensions=
        safe_text
)
C_Declarations_SimpleVariableDeclaration_strategy = st.builds(
    C_Declarations_SimpleVariableDeclaration,
)
C_Main_Block_strategy = st.builds(
    C_Main_Block,
)
Declarations_Declaration_strategy = st.builds(
    Declarations_Declaration,
)
Element_strategy = st.builds(
    Element,
)
C_Main_DeclarationsBlock_strategy = st.builds(
    C_Main_DeclarationsBlock,
)
C_Main_FunctionsBlock_strategy = st.builds(
    C_Main_FunctionsBlock,
)
C_Main_Function_strategy = st.builds(
    C_Main_Function,
    functionModifier=
        safe_text,
    modifier=
        safe_text
)
Main_DeclarationsBlock_strategy = st.builds(
    Main_DeclarationsBlock,
)
C_Main_H_Unit_strategy = st.builds(
    C_Main_H_Unit,
)
Type_strategy = st.builds(
    Type,
)
C_Types_CompositeType_strategy = st.builds(
    C_Types_CompositeType,
)
C_Types_PrimitiveType_strategy = st.builds(
    C_Types_PrimitiveType,
)
C_Types_Type_strategy = st.builds(
    C_Types_Type,
)

@given(instance=Commands_LabelCommand_strategy)
@settings(max_examples=50)
def test_commands_labelcommand_instantiation(instance):
    assert isinstance(instance, Commands_LabelCommand)

@given(instance=Sequencer_strategy)
@settings(max_examples=50)
def test_sequencer_instantiation(instance):
    assert isinstance(instance, Sequencer)

@given(instance=C_Sequencers_Break_strategy)
@settings(max_examples=50)
def test_c_sequencers_break_instantiation(instance):
    assert isinstance(instance, C_Sequencers_Break)

@given(instance=C_Sequencers_Goto_strategy)
@settings(max_examples=50)
def test_c_sequencers_goto_instantiation(instance):
    assert isinstance(instance, C_Sequencers_Goto)

@given(instance=Literal_strategy)
@settings(max_examples=50)
def test_literal_instantiation(instance):
    assert isinstance(instance, Literal)

@given(instance=C_Expressions_FloatLiteral_strategy)
@settings(max_examples=50)
def test_c_expressions_floatliteral_instantiation(instance):
    assert isinstance(instance, C_Expressions_FloatLiteral)



@given(instance=C_Expressions_FloatLiteral_strategy)
def test_c_expressions_floatliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=C_Expressions_DoubleLiteral_strategy)
@settings(max_examples=50)
def test_c_expressions_doubleliteral_instantiation(instance):
    assert isinstance(instance, C_Expressions_DoubleLiteral)



@given(instance=C_Expressions_DoubleLiteral_strategy)
def test_c_expressions_doubleliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=C_Expressions_ShortLiteral_strategy)
@settings(max_examples=50)
def test_c_expressions_shortliteral_instantiation(instance):
    assert isinstance(instance, C_Expressions_ShortLiteral)



@given(instance=C_Expressions_ShortLiteral_strategy)
def test_c_expressions_shortliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=C_Expressions_StringLiteral_strategy)
@settings(max_examples=50)
def test_c_expressions_stringliteral_instantiation(instance):
    assert isinstance(instance, C_Expressions_StringLiteral)



@given(instance=C_Expressions_StringLiteral_strategy)
def test_c_expressions_stringliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=C_Expressions_IntLiteral_strategy)
@settings(max_examples=50)
def test_c_expressions_intliteral_instantiation(instance):
    assert isinstance(instance, C_Expressions_IntLiteral)



@given(instance=C_Expressions_IntLiteral_strategy)
def test_c_expressions_intliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=C_Expressions_CharLiteral_strategy)
@settings(max_examples=50)
def test_c_expressions_charliteral_instantiation(instance):
    assert isinstance(instance, C_Expressions_CharLiteral)



@given(instance=C_Expressions_CharLiteral_strategy)
def test_c_expressions_charliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=LogicExpression_strategy)
@settings(max_examples=50)
def test_logicexpression_instantiation(instance):
    assert isinstance(instance, LogicExpression)

@given(instance=C_Expressions_SimpleLogicExpression_strategy)
@settings(max_examples=50)
def test_c_expressions_simplelogicexpression_instantiation(instance):
    assert isinstance(instance, C_Expressions_SimpleLogicExpression)



@given(instance=C_Expressions_SimpleLogicExpression_strategy)
def test_c_expressions_simplelogicexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=C_Expressions_DisplacementLogicExpression_strategy)
@settings(max_examples=50)
def test_c_expressions_displacementlogicexpression_instantiation(instance):
    assert isinstance(instance, C_Expressions_DisplacementLogicExpression)



@given(instance=C_Expressions_DisplacementLogicExpression_strategy)
def test_c_expressions_displacementlogicexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=ConditionalExpression_strategy)
@settings(max_examples=50)
def test_conditionalexpression_instantiation(instance):
    assert isinstance(instance, ConditionalExpression)

@given(instance=C_Expressions_ComposedConditionalExpression_strategy)
@settings(max_examples=50)
def test_c_expressions_composedconditionalexpression_instantiation(instance):
    assert isinstance(instance, C_Expressions_ComposedConditionalExpression)



@given(instance=C_Expressions_ComposedConditionalExpression_strategy)
def test_c_expressions_composedconditionalexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=ArithmeticExpression_strategy)
@settings(max_examples=50)
def test_arithmeticexpression_instantiation(instance):
    assert isinstance(instance, ArithmeticExpression)

@given(instance=C_Expressions_BinaryArithmeticExpression_strategy)
@settings(max_examples=50)
def test_c_expressions_binaryarithmeticexpression_instantiation(instance):
    assert isinstance(instance, C_Expressions_BinaryArithmeticExpression)



@given(instance=C_Expressions_BinaryArithmeticExpression_strategy)
def test_c_expressions_binaryarithmeticexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=C_Expressions_UnaryArithmeticExpression_strategy)
@settings(max_examples=50)
def test_c_expressions_unaryarithmeticexpression_instantiation(instance):
    assert isinstance(instance, C_Expressions_UnaryArithmeticExpression)



@given(instance=C_Expressions_UnaryArithmeticExpression_strategy)
def test_c_expressions_unaryarithmeticexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=Declarations_PrototypeFunctionDeclaration_strategy)
@settings(max_examples=50)
def test_declarations_prototypefunctiondeclaration_instantiation(instance):
    assert isinstance(instance, Declarations_PrototypeFunctionDeclaration)

@given(instance=VariableAccess_strategy)
@settings(max_examples=50)
def test_variableaccess_instantiation(instance):
    assert isinstance(instance, VariableAccess)

@given(instance=C_Expressions_PointerVariableAccess_strategy)
@settings(max_examples=50)
def test_c_expressions_pointervariableaccess_instantiation(instance):
    assert isinstance(instance, C_Expressions_PointerVariableAccess)

@given(instance=Declarations_ArrayDeclaration_strategy)
@settings(max_examples=50)
def test_declarations_arraydeclaration_instantiation(instance):
    assert isinstance(instance, Declarations_ArrayDeclaration)

@given(instance=Declarations_ConstantDeclaration_strategy)
@settings(max_examples=50)
def test_declarations_constantdeclaration_instantiation(instance):
    assert isinstance(instance, Declarations_ConstantDeclaration)

@given(instance=Access_strategy)
@settings(max_examples=50)
def test_access_instantiation(instance):
    assert isinstance(instance, Access)

@given(instance=C_Expressions_ArrayAccess_strategy)
@settings(max_examples=50)
def test_c_expressions_arrayaccess_instantiation(instance):
    assert isinstance(instance, C_Expressions_ArrayAccess)

@given(instance=C_Expressions_VariableAccess_strategy)
@settings(max_examples=50)
def test_c_expressions_variableaccess_instantiation(instance):
    assert isinstance(instance, C_Expressions_VariableAccess)

@given(instance=C_Expressions_PrototypeAccess_strategy)
@settings(max_examples=50)
def test_c_expressions_prototypeaccess_instantiation(instance):
    assert isinstance(instance, C_Expressions_PrototypeAccess)

@given(instance=C_Expressions_ConstantAccess_strategy)
@settings(max_examples=50)
def test_c_expressions_constantaccess_instantiation(instance):
    assert isinstance(instance, C_Expressions_ConstantAccess)

@given(instance=IterativeCommand_strategy)
@settings(max_examples=50)
def test_iterativecommand_instantiation(instance):
    assert isinstance(instance, IterativeCommand)

@given(instance=C_Commands_ForCommand_strategy)
@settings(max_examples=50)
def test_c_commands_forcommand_instantiation(instance):
    assert isinstance(instance, C_Commands_ForCommand)

@given(instance=C_Commands_DefaultOption_strategy)
@settings(max_examples=50)
def test_c_commands_defaultoption_instantiation(instance):
    assert isinstance(instance, C_Commands_DefaultOption)

@given(instance=C_Commands_CaseOption_strategy)
@settings(max_examples=50)
def test_c_commands_caseoption_instantiation(instance):
    assert isinstance(instance, C_Commands_CaseOption)

@given(instance=Commands_DefaultOption_strategy)
@settings(max_examples=50)
def test_commands_defaultoption_instantiation(instance):
    assert isinstance(instance, Commands_DefaultOption)

@given(instance=Commands_CaseOption_strategy)
@settings(max_examples=50)
def test_commands_caseoption_instantiation(instance):
    assert isinstance(instance, Commands_CaseOption)

@given(instance=Expressions_VariableAccess_strategy)
@settings(max_examples=50)
def test_expressions_variableaccess_instantiation(instance):
    assert isinstance(instance, Expressions_VariableAccess)

@given(instance=Expressions_ConditionalExpression_strategy)
@settings(max_examples=50)
def test_expressions_conditionalexpression_instantiation(instance):
    assert isinstance(instance, Expressions_ConditionalExpression)

@given(instance=DecisionCommand_strategy)
@settings(max_examples=50)
def test_decisioncommand_instantiation(instance):
    assert isinstance(instance, DecisionCommand)

@given(instance=C_Commands_SwitchCommand_strategy)
@settings(max_examples=50)
def test_c_commands_switchcommand_instantiation(instance):
    assert isinstance(instance, C_Commands_SwitchCommand)

@given(instance=C_Commands_IfCommand_strategy)
@settings(max_examples=50)
def test_c_commands_ifcommand_instantiation(instance):
    assert isinstance(instance, C_Commands_IfCommand)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=C_Expressions_LogicExpression_strategy)
@settings(max_examples=50)
def test_c_expressions_logicexpression_instantiation(instance):
    assert isinstance(instance, C_Expressions_LogicExpression)

@given(instance=C_Expressions_ArithmeticExpression_strategy)
@settings(max_examples=50)
def test_c_expressions_arithmeticexpression_instantiation(instance):
    assert isinstance(instance, C_Expressions_ArithmeticExpression)

@given(instance=C_Expressions_Literal_strategy)
@settings(max_examples=50)
def test_c_expressions_literal_instantiation(instance):
    assert isinstance(instance, C_Expressions_Literal)

@given(instance=C_Expressions_ConditionalExpression_strategy)
@settings(max_examples=50)
def test_c_expressions_conditionalexpression_instantiation(instance):
    assert isinstance(instance, C_Expressions_ConditionalExpression)



@given(instance=C_Expressions_ConditionalExpression_strategy)
def test_c_expressions_conditionalexpression_conector_setter(instance):
    original = instance.conector
    instance.conector = original
    assert instance.conector == original

@given(instance=C_Expressions_ConstantExpression_strategy)
@settings(max_examples=50)
def test_c_expressions_constantexpression_instantiation(instance):
    assert isinstance(instance, C_Expressions_ConstantExpression)

@given(instance=C_Expressions_CastExpression_strategy)
@settings(max_examples=50)
def test_c_expressions_castexpression_instantiation(instance):
    assert isinstance(instance, C_Expressions_CastExpression)

@given(instance=C_Expressions_Construction_strategy)
@settings(max_examples=50)
def test_c_expressions_construction_instantiation(instance):
    assert isinstance(instance, C_Expressions_Construction)

@given(instance=C_Expressions_Expression_strategy)
@settings(max_examples=50)
def test_c_expressions_expression_instantiation(instance):
    assert isinstance(instance, C_Expressions_Expression)

@given(instance=C_Commands_WhileCommand_strategy)
@settings(max_examples=50)
def test_c_commands_whilecommand_instantiation(instance):
    assert isinstance(instance, C_Commands_WhileCommand)

@given(instance=BlockedElement_strategy)
@settings(max_examples=50)
def test_blockedelement_instantiation(instance):
    assert isinstance(instance, BlockedElement)

@given(instance=C_Sequencers_Sequencer_strategy)
@settings(max_examples=50)
def test_c_sequencers_sequencer_instantiation(instance):
    assert isinstance(instance, C_Sequencers_Sequencer)

@given(instance=C_Commands_Command_strategy)
@settings(max_examples=50)
def test_c_commands_command_instantiation(instance):
    assert isinstance(instance, C_Commands_Command)

@given(instance=C_CompilationDirectiveDeclarations_Endif_strategy)
@settings(max_examples=50)
def test_c_compilationdirectivedeclarations_endif_instantiation(instance):
    assert isinstance(instance, C_CompilationDirectiveDeclarations_Endif)

@given(instance=IfDirective_strategy)
@settings(max_examples=50)
def test_ifdirective_instantiation(instance):
    assert isinstance(instance, IfDirective)

@given(instance=C_CompilationDirectiveDeclarations_Elif_strategy)
@settings(max_examples=50)
def test_c_compilationdirectivedeclarations_elif_instantiation(instance):
    assert isinstance(instance, C_CompilationDirectiveDeclarations_Elif)

@given(instance=Expressions_ConstantExpression_strategy)
@settings(max_examples=50)
def test_expressions_constantexpression_instantiation(instance):
    assert isinstance(instance, Expressions_ConstantExpression)

@given(instance=ComplexDirectiveDeclaration_strategy)
@settings(max_examples=50)
def test_complexdirectivedeclaration_instantiation(instance):
    assert isinstance(instance, ComplexDirectiveDeclaration)

@given(instance=C_CompilationDirectiveDeclarations_IfDirective_strategy)
@settings(max_examples=50)
def test_c_compilationdirectivedeclarations_ifdirective_instantiation(instance):
    assert isinstance(instance, C_CompilationDirectiveDeclarations_IfDirective)

@given(instance=C_CompilationDirectiveDeclarations_ElseDirective_strategy)
@settings(max_examples=50)
def test_c_compilationdirectivedeclarations_elsedirective_instantiation(instance):
    assert isinstance(instance, C_CompilationDirectiveDeclarations_ElseDirective)

@given(instance=C_CompilationDirectiveDeclarations_Ifndef_strategy)
@settings(max_examples=50)
def test_c_compilationdirectivedeclarations_ifndef_instantiation(instance):
    assert isinstance(instance, C_CompilationDirectiveDeclarations_Ifndef)

@given(instance=CompilationDirectiveDeclarations_Endif_strategy)
@settings(max_examples=50)
def test_compilationdirectivedeclarations_endif_instantiation(instance):
    assert isinstance(instance, CompilationDirectiveDeclarations_Endif)

@given(instance=CompilationDirectiveDeclarations_ComplexDirectiveDeclaration_strategy)
@settings(max_examples=50)
def test_compilationdirectivedeclarations_complexdirectivedeclaration_instantiation(instance):
    assert isinstance(instance, CompilationDirectiveDeclarations_ComplexDirectiveDeclaration)

@given(instance=SimpleDirectiveDeclaration_strategy)
@settings(max_examples=50)
def test_simpledirectivedeclaration_instantiation(instance):
    assert isinstance(instance, SimpleDirectiveDeclaration)

@given(instance=C_CompilationDirectiveDeclarations_Include_strategy)
@settings(max_examples=50)
def test_c_compilationdirectivedeclarations_include_instantiation(instance):
    assert isinstance(instance, C_CompilationDirectiveDeclarations_Include)

@given(instance=C_CompilationDirectiveDeclarations_Define_strategy)
@settings(max_examples=50)
def test_c_compilationdirectivedeclarations_define_instantiation(instance):
    assert isinstance(instance, C_CompilationDirectiveDeclarations_Define)



@given(instance=C_CompilationDirectiveDeclarations_Define_strategy)
def test_c_compilationdirectivedeclarations_define_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=CompilationDirectiveDeclaration_strategy)
@settings(max_examples=50)
def test_compilationdirectivedeclaration_instantiation(instance):
    assert isinstance(instance, CompilationDirectiveDeclaration)

@given(instance=C_CompilationDirectiveDeclarations_ComplexDirectiveDeclaration_strategy)
@settings(max_examples=50)
def test_c_compilationdirectivedeclarations_complexdirectivedeclaration_instantiation(instance):
    assert isinstance(instance, C_CompilationDirectiveDeclarations_ComplexDirectiveDeclaration)

@given(instance=C_CompilationDirectiveDeclarations_CompilationDirectiveDeclaration_strategy)
@settings(max_examples=50)
def test_c_compilationdirectivedeclarations_compilationdirectivedeclaration_instantiation(instance):
    assert isinstance(instance, C_CompilationDirectiveDeclarations_CompilationDirectiveDeclaration)

@given(instance=Declarations_SimpleVariableDeclaration_strategy)
@settings(max_examples=50)
def test_declarations_simplevariabledeclaration_instantiation(instance):
    assert isinstance(instance, Declarations_SimpleVariableDeclaration)

@given(instance=FlowControlCommand_strategy)
@settings(max_examples=50)
def test_flowcontrolcommand_instantiation(instance):
    assert isinstance(instance, FlowControlCommand)

@given(instance=C_Commands_ReturnCommand_strategy)
@settings(max_examples=50)
def test_c_commands_returncommand_instantiation(instance):
    assert isinstance(instance, C_Commands_ReturnCommand)

@given(instance=C_Commands_DecisionCommand_strategy)
@settings(max_examples=50)
def test_c_commands_decisioncommand_instantiation(instance):
    assert isinstance(instance, C_Commands_DecisionCommand)

@given(instance=Expressions_Access_strategy)
@settings(max_examples=50)
def test_expressions_access_instantiation(instance):
    assert isinstance(instance, Expressions_Access)

@given(instance=Command_strategy)
@settings(max_examples=50)
def test_command_instantiation(instance):
    assert isinstance(instance, Command)

@given(instance=C_Commands_FlowControlCommand_strategy)
@settings(max_examples=50)
def test_c_commands_flowcontrolcommand_instantiation(instance):
    assert isinstance(instance, C_Commands_FlowControlCommand)

@given(instance=C_Commands_IterativeCommand_strategy)
@settings(max_examples=50)
def test_c_commands_iterativecommand_instantiation(instance):
    assert isinstance(instance, C_Commands_IterativeCommand)

@given(instance=C_Commands_ExpressionCommand_strategy)
@settings(max_examples=50)
def test_c_commands_expressioncommand_instantiation(instance):
    assert isinstance(instance, C_Commands_ExpressionCommand)

@given(instance=C_Commands_Assignment_strategy)
@settings(max_examples=50)
def test_c_commands_assignment_instantiation(instance):
    assert isinstance(instance, C_Commands_Assignment)

@given(instance=Commands_Command_strategy)
@settings(max_examples=50)
def test_commands_command_instantiation(instance):
    assert isinstance(instance, Commands_Command)

@given(instance=Declarations_FragmentVariableDeclaration_strategy)
@settings(max_examples=50)
def test_declarations_fragmentvariabledeclaration_instantiation(instance):
    assert isinstance(instance, Declarations_FragmentVariableDeclaration)

@given(instance=Declarations_VariableDeclaration_strategy)
@settings(max_examples=50)
def test_declarations_variabledeclaration_instantiation(instance):
    assert isinstance(instance, Declarations_VariableDeclaration)

@given(instance=Expressions_Expression_strategy)
@settings(max_examples=50)
def test_expressions_expression_instantiation(instance):
    assert isinstance(instance, Expressions_Expression)

@given(instance=Declaration_strategy)
@settings(max_examples=50)
def test_declaration_instantiation(instance):
    assert isinstance(instance, Declaration)

@given(instance=C_Declarations_PrototypeFunctionDeclaration_strategy)
@settings(max_examples=50)
def test_c_declarations_prototypefunctiondeclaration_instantiation(instance):
    assert isinstance(instance, C_Declarations_PrototypeFunctionDeclaration)



@given(instance=C_Declarations_PrototypeFunctionDeclaration_strategy)
def test_c_declarations_prototypefunctiondeclaration_isAPointer_setter(instance):
    original = instance.isAPointer
    instance.isAPointer = original
    assert instance.isAPointer == original



@given(instance=C_Declarations_PrototypeFunctionDeclaration_strategy)
def test_c_declarations_prototypefunctiondeclaration_functionModifier_setter(instance):
    original = instance.functionModifier
    instance.functionModifier = original
    assert instance.functionModifier == original

@given(instance=C_Declarations_VariableDeclaration_strategy)
@settings(max_examples=50)
def test_c_declarations_variabledeclaration_instantiation(instance):
    assert isinstance(instance, C_Declarations_VariableDeclaration)



@given(instance=C_Declarations_VariableDeclaration_strategy)
def test_c_declarations_variabledeclaration_numberOfPointers_setter(instance):
    original = instance.numberOfPointers
    instance.numberOfPointers = original
    assert instance.numberOfPointers == original



@given(instance=C_Declarations_VariableDeclaration_strategy)
def test_c_declarations_variabledeclaration_isAPointer_setter(instance):
    original = instance.isAPointer
    instance.isAPointer = original
    assert instance.isAPointer == original

@given(instance=C_Declarations_ConstantDeclaration_strategy)
@settings(max_examples=50)
def test_c_declarations_constantdeclaration_instantiation(instance):
    assert isinstance(instance, C_Declarations_ConstantDeclaration)

@given(instance=Main_Function_strategy)
@settings(max_examples=50)
def test_main_function_instantiation(instance):
    assert isinstance(instance, Main_Function)

@given(instance=CompilationDirectiveDeclarations_CompilationDirectiveDeclaration_strategy)
@settings(max_examples=50)
def test_compilationdirectivedeclarations_compilationdirectivedeclaration_instantiation(instance):
    assert isinstance(instance, CompilationDirectiveDeclarations_CompilationDirectiveDeclaration)

@given(instance=Expressions_Construction_strategy)
@settings(max_examples=50)
def test_expressions_construction_instantiation(instance):
    assert isinstance(instance, Expressions_Construction)

@given(instance=Declarations_CompositeVariableDeclaration_strategy)
@settings(max_examples=50)
def test_declarations_compositevariabledeclaration_instantiation(instance):
    assert isinstance(instance, Declarations_CompositeVariableDeclaration)

@given(instance=Expressions_Literal_strategy)
@settings(max_examples=50)
def test_expressions_literal_instantiation(instance):
    assert isinstance(instance, Expressions_Literal)

@given(instance=CompositeVariableDeclaration_strategy)
@settings(max_examples=50)
def test_compositevariabledeclaration_instantiation(instance):
    assert isinstance(instance, CompositeVariableDeclaration)

@given(instance=C_Declarations_StructDeclaration_strategy)
@settings(max_examples=50)
def test_c_declarations_structdeclaration_instantiation(instance):
    assert isinstance(instance, C_Declarations_StructDeclaration)

@given(instance=C_Declarations_TypeDefDeclaration_strategy)
@settings(max_examples=50)
def test_c_declarations_typedefdeclaration_instantiation(instance):
    assert isinstance(instance, C_Declarations_TypeDefDeclaration)

@given(instance=C_Declarations_EnumDeclaration_strategy)
@settings(max_examples=50)
def test_c_declarations_enumdeclaration_instantiation(instance):
    assert isinstance(instance, C_Declarations_EnumDeclaration)

@given(instance=VariableDeclaration_strategy)
@settings(max_examples=50)
def test_variabledeclaration_instantiation(instance):
    assert isinstance(instance, VariableDeclaration)

@given(instance=C_Declarations_CompositeVariableDeclaration_strategy)
@settings(max_examples=50)
def test_c_declarations_compositevariabledeclaration_instantiation(instance):
    assert isinstance(instance, C_Declarations_CompositeVariableDeclaration)

@given(instance=Main_Element_strategy)
@settings(max_examples=50)
def test_main_element_instantiation(instance):
    assert isinstance(instance, Main_Element)

@given(instance=Unit_strategy)
@settings(max_examples=50)
def test_unit_instantiation(instance):
    assert isinstance(instance, Unit)

@given(instance=C_Main_C_Unit_strategy)
@settings(max_examples=50)
def test_c_main_c_unit_instantiation(instance):
    assert isinstance(instance, C_Main_C_Unit)

@given(instance=Main_Comment_strategy)
@settings(max_examples=50)
def test_main_comment_instantiation(instance):
    assert isinstance(instance, Main_Comment)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=C_Declarations_Declaration_strategy)
@settings(max_examples=50)
def test_c_declarations_declaration_instantiation(instance):
    assert isinstance(instance, C_Declarations_Declaration)



@given(instance=C_Declarations_Declaration_strategy)
def test_c_declarations_declaration_modifier_setter(instance):
    original = instance.modifier
    instance.modifier = original
    assert instance.modifier == original

@given(instance=C_Main_Comment_strategy)
@settings(max_examples=50)
def test_c_main_comment_instantiation(instance):
    assert isinstance(instance, C_Main_Comment)

@given(instance=C_Main_Element_strategy)
@settings(max_examples=50)
def test_c_main_element_instantiation(instance):
    assert isinstance(instance, C_Main_Element)

@given(instance=C_Main_Unit_strategy)
@settings(max_examples=50)
def test_c_main_unit_instantiation(instance):
    assert isinstance(instance, C_Main_Unit)

@given(instance=Main_Unit_strategy)
@settings(max_examples=50)
def test_main_unit_instantiation(instance):
    assert isinstance(instance, Main_Unit)

@given(instance=C_Main_Program_strategy)
@settings(max_examples=50)
def test_c_main_program_instantiation(instance):
    assert isinstance(instance, C_Main_Program)



@given(instance=C_Main_Program_strategy)
def test_c_main_program_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=Main_Block_strategy)
@settings(max_examples=50)
def test_main_block_instantiation(instance):
    assert isinstance(instance, Main_Block)

@given(instance=C_Abstractions_BlockedElement_strategy)
@settings(max_examples=50)
def test_c_abstractions_blockedelement_instantiation(instance):
    assert isinstance(instance, C_Abstractions_BlockedElement)

@given(instance=C_Abstractions_NamedElement_strategy)
@settings(max_examples=50)
def test_c_abstractions_namedelement_instantiation(instance):
    assert isinstance(instance, C_Abstractions_NamedElement)



@given(instance=C_Abstractions_NamedElement_strategy)
def test_c_abstractions_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Abstractions_NamedElement_strategy)
@settings(max_examples=50)
def test_abstractions_namedelement_instantiation(instance):
    assert isinstance(instance, Abstractions_NamedElement)

@given(instance=C_Expressions_AtomicConditionalExpression_strategy)
@settings(max_examples=50)
def test_c_expressions_atomicconditionalexpression_instantiation(instance):
    assert isinstance(instance, C_Expressions_AtomicConditionalExpression)

@given(instance=C_Expressions_FunctionCall_strategy)
@settings(max_examples=50)
def test_c_expressions_functioncall_instantiation(instance):
    assert isinstance(instance, C_Expressions_FunctionCall)

@given(instance=C_CompilationDirectiveDeclarations_Ifdef_strategy)
@settings(max_examples=50)
def test_c_compilationdirectivedeclarations_ifdef_instantiation(instance):
    assert isinstance(instance, C_CompilationDirectiveDeclarations_Ifdef)

@given(instance=C_Declarations_FragmentVariableDeclaration_strategy)
@settings(max_examples=50)
def test_c_declarations_fragmentvariabledeclaration_instantiation(instance):
    assert isinstance(instance, C_Declarations_FragmentVariableDeclaration)

@given(instance=C_Commands_LabelCommand_strategy)
@settings(max_examples=50)
def test_c_commands_labelcommand_instantiation(instance):
    assert isinstance(instance, C_Commands_LabelCommand)

@given(instance=C_Expressions_Access_strategy)
@settings(max_examples=50)
def test_c_expressions_access_instantiation(instance):
    assert isinstance(instance, C_Expressions_Access)

@given(instance=C_CompilationDirectiveDeclarations_SimpleDirectiveDeclaration_strategy)
@settings(max_examples=50)
def test_c_compilationdirectivedeclarations_simpledirectivedeclaration_instantiation(instance):
    assert isinstance(instance, C_CompilationDirectiveDeclarations_SimpleDirectiveDeclaration)

@given(instance=Types_Type_strategy)
@settings(max_examples=50)
def test_types_type_instantiation(instance):
    assert isinstance(instance, Types_Type)

@given(instance=C_Types_FromHeader_strategy)
@settings(max_examples=50)
def test_c_types_fromheader_instantiation(instance):
    assert isinstance(instance, C_Types_FromHeader)

@given(instance=CompositeType_strategy)
@settings(max_examples=50)
def test_compositetype_instantiation(instance):
    assert isinstance(instance, CompositeType)

@given(instance=C_Types_Enum_strategy)
@settings(max_examples=50)
def test_c_types_enum_instantiation(instance):
    assert isinstance(instance, C_Types_Enum)

@given(instance=C_Types_Struct_strategy)
@settings(max_examples=50)
def test_c_types_struct_instantiation(instance):
    assert isinstance(instance, C_Types_Struct)

@given(instance=C_Types_Array_strategy)
@settings(max_examples=50)
def test_c_types_array_instantiation(instance):
    assert isinstance(instance, C_Types_Array)

@given(instance=C_Types_Typedef_strategy)
@settings(max_examples=50)
def test_c_types_typedef_instantiation(instance):
    assert isinstance(instance, C_Types_Typedef)

@given(instance=Types_Array_strategy)
@settings(max_examples=50)
def test_types_array_instantiation(instance):
    assert isinstance(instance, Types_Array)

@given(instance=Types_PrimitiveType_strategy)
@settings(max_examples=50)
def test_types_primitivetype_instantiation(instance):
    assert isinstance(instance, Types_PrimitiveType)

@given(instance=C_Types_Int_strategy)
@settings(max_examples=50)
def test_c_types_int_instantiation(instance):
    assert isinstance(instance, C_Types_Int)

@given(instance=PrimitiveType_strategy)
@settings(max_examples=50)
def test_primitivetype_instantiation(instance):
    assert isinstance(instance, PrimitiveType)

@given(instance=C_Types_Float_strategy)
@settings(max_examples=50)
def test_c_types_float_instantiation(instance):
    assert isinstance(instance, C_Types_Float)

@given(instance=C_Types_Void_strategy)
@settings(max_examples=50)
def test_c_types_void_instantiation(instance):
    assert isinstance(instance, C_Types_Void)

@given(instance=C_Types_Double_strategy)
@settings(max_examples=50)
def test_c_types_double_instantiation(instance):
    assert isinstance(instance, C_Types_Double)

@given(instance=C_Types_Short_strategy)
@settings(max_examples=50)
def test_c_types_short_instantiation(instance):
    assert isinstance(instance, C_Types_Short)

@given(instance=C_Types_Char_strategy)
@settings(max_examples=50)
def test_c_types_char_instantiation(instance):
    assert isinstance(instance, C_Types_Char)

@given(instance=Abstractions_BlockedElement_strategy)
@settings(max_examples=50)
def test_abstractions_blockedelement_instantiation(instance):
    assert isinstance(instance, Abstractions_BlockedElement)

@given(instance=C_Declarations_ArrayDeclaration_strategy)
@settings(max_examples=50)
def test_c_declarations_arraydeclaration_instantiation(instance):
    assert isinstance(instance, C_Declarations_ArrayDeclaration)



@given(instance=C_Declarations_ArrayDeclaration_strategy)
def test_c_declarations_arraydeclaration_dimensions_setter(instance):
    original = instance.dimensions
    instance.dimensions = original
    assert instance.dimensions == original

@given(instance=C_Declarations_SimpleVariableDeclaration_strategy)
@settings(max_examples=50)
def test_c_declarations_simplevariabledeclaration_instantiation(instance):
    assert isinstance(instance, C_Declarations_SimpleVariableDeclaration)

@given(instance=C_Main_Block_strategy)
@settings(max_examples=50)
def test_c_main_block_instantiation(instance):
    assert isinstance(instance, C_Main_Block)

@given(instance=Declarations_Declaration_strategy)
@settings(max_examples=50)
def test_declarations_declaration_instantiation(instance):
    assert isinstance(instance, Declarations_Declaration)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=C_Main_DeclarationsBlock_strategy)
@settings(max_examples=50)
def test_c_main_declarationsblock_instantiation(instance):
    assert isinstance(instance, C_Main_DeclarationsBlock)

@given(instance=C_Main_FunctionsBlock_strategy)
@settings(max_examples=50)
def test_c_main_functionsblock_instantiation(instance):
    assert isinstance(instance, C_Main_FunctionsBlock)

@given(instance=C_Main_Function_strategy)
@settings(max_examples=50)
def test_c_main_function_instantiation(instance):
    assert isinstance(instance, C_Main_Function)



@given(instance=C_Main_Function_strategy)
def test_c_main_function_functionModifier_setter(instance):
    original = instance.functionModifier
    instance.functionModifier = original
    assert instance.functionModifier == original



@given(instance=C_Main_Function_strategy)
def test_c_main_function_modifier_setter(instance):
    original = instance.modifier
    instance.modifier = original
    assert instance.modifier == original

@given(instance=Main_DeclarationsBlock_strategy)
@settings(max_examples=50)
def test_main_declarationsblock_instantiation(instance):
    assert isinstance(instance, Main_DeclarationsBlock)

@given(instance=C_Main_H_Unit_strategy)
@settings(max_examples=50)
def test_c_main_h_unit_instantiation(instance):
    assert isinstance(instance, C_Main_H_Unit)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=C_Types_CompositeType_strategy)
@settings(max_examples=50)
def test_c_types_compositetype_instantiation(instance):
    assert isinstance(instance, C_Types_CompositeType)

@given(instance=C_Types_PrimitiveType_strategy)
@settings(max_examples=50)
def test_c_types_primitivetype_instantiation(instance):
    assert isinstance(instance, C_Types_PrimitiveType)

@given(instance=C_Types_Type_strategy)
@settings(max_examples=50)
def test_c_types_type_instantiation(instance):
    assert isinstance(instance, C_Types_Type)
