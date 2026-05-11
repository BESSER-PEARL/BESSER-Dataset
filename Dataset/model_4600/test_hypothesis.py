import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    dot::AttributedItem,
    dot::StringToStringMapEntry,
    dot::Identifiable,
    dot::Statement,
    Statement,
    dot::Assignment,
    Identifiable,
    dot::Graph,
    Node,
    dot::InnerNode,
    dot::RecordNode,
    AttributedItem,
    dot::Edge,
    dot::Settings,
    dot::Node,
    SettingsType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_dot::attributeditem_is_not_abstract():
    assert not inspect.isabstract(dot::AttributedItem)


def test_dot::attributeditem_constructor_exists():
    assert callable(dot::AttributedItem.__init__)


def test_dot::attributeditem_constructor_args():
    sig = inspect.signature(dot::AttributedItem.__init__)
    params = list(sig.parameters.keys())



def test_dot::stringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(dot::StringToStringMapEntry)


def test_dot::stringtostringmapentry_constructor_exists():
    assert callable(dot::StringToStringMapEntry.__init__)


def test_dot::stringtostringmapentry_constructor_args():
    sig = inspect.signature(dot::StringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "key" in params, "Missing parameter 'key'"

def test_dot::stringtostringmapentry_has_value():
    assert hasattr(dot::StringToStringMapEntry, "value")
    descriptor = None
    for klass in dot::StringToStringMapEntry.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_dot::stringtostringmapentry_has_key():
    assert hasattr(dot::StringToStringMapEntry, "key")
    descriptor = None
    for klass in dot::StringToStringMapEntry.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_dot::identifiable_is_not_abstract():
    assert not inspect.isabstract(dot::Identifiable)


def test_dot::identifiable_constructor_exists():
    assert callable(dot::Identifiable.__init__)


def test_dot::identifiable_constructor_args():
    sig = inspect.signature(dot::Identifiable.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_dot::identifiable_has_id():
    assert hasattr(dot::Identifiable, "id")
    descriptor = None
    for klass in dot::Identifiable.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_dot::statement_is_not_abstract():
    assert not inspect.isabstract(dot::Statement)


def test_dot::statement_constructor_exists():
    assert callable(dot::Statement.__init__)


def test_dot::statement_constructor_args():
    sig = inspect.signature(dot::Statement.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_dot::assignment_is_not_abstract():
    assert not inspect.isabstract(dot::Assignment)


def test_dot::assignment_constructor_exists():
    assert callable(dot::Assignment.__init__)


def test_dot::assignment_constructor_args():
    sig = inspect.signature(dot::Assignment.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "value" in params, "Missing parameter 'value'"

def test_dot::assignment_has_key():
    assert hasattr(dot::Assignment, "key")
    descriptor = None
    for klass in dot::Assignment.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_dot::assignment_has_value():
    assert hasattr(dot::Assignment, "value")
    descriptor = None
    for klass in dot::Assignment.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_identifiable_is_not_abstract():
    assert not inspect.isabstract(Identifiable)


def test_identifiable_constructor_exists():
    assert callable(Identifiable.__init__)


def test_identifiable_constructor_args():
    sig = inspect.signature(Identifiable.__init__)
    params = list(sig.parameters.keys())



def test_dot::graph_is_not_abstract():
    assert not inspect.isabstract(dot::Graph)


def test_dot::graph_constructor_exists():
    assert callable(dot::Graph.__init__)


def test_dot::graph_constructor_args():
    sig = inspect.signature(dot::Graph.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_dot::innernode_is_not_abstract():
    assert not inspect.isabstract(dot::InnerNode)


def test_dot::innernode_constructor_exists():
    assert callable(dot::InnerNode.__init__)


def test_dot::innernode_constructor_args():
    sig = inspect.signature(dot::InnerNode.__init__)
    params = list(sig.parameters.keys())



def test_dot::recordnode_is_not_abstract():
    assert not inspect.isabstract(dot::RecordNode)


def test_dot::recordnode_constructor_exists():
    assert callable(dot::RecordNode.__init__)


def test_dot::recordnode_constructor_args():
    sig = inspect.signature(dot::RecordNode.__init__)
    params = list(sig.parameters.keys())



def test_attributeditem_is_not_abstract():
    assert not inspect.isabstract(AttributedItem)


def test_attributeditem_constructor_exists():
    assert callable(AttributedItem.__init__)


def test_attributeditem_constructor_args():
    sig = inspect.signature(AttributedItem.__init__)
    params = list(sig.parameters.keys())



def test_dot::edge_is_not_abstract():
    assert not inspect.isabstract(dot::Edge)


def test_dot::edge_constructor_exists():
    assert callable(dot::Edge.__init__)


def test_dot::edge_constructor_args():
    sig = inspect.signature(dot::Edge.__init__)
    params = list(sig.parameters.keys())



def test_dot::settings_is_not_abstract():
    assert not inspect.isabstract(dot::Settings)


def test_dot::settings_constructor_exists():
    assert callable(dot::Settings.__init__)


def test_dot::settings_constructor_args():
    sig = inspect.signature(dot::Settings.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_dot::settings_has_type():
    assert hasattr(dot::Settings, "type")
    descriptor = None
    for klass in dot::Settings.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_dot::node_is_not_abstract():
    assert not inspect.isabstract(dot::Node)


def test_dot::node_constructor_exists():
    assert callable(dot::Node.__init__)


def test_dot::node_constructor_args():
    sig = inspect.signature(dot::Node.__init__)
    params = list(sig.parameters.keys())

def test_settingstype_exists():
    # Check that the Enumeration exists
    assert SettingsType is not None

def test_settingstype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SettingsType]
    expected_literals = [
        "NODE",
        "EDGE",
        "GRAPH",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SettingsType"


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
dot::AttributedItem_strategy = st.builds(
    dot::AttributedItem,
)
dot::StringToStringMapEntry_strategy = st.builds(
    dot::StringToStringMapEntry,
    value=
        safe_text,
    key=
        safe_text
)
dot::Identifiable_strategy = st.builds(
    dot::Identifiable,
    id=
        safe_text
)
dot::Statement_strategy = st.builds(
    dot::Statement,
)
Statement_strategy = st.builds(
    Statement,
)
dot::Assignment_strategy = st.builds(
    dot::Assignment,
    key=
        safe_text,
    value=
        safe_text
)
Identifiable_strategy = st.builds(
    Identifiable,
)
dot::Graph_strategy = st.builds(
    dot::Graph,
)
Node_strategy = st.builds(
    Node,
)
dot::InnerNode_strategy = st.builds(
    dot::InnerNode,
)
dot::RecordNode_strategy = st.builds(
    dot::RecordNode,
)
AttributedItem_strategy = st.builds(
    AttributedItem,
)
dot::Edge_strategy = st.builds(
    dot::Edge,
)
dot::Settings_strategy = st.builds(
    dot::Settings,
    type=
        safe_text
)
dot::Node_strategy = st.builds(
    dot::Node,
)

@given(instance=dot::AttributedItem_strategy)
@settings(max_examples=50)
def test_dot::attributeditem_instantiation(instance):
    assert isinstance(instance, dot::AttributedItem)

@given(instance=dot::StringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_dot::stringtostringmapentry_instantiation(instance):
    assert isinstance(instance, dot::StringToStringMapEntry)

@given(instance=dot::StringToStringMapEntry_strategy)
def test_dot::stringtostringmapentry_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=dot::StringToStringMapEntry_strategy)
def test_dot::stringtostringmapentry_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=dot::StringToStringMapEntry_strategy)
def test_dot::stringtostringmapentry_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=dot::StringToStringMapEntry_strategy)
def test_dot::stringtostringmapentry_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=dot::Identifiable_strategy)
@settings(max_examples=50)
def test_dot::identifiable_instantiation(instance):
    assert isinstance(instance, dot::Identifiable)

@given(instance=dot::Identifiable_strategy)
def test_dot::identifiable_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=dot::Identifiable_strategy)
def test_dot::identifiable_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=dot::Statement_strategy)
@settings(max_examples=50)
def test_dot::statement_instantiation(instance):
    assert isinstance(instance, dot::Statement)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=dot::Assignment_strategy)
@settings(max_examples=50)
def test_dot::assignment_instantiation(instance):
    assert isinstance(instance, dot::Assignment)

@given(instance=dot::Assignment_strategy)
def test_dot::assignment_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=dot::Assignment_strategy)
def test_dot::assignment_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=dot::Assignment_strategy)
def test_dot::assignment_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=dot::Assignment_strategy)
def test_dot::assignment_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Identifiable_strategy)
@settings(max_examples=50)
def test_identifiable_instantiation(instance):
    assert isinstance(instance, Identifiable)

@given(instance=dot::Graph_strategy)
@settings(max_examples=50)
def test_dot::graph_instantiation(instance):
    assert isinstance(instance, dot::Graph)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=dot::InnerNode_strategy)
@settings(max_examples=50)
def test_dot::innernode_instantiation(instance):
    assert isinstance(instance, dot::InnerNode)

@given(instance=dot::RecordNode_strategy)
@settings(max_examples=50)
def test_dot::recordnode_instantiation(instance):
    assert isinstance(instance, dot::RecordNode)

@given(instance=AttributedItem_strategy)
@settings(max_examples=50)
def test_attributeditem_instantiation(instance):
    assert isinstance(instance, AttributedItem)

@given(instance=dot::Edge_strategy)
@settings(max_examples=50)
def test_dot::edge_instantiation(instance):
    assert isinstance(instance, dot::Edge)

@given(instance=dot::Settings_strategy)
@settings(max_examples=50)
def test_dot::settings_instantiation(instance):
    assert isinstance(instance, dot::Settings)

@given(instance=dot::Settings_strategy)
def test_dot::settings_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=dot::Settings_strategy)
def test_dot::settings_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=dot::Node_strategy)
@settings(max_examples=50)
def test_dot::node_instantiation(instance):
    assert isinstance(instance, dot::Node)
