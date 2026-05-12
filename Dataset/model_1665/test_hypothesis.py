import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    rel2rel_World,
    Thing,
    rel2rel_NamedElement,
    rel2rel_RelatedTo,
    NamedElement,
    rel2rel_Thing,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_rel2rel_world_is_not_abstract():
    assert not inspect.isabstract(rel2rel_World)


def test_rel2rel_world_constructor_exists():
    assert callable(rel2rel_World.__init__)


def test_rel2rel_world_constructor_args():
    sig = inspect.signature(rel2rel_World.__init__)
    params = list(sig.parameters.keys())



def test_thing_is_not_abstract():
    assert not inspect.isabstract(Thing)


def test_thing_constructor_exists():
    assert callable(Thing.__init__)


def test_thing_constructor_args():
    sig = inspect.signature(Thing.__init__)
    params = list(sig.parameters.keys())



def test_rel2rel_namedelement_is_not_abstract():
    assert not inspect.isabstract(rel2rel_NamedElement)


def test_rel2rel_namedelement_constructor_exists():
    assert callable(rel2rel_NamedElement.__init__)


def test_rel2rel_namedelement_constructor_args():
    sig = inspect.signature(rel2rel_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rel2rel_namedelement_has_name():
    assert hasattr(rel2rel_NamedElement, "name")
    descriptor = None
    for klass in rel2rel_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rel2rel_relatedto_is_not_abstract():
    assert not inspect.isabstract(rel2rel_RelatedTo)


def test_rel2rel_relatedto_constructor_exists():
    assert callable(rel2rel_RelatedTo.__init__)


def test_rel2rel_relatedto_constructor_args():
    sig = inspect.signature(rel2rel_RelatedTo.__init__)
    params = list(sig.parameters.keys())
    assert "since" in params, "Missing parameter 'since'"

def test_rel2rel_relatedto_has_since():
    assert hasattr(rel2rel_RelatedTo, "since")
    descriptor = None
    for klass in rel2rel_RelatedTo.__mro__:
        if "since" in klass.__dict__:
            descriptor = klass.__dict__["since"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_rel2rel_thing_is_not_abstract():
    assert not inspect.isabstract(rel2rel_Thing)


def test_rel2rel_thing_constructor_exists():
    assert callable(rel2rel_Thing.__init__)


def test_rel2rel_thing_constructor_args():
    sig = inspect.signature(rel2rel_Thing.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_rel2rel_thing_has_id():
    assert hasattr(rel2rel_Thing, "id")
    descriptor = None
    for klass in rel2rel_Thing.__mro__:
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
rel2rel_World_strategy = st.builds(
    rel2rel_World,
)
Thing_strategy = st.builds(
    Thing,
)
rel2rel_NamedElement_strategy = st.builds(
    rel2rel_NamedElement,
    name=
        safe_text
)
rel2rel_RelatedTo_strategy = st.builds(
    rel2rel_RelatedTo,
    since=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
rel2rel_Thing_strategy = st.builds(
    rel2rel_Thing,
    id=
        st.integers()
)

@given(instance=rel2rel_World_strategy)
@settings(max_examples=50)
def test_rel2rel_world_instantiation(instance):
    assert isinstance(instance, rel2rel_World)

@given(instance=Thing_strategy)
@settings(max_examples=50)
def test_thing_instantiation(instance):
    assert isinstance(instance, Thing)

@given(instance=rel2rel_NamedElement_strategy)
@settings(max_examples=50)
def test_rel2rel_namedelement_instantiation(instance):
    assert isinstance(instance, rel2rel_NamedElement)



@given(instance=rel2rel_NamedElement_strategy)
def test_rel2rel_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rel2rel_RelatedTo_strategy)
@settings(max_examples=50)
def test_rel2rel_relatedto_instantiation(instance):
    assert isinstance(instance, rel2rel_RelatedTo)



@given(instance=rel2rel_RelatedTo_strategy)
def test_rel2rel_relatedto_since_setter(instance):
    original = instance.since
    instance.since = original
    assert instance.since == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=rel2rel_Thing_strategy)
@settings(max_examples=50)
def test_rel2rel_thing_instantiation(instance):
    assert isinstance(instance, rel2rel_Thing)



@given(instance=rel2rel_Thing_strategy)
def test_rel2rel_thing_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
