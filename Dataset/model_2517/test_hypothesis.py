import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    test::EClass0,
    test::EClass1,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_test::eclass0_is_not_abstract():
    assert not inspect.isabstract(test::EClass0)


def test_test::eclass0_constructor_exists():
    assert callable(test::EClass0.__init__)


def test_test::eclass0_constructor_args():
    sig = inspect.signature(test::EClass0.__init__)
    params = list(sig.parameters.keys())
    assert "EAttribute0" in params, "Missing parameter 'EAttribute0'"

def test_test::eclass0_has_EAttribute0():
    assert hasattr(test::EClass0, "EAttribute0")
    descriptor = None
    for klass in test::EClass0.__mro__:
        if "EAttribute0" in klass.__dict__:
            descriptor = klass.__dict__["EAttribute0"]
            break
    assert isinstance(descriptor, property)



def test_test::eclass1_is_not_abstract():
    assert not inspect.isabstract(test::EClass1)


def test_test::eclass1_constructor_exists():
    assert callable(test::EClass1.__init__)


def test_test::eclass1_constructor_args():
    sig = inspect.signature(test::EClass1.__init__)
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
test::EClass0_strategy = st.builds(
    test::EClass0,
    EAttribute0=
        st.booleans()
)
test::EClass1_strategy = st.builds(
    test::EClass1,
)

@given(instance=test::EClass0_strategy)
@settings(max_examples=50)
def test_test::eclass0_instantiation(instance):
    assert isinstance(instance, test::EClass0)

@given(instance=test::EClass0_strategy)
def test_test::eclass0_EAttribute0_type(instance):
    assert isinstance(instance.EAttribute0, bool)


@given(instance=test::EClass0_strategy)
def test_test::eclass0_EAttribute0_setter(instance):
    original = instance.EAttribute0
    instance.EAttribute0 = original
    assert instance.EAttribute0 == original

@given(instance=test::EClass1_strategy)
@settings(max_examples=50)
def test_test::eclass1_instantiation(instance):
    assert isinstance(instance, test::EClass1)
