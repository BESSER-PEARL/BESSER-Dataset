import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    basesyntax3_B3,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_basesyntax3_b3_is_not_abstract():
    assert not inspect.isabstract(basesyntax3_B3)


def test_basesyntax3_b3_constructor_exists():
    assert callable(basesyntax3_B3.__init__)


def test_basesyntax3_b3_constructor_args():
    sig = inspect.signature(basesyntax3_B3.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_basesyntax3_b3_has_name():
    assert hasattr(basesyntax3_B3, "name")
    descriptor = None
    for klass in basesyntax3_B3.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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
basesyntax3_B3_strategy = st.builds(
    basesyntax3_B3,
    name=
        safe_text
)

@given(instance=basesyntax3_B3_strategy)
@settings(max_examples=50)
def test_basesyntax3_b3_instantiation(instance):
    assert isinstance(instance, basesyntax3_B3)



@given(instance=basesyntax3_B3_strategy)
def test_basesyntax3_b3_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
