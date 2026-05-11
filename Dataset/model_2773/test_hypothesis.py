import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    nestedgroup::A,
    nestedgroup::Element,
    nestedgroup::CType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_nestedgroup::a_is_not_abstract():
    assert not inspect.isabstract(nestedgroup::A)


def test_nestedgroup::a_constructor_exists():
    assert callable(nestedgroup::A.__init__)


def test_nestedgroup::a_constructor_args():
    sig = inspect.signature(nestedgroup::A.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "group" in params, "Missing parameter 'group'"
    assert "b" in params, "Missing parameter 'b'"

def test_nestedgroup::a_has_name():
    assert hasattr(nestedgroup::A, "name")
    descriptor = None
    for klass in nestedgroup::A.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_nestedgroup::a_has_group():
    assert hasattr(nestedgroup::A, "group")
    descriptor = None
    for klass in nestedgroup::A.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_nestedgroup::a_has_b():
    assert hasattr(nestedgroup::A, "b")
    descriptor = None
    for klass in nestedgroup::A.__mro__:
        if "b" in klass.__dict__:
            descriptor = klass.__dict__["b"]
            break
    assert isinstance(descriptor, property)



def test_nestedgroup::element_is_not_abstract():
    assert not inspect.isabstract(nestedgroup::Element)


def test_nestedgroup::element_constructor_exists():
    assert callable(nestedgroup::Element.__init__)


def test_nestedgroup::element_constructor_args():
    sig = inspect.signature(nestedgroup::Element.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "name" in params, "Missing parameter 'name'"
    assert "true" in params, "Missing parameter 'true'"

def test_nestedgroup::element_has_mixed():
    assert hasattr(nestedgroup::Element, "mixed")
    descriptor = None
    for klass in nestedgroup::Element.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_nestedgroup::element_has_name():
    assert hasattr(nestedgroup::Element, "name")
    descriptor = None
    for klass in nestedgroup::Element.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_nestedgroup::element_has_true():
    assert hasattr(nestedgroup::Element, "true")
    descriptor = None
    for klass in nestedgroup::Element.__mro__:
        if "true" in klass.__dict__:
            descriptor = klass.__dict__["true"]
            break
    assert isinstance(descriptor, property)



def test_nestedgroup::ctype_is_not_abstract():
    assert not inspect.isabstract(nestedgroup::CType)


def test_nestedgroup::ctype_constructor_exists():
    assert callable(nestedgroup::CType.__init__)


def test_nestedgroup::ctype_constructor_args():
    sig = inspect.signature(nestedgroup::CType.__init__)
    params = list(sig.parameters.keys())
    assert "cvalue" in params, "Missing parameter 'cvalue'"
    assert "cname" in params, "Missing parameter 'cname'"

def test_nestedgroup::ctype_has_cvalue():
    assert hasattr(nestedgroup::CType, "cvalue")
    descriptor = None
    for klass in nestedgroup::CType.__mro__:
        if "cvalue" in klass.__dict__:
            descriptor = klass.__dict__["cvalue"]
            break
    assert isinstance(descriptor, property)

def test_nestedgroup::ctype_has_cname():
    assert hasattr(nestedgroup::CType, "cname")
    descriptor = None
    for klass in nestedgroup::CType.__mro__:
        if "cname" in klass.__dict__:
            descriptor = klass.__dict__["cname"]
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
nestedgroup::A_strategy = st.builds(
    nestedgroup::A,
    name=
        safe_text,
    group=
        safe_text,
    b=
        safe_text
)
nestedgroup::Element_strategy = st.builds(
    nestedgroup::Element,
    mixed=
        safe_text,
    name=
        safe_text,
    true=
        safe_text
)
nestedgroup::CType_strategy = st.builds(
    nestedgroup::CType,
    cvalue=
        safe_text,
    cname=
        safe_text
)

@given(instance=nestedgroup::A_strategy)
@settings(max_examples=50)
def test_nestedgroup::a_instantiation(instance):
    assert isinstance(instance, nestedgroup::A)

@given(instance=nestedgroup::A_strategy)
def test_nestedgroup::a_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=nestedgroup::A_strategy)
def test_nestedgroup::a_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=nestedgroup::A_strategy)
def test_nestedgroup::a_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=nestedgroup::A_strategy)
def test_nestedgroup::a_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=nestedgroup::A_strategy)
def test_nestedgroup::a_b_type(instance):
    assert isinstance(instance.b, str)


@given(instance=nestedgroup::A_strategy)
def test_nestedgroup::a_b_setter(instance):
    original = instance.b
    instance.b = original
    assert instance.b == original

@given(instance=nestedgroup::Element_strategy)
@settings(max_examples=50)
def test_nestedgroup::element_instantiation(instance):
    assert isinstance(instance, nestedgroup::Element)

@given(instance=nestedgroup::Element_strategy)
def test_nestedgroup::element_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=nestedgroup::Element_strategy)
def test_nestedgroup::element_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=nestedgroup::Element_strategy)
def test_nestedgroup::element_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=nestedgroup::Element_strategy)
def test_nestedgroup::element_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=nestedgroup::Element_strategy)
def test_nestedgroup::element_true_type(instance):
    assert isinstance(instance.true, str)


@given(instance=nestedgroup::Element_strategy)
def test_nestedgroup::element_true_setter(instance):
    original = instance.true
    instance.true = original
    assert instance.true == original

@given(instance=nestedgroup::CType_strategy)
@settings(max_examples=50)
def test_nestedgroup::ctype_instantiation(instance):
    assert isinstance(instance, nestedgroup::CType)

@given(instance=nestedgroup::CType_strategy)
def test_nestedgroup::ctype_cvalue_type(instance):
    assert isinstance(instance.cvalue, str)


@given(instance=nestedgroup::CType_strategy)
def test_nestedgroup::ctype_cvalue_setter(instance):
    original = instance.cvalue
    instance.cvalue = original
    assert instance.cvalue == original

@given(instance=nestedgroup::CType_strategy)
def test_nestedgroup::ctype_cname_type(instance):
    assert isinstance(instance.cname, str)


@given(instance=nestedgroup::CType_strategy)
def test_nestedgroup::ctype_cname_setter(instance):
    original = instance.cname
    instance.cname = original
    assert instance.cname == original
