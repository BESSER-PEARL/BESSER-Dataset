import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    LazyRuleInheritanceTest_ClassA,
    LazyRuleInheritanceTest_subpackage_ClassB,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_lazyruleinheritancetest_classa_is_not_abstract():
    assert not inspect.isabstract(LazyRuleInheritanceTest_ClassA)


def test_lazyruleinheritancetest_classa_constructor_exists():
    assert callable(LazyRuleInheritanceTest_ClassA.__init__)


def test_lazyruleinheritancetest_classa_constructor_args():
    sig = inspect.signature(LazyRuleInheritanceTest_ClassA.__init__)
    params = list(sig.parameters.keys())



def test_lazyruleinheritancetest_subpackage_classb_is_not_abstract():
    assert not inspect.isabstract(LazyRuleInheritanceTest_subpackage_ClassB)


def test_lazyruleinheritancetest_subpackage_classb_constructor_exists():
    assert callable(LazyRuleInheritanceTest_subpackage_ClassB.__init__)


def test_lazyruleinheritancetest_subpackage_classb_constructor_args():
    sig = inspect.signature(LazyRuleInheritanceTest_subpackage_ClassB.__init__)
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
LazyRuleInheritanceTest_ClassA_strategy = st.builds(
    LazyRuleInheritanceTest_ClassA,
)
LazyRuleInheritanceTest_subpackage_ClassB_strategy = st.builds(
    LazyRuleInheritanceTest_subpackage_ClassB,
)

@given(instance=LazyRuleInheritanceTest_ClassA_strategy)
@settings(max_examples=50)
def test_lazyruleinheritancetest_classa_instantiation(instance):
    assert isinstance(instance, LazyRuleInheritanceTest_ClassA)

@given(instance=LazyRuleInheritanceTest_subpackage_ClassB_strategy)
@settings(max_examples=50)
def test_lazyruleinheritancetest_subpackage_classb_instantiation(instance):
    assert isinstance(instance, LazyRuleInheritanceTest_subpackage_ClassB)
