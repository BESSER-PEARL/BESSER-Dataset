import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    nestedgroup_A,
    nestedgroup_Element,
    nestedgroup_CType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_nestedgroup_a_is_not_abstract():
    assert not inspect.isabstract(nestedgroup_A)


def test_nestedgroup_a_constructor_exists():
    assert callable(nestedgroup_A.__init__)


def test_nestedgroup_a_constructor_args():
    sig = inspect.signature(nestedgroup_A.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"
    assert "b" in params, "Missing parameter 'b'"
    assert "name" in params, "Missing parameter 'name'"

def test_nestedgroup_a_has_group():
    assert hasattr(nestedgroup_A, "group")
    descriptor = None
    for klass in nestedgroup_A.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_nestedgroup_a_has_b():
    assert hasattr(nestedgroup_A, "b")
    descriptor = None
    for klass in nestedgroup_A.__mro__:
        if "b" in klass.__dict__:
            descriptor = klass.__dict__["b"]
            break
    assert isinstance(descriptor, property)

def test_nestedgroup_a_has_name():
    assert hasattr(nestedgroup_A, "name")
    descriptor = None
    for klass in nestedgroup_A.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_nestedgroup_element_is_not_abstract():
    assert not inspect.isabstract(nestedgroup_Element)


def test_nestedgroup_element_constructor_exists():
    assert callable(nestedgroup_Element.__init__)


def test_nestedgroup_element_constructor_args():
    sig = inspect.signature(nestedgroup_Element.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "true" in params, "Missing parameter 'true'"
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_nestedgroup_element_has_name():
    assert hasattr(nestedgroup_Element, "name")
    descriptor = None
    for klass in nestedgroup_Element.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_nestedgroup_element_has_true():
    assert hasattr(nestedgroup_Element, "true")
    descriptor = None
    for klass in nestedgroup_Element.__mro__:
        if "true" in klass.__dict__:
            descriptor = klass.__dict__["true"]
            break
    assert isinstance(descriptor, property)

def test_nestedgroup_element_has_mixed():
    assert hasattr(nestedgroup_Element, "mixed")
    descriptor = None
    for klass in nestedgroup_Element.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_nestedgroup_ctype_is_not_abstract():
    assert not inspect.isabstract(nestedgroup_CType)


def test_nestedgroup_ctype_constructor_exists():
    assert callable(nestedgroup_CType.__init__)


def test_nestedgroup_ctype_constructor_args():
    sig = inspect.signature(nestedgroup_CType.__init__)
    params = list(sig.parameters.keys())
    assert "cvalue" in params, "Missing parameter 'cvalue'"
    assert "cname" in params, "Missing parameter 'cname'"

def test_nestedgroup_ctype_has_cvalue():
    assert hasattr(nestedgroup_CType, "cvalue")
    descriptor = None
    for klass in nestedgroup_CType.__mro__:
        if "cvalue" in klass.__dict__:
            descriptor = klass.__dict__["cvalue"]
            break
    assert isinstance(descriptor, property)

def test_nestedgroup_ctype_has_cname():
    assert hasattr(nestedgroup_CType, "cname")
    descriptor = None
    for klass in nestedgroup_CType.__mro__:
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
nestedgroup_A_strategy = st.builds(
    nestedgroup_A,
    group=
        safe_text,
    b=
        safe_text,
    name=
        safe_text
)
nestedgroup_Element_strategy = st.builds(
    nestedgroup_Element,
    name=
        safe_text,
    true=
        safe_text,
    mixed=
        safe_text
)
nestedgroup_CType_strategy = st.builds(
    nestedgroup_CType,
    cvalue=
        safe_text,
    cname=
        safe_text
)

@given(instance=nestedgroup_A_strategy)
@settings(max_examples=50)
def test_nestedgroup_a_instantiation(instance):
    assert isinstance(instance, nestedgroup_A)



@given(instance=nestedgroup_A_strategy)
def test_nestedgroup_a_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original



@given(instance=nestedgroup_A_strategy)
def test_nestedgroup_a_b_setter(instance):
    original = instance.b
    instance.b = original
    assert instance.b == original



@given(instance=nestedgroup_A_strategy)
def test_nestedgroup_a_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=nestedgroup_Element_strategy)
@settings(max_examples=50)
def test_nestedgroup_element_instantiation(instance):
    assert isinstance(instance, nestedgroup_Element)



@given(instance=nestedgroup_Element_strategy)
def test_nestedgroup_element_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=nestedgroup_Element_strategy)
def test_nestedgroup_element_true_setter(instance):
    original = instance.true
    instance.true = original
    assert instance.true == original



@given(instance=nestedgroup_Element_strategy)
def test_nestedgroup_element_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=nestedgroup_CType_strategy)
@settings(max_examples=50)
def test_nestedgroup_ctype_instantiation(instance):
    assert isinstance(instance, nestedgroup_CType)



@given(instance=nestedgroup_CType_strategy)
def test_nestedgroup_ctype_cvalue_setter(instance):
    original = instance.cvalue
    instance.cvalue = original
    assert instance.cvalue == original



@given(instance=nestedgroup_CType_strategy)
def test_nestedgroup_ctype_cname_setter(instance):
    original = instance.cname
    instance.cname = original
    assert instance.cname == original
