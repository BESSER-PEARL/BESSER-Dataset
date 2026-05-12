import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    statement_logo_Expression,
    Statement,
    logo_statement_Left,
    logo_statement_PenDown,
    logo_statement_Forward,
    logo_statement_Right,
    logo_Value,
    logo_Symbol,
    logo_Parameter,
    logo_Expression,
    Symbol,
    logo_symbol_Procedure,
    logo_symbol_Variable,
    ExtendedExpression,
    logo_extended_Or,
    logo_extended_And,
    Value,
    logo_value_BoolValue,
    logo_value_IntValue,
    Block,
    ControlStatement,
    logo_control_While,
    logo_control_If,
    BinaryExpression,
    logo_binary_Lower,
    logo_binary_Mult,
    logo_binary_Equals,
    logo_binary_Greater,
    logo_binary_Plus,
    logo_binary_Div,
    logo_binary_Minus,
    UnaryExpression,
    logo_unary_Opposite,
    logo_unary_Not,
    Constant,
    logo_constant_BoolValue,
    logo_constant_IntValue,
    expression_logo_Expression,
    Expression,
    logo_expression_ExtendedExpression,
    logo_expression_VariableRead,
    logo_expression_UnaryExpression,
    logo_expression_Constant,
    logo_expression_BinaryExpression,
    logo_control_Repeat,
    logo_Statement,
    logo_Logo,
    logo_statement_ControlStatement,
    logo_statement_Block,
    ProcedureDefinition,
    logo_statement_ProcedureCall,
    statement_logo_Statement,
    statement_logo_Parameter,
    logo_statement_ProcedureDefinition,
    logo_statement_PenUp,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statement_logo_expression_is_not_abstract():
    assert not inspect.isabstract(statement_logo_Expression)


def test_statement_logo_expression_constructor_exists():
    assert callable(statement_logo_Expression.__init__)


def test_statement_logo_expression_constructor_args():
    sig = inspect.signature(statement_logo_Expression.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_logo_statement_left_is_not_abstract():
    assert not inspect.isabstract(logo_statement_Left)


def test_logo_statement_left_constructor_exists():
    assert callable(logo_statement_Left.__init__)


def test_logo_statement_left_constructor_args():
    sig = inspect.signature(logo_statement_Left.__init__)
    params = list(sig.parameters.keys())



def test_logo_statement_pendown_is_not_abstract():
    assert not inspect.isabstract(logo_statement_PenDown)


def test_logo_statement_pendown_constructor_exists():
    assert callable(logo_statement_PenDown.__init__)


def test_logo_statement_pendown_constructor_args():
    sig = inspect.signature(logo_statement_PenDown.__init__)
    params = list(sig.parameters.keys())



def test_logo_statement_forward_is_not_abstract():
    assert not inspect.isabstract(logo_statement_Forward)


def test_logo_statement_forward_constructor_exists():
    assert callable(logo_statement_Forward.__init__)


def test_logo_statement_forward_constructor_args():
    sig = inspect.signature(logo_statement_Forward.__init__)
    params = list(sig.parameters.keys())



def test_logo_statement_right_is_not_abstract():
    assert not inspect.isabstract(logo_statement_Right)


def test_logo_statement_right_constructor_exists():
    assert callable(logo_statement_Right.__init__)


def test_logo_statement_right_constructor_args():
    sig = inspect.signature(logo_statement_Right.__init__)
    params = list(sig.parameters.keys())



def test_logo_value_is_not_abstract():
    assert not inspect.isabstract(logo_Value)


def test_logo_value_constructor_exists():
    assert callable(logo_Value.__init__)


def test_logo_value_constructor_args():
    sig = inspect.signature(logo_Value.__init__)
    params = list(sig.parameters.keys())



def test_logo_symbol_is_not_abstract():
    assert not inspect.isabstract(logo_Symbol)


def test_logo_symbol_constructor_exists():
    assert callable(logo_Symbol.__init__)


def test_logo_symbol_constructor_args():
    sig = inspect.signature(logo_Symbol.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_logo_symbol_has_name():
    assert hasattr(logo_Symbol, "name")
    descriptor = None
    for klass in logo_Symbol.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_logo_parameter_is_not_abstract():
    assert not inspect.isabstract(logo_Parameter)


def test_logo_parameter_constructor_exists():
    assert callable(logo_Parameter.__init__)


def test_logo_parameter_constructor_args():
    sig = inspect.signature(logo_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_logo_parameter_has_name():
    assert hasattr(logo_Parameter, "name")
    descriptor = None
    for klass in logo_Parameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_logo_expression_is_not_abstract():
    assert not inspect.isabstract(logo_Expression)


def test_logo_expression_constructor_exists():
    assert callable(logo_Expression.__init__)


def test_logo_expression_constructor_args():
    sig = inspect.signature(logo_Expression.__init__)
    params = list(sig.parameters.keys())



def test_symbol_is_not_abstract():
    assert not inspect.isabstract(Symbol)


def test_symbol_constructor_exists():
    assert callable(Symbol.__init__)


def test_symbol_constructor_args():
    sig = inspect.signature(Symbol.__init__)
    params = list(sig.parameters.keys())



def test_logo_symbol_procedure_is_not_abstract():
    assert not inspect.isabstract(logo_symbol_Procedure)


def test_logo_symbol_procedure_constructor_exists():
    assert callable(logo_symbol_Procedure.__init__)


def test_logo_symbol_procedure_constructor_args():
    sig = inspect.signature(logo_symbol_Procedure.__init__)
    params = list(sig.parameters.keys())



def test_logo_symbol_variable_is_not_abstract():
    assert not inspect.isabstract(logo_symbol_Variable)


def test_logo_symbol_variable_constructor_exists():
    assert callable(logo_symbol_Variable.__init__)


def test_logo_symbol_variable_constructor_args():
    sig = inspect.signature(logo_symbol_Variable.__init__)
    params = list(sig.parameters.keys())



def test_extendedexpression_is_not_abstract():
    assert not inspect.isabstract(ExtendedExpression)


def test_extendedexpression_constructor_exists():
    assert callable(ExtendedExpression.__init__)


def test_extendedexpression_constructor_args():
    sig = inspect.signature(ExtendedExpression.__init__)
    params = list(sig.parameters.keys())



def test_logo_extended_or_is_not_abstract():
    assert not inspect.isabstract(logo_extended_Or)


def test_logo_extended_or_constructor_exists():
    assert callable(logo_extended_Or.__init__)


def test_logo_extended_or_constructor_args():
    sig = inspect.signature(logo_extended_Or.__init__)
    params = list(sig.parameters.keys())



def test_logo_extended_and_is_not_abstract():
    assert not inspect.isabstract(logo_extended_And)


def test_logo_extended_and_constructor_exists():
    assert callable(logo_extended_And.__init__)


def test_logo_extended_and_constructor_args():
    sig = inspect.signature(logo_extended_And.__init__)
    params = list(sig.parameters.keys())



def test_value_is_not_abstract():
    assert not inspect.isabstract(Value)


def test_value_constructor_exists():
    assert callable(Value.__init__)


def test_value_constructor_args():
    sig = inspect.signature(Value.__init__)
    params = list(sig.parameters.keys())



def test_logo_value_boolvalue_is_not_abstract():
    assert not inspect.isabstract(logo_value_BoolValue)


def test_logo_value_boolvalue_constructor_exists():
    assert callable(logo_value_BoolValue.__init__)


def test_logo_value_boolvalue_constructor_args():
    sig = inspect.signature(logo_value_BoolValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_logo_value_boolvalue_has_value():
    assert hasattr(logo_value_BoolValue, "value")
    descriptor = None
    for klass in logo_value_BoolValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_logo_value_intvalue_is_not_abstract():
    assert not inspect.isabstract(logo_value_IntValue)


def test_logo_value_intvalue_constructor_exists():
    assert callable(logo_value_IntValue.__init__)


def test_logo_value_intvalue_constructor_args():
    sig = inspect.signature(logo_value_IntValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_logo_value_intvalue_has_value():
    assert hasattr(logo_value_IntValue, "value")
    descriptor = None
    for klass in logo_value_IntValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_block_is_not_abstract():
    assert not inspect.isabstract(Block)


def test_block_constructor_exists():
    assert callable(Block.__init__)


def test_block_constructor_args():
    sig = inspect.signature(Block.__init__)
    params = list(sig.parameters.keys())



def test_controlstatement_is_not_abstract():
    assert not inspect.isabstract(ControlStatement)


def test_controlstatement_constructor_exists():
    assert callable(ControlStatement.__init__)


def test_controlstatement_constructor_args():
    sig = inspect.signature(ControlStatement.__init__)
    params = list(sig.parameters.keys())



def test_logo_control_while_is_not_abstract():
    assert not inspect.isabstract(logo_control_While)


def test_logo_control_while_constructor_exists():
    assert callable(logo_control_While.__init__)


def test_logo_control_while_constructor_args():
    sig = inspect.signature(logo_control_While.__init__)
    params = list(sig.parameters.keys())



def test_logo_control_if_is_not_abstract():
    assert not inspect.isabstract(logo_control_If)


def test_logo_control_if_constructor_exists():
    assert callable(logo_control_If.__init__)


def test_logo_control_if_constructor_args():
    sig = inspect.signature(logo_control_If.__init__)
    params = list(sig.parameters.keys())



def test_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(BinaryExpression)


def test_binaryexpression_constructor_exists():
    assert callable(BinaryExpression.__init__)


def test_binaryexpression_constructor_args():
    sig = inspect.signature(BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_logo_binary_lower_is_not_abstract():
    assert not inspect.isabstract(logo_binary_Lower)


def test_logo_binary_lower_constructor_exists():
    assert callable(logo_binary_Lower.__init__)


def test_logo_binary_lower_constructor_args():
    sig = inspect.signature(logo_binary_Lower.__init__)
    params = list(sig.parameters.keys())



def test_logo_binary_mult_is_not_abstract():
    assert not inspect.isabstract(logo_binary_Mult)


def test_logo_binary_mult_constructor_exists():
    assert callable(logo_binary_Mult.__init__)


def test_logo_binary_mult_constructor_args():
    sig = inspect.signature(logo_binary_Mult.__init__)
    params = list(sig.parameters.keys())



def test_logo_binary_equals_is_not_abstract():
    assert not inspect.isabstract(logo_binary_Equals)


def test_logo_binary_equals_constructor_exists():
    assert callable(logo_binary_Equals.__init__)


def test_logo_binary_equals_constructor_args():
    sig = inspect.signature(logo_binary_Equals.__init__)
    params = list(sig.parameters.keys())



def test_logo_binary_greater_is_not_abstract():
    assert not inspect.isabstract(logo_binary_Greater)


def test_logo_binary_greater_constructor_exists():
    assert callable(logo_binary_Greater.__init__)


def test_logo_binary_greater_constructor_args():
    sig = inspect.signature(logo_binary_Greater.__init__)
    params = list(sig.parameters.keys())



def test_logo_binary_plus_is_not_abstract():
    assert not inspect.isabstract(logo_binary_Plus)


def test_logo_binary_plus_constructor_exists():
    assert callable(logo_binary_Plus.__init__)


def test_logo_binary_plus_constructor_args():
    sig = inspect.signature(logo_binary_Plus.__init__)
    params = list(sig.parameters.keys())



def test_logo_binary_div_is_not_abstract():
    assert not inspect.isabstract(logo_binary_Div)


def test_logo_binary_div_constructor_exists():
    assert callable(logo_binary_Div.__init__)


def test_logo_binary_div_constructor_args():
    sig = inspect.signature(logo_binary_Div.__init__)
    params = list(sig.parameters.keys())



def test_logo_binary_minus_is_not_abstract():
    assert not inspect.isabstract(logo_binary_Minus)


def test_logo_binary_minus_constructor_exists():
    assert callable(logo_binary_Minus.__init__)


def test_logo_binary_minus_constructor_args():
    sig = inspect.signature(logo_binary_Minus.__init__)
    params = list(sig.parameters.keys())



def test_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(UnaryExpression)


def test_unaryexpression_constructor_exists():
    assert callable(UnaryExpression.__init__)


def test_unaryexpression_constructor_args():
    sig = inspect.signature(UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_logo_unary_opposite_is_not_abstract():
    assert not inspect.isabstract(logo_unary_Opposite)


def test_logo_unary_opposite_constructor_exists():
    assert callable(logo_unary_Opposite.__init__)


def test_logo_unary_opposite_constructor_args():
    sig = inspect.signature(logo_unary_Opposite.__init__)
    params = list(sig.parameters.keys())



def test_logo_unary_not_is_not_abstract():
    assert not inspect.isabstract(logo_unary_Not)


def test_logo_unary_not_constructor_exists():
    assert callable(logo_unary_Not.__init__)


def test_logo_unary_not_constructor_args():
    sig = inspect.signature(logo_unary_Not.__init__)
    params = list(sig.parameters.keys())



def test_constant_is_not_abstract():
    assert not inspect.isabstract(Constant)


def test_constant_constructor_exists():
    assert callable(Constant.__init__)


def test_constant_constructor_args():
    sig = inspect.signature(Constant.__init__)
    params = list(sig.parameters.keys())



def test_logo_constant_boolvalue_is_not_abstract():
    assert not inspect.isabstract(logo_constant_BoolValue)


def test_logo_constant_boolvalue_constructor_exists():
    assert callable(logo_constant_BoolValue.__init__)


def test_logo_constant_boolvalue_constructor_args():
    sig = inspect.signature(logo_constant_BoolValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_logo_constant_boolvalue_has_value():
    assert hasattr(logo_constant_BoolValue, "value")
    descriptor = None
    for klass in logo_constant_BoolValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_logo_constant_intvalue_is_not_abstract():
    assert not inspect.isabstract(logo_constant_IntValue)


def test_logo_constant_intvalue_constructor_exists():
    assert callable(logo_constant_IntValue.__init__)


def test_logo_constant_intvalue_constructor_args():
    sig = inspect.signature(logo_constant_IntValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_logo_constant_intvalue_has_value():
    assert hasattr(logo_constant_IntValue, "value")
    descriptor = None
    for klass in logo_constant_IntValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_expression_logo_expression_is_not_abstract():
    assert not inspect.isabstract(expression_logo_Expression)


def test_expression_logo_expression_constructor_exists():
    assert callable(expression_logo_Expression.__init__)


def test_expression_logo_expression_constructor_args():
    sig = inspect.signature(expression_logo_Expression.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_logo_expression_extendedexpression_is_not_abstract():
    assert not inspect.isabstract(logo_expression_ExtendedExpression)


def test_logo_expression_extendedexpression_constructor_exists():
    assert callable(logo_expression_ExtendedExpression.__init__)


def test_logo_expression_extendedexpression_constructor_args():
    sig = inspect.signature(logo_expression_ExtendedExpression.__init__)
    params = list(sig.parameters.keys())



def test_logo_expression_variableread_is_not_abstract():
    assert not inspect.isabstract(logo_expression_VariableRead)


def test_logo_expression_variableread_constructor_exists():
    assert callable(logo_expression_VariableRead.__init__)


def test_logo_expression_variableread_constructor_args():
    sig = inspect.signature(logo_expression_VariableRead.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_logo_expression_variableread_has_name():
    assert hasattr(logo_expression_VariableRead, "name")
    descriptor = None
    for klass in logo_expression_VariableRead.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_logo_expression_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(logo_expression_UnaryExpression)


def test_logo_expression_unaryexpression_constructor_exists():
    assert callable(logo_expression_UnaryExpression.__init__)


def test_logo_expression_unaryexpression_constructor_args():
    sig = inspect.signature(logo_expression_UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_logo_expression_constant_is_not_abstract():
    assert not inspect.isabstract(logo_expression_Constant)


def test_logo_expression_constant_constructor_exists():
    assert callable(logo_expression_Constant.__init__)


def test_logo_expression_constant_constructor_args():
    sig = inspect.signature(logo_expression_Constant.__init__)
    params = list(sig.parameters.keys())



def test_logo_expression_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(logo_expression_BinaryExpression)


def test_logo_expression_binaryexpression_constructor_exists():
    assert callable(logo_expression_BinaryExpression.__init__)


def test_logo_expression_binaryexpression_constructor_args():
    sig = inspect.signature(logo_expression_BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_logo_control_repeat_is_not_abstract():
    assert not inspect.isabstract(logo_control_Repeat)


def test_logo_control_repeat_constructor_exists():
    assert callable(logo_control_Repeat.__init__)


def test_logo_control_repeat_constructor_args():
    sig = inspect.signature(logo_control_Repeat.__init__)
    params = list(sig.parameters.keys())



def test_logo_statement_is_not_abstract():
    assert not inspect.isabstract(logo_Statement)


def test_logo_statement_constructor_exists():
    assert callable(logo_Statement.__init__)


def test_logo_statement_constructor_args():
    sig = inspect.signature(logo_Statement.__init__)
    params = list(sig.parameters.keys())



def test_logo_logo_is_not_abstract():
    assert not inspect.isabstract(logo_Logo)


def test_logo_logo_constructor_exists():
    assert callable(logo_Logo.__init__)


def test_logo_logo_constructor_args():
    sig = inspect.signature(logo_Logo.__init__)
    params = list(sig.parameters.keys())



def test_logo_statement_controlstatement_is_not_abstract():
    assert not inspect.isabstract(logo_statement_ControlStatement)


def test_logo_statement_controlstatement_constructor_exists():
    assert callable(logo_statement_ControlStatement.__init__)


def test_logo_statement_controlstatement_constructor_args():
    sig = inspect.signature(logo_statement_ControlStatement.__init__)
    params = list(sig.parameters.keys())



def test_logo_statement_block_is_not_abstract():
    assert not inspect.isabstract(logo_statement_Block)


def test_logo_statement_block_constructor_exists():
    assert callable(logo_statement_Block.__init__)


def test_logo_statement_block_constructor_args():
    sig = inspect.signature(logo_statement_Block.__init__)
    params = list(sig.parameters.keys())



def test_proceduredefinition_is_not_abstract():
    assert not inspect.isabstract(ProcedureDefinition)


def test_proceduredefinition_constructor_exists():
    assert callable(ProcedureDefinition.__init__)


def test_proceduredefinition_constructor_args():
    sig = inspect.signature(ProcedureDefinition.__init__)
    params = list(sig.parameters.keys())



def test_logo_statement_procedurecall_is_not_abstract():
    assert not inspect.isabstract(logo_statement_ProcedureCall)


def test_logo_statement_procedurecall_constructor_exists():
    assert callable(logo_statement_ProcedureCall.__init__)


def test_logo_statement_procedurecall_constructor_args():
    sig = inspect.signature(logo_statement_ProcedureCall.__init__)
    params = list(sig.parameters.keys())



def test_statement_logo_statement_is_not_abstract():
    assert not inspect.isabstract(statement_logo_Statement)


def test_statement_logo_statement_constructor_exists():
    assert callable(statement_logo_Statement.__init__)


def test_statement_logo_statement_constructor_args():
    sig = inspect.signature(statement_logo_Statement.__init__)
    params = list(sig.parameters.keys())



def test_statement_logo_parameter_is_not_abstract():
    assert not inspect.isabstract(statement_logo_Parameter)


def test_statement_logo_parameter_constructor_exists():
    assert callable(statement_logo_Parameter.__init__)


def test_statement_logo_parameter_constructor_args():
    sig = inspect.signature(statement_logo_Parameter.__init__)
    params = list(sig.parameters.keys())



def test_logo_statement_proceduredefinition_is_not_abstract():
    assert not inspect.isabstract(logo_statement_ProcedureDefinition)


def test_logo_statement_proceduredefinition_constructor_exists():
    assert callable(logo_statement_ProcedureDefinition.__init__)


def test_logo_statement_proceduredefinition_constructor_args():
    sig = inspect.signature(logo_statement_ProcedureDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_logo_statement_proceduredefinition_has_name():
    assert hasattr(logo_statement_ProcedureDefinition, "name")
    descriptor = None
    for klass in logo_statement_ProcedureDefinition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_logo_statement_penup_is_not_abstract():
    assert not inspect.isabstract(logo_statement_PenUp)


def test_logo_statement_penup_constructor_exists():
    assert callable(logo_statement_PenUp.__init__)


def test_logo_statement_penup_constructor_args():
    sig = inspect.signature(logo_statement_PenUp.__init__)
    params = list(sig.parameters.keys())


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
statement_logo_Expression_strategy = st.builds(
    statement_logo_Expression,
)
Statement_strategy = st.builds(
    Statement,
)
logo_statement_Left_strategy = st.builds(
    logo_statement_Left,
)
logo_statement_PenDown_strategy = st.builds(
    logo_statement_PenDown,
)
logo_statement_Forward_strategy = st.builds(
    logo_statement_Forward,
)
logo_statement_Right_strategy = st.builds(
    logo_statement_Right,
)
logo_Value_strategy = st.builds(
    logo_Value,
)
logo_Symbol_strategy = st.builds(
    logo_Symbol,
    name=
        safe_text
)
logo_Parameter_strategy = st.builds(
    logo_Parameter,
    name=
        safe_text
)
logo_Expression_strategy = st.builds(
    logo_Expression,
)
Symbol_strategy = st.builds(
    Symbol,
)
logo_symbol_Procedure_strategy = st.builds(
    logo_symbol_Procedure,
)
logo_symbol_Variable_strategy = st.builds(
    logo_symbol_Variable,
)
ExtendedExpression_strategy = st.builds(
    ExtendedExpression,
)
logo_extended_Or_strategy = st.builds(
    logo_extended_Or,
)
logo_extended_And_strategy = st.builds(
    logo_extended_And,
)
Value_strategy = st.builds(
    Value,
)
logo_value_BoolValue_strategy = st.builds(
    logo_value_BoolValue,
    value=
        st.booleans()
)
logo_value_IntValue_strategy = st.builds(
    logo_value_IntValue,
    value=
        st.integers()
)
Block_strategy = st.builds(
    Block,
)
ControlStatement_strategy = st.builds(
    ControlStatement,
)
logo_control_While_strategy = st.builds(
    logo_control_While,
)
logo_control_If_strategy = st.builds(
    logo_control_If,
)
BinaryExpression_strategy = st.builds(
    BinaryExpression,
)
logo_binary_Lower_strategy = st.builds(
    logo_binary_Lower,
)
logo_binary_Mult_strategy = st.builds(
    logo_binary_Mult,
)
logo_binary_Equals_strategy = st.builds(
    logo_binary_Equals,
)
logo_binary_Greater_strategy = st.builds(
    logo_binary_Greater,
)
logo_binary_Plus_strategy = st.builds(
    logo_binary_Plus,
)
logo_binary_Div_strategy = st.builds(
    logo_binary_Div,
)
logo_binary_Minus_strategy = st.builds(
    logo_binary_Minus,
)
UnaryExpression_strategy = st.builds(
    UnaryExpression,
)
logo_unary_Opposite_strategy = st.builds(
    logo_unary_Opposite,
)
logo_unary_Not_strategy = st.builds(
    logo_unary_Not,
)
Constant_strategy = st.builds(
    Constant,
)
logo_constant_BoolValue_strategy = st.builds(
    logo_constant_BoolValue,
    value=
        st.booleans()
)
logo_constant_IntValue_strategy = st.builds(
    logo_constant_IntValue,
    value=
        st.integers()
)
expression_logo_Expression_strategy = st.builds(
    expression_logo_Expression,
)
Expression_strategy = st.builds(
    Expression,
)
logo_expression_ExtendedExpression_strategy = st.builds(
    logo_expression_ExtendedExpression,
)
logo_expression_VariableRead_strategy = st.builds(
    logo_expression_VariableRead,
    name=
        safe_text
)
logo_expression_UnaryExpression_strategy = st.builds(
    logo_expression_UnaryExpression,
)
logo_expression_Constant_strategy = st.builds(
    logo_expression_Constant,
)
logo_expression_BinaryExpression_strategy = st.builds(
    logo_expression_BinaryExpression,
)
logo_control_Repeat_strategy = st.builds(
    logo_control_Repeat,
)
logo_Statement_strategy = st.builds(
    logo_Statement,
)
logo_Logo_strategy = st.builds(
    logo_Logo,
)
logo_statement_ControlStatement_strategy = st.builds(
    logo_statement_ControlStatement,
)
logo_statement_Block_strategy = st.builds(
    logo_statement_Block,
)
ProcedureDefinition_strategy = st.builds(
    ProcedureDefinition,
)
logo_statement_ProcedureCall_strategy = st.builds(
    logo_statement_ProcedureCall,
)
statement_logo_Statement_strategy = st.builds(
    statement_logo_Statement,
)
statement_logo_Parameter_strategy = st.builds(
    statement_logo_Parameter,
)
logo_statement_ProcedureDefinition_strategy = st.builds(
    logo_statement_ProcedureDefinition,
    name=
        safe_text
)
logo_statement_PenUp_strategy = st.builds(
    logo_statement_PenUp,
)

@given(instance=statement_logo_Expression_strategy)
@settings(max_examples=50)
def test_statement_logo_expression_instantiation(instance):
    assert isinstance(instance, statement_logo_Expression)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=logo_statement_Left_strategy)
@settings(max_examples=50)
def test_logo_statement_left_instantiation(instance):
    assert isinstance(instance, logo_statement_Left)

@given(instance=logo_statement_PenDown_strategy)
@settings(max_examples=50)
def test_logo_statement_pendown_instantiation(instance):
    assert isinstance(instance, logo_statement_PenDown)

@given(instance=logo_statement_Forward_strategy)
@settings(max_examples=50)
def test_logo_statement_forward_instantiation(instance):
    assert isinstance(instance, logo_statement_Forward)

@given(instance=logo_statement_Right_strategy)
@settings(max_examples=50)
def test_logo_statement_right_instantiation(instance):
    assert isinstance(instance, logo_statement_Right)

@given(instance=logo_Value_strategy)
@settings(max_examples=50)
def test_logo_value_instantiation(instance):
    assert isinstance(instance, logo_Value)

@given(instance=logo_Symbol_strategy)
@settings(max_examples=50)
def test_logo_symbol_instantiation(instance):
    assert isinstance(instance, logo_Symbol)



@given(instance=logo_Symbol_strategy)
def test_logo_symbol_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=logo_Parameter_strategy)
@settings(max_examples=50)
def test_logo_parameter_instantiation(instance):
    assert isinstance(instance, logo_Parameter)



@given(instance=logo_Parameter_strategy)
def test_logo_parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=logo_Expression_strategy)
@settings(max_examples=50)
def test_logo_expression_instantiation(instance):
    assert isinstance(instance, logo_Expression)

@given(instance=Symbol_strategy)
@settings(max_examples=50)
def test_symbol_instantiation(instance):
    assert isinstance(instance, Symbol)

@given(instance=logo_symbol_Procedure_strategy)
@settings(max_examples=50)
def test_logo_symbol_procedure_instantiation(instance):
    assert isinstance(instance, logo_symbol_Procedure)

@given(instance=logo_symbol_Variable_strategy)
@settings(max_examples=50)
def test_logo_symbol_variable_instantiation(instance):
    assert isinstance(instance, logo_symbol_Variable)

@given(instance=ExtendedExpression_strategy)
@settings(max_examples=50)
def test_extendedexpression_instantiation(instance):
    assert isinstance(instance, ExtendedExpression)

@given(instance=logo_extended_Or_strategy)
@settings(max_examples=50)
def test_logo_extended_or_instantiation(instance):
    assert isinstance(instance, logo_extended_Or)

@given(instance=logo_extended_And_strategy)
@settings(max_examples=50)
def test_logo_extended_and_instantiation(instance):
    assert isinstance(instance, logo_extended_And)

@given(instance=Value_strategy)
@settings(max_examples=50)
def test_value_instantiation(instance):
    assert isinstance(instance, Value)

@given(instance=logo_value_BoolValue_strategy)
@settings(max_examples=50)
def test_logo_value_boolvalue_instantiation(instance):
    assert isinstance(instance, logo_value_BoolValue)



@given(instance=logo_value_BoolValue_strategy)
def test_logo_value_boolvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=logo_value_IntValue_strategy)
@settings(max_examples=50)
def test_logo_value_intvalue_instantiation(instance):
    assert isinstance(instance, logo_value_IntValue)



@given(instance=logo_value_IntValue_strategy)
def test_logo_value_intvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Block_strategy)
@settings(max_examples=50)
def test_block_instantiation(instance):
    assert isinstance(instance, Block)

@given(instance=ControlStatement_strategy)
@settings(max_examples=50)
def test_controlstatement_instantiation(instance):
    assert isinstance(instance, ControlStatement)

@given(instance=logo_control_While_strategy)
@settings(max_examples=50)
def test_logo_control_while_instantiation(instance):
    assert isinstance(instance, logo_control_While)

@given(instance=logo_control_If_strategy)
@settings(max_examples=50)
def test_logo_control_if_instantiation(instance):
    assert isinstance(instance, logo_control_If)

@given(instance=BinaryExpression_strategy)
@settings(max_examples=50)
def test_binaryexpression_instantiation(instance):
    assert isinstance(instance, BinaryExpression)

@given(instance=logo_binary_Lower_strategy)
@settings(max_examples=50)
def test_logo_binary_lower_instantiation(instance):
    assert isinstance(instance, logo_binary_Lower)

@given(instance=logo_binary_Mult_strategy)
@settings(max_examples=50)
def test_logo_binary_mult_instantiation(instance):
    assert isinstance(instance, logo_binary_Mult)

@given(instance=logo_binary_Equals_strategy)
@settings(max_examples=50)
def test_logo_binary_equals_instantiation(instance):
    assert isinstance(instance, logo_binary_Equals)

@given(instance=logo_binary_Greater_strategy)
@settings(max_examples=50)
def test_logo_binary_greater_instantiation(instance):
    assert isinstance(instance, logo_binary_Greater)

@given(instance=logo_binary_Plus_strategy)
@settings(max_examples=50)
def test_logo_binary_plus_instantiation(instance):
    assert isinstance(instance, logo_binary_Plus)

@given(instance=logo_binary_Div_strategy)
@settings(max_examples=50)
def test_logo_binary_div_instantiation(instance):
    assert isinstance(instance, logo_binary_Div)

@given(instance=logo_binary_Minus_strategy)
@settings(max_examples=50)
def test_logo_binary_minus_instantiation(instance):
    assert isinstance(instance, logo_binary_Minus)

@given(instance=UnaryExpression_strategy)
@settings(max_examples=50)
def test_unaryexpression_instantiation(instance):
    assert isinstance(instance, UnaryExpression)

@given(instance=logo_unary_Opposite_strategy)
@settings(max_examples=50)
def test_logo_unary_opposite_instantiation(instance):
    assert isinstance(instance, logo_unary_Opposite)

@given(instance=logo_unary_Not_strategy)
@settings(max_examples=50)
def test_logo_unary_not_instantiation(instance):
    assert isinstance(instance, logo_unary_Not)

@given(instance=Constant_strategy)
@settings(max_examples=50)
def test_constant_instantiation(instance):
    assert isinstance(instance, Constant)

@given(instance=logo_constant_BoolValue_strategy)
@settings(max_examples=50)
def test_logo_constant_boolvalue_instantiation(instance):
    assert isinstance(instance, logo_constant_BoolValue)



@given(instance=logo_constant_BoolValue_strategy)
def test_logo_constant_boolvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=logo_constant_IntValue_strategy)
@settings(max_examples=50)
def test_logo_constant_intvalue_instantiation(instance):
    assert isinstance(instance, logo_constant_IntValue)



@given(instance=logo_constant_IntValue_strategy)
def test_logo_constant_intvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=expression_logo_Expression_strategy)
@settings(max_examples=50)
def test_expression_logo_expression_instantiation(instance):
    assert isinstance(instance, expression_logo_Expression)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=logo_expression_ExtendedExpression_strategy)
@settings(max_examples=50)
def test_logo_expression_extendedexpression_instantiation(instance):
    assert isinstance(instance, logo_expression_ExtendedExpression)

@given(instance=logo_expression_VariableRead_strategy)
@settings(max_examples=50)
def test_logo_expression_variableread_instantiation(instance):
    assert isinstance(instance, logo_expression_VariableRead)



@given(instance=logo_expression_VariableRead_strategy)
def test_logo_expression_variableread_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=logo_expression_UnaryExpression_strategy)
@settings(max_examples=50)
def test_logo_expression_unaryexpression_instantiation(instance):
    assert isinstance(instance, logo_expression_UnaryExpression)

@given(instance=logo_expression_Constant_strategy)
@settings(max_examples=50)
def test_logo_expression_constant_instantiation(instance):
    assert isinstance(instance, logo_expression_Constant)

@given(instance=logo_expression_BinaryExpression_strategy)
@settings(max_examples=50)
def test_logo_expression_binaryexpression_instantiation(instance):
    assert isinstance(instance, logo_expression_BinaryExpression)

@given(instance=logo_control_Repeat_strategy)
@settings(max_examples=50)
def test_logo_control_repeat_instantiation(instance):
    assert isinstance(instance, logo_control_Repeat)

@given(instance=logo_Statement_strategy)
@settings(max_examples=50)
def test_logo_statement_instantiation(instance):
    assert isinstance(instance, logo_Statement)

@given(instance=logo_Logo_strategy)
@settings(max_examples=50)
def test_logo_logo_instantiation(instance):
    assert isinstance(instance, logo_Logo)

@given(instance=logo_statement_ControlStatement_strategy)
@settings(max_examples=50)
def test_logo_statement_controlstatement_instantiation(instance):
    assert isinstance(instance, logo_statement_ControlStatement)

@given(instance=logo_statement_Block_strategy)
@settings(max_examples=50)
def test_logo_statement_block_instantiation(instance):
    assert isinstance(instance, logo_statement_Block)

@given(instance=ProcedureDefinition_strategy)
@settings(max_examples=50)
def test_proceduredefinition_instantiation(instance):
    assert isinstance(instance, ProcedureDefinition)

@given(instance=logo_statement_ProcedureCall_strategy)
@settings(max_examples=50)
def test_logo_statement_procedurecall_instantiation(instance):
    assert isinstance(instance, logo_statement_ProcedureCall)

@given(instance=statement_logo_Statement_strategy)
@settings(max_examples=50)
def test_statement_logo_statement_instantiation(instance):
    assert isinstance(instance, statement_logo_Statement)

@given(instance=statement_logo_Parameter_strategy)
@settings(max_examples=50)
def test_statement_logo_parameter_instantiation(instance):
    assert isinstance(instance, statement_logo_Parameter)

@given(instance=logo_statement_ProcedureDefinition_strategy)
@settings(max_examples=50)
def test_logo_statement_proceduredefinition_instantiation(instance):
    assert isinstance(instance, logo_statement_ProcedureDefinition)



@given(instance=logo_statement_ProcedureDefinition_strategy)
def test_logo_statement_proceduredefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=logo_statement_PenUp_strategy)
@settings(max_examples=50)
def test_logo_statement_penup_instantiation(instance):
    assert isinstance(instance, logo_statement_PenUp)
