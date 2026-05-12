import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    error4_NamedElement,
    error4_World,
    NamedElement,
    error4_Component,
    error4_RelatedTo,
    error4_Thing,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_error4_namedelement_is_not_abstract():
    assert not inspect.isabstract(error4_NamedElement)


def test_error4_namedelement_constructor_exists():
    assert callable(error4_NamedElement.__init__)


def test_error4_namedelement_constructor_args():
    sig = inspect.signature(error4_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_error4_namedelement_has_name():
    assert hasattr(error4_NamedElement, "name")
    descriptor = None
    for klass in error4_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_error4_world_is_not_abstract():
    assert not inspect.isabstract(error4_World)


def test_error4_world_constructor_exists():
    assert callable(error4_World.__init__)


def test_error4_world_constructor_args():
    sig = inspect.signature(error4_World.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_error4_component_is_not_abstract():
    assert not inspect.isabstract(error4_Component)


def test_error4_component_constructor_exists():
    assert callable(error4_Component.__init__)


def test_error4_component_constructor_args():
    sig = inspect.signature(error4_Component.__init__)
    params = list(sig.parameters.keys())



def test_error4_relatedto_is_not_abstract():
    assert not inspect.isabstract(error4_RelatedTo)


def test_error4_relatedto_constructor_exists():
    assert callable(error4_RelatedTo.__init__)


def test_error4_relatedto_constructor_args():
    sig = inspect.signature(error4_RelatedTo.__init__)
    params = list(sig.parameters.keys())
    assert "since" in params, "Missing parameter 'since'"

def test_error4_relatedto_has_since():
    assert hasattr(error4_RelatedTo, "since")
    descriptor = None
    for klass in error4_RelatedTo.__mro__:
        if "since" in klass.__dict__:
            descriptor = klass.__dict__["since"]
            break
    assert isinstance(descriptor, property)



def test_error4_thing_is_not_abstract():
    assert not inspect.isabstract(error4_Thing)


def test_error4_thing_constructor_exists():
    assert callable(error4_Thing.__init__)


def test_error4_thing_constructor_args():
    sig = inspect.signature(error4_Thing.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_error4_thing_has_id():
    assert hasattr(error4_Thing, "id")
    descriptor = None
    for klass in error4_Thing.__mro__:
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
error4_NamedElement_strategy = st.builds(
    error4_NamedElement,
    name=
        safe_text
)
error4_World_strategy = st.builds(
    error4_World,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
error4_Component_strategy = st.builds(
    error4_Component,
)
error4_RelatedTo_strategy = st.builds(
    error4_RelatedTo,
    since=
        safe_text
)
error4_Thing_strategy = st.builds(
    error4_Thing,
    id=
        st.integers()
)

@given(instance=error4_NamedElement_strategy)
@settings(max_examples=50)
def test_error4_namedelement_instantiation(instance):
    assert isinstance(instance, error4_NamedElement)



@given(instance=error4_NamedElement_strategy)
def test_error4_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=error4_World_strategy)
@settings(max_examples=50)
def test_error4_world_instantiation(instance):
    assert isinstance(instance, error4_World)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=error4_Component_strategy)
@settings(max_examples=50)
def test_error4_component_instantiation(instance):
    assert isinstance(instance, error4_Component)

@given(instance=error4_RelatedTo_strategy)
@settings(max_examples=50)
def test_error4_relatedto_instantiation(instance):
    assert isinstance(instance, error4_RelatedTo)



@given(instance=error4_RelatedTo_strategy)
def test_error4_relatedto_since_setter(instance):
    original = instance.since
    instance.since = original
    assert instance.since == original

@given(instance=error4_Thing_strategy)
@settings(max_examples=50)
def test_error4_thing_instantiation(instance):
    assert isinstance(instance, error4_Thing)



@given(instance=error4_Thing_strategy)
def test_error4_thing_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
