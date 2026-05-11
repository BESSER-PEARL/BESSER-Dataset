import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    testPackage::sub::OnlyInWorkingCopy,
    testPackage::ExistsInBoth,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_testpackage::sub::onlyinworkingcopy_is_not_abstract():
    assert not inspect.isabstract(testPackage::sub::OnlyInWorkingCopy)


def test_testpackage::sub::onlyinworkingcopy_constructor_exists():
    assert callable(testPackage::sub::OnlyInWorkingCopy.__init__)


def test_testpackage::sub::onlyinworkingcopy_constructor_args():
    sig = inspect.signature(testPackage::sub::OnlyInWorkingCopy.__init__)
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
testPackage::sub::OnlyInWorkingCopy_strategy = st.builds(
    testPackage::sub::OnlyInWorkingCopy,
)
testPackage::ExistsInBoth_strategy = st.builds(
    testPackage::ExistsInBoth,
)

@given(instance=testPackage::sub::OnlyInWorkingCopy_strategy)
@settings(max_examples=50)
def test_testpackage::sub::onlyinworkingcopy_instantiation(instance):
    assert isinstance(instance, testPackage::sub::OnlyInWorkingCopy)

@given(instance=testPackage::ExistsInBoth_strategy)
@settings(max_examples=50)
def test_testpackage::existsinboth_instantiation(instance):
    assert isinstance(instance, testPackage::ExistsInBoth)
