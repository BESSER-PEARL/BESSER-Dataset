import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Named,
    simpleworld102::Part,
    simpleworld102::World,
    simpleworld102::Thing,
    simpleworld102::Element,
    simpleworld102::Relations,
    simpleworld102::Named,
    simpleworld102::Person,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_named_is_not_abstract():
    assert not inspect.isabstract(Named)


def test_named_constructor_exists():
    assert callable(Named.__init__)


def test_named_constructor_args():
    sig = inspect.signature(Named.__init__)
    params = list(sig.parameters.keys())



def test_simpleworld102::part_is_not_abstract():
    assert not inspect.isabstract(simpleworld102::Part)


def test_simpleworld102::part_constructor_exists():
    assert callable(simpleworld102::Part.__init__)


def test_simpleworld102::part_constructor_args():
    sig = inspect.signature(simpleworld102::Part.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "content" in params, "Missing parameter 'content'"

def test_simpleworld102::part_has_id():
    assert hasattr(simpleworld102::Part, "id")
    descriptor = None
    for klass in simpleworld102::Part.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_simpleworld102::part_has_content():
    assert hasattr(simpleworld102::Part, "content")
    descriptor = None
    for klass in simpleworld102::Part.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)



def test_simpleworld102::world_is_not_abstract():
    assert not inspect.isabstract(simpleworld102::World)


def test_simpleworld102::world_constructor_exists():
    assert callable(simpleworld102::World.__init__)


def test_simpleworld102::world_constructor_args():
    sig = inspect.signature(simpleworld102::World.__init__)
    params = list(sig.parameters.keys())



def test_simpleworld102::thing_is_not_abstract():
    assert not inspect.isabstract(simpleworld102::Thing)


def test_simpleworld102::thing_constructor_exists():
    assert callable(simpleworld102::Thing.__init__)


def test_simpleworld102::thing_constructor_args():
    sig = inspect.signature(simpleworld102::Thing.__init__)
    params = list(sig.parameters.keys())



def test_simpleworld102::element_is_not_abstract():
    assert not inspect.isabstract(simpleworld102::Element)


def test_simpleworld102::element_constructor_exists():
    assert callable(simpleworld102::Element.__init__)


def test_simpleworld102::element_constructor_args():
    sig = inspect.signature(simpleworld102::Element.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_simpleworld102::element_has_description():
    assert hasattr(simpleworld102::Element, "description")
    descriptor = None
    for klass in simpleworld102::Element.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_simpleworld102::relations_is_not_abstract():
    assert not inspect.isabstract(simpleworld102::Relations)


def test_simpleworld102::relations_constructor_exists():
    assert callable(simpleworld102::Relations.__init__)


def test_simpleworld102::relations_constructor_args():
    sig = inspect.signature(simpleworld102::Relations.__init__)
    params = list(sig.parameters.keys())
    assert "since" in params, "Missing parameter 'since'"

def test_simpleworld102::relations_has_since():
    assert hasattr(simpleworld102::Relations, "since")
    descriptor = None
    for klass in simpleworld102::Relations.__mro__:
        if "since" in klass.__dict__:
            descriptor = klass.__dict__["since"]
            break
    assert isinstance(descriptor, property)



def test_simpleworld102::named_is_not_abstract():
    assert not inspect.isabstract(simpleworld102::Named)


def test_simpleworld102::named_constructor_exists():
    assert callable(simpleworld102::Named.__init__)


def test_simpleworld102::named_constructor_args():
    sig = inspect.signature(simpleworld102::Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simpleworld102::named_has_name():
    assert hasattr(simpleworld102::Named, "name")
    descriptor = None
    for klass in simpleworld102::Named.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simpleworld102::person_is_not_abstract():
    assert not inspect.isabstract(simpleworld102::Person)


def test_simpleworld102::person_constructor_exists():
    assert callable(simpleworld102::Person.__init__)


def test_simpleworld102::person_constructor_args():
    sig = inspect.signature(simpleworld102::Person.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "foreName" in params, "Missing parameter 'foreName'"

def test_simpleworld102::person_has_name():
    assert hasattr(simpleworld102::Person, "name")
    descriptor = None
    for klass in simpleworld102::Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_simpleworld102::person_has_foreName():
    assert hasattr(simpleworld102::Person, "foreName")
    descriptor = None
    for klass in simpleworld102::Person.__mro__:
        if "foreName" in klass.__dict__:
            descriptor = klass.__dict__["foreName"]
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
Named_strategy = st.builds(
    Named,
)
simpleworld102::Part_strategy = st.builds(
    simpleworld102::Part,
    id=
        st.integers(),
    content=
        safe_text
)
simpleworld102::World_strategy = st.builds(
    simpleworld102::World,
)
simpleworld102::Thing_strategy = st.builds(
    simpleworld102::Thing,
)
simpleworld102::Element_strategy = st.builds(
    simpleworld102::Element,
    description=
        safe_text
)
simpleworld102::Relations_strategy = st.builds(
    simpleworld102::Relations,
    since=
        st.integers()
)
simpleworld102::Named_strategy = st.builds(
    simpleworld102::Named,
    name=
        safe_text
)
simpleworld102::Person_strategy = st.builds(
    simpleworld102::Person,
    name=
        safe_text,
    foreName=
        safe_text
)

@given(instance=Named_strategy)
@settings(max_examples=50)
def test_named_instantiation(instance):
    assert isinstance(instance, Named)

@given(instance=simpleworld102::Part_strategy)
@settings(max_examples=50)
def test_simpleworld102::part_instantiation(instance):
    assert isinstance(instance, simpleworld102::Part)

@given(instance=simpleworld102::Part_strategy)
def test_simpleworld102::part_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=simpleworld102::Part_strategy)
def test_simpleworld102::part_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=simpleworld102::Part_strategy)
def test_simpleworld102::part_content_type(instance):
    assert isinstance(instance.content, str)


@given(instance=simpleworld102::Part_strategy)
def test_simpleworld102::part_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original

@given(instance=simpleworld102::World_strategy)
@settings(max_examples=50)
def test_simpleworld102::world_instantiation(instance):
    assert isinstance(instance, simpleworld102::World)

@given(instance=simpleworld102::Thing_strategy)
@settings(max_examples=50)
def test_simpleworld102::thing_instantiation(instance):
    assert isinstance(instance, simpleworld102::Thing)

@given(instance=simpleworld102::Element_strategy)
@settings(max_examples=50)
def test_simpleworld102::element_instantiation(instance):
    assert isinstance(instance, simpleworld102::Element)

@given(instance=simpleworld102::Element_strategy)
def test_simpleworld102::element_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=simpleworld102::Element_strategy)
def test_simpleworld102::element_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=simpleworld102::Relations_strategy)
@settings(max_examples=50)
def test_simpleworld102::relations_instantiation(instance):
    assert isinstance(instance, simpleworld102::Relations)

@given(instance=simpleworld102::Relations_strategy)
def test_simpleworld102::relations_since_type(instance):
    assert isinstance(instance.since, int)


@given(instance=simpleworld102::Relations_strategy)
def test_simpleworld102::relations_since_setter(instance):
    original = instance.since
    instance.since = original
    assert instance.since == original

@given(instance=simpleworld102::Named_strategy)
@settings(max_examples=50)
def test_simpleworld102::named_instantiation(instance):
    assert isinstance(instance, simpleworld102::Named)

@given(instance=simpleworld102::Named_strategy)
def test_simpleworld102::named_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simpleworld102::Named_strategy)
def test_simpleworld102::named_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simpleworld102::Person_strategy)
@settings(max_examples=50)
def test_simpleworld102::person_instantiation(instance):
    assert isinstance(instance, simpleworld102::Person)

@given(instance=simpleworld102::Person_strategy)
def test_simpleworld102::person_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simpleworld102::Person_strategy)
def test_simpleworld102::person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simpleworld102::Person_strategy)
def test_simpleworld102::person_foreName_type(instance):
    assert isinstance(instance.foreName, str)


@given(instance=simpleworld102::Person_strategy)
def test_simpleworld102::person_foreName_setter(instance):
    original = instance.foreName
    instance.foreName = original
    assert instance.foreName == original
