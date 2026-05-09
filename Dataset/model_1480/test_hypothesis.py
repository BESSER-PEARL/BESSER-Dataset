import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Entity,
    graphmodel::Operation,
    graphmodel::Node,
    graphmodel::Property,
    graphmodel::Edge,
    graphmodel::Graph,
    graphmodel::Entity,
    graphmodel::ModellingType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_entity_is_not_abstract():
    assert not inspect.isabstract(Entity)


def test_entity_constructor_exists():
    assert callable(Entity.__init__)


def test_entity_constructor_args():
    sig = inspect.signature(Entity.__init__)
    params = list(sig.parameters.keys())



def test_graphmodel::operation_is_not_abstract():
    assert not inspect.isabstract(graphmodel::Operation)


def test_graphmodel::operation_constructor_exists():
    assert callable(graphmodel::Operation.__init__)


def test_graphmodel::operation_constructor_args():
    sig = inspect.signature(graphmodel::Operation.__init__)
    params = list(sig.parameters.keys())



def test_graphmodel::node_is_not_abstract():
    assert not inspect.isabstract(graphmodel::Node)


def test_graphmodel::node_constructor_exists():
    assert callable(graphmodel::Node.__init__)


def test_graphmodel::node_constructor_args():
    sig = inspect.signature(graphmodel::Node.__init__)
    params = list(sig.parameters.keys())



def test_graphmodel::property_is_not_abstract():
    assert not inspect.isabstract(graphmodel::Property)


def test_graphmodel::property_constructor_exists():
    assert callable(graphmodel::Property.__init__)


def test_graphmodel::property_constructor_args():
    sig = inspect.signature(graphmodel::Property.__init__)
    params = list(sig.parameters.keys())



def test_graphmodel::edge_is_not_abstract():
    assert not inspect.isabstract(graphmodel::Edge)


def test_graphmodel::edge_constructor_exists():
    assert callable(graphmodel::Edge.__init__)


def test_graphmodel::edge_constructor_args():
    sig = inspect.signature(graphmodel::Edge.__init__)
    params = list(sig.parameters.keys())



def test_graphmodel::graph_is_not_abstract():
    assert not inspect.isabstract(graphmodel::Graph)


def test_graphmodel::graph_constructor_exists():
    assert callable(graphmodel::Graph.__init__)


def test_graphmodel::graph_constructor_args():
    sig = inspect.signature(graphmodel::Graph.__init__)
    params = list(sig.parameters.keys())



def test_graphmodel::entity_is_not_abstract():
    assert not inspect.isabstract(graphmodel::Entity)


def test_graphmodel::entity_constructor_exists():
    assert callable(graphmodel::Entity.__init__)


def test_graphmodel::entity_constructor_args():
    sig = inspect.signature(graphmodel::Entity.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"
    assert "value" in params, "Missing parameter 'value'"
    assert "height" in params, "Missing parameter 'height'"
    assert "className" in params, "Missing parameter 'className'"
    assert "category" in params, "Missing parameter 'category'"
    assert "x" in params, "Missing parameter 'x'"
    assert "width" in params, "Missing parameter 'width'"
    assert "ID" in params, "Missing parameter 'ID'"
    assert "accessModifier" in params, "Missing parameter 'accessModifier'"
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"
    assert "type" in params, "Missing parameter 'type'"
    assert "group" in params, "Missing parameter 'group'"
    assert "y" in params, "Missing parameter 'y'"

def test_graphmodel::entity_has_text():
    assert hasattr(graphmodel::Entity, "text")
    descriptor = None
    for klass in graphmodel::Entity.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_graphmodel::entity_has_value():
    assert hasattr(graphmodel::Entity, "value")
    descriptor = None
    for klass in graphmodel::Entity.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_graphmodel::entity_has_height():
    assert hasattr(graphmodel::Entity, "height")
    descriptor = None
    for klass in graphmodel::Entity.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_graphmodel::entity_has_className():
    assert hasattr(graphmodel::Entity, "className")
    descriptor = None
    for klass in graphmodel::Entity.__mro__:
        if "className" in klass.__dict__:
            descriptor = klass.__dict__["className"]
            break
    assert isinstance(descriptor, property)

def test_graphmodel::entity_has_category():
    assert hasattr(graphmodel::Entity, "category")
    descriptor = None
    for klass in graphmodel::Entity.__mro__:
        if "category" in klass.__dict__:
            descriptor = klass.__dict__["category"]
            break
    assert isinstance(descriptor, property)

def test_graphmodel::entity_has_x():
    assert hasattr(graphmodel::Entity, "x")
    descriptor = None
    for klass in graphmodel::Entity.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_graphmodel::entity_has_width():
    assert hasattr(graphmodel::Entity, "width")
    descriptor = None
    for klass in graphmodel::Entity.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_graphmodel::entity_has_ID():
    assert hasattr(graphmodel::Entity, "ID")
    descriptor = None
    for klass in graphmodel::Entity.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)

def test_graphmodel::entity_has_accessModifier():
    assert hasattr(graphmodel::Entity, "accessModifier")
    descriptor = None
    for klass in graphmodel::Entity.__mro__:
        if "accessModifier" in klass.__dict__:
            descriptor = klass.__dict__["accessModifier"]
            break
    assert isinstance(descriptor, property)

def test_graphmodel::entity_has_name():
    assert hasattr(graphmodel::Entity, "name")
    descriptor = None
    for klass in graphmodel::Entity.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_graphmodel::entity_has_description():
    assert hasattr(graphmodel::Entity, "description")
    descriptor = None
    for klass in graphmodel::Entity.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_graphmodel::entity_has_type():
    assert hasattr(graphmodel::Entity, "type")
    descriptor = None
    for klass in graphmodel::Entity.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_graphmodel::entity_has_group():
    assert hasattr(graphmodel::Entity, "group")
    descriptor = None
    for klass in graphmodel::Entity.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_graphmodel::entity_has_y():
    assert hasattr(graphmodel::Entity, "y")
    descriptor = None
    for klass in graphmodel::Entity.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)



def test_graphmodel::modellingtype_is_not_abstract():
    assert not inspect.isabstract(graphmodel::ModellingType)


def test_graphmodel::modellingtype_constructor_exists():
    assert callable(graphmodel::ModellingType.__init__)


def test_graphmodel::modellingtype_constructor_args():
    sig = inspect.signature(graphmodel::ModellingType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_graphmodel::modellingtype_has_name():
    assert hasattr(graphmodel::ModellingType, "name")
    descriptor = None
    for klass in graphmodel::ModellingType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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
Entity_strategy = st.builds(
    Entity,
)
graphmodel::Operation_strategy = st.builds(
    graphmodel::Operation,
)
graphmodel::Node_strategy = st.builds(
    graphmodel::Node,
)
graphmodel::Property_strategy = st.builds(
    graphmodel::Property,
)
graphmodel::Edge_strategy = st.builds(
    graphmodel::Edge,
)
graphmodel::Graph_strategy = st.builds(
    graphmodel::Graph,
)
graphmodel::Entity_strategy = st.builds(
    graphmodel::Entity,
    text=
        safe_text,
    value=
        safe_text,
    height=
        safe_text,
    className=
        safe_text,
    category=
        safe_text,
    x=
        safe_text,
    width=
        safe_text,
    ID=
        safe_text,
    accessModifier=
        safe_text,
    name=
        safe_text,
    description=
        safe_text,
    type=
        safe_text,
    group=
        safe_text,
    y=
        safe_text
)
graphmodel::ModellingType_strategy = st.builds(
    graphmodel::ModellingType,
    name=
        safe_text
)

@given(instance=Entity_strategy)
@settings(max_examples=50)
def test_entity_instantiation(instance):
    assert isinstance(instance, Entity)

@given(instance=graphmodel::Operation_strategy)
@settings(max_examples=50)
def test_graphmodel::operation_instantiation(instance):
    assert isinstance(instance, graphmodel::Operation)

@given(instance=graphmodel::Node_strategy)
@settings(max_examples=50)
def test_graphmodel::node_instantiation(instance):
    assert isinstance(instance, graphmodel::Node)

@given(instance=graphmodel::Property_strategy)
@settings(max_examples=50)
def test_graphmodel::property_instantiation(instance):
    assert isinstance(instance, graphmodel::Property)

@given(instance=graphmodel::Edge_strategy)
@settings(max_examples=50)
def test_graphmodel::edge_instantiation(instance):
    assert isinstance(instance, graphmodel::Edge)

@given(instance=graphmodel::Graph_strategy)
@settings(max_examples=50)
def test_graphmodel::graph_instantiation(instance):
    assert isinstance(instance, graphmodel::Graph)

@given(instance=graphmodel::Entity_strategy)
@settings(max_examples=50)
def test_graphmodel::entity_instantiation(instance):
    assert isinstance(instance, graphmodel::Entity)

@given(instance=graphmodel::Entity_strategy)
def test_graphmodel::entity_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=graphmodel::Entity_strategy)
def test_graphmodel::entity_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=graphmodel::Entity_strategy)
def test_graphmodel::entity_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=graphmodel::Entity_strategy)
def test_graphmodel::entity_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=graphmodel::Entity_strategy)
def test_graphmodel::entity_height_type(instance):
    assert isinstance(instance.height, str)


@given(instance=graphmodel::Entity_strategy)
def test_graphmodel::entity_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=graphmodel::Entity_strategy)
def test_graphmodel::entity_className_type(instance):
    assert isinstance(instance.className, str)


@given(instance=graphmodel::Entity_strategy)
def test_graphmodel::entity_className_setter(instance):
    original = instance.className
    instance.className = original
    assert instance.className == original

@given(instance=graphmodel::Entity_strategy)
def test_graphmodel::entity_category_type(instance):
    assert isinstance(instance.category, str)


@given(instance=graphmodel::Entity_strategy)
def test_graphmodel::entity_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original

@given(instance=graphmodel::Entity_strategy)
def test_graphmodel::entity_x_type(instance):
    assert isinstance(instance.x, str)


@given(instance=graphmodel::Entity_strategy)
def test_graphmodel::entity_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=graphmodel::Entity_strategy)
def test_graphmodel::entity_width_type(instance):
    assert isinstance(instance.width, str)


@given(instance=graphmodel::Entity_strategy)
def test_graphmodel::entity_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=graphmodel::Entity_strategy)
def test_graphmodel::entity_ID_type(instance):
    assert isinstance(instance.ID, str)


@given(instance=graphmodel::Entity_strategy)
def test_graphmodel::entity_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

@given(instance=graphmodel::Entity_strategy)
def test_graphmodel::entity_accessModifier_type(instance):
    assert isinstance(instance.accessModifier, str)


@given(instance=graphmodel::Entity_strategy)
def test_graphmodel::entity_accessModifier_setter(instance):
    original = instance.accessModifier
    instance.accessModifier = original
    assert instance.accessModifier == original

@given(instance=graphmodel::Entity_strategy)
def test_graphmodel::entity_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=graphmodel::Entity_strategy)
def test_graphmodel::entity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=graphmodel::Entity_strategy)
def test_graphmodel::entity_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=graphmodel::Entity_strategy)
def test_graphmodel::entity_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=graphmodel::Entity_strategy)
def test_graphmodel::entity_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=graphmodel::Entity_strategy)
def test_graphmodel::entity_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=graphmodel::Entity_strategy)
def test_graphmodel::entity_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=graphmodel::Entity_strategy)
def test_graphmodel::entity_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=graphmodel::Entity_strategy)
def test_graphmodel::entity_y_type(instance):
    assert isinstance(instance.y, str)


@given(instance=graphmodel::Entity_strategy)
def test_graphmodel::entity_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=graphmodel::ModellingType_strategy)
@settings(max_examples=50)
def test_graphmodel::modellingtype_instantiation(instance):
    assert isinstance(instance, graphmodel::ModellingType)

@given(instance=graphmodel::ModellingType_strategy)
def test_graphmodel::modellingtype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=graphmodel::ModellingType_strategy)
def test_graphmodel::modellingtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
