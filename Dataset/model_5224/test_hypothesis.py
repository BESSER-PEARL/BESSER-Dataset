import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    C,
    linkinher::T,
    linkinher::X,
    linkinher::K,
    E,
    linkinher::M,
    S,
    linkinher::C,
    T,
    linkinher::L,
    linkinher::Named,
    Named,
    linkinher::N,
    linkinher::S,
    linkinher::E,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_c_is_not_abstract():
    assert not inspect.isabstract(C)


def test_c_constructor_exists():
    assert callable(C.__init__)


def test_c_constructor_args():
    sig = inspect.signature(C.__init__)
    params = list(sig.parameters.keys())



def test_linkinher::t_is_not_abstract():
    assert not inspect.isabstract(linkinher::T)


def test_linkinher::t_constructor_exists():
    assert callable(linkinher::T.__init__)


def test_linkinher::t_constructor_args():
    sig = inspect.signature(linkinher::T.__init__)
    params = list(sig.parameters.keys())



def test_linkinher::x_is_not_abstract():
    assert not inspect.isabstract(linkinher::X)


def test_linkinher::x_constructor_exists():
    assert callable(linkinher::X.__init__)


def test_linkinher::x_constructor_args():
    sig = inspect.signature(linkinher::X.__init__)
    params = list(sig.parameters.keys())



def test_linkinher::k_is_not_abstract():
    assert not inspect.isabstract(linkinher::K)


def test_linkinher::k_constructor_exists():
    assert callable(linkinher::K.__init__)


def test_linkinher::k_constructor_args():
    sig = inspect.signature(linkinher::K.__init__)
    params = list(sig.parameters.keys())



def test_e_is_not_abstract():
    assert not inspect.isabstract(E)


def test_e_constructor_exists():
    assert callable(E.__init__)


def test_e_constructor_args():
    sig = inspect.signature(E.__init__)
    params = list(sig.parameters.keys())



def test_linkinher::m_is_not_abstract():
    assert not inspect.isabstract(linkinher::M)


def test_linkinher::m_constructor_exists():
    assert callable(linkinher::M.__init__)


def test_linkinher::m_constructor_args():
    sig = inspect.signature(linkinher::M.__init__)
    params = list(sig.parameters.keys())



def test_s_is_not_abstract():
    assert not inspect.isabstract(S)


def test_s_constructor_exists():
    assert callable(S.__init__)


def test_s_constructor_args():
    sig = inspect.signature(S.__init__)
    params = list(sig.parameters.keys())



def test_linkinher::c_is_not_abstract():
    assert not inspect.isabstract(linkinher::C)


def test_linkinher::c_constructor_exists():
    assert callable(linkinher::C.__init__)


def test_linkinher::c_constructor_args():
    sig = inspect.signature(linkinher::C.__init__)
    params = list(sig.parameters.keys())



def test_t_is_not_abstract():
    assert not inspect.isabstract(T)


def test_t_constructor_exists():
    assert callable(T.__init__)


def test_t_constructor_args():
    sig = inspect.signature(T.__init__)
    params = list(sig.parameters.keys())



def test_linkinher::l_is_not_abstract():
    assert not inspect.isabstract(linkinher::L)


def test_linkinher::l_constructor_exists():
    assert callable(linkinher::L.__init__)


def test_linkinher::l_constructor_args():
    sig = inspect.signature(linkinher::L.__init__)
    params = list(sig.parameters.keys())



def test_linkinher::named_is_not_abstract():
    assert not inspect.isabstract(linkinher::Named)


def test_linkinher::named_constructor_exists():
    assert callable(linkinher::Named.__init__)


def test_linkinher::named_constructor_args():
    sig = inspect.signature(linkinher::Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_linkinher::named_has_name():
    assert hasattr(linkinher::Named, "name")
    descriptor = None
    for klass in linkinher::Named.__mro__:
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



def test_linkinher::n_is_not_abstract():
    assert not inspect.isabstract(linkinher::N)


def test_linkinher::n_constructor_exists():
    assert callable(linkinher::N.__init__)


def test_linkinher::n_constructor_args():
    sig = inspect.signature(linkinher::N.__init__)
    params = list(sig.parameters.keys())



def test_linkinher::s_is_not_abstract():
    assert not inspect.isabstract(linkinher::S)


def test_linkinher::s_constructor_exists():
    assert callable(linkinher::S.__init__)


def test_linkinher::s_constructor_args():
    sig = inspect.signature(linkinher::S.__init__)
    params = list(sig.parameters.keys())



def test_linkinher::e_is_not_abstract():
    assert not inspect.isabstract(linkinher::E)


def test_linkinher::e_constructor_exists():
    assert callable(linkinher::E.__init__)


def test_linkinher::e_constructor_args():
    sig = inspect.signature(linkinher::E.__init__)
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
C_strategy = st.builds(
    C,
)
linkinher::T_strategy = st.builds(
    linkinher::T,
)
linkinher::X_strategy = st.builds(
    linkinher::X,
)
linkinher::K_strategy = st.builds(
    linkinher::K,
)
E_strategy = st.builds(
    E,
)
linkinher::M_strategy = st.builds(
    linkinher::M,
)
S_strategy = st.builds(
    S,
)
linkinher::C_strategy = st.builds(
    linkinher::C,
)
T_strategy = st.builds(
    T,
)
linkinher::L_strategy = st.builds(
    linkinher::L,
)
linkinher::Named_strategy = st.builds(
    linkinher::Named,
    name=
        safe_text
)
Named_strategy = st.builds(
    Named,
)
linkinher::N_strategy = st.builds(
    linkinher::N,
)
linkinher::S_strategy = st.builds(
    linkinher::S,
)
linkinher::E_strategy = st.builds(
    linkinher::E,
)

@given(instance=C_strategy)
@settings(max_examples=50)
def test_c_instantiation(instance):
    assert isinstance(instance, C)

@given(instance=linkinher::T_strategy)
@settings(max_examples=50)
def test_linkinher::t_instantiation(instance):
    assert isinstance(instance, linkinher::T)

@given(instance=linkinher::X_strategy)
@settings(max_examples=50)
def test_linkinher::x_instantiation(instance):
    assert isinstance(instance, linkinher::X)

@given(instance=linkinher::K_strategy)
@settings(max_examples=50)
def test_linkinher::k_instantiation(instance):
    assert isinstance(instance, linkinher::K)

@given(instance=E_strategy)
@settings(max_examples=50)
def test_e_instantiation(instance):
    assert isinstance(instance, E)

@given(instance=linkinher::M_strategy)
@settings(max_examples=50)
def test_linkinher::m_instantiation(instance):
    assert isinstance(instance, linkinher::M)

@given(instance=S_strategy)
@settings(max_examples=50)
def test_s_instantiation(instance):
    assert isinstance(instance, S)

@given(instance=linkinher::C_strategy)
@settings(max_examples=50)
def test_linkinher::c_instantiation(instance):
    assert isinstance(instance, linkinher::C)

@given(instance=T_strategy)
@settings(max_examples=50)
def test_t_instantiation(instance):
    assert isinstance(instance, T)

@given(instance=linkinher::L_strategy)
@settings(max_examples=50)
def test_linkinher::l_instantiation(instance):
    assert isinstance(instance, linkinher::L)

@given(instance=linkinher::Named_strategy)
@settings(max_examples=50)
def test_linkinher::named_instantiation(instance):
    assert isinstance(instance, linkinher::Named)

@given(instance=linkinher::Named_strategy)
def test_linkinher::named_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=linkinher::Named_strategy)
def test_linkinher::named_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Named_strategy)
@settings(max_examples=50)
def test_named_instantiation(instance):
    assert isinstance(instance, Named)

@given(instance=linkinher::N_strategy)
@settings(max_examples=50)
def test_linkinher::n_instantiation(instance):
    assert isinstance(instance, linkinher::N)

@given(instance=linkinher::S_strategy)
@settings(max_examples=50)
def test_linkinher::s_instantiation(instance):
    assert isinstance(instance, linkinher::S)

@given(instance=linkinher::E_strategy)
@settings(max_examples=50)
def test_linkinher::e_instantiation(instance):
    assert isinstance(instance, linkinher::E)
