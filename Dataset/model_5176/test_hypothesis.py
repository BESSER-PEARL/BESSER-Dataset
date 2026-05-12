import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    output_B,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_output_b_is_not_abstract():
    assert not inspect.isabstract(output_B)


def test_output_b_constructor_exists():
    assert callable(output_B.__init__)


def test_output_b_constructor_args():
    sig = inspect.signature(output_B.__init__)
    params = list(sig.parameters.keys())
    assert "b" in params, "Missing parameter 'b'"

def test_output_b_has_b():
    assert hasattr(output_B, "b")
    descriptor = None
    for klass in output_B.__mro__:
        if "b" in klass.__dict__:
            descriptor = klass.__dict__["b"]
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
output_B_strategy = st.builds(
    output_B,
    b=
        safe_text
)

@given(instance=output_B_strategy)
@settings(max_examples=50)
def test_output_b_instantiation(instance):
    assert isinstance(instance, output_B)



@given(instance=output_B_strategy)
def test_output_b_b_setter(instance):
    original = instance.b
    instance.b = original
    assert instance.b == original
