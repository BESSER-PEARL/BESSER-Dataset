import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    NamedElement,
    family::Family,
    family::NamedElement,
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



def test_family::family_is_not_abstract():
    assert not inspect.isabstract(family::Family)


def test_family::family_constructor_exists():
    assert callable(family::Family.__init__)


def test_family::family_constructor_args():
    sig = inspect.signature(family::Family.__init__)
    params = list(sig.parameters.keys())
    assert "mother" in params, "Missing parameter 'mother'"
    assert "children" in params, "Missing parameter 'children'"
    assert "father" in params, "Missing parameter 'father'"

def test_family::family_has_mother():
    assert hasattr(family::Family, "mother")
    descriptor = None
    for klass in family::Family.__mro__:
        if "mother" in klass.__dict__:
            descriptor = klass.__dict__["mother"]
            break
    assert isinstance(descriptor, property)

def test_family::family_has_children():
    assert hasattr(family::Family, "children")
    descriptor = None
    for klass in family::Family.__mro__:
        if "children" in klass.__dict__:
            descriptor = klass.__dict__["children"]
            break
    assert isinstance(descriptor, property)

def test_family::family_has_father():
    assert hasattr(family::Family, "father")
    descriptor = None
    for klass in family::Family.__mro__:
        if "father" in klass.__dict__:
            descriptor = klass.__dict__["father"]
            break
    assert isinstance(descriptor, property)



def test_family::namedelement_is_not_abstract():
    assert not inspect.isabstract(family::NamedElement)


def test_family::namedelement_constructor_exists():
    assert callable(family::NamedElement.__init__)


def test_family::namedelement_constructor_args():
    sig = inspect.signature(family::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_family::namedelement_has_name():
    assert hasattr(family::NamedElement, "name")
    descriptor = None
    for klass in family::NamedElement.__mro__:
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
family::Family_strategy = st.builds(
    family::Family,
    mother=
        safe_text,
    children=
        safe_text,
    father=
        safe_text
)
family::NamedElement_strategy = st.builds(
    family::NamedElement,
    name=
        safe_text
)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=family::Family_strategy)
@settings(max_examples=50)
def test_family::family_instantiation(instance):
    assert isinstance(instance, family::Family)

@given(instance=family::Family_strategy)
def test_family::family_mother_type(instance):
    assert isinstance(instance.mother, str)


@given(instance=family::Family_strategy)
def test_family::family_mother_setter(instance):
    original = instance.mother
    instance.mother = original
    assert instance.mother == original

@given(instance=family::Family_strategy)
def test_family::family_children_type(instance):
    assert isinstance(instance.children, str)


@given(instance=family::Family_strategy)
def test_family::family_children_setter(instance):
    original = instance.children
    instance.children = original
    assert instance.children == original

@given(instance=family::Family_strategy)
def test_family::family_father_type(instance):
    assert isinstance(instance.father, str)


@given(instance=family::Family_strategy)
def test_family::family_father_setter(instance):
    original = instance.father
    instance.father = original
    assert instance.father == original

@given(instance=family::NamedElement_strategy)
@settings(max_examples=50)
def test_family::namedelement_instantiation(instance):
    assert isinstance(instance, family::NamedElement)

@given(instance=family::NamedElement_strategy)
def test_family::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=family::NamedElement_strategy)
def test_family::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
