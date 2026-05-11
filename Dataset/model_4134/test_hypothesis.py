import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Expression,
    mathCompiler::Mult,
    mathCompiler::Num,
    mathCompiler::Let,
    mathCompiler::Minus,
    mathCompiler::External,
    mathCompiler::Var,
    mathCompiler::Div,
    mathCompiler::Plus,
    mathCompiler::Expression,
    mathCompiler::MathExp,
    mathCompiler::Expressions,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_mathcompiler::mult_is_not_abstract():
    assert not inspect.isabstract(mathCompiler::Mult)


def test_mathcompiler::mult_constructor_exists():
    assert callable(mathCompiler::Mult.__init__)


def test_mathcompiler::mult_constructor_args():
    sig = inspect.signature(mathCompiler::Mult.__init__)
    params = list(sig.parameters.keys())



def test_mathcompiler::num_is_not_abstract():
    assert not inspect.isabstract(mathCompiler::Num)


def test_mathcompiler::num_constructor_exists():
    assert callable(mathCompiler::Num.__init__)


def test_mathcompiler::num_constructor_args():
    sig = inspect.signature(mathCompiler::Num.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_mathcompiler::num_has_value():
    assert hasattr(mathCompiler::Num, "value")
    descriptor = None
    for klass in mathCompiler::Num.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_mathcompiler::let_is_not_abstract():
    assert not inspect.isabstract(mathCompiler::Let)


def test_mathcompiler::let_constructor_exists():
    assert callable(mathCompiler::Let.__init__)


def test_mathcompiler::let_constructor_args():
    sig = inspect.signature(mathCompiler::Let.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_mathcompiler::let_has_id():
    assert hasattr(mathCompiler::Let, "id")
    descriptor = None
    for klass in mathCompiler::Let.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_mathcompiler::minus_is_not_abstract():
    assert not inspect.isabstract(mathCompiler::Minus)


def test_mathcompiler::minus_constructor_exists():
    assert callable(mathCompiler::Minus.__init__)


def test_mathcompiler::minus_constructor_args():
    sig = inspect.signature(mathCompiler::Minus.__init__)
    params = list(sig.parameters.keys())



def test_mathcompiler::external_is_not_abstract():
    assert not inspect.isabstract(mathCompiler::External)


def test_mathcompiler::external_constructor_exists():
    assert callable(mathCompiler::External.__init__)


def test_mathcompiler::external_constructor_args():
    sig = inspect.signature(mathCompiler::External.__init__)
    params = list(sig.parameters.keys())
    assert "exponent" in params, "Missing parameter 'exponent'"
    assert "base" in params, "Missing parameter 'base'"

def test_mathcompiler::external_has_exponent():
    assert hasattr(mathCompiler::External, "exponent")
    descriptor = None
    for klass in mathCompiler::External.__mro__:
        if "exponent" in klass.__dict__:
            descriptor = klass.__dict__["exponent"]
            break
    assert isinstance(descriptor, property)

def test_mathcompiler::external_has_base():
    assert hasattr(mathCompiler::External, "base")
    descriptor = None
    for klass in mathCompiler::External.__mro__:
        if "base" in klass.__dict__:
            descriptor = klass.__dict__["base"]
            break
    assert isinstance(descriptor, property)



def test_mathcompiler::var_is_not_abstract():
    assert not inspect.isabstract(mathCompiler::Var)


def test_mathcompiler::var_constructor_exists():
    assert callable(mathCompiler::Var.__init__)


def test_mathcompiler::var_constructor_args():
    sig = inspect.signature(mathCompiler::Var.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_mathcompiler::var_has_id():
    assert hasattr(mathCompiler::Var, "id")
    descriptor = None
    for klass in mathCompiler::Var.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_mathcompiler::div_is_not_abstract():
    assert not inspect.isabstract(mathCompiler::Div)


def test_mathcompiler::div_constructor_exists():
    assert callable(mathCompiler::Div.__init__)


def test_mathcompiler::div_constructor_args():
    sig = inspect.signature(mathCompiler::Div.__init__)
    params = list(sig.parameters.keys())



def test_mathcompiler::plus_is_not_abstract():
    assert not inspect.isabstract(mathCompiler::Plus)


def test_mathcompiler::plus_constructor_exists():
    assert callable(mathCompiler::Plus.__init__)


def test_mathcompiler::plus_constructor_args():
    sig = inspect.signature(mathCompiler::Plus.__init__)
    params = list(sig.parameters.keys())



def test_mathcompiler::expression_is_not_abstract():
    assert not inspect.isabstract(mathCompiler::Expression)


def test_mathcompiler::expression_constructor_exists():
    assert callable(mathCompiler::Expression.__init__)


def test_mathcompiler::expression_constructor_args():
    sig = inspect.signature(mathCompiler::Expression.__init__)
    params = list(sig.parameters.keys())



def test_mathcompiler::mathexp_is_not_abstract():
    assert not inspect.isabstract(mathCompiler::MathExp)


def test_mathcompiler::mathexp_constructor_exists():
    assert callable(mathCompiler::MathExp.__init__)


def test_mathcompiler::mathexp_constructor_args():
    sig = inspect.signature(mathCompiler::MathExp.__init__)
    params = list(sig.parameters.keys())
    assert "line" in params, "Missing parameter 'line'"

def test_mathcompiler::mathexp_has_line():
    assert hasattr(mathCompiler::MathExp, "line")
    descriptor = None
    for klass in mathCompiler::MathExp.__mro__:
        if "line" in klass.__dict__:
            descriptor = klass.__dict__["line"]
            break
    assert isinstance(descriptor, property)



def test_mathcompiler::expressions_is_not_abstract():
    assert not inspect.isabstract(mathCompiler::Expressions)


def test_mathcompiler::expressions_constructor_exists():
    assert callable(mathCompiler::Expressions.__init__)


def test_mathcompiler::expressions_constructor_args():
    sig = inspect.signature(mathCompiler::Expressions.__init__)
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
Expression_strategy = st.builds(
    Expression,
)
mathCompiler::Mult_strategy = st.builds(
    mathCompiler::Mult,
)
mathCompiler::Num_strategy = st.builds(
    mathCompiler::Num,
    value=
        st.integers()
)
mathCompiler::Let_strategy = st.builds(
    mathCompiler::Let,
    id=
        safe_text
)
mathCompiler::Minus_strategy = st.builds(
    mathCompiler::Minus,
)
mathCompiler::External_strategy = st.builds(
    mathCompiler::External,
    exponent=
        st.integers(),
    base=
        st.integers()
)
mathCompiler::Var_strategy = st.builds(
    mathCompiler::Var,
    id=
        safe_text
)
mathCompiler::Div_strategy = st.builds(
    mathCompiler::Div,
)
mathCompiler::Plus_strategy = st.builds(
    mathCompiler::Plus,
)
mathCompiler::Expression_strategy = st.builds(
    mathCompiler::Expression,
)
mathCompiler::MathExp_strategy = st.builds(
    mathCompiler::MathExp,
    line=
        safe_text
)
mathCompiler::Expressions_strategy = st.builds(
    mathCompiler::Expressions,
)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=mathCompiler::Mult_strategy)
@settings(max_examples=50)
def test_mathcompiler::mult_instantiation(instance):
    assert isinstance(instance, mathCompiler::Mult)

@given(instance=mathCompiler::Num_strategy)
@settings(max_examples=50)
def test_mathcompiler::num_instantiation(instance):
    assert isinstance(instance, mathCompiler::Num)

@given(instance=mathCompiler::Num_strategy)
def test_mathcompiler::num_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=mathCompiler::Num_strategy)
def test_mathcompiler::num_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=mathCompiler::Let_strategy)
@settings(max_examples=50)
def test_mathcompiler::let_instantiation(instance):
    assert isinstance(instance, mathCompiler::Let)

@given(instance=mathCompiler::Let_strategy)
def test_mathcompiler::let_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=mathCompiler::Let_strategy)
def test_mathcompiler::let_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=mathCompiler::Minus_strategy)
@settings(max_examples=50)
def test_mathcompiler::minus_instantiation(instance):
    assert isinstance(instance, mathCompiler::Minus)

@given(instance=mathCompiler::External_strategy)
@settings(max_examples=50)
def test_mathcompiler::external_instantiation(instance):
    assert isinstance(instance, mathCompiler::External)

@given(instance=mathCompiler::External_strategy)
def test_mathcompiler::external_exponent_type(instance):
    assert isinstance(instance.exponent, int)


@given(instance=mathCompiler::External_strategy)
def test_mathcompiler::external_exponent_setter(instance):
    original = instance.exponent
    instance.exponent = original
    assert instance.exponent == original

@given(instance=mathCompiler::External_strategy)
def test_mathcompiler::external_base_type(instance):
    assert isinstance(instance.base, int)


@given(instance=mathCompiler::External_strategy)
def test_mathcompiler::external_base_setter(instance):
    original = instance.base
    instance.base = original
    assert instance.base == original

@given(instance=mathCompiler::Var_strategy)
@settings(max_examples=50)
def test_mathcompiler::var_instantiation(instance):
    assert isinstance(instance, mathCompiler::Var)

@given(instance=mathCompiler::Var_strategy)
def test_mathcompiler::var_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=mathCompiler::Var_strategy)
def test_mathcompiler::var_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=mathCompiler::Div_strategy)
@settings(max_examples=50)
def test_mathcompiler::div_instantiation(instance):
    assert isinstance(instance, mathCompiler::Div)

@given(instance=mathCompiler::Plus_strategy)
@settings(max_examples=50)
def test_mathcompiler::plus_instantiation(instance):
    assert isinstance(instance, mathCompiler::Plus)

@given(instance=mathCompiler::Expression_strategy)
@settings(max_examples=50)
def test_mathcompiler::expression_instantiation(instance):
    assert isinstance(instance, mathCompiler::Expression)

@given(instance=mathCompiler::MathExp_strategy)
@settings(max_examples=50)
def test_mathcompiler::mathexp_instantiation(instance):
    assert isinstance(instance, mathCompiler::MathExp)

@given(instance=mathCompiler::MathExp_strategy)
def test_mathcompiler::mathexp_line_type(instance):
    assert isinstance(instance.line, str)


@given(instance=mathCompiler::MathExp_strategy)
def test_mathcompiler::mathexp_line_setter(instance):
    original = instance.line
    instance.line = original
    assert instance.line == original

@given(instance=mathCompiler::Expressions_strategy)
@settings(max_examples=50)
def test_mathcompiler::expressions_instantiation(instance):
    assert isinstance(instance, mathCompiler::Expressions)
