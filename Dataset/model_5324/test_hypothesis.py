import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    testPackage_sub_OnlyInWorkingCopy,
    testPackage_ExistsInBoth,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_testpackage_sub_onlyinworkingcopy_is_not_abstract():
    assert not inspect.isabstract(testPackage_sub_OnlyInWorkingCopy)


def test_testpackage_sub_onlyinworkingcopy_constructor_exists():
    assert callable(testPackage_sub_OnlyInWorkingCopy.__init__)


def test_testpackage_sub_onlyinworkingcopy_constructor_args():
    sig = inspect.signature(testPackage_sub_OnlyInWorkingCopy.__init__)
    params = list(sig.parameters.keys())



def test_testpackage_existsinboth_is_not_abstract():
    assert not inspect.isabstract(testPackage_ExistsInBoth)


def test_testpackage_existsinboth_constructor_exists():
    assert callable(testPackage_ExistsInBoth.__init__)


def test_testpackage_existsinboth_constructor_args():
    sig = inspect.signature(testPackage_ExistsInBoth.__init__)
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
testPackage_sub_OnlyInWorkingCopy_strategy = st.builds(
    testPackage_sub_OnlyInWorkingCopy,
)
testPackage_ExistsInBoth_strategy = st.builds(
    testPackage_ExistsInBoth,
)

@given(instance=testPackage_sub_OnlyInWorkingCopy_strategy)
@settings(max_examples=50)
def test_testpackage_sub_onlyinworkingcopy_instantiation(instance):
    assert isinstance(instance, testPackage_sub_OnlyInWorkingCopy)

@given(instance=testPackage_ExistsInBoth_strategy)
@settings(max_examples=50)
def test_testpackage_existsinboth_instantiation(instance):
    assert isinstance(instance, testPackage_ExistsInBoth)
