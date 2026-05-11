import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    subpackage::ClassB,
    LazyRuleInheritanceTest::subpackage::ClassB,
    LazyRuleInheritanceTest::ClassA,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_subpackage::classb_is_not_abstract():
    assert not inspect.isabstract(subpackage::ClassB)


def test_subpackage::classb_constructor_exists():
    assert callable(subpackage::ClassB.__init__)


def test_subpackage::classb_constructor_args():
    sig = inspect.signature(subpackage::ClassB.__init__)
    params = list(sig.parameters.keys())



def test_lazyruleinheritancetest::subpackage::classb_is_not_abstract():
    assert not inspect.isabstract(LazyRuleInheritanceTest::subpackage::ClassB)


def test_lazyruleinheritancetest::subpackage::classb_constructor_exists():
    assert callable(LazyRuleInheritanceTest::subpackage::ClassB.__init__)


def test_lazyruleinheritancetest::subpackage::classb_constructor_args():
    sig = inspect.signature(LazyRuleInheritanceTest::subpackage::ClassB.__init__)
    params = list(sig.parameters.keys())



def test_lazyruleinheritancetest::classa_is_not_abstract():
    assert not inspect.isabstract(LazyRuleInheritanceTest::ClassA)


def test_lazyruleinheritancetest::classa_constructor_exists():
    assert callable(LazyRuleInheritanceTest::ClassA.__init__)


def test_lazyruleinheritancetest::classa_constructor_args():
    sig = inspect.signature(LazyRuleInheritanceTest::ClassA.__init__)
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
subpackage::ClassB_strategy = st.builds(
    subpackage::ClassB,
)
LazyRuleInheritanceTest::subpackage::ClassB_strategy = st.builds(
    LazyRuleInheritanceTest::subpackage::ClassB,
)
LazyRuleInheritanceTest::ClassA_strategy = st.builds(
    LazyRuleInheritanceTest::ClassA,
)

@given(instance=subpackage::ClassB_strategy)
@settings(max_examples=50)
def test_subpackage::classb_instantiation(instance):
    assert isinstance(instance, subpackage::ClassB)

@given(instance=LazyRuleInheritanceTest::subpackage::ClassB_strategy)
@settings(max_examples=50)
def test_lazyruleinheritancetest::subpackage::classb_instantiation(instance):
    assert isinstance(instance, LazyRuleInheritanceTest::subpackage::ClassB)

@given(instance=LazyRuleInheritanceTest::ClassA_strategy)
@settings(max_examples=50)
def test_lazyruleinheritancetest::classa_instantiation(instance):
    assert isinstance(instance, LazyRuleInheritanceTest::ClassA)
