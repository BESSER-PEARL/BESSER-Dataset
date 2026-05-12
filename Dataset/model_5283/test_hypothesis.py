import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    astransast_AAS,
    astransast_BAS,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_astransast_aas_is_not_abstract():
    assert not inspect.isabstract(astransast_AAS)


def test_astransast_aas_constructor_exists():
    assert callable(astransast_AAS.__init__)


def test_astransast_aas_constructor_args():
    sig = inspect.signature(astransast_AAS.__init__)
    params = list(sig.parameters.keys())



def test_astransast_bas_is_not_abstract():
    assert not inspect.isabstract(astransast_BAS)


def test_astransast_bas_constructor_exists():
    assert callable(astransast_BAS.__init__)


def test_astransast_bas_constructor_args():
    sig = inspect.signature(astransast_BAS.__init__)
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
astransast_AAS_strategy = st.builds(
    astransast_AAS,
)
astransast_BAS_strategy = st.builds(
    astransast_BAS,
)

@given(instance=astransast_AAS_strategy)
@settings(max_examples=50)
def test_astransast_aas_instantiation(instance):
    assert isinstance(instance, astransast_AAS)

@given(instance=astransast_BAS_strategy)
@settings(max_examples=50)
def test_astransast_bas_instantiation(instance):
    assert isinstance(instance, astransast_BAS)
