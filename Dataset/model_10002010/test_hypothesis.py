import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Package_Class,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_package_class_is_not_abstract():
    assert not inspect.isabstract(Package_Class)


def test_package_class_constructor_exists():
    assert callable(Package_Class.__init__)


def test_package_class_constructor_args():
    sig = inspect.signature(Package_Class.__init__)
    params = list(sig.parameters.keys())
    assert "attribute" in params, "Missing parameter 'attribute'"

def test_package_class_has_attribute():
    assert hasattr(Package_Class, "attribute")
    descriptor = None
    for klass in Package_Class.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
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
Package_Class_strategy = st.builds(
    Package_Class,
    attribute=
        safe_text
)

@given(instance=Package_Class_strategy)
@settings(max_examples=50)
def test_package_class_instantiation(instance):
    assert isinstance(instance, Package_Class)



@given(instance=Package_Class_strategy)
def test_package_class_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original
