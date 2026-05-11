import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    manypov::Named,
    Named,
    manypov::K,
    manypov::M,
    manypov::C,
    manypov::E,
    manypov::JK,
    manypov::F,
    manypov::J,
    manypov::B,
    manypov::A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_manypov::named_is_not_abstract():
    assert not inspect.isabstract(manypov::Named)


def test_manypov::named_constructor_exists():
    assert callable(manypov::Named.__init__)


def test_manypov::named_constructor_args():
    sig = inspect.signature(manypov::Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_manypov::named_has_name():
    assert hasattr(manypov::Named, "name")
    descriptor = None
    for klass in manypov::Named.__mro__:
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



def test_manypov::k_is_not_abstract():
    assert not inspect.isabstract(manypov::K)


def test_manypov::k_constructor_exists():
    assert callable(manypov::K.__init__)


def test_manypov::k_constructor_args():
    sig = inspect.signature(manypov::K.__init__)
    params = list(sig.parameters.keys())



def test_manypov::m_is_not_abstract():
    assert not inspect.isabstract(manypov::M)


def test_manypov::m_constructor_exists():
    assert callable(manypov::M.__init__)


def test_manypov::m_constructor_args():
    sig = inspect.signature(manypov::M.__init__)
    params = list(sig.parameters.keys())



def test_manypov::c_is_not_abstract():
    assert not inspect.isabstract(manypov::C)


def test_manypov::c_constructor_exists():
    assert callable(manypov::C.__init__)


def test_manypov::c_constructor_args():
    sig = inspect.signature(manypov::C.__init__)
    params = list(sig.parameters.keys())



def test_manypov::e_is_not_abstract():
    assert not inspect.isabstract(manypov::E)


def test_manypov::e_constructor_exists():
    assert callable(manypov::E.__init__)


def test_manypov::e_constructor_args():
    sig = inspect.signature(manypov::E.__init__)
    params = list(sig.parameters.keys())



def test_manypov::jk_is_not_abstract():
    assert not inspect.isabstract(manypov::JK)


def test_manypov::jk_constructor_exists():
    assert callable(manypov::JK.__init__)


def test_manypov::jk_constructor_args():
    sig = inspect.signature(manypov::JK.__init__)
    params = list(sig.parameters.keys())



def test_manypov::f_is_not_abstract():
    assert not inspect.isabstract(manypov::F)


def test_manypov::f_constructor_exists():
    assert callable(manypov::F.__init__)


def test_manypov::f_constructor_args():
    sig = inspect.signature(manypov::F.__init__)
    params = list(sig.parameters.keys())



def test_manypov::j_is_not_abstract():
    assert not inspect.isabstract(manypov::J)


def test_manypov::j_constructor_exists():
    assert callable(manypov::J.__init__)


def test_manypov::j_constructor_args():
    sig = inspect.signature(manypov::J.__init__)
    params = list(sig.parameters.keys())



def test_manypov::b_is_not_abstract():
    assert not inspect.isabstract(manypov::B)


def test_manypov::b_constructor_exists():
    assert callable(manypov::B.__init__)


def test_manypov::b_constructor_args():
    sig = inspect.signature(manypov::B.__init__)
    params = list(sig.parameters.keys())



def test_manypov::a_is_not_abstract():
    assert not inspect.isabstract(manypov::A)


def test_manypov::a_constructor_exists():
    assert callable(manypov::A.__init__)


def test_manypov::a_constructor_args():
    sig = inspect.signature(manypov::A.__init__)
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
manypov::Named_strategy = st.builds(
    manypov::Named,
    name=
        safe_text
)
Named_strategy = st.builds(
    Named,
)
manypov::K_strategy = st.builds(
    manypov::K,
)
manypov::M_strategy = st.builds(
    manypov::M,
)
manypov::C_strategy = st.builds(
    manypov::C,
)
manypov::E_strategy = st.builds(
    manypov::E,
)
manypov::JK_strategy = st.builds(
    manypov::JK,
)
manypov::F_strategy = st.builds(
    manypov::F,
)
manypov::J_strategy = st.builds(
    manypov::J,
)
manypov::B_strategy = st.builds(
    manypov::B,
)
manypov::A_strategy = st.builds(
    manypov::A,
)

@given(instance=manypov::Named_strategy)
@settings(max_examples=50)
def test_manypov::named_instantiation(instance):
    assert isinstance(instance, manypov::Named)

@given(instance=manypov::Named_strategy)
def test_manypov::named_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=manypov::Named_strategy)
def test_manypov::named_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Named_strategy)
@settings(max_examples=50)
def test_named_instantiation(instance):
    assert isinstance(instance, Named)

@given(instance=manypov::K_strategy)
@settings(max_examples=50)
def test_manypov::k_instantiation(instance):
    assert isinstance(instance, manypov::K)

@given(instance=manypov::M_strategy)
@settings(max_examples=50)
def test_manypov::m_instantiation(instance):
    assert isinstance(instance, manypov::M)

@given(instance=manypov::C_strategy)
@settings(max_examples=50)
def test_manypov::c_instantiation(instance):
    assert isinstance(instance, manypov::C)

@given(instance=manypov::E_strategy)
@settings(max_examples=50)
def test_manypov::e_instantiation(instance):
    assert isinstance(instance, manypov::E)

@given(instance=manypov::JK_strategy)
@settings(max_examples=50)
def test_manypov::jk_instantiation(instance):
    assert isinstance(instance, manypov::JK)

@given(instance=manypov::F_strategy)
@settings(max_examples=50)
def test_manypov::f_instantiation(instance):
    assert isinstance(instance, manypov::F)

@given(instance=manypov::J_strategy)
@settings(max_examples=50)
def test_manypov::j_instantiation(instance):
    assert isinstance(instance, manypov::J)

@given(instance=manypov::B_strategy)
@settings(max_examples=50)
def test_manypov::b_instantiation(instance):
    assert isinstance(instance, manypov::B)

@given(instance=manypov::A_strategy)
@settings(max_examples=50)
def test_manypov::a_instantiation(instance):
    assert isinstance(instance, manypov::A)
