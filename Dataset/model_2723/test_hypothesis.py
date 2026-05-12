import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Kasu4_ClassB,
    Kasu4_ClassA,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_kasu4_classb_is_not_abstract():
    assert not inspect.isabstract(Kasu4_ClassB)


def test_kasu4_classb_constructor_exists():
    assert callable(Kasu4_ClassB.__init__)


def test_kasu4_classb_constructor_args():
    sig = inspect.signature(Kasu4_ClassB.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_kasu4_classb_has_Name():
    assert hasattr(Kasu4_ClassB, "Name")
    descriptor = None
    for klass in Kasu4_ClassB.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_kasu4_classa_is_not_abstract():
    assert not inspect.isabstract(Kasu4_ClassA)


def test_kasu4_classa_constructor_exists():
    assert callable(Kasu4_ClassA.__init__)


def test_kasu4_classa_constructor_args():
    sig = inspect.signature(Kasu4_ClassA.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_kasu4_classa_has_Name():
    assert hasattr(Kasu4_ClassA, "Name")
    descriptor = None
    for klass in Kasu4_ClassA.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
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
Kasu4_ClassB_strategy = st.builds(
    Kasu4_ClassB,
    Name=
        safe_text
)
Kasu4_ClassA_strategy = st.builds(
    Kasu4_ClassA,
    Name=
        safe_text
)

@given(instance=Kasu4_ClassB_strategy)
@settings(max_examples=50)
def test_kasu4_classb_instantiation(instance):
    assert isinstance(instance, Kasu4_ClassB)



@given(instance=Kasu4_ClassB_strategy)
def test_kasu4_classb_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=Kasu4_ClassA_strategy)
@settings(max_examples=50)
def test_kasu4_classa_instantiation(instance):
    assert isinstance(instance, Kasu4_ClassA)



@given(instance=Kasu4_ClassA_strategy)
def test_kasu4_classa_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original
