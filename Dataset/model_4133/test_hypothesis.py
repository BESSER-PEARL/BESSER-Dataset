import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Instance,
    myDsl::Method,
    myDsl::Instance,
    myDsl::Classs,
    Expression,
    myDsl::Minus,
    myDsl::Mult,
    myDsl::Plus,
    myDsl::Expression,
    myDsl::MathExp,
    myDsl::Parameter,
    myDsl::Num,
    myDsl::Let,
    myDsl::Var,
    myDsl::Div,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_instance_is_not_abstract():
    assert not inspect.isabstract(Instance)


def test_instance_constructor_exists():
    assert callable(Instance.__init__)


def test_instance_constructor_args():
    sig = inspect.signature(Instance.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::method_is_not_abstract():
    assert not inspect.isabstract(myDsl::Method)


def test_mydsl::method_constructor_exists():
    assert callable(myDsl::Method.__init__)


def test_mydsl::method_constructor_args():
    sig = inspect.signature(myDsl::Method.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::method_has_name():
    assert hasattr(myDsl::Method, "name")
    descriptor = None
    for klass in myDsl::Method.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::instance_is_not_abstract():
    assert not inspect.isabstract(myDsl::Instance)


def test_mydsl::instance_constructor_exists():
    assert callable(myDsl::Instance.__init__)


def test_mydsl::instance_constructor_args():
    sig = inspect.signature(myDsl::Instance.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::classs_is_not_abstract():
    assert not inspect.isabstract(myDsl::Classs)


def test_mydsl::classs_constructor_exists():
    assert callable(myDsl::Classs.__init__)


def test_mydsl::classs_constructor_args():
    sig = inspect.signature(myDsl::Classs.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::minus_is_not_abstract():
    assert not inspect.isabstract(myDsl::Minus)


def test_mydsl::minus_constructor_exists():
    assert callable(myDsl::Minus.__init__)


def test_mydsl::minus_constructor_args():
    sig = inspect.signature(myDsl::Minus.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::mult_is_not_abstract():
    assert not inspect.isabstract(myDsl::Mult)


def test_mydsl::mult_constructor_exists():
    assert callable(myDsl::Mult.__init__)


def test_mydsl::mult_constructor_args():
    sig = inspect.signature(myDsl::Mult.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::plus_is_not_abstract():
    assert not inspect.isabstract(myDsl::Plus)


def test_mydsl::plus_constructor_exists():
    assert callable(myDsl::Plus.__init__)


def test_mydsl::plus_constructor_args():
    sig = inspect.signature(myDsl::Plus.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::expression_is_not_abstract():
    assert not inspect.isabstract(myDsl::Expression)


def test_mydsl::expression_constructor_exists():
    assert callable(myDsl::Expression.__init__)


def test_mydsl::expression_constructor_args():
    sig = inspect.signature(myDsl::Expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::mathexp_is_not_abstract():
    assert not inspect.isabstract(myDsl::MathExp)


def test_mydsl::mathexp_constructor_exists():
    assert callable(myDsl::MathExp.__init__)


def test_mydsl::mathexp_constructor_args():
    sig = inspect.signature(myDsl::MathExp.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_mydsl::mathexp_has_text():
    assert hasattr(myDsl::MathExp, "text")
    descriptor = None
    for klass in myDsl::MathExp.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::parameter_is_not_abstract():
    assert not inspect.isabstract(myDsl::Parameter)


def test_mydsl::parameter_constructor_exists():
    assert callable(myDsl::Parameter.__init__)


def test_mydsl::parameter_constructor_args():
    sig = inspect.signature(myDsl::Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::parameter_has_name():
    assert hasattr(myDsl::Parameter, "name")
    descriptor = None
    for klass in myDsl::Parameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::num_is_not_abstract():
    assert not inspect.isabstract(myDsl::Num)


def test_mydsl::num_constructor_exists():
    assert callable(myDsl::Num.__init__)


def test_mydsl::num_constructor_args():
    sig = inspect.signature(myDsl::Num.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_mydsl::num_has_value():
    assert hasattr(myDsl::Num, "value")
    descriptor = None
    for klass in myDsl::Num.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::let_is_not_abstract():
    assert not inspect.isabstract(myDsl::Let)


def test_mydsl::let_constructor_exists():
    assert callable(myDsl::Let.__init__)


def test_mydsl::let_constructor_args():
    sig = inspect.signature(myDsl::Let.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_mydsl::let_has_id():
    assert hasattr(myDsl::Let, "id")
    descriptor = None
    for klass in myDsl::Let.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::var_is_not_abstract():
    assert not inspect.isabstract(myDsl::Var)


def test_mydsl::var_constructor_exists():
    assert callable(myDsl::Var.__init__)


def test_mydsl::var_constructor_args():
    sig = inspect.signature(myDsl::Var.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_mydsl::var_has_id():
    assert hasattr(myDsl::Var, "id")
    descriptor = None
    for klass in myDsl::Var.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::div_is_not_abstract():
    assert not inspect.isabstract(myDsl::Div)


def test_mydsl::div_constructor_exists():
    assert callable(myDsl::Div.__init__)


def test_mydsl::div_constructor_args():
    sig = inspect.signature(myDsl::Div.__init__)
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
Instance_strategy = st.builds(
    Instance,
)
myDsl::Method_strategy = st.builds(
    myDsl::Method,
    name=
        safe_text
)
myDsl::Instance_strategy = st.builds(
    myDsl::Instance,
)
myDsl::Classs_strategy = st.builds(
    myDsl::Classs,
)
Expression_strategy = st.builds(
    Expression,
)
myDsl::Minus_strategy = st.builds(
    myDsl::Minus,
)
myDsl::Mult_strategy = st.builds(
    myDsl::Mult,
)
myDsl::Plus_strategy = st.builds(
    myDsl::Plus,
)
myDsl::Expression_strategy = st.builds(
    myDsl::Expression,
)
myDsl::MathExp_strategy = st.builds(
    myDsl::MathExp,
    text=
        safe_text
)
myDsl::Parameter_strategy = st.builds(
    myDsl::Parameter,
    name=
        safe_text
)
myDsl::Num_strategy = st.builds(
    myDsl::Num,
    value=
        st.integers()
)
myDsl::Let_strategy = st.builds(
    myDsl::Let,
    id=
        safe_text
)
myDsl::Var_strategy = st.builds(
    myDsl::Var,
    id=
        safe_text
)
myDsl::Div_strategy = st.builds(
    myDsl::Div,
)

@given(instance=Instance_strategy)
@settings(max_examples=50)
def test_instance_instantiation(instance):
    assert isinstance(instance, Instance)

@given(instance=myDsl::Method_strategy)
@settings(max_examples=50)
def test_mydsl::method_instantiation(instance):
    assert isinstance(instance, myDsl::Method)

@given(instance=myDsl::Method_strategy)
def test_mydsl::method_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::Method_strategy)
def test_mydsl::method_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::Instance_strategy)
@settings(max_examples=50)
def test_mydsl::instance_instantiation(instance):
    assert isinstance(instance, myDsl::Instance)

@given(instance=myDsl::Classs_strategy)
@settings(max_examples=50)
def test_mydsl::classs_instantiation(instance):
    assert isinstance(instance, myDsl::Classs)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=myDsl::Minus_strategy)
@settings(max_examples=50)
def test_mydsl::minus_instantiation(instance):
    assert isinstance(instance, myDsl::Minus)

@given(instance=myDsl::Mult_strategy)
@settings(max_examples=50)
def test_mydsl::mult_instantiation(instance):
    assert isinstance(instance, myDsl::Mult)

@given(instance=myDsl::Plus_strategy)
@settings(max_examples=50)
def test_mydsl::plus_instantiation(instance):
    assert isinstance(instance, myDsl::Plus)

@given(instance=myDsl::Expression_strategy)
@settings(max_examples=50)
def test_mydsl::expression_instantiation(instance):
    assert isinstance(instance, myDsl::Expression)

@given(instance=myDsl::MathExp_strategy)
@settings(max_examples=50)
def test_mydsl::mathexp_instantiation(instance):
    assert isinstance(instance, myDsl::MathExp)

@given(instance=myDsl::MathExp_strategy)
def test_mydsl::mathexp_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=myDsl::MathExp_strategy)
def test_mydsl::mathexp_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=myDsl::Parameter_strategy)
@settings(max_examples=50)
def test_mydsl::parameter_instantiation(instance):
    assert isinstance(instance, myDsl::Parameter)

@given(instance=myDsl::Parameter_strategy)
def test_mydsl::parameter_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::Parameter_strategy)
def test_mydsl::parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::Num_strategy)
@settings(max_examples=50)
def test_mydsl::num_instantiation(instance):
    assert isinstance(instance, myDsl::Num)

@given(instance=myDsl::Num_strategy)
def test_mydsl::num_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=myDsl::Num_strategy)
def test_mydsl::num_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=myDsl::Let_strategy)
@settings(max_examples=50)
def test_mydsl::let_instantiation(instance):
    assert isinstance(instance, myDsl::Let)

@given(instance=myDsl::Let_strategy)
def test_mydsl::let_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=myDsl::Let_strategy)
def test_mydsl::let_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=myDsl::Var_strategy)
@settings(max_examples=50)
def test_mydsl::var_instantiation(instance):
    assert isinstance(instance, myDsl::Var)

@given(instance=myDsl::Var_strategy)
def test_mydsl::var_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=myDsl::Var_strategy)
def test_mydsl::var_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=myDsl::Div_strategy)
@settings(max_examples=50)
def test_mydsl::div_instantiation(instance):
    assert isinstance(instance, myDsl::Div)
