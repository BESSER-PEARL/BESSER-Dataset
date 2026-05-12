import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    simpleworld_World,
    simpleworld_NamedElement,
    NamedElement,
    simpleworld_RelatedTo,
    simpleworld_Thing,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_simpleworld_world_is_not_abstract():
    assert not inspect.isabstract(simpleworld_World)


def test_simpleworld_world_constructor_exists():
    assert callable(simpleworld_World.__init__)


def test_simpleworld_world_constructor_args():
    sig = inspect.signature(simpleworld_World.__init__)
    params = list(sig.parameters.keys())



def test_simpleworld_namedelement_is_not_abstract():
    assert not inspect.isabstract(simpleworld_NamedElement)


def test_simpleworld_namedelement_constructor_exists():
    assert callable(simpleworld_NamedElement.__init__)


def test_simpleworld_namedelement_constructor_args():
    sig = inspect.signature(simpleworld_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simpleworld_namedelement_has_name():
    assert hasattr(simpleworld_NamedElement, "name")
    descriptor = None
    for klass in simpleworld_NamedElement.__mro__:
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



def test_simpleworld_relatedto_is_not_abstract():
    assert not inspect.isabstract(simpleworld_RelatedTo)


def test_simpleworld_relatedto_constructor_exists():
    assert callable(simpleworld_RelatedTo.__init__)


def test_simpleworld_relatedto_constructor_args():
    sig = inspect.signature(simpleworld_RelatedTo.__init__)
    params = list(sig.parameters.keys())
    assert "since" in params, "Missing parameter 'since'"

def test_simpleworld_relatedto_has_since():
    assert hasattr(simpleworld_RelatedTo, "since")
    descriptor = None
    for klass in simpleworld_RelatedTo.__mro__:
        if "since" in klass.__dict__:
            descriptor = klass.__dict__["since"]
            break
    assert isinstance(descriptor, property)



def test_simpleworld_thing_is_not_abstract():
    assert not inspect.isabstract(simpleworld_Thing)


def test_simpleworld_thing_constructor_exists():
    assert callable(simpleworld_Thing.__init__)


def test_simpleworld_thing_constructor_args():
    sig = inspect.signature(simpleworld_Thing.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_simpleworld_thing_has_id():
    assert hasattr(simpleworld_Thing, "id")
    descriptor = None
    for klass in simpleworld_Thing.__mro__:
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
simpleworld_World_strategy = st.builds(
    simpleworld_World,
)
simpleworld_NamedElement_strategy = st.builds(
    simpleworld_NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
simpleworld_RelatedTo_strategy = st.builds(
    simpleworld_RelatedTo,
    since=
        safe_text
)
simpleworld_Thing_strategy = st.builds(
    simpleworld_Thing,
    id=
        st.integers()
)

@given(instance=simpleworld_World_strategy)
@settings(max_examples=50)
def test_simpleworld_world_instantiation(instance):
    assert isinstance(instance, simpleworld_World)

@given(instance=simpleworld_NamedElement_strategy)
@settings(max_examples=50)
def test_simpleworld_namedelement_instantiation(instance):
    assert isinstance(instance, simpleworld_NamedElement)



@given(instance=simpleworld_NamedElement_strategy)
def test_simpleworld_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=simpleworld_RelatedTo_strategy)
@settings(max_examples=50)
def test_simpleworld_relatedto_instantiation(instance):
    assert isinstance(instance, simpleworld_RelatedTo)



@given(instance=simpleworld_RelatedTo_strategy)
def test_simpleworld_relatedto_since_setter(instance):
    original = instance.since
    instance.since = original
    assert instance.since == original

@given(instance=simpleworld_Thing_strategy)
@settings(max_examples=50)
def test_simpleworld_thing_instantiation(instance):
    assert isinstance(instance, simpleworld_Thing)



@given(instance=simpleworld_Thing_strategy)
def test_simpleworld_thing_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
