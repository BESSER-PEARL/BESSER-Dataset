import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    main_subsub_SSC,
    subsub_SSC,
    main_M,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_main_subsub_ssc_is_not_abstract():
    assert not inspect.isabstract(main_subsub_SSC)


def test_main_subsub_ssc_constructor_exists():
    assert callable(main_subsub_SSC.__init__)


def test_main_subsub_ssc_constructor_args():
    sig = inspect.signature(main_subsub_SSC.__init__)
    params = list(sig.parameters.keys())



def test_subsub_ssc_is_not_abstract():
    assert not inspect.isabstract(subsub_SSC)


def test_subsub_ssc_constructor_exists():
    assert callable(subsub_SSC.__init__)


def test_subsub_ssc_constructor_args():
    sig = inspect.signature(subsub_SSC.__init__)
    params = list(sig.parameters.keys())



def test_main_m_is_not_abstract():
    assert not inspect.isabstract(main_M)


def test_main_m_constructor_exists():
    assert callable(main_M.__init__)


def test_main_m_constructor_args():
    sig = inspect.signature(main_M.__init__)
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
main_subsub_SSC_strategy = st.builds(
    main_subsub_SSC,
)
subsub_SSC_strategy = st.builds(
    subsub_SSC,
)
main_M_strategy = st.builds(
    main_M,
)

@given(instance=main_subsub_SSC_strategy)
@settings(max_examples=50)
def test_main_subsub_ssc_instantiation(instance):
    assert isinstance(instance, main_subsub_SSC)

@given(instance=subsub_SSC_strategy)
@settings(max_examples=50)
def test_subsub_ssc_instantiation(instance):
    assert isinstance(instance, subsub_SSC)

@given(instance=main_M_strategy)
@settings(max_examples=50)
def test_main_m_instantiation(instance):
    assert isinstance(instance, main_M)
