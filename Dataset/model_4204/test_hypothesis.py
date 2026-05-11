import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    helloScoping::FieldReference,
    helloScoping::Field,
    helloScoping::Greeting,
    helloScoping::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_helloscoping::fieldreference_is_not_abstract():
    assert not inspect.isabstract(helloScoping::FieldReference)


def test_helloscoping::fieldreference_constructor_exists():
    assert callable(helloScoping::FieldReference.__init__)


def test_helloscoping::fieldreference_constructor_args():
    sig = inspect.signature(helloScoping::FieldReference.__init__)
    params = list(sig.parameters.keys())



def test_helloscoping::field_is_not_abstract():
    assert not inspect.isabstract(helloScoping::Field)


def test_helloscoping::field_constructor_exists():
    assert callable(helloScoping::Field.__init__)


def test_helloscoping::field_constructor_args():
    sig = inspect.signature(helloScoping::Field.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_helloscoping::field_has_name():
    assert hasattr(helloScoping::Field, "name")
    descriptor = None
    for klass in helloScoping::Field.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_helloscoping::greeting_is_not_abstract():
    assert not inspect.isabstract(helloScoping::Greeting)


def test_helloscoping::greeting_constructor_exists():
    assert callable(helloScoping::Greeting.__init__)


def test_helloscoping::greeting_constructor_args():
    sig = inspect.signature(helloScoping::Greeting.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_helloscoping::greeting_has_name():
    assert hasattr(helloScoping::Greeting, "name")
    descriptor = None
    for klass in helloScoping::Greeting.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_helloscoping::model_is_not_abstract():
    assert not inspect.isabstract(helloScoping::Model)


def test_helloscoping::model_constructor_exists():
    assert callable(helloScoping::Model.__init__)


def test_helloscoping::model_constructor_args():
    sig = inspect.signature(helloScoping::Model.__init__)
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
helloScoping::FieldReference_strategy = st.builds(
    helloScoping::FieldReference,
)
helloScoping::Field_strategy = st.builds(
    helloScoping::Field,
    name=
        safe_text
)
helloScoping::Greeting_strategy = st.builds(
    helloScoping::Greeting,
    name=
        safe_text
)
helloScoping::Model_strategy = st.builds(
    helloScoping::Model,
)

@given(instance=helloScoping::FieldReference_strategy)
@settings(max_examples=50)
def test_helloscoping::fieldreference_instantiation(instance):
    assert isinstance(instance, helloScoping::FieldReference)

@given(instance=helloScoping::Field_strategy)
@settings(max_examples=50)
def test_helloscoping::field_instantiation(instance):
    assert isinstance(instance, helloScoping::Field)

@given(instance=helloScoping::Field_strategy)
def test_helloscoping::field_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=helloScoping::Field_strategy)
def test_helloscoping::field_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=helloScoping::Greeting_strategy)
@settings(max_examples=50)
def test_helloscoping::greeting_instantiation(instance):
    assert isinstance(instance, helloScoping::Greeting)

@given(instance=helloScoping::Greeting_strategy)
def test_helloscoping::greeting_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=helloScoping::Greeting_strategy)
def test_helloscoping::greeting_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=helloScoping::Model_strategy)
@settings(max_examples=50)
def test_helloscoping::model_instantiation(instance):
    assert isinstance(instance, helloScoping::Model)
