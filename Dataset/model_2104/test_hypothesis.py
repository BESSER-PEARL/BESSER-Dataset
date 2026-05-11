import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Text,
    MocaTree::TreeElement,
    MocaTree::Node,
    TreeElement,
    MocaTree::Link,
    MocaTree::File,
    MocaTree::Folder,
    MocaTree::Text,
    MocaTree::Attribute,
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



def test_mocatree::treeelement_is_not_abstract():
    assert not inspect.isabstract(MocaTree::TreeElement)


def test_mocatree::treeelement_constructor_exists():
    assert callable(MocaTree::TreeElement.__init__)


def test_mocatree::treeelement_constructor_args():
    sig = inspect.signature(MocaTree::TreeElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "index" in params, "Missing parameter 'index'"

def test_mocatree::treeelement_has_name():
    assert hasattr(MocaTree::TreeElement, "name")
    descriptor = None
    for klass in MocaTree::TreeElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mocatree::treeelement_has_index():
    assert hasattr(MocaTree::TreeElement, "index")
    descriptor = None
    for klass in MocaTree::TreeElement.__mro__:
        if "index" in klass.__dict__:
            descriptor = klass.__dict__["index"]
            break
    assert isinstance(descriptor, property)



def test_mocatree::node_is_not_abstract():
    assert not inspect.isabstract(MocaTree::Node)


def test_mocatree::node_constructor_exists():
    assert callable(MocaTree::Node.__init__)


def test_mocatree::node_constructor_args():
    sig = inspect.signature(MocaTree::Node.__init__)
    params = list(sig.parameters.keys())
    assert "stopLineIndex" in params, "Missing parameter 'stopLineIndex'"
    assert "startIndex" in params, "Missing parameter 'startIndex'"
    assert "stopIndex" in params, "Missing parameter 'stopIndex'"
    assert "startLineIndex" in params, "Missing parameter 'startLineIndex'"

def test_mocatree::node_has_stopLineIndex():
    assert hasattr(MocaTree::Node, "stopLineIndex")
    descriptor = None
    for klass in MocaTree::Node.__mro__:
        if "stopLineIndex" in klass.__dict__:
            descriptor = klass.__dict__["stopLineIndex"]
            break
    assert isinstance(descriptor, property)

def test_mocatree::node_has_startIndex():
    assert hasattr(MocaTree::Node, "startIndex")
    descriptor = None
    for klass in MocaTree::Node.__mro__:
        if "startIndex" in klass.__dict__:
            descriptor = klass.__dict__["startIndex"]
            break
    assert isinstance(descriptor, property)

def test_mocatree::node_has_stopIndex():
    assert hasattr(MocaTree::Node, "stopIndex")
    descriptor = None
    for klass in MocaTree::Node.__mro__:
        if "stopIndex" in klass.__dict__:
            descriptor = klass.__dict__["stopIndex"]
            break
    assert isinstance(descriptor, property)

def test_mocatree::node_has_startLineIndex():
    assert hasattr(MocaTree::Node, "startLineIndex")
    descriptor = None
    for klass in MocaTree::Node.__mro__:
        if "startLineIndex" in klass.__dict__:
            descriptor = klass.__dict__["startLineIndex"]
            break
    assert isinstance(descriptor, property)



def test_treeelement_is_not_abstract():
    assert not inspect.isabstract(TreeElement)


def test_treeelement_constructor_exists():
    assert callable(TreeElement.__init__)


def test_treeelement_constructor_args():
    sig = inspect.signature(TreeElement.__init__)
    params = list(sig.parameters.keys())



def test_mocatree::link_is_not_abstract():
    assert not inspect.isabstract(MocaTree::Link)


def test_mocatree::link_constructor_exists():
    assert callable(MocaTree::Link.__init__)


def test_mocatree::link_constructor_args():
    sig = inspect.signature(MocaTree::Link.__init__)
    params = list(sig.parameters.keys())



def test_mocatree::file_is_not_abstract():
    assert not inspect.isabstract(MocaTree::File)


def test_mocatree::file_constructor_exists():
    assert callable(MocaTree::File.__init__)


def test_mocatree::file_constructor_args():
    sig = inspect.signature(MocaTree::File.__init__)
    params = list(sig.parameters.keys())



def test_mocatree::folder_is_not_abstract():
    assert not inspect.isabstract(MocaTree::Folder)


def test_mocatree::folder_constructor_exists():
    assert callable(MocaTree::Folder.__init__)


def test_mocatree::folder_constructor_args():
    sig = inspect.signature(MocaTree::Folder.__init__)
    params = list(sig.parameters.keys())



def test_mocatree::text_is_not_abstract():
    assert not inspect.isabstract(MocaTree::Text)


def test_mocatree::text_constructor_exists():
    assert callable(MocaTree::Text.__init__)


def test_mocatree::text_constructor_args():
    sig = inspect.signature(MocaTree::Text.__init__)
    params = list(sig.parameters.keys())



def test_mocatree::attribute_is_not_abstract():
    assert not inspect.isabstract(MocaTree::Attribute)


def test_mocatree::attribute_constructor_exists():
    assert callable(MocaTree::Attribute.__init__)


def test_mocatree::attribute_constructor_args():
    sig = inspect.signature(MocaTree::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_mocatree::attribute_has_value():
    assert hasattr(MocaTree::Attribute, "value")
    descriptor = None
    for klass in MocaTree::Attribute.__mro__:
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
MocaTree::TreeElement_strategy = st.builds(
    MocaTree::TreeElement,
    name=
        safe_text,
    index=
        st.integers()
)
MocaTree::Node_strategy = st.builds(
    MocaTree::Node,
    stopLineIndex=
        st.integers(),
    startIndex=
        st.integers(),
    stopIndex=
        st.integers(),
    startLineIndex=
        st.integers()
)
TreeElement_strategy = st.builds(
    TreeElement,
)
MocaTree::Link_strategy = st.builds(
    MocaTree::Link,
)
MocaTree::File_strategy = st.builds(
    MocaTree::File,
)
MocaTree::Folder_strategy = st.builds(
    MocaTree::Folder,
)
MocaTree::Text_strategy = st.builds(
    MocaTree::Text,
)
MocaTree::Attribute_strategy = st.builds(
    MocaTree::Attribute,
    value=
        safe_text
)

@given(instance=Text_strategy)
@settings(max_examples=50)
def test_text_instantiation(instance):
    assert isinstance(instance, Text)

@given(instance=MocaTree::TreeElement_strategy)
@settings(max_examples=50)
def test_mocatree::treeelement_instantiation(instance):
    assert isinstance(instance, MocaTree::TreeElement)

@given(instance=MocaTree::TreeElement_strategy)
def test_mocatree::treeelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=MocaTree::TreeElement_strategy)
def test_mocatree::treeelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MocaTree::TreeElement_strategy)
def test_mocatree::treeelement_index_type(instance):
    assert isinstance(instance.index, int)


@given(instance=MocaTree::TreeElement_strategy)
def test_mocatree::treeelement_index_setter(instance):
    original = instance.index
    instance.index = original
    assert instance.index == original

@given(instance=MocaTree::Node_strategy)
@settings(max_examples=50)
def test_mocatree::node_instantiation(instance):
    assert isinstance(instance, MocaTree::Node)

@given(instance=MocaTree::Node_strategy)
def test_mocatree::node_stopLineIndex_type(instance):
    assert isinstance(instance.stopLineIndex, int)


@given(instance=MocaTree::Node_strategy)
def test_mocatree::node_stopLineIndex_setter(instance):
    original = instance.stopLineIndex
    instance.stopLineIndex = original
    assert instance.stopLineIndex == original

@given(instance=MocaTree::Node_strategy)
def test_mocatree::node_startIndex_type(instance):
    assert isinstance(instance.startIndex, int)


@given(instance=MocaTree::Node_strategy)
def test_mocatree::node_startIndex_setter(instance):
    original = instance.startIndex
    instance.startIndex = original
    assert instance.startIndex == original

@given(instance=MocaTree::Node_strategy)
def test_mocatree::node_stopIndex_type(instance):
    assert isinstance(instance.stopIndex, int)


@given(instance=MocaTree::Node_strategy)
def test_mocatree::node_stopIndex_setter(instance):
    original = instance.stopIndex
    instance.stopIndex = original
    assert instance.stopIndex == original

@given(instance=MocaTree::Node_strategy)
def test_mocatree::node_startLineIndex_type(instance):
    assert isinstance(instance.startLineIndex, int)


@given(instance=MocaTree::Node_strategy)
def test_mocatree::node_startLineIndex_setter(instance):
    original = instance.startLineIndex
    instance.startLineIndex = original
    assert instance.startLineIndex == original

@given(instance=TreeElement_strategy)
@settings(max_examples=50)
def test_treeelement_instantiation(instance):
    assert isinstance(instance, TreeElement)

@given(instance=MocaTree::Link_strategy)
@settings(max_examples=50)
def test_mocatree::link_instantiation(instance):
    assert isinstance(instance, MocaTree::Link)

@given(instance=MocaTree::File_strategy)
@settings(max_examples=50)
def test_mocatree::file_instantiation(instance):
    assert isinstance(instance, MocaTree::File)

@given(instance=MocaTree::Folder_strategy)
@settings(max_examples=50)
def test_mocatree::folder_instantiation(instance):
    assert isinstance(instance, MocaTree::Folder)

@given(instance=MocaTree::Text_strategy)
@settings(max_examples=50)
def test_mocatree::text_instantiation(instance):
    assert isinstance(instance, MocaTree::Text)

@given(instance=MocaTree::Attribute_strategy)
@settings(max_examples=50)
def test_mocatree::attribute_instantiation(instance):
    assert isinstance(instance, MocaTree::Attribute)

@given(instance=MocaTree::Attribute_strategy)
def test_mocatree::attribute_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=MocaTree::Attribute_strategy)
def test_mocatree::attribute_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original
