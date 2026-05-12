import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Root_NewEClass3,
    Root_NewEClass2,
    Root_NewEClass1,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_root_neweclass3_is_not_abstract():
    assert not inspect.isabstract(Root_NewEClass3)


def test_root_neweclass3_constructor_exists():
    assert callable(Root_NewEClass3.__init__)


def test_root_neweclass3_constructor_args():
    sig = inspect.signature(Root_NewEClass3.__init__)
    params = list(sig.parameters.keys())



def test_root_neweclass2_is_not_abstract():
    assert not inspect.isabstract(Root_NewEClass2)


def test_root_neweclass2_constructor_exists():
    assert callable(Root_NewEClass2.__init__)


def test_root_neweclass2_constructor_args():
    sig = inspect.signature(Root_NewEClass2.__init__)
    params = list(sig.parameters.keys())



def test_root_neweclass1_is_not_abstract():
    assert not inspect.isabstract(Root_NewEClass1)


def test_root_neweclass1_constructor_exists():
    assert callable(Root_NewEClass1.__init__)


def test_root_neweclass1_constructor_args():
    sig = inspect.signature(Root_NewEClass1.__init__)
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
Root_NewEClass3_strategy = st.builds(
    Root_NewEClass3,
)
Root_NewEClass2_strategy = st.builds(
    Root_NewEClass2,
)
Root_NewEClass1_strategy = st.builds(
    Root_NewEClass1,
)

@given(instance=Root_NewEClass3_strategy)
@settings(max_examples=50)
def test_root_neweclass3_instantiation(instance):
    assert isinstance(instance, Root_NewEClass3)

@given(instance=Root_NewEClass2_strategy)
@settings(max_examples=50)
def test_root_neweclass2_instantiation(instance):
    assert isinstance(instance, Root_NewEClass2)

@given(instance=Root_NewEClass1_strategy)
@settings(max_examples=50)
def test_root_neweclass1_instantiation(instance):
    assert isinstance(instance, Root_NewEClass1)
