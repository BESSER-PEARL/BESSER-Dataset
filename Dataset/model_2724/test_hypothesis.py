import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Kasu2::Root,
    Kasu2::ClassB,
    Kasu2::ClassA,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_kasu2::root_is_not_abstract():
    assert not inspect.isabstract(Kasu2::Root)


def test_kasu2::root_constructor_exists():
    assert callable(Kasu2::Root.__init__)


def test_kasu2::root_constructor_args():
    sig = inspect.signature(Kasu2::Root.__init__)
    params = list(sig.parameters.keys())



def test_kasu2::classb_is_not_abstract():
    assert not inspect.isabstract(Kasu2::ClassB)


def test_kasu2::classb_constructor_exists():
    assert callable(Kasu2::ClassB.__init__)


def test_kasu2::classb_constructor_args():
    sig = inspect.signature(Kasu2::ClassB.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_kasu2::classb_has_Name():
    assert hasattr(Kasu2::ClassB, "Name")
    descriptor = None
    for klass in Kasu2::ClassB.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_kasu2::classa_is_not_abstract():
    assert not inspect.isabstract(Kasu2::ClassA)


def test_kasu2::classa_constructor_exists():
    assert callable(Kasu2::ClassA.__init__)


def test_kasu2::classa_constructor_args():
    sig = inspect.signature(Kasu2::ClassA.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_kasu2::classa_has_Name():
    assert hasattr(Kasu2::ClassA, "Name")
    descriptor = None
    for klass in Kasu2::ClassA.__mro__:
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
Kasu2::Root_strategy = st.builds(
    Kasu2::Root,
)
Kasu2::ClassB_strategy = st.builds(
    Kasu2::ClassB,
    Name=
        safe_text
)
Kasu2::ClassA_strategy = st.builds(
    Kasu2::ClassA,
    Name=
        safe_text
)

@given(instance=Kasu2::Root_strategy)
@settings(max_examples=50)
def test_kasu2::root_instantiation(instance):
    assert isinstance(instance, Kasu2::Root)

@given(instance=Kasu2::ClassB_strategy)
@settings(max_examples=50)
def test_kasu2::classb_instantiation(instance):
    assert isinstance(instance, Kasu2::ClassB)

@given(instance=Kasu2::ClassB_strategy)
def test_kasu2::classb_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=Kasu2::ClassB_strategy)
def test_kasu2::classb_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=Kasu2::ClassA_strategy)
@settings(max_examples=50)
def test_kasu2::classa_instantiation(instance):
    assert isinstance(instance, Kasu2::ClassA)

@given(instance=Kasu2::ClassA_strategy)
def test_kasu2::classa_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=Kasu2::ClassA_strategy)
def test_kasu2::classa_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original
