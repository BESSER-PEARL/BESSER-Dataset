import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    testenums_Root,
    Enum1,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_testenums_root_is_not_abstract():
    assert not inspect.isabstract(testenums_Root)


def test_testenums_root_constructor_exists():
    assert callable(testenums_Root.__init__)


def test_testenums_root_constructor_args():
    sig = inspect.signature(testenums_Root.__init__)
    params = list(sig.parameters.keys())
    assert "enums" in params, "Missing parameter 'enums'"
    assert "enum" in params, "Missing parameter 'enum'"

def test_testenums_root_has_enums():
    assert hasattr(testenums_Root, "enums")
    descriptor = None
    for klass in testenums_Root.__mro__:
        if "enums" in klass.__dict__:
            descriptor = klass.__dict__["enums"]
            break
    assert isinstance(descriptor, property)

def test_testenums_root_has_enum():
    assert hasattr(testenums_Root, "enum")
    descriptor = None
    for klass in testenums_Root.__mro__:
        if "enum" in klass.__dict__:
            descriptor = klass.__dict__["enum"]
            break
    assert isinstance(descriptor, property)

def test_enum1_exists():
    # Check that the Enumeration exists
    assert Enum1 is not None

def test_enum1_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Enum1]
    expected_literals = [
        "LITERAL1",
        "LITERAL0",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Enum1"


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
testenums_Root_strategy = st.builds(
    testenums_Root,
    enums=
        safe_text,
    enum=
        safe_text
)

@given(instance=testenums_Root_strategy)
@settings(max_examples=50)
def test_testenums_root_instantiation(instance):
    assert isinstance(instance, testenums_Root)



@given(instance=testenums_Root_strategy)
def test_testenums_root_enums_setter(instance):
    original = instance.enums
    instance.enums = original
    assert instance.enums == original



@given(instance=testenums_Root_strategy)
def test_testenums_root_enum_setter(instance):
    original = instance.enum
    instance.enum = original
    assert instance.enum == original
