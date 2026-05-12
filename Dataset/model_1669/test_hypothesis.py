import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    yyb_Alias,
    yyb_NamedElement,
    NamedElement,
    yyb_RelatedTo,
    yyb_Thing,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_yyb_alias_is_not_abstract():
    assert not inspect.isabstract(yyb_Alias)


def test_yyb_alias_constructor_exists():
    assert callable(yyb_Alias.__init__)


def test_yyb_alias_constructor_args():
    sig = inspect.signature(yyb_Alias.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_yyb_alias_has_id():
    assert hasattr(yyb_Alias, "id")
    descriptor = None
    for klass in yyb_Alias.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_yyb_namedelement_is_not_abstract():
    assert not inspect.isabstract(yyb_NamedElement)


def test_yyb_namedelement_constructor_exists():
    assert callable(yyb_NamedElement.__init__)


def test_yyb_namedelement_constructor_args():
    sig = inspect.signature(yyb_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_yyb_namedelement_has_name():
    assert hasattr(yyb_NamedElement, "name")
    descriptor = None
    for klass in yyb_NamedElement.__mro__:
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



def test_yyb_relatedto_is_not_abstract():
    assert not inspect.isabstract(yyb_RelatedTo)


def test_yyb_relatedto_constructor_exists():
    assert callable(yyb_RelatedTo.__init__)


def test_yyb_relatedto_constructor_args():
    sig = inspect.signature(yyb_RelatedTo.__init__)
    params = list(sig.parameters.keys())
    assert "since" in params, "Missing parameter 'since'"

def test_yyb_relatedto_has_since():
    assert hasattr(yyb_RelatedTo, "since")
    descriptor = None
    for klass in yyb_RelatedTo.__mro__:
        if "since" in klass.__dict__:
            descriptor = klass.__dict__["since"]
            break
    assert isinstance(descriptor, property)



def test_yyb_thing_is_not_abstract():
    assert not inspect.isabstract(yyb_Thing)


def test_yyb_thing_constructor_exists():
    assert callable(yyb_Thing.__init__)


def test_yyb_thing_constructor_args():
    sig = inspect.signature(yyb_Thing.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_yyb_thing_has_id():
    assert hasattr(yyb_Thing, "id")
    descriptor = None
    for klass in yyb_Thing.__mro__:
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
yyb_Alias_strategy = st.builds(
    yyb_Alias,
    id=
        safe_text
)
yyb_NamedElement_strategy = st.builds(
    yyb_NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
yyb_RelatedTo_strategy = st.builds(
    yyb_RelatedTo,
    since=
        safe_text
)
yyb_Thing_strategy = st.builds(
    yyb_Thing,
    id=
        st.integers()
)

@given(instance=yyb_Alias_strategy)
@settings(max_examples=50)
def test_yyb_alias_instantiation(instance):
    assert isinstance(instance, yyb_Alias)



@given(instance=yyb_Alias_strategy)
def test_yyb_alias_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=yyb_NamedElement_strategy)
@settings(max_examples=50)
def test_yyb_namedelement_instantiation(instance):
    assert isinstance(instance, yyb_NamedElement)



@given(instance=yyb_NamedElement_strategy)
def test_yyb_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=yyb_RelatedTo_strategy)
@settings(max_examples=50)
def test_yyb_relatedto_instantiation(instance):
    assert isinstance(instance, yyb_RelatedTo)



@given(instance=yyb_RelatedTo_strategy)
def test_yyb_relatedto_since_setter(instance):
    original = instance.since
    instance.since = original
    assert instance.since == original

@given(instance=yyb_Thing_strategy)
@settings(max_examples=50)
def test_yyb_thing_instantiation(instance):
    assert isinstance(instance, yyb_Thing)



@given(instance=yyb_Thing_strategy)
def test_yyb_thing_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
