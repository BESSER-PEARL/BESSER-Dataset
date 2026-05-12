import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Expression,
    mathCompiler_Let,
    mathCompiler_Div,
    mathCompiler_Minus,
    mathCompiler_Num,
    mathCompiler_External,
    mathCompiler_Var,
    mathCompiler_Mult,
    mathCompiler_Plus,
    mathCompiler_Expression,
    mathCompiler_MathExp,
    mathCompiler_Expressions,
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



def test_mathcompiler_let_is_not_abstract():
    assert not inspect.isabstract(mathCompiler_Let)


def test_mathcompiler_let_constructor_exists():
    assert callable(mathCompiler_Let.__init__)


def test_mathcompiler_let_constructor_args():
    sig = inspect.signature(mathCompiler_Let.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_mathcompiler_let_has_id():
    assert hasattr(mathCompiler_Let, "id")
    descriptor = None
    for klass in mathCompiler_Let.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_mathcompiler_div_is_not_abstract():
    assert not inspect.isabstract(mathCompiler_Div)


def test_mathcompiler_div_constructor_exists():
    assert callable(mathCompiler_Div.__init__)


def test_mathcompiler_div_constructor_args():
    sig = inspect.signature(mathCompiler_Div.__init__)
    params = list(sig.parameters.keys())



def test_mathcompiler_minus_is_not_abstract():
    assert not inspect.isabstract(mathCompiler_Minus)


def test_mathcompiler_minus_constructor_exists():
    assert callable(mathCompiler_Minus.__init__)


def test_mathcompiler_minus_constructor_args():
    sig = inspect.signature(mathCompiler_Minus.__init__)
    params = list(sig.parameters.keys())



def test_mathcompiler_num_is_not_abstract():
    assert not inspect.isabstract(mathCompiler_Num)


def test_mathcompiler_num_constructor_exists():
    assert callable(mathCompiler_Num.__init__)


def test_mathcompiler_num_constructor_args():
    sig = inspect.signature(mathCompiler_Num.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_mathcompiler_num_has_value():
    assert hasattr(mathCompiler_Num, "value")
    descriptor = None
    for klass in mathCompiler_Num.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_mathcompiler_external_is_not_abstract():
    assert not inspect.isabstract(mathCompiler_External)


def test_mathcompiler_external_constructor_exists():
    assert callable(mathCompiler_External.__init__)


def test_mathcompiler_external_constructor_args():
    sig = inspect.signature(mathCompiler_External.__init__)
    params = list(sig.parameters.keys())
    assert "exponent" in params, "Missing parameter 'exponent'"
    assert "base" in params, "Missing parameter 'base'"

def test_mathcompiler_external_has_exponent():
    assert hasattr(mathCompiler_External, "exponent")
    descriptor = None
    for klass in mathCompiler_External.__mro__:
        if "exponent" in klass.__dict__:
            descriptor = klass.__dict__["exponent"]
            break
    assert isinstance(descriptor, property)

def test_mathcompiler_external_has_base():
    assert hasattr(mathCompiler_External, "base")
    descriptor = None
    for klass in mathCompiler_External.__mro__:
        if "base" in klass.__dict__:
            descriptor = klass.__dict__["base"]
            break
    assert isinstance(descriptor, property)



def test_mathcompiler_var_is_not_abstract():
    assert not inspect.isabstract(mathCompiler_Var)


def test_mathcompiler_var_constructor_exists():
    assert callable(mathCompiler_Var.__init__)


def test_mathcompiler_var_constructor_args():
    sig = inspect.signature(mathCompiler_Var.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_mathcompiler_var_has_id():
    assert hasattr(mathCompiler_Var, "id")
    descriptor = None
    for klass in mathCompiler_Var.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_mathcompiler_mult_is_not_abstract():
    assert not inspect.isabstract(mathCompiler_Mult)


def test_mathcompiler_mult_constructor_exists():
    assert callable(mathCompiler_Mult.__init__)


def test_mathcompiler_mult_constructor_args():
    sig = inspect.signature(mathCompiler_Mult.__init__)
    params = list(sig.parameters.keys())



def test_mathcompiler_plus_is_not_abstract():
    assert not inspect.isabstract(mathCompiler_Plus)


def test_mathcompiler_plus_constructor_exists():
    assert callable(mathCompiler_Plus.__init__)


def test_mathcompiler_plus_constructor_args():
    sig = inspect.signature(mathCompiler_Plus.__init__)
    params = list(sig.parameters.keys())



def test_mathcompiler_expression_is_not_abstract():
    assert not inspect.isabstract(mathCompiler_Expression)


def test_mathcompiler_expression_constructor_exists():
    assert callable(mathCompiler_Expression.__init__)


def test_mathcompiler_expression_constructor_args():
    sig = inspect.signature(mathCompiler_Expression.__init__)
    params = list(sig.parameters.keys())



def test_mathcompiler_mathexp_is_not_abstract():
    assert not inspect.isabstract(mathCompiler_MathExp)


def test_mathcompiler_mathexp_constructor_exists():
    assert callable(mathCompiler_MathExp.__init__)


def test_mathcompiler_mathexp_constructor_args():
    sig = inspect.signature(mathCompiler_MathExp.__init__)
    params = list(sig.parameters.keys())
    assert "line" in params, "Missing parameter 'line'"

def test_mathcompiler_mathexp_has_line():
    assert hasattr(mathCompiler_MathExp, "line")
    descriptor = None
    for klass in mathCompiler_MathExp.__mro__:
        if "line" in klass.__dict__:
            descriptor = klass.__dict__["line"]
            break
    assert isinstance(descriptor, property)



def test_mathcompiler_expressions_is_not_abstract():
    assert not inspect.isabstract(mathCompiler_Expressions)


def test_mathcompiler_expressions_constructor_exists():
    assert callable(mathCompiler_Expressions.__init__)


def test_mathcompiler_expressions_constructor_args():
    sig = inspect.signature(mathCompiler_Expressions.__init__)
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
mathCompiler_Let_strategy = st.builds(
    mathCompiler_Let,
    id=
        safe_text
)
mathCompiler_Div_strategy = st.builds(
    mathCompiler_Div,
)
mathCompiler_Minus_strategy = st.builds(
    mathCompiler_Minus,
)
mathCompiler_Num_strategy = st.builds(
    mathCompiler_Num,
    value=
        st.integers()
)
mathCompiler_External_strategy = st.builds(
    mathCompiler_External,
    exponent=
        st.integers(),
    base=
        st.integers()
)
mathCompiler_Var_strategy = st.builds(
    mathCompiler_Var,
    id=
        safe_text
)
mathCompiler_Mult_strategy = st.builds(
    mathCompiler_Mult,
)
mathCompiler_Plus_strategy = st.builds(
    mathCompiler_Plus,
)
mathCompiler_Expression_strategy = st.builds(
    mathCompiler_Expression,
)
mathCompiler_MathExp_strategy = st.builds(
    mathCompiler_MathExp,
    line=
        safe_text
)
mathCompiler_Expressions_strategy = st.builds(
    mathCompiler_Expressions,
)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=mathCompiler_Let_strategy)
@settings(max_examples=50)
def test_mathcompiler_let_instantiation(instance):
    assert isinstance(instance, mathCompiler_Let)



@given(instance=mathCompiler_Let_strategy)
def test_mathcompiler_let_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=mathCompiler_Div_strategy)
@settings(max_examples=50)
def test_mathcompiler_div_instantiation(instance):
    assert isinstance(instance, mathCompiler_Div)

@given(instance=mathCompiler_Minus_strategy)
@settings(max_examples=50)
def test_mathcompiler_minus_instantiation(instance):
    assert isinstance(instance, mathCompiler_Minus)

@given(instance=mathCompiler_Num_strategy)
@settings(max_examples=50)
def test_mathcompiler_num_instantiation(instance):
    assert isinstance(instance, mathCompiler_Num)



@given(instance=mathCompiler_Num_strategy)
def test_mathcompiler_num_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=mathCompiler_External_strategy)
@settings(max_examples=50)
def test_mathcompiler_external_instantiation(instance):
    assert isinstance(instance, mathCompiler_External)



@given(instance=mathCompiler_External_strategy)
def test_mathcompiler_external_exponent_setter(instance):
    original = instance.exponent
    instance.exponent = original
    assert instance.exponent == original



@given(instance=mathCompiler_External_strategy)
def test_mathcompiler_external_base_setter(instance):
    original = instance.base
    instance.base = original
    assert instance.base == original

@given(instance=mathCompiler_Var_strategy)
@settings(max_examples=50)
def test_mathcompiler_var_instantiation(instance):
    assert isinstance(instance, mathCompiler_Var)



@given(instance=mathCompiler_Var_strategy)
def test_mathcompiler_var_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=mathCompiler_Mult_strategy)
@settings(max_examples=50)
def test_mathcompiler_mult_instantiation(instance):
    assert isinstance(instance, mathCompiler_Mult)

@given(instance=mathCompiler_Plus_strategy)
@settings(max_examples=50)
def test_mathcompiler_plus_instantiation(instance):
    assert isinstance(instance, mathCompiler_Plus)

@given(instance=mathCompiler_Expression_strategy)
@settings(max_examples=50)
def test_mathcompiler_expression_instantiation(instance):
    assert isinstance(instance, mathCompiler_Expression)

@given(instance=mathCompiler_MathExp_strategy)
@settings(max_examples=50)
def test_mathcompiler_mathexp_instantiation(instance):
    assert isinstance(instance, mathCompiler_MathExp)



@given(instance=mathCompiler_MathExp_strategy)
def test_mathcompiler_mathexp_line_setter(instance):
    original = instance.line
    instance.line = original
    assert instance.line == original

@given(instance=mathCompiler_Expressions_strategy)
@settings(max_examples=50)
def test_mathcompiler_expressions_instantiation(instance):
    assert isinstance(instance, mathCompiler_Expressions)
