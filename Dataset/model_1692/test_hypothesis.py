import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    stuff_NamedElement,
    NamedElement,
    stuff_Baz,
    stuff_Bar,
    stuff_Thing,
    stuff_Foo,
    Thing,
    stuff_Stuff,
    stuff_World,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_stuff_namedelement_is_not_abstract():
    assert not inspect.isabstract(stuff_NamedElement)


def test_stuff_namedelement_constructor_exists():
    assert callable(stuff_NamedElement.__init__)


def test_stuff_namedelement_constructor_args():
    sig = inspect.signature(stuff_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_stuff_namedelement_has_name():
    assert hasattr(stuff_NamedElement, "name")
    descriptor = None
    for klass in stuff_NamedElement.__mro__:
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



def test_stuff_baz_is_not_abstract():
    assert not inspect.isabstract(stuff_Baz)


def test_stuff_baz_constructor_exists():
    assert callable(stuff_Baz.__init__)


def test_stuff_baz_constructor_args():
    sig = inspect.signature(stuff_Baz.__init__)
    params = list(sig.parameters.keys())



def test_stuff_bar_is_not_abstract():
    assert not inspect.isabstract(stuff_Bar)


def test_stuff_bar_constructor_exists():
    assert callable(stuff_Bar.__init__)


def test_stuff_bar_constructor_args():
    sig = inspect.signature(stuff_Bar.__init__)
    params = list(sig.parameters.keys())



def test_stuff_thing_is_not_abstract():
    assert not inspect.isabstract(stuff_Thing)


def test_stuff_thing_constructor_exists():
    assert callable(stuff_Thing.__init__)


def test_stuff_thing_constructor_args():
    sig = inspect.signature(stuff_Thing.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_stuff_thing_has_id():
    assert hasattr(stuff_Thing, "id")
    descriptor = None
    for klass in stuff_Thing.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_stuff_foo_is_not_abstract():
    assert not inspect.isabstract(stuff_Foo)


def test_stuff_foo_constructor_exists():
    assert callable(stuff_Foo.__init__)


def test_stuff_foo_constructor_args():
    sig = inspect.signature(stuff_Foo.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_stuff_foo_has_name():
    assert hasattr(stuff_Foo, "name")
    descriptor = None
    for klass in stuff_Foo.__mro__:
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



def test_stuff_stuff_is_not_abstract():
    assert not inspect.isabstract(stuff_Stuff)


def test_stuff_stuff_constructor_exists():
    assert callable(stuff_Stuff.__init__)


def test_stuff_stuff_constructor_args():
    sig = inspect.signature(stuff_Stuff.__init__)
    params = list(sig.parameters.keys())



def test_stuff_world_is_not_abstract():
    assert not inspect.isabstract(stuff_World)


def test_stuff_world_constructor_exists():
    assert callable(stuff_World.__init__)


def test_stuff_world_constructor_args():
    sig = inspect.signature(stuff_World.__init__)
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
stuff_NamedElement_strategy = st.builds(
    stuff_NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
stuff_Baz_strategy = st.builds(
    stuff_Baz,
)
stuff_Bar_strategy = st.builds(
    stuff_Bar,
)
stuff_Thing_strategy = st.builds(
    stuff_Thing,
    id=
        st.integers()
)
stuff_Foo_strategy = st.builds(
    stuff_Foo,
    name=
        safe_text
)
Thing_strategy = st.builds(
    Thing,
)
stuff_Stuff_strategy = st.builds(
    stuff_Stuff,
)
stuff_World_strategy = st.builds(
    stuff_World,
)

@given(instance=stuff_NamedElement_strategy)
@settings(max_examples=50)
def test_stuff_namedelement_instantiation(instance):
    assert isinstance(instance, stuff_NamedElement)



@given(instance=stuff_NamedElement_strategy)
def test_stuff_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=stuff_Baz_strategy)
@settings(max_examples=50)
def test_stuff_baz_instantiation(instance):
    assert isinstance(instance, stuff_Baz)

@given(instance=stuff_Bar_strategy)
@settings(max_examples=50)
def test_stuff_bar_instantiation(instance):
    assert isinstance(instance, stuff_Bar)

@given(instance=stuff_Thing_strategy)
@settings(max_examples=50)
def test_stuff_thing_instantiation(instance):
    assert isinstance(instance, stuff_Thing)



@given(instance=stuff_Thing_strategy)
def test_stuff_thing_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=stuff_Foo_strategy)
@settings(max_examples=50)
def test_stuff_foo_instantiation(instance):
    assert isinstance(instance, stuff_Foo)



@given(instance=stuff_Foo_strategy)
def test_stuff_foo_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Thing_strategy)
@settings(max_examples=50)
def test_thing_instantiation(instance):
    assert isinstance(instance, Thing)

@given(instance=stuff_Stuff_strategy)
@settings(max_examples=50)
def test_stuff_stuff_instantiation(instance):
    assert isinstance(instance, stuff_Stuff)

@given(instance=stuff_World_strategy)
@settings(max_examples=50)
def test_stuff_world_instantiation(instance):
    assert isinstance(instance, stuff_World)
