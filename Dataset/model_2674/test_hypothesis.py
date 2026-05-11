import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    reference::Named,
    Named,
    reference::F,
    reference::C,
    reference::H,
    reference::E,
    reference::B,
    reference::G,
    reference::A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_reference::named_is_not_abstract():
    assert not inspect.isabstract(reference::Named)


def test_reference::named_constructor_exists():
    assert callable(reference::Named.__init__)


def test_reference::named_constructor_args():
    sig = inspect.signature(reference::Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_reference::named_has_name():
    assert hasattr(reference::Named, "name")
    descriptor = None
    for klass in reference::Named.__mro__:
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



def test_reference::f_is_not_abstract():
    assert not inspect.isabstract(reference::F)


def test_reference::f_constructor_exists():
    assert callable(reference::F.__init__)


def test_reference::f_constructor_args():
    sig = inspect.signature(reference::F.__init__)
    params = list(sig.parameters.keys())



def test_reference::c_is_not_abstract():
    assert not inspect.isabstract(reference::C)


def test_reference::c_constructor_exists():
    assert callable(reference::C.__init__)


def test_reference::c_constructor_args():
    sig = inspect.signature(reference::C.__init__)
    params = list(sig.parameters.keys())



def test_reference::h_is_not_abstract():
    assert not inspect.isabstract(reference::H)


def test_reference::h_constructor_exists():
    assert callable(reference::H.__init__)


def test_reference::h_constructor_args():
    sig = inspect.signature(reference::H.__init__)
    params = list(sig.parameters.keys())



def test_reference::e_is_not_abstract():
    assert not inspect.isabstract(reference::E)


def test_reference::e_constructor_exists():
    assert callable(reference::E.__init__)


def test_reference::e_constructor_args():
    sig = inspect.signature(reference::E.__init__)
    params = list(sig.parameters.keys())



def test_reference::b_is_not_abstract():
    assert not inspect.isabstract(reference::B)


def test_reference::b_constructor_exists():
    assert callable(reference::B.__init__)


def test_reference::b_constructor_args():
    sig = inspect.signature(reference::B.__init__)
    params = list(sig.parameters.keys())



def test_reference::g_is_not_abstract():
    assert not inspect.isabstract(reference::G)


def test_reference::g_constructor_exists():
    assert callable(reference::G.__init__)


def test_reference::g_constructor_args():
    sig = inspect.signature(reference::G.__init__)
    params = list(sig.parameters.keys())



def test_reference::a_is_not_abstract():
    assert not inspect.isabstract(reference::A)


def test_reference::a_constructor_exists():
    assert callable(reference::A.__init__)


def test_reference::a_constructor_args():
    sig = inspect.signature(reference::A.__init__)
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
reference::Named_strategy = st.builds(
    reference::Named,
    name=
        safe_text
)
Named_strategy = st.builds(
    Named,
)
reference::F_strategy = st.builds(
    reference::F,
)
reference::C_strategy = st.builds(
    reference::C,
)
reference::H_strategy = st.builds(
    reference::H,
)
reference::E_strategy = st.builds(
    reference::E,
)
reference::B_strategy = st.builds(
    reference::B,
)
reference::G_strategy = st.builds(
    reference::G,
)
reference::A_strategy = st.builds(
    reference::A,
)

@given(instance=reference::Named_strategy)
@settings(max_examples=50)
def test_reference::named_instantiation(instance):
    assert isinstance(instance, reference::Named)

@given(instance=reference::Named_strategy)
def test_reference::named_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=reference::Named_strategy)
def test_reference::named_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Named_strategy)
@settings(max_examples=50)
def test_named_instantiation(instance):
    assert isinstance(instance, Named)

@given(instance=reference::F_strategy)
@settings(max_examples=50)
def test_reference::f_instantiation(instance):
    assert isinstance(instance, reference::F)

@given(instance=reference::C_strategy)
@settings(max_examples=50)
def test_reference::c_instantiation(instance):
    assert isinstance(instance, reference::C)

@given(instance=reference::H_strategy)
@settings(max_examples=50)
def test_reference::h_instantiation(instance):
    assert isinstance(instance, reference::H)

@given(instance=reference::E_strategy)
@settings(max_examples=50)
def test_reference::e_instantiation(instance):
    assert isinstance(instance, reference::E)

@given(instance=reference::B_strategy)
@settings(max_examples=50)
def test_reference::b_instantiation(instance):
    assert isinstance(instance, reference::B)

@given(instance=reference::G_strategy)
@settings(max_examples=50)
def test_reference::g_instantiation(instance):
    assert isinstance(instance, reference::G)

@given(instance=reference::A_strategy)
@settings(max_examples=50)
def test_reference::a_instantiation(instance):
    assert isinstance(instance, reference::A)
