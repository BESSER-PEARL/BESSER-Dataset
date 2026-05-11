import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    A,
    refinher3::M,
    CE,
    refinher3::DG,
    refinher3::DC,
    E,
    refinher3::CE,
    refinher3::DR,
    refinher3::DL,
    refinher3::DNamedElement,
    refinher3::N,
    DNamedElement,
    refinher3::Foobar,
    refinher3::A,
    refinher3::BB,
    refinher3::E,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_a_is_not_abstract():
    assert not inspect.isabstract(A)


def test_a_constructor_exists():
    assert callable(A.__init__)


def test_a_constructor_args():
    sig = inspect.signature(A.__init__)
    params = list(sig.parameters.keys())



def test_refinher3::m_is_not_abstract():
    assert not inspect.isabstract(refinher3::M)


def test_refinher3::m_constructor_exists():
    assert callable(refinher3::M.__init__)


def test_refinher3::m_constructor_args():
    sig = inspect.signature(refinher3::M.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_refinher3::m_has_id():
    assert hasattr(refinher3::M, "id")
    descriptor = None
    for klass in refinher3::M.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_ce_is_not_abstract():
    assert not inspect.isabstract(CE)


def test_ce_constructor_exists():
    assert callable(CE.__init__)


def test_ce_constructor_args():
    sig = inspect.signature(CE.__init__)
    params = list(sig.parameters.keys())



def test_refinher3::dg_is_not_abstract():
    assert not inspect.isabstract(refinher3::DG)


def test_refinher3::dg_constructor_exists():
    assert callable(refinher3::DG.__init__)


def test_refinher3::dg_constructor_args():
    sig = inspect.signature(refinher3::DG.__init__)
    params = list(sig.parameters.keys())



def test_refinher3::dc_is_not_abstract():
    assert not inspect.isabstract(refinher3::DC)


def test_refinher3::dc_constructor_exists():
    assert callable(refinher3::DC.__init__)


def test_refinher3::dc_constructor_args():
    sig = inspect.signature(refinher3::DC.__init__)
    params = list(sig.parameters.keys())



def test_e_is_not_abstract():
    assert not inspect.isabstract(E)


def test_e_constructor_exists():
    assert callable(E.__init__)


def test_e_constructor_args():
    sig = inspect.signature(E.__init__)
    params = list(sig.parameters.keys())



def test_refinher3::ce_is_not_abstract():
    assert not inspect.isabstract(refinher3::CE)


def test_refinher3::ce_constructor_exists():
    assert callable(refinher3::CE.__init__)


def test_refinher3::ce_constructor_args():
    sig = inspect.signature(refinher3::CE.__init__)
    params = list(sig.parameters.keys())



def test_refinher3::dr_is_not_abstract():
    assert not inspect.isabstract(refinher3::DR)


def test_refinher3::dr_constructor_exists():
    assert callable(refinher3::DR.__init__)


def test_refinher3::dr_constructor_args():
    sig = inspect.signature(refinher3::DR.__init__)
    params = list(sig.parameters.keys())



def test_refinher3::dl_is_not_abstract():
    assert not inspect.isabstract(refinher3::DL)


def test_refinher3::dl_constructor_exists():
    assert callable(refinher3::DL.__init__)


def test_refinher3::dl_constructor_args():
    sig = inspect.signature(refinher3::DL.__init__)
    params = list(sig.parameters.keys())



def test_refinher3::dnamedelement_is_not_abstract():
    assert not inspect.isabstract(refinher3::DNamedElement)


def test_refinher3::dnamedelement_constructor_exists():
    assert callable(refinher3::DNamedElement.__init__)


def test_refinher3::dnamedelement_constructor_args():
    sig = inspect.signature(refinher3::DNamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_refinher3::dnamedelement_has_name():
    assert hasattr(refinher3::DNamedElement, "name")
    descriptor = None
    for klass in refinher3::DNamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_refinher3::n_is_not_abstract():
    assert not inspect.isabstract(refinher3::N)


def test_refinher3::n_constructor_exists():
    assert callable(refinher3::N.__init__)


def test_refinher3::n_constructor_args():
    sig = inspect.signature(refinher3::N.__init__)
    params = list(sig.parameters.keys())
    assert "nam" in params, "Missing parameter 'nam'"

def test_refinher3::n_has_nam():
    assert hasattr(refinher3::N, "nam")
    descriptor = None
    for klass in refinher3::N.__mro__:
        if "nam" in klass.__dict__:
            descriptor = klass.__dict__["nam"]
            break
    assert isinstance(descriptor, property)



def test_dnamedelement_is_not_abstract():
    assert not inspect.isabstract(DNamedElement)


def test_dnamedelement_constructor_exists():
    assert callable(DNamedElement.__init__)


def test_dnamedelement_constructor_args():
    sig = inspect.signature(DNamedElement.__init__)
    params = list(sig.parameters.keys())



def test_refinher3::foobar_is_not_abstract():
    assert not inspect.isabstract(refinher3::Foobar)


def test_refinher3::foobar_constructor_exists():
    assert callable(refinher3::Foobar.__init__)


def test_refinher3::foobar_constructor_args():
    sig = inspect.signature(refinher3::Foobar.__init__)
    params = list(sig.parameters.keys())



def test_refinher3::a_is_not_abstract():
    assert not inspect.isabstract(refinher3::A)


def test_refinher3::a_constructor_exists():
    assert callable(refinher3::A.__init__)


def test_refinher3::a_constructor_args():
    sig = inspect.signature(refinher3::A.__init__)
    params = list(sig.parameters.keys())



def test_refinher3::bb_is_not_abstract():
    assert not inspect.isabstract(refinher3::BB)


def test_refinher3::bb_constructor_exists():
    assert callable(refinher3::BB.__init__)


def test_refinher3::bb_constructor_args():
    sig = inspect.signature(refinher3::BB.__init__)
    params = list(sig.parameters.keys())



def test_refinher3::e_is_not_abstract():
    assert not inspect.isabstract(refinher3::E)


def test_refinher3::e_constructor_exists():
    assert callable(refinher3::E.__init__)


def test_refinher3::e_constructor_args():
    sig = inspect.signature(refinher3::E.__init__)
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
A_strategy = st.builds(
    A,
)
refinher3::M_strategy = st.builds(
    refinher3::M,
    id=
        safe_text
)
CE_strategy = st.builds(
    CE,
)
refinher3::DG_strategy = st.builds(
    refinher3::DG,
)
refinher3::DC_strategy = st.builds(
    refinher3::DC,
)
E_strategy = st.builds(
    E,
)
refinher3::CE_strategy = st.builds(
    refinher3::CE,
)
refinher3::DR_strategy = st.builds(
    refinher3::DR,
)
refinher3::DL_strategy = st.builds(
    refinher3::DL,
)
refinher3::DNamedElement_strategy = st.builds(
    refinher3::DNamedElement,
    name=
        safe_text
)
refinher3::N_strategy = st.builds(
    refinher3::N,
    nam=
        safe_text
)
DNamedElement_strategy = st.builds(
    DNamedElement,
)
refinher3::Foobar_strategy = st.builds(
    refinher3::Foobar,
)
refinher3::A_strategy = st.builds(
    refinher3::A,
)
refinher3::BB_strategy = st.builds(
    refinher3::BB,
)
refinher3::E_strategy = st.builds(
    refinher3::E,
)

@given(instance=A_strategy)
@settings(max_examples=50)
def test_a_instantiation(instance):
    assert isinstance(instance, A)

@given(instance=refinher3::M_strategy)
@settings(max_examples=50)
def test_refinher3::m_instantiation(instance):
    assert isinstance(instance, refinher3::M)

@given(instance=refinher3::M_strategy)
def test_refinher3::m_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=refinher3::M_strategy)
def test_refinher3::m_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=CE_strategy)
@settings(max_examples=50)
def test_ce_instantiation(instance):
    assert isinstance(instance, CE)

@given(instance=refinher3::DG_strategy)
@settings(max_examples=50)
def test_refinher3::dg_instantiation(instance):
    assert isinstance(instance, refinher3::DG)

@given(instance=refinher3::DC_strategy)
@settings(max_examples=50)
def test_refinher3::dc_instantiation(instance):
    assert isinstance(instance, refinher3::DC)

@given(instance=E_strategy)
@settings(max_examples=50)
def test_e_instantiation(instance):
    assert isinstance(instance, E)

@given(instance=refinher3::CE_strategy)
@settings(max_examples=50)
def test_refinher3::ce_instantiation(instance):
    assert isinstance(instance, refinher3::CE)

@given(instance=refinher3::DR_strategy)
@settings(max_examples=50)
def test_refinher3::dr_instantiation(instance):
    assert isinstance(instance, refinher3::DR)

@given(instance=refinher3::DL_strategy)
@settings(max_examples=50)
def test_refinher3::dl_instantiation(instance):
    assert isinstance(instance, refinher3::DL)

@given(instance=refinher3::DNamedElement_strategy)
@settings(max_examples=50)
def test_refinher3::dnamedelement_instantiation(instance):
    assert isinstance(instance, refinher3::DNamedElement)

@given(instance=refinher3::DNamedElement_strategy)
def test_refinher3::dnamedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=refinher3::DNamedElement_strategy)
def test_refinher3::dnamedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=refinher3::N_strategy)
@settings(max_examples=50)
def test_refinher3::n_instantiation(instance):
    assert isinstance(instance, refinher3::N)

@given(instance=refinher3::N_strategy)
def test_refinher3::n_nam_type(instance):
    assert isinstance(instance.nam, str)


@given(instance=refinher3::N_strategy)
def test_refinher3::n_nam_setter(instance):
    original = instance.nam
    instance.nam = original
    assert instance.nam == original

@given(instance=DNamedElement_strategy)
@settings(max_examples=50)
def test_dnamedelement_instantiation(instance):
    assert isinstance(instance, DNamedElement)

@given(instance=refinher3::Foobar_strategy)
@settings(max_examples=50)
def test_refinher3::foobar_instantiation(instance):
    assert isinstance(instance, refinher3::Foobar)

@given(instance=refinher3::A_strategy)
@settings(max_examples=50)
def test_refinher3::a_instantiation(instance):
    assert isinstance(instance, refinher3::A)

@given(instance=refinher3::BB_strategy)
@settings(max_examples=50)
def test_refinher3::bb_instantiation(instance):
    assert isinstance(instance, refinher3::BB)

@given(instance=refinher3::E_strategy)
@settings(max_examples=50)
def test_refinher3::e_instantiation(instance):
    assert isinstance(instance, refinher3::E)
