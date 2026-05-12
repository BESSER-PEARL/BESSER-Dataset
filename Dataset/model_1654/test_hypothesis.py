import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    yyaa_Alias,
    yyaa_NamedElement,
    NamedElement,
    yyaa_RelatedTo,
    yyaa_Thing,
    yyaa_World,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_yyaa_alias_is_not_abstract():
    assert not inspect.isabstract(yyaa_Alias)


def test_yyaa_alias_constructor_exists():
    assert callable(yyaa_Alias.__init__)


def test_yyaa_alias_constructor_args():
    sig = inspect.signature(yyaa_Alias.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_yyaa_alias_has_id():
    assert hasattr(yyaa_Alias, "id")
    descriptor = None
    for klass in yyaa_Alias.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_yyaa_namedelement_is_not_abstract():
    assert not inspect.isabstract(yyaa_NamedElement)


def test_yyaa_namedelement_constructor_exists():
    assert callable(yyaa_NamedElement.__init__)


def test_yyaa_namedelement_constructor_args():
    sig = inspect.signature(yyaa_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_yyaa_namedelement_has_name():
    assert hasattr(yyaa_NamedElement, "name")
    descriptor = None
    for klass in yyaa_NamedElement.__mro__:
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



def test_yyaa_relatedto_is_not_abstract():
    assert not inspect.isabstract(yyaa_RelatedTo)


def test_yyaa_relatedto_constructor_exists():
    assert callable(yyaa_RelatedTo.__init__)


def test_yyaa_relatedto_constructor_args():
    sig = inspect.signature(yyaa_RelatedTo.__init__)
    params = list(sig.parameters.keys())
    assert "since" in params, "Missing parameter 'since'"

def test_yyaa_relatedto_has_since():
    assert hasattr(yyaa_RelatedTo, "since")
    descriptor = None
    for klass in yyaa_RelatedTo.__mro__:
        if "since" in klass.__dict__:
            descriptor = klass.__dict__["since"]
            break
    assert isinstance(descriptor, property)



def test_yyaa_thing_is_not_abstract():
    assert not inspect.isabstract(yyaa_Thing)


def test_yyaa_thing_constructor_exists():
    assert callable(yyaa_Thing.__init__)


def test_yyaa_thing_constructor_args():
    sig = inspect.signature(yyaa_Thing.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_yyaa_thing_has_id():
    assert hasattr(yyaa_Thing, "id")
    descriptor = None
    for klass in yyaa_Thing.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_yyaa_world_is_not_abstract():
    assert not inspect.isabstract(yyaa_World)


def test_yyaa_world_constructor_exists():
    assert callable(yyaa_World.__init__)


def test_yyaa_world_constructor_args():
    sig = inspect.signature(yyaa_World.__init__)
    params = list(sig.parameters.keys())


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
yyaa_Alias_strategy = st.builds(
    yyaa_Alias,
    id=
        safe_text
)
yyaa_NamedElement_strategy = st.builds(
    yyaa_NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
yyaa_RelatedTo_strategy = st.builds(
    yyaa_RelatedTo,
    since=
        safe_text
)
yyaa_Thing_strategy = st.builds(
    yyaa_Thing,
    id=
        st.integers()
)
yyaa_World_strategy = st.builds(
    yyaa_World,
)

@given(instance=yyaa_Alias_strategy)
@settings(max_examples=50)
def test_yyaa_alias_instantiation(instance):
    assert isinstance(instance, yyaa_Alias)



@given(instance=yyaa_Alias_strategy)
def test_yyaa_alias_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=yyaa_NamedElement_strategy)
@settings(max_examples=50)
def test_yyaa_namedelement_instantiation(instance):
    assert isinstance(instance, yyaa_NamedElement)



@given(instance=yyaa_NamedElement_strategy)
def test_yyaa_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=yyaa_RelatedTo_strategy)
@settings(max_examples=50)
def test_yyaa_relatedto_instantiation(instance):
    assert isinstance(instance, yyaa_RelatedTo)



@given(instance=yyaa_RelatedTo_strategy)
def test_yyaa_relatedto_since_setter(instance):
    original = instance.since
    instance.since = original
    assert instance.since == original

@given(instance=yyaa_Thing_strategy)
@settings(max_examples=50)
def test_yyaa_thing_instantiation(instance):
    assert isinstance(instance, yyaa_Thing)



@given(instance=yyaa_Thing_strategy)
def test_yyaa_thing_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=yyaa_World_strategy)
@settings(max_examples=50)
def test_yyaa_world_instantiation(instance):
    assert isinstance(instance, yyaa_World)
