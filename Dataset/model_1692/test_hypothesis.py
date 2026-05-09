import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    stuff::NamedElement,
    NamedElement,
    stuff::Baz,
    stuff::Bar,
    stuff::Thing,
    stuff::Foo,
    Thing,
    stuff::Stuff,
    stuff::World,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_stuff::namedelement_is_not_abstract():
    assert not inspect.isabstract(stuff::NamedElement)


def test_stuff::namedelement_constructor_exists():
    assert callable(stuff::NamedElement.__init__)


def test_stuff::namedelement_constructor_args():
    sig = inspect.signature(stuff::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_stuff::namedelement_has_name():
    assert hasattr(stuff::NamedElement, "name")
    descriptor = None
    for klass in stuff::NamedElement.__mro__:
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



def test_stuff::baz_is_not_abstract():
    assert not inspect.isabstract(stuff::Baz)


def test_stuff::baz_constructor_exists():
    assert callable(stuff::Baz.__init__)


def test_stuff::baz_constructor_args():
    sig = inspect.signature(stuff::Baz.__init__)
    params = list(sig.parameters.keys())



def test_stuff::bar_is_not_abstract():
    assert not inspect.isabstract(stuff::Bar)


def test_stuff::bar_constructor_exists():
    assert callable(stuff::Bar.__init__)


def test_stuff::bar_constructor_args():
    sig = inspect.signature(stuff::Bar.__init__)
    params = list(sig.parameters.keys())



def test_stuff::thing_is_not_abstract():
    assert not inspect.isabstract(stuff::Thing)


def test_stuff::thing_constructor_exists():
    assert callable(stuff::Thing.__init__)


def test_stuff::thing_constructor_args():
    sig = inspect.signature(stuff::Thing.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_stuff::thing_has_id():
    assert hasattr(stuff::Thing, "id")
    descriptor = None
    for klass in stuff::Thing.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_stuff::foo_is_not_abstract():
    assert not inspect.isabstract(stuff::Foo)


def test_stuff::foo_constructor_exists():
    assert callable(stuff::Foo.__init__)


def test_stuff::foo_constructor_args():
    sig = inspect.signature(stuff::Foo.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_stuff::foo_has_name():
    assert hasattr(stuff::Foo, "name")
    descriptor = None
    for klass in stuff::Foo.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_thing_is_not_abstract():
    assert not inspect.isabstract(Thing)


def test_thing_constructor_exists():
    assert callable(Thing.__init__)


def test_thing_constructor_args():
    sig = inspect.signature(Thing.__init__)
    params = list(sig.parameters.keys())



def test_stuff::stuff_is_not_abstract():
    assert not inspect.isabstract(stuff::Stuff)


def test_stuff::stuff_constructor_exists():
    assert callable(stuff::Stuff.__init__)


def test_stuff::stuff_constructor_args():
    sig = inspect.signature(stuff::Stuff.__init__)
    params = list(sig.parameters.keys())



def test_stuff::world_is_not_abstract():
    assert not inspect.isabstract(stuff::World)


def test_stuff::world_constructor_exists():
    assert callable(stuff::World.__init__)


def test_stuff::world_constructor_args():
    sig = inspect.signature(stuff::World.__init__)
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
stuff::NamedElement_strategy = st.builds(
    stuff::NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
stuff::Baz_strategy = st.builds(
    stuff::Baz,
)
stuff::Bar_strategy = st.builds(
    stuff::Bar,
)
stuff::Thing_strategy = st.builds(
    stuff::Thing,
    id=
        st.integers()
)
stuff::Foo_strategy = st.builds(
    stuff::Foo,
    name=
        safe_text
)
Thing_strategy = st.builds(
    Thing,
)
stuff::Stuff_strategy = st.builds(
    stuff::Stuff,
)
stuff::World_strategy = st.builds(
    stuff::World,
)

@given(instance=stuff::NamedElement_strategy)
@settings(max_examples=50)
def test_stuff::namedelement_instantiation(instance):
    assert isinstance(instance, stuff::NamedElement)

@given(instance=stuff::NamedElement_strategy)
def test_stuff::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=stuff::NamedElement_strategy)
def test_stuff::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=stuff::Baz_strategy)
@settings(max_examples=50)
def test_stuff::baz_instantiation(instance):
    assert isinstance(instance, stuff::Baz)

@given(instance=stuff::Bar_strategy)
@settings(max_examples=50)
def test_stuff::bar_instantiation(instance):
    assert isinstance(instance, stuff::Bar)

@given(instance=stuff::Thing_strategy)
@settings(max_examples=50)
def test_stuff::thing_instantiation(instance):
    assert isinstance(instance, stuff::Thing)

@given(instance=stuff::Thing_strategy)
def test_stuff::thing_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=stuff::Thing_strategy)
def test_stuff::thing_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=stuff::Foo_strategy)
@settings(max_examples=50)
def test_stuff::foo_instantiation(instance):
    assert isinstance(instance, stuff::Foo)

@given(instance=stuff::Foo_strategy)
def test_stuff::foo_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=stuff::Foo_strategy)
def test_stuff::foo_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Thing_strategy)
@settings(max_examples=50)
def test_thing_instantiation(instance):
    assert isinstance(instance, Thing)

@given(instance=stuff::Stuff_strategy)
@settings(max_examples=50)
def test_stuff::stuff_instantiation(instance):
    assert isinstance(instance, stuff::Stuff)

@given(instance=stuff::World_strategy)
@settings(max_examples=50)
def test_stuff::world_instantiation(instance):
    assert isinstance(instance, stuff::World)
