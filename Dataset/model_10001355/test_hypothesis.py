import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    venda,
    VendaParcelada,
    VendaAVista,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_venda_is_not_abstract():
    assert not inspect.isabstract(venda)


def test_venda_constructor_exists():
    assert callable(venda.__init__)


def test_venda_constructor_args():
    sig = inspect.signature(venda.__init__)
    params = list(sig.parameters.keys())



def test_vendaparcelada_is_not_abstract():
    assert not inspect.isabstract(VendaParcelada)


def test_vendaparcelada_constructor_exists():
    assert callable(VendaParcelada.__init__)


def test_vendaparcelada_constructor_args():
    sig = inspect.signature(VendaParcelada.__init__)
    params = list(sig.parameters.keys())



def test_vendaavista_is_not_abstract():
    assert not inspect.isabstract(VendaAVista)


def test_vendaavista_constructor_exists():
    assert callable(VendaAVista.__init__)


def test_vendaavista_constructor_args():
    sig = inspect.signature(VendaAVista.__init__)
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
venda_strategy = st.builds(
    venda,
)
VendaParcelada_strategy = st.builds(
    VendaParcelada,
)
VendaAVista_strategy = st.builds(
    VendaAVista,
)

@given(instance=venda_strategy)
@settings(max_examples=50)
def test_venda_instantiation(instance):
    assert isinstance(instance, venda)

@given(instance=VendaParcelada_strategy)
@settings(max_examples=50)
def test_vendaparcelada_instantiation(instance):
    assert isinstance(instance, VendaParcelada)

@given(instance=VendaAVista_strategy)
@settings(max_examples=50)
def test_vendaavista_instantiation(instance):
    assert isinstance(instance, VendaAVista)
