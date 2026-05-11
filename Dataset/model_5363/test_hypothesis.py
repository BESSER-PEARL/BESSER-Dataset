import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    c::AbstractClass,
    Foo,
    c::Bar,
    AbstractClass,
    c::Foo,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_c::abstractclass_is_not_abstract():
    assert not inspect.isabstract(c::AbstractClass)


def test_c::abstractclass_constructor_exists():
    assert callable(c::AbstractClass.__init__)


def test_c::abstractclass_constructor_args():
    sig = inspect.signature(c::AbstractClass.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_c::abstractclass_has_name():
    assert hasattr(c::AbstractClass, "name")
    descriptor = None
    for klass in c::AbstractClass.__mro__:
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



def test_c::bar_is_not_abstract():
    assert not inspect.isabstract(c::Bar)


def test_c::bar_constructor_exists():
    assert callable(c::Bar.__init__)


def test_c::bar_constructor_args():
    sig = inspect.signature(c::Bar.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_c::bar_has_value():
    assert hasattr(c::Bar, "value")
    descriptor = None
    for klass in c::Bar.__mro__:
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



def test_c::foo_is_not_abstract():
    assert not inspect.isabstract(c::Foo)


def test_c::foo_constructor_exists():
    assert callable(c::Foo.__init__)


def test_c::foo_constructor_args():
    sig = inspect.signature(c::Foo.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_c::foo_has_description():
    assert hasattr(c::Foo, "description")
    descriptor = None
    for klass in c::Foo.__mro__:
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
c::AbstractClass_strategy = st.builds(
    c::AbstractClass,
    name=
        safe_text
)
Foo_strategy = st.builds(
    Foo,
)
c::Bar_strategy = st.builds(
    c::Bar,
    value=
        safe_text
)
AbstractClass_strategy = st.builds(
    AbstractClass,
)
c::Foo_strategy = st.builds(
    c::Foo,
    description=
        safe_text
)

@given(instance=c::AbstractClass_strategy)
@settings(max_examples=50)
def test_c::abstractclass_instantiation(instance):
    assert isinstance(instance, c::AbstractClass)

@given(instance=c::AbstractClass_strategy)
def test_c::abstractclass_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=c::AbstractClass_strategy)
def test_c::abstractclass_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Foo_strategy)
@settings(max_examples=50)
def test_foo_instantiation(instance):
    assert isinstance(instance, Foo)

@given(instance=c::Bar_strategy)
@settings(max_examples=50)
def test_c::bar_instantiation(instance):
    assert isinstance(instance, c::Bar)

@given(instance=c::Bar_strategy)
def test_c::bar_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=c::Bar_strategy)
def test_c::bar_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=AbstractClass_strategy)
@settings(max_examples=50)
def test_abstractclass_instantiation(instance):
    assert isinstance(instance, AbstractClass)

@given(instance=c::Foo_strategy)
@settings(max_examples=50)
def test_c::foo_instantiation(instance):
    assert isinstance(instance, c::Foo)

@given(instance=c::Foo_strategy)
def test_c::foo_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=c::Foo_strategy)
def test_c::foo_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original
