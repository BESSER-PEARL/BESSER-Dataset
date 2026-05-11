import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    testPackage::OnlyInDocument,
    testPackage::ExistsInBoth,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_testpackage::onlyindocument_is_not_abstract():
    assert not inspect.isabstract(testPackage::OnlyInDocument)


def test_testpackage::onlyindocument_constructor_exists():
    assert callable(testPackage::OnlyInDocument.__init__)


def test_testpackage::onlyindocument_constructor_args():
    sig = inspect.signature(testPackage::OnlyInDocument.__init__)
    params = list(sig.parameters.keys())



def test_testpackage::existsinboth_is_not_abstract():
    assert not inspect.isabstract(testPackage::ExistsInBoth)


def test_testpackage::existsinboth_constructor_exists():
    assert callable(testPackage::ExistsInBoth.__init__)


def test_testpackage::existsinboth_constructor_args():
    sig = inspect.signature(testPackage::ExistsInBoth.__init__)
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
testPackage::OnlyInDocument_strategy = st.builds(
    testPackage::OnlyInDocument,
)
testPackage::ExistsInBoth_strategy = st.builds(
    testPackage::ExistsInBoth,
)

@given(instance=testPackage::OnlyInDocument_strategy)
@settings(max_examples=50)
def test_testpackage::onlyindocument_instantiation(instance):
    assert isinstance(instance, testPackage::OnlyInDocument)

@given(instance=testPackage::ExistsInBoth_strategy)
@settings(max_examples=50)
def test_testpackage::existsinboth_instantiation(instance):
    assert isinstance(instance, testPackage::ExistsInBoth)
