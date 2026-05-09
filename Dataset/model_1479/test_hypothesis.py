import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Entity,
    graphmodelling::Edge,
    graphmodelling::Operation,
    graphmodelling::Property,
    graphmodelling::Node,
    graphmodelling::Graph,
    graphmodelling::Entity,
    graphmodelling::ModellingType,
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



def test_graphmodelling::edge_is_not_abstract():
    assert not inspect.isabstract(graphmodelling::Edge)


def test_graphmodelling::edge_constructor_exists():
    assert callable(graphmodelling::Edge.__init__)


def test_graphmodelling::edge_constructor_args():
    sig = inspect.signature(graphmodelling::Edge.__init__)
    params = list(sig.parameters.keys())



def test_graphmodelling::operation_is_not_abstract():
    assert not inspect.isabstract(graphmodelling::Operation)


def test_graphmodelling::operation_constructor_exists():
    assert callable(graphmodelling::Operation.__init__)


def test_graphmodelling::operation_constructor_args():
    sig = inspect.signature(graphmodelling::Operation.__init__)
    params = list(sig.parameters.keys())



def test_graphmodelling::property_is_not_abstract():
    assert not inspect.isabstract(graphmodelling::Property)


def test_graphmodelling::property_constructor_exists():
    assert callable(graphmodelling::Property.__init__)


def test_graphmodelling::property_constructor_args():
    sig = inspect.signature(graphmodelling::Property.__init__)
    params = list(sig.parameters.keys())



def test_graphmodelling::node_is_not_abstract():
    assert not inspect.isabstract(graphmodelling::Node)


def test_graphmodelling::node_constructor_exists():
    assert callable(graphmodelling::Node.__init__)


def test_graphmodelling::node_constructor_args():
    sig = inspect.signature(graphmodelling::Node.__init__)
    params = list(sig.parameters.keys())



def test_graphmodelling::graph_is_not_abstract():
    assert not inspect.isabstract(graphmodelling::Graph)


def test_graphmodelling::graph_constructor_exists():
    assert callable(graphmodelling::Graph.__init__)


def test_graphmodelling::graph_constructor_args():
    sig = inspect.signature(graphmodelling::Graph.__init__)
    params = list(sig.parameters.keys())



def test_graphmodelling::entity_is_not_abstract():
    assert not inspect.isabstract(graphmodelling::Entity)


def test_graphmodelling::entity_constructor_exists():
    assert callable(graphmodelling::Entity.__init__)


def test_graphmodelling::entity_constructor_args():
    sig = inspect.signature(graphmodelling::Entity.__init__)
    params = list(sig.parameters.keys())
    assert "accessModifier" in params, "Missing parameter 'accessModifier'"
    assert "x" in params, "Missing parameter 'x'"
    assert "description" in params, "Missing parameter 'description'"
    assert "height" in params, "Missing parameter 'height'"
    assert "type" in params, "Missing parameter 'type'"
    assert "ID" in params, "Missing parameter 'ID'"
    assert "value" in params, "Missing parameter 'value'"
    assert "category" in params, "Missing parameter 'category'"
    assert "group" in params, "Missing parameter 'group'"
    assert "y" in params, "Missing parameter 'y'"
    assert "name" in params, "Missing parameter 'name'"
    assert "className" in params, "Missing parameter 'className'"
    assert "width" in params, "Missing parameter 'width'"
    assert "text" in params, "Missing parameter 'text'"

def test_graphmodelling::entity_has_accessModifier():
    assert hasattr(graphmodelling::Entity, "accessModifier")
    descriptor = None
    for klass in graphmodelling::Entity.__mro__:
        if "accessModifier" in klass.__dict__:
            descriptor = klass.__dict__["accessModifier"]
            break
    assert isinstance(descriptor, property)

def test_graphmodelling::entity_has_x():
    assert hasattr(graphmodelling::Entity, "x")
    descriptor = None
    for klass in graphmodelling::Entity.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_graphmodelling::entity_has_description():
    assert hasattr(graphmodelling::Entity, "description")
    descriptor = None
    for klass in graphmodelling::Entity.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_graphmodelling::entity_has_height():
    assert hasattr(graphmodelling::Entity, "height")
    descriptor = None
    for klass in graphmodelling::Entity.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_graphmodelling::entity_has_type():
    assert hasattr(graphmodelling::Entity, "type")
    descriptor = None
    for klass in graphmodelling::Entity.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_graphmodelling::entity_has_ID():
    assert hasattr(graphmodelling::Entity, "ID")
    descriptor = None
    for klass in graphmodelling::Entity.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)

def test_graphmodelling::entity_has_value():
    assert hasattr(graphmodelling::Entity, "value")
    descriptor = None
    for klass in graphmodelling::Entity.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_graphmodelling::entity_has_category():
    assert hasattr(graphmodelling::Entity, "category")
    descriptor = None
    for klass in graphmodelling::Entity.__mro__:
        if "category" in klass.__dict__:
            descriptor = klass.__dict__["category"]
            break
    assert isinstance(descriptor, property)

def test_graphmodelling::entity_has_group():
    assert hasattr(graphmodelling::Entity, "group")
    descriptor = None
    for klass in graphmodelling::Entity.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_graphmodelling::entity_has_y():
    assert hasattr(graphmodelling::Entity, "y")
    descriptor = None
    for klass in graphmodelling::Entity.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_graphmodelling::entity_has_name():
    assert hasattr(graphmodelling::Entity, "name")
    descriptor = None
    for klass in graphmodelling::Entity.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_graphmodelling::entity_has_className():
    assert hasattr(graphmodelling::Entity, "className")
    descriptor = None
    for klass in graphmodelling::Entity.__mro__:
        if "className" in klass.__dict__:
            descriptor = klass.__dict__["className"]
            break
    assert isinstance(descriptor, property)

def test_graphmodelling::entity_has_width():
    assert hasattr(graphmodelling::Entity, "width")
    descriptor = None
    for klass in graphmodelling::Entity.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_graphmodelling::entity_has_text():
    assert hasattr(graphmodelling::Entity, "text")
    descriptor = None
    for klass in graphmodelling::Entity.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_graphmodelling::modellingtype_is_not_abstract():
    assert not inspect.isabstract(graphmodelling::ModellingType)


def test_graphmodelling::modellingtype_constructor_exists():
    assert callable(graphmodelling::ModellingType.__init__)


def test_graphmodelling::modellingtype_constructor_args():
    sig = inspect.signature(graphmodelling::ModellingType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_graphmodelling::modellingtype_has_name():
    assert hasattr(graphmodelling::ModellingType, "name")
    descriptor = None
    for klass in graphmodelling::ModellingType.__mro__:
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
graphmodelling::Edge_strategy = st.builds(
    graphmodelling::Edge,
)
graphmodelling::Operation_strategy = st.builds(
    graphmodelling::Operation,
)
graphmodelling::Property_strategy = st.builds(
    graphmodelling::Property,
)
graphmodelling::Node_strategy = st.builds(
    graphmodelling::Node,
)
graphmodelling::Graph_strategy = st.builds(
    graphmodelling::Graph,
)
graphmodelling::Entity_strategy = st.builds(
    graphmodelling::Entity,
    accessModifier=
        safe_text,
    x=
        safe_text,
    description=
        safe_text,
    height=
        safe_text,
    type=
        safe_text,
    ID=
        safe_text,
    value=
        safe_text,
    category=
        safe_text,
    group=
        safe_text,
    y=
        safe_text,
    name=
        safe_text,
    className=
        safe_text,
    width=
        safe_text,
    text=
        safe_text
)
graphmodelling::ModellingType_strategy = st.builds(
    graphmodelling::ModellingType,
    name=
        safe_text
)

@given(instance=Entity_strategy)
@settings(max_examples=50)
def test_entity_instantiation(instance):
    assert isinstance(instance, Entity)

@given(instance=graphmodelling::Edge_strategy)
@settings(max_examples=50)
def test_graphmodelling::edge_instantiation(instance):
    assert isinstance(instance, graphmodelling::Edge)

@given(instance=graphmodelling::Operation_strategy)
@settings(max_examples=50)
def test_graphmodelling::operation_instantiation(instance):
    assert isinstance(instance, graphmodelling::Operation)

@given(instance=graphmodelling::Property_strategy)
@settings(max_examples=50)
def test_graphmodelling::property_instantiation(instance):
    assert isinstance(instance, graphmodelling::Property)

@given(instance=graphmodelling::Node_strategy)
@settings(max_examples=50)
def test_graphmodelling::node_instantiation(instance):
    assert isinstance(instance, graphmodelling::Node)

@given(instance=graphmodelling::Graph_strategy)
@settings(max_examples=50)
def test_graphmodelling::graph_instantiation(instance):
    assert isinstance(instance, graphmodelling::Graph)

@given(instance=graphmodelling::Entity_strategy)
@settings(max_examples=50)
def test_graphmodelling::entity_instantiation(instance):
    assert isinstance(instance, graphmodelling::Entity)

@given(instance=graphmodelling::Entity_strategy)
def test_graphmodelling::entity_accessModifier_type(instance):
    assert isinstance(instance.accessModifier, str)


@given(instance=graphmodelling::Entity_strategy)
def test_graphmodelling::entity_accessModifier_setter(instance):
    original = instance.accessModifier
    instance.accessModifier = original
    assert instance.accessModifier == original

@given(instance=graphmodelling::Entity_strategy)
def test_graphmodelling::entity_x_type(instance):
    assert isinstance(instance.x, str)


@given(instance=graphmodelling::Entity_strategy)
def test_graphmodelling::entity_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=graphmodelling::Entity_strategy)
def test_graphmodelling::entity_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=graphmodelling::Entity_strategy)
def test_graphmodelling::entity_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=graphmodelling::Entity_strategy)
def test_graphmodelling::entity_height_type(instance):
    assert isinstance(instance.height, str)


@given(instance=graphmodelling::Entity_strategy)
def test_graphmodelling::entity_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=graphmodelling::Entity_strategy)
def test_graphmodelling::entity_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=graphmodelling::Entity_strategy)
def test_graphmodelling::entity_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=graphmodelling::Entity_strategy)
def test_graphmodelling::entity_ID_type(instance):
    assert isinstance(instance.ID, str)


@given(instance=graphmodelling::Entity_strategy)
def test_graphmodelling::entity_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

@given(instance=graphmodelling::Entity_strategy)
def test_graphmodelling::entity_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=graphmodelling::Entity_strategy)
def test_graphmodelling::entity_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=graphmodelling::Entity_strategy)
def test_graphmodelling::entity_category_type(instance):
    assert isinstance(instance.category, str)


@given(instance=graphmodelling::Entity_strategy)
def test_graphmodelling::entity_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original

@given(instance=graphmodelling::Entity_strategy)
def test_graphmodelling::entity_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=graphmodelling::Entity_strategy)
def test_graphmodelling::entity_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=graphmodelling::Entity_strategy)
def test_graphmodelling::entity_y_type(instance):
    assert isinstance(instance.y, str)


@given(instance=graphmodelling::Entity_strategy)
def test_graphmodelling::entity_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=graphmodelling::Entity_strategy)
def test_graphmodelling::entity_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=graphmodelling::Entity_strategy)
def test_graphmodelling::entity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=graphmodelling::Entity_strategy)
def test_graphmodelling::entity_className_type(instance):
    assert isinstance(instance.className, str)


@given(instance=graphmodelling::Entity_strategy)
def test_graphmodelling::entity_className_setter(instance):
    original = instance.className
    instance.className = original
    assert instance.className == original

@given(instance=graphmodelling::Entity_strategy)
def test_graphmodelling::entity_width_type(instance):
    assert isinstance(instance.width, str)


@given(instance=graphmodelling::Entity_strategy)
def test_graphmodelling::entity_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=graphmodelling::Entity_strategy)
def test_graphmodelling::entity_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=graphmodelling::Entity_strategy)
def test_graphmodelling::entity_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=graphmodelling::ModellingType_strategy)
@settings(max_examples=50)
def test_graphmodelling::modellingtype_instantiation(instance):
    assert isinstance(instance, graphmodelling::ModellingType)

@given(instance=graphmodelling::ModellingType_strategy)
def test_graphmodelling::modellingtype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=graphmodelling::ModellingType_strategy)
def test_graphmodelling::modellingtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
