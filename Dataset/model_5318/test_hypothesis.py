import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    main::subsub::SSC,
    subsub::SSC,
    main::M,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_main::subsub::ssc_is_not_abstract():
    assert not inspect.isabstract(main::subsub::SSC)


def test_main::subsub::ssc_constructor_exists():
    assert callable(main::subsub::SSC.__init__)


def test_main::subsub::ssc_constructor_args():
    sig = inspect.signature(main::subsub::SSC.__init__)
    params = list(sig.parameters.keys())



def test_subsub::ssc_is_not_abstract():
    assert not inspect.isabstract(subsub::SSC)


def test_subsub::ssc_constructor_exists():
    assert callable(subsub::SSC.__init__)


def test_subsub::ssc_constructor_args():
    sig = inspect.signature(subsub::SSC.__init__)
    params = list(sig.parameters.keys())



def test_main::m_is_not_abstract():
    assert not inspect.isabstract(main::M)


def test_main::m_constructor_exists():
    assert callable(main::M.__init__)


def test_main::m_constructor_args():
    sig = inspect.signature(main::M.__init__)
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
main::subsub::SSC_strategy = st.builds(
    main::subsub::SSC,
)
subsub::SSC_strategy = st.builds(
    subsub::SSC,
)
main::M_strategy = st.builds(
    main::M,
)

@given(instance=main::subsub::SSC_strategy)
@settings(max_examples=50)
def test_main::subsub::ssc_instantiation(instance):
    assert isinstance(instance, main::subsub::SSC)

@given(instance=subsub::SSC_strategy)
@settings(max_examples=50)
def test_subsub::ssc_instantiation(instance):
    assert isinstance(instance, subsub::SSC)

@given(instance=main::M_strategy)
@settings(max_examples=50)
def test_main::m_instantiation(instance):
    assert isinstance(instance, main::M)
