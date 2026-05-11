import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    M,
    A,
    N,
    refinher2::Y,
    refinher2::H,
    CE,
    refinher2::DL,
    refinher2::DNamedElement,
    refinher2::M,
    DNamedElement,
    refinher2::N,
    refinher2::AB,
    refinher2::A,
    refinher2::E,
    refinher2::DG,
    refinher2::DC,
    E,
    refinher2::CE,
    refinher2::DR,
    refinher2::BB,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_m_is_not_abstract():
    assert not inspect.isabstract(M)


def test_m_constructor_exists():
    assert callable(M.__init__)


def test_m_constructor_args():
    sig = inspect.signature(M.__init__)
    params = list(sig.parameters.keys())



def test_a_is_not_abstract():
    assert not inspect.isabstract(A)


def test_a_constructor_exists():
    assert callable(A.__init__)


def test_a_constructor_args():
    sig = inspect.signature(A.__init__)
    params = list(sig.parameters.keys())



def test_n_is_not_abstract():
    assert not inspect.isabstract(N)


def test_n_constructor_exists():
    assert callable(N.__init__)


def test_n_constructor_args():
    sig = inspect.signature(N.__init__)
    params = list(sig.parameters.keys())



def test_refinher2::y_is_not_abstract():
    assert not inspect.isabstract(refinher2::Y)


def test_refinher2::y_constructor_exists():
    assert callable(refinher2::Y.__init__)


def test_refinher2::y_constructor_args():
    sig = inspect.signature(refinher2::Y.__init__)
    params = list(sig.parameters.keys())



def test_refinher2::h_is_not_abstract():
    assert not inspect.isabstract(refinher2::H)


def test_refinher2::h_constructor_exists():
    assert callable(refinher2::H.__init__)


def test_refinher2::h_constructor_args():
    sig = inspect.signature(refinher2::H.__init__)
    params = list(sig.parameters.keys())



def test_ce_is_not_abstract():
    assert not inspect.isabstract(CE)


def test_ce_constructor_exists():
    assert callable(CE.__init__)


def test_ce_constructor_args():
    sig = inspect.signature(CE.__init__)
    params = list(sig.parameters.keys())



def test_refinher2::dl_is_not_abstract():
    assert not inspect.isabstract(refinher2::DL)


def test_refinher2::dl_constructor_exists():
    assert callable(refinher2::DL.__init__)


def test_refinher2::dl_constructor_args():
    sig = inspect.signature(refinher2::DL.__init__)
    params = list(sig.parameters.keys())



def test_refinher2::dnamedelement_is_not_abstract():
    assert not inspect.isabstract(refinher2::DNamedElement)


def test_refinher2::dnamedelement_constructor_exists():
    assert callable(refinher2::DNamedElement.__init__)


def test_refinher2::dnamedelement_constructor_args():
    sig = inspect.signature(refinher2::DNamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_refinher2::dnamedelement_has_name():
    assert hasattr(refinher2::DNamedElement, "name")
    descriptor = None
    for klass in refinher2::DNamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_refinher2::m_is_not_abstract():
    assert not inspect.isabstract(refinher2::M)


def test_refinher2::m_constructor_exists():
    assert callable(refinher2::M.__init__)


def test_refinher2::m_constructor_args():
    sig = inspect.signature(refinher2::M.__init__)
    params = list(sig.parameters.keys())



def test_dnamedelement_is_not_abstract():
    assert not inspect.isabstract(DNamedElement)


def test_dnamedelement_constructor_exists():
    assert callable(DNamedElement.__init__)


def test_dnamedelement_constructor_args():
    sig = inspect.signature(DNamedElement.__init__)
    params = list(sig.parameters.keys())



def test_refinher2::n_is_not_abstract():
    assert not inspect.isabstract(refinher2::N)


def test_refinher2::n_constructor_exists():
    assert callable(refinher2::N.__init__)


def test_refinher2::n_constructor_args():
    sig = inspect.signature(refinher2::N.__init__)
    params = list(sig.parameters.keys())



def test_refinher2::ab_is_not_abstract():
    assert not inspect.isabstract(refinher2::AB)


def test_refinher2::ab_constructor_exists():
    assert callable(refinher2::AB.__init__)


def test_refinher2::ab_constructor_args():
    sig = inspect.signature(refinher2::AB.__init__)
    params = list(sig.parameters.keys())



def test_refinher2::a_is_not_abstract():
    assert not inspect.isabstract(refinher2::A)


def test_refinher2::a_constructor_exists():
    assert callable(refinher2::A.__init__)


def test_refinher2::a_constructor_args():
    sig = inspect.signature(refinher2::A.__init__)
    params = list(sig.parameters.keys())



def test_refinher2::e_is_not_abstract():
    assert not inspect.isabstract(refinher2::E)


def test_refinher2::e_constructor_exists():
    assert callable(refinher2::E.__init__)


def test_refinher2::e_constructor_args():
    sig = inspect.signature(refinher2::E.__init__)
    params = list(sig.parameters.keys())



def test_refinher2::dg_is_not_abstract():
    assert not inspect.isabstract(refinher2::DG)


def test_refinher2::dg_constructor_exists():
    assert callable(refinher2::DG.__init__)


def test_refinher2::dg_constructor_args():
    sig = inspect.signature(refinher2::DG.__init__)
    params = list(sig.parameters.keys())



def test_refinher2::dc_is_not_abstract():
    assert not inspect.isabstract(refinher2::DC)


def test_refinher2::dc_constructor_exists():
    assert callable(refinher2::DC.__init__)


def test_refinher2::dc_constructor_args():
    sig = inspect.signature(refinher2::DC.__init__)
    params = list(sig.parameters.keys())



def test_e_is_not_abstract():
    assert not inspect.isabstract(E)


def test_e_constructor_exists():
    assert callable(E.__init__)


def test_e_constructor_args():
    sig = inspect.signature(E.__init__)
    params = list(sig.parameters.keys())



def test_refinher2::ce_is_not_abstract():
    assert not inspect.isabstract(refinher2::CE)


def test_refinher2::ce_constructor_exists():
    assert callable(refinher2::CE.__init__)


def test_refinher2::ce_constructor_args():
    sig = inspect.signature(refinher2::CE.__init__)
    params = list(sig.parameters.keys())



def test_refinher2::dr_is_not_abstract():
    assert not inspect.isabstract(refinher2::DR)


def test_refinher2::dr_constructor_exists():
    assert callable(refinher2::DR.__init__)


def test_refinher2::dr_constructor_args():
    sig = inspect.signature(refinher2::DR.__init__)
    params = list(sig.parameters.keys())



def test_refinher2::bb_is_not_abstract():
    assert not inspect.isabstract(refinher2::BB)


def test_refinher2::bb_constructor_exists():
    assert callable(refinher2::BB.__init__)


def test_refinher2::bb_constructor_args():
    sig = inspect.signature(refinher2::BB.__init__)
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
M_strategy = st.builds(
    M,
)
A_strategy = st.builds(
    A,
)
N_strategy = st.builds(
    N,
)
refinher2::Y_strategy = st.builds(
    refinher2::Y,
)
refinher2::H_strategy = st.builds(
    refinher2::H,
)
CE_strategy = st.builds(
    CE,
)
refinher2::DL_strategy = st.builds(
    refinher2::DL,
)
refinher2::DNamedElement_strategy = st.builds(
    refinher2::DNamedElement,
    name=
        safe_text
)
refinher2::M_strategy = st.builds(
    refinher2::M,
)
DNamedElement_strategy = st.builds(
    DNamedElement,
)
refinher2::N_strategy = st.builds(
    refinher2::N,
)
refinher2::AB_strategy = st.builds(
    refinher2::AB,
)
refinher2::A_strategy = st.builds(
    refinher2::A,
)
refinher2::E_strategy = st.builds(
    refinher2::E,
)
refinher2::DG_strategy = st.builds(
    refinher2::DG,
)
refinher2::DC_strategy = st.builds(
    refinher2::DC,
)
E_strategy = st.builds(
    E,
)
refinher2::CE_strategy = st.builds(
    refinher2::CE,
)
refinher2::DR_strategy = st.builds(
    refinher2::DR,
)
refinher2::BB_strategy = st.builds(
    refinher2::BB,
)

@given(instance=M_strategy)
@settings(max_examples=50)
def test_m_instantiation(instance):
    assert isinstance(instance, M)

@given(instance=A_strategy)
@settings(max_examples=50)
def test_a_instantiation(instance):
    assert isinstance(instance, A)

@given(instance=N_strategy)
@settings(max_examples=50)
def test_n_instantiation(instance):
    assert isinstance(instance, N)

@given(instance=refinher2::Y_strategy)
@settings(max_examples=50)
def test_refinher2::y_instantiation(instance):
    assert isinstance(instance, refinher2::Y)

@given(instance=refinher2::H_strategy)
@settings(max_examples=50)
def test_refinher2::h_instantiation(instance):
    assert isinstance(instance, refinher2::H)

@given(instance=CE_strategy)
@settings(max_examples=50)
def test_ce_instantiation(instance):
    assert isinstance(instance, CE)

@given(instance=refinher2::DL_strategy)
@settings(max_examples=50)
def test_refinher2::dl_instantiation(instance):
    assert isinstance(instance, refinher2::DL)

@given(instance=refinher2::DNamedElement_strategy)
@settings(max_examples=50)
def test_refinher2::dnamedelement_instantiation(instance):
    assert isinstance(instance, refinher2::DNamedElement)

@given(instance=refinher2::DNamedElement_strategy)
def test_refinher2::dnamedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=refinher2::DNamedElement_strategy)
def test_refinher2::dnamedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=refinher2::M_strategy)
@settings(max_examples=50)
def test_refinher2::m_instantiation(instance):
    assert isinstance(instance, refinher2::M)

@given(instance=DNamedElement_strategy)
@settings(max_examples=50)
def test_dnamedelement_instantiation(instance):
    assert isinstance(instance, DNamedElement)

@given(instance=refinher2::N_strategy)
@settings(max_examples=50)
def test_refinher2::n_instantiation(instance):
    assert isinstance(instance, refinher2::N)

@given(instance=refinher2::AB_strategy)
@settings(max_examples=50)
def test_refinher2::ab_instantiation(instance):
    assert isinstance(instance, refinher2::AB)

@given(instance=refinher2::A_strategy)
@settings(max_examples=50)
def test_refinher2::a_instantiation(instance):
    assert isinstance(instance, refinher2::A)

@given(instance=refinher2::E_strategy)
@settings(max_examples=50)
def test_refinher2::e_instantiation(instance):
    assert isinstance(instance, refinher2::E)

@given(instance=refinher2::DG_strategy)
@settings(max_examples=50)
def test_refinher2::dg_instantiation(instance):
    assert isinstance(instance, refinher2::DG)

@given(instance=refinher2::DC_strategy)
@settings(max_examples=50)
def test_refinher2::dc_instantiation(instance):
    assert isinstance(instance, refinher2::DC)

@given(instance=E_strategy)
@settings(max_examples=50)
def test_e_instantiation(instance):
    assert isinstance(instance, E)

@given(instance=refinher2::CE_strategy)
@settings(max_examples=50)
def test_refinher2::ce_instantiation(instance):
    assert isinstance(instance, refinher2::CE)

@given(instance=refinher2::DR_strategy)
@settings(max_examples=50)
def test_refinher2::dr_instantiation(instance):
    assert isinstance(instance, refinher2::DR)

@given(instance=refinher2::BB_strategy)
@settings(max_examples=50)
def test_refinher2::bb_instantiation(instance):
    assert isinstance(instance, refinher2::BB)
