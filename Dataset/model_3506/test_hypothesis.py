import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    test1unique_ConceptA,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_test1unique_concepta_is_not_abstract():
    assert not inspect.isabstract(test1unique_ConceptA)


def test_test1unique_concepta_constructor_exists():
    assert callable(test1unique_ConceptA.__init__)


def test_test1unique_concepta_constructor_args():
    sig = inspect.signature(test1unique_ConceptA.__init__)
    params = list(sig.parameters.keys())
    assert "bs" in params, "Missing parameter 'bs'"

def test_test1unique_concepta_has_bs():
    assert hasattr(test1unique_ConceptA, "bs")
    descriptor = None
    for klass in test1unique_ConceptA.__mro__:
        if "bs" in klass.__dict__:
            descriptor = klass.__dict__["bs"]
            break
    assert isinstance(descriptor, property)


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
test1unique_ConceptA_strategy = st.builds(
    test1unique_ConceptA,
    bs=
        safe_text
)

@given(instance=test1unique_ConceptA_strategy)
@settings(max_examples=50)
def test_test1unique_concepta_instantiation(instance):
    assert isinstance(instance, test1unique_ConceptA)



@given(instance=test1unique_ConceptA_strategy)
def test_test1unique_concepta_bs_setter(instance):
    original = instance.bs
    instance.bs = original
    assert instance.bs == original
