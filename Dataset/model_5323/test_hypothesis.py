import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    main_sub2_Sub2Type,
    main_sub1_Sub1Type,
    main_MainType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_main_sub2_sub2type_is_not_abstract():
    assert not inspect.isabstract(main_sub2_Sub2Type)


def test_main_sub2_sub2type_constructor_exists():
    assert callable(main_sub2_Sub2Type.__init__)


def test_main_sub2_sub2type_constructor_args():
    sig = inspect.signature(main_sub2_Sub2Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_main_sub2_sub2type_has_name():
    assert hasattr(main_sub2_Sub2Type, "name")
    descriptor = None
    for klass in main_sub2_Sub2Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_main_sub1_sub1type_is_not_abstract():
    assert not inspect.isabstract(main_sub1_Sub1Type)


def test_main_sub1_sub1type_constructor_exists():
    assert callable(main_sub1_Sub1Type.__init__)


def test_main_sub1_sub1type_constructor_args():
    sig = inspect.signature(main_sub1_Sub1Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_main_sub1_sub1type_has_name():
    assert hasattr(main_sub1_Sub1Type, "name")
    descriptor = None
    for klass in main_sub1_Sub1Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_main_maintype_is_not_abstract():
    assert not inspect.isabstract(main_MainType)


def test_main_maintype_constructor_exists():
    assert callable(main_MainType.__init__)


def test_main_maintype_constructor_args():
    sig = inspect.signature(main_MainType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_main_maintype_has_name():
    assert hasattr(main_MainType, "name")
    descriptor = None
    for klass in main_MainType.__mro__:
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
main_sub2_Sub2Type_strategy = st.builds(
    main_sub2_Sub2Type,
    name=
        safe_text
)
main_sub1_Sub1Type_strategy = st.builds(
    main_sub1_Sub1Type,
    name=
        safe_text
)
main_MainType_strategy = st.builds(
    main_MainType,
    name=
        safe_text
)

@given(instance=main_sub2_Sub2Type_strategy)
@settings(max_examples=50)
def test_main_sub2_sub2type_instantiation(instance):
    assert isinstance(instance, main_sub2_Sub2Type)



@given(instance=main_sub2_Sub2Type_strategy)
def test_main_sub2_sub2type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=main_sub1_Sub1Type_strategy)
@settings(max_examples=50)
def test_main_sub1_sub1type_instantiation(instance):
    assert isinstance(instance, main_sub1_Sub1Type)



@given(instance=main_sub1_Sub1Type_strategy)
def test_main_sub1_sub1type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=main_MainType_strategy)
@settings(max_examples=50)
def test_main_maintype_instantiation(instance):
    assert isinstance(instance, main_MainType)



@given(instance=main_MainType_strategy)
def test_main_maintype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
