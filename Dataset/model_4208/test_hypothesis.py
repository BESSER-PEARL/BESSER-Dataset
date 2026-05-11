import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Greeting,
    myDsl::Operation,
    myDsl::Lambda,
    myDsl::Square,
    myDsl::Conditional,
    myDsl::Define,
    myDsl::Greeting,
    myDsl::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_greeting_is_not_abstract():
    assert not inspect.isabstract(Greeting)


def test_greeting_constructor_exists():
    assert callable(Greeting.__init__)


def test_greeting_constructor_args():
    sig = inspect.signature(Greeting.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::operation_is_not_abstract():
    assert not inspect.isabstract(myDsl::Operation)


def test_mydsl::operation_constructor_exists():
    assert callable(myDsl::Operation.__init__)


def test_mydsl::operation_constructor_args():
    sig = inspect.signature(myDsl::Operation.__init__)
    params = list(sig.parameters.keys())
    assert "value2" in params, "Missing parameter 'value2'"
    assert "op" in params, "Missing parameter 'op'"

def test_mydsl::operation_has_value2():
    assert hasattr(myDsl::Operation, "value2")
    descriptor = None
    for klass in myDsl::Operation.__mro__:
        if "value2" in klass.__dict__:
            descriptor = klass.__dict__["value2"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::operation_has_op():
    assert hasattr(myDsl::Operation, "op")
    descriptor = None
    for klass in myDsl::Operation.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::lambda_is_not_abstract():
    assert not inspect.isabstract(myDsl::Lambda)


def test_mydsl::lambda_constructor_exists():
    assert callable(myDsl::Lambda.__init__)


def test_mydsl::lambda_constructor_args():
    sig = inspect.signature(myDsl::Lambda.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::square_is_not_abstract():
    assert not inspect.isabstract(myDsl::Square)


def test_mydsl::square_constructor_exists():
    assert callable(myDsl::Square.__init__)


def test_mydsl::square_constructor_args():
    sig = inspect.signature(myDsl::Square.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::conditional_is_not_abstract():
    assert not inspect.isabstract(myDsl::Conditional)


def test_mydsl::conditional_constructor_exists():
    assert callable(myDsl::Conditional.__init__)


def test_mydsl::conditional_constructor_args():
    sig = inspect.signature(myDsl::Conditional.__init__)
    params = list(sig.parameters.keys())
    assert "value2" in params, "Missing parameter 'value2'"
    assert "value3" in params, "Missing parameter 'value3'"

def test_mydsl::conditional_has_value2():
    assert hasattr(myDsl::Conditional, "value2")
    descriptor = None
    for klass in myDsl::Conditional.__mro__:
        if "value2" in klass.__dict__:
            descriptor = klass.__dict__["value2"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::conditional_has_value3():
    assert hasattr(myDsl::Conditional, "value3")
    descriptor = None
    for klass in myDsl::Conditional.__mro__:
        if "value3" in klass.__dict__:
            descriptor = klass.__dict__["value3"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::define_is_not_abstract():
    assert not inspect.isabstract(myDsl::Define)


def test_mydsl::define_constructor_exists():
    assert callable(myDsl::Define.__init__)


def test_mydsl::define_constructor_args():
    sig = inspect.signature(myDsl::Define.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::greeting_is_not_abstract():
    assert not inspect.isabstract(myDsl::Greeting)


def test_mydsl::greeting_constructor_exists():
    assert callable(myDsl::Greeting.__init__)


def test_mydsl::greeting_constructor_args():
    sig = inspect.signature(myDsl::Greeting.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::greeting_has_value():
    assert hasattr(myDsl::Greeting, "value")
    descriptor = None
    for klass in myDsl::Greeting.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::greeting_has_name():
    assert hasattr(myDsl::Greeting, "name")
    descriptor = None
    for klass in myDsl::Greeting.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::model_is_not_abstract():
    assert not inspect.isabstract(myDsl::Model)


def test_mydsl::model_constructor_exists():
    assert callable(myDsl::Model.__init__)


def test_mydsl::model_constructor_args():
    sig = inspect.signature(myDsl::Model.__init__)
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
Greeting_strategy = st.builds(
    Greeting,
)
myDsl::Operation_strategy = st.builds(
    myDsl::Operation,
    value2=
        st.integers(),
    op=
        safe_text
)
myDsl::Lambda_strategy = st.builds(
    myDsl::Lambda,
)
myDsl::Square_strategy = st.builds(
    myDsl::Square,
)
myDsl::Conditional_strategy = st.builds(
    myDsl::Conditional,
    value2=
        st.integers(),
    value3=
        st.integers()
)
myDsl::Define_strategy = st.builds(
    myDsl::Define,
)
myDsl::Greeting_strategy = st.builds(
    myDsl::Greeting,
    value=
        st.integers(),
    name=
        safe_text
)
myDsl::Model_strategy = st.builds(
    myDsl::Model,
)

@given(instance=Greeting_strategy)
@settings(max_examples=50)
def test_greeting_instantiation(instance):
    assert isinstance(instance, Greeting)

@given(instance=myDsl::Operation_strategy)
@settings(max_examples=50)
def test_mydsl::operation_instantiation(instance):
    assert isinstance(instance, myDsl::Operation)

@given(instance=myDsl::Operation_strategy)
def test_mydsl::operation_value2_type(instance):
    assert isinstance(instance.value2, int)


@given(instance=myDsl::Operation_strategy)
def test_mydsl::operation_value2_setter(instance):
    original = instance.value2
    instance.value2 = original
    assert instance.value2 == original

@given(instance=myDsl::Operation_strategy)
def test_mydsl::operation_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=myDsl::Operation_strategy)
def test_mydsl::operation_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=myDsl::Lambda_strategy)
@settings(max_examples=50)
def test_mydsl::lambda_instantiation(instance):
    assert isinstance(instance, myDsl::Lambda)

@given(instance=myDsl::Square_strategy)
@settings(max_examples=50)
def test_mydsl::square_instantiation(instance):
    assert isinstance(instance, myDsl::Square)

@given(instance=myDsl::Conditional_strategy)
@settings(max_examples=50)
def test_mydsl::conditional_instantiation(instance):
    assert isinstance(instance, myDsl::Conditional)

@given(instance=myDsl::Conditional_strategy)
def test_mydsl::conditional_value2_type(instance):
    assert isinstance(instance.value2, int)


@given(instance=myDsl::Conditional_strategy)
def test_mydsl::conditional_value2_setter(instance):
    original = instance.value2
    instance.value2 = original
    assert instance.value2 == original

@given(instance=myDsl::Conditional_strategy)
def test_mydsl::conditional_value3_type(instance):
    assert isinstance(instance.value3, int)


@given(instance=myDsl::Conditional_strategy)
def test_mydsl::conditional_value3_setter(instance):
    original = instance.value3
    instance.value3 = original
    assert instance.value3 == original

@given(instance=myDsl::Define_strategy)
@settings(max_examples=50)
def test_mydsl::define_instantiation(instance):
    assert isinstance(instance, myDsl::Define)

@given(instance=myDsl::Greeting_strategy)
@settings(max_examples=50)
def test_mydsl::greeting_instantiation(instance):
    assert isinstance(instance, myDsl::Greeting)

@given(instance=myDsl::Greeting_strategy)
def test_mydsl::greeting_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=myDsl::Greeting_strategy)
def test_mydsl::greeting_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=myDsl::Greeting_strategy)
def test_mydsl::greeting_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::Greeting_strategy)
def test_mydsl::greeting_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::Model_strategy)
@settings(max_examples=50)
def test_mydsl::model_instantiation(instance):
    assert isinstance(instance, myDsl::Model)
