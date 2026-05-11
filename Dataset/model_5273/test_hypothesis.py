import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    AddBindingTarget::Type3,
    AddBindingTarget::Type2,
    AddBindingTarget::Type1,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_addbindingtarget::type3_is_not_abstract():
    assert not inspect.isabstract(AddBindingTarget::Type3)


def test_addbindingtarget::type3_constructor_exists():
    assert callable(AddBindingTarget::Type3.__init__)


def test_addbindingtarget::type3_constructor_args():
    sig = inspect.signature(AddBindingTarget::Type3.__init__)
    params = list(sig.parameters.keys())



def test_addbindingtarget::type2_is_not_abstract():
    assert not inspect.isabstract(AddBindingTarget::Type2)


def test_addbindingtarget::type2_constructor_exists():
    assert callable(AddBindingTarget::Type2.__init__)


def test_addbindingtarget::type2_constructor_args():
    sig = inspect.signature(AddBindingTarget::Type2.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_addbindingtarget::type2_has_name():
    assert hasattr(AddBindingTarget::Type2, "name")
    descriptor = None
    for klass in AddBindingTarget::Type2.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_addbindingtarget::type1_is_not_abstract():
    assert not inspect.isabstract(AddBindingTarget::Type1)


def test_addbindingtarget::type1_constructor_exists():
    assert callable(AddBindingTarget::Type1.__init__)


def test_addbindingtarget::type1_constructor_args():
    sig = inspect.signature(AddBindingTarget::Type1.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_addbindingtarget::type1_has_name():
    assert hasattr(AddBindingTarget::Type1, "name")
    descriptor = None
    for klass in AddBindingTarget::Type1.__mro__:
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
AddBindingTarget::Type3_strategy = st.builds(
    AddBindingTarget::Type3,
)
AddBindingTarget::Type2_strategy = st.builds(
    AddBindingTarget::Type2,
    name=
        safe_text
)
AddBindingTarget::Type1_strategy = st.builds(
    AddBindingTarget::Type1,
    name=
        safe_text
)

@given(instance=AddBindingTarget::Type3_strategy)
@settings(max_examples=50)
def test_addbindingtarget::type3_instantiation(instance):
    assert isinstance(instance, AddBindingTarget::Type3)

@given(instance=AddBindingTarget::Type2_strategy)
@settings(max_examples=50)
def test_addbindingtarget::type2_instantiation(instance):
    assert isinstance(instance, AddBindingTarget::Type2)

@given(instance=AddBindingTarget::Type2_strategy)
def test_addbindingtarget::type2_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=AddBindingTarget::Type2_strategy)
def test_addbindingtarget::type2_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=AddBindingTarget::Type1_strategy)
@settings(max_examples=50)
def test_addbindingtarget::type1_instantiation(instance):
    assert isinstance(instance, AddBindingTarget::Type1)

@given(instance=AddBindingTarget::Type1_strategy)
def test_addbindingtarget::type1_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=AddBindingTarget::Type1_strategy)
def test_addbindingtarget::type1_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
