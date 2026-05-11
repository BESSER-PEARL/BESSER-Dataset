import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    kmLogo::Expression,
    Primitive,
    kmLogo::Forward,
    kmLogo::Back,
    Instruction,
    kmLogo::Primitive,
    kmLogo::Instruction,
    kmLogo::VarDecl,
    kmLogo::LogoProgram,
    Literal,
    kmLogo::BoolLit,
    kmLogo::StringLit,
    kmLogo::IntegerLit,
    Expression,
    kmLogo::VarReference,
    kmLogo::ArithmeticExpression,
    kmLogo::RelationalExpression,
    kmLogo::Literal,
    kmLogo::Clear,
    kmLogo::PenUp,
    kmLogo::PenDown,
    kmLogo::Right,
    kmLogo::Left,
    ArithmeticOperator,
    RelationalOperator,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_kmlogo::expression_is_not_abstract():
    assert not inspect.isabstract(kmLogo::Expression)


def test_kmlogo::expression_constructor_exists():
    assert callable(kmLogo::Expression.__init__)


def test_kmlogo::expression_constructor_args():
    sig = inspect.signature(kmLogo::Expression.__init__)
    params = list(sig.parameters.keys())



def test_primitive_is_not_abstract():
    assert not inspect.isabstract(Primitive)


def test_primitive_constructor_exists():
    assert callable(Primitive.__init__)


def test_primitive_constructor_args():
    sig = inspect.signature(Primitive.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::forward_is_not_abstract():
    assert not inspect.isabstract(kmLogo::Forward)


def test_kmlogo::forward_constructor_exists():
    assert callable(kmLogo::Forward.__init__)


def test_kmlogo::forward_constructor_args():
    sig = inspect.signature(kmLogo::Forward.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::back_is_not_abstract():
    assert not inspect.isabstract(kmLogo::Back)


def test_kmlogo::back_constructor_exists():
    assert callable(kmLogo::Back.__init__)


def test_kmlogo::back_constructor_args():
    sig = inspect.signature(kmLogo::Back.__init__)
    params = list(sig.parameters.keys())



def test_instruction_is_not_abstract():
    assert not inspect.isabstract(Instruction)


def test_instruction_constructor_exists():
    assert callable(Instruction.__init__)


def test_instruction_constructor_args():
    sig = inspect.signature(Instruction.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::primitive_is_not_abstract():
    assert not inspect.isabstract(kmLogo::Primitive)


def test_kmlogo::primitive_constructor_exists():
    assert callable(kmLogo::Primitive.__init__)


def test_kmlogo::primitive_constructor_args():
    sig = inspect.signature(kmLogo::Primitive.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::instruction_is_not_abstract():
    assert not inspect.isabstract(kmLogo::Instruction)


def test_kmlogo::instruction_constructor_exists():
    assert callable(kmLogo::Instruction.__init__)


def test_kmlogo::instruction_constructor_args():
    sig = inspect.signature(kmLogo::Instruction.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::vardecl_is_not_abstract():
    assert not inspect.isabstract(kmLogo::VarDecl)


def test_kmlogo::vardecl_constructor_exists():
    assert callable(kmLogo::VarDecl.__init__)


def test_kmlogo::vardecl_constructor_args():
    sig = inspect.signature(kmLogo::VarDecl.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"

def test_kmlogo::vardecl_has_key():
    assert hasattr(kmLogo::VarDecl, "key")
    descriptor = None
    for klass in kmLogo::VarDecl.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_kmlogo::logoprogram_is_not_abstract():
    assert not inspect.isabstract(kmLogo::LogoProgram)


def test_kmlogo::logoprogram_constructor_exists():
    assert callable(kmLogo::LogoProgram.__init__)


def test_kmlogo::logoprogram_constructor_args():
    sig = inspect.signature(kmLogo::LogoProgram.__init__)
    params = list(sig.parameters.keys())



def test_literal_is_not_abstract():
    assert not inspect.isabstract(Literal)


def test_literal_constructor_exists():
    assert callable(Literal.__init__)


def test_literal_constructor_args():
    sig = inspect.signature(Literal.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::boollit_is_not_abstract():
    assert not inspect.isabstract(kmLogo::BoolLit)


def test_kmlogo::boollit_constructor_exists():
    assert callable(kmLogo::BoolLit.__init__)


def test_kmlogo::boollit_constructor_args():
    sig = inspect.signature(kmLogo::BoolLit.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_kmlogo::boollit_has_value():
    assert hasattr(kmLogo::BoolLit, "value")
    descriptor = None
    for klass in kmLogo::BoolLit.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_kmlogo::stringlit_is_not_abstract():
    assert not inspect.isabstract(kmLogo::StringLit)


def test_kmlogo::stringlit_constructor_exists():
    assert callable(kmLogo::StringLit.__init__)


def test_kmlogo::stringlit_constructor_args():
    sig = inspect.signature(kmLogo::StringLit.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_kmlogo::stringlit_has_value():
    assert hasattr(kmLogo::StringLit, "value")
    descriptor = None
    for klass in kmLogo::StringLit.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_kmlogo::integerlit_is_not_abstract():
    assert not inspect.isabstract(kmLogo::IntegerLit)


def test_kmlogo::integerlit_constructor_exists():
    assert callable(kmLogo::IntegerLit.__init__)


def test_kmlogo::integerlit_constructor_args():
    sig = inspect.signature(kmLogo::IntegerLit.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_kmlogo::integerlit_has_value():
    assert hasattr(kmLogo::IntegerLit, "value")
    descriptor = None
    for klass in kmLogo::IntegerLit.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::varreference_is_not_abstract():
    assert not inspect.isabstract(kmLogo::VarReference)


def test_kmlogo::varreference_constructor_exists():
    assert callable(kmLogo::VarReference.__init__)


def test_kmlogo::varreference_constructor_args():
    sig = inspect.signature(kmLogo::VarReference.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"

def test_kmlogo::varreference_has_key():
    assert hasattr(kmLogo::VarReference, "key")
    descriptor = None
    for klass in kmLogo::VarReference.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_kmlogo::arithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(kmLogo::ArithmeticExpression)


def test_kmlogo::arithmeticexpression_constructor_exists():
    assert callable(kmLogo::ArithmeticExpression.__init__)


def test_kmlogo::arithmeticexpression_constructor_args():
    sig = inspect.signature(kmLogo::ArithmeticExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_kmlogo::arithmeticexpression_has_operator():
    assert hasattr(kmLogo::ArithmeticExpression, "operator")
    descriptor = None
    for klass in kmLogo::ArithmeticExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_kmlogo::relationalexpression_is_not_abstract():
    assert not inspect.isabstract(kmLogo::RelationalExpression)


def test_kmlogo::relationalexpression_constructor_exists():
    assert callable(kmLogo::RelationalExpression.__init__)


def test_kmlogo::relationalexpression_constructor_args():
    sig = inspect.signature(kmLogo::RelationalExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_kmlogo::relationalexpression_has_operator():
    assert hasattr(kmLogo::RelationalExpression, "operator")
    descriptor = None
    for klass in kmLogo::RelationalExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_kmlogo::literal_is_not_abstract():
    assert not inspect.isabstract(kmLogo::Literal)


def test_kmlogo::literal_constructor_exists():
    assert callable(kmLogo::Literal.__init__)


def test_kmlogo::literal_constructor_args():
    sig = inspect.signature(kmLogo::Literal.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::clear_is_not_abstract():
    assert not inspect.isabstract(kmLogo::Clear)


def test_kmlogo::clear_constructor_exists():
    assert callable(kmLogo::Clear.__init__)


def test_kmlogo::clear_constructor_args():
    sig = inspect.signature(kmLogo::Clear.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::penup_is_not_abstract():
    assert not inspect.isabstract(kmLogo::PenUp)


def test_kmlogo::penup_constructor_exists():
    assert callable(kmLogo::PenUp.__init__)


def test_kmlogo::penup_constructor_args():
    sig = inspect.signature(kmLogo::PenUp.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::pendown_is_not_abstract():
    assert not inspect.isabstract(kmLogo::PenDown)


def test_kmlogo::pendown_constructor_exists():
    assert callable(kmLogo::PenDown.__init__)


def test_kmlogo::pendown_constructor_args():
    sig = inspect.signature(kmLogo::PenDown.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::right_is_not_abstract():
    assert not inspect.isabstract(kmLogo::Right)


def test_kmlogo::right_constructor_exists():
    assert callable(kmLogo::Right.__init__)


def test_kmlogo::right_constructor_args():
    sig = inspect.signature(kmLogo::Right.__init__)
    params = list(sig.parameters.keys())



def test_kmlogo::left_is_not_abstract():
    assert not inspect.isabstract(kmLogo::Left)


def test_kmlogo::left_constructor_exists():
    assert callable(kmLogo::Left.__init__)


def test_kmlogo::left_constructor_args():
    sig = inspect.signature(kmLogo::Left.__init__)
    params = list(sig.parameters.keys())

def test_arithmeticoperator_exists():
    # Check that the Enumeration exists
    assert ArithmeticOperator is not None

def test_arithmeticoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ArithmeticOperator]
    expected_literals = [
        "div",
        "plus",
        "minus",
        "mult",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ArithmeticOperator"

def test_relationaloperator_exists():
    # Check that the Enumeration exists
    assert RelationalOperator is not None

def test_relationaloperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RelationalOperator]
    expected_literals = [
        "notEqual",
        "greaterThan",
        "lessThan",
        "equals",
        "lessThanOrEqualTo",
        "greaterThanOrEqualTo",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RelationalOperator"


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
kmLogo::Expression_strategy = st.builds(
    kmLogo::Expression,
)
Primitive_strategy = st.builds(
    Primitive,
)
kmLogo::Forward_strategy = st.builds(
    kmLogo::Forward,
)
kmLogo::Back_strategy = st.builds(
    kmLogo::Back,
)
Instruction_strategy = st.builds(
    Instruction,
)
kmLogo::Primitive_strategy = st.builds(
    kmLogo::Primitive,
)
kmLogo::Instruction_strategy = st.builds(
    kmLogo::Instruction,
)
kmLogo::VarDecl_strategy = st.builds(
    kmLogo::VarDecl,
    key=
        safe_text
)
kmLogo::LogoProgram_strategy = st.builds(
    kmLogo::LogoProgram,
)
Literal_strategy = st.builds(
    Literal,
)
kmLogo::BoolLit_strategy = st.builds(
    kmLogo::BoolLit,
    value=
        st.booleans()
)
kmLogo::StringLit_strategy = st.builds(
    kmLogo::StringLit,
    value=
        safe_text
)
kmLogo::IntegerLit_strategy = st.builds(
    kmLogo::IntegerLit,
    value=
        st.integers()
)
Expression_strategy = st.builds(
    Expression,
)
kmLogo::VarReference_strategy = st.builds(
    kmLogo::VarReference,
    key=
        safe_text
)
kmLogo::ArithmeticExpression_strategy = st.builds(
    kmLogo::ArithmeticExpression,
    operator=
        safe_text
)
kmLogo::RelationalExpression_strategy = st.builds(
    kmLogo::RelationalExpression,
    operator=
        safe_text
)
kmLogo::Literal_strategy = st.builds(
    kmLogo::Literal,
)
kmLogo::Clear_strategy = st.builds(
    kmLogo::Clear,
)
kmLogo::PenUp_strategy = st.builds(
    kmLogo::PenUp,
)
kmLogo::PenDown_strategy = st.builds(
    kmLogo::PenDown,
)
kmLogo::Right_strategy = st.builds(
    kmLogo::Right,
)
kmLogo::Left_strategy = st.builds(
    kmLogo::Left,
)

@given(instance=kmLogo::Expression_strategy)
@settings(max_examples=50)
def test_kmlogo::expression_instantiation(instance):
    assert isinstance(instance, kmLogo::Expression)

@given(instance=Primitive_strategy)
@settings(max_examples=50)
def test_primitive_instantiation(instance):
    assert isinstance(instance, Primitive)

@given(instance=kmLogo::Forward_strategy)
@settings(max_examples=50)
def test_kmlogo::forward_instantiation(instance):
    assert isinstance(instance, kmLogo::Forward)

@given(instance=kmLogo::Back_strategy)
@settings(max_examples=50)
def test_kmlogo::back_instantiation(instance):
    assert isinstance(instance, kmLogo::Back)

@given(instance=Instruction_strategy)
@settings(max_examples=50)
def test_instruction_instantiation(instance):
    assert isinstance(instance, Instruction)

@given(instance=kmLogo::Primitive_strategy)
@settings(max_examples=50)
def test_kmlogo::primitive_instantiation(instance):
    assert isinstance(instance, kmLogo::Primitive)

@given(instance=kmLogo::Instruction_strategy)
@settings(max_examples=50)
def test_kmlogo::instruction_instantiation(instance):
    assert isinstance(instance, kmLogo::Instruction)

@given(instance=kmLogo::VarDecl_strategy)
@settings(max_examples=50)
def test_kmlogo::vardecl_instantiation(instance):
    assert isinstance(instance, kmLogo::VarDecl)

@given(instance=kmLogo::VarDecl_strategy)
def test_kmlogo::vardecl_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=kmLogo::VarDecl_strategy)
def test_kmlogo::vardecl_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=kmLogo::LogoProgram_strategy)
@settings(max_examples=50)
def test_kmlogo::logoprogram_instantiation(instance):
    assert isinstance(instance, kmLogo::LogoProgram)

@given(instance=Literal_strategy)
@settings(max_examples=50)
def test_literal_instantiation(instance):
    assert isinstance(instance, Literal)

@given(instance=kmLogo::BoolLit_strategy)
@settings(max_examples=50)
def test_kmlogo::boollit_instantiation(instance):
    assert isinstance(instance, kmLogo::BoolLit)

@given(instance=kmLogo::BoolLit_strategy)
def test_kmlogo::boollit_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=kmLogo::BoolLit_strategy)
def test_kmlogo::boollit_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=kmLogo::StringLit_strategy)
@settings(max_examples=50)
def test_kmlogo::stringlit_instantiation(instance):
    assert isinstance(instance, kmLogo::StringLit)

@given(instance=kmLogo::StringLit_strategy)
def test_kmlogo::stringlit_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=kmLogo::StringLit_strategy)
def test_kmlogo::stringlit_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=kmLogo::IntegerLit_strategy)
@settings(max_examples=50)
def test_kmlogo::integerlit_instantiation(instance):
    assert isinstance(instance, kmLogo::IntegerLit)

@given(instance=kmLogo::IntegerLit_strategy)
def test_kmlogo::integerlit_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=kmLogo::IntegerLit_strategy)
def test_kmlogo::integerlit_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=kmLogo::VarReference_strategy)
@settings(max_examples=50)
def test_kmlogo::varreference_instantiation(instance):
    assert isinstance(instance, kmLogo::VarReference)

@given(instance=kmLogo::VarReference_strategy)
def test_kmlogo::varreference_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=kmLogo::VarReference_strategy)
def test_kmlogo::varreference_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=kmLogo::ArithmeticExpression_strategy)
@settings(max_examples=50)
def test_kmlogo::arithmeticexpression_instantiation(instance):
    assert isinstance(instance, kmLogo::ArithmeticExpression)

@given(instance=kmLogo::ArithmeticExpression_strategy)
def test_kmlogo::arithmeticexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=kmLogo::ArithmeticExpression_strategy)
def test_kmlogo::arithmeticexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=kmLogo::RelationalExpression_strategy)
@settings(max_examples=50)
def test_kmlogo::relationalexpression_instantiation(instance):
    assert isinstance(instance, kmLogo::RelationalExpression)

@given(instance=kmLogo::RelationalExpression_strategy)
def test_kmlogo::relationalexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=kmLogo::RelationalExpression_strategy)
def test_kmlogo::relationalexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=kmLogo::Literal_strategy)
@settings(max_examples=50)
def test_kmlogo::literal_instantiation(instance):
    assert isinstance(instance, kmLogo::Literal)

@given(instance=kmLogo::Clear_strategy)
@settings(max_examples=50)
def test_kmlogo::clear_instantiation(instance):
    assert isinstance(instance, kmLogo::Clear)

@given(instance=kmLogo::PenUp_strategy)
@settings(max_examples=50)
def test_kmlogo::penup_instantiation(instance):
    assert isinstance(instance, kmLogo::PenUp)

@given(instance=kmLogo::PenDown_strategy)
@settings(max_examples=50)
def test_kmlogo::pendown_instantiation(instance):
    assert isinstance(instance, kmLogo::PenDown)

@given(instance=kmLogo::Right_strategy)
@settings(max_examples=50)
def test_kmlogo::right_instantiation(instance):
    assert isinstance(instance, kmLogo::Right)

@given(instance=kmLogo::Left_strategy)
@settings(max_examples=50)
def test_kmlogo::left_instantiation(instance):
    assert isinstance(instance, kmLogo::Left)
