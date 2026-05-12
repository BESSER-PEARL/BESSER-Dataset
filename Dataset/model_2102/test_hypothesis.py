import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Text,
    SimpleTree_TreeElement,
    SimpleTree_Node,
    TreeElement,
    SimpleTree_File,
    SimpleTree_Folder,
    SimpleTree_Text,
    SimpleTree_Attribute,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_text_is_not_abstract():
    assert not inspect.isabstract(Text)


def test_text_constructor_exists():
    assert callable(Text.__init__)


def test_text_constructor_args():
    sig = inspect.signature(Text.__init__)
    params = list(sig.parameters.keys())



def test_simpletree_treeelement_is_not_abstract():
    assert not inspect.isabstract(SimpleTree_TreeElement)


def test_simpletree_treeelement_constructor_exists():
    assert callable(SimpleTree_TreeElement.__init__)


def test_simpletree_treeelement_constructor_args():
    sig = inspect.signature(SimpleTree_TreeElement.__init__)
    params = list(sig.parameters.keys())
    assert "index" in params, "Missing parameter 'index'"
    assert "name" in params, "Missing parameter 'name'"

def test_simpletree_treeelement_has_index():
    assert hasattr(SimpleTree_TreeElement, "index")
    descriptor = None
    for klass in SimpleTree_TreeElement.__mro__:
        if "index" in klass.__dict__:
            descriptor = klass.__dict__["index"]
            break
    assert isinstance(descriptor, property)

def test_simpletree_treeelement_has_name():
    assert hasattr(SimpleTree_TreeElement, "name")
    descriptor = None
    for klass in SimpleTree_TreeElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simpletree_node_is_not_abstract():
    assert not inspect.isabstract(SimpleTree_Node)


def test_simpletree_node_constructor_exists():
    assert callable(SimpleTree_Node.__init__)


def test_simpletree_node_constructor_args():
    sig = inspect.signature(SimpleTree_Node.__init__)
    params = list(sig.parameters.keys())
    assert "stopLineIndex" in params, "Missing parameter 'stopLineIndex'"
    assert "startIndex" in params, "Missing parameter 'startIndex'"
    assert "startLineIndex" in params, "Missing parameter 'startLineIndex'"
    assert "stopIndex" in params, "Missing parameter 'stopIndex'"

def test_simpletree_node_has_stopLineIndex():
    assert hasattr(SimpleTree_Node, "stopLineIndex")
    descriptor = None
    for klass in SimpleTree_Node.__mro__:
        if "stopLineIndex" in klass.__dict__:
            descriptor = klass.__dict__["stopLineIndex"]
            break
    assert isinstance(descriptor, property)

def test_simpletree_node_has_startIndex():
    assert hasattr(SimpleTree_Node, "startIndex")
    descriptor = None
    for klass in SimpleTree_Node.__mro__:
        if "startIndex" in klass.__dict__:
            descriptor = klass.__dict__["startIndex"]
            break
    assert isinstance(descriptor, property)

def test_simpletree_node_has_startLineIndex():
    assert hasattr(SimpleTree_Node, "startLineIndex")
    descriptor = None
    for klass in SimpleTree_Node.__mro__:
        if "startLineIndex" in klass.__dict__:
            descriptor = klass.__dict__["startLineIndex"]
            break
    assert isinstance(descriptor, property)

def test_simpletree_node_has_stopIndex():
    assert hasattr(SimpleTree_Node, "stopIndex")
    descriptor = None
    for klass in SimpleTree_Node.__mro__:
        if "stopIndex" in klass.__dict__:
            descriptor = klass.__dict__["stopIndex"]
            break
    assert isinstance(descriptor, property)



def test_treeelement_is_not_abstract():
    assert not inspect.isabstract(TreeElement)


def test_treeelement_constructor_exists():
    assert callable(TreeElement.__init__)


def test_treeelement_constructor_args():
    sig = inspect.signature(TreeElement.__init__)
    params = list(sig.parameters.keys())



def test_simpletree_file_is_not_abstract():
    assert not inspect.isabstract(SimpleTree_File)


def test_simpletree_file_constructor_exists():
    assert callable(SimpleTree_File.__init__)


def test_simpletree_file_constructor_args():
    sig = inspect.signature(SimpleTree_File.__init__)
    params = list(sig.parameters.keys())



def test_simpletree_folder_is_not_abstract():
    assert not inspect.isabstract(SimpleTree_Folder)


def test_simpletree_folder_constructor_exists():
    assert callable(SimpleTree_Folder.__init__)


def test_simpletree_folder_constructor_args():
    sig = inspect.signature(SimpleTree_Folder.__init__)
    params = list(sig.parameters.keys())



def test_simpletree_text_is_not_abstract():
    assert not inspect.isabstract(SimpleTree_Text)


def test_simpletree_text_constructor_exists():
    assert callable(SimpleTree_Text.__init__)


def test_simpletree_text_constructor_args():
    sig = inspect.signature(SimpleTree_Text.__init__)
    params = list(sig.parameters.keys())



def test_simpletree_attribute_is_not_abstract():
    assert not inspect.isabstract(SimpleTree_Attribute)


def test_simpletree_attribute_constructor_exists():
    assert callable(SimpleTree_Attribute.__init__)


def test_simpletree_attribute_constructor_args():
    sig = inspect.signature(SimpleTree_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_simpletree_attribute_has_value():
    assert hasattr(SimpleTree_Attribute, "value")
    descriptor = None
    for klass in SimpleTree_Attribute.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
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
Text_strategy = st.builds(
    Text,
)
SimpleTree_TreeElement_strategy = st.builds(
    SimpleTree_TreeElement,
    index=
        st.integers(),
    name=
        safe_text
)
SimpleTree_Node_strategy = st.builds(
    SimpleTree_Node,
    stopLineIndex=
        st.integers(),
    startIndex=
        st.integers(),
    startLineIndex=
        st.integers(),
    stopIndex=
        st.integers()
)
TreeElement_strategy = st.builds(
    TreeElement,
)
SimpleTree_File_strategy = st.builds(
    SimpleTree_File,
)
SimpleTree_Folder_strategy = st.builds(
    SimpleTree_Folder,
)
SimpleTree_Text_strategy = st.builds(
    SimpleTree_Text,
)
SimpleTree_Attribute_strategy = st.builds(
    SimpleTree_Attribute,
    value=
        safe_text
)

@given(instance=Text_strategy)
@settings(max_examples=50)
def test_text_instantiation(instance):
    assert isinstance(instance, Text)

@given(instance=SimpleTree_TreeElement_strategy)
@settings(max_examples=50)
def test_simpletree_treeelement_instantiation(instance):
    assert isinstance(instance, SimpleTree_TreeElement)



@given(instance=SimpleTree_TreeElement_strategy)
def test_simpletree_treeelement_index_setter(instance):
    original = instance.index
    instance.index = original
    assert instance.index == original



@given(instance=SimpleTree_TreeElement_strategy)
def test_simpletree_treeelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SimpleTree_Node_strategy)
@settings(max_examples=50)
def test_simpletree_node_instantiation(instance):
    assert isinstance(instance, SimpleTree_Node)



@given(instance=SimpleTree_Node_strategy)
def test_simpletree_node_stopLineIndex_setter(instance):
    original = instance.stopLineIndex
    instance.stopLineIndex = original
    assert instance.stopLineIndex == original



@given(instance=SimpleTree_Node_strategy)
def test_simpletree_node_startIndex_setter(instance):
    original = instance.startIndex
    instance.startIndex = original
    assert instance.startIndex == original



@given(instance=SimpleTree_Node_strategy)
def test_simpletree_node_startLineIndex_setter(instance):
    original = instance.startLineIndex
    instance.startLineIndex = original
    assert instance.startLineIndex == original



@given(instance=SimpleTree_Node_strategy)
def test_simpletree_node_stopIndex_setter(instance):
    original = instance.stopIndex
    instance.stopIndex = original
    assert instance.stopIndex == original

@given(instance=TreeElement_strategy)
@settings(max_examples=50)
def test_treeelement_instantiation(instance):
    assert isinstance(instance, TreeElement)

@given(instance=SimpleTree_File_strategy)
@settings(max_examples=50)
def test_simpletree_file_instantiation(instance):
    assert isinstance(instance, SimpleTree_File)

@given(instance=SimpleTree_Folder_strategy)
@settings(max_examples=50)
def test_simpletree_folder_instantiation(instance):
    assert isinstance(instance, SimpleTree_Folder)

@given(instance=SimpleTree_Text_strategy)
@settings(max_examples=50)
def test_simpletree_text_instantiation(instance):
    assert isinstance(instance, SimpleTree_Text)

@given(instance=SimpleTree_Attribute_strategy)
@settings(max_examples=50)
def test_simpletree_attribute_instantiation(instance):
    assert isinstance(instance, SimpleTree_Attribute)



@given(instance=SimpleTree_Attribute_strategy)
def test_simpletree_attribute_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original
