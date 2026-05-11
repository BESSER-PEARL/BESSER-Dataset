import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    main::sub1::Sub1Type,
    main::MainType,
    main::sub2::Sub2Type,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_main::sub1::sub1type_is_not_abstract():
    assert not inspect.isabstract(main::sub1::Sub1Type)


def test_main::sub1::sub1type_constructor_exists():
    assert callable(main::sub1::Sub1Type.__init__)


def test_main::sub1::sub1type_constructor_args():
    sig = inspect.signature(main::sub1::Sub1Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_main::sub1::sub1type_has_name():
    assert hasattr(main::sub1::Sub1Type, "name")
    descriptor = None
    for klass in main::sub1::Sub1Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_main::maintype_is_not_abstract():
    assert not inspect.isabstract(main::MainType)


def test_main::maintype_constructor_exists():
    assert callable(main::MainType.__init__)


def test_main::maintype_constructor_args():
    sig = inspect.signature(main::MainType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_main::maintype_has_name():
    assert hasattr(main::MainType, "name")
    descriptor = None
    for klass in main::MainType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_main::sub2::sub2type_is_not_abstract():
    assert not inspect.isabstract(main::sub2::Sub2Type)


def test_main::sub2::sub2type_constructor_exists():
    assert callable(main::sub2::Sub2Type.__init__)


def test_main::sub2::sub2type_constructor_args():
    sig = inspect.signature(main::sub2::Sub2Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_main::sub2::sub2type_has_name():
    assert hasattr(main::sub2::Sub2Type, "name")
    descriptor = None
    for klass in main::sub2::Sub2Type.__mro__:
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
main::sub1::Sub1Type_strategy = st.builds(
    main::sub1::Sub1Type,
    name=
        safe_text
)
main::MainType_strategy = st.builds(
    main::MainType,
    name=
        safe_text
)
main::sub2::Sub2Type_strategy = st.builds(
    main::sub2::Sub2Type,
    name=
        safe_text
)

@given(instance=main::sub1::Sub1Type_strategy)
@settings(max_examples=50)
def test_main::sub1::sub1type_instantiation(instance):
    assert isinstance(instance, main::sub1::Sub1Type)

@given(instance=main::sub1::Sub1Type_strategy)
def test_main::sub1::sub1type_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=main::sub1::Sub1Type_strategy)
def test_main::sub1::sub1type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=main::MainType_strategy)
@settings(max_examples=50)
def test_main::maintype_instantiation(instance):
    assert isinstance(instance, main::MainType)

@given(instance=main::MainType_strategy)
def test_main::maintype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=main::MainType_strategy)
def test_main::maintype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=main::sub2::Sub2Type_strategy)
@settings(max_examples=50)
def test_main::sub2::sub2type_instantiation(instance):
    assert isinstance(instance, main::sub2::Sub2Type)

@given(instance=main::sub2::Sub2Type_strategy)
def test_main::sub2::sub2type_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=main::sub2::Sub2Type_strategy)
def test_main::sub2::sub2type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
