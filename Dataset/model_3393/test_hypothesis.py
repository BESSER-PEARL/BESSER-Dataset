import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    mindmap::Topic,
    mindmap::MindMap,
    Topic,
    mindmap::MainTopic,
    mindmap::SubTopic,
    mindmap::CentralTopic,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mindmap::topic_is_not_abstract():
    assert not inspect.isabstract(mindmap::Topic)


def test_mindmap::topic_constructor_exists():
    assert callable(mindmap::Topic.__init__)


def test_mindmap::topic_constructor_args():
    sig = inspect.signature(mindmap::Topic.__init__)
    params = list(sig.parameters.keys())
    assert "marker" in params, "Missing parameter 'marker'"
    assert "name" in params, "Missing parameter 'name'"

def test_mindmap::topic_has_marker():
    assert hasattr(mindmap::Topic, "marker")
    descriptor = None
    for klass in mindmap::Topic.__mro__:
        if "marker" in klass.__dict__:
            descriptor = klass.__dict__["marker"]
            break
    assert isinstance(descriptor, property)

def test_mindmap::topic_has_name():
    assert hasattr(mindmap::Topic, "name")
    descriptor = None
    for klass in mindmap::Topic.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mindmap::mindmap_is_not_abstract():
    assert not inspect.isabstract(mindmap::MindMap)


def test_mindmap::mindmap_constructor_exists():
    assert callable(mindmap::MindMap.__init__)


def test_mindmap::mindmap_constructor_args():
    sig = inspect.signature(mindmap::MindMap.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_mindmap::mindmap_has_title():
    assert hasattr(mindmap::MindMap, "title")
    descriptor = None
    for klass in mindmap::MindMap.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_topic_is_not_abstract():
    assert not inspect.isabstract(Topic)


def test_topic_constructor_exists():
    assert callable(Topic.__init__)


def test_topic_constructor_args():
    sig = inspect.signature(Topic.__init__)
    params = list(sig.parameters.keys())



def test_mindmap::maintopic_is_not_abstract():
    assert not inspect.isabstract(mindmap::MainTopic)


def test_mindmap::maintopic_constructor_exists():
    assert callable(mindmap::MainTopic.__init__)


def test_mindmap::maintopic_constructor_args():
    sig = inspect.signature(mindmap::MainTopic.__init__)
    params = list(sig.parameters.keys())



def test_mindmap::subtopic_is_not_abstract():
    assert not inspect.isabstract(mindmap::SubTopic)


def test_mindmap::subtopic_constructor_exists():
    assert callable(mindmap::SubTopic.__init__)


def test_mindmap::subtopic_constructor_args():
    sig = inspect.signature(mindmap::SubTopic.__init__)
    params = list(sig.parameters.keys())



def test_mindmap::centraltopic_is_not_abstract():
    assert not inspect.isabstract(mindmap::CentralTopic)


def test_mindmap::centraltopic_constructor_exists():
    assert callable(mindmap::CentralTopic.__init__)


def test_mindmap::centraltopic_constructor_args():
    sig = inspect.signature(mindmap::CentralTopic.__init__)
    params = list(sig.parameters.keys())


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
mindmap::Topic_strategy = st.builds(
    mindmap::Topic,
    marker=
        st.integers(),
    name=
        safe_text
)
mindmap::MindMap_strategy = st.builds(
    mindmap::MindMap,
    title=
        safe_text
)
Topic_strategy = st.builds(
    Topic,
)
mindmap::MainTopic_strategy = st.builds(
    mindmap::MainTopic,
)
mindmap::SubTopic_strategy = st.builds(
    mindmap::SubTopic,
)
mindmap::CentralTopic_strategy = st.builds(
    mindmap::CentralTopic,
)

@given(instance=mindmap::Topic_strategy)
@settings(max_examples=50)
def test_mindmap::topic_instantiation(instance):
    assert isinstance(instance, mindmap::Topic)

@given(instance=mindmap::Topic_strategy)
def test_mindmap::topic_marker_type(instance):
    assert isinstance(instance.marker, int)


@given(instance=mindmap::Topic_strategy)
def test_mindmap::topic_marker_setter(instance):
    original = instance.marker
    instance.marker = original
    assert instance.marker == original

@given(instance=mindmap::Topic_strategy)
def test_mindmap::topic_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mindmap::Topic_strategy)
def test_mindmap::topic_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mindmap::MindMap_strategy)
@settings(max_examples=50)
def test_mindmap::mindmap_instantiation(instance):
    assert isinstance(instance, mindmap::MindMap)

@given(instance=mindmap::MindMap_strategy)
def test_mindmap::mindmap_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=mindmap::MindMap_strategy)
def test_mindmap::mindmap_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=Topic_strategy)
@settings(max_examples=50)
def test_topic_instantiation(instance):
    assert isinstance(instance, Topic)

@given(instance=mindmap::MainTopic_strategy)
@settings(max_examples=50)
def test_mindmap::maintopic_instantiation(instance):
    assert isinstance(instance, mindmap::MainTopic)

@given(instance=mindmap::SubTopic_strategy)
@settings(max_examples=50)
def test_mindmap::subtopic_instantiation(instance):
    assert isinstance(instance, mindmap::SubTopic)

@given(instance=mindmap::CentralTopic_strategy)
@settings(max_examples=50)
def test_mindmap::centraltopic_instantiation(instance):
    assert isinstance(instance, mindmap::CentralTopic)
