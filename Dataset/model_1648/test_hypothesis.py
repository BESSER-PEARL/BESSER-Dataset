import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    visualworld_NamedElement,
    NamedElement,
    visualworld_RelatedTo,
    visualworld_Thing,
    visualworld_World,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_visualworld_namedelement_is_not_abstract():
    assert not inspect.isabstract(visualworld_NamedElement)


def test_visualworld_namedelement_constructor_exists():
    assert callable(visualworld_NamedElement.__init__)


def test_visualworld_namedelement_constructor_args():
    sig = inspect.signature(visualworld_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_visualworld_namedelement_has_name():
    assert hasattr(visualworld_NamedElement, "name")
    descriptor = None
    for klass in visualworld_NamedElement.__mro__:
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



def test_visualworld_relatedto_is_not_abstract():
    assert not inspect.isabstract(visualworld_RelatedTo)


def test_visualworld_relatedto_constructor_exists():
    assert callable(visualworld_RelatedTo.__init__)


def test_visualworld_relatedto_constructor_args():
    sig = inspect.signature(visualworld_RelatedTo.__init__)
    params = list(sig.parameters.keys())
    assert "since" in params, "Missing parameter 'since'"

def test_visualworld_relatedto_has_since():
    assert hasattr(visualworld_RelatedTo, "since")
    descriptor = None
    for klass in visualworld_RelatedTo.__mro__:
        if "since" in klass.__dict__:
            descriptor = klass.__dict__["since"]
            break
    assert isinstance(descriptor, property)



def test_visualworld_thing_is_not_abstract():
    assert not inspect.isabstract(visualworld_Thing)


def test_visualworld_thing_constructor_exists():
    assert callable(visualworld_Thing.__init__)


def test_visualworld_thing_constructor_args():
    sig = inspect.signature(visualworld_Thing.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_visualworld_thing_has_id():
    assert hasattr(visualworld_Thing, "id")
    descriptor = None
    for klass in visualworld_Thing.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_visualworld_world_is_not_abstract():
    assert not inspect.isabstract(visualworld_World)


def test_visualworld_world_constructor_exists():
    assert callable(visualworld_World.__init__)


def test_visualworld_world_constructor_args():
    sig = inspect.signature(visualworld_World.__init__)
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
visualworld_NamedElement_strategy = st.builds(
    visualworld_NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
visualworld_RelatedTo_strategy = st.builds(
    visualworld_RelatedTo,
    since=
        safe_text
)
visualworld_Thing_strategy = st.builds(
    visualworld_Thing,
    id=
        st.integers()
)
visualworld_World_strategy = st.builds(
    visualworld_World,
)

@given(instance=visualworld_NamedElement_strategy)
@settings(max_examples=50)
def test_visualworld_namedelement_instantiation(instance):
    assert isinstance(instance, visualworld_NamedElement)



@given(instance=visualworld_NamedElement_strategy)
def test_visualworld_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=visualworld_RelatedTo_strategy)
@settings(max_examples=50)
def test_visualworld_relatedto_instantiation(instance):
    assert isinstance(instance, visualworld_RelatedTo)



@given(instance=visualworld_RelatedTo_strategy)
def test_visualworld_relatedto_since_setter(instance):
    original = instance.since
    instance.since = original
    assert instance.since == original

@given(instance=visualworld_Thing_strategy)
@settings(max_examples=50)
def test_visualworld_thing_instantiation(instance):
    assert isinstance(instance, visualworld_Thing)



@given(instance=visualworld_Thing_strategy)
def test_visualworld_thing_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=visualworld_World_strategy)
@settings(max_examples=50)
def test_visualworld_world_instantiation(instance):
    assert isinstance(instance, visualworld_World)
