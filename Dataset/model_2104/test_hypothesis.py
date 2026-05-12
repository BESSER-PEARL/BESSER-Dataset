import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Text,
    MocaTree_TreeElement,
    MocaTree_Node,
    TreeElement,
    MocaTree_File,
    MocaTree_Link,
    MocaTree_Text,
    MocaTree_Folder,
    MocaTree_Attribute,
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



def test_mocatree_treeelement_is_not_abstract():
    assert not inspect.isabstract(MocaTree_TreeElement)


def test_mocatree_treeelement_constructor_exists():
    assert callable(MocaTree_TreeElement.__init__)


def test_mocatree_treeelement_constructor_args():
    sig = inspect.signature(MocaTree_TreeElement.__init__)
    params = list(sig.parameters.keys())
    assert "index" in params, "Missing parameter 'index'"
    assert "name" in params, "Missing parameter 'name'"

def test_mocatree_treeelement_has_index():
    assert hasattr(MocaTree_TreeElement, "index")
    descriptor = None
    for klass in MocaTree_TreeElement.__mro__:
        if "index" in klass.__dict__:
            descriptor = klass.__dict__["index"]
            break
    assert isinstance(descriptor, property)

def test_mocatree_treeelement_has_name():
    assert hasattr(MocaTree_TreeElement, "name")
    descriptor = None
    for klass in MocaTree_TreeElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mocatree_node_is_not_abstract():
    assert not inspect.isabstract(MocaTree_Node)


def test_mocatree_node_constructor_exists():
    assert callable(MocaTree_Node.__init__)


def test_mocatree_node_constructor_args():
    sig = inspect.signature(MocaTree_Node.__init__)
    params = list(sig.parameters.keys())
    assert "startLineIndex" in params, "Missing parameter 'startLineIndex'"
    assert "stopLineIndex" in params, "Missing parameter 'stopLineIndex'"
    assert "startIndex" in params, "Missing parameter 'startIndex'"
    assert "stopIndex" in params, "Missing parameter 'stopIndex'"

def test_mocatree_node_has_startLineIndex():
    assert hasattr(MocaTree_Node, "startLineIndex")
    descriptor = None
    for klass in MocaTree_Node.__mro__:
        if "startLineIndex" in klass.__dict__:
            descriptor = klass.__dict__["startLineIndex"]
            break
    assert isinstance(descriptor, property)

def test_mocatree_node_has_stopLineIndex():
    assert hasattr(MocaTree_Node, "stopLineIndex")
    descriptor = None
    for klass in MocaTree_Node.__mro__:
        if "stopLineIndex" in klass.__dict__:
            descriptor = klass.__dict__["stopLineIndex"]
            break
    assert isinstance(descriptor, property)

def test_mocatree_node_has_startIndex():
    assert hasattr(MocaTree_Node, "startIndex")
    descriptor = None
    for klass in MocaTree_Node.__mro__:
        if "startIndex" in klass.__dict__:
            descriptor = klass.__dict__["startIndex"]
            break
    assert isinstance(descriptor, property)

def test_mocatree_node_has_stopIndex():
    assert hasattr(MocaTree_Node, "stopIndex")
    descriptor = None
    for klass in MocaTree_Node.__mro__:
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



def test_mocatree_file_is_not_abstract():
    assert not inspect.isabstract(MocaTree_File)


def test_mocatree_file_constructor_exists():
    assert callable(MocaTree_File.__init__)


def test_mocatree_file_constructor_args():
    sig = inspect.signature(MocaTree_File.__init__)
    params = list(sig.parameters.keys())



def test_mocatree_link_is_not_abstract():
    assert not inspect.isabstract(MocaTree_Link)


def test_mocatree_link_constructor_exists():
    assert callable(MocaTree_Link.__init__)


def test_mocatree_link_constructor_args():
    sig = inspect.signature(MocaTree_Link.__init__)
    params = list(sig.parameters.keys())



def test_mocatree_text_is_not_abstract():
    assert not inspect.isabstract(MocaTree_Text)


def test_mocatree_text_constructor_exists():
    assert callable(MocaTree_Text.__init__)


def test_mocatree_text_constructor_args():
    sig = inspect.signature(MocaTree_Text.__init__)
    params = list(sig.parameters.keys())



def test_mocatree_folder_is_not_abstract():
    assert not inspect.isabstract(MocaTree_Folder)


def test_mocatree_folder_constructor_exists():
    assert callable(MocaTree_Folder.__init__)


def test_mocatree_folder_constructor_args():
    sig = inspect.signature(MocaTree_Folder.__init__)
    params = list(sig.parameters.keys())



def test_mocatree_attribute_is_not_abstract():
    assert not inspect.isabstract(MocaTree_Attribute)


def test_mocatree_attribute_constructor_exists():
    assert callable(MocaTree_Attribute.__init__)


def test_mocatree_attribute_constructor_args():
    sig = inspect.signature(MocaTree_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_mocatree_attribute_has_value():
    assert hasattr(MocaTree_Attribute, "value")
    descriptor = None
    for klass in MocaTree_Attribute.__mro__:
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
MocaTree_TreeElement_strategy = st.builds(
    MocaTree_TreeElement,
    index=
        st.integers(),
    name=
        safe_text
)
MocaTree_Node_strategy = st.builds(
    MocaTree_Node,
    startLineIndex=
        st.integers(),
    stopLineIndex=
        st.integers(),
    startIndex=
        st.integers(),
    stopIndex=
        st.integers()
)
TreeElement_strategy = st.builds(
    TreeElement,
)
MocaTree_File_strategy = st.builds(
    MocaTree_File,
)
MocaTree_Link_strategy = st.builds(
    MocaTree_Link,
)
MocaTree_Text_strategy = st.builds(
    MocaTree_Text,
)
MocaTree_Folder_strategy = st.builds(
    MocaTree_Folder,
)
MocaTree_Attribute_strategy = st.builds(
    MocaTree_Attribute,
    value=
        safe_text
)

@given(instance=Text_strategy)
@settings(max_examples=50)
def test_text_instantiation(instance):
    assert isinstance(instance, Text)

@given(instance=MocaTree_TreeElement_strategy)
@settings(max_examples=50)
def test_mocatree_treeelement_instantiation(instance):
    assert isinstance(instance, MocaTree_TreeElement)



@given(instance=MocaTree_TreeElement_strategy)
def test_mocatree_treeelement_index_setter(instance):
    original = instance.index
    instance.index = original
    assert instance.index == original



@given(instance=MocaTree_TreeElement_strategy)
def test_mocatree_treeelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MocaTree_Node_strategy)
@settings(max_examples=50)
def test_mocatree_node_instantiation(instance):
    assert isinstance(instance, MocaTree_Node)



@given(instance=MocaTree_Node_strategy)
def test_mocatree_node_startLineIndex_setter(instance):
    original = instance.startLineIndex
    instance.startLineIndex = original
    assert instance.startLineIndex == original



@given(instance=MocaTree_Node_strategy)
def test_mocatree_node_stopLineIndex_setter(instance):
    original = instance.stopLineIndex
    instance.stopLineIndex = original
    assert instance.stopLineIndex == original



@given(instance=MocaTree_Node_strategy)
def test_mocatree_node_startIndex_setter(instance):
    original = instance.startIndex
    instance.startIndex = original
    assert instance.startIndex == original



@given(instance=MocaTree_Node_strategy)
def test_mocatree_node_stopIndex_setter(instance):
    original = instance.stopIndex
    instance.stopIndex = original
    assert instance.stopIndex == original

@given(instance=TreeElement_strategy)
@settings(max_examples=50)
def test_treeelement_instantiation(instance):
    assert isinstance(instance, TreeElement)

@given(instance=MocaTree_File_strategy)
@settings(max_examples=50)
def test_mocatree_file_instantiation(instance):
    assert isinstance(instance, MocaTree_File)

@given(instance=MocaTree_Link_strategy)
@settings(max_examples=50)
def test_mocatree_link_instantiation(instance):
    assert isinstance(instance, MocaTree_Link)

@given(instance=MocaTree_Text_strategy)
@settings(max_examples=50)
def test_mocatree_text_instantiation(instance):
    assert isinstance(instance, MocaTree_Text)

@given(instance=MocaTree_Folder_strategy)
@settings(max_examples=50)
def test_mocatree_folder_instantiation(instance):
    assert isinstance(instance, MocaTree_Folder)

@given(instance=MocaTree_Attribute_strategy)
@settings(max_examples=50)
def test_mocatree_attribute_instantiation(instance):
    assert isinstance(instance, MocaTree_Attribute)



@given(instance=MocaTree_Attribute_strategy)
def test_mocatree_attribute_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original
