import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    link::Named,
    Named,
    link::M,
    link::W,
    link::B,
    link::C,
    link::K,
    link::X,
    link::D,
    link::N99,
    link::A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_link::named_is_not_abstract():
    assert not inspect.isabstract(link::Named)


def test_link::named_constructor_exists():
    assert callable(link::Named.__init__)


def test_link::named_constructor_args():
    sig = inspect.signature(link::Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_link::named_has_name():
    assert hasattr(link::Named, "name")
    descriptor = None
    for klass in link::Named.__mro__:
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



def test_link::m_is_not_abstract():
    assert not inspect.isabstract(link::M)


def test_link::m_constructor_exists():
    assert callable(link::M.__init__)


def test_link::m_constructor_args():
    sig = inspect.signature(link::M.__init__)
    params = list(sig.parameters.keys())



def test_link::w_is_not_abstract():
    assert not inspect.isabstract(link::W)


def test_link::w_constructor_exists():
    assert callable(link::W.__init__)


def test_link::w_constructor_args():
    sig = inspect.signature(link::W.__init__)
    params = list(sig.parameters.keys())



def test_link::b_is_not_abstract():
    assert not inspect.isabstract(link::B)


def test_link::b_constructor_exists():
    assert callable(link::B.__init__)


def test_link::b_constructor_args():
    sig = inspect.signature(link::B.__init__)
    params = list(sig.parameters.keys())



def test_link::c_is_not_abstract():
    assert not inspect.isabstract(link::C)


def test_link::c_constructor_exists():
    assert callable(link::C.__init__)


def test_link::c_constructor_args():
    sig = inspect.signature(link::C.__init__)
    params = list(sig.parameters.keys())



def test_link::k_is_not_abstract():
    assert not inspect.isabstract(link::K)


def test_link::k_constructor_exists():
    assert callable(link::K.__init__)


def test_link::k_constructor_args():
    sig = inspect.signature(link::K.__init__)
    params = list(sig.parameters.keys())



def test_link::x_is_not_abstract():
    assert not inspect.isabstract(link::X)


def test_link::x_constructor_exists():
    assert callable(link::X.__init__)


def test_link::x_constructor_args():
    sig = inspect.signature(link::X.__init__)
    params = list(sig.parameters.keys())



def test_link::d_is_not_abstract():
    assert not inspect.isabstract(link::D)


def test_link::d_constructor_exists():
    assert callable(link::D.__init__)


def test_link::d_constructor_args():
    sig = inspect.signature(link::D.__init__)
    params = list(sig.parameters.keys())



def test_link::n99_is_not_abstract():
    assert not inspect.isabstract(link::N99)


def test_link::n99_constructor_exists():
    assert callable(link::N99.__init__)


def test_link::n99_constructor_args():
    sig = inspect.signature(link::N99.__init__)
    params = list(sig.parameters.keys())



def test_link::a_is_not_abstract():
    assert not inspect.isabstract(link::A)


def test_link::a_constructor_exists():
    assert callable(link::A.__init__)


def test_link::a_constructor_args():
    sig = inspect.signature(link::A.__init__)
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
link::Named_strategy = st.builds(
    link::Named,
    name=
        safe_text
)
Named_strategy = st.builds(
    Named,
)
link::M_strategy = st.builds(
    link::M,
)
link::W_strategy = st.builds(
    link::W,
)
link::B_strategy = st.builds(
    link::B,
)
link::C_strategy = st.builds(
    link::C,
)
link::K_strategy = st.builds(
    link::K,
)
link::X_strategy = st.builds(
    link::X,
)
link::D_strategy = st.builds(
    link::D,
)
link::N99_strategy = st.builds(
    link::N99,
)
link::A_strategy = st.builds(
    link::A,
)

@given(instance=link::Named_strategy)
@settings(max_examples=50)
def test_link::named_instantiation(instance):
    assert isinstance(instance, link::Named)

@given(instance=link::Named_strategy)
def test_link::named_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=link::Named_strategy)
def test_link::named_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Named_strategy)
@settings(max_examples=50)
def test_named_instantiation(instance):
    assert isinstance(instance, Named)

@given(instance=link::M_strategy)
@settings(max_examples=50)
def test_link::m_instantiation(instance):
    assert isinstance(instance, link::M)

@given(instance=link::W_strategy)
@settings(max_examples=50)
def test_link::w_instantiation(instance):
    assert isinstance(instance, link::W)

@given(instance=link::B_strategy)
@settings(max_examples=50)
def test_link::b_instantiation(instance):
    assert isinstance(instance, link::B)

@given(instance=link::C_strategy)
@settings(max_examples=50)
def test_link::c_instantiation(instance):
    assert isinstance(instance, link::C)

@given(instance=link::K_strategy)
@settings(max_examples=50)
def test_link::k_instantiation(instance):
    assert isinstance(instance, link::K)

@given(instance=link::X_strategy)
@settings(max_examples=50)
def test_link::x_instantiation(instance):
    assert isinstance(instance, link::X)

@given(instance=link::D_strategy)
@settings(max_examples=50)
def test_link::d_instantiation(instance):
    assert isinstance(instance, link::D)

@given(instance=link::N99_strategy)
@settings(max_examples=50)
def test_link::n99_instantiation(instance):
    assert isinstance(instance, link::N99)

@given(instance=link::A_strategy)
@settings(max_examples=50)
def test_link::a_instantiation(instance):
    assert isinstance(instance, link::A)
