import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    basesyntax2_B2,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_basesyntax2_b2_is_not_abstract():
    assert not inspect.isabstract(basesyntax2_B2)


def test_basesyntax2_b2_constructor_exists():
    assert callable(basesyntax2_B2.__init__)


def test_basesyntax2_b2_constructor_args():
    sig = inspect.signature(basesyntax2_B2.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_basesyntax2_b2_has_name():
    assert hasattr(basesyntax2_B2, "name")
    descriptor = None
    for klass in basesyntax2_B2.__mro__:
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
basesyntax2_B2_strategy = st.builds(
    basesyntax2_B2,
    name=
        safe_text
)

@given(instance=basesyntax2_B2_strategy)
@settings(max_examples=50)
def test_basesyntax2_b2_instantiation(instance):
    assert isinstance(instance, basesyntax2_B2)



@given(instance=basesyntax2_B2_strategy)
def test_basesyntax2_b2_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
