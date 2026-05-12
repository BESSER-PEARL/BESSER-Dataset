import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ed2_Model,
    ed2_ED2,
    ed2_EDD,
    TreeElement,
    ed2_Leaf,
    ed2_Node,
    ed2_TreeElement,
    ed2_TreeParent,
    ed2_TreeObject,
    TreeElementType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ed2_model_is_not_abstract():
    assert not inspect.isabstract(ed2_Model)


def test_ed2_model_constructor_exists():
    assert callable(ed2_Model.__init__)


def test_ed2_model_constructor_args():
    sig = inspect.signature(ed2_Model.__init__)
    params = list(sig.parameters.keys())



def test_ed2_ed2_is_not_abstract():
    assert not inspect.isabstract(ed2_ED2)


def test_ed2_ed2_constructor_exists():
    assert callable(ed2_ED2.__init__)


def test_ed2_ed2_constructor_args():
    sig = inspect.signature(ed2_ED2.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ed2_ed2_has_name():
    assert hasattr(ed2_ED2, "name")
    descriptor = None
    for klass in ed2_ED2.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ed2_edd_is_not_abstract():
    assert not inspect.isabstract(ed2_EDD)


def test_ed2_edd_constructor_exists():
    assert callable(ed2_EDD.__init__)


def test_ed2_edd_constructor_args():
    sig = inspect.signature(ed2_EDD.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ed2_edd_has_name():
    assert hasattr(ed2_EDD, "name")
    descriptor = None
    for klass in ed2_EDD.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_treeelement_is_not_abstract():
    assert not inspect.isabstract(TreeElement)


def test_treeelement_constructor_exists():
    assert callable(TreeElement.__init__)


def test_treeelement_constructor_args():
    sig = inspect.signature(TreeElement.__init__)
    params = list(sig.parameters.keys())



def test_ed2_leaf_is_not_abstract():
    assert not inspect.isabstract(ed2_Leaf)


def test_ed2_leaf_constructor_exists():
    assert callable(ed2_Leaf.__init__)


def test_ed2_leaf_constructor_args():
    sig = inspect.signature(ed2_Leaf.__init__)
    params = list(sig.parameters.keys())



def test_ed2_node_is_not_abstract():
    assert not inspect.isabstract(ed2_Node)


def test_ed2_node_constructor_exists():
    assert callable(ed2_Node.__init__)


def test_ed2_node_constructor_args():
    sig = inspect.signature(ed2_Node.__init__)
    params = list(sig.parameters.keys())



def test_ed2_treeelement_is_not_abstract():
    assert not inspect.isabstract(ed2_TreeElement)


def test_ed2_treeelement_constructor_exists():
    assert callable(ed2_TreeElement.__init__)


def test_ed2_treeelement_constructor_args():
    sig = inspect.signature(ed2_TreeElement.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "index" in params, "Missing parameter 'index'"
    assert "name" in params, "Missing parameter 'name'"

def test_ed2_treeelement_has_type():
    assert hasattr(ed2_TreeElement, "type")
    descriptor = None
    for klass in ed2_TreeElement.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_ed2_treeelement_has_index():
    assert hasattr(ed2_TreeElement, "index")
    descriptor = None
    for klass in ed2_TreeElement.__mro__:
        if "index" in klass.__dict__:
            descriptor = klass.__dict__["index"]
            break
    assert isinstance(descriptor, property)

def test_ed2_treeelement_has_name():
    assert hasattr(ed2_TreeElement, "name")
    descriptor = None
    for klass in ed2_TreeElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ed2_treeparent_is_not_abstract():
    assert not inspect.isabstract(ed2_TreeParent)


def test_ed2_treeparent_constructor_exists():
    assert callable(ed2_TreeParent.__init__)


def test_ed2_treeparent_constructor_args():
    sig = inspect.signature(ed2_TreeParent.__init__)
    params = list(sig.parameters.keys())
    assert "index" in params, "Missing parameter 'index'"
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_ed2_treeparent_has_index():
    assert hasattr(ed2_TreeParent, "index")
    descriptor = None
    for klass in ed2_TreeParent.__mro__:
        if "index" in klass.__dict__:
            descriptor = klass.__dict__["index"]
            break
    assert isinstance(descriptor, property)

def test_ed2_treeparent_has_type():
    assert hasattr(ed2_TreeParent, "type")
    descriptor = None
    for klass in ed2_TreeParent.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_ed2_treeparent_has_name():
    assert hasattr(ed2_TreeParent, "name")
    descriptor = None
    for klass in ed2_TreeParent.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ed2_treeobject_is_not_abstract():
    assert not inspect.isabstract(ed2_TreeObject)


def test_ed2_treeobject_constructor_exists():
    assert callable(ed2_TreeObject.__init__)


def test_ed2_treeobject_constructor_args():
    sig = inspect.signature(ed2_TreeObject.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"
    assert "index" in params, "Missing parameter 'index'"

def test_ed2_treeobject_has_name():
    assert hasattr(ed2_TreeObject, "name")
    descriptor = None
    for klass in ed2_TreeObject.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ed2_treeobject_has_type():
    assert hasattr(ed2_TreeObject, "type")
    descriptor = None
    for klass in ed2_TreeObject.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_ed2_treeobject_has_index():
    assert hasattr(ed2_TreeObject, "index")
    descriptor = None
    for klass in ed2_TreeObject.__mro__:
        if "index" in klass.__dict__:
            descriptor = klass.__dict__["index"]
            break
    assert isinstance(descriptor, property)

def test_treeelementtype_exists():
    # Check that the Enumeration exists
    assert TreeElementType is not None

def test_treeelementtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TreeElementType]
    expected_literals = [
        "dont_know",
        "yes",
        "no",
        "trusted",
        "empty",
        "inadmissible",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TreeElementType"


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
ed2_Model_strategy = st.builds(
    ed2_Model,
)
ed2_ED2_strategy = st.builds(
    ed2_ED2,
    name=
        safe_text
)
ed2_EDD_strategy = st.builds(
    ed2_EDD,
    name=
        safe_text
)
TreeElement_strategy = st.builds(
    TreeElement,
)
ed2_Leaf_strategy = st.builds(
    ed2_Leaf,
)
ed2_Node_strategy = st.builds(
    ed2_Node,
)
ed2_TreeElement_strategy = st.builds(
    ed2_TreeElement,
    type=
        safe_text,
    index=
        safe_text,
    name=
        safe_text
)
ed2_TreeParent_strategy = st.builds(
    ed2_TreeParent,
    index=
        safe_text,
    type=
        safe_text,
    name=
        safe_text
)
ed2_TreeObject_strategy = st.builds(
    ed2_TreeObject,
    name=
        safe_text,
    type=
        safe_text,
    index=
        safe_text
)

@given(instance=ed2_Model_strategy)
@settings(max_examples=50)
def test_ed2_model_instantiation(instance):
    assert isinstance(instance, ed2_Model)

@given(instance=ed2_ED2_strategy)
@settings(max_examples=50)
def test_ed2_ed2_instantiation(instance):
    assert isinstance(instance, ed2_ED2)



@given(instance=ed2_ED2_strategy)
def test_ed2_ed2_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ed2_EDD_strategy)
@settings(max_examples=50)
def test_ed2_edd_instantiation(instance):
    assert isinstance(instance, ed2_EDD)



@given(instance=ed2_EDD_strategy)
def test_ed2_edd_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=TreeElement_strategy)
@settings(max_examples=50)
def test_treeelement_instantiation(instance):
    assert isinstance(instance, TreeElement)

@given(instance=ed2_Leaf_strategy)
@settings(max_examples=50)
def test_ed2_leaf_instantiation(instance):
    assert isinstance(instance, ed2_Leaf)

@given(instance=ed2_Node_strategy)
@settings(max_examples=50)
def test_ed2_node_instantiation(instance):
    assert isinstance(instance, ed2_Node)

@given(instance=ed2_TreeElement_strategy)
@settings(max_examples=50)
def test_ed2_treeelement_instantiation(instance):
    assert isinstance(instance, ed2_TreeElement)



@given(instance=ed2_TreeElement_strategy)
def test_ed2_treeelement_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=ed2_TreeElement_strategy)
def test_ed2_treeelement_index_setter(instance):
    original = instance.index
    instance.index = original
    assert instance.index == original



@given(instance=ed2_TreeElement_strategy)
def test_ed2_treeelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ed2_TreeParent_strategy)
@settings(max_examples=50)
def test_ed2_treeparent_instantiation(instance):
    assert isinstance(instance, ed2_TreeParent)



@given(instance=ed2_TreeParent_strategy)
def test_ed2_treeparent_index_setter(instance):
    original = instance.index
    instance.index = original
    assert instance.index == original



@given(instance=ed2_TreeParent_strategy)
def test_ed2_treeparent_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=ed2_TreeParent_strategy)
def test_ed2_treeparent_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ed2_TreeObject_strategy)
@settings(max_examples=50)
def test_ed2_treeobject_instantiation(instance):
    assert isinstance(instance, ed2_TreeObject)



@given(instance=ed2_TreeObject_strategy)
def test_ed2_treeobject_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=ed2_TreeObject_strategy)
def test_ed2_treeobject_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=ed2_TreeObject_strategy)
def test_ed2_treeobject_index_setter(instance):
    original = instance.index
    instance.index = original
    assert instance.index == original
