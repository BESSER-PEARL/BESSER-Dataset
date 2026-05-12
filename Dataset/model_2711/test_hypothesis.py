import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Kasu11_ClassB,
    Kasu11_ClassA,
    Kasu11_ClassC,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_kasu11_classb_is_not_abstract():
    assert not inspect.isabstract(Kasu11_ClassB)


def test_kasu11_classb_constructor_exists():
    assert callable(Kasu11_ClassB.__init__)


def test_kasu11_classb_constructor_args():
    sig = inspect.signature(Kasu11_ClassB.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_kasu11_classb_has_Name():
    assert hasattr(Kasu11_ClassB, "Name")
    descriptor = None
    for klass in Kasu11_ClassB.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_kasu11_classa_is_not_abstract():
    assert not inspect.isabstract(Kasu11_ClassA)


def test_kasu11_classa_constructor_exists():
    assert callable(Kasu11_ClassA.__init__)


def test_kasu11_classa_constructor_args():
    sig = inspect.signature(Kasu11_ClassA.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_kasu11_classa_has_Name():
    assert hasattr(Kasu11_ClassA, "Name")
    descriptor = None
    for klass in Kasu11_ClassA.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_kasu11_classc_is_not_abstract():
    assert not inspect.isabstract(Kasu11_ClassC)


def test_kasu11_classc_constructor_exists():
    assert callable(Kasu11_ClassC.__init__)


def test_kasu11_classc_constructor_args():
    sig = inspect.signature(Kasu11_ClassC.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_kasu11_classc_has_Name():
    assert hasattr(Kasu11_ClassC, "Name")
    descriptor = None
    for klass in Kasu11_ClassC.__mro__:
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
Kasu11_ClassB_strategy = st.builds(
    Kasu11_ClassB,
    Name=
        safe_text
)
Kasu11_ClassA_strategy = st.builds(
    Kasu11_ClassA,
    Name=
        safe_text
)
Kasu11_ClassC_strategy = st.builds(
    Kasu11_ClassC,
    Name=
        safe_text
)

@given(instance=Kasu11_ClassB_strategy)
@settings(max_examples=50)
def test_kasu11_classb_instantiation(instance):
    assert isinstance(instance, Kasu11_ClassB)



@given(instance=Kasu11_ClassB_strategy)
def test_kasu11_classb_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=Kasu11_ClassA_strategy)
@settings(max_examples=50)
def test_kasu11_classa_instantiation(instance):
    assert isinstance(instance, Kasu11_ClassA)



@given(instance=Kasu11_ClassA_strategy)
def test_kasu11_classa_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=Kasu11_ClassC_strategy)
@settings(max_examples=50)
def test_kasu11_classc_instantiation(instance):
    assert isinstance(instance, Kasu11_ClassC)



@given(instance=Kasu11_ClassC_strategy)
def test_kasu11_classc_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original
