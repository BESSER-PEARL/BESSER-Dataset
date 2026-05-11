import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Simpletree::TreeElement,
    TreeElement,
    Simpletree::File,
    Simpletree::Folder,
    Simpletree::Attribute,
    Simpletree::Text,
    Text,
    Simpletree::Node,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_simpletree::treeelement_is_not_abstract():
    assert not inspect.isabstract(Simpletree::TreeElement)


def test_simpletree::treeelement_constructor_exists():
    assert callable(Simpletree::TreeElement.__init__)


def test_simpletree::treeelement_constructor_args():
    sig = inspect.signature(Simpletree::TreeElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "index" in params, "Missing parameter 'index'"

def test_simpletree::treeelement_has_name():
    assert hasattr(Simpletree::TreeElement, "name")
    descriptor = None
    for klass in Simpletree::TreeElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_simpletree::treeelement_has_index():
    assert hasattr(Simpletree::TreeElement, "index")
    descriptor = None
    for klass in Simpletree::TreeElement.__mro__:
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



def test_simpletree::file_is_not_abstract():
    assert not inspect.isabstract(Simpletree::File)


def test_simpletree::file_constructor_exists():
    assert callable(Simpletree::File.__init__)


def test_simpletree::file_constructor_args():
    sig = inspect.signature(Simpletree::File.__init__)
    params = list(sig.parameters.keys())



def test_simpletree::folder_is_not_abstract():
    assert not inspect.isabstract(Simpletree::Folder)


def test_simpletree::folder_constructor_exists():
    assert callable(Simpletree::Folder.__init__)


def test_simpletree::folder_constructor_args():
    sig = inspect.signature(Simpletree::Folder.__init__)
    params = list(sig.parameters.keys())



def test_simpletree::attribute_is_not_abstract():
    assert not inspect.isabstract(Simpletree::Attribute)


def test_simpletree::attribute_constructor_exists():
    assert callable(Simpletree::Attribute.__init__)


def test_simpletree::attribute_constructor_args():
    sig = inspect.signature(Simpletree::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_simpletree::attribute_has_value():
    assert hasattr(Simpletree::Attribute, "value")
    descriptor = None
    for klass in Simpletree::Attribute.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_simpletree::text_is_not_abstract():
    assert not inspect.isabstract(Simpletree::Text)


def test_simpletree::text_constructor_exists():
    assert callable(Simpletree::Text.__init__)


def test_simpletree::text_constructor_args():
    sig = inspect.signature(Simpletree::Text.__init__)
    params = list(sig.parameters.keys())



def test_text_is_not_abstract():
    assert not inspect.isabstract(Text)


def test_text_constructor_exists():
    assert callable(Text.__init__)


def test_text_constructor_args():
    sig = inspect.signature(Text.__init__)
    params = list(sig.parameters.keys())



def test_simpletree::node_is_not_abstract():
    assert not inspect.isabstract(Simpletree::Node)


def test_simpletree::node_constructor_exists():
    assert callable(Simpletree::Node.__init__)


def test_simpletree::node_constructor_args():
    sig = inspect.signature(Simpletree::Node.__init__)
    params = list(sig.parameters.keys())
    assert "stopIndex" in params, "Missing parameter 'stopIndex'"
    assert "startLineIndex" in params, "Missing parameter 'startLineIndex'"
    assert "startIndex" in params, "Missing parameter 'startIndex'"
    assert "stopLineIndex" in params, "Missing parameter 'stopLineIndex'"

def test_simpletree::node_has_stopIndex():
    assert hasattr(Simpletree::Node, "stopIndex")
    descriptor = None
    for klass in Simpletree::Node.__mro__:
        if "stopIndex" in klass.__dict__:
            descriptor = klass.__dict__["stopIndex"]
            break
    assert isinstance(descriptor, property)

def test_simpletree::node_has_startLineIndex():
    assert hasattr(Simpletree::Node, "startLineIndex")
    descriptor = None
    for klass in Simpletree::Node.__mro__:
        if "startLineIndex" in klass.__dict__:
            descriptor = klass.__dict__["startLineIndex"]
            break
    assert isinstance(descriptor, property)

def test_simpletree::node_has_startIndex():
    assert hasattr(Simpletree::Node, "startIndex")
    descriptor = None
    for klass in Simpletree::Node.__mro__:
        if "startIndex" in klass.__dict__:
            descriptor = klass.__dict__["startIndex"]
            break
    assert isinstance(descriptor, property)

def test_simpletree::node_has_stopLineIndex():
    assert hasattr(Simpletree::Node, "stopLineIndex")
    descriptor = None
    for klass in Simpletree::Node.__mro__:
        if "stopLineIndex" in klass.__dict__:
            descriptor = klass.__dict__["stopLineIndex"]
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
Simpletree::TreeElement_strategy = st.builds(
    Simpletree::TreeElement,
    name=
        safe_text,
    index=
        st.integers()
)
TreeElement_strategy = st.builds(
    TreeElement,
)
Simpletree::File_strategy = st.builds(
    Simpletree::File,
)
Simpletree::Folder_strategy = st.builds(
    Simpletree::Folder,
)
Simpletree::Attribute_strategy = st.builds(
    Simpletree::Attribute,
    value=
        safe_text
)
Simpletree::Text_strategy = st.builds(
    Simpletree::Text,
)
Text_strategy = st.builds(
    Text,
)
Simpletree::Node_strategy = st.builds(
    Simpletree::Node,
    stopIndex=
        st.integers(),
    startLineIndex=
        st.integers(),
    startIndex=
        st.integers(),
    stopLineIndex=
        st.integers()
)

@given(instance=Simpletree::TreeElement_strategy)
@settings(max_examples=50)
def test_simpletree::treeelement_instantiation(instance):
    assert isinstance(instance, Simpletree::TreeElement)

@given(instance=Simpletree::TreeElement_strategy)
def test_simpletree::treeelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Simpletree::TreeElement_strategy)
def test_simpletree::treeelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Simpletree::TreeElement_strategy)
def test_simpletree::treeelement_index_type(instance):
    assert isinstance(instance.index, int)


@given(instance=Simpletree::TreeElement_strategy)
def test_simpletree::treeelement_index_setter(instance):
    original = instance.index
    instance.index = original
    assert instance.index == original

@given(instance=TreeElement_strategy)
@settings(max_examples=50)
def test_treeelement_instantiation(instance):
    assert isinstance(instance, TreeElement)

@given(instance=Simpletree::File_strategy)
@settings(max_examples=50)
def test_simpletree::file_instantiation(instance):
    assert isinstance(instance, Simpletree::File)

@given(instance=Simpletree::Folder_strategy)
@settings(max_examples=50)
def test_simpletree::folder_instantiation(instance):
    assert isinstance(instance, Simpletree::Folder)

@given(instance=Simpletree::Attribute_strategy)
@settings(max_examples=50)
def test_simpletree::attribute_instantiation(instance):
    assert isinstance(instance, Simpletree::Attribute)

@given(instance=Simpletree::Attribute_strategy)
def test_simpletree::attribute_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=Simpletree::Attribute_strategy)
def test_simpletree::attribute_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Simpletree::Text_strategy)
@settings(max_examples=50)
def test_simpletree::text_instantiation(instance):
    assert isinstance(instance, Simpletree::Text)

@given(instance=Text_strategy)
@settings(max_examples=50)
def test_text_instantiation(instance):
    assert isinstance(instance, Text)

@given(instance=Simpletree::Node_strategy)
@settings(max_examples=50)
def test_simpletree::node_instantiation(instance):
    assert isinstance(instance, Simpletree::Node)

@given(instance=Simpletree::Node_strategy)
def test_simpletree::node_stopIndex_type(instance):
    assert isinstance(instance.stopIndex, int)


@given(instance=Simpletree::Node_strategy)
def test_simpletree::node_stopIndex_setter(instance):
    original = instance.stopIndex
    instance.stopIndex = original
    assert instance.stopIndex == original

@given(instance=Simpletree::Node_strategy)
def test_simpletree::node_startLineIndex_type(instance):
    assert isinstance(instance.startLineIndex, int)


@given(instance=Simpletree::Node_strategy)
def test_simpletree::node_startLineIndex_setter(instance):
    original = instance.startLineIndex
    instance.startLineIndex = original
    assert instance.startLineIndex == original

@given(instance=Simpletree::Node_strategy)
def test_simpletree::node_startIndex_type(instance):
    assert isinstance(instance.startIndex, int)


@given(instance=Simpletree::Node_strategy)
def test_simpletree::node_startIndex_setter(instance):
    original = instance.startIndex
    instance.startIndex = original
    assert instance.startIndex == original

@given(instance=Simpletree::Node_strategy)
def test_simpletree::node_stopLineIndex_type(instance):
    assert isinstance(instance.stopLineIndex, int)


@given(instance=Simpletree::Node_strategy)
def test_simpletree::node_stopLineIndex_setter(instance):
    original = instance.stopLineIndex
    instance.stopLineIndex = original
    assert instance.stopLineIndex == original
