import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    graph::ResourcePlot,
    graph::ResourceGraph,
    graph::ResourceGraphs,
    FitPolicy,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_graph::resourceplot_is_not_abstract():
    assert not inspect.isabstract(graph::ResourcePlot)


def test_graph::resourceplot_constructor_exists():
    assert callable(graph::ResourcePlot.__init__)


def test_graph::resourceplot_constructor_args():
    sig = inspect.signature(graph::ResourcePlot.__init__)
    params = list(sig.parameters.keys())
    assert "min" in params, "Missing parameter 'min'"
    assert "name" in params, "Missing parameter 'name'"
    assert "rgb" in params, "Missing parameter 'rgb'"
    assert "max" in params, "Missing parameter 'max'"
    assert "fit" in params, "Missing parameter 'fit'"

def test_graph::resourceplot_has_min():
    assert hasattr(graph::ResourcePlot, "min")
    descriptor = None
    for klass in graph::ResourcePlot.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)

def test_graph::resourceplot_has_name():
    assert hasattr(graph::ResourcePlot, "name")
    descriptor = None
    for klass in graph::ResourcePlot.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_graph::resourceplot_has_rgb():
    assert hasattr(graph::ResourcePlot, "rgb")
    descriptor = None
    for klass in graph::ResourcePlot.__mro__:
        if "rgb" in klass.__dict__:
            descriptor = klass.__dict__["rgb"]
            break
    assert isinstance(descriptor, property)

def test_graph::resourceplot_has_max():
    assert hasattr(graph::ResourcePlot, "max")
    descriptor = None
    for klass in graph::ResourcePlot.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
            break
    assert isinstance(descriptor, property)

def test_graph::resourceplot_has_fit():
    assert hasattr(graph::ResourcePlot, "fit")
    descriptor = None
    for klass in graph::ResourcePlot.__mro__:
        if "fit" in klass.__dict__:
            descriptor = klass.__dict__["fit"]
            break
    assert isinstance(descriptor, property)



def test_graph::resourcegraph_is_not_abstract():
    assert not inspect.isabstract(graph::ResourceGraph)


def test_graph::resourcegraph_constructor_exists():
    assert callable(graph::ResourceGraph.__init__)


def test_graph::resourcegraph_constructor_args():
    sig = inspect.signature(graph::ResourceGraph.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_graph::resourcegraph_has_name():
    assert hasattr(graph::ResourceGraph, "name")
    descriptor = None
    for klass in graph::ResourceGraph.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_graph::resourcegraphs_is_not_abstract():
    assert not inspect.isabstract(graph::ResourceGraphs)


def test_graph::resourcegraphs_constructor_exists():
    assert callable(graph::ResourceGraphs.__init__)


def test_graph::resourcegraphs_constructor_args():
    sig = inspect.signature(graph::ResourceGraphs.__init__)
    params = list(sig.parameters.keys())

def test_fitpolicy_exists():
    # Check that the Enumeration exists
    assert FitPolicy is not None

def test_fitpolicy_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FitPolicy]
    expected_literals = [
        "AUTO",
        "CUSTOM",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FitPolicy"


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
graph::ResourcePlot_strategy = st.builds(
    graph::ResourcePlot,
    min=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text,
    rgb=
        safe_text,
    max=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    fit=
        safe_text
)
graph::ResourceGraph_strategy = st.builds(
    graph::ResourceGraph,
    name=
        safe_text
)
graph::ResourceGraphs_strategy = st.builds(
    graph::ResourceGraphs,
)

@given(instance=graph::ResourcePlot_strategy)
@settings(max_examples=50)
def test_graph::resourceplot_instantiation(instance):
    assert isinstance(instance, graph::ResourcePlot)

@given(instance=graph::ResourcePlot_strategy)
def test_graph::resourceplot_min_type(instance):
    assert isinstance(instance.min, float)


@given(instance=graph::ResourcePlot_strategy)
def test_graph::resourceplot_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original

@given(instance=graph::ResourcePlot_strategy)
def test_graph::resourceplot_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=graph::ResourcePlot_strategy)
def test_graph::resourceplot_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=graph::ResourcePlot_strategy)
def test_graph::resourceplot_rgb_type(instance):
    assert isinstance(instance.rgb, str)


@given(instance=graph::ResourcePlot_strategy)
def test_graph::resourceplot_rgb_setter(instance):
    original = instance.rgb
    instance.rgb = original
    assert instance.rgb == original

@given(instance=graph::ResourcePlot_strategy)
def test_graph::resourceplot_max_type(instance):
    assert isinstance(instance.max, float)


@given(instance=graph::ResourcePlot_strategy)
def test_graph::resourceplot_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original

@given(instance=graph::ResourcePlot_strategy)
def test_graph::resourceplot_fit_type(instance):
    assert isinstance(instance.fit, str)


@given(instance=graph::ResourcePlot_strategy)
def test_graph::resourceplot_fit_setter(instance):
    original = instance.fit
    instance.fit = original
    assert instance.fit == original

@given(instance=graph::ResourceGraph_strategy)
@settings(max_examples=50)
def test_graph::resourcegraph_instantiation(instance):
    assert isinstance(instance, graph::ResourceGraph)

@given(instance=graph::ResourceGraph_strategy)
def test_graph::resourcegraph_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=graph::ResourceGraph_strategy)
def test_graph::resourcegraph_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=graph::ResourceGraphs_strategy)
@settings(max_examples=50)
def test_graph::resourcegraphs_instantiation(instance):
    assert isinstance(instance, graph::ResourceGraphs)
