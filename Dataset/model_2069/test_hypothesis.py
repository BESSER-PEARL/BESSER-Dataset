import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Simpletree_TreeElement,
    TreeElement,
    Simpletree_Folder,
    Simpletree_File,
    Simpletree_Attribute,
    Simpletree_Text,
    Text,
    Simpletree_Node,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_simpletree_treeelement_is_not_abstract():
    assert not inspect.isabstract(Simpletree_TreeElement)


def test_simpletree_treeelement_constructor_exists():
    assert callable(Simpletree_TreeElement.__init__)


def test_simpletree_treeelement_constructor_args():
    sig = inspect.signature(Simpletree_TreeElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "index" in params, "Missing parameter 'index'"

def test_simpletree_treeelement_has_name():
    assert hasattr(Simpletree_TreeElement, "name")
    descriptor = None
    for klass in Simpletree_TreeElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_simpletree_treeelement_has_index():
    assert hasattr(Simpletree_TreeElement, "index")
    descriptor = None
    for klass in Simpletree_TreeElement.__mro__:
        if "index" in klass.__dict__:
            descriptor = klass.__dict__["index"]
            break
    assert isinstance(descriptor, property)



def test_treeelement_is_not_abstract():
    assert not inspect.isabstract(TreeElement)


def test_treeelement_constructor_exists():
    assert callable(TreeElement.__init__)


def test_treeelement_constructor_args():
    sig = inspect.signature(TreeElement.__init__)
    params = list(sig.parameters.keys())



def test_simpletree_folder_is_not_abstract():
    assert not inspect.isabstract(Simpletree_Folder)


def test_simpletree_folder_constructor_exists():
    assert callable(Simpletree_Folder.__init__)


def test_simpletree_folder_constructor_args():
    sig = inspect.signature(Simpletree_Folder.__init__)
    params = list(sig.parameters.keys())



def test_simpletree_file_is_not_abstract():
    assert not inspect.isabstract(Simpletree_File)


def test_simpletree_file_constructor_exists():
    assert callable(Simpletree_File.__init__)


def test_simpletree_file_constructor_args():
    sig = inspect.signature(Simpletree_File.__init__)
    params = list(sig.parameters.keys())



def test_simpletree_attribute_is_not_abstract():
    assert not inspect.isabstract(Simpletree_Attribute)


def test_simpletree_attribute_constructor_exists():
    assert callable(Simpletree_Attribute.__init__)


def test_simpletree_attribute_constructor_args():
    sig = inspect.signature(Simpletree_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_simpletree_attribute_has_value():
    assert hasattr(Simpletree_Attribute, "value")
    descriptor = None
    for klass in Simpletree_Attribute.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_simpletree_text_is_not_abstract():
    assert not inspect.isabstract(Simpletree_Text)


def test_simpletree_text_constructor_exists():
    assert callable(Simpletree_Text.__init__)


def test_simpletree_text_constructor_args():
    sig = inspect.signature(Simpletree_Text.__init__)
    params = list(sig.parameters.keys())



def test_text_is_not_abstract():
    assert not inspect.isabstract(Text)


def test_text_constructor_exists():
    assert callable(Text.__init__)


def test_text_constructor_args():
    sig = inspect.signature(Text.__init__)
    params = list(sig.parameters.keys())



def test_simpletree_node_is_not_abstract():
    assert not inspect.isabstract(Simpletree_Node)


def test_simpletree_node_constructor_exists():
    assert callable(Simpletree_Node.__init__)


def test_simpletree_node_constructor_args():
    sig = inspect.signature(Simpletree_Node.__init__)
    params = list(sig.parameters.keys())
    assert "stopIndex" in params, "Missing parameter 'stopIndex'"
    assert "stopLineIndex" in params, "Missing parameter 'stopLineIndex'"
    assert "startLineIndex" in params, "Missing parameter 'startLineIndex'"
    assert "startIndex" in params, "Missing parameter 'startIndex'"

def test_simpletree_node_has_stopIndex():
    assert hasattr(Simpletree_Node, "stopIndex")
    descriptor = None
    for klass in Simpletree_Node.__mro__:
        if "stopIndex" in klass.__dict__:
            descriptor = klass.__dict__["stopIndex"]
            break
    assert isinstance(descriptor, property)

def test_simpletree_node_has_stopLineIndex():
    assert hasattr(Simpletree_Node, "stopLineIndex")
    descriptor = None
    for klass in Simpletree_Node.__mro__:
        if "stopLineIndex" in klass.__dict__:
            descriptor = klass.__dict__["stopLineIndex"]
            break
    assert isinstance(descriptor, property)

def test_simpletree_node_has_startLineIndex():
    assert hasattr(Simpletree_Node, "startLineIndex")
    descriptor = None
    for klass in Simpletree_Node.__mro__:
        if "startLineIndex" in klass.__dict__:
            descriptor = klass.__dict__["startLineIndex"]
            break
    assert isinstance(descriptor, property)

def test_simpletree_node_has_startIndex():
    assert hasattr(Simpletree_Node, "startIndex")
    descriptor = None
    for klass in Simpletree_Node.__mro__:
        if "startIndex" in klass.__dict__:
            descriptor = klass.__dict__["startIndex"]
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
Simpletree_TreeElement_strategy = st.builds(
    Simpletree_TreeElement,
    name=
        safe_text,
    index=
        st.integers()
)
TreeElement_strategy = st.builds(
    TreeElement,
)
Simpletree_Folder_strategy = st.builds(
    Simpletree_Folder,
)
Simpletree_File_strategy = st.builds(
    Simpletree_File,
)
Simpletree_Attribute_strategy = st.builds(
    Simpletree_Attribute,
    value=
        safe_text
)
Simpletree_Text_strategy = st.builds(
    Simpletree_Text,
)
Text_strategy = st.builds(
    Text,
)
Simpletree_Node_strategy = st.builds(
    Simpletree_Node,
    stopIndex=
        st.integers(),
    stopLineIndex=
        st.integers(),
    startLineIndex=
        st.integers(),
    startIndex=
        st.integers()
)

@given(instance=Simpletree_TreeElement_strategy)
@settings(max_examples=50)
def test_simpletree_treeelement_instantiation(instance):
    assert isinstance(instance, Simpletree_TreeElement)



@given(instance=Simpletree_TreeElement_strategy)
def test_simpletree_treeelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Simpletree_TreeElement_strategy)
def test_simpletree_treeelement_index_setter(instance):
    original = instance.index
    instance.index = original
    assert instance.index == original

@given(instance=TreeElement_strategy)
@settings(max_examples=50)
def test_treeelement_instantiation(instance):
    assert isinstance(instance, TreeElement)

@given(instance=Simpletree_Folder_strategy)
@settings(max_examples=50)
def test_simpletree_folder_instantiation(instance):
    assert isinstance(instance, Simpletree_Folder)

@given(instance=Simpletree_File_strategy)
@settings(max_examples=50)
def test_simpletree_file_instantiation(instance):
    assert isinstance(instance, Simpletree_File)

@given(instance=Simpletree_Attribute_strategy)
@settings(max_examples=50)
def test_simpletree_attribute_instantiation(instance):
    assert isinstance(instance, Simpletree_Attribute)



@given(instance=Simpletree_Attribute_strategy)
def test_simpletree_attribute_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Simpletree_Text_strategy)
@settings(max_examples=50)
def test_simpletree_text_instantiation(instance):
    assert isinstance(instance, Simpletree_Text)

@given(instance=Text_strategy)
@settings(max_examples=50)
def test_text_instantiation(instance):
    assert isinstance(instance, Text)

@given(instance=Simpletree_Node_strategy)
@settings(max_examples=50)
def test_simpletree_node_instantiation(instance):
    assert isinstance(instance, Simpletree_Node)



@given(instance=Simpletree_Node_strategy)
def test_simpletree_node_stopIndex_setter(instance):
    original = instance.stopIndex
    instance.stopIndex = original
    assert instance.stopIndex == original



@given(instance=Simpletree_Node_strategy)
def test_simpletree_node_stopLineIndex_setter(instance):
    original = instance.stopLineIndex
    instance.stopLineIndex = original
    assert instance.stopLineIndex == original



@given(instance=Simpletree_Node_strategy)
def test_simpletree_node_startLineIndex_setter(instance):
    original = instance.startLineIndex
    instance.startLineIndex = original
    assert instance.startLineIndex == original



@given(instance=Simpletree_Node_strategy)
def test_simpletree_node_startIndex_setter(instance):
    original = instance.startIndex
    instance.startIndex = original
    assert instance.startIndex == original
