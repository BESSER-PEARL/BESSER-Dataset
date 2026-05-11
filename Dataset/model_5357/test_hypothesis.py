import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    test::Bar,
    test::Foo,
    test::Container,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_test::bar_is_not_abstract():
    assert not inspect.isabstract(test::Bar)


def test_test::bar_constructor_exists():
    assert callable(test::Bar.__init__)


def test_test::bar_constructor_args():
    sig = inspect.signature(test::Bar.__init__)
    params = list(sig.parameters.keys())
    assert "barA" in params, "Missing parameter 'barA'"

def test_test::bar_has_barA():
    assert hasattr(test::Bar, "barA")
    descriptor = None
    for klass in test::Bar.__mro__:
        if "barA" in klass.__dict__:
            descriptor = klass.__dict__["barA"]
            break
    assert isinstance(descriptor, property)



def test_test::foo_is_not_abstract():
    assert not inspect.isabstract(test::Foo)


def test_test::foo_constructor_exists():
    assert callable(test::Foo.__init__)


def test_test::foo_constructor_args():
    sig = inspect.signature(test::Foo.__init__)
    params = list(sig.parameters.keys())
    assert "fooA" in params, "Missing parameter 'fooA'"

def test_test::foo_has_fooA():
    assert hasattr(test::Foo, "fooA")
    descriptor = None
    for klass in test::Foo.__mro__:
        if "fooA" in klass.__dict__:
            descriptor = klass.__dict__["fooA"]
            break
    assert isinstance(descriptor, property)



def test_test::container_is_not_abstract():
    assert not inspect.isabstract(test::Container)


def test_test::container_constructor_exists():
    assert callable(test::Container.__init__)


def test_test::container_constructor_args():
    sig = inspect.signature(test::Container.__init__)
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
test::Bar_strategy = st.builds(
    test::Bar,
    barA=
        safe_text
)
test::Foo_strategy = st.builds(
    test::Foo,
    fooA=
        safe_text
)
test::Container_strategy = st.builds(
    test::Container,
)

@given(instance=test::Bar_strategy)
@settings(max_examples=50)
def test_test::bar_instantiation(instance):
    assert isinstance(instance, test::Bar)

@given(instance=test::Bar_strategy)
def test_test::bar_barA_type(instance):
    assert isinstance(instance.barA, str)


@given(instance=test::Bar_strategy)
def test_test::bar_barA_setter(instance):
    original = instance.barA
    instance.barA = original
    assert instance.barA == original

@given(instance=test::Foo_strategy)
@settings(max_examples=50)
def test_test::foo_instantiation(instance):
    assert isinstance(instance, test::Foo)

@given(instance=test::Foo_strategy)
def test_test::foo_fooA_type(instance):
    assert isinstance(instance.fooA, str)


@given(instance=test::Foo_strategy)
def test_test::foo_fooA_setter(instance):
    original = instance.fooA
    instance.fooA = original
    assert instance.fooA == original

@given(instance=test::Container_strategy)
@settings(max_examples=50)
def test_test::container_instantiation(instance):
    assert isinstance(instance, test::Container)
