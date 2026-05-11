import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    egt::GraphModel,
    Edge,
    egt::SingleEdge,
    egt::DiEdge,
    egt::ColorRegistry,
    egt::Edge,
    egt::Vertex,
    Colors,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_egt::graphmodel_is_not_abstract():
    assert not inspect.isabstract(egt::GraphModel)


def test_egt::graphmodel_constructor_exists():
    assert callable(egt::GraphModel.__init__)


def test_egt::graphmodel_constructor_args():
    sig = inspect.signature(egt::GraphModel.__init__)
    params = list(sig.parameters.keys())



def test_edge_is_not_abstract():
    assert not inspect.isabstract(Edge)


def test_edge_constructor_exists():
    assert callable(Edge.__init__)


def test_edge_constructor_args():
    sig = inspect.signature(Edge.__init__)
    params = list(sig.parameters.keys())



def test_egt::singleedge_is_not_abstract():
    assert not inspect.isabstract(egt::SingleEdge)


def test_egt::singleedge_constructor_exists():
    assert callable(egt::SingleEdge.__init__)


def test_egt::singleedge_constructor_args():
    sig = inspect.signature(egt::SingleEdge.__init__)
    params = list(sig.parameters.keys())



def test_egt::diedge_is_not_abstract():
    assert not inspect.isabstract(egt::DiEdge)


def test_egt::diedge_constructor_exists():
    assert callable(egt::DiEdge.__init__)


def test_egt::diedge_constructor_args():
    sig = inspect.signature(egt::DiEdge.__init__)
    params = list(sig.parameters.keys())



def test_egt::colorregistry_is_not_abstract():
    assert not inspect.isabstract(egt::ColorRegistry)


def test_egt::colorregistry_constructor_exists():
    assert callable(egt::ColorRegistry.__init__)


def test_egt::colorregistry_constructor_args():
    sig = inspect.signature(egt::ColorRegistry.__init__)
    params = list(sig.parameters.keys())
    assert "images" in params, "Missing parameter 'images'"

def test_egt::colorregistry_has_images():
    assert hasattr(egt::ColorRegistry, "images")
    descriptor = None
    for klass in egt::ColorRegistry.__mro__:
        if "images" in klass.__dict__:
            descriptor = klass.__dict__["images"]
            break
    assert isinstance(descriptor, property)



def test_egt::edge_is_not_abstract():
    assert not inspect.isabstract(egt::Edge)


def test_egt::edge_constructor_exists():
    assert callable(egt::Edge.__init__)


def test_egt::edge_constructor_args():
    sig = inspect.signature(egt::Edge.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"
    assert "color" in params, "Missing parameter 'color'"

def test_egt::edge_has_weight():
    assert hasattr(egt::Edge, "weight")
    descriptor = None
    for klass in egt::Edge.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)

def test_egt::edge_has_color():
    assert hasattr(egt::Edge, "color")
    descriptor = None
    for klass in egt::Edge.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)



def test_egt::vertex_is_not_abstract():
    assert not inspect.isabstract(egt::Vertex)


def test_egt::vertex_constructor_exists():
    assert callable(egt::Vertex.__init__)


def test_egt::vertex_constructor_args():
    sig = inspect.signature(egt::Vertex.__init__)
    params = list(sig.parameters.keys())
    assert "color" in params, "Missing parameter 'color'"
    assert "index" in params, "Missing parameter 'index'"
    assert "name" in params, "Missing parameter 'name'"

def test_egt::vertex_has_color():
    assert hasattr(egt::Vertex, "color")
    descriptor = None
    for klass in egt::Vertex.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_egt::vertex_has_index():
    assert hasattr(egt::Vertex, "index")
    descriptor = None
    for klass in egt::Vertex.__mro__:
        if "index" in klass.__dict__:
            descriptor = klass.__dict__["index"]
            break
    assert isinstance(descriptor, property)

def test_egt::vertex_has_name():
    assert hasattr(egt::Vertex, "name")
    descriptor = None
    for klass in egt::Vertex.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_colors_exists():
    # Check that the Enumeration exists
    assert Colors is not None

def test_colors_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Colors]
    expected_literals = [
        "performed",
        "clean",
        "touched",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Colors"


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
egt::GraphModel_strategy = st.builds(
    egt::GraphModel,
)
Edge_strategy = st.builds(
    Edge,
)
egt::SingleEdge_strategy = st.builds(
    egt::SingleEdge,
)
egt::DiEdge_strategy = st.builds(
    egt::DiEdge,
)
egt::ColorRegistry_strategy = st.builds(
    egt::ColorRegistry,
    images=
        safe_text
)
egt::Edge_strategy = st.builds(
    egt::Edge,
    weight=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    color=
        safe_text
)
egt::Vertex_strategy = st.builds(
    egt::Vertex,
    color=
        safe_text,
    index=
        st.integers(),
    name=
        safe_text
)

@given(instance=egt::GraphModel_strategy)
@settings(max_examples=50)
def test_egt::graphmodel_instantiation(instance):
    assert isinstance(instance, egt::GraphModel)

@given(instance=Edge_strategy)
@settings(max_examples=50)
def test_edge_instantiation(instance):
    assert isinstance(instance, Edge)

@given(instance=egt::SingleEdge_strategy)
@settings(max_examples=50)
def test_egt::singleedge_instantiation(instance):
    assert isinstance(instance, egt::SingleEdge)

@given(instance=egt::DiEdge_strategy)
@settings(max_examples=50)
def test_egt::diedge_instantiation(instance):
    assert isinstance(instance, egt::DiEdge)

@given(instance=egt::ColorRegistry_strategy)
@settings(max_examples=50)
def test_egt::colorregistry_instantiation(instance):
    assert isinstance(instance, egt::ColorRegistry)

@given(instance=egt::ColorRegistry_strategy)
def test_egt::colorregistry_images_type(instance):
    assert isinstance(instance.images, str)


@given(instance=egt::ColorRegistry_strategy)
def test_egt::colorregistry_images_setter(instance):
    original = instance.images
    instance.images = original
    assert instance.images == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=egt::ColorRegistry_strategy)
@settings(max_examples=30)
def test_egt::colorregistry_init_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.init()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.init).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'init' in egt::ColorRegistry is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'init' in egt::ColorRegistry did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'init' in egt::ColorRegistry is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=egt::ColorRegistry_strategy)
@settings(max_examples=30)
def test_egt::colorregistry_dispose_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.dispose()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.dispose).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'dispose' in egt::ColorRegistry is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'dispose' in egt::ColorRegistry did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'dispose' in egt::ColorRegistry is not implemented or raised an error")

@given(instance=egt::Edge_strategy)
@settings(max_examples=50)
def test_egt::edge_instantiation(instance):
    assert isinstance(instance, egt::Edge)

@given(instance=egt::Edge_strategy)
def test_egt::edge_weight_type(instance):
    assert isinstance(instance.weight, float)


@given(instance=egt::Edge_strategy)
def test_egt::edge_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=egt::Edge_strategy)
def test_egt::edge_color_type(instance):
    assert isinstance(instance.color, str)


@given(instance=egt::Edge_strategy)
def test_egt::edge_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=egt::Vertex_strategy)
@settings(max_examples=50)
def test_egt::vertex_instantiation(instance):
    assert isinstance(instance, egt::Vertex)

@given(instance=egt::Vertex_strategy)
def test_egt::vertex_color_type(instance):
    assert isinstance(instance.color, str)


@given(instance=egt::Vertex_strategy)
def test_egt::vertex_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=egt::Vertex_strategy)
def test_egt::vertex_index_type(instance):
    assert isinstance(instance.index, int)


@given(instance=egt::Vertex_strategy)
def test_egt::vertex_index_setter(instance):
    original = instance.index
    instance.index = original
    assert instance.index == original

@given(instance=egt::Vertex_strategy)
def test_egt::vertex_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=egt::Vertex_strategy)
def test_egt::vertex_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
