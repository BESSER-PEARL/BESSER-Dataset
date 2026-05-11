import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    multiview2::Named,
    Named,
    multiview2::B,
    multiview2::E,
    multiview2::F,
    multiview2::A,
    multiview2::C,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_multiview2::named_is_not_abstract():
    assert not inspect.isabstract(multiview2::Named)


def test_multiview2::named_constructor_exists():
    assert callable(multiview2::Named.__init__)


def test_multiview2::named_constructor_args():
    sig = inspect.signature(multiview2::Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_multiview2::named_has_name():
    assert hasattr(multiview2::Named, "name")
    descriptor = None
    for klass in multiview2::Named.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_named_is_not_abstract():
    assert not inspect.isabstract(Named)


def test_named_constructor_exists():
    assert callable(Named.__init__)


def test_named_constructor_args():
    sig = inspect.signature(Named.__init__)
    params = list(sig.parameters.keys())



def test_multiview2::b_is_not_abstract():
    assert not inspect.isabstract(multiview2::B)


def test_multiview2::b_constructor_exists():
    assert callable(multiview2::B.__init__)


def test_multiview2::b_constructor_args():
    sig = inspect.signature(multiview2::B.__init__)
    params = list(sig.parameters.keys())



def test_multiview2::e_is_not_abstract():
    assert not inspect.isabstract(multiview2::E)


def test_multiview2::e_constructor_exists():
    assert callable(multiview2::E.__init__)


def test_multiview2::e_constructor_args():
    sig = inspect.signature(multiview2::E.__init__)
    params = list(sig.parameters.keys())



def test_multiview2::f_is_not_abstract():
    assert not inspect.isabstract(multiview2::F)


def test_multiview2::f_constructor_exists():
    assert callable(multiview2::F.__init__)


def test_multiview2::f_constructor_args():
    sig = inspect.signature(multiview2::F.__init__)
    params = list(sig.parameters.keys())



def test_multiview2::a_is_not_abstract():
    assert not inspect.isabstract(multiview2::A)


def test_multiview2::a_constructor_exists():
    assert callable(multiview2::A.__init__)


def test_multiview2::a_constructor_args():
    sig = inspect.signature(multiview2::A.__init__)
    params = list(sig.parameters.keys())



def test_multiview2::c_is_not_abstract():
    assert not inspect.isabstract(multiview2::C)


def test_multiview2::c_constructor_exists():
    assert callable(multiview2::C.__init__)


def test_multiview2::c_constructor_args():
    sig = inspect.signature(multiview2::C.__init__)
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
multiview2::Named_strategy = st.builds(
    multiview2::Named,
    name=
        safe_text
)
Named_strategy = st.builds(
    Named,
)
multiview2::B_strategy = st.builds(
    multiview2::B,
)
multiview2::E_strategy = st.builds(
    multiview2::E,
)
multiview2::F_strategy = st.builds(
    multiview2::F,
)
multiview2::A_strategy = st.builds(
    multiview2::A,
)
multiview2::C_strategy = st.builds(
    multiview2::C,
)

@given(instance=multiview2::Named_strategy)
@settings(max_examples=50)
def test_multiview2::named_instantiation(instance):
    assert isinstance(instance, multiview2::Named)

@given(instance=multiview2::Named_strategy)
def test_multiview2::named_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=multiview2::Named_strategy)
def test_multiview2::named_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Named_strategy)
@settings(max_examples=50)
def test_named_instantiation(instance):
    assert isinstance(instance, Named)

@given(instance=multiview2::B_strategy)
@settings(max_examples=50)
def test_multiview2::b_instantiation(instance):
    assert isinstance(instance, multiview2::B)

@given(instance=multiview2::E_strategy)
@settings(max_examples=50)
def test_multiview2::e_instantiation(instance):
    assert isinstance(instance, multiview2::E)

@given(instance=multiview2::F_strategy)
@settings(max_examples=50)
def test_multiview2::f_instantiation(instance):
    assert isinstance(instance, multiview2::F)

@given(instance=multiview2::A_strategy)
@settings(max_examples=50)
def test_multiview2::a_instantiation(instance):
    assert isinstance(instance, multiview2::A)

@given(instance=multiview2::C_strategy)
@settings(max_examples=50)
def test_multiview2::c_instantiation(instance):
    assert isinstance(instance, multiview2::C)
