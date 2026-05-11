import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    multiview4::Named,
    Named,
    multiview4::E,
    multiview4::B,
    multiview4::C,
    multiview4::A,
    multiview4::F,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_multiview4::named_is_not_abstract():
    assert not inspect.isabstract(multiview4::Named)


def test_multiview4::named_constructor_exists():
    assert callable(multiview4::Named.__init__)


def test_multiview4::named_constructor_args():
    sig = inspect.signature(multiview4::Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_multiview4::named_has_name():
    assert hasattr(multiview4::Named, "name")
    descriptor = None
    for klass in multiview4::Named.__mro__:
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



def test_multiview4::e_is_not_abstract():
    assert not inspect.isabstract(multiview4::E)


def test_multiview4::e_constructor_exists():
    assert callable(multiview4::E.__init__)


def test_multiview4::e_constructor_args():
    sig = inspect.signature(multiview4::E.__init__)
    params = list(sig.parameters.keys())



def test_multiview4::b_is_not_abstract():
    assert not inspect.isabstract(multiview4::B)


def test_multiview4::b_constructor_exists():
    assert callable(multiview4::B.__init__)


def test_multiview4::b_constructor_args():
    sig = inspect.signature(multiview4::B.__init__)
    params = list(sig.parameters.keys())



def test_multiview4::c_is_not_abstract():
    assert not inspect.isabstract(multiview4::C)


def test_multiview4::c_constructor_exists():
    assert callable(multiview4::C.__init__)


def test_multiview4::c_constructor_args():
    sig = inspect.signature(multiview4::C.__init__)
    params = list(sig.parameters.keys())



def test_multiview4::a_is_not_abstract():
    assert not inspect.isabstract(multiview4::A)


def test_multiview4::a_constructor_exists():
    assert callable(multiview4::A.__init__)


def test_multiview4::a_constructor_args():
    sig = inspect.signature(multiview4::A.__init__)
    params = list(sig.parameters.keys())



def test_multiview4::f_is_not_abstract():
    assert not inspect.isabstract(multiview4::F)


def test_multiview4::f_constructor_exists():
    assert callable(multiview4::F.__init__)


def test_multiview4::f_constructor_args():
    sig = inspect.signature(multiview4::F.__init__)
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
multiview4::Named_strategy = st.builds(
    multiview4::Named,
    name=
        safe_text
)
Named_strategy = st.builds(
    Named,
)
multiview4::E_strategy = st.builds(
    multiview4::E,
)
multiview4::B_strategy = st.builds(
    multiview4::B,
)
multiview4::C_strategy = st.builds(
    multiview4::C,
)
multiview4::A_strategy = st.builds(
    multiview4::A,
)
multiview4::F_strategy = st.builds(
    multiview4::F,
)

@given(instance=multiview4::Named_strategy)
@settings(max_examples=50)
def test_multiview4::named_instantiation(instance):
    assert isinstance(instance, multiview4::Named)

@given(instance=multiview4::Named_strategy)
def test_multiview4::named_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=multiview4::Named_strategy)
def test_multiview4::named_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Named_strategy)
@settings(max_examples=50)
def test_named_instantiation(instance):
    assert isinstance(instance, Named)

@given(instance=multiview4::E_strategy)
@settings(max_examples=50)
def test_multiview4::e_instantiation(instance):
    assert isinstance(instance, multiview4::E)

@given(instance=multiview4::B_strategy)
@settings(max_examples=50)
def test_multiview4::b_instantiation(instance):
    assert isinstance(instance, multiview4::B)

@given(instance=multiview4::C_strategy)
@settings(max_examples=50)
def test_multiview4::c_instantiation(instance):
    assert isinstance(instance, multiview4::C)

@given(instance=multiview4::A_strategy)
@settings(max_examples=50)
def test_multiview4::a_instantiation(instance):
    assert isinstance(instance, multiview4::A)

@given(instance=multiview4::F_strategy)
@settings(max_examples=50)
def test_multiview4::f_instantiation(instance):
    assert isinstance(instance, multiview4::F)
