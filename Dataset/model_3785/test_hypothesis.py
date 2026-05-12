import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    d_D,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_d_d_is_not_abstract():
    assert not inspect.isabstract(d_D)


def test_d_d_constructor_exists():
    assert callable(d_D.__init__)


def test_d_d_constructor_args():
    sig = inspect.signature(d_D.__init__)
    params = list(sig.parameters.keys())
    assert "atts" in params, "Missing parameter 'atts'"
    assert "name" in params, "Missing parameter 'name'"

def test_d_d_has_atts():
    assert hasattr(d_D, "atts")
    descriptor = None
    for klass in d_D.__mro__:
        if "atts" in klass.__dict__:
            descriptor = klass.__dict__["atts"]
            break
    assert isinstance(descriptor, property)

def test_d_d_has_name():
    assert hasattr(d_D, "name")
    descriptor = None
    for klass in d_D.__mro__:
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
d_D_strategy = st.builds(
    d_D,
    atts=
        safe_text,
    name=
        safe_text
)

@given(instance=d_D_strategy)
@settings(max_examples=50)
def test_d_d_instantiation(instance):
    assert isinstance(instance, d_D)



@given(instance=d_D_strategy)
def test_d_d_atts_setter(instance):
    original = instance.atts
    instance.atts = original
    assert instance.atts == original



@given(instance=d_D_strategy)
def test_d_d_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
