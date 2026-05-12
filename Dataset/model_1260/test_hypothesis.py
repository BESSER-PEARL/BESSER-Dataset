import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    NamedElement,
    family_Family,
    family_NamedElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_family_family_is_not_abstract():
    assert not inspect.isabstract(family_Family)


def test_family_family_constructor_exists():
    assert callable(family_Family.__init__)


def test_family_family_constructor_args():
    sig = inspect.signature(family_Family.__init__)
    params = list(sig.parameters.keys())
    assert "father" in params, "Missing parameter 'father'"
    assert "mother" in params, "Missing parameter 'mother'"
    assert "children" in params, "Missing parameter 'children'"

def test_family_family_has_father():
    assert hasattr(family_Family, "father")
    descriptor = None
    for klass in family_Family.__mro__:
        if "father" in klass.__dict__:
            descriptor = klass.__dict__["father"]
            break
    assert isinstance(descriptor, property)

def test_family_family_has_mother():
    assert hasattr(family_Family, "mother")
    descriptor = None
    for klass in family_Family.__mro__:
        if "mother" in klass.__dict__:
            descriptor = klass.__dict__["mother"]
            break
    assert isinstance(descriptor, property)

def test_family_family_has_children():
    assert hasattr(family_Family, "children")
    descriptor = None
    for klass in family_Family.__mro__:
        if "children" in klass.__dict__:
            descriptor = klass.__dict__["children"]
            break
    assert isinstance(descriptor, property)



def test_family_namedelement_is_not_abstract():
    assert not inspect.isabstract(family_NamedElement)


def test_family_namedelement_constructor_exists():
    assert callable(family_NamedElement.__init__)


def test_family_namedelement_constructor_args():
    sig = inspect.signature(family_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_family_namedelement_has_name():
    assert hasattr(family_NamedElement, "name")
    descriptor = None
    for klass in family_NamedElement.__mro__:
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
NamedElement_strategy = st.builds(
    NamedElement,
)
family_Family_strategy = st.builds(
    family_Family,
    father=
        safe_text,
    mother=
        safe_text,
    children=
        safe_text
)
family_NamedElement_strategy = st.builds(
    family_NamedElement,
    name=
        safe_text
)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=family_Family_strategy)
@settings(max_examples=50)
def test_family_family_instantiation(instance):
    assert isinstance(instance, family_Family)



@given(instance=family_Family_strategy)
def test_family_family_father_setter(instance):
    original = instance.father
    instance.father = original
    assert instance.father == original



@given(instance=family_Family_strategy)
def test_family_family_mother_setter(instance):
    original = instance.mother
    instance.mother = original
    assert instance.mother == original



@given(instance=family_Family_strategy)
def test_family_family_children_setter(instance):
    original = instance.children
    instance.children = original
    assert instance.children == original

@given(instance=family_NamedElement_strategy)
@settings(max_examples=50)
def test_family_namedelement_instantiation(instance):
    assert isinstance(instance, family_NamedElement)



@given(instance=family_NamedElement_strategy)
def test_family_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
