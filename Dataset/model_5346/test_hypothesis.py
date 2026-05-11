import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    basesyntax1::B1,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_basesyntax1::b1_is_not_abstract():
    assert not inspect.isabstract(basesyntax1::B1)


def test_basesyntax1::b1_constructor_exists():
    assert callable(basesyntax1::B1.__init__)


def test_basesyntax1::b1_constructor_args():
    sig = inspect.signature(basesyntax1::B1.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_basesyntax1::b1_has_name():
    assert hasattr(basesyntax1::B1, "name")
    descriptor = None
    for klass in basesyntax1::B1.__mro__:
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
basesyntax1::B1_strategy = st.builds(
    basesyntax1::B1,
    name=
        safe_text
)

@given(instance=basesyntax1::B1_strategy)
@settings(max_examples=50)
def test_basesyntax1::b1_instantiation(instance):
    assert isinstance(instance, basesyntax1::B1)

@given(instance=basesyntax1::B1_strategy)
def test_basesyntax1::b1_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=basesyntax1::B1_strategy)
def test_basesyntax1::b1_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
