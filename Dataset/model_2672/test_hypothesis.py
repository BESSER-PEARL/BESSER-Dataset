import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Named,
    containment::B,
    containment::H,
    containment::E,
    containment::A,
    containment::F,
    containment::Named,
    containment::G,
    containment::C,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_named_is_not_abstract():
    assert not inspect.isabstract(Named)


def test_named_constructor_exists():
    assert callable(Named.__init__)


def test_named_constructor_args():
    sig = inspect.signature(Named.__init__)
    params = list(sig.parameters.keys())



def test_containment::b_is_not_abstract():
    assert not inspect.isabstract(containment::B)


def test_containment::b_constructor_exists():
    assert callable(containment::B.__init__)


def test_containment::b_constructor_args():
    sig = inspect.signature(containment::B.__init__)
    params = list(sig.parameters.keys())



def test_containment::h_is_not_abstract():
    assert not inspect.isabstract(containment::H)


def test_containment::h_constructor_exists():
    assert callable(containment::H.__init__)


def test_containment::h_constructor_args():
    sig = inspect.signature(containment::H.__init__)
    params = list(sig.parameters.keys())



def test_containment::e_is_not_abstract():
    assert not inspect.isabstract(containment::E)


def test_containment::e_constructor_exists():
    assert callable(containment::E.__init__)


def test_containment::e_constructor_args():
    sig = inspect.signature(containment::E.__init__)
    params = list(sig.parameters.keys())



def test_containment::a_is_not_abstract():
    assert not inspect.isabstract(containment::A)


def test_containment::a_constructor_exists():
    assert callable(containment::A.__init__)


def test_containment::a_constructor_args():
    sig = inspect.signature(containment::A.__init__)
    params = list(sig.parameters.keys())



def test_containment::f_is_not_abstract():
    assert not inspect.isabstract(containment::F)


def test_containment::f_constructor_exists():
    assert callable(containment::F.__init__)


def test_containment::f_constructor_args():
    sig = inspect.signature(containment::F.__init__)
    params = list(sig.parameters.keys())



def test_containment::named_is_not_abstract():
    assert not inspect.isabstract(containment::Named)


def test_containment::named_constructor_exists():
    assert callable(containment::Named.__init__)


def test_containment::named_constructor_args():
    sig = inspect.signature(containment::Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_containment::named_has_name():
    assert hasattr(containment::Named, "name")
    descriptor = None
    for klass in containment::Named.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_containment::g_is_not_abstract():
    assert not inspect.isabstract(containment::G)


def test_containment::g_constructor_exists():
    assert callable(containment::G.__init__)


def test_containment::g_constructor_args():
    sig = inspect.signature(containment::G.__init__)
    params = list(sig.parameters.keys())



def test_containment::c_is_not_abstract():
    assert not inspect.isabstract(containment::C)


def test_containment::c_constructor_exists():
    assert callable(containment::C.__init__)


def test_containment::c_constructor_args():
    sig = inspect.signature(containment::C.__init__)
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
Named_strategy = st.builds(
    Named,
)
containment::B_strategy = st.builds(
    containment::B,
)
containment::H_strategy = st.builds(
    containment::H,
)
containment::E_strategy = st.builds(
    containment::E,
)
containment::A_strategy = st.builds(
    containment::A,
)
containment::F_strategy = st.builds(
    containment::F,
)
containment::Named_strategy = st.builds(
    containment::Named,
    name=
        safe_text
)
containment::G_strategy = st.builds(
    containment::G,
)
containment::C_strategy = st.builds(
    containment::C,
)

@given(instance=Named_strategy)
@settings(max_examples=50)
def test_named_instantiation(instance):
    assert isinstance(instance, Named)

@given(instance=containment::B_strategy)
@settings(max_examples=50)
def test_containment::b_instantiation(instance):
    assert isinstance(instance, containment::B)

@given(instance=containment::H_strategy)
@settings(max_examples=50)
def test_containment::h_instantiation(instance):
    assert isinstance(instance, containment::H)

@given(instance=containment::E_strategy)
@settings(max_examples=50)
def test_containment::e_instantiation(instance):
    assert isinstance(instance, containment::E)

@given(instance=containment::A_strategy)
@settings(max_examples=50)
def test_containment::a_instantiation(instance):
    assert isinstance(instance, containment::A)

@given(instance=containment::F_strategy)
@settings(max_examples=50)
def test_containment::f_instantiation(instance):
    assert isinstance(instance, containment::F)

@given(instance=containment::Named_strategy)
@settings(max_examples=50)
def test_containment::named_instantiation(instance):
    assert isinstance(instance, containment::Named)

@given(instance=containment::Named_strategy)
def test_containment::named_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=containment::Named_strategy)
def test_containment::named_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=containment::G_strategy)
@settings(max_examples=50)
def test_containment::g_instantiation(instance):
    assert isinstance(instance, containment::G)

@given(instance=containment::C_strategy)
@settings(max_examples=50)
def test_containment::c_instantiation(instance):
    assert isinstance(instance, containment::C)
