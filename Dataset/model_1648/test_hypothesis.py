import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    visualworld::NamedElement,
    NamedElement,
    visualworld::RelatedTo,
    visualworld::Thing,
    visualworld::World,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_visualworld::namedelement_is_not_abstract():
    assert not inspect.isabstract(visualworld::NamedElement)


def test_visualworld::namedelement_constructor_exists():
    assert callable(visualworld::NamedElement.__init__)


def test_visualworld::namedelement_constructor_args():
    sig = inspect.signature(visualworld::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_visualworld::namedelement_has_name():
    assert hasattr(visualworld::NamedElement, "name")
    descriptor = None
    for klass in visualworld::NamedElement.__mro__:
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



def test_visualworld::relatedto_is_not_abstract():
    assert not inspect.isabstract(visualworld::RelatedTo)


def test_visualworld::relatedto_constructor_exists():
    assert callable(visualworld::RelatedTo.__init__)


def test_visualworld::relatedto_constructor_args():
    sig = inspect.signature(visualworld::RelatedTo.__init__)
    params = list(sig.parameters.keys())
    assert "since" in params, "Missing parameter 'since'"

def test_visualworld::relatedto_has_since():
    assert hasattr(visualworld::RelatedTo, "since")
    descriptor = None
    for klass in visualworld::RelatedTo.__mro__:
        if "since" in klass.__dict__:
            descriptor = klass.__dict__["since"]
            break
    assert isinstance(descriptor, property)



def test_visualworld::thing_is_not_abstract():
    assert not inspect.isabstract(visualworld::Thing)


def test_visualworld::thing_constructor_exists():
    assert callable(visualworld::Thing.__init__)


def test_visualworld::thing_constructor_args():
    sig = inspect.signature(visualworld::Thing.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_visualworld::thing_has_id():
    assert hasattr(visualworld::Thing, "id")
    descriptor = None
    for klass in visualworld::Thing.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_visualworld::world_is_not_abstract():
    assert not inspect.isabstract(visualworld::World)


def test_visualworld::world_constructor_exists():
    assert callable(visualworld::World.__init__)


def test_visualworld::world_constructor_args():
    sig = inspect.signature(visualworld::World.__init__)
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
visualworld::NamedElement_strategy = st.builds(
    visualworld::NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
visualworld::RelatedTo_strategy = st.builds(
    visualworld::RelatedTo,
    since=
        safe_text
)
visualworld::Thing_strategy = st.builds(
    visualworld::Thing,
    id=
        st.integers()
)
visualworld::World_strategy = st.builds(
    visualworld::World,
)

@given(instance=visualworld::NamedElement_strategy)
@settings(max_examples=50)
def test_visualworld::namedelement_instantiation(instance):
    assert isinstance(instance, visualworld::NamedElement)

@given(instance=visualworld::NamedElement_strategy)
def test_visualworld::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=visualworld::NamedElement_strategy)
def test_visualworld::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=visualworld::RelatedTo_strategy)
@settings(max_examples=50)
def test_visualworld::relatedto_instantiation(instance):
    assert isinstance(instance, visualworld::RelatedTo)

@given(instance=visualworld::RelatedTo_strategy)
def test_visualworld::relatedto_since_type(instance):
    assert isinstance(instance.since, str)


@given(instance=visualworld::RelatedTo_strategy)
def test_visualworld::relatedto_since_setter(instance):
    original = instance.since
    instance.since = original
    assert instance.since == original

@given(instance=visualworld::Thing_strategy)
@settings(max_examples=50)
def test_visualworld::thing_instantiation(instance):
    assert isinstance(instance, visualworld::Thing)

@given(instance=visualworld::Thing_strategy)
def test_visualworld::thing_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=visualworld::Thing_strategy)
def test_visualworld::thing_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=visualworld::World_strategy)
@settings(max_examples=50)
def test_visualworld::world_instantiation(instance):
    assert isinstance(instance, visualworld::World)
