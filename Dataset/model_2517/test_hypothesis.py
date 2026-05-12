import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    test_EClass0,
    test_EClass1,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_test_eclass0_is_not_abstract():
    assert not inspect.isabstract(test_EClass0)


def test_test_eclass0_constructor_exists():
    assert callable(test_EClass0.__init__)


def test_test_eclass0_constructor_args():
    sig = inspect.signature(test_EClass0.__init__)
    params = list(sig.parameters.keys())
    assert "EAttribute0" in params, "Missing parameter 'EAttribute0'"

def test_test_eclass0_has_EAttribute0():
    assert hasattr(test_EClass0, "EAttribute0")
    descriptor = None
    for klass in test_EClass0.__mro__:
        if "EAttribute0" in klass.__dict__:
            descriptor = klass.__dict__["EAttribute0"]
            break
    assert isinstance(descriptor, property)



def test_test_eclass1_is_not_abstract():
    assert not inspect.isabstract(test_EClass1)


def test_test_eclass1_constructor_exists():
    assert callable(test_EClass1.__init__)


def test_test_eclass1_constructor_args():
    sig = inspect.signature(test_EClass1.__init__)
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
test_EClass0_strategy = st.builds(
    test_EClass0,
    EAttribute0=
        st.booleans()
)
test_EClass1_strategy = st.builds(
    test_EClass1,
)

@given(instance=test_EClass0_strategy)
@settings(max_examples=50)
def test_test_eclass0_instantiation(instance):
    assert isinstance(instance, test_EClass0)



@given(instance=test_EClass0_strategy)
def test_test_eclass0_EAttribute0_setter(instance):
    original = instance.EAttribute0
    instance.EAttribute0 = original
    assert instance.EAttribute0 == original

@given(instance=test_EClass1_strategy)
@settings(max_examples=50)
def test_test_eclass1_instantiation(instance):
    assert isinstance(instance, test_EClass1)
