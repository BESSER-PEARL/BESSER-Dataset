import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    BinaryExpression,
    logo::binary::Plus,
    logo::binary::Mult,
    logo::binary::Div,
    logo::binary::Equals,
    logo::binary::Greater,
    logo::binary::Minus,
    UnaryExpression,
    logo::unary::Opposite,
    logo::unary::Not,
    Constant,
    logo::constant::BoolValue,
    logo::constant::IntValue,
    expression::logo::Expression,
    Expression,
    logo::expression::VariableRead,
    logo::expression::UnaryExpression,
    logo::expression::ExtendedExpression,
    logo::expression::Constant,
    logo::expression::BinaryExpression,
    logo::Statement,
    logo::Logo,
    ProcedureDefinition,
    statement::logo::Statement,
    statement::logo::Parameter,
    statement::logo::Expression,
    Statement,
    logo::statement::ProcedureDefinition,
    logo::statement::Block,
    logo::statement::ControlStatement,
    logo::statement::Left,
    logo::statement::ProcedureCall,
    logo::statement::PenUp,
    logo::statement::PenDown,
    logo::statement::Forward,
    logo::statement::Right,
    logo::Value,
    logo::Symbol,
    logo::Parameter,
    logo::Expression,
    Symbol,
    logo::symbol::Procedure,
    logo::symbol::Variable,
    ExtendedExpression,
    logo::extended::Or,
    logo::extended::And,
    logo::binary::Lower,
    Value,
    logo::value::BoolValue,
    logo::value::IntValue,
    Block,
    ControlStatement,
    logo::control::If,
    logo::control::Repeat,
    logo::control::While,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(BinaryExpression)


def test_binaryexpression_constructor_exists():
    assert callable(BinaryExpression.__init__)


def test_binaryexpression_constructor_args():
    sig = inspect.signature(BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_logo::binary::plus_is_not_abstract():
    assert not inspect.isabstract(logo::binary::Plus)


def test_logo::binary::plus_constructor_exists():
    assert callable(logo::binary::Plus.__init__)


def test_logo::binary::plus_constructor_args():
    sig = inspect.signature(logo::binary::Plus.__init__)
    params = list(sig.parameters.keys())



def test_logo::binary::mult_is_not_abstract():
    assert not inspect.isabstract(logo::binary::Mult)


def test_logo::binary::mult_constructor_exists():
    assert callable(logo::binary::Mult.__init__)


def test_logo::binary::mult_constructor_args():
    sig = inspect.signature(logo::binary::Mult.__init__)
    params = list(sig.parameters.keys())



def test_logo::binary::div_is_not_abstract():
    assert not inspect.isabstract(logo::binary::Div)


def test_logo::binary::div_constructor_exists():
    assert callable(logo::binary::Div.__init__)


def test_logo::binary::div_constructor_args():
    sig = inspect.signature(logo::binary::Div.__init__)
    params = list(sig.parameters.keys())



def test_logo::binary::equals_is_not_abstract():
    assert not inspect.isabstract(logo::binary::Equals)


def test_logo::binary::equals_constructor_exists():
    assert callable(logo::binary::Equals.__init__)


def test_logo::binary::equals_constructor_args():
    sig = inspect.signature(logo::binary::Equals.__init__)
    params = list(sig.parameters.keys())



def test_logo::binary::greater_is_not_abstract():
    assert not inspect.isabstract(logo::binary::Greater)


def test_logo::binary::greater_constructor_exists():
    assert callable(logo::binary::Greater.__init__)


def test_logo::binary::greater_constructor_args():
    sig = inspect.signature(logo::binary::Greater.__init__)
    params = list(sig.parameters.keys())



def test_logo::binary::minus_is_not_abstract():
    assert not inspect.isabstract(logo::binary::Minus)


def test_logo::binary::minus_constructor_exists():
    assert callable(logo::binary::Minus.__init__)


def test_logo::binary::minus_constructor_args():
    sig = inspect.signature(logo::binary::Minus.__init__)
    params = list(sig.parameters.keys())



def test_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(UnaryExpression)


def test_unaryexpression_constructor_exists():
    assert callable(UnaryExpression.__init__)


def test_unaryexpression_constructor_args():
    sig = inspect.signature(UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_logo::unary::opposite_is_not_abstract():
    assert not inspect.isabstract(logo::unary::Opposite)


def test_logo::unary::opposite_constructor_exists():
    assert callable(logo::unary::Opposite.__init__)


def test_logo::unary::opposite_constructor_args():
    sig = inspect.signature(logo::unary::Opposite.__init__)
    params = list(sig.parameters.keys())



def test_logo::unary::not_is_not_abstract():
    assert not inspect.isabstract(logo::unary::Not)


def test_logo::unary::not_constructor_exists():
    assert callable(logo::unary::Not.__init__)


def test_logo::unary::not_constructor_args():
    sig = inspect.signature(logo::unary::Not.__init__)
    params = list(sig.parameters.keys())



def test_constant_is_not_abstract():
    assert not inspect.isabstract(Constant)


def test_constant_constructor_exists():
    assert callable(Constant.__init__)


def test_constant_constructor_args():
    sig = inspect.signature(Constant.__init__)
    params = list(sig.parameters.keys())



def test_logo::constant::boolvalue_is_not_abstract():
    assert not inspect.isabstract(logo::constant::BoolValue)


def test_logo::constant::boolvalue_constructor_exists():
    assert callable(logo::constant::BoolValue.__init__)


def test_logo::constant::boolvalue_constructor_args():
    sig = inspect.signature(logo::constant::BoolValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_logo::constant::boolvalue_has_value():
    assert hasattr(logo::constant::BoolValue, "value")
    descriptor = None
    for klass in logo::constant::BoolValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_logo::constant::intvalue_is_not_abstract():
    assert not inspect.isabstract(logo::constant::IntValue)


def test_logo::constant::intvalue_constructor_exists():
    assert callable(logo::constant::IntValue.__init__)


def test_logo::constant::intvalue_constructor_args():
    sig = inspect.signature(logo::constant::IntValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_logo::constant::intvalue_has_value():
    assert hasattr(logo::constant::IntValue, "value")
    descriptor = None
    for klass in logo::constant::IntValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_expression::logo::expression_is_not_abstract():
    assert not inspect.isabstract(expression::logo::Expression)


def test_expression::logo::expression_constructor_exists():
    assert callable(expression::logo::Expression.__init__)


def test_expression::logo::expression_constructor_args():
    sig = inspect.signature(expression::logo::Expression.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_logo::expression::variableread_is_not_abstract():
    assert not inspect.isabstract(logo::expression::VariableRead)


def test_logo::expression::variableread_constructor_exists():
    assert callable(logo::expression::VariableRead.__init__)


def test_logo::expression::variableread_constructor_args():
    sig = inspect.signature(logo::expression::VariableRead.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_logo::expression::variableread_has_name():
    assert hasattr(logo::expression::VariableRead, "name")
    descriptor = None
    for klass in logo::expression::VariableRead.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_logo::expression::unaryexpression_is_not_abstract():
    assert not inspect.isabstract(logo::expression::UnaryExpression)


def test_logo::expression::unaryexpression_constructor_exists():
    assert callable(logo::expression::UnaryExpression.__init__)


def test_logo::expression::unaryexpression_constructor_args():
    sig = inspect.signature(logo::expression::UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_logo::expression::extendedexpression_is_not_abstract():
    assert not inspect.isabstract(logo::expression::ExtendedExpression)


def test_logo::expression::extendedexpression_constructor_exists():
    assert callable(logo::expression::ExtendedExpression.__init__)


def test_logo::expression::extendedexpression_constructor_args():
    sig = inspect.signature(logo::expression::ExtendedExpression.__init__)
    params = list(sig.parameters.keys())



def test_logo::expression::constant_is_not_abstract():
    assert not inspect.isabstract(logo::expression::Constant)


def test_logo::expression::constant_constructor_exists():
    assert callable(logo::expression::Constant.__init__)


def test_logo::expression::constant_constructor_args():
    sig = inspect.signature(logo::expression::Constant.__init__)
    params = list(sig.parameters.keys())



def test_logo::expression::binaryexpression_is_not_abstract():
    assert not inspect.isabstract(logo::expression::BinaryExpression)


def test_logo::expression::binaryexpression_constructor_exists():
    assert callable(logo::expression::BinaryExpression.__init__)


def test_logo::expression::binaryexpression_constructor_args():
    sig = inspect.signature(logo::expression::BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_logo::statement_is_not_abstract():
    assert not inspect.isabstract(logo::Statement)


def test_logo::statement_constructor_exists():
    assert callable(logo::Statement.__init__)


def test_logo::statement_constructor_args():
    sig = inspect.signature(logo::Statement.__init__)
    params = list(sig.parameters.keys())



def test_logo::logo_is_not_abstract():
    assert not inspect.isabstract(logo::Logo)


def test_logo::logo_constructor_exists():
    assert callable(logo::Logo.__init__)


def test_logo::logo_constructor_args():
    sig = inspect.signature(logo::Logo.__init__)
    params = list(sig.parameters.keys())



def test_proceduredefinition_is_not_abstract():
    assert not inspect.isabstract(ProcedureDefinition)


def test_proceduredefinition_constructor_exists():
    assert callable(ProcedureDefinition.__init__)


def test_proceduredefinition_constructor_args():
    sig = inspect.signature(ProcedureDefinition.__init__)
    params = list(sig.parameters.keys())



def test_statement::logo::statement_is_not_abstract():
    assert not inspect.isabstract(statement::logo::Statement)


def test_statement::logo::statement_constructor_exists():
    assert callable(statement::logo::Statement.__init__)


def test_statement::logo::statement_constructor_args():
    sig = inspect.signature(statement::logo::Statement.__init__)
    params = list(sig.parameters.keys())



def test_statement::logo::parameter_is_not_abstract():
    assert not inspect.isabstract(statement::logo::Parameter)


def test_statement::logo::parameter_constructor_exists():
    assert callable(statement::logo::Parameter.__init__)


def test_statement::logo::parameter_constructor_args():
    sig = inspect.signature(statement::logo::Parameter.__init__)
    params = list(sig.parameters.keys())



def test_statement::logo::expression_is_not_abstract():
    assert not inspect.isabstract(statement::logo::Expression)


def test_statement::logo::expression_constructor_exists():
    assert callable(statement::logo::Expression.__init__)


def test_statement::logo::expression_constructor_args():
    sig = inspect.signature(statement::logo::Expression.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_logo::statement::proceduredefinition_is_not_abstract():
    assert not inspect.isabstract(logo::statement::ProcedureDefinition)


def test_logo::statement::proceduredefinition_constructor_exists():
    assert callable(logo::statement::ProcedureDefinition.__init__)


def test_logo::statement::proceduredefinition_constructor_args():
    sig = inspect.signature(logo::statement::ProcedureDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_logo::statement::proceduredefinition_has_name():
    assert hasattr(logo::statement::ProcedureDefinition, "name")
    descriptor = None
    for klass in logo::statement::ProcedureDefinition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_logo::statement::block_is_not_abstract():
    assert not inspect.isabstract(logo::statement::Block)


def test_logo::statement::block_constructor_exists():
    assert callable(logo::statement::Block.__init__)


def test_logo::statement::block_constructor_args():
    sig = inspect.signature(logo::statement::Block.__init__)
    params = list(sig.parameters.keys())



def test_logo::statement::controlstatement_is_not_abstract():
    assert not inspect.isabstract(logo::statement::ControlStatement)


def test_logo::statement::controlstatement_constructor_exists():
    assert callable(logo::statement::ControlStatement.__init__)


def test_logo::statement::controlstatement_constructor_args():
    sig = inspect.signature(logo::statement::ControlStatement.__init__)
    params = list(sig.parameters.keys())



def test_logo::statement::left_is_not_abstract():
    assert not inspect.isabstract(logo::statement::Left)


def test_logo::statement::left_constructor_exists():
    assert callable(logo::statement::Left.__init__)


def test_logo::statement::left_constructor_args():
    sig = inspect.signature(logo::statement::Left.__init__)
    params = list(sig.parameters.keys())



def test_logo::statement::procedurecall_is_not_abstract():
    assert not inspect.isabstract(logo::statement::ProcedureCall)


def test_logo::statement::procedurecall_constructor_exists():
    assert callable(logo::statement::ProcedureCall.__init__)


def test_logo::statement::procedurecall_constructor_args():
    sig = inspect.signature(logo::statement::ProcedureCall.__init__)
    params = list(sig.parameters.keys())



def test_logo::statement::penup_is_not_abstract():
    assert not inspect.isabstract(logo::statement::PenUp)


def test_logo::statement::penup_constructor_exists():
    assert callable(logo::statement::PenUp.__init__)


def test_logo::statement::penup_constructor_args():
    sig = inspect.signature(logo::statement::PenUp.__init__)
    params = list(sig.parameters.keys())



def test_logo::statement::pendown_is_not_abstract():
    assert not inspect.isabstract(logo::statement::PenDown)


def test_logo::statement::pendown_constructor_exists():
    assert callable(logo::statement::PenDown.__init__)


def test_logo::statement::pendown_constructor_args():
    sig = inspect.signature(logo::statement::PenDown.__init__)
    params = list(sig.parameters.keys())



def test_logo::statement::forward_is_not_abstract():
    assert not inspect.isabstract(logo::statement::Forward)


def test_logo::statement::forward_constructor_exists():
    assert callable(logo::statement::Forward.__init__)


def test_logo::statement::forward_constructor_args():
    sig = inspect.signature(logo::statement::Forward.__init__)
    params = list(sig.parameters.keys())



def test_logo::statement::right_is_not_abstract():
    assert not inspect.isabstract(logo::statement::Right)


def test_logo::statement::right_constructor_exists():
    assert callable(logo::statement::Right.__init__)


def test_logo::statement::right_constructor_args():
    sig = inspect.signature(logo::statement::Right.__init__)
    params = list(sig.parameters.keys())



def test_logo::value_is_not_abstract():
    assert not inspect.isabstract(logo::Value)


def test_logo::value_constructor_exists():
    assert callable(logo::Value.__init__)


def test_logo::value_constructor_args():
    sig = inspect.signature(logo::Value.__init__)
    params = list(sig.parameters.keys())



def test_logo::symbol_is_not_abstract():
    assert not inspect.isabstract(logo::Symbol)


def test_logo::symbol_constructor_exists():
    assert callable(logo::Symbol.__init__)


def test_logo::symbol_constructor_args():
    sig = inspect.signature(logo::Symbol.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_logo::symbol_has_name():
    assert hasattr(logo::Symbol, "name")
    descriptor = None
    for klass in logo::Symbol.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_logo::parameter_is_not_abstract():
    assert not inspect.isabstract(logo::Parameter)


def test_logo::parameter_constructor_exists():
    assert callable(logo::Parameter.__init__)


def test_logo::parameter_constructor_args():
    sig = inspect.signature(logo::Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_logo::parameter_has_name():
    assert hasattr(logo::Parameter, "name")
    descriptor = None
    for klass in logo::Parameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_logo::expression_is_not_abstract():
    assert not inspect.isabstract(logo::Expression)


def test_logo::expression_constructor_exists():
    assert callable(logo::Expression.__init__)


def test_logo::expression_constructor_args():
    sig = inspect.signature(logo::Expression.__init__)
    params = list(sig.parameters.keys())



def test_symbol_is_not_abstract():
    assert not inspect.isabstract(Symbol)


def test_symbol_constructor_exists():
    assert callable(Symbol.__init__)


def test_symbol_constructor_args():
    sig = inspect.signature(Symbol.__init__)
    params = list(sig.parameters.keys())



def test_logo::symbol::procedure_is_not_abstract():
    assert not inspect.isabstract(logo::symbol::Procedure)


def test_logo::symbol::procedure_constructor_exists():
    assert callable(logo::symbol::Procedure.__init__)


def test_logo::symbol::procedure_constructor_args():
    sig = inspect.signature(logo::symbol::Procedure.__init__)
    params = list(sig.parameters.keys())



def test_logo::symbol::variable_is_not_abstract():
    assert not inspect.isabstract(logo::symbol::Variable)


def test_logo::symbol::variable_constructor_exists():
    assert callable(logo::symbol::Variable.__init__)


def test_logo::symbol::variable_constructor_args():
    sig = inspect.signature(logo::symbol::Variable.__init__)
    params = list(sig.parameters.keys())



def test_extendedexpression_is_not_abstract():
    assert not inspect.isabstract(ExtendedExpression)


def test_extendedexpression_constructor_exists():
    assert callable(ExtendedExpression.__init__)


def test_extendedexpression_constructor_args():
    sig = inspect.signature(ExtendedExpression.__init__)
    params = list(sig.parameters.keys())



def test_logo::extended::or_is_not_abstract():
    assert not inspect.isabstract(logo::extended::Or)


def test_logo::extended::or_constructor_exists():
    assert callable(logo::extended::Or.__init__)


def test_logo::extended::or_constructor_args():
    sig = inspect.signature(logo::extended::Or.__init__)
    params = list(sig.parameters.keys())



def test_logo::extended::and_is_not_abstract():
    assert not inspect.isabstract(logo::extended::And)


def test_logo::extended::and_constructor_exists():
    assert callable(logo::extended::And.__init__)


def test_logo::extended::and_constructor_args():
    sig = inspect.signature(logo::extended::And.__init__)
    params = list(sig.parameters.keys())



def test_logo::binary::lower_is_not_abstract():
    assert not inspect.isabstract(logo::binary::Lower)


def test_logo::binary::lower_constructor_exists():
    assert callable(logo::binary::Lower.__init__)


def test_logo::binary::lower_constructor_args():
    sig = inspect.signature(logo::binary::Lower.__init__)
    params = list(sig.parameters.keys())



def test_value_is_not_abstract():
    assert not inspect.isabstract(Value)


def test_value_constructor_exists():
    assert callable(Value.__init__)


def test_value_constructor_args():
    sig = inspect.signature(Value.__init__)
    params = list(sig.parameters.keys())



def test_logo::value::boolvalue_is_not_abstract():
    assert not inspect.isabstract(logo::value::BoolValue)


def test_logo::value::boolvalue_constructor_exists():
    assert callable(logo::value::BoolValue.__init__)


def test_logo::value::boolvalue_constructor_args():
    sig = inspect.signature(logo::value::BoolValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_logo::value::boolvalue_has_value():
    assert hasattr(logo::value::BoolValue, "value")
    descriptor = None
    for klass in logo::value::BoolValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_logo::value::intvalue_is_not_abstract():
    assert not inspect.isabstract(logo::value::IntValue)


def test_logo::value::intvalue_constructor_exists():
    assert callable(logo::value::IntValue.__init__)


def test_logo::value::intvalue_constructor_args():
    sig = inspect.signature(logo::value::IntValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_logo::value::intvalue_has_value():
    assert hasattr(logo::value::IntValue, "value")
    descriptor = None
    for klass in logo::value::IntValue.__mro__:
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



def test_logo::control::if_is_not_abstract():
    assert not inspect.isabstract(logo::control::If)


def test_logo::control::if_constructor_exists():
    assert callable(logo::control::If.__init__)


def test_logo::control::if_constructor_args():
    sig = inspect.signature(logo::control::If.__init__)
    params = list(sig.parameters.keys())



def test_logo::control::repeat_is_not_abstract():
    assert not inspect.isabstract(logo::control::Repeat)


def test_logo::control::repeat_constructor_exists():
    assert callable(logo::control::Repeat.__init__)


def test_logo::control::repeat_constructor_args():
    sig = inspect.signature(logo::control::Repeat.__init__)
    params = list(sig.parameters.keys())



def test_logo::control::while_is_not_abstract():
    assert not inspect.isabstract(logo::control::While)


def test_logo::control::while_constructor_exists():
    assert callable(logo::control::While.__init__)


def test_logo::control::while_constructor_args():
    sig = inspect.signature(logo::control::While.__init__)
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
BinaryExpression_strategy = st.builds(
    BinaryExpression,
)
logo::binary::Plus_strategy = st.builds(
    logo::binary::Plus,
)
logo::binary::Mult_strategy = st.builds(
    logo::binary::Mult,
)
logo::binary::Div_strategy = st.builds(
    logo::binary::Div,
)
logo::binary::Equals_strategy = st.builds(
    logo::binary::Equals,
)
logo::binary::Greater_strategy = st.builds(
    logo::binary::Greater,
)
logo::binary::Minus_strategy = st.builds(
    logo::binary::Minus,
)
UnaryExpression_strategy = st.builds(
    UnaryExpression,
)
logo::unary::Opposite_strategy = st.builds(
    logo::unary::Opposite,
)
logo::unary::Not_strategy = st.builds(
    logo::unary::Not,
)
Constant_strategy = st.builds(
    Constant,
)
logo::constant::BoolValue_strategy = st.builds(
    logo::constant::BoolValue,
    value=
        st.booleans()
)
logo::constant::IntValue_strategy = st.builds(
    logo::constant::IntValue,
    value=
        st.integers()
)
expression::logo::Expression_strategy = st.builds(
    expression::logo::Expression,
)
Expression_strategy = st.builds(
    Expression,
)
logo::expression::VariableRead_strategy = st.builds(
    logo::expression::VariableRead,
    name=
        safe_text
)
logo::expression::UnaryExpression_strategy = st.builds(
    logo::expression::UnaryExpression,
)
logo::expression::ExtendedExpression_strategy = st.builds(
    logo::expression::ExtendedExpression,
)
logo::expression::Constant_strategy = st.builds(
    logo::expression::Constant,
)
logo::expression::BinaryExpression_strategy = st.builds(
    logo::expression::BinaryExpression,
)
logo::Statement_strategy = st.builds(
    logo::Statement,
)
logo::Logo_strategy = st.builds(
    logo::Logo,
)
ProcedureDefinition_strategy = st.builds(
    ProcedureDefinition,
)
statement::logo::Statement_strategy = st.builds(
    statement::logo::Statement,
)
statement::logo::Parameter_strategy = st.builds(
    statement::logo::Parameter,
)
statement::logo::Expression_strategy = st.builds(
    statement::logo::Expression,
)
Statement_strategy = st.builds(
    Statement,
)
logo::statement::ProcedureDefinition_strategy = st.builds(
    logo::statement::ProcedureDefinition,
    name=
        safe_text
)
logo::statement::Block_strategy = st.builds(
    logo::statement::Block,
)
logo::statement::ControlStatement_strategy = st.builds(
    logo::statement::ControlStatement,
)
logo::statement::Left_strategy = st.builds(
    logo::statement::Left,
)
logo::statement::ProcedureCall_strategy = st.builds(
    logo::statement::ProcedureCall,
)
logo::statement::PenUp_strategy = st.builds(
    logo::statement::PenUp,
)
logo::statement::PenDown_strategy = st.builds(
    logo::statement::PenDown,
)
logo::statement::Forward_strategy = st.builds(
    logo::statement::Forward,
)
logo::statement::Right_strategy = st.builds(
    logo::statement::Right,
)
logo::Value_strategy = st.builds(
    logo::Value,
)
logo::Symbol_strategy = st.builds(
    logo::Symbol,
    name=
        safe_text
)
logo::Parameter_strategy = st.builds(
    logo::Parameter,
    name=
        safe_text
)
logo::Expression_strategy = st.builds(
    logo::Expression,
)
Symbol_strategy = st.builds(
    Symbol,
)
logo::symbol::Procedure_strategy = st.builds(
    logo::symbol::Procedure,
)
logo::symbol::Variable_strategy = st.builds(
    logo::symbol::Variable,
)
ExtendedExpression_strategy = st.builds(
    ExtendedExpression,
)
logo::extended::Or_strategy = st.builds(
    logo::extended::Or,
)
logo::extended::And_strategy = st.builds(
    logo::extended::And,
)
logo::binary::Lower_strategy = st.builds(
    logo::binary::Lower,
)
Value_strategy = st.builds(
    Value,
)
logo::value::BoolValue_strategy = st.builds(
    logo::value::BoolValue,
    value=
        st.booleans()
)
logo::value::IntValue_strategy = st.builds(
    logo::value::IntValue,
    value=
        st.integers()
)
Block_strategy = st.builds(
    Block,
)
ControlStatement_strategy = st.builds(
    ControlStatement,
)
logo::control::If_strategy = st.builds(
    logo::control::If,
)
logo::control::Repeat_strategy = st.builds(
    logo::control::Repeat,
)
logo::control::While_strategy = st.builds(
    logo::control::While,
)

@given(instance=BinaryExpression_strategy)
@settings(max_examples=50)
def test_binaryexpression_instantiation(instance):
    assert isinstance(instance, BinaryExpression)

@given(instance=logo::binary::Plus_strategy)
@settings(max_examples=50)
def test_logo::binary::plus_instantiation(instance):
    assert isinstance(instance, logo::binary::Plus)

@given(instance=logo::binary::Mult_strategy)
@settings(max_examples=50)
def test_logo::binary::mult_instantiation(instance):
    assert isinstance(instance, logo::binary::Mult)

@given(instance=logo::binary::Div_strategy)
@settings(max_examples=50)
def test_logo::binary::div_instantiation(instance):
    assert isinstance(instance, logo::binary::Div)

@given(instance=logo::binary::Equals_strategy)
@settings(max_examples=50)
def test_logo::binary::equals_instantiation(instance):
    assert isinstance(instance, logo::binary::Equals)

@given(instance=logo::binary::Greater_strategy)
@settings(max_examples=50)
def test_logo::binary::greater_instantiation(instance):
    assert isinstance(instance, logo::binary::Greater)

@given(instance=logo::binary::Minus_strategy)
@settings(max_examples=50)
def test_logo::binary::minus_instantiation(instance):
    assert isinstance(instance, logo::binary::Minus)

@given(instance=UnaryExpression_strategy)
@settings(max_examples=50)
def test_unaryexpression_instantiation(instance):
    assert isinstance(instance, UnaryExpression)

@given(instance=logo::unary::Opposite_strategy)
@settings(max_examples=50)
def test_logo::unary::opposite_instantiation(instance):
    assert isinstance(instance, logo::unary::Opposite)

@given(instance=logo::unary::Not_strategy)
@settings(max_examples=50)
def test_logo::unary::not_instantiation(instance):
    assert isinstance(instance, logo::unary::Not)

@given(instance=Constant_strategy)
@settings(max_examples=50)
def test_constant_instantiation(instance):
    assert isinstance(instance, Constant)

@given(instance=logo::constant::BoolValue_strategy)
@settings(max_examples=50)
def test_logo::constant::boolvalue_instantiation(instance):
    assert isinstance(instance, logo::constant::BoolValue)

@given(instance=logo::constant::BoolValue_strategy)
def test_logo::constant::boolvalue_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=logo::constant::BoolValue_strategy)
def test_logo::constant::boolvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=logo::constant::IntValue_strategy)
@settings(max_examples=50)
def test_logo::constant::intvalue_instantiation(instance):
    assert isinstance(instance, logo::constant::IntValue)

@given(instance=logo::constant::IntValue_strategy)
def test_logo::constant::intvalue_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=logo::constant::IntValue_strategy)
def test_logo::constant::intvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=expression::logo::Expression_strategy)
@settings(max_examples=50)
def test_expression::logo::expression_instantiation(instance):
    assert isinstance(instance, expression::logo::Expression)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=logo::expression::VariableRead_strategy)
@settings(max_examples=50)
def test_logo::expression::variableread_instantiation(instance):
    assert isinstance(instance, logo::expression::VariableRead)

@given(instance=logo::expression::VariableRead_strategy)
def test_logo::expression::variableread_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=logo::expression::VariableRead_strategy)
def test_logo::expression::variableread_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=logo::expression::UnaryExpression_strategy)
@settings(max_examples=50)
def test_logo::expression::unaryexpression_instantiation(instance):
    assert isinstance(instance, logo::expression::UnaryExpression)

@given(instance=logo::expression::ExtendedExpression_strategy)
@settings(max_examples=50)
def test_logo::expression::extendedexpression_instantiation(instance):
    assert isinstance(instance, logo::expression::ExtendedExpression)

@given(instance=logo::expression::Constant_strategy)
@settings(max_examples=50)
def test_logo::expression::constant_instantiation(instance):
    assert isinstance(instance, logo::expression::Constant)

@given(instance=logo::expression::BinaryExpression_strategy)
@settings(max_examples=50)
def test_logo::expression::binaryexpression_instantiation(instance):
    assert isinstance(instance, logo::expression::BinaryExpression)

@given(instance=logo::Statement_strategy)
@settings(max_examples=50)
def test_logo::statement_instantiation(instance):
    assert isinstance(instance, logo::Statement)

@given(instance=logo::Logo_strategy)
@settings(max_examples=50)
def test_logo::logo_instantiation(instance):
    assert isinstance(instance, logo::Logo)

@given(instance=ProcedureDefinition_strategy)
@settings(max_examples=50)
def test_proceduredefinition_instantiation(instance):
    assert isinstance(instance, ProcedureDefinition)

@given(instance=statement::logo::Statement_strategy)
@settings(max_examples=50)
def test_statement::logo::statement_instantiation(instance):
    assert isinstance(instance, statement::logo::Statement)

@given(instance=statement::logo::Parameter_strategy)
@settings(max_examples=50)
def test_statement::logo::parameter_instantiation(instance):
    assert isinstance(instance, statement::logo::Parameter)

@given(instance=statement::logo::Expression_strategy)
@settings(max_examples=50)
def test_statement::logo::expression_instantiation(instance):
    assert isinstance(instance, statement::logo::Expression)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=logo::statement::ProcedureDefinition_strategy)
@settings(max_examples=50)
def test_logo::statement::proceduredefinition_instantiation(instance):
    assert isinstance(instance, logo::statement::ProcedureDefinition)

@given(instance=logo::statement::ProcedureDefinition_strategy)
def test_logo::statement::proceduredefinition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=logo::statement::ProcedureDefinition_strategy)
def test_logo::statement::proceduredefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=logo::statement::Block_strategy)
@settings(max_examples=50)
def test_logo::statement::block_instantiation(instance):
    assert isinstance(instance, logo::statement::Block)

@given(instance=logo::statement::ControlStatement_strategy)
@settings(max_examples=50)
def test_logo::statement::controlstatement_instantiation(instance):
    assert isinstance(instance, logo::statement::ControlStatement)

@given(instance=logo::statement::Left_strategy)
@settings(max_examples=50)
def test_logo::statement::left_instantiation(instance):
    assert isinstance(instance, logo::statement::Left)

@given(instance=logo::statement::ProcedureCall_strategy)
@settings(max_examples=50)
def test_logo::statement::procedurecall_instantiation(instance):
    assert isinstance(instance, logo::statement::ProcedureCall)

@given(instance=logo::statement::PenUp_strategy)
@settings(max_examples=50)
def test_logo::statement::penup_instantiation(instance):
    assert isinstance(instance, logo::statement::PenUp)

@given(instance=logo::statement::PenDown_strategy)
@settings(max_examples=50)
def test_logo::statement::pendown_instantiation(instance):
    assert isinstance(instance, logo::statement::PenDown)

@given(instance=logo::statement::Forward_strategy)
@settings(max_examples=50)
def test_logo::statement::forward_instantiation(instance):
    assert isinstance(instance, logo::statement::Forward)

@given(instance=logo::statement::Right_strategy)
@settings(max_examples=50)
def test_logo::statement::right_instantiation(instance):
    assert isinstance(instance, logo::statement::Right)

@given(instance=logo::Value_strategy)
@settings(max_examples=50)
def test_logo::value_instantiation(instance):
    assert isinstance(instance, logo::Value)

@given(instance=logo::Symbol_strategy)
@settings(max_examples=50)
def test_logo::symbol_instantiation(instance):
    assert isinstance(instance, logo::Symbol)

@given(instance=logo::Symbol_strategy)
def test_logo::symbol_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=logo::Symbol_strategy)
def test_logo::symbol_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=logo::Parameter_strategy)
@settings(max_examples=50)
def test_logo::parameter_instantiation(instance):
    assert isinstance(instance, logo::Parameter)

@given(instance=logo::Parameter_strategy)
def test_logo::parameter_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=logo::Parameter_strategy)
def test_logo::parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=logo::Expression_strategy)
@settings(max_examples=50)
def test_logo::expression_instantiation(instance):
    assert isinstance(instance, logo::Expression)

@given(instance=Symbol_strategy)
@settings(max_examples=50)
def test_symbol_instantiation(instance):
    assert isinstance(instance, Symbol)

@given(instance=logo::symbol::Procedure_strategy)
@settings(max_examples=50)
def test_logo::symbol::procedure_instantiation(instance):
    assert isinstance(instance, logo::symbol::Procedure)

@given(instance=logo::symbol::Variable_strategy)
@settings(max_examples=50)
def test_logo::symbol::variable_instantiation(instance):
    assert isinstance(instance, logo::symbol::Variable)

@given(instance=ExtendedExpression_strategy)
@settings(max_examples=50)
def test_extendedexpression_instantiation(instance):
    assert isinstance(instance, ExtendedExpression)

@given(instance=logo::extended::Or_strategy)
@settings(max_examples=50)
def test_logo::extended::or_instantiation(instance):
    assert isinstance(instance, logo::extended::Or)

@given(instance=logo::extended::And_strategy)
@settings(max_examples=50)
def test_logo::extended::and_instantiation(instance):
    assert isinstance(instance, logo::extended::And)

@given(instance=logo::binary::Lower_strategy)
@settings(max_examples=50)
def test_logo::binary::lower_instantiation(instance):
    assert isinstance(instance, logo::binary::Lower)

@given(instance=Value_strategy)
@settings(max_examples=50)
def test_value_instantiation(instance):
    assert isinstance(instance, Value)

@given(instance=logo::value::BoolValue_strategy)
@settings(max_examples=50)
def test_logo::value::boolvalue_instantiation(instance):
    assert isinstance(instance, logo::value::BoolValue)

@given(instance=logo::value::BoolValue_strategy)
def test_logo::value::boolvalue_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=logo::value::BoolValue_strategy)
def test_logo::value::boolvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=logo::value::IntValue_strategy)
@settings(max_examples=50)
def test_logo::value::intvalue_instantiation(instance):
    assert isinstance(instance, logo::value::IntValue)

@given(instance=logo::value::IntValue_strategy)
def test_logo::value::intvalue_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=logo::value::IntValue_strategy)
def test_logo::value::intvalue_value_setter(instance):
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

@given(instance=logo::control::If_strategy)
@settings(max_examples=50)
def test_logo::control::if_instantiation(instance):
    assert isinstance(instance, logo::control::If)

@given(instance=logo::control::Repeat_strategy)
@settings(max_examples=50)
def test_logo::control::repeat_instantiation(instance):
    assert isinstance(instance, logo::control::Repeat)

@given(instance=logo::control::While_strategy)
@settings(max_examples=50)
def test_logo::control::while_instantiation(instance):
    assert isinstance(instance, logo::control::While)
