import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Text,
    SimpleTree::TreeElement,
    SimpleTree::Node,
    TreeElement,
    SimpleTree::Text,
    SimpleTree::File,
    SimpleTree::Folder,
    SimpleTree::Attribute,
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



def test_simpletree::treeelement_is_not_abstract():
    assert not inspect.isabstract(SimpleTree::TreeElement)


def test_simpletree::treeelement_constructor_exists():
    assert callable(SimpleTree::TreeElement.__init__)


def test_simpletree::treeelement_constructor_args():
    sig = inspect.signature(SimpleTree::TreeElement.__init__)
    params = list(sig.parameters.keys())
    assert "index" in params, "Missing parameter 'index'"
    assert "name" in params, "Missing parameter 'name'"

def test_simpletree::treeelement_has_index():
    assert hasattr(SimpleTree::TreeElement, "index")
    descriptor = None
    for klass in SimpleTree::TreeElement.__mro__:
        if "index" in klass.__dict__:
            descriptor = klass.__dict__["index"]
            break
    assert isinstance(descriptor, property)

def test_simpletree::treeelement_has_name():
    assert hasattr(SimpleTree::TreeElement, "name")
    descriptor = None
    for klass in SimpleTree::TreeElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simpletree::node_is_not_abstract():
    assert not inspect.isabstract(SimpleTree::Node)


def test_simpletree::node_constructor_exists():
    assert callable(SimpleTree::Node.__init__)


def test_simpletree::node_constructor_args():
    sig = inspect.signature(SimpleTree::Node.__init__)
    params = list(sig.parameters.keys())
    assert "stopLineIndex" in params, "Missing parameter 'stopLineIndex'"
    assert "startLineIndex" in params, "Missing parameter 'startLineIndex'"
    assert "stopIndex" in params, "Missing parameter 'stopIndex'"
    assert "startIndex" in params, "Missing parameter 'startIndex'"

def test_simpletree::node_has_stopLineIndex():
    assert hasattr(SimpleTree::Node, "stopLineIndex")
    descriptor = None
    for klass in SimpleTree::Node.__mro__:
        if "stopLineIndex" in klass.__dict__:
            descriptor = klass.__dict__["stopLineIndex"]
            break
    assert isinstance(descriptor, property)

def test_simpletree::node_has_startLineIndex():
    assert hasattr(SimpleTree::Node, "startLineIndex")
    descriptor = None
    for klass in SimpleTree::Node.__mro__:
        if "startLineIndex" in klass.__dict__:
            descriptor = klass.__dict__["startLineIndex"]
            break
    assert isinstance(descriptor, property)

def test_simpletree::node_has_stopIndex():
    assert hasattr(SimpleTree::Node, "stopIndex")
    descriptor = None
    for klass in SimpleTree::Node.__mro__:
        if "stopIndex" in klass.__dict__:
            descriptor = klass.__dict__["stopIndex"]
            break
    assert isinstance(descriptor, property)

def test_simpletree::node_has_startIndex():
    assert hasattr(SimpleTree::Node, "startIndex")
    descriptor = None
    for klass in SimpleTree::Node.__mro__:
        if "startIndex" in klass.__dict__:
            descriptor = klass.__dict__["startIndex"]
            break
    assert isinstance(descriptor, property)



def test_treeelement_is_not_abstract():
    assert not inspect.isabstract(TreeElement)


def test_treeelement_constructor_exists():
    assert callable(TreeElement.__init__)


def test_treeelement_constructor_args():
    sig = inspect.signature(TreeElement.__init__)
    params = list(sig.parameters.keys())



def test_simpletree::text_is_not_abstract():
    assert not inspect.isabstract(SimpleTree::Text)


def test_simpletree::text_constructor_exists():
    assert callable(SimpleTree::Text.__init__)


def test_simpletree::text_constructor_args():
    sig = inspect.signature(SimpleTree::Text.__init__)
    params = list(sig.parameters.keys())



def test_simpletree::file_is_not_abstract():
    assert not inspect.isabstract(SimpleTree::File)


def test_simpletree::file_constructor_exists():
    assert callable(SimpleTree::File.__init__)


def test_simpletree::file_constructor_args():
    sig = inspect.signature(SimpleTree::File.__init__)
    params = list(sig.parameters.keys())



def test_simpletree::folder_is_not_abstract():
    assert not inspect.isabstract(SimpleTree::Folder)


def test_simpletree::folder_constructor_exists():
    assert callable(SimpleTree::Folder.__init__)


def test_simpletree::folder_constructor_args():
    sig = inspect.signature(SimpleTree::Folder.__init__)
    params = list(sig.parameters.keys())



def test_simpletree::attribute_is_not_abstract():
    assert not inspect.isabstract(SimpleTree::Attribute)


def test_simpletree::attribute_constructor_exists():
    assert callable(SimpleTree::Attribute.__init__)


def test_simpletree::attribute_constructor_args():
    sig = inspect.signature(SimpleTree::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_simpletree::attribute_has_value():
    assert hasattr(SimpleTree::Attribute, "value")
    descriptor = None
    for klass in SimpleTree::Attribute.__mro__:
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
SimpleTree::TreeElement_strategy = st.builds(
    SimpleTree::TreeElement,
    index=
        st.integers(),
    name=
        safe_text
)
SimpleTree::Node_strategy = st.builds(
    SimpleTree::Node,
    stopLineIndex=
        st.integers(),
    startLineIndex=
        st.integers(),
    stopIndex=
        st.integers(),
    startIndex=
        st.integers()
)
TreeElement_strategy = st.builds(
    TreeElement,
)
SimpleTree::Text_strategy = st.builds(
    SimpleTree::Text,
)
SimpleTree::File_strategy = st.builds(
    SimpleTree::File,
)
SimpleTree::Folder_strategy = st.builds(
    SimpleTree::Folder,
)
SimpleTree::Attribute_strategy = st.builds(
    SimpleTree::Attribute,
    value=
        safe_text
)

@given(instance=Text_strategy)
@settings(max_examples=50)
def test_text_instantiation(instance):
    assert isinstance(instance, Text)

@given(instance=SimpleTree::TreeElement_strategy)
@settings(max_examples=50)
def test_simpletree::treeelement_instantiation(instance):
    assert isinstance(instance, SimpleTree::TreeElement)

@given(instance=SimpleTree::TreeElement_strategy)
def test_simpletree::treeelement_index_type(instance):
    assert isinstance(instance.index, int)


@given(instance=SimpleTree::TreeElement_strategy)
def test_simpletree::treeelement_index_setter(instance):
    original = instance.index
    instance.index = original
    assert instance.index == original

@given(instance=SimpleTree::TreeElement_strategy)
def test_simpletree::treeelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SimpleTree::TreeElement_strategy)
def test_simpletree::treeelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SimpleTree::Node_strategy)
@settings(max_examples=50)
def test_simpletree::node_instantiation(instance):
    assert isinstance(instance, SimpleTree::Node)

@given(instance=SimpleTree::Node_strategy)
def test_simpletree::node_stopLineIndex_type(instance):
    assert isinstance(instance.stopLineIndex, int)


@given(instance=SimpleTree::Node_strategy)
def test_simpletree::node_stopLineIndex_setter(instance):
    original = instance.stopLineIndex
    instance.stopLineIndex = original
    assert instance.stopLineIndex == original

@given(instance=SimpleTree::Node_strategy)
def test_simpletree::node_startLineIndex_type(instance):
    assert isinstance(instance.startLineIndex, int)


@given(instance=SimpleTree::Node_strategy)
def test_simpletree::node_startLineIndex_setter(instance):
    original = instance.startLineIndex
    instance.startLineIndex = original
    assert instance.startLineIndex == original

@given(instance=SimpleTree::Node_strategy)
def test_simpletree::node_stopIndex_type(instance):
    assert isinstance(instance.stopIndex, int)


@given(instance=SimpleTree::Node_strategy)
def test_simpletree::node_stopIndex_setter(instance):
    original = instance.stopIndex
    instance.stopIndex = original
    assert instance.stopIndex == original

@given(instance=SimpleTree::Node_strategy)
def test_simpletree::node_startIndex_type(instance):
    assert isinstance(instance.startIndex, int)


@given(instance=SimpleTree::Node_strategy)
def test_simpletree::node_startIndex_setter(instance):
    original = instance.startIndex
    instance.startIndex = original
    assert instance.startIndex == original

@given(instance=TreeElement_strategy)
@settings(max_examples=50)
def test_treeelement_instantiation(instance):
    assert isinstance(instance, TreeElement)

@given(instance=SimpleTree::Text_strategy)
@settings(max_examples=50)
def test_simpletree::text_instantiation(instance):
    assert isinstance(instance, SimpleTree::Text)

@given(instance=SimpleTree::File_strategy)
@settings(max_examples=50)
def test_simpletree::file_instantiation(instance):
    assert isinstance(instance, SimpleTree::File)

@given(instance=SimpleTree::Folder_strategy)
@settings(max_examples=50)
def test_simpletree::folder_instantiation(instance):
    assert isinstance(instance, SimpleTree::Folder)

@given(instance=SimpleTree::Attribute_strategy)
@settings(max_examples=50)
def test_simpletree::attribute_instantiation(instance):
    assert isinstance(instance, SimpleTree::Attribute)

@given(instance=SimpleTree::Attribute_strategy)
def test_simpletree::attribute_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=SimpleTree::Attribute_strategy)
def test_simpletree::attribute_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original
