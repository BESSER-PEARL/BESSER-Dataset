import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    di_EStringToStringMapEntry,
    di_DiNode,
    ContainerShape,
    di_Diagram,
    di_Shape,
    DiNode,
    di_Link,
    di_ContainerShape,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_di_estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(di_EStringToStringMapEntry)


def test_di_estringtostringmapentry_constructor_exists():
    assert callable(di_EStringToStringMapEntry.__init__)


def test_di_estringtostringmapentry_constructor_args():
    sig = inspect.signature(di_EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_di_dinode_is_not_abstract():
    assert not inspect.isabstract(di_DiNode)


def test_di_dinode_constructor_exists():
    assert callable(di_DiNode.__init__)


def test_di_dinode_constructor_args():
    sig = inspect.signature(di_DiNode.__init__)
    params = list(sig.parameters.keys())
    assert "modelElement" in params, "Missing parameter 'modelElement'"

def test_di_dinode_has_modelElement():
    assert hasattr(di_DiNode, "modelElement")
    descriptor = None
    for klass in di_DiNode.__mro__:
        if "modelElement" in klass.__dict__:
            descriptor = klass.__dict__["modelElement"]
            break
    assert isinstance(descriptor, property)



def test_containershape_is_not_abstract():
    assert not inspect.isabstract(ContainerShape)


def test_containershape_constructor_exists():
    assert callable(ContainerShape.__init__)


def test_containershape_constructor_args():
    sig = inspect.signature(ContainerShape.__init__)
    params = list(sig.parameters.keys())



def test_di_diagram_is_not_abstract():
    assert not inspect.isabstract(di_Diagram)


def test_di_diagram_constructor_exists():
    assert callable(di_Diagram.__init__)


def test_di_diagram_constructor_args():
    sig = inspect.signature(di_Diagram.__init__)
    params = list(sig.parameters.keys())



def test_di_shape_is_not_abstract():
    assert not inspect.isabstract(di_Shape)


def test_di_shape_constructor_exists():
    assert callable(di_Shape.__init__)


def test_di_shape_constructor_args():
    sig = inspect.signature(di_Shape.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "width" in params, "Missing parameter 'width'"
    assert "x" in params, "Missing parameter 'x'"
    assert "height" in params, "Missing parameter 'height'"

def test_di_shape_has_y():
    assert hasattr(di_Shape, "y")
    descriptor = None
    for klass in di_Shape.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_di_shape_has_width():
    assert hasattr(di_Shape, "width")
    descriptor = None
    for klass in di_Shape.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_di_shape_has_x():
    assert hasattr(di_Shape, "x")
    descriptor = None
    for klass in di_Shape.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_di_shape_has_height():
    assert hasattr(di_Shape, "height")
    descriptor = None
    for klass in di_Shape.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)



def test_dinode_is_not_abstract():
    assert not inspect.isabstract(DiNode)


def test_dinode_constructor_exists():
    assert callable(DiNode.__init__)


def test_dinode_constructor_args():
    sig = inspect.signature(DiNode.__init__)
    params = list(sig.parameters.keys())



def test_di_link_is_not_abstract():
    assert not inspect.isabstract(di_Link)


def test_di_link_constructor_exists():
    assert callable(di_Link.__init__)


def test_di_link_constructor_args():
    sig = inspect.signature(di_Link.__init__)
    params = list(sig.parameters.keys())



def test_di_containershape_is_not_abstract():
    assert not inspect.isabstract(di_ContainerShape)


def test_di_containershape_constructor_exists():
    assert callable(di_ContainerShape.__init__)


def test_di_containershape_constructor_args():
    sig = inspect.signature(di_ContainerShape.__init__)
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
di_EStringToStringMapEntry_strategy = st.builds(
    di_EStringToStringMapEntry,
)
di_DiNode_strategy = st.builds(
    di_DiNode,
    modelElement=
        safe_text
)
ContainerShape_strategy = st.builds(
    ContainerShape,
)
di_Diagram_strategy = st.builds(
    di_Diagram,
)
di_Shape_strategy = st.builds(
    di_Shape,
    y=
        st.integers(),
    width=
        st.integers(),
    x=
        st.integers(),
    height=
        st.integers()
)
DiNode_strategy = st.builds(
    DiNode,
)
di_Link_strategy = st.builds(
    di_Link,
)
di_ContainerShape_strategy = st.builds(
    di_ContainerShape,
)

@given(instance=di_EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_di_estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, di_EStringToStringMapEntry)

@given(instance=di_DiNode_strategy)
@settings(max_examples=50)
def test_di_dinode_instantiation(instance):
    assert isinstance(instance, di_DiNode)



@given(instance=di_DiNode_strategy)
def test_di_dinode_modelElement_setter(instance):
    original = instance.modelElement
    instance.modelElement = original
    assert instance.modelElement == original

@given(instance=ContainerShape_strategy)
@settings(max_examples=50)
def test_containershape_instantiation(instance):
    assert isinstance(instance, ContainerShape)

@given(instance=di_Diagram_strategy)
@settings(max_examples=50)
def test_di_diagram_instantiation(instance):
    assert isinstance(instance, di_Diagram)

@given(instance=di_Shape_strategy)
@settings(max_examples=50)
def test_di_shape_instantiation(instance):
    assert isinstance(instance, di_Shape)



@given(instance=di_Shape_strategy)
def test_di_shape_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=di_Shape_strategy)
def test_di_shape_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=di_Shape_strategy)
def test_di_shape_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=di_Shape_strategy)
def test_di_shape_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=DiNode_strategy)
@settings(max_examples=50)
def test_dinode_instantiation(instance):
    assert isinstance(instance, DiNode)

@given(instance=di_Link_strategy)
@settings(max_examples=50)
def test_di_link_instantiation(instance):
    assert isinstance(instance, di_Link)

@given(instance=di_ContainerShape_strategy)
@settings(max_examples=50)
def test_di_containershape_instantiation(instance):
    assert isinstance(instance, di_ContainerShape)
