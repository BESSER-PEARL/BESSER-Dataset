import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    testPackage_OnlyInDocument,
    testPackage_ExistsInBoth,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_testpackage_onlyindocument_is_not_abstract():
    assert not inspect.isabstract(testPackage_OnlyInDocument)


def test_testpackage_onlyindocument_constructor_exists():
    assert callable(testPackage_OnlyInDocument.__init__)


def test_testpackage_onlyindocument_constructor_args():
    sig = inspect.signature(testPackage_OnlyInDocument.__init__)
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
testPackage_OnlyInDocument_strategy = st.builds(
    testPackage_OnlyInDocument,
)
testPackage_ExistsInBoth_strategy = st.builds(
    testPackage_ExistsInBoth,
)

@given(instance=testPackage_OnlyInDocument_strategy)
@settings(max_examples=50)
def test_testpackage_onlyindocument_instantiation(instance):
    assert isinstance(instance, testPackage_OnlyInDocument)

@given(instance=testPackage_ExistsInBoth_strategy)
@settings(max_examples=50)
def test_testpackage_existsinboth_instantiation(instance):
    assert isinstance(instance, testPackage_ExistsInBoth)
