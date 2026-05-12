import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    unql_Select,
    unql_Connection,
    unql_Definition,
    unql_Program,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_unql_select_is_not_abstract():
    assert not inspect.isabstract(unql_Select)


def test_unql_select_constructor_exists():
    assert callable(unql_Select.__init__)


def test_unql_select_constructor_args():
    sig = inspect.signature(unql_Select.__init__)
    params = list(sig.parameters.keys())
    assert "relations" in params, "Missing parameter 'relations'"
    assert "conditions" in params, "Missing parameter 'conditions'"
    assert "attributes" in params, "Missing parameter 'attributes'"

def test_unql_select_has_relations():
    assert hasattr(unql_Select, "relations")
    descriptor = None
    for klass in unql_Select.__mro__:
        if "relations" in klass.__dict__:
            descriptor = klass.__dict__["relations"]
            break
    assert isinstance(descriptor, property)

def test_unql_select_has_conditions():
    assert hasattr(unql_Select, "conditions")
    descriptor = None
    for klass in unql_Select.__mro__:
        if "conditions" in klass.__dict__:
            descriptor = klass.__dict__["conditions"]
            break
    assert isinstance(descriptor, property)

def test_unql_select_has_attributes():
    assert hasattr(unql_Select, "attributes")
    descriptor = None
    for klass in unql_Select.__mro__:
        if "attributes" in klass.__dict__:
            descriptor = klass.__dict__["attributes"]
            break
    assert isinstance(descriptor, property)



def test_unql_connection_is_not_abstract():
    assert not inspect.isabstract(unql_Connection)


def test_unql_connection_constructor_exists():
    assert callable(unql_Connection.__init__)


def test_unql_connection_constructor_args():
    sig = inspect.signature(unql_Connection.__init__)
    params = list(sig.parameters.keys())
    assert "url" in params, "Missing parameter 'url'"
    assert "username" in params, "Missing parameter 'username'"
    assert "password" in params, "Missing parameter 'password'"
    assert "name" in params, "Missing parameter 'name'"

def test_unql_connection_has_url():
    assert hasattr(unql_Connection, "url")
    descriptor = None
    for klass in unql_Connection.__mro__:
        if "url" in klass.__dict__:
            descriptor = klass.__dict__["url"]
            break
    assert isinstance(descriptor, property)

def test_unql_connection_has_username():
    assert hasattr(unql_Connection, "username")
    descriptor = None
    for klass in unql_Connection.__mro__:
        if "username" in klass.__dict__:
            descriptor = klass.__dict__["username"]
            break
    assert isinstance(descriptor, property)

def test_unql_connection_has_password():
    assert hasattr(unql_Connection, "password")
    descriptor = None
    for klass in unql_Connection.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_unql_connection_has_name():
    assert hasattr(unql_Connection, "name")
    descriptor = None
    for klass in unql_Connection.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_unql_definition_is_not_abstract():
    assert not inspect.isabstract(unql_Definition)


def test_unql_definition_constructor_exists():
    assert callable(unql_Definition.__init__)


def test_unql_definition_constructor_args():
    sig = inspect.signature(unql_Definition.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_unql_definition_has_type():
    assert hasattr(unql_Definition, "type")
    descriptor = None
    for klass in unql_Definition.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_unql_definition_has_name():
    assert hasattr(unql_Definition, "name")
    descriptor = None
    for klass in unql_Definition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_unql_program_is_not_abstract():
    assert not inspect.isabstract(unql_Program)


def test_unql_program_constructor_exists():
    assert callable(unql_Program.__init__)


def test_unql_program_constructor_args():
    sig = inspect.signature(unql_Program.__init__)
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
unql_Select_strategy = st.builds(
    unql_Select,
    relations=
        safe_text,
    conditions=
        safe_text,
    attributes=
        safe_text
)
unql_Connection_strategy = st.builds(
    unql_Connection,
    url=
        safe_text,
    username=
        safe_text,
    password=
        safe_text,
    name=
        safe_text
)
unql_Definition_strategy = st.builds(
    unql_Definition,
    type=
        safe_text,
    name=
        safe_text
)
unql_Program_strategy = st.builds(
    unql_Program,
)

@given(instance=unql_Select_strategy)
@settings(max_examples=50)
def test_unql_select_instantiation(instance):
    assert isinstance(instance, unql_Select)



@given(instance=unql_Select_strategy)
def test_unql_select_relations_setter(instance):
    original = instance.relations
    instance.relations = original
    assert instance.relations == original



@given(instance=unql_Select_strategy)
def test_unql_select_conditions_setter(instance):
    original = instance.conditions
    instance.conditions = original
    assert instance.conditions == original



@given(instance=unql_Select_strategy)
def test_unql_select_attributes_setter(instance):
    original = instance.attributes
    instance.attributes = original
    assert instance.attributes == original

@given(instance=unql_Connection_strategy)
@settings(max_examples=50)
def test_unql_connection_instantiation(instance):
    assert isinstance(instance, unql_Connection)



@given(instance=unql_Connection_strategy)
def test_unql_connection_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original



@given(instance=unql_Connection_strategy)
def test_unql_connection_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original



@given(instance=unql_Connection_strategy)
def test_unql_connection_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=unql_Connection_strategy)
def test_unql_connection_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=unql_Definition_strategy)
@settings(max_examples=50)
def test_unql_definition_instantiation(instance):
    assert isinstance(instance, unql_Definition)



@given(instance=unql_Definition_strategy)
def test_unql_definition_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=unql_Definition_strategy)
def test_unql_definition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=unql_Program_strategy)
@settings(max_examples=50)
def test_unql_program_instantiation(instance):
    assert isinstance(instance, unql_Program)
