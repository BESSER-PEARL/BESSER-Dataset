import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    unql::Select,
    unql::Connection,
    unql::Definition,
    unql::Program,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_unql::select_is_not_abstract():
    assert not inspect.isabstract(unql::Select)


def test_unql::select_constructor_exists():
    assert callable(unql::Select.__init__)


def test_unql::select_constructor_args():
    sig = inspect.signature(unql::Select.__init__)
    params = list(sig.parameters.keys())
    assert "attributes" in params, "Missing parameter 'attributes'"
    assert "relations" in params, "Missing parameter 'relations'"
    assert "conditions" in params, "Missing parameter 'conditions'"

def test_unql::select_has_attributes():
    assert hasattr(unql::Select, "attributes")
    descriptor = None
    for klass in unql::Select.__mro__:
        if "attributes" in klass.__dict__:
            descriptor = klass.__dict__["attributes"]
            break
    assert isinstance(descriptor, property)

def test_unql::select_has_relations():
    assert hasattr(unql::Select, "relations")
    descriptor = None
    for klass in unql::Select.__mro__:
        if "relations" in klass.__dict__:
            descriptor = klass.__dict__["relations"]
            break
    assert isinstance(descriptor, property)

def test_unql::select_has_conditions():
    assert hasattr(unql::Select, "conditions")
    descriptor = None
    for klass in unql::Select.__mro__:
        if "conditions" in klass.__dict__:
            descriptor = klass.__dict__["conditions"]
            break
    assert isinstance(descriptor, property)



def test_unql::connection_is_not_abstract():
    assert not inspect.isabstract(unql::Connection)


def test_unql::connection_constructor_exists():
    assert callable(unql::Connection.__init__)


def test_unql::connection_constructor_args():
    sig = inspect.signature(unql::Connection.__init__)
    params = list(sig.parameters.keys())
    assert "password" in params, "Missing parameter 'password'"
    assert "name" in params, "Missing parameter 'name'"
    assert "url" in params, "Missing parameter 'url'"
    assert "username" in params, "Missing parameter 'username'"

def test_unql::connection_has_password():
    assert hasattr(unql::Connection, "password")
    descriptor = None
    for klass in unql::Connection.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_unql::connection_has_name():
    assert hasattr(unql::Connection, "name")
    descriptor = None
    for klass in unql::Connection.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_unql::connection_has_url():
    assert hasattr(unql::Connection, "url")
    descriptor = None
    for klass in unql::Connection.__mro__:
        if "url" in klass.__dict__:
            descriptor = klass.__dict__["url"]
            break
    assert isinstance(descriptor, property)

def test_unql::connection_has_username():
    assert hasattr(unql::Connection, "username")
    descriptor = None
    for klass in unql::Connection.__mro__:
        if "username" in klass.__dict__:
            descriptor = klass.__dict__["username"]
            break
    assert isinstance(descriptor, property)



def test_unql::definition_is_not_abstract():
    assert not inspect.isabstract(unql::Definition)


def test_unql::definition_constructor_exists():
    assert callable(unql::Definition.__init__)


def test_unql::definition_constructor_args():
    sig = inspect.signature(unql::Definition.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_unql::definition_has_type():
    assert hasattr(unql::Definition, "type")
    descriptor = None
    for klass in unql::Definition.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_unql::definition_has_name():
    assert hasattr(unql::Definition, "name")
    descriptor = None
    for klass in unql::Definition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_unql::program_is_not_abstract():
    assert not inspect.isabstract(unql::Program)


def test_unql::program_constructor_exists():
    assert callable(unql::Program.__init__)


def test_unql::program_constructor_args():
    sig = inspect.signature(unql::Program.__init__)
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
unql::Select_strategy = st.builds(
    unql::Select,
    attributes=
        safe_text,
    relations=
        safe_text,
    conditions=
        safe_text
)
unql::Connection_strategy = st.builds(
    unql::Connection,
    password=
        safe_text,
    name=
        safe_text,
    url=
        safe_text,
    username=
        safe_text
)
unql::Definition_strategy = st.builds(
    unql::Definition,
    type=
        safe_text,
    name=
        safe_text
)
unql::Program_strategy = st.builds(
    unql::Program,
)

@given(instance=unql::Select_strategy)
@settings(max_examples=50)
def test_unql::select_instantiation(instance):
    assert isinstance(instance, unql::Select)

@given(instance=unql::Select_strategy)
def test_unql::select_attributes_type(instance):
    assert isinstance(instance.attributes, str)


@given(instance=unql::Select_strategy)
def test_unql::select_attributes_setter(instance):
    original = instance.attributes
    instance.attributes = original
    assert instance.attributes == original

@given(instance=unql::Select_strategy)
def test_unql::select_relations_type(instance):
    assert isinstance(instance.relations, str)


@given(instance=unql::Select_strategy)
def test_unql::select_relations_setter(instance):
    original = instance.relations
    instance.relations = original
    assert instance.relations == original

@given(instance=unql::Select_strategy)
def test_unql::select_conditions_type(instance):
    assert isinstance(instance.conditions, str)


@given(instance=unql::Select_strategy)
def test_unql::select_conditions_setter(instance):
    original = instance.conditions
    instance.conditions = original
    assert instance.conditions == original

@given(instance=unql::Connection_strategy)
@settings(max_examples=50)
def test_unql::connection_instantiation(instance):
    assert isinstance(instance, unql::Connection)

@given(instance=unql::Connection_strategy)
def test_unql::connection_password_type(instance):
    assert isinstance(instance.password, str)


@given(instance=unql::Connection_strategy)
def test_unql::connection_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original

@given(instance=unql::Connection_strategy)
def test_unql::connection_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=unql::Connection_strategy)
def test_unql::connection_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=unql::Connection_strategy)
def test_unql::connection_url_type(instance):
    assert isinstance(instance.url, str)


@given(instance=unql::Connection_strategy)
def test_unql::connection_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original

@given(instance=unql::Connection_strategy)
def test_unql::connection_username_type(instance):
    assert isinstance(instance.username, str)


@given(instance=unql::Connection_strategy)
def test_unql::connection_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original

@given(instance=unql::Definition_strategy)
@settings(max_examples=50)
def test_unql::definition_instantiation(instance):
    assert isinstance(instance, unql::Definition)

@given(instance=unql::Definition_strategy)
def test_unql::definition_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=unql::Definition_strategy)
def test_unql::definition_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=unql::Definition_strategy)
def test_unql::definition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=unql::Definition_strategy)
def test_unql::definition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=unql::Program_strategy)
@settings(max_examples=50)
def test_unql::program_instantiation(instance):
    assert isinstance(instance, unql::Program)
