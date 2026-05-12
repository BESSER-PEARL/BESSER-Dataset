import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    yya_Alias,
    yya_NamedElement,
    NamedElement,
    yya_RelatedTo,
    yya_Thing,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_yya_alias_is_not_abstract():
    assert not inspect.isabstract(yya_Alias)


def test_yya_alias_constructor_exists():
    assert callable(yya_Alias.__init__)


def test_yya_alias_constructor_args():
    sig = inspect.signature(yya_Alias.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_yya_alias_has_id():
    assert hasattr(yya_Alias, "id")
    descriptor = None
    for klass in yya_Alias.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_yya_namedelement_is_not_abstract():
    assert not inspect.isabstract(yya_NamedElement)


def test_yya_namedelement_constructor_exists():
    assert callable(yya_NamedElement.__init__)


def test_yya_namedelement_constructor_args():
    sig = inspect.signature(yya_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_yya_namedelement_has_name():
    assert hasattr(yya_NamedElement, "name")
    descriptor = None
    for klass in yya_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_yya_relatedto_is_not_abstract():
    assert not inspect.isabstract(yya_RelatedTo)


def test_yya_relatedto_constructor_exists():
    assert callable(yya_RelatedTo.__init__)


def test_yya_relatedto_constructor_args():
    sig = inspect.signature(yya_RelatedTo.__init__)
    params = list(sig.parameters.keys())
    assert "since" in params, "Missing parameter 'since'"

def test_yya_relatedto_has_since():
    assert hasattr(yya_RelatedTo, "since")
    descriptor = None
    for klass in yya_RelatedTo.__mro__:
        if "since" in klass.__dict__:
            descriptor = klass.__dict__["since"]
            break
    assert isinstance(descriptor, property)



def test_yya_thing_is_not_abstract():
    assert not inspect.isabstract(yya_Thing)


def test_yya_thing_constructor_exists():
    assert callable(yya_Thing.__init__)


def test_yya_thing_constructor_args():
    sig = inspect.signature(yya_Thing.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_yya_thing_has_id():
    assert hasattr(yya_Thing, "id")
    descriptor = None
    for klass in yya_Thing.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
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
yya_Alias_strategy = st.builds(
    yya_Alias,
    id=
        safe_text
)
yya_NamedElement_strategy = st.builds(
    yya_NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
yya_RelatedTo_strategy = st.builds(
    yya_RelatedTo,
    since=
        safe_text
)
yya_Thing_strategy = st.builds(
    yya_Thing,
    id=
        st.integers()
)

@given(instance=yya_Alias_strategy)
@settings(max_examples=50)
def test_yya_alias_instantiation(instance):
    assert isinstance(instance, yya_Alias)



@given(instance=yya_Alias_strategy)
def test_yya_alias_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=yya_NamedElement_strategy)
@settings(max_examples=50)
def test_yya_namedelement_instantiation(instance):
    assert isinstance(instance, yya_NamedElement)



@given(instance=yya_NamedElement_strategy)
def test_yya_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=yya_RelatedTo_strategy)
@settings(max_examples=50)
def test_yya_relatedto_instantiation(instance):
    assert isinstance(instance, yya_RelatedTo)



@given(instance=yya_RelatedTo_strategy)
def test_yya_relatedto_since_setter(instance):
    original = instance.since
    instance.since = original
    assert instance.since == original

@given(instance=yya_Thing_strategy)
@settings(max_examples=50)
def test_yya_thing_instantiation(instance):
    assert isinstance(instance, yya_Thing)



@given(instance=yya_Thing_strategy)
def test_yya_thing_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
