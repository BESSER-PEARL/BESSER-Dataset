import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    dot::StrictIdentifiable,
    dot::Statement,
    StrictIdentifiable,
    Connectable,
    Attribute,
    dot::Identifiable,
    dot::Commentable,
    Attributable,
    dot::Attributable,
    AbstractGraph,
    dot::Connectable,
    Commentable,
    dot::Target,
    dot::Attribute,
    dot::Graph,
    dot::NodeID,
    dot::Subgraph,
    dot::AttributeList,
    dot::AList,
    dot::StatementList,
    Identifiable,
    dot::Port,
    dot::AbstractGraph,
    Statement,
    dot::EdgeStatement,
    dot::AssignmentStatement,
    dot::AttributeStatement,
    dot::NodeStatement,
    Compass,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_dot::strictidentifiable_is_not_abstract():
    assert not inspect.isabstract(dot::StrictIdentifiable)


def test_dot::strictidentifiable_constructor_exists():
    assert callable(dot::StrictIdentifiable.__init__)


def test_dot::strictidentifiable_constructor_args():
    sig = inspect.signature(dot::StrictIdentifiable.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_dot::strictidentifiable_has_id():
    assert hasattr(dot::StrictIdentifiable, "id")
    descriptor = None
    for klass in dot::StrictIdentifiable.__mro__:
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



def test_strictidentifiable_is_not_abstract():
    assert not inspect.isabstract(StrictIdentifiable)


def test_strictidentifiable_constructor_exists():
    assert callable(StrictIdentifiable.__init__)


def test_strictidentifiable_constructor_args():
    sig = inspect.signature(StrictIdentifiable.__init__)
    params = list(sig.parameters.keys())



def test_connectable_is_not_abstract():
    assert not inspect.isabstract(Connectable)


def test_connectable_constructor_exists():
    assert callable(Connectable.__init__)


def test_connectable_constructor_args():
    sig = inspect.signature(Connectable.__init__)
    params = list(sig.parameters.keys())



def test_attribute_is_not_abstract():
    assert not inspect.isabstract(Attribute)


def test_attribute_constructor_exists():
    assert callable(Attribute.__init__)


def test_attribute_constructor_args():
    sig = inspect.signature(Attribute.__init__)
    params = list(sig.parameters.keys())



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



def test_dot::commentable_is_not_abstract():
    assert not inspect.isabstract(dot::Commentable)


def test_dot::commentable_constructor_exists():
    assert callable(dot::Commentable.__init__)


def test_dot::commentable_constructor_args():
    sig = inspect.signature(dot::Commentable.__init__)
    params = list(sig.parameters.keys())
    assert "comments" in params, "Missing parameter 'comments'"

def test_dot::commentable_has_comments():
    assert hasattr(dot::Commentable, "comments")
    descriptor = None
    for klass in dot::Commentable.__mro__:
        if "comments" in klass.__dict__:
            descriptor = klass.__dict__["comments"]
            break
    assert isinstance(descriptor, property)



def test_attributable_is_not_abstract():
    assert not inspect.isabstract(Attributable)


def test_attributable_constructor_exists():
    assert callable(Attributable.__init__)


def test_attributable_constructor_args():
    sig = inspect.signature(Attributable.__init__)
    params = list(sig.parameters.keys())



def test_dot::attributable_is_not_abstract():
    assert not inspect.isabstract(dot::Attributable)


def test_dot::attributable_constructor_exists():
    assert callable(dot::Attributable.__init__)


def test_dot::attributable_constructor_args():
    sig = inspect.signature(dot::Attributable.__init__)
    params = list(sig.parameters.keys())



def test_abstractgraph_is_not_abstract():
    assert not inspect.isabstract(AbstractGraph)


def test_abstractgraph_constructor_exists():
    assert callable(AbstractGraph.__init__)


def test_abstractgraph_constructor_args():
    sig = inspect.signature(AbstractGraph.__init__)
    params = list(sig.parameters.keys())



def test_dot::connectable_is_not_abstract():
    assert not inspect.isabstract(dot::Connectable)


def test_dot::connectable_constructor_exists():
    assert callable(dot::Connectable.__init__)


def test_dot::connectable_constructor_args():
    sig = inspect.signature(dot::Connectable.__init__)
    params = list(sig.parameters.keys())



def test_commentable_is_not_abstract():
    assert not inspect.isabstract(Commentable)


def test_commentable_constructor_exists():
    assert callable(Commentable.__init__)


def test_commentable_constructor_args():
    sig = inspect.signature(Commentable.__init__)
    params = list(sig.parameters.keys())



def test_dot::target_is_not_abstract():
    assert not inspect.isabstract(dot::Target)


def test_dot::target_constructor_exists():
    assert callable(dot::Target.__init__)


def test_dot::target_constructor_args():
    sig = inspect.signature(dot::Target.__init__)
    params = list(sig.parameters.keys())
    assert "operation" in params, "Missing parameter 'operation'"

def test_dot::target_has_operation():
    assert hasattr(dot::Target, "operation")
    descriptor = None
    for klass in dot::Target.__mro__:
        if "operation" in klass.__dict__:
            descriptor = klass.__dict__["operation"]
            break
    assert isinstance(descriptor, property)



def test_dot::attribute_is_not_abstract():
    assert not inspect.isabstract(dot::Attribute)


def test_dot::attribute_constructor_exists():
    assert callable(dot::Attribute.__init__)


def test_dot::attribute_constructor_args():
    sig = inspect.signature(dot::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "value" in params, "Missing parameter 'value'"

def test_dot::attribute_has_key():
    assert hasattr(dot::Attribute, "key")
    descriptor = None
    for klass in dot::Attribute.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_dot::attribute_has_value():
    assert hasattr(dot::Attribute, "value")
    descriptor = None
    for klass in dot::Attribute.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_dot::graph_is_not_abstract():
    assert not inspect.isabstract(dot::Graph)


def test_dot::graph_constructor_exists():
    assert callable(dot::Graph.__init__)


def test_dot::graph_constructor_args():
    sig = inspect.signature(dot::Graph.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "strict" in params, "Missing parameter 'strict'"

def test_dot::graph_has_type():
    assert hasattr(dot::Graph, "type")
    descriptor = None
    for klass in dot::Graph.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_dot::graph_has_strict():
    assert hasattr(dot::Graph, "strict")
    descriptor = None
    for klass in dot::Graph.__mro__:
        if "strict" in klass.__dict__:
            descriptor = klass.__dict__["strict"]
            break
    assert isinstance(descriptor, property)



def test_dot::nodeid_is_not_abstract():
    assert not inspect.isabstract(dot::NodeID)


def test_dot::nodeid_constructor_exists():
    assert callable(dot::NodeID.__init__)


def test_dot::nodeid_constructor_args():
    sig = inspect.signature(dot::NodeID.__init__)
    params = list(sig.parameters.keys())



def test_dot::subgraph_is_not_abstract():
    assert not inspect.isabstract(dot::Subgraph)


def test_dot::subgraph_constructor_exists():
    assert callable(dot::Subgraph.__init__)


def test_dot::subgraph_constructor_args():
    sig = inspect.signature(dot::Subgraph.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_dot::subgraph_has_type():
    assert hasattr(dot::Subgraph, "type")
    descriptor = None
    for klass in dot::Subgraph.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_dot::attributelist_is_not_abstract():
    assert not inspect.isabstract(dot::AttributeList)


def test_dot::attributelist_constructor_exists():
    assert callable(dot::AttributeList.__init__)


def test_dot::attributelist_constructor_args():
    sig = inspect.signature(dot::AttributeList.__init__)
    params = list(sig.parameters.keys())



def test_dot::alist_is_not_abstract():
    assert not inspect.isabstract(dot::AList)


def test_dot::alist_constructor_exists():
    assert callable(dot::AList.__init__)


def test_dot::alist_constructor_args():
    sig = inspect.signature(dot::AList.__init__)
    params = list(sig.parameters.keys())



def test_dot::statementlist_is_not_abstract():
    assert not inspect.isabstract(dot::StatementList)


def test_dot::statementlist_constructor_exists():
    assert callable(dot::StatementList.__init__)


def test_dot::statementlist_constructor_args():
    sig = inspect.signature(dot::StatementList.__init__)
    params = list(sig.parameters.keys())



def test_identifiable_is_not_abstract():
    assert not inspect.isabstract(Identifiable)


def test_identifiable_constructor_exists():
    assert callable(Identifiable.__init__)


def test_identifiable_constructor_args():
    sig = inspect.signature(Identifiable.__init__)
    params = list(sig.parameters.keys())



def test_dot::port_is_not_abstract():
    assert not inspect.isabstract(dot::Port)


def test_dot::port_constructor_exists():
    assert callable(dot::Port.__init__)


def test_dot::port_constructor_args():
    sig = inspect.signature(dot::Port.__init__)
    params = list(sig.parameters.keys())
    assert "compass" in params, "Missing parameter 'compass'"

def test_dot::port_has_compass():
    assert hasattr(dot::Port, "compass")
    descriptor = None
    for klass in dot::Port.__mro__:
        if "compass" in klass.__dict__:
            descriptor = klass.__dict__["compass"]
            break
    assert isinstance(descriptor, property)



def test_dot::abstractgraph_is_not_abstract():
    assert not inspect.isabstract(dot::AbstractGraph)


def test_dot::abstractgraph_constructor_exists():
    assert callable(dot::AbstractGraph.__init__)


def test_dot::abstractgraph_constructor_args():
    sig = inspect.signature(dot::AbstractGraph.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_dot::edgestatement_is_not_abstract():
    assert not inspect.isabstract(dot::EdgeStatement)


def test_dot::edgestatement_constructor_exists():
    assert callable(dot::EdgeStatement.__init__)


def test_dot::edgestatement_constructor_args():
    sig = inspect.signature(dot::EdgeStatement.__init__)
    params = list(sig.parameters.keys())



def test_dot::assignmentstatement_is_not_abstract():
    assert not inspect.isabstract(dot::AssignmentStatement)


def test_dot::assignmentstatement_constructor_exists():
    assert callable(dot::AssignmentStatement.__init__)


def test_dot::assignmentstatement_constructor_args():
    sig = inspect.signature(dot::AssignmentStatement.__init__)
    params = list(sig.parameters.keys())
    assert "left" in params, "Missing parameter 'left'"
    assert "right" in params, "Missing parameter 'right'"

def test_dot::assignmentstatement_has_left():
    assert hasattr(dot::AssignmentStatement, "left")
    descriptor = None
    for klass in dot::AssignmentStatement.__mro__:
        if "left" in klass.__dict__:
            descriptor = klass.__dict__["left"]
            break
    assert isinstance(descriptor, property)

def test_dot::assignmentstatement_has_right():
    assert hasattr(dot::AssignmentStatement, "right")
    descriptor = None
    for klass in dot::AssignmentStatement.__mro__:
        if "right" in klass.__dict__:
            descriptor = klass.__dict__["right"]
            break
    assert isinstance(descriptor, property)



def test_dot::attributestatement_is_not_abstract():
    assert not inspect.isabstract(dot::AttributeStatement)


def test_dot::attributestatement_constructor_exists():
    assert callable(dot::AttributeStatement.__init__)


def test_dot::attributestatement_constructor_args():
    sig = inspect.signature(dot::AttributeStatement.__init__)
    params = list(sig.parameters.keys())
    assert "context" in params, "Missing parameter 'context'"

def test_dot::attributestatement_has_context():
    assert hasattr(dot::AttributeStatement, "context")
    descriptor = None
    for klass in dot::AttributeStatement.__mro__:
        if "context" in klass.__dict__:
            descriptor = klass.__dict__["context"]
            break
    assert isinstance(descriptor, property)



def test_dot::nodestatement_is_not_abstract():
    assert not inspect.isabstract(dot::NodeStatement)


def test_dot::nodestatement_constructor_exists():
    assert callable(dot::NodeStatement.__init__)


def test_dot::nodestatement_constructor_args():
    sig = inspect.signature(dot::NodeStatement.__init__)
    params = list(sig.parameters.keys())

def test_compass_exists():
    # Check that the Enumeration exists
    assert Compass is not None

def test_compass_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Compass]
    expected_literals = [
        "CENTER",
        "NORTH_WEST",
        "SOUTH_WEST",
        "APPROPRIATE",
        "NORTH",
        "SOUTH",
        "EAST",
        "SOUTH_EAST",
        "NORTH_EAST",
        "WEST",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Compass"


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
dot::StrictIdentifiable_strategy = st.builds(
    dot::StrictIdentifiable,
    id=
        safe_text
)
dot::Statement_strategy = st.builds(
    dot::Statement,
)
StrictIdentifiable_strategy = st.builds(
    StrictIdentifiable,
)
Connectable_strategy = st.builds(
    Connectable,
)
Attribute_strategy = st.builds(
    Attribute,
)
dot::Identifiable_strategy = st.builds(
    dot::Identifiable,
    id=
        safe_text
)
dot::Commentable_strategy = st.builds(
    dot::Commentable,
    comments=
        safe_text
)
Attributable_strategy = st.builds(
    Attributable,
)
dot::Attributable_strategy = st.builds(
    dot::Attributable,
)
AbstractGraph_strategy = st.builds(
    AbstractGraph,
)
dot::Connectable_strategy = st.builds(
    dot::Connectable,
)
Commentable_strategy = st.builds(
    Commentable,
)
dot::Target_strategy = st.builds(
    dot::Target,
    operation=
        safe_text
)
dot::Attribute_strategy = st.builds(
    dot::Attribute,
    key=
        safe_text,
    value=
        safe_text
)
dot::Graph_strategy = st.builds(
    dot::Graph,
    type=
        safe_text,
    strict=
        safe_text
)
dot::NodeID_strategy = st.builds(
    dot::NodeID,
)
dot::Subgraph_strategy = st.builds(
    dot::Subgraph,
    type=
        safe_text
)
dot::AttributeList_strategy = st.builds(
    dot::AttributeList,
)
dot::AList_strategy = st.builds(
    dot::AList,
)
dot::StatementList_strategy = st.builds(
    dot::StatementList,
)
Identifiable_strategy = st.builds(
    Identifiable,
)
dot::Port_strategy = st.builds(
    dot::Port,
    compass=
        safe_text
)
dot::AbstractGraph_strategy = st.builds(
    dot::AbstractGraph,
)
Statement_strategy = st.builds(
    Statement,
)
dot::EdgeStatement_strategy = st.builds(
    dot::EdgeStatement,
)
dot::AssignmentStatement_strategy = st.builds(
    dot::AssignmentStatement,
    left=
        safe_text,
    right=
        safe_text
)
dot::AttributeStatement_strategy = st.builds(
    dot::AttributeStatement,
    context=
        safe_text
)
dot::NodeStatement_strategy = st.builds(
    dot::NodeStatement,
)

@given(instance=dot::StrictIdentifiable_strategy)
@settings(max_examples=50)
def test_dot::strictidentifiable_instantiation(instance):
    assert isinstance(instance, dot::StrictIdentifiable)

@given(instance=dot::StrictIdentifiable_strategy)
def test_dot::strictidentifiable_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=dot::StrictIdentifiable_strategy)
def test_dot::strictidentifiable_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=dot::Statement_strategy)
@settings(max_examples=50)
def test_dot::statement_instantiation(instance):
    assert isinstance(instance, dot::Statement)

@given(instance=StrictIdentifiable_strategy)
@settings(max_examples=50)
def test_strictidentifiable_instantiation(instance):
    assert isinstance(instance, StrictIdentifiable)

@given(instance=Connectable_strategy)
@settings(max_examples=50)
def test_connectable_instantiation(instance):
    assert isinstance(instance, Connectable)

@given(instance=Attribute_strategy)
@settings(max_examples=50)
def test_attribute_instantiation(instance):
    assert isinstance(instance, Attribute)

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

@given(instance=dot::Commentable_strategy)
@settings(max_examples=50)
def test_dot::commentable_instantiation(instance):
    assert isinstance(instance, dot::Commentable)

@given(instance=dot::Commentable_strategy)
def test_dot::commentable_comments_type(instance):
    assert isinstance(instance.comments, str)


@given(instance=dot::Commentable_strategy)
def test_dot::commentable_comments_setter(instance):
    original = instance.comments
    instance.comments = original
    assert instance.comments == original

@given(instance=Attributable_strategy)
@settings(max_examples=50)
def test_attributable_instantiation(instance):
    assert isinstance(instance, Attributable)

@given(instance=dot::Attributable_strategy)
@settings(max_examples=50)
def test_dot::attributable_instantiation(instance):
    assert isinstance(instance, dot::Attributable)

@given(instance=AbstractGraph_strategy)
@settings(max_examples=50)
def test_abstractgraph_instantiation(instance):
    assert isinstance(instance, AbstractGraph)

@given(instance=dot::Connectable_strategy)
@settings(max_examples=50)
def test_dot::connectable_instantiation(instance):
    assert isinstance(instance, dot::Connectable)

@given(instance=Commentable_strategy)
@settings(max_examples=50)
def test_commentable_instantiation(instance):
    assert isinstance(instance, Commentable)

@given(instance=dot::Target_strategy)
@settings(max_examples=50)
def test_dot::target_instantiation(instance):
    assert isinstance(instance, dot::Target)

@given(instance=dot::Target_strategy)
def test_dot::target_operation_type(instance):
    assert isinstance(instance.operation, str)


@given(instance=dot::Target_strategy)
def test_dot::target_operation_setter(instance):
    original = instance.operation
    instance.operation = original
    assert instance.operation == original

@given(instance=dot::Attribute_strategy)
@settings(max_examples=50)
def test_dot::attribute_instantiation(instance):
    assert isinstance(instance, dot::Attribute)

@given(instance=dot::Attribute_strategy)
def test_dot::attribute_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=dot::Attribute_strategy)
def test_dot::attribute_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=dot::Attribute_strategy)
def test_dot::attribute_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=dot::Attribute_strategy)
def test_dot::attribute_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=dot::Graph_strategy)
@settings(max_examples=50)
def test_dot::graph_instantiation(instance):
    assert isinstance(instance, dot::Graph)

@given(instance=dot::Graph_strategy)
def test_dot::graph_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=dot::Graph_strategy)
def test_dot::graph_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=dot::Graph_strategy)
def test_dot::graph_strict_type(instance):
    assert isinstance(instance.strict, str)


@given(instance=dot::Graph_strategy)
def test_dot::graph_strict_setter(instance):
    original = instance.strict
    instance.strict = original
    assert instance.strict == original

@given(instance=dot::NodeID_strategy)
@settings(max_examples=50)
def test_dot::nodeid_instantiation(instance):
    assert isinstance(instance, dot::NodeID)

@given(instance=dot::Subgraph_strategy)
@settings(max_examples=50)
def test_dot::subgraph_instantiation(instance):
    assert isinstance(instance, dot::Subgraph)

@given(instance=dot::Subgraph_strategy)
def test_dot::subgraph_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=dot::Subgraph_strategy)
def test_dot::subgraph_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=dot::AttributeList_strategy)
@settings(max_examples=50)
def test_dot::attributelist_instantiation(instance):
    assert isinstance(instance, dot::AttributeList)

@given(instance=dot::AList_strategy)
@settings(max_examples=50)
def test_dot::alist_instantiation(instance):
    assert isinstance(instance, dot::AList)

@given(instance=dot::StatementList_strategy)
@settings(max_examples=50)
def test_dot::statementlist_instantiation(instance):
    assert isinstance(instance, dot::StatementList)

@given(instance=Identifiable_strategy)
@settings(max_examples=50)
def test_identifiable_instantiation(instance):
    assert isinstance(instance, Identifiable)

@given(instance=dot::Port_strategy)
@settings(max_examples=50)
def test_dot::port_instantiation(instance):
    assert isinstance(instance, dot::Port)

@given(instance=dot::Port_strategy)
def test_dot::port_compass_type(instance):
    assert isinstance(instance.compass, str)


@given(instance=dot::Port_strategy)
def test_dot::port_compass_setter(instance):
    original = instance.compass
    instance.compass = original
    assert instance.compass == original

@given(instance=dot::AbstractGraph_strategy)
@settings(max_examples=50)
def test_dot::abstractgraph_instantiation(instance):
    assert isinstance(instance, dot::AbstractGraph)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=dot::EdgeStatement_strategy)
@settings(max_examples=50)
def test_dot::edgestatement_instantiation(instance):
    assert isinstance(instance, dot::EdgeStatement)

@given(instance=dot::AssignmentStatement_strategy)
@settings(max_examples=50)
def test_dot::assignmentstatement_instantiation(instance):
    assert isinstance(instance, dot::AssignmentStatement)

@given(instance=dot::AssignmentStatement_strategy)
def test_dot::assignmentstatement_left_type(instance):
    assert isinstance(instance.left, str)


@given(instance=dot::AssignmentStatement_strategy)
def test_dot::assignmentstatement_left_setter(instance):
    original = instance.left
    instance.left = original
    assert instance.left == original

@given(instance=dot::AssignmentStatement_strategy)
def test_dot::assignmentstatement_right_type(instance):
    assert isinstance(instance.right, str)


@given(instance=dot::AssignmentStatement_strategy)
def test_dot::assignmentstatement_right_setter(instance):
    original = instance.right
    instance.right = original
    assert instance.right == original

@given(instance=dot::AttributeStatement_strategy)
@settings(max_examples=50)
def test_dot::attributestatement_instantiation(instance):
    assert isinstance(instance, dot::AttributeStatement)

@given(instance=dot::AttributeStatement_strategy)
def test_dot::attributestatement_context_type(instance):
    assert isinstance(instance.context, str)


@given(instance=dot::AttributeStatement_strategy)
def test_dot::attributestatement_context_setter(instance):
    original = instance.context
    instance.context = original
    assert instance.context == original

@given(instance=dot::NodeStatement_strategy)
@settings(max_examples=50)
def test_dot::nodestatement_instantiation(instance):
    assert isinstance(instance, dot::NodeStatement)
