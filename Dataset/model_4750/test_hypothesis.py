import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ed2::Model,
    ed2::ED2,
    ed2::EDD,
    TreeElement,
    ed2::Leaf,
    ed2::Node,
    ed2::TreeElement,
    ed2::TreeParent,
    ed2::TreeObject,
    TreeElementType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ed2::model_is_not_abstract():
    assert not inspect.isabstract(ed2::Model)


def test_ed2::model_constructor_exists():
    assert callable(ed2::Model.__init__)


def test_ed2::model_constructor_args():
    sig = inspect.signature(ed2::Model.__init__)
    params = list(sig.parameters.keys())



def test_ed2::ed2_is_not_abstract():
    assert not inspect.isabstract(ed2::ED2)


def test_ed2::ed2_constructor_exists():
    assert callable(ed2::ED2.__init__)


def test_ed2::ed2_constructor_args():
    sig = inspect.signature(ed2::ED2.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ed2::ed2_has_name():
    assert hasattr(ed2::ED2, "name")
    descriptor = None
    for klass in ed2::ED2.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ed2::edd_is_not_abstract():
    assert not inspect.isabstract(ed2::EDD)


def test_ed2::edd_constructor_exists():
    assert callable(ed2::EDD.__init__)


def test_ed2::edd_constructor_args():
    sig = inspect.signature(ed2::EDD.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ed2::edd_has_name():
    assert hasattr(ed2::EDD, "name")
    descriptor = None
    for klass in ed2::EDD.__mro__:
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



def test_ed2::leaf_is_not_abstract():
    assert not inspect.isabstract(ed2::Leaf)


def test_ed2::leaf_constructor_exists():
    assert callable(ed2::Leaf.__init__)


def test_ed2::leaf_constructor_args():
    sig = inspect.signature(ed2::Leaf.__init__)
    params = list(sig.parameters.keys())



def test_ed2::node_is_not_abstract():
    assert not inspect.isabstract(ed2::Node)


def test_ed2::node_constructor_exists():
    assert callable(ed2::Node.__init__)


def test_ed2::node_constructor_args():
    sig = inspect.signature(ed2::Node.__init__)
    params = list(sig.parameters.keys())



def test_ed2::treeelement_is_not_abstract():
    assert not inspect.isabstract(ed2::TreeElement)


def test_ed2::treeelement_constructor_exists():
    assert callable(ed2::TreeElement.__init__)


def test_ed2::treeelement_constructor_args():
    sig = inspect.signature(ed2::TreeElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "index" in params, "Missing parameter 'index'"
    assert "type" in params, "Missing parameter 'type'"

def test_ed2::treeelement_has_name():
    assert hasattr(ed2::TreeElement, "name")
    descriptor = None
    for klass in ed2::TreeElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ed2::treeelement_has_index():
    assert hasattr(ed2::TreeElement, "index")
    descriptor = None
    for klass in ed2::TreeElement.__mro__:
        if "index" in klass.__dict__:
            descriptor = klass.__dict__["index"]
            break
    assert isinstance(descriptor, property)

def test_ed2::treeelement_has_type():
    assert hasattr(ed2::TreeElement, "type")
    descriptor = None
    for klass in ed2::TreeElement.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_ed2::treeparent_is_not_abstract():
    assert not inspect.isabstract(ed2::TreeParent)


def test_ed2::treeparent_constructor_exists():
    assert callable(ed2::TreeParent.__init__)


def test_ed2::treeparent_constructor_args():
    sig = inspect.signature(ed2::TreeParent.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "index" in params, "Missing parameter 'index'"
    assert "type" in params, "Missing parameter 'type'"

def test_ed2::treeparent_has_name():
    assert hasattr(ed2::TreeParent, "name")
    descriptor = None
    for klass in ed2::TreeParent.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ed2::treeparent_has_index():
    assert hasattr(ed2::TreeParent, "index")
    descriptor = None
    for klass in ed2::TreeParent.__mro__:
        if "index" in klass.__dict__:
            descriptor = klass.__dict__["index"]
            break
    assert isinstance(descriptor, property)

def test_ed2::treeparent_has_type():
    assert hasattr(ed2::TreeParent, "type")
    descriptor = None
    for klass in ed2::TreeParent.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_ed2::treeobject_is_not_abstract():
    assert not inspect.isabstract(ed2::TreeObject)


def test_ed2::treeobject_constructor_exists():
    assert callable(ed2::TreeObject.__init__)


def test_ed2::treeobject_constructor_args():
    sig = inspect.signature(ed2::TreeObject.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"
    assert "index" in params, "Missing parameter 'index'"

def test_ed2::treeobject_has_name():
    assert hasattr(ed2::TreeObject, "name")
    descriptor = None
    for klass in ed2::TreeObject.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ed2::treeobject_has_type():
    assert hasattr(ed2::TreeObject, "type")
    descriptor = None
    for klass in ed2::TreeObject.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_ed2::treeobject_has_index():
    assert hasattr(ed2::TreeObject, "index")
    descriptor = None
    for klass in ed2::TreeObject.__mro__:
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
        "yes",
        "dont_know",
        "empty",
        "inadmissible",
        "no",
        "trusted",
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
ed2::Model_strategy = st.builds(
    ed2::Model,
)
ed2::ED2_strategy = st.builds(
    ed2::ED2,
    name=
        safe_text
)
ed2::EDD_strategy = st.builds(
    ed2::EDD,
    name=
        safe_text
)
TreeElement_strategy = st.builds(
    TreeElement,
)
ed2::Leaf_strategy = st.builds(
    ed2::Leaf,
)
ed2::Node_strategy = st.builds(
    ed2::Node,
)
ed2::TreeElement_strategy = st.builds(
    ed2::TreeElement,
    name=
        safe_text,
    index=
        safe_text,
    type=
        safe_text
)
ed2::TreeParent_strategy = st.builds(
    ed2::TreeParent,
    name=
        safe_text,
    index=
        safe_text,
    type=
        safe_text
)
ed2::TreeObject_strategy = st.builds(
    ed2::TreeObject,
    name=
        safe_text,
    type=
        safe_text,
    index=
        safe_text
)

@given(instance=ed2::Model_strategy)
@settings(max_examples=50)
def test_ed2::model_instantiation(instance):
    assert isinstance(instance, ed2::Model)

@given(instance=ed2::ED2_strategy)
@settings(max_examples=50)
def test_ed2::ed2_instantiation(instance):
    assert isinstance(instance, ed2::ED2)

@given(instance=ed2::ED2_strategy)
def test_ed2::ed2_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ed2::ED2_strategy)
def test_ed2::ed2_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ed2::EDD_strategy)
@settings(max_examples=50)
def test_ed2::edd_instantiation(instance):
    assert isinstance(instance, ed2::EDD)

@given(instance=ed2::EDD_strategy)
def test_ed2::edd_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ed2::EDD_strategy)
def test_ed2::edd_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=TreeElement_strategy)
@settings(max_examples=50)
def test_treeelement_instantiation(instance):
    assert isinstance(instance, TreeElement)

@given(instance=ed2::Leaf_strategy)
@settings(max_examples=50)
def test_ed2::leaf_instantiation(instance):
    assert isinstance(instance, ed2::Leaf)

@given(instance=ed2::Node_strategy)
@settings(max_examples=50)
def test_ed2::node_instantiation(instance):
    assert isinstance(instance, ed2::Node)

@given(instance=ed2::TreeElement_strategy)
@settings(max_examples=50)
def test_ed2::treeelement_instantiation(instance):
    assert isinstance(instance, ed2::TreeElement)

@given(instance=ed2::TreeElement_strategy)
def test_ed2::treeelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ed2::TreeElement_strategy)
def test_ed2::treeelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ed2::TreeElement_strategy)
def test_ed2::treeelement_index_type(instance):
    assert isinstance(instance.index, str)


@given(instance=ed2::TreeElement_strategy)
def test_ed2::treeelement_index_setter(instance):
    original = instance.index
    instance.index = original
    assert instance.index == original

@given(instance=ed2::TreeElement_strategy)
def test_ed2::treeelement_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=ed2::TreeElement_strategy)
def test_ed2::treeelement_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=ed2::TreeParent_strategy)
@settings(max_examples=50)
def test_ed2::treeparent_instantiation(instance):
    assert isinstance(instance, ed2::TreeParent)

@given(instance=ed2::TreeParent_strategy)
def test_ed2::treeparent_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ed2::TreeParent_strategy)
def test_ed2::treeparent_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ed2::TreeParent_strategy)
def test_ed2::treeparent_index_type(instance):
    assert isinstance(instance.index, str)


@given(instance=ed2::TreeParent_strategy)
def test_ed2::treeparent_index_setter(instance):
    original = instance.index
    instance.index = original
    assert instance.index == original

@given(instance=ed2::TreeParent_strategy)
def test_ed2::treeparent_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=ed2::TreeParent_strategy)
def test_ed2::treeparent_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=ed2::TreeObject_strategy)
@settings(max_examples=50)
def test_ed2::treeobject_instantiation(instance):
    assert isinstance(instance, ed2::TreeObject)

@given(instance=ed2::TreeObject_strategy)
def test_ed2::treeobject_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ed2::TreeObject_strategy)
def test_ed2::treeobject_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ed2::TreeObject_strategy)
def test_ed2::treeobject_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=ed2::TreeObject_strategy)
def test_ed2::treeobject_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=ed2::TreeObject_strategy)
def test_ed2::treeobject_index_type(instance):
    assert isinstance(instance.index, str)


@given(instance=ed2::TreeObject_strategy)
def test_ed2::treeobject_index_setter(instance):
    original = instance.index
    instance.index = original
    assert instance.index == original
