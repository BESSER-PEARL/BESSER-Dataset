import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Kasu11::ClassB,
    Kasu11::ClassA,
    Kasu11::ClassC,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_kasu11::classb_is_not_abstract():
    assert not inspect.isabstract(Kasu11::ClassB)


def test_kasu11::classb_constructor_exists():
    assert callable(Kasu11::ClassB.__init__)


def test_kasu11::classb_constructor_args():
    sig = inspect.signature(Kasu11::ClassB.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_kasu11::classb_has_Name():
    assert hasattr(Kasu11::ClassB, "Name")
    descriptor = None
    for klass in Kasu11::ClassB.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_kasu11::classa_is_not_abstract():
    assert not inspect.isabstract(Kasu11::ClassA)


def test_kasu11::classa_constructor_exists():
    assert callable(Kasu11::ClassA.__init__)


def test_kasu11::classa_constructor_args():
    sig = inspect.signature(Kasu11::ClassA.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_kasu11::classa_has_Name():
    assert hasattr(Kasu11::ClassA, "Name")
    descriptor = None
    for klass in Kasu11::ClassA.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_kasu11::classc_is_not_abstract():
    assert not inspect.isabstract(Kasu11::ClassC)


def test_kasu11::classc_constructor_exists():
    assert callable(Kasu11::ClassC.__init__)


def test_kasu11::classc_constructor_args():
    sig = inspect.signature(Kasu11::ClassC.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_kasu11::classc_has_Name():
    assert hasattr(Kasu11::ClassC, "Name")
    descriptor = None
    for klass in Kasu11::ClassC.__mro__:
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
Kasu11::ClassB_strategy = st.builds(
    Kasu11::ClassB,
    Name=
        safe_text
)
Kasu11::ClassA_strategy = st.builds(
    Kasu11::ClassA,
    Name=
        safe_text
)
Kasu11::ClassC_strategy = st.builds(
    Kasu11::ClassC,
    Name=
        safe_text
)

@given(instance=Kasu11::ClassB_strategy)
@settings(max_examples=50)
def test_kasu11::classb_instantiation(instance):
    assert isinstance(instance, Kasu11::ClassB)

@given(instance=Kasu11::ClassB_strategy)
def test_kasu11::classb_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=Kasu11::ClassB_strategy)
def test_kasu11::classb_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=Kasu11::ClassA_strategy)
@settings(max_examples=50)
def test_kasu11::classa_instantiation(instance):
    assert isinstance(instance, Kasu11::ClassA)

@given(instance=Kasu11::ClassA_strategy)
def test_kasu11::classa_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=Kasu11::ClassA_strategy)
def test_kasu11::classa_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=Kasu11::ClassC_strategy)
@settings(max_examples=50)
def test_kasu11::classc_instantiation(instance):
    assert isinstance(instance, Kasu11::ClassC)

@given(instance=Kasu11::ClassC_strategy)
def test_kasu11::classc_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=Kasu11::ClassC_strategy)
def test_kasu11::classc_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original
