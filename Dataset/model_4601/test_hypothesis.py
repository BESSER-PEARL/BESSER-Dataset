import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    gv_StrictIdentifiable,
    gv_Statement,
    StrictIdentifiable,
    Connectable,
    gv_Commentable,
    Attribute,
    gv_Identifiable,
    AbstractGraph,
    Attributable,
    gv_Connectable,
    Commentable,
    gv_Graph,
    gv_Target,
    gv_NodeID,
    gv_Subgraph,
    gv_Attribute,
    gv_AList,
    gv_StatementList,
    Identifiable,
    gv_Port,
    gv_AbstractGraph,
    gv_AttributeList,
    gv_Attributable,
    Statement,
    gv_AttributeStatement,
    gv_EdgeStatement,
    gv_NodeStatement,
    gv_AssignmentStatement,
    Compass,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_gv_strictidentifiable_is_not_abstract():
    assert not inspect.isabstract(gv_StrictIdentifiable)


def test_gv_strictidentifiable_constructor_exists():
    assert callable(gv_StrictIdentifiable.__init__)


def test_gv_strictidentifiable_constructor_args():
    sig = inspect.signature(gv_StrictIdentifiable.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_gv_strictidentifiable_has_id():
    assert hasattr(gv_StrictIdentifiable, "id")
    descriptor = None
    for klass in gv_StrictIdentifiable.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_gv_statement_is_not_abstract():
    assert not inspect.isabstract(gv_Statement)


def test_gv_statement_constructor_exists():
    assert callable(gv_Statement.__init__)


def test_gv_statement_constructor_args():
    sig = inspect.signature(gv_Statement.__init__)
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



def test_gv_commentable_is_not_abstract():
    assert not inspect.isabstract(gv_Commentable)


def test_gv_commentable_constructor_exists():
    assert callable(gv_Commentable.__init__)


def test_gv_commentable_constructor_args():
    sig = inspect.signature(gv_Commentable.__init__)
    params = list(sig.parameters.keys())
    assert "comments" in params, "Missing parameter 'comments'"

def test_gv_commentable_has_comments():
    assert hasattr(gv_Commentable, "comments")
    descriptor = None
    for klass in gv_Commentable.__mro__:
        if "comments" in klass.__dict__:
            descriptor = klass.__dict__["comments"]
            break
    assert isinstance(descriptor, property)



def test_attribute_is_not_abstract():
    assert not inspect.isabstract(Attribute)


def test_attribute_constructor_exists():
    assert callable(Attribute.__init__)


def test_attribute_constructor_args():
    sig = inspect.signature(Attribute.__init__)
    params = list(sig.parameters.keys())



def test_gv_identifiable_is_not_abstract():
    assert not inspect.isabstract(gv_Identifiable)


def test_gv_identifiable_constructor_exists():
    assert callable(gv_Identifiable.__init__)


def test_gv_identifiable_constructor_args():
    sig = inspect.signature(gv_Identifiable.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_gv_identifiable_has_id():
    assert hasattr(gv_Identifiable, "id")
    descriptor = None
    for klass in gv_Identifiable.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_abstractgraph_is_not_abstract():
    assert not inspect.isabstract(AbstractGraph)


def test_abstractgraph_constructor_exists():
    assert callable(AbstractGraph.__init__)


def test_abstractgraph_constructor_args():
    sig = inspect.signature(AbstractGraph.__init__)
    params = list(sig.parameters.keys())



def test_attributable_is_not_abstract():
    assert not inspect.isabstract(Attributable)


def test_attributable_constructor_exists():
    assert callable(Attributable.__init__)


def test_attributable_constructor_args():
    sig = inspect.signature(Attributable.__init__)
    params = list(sig.parameters.keys())



def test_gv_connectable_is_not_abstract():
    assert not inspect.isabstract(gv_Connectable)


def test_gv_connectable_constructor_exists():
    assert callable(gv_Connectable.__init__)


def test_gv_connectable_constructor_args():
    sig = inspect.signature(gv_Connectable.__init__)
    params = list(sig.parameters.keys())



def test_commentable_is_not_abstract():
    assert not inspect.isabstract(Commentable)


def test_commentable_constructor_exists():
    assert callable(Commentable.__init__)


def test_commentable_constructor_args():
    sig = inspect.signature(Commentable.__init__)
    params = list(sig.parameters.keys())



def test_gv_graph_is_not_abstract():
    assert not inspect.isabstract(gv_Graph)


def test_gv_graph_constructor_exists():
    assert callable(gv_Graph.__init__)


def test_gv_graph_constructor_args():
    sig = inspect.signature(gv_Graph.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "strict" in params, "Missing parameter 'strict'"

def test_gv_graph_has_type():
    assert hasattr(gv_Graph, "type")
    descriptor = None
    for klass in gv_Graph.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_gv_graph_has_strict():
    assert hasattr(gv_Graph, "strict")
    descriptor = None
    for klass in gv_Graph.__mro__:
        if "strict" in klass.__dict__:
            descriptor = klass.__dict__["strict"]
            break
    assert isinstance(descriptor, property)



def test_gv_target_is_not_abstract():
    assert not inspect.isabstract(gv_Target)


def test_gv_target_constructor_exists():
    assert callable(gv_Target.__init__)


def test_gv_target_constructor_args():
    sig = inspect.signature(gv_Target.__init__)
    params = list(sig.parameters.keys())
    assert "operation" in params, "Missing parameter 'operation'"

def test_gv_target_has_operation():
    assert hasattr(gv_Target, "operation")
    descriptor = None
    for klass in gv_Target.__mro__:
        if "operation" in klass.__dict__:
            descriptor = klass.__dict__["operation"]
            break
    assert isinstance(descriptor, property)



def test_gv_nodeid_is_not_abstract():
    assert not inspect.isabstract(gv_NodeID)


def test_gv_nodeid_constructor_exists():
    assert callable(gv_NodeID.__init__)


def test_gv_nodeid_constructor_args():
    sig = inspect.signature(gv_NodeID.__init__)
    params = list(sig.parameters.keys())



def test_gv_subgraph_is_not_abstract():
    assert not inspect.isabstract(gv_Subgraph)


def test_gv_subgraph_constructor_exists():
    assert callable(gv_Subgraph.__init__)


def test_gv_subgraph_constructor_args():
    sig = inspect.signature(gv_Subgraph.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_gv_subgraph_has_type():
    assert hasattr(gv_Subgraph, "type")
    descriptor = None
    for klass in gv_Subgraph.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_gv_attribute_is_not_abstract():
    assert not inspect.isabstract(gv_Attribute)


def test_gv_attribute_constructor_exists():
    assert callable(gv_Attribute.__init__)


def test_gv_attribute_constructor_args():
    sig = inspect.signature(gv_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "key" in params, "Missing parameter 'key'"

def test_gv_attribute_has_value():
    assert hasattr(gv_Attribute, "value")
    descriptor = None
    for klass in gv_Attribute.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_gv_attribute_has_key():
    assert hasattr(gv_Attribute, "key")
    descriptor = None
    for klass in gv_Attribute.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_gv_alist_is_not_abstract():
    assert not inspect.isabstract(gv_AList)


def test_gv_alist_constructor_exists():
    assert callable(gv_AList.__init__)


def test_gv_alist_constructor_args():
    sig = inspect.signature(gv_AList.__init__)
    params = list(sig.parameters.keys())



def test_gv_statementlist_is_not_abstract():
    assert not inspect.isabstract(gv_StatementList)


def test_gv_statementlist_constructor_exists():
    assert callable(gv_StatementList.__init__)


def test_gv_statementlist_constructor_args():
    sig = inspect.signature(gv_StatementList.__init__)
    params = list(sig.parameters.keys())



def test_identifiable_is_not_abstract():
    assert not inspect.isabstract(Identifiable)


def test_identifiable_constructor_exists():
    assert callable(Identifiable.__init__)


def test_identifiable_constructor_args():
    sig = inspect.signature(Identifiable.__init__)
    params = list(sig.parameters.keys())



def test_gv_port_is_not_abstract():
    assert not inspect.isabstract(gv_Port)


def test_gv_port_constructor_exists():
    assert callable(gv_Port.__init__)


def test_gv_port_constructor_args():
    sig = inspect.signature(gv_Port.__init__)
    params = list(sig.parameters.keys())
    assert "compass" in params, "Missing parameter 'compass'"

def test_gv_port_has_compass():
    assert hasattr(gv_Port, "compass")
    descriptor = None
    for klass in gv_Port.__mro__:
        if "compass" in klass.__dict__:
            descriptor = klass.__dict__["compass"]
            break
    assert isinstance(descriptor, property)



def test_gv_abstractgraph_is_not_abstract():
    assert not inspect.isabstract(gv_AbstractGraph)


def test_gv_abstractgraph_constructor_exists():
    assert callable(gv_AbstractGraph.__init__)


def test_gv_abstractgraph_constructor_args():
    sig = inspect.signature(gv_AbstractGraph.__init__)
    params = list(sig.parameters.keys())



def test_gv_attributelist_is_not_abstract():
    assert not inspect.isabstract(gv_AttributeList)


def test_gv_attributelist_constructor_exists():
    assert callable(gv_AttributeList.__init__)


def test_gv_attributelist_constructor_args():
    sig = inspect.signature(gv_AttributeList.__init__)
    params = list(sig.parameters.keys())



def test_gv_attributable_is_not_abstract():
    assert not inspect.isabstract(gv_Attributable)


def test_gv_attributable_constructor_exists():
    assert callable(gv_Attributable.__init__)


def test_gv_attributable_constructor_args():
    sig = inspect.signature(gv_Attributable.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_gv_attributestatement_is_not_abstract():
    assert not inspect.isabstract(gv_AttributeStatement)


def test_gv_attributestatement_constructor_exists():
    assert callable(gv_AttributeStatement.__init__)


def test_gv_attributestatement_constructor_args():
    sig = inspect.signature(gv_AttributeStatement.__init__)
    params = list(sig.parameters.keys())
    assert "context" in params, "Missing parameter 'context'"

def test_gv_attributestatement_has_context():
    assert hasattr(gv_AttributeStatement, "context")
    descriptor = None
    for klass in gv_AttributeStatement.__mro__:
        if "context" in klass.__dict__:
            descriptor = klass.__dict__["context"]
            break
    assert isinstance(descriptor, property)



def test_gv_edgestatement_is_not_abstract():
    assert not inspect.isabstract(gv_EdgeStatement)


def test_gv_edgestatement_constructor_exists():
    assert callable(gv_EdgeStatement.__init__)


def test_gv_edgestatement_constructor_args():
    sig = inspect.signature(gv_EdgeStatement.__init__)
    params = list(sig.parameters.keys())



def test_gv_nodestatement_is_not_abstract():
    assert not inspect.isabstract(gv_NodeStatement)


def test_gv_nodestatement_constructor_exists():
    assert callable(gv_NodeStatement.__init__)


def test_gv_nodestatement_constructor_args():
    sig = inspect.signature(gv_NodeStatement.__init__)
    params = list(sig.parameters.keys())



def test_gv_assignmentstatement_is_not_abstract():
    assert not inspect.isabstract(gv_AssignmentStatement)


def test_gv_assignmentstatement_constructor_exists():
    assert callable(gv_AssignmentStatement.__init__)


def test_gv_assignmentstatement_constructor_args():
    sig = inspect.signature(gv_AssignmentStatement.__init__)
    params = list(sig.parameters.keys())
    assert "right" in params, "Missing parameter 'right'"
    assert "left" in params, "Missing parameter 'left'"

def test_gv_assignmentstatement_has_right():
    assert hasattr(gv_AssignmentStatement, "right")
    descriptor = None
    for klass in gv_AssignmentStatement.__mro__:
        if "right" in klass.__dict__:
            descriptor = klass.__dict__["right"]
            break
    assert isinstance(descriptor, property)

def test_gv_assignmentstatement_has_left():
    assert hasattr(gv_AssignmentStatement, "left")
    descriptor = None
    for klass in gv_AssignmentStatement.__mro__:
        if "left" in klass.__dict__:
            descriptor = klass.__dict__["left"]
            break
    assert isinstance(descriptor, property)

def test_compass_exists():
    # Check that the Enumeration exists
    assert Compass is not None

def test_compass_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Compass]
    expected_literals = [
        "WEST",
        "APPROPRIATE",
        "SOUTH_WEST",
        "CENTER",
        "NORTH_EAST",
        "SOUTH_EAST",
        "NORTH",
        "EAST",
        "NORTH_WEST",
        "SOUTH",
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
gv_StrictIdentifiable_strategy = st.builds(
    gv_StrictIdentifiable,
    id=
        safe_text
)
gv_Statement_strategy = st.builds(
    gv_Statement,
)
StrictIdentifiable_strategy = st.builds(
    StrictIdentifiable,
)
Connectable_strategy = st.builds(
    Connectable,
)
gv_Commentable_strategy = st.builds(
    gv_Commentable,
    comments=
        safe_text
)
Attribute_strategy = st.builds(
    Attribute,
)
gv_Identifiable_strategy = st.builds(
    gv_Identifiable,
    id=
        safe_text
)
AbstractGraph_strategy = st.builds(
    AbstractGraph,
)
Attributable_strategy = st.builds(
    Attributable,
)
gv_Connectable_strategy = st.builds(
    gv_Connectable,
)
Commentable_strategy = st.builds(
    Commentable,
)
gv_Graph_strategy = st.builds(
    gv_Graph,
    type=
        safe_text,
    strict=
        safe_text
)
gv_Target_strategy = st.builds(
    gv_Target,
    operation=
        safe_text
)
gv_NodeID_strategy = st.builds(
    gv_NodeID,
)
gv_Subgraph_strategy = st.builds(
    gv_Subgraph,
    type=
        safe_text
)
gv_Attribute_strategy = st.builds(
    gv_Attribute,
    value=
        safe_text,
    key=
        safe_text
)
gv_AList_strategy = st.builds(
    gv_AList,
)
gv_StatementList_strategy = st.builds(
    gv_StatementList,
)
Identifiable_strategy = st.builds(
    Identifiable,
)
gv_Port_strategy = st.builds(
    gv_Port,
    compass=
        safe_text
)
gv_AbstractGraph_strategy = st.builds(
    gv_AbstractGraph,
)
gv_AttributeList_strategy = st.builds(
    gv_AttributeList,
)
gv_Attributable_strategy = st.builds(
    gv_Attributable,
)
Statement_strategy = st.builds(
    Statement,
)
gv_AttributeStatement_strategy = st.builds(
    gv_AttributeStatement,
    context=
        safe_text
)
gv_EdgeStatement_strategy = st.builds(
    gv_EdgeStatement,
)
gv_NodeStatement_strategy = st.builds(
    gv_NodeStatement,
)
gv_AssignmentStatement_strategy = st.builds(
    gv_AssignmentStatement,
    right=
        safe_text,
    left=
        safe_text
)

@given(instance=gv_StrictIdentifiable_strategy)
@settings(max_examples=50)
def test_gv_strictidentifiable_instantiation(instance):
    assert isinstance(instance, gv_StrictIdentifiable)



@given(instance=gv_StrictIdentifiable_strategy)
def test_gv_strictidentifiable_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=gv_Statement_strategy)
@settings(max_examples=50)
def test_gv_statement_instantiation(instance):
    assert isinstance(instance, gv_Statement)

@given(instance=StrictIdentifiable_strategy)
@settings(max_examples=50)
def test_strictidentifiable_instantiation(instance):
    assert isinstance(instance, StrictIdentifiable)

@given(instance=Connectable_strategy)
@settings(max_examples=50)
def test_connectable_instantiation(instance):
    assert isinstance(instance, Connectable)

@given(instance=gv_Commentable_strategy)
@settings(max_examples=50)
def test_gv_commentable_instantiation(instance):
    assert isinstance(instance, gv_Commentable)



@given(instance=gv_Commentable_strategy)
def test_gv_commentable_comments_setter(instance):
    original = instance.comments
    instance.comments = original
    assert instance.comments == original

@given(instance=Attribute_strategy)
@settings(max_examples=50)
def test_attribute_instantiation(instance):
    assert isinstance(instance, Attribute)

@given(instance=gv_Identifiable_strategy)
@settings(max_examples=50)
def test_gv_identifiable_instantiation(instance):
    assert isinstance(instance, gv_Identifiable)



@given(instance=gv_Identifiable_strategy)
def test_gv_identifiable_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=AbstractGraph_strategy)
@settings(max_examples=50)
def test_abstractgraph_instantiation(instance):
    assert isinstance(instance, AbstractGraph)

@given(instance=Attributable_strategy)
@settings(max_examples=50)
def test_attributable_instantiation(instance):
    assert isinstance(instance, Attributable)

@given(instance=gv_Connectable_strategy)
@settings(max_examples=50)
def test_gv_connectable_instantiation(instance):
    assert isinstance(instance, gv_Connectable)

@given(instance=Commentable_strategy)
@settings(max_examples=50)
def test_commentable_instantiation(instance):
    assert isinstance(instance, Commentable)

@given(instance=gv_Graph_strategy)
@settings(max_examples=50)
def test_gv_graph_instantiation(instance):
    assert isinstance(instance, gv_Graph)



@given(instance=gv_Graph_strategy)
def test_gv_graph_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=gv_Graph_strategy)
def test_gv_graph_strict_setter(instance):
    original = instance.strict
    instance.strict = original
    assert instance.strict == original

@given(instance=gv_Target_strategy)
@settings(max_examples=50)
def test_gv_target_instantiation(instance):
    assert isinstance(instance, gv_Target)



@given(instance=gv_Target_strategy)
def test_gv_target_operation_setter(instance):
    original = instance.operation
    instance.operation = original
    assert instance.operation == original

@given(instance=gv_NodeID_strategy)
@settings(max_examples=50)
def test_gv_nodeid_instantiation(instance):
    assert isinstance(instance, gv_NodeID)

@given(instance=gv_Subgraph_strategy)
@settings(max_examples=50)
def test_gv_subgraph_instantiation(instance):
    assert isinstance(instance, gv_Subgraph)



@given(instance=gv_Subgraph_strategy)
def test_gv_subgraph_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=gv_Attribute_strategy)
@settings(max_examples=50)
def test_gv_attribute_instantiation(instance):
    assert isinstance(instance, gv_Attribute)



@given(instance=gv_Attribute_strategy)
def test_gv_attribute_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=gv_Attribute_strategy)
def test_gv_attribute_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=gv_AList_strategy)
@settings(max_examples=50)
def test_gv_alist_instantiation(instance):
    assert isinstance(instance, gv_AList)

@given(instance=gv_StatementList_strategy)
@settings(max_examples=50)
def test_gv_statementlist_instantiation(instance):
    assert isinstance(instance, gv_StatementList)

@given(instance=Identifiable_strategy)
@settings(max_examples=50)
def test_identifiable_instantiation(instance):
    assert isinstance(instance, Identifiable)

@given(instance=gv_Port_strategy)
@settings(max_examples=50)
def test_gv_port_instantiation(instance):
    assert isinstance(instance, gv_Port)



@given(instance=gv_Port_strategy)
def test_gv_port_compass_setter(instance):
    original = instance.compass
    instance.compass = original
    assert instance.compass == original

@given(instance=gv_AbstractGraph_strategy)
@settings(max_examples=50)
def test_gv_abstractgraph_instantiation(instance):
    assert isinstance(instance, gv_AbstractGraph)

@given(instance=gv_AttributeList_strategy)
@settings(max_examples=50)
def test_gv_attributelist_instantiation(instance):
    assert isinstance(instance, gv_AttributeList)

@given(instance=gv_Attributable_strategy)
@settings(max_examples=50)
def test_gv_attributable_instantiation(instance):
    assert isinstance(instance, gv_Attributable)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=gv_AttributeStatement_strategy)
@settings(max_examples=50)
def test_gv_attributestatement_instantiation(instance):
    assert isinstance(instance, gv_AttributeStatement)



@given(instance=gv_AttributeStatement_strategy)
def test_gv_attributestatement_context_setter(instance):
    original = instance.context
    instance.context = original
    assert instance.context == original

@given(instance=gv_EdgeStatement_strategy)
@settings(max_examples=50)
def test_gv_edgestatement_instantiation(instance):
    assert isinstance(instance, gv_EdgeStatement)

@given(instance=gv_NodeStatement_strategy)
@settings(max_examples=50)
def test_gv_nodestatement_instantiation(instance):
    assert isinstance(instance, gv_NodeStatement)

@given(instance=gv_AssignmentStatement_strategy)
@settings(max_examples=50)
def test_gv_assignmentstatement_instantiation(instance):
    assert isinstance(instance, gv_AssignmentStatement)



@given(instance=gv_AssignmentStatement_strategy)
def test_gv_assignmentstatement_right_setter(instance):
    original = instance.right
    instance.right = original
    assert instance.right == original



@given(instance=gv_AssignmentStatement_strategy)
def test_gv_assignmentstatement_left_setter(instance):
    original = instance.left
    instance.left = original
    assert instance.left == original
