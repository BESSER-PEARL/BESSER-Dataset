import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    test_Bar,
    test_Foo,
    test_Container,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_test_bar_is_not_abstract():
    assert not inspect.isabstract(test_Bar)


def test_test_bar_constructor_exists():
    assert callable(test_Bar.__init__)


def test_test_bar_constructor_args():
    sig = inspect.signature(test_Bar.__init__)
    params = list(sig.parameters.keys())
    assert "barA" in params, "Missing parameter 'barA'"

def test_test_bar_has_barA():
    assert hasattr(test_Bar, "barA")
    descriptor = None
    for klass in test_Bar.__mro__:
        if "barA" in klass.__dict__:
            descriptor = klass.__dict__["barA"]
            break
    assert isinstance(descriptor, property)



def test_test_foo_is_not_abstract():
    assert not inspect.isabstract(test_Foo)


def test_test_foo_constructor_exists():
    assert callable(test_Foo.__init__)


def test_test_foo_constructor_args():
    sig = inspect.signature(test_Foo.__init__)
    params = list(sig.parameters.keys())
    assert "fooA" in params, "Missing parameter 'fooA'"

def test_test_foo_has_fooA():
    assert hasattr(test_Foo, "fooA")
    descriptor = None
    for klass in test_Foo.__mro__:
        if "fooA" in klass.__dict__:
            descriptor = klass.__dict__["fooA"]
            break
    assert isinstance(descriptor, property)



def test_test_container_is_not_abstract():
    assert not inspect.isabstract(test_Container)


def test_test_container_constructor_exists():
    assert callable(test_Container.__init__)


def test_test_container_constructor_args():
    sig = inspect.signature(test_Container.__init__)
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
test_Bar_strategy = st.builds(
    test_Bar,
    barA=
        safe_text
)
test_Foo_strategy = st.builds(
    test_Foo,
    fooA=
        safe_text
)
test_Container_strategy = st.builds(
    test_Container,
)

@given(instance=test_Bar_strategy)
@settings(max_examples=50)
def test_test_bar_instantiation(instance):
    assert isinstance(instance, test_Bar)



@given(instance=test_Bar_strategy)
def test_test_bar_barA_setter(instance):
    original = instance.barA
    instance.barA = original
    assert instance.barA == original

@given(instance=test_Foo_strategy)
@settings(max_examples=50)
def test_test_foo_instantiation(instance):
    assert isinstance(instance, test_Foo)



@given(instance=test_Foo_strategy)
def test_test_foo_fooA_setter(instance):
    original = instance.fooA
    instance.fooA = original
    assert instance.fooA == original

@given(instance=test_Container_strategy)
@settings(max_examples=50)
def test_test_container_instantiation(instance):
    assert isinstance(instance, test_Container)
