import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    astransast::AAS,
    astransast::BAS,
    astransast::C,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_astransast::aas_is_not_abstract():
    assert not inspect.isabstract(astransast::AAS)


def test_astransast::aas_constructor_exists():
    assert callable(astransast::AAS.__init__)


def test_astransast::aas_constructor_args():
    sig = inspect.signature(astransast::AAS.__init__)
    params = list(sig.parameters.keys())



def test_astransast::bas_is_not_abstract():
    assert not inspect.isabstract(astransast::BAS)


def test_astransast::bas_constructor_exists():
    assert callable(astransast::BAS.__init__)


def test_astransast::bas_constructor_args():
    sig = inspect.signature(astransast::BAS.__init__)
    params = list(sig.parameters.keys())



def test_astransast::c_is_not_abstract():
    assert not inspect.isabstract(astransast::C)


def test_astransast::c_constructor_exists():
    assert callable(astransast::C.__init__)


def test_astransast::c_constructor_args():
    sig = inspect.signature(astransast::C.__init__)
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
astransast::AAS_strategy = st.builds(
    astransast::AAS,
)
astransast::BAS_strategy = st.builds(
    astransast::BAS,
)
astransast::C_strategy = st.builds(
    astransast::C,
)

@given(instance=astransast::AAS_strategy)
@settings(max_examples=50)
def test_astransast::aas_instantiation(instance):
    assert isinstance(instance, astransast::AAS)

@given(instance=astransast::BAS_strategy)
@settings(max_examples=50)
def test_astransast::bas_instantiation(instance):
    assert isinstance(instance, astransast::BAS)

@given(instance=astransast::C_strategy)
@settings(max_examples=50)
def test_astransast::c_instantiation(instance):
    assert isinstance(instance, astransast::C)
