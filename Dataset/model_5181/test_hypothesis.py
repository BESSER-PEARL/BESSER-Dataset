import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    manypov2::Named,
    Named,
    manypov2::B,
    manypov2::C,
    manypov2::M,
    manypov2::E,
    manypov2::F,
    manypov2::N,
    manypov2::K,
    manypov2::J,
    manypov2::JK,
    manypov2::A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_manypov2::named_is_not_abstract():
    assert not inspect.isabstract(manypov2::Named)


def test_manypov2::named_constructor_exists():
    assert callable(manypov2::Named.__init__)


def test_manypov2::named_constructor_args():
    sig = inspect.signature(manypov2::Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_manypov2::named_has_name():
    assert hasattr(manypov2::Named, "name")
    descriptor = None
    for klass in manypov2::Named.__mro__:
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



def test_manypov2::b_is_not_abstract():
    assert not inspect.isabstract(manypov2::B)


def test_manypov2::b_constructor_exists():
    assert callable(manypov2::B.__init__)


def test_manypov2::b_constructor_args():
    sig = inspect.signature(manypov2::B.__init__)
    params = list(sig.parameters.keys())



def test_manypov2::c_is_not_abstract():
    assert not inspect.isabstract(manypov2::C)


def test_manypov2::c_constructor_exists():
    assert callable(manypov2::C.__init__)


def test_manypov2::c_constructor_args():
    sig = inspect.signature(manypov2::C.__init__)
    params = list(sig.parameters.keys())



def test_manypov2::m_is_not_abstract():
    assert not inspect.isabstract(manypov2::M)


def test_manypov2::m_constructor_exists():
    assert callable(manypov2::M.__init__)


def test_manypov2::m_constructor_args():
    sig = inspect.signature(manypov2::M.__init__)
    params = list(sig.parameters.keys())



def test_manypov2::e_is_not_abstract():
    assert not inspect.isabstract(manypov2::E)


def test_manypov2::e_constructor_exists():
    assert callable(manypov2::E.__init__)


def test_manypov2::e_constructor_args():
    sig = inspect.signature(manypov2::E.__init__)
    params = list(sig.parameters.keys())



def test_manypov2::f_is_not_abstract():
    assert not inspect.isabstract(manypov2::F)


def test_manypov2::f_constructor_exists():
    assert callable(manypov2::F.__init__)


def test_manypov2::f_constructor_args():
    sig = inspect.signature(manypov2::F.__init__)
    params = list(sig.parameters.keys())



def test_manypov2::n_is_not_abstract():
    assert not inspect.isabstract(manypov2::N)


def test_manypov2::n_constructor_exists():
    assert callable(manypov2::N.__init__)


def test_manypov2::n_constructor_args():
    sig = inspect.signature(manypov2::N.__init__)
    params = list(sig.parameters.keys())



def test_manypov2::k_is_not_abstract():
    assert not inspect.isabstract(manypov2::K)


def test_manypov2::k_constructor_exists():
    assert callable(manypov2::K.__init__)


def test_manypov2::k_constructor_args():
    sig = inspect.signature(manypov2::K.__init__)
    params = list(sig.parameters.keys())



def test_manypov2::j_is_not_abstract():
    assert not inspect.isabstract(manypov2::J)


def test_manypov2::j_constructor_exists():
    assert callable(manypov2::J.__init__)


def test_manypov2::j_constructor_args():
    sig = inspect.signature(manypov2::J.__init__)
    params = list(sig.parameters.keys())



def test_manypov2::jk_is_not_abstract():
    assert not inspect.isabstract(manypov2::JK)


def test_manypov2::jk_constructor_exists():
    assert callable(manypov2::JK.__init__)


def test_manypov2::jk_constructor_args():
    sig = inspect.signature(manypov2::JK.__init__)
    params = list(sig.parameters.keys())



def test_manypov2::a_is_not_abstract():
    assert not inspect.isabstract(manypov2::A)


def test_manypov2::a_constructor_exists():
    assert callable(manypov2::A.__init__)


def test_manypov2::a_constructor_args():
    sig = inspect.signature(manypov2::A.__init__)
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
manypov2::Named_strategy = st.builds(
    manypov2::Named,
    name=
        safe_text
)
Named_strategy = st.builds(
    Named,
)
manypov2::B_strategy = st.builds(
    manypov2::B,
)
manypov2::C_strategy = st.builds(
    manypov2::C,
)
manypov2::M_strategy = st.builds(
    manypov2::M,
)
manypov2::E_strategy = st.builds(
    manypov2::E,
)
manypov2::F_strategy = st.builds(
    manypov2::F,
)
manypov2::N_strategy = st.builds(
    manypov2::N,
)
manypov2::K_strategy = st.builds(
    manypov2::K,
)
manypov2::J_strategy = st.builds(
    manypov2::J,
)
manypov2::JK_strategy = st.builds(
    manypov2::JK,
)
manypov2::A_strategy = st.builds(
    manypov2::A,
)

@given(instance=manypov2::Named_strategy)
@settings(max_examples=50)
def test_manypov2::named_instantiation(instance):
    assert isinstance(instance, manypov2::Named)

@given(instance=manypov2::Named_strategy)
def test_manypov2::named_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=manypov2::Named_strategy)
def test_manypov2::named_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Named_strategy)
@settings(max_examples=50)
def test_named_instantiation(instance):
    assert isinstance(instance, Named)

@given(instance=manypov2::B_strategy)
@settings(max_examples=50)
def test_manypov2::b_instantiation(instance):
    assert isinstance(instance, manypov2::B)

@given(instance=manypov2::C_strategy)
@settings(max_examples=50)
def test_manypov2::c_instantiation(instance):
    assert isinstance(instance, manypov2::C)

@given(instance=manypov2::M_strategy)
@settings(max_examples=50)
def test_manypov2::m_instantiation(instance):
    assert isinstance(instance, manypov2::M)

@given(instance=manypov2::E_strategy)
@settings(max_examples=50)
def test_manypov2::e_instantiation(instance):
    assert isinstance(instance, manypov2::E)

@given(instance=manypov2::F_strategy)
@settings(max_examples=50)
def test_manypov2::f_instantiation(instance):
    assert isinstance(instance, manypov2::F)

@given(instance=manypov2::N_strategy)
@settings(max_examples=50)
def test_manypov2::n_instantiation(instance):
    assert isinstance(instance, manypov2::N)

@given(instance=manypov2::K_strategy)
@settings(max_examples=50)
def test_manypov2::k_instantiation(instance):
    assert isinstance(instance, manypov2::K)

@given(instance=manypov2::J_strategy)
@settings(max_examples=50)
def test_manypov2::j_instantiation(instance):
    assert isinstance(instance, manypov2::J)

@given(instance=manypov2::JK_strategy)
@settings(max_examples=50)
def test_manypov2::jk_instantiation(instance):
    assert isinstance(instance, manypov2::JK)

@given(instance=manypov2::A_strategy)
@settings(max_examples=50)
def test_manypov2::a_instantiation(instance):
    assert isinstance(instance, manypov2::A)
