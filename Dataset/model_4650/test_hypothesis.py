import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    DiNode,
    di::ContainerShape,
    di::Link,
    ContainerShape,
    di::Shape,
    di::Diagram,
    di::EStringToStringMapEntry,
    di::DiNode,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_dinode_is_not_abstract():
    assert not inspect.isabstract(DiNode)


def test_dinode_constructor_exists():
    assert callable(DiNode.__init__)


def test_dinode_constructor_args():
    sig = inspect.signature(DiNode.__init__)
    params = list(sig.parameters.keys())



def test_di::containershape_is_not_abstract():
    assert not inspect.isabstract(di::ContainerShape)


def test_di::containershape_constructor_exists():
    assert callable(di::ContainerShape.__init__)


def test_di::containershape_constructor_args():
    sig = inspect.signature(di::ContainerShape.__init__)
    params = list(sig.parameters.keys())



def test_di::link_is_not_abstract():
    assert not inspect.isabstract(di::Link)


def test_di::link_constructor_exists():
    assert callable(di::Link.__init__)


def test_di::link_constructor_args():
    sig = inspect.signature(di::Link.__init__)
    params = list(sig.parameters.keys())



def test_containershape_is_not_abstract():
    assert not inspect.isabstract(ContainerShape)


def test_containershape_constructor_exists():
    assert callable(ContainerShape.__init__)


def test_containershape_constructor_args():
    sig = inspect.signature(ContainerShape.__init__)
    params = list(sig.parameters.keys())



def test_di::shape_is_not_abstract():
    assert not inspect.isabstract(di::Shape)


def test_di::shape_constructor_exists():
    assert callable(di::Shape.__init__)


def test_di::shape_constructor_args():
    sig = inspect.signature(di::Shape.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "width" in params, "Missing parameter 'width'"
    assert "height" in params, "Missing parameter 'height'"
    assert "y" in params, "Missing parameter 'y'"

def test_di::shape_has_x():
    assert hasattr(di::Shape, "x")
    descriptor = None
    for klass in di::Shape.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_di::shape_has_width():
    assert hasattr(di::Shape, "width")
    descriptor = None
    for klass in di::Shape.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_di::shape_has_height():
    assert hasattr(di::Shape, "height")
    descriptor = None
    for klass in di::Shape.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_di::shape_has_y():
    assert hasattr(di::Shape, "y")
    descriptor = None
    for klass in di::Shape.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)



def test_di::diagram_is_not_abstract():
    assert not inspect.isabstract(di::Diagram)


def test_di::diagram_constructor_exists():
    assert callable(di::Diagram.__init__)


def test_di::diagram_constructor_args():
    sig = inspect.signature(di::Diagram.__init__)
    params = list(sig.parameters.keys())



def test_di::estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(di::EStringToStringMapEntry)


def test_di::estringtostringmapentry_constructor_exists():
    assert callable(di::EStringToStringMapEntry.__init__)


def test_di::estringtostringmapentry_constructor_args():
    sig = inspect.signature(di::EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_di::dinode_is_not_abstract():
    assert not inspect.isabstract(di::DiNode)


def test_di::dinode_constructor_exists():
    assert callable(di::DiNode.__init__)


def test_di::dinode_constructor_args():
    sig = inspect.signature(di::DiNode.__init__)
    params = list(sig.parameters.keys())
    assert "modelElement" in params, "Missing parameter 'modelElement'"

def test_di::dinode_has_modelElement():
    assert hasattr(di::DiNode, "modelElement")
    descriptor = None
    for klass in di::DiNode.__mro__:
        if "modelElement" in klass.__dict__:
            descriptor = klass.__dict__["modelElement"]
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
DiNode_strategy = st.builds(
    DiNode,
)
di::ContainerShape_strategy = st.builds(
    di::ContainerShape,
)
di::Link_strategy = st.builds(
    di::Link,
)
ContainerShape_strategy = st.builds(
    ContainerShape,
)
di::Shape_strategy = st.builds(
    di::Shape,
    x=
        st.integers(),
    width=
        st.integers(),
    height=
        st.integers(),
    y=
        st.integers()
)
di::Diagram_strategy = st.builds(
    di::Diagram,
)
di::EStringToStringMapEntry_strategy = st.builds(
    di::EStringToStringMapEntry,
)
di::DiNode_strategy = st.builds(
    di::DiNode,
    modelElement=
        safe_text
)

@given(instance=DiNode_strategy)
@settings(max_examples=50)
def test_dinode_instantiation(instance):
    assert isinstance(instance, DiNode)

@given(instance=di::ContainerShape_strategy)
@settings(max_examples=50)
def test_di::containershape_instantiation(instance):
    assert isinstance(instance, di::ContainerShape)

@given(instance=di::Link_strategy)
@settings(max_examples=50)
def test_di::link_instantiation(instance):
    assert isinstance(instance, di::Link)

@given(instance=ContainerShape_strategy)
@settings(max_examples=50)
def test_containershape_instantiation(instance):
    assert isinstance(instance, ContainerShape)

@given(instance=di::Shape_strategy)
@settings(max_examples=50)
def test_di::shape_instantiation(instance):
    assert isinstance(instance, di::Shape)

@given(instance=di::Shape_strategy)
def test_di::shape_x_type(instance):
    assert isinstance(instance.x, int)


@given(instance=di::Shape_strategy)
def test_di::shape_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=di::Shape_strategy)
def test_di::shape_width_type(instance):
    assert isinstance(instance.width, int)


@given(instance=di::Shape_strategy)
def test_di::shape_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=di::Shape_strategy)
def test_di::shape_height_type(instance):
    assert isinstance(instance.height, int)


@given(instance=di::Shape_strategy)
def test_di::shape_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=di::Shape_strategy)
def test_di::shape_y_type(instance):
    assert isinstance(instance.y, int)


@given(instance=di::Shape_strategy)
def test_di::shape_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=di::Diagram_strategy)
@settings(max_examples=50)
def test_di::diagram_instantiation(instance):
    assert isinstance(instance, di::Diagram)

@given(instance=di::EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_di::estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, di::EStringToStringMapEntry)

@given(instance=di::DiNode_strategy)
@settings(max_examples=50)
def test_di::dinode_instantiation(instance):
    assert isinstance(instance, di::DiNode)

@given(instance=di::DiNode_strategy)
def test_di::dinode_modelElement_type(instance):
    assert isinstance(instance.modelElement, str)


@given(instance=di::DiNode_strategy)
def test_di::dinode_modelElement_setter(instance):
    original = instance.modelElement
    instance.modelElement = original
    assert instance.modelElement == original
