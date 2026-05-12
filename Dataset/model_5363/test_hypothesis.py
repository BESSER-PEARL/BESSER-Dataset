import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    c_AbstractClass,
    Foo,
    c_Bar,
    AbstractClass,
    c_Foo,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_c_abstractclass_is_not_abstract():
    assert not inspect.isabstract(c_AbstractClass)


def test_c_abstractclass_constructor_exists():
    assert callable(c_AbstractClass.__init__)


def test_c_abstractclass_constructor_args():
    sig = inspect.signature(c_AbstractClass.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_c_abstractclass_has_name():
    assert hasattr(c_AbstractClass, "name")
    descriptor = None
    for klass in c_AbstractClass.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_foo_is_not_abstract():
    assert not inspect.isabstract(Foo)


def test_foo_constructor_exists():
    assert callable(Foo.__init__)


def test_foo_constructor_args():
    sig = inspect.signature(Foo.__init__)
    params = list(sig.parameters.keys())



def test_c_bar_is_not_abstract():
    assert not inspect.isabstract(c_Bar)


def test_c_bar_constructor_exists():
    assert callable(c_Bar.__init__)


def test_c_bar_constructor_args():
    sig = inspect.signature(c_Bar.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_c_bar_has_value():
    assert hasattr(c_Bar, "value")
    descriptor = None
    for klass in c_Bar.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_abstractclass_is_not_abstract():
    assert not inspect.isabstract(AbstractClass)


def test_abstractclass_constructor_exists():
    assert callable(AbstractClass.__init__)


def test_abstractclass_constructor_args():
    sig = inspect.signature(AbstractClass.__init__)
    params = list(sig.parameters.keys())



def test_c_foo_is_not_abstract():
    assert not inspect.isabstract(c_Foo)


def test_c_foo_constructor_exists():
    assert callable(c_Foo.__init__)


def test_c_foo_constructor_args():
    sig = inspect.signature(c_Foo.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_c_foo_has_description():
    assert hasattr(c_Foo, "description")
    descriptor = None
    for klass in c_Foo.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)


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
c_AbstractClass_strategy = st.builds(
    c_AbstractClass,
    name=
        safe_text
)
Foo_strategy = st.builds(
    Foo,
)
c_Bar_strategy = st.builds(
    c_Bar,
    value=
        safe_text
)
AbstractClass_strategy = st.builds(
    AbstractClass,
)
c_Foo_strategy = st.builds(
    c_Foo,
    description=
        safe_text
)

@given(instance=c_AbstractClass_strategy)
@settings(max_examples=50)
def test_c_abstractclass_instantiation(instance):
    assert isinstance(instance, c_AbstractClass)



@given(instance=c_AbstractClass_strategy)
def test_c_abstractclass_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Foo_strategy)
@settings(max_examples=50)
def test_foo_instantiation(instance):
    assert isinstance(instance, Foo)

@given(instance=c_Bar_strategy)
@settings(max_examples=50)
def test_c_bar_instantiation(instance):
    assert isinstance(instance, c_Bar)



@given(instance=c_Bar_strategy)
def test_c_bar_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=AbstractClass_strategy)
@settings(max_examples=50)
def test_abstractclass_instantiation(instance):
    assert isinstance(instance, AbstractClass)

@given(instance=c_Foo_strategy)
@settings(max_examples=50)
def test_c_foo_instantiation(instance):
    assert isinstance(instance, c_Foo)



@given(instance=c_Foo_strategy)
def test_c_foo_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original
