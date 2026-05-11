import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Root::NewEClass3,
    Root::NewEClass2,
    Root::NewEClass1,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_root::neweclass3_is_not_abstract():
    assert not inspect.isabstract(Root::NewEClass3)


def test_root::neweclass3_constructor_exists():
    assert callable(Root::NewEClass3.__init__)


def test_root::neweclass3_constructor_args():
    sig = inspect.signature(Root::NewEClass3.__init__)
    params = list(sig.parameters.keys())



def test_root::neweclass2_is_not_abstract():
    assert not inspect.isabstract(Root::NewEClass2)


def test_root::neweclass2_constructor_exists():
    assert callable(Root::NewEClass2.__init__)


def test_root::neweclass2_constructor_args():
    sig = inspect.signature(Root::NewEClass2.__init__)
    params = list(sig.parameters.keys())



def test_root::neweclass1_is_not_abstract():
    assert not inspect.isabstract(Root::NewEClass1)


def test_root::neweclass1_constructor_exists():
    assert callable(Root::NewEClass1.__init__)


def test_root::neweclass1_constructor_args():
    sig = inspect.signature(Root::NewEClass1.__init__)
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
Root::NewEClass3_strategy = st.builds(
    Root::NewEClass3,
)
Root::NewEClass2_strategy = st.builds(
    Root::NewEClass2,
)
Root::NewEClass1_strategy = st.builds(
    Root::NewEClass1,
)

@given(instance=Root::NewEClass3_strategy)
@settings(max_examples=50)
def test_root::neweclass3_instantiation(instance):
    assert isinstance(instance, Root::NewEClass3)

@given(instance=Root::NewEClass2_strategy)
@settings(max_examples=50)
def test_root::neweclass2_instantiation(instance):
    assert isinstance(instance, Root::NewEClass2)

@given(instance=Root::NewEClass1_strategy)
@settings(max_examples=50)
def test_root::neweclass1_instantiation(instance):
    assert isinstance(instance, Root::NewEClass1)
