import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    test::A,
    test::B,
    test::Compo,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_test::a_is_not_abstract():
    assert not inspect.isabstract(test::A)


def test_test::a_constructor_exists():
    assert callable(test::A.__init__)


def test_test::a_constructor_args():
    sig = inspect.signature(test::A.__init__)
    params = list(sig.parameters.keys())
    assert "listen" in params, "Missing parameter 'listen'"

def test_test::a_has_listen():
    assert hasattr(test::A, "listen")
    descriptor = None
    for klass in test::A.__mro__:
        if "listen" in klass.__dict__:
            descriptor = klass.__dict__["listen"]
            break
    assert isinstance(descriptor, property)



def test_test::b_is_not_abstract():
    assert not inspect.isabstract(test::B)


def test_test::b_constructor_exists():
    assert callable(test::B.__init__)


def test_test::b_constructor_args():
    sig = inspect.signature(test::B.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_test::b_has_name():
    assert hasattr(test::B, "name")
    descriptor = None
    for klass in test::B.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_test::compo_is_not_abstract():
    assert not inspect.isabstract(test::Compo)


def test_test::compo_constructor_exists():
    assert callable(test::Compo.__init__)


def test_test::compo_constructor_args():
    sig = inspect.signature(test::Compo.__init__)
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
test::A_strategy = st.builds(
    test::A,
    listen=
        st.integers()
)
test::B_strategy = st.builds(
    test::B,
    name=
        safe_text
)
test::Compo_strategy = st.builds(
    test::Compo,
)

@given(instance=test::A_strategy)
@settings(max_examples=50)
def test_test::a_instantiation(instance):
    assert isinstance(instance, test::A)

@given(instance=test::A_strategy)
def test_test::a_listen_type(instance):
    assert isinstance(instance.listen, int)


@given(instance=test::A_strategy)
def test_test::a_listen_setter(instance):
    original = instance.listen
    instance.listen = original
    assert instance.listen == original

@given(instance=test::B_strategy)
@settings(max_examples=50)
def test_test::b_instantiation(instance):
    assert isinstance(instance, test::B)

@given(instance=test::B_strategy)
def test_test::b_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=test::B_strategy)
def test_test::b_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=test::Compo_strategy)
@settings(max_examples=50)
def test_test::compo_instantiation(instance):
    assert isinstance(instance, test::Compo)
